# Implementation initiatives

Use this directory for an initiative whose permitted primary output is a
**product change**: code, a script, an SDK, API, configuration, schema, product
documentation, or another delivered artifact. An implementation initiative
realizes an accepted specification. It is not allowed to silently revise that
specification when delivery becomes difficult or when the observed product
reveals a gap.

## Start an implementation initiative

1. Use Stage 0 to select or allocate the exact
   initiatives/<scope>/<type>/<id-and-slug>/ destination under the adopted
   workflow. This baseline type folder explains the output boundary; it does
   not own unscoped live initiatives or allocate identity.
2. Use the [coverage map](../../template/TEMPLATE-COVERAGE.md) and
   [common initiative sources](../initiative-README.template.md) to instantiate
   only the records owned by the current activity. Remove .template from
   instance names and recalculate links. Do not copy conditional late-stage
   records during initial creation.
3. Link the accepted governing specification and precise sections. If no
   accepted specification exists, create or route a design initiative first.
4. List every product destination: repository path, package, API route,
   documentation site, configuration target, migration, or deployment artifact.
   A product does not need to be physically below `../../../../products` to be governed.
5. Record preconditions, evidence, dependencies, verification, deployment,
   rollback, recovery, and release gates before material product work begins.
6. Add the initiative to the parent index and obtain the required acceptance
   before status becomes `Accepted`.

## Fill the implementation template

| Template section | Expected content |
|---|---|
| Intended product outcome | Observable delivered behavior, not merely a coding task. |
| Product boundary | Each product destination, change, governing specification section, and owner. |
| Preconditions | Accepted decisions, evidence, environments, dependencies, migrations, or approvals required before work starts. |
| Delivery and verification | Coherent steps with a test, review, audit, or operational check and a rollback/recovery consideration. |
| Open issues and escalation | Issues that could block delivery, their product impact, owner, and routing—especially a design initiative when specification change is needed. |
| Completion gate | Proof that product behavior, verification, recovery, release records, and traceability are complete. |

Do not delete an unfinished section. State the gap and its stop condition. For
example, `Migration rollback: Not applicable — the change adds no durable
state` is reviewable; an empty field is not.

## Protect the specification boundary

Implementation may choose ordinary construction details that remain within an
accepted specification. It must stop the affected work and route to a design
initiative if it needs to change any of the following:

- an externally observable required behavior or acceptance condition;
- a durable architecture boundary, interface contract, or authoritative rule;
- the product ownership, data authority, or compatibility promise;
- the scope of users, environments, or products the specification covers; or
- a required verification, rollout, migration, or recovery guarantee.

Record the discovery as an issue with a clear product impact. Continue only
work that is unaffected by the missing or changed specification. The route to a
design initiative prevents a product convenience from becoming unreviewed
architecture.

## Delivery, verification, and release

For each destination, link the governing evidence and specification to the
concrete proof: a test, contract test, audit, reviewed document, deployment
record, monitoring signal, or recovery exercise. Verify failure behavior as
well as success behavior when the product handles state, network, authorization,
or data changes. Record feature gates, supported mixed-version behavior,
migration ordering, rollback limits, and the owner of recovery actions.

At completion, create or update the appropriate product record. It should name
the actual destination, current version/revision, initiative, specification,
authoritative evidence, verification, and operational safeguards. The product
record is the durable answer to `what was delivered and how do we know it
aligns?`.

## Completion checklist

- [ ] Each product change has an accepted specification, evidence basis, owner,
      and destination.
- [ ] Tests, reviews, audits, or operational checks prove each required behavior.
- [ ] Compatibility, migration, release, rollback, and recovery requirements
      are explicit or marked not applicable with reasons.
- [ ] A required specification change was routed to design before the affected
      product work proceeded.
- [ ] Product records and the initiative index reflect the delivered state.
- [ ] Deferred work, remaining risk, and operational ownership are visible.
