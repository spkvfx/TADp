<!--
Copy to the governed initiative's or scope's integration/closure evidence
location outside template/. Replace every token; retain only applicable fields
and preserve each prior cycle/event receipt. This is evidence of actual action,
not a preauthorization or an acceptance/completion certificate.
-->

# {{receipt_id}} local integration receipt

**Receipt ID:** {{receipt_id}}

**Initiative ID:** {{exact_initiative_id_or_not_applicable_for_scope}}

**Scope:** {{exact_version_scope}}

**Revision cycle:** {{positive_integer_current_cycle}}

**Claim revision:** {{exact_current_claim_revision_or_scope_closure_snapshot}}

**Prior revision record:** {{preserved_prior_cycle_or_closure_snapshot_link_or_initial}}

**Governing revision:** {{adopted_protocol_revision_commit}}

**Lifecycle closure evidence:** {{verified_completed_claim_or_explicit_cancelled_superseded_scope_disposition_link}}

**Closure authority:** {{exact_human_close_finalize_instruction_and_capture_link}}

**Human authority:** {{actual_human_responder_role_instruction_and_bounded_authority}}

**Integration state:** {{Pending_Blocked_Merged_Fast-forward_Already_integrated_Direct_placement_Excluded_Transferred_or_No_deliverable}}

**Source ref:** {{exact_initiative_or_scope_branch}}

**Source tip:** {{actual_immutable_source_commit}}

**Target ref:** {{exact_recorded_immediate_parent_branch}}

**Target before:** {{actual_immutable_pre_action_target_commit}}

**Target after:** {{actual_immutable_post_action_target_commit_or_pending}}

**Authority:** {{exact_source_to_target_local_merge_authority_and_receipt_link}}

**Method:** {{actual_merge_fast_forward_already_integrated_direct_placement_or_explicit_no_merge_disposition}}

**Resulting commit:** {{actual_result_commit_or_no_merge_commit_created}}

**Post-integration verification:** {{Passed_Failed_Not_performed_or_pending}}

**Verified member commit:** {{immutable_initiative_specific_accepted_commit_for_shared_member_or_not_applicable}}

**Capture event and author:** {{actual_date_event_and_recording_agent}}

## Closure snapshot and complete inventory

**Inventory baseline:** {{immutable_git_commit_and_captured_membership_revision}}

**Scope membership and child inventory:** {{exact_canonical_member_child_links_or_not_applicable}}

**Acceptance and current-cycle verification:** {{receipts_delivery_completion_and_delta_checks}}

**Coherence and work conflicts:** {{inventory_review_register_and_reconciliation_links}}

**Parent open/reopening evidence:** {{recorded_parent_state_and_each_required_reopening_event}}

| Member or child | Exact claim/cycle | Closed disposition | Accepted deliverables | Required integration result | Retained/excluded/transferred work and authority |
|---|---|---|---|---|---|
| {{member_or_child_link}} | {{revision}} | {{truthful_disposition}} | {{exact_accepted_outputs_or_none}} | {{integration_receipt_or_blocker}} | {{scope_ownership_and_authority_links}} |

A scope cannot close with open members/descendants, pending required child
integration or omitted accepted deliverables. An empty scope needs an explicit
No work closure disposition. A member closure never closes siblings or scope.

## Actual source and target review

**Source delta and paths:** {{exact_revision_base_diff_and_initiative_attribution}}

**Worktree inspection:** {{staged_unstaged_untracked_inventory_and_preservation}}

**Target-tip review:** {{current_target_checks_and_drift_disposition}}

**Shared-branch qualification:** {{all_included_changes_qualify_or_exact_blocker}}

**Commands and results:** {{actual_commands_outputs_and_verification_links}}

A Direct placement receipt records the member's exact verified accepted commit
and its presence on the assigned scope branch, without a self-merge or upward
scope merge. Source tip is that verified member commit; Target before and Target
after are actual scope tips. A shared whole tip must never carry unfinished,
unaccepted, cancelled or unrelated work upward. Safe isolation or transfer
requires separate authority preserving every owner's evidence.

## Exclusion, transfer or no-deliverable disposition

**Disposition boundary:** {{exact_retained_excluded_or_transferred_paths_claims_and_commits_or_not_applicable}}

**Continuing owner and destination:** {{owner_and_receiving_records_or_none}}

**Disposition authority:** {{exact_human_instruction_and_receipt_or_not_applicable}}

For Excluded, Transferred or No deliverable, retain Human authority, exact
ownership/claim consequences and the explicit reason no merge occurred. A
Cancelled or Superseded lifecycle alone cannot qualify abandoned implementation.

## Failure, retry and re-entry evidence

**Observed failures and integration blockers:** {{actual_failure_or_none}}

**Prior attempt and already-integrated check:** {{earlier_receipt_source_commit_and_current_ancestry_check}}

**Remaining obligations and re-entry conditions:** {{owner_required_checks_and_target_reinspection}}

Integration state remains Pending or Blocked when the action or required checks
fail. Preserve truthful lifecycle completion separately and never fabricate a
merge commit, passing check or acceptance. Fast-forward and Already integrated
receipts record actual commits and methods. A new cycle's delta requires fresh
verification and integration evidence; no old receipt certifies changed work.
Retain branches unless their removal is separately authorized. Local integration
authority implies no push, publication, deletion or ancestor closure.