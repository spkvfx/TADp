<!--
Replace every double-brace token. Assign stable {{decision_prefix}}-xx IDs in order
and never reuse an ID. Keep accepted and deferred entries so later documents
retain their decision history.
-->

# {{initiative_name}} open questions and decisions

**Initiative:** {{initiative_name}}
**Status:** Open
**Last updated:** {{date}}

This register separates unresolved design choices from the high-confidence
intent in [assumption.template.md](assumption.template.md). Recommendations are proposed defaults
until an exact sufficiently authorized disposition is recorded. Accepted answers must be
reconciled into [architecture.template.md](architecture.template.md),
[source-mapping.template.md](source-mapping.template.md),
[implementation-roadmap.template.md](implementation-roadmap.template.md), and
[implementation-steps.template.md](implementation-steps.template.md) in the same change.

**Human ownership:** When the repository's
[project ownership convention]({{project_profile_path}})
applies, `Owner` identifies its actual recorded role or delegate. Avoid redundant
personnel approval within sufficient authority; preserve component, profile,
external-party, target and evidence dependencies. One project's owner does not
thereby acquire another project's decision or write authority.

## Discovery and canonical ownership

Either numbered review may independently define new questions and assumptions
from human input or evidence without a preceding answer, correction or existing
source ID. Give each new item its own stable ID, exact source text and origin;
keep it unresolved until its own sufficient disposition exists. A human may
answer outside the original options or reviewed initiative's scope. Assess the
answer's authority and proper destination rather than rejecting it for scope.

This register owns this initiative's questions. Another named initiative owns
its canonical items; project-wide items or items with no suitable initiative
owner use the conditional [project register](../decisions/assumptions-and-open-questions.template.md)
through the coverage map. Link the originating initiative's effect/dependency
instead of importing external work. Before an external record edit, identify
its exact target/current state, owner, governing revision, branch and sufficient
write/decision authority. If sufficient, record the item and authorized answer
there without redundant approval solely for outside-initiative ownership.
Otherwise preserve exact input and an owned unresolved handoff with proposed
owner, blocker and re-entry condition. Separate scaffolds, repositories, forks
and services retain their target-naming authority boundary.

## Status vocabulary

- `Open, blocking`: the initiative cannot safely produce its permitted output
  for the affected contract.
- `Open`: a decision is needed before the phase named in `Blocks`.
- `Proposed; confirm`: a recommendation exists and needs explicit review.
- `Accepted YYYY-MM-DD`: the exact recorded disposition governs this item
  within its stated authority; resulting work retains its separate gates.
- `Deferred`: an explicit authorized deferral retains its owner and re-entry
  condition; silence or a dependency alone is not deferral.
- `Superseded by {{decision_prefix}}-xx`: a later decision replaces the entry.

## Decision register

| ID | Decision | Recommendation | Status | Blocks |
|---|---|---|---|---|
| {{decision_prefix}}-01 | {{decision_needed}} | {{recommended_direction}} | Open, blocking | {{affected_phase_or_contract}} |
| {{decision_prefix}}-02 | {{decision_needed}} | {{recommended_direction}} | Open | {{affected_phase_or_contract}} |

## Earliest blocking decisions

1. `{{decision_prefix}}-01` - {{why_this_must_be_decided_first}}.
2. `{{decision_prefix}}-02` - {{dependency_or_cost_of_delay}}.

## {{decision_prefix}}-01 - {{decision_title}}

**Question:** {{precise_question_with_mutually_exclusive_outcomes}}

**Original source:** {{exact_source_path_locator_revision_or_event}}

**Originating review or evidence:** {{review_identity_or_evidence_link_without_requiring_a_prior_answer}}

**Canonical owner and location:** {{actual_owner_and_canonical_register_link}}

**Scope classification:** {{in_scope_cross_initiative_or_project_wide}}

**Dependencies and re-entry trigger:** {{stable_dependency_IDs_and_trigger_or_none}}

**Context and evidence:** {{repository_evidence_constraints_and_users_affected}}

**Options:**

1. {{option_and_consequence}}
2. {{option_and_consequence}}
3. {{option_and_consequence}}

**Recommendation:** {{recommended_option_and_reason}}

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** {{decision_owner}}

**Decision date:** -

**Disposition evidence:** {{unresolved_or_exact_receipt_link_and_actual_human_or_delegated_author_method}}

**Owned handoff, if blocked:** {{exact_preserved_input_proposed_owner_blocker_and_reentry_or_none}}

**Acceptance:** {{facts_contracts_tests_or_documents_the_decision_must_define}}

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

<!-- Duplicate the complete decision section for every register row. -->

## Decision dependencies

| Decision | Depends on | Unblocks |
|---|---|---|
| {{decision_prefix}}-01 | {{decision_or_evidence_or_none}} | {{decisions_phases_or_contracts}} |

## Decision process

1. Confirm the current repository evidence and affected owner boundaries.
2. Compare viable options against the proposal, assumptions,
   compatibility requirements, and failure behavior.
3. Present one ready item at a time on the ordinary human path. Either review
   may record a question or assumption's own authorized answer in that same
   review. Capture exact human words/authority in a linked receipt before
   changing source disposition. Preserve the original question/options and
   append the selected decision, rationale, owner and event.
4. Update the register status and reconcile every affected initiative document
   in the same change.
5. Link product, specification, or evidence verification when the decision is
   first exercised.

A specifically authorized alternative method applies only to its covered IDs
after authority receipt and rule-specific exception. Record actual agent
authorship, method, evidence, result and limits; never invent a human response
or let a new ID inherit delegation. One response covers multiple IDs only when
it explicitly and unambiguously identifies the complete set and outcomes.

Defining an assumption during this review does not resolve it. Answering a
question does not confirm a separate derived assumption: retain its exact text
and give it its own sufficient disposition, which may occur in the same review.
Preserve prior texts/options, receipts, settled decisions and dormant triggers;
append replacements and supersession links instead of silently rewriting history.

Report original/new item coverage, canonical owners, actual answers, unresolved
and deferred items, transferred dependencies and blocked handoffs. A pending
external matter need not become an in-scope deliverable or falsely prevent a
bounded coverage report, but its applicable blocking dependency still blocks
the affected handoff. Recording a decision does not accept an initiative,
implement its consequences, revise a protected invariant or reopen a closed
claim. Preserve conflict, split, reopening and renewed-acceptance requirements.
