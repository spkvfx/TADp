# Group initiatives by realization version scope and integrate closed branches

Implement one bounded TADp protocol revision: group initiatives by the version
scope of their originating realization notes, allow several initiatives in
one version scope, establish major/minor/patch integration branches, and merge
closed work into its recorded parent. Let the LLM route new realizations into
existing initiatives or branches, including append, revision, and reopening,
and reconcile the consequences. Remove pull-request prompting from the
governed workflow; the human decides when to open a pull request.

Work in the current TADp repository. Read the repository-root `AGENTS.md`,
`protocol/AGENTS.md`, `prompts/AGENTS.md`, and the authoritative LLM suite,
beginning with its index. Apply specification 11's operative/inert boundaries,
effective-settings ledger, and list scheduling. No keyword or example in a
referenced source becomes an operative directive through this prompt.

This is a repository-maintenance prompt. Creating, reading, or reviewing it
does not execute it. Perform the changes below only when the human explicitly
instructs execution. Verify the protocol pass before synchronizing its
corresponding paths into `../_old/example/`, as required by `prompts/AGENTS.md`.

## Exact revision authority and boundaries

Execution of this prompt authorizes the following precise replacements of the
current invariant model:

1. Replace specification 09's one-to-one work-version, realization-suite,
   initiative, and branch correlation with a shared version-scope grouping.
   Each initiative belongs to exactly one version scope; a scope may contain
   multiple independently acceptable initiatives.
2. Permit major (`vN`), minor (`vN.M`), and patch (`vN.M.P`) scopes. Preserve
   project-local immutable scope identity while allocating initiative IDs
   independently of shared version tokens.
3. Permit realization notes and their suite to originate multiple narrow
   initiatives in the same scope. Preserve exact note provenance, evidence
   standing, and initiative-local specifications and acceptance claims.
4. Replace the requirement that every substantive revision necessarily creates
   a successor tuple. The LLM may revise or reopen an existing initiative when
   the resulting claim remains one coherent, narrowly bounded outcome. A new
   independent outcome, mandatory split, or incompatible type/owner/authority
   boundary still requires a separate initiative with complete records. New
   initiatives and successors may share a version scope and source material.
5. Extend specification 05's branch model and specification 08's preparation
   and finalization contracts for the hierarchy and closure integration below.
6. Remove instructions to solicit, prepare, create, or require pull requests
   from operational prompts and their workflow consumers. Pull requests are
   human-managed and are not a prerequisite or output of these stages.
7. Replace per-target human confirmation for realization placement and
   reopening with the bounded LLM decision method below. This specifically
   revises the reopening and successor clauses in specifications 02, 04, 07,
   08, 09, and 10 and their necessary references. Preserve prior claims and
   actual decision authorship; initiative acceptance remains a human gate.
8. Replace mandatory exclusive initiative-branch ownership with recorded
   execution placement: a new initiative may use an existing version-scope
   branch directly or a dedicated child branch, as chosen by the LLM. Shared
   scope branches require per-initiative change and verification traceability.

The authorized protected changes are the corresponding portions of
specifications 01 through 10 and the suite index under
`protocol/evidence/authoritative/LLM/`, the necessarily affected reusable
sources under `protocol/template/`, their downstream mirrors, and their
affected integrity locks after coherent verification. Reconcile directly
affected entry points, validators, tests, guidance, and adoption records.
Specification 11 remains the governing keyword contract. Reconcile only its
necessarily affected reopening/successor cross-references to the exact
delegation and revision policy adopted here; do not revise its registry or
directive semantics, or introduce a blanket gate waiver.

Preserve evidence precedence, narrow initiative scope, type-specific output
boundaries, ordinary acceptance and completion requirements, human decision
receipts, recorded reopening under the stated authority, completion feedback,
and immutable historical claims. Record the revision's authority, reason,
affected clauses, effective
event, compatibility, and successor relationship. Retain earlier revisions
through Git and linked migration records.

This execution changes the protocol and its distribution mirror. It does not
create or migrate live project initiatives, close live scopes, merge live
branches, push, open pull requests, release, deploy, rewrite shared history,
or remove branches. Self-contained test repositories may exercise the new
branching and merge behavior. Existing historical prompts and receipts remain
historical evidence rather than being rewritten to imply the new rule always
applied.

