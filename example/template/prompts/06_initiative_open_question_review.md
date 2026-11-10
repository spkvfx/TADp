<!--
Replace every braced placeholder before using this prompt.
-->

# 6. Initiative open-question resolution review

## Use when a human must answer an initiative's open questions

Use this prompt to review every active open question in one existing
initiative. It is an interactive human-decision workflow. Precedence and
repository evidence organize the review and explain a question's consequences;
they do not choose an answer.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Example usage

> **Reference only — do not execute this example.**
>
> Using the [initiative open-question resolution review prompt](06_initiative_open_question_review.md),
> review every active open question in the attached initiative with me one at a
> time.

This example shows how to invoke the template. When using this file, execute
only the instructions in the **Initiative open-question resolution prompt**
block below. Do not execute, recurse into, or derive additional work from the
example.

## Initiative open-question resolution prompt

~~~text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md. Its shared rules
are mandatory and do not reduce this prompt's specific requirements.

Facilitate a human resolution review of every active open question for
{initiative} at {initiative_path}. This is an interactive human-decision
workflow, not an autonomous design task. A human user must explicitly answer
each source question before that question may be accepted, deferred, closed,
or used to change related initiative documents.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Preserve every technical component, profile, placement, external-party,
contract, and evidence dependency. This convention never supplies an answer to
a source question.

Read `{initiative_path}/README.md` to identify the initiative type and its
allowed output. The type does not change the human-review requirement: a source
question is answered, deferred, or closed only through an explicit human
response.

Before asking the first question, verify that the target has a readable
initiative index, `open-questions.md` register, assumption record, and every
initiative record that its index identifies as affected by decisions. Read
every active source-question section, not only its summary row. The canonical
source set is `open-questions.md` and only an initiative-local addendum that
the index explicitly identifies as its continuation. Build a complete coverage
inventory of each stable question ID, exact question text, current status,
owner, options, recommendation, dependencies, conditional trigger, acceptance
criteria, and affected documents.

Treat "Open", "Open, blocking", and "Proposed; confirm" records as active. A
"Deferred" record remains dormant until its recorded re-entry condition is met
or the human explicitly directs a change in its status. Do not use this prompt
to force a conditional question early. Keep dormant questions in the coverage
inventory and report their trigger.

When one source ID appears in a register table and a related summary or detail
section, count it once. Take its exact question, options, status, and acceptance
conditions from the authoritative source entry, then reconcile every canonical
representation of that same ID after the human responds. Do not use a summary
or supporting record to replace source content.

Use the source register's explicit dependencies and earliest-blocking order,
then stable-ID order, to select the next ready source question. Do not silently
omit an active source question. A supporting record may explain order or
evidence, but it cannot answer, accept, close, defer, or supersede a source
question.

Use `evidence/authoritative`, accepted repository decisions and
specifications, released contracts, implemented behavior and its verification,
completed initiatives, and documented evidence labels to explain constraints. A
recommendation, proposal, assumed assumption, or
`evidence/non-authoritative` source is never a human decision and cannot
override established precedent.

Ask exactly one ready source question at a time. For each one, use this
structure:

Question ID: {stable_source_id}
Original question:
{the complete source Question text copied exactly, with no paraphrase,
translation, correction, omission, or added wording}

Plain-language explanation:
{a short, plain-text explanation of the decision, its practical effect, and
what would change if the human selects an option}

Source options and recommendation:
{copy existing source options and recommendation faithfully; label the
recommendation as unaccepted and do not add invented options}

Relevant evidence and effect:
{the governing sources, precedence, dependencies, acceptance criteria, and
initiative records that the answer would need to reconcile}

Human answer requested:
Which option or in-scope answer should govern this source question? You may
select a source option, provide another in-scope answer, ask for more context,
or explicitly defer the question with a re-entry condition.

Write the Plain-language explanation for approximately an eighth-grade reading
level. Use short, direct sentences and define necessary technical terms. Do not
use allegories about schoolchildren, including schools, teachers, classrooms,
or groups of friends. Another allegory may be used only when it makes the
meaning easier to understand. Do not hide the original question inside the
explanation; always show it separately and exactly as recorded.

Do not infer an answer from source evidence, a recommendation, a precedence
review, a previous chat message about a different source ID, silence, or likely
intent. Do not change a question status; update a document; stage a file;
create a commit; or continue to a dependent question until the human gives an
explicit answer for the exact stable source ID. If the human asks for more
context, provide it and wait for a clear answer.

