<!--
Maintain one canonical row per concept or contract. Cite the strongest source
evidence that governs the row and link the accepted assumption or decision that
controls its product- or specification-facing expression. Split this file only when scale
makes a single map unreviewable, and retain one canonical owner for each row.
-->

# {{initiative_name}} evidence mapping

**Initiative:** {{initiative_name}}
**Status:** Proposed
**Last updated:** {{date}}
**Decision prefix:** `{{decision_prefix}}`

This map connects evidence to accepted specifications, product destinations,
and verification. It supports traceability; it does not replace the proposal,
assumption record, decision register, or architecture and specification.

## Evidence inventory

| Evidence ID | Source | Evidence label | Governs | Conflict rule |
|---|---|---|---|---|
| EVD-01 | {{source_link_or_path}} | `../../evidence/authoritative` | {{governed_concepts}} | {{how_conflict_is_handled}} |
| EVD-02 | {{source_link_or_path}} | `../../evidence/non-authoritative` | {{context_or_supported_claim}} | {{how_conflict_is_handled}} |

Use `../../evidence/authoritative` only for binding evidence that an accepted
specification or product decision must follow. Use
`../../evidence/non-authoritative` for observations, proposals, examples, exploratory
analysis, and other material that can inform but cannot by itself govern a
decision.

## Concept and contract mapping

| Map ID | Concept or contract | Authoritative evidence | Assumption | Decision | Specification location | Product destination | Verification evidence | Status |
|---|---|---|---|---|---|---|---|---|
| MAP-001 | {{concept_or_contract}} | {{evidence_id_and_precise_section_or_na}} | {{assumption_id_or_na}} | {{decision_id_or_na}} | [architecture.md](architecture.md) - {{section}} | {{product_path_symbol_api_or_documentation}} | {{test_audit_or_review}} | Proposed |

## Mapping rules

- Cite a precise section, heading, claim, or record when evidence supports one;
  a directory link alone is insufficient for a binding row.
- Use the source inventory in [proposal/README.md](proposal/README.md) to apply
  evidence labels and precedence consistently.
- Link every product output or specification change to an accepted assumption
  row or decision. Use `Not applicable` only with a stated reason.
- Give each concept one canonical map row. Related documents link to that row
  instead of duplicating authority.
- Keep proposed interpretation visibly `Proposed`; change it to `Mapped` only
  after source, architecture, destination, and verification columns agree.
- Treat a conflict in, or missing, `../../evidence/authoritative` as blocking. Record
  the issue in [open-questions.md](open-questions.md) before hardening the
  affected contract.

## Coverage audit

| Area | Expected concepts or contracts | Mapped | Gaps | Gate |
|---|---|---|---|---|
| Product and scope | {{expected_scope_items}} | {{mapped_ids}} | {{gap_or_none}} | {{pass_blocked_or_na}} |
| Domain and identity | {{expected_domain_items}} | {{mapped_ids}} | {{gap_or_none}} | {{pass_blocked_or_na}} |
| Interfaces and integration | {{expected_interface_items}} | {{mapped_ids}} | {{gap_or_none}} | {{pass_blocked_or_na}} |
| Data and lifecycle | {{expected_state_items}} | {{mapped_ids}} | {{gap_or_none}} | {{pass_blocked_or_na}} |
| Security and authority | {{expected_security_items}} | {{mapped_ids}} | {{gap_or_none}} | {{pass_blocked_or_na}} |
| Operations and recovery | {{expected_operations_items}} | {{mapped_ids}} | {{gap_or_none}} | {{pass_blocked_or_na}} |

## Unresolved mappings

| ID | Missing or conflicting evidence | Affected rows | Decision or owner | Required resolution |
|---|---|---|---|---|
| MAP-Q01 | {{issue}} | {{map_ids}} | {{decision_id_or_owner}} | {{resolution_and_gate}} |

Remove placeholder rows only after recording `None` when no unresolved mapping
remains. Re-run the coverage audit whenever evidence classification, an
accepted assumption, decision, specification, or product destination changes.

## Realization routing and revision provenance

| Suite ID | Suite path | Source ID | Source path | Source scope | Target initiative/scope | Disposition | Fit, rejected alternatives and compatibility | Routing evidence | Intake instruction/delegation and actual decision author | Cycle and affected records |
|---|---|---|---|---|---|---|---|---|---|---|
| {{suite_id}} | {{suite_link}} | {{note_id}} | {{note_link}} | {{source_scope}} | {{target_ID_and_scope}} | {{append_revision_reopening_new_successor}} | {{rationale_impact_and_limits}} | {{routing_receipt_link}} | {{receipt_and_LLM_method}} | {{cycle_and_reconciled_links}} |

Preserve original and later contributing sources independently. Shared notes
remain non-authoritative and do not share target acceptance or completion.
An existing target keeps scope when receiving cross-scope material. Every
routing/reopening disposition is recorded before changes and reconciles claims,
dependencies, roadmap, steps, compatibility, verification and conflict records.