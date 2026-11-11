<!--
Replace every braced placeholder before using this prompt.
-->

# 10. Implementation execution

## Use when an implementation initiative aligns products to specifications

Use this prompt only after an `implementation` initiative has a complete,
aligned initiative record and is ready to turn its accepted specifications into
products, product documentation, and verification evidence. It performs planned
product work in place; it does not create a new initiative. Execution aligns
products to specifications: `../../evidence/authoritative` is binding, and an
implementation initiative does not modify an existing specification when
product evidence exposes a conflict.
Run it on the initiative
branch prepared by [00_initiative_preparation.md](00_initiative_preparation.md);
use [13_initiative_finalization.md](13_initiative_finalization.md) only after
successful execution to update tracking and open the pull request.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [implementation execution prompt](10_initiative_execution.md), execute
> the fully aligned attached initiative. Implement only its
> accepted roadmap and implementation steps, create the planned products and
> verification evidence in place, then reconcile the work product, initiative,
> and any ledgered in-repository product dependencies against
> `../../evidence/authoritative` and existing work.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Implementation execution prompt** block below. Do
not execute, recurse into, or derive additional work from the example.

## Implementation execution prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Execute the fully aligned {initiative} at {initiative_path} in place.

Verify that the target's declared type is `implementation`. A `design`
initiative modifies specifications and a `planning` initiative creates evidence
only; neither may use this prompt.

Verify that the initiative is `Accepted` or `In progress`, links its explicit
acceptance receipt, and identifies the accepted baseline revision. Do not infer
acceptance from resolved source records or an instruction to implement.

This is the implementation step. Deliver the products, product documentation,
configuration, migrations, tests, operational material, and verification
evidence explicitly required by the initiative's accepted architecture,
implementation roadmap, and implementation steps. Do not create a new
initiative, proposal, initiative suite, or template-derived document.

This prompt authorizes product changes needed to deliver the accepted
implementation initiative. You may create new code and supporting product
artifacts; improve or modify existing code; and modify existing SDK/API
implementations, contracts, and product documentation when they are products
within the accepted scope. You may also change an otherwise out-of-scope
in-repository product boundary, shared SDK/API, or dependent product artifact
when the accepted initiative requires it. Record its relationship to the
accepted work, owner boundary, compatibility and migration effects, and
verification evidence. This authorization never permits changing an existing
specification.

Treat implementation as alignment, not merely code production.
`evidence/authoritative` and the accepted specifications are the hard
constraints. Correct products that conflict with them. If product evidence
exposes a conflict in an existing specification, stop the affected product
work, preserve the specification, and report the required `design` initiative.
Do not use an implementation convenience, a ledgered product dependency, or a
user override to rewrite an existing specification.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Continue to enforce every technical component, profile, placement,
external-party, contract, artifact, and verification requirement.

Before changing products, verify that:
- the active branch is exactly {initiative_branch}, the branch prepared for
  this initiative;
- the canonical work version, realization suite, initiative ID and path,
  version-bearing branch, captured base branch and commit, and reciprocal links
  match one unique project correlation row;
- the target has its complete initiative suite: initiative index, proposal source
  inventory and proposal, assumption record, architecture, source mapping,
  open-question and decision register, implementation roadmap, implementation
  steps, and any linked supporting records;
- the initiative-level alignment is complete, its architecture and delivery
  boundaries are accepted or otherwise explicitly authorized for execution,
  and its status is `Accepted` or `In progress`;
- no unconfirmed assumption relevant to the intended work remains;
  treat every `Assumed aligned`, pending, or otherwise unresolved assumption as
  unconfirmed unless its source record gives it an explicit resolved
  disposition;
- no active, unanswered open question or unresolved derived assumption affects
  the intended work; honor the source register's documented active and blocking
  statuses rather than relying only on a summary or recommendation;
- every SDK/API surface required by the intended work has a compatible recorded
  result from the initiative SDK/API alignment prompt; treat an unresolved
  conflict or blocked surface as a blocker;
