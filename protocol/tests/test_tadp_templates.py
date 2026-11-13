from __future__ import annotations

import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

PROTOCOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOCOL / "tools"))

from tadp_templates import (  # noqa: E402
    COVERAGE, PROCEDURE, Evidence, Prerequisite, PreparationContext,
    assess_prerequisites, instance_link_issues, load_coverage, validate_contract,
)


class TemplateContractTests(unittest.TestCase):
    def write(self, root: Path, path: str, text: str) -> None:
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def fixture(self, root: Path) -> list[dict]:
        self.write(root, "rules.md", "# Rules\n\n## Ownership\n")
        self.write(root, "template/record.md", "# Source\n\n## Embedded history\n")
        records = [dict(id="record", source="template/record.md", section="",
                        destination="initiatives/<scope>/<type>/<id>/README.md",
                        kind="file", owner=3, trigger="Initial suite", evidence="rules and proposal",
                        governing_requirement="rules.md#ownership", conditional=False),
                   dict(id="history", source="template/record.md", section="Embedded history",
                        destination="initiatives/<scope>/<type>/<id>/README.md#history",
                        kind="section", owner=3, trigger="Actual lifecycle event",
                        evidence="actual event", governing_requirement="rules.md#ownership",
                        conditional="Only after the actual event"),
                   dict(id="readiness", source="template/record.md", section="",
                        destination="response only", kind="response", owner=9,
                        trigger="Phase review", evidence="current phase",
                        governing_requirement="rules.md#ownership", conditional=False)]
        for record in records:
            record.update(use="Copy or populate only the owning instance", verification="Check evidence and links",
                          disposition="covered")
        self.coverage(root, records)
        self.write(root, "template/prompts/WORKFLOW-CONTRACT.md",
                   "# Contract\n\n## Documentary prerequisite preparation\n")
        for stage in (*range(14), "scope-closure"):
            path = (f"template/prompts/{stage:02d}_activity.md" if isinstance(stage, int)
                    else "template/prompts/scope_closure.md")
            declaration = dict(stage=stage, records=["record"], procedure=PROCEDURE)
            self.write(root, path, "# Prompt\n\n## Documentary prerequisites\n\n"
                       "<!-- tadp-prerequisites: " + json.dumps(declaration) + " -->\n\n"
                       "~~~text\nBefore the substantive step, apply documentary prerequisite preparation.\n~~~\n")
        return records

    def coverage(self, root: Path, records: list[dict]) -> None:
        self.write(root, COVERAGE, "# Coverage\n\n<!-- tadp-template-coverage -->\n```json\n"
                   + json.dumps(dict(schema_version=1, records=records)) + "\n```\n")

    def snapshot(self, root: Path) -> dict[str, bytes]:
        return {path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*") if path.is_file()}

    def test_complete_coverage_embedded_and_conditional_sources_are_reused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            before = self.snapshot(root)
            self.assertEqual([], validate_contract(root))
            self.assertEqual([], validate_contract(root))
            self.assertEqual(before, self.snapshot(root))

    def test_genuinely_missing_source_is_reported_without_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            (root / "template/record.md").unlink()
            self.assertTrue(any(item.code == "TADP050" for item in validate_contract(root)))
            self.assertFalse((root / "template/record.md").exists())

    def test_missing_embedded_section_is_a_gap(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            records = self.fixture(root)
            records[1]["section"] = "Absent section"
            self.coverage(root, records)
            self.assertTrue(any("section is missing" in item.message for item in validate_contract(root)))

    def test_use_validation_and_applicability_are_required(self):
        for field in ("conditional", "use", "verification", "disposition"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                records = self.fixture(root)
                records[0].pop(field)
                self.coverage(root, records)
                self.assertTrue(any(item.code == "TADP050" for item in validate_contract(root)))

    def test_malformed_coverage_reports_instead_of_crashing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            records = self.fixture(root)
            records[0]["source"] = ["invalid source"]
            self.coverage(root, records)
            self.assertTrue(any(item.code == "TADP050" for item in validate_contract(root)))

    def test_protected_or_escaping_instance_destination_is_rejected(self):
        for destination in ("template/instance.md", "../outside.md", "C:/outside.md"):
            with self.subTest(destination=destination), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                records = self.fixture(root)
                records[0]["destination"] = destination
                self.coverage(root, records)
                self.assertTrue(any(item.code == "TADP050" for item in validate_contract(root)))

    def test_missing_prompt_prerequisites_and_unknown_ids_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            path = root / "template/prompts/09_activity.md"
            path.write_text(path.read_text().replace('"record"', '"missing"'), encoding="utf-8")
            self.assertTrue(any(item.code == "TADP051" and "known coverage IDs" in item.message
                                for item in validate_contract(root)))

    def test_missing_executable_preparation_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            self.write(root, "template/prompts/00_activity.md", "# Prompt\n")
            self.assertTrue(any(item.code == "TADP051" for item in validate_contract(root)))

    def test_legacy_distribution_retains_its_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual([], validate_contract(Path(directory)))

    def test_removing_map_from_revised_contract_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "evidence/authoritative/LLM/08_Workflow.md", "See TEMPLATE-COVERAGE.md")
            self.assertEqual("TADP050", validate_contract(root)[0].code)

    def test_installed_distribution_coverage_and_each_prompt(self):
        records = load_coverage(PROTOCOL)
        self.assertGreater(len(records), 15)
        self.assertEqual([], validate_contract(PROTOCOL))

    def test_instance_links_use_actual_grouped_directory_depth(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "evidence/source.md", "# Source\n")
            destination = "initiatives/v1/implementation/INIT-1/source-mapping.md"
            self.write(root, destination, "[source](../../../../evidence/source.md)\n")
            self.assertEqual((), instance_link_issues(root, destination))
            self.write(root, destination, "[source](../../evidence/source.md)\n")
            self.assertTrue(instance_link_issues(root, destination))


class PrerequisiteAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "sources").mkdir()
        (self.root / "sources/invariant.md").write_text("# Baseline\n\n## Requirement\n", encoding="utf-8")
        self.evidence = Evidence("sources/invariant.md", "Requirement", "invariant", "captured revision")
        self.context = PreparationContext("implementation", ("implementation",), True, phase="phase-2")
        self.record = Prerequisite("suite", "initiative/README.md", 3, evidence=(self.evidence,))

    def assess(self, record=None, context=None):
        return assess_prerequisites(self.root, (record or self.record,), context or self.context)

    def test_constructible_paperwork_does_not_pass_entry_gate(self):
        result = self.assess()
        self.assertEqual((('suite', 3),), result.recovery)
        self.assertFalse(result.ready)
        self.assertFalse((self.root / "initiative").exists())

    def test_exact_available_authority_allows_missing_receipt_preparation(self):
        receipt = replace(self.record, id="receipt", destination="receipts/DR-1.md", owner=7,
                          requires_human=True, instruction="I accept this exact baseline.",
                          author="User", event="captured human message")
        result = self.assess(receipt)
        self.assertEqual((('receipt', 7),), result.recovery)
        self.assertFalse(result.ready)
        self.assertEqual((), result.blockers)

    def test_missing_actual_authority_remains_blocked(self):
        result = self.assess(replace(self.record, requires_human=True))
        self.assertTrue(any("human instruction" in item for item in result.blockers))

    def test_unresolved_acceptance_remains_blocked_even_with_constructible_suite(self):
        result = self.assess(context=replace(self.context, acceptance_required=True))
        self.assertTrue(any("acceptance" in item for item in result.blockers))
        self.assertFalse(result.ready)

    def test_unavailable_evidence_and_unperformed_verification_remain_blockers(self):
        for record in (replace(self.record, evidence=(replace(self.evidence, path="absent.md"),)),
                       replace(self.record, requires_verification=True)):
            with self.subTest(record=record):
                self.assertTrue(self.assess(record).blockers)

    def test_lower_standing_conflict_cannot_support_recovery(self):
        observed = replace(self.evidence, standing="observed implementation", compatible=False)
        self.assertTrue(any("invariant-conflicting" in item
                            for item in self.assess(replace(self.record, evidence=(observed,))).blockers))

    def test_owning_stage_recovery_is_dependency_ordered(self):
        proposal = replace(self.record, id="proposal", destination="initiative/proposal.md", owner=1)
        suite = replace(self.record, dependencies=("proposal",))
        result = assess_prerequisites(self.root, (suite, proposal), self.context)
        self.assertEqual((("proposal", 1), ("suite", 3)), result.recovery)

    def test_condition_requires_cited_non_applicability(self):
        conditional = replace(self.record, applicable=False, non_applicability="SDK absent; scope assessment section 2")
        self.assertTrue(self.assess(conditional).ready)
        self.assertFalse(self.assess(replace(conditional, non_applicability="")).ready)

    def test_missing_identity_and_wrong_type_fail_closed(self):
        for context in (replace(self.context, identity_verified=False),
                        replace(self.context, initiative_type="design")):
            with self.subTest(context=context):
                self.assertTrue(self.assess(context=context).blockers)

    def test_closed_claim_cannot_be_refined_without_recorded_reopening(self):
        record = replace(self.record, alters_claim=True)
        self.assertFalse(self.assess(record, replace(self.context, closed_claim=True)).ready)
        self.assertTrue(any("reopening" in item
                            for item in self.assess(record, replace(self.context, closed_claim=True)).blockers))

    def test_stale_phase_evidence_is_not_current_readiness(self):
        self.assertTrue(any("stale phase" in item
                            for item in self.assess(replace(self.record, phase="phase-1")).blockers))

    def test_second_invocation_reuses_prepared_document_without_mutation(self):
        target = self.root / self.record.destination
        target.parent.mkdir()
        target.write_text("# Actual prepared suite\n", encoding="utf-8")
        before = target.read_bytes()
        self.assertTrue(self.assess().ready)
        self.assertTrue(self.assess().ready)
        self.assertEqual((), self.assess().recovery)
        self.assertEqual(before, target.read_bytes())

    def test_existing_stale_and_incomplete_records_are_distinguished_from_missing(self):
        target = self.root / self.record.destination
        target.parent.mkdir()
        target.write_text("# Existing customized record\n", encoding="utf-8")
        for record, state in ((replace(self.record, current=False), "stale"),
                              (replace(self.record, complete=False), "incomplete")):
            with self.subTest(state=state):
                result = self.assess(record)
                self.assertEqual((("suite", state),), result.dispositions)
                self.assertEqual((("suite", 3),), result.recovery)
                self.assertFalse(result.ready)

    def test_stage9_preparation_and_assessment_are_separate_in_actual_prompt(self):
        before_preparation = {path.relative_to(self.root).as_posix(): path.read_bytes()
                              for path in self.root.rglob("*") if path.is_file()}
        self.assertFalse(self.assess().ready)
        target = self.root / self.record.destination
        target.parent.mkdir()
        target.write_text("# Recovered earlier-stage suite\n", encoding="utf-8")
        post_preparation = {path.relative_to(self.root).as_posix(): path.read_bytes()
                            for path in self.root.rglob("*") if path.is_file()}
        self.assertNotEqual(before_preparation, post_preparation)
        readiness_input = replace(self.record, phase="phase-2", requires_verification=True)
        result = self.assess(readiness_input)
        self.assertFalse(result.ready)  # Paperwork did not supply the missing run.
        self.assertTrue(any("verification" in item for item in result.blockers))
        self.assertEqual(post_preparation,
                         {path.relative_to(self.root).as_posix(): path.read_bytes()
                          for path in self.root.rglob("*") if path.is_file()})
        path = next((PROTOCOL / "template/prompts").glob("09_*.md"))
        text = path.read_text(encoding="utf-8").lower()
        self.assertIn("preceding", text)
        self.assertIn("assessment", text)
        self.assertIn("read-only", text)
        self.assertIn("response", text)


if __name__ == "__main__":
    unittest.main()
