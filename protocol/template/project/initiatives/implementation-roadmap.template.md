<!--
Replace every double-brace token. Add, remove, or reorder phases to match real
dependencies, but retain the standard Objective, Work, and Exit gate fields.
-->

# {{initiative_name}} delivery roadmap

**Initiative:** {{initiative_name}}  
**Status:** Proposed  
**Last updated:** {{date}}  
**Initiative type:** `{{initiative_type}}`

Related documents:

- [Initiative index](initiative-README.template.md)
- [Assumption review](assumption.template.md)
- [Architecture](architecture.template.md)
- [Evidence mapping](source-mapping.template.md)
- [Open questions and decisions](open-questions.template.md)
- [Detailed delivery steps](implementation-steps.template.md)

## Objective

{{delivery_objective_and_observable_end_state}}

## Delivery scope

### Included

- {{included_delivery}}
- {{included_delivery}}

### Excluded from this roadmap

- {{excluded_delivery_and_reason}}
- {{excluded_delivery_and_reason}}

## Type-specific delivery boundary

- **`implementation`:** align products to accepted specifications. It may create
  or modify products, but it must not modify an existing specification.
- **`design`:** align specifications to observed products. It may create or
  modify specifications and supporting evidence, but it must not create a new
  product.
- **`planning`:** create evidence exclusively for other initiatives. It must not
  create or change products or specifications.

## Prerequisites

| Prerequisite | Required state | Evidence |
|---|---|---|
| {{decision_dependency_or_foundation}} | {{required_state}} | {{link_or_verification}} |

## Phase summary

| Phase | Outcome | Depends on | Parallel work allowed |
|---|---|---|---|
| 0 | Accepted specifications and initiative output boundary | None | {{yes_no_and_constraints}} |
| 1 | {{first_deliverable_outcome}} | Phase 0 | {{yes_no_and_constraints}} |
| {{phase_number}} | {{release_outcome}} | {{dependencies}} | {{yes_no_and_constraints}} |

## Phase 0 - Accept the specifications and output boundary

### Objective

Reconcile proposal intent, assumption corrections, evidence, and blocking
decisions before the initiative creates its permitted output.

### Work

- Resolve every decision marked `Open, blocking`.
- Confirm ownership, identity, transaction, compatibility, and migration
  boundaries against the current repository.
- Confirm every normative contract has a source-mapping row and delivery or
  verification destination.
- Map each `../../evidence/authoritative` requirement to a detailed step and a test
  or review gate.
- Record rollout flags, mixed-version rules, and rollback limits.
- Confirm the initiative type and enumerate the products, specifications, or
  evidence it may change. For an `implementation` initiative, confirm that the
  accepted specifications support the intended product work. If a specification
  change is needed, stop the affected work and route it to a `design` initiative.
- Verify that the exact version scope, realization suite, initiative,
  branch, captured base, and reciprocal links remain intact. Route a mandatory
  split or independent successor through Stage 0 for its distinct initiative.
  A coherent same-outcome revision follows the recorded current cycle.

### Exit gate

- [ ] Assumption review is complete or all remaining assumptions are explicitly
       accepted as type-specific delivery risk.
- [ ] Every blocking decision has an owner, rationale, date, and acceptance
      condition.
- [ ] Architecture, roadmap, and steps use the same vocabulary and boundaries.
- [ ] The canonical correlation row and reciprocal records agree and no
      independently acceptable outcome is absorbed into this initiative claim.
- [ ] No planned product migration edits a released or applied migration.
- [ ] When an `implementation` initiative needs a specification change, a
       `design` initiative owns that change before the affected product work
       begins.

## Phase 1 - {{phase_name}}

### Objective

{{phase_objective}}

### Work

- {{coherent_deliverable}}
- {{coherent_deliverable}}
- {{migration_test_or_operational_work}}

### Exit gate

- [ ] {{observable_behavior}}
- [ ] {{failure_or_recovery_behavior}}
- [ ] {{compatibility_or_operational_evidence}}

<!-- Duplicate the complete phase section for each ordered phase. -->

## Phase {{phase_number}} - Outcome qualification

### Objective

Prove the complete product, specification, or evidence outcome in its supported
context, then capture the evidence required to mark the initiative completed.

### Work

- Run the end-to-end acceptance scenarios.
- Exercise upgrade, downgrade or rollback where supported, restart, partial
  failure, and recovery.
- Verify security, observability, backup and restore, and operator procedures.
- Update durable architecture and operations documentation.

### Exit gate

- [ ] Every acceptance outcome passes in a supported environment.
- [ ] No unresolved blocking decision or unowned release risk remains.
- [ ] Migration, rollback, and recovery procedures have recorded evidence.
- [ ] Initiative status and durable documentation reflect the delivered result.

## Rollout controls

| Control | Initial state | Enablement condition | Rollback or disable behavior |
|---|---|---|---|
| {{feature_flag_config_gate_or_migration}} | {{initial_state}} | {{enablement_condition}} | {{rollback_behavior_and_limit}} |

## Release definition

The initiative is complete when all phase exit gates pass, each
`../../evidence/authoritative` requirement has verification evidence, applicable
upgrade and recovery paths have been exercised, deferred work is explicit, and
the initiative status points to the durable specification, product, or evidence
that now owns the accepted result.
