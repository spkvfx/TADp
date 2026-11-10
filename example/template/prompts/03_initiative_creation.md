<!--
Replace every braced placeholder before using this prompt.
-->

# 3. Initiative creation

## Use when creating an initiative's first complete record

Use this prompt when an initiative already has its canonical proposal and needs
its initial complete initiative documentation. It follows the
[prepare-initiative prompt](00_initiative_preparation.md), which owns the
initiative preparation and its two README-file skeletons. The existing
initiative proposal is the primary input. This prompt completes the standard
initiative record; use the [initiative alignment prompt](04_initiative_alignment.md)
only after that record exists. Branch creation, selection, switching, and
validation are out of scope for this prompt.

## Structure and reference evidence

The shared [initiative template](../initiatives/README.md) defines the required initiative
structure, document roles, reading order, lifecycle, and maintenance rules. Use
its individual document templates as the source format:

- [`../../../README.md`](../initiatives/README.md)
- [`proposal/README.md`](../initiatives/proposal/README.md)
- [`assumption.md`](../initiatives/assumption.md)
- [`scope-assessment.md`](../initiatives/scope-assessment.md)
- [`architecture.md`](../initiatives/architecture.md)
- [`source-mapping.md`](../initiatives/source-mapping.md)
- [`open-questions.md`](../initiatives/open-questions.md)
- [`implementation-roadmap.md`](../initiatives/implementation-roadmap.md)
- [`implementation-steps.md`](../initiatives/implementation-steps.md)

Some existing initiatives predate the current template or contain
initiative-specific supporting records. Use them only to understand evidence
discipline and cross-links. The shared template's required filenames, document
roles, and creation boundary remain authoritative; do not copy an example's
legacy filename, additional record, or exception into a new initiative.

The adjacent
[implementation-readiness template](../initiatives/implementation-readiness.md)
is deliberately not an initial initiative artifact. Do not create, copy, or
link an implementation-readiness review when creating an initiative. Gather
readiness evidence later, immediately before execution, with the
[implementation-readiness review prompt](09_initiative_implementation_readiness_review.md).
That prompt only reports evidence; create any readiness document in a separate,
explicitly scoped documentation change.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative creation prompt](03_initiative_creation.md), create the
> initial complete documentation for the attached initiative from the shared
> initiative templates. Do not modify the proposal or create implementation
> artifacts.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative creation prompt** block
below. Do not execute, recurse into, or derive additional work from the example.

## Initiative creation prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Using the existing {initiative} proposal at
{initiative_path}/proposal/proposal.md, create the initial complete initiative
documentation for {initiative} at {initiative_path}. Its declared type must be
exactly `implementation`, `design`, or `planning`. Retain this prompt's stated
target and edit boundaries.

Treat the existing proposal as the primary input and preserve it in place. This
is documentation creation, not proposal alignment: do not rewrite the proposal
to resolve uncertainty or make it appear accepted. Record assumptions in the
assumption record, unresolved choices in the decision register, and source
conflicts in the source mapping. After this documentation exists, the initiative
alignment prompt may reconcile the initiative as a whole.

Human decisions are required to resolve uncertainty. Do not answer, select,
accept, close, or otherwise resolve an open question, even when repository
evidence favors an answer. Do not confirm, correct, or mark an assumption not
applicable. Only an explicit instruction from a human user may change an open
question into a decision or change an assumption's disposition. You may record
evidence, alternatives, and a clearly labeled recommendation awaiting that
human decision.

Apply the ownership and approval convention at {project_profile_path}. It
resolves human owner, reviewer, and approver roles as recorded for the target
project. Preserve every technical component, profile, placement,
external-party, contract, and evidence dependency.

Use {initiative_template_root}/initiatives/README.md as the authoritative structure for the
initiative. It defines the standard documents, their reading order, lifecycle,
and maintenance rules. Base each new document on its corresponding file in
{initiative_template_root}/initiatives. The shared template governs the new
structure; any existing initiative is an example only and must not be copied as
authority, scope, terminology, decision IDs, or content.

Treat the shared template's standard filenames and document roles as
authoritative even when an example initiative uses an older filename or a
focused supporting document. A source map, readiness review, implementation
report, consistency review, or other initiative-specific record in an example
does not replace, expand, or excuse any standard artifact listed below.

Before writing, verify that:
- 00_initiative_preparation.md prepared the initiative;
- {initiative_path}/README.md and {initiative_path}/proposal/README.md exist
  as an unmodified prepared README skeleton; if they predate preparation or
  contain initiative-specific content, stop rather than overwrite them;
- {initiative_path}/proposal/proposal.md exists and is the intended canonical
  working proposal;
- {initiative_template_root}/initiatives/README.md and each standard document template exist;
- the target contains no initial-initiative artifact beyond the prepared README
  skeleton and canonical proposal whose existing work could be overwritten;
- the target path, initiative type, decision prefix, governing sources, and
  any applicable parent initiative are unambiguous; and
