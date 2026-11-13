<!--
Replace every braced placeholder before using this prompt.
-->

# 8. Initiative SDK/API alignment

## Use when an implementation initiative aligns existing SDKs and APIs

Use this prompt only for an `implementation` initiative, after the
initiative-to-precedent alignment, assumption-confirmation,
open-question-resolution, and initiative-acceptance stages have completed.
It is the SDK/API-to-initiative alignment effort: it aligns applicable existing
SDKs and APIs with the initiative's confirmed scope through compatible,
evidence-backed extensions. It does not establish initiative scope, confirm an
assumption, or answer an open question.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":8,"records":["profile","initial-suite","membership","decision-receipt","acceptance"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative SDK/API alignment prompt](08_initiative_sdk_api_alignment.md),
> align the existing in-scope SDKs and APIs to the attached initiative after it
> is confirmed. Do not begin an extension while a material assumption or open
> question remains unresolved. Report any incompatibility instead of changing
> an established contract.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative SDK/API alignment prompt** block
below. Do not execute, recurse into, or derive additional work from the
example.

## Initiative SDK/API alignment prompt

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
Required inputs: accepted implementation suite, exact baseline and acceptance
receipt, resolved surface decisions and current in-scope SDK/API contracts,
implementation and compatibility tests. Use initiatives/README.md and its
constituent sources and initiatives/decision-receipts/decision-receipt.template.md from
the map. Recover only missing documentary prerequisites from actual earlier
events and authority. Missing acceptance, wrong type, unavailable contract or
unverified compatibility still blocks affected product work. Validate type,
phase, authority, links and actual SDK evidence before alignment.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
Align the applicable existing SDKs and APIs to the accepted {initiative} at
{initiative_path}.

This is the SDK/API-to-initiative alignment effort. It follows the
initiative-to-precedent alignment, human assumption-confirmation review, human
open-question-resolution review, and explicit acceptance. Treat the accepted initiative as the
target contract for this work, while established SDK/API precedent remains a
compatibility constraint. Do not use a current SDK or API limitation to reopen,
narrow, reinterpret, or silently change the confirmed initiative.

Verify that the target's declared type is `implementation`. A `design`
initiative changes specifications, not SDKs or APIs; a `planning` initiative
creates evidence only. If the type is not `implementation`, stop and route the
work to the appropriate initiative.

Verify that the initiative is `Accepted` or `In progress`, links an explicit
acceptance receipt, and identifies the accepted baseline revision. Resolved
assumptions and questions without the acceptance stage are not sufficient.

Verify that the active branch, exact version scope, realization suite,
initiative identity, execution branch, captured base branch and commit, and
reciprocal links match one unique canonical correlation row. Stop on drift;
SDK/API alignment must not allocate or repair membership identity.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
An existing SDK/API surface, its technical boundary, and the required
compatibility and verification evidence remain required.

Before editing, verify that:

- the target initiative has its complete canonical initiative suite: the
  initiative index, proposal source inventory and working proposal, assumption
  record, architecture, source mapping, open-question and decision register,
  implementation roadmap, and implementation steps;
- the initiative-to-precedent alignment is complete and every material
  assumption has an explicit human outcome in the assumption record;
- every active open question that affects the intended SDK/API surface,
  contract, compatibility, ownership, lifecycle, rollout, or verification has
  an explicit human outcome in the open-question register;
- the confirmed initiative identifies an existing SDK/API surface and owner
  that are in scope for each intended extension; and
- the existing SDK/API contract, implementation, compatibility commitments,
  tests, and governing evidence are readable enough to determine whether an
  additive extension is possible.

If an assumption or question material to an intended extension remains
unresolved, the target SDK/API surface is missing or ambiguous, or the
compatibility evidence is insufficient, stop before changing that affected
surface and report the blocker. Do not infer a human outcome, create a new
SDK/API, or replace an existing contract to make the initiative fit.

Apply the initiative's documented evidence labels and precedence. Prioritize
`evidence/authoritative`, accepted repository decisions and specifications,
released contracts, implemented behavior and its verification, and completed
initiatives. Use in-progress initiative material only according to its
documented evidence label and precedence. A confirmed initiative must not
invalidate established SDK/API precedent; an SDK/API limitation must not
invalidate or rewrite the initiative without the decision and review that its
records require.

Edit only existing documents in the target initiative, the applicable parent
status record when the initiative's status or next milestone changes, and
existing SDK/API surfaces demonstrably within the confirmed initiative's scope.
Do not edit {initiative_template_root}/initiatives or {initiative_template_root}/prompts.
After preceding owning-stage documentary preparation, substantive SDK/API
alignment must not create, copy, scaffold, move or rename an initiative
document or directory, standalone SDK, replacement API or competing interface. Add a
source file only when it is an additive part of an existing in-scope SDK or API
and the compatibility requirements below are met.

Work in this order:

1. Establish the confirmed SDK/API contract. Read the complete aligned
   initiative suite, the recorded human outcomes, governing repository sources,
   and each candidate SDK/API's public contract, implementation, tests, and
   supported versions. For every intended extension, identify the precise
   initiative claim, owning SDK/API surface, existing contract, source
   precedence, compatibility rule, required verification, and rollout or
   migration boundary.
2. Compare the confirmed initiative to existing SDK/API precedent. Determine
   whether each intended extension is additive and compatible, already present,
   out of scope, blocked by a conflict, or requires a decision outside the
   initiative. Do not treat a proposal claim, initiative convenience, or an
   undocumented existing behavior as authority to change a public contract.
3. Make only compatible, additive extensions. Preserve public symbols, routes,
   schemas, defaults, ownership, authority, lifecycle, wire behavior, and
   supported compatibility commitments. Prefer optional, versioned extension
   points with explicit mixed-version behavior, migration limits, and tests.
   Do not replace, remove, rename, narrow, reinterpret, or silently change an
   existing SDK/API contract.
4. Verify each extension against the confirmed initiative and existing
   precedent. Run the meaningful focused tests and required compatibility,
   migration, and mixed-version checks. Do not claim an extension is complete
   without evidence for its required behavior and compatibility commitments.
5. Reconcile only the evidence of the completed extension or conflict back into
   the affected initiative records. Record the exact existing surface, the
   compatibility rule, implementation and verification evidence, and any
   rollout or migration boundary. Do not change the confirmed initiative merely
   to conceal an SDK/API limitation.

If an SDK or API cannot be aligned through an additive,
precedent-preserving extension, leave that surface unchanged and report a
conflict. For every such conflict, identify the affected SDK/API and exact
contract, the confirmed initiative claim, the conflicting source or precedent
and its evidence label, why an additive extension is insufficient, the changes not
made, and the decision, owner, or evidence required to resolve it. Record the
conflict in the initiative's existing records when their format calls
for it; never conceal it with a compatibility shim that changes established
meaning.

For every conclusion, cite the supporting source. Distinguish completed
SDK/API extensions, already-compatible surfaces, blocked or out-of-scope
surfaces, open follow-up decisions, and unresolved conflicts. In the review
response, state the confirmed initiative scope used, list SDKs/APIs evaluated,
list extensions and their compatibility and verification evidence, list
initiative records changed to record the result, and identify every conflict or
blocker that prevented alignment. Include the correlation and active-branch
verification in the response.
```

