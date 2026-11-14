"""Qualify the exact owned-review candidate in an isolated clean installation.

This evidence helper is not a runtime product. It reads the pinned reusable
library and declared candidate, writes this evidence directory and a retained
temporary fixture, and never refreshes a live installed/distribution lock.
Document-contract tests and synthetic inputs do not prove future LLM judgments;
independent scenario walkthrough and complete-diff review remain separate.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import traceback
from datetime import datetime, timezone
from urllib.parse import unquote
import uuid


REPOSITORY = Path(__file__).resolve().parents[4]
EVIDENCE = Path(__file__).resolve().parent
CANDIDATE = REPOSITORY / "TADp/protocol"
BASELINE = "294d70d1b7b313bd46cab481b714c8cbb5c0e612"
AUTHORITY = (
    "Isolated fixture only: invoked assumption-and-open-question-review-protocol-"
    "change prompt, exact candidate revision and fixture-lock authority; "
    "TADP-001 ACCEPT-001; no live library introduction or adoption"
)
PRESERVED = (
    "protocol", "TADp/template", "TADp/evidence/authoritative",
    "TADp/prompts/AGENTS.md", "prompts", "AGENTS.md", ".gitignore",
    ".gitattributes", ".githooks",
)
TEST_PATHS = (
    "tests/test_assumption_question_review.py",
    "tests/fixtures/owned_review_scenarios.json",
)
ENVIRONMENT = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")


def canonical(data: bytes) -> bytes:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def digest(data: bytes) -> str:
    return hashlib.sha256(canonical(data)).hexdigest()


def git(*arguments: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(REPOSITORY), *arguments], capture_output=True,
        check=False, env=ENVIRONMENT,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout


def json_file(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def preservation() -> dict:
    names = git("ls-tree", "-r", "--name-only", BASELINE, "--", *PRESERVED)
    checked = names.decode("utf-8").splitlines()
    changed = []
    for name in checked:
        path = REPOSITORY / name
        original = git("show", f"{BASELINE}:{name}")
        if not path.is_file() or digest(path.read_bytes()) != digest(original):
            changed.append(name)
    untracked = git("ls-files", "--others", "--exclude-standard", "--", *PRESERVED)
    diff = git("diff", "--name-only", BASELINE, "--", *PRESERVED)
    return {
        "baseline": BASELINE, "checked_files": len(checked),
        "changed_content": changed,
        "git_diff": diff.decode("utf-8").splitlines(),
        "untracked_in_preserved_scope": untracked.decode("utf-8").splitlines(),
    }


def candidate_payload() -> tuple[dict[str, bytes], dict]:
    mapping = json.loads((EVIDENCE / "source-map.json").read_text(encoding="utf-8"))
    declared = {}
    absent = []
    rows = [*mapping["sources"], *mapping["protection_dependencies"],
            *mapping["proposed_additions"]]
    for row in rows:
        name = row.get("candidate")
        if not name:
            continue
        path = (REPOSITORY / name).resolve()
        relative = path.relative_to(CANDIDATE.resolve()).as_posix()
        if not path.is_file():
            if row.get("conditional"):
                absent.append({"candidate": name, "reason": "Conditional change not needed"})
                continue
            raise ValueError("Declared candidate is missing: " + name)
        declared[relative] = path.read_bytes()
    required = {"template/project/decisions/assumptions-and-open-questions.template.md",
                *TEST_PATHS}
    if not required.issubset(declared):
        raise ValueError("Required addition is not declared: " + str(sorted(required - declared.keys())))
    actual = {p.relative_to(CANDIDATE).as_posix()
              for folder in (CANDIDATE / "template", CANDIDATE / "tests")
              for p in folder.rglob("*") if p.is_file()
              and "__pycache__" not in p.parts}
    unknown = actual - declared.keys()
    if unknown:
        raise ValueError("Undeclared candidate files: " + str(sorted(unknown)))
    manifest = {
        name: {"sha256_utf8_lf": digest(data), "bytes": len(data)}
        for name, data in sorted(declared.items())
    }
    return declared, {"files": manifest, "conditional_absence": absent}


def extract_library(destination: Path) -> None:
    archive_bytes = git("archive", "--format=tar", f"{BASELINE}:TADp/template")
    destination.mkdir()
    with tarfile.open(fileobj=io.BytesIO(archive_bytes)) as archive:
        for member in archive.getmembers():
            relative = PurePosixPath(member.name)
            if relative.is_absolute() or ".." in relative.parts or "\\" in member.name:
                raise ValueError("Escaping archive path: " + member.name)
            if member.issym() or member.islnk():
                raise ValueError("Linked archive member: " + member.name)
            path = destination.joinpath(*relative.parts).resolve()
            path.relative_to(destination.resolve())
            if member.isdir():
                path.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                path.parent.mkdir(parents=True, exist_ok=True)
                stream = archive.extractfile(member)
                if stream is None:
                    raise ValueError("Unreadable archive member: " + member.name)
                path.write_bytes(stream.read())
            else:
                raise ValueError("Unsupported archive member: " + member.name)


def copy_entry(source: Path, destination: Path) -> None:
    if source.is_symlink():
        raise ValueError("Fixture dependency must not be a link: " + str(source))
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)


def install_clean(library: Path, project: Path, payload: dict[str, bytes]) -> list[Path]:
    # No populated P records, source distribution history or old trial support.
    for source in sorted((library / "project").iterdir()):
        if source.name != "template":
            copy_entry(source, project / source.name)
    shutil.copytree(library, project / "template")
    checked = []
    for relative, data in sorted(payload.items()):
        destination = project / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        if relative.startswith("template/project/"):
            runtime = project / relative.removeprefix("template/project/")
            runtime.parent.mkdir(parents=True, exist_ok=True)
            runtime.write_bytes(data)
            if runtime.suffix == ".md":
                checked.append(runtime)
        elif relative.startswith("template/") and destination.suffix == ".md":
            checked.append(destination)
    return checked


def heading_anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)', text))
    seen = {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text):
        heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading).lower().strip()
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        number = seen.get(slug, 0)
        seen[slug] = number + 1
        result.add(slug + (f"-{number}" if number else ""))
    return result


def changed_links(project: Path, files: list[Path]) -> dict:
    checked, dynamic, external = 0, 0, 0
    failures = []
    for path in sorted(set(files)):
        text = path.read_text(encoding="utf-8-sig")
        text = re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$", "", text)
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        text = re.sub(r"(?<!`)`(?!`)[^`\r\n]*`(?!`)", "", text)
        for reference in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            reference = reference.strip().strip("<>")
            if "{" in reference or "}" in reference:
                dynamic += 1
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", reference):
                external += 1
                continue
            target, _, fragment = reference.partition("#")
            destination = (path.parent / unquote(target)).resolve() if target else path
            checked += 1
            try:
                destination.relative_to(project.resolve())
            except ValueError:
                failures.append(f"{path.relative_to(project)}: escapes fixture: {reference}")
                continue
            if not destination.exists():
                failures.append(f"{path.relative_to(project)}: missing {reference}")
            elif fragment and destination.is_file() and destination.suffix == ".md":
                if unquote(fragment) not in heading_anchors(destination.read_text(encoding="utf-8-sig")):
                    failures.append(f"{path.relative_to(project)}: missing fragment {reference}")
    return {"checked": checked, "dynamic_placeholders_not_instantiated": dynamic,
            "external_references_not_accessed": external, "failures": failures,
            "context": "Runtime copies for project/*; outer-library prompts and coverage"}


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit("No options accepted; each invocation retains a separate attempt.")
    attempt_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    attempt = EVIDENCE / "qualification-attempts" / attempt_id
    attempt.mkdir(parents=True)
    workspace = Path(tempfile.mkdtemp(prefix="tadp-owned-review-"))
    report = {
        "attempt": attempt_id, "recorded_by": "Codex qualification evidence helper",
        "baseline": BASELINE, "baseline_library": "TADp/template",
        "baseline_tree": git("rev-parse", f"{BASELINE}:TADp/template").decode().strip(),
        "python": sys.executable, "python_version": sys.version,
        "workspace": str(workspace), "fixture": str(workspace / "installed"),
        "commands": [], "result": "in progress",
        "limitations": [
            "One representative clean installation; no live project or example dependency",
            "Document-contract tests do not authenticate authority or prove future LLM behavior",
            "Synthetic scenario inputs/expected outcomes require separate semantic walkthrough",
            "Fixture-only locks are regenerated for the complete isolated installed context",
            "No library introduction, adoption, development completion, promotion or rollout",
        ],
    }

    def save() -> None:
        json_file(attempt / "qualification.json", report)
        json_file(EVIDENCE / "qualification.json", report)

    def run(arguments: list[str], cwd: Path, label: str, expected: int = 0,
            extra_environment: dict | None = None) -> dict:
        environment = dict(ENVIRONMENT, **(extra_environment or {}))
        result = subprocess.run(arguments, cwd=cwd, capture_output=True,
                                text=True, encoding="utf-8", errors="replace", env=environment)
        log = attempt / f"{label}.log"
        log.write_text(result.stdout + result.stderr, encoding="utf-8")
        row = {"label": label, "command": arguments, "cwd": str(cwd),
               "exit": result.returncode, "expected_exit": expected,
               "log": log.relative_to(EVIDENCE).as_posix(),
               "extra_environment": extra_environment or {}}
        report["commands"].append(row)
        save()
        print(f"{label}: exit={result.returncode}; expected={expected}", flush=True)
        if result.returncode != expected:
            raise RuntimeError(f"{label} returned {result.returncode}, expected {expected}; see {log}")
        return row

    try:
        report["preservation_before"] = preservation()
        if any(report["preservation_before"][name] for name in
               ("changed_content", "git_diff", "untracked_in_preserved_scope")):
            raise ValueError("Installed/distribution preservation preflight failed")
        payload, report["candidate_manifest"] = candidate_payload()
        library = workspace / "baseline-template"
        extract_library(library)
        project = workspace / "installed"
        project.mkdir()
        run(["git", "init", "--quiet"], project, "fixture-git-init")
        hook_probe = subprocess.run(["git", "config", "--get", "core.hooksPath"],
                                    cwd=project, capture_output=True, text=True, env=ENVIRONMENT)
        report["hook_configuration"] = hook_probe.stdout.strip()
        if report["hook_configuration"]:
            raise ValueError("Fixture inherits a configured hooksPath; no hook is activated by this helper")
        (project / ".fixture-baseline").write_text("Inert isolated fixture identity only.\n", encoding="utf-8")
        run(["git", "add", ".fixture-baseline"], project, "fixture-git-add")
        run(["git", "-c", "user.name=TADp Fixture", "-c", "user.email=fixture@example.invalid",
             "commit", "--quiet", "-m", "Inert isolated fixture baseline"],
            project, "fixture-git-baseline")
        files = install_clean(library, project, payload)
        report["changed_source_links"] = changed_links(project, files)
        save()
        if report["changed_source_links"]["failures"]:
            raise ValueError("Changed source links failed before fixture lock refresh")
        protect = str(project / "tools/tadp_protect.py")
        for selected_root, protected_root, label in (
            (project / "template/project", "evidence/authoritative/LLM", "fixture-embedded-suite-lock"),
            (project, "template", "fixture-outer-library-lock"),
            (project, "evidence/authoritative/LLM", "fixture-runtime-suite-lock"),
        ):
            run([sys.executable, "-B", protect, "refresh", str(selected_root),
                 "--protected-root", protected_root, "--authority", AUTHORITY], project, label)
        report["fixture_generated_locks"] = {
            name: digest((project / name).read_bytes()) for name in (
                "template/project/evidence/authoritative/LLM/.tadp-lock.json",
                "evidence/authoritative/LLM/.tadp-lock.json", "template/.tadp-lock.json")}
        run([sys.executable, "-B", protect, "check", "."], project, "fixture-protection")
        run([sys.executable, "-B", "tools/tadp_validate.py", ".", "--json"], project, "fixture-validation")
        run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests",
             "-p", "test_assumption_question_review.py", "-v"], project, "fixture-focused-contracts",
            extra_environment={"TADP_REVIEW_ROOT": str(project)})
        tampered = project / "template/prompts/05_initiative_assumption_review.md"
        original = tampered.read_bytes()
        try:
            tampered.write_bytes(original + b"\nFixture-only integrity probe.\n")
            tamper_check = run([sys.executable, "-B", protect, "check", "."], project,
                               "fixture-deliberate-tamper-rejected", expected=1)
            tamper_log = (EVIDENCE / tamper_check["log"]).read_text(encoding="utf-8")
            if "template/prompts/05_initiative_assumption_review.md" not in tamper_log:
                raise ValueError("Tamper rejection did not identify the deliberately changed source")
        finally:
            tampered.write_bytes(original)
        run([sys.executable, "-B", protect, "check", "."], project, "fixture-restored-protection")
        current, _ = candidate_payload()
        report["candidate_drift"] = sorted(
            name for name in payload.keys() | current.keys()
            if name not in payload or name not in current
            or digest(payload[name]) != digest(current[name])
        )
        report["preservation_after"] = preservation()
        if report["candidate_drift"] or any(report["preservation_after"][name] for name in
                                           ("changed_content", "git_diff", "untracked_in_preserved_scope")):
            raise ValueError("Candidate drift or live source preservation failed")
        report["result"] = "passed structural, protection, isolated-install and document-contract checks"
        report["independent_semantic_review"] = "separate required review; not performed by this helper"
        save()
        print("qualification.json recorded; independent semantic review remains separate", flush=True)
        return 0
    except Exception as error:
        report["result"] = "failed"
        report["error"] = str(error)
        report["traceback"] = traceback.format_exc()
        save()
        print(f"Qualification failed: {error}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
