# Rules evidence

This directory contains the project's independently enforceable rules. A rule
is a normative statement that a product, initiative, component, or operator
must follow. It may encode a policy, security or compliance control, naming or
compatibility standard, operating constraint, or acceptance condition.

One file should state one rule or one inseparable rule set. That keeps scope,
exceptions, ownership, and verification unambiguous. Do not place an informal
preference, a future idea, or a product-specific implementation note here just
because it sounds prescriptive.

## Create a rule

1. Copy [rule.template.md](rule.template.md) to a descriptive, stable name such
   as `RULE-003-data-retention.md`.
2. Give the rule a permanent **Rule ID**. Do not reuse IDs, even when a rule is
   retired or superseded.
3. State the **normative rule** using clear language such as `must`, `must not`,
   or `is required to`. A reviewer should be able to decide compliance without
   inferring intent from a paragraph of background.
4. Define its **applicability**: products, components, data, people, and
   environments covered, plus deliberate exclusions and why they are excluded.
5. List the concrete practices or controls required to comply. The list may be
   detailed, but it must remain tied to the single rule stated above.
6. Specify a verification method, retained evidence, reviewer, owner, source,
   effective date, and review cadence.
7. Remove the instructional comment only after all placeholders are resolved.

## Write rules that can be followed

| Weak wording | Better rule | Why it is better |
|---|---|---|
| `Use secure storage.` | `Secrets must be stored only in the approved secrets service; repositories and logs must not contain plaintext secrets.` | States the required and prohibited behavior. |
| `Avoid breaking changes.` | `A public API change must be additive until all supported clients have migrated; removal requires a recorded deprecation period.` | Defines the boundary and lifecycle. |
| `Test thoroughly.` | `Every payment-state transition must have a deterministic unit test and a recovery-path integration test.` | Identifies behavior and proof. |

Put explanatory rationale in the source or applicability sections, but do not
let rationale obscure the rule itself. If a different scope needs a different
exception, verification method, or owner, create another rule and link them.

## Use rules in other records

An initiative cites a rule ID and states how it affects scope, a design, or an
acceptance gate. A product record maps the rule to an implementation behavior
and evidence of verification. A boundary or contract record links the rule when
it constrains ownership, interface behavior, data handling, or operations.

Never copy a rule into those records as an independent source of truth. If
product work appears to violate a rule, record a conflict and route it to the
rule owner. The implementation does not create an implicit exception.

## Exceptions, revisions, and retirement

An exception needs a named approving authority, exact scope, duration or review
date, reason, and compensating controls. Write it as a linked record or an
explicit exception section; an unreviewed note in code or an initiative is not
an exception.

When a rule changes, retain the prior file and update its status to
`Superseded` with a successor link. State the new rule's effective date,
migration period, affected products, and whether past releases are evaluated
under the old or new rule. Retire a rule only when it no longer governs any
supported scope.

## Rule review checklist

- [ ] The rule is one clear, testable normative statement.
- [ ] Scope, exclusions, owner, authority, effective date, and source are
      explicit.
- [ ] Verification evidence and the responsible reviewer are specified.
- [ ] Initiative, architecture, and product citations use the rule ID.
- [ ] Exceptions are authorized, time-bounded, and linked.
- [ ] Superseded rules remain available with their replacement relationship.
