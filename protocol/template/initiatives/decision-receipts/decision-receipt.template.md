<!--
Copy for one explicit human decision. Replace every double-brace token, remove
instructional comments, and preserve the exact prompt and response verbatim.
-->

# {{receipt_id}} decision receipt

**Receipt ID:** {{receipt_id}}  
**Initiative:** {{initiative_name_and_link}}  
**Source ID or lifecycle event:** {{stable_source_id_or_event}}  
**Human authority:** {{responder_and_governing_role}}  
**Response date or event:** {{yyyy-mm-dd_or_event}}  
**Capture date or event:** {{actual_capture_time_separate_from_original_response_event}}

**Recorded by:** {{actual_recording_agent_or_human}}

**Capture context:** {{chat_review_meeting_or_other_traceable_context}}  
**Disposition:** {{confirmed_corrected_not_applicable_accepted_deferred_cancelled_superseded_reopened_or_other_exact_result}}  
**Git commit:** {{commit_or_pending}}
**Scope:** {{exact_version_scope}}
**Revision cycle:** {{positive_integer_cycle}}
**Claim revision:** {{exact_current_claim_revision}}

<!--
For a reopening, set the exact field **Disposition:** Reopened and retain
**Human authority:** with the responder and governing role.
For an explicit unchanged-claim reopening directly to Accepted, add
**Unchanged accepted claim:** Yes
only when the exact human response confirms that exception. Otherwise the
reopening returns to Proposed. Never infer the exception from older acceptance.
-->

## Exact prompt or question

{{verbatim_prompt_or_question_presented_to_the_human}}

## Evidence and limitations presented

- **Authoritative evidence:** {{precise_sources_and_claims}}
- **Other evidence:** {{sources_and_classification_or_none}}
- **Material limitations:** {{missing_stale_or_out_of_scope_evidence_or_none}}
- **Affected scope described to the human:** {{bounded_scope}}

## Exact human response

{{verbatim_human_response}}

## Resulting scope and rationale

{{what_the_response_governs_and_why_it_is_actionable}}

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| {{relative_link}} | {{disposition_or_claim_changed}} | {{review_diff_test_or_other_evidence}} |

## Unresolved consequences and re-entry conditions

{{none_or_exact_remaining_question_owner_and_trigger}}

## Bounded prompt exception or autonomous-method authority

<!--
Retain this section when this human decision authorizes a prompt exception or
another decision method; otherwise remove it. Follow canonical specification
11. Draft only in the response for preview work. Do not invent a human answer
for a resulting agent-made disposition or claim a waived gate passed.
-->

- **Exception record:** {{gate_exception_link_or_none}}
- **Source prompt and block:** {{stable_prompt_revision_block_id_and_exact_range}}
- **Authorized rules and gates:** {{exact_rule_ids_revisions_and_bounded_replacements}}
- **Autonomous method and limits:** {{explicitly_authorized_method_or_none}}
- **Resulting agent-made dispositions:** {{actual_agent_author_method_source_ids_and_links_or_none}}
- **Remaining obligations and restoration:** {{locks_unexcepted_rules_end_condition_and_rechecks}}



## Delegated realization intake event

<!-- Retain for one adopted specification 09 intake routing/reopening event.
Record before applying the disposition. Preserve exact human instruction
separately from actual LLM authorship. No fabricated per-target human answer.
Every new reopening needs its own event receipt. -->

**Decision author:** {{actual_LLM_or_human_author}}

**Decision method:** Delegated realization intake

**Governing delegation:** {{adopted_specification_09_revision_and_intake_authority_link}}

**Human intake instruction:** {{verbatim_actual_human_instruction}}

**Source realization:** {{exact_suite_note_IDs_paths_and_source_scope}}

**Target initiative and scope:** {{exact_ID_path_and_target_scope}}

**Prior lifecycle state:** {{prior_state}}

**Prior claim revision:** {{immutable_prior_baseline}}

**Revision history:** {{prior_cycle_history_link}}

**Routing disposition:** {{append_revision_reopening_new_or_successor}}

**Candidates and rejected alternatives:** {{target_inventory_and_rationale}}

**Change boundary:** {{bounded_same_outcome_change_risks_and_compatibility}}

**Verification boundary:** {{required_checks_and_new_delta}}

**Routing evidence:** {{per_source_routing_and_fit_links}}

**Affected scope/ancestor events:** {{separate_event_links_or_none}}

For a reopening retain **Disposition:** Reopened and the actual human authority
that delegated this intake, with this event's LLM decision separately identified.
Return to Proposed. Direct return to Accepted requires a separate explicit human
unchanged-claim decision and **Unchanged accepted claim:** Yes. Prior acceptance
and prior integration do not certify a changed claim or new revision delta.
Reconcile replacement consequences for Cancelled/Superseded targets explicitly.

For acceptance, Revision cycle and Claim revision identify the exact current
claim being accepted and match its README and subsequent delivery/completion
evidence. A prior-cycle acceptance receipt supplies no changed-claim acceptance.


For separately authorized historical ref removal, retain **Human authority:**
and add **Branch:** {{exact_removed_branch_ref}} and **Historical branch tip:**
{{immutable_source_tip_commit}}. Preserve source history and all reciprocal
removal links; this receipt does not authorize reusing a historical name.


For a scope/ancestor reopening, record a separate event with exact **Scope:**,
**Disposition:** Reopened and actual **Human authority:** plus the adopted
intake Governing delegation and Human intake instruction when delegated. Link
the receipt from the canonical scope registry's Reopening evidence metadata.
No child event implicitly reopens another scope or ancestor.
