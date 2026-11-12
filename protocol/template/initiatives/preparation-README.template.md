<!--
Stage 0 copies this file to an initiative's README.md and replaces every token.
Stage 3 later expands that prepared skeleton with the complete README template.
-->

# {{initiative_name}} initiative

**Initiative:** {{initiative_name}}

**Initiative ID:** {{initiative_id}}

**Status:** Proposed

**Last updated:** {{yyyy-mm-dd}}

**Initiative type:** `{{initiative_type}}`

**Version scope:** {{version_scope}}
**Source notes:** {{exact_originating_and_contributing_note_ID_path_links_only}}
**Realization suite ID:** {{originating_realization_suite_id}}
**Realization suite:** [{{realization_suite_path}}]({{relative_realization_suite_index_path}})
**Canonical project correlation:** [initiative register]({{relative_initiative_index_path}}#initiative-and-correlation-register)
**Canonical scope record:** [Version scopes]({{relative_version_scopes_path}})
**Execution branch:** {{active_execution_branch}}
**Execution mode:** {{dedicated_or_shared}}
**Historical branch tip:** {{immutable_tip_if_ref_removed_or_not_applicable}}
**Branch removal evidence:** {{separate_removal_receipt_link_or_not_applicable}}
**Captured base ref:** {{captured_base_ref}}
**Captured base commit:** {{immutable_base_commit}}
**Integration target:** {{assigned_scope_branch}}
**Revision cycle:** {{positive_integer_cycle}}
**Claim revision:** {{exact_current_claim_revision}}
**Prior revision record:** {{preserved_previous_README_assignment_snapshot_link_or_initial}}
**Revision history:** {{cycle_history_link}}
**Predecessor or successor:** {{relationship_or_none}}
**Correlation governance:** {{adopted_revision_or_legacy_ledger_link}}

## Preparation state

Stage 0 prepared this identity and branch. The proposal and complete initiative
suite do not yet exist. This skeleton establishes no acceptance, delivery,
completion, compatibility, or release claim.

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| {{yyyy-mm-dd_or_event}} | Initial | Proposed | [realization suite]({{relative_realization_suite_index_path}}) and [canonical correlation row]({{relative_initiative_index_path}}#initiative-and-correlation-register) | Preparation skeleton | Allocate independent initiative membership and open the initiative for proposal work; no acceptance or delivery authority | {{commit_or_pending}} |

## Source routing provenance

| Suite ID | Suite path | Source ID | Source scope | Source path | Disposition | Routing evidence |
|---|---|---|---|---|---|---|
| {{suite_id}} | [{{suite_id}}]({{relative_suite_path}}) | {{note_id}} | {{source_scope}} | [{{note_id}}]({{relative_note_path}}) | {{originating_or_contributing_append_revision_reopening_new_or_successor}} | {{routing_receipt_link}} |

Retain exact originating and later contributing notes independently. Each row
links its source suite and note and the per-source fit/authority record. Source
scope may differ from target scope without relabeling either identity.

Any absent historical dedicated ref retains its exact immutable Historical
branch tip and separately authorized Branch removal evidence. That removal
receipt records Human authority and exact Branch; removing a ref never frees
its identity for unrelated work or qualifies a new cycle.
