<!--
Delivery-stage template for an accepted `design` or `planning` initiative. Do
not copy it during initial initiative creation. Create it when the permitted
specification or evidence work actually begins, update it throughout delivery,
and replace every token.
-->

# {{initiative_name}} delivery record

**Initiative:** {{initiative_name}}  
**Initiative type:** `{{design_or_planning}}`  
**Delivery status:** {{in_progress_blocked_or_complete}}  
**Accepted delivery scope:** {{exact_steps_or_output_set}}  
**Accepted baseline revision:** {{revision_or_commit}}  
**Version scope:** {{version_scope}}
**Source notes:** {{exact_originating_and_contributing_note_ID_path_links_only}}
**Revision cycle:** {{positive_integer_cycle}}
**Claim revision:** {{exact_current_claim_revision}}
**Execution mode:** {{dedicated_or_shared}}
**Integration target:** {{assigned_scope_branch}}
**Realization suite:** {{realization_suite_id_and_link}}
**Canonical correlation:** {{initiative_index_row_link}}
**Execution branch:** {{initiative_branch}}
**Captured base:** {{base_branch_and_commit}}
**Started:** {{yyyy-mm-dd}}  
**Last updated:** {{yyyy-mm-dd}}  
**Delivery owner:** {{owner}}  

## Governing record

- **Accepted specification:** {{precise_initiative_sections}}
- **Authoritative evidence:** {{evidence_ids_and_claims}}
- **Acceptance receipt:** {{decision_receipt_link}}
- **Permitted output destinations:** {{specification_or_evidence_paths}}
- **Prohibited output boundary:** {{products_for_design_or_external_changes_for_planning}}

## Delivery ledger

| Step | Accepted outcome | Output destination | Status | Verification | Commit or revision |
|---|---|---|---|---|---|
| {{step_id}} | {{accepted_outcome}} | {{exact_destination}} | {{not_started_in_progress_blocked_or_complete}} | {{review_lint_audit_or_method}} | {{commit_revision_or_pending}} |

## Output changes

| Destination | Change or evidence output | Governing claim | Consumers or affected owners | Compatibility or limitation |
|---|---|---|---|---|
| {{path_or_artifact}} | {{factual_change_or_output}} | {{section_or_decision}} | {{owners_dependencies_or_audience}} | {{effect_limit_or_not_applicable}} |

## Method and verification evidence

| Claim | Method or command | Inputs and environment | Result | Evidence location | Claim limit |
|---|---|---|---|---|---|
| {{claim_id}} | {{review_lint_audit_analysis_or_command}} | {{sources_fixtures_or_context}} | {{pass_fail_blocked_or_not_run}} | {{artifact_log_or_review}} | {{what_this_does_not_prove}} |

Record only work and verification that actually occurred. Planning evidence
retains its source classification and limitations. Design verification proves
the delivered specification claim, not unimplemented product behavior.

## Deviations, blockers, and conflicts

| ID | Type | Exact issue | Affected output | Owner | Required resolution | Status |
|---|---|---|---|---|---|---|
| {{DEL-001}} | {{blocker_deviation_or_conflict}} | {{evidence_backed_description}} | {{steps_claims_or_destinations}} | {{owner}} | {{decision_evidence_or_separate_initiative}} | {{open_or_resolved}} |

Do not change an invariant, product, another initiative, or accepted scope to
hide a delivery deviation.

## Reconciliation

- **Roadmap and steps updated:** {{links_and_result}}
- **Source mapping updated:** {{links_and_result}}
- **Specification or evidence outputs indexed:** {{links_and_result}}
- **Initiative and parent status updated:** {{links_and_result}}
- **Residual work has an owner:** {{links_or_none}}
- **Membership, provenance and active revision remain intact:** {{canonical_row_and_reciprocal_link_review}}

## Prompt blocks and bounded exceptions

{{source_prompt_revision_effective_block_ledger_exception_records_and_receipts_or_none}}

Preserve actual author and authorized method for agent-made dispositions;
reconcile affected decisions, lifecycle, status, and dependent records. Label
waived, excepted, skipped, unperformed, and failed checks truthfully. They do
not prove acceptance, qualification, or ordinary completion. Locks remain
enforced. Keep preview proposals response-only, local access within its
restriction, and independent-review results and unresolved findings explicit.
Restored gates recheck current prerequisites dependent on excepted work.

## Delivery conclusion

{{state_the_exact_completed_blocked_or_partial_delivery_result}}

Delivery is complete only when every in-scope ledger row and verification gate
has evidence and the result is captured in `completion-evidence.md`.

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

Instantiate the [integration receipt source](../project/initiatives/integration-receipt.template.md)
outside template/ to record actual integration. Its exact current-cycle fields
are Initiative ID, Revision cycle, Claim revision, Integration state, Source tip,
Target ref, Target before, Target after, Authority, Method and Post-integration
verification. Preserve closure authority, inventory and any exclusion/transfer
Human authority. A status or combined narrative does not substitute for this
receipt or its actual Git/verification evidence.