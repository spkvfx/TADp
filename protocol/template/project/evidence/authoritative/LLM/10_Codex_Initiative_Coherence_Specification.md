# Codex initiative coherence specification

## Purpose and authority

Coherence includes all relevant work, not only delivered products. An open
initiative represents work even before acceptance or product execution.
Completion learning must be usable by open initiatives without silently
changing a closed claim or discarding conflicting effort.

Apply the canonical
[prompt keyword specification](11_Codex_Prompt_Keyword_Specification.md)
to requests involving this specification. Coherence, conflict, completion,
and reopening requirements below remain the ordinary contract. A mode name
does not except an inventory, resolve an incompatibility, authorize a target
edit, or supply human reopening authority. A proposed exception must identify
the exact affected rule, block, prior claim, authority, consequences, and
dependent records, with its receipt and exception record created before use.
An agent-inferred exception requires explicit confirmation. Never hide known
incompatible effort or convert waived or failed review into passing evidence.
Ordinary lifecycle labels retain their meanings; excepted prompt completion
does not establish ordinary initiative completion. Restored gates require
current checks when later work depends on excepted output. Locks and
historical source identities remain enforced.

### Revision record

- **Authority:** The User's exact 2026-11-12 instructions preserved in
  COH-DR-001 (TADp distribution source `decisions/COH-DR-001-initiative-coherence.md`; not a project decision or work record).
- **Reason:** Make completion feedback, recognition of open effort,
  work-conflict recording, and closed-claim preservation explicit.
- **Affected scope:** Governance, lifecycle, decisions, workflow handoffs,
  common and type-specific reusable sources, validation, tests, documentation,
  the reference protocol, and the installed example.
- **Effective event:** Adoption of this coherent revision and its consumers.
  Each adopting project records a `Coherence revision baseline` in its project
  profile: the immutable Git snapshot immediately before adoption, not an
  invented future effective commit.
- **Compatibility and migration:** Preserve earlier claims and their evidence.
  Unchanged terminal initiatives at the adoption baseline need no retrospective
  completion review. All new work, completion, and later refinement follow
  this rule. Adoption must not silently accept an open initiative, settle a
  question, or change a historical claim.
- **Successor relationship:** This specification strengthens specifications
  02, 04, 07, and 08 for coherence and feedback. Evidence precedence, human
  gates, type-specific output boundaries, scope, and specification 09's
  substantive-successor requirement remain binding. Git retains predecessors.

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

## Work inventory and standing

`Proposed`, `Accepted`, and `In progress` are open states. `Completed`,
`Cancelled`, and `Superseded` are closed states. `Reopened` remains an event.

Before alignment, acceptance, materially changing work, or completion, Codex
must inventory relevant open initiatives and their effort alongside accepted
specifications, partial delivery, completed work, and released contracts. The
review must consider intended scope, assumptions, decisions, dependencies,
ownership, interfaces, verification, products, and known changes or sunk
effort. Proposed work must not be omitted because it is unaccepted or has no
product output. Independent, unrelated work need not be absorbed into scope.

Counting effort as work does not promote its authority. A proposal remains a
proposal; partial implementation remains observed evidence. Time spent, recent
completion, or a later version never overrides an invariant or accepted claim.
Coherence is established by reconciling actual conflicts, not by deleting the
weaker source or pretending that its effort did not occur.

## Work conflicts

A work conflict exists when two intended, accepted, partial, or delivered
efforts cannot coexist as described within a shared scope, ownership,
contract, dependency, compatibility, or verification boundary. An unresolved
choice is not automatically a conflict; cite the incompatible claims.

Each project must keep `initiatives/work-conflicts.md` as its canonical
work-conflict register. Every discovered work conflict requires a stable ID,
both exact source identities and claims, their lifecycle and authority
standing, planned or performed effort, evidence, affected scope and impact,
owner, blocked actions, required decision or correction, and disposition.
Link the register from affected initiative-local source mappings, questions,
status, or other canonical conflict records. Preserve resolved entries and
the earlier claims. A register entry records a conflict; it does not resolve
one or transfer authority.

The reusable minimum table is:

| ID | Source work | Conflicting work | States and effort | Conflict and impact | Owner | Status | Disposition and evidence |
|---|---|---|---|---|---|---|---|

Each row must link both work sources and retain their precise claims, evidence
and limits in the row or a linked detailed entry. Status is `Open` or
`Resolved`. Record blocking scope and a concrete next action while open. A
resolution requires evidence of a compatible correction or linked human
decision, with the affected records reconciled. Do not erase an entry when
work is cancelled, superseded, transferred, or no longer being executed.

An invariant contradiction must also use the authoritative invariant-conflict
register and the specification 01 procedure. Work-versus-work conflicts that
do not contradict an invariant must not be misclassified as invariant changes.
Stop the incompatible acceptance, execution, or completion claim. Independent
authorized work may continue. Human choices, assumption dispositions,
acceptance, and exceptions retain their required receipts.

## Completion feedback and refinement

Before an initiative transitions to `Completed`, every delivery type must
produce a cross-initiative coherence review in `completion-evidence.md`.
Finalization must verify that review remains consistent with the branch diff
and any material inventory drift. The review must:

1. Identify the inventory baseline and the project work-conflict register.
2. Account for every other currently open initiative, including `Proposed`
   initiatives; name unrelated targets with a reason rather than omitting
   them. Include closed targets affected by the findings.
3. Record each target's lifecycle state, work and effort evidence, finding,
   required disposition, and linked records. Use the table columns below;
   the completing initiative cannot stand in for another target.
