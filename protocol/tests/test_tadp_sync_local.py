from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PROTOCOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOCOL / "tools"))

import tadp_sync as sync  # noqa: E402


class LocalTemplateSynchronizationTests(unittest.TestCase):
    """Exercise authority selection without touching the repository's library."""

    def git(self, root: Path, *arguments: str) -> bytes:
        return subprocess.run(
            ("git", "-c", "core.hooksPath=", "-c", "commit.gpgsign=false",
             "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
             *arguments), cwd=root, check=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout

    def files(self, label: str) -> dict[str, bytes]:
        content = (label + "\n").encode()
        files = {
            "AGENTS.md": b"# Reusable source rules\n",
            "README.md": b"# Reusable library\n" + content,
            "project/AGENTS.md": b"# Project instructions\n",
            "project/README.md": content,
            "project/prompts/AGENTS.md": b"# Prompt instructions\n",
            "project/prompts/README.md": b"# Project prompts\n",
            "project/initiatives/README.md": b"# Initiatives\n",
            "project/products/README.md": b"# Products\n",
            "project/template/README.md": b"# Nonrecursive placeholder\n",
            "project/evidence/authoritative/LLM/AGENTS.md": b"# Suite rules\n",
            "project/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md": b"# Suite\n",
            "project/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md": b"# Keywords\n",
        }
        for name in sync.RUNTIME_TOOLS:
            files["project/tools/" + name] = b"# Fixture tool; never execute.\n" + b"# " + content
        self.refresh_locks(files)
        return files

    def refresh_locks(self, files: dict[str, bytes]) -> None:
        suite = "project/evidence/authoritative/LLM/"
        suite_lock = suite + ".tadp-lock.json"
        files[suite_lock] = self.lock(
            "evidence/authoritative/LLM",
            {name[len(suite):]: content for name, content in files.items()
             if name.startswith(suite) and name != suite_lock},
        )
        files[".tadp-lock.json"] = self.lock(
            "template", {name: content for name, content in files.items()
                         if name != ".tadp-lock.json"},
        )

    def lock(self, protected: str, files: dict[str, bytes]) -> bytes:
        return (json.dumps({
            "schema_version": 1, "algorithm": "sha256-canonical-v1",
            "protected_root": protected, "authority": "Fixture source authority",
            "files": {name: sync.canonical_digest(content) for name, content in files.items()},
        }, sort_keys=True) + "\n").encode()

    def write(self, root: Path, files: dict[str, bytes]) -> None:
        root.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)

    def snapshot(self, root: Path) -> dict[str, bytes]:
        return {path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file() and ".git" not in path.relative_to(root).parts}

    def target(self, base: Path, name: str = "target") -> Path:
        target = base / name
        target.mkdir()
        self.git(target, "init", "--quiet")
        return target

    def remote(self, base: Path, label: str = "remote") -> tuple[Path, str]:
        remote = base / "remote"
        self.write(remote / "protocol/template", self.files(label))
        self.git(remote, "init", "--quiet")
        self.git(remote, "add", "--", ".")
        self.git(remote, "commit", "--quiet", "-m", "fixture distribution")
        return remote, self.git(remote, "rev-parse", "HEAD").decode().strip()

    def run_sync(self, local: Path, target: Path, *arguments: str):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = sync.main(["--local-template", str(local), "--target", str(target),
                                "--json", *arguments])
        result = json.loads(out.getvalue()) if out.getvalue() else None
        return status, result, err.getvalue()

    def test_local_apply_uses_current_template_without_fetching(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local working bytes"))
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, result, error = self.run_sync(local, target, "--apply")
            self.assertEqual(0, status, error)
            self.assertTrue(result["applied"])
            self.assertEqual(b"local working bytes\n", (target / "README.md").read_bytes())
            self.assertEqual(str(local), sync.load_state(target)["source"])

    def test_local_preview_preserves_library_target_and_state(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            before = self.snapshot(base)
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, result, error = self.run_sync(local, target)
            self.assertEqual(0, status, error)
            self.assertFalse(result["applied"])
            self.assertEqual(before, self.snapshot(base))
            self.assertFalse((target / sync.STATE).exists())

    def test_remote_preview_preserves_both_trees(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            remote, revision = self.remote(base)
            before = self.snapshot(base)
            status, result, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
            )
            self.assertEqual(0, status, error)
            self.assertFalse(result["applied"])
            self.assertEqual(revision, result["upstream_revision"])
            self.assertEqual(before, self.snapshot(base))

    def test_remote_refresh_is_reused_by_subsequent_local_sync(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            local_files = self.files("local")
            local_files["retired-source.md"] = b"old source retained in the library backup\n"
            self.refresh_locks(local_files)
            self.write(local, local_files)
            old_library = self.snapshot(local)
            remote, revision = self.remote(base)
            status, result, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                "--apply", "--authority", "Fixture human approves exact remote template revision",
            )
            self.assertEqual(0, status, error)
            self.assertTrue(result["applied"])
            self.assertEqual(b"remote\n", (local / "project/README.md").read_bytes())
            self.assertEqual(b"remote\n", (target / "README.md").read_bytes())
            self.assertEqual(self.snapshot(remote / "protocol/template"), self.snapshot(local))
            self.assertNotEqual(old_library, self.snapshot(local))
            self.assertEqual(old_library, self.snapshot(Path(result["template_backup"])))
            self.assertFalse((local / "retired-source.md").exists())
            second_target = self.target(base, "second-target")
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, result, error = self.run_sync(local, second_target, "--apply")
            self.assertEqual(0, status, error)
            self.assertEqual(b"remote\n", (second_target / "README.md").read_bytes())
            self.assertEqual(str(local), sync.load_state(target)["source"])
            self.assertEqual(str(local), sync.load_state(second_target)["source"])

    def test_refresh_existing_library_requires_authority_before_either_write(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            remote, revision = self.remote(base)
            before = self.snapshot(base)
            status, _, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision, "--apply",
            )
            self.assertEqual(2, status)
            self.assertIn("authority", error)
            self.assertEqual(before, self.snapshot(base))

    def test_target_conflict_prevents_local_refresh(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            self.write(target, {"tools/tadp_validate.py": b"user runtime customization\n"})
            remote, revision = self.remote(base)
            before = self.snapshot(base)
            status, result, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                "--apply", "--authority", "Fixture approves exact remote revision",
            )
            self.assertEqual(1, status, error)
            self.assertTrue(result["conflicts"])
            self.assertFalse(result["applied"])
            self.assertEqual(before, self.snapshot(base))

    def test_existing_installation_can_switch_authorities_without_source_change(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(0, status, error)
            remote, revision = self.remote(base)
            status, _, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                "--apply", "--authority", "Fixture approves exact remote revision",
            )
            self.assertEqual(0, status, error)
            self.assertEqual(str(local), sync.load_state(target)["source"])
            # Existing scaffold content remains project-owned during the managed update.
            self.assertEqual(b"local\n", (target / "README.md").read_bytes())
            self.assertIn(b"# remote\n", (target / "tools/tadp_validate.py").read_bytes())
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(0, status, error)

    def test_corrupt_local_template_blocks_sync_without_repair(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            (local / "project/README.md").write_bytes(b"unapproved protected drift\n")
            before = self.snapshot(base)
            status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(2, status)
            self.assertIn("lock", error)
            self.assertEqual(before, self.snapshot(base))

    def test_invalid_remote_template_preserves_local_and_target(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            remote, _ = self.remote(base)
            (remote / "protocol/template/project/README.md").write_bytes(b"remote drift\n")
            self.git(remote, "add", "--", ".")
            self.git(remote, "commit", "--quiet", "-m", "invalid fixture lock")
            revision = self.git(remote, "rev-parse", "HEAD").decode().strip()
            before = self.snapshot(base)
            status, _, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                "--apply", "--authority", "Fixture approves exact remote revision",
            )
            self.assertEqual(2, status)
            self.assertIn("lock", error)
            self.assertEqual(before, self.snapshot(base))

    def test_target_uses_its_own_template_for_local_and_remote_sync(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            target = self.target(base)
            local = target / "template"
            self.write(local, self.files("local"))
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(0, status, error)
            self.assertEqual(b"local\n", (target / "README.md").read_bytes())
            remote, revision = self.remote(base)
            status, result, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                "--apply", "--authority", "Fixture approves exact remote revision",
            )
            self.assertEqual(0, status, error)
            self.assertTrue(result["applied"])
            self.assertEqual(b"remote\n", (local / "project/README.md").read_bytes())
            self.assertEqual(b"local\n", (target / "README.md").read_bytes())
            self.assertIn(b"# remote\n", (target / "tools/tadp_validate.py").read_bytes())
            before = (target / sync.STATE).read_bytes()
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(0, status, error)
            self.assertEqual(before, (target / sync.STATE).read_bytes())

    def test_existing_target_lock_blocks_refresh_before_local_replacement(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            self.write(target, {sync.RUN_LOCK: b"another synchronization owns this lock\n"})
            remote, revision = self.remote(base)
            before = self.snapshot(base)
            status, _, error = self.run_sync(
                local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                "--apply", "--authority", "Fixture approves exact remote revision",
            )
            self.assertEqual(2, status)
            self.assertIn("lock", error)
            self.assertEqual(before, self.snapshot(base))

    def test_changed_refreshed_local_source_blocks_target_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            local, target = base / "library", self.target(base)
            self.write(local, self.files("local"))
            remote, revision = self.remote(base)
            before = self.snapshot(target)
            original_replace = sync.replace_template

            def concurrent_source_edit(*args, **kwargs):
                backup = original_replace(*args, **kwargs)
                (local / "project/README.md").write_bytes(b"concurrent protected-source drift\n")
                return backup

            with patch.object(sync, "replace_template", side_effect=concurrent_source_edit):
                status, _, error = self.run_sync(
                    local, target, "--refresh-template", "--source", str(remote), "--ref", revision,
                    "--apply", "--authority", "Fixture approves exact remote revision",
                )
            self.assertEqual(2, status)
            self.assertIn("lock", error)
            self.assertEqual(before, self.snapshot(target))

    def test_template_cannot_overlap_target_runtime_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            target = self.target(base)
            local = target / "tools"
            self.write(local, self.files("local"))
            before = self.snapshot(base)
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(2, status)
            self.assertTrue(error)
            self.assertEqual(before, self.snapshot(base))

    def test_template_cannot_be_nested_inside_another_protected_source(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            target = self.target(base)
            protected = base / "protected"
            self.write(protected, {".tadp-lock.json": b"parent protection must remain untouched\n"})
            local = protected / "child-library"
            self.write(local, self.files("local"))
            before = self.snapshot(base)
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, _, error = self.run_sync(local, target, "--apply")
            self.assertEqual(2, status)
            self.assertIn("protected", error)
            self.assertEqual(before, self.snapshot(base))

    def test_old_remote_install_can_adopt_its_local_library_without_stale_baselines(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory).resolve()
            target = self.target(base)
            source = base / "source-library"
            self.write(source, self.files("installed"))
            assets = sync.load_local_assets(source)
            plan = sync.make_plan(target, assets, None)
            sync.apply_plan(target, assets, plan, source=sync.DEFAULT_SOURCE,
                            revision="a" * 40, git_root=target)
            old_state = sync.load_state(target)
            self.assertTrue(any(name.startswith("template/") for name in old_state["files"]))
            local = target / "template"
            before = self.snapshot(local)
            with patch.object(sync, "fetch_source", side_effect=AssertionError("unexpected fetch")):
                status, result, error = self.run_sync(local, target, "--apply")
            self.assertEqual(0, status, error)
            self.assertTrue(result["applied"])
            state = sync.load_state(target)
            self.assertEqual(str(local), state["source"])
            self.assertFalse(any(name.startswith("template/") for name in state["files"]))
            self.assertEqual(before, self.snapshot(local))
            self.assertEqual(old_state["history"], state["history"][:len(old_state["history"])])


if __name__ == "__main__":
    unittest.main()
