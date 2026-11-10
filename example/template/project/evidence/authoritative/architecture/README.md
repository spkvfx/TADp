# Architectural evidence

This directory holds the accepted, durable architecture that governs the
project. Architecture here is a **suite of narrowly scoped records**, not a
single accumulating `architecture.md` narrative. Each record owns one reviewable
subject: a system boundary, an interaction contract, or a durable decision.
The suite as a whole describes the system; individual files stay small enough
to change, review, cite, and supersede independently.

## Select the right architecture template

| Template | Use one file for | Do not put here | Typical filename |
|---|---|---|---|
| [system-boundary.template.md](system-boundary.template.md) | One system, subsystem, or ownership boundary | The full API contract of every adjacent system or the reasoning for an unrelated choice | `billing-service-boundary.md` |
| [component-contract.template.md](component-contract.template.md) | One producer/consumer interaction or shared artifact contract | Overall component ownership or unrelated decisions | `orders-to-billing-contract.md` |
| [architecture-decision.template.md](architecture-decision.template.md) | One accepted durable architectural choice | An open question, a work plan, or a complete system design | `ADR-012-event-ordering.md` |

Use links—not copied paragraphs—to connect the records. For example, a payment
service boundary links to its `checkout-to-payment` contract, and that contract
links to the decision that selects its delivery semantics. This makes it clear
which record changes when only the contract version changes.

## Build an architecture suite

Use this sequence for a new or substantially changed area:

1. **Name the boundary.** Start with one
   [system-boundary template](system-boundary.template.md) per independently
   owned system, service, module, or bounded subsystem. Define what is inside,
   what is explicitly outside, who writes authoritative state, and where
   recovery responsibility stops.
2. **Document material interactions.** For every interface whose behavior,
   authorization, reliability, or versioning matters, copy
   [component-contract.template.md](component-contract.template.md). A
   contract needs named producer and consumer, validated input, success and
   failure behavior, compatibility rules, and verification.
3. **Record durable choices.** When alternatives exist and the selected option
   affects future design or product work, copy
   [architecture-decision.template.md](architecture-decision.template.md).
   An accepted decision is concise: one question, one direction, consequences,
   alternatives, and proof of acceptance. Keep undecided questions in the
   relevant initiative until a decision is accepted.
4. **Link outward.** Cite applicable rules and other authoritative evidence in
   the record. Link the initiative that proposed or implemented a change, and
   link product verification once work is delivered.
5. **Review the suite as a graph.** Check that each boundary has the needed
   contracts, each contract has a boundary owner, each durable trade-off has a
   decision record, and no two records make incompatible claims.

## Keep records narrowly scoped

Use the following tests before adding a section to an existing record:

- Can the subject be accepted, revised, or deprecated separately? Create a new
  file.
- Does the subject have a different owner, verification method, or lifecycle?
  Create a new file.
- Is it a specific interaction between two parties? Use a contract record,
  even if it is mentioned by both boundary records.
- Is it a choice between alternatives with lasting consequences? Use a decision
  record, even if the choice is motivated by a boundary or contract.
- Is it implementation detail that does not change an ownership or interface
  contract? Keep it with the product or initiative, not durable architecture.

Conversely, do not split a single inseparable contract into tiny fragments that
cannot be understood together. A file should have one primary question and one
set of owners; related tables and failure cases that answer that question stay
in the same file.

## Fill the templates precisely

All template files begin with an HTML instruction comment. Copy a template to a
descriptive filename, replace every `{{token}}`, then remove the comment.
Retain headings and write `Not applicable — {{reason}}` when a standard field
does not apply.

### System boundary records

The **boundary statement** must identify the inside edge and the excluded edge
in one paragraph. The responsibility table assigns work and explicitly says
what the boundary must not own. The inputs/outputs table names every material
counterparty and shows where input becomes validated. The state table names the
system of record and recovery owner; do not label a cache or projection as the
authoritative state without explaining why. Complete the invariant section with
links to binding rules or evidence, and put the matching test, review, or
operational check in verification.

### Component contract records

One contract record covers one interaction, not a product's entire API catalog.
For each operation or event, define required input, success result, failure
result, validation, authorization, retry/idempotency, ordering, versioning, and
observability. State exactly who owns a timeout, duplicate, invalid message, or
partial failure. A client expectation is not a contract until the producer and
consumer owners accept the same record.

### Decision records

Write the **decision question** as one answerable question. Cite binding
evidence separately from contextual observations in the context table. The
**decision** section must be normative and unambiguous: a future contributor
can tell what to do without rereading the alternatives. Consequences include
costs and required follow-up, not just benefits. Mark a record `Proposed` while
authority is pending and `Accepted` only when the named decision owner has
approved it.

## Relationship to initiative architecture

The standard initiative suite contains an `architecture.md` file for an
initiative-specific specification and baseline. It can cite records in this
directory and propose an architectural change, but it does not silently edit a
durable accepted boundary, contract, or decision. When an initiative change is
accepted as lasting project architecture, create or revise the focused record
here, preserve the predecessor, and link both records.

## Status, revision, and retirement

Use `Draft` or `Proposed` while a record is being reviewed; use `Accepted` only
after its named authority accepts it. Use `Superseded` with a direct successor
link when a new record replaces it. Retire a record only when it no longer
governs any supported system or product; retain it for historical traceability.
Do not overwrite an accepted record without a revision entry, affected-record
review, and an effective date.

## Architecture review checklist

- [ ] Every file has one primary boundary, contract, or decision question.
- [ ] Every record names its owner, status, review date, and related records.
- [ ] Boundary records identify authoritative state, validation, and recovery.
- [ ] Contract records define success, failure, compatibility, and verification.
- [ ] Decision records cite binding evidence, alternatives, consequences, and
      acceptance.
- [ ] Initiatives and products cite the precise architecture record and section.
- [ ] Superseded records remain linked and discoverable.
