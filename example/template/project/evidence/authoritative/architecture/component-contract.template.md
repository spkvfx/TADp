<!--
Copy this file to a descriptive name such as orders-to-billing-contract.md.
Use one file for one interaction boundary between named parties. Put system
ownership in a system-boundary record and durable trade-offs in a decision
record rather than duplicating them here.
-->

# {{producer}} to {{consumer}} contract

**Architecture ID:** {{ARC-CTR-001}}  
**Status:** {{draft_accepted_deprecated_or_retired}}  
**Contract owner:** {{human_or_team}}  
**Producer:** {{component_or_team}}  
**Consumer:** {{component_or_team}}  
**Last reviewed:** {{yyyy-mm-dd}}  

## Purpose and scope

{{why_this_interaction_exists_and_the_behavior_it_covers}}

## Interface surface

| Operation, event, or artifact | Direction | Required input | Success result | Failure result |
|---|---|---|---|---|
| {{name}} | {{request_response_publish_or_consume}} | {{validated_payload_or_precondition}} | {{observable_result}} | {{error_or_recovery_behavior}} |

## Contract rules

| Concern | Rule | Owner |
|---|---|---|
| Authentication and authorization | {{rule}} | {{owner}} |
| Validation and idempotency | {{rule}} | {{owner}} |
| Ordering, timeouts, and retries | {{rule}} | {{owner}} |
| Versioning and compatibility | {{rule}} | {{owner}} |
| Observability and audit | {{rule}} | {{owner}} |

## Failure and recovery

| Failure condition | Detection | Required behavior | Recovery owner |
|---|---|---|---|
| {{failure_condition}} | {{signal}} | {{behavior}} | {{owner}} |

## Compatibility and verification

{{mixed_version_migration_deprecation_and_rollback_rules}}

| Verification | Scenario | Evidence location |
|---|---|---|
| {{contract_or_integration_test}} | {{scenario}} | {{path_or_link}} |

## Related records

- System boundary: {{link}}
- Decision record: {{link_or_not_applicable}}
- Governing rule or evidence: {{link}}
