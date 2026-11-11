<!--
Use this file when the proposal is authored in the repository. If an external
artifact is the canonical proposal, retain this file as an index and concise
summary that points to that artifact. Replace every double-brace token.
-->

# {{initiative_name}} proposal

**Initiative:** {{initiative_name}}  
**Proposal status:** Draft  
**Revision:** {{proposal_revision}}  
**Last updated:** {{date}}  
**Owner:** {{proposal_owner}}  
**Initiative type:** `{{initiative_type}}`  
**Work version:** {{v_major_minor}}
**Realization suite:** [{{realization_suite_id}}]({{relative_realization_suite_index_path}})
**Type requirements:** See [the initiative template](../README.md#initiative-type-and-output-boundary).

## Executive proposal

<!-- State the requested decision, intended result, and why it matters. -->

{{executive_proposal}}

## Initiative type and permitted output

State the selected initiative type and its permitted output. An
`implementation` initiative proposes product changes only; a `design`
initiative proposes specification changes based on existing products without
creating a new product; and a `planning` initiative proposes evidence for other
initiatives only.

{{initiative_type_and_output_boundary}}

## Problem and evidence

<!-- Describe observed behavior, affected users or systems, and evidence. -->

{{problem_and_evidence}}

## Intended outcomes

1. {{measurable_or_observable_outcome}}
2. {{measurable_or_observable_outcome}}
3. {{measurable_or_observable_outcome}}

## Scope

### Included

- {{included_capability}}
- {{included_capability}}

### Excluded

- {{excluded_capability_and_reason}}
- {{excluded_capability_and_reason}}

## Users and stakeholders

| Stakeholder or affected party | Need or responsibility | Expected change |
|---|---|---|
| {{user_or_stakeholder}} | {{need_or_responsibility}} | {{expected_change}} |

## Terms

| Term | Meaning in this proposal |
|---|---|
| {{term}} | {{definition}} |

## Proposed direction

### Product behavior or placement

{{product_behavior}}

### Domain and authority model

{{domain_and_authority_model}}

### System boundaries

{{system_boundaries}}

### Primary workflows

1. {{workflow_step}}
2. {{workflow_step}}
3. {{workflow_step}}

### Data and lifecycle

{{data_ownership_identity_lifecycle_and_retention}}

## Operational behavior

### Failure and recovery

{{failure_modes_recovery_and_idempotency}}

### Security and authorization

{{trust_permissions_secrets_and_audit}}

### Observability

{{logs_metrics_traces_and_operator_views}}

## Compatibility and transition

{{migration_rollout_coexistence_and_removal_plan}}

## Alternatives considered

| Alternative | Benefit | Cost or reason not selected |
|---|---|---|
| {{alternative}} | {{benefit}} | {{cost_or_rejection_reason}} |

## Risks and tradeoffs

| Risk or tradeoff | Impact | Mitigation or evidence needed |
|---|---|---|
| {{risk_or_tradeoff}} | {{impact}} | {{mitigation_or_evidence}} |

## Assumptions requiring assumption

<!-- These become stable {{decision_prefix}}-Axx rows in ../assumption.md. -->

- {{high_confidence_assumption}}
- {{high_confidence_assumption}}

## Questions requiring decisions

<!-- These become stable {{decision_prefix}}-xx entries in ../open-questions.md. -->

- {{open_decision}}
- {{open_decision}}

## Acceptance outcomes

- {{observable_acceptance_outcome}}
- {{observable_acceptance_outcome}}

## References

- {{reference_and_relevance}}

## Revision history

| Revision | Date | Owner | Change |
|---|---|---|---|
| {{proposal_revision}} | {{date}} | {{proposal_owner}} | Initial proposal |
