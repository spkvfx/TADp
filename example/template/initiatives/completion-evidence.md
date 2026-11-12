<!--
Completion-stage template for every initiative type. Do not copy it during
initial initiative creation. Create it only when the initiative's permitted
work has reached a terminal, evidence-backed result. Replace every token.
-->

# {{initiative_name}} completion evidence

**Initiative:** {{initiative_name}}  
**Initiative type:** `{{implementation_design_or_planning}}`  
**Work version:** {{v_major_minor}}
**Realization suite:** {{realization_suite_id_and_link}}
**Canonical correlation:** {{initiative_index_row_link}}
**Dedicated branch:** {{initiative_branch}}
**Captured base:** {{base_branch_and_commit}}
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

## Cross-initiative coherence review

**Inventory baseline:** {{git_commit_or_exact_inventory_revision_reviewed}}
**Work-conflict register:** {{link_to_project_initiatives_work_conflicts}}

Review every other open initiative (`Proposed`, `Accepted`, or `In progress`)
and every affected closed initiative (`Completed`, `Cancelled`, or
`Superseded`). Include proposed, planned, and partially delivered effort as
work while retaining its evidence standing. Add one row per target; if there
are no other active targets or affected closed targets, say so explicitly.
Use `No other active initiatives; no affected closed targets.` for that result
and retain the empty table with supporting inventory evidence.

| Target initiative | Lifecycle state | Work and effort evidence | Finding | Disposition | Record links |
|---|---|---|---|---|---|
| {{initiative_id_and_link}} | {{current_state}} | {{linked_claim_plan_partial_work_or_verified_output}} | {{compatible_refinement_needed_or_conflict}} | {{reconciled_or_owned_governed_follow_up_with_re_entry_condition}} | {{review_conflict_decision_or_handoff_links}} |

Completion findings may refine open initiative effort only through an
authorized operation and branch, preserving the target's workflow and human
gates. Record both conflicting claims,
their effort, impact, owner, and disposition in the project work-conflict
register and affected records. Also record any invariant contradiction in the
authoritative invariant conflict register. An unresolved conflict affecting
this completion claim blocks completion; transferring incompatible work does
not resolve it.
Prefix incompatible findings with `Conflict:` and link the specific
work-conflict register entry in `Record links`, using its stable
`#work-conflict-NNN` anchor; the ID must exist in the project register.

Do not refine a closed initiative without explicit human reopening authority,
a linked receipt, and a recorded legal transition. Preserve its prior claim.
A substantive change requires a successor tuple; a successor may cite the
closed predecessor without modifying its claim. Review and referral do not
authorize another initiative's changes or resolve its open questions.

## Cross-record reconciliation

- [ ] The acceptance receipt identifies the same accepted baseline and bounded
      claim proved here.
- [ ] The type-specific `execution-record.md` or `delivery-record.md` agrees
      with the outputs, methods, verification, and revisions recorded here.
- [ ] Initiative README states the same bounded result.
- [ ] Source mapping links every completed normative claim to verification.
- [ ] Roadmap and steps show actual, not planned, completion.
- [ ] Product, specification, or evidence records identify delivered outputs.
- [ ] Parent, subinitiative, dependency, index, and status records agree.
- [ ] Work version, suite, initiative, branch, and captured base agree with the
      canonical correlation row and reciprocal records.
- [ ] Open conflicts and exceptions remain visible.
- [ ] The cross-initiative coherence review covers current open work and
      affected closed claims; every finding has a compatible disposition.

## Completion determination

{{state_why_the_initiative_is_completed_cancelled_superseded_or_still_blocked}}

The initiative may be marked `Completed` only when every applicable row and
checkbox above is supported by linked evidence.

