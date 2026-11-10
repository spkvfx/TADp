<!--
Replace every braced placeholder before using this prompt.
-->

# 7. Initiative SDK/API alignment

## Use when an implementation initiative aligns existing SDKs and APIs

Use this prompt only for an `implementation` initiative, after the
initiative-to-precedent alignment,
assumption-confirmation, and open-question-resolution reviews have completed.
It is the SDK/API-to-initiative alignment effort: it aligns applicable existing
SDKs and APIs with the initiative's confirmed scope through compatible,
evidence-backed extensions. It does not establish initiative scope, confirm an
assumption, or answer an open question.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative SDK/API alignment prompt](07_initiative_sdk_api_alignment.md),
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
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Align the applicable existing SDKs and APIs to the confirmed {initiative} at
{initiative_path}.

This is the SDK/API-to-initiative alignment effort. It follows the
initiative-to-precedent alignment, human assumption-confirmation review, and
human open-question-resolution review. Treat the confirmed initiative as the
target contract for this work, while established SDK/API precedent remains a
compatibility constraint. Do not use a current SDK or API limitation to reopen,
narrow, reinterpret, or silently change the confirmed initiative.

Verify that the target's declared type is `implementation`. A `design`
initiative changes specifications, not SDKs or APIs; a `planning` initiative
creates evidence only. If the type is not `implementation`, stop and route the
work to the appropriate initiative.

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
Do not create, copy, scaffold, move, or rename an initiative document, initiative
directory, standalone SDK, replacement API, or competing interface. Add a
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
blocker that prevented alignment.
```

