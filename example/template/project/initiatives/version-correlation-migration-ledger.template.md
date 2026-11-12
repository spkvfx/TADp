<!--
Copy this file to version-correlation-migration-ledger.md beside the project
initiative index when adopting the correlation revision. Preserve legacy
source identity. Replace every token and remove this comment.
-->

# {{project_name}} version-correlation migration ledger

**Project:** {{project_name}}

**Correlation revision effective point:** {{commit}}

**Ledger owner:** {{human_or_team}}

**Last reviewed:** {{yyyy-mm-dd}}

## Authority boundary

This ledger records compatibility and migration disposition. It does not infer
identity, accept an initiative, create a lifecycle state, or prove delivery.
Every meaning-changing mapping requires an explicit human decision receipt.

## Migration ledger

| Legacy identity | Canonical identity | Suite | Initiative | Branch | Action | Authority/evidence | Ambiguity or blocker |
|---|---|---|---|---|---|---|---|
| {{legacy_identity}} | {{canonical_identity_or_not_allocated}} | {{suite_path_or_not_inferred}} | {{initiative_path_or_not_inferred}} | {{branch_or_not_inferred}} | {{Unmigrated_Deferred_Migrate_Normalize_Split_or_Blocked}} | {{source_links}}; governing workflow revision: {{revision}} | {{ambiguity_or_none}}; re-entry or migration condition: {{condition}} |

## Rules

- Preserve historical normalization evidence under its original governing
  revision. Under the adopted scope model vN and vN.0 are distinct identities;
  never normalize one into the other. Use the separate scope adoption ledger.
- Use `Not allocated — must not be inferred` for every new-correlation field
  that lacks authority or evidence. Do not create a partial tuple.
- Preserve broad legacy realizations and initiatives. A required split
  allocates one new independent initiative membership per narrow outcome through Stage 0.
- Preserve original realization evidence, historical links, governing workflow
  revision, and lifecycle evidence.
- A migrated initiative starts `Proposed` unless existing evidence supports
  another legal state.
- `Unmigrated` and `Deferred` rows are actionable warnings and must state a
  re-entry or migration condition.
