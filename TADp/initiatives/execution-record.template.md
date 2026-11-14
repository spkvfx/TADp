<!--
Execution-stage template for an accepted `implementation` initiative. Do not
copy it during initial initiative creation. Create it when product execution
actually begins, update it throughout execution, and replace every token.
-->

# {{initiative_name}} execution record

**Initiative:** {{initiative_name}}  
**Execution status:** {{in_progress_blocked_or_complete}}  
**Accepted execution scope:** {{exact_phase_steps_or_change_set}}  
**Version scope:** {{version_scope}}
**Source notes:** {{exact_originating_and_contributing_note_ID_path_links_only}}
**Revision cycle:** {{positive_integer_cycle}}
**Claim revision:** {{exact_current_claim_revision}}
**Execution mode:** {{dedicated_or_shared}}
**Integration target:** {{assigned_scope_branch}}
**Realization suite:** {{realization_suite_id_and_link}}
**Canonical correlation:** {{initiative_index_row_link}}
**Execution branch:** {{initiative_branch}}
**Captured base ref:** {{base_branch}}
**Captured base commit:** {{commit_id}}
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
- **Membership, provenance and active revision remain intact:** {{canonical_row_and_reciprocal_link_review}}

## Prompt blocks and bounded exceptions

{{source_prompt_revision_effective_block_ledger_exception_records_and_receipts_or_none}}

Preserve actual author and authorized method for agent-made dispositions;
reconcile affected decisions, lifecycle, status, and dependent records. Label
waived, excepted, skipped, unperformed, and failed checks truthfully. They do
not prove acceptance, readiness, or ordinary completion. Locks remain enforced.
Keep preview proposals response-only, local access within its restriction,
and independent-review results and unresolved findings explicit. Restored
gates recheck current prerequisites dependent on earlier excepted work.

## Execution conclusion

{{state_the_exact_completed_blocked_or_partial_execution_result}}

Execution is complete only when every in-scope ledger row and verification gate
has passing evidence and the result is captured in `completion-evidence.md`.


## Per-cycle Git attribution and integration

**Revision base:** {{immutable_current_cycle_base_commit}}

**Initiative-specific paths and commits:** {{exact_paths_commits_and_verified_delta}}

**Shared mixed-change boundary:** {{limits_and_other_member_ownership_or_none}}

**Integration state:** {{Pending_Blocked_Merged_Fast-forward_Already_integrated_Direct_placement_Excluded_Transferred_or_No_deliverable}}

**Integration evidence:** {{current_cycle_integration_receipt_link_or_pending}}

**Verified member commit:** {{immutable_accepted_initiative_specific_commit_or_pending}}

Earlier cycle evidence is historical. A new cycle requires fresh verification
and integration of its delta. Direct scope placement uses exact verified commits
without self-merge or upward scope closure. Never merge shared whole tips with
unfinished/unaccepted/cancelled/unrelated changes. Preserve failures and prior
truthful lifecycle independently of integration success.

The exact Revision cycle and Claim revision must match the current initiative
README and acceptance receipt. Earlier-cycle evidence cannot qualify reopened
or changed claims. For shared execution, Verified member commit identifies this
member's accepted verified commit, not an undifferentiated whole shared tip.

Instantiate the [integration receipt source](integration-receipt.template.md)
outside template/ to record actual integration. Its exact current-cycle fields
are Initiative ID, Revision cycle, Claim revision, Integration state, Source tip,
Target ref, Target before, Target after, Authority, Method and Post-integration
verification. Preserve closure authority, inventory and any exclusion/transfer
Human authority. A status or combined narrative does not substitute for this
receipt or its actual Git/verification evidence.
