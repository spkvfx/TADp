<!--
Copy this file to status.md at the root of the initiatives directory. Replace
every double-brace token and remove this comment before review. This is a
portfolio coordination view, not a substitute for initiative records or
verification evidence.
-->

# {{project_name}} initiative status

**Status owner:** {{human_or_team}}  
**Last reviewed:** {{yyyy-mm-dd}}  
**Review cadence:** {{event_or_interval}}  

## Authority boundary

This record summarizes current lifecycle standing and gates. Each initiative's
own record remains authoritative for its scope, decisions, assumptions, and
detailed state. A status row must cite the evidence that supports its claim.
Listing work as `Proposed`, `Accepted`, `In progress`, or `Completed` here does
not create that state without the required initiative-local authority and
verification.

## Current status

| Scope | Initiative ID | Realization suite | Type | Status | Current milestone | Next gate | Blockers or holds | Status evidence | Owner | Last updated |
|---|---|---|---|---|---|---|---|---|---|---|
| {{version_scope}} | {{INIT-001}} | [{{realization_suite_id}}]({{relative_suite_index_path}}) | `{{design_implementation_or_planning}}` | {{status}} | {{current_milestone}} | {{next_review_decision_or_verification_gate}} | {{blocker_links_or_none}} | {{initiative_lifecycle_and_canonical_correlation_links}} | {{owner}} | {{yyyy-mm-dd}} |

## Portfolio gates

| Gate ID | Outcome required | Depends on | Evidence required | Owner | State |
|---|---|---|---|---|---|
| {{GATE-01}} | {{observable_outcome}} | {{initiative_ids_or_prior_gates}} | {{verification_or_acceptance_evidence}} | {{owner}} | {{open_ready_passed_or_blocked}} |

## Maintenance rules

- Update a row only from current initiative and verification evidence.
- Record only lifecycle states and transitions permitted by the authoritative
  lifecycle specification. `Reopened` is an event recorded in the initiative
  history, not a status value.
- Link a blocker to the record that owns its resolution; do not restate an
  unresolved decision as if this status page could decide it.
- Keep completed, cancelled, and superseded rows until the retention rule in
  `project-profile.md` permits archival.
- Reconcile this record with `initiative-index.md`, applicable parent and
  subinitiative indexes, and affected initiative READMEs in the same reviewed
  change.
- Copy scope, source and current assignment identity from the canonical correlation row;
  never allocate, renumber, or infer identity in this status view.
- A parent, subinitiative, release, or version boundary does not rewrite the
  identity, authority, or classification of retained proposal sources.


Scope closure/integration is linked from the canonical version-scopes.md
registry, independently of member lifecycle. This view creates no collective
acceptance or scope closure. Keep membership links and per-cycle integration
history in their canonical owners.