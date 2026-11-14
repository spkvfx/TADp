# Codex Git workflow specification

## Requirement

Every TADp project must be contained in a valid Git worktree. Its **TADp
project root**, `P`, is the resolved destination directory receiving the
installed project scaffold. Project paths are relative to `P`, including
`AGENTS.md`, `evidence/`, `initiatives/`, `products/`, `prompts/`, `template/`
and `tools/`. Before installation, `P` is the explicitly selected destination;
after installation, verify the installed scaffold and available installation
evidence. A sync-state file is not required for manual or earlier compatible
installations.

The **Git worktree root**, `G`, is the actual enclosing root discovered through
Git for `P`. `P` may equal `G` or be beneath it. Git metadata may be a directory
or a linked-worktree `.git` file; no separate `.git` entry at `P` is required.
Git history is part of traceability; a copied directory or informal change log
is no substitute. An enclosing worktree supplies Git identity and history
without expanding the project's file boundary.
Discover actual current branches, integration configuration and refs from Git;
never assume `main`, `master`, a remote or a hosting service.

### Root resolution and ownership

Resolve `P` from the invoked context: an explicit tool target, the verified
installed project-local `prompts/AGENTS.md`, or a documented installation
destination. Check consistency when multiple contexts apply. For an installed
project-local prompt, `P` remains the parent of its verified `prompts/`
directory. Ambiguous or contradictory targets block the affected action
before writes. Never silently redirect to `G`, an ancestor scaffold, a sibling,
the script's distribution, or a protected reusable source.

The source distribution `protocol/` assembles installations; it is not
automatically the target project. Source `template/project/` is protected
scaffold material, and installed `P/template/` is the protected reusable library
within a project. Neither source is an active project merely because it is
read or copied. Reference-repository checks use `protocol/` as their checked
root with Git rooted above it; this does not adopt it as a live project.

Ownership ends at `P` and any narrower authorized boundary. Other scaffolds,
repositories, worktrees and submodules nested under `P` remain outside that
ownership. Resolve symlinks and junctions, reject escaping destinations, retain
applicable parent instructions, and preserve parent and sibling files.

Run Git operations using verified `G` and map project-relative paths through
the verified `P`-relative-to-`G` prefix. This applies to historical comparisons,
base refs, diffs, staged protection, staging, commits and installed hooks.
Inspect both sides of renames and all included paths. Project authorization
can cover necessary Git metadata operations for its authorized commits, but
cannot cover outside-project file changes or commits. Validators are read-only
and protection checks must not repair locks.

An enclosing repository shares refs, index, worktree state and hook
configuration. Nested projects have no independent branch namespace. Preserve
the branch rules below, detect incompatible roles, and report coordination
limits rather than inventing names or silently sharing assignments. Hook
coordination is manual; installation must not overwrite or enable parent hooks.

### Installation-root revision record

- **Authority:** The User's 2026-11-13 explicit invocation of
  `prompts/project-root-installation-directory-protocol-change.md`, captured
  as ROOT-DR-001 in the distribution source
  `docs/development/project-root-installation-maintenance.md`.
- **Reason:** Make the scaffold installation destination the project boundary
  while retaining mandatory Git traceability in an enclosing worktree.
- **Affected scope:** This requirement and necessary root/path consumers in
  the suite index, instructions, scaffold, tools, fixtures, documentation and
  affected protected locks. No other evidence, identity, lifecycle, acceptance,
  branch-assignment, coherence or keyword rule is revised.
- **Effective event:** The first coherent Git commit containing the revision,
  reconciled consumers, verification and authorized locks. Locate that commit
  through ROOT-DR-001's Git history; do not invent its hash before committing.
- **Compatibility and migration:** Prospective explicit project adoption with
  recorded governing commit, actual baseline, authority and impact assessment.
  Preserve earlier governing revisions and historical records. Existing root
  installations retain their paths. Installation or synchronization alone
  adopts nothing, moves no files, reopens no work and establishes no compliance,
  initiative acceptance, lifecycle completion or release. See the
  [adoption guide](../../../docs/guides/project-root-installation-migration.md).
