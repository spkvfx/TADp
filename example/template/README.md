# Initiative templates

This directory groups reusable initiative material by purpose.

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
  records, and completion evidence.
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
- [Realizations](../realizations/README.md) provide notes for proposals.
- [Initiatives](../initiatives/README.md) hold authoritative, conflict-resolved
  initiative records.
- [Products](../products/README.md) identify authoritative output placements.

Keep the copied initiative record coherent with these directories. Do not use a
template, proposal, realization, or product convenience to silently alter
`../evidence/authoritative`.
