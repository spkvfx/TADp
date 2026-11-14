<!-- Copy to initiatives/version-scopes.md. Replace tokens; preserve history. -->

# {{project_name}} version scopes

This is the canonical scope identity, topology and closure registry. Scope
READMEs and status views link here; each initiative README owns its lifecycle.
Scopes are coordination containers, not collective specifications or releases.

**Governing revision:** {{adopted_version_scope_revision_commit}}

**Reopening evidence:** {{per_event_scope_reopening_receipt_links_or_none}}

| Scope | Kind | Structural parent | Integration branch | Captured base ref | Captured base commit | Integration target | Source catalog | Members | Child scopes | Closure disposition | Integration state | Closure evidence | Merge evidence | Governing revision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {{version_scope}} | {{major_minor_or_patch}} | {{matching_parent_scope_or_project_integration_base}} | {{exact_scope_branch}} | {{actual_creation_parent_ref}} | {{immutable_creation_commit}} | {{immediate_parent_ref}} | {{source_catalog_links}} | {{exact_initiative_README_links_and_canonical_membership_row_links_or_none}} | {{child_scope_links_or_none}} | {{Open_Completed_Cancelled_Superseded_or_explicit_no_work}} | {{Pending_Blocked_Merged_Fast-forward_Already_integrated_Direct_placement_Excluded_Transferred_or_No_deliverable}} | {{closure_snapshot_link_or_none}} | {{merge_receipt_link_or_none}} | {{revision_commit}} |

Canonical scopes are exact vN, vN.M or vN.M.P with non-negative decimal
components and no leading zeros except 0. Compare numerically without
normalizing identities. Major/minor/patch parents are structural and creation
bases never change after allocation. Zero members is valid without delivery
authority. Preserve additions, reopenings, branch removals and historical bases.

## Scope event history

| Event | Scope | Prior disposition | New disposition | Instruction and actual decision author | Snapshot or revision | Consequences and record links | Git commit |
|---|---|---|---|---|---|---|---|
| {{date_or_event}} | {{scope}} | {{prior_or_initial}} | {{new}} | {{human_intake_or_closure_instruction_and_LLM_choice_or_human_decision}} | {{snapshot}} | {{records}} | {{actual_commit_or_pending}} |

Closing one member never closes a scope. Scope closure needs all member and
child dispositions, successful required integration, aggregate checks and
coherence/conflict reconciliation. Accepted deliverables must be integrated or
have explicitly authorized exclusion/transfer. Reopening and reintegration
remain per-event records; no silent ancestor reopening or closure.

Each scope or ancestor reopening has its own receipt declaring Disposition:
Reopened, exact Scope and actual Human authority/intake delegation. Link every
applicable event from Reopening evidence; the event table alone is insufficient.
