#!/usr/bin/env python3
"""Validate a Traceable Architecture Design Protocol repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import unquote


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
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
    "docs/guides/protected-source-integrity-migration.md",
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
    "evidence/non-authoritative/README.md",
    "initiatives/README.md",
    "template/AGENTS.md",
    "template/initiatives/README.md",
    "template/project/AGENTS.md",
    "template/project/.gitattributes",
    "template/project/.githooks/pre-commit",
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


def markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


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


def validate_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#", "{")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / unquote(target_path)).resolve()
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


def validate(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    findings.extend(validate_required_paths(root))
    findings.extend(validate_protected_sources(root))
    findings.extend(validate_links(root))
    findings.extend(validate_tokens(root))
    findings.extend(validate_initiatives(root))
    findings.extend(validate_prompts(root))
    return sorted(findings, key=lambda item: (item.severity, item.code, item.path))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="TADp repository root")
    parser.add_argument("--json", action="store_true", help="emit a JSON report")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: repository root does not exist: {root}", file=sys.stderr)
        return 2

    findings = validate(root)
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

