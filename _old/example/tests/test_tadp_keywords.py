from __future__ import annotations

import asyncio
import copy
import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

from tadp_keywords import (  # noqa: E402
    Action, ActionList, ExceptionRecord, REGISTRY_MARKER, Review, Rule,
    action_problems, evaluate_gate, execute_list, interpret, load_registry,
    registry_from_text, review_problems,
)
from tadp_validate import (  # noqa: E402
    PROTECTED_ROOTS, build_protected_lock, protected_lock_path,
    validate_keyword_contract, validate_links, validate_protected_sources,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md"


class KeywordTests(unittest.TestCase):
    def setUp(self):
        self.registry = load_registry(ROOT)

    def blocks(self, text, **kwargs):
        return interpret(text, self.registry, prompt_id="P-1", **kwargs).blocks

    def block(self, text):
        return self.blocks(text)[-1]

    def record(self, block, **changes):
        record = ExceptionRecord(
            identity="EX-1", author="agent-A", captured="test event", rule_id="R-1",
            rule_source="rule.md#gate", governing_revision="r1", gate_class="human",
            original_requirement="Ask the human", replacement="Use documented evidence method",
            prompt_id=block.prompt_id, block_id=block.block_id,
            keyword=block.setting_sources["human_gates"], targets=("INIT-1",),
            end_condition="this source block finishes", human_instruction="Resolve Q-1 by method M",
            human_authority="User for INIT-1", authority_receipt="DR-1",
            rationale="bounded delegation", consequences="agent disposition", risks="method may err",
            evidence_limits="local evidence only", prior_state="Q-1 unresolved; initiative Proposed",
            effective_settings=dict(block.settings), affected_ids=("Q-1",),
            decision_method="M: compare named authoritative evidence",
            disposition_author="agent-A", agent_dispositions="agent-A recommends outcome X for Q-1",
            reconciliation="question, decision register and source mapping linked",
            remaining_obligations="TADp locks and independent verification enforced",
            restoration="recheck ordinary gate on later gated work", disposition="excepted",
        )
        return replace(record, **changes)

    def rule(self, **changes):
        return replace(Rule("R-1", "rule.md#gate", "r1", "human", "Ask the human"), **changes)

    def test_default_and_separate_prompt_have_no_gate_waivers(self):
        default = self.block("Inspect the claim.")
        self.assertEqual(dict(self.registry.initial), default.settings)
        self.block("[tadp:ungated] earlier")
        self.assertTrue(self.block("next prompt").settings["human_gates"])
        self.assertTrue(self.block("next prompt").settings["other_gates"])

    def test_mid_line_switch_and_source_offsets(self):
        blocks = self.blocks("Before [tadp:robotic] after")
        self.assertTrue(blocks[0].settings["human_gates"])
        self.assertFalse(blocks[1].settings["human_gates"])
        self.assertTrue(blocks[1].settings["other_gates"])
        self.assertEqual(" after", blocks[1].text)
        self.assertEqual("P-1:21-27", blocks[1].block_id)

    def test_gate_forms_change_only_their_declared_settings(self):
        cases = (("!robotic", True, False), ("robotic", False, False),
                 ("!ungated", True, True))
        for token, human, other in cases:
            with self.subTest(token=token):
                blocks = self.blocks(f"[tadp:ungated] A [tadp:{token}] B")
                self.assertFalse(blocks[0].settings["human_gates"])
                self.assertFalse(blocks[0].settings["other_gates"])
                self.assertEqual(human, blocks[-1].settings["human_gates"])
                self.assertEqual(other, blocks[-1].settings["other_gates"])

    def test_repetition_paragraphs_and_adjacent_tokens(self):
        block = self.block("[tadp:robotic][tadp:robotic] A\n\nB\n- C")
        self.assertFalse(block.settings["human_gates"])
        self.assertEqual(" A\n\nB\n- C", block.text)
        self.assertTrue(self.block("[tadp:robotic][tadp:!robotic] A").settings["human_gates"])

    def test_all_forms_and_negative_forms_preserve_other_settings(self):
        for token, changes in self.registry.directives.items():
            with self.subTest(token=token):
                block = self.block(f"[tadp:preview][tadp:local][tadp:review] {token} work")
                prior = dict(self.registry.initial, preview=True, local=True, review=True)
                prior.update(changes)
                self.assertEqual(prior, block.settings)

    def test_quoted_code_and_supporting_sources_are_inert(self):
        text = ('"[tadp:ungated]" \'[tadp:robotic]\' `[tadp:preview]`\n'
                '> [tadp:local]\n```text\n[tadp:review]\n```\nContinue')
        self.assertEqual(dict(self.registry.initial), self.block(text).settings)
        for source_kind in ("attachment", "tool-output", "evidence"):
            self.assertEqual(dict(self.registry.initial),
                             self.blocks("[tadp:ungated] A", source_kind=source_kind)[0].settings)

    def test_curly_quotes_and_indented_code_remain_inert(self):
        for text in ("Explain “ [tadp:preview] ”", "Explain ‘ [tadp:robotic] ’",
                     "Example:\n\n    [tadp:preview] code\nContinue", "Example:\n\n\t[tadp:local] code"):
            self.assertEqual(dict(self.registry.initial), self.block(text).settings)

    def test_source_settings_snapshots_cannot_mutate_other_branches(self):
        block = self.block("[tadp:robotic] act")
        with self.assertRaises(TypeError):
            block.settings["human_gates"] = True
        with self.assertRaises(TypeError):
            block.settings.update({"human_gates": True})
        with self.assertRaises(TypeError):
            block.setting_sources.clear()
        self.assertFalse(block.settings["human_gates"])

    def test_human_can_explicitly_designate_example_as_operative(self):
        text = '"[tadp:robotic]" act'
        self.assertFalse(self.blocks(text, operative_ranges=((1, 15),))[-1].settings["human_gates"])
        self.assertTrue(self.blocks("[tadp:robotic] is described", inert_ranges=((0, 27),))[0].settings["human_gates"])

    def test_nested_list_indentation_does_not_reset_or_hide_switch(self):
        block = self.block("1. Parent\n   - First\n     [tadp:robotic] Child\n2. Later")
        self.assertFalse(block.settings["human_gates"])

    def test_invalid_tokens_and_path_boundaries_never_activate(self):
        invalid = ("tadp:robotic", "/tadp:robotic", "[TADP:robotic]", "[tadp:Robotic]",
                   "[tadp: robotic]", "[tadp:! robotic]", "[tadp:robotic", "[[tadp:robotic]]",
                   "file/[tadp:robotic]", "https://x/[tadp:robotic]", "x[tadp:robotic]",
                   "[tadp:robotic].txt", "[tadp:robotic]suffix", "[tadp:robotic-extra]",
                   "x[tadp:robotic][tadp:ungated]")
        for text in invalid:
            with self.subTest(text=text):
                self.assertEqual(dict(self.registry.initial), self.block(text + " work").settings)
        self.assertFalse(self.block("([tadp:robotic]), work").settings["human_gates"])

    def test_unknown_and_generic_placeholders_reported_without_effect(self):
        result = interpret("[tadp:keyword] [tadp:unknown] act", self.registry, prompt_id="P")
        self.assertEqual(2, len(result.diagnostics))
        self.assertIn("unregistered", result.diagnostics[0])
        self.assertEqual(dict(self.registry.initial), result.blocks[0].settings)

    def test_inferred_switch_requires_confirmation(self):
        self.assertTrue(self.blocks("[tadp:robotic] A", inferred=True)[0].settings["human_gates"])
        self.assertFalse(self.blocks("[tadp:robotic] A", inferred=True, confirmed=True)[0].settings["human_gates"])

    def test_gate_request_needs_exact_authority_record_before_reliance(self):
        block = self.block("[tadp:robotic] Resolve Q-1")
        self.assertFalse(evaluate_gate(self.rule(), "pending", block).allowed)
        record = self.record(block)
        result = evaluate_gate(self.rule(), "pending", block, record, target="INIT-1", scope_active=True)
        self.assertTrue(result.allowed)
        self.assertEqual("excepted", result.disposition)
        self.assertEqual("pending", result.observed)
        # Same confirmed bounded method and receipt can cover retries of this exact block.
        self.assertEqual(result, evaluate_gate(self.rule(), "pending", block, record,
                                               target="INIT-1", scope_active=True))
        self.assertEqual("agent-A", record.disposition_author)
        self.assertEqual(("Q-1",), record.affected_ids)

    def test_missing_authority_scope_target_or_confirmation_blocks(self):
        block = self.block("[tadp:robotic] Resolve Q-1")
        record = self.record(block)
        for changes in ({"human_instruction": ""}, {"rule_id": "another-rule"},
                        {"governing_revision": "r2"}, {"block_id": "another-block"},
                        {"targets": ("INIT-2",)}, {"keyword": "[tadp:ungated]"},
                        {"inferred": True}, {"effective_settings": {}}, {"disposition": "passed"}):
            with self.subTest(changes=changes):
                self.assertFalse(evaluate_gate(self.rule(), "pending", block,
                    replace(record, **changes), target="INIT-1", scope_active=True).allowed)
        self.assertFalse(evaluate_gate(self.rule(), "pending", block, record,
                                       target="INIT-1", scope_active=False).allowed)

    def test_robotic_does_not_waive_an_automated_failure(self):
        block = self.block("[tadp:robotic] execute")
        automated = self.rule(gate_class="other", requirement="Test passes")
        self.assertFalse(evaluate_gate(automated, "failed", block).allowed)

    def test_locks_remain_enforced_in_all_gate_modes(self):
        for token in ("robotic", "ungated", "!robotic", "!ungated"):
            block = self.block(f"[tadp:{token}] work")
            self.assertFalse(evaluate_gate(self.rule(lock=True), "failed", block).allowed)
        self.assertTrue(evaluate_gate(self.rule(lock=True), "passed", block).allowed)

    def test_restoring_gates_does_not_turn_skipped_evidence_into_pass(self):
        before, after = self.blocks("[tadp:ungated] A [tadp:!ungated] B")
        result = evaluate_gate(self.rule(), "skipped", before, self.record(before),
                               target="INIT-1", scope_active=True)
        self.assertEqual("skipped", result.observed)
        self.assertEqual("excepted", result.disposition)
        self.assertFalse(evaluate_gate(self.rule(), result.observed, after).allowed)

    def test_preview_prohibits_all_mutations_and_adopted_exception_records(self):
        block = self.block("[tadp:preview][tadp:robotic] propose")
        for action in ({"writes": True}, {"external_effect": True}, {"state_changing_check": True}):
            self.assertTrue(action_problems(block, permitted=True, **action))
        self.assertEqual((), action_problems(block, permitted=True, network=True))
        self.assertFalse(evaluate_gate(self.rule(), "pending", block, self.record(block),
                                       target="INIT-1", scope_active=True).allowed)
        earlier, later = self.blocks("[tadp:preview] proposal [tadp:!preview] execute")
        self.assertTrue(action_problems(earlier, permitted=True, writes=True))
        self.assertEqual((), action_problems(later, permitted=True, writes=True))

    def test_local_forbids_external_access_without_granting_negative_authority(self):
        first, later = self.blocks("[tadp:local][tadp:ungated] A [tadp:!local] B")
        self.assertTrue(action_problems(first, permitted=True, network=True))
        self.assertTrue(action_problems(first, permitted=True, external_effect=True))
        self.assertEqual((), action_problems(first, permitted=True, writes=True))
        self.assertTrue(action_problems(later, permitted=False, network=True))

    def test_review_is_independent_actual_output_and_findings_reconciled(self):
        first, later = self.blocks("[tadp:review] A [tadp:!review] B")
        review = Review("output-A", "producer", "reviewer", "no findings", "verified")
        self.assertEqual((), review_problems(first, "output-A", review))
        for invalid in (None, replace(review, reviewer="producer"), replace(review, available=False),
                        replace(review, output_id="different"), replace(review, unresolved=True),
                        replace(review, producer="")):
            self.assertTrue(review_problems(first, "output-A", invalid))
        self.assertEqual((), review_problems(later, "output-B", None))
        self.assertTrue(review_problems(first, "output-A", None))
        self.assertTrue(review_problems(later, "output-B", None, ordinarily_required=True))

    def test_all_five_settings_compose_without_cross_reset(self):
        block = self.block("[tadp:preview][tadp:local][tadp:robotic][tadp:review][tadp:!ungated] A")
        self.assertEqual(dict(self.registry.initial, preview=True, local=True, review=True), block.settings)
        self.assertTrue(action_problems(block, permitted=True, writes=True))
        self.assertTrue(action_problems(block, permitted=True, network=True))
        self.assertTrue(review_problems(block, "actual", None))

    def registry_data(self):
        return json.loads(SPEC.read_text(encoding="utf-8").split(REGISTRY_MARKER)[1].split("```json", 1)[1].split("```", 1)[0])

    def encoded_registry(self, data):
        return REGISTRY_MARKER + "\n```json\n" + json.dumps(data) + "\n```\n"

    def test_authoritative_extension_requires_no_competing_name_allowlist(self):
        data = self.registry_data()
        data["initial_settings"]["diagnostics"] = False
        data["definitions"].append({"id": "TEST-EXT-001", "name": "diagnostics",
                                    "positive": {"diagnostics": True}, "inverse": {"diagnostics": False}})
        # This synthetic source models the already-authorized protected addition;
        # authorship/adoption authority and lock review are separate human checks.
        registry = registry_from_text(self.encoded_registry(data))
        result = interpret("[tadp:diagnostics][tadp:robotic] A [tadp:!diagnostics] B", registry, prompt_id="E")
        self.assertTrue(result.blocks[0].settings["diagnostics"])
        self.assertFalse(result.blocks[-1].settings["diagnostics"])
        self.assertFalse(result.blocks[-1].settings["human_gates"])

    def test_registry_rejects_duplicates_conflicts_bad_names_and_default_drift(self):
        original = self.registry_data()
        variants = []
        data = copy.deepcopy(original); data["definitions"].append(data["definitions"][0]); variants.append(data)
        data = copy.deepcopy(original); data["definitions"][0]["name"] = "Robotic"; variants.append(data)
        data = copy.deepcopy(original); data["definitions"][0]["positive"] = {"undeclared": True}; variants.append(data)
        data = copy.deepcopy(original); data["initial_settings"]["human_gates"] = False; variants.append(data)
        variants.extend((None, [], {"schema_version": 2}))
        for data in variants:
            with self.subTest(data=data):
                with self.assertRaises(ValueError):
                    registry_from_text(self.encoded_registry(data))
        with self.assertRaises(ValueError):
            registry_from_text(REGISTRY_MARKER + '\n```json\n{"schema_version":1,"schema_version":1}\n```')

    def test_registry_and_universal_references_are_valid(self):
        self.assertEqual([], validate_keyword_contract(ROOT))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual([], validate_keyword_contract(root))  # pre-adoption legacy
            target = root / SPEC.relative_to(ROOT)
            target.parent.mkdir(parents=True)
            target.write_text(SPEC.read_text(encoding="utf-8"), encoding="utf-8")
            self.assertEqual({"TADP047"}, {finding.code for finding in validate_keyword_contract(root)})
            target.write_text("invalid registry", encoding="utf-8")
            self.assertIn("TADP046", {finding.code for finding in validate_keyword_contract(root)})

    def test_keyword_modes_do_not_change_protected_source_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in PROTECTED_ROOTS:
                folder = root / name; folder.mkdir(parents=True)
                (folder / "source.md").write_text("original", encoding="utf-8")
                protected_lock_path(root, name).write_text(json.dumps(build_protected_lock(root, name, "test authority")), encoding="utf-8")
            self.assertEqual([], validate_protected_sources(root))
            (root / "template/source.md").write_text("drift", encoding="utf-8")
            for token in self.registry.directives:
                self.block(token + " work")
                self.assertTrue(validate_protected_sources(root))

    def test_installed_canonical_links_resolve_in_templates_and_projects(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / SPEC.relative_to(ROOT)
            target.parent.mkdir(parents=True)
            target.write_text("# Canonical", encoding="utf-8")
            paths = {
                "template/project/AGENTS.md": str(SPEC.relative_to(ROOT)).replace("\\", "/"),
                "template/project/prompts/AGENTS.md": "../" + str(SPEC.relative_to(ROOT)).replace("\\", "/"),
                "AGENTS.md": str(SPEC.relative_to(ROOT)).replace("\\", "/"),
            }
            for name, link in paths.items():
                path = root / name; path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"[Canonical]({link})", encoding="utf-8")
            self.assertEqual([], validate_links(root))
            target.unlink()
            self.assertEqual(3, len(validate_links(root)))


class SchedulingTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.registry = load_registry(ROOT)
        self.block = interpret("act", self.registry, prompt_id="P").blocks[0]

    async def test_numbered_siblings_finish_checks_before_next_and_block_later(self):
        events = []
        async def first(block):
            events.append("first-start"); await asyncio.sleep(0); events.append("first-check"); return False
        async def second(block):
            events.append("second"); return True
        result = await execute_list(ActionList("numbered", (Action("A", self.block, first), Action("B", self.block, second))))
        self.assertEqual(["first-start", "first-check"], events)
        self.assertEqual({"A": "blocked", "B": "not started"}, result.dispositions)
        self.assertFalse(result.finished)

    async def test_bulleted_siblings_are_concurrent_and_blocked_sibling_does_not_stop_other(self):
        arrived = asyncio.Event(); events = []
        async def first(block):
            events.append("A-start"); await asyncio.wait_for(arrived.wait(), 1); events.append("A-end"); return False
        async def second(block):
            events.append("B-start"); arrived.set(); await asyncio.sleep(0); events.append("B-end"); return True
        result = await execute_list(ActionList("bulleted", (Action("A", self.block, first), Action("B", self.block, second))))
        self.assertLess(events.index("B-start"), events.index("A-end"))
        self.assertEqual("finished", result.dispositions["B"])
        self.assertFalse(result.finished)

    async def test_numbered_parent_joins_parallel_children_before_next(self):
        events = []; both = asyncio.Event()
        async def child(block):
            events.append("child-start")
            if events.count("child-start") == 2: both.set()
            await asyncio.wait_for(both.wait(), 1); events.append("child-end"); return True
        async def later(block):
            self.assertEqual(2, events.count("child-end")); events.append("later"); return True
        children = ActionList("bulleted", (Action("C1", self.block, child), Action("C2", self.block, child)))
        plan = ActionList("numbered", (Action("P1", self.block, children=children), Action("P2", self.block, later)))
        self.assertTrue((await execute_list(plan)).finished)
        self.assertEqual("later", events[-1])

    async def test_parallel_parents_keep_numbered_children_serial_and_source_settings_frozen(self):
        blocks = interpret("[tadp:ungated] A [tadp:!robotic] B", self.registry, prompt_id="P").blocks
        events = []; ready = asyncio.Event()
        async def a1(block):
            events.append("A1"); await asyncio.wait_for(ready.wait(), 1); self.assertFalse(block.settings["human_gates"]); return True
        async def a2(block):
            events.append("A2"); return True
        async def b1(block):
            events.append("B1"); ready.set(); self.assertTrue(block.settings["human_gates"]); return True
        async def b2(block):
            events.append("B2"); return True
        plan = ActionList("bulleted", (
            Action("A", blocks[0], children=ActionList("numbered", (Action("A1", blocks[0], a1), Action("A2", blocks[0], a2)))),
            Action("B", blocks[1], children=ActionList("numbered", (Action("B1", blocks[1], b1), Action("B2", blocks[1], b2)))),
        ))
        self.assertTrue((await execute_list(plan)).finished)
        self.assertLess(events.index("A1"), events.index("A2"))
        self.assertLess(events.index("B1"), events.index("B2"))
        self.assertLess(events.index("B1"), events.index("A2"))

    async def test_capacity_conflicts_reported_without_silent_serial_execution(self):
        events = []
        async def run(block): events.append("run"); return True
        plan = ActionList("bulleted", (Action("A", self.block, run), Action("B", self.block, run)))
        result = await execute_list(plan, capacity=1)
        self.assertFalse(result.finished)
        self.assertTrue(result.constraints)
        self.assertEqual([], events)

    async def test_capacity_accounts_for_parallel_descendants_across_branches(self):
        events = []
        async def run(block): events.append("run"); return True
        branch_a = ActionList("bulleted", (Action("A1", self.block, run), Action("A2", self.block, run)))
        branch_b = ActionList("bulleted", (Action("B1", self.block, run), Action("B2", self.block, run)))
        plan = ActionList("bulleted", (Action("A", self.block, children=branch_a), Action("B", self.block, children=branch_b)))
        result = await execute_list(plan, capacity=2)
        self.assertFalse(result.finished)
        self.assertTrue(result.constraints)
        self.assertEqual([], events)

    async def test_numbered_preparation_finishes_before_later_capacity_blocker(self):
        events = []
        async def run(block): events.append("prepare"); return True
        children = ActionList("bulleted", tuple(Action(str(i), self.block, run) for i in range(3)))
        plan = ActionList("numbered", (Action("prepare", self.block, run),
                                       Action("parallel-work", self.block, children=children),
                                       Action("later", self.block, run)))
        result = await execute_list(plan, capacity=2)
        self.assertEqual(["prepare"], events)
        self.assertEqual("finished", result.dispositions["prepare"])
        self.assertEqual("blocked", result.dispositions["parallel-work"])
        self.assertEqual("not started", result.dispositions["later"])
        self.assertTrue(result.constraints)

    async def test_outside_lists_allow_discretion_and_descriptive_lists_are_not_parsed(self):
        events = []
        async def run(block): events.append(block.text); return True
        text = "Requirements:\n- explain the claim\n- preserve truth"
        result = interpret(text, self.registry, prompt_id="D")
        self.assertEqual(1, len(result.blocks))  # no invented action tree from descriptive markers
        self.assertTrue((await execute_list(ActionList("outside", (Action("A", self.block, run),)))).finished)
        self.assertEqual(["act"], events)


if __name__ == "__main__":
    unittest.main()
