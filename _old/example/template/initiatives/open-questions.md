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
intent in [assumption.md](assumption.md). Recommendations are proposed defaults
until a reviewer records an accepted decision. Accepted answers must be
reconciled into [architecture.md](architecture.md),
[source-mapping.md](source-mapping.md),
[implementation-roadmap.md](implementation-roadmap.md), and
[implementation-steps.md](implementation-steps.md) in the same change.

**Human ownership:** When the repository's
[project ownership convention]({{project_profile_path}})
applies, `Owner` identifies a role fulfilled by the Sole Project Owner. Do not
make human-owner assignment or review a separate gate; preserve component,
profile, external-party, and evidence dependencies.

## Status vocabulary

- `Open, blocking`: the initiative cannot safely produce its permitted output
  for the affected contract.
- `Open`: a decision is needed before the phase named in `Blocks`.
- `Proposed; confirm`: a recommendation exists and needs explicit review.
- `Accepted YYYY-MM-DD`: the recorded decision governs the initiative's
  type-specific work.
- `Deferred`: the capability is outside current scope and has a re-entry
  condition.
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
3. Record the selected decision, rationale, owner, and date without rewriting
   the original question.
4. Update the register status and reconcile every affected initiative document
   in the same change.
5. Link product, specification, or evidence verification when the decision is
   first exercised.
