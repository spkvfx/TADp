<!--
Execution-stage template for an accepted `implementation` initiative. Do not
copy it during initial initiative creation. Create it when product execution
actually begins, update it throughout execution, and replace every token.
-->

# {{initiative_name}} execution record

**Initiative:** {{initiative_name}}  
**Execution status:** {{in_progress_blocked_or_complete}}  
**Accepted execution scope:** {{exact_phase_steps_or_change_set}}  
**Branch:** {{initiative_branch}}  
**Baseline commit:** {{commit_id}}  
**Started:** {{yyyy-mm-dd}}  
**Last updated:** {{yyyy-mm-dd}}  
**Execution owner:** {{owner}}  

## Governing record

- **Accepted specification:** {{precise_initiative_sections}}
- **Authoritative evidence:** {{evidence_ids_and_claims}}
- **Readiness decision:** {{review_link_or_supplied_result}}
- **Permitted product destinations:** {{paths_packages_apis_or_placements}}

## Execution ledger

| Step | Planned outcome | Product destinations | Status | Verification | Commit or artifact |
|---|---|---|---|---|---|
| {{step_id}} | {{accepted_outcome}} | {{exact_destinations}} | {{not_started_in_progress_blocked_or_complete}} | {{command_test_review_or_pending_gate}} | {{commit_id_link_or_not_yet_created}} |

## Product changes

| Destination | Change | Governing specification | Compatibility or migration effect | Recovery or rollback | Owner |
|---|---|---|---|---|---|
| {{path_symbol_or_placement}} | {{factual_change}} | {{section_or_claim}} | {{effect_or_not_applicable_with_reason}} | {{method_limit_or_not_applicable_with_reason}} | {{owner}} |

## Verification evidence

| Claim | Method or command | Environment | Result | Evidence location |
|---|---|---|---|---|
| {{claim_id}} | {{exact_method_or_command}} | {{fixture_service_or_environment}} | {{pass_fail_blocked_or_not_run}} | {{log_test_artifact_or_review}} |

Record only verification that actually ran. A passing local check does not
establish production, deployment, certification, or public-release readiness
unless the governing specification defines that exact claim.

## Deviations, blockers, and conflicts

| ID | Type | Exact issue | Affected work | Owner | Required resolution | Status |
|---|---|---|---|---|---|---|
| {{EXE-001}} | {{blocker_deviation_or_conflict}} | {{evidence_backed_description}} | {{steps_claims_or_destinations}} | {{owner}} | {{decision_evidence_or_product_change}} | {{open_or_resolved}} |

Do not change an accepted specification to hide an implementation deviation.
Route specification conflicts to a design initiative and invariant conflicts
to the invariant conflict register.

## Reconciliation

- **Implementation steps updated:** {{links_and_result}}
- **Source mapping updated:** {{links_and_result}}
- **Product records updated:** {{links_and_result}}
- **Initiative and parent status updated:** {{links_and_result}}
- **Deferred work has an owner:** {{links_or_none}}

## Execution conclusion

{{state_the_exact_completed_blocked_or_partial_execution_result}}

Execution is complete only when every in-scope ledger row and verification gate
has passing evidence and the result is captured in `completion-evidence.md`.

