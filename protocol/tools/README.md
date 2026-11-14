# TADp tools

Run commands below from `protocol/` in this distribution, or the root of an
adopted TADp project. `python` means that project's configured interpreter;
the maintained checks were verified with Python 3.11.1. Examples are reference
commands and do not execute when this document is read.

## Project root and installation directory

[Specification 05](../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement)
defines project root `P` as the resolved scaffold installation directory.
Its direct children include `AGENTS.md`, `evidence/`, `initiatives/`,
`products/`, `prompts/`, `template/` and `tools/`. The installed
`P/template/` is the reusable library; upstream `protocol/template/project/`
is a protected source. Neither template directory selects an active project.

Git remains mandatory. Its discovered worktree root `G` may equal `P` or
contain it. Git metadata may be a directory or linked-worktree `.git` file;
no separate metadata entry is required at a nested `P`. Checks of `protocol/`
in this distribution use that checked root with Git rooted above it, without
establishing live project adoption.

Validation and protection take an explicit `root`, defaulting to the exact
current directory. Sync selects an existing `--target DIRECTORY` or the exact
current directory when omitted. Relative targets are cwd-relative; the script
location and Git top level never redirect the destination. Sync prints absolute
`project_root` and `git_root` in text and JSON preview/apply output. Unsafe
or contradictory targets fail before writes; no ancestor or sibling lookup
selects a different project. If default cwd is not itself an identified
installation but lies beneath an installed project, the ambiguous default is
rejected; use explicit `--target` for a deliberate independent nested
installation. A verified installed nested project remains a valid default.
Ancestor inspection rejects ambiguity and never redirects. Installed markers and state, when available, corroborate the
target; malformed identified installations fail. Valid manual installations
need no sync-state file. New sync state records absolute root evidence while
older state without those fields remains compatible.
A project-local prompt instead derives `P` from its verified installed
`prompts/AGENTS.md`. Reconcile conflicting target evidence before action.

Files, runtime tools, installed library, `.tadp-sync.json`, backups at
`.tadp-sync-backups/`, temporary `.tadp-sync.lock` and protected locks all
stay under `P`. Preview creates none of them. Parent instructions remain
applicable; sibling projects and nested repositories, worktrees, submodules or
scaffolds remain outside project authority. Reject escaping links/junctions.
See [prospective adoption](../docs/guides/project-root-installation-migration.md).

## Command reference

| Entry point | Inputs and output | Exit and effect |
|---|---|---|
| `python tools/tadp_validate.py [root]` | Root defaults to `.`; `--json` emits `root`, `valid`, error/warning counts and findings; `--base-ref` selects the closed-claim comparison revision, default `HEAD`. | Read-only. `0`: no errors, including warnings-only results; `1`: errors; `2`: nonexistent root or invalid CLI arguments. |
| `python tools/tadp_protect.py check [root]` | Root defaults to `.`; text findings for both protected roots. | Read-only. `0`: locks match; `1`: integrity findings; `2`: invalid root or arguments. |
| `python tools/tadp_protect.py guard-staged [root]` | Inspects actual staged/unstaged protected paths and matching recorded update authority. | Read-only commit gate. `0`: permitted; `1`: blocked; `2`: inspection or argument error. |
| `python tools/tadp_keywords.py root --prompt-id ID --text TEXT` | Explicit prompt text and identity; reads the canonical registry and emits JSON interpretation blocks. | Read-only. `0`: interpreted; `2`: invalid arguments or registry/input error. It performs no requested work. |
| `python tools/tadp_sync.py [--target DIRECTORY] [--ref REVISION] [--apply] [--authority REFERENCE] [--json]` | Select an existing target directory, default exact cwd, contained in a valid Git worktree; fetches the canonical GitHub template and pins its actual commit. Defaults to a preview. | `0`: conflict-free preview or successful apply; `1`: conflicts, no target writes; `2`: invalid input, unsafe source/destination, missing authority, Git or I/O error. An I/O failure during apply can leave partial writes and retained backups. |
| `python tools/tadp_reset.py [--json]` | Preview a reset of the TADp project directly above this script's `tools/` directory. `--apply` also requires `--confirm` with that exact absolute project path and `--backup` with a new external directory. | `0`: preview or verified reset; `2`: invalid input, protected drift, unsafe paths, changed files or I/O error. A failure during apply may leave partial changes; retain the backup. |
| `tadp_scopes.py`, `tadp_templates.py` | Python library APIs described below; called by the validator where applicable. | No standalone CLI. Integration helpers have their own explicit side effects and authority requirements. |

