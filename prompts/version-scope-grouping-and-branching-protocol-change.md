# Group initiatives by realization version scope and integrate closed branches

Implement one bounded TADp protocol revision: group initiatives by the version
scope of their originating realization notes, allow several initiatives in
one version scope, establish major/minor/patch integration branches, and merge
closed work into its recorded parent. Remove pull-request prompting from the
governed workflow; the human decides when to open a pull request.

Work in the current TADp repository. Read the repository-root `AGENTS.md`,
`protocol/AGENTS.md`, `prompts/AGENTS.md`, and the authoritative LLM suite,
beginning with its index. Apply specification 11's operative/inert boundaries,
effective-settings ledger, and list scheduling. No keyword or example in a
referenced source becomes an operative directive through this prompt.

This is a repository-maintenance prompt. Creating, reading, or reviewing it
does not execute it. Perform the changes below only when the human explicitly
instructs execution. Verify the protocol pass before synchronizing its
corresponding paths into `example/`, as required by `prompts/AGENTS.md`.

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
4. Replace the requirement that each split or successor necessarily allocates
   a different version and source suite. It must still allocate a new
   initiative identity and dedicated branch, with its own complete records;
   it may share an appropriate open version scope and source material.
5. Extend specification 05's branch model and specification 08's preparation
   and finalization contracts for the hierarchy and closure integration below.
6. Remove instructions to solicit, prepare, create, or require pull requests
   from operational prompts and their workflow consumers. Pull requests are
   human-managed and are not a prerequisite or output of these stages.

The authorized protected changes are the corresponding portions of
specifications 01 through 10 and the suite index under
`protocol/evidence/authoritative/LLM/`, the necessarily affected reusable
sources under `protocol/template/`, their downstream mirrors, and their
affected integrity locks after coherent verification. Reconcile directly
affected entry points, validators, tests, guidance, and adoption records.
Specification 11 remains the governing keyword contract; do not revise its
registry or directive semantics for this change.

Preserve evidence precedence, narrow initiative scope, type-specific output
boundaries, ordinary acceptance and completion requirements, human decision
receipts, explicit reopening, completion feedback, and immutable historical
claims. Record the revision's authority, reason, affected clauses, effective
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
delivery records, completion evidence, and dedicated branch.

Use these relationships as the new normative model:

```text
version scope -> source realization catalog -> zero or more initiatives
initiative -> exactly one version scope
initiative -> one or more precisely identified originating realization notes
realization note -> zero or more originating initiatives in its recorded scope
version scope -> exactly one integration branch
initiative -> exactly one dedicated initiative branch
```

Zero initiatives is valid for a registered scope or note awaiting decomposition;
it grants no delivery authority. Every allocated initiative must have complete
reciprocal membership and provenance records before preparation can finish.

The source note's recorded version scope determines the initiative's group.
For example, two independently scoped initiatives derived from a `v1.0`
realization note both belong to `v1.0`; creating the second does not allocate
`v1.1`. Several notes recorded under `v1.0` may contribute to either member.
Supporting evidence from another scope may be cited without changing its
identity or automatically making it an originating note.

Determine provenance from explicit source records, not filenames, directory
similarity, inferred numbering, or the existence of a branch. If originating
notes have incompatible scope assignments, record the exact ambiguity and
obtain a human disposition before allocation. Preserve the original notes;
use a linked new realization or explicit mapping when changed intent requires
a different scope.

The realization catalog and its notes remain non-authoritative proposal input.
Shared source material does not permit sharing an initiative's acceptance,
implementation, or completion evidence. Relax the existing suite-level
single-outcome restriction only enough to catalog source material for multiple
narrow initiatives within one declared scope. Apply the initiative cohesion
and mandatory-split tests to each resulting initiative.

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
path, exact scope, originating suite/note IDs and paths, dedicated branch,
captured scope-branch base and immutable commit, integration target,
predecessor/successor links, lifecycle evidence, and integration evidence.
Scope and branch identities are immutable and never recycled. Reusing a scope
across members is valid; duplicating an initiative identity or its branch is
not. Preserve recorded identity even after separately authorized ref removal.

## Branch hierarchy

Discover the project's actual integration base from Git and its recorded
configuration; do not assume `main`, `master`, a remote, or a hosting service.
Use exact scope tokens as version branch names and, by default, use
`initiative/<scope>-<initiative-id-and-slug>` for dedicated member branches.

