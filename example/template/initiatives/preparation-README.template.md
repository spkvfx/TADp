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

**Work version:** {{v_major_minor}}

**Realization suite ID:** {{realization_suite_id}}

**Realization suite:** [{{realization_suite_path}}]({{relative_realization_suite_index_path}})

**Canonical project correlation:** [initiative and correlation register]({{relative_initiative_index_path}}#initiative-and-correlation-register)

**Dedicated branch:** {{initiative_branch}}

**Captured base branch:** {{base_branch}}

**Captured base commit:** {{base_commit}}

**Predecessor or successor:** {{relationship_or_none}}

**Correlation governance:** {{effective_commit}}

## Preparation state

Stage 0 prepared this identity and branch. The proposal and complete initiative
suite do not yet exist. This skeleton establishes no acceptance, delivery,
completion, compatibility, or release claim.

## Initiative lifecycle

### Lifecycle history

| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |
|---|---|---|---|---|---|---|
| {{yyyy-mm-dd_or_event}} | Initial | Proposed | [realization suite]({{relative_realization_suite_index_path}}) and [canonical correlation row]({{relative_initiative_index_path}}#initiative-and-correlation-register) | Preparation skeleton | Allocate the correlated tuple and open the initiative for proposal work; no acceptance or delivery authority | {{commit_or_pending}} |
