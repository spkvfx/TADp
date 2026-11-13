"""Read-only checks for canonical sources and documentary preparation.

The assessment API consumes explicitly reviewed facts. It cannot authenticate
authority, establish semantic completeness, execute a stage, or create records.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


COVERAGE = "template/TEMPLATE-COVERAGE.md"
PROCEDURE = "WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"
_COVERAGE = re.compile(r"<!-- tadp-template-coverage -->\s*```json\s*(.*?)\s*```", re.S)
_PREREQUISITES = re.compile(r"<!--\s*tadp-prerequisites:\s*(.*?)\s*-->", re.S)
_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class Issue:
    code: str
    path: str
    message: str


def _inside(root: Path, path: str) -> Path:
    relative = PurePosixPath(path)
    if relative.is_absolute() or ".." in relative.parts or "\\" in path or ":" in path:
        raise ValueError(f"path must stay inside the project: {path}")
    resolved = (root / path).resolve()
    resolved.relative_to(root.resolve())
    return resolved


def _anchors(text: str) -> set[str]:
    anchors = set()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text):
        heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading)
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        anchors.add(slug)
    return anchors


def _locator(root: Path, value: str, section: str = "") -> None:
    path, _, fragment = value.partition("#")
    target = _inside(root, path)
    if not target.is_file():
        raise ValueError(f"canonical source is missing: {path}")
    anchor = fragment or section
    if anchor:
        text = target.read_text(encoding="utf-8")
        slug = re.sub(r"[^\w -]", "", anchor.lstrip("#").lower()).replace(" ", "-")
        if slug not in _anchors(text):
            raise ValueError(f"source section is missing: {path}#{anchor}")


def load_coverage(root: Path) -> list[dict]:
    text = (root / COVERAGE).read_text(encoding="utf-8")
    match = _COVERAGE.search(text)
    if not match:
        raise ValueError("missing canonical JSON coverage block")
    payload = json.loads(match.group(1))
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise ValueError("unsupported coverage schema")
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("coverage records must be a nonempty list")
    return records


def installed(root: Path) -> bool:
    if (root / COVERAGE).exists():
        return True
    suite = root / "evidence/authoritative/LLM"
    return any("TEMPLATE-COVERAGE.md" in path.read_text(encoding="utf-8")
               for path in suite.glob("0[28]_*.md"))


def validate_contract(root: Path) -> list[Issue]:
    """Check installed source coverage and declarations; never repair files."""
    if not installed(root):
        return []  # Earlier distributions retain their recorded contract.
    issues = []
    try:
        records = load_coverage(root)
    except (OSError, UnicodeError, ValueError, TypeError) as error:
        return [Issue("TADP050", COVERAGE, str(error))]
    ids = set()
    for record in records:
        try:
            if not isinstance(record, dict):
                raise ValueError("coverage row is not an object")
            for key in ("id", "source", "destination", "kind", "owner", "trigger",
                        "evidence", "governing_requirement", "use", "verification", "disposition"):
                if key not in record or record[key] in (None, "", []):
                    raise ValueError(f"coverage row lacks {key}")
            if "section" not in record or "conditional" not in record:
                raise ValueError("coverage row lacks section or conditional applicability")
            if record["conditional"] is None or record["conditional"] == "":
                raise ValueError("conditional applicability must be explicit")
            for key in ("id", "source", "section", "destination", "kind", "trigger",
                        "governing_requirement", "use", "verification", "disposition"):
                if not isinstance(record[key], str):
                    raise ValueError(f"coverage field {key} must be text")
            identity = record["id"]
            if not isinstance(identity, str) or identity in ids:
                raise ValueError(f"duplicate or invalid coverage ID: {identity}")
            ids.add(identity)
            if record["kind"] not in {"file", "section", "response"}:
                raise ValueError(f"invalid kind for {identity}")
            if record["kind"] == "section" and not record.get("section"):
                raise ValueError(f"embedded source {identity} lacks its section")
            _locator(root, record["source"], record.get("section", ""))
            _locator(root, record["governing_requirement"])
            if record["kind"] != "response":
                destination = record["destination"]
                _inside(root, destination)
                if PurePosixPath(destination).parts[0] == "template":
                    raise ValueError(f"instance destination is protected: {destination}")
        except (OSError, UnicodeError, ValueError, TypeError, KeyError, IndexError) as error:
            issues.append(Issue("TADP050", COVERAGE, str(error)))
    for record in records:
        if isinstance(record, dict):
            members = record.get("members", [])
            if not isinstance(members, list):
                issues.append(Issue("TADP050", COVERAGE, "members must be a list of coverage IDs"))
                continue
            for member in members:
                if not isinstance(member, str) or member not in ids:
                    issues.append(Issue("TADP050", COVERAGE, f"unknown member ID: {member}"))
    contract = root / "template/prompts/WORKFLOW-CONTRACT.md"
    if not contract.is_file() or "documentary-prerequisite-preparation" not in _anchors(
            contract.read_text(encoding="utf-8")):
        issues.append(Issue("TADP051", "template/prompts/WORKFLOW-CONTRACT.md",
                            "shared documentary preparation procedure is missing"))
    for stage in (*range(14), "scope-closure"):
        paths = (list((root / "template/prompts").glob(f"{stage:02d}_*.md"))
                 if isinstance(stage, int) else [root / "template/prompts/scope_closure.md"])
        if len(paths) != 1 or not paths[0].is_file():
            issues.append(Issue("TADP051", "template/prompts", f"missing unique prompt for {stage}"))
            continue
        path = paths[0]
        text = path.read_text(encoding="utf-8")
        try:
            match = _PREREQUISITES.search(text)
            if not match:
                raise ValueError("missing prerequisite declaration")
            declaration = json.loads(match.group(1))
            if declaration.get("stage") != stage or declaration.get("procedure") != PROCEDURE:
                raise ValueError("prerequisite stage or shared procedure mismatch")
            names = declaration.get("records")
            if not isinstance(names, list) or not names or any(name not in ids for name in names):
                raise ValueError("prerequisites must reference known coverage IDs")
            if "## Documentary prerequisites" not in text:
                raise ValueError("missing explicit documentary prerequisites section")
            blocks = re.findall(r"(?:~~~|```)text\s*\n(.*?)(?:~~~|```)", text, re.S)
            if not any("documentary prerequisite preparation" in block.lower() for block in blocks):
                raise ValueError("executable prompt does not invoke documentary preparation")
        except (ValueError, TypeError, AttributeError) as error:
            issues.append(Issue("TADP051", path.relative_to(root).as_posix(), str(error)))
    return issues


@dataclass(frozen=True)
class Evidence:
    path: str
    locator: str
    standing: str
    revision: str = ""
    limitation: str = ""
    compatible: bool = True


@dataclass(frozen=True)
class Prerequisite:
    id: str
    destination: str
    owner: int
    evidence: tuple[Evidence, ...] = ()
    dependencies: tuple[str, ...] = ()
    current: bool = True
    complete: bool = True
    applicable: bool = True
    non_applicability: str = ""
    requires_human: bool = False
    instruction: str = ""
    author: str = ""
    event: str = ""
    requires_verification: bool = False
    verification_passed: bool = False
    phase: str = ""
    alters_claim: bool = False


@dataclass(frozen=True)
class PreparationContext:
    initiative_type: str
    allowed_types: tuple[str, ...]
    identity_verified: bool
    phase: str = ""
    closed_claim: bool = False
    reopening_recorded: bool = False
    acceptance_required: bool = False
    acceptance_recorded: bool = False


@dataclass(frozen=True)
class Assessment:
    dispositions: tuple[tuple[str, str], ...]
    recovery: tuple[tuple[str, int], ...]
    blockers: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.blockers and all(state in {"current", "not applicable"}
                                         for _, state in self.dispositions)


def assess_prerequisites(root: Path, requirements: tuple[Prerequisite, ...],
                         context: PreparationContext) -> Assessment:
    """Classify supplied facts and suggest owning-stage order, without writes.

    Exact instruction fields preserve a caller's authority assessment, not an
    authenticated approval. A constructible receipt is still missing paperwork;
    callers must prepare, validate, and recheck before the substantive activity.
    """
    blockers = []
    if not context.identity_verified:
        blockers.append("immutable target identity is unverified; return to Stage 0")
    if context.initiative_type not in context.allowed_types:
        blockers.append("wrong initiative type for the invoked activity")
    if context.acceptance_required and not context.acceptance_recorded:
        blockers.append("actual acceptance remains unresolved")
    by_id = {item.id: item for item in requirements}
    if len(by_id) != len(requirements):
        blockers.append("duplicate prerequisite identity")
    states = {}
    ordered = []
    active = set()

    def visit(item: Prerequisite) -> None:
        if item.id in states:
            return
        if item.id in active:
            blockers.append(f"{item.id}: prerequisite dependency cycle")
            return
        active.add(item.id)
        reasons = []
        for dependency in item.dependencies:
            if dependency not in by_id:
                reasons.append(f"unknown owning-stage dependency {dependency}")
            else:
                visit(by_id[dependency])
                if states.get(dependency) == "blocked":
                    reasons.append(f"blocked dependency {dependency}")
        if not item.applicable:
            state = "not applicable" if item.non_applicability.strip() else "blocked"
            if state == "blocked":
                reasons.append("conditional omission has no cited reason")
        else:
            try:
                target = _inside(root, item.destination)
                if PurePosixPath(item.destination).parts[0] == "template":
                    raise ValueError("instance destination is protected")
                for source in item.evidence:
                    _locator(root, source.path, source.locator)
                    if not source.standing or not source.compatible:
                        reasons.append("unclassified or invariant-conflicting evidence")
                if not item.evidence:
                    reasons.append("insufficient scoped source evidence")
                if item.requires_human and not all((item.instruction, item.author, item.event)):
                    reasons.append("actual sufficient human instruction is unavailable")
                if item.requires_verification and not item.verification_passed:
                    reasons.append("actual passing verification is unavailable")
                if item.phase and item.phase != context.phase:
                    reasons.append("stale phase-specific evidence")
                if item.alters_claim and context.closed_claim and not context.reopening_recorded:
                    reasons.append("closed claim needs recorded authorized reopening")
                if not target.is_file():
                    state = "constructible"
                elif not item.complete:
                    state = "incomplete"
                elif not item.current:
                    state = "stale"
                else:
                    state = "current"
            except (OSError, UnicodeError, ValueError, IndexError) as error:
                reasons.append(str(error))
                state = "blocked"
        active.discard(item.id)
        if reasons:
            state = "blocked"
            blockers.extend(f"{item.id}: {reason}" for reason in reasons)
        states[item.id] = state
        if state in {"constructible", "incomplete", "stale"}:
            ordered.append((item.id, item.owner))

    for item in requirements:
        visit(item)
    return Assessment(tuple(states.items()), tuple(ordered), tuple(blockers))


def instance_link_issues(root: Path, destination: str) -> tuple[str, ...]:
    """Check actual instance links at their destination depth, without rebasing."""
    try:
        path = _inside(root, destination)
        if PurePosixPath(destination).parts[0] == "template":
            raise ValueError("instance destination is protected")
        text = path.read_text(encoding="utf-8")
        issues = []
        for link in _LINK.findall(text):
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            target.relative_to(root.resolve())
            if not target.is_file():
                issues.append(f"instance link does not resolve at {destination}: {link}")
        return tuple(issues)
    except (OSError, UnicodeError, ValueError, IndexError) as error:
        return (str(error),)
