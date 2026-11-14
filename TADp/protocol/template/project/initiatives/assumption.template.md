<!--
Replace every double-brace token. Give each assumption a stable, sequential
{{decision_prefix}}-Axx ID. Add rows as needed and never reuse retired IDs.
Preserve the exact original statement in its canonical row. Complete one
provenance/ownership row for every item; link external canonical items instead
of duplicating their text or disposition here.
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

## Discovery and canonical ownership

Either the assumption review or open-question review may independently define
new assumptions and new questions from human input or evidence, without a
preceding answer, correction or existing source ID. Each new item begins
unresolved. `Assumed aligned` describes a proposed premise, not a confirmed
decision or permission to implement it. A proposed answer or recommendation
must remain clearly labelled unaccepted.

An assumption owned by this initiative remains here. One owned by another
named initiative remains in that initiative's canonical register. A project-wide
item, or one with no suitable initiative owner, uses the conditional
[project register](../decisions/assumptions-and-open-questions.template.md)
through the coverage map. The originating initiative links its effect or
dependency; it does not absorb the external outcome into its scope.

Before recording an external item or answer, identify the exact target, current
state, owner, governing revision, applicable branch and sufficient write and
decision authority. Sufficient authority permits the proper record update
without another approval solely for external ownership. Otherwise preserve the
exact input in an owned unresolved handoff with proposed owner, blocker and
re-entry condition. Another scaffold, repository, fork or external service
still requires authority naming that target.

## Review method

Every assumption begins unresolved, including any `Assumed aligned` premise.
On the ordinary human path present one ready item at a time. Either review may
record that item's own exact disposition during the same review. A human with
sufficient authority changes its
disposition to:

- `Confirmed` when the statement accurately reflects the intended design;
- `Corrected` when the correction column states the intended replacement; or
- `Not applicable` when the initiative should stop depending on the statement.

If review exposes uncertainty rather than a correction, add or update a stable
decision in [open-questions.template.md](open-questions.template.md). Reconcile each correction
with the architecture, decision register, [source mapping](source-mapping.template.md),
roadmap, and implementation steps before implementing the affected area.

Capture the exact human response and actual authority in a linked receipt
before changing disposition. One response covers several IDs only when it
explicitly and unambiguously identifies the complete set and each required
outcome. A specifically delegated alternative method requires its authority
receipt and rule-specific exception first; retain actual agent authorship,
method, evidence, result and limits for each covered ID. A new ID never inherits
delegation by proximity. Discovery itself grants no answer authority.

Answering a question does not confirm a separate derived assumption. Preserve
its original statement and give it its own disposition, even during the same
review. Do not reopen settled items solely because a related matter is found.
Keep dormant or deferred triggers, prior wording, dispositions and receipt links.

## Item provenance and ownership

Complete one row per stable assumption ID. The exact statement remains in its
canonical assumption row; summaries and external references link that source.
Keep this metadata and every representation of the ID coherent on reconciliation.

| ID | Original source and originating review/evidence | Canonical owner and location | Scope classification | Dependencies and re-entry trigger | Affected records | Disposition evidence or owned handoff |
|---|---|---|---|---|---|---|
| {{decision_prefix}}-A01 | {{source_path_locator_revision_or_event_and_originating_review}} | {{actual_owner_and_canonical_record_link}} | {{in_scope_cross_initiative_or_project_wide}} | {{dependency_IDs_trigger_or_none}} | {{exact_affected_record_links}} | {{unresolved_or_receipt_link_with_human_or_delegated_authorship_or_handoff_blocker}} |

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

Report complete coverage of original assumptions and newly defined items of
either kind, distinguishing their canonical owners, actual answers, unresolved
items, deferred triggers and owned handoffs. A bounded review may finish with
explicit pending external matters; it must not claim those matters resolved.
Every applicable in-scope blocking assumption still needs its own sufficient
disposition, and a pending external dependency blocks the handoff it actually
affects. Review coverage and item resolution establish no initiative acceptance,
implementation, reopening or completion.

| Review cycle | Reviewer | Date | Outcome | Notes |
|---|---|---|---|---|
| Initial assumption review | {{reviewer}} | {{date}} | Assumed aligned; awaiting validation | {{notes}} |

## Change discipline

Keep frozen proposal sources unchanged. Record corrections here, then update
affected initiative documents in the same change. Keep unresolved implementation
choices in [open-questions.template.md](open-questions.template.md) so assumption remains the
stable statement of intended design rather than a second uncertainty register.
