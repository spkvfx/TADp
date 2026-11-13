<!--
Copy the standard files in this directory to initiatives/{{version_scope}}/{{initiative_type}}/{{initiative_id_and_slug}}.
Do not copy `implementation-readiness.md`, `execution-record.md`,
`delivery-record.md`, `completion-evidence.md`, or `decision-receipts/` during
initiative creation.
They are later-stage templates created only when their named stage begins.
Replace every double-brace token, remove instructional comments, and keep the
standard files. If a section does not apply, state why instead of deleting it.
-->

# {{initiative_name}} initiative

**Initiative:** {{initiative_name}}
**Initiative ID:** {{initiative_id}}
**Status:** Proposed
**Last updated:** {{date}}
**Initiative type:** `{{initiative_type}}`
**Decision prefix:** `{{decision_prefix}}`
**Version scope:** {{version_scope}}
**Source notes:** {{exact_originating_and_contributing_note_ID_path_links_only}}
**Realization suite ID:** {{originating_realization_suite_id}}
**Realization suite:** [{{realization_suite_path}}]({{relative_realization_suite_index_path}})
**Canonical project correlation:** [initiative register]({{relative_initiative_index_path}}#initiative-and-correlation-register)
**Canonical scope record:** [Version scopes]({{relative_version_scopes_path}})
**Execution branch:** {{active_execution_branch}}
**Execution mode:** {{dedicated_or_shared}}
**Historical branch tip:** {{immutable_tip_if_ref_removed_or_not_applicable}}
**Branch removal evidence:** {{separate_removal_receipt_link_or_not_applicable}}
**Captured base ref:** {{captured_base_ref}}
**Captured base commit:** {{immutable_base_commit}}
**Integration target:** {{assigned_scope_branch}}
**Revision cycle:** {{positive_integer_cycle}}
**Claim revision:** {{exact_current_claim_revision}}
**Prior revision record:** {{preserved_previous_README_assignment_snapshot_link_or_initial}}
**Revision history:** {{cycle_history_link}}
**Predecessor or successor:** {{relationship_or_none}}
**Correlation governance:** {{adopted_revision_or_legacy_ledger_link}}
**Human ownership:** Apply the ownership and approval convention recorded in
`{{project_profile_path}}`. Human owner, reviewer, and approver roles resolve
as recorded there; technical component and resource boundaries remain
explicit.

<!--
In one or two paragraphs, state the initiative's intended outcome, why it is
needed now, and the principal repository or product boundary it changes.
Lead with the proposed result rather than the history of the discussion.
-->

{{initiative_summary}}

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
| {{cycle}} | {{source_links}} | {{source_scope}} | {{immutable_target_scope}} | {{routing_record}} | {{receipt_author_method}} | {{branch_mode}} | {{base}} | {{target_and_evidence}} |

Append cycle/continuation assignments and integration receipts; never overwrite
historical bases, prior closure snapshots, acceptance or branch-removal evidence.
On shared execution record initiative-specific paths, commits, revision base,
verification and unavoidable mixed boundaries. Serialize shared record writes.
## Protocol vocabulary

Within the initiative-type rules in this template, **specification** and
**evidence** mean the relevant initiative-scoped record or output. These terms
are distinct from artifacts in the repository `../../evidence` directory; they do
not create, alter, reclassify, or otherwise modify repository invariants.

- `../../evidence/authoritative` identifies binding repository evidence that governs
  an initiative specification or product decision. It is the current repository
  label for the former `invariants` classification. An initiative may cite it
  but cannot modify it.
- `../../evidence/non-authoritative` identifies contextual, exploratory, or
  supporting repository evidence. It may inform a decision but cannot by itself
  override `../../evidence/authoritative`.
- A **product** is output material placed in a declared destination. It can be
  executable code, a script, an SDK, an API, product documentation, or another
  deliverable. A document is an **initiative specification** when it defines
  what a product must do; classify it by its role, not its file extension.

## Initiative type and output boundary

Set `{{initiative_type}}` to exactly one of these types and follow its boundary:

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
is normally classified `../../evidence/non-authoritative` until an explicit owning
authority accepts it as `../../evidence/authoritative`; that acceptance affects the
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

## Products and placement

Record every product output and its destination. A destination can be a
repository path, package, API route, documentation site, or another explicit
placement; it does not need to be a directory named `products`.

| Product | Form | Destination | Governing specification | Verification |
|---|---|---|---|---|
| {{product_name}} | {{code_script_sdk_api_or_documentation}} | {{repository_path_or_public_placement}} | {{specification_link_or_na}} | {{test_review_or_other_evidence}} |

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
   specification, ownership boundaries, `../../evidence/authoritative`, and failure
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
[readiness template](implementation-readiness.md) provides the response shape
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

## Human decision receipts

Create `decision-receipts` from the shared templates when the first explicit
human decision is received. Create one receipt for each assumption disposition,
open-question answer, lifecycle decision, or invariant exception. Preserve the
exact prompt and exact response, link the receipt from its source record, and
commit it with the records reconciled from that decision. A receipt proves the
decision only; it does not prove implementation or verification.

## Reusable prompts

Use the [coverage and use map](../TEMPLATE-COVERAGE.md) to select the canonical
source and destination for each required file or embedded section. It includes
conditional later records, stage ownership, evidence inputs, and verification.
Prepare only the prerequisites needed by the invoked activity under the
[shared contract](../prompts/WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation),
without recursively executing linked prompts. Reuse existing records and
preserve stable IDs, human text, accepted baselines, source identities, and
history. Missing authority, identity, facts, or passing verification remain
blockers after documentary recovery.

[Initiative prompts](../prompts/README.md) contains reusable prompts for initiative
reviews and creation. It follows this sequence:

0. [prepare initiative](../prompts/00_initiative_preparation.md)
1. [proposal creation](../prompts/01_proposal_creation.md)
2. [proposal alignment](../prompts/02_proposal_alignment.md)
3. [initiative creation](../prompts/03_initiative_creation.md)
4. [initiative-to-precedent alignment](../prompts/04_initiative_alignment.md)
5. [initiative assumption confirmation review](../prompts/05_initiative_assumption_review.md)
6. [initiative open-question resolution review](../prompts/06_initiative_open_question_review.md)
7. [initiative acceptance](../prompts/07_initiative_acceptance.md)
8. [initiative SDK/API alignment](../prompts/08_initiative_sdk_api_alignment.md), for implementation when applicable
9. [initiative implementation-readiness review](../prompts/09_initiative_implementation_readiness_review.md), for implementation
10. [implementation execution](../prompts/10_initiative_execution.md), for implementation
11. [design delivery](../prompts/11_design_delivery.md), for design
12. [planning delivery](../prompts/12_planning_delivery.md), for planning
13. [finalize initiative](../prompts/13_initiative_finalization.md).

Add future prompts to that directory and its README; prompts guide review,
while documented source precedence and repository evidence continue to govern
the outcome.

## Repository baseline

<!--
Summarize only the existing contracts that materially constrain the proposal.
Link to code, accepted architecture, and dependent initiatives where useful.
-->

- {{existing_contract_or_constraint}}
- {{existing_contract_or_constraint}}
- {{existing_contract_or_constraint}}

## Intended outcome

<!-- Describe observable behavior after the initiative is complete. -->

{{intended_outcome}}

## Scope

### Included

- {{included_capability}}
- {{included_capability}}

### Excluded

- {{excluded_capability_and_reason}}
- {{excluded_capability_and_reason}}

## Dependencies

| Initiative or contract | Relationship | Required state |
|---|---|---|
| {{dependency}} | {{how_this_initiative_depends_on_or_changes_it}} | {{required_state}} |

## Readiness

| Area | Current evidence | Required before the next initiative output |
|---|---|---|
| Product direction | {{evidence_or_gap}} | {{review_or_decision}} |
| Repository fit | {{evidence_or_gap}} | {{review_or_decision}} |
| Data and migration | {{evidence_or_gap}} | {{review_or_decision}} |
| Operations and recovery | {{evidence_or_gap}} | {{review_or_decision}} |
| Verification | {{evidence_or_gap}} | {{test_or_acceptance_gate}} |

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

<!--
Append one row for every transition. Preserve earlier truthful entries. Link
the decision receipt, execution record, or completion evidence that permits the
transition. Use `Initial` for the prior state of the first Proposed entry.
-->

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| {{yyyy-mm-dd_or_event}} | Initial | Proposed | {{proposal_or_human_instruction_link}} | {{revision_or_initial}} | {{reason_and_scope}} | {{commit_or_pending}} |

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
authorized. `../../evidence/non-authoritative` may explain ambiguity or support a
decision, but cannot supersede `../../evidence/authoritative`.


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
| {{suite_id}} | [{{suite_id}}]({{relative_suite_path}}) | {{note_id}} | {{source_scope}} | [{{note_id}}]({{relative_note_path}}) | {{originating_or_contributing_append_revision_reopening_new_or_successor}} | {{routing_receipt_link}} |

Retain exact originating and later contributing notes independently. Each row
links its source suite and note and the per-source fit/authority record. Source
scope may differ from target scope without relabeling either identity.

Any absent historical dedicated ref retains its exact immutable Historical
branch tip and separately authorized Branch removal evidence. That removal
receipt records Human authority and exact Branch; removing a ref never frees
its identity for unrelated work or qualifies a new cycle.
