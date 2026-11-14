#!/usr/bin/env python3
"""Read the canonical keyword registry and check explicit prompt execution plans.

This is a reference consumer, not an agent sandbox or a natural-language intent
classifier. Callers identify operative prose, rules, authority, and action trees;
this module preserves source positions and fails closed on objective omissions.
It never scans repository records to turn their contents into instructions.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Awaitable, Callable, Mapping


SPECIFICATION = "evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md"
REGISTRY_MARKER = "<!-- tadp-keyword-registry -->"
NAME = re.compile(r"[a-z][a-z0-9-]*\Z")
TOKEN = re.compile(r"\[tadp:(!?)([a-z][a-z0-9-]*)\]")
ADJOINING = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./\\:!%#@?=&+~-")
REQUIRED_INITIAL = {"human_gates": True, "other_gates": True,
                    "preview": False, "local": False, "review": False}


class FrozenSettings(dict):
    """JSON-compatible immutable snapshot for source-position handoffs."""

    def _immutable(self, *args, **kwargs):
        raise TypeError("source-position settings are immutable")

    __setitem__ = __delitem__ = clear = pop = popitem = setdefault = update = _immutable

    def __ior__(self, other):
        return self._immutable(other)


@dataclass(frozen=True)
class Registry:
    initial: Mapping[str, bool]
    directives: Mapping[str, Mapping[str, bool]]
    definition_ids: tuple[str, ...]


def registry_from_text(text: str) -> Registry:
    """Load only the uniquely marked authoritative JSON block, never examples."""
    if text.count(REGISTRY_MARKER) != 1:
        raise ValueError("expected exactly one canonical keyword registry marker")
    match = re.match(r"\s*```json\s*\n(.*?)\n```", text.split(REGISTRY_MARKER, 1)[1], re.S)
    if not match:
        raise ValueError("canonical registry must be a JSON fenced block")
    try:
        data = json.loads(match.group(1), object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, TypeError) as error:
        raise ValueError(f"invalid keyword registry JSON: {error}") from error
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        raise ValueError("unsupported keyword registry schema")
    initial = data.get("initial_settings")
    if not isinstance(initial, dict) or any(type(value) is not bool for value in initial.values()):
        raise ValueError("initial_settings must contain boolean settings")
    if any(initial.get(key) is not value for key, value in REQUIRED_INITIAL.items()):
        raise ValueError("ordinary initial gate and restriction settings must be preserved")
    definitions = data.get("definitions")
    if not isinstance(definitions, list) or not definitions:
        raise ValueError("registry definitions must be a non-empty list")
    directives: dict[str, dict[str, bool]] = {}
    ids: set[str] = set()
    for definition in definitions:
        if not isinstance(definition, dict):
            raise ValueError("keyword definition must be an object")
        name, identity = definition.get("name"), definition.get("id")
        if not isinstance(name, str) or not NAME.fullmatch(name):
            raise ValueError("keyword name must use canonical lowercase syntax")
        if not isinstance(identity, str) or not identity.strip() or identity in ids:
            raise ValueError("keyword definition IDs must be non-empty and unique")
        ids.add(identity)
        for form, inverse in (("positive", ""), ("inverse", "!")):
            token = f"[tadp:{inverse}{name}]"
            if token in directives:
                raise ValueError(f"duplicate keyword spelling: {token}")
            changes = definition.get(form)
            if not isinstance(changes, dict) or not changes:
                raise ValueError(f"{identity} {form} must explicitly change settings")
            if any(key not in initial or type(value) is not bool for key, value in changes.items()):
                raise ValueError(f"{identity} refers to undeclared or non-boolean settings")
            directives[token] = dict(changes)
    return Registry(dict(initial), directives, tuple(sorted(ids)))


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate registry JSON key: {key}")
        result[key] = value
    return result


def load_registry(root: Path) -> Registry:
    return registry_from_text((root / SPECIFICATION).read_text(encoding="utf-8"))


@dataclass(frozen=True)
class Block:
    prompt_id: str
    block_id: str
    start: int
    end: int
    text: str
    settings: Mapping[str, bool]
    setting_sources: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Interpretation:
    blocks: tuple[Block, ...]
    diagnostics: tuple[str, ...]


def markdown_inert_ranges(text: str) -> list[tuple[int, int]]:
    """Conservative lexical examples; semantic explanatory spans remain caller-owned."""
    ranges: list[tuple[int, int]] = []
    fence: tuple[str, int, int] | None = None
    offset = 0
    list_indents: list[tuple[int, int]] = []
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^[ \t]*(`{3,}|~{3,})", line)
        if fence:
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= fence[1]:
                ranges.append((fence[2], offset + len(line)))
                fence = None
        elif marker:
            fence = (marker.group(1)[0], len(marker.group(1)), offset)
        elif re.match(r"^[ \t]*>", line):
            ranges.append((offset, offset + len(line)))
        elif line.strip():
            expanded = line.expandtabs(4)
            indent = len(expanded) - len(expanded.lstrip(" "))
            item = re.match(r"^( *)(?:[-*+]|\d+[.)]) +", expanded)
            while list_indents and indent <= list_indents[-1][0]:
                list_indents.pop()
            threshold = list_indents[-1][1] + 4 if list_indents else 4
            if indent >= threshold:
                ranges.append((offset, offset + len(line)))
            elif item:
                list_indents.append((indent, item.end()))
        offset += len(line)
    if fence:
        ranges.append((fence[2], len(text)))
    for pattern in (r"(`+)([^\r\n]*?)\1", r'"[^"\r\n]*"', r"(?<!\w)'[^'\r\n]*'(?!\w)",
                    r"“[^”\r\n]*”", r"‘[^’\r\n]*’", r"<!--.*?-->"):
        ranges.extend((match.start(), match.end()) for match in re.finditer(pattern, text, re.S))
    return ranges


def interpret(text: str, registry: Registry, *, prompt_id: str,
              inert_ranges: tuple[tuple[int, int], ...] = (),
              operative_ranges: tuple[tuple[int, int], ...] = (),
              source_kind: str = "human", inferred: bool = False,
              confirmed: bool = False) -> Interpretation:
    """Interpret a single source prompt. A new call always starts at initial state.

    Explicit human designation is represented by operative_ranges; it may make
    quoted text operative. Callers must not supply such ranges on their own
    inference. Attachments/tool output/evidence are wholly inert by default.
    Offsets are Unicode code-point offsets in the unmodified source text.
    """
    if not prompt_id:
        raise ValueError("source prompt identity is required")
    for start, end in (*inert_ranges, *operative_ranges):
        if not 0 <= start <= end <= len(text):
            raise ValueError("invalid source range")
    inert = [*markdown_inert_ranges(text), *inert_ranges]
    if source_kind != "human":
        inert.append((0, len(text)))
    state = dict(registry.initial)
    setting_sources: dict[str, str] = {}
    blocks: list[Block] = []
    diagnostics: list[str] = []
    cursor = 0
    previous_token_end = -1
    matches = list(TOKEN.finditer(text))
    for index, match in enumerate(matches):
        start, end = match.span()
        explicit = any(left <= start and end <= right for left, right in operative_ranges)
        if not explicit and any(left < end and start < right for left, right in inert):
            continue
        adjacent_before = previous_token_end == start
        adjacent_after = index + 1 < len(matches) and matches[index + 1].start() == end
        if (start and not adjacent_before and (text[start - 1] in ADJOINING or text[start - 1] in "[]")):
            continue
        if end < len(text) and not adjacent_after and (text[end] in ADJOINING or text[end] in "[]"):
            continue
        previous_token_end = end
        token = match.group()
        if token not in registry.directives:
            diagnostics.append(f"unregistered directive {token} at {start}; inert")
            continue
        if inferred and not confirmed:
            diagnostics.append(f"inferred directive {token} at {start} awaits explicit human confirmation")
            continue
        if cursor < start:
            blocks.append(Block(prompt_id, f"{prompt_id}:{cursor}-{start}", cursor, start,
                                text[cursor:start], FrozenSettings(state), FrozenSettings(setting_sources)))
        state.update(registry.directives[token])
        setting_sources.update({key: token for key in registry.directives[token]})
        cursor = end
    if cursor < len(text):
        blocks.append(Block(prompt_id, f"{prompt_id}:{cursor}-{len(text)}", cursor, len(text),
                            text[cursor:], FrozenSettings(state), FrozenSettings(setting_sources)))
    return Interpretation(tuple(blocks), tuple(diagnostics))


@dataclass(frozen=True)
class Rule:
    identity: str
    source: str
    revision: str
    gate_class: str  # human or other
    requirement: str
    lock: bool = False


@dataclass(frozen=True)
class ExceptionRecord:
    identity: str
    author: str
    captured: str
    rule_id: str
    rule_source: str
    governing_revision: str
    gate_class: str
    original_requirement: str
    replacement: str
    prompt_id: str
    block_id: str
    keyword: str
    targets: tuple[str, ...]
    end_condition: str
    human_instruction: str
    human_authority: str
    authority_receipt: str
    rationale: str
    consequences: str
    risks: str
    evidence_limits: str
    prior_state: str
    effective_settings: Mapping[str, bool]
    affected_ids: tuple[str, ...]
    decision_method: str
    disposition_author: str
    agent_dispositions: str
    reconciliation: str
    remaining_obligations: str
    restoration: str
    disposition: str
    inferred: bool = False
    confirmation: str = ""
    git_evidence: str = "not yet available"

    def problems(self) -> tuple[str, ...]:
        problems = []
        for key, value in asdict(self).items():
            if key not in {"inferred", "confirmation"} and (not value or isinstance(value, str) and not value.strip()):
                problems.append(f"missing {key}")
        if self.gate_class not in {"human", "other"}:
            problems.append("invalid gate class")
        if self.disposition not in {"excepted", "waived", "skipped", "not performed"}:
            problems.append("exception disposition must not claim a passing check")
        if self.inferred and not self.confirmation.strip():
            problems.append("inferred exception requires exact human confirmation")
        return tuple(problems)


@dataclass(frozen=True)
class GateResult:
    allowed: bool
    disposition: str
    observed: str
    reason: str


def evaluate_gate(rule: Rule, observed: str, block: Block,
                  record: ExceptionRecord | None = None, *,
                  target: str = "", scope_active: bool = False) -> GateResult:
    """Check recorded scope; authentic human authority requires semantic review.

    A lock failure can never use a gate exception. Separately authorized source
    maintenance must reconcile and actually verify the lock with tadp_protect.
    """
    if rule.gate_class not in {"human", "other"}:
        raise ValueError("unknown gate class")
    if observed not in {"passed", "failed", "pending", "not performed", "skipped"}:
        raise ValueError("unknown observed gate result")
    if observed == "passed":
        return GateResult(True, "passed", observed, "observed passing evidence")
    if rule.lock:
        return GateResult(False, "blocked", observed, "TADp locks remain enforced")
    if block.settings[f"{rule.gate_class}_gates"]:
        return GateResult(False, "blocked", observed, "ordinary gate is required")
    if record is None:
        return GateResult(False, "blocked", observed, "specific authority and adopted record required")
    problems = list(record.problems())
    if not target.strip() or target not in record.targets or not scope_active:
        problems.append("exact target and active duration must be established")
    if dict(record.effective_settings) != dict(block.settings):
        problems.append("record effective settings differ from source block")
    comparisons = ((record.rule_id, rule.identity), (record.rule_source, rule.source),
                   (record.governing_revision, rule.revision),
                   (record.gate_class, rule.gate_class),
                   (record.original_requirement, rule.requirement),
                   (record.prompt_id, block.prompt_id), (record.block_id, block.block_id))
    if any(actual != expected for actual, expected in comparisons):
        problems.append("record does not cover this exact rule and source block")
    if record.keyword != block.setting_sources.get(f"{rule.gate_class}_gates"):
        problems.append("record does not identify the directive requesting this gate exception")
    if block.settings["preview"]:
        problems.append("preview exception is a response-only draft, not an adopted record")
    if problems:
        return GateResult(False, "blocked", observed, "; ".join(problems))
    return GateResult(True, record.disposition, observed,
                      "bounded recorded exception; original evidence is retained")


def action_problems(block: Block, *, permitted: bool, writes: bool = False,
                    external_effect: bool = False, network: bool = False,
                    state_changing_check: bool = False) -> tuple[str, ...]:
    problems = []
    if not permitted:
        problems.append("ordinary action authority or tool permission is missing")
    if block.settings["preview"] and (writes or external_effect or state_changing_check):
        problems.append("preview permits proposals and read-only checks only")
    if block.settings["local"] and (network or external_effect):
        problems.append("local restriction forbids external resource access or effects")
    return tuple(problems)


@dataclass(frozen=True)
class Review:
    output_id: str
    producer: str
    reviewer: str
    findings: str
    disposition: str
    available: bool = True
    unresolved: bool = False


def review_problems(block: Block, output_id: str, review: Review | None,
                    *, ordinarily_required: bool = False) -> tuple[str, ...]:
    if not block.settings["review"] and not ordinarily_required:
        return ()
    if review is None or not review.available:
        return ("independent review is unavailable or missing",)
    if (review.output_id != output_id or not review.producer.strip() or not review.reviewer.strip()
            or review.producer.strip() == review.reviewer.strip()
            or not review.findings.strip() or not review.disposition.strip() or review.unresolved):
        return ("review must independently cover this output and reconcile its findings",)
    return ()


@dataclass(frozen=True)
class Action:
    identity: str
    block: Block
    run: Callable[[Block], Awaitable[bool]] | None = None
    children: ActionList | None = None


@dataclass(frozen=True)
class ActionList:
    kind: str  # numbered, bulleted, or outside
    items: tuple[Action, ...]


@dataclass
class ScheduleResult:
    finished: bool
    dispositions: dict[str, str] = field(default_factory=dict)
    constraints: list[str] = field(default_factory=list)


async def execute_list(plan: ActionList, *, capacity: int | None = None) -> ScheduleResult:
    """Reference scheduling for caller-classified action lists, not Markdown prose.

    Callbacks must enforce actual tool permissions, dependencies, locks and gate
    results. False means blocked. Runtime concurrency never mutates block state.
    Capacity conflicts remain explicit and do not silently serialize a list.
    """
    if plan.kind not in {"numbered", "bulleted", "outside"}:
        raise ValueError("unknown action list kind")
    identities = [item.identity for item in plan.items]
    if len(set(identities)) != len(identities):
        raise ValueError("action sibling identities must be unique")
    result = ScheduleResult(True)
    if capacity is not None and (capacity < 1 or plan.kind == "bulleted" and _parallel_width(plan) > capacity):
        return ScheduleResult(False, {item.identity: "capacity conflict" for item in plan.items},
                              ["declared equal-priority parallel list exceeds available capacity"])

    async def perform(item: Action) -> ScheduleResult:
        try:
            okay = await item.run(item.block) if item.run else True
        except Exception as error:
            return ScheduleResult(False, {item.identity: "blocked"},
                                  [f"{item.identity}: {type(error).__name__}: {error}"])
        child = await execute_list(item.children, capacity=capacity) if okay and item.children else None
        okay = okay and (child is None or child.finished)
        own = ScheduleResult(okay, {item.identity: "finished" if okay else "blocked"})
        if child:
            own.dispositions.update(child.dispositions)
            own.constraints.extend(child.constraints)
        return own

    if plan.kind == "bulleted":
        outcomes = await asyncio.gather(*(perform(item) for item in plan.items))
    else:
        # Outside lists permit discretion; this consumer chooses serial order.
        outcomes = []
        for index, item in enumerate(plan.items):
            outcome = await perform(item)
            outcomes.append(outcome)
            if not outcome.finished:
                result.dispositions.update({later.identity: "not started" for later in plan.items[index + 1:]})
                break
    for outcome in outcomes:
        result.finished = result.finished and outcome.finished
        result.dispositions.update(outcome.dispositions)
        result.constraints.extend(outcome.constraints)
    return result


def _parallel_width(plan: ActionList) -> int:
    """Conservative peak ready-action capacity, including parallel descendants."""
    widths = [max(int(item.run is not None), _parallel_width(item.children) if item.children else 1)
              for item in plan.items]
    return sum(widths) if plan.kind == "bulleted" else max(widths, default=0)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="TADp root containing the canonical registry")
    parser.add_argument("--text", required=True, help="explicit human prompt prose; not an attachment")
    parser.add_argument("--prompt-id", required=True)
    args = parser.parse_args(argv)
    try:
        result = interpret(args.text, load_registry(args.root), prompt_id=args.prompt_id)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(asdict(result), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
