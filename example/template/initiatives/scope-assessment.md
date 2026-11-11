<!--
Replace every double-brace token, remove instructional comments, and retain all
sections. This is an initial initiative artifact. It assesses scope; it does
not accept the initiative or resolve a human decision.
-->

# {{initiative_name}} scope assessment

**Initiative:** {{initiative_name}}  
**Initiative type:** `{{initiative_type}}`  
**Assessment status:** {{draft_reviewed_or_blocked}}  
**Last updated:** {{yyyy-mm-dd}}  

## Bounded outcome

**Single outcome:** {{observable_outcome}}  
**Beneficiary:** {{user_owner_or_system}}  
**Accountable owner:** {{human_or_team}}  
**Authority boundary:** {{governing_specification_and_invariant_boundary}}  
**Acceptance claim:** {{one_independently_reviewable_claim}}  

## Cohesion assessment

| Dimension | One coherent unit? | Evidence and rationale |
|---|---|---|
| Outcome and beneficiary | {{yes_or_no}} | {{evidence}} |
| Accountable owner | {{yes_or_no}} | {{evidence}} |
| Authority boundary | {{yes_or_no}} | {{evidence}} |
| Initiative type and output class | {{yes_or_no}} | {{evidence}} |
| Acceptance and verification | {{yes_or_no}} | {{evidence}} |
| Lifecycle and release disposition | {{yes_or_no}} | {{evidence}} |
| Compatibility, migration, and recovery | {{yes_or_no}} | {{evidence}} |

## Split-trigger review

| Trigger | Present? | Affected portion | Disposition or human decision needed |
|---|---|---|---|
| Independently acceptable outcome | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |
| Different accountable owner | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |
| Different authority or specification boundary | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |
| Different initiative type | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |
| Separable verification, release, cancellation, or completion | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |
| Unrelated product destination or compatibility obligation | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |
| Independent lifecycle | {{yes_or_no}} | {{scope_or_na}} | {{split_rationale_or_decision}} |

## Placement

**Placement:** {{root_sibling_or_subinitiative}}  
**Parent requirement, if any:** {{exact_parent_requirement_or_na}}  
**Boundary retained by parent:** {{retained_scope_or_na}}  
**Sibling relationships:** {{initiative_links_or_none}}  

## Explicit exclusions

- {{excluded_outcome_and_owner}}
- {{excluded_outcome_and_owner}}

## Assessment result

{{narrow_enough_split_required_or_blocked_pending_human_decision}}

When a split is mandatory, identify each separately bounded outcome without
allocating identity in this assessment. Each split enters Stage 0 and receives
its own canonical work version, realization suite, self-contained initiative,
and dedicated branch. Do not reuse this initiative's tuple as an umbrella.


