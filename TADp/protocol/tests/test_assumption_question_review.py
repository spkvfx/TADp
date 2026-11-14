"""Document-contract regressions for owned review decisions.

Run against the candidate tree, or set TADP_REVIEW_ROOT to an assembled clean
installation. These checks detect conflicting instructions and missing record
contracts; they do not authenticate authority or prove an LLM's future answers.
The isolated workflow trial and independent semantic review remain necessary.
"""
from pathlib import Path
import json
import os
import re
import unittest


ROOT = Path(os.environ.get("TADP_REVIEW_ROOT", Path(__file__).resolve().parents[1]))


def read(relative):
    return (ROOT / "template" / relative).read_text(encoding="utf-8-sig")


def compact(text):
    return re.sub(r"\s+", " ", text).lower()


class OwnedReviewContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = compact(read("prompts/WORKFLOW-CONTRACT.md"))
        cls.prompts = {
            number: compact(read(f"prompts/{number}_{name}.md"))
            for number, name in (
                ("05", "initiative_assumption_review"),
                ("06", "initiative_open_question_review"),
            )
        }

    def test_both_reviews_explicitly_allow_independent_either_kind_discovery(self):
        for number, text in self.prompts.items():
            with self.subTest(stage=number):
                self.assertRegex(text, r"(?:discover|defin|creat)[a-z]*")
                self.assertIn("new assumption", text)
                self.assertIn("new open question", text)
                self.assertRegex(text, r"(?:without waiting|without a prior|independent)")
                self.assertIn("unresolved", text)

    def test_no_blanket_initiative_scope_or_prior_answer_rejection(self):
        forbidden = (
            "which option or in-scope answer",
            "provide another in-scope answer",
            "without changing the external target",
            "real, in-scope boundary or uncertainty",
            "do not broaden the initiative, introduce a new capability, change another initiative",
        )
        for number, text in self.prompts.items():
            for phrase in forbidden:
                with self.subTest(stage=number, phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_each_review_retains_authority_and_independent_dispositions(self):
        for number, text in self.prompts.items():
            with self.subTest(stage=number):
                combined = text + self.contract
                for marker in ("receipt", "stable", "exact", "canonical", "owner",
                               "authority", "delegat", "unresolved", "one ready"):
                    self.assertIn(marker, combined)
                self.assertRegex(combined, r"(?:same review|same-review)")
                self.assertRegex(combined, r"(?:uncovered|not covered|outside.*delegation)")

    def test_external_preedit_and_separate_project_boundaries(self):
        for number, text in self.prompts.items():
            with self.subTest(stage=number):
                combined = text + self.contract
                for marker in ("current state", "governing revision", "branch",
                               "write", "decision authority", "handoff", "re-entry",
                               "scaffold", "repository", "fork"):
                    self.assertIn(marker, combined)

    def test_governing_consumers_do_not_restore_context_only_scope_rule(self):
        for name in (
            "02_Codex_Initiative_Governance_Specification.md",
            "07_Codex_Human_Decision_Receipt_Specification.md",
            "08_Codex_Initiative_Workflow_Specification.md",
        ):
            with self.subTest(specification=name):
                text = compact(read("project/evidence/authoritative/LLM/" + name))
                for marker in ("canonical", "owner", "authority", "unresolved"):
                    self.assertIn(marker, text)
                self.assertNotIn(
                    "ambiguous, incomplete, outside the initiative boundary, or", text
                )

    def test_conditional_project_register_has_one_canonical_coverage_destination(self):
        text = read("TEMPLATE-COVERAGE.md")
        payload = json.loads(re.search(
            r"<!-- tadp-template-coverage -->\s*```json\s*(.*?)\s*```", text, re.S
        ).group(1))
        roles = payload["records"]
        item_roles = [row for row in roles if row["destination"] ==
                      "decisions/assumptions-and-open-questions.md"]
        self.assertEqual(len(item_roles), 1)
        role = item_roles[0]
        for field in ("owner", "trigger", "evidence", "conditional", "verification"):
            self.assertTrue(role[field])
        self.assertIn("conditional", compact(json.dumps(role)))
        self.assertEqual(role["source"],
                         "template/project/decisions/assumptions-and-open-questions.template.md")
        sources = [row["source"] for row in roles
                   if row["destination"].startswith("decisions/")]
        self.assertIn("template/project/initiatives/decision-receipts/decision-receipt.template.md",
                      sources)

    def test_item_shapes_preserve_definition_provenance_and_disposition(self):
        for name in (
            "project/initiatives/assumption.template.md",
            "project/initiatives/open-questions.template.md",
            "project/decisions/assumptions-and-open-questions.template.md",
        ):
            with self.subTest(shape=name):
                text = compact(read(name))
                for marker in ("source", "origin", "canonical", "owner", "scope",
                               "dependenc", "affected", "unresolved", "receipt"):
                    self.assertIn(marker, text)

    def test_receipt_distinguishes_review_owner_and_actual_decision_author(self):
        text = compact(read("project/initiatives/decision-receipts/decision-receipt.template.md"))
        for marker in ("originating", "canonical", "target", "exact human response",
                       "authority", "agent", "method", "covered"):
            self.assertIn(marker, text)

    def test_shared_receipt_still_supports_separately_authorized_lifecycle_events(self):
        text = compact(read("project/initiatives/decision-receipts/decision-receipt.template.md"))
        self.assertIn("separately authorized lifecycle and exception events", text)
        self.assertIn("by itself", text)
        self.assertIn("own exact governing requirements", text)

    def test_preservation_and_coverage_limits_survive_both_entry_points(self):
        for number, text in self.prompts.items():
            with self.subTest(stage=number):
                combined = text + self.contract
                for marker in ("dormant", "trigger", "derived", "blocking",
                               "coverage", "reopen", "acceptance", "independent outcome"):
                    self.assertIn(marker, combined)
                self.assertIn("unresolved", combined)

    def test_isolated_scenario_inventory_covers_both_reviews_without_live_authority(self):
        path = Path(__file__).parent / "fixtures/owned_review_scenarios.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(cases["review_entry_points"], ["05", "06"])
        self.assertIn("Synthetic", cases["standing"])
        self.assertEqual([case["id"] for case in cases["cases"]],
                         [f"REV-{number:02d}" for number in range(1, 12)])
        self.assertTrue(all(case["input"] and case["expected"] for case in cases["cases"]))


if __name__ == "__main__":
    unittest.main()
