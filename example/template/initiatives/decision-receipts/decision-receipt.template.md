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
**Capture context:** {{chat_review_meeting_or_other_traceable_context}}  
**Disposition:** {{confirmed_corrected_not_applicable_accepted_deferred_cancelled_superseded_reopened_or_other_exact_result}}  
**Git commit:** {{commit_or_pending}}  

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


