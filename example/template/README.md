# Initiative templates

This directory groups reusable initiative material by purpose.

## Protected source boundary

This complete tree is protected reusable source. Read or copy it during
ordinary work; do not edit, fill, rename, move, or delete files in place.
`AGENTS.md` carries that boundary into Codex's directory-scoped instructions,
and `.tadp-lock.json` lets the validator detect content or file-set drift.

Instantiate a record outside `template/` and edit the copy. A change to this
tree requires an explicit human request for the exact reusable-source change,
compatibility and migration review, affected-consumer updates, verification,
and a governed lock refresh. A lock refresh is not a repair for an unintended
template edit.

## Protocol vocabulary

- `../evidence/authoritative` replaces the former `invariants` label. It identifies
  binding evidence that governs a specification or product decision.
- `../evidence/non-authoritative` identifies contextual, exploratory, or supporting
  evidence. It can inform a decision but cannot by itself override
  `../evidence/authoritative`.
- A **product** is output material placed in a repository, distribution channel,
  or other declared destination. Products include executable code, scripts,
  SDKs, APIs, product documentation, and similar deliverables. A document that
  defines what a product must do is a **specification**, not a product merely
  because it is a document.

- [Initiative templates](initiatives/README.md) define the standard initiative
  record: proposal sources, assumptions, scope, specifications, evidence
  mapping, decisions, delivery roadmap, delivery steps, type-specific work
  records, completion evidence, and the minimal preparation skeletons used at
  Stage 0.
- [Project templates](project/README.md) define project profile and initiative
  indexes, the canonical realization-suite index, and the pre-effective
  correlation migration ledger, plus the work-conflict register and coherence
  adoption baseline.
- [Initiative prompts](prompts/README.md) provide focused workflows for
  preparing an initiative branch, proposal creation and alignment, initiative
  creation and alignment, human-led assumption and decision reviews, explicit
  acceptance, type-specific delivery, implementation readiness, and
  finalization.

Use the initiative templates to structure a new initiative. Use a prompt only
for its named workflow; the initiative type, evidence classification, and
repository evidence continue to govern the outcome.

## Protocol directory readmes

The reusable templates operate with the protocol directories at this project
root:

- [Authoritative evidence](../evidence/authoritative/README.md) provides
  invariant conditions that initiatives and products must meet.
- [Non-authoritative evidence](../evidence/non-authoritative/README.md)
  provides clues and context only; it cannot supersede binding evidence.
- [Realizations](../evidence/non-authoritative/realizations/README.md) provide
  permanently non-authoritative notes for proposals from their sole canonical
  location.
- [Initiatives](../initiatives/README.md) hold authoritative, conflict-resolved
  initiative records.
- [Products](../products/README.md) identify authoritative output placements.

Keep the copied initiative record coherent with these directories. Do not use a
template, proposal, realization, or product convenience to silently alter
`../evidence/authoritative`.

## Scope grouping and integration sources

Newly governed initiative records belong under initiatives/<scope>/<type>/<id-and-slug>/.
The project sources include the canonical [scope registry](project/initiatives/version-scopes.template.md),
[scope navigation README](project/initiatives/scope-README.template.md),
[membership index](project/initiatives/initiative-index.template.md), and
[prospective adoption ledger](project/initiatives/version-scope-migration-ledger.template.md).
Stage 0 records fit-based routing before allocation, including coherent revision
and necessary reopening under its bounded adopted intake authority. It chooses
a dedicated child or declared shared scope assignment with per-cycle history.
[Scope closure](prompts/scope_closure.md) is separate from member finalization
and integrates only into the recorded immediate parent after its own gates.
Preserve legacy paths and claims during distribution synchronization.
When instantiating an initiative in the grouped layout, recompute all relative
links from its actual scope/type depth rather than copying navigation paths
from the reusable source location.

The [integration receipt source](project/initiatives/integration-receipt.template.md)
records exact current-cycle source/target Git evidence, closure authority,
post-integration checks and explicit exclusion/transfer/no-deliverable outcomes.