Every major branch is created from the captured project integration base.
Every minor branch is created directly from its matching major branch.
Every patch branch is created directly from its matching minor branch.
Every initiative branch is created from its assigned version-scope branch.
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
records. Detect wrong parents, cycles, wrong-major mappings, and duplicate
branch ownership. Existing parents are reused rather than recreated.

Scope branches are explicitly permitted to aggregate their members and
closed child scopes. Initiative branches remain limited to their one bounded
initiative plus required verification and tracking. Shared membership updates
must preserve concurrent additions; no branch may overwrite another member's
row with an older index snapshot.

## Closure and merge-down contract

Define **merge down** as integration of the closed child branch into its
recorded immediate parent, in this direction:

```text
initiative branch -> assigned version-scope branch
patch branch      -> matching minor branch
minor branch      -> matching major branch
major branch      -> captured project integration base
```

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
snapshot and its authority. New membership in a closed scope requires explicit
human reopening or a new scope; closure never silently reopens ancestors.
Integration into an already closed parent scope also requires its explicit
human reopening, including when a previously integrated child is reopened.

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

Keep lifecycle closure and Git integration status separate. A conflict,
changed target, unavailable ref, or failed check leaves integration pending or
blocked with the actual failure preserved. It does not fabricate a successful
merge or erase prior completion. Resolve conflicts only within accepted scope;
route substantive changes through alignment, acceptance, and successor rules.
Reruns must detect already integrated source commits and avoid duplicate work.

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
preflight/register the scope and ancestors when needed, prepare the scope
branch, then allocate each narrow initiative and its branch as an independently
traceable preparation unit. Reusing a scope or realization must not fail the
old bijection check. Later stages verify membership, provenance, branch, and
captured base without inferring repairs.

Update Stage 13 to verify completed work, finalize traceable commits, and
perform authorized initiative-to-scope integration under the new contract.
Provide a distinct scope-closure operation for patch/minor/major integration;
it must not pose as another initiative type or implicitly close ancestors.
Preserve explicit dispositions for cancelled or superseded work outside the
completed-initiative finalization entry contract.

Reconcile affected specifications, entry points, realization guidance and
templates, initiative/preparation templates, project profile and indexes,
status views, scope registry/README sources, workflow prompts and contracts,
handoffs, recovery rules, validation, regression fixtures, and documentation.
Check both hardcoded type-root assumptions and old bijection/successor checks.
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
compatible revision and a complete ledger disposition. Substantive successor
work still needs a new initiative and branch; it may join a suitable open scope
without claiming the predecessor's acceptance or completion.

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
4. Synchronize every corresponding protocol-owned path into `example/` and
   verify mirrors, locks, and parity. Leave example-specific initiatives and
   evidence unchanged; report their actual migration needs.
5. Run the repository-defined protected-source checks, validator, relevant
   regression suite, Markdown link checks, and final diff/whitespace review.
   Obtain independent review of this revision and reconcile its findings.
   Record exact commands, results, and remaining limitations.

The required verification-case inventory is:

- Two initiatives from one `v1.0` note are both grouped under `v1.0`, with
  distinct identities, branches, lifecycle records, and acceptance evidence.
- Several notes in one scope and mixed initiative types retain exact provenance
  and type boundaries; unresolved cross-scope origins block allocation.
- Major, minor, and patch syntax is valid, numeric ordering puts `v1.10` after
  `v1.9`, and malformed or noncanonical tokens fail.
- `v1.0` and `v1.1` branch from `v1`; `v2.0` and `v2.1` branch from `v2`;
  `v1.0.1` and `v2.1.1` branch from their matching minors.
- Minor-from-minor, wrong-major, wrong-patch-parent, cyclic, orphan, duplicate
  ownership, and missing reciprocal mappings fail with useful findings.
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
  integrity, evidence standing, human gates, coherence reviews, and substantive
  successor requirements remain preserved.

## Completion report

Report the final cardinality, directory grouping, provenance model, exact
branch topology, merge direction, closure and integration meanings, authority
boundary, and human-managed PR behavior. List the exact changed protocol paths,
example mirrors, and intentionally unmirrored repository support. Include the
revision/adoption records, verification and independent-review results, lock
changes, unresolved conflicts, migration needs, and remaining human decisions.
Claim only the protocol work actually performed and verified.
