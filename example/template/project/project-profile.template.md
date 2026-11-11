<!--
Copy this file to project-profile.md at the root of a new project. Replace
every double-brace token and remove this comment before review. This profile is
an orientation and ownership record; it does not override authoritative
evidence, an accepted initiative, or a product contract.
-->

# {{project_name}} project profile

**Project:** {{project_name}}  
**Status:** {{proposed_active_maintained_or_retired}}  
**Project owner:** {{human_or_team}}  
**Technical owner:** {{human_or_team}}  
**Human authority model:** {{solo_project_owner_or_named_review_authorities}}  
**Git repository root:** {{repository_root}}  
**Default integration branch:** {{actual_branch_or_not_assumed}}  
**Pull-request remote:** {{remote_name_or_not_configured}}  
**Correlation revision effective point:** {{commit_or_not_yet_adopted}}
**Correlation migration ledger:** [{{ledger_name}}]({{relative_migration_ledger_path}})
**Last reviewed:** {{yyyy-mm-dd}}  

## Purpose

{{one_or_two_sentences_describing_the_project_outcome_and_primary_users}}

## Scope boundary

### Included

- {{capability_or_domain_owned_by_this_project}}
- {{capability_or_domain_owned_by_this_project}}

### Excluded

- {{adjacent_capability_owned_elsewhere_and_reason}}
- {{adjacent_capability_owned_elsewhere_and_reason}}

## Directory map

| Logical record | Location | What belongs there | Owner |
|---|---|---|---|
| Binding evidence | `../../evidence/authoritative` | {{architecture_rules_or_other_binding_sources}} | {{owner}} |
| Contextual evidence | `../../evidence/non-authoritative` | {{research_observations_or_realizations}} | {{owner}} |
| Initiative records | `../../initiatives` | {{accepted_work_records}} | {{owner}} |
| Delivered products | `../../products` or {{actual_destination}} | {{code_documentation_or_other_outputs}} | {{owner}} |

## Human ownership and approval

{{state_whether_human_owner_reviewer_and_approver_roles_are_distinct_or_resolve_to_one_project_owner}}

This convention applies only to human roles. Preserve every technical
component owner, source authority, external-party dependency, placement,
contract, security, environment, verification, and release gate. Record the
specific human authority whose explicit instruction is required to accept an
initiative, resolve an open decision, change an assumption disposition,
authorize product execution, and authorize publication.

## Authority and traceability

1. {{authoritative_evidence_path_or_identifier}} governs {{subject}}.
2. {{initiative_identifier_or_path}} authorizes {{approved_work}}.
3. {{product_identifier_or_destination}} realizes {{accepted_outcome}}.

Record a conflict instead of changing an earlier record to make a later one
appear aligned. Link the conflict to its owner, resolution, and effective date.

## Work identity and correlation

The project initiative index owns the canonical one-to-one mapping among work
version, realization suite, self-contained initiative, and dedicated Git
branch. Record the exact protocol effective commit above before allocating a
governed tuple. Copies in suites, initiatives, status, delivery, completion,
and Git records link to the canonical row and do not create authority or
lifecycle standing.

Use the linked migration ledger for every pre-effective record. A complete
`Unmigrated` or `Deferred` disposition preserves earlier identity and workflow
without inferring a partial tuple. A substantive successor or mandatory split
after the effective point receives a new tuple.

## Operating cadence

| Event | Required review | Record to update |
|---|---|---|
| {{new_evidence_arrives}} | {{classification_and_owner_review}} | {{evidence_register_or_record}} |
| {{initiative_is_accepted_or_changes_status}} | {{scope_and_dependency_review}} | {{initiative_index}} |
| {{product_is_released}} | {{traceability_and_verification_review}} | {{product_record}} |
| {{scheduled_review}} | {{owner_and_staleness_review}} | {{this_profile_and_affected_records}} |

## Git workflow

This project requires Git. Every initiative uses a dedicated branch created
from a captured base branch. Record repository-specific branch naming,
required checks, commit signing, review, remote, and pull-request conventions
here without weakening the authoritative Git workflow specification.

- **Initiative branch convention:** {{branch_naming_rule}}
- **Required checks:** {{checks_or_none_beyond_initiative_gates}}
- **Commit requirements:** {{signing_message_or_review_requirements}}
- **Merge authority:** {{human_or_team_and_merge_method}}

## Change record

| Date | Change | Reason | Owner |
|---|---|---|---|
| {{yyyy-mm-dd}} | {{change_summary}} | {{reason}} | {{owner}} |

