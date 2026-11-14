#!/usr/bin/env python3
"""Preview or reset the TADp project immediately above this script's tools folder.

Uses the installed, locked template/project scaffold. No network access, Git
history changes, lock refresh, adoption, or lifecycle transitions are performed.
"""

from __future__ import annotations

import argparse
import json
import os
import stat
import sys
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath

# A preview must not populate the project's tools/__pycache__ directory.
sys.dont_write_bytecode = True

from tadp_sync import (  # noqa: E402
    Asset, PROTECTED, SyncError, digest, git, linked, safe_name, safe_target,
    validate_names, verify_lock,
)

SELF = "tools/tadp_reset.py"


@dataclass(frozen=True)
class Node:
    kind: str
    mode: int
    size: int = 0
    mtime: int = 0
    inode: int = 0
    sha256: str = ""


def checked_path(path: Path) -> Path:
    """Resolve only after refusing linked ancestors, including Windows junctions."""
    path = Path(os.path.abspath(path.expanduser()))
    for component in (*reversed(path.parents), path):
        if os.path.lexists(component) and linked(component):
            raise SyncError(f"symlink or junction in path: {component}")
    return path.resolve()


def inside(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def preserved(name: str) -> bool:
    return name == SELF or any(name == p or name.startswith(p + "/") for p in PROTECTED)


def inventory(root: Path) -> dict[str, Node]:
    """Inspect every project entry except root Git metadata, without following links."""
    result: dict[str, Node] = {}

    def visit(directory: Path) -> None:
        children = sorted(directory.iterdir(), key=lambda p: p.name)
        names: set[str] = set()
        for path in children:
            name = path.relative_to(root).as_posix()
            if path.name.casefold() in names:
                raise SyncError(f"case-colliding path: {name}")
            names.add(path.name.casefold())
            if path.name.casefold() == ".git":
                if directory == root and path.name == ".git":
                    continue  # Includes a linked-worktree .git file; never traverse it.
                raise SyncError(f"nested Git repository or aliased Git metadata: {name}")
            safe_name(name)
            info = path.lstat()
            if linked(path):
                raise SyncError(f"symlink or junction in project: {name}")
            mode = stat.S_IMODE(info.st_mode)
            if stat.S_ISDIR(info.st_mode):
                result[name] = Node("directory", mode, inode=info.st_ino)
                visit(path)
            elif stat.S_ISREG(info.st_mode) and info.st_nlink == 1:
                result[name] = Node("file", mode, info.st_size, info.st_mtime_ns,
                                    info.st_ino, digest(path.read_bytes()))
            else:
                raise SyncError(f"not an independent regular file/directory: {name}")

    visit(root)
    return result


def git_context(root: Path) -> dict[str, str]:
    top = Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    if not inside(root, top):
        raise SyncError("TADp project must be inside its Git worktree")
    metadata = Path(git(root, "rev-parse", "--absolute-git-dir").decode().strip()).resolve()
    common = Path(git(root, "rev-parse", "--path-format=absolute", "--git-common-dir").decode().strip()).resolve()
    for path in (metadata, common):
        if inside(path, root) and not inside(path, root / ".git"):
            raise SyncError("Git metadata inside the project must be under its retained .git directory")
    return dict(worktree=str(top), metadata=str(metadata), common=str(common))


def make_plan(root: Path) -> dict:
    root = checked_path(root)
    if not root.is_dir():
        raise SyncError(f"project directory does not exist: {root}")
    context = git_context(root)
    tree = inventory(root)
    if ".tadp-sync.lock" in tree:
        raise SyncError("a .tadp-sync.lock exists; inspect the sync run before resetting")
    assets: dict[str, Asset] = {}
    for prefix in PROTECTED:
        locked = {name: Asset((root / name).read_bytes()) for name, node in tree.items()
                  if node.kind == "file" and name.startswith(prefix + "/")}
        verify_lock(locked, prefix)
    for required in ("template/project/README.md", "template/project/AGENTS.md"):
        if required not in tree or tree[required].kind != "file":
            raise SyncError(f"installed project scaffold is missing: {required}")
    for name, node in tree.items():
        if node.kind != "file" or not name.startswith("template/project/"):
            continue
        target = name[len("template/project/"):]
        # Retain the complete outer library and installed invariant revision.
        # The embedded template/README.md is only a nonrecursive placeholder.
        if preserved(target):
            continue
        assets[target] = Asset((root / name).read_bytes(), node.mode)
    retained = {name for name, node in tree.items() if node.kind == "file" and preserved(name)}
    # Check the final namespace, including retained sources, before any deletion.
    validate_names([*assets, *retained])
    for name, asset in assets.items():
        if digest(asset.content) != tree["template/project/" + name].sha256:
            raise SyncError("scaffold changed during inspection; retry the preview")
    actions = []
    for name in sorted(set(assets) | {n for n, node in tree.items() if node.kind == "file"}):
        node, asset = tree.get(name), assets.get(name)
        if preserved(name):
            action = "preserve"
        elif asset is None:
            action = "delete"
        elif node is None or node.kind == "directory":
            action = "create"
        elif node.sha256 == digest(asset.content) and node.mode == asset.mode:
            action = "unchanged"
        else:
            action = "replace"
        actions.append(dict(path=name, action=action))
    needed = {p.as_posix() for name in assets for p in PurePosixPath(name).parents
              if p.as_posix() != "."}
    # Retain the source trees and the reset command's parent directories.
    for name, node in tree.items():
        if preserved(name):
            if node.kind == "directory":
                needed.add(name)
            needed.update(p.as_posix() for p in PurePosixPath(name).parents if p.as_posix() != ".")
    for name, node in sorted(tree.items()):
        if node.kind == "directory" and name not in needed:
            actions.append(dict(path=name, action="delete-directory"))
    if inventory(root) != tree:
        raise SyncError("project changed during inspection; retry the preview")
    return dict(root=str(root), git=context, actions=actions,
                _tree=tree, _assets=assets, _directories=needed)


def check_unchanged(root: Path, plan: dict) -> None:
    if str(root) != plan["root"] or git_context(root) != plan["git"] or inventory(root) != plan["_tree"]:
        raise SyncError("project changed since planning; no further reset writes permitted")


def check_backup(root: Path, plan: dict, backup: Path) -> Path:
    backup = checked_path(backup)
    for forbidden in (root, *(Path(p) for p in plan["git"].values())):
        if inside(backup, forbidden) or inside(forbidden, backup):
            raise SyncError("backup must be outside the entire Git worktree and Git metadata")
    if os.path.lexists(backup):
        raise SyncError("backup destination must be a new directory")
    if not backup.parent.is_dir():
        raise SyncError("backup parent directory must already exist")
    return backup


def write_backup(root: Path, plan: dict, backup: Path) -> None:
    backup.mkdir()
    for name, node in plan["_tree"].items():
        if preserved(name):
            continue
        destination = backup / "files" / name
        if node.kind == "directory":
            destination.mkdir(parents=True, exist_ok=True)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            data = safe_target(root, name).read_bytes()
            if digest(data) != node.sha256:
                raise SyncError(f"project changed while backing up: {name}")
            with destination.open("xb") as stream:
                stream.write(data)
            if digest(destination.read_bytes()) != node.sha256:
                raise SyncError(f"backup verification failed: {name}")
    manifest = dict(root=str(root), git=plan["git"], actions=plan["actions"],
                    entries={name: asdict(node) for name, node in plan["_tree"].items()},
                    authority="Explicit reset invocation with matching --confirm project path",
                    disposition="backup complete; inspect target after any interrupted reset")
    (backup / "reset-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def check_file(root: Path, name: str, expected: Node) -> Path:
    path = safe_target(root, name)
    info = path.lstat()
    actual = Node("file", stat.S_IMODE(info.st_mode), info.st_size, info.st_mtime_ns,
                  info.st_ino, digest(path.read_bytes()))
    if info.st_nlink != 1 or actual != expected:
        raise SyncError(f"project file changed before removal/replacement: {name}")
    return path


def apply_plan(root: Path, plan: dict, backup: Path, confirmation: str) -> Path:
    root = checked_path(root)
    if confirmation != str(root):
        raise SyncError("--confirm must exactly match the absolute project path printed by preview")
    check_unchanged(root, plan)
    backup = check_backup(root, plan, backup)
    for executable in (Path(sys.executable).resolve(), Path(sys.prefix).resolve()):
        if inside(executable, root) and not any(inside(executable, root / p) for p in PROTECTED):
            raise SyncError("use a Python interpreter outside the target project; reset removes local environments")
    lock = Path(plan["git"]["metadata"]) / "tadp-reset.lock"
    # Serialize resets even when several TADp projects share a repository.
    with lock.open("x", encoding="utf-8") as stream:
        stream.write(str(root) + "\n")
    try:
        check_unchanged(root, plan)
        write_backup(root, plan, backup)
        check_unchanged(root, plan)
        tree, assets = plan["_tree"], plan["_assets"]
        for item in plan["actions"]:
            if item["action"] in ("delete", "replace"):
                check_file(root, item["path"], tree[item["path"]]).unlink()
        for name, node in sorted(tree.items(), key=lambda pair: (-pair[0].count("/"), pair[0])):
            if node.kind == "directory" and name not in plan["_directories"]:
                path = safe_target(root, name)
                info = path.lstat()
                if (not stat.S_ISDIR(info.st_mode) or stat.S_IMODE(info.st_mode) != node.mode
                        or info.st_ino != node.inode):
                    raise SyncError(f"project directory changed before removal: {name}")
                path.rmdir()  # Fails on unexpected new content; never recursive.
        for name in sorted(plan["_directories"], key=lambda n: (n.count("/"), n)):
            safe_target(root, name).mkdir(exist_ok=True)
        for item in plan["actions"]:
            if item["action"] not in ("create", "replace"):
                continue
            name = item["path"]
            path = safe_target(root, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation refuses a newly appeared file, rather than overwriting it.
            with path.open("xb") as stream:
                stream.write(assets[name].content)
            path.chmod(assets[name].mode)
        final = inventory(root)
        if {name for name, node in final.items() if node.kind == "directory"} != plan["_directories"]:
            raise SyncError("post-reset directory inventory differs from the reviewed plan")
        expected_files = {name for name, node in tree.items() if node.kind == "file" and preserved(name)} | set(assets)
        if {name for name, node in final.items() if node.kind == "file"} != expected_files:
            raise SyncError("post-reset file inventory differs from the reviewed plan")
        for name, asset in assets.items():
            if final[name].sha256 != digest(asset.content) or final[name].mode != asset.mode:
                raise SyncError(f"post-reset verification failed: {name}")
        for name, node in tree.items():
            if preserved(name) and final.get(name) != node:
                raise SyncError(f"protected/preserved entry changed during reset: {name}")
    except (OSError, ValueError) as error:
        raise SyncError(f"reset stopped; target may be partially changed; retain backup {backup}: {error}") from error
    finally:
        lock.unlink()
    return backup


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="remove user work and restore the scaffold")
    parser.add_argument("--confirm", help="exact absolute TADp project path printed by preview")
    parser.add_argument("--backup", type=Path, help="new backup directory outside the enclosing Git worktree")
    parser.add_argument("--json", action="store_true", help="emit the plan as JSON")
    args = parser.parse_args(argv)
    if args.apply and (not args.confirm or args.backup is None):
        parser.error("--apply requires --confirm and --backup")
    if not args.apply and (args.confirm is not None or args.backup is not None):
        parser.error("--confirm and --backup are only used with --apply")
    try:
        root = checked_path(Path(__file__).absolute().parent.parent)
        if Path(__file__).parent.name != "tools":
            raise SyncError("install this script in the TADp project's tools directory")
        plan = make_plan(root)
        result = {key: value for key, value in plan.items() if not key.startswith("_")}
        result.update(mode="apply" if args.apply else "preview", applied=False)
        if args.apply:
            backup = apply_plan(root, plan, args.backup, args.confirm)
            result.update(applied=True, backup=str(backup))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"TADp {result['mode']}: {root}")
            for item in plan["actions"]:
                if item["action"] not in ("preserve", "unchanged"):
                    print(f"{item['action']:17} {item['path']}")
            print("Preserved: Git history/index/configuration, template/, invariant suite, reset script.")
            if args.apply:
                print(f"Reset verified. Original project files: {backup / 'files'}")
            else:
                print("Preview only. Apply requires --apply --confirm with this exact project path and --backup.")
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
