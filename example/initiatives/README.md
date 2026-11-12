# Initiatives

This directory holds authoritative initiative records. Every initiative is
authoritative for its declared status, scope, and intended alignment. An
accepted initiative additionally identifies approved work, its evidence basis,
and the expected outcome.

Initiatives must be coherent with one another, with
`../evidence/authoritative`, and with the products they govern. Record and resolve
every conflict explicitly; do not silently rewrite an initiative, product, or
invariant to make another record appear aligned.

Open effort counts as work, including proposed and partial work, without
gaining accepted authority. Use the [work-conflict register](work-conflicts.md)
to preserve incompatible efforts. Apply the
[coherence specification](../evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md)
to completion feedback and require explicit reopening before refining closed
claims. Substantive new claims retain the successor workflow.

Every initiative must own one narrowly bounded outcome and one independently
reviewable acceptance claim. Do not create umbrella or multi-purpose
initiatives. Use separately scoped initiatives for independent outcomes.
Subinitiatives are permitted when they own a smaller dependent outcome inside
a real parent specification, retain their own evidence and gates, and do not
absorb unrelated work.

| Type | Alignment purpose | Permitted primary output |
|---|---|---|
| `implementation` | Products to accepted specifications | Create or modify products; do not modify an existing specification |
| `design` | Specifications to observed products | Create or modify specifications; do not create a new product |
| `planning` | Evidence for other initiatives | Evidence only |
