#!/usr/bin/env python3
"""Validate a Traceable Architecture Design Protocol repository."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import unquote

from tadp_keywords import SPECIFICATION as KEYWORD_SPECIFICATION, load_registry


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
INLINE_CODE = re.compile(r"(?<!`)`(?!`)[^`\r\n]*`(?!`)")
TOKEN = re.compile(r"\{\{[^{}]+\}\}|(?<!\{)\{[a-z][a-z0-9_]*\}(?!\})")
STATUS_LINE = re.compile(r"(?im)^\*\*Status:\*\*\s*([^\r\n]+)")
TYPE_LINE = re.compile(r"(?im)^\*\*Initiative type:\*\*\s*`?([^`\r\n]+)`?")
RESOLVED_TABLE_ROW = re.compile(
    r"(?im)^\|(?=[^\n]*\b(?:Confirmed|Corrected|Not applicable|Accepted(?:\s+\d{4}-\d{2}-\d{2})?|Deferred)\b)[^\n]*\|\s*$"
)
ACCEPTANCE_DISPOSITION = re.compile(r"(?im)^\*\*Disposition:\*\*\s*Accepted\b")
LIFECYCLE_SECTION = re.compile(
    r"(?ims)^#{2,3}\s+Lifecycle history\s*$\n(.*?)(?=^#{1,3}\s|\Z)"
)
WORK_VERSION = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)$")
COMMIT_ID = re.compile(r"^[0-9a-fA-F]{7,40}$")
MARKDOWN_CELL_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CORRELATION_EFFECTIVE_POINT = re.compile(
    r"(?im)^\*\*Correlation revision effective point:\*\*\s*(.+)$"
)

COHERENCE_REVIEW_HEADERS = (
    "Target initiative", "Lifecycle state", "Work and effort evidence",
    "Finding", "Disposition", "Record links",
)
WORK_CONFLICT_HEADERS = (
    "ID", "Source work", "Conflicting work", "States and effort",
    "Conflict and impact", "Owner", "Status", "Disposition and evidence",
)

CORRELATION_HEADERS = (
    "Work version",
    "Realization suite",
    "Initiative ID",
    "Name",
    "Type",
    "Status",
    "Dedicated branch",
    "Captured base branch",
    "Captured base commit",
    "Predecessor or successor",
    "Record location",
    "Lifecycle evidence",
    "Branch removal evidence",
    "Owner",
    "Next gate",
)

LEGACY_HEADERS = (
    "Legacy identity",
    "Canonical identity",
    "Suite",
    "Initiative",
    "Branch",
    "Action",
    "Authority/evidence",
    "Ambiguity or blocker",
)

LEGACY_WARNING_ACTIONS = {"Unmigrated", "Deferred"}
LEGACY_ACTIONS = LEGACY_WARNING_ACTIONS | {
    "Migrate",
    "Normalize",
    "Split",
    "Blocked",
}
ACTIVE_STATUSES = {"Proposed", "Accepted", "In progress"}
TERMINAL_STATUSES = {"Completed", "Cancelled", "Superseded"}

ALLOWED_STATUSES = {
    "Proposed",
    "Accepted",
    "In progress",
    "Completed",
    "Cancelled",
    "Superseded",
}

LEGAL_TRANSITIONS = {
    "Proposed": {"Accepted", "Cancelled", "Superseded"},
    "Accepted": {"In progress", "Proposed", "Cancelled", "Superseded"},
    "In progress": {"Completed", "Accepted", "Proposed", "Cancelled", "Superseded"},
    "Completed": {"Proposed", "Accepted"},
    "Cancelled": {"Proposed", "Accepted"},
    "Superseded": {"Proposed", "Accepted"},
}

PROTECTED_ROOTS = (
    "template",
    "evidence/authoritative/LLM",
)
PROTECTED_LOCK_NAME = ".tadp-lock.json"
PROTECTED_LOCK_SCHEMA_VERSION = 1
PROTECTED_HASH_ALGORITHM = "sha256-canonical-v1"
SHA256_DIGEST = re.compile(r"^[0-9a-f]{64}$")
PROJECT_PROMPT_FILES = ("AGENTS.md", "README.md")

BASE_REQUIRED_PATHS = (
    ".gitattributes",
    "README.md",
    "AGENTS.md",
    "docs/README.md",
    "docs/development/getting-started.md",
    "docs/development/architecture-and-authority.md",
    "docs/development/repository-layout.md",
    "docs/development/initiative-workflow.md",
    "docs/development/git-and-codex-requirements.md",
    "docs/development/validation-and-quality.md",
    "docs/development/developing-tadp.md",
    "docs/development/adapting-other-tools.md",
    "docs/guides/project-local-prompts-migration.md",
    "docs/guides/protected-source-integrity-migration.md",
    "docs/guides/version-realization-correlation-migration.md",
    "docs/guides/workflow-stage-0-13-migration.md",
    "evidence/README.md",
    "evidence/authoritative/README.md",
    "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md",
    "evidence/authoritative/LLM/AGENTS.md",
    "evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md",
    "evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md",
    "evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md",
    "evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md",
    "evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md",
    "evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md",
    "evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md",
    "evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md",
    "evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md",
    "evidence/non-authoritative/README.md",
    "initiatives/README.md",
    "products/README.md",
    "template/AGENTS.md",
    "template/initiatives/README.md",
    "template/initiatives/preparation-README.template.md",
    "template/initiatives/proposal/preparation-README.template.md",
    "template/project/AGENTS.md",
    "template/project/.gitattributes",
    "template/project/.githooks/pre-commit",
    "template/project/evidence/non-authoritative/realizations/realization-suite-index.template.md",
    "template/project/initiatives/version-correlation-migration-ledger.template.md",
    "template/prompts/README.md",
    "template/prompts/WORKFLOW-CONTRACT.md",
    ".githooks/pre-commit",
    "tools/tadp_protect.py",
)

INITIAL_INITIATIVE_FILES = (
    "README.md",
    "proposal/README.md",
    "proposal/proposal.md",
    "assumption.md",
    "scope-assessment.md",
    "architecture.md",
    "source-mapping.md",
    "open-questions.md",
    "implementation-roadmap.md",
    "implementation-steps.md",
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def parse_work_version(value: str) -> tuple[int, int]:
    """Parse a canonical TADp work version for numeric comparison."""

    match = WORK_VERSION.fullmatch(value.strip())
    if not match:
        raise ValueError(f"non-canonical work version: {value}")
    return int(match.group(1)), int(match.group(2))


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_markdown_separator(line: str) -> bool:
    cells = split_markdown_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def find_markdown_table(
    text: str, required_headers: tuple[str, ...]
) -> tuple[list[str], list[dict[str, str]]] | None:
    """Return the first Markdown table containing all required headers."""

    lines = text.splitlines()
    for index in range(len(lines) - 1):
        if not lines[index].lstrip().startswith("|") or not is_markdown_separator(
            lines[index + 1]
        ):
            continue
        headers = split_markdown_row(lines[index])
        if not set(required_headers).issubset(headers):
            continue
        rows: list[dict[str, str]] = []
        for row_line in lines[index + 2 :]:
            if not row_line.lstrip().startswith("|"):
                break
            cells = split_markdown_row(row_line)
            if len(cells) != len(headers):
                continue
            rows.append(dict(zip(headers, cells)))
        return headers, rows
    return None


def markdown_link(cell: str) -> tuple[str, str] | None:
    match = MARKDOWN_CELL_LINK.search(cell)
    if not match:
        return None
    return match.group(1).strip(), match.group(2).strip()


def resolve_markdown_link(cell: str, source: Path) -> Path | None:
    link = markdown_link(cell)
    if not link:
        return None
    target = unquote(link[1].split("#", 1)[0])
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    return (source.parent / target).resolve()


def plain_cell(cell: str) -> str:
    link = markdown_link(cell)
    if link:
        cell = link[0]
    return cell.strip().strip("`").strip()


def metadata_value(text: str, label: str) -> str | None:
    match = re.search(
        rf"(?im)^\*\*{re.escape(label)}:\*\*[ \t]*([^\r\n]+)", text
    )
    return match.group(1).strip().rstrip("  ") if match else None


def metadata_plain(text: str, label: str) -> str | None:
    value = metadata_value(text, label)
    return plain_cell(value) if value is not None else None


def initiative_record_path(path: Path) -> Path:
    return path if path.name.lower() == "readme.md" else path / "README.md"


def initiative_directory(path: Path) -> Path:
    return path.parent if path.name.lower() == "readme.md" else path


def git_directory(root: Path) -> Path | None:
    for candidate in (root, *root.parents):
        entry = candidate / ".git"
        if entry.is_dir():
            return entry.resolve()
        if entry.is_file():
            content = entry.read_text(encoding="utf-8", errors="replace").strip()
            if content.startswith("gitdir:"):
                target = content.split(":", 1)[1].strip()
                return (candidate / target).resolve()
    return None


def local_branch_exists(root: Path, branch: str) -> bool:
    directory = git_directory(root)
    if directory is None:
        return False
    ref = directory / "refs" / "heads" / Path(*branch.split("/"))
    if ref.is_file():
        return True
    packed = directory / "packed-refs"
    if packed.is_file():
        suffix = f" refs/heads/{branch}"
        return any(
            line.rstrip().endswith(suffix)
            for line in packed.read_text(encoding="utf-8", errors="replace").splitlines()
            if line and not line.startswith(("#", "^"))
        )
    return False


def first_code_span(cell: str) -> str | None:
    match = re.search(r"`([^`]+)`", cell)
    return match.group(1).strip() if match else None


def markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


def mask_fenced_code(text: str) -> str:
    """Mask fenced code while preserving offsets and line boundaries."""
    masked: list[str] = []
    fence_character: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", content)
        if fence_character is None and opening:
            token = opening.group(1)
            fence_character = token[0]
            fence_length = len(token)
            masked.append("".join(character if character in "\r\n" else " " for character in line))
            continue

        if fence_character is not None:
            closing = re.fullmatch(
                rf" {{0,3}}{re.escape(fence_character)}{{{fence_length},}}[ \t]*",
                content,
            )
            masked.append("".join(character if character in "\r\n" else " " for character in line))
            if closing:
                fence_character = None
                fence_length = 0
            continue

        masked.append(line)

    return "".join(masked)


def mask_markdown_code(text: str) -> str:
    fenced = mask_fenced_code(text)
    return INLINE_CODE.sub(
        lambda match: " " * len(match.group(0)),
        fenced,
    )


def is_template(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return "template" in rel.parts or path.name.endswith(".template.md")


def sha256_file(path: Path) -> str:
    content = path.read_bytes()
    if b"\0" not in content:
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            content = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def protected_lock_path(root: Path, protected_root: str) -> Path:
    return root / protected_root / PROTECTED_LOCK_NAME


def protected_source_files(root: Path, protected_root: str) -> list[Path]:
    source_root = root / protected_root
    lock_path = protected_lock_path(root, protected_root)
    if not source_root.is_dir():
        return []
    return sorted(
        path
        for path in source_root.rglob("*")
        if path.is_file() and path != lock_path and ".git" not in path.parts
    )


def protected_source_symlinks(root: Path, protected_root: str) -> list[Path]:
    source_root = root / protected_root
    if not source_root.is_dir():
        return []
    return sorted(path for path in source_root.rglob("*") if path.is_symlink())


def build_protected_lock(
    root: Path, protected_root: str, authority: str
) -> dict[str, object]:
    root = root.resolve()
    if protected_root not in PROTECTED_ROOTS:
        raise ValueError(f"unsupported protected root: {protected_root}")
    source_root = root / protected_root
    if not source_root.is_dir():
        raise ValueError(f"protected root does not exist: {protected_root}")
    authority = authority.strip()
    if not authority:
        raise ValueError("authority reference must not be empty")

    symlinks = protected_source_symlinks(root, protected_root)
    if symlinks:
        raise ValueError(
            "protected source must not be a symbolic link: "
            f"{relative(symlinks[0], root)}"
        )

    files: dict[str, str] = {}
    for path in protected_source_files(root, protected_root):
        files[path.relative_to(source_root).as_posix()] = sha256_file(path)

    return {
        "schema_version": PROTECTED_LOCK_SCHEMA_VERSION,
        "algorithm": PROTECTED_HASH_ALGORITHM,
        "protected_root": protected_root,
        "authority": authority,
        "files": files,
    }


def validate_protected_sources(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for protected_root in PROTECTED_ROOTS:
        source_root = root / protected_root
        lock_path = protected_lock_path(root, protected_root)
        lock_display = relative(lock_path, root)

        if not lock_path.is_file():
            findings.append(
                Finding(
                    "error",
                    "TADP023",
                    lock_display,
                    "protected-source lock is missing; initialize it through the governed protection workflow",
                )
            )
            continue

        try:
            payload = json.loads(lock_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            findings.append(
                Finding(
                    "error",
                    "TADP023",
                    lock_display,
                    f"protected-source lock is unreadable or invalid JSON: {error}",
                )
            )
            continue

        if not isinstance(payload, dict):
            findings.append(
                Finding(
                    "error",
                    "TADP023",
                    lock_display,
                    "protected-source lock must be a JSON object",
                )
            )
            continue

        authority = payload.get("authority")
        files = payload.get("files")
        config_valid = (
            payload.get("schema_version") == PROTECTED_LOCK_SCHEMA_VERSION
            and payload.get("algorithm") == PROTECTED_HASH_ALGORITHM
            and payload.get("protected_root") == protected_root
            and isinstance(authority, str)
            and bool(authority.strip())
            and isinstance(files, dict)
        )
        if not config_valid:
            findings.append(
                Finding(
                    "error",
                    "TADP023",
                    lock_display,
                    "protected-source lock metadata does not match the required schema, root, algorithm, or authority",
                )
            )
            continue

        locked_files: dict[str, str] = {}
        invalid_entry: str | None = None
        for name, digest in files.items():
            if not isinstance(name, str) or not isinstance(digest, str):
                invalid_entry = "file paths and digests must be strings"
                break
            pure_path = PurePosixPath(name)
            if (
                pure_path.is_absolute()
                or not pure_path.parts
                or ".." in pure_path.parts
                or name == PROTECTED_LOCK_NAME
                or not SHA256_DIGEST.fullmatch(digest)
            ):
                invalid_entry = f"invalid protected file entry: {name}"
                break
            locked_files[name] = digest
        if invalid_entry:
            findings.append(Finding("error", "TADP023", lock_display, invalid_entry))
            continue

        symlink_names: set[str] = set()
        for path in protected_source_symlinks(root, protected_root):
            try:
                symlink_names.add(path.relative_to(source_root).as_posix())
            except ValueError:
                pass
            findings.append(
                Finding(
                    "error",
                    "TADP027",
                    relative(path, root),
                    "protected sources must not be symbolic links",
                )
            )

        current_files: dict[str, Path] = {
            path.relative_to(source_root).as_posix(): path
            for path in protected_source_files(root, protected_root)
        }

        for name in sorted(current_files.keys() - locked_files.keys()):
            findings.append(
                Finding(
                    "error",
                    "TADP025",
                    relative(current_files[name], root),
                    "protected source is not recorded in its lock",
                )
            )
        for name in sorted(locked_files.keys() - current_files.keys()):
            findings.append(
                Finding(
                    "error",
                    "TADP026",
                    f"{protected_root}/{name}",
                    "locked protected source is missing",
                )
            )
        for name in sorted(current_files.keys() & locked_files.keys()):
            if name in symlink_names:
                continue
            try:
                actual_digest = sha256_file(current_files[name])
            except OSError as error:
                findings.append(
                    Finding(
                        "error",
                        "TADP024",
                        relative(current_files[name], root),
                        f"protected source cannot be hashed: {error}",
                    )
                )
                continue
            if actual_digest != locked_files[name]:
                findings.append(
                    Finding(
                        "error",
                        "TADP024",
                        relative(current_files[name], root),
                        "protected source content differs from its authorized lock",
                    )
                )

    return findings


def validate_required_paths(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    valid_git_root: Path | None = None
    for candidate in (root, *root.parents):
        git_entry = candidate / ".git"
        if git_entry.is_dir() and (git_entry / "HEAD").is_file() and (
            git_entry / "config"
        ).is_file():
            valid_git_root = candidate
            break
        if git_entry.is_file() and git_entry.read_text(
            encoding="utf-8", errors="replace"
        ).lstrip().startswith("gitdir:"):
            valid_git_root = candidate
            break
    if valid_git_root is None:
        findings.append(
            Finding(
                "error",
                "TADP012",
                ".git",
                "TADp root is not contained in a valid Git repository",
            )
        )
    elif not (valid_git_root / "AGENTS.md").is_file():
        findings.append(
            Finding(
                "error",
                "TADP022",
                relative(valid_git_root / "AGENTS.md", root),
                "TADp Git repository root has no Codex AGENTS.md entry point",
            )
        )
    for item in BASE_REQUIRED_PATHS:
        if not (root / item).exists():
            findings.append(Finding("error", "TADP001", item, "required path is missing"))
    return findings


def resolves_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return False
    return True


def validate_project_prompt_scaffold(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    prompt_root = root / "prompts"
    source_root = root / "template" / "project" / "prompts"

    if not prompt_root.is_dir():
        findings.append(
            Finding(
                "error",
                "TADP038",
                "prompts",
                "project-local prompt directory is missing from the checked scaffold root",
            )
        )
    elif not resolves_within(prompt_root, root):
        findings.append(
            Finding(
                "error",
                "TADP039",
                "prompts",
                "project-local prompt directory resolves outside the checked scaffold",
            )
        )

    for name in PROJECT_PROMPT_FILES:
        working = prompt_root / name
        source = source_root / name
        working_ready = prompt_root.is_dir() and working.is_file()
        source_ready = source.is_file()

        if prompt_root.is_dir() and not working_ready:
            findings.append(
                Finding(
                    "error",
                    "TADP038",
                    relative(working, root),
                    f"required project-local prompt file is missing: prompts/{name}",
                )
            )
        if not source_ready:
            findings.append(
                Finding(
                    "error",
                    "TADP038",
                    relative(source, root),
                    "required reusable project-local prompt source is missing",
                )
            )

        safe_working = working_ready and resolves_within(working, root)
        safe_source = source_ready and resolves_within(source, root)
        if working_ready and not safe_working:
            findings.append(
                Finding(
                    "error",
                    "TADP039",
                    relative(working, root),
                    "project-local prompt file resolves outside the checked scaffold",
                )
            )
        if source_ready and not safe_source:
            findings.append(
                Finding(
                    "error",
                    "TADP039",
                    relative(source, root),
                    "reusable project-local prompt source resolves outside the checked scaffold",
                )
            )

        if not (safe_working and safe_source):
            continue
        try:
            working_text = working.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
            source_text = source.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
        except (OSError, UnicodeError) as error:
            findings.append(
                Finding(
                    "error",
                    "TADP040",
                    relative(working, root),
                    f"cannot compare working and reusable project-local prompt files: {error}",
                )
            )
            continue

        canonical = source_text.strip()
        if not canonical or canonical not in working_text.strip():
            findings.append(
                Finding(
                    "error",
                    "TADP040",
                    relative(working, root),
                    f"working project-local prompt file does not preserve template/project/prompts/{name}",
                )
            )

    return findings


def validate_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        link_text = mask_markdown_code(text)
        for match in MARKDOWN_LINK.finditer(link_text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#", "{")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / unquote(target_path)).resolve()
            # Project instruction templates deliberately use the installed
            # project's direct canonical link. Resolve that one destination
            # against the adopting root, rather than duplicating authority
            # below template/project/evidence.
            template_keyword = (root / "template/project" / KEYWORD_SPECIFICATION).resolve()
            if resolved == template_keyword and is_template(path, root):
                resolved = (root / KEYWORD_SPECIFICATION).resolve()
            if not resolved.exists():
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    Finding(
                        "error",
                        "TADP002",
                        f"{relative(path, root)}:{line}",
                        f"local Markdown target does not exist: {target}",
                    )
                )
    return findings


def validate_tokens(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root):
        if is_template(path, root):
            continue
        text = HTML_COMMENT.sub("", path.read_text(encoding="utf-8"))
        text = mask_markdown_code(text)
        match = TOKEN.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            findings.append(
                Finding(
                    "error",
                    "TADP003",
                    f"{relative(path, root)}:{line}",
                    f"unresolved template token: {match.group(0)}",
                )
            )
    return findings


def initiative_directories(root: Path) -> list[Path]:
    result: set[Path] = set()
    for marker in ("architecture.md", "source-mapping.md", "open-questions.md"):
        for path in root.rglob(marker):
            rel = path.relative_to(root)
            if "template" in rel.parts or "evidence" in rel.parts:
                continue
            result.add(path.parent)
    return sorted(result)


def correlated_initiative_directories(root: Path) -> list[Path]:
    result = set(initiative_directories(root))
    initiative_root = root / "initiatives"
    if not initiative_root.is_dir():
        return sorted(result)

    for readme in initiative_root.rglob("README.md"):
        text = readme.read_text(encoding="utf-8")
        if metadata_plain(text, "Work version") and metadata_plain(
            text, "Initiative ID"
        ):
            result.add(readme.parent)
    return sorted(result)


def validate_initiatives(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for directory in initiative_directories(root):
        for item in INITIAL_INITIATIVE_FILES:
            if not (directory / item).exists():
                findings.append(
                    Finding(
                        "error",
                        "TADP004",
                        relative(directory / item, root),
                        "initial initiative artifact is missing",
                    )
                )

        readme = directory / "README.md"
        if readme.exists():
            text = readme.read_text(encoding="utf-8")
            status = STATUS_LINE.search(text)
            if not status:
                findings.append(
                    Finding(
                        "error",
                        "TADP005",
                        relative(readme, root),
                        "initiative README has no **Status:** metadata",
                    )
                )
            else:
                value = status.group(1).strip().rstrip("  ")
                if value not in ALLOWED_STATUSES:
                    findings.append(
                        Finding(
                            "error",
                            "TADP006",
                            relative(readme, root),
                            f"unsupported lifecycle status: {value}",
                        )
                    )

            history = LIFECYCLE_SECTION.search(text)
            if not history:
                findings.append(
                    Finding(
                        "error",
                        "TADP008",
                        relative(readme, root),
                        "initiative README has no lifecycle history",
                    )
                )
            else:
                rows: list[tuple[str, str]] = []
                for line in history.group(1).splitlines():
                    cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
                    if len(cells) < 3 or cells[0].lower().startswith("effective") or set(cells[0]) == {"-"}:
                        continue
                    prior, result = cells[1], cells[2]
                    if result not in ALLOWED_STATUSES:
                        continue
                    rows.append((prior, result))
                for index, (prior, result) in enumerate(rows):
                    valid = (index == 0 and prior == "Initial" and result == "Proposed") or (
                        prior in LEGAL_TRANSITIONS and result in LEGAL_TRANSITIONS[prior]
                    )
                    if not valid:
                        findings.append(
                            Finding(
                                "error",
                                "TADP009",
                                relative(readme, root),
                                f"illegal lifecycle transition: {prior} -> {result}",
                            )
                        )
                    if index > 0 and prior != rows[index - 1][1]:
                        findings.append(
                            Finding(
                                "error",
                                "TADP017",
                                relative(readme, root),
                                f"lifecycle history is discontinuous: expected {rows[index - 1][1]}, found {prior}",
                            )
                        )
                if status and rows:
                    declared = status.group(1).strip().rstrip("  ")
                    if declared in ALLOWED_STATUSES and rows[-1][1] != declared:
                        findings.append(
                            Finding(
                                "error",
                                "TADP018",
                                relative(readme, root),
                                f"declared status {declared} does not match lifecycle history {rows[-1][1]}",
                            )
                        )

            declared_status = status.group(1).strip().rstrip("  ") if status else None

            if declared_status == "Completed":
                if not (directory / "completion-evidence.md").exists():
                    findings.append(
                        Finding(
                            "error",
                            "TADP010",
                            relative(directory / "completion-evidence.md", root),
                            "Completed initiative has no completion evidence",
                        )
                    )

            initiative_type = TYPE_LINE.search(text)
            initiative_type_value = initiative_type.group(1).strip() if initiative_type else None
            if (
                declared_status in {"In progress", "Completed"}
                and initiative_type_value == "implementation"
                and not (directory / "execution-record.md").exists()
            ):
                findings.append(
                    Finding(
                        "error",
                        "TADP011",
                        relative(directory / "execution-record.md", root),
                        "in-progress implementation initiative has no execution record",
                    )
                )

            if (
                declared_status in {"In progress", "Completed"}
                and initiative_type_value in {"design", "planning"}
                and not (directory / "delivery-record.md").exists()
            ):
                findings.append(
                    Finding(
                        "error",
                        "TADP019",
                        relative(directory / "delivery-record.md", root),
                        f"{declared_status.lower()} {initiative_type_value} initiative has no delivery record",
                    )
                )

            receipts = directory / "decision-receipts"
            receipt_files = (
                [path for path in receipts.glob("*.md") if path.name != "README.md"]
                if receipts.is_dir()
                else []
            )
            if declared_status in {"Accepted", "In progress", "Completed"}:
                acceptance_receipts = [
                    path
                    for path in receipt_files
                    if ACCEPTANCE_DISPOSITION.search(path.read_text(encoding="utf-8"))
                ]
                if not acceptance_receipts:
                    findings.append(
                        Finding(
                            "error",
                            "TADP020",
                            relative(receipts, root),
                            f"{declared_status} initiative has no explicit acceptance receipt",
                        )
                    )
                if "decision-receipts/" not in text:
                    findings.append(
                        Finding(
                            "error",
                            "TADP021",
                            relative(readme, root),
                            "accepted lifecycle standing does not link its decision receipt",
                        )
                    )

        source_map = directory / "source-mapping.md"
        if source_map.exists():
            text = source_map.read_text(encoding="utf-8").lower()
            for heading in ("authoritative evidence", "verification evidence"):
                if heading not in text:
                    findings.append(
                        Finding(
                            "error",
                            "TADP007",
                            relative(source_map, root),
                            f"source mapping does not name a {heading} field",
                        )
                    )

        decision_sources = [directory / "assumption.md", directory / "open-questions.md"]
        resolved_sources = [
            path
            for path in decision_sources
            if path.exists() and RESOLVED_TABLE_ROW.search(path.read_text(encoding="utf-8"))
        ]
        if resolved_sources:
            receipts = directory / "decision-receipts"
            receipt_files = (
                [path for path in receipts.glob("*.md") if path.name != "README.md"]
                if receipts.is_dir()
                else []
            )
            if not receipt_files:
                findings.append(
                    Finding(
                        "error",
                        "TADP013",
                        relative(receipts, root),
                        "resolved human decision has no decision receipt",
                    )
                )
            for source in resolved_sources:
                if "decision-receipts/" not in source.read_text(encoding="utf-8"):
                    findings.append(
                        Finding(
                            "error",
                            "TADP014",
                            relative(source, root),
                            "resolved decision source does not link a decision receipt",
                        )
                    )
    return findings


def validate_version_correlation(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    profile = root / "project-profile.md"
    if not profile.is_file():
        return findings

    profile_text = profile.read_text(encoding="utf-8")
    effective = CORRELATION_EFFECTIVE_POINT.search(profile_text)
    if not effective or "not yet adopted" in effective.group(1).lower():
        return findings

    ledger_path = root / "initiatives" / "version-correlation-migration-ledger.md"
    legacy_suite_paths: set[Path] = set()
    legacy_initiative_paths: set[Path] = set()
    legacy_branches: set[str] = set()

    if not ledger_path.is_file():
        findings.append(
            Finding(
                "error",
                "TADP034",
                relative(ledger_path, root),
                "correlation revision is active but the legacy migration ledger is missing",
            )
        )
    else:
        ledger_text = ledger_path.read_text(encoding="utf-8")
        ledger_table = find_markdown_table(ledger_text, LEGACY_HEADERS)
        if ledger_table is None:
            findings.append(
                Finding(
                    "error",
                    "TADP034",
                    relative(ledger_path, root),
                    "migration ledger is missing the required eight-column table",
                )
            )
        else:
            _, legacy_rows = ledger_table
            for row_number, row in enumerate(legacy_rows, start=1):
                action = plain_cell(row["Action"])
                missing = [
                    header for header in LEGACY_HEADERS if not plain_cell(row[header])
                ]
                if missing or action not in LEGACY_ACTIONS:
                    findings.append(
                        Finding(
                            "error",
                            "TADP034",
                            relative(ledger_path, root),
                            "legacy row "
                            f"{row_number} is incomplete or has an unsupported action: "
                            + ", ".join(missing or [action]),
                        )
                    )
                    continue

                suite_path = resolve_markdown_link(row["Suite"], ledger_path)
                initiative_path = resolve_markdown_link(row["Initiative"], ledger_path)
                branch = first_code_span(row["Branch"])
                if suite_path is not None:
                    legacy_suite_paths.add(suite_path)
                if initiative_path is not None:
                    legacy_initiative_paths.add(initiative_directory(initiative_path))
                if branch:
                    legacy_branches.add(branch)

                if action in LEGACY_WARNING_ACTIONS:
                    canonical = plain_cell(row["Canonical identity"])
                    authority = row["Authority/evidence"].lower()
                    blocker = row["Ambiguity or blocker"].lower()
                    complete = (
                        not WORK_VERSION.fullmatch(canonical)
                        and "governing workflow revision:" in authority
                        and "re-entry or migration condition:" in blocker
                    )
                    if not complete:
                        findings.append(
                            Finding(
                                "error",
                                "TADP034",
                                relative(ledger_path, root),
                                f"{action} row {row_number} is partial, inferred, or lacks workflow and re-entry evidence",
                            )
                        )
                    else:
                        findings.append(
                            Finding(
                                "warning",
                                "TADP033",
                                relative(ledger_path, root),
                                f"actionable legacy disposition remains {action}: {plain_cell(row['Legacy identity'])}",
                            )
                        )

    index_path = root / "initiatives" / "initiative-index.md"
    if not index_path.is_file():
        findings.append(
            Finding(
                "error",
                "TADP029",
                relative(index_path, root),
                "correlation revision is active but the canonical initiative index is missing",
            )
        )
        return findings

    index_text = index_path.read_text(encoding="utf-8")
    correlation_table = find_markdown_table(index_text, CORRELATION_HEADERS)
    if correlation_table is None:
        findings.append(
            Finding(
                "error",
                "TADP029",
                relative(index_path, root),
                "initiative index is missing the required canonical correlation table",
            )
        )
        return findings

    _, rows = correlation_table
    seen: dict[str, dict[str, int]] = {
        "work version": {},
        "suite ID": {},
        "suite path": {},
        "initiative ID": {},
        "initiative path": {},
        "branch": {},
    }
    canonical_suite_paths: set[Path] = set()
    canonical_initiative_paths: set[Path] = set()
    governed_status_rows: dict[tuple[str, str], tuple[str, str, str]] = {}

    def remember(kind: str, value: str, row_number: int) -> None:
        if not value:
            return
        prior = seen[kind].get(value)
        if prior is not None:
            findings.append(
                Finding(
                    "error",
                    "TADP030",
                    relative(index_path, root),
                    f"duplicate {kind} mapping in rows {prior} and {row_number}: {value}",
                )
            )
        else:
            seen[kind][value] = row_number

    required_values = (
        "Work version",
        "Realization suite",
        "Initiative ID",
        "Name",
        "Type",
        "Status",
        "Dedicated branch",
        "Captured base branch",
        "Captured base commit",
        "Record location",
        "Lifecycle evidence",
        "Owner",
    )

    for row_number, row in enumerate(rows, start=1):
        version = plain_cell(row["Work version"])
        suite_link = markdown_link(row["Realization suite"])
        suite_id = suite_link[0] if suite_link else ""
        suite_path = resolve_markdown_link(row["Realization suite"], index_path)
        initiative_id = plain_cell(row["Initiative ID"])
        initiative_path = resolve_markdown_link(row["Record location"], index_path)
        initiative_dir = (
            initiative_directory(initiative_path) if initiative_path is not None else None
        )
        branch = plain_cell(row["Dedicated branch"])
        status = plain_cell(row["Status"])

        missing = [header for header in required_values if not plain_cell(row[header])]
        if suite_link is None:
            missing.append("Realization suite link")
        if initiative_path is None:
            missing.append("Record location link")
        if missing:
            findings.append(
                Finding(
                    "error",
                    "TADP029",
                    relative(index_path, root),
                    f"correlation row {row_number} is missing required metadata: "
                    + ", ".join(missing),
                )
            )

        remember("work version", version, row_number)
        remember("suite ID", suite_id, row_number)
        remember(
            "suite path", str(suite_path) if suite_path is not None else "", row_number
        )
        remember("initiative ID", initiative_id, row_number)
        remember(
            "initiative path",
            str(initiative_dir) if initiative_dir is not None else "",
            row_number,
        )
        remember("branch", branch, row_number)

        if suite_path is not None:
            canonical_suite_paths.add(suite_path)
        if initiative_dir is not None:
            canonical_initiative_paths.add(initiative_dir)

        legacy_matches = (
            suite_path is not None and suite_path in legacy_suite_paths,
            initiative_dir is not None and initiative_dir in legacy_initiative_paths,
            branch in legacy_branches,
        )
        if any(legacy_matches):
            if not all(legacy_matches):
                findings.append(
                    Finding(
                        "error",
                        "TADP034",
                        relative(index_path, root),
                        f"correlation row {row_number} mixes legacy and governed tuple fields",
                    )
                )
                continue
            if "version-correlation-migration-ledger" not in row[
                "Lifecycle evidence"
            ]:
                findings.append(
                    Finding(
                        "error",
                        "TADP034",
                        relative(index_path, root),
                        f"pre-effective correlation row {row_number} does not link its migration-ledger disposition",
                    )
                )
            continue

        try:
            parse_work_version(version)
        except ValueError:
            findings.append(
                Finding(
                    "error",
                    "TADP028",
                    relative(index_path, root),
                    f"non-canonical governed work version in row {row_number}: {version}",
                )
            )

        if status not in ALLOWED_STATUSES:
            findings.append(
                Finding(
                    "error",
                    "TADP029",
                    relative(index_path, root),
                    f"correlation row {row_number} has unsupported lifecycle status: {status}",
                )
            )

        base_commit = plain_cell(row["Captured base commit"])
        if not COMMIT_ID.fullmatch(base_commit):
            findings.append(
                Finding(
                    "error",
                    "TADP029",
                    relative(index_path, root),
                    f"correlation row {row_number} has no valid captured base commit",
                )
            )

        version_token = re.search(
            rf"(?:^|[/_-]){re.escape(version)}(?:$|[/_-])", branch
        )
        if version and version_token is None:
            findings.append(
                Finding(
                    "error",
                    "TADP035",
                    relative(index_path, root),
                    f"dedicated branch does not retain exact version token {version}: {branch}",
                )
            )

        branch_exists = local_branch_exists(root, branch)
        if status in ACTIVE_STATUSES and not branch_exists:
            findings.append(
                Finding(
                    "error",
                    "TADP035",
                    relative(index_path, root),
                    f"active initiative branch does not exist locally: {branch}",
                )
            )
        if status in TERMINAL_STATUSES and not branch_exists:
            removal = resolve_markdown_link(row["Branch removal evidence"], index_path)
            if removal is None or not removal.exists():
                findings.append(
                    Finding(
                        "error",
                        "TADP035",
                        relative(index_path, root),
                        f"absent historical branch has no linked removal authority: {branch}",
                    )
                )

        if suite_path is None or not suite_path.is_file():
            findings.append(
                Finding(
                    "error",
                    "TADP031",
                    relative(index_path, root),
                    f"correlation row {row_number} points to a missing realization suite",
                )
            )
            continue
        if initiative_path is None or not initiative_record_path(initiative_path).is_file():
            findings.append(
                Finding(
                    "error",
                    "TADP031",
                    relative(index_path, root),
                    f"correlation row {row_number} points to a missing initiative record",
                )
            )
            continue

        suite_text = suite_path.read_text(encoding="utf-8")
        initiative_readme = initiative_record_path(initiative_path)
        initiative_text = initiative_readme.read_text(encoding="utf-8")
        initiative_type = plain_cell(row["Type"])
        base_branch = plain_cell(row["Captured base branch"])

        comparisons = (
            (suite_path, "Work version", metadata_plain(suite_text, "Work version"), version),
            (suite_path, "Suite ID", metadata_plain(suite_text, "Suite ID"), suite_id),
            (suite_path, "Initiative ID", metadata_plain(suite_text, "Initiative ID"), initiative_id),
            (suite_path, "Initiative type", metadata_plain(suite_text, "Initiative type"), initiative_type),
            (suite_path, "Dedicated branch", metadata_plain(suite_text, "Dedicated branch"), branch),
            (suite_path, "Captured base branch", metadata_plain(suite_text, "Captured base branch"), base_branch),
            (suite_path, "Captured base commit", metadata_plain(suite_text, "Captured base commit"), base_commit),
            (initiative_readme, "Initiative ID", metadata_plain(initiative_text, "Initiative ID"), initiative_id),
            (initiative_readme, "Work version", metadata_plain(initiative_text, "Work version"), version),
            (initiative_readme, "Realization suite ID", metadata_plain(initiative_text, "Realization suite ID"), suite_id),
            (initiative_readme, "Initiative type", metadata_plain(initiative_text, "Initiative type"), initiative_type),
            (initiative_readme, "Status", metadata_plain(initiative_text, "Status"), status),
            (initiative_readme, "Dedicated branch", metadata_plain(initiative_text, "Dedicated branch"), branch),
            (initiative_readme, "Captured base branch", metadata_plain(initiative_text, "Captured base branch"), base_branch),
            (initiative_readme, "Captured base commit", metadata_plain(initiative_text, "Captured base commit"), base_commit),
        )
        for record, label, actual, expected in comparisons:
            if actual != expected:
                findings.append(
                    Finding(
                        "error",
                        "TADP032",
                        relative(record, root),
                        f"reciprocal {label} mismatch: expected {expected!r}, found {actual!r}",
                    )
                )

        suite_initiative = resolve_markdown_link(
            metadata_value(suite_text, "Initiative path") or "", suite_path
        )
        initiative_suite = resolve_markdown_link(
            metadata_value(initiative_text, "Realization suite") or "",
            initiative_readme,
        )
        suite_canonical = resolve_markdown_link(
            metadata_value(suite_text, "Canonical project correlation") or "",
            suite_path,
        )
        initiative_canonical = resolve_markdown_link(
            metadata_value(initiative_text, "Canonical project correlation") or "",
            initiative_readme,
        )
        if (
            suite_initiative is None
            or initiative_directory(suite_initiative) != initiative_dir
            or initiative_suite != suite_path
            or suite_canonical != index_path.resolve()
            or initiative_canonical != index_path.resolve()
        ):
            findings.append(
                Finding(
                    "error",
                    "TADP032",
                    relative(index_path, root),
                    f"correlation row {row_number} has missing or inconsistent reciprocal links",
                )
            )

        if "non-authoritative" not in suite_text.lower():
            findings.append(
                Finding(
                    "error",
                    "TADP037",
                    relative(suite_path, root),
                    "realization suite does not preserve non-authoritative evidence standing",
                )
            )

        if "## Preparation state" not in initiative_text:
            governed_status_rows[(version, initiative_id)] = (
                suite_id,
                initiative_type,
                status,
            )

    realization_root = root / "evidence" / "non-authoritative" / "realizations"
    if realization_root.is_dir():
        for suite_path in realization_root.rglob("*suite-index.md"):
            resolved = suite_path.resolve()
            if resolved not in canonical_suite_paths and resolved not in legacy_suite_paths:
                findings.append(
                    Finding(
                        "error",
                        "TADP031",
                        relative(suite_path, root),
                        "orphan or undeclared realization suite has no canonical row or legacy disposition",
                    )
                )

    for directory in correlated_initiative_directories(root):
        resolved = directory.resolve()
        if (
            resolved not in canonical_initiative_paths
            and resolved not in legacy_initiative_paths
        ):
            findings.append(
                Finding(
                    "error",
                    "TADP031",
                    relative(directory, root),
                    "orphan or undeclared initiative has no canonical row or legacy disposition",
                )
            )

    status_path = root / "initiatives" / "status.md"
    if governed_status_rows:
        if not status_path.is_file():
            findings.append(
                Finding(
                    "error",
                    "TADP029",
                    relative(status_path, root),
                    "governed correlation rows exist but the project status view is missing",
                )
            )
        else:
            status_table = find_markdown_table(
                status_path.read_text(encoding="utf-8"),
                (
                    "Work version",
                    "Initiative ID",
                    "Realization suite",
                    "Type",
                    "Status",
                    "Status evidence",
                ),
            )
            if status_table is None:
                findings.append(
                    Finding(
                        "error",
                        "TADP029",
                        relative(status_path, root),
                        "status view is missing the required reciprocal correlation table",
                    )
                )
            else:
                status_rows: dict[tuple[str, str], dict[str, str]] = {}
                for row in status_table[1]:
                    key = (
                        plain_cell(row["Work version"]),
                        plain_cell(row["Initiative ID"]),
                    )
                    if key in status_rows:
                        findings.append(
                            Finding(
                                "error",
                                "TADP032",
                                relative(status_path, root),
                                f"status view has duplicate reciprocal rows for {key[0]} / {key[1]}",
                            )
                        )
                    else:
                        status_rows[key] = row

                for key, expected in sorted(governed_status_rows.items()):
                    actual = status_rows.get(key)
                    if actual is None:
                        findings.append(
                            Finding(
                                "error",
                                "TADP032",
                                relative(status_path, root),
                                f"status view has no reciprocal row for {key[0]} / {key[1]}",
                            )
                        )
                        continue

                    actual_values = (
                        plain_cell(actual["Realization suite"]),
                        plain_cell(actual["Type"]),
                        plain_cell(actual["Status"]),
                    )
                    if actual_values != expected or markdown_link(
                        actual["Status evidence"]
                    ) is None:
                        findings.append(
                            Finding(
                                "error",
                                "TADP032",
                                relative(status_path, root),
                                f"status view metadata or evidence disagrees with {key[0]} / {key[1]}",
                            )
                        )

    return findings


def coherence_git(root: Path, *arguments: str, input_data: bytes | None = None) -> bytes:
    """Read Git evidence without changing refs, the index, or working files."""
    result = subprocess.run(
        ("git", "-C", str(root), *arguments),
        input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        raise ValueError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def coherence_commit(root: Path, ref: str) -> str:
    if not ref or ref.startswith("-"):
        raise ValueError("a non-option Git revision is required")
    return coherence_git(
        root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}"
    ).decode("ascii").strip()


def coherence_snapshot(root: Path, commit: str, prefix: str) -> dict[str, bytes]:
    entries = coherence_git(root, "ls-tree", "-r", "-z", commit, "--", prefix).split(b"\0")
    objects: list[tuple[str, bytes]] = []
    for entry in entries:
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        _, kind, object_id = metadata.split()
        if kind == b"blob":
            objects.append((name.decode("utf-8"), object_id))
    if not objects:
        return {}
    # Batch raw blobs, preserving bytes and ignoring export-ignore attributes.
    stream = io.BytesIO(coherence_git(
        root, "cat-file", "--batch", input_data=b"\n".join(oid for _, oid in objects) + b"\n"
    ))
    result: dict[str, bytes] = {}
    for name, object_id in objects:
        header = stream.readline().split()
        if len(header) != 3 or header[:2] != [object_id, b"blob"]:
            raise ValueError("cannot read exact initiative blob from Git")
        size = int(header[2])
        content = stream.read(size)
        if len(content) != size or stream.read(1) != b"\n":
            raise ValueError("incomplete initiative blob in Git response")
        result[name] = content
    return result


def coherence_text(content: bytes) -> str:
    return content.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")


def coherence_history(text: str) -> list[list[str]]:
    history = LIFECYCLE_SECTION.search(text)
    if not history:
        return []
    return [
        [plain_cell(cell) for cell in split_markdown_row(line)]
        for line in history.group(1).splitlines()
        if line.lstrip().startswith("|")
        and len(split_markdown_row(line)) >= 4
        and plain_cell(split_markdown_row(line)[2]) in ALLOWED_STATUSES
    ]


def coherence_content(path: Path, git_root: Path, snapshot: dict[str, bytes] | None) -> bytes | None:
    if snapshot is not None:
        return snapshot.get(relative(path, git_root))
    return path.read_bytes() if path.is_file() else None


def coherence_reopened(
    prior_text: str, current_text: str, readme: Path,
    previous_files: dict[str, bytes], git_root: Path,
    current_files: dict[str, bytes] | None = None,
) -> bool:
    """A new, appended reopening needs a new receipt, never an old approval."""
    before = coherence_history(prior_text)
    after = coherence_history(current_text)
    if not before or after[:len(before)] != before or len(after) <= len(before):
        return False
    row = after[len(before)]
    if row[1] not in TERMINAL_STATUSES or row[2] not in ACTIVE_STATUSES:
        return False
    if row[2] not in {"Proposed", "Accepted"}:
        return False
    # Inspect only the transition's authority cell, not unrelated README links.
    history = LIFECYCLE_SECTION.search(current_text)
    assert history is not None
    raw_rows = [
        split_markdown_row(line)
        for line in history.group(1).splitlines()
        if line.lstrip().startswith("|")
        and len(split_markdown_row(line)) >= 4
        and plain_cell(split_markdown_row(line)[2]) in ALLOWED_STATUSES
    ]
    authority_cell = raw_rows[len(before)][3]
    for target in MARKDOWN_LINK.findall(authority_cell):
        if target.startswith(("http:", "https:", "mailto:")):
            continue
        receipt = (readme.parent / unquote(target.split("#", 1)[0])).resolve()
        if receipt.parent != (readme.parent / "decision-receipts").resolve():
            continue
        if not resolves_within(receipt, git_root):
            continue
        if relative(receipt, git_root) in previous_files:
            continue
        content = coherence_content(receipt, git_root, current_files)
        if content is None:
            continue
        text = coherence_text(content)
        if metadata_plain(text, "Disposition") != "Reopened":
            continue
        if not metadata_value(text, "Human authority"):
            continue
        if row[2] == "Accepted" and metadata_plain(text, "Unchanged accepted claim") != "Yes":
            continue
        return True
    return False


def coherence_append_only(before: bytes, after: bytes, *, readme: bool) -> bool:
    try:
        old, new = coherence_text(before), coherence_text(after)
    except UnicodeError:
        return before == after
    if readme:
        # A date is navigation metadata, not permission to alter a closed claim.
        date = re.compile(r"(?im)^\*\*Last updated:\*\*[^\n]*\n?")
        old, new = date.sub("", old), date.sub("", new)
    old = old.rstrip()
    if new.rstrip() == old:
        return True
    if not new.startswith(old):
        return False
    suffix = new[len(old):].lstrip()
    allowed = ("Historical correction", "Successor references", "Administrative addendum") if readme else ("Historical correction",)
    return any(suffix.startswith(f"## {heading}\n") for heading in allowed)


def validate_terminal_changes(
    root: Path, git_root: Path, previous: dict[str, bytes],
    current_files: dict[str, bytes] | None = None,
) -> list[Finding]:
    findings: list[Finding] = []
    owners = {
        name.rsplit("/", 1)[0] + "/"
        for name, content in previous.items()
        if name.endswith("/README.md") and TYPE_LINE.search(content.decode("utf-8", errors="replace"))
    }
    if current_files is not None:
        owners.update(
            name.rsplit("/", 1)[0] + "/"
            for name, content in current_files.items()
            if name.endswith("/README.md") and TYPE_LINE.search(content.decode("utf-8", errors="replace"))
        )
    elif (root / "initiatives").is_dir():
        owners.update(
            relative(path.parent, git_root).rstrip("/") + "/"
            for path in (root / "initiatives").rglob("README.md")
            if TYPE_LINE.search(path.read_text(encoding="utf-8"))
        )
    for name, content in previous.items():
        if not name.endswith("/README.md"):
            continue
        try:
            prior_text = coherence_text(content)
        except UnicodeError:
            continue
        if not TYPE_LINE.search(prior_text) or metadata_plain(prior_text, "Status") not in TERMINAL_STATUSES:
            continue
        readme = git_root / name
        prefix = name.rsplit("/", 1)[0] + "/"
        children = [owner for owner in owners if owner != prefix and owner.startswith(prefix)]
        current_readme = coherence_content(readme, git_root, current_files)
        current_text = coherence_text(current_readme) if current_readme is not None else ""
        reopened = coherence_reopened(prior_text, current_text, readme, previous, git_root, current_files)
        for old_name, old_content in previous.items():
            if not old_name.startswith(prefix) or any(old_name.startswith(child) for child in children):
                continue
            path = git_root / old_name
            content = coherence_content(path, git_root, current_files)
            if content is not None and (
                reopened or coherence_append_only(old_content, content, readme=path == readme)
            ):
                continue
            findings.append(Finding(
                "error", "TADP043", relative(path, root),
                "closed initiative record changed or was removed without a new evidenced reopening; preserve the prior claim and use a successor for substantive work",
            ))
        if not reopened:
            candidates = (
                [git_root / path for path in current_files if path.startswith(prefix)]
                if current_files is not None else list(readme.parent.rglob("*"))
            )
            for path in candidates:
                if coherence_content(path, git_root, current_files) is None or relative(path, git_root) in previous:
                    continue
                if any(relative(path, git_root).startswith(child) for child in children):
                    continue
                if path.parent == readme.parent / "decision-receipts" and path.suffix == ".md":
                    continue
                findings.append(Finding(
                    "error", "TADP043", relative(path, root),
                    "new closed-initiative content requires a new evidenced reopening; record feedback in the source initiative instead",
                ))
    return findings


def coherence_table(text: str, headers: tuple[str, ...]) -> list[dict[str, str]] | None:
    table = find_markdown_table(text, headers)
    if table is None:
        return None
    # The generic parser skips malformed-width rows; coherence records must not.
    lines = text.splitlines()
    for index, line in enumerate(lines[:-1]):
        if line.lstrip().startswith("|") and is_markdown_separator(lines[index + 1]):
            actual = split_markdown_row(line)
            if not set(headers).issubset(actual):
                continue
            for row in lines[index + 2:]:
                if not row.lstrip().startswith("|"):
                    break
                if len(split_markdown_row(row)) != len(actual):
                    return None
            break
    return table[1]


def validate_work_conflicts(root: Path) -> list[Finding]:
    path = root / "initiatives" / "work-conflicts.md"
    if not path.is_file():
        return [Finding("error", "TADP041", relative(path, root), "coherence adoption requires a project work-conflict register")]
    text = HTML_COMMENT.sub("", mask_fenced_code(path.read_text(encoding="utf-8")))
    rows = coherence_table(text, WORK_CONFLICT_HEADERS)
    if rows is None or (not rows and "no work conflicts recorded" not in text.lower()):
        return [Finding("error", "TADP044", relative(path, root), "work-conflict register needs the declared table or an explicit empty register")]
    findings: list[Finding] = []
    seen: set[str] = set()
    for row in rows:
        conflict_id = plain_cell(row["ID"])
        invalid = (
            not re.fullmatch(r"WORK-CONFLICT-[0-9]{3,}", conflict_id)
            or conflict_id in seen
            or any(not plain_cell(row[field]) or plain_cell(row[field]) == "-" for field in WORK_CONFLICT_HEADERS)
            or plain_cell(row["Status"]) not in {"Open", "Resolved"}
            or any(markdown_link(row[field]) is None for field in ("Source work", "Conflicting work"))
            or (plain_cell(row["Status"]) == "Resolved" and markdown_link(row["Disposition and evidence"]) is None)
        )
        if invalid:
            findings.append(Finding(
                "error", "TADP044", relative(path, root),
                f"{conflict_id or 'conflict row'} must preserve unique identity, both linked work claims, effort/impact, owner, status, and evidenced disposition",
            ))
        seen.add(conflict_id)
    return findings


def validate_completion_coherence(
    root: Path, git_root: Path, adoption: dict[str, bytes], comparison: dict[str, bytes],
) -> list[Finding]:
    findings: list[Finding] = []
    readmes = {
        path for path in (root / "initiatives").rglob("README.md")
        if TYPE_LINE.search(path.read_text(encoding="utf-8"))
    } if (root / "initiatives").is_dir() else set()
    states = {path.resolve(): metadata_plain(path.read_text(encoding="utf-8"), "Status") for path in readmes}
    register = (root / "initiatives" / "work-conflicts.md").resolve()
    register_text = HTML_COMMENT.sub("", mask_fenced_code(register.read_text(encoding="utf-8"))) if register.is_file() else ""
    register_rows = coherence_table(register_text, WORK_CONFLICT_HEADERS) or []
    registered_ids = {plain_cell(row["ID"]).lower() for row in register_rows}
    registered_anchors = {
        match.lower() for match in re.findall(r"(?im)^#{1,6}[ \t]+(WORK-CONFLICT-[0-9]{3,})[ \t]*$", register_text)
    }
    for readme in sorted(readmes):
        current_text = readme.read_text(encoding="utf-8")
        if metadata_plain(current_text, "Status") != "Completed":
            continue
        name = relative(readme, git_root)
        prior = coherence_text(adoption.get(name, b""))
        # Retain truthful historical completion; a new cycle is a new claim.
        if metadata_plain(prior, "Status") == "Completed" and not coherence_reopened(prior, current_text, readme, adoption, git_root):
            continue
        evidence = readme.parent / "completion-evidence.md"
        if not evidence.is_file():
            continue  # The existing completion-record rule reports this.
        text = HTML_COMMENT.sub("", mask_fenced_code(evidence.read_text(encoding="utf-8")))
        section = re.search(r"(?ims)^## Cross-initiative coherence review\s*\n(.*?)(?=^##\s|\Z)", text)
        body = section.group(1) if section else ""
        rows = coherence_table(body, COHERENCE_REVIEW_HEADERS)
        problems: list[str] = []
        if not metadata_value(body, "Inventory baseline"):
            problems.append("inventory baseline")
        register_field = metadata_value(body, "Work-conflict register") or ""
        if resolve_markdown_link(register_field, evidence) != register:
            problems.append("linked project work-conflict register")
        if rows is None:
            problems.append("coherence review table")
            rows = []
        seen: set[Path] = set()
        previous_evidence = comparison.get(relative(evidence, git_root))
        changed = previous_evidence is None or coherence_text(previous_evidence) != coherence_text(evidence.read_bytes())
        before_status = metadata_plain(coherence_text(comparison.get(name, b"")), "Status")
        check_inventory = changed or before_status != "Completed"
        for row in rows:
            target = resolve_markdown_link(row["Target initiative"], evidence)
            if target is not None:
                target = initiative_record_path(target).resolve()
            state = plain_cell(row["Lifecycle state"])
            if target is None or target == readme.resolve() or not resolves_within(target, root / "initiatives") or not target.is_file() or target in seen:
                problems.append("unique linked target initiative")
            elif check_inventory and (target not in states or states[target] != state):
                problems.append(f"current lifecycle state for {relative(target, root)}")
            if target is not None:
                seen.add(target)
            if state not in ALLOWED_STATUSES or any(not plain_cell(row[field]) or plain_cell(row[field]) == "-" for field in COHERENCE_REVIEW_HEADERS):
                problems.append("complete review row")
            if any(markdown_link(row[field]) is None for field in ("Work and effort evidence", "Record links")):
                problems.append("linked work/effort evidence and disposition records")
            if re.match(r"(?i)^Conflict[ \t]*:", plain_cell(row["Finding"])):
                linked_conflict = False
                for link in MARKDOWN_LINK.findall(row["Record links"]):
                    target_file = resolve_markdown_link(f"[record]({link})", evidence)
                    anchor = unquote(link.partition("#")[2]).lower()
                    if target_file == register and anchor in registered_ids and anchor in registered_anchors:
                        linked_conflict = True
                if not linked_conflict:
                    problems.append("linked existing work-conflict entry for a conflict finding")
        if check_inventory:
            expected = {path for path, state in states.items() if state in ACTIVE_STATUSES and path != readme.resolve()}
            missing = expected - seen
            if missing:
                problems.append("active initiative coverage (including Proposed): " + ", ".join(relative(path, root) for path in sorted(missing)))
            if not rows and not expected and "no other active initiatives" not in body.lower():
                problems.append("explicit no other active initiatives finding")
        if problems:
            findings.append(Finding(
                "error", "TADP042", relative(evidence, root),
                "completion coherence review is missing or incomplete: " + "; ".join(dict.fromkeys(problems)),
            ))
    return findings


def validate_coherence(root: Path, base_ref: str = "HEAD") -> list[Finding]:
    profile = root / "project-profile.md"
    declaration = re.compile(r"(?im)^\*\*Coherence revision baseline:\*\*[ \t]*([^\r\n]*)")

    def declared_baseline(text: str) -> str | None:
        match = declaration.search(text)
        return plain_cell(match.group(1)) if match else None

    baseline = declared_baseline(profile.read_text(encoding="utf-8")) if profile.is_file() else None
    active = baseline is not None and not baseline.lower().startswith("not yet adopted")
    findings: list[Finding] = []
    previously_active = False
    try:
        git_root = Path(coherence_git(root, "rev-parse", "--show-toplevel").decode("utf-8").strip()).resolve()
        head = coherence_commit(root, "HEAD")
        profile_name = relative(profile, git_root)
        history = coherence_git(root, "log", "--format=%H", head, "--", profile_name).decode("ascii").splitlines()
        previous_baselines: set[str] = set()
        # The selected CI base may predate adoption. Inspect HEAD history too,
        # so deleting the declaration cannot disable a previously adopted rule.
        for revision in dict.fromkeys((head, *history)):
            try:
                prior_profile = coherence_text(coherence_git(root, "show", f"{revision}:{profile_name}"))
            except ValueError:
                continue  # A first adoption may create the project profile.
            previous = declared_baseline(prior_profile)
            if previous is not None and not previous.lower().startswith("not yet adopted"):
                previous_baselines.add(previous)
        previously_active = bool(previous_baselines)
        comparison_commit = coherence_commit(root, base_ref)
        if previously_active and not active:
            raise ValueError("adopted coherence baseline must not be removed or disabled")
        if not active:
            return []
        assert baseline is not None
        findings.extend(validate_work_conflicts(root))
        for required in (
            "evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md",
            "template/project/initiatives/work-conflicts.template.md",
        ):
            if not (root / required).is_file():
                findings.append(Finding("error", "TADP041", required, "adopted coherence source is missing"))
        if not COMMIT_ID.fullmatch(baseline):
            raise ValueError("Coherence revision baseline must name the captured pre-revision Git commit")
        adoption_commit = coherence_commit(root, baseline)
        for previous in previous_baselines:
            if not COMMIT_ID.fullmatch(previous) or coherence_commit(root, previous) != adoption_commit:
                raise ValueError("captured coherence baseline must not be changed after adoption")
        coherence_git(root, "merge-base", "--is-ancestor", adoption_commit, head)
        coherence_git(root, "merge-base", "--is-ancestor", comparison_commit, head)
        common = coherence_git(root, "merge-base", adoption_commit, comparison_commit).decode("ascii").strip()
        if common == comparison_commit:
            # Rules apply prospectively; never reinterpret pre-adoption edits.
            comparison_commit = adoption_commit
        elif common != adoption_commit:
            raise ValueError("comparison and adoption baselines must be on the same ancestry")
        prefix = relative(root / "initiatives", git_root).rstrip("/") + "/"
        adoption = coherence_snapshot(root, adoption_commit, prefix)
        comparison = adoption if comparison_commit == adoption_commit else coherence_snapshot(root, comparison_commit, prefix)
        # In CI a range may contain both completion and a later closed edit.
        # Check each parent-to-commit snapshot, not just the range's endpoints.
        if comparison_commit != head:
            coherence_git(root, "merge-base", "--is-ancestor", comparison_commit, head)
            snapshots = {adoption_commit: adoption, comparison_commit: comparison}
            revisions = coherence_git(
                root, "rev-list", "--reverse", "--ancestry-path", f"{comparison_commit}..{head}"
            ).decode("ascii").splitlines()
            for revision in revisions:
                parents = coherence_git(root, "rev-list", "--parents", "-n", "1", revision).decode("ascii").split()[1:]
                if revision not in snapshots:
                    snapshots[revision] = coherence_snapshot(root, revision, prefix)
                for parent in parents:
                    if parent not in snapshots:
                        snapshots[parent] = coherence_snapshot(root, parent, prefix)
                    for finding in validate_terminal_changes(root, git_root, snapshots[parent], snapshots[revision]):
                        findings.append(Finding(
                            finding.severity, finding.code, finding.path,
                            f"commit {revision}: {finding.message}",
                        ))
    except (OSError, ValueError, UnicodeError) as error:
        # Unadopted legacy scaffolds do not require Git objects for this rule.
        # A declared or previously observed adoption always fails closed.
        if not active and not previously_active:
            return []
        findings.append(Finding(
            "error", "TADP041", relative(profile, root),
            f"cannot verify coherence Git baseline or comparison revision: {error}",
        ))
        return findings
    findings.extend(validate_terminal_changes(root, git_root, comparison))
    findings.extend(validate_completion_coherence(root, git_root, adoption, comparison))
    return findings


def validate_prompts(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    prompt_root = root / "template" / "prompts"
    for number in range(14):
        matches = sorted(prompt_root.glob(f"{number:02d}_*.md"))
        if len(matches) != 1:
            findings.append(
                Finding(
                    "error",
                    "TADP015",
                    relative(prompt_root, root),
                    f"expected exactly one numbered prompt for stage {number}",
                )
            )
            continue
        path = matches[0]
        text = path.read_text(encoding="utf-8")
        requirements = {
            "## Example usage": "Example usage section",
            "WORKFLOW-CONTRACT.md": "shared workflow contract reference",
            "attached initiative": "attached-initiative example language",
            "{initiative}": "{initiative} executable placeholder",
        }
        for marker, description in requirements.items():
            if marker not in text:
                findings.append(
                    Finding(
                        "error",
                        "TADP016",
                        relative(path, root),
                        f"prompt is missing {description}",
                    )
                )
    return findings


def validate_keyword_contract(root: Path) -> list[Finding]:
    """Check adopted registry and entry points without interpreting stored prompts.

    Earlier projects without specification 11 retain their governing revision.
    Protected-source validation independently detects removal or drift of an
    adopted specification; keyword requests never bypass that check.
    """
    specification = root / KEYWORD_SPECIFICATION
    if not specification.is_file():
        return []
    findings: list[Finding] = []
    try:
        load_registry(root)
    except (OSError, ValueError, TypeError, AttributeError) as error:
        findings.append(Finding("error", "TADP046", KEYWORD_SPECIFICATION,
                                f"invalid canonical keyword registry: {error}"))
    name = specification.name
    references = {
        "AGENTS.md": f"evidence/authoritative/LLM/{name}",
        "template/project/AGENTS.md": f"evidence/authoritative/LLM/{name}",
        "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md": name,
    }
    for path, target in references.items():
        source = root / path
        text = source.read_text(encoding="utf-8") if source.is_file() else ""
        if target not in MARKDOWN_LINK.findall(text):
            findings.append(Finding("error", "TADP047", path,
                                    "missing direct relative canonical keyword specification reference"))
    return findings


def validate(root: Path, *, base_ref: str = "HEAD") -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    findings.extend(validate_required_paths(root))
    findings.extend(validate_protected_sources(root))
    findings.extend(validate_project_prompt_scaffold(root))
    findings.extend(validate_links(root))
    findings.extend(validate_tokens(root))
    findings.extend(validate_initiatives(root))
    findings.extend(validate_version_correlation(root))
    findings.extend(validate_coherence(root, base_ref))
    findings.extend(validate_prompts(root))
    findings.extend(validate_keyword_contract(root))
    return sorted(findings, key=lambda item: (item.severity, item.code, item.path))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="TADp repository root")
    parser.add_argument("--json", action="store_true", help="emit a JSON report")
    parser.add_argument(
        "--base-ref", default="HEAD",
        help="Git comparison revision for closed-initiative changes (use the integration base in CI)",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: repository root does not exist: {root}", file=sys.stderr)
        return 2

    findings = validate(root, base_ref=args.base_ref)
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)

    if args.json:
        print(
            json.dumps(
                {
                    "root": str(root),
                    "valid": errors == 0,
                    "errors": errors,
                    "warnings": warnings,
                    "findings": [asdict(item) for item in findings],
                },
                indent=2,
            )
        )
    else:
        for item in findings:
            print(f"{item.severity.upper()} {item.code} {item.path}: {item.message}")
        print(f"TADp validation: {errors} error(s), {warnings} warning(s)")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

