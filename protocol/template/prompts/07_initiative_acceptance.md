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

## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":7,"records":["profile","initial-suite","membership","decision-receipt","acceptance","work-conflict"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

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
Required inputs: complete aligned suite, scope assessment, resolved blocking
decisions/receipts, exact proposed baseline, acceptance authority and coherence
inventory. Use initiatives/README.md and its constituent sources plus
initiatives/decision-receipts/decision-receipt.template.md and
project/initiatives/work-conflicts.template.md. Retain the pre-acceptance
open-work inventory in existing owning records or the acceptance packet;
create no completion-evidence file. Recover earlier documentary inputs through owning
activities, capturing sufficient actual decisions without repeating them.
Missing acceptance authority or unresolved blocking decisions remain blockers;
preparation cannot turn alignment or implementation into acceptance. Validate
baseline, receipts, source standing and current gates before presentation.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
Conduct the acceptance review for {initiative} at {initiative_path} on
{initiative_branch}. This is the human-authority gate from `Proposed` to
`Accepted`; it is not delivery, execution, finalization, or autonomous approval.

If separately sufficient authority excepts a named prerequisite or requests
bounded work without the ordinary acceptance decision, record the exact
exception and actual outcome. A waived human gate is not an Accept response:
do not run the Accept reconciliation below or manufacture the `Accepted`
transition. Report the bounded prompt result and the remaining acceptance
obligation. Existing exact acceptance authority may be documented without
requesting the same human decision again.

Apply the ownership and approval convention at {project_profile_path}. Identify
the exact human authority permitted to accept this initiative. Do not infer
acceptance from prior assumption confirmations, question answers,
recommendations, implementation activity, or an instruction about another
initiative.

Before presenting the acceptance question, verify that:
- the active branch is exactly {initiative_branch}, prepared for this
  initiative from its captured base branch;
- the exact version scope, realization suite, initiative ID and path,
  recorded execution branch, captured base branch and commit, and reciprocal links
  match one unique canonical project correlation row;
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
- current open effort, including Proposed and partial work, and affected
  closed claims have been reviewed against an identified inventory baseline;
  work conflicts are preserved in initiatives/work-conflicts.md and affected
  records, with no unresolved incompatibility blocking this acceptance;
- the initiative type and permitted output boundary are unambiguous;
- dependencies, owners, compatibility, migration, recovery, security,
  verification, release gates, and residual limitations are explicit; and
- the exact proposed accepted-baseline revision can be identified by commit,
  content revision, or another stable repository locator.

After owning-stage documentary preparation, stop and report every remaining
precondition failure. Acceptance itself cannot repair earlier authority,
resolve a separate decision, weaken a gate, narrow the claim, infer membership
identity or begin delivery. Change status only after actual sufficient
acceptance authority is captured and all real gates hold.

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

For Accept, perform these reconciliation steps serially:
1. retain the accepted baseline without changing its meaning;
2. set the initiative status to `Accepted`;
3. append the legal `Proposed` to `Accepted` lifecycle entry with the receipt and
  baseline revision;
4. link the acceptance receipt from the initiative README;
5. reconcile {initiative_status_path}, {initiative_registry_path}, and every
  applicable parent or dependent tracking record; and
6. preserve all allocated correlation fields while updating only copied
  lifecycle status and its receipt evidence; and
7. identify the next type-specific stage without starting it.

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
