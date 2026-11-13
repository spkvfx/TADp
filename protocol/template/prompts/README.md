<!--
This directory holds reusable prompts for initiatives. It currently contains
fourteen prompts, numbered 0 through 13, that follow the initiative workflow.
Add other focused initiative prompts here as the protocol gains new review
needs.
-->

# Initiative prompts

Apply the canonical
[prompt keyword specification](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
when interpreting these prompts and ordinary TADp requests. Its registry owns
recognized directives and extensions; this library does not define aliases.
The shared contract explains how bounded exception records qualify the ordinary
gate path without changing lifecycle meanings, lock protection, or evidence.
The numbered stage map below is a reference inventory, not an action list.

Use these prompts to review and reconcile initiative material. Each prompt
addresses a specific task; additional prompts can be added here as they are
defined.

Every numbered prompt applies the mandatory
[initiative workflow contract](WORKFLOW-CONTRACT.md). The contract centralizes
shared evidence, authority, scope, human-decision, Git, lifecycle, and reporting
rules. It does not replace or shorten a prompt's stage-specific preconditions,
edit boundary, verification, or reporting requirements.

The binding stage sequence and handoff rules are defined by the
[authoritative initiative workflow specification](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md).
Stages 0 through 7 are the common path. An accepted initiative then follows
exactly one type-specific delivery path before stage 13 finalization.

Stage 0 assesses realization fit before allocation, records each delegated
routing/reopening choice, and selects dedicated or shared scope execution.
Later stages verify membership, provenance, current revision assignment and
captured base. Existing complete initiatives reuse records and return through
alignment/decisions/renewed acceptance rather than new-initiative creation.
New initiatives are grouped at initiatives/<scope>/<type>/<id-and-slug>/.
## Example request

> Using the [proposal alignment prompt](02_proposal_alignment.md), align the
> attached initiative's proposal in place after preparing any constructible
> documentary prerequisites through their owning stages.

Unless a prompt explicitly says otherwise, use it only on its named existing
target. Before its substantive step, apply the shared contract's
[documentary prerequisite preparation](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation)
to that prompt's explicit prerequisite inventory and the
[canonical coverage and use map](../TEMPLATE-COVERAGE.md). Recover only
necessary documentary inputs from sufficient scoped evidence through their
owning preparation activities after their actual entry gates hold. The
substantive step's in-place edit limits follow this preparation; missing
paperwork alone does not block recoverable inputs. Missing facts, immutable
identity, actual decisions, authority and verification still block affected
work. This permission cannot scaffold an invented target or edit reusable
templates, execute linked prompts, or manufacture an earlier gate.

Apply the ownership and approval convention in the target project's profile.
It resolves human owner, reviewer, and approver roles as recorded by that
project; it never removes a technical component, profile, placement,
external-party, contract, artifact, or evidence gate.

The preparation, proposal-creation, initiative-creation, acceptance,
type-specific delivery, and finalization prompts are the explicit exceptions.
Preparation may register scopes/ancestors and independent source routing,
record necessary reopening under the adopted intake method, select/reuse a
shared scope branch or create a dedicated child, and prepare new member
correlation and minimal README skeletons. Existing targets retain their records. Proposal creation may
create only its target `proposal/proposal.md`. Initiative creation may complete
the standard initial initiative record and its parent tracking entries.
Acceptance may create the acceptance receipt and reconcile the accepted
baseline and lifecycle tracking, but it creates no delivery output.
Implementation execution applies only to an `implementation` initiative. It may
create the accepted initiative's planned product artifacts and required
evidence, reconcile every ledgered in-repository product dependency needed for
authoritative-evidence-first alignment, and update execution and status records
to the result actually verified. It uses the standard `execution-record.md` and
`completion-evidence.md` records and may set `Completed` only when all in-scope
gates pass. Design delivery may change only accepted specification destinations
and supporting initiative evidence. Planning delivery may create only accepted
initiative-local evidence. Both use `delivery-record.md`, and every type
requires `completion-evidence.md` before completion. Finalization verifies that already-aligned completion
state, commits remaining traceable accepted work, and performs authorized local
initiative-to-scope integration or records verified direct scope placement.
It never declares incomplete delivery complete or closes its scope.
The implementation-readiness assessment is read-only and applies only to an
`implementation` initiative. Its preceding prerequisite preparation may recover
documentary records through their owning stages; disclose those changes, then
capture an assessment baseline and verify no file changes during assessment.
Its canonical template is a response shape, not a required durable readiness
file. Reconstructed paperwork does not prove phase readiness.

Each prompt declares its documentary prerequisites, canonical record IDs,
scoped evidence, preparation boundary, genuine blockers and post-preparation
validation. Records and required embedded sections retain one owner. Stages
5 through 7 may capture already sufficient exact human instructions without
repeating the decision; otherwise their human gates remain open. Delivery,
verification, completion and integration records require actual events, not
plausible reconstruction. Repeated invocations reuse valid records and receipts
without overwriting customization, changing claims or creating duplicates.

Every prompt template must include an **Example usage** section. The example
must link to the template's specific Markdown file inline. Mark the example as
reference-only and identify the template's actual prompt block as the only
executable instruction, so an example cannot recursively trigger work.

## Evidence and authority handling

Every prompt must preserve cited evidence. `../../evidence/authoritative` is
invariant and binding; it defines conditions that initiatives and products must
meet. `../../evidence/non-authoritative` supplies clues and support for decisions,
but cannot supersede authoritative evidence. A realization is a proposal input,
not an accepted requirement. An accepted initiative and its products are
authoritative within their respective claims and must remain mutually coherent.

## Prompt sequence

| # | Prompt | Use it when |
|---|---|---|
| 0 | [Prepare initiative](00_initiative_preparation.md) | Assessing realization fit; recording append, coherent revision, reopening or new targets, scopes/ancestors and dedicated/shared execution assignments. |
| 1 | [Proposal creation](01_proposal_creation.md) | Creating the first proposal-only record from the correlated realization suite and its intended note. |
| 2 | [Proposal alignment](02_proposal_alignment.md) | Aligning an existing initiative proposal in place to its scope, repository evidence, active initiatives, `../../evidence/authoritative`, and implemented work. |
| 3 | [Initiative creation](03_initiative_creation.md) | Creating the first complete initiative record from an initiative's existing proposal, the shared templates, and repository evidence. |
| 4 | [Initiative-to-precedent alignment](04_initiative_alignment.md) | Aligning a fully documented initiative as a whole to governing evidence and established precedent before any human confirmation or SDK/API work. |
| 5 | [Initiative assumption confirmation review](05_initiative_assumption_review.md) | Guiding a human through every unresolved assumption one at a time and reconciling each explicit response within the initiative. |
| 6 | [Initiative open-question resolution review](06_initiative_open_question_review.md) | Guiding a human through every active open question one at a time and reconciling each explicit answer within the initiative. |
| 7 | [Initiative acceptance](07_initiative_acceptance.md) | Presenting the exact coherent proposed baseline for explicit human acceptance and recording the accepted revision and lifecycle transition. |
| 8 | [Initiative SDK/API alignment](08_initiative_sdk_api_alignment.md) | For an accepted `implementation` initiative, aligning applicable existing SDKs and APIs through compatible, precedent-preserving product changes, or reporting conflicts. |
| 9 | [Initiative implementation-readiness review](09_initiative_implementation_readiness_review.md) | For an accepted `implementation` initiative, comparing current evidence against its specifications immediately before product execution, then reporting a phase-specific readiness result. |
| 10 | [Implementation execution](10_initiative_execution.md) | For an `implementation` initiative, aligning products to accepted specifications and recording execution and verification evidence. |
| 11 | [Design delivery](11_design_delivery.md) | For a `design` initiative, delivering accepted specification changes and their verification without modifying products. |
| 12 | [Planning delivery](12_planning_delivery.md) | For a `planning` initiative, delivering accepted initiative-local evidence while preserving source classifications and limitations. |
| 13 | [Finalize initiative](13_initiative_finalization.md) | Verifying completion, finalizing traceable commits, and recording authorized immediate-parent integration or direct placement. |


[Scope closure](scope_closure.md) is a distinct operation for patch/minor/major
integration; it is not another initiative type or stage. Closing a member does
not close scope or ancestors. Pull requests are independently human-managed;
these prompts neither solicit nor prepare/create them, and require no URL or
hosting connection. Pushes remain separately authorized.
