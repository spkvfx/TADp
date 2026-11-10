<!--
Replace every braced placeholder before using this prompt.
-->

# 5. Initiative assumption confirmation review

## Use when a human must confirm an initiative's assumptions

Use this prompt to review every current, unresolved assumption in one existing
initiative. It is an interactive human-decision workflow. Repository evidence
can explain a record's effects, but it cannot confirm an assumption for the
human.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative assumption confirmation review prompt](05_initiative_assumption_review.md),
> review every unresolved assumption in the attached initiative with me one at
> a time.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative assumption confirmation prompt**
block below. Do not execute, recurse into, or derive additional work from the
example.

## Initiative assumption confirmation prompt

~~~text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Facilitate a human confirmation review of every current, unresolved assumption for {initiative} at {initiative_path}. This is an interactive
review, not an autonomous assumption task. A human user must explicitly confirm,
correct, reject as not applicable, or turn each source assumption into an open
question before that source record may change.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Preserve every technical component, profile, placement, external-party,
contract, and evidence dependency.

Read `{initiative_path}/README.md` to identify the initiative type and its
allowed output. The type does not change the human-review requirement:
assumptions can be confirmed, corrected, rejected as not applicable, or turned
into an open question only through an explicit human response.

Before asking the first question, verify that the target has a readable
initiative index, assumption record, open-question register, and every
initiative record identified as affected by an assumption change. Read
`assumption.md` and any continuation explicitly identified by the initiative
index. Build a complete coverage inventory of every stable assumption ID, exact
source location, current disposition, dependencies, and documents named by its
`If corrected, revisit` fields.

Use a source assumption record's explicit dependencies first, then stable-ID
order to select the next ready source assumption. Do not silently omit a source
record. A supporting record may explain order or evidence, but it does not add,
replace, or resolve a source assumption.

Do not ask an already Confirmed or Not applicable source assumption again
unless the human asks to reopen it or a changed linked record explicitly marks
it for re-review. Keep it in the coverage inventory and report it as already
resolved. Treat Assumed aligned, pending, and otherwise unresolved assumptions
as needing human review.

When one source ID appears in a canonical assumption table and a related
ratification, summary, or detail section, count it once. Copy the original
assumption from the authoritative source row or detail, then reconcile every
canonical representation of that same ID after the human responds. Do not use a
summary or supporting record to replace the original assumption text.

Use `evidence/authoritative`, accepted repository decisions and
specifications, released contracts, implemented behavior and its verification,
completed initiatives, and documented evidence labels to prepare the
explanation. A proposal, an initiative assumption, or
`evidence/non-authoritative` must never override established precedent.
Evidence may describe a constraint or consequence; it cannot be treated as a
human answer.

Ask exactly one ready source assumption at a time. For each one, use this
structure:

Assumption ID: {stable_source_id}
Original assumption:
{the complete original source assumption copied exactly, with no paraphrase,
translation, correction, omission, or added wording}

Plain-language explanation:
{a short, plain-text explanation of what the original assumption means and why
it matters to this initiative}

Relevant evidence and effect:
{the governing sources, precedence, dependencies, and initiative records that
would need reconciliation if the human changes the assumption}

Human confirmation requested:
Does the original assumption accurately state the intended initiative boundary?
Reply with one of: Confirm; Correct: {replacement}; Not applicable: {reason};
or Open question: {question that must be decided}.

Write the Plain-language explanation for approximately an eighth-grade reading
level. Use short, direct sentences and define necessary technical terms. Do not
use allegories about schoolchildren, including schools, teachers, classrooms,
or groups of friends. Another allegory may be used only when it makes the
meaning easier to understand. Do not hide the original assumption inside the
explanation; always show it separately and exactly as recorded.

Do not infer a human response from source evidence, a recommendation, an
earlier review, a previous chat message about a different source ID, silence,
or likely intent. Do not mark an assumption Confirmed, Corrected, or Not
applicable; update a document; stage a file; create a commit; or continue to a
dependent assumption until the human gives an explicit response for the exact
stable source ID. If the human asks for more context, provide it and wait for a
clear response.