## Version scopes and realization provenance

A version scope is a coordination and integration container. It is not an
umbrella initiative, an accepted specification, a release, or a collective
acceptance claim. It may hold several narrow initiatives of different types;
each retains its own owner, gates, decisions, lifecycle, permitted outputs,
delivery records, completion evidence, and recorded execution placement.

Use these relationships as the new normative model:

```text
version scope -> source realization catalog -> zero or more initiatives
initiative -> exactly one version scope
initiative -> one or more precisely identified originating realization notes
realization note -> zero or more new or existing initiative targets
version scope -> exactly one integration branch
initiative -> one recorded active execution branch per revision cycle
scope branch -> zero or more directly hosted initiatives
```

Zero initiatives is valid for a registered scope or note awaiting decomposition;
it grants no delivery authority. Every allocated initiative must have complete
reciprocal membership and provenance records before preparation can finish.

The source note's recorded version scope is the default placement for new
initiatives. For example, two independently scoped initiatives derived from a
`v1.0` realization note normally both belong to `v1.0`; creating the second
does not allocate `v1.1`. The LLM may instead target a suitable existing
initiative or scope when its recorded fit assessment supports that choice.
An existing initiative retains its identity and scope when receiving a new
realization; do not relocate it merely to match the new note's version.

Determine provenance from explicit source records, not filenames, directory
similarity, inferred numbering, or the existence of a branch. Record source
scope and selected target scope separately, including cross-scope mappings,
rationale, and compatibility effects. The LLM resolves placement differences
under the delegated method below; seek human input only when evidence cannot
support a coherent choice or an unexcepted authority boundary is crossed.
Preserve original notes and their identities rather than relabeling them to
make the selected placement appear automatic.

The realization catalog and its notes remain non-authoritative proposal input.
Shared source material does not permit sharing an initiative's acceptance,
implementation, or completion evidence. Relax the existing suite-level
single-outcome restriction only enough to catalog source material for multiple
narrow initiatives within one declared scope. Apply the initiative cohesion
and mandatory-split tests to each resulting initiative.

## LLM realization routing, revision, and reopening

When a human requests processing of an identified realization under this
adopted workflow, that request delegates placement, append/revision selection,
and necessary initiative/scope reopening decisions to the LLM for that intake.
The realization's contents alone do not grant authority. The LLM inventories
existing open and closed initiatives, branches, accepted claims, source links,
dependencies, partial effort, and conflicts before choosing the best fit.
Do not require a fresh human choice solely because the selected target is
existing, closed, or belongs to a different version scope.

Use this decision inventory, not an action list:

| Fit | Permitted disposition |
|---|---|
| Adds evidence or detail without changing the claim | Append to the existing initiative; preserve prior evidence and lifecycle standing |
| Revises the same coherent narrow outcome | Revise the existing initiative through alignment and renewed acceptance when the accepted claim changes |
| Changes a closed initiative's claim | Record reopening first, then revise the existing initiative |
| Introduces an independently acceptable outcome | Create a separate initiative in the best-fitting existing scope/branch, or prepare a new scope when needed |
| Cannot coexist with a target's type, ownership, or authority boundary | Split or use a successor; record conflicts and preserve continuing ownership |

This applies to `Proposed`, `Accepted`, `In progress`, `Completed`, `Cancelled`,
and `Superseded` targets. A closed claim must not be edited substantively while
remaining closed. Reopening returns it to `Proposed`; only a separately
recorded human unchanged-claim decision permits direct return to `Accepted`.
Before revising an accepted or in-progress normative claim, pause affected
delivery, preserve partial-work evidence, and record the return to `Proposed`.
The changed claim then passes alignment and renewed human acceptance before
delivery resumes. A historical addendum that preserves the exact closed
claim may remain append-only without reopening. Do not turn independent
outcomes into an umbrella initiative to avoid a split.

Before applying each routing/reopening disposition, record the actual human
intake instruction and governing delegation, source realization, candidate
targets, chosen initiative/scope/branch, rejected alternatives, rationale,
prior state and exact claim revision, change boundary, risks, compatibility,
and affected records. Attribute the choice and reopening to the LLM acting
under delegated authority, not to a fabricated per-target human response.
Reconcile decision-receipt and specification 11 exception records where their
governing clauses require them. This delegation is limited to intake placement,
specification revision, and necessary reopening; it does not automatically
answer unrelated questions, accept changed claims, authorize product delivery,
or pass verification and completion gates.

