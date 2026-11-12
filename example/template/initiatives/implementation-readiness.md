<!--
This is an execution-stage template for an `implementation` initiative, not a
standard initial initiative artifact.
Do NOT copy or create it when creating an initiative. Create an initiative-local
implementation-readiness.md later, immediately before execution begins, and
replace every double-brace token. Remove instructional comments before review.
Use the shared `prompts/09_initiative_implementation_readiness_review.md`
to gather and report the evidence comparison before this document is created in
a separately scoped documentation change.

The review makes a phase-specific implementation-entry decision from current
evidence. It does not replace the initiative record, authorize unplanned work,
or prove release, deployment, or operational readiness.
-->

# {{initiative_name}} implementation-readiness review

- **Initiative:** {{initiative_name}}
- **Work version:** {{v_major_minor}}
- **Realization suite:** {{realization_suite_id_and_link}}
- **Canonical correlation:** {{initiative_index_row_link}}
- **Dedicated branch and captured base:** {{branch_base_and_commit}}
- **Review date:** {{date}}
- **Reviewed phase or scope:** {{phase_or_execution_scope}}
- **Initiative disposition:** {{accepted_initiative_state}}
- **Implementation disposition:** **{{go_no_go_or_conditional_disposition}}**

**Human ownership:** Apply the ownership and approval convention recorded in
`{{project_profile_path}}`. Human roles resolve as recorded there; selected
technical components, contracts, environments, artifacts, and evidence remain
readiness gates.

This review is not applicable to a `design` or `planning` initiative. Those
initiative types deliver specifications or evidence, not product
implementation.

## Review purpose and decision

<!--
State what product-execution decision this review makes. Distinguish accepted
directions from the concrete owners, specifications, environments, artifacts,
and verification evidence needed to begin the reviewed work safely. State the
exact phase or change set this decision covers.
-->

{{review_purpose_and_phase_specific_decision}}

This decision applies only to {{phase_or_execution_scope}}. It must not be
used to claim {{unapproved_phase_release_deployment_or_operational_claim}}.

## Evidence reviewed

<!--
Use current, linked evidence. Include the initiative suite, accepted decisions,
repository baseline, dependencies and owners, relevant contracts, operational
constraints, and verification/environment evidence. Do not treat a proposal,
recommendation, or unconfirmed assumption as accepted evidence.
-->

| Area | Evidence | Finding | Readiness effect |
|---|---|---|---|
| Governing sources and precedence | {{sources_and_precedence_links}} | {{finding}} | {{effect_on_entry_decision}} |
| Initiative record and accepted decisions | {{initiative_record_and_decision_links}} | {{finding}} | {{effect_on_entry_decision}} |
| Correlation identity and Git traceability | {{canonical_row_suite_initiative_branch_and_base_links}} | {{finding}} | {{effect_on_entry_decision}} |
| Repository and product baseline | {{repository_or_product_evidence}} | {{finding}} | {{effect_on_entry_decision}} |
| Dependencies, owners, and external contracts | {{dependency_owner_or_contract_evidence}} | {{finding}} | {{effect_on_entry_decision}} |
| Security, operations, recovery, and migration | {{operational_evidence_or_gap}} | {{finding}} | {{effect_on_entry_decision}} |
| Verification and execution environment | {{test_fixture_or_environment_evidence}} | {{finding}} | {{effect_on_entry_decision}} |

## Accepted directions versus execution inputs

<!--
For every accepted specification direction that affects the reviewed work, identify the
concrete input or evidence still needed. A specification decision alone does not
authorize implementation when an owner, contract, environment, migration,
security, recovery, or verification input is missing.
-->

| Decision or direction | Accepted specification direction | Input or evidence still required | Earliest affected phase or step |
|---|---|---|---|
| {{decision_id}} | {{accepted_direction}} | {{missing_input_or_evidence_or_not_applicable}} | {{phase_or_step}} |

## Phase and work readiness

<!--
Assess the reviewed phase and every dependent phase or work item. Use precise
statuses such as Ready, Conditional, Blocked, Deferred, Implemented and
verified, or Not applicable. Explain the evidence rather than implying a
general release or deployment claim.
-->

| Phase or work item | Status | Reason and required gate |
|---|---|---|
| {{phase_or_step}} | {{status}} | {{evidence_or_remaining_gate}} |

## Required order of work

<!--
List the minimum dependency order for the reviewed execution. Include named
owners, decision/input completion, scope limits, tests, and evidence gates
where they are prerequisites. Keep deferred or out-of-scope work visible.
-->

1. {{first_prerequisite_or_authorized_step}}
2. {{next_prerequisite_or_authorized_step}}
3. {{verification_or_release_gate}}

## Entry constraints and scope limits

<!--
State the `evidence/authoritative` requirements, ownership boundaries,
compatibility, migration, rollback,
security, recovery, and environment limits that the work must preserve. List
explicitly what the decision does not authorize.
-->

- {{constraint_or_authoritative_evidence}}
- {{constraint_or_authoritative_evidence}}
- **Not authorized by this review:** {{out_of_scope_or_unmet_claim}}

## Prompt blocks and exception boundaries

{{source_prompt_revision_block_settings_exception_links_and_actual_gate_outcomes_or_none}}

Distinguish the observed readiness finding from separately authorized permission
to perform bounded work under an exception. A waived or unperformed gate is
not ready or passed; preserve failures, missing evidence, owners, and re-entry
conditions. A read-only readiness review creates no persistent exception record.
For preview work, draft records remain response-only. Identify independent
review findings and their disposition where required; retain locks and all
unexcepted obligations.

## Conclusion and next action

<!--
Give a concise, evidence-backed go/no-go or conditional conclusion. Identify
the exact next action, owner, and evidence needed to remove any blocker. Do not
upgrade an initiative lifecycle, release, or deployment claim unless the
reviewed evidence supports it.
-->

{{conclusion_and_next_action}}

## Documentation verification

<!--
Record only checks actually performed after the review is written. Add the
review to the initiative README at this point, rather than during initiative
creation, and update initiative status only when the evidence changes it.
-->

- [ ] {{documentation_or_link_check}}
- [ ] {{cross_record_consistency_check}}
- [ ] {{diff_or_required_verification_check}}
