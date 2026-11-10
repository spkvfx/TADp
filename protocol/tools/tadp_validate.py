#!/usr/bin/env python3
"""Validate a Traceable Architecture Design Protocol repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
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

BASE_REQUIRED_PATHS = (
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
    "evidence/README.md",
    "evidence/authoritative/README.md",
    "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md",
    "evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md",
    "evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md",
    "evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md",
    "evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md",
    "evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md",
    "evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md",
    "evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md",
    "evidence/non-authoritative/README.md",
    "initiatives/README.md",
    "template/initiatives/README.md",
    "template/project/AGENTS.md",
    "template/prompts/README.md",
    "template/prompts/WORKFLOW-CONTRACT.md",
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


def validate_required_paths(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    git_entry = root / ".git"
    valid_git_entry = False
    if git_entry.is_dir():
        valid_git_entry = (git_entry / "HEAD").is_file() and (git_entry / "config").is_file()
    elif git_entry.is_file():
        valid_git_entry = git_entry.read_text(encoding="utf-8", errors="replace").lstrip().startswith(
            "gitdir:"
        )
    if not valid_git_entry:
        findings.append(
            Finding("error", "TADP012", ".git", "TADp project has no valid Git metadata entry")
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

            if status and status.group(1).strip().rstrip("  ") == "Completed":
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
            if (
                status
                and status.group(1).strip().rstrip("  ") == "In progress"
                and initiative_type
                and initiative_type.group(1).strip() == "implementation"
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
    for number in range(11):
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