The LLM must address consequences across source mapping, assumptions and
decisions, architecture, scope assessment, dependencies, roadmap, steps,
verification, products' compatibility obligations, membership, status, and
work-conflict records. Preserve prior accepted/completed baselines, receipts,
closure snapshots, and integration evidence as historical revisions. Handle
reopening a superseded initiative's relationship with its replacement
explicitly; do not assign the same claim to competing owners silently.

Reopen affected closed scopes or ancestors under the same bounded delegation
when required to admit work or integrate its later result. Record each event
and the resulting pending integration; reopening a child does not silently
reopen or re-close its ancestors. Previously integrated commits stay historical
evidence. New changes require fresh completion and integration evidence, and
further merges still follow the closure-authorization contract below.

## Canonical identifiers, grouping, and records

Accept exactly these version-scope forms:

| Kind | Syntax | Structural parent |
|---|---|---|
| Major | `v<major>` | Project's captured integration base |
| Minor | `v<major>.<minor>` | Matching major scope |
| Patch | `v<major>.<minor>.<patch>` | Matching minor scope |

Components are non-negative decimal integers with no leading zero except
`0`; compare them numerically. Reject signs, whitespace, missing components,
extra components, prerelease labels, and build metadata. Distinguish `v1`
from `v1.0` and `v1.0` from `v1.0.0`; do not normalize them into one identity.
These are work scopes, separate from package, contract, and release versions.
Their numbers confer no authority, compatibility, or release claim.

For newly governed work, group initiative directories physically as:

```text
initiatives/
  version-scopes.md
  initiative-index.md
  v1.0/
    README.md
    implementation/<initiative-id-and-slug>/
    design/<initiative-id-and-slug>/
    planning/<initiative-id-and-slug>/
  v1.1/
    README.md
  v2.1.1/
    README.md
```

The type directories retain the existing type-specific suites. Use the same
layout for major scopes when they directly own initiatives. Shared project
indexes, migration ledgers, and `work-conflicts.md` stay project-level.
Version grouping must not change ownership of any initiative-local record.

Make `initiatives/version-scopes.md` the canonical scope registry, and retain
`initiatives/initiative-index.md` as the canonical membership/correlation
index with one row per initiative. Scope READMEs and status views link to
these owners instead of creating competing lifecycle authority. Each
initiative README remains its lifecycle authority.

The scope registry must preserve the exact scope ID, kind, structural parent,
integration branch, captured creation base ref and commit, integration target,
source suite/note catalog, member and child-scope links, closure disposition,
integration state, closure evidence, merge evidence, and governing revision.

Each initiative row and its reciprocal records must preserve its ID, type and
path, exact scope, originating and later contributing suite/note IDs and paths,
per-source routing disposition, assigned execution branch and dedicated/shared
mode, captured base and immutable commit, integration target, current revision
cycle, predecessor/successor links, lifecycle evidence, and integration evidence.
Preserve allocation and branch history rather than overwriting it on reopening.
An initiative has one active execution assignment per cycle; record continuation
branches when a retained or removed historical ref cannot safely host new work.
Reusing a scope or a declared shared scope branch is valid; duplicating an
initiative identity or reassigning a historical branch name to unrelated work
is not. Preserve identity after separately authorized ref removal.

## Branch hierarchy

Discover the project's actual integration base from Git and its recorded
configuration; do not assume `main`, `master`, a remote, or a hosting service.
Use exact scope tokens as version branch names and, by default, use
`initiative/<scope>-<initiative-id-and-slug>` for dedicated member branches.

Every major branch is created from the captured project integration base.
Every minor branch is created directly from its matching major branch.
Every patch branch is created directly from its matching minor branch.
When a dedicated initiative branch is chosen, create it from its assigned
version-scope branch. Alternatively, register the new initiative directly on
an existing matching scope branch without requiring another branch. The LLM
chooses and records the best placement based on scope, dependencies, existing
work, and integration risk. Preserve the major/minor/patch parent topology.
Capture the actual base tip before creation and preserve it afterward.

The required topology is illustrated here; arrows mean branch creation:

