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
**Work version:** {{v_major_minor}}
**Realization suite:** {{realization_suite_id_and_link}}
**Canonical correlation:** {{initiative_index_row_link}}
**Branch:** {{initiative_branch}}  
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
- **Correlation tuple remains intact:** {{canonical_row_and_reciprocal_link_review}}

## Delivery conclusion

{{state_the_exact_completed_blocked_or_partial_delivery_result}}

Delivery is complete only when every in-scope ledger row and verification gate
has evidence and the result is captured in `completion-evidence.md`.
