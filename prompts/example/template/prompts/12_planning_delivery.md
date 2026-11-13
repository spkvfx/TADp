<!--
Replace every braced placeholder before using this prompt.
-->

# 12. Planning delivery

## Use when an accepted planning initiative delivers initiative-local evidence

Use this prompt only for an accepted `planning` initiative. It delivers the
accepted research, audit, inventory, comparison, analysis, or recommendation
as initiative-local evidence. It does not change a product, specification,
authoritative source, or another initiative.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [planning delivery prompt](12_planning_delivery.md), produce the
> accepted evidence outputs for the attached initiative, preserve source
> classifications and limitations, and create its completion evidence.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Planning delivery prompt** block below. Do not
execute, recurse into, or derive additional work from the example.

## Planning delivery prompt

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
Deliver the accepted planning initiative {initiative} at {initiative_path} on
{initiative_branch}.

Verify that the declared type is exactly `planning`, the status is `Accepted`
or `In progress`, and the accepted baseline and acceptance receipt are current.
An `implementation` initiative must use the implementation path; a `design`
initiative must use the design delivery prompt.

This stage may create only the initiative-local evidence outputs explicitly
named by the accepted planning scope and may reconcile the owning initiative's
records and applicable status tracking. It must not modify a product, an
existing specification, authoritative evidence, another initiative, an SDK or
API, runtime configuration, deployment state, or an external system.

Before creating an evidence output, verify that:
- the active branch is exactly {initiative_branch};
- the exact version scope, realization suite, initiative ID and path,
  recorded execution branch, captured base branch and commit, and reciprocal links
  match one unique project correlation row;
- the worktree and branch diff contain no unexplained unrelated work;
- the complete initiative suite, scope assessment, acceptance receipt, accepted
  baseline, roadmap, steps, and source mapping are readable and coherent;
- no unresolved human decision, invariant conflict, dependency, source-access
  requirement, or delivery gate blocks the intended evidence work;
- every input source, evidence classification, method, output destination,
  owner, limitation, and verification method is unambiguous; and
- the shared `delivery-record.md` and `completion-evidence.md` templates are
  readable and would not overwrite existing initiative-local records.

If any precondition fails, stop the affected work and report every blocker. Do
not invent missing external evidence, silently change the method, promote a
recommendation to authority, or edit another record to make the evidence appear
complete.

Before producing evidence, create or update
{initiative_path}/delivery-record.md from the shared template. Record the
accepted baseline, branch, permitted initiative-local destinations, prohibited
external-change boundary, work version, suite, canonical-row link, captured
base, and a delivery ledger containing the accepted step,
source set, classification, method, output, limitations, and verification.

When evidence work actually begins, append the legal transition to
`In progress` and reconcile the initiative and applicable status records.

Work in dependency order. For each accepted planning step:
1. Read the governing question, accepted method, source inventory, evidence
   classes, access limits, intended audience, and verification.
2. Gather only available authorized evidence and preserve precise source
   identity, date or revision, scope, method, and limitations.
3. Produce the ledgered initiative-local output without editing a source or
   consumer record.
4. Separate observations, inferences, recommendations, missing evidence, and
   human decisions visibly.
5. Record the output and source coverage in `delivery-record.md`.
6. Verify the accepted method, coverage, calculations, internal consistency,
   links, reproducibility, and stated limitations as applicable, recording the
   actual result.
7. Stop and report evidence that requires an invariant revision, new human
   decision, broader scope, product change, or specification change.

After all accepted planning steps, reconcile the evidence outputs, source
mapping, roadmap, steps, initiative index, and delivery record. Planning output
remains non-authoritative unless a named owning authority accepts it through a
separate governed decision. Do not edit another initiative to consume the
result; report that follow-up to its owner.

When every in-scope planning gate passes, create or update
{initiative_path}/completion-evidence.md. State the exact delivered evidence
claim, inputs and classifications, output destinations, method verification,
limitations, recommendations, missing evidence, and residual work. Reconcile it
with `delivery-record.md` and append the legal `Completed` transition only when
all records agree.

Before that transition, complete the standard cross-initiative coherence
review against an exact inventory baseline. Include every other current open
initiative, including Proposed and partial effort, and affected closed claims.
Record target states, effort evidence, findings, compatible dispositions, and
links. Append factual conflicts to initiatives/work-conflicts.md and link
the owning planning and completion evidence; this coordination record is the
only additional project-level edit authorized by this review. Preserve both
claims and effort, impact, owner, blocking scope, and required decision or
evidence. Invariant contradictions also require the authoritative register.
Stop completion when a conflict affects the accepted evidence claim. Hand
findings to target owners through their workflow and branch; do not refine
another initiative from this planning stage. A closed target needs recorded reopening under adopted bounded intake delegation
or separate human authority, a receipt and legal transition before refinement.
Coherent same-outcome revision may retain identity; independent outcomes split.
Planning delivery alone supplies no target intake authority.

Report every evidence artifact created or changed, delivery steps, source
coverage, verification results, lifecycle and status updates, limitations,
correlation verification, recommended follow-up, and remaining blocker. Do not create an ad hoc report
outside the accepted output set or modify another record to act on the result.
```
