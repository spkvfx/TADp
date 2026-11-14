"""Prospective version-scope records, read-only validation and local integration.

Machine checks establish objective consistency, not authentic human authority,
semantic fit, acceptance or completeness of the declared work inventory.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
from typing import Callable

SCOPE = re.compile(r"v(0|[1-9][0-9]*)(?:\.(0|[1-9][0-9]*))?(?:\.(0|[1-9][0-9]*))?\Z")
SCOPE_HEADERS = (
    "Scope", "Kind", "Structural parent", "Integration branch", "Captured base ref",
    "Captured base commit", "Integration target", "Source catalog", "Members",
    "Child scopes", "Closure disposition", "Integration state", "Closure evidence",
    "Merge evidence", "Governing revision",
)
MEMBER_HEADERS = (
    "Scope", "Initiative ID", "Type", "Record location", "Source notes",
    "Execution branch", "Execution mode", "Captured base ref", "Captured base commit",
    "Integration target", "Revision cycle", "Lifecycle evidence", "Integration evidence",
)
MIGRATION_HEADERS = (
    "Legacy identity/version", "Suite and exact notes", "Initiative and historical path",
    "Branch and captured base", "Governing revision", "Proposed scope membership",
    "Action", "Authority/source evidence", "Blockers and re-entry conditions", "Historical link mapping",
)
SOURCE_HEADERS = ("Suite ID", "Suite path", "Source ID", "Source scope", "Source path", "Disposition", "Routing evidence")
INTEGRATED = {"Merged", "Fast-forward", "Already integrated", "Direct placement"}
TERMINAL = {"Completed", "Cancelled", "Superseded"}


def parse_scope(value: str) -> tuple[int, ...]:
    """Exact immutable identity: v1, v1.0 and v1.0.0 remain distinct."""
    match = SCOPE.fullmatch(value)
    if not match:
        raise ValueError(f"noncanonical version scope: {value!r}")
    return tuple(int(component) for component in match.groups() if component is not None)


def scope_parent(value: str) -> str | None:
    components = parse_scope(value)
    return "v" + ".".join(map(str, components[:-1])) if len(components) > 1 else None


def adopted(text: str) -> bool:
    from tadp_validate import metadata_plain
    value = metadata_plain(text, "Version scope revision effective point")
    return bool(value and not value.lower().startswith(("not yet adopted", "installed; adoption pending")))


def adopted_for_record(path: Path, git_root: Path) -> bool:
    from tadp_validate import coherence_table, resolve_markdown_link, initiative_record_path, plain_cell
    for parent in path.parents:
        profile = parent / "project-profile.md"
        if profile.is_file():
            index = parent / "initiatives/initiative-index.md"
            if not adopted(profile.read_text(encoding="utf-8")) or not index.is_file():
                return False
            rows = coherence_table(index.read_text(encoding="utf-8"), MEMBER_HEADERS) or []
            return any(
                (target := resolve_markdown_link(row["Record location"], index)) is not None
                and initiative_record_path(target).resolve() == path.resolve()
                and plain_cell(row["Scope"]) in {ancestor.name for ancestor in path.parents}
                for row in rows
            )
        if parent == git_root:
            break
    return False


def git(root: Path, *args: str) -> str:
    result = subprocess.run(("git", "-C", str(root), *args), capture_output=True, text=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or f"Git failed: {args[0]}")
    return result.stdout.strip()


def commit(root: Path, ref: str) -> str:
    if not ref or ref.startswith("-"):
        raise ValueError("non-option Git revision required")
    return git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")


def ancestor(root: Path, before: str, after: str) -> bool:
    result = subprocess.run(("git", "-C", str(root), "merge-base", "--is-ancestor", before, after), capture_output=True)
    if result.returncode not in (0, 1):
        raise ValueError(result.stderr.decode(errors="replace"))
    return result.returncode == 0


@dataclass(frozen=True)
class IntegrationRequest:
    source: str
    target: str
    recorded_parent: str
    source_tip: str
    target_tip: str
    closure_instruction: str
    authority_record: str
    closed: bool
    all_changes_qualified: bool
    parent_open: bool = True
    no_deliverable: bool = False


@dataclass(frozen=True)
class IntegrationResult:
    state: str
    source_tip: str
    target_before: str
    target_after: str
    method: str
    failure: str = ""


def integrate_closed_child(root: Path, request: IntegrationRequest, verify: Callable[[], bool]) -> IntegrationResult:
    """Bounded local child-to-recorded-parent integration; never pushes/deletes.

    The caller must persist authority and review records first, inspect semantic
    scope and shared-work ownership, and persist the returned actual evidence.
    This helper requires the target checked out, so cannot switch away from or
    hide user work. A conflicted merge is left intact with a Blocked result.
    """
    r = request
    before = after = r.target_tip
    try:
        root = root.resolve()
        git_root = Path(git(root, "rev-parse", "--show-toplevel")).resolve()
        project_prefix = root.relative_to(git_root).as_posix()
        if not r.closed or not r.parent_open:
            raise ValueError("closure and open immediate parent are required")
        authority = (root / r.authority_record).resolve()
        if not authority.is_relative_to(root) or not r.closure_instruction.strip() or not r.authority_record.strip() or not authority.is_file():
            raise ValueError("persisted bounded closure authority required")
        if r.target != r.recorded_parent or r.source.startswith("-") or r.target.startswith("-"):
            raise ValueError("integration must target the recorded immediate parent")
        if not r.all_changes_qualified and not r.no_deliverable:
            raise ValueError("unfinished, unaccepted or unrelated changes block whole-tip integration")
        if git(root, "status", "--porcelain"):
            raise ValueError("clean worktree required")
        if git(root, "branch", "--show-current") != r.target:
            raise ValueError("recorded target must already be checked out")
        source = commit(root, "refs/heads/" + r.source)
        before = commit(root, "refs/heads/" + r.target)
        if source != r.source_tip or before != r.target_tip:
            raise ValueError("branch-tip drift requires renewed inspection and verification")
        # A branch is shared by every project in G. Whole-tip integration
        # cannot import parent/sibling changes under P-only authority.
        revisions = git(git_root, "rev-list", f"{before}..{source}").splitlines()
        changed = set()
        source_names = set()
        gitlinks = set()
        imported_symlinks = set()
        inspected_trees = {before, *revisions}
        for revision in revisions:
            # Inspect imported history too: an outside-P edit then revert still
            # imports outside-project commits despite a clean final diff.
            raw = subprocess.run(("git", "-C", str(git_root), "diff-tree", "--root", "-r", "-m", "--no-commit-id", "--name-only", "--no-renames", "-z", revision),
                                 capture_output=True, check=True).stdout
            changed.update(filter(None, raw.decode("utf-8", errors="surrogateescape").split("\0")))
            inspected_trees.update(git(git_root, "rev-list", "--parents", "-n", "1", revision).split()[1:])
        for revision in inspected_trees:
            raw = subprocess.run(("git", "-C", str(git_root), "ls-tree", "-r", "-z", revision),
                                 capture_output=True, check=True).stdout
            for entry in filter(None, raw.split(b"\0")):
                metadata, raw_name = entry.split(b"\t", 1)
                name = raw_name.decode("utf-8", errors="surrogateescape")
                source_names.add(name)
                if metadata.startswith(b"160000 "):
                    gitlinks.add(name)
                if revision in revisions and metadata.startswith(b"120000 "):
                    imported_symlinks.add(name)
        for name in changed:
            if project_prefix != "." and not name.startswith(project_prefix + "/"):
                raise ValueError("source branch includes changes outside the selected TADp project root; separate coordination authority required")
            path = git_root / name
            if not path.resolve().is_relative_to(root):
                raise ValueError("source change escapes the selected TADp project root")
            if name in gitlinks:
                raise ValueError("source change crosses a submodule ownership boundary")
            if name in imported_symlinks:
                raise ValueError("source change introduces or changes a symbolic link; resolved project containment requires separate review")
            for parent in (path, *path.parents):
                if parent == root:
                    break
                if (parent / ".git").exists():
                    raise ValueError("source change crosses a nested Git ownership boundary")
                # Reusable project-shaped library sources are not installations.
                if parent.is_relative_to(root / "template"):
                    continue
                prefix = parent.relative_to(git_root).as_posix()
                if ((parent / "prompts/AGENTS.md").is_file() and (parent / "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md").is_file()) or (
                    prefix + "/prompts/AGENTS.md" in source_names and prefix + "/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md" in source_names
                ):
                    raise ValueError("source change crosses another scaffold ownership boundary")
        if not verify():
            raise ValueError("pre-integration verification failed")
        after = commit(root, "refs/heads/" + r.target)
        if after != before or commit(root, "refs/heads/" + r.source) != source or git(root, "status", "--porcelain") or git(root, "branch", "--show-current") != r.target:
            raise ValueError("verification changed refs or worktree; renewed inspection required")
        if r.no_deliverable:
            return IntegrationResult("No deliverable", source, before, before, "No merge")
        if r.source == r.target:
            return IntegrationResult("Direct placement", source, before, before, "No self-merge")
        if ancestor(root, source, before):
            return IntegrationResult("Already integrated", source, before, before, "No merge")
        fast_forward = ancestor(root, before, source)
        result = subprocess.run(("git", "-C", str(root), "merge", "--no-edit", "--", r.source), capture_output=True, text=True)
        after = commit(root, "refs/heads/" + r.target)
        if result.returncode:
            return IntegrationResult("Blocked", source, before, after, "Merge attempted", result.stderr.strip() or result.stdout.strip())
        if not verify() or git(root, "status", "--porcelain") or commit(root, "refs/heads/" + r.target) != after:
            after = commit(root, "refs/heads/" + r.target)
            return IntegrationResult("Blocked", source, before, after, "Fast-forward" if fast_forward else "Merge", "post-integration verification failed; retain actual integration and failure")
        return IntegrationResult("Fast-forward" if fast_forward else "Merged", source, before, after, "Fast-forward" if fast_forward else "Merge")
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        return IntegrationResult("Blocked", r.source_tip, before, after, "No merge", str(error))


def validate_version_scopes(root: Path) -> list:
    """Validate explicitly adopted scope tables; never allocate or repair them."""
    from tadp_validate import (
        Finding, COMMIT_ID, MARKDOWN_LINK, coherence_table, metadata_plain,
        metadata_value, plain_cell, relative, resolve_markdown_link, initiative_record_path,
        TYPE_LINE, resolves_within,
    )
    profile = root / "project-profile.md"
    text = profile.read_text(encoding="utf-8") if profile.is_file() else ""
    findings = []

    def error(path, message, code="TADP048"):
        findings.append(Finding("error", code, relative(path, root), message))

    previous_registry = previous_index = ""
    try:
        git_root = Path(git(root, "rev-parse", "--show-toplevel")).resolve()
        profile_name = profile.resolve().relative_to(git_root).as_posix()
        history = git(git_root, "log", "--format=%H", "--", profile_name).splitlines()
        prior_effective = set()
        for revision in history:
            try:
                prior = git(root, "show", f"{revision}:{profile_name}")
            except ValueError:
                continue
            if adopted(prior):
                prior_effective.add(metadata_plain(prior, "Version scope revision effective point"))
        if prior_effective and not adopted(text):
            error(profile, "adopted version-scope revision must not be removed or disabled")
            return findings
        if prior_effective and prior_effective != {metadata_plain(text, "Version scope revision effective point")}:
            error(profile, "recorded version-scope effective point must not change after adoption")
        for name in ("version-scopes.md", "initiative-index.md"):
            try:
                prior = git(root, "show", "HEAD:" + (root / "initiatives" / name).resolve().relative_to(git_root).as_posix())
                if name == "version-scopes.md":
                    previous_registry = prior
                else:
                    previous_index = prior
            except ValueError:
                pass  # Initial prospective adoption has no prior records.
    except (ValueError, OSError):
        pass  # Actual adopted declarations fail closed in commit verification below.
    if not adopted(text):
        return findings

    def links(cell, source):
        return {resolve_markdown_link(f"[record]({target})", source) for target in MARKDOWN_LINK.findall(cell)} - {None}

    def table(path, headers):
        if not path.is_file():
            error(path, "adopted version-scope record is missing")
            return []
        rows = coherence_table(path.read_text(encoding="utf-8"), headers)
        if rows is None:
            error(path, "missing or malformed version-scope table: " + ", ".join(headers))
            return []
        return rows

    effective = metadata_plain(text, "Version scope revision effective point") or ""
    try:
        if not COMMIT_ID.fullmatch(effective):
            raise ValueError("effective point must be an actual immutable commit")
        effective_commit = commit(root, effective)
        if not ancestor(root, effective_commit, commit(root, "HEAD")):
            raise ValueError("effective point is not in current history")
    except (ValueError, OSError) as exc:
        error(profile, str(exc))

    registry = root / "initiatives/version-scopes.md"
    index = root / "initiatives/initiative-index.md"
    ledger = root / "initiatives/version-scope-migration-ledger.md"
    scope_rows = table(registry, SCOPE_HEADERS)
    member_rows = table(index, MEMBER_HEADERS)
    legacy_paths = set()
    for row in table(ledger, MIGRATION_HEADERS):
        if any(not plain_cell(row[key]) for key in MIGRATION_HEADERS):
            error(ledger, "migration disposition must preserve every identity, evidence, authority, blocker and re-entry condition")
        action = plain_cell(row["Action"])
        if action not in {"Deferred", "Unmigrated", "Migrate", "Blocked", "Split", "Retained"}:
            error(ledger, f"unsupported migration action: {action}")
        if action in {"Deferred", "Unmigrated", "Retained"}:
            legacy_paths.update(initiative_record_path(path).resolve() for path in links(row["Initiative and historical path"], ledger))
            findings.append(Finding("warning", "TADP049", relative(ledger, root), "legacy identity remains under recorded revision: " + plain_cell(row["Legacy identity/version"])))

    scopes = {}
    roles = {}
    for row in scope_rows:
        scope = plain_cell(row["Scope"])
        if scope in scopes:
            error(registry, f"duplicate scope identity: {scope}")
            continue
        try:
            parts = parse_scope(scope)
        except ValueError as exc:
            error(registry, str(exc))
            continue
        scopes[scope] = row
        scope_readme = root / "initiatives" / scope / "README.md"
        scope_text = scope_readme.read_text(encoding="utf-8") if scope_readme.is_file() else ""
        if metadata_plain(scope_text, "Scope") != scope or registry.resolve() not in links(scope_text, scope_readme) or index.resolve() not in links(scope_text, scope_readme):
            error(scope_readme, "scope navigation README must preserve identity and link canonical registry and membership")
        if plain_cell(row["Kind"]).lower() != ("major", "minor", "patch")[len(parts)-1]:
            error(registry, f"wrong scope kind: {scope}")
        if any(not plain_cell(row[key]) for key in SCOPE_HEADERS):
            error(registry, f"scope {scope} lacks required identity, inventory, closure or integration metadata")
        branch = plain_cell(row["Integration branch"])
        if branch != scope or branch in roles:
            error(registry, f"conflicting scope branch role: {branch}")
        roles[branch] = scope
        parent = scope_parent(scope)
        expected_parent = parent or plain_cell(row["Captured base ref"])
        if not parent and expected_parent != metadata_plain(text, "Default integration branch"):
            error(registry, f"major {scope} creation base must match the project's recorded integration branch")
        if not parent and expected_parent in {plain_cell(item["Integration branch"]) for item in scope_rows}:
            error(registry, f"major {scope} must originate at project integration base, not a scope branch")
        if plain_cell(row["Structural parent"]) != expected_parent or plain_cell(row["Integration target"]) != expected_parent or plain_cell(row["Captured base ref"]) != expected_parent:
            error(registry, f"wrong structural parent, creation base or integration target for {scope}; expected {expected_parent}")
        base = plain_cell(row["Captured base commit"])
        try:
            if not COMMIT_ID.fullmatch(base):
                raise ValueError("captured base must be immutable commit")
            base = commit(root, base)
            if not ancestor(root, base, commit(root, "refs/heads/" + branch)):
                raise ValueError("captured creation base is not an ancestor of scope branch")
            if not ancestor(root, base, commit(root, "refs/heads/" + expected_parent)):
                raise ValueError("captured creation base is not in recorded parent history")
        except (ValueError, OSError) as exc:
            error(registry, f"{scope}: {exc}")

    def integration_evidence(paths, expected_target, source_tip=None, cycle=None, identity=None):
        for path in paths:
            if not path.is_file():
                continue
            evidence = path.read_text(encoding="utf-8")
            state = metadata_plain(evidence, "Integration state")
            if cycle and metadata_plain(evidence, "Revision cycle") != cycle:
                continue
            if identity and metadata_plain(evidence, "Initiative ID") != identity:
                continue
            if state in {"Excluded", "Transferred", "No deliverable"} and metadata_value(evidence, "Human authority"):
                return True
            if state not in INTEGRATED or metadata_plain(evidence, "Target ref") != expected_target:
                continue
            required = ("Source tip", "Target before", "Target after", "Authority", "Method", "Post-integration verification")
            if not all(metadata_value(evidence, field) for field in required) or metadata_plain(evidence, "Post-integration verification") != "Passed":
                continue
            try:
                source = commit(root, metadata_plain(evidence, "Source tip") or "")
                target = commit(root, metadata_plain(evidence, "Target after") or "")
                if source_tip and not ancestor(root, source_tip, source):
                    continue
                if not ancestor(root, source, target) or not ancestor(root, target, commit(root, "refs/heads/" + expected_target)):
                    continue
                return True
            except (ValueError, OSError):
                continue
        return False

    members = {}
    paths = set()
    for row in member_rows:
        identity = plain_cell(row["Initiative ID"])
        scope = plain_cell(row["Scope"])
        path = resolve_markdown_link(row["Record location"], index)
        readme = initiative_record_path(path).resolve() if path else None
        if identity in members or readme in paths:
            error(index, f"duplicate initiative identity or path: {identity}")
        members[identity] = (row, readme)
        paths.add(readme)
        if scope not in scopes:
            error(index, f"orphan initiative {identity}: unknown scope {scope}")
            continue
        kind = plain_cell(row["Type"])
        if readme is None or not readme.is_file() or kind not in {"implementation", "design", "planning"}:
            error(index, f"missing record or invalid type for {identity}")
            continue
        expected = root / "initiatives" / scope / kind
        if readme.parent.parent != expected.resolve():
            error(index, f"initiative {identity} must be grouped under initiatives/{scope}/{kind}/")
        record = readme.read_text(encoding="utf-8")
        status = metadata_plain(record, "Status")
        cycle = plain_cell(row["Revision cycle"])
        claim = metadata_plain(record, "Claim revision")
        if status in {"Accepted", "In progress", "Completed"}:
            receipts = readme.parent / "decision-receipts"
            accepted = [path for path in receipts.glob("*.md") if metadata_plain(path.read_text(encoding="utf-8"), "Disposition") == "Accepted"] if receipts.is_dir() else []
            if not claim or not any(metadata_plain(path.read_text(encoding="utf-8"), "Revision cycle") == cycle and metadata_plain(path.read_text(encoding="utf-8"), "Claim revision") == claim for path in accepted):
                error(readme, "current cycle and exact claim revision require renewed human acceptance evidence")
            required_records = []
            if status in {"In progress", "Completed"}:
                required_records.append("execution-record.md" if kind == "implementation" else "delivery-record.md")
            if status == "Completed":
                required_records.append("completion-evidence.md")
            for filename in required_records:
                evidence_path = readme.parent / filename
                evidence_text = evidence_path.read_text(encoding="utf-8") if evidence_path.is_file() else ""
                if metadata_plain(evidence_text, "Revision cycle") != cycle or not claim or metadata_plain(evidence_text, "Claim revision") != claim:
                    error(evidence_path, "delivery/completion evidence must certify current cycle and exact accepted claim revision")
        for column, label in (("Scope", "Version scope"), ("Initiative ID", "Initiative ID"), ("Type", "Initiative type"), ("Execution branch", "Execution branch"), ("Execution mode", "Execution mode"), ("Captured base ref", "Captured base ref"), ("Captured base commit", "Captured base commit"), ("Integration target", "Integration target"), ("Revision cycle", "Revision cycle")):
            if plain_cell(row[column]) != metadata_plain(record, label):
                error(readme, f"reciprocal {label} disagrees with canonical membership row")
        if index.resolve() not in links(record, readme):
            error(readme, "missing reciprocal canonical initiative-index link")
        branch = plain_cell(row["Execution branch"])
        mode = plain_cell(row["Execution mode"]).lower()
        if mode not in {"dedicated", "shared"} or (mode == "shared" and branch != scope) or (mode == "dedicated" and (branch in roles or not branch.startswith(f"initiative/{scope}-"))):
            error(index, f"conflicting or undeclared execution branch role: {identity}/{branch}")
        if mode == "dedicated":
            roles[branch] = identity
        if plain_cell(row["Integration target"]) != scope or (mode == "dedicated" and plain_cell(row["Captured base ref"]) != scope):
            error(index, f"initiative {identity} has wrong creation parent or integration target")
        try:
            base = plain_cell(row["Captured base commit"])
            if not COMMIT_ID.fullmatch(base):
                raise ValueError("immutable captured base commit required")
            base_commit = commit(root, base)
            try:
                branch_tip = commit(root, "refs/heads/" + branch)
            except ValueError:
                removal = links(metadata_value(record, "Branch removal evidence") or "", readme)
                status = metadata_plain(record, "Status")
                authorized = any(path.is_file() and metadata_value(path.read_text(encoding="utf-8"), "Human authority") and metadata_plain(path.read_text(encoding="utf-8"), "Branch") == branch for path in removal)
                if status not in TERMINAL or not authorized:
                    raise ValueError("absent branch requires terminal state and separately authorized removal evidence")
                branch_tip = commit(root, metadata_plain(record, "Historical branch tip") or "")
            if not ancestor(root, base_commit, branch_tip):
                raise ValueError("initiative branch does not contain captured base")
        except (ValueError, OSError) as exc:
            error(index, f"{identity}: {exc}")
        sources = links(row["Source notes"], index)
        if not sources or sources != links(metadata_value(record, "Source notes") or "", readme):
            error(readme, "precise reciprocal source-note links required")
        provenance = coherence_table(record, SOURCE_HEADERS)
        if not provenance:
            error(readme, "per-source scope, ID, disposition and routing evidence required")
        else:
            routed_sources = set()
            for source in provenance:
                source_paths = links(source["Source path"], readme)
                routed_sources.update(source_paths)
                suite_paths = links(source["Suite path"], readme)
                if not plain_cell(source["Suite ID"]) or len(suite_paths) != 1 or not all(path.is_file() for path in suite_paths):
                    error(readme, "exact suite identity and existing suite path required for each source note")
                for suite in suite_paths:
                    suite_text = suite.read_text(encoding="utf-8") if suite.is_file() else ""
                    if metadata_plain(suite_text, "Suite ID") != plain_cell(source["Suite ID"]) or metadata_plain(suite_text, "Version scope") != plain_cell(source["Source scope"]):
                        error(readme, "source suite ID/scope must match explicit suite metadata")
                    if not source_paths.issubset(links(suite_text, suite)) or "non-authoritative" not in suite_text.lower():
                        error(readme, "source suite must catalog exact notes and preserve non-authoritative standing")
                for note in source_paths:
                    note_text = note.read_text(encoding="utf-8") if note.is_file() else ""
                    if (metadata_plain(note_text, "Source ID") or metadata_plain(note_text, "Realization ID")) != plain_cell(source["Source ID"]) or metadata_plain(note_text, "Version scope") != plain_cell(source["Source scope"]):
                        error(readme, "source note ID/scope must match explicit note metadata")
                catalog_paths = links(scopes[scope]["Source catalog"], registry)
                if not (source_paths | suite_paths).issubset(catalog_paths):
                    error(registry, f"scope {scope} source catalog omits contributing suite/note provenance")
                if not source_paths or not source_paths.issubset(sources) or not links(source["Routing evidence"], readme):
                    error(readme, "source routing row must link exact source and routing evidence")
                try:
                    parse_scope(plain_cell(source["Source scope"]))
                except ValueError:
                    error(readme, "source scope must preserve exact canonical identity separately from target scope")
                if plain_cell(source["Disposition"]).lower() not in {"originate", "append", "revise", "reopen", "successor", "split"}:
                    error(readme, "unsupported per-source routing disposition")
            if routed_sources != sources:
                error(readme, "every originating and contributing source requires its own routing disposition")
        for source in sources:
            if not source.is_file() or readme not in {initiative_record_path(p).resolve() for p in links(source.read_text(encoding="utf-8") if source.is_file() else "", source)}:
                error(readme, "source notes must exist and reciprocally link target initiative")
        if not plain_cell(row["Revision cycle"]).isdigit() or int(plain_cell(row["Revision cycle"])) < 1:
            error(readme, "revision cycle must be a positive integer")
        if mode == "shared" and not links(row["Lifecycle evidence"], index):
            error(readme, "shared placement requires linked initiative-specific paths, commits and verification evidence")
        if readme not in {initiative_record_path(p).resolve() for p in links(scopes[scope]["Members"], registry)}:
            error(registry, f"scope inventory omits member {identity}")

    for scope, row in scopes.items():
        parent = scope_parent(scope)
        if parent:
            if parent not in scopes:
                error(registry, f"orphan {scope}: missing ancestor {parent}")
            elif scope not in plain_cell(scopes[parent]["Child scopes"]).split(", ") and (root / "initiatives" / scope / "README.md").resolve() not in links(scopes[parent]["Child scopes"], registry):
                error(registry, f"missing reciprocal child-scope inventory for {scope}")
        closed = plain_cell(row["Closure disposition"]).lower() in {"closed", "completed", "cancelled", "superseded", "no work"}
        if closed:
            contained = [(member, readme) for member, readme in members.values() if plain_cell(member["Scope"]) == scope]
            children = [child for child in scopes if scope_parent(child) == scope]
            for member, readme in contained:
                status = metadata_plain(readme.read_text(encoding="utf-8"), "Status") if readme and readme.is_file() else None
                if status not in TERMINAL:
                    error(registry, f"scope {scope} cannot close with open member {plain_cell(member['Initiative ID'])}")
                evidence = links(member["Integration evidence"], index)
                tip = None
                try:
                    if plain_cell(member["Execution mode"]).lower() == "dedicated":
                        try:
                            tip = commit(root, "refs/heads/" + plain_cell(member["Execution branch"]))
                        except ValueError:
                            tip = commit(root, metadata_plain(readme.read_text(encoding="utf-8"), "Historical branch tip") or "")
                    else:
                        verified = metadata_plain(readme.read_text(encoding="utf-8"), "Verified member commit")
                        if not verified:
                            for filename in ("completion-evidence.md", "execution-record.md", "delivery-record.md"):
                                path = readme.parent / filename
                                value = path.read_text(encoding="utf-8") if path.is_file() else ""
                                if metadata_plain(value, "Revision cycle") == plain_cell(member["Revision cycle"]):
                                    verified = metadata_plain(value, "Verified member commit")
                                    if verified:
                                        break
                        tip = commit(root, verified or "")
                except (ValueError, OSError):
                    if status == "Completed":
                        error(readme, "completed member requires its current verified immutable commit before scope closure")
                if status in TERMINAL and not integration_evidence(evidence, scope, tip, plain_cell(member["Revision cycle"]), plain_cell(member["Initiative ID"])):
                    error(registry, f"scope {scope} cannot close before required member integration")
            for child in children:
                child_row = scopes[child]
                try:
                    child_tip = commit(root, "refs/heads/" + child)
                except (ValueError, OSError):
                    child_tip = None
                if plain_cell(child_row["Closure disposition"]).lower() not in {"closed", "completed", "cancelled", "superseded", "no work"} or plain_cell(child_row["Integration state"]) not in INTEGRATED | {"Excluded", "Transferred", "No deliverable"} or not integration_evidence(links(child_row["Merge evidence"], registry), scope, child_tip):
                    error(registry, f"scope {scope} cannot close before child {child} closure/integration")
            if not contained and not children and plain_cell(row["Closure disposition"]).lower() != "no work":
                error(registry, f"empty scope {scope} requires explicit no-work closure")
            if not links(row["Closure evidence"], registry):
                error(registry, f"closed scope {scope} lacks closure snapshot and authority")
        if plain_cell(row["Integration state"]) in INTEGRATED and (not closed or not links(row["Merge evidence"], registry)):
            error(registry, f"integrated scope {scope} requires prior closure and actual merge evidence")

    prior_scopes = {plain_cell(row["Scope"]): row for row in (coherence_table(previous_registry, SCOPE_HEADERS) or [])}
    for scope, prior in prior_scopes.items():
        if scope not in scopes:
            error(registry, f"scope identity/history removed: {scope}")
            continue
        current = scopes[scope]
        immutable = ("Kind", "Structural parent", "Integration branch", "Captured base ref", "Captured base commit", "Integration target")
        if any(current[key] != prior[key] for key in immutable):
            error(registry, f"captured scope identity and creation base are immutable: {scope}")
        if plain_cell(prior["Closure disposition"]).lower() in {"closed", "completed", "cancelled", "superseded", "no work"} and (current["Members"] != prior["Members"] or current["Child scopes"] != prior["Child scopes"] or current["Closure disposition"] != prior["Closure disposition"]):
            registry_text = registry.read_text(encoding="utf-8")
            reopening = links(metadata_value(registry_text, "Reopening evidence") or "", registry)
            if not any(path.is_file() and metadata_plain(path.read_text(encoding="utf-8"), "Disposition") == "Reopened" and metadata_plain(path.read_text(encoding="utf-8"), "Scope") == scope and (metadata_value(path.read_text(encoding="utf-8"), "Human authority") or (metadata_value(path.read_text(encoding="utf-8"), "Human intake instruction") and metadata_value(path.read_text(encoding="utf-8"), "Governing delegation"))) for path in reopening):
                error(registry, f"closed scope {scope} additions or reopening require a new recorded reopening event")
    prior_members = {plain_cell(row["Initiative ID"]): row for row in (coherence_table(previous_index, MEMBER_HEADERS) or [])}
    for identity, prior in prior_members.items():
        if identity not in members:
            error(index, f"initiative identity/history removed: {identity}")
            continue
        row, readme = members[identity]
        if row["Scope"] != prior["Scope"] or row["Record location"] != prior["Record location"] or row["Type"] != prior["Type"]:
            error(index, f"initiative identity, scope, type and path cannot change as a notation repair: {identity}")
        assignment = ("Execution branch", "Execution mode", "Captured base ref", "Captured base commit")
        if row["Revision cycle"] != prior["Revision cycle"]:
            record = readme.read_text(encoding="utf-8") if readme and readme.is_file() else ""
            prior_records = links(metadata_value(record, "Prior revision record") or "", readme) if readme else set()
            if not prior_records or not all(path.is_file() for path in prior_records):
                error(index, f"new cycle must preserve linked prior claim and assignment snapshot: {identity}")
        if any(row[key] != prior[key] for key in assignment):
            record = readme.read_text(encoding="utf-8") if readme and readme.is_file() else ""
            if row["Revision cycle"] == prior["Revision cycle"] or not metadata_value(record, "Prior revision record"):
                error(index, f"execution reassignment requires a new revision cycle and preserved prior revision record: {identity}")

    initiatives = root / "initiatives"
    if initiatives.is_dir():
        for readme in initiatives.rglob("README.md"):
            record = readme.read_text(encoding="utf-8")
            if TYPE_LINE.search(record) and readme.resolve() not in paths | legacy_paths:
                error(readme, "orphan initiative: no canonical membership or complete legacy disposition")
    return findings
