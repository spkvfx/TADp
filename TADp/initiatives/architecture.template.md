<!--
Replace every double-brace token. Base claims about the current repository on
specific code, tests, configuration, accepted architecture, or operating
evidence. State "Not applicable" with a reason when a standard section does
not apply.
-->

# {{initiative_name}} architecture and specification

**Initiative:** {{initiative_name}}  
**Status:** Proposed  
**Last updated:** {{date}}

Related documents:

- [Initiative index](initiative-README.template.md)
- [Proposal sources](proposal/README.template.md)
- [Assumption review](assumption.template.md)
- [Evidence mapping](source-mapping.template.md)
- [Open questions and decisions](open-questions.template.md)
- [Delivery roadmap](implementation-roadmap.template.md)
- [Detailed delivery steps](implementation-steps.template.md)

## Proposal standing

<!--
Explain how the proposal relates to this repository-specific design and which
decisions must be accepted before statements become architectural contracts.
-->

{{proposal_standing}}

## Specification boundary

For an `implementation` or `design` initiative, this document is a
specification. An `implementation` initiative uses the accepted specification
to align products and must not modify an existing specification. A `design`
initiative may create or modify this specification to align it with observed
products. For a `planning` initiative, this document is an evidence-boundary
record only: it must not introduce or modify a specification, and it must state
`Not applicable` for specification sections that do not apply.

## Current repository baseline

<!-- Describe the current behavior before proposing new types or systems. -->

| Area | Current contract or evidence | Consequence for this initiative |
|---|---|---|
| {{area}} | {{code_test_document_or_observed_behavior}} | {{constraint_or_extension_point}} |
| {{area}} | {{code_test_document_or_observed_behavior}} | {{constraint_or_extension_point}} |

## Goals and non-goals

### Goals

1. {{goal}}
2. {{goal}}
3. {{goal}}

### Non-goals

- {{non_goal_and_boundary}}
- {{non_goal_and_boundary}}

## Terms and identity

| Term or identity | Definition | Authority or lifecycle |
|---|---|---|
| {{term_or_identity}} | {{definition}} | {{authority_or_lifecycle}} |

State which identifiers are stable, which fields may change, where identity is
created, and how duplicate or stale identity is rejected.

## Architectural decisions

| Decision ID | Direction used by this design | Status |
|---|---|---|
| {{decision_prefix}}-01 | {{decision_summary}} | {{open_proposed_or_accepted}} |

The detailed rationale, alternatives, owner, and acceptance conditions remain
in [open-questions.template.md](open-questions.template.md). This section states only the design
direction that the architecture currently applies.

## Boundaries and ownership

| Component or package | Responsibility | Authoritative state | Must not own |
|---|---|---|---|
| {{component_or_package}} | {{responsibility}} | {{authoritative_state}} | {{excluded_responsibility}} |

Document dependency direction, control-plane and data-plane boundaries, and
which package or service validates every externally supplied command.

## Domain model and evidence/authoritative

<!-- Define new and changed domain values before persistence or API shapes. -->

### Model

{{domain_model_and_relationships}}

### Binding requirements

- {{authoritative_evidence_or_requirement}}
- {{authoritative_evidence_or_requirement}}

Classify the source for each binding requirement as
`../../evidence/authoritative` in [source-mapping.template.md](source-mapping.template.md). Contextual
or exploratory material belongs in `../../evidence/non-authoritative` and may not
supersede a binding requirement.

## State and persistence

| State | Durable source | Live or derived state | Write owner | Recovery rule |
|---|---|---|---|---|
| {{state}} | {{durable_source}} | {{projection_or_none}} | {{write_owner}} | {{recovery_rule}} |

Describe transaction boundaries, concurrency or fencing, idempotency keys,
retention, schema evolution, and how derived state is rebuilt.

## Primary workflows

### {{workflow_name}}

**Preconditions:** {{preconditions}}

1. {{ordered_step}}
2. {{ordered_step}}
3. {{ordered_step}}

**Success result:** {{success_result}}

**Failure result:** {{failure_result_and_recovery_owner}}

<!-- Duplicate the workflow section for every materially different path. -->

## Interfaces and integration

| Interface | Producer or caller | Consumer or handler | Compatibility rule |
|---|---|---|---|
| {{command_event_protocol_or_api}} | {{producer}} | {{consumer}} | {{versioning_idempotency_or_ordering_rule}} |

Define payload limits, acknowledgement meaning, timeouts, retry ownership,
version negotiation, and the point where untrusted input becomes validated.

## Failure and recovery

| Failure | Detection | Durable effect | Recovery | Required evidence |
|---|---|---|---|---|
| {{failure_mode}} | {{detection}} | {{durable_effect}} | {{recovery_action_and_owner}} | {{test_log_metric_or_audit}} |

Cover restart, duplicate delivery, partial commit, timeout, stale work, missing
dependency, migration failure, rollback, and permanently invalid input where
they apply.

## Security and authorization

- **Trust boundary:** {{trust_boundary}}
- **Authentication:** {{authentication}}
- **Authorization:** {{authorization_and_scope}}
- **Secrets:** {{storage_rotation_and_revocation}}
- **Audit:** {{security_relevant_events_and_retention}}
- **Data handling:** {{sensitive_data_minimization_and_deletion}}

## Observability and operations

| Signal or operation | Purpose | Required dimensions or safeguards |
|---|---|---|
| {{metric_log_trace_health_or_command}} | {{operator_question_answered}} | {{bounded_dimensions_permissions_or_rate_limit}} |

Document health states, alerts, inspection and repair commands, backup and
restore effects, and the evidence used to declare a rollout healthy.

## Compatibility migration and rollout

<!--
Describe additive schema and protocol changes, mixed-version behavior,
backfill, feature gates, cutover, rollback limits, and removal criteria.
-->

{{compatibility_migration_and_rollout}}

## Testing strategy

| Level | Behavior proved | Required environment or fixture |
|---|---|---|
| Unit or domain | {{authoritative_requirements_and_transitions}} | {{fixture}} |
| Contract | {{interfaces_and_compatibility}} | {{fixture}} |
| Integration | {{persistence_transport_or_adapter_behavior}} | {{environment}} |
| Failure and recovery | {{restart_partition_retry_or_rollback_behavior}} | {{environment}} |
| Acceptance | {{user_or_operator_outcome}} | {{scenario}} |

## Risks and edge cases

| Risk or edge case | Impact | Mitigation or decision |
|---|---|---|
| {{risk_or_edge_case}} | {{impact}} | {{mitigation_or_decision_id}} |

## Deferred work

- {{deferred_capability_and_reentry_condition}}

## Architecture and specification acceptance

This architecture and specification are ready for the initiative's permitted
output when assumption corrections are reconciled, every blocking decision is
accepted, repository evidence supports the stated baseline, applicable
migration and rollback limits are explicit, and every authoritative requirement
maps to a delivery step and a verification gate.
