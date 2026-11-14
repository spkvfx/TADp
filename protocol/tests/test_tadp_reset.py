from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import tadp_reset  # noqa: E402
from tadp_reset import apply_plan, main, make_plan  # noqa: E402
from tadp_validate import build_protected_lock, validate_protected_sources  # noqa: E402


class ResetSafetyTests(unittest.TestCase):
    """Run destructive operations only inside isolated fixture repositories."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="tadp-reset-test-")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name).resolve()
        self.root = self.directory / "project"
        self.root.mkdir()
        self.git("init", "--quiet")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Reset test fixture")
        self.scaffold = {
            "AGENTS.md": b"# Project instructions\n",
            "README.md": b"# Empty project\r\n",
            ".gitattributes": b"* text=auto\n",
            "project-profile.template.md": b"# Unpopulated profile source\n",
            "initiatives/README.md": b"# Initiatives\n",
            "products/README.md": b"# Products\n",
            "tests/README.md": b"# Project verification\n",
            "tools/README.md": b"# Runtime tools\n",
            "tools/tadp_validate.py": b"# Installed validator\n",
            "tools/tadp_protect.py": b"# Installed protection tool\n",
        }
        for name, content in self.scaffold.items():
            self.write("template/project/" + name, content)
            self.write(name, content)
        self.write("template/project/template/README.md", b"# Nonrecursive placeholder\n")
        self.write("template/README.md", b"# Complete reusable library\n")
        self.write("template/AGENTS.md", b"# Protected sources\n")
        self.write("evidence/authoritative/LLM/00_index.md", b"# Governing invariant suite\n")
        self.write("tools/tadp_reset.py", b"# Installed reset command survives its own apply\n")
        self.seal_sources()
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "Fixture baseline")

    def git(self, *arguments: str) -> bytes:
        result = subprocess.run(
            ("git", "-c", "core.hooksPath=", *arguments),
            cwd=self.root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode:
            self.fail(result.stderr.decode(errors="replace"))
        return result.stdout

    def write(self, name: str, content: bytes) -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def seal_sources(self):
        # Test-only authority for newly authored, disposable fixture sources.
        for prefix in ("template", "evidence/authoritative/LLM"):
            payload = build_protected_lock(self.root, prefix, "Disposable reset test fixture")
            self.write(prefix + "/.tadp-lock.json", json.dumps(payload).encode())

    def snapshot(self, root: Path | None = None) -> dict[str, bytes]:
        base = root or self.root
        return {
            path.relative_to(base).as_posix(): path.read_bytes()
            for path in base.rglob("*")
            if path.is_file() and not path.is_symlink()
        }

    def backup(self, name: str = "backup") -> Path:
        return self.directory / name

    def apply(self, backup: Path | None = None):
        apply_plan(self.root, make_plan(self.root), backup or self.backup(), str(self.root))

    def test_preview_lists_removals_without_writing_any_files(self):
        self.write("products/user-output.bin", b"\x00\xff\x10")
        self.write("README.md", b"User customization\n")
        before = self.snapshot()
        parent_before = set(self.directory.iterdir())

        plan = make_plan(self.root)

        actions = {item["path"]: item["action"] for item in plan["actions"]}
        self.assertEqual("delete", actions["products/user-output.bin"])
        self.assertEqual("replace", actions["README.md"])
        self.assertEqual(before, self.snapshot())
        self.assertEqual(parent_before, set(self.directory.iterdir()))

    def test_apply_restores_sources_removes_work_and_backs_up_exact_bytes(self):
        self.write("README.md", b"Custom root\r\n")
        self.write("project-profile.md", b"My live adopted project\n")
        self.write("initiatives/v1/accepted.md", b"Accepted work retained in backup\n")
        self.write("products/result.bin", b"\x00\xff\r\n")
        self.write(".gitignore", b"ignored/\n")
        self.write("ignored/cache.bin", b"Ignored work\n")
        (self.root / "empty-user-folder").mkdir()
        removed = {
            name: (self.root / name).read_bytes()
            for name in ("project-profile.md", "initiatives/v1/accepted.md", "products/result.bin",
                         ".gitignore", "ignored/cache.bin", "README.md")
        }
        protected_before = {
            key: value for key, value in self.snapshot().items()
            if key.startswith(("template/", "evidence/authoritative/LLM/"))
        }

        self.apply()

        for name, content in self.scaffold.items():
            self.assertEqual(content, (self.root / name).read_bytes(), name)
        for name, content in removed.items():
            self.assertEqual(content, (self.backup() / "files" / name).read_bytes(), name)
            if name != "README.md":
                self.assertFalse((self.root / name).exists(), name)
        self.assertFalse((self.root / "empty-user-folder").exists())
        self.assertFalse((self.root / "initiatives/v1").exists())
        self.assertEqual(b"# Complete reusable library\n", (self.root / "template/README.md").read_bytes())
        for name, content in protected_before.items():
            self.assertEqual(content, (self.root / name).read_bytes(), name)
        self.assertEqual([], validate_protected_sources(self.root))
        self.assertTrue((self.root / "tools/tadp_reset.py").is_file())
        self.assertTrue((self.backup() / "reset-manifest.json").is_file())

    def test_full_repository_baseline_restores_exact_scaffold_and_preserves_locks(self):
        protocol = TOOLS.parent
        self.root = self.directory / "full-project"
        self.root.mkdir()
        self.git("init", "--quiet")
        shutil.copytree(protocol / "template", self.root / "template")
        shutil.copytree(
            protocol / "evidence/authoritative/LLM",
            self.root / "evidence/authoritative/LLM",
        )
        expected_scaffold = {}
        for source in (protocol / "template/project").rglob("*"):
            if not source.is_file():
                continue
            relative = source.relative_to(protocol / "template/project")
            name = relative.as_posix()
            if name.startswith(("template/", "evidence/authoritative/LLM/")):
                continue
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            expected_scaffold[name] = source.read_bytes()
        shutil.copy2(TOOLS / "tadp_reset.py", self.root / "tools/tadp_reset.py")
        protected_before = {
            key: value for key, value in self.snapshot().items()
            if key.startswith(("template/", "evidence/authoritative/LLM/"))
            or key == "tools/tadp_reset.py"
        }
        self.write("README.md", b"Customized full project README\n")
        self.write("products/user-output.bin", b"\x00\xff Actual user output\n")
        self.write("initiatives/v1/custom.md", b"Actual project initiative\n")

        self.apply()

        for name, content in expected_scaffold.items():
            self.assertEqual(content, (self.root / name).read_bytes(), name)
        for name, content in protected_before.items():
            self.assertEqual(content, (self.root / name).read_bytes(), name)
        files = {name for name in self.snapshot() if not name.startswith(".git/")}
        self.assertEqual(set(expected_scaffold) | set(protected_before), files)
        self.assertEqual([], validate_protected_sources(self.root))
        self.assertEqual(
            b"Customized full project README\n",
            (self.backup() / "files/README.md").read_bytes(),
        )
        self.assertEqual(
            b"\x00\xff Actual user output\n",
            (self.backup() / "files/products/user-output.bin").read_bytes(),
        )

    def test_apply_preserves_staged_index_commits_refs_and_git_configuration(self):
        self.write("tracked.txt", b"Before staged change\n")
        self.git("add", "tracked.txt")
        self.git("commit", "--quiet", "-m", "User work")
        self.write("tracked.txt", b"Staged work\n")
        self.git("add", "tracked.txt")
        self.write("tracked.txt", b"Unstaged work\n")
        before = self.snapshot(self.root / ".git")

        self.apply()

        self.assertEqual(before, self.snapshot(self.root / ".git"))
        self.assertEqual(b"Unstaged work\n", (self.backup() / "files/tracked.txt").read_bytes())
        self.assertEqual(b"Staged work\n", self.git("show", ":tracked.txt"))

    def test_repeat_reset_leaves_clean_scaffold_content_unchanged(self):
        self.write("user.txt", b"Remove once\n")
        self.apply()
        before = self.snapshot()

        self.apply(self.backup("second-backup"))

        self.assertEqual(before, self.snapshot())

    def test_baseline_file_replaces_user_directory_and_saves_its_children(self):
        (self.root / "README.md").unlink()
        self.write("README.md/user.txt", b"Directory in place of baseline file\n")

        self.apply()

        self.assertEqual(self.scaffold["README.md"], (self.root / "README.md").read_bytes())
        self.assertEqual(
            b"Directory in place of baseline file\n",
            (self.backup() / "files/README.md/user.txt").read_bytes(),
        )

    def test_baseline_directory_replaces_user_file_and_saves_original(self):
        (self.root / "initiatives/README.md").unlink()
        (self.root / "initiatives").rmdir()
        self.write("initiatives", b"File in place of baseline directory\n")

        self.apply()

        self.assertEqual(
            self.scaffold["initiatives/README.md"],
            (self.root / "initiatives/README.md").read_bytes(),
        )
        self.assertEqual(
            b"File in place of baseline directory\n",
            (self.backup() / "files/initiatives").read_bytes(),
        )

    def test_backup_io_failure_leaves_project_unchanged_and_retains_partial_backup(self):
        self.write("user.txt", b"User work must survive failed backup\n")
        before = self.snapshot()
        original_open = Path.open
        failed_path = self.backup() / "files/user.txt"

        def fail_backup_open(path, *args, **kwargs):
            if path == failed_path and args and args[0] == "xb":
                raise OSError("Simulated backup storage failure")
            return original_open(path, *args, **kwargs)

        with mock.patch.object(Path, "open", new=fail_backup_open):
            with self.assertRaisesRegex((ValueError, RuntimeError, OSError), "backup"):
                self.apply()
        self.assertEqual(before, self.snapshot())
        self.assertTrue(self.backup().is_dir())

    def test_partial_apply_keeps_complete_backup_and_protected_sources(self):
        self.write("README.md", b"Customized README before interrupted reset\n")
        self.write("user.txt", b"User work retained in verified backup\n")
        protected_before = {
            key: value for key, value in self.snapshot().items()
            if key.startswith(("template/", "evidence/authoritative/LLM/", ".git/"))
        }
        original_open = Path.open

        def fail_target_open(path, *args, **kwargs):
            if path == self.root / "README.md" and args and args[0] == "xb":
                raise OSError("Simulated target write failure")
            return original_open(path, *args, **kwargs)

        with mock.patch.object(Path, "open", new=fail_target_open):
            with self.assertRaisesRegex((ValueError, RuntimeError, OSError), "backup"):
                self.apply()
        self.assertEqual(
            b"Customized README before interrupted reset\n",
            (self.backup() / "files/README.md").read_bytes(),
        )
        self.assertEqual(
            b"User work retained in verified backup\n",
            (self.backup() / "files/user.txt").read_bytes(),
        )
        self.assertTrue((self.backup() / "reset-manifest.json").is_file())
        for name, content in protected_before.items():
            self.assertEqual(content, (self.root / name).read_bytes(), name)

    def test_wrong_confirmation_refuses_before_creating_backup(self):
        self.write("user.txt", b"Keep until target confirmed\n")
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError)):
            apply_plan(self.root, make_plan(self.root), self.backup(), "another project")
        self.assertEqual(before, self.snapshot())
        self.assertFalse(self.backup().exists())

    def test_interpreter_in_removed_project_environment_blocks_before_backup(self):
        interpreter = self.write(".venv/Scripts/python.exe", b"Fixture interpreter\n")
        self.write("user.txt", b"Keep user work when running interpreter would be removed\n")
        before = self.snapshot()
        plan = make_plan(self.root)

        with mock.patch.object(sys, "executable", str(interpreter)):
            with mock.patch.object(sys, "prefix", str(self.root / ".venv")):
                with self.assertRaises((ValueError, RuntimeError)):
                    apply_plan(self.root, plan, self.backup(), str(self.root))

        self.assertEqual(before, self.snapshot())
        self.assertFalse(self.backup().exists())

    def test_backup_inside_worktree_is_refused_before_writes(self):
        before = self.snapshot()
        backup = self.root / "backups/run-1"
        with self.assertRaises((ValueError, RuntimeError)):
            apply_plan(self.root, make_plan(self.root), backup, str(self.root))
        self.assertEqual(before, self.snapshot())
        self.assertFalse(backup.exists())

    def test_preexisting_backup_is_never_reused(self):
        self.backup().mkdir()
        sentinel = self.backup() / "keep.txt"
        sentinel.write_bytes(b"Other backup\n")
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError, OSError)):
            self.apply()
        self.assertEqual(before, self.snapshot())
        self.assertEqual(b"Other backup\n", sentinel.read_bytes())

    def test_file_content_drift_after_preview_blocks_apply_without_backup(self):
        self.write("user.txt", b"Before preview\n")
        plan = make_plan(self.root)
        self.write("user.txt", b"Concurrent edit\n")
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError)):
            apply_plan(self.root, plan, self.backup(), str(self.root))
        self.assertEqual(before, self.snapshot())
        self.assertFalse(self.backup().exists())

    def test_new_file_after_preview_blocks_apply_without_backup(self):
        plan = make_plan(self.root)
        self.write("new-user-work.txt", b"Created after preview\n")
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError)):
            apply_plan(self.root, plan, self.backup(), str(self.root))
        self.assertEqual(before, self.snapshot())
        self.assertFalse(self.backup().exists())

    def test_protected_drift_is_reported_without_repairing_or_refreshing_lock(self):
        self.write("template/README.md", b"Unapproved source drift\n")
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)
        self.assertEqual(before, self.snapshot())

    def test_missing_source_lock_is_a_blocker(self):
        (self.root / "template/.tadp-lock.json").unlink()
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)
        self.assertEqual(before, self.snapshot())

    def test_subdirectory_target_is_refused(self):
        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root / "template/project")

    def test_nested_protocol_target_preserves_enclosing_git_and_siblings(self):
        enclosing = self.directory / "enclosing"
        enclosing.mkdir()
        moved_root = enclosing / "protocol"
        self.root.rename(moved_root)
        self.root = moved_root
        (self.root / ".git").rename(enclosing / ".git")
        sibling = enclosing / "outside.txt"
        sibling.write_bytes(b"Outside the reset target\n")
        self.write("user.txt", b"Inside the reset target\n")
        metadata = self.snapshot(enclosing / ".git")

        self.apply()

        self.assertFalse((self.root / "user.txt").exists())
        self.assertEqual(b"Outside the reset target\n", sibling.read_bytes())
        self.assertEqual(metadata, self.snapshot(enclosing / ".git"))

    def test_nested_git_repository_blocks_reset(self):
        self.write("nested/.git/HEAD", b"ref: refs/heads/main\n")
        before = self.snapshot()
        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)
        self.assertEqual(before, self.snapshot())

    def test_git_metadata_inside_project_under_another_name_blocks_reset(self):
        self.git("init", "--quiet", "--separate-git-dir", str(self.root / "git-data"))
        before = self.snapshot()

        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)

        self.assertEqual(before, self.snapshot())

    def test_scaffold_file_cannot_replace_parent_of_protected_invariant_suite(self):
        self.write("template/project/evidence/authoritative", b"Conflicting scaffold file\n")
        self.seal_sources()
        before = self.snapshot()

        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)

        self.assertEqual(before, self.snapshot())

    def test_hardlinked_work_is_refused_and_outside_content_is_unchanged(self):
        outside = self.directory / "outside.txt"
        outside.write_bytes(b"Outside work\n")
        try:
            os.link(outside, self.root / "linked.txt")
        except OSError as error:
            self.skipTest(f"Hardlinks are unavailable: {error}")
        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)
        self.assertEqual(b"Outside work\n", outside.read_bytes())

    def test_symlinked_work_is_refused_without_following_outside_directory(self):
        outside = self.directory / "outside"
        outside.mkdir()
        sentinel = outside / "keep.txt"
        sentinel.write_bytes(b"Outside work\n")
        try:
            (self.root / "linked").symlink_to(outside, target_is_directory=True)
        except OSError as error:
            self.skipTest(f"Symlinks are unavailable: {error}")
        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)
        self.assertEqual(b"Outside work\n", sentinel.read_bytes())

    @unittest.skipUnless(os.name == "nt", "Windows junction behavior")
    def test_windows_junction_is_refused_without_touching_outside_directory(self):
        outside = self.directory / "outside"
        outside.mkdir()
        sentinel = outside / "keep.txt"
        sentinel.write_bytes(b"Outside work\n")
        junction = self.root / "junction"
        created = subprocess.run(
            ("cmd.exe", "/d", "/c", "mklink", "/J", str(junction), str(outside)),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if created.returncode:
            self.skipTest("Junction creation unavailable: " + created.stderr.decode(errors="replace"))
        self.addCleanup(junction.rmdir)

        with self.assertRaises((ValueError, RuntimeError)):
            make_plan(self.root)

        self.assertEqual(b"Outside work\n", sentinel.read_bytes())

    def test_cli_preview_emits_json_and_does_not_write(self):
        self.write("draft.txt", b"User draft\n")
        before = self.snapshot()
        output = io.StringIO()
        with mock.patch.object(tadp_reset, "__file__", str(self.root / "tools/tadp_reset.py")):
            with contextlib.redirect_stdout(output):
                result = main(["--json"])
        self.assertEqual(0, result)
        payload = json.loads(output.getvalue())
        self.assertEqual(str(self.root), payload["root"])
        self.assertEqual(before, self.snapshot())

    def test_cli_apply_requires_backup_and_confirmation(self):
        before = self.snapshot()
        output = io.StringIO()
        try:
            with mock.patch.object(tadp_reset, "__file__", str(self.root / "tools/tadp_reset.py")):
                with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                    result = main(["--apply"])
        except SystemExit as error:
            result = error.code
        self.assertEqual(2, result)
        self.assertEqual(before, self.snapshot())


if __name__ == "__main__":
    unittest.main()
