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
claims. Under explicit scope-revision adoption, coherent same-outcome revision
may retain identity; independent outcomes still require separate work.

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

## Find the governing record

The [initiative index](initiative-index.md) owns recorded identity and
membership. After explicit version-scope adoption,
`initiatives/version-scopes.md` owns scope topology and closure, while each
initiative README owns its lifecycle. New governed records use
`initiatives/<scope>/<type>/<id-and-slug>/`; historical paths remain under
their recorded compatible revision until explicitly migrated. A scope, branch,
or index row establishes no acceptance or completion by itself.

An actual human instruction to process an identified realization under adopted
[specification 09](../evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
delegates the bounded fit, placement, coherent revision, and necessary reopening
decisions. Record the instruction and each agent-authored disposition before
action. Preserve exact source notes, source and target scopes, prior claims,
and execution assignments. Independent outcomes and incompatible type, owner,
or authority boundaries require separate initiatives. Changed accepted claims
return through alignment and renewed human acceptance before delivery.

## Prepare and use initiative documents

The [canonical coverage map](../template/TEMPLATE-COVERAGE.md) identifies each
file or embedded section, its source, destination, trigger, owner, evidence,
and checks. The same initial suite serves all three initiative types. Stage 0
creates only the preparation skeleton for a new allocation; Stage 1 owns its
proposal, and Stage 3 completes the initial suite. Decision receipts and
type-specific delivery/completion records need their actual later triggering
events. The ordinary Stage 9 readiness template supplies a response shape.

Each invoked step first performs bounded
[documentary prerequisite recovery](../docs/guides/template-prerequisites-migration.md)
through the owning stages. Reuse valid records; capture sufficient existing
human decisions without asking for the same decision again. Missing facts,
identity, authority, actual work, or passing verification remain blockers.
This preparation does not accept an initiative or start its delivery path.

Use the [workflow guide](../docs/development/initiative-workflow.md) for stages
0 through 13, decision receipts, separate acceptance, delivery records, and
completion feedback. Finalizing one initiative does not close its scope;
scope closure and immediate-parent integration have their own inventories and
authority under [specification 05](../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md).
