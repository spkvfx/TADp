<!--
Replace every braced placeholder before using this prompt.
-->

# 1. Proposal creation

## Use when starting a proposal-only initiative record

Use this prompt after [preparing the initiative](00_initiative_preparation.md)
to turn an existing realization note into the first working proposal for a new
initiative. It creates only the proposal inside the prepared README skeleton;
it does not create a branch or scaffold the initiative's full record.

**Proposal template:**
the shared [`proposal/proposal.md`](../initiatives/proposal/proposal.md) template

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [proposal creation prompt](01_proposal_creation.md), create the
> proposal for the attached initiative from its realization note after
> preparation. Create only the canonical proposal document.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Proposal creation prompt** block below. Do not
execute, recurse into, or derive additional work from the example.

## Proposal creation prompt

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
This new-initiative stage must not recreate complete existing target records.
For an existing-target intake revision, use its recorded alignment, decision
and renewed-acceptance route instead of scaffolding or overwriting records.

Using the correlated realization suite at {realization_suite_index_path} and
its intended note at {realization_note_path}, create a new
{initiative_type} initiative proposal for {initiative} at {initiative_path}. The type must be
exactly `implementation`, `design`, or `planning`. State its permitted output:
products only for implementation, specifications only for design, and evidence
only for planning.

Before writing, verify that:
- the initiative was prepared with 00_initiative_preparation.md and the active
  branch is exactly {initiative_branch};
- the canonical correlation row, realization-suite index, and prepared
  initiative metadata agree on version scope, source suite/note IDs and paths, initiative ID
  and path, execution branch, captured base branch, and captured base commit;
- {initiative_path}/README.md and {initiative_path}/proposal/README.md exist
  as the prepared README skeleton;
- {realization_note_path} exists, is readable, and is the intended realization
  note;
- {initiative_path}/proposal/proposal.md does not already exist or contain a
  proposal that could be overwritten; and
- {initiative_template_root}/initiatives/proposal/proposal.md exists and is the applicable
  proposal template.

If any precondition fails or the target path is ambiguous, stop and report the
blocker. Do not invent, move, overwrite, or repair any missing source,
template, initiative, or directory. Do not create or switch branches, alter
the prepared README files, or change a status or parent index.

Create only {initiative_path}/proposal/proposal.md in the prepared directory.
Base that file on
{initiative_template_root}/initiatives/proposal/proposal.md.
Do not copy the complete initiative template or create any other initiative
document, including an initiative README, proposal-source README, assumption,
architecture, source mapping, open-question register, roadmap, implementation
steps, status entry, or supporting report. Do not modify the realization note
or the template.

Do not infer a realization note's authority from its directory, filename, or
wording. Identify its exact path and any stated evidence label in the proposal's
references, and treat it as an input to a working proposal rather than an
accepted decision, architecture, or implementation claim.

Write a clear working proposal that:
1. Preserves the realization note's intended outcome and scope without adding
   capabilities or treating an assumption as an accepted decision.
2. Names the requested {initiative_type} initiative and explains why the
   realization is needed now.
3. Distinguishes included work, excluded work, assumptions, open decisions,
   risks, dependencies, and future acceptance outcomes.
4. Uses all available evidence. Prioritize `evidence/authoritative`,
   accepted repository decisions and specifications, implemented behavior and
   its verification, and completed initiatives. Use in-progress initiative
   material according to its documented evidence label and precedence.
5. Cites {realization_note_path} and every material repository source used,
   distinguishing the realization note from `evidence/authoritative` when both
   inform the proposal.
6. Records the same work version and realization-suite link without modifying
   or competing with the canonical project correlation row.
7. Labels the result as a working proposal only; it does not claim accepted
   architecture, implementation, qualification, or release readiness.

After creating the proposal, report its exact path, work version, realization
suite and note used, canonical-row verification, active initiative branch, and
any assumptions or open decisions that need review. Do not create a separate
report or any additional document.
```

