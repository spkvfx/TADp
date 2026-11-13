<!--
Replace {initiative} with the initiative name or path before using this prompt.
-->

# 2. Proposal alignment

## Use when revising an existing proposal in place

Use this prompt with an identified target initiative and canonical proposal.
After preceding documentary preparation, its alignment activity updates only
that proposal.

When the target has an initiative index or proposal source inventory, use it to
identify the canonical editable proposal, editability, and evidence label
before editing. A realization note, frozen source, precedence review, readiness record, report, or
initiative-specific supporting file may supply evidence, but it is not a
substitute for the target's canonical proposal.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":2,"records":["profile","preparation-skeleton","preparation-proposal-source","realization-suite","membership","proposal"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [proposal alignment prompt](02_proposal_alignment.md), align the
> attached initiative's proposal in place after preparing constructible
> documentary prerequisites through their owning stages.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Alignment prompt** block below. Do not execute,
recurse into, or derive additional work from the example.

## Alignment prompt

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

Before the substantive step, apply documentary prerequisite preparation in
{initiative_template_root}/prompts/WORKFLOW-CONTRACT.md using
{initiative_template_root}/TEMPLATE-COVERAGE.md and this stage's inventory.
Classify and prepare only necessary constructible inputs from sufficient
scoped evidence through their owning stages; then validate and recheck this
step's real entry gates. Disclose preparation changes separately. The edit
limits below govern the substantive activity after this preparation.
Reusable source paths below are relative to {initiative_template_root};
instantiate only at the map's declared project-relative destination.
Required inputs: one canonical editable proposal, source inventory, actual
realization and governing evidence, target identity and recorded assignment.
Use initiatives/proposal/README.md and initiatives/proposal/proposal.md and
Stage 0 preparation-README sources from the map. A missing proposal may be prepared
through Stage 1's documentary activity only after its real entry gates hold;
reuse valid proposals and preserve frozen sources. Missing identity, ambiguous
editability or insufficient evidence blocks the substantive alignment. Validate
source standing, links and the single canonical owner before editing.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
Review the existing {initiative} proposal in place. Preserve its declared
initiative type: `implementation` aligns products to specifications, `design`
aligns specifications to products, and `planning` produces evidence only.

Before editing, verify that the active branch, canonical project correlation
row, realization-suite index, initiative metadata, and captured base identity
all describe the same prepared membership and active assignment. Stop on any missing, partial, duplicate,
or inconsistent relationship. Proposal alignment must not allocate, infer,
renumber, or repair membership identity.

After preceding preparation, edit only the target initiative's canonical
working proposal during alignment. This substantive activity must not create,
copy, scaffold, move or rename another file or directory, including an
assumption record, initiative directory or template-derived document.
Do not edit `{initiative_template_root}/initiatives` or
`{initiative_template_root}/prompts`; use them only as guidance. Put every
proposal correction in the target proposal itself, and report unresolved
conflicts in the review response rather than creating a new document.

Keep the proposal's current scope, intended outcome, and excluded work. Do not
add capabilities, broaden boundaries, or resolve uncertainty by silently
changing the proposal. Treat frozen proposal artifacts as historical evidence:
if the only target proposal is frozen, leave it unchanged, create no
replacement, and report that the review is blocked by its frozen state.

If the initiative index or source inventory does not identify one canonical
editable proposal, or identifies a legacy document whose role is ambiguous,
stop and report that discrepancy. Do not infer equivalence from a similar
filename. Missing documentary records may be prepared only through the shared
owning-stage procedure; unresolved identity or role ambiguity still blocks
this proposal-only alignment activity.

Work in this order:

1. Clarify and elaborate the proposal using all available evidence. Prioritize
   `evidence/authoritative`, accepted repository decisions and specifications,
   implemented behavior and its verification, and completed initiatives. Use
   in-progress initiative material according to its documented evidence label
   and precedence.
2. Check the proposal for internal contradictions, incompatible claims, and
   ambiguous statements. Revise correctable claims into one coherent proposal,
   and report each material correction with its evidence and rationale.
3. Recheck the proposal against other in-progress initiatives. Align shared
   boundaries, terminology, dependencies, and sequencing with established
   precedent. Edit only the target proposal; when the conflict also requires a
   change in another initiative, identify that needed coordinated correction
   and the source that governs it without editing or creating other records.
4. Recheck the proposal against `evidence/authoritative` and implemented work.
   Align it with higher-authority requirements and actual verified behavior.
   Report each unresolved conflict explicitly, including the conflicting
   sources, their precedence, the affected scope, and the decision or evidence
   needed to resolve it.

For every conclusion, cite the supporting source. Distinguish corrected claims,
open decisions, and unresolved conflicts; do not represent a proposal claim as
accepted architecture or implementation evidence until the relevant record
confirms it.

Report the verified work version, suite, initiative, branch, and canonical row
with the proposal-alignment result.
```