`initialize` and `refresh` are the protection tool's separately authorized
maintenance actions, not ordinary validation. Both accept repeated
`--protected-root template` or `--protected-root evidence/authoritative/LLM`
selectors and require `--authority`; without selectors they address both
roots. They write locks, return `0` on success and `2` for rejected input or
baseline conditions. See the governed procedure in
[Validation and quality](../docs/development/validation-and-quality.md#protected-source-workflow).

## Reset a TADp project to its installed template

`tadp_reset.py` removes user work from the **TADp project directory**, located
one level above the script's own `tools/` directory. The current working
directory does not select the target. A repository may contain several TADp
projects or have one at its Git root. Only the selected project is reset;
siblings and the enclosing repository are left alone. Git is required.

The local, locked `template/project/` supplies the clean scaffold. The command
restores its files, including `.template.md` record sources, without filling
them or creating live records. All other project files and empty directories
are removed, including initiatives, evidence, products, code, tests, local
prompts, sync state/backups, untracked files and ignored environments. It does
not fetch a newer template. Existing runtime files are restored from the local
scaffold. The complete `template/` library, installed
`evidence/authoritative/LLM/` suite, and `tools/tadp_reset.py` itself are retained
unchanged. The embedded invariant suite and nonrecursive `template/README.md`
placeholder do not overwrite those retained sources.

Both protected locks must pass before preview or apply. There is no lock
refresh, gate override or protected-source reset option. A reset does not
cancel, reopen, accept or complete initiatives, or establish adoption. Git
metadata, history, branches, index and configuration remain in place; the
resulting working-tree changes are not staged or committed. A root `.git`
directory or linked-worktree `.git` file is retained. Nested repositories,
links/junctions, hardlinks and unsafe or case-colliding paths block the command.

Preview first. For this distribution the target is `protocol/`; in an adopted
project it is wherever its `tools/` directory lives. These are inert examples;
replace the confirmation with the exact `root` printed by your preview:

```powershell
python C:/path/to/project/tools/tadp_reset.py --json
python C:/path/to/project/tools/tadp_reset.py --apply --confirm 'C:\path\to\project' --backup C:/backups/project-before-reset
```

`--backup` must name a new directory outside the entire enclosing Git worktree
and its metadata, with an existing parent. Before any deletion, the tool saves
all non-retained project files under `BACKUP/files/`, verifies their bytes and
writes `BACKUP/reset-manifest.json` with original hashes, modes, directories and
the planned changes. Protected sources and Git remain at their original paths.
Use a Python interpreter outside the target project: a local environment inside
the target is itself user work to remove. To use this standalone tool with an
older installed template, copy it to that project's `tools/` beside
`tadp_sync.py`; synchronization's current payload does not install it.

Do not run concurrent writers. File changes detected during planning, backup
or removal stop the operation. An exclusive `tadp-reset.lock` in the enclosing
Git metadata serializes resets across sibling TADp projects. Inspect an
interrupted run before manually removing a stale lock. Apply is not atomic:
an I/O failure or late concurrent edit may leave partial changes. Keep the
external backup and inspect the error and target before recovery; the command
does not automatically restore files over subsequent edits. After a successful
reset, review the Git diff and run the ordinary protection and validation
checks. A clean scaffold still needs real ownership and adoption records.

## Synchronize template sources into a project

Use `tadp_sync.py` with Python 3.11 or later and Git. Run from the selected
project installation directory, or name its existing directory with
`--target` from any working directory. Use an absolute script path if it is
not installed there. Every sync reads the local `template/` beside the script's
`tools/` directory. Use `--local-template PATH` to select a different library.
Default local authority uses current on-disk bytes and never fetches remote
content. The library must have valid locks and contain its project suite and
runtime tools; incomplete historical libraries need a complete refresh first.

Choose `--refresh-template` to make the remote authoritative: preview replacement
of the local library, then use `--apply` to back up and replace it before syncing
from the replaced local files. Refresh defaults to
`https://github.com/spkvfx/TADp.git` and upstream `HEAD`. `--source` accepts
another trusted HTTPS Git repository or local repository with the `protocol/`
distribution layout. `--ref` pins its branch, tag or commit. These arguments
are used only with `--refresh-template`. Fetched programs and hooks are never
executed during synchronization.

These are inert command examples. Here `python` denotes the configured
interpreter, and `UPSTREAM_COMMIT` is the exact hash printed by the preview:

```powershell
# Git-root installation: run from C:/work/repository (P = G).
python C:/path/to/TADp/protocol/tools/tadp_sync.py --json
python C:/path/to/TADp/protocol/tools/tadp_sync.py --apply
# Nested installation: existing C:/work/repository/projects/widget is P.
python C:/path/to/TADp/protocol/tools/tadp_sync.py --target C:/work/repository/projects/widget --json
python C:/path/to/TADp/protocol/tools/tadp_sync.py --target C:/work/repository/projects/widget --apply
# Remote authority: preview first, then pin and authorize the exact replacement.
python C:/path/to/TADp/protocol/tools/tadp_sync.py --refresh-template --json
python C:/path/to/TADp/protocol/tools/tadp_sync.py --refresh-template --ref UPSTREAM_COMMIT --authority "Approved revision/change receipt" --apply
```

The payload contains the complete local library at
`template/`, project scaffold files from `template/project/` at the target
root, the runtime invariant suite, and the named `tadp_*.py` runtime tools.
The embedded suite and tools are authoritative, including when distribution
development tools differ. Both source locks must match their complete trees.
The script copies source locks unchanged and never refreshes them.
It excludes the distribution's live initiatives, products, realizations,
decisions, development reports and regression tests. The consolidated project
baseline includes its own project-use guides and empty navigation folders;
the loader accepts the named operational guides and rejects development
reports, unknown development documents and decision records.
It does not copy the reference repository's root maintenance `prompts/`.

All `.template.md` files copy unchanged as record sources. They do not become
live initiative, profile or decision records during synchronization. The
project baseline's `template/README.md` is a nonrecursive placeholder: the
complete outer library supplies the installed `template/` once, retaining its
own README. Additional contents under that placeholder are rejected.

Existing scaffold files such as root `README.md`, `AGENTS.md`, project prompts
and `.githooks/pre-commit` are preserved. Missing scaffold sources are copied
without populating project-specific fields or instantiating live work records.
Review existing instructions against newer scaffold sources under
`template/project/` manually. A preserved root hook is not automatically
upgraded or enabled.

`.tadp-sync.json` records the local library path, content revision and raw hashes,
plus history of authority choices, remote commit provenance and backups.
Keep it with the project. Existing managed files update only when they still
match their recorded installation; identical upstream files can establish a
baseline on the first run. Unmanaged collisions, locally edited managed files,
and locally removed installed files require manual reconciliation. Any
conflict prevents all target writes. Preview does not create state or backups.
Local and remote authority share the same local-library source identity, so
switching between them is supported. A previous direct-remote installation
can transition when its recorded source matches `--source`; choosing a
different local-library path requires manual identity reconciliation.

Existing protected-source updates additionally require `--authority` naming
the human-approved revision and exact change, for example a project decision
receipt. This argument records authority; it cannot create authorization.
Review compatibility and adoption requirements before approving that update.
Local additions or source removals that would contradict an incoming
target protected lock block the sync. Target-retired files and user work remain
in place. Remote replacement of an existing local library additionally needs
`--authority`; its complete previous directory, including retired or modified
files, is retained under `.tadp-template-backups/<run-id>/template` beside the
local library. Locks are copied unchanged. Target conflicts and missing authority
block both phases before writes. Preview changes neither tree. When the source
is the target's own `template/`, only refresh manages that library; sync uses it
to update runtime and missing scaffold files without copying it over itself.
The tool never stages,
commits, merges, changes Git configuration, enables hooks or deletes branches.

Before replacing a managed file, the script saves its exact previous content
under `.tadp-sync-backups/<run-id>/<original-path>`. Retain these backups until
the update has been reviewed. Run without concurrent writers; changes detected
between planning and writing abort the operation. Apply is not a transaction:
an I/O failure can leave some files updated, with backups retained and an error
exit. Inspect those paths and reconcile them manually before retrying; the
script never deletes work as rollback or restores backups over user edits.
An exclusive `.tadp-sync.lock` serializes sync runs and is removed only by its
own invocation. If interruption leaves it behind, inspect it before manually
reconciling the stale lock; the tool never removes another run's lock.
An additional `.tadp-template.lock` beside the local library serializes source
replacement. Replacement uses a staged directory on the same filesystem and
retains old bytes before switching directories. A later target-write failure
can leave the refreshed library installed; inspect retained backups and any
`.tadp-template-stage-*` directory before retrying. Neither phase automatically
rolls back over later user changes.

Source synchronization does not establish project adoption, migration,
acceptance or lifecycle completion. A new clean baseline still needs actual
project ownership, adoption and applicable coordination records populated
through their owning workflows; synchronization does not invent them. Earlier
published distributions may retain missing-guide or historical-link findings.
Report those gaps rather than importing protocol-development records to make
validation pass. After installation, review the template completeness prompt,
the project's recorded governing revision, required manual scaffold changes,
and the actual protection/validation findings. Use
`python tools/tadp_protect.py check .` and `python tools/tadp_validate.py .`
from the adopting root; do not infer a passing result from successful copying.

`tadp_templates.py` supplies read-only checks for the installed
[canonical coverage map](../template/TEMPLATE-COVERAGE.md) and documentary
prerequisite declarations in all fourteen workflow prompts and scope closure.
The full validator invokes these checks; the module has no writer or stage
dispatcher. `TADP050` reports missing or malformed coverage, sources, sections,
governing locators, or unsafe instance destinations. `TADP051` reports missing
or inconsistent prompt prerequisites or the shared preparation procedure.
`TADP052` reports a missing project-folder README, the obsolete sibling
initiative-source owner, or contents beyond the nonrecursive placeholder.
New-baseline link checks resolve the placeholder against the actual installed
library; missing library targets remain errors.
Earlier distributions without this contract retain their recorded behavior;
installation checks do not adopt the revision for live initiatives.

The optional `assess_prerequisites(root, requirements, context)` API consumes
explicitly reviewed evidence facts and returns classifications, owning-stage
recovery order, and blockers. `ready` requires current applicable documents and
the supplied actual gates; constructible paperwork is still missing. The
caller must establish semantic sufficiency, genuine authority, correct type,
identity, phase and revision. `instance_link_issues` checks links at an actual
instance's destination depth. Neither helper copies templates, authenticates
instructions, repairs records, or proves that an event occurred. See the
[recovery guide](../docs/guides/template-prerequisites-migration.md).

Run the repository validator from the protocol root (`protocol/` in the
reference repository and normally the project root in an adopted repository):

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
```

Use the validator's `--json` option for continuous integration or another
machine consumer. The protection tool's output is text. A directory that
exists but lacks a valid TADp/Git scaffold produces validator findings and
exit `1`; a nonexistent root produces exit `2`.

The validator checks the Git worktree and project-root `AGENTS.md` requirements,
protocol structure, protected template and authoritative-LLM SHA-256 locks,
the project-local prompt boundary and its reusable-source alignment, required
developer documentation, local Markdown links, unresolved
prose tokens outside reusable templates, complete initiative suites, legal lifecycle
transitions, acceptance receipts, type-specific execution or delivery records,
completion evidence, human decision receipts, all fourteen numbered prompt
contracts, source-mapping fields, and—after a project declares the correlation
revision effective—legacy work-version syntax, reciprocal tuple metadata,
branch continuity and migration dispositions. After explicit version-scope
adoption, it also validates shared scope membership, precise source routing,
major/minor/patch topology, recorded execution placement and closure evidence.
Its checks grow with the binding TADp
specifications; passing validation never replaces human acceptance, delivery
verification, or product verification.

After the project profile records a resolved `Coherence revision baseline`,
validation also checks the work-conflict register, completion reviews of every
other open initiative, and terminal-record preservation against Git. Proposed
effort is included in the review without gaining authority. Historical closed
claims preserved at the adoption baseline do not acquire invented reviews.

The terminal comparison defaults to `HEAD`. Use a captured integration or
merge-base commit to review a whole branch:

```powershell
python tools/tadp_validate.py . --base-ref <captured-base-commit>
```

The guard detects record edits and missing reopening evidence; it cannot judge
semantic compatibility or whether the named human had authority. See the
[coherence migration guide](../docs/guides/initiative-coherence-migration.md)
for the separate adoption-baseline and comparison-base roles.

The path supplied to the validator must be the protocol or adopted TADp root
and must be contained in a valid Git repository. The Git metadata may be at
that path or an ancestor, as it is in this reference repository where
`protocol/` is the distributable protocol tree and the parent directory is the
Git root. Git operations use `G` and map project paths through the verified
`P`-relative-to-`G` prefix for staged protection and historical comparisons.
They do not include parent or sibling changes. Refs, index, worktree state and
hooks are shared: existing branch-role rules remain, and incompatible roles or
outside-project changes may block integration. Project-scoped commit authority
permits necessary Git metadata operations, never outside-project file changes
or commits. Coordinate hooks manually at `G`; a nested hook path includes its
project prefix. Installation does not change configuration or enable hooks.

`tadp_protect.py` owns deliberate lock creation and refresh. `initialize`
refuses to replace an existing lock, `refresh` refuses to create a missing
lock, and both require a non-empty `--authority` reference. Ordinary work must
use `check` only. The `guard-staged` action is called by the tracked pre-commit
hook and blocks protected-source commits unless the explicit update variables
and refreshed lock carry the same authority reference. See
[Validation and quality](../docs/development/validation-and-quality.md) for the
governed commands and limitations.


`tadp_keywords.py` consumes the single protected registry in
[specification 11](../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
It exposes positional interpretation, objective exception-record checks,
preview/local action checks, independent-review checks, and an asynchronous
reference scheduler for explicitly classified action trees. The validator
checks installed registry structure and universal entry-point links when that
revision is present; earlier projects retain their recorded governing revision.
Stored prompts and evidence are never scanned to activate directives.

```powershell
python tools/tadp_keywords.py . --prompt-id request-1 --text "Inspect first [tadp:preview] propose a change"
```

The CLI reports source blocks and requested settings; it performs no work and
adopts no exception. Callers must identify semantic explanatory ranges, actual
action lists, dependencies, tool permissions, specific human authority, and
active exception duration. Source settings snapshots are immutable. The list
scheduler joins nested children, preserves serial blockers, runs bulleted
siblings concurrently, and reports capacity limits before dispatch rather
than silently serializing declared parallel work.

`ExceptionRecord` records exact authority, rule/revision, source block, targets,
settings, prior state, method, actual agent dispositions, risks, evidence
limits, reconciliation, and restoration. `evaluate_gate` fails closed without
an exact active target scope; it preserves the original observed result and
never turns an exception into passing evidence. A preview exception remains a
response-only proposal; preview analysis and proposals use read-only action
checks without persisting or adopting an exception. Separate protected-source
maintenance must actually reconcile and verify locks through `tadp_protect`.
These helpers cannot authenticate human authority, classify natural-language
intent, establish semantic review quality, or intercept arbitrary agent tools.
The governing agent remains responsible for enforcing the canonical contract.

`tadp_scopes.py` supplies the prospectively adopted version-scope model.
`parse_scope` accepts exact `vN`, `vN.M`, and `vN.M.P` identities, compares
components numerically and preserves arity. `scope_parent` derives only the
structural major/minor parent; major scopes use the project's explicitly
recorded integration branch. No helper infers migration or source authority.

An immutable `Version scope revision effective point` in `project-profile.md`
activates `initiatives/version-scopes.md`, the scope membership table in
`initiative-index.md`, and `version-scope-migration-ledger.md`. Absence,
`Not yet adopted`, and `Installed; adoption pending` retain legacy handling.
The module exports `SCOPE_HEADERS`, `MEMBER_HEADERS`, `MIGRATION_HEADERS`, and
`SOURCE_HEADERS`; templates use those table shapes. Original tuple tables and
their legacy ledger remain checked when retained alongside the new table.
Deferred records do not qualify for delegated reopening just because a
project has adopted scopes; the target needs actual new canonical membership.

Read-only checks cover explicit suite/note identities and metadata, reciprocal
links, source catalogs, grouped paths and types, branch roles and captured
ancestry, scope navigation, current cycle/claim acceptance and delivery records,
closed-member/child integration evidence, and required scope reopening.
Recorded scope creation fields and execution assignment history are compared
with `HEAD`. This scope-table comparison does not inspect every intermediate
commit in a branch range; review must inspect those transitions separately.
The existing coherence guard retains its independent `--base-ref` range checks
for closed initiative claims. Human authority authenticity, narrow semantic
fit, ownership, completeness of an inventory and verification quality still
require review; objective fields cannot establish them.

`integrate_closed_child(root, IntegrationRequest(...), verify)` is an optional
bounded local helper, not a workflow dispatcher. Callers first persist the
actual closure instruction/authority, inspect accepted source changes and the
current parent, and check ownership of every included change. The helper
requires the recorded parent already checked out, a clean worktree, matching
captured source/target tips, closed source, open parent and qualified changes.
It rechecks refs/worktree after pre-verification and records direct placement,
no-deliverable, fast-forward, merge, already-integrated, or blocked results.
Conflicts and failed post-verification retain actual Git evidence; the helper
does not revert, delete branches, push, or invoke a hosting service. Callers
persist the result and post-verification evidence; it never accepts an
initiative or closes ancestors. Shared completed members must record their
`Verified member commit` separately from the whole shared tip.

`test_tadp_scopes.py` uses isolated Git repositories for shared/dedicated
placement, cross-scope provenance and mixed types, full adopted-project
validation, delegated terminal-state reopening, current-cycle acceptance,
closure blockers, precise numeric syntax, integration reruns, drift and real
conflicts. These fixtures are protocol-owned and do not migrate live projects.