```text
<project integration base>
  -> v1
       -> v1.0
            -> v1.0.1
            -> initiative/v1.0-<initiative-A>
            -> initiative/v1.0-<initiative-B>
       -> v1.1
  -> v2
       -> v2.0
       -> v2.1
            -> v2.1.1
```

The human clarified that `v2.0` and `v2.1` are siblings under `v2`; a
derivative scope from `v2.1` is `v2.1.1`. An earlier minor is not the creation
parent of the next minor. Sibling integration, a later parent update, or
numeric ordering must not silently rewrite the captured creation base.

Preflight parent existence, open scope state, identity uniqueness, a clean
worktree, and reciprocal records before branch creation. Missing ancestors
must be prepared explicitly in major-to-minor-to-patch order with their own
records. Detect wrong parents, cycles, wrong-major mappings, conflicting branch
roles, and undeclared branch sharing. Existing parents are reused rather than
recreated.

Scope branches are explicitly permitted to host multiple initiatives directly
and aggregate dedicated member branches and closed child scopes. Dedicated
initiative branches remain limited to their one bounded initiative plus
required verification and tracking. Before reusing an existing branch, inspect
its recorded role and work; do not silently convert another initiative's
exclusive branch into a shared container. Choose its matching scope branch
or a dedicated child when shared use would violate existing ownership.

On shared branches, record initiative-specific paths, commits, revision bases,
delivery and verification evidence, and any unavoidable mixed-change boundary.
Serialize writes that share a worktree or records, and preserve unrelated and
unaccepted work. Shared membership updates must preserve concurrent additions;
no branch may overwrite another member's row with an older index snapshot.

## Closure and merge-down contract

Define **merge down** as integration of the closed child branch into its
recorded immediate parent, in this direction:

```text
initiative branch -> assigned version-scope branch
patch branch      -> matching minor branch
minor branch      -> matching major branch
major branch      -> captured project integration base
```

An initiative hosted directly on its scope branch is already present there;
record this fact and its exact verified commits instead of creating a self-merge
or merging the scope upward on that initiative's closure. Work present on a
shared branch is not automatically accepted or qualified for upward integration.

Integrate bottom-up. Closing one initiative does not close its scope, closing
a patch does not close its minor, and closing a minor does not close its major.
Do not merge a scope upward merely because one member has completed.

Define scope closure separately from initiative lifecycle. A scope may close
only after its membership and child-scope inventory are captured, every
member and descendant is closed with a truthful disposition, required child
integration has succeeded, aggregate verification passes, coherence and
conflict checks are reconciled, and no in-scope work is silently omitted.
Every completed member or child scope with accepted deliverables must already
be integrated into this scope, or carry an explicitly authorized exclusion or
transfer that preserves ownership and the exact closure claim. A pending or
blocked required integration blocks scope closure.
An empty scope needs an explicit no-work disposition. Preserve the closure
snapshot and its authority. New membership in a closed scope requires recorded
reopening under the intake delegation or separate human authority, or a new
scope; closure never silently reopens ancestors. Integration into an already
closed parent scope also requires its recorded reopening under the applicable
authority, including when a previously integrated child is reopened.

Successful completed work is merged into its recorded parent after closure
gates pass. `Cancelled` and `Superseded` are also closed lifecycle states but
must not automatically integrate abandoned or unaccepted implementation.
Record what is retained, excluded, or transferred and its authority. A branch
with no accepted deliverable may close without integration under an explicit
no-deliverable disposition; retain its history and report that no merge occurred.

Adopt this narrowly bounded merge-authorization rule: a human instruction to
close/finalize an identified governed initiative or scope under the new
workflow authorizes its local child-to-recorded-parent merge once every
required gate passes. Capture that instruction and the exact source/target
in the closure record before acting; do not ask the human to repeat sufficient
authority. Ordinary implementation, a terminal status field, or adoption of
this protocol revision alone is not authority to merge live work. Parent
closure and further upward merges require their own satisfied closure scope.

Every integration must inspect both branch tips and the worktree, preserve
unrelated work, verify the source diff and current target, run applicable
checks, and record actual source/target tips, target ref, authority, method,
resulting commit, and post-integration verification. A fast-forward or already
integrated result may be recorded truthfully; do not invent a merge commit.
Retain source branches unless deletion is separately authorized.

