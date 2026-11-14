<!--
Replace every braced placeholder before using this prompt.
-->

# 6. Initiative open-question resolution review

## Use when a human must answer an initiative's open questions

Use this prompt to review every active open question in one existing
initiative and to define or decide either kind of item discovered during that
review, including properly owned cross-initiative and project-wide matters.
It is an interactive human-decision workflow. Precedence and repository evidence
organize the review and explain consequences; they do not choose an answer.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":6,"records":["profile","initial-suite","membership","decision-receipt"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

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
Required inputs: stable question IDs, exact original questions/options,
assumptions and affected records, evidence, recorded assignment and prior
human instructions/receipts. Use project/initiatives/open-questions.template.md,
project/initiatives/assumption.template.md and project/initiatives/decision-receipts/decision-receipt.template.md
with its README. For actual project-owned items without a suitable initiative
owner, select the
conditional project/decisions/assumptions-and-open-questions.template.md source
and existing project decision index/receipt destinations through the coverage
map. Do not instantiate an unused register. Recover missing documentary inputs
through owning stages; capture sufficient actual prior answers in receipts
without re-asking them.
Keep original event separate from capture time and preserve exact human text.
Missing authority, source text or immutable identity blocks affected review;
evidence alone cannot answer a question. Validate IDs, dependencies and links.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
Facilitate a human resolution review of every active open question for
{initiative} at {initiative_path}. The ordinary path is an interactive human-decision
workflow. Under that path, a human user must explicitly answer
each source question before that question may be accepted, deferred, closed,
or used to change related initiative documents.

Apply the shared contract's decision-item rules for Stage 5 and 6. Both the
human and Codex may define new assumptions and new open questions independently
from the review and its evidence, without a prior answer or correction. The
human may answer or dispose of existing and new items of either kind during
this same review, including in-scope, cross-initiative and project-wide items.
An answer outside original options or the reviewed initiative's scope is
preserved and assessed for authority and canonical destination, not rejected
solely for scope. Definition is not resolution: each newly defined item remains
unresolved until its own sufficient disposition exists. Clearly label any
proposed answer as unaccepted.

If a prior exact human instruction sufficiently authorizes an autonomous
decision method for the named questions, first capture that authority and
the rule-specific exception. For those covered IDs only, use the recorded
method instead of the human presentation/wait loop below. Retain the source
inventory and all applicable reconciliation steps, label actual dispositions
as agent-made, and preserve actual agent author, method, evidence, result,
rationale, affected IDs, limits, and authority.
Do not fabricate a human response or repeat a covered confirmation. All other
questions retain the ordinary human path. Newly discovered IDs are not
covered by proximity to an authorized ID; assess their exact delegation scope.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Preserve every technical component, profile, placement, external-party,
contract, and evidence dependency. This convention never supplies an answer to
a source question.

Read `{initiative_path}/README.md` to identify the initiative type and its
allowed output. The type does not change the ordinary human-review requirement: a source
question is answered, deferred, or closed only through an explicit human
response.

Before asking the first question, verify that the active branch, canonical
correlation row, realization-suite index, initiative metadata, and captured
base identity are complete and reciprocal. Stop on drift or a partial mapping;
this review must not allocate or repair identity. If an answer creates a
mandatory split or independent successor, preserve the decision and route the
new outcome to Stage 0 for its distinct complete initiative and assignment.

Before asking the first question, verify that the target has a readable
initiative index, `open-questions.md` register, assumption record, and every
initiative record that its index identifies as affected by decisions. Read
every active source-question section, not only its summary row. The original
reviewed initiative's canonical source set is `open-questions.md` and any
initiative-local addendum its index explicitly identifies as a continuation.
New external items retain their own identified canonical owners. Build complete coverage
inventory of each stable question ID, exact question text, current status,
owner, options, recommendation, dependencies, conditional trigger, acceptance
criteria, and affected documents.
Retain that original review set. Append each new item of either kind with its
unique stable ID, exact original text, originating review/evidence, canonical
owner/location, scope classification, dependencies, affected records and
current unresolved disposition. Link rather than duplicate another canonical
owner's item. Do not require an existing source ID or human answer as the
origin of discovery. Respect actual dependencies across both item kinds and
owners when selecting the next ready item.

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
Which answer should govern this exact question at its canonical owner/target?
You may select a source option, provide another answer including one outside
the original options or reviewed initiative's scope, ask for more context, or
explicitly defer with a re-entry condition. You may also define a new assumption
or open question; each new item gets its own stable ID and disposition.