- a current, phase-specific result from the implementation-readiness review
  prompt covers the intended phase or scope, and every applicable entry gate is
  ready or has evidence that its stated condition is satisfied; the review is
  read-only, so its result may be supplied in the execution context and need
  not exist as an initiative-local artifact; treat a missing result, a
  `Blocked`, `Deferred`, or non-ready finding, and an unmet `Conditional`
  finding as a blocker;
- no unresolved blocking decision, source conflict, prerequisite, or release
  gate prevents the planned work from starting;
- every intended product change, including a necessary dependent or
  ordinarily out-of-scope change, traces to an accepted implementation step or
  is demonstrably required to align a product with an authorized modification,
  and traces to `evidence/authoritative`; and
- the target paths, package or product owners, compatibility commitments,
  migration limits, verification commands, and allowed external environments
  are unambiguous; and
- the shared `execution-record.md` and `completion-evidence.md` templates are
  readable, their required fields are understood, and neither standard record
  would overwrite an existing initiative-local record.

The shared initiative template defines the standard initiative-record roles. A
historical or initiative-specific supporting document may supply evidence when
the initiative index links it, but it does not satisfy a missing standard
record or substitute for a current phase-specific implementation-readiness
result merely because it has a similar title or topic. Do not require the
read-only readiness prompt to have created a repository artifact. Treat an
undocumented legacy deviation as a blocker; do not rename, migrate, or
normalize initiative records during execution.

Before changing a product artifact, build a complete blocker inventory from
those checks. Include every relevant unconfirmed assumption, unanswered active
question, non-ready readiness finding, unmet condition, conflict, prerequisite,
or gate; do not silently omit an item because another item is already
blocking. For each item, identify its stable ID when available, exact source
and current status, affected implementation step or scope, why it blocks
execution, the evidence or decision needed to remove it, and the consequence
of proceeding without it.

For every product artifact in the reviewed scope, build a step-to-target ledger
before changing it. When the first product change begins, create or update
`{initiative_path}/execution-record.md` from the shared template. Record the
work version, realization suite, canonical-row link, captured base and
initiative branches, governing sources, and the complete
step-to-target ledger there. Record the accepted implementation-step ID, governing
source or mapped contract, exact path or symbol, owning product boundary,
reason the change is needed, and required verification. Treat only ledgered
items as this initiative's work product. A shared package, SDK, API,
deployment asset, or another initiative's path is authorized when an accepted
implementation step names it or when a documented, necessary relationship to
an authorized modification requires it to keep the initiative aligned. For an
otherwise out-of-scope target, record that relationship, the affected owner,
the compatibility or migration effect, and the verification plan before
modifying it. Report a cross-boundary conflict only when no authorized,
verifiable change can resolve it.

An in-repository product mismatch that can be corrected under
`evidence/authoritative` and the accepted specifications is implementation
work. Correct the product and add its verification to the ledger. Treat a
mismatch as a blocker when resolving it requires a specification change, an
unmade product choice, authority beyond the current initiative, an unavailable
external party or system, or a destructive environment action.

If any blocker exists, stop before the affected work and report its exact
source, effect, and required resolution. A specification conflict always
requires a `design` initiative; do not seek or treat a user override as
permission for an `implementation` initiative to edit an existing
specification.

Use all available evidence. Prioritize `evidence/authoritative`, accepted
repository decisions and specifications, released contracts, implemented
behavior and its verification, and completed initiatives. Use in-progress
initiative material only according to its documented evidence label and
precedence. Do not allow an implementation convenience, proposal claim,
initiative assumption, or `evidence/non-authoritative` source to override
established precedent.

Work in dependency order, completing one coherent implementation step at a
time. For each step:
1. Read its objective, scope, dependencies, `evidence/authoritative`,
   migration and rollback
   limits, tests, acceptance conditions, and source-mapping evidence.
2. Implement the declared behavior in the responsible product boundary. Create
   or change source, configuration, schema, migration, test, package,
   deployment, operational, or product-documentation artifacts when the
   accepted step calls for them or when they are necessary to align a dependent
   component with an authorized modification. This includes new code and
   improvements or modifications to existing code and SDK/API artifacts.
