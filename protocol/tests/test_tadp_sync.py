from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROTOCOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOCOL / "tools"))

from tadp_sync import Asset, apply_plan, digest, load_assets, load_state, make_plan, select_destination  # noqa: E402


class SynchronizationSafetyTests(unittest.TestCase):
    """Exercise preservation with real files, independently of Git/network access."""

    def write(self, root: Path, name: str, content: bytes) -> Path:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def snapshot(self, root: Path) -> dict[str, bytes]:
        return {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*")
            if path.is_file() and not path.is_symlink()
        }

    def apply(self, root: Path, assets: dict[str, Asset], revision: str = "a" * 40):
        plan = make_plan(root, assets, load_state(root))
        self.assertFalse(plan["conflicts"], plan["conflicts"])
        apply_plan(root, assets, plan, source="https://github.com/spkvfx/TADp.git",
                   revision=revision)
        return plan

    def refuse(self, root: Path, assets: dict[str, Asset]):
        before = self.snapshot(root)
        try:
            plan = make_plan(root, assets, load_state(root))
        except (ValueError, RuntimeError, OSError):
            pass
        else:
            self.assertTrue(plan["conflicts"], plan)
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                apply_plan(root, assets, plan,
                           source="https://github.com/spkvfx/TADp.git", revision="b" * 40)
        self.assertEqual(before, self.snapshot(root))

    def test_preview_does_not_write_files_or_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "user.txt", b"draft work\n")
            before = self.snapshot(root)
            plan = make_plan(root, {"tools/runtime.py": Asset(b"runtime\n")}, None)
            self.assertFalse(plan["conflicts"])
            self.assertEqual(before, self.snapshot(root))

    def test_install_creates_only_requested_assets_and_records_raw_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            content = b"runtime\r\n"
            self.apply(root, {"tools/runtime.py": Asset(content)})
            self.assertEqual(content, (root / "tools/runtime.py").read_bytes())
            state = load_state(root)
            self.assertEqual(digest(content), state["files"]["tools/runtime.py"]["sha256"])
            self.assertNotEqual(digest(content), digest(b"runtime\n"))

    def test_identical_repeat_apply_does_not_rewrite_state_or_create_backups(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            assets = {"tools/runtime.py": Asset(b"unchanged runtime\n")}
            self.apply(root, assets)
            before = self.snapshot(root)
            state_modified = (root / ".tadp-sync.json").stat().st_mtime_ns
            self.apply(root, assets)
            self.assertEqual(before, self.snapshot(root))
            self.assertEqual(state_modified, (root / ".tadp-sync.json").stat().st_mtime_ns)
            self.assertFalse((root / ".tadp-sync-backups").exists())

    def test_existing_project_scaffold_remains_user_owned(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            user_files = {
                "README.md": b"My application, not a blank scaffold\n",
                "AGENTS.md": b"My project instructions\n",
                "prompts/AGENTS.md": b"Project prompt rules\n",
                ".githooks/pre-commit": b"My existing hook\n",
            }
            for name, content in user_files.items():
                self.write(root, name, content)
            assets = {name: Asset(b"upstream seed\n", kind="seed") for name in user_files}
            self.apply(root, assets)
            for name, content in user_files.items():
                self.assertEqual(content, (root / name).read_bytes(), name)

    def test_user_customized_seed_survives_later_sync(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"README.md": Asset(b"scaffold\n", kind="seed")})
            self.write(root, "README.md", b"Now my actual project\n")
            self.apply(root, {"README.md": Asset(b"new scaffold\n", kind="seed")}, "b" * 40)
            self.assertEqual(b"Now my actual project\n", (root / "README.md").read_bytes())

    def test_unmanaged_collision_blocks_every_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "tools/runtime.py", b"user-owned implementation\n")
            self.refuse(root, {
                "tools/runtime.py": Asset(b"upstream runtime\n"),
                "tools/new.py": Asset(b"new upstream file\n"),
            })
            self.assertFalse((root / "tools/new.py").exists())
            self.assertFalse((root / ".tadp-sync.json").exists())

    def test_unchanged_managed_file_updates_with_retained_backup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n")})
            user_files = {
                "initiatives/my-initiative/README.md": b"partially performed user work\n",
                "products/user-product.txt": b"delivered work\n",
                "prompts/custom.md": b"a user prompt\n",
                "evidence/authoritative/user-rule.md": b"user authority\n",
                "untracked-draft.txt": b"a user draft\n",
            }
            for name, content in user_files.items():
                self.write(root, name, content)
            self.apply(root, {"tools/runtime.py": Asset(b"version two\n")}, "b" * 40)
            self.assertEqual(b"version two\n", (root / "tools/runtime.py").read_bytes())
            backups = [path for path in (root / ".tadp-sync-backups").rglob("*") if path.is_file()]
            self.assertTrue(any(path.read_bytes() == b"version one\n" for path in backups))
            for name, content in user_files.items():
                self.assertEqual(content, (root / name).read_bytes(), name)

    def test_user_edit_to_managed_file_blocks_update(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n")})
            self.write(root, "tools/runtime.py", b"version one plus user changes\n")
            self.refuse(root, {
                "tools/runtime.py": Asset(b"version two\n"),
                "tools/new.py": Asset(b"new file\n"),
            })

    def test_newline_only_user_edit_is_preserved_as_conflict(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n")})
            self.write(root, "tools/runtime.py", b"version one\r\n")
            self.refuse(root, {"tools/runtime.py": Asset(b"version two\n")})

    def test_locally_deleted_managed_file_is_not_recreated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n")})
            (root / "tools/runtime.py").unlink()
            self.refuse(root, {"tools/runtime.py": Asset(b"version two\n")})
            self.assertFalse((root / "tools/runtime.py").exists())

    def test_files_removed_upstream_are_retained_including_user_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {
                "tools/retired.py": Asset(b"old runtime\n"),
                "tools/runtime.py": Asset(b"current runtime\n"),
            })
            self.write(root, "tools/retired.py", b"user kept and extended this\n")
            self.apply(root, {"tools/runtime.py": Asset(b"current runtime\n")}, "b" * 40)
            self.assertEqual(b"user kept and extended this\n", (root / "tools/retired.py").read_bytes())

    def test_file_created_after_preview_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            assets = {"tools/runtime.py": Asset(b"upstream runtime\n")}
            plan = make_plan(root, assets, None)
            self.write(root, "tools/runtime.py", b"new user work after preview\n")
            before = self.snapshot(root)
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                apply_plan(root, assets, plan, source="source", revision="a" * 40)
            self.assertEqual(before, self.snapshot(root))

    def test_edit_after_preview_blocks_all_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n")})
            assets = {
                "tools/runtime.py": Asset(b"version two\n"),
                "tools/new.py": Asset(b"new file\n"),
            }
            plan = make_plan(root, assets, load_state(root))
            self.write(root, "tools/runtime.py", b"a concurrent user edit\n")
            before = self.snapshot(root)
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                apply_plan(root, assets, plan, source="source", revision="b" * 40)
            self.assertEqual(before, self.snapshot(root))

    def test_changed_sync_state_after_preview_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n")})
            assets = {"tools/runtime.py": Asset(b"version two\n")}
            plan = make_plan(root, assets, load_state(root))
            state_path = root / ".tadp-sync.json"
            state_path.write_bytes(state_path.read_bytes() + b" \n")
            before = self.snapshot(root)
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                apply_plan(root, assets, plan, source="source", revision="b" * 40)
            self.assertEqual(before, self.snapshot(root))

    def test_existing_sync_lock_is_preserved_and_blocks_every_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            assets = {"tools/runtime.py": Asset(b"upstream runtime\n")}
            plan = make_plan(root, assets, None)
            self.write(root, ".tadp-sync.lock", b"another process or retained user evidence\n")
            before = self.snapshot(root)
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                apply_plan(root, assets, plan, source="source", revision="a" * 40)
            self.assertEqual(before, self.snapshot(root))
            self.assertFalse((root / "tools/runtime.py").exists())

    @unittest.skipIf(os.name == "nt", "Windows chmod does not expose POSIX execution modes")
    def test_updates_preserve_locally_selected_permissions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, {"tools/runtime.py": Asset(b"version one\n", mode=0o644)})
            target = root / "tools/runtime.py"
            target.chmod(0o700)
            self.apply(root, {"tools/runtime.py": Asset(b"version two\n", mode=0o755)}, "b" * 40)
            self.assertEqual(0o700, stat.S_IMODE(target.stat().st_mode))
            backups = [path for path in (root / ".tadp-sync-backups").rglob("*")
                       if path.is_file() and path.read_bytes() == b"version one\n"]
            self.assertTrue(backups)
            self.assertTrue(all(stat.S_IMODE(path.stat().st_mode) == 0o700 for path in backups))

    def test_malformed_state_never_becomes_overwrite_authority(self):
        for value in (b"not JSON\n", b"[]\n", b'{"schema_version":99,"files":{}}\n'):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                self.write(root, ".tadp-sync.json", value)
                before = self.snapshot(root)
                with self.assertRaises((ValueError, RuntimeError, OSError)):
                    load_state(root)
                self.assertEqual(before, self.snapshot(root))

    def test_state_cannot_name_paths_outside_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = {
                "schema_version": 1, "source": "source", "revision": "a" * 40,
                "files": {"../outside.txt": {"sha256": "a" * 64, "kind": "managed"}},
            }
            self.write(root, ".tadp-sync.json", json.dumps(value).encode())
            with self.assertRaises((ValueError, RuntimeError, OSError)):
                load_state(root)

    def test_traversal_and_git_metadata_assets_are_refused(self):
        for path in ("../outside.txt", "/absolute.txt", "tools/../../outside.txt",
                     "C:/outside.txt", ".git/config", "tools\\escape.py"):
            with self.subTest(path=path), tempfile.TemporaryDirectory() as directory:
                self.refuse(Path(directory), {path: Asset(b"untrusted source\n")})

    def test_case_colliding_assets_are_refused_on_every_platform(self):
        with tempfile.TemporaryDirectory() as directory:
            self.refuse(Path(directory), {
                "tools/runtime.py": Asset(b"one\n"),
                "tools/Runtime.py": Asset(b"another\n"),
            })

    def test_case_colliding_parent_directories_are_refused_before_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            self.refuse(Path(directory), {
                "Tools/first.py": Asset(b"one\n"),
                "tools/second.py": Asset(b"another\n"),
            })

    def test_user_file_blocking_directory_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "tools", b"a user file named tools\n")
            self.refuse(root, {"tools/runtime.py": Asset(b"upstream\n")})

    def test_symlink_parent_never_writes_outside_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root, outside = parent / "repo", parent / "outside"
            root.mkdir()
            outside.mkdir()
            try:
                (root / "tools").symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("creating symbolic links is unavailable")
            self.refuse(root, {"tools/runtime.py": Asset(b"untrusted\n")})
            self.assertEqual([], list(outside.iterdir()))

    def protected_assets(self, content: bytes) -> dict[str, Asset]:
        lock = {
            "schema_version": 1, "algorithm": "sha256-canonical-v1",
            "protected_root": "template", "authority": "Fixture protected source revision",
            "files": {"record.md": digest(content)},
        }
        return {
            "template/record.md": Asset(content),
            "template/.tadp-lock.json": Asset(json.dumps(lock, sort_keys=True).encode() + b"\n"),
        }

    def test_existing_protected_source_update_requires_exact_authority_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, self.protected_assets(b"source one\n"))
            assets = self.protected_assets(b"source two\n")
            plan = make_plan(root, assets, load_state(root))
            before = self.snapshot(root)
            with self.assertRaisesRegex(ValueError, "authority"):
                apply_plan(root, assets, plan, source="source", revision="b" * 40)
            self.assertEqual(before, self.snapshot(root))
            apply_plan(root, assets, plan, source="source", revision="b" * 40,
                       authority="Fixture human authorizes source-two revision")
            self.assertEqual(b"source two\n", (root / "template/record.md").read_bytes())

    def test_local_addition_to_protected_tree_blocks_lock_replacement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, self.protected_assets(b"source one\n"))
            self.write(root, "template/user-source.md", b"a user-created source\n")
            self.refuse(root, self.protected_assets(b"source two\n"))

    def test_protected_addition_after_preview_blocks_every_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, self.protected_assets(b"source one\n"))
            assets = self.protected_assets(b"source two\n")
            assets["tools/new.py"] = Asset(b"new runtime\n")
            plan = make_plan(root, assets, load_state(root))
            self.assertFalse(plan["conflicts"])
            self.write(root, "template/new-user-source.md", b"created after preview\n")
            before = self.snapshot(root)
            with self.assertRaisesRegex(ValueError, "changed"):
                apply_plan(root, assets, plan, source="source", revision="b" * 40,
                           authority="Fixture authorizes source-two revision")
            self.assertEqual(before, self.snapshot(root))

    def test_later_updates_preserve_authority_revision_and_backup_history(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = "https://github.com/spkvfx/TADp.git"
            self.apply(root, self.protected_assets(b"source one\n"))
            assets_two = self.protected_assets(b"source two\n")
            plan_two = make_plan(root, assets_two, load_state(root))
            apply_plan(root, assets_two, plan_two, source=source, revision="b" * 40,
                       authority="Fixture human approves source two")
            state_two = load_state(root)
            history_two = state_two["history"]
            self.assertTrue(any(entry.get("authority") == "Fixture human approves source two"
                                and entry.get("revision") == "b" * 40 for entry in history_two))
            old_backup = root / ".tadp-sync-backups" / state_two["backup"] / "template/record.md"
            self.assertEqual(b"source one\n", old_backup.read_bytes())
            assets_three = self.protected_assets(b"source three\n")
            plan_three = make_plan(root, assets_three, load_state(root))
            apply_plan(root, assets_three, plan_three, source=source, revision="c" * 40,
                       authority="Fixture human approves source three")
            state_three = load_state(root)
            self.assertEqual(history_two, state_three["history"][:len(history_two)])
            self.assertEqual(b"source one\n", old_backup.read_bytes())
            self.assertEqual("Fixture human approves source three", state_three["history"][-1]["authority"])
            self.assertEqual("c" * 40, state_three["history"][-1]["revision"])

    def test_upstream_removal_from_protected_tree_is_retained_and_blocks_new_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.apply(root, self.protected_assets(b"source one\n"))
            next_lock = {
                "schema_version": 1, "algorithm": "sha256-canonical-v1",
                "protected_root": "template", "authority": "Fixture next revision", "files": {},
            }
            self.refuse(root, {"template/.tadp-lock.json": Asset(json.dumps(next_lock).encode() + b"\n")})
            self.assertEqual(b"source one\n", (root / "template/record.md").read_bytes())


class CommittedDistributionTests(unittest.TestCase):
    """Check actual Git blobs without executing or checking out upstream code."""

    def git(self, root: Path, *arguments: str, data: bytes | None = None) -> bytes:
        result = subprocess.run(
            ("git", "-c", "core.hooksPath=", "-c", "commit.gpgsign=false",
             "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", *arguments),
            cwd=root, input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
        )
        return result.stdout

    def fixture_files(self) -> dict[str, bytes]:
        files = {
            "protocol/template/AGENTS.md": b"# Reusable source rules\n",
            "protocol/template/project/AGENTS.md": b"# Project instructions\n",
            "protocol/template/project/README.md": b"# Project scaffold\n",
            "protocol/template/project/.githooks/pre-commit": b"#!/bin/sh\nexit 0\n",
            "protocol/template/prompts/00_initiative_preparation.md": b"# Preparation\n",
            "protocol/evidence/authoritative/LLM/AGENTS.md": b"# Protected suite\n",
            "protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md": b"# Keywords\n",
            "protocol/docs/development/private-development-notes.md": b"EXCLUDED development report\n",
            "protocol/decisions/private-decision.md": b"EXCLUDED historical development decision\n",
            "protocol/initiatives/private-initiative/README.md": b"EXCLUDED development initiative\n",
            "protocol/products/private-product.txt": b"EXCLUDED development product\n",
            "protocol/evidence/non-authoritative/realizations/private.md": b"EXCLUDED development realization\n",
        }
        for name in ("tadp_validate.py", "tadp_protect.py", "tadp_keywords.py",
                     "tadp_scopes.py", "tadp_templates.py"):
            files["protocol/tools/" + name] = b"# runtime tool fixture, never executed\n"
        self.refresh_fixture_locks(files)
        return files

    def refresh_fixture_locks(self, files: dict[str, bytes]) -> None:
        for protected in ("template", "evidence/authoritative/LLM"):
            prefix = "protocol/" + protected + "/"
            lock_name = prefix + ".tadp-lock.json"
            content_hashes = {
                name[len(prefix):]: digest(content)
                for name, content in files.items()
                if name.startswith(prefix) and name != lock_name
            }
            files[lock_name] = json.dumps({
                "schema_version": 1, "algorithm": "sha256-canonical-v1",
                "protected_root": protected, "authority": "Fixture source authority",
                "files": content_hashes,
            }, sort_keys=True).encode() + b"\n"

    def commit_fixture(self, root: Path, files: dict[str, bytes]) -> str:
        self.git(root, "init", "--quiet")
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        self.git(root, "add", "--", ".")
        self.git(root, "commit", "--quiet", "-m", "isolated template source")
        return self.git(root, "rev-parse", "HEAD").decode().strip()

    def sync(self, cwd: Path, source: Path, revision: str, *arguments: str):
        return subprocess.run(
            (sys.executable, str(PROTOCOL / "tools/tadp_sync.py"), "--source", str(source),
             "--ref", revision, "--json", *arguments),
            cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )

    def installation_fixture_files(self) -> dict[str, bytes]:
        files = self.fixture_files()
        for name in ("prompts/AGENTS.md", "prompts/README.md", "initiatives/README.md", "products/README.md"):
            files["protocol/template/project/" + name] = b"# Installed fixture marker\n"
        files["protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md"] = b"# Suite fixture marker\n"
        self.refresh_fixture_locks(files)
        return files

    def test_nested_default_and_explicit_target_preserve_parent_sibling_and_index(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            source, outer = Path(source_dir).resolve(), Path(target_dir).resolve()
            revision = self.commit_fixture(source, self.installation_fixture_files())
            self.git(outer, "init", "--quiet")
            parent = outer / "AGENTS.md"
            parent.write_bytes(b"parent instructions\n")
            sibling = outer / "sibling/AGENTS.md"
            sibling.parent.mkdir()
            sibling.write_bytes(b"sibling instructions\n")
            staged = outer / "unrelated.txt"
            staged.write_bytes(b"unrelated staged work\n")
            self.git(outer, "add", "--", "unrelated.txt")
            index_before = self.git(outer, "diff", "--cached", "--binary")
            project = outer / "projects/nested"
            project.mkdir(parents=True)
            before = sorted(p.relative_to(outer).as_posix() for p in outer.rglob("*") if ".git" not in p.parts)
            preview = self.sync(project, source, revision)
            self.assertEqual(0, preview.returncode, preview.stderr.decode())
            result = json.loads(preview.stdout)
            self.assertEqual(str(project), result["project_root"])
            self.assertEqual(str(outer), result["git_root"])
            self.assertFalse(result["applied"])
            self.assertEqual(before, sorted(p.relative_to(outer).as_posix() for p in outer.rglob("*") if ".git" not in p.parts))
            applied = self.sync(outer, source, revision, "--target", "projects/nested", "--apply")
            self.assertEqual(0, applied.returncode, applied.stderr.decode())
            self.assertTrue(json.loads(applied.stdout)["applied"])
            state = load_state(project)
            self.assertEqual(str(project), state["project_root"])
            self.assertEqual(str(outer), state["git_root"])
            self.assertTrue((project / "template/.tadp-lock.json").is_file())
            self.assertFalse((outer / ".tadp-sync.json").exists())
            self.assertFalse((project / ".tadp-sync.lock").exists())
            state_bytes = (project / ".tadp-sync.json").read_bytes()
            repeated = self.sync(project, source, revision, "--apply")
            self.assertEqual(0, repeated.returncode, repeated.stderr.decode())
            self.assertEqual(state_bytes, (project / ".tadp-sync.json").read_bytes())
            self.assertFalse((project / ".tadp-sync-backups").exists())
            self.assertEqual(b"parent instructions\n", parent.read_bytes())
            self.assertEqual(b"sibling instructions\n", sibling.read_bytes())
            self.assertEqual(index_before, self.git(outer, "diff", "--cached", "--binary"))

    def test_git_root_installation_cli_remains_supported(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            source, root = Path(source_dir).resolve(), Path(target_dir).resolve()
            revision = self.commit_fixture(source, self.installation_fixture_files())
            self.git(root, "init", "--quiet")
            result = self.sync(root, source, revision, "--apply")
            self.assertEqual(0, result.returncode, result.stderr.decode())
            payload = json.loads(result.stdout)
            self.assertEqual(str(root), payload["project_root"])
            self.assertEqual(str(root), payload["git_root"])
            self.assertTrue((root / ".tadp-sync.json").is_file())

    def test_destination_selection_never_redirects_and_requires_git_and_existing_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            outer = Path(directory).resolve()
            empty = outer / "empty"
            empty.mkdir()
            with self.assertRaises(ValueError):
                select_destination(empty)
            self.git(outer, "init", "--quiet")
            self.assertEqual((empty, outer), select_destination(empty))
            with self.assertRaisesRegex(ValueError, "existing directory"):
                select_destination(outer / "missing")
            self.assertFalse((outer / "missing").exists())

    def test_linked_worktree_supports_nested_installation(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as source_dir:
            base = Path(directory).resolve()
            original = base / "original"
            original.mkdir()
            self.commit_fixture(original, {"sentinel.txt": b"worktree fixture\n"})
            linked = base / "linked"
            self.git(original, "worktree", "add", "--quiet", "--detach", str(linked), "HEAD")
            self.assertTrue((linked / ".git").is_file())
            sentinel = (linked / "sentinel.txt").read_bytes()
            project = linked / "projects/p"
            project.mkdir(parents=True)
            self.assertEqual((project, linked), select_destination(project))
            source = Path(source_dir).resolve()
            revision = self.commit_fixture(source, self.installation_fixture_files())
            result = self.sync(original, source, revision, "--target", str(project), "--apply")
            self.assertEqual(0, result.returncode, result.stderr.decode())
            self.assertEqual(str(linked), json.loads(result.stdout)["git_root"])
            self.assertTrue((project / ".tadp-sync.json").is_file())
            self.assertEqual(sentinel, (linked / "sentinel.txt").read_bytes())

    def test_nested_updates_keep_backups_and_metadata_beneath_project(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            source, outer = Path(source_dir).resolve(), Path(target_dir).resolve()
            files = self.installation_fixture_files()
            revision = self.commit_fixture(source, files)
            self.git(outer, "init", "--quiet")
            project = outer / "nested"
            project.mkdir()
            first = self.sync(outer, source, revision, "--target", "nested", "--apply")
            self.assertEqual(0, first.returncode, first.stderr.decode())
            prior = (project / "tools/tadp_validate.py").read_bytes()
            files["protocol/tools/tadp_validate.py"] = b"# updated runtime fixture\n"
            updated_revision = self.commit_fixture(source, files)
            update = self.sync(outer, source, updated_revision, "--target", "nested", "--apply")
            self.assertEqual(0, update.returncode, update.stderr.decode())
            state = load_state(project)
            backup = project / ".tadp-sync-backups" / state["backup"] / "tools/tadp_validate.py"
            self.assertEqual(prior, backup.read_bytes())
            self.assertEqual(b"# updated runtime fixture\n", (project / "tools/tadp_validate.py").read_bytes())
            self.assertFalse((outer / ".tadp-sync-backups").exists())
            self.assertFalse((outer / ".tadp-sync.lock").exists())
            self.assertFalse((project / ".tadp-sync.lock").exists())

    def test_installed_context_rejects_ambiguous_cwd_and_missing_markers(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            source, root = Path(source_dir).resolve(), Path(target_dir).resolve()
            revision = self.commit_fixture(source, self.installation_fixture_files())
            self.git(root, "init", "--quiet")
            install = self.sync(root, source, revision, "--apply")
            self.assertEqual(0, install.returncode, install.stderr.decode())
            child = root / "new-child"
            child.mkdir()
            ambiguous = self.sync(child, source, revision)
            self.assertEqual(2, ambiguous.returncode)
            self.assertIn(b"beneath an installed project", ambiguous.stderr)
            self.assertFalse(list(child.iterdir()))
            # An explicit target is a deliberate independent installation choice.
            explicit = self.sync(root, source, revision, "--target", "new-child")
            self.assertEqual(0, explicit.returncode, explicit.stderr.decode())
            installed = self.sync(root, source, revision, "--target", "new-child", "--apply")
            self.assertEqual(0, installed.returncode, installed.stderr.decode())
            nested_default = self.sync(child, source, revision)
            self.assertEqual(0, nested_default.returncode, nested_default.stderr.decode())
            self.assertEqual(str(child), json.loads(nested_default.stdout)["project_root"])
            (root / "prompts/README.md").unlink()
            malformed = self.sync(root, source, revision)
            self.assertEqual(2, malformed.returncode)
            self.assertIn(b"malformed installed scaffold", malformed.stderr)
            self.assertFalse((root / "prompts/README.md").exists())

    def test_current_distribution_nested_install_validates_and_preserves_sibling_index(self):
        # Exercise the actual locked distribution and its installed runtime,
        # rather than promoting the reference project's live records to fixtures.
        files = {}
        for prefix in ("template", "evidence/authoritative/LLM"):
            for path in (PROTOCOL / prefix).rglob("*"):
                if path.is_file() and "__pycache__" not in path.parts:
                    files["protocol/" + path.relative_to(PROTOCOL).as_posix()] = path.read_bytes()
        for path in (PROTOCOL / "tools").glob("tadp_*.py"):
            files["protocol/tools/" + path.name] = path.read_bytes()
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            source, outer = Path(source_dir).resolve(), Path(target_dir).resolve()
            revision = self.commit_fixture(source, files)
            self.git(outer, "init", "--quiet")
            sibling = outer / "sibling/sentinel.txt"
            sibling.parent.mkdir()
            sibling.write_bytes(b"unrelated staged sibling\n")
            self.git(outer, "add", "--", "sibling/sentinel.txt")
            staged = self.git(outer, "diff", "--cached", "--binary")
            sentinel = sibling.read_bytes()
            project = outer / "projects/current"
            project.mkdir(parents=True)
            preview = self.sync(outer, source, revision, "--target", "projects/current")
            self.assertEqual(0, preview.returncode, preview.stderr.decode())
            self.assertFalse(list(project.iterdir()))
            apply = self.sync(outer, source, revision, "--target", "projects/current", "--apply")
            self.assertEqual(0, apply.returncode, apply.stderr.decode())
            self.assertFalse((outer / "AGENTS.md").exists())
            self.assertFalse((outer / ".tadp-sync.json").exists())
            for tool, arguments in (("tadp_protect.py", ("check", ".")), ("tadp_validate.py", (".",))):
                result = subprocess.run((sys.executable, str(project / "tools" / tool), *arguments),
                                        cwd=project, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.assertEqual(0, result.returncode, result.stdout.decode() + result.stderr.decode())
            state = (project / ".tadp-sync.json").read_bytes()
            repeat = self.sync(project, source, revision, "--apply")
            self.assertEqual(0, repeat.returncode, repeat.stderr.decode())
            self.assertEqual(state, (project / ".tadp-sync.json").read_bytes())
            self.assertEqual(sentinel, sibling.read_bytes())
            self.assertEqual(staged, self.git(outer, "diff", "--cached", "--binary"))

    def test_conflicting_installation_identity_blocks_before_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            outer = Path(directory).resolve()
            self.git(outer, "init", "--quiet")
            project = outer / "project"
            project.mkdir()
            state = dict(schema_version=1, source="source", revision="a" * 40,
                         files={}, project_root=str(outer), git_root=str(outer))
            path = project / ".tadp-sync.json"
            path.write_text(json.dumps(state), encoding="utf-8")
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, "contradicts"):
                select_destination(project)
            self.assertEqual(before, path.read_bytes())
            state.pop("project_root")
            state.pop("git_root")
            path.write_text(json.dumps(state), encoding="utf-8")
            self.assertEqual((project, outer), select_destination(project))

    def test_protected_template_source_is_not_an_installation_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            outer = Path(directory).resolve()
            self.commit_fixture(outer, self.fixture_files())
            with self.assertRaisesRegex(ValueError, "protected reusable source"):
                select_destination(outer / "protocol/template/project")

    def test_manually_installed_scaffold_requires_complete_markers_without_sync_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            self.git(root, "init", "--quiet")
            (root / "AGENTS.md").write_bytes(b"unrelated project instructions\n")
            self.assertEqual((root, root), select_destination(root))
            index = root / "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md"
            index.parent.mkdir(parents=True)
            index.write_bytes(b"installed suite marker\n")
            with self.assertRaisesRegex(ValueError, "malformed installed scaffold"):
                select_destination(root)
            for name in ("prompts/AGENTS.md", "prompts/README.md"):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"installed marker\n")
            for name in ("initiatives", "products", "template", "tools"):
                (root / name).mkdir()
            self.assertEqual((root, root), select_destination(root))
            self.assertFalse((root / ".tadp-sync.json").exists())
            index.unlink()
            with self.assertRaisesRegex(ValueError, "malformed installed scaffold"):
                select_destination(root)

    def test_destination_symlink_is_rejected_without_touching_target(self):
        with tempfile.TemporaryDirectory() as directory:
            outer = Path(directory).resolve()
            self.git(outer, "init", "--quiet")
            real = outer / "real"
            real.mkdir()
            alias = outer / "alias"
            try:
                alias.symlink_to(real, target_is_directory=True)
            except OSError:
                self.skipTest("symlinks unavailable on this platform")
            with self.assertRaisesRegex(ValueError, "symlink or junction"):
                select_destination(alias)
            self.assertFalse(list(real.iterdir()))

    def test_managed_paths_cannot_cross_nested_repository_or_scaffold(self):
        for boundary in ("git", "scaffold"):
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                other = root / "tools"
                other.mkdir()
                if boundary == "git":
                    (other / ".git").write_text("gitdir: elsewhere\n", encoding="utf-8")
                else:
                    for name in ("AGENTS.md", "prompts/AGENTS.md", "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md"):
                        path = other / name
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_bytes(b"other project\n")
                with self.assertRaisesRegex(ValueError, "nested Git|another installed scaffold"):
                    make_plan(root, {"tools/runtime.py": Asset(b"runtime\n")}, None)
                self.assertFalse((other / "runtime.py").exists())

    def test_load_selects_template_and_runtime_without_development_records(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            revision = self.commit_fixture(root, self.fixture_files())
            assets = load_assets(root, revision)
            self.assertIn("template/project/README.md", assets)
            self.assertEqual("seed", assets["README.md"].kind)
            self.assertEqual("seed", assets[".githooks/pre-commit"].kind)
            self.assertIn("tools/tadp_validate.py", assets)
            self.assertIn("evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md", assets)
            self.assertFalse(any(b"EXCLUDED" in asset.content for asset in assets.values()))
            self.assertFalse(any(name.startswith(("docs/development/", "decisions/", "products/"))
                                 for name in assets))

    def test_uncommitted_source_changes_are_not_imported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            revision = self.commit_fixture(root, self.fixture_files())
            path = root / "protocol/template/project/README.md"
            path.write_bytes(b"uncommitted source changes\n")
            assets = load_assets(root, revision)
            self.assertEqual(b"# Project scaffold\n", assets["README.md"].content)

    def test_project_template_placeholder_does_not_overlay_installed_library(self):
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source = Path(source_directory)
            target = Path(target_directory)
            files = self.fixture_files()
            files["protocol/template/README.md"] = b"# Complete reusable library\n"
            files["protocol/template/project/template/README.md"] = b"# Install the complete library here, once\n"
            self.refresh_fixture_locks(files)
            revision = self.commit_fixture(source, files)
            assets = load_assets(source, revision)
            self.assertEqual(b"# Complete reusable library\n", assets["template/README.md"].content)
            self.assertEqual(b"# Install the complete library here, once\n",
                             assets["template/project/template/README.md"].content)
            plan = make_plan(target, assets, None)
            self.assertFalse(plan["conflicts"])
            apply_plan(target, assets, plan, source=str(source), revision=revision)
            self.assertEqual(b"# Complete reusable library\n", (target / "template/README.md").read_bytes())
            self.assertTrue((target / "template/project/template/README.md").is_file())
            self.assertFalse((target / "template/template").exists())
            self.assertEqual(["README.md"], sorted(path.name for path in (target / "template/project/template").iterdir()))

    def test_project_template_rejects_recursive_or_extra_payload(self):
        for extra in ("template/README.md", "project/README.md", "notes.md", "README.template.md"):
            with self.subTest(extra=extra), tempfile.TemporaryDirectory() as directory:
                source = Path(directory)
                files = self.fixture_files()
                files["protocol/template/project/template/README.md"] = b"# Nonrecursive placeholder\n"
                files["protocol/template/project/template/" + extra] = b"nested or extra payload\n"
                self.refresh_fixture_locks(files)
                revision = self.commit_fixture(source, files)
                with self.assertRaisesRegex(ValueError, "nonrecursive"):
                    load_assets(source, revision)

    def test_record_templates_are_copied_verbatim_without_creating_live_records(self):
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source = Path(source_directory)
            target = Path(target_directory)
            files = self.fixture_files()
            content = b"# {{initiative_name}} architecture\n\n{{required_evidence}}\n"
            files["protocol/template/project/initiatives/architecture.template.md"] = content
            files["protocol/template/project/initiatives/README.md"] = b"# Initiative baseline navigation\n"
            self.refresh_fixture_locks(files)
            revision = self.commit_fixture(source, files)
            assets = load_assets(source, revision)
            self.assertEqual("seed", assets["initiatives/architecture.template.md"].kind)
            self.assertEqual(content, assets["initiatives/architecture.template.md"].content)
            self.assertEqual(content, assets["template/project/initiatives/architecture.template.md"].content)
            plan = make_plan(target, assets, None)
            apply_plan(target, assets, plan, source=str(source), revision=revision)
            self.assertEqual(content, (target / "initiatives/architecture.template.md").read_bytes())
            self.assertEqual(b"# Initiative baseline navigation\n", (target / "initiatives/README.md").read_bytes())
            self.assertFalse((target / "initiatives/architecture.md").exists())
            self.assertFalse((target / "initiatives/v1").exists())

    def test_older_distribution_without_unused_optional_tools_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = self.fixture_files()
            for optional in ("tadp_keywords.py", "tadp_scopes.py", "tadp_templates.py"):
                files.pop("protocol/tools/" + optional)
            files["protocol/tools/tadp_protect.py"] = b"from tadp_validate import validate\n"
            revision = self.commit_fixture(root, files)
            assets = load_assets(root, revision)
            self.assertIn("tools/tadp_validate.py", assets)
            self.assertIn("tools/tadp_protect.py", assets)
            self.assertNotIn("tools/tadp_templates.py", assets)

    def test_missing_actual_runtime_import_is_rejected_without_execution(self):
        for code in (b"import tadp_missing\n", b"from tadp_missing import validate\n"):
            with self.subTest(code=code), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                files = self.fixture_files()
                files["protocol/tools/tadp_validate.py"] = code + b"raise AssertionError('must not execute')\n"
                revision = self.commit_fixture(root, files)
                with self.assertRaisesRegex(ValueError, "dependency.*tadp_missing"):
                    load_assets(root, revision)

    def test_drifted_upstream_lock_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = self.fixture_files()
            files["protocol/template/project/README.md"] = b"changed without authorized lock\n"
            revision = self.commit_fixture(root, files)
            with self.assertRaisesRegex(ValueError, "lock"):
                load_assets(root, revision)

    def test_development_documents_embedded_in_template_are_rejected(self):
        for excluded in ("docs/development/maintenance-report.md", "decisions/history.md"):
            with self.subTest(excluded=excluded), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                files = self.fixture_files()
                files["protocol/template/project/" + excluded] = b"forbidden deployment content\n"
                self.refresh_fixture_locks(files)
                revision = self.commit_fixture(root, files)
                with self.assertRaisesRegex(ValueError, "development"):
                    load_assets(root, revision)

    def test_new_project_baseline_copies_operational_guides_verbatim(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = self.fixture_files()
            files["protocol/template/project/template/README.md"] = b"# Nonrecursive project library placeholder\n"
            operational = (
                "README.md", "getting-started.md", "architecture-and-authority.md",
                "repository-layout.md", "initiative-workflow.md", "git-and-codex-requirements.md",
                "validation-and-quality.md", "adapting-other-tools.md",
            )
            for name in operational:
                files["protocol/template/project/docs/development/" + name] = ("# Project-use " + name + "\n").encode()
            self.refresh_fixture_locks(files)
            revision = self.commit_fixture(root, files)
            assets = load_assets(root, revision)
            for name in operational:
                source = "protocol/template/project/docs/development/" + name
                self.assertEqual(files[source], assets["docs/development/" + name].content)
                self.assertEqual(files[source], assets["template/project/docs/development/" + name].content)
                self.assertEqual("seed", assets["docs/development/" + name].kind)
            self.assertFalse(any(b"EXCLUDED" in asset.content for asset in assets.values()))

    def test_new_project_baseline_rejects_development_work_and_unknown_guides(self):
        for excluded in ("documentation-review-20261113.md", "template-prerequisites-maintenance.md",
                         "developing-tadp.md", "protocol-history.md", "other/README.md"):
            with self.subTest(excluded=excluded), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                files = self.fixture_files()
                files["protocol/template/project/template/README.md"] = b"# Nonrecursive placeholder\n"
                files["protocol/template/project/docs/development/" + excluded] = b"excluded source work\n"
                self.refresh_fixture_locks(files)
                revision = self.commit_fixture(root, files)
                with self.assertRaisesRegex(ValueError, "development"):
                    load_assets(root, revision)

    def test_decisions_navigation_is_copied_but_development_receipts_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = self.fixture_files()
            navigation = b"# Project decisions\n\nCreate receipts only for actual project decisions.\n"
            files["protocol/template/project/template/README.md"] = b"# Nonrecursive placeholder\n"
            files["protocol/template/project/decisions/README.md"] = navigation
            self.refresh_fixture_locks(files)
            revision = self.commit_fixture(root, files)
            assets = load_assets(root, revision)
            self.assertEqual(navigation, assets["decisions/README.md"].content)
            self.assertNotIn("decisions/private-decision.md", assets)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files["protocol/template/project/decisions/DR-001-maintenance.md"] = b"actual development receipt\n"
            self.refresh_fixture_locks(files)
            revision = self.commit_fixture(root, files)
            with self.assertRaisesRegex(ValueError, "development"):
                load_assets(root, revision)

    def test_committed_symlink_is_rejected_without_creating_local_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.commit_fixture(root, self.fixture_files())
            object_id = self.git(root, "hash-object", "-w", "--stdin", data=b"../../outside.txt").decode().strip()
            self.git(root, "update-index", "--add", "--cacheinfo",
                     "120000," + object_id + ",protocol/template/project/README.md")
            self.git(root, "commit", "--quiet", "-m", "source link fixture")
            revision = self.git(root, "rev-parse", "HEAD").decode().strip()
            with self.assertRaisesRegex(ValueError, "links"):
                load_assets(root, revision)


if __name__ == "__main__":
    unittest.main()
