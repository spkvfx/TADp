<!--
Replace every double-brace token. Each step must be a coherent review unit that
can land with its `evidence/authoritative` requirements satisfied and its tests
or other verification passing. Duplicate the full step structure; do not reduce
a step to a file checklist.
-->

# {{initiative_name}} delivery steps

**Initiative:** {{initiative_name}}  
**Status:** Proposed  
**Last updated:** {{date}}  
**Initiative type:** `{{initiative_type}}`

Related documents:

- [Initiative index](initiative-README.template.md)
- [Architecture](architecture.template.md)
- [Evidence mapping](source-mapping.template.md)
- [Delivery roadmap](implementation-roadmap.template.md)
- [Open questions and decisions](open-questions.template.md)

## Current-state analysis

| Path or system | Current behavior | Planned use or change | Evidence |
|---|---|---|---|
| `{{repository_path}}` | {{current_behavior}} | {{planned_change_or_reuse}} | {{test_symbol_document_or_observation}} |

Record the current products, specifications, and evidence relevant to this
initiative. Include extension points, applied migrations, compatibility
constraints, test fixtures, and missing infrastructure where they apply.

## Delivery strategy

- Follow the initiative type boundary in [initiative-README.template.md](initiative-README.template.md). An
  `implementation` initiative changes products; a `design` initiative changes
  specifications and supporting evidence but does not create a new product; a
  `planning` initiative creates evidence only.
- Land changes in dependency order and keep each step independently reviewable.
- For product changes, preserve existing behavior until the roadmap's explicit
  cutover step and add compatibility seams before switching writers or
  consumers.
- For irreversible product boundaries, pair recovery evidence with an explicit
  rollback limit.

## Step 1 - {{step_name}}

### Objective

{{one_reviewable_outcome}}

### Expected output locations

- `{{existing_or_proposed_path}}`
- `{{existing_or_proposed_path}}`

Paths are expected product, specification, or evidence placements, not
permission to bypass ownership and dependency rules in
[architecture.template.md](architecture.template.md).

### Planned output

- {{behavior_change}}
- {{behavior_change}}
- {{compatibility_or_failure_behavior}}

### Dependencies

- {{earlier_step_decision_or_external_dependency}}

### Evidence / authoritative

- {{authoritative_evidence_or_requirement}}
- {{authoritative_evidence_or_requirement}}

### Migration and rollback

- **Migration or backfill:** {{migration_backfill_or_not_applicable_reason}}
- **Mixed-version behavior:** {{mixed_version_behavior_or_not_applicable_reason}}
- **Rollback:** {{rollback_path_and_point_of_no_return}}

### Verification

- {{meaningful_unit_contract_or_integration_test}}
- {{failure_recovery_or_compatibility_test}}

### Acceptance

- {{observable_acceptance_condition}}
- {{evidence_required_for_review}}

<!-- Duplicate the complete step section and keep step numbers stable. -->

## Validation matrix

| Requirement or authoritative evidence | Step | Verification | Evidence location |
|---|---|---|---|
| {{requirement_or_authoritative_evidence}} | {{step_number}} | {{test_review_or_manual_scenario}} | {{path_command_or_report}} |

## Final acceptance criteria

- [ ] Every delivery step is complete and its verification passes.
- [ ] Every `../../evidence/authoritative` requirement appears in the validation
      matrix.
- [ ] Every normative product or specification contract traces through
      `source-mapping.md` to `../../evidence/authoritative` and verification.
- [ ] Applicable upgrade, rollback limits, restart, and recovery have been
      verified.
- [ ] Security and operational review findings are resolved or explicitly
      accepted with an owner.
- [ ] User-facing and operator-facing documentation describes the delivered
      behavior.
- [ ] Work-version, suite, initiative, branch, and captured-base identity still
      match the canonical correlation row.
- [ ] `../status.md` and the initiative index record the final state and next
      maintenance responsibility.
