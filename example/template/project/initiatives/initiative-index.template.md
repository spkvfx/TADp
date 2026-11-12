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

## Authority boundary

This index owns canonical project-level tuple identity and initiative
discovery. It does not accept an initiative, resolve a decision, prove
delivery, or replace the initiative README's lifecycle authority.

## Initiative and correlation register

| Work version | Realization suite | Initiative ID | Name | Type | Status | Dedicated branch | Captured base branch | Captured base commit | Predecessor or successor | Record location | Lifecycle evidence | Branch removal evidence | Owner | Next gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {{v_major_minor}} | [{{realization_suite_id}}]({{relative_suite_index_path}}) | {{INIT-001}} | {{initiative_name}} | `{{design_implementation_or_planning}}` | {{proposed_accepted_in_progress_completed_cancelled_or_superseded}} | {{initiative_branch}} | {{base_branch}} | {{base_commit}} | {{relationship_or_none}} | [{{directory_or_record}}]({{relative_initiative_path}}) | {{lifecycle_evidence_link}} | {{not_applicable_or_removal_authority_link}} | {{owner}} | {{decision_review_or_date}} |

## Cross-initiative dependencies

| Dependent initiative | Depends on | Required state | Owner | Blocking? |
|---|---|---|---|---|
| {{initiative_id}} | {{initiative_id_or_evidence}} | {{accepted_completed_or_other_state}} | {{owner}} | {{yes_or_no}} |

Review dependencies alongside proposed, planned, and partially delivered open
effort. Record incompatibilities in [work-conflicts.md]({{relative_work_conflict_register_path}})
with links to both claims and their affected initiative records. Neither this
index nor a completion finding authorizes changes to another initiative or
reopening of a closed claim.

## Status update rules

- Add a row only as part of the Stage 0 preparation unit that allocates the
  unused version, suite, initiative, and branch from a captured base.
- Preserve allocated identity and base fields immutably. Update copied status,
  lifecycle evidence, branch-removal evidence, owner, dependency, or next gate
  only from their owning records.
- Keep completed, cancelled, and superseded rows as traceable history.
- Link conflicts and major decisions to the initiative's own record; do not put
  unreviewed decisions only in this index.
- Keep this registry coherent with `status.md`, the realization-suite index,
  the initiative README, and any applicable parent or subinitiative indexes.
  A row establishes identity and discoverability, not evidence authority,
  acceptance, implementation, qualification, completion, or release readiness.
- Never reuse a version or branch. If a terminal branch ref is separately
  removed, retain the recorded name and link its removal authority.