After an explicit human response, create one decision receipt from
`{initiative_template_root}/initiatives/decision-receipts/decision-receipt.template.md`
before changing the source disposition. If this is the initiative's first
receipt, create `{initiative_path}/decision-receipts/README.md` from the shared
template. Preserve the exact prompt, exact response, human authority, evidence
presented, scope, date or event, resulting disposition, affected records, and
unresolved consequences. Give the receipt a stable ID and link it from the
source assumption row. If the response is ambiguous or conflicts with
authoritative evidence, do not create a governing disposition; request
clarification or use the invariant-conflict procedure.

Then update the source assumption record:

1. For Confirm, retain the original assumption verbatim, mark that exact row
   Confirmed, and record the confirmation note and date where the record's
   format supports them.
2. For Correct, retain the original assumption verbatim, mark the row
   Corrected, and record the human's intended replacement in the correction
   field. Do not rewrite the original source text to make it appear confirmed.
3. For Not applicable, retain the original assumption verbatim, record the
   explicit reason, and remove only the initiative's reliance on that
   assumption.
4. For Open question, preserve the source assumption and its unresolved state.
   Add or update a stable entry in the existing open-questions.md register,
   link the two records, and state that the assumption cannot be confirmed
   until that question receives an explicit human decision. Use an existing
   pending disposition when the assumption record defines one; otherwise retain
   its unresolved disposition and put the question ID in the note. Use the
   initiative open-question resolution review to obtain that decision, then
   resume this assumption and obtain its own explicit human outcome.

Then reconcile only the existing initiative records actually affected by that
human response: the initiative index, current working proposal when it is not
frozen, architecture, source mapping, open-question register, roadmap,
implementation steps, and linked supporting records. A human correction may
add a new stable assumption row or a new stable open question when it exposes a
real, in-scope boundary or uncertainty. Preserve the original records and make
the new entry traceable to the source ID and human response.

Maintain the initiative's intended outcome, included work, excluded work, and
ownership boundaries. Do not broaden the initiative, introduce a new
capability, change another initiative, modify a shared contract, or resolve
uncertainty by silently rewriting initiative scope. Preserve frozen proposal
artifacts as historical evidence. If a response reveals an out-of-scope or
cross-initiative conflict, record the in-scope question or assumption effect
and report the needed owner or decision without changing the external target.

After each explicit response and its reconciliation, inspect the diff. Stage
the decision receipt and only files changed for that one source assumption;
never include pre-existing or unrelated work. If there is a change to commit,
commit it before asking the next source assumption, using exactly this format:

{Code} {Initiative Name} - {comma-delimited scope}

Use the source assumption's stable ID as {Code}, the initiative index's name as
{Initiative Name}, and concise comma-delimited descriptions of the records or
boundaries changed as the scope. Follow the repository's prior initiative
commits for capitalization and terminology. Do not amend, squash, rebase,
force-push, or commit an unrelated change.

Continue until every source assumption has an explicit human outcome or is
already resolved with a valid recorded disposition. An assumption linked to a
new open question remains unresolved; do not claim the review is complete
until that question has an explicit human decision and the assumption then has
its own explicit human outcome.

Only after every assumption is explicitly confirmed, corrected, or marked not
applicable, and every resulting initiative change is reconciled, update the
applicable status documents. Update the initiative index's Last updated field
and every applicable parent status record, such as {initiative_status_path}, to
record the completed review and its current result. Change the initiative's
next milestone only when the human outcomes support that change. Leave the
initiative lifecycle `Proposed`; this review does not accept the initiative.
An unresolved or blocking question prevents handoff to the separate initiative
acceptance stage. Make the final tracking updates before committing the final
resolved source assumption, and include them in that source assumption's commit
scope.

Verify that the review coverage inventory is complete, every changed record
has a linked decision receipt and traceable human response, and no unrelated files are staged. Push the
new review commits for the current branch only after the final status changes
are committed. Use a normal push; do not force-push, guess an upstream, or
push pre-existing unrelated commits. If the branch has no configured upstream
or the push fails, report the exact blocker.

At the end, report the source assumptions reviewed in precedence order, each
explicit human response, documents changed, commit hashes and messages, status
updates, push result, every deferred or newly opened question, and every
remaining blocker. When all applicable human reviews are complete, identify the
initiative acceptance prompt as the next stage.
Do not create a separate report file.
~~~

