<!--
This directory holds reusable prompts for initiatives. It currently contains
eleven prompts, numbered 0 through 10, that follow the initiative workflow.
Add other focused initiative prompts here as the protocol gains new review
needs.
-->

# Initiative prompts

Use these prompts to review and reconcile initiative material. Each prompt
addresses a specific task; additional prompts can be added here as they are
defined.

Every numbered prompt applies the mandatory
[initiative workflow contract](WORKFLOW-CONTRACT.md). The contract centralizes
shared evidence, authority, scope, human-decision, Git, lifecycle, and reporting
rules. It does not replace or shorten a prompt's stage-specific preconditions,
edit boundary, verification, or reporting requirements.

After stage 0 prepares an initiative, run every initiative-specific prompt on
that initiative's prepared branch. Only the preparation prompt creates or
switches the branch; later prompts stop when the active branch does not match
the initiative.

## Example request

> Using the [proposal alignment prompt](02_proposal_alignment.md), align the
> attached initiative's proposal in place. Do not create, copy, or change any
> other document or directory.

Unless a prompt explicitly says otherwise, use it only on its named existing
target and make changes in place. Prompts must not scaffold, copy, or create
template, proposal, assumption, or initiative documents.

Apply the ownership and approval convention in the target project's profile.
It resolves human owner, reviewer, and approver roles as recorded by that
project; it never removes a technical component, profile, placement,
external-party, contract, artifact, or evidence gate.

The preparation, proposal-creation, initiative-creation, initiative-execution,
and finalization prompts are the explicit exceptions. Preparation may create or
switch to an initiative branch and create only a missing directory-and-README
skeleton; it preserves an existing initiative tree. Proposal creation may
create only its target `proposal/proposal.md`. Initiative creation may complete
the standard initial initiative record and its parent tracking entries.
Initiative execution applies only to an `implementation` initiative. It may
create the accepted initiative's planned product artifacts and required
evidence, reconcile every ledgered in-repository product dependency needed for
authoritative-evidence-first alignment, and update execution and status records
to the result actually verified. It uses the standard `execution-record.md` and
`completion-evidence.md` records and may set `Completed` only when all in-scope
gates pass. Design and planning initiatives also require the standard
`completion-evidence.md` record before completion. Finalization verifies that already-aligned completion
state, commits any remaining accepted work, pushes the initiative branch, and
creates its pull request; it does not declare an incomplete execution complete.
The implementation-readiness review prompt is read-only and applies only to an
`implementation` initiative: it gathers and reports evidence without changing
its target.

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
| 0 | [Prepare initiative](00_initiative_preparation.md) | Giving a new or existing initiative its own branch and, only when needed, its minimal README skeleton. |
| 1 | [Proposal creation](01_proposal_creation.md) | Creating the first, proposal-only record for a new initiative from an existing realization note. |
| 2 | [Proposal alignment](02_proposal_alignment.md) | Aligning an existing initiative proposal in place to its scope, repository evidence, active initiatives, `../../evidence/authoritative`, and implemented work. |
| 3 | [Initiative creation](03_initiative_creation.md) | Creating the first complete initiative record from an initiative's existing proposal, the shared templates, and repository evidence. |
| 4 | [Initiative-to-precedent alignment](04_initiative_alignment.md) | Aligning a fully documented initiative as a whole to governing evidence and established precedent before any human confirmation or SDK/API work. |
| 5 | [Initiative assumption confirmation review](05_initiative_assumption_review.md) | Guiding a human through every unresolved assumption one at a time and reconciling each explicit response within the initiative. |
| 6 | [Initiative open-question resolution review](06_initiative_open_question_review.md) | Guiding a human through every active open question one at a time and reconciling each explicit answer within the initiative. |
| 7 | [Initiative SDK/API alignment](07_initiative_sdk_api_alignment.md) | For an `implementation` initiative, aligning applicable existing SDKs and APIs to the confirmed specifications through compatible, precedent-preserving product changes, or reporting conflicts. |
| 8 | [Initiative implementation-readiness review](08_initiative_implementation_readiness_review.md) | For an `implementation` initiative, comparing current evidence against its accepted specifications immediately before product execution, then reporting a phase-specific readiness result. |
| 9 | [Initiative execution](09_initiative_execution.md) | For an `implementation` initiative, aligning products to accepted specifications and recording verification evidence. |
| 10 | [Finalize initiative](10_initiative_finalization.md) | Verifying an executed initiative's aligned completion records, committing any remaining accepted work, pushing its branch, and opening its pull request. |

