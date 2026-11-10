<!--
Replace every braced placeholder before using this prompt.
-->

# 7. Initiative acceptance

## Use when a human authority must accept the completed proposed specification

Use this prompt only after initiative alignment and every applicable assumption
and open-question review are complete. Acceptance is a distinct human decision:
alignment, resolved source items, or a general instruction to continue does not
make an initiative `Accepted`.

This prompt changes no product, SDK, API, authoritative evidence, or delivery
output. It records the accepted initiative baseline and lifecycle transition.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative acceptance prompt](07_initiative_acceptance.md), present
> the attached initiative's exact bounded claim and delivery gates for human
> acceptance, then record the response without beginning delivery.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative acceptance prompt** block below. Do
not execute, recurse into, or derive additional work from the example.

## Initiative acceptance prompt

~~~text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Conduct the acceptance review for {initiative} at {initiative_path} on
{initiative_branch}. This is the human-authority gate from `Proposed` to
`Accepted`; it is not delivery, execution, finalization, or autonomous approval.

Apply the ownership and approval convention at {project_profile_path}. Identify
the exact human authority permitted to accept this initiative. Do not infer
acceptance from prior assumption confirmations, question answers,
recommendations, implementation activity, or an instruction about another
initiative.

Before presenting the acceptance question, verify that:
- the active branch is exactly {initiative_branch}, prepared for this
  initiative from its captured base branch;
- the worktree contains no unexplained or unrelated change that would make the
  proposed baseline ambiguous;
- the initiative is `Proposed` and its lifecycle history is current;
- the complete canonical initiative suite exists and uses the current template;
- `scope-assessment.md` records one bounded outcome and no undisposed mandatory
  split trigger;
- the proposal, assumptions, scope assessment, architecture, source mapping,
  open questions, roadmap, steps, README, registry, status, and linked
  supporting records describe one coherent initiative;
- every blocking assumption has an explicit human disposition and linked
  decision receipt;
- every active blocking question has an explicit accepted answer or an
  authorized deferral whose re-entry condition does not block acceptance;
- every normative claim is compatible with applicable authoritative evidence;
- the initiative type and permitted output boundary are unambiguous;
- dependencies, owners, compatibility, migration, recovery, security,
  verification, release gates, and residual limitations are explicit; and
- the exact proposed accepted-baseline revision can be identified by commit,
  content revision, or another stable repository locator.

If a precondition fails, stop and report every blocker. Do not repair missing
earlier-stage records, resolve a decision, weaken a gate, narrow the claim,
change status, or begin delivery in this prompt.

Prepare one acceptance packet from the existing records with:
1. initiative identity and declared type;
2. exact bounded outcome and beneficiary;
3. included scope and explicit exclusions;
4. authoritative evidence and accepted decisions governing the claim;
5. permitted output destinations and prohibited output boundary;
6. dependencies and affected owners;
7. compatibility, migration, recovery, security, and operational effects;
8. delivery order, entry gates, verification, and completion conditions;
9. every remaining non-blocking limitation, deferred item, and re-entry
   condition; and
10. the proposed accepted-baseline revision.

Present that packet without silently simplifying or expanding it. Then ask the
identified human authority exactly one acceptance question:

Acceptance requested:
Do you accept this exact initiative baseline for its declared type, scope,
outputs, gates, limitations, and verification obligations? Reply with one of:
Accept; Reject: {reason}; or Revise: {required_change}.

Wait for an explicit response. If the human asks for context, provide it and
ask the acceptance question again after the context is complete. Do not treat
silence, likely intent, an earlier broad approval, or permission to implement as
acceptance.

After the explicit response, create a decision receipt from
{initiative_template_root}/initiatives/decision-receipts/decision-receipt.template.md.
Preserve the complete acceptance packet or its stable link, the exact question,
exact response, human authority, date or event, accepted revision, scope, and
affected records.

For Accept:
- retain the accepted baseline without changing its meaning;
- set the initiative status to `Accepted`;
- append the legal `Proposed` to `Accepted` lifecycle entry with the receipt and
  baseline revision;
- link the acceptance receipt from the initiative README;
- reconcile {initiative_status_path}, {initiative_registry_path}, and every
  applicable parent or dependent tracking record; and
- identify the next type-specific stage without starting it.

For Reject, leave the initiative `Proposed`, record the rejection receipt and
reason, and identify the owning earlier stage or evidence needed before another
acceptance review.

For Revise, leave the initiative `Proposed`, record the requested revision and
receipt, and route the initiative back to alignment, scope decomposition,
assumption review, or question resolution as appropriate. Do not perform that
revision in this prompt.

Inspect the diff and stage only the decision receipt and acceptance-owned
tracking reconciliation. If there is a change, commit it with a clear
initiative-specific acceptance, rejection, or revision-request message. Do not
push, merge, begin delivery, or include unrelated changes.

Report the exact response, receipt, baseline revision, lifecycle result,
records changed, commit identifier when created, next owning stage, and every
remaining limitation or blocker.
~~~