4. Record discovered conflicts and their owners. Route compatible refinements
   to the target's normal alignment, decision, acceptance, or design workflow.
5. Reconcile all source-claim blockers before claiming completion. A compatible
   future refinement may remain owned by an open target with a concrete
   handoff and re-entry condition only when it does not invalidate the
   completing initiative's exact accepted claim.

Required heading and fields are `## Cross-initiative coherence review`,
`**Inventory baseline:**`, and `**Work-conflict register:**`, followed by:

| Target initiative | Lifecycle state | Work and effort evidence | Finding | Disposition | Record links |
|---|---|---|---|---|---|

With no other open or affected closed targets, retain the empty table and an
explicit evidence-based statement. Each target row must link the target and
the records supporting its disposition. Prefix a finding that identifies
incompatible work with `Conflict:` and link its work-conflict register entry
using a stable `#work-conflict-NNN` anchor matching a registered ID;
the validator checks this declaration without inferring semantic conflicts
from narrative text. A completed review is historical
evidence at its stated baseline; later initiative creation does not rewrite it.
New material drift before finalization requires a new or reconciled review.

Completion gives findings evidence standing, not permission to edit every
target. An implementation initiative routes specification changes to design;
a planning initiative records and hands off findings without changing another
initiative. A design initiative may change only specifications declared in
its accepted scope. Refinement must use the branch and edit boundary
authorized for the governing operation by specifications 05, 08, and 09.
Accepted design delivery may edit its named target specifications on the
design initiative's branch; target acceptance, reopening, and lifecycle
decisions remain owned by the target's workflow. The completing branch must
not absorb another initiative's execution work.

Open refinements may improve evidence, detail and consistency. Under adopted
specification 09 intake delegation, the LLM may revise the same coherent narrow
outcome instead of forcing a successor for every substantive change. Independent
outcomes, mandatory split triggers and incompatible type/owner/authority
boundaries still require separate complete initiatives. Changed accepted or
in-progress claims pause affected delivery, preserve partial work and return
to `Proposed` for alignment and renewed human acceptance. Completion feedback
alone supplies no intake delegation. An unresolved or previously answered
question cannot be automatically resolved or reopened merely because another
initiative completed.

## Closed-claim preservation and reopening

Codex must not refine a closed initiative's specification, scope, assumptions,
decisions, delivery, or verification claim while leaving it closed. First
preserve the exact prior claim and record specification 09 bounded realization
intake delegation or separate explicit human reopening authority. Create an
event-specific receipt identifying the actual LLM author and intake fit,
append the event, and reconcile affected records before substantive edits.
Return to `Proposed` unless a separate explicit human unchanged-claim decision
authorizes direct return to `Accepted`. This applies to completed, cancelled
and superseded targets, with prior cancellation and replacement consequences
explicitly reconciled. Reopen every necessary closed scope/ancestor by its own
event; no child event silently reopens or re-closes ancestors.

The receipt must declare `**Disposition:** Reopened` and
`**Human authority:**`. A direct terminal-to-`Accepted` reopening additionally
requires `**Unchanged accepted claim:** Yes`, the exact prior claim and
baseline, and the new verification boundary. A previously used acceptance or
reopening event is not authority for a new event. A recorded human intake may
delegate several necessary events, each with its own target/claim disposition;
never label the LLM result as a per-target human response. Unrelated questions,
acceptance and execution remain outside that delegation. Closing again requires
new completion evidence; a same-change reopen and close must retain both
events and their separate evidence.

A separate successor may instead preserve the closed predecessor intact and
own the new claim with complete records and independent acceptance. It may
share scope and precise realization sources. This does not refine the closed
record. A successor reference may be appended without reopening. Preserve
prior closure snapshots and integrated commits; new revision deltas require
fresh completion and integration evidence, including affected ancestors.

Append-only factual historical corrections and administrative or successor
references that preserve the earlier claim are permitted without reopening.
Use `## Historical correction`, `## Successor references`, or
`## Administrative addendum` for README additions; other existing records may
append `## Historical correction`. A `Last updated` field may be advanced.
These exceptions cannot change normative meaning, replace old evidence,
rewrite receipts, or conceal a revised claim. An existing closed record must
not be deleted, moved, or renamed to evade preservation.

## Validation and limits

An adopting project records `**Coherence revision baseline:**` with a valid
pre-adoption Git commit and instantiates the work-conflict register. Validation
must check the register structure, completion-review fields and inventory,
and new terminal-claim changes against Git history. Unchanged completions
already terminal at the adoption baseline retain their historical evidence.
The recorded adoption baseline is immutable. Removing or deactivating the
profile declaration, or changing its baseline, must not silently disable
checks that were already adopted.

The default terminal-edit comparison is `HEAD`; review and CI must also use
`--base-ref` with the captured integration or review base to cover changes
already committed on the branch. An invalid or unavailable comparison ref
must fail the affected check, not silently disable preservation. History and
append-only corrections must survive both comparisons.
Branch review must account for initiatives that close and are then changed in
later commits within the review range, not only targets already closed at the
range's starting snapshot. Separately governed nested initiatives retain
their own lifecycle and edit boundary; a closed parent does not make an open
child closed, nor permit changes to the parent's claim.

Machine checks enforce objective records and preservation signals. They do
not establish semantic compatibility, completeness of conflict discovery,
authentic human authority, or the correctness of a claimed unchanged outcome.
Human review remains required for those claims. A validator must never resolve
a conflict, reopen a target, manufacture evidence, or repair a disposition.