Never merge a shared branch's whole tip if that would carry unfinished,
unaccepted, cancelled, or unrelated work into its parent. Keep the merge
blocked until all included changes qualify or a separately recorded safe
isolation/transfer preserves every initiative's ownership and evidence.
Closing one hosted initiative does not authorize cherry-picking, reverting,
discarding, or qualifying other initiatives' changes.

Keep lifecycle closure and Git integration status separate. A conflict,
changed target, unavailable ref, or failed check leaves integration pending or
blocked with the actual failure preserved. It does not fabricate a successful
merge or erase prior completion. Resolve conflicts only within accepted scope;
route substantive changes through the revision/reopening or successor policy
above and human acceptance where required. Reruns must detect already integrated
source commits and avoid duplicate work. A reopened revision is evaluated on
its new commit delta and current gates; a prior merge receipt cannot certify
the new changes or bypass required ancestor integration.

## Human-managed pull requests

Remove pull-request actions, questions, placeholders, required URLs, handoff
instructions, examples, and completion criteria from active workflow prompts,
especially Stage 13 finalization. Reconcile their shared contract, template
README, developer guidance, tests, and the smallest necessary authoritative
clauses so they no longer require or imply a pull request.

Do not ask whether to open a pull request, generate PR titles/bodies, create
drafts, use hosting-service PR commands, or make closure or local integration
depend on a PR. The human independently decides when and how to open one.
Preserve historical PR evidence and general safeguards for remote operations.
Pushes remain separately authorized and are not implied by local merge
authority. A remote policy requiring a PR is a reported external constraint;
do not bypass it or automatically create a PR to satisfy it.

## Workflow, migration, and consumer reconciliation

Keep stages 0 through 13 and the three delivery paths. Revise Stage 0 to
perform realization-fit assessment before allocation, preflight/register the
chosen scope and ancestors when needed, and record either the existing-target
revision/reopening or the new initiative with its chosen execution assignment.
Prepare a new branch only when the recorded placement requires one. Each
disposition remains independently traceable. Reusing a scope, realization, or
declared shared branch must not fail the old bijection check. Later stages
verify membership, provenance, active revision, branch assignment, and captured
base without inferring repairs. Existing complete initiatives reuse their
records rather than being recreated by the new-initiative stages.

Update Stage 13 to verify completed work, finalize traceable commits, and
perform authorized initiative-to-scope integration or record verified direct
scope-branch placement under the new contract.
Provide a distinct scope-closure operation for patch/minor/major integration;
it must not pose as another initiative type or implicitly close ancestors.
Preserve explicit dispositions for cancelled or superseded work outside the
completed-initiative finalization entry contract.

Reconcile affected specifications, entry points, realization guidance and
templates, initiative/preparation templates, project profile and indexes,
status views, scope registry/README sources, workflow prompts and contracts,
handoffs, recovery rules, validation, regression fixtures, and documentation.
Check hardcoded type-root assumptions, old bijection/exclusive-branch checks,
human-only per-target reopening checks, and mandatory-successor checks.
Keep historical repository prompts as historical sources; do not edit their
recorded instructions into retroactive authority for this revision.

Define a prospective effective event and an adoption/migration ledger. Retain
legacy version, suite, initiative, branch, path, and governing revision;
record proposed scope membership, source evidence, action, authority, blockers,
and re-entry conditions. Existing one-to-one tuples may map into shared scopes
only through explicit, evidence-backed migration. Moving existing initiative
paths, changing provenance, or reparenting branches is not a notation repair.
Preserve old links through mappings and historical references.

Do not rename a legacy `v1.0` to `v1`, or reinterpret bare `v1` as `v1.0`.
Do not move closed initiatives or rewrite accepted claims as part of generic
distribution synchronization. Leave unmigrated projects under their recorded
compatible revision and a complete ledger disposition. After explicit adoption,
the intake method may choose a same-initiative revision or a separate successor
with recorded execution placement; neither can claim new acceptance or
completion from the predecessor's evidence.

## Execution order and verification

The following is a serial action list. Other lists and tables above describe
requirements, relationships, or examples rather than independent action jobs.

1. Inspect Git and record the initial branch, base commit, worktree changes,
   affected-source inventory, and protected-source check results. Preserve
   unrelated work and pre-existing drift. Capture the execution instruction
   in a decision receipt and document the exact superseded invariant clauses.
