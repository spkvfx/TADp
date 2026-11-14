"""Isolated worktree fixtures for project-root and Git-root separation."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from tadp_protect import guard_staged, mutate_locks
from tadp_scopes import IntegrationRequest, integrate_closed_child, validate_version_scopes
from tadp_validate import (
    PROTECTED_ROOTS, local_branch_exists, validate_coherence,
    validate_required_paths, validate_protected_sources,
)
import test_tadp_validate as fixtures
import test_tadp_scopes as scope_fixtures


class ProjectRootTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tadp-project-roots-")
        self.addCleanup(self.temp.cleanup)
        self.git_root = Path(self.temp.name)
        self.root = self.git_root / "projects" / "alpha"
        self.root.mkdir(parents=True)
        self.git("init", "--quiet", "-b", "trunk")
        self.git("config", "user.name", "TADp fixture")
        self.git("config", "user.email", "fixture@example.invalid")

    def git(self, *arguments):
        return subprocess.run(("git", "-C", str(self.git_root), *arguments),
                              capture_output=True, text=True, check=True).stdout.strip()

    def save(self, message):
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", message)
        return self.git("rev-parse", "HEAD")

    def scaffold(self):
        fixtures.ValidatorTests().make_repository(self.root)
        # Remove only this disposable fixture's nested repository, retaining G.
        shutil.rmtree(self.root / ".git")

    def test_project_entry_point_and_invalid_git_file(self):
        self.scaffold()
        self.assertEqual([], validate_required_paths(self.root))
        self.assertFalse((self.git_root / "AGENTS.md").exists())
        (self.root / "AGENTS.md").unlink()
        (self.git_root / "AGENTS.md").write_text("Parent instructions\n")
        self.assertIn("TADP022", {f.code for f in validate_required_paths(self.root)})
        (self.root / ".git").write_text("gitdir: missing-metadata\n")
        self.assertIn("TADP012", {f.code for f in validate_required_paths(self.root)})

    def test_nested_staged_protection_preserves_sibling_index(self):
        for name in ("template/source.md", "evidence/authoritative/LLM/source.md"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Initial\n")
        with redirect_stdout(StringIO()):
            self.assertEqual(0, mutate_locks(self.root, action="initialize", protected_roots=PROTECTED_ROOTS, authority="fixture"))
        sibling = self.git_root / "sibling.txt"
        sibling.write_text("Parent sentinel\n")
        self.save("scaffold")
        (self.root / "template/source.md").write_text("Authorized new source\n")
        with redirect_stdout(StringIO()):
            self.assertEqual(0, mutate_locks(self.root, action="refresh", protected_roots=("template",), authority="fixture update"))
        sibling.write_text("Unrelated staged work\n")
        self.git("add", ".")
        before = self.git("diff", "--cached", "--binary")
        with patch.dict(os.environ, {"TADP_ALLOW_PROTECTED_UPDATE": "", "TADP_PROTECTED_UPDATE_AUTHORITY": ""}), redirect_stderr(StringIO()):
            self.assertEqual(1, guard_staged(self.root))
        with patch.dict(os.environ, {"TADP_ALLOW_PROTECTED_UPDATE": "1", "TADP_PROTECTED_UPDATE_AUTHORITY": "fixture update"}):
            self.assertEqual(0, guard_staged(self.root))
        self.assertEqual([], validate_protected_sources(self.root))
        self.assertEqual(before, self.git("diff", "--cached", "--binary"))
        self.assertEqual("Unrelated staged work\n", sibling.read_text())

    def test_linked_worktree_uses_shared_refs(self):
        (self.root / "AGENTS.md").write_text("Project instructions\n")
        self.save("seed")
        self.git("branch", "initiative/shared-ref")
        linked = self.git_root / "linked-fixture"
        self.git("worktree", "add", "--quiet", "-b", "linked", str(linked))
        linked_project = linked / "projects/alpha"
        self.assertTrue((linked / ".git").is_file())
        self.assertTrue(local_branch_exists(linked_project, "initiative/shared-ref"))
        self.assertNotIn("TADP012", {f.code for f in validate_required_paths(linked_project)})
        self.assertFalse(local_branch_exists(linked_project, "initiative/missing"))

    def adopt_nested_coherence(self):
        self.scaffold()
        fixture = fixtures.CoherenceTests()
        initiative = fixture.make_initiative(self.root, status="Completed")
        baseline = self.save("historical closed initiative")
        (self.root / "project-profile.md").write_text(f"**Coherence revision baseline:** {baseline}\n")
        (self.root / "initiatives/work-conflicts.md").write_text(
            "# Work conflicts\n\nNo work conflicts recorded.\n\n| ID | Source work | Conflicting work | States and effort | Conflict and impact | Owner | Status | Disposition and evidence |\n"
            "|---|---|---|---|---|---|---|---|\n")
        self.save("adopt coherence")
        return initiative, baseline

    def test_nested_terminal_history_detects_working_and_committed_changes(self):
        initiative, baseline = self.adopt_nested_coherence()
        self.assertEqual([], validate_coherence(self.root))
        architecture = initiative / "architecture.md"
        architecture.write_text("# Unapproved closed-claim revision\n")
        self.assertTrue(any(f.code == "TADP043" for f in validate_coherence(self.root)))
        self.save("unapproved closed edit")
        findings = validate_coherence(self.root, base_ref=baseline)
        self.assertTrue(any(f.code == "TADP043" for f in findings), findings)

    def test_nested_removed_coherence_declaration_remains_detectable(self):
        self.adopt_nested_coherence()
        (self.root / "project-profile.md").write_text("# Profile removed adoption\n")
        self.save("remove declaration")
        self.assertTrue(any(f.code == "TADP041" and "must not be removed" in f.message
                            for f in validate_coherence(self.root)))

    def test_nested_scope_history_preserves_adoption(self):
        helper = scope_fixtures.ScopeTests()
        # Reuse scope fixture builders against P, retaining this enclosing G.
        (self.root / "seed.txt").write_text("seed\n")
        helper.root = self.root
        helper.base = self.save("scope baseline")
        helper.fixture()
        self.save("adopt scopes")
        self.assertEqual([], validate_version_scopes(self.root))
        (self.root / "project-profile.md").write_text("# Removed scope adoption\n")
        self.save("remove scope declaration")
        self.assertTrue(any("must not be removed" in f.message for f in validate_version_scopes(self.root)))

    def integration(self, *paths):
        (self.root / "authority.md").write_text("Human closure authority\n")
        self.save("base")
        target = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "-c", "child")
        for name in paths:
            path = self.git_root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("child change\n")
        source = self.save("child")
        self.git("switch", "--quiet", "trunk")
        return IntegrationRequest("child", "trunk", "trunk", source, target, "Finalize child", "authority.md", True, True)

    def test_nested_integration_rejects_parent_or_sibling_changes(self):
        request = self.integration("projects/alpha/delivered.txt", "sibling.txt")
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Blocked", result.state)
        self.assertIn("outside", result.failure)
        self.assertEqual(request.target_tip, self.git("rev-parse", "HEAD"))
        self.assertFalse((self.git_root / "sibling.txt").exists())

    def test_nested_integration_permits_only_project_changes(self):
        request = self.integration("projects/alpha/delivered.txt")
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Fast-forward", result.state, result.failure)
        self.assertTrue((self.root / "delivered.txt").is_file())

    def test_nested_integration_rejects_another_scaffold(self):
        request = self.integration(
            "projects/alpha/other/prompts/AGENTS.md",
            "projects/alpha/other/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md")
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Blocked", result.state)
        self.assertIn("scaffold ownership", result.failure)

    def test_nested_integration_rejects_reverted_outside_history(self):
        (self.root / "authority.md").write_text("Human closure authority\n")
        self.save("base")
        target = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "-c", "child")
        sibling = self.git_root / "sibling.txt"
        sibling.write_text("Outside edit\n")
        self.save("outside edit")
        sibling.unlink()
        self.save("revert outside edit")
        source = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "trunk")
        request = IntegrationRequest("child", "trunk", "trunk", source, target,
                                     "Finalize child", "authority.md", True, True)
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Blocked", result.state)
        self.assertIn("outside", result.failure)
        self.assertEqual(target, self.git("rev-parse", "HEAD"))

    def test_nested_integration_rejects_deleted_uninitialized_gitlink(self):
        (self.root / "authority.md").write_text("Human closure authority\n")
        seed = self.save("base")
        self.git("update-index", "--add", "--cacheinfo", f"160000,{seed},projects/alpha/vendor")
        self.git("commit", "--quiet", "-m", "uninitialized submodule boundary")
        target = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "-c", "child")
        self.git("update-index", "--force-remove", "projects/alpha/vendor")
        self.git("commit", "--quiet", "-m", "remove gitlink")
        source = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "trunk")
        request = IntegrationRequest("child", "trunk", "trunk", source, target,
                                     "Finalize child", "authority.md", True, True)
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Blocked", result.state)
        self.assertIn("submodule ownership", result.failure)
        self.assertEqual(target, self.git("rev-parse", "HEAD"))

    def test_nested_staged_rename_cannot_hide_protected_source_removal(self):
        for name in ("template/source.md", "evidence/authoritative/LLM/source.md"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Protected source\n")
        with redirect_stdout(StringIO()):
            mutate_locks(self.root, action="initialize", protected_roots=PROTECTED_ROOTS, authority="fixture")
        self.save("protected baseline")
        self.git("mv", "projects/alpha/template/source.md", "projects/alpha/moved.md")
        # An ignored working restoration must not conceal the index deletion.
        (self.git_root / ".git/info/exclude").write_text("/projects/alpha/template/source.md\n")
        (self.root / "template/source.md").write_text("Protected source\n")
        self.assertEqual([], validate_protected_sources(self.root))
        errors = StringIO()
        with patch.dict(os.environ, {"TADP_ALLOW_PROTECTED_UPDATE": ""}), redirect_stderr(errors):
            self.assertEqual(1, guard_staged(self.root))
        self.assertIn("staged protected-source changes", errors.getvalue())

    def test_nested_integration_rejects_source_tree_symlink(self):
        (self.root / "authority.md").write_text("Human closure authority\n")
        target = self.save("base")
        self.git("switch", "--quiet", "-c", "child")
        blob = subprocess.run(("git", "-C", str(self.git_root), "hash-object", "-w", "--stdin"),
                              input="../../../outside", capture_output=True, text=True, check=True).stdout.strip()
        self.git("update-index", "--add", "--cacheinfo", f"120000,{blob},projects/alpha/escape")
        self.git("commit", "--quiet", "-m", "source symlink fixture")
        source = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "trunk")
        request = IntegrationRequest("child", "trunk", "trunk", source, target,
                                     "Finalize child", "authority.md", True, True)
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Blocked", result.state)
        self.assertIn("symbolic link", result.failure)
        self.assertEqual(target, self.git("rev-parse", "HEAD"))

    def test_nested_integration_checks_gitlinks_in_imported_parent_tree(self):
        (self.root / "authority.md").write_text("Human closure authority\n")
        seed = self.save("base")
        self.git("update-index", "--add", "--cacheinfo", f"160000,{seed},projects/alpha/vendor")
        self.git("commit", "--quiet", "-m", "gitlink common baseline")
        self.git("branch", "child")
        self.git("update-index", "--force-remove", "projects/alpha/vendor")
        self.git("commit", "--quiet", "-m", "target removes gitlink")
        target = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "child")
        self.git("update-index", "--force-remove", "projects/alpha/vendor")
        self.git("commit", "--quiet", "-m", "source independently removes gitlink")
        source = self.git("rev-parse", "HEAD")
        self.git("switch", "--quiet", "trunk")
        request = IntegrationRequest("child", "trunk", "trunk", source, target,
                                     "Finalize child", "authority.md", True, True)
        result = integrate_closed_child(self.root, request, lambda: True)
        self.assertEqual("Blocked", result.state)
        self.assertIn("submodule ownership", result.failure)
        self.assertEqual(target, self.git("rev-parse", "HEAD"))

    def test_nested_validation_and_protection_clis_are_read_only(self):
        self.scaffold()
        tools = Path(__file__).resolve().parents[1] / "tools"
        shutil.copytree(tools, self.root / "tools", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.md"))

        def snapshot():
            return {p.relative_to(self.root).as_posix(): p.read_bytes()
                    for p in self.root.rglob("*") if p.is_file()}

        before = snapshot()
        for command in (("tadp_validate.py", str(self.root)),
                        ("tadp_protect.py", "check", str(self.root))):
            result = subprocess.run((sys.executable, str(self.root / "tools" / command[0]), *command[1:]),
                                    cwd=self.git_root, capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertEqual(before, snapshot())
            self.assertFalse((self.root / "tools/__pycache__").exists())

    def test_nested_installed_hook_resolves_relative_git_environment(self):
        shell = shutil.which("sh")
        if shell is None and (git_binary := shutil.which("git")):
            candidate = Path(git_binary).parents[1] / "bin/sh.exe"
            shell = str(candidate) if candidate.is_file() else None
        if shell is None:
            self.skipTest("POSIX shell unavailable for installed hook fixture")
        self.scaffold()
        protocol = Path(__file__).resolve().parents[1]
        shutil.copytree(protocol / "tools", self.root / "tools", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.md"))
        hook = self.root / ".githooks/pre-commit"
        shutil.copyfile(protocol / "template/project/.githooks/pre-commit", hook)
        sibling = self.git_root / "sibling.txt"
        sibling.write_text("Original parent work\n")
        self.save("installed hook fixture")
        sibling.write_text("Unrelated staged parent work\n")
        self.git("add", "sibling.txt")
        before_index = self.git("diff", "--cached", "--binary")
        before_files = {p.relative_to(self.root).as_posix(): p.read_bytes()
                        for p in self.root.rglob("*") if p.is_file()}
        env = os.environ | {"GIT_DIR": ".git", "GIT_INDEX_FILE": ".git/index",
                            "TADP_PYTHON": sys.executable.replace("\\", "/")}
        env.pop("GIT_WORK_TREE", None)
        result = subprocess.run((shell, str(hook).replace("\\", "/")),
                                cwd=self.git_root, env=env, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(before_index, self.git("diff", "--cached", "--binary"))
        self.assertEqual(before_files, {p.relative_to(self.root).as_posix(): p.read_bytes()
                                       for p in self.root.rglob("*") if p.is_file()})


if __name__ == "__main__":
    unittest.main()