Canonical owner and decision target:
{item_owner_location_scope_classification_and_authority_needed}

For a new or existing assumption selected during this review, present its
stable ID, complete exact Original assumption, plain-language explanation,
relevant evidence/effect, canonical owner/target and requested confirmation.
The human may Confirm, Correct with exact replacement, mark Not applicable with
a reason, identify an open question, or give another answer whose authority
and proper destination are assessed. Resolve that exact assumption here when
sufficiently authorized; a separate prompt invocation is not required. A
question answer never confirms the assumption's separate ID automatically.
Continue presenting exactly one ready item at a time.

Write the Plain-language explanation for approximately an eighth-grade reading
level. Use short, direct sentences and define necessary technical terms. Do not
use allegories about schoolchildren, including schools, teachers, classrooms,
or groups of friends. Another allegory may be used only when it makes the
meaning easier to understand. Do not hide the original question inside the
explanation; always show it separately and exactly as recorded.

Do not infer an answer from source evidence, a recommendation, a precedence
review, a previous chat message about a different source ID, silence, or likely
intent. Do not resolve a question or assumption, change dependent claims, or
continue to a dependent item until its exact stable ID has an explicit human
response or a sufficient covered alternative disposition. This does not
prohibit defining and committing independent unresolved discoveries with their
source evidence. Do not fabricate a decision receipt for discovery alone.
If the human asks for more context, provide it and wait for a clear answer on
the ordinary path.

After an explicit human answer, create one decision receipt from
`{initiative_template_root}/project/initiatives/decision-receipts/decision-receipt.template.md`
before changing the source status. Use the canonical record owner's receipt
location and index from the coverage map; for this initiative's first receipt,
create `{initiative_path}/decision-receipts/README.md` from the shared template.
Preserve the originating review separately from the decision target, exact
question, exact answer, actual human authority, evidence presented,
scope, date or event, resulting disposition, affected records, and unresolved
consequences. Give the receipt a stable ID and link every covered source item
and canonical consumer. A response covers multiple IDs only when it explicitly
and unambiguously identifies their complete set and outcomes. If the answer
is ambiguous, insufficiently authorized or conflicts with authoritative evidence, do
not create a governing disposition; request clarification or use the
invariant-conflict procedure.

Then update the source open-question register:

1. Preserve the original Question text and the source options. Record the
   human's chosen answer, rationale, owner, decision date, acceptance
   conditions, and an Accepted YYYY-MM-DD status when the answer is final.
2. If the human explicitly defers the question, record Deferred and a specific
   re-entry condition. Do not infer deferral from a missing answer or an
   unresolved dependency.
3. Add independently discovered or answer-exposed new items of either kind
   to the coverage inventory at their canonical owner, with stable identity,
   exact source/provenance and unresolved standing. Each disposition requires
   its own sufficient authority; related discovery does not resolve or reopen
   another item. Keep pending external items and their actual blocking effects
   distinct from the reviewed initiative's deliverables.
4. If the answer establishes a durable initiative boundary, add or update the
   related assumption entry. Keep any earlier assumption or question verbatim
   for traceability, and record the source decision ID and human answer. Treat
   a new or materially changed assumption entry as unresolved until that exact
   stable assumption ID receives its own sufficient disposition. Present it
   during this same review using the assumption presentation above, or link a
   later assumption review if it remains pending; answering a question does
   not automatically confirm a different assumption record.

Then reconcile only affected authorized canonical records, including the
initiative index, editable working proposal, assumption, architecture, source
mapping, roadmap, implementation steps and linked consumers when the
disposition actually affects them. Independent discovery of either kind is
permitted before or after any answer. Preserve exact original wording,
options, earlier dispositions and receipt links; append replacements and
supersession relationships rather than silently rewriting source history.