2. Implement and reconcile the authorized protocol surfaces and repository
   support. Use protocol-owned fixtures, not project-specific evidence, to
   design and test the new rules.
3. Verify the protocol change, including semantic review and focused regression
   tests, before starting example synchronization. Use the configured project
   Python environment for any Python checks. Do not refresh locks to conceal
   unexplained drift; refresh only authorized coherent sources after their
   substantive verification, then rerun integrity and structural checks.
4. Synchronize every corresponding protocol-owned path into `../_old/example/` and
   verify mirrors, locks, and parity. Leave example-specific initiatives and
   evidence unchanged; report their actual migration needs.
5. Run the repository-defined protected-source checks, validator, relevant
   regression suite, Markdown link checks, and final diff/whitespace review.
   Obtain independent review of this revision and reconcile its findings.
   Record exact commands, results, and remaining limitations.

The required verification-case inventory is:

- Two initiatives from one `v1.0` note are both grouped under `v1.0`, with
  distinct identities, lifecycle records, and acceptance evidence; when
  dedicated execution is selected, each has its own branch.
- Several notes in one scope and mixed initiative types retain exact provenance
  and type boundaries. A `v2.1` realization may append compatible detail to an
  existing `v1.0` initiative while preserving both source and target scopes.
- One realization may affect several existing initiatives; each append,
  revision, reopening, or new-initiative disposition has its own fit rationale,
  exact source links, impact review, and reconciled records.
- The LLM may revise a coherent existing claim instead of forcing a successor;
  independent outcomes still split, and changed accepted claims require renewed
  human acceptance before delivery.
- Delegated reopening of `Completed`, `Cancelled`, and `Superseded` targets
  preserves prior claims and replacement consequences and returns to `Proposed`.
  No fabricated human answer, implied acceptance, or retained changed completion
  is permitted. Necessary scope/ancestor reopening is recorded per event.
- A new initiative may be assigned directly to an existing scope branch with
  independent records and per-initiative commit attribution. Its closure causes
  no self-merge and no premature upward merge of its still-open scope.
- Shared-branch writes preserve concurrent work; unaccepted or unfinished
  changes block whole-tip integration, and closed/reopened revision cycles
  require verification and integration evidence for their new deltas.
- Major, minor, and patch syntax is valid, numeric ordering puts `v1.10` after
  `v1.9`, and malformed or noncanonical tokens fail.
- `v1.0` and `v1.1` branch from `v1`; `v2.0` and `v2.1` branch from `v2`;
  `v1.0.1` and `v2.1.1` branch from their matching minors.
- Minor-from-minor, wrong-major, wrong-patch-parent, cyclic, orphan, duplicate
  initiative identity, conflicting branch roles, and missing reciprocal
  mappings fail with useful findings; declared scope-branch sharing is valid.
- Closing a member leaves open siblings and its scope open. Closing a scope
  with an open member/descendant fails. Closed-scope additions require reopening.
- Authorized completed work integrates child-to-parent in bottom-up order;
  failed merges preserve pending status and truthful completion. Cancelled or
  superseded unaccepted work is excluded with an explicit disposition.
- Already integrated reruns, parent-tip drift, shared-index updates, and
  fast-forwards retain accurate Git evidence without fabricated merge commits.
- A closure instruction supplies its bounded local merge authority once;
  missing authority, arbitrary targets, and unapproved remote operations fail.
- Finalization requires no PR URL or hosting connection, performs no PR
  commands, and never asks the human whether to create one.
- Legacy tuples, historical PR records, closed claims, protected-source
  integrity, evidence standing, unexcepted human gates, and coherence reviews
  remain preserved. Revised reopening/successor rules recognize the exact
  delegated choices without weakening acceptance or independent-outcome splits.

## Completion report

Report the final cardinality, directory grouping, provenance and LLM routing
model, delegated reopening boundary, dedicated/shared execution placement, exact
branch topology, merge direction, closure and integration meanings, authority
boundary, and human-managed PR behavior. List the exact changed protocol paths,
example mirrors, and intentionally unmirrored repository support. Include the
revision/adoption records, verification and independent-review results, lock
changes, unresolved conflicts, migration needs, and remaining human decisions.
Claim only the protocol work actually performed and verified.