3. Preserve public behavior, authority, ownership, identity, lifecycle,
   security, compatibility, migration, recovery, and rollback commitments when
   they remain aligned with `evidence/authoritative` and the accepted
   specifications. Correct the product implementation when it diverges. Do not
   change an existing specification; route a specification conflict to a
   `design` initiative. Never remove, narrow, reinterpret, or replace a product
   contract silently: record the reason, precedence, owner,
   compatibility/migration effect, and tests.
4. Run the step's meaningful tests and the required focused verification. Test
   the intended behavior as well as applicable denial, failure, recovery,
   compatibility, migration, and rollback paths. Do not mark a step complete
   without its required evidence.
5. Keep factual evidence in `execution-record.md`, including paths changed,
   commands run, results, deviations, and unresolved conditions. If implementation
   evidence exposes a specification conflict, preserve the existing
   specification and report the required design work. Never alter scope,
   architecture, decisions, roadmap, or steps to make incomplete work appear
   complete or to weaken a requirement.

Create product artifacts within the initiative's accepted scope and every
documented dependent boundary needed to deliver it. You may create new code,
improve or modify existing code, and create or alter another initiative's
product path
or a shared SDK/API when the ledger establishes that the work is directly
required by the accepted initiative or to align with an authorized modification.
For each such out-of-scope change, retain the owner, compatibility, migration,
and verification evidence. Do not alter a deployment environment, production
service, external account, or destructive migration unless the accepted
implementation step explicitly requires it and this execution is authorized for
that target. If integration work exposes a conflict for which no authorized,
verifiable change is available, report the conflict instead of making an
unsupported change.

After the planned work product is created, complete this scoped reconciliation
in order:

1. Compare product artifacts, behavior, tests, and evidence with the accepted
   specifications, `evidence/authoritative`, implementation steps, and
   acceptance conditions. Correct the work product when it diverges.
2. Compare the product work with affected existing products, SDKs, APIs,
   packages, contracts, and product documentation. Correct only ledgered
   product artifacts needed to make the products agree.
3. Report every conflict that cannot be resolved through a product change. For
   each conflict, identify the product claim, affected specification or
   external product, evidence and precedence, the product change intentionally
   not made, and the required `design` initiative, decision, owner, or evidence.

During final reconciliation, do not modify anything outside the initiative's
own product work except a ledgered dependent product artifact authorized by
this prompt. Do not edit a specification, another initiative's specification
record, a shared specification, or a status record to conceal a mismatch. Do
not alter a deployment environment, external system, or destructive migration
unless an accepted implementation step expressly authorizes that target.

Keep the initiative's lifecycle and tracking truthful. Record `In progress`
only when implementation has actually begun, and record execution completion
only after every in-scope acceptance and qualification gate has evidence.
When every gate passes, create or update
`{initiative_path}/completion-evidence.md` from the shared template and state
the exact completed claim, evidence for every acceptance condition, verification
results, remaining out-of-claim follow-up, and the responsible reviewer. Reconcile
that record with `execution-record.md` and the initiative suite before recording
`Completed`.
Update {initiative_status_path}, the initiative index, and affected parent or
dependent tracking records when needed to reflect that evidence; retain every
deferred production, release, deployment, risk, and blocker statement. These
execution-stage updates do not perform branch finalization, merge, release, or
pull-request work. When all required work and gates pass, hand the aligned
initiative to the [finalize-initiative prompt](13_initiative_finalization.md),
which owns final branch tracking, push, and pull-request creation. Do not
finalize a partial or blocked execution.

After execution, report the product artifacts created or changed, including new
code, improvements to existing code, SDK/API changes, and authorized dependent
out-of-scope changes; the implementation steps completed; commands and
verification results; compatibility or migration effects; initiative-status
updates performed or still externally blocked; and every remaining blocker,
deferred item, unresolvable conflict, or failed gate. Do not create an ad hoc
implementation report; use `execution-record.md` and `completion-evidence.md`
as the standard records unless an accepted implementation step explicitly
requires another artifact. When every gate passed, state that the
finalization prompt is the next step. Include the final correlation and branch
verification in the report.
```

