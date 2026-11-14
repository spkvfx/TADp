# Owned assumption and question review decisions initiative

**Initiative:** Owned assumption and question review decisions
**Initiative ID:** TADP-001
**Status:** Accepted
**Last updated:** 2026-11-14
**Initiative type:** `implementation`
**Decision prefix:** `TADP001`
**Version scope:** v2
**Source notes:** [RZN-001](../../../../evidence/non-authoritative/realizations/v2/RZN-001-owned-review-decisions.md)
**Realization suite ID:** RZN-SUITE-001
**Realization suite:** [evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md](../../../../evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md)
**Canonical project correlation:** [initiative register](../../../initiative-index.md#initiative-and-correlation-register)
**Canonical scope record:** [Version scopes](../../../version-scopes.md)
**Execution branch:** initiative/v2-tadp-001-owned-review-decisions
**Execution mode:** Dedicated
**Historical branch tip:** Not applicable; active ref retained
**Branch removal evidence:** Not applicable; no ref removal
**Captured base ref:** v2
**Captured base commit:** 9c9fd1daad655fd58349c005f8d31a4f52790cc9
**Integration target:** v2
**Revision cycle:** 1
**Claim revision:** 294d70d1b7b313bd46cab481b714c8cbb5c0e612

**Acceptance receipt:** [ACCEPT-001](decision-receipts/ACCEPT-001.md)

**Accepted baseline:** 294d70d1b7b313bd46cab481b714c8cbb5c0e612
**Prior revision record:** Initial
**Revision history:** [Routing and execution history](#routing-and-execution-history)
**Predecessor or successor:** None
**Correlation governance:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6
**Human ownership:** Apply the ownership and approval convention recorded in
`../../../../project-profile.md`. Human owner, reviewer, and approver roles resolve
as recorded there; technical component and resource boundaries remain
explicit.

Develop and qualify one candidate TADp behavior: both numbered decision reviews may independently define assumptions and open questions and record sufficiently authorized dispositions at their canonical initiative or project owners. Definition remains distinct from resolution, and an external decision does not expand the reviewed initiative's accepted work.

This accepted implementation claim is confined to the declared C=P/protocol candidate slice under ACCEPT-001. Candidate product start follows read-only readiness. Candidate qualification does not authorize or prove ordinary Completed, development completion, installed-library introduction, promotion, rollout, adoption, integration or release. The [aligned proposal](proposal/proposal.md) and [source map](../../../../evidence/non-authoritative/assumption-question-review/source-map.json) bound the work.

## Correlation and identity

The project initiative index owns this initiative's single membership row;
version-scopes.md owns its immutable scope and topology. Multiple initiatives
may share a scope, sources and a declared shared scope branch. Each retains
one narrow claim and independent lifecycle, decisions, acceptance and evidence.
Verify exact source provenance, current cycle/assignment and captured immutable
base before every stage; stop on drift instead of inferring repairs.

Record new contributing notes without relocating this initiative to their
source scope. Preserve source versus target scopes, exact note/suite IDs and
paths, routing disposition and rationale in the source mapping/history. A human
request to process an identified realization under adopted specification 09
supplies bounded LLM intake placement, coherent revision and necessary reopening
authority. Record each actual choice before applying it, with candidates,
rejected alternatives, prior claim, risks and affected records; it does not
answer unrelated questions, accept changed claims or authorize delivery.

Coherent same-outcome revision may retain identity. Independent outcomes and
incompatible type/owner/authority boundaries split or use successors, which
may share this scope and source material. Reopen changed closed claims to
Proposed; changed Accepted/In progress claims pause delivery and return to
Proposed with partial work preserved. Renew human acceptance before delivery.
Direct return from closed to Accepted needs separate human unchanged-claim
authority. Legacy targets retain their governing revision until explicitly
migrated with evidence; never infer path moves, reparenting or normalization.

### Routing and execution history

| Cycle | Exact source suite/note IDs and paths | Source scope | Target scope | Disposition and fit rationale | Instruction, delegation and actual LLM decision | Execution branch/mode | Captured base ref/commit | Integration target/evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | [RZN-SUITE-001](../../../../evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md) / [RZN-001](../../../../evidence/non-authoritative/realizations/v2/RZN-001-owned-review-decisions.md) | v2 | v2 | Originate one narrow candidate outcome; see [intake](../../../../evidence/non-authoritative/assumption-question-review/intake.md) | Codex under adopted specification 09 intake placement; human integration appointment in [INTEGRATION-001](../../../../decisions/INTEGRATION-001.md) | initiative/v2-tadp-001-owned-review-decisions / Dedicated | v2 / 9c9fd1daad655fd58349c005f8d31a4f52790cc9 | v2; no integration or closure authority |

Append cycle/continuation assignments and integration receipts; never overwrite
historical bases, prior closure snapshots, acceptance or branch-removal evidence.
On shared execution record initiative-specific paths, commits, revision base,
verification and unavoidable mixed boundaries. Serialize shared record writes.
## Protocol vocabulary

Within the initiative-type rules in this record, **specification** and
**evidence** mean the relevant initiative-scoped record or output. These terms
are distinct from artifacts in the project `../../../../evidence` directory; they do
not create, alter, reclassify, or otherwise modify repository invariants.

- `../../../../evidence/authoritative` identifies binding repository evidence that governs
  an initiative specification or product decision. An initiative may cite it
  but cannot modify it.
- `../../../../evidence/non-authoritative` identifies contextual, exploratory, or
  supporting repository evidence. It may inform a decision but cannot by itself
  override `../../../../evidence/authoritative`.
- A **product** is output material placed in a declared destination. It can be
  executable code, a script, an SDK, an API, product documentation, or another
  deliverable. A document is an **initiative specification** when it defines
  what a product must do; classify it by its role, not its file extension.

## Initiative type and output boundary

This initiative selects `implementation` and follows its output boundary. The canonical type boundaries remain:

| Type | Alignment direction | May create or modify | Must not |
|---|---|---|---|
| `implementation` | Products to initiative specifications | Products and their product documentation | An initiative specification owned by another initiative |
| `design` | Initiative specifications to existing products | Initiative specifications and supporting initiative evidence | A new product |
| `planning` | Initiative evidence for other initiatives | Its own initiative record and initiative-local evidence documents or reports | Products, initiative specifications, or documents outside its declared scope |

The terms in this table describe initiative work. A design or planning
initiative may be cited by another initiative as a specification or evidence,
but that status does not modify repository evidence or any invariant.

An implementation initiative that discovers a conflict with an initiative
specification stops the affected product work and routes the needed initiative
specification change to a design initiative. A design initiative records the
observed product state as initiative evidence and does not create a new product
to make its initiative specification appear aligned. A planning initiative's
complete record, including its standard documents and any reports it creates,
is initiative evidence for other initiatives. It may create or revise only
documents within its declared scope. A planning report must remain within the
planning initiative, be classified as initiative evidence, and may be cited by
another initiative but must not amend that initiative's record. Planning output
is normally classified `../../../../evidence/non-authoritative` until an explicit owning
authority accepts it as `../../../../evidence/authoritative`; that acceptance affects the
initiative record only and does not modify repository evidence or an invariant.

## Narrow scope and nesting

An initiative owns one narrowly bounded outcome and one independently
reviewable acceptance claim. Do not create umbrella or multi-purpose
initiatives. When outcomes, owners, authority boundaries, or completion gates
can be separated, use separate initiatives.

Record the cohesion test and every split trigger in
[scope-assessment.md](scope-assessment.md). A split is mandatory when a portion
has its own outcome, owner, authority boundary, initiative type, verification or
release claim, unrelated product destination, or independent lifecycle, unless
an explicit human decision records why that trigger does not apply.

A subinitiative is permitted when it implements, designs, or investigates one
smaller dependent outcome inside an actual parent specification. It must cite
the parent requirement, keep its own coherent record and verification, and
must not expand the parent or absorb unrelated work.

Every parent, sibling and subinitiative has independent identity, records and
acceptance evidence. They may share scope, sources and a declared scope branch.
A version scope is a coordination container, never an umbrella acceptance claim.

## Coherence with other work

Proposed, planned, and partially delivered effort in open initiatives is work
that must be included in coherence review; its existence does not create
acceptance or authority. Review current open initiatives and affected closed
claims at alignment and completion. Preserve each claim, lifecycle state,
effort evidence, impact, and disposition. Link conflicts from affected records
to the project `initiatives/work-conflicts.md`; also record invariant
contradictions in the authoritative conflict register.

Completion findings may refine open work through the target's authorized
workflow, branch, and human gates. They do not authorize changes to another
initiative, resolve its questions, or widen this initiative's declared type.
Stop affected acceptance, execution, or completion while a conflicting claim
remains incompatible. Independently owned follow-up may remain open only when
it does not contradict the completed claim.

A closed initiative (`Completed`, `Cancelled`, or `Superseded`) must be
reopened with a receipt under bounded adopted intake delegation or separate
human authority before refinement, returning to Proposed. Preserve prior claims
and apply coherent revision versus mandatory split rules. Append-only historical corrections and
administrative links must not change earlier meaning.

Actual inventory at preparation: TADP-001 is the only allocated P initiative. The earlier documentation split and refresh remain proposed/partially prepared effort and were included without promoting their authority. Their candidate files and history remain unchanged. No incompatible claim or closed P claim requiring reopening was identified; future overlapping navigation changes require exact comparison at their separately authorized delivery boundary. See [intake](../../../../evidence/non-authoritative/assumption-question-review/intake.md#inventory-candidates-and-fit-before-allocation) and [work conflicts](../../../work-conflicts.md).

## Products and placement

Record every product output and its destination. A destination can be a
repository path, package, API route, documentation site, or another explicit
placement; it does not need to be a directory named `products`.

| Product | Form | Destination | Governing specification | Verification |
|---|---|---|---|---|
| Owned decision-review candidate | Reusable prompts, rule text, shapes, navigation and minimum necessary validation/fixtures | P/protocol/template and P/protocol/tests/test_assumption_question_review.py, exactly as declared in the linked source map | [Architecture](architecture.md), [source mapping](source-mapping.md) and aligned proposal | Future structural/link/protection checks, focused scenarios, pinned isolated trial and independent complete-diff review; none performed yet |

## Proposal source

The proposal inputs and their precedence are cataloged in
[proposal/README.md](proposal/README.md). The canonical Markdown proposal is
[proposal/proposal.md](proposal/proposal.md). Preserve frozen proposal inputs
as historical source material; record corrections in [assumption.md](assumption.md)
and accepted repository decisions in [architecture.md](architecture.md).

## Reading order

1. Read [proposal/proposal.md](proposal/proposal.md) and the source inventory
   for the intended outcome and original rationale.
2. Review [assumption.md](assumption.md) to confirm or correct the assumptions
   that constrain the plan.
3. Review [scope-assessment.md](scope-assessment.md) to confirm that the
   initiative owns one bounded outcome and to identify required splits.
4. Read [architecture.md](architecture.md) for the repository-specific
   specification, ownership boundaries, `../../../../evidence/authoritative`, and failure
   behavior.
5. Use the [evidence mapping](source-mapping.md) to trace evidence classification
   to assumptions, decisions, specifications, product destinations, and
   verification.
6. Resolve blocking decisions in [open-questions.md](open-questions.md).
7. Use the [delivery roadmap](implementation-roadmap.md) for delivery
   order, dependencies, rollout controls, and release gates. For a design or
   planning initiative, its delivery is specification or evidence work, not
   product implementation.
8. Use the [delivery steps](implementation-steps.md) for reviewable
   change sets, affected paths, verification, and acceptance criteria.

## Optional supporting documents

The `evidence mapping` is a standard traceability file. Add another focused
supporting document only when its evidence would overwhelm a standard file.
Common examples are `repository-audit.md` for extensive
current-state evidence and `data-classification.md` for a large state-placement
matrix. Use the standard execution and completion records below instead of an
ad hoc implementation report.
Link every supporting document here, state its purpose, and keep decisions in
`open-questions.md` rather than creating a second decision log.

A planning initiative may add a focused report of initiative evidence when
needed, but the report must remain within that initiative and cannot become an
initiative specification or an edit to another initiative's record.

## Implementation-readiness review

`implementation-readiness.md` applies only to an `implementation` initiative
and is deliberately **not** part of the initial initiative record. Do not
create, copy, or link a file when creating an initiative. The shared
[readiness template](../../../../template/project/initiatives/implementation-readiness.template.md) provides the response shape
for the phase-specific Stage 9 go/no-go assessment, reviewed evidence,
remaining inputs, and execution gates. It creates no durable file unless an
applicable governing requirement explicitly requires one. Preserve historical
durable readiness records under their recorded revision. Recover necessary
documentary inputs through preceding owning-stage preparation, disclose those
changes, then assess readiness read-only against current phase evidence. A
reconstructed document does not establish that its gate passed.

## Delivery, execution, and completion records

`execution-record.md` applies to an accepted `implementation` initiative and
is created when product execution actually begins. Keep its step ledger,
product destinations, verification, blockers, commits, and reconciliation
current throughout execution.

`delivery-record.md` applies to an accepted `design` or `planning` initiative
and is created when its permitted specification or evidence work actually
begins. Keep its output ledger, destinations, method, verification, blockers,
commits or revisions, and reconciliation current throughout delivery.

`completion-evidence.md` applies to every initiative type and is created only
when the initiative's permitted work reaches an evidence-backed terminal
result. It records the exact bounded claim, authoritative-evidence coverage,
outputs, verification, compatibility, residual scope, and cross-record
reconciliation. Its cross-initiative coherence review inventories other open
initiatives, affected closed claims, effort evidence, findings, and governed
dispositions, including linked work conflicts. It is required before `Completed`; it does not replace a
product record or expand a local result into a release or production claim.

Candidate qualification alone will not satisfy the installed development workflow's later exact D-introduction and actual development-completion boundaries. No completion record or ordinary Completed claim follows merely from finishing this currently authorized slice.

## Human decision receipts

Create `decision-receipts` from the shared templates when the first explicit
human decision is received. Create one receipt for each assumption disposition,
open-question answer, lifecycle decision, or invariant exception. Preserve the
exact prompt and exact response, link the receipt from its source record, and
commit it with the records reconciled from that decision. A receipt proves the
decision only; it does not prove implementation or verification.

## Reusable prompts

Use the [coverage and use map](../../../../template/TEMPLATE-COVERAGE.md) to select the canonical
source and destination for each required file or embedded section. It includes
conditional later records, stage ownership, evidence inputs, and verification.
Prepare only the prerequisites needed by the invoked activity under the
[shared contract](../../../../template/prompts/WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation),
without recursively executing linked prompts. Reuse existing records and
preserve stable IDs, human text, accepted baselines, source identities, and
history. Missing authority, identity, facts, or passing verification remain
blockers after documentary recovery.

[Initiative prompts](../../../../template/prompts/README.md) contains reusable prompts for initiative
reviews and creation. It follows this sequence:

0. [prepare initiative](../../../../template/prompts/00_initiative_preparation.md)
1. [proposal creation](../../../../template/prompts/01_proposal_creation.md)
2. [proposal alignment](../../../../template/prompts/02_proposal_alignment.md)
3. [initiative creation](../../../../template/prompts/03_initiative_creation.md)
4. [initiative-to-precedent alignment](../../../../template/prompts/04_initiative_alignment.md)
5. [initiative assumption confirmation review](../../../../template/prompts/05_initiative_assumption_review.md)
6. [initiative open-question resolution review](../../../../template/prompts/06_initiative_open_question_review.md)
7. [initiative acceptance](../../../../template/prompts/07_initiative_acceptance.md)
8. [initiative SDK/API alignment](../../../../template/prompts/08_initiative_sdk_api_alignment.md), for implementation when applicable
9. [initiative implementation-readiness review](../../../../template/prompts/09_initiative_implementation_readiness_review.md), for implementation
10. [implementation execution](../../../../template/prompts/10_initiative_execution.md), for implementation
11. [design delivery](../../../../template/prompts/11_design_delivery.md), for design
12. [planning delivery](../../../../template/prompts/12_planning_delivery.md), for planning
13. [finalize initiative](../../../../template/prompts/13_initiative_finalization.md).

Add future prompts to that directory and its README; prompts guide review,
while documented source precedence and repository evidence continue to govern
the outcome.

## Repository baseline

- The installed suite at governing revision 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6 remains binding. The exact invoked prompt authorizes its named candidate rule revision only.
- The installed review sources contain the restrictions identified in [preflight](../../../../evidence/non-authoritative/assumption-question-review/preparation.md#affected-rules-and-consumers). Candidate replacements do not amend those installed governing sources merely by being written or qualified.
- Project integration base v1 and scope/dedicated branch bases are recorded in [intake](../../../../evidence/non-authoritative/assumption-question-review/intake.md). Allocation and assignment establish identity only; the original prompt retains human acceptance and later delivery gates.

## Intended outcome

Both candidate reviews support existing and new assumptions and questions, same-review authorized dispositions, and proper external canonical owners. Their shared contract, governing candidate rules, record shapes and necessary consumers agree. Exact qualification evidence and a reviewed manifest describe compatibility, prospective adoption, migration, recovery and every remaining boundary without making an installed or completion claim.

## Scope

### Included

- The 16 pinned source-to-candidate mappings, the smallest conditional project-owned register, and necessary declared candidate guards/locks and isolated scenarios in the [source map](../../../../evidence/non-authoritative/assumption-question-review/source-map.json).
- An exact qualification manifest and compatibility, prospective adoption, migration, recovery, remaining-gate and downstream-consumer guidance in owning P records outside the reusable payload. All evidence must distinguish actual checks from planned, skipped, unavailable or failed checks.

### Excluded

- All installed D=P/template sources/tools/suite/locks, S=R/protocol/template, U=R/protocol, live review records, other scaffolds/forks/services and existing documentation candidates are outside candidate edits. Installed introduction, ordinary development completion, promotion, rollout, integration, adoption, live migration, release and publication retain separate exact authority/evidence.
- Keyword semantics, stage numbering, initiative types, narrow-scope rules, ordinary acceptance/completion meanings, closed-claim protection, project-local prompt authority, unrelated invariants and SDK/API work remain unchanged.

## Dependencies

| Initiative or contract | Relationship | Required state |
|---|---|---|
| Installed governing suite and pinned reusable sources | Read-only provenance and requirements for the exact candidate slice; no installed edit or adoption | Preserved at declared digests; current source/destination comparison before any later delivery |

## Readiness

| Area | Current evidence | Required before the next initiative output |
|---|---|---|
| Product direction | Proposal revision 2 states one candidate decision-review behavior, permitted output and exclusions. | Complete-suite alignment followed by explicit human acceptance of the exact proposed baseline; no acceptance inferred from intake. |
| Repository fit | Recorded v2/dedicated assignment and [scope assessment](scope-assessment.md) preserve one outcome and include earlier proposed/partial documentation effort. | Confirm reciprocal identity and current source/consumer mapping at alignment and before execution. |
| Data and migration | Stable IDs, exact text, canonical ownership and receipt/history preservation are declared; no live migration is included. | Candidate shapes and guidance must preserve earlier compatible governing revisions and disclose future adoption/migration requirements. |
| Operations and recovery | Pinned sources and history remain available; no destructive rollback or external action is authorized. | Declare exact candidate/fixture dependencies, protection and scoped recovery before implementation and qualification. |
| Verification | Baseline P checks are recorded in preflight; no candidate check or isolated trial has run. | After actual acceptance: phase-specific readiness, focused scenarios, pinned isolated trial, source protection, links and independent scoped-diff review. |

## Initiative lifecycle

- **Proposed:** proposal, assumptions, and repository design are open
  for review.
- **Accepted:** an identified human authority explicitly accepted the exact
  baseline after blocking decisions, assumption corrections, and standard
  records were reconciled. The acceptance receipt and lifecycle transition
  must be linked; an earlier decision or instruction to continue is not
  acceptance.
- **In progress:** the initiative's permitted work is underway and completed
  gates carry linked evidence.
- **Completed:** the type-specific acceptance criteria pass and durable
  conclusions have moved to accepted specifications, products, or evidence.
- **Cancelled:** the initiative stops without a replacement; retain the reason,
  reusable evidence, and any accepted conclusions.
- **Superseded:** a replacement is linked and this directory remains as
  historical context.

`Reopened` is an event, not a status. A reopened initiative returns to
`Proposed` unless an explicit human decision records that the previously
accepted claim is unchanged and authorizes return to `Accepted`.

Membership allocation, a branch, and a version scope do not prove any lifecycle state.
Preserve the exact branch and base identity after a separately authorized
branch removal and link that removal evidence from the canonical row.

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| 2026-11-14 | Initial | Proposed | [realization suite](../../../../evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md) and [canonical correlation row](../../../initiative-index.md#initiative-and-correlation-register) | Preparation skeleton | Allocate independent initiative membership and open the initiative for proposal work; no acceptance or delivery authority | 7b38e61 |
| 2026-11-14 implementation request | Proposed | Accepted | [ACCEPT-001](decision-receipts/ACCEPT-001.md), requesting human under repository-owner role | 294d70d1b7b313bd46cab481b714c8cbb5c0e612 | Exact candidate implementation and qualification accepted after clarification | Scoped acceptance commit |

### Preparation events

Stage 0 created the original skeleton and Initial-to-Proposed event in commit 7b38e61. Stages 1 and 2 created and aligned proposal revision 2. Stage 3 expands the complete initial suite from the installed canonical sources while retaining this event and assignment. These are factual preparation activities, not lifecycle transitions, acceptance or product execution. The current complete Proposed claim awaits Stage 4 alignment and distinct Stage 7 human acceptance.

## Initiative record maintenance

When an assumption is confirmed or corrected, update `assumption.md` and every
affected initiative document in the same change. When a decision is accepted,
update its stable entry in `open-questions.md`, then reconcile the architecture,
roadmap, and implementation step that depend on it. Update `Last updated` only
in files whose meaning changed. An implementation or design initiative updates
the project-level `initiatives/status.md` whenever its status or next milestone changes. A planning
initiative records those changes only in its own record; a shared-status owner
may cite that evidence separately.

Every status change must be a legal lifecycle transition backed by the required
evidence and appended to the lifecycle history. Reopening must preserve the
prior accepted or completed claim and exact intake delegation or separate
human authority, actual decision author and recorded change boundary. Before refining a closed initiative, link the reopening decision
receipt and record its return to `Proposed`, or to `Accepted` only under the
explicit unchanged-claim exception. Historical corrections and successor
links may be appended under `Historical correction`, `Successor references`,
or `Administrative addendum` headings without changing earlier meaning.

## Authority and conflict discipline

An initiative is authoritative for its declared status, scope, and stated
outcome. An accepted initiative is authoritative for approved work. Every
initiative must remain coherent with every other accepted initiative, applicable
authoritative initiative evidence, proposed and partial open work, and the
products it governs. Open effort remains at its original evidence standing.
Record and
resolve every conflict explicitly; do not silently rewrite another initiative,
a product record, or a cited invariant to make this initiative appear aligned.

An initiative may cite an invariant as evidence, but it never changes that
invariant. Treat cited artifacts as read-only: preserve them and record an
initiative-local correction or reference to a new revision only when explicitly
authorized. `../../../../evidence/non-authoritative` may explain ambiguity or support a
decision, but cannot supersede `../../../../evidence/authoritative`.


## Closure and integration evidence

Record lifecycle closure separately from Git integration. A Completed dedicated
initiative integrates into its assigned scope branch only after gates and
recorded human close/finalize authority; direct shared placement records exact
verified commits without self-merge or scope-upward merge. Retain source/target
tips, target ref, authority, method/result commit and post-checks for each cycle.
Failure leaves integration pending/blocked without inventing success or erasing
truthful prior completion. Cancelled/Superseded deliverables need explicit
retain/exclude/transfer/no-deliverable disposition. This member's closure never
closes scope or siblings. Source refs are retained unless removal is separately
authorized. New cycle deltas need fresh completion and integration evidence.
## Source routing provenance

| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |
|---|---|---|---|---|---|---|
| RZN-SUITE-001 | [RZN-SUITE-001](../../../../evidence/non-authoritative/realizations/v2/00-review-decisions-suite-index.md) | RZN-001 | v2 | [RZN-001](../../../../evidence/non-authoritative/realizations/v2/RZN-001-owned-review-decisions.md) | originate | [Recorded intake](../../../../evidence/non-authoritative/assumption-question-review/intake.md) |

Retain exact originating and later contributing notes independently. Each row
links its source suite and note and the per-source fit/authority record. Source
scope may differ from target scope without relabeling either identity.

Any absent historical dedicated ref retains its exact immutable Historical
branch tip and separately authorized Branch removal evidence. That removal
receipt records Human authority and exact Branch; removing a ref never frees
its identity for unrelated work or qualifies a new cycle.
