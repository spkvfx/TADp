# Project installation root and prospective adoption

The owning definition is [specification 05](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
The project root `P` is the resolved directory receiving the project scaffold.
The Git worktree root `G` is discovered through Git for `P`. `P` may equal `G`
or be a directory beneath it. A `.git` directory or linked-worktree `.git`
file belongs to Git; a separate metadata entry at `P` is unnecessary.

Project records and paths are relative to `P`. The source distribution
`protocol/`, source `template/project/` and installed `P/template/` library
have distinct roles. A protected template source is never an active target.
In the reference checkout, checks target `protocol/` while Git is rooted above
it; this does not adopt that distribution as a live project.

## Destination selection

`tadp_sync.py --target DIRECTORY` selects an existing destination explicitly;
relative paths are relative to the invocation's working directory. Without
`--target`, the exact current directory is selected. The script location and
Git top level never substitute for that destination. Preview and apply print
absolute `project_root` and `git_root`, also present in JSON output. Inspect
them before applying the pinned revision. Unsafe or contradictory targets
fail before writes. No upward search selects an ancestor or sibling project.
If default cwd is not itself an identified installation but lies beneath an
installed project, sync rejects that ambiguous default; explicit `--target`
can identify a deliberate independent nested installation. A verified installed
nested project remains a valid default. Ancestors are inspected only to reject
ambiguity and are not inspected above `G`. Identified
installed scaffolds with malformed markers fail. New sync state records
absolute root evidence; older state lacking those fields remains compatible.

Validation and protection accept an explicit `root`, defaulting to the exact
current directory. The keyword CLI requires its root argument. Reset keeps its
separate script-location target contract. See the [command reference](../../tools/README.md)
for exit codes and failure behavior. A project-local prompt derives `P` from
its verified installed `prompts/AGENTS.md`, retaining all parent instructions.
When multiple pieces of target evidence are supplied, reconcile them before
action. A manually installed compatible scaffold need not have sync state.

All synchronized files, installed tools and library, `.tadp-sync.json`,
`.tadp-sync-backups/`, `.tadp-sync.lock` and protected locks stay under `P`.
Preview creates none of them. A successful copy is installation evidence,
not adoption, acceptance, reopening, completion or release.

## Adopt the revision

The revision becomes available at the first coherent commit containing the
authorized invariant, consumers, verification and affected locks, identified
by the specification's revision record and Git history. Do not infer a future
hash or replace an earlier governing revision merely because files arrived.

1. Capture current Git identity, commit, branch and all worktree/index changes.
   Preserve unrelated work and existing root-installation paths.
2. Record sufficient human adoption authority, the exact available revision,
   prior governing revision, resolved `P`, discovered `G`, verified prefix,
   baseline and affected active work in the project profile change record.
3. Review installed sources and operating instructions at that revision.
   Preserve historical claims, decisions, assignments, exceptions and earlier
   compatible governing revisions. Reconcile existing instructions manually.
4. Run protection and validation for that exact project root. Record actual
   results and remaining findings. Installation and passing structural checks
   alone do not establish adoption or compliance with substantive requirements.

This route moves no files or live projects and creates no nested repository.
Any relocation or live-work migration needs its own authority and evidence.

## Shared Git coordination

Use `G` for Git operations and prefix project paths with verified `P` relative
to `G`. Historical comparisons and staged protection inspect that project's
paths. Commits must contain only authorized project changes; preserve parent
and sibling staged, unstaged and untracked work. Necessary metadata operations
for an authorized project commit do not authorize outside-project file changes.

All projects in an enclosing worktree share refs, index, worktree state and
hook configuration. Existing branch and scope rules still apply. Detect
incompatible branch roles and coordinate rather than claiming independent
project branches or inventing a new naming scheme. Whole-ref integration may
remain blocked by outside-project changes even when a project itself is clean.

Inspect existing hook configuration at `G` and coordinate a single dispatcher
manually. For a nested project, a hook path is relative to `G` (for example
`projects/widget/.githooks`), not implicitly relative to `P`. Installation does
not set `core.hooksPath`, overwrite parent hooks or enable any hook. Other
scaffolds, worktrees, repositories and submodules remain separate boundaries,
including when physically beneath `P`. Reject escaping links and junctions.
