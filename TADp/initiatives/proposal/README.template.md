<!--
This file is both the proposal-source inventory template and the handling rule
for proposal artifacts. Add external source files beside it and list each one
below. Replace every double-brace token before review.
-->

# {{initiative_name}} proposal sources

**Initiative:** {{initiative_name}}  
**Status:** Proposed  
**Last updated:** {{date}}
**Version scope:** {{version_scope}}
**Realization suite:** [{{realization_suite_id}}]({{relative_realization_suite_index_path}})
**Canonical project correlation:** [initiative and correlation register]({{relative_initiative_index_path}}#initiative-and-correlation-register)

This directory preserves the material that initiated the work. Proposal source
records intended outcomes and rationale; it does not become an accepted
repository specification merely by being stored here.
[../assumption.template.md](../assumption.template.md) records corrections to assumed intent, and
[../architecture.template.md](../architecture.template.md) records the specification accepted for
this repository.

## Source inventory

| Source | Revision or date | Evidence label | Purpose |
|---|---|---|---|
| [Canonical proposal](proposal.template.md) | {{revision_or_date}} | `../../../evidence/non-authoritative` | Primary statement of intent and scope |
| {{source_link_or_filename}} | {{revision_or_date}} | {{evidence_authoritative_or_non_authoritative}} | {{source_purpose}} |

Use `../../../evidence/authoritative` for binding evidence that governs a specification
or product decision. Use `../../../evidence/non-authoritative` for proposal, contextual,
or exploratory material. A proposal is non-authoritative until an owning
authority accepts the relevant requirement or decision.

## Precedence

<!--
List authoritative evidence before non-authoritative evidence and explain how
conflicts between revisions are resolved. Do not imply that proposal precedence
overrides an accepted repository decision.
-->

1. {{highest_precedence_proposal_source}}
2. {{next_proposal_source}}

Accepted decisions in `../open-questions.md` and the accepted repository
specification in `../architecture.md` govern product work when they
intentionally differ from proposal source. The difference must be recorded in
`../assumption.md` or the relevant decision entry.

## Source handling

- Keep frozen source artifacts unchanged.
- Add a new revision instead of overwriting a frozen source.
- Record source, author or owner, date, and evidence label for every artifact.
- Keep credentials, customer data, generated exports, and unrelated working
  files out of this directory.
- Link every material correction to an assumption or stable decision
  ID.

## Realization handling

A realization is a note used primarily to create a proposal. Preserve it as an
immutable proposal input and link it from the source inventory. A realization
is `../../../evidence/non-authoritative` unless an explicit owning authority separately
classifies it otherwise; it cannot supersede `../../../evidence/authoritative` or an
accepted initiative.

Use the paired suite index as the source of realization-suite identity and
boundary. Do not infer a second suite, initiative, version, or branch from a
supporting note. If the notes do not share one narrow boundary, stop and route
the required split through Stage 0 as a new independent initiative membership.
