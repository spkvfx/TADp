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
**TADp project root:** {{resolved_scaffold_installation_directory}}
**Git worktree root:** {{repository_root}}
**Project path relative to Git root:** {{verified_prefix_or_dot}}
**Project-root revision:** {{coherent_revision_commit_or_not_yet_adopted}}
**Default integration branch:** {{actual_branch_or_not_assumed}}  
**Remote operations:** {{separate_authority_and_external_constraints}}
**Version scope revision effective point:** {{coherent_revision_commit_or_not_yet_adopted}}
**Version scope migration ledger:** [Scope migration]({{relative_version_scope_migration_ledger_path}})
**Correlation revision effective point:** {{commit_or_not_yet_adopted}}
**Correlation migration ledger:** [{{ledger_name}}]({{relative_migration_ledger_path}})
**Coherence revision baseline:** {{pre_adoption_git_commit_or_not_yet_adopted}}
**Work-conflict register:** [Work conflicts]({{relative_work_conflict_register_path}})
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
| Binding evidence | `evidence/authoritative` | {{architecture_rules_or_other_binding_sources}} | {{owner}} |
| Contextual evidence | `evidence/non-authoritative` | {{research_observations_or_realizations}} | {{owner}} |
| Initiative records | `initiatives` | {{accepted_work_records}} | {{owner}} |
| Delivered products | `products` or {{actual_destination}} | {{code_documentation_or_other_outputs}} | {{owner}} |

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

The scope registry initiatives/version-scopes.md owns exact major/minor/patch
scope identity and topology. The initiative index owns one membership row per
initiative, its exact source provenance and current cycle execution assignment.
Scope READMEs and status link those owners; initiative READMEs own lifecycle.
Sources remain non-authoritative and may route to several narrow targets.
Scopes and declared shared scope branches may be reused. Initiative IDs are
independent of scope numbers. Record fit choices, target/source scopes and
LLM authorship under the exact bounded intake delegation before applying them.

Adopt prospectively at the recorded coherent commit. Existing one-to-one
correlation records keep their compatible earlier revision and complete ledger
disposition until explicit evidence-backed migration. Preserve legacy scopes,
paths, branch/base and source identities, historical PR evidence and claims.
Neither synchronization nor scope notation authorizes migration, path moves,
reparenting, acceptance or completion.
## Operating cadence

| Event | Required review | Record to update |
|---|---|---|
| {{new_evidence_arrives}} | {{classification_and_owner_review}} | {{evidence_register_or_record}} |
| {{initiative_is_accepted_or_changes_status}} | {{scope_and_dependency_review}} | {{initiative_index}} |
| {{product_is_released}} | {{traceability_and_verification_review}} | {{product_record}} |
| {{scheduled_review}} | {{owner_and_staleness_review}} | {{this_profile_and_affected_records}} |
| Initiative alignment or completion | Compare current open effort and affected closed claims; preserve and route incompatibilities | Owning review, completion evidence, and work-conflict register |

The coherence revision baseline identifies the Git commit immediately before
adoption. Historical terminal claims are preserved without retroactive review;
new or changed work follows the adopted coherence rule. Open effort counts as
work to reconcile, not as authority or execution approval. Refine closed claims only after recorded reopening under adopted bounded
intake delegation or separate human authority; coherent same-outcome claim changes may retain identity; independent outcomes
and incompatible type/owner/authority boundaries require separate initiatives.

## Git workflow

The project root is the installed scaffold directory, contained in a valid Git
worktree under specification 05. The Git root supplies shared refs, index,
worktree state and hook configuration without widening file ownership.
Record hook coordination and any incompatible branch roles before action.
This project requires Git and recorded dedicated/shared execution per cycle.
Use exact scope branches, major from captured project integration base, minor
from matching major, patch from matching minor, and dedicated member from scope.
Record immutable creation bases and initiative-specific shared-branch evidence.
Human close/finalize instructions supply bounded local immediate-parent merge
authority after all gates; pushes require separate authority.

- **Initiative branch convention:** {{branch_naming_rule}}
- **Required checks:** {{checks_or_none_beyond_initiative_gates}}
- **Commit requirements:** {{signing_message_or_review_requirements}}
- **Merge authority:** {{human_or_team_and_merge_method}}

## Change record

| Date | Change | Reason | Owner |
|---|---|---|---|
| {{yyyy-mm-dd}} | {{change_summary}} | {{reason}} | {{owner}} |