- {initiative_registry_path}, {initiative_status_path}, and any applicable parent
  initiative index are available for the required tracking entries.

If any precondition fails, stop and report the blocker. The two prepared README
files are the only existing-document exception: complete them below. Do not
overwrite, merge, move, rename, or repair another existing initiative document.
Branching is out of scope: do not create, select, switch, validate, or otherwise
operate on branches. Do not create a replacement proposal, alter the existing
proposal, or modify the template.

Complete the prepared README files and create only these initial initiative
artifacts, replacing every template placeholder and removing instructional
comments:
1. {initiative_path}/README.md (complete the prepared file)
2. {initiative_path}/proposal/README.md (complete the prepared file)
3. {initiative_path}/assumption.md
4. {initiative_path}/scope-assessment.md
5. {initiative_path}/architecture.md
6. {initiative_path}/source-mapping.md
7. {initiative_path}/open-questions.md
8. {initiative_path}/implementation-roadmap.md
9. {initiative_path}/implementation-steps.md

Retain {initiative_path}/proposal/proposal.md as the existing canonical proposal.
Do not copy {initiative_template_root}/prompts into the initiative. Do not create
implementation-readiness.md: it is created later, immediately before
execution. Do not create delivery-record.md, optional supporting documents,
implementation reports, decision receipts, SDKs, APIs, code, schemas, tests,
migrations, or other product artifacts as
part of this prompt.
When a standard section does not apply, state why instead of deleting it.

Write one coherent initial initiative record that:
1. Uses the existing proposal for the intended outcome, scope, exclusions,
   dependencies, risks, assumptions, and acceptance outcomes without treating
   proposal claims as accepted architecture or implementation evidence.
2. Applies the documented initiative type. An `implementation` initiative plans
   product changes against accepted specifications without changing existing
   specifications. A `design` initiative plans specification changes against
   observed products without creating a new product. A `planning`
   initiative plans evidence outputs only for other initiatives.
3. Creates proposal/README.md as an evidence inventory with
   `evidence/authoritative` and `evidence/non-authoritative` labels,
   precedence, conflict handling, and frozen-source rules. Cite the existing
   proposal and every material source used.
4. Creates assumption.md with stable {decision_prefix}-Axx assumptions, each
   initially marked `Assumed aligned`, and the affected initiative records for a
   possible future correction. Do not mark an assumption `Confirmed`,
   `Corrected`, or `Not applicable` without an explicit human instruction. It
   must record intended boundaries, not duplicate the decision register.
5. Creates scope-assessment.md with one bounded outcome, accountable owner,
   authority boundary, acceptance claim, and an explicit result for every
   mandatory split trigger. If a trigger is present, stop acceptance of the
   broad claim and identify the narrow sibling or subinitiative work needed;
   do not create an umbrella initiative.
6. Creates architecture.md from verified repository evidence. State the current
   baseline, intended ownership, `evidence/authoritative` requirements,
   interfaces, lifecycle, failure, security, compatibility, and verification
   direction without claiming that a proposed design is already accepted or
   implemented.
7. Creates source-mapping.md with one traceable row per normative concept or
   contract, linking authoritative evidence to assumptions or decisions,
   specifications, product destinations, and verification. Treat missing or
   conflicting `evidence/authoritative` as blocking.
8. Creates open-questions.md with stable {decision_prefix}-xx IDs. Mark every
   initiative-specific question `Open` or `Open, blocking`; distinguish it from
   evidence and a proposed recommendation, but do not answer, accept, close,
   or silently select it. A decision accepted in another governing source may
   be cited as evidence, but it does not confirm this initiative's assumption
   or resolve its question without an explicit human instruction.
9. Creates an implementation roadmap and implementation steps in dependency
   order. Include Phase 0 specification and output-boundary acceptance, explicit
   prerequisites, release gates, compatibility, migration and rollback limits,
   and meaningful verification. These are planned work, not evidence that work
   is complete.
10. Keeps terminology, scope, ownership, evidence labels, decision IDs,
   dependencies, phases, acceptance gates, and verification references coherent
   across the complete initiative record.

Use all available evidence. Prioritize `evidence/authoritative`, accepted
repository decisions and specifications, released contracts, implemented
behavior and its verification, and completed initiatives. Use in-progress
initiative material only according to its documented evidence label and
precedence. Do not allow a proposal, initiative assumption, or
`evidence/non-authoritative` source to override established precedent.

Add the new initiative to {initiative_registry_path},
{initiative_status_path}, and the applicable parent initiative index when
one exists. The initiative index must identify the initiative and its entry
point. The status entry must
start at Proposed, summarize its first reviewable milestone, and link any known
blockers to the new initiative's records. Do not change unrelated initiative rows
or parent scope.

After creating the documentation, report the exact artifacts created, the
proposal and governing sources used, the template and example initiatives
consulted, the parent tracking records updated, and every assumption, open
decision, source conflict, or blocker that needs review. Do not create a
separate report.
```

