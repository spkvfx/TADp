#!/usr/bin/env python3
"""Manage and enforce TADp protected-source integrity locks."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # Importing the validator must remain read-only.

from tadp_validate import (
    PROTECTED_LOCK_NAME,
    PROTECTED_ROOTS,
    build_protected_lock,
    protected_lock_path,
    validate_protected_sources,
)


ALLOW_UPDATE_ENV = "TADP_ALLOW_PROTECTED_UPDATE"
UPDATE_AUTHORITY_ENV = "TADP_PROTECTED_UPDATE_AUTHORITY"


def write_lock(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def mutate_locks(
    root: Path,
    *,
    action: str,
    protected_roots: tuple[str, ...],
    authority: str,
) -> int:
    authority = authority.strip()
    if not authority:
        print("error: --authority must identify the explicit human instruction or decision record", file=sys.stderr)
        return 2

    locks = {name: protected_lock_path(root, name) for name in protected_roots}
    if action == "initialize":
        existing = [path for path in locks.values() if path.exists()]
        if existing:
            print(
                "error: initialize refuses to replace an existing lock: "
                + ", ".join(str(path) for path in existing),
                file=sys.stderr,
            )
            return 2
    elif action == "refresh":
        missing = [path for path in locks.values() if not path.is_file()]
        if missing:
            print(
                "error: refresh requires an existing lock: "
                + ", ".join(str(path) for path in missing),
                file=sys.stderr,
            )
            return 2

    try:
        payloads = {
            name: build_protected_lock(root, name, authority) for name in protected_roots
        }
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    for name in protected_roots:
        write_lock(locks[name], payloads[name])
        verb = "initialized" if action == "initialize" else "refreshed"
        print(f"{verb} {locks[name]}")
    return 0


def decode_nul_paths(output: bytes) -> set[str]:
    return {
        item.decode("utf-8", errors="surrogateescape").replace("\\", "/")
        for item in output.split(b"\0")
        if item
    }


def git_output(git_root: Path, *arguments: str) -> bytes:
    result = subprocess.run(
        ("git", *arguments),
        cwd=git_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(message or f"git {' '.join(arguments)} failed")
    return result.stdout


def scoped_prefix(git_root: Path, root: Path, protected_root: str) -> str:
    relative_root = root.relative_to(git_root).as_posix()
    return f"{relative_root}/{protected_root}" if relative_root != "." else protected_root


def paths_for_roots(
    paths: set[str], git_root: Path, root: Path
) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {name: [] for name in PROTECTED_ROOTS}
    for name in PROTECTED_ROOTS:
        prefix = scoped_prefix(git_root, root, name).rstrip("/") + "/"
        result[name] = sorted(path for path in paths if path.startswith(prefix))
    return result


def guard_staged(root: Path) -> int:
    protection_findings = validate_protected_sources(root)
    if protection_findings:
        for finding in protection_findings:
            print(f"ERROR {finding.code} {finding.path}: {finding.message}", file=sys.stderr)
        return 1

    try:
        git_root = Path(
            git_output(root, "rev-parse", "--show-toplevel")
            .decode("utf-8", errors="replace")
            .strip()
        ).resolve()
        root = root.resolve()
        root.relative_to(git_root)

        staged = decode_nul_paths(
            git_output(
                git_root,
                "diff",
                "--cached",
                "--name-only",
                "--no-renames",
                "-z",
                "--diff-filter=ACDMRTUXB",
            )
        )
        unstaged = decode_nul_paths(
            git_output(
                git_root,
                "diff",
                "--name-only",
                "--no-renames",
                "-z",
                "--diff-filter=ACDMRTUXB",
            )
        )
        untracked = decode_nul_paths(
            git_output(git_root, "ls-files", "--others", "--exclude-standard", "-z")
        )
    except (RuntimeError, ValueError) as error:
        print(f"error: cannot inspect Git protected-source state: {error}", file=sys.stderr)
        return 2

    staged_by_root = paths_for_roots(staged, git_root, root)
    unstaged_by_root = paths_for_roots(unstaged | untracked, git_root, root)
    dirty = sorted(path for paths in unstaged_by_root.values() for path in paths)
    if dirty:
        print("error: protected sources have unstaged or untracked changes:", file=sys.stderr)
        for path in dirty:
            print(f"  {path}", file=sys.stderr)
        print("stage or revert those paths before committing", file=sys.stderr)
        return 1

    affected = {name: paths for name, paths in staged_by_root.items() if paths}
    if not affected:
        return 0

    if os.environ.get(ALLOW_UPDATE_ENV) != "1":
        print("error: staged protected-source changes are blocked by default:", file=sys.stderr)
        for path in sorted(path for paths in affected.values() for path in paths):
            print(f"  {path}", file=sys.stderr)
        print(
            f"an explicitly authorized update must set {ALLOW_UPDATE_ENV}=1 and "
            f"{UPDATE_AUTHORITY_ENV} to the lock authority reference",
            file=sys.stderr,
        )
        return 1

    authority = os.environ.get(UPDATE_AUTHORITY_ENV, "").strip()
    if not authority:
        print(
            f"error: {UPDATE_AUTHORITY_ENV} is required for a protected update",
            file=sys.stderr,
        )
        return 1

    for name in affected:
        lock = protected_lock_path(root, name)
        try:
            payload = json.loads(lock.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            print(f"error: cannot read {lock}: {error}", file=sys.stderr)
            return 1
        if payload.get("authority") != authority:
            print(
                f"error: {UPDATE_AUTHORITY_ENV} does not match the authority in "
                f"{name}/{PROTECTED_LOCK_NAME}",
                file=sys.stderr,
            )
            return 1
    return 0


def check(root: Path) -> int:
    findings = validate_protected_sources(root)
    for finding in findings:
        print(f"{finding.severity.upper()} {finding.code} {finding.path}: {finding.message}")
    if findings:
        print(f"TADp protected-source check: {len(findings)} error(s)")
        return 1
    print("TADp protected-source check: 0 error(s)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "action", choices=("check", "initialize", "refresh", "guard-staged")
    )
    parser.add_argument("root", nargs="?", default=".", help="installed TADp project root (default: current directory)")
    parser.add_argument(
        "--protected-root",
        action="append",
        choices=PROTECTED_ROOTS,
        dest="protected_roots",
        help="root to initialize or refresh; repeat to select both",
    )
    parser.add_argument(
        "--authority",
        default="",
        help="explicit human instruction or decision-record reference for a lock change",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: repository root does not exist: {root}", file=sys.stderr)
        return 2

    if args.action == "check":
        return check(root)
    if args.action == "guard-staged":
        return guard_staged(root)

    selected = tuple(dict.fromkeys(args.protected_roots or PROTECTED_ROOTS))
    return mutate_locks(
        root,
        action=args.action,
        protected_roots=selected,
        authority=args.authority,
    )


if __name__ == "__main__":
    raise SystemExit(main())
