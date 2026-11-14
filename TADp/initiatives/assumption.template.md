<!--
Replace every double-brace token. Give each assumption a stable, sequential
{{decision_prefix}}-Axx ID. Add rows as needed and never reuse retired IDs.
-->

# {{initiative_name}} assumption

**Initiative:** {{initiative_name}}  
**Status:** Proposed  
**Last updated:** {{date}}  
**Assumption review:** Assumed aligned; awaiting validation

This document records the high-confidence assumptions that shape the proposed
[architecture](architecture.template.md). The initiative proceeds as though these
statements describe the intended design until a reviewer confirms or corrects
them. Reviewing them before the initiative produces its permitted output keeps
a misunderstood proposal from hardening into specifications, products, or
evidence.

[Open questions](open-questions.template.md) records genuine uncertainty about choices
that still need decisions. This document records the intended boundaries within
which those questions should be answered.

## Review method

Every assumption begins as `Assumed aligned`. A reviewer changes its
disposition to:

- `Confirmed` when the statement accurately reflects the intended design;
- `Corrected` when the correction column states the intended replacement; or
- `Not applicable` when the initiative should stop depending on the statement.

If review exposes uncertainty rather than a correction, add or update a stable
decision in [open-questions.template.md](open-questions.template.md). Reconcile each correction
with the architecture, decision register, [source mapping](source-mapping.template.md),
roadmap, and implementation steps before implementing the affected area.

## Boundary between assumption and open questions

| Assumption | Implementation question that may remain open |
|---|---|
| {{stable_statement_of_intent}} | {{mechanism_schema_policy_or_rollout_choice}} |
| {{stable_statement_of_intent}} | {{mechanism_schema_policy_or_rollout_choice}} |

## Product and scope

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| {{decision_prefix}}-A01 | {{product_outcome_or_scope_boundary}} | Proposal, scope, acceptance outcomes, and rollout | Assumed aligned | - |

## Domain and authority

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| {{decision_prefix}}-A02 | {{identity_ownership_or_authority_assumption}} | Domain model, persistence, APIs, and authorization | Assumed aligned | - |

## System boundaries and dependencies

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| {{decision_prefix}}-A03 | {{package_service_or_initiative_boundary}} | Architecture, dependencies, composition, and deployment | Assumed aligned | - |

## Data and lifecycle

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| {{decision_prefix}}-A04 | {{data_identity_state_or_retention_assumption}} | Schemas, migrations, lifecycle, recovery, and compatibility | Assumed aligned | - |

## Operations security and failure behavior

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| {{decision_prefix}}-A05 | {{operational_security_or_failure_assumption}} | Operations, trust, failure handling, tests, and release gates | Assumed aligned | - |

## Cross-initiative compatibility

| ID | Assumption currently treated as aligned | If corrected, revisit | Disposition | Correction or note |
|---|---|---|---|---|
| {{decision_prefix}}-A06 | {{compatibility_assumption}} | Dependent initiatives, shared contracts, sequencing, and migration | Assumed aligned | - |

## Validation record

The assumption review is complete when every row is confirmed, corrected, or
marked not applicable; every correction is reconciled into downstream initiative
records;
and the overall outcome is recorded here.

| Review cycle | Reviewer | Date | Outcome | Notes |
|---|---|---|---|---|
| Initial assumption review | {{reviewer}} | {{date}} | Assumed aligned; awaiting validation | {{notes}} |

## Change discipline

Keep frozen proposal sources unchanged. Record corrections here, then update
affected initiative documents in the same change. Keep unresolved implementation
choices in [open-questions.template.md](open-questions.template.md) so assumption remains the
stable statement of intended design rather than a second uncertainty register.
