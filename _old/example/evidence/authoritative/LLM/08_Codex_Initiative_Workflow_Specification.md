# Codex initiative workflow specification

## Purpose and authority

This specification defines the required end-to-end workflow semantics for a
TADp initiative. It governs stage order, stage entry and exit evidence,
record ownership, type-specific delivery paths, acceptance, recovery, and
finalization.

Numbered prompts implement this specification for Codex. A prompt may impose a
stricter operational precondition, but it must not skip, weaken, reorder, or
expand the authority granted by this specification.

## Canonical prompt interpretation and exception route

Read and apply the canonical
[prompt keyword specification](11_Codex_Prompt_Keyword_Specification.md)
for every governed task, including tasks without a stored prompt. It owns
registered names, source-position settings, operative/inert boundaries,
action-list scheduling, preview, local access, independent review, and
specific exceptions. Compute block settings before dispatch; nested and
parallel execution, retries, and resumes retain the source block identity.
List scheduling does not renumber stages or create lifecycle facts.

All stage-entry, human-review, failure-stop, handoff, execution, and completion
clauses below state the ordinary contract. A specific exception may replace
only the exact named prerequisite or human interaction covered by actual
human authority and its receipt and exception record, created before reliance.
Do not treat a mode request as a stage-wide waiver. An automated failure still
blocks when only human-input gates are excepted; preserve all actual failure
and waiver evidence. Preview allows only response-only proposals and read-only
checks; local forbids external access; independent-review obligations attach
to actual or proposed output and survive later inverse directives. Gate modes
do not cancel these settings. Locks remain enforced.

For stages 5 and 6, an expressly authorized alternative decision method may
replace the human interaction for the named source IDs. Preserve the exact
human authorization separately from actual agent-made dispositions, method,
author, rationale, and reconciliation. Do not repeatedly solicit authority
already sufficiently recorded. Stage 7 acceptance and reopening outside
specification 09 intake delegation
remain separate specific human-authority acts; autonomous question handling
is not either act. Specification 09 separately delegates intake routing and
necessary reopening when a human requests processing an identified realization
under the adopted workflow; record each event and actual LLM authorship first.
It supplies no acceptance or delivery authority. The standard execution or
delivery record must retain
every bypassed prerequisite and actual output, without claiming an ordinary
gate passed. Stage 10, 11, or 12 completion evidence must distinguish passing,
failed, skipped, waived, and not-performed checks. No keyword itself permits
ordinary `Accepted` or `Completed` without their required actual evidence;
retain the last truthful state and report bounded prompt completion under its
exception separately. Any proposed lifecycle replacement requires the separate
specific authority and consumer reconciliation defined by specification 11.
This revision adopts no such replacement.

When gates resume, recheck current prerequisites for later work depending on
excepted output; restoration never retroactively validates an earlier skip.
Inferred switches and any further inferred invariant exception require exact
human confirmation; no switch can waive that requirement. Existing sufficient
authority remains usable only within its recorded scope. Stage ownership,
type boundaries, historical claims, and specification 09 successor rules
remain unchanged unless separately specifically authorized.

## Workflow stages and lifecycle states

A workflow stage is an activity that reads evidence and may create or reconcile
specified records. A lifecycle state is an evidence-backed standing of the
initiative. They are not interchangeable.

- Completing a stage does not automatically create a lifecycle transition.
- A lifecycle transition occurs only when its required evidence exists and the
  transition is recorded in lifecycle history.
- Re-running a stage does not recreate authority already recorded or erase a
  prior truthful state.
- A status field, branch, commit, merge, or prompt completion is not by itself
  evidence that an initiative is accepted or completed.

The lifecycle specification governs legal states and transitions. This
specification governs the activities that may produce transition evidence.

