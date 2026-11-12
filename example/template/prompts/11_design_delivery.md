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
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md and the canonical
prompt keyword specification at evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md.
The following human-response and gate-stop instructions state the ordinary
required path. Apply only specifically authorized, recorded exceptions under
that specification; a mode request alone supplies no waiver. Record effective
settings for each source-position block before dispatch or retry, preserve
locks and truthful evidence, and retain ordinary lifecycle meanings. Preview
work remains response-only; local resource restrictions and independent review
obligations compose with gates. The shared contract and this prompt retain
all unexcepted preconditions, edit boundaries, verification, and reporting.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
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
another initiative outside the exact accepted specification destinations.
A specification stored outside the initiative directory is
editable only when the accepted scope names its exact destination and owner.

Before changing a specification, verify that:
- the active branch is exactly {initiative_branch};
- the exact version scope, realization suite, initiative ID and path,
  recorded execution branch, captured base branch and commit, and reciprocal links
  match one unique project correlation row;
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
destinations, prohibited product boundary, work version, suite, canonical-row
link, captured base, and a delivery ledger containing the
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

Before that transition, complete the standard cross-initiative coherence
review against an exact inventory baseline. Include every other current open
initiative, including Proposed and partial effort, and affected closed claims.
Record target states, effort evidence, findings, compatible dispositions, and
links. Append factual conflicts to initiatives/work-conflicts.md with both
claims and effort, impact, owner, blocking scope, and decision or evidence
required; also record invariant contradictions in the authoritative register.
Stop completion while a conflict affects the accepted design claim. Refining
an open consumer requires its declared destination in the accepted design
scope and the governing operation's authorized branch and edit boundary,
while preserving the consumer's own acceptance, reopening, lifecycle, and
human gates; this review alone grants no cross-initiative edit authority.
Never refine a closed consumer before recorded reopening under adopted bounded
intake delegation or separate human authority, receipt and legal transition.
Coherent same-outcome revision may retain identity; independent outcomes split.
This delivery alone supplies no target intake authority; record owned referrals.

Report every specification and evidence artifact changed, delivery steps,
verification results, lifecycle and status updates, compatibility or migration
effects, correlation verification, required implementation follow-up, and
remaining blocker. Do not
create an ad hoc delivery report or modify a product.
```
