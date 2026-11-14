# Products

Products are delivered outputs with a declared destination. They include
executable code, scripts, SDKs, APIs, product documentation, configuration,
schemas, reports, and other artifacts that realize accepted initiative work.
The actual product may live anywhere appropriate: a repository path, package,
deployment, API route, documentation site, or distribution channel. This
directory is an optional index and durable product-record location, not a rule
that every output must be physically stored under `../../../products`.

## Create a product record

Create or update a record when an output is planned for delivery, first
released, materially changed, deprecated, or retired.

1. Select the [product record source](../template/project/products/product-record.template.md)
   from the protected library when one of these lifecycle events requires a
   record. Copy it to a stable descriptive filename such as `products/payment-api.md`,
   or place the copied record beside its declared product destination. Edit only
   that copy.
2. Assign a **Product ID**, name the product owner, and write the exact actual
   destination. `The application repository` is not enough; name the path,
   package, API route, artifact, or published site.
3. Link the governing implementation initiative, accepted specification section
   or architecture decision, and each applicable authoritative evidence/rule
   claim.
4. Describe the delivered interface or behavior in terms a consumer or operator
   can verify. State support, versioning, compatibility, and deprecation rules
   where relevant.
5. Add evidence of verification and operational safeguards: tests, reviews,
   audits, release artifacts, monitoring, deployment/runbook, backup, recovery,
   security, or support procedures as applicable.
6. Update the change history and remove the instructional comment after all
   tokens are resolved.

## Complete the template precisely

| Template section | Expected content |
|---|---|
| Purpose and consumers | The user, operator, component, or channel served and the outcome delivered. |
| Governing records | Precise initiative, specification, and authoritative evidence links—not a generic directory. |
| Delivered interface or behavior | A public API, command, package surface, documented workflow, or other observable product contract. |
| Verification and operations | Proof of required behavior plus the person/process that handles deployment, failure, recovery, security, and support. |
| Change history | Dated product revision, what changed, and the initiative that authorized it. |

Use `Not applicable — {{reason}}` when a field does not apply. For example,
`Rollback: Not applicable — static documentation has no deployed runtime state`
is a valid decision; omitting rollback information leaves an unresolved review
question.

## Product records and authority

A product record is authoritative for what is actually delivered at its stated
destination and revision. It does **not** create a new requirement merely by
describing current behavior. If the delivered product and its governing
initiative, specification, or authoritative evidence disagree, preserve the
facts and record a conflict. Do not edit a rule or initiative solely to make
the product look compliant.

Product work normally originates in an accepted implementation initiative. A
design initiative may define or revise a specification, and a planning
initiative may supply evidence, but neither type may use a product record to
claim that it delivered product work. Keep the type boundary visible in linked
records.

## Keep records current through the lifecycle

| Lifecycle event | Product record update |
|---|---|
| Planned delivery | Record intended destination, governing initiative/specification, owner, and prerequisites; mark status `Planned`. |
| Release or material change | Update revision/version, behavior, verification results, operations, and change history. |
| Evidence or rule change | Recheck affected behavior, link the revised source, and record migration or exception decisions. |
| Deprecation | State replacement, consumer migration path, support window, owner, and end date. |
| Retirement | Mark status `Retired`, preserve the historical record, final destination, and rationale. |

## Product review checklist

- [ ] The product ID, owner, status, destination, and current revision are
      accurate.
- [ ] Every claimed behavior maps to an accepted initiative/specification and
      applicable authoritative evidence.
- [ ] Verification is specific enough to locate a test, audit, review, or
      operational signal.
- [ ] Compatibility, security, deployment, recovery, and support conditions are
      explicit or documented as not applicable.
- [ ] Changes, deprecations, conflicts, and exceptions have dates and owners.
- [ ] The linked initiative index and product record agree on current status.
