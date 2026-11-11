# Codex initiative workflow specification

## Purpose and authority

This specification defines the required end-to-end workflow semantics for a
TADp initiative. It governs stage order, stage entry and exit evidence,
record ownership, type-specific delivery paths, acceptance, recovery, and
finalization.

Numbered prompts implement this specification for Codex. A prompt may impose a
stricter operational precondition, but it must not skip, weaken, reorder, or
expand the authority granted by this specification.

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
governs identity allocated by Stage 0 and verified by every later stage. Tuple
creation is preparation evidence only and does not change lifecycle standing.

## Universal workflow rules

Every stage must:

1. Identify the exact initiative, declared type, active branch, stage, and edit
   boundary before changing anything.
2. Read applicable authoritative evidence before using lower-standing evidence
   for a normative conclusion.
3. Preserve source identity, authority, revision, limitations, and unresolved
   conflicts.
4. Operate only on records and outputs owned by the stage.
5. Stop the affected work when an entry gate fails or a required human decision
   is missing.
6. Preserve unrelated work and report every changed path and verification
   result truthfully.
7. Reconcile every record named by the stage's exit contract before handing the
   initiative to another stage.
8. For a tuple governed by specification 09, verify the canonical work
   version, suite, initiative, branch, captured base, and reciprocal links
   before consuming or changing the initiative.

No stage may use urgency, a recommendation, implementation convenience, or the
existence of later work to infer an earlier gate.

## Canonical stage sequence

| Stage | Activity | Applies to | Principal output | Lifecycle effect permitted |
|---|---|---|---|---|
| 0 | Correlated initiative preparation | All types | Version-bearing branch, realization-suite index, canonical correlation row, and minimal skeleton | None |
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
| 13 | Finalization | All types after completion | Reconciled commit, push, and pull request when configured | No new completion claim |

Stages 5 and 6 are repeated until their applicable source records have explicit
human outcomes. Stages 8 through 10 form the implementation path. Stage 11 is
the design path. Stage 12 is the planning path. An initiative follows exactly
one delivery path for its declared type.

## Stage entry and exit contracts

### Stage 0: preparation

Entry requires a Git repository, a checked-out source branch, a clean worktree,
an unambiguous initiative identity and type, readable suite and skeleton
templates, and a read-only preflight proving that the proposed canonical work
version, suite ID and path, initiative ID and path, and version-bearing branch
are unused. The stage captures the base branch and base commit before writing.

The stage creates the dedicated branch from that base. On the new branch it
may create, as one preparation unit, the realization-suite index and initial
non-authoritative realization note, canonical project correlation row,
reciprocal correlation metadata, and only the minimal initiative and
proposal-source README skeleton. The initiative remains `Proposed`; Stage 0
creates no proposal, decision, acceptance, or delivery output. Exit verifies
every reciprocal link and records the work version, suite, initiative, branch,
captured base, target placement, and any preparation commit.

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

Finalization may commit remaining accepted work, push the initiative branch,
and open one pull request when the repository is configured and authorized. It
does not create completion, accept deferred in-scope work, merge, deploy,
enable auto-merge, or delete the branch.

## Record ownership by stage

| Record or output | Stage that creates it | Later stages permitted to reconcile it |
|---|---|---|
| Realization-suite index and canonical correlation row | 0 | Later stages may reconcile copied lifecycle evidence but must not change allocated identity |
| Minimal README skeleton | 0 | 3 and later owning stages; tuple identity remains immutable |
| Working proposal | 1 | 2 through 7 when evidence requires and it is not frozen |
| Initial initiative suite | 3 | 4 through the applicable delivery stage |
| Decision receipt | 5, 6, or 7 for its named human decision | No stage rewrites the exact prompt or response; later stages may add commit links or supersession references |
| Accepted baseline revision | 7 | Only an explicitly authorized revision or reopening workflow |
| Readiness result | 9 | A later readiness review supersedes it for a named phase; execution does not rewrite it |
| Execution record | 10 | 10 and verification reconciliation before 13 |
| Design or planning delivery record | 11 or 12 | Its owning delivery stage and verification reconciliation before 13 |
| Design specification output | 11 | 11 and explicitly authorized later revisions |
| Planning evidence output | 12 | 12; later consumers cite rather than rewrite it |
| Completion evidence | 10, 11, or 12 | The owning delivery stage before finalization; corrections preserve history |
| Finalization commit and pull request | 13 | Later merge or release workflows outside this stage |

No supporting document may replace a missing canonical record merely because
it covers a similar subject.

## Stop, resume, retry, and return behavior

### Failed entry or verification

When an entry gate or verification fails, preserve the failure, stop the
affected work, and identify the owning stage and evidence needed. Independent
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
not infer or silently rewrite a tuple. A pre-effective record proceeds only
under its complete migration-ledger disposition; substantive re-entry after
the effective point allocates a new governed tuple.

### Partial delivery

Partial work remains `In progress`, blocked, cancelled, or superseded according
to evidence. It must not be made `Completed` by narrowing the claim after the
fact. A substantive scope revision returns through the documented revision and
acceptance workflow.

## Cross-stage reconciliation

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
