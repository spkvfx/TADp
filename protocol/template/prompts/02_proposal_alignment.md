<!--
Replace {initiative} with the initiative name or path before using this prompt.
-->

# 2. Proposal alignment

## Use when revising an existing proposal in place

Use this prompt with an existing target initiative and proposal. It updates only
that proposal; it does not create initiative artifacts.

When the target has an initiative index or proposal source inventory, use it to
identify the canonical editable proposal, editability, and evidence label
before editing. A realization note, frozen source, precedence review, readiness record, report, or
initiative-specific supporting file may supply evidence, but it is not a
substitute for the target's canonical proposal.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [proposal alignment prompt](02_proposal_alignment.md), align the
> attached initiative's proposal in place. Do not create, copy, or change any
> other document or directory.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Alignment prompt** block below. Do not execute,
recurse into, or derive additional work from the example.

## Alignment prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Review the existing {initiative} proposal in place. Preserve its declared
initiative type: `implementation` aligns products to specifications, `design`
aligns specifications to products, and `planning` produces evidence only.

Edit only the target initiative's existing canonical working proposal. Do not
create, copy, scaffold, move, or rename any file or directory, including a
proposal, assumption record, initiative directory, or template-derived document.
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
filename or repair the initiative structure in this proposal-only workflow.

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
```

