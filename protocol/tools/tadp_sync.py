#!/usr/bin/env python3
"""Sync a selected project root from the local TADp template.

Use --refresh-template to replace the local library from a pinned remote first.
Standard library only; Git is required. No upstream code is executed. Installation
does not adopt a protocol revision, migrate work, enable hooks, or commit files.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import uuid
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

DEFAULT_SOURCE = "https://github.com/spkvfx/TADp.git"
STATE = ".tadp-sync.json"
BACKUPS = ".tadp-sync-backups"
RUN_LOCK = ".tadp-sync.lock"
PROTECTED = ("template", "evidence/authoritative/LLM")
RUNTIME_TOOLS = ("tadp_validate.py", "tadp_protect.py", "tadp_keywords.py",
                 "tadp_scopes.py", "tadp_templates.py", "tadp_sync.py")
PROJECT_USE_GUIDES = frozenset((
    "README.md", "getting-started.md", "architecture-and-authority.md",
    "repository-layout.md", "initiative-workflow.md", "git-and-codex-requirements.md",
    "validation-and-quality.md", "adapting-other-tools.md",
))


class SyncError(ValueError):
    """A synchronization was refused without overriding local work."""


@dataclass(frozen=True)
class Asset:
    content: bytes
    mode: int = 0o644
    kind: str = "managed"


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def canonical_digest(content: bytes) -> str:
    if b"\0" not in content:
        try:
            content = content.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
        except UnicodeDecodeError:
            pass
    return digest(content)


def safe_name(name: str) -> str:
    if not isinstance(name, str) or not name or "\\" in name:
        raise SyncError(f"unsafe relative path: {name!r}")
    path = PurePosixPath(name)
    if path.is_absolute() or path.as_posix() != name:
        raise SyncError(f"unsafe relative path: {name!r}")
    for part in path.parts:
        if (part in (".", "..") or part.lower() == ".git" or part.endswith((".", " "))
                or re.search(r'[<>:"|?*\x00-\x1f]', part)
                or re.fullmatch(r"(?i)(con|prn|aux|nul|com[0-9]|lpt[0-9])(?:\..*)?", part)):
            raise SyncError(f"unsafe relative path: {name!r}")
    return name


def linked(path: Path) -> bool:
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & 0x400)


def safe_target(root: Path, name: str) -> Path:
    safe_name(name)
    current = root
    for part in PurePosixPath(name).parts:
        if current.exists():
            # Reject aliases on case-sensitive systems as well as Windows.
            if not current.is_dir():
                raise SyncError(f"parent is not a directory: {current}")
            if current != root:
                if os.path.lexists(current / ".git"):
                    raise SyncError(f"nested Git repository/worktree destination: {current}")
                # The reusable project source in the installed library is
                # intentionally scaffold-shaped, but is not an active project.
                if (current.relative_to(root).parts[0] != "template"
                        and (current / "AGENTS.md").is_file()
                        and (current / "prompts/AGENTS.md").is_file()
                        and (current / "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md").is_file()):
                    raise SyncError(f"another installed scaffold owns destination: {current}")
            aliases = [p.name for p in current.iterdir() if p.name.casefold() == part.casefold()]
            if len(aliases) > 1 or (aliases and part not in aliases):
                raise SyncError(f"case-colliding destination: {name}")
        current = current / part
        if os.path.lexists(current) and linked(current):
            raise SyncError(f"symlink or junction destination: {current}")
    return current


def snapshot(root: Path, name: str) -> str | None:
    path = safe_target(root, name)
    if not path.exists():
        return None
    if not path.is_file() or path.stat().st_nlink > 1:
        raise SyncError(f"destination is not an independent regular file: {name}")
    return digest(path.read_bytes())


def validate_names(names) -> None:
    seen: set[str] = set()
    spellings: dict[str, str] = {}
    for name in names:
        safe_name(name)
        folded = name.casefold()
        if folded in seen:
            raise SyncError(f"case-colliding payload/state paths: {name}")
        seen.add(folded)
        parts = PurePosixPath(name).parts
        for length in range(1, len(parts) + 1):
            prefix = "/".join(parts[:length])
            prior = spellings.setdefault(prefix.casefold(), prefix)
            if prior != prefix:
                raise SyncError(f"case-colliding path components: {prior}, {prefix}")
    for name in seen:
        if any(parent.as_posix() in seen for parent in PurePosixPath(name).parents if parent.as_posix() != "."):
            raise SyncError(f"file/directory collision: {name}")


def load_state(root: Path) -> dict | None:
    path = safe_target(root, STATE)
    if not path.exists():
        return None
    snapshot(root, STATE)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as error:
        raise SyncError(f"invalid {STATE}; preserve it and reconcile manually") from error
    if (not isinstance(value, dict) or value.get("schema_version") != 1
            or not isinstance(value.get("source"), str)
            or not isinstance(value.get("revision"), str)
            or not isinstance(value.get("files"), dict)):
        raise SyncError(f"unrecognized {STATE}; refusing to replace it")
    if "history" in value and not isinstance(value["history"], list):
        raise SyncError(f"unrecognized history in {STATE}; refusing to replace it")
    validate_names(value["files"])
    for name, entry in value["files"].items():
        if (name.casefold() in (STATE, RUN_LOCK) or name.casefold().startswith(BACKUPS + "/")
                or not isinstance(entry, dict) or entry.get("kind") not in ("managed", "seed")
                or not isinstance(entry.get("sha256"), str)
                or not re.fullmatch("[0-9a-f]{64}", entry["sha256"])):
            raise SyncError(f"invalid sync baseline: {name}")
    return value


def git(repo: Path, *args: str, data: bytes | None = None) -> bytes:
    result = subprocess.run(("git", "-c", "core.hooksPath=", *args), cwd=repo,
                            input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise SyncError(result.stderr.decode("utf-8", errors="replace").strip() or "Git failed")
    return result.stdout


def select_destination(target: str | Path | None = None) -> tuple[Path, Path]:
    """Select exactly the supplied directory or cwd, without ancestor redirection.

    Installation is deliberately limited to an existing directory. Reject path
    indirection before resolving, so a symlink cannot silently select a sibling.
    Git supplies history and identity, never a replacement installation target.
    """
    selected = Path(os.path.abspath(Path(target or Path.cwd()).expanduser()))
    for component in (*reversed(selected.parents), selected):
        if os.path.lexists(component) and linked(component):
            raise SyncError(f"symlink or junction in installation destination: {component}")
    root = selected.resolve()
    if not root.is_dir():
        raise SyncError(f"installation destination must be an existing directory: {root}")
    git_root = Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    if root != git_root and git_root not in root.parents:
        raise SyncError("installation destination must be inside its Git worktree")
    for component in (root, *root.parents):
        if (component / ".tadp-lock.json").exists() or (
                component.name == "template" and (component / "project/AGENTS.md").is_file()):
            raise SyncError(f"protected reusable source is not an installation destination: {root}")
        if component == git_root:
            break
    state = load_state(root)
    if state and "project_root" in state:
        recorded = state["project_root"]
        if not isinstance(recorded, str) or Path(recorded) != root:
            raise SyncError("recorded installation project_root contradicts selected destination; reconcile identity manually")
    if state and "git_root" in state:
        recorded = state["git_root"]
        if not isinstance(recorded, str) or Path(recorded) != git_root:
            raise SyncError("recorded installation git_root contradicts selected worktree; reconcile identity manually")
    required_files = ("AGENTS.md", "prompts/AGENTS.md", "prompts/README.md",
                      "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md")
    required_directories = ("initiatives", "products", "template", "tools")
    installed = (bool(state and "project_root" in state)
                 or (root / required_files[-1]).is_file()
                 or ((root / "prompts/AGENTS.md").is_file()
                     and (state is not None or (root / "evidence/authoritative/LLM").is_dir()
                          or (root / "template/project").is_dir())))
    if installed:
        missing = [name for name in required_files if not (root / name).is_file()]
        missing += [name for name in required_directories if not (root / name).is_dir()]
        if missing:
            raise SyncError("malformed installed scaffold; missing markers: " + ", ".join(missing))
    if target is None and not installed and root != git_root:
        for ancestor in root.parents:
            if (ancestor / "prompts/AGENTS.md").is_file() and (ancestor / required_files[-1]).is_file():
                raise SyncError("cwd is beneath an installed project; use --target to select an independent installation explicitly")
            if ancestor == git_root:
                break
    return root, git_root


def fetch_source(directory: Path, source: str, ref: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", ref) or ".." in ref:
        raise SyncError("--ref must be HEAD, a branch/tag/ref, or a commit ID")
    if not source.startswith("https://"):
        local = Path(source).expanduser()
        if not local.is_dir():
            raise SyncError("--source must be an HTTPS Git URL or a local repository directory")
        source = str(local.resolve())
    git(directory, "init", "--bare", "--quiet")
    git(directory, "-c", "protocol.file.allow=always", "fetch", "--quiet", "--depth=1",
        "--no-tags", "--", source, ref)
    return git(directory, "rev-parse", "--verify", "FETCH_HEAD^{commit}").decode().strip()


def verify_lock(assets: dict[str, Asset], prefix: str) -> None:
    lock_name = prefix + "/.tadp-lock.json"
    if lock_name not in assets:
        raise SyncError(f"upstream is missing {lock_name}")
    try:
        lock = json.loads(assets[lock_name].content)
    except (ValueError, UnicodeError) as error:
        raise SyncError(f"invalid upstream lock: {lock_name}") from error
    expected = {name[len(prefix) + 1:]: canonical_digest(asset.content)
                for name, asset in assets.items() if name.startswith(prefix + "/") and name != lock_name}
    if (not isinstance(lock, dict) or lock.get("schema_version") != 1
            or lock.get("algorithm") != "sha256-canonical-v1"
            or lock.get("protected_root") != prefix
            or not isinstance(lock.get("authority"), str) or not lock["authority"].strip()
            or lock.get("files") != expected):
        raise SyncError(f"upstream lock does not match its complete source tree: {lock_name}")


def load_assets(repo: Path, revision: str) -> dict[str, Asset]:
    """Read committed blobs, never a checkout or executable remote code.

    Only template/, the runtime invariant suite and the named runtime tools
    are selected. New project baselines may include the named project-use
    guides and decisions navigation, never development work or receipts.
    The project's template/README.md is a nonrecursive placeholder: the full
    distribution library supplies the installed template/ directory instead.
    Record sources retain their .template names and are never instantiated.
    """
    entries = []
    for item in git(repo, "ls-tree", "-r", "-z", revision).split(b"\0"):
        if not item:
            continue
        metadata, encoded_name = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        name = encoded_name.decode("utf-8")
        if (name.startswith("protocol/template/")
                or name.startswith("protocol/evidence/authoritative/LLM/")
                or name in {"protocol/tools/" + tool for tool in RUNTIME_TOOLS}):
            safe_name(name)
            if mode not in ("100644", "100755") or kind != "blob":
                raise SyncError(f"upstream links/submodules are not supported: {name}")
            entries.append((name, oid, 0o755 if mode == "100755" else 0o644))
    if not entries:
        raise SyncError("upstream has no protocol/template distribution")
    raw = git(repo, "cat-file", "--batch", data="".join(oid + "\n" for _, oid, _ in entries).encode())
    blobs = []
    offset = 0
    for _ in entries:
        end = raw.index(b"\n", offset)
        header = raw[offset:end].split()
        if len(header) != 3 or header[1] != b"blob":
            raise SyncError("unreadable upstream blob")
        size = int(header[2])
        if size > 32 * 1024 * 1024:
            raise SyncError("upstream template file exceeds 32 MiB")
        blobs.append(raw[end + 1:end + 1 + size])
        offset = end + 2 + size
    return deployment_assets({name: Asset(content, mode)
                              for (name, _, mode), content in zip(entries, blobs)})


def deployment_assets(sources: dict[str, Asset]) -> dict[str, Asset]:
    """Project a verified distribution into library, runtime and seed files."""
    assets: dict[str, Asset] = {}
    has_embedded_suite = any(name.startswith("protocol/template/project/evidence/authoritative/LLM/")
                             for name in sources)
    has_project_baseline = "protocol/template/project/template/README.md" in sources

    def add(name: str, content: bytes, mode: int, kind: str = "managed") -> None:
        asset = Asset(content, mode, kind)
        if name in assets and assets[name] != asset:
            raise SyncError(f"conflicting upstream deployment sources: {name}")
        assets[name] = asset

    for name, asset in sources.items():
        content, mode = asset.content, asset.mode
        if name.startswith("protocol/template/"):
            relative = name[len("protocol/template/"):]
            if relative.startswith("project/docs/development/") and (
                    not has_project_baseline
                    or relative[len("project/docs/development/"):] not in PROJECT_USE_GUIDES):
                raise SyncError(f"template contains excluded development documents: {name}")
            if relative.startswith("project/decisions/") and relative != "project/decisions/README.md":
                raise SyncError(f"template contains excluded development documents: {name}")
            if (relative == "project/template"
                    or relative.startswith("project/template/") and relative != "project/template/README.md"):
                raise SyncError(f"project template must contain only its nonrecursive template/README.md placeholder: {name}")
            add("template/" + relative, content, mode)
            if relative.startswith("project/"):
                target = relative[len("project/"):]
                if target == "template/README.md":
                    # Keep the placeholder inside the reusable project source,
                    # never overlay the installed complete library's README.
                    continue
                managed = target.startswith(("evidence/authoritative/LLM/", "tools/"))
                add(target, content, mode, "managed" if managed else "seed")
        elif name.startswith("protocol/evidence/"):
            if not has_embedded_suite:
                add(name[len("protocol/"):], content, mode)
        else:
            # The embedded project runtime is authoritative when present.
            # Distribution development tools must not override that template.
            target = name[len("protocol/"):]
            if "protocol/template/project/" + target not in sources:
                add(target, content, mode)
    validate_names(assets)
    for required in ("template/AGENTS.md", "AGENTS.md", "README.md",
                     "evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md",
                     "tools/tadp_validate.py", "tools/tadp_protect.py"):
        if required not in assets:
            raise SyncError(f"upstream deployment prerequisite is missing: {required}")
    for prefix in PROTECTED:
        verify_lock(assets, prefix)
    # Older published revisions need only their actual runtime dependencies.
    # Check local tadp_* imports without importing or running fetched code.
    for name, asset in assets.items():
        if name.startswith("tools/") and name.endswith(".py"):
            try:
                tree = ast.parse(asset.content, filename=name)
            except SyntaxError as error:
                raise SyncError(f"upstream tool requires unsupported/invalid Python syntax: {name}") from error
            for node in ast.walk(tree):
                modules = ([node.module] if isinstance(node, ast.ImportFrom)
                           else [alias.name for alias in node.names] if isinstance(node, ast.Import) else [])
                for module in modules:
                    if module and module.startswith("tadp_") and "tools/" + module + ".py" not in assets:
                        raise SyncError(f"upstream runtime dependency is missing: {name} imports {module}")
    return assets


def read_template(template: Path) -> dict[str, Asset]:
    """Snapshot regular local files without following links or project boundaries."""
    for component in (*reversed(template.parents), template):
        if os.path.lexists(component) and linked(component):
            raise SyncError(f"symlink or junction in local template: {component}")
    if not template.is_dir():
        raise SyncError(f"local template directory is missing: {template}; use --refresh-template to install it")
    files: dict[str, Asset] = {}

    def visit(directory: Path) -> None:
        for path in sorted(directory.iterdir()):
            name = path.relative_to(template).as_posix()
            safe_name(name)
            if linked(path):
                raise SyncError(f"symlink or junction in local template: {path}")
            if path.is_dir():
                visit(path)
            elif path.is_file() and path.stat().st_nlink == 1:
                if path.stat().st_size > 32 * 1024 * 1024:
                    raise SyncError(f"local template file exceeds 32 MiB: {path}")
                mode = 0o755 if path.stat().st_mode & stat.S_IXUSR else 0o644
                files[name] = Asset(path.read_bytes(), mode)
            else:
                raise SyncError(f"local template is not an independent regular file: {path}")

    visit(template)
    validate_names(files)
    return files


def load_local_assets(template: Path) -> dict[str, Asset]:
    """Use current local template bytes, including its embedded suite and tools.

    Incomplete historical libraries need a complete remote refresh before they
    can be the sole synchronization authority. Locks are copied, never generated.
    """
    sources = {"protocol/template/" + name: asset for name, asset in read_template(template).items()}
    return deployment_assets(sources)


def template_revision(assets: dict[str, Asset]) -> str:
    manifest = [(name, digest(asset.content), asset.mode, asset.kind)
                for name, asset in sorted(assets.items())]
    return "sha256:" + digest(json.dumps(manifest, separators=(",", ":")).encode())


def stage_template(directory: Path, assets: dict[str, Asset]) -> None:
    """Materialize only the remote library; never execute fetched tools."""
    directory.mkdir()
    validate_names(assets)
    for name, asset in assets.items():
        if name.startswith("template/"):
            path = directory.joinpath(*PurePosixPath(name[len("template/"):]).parts)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(asset.content)
            os.chmod(path, asset.mode)


def replace_template(template: Path, incoming: Path, expected: dict[str, Asset] | None,
                     authority: str) -> str | None:
    """Retain the complete previous library before installing its replacement.

    Directory renames preserve retired files in the backup, without pruning or
    refreshing any lock. An I/O failure retains staging/backup for inspection.
    """
    if expected is not None and not authority.strip():
        raise SyncError("replacing the local protected template requires --authority identifying the exact human-approved revision/change")
    template.parent.mkdir(parents=True, exist_ok=True)
    lock = safe_target(template.parent, ".tadp-template.lock")
    token = uuid.uuid4().hex.encode()
    with lock.open("xb") as stream:
        stream.write(token)
    try:
        actual = read_template(template) if os.path.lexists(template) else None
        if actual != expected:
            raise SyncError("local template changed since preview; preview again before applying")
        # Stage on the same filesystem as the destination so replacement uses
        # renames, including when the system temporary directory is elsewhere.
        staged = safe_target(template.parent, ".tadp-template-stage-" + uuid.uuid4().hex)
        stage_template(staged, load_local_assets(incoming))
        load_local_assets(staged)
        if (read_template(template) if os.path.lexists(template) else None) != expected:
            raise SyncError(f"local template changed during staging; staged library retained at {staged}")
        backup = None
        if expected is not None:
            backup_path = safe_target(template.parent, ".tadp-template-backups/" + uuid.uuid4().hex + "/template")
            backup_path.parent.mkdir(parents=True)
            template.rename(backup_path)
            backup = str(backup_path)
        try:
            staged.rename(template)
        except OSError as error:
            raise SyncError(f"could not install local template; staging retained at {staged}; previous library: {backup}") from error
        return backup
    finally:
        if snapshot(template.parent, lock.name) == digest(token):
            lock.unlink()


def make_plan(root: Path, assets: dict[str, Asset], state: dict | None, *,
              template_is_source: bool = False) -> dict:
    # An installed library used as the authority is already in place. It is
    # managed by the explicit refresh phase, never by the target sync phase.
    if template_is_source:
        assets = {name: asset for name, asset in assets.items() if not name.startswith("template/")}
    validate_names(assets)
    previous = state["files"] if state else {}
    if template_is_source:
        previous = {name: entry for name, entry in previous.items() if not name.startswith("template/")}
    actions = []
    expected = {STATE: snapshot(root, STATE)}
    for name in sorted(set(assets) | set(previous)):
        if name.casefold() in (STATE, RUN_LOCK) or name.casefold().startswith(BACKUPS + "/"):
            raise SyncError(f"reserved sync path: {name}")
        current = expected[name] = snapshot(root, name)
        asset = assets.get(name)
        baseline = previous.get(name)
        if asset is None:
            action, reason = "retain", "removed upstream; local file is never deleted or recreated"
        elif asset.kind == "seed" and current is not None:
            action, reason = "preserve", "project-owned scaffold file already exists"
        elif current == digest(asset.content):
            action, reason = "unchanged", "already matches upstream"
        elif current is None and baseline:
            action, reason = "conflict", "previously installed file was removed locally; preserving that choice"
        elif current is None:
            action, reason = "create", "missing template/runtime asset"
        elif baseline and baseline["kind"] == "managed" and current == baseline["sha256"]:
            action, reason = "update", "unchanged since the recorded installation"
        else:
            action, reason = "conflict", "user-modified or unmanaged destination; manual reconciliation required"
        actions.append(dict(path=name, action=action, reason=reason))
    # A changed lock must never hide local additions or upstream removals.
    for prefix in PROTECTED:
        if prefix == "template" and template_is_source:
            continue
        if not any(a["action"] in ("create", "update") and a["path"].startswith(prefix + "/") for a in actions):
            continue
        directory = safe_target(root, prefix)
        if directory.exists():
            for path in directory.rglob("*"):
                if linked(path):
                    raise SyncError(f"symlink or junction in protected tree: {path}")
                if path.is_file():
                    name = path.relative_to(root).as_posix()
                    expected[name] = snapshot(root, name)
                    if name not in assets:
                        actions.append(dict(path=name, action="conflict",
                                            reason="protected local/retired file would contradict upstream lock; retained"))
    conflicts = [a["path"] + ": " + a["reason"] for a in actions if a["action"] == "conflict"]
    return dict(actions=actions, conflicts=conflicts, _expected=expected,
                _template_is_source=template_is_source,
                _assets={name: (digest(a.content), a.mode, a.kind) for name, a in assets.items()})


def apply_plan(root: Path, assets: dict[str, Asset], plan: dict, *, source: str,
               revision: str, authority: str = "", git_root: Path | None = None,
               template_origin: dict | None = None) -> None:
    # Serialize cooperating sync processes. Never replace/remove someone else's
    # lock, including a stale lock left by interruption; that requires inspection.
    if plan["conflicts"]:
        raise SyncError("conflicts block all writes; reconcile manually and preview again")
    if git_root is not None and select_destination(root) != (root, git_root):
        raise SyncError("installation/Git context changed after preview")
    lock = safe_target(root, RUN_LOCK)
    token = uuid.uuid4().hex.encode()
    with lock.open("xb") as stream:
        stream.write(token)
    try:
        _apply_plan(root, assets, plan, source=source, revision=revision, authority=authority,
                    git_root=git_root, template_origin=template_origin)
    finally:
        if snapshot(root, RUN_LOCK) == digest(token):
            lock.unlink()  # Only our own temporary coordination file, never payload.


def _apply_plan(root: Path, assets: dict[str, Asset], plan: dict, *, source: str,
                revision: str, authority: str = "", git_root: Path | None = None,
                template_origin: dict | None = None) -> None:
    if plan["conflicts"]:
        raise SyncError("conflicts block all writes; reconcile manually and preview again")
    if plan.get("_template_is_source"):
        assets = {name: asset for name, asset in assets.items() if not name.startswith("template/")}
    if plan["_assets"] != {name: (digest(a.content), a.mode, a.kind) for name, a in assets.items()}:
        raise SyncError("payload changed after preview")
    updates = [a for a in plan["actions"] if a["action"] in ("create", "update")]
    protected_updates = [a["path"] for a in updates if a["action"] == "update"
                         and any(a["path"].startswith(p + "/") for p in PROTECTED)]
    if protected_updates and not authority.strip():
        raise SyncError("protected updates require --authority identifying the exact human-approved upstream revision/change")
    for name, expected in plan["_expected"].items():
        if snapshot(root, name) != expected:
            raise SyncError(f"destination changed since preview: {name}")
    old_state = load_state(root)
    fresh = make_plan(root, assets, old_state, template_is_source=plan.get("_template_is_source", False))
    if fresh["conflicts"] or fresh["actions"] != plan["actions"] or fresh["_expected"] != plan["_expected"]:
        raise SyncError("destination tree changed since preview; preview again before applying")
    files = dict(old_state["files"]) if old_state else {}
    if plan.get("_template_is_source"):
        files = {name: entry for name, entry in files.items() if not name.startswith("template/")}
    backup_id = uuid.uuid4().hex
    # Back up every replaceable file first, retaining exact bytes and permissions.
    for item in updates:
        if item["action"] == "update":
            name = item["path"]
            destination = safe_target(root, f"{BACKUPS}/{backup_id}/{name}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            original = safe_target(root, name)
            with destination.open("xb") as stream:
                stream.write(original.read_bytes())
            os.chmod(destination, stat.S_IMODE(original.stat().st_mode))
    for item in updates:
        name = item["path"]
        if snapshot(root, name) != plan["_expected"][name]:
            raise SyncError(f"destination changed during apply: {name}; earlier writes/backups retained")
        path = safe_target(root, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        asset = assets[name]
        # Exclusive creation; existing managed files are opened without truncation
        # and checked again on the actual handle before replacement.
        with path.open("xb" if item["action"] == "create" else "r+b") as stream:
            # Confirm the actual opened handle still names the intended regular
            # file before writing (including Windows link/junction checks).
            checked = safe_target(root, name).stat(follow_symlinks=False)
            opened = os.fstat(stream.fileno())
            if ((checked.st_dev, checked.st_ino) != (opened.st_dev, opened.st_ino)
                    or not stat.S_ISREG(opened.st_mode) or opened.st_nlink != 1):
                raise SyncError(f"destination identity changed while opening: {name}")
            if item["action"] == "update":
                if digest(stream.read()) != plan["_expected"][name]:
                    raise SyncError(f"destination changed while opening: {name}")
                stream.seek(0)
            stream.write(asset.content)
            stream.truncate()
        if item["action"] == "create":
            os.chmod(path, asset.mode)
    for item in plan["actions"]:
        name = item["path"]
        if name in assets and item["action"] in ("create", "update", "unchanged"):
            files[name] = dict(sha256=digest(assets[name].content), kind=assets[name].kind)
    if (old_state and not updates and files == old_state["files"]
            and source == old_state["source"] and revision == old_state["revision"]
            and not authority):
        return  # A repeated identical apply does not erase authority or rewrite state.
    history = list(old_state.get("history", [])) if old_state else []
    if old_state and not history:
        history.append({key: old_state.get(key) for key in ("source", "revision", "authority", "backup")})
    history.append(dict(source=source, revision=revision, authority=authority,
                        backup=backup_id if any(a["action"] == "update" for a in updates) else None,
                        paths=[a["path"] for a in updates]))
    payload = dict(schema_version=1, source=source, revision=revision, authority=authority,
                   backup=backup_id if any(a["action"] == "update" for a in updates) else None,
                   files=files, history=history)
    if template_origin is not None:
        payload["template_origin"] = template_origin
        history[-1]["template_origin"] = template_origin
    if git_root is not None:
        payload.update(project_root=str(root), git_root=str(git_root))
    elif old_state:
        payload.update({key: old_state[key] for key in ("project_root", "git_root") if key in old_state})
    if snapshot(root, STATE) != plan["_expected"][STATE]:
        raise SyncError("sync state changed during apply; earlier writes/backups retained")
    # Metadata replacement is atomic; payload writes are deliberately not described
    # as transactional. On an I/O failure retain all work and backups for inspection.
    temporary = safe_target(root, STATE + "." + uuid.uuid4().hex + ".tmp")
    with temporary.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(payload, stream, indent=2, sort_keys=True)
        stream.write("\n")
    os.replace(temporary, safe_target(root, STATE))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-template", default=str(Path(__file__).resolve().parents[1] / "template"),
                        help="local authoritative library; defaults to template/ beside the script's tools/ directory")
    parser.add_argument("--refresh-template", action="store_true",
                        help="replace the local template from --source/--ref, then sync from that local copy")
    parser.add_argument("--source", default=DEFAULT_SOURCE, help="HTTPS Git URL or local Git repository (refresh only)")
    parser.add_argument("--ref", default="HEAD", help="upstream branch/tag/commit (refresh only); pin the previewed commit when applying")
    parser.add_argument("--target", help="existing installation directory inside a Git worktree; defaults to exact cwd")
    parser.add_argument("--apply", action="store_true", help="write a conflict-free plan; default is preview")
    parser.add_argument("--authority", default="", help="exact human authority for existing protected-source updates")
    parser.add_argument("--json", action="store_true", help="emit local template identity, optional upstream commit and plans as JSON")
    args = parser.parse_args(argv)
    try:
        root, git_root = select_destination(args.target)
        template = Path(os.path.abspath(Path(args.local_template).expanduser()))
        # Check aliases before resolving; refreshing must never rename through
        # an alias, or move a directory that contains the target project.
        for component in (*reversed(template.parents), template):
            if component.name.casefold() == ".git":
                raise SyncError("Git metadata is not a local template destination")
            if os.path.lexists(component) and linked(component):
                raise SyncError(f"symlink or junction in local template: {component}")
        template = template.resolve()
        if template == root or template in root.parents:
            raise SyncError("local template must not contain the installation destination")
        template_is_source = template == root / "template"
        if root in template.parents and not template_is_source:
            raise SyncError("a local template inside the target must be its template/ directory")
        if any((parent / ".tadp-lock.json").exists() for parent in template.parents):
            raise SyncError("local template must not be nested inside another protected source")
        state = load_state(root)
        source = str(template)
        if state and state["source"] not in (source, args.source):
            raise SyncError("source differs from recorded installation; reconcile source identity manually")
        upstream_revision = None
        template_backup = None
        with tempfile.TemporaryDirectory(prefix="tadp-upstream-") as directory:
            incoming = Path(directory) / "template"
            if args.refresh_template:
                source_repo = Path(directory) / "repository"
                source_repo.mkdir()
                upstream_revision = fetch_source(source_repo, args.source, args.ref)
                stage_template(incoming, load_assets(source_repo, upstream_revision))
                assets = load_local_assets(incoming)
                local_before = read_template(template) if os.path.lexists(template) else None
                if local_before and not {".tadp-lock.json", "AGENTS.md", "project/AGENTS.md"}.issubset(local_before):
                    raise SyncError("refusing to replace a non-template directory; select a local template library")
                remote_files = read_template(incoming)
                template_actions = [dict(path=name,
                    action="retain-backup" if name not in remote_files else
                           "create" if local_before is None or name not in local_before else
                           "unchanged" if local_before[name] == remote_files[name] else "replace")
                    for name in sorted(set(local_before or {}) | set(remote_files))]
            else:
                assets = load_local_assets(template)
                local_before = read_template(template)
                template_actions = []
            revision = template_revision(assets)
            plan = make_plan(root, assets, state, template_is_source=template_is_source)
            origin = dict(authority="remote" if args.refresh_template else "local", local_template=source)
            if args.refresh_template:
                origin.update(upstream_source=args.source, upstream_revision=upstream_revision)
            warnings = ["All target files are synchronized from the local template; remote authority replaces that library first.",
                        "Source synchronization is not template completeness or protocol adoption; run project validation and review any references to excluded records.",
                        "Project work and retired target files are preserved; no automatic merge, hook activation, staging or commit is performed."]
            result = dict(source=source, revision=revision, mode="apply" if args.apply else "preview",
                          template_authority=origin["authority"], local_template=source,
                          upstream_source=args.source if args.refresh_template else None,
                          upstream_revision=upstream_revision, template_actions=template_actions,
                          template_backup=None, template_refreshed=False,
                          project_root=str(root), git_root=str(git_root),
                          actions=plan["actions"], conflicts=plan["conflicts"], warnings=warnings, applied=False)
            if args.apply and not plan["conflicts"]:
                # Reject missing authority for either phase before any source or
                # target writes. A flag records human authority; it creates none.
                protected_updates = any(item["action"] == "update" and
                    any(item["path"].startswith(prefix + "/") for prefix in PROTECTED)
                    for item in plan["actions"])
                if (protected_updates or args.refresh_template and local_before is not None) and not args.authority.strip():
                    raise SyncError("protected updates/replacement require --authority identifying the exact human-approved revision/change")
                if args.refresh_template:
                    # Preflight destination drift and an existing target lock
                    # before replacing the local source. Apply checks them again.
                    if os.path.lexists(safe_target(root, RUN_LOCK)):
                        raise SyncError("existing target sync lock blocks local template replacement")
                    fresh = make_plan(root, assets, load_state(root), template_is_source=template_is_source)
                    if fresh != plan:
                        raise SyncError("destination changed since preview; local template was not replaced")
                    template_backup = replace_template(template, incoming, local_before, args.authority)
                    result.update(template_backup=template_backup, template_refreshed=True)
                # Even refreshed syncs read the actual installed local copy. The
                # fetched payload is never passed directly to the target writer.
                assets = load_local_assets(template)
                if template_revision(assets) != revision:
                    raise SyncError("local template changed since preview; refusing target writes")
                origin["backup"] = template_backup
                apply_plan(root, assets, plan, source=source, revision=revision,
                           authority=args.authority, git_root=git_root, template_origin=origin)
                result["applied"] = True
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"TADp {result['mode']}: {source} @ {revision}")
            print(f"Template authority: {result['template_authority']}")
            if args.refresh_template:
                print(f"Replace local template from: {args.source} @ {upstream_revision}")
                for item in template_actions:
                    print(f"{item['action']:14} local template/{item['path']}")
            if template_backup:
                print(f"Previous local template: {template_backup}")
            print(f"Project root: {root}")
            print(f"Git root: {git_root}")
            for item in plan["actions"]:
                print(f"{item['action']:10} {item['path']}: {item['reason']}")
            for warning in warnings:
                print(f"NOTE: {warning}")
            if result["applied"]:
                print(f"Applied. Baselines: {STATE}; previous managed bytes: {BACKUPS}/ (when updated).")
            elif plan["conflicts"]:
                print("Blocked: conflicts; no local template or target writes performed.")
            else:
                print("Preview only; no local template or target writes. Use --apply after review.")
                if args.refresh_template:
                    print(f"Pin the reviewed remote revision with --ref {upstream_revision}.")
        return 1 if plan["conflicts"] else 0
    except (OSError, UnicodeError, SyncError, subprocess.SubprocessError) as error:
        print(f"error: {error}", file=sys.stderr)
        if locals().get("template_backup"):
            print(f"Local template was replaced; previous library retained at {template_backup}. Inspect before retrying.", file=sys.stderr)
        elif locals().get("result", {}).get("template_refreshed"):
            print("Local template was installed before the target error. Inspect both trees before retrying.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