Maintain the initiative's intended outcome, included work, excluded work, and
ownership boundaries. Do not broaden the initiative, introduce a new
capability, modify a shared contract or turn a recommendation into expanded
work. Preserve frozen proposals and prior claims. An item owned by another
named initiative links to its canonical register; a project-wide item or one
with no suitable initiative owner uses the conditional project-owned register
without an umbrella initiative.

Before an external record edit, identify exact target/current state, owner,
governing revision, applicable branch and sufficient write/decision authority.
When sufficient, define the item and record its authorized disposition there
during this review without redundant approval merely for external ownership.
When missing, preserve exact input and a linked handoff with proposed owner,
blocker and re-entry condition, and continue independent authorized work without
claiming resolution. Another scaffold, repository, fork or service additionally
requires authority naming that target; a link or shared Git root is insufficient.

Link external dependencies/effects without importing their outcomes into this
initiative. A decision does not implement its consequences. Independent outcomes
route to Stage 0; coherent same-outcome revisions retain the existing route;
changed accepted claims need renewed acceptance and closed claims need recorded
authorized reopening before substantive refinement. Record invariant and work
conflicts through their governing procedures; update only affected authorized
records. Do not reopen a settled item solely because related discovery exists.

After each actual disposition and its reconciliation, inspect the diff.
Stage the decision receipt and only files changed for that source item or an
explicitly covered coherent complete set; never include
pre-existing or unrelated work. If there is a change to commit, commit it
before asking the next ready item, using exactly this format:

{Code} {Initiative Name} - {comma-delimited scope}

Use the source item's stable ID as {Code}, its canonical owner's initiative or
project index name as {Initiative Name}, and concise descriptions of records or
boundaries changed as the scope. Follow the repository's prior initiative
commits for capitalization and terminology. Do not amend, squash, rebase,
force-push, or commit an unrelated change.
For an explicitly covered complete set, retain every covered stable ID in the
commit scope and receipt links; do not turn one answer into unstated coverage.

Record discovery-only changes separately with source links and unresolved
standing; they require no fabricated human receipt. Keep commits traceable to
their actual item/owner and preserve unrelated work.

Retain complete coverage of original questions and append every new item of
either kind, identifying canonical owners. Report actual authorized answers,
unresolved items, deferred triggers, transferred dependencies and blocked
handoffs. Keep dormant questions dormant until their recorded trigger or an
explicit authorized change. Finishing bounded review coverage is distinct from
resolving every discovery. A nonblocking external item may remain pending
without becoming an in-scope deliverable. Do not claim all applicable questions
resolved while active items remain unresolved; report covered work and exact
blockers instead.

Update applicable status documents truthfully from the actual coverage,
dispositions and reconciled affected records, including pending work and its
owner rather than falsely marking it complete. Update the initiative index's
Last updated field and every
applicable parent status record, such as {initiative_status_path}, to record
the bounded review's actual result. Change the initiative's lifecycle
status or next milestone only when actual authorized outcomes support that change.
Leave the initiative lifecycle `Proposed`; this review does not accept the
initiative. An unresolved assumption, question or external dependency blocks
only the acceptance claim or handoff it actually affects. Applicable blocking
decisions must be resolved before initiative acceptance. Make final tracking
updates before committing the final disposition, and include them in that
item's commit scope.

Verify that the coverage inventory is complete, every changed record reflects
either unresolved discovery with source evidence or a linked receipt and
traceable actual disposition, and no unrelated files are staged. Push the new review
commits for the current branch only after the final status changes are
committed. Use a normal push; do not force-push, guess an upstream, or push
pre-existing unrelated commits. If the branch has no configured upstream or
the push fails, report the exact blocker.

After applicable blocking decisions and required reviews are complete, use
the initiative acceptance prompt. Only an accepted implementation initiative
may later use the SDK/API alignment prompt. Do not edit an SDK or API in this
prompt.

At the end, report the source questions reviewed in precedence order, each
explicit human response or covered agent-made disposition and its authorship,
documents changed, commit hashes/messages, status updates, push result, every
new assumption/question with provenance and owner, deferred trigger, transferred
dependency, blocked handoff and remaining blocker.
Do not create a separate report file.
~~~