- **Predecessor relationship:** Supersedes only the former requirement that
  every project itself be a Git repository root and its directly contradictory
  root/path consumers. Git preserves that predecessor at revision
  `fc0c8e3ea01471d3a35f06a29d96f837070afd70`; all other rules remain binding.

## Documentary sources

Use specification 02's
[canonical template rules](02_Codex_Initiative_Governance_Specification.md#canonical-template-selection-and-use)
and specification 08's
[preceding preparation procedure](08_Codex_Initiative_Workflow_Specification.md#documentary-prerequisite-preparation)
for records required by this specification. The
[coverage map](../../../template/TEMPLATE-COVERAGE.md) identifies reusable file
and embedded-section sources, their destinations, owners, and conditional
triggers. Documentary recovery does not supply missing authority, identity,
decisions, work, verification, or legal lifecycle events; this specification's
substantive requirements remain binding.

## Version-scope hierarchy and execution placement

The [scope specification](09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
governs prospective adoption, identity, provenance and routing. Each scope has
one integration branch named by its exact scope token. Capture the actual base
tip before creation and retain that immutable evidence afterward.

| Branch | Creation parent and integration target |
|---|---|
| Major `vN` | Captured project integration base |
| Minor `vN.M` | Matching major `vN` |
| Patch `vN.M.P` | Matching minor `vN.M` |
| Dedicated initiative | Assigned scope branch |

Thus `v1.0` and `v1.1` are siblings from `v1`; `v2.0` and `v2.1` are siblings
from `v2`; `v1.0.1` and `v2.1.1` originate from their respective minors.
An earlier minor is never the creation parent of a later minor. Numeric order,
later parent updates or sibling integration cannot rewrite creation evidence.

The LLM chooses and records dedicated or shared execution based on scope,
dependencies, existing work and integration risk. Default dedicated names are
`initiative/<scope>-<initiative-id-and-slug>`. A new initiative may instead be
registered directly on the existing matching scope branch. It retains all
independent records and one active execution assignment per revision cycle.
A dedicated branch contains only its bounded initiative, required verification
and tracking; never silently convert another initiative's exclusive branch
into a shared container. Scope branches may directly host multiple initiatives
and aggregate dedicated members and closed child scopes.

Preflight identity uniqueness, actual branch roles, open scope state, parent
existence, clean worktree and reciprocal records. Explicitly prepare missing
ancestors major-to-minor-to-patch with their own records; reuse existing
parents. Reject wrong parents, wrong-major/patch mapping, cycles, conflicting
branch roles and undeclared sharing. Later stages stop on an assignment or
captured-base mismatch rather than inferring a repair.

Shared branches require initiative-specific paths, commits, revision bases,
delivery/verification evidence and any unavoidable mixed-change boundary.
Serialize writes sharing a worktree or records. Refresh indexes before
updating so concurrent member additions survive; never replace another
member's row from an older snapshot. Presence on a scope branch does not
accept or qualify any work for upward integration.

Active work requires its assigned local ref. Preserve historical assignments,
bases, continuation refs and revision cycles. An historical ref may be absent
only with separately authorized removal evidence linked in the canonical row
and initiative history; do not reuse an historical dedicated name for unrelated
work. Source retention is the default after integration.

## Worktree, commits and history safety

Before branch creation/switching, rebasing, finalization, integration or shared
tracking changes, inspect staged, unstaged and untracked work. Never discard,
overwrite, stash, move, absorb or commit unrelated work. Branch creation needs
a clean worktree and read-only preflight. Stage only traceable changes and
account for every changed path. Coherent commits name the initiative outcome
or workflow event. Record actual identifiers after creation; do not invent
future commits or create empty commits to satisfy a field.

Do not rewrite shared history, force-push, remove refs, release or deploy
without their separate explicit authority. Local closure authority below does
not authorize pushes or any remote action. Preserve general remote-operation
safeguards and historical PR evidence.

## Closure authority and merge direction

Merge down means integration of a closed child into its recorded immediate
parent, bottom-up:

```text
initiative branch -> assigned version-scope branch
patch branch      -> matching minor branch
minor branch      -> matching major branch
major branch      -> captured project integration base
```

A human instruction to close/finalize an identified governed initiative or
scope under the adopted workflow authorizes its local child-to-recorded-parent
merge once every required gate passes. Capture the actual instruction and
exact source/target in the closure record before acting. Do not ask the human
to repeat sufficient authority. Implementation instructions, a terminal status
or protocol adoption alone do not authorize live integration. Parent closure
and further upward merges require their own satisfied closure scope.

An initiative hosted directly on its scope branch is already present there.
Record exact verified commits and direct placement; do not create a self-merge
or merge the scope upward on that member's closure. Closing a member does not
close its scope; closing a patch does not close its minor; closing a minor
does not close its major. Open siblings remain open.

## Separate scope closure

Scope closure is distinct from initiative lifecycle and is not another
initiative type. Before closure, capture complete member and child inventories,
including descendants. Every member and descendant must be closed with a
truthful disposition, all required child integration must have succeeded,
aggregate verification must pass, and coherence/conflicts must be reconciled.
No in-scope work may silently disappear. Every completed accepted deliverable
must be integrated into the scope or carry explicitly authorized exclusion or
transfer preserving ownership and the exact closure claim. Pending or blocked
required integration blocks scope closure. Empty scopes require explicit
no-work disposition. Preserve the closure snapshot and authority.

New membership in a closed scope, or integration into an already closed
parent, requires recorded reopening under specification 09's bounded intake
delegation or separate human authority. A reopened child does not silently
reopen or re-close ancestors. Preserve previous snapshots and merge evidence;
new deltas need fresh completion and integration evidence at each ancestor.

`Cancelled` and `Superseded` are closed but do not automatically integrate
abandoned or unaccepted implementation. Record retained, excluded or transferred
work and authority. With no accepted deliverable, explicit no-deliverable
closure may occur without integration; retain history and report no merge.

## Integration safety and evidence

Inspect both tips and the worktree, verify the source diff against its accepted
claim and the current target, preserve unrelated work, and run applicable
checks before integration. Record actual source/target tips, target ref,
authority, method, resulting commit and post-integration verification.
A fast-forward or already-integrated result must be reported as such; never
invent a merge commit. Reruns detect integrated commits and avoid duplicate
work. Parent-tip drift requires current comparison and checks rather than
reuse of stale evidence.

Never merge a shared branch's whole tip if it includes unfinished, unaccepted,
cancelled or unrelated work. Block integration until all included changes
qualify or separately recorded safe isolation/transfer preserves every
initiative's ownership and evidence. Closing one member does not authorize
cherry-picking, reverting, discarding or qualifying another member's changes.

Lifecycle closure and integration status are separate. Conflict, changed
target, unavailable ref or failed checks preserve truthful completion but leave
integration pending or blocked with actual failure evidence. Resolve only
within accepted scope; substantive changes use revision/reopening or successor
policy and renewed human acceptance where required. A prior merge cannot
certify a reopened cycle's new delta or bypass ancestor integration.

## Finalization and human-managed pull requests

Stage 13 verifies a truthful completed initiative, reconciles its bounded diff,
completion/coherence evidence, lifecycle, type-specific delivery records and
tracking, and finalizes traceable commits. With captured closure authority it
integrates a dedicated member into its assigned scope, or records verified
direct scope placement. Scope closure is a separate operation.

Pull requests are independently human managed. Operational workflow prompts
must not solicit, prepare, create or require one, generate its title/body,
request a PR URL, call hosting PR commands, or make local closure/integration
depend on a PR. A remote policy requiring one is a reported external constraint,
not authority to bypass policy or create a PR. Pushes require separate
authorization; branch deletion, deployment and release remain separate acts.