After an explicit human answer, create one decision receipt from
`{initiative_template_root}/initiatives/decision-receipts/decision-receipt.template.md`
before changing the source status. If this is the initiative's first receipt,
create `{initiative_path}/decision-receipts/README.md` from the shared template.
Preserve the exact question, exact answer, human authority, evidence presented,
scope, date or event, resulting disposition, affected records, and unresolved
consequences. Give the receipt a stable ID and link it from the source question
entry. If the answer is ambiguous or conflicts with authoritative evidence, do
not create a governing disposition; request clarification or use the
invariant-conflict procedure.

Then update the source open-question register:

1. Preserve the original Question text and the source options. Record the
   human's chosen answer, rationale, owner, decision date, acceptance
   conditions, and an Accepted YYYY-MM-DD status when the answer is final.
2. If the human explicitly defers the question, record Deferred and a specific
   re-entry condition. Do not infer deferral from a missing answer or an
   unresolved dependency.
3. If the answer exposes another unresolved decision, add a new stable
   open-question entry with its source link and put it into the coverage
   inventory. Do not claim completion until that new active question has its
   own explicit human answer or an explicit Deferred status.
4. If the answer establishes a durable initiative boundary, add or update the
   related assumption entry. Keep any earlier assumption or question verbatim
   for traceability, and record the source decision ID and human answer. Treat
   a new or materially changed assumption entry as unresolved until a human
   confirms that exact stable assumption ID through the initiative assumption
   confirmation review; answering a question does not automatically confirm a
   different assumption record.

Then reconcile only the existing initiative records actually affected by that
human answer: the initiative index, current working proposal when it is not
frozen, assumption, architecture, source mapping, roadmap, implementation
steps, and linked supporting records.

Maintain the initiative's intended outcome, included work, excluded work, and
ownership boundaries. Do not broaden the initiative, introduce a new
capability, change another initiative, modify a shared contract, or turn a
recommendation into an expanded plan. Preserve frozen proposal artifacts as
historical evidence. If a human answer exposes an out-of-scope or
cross-initiative conflict, record the in-scope effect and report the owner,
decision, or evidence needed without changing the external target.

After each explicit human answer and its reconciliation, inspect the diff.
Stage the decision receipt and only files changed for that one source question; never include
pre-existing or unrelated work. If there is a change to commit, commit it
before asking the next source question, using exactly this format:

{Code} {Initiative Name} - {comma-delimited scope}

Use the source question's stable ID as {Code}, the initiative index's name as
{Initiative Name}, and concise comma-delimited descriptions of the records or
boundaries changed as the scope. Follow the repository's prior initiative
commits for capitalization and terminology. Do not amend, squash, rebase,
force-push, or commit an unrelated change.

Continue until every active source question has an explicit human Accepted
answer or explicit Deferred status, and every active question created during
the review has the same outcome. A blocked or dormant question prevents a
completion claim unless its explicit source status and re-entry condition
truthfully permit deferral.

Only after every active question has an explicit human outcome and every
resulting initiative change is reconciled, update the applicable status
documents. Update the initiative index's Last updated field and every
applicable parent status record, such as {initiative_status_path}, to record
the completed review and its current result. Change the initiative's lifecycle
status or next milestone only when the human outcomes support that change.
Leave the initiative lifecycle `Proposed`; this review does not accept the
initiative. An open blocking question or an unconfirmed derived assumption
prevents handoff to the separate initiative acceptance stage. Make the final
tracking updates before committing the final resolved source question, and
include them in that source question's commit scope.

Verify that the coverage inventory is complete, every changed record has a
linked decision receipt and traceable human answer, and no unrelated files are staged. Push the new review
commits for the current branch only after the final status changes are
committed. Use a normal push; do not force-push, guess an upstream, or push
pre-existing unrelated commits. If the branch has no configured upstream or
the push fails, report the exact blocker.

After every question and derived assumption has its required human outcome, use
the initiative acceptance prompt. Only an accepted implementation initiative
may later use the SDK/API alignment prompt. Do not edit an SDK or API in this
prompt.

At the end, report the source questions reviewed in precedence order, each
explicit human answer, documents changed, commit hashes and messages, status
updates, push result, every deferred or newly opened question, and every
remaining blocker.
Do not create a separate report file.
~~~