The
[version-realization-initiative correlation specification](09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
governs identity allocated or reused by Stage 0 and verified by every later
stage. Membership
allocation is preparation evidence only and does not change lifecycle standing.

## Universal workflow rules

Every stage must:

1. Identify the exact initiative, declared type, active branch, stage, and edit
   boundary before changing anything.
2. Read applicable authoritative evidence before using lower-standing evidence
   for a normative conclusion.
3. Preserve source identity, authority, revision, limitations, and unresolved
   conflicts.
4. Operate only on records and outputs owned by the stage.
5. Stop the affected work when an unexcepted entry gate fails or an unexcepted
   required human decision is missing. The specific exception route above
   never changes a failed result into passing evidence.
6. Preserve unrelated work and report every changed path and verification
   result truthfully.
7. Reconcile every record named by the stage's exit contract before handing the
   initiative to another stage.
8. For work governed by specification 09, verify exact scope membership,
   originating/contributing note provenance, active revision cycle, execution
   assignment, immutable captured base and reciprocal links before use.
9. Apply the [coherence specification](10_Codex_Initiative_Coherence_Specification.md):
   include relevant open initiative effort as work, record incompatible
   efforts, and preserve closed claims until recorded reopening under
   specification 09 delegation or separate human authority.

No stage may use urgency, a recommendation, implementation convenience, or the
existence of later work to infer an earlier gate.

## Canonical stage sequence

| Stage | Activity | Applies to | Principal output | Lifecycle effect permitted |
|---|---|---|---|---|
| 0 | Realization fit and scoped preparation | All types | Recorded routing; scope/ancestor and membership records, required execution placement, new skeleton only when allocated | Existing-target revision/reopening may return to `Proposed` under recorded authority; no acceptance |
| 1 | Proposal creation | All types | Canonical working proposal | None |
| 2 | Proposal alignment | All types | Evidence-aligned proposal with uncertainty preserved | None |
| 3 | Initiative creation | All types | Complete initial initiative suite | Remains `Proposed` |
| 4 | Initiative alignment | All types | Coherent, invariant-compatible proposed specification | Remains `Proposed` |
| 5 | Assumption confirmation | All types when unresolved assumptions exist | Decision receipts and reconciled assumption dispositions | None by itself |
| 6 | Open-question resolution | All types when active questions exist | Decision receipts and reconciled question dispositions | None by itself |
| 7 | Initiative acceptance | All types | Accepted baseline, acceptance receipt, and transition evidence | `Proposed` to `Accepted` |
| 8 | SDK/API alignment | Implementation when applicable | Compatible SDK/API product changes or explicit blocker | May remain `Accepted` or become `In progress` only when product work actually begins |
| 9 | Implementation-readiness review | Implementation | Current phase-specific entry decision | None by itself |
| 10 | Implementation execution | Implementation | Products, execution record, verification, and completion evidence | `Accepted` to `In progress`; then `Completed` when all evidence exists |
| 11 | Design delivery | Design | Delivery record, accepted specification changes, verification, and completion evidence | `Accepted` to `In progress`; then `Completed` when all evidence exists |
| 12 | Planning delivery | Planning | Delivery record, initiative-local evidence outputs, verification, and completion evidence | `Accepted` to `In progress`; then `Completed` when all evidence exists |
| 13 | Finalization | All types after completion | Traceable commits and authorized initiative-to-scope integration or verified direct scope placement | No new completion or parent closure claim |

Stages 5 and 6 are repeated until their applicable source records have explicit
human outcomes or actual agent dispositions under the specific recorded
alternative method described above. Stages 8 through 10 form the implementation path. Stage 11 is
the design path. Stage 12 is the planning path. An initiative follows exactly
one delivery path for its declared type.

## Stage entry and exit contracts

### Stage 0: realization fit and preparation

Entry requires Git, inspected actual integration configuration and worktree,
identified realization intake authority, source records, readable templates
and an inventory of open/closed candidate initiatives and branches. Perform
specification 09 fit assessment before allocation. Preserve exact source scope
and note identity separately from selected target scope.

Record each append, revision, reopening or new-initiative disposition, actual
LLM author, candidate/rejected targets, fit rationale, prior state/claim,
compatibility, risks and affected records before applying it. The human intake
instruction supplies the adopted bounded placement/reopening delegation; seek
input only for unsupported fit or an unexcepted boundary. Changed accepted or
in-progress claims pause delivery, preserve partial evidence and return to
`Proposed`. Closed targets first receive an event-specific reopening record.
Alignment and renewed human acceptance are still required before delivery.

For allocation, preflight exact canonical scope syntax, parent existence/open
state, unique initiative ID/path, branch role and assignment, clean worktree,
immutable base and reciprocal records. Reuse existing scopes, source catalogs
and declared scope branches. Prepare missing ancestors explicitly in
major-to-minor-to-patch order. Choose and record shared scope execution or a
dedicated child created from that scope, capturing actual base tip first.

Create only required new scope/ancestor records, exact source catalog/note
links, canonical membership row, reciprocal metadata and minimal initiative
and proposal-source skeleton for a new initiative. Newly governed paths are
`initiatives/<scope>/<type>/<initiative-id-and-slug>/`. A new initiative remains
`Proposed`; create no acceptance or delivery evidence. Existing complete
initiatives retain their suites rather than being recreated by stages 1 or 3.
Exit checks each independent routing disposition, reciprocal scope membership,
provenance, current cycle, assignment, base and any actual preparation commit.
### Stages 1 and 2: proposal

Proposal creation requires the prepared branch, minimal skeleton, intended
realization suite, intact canonical correlation, and canonical proposal
template. It creates only the working proposal.

Proposal alignment requires one identifiable editable proposal. It reconciles
that proposal with evidence while preserving assumptions, unresolved choices,
frozen sources, type, scope, and exclusions. Neither stage accepts the
initiative or creates product work.

### Stage 3: initiative creation

Entry requires the prepared skeleton, aligned proposal, complete current
templates, intact canonical correlation, and unambiguous registry and status
locations.

The stage creates the complete initial suite, including the scope assessment,
but no decision receipts, readiness, execution, delivery, or completion record.
Exit requires coherent IDs, evidence labels, scope, architecture, source
mapping, questions, roadmap, steps, and tracking entries in `Proposed` state.

### Stage 4: initiative alignment

Entry requires the complete initial suite. The stage re-evaluates every
material claim and split trigger against authoritative evidence and established
precedent. It may reconcile existing initiative records but must not make human
decisions, create products, or conceal a required decomposition.

Exit requires either a coherent proposed specification ready for human gates or
an explicit blocker, conflict, or decomposition requirement.

The alignment inventory includes proposed and partially performed effort in
other open initiatives. Record incompatible work in the project work-conflict
register and affected initiative records, retaining source authority and human
gates. The existence of a completed product does not erase open effort.

### Stages 5 and 6: human decision reviews

Entry requires stable source IDs, complete source text, applicable evidence,
and identified affected records. Each review presents one ready source item,
waits for an explicit human response, creates a decision receipt, and reconciles
only the records affected by that response.

A review exits only when every applicable item has a truthful human disposition
or an explicit recorded blocker or re-entry condition. These reviews make
acceptance possible; they do not perform acceptance.

### Stage 7: initiative acceptance

Acceptance is a distinct human-authority gate. Entry requires:

- a complete current initiative suite;
- a scope assessment with no undisposed mandatory split trigger;
- an invariant-compatible architecture and source mapping;
- every blocking assumption and question resolved through linked receipts;
- coherent type, scope, exclusions, ownership, dependencies, roadmap, steps,
  acceptance gates, and verification;
- an identified acceptance authority; and
- an exact proposed accepted-baseline revision.

The stage presents the exact bounded claim, output boundary, remaining
non-blocking limitations, delivery gates, and verification obligations to the
human authority. It must not infer acceptance from earlier answers or from a
general request to continue.

After explicit acceptance, the stage creates an acceptance decision receipt,
records the accepted baseline revision, appends the `Proposed` to `Accepted`
lifecycle transition, and reconciles the initiative README, status, registry,
and parent or dependent tracking. It creates no product or delivery output.

### Stages 8 through 10: implementation path

SDK/API alignment applies only when the accepted implementation scope affects
an existing SDK or API. It may create compatible product changes traceable to
the accepted initiative, but it must route a required specification change to
a design initiative.

The readiness review is read-only and must be current for the requested phase
or work set. A missing, blocked, deferred, failed, or unmet conditional entry
gate prevents the affected execution.

Implementation execution creates or updates `execution-record.md` when product
work actually begins, records the `In progress` transition, implements only
accepted product work, and maintains the step-to-target and verification
ledger. It creates `completion-evidence.md` and records `Completed` only when
every in-scope gate has passing evidence and every record agrees.

### Stage 11: design delivery

Entry requires an accepted design initiative and a current accepted baseline.
The stage may create or modify only the initiative specifications and supporting
initiative evidence declared by the accepted scope. It must not create a new
product or modify an observed product to make the specification appear aligned.

When specification work begins, record `In progress`. Exit requires the exact
accepted design claim, `delivery-record.md`, changed specifications, source
mappings, compatibility and migration consequences, review or verification
evidence, and `completion-evidence.md` to agree. Unresolved product
implementation belongs to an implementation initiative and is not hidden
inside the design completion claim.

### Stage 12: planning delivery

Entry requires an accepted planning initiative and a current accepted baseline.
The stage may create only its declared initiative-local evidence outputs. It
must not change a product, another initiative, or an existing specification.
Specification 10 additionally permits factual recording in the project
work-conflict register; this coordination record does not change either
work claim or authorize its resolution.

When evidence work begins, record `In progress`. Exit requires every accepted
research, audit, comparison, inventory, or recommendation output;
`delivery-record.md`; its source classification and limitations; verification
of the declared method; and `completion-evidence.md` to agree. Planning output
remains non-authoritative unless an owning authority accepts it through a
separate governed action.

### Stage 13: finalization

Entry requires a truthful `Completed` initiative, completion evidence, aligned
tracking, and a branch diff that matches the completed claim. Implementation
also requires an execution record aligned with the diff.

Finalization verifies membership, provenance, active revision/assignment and
captured base; reconciles coherence feedback and traceable commits; and applies
specification 05's bounded local initiative-to-recorded-scope integration when
the actual human closure/finalization instruction and required gates are
recorded. Direct scope execution records exact verified commits without a
self-merge. It does not close or merge the scope upward, accept deferred work,
create completion, push, release, deploy or delete refs. PRs are independently
human managed: no prompt, title/body, URL requirement, command or PR handoff
belongs to finalization.

### Separate scope-closure operation

Specification 05 governs patch-to-minor, minor-to-major and major-to-captured-
base closure integration. Capture complete membership/descendants, truthful
closed dispositions, successful required child integrations, aggregate checks,
coherence/conflict reconciliation and authority. Pending integration blocks
closure; empty scopes require no-work disposition. Closing a child never
closes an ancestor. Closed parents require recorded reopening before new
membership/integration. Cancelled/superseded work retains explicit retention,
exclusion/transfer or no-deliverable disposition outside Stage 13's completed
entry contract. Shared whole-tip integration is blocked by any included
unaccepted or unfinished work. Preserve actual failures and separate lifecycle
closure from integration state; reruns and reopened deltas need current proof.

## Record ownership by stage

| Record or output | Stage that creates it | Later stages permitted to reconcile it |
|---|---|---|
| Realization-suite index and canonical correlation row | 0 | Later stages may reconcile copied lifecycle evidence but must not change allocated identity |
| Minimal README skeleton | 0 for new initiatives | 3 and later owning stages; identity remains immutable |
| Working proposal | 1 | 2 through 7 when evidence requires and it is not frozen |
| Initial initiative suite | 3 | 4 through the applicable delivery stage |
| Decision receipt | 0 for delegated intake events; 5, 6, or 7 for named human decisions | No stage rewrites the exact prompt or response; later stages may add commit links or supersession references |
| Accepted baseline revision | 7 | Only an explicitly authorized revision or reopening workflow |
| Readiness result | 9 | A later readiness review supersedes it for a named phase; execution does not rewrite it |
| Execution record | 10 | 10 and verification reconciliation before 13 |
| Design or planning delivery record | 11 or 12 | Its owning delivery stage and verification reconciliation before 13 |
| Design specification output | 11 | 11 and explicitly authorized later revisions |
| Planning evidence output | 12 | 12; later consumers cite rather than rewrite it |
| Completion evidence | 10, 11, or 12 | The owning delivery stage before finalization; corrections preserve history |
| Finalization commits and initiative integration evidence | 13 | New revision cycles and separately authorized scope closure retain history |

No supporting document may replace a missing canonical record merely because
it covers a similar subject.

## Stop, resume, retry, and return behavior

### Failed entry or verification

When an unexcepted entry gate or verification fails, preserve the failure, stop
the affected work, and identify the owning stage and evidence needed. A named
authorized exception retains the actual failed or unperformed result and
its limitation; it never supplies ordinary completion evidence. Independent
authorized work may continue when it cannot alter the failed claim.

### Human pause and resume

Resume a human review at the next unresolved stable source ID. Do not ask an
already resolved item again unless it is explicitly reopened. Do not create a
duplicate receipt for the same response; add a correction or supersession
relationship when the recorded response must change.

### Re-running a stage

A stage must be idempotent with respect to existing truthful records. Inventory
the target before writing, preserve existing evidence, and update only records
whose meaning changed. A rerun never treats the absence of new changes as a
failure and never manufactures an empty commit.

### New or changed authoritative evidence

If new authoritative evidence changes a material premise, stop affected later
stages and return to alignment. Reconcile assumptions, questions, scope, and
accepted claims. When the accepted baseline changes, obtain a new explicit
acceptance receipt before delivery resumes.

### Base-branch or dependency drift

When the captured base or a material dependency changes, compare the drift with
the accepted baseline. Continue only when evidence shows that the initiative
remains coherent and the branch can be reconciled without changing the accepted
claim. Otherwise return to alignment and acceptance. Do not rebase, merge, or
rewrite history implicitly.

### Correlation drift or missing identity

When the canonical row, realization-suite index, initiative README, active
branch, or captured base identity is missing, duplicate, partial, or
inconsistent, stop the affected stage and return to preparation recovery. Do
not infer or silently rewrite identity, provenance or assignment. Shared scopes
and declared scope branches are valid and do not fail a bijection check.
A pre-effective record proceeds under its complete compatible migration-ledger
disposition until explicit adoption/migration; subsequent intake uses the
recorded coherent-revision or separate-successor decision method.

### Partial delivery

Partial work remains `In progress`, blocked, cancelled, or superseded according
to evidence. It must not be made `Completed` by narrowing the claim after the
fact. A substantive scope revision returns through the documented revision and
acceptance workflow.

## Cross-stage reconciliation

All three delivery paths require the specification 10 cross-initiative
coherence review in completion evidence before recording `Completed`.
Inventory every other open initiative, include affected closed claims,
document incompatible effort, and route compatible feedback to its owning
workflow. Finalization verifies the review against material inventory drift
and the branch diff. A handoff does not authorize implementation or planning
to change another initiative's specifications, waive human decisions, or
refine a closed target without explicit reopening. A compatible future
refinement may remain open only when its owned handoff does not invalidate
the completing initiative's exact accepted claim.

Before every handoff, reconcile the records owned by the current stage with the
initiative README, source mapping, lifecycle history, status, registry, parent
and dependent tracking, and Git evidence that consume its result. A later stage
must stop when the handoff records are missing, stale, or inconsistent rather
than repairing earlier authority implicitly.

## Workflow versioning and compatibility

The numbered stage map, stage ownership, and required handoffs are part of the
authoritative protocol revision. Renumbering, adding, removing, or changing a
stage requires:

- explicit human authority for the workflow revision;
- updates to this specification, the suite index, lifecycle and governance
  references, prompts, templates, validator, tests, and developer documentation;
- a migration note for active initiatives using an earlier stage map; and
- preservation of historical prompt and workflow identity in existing records.

An active initiative may finish under its recorded workflow revision when that
revision remains invariant-compatible, or migrate through an explicit change
record. It must not silently mix stage contracts from different revisions.
