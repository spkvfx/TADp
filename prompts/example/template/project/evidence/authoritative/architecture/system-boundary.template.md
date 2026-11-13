<!--
Copy this file to a descriptive name such as payment-service-boundary.md. One
file must describe one bounded system, subsystem, or ownership boundary. Do
not use it as a catch-all architecture narrative: create and link another
focused record when a second boundary needs independent review or change.
-->

# {{boundary_name}} system boundary

**Architecture ID:** {{ARC-BND-001}}  
**Status:** {{draft_accepted_superseded_or_retired}}  
**Owner:** {{human_or_team}}  
**Last reviewed:** {{yyyy-mm-dd}}  
**Related records:** {{links_to_contracts_decisions_and_rules}}  

## Boundary statement

{{one_paragraph_defining_what_is_inside_the_boundary_and_why}}

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| {{responsibility}} | {{component_or_team}} | {{adjacent_owner_or_component}} |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | {{caller_or_source}} | {{command_event_or_data}} | {{validator}} | {{versioning_rule}} |
| Outbound | {{consumer_or_destination}} | {{response_event_or_data}} | {{owner}} | {{versioning_rule}} |

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| {{state_or_decision}} | {{durable_source}} | {{component_or_role}} | {{recovery_rule}} |

## Invariants and failure boundaries

- {{binding_invariant_with_evidence_or_rule_link}}
- {{failure_mode_and_the_component_that_recovers_or_reports_it}}

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| {{boundary_claim}} | {{test_review_or_operational_check}} | {{path_or_link}} |

Changes to this boundary require review by {{owner_or_governance_role}} and
updates to every affected contract, decision, rule, initiative, or product
record.
