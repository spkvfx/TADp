from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import shutil

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from tadp_scopes import (
    SCOPE_HEADERS, MEMBER_HEADERS, MIGRATION_HEADERS, IntegrationRequest,
    adopted, git, integrate_closed_child, parse_scope, scope_parent,
    validate_version_scopes,
)
from tadp_validate import validate_version_correlation, validate, INITIAL_INITIATIVE_FILES
import test_tadp_validate as legacy_fixtures


def table(headers, rows):
    return "| " + " | ".join(headers) + " |\n| " + " | ".join("---" for _ in headers) + " |\n" + "".join("| " + " | ".join(row[key] for key in headers) + " |\n" for row in rows)


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        git(self.root, "init", "-b", "trunk")
        git(self.root, "config", "user.email", "fixture@example.invalid")
        git(self.root, "config", "user.name", "Protocol fixture")
        self.write("authority.md", "Human: finalize identified fixture work into recorded parent.\n")
        self.write("base.txt", "base\n")
        self.base = self.save("base")

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def save(self, message):
        git(self.root, "add", ".")
        git(self.root, "commit", "-m", message)
        return git(self.root, "rev-parse", "HEAD")

    def fixture(self, shared=False):
        self.scopes = []
        for name, kind, parent in (("v1", "Major", "trunk"), ("v1.0", "Minor", "v1")):
            git(self.root, "branch", name, parent)
            self.scopes.append(dict(zip(SCOPE_HEADERS, (name, kind, parent, name, parent, self.base, parent, "[source](../notes/note.md), [suite](../notes/README.md)", "None", "v1.0" if name == "v1" else "None", "Open", "Pending", "Not closed", "Not integrated", self.base))))
            self.write(f"initiatives/{name}/README.md", f"**Scope:** {name}\n\n[registry](../version-scopes.md)\n\n[membership](../initiative-index.md)\n")
        self.members = []
        for number in (1, 2):
            identity = f"INIT-IMP-00{number}"
            slug = identity + "-work"
            branch = "v1.0" if shared else "initiative/v1.0-" + slug
            if not shared:
                git(self.root, "branch", branch, "v1.0")
            directory = f"initiatives/v1.0/implementation/{slug}"
            record = f"{directory}/README.md"
            self.members.append(dict(zip(MEMBER_HEADERS, ("v1.0", identity, "implementation", f"[{identity}](v1.0/implementation/{slug}/README.md)", "[NOTE-1](../notes/note.md)", branch, "shared" if shared else "dedicated", "v1.0", self.base, "v1.0", "1", f"[lifecycle](v1.0/implementation/{slug}/README.md)", "Pending"))))
            self.write(record, "\n\n".join((f"**Initiative ID:** {identity}", "**Initiative type:** implementation", "**Status:** Proposed", "**Version scope:** v1.0", f"**Execution branch:** {branch}", f"**Execution mode:** {'shared' if shared else 'dedicated'}", "**Captured base ref:** v1.0", f"**Captured base commit:** {self.base}", "**Integration target:** v1.0", "**Revision cycle:** 1", "**Source notes:** [NOTE-1](../../../../notes/note.md)", "[canonical membership](../../../initiative-index.md)", "| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |\n| --- | --- | --- | --- | --- | --- | --- |\n| SUITE-1 | [suite](../../../../notes/README.md) | NOTE-1 | v1.0 | [note](../../../../notes/note.md) | originate | [fit](routing.md) |")))
            self.write(f"{directory}/routing.md", "Bounded source fit; no acceptance implied.\n")
        self.scopes[1]["Members"] = ", ".join(row["Record location"] for row in self.members)
        self.write("notes/note.md", "**Source ID:** NOTE-1\n\n**Version scope:** v1.0\n\nNon-authoritative proposal input.\n\n" + "\n".join(f"[{row['Initiative ID']}](../initiatives/v1.0/implementation/{row['Initiative ID']}-work/README.md)" for row in self.members))
        self.write("notes/README.md", "**Suite ID:** SUITE-1\n\n**Version scope:** v1.0\n\nNon-authoritative proposal input\n\n[NOTE-1](note.md)\n")
        self.write("project-profile.md", f"**Version scope revision effective point:** {self.base}\n\n**Default integration branch:** trunk\n")
        self.write("initiatives/version-scope-migration-ledger.md", table(MIGRATION_HEADERS, []))
        self.flush()

    def flush(self):
        self.write("initiatives/version-scopes.md", table(SCOPE_HEADERS, self.scopes))
        self.write("initiatives/initiative-index.md", table(MEMBER_HEADERS, self.members))

    def findings(self):
        self.flush()
        return [finding.message for finding in validate_version_scopes(self.root) if finding.severity == "error"]

    def test_exact_numeric_scope_identity(self):
        self.assertEqual(sorted(["v1.10", "v1.9", "v1", "v1.0.0", "v1.0"], key=parse_scope), ["v1", "v1.0", "v1.0.0", "v1.9", "v1.10"])
        for scope in (" v1", "v1 ", "v01", "v1.01", "v1..0", "v1.2.3.4", "v1.0-alpha", "v1+meta", "v-1", "V1", "v1\n"):
            with self.subTest(scope=scope), self.assertRaises(ValueError):
                parse_scope(scope)
        self.assertEqual(scope_parent("v2.1.1"), "v2.1")
        self.assertEqual(scope_parent("v2.1"), "v2")
        self.assertIsNone(scope_parent("v2"))

    def test_adoption_does_not_reinterpret_legacy(self):
        for value in ("Not yet adopted", "Installed; adoption pending"):
            self.assertFalse(adopted(f"**Version scope revision effective point:** {value}\n"))
        self.assertEqual(validate_version_scopes(self.root), [])

    def test_two_independent_initiatives_share_one_note_and_scope(self):
        self.fixture()
        self.assertEqual(self.findings(), [])
        self.assertEqual(validate_version_correlation(self.root), [])

    def test_declared_shared_scope_placement_is_valid(self):
        self.fixture(shared=True)
        self.assertEqual(self.findings(), [])

    def test_wrong_parent_duplicate_identity_and_undeclared_sharing_fail(self):
        self.fixture()
        self.scopes[1]["Structural parent"] = "v2"
        self.members[1]["Initiative ID"] = self.members[0]["Initiative ID"]
        self.members[1]["Execution branch"] = self.members[0]["Execution branch"]
        findings = " ".join(self.findings())
        self.assertIn("wrong structural parent", findings)
        self.assertIn("duplicate initiative", findings)
        self.assertIn("branch role", findings)

    def test_open_member_blocks_scope_closure(self):
        self.fixture(shared=True)
        self.scopes[1]["Closure disposition"] = "Closed"
        self.assertIn("open member", " ".join(self.findings()))
        self.assertEqual(self.scopes[0]["Closure disposition"], "Open")

    def test_missing_reciprocal_mapping_is_not_repaired(self):
        self.fixture()
        self.scopes[1]["Members"] = "None"
        before = (self.root / "notes/note.md").read_bytes()
        self.assertIn("omits member", " ".join(self.findings()))
        self.assertEqual((self.root / "notes/note.md").read_bytes(), before)

    def complete_scaffold(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            legacy_fixtures.ValidatorTests.make_repository(self, source)
            for path in source.iterdir():
                if path.name == ".git":
                    continue
                if path.is_dir():
                    shutil.copytree(path, self.root / path.name, dirs_exist_ok=True)
                else:
                    shutil.copy2(path, self.root / path.name)
        for member in self.members:
            directory = self.root / "initiatives/v1.0/implementation" / (member["Initiative ID"] + "-work")
            for name in INITIAL_INITIATIVE_FILES:
                if name == "README.md":
                    continue
                self.write(str((directory / name).relative_to(self.root)), "# Record\n\nAuthoritative evidence\n\nVerification evidence\n")
            readme = directory / "README.md"
            readme.write_text(readme.read_text(encoding="utf-8") + "\n\n### Lifecycle history\n\n| Date | From | To | Authority | Claim | Reason | Git |\n| --- | --- | --- | --- | --- | --- | --- |\n| 2026-11-12 | Initial | Proposed | Source | initial | prepare | pending |\n", encoding="utf-8")
        self.write("initiatives/work-conflicts.md", "No work conflicts recorded.\n\n| ID | Source work | Conflicting work | States and effort | Conflict and impact | Owner | Status | Disposition and evidence |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n")
        profile = self.root / "project-profile.md"
        profile.write_text(profile.read_text(encoding="utf-8") + f"\n**Coherence revision baseline:** {self.base}\n", encoding="utf-8")

    def test_full_adopted_validator_with_all_ordinary_checks_passes(self):
        self.fixture(shared=True)
        self.complete_scaffold()
        self.assertEqual([finding for finding in validate(self.root) if finding.severity == "error"], [])

    def test_source_metadata_catalog_and_scope_readme_are_checked(self):
        self.fixture()
        self.write("notes/note.md", "**Source ID:** WRONG\n\n**Version scope:** v2.1\n")
        self.scopes[1]["Source catalog"] = "None"
        (self.root / "initiatives/v1/README.md").unlink()
        messages = " ".join(self.findings())
        self.assertIn("source note ID/scope", messages)
        self.assertIn("source catalog omits", messages)
        self.assertIn("navigation README", messages)

    def test_adoption_and_creation_bases_cannot_be_rewritten(self):
        self.fixture()
        self.save("adopt scopes")
        profile = self.root / "project-profile.md"
        old = profile.read_text(encoding="utf-8")
        self.write("project-profile.md", old.replace(self.base, "f" * 40))
        self.assertIn("must not change", " ".join(self.findings()))
        self.write("project-profile.md", old.replace("**Version scope revision effective point:**", "**Removed:**"))
        self.assertIn("must not be removed", " ".join(self.findings()))
        self.write("project-profile.md", old)
        self.scopes[1]["Captured base ref"] = "trunk"
        self.assertIn("immutable", " ".join(self.findings()))

    def test_pending_member_receipt_blocks_scope_closure(self):
        self.fixture()
        self.scopes[1]["Closure disposition"] = "Closed"
        self.members[0]["Integration evidence"] = "[receipt](pending.md)"
        self.write("initiatives/pending.md", "**Integration state:** Pending\n")
        readme = self.root / "initiatives/v1.0/implementation/INIT-IMP-001-work/README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace("**Status:** Proposed", "**Status:** Completed"), encoding="utf-8")
        self.assertIn("before required member integration", " ".join(self.findings()))

    def test_cross_scope_append_and_mixed_types_preserve_source_and_target(self):
        self.fixture()
        old = self.root / "initiatives/v1.0/implementation/INIT-IMP-002-work"
        new = self.root / "initiatives/v1.0/planning/INIT-IMP-002-work"
        new.parent.mkdir(parents=True)
        shutil.move(str(old), str(new))
        readme = new / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace("**Initiative type:** implementation", "**Initiative type:** planning"), encoding="utf-8")
        self.members[1]["Type"] = "planning"
        self.members[1]["Record location"] = self.members[1]["Record location"].replace("/implementation/", "/planning/")
        self.scopes[1]["Members"] = ", ".join(row["Record location"] for row in self.members)
        note = self.root / "notes/note.md"
        note.write_text(note.read_text(encoding="utf-8").replace("implementation/INIT-IMP-002", "planning/INIT-IMP-002"), encoding="utf-8")
        self.write("notes/later.md", "**Realization ID:** NOTE-2\n\n**Version scope:** v2.1\n\n[existing](../initiatives/v1.0/implementation/INIT-IMP-001-work/README.md)\n")
        self.write("notes/later-suite.md", "**Suite ID:** SUITE-2\n\n**Version scope:** v2.1\n\nNon-authoritative proposal input\n\n[NOTE-2](later.md)\n")
        target = self.root / "initiatives/v1.0/implementation/INIT-IMP-001-work/README.md"
        target.write_text(target.read_text(encoding="utf-8").replace("**Source notes:** [NOTE-1](../../../../notes/note.md)", "**Source notes:** [NOTE-1](../../../../notes/note.md), [NOTE-2](../../../../notes/later.md)").rstrip() + "\n| SUITE-2 | [later suite](../../../../notes/later-suite.md) | NOTE-2 | v2.1 | [later](../../../../notes/later.md) | append | [fit](routing.md) |\n", encoding="utf-8")
        self.members[0]["Source notes"] += ", [NOTE-2](../notes/later.md)"
        self.scopes[1]["Source catalog"] += ", [NOTE-2](../notes/later.md), [SUITE-2](../notes/later-suite.md)"
        self.assertEqual(self.findings(), [])

    def delegated_cycle(self, status):
        self.fixture()
        self.complete_scaffold()
        readme = self.root / "initiatives/v1.0/implementation/INIT-IMP-001-work/README.md"
        current = readme.read_text(encoding="utf-8").replace("**Status:** Proposed", f"**Status:** {status}")
        current = "**Claim revision:** claim1\n\n" + current
        if status == "Completed":
            current += "| 2026-11-12 | Proposed | Accepted | [accept](decision-receipts/accept.md) | claim1 | accepted | pending |\n| 2026-11-12 | Accepted | In progress | execution | claim1 | begin | pending |\n| 2026-11-12 | In progress | Completed | completion | claim1 | done | pending |\n"
            self.write(str((readme.parent / "execution-record.md").relative_to(self.root)), "# Accepted bounded product output\n\n**Revision cycle:** 1\n\n**Claim revision:** claim1\n")
            self.write(str((readme.parent / "decision-receipts/accept.md").relative_to(self.root)), "**Disposition:** Accepted\n\n**Human authority:** User\n\n**Revision cycle:** 1\n\n**Claim revision:** claim1\n")
            self.write(str((readme.parent / "completion-evidence.md").relative_to(self.root)), "**Revision cycle:** 1\n\n**Claim revision:** claim1\n\n## Cross-initiative coherence review\n\n**Inventory baseline:** inspected all work\n\n**Work-conflict register:** [register](../../../work-conflicts.md)\n\n| Target initiative | Lifecycle state | Work and effort evidence | Finding | Disposition | Record links |\n| --- | --- | --- | --- | --- | --- |\n| [other](../INIT-IMP-002-work/README.md) | Proposed | [planned](../INIT-IMP-002-work/implementation-steps.md) | Compatible | Remains proposed | [scope](../INIT-IMP-002-work/scope-assessment.md) |\n")
        else:
            current += f"| 2026-11-12 | Proposed | {status} | decision | claim1 | terminal disposition | pending |\n"
        readme.write_text(current, encoding="utf-8")
        self.save("prior terminal claim")
        self.assertEqual([finding for finding in validate(self.root) if finding.severity == "error"], [])
        self.write(str((readme.parent / "prior-cycle.md").relative_to(self.root)), current)
        self.members[0]["Revision cycle"] = "2"
        self.flush()
        readme.write_text("**Prior revision record:** [prior](prior-cycle.md)\n\n" + current.replace(f"**Status:** {status}", "**Status:** Proposed").replace("**Revision cycle:** 1", "**Revision cycle:** 2").replace("**Claim revision:** claim1", "**Claim revision:** claim2") + f"| 2026-11-13 | {status} | Proposed | [reopen](decision-receipts/reopen.md) | claim2 | delegated intake; replacement consequences preserved | pending |\n", encoding="utf-8")
        receipt = readme.parent / "decision-receipts/reopen.md"
        self.write(str(receipt.relative_to(self.root)), "\n\n".join(("**Disposition:** Reopened", "**Human authority:** User's adopted bounded intake delegation", "**Decision method:** Delegated realization intake", "**Decision author:** Codex", "**Human intake instruction:** Process the identified realization", "**Governing delegation:** adopted specification 09 and actual intake", "**Routing evidence:** fit assessed; one coherent outcome", "**Prior claim revision:** claim1 preserved in prior commit", "**Verification boundary:** renewed claim requires new verification and human acceptance")))
        self.assertEqual([finding for finding in validate(self.root) if finding.severity == "error"], [])
        return readme, receipt

    def test_completed_delegated_reopening_reenters_proposed(self):
        self.delegated_cycle("Completed")

    def test_cancelled_delegated_reopening_reenters_proposed(self):
        self.delegated_cycle("Cancelled")

    def test_superseded_delegated_reopening_and_unmigrated_exclusion(self):
        readme, receipt = self.delegated_cycle("Superseded")
        self.members = self.members[1:]
        self.flush()
        errors = [finding.code for finding in validate(self.root) if finding.severity == "error"]
        self.assertIn("TADP043", errors)

    def test_delegated_reopening_cannot_claim_accepted(self):
        readme, receipt = self.delegated_cycle("Cancelled")
        text = readme.read_text(encoding="utf-8")
        readme.write_text(text.replace("**Status:** Proposed", "**Status:** Accepted").replace("| Cancelled | Proposed |", "| Cancelled | Accepted |"), encoding="utf-8")
        self.assertIn("TADP043", [finding.code for finding in validate(self.root)])

    def test_old_cycle_acceptance_cannot_certify_changed_claim(self):
        readme, receipt = self.delegated_cycle("Completed")
        readme.write_text(readme.read_text(encoding="utf-8").replace("**Status:** Proposed", "**Status:** Accepted"), encoding="utf-8")
        self.assertIn("renewed human acceptance", " ".join(finding.message for finding in validate_version_scopes(self.root)))

    def request(self, **changes):
        return IntegrationRequest(**(dict(source="child", target="trunk", recorded_parent="trunk", source_tip=git(self.root, "rev-parse", "child"), target_tip=git(self.root, "rev-parse", "trunk"), closure_instruction="Finalize child fixture", authority_record="authority.md", closed=True, all_changes_qualified=True) | changes))

    def child(self):
        git(self.root, "switch", "-c", "child")
        self.write("deliverable.txt", "accepted fixture\n")
        self.save("accepted child")
        git(self.root, "switch", "trunk")

    def test_fast_forward_rerun_and_actual_commit_evidence(self):
        self.child()
        result = integrate_closed_child(self.root, self.request(), lambda: True)
        self.assertEqual(result.state, "Fast-forward")
        self.assertEqual(result.target_after, result.source_tip)
        rerun = integrate_closed_child(self.root, self.request(), lambda: True)
        self.assertEqual(rerun.state, "Already integrated")
        self.assertEqual(rerun.target_before, rerun.target_after)
        self.assertEqual(git(self.root, "branch", "--list", "child"), "child")

    def test_shared_direct_placement_has_no_self_merge(self):
        result = integrate_closed_child(self.root, IntegrationRequest("trunk", "trunk", "trunk", self.base, self.base, "finalize hosted initiative", "authority.md", True, True), lambda: True)
        self.assertEqual(result.state, "Direct placement")
        self.assertEqual(result.target_before, result.target_after)

    def test_no_deliverable_closes_without_integrating_unaccepted_work(self):
        self.child()
        result = integrate_closed_child(self.root, self.request(no_deliverable=True, all_changes_qualified=False), lambda: True)
        self.assertEqual(result.state, "No deliverable")
        self.assertEqual(result.target_before, result.target_after)
        self.assertFalse((self.root / "deliverable.txt").exists())

    def test_unaccepted_work_missing_authority_wrong_target_drift_checks_block(self):
        self.child()
        for changes, fragment in (({"all_changes_qualified": False}, "unfinished"), ({"closure_instruction": ""}, "authority"), ({"recorded_parent": "elsewhere"}, "immediate parent"), ({"target_tip": "0" * 40}, "drift"), ({"parent_open": False}, "open immediate parent")):
            with self.subTest(changes=changes):
                result = integrate_closed_child(self.root, self.request(**changes), lambda: True)
                self.assertEqual(result.state, "Blocked")
                self.assertIn(fragment, result.failure)
                self.assertEqual(git(self.root, "rev-parse", "trunk"), self.base)
        self.assertEqual(integrate_closed_child(self.root, self.request(), lambda: False).state, "Blocked")

    def test_failed_merge_keeps_pending_evidence_and_conflict(self):
        git(self.root, "switch", "-c", "child")
        self.write("base.txt", "child\n")
        self.save("child claim")
        git(self.root, "switch", "trunk")
        self.write("base.txt", "parent\n")
        target = self.save("parent change")
        result = integrate_closed_child(self.root, self.request(), lambda: True)
        self.assertEqual(result.state, "Blocked")
        self.assertEqual(result.target_after, target)
        self.assertIn("UU", git(self.root, "status", "--porcelain"))

    def test_post_merge_failure_does_not_invent_passing_result(self):
        self.child()
        checks = iter((True, False))
        result = integrate_closed_child(self.root, self.request(), lambda: next(checks))
        self.assertEqual(result.state, "Blocked")
        self.assertIn("retain actual integration", result.failure)
        self.assertEqual(result.target_after, result.source_tip)

    def test_verification_tip_drift_blocks_merge(self):
        self.child()
        request = self.request()
        def drift():
            self.write("target-drift.txt", "external target change\n")
            self.save("target drift during verification")
            return True
        result = integrate_closed_child(self.root, request, drift)
        self.assertEqual(result.state, "Blocked")
        self.assertIn("verification changed", result.failure)
        self.assertEqual(result.target_after, git(self.root, "rev-parse", "trunk"))
        self.assertFalse((self.root / "deliverable.txt").exists())


if __name__ == "__main__":
    unittest.main()
