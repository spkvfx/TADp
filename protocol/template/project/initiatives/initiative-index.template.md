<!-- Copy to initiatives/initiative-index.md. Replace tokens and retain rows. -->

# {{project_name}} initiative index

**Index owner:** {{human_or_team}}

**Last reviewed:** {{yyyy-mm-dd}}

**Review cadence:** {{event_or_interval}}

## Authority boundary

This is the canonical membership/provenance index with exactly one row per
initiative. [Version scopes]({{relative_version_scopes_path}}) owns scopes;
each initiative README owns lifecycle. Source catalogs remain permanently
non-authoritative. Correlation creates no acceptance, delivery or release.

## Initiative and correlation register

| Scope | Initiative ID | Type | Record location | Source notes | Execution branch | Execution mode | Captured base ref | Captured base commit | Integration target | Revision cycle | Lifecycle evidence | Integration evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {{version_scope}} | {{initiative_id}} | {{implementation_design_or_planning}} | [{{initiative_name}}]({{scope_type_id_slug_path}}) | {{exact_originating_and_contributing_note_ID_path_links_only}} | {{active_branch}} | {{dedicated_or_shared}} | {{actual_base_ref}} | {{immutable_base_commit}} | {{assigned_scope_branch}} | {{positive_integer_cycle}} | {{README_lifecycle_link}} | {{integration_receipt_or_pending}} |

Each initiative has one immutable scope, one narrow claim and one active
execution assignment per revision cycle. Multiple initiatives may share scope,
notes/suites and a declared scope branch. IDs remain independent of scope
numbers. Preserve exact source and selected target scopes, fit/routing rationale,
predecessor/successor links and branch-removal authority in reciprocal records.
No row or historical branch identity may be reassigned to unrelated work.

## Source and execution history

| Initiative | Cycle | Source suite ID/path | Source note ID/path | Source scope | Target scope | Routing disposition and rationale | Branch/mode | Captured base ref/commit | Integration target | Prior/replacement relationship | Authority and evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {{initiative_link}} | {{cycle}} | {{suite_link}} | {{note_link}} | {{source_scope}} | {{target_scope}} | {{append_revision_reopening_new_or_successor_and_fit_link}} | {{branch_and_mode}} | {{base}} | {{target}} | {{relationship_or_none}} | {{intake_receipt_routing_history_and_verification_links}} |

Append contributing sources and new-cycle/continuation assignments; do not
overwrite earlier allocation/base/integration history. The current row points
to that history and current lifecycle evidence. Serialize shared writes and
preserve concurrent additions instead of restoring an older index snapshot.

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|
| {{initiative_id}} | {{initiative_id_or_evidence}} | {{required_state}} | {{owner}} | {{yes_or_no}} |

Review proposed and partial effort without promoting authority. Record
incompatible work in [work-conflicts.md]({{relative_work_conflict_register_path}}).
Routing authority and necessary reopening follow the exact adopted intake
method; changed claims still require renewed human acceptance before delivery.

## Status update rules

Preserve closed rows and prior claims. Update copied current fields from their
owners, not inference. A closed scope needs recorded reopening before new
membership. Legacy records stay under their complete non-inferred ledger and
governing revision until explicit migration; historical paths are retained.
