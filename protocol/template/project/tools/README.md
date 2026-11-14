# Project runtime tools

These files copy directly. Use Python 3.11 or later, Git and the project's
configured interpreter. Run commands from project installation root `P`,
which may equal or lie beneath Git worktree root `G` under
[specification 05](../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
The installed library `P/template/` and upstream source `template/project/`
are protected reusable material, never active targets by shape alone.
The following examples are inert until an authorized invocation executes them.

| Command | Effect |
|---|---|
| `python tools/tadp_protect.py check .` | Read-only integrity check: exit 0 passes, 1 reports drift, 2 rejects input. |
| `python tools/tadp_validate.py . --json` | Read-only structural checks: exit 0 has no errors, 1 has findings, 2 rejects input. |
| `python tools/tadp_sync.py [--target DIRECTORY] --json` | Preview an upstream update into an existing selected directory, default exact cwd; report absolute project_root and git_root without project writes. |
| `python tools/tadp_sync.py --ref UPSTREAM_COMMIT --apply` | Apply a reviewed conflict-free update; existing protected changes also need `--authority` naming actual human authorization. |

The keyword tool reads the protected registry. Scope and template modules
supply runtime APIs and objective checks; they do not allocate work or create
decisions. Template checks include folder READMEs and the nonrecursive library
placeholder. Passing structural checks proves no adoption or product claim.

Validation and protection accept explicit root arguments, defaulting to exact
cwd; the keyword CLI requires its root argument. Sync `--target` is
cwd-relative when relative and otherwise defaults to exact cwd. It never
redirects to the Git top level, script distribution, ancestor or sibling.
An unidentified/uninstalled default cwd beneath an installed ancestor is
ambiguous and rejected; explicit selection can identify a deliberate independent
nested installation. An already verified installed nested project remains a
valid default. No ancestor inspection goes above `G`. Missing
Git, unsafe paths, malformed identified scaffolds or contradictory root
evidence fail before writes. Manual compatible installs need no sync state.

Inert examples (`UPSTREAM_COMMIT` is the actual previewed hash):

~~~text
# At the Git root (P = G):
python C:/distribution/protocol/tools/tadp_sync.py --json
# Existing nested project P, invoked from any directory:
python C:/distribution/protocol/tools/tadp_sync.py --target C:/repository/projects/widget --json
python C:/distribution/protocol/tools/tadp_sync.py --target C:/repository/projects/widget --ref UPSTREAM_COMMIT --apply
~~~

Sync returns 0 for a conflict-free preview or successful apply, 1 for conflicts
with no target writes, and 2 for invalid input, unsafe source/destination,
missing authority, Git or I/O errors. Apply may leave partial writes and
retained backups on I/O failure. Protection guard-staged returns 0 when allowed,
1 when blocked and 2 on inspection/input errors. Lock initialize/refresh are
separately authorized writers requiring `--authority`; 0 succeeds, 2 rejects.
Scope/template modules are APIs, not standalone commands. See
[adoption and Git coordination](../docs/guides/project-root-installation-migration.md).

## Preserve project work

Synchronization copies `.template.md` sources unchanged, preserves existing
scaffold files and user work, refuses conflicts, and retains retired files.
It saves managed replacements under `.tadp-sync-backups/`. Keep
`.tadp-sync.json` for content hashes, source revision and authority history.
State, `.tadp-sync-backups/`, `.tadp-sync.lock`, protected locks, tools and
scaffold files stay under `P`; preview writes none. New state records absolute
root evidence; earlier compatible state remains supported. Use `G` for Git
operations with the verified project prefix for historical and staged paths.
Preserve unrelated parent and sibling staged, unstaged and untracked work.
Refs, index, worktree state and hooks are shared, with existing branch rules.
Report incompatible branch roles or outside-project integration constraints.
Manually coordinate hooks at `G` without overwriting or enabling parent hooks.
There is no delete or force option. The complete library is installed once;
its source `project/template/README.md` is only a nonrecursive placeholder.

The payload excludes TADp development reports, decisions, live initiatives,
delivered products and regression fixtures. It installs no test results or
project-specific evidence. No hooks, Git configuration, staging, commits,
merges, pushes or lifecycle events occur automatically.

Apply is not transactional. Avoid concurrent writers. Inspect retained files
and backups after an I/O failure before retrying. Inspect an interrupted run's
`.tadp-sync.lock` before manually reconciling it.

## Authority and verification

Actual project records require the owning workflow and sufficient evidence.
`initialize` and `refresh` require separately authorized source maintenance;
ordinary work uses `check`. Never refresh a lock to hide unexplained drift.
See [validation guidance](../docs/development/validation-and-quality.md) and
[the governing suite](../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
[Project tests](../tests/README.md) arise from actual scoped work; the clean
baseline supplies no TADp regression suite or fictional verification.
