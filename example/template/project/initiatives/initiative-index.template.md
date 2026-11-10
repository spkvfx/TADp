<!--
Copy this file to initiative-index.md at the root of the initiatives directory.
It is a directory-level register, not a replacement for an initiative's own
record. Replace tokens, retain closed rows for history, and remove this comment
before review.
-->

# {{project_name}} initiative index

**Index owner:** {{human_or_team}}  
**Last reviewed:** {{yyyy-mm-dd}}  
**Review cadence:** {{event_or_interval}}  

## Initiative register

| Initiative ID | Name | Type | Status | Record location | Governing evidence | Primary output | Owner | Next gate |
|---|---|---|---|---|---|---|---|---|
| {{INIT-001}} | {{initiative_name}} | `{{design_implementation_or_planning}}` | {{proposed_accepted_in_progress_completed_cancelled_or_superseded}} | [{{directory_or_record}}]({{relative_path}}) | {{evidence_ids_or_links}} | {{specification_product_or_evidence}} | {{owner}} | {{decision_review_or_date}} |

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|
| {{initiative_id}} | {{initiative_id_or_evidence}} | {{accepted_completed_or_other_state}} | {{owner}} | {{yes_or_no}} |

## Status update rules

- Add a row when an initiative receives an ID and a record location.
- Update the row when its status, owner, governing evidence, primary output,
  dependency, or next gate changes.
- Keep completed, cancelled, and superseded rows as traceable history.
- Link conflicts and major decisions to the initiative's own record; do not put
  unreviewed decisions only in this index.
- Keep this registry coherent with `status.md` and any applicable parent or
  subinitiative indexes. A row here establishes discoverability, not
  acceptance, implementation authority, qualification, or release readiness.
