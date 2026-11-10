<!--
Completion-stage template for every initiative type. Do not copy it during
initial initiative creation. Create it only when the initiative's permitted
work has reached a terminal, evidence-backed result. Replace every token.
-->

# {{initiative_name}} completion evidence

**Initiative:** {{initiative_name}}  
**Initiative type:** `{{implementation_design_or_planning}}`  
**Completion claim:** {{exact_bounded_claim}}  
**Completion date:** {{yyyy-mm-dd}}  
**Completed commit or artifact revision:** {{commit_id_or_revision}}  
**Evidence owner:** {{owner}}  

## Accepted scope proved

{{state_the_accepted_outcome_and_the_exact_scope_this_record_proves}}

This record does not claim {{explicitly_excluded_release_deployment_or_follow_up_scope}}.

## Requirement coverage

| Requirement or step | Governing evidence or decision | Delivered output | Verification | Result |
|---|---|---|---|---|
| {{requirement_or_step_id}} | {{precise_claim_or_decision}} | {{product_specification_or_evidence_destination}} | {{test_audit_review_or_record}} | {{pass_or_not_applicable_with_reason}} |

## Authoritative-evidence coverage

| Authoritative claim | Initiative interpretation | Compliance evidence | Conflicts or exceptions |
|---|---|---|---|
| {{evidence_id_and_claim}} | {{initiative_section}} | {{verification_or_artifact}} | {{none_or_explicit_approved_record}} |

## Output inventory

| Output | Destination | Revision or commit | Owner | Product or evidence record |
|---|---|---|---|---|
| {{output}} | {{path_package_api_or_placement}} | {{revision}} | {{owner}} | {{record_link}} |

## Verification summary

| Verification gate | Environment | Result | Evidence | Claim limit |
|---|---|---|---|---|
| {{gate}} | {{environment_or_fixture}} | {{pass}} | {{log_test_review_or_artifact}} | {{what_this_does_not_prove}} |

## Compatibility, migration, and recovery

- **Compatibility:** {{effect_and_evidence_or_not_applicable}}
- **Migration:** {{completed_work_order_and_evidence_or_not_applicable}}
- **Rollback or recovery:** {{verified_method_limits_and_owner_or_not_applicable}}

## Residual scope

| Item | Disposition | Owner | Destination initiative or record | Re-entry condition |
|---|---|---|---|---|
| {{remaining_item_or_none}} | {{deferred_blocked_transferred_cancelled_or_not_applicable}} | {{owner}} | {{link_or_not_applicable}} | {{condition_or_not_applicable}} |

No unfinished requirement may disappear from this record. Every residual item
must have a truthful disposition and owner.

## Cross-record reconciliation

- [ ] Initiative README states the same bounded result.
- [ ] Source mapping links every completed normative claim to verification.
- [ ] Roadmap and steps show actual, not planned, completion.
- [ ] Product, specification, or evidence records identify delivered outputs.
- [ ] Parent, subinitiative, dependency, index, and status records agree.
- [ ] Open conflicts and exceptions remain visible.

## Completion determination

{{state_why_the_initiative_is_completed_cancelled_superseded_or_still_blocked}}

The initiative may be marked `Completed` only when every applicable row and
checkbox above is supported by linked evidence.

