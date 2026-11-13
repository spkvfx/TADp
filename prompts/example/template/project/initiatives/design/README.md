# Design initiatives

Use this directory for an initiative whose permitted primary output is a new or
revised **specification**. A design initiative compares the observed product
state with binding evidence and makes the intended behavior, boundaries,
interfaces, acceptance conditions, and unresolved decisions explicit. It may
create supporting initiative evidence, but it does not create a new product to
demonstrate that the specification is correct.

## Start a design initiative

1. Create a unique directory such as
   `INIT-DSN-001-payment-state-model/` beneath this directory.
2. Copy the complete
   [canonical initiative template suite](../../../initiatives/README.md) into
   it. Every design initiative uses the canonical suite.
3. Record the **observed product baseline** before stating the intended design.
   Cite actual code, tests, APIs, configuration, operational evidence, or
   product records; do not infer current behavior from a proposal.
4. Cite every binding source by evidence/rule/architecture ID and precise
   section. Record contextual studies separately from mandates.
5. State the specification changes and their acceptance conditions. If a
   product will need to change, name a future or dependent implementation
   initiative rather than making the change here.
6. Register the initiative in the parent initiative index and obtain review
   before status becomes `Accepted`.

## Complete the template accurately

| Template section | What a reviewer needs to see |
|---|---|
| Intended specification outcome | An observable contract, behavior, or boundary—not a vague goal such as `improve payments`. |
| Included and excluded scope | Which specifications and evidence may change, and which product work belongs elsewhere. |
| Evidence and observed baseline | Precise source or product locators, current behavior, and the design consequence of each. |
| Proposed specification changes | One row per affected contract or document, its required behavior, acceptance condition, and implementation consumer. |
| Open decisions and risks | A stable question/risk ID, owner, and the evidence or decision gate needed to resolve it. |
| Acceptance | Proof that the specification is coherent with evidence, observed products, and its downstream implementation plan. |

Replace all `{{tokens}}` and remove the instruction comment. For a non-applicable
field, write `Not applicable — {{reason}}`; this proves the field was considered
rather than accidentally omitted.

## Specification versus product work

Design work may define or revise what a product **must do**. It may update the
initiative's architecture/specification, acceptance criteria, source mapping,
or supporting design evidence. It must not implement a new code path, alter a
production configuration, publish an API, or create a documentation product
solely to make its own specification look aligned.

If examination reveals a pre-existing product mismatch, record it as observed
state and a conflict or design input. Do not silently rewrite the evidence or
the product description. A later implementation initiative owns the product
change; it must cite the accepted design specification and prove the resulting
behavior.

## Acceptance gate for a design initiative

Before completing or handing the design to implementation, confirm:

- [ ] The product baseline is evidence-backed and distinct from the desired
      specification.
- [ ] Every binding requirement is mapped to a specification section and
      acceptance condition.
- [ ] Ownership, data, interface, failure, compatibility, and operational
      boundaries are explicit where applicable.
- [ ] Blocking decisions are accepted or routed with owners and stop conditions.
- [ ] Every required product change has a named implementation consumer.
- [ ] The design did not create a product as part of its own output.

## Maintain the record

When new evidence or an accepted decision changes the design, update the
baseline, scope, specification, source mapping, and downstream handoff in the
same reviewable change. Keep the initiative status and parent index current.
If a later design replaces this one, mark it `Superseded` and link the successor
rather than erasing the original rationale.
