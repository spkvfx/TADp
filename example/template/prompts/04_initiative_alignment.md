<!--
Replace {initiative} with the initiative name or path before using this prompt.
-->

# 4. Initiative-to-precedent alignment

## Use when aligning a fully documented initiative to evidence and precedent

Use this prompt after an initiative's initial documentation exists. The
initiative is the target, not any one document: treat its proposal and every
other initiative record as a coupled account of the same initiative. Establish
which claims and assumptions the available authority supports before confirming
them in the initiative record. This is the evidence-and-precedent
alignment effort; it does not align or extend an SDK or API.

After this prompt, use the [initiative assumption confirmation review](05_initiative_assumption_review.md)
and [initiative open-question resolution review](06_initiative_open_question_review.md)
to obtain the required human outcomes. Then use the
[initiative acceptance prompt](07_initiative_acceptance.md). Only an accepted
implementation initiative may use the separate
[initiative SDK/API alignment prompt](08_initiative_sdk_api_alignment.md).
Do not use an SDK or API limitation to confirm an unvalidated initiative
assumption.

The shared initiative template defines the required record roles and filenames.
An older initiative can contain historical aliases or focused supporting
documents, but those records are evidence only unless the initiative index
explicitly identifies them as a continuation of a canonical record. Do not use
a similarly named legacy file to silently satisfy a missing standard artifact.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative alignment prompt](04_initiative_alignment.md), align the
> attached initiative as a whole to governing evidence and established
> precedent, including its proposal and all initiative records. Do not confirm an
> initiative assumption until its required review has an explicit human outcome,
> and do not modify an SDK or API in this alignment step.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative alignment prompt** block below.
Do not execute, recurse into, or derive additional work from the example.

## Initiative alignment prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Review and align the existing {initiative} as a whole in place. This is the
post-documentation initiative-to-precedent alignment step: validate evidence
before confirming any initiative assumption. It precedes the
human assumption-confirmation and open-question reviews and the separate
SDK/API alignment prompt. Do not modify an SDK or API in this prompt, or use an
SDK or API limitation to change, confirm, or narrow the initiative. The
proposal-alignment prompt has a different, proposal-only target; do not apply
it document by document or treat any initiative document as an independent
assumption target.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Preserve every technical component, profile, placement, external-party,
contract, and evidence dependency.

Before editing, verify that the target initiative contains its initial canonical
initiative suite: the initiative index, proposal source inventory and working
proposal, assumption record, scope assessment, architecture, source mapping, open-question and
decision register, implementation roadmap, and implementation steps. Also
identify every existing supporting initiative document linked from the initiative
index. If a required document is missing, the target is ambiguous, or the
initiative has not been initialized, stop and report the blocker. Do not
scaffold, copy, or repair a missing initiative document or directory.

Read linked supporting records for evidence that bears on the aligned account,
but keep their role separate from the canonical suite. A readiness review,
implementation report, consistency review, execution specification, or other
initiative-specific document cannot replace a missing standard record merely
because it covers a similar topic. Report any template deviation; do not rename,
migrate, or normalize it in this alignment workflow.

Before editing, read the target's declared initiative type and classify each
proposed output. An `implementation` initiative must not modify an existing
specification; report a needed specification change for a `design` initiative.
A `design` initiative may create or modify specifications and evidence, but
must not create a new product. A `planning` initiative may modify evidence
only. Do not use alignment to bypass those boundaries.

Review `scope-assessment.md` before changing any other record. Re-run every
mandatory split trigger against current evidence. If the initiative combines
an independently acceptable outcome, different owner, materially different
authority boundary or initiative type, separable verification or release,
unrelated product destination, or independent lifecycle, stop and report the
required decomposition. This alignment prompt does not create sibling or
subinitiative records and must not make an umbrella initiative appear coherent.

Edit only existing allowed documents in the target initiative and the applicable
parent status record when the initiative's status or next milestone changes. Do
not edit {initiative_template_root}/initiatives,
{initiative_template_root}/prompts, product source, SDK/API surfaces, or another
initiative. Do not create, copy, scaffold, move, or rename an initiative
document or initiative directory.

Keep the initiative's intended outcome, included work, and excluded work. Do
not broaden boundaries, add capabilities, or resolve uncertainty by silently
rewriting the plan. Treat frozen proposal artifacts as historical evidence:
leave them unchanged and record their correction or supersession through the
existing assumption and decision records. A current canonical working proposal
may be corrected in place when higher-precedence evidence requires it.

Apply the initiative's documented evidence labels and precedence. Prioritize
`evidence/authoritative`, accepted repository decisions and specifications,
released contracts, implemented behavior and its verification, and completed
initiatives. Use in-progress initiative material only according to its
documented evidence label and precedence. A proposal, initiative assumption, or
`evidence/non-authoritative` source must never invalidate an established
precedent.

Work in this order:

### Align the initiative to evidence and existing precedent

1. Establish the initiative-level evidence base. Read the complete set of
   canonical and linked supporting initiative records together with the
   proposal-source inventory, governing repository sources, specifications,
   implementations, tests, completed initiatives, and relevant existing SDKs
   and APIs. Identify the evidence label, authority, and precise source for each
   material claim and how it affects the initiative's outcome, boundaries,
   ownership, delivery, or verification.
2. Evaluate evidence before confirming assumptions. For every material proposal
   claim or initiative assumption, determine whether governing evidence or
   established precedent supports it, corrects it, leaves it open, or conflicts
   with it. Do not confirm an assumption merely because it appears in multiple
   initiative records, is convenient for an existing SDK or API, or would
   simplify
   implementation.
3. Reconcile the initiative to the evidence and precedent. Reconcile the
   proposal, assumption record, scope assessment, architecture, source mapping, decision register,
   roadmap, implementation steps, initiative index, and applicable supporting
   records as one account of the initiative. Align its terminology, scope,
   ownership, `evidence/authoritative` requirements, compatibility,
   dependencies, sequencing, acceptance
   gates, and verification. Update each affected existing record only to
   express the evidence-backed initiative-level result, including the working
   proposal. Do not modify an SDK or API.
4. Preserve uncertainty and conflicts explicitly. Record missing or conflicting
   `evidence/authoritative` in the source mapping and affected assumption or architecture
   records as appropriate. Preserve unsupported assumptions and unresolved
   choices in their existing source records; do not mark an assumption
   confirmed or an open question answered in this prompt. Do not represent a
   proposal claim as accepted architecture or implementation evidence until the
   relevant record confirms it.
5. Validate the evidence-backed initiative-level account. The proposal,
   assumption, scope assessment, architecture, source mapping, decisions, roadmap, implementation
   steps, and linked supporting records must collectively describe the same
   initiative and its delivery path. Each proposed output or compatibility
   claim must trace to governing evidence and a verification gate. Correct
   contradictions that the evidence resolves; retain and report conflicts that
   it does not.
6. Hand off unresolved human decisions. Use the initiative assumption
   confirmation review for every unconfirmed assumption and the
   initiative open-question resolution review for every active open question.
   Do not begin acceptance until the applicable human reviews have recorded
   their required outcomes. Acceptance remains a separate explicit human gate;
   it owns the transition to `Accepted`. Only after acceptance may the SDK/API
   alignment prompt own applicable implementation changes.

For every conclusion, cite the supporting source. Distinguish evidence-backed
and corrected initiative claims, unconfirmed assumptions, active open
questions, and unresolved conflicts. In the review response, state the
initiative-to-precedent alignment outcome, list the initiative records changed to
express it, identify every assumption or question requiring its human review,
and report every conflict or blocker that prevents alignment.
```

