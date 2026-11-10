<!--
Replace every braced placeholder before using this prompt.
-->

# 11. Design delivery

## Use when an accepted design initiative delivers specification changes

Use this prompt only for an accepted `design` initiative. It delivers the
accepted specification and supporting initiative evidence without creating or
changing a product. Observed product behavior is evidence for the design; it is
not an edit target in this stage.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [design delivery prompt](11_design_delivery.md), deliver the
> accepted specification changes for the attached initiative, verify the exact
> design claim, and create its completion evidence without modifying products.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Design delivery prompt** block below. Do not
execute, recurse into, or derive additional work from the example.

## Design delivery prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Deliver the accepted design initiative {initiative} at {initiative_path} on
{initiative_branch}.

Verify that the declared type is exactly `design`, the status is `Accepted` or
`In progress`, and the accepted baseline and acceptance receipt are current. An
`implementation` initiative must use the implementation path; a `planning`
initiative must use the planning delivery prompt.

This stage may create or modify only the specification destinations and
supporting initiative evidence explicitly named by the accepted design scope.
It must not create or modify product source, SDK/API implementation, runtime
configuration, migration execution, deployment assets, product tests, or
another initiative. A specification stored outside the initiative directory is
editable only when the accepted scope names its exact destination and owner.

Before changing a specification, verify that:
- the active branch is exactly {initiative_branch};
- the worktree and branch diff contain no unexplained unrelated work;
- the complete initiative suite, scope assessment, acceptance receipt, accepted
  baseline, roadmap, steps, and source mapping are readable and coherent;
- no unresolved human decision, invariant conflict, dependency, or delivery
  gate blocks the intended specification work;
- every specification destination, owner, consumer, compatibility effect,
  migration obligation, and verification method is unambiguous; and
- the shared `delivery-record.md` and `completion-evidence.md` templates are
  readable and would not overwrite existing initiative-local records.

If any precondition fails, stop the affected work and report every blocker. Do
not change the accepted specification to remove a gate, edit a product to make
the design appear valid, or create an implementation initiative implicitly.

Before editing, create or update {initiative_path}/delivery-record.md from the
shared template. Record the accepted baseline, branch, permitted specification
destinations, prohibited product boundary, and a delivery ledger containing the
accepted step, governing authority, exact specification target, affected
consumers, compatibility or migration effect, and required verification.

When the first specification change begins, append the legal transition to
`In progress` and reconcile the initiative and applicable status records.

Work in dependency order. For each accepted design step:
1. Read the governing evidence, decision, existing specification, observed
   product evidence, consumers, compatibility commitments, and verification.
2. Create or modify only the ledgered specification and supporting evidence.
3. Preserve stable terminology, ownership, identifiers, interfaces, lifecycle,
   failure, security, compatibility, migration, recovery, and deprecation
   commitments unless the accepted design explicitly changes them.
4. Record the change and affected consumers in `delivery-record.md`.
5. Run the meaningful specification checks, such as structured review, schema
   validation, documentation tests, link validation, example validation, or
   contract comparison, and record the actual result and its limits.
6. Stop and report any evidence that requires an invariant revision, new human
   decision, broader scope, or product implementation.

After all accepted design steps, reconcile the specification outputs,
architecture, source mapping, roadmap, steps, affected owner records, and
delivery record. Do not mark a planned product implementation complete; route
it to a separately accepted implementation initiative.

When every in-scope design gate passes, create or update
{initiative_path}/completion-evidence.md. State the exact delivered design
claim, specification destinations and revisions, authoritative-evidence
coverage, verification, consumer and migration effects, and residual work.
Reconcile it with `delivery-record.md` and append the legal `Completed`
transition only when all records agree.

Report every specification and evidence artifact changed, delivery steps,
verification results, lifecycle and status updates, compatibility or migration
effects, required implementation follow-up, and remaining blocker. Do not
create an ad hoc delivery report or modify a product.
```
