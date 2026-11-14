<!--
Replace every braced placeholder before using this prompt.
-->

# 5. Initiative assumption confirmation review

## Use when a human must confirm an initiative's assumptions

Use this prompt to review every current, unresolved assumption in one existing
initiative and to define or decide either kind of item discovered during that
review, including properly owned cross-initiative and project-wide matters.
It is an interactive human-decision workflow. Repository evidence can explain
a record's effects, but it cannot confirm an assumption for the human.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) together with this prompt.
The contract is mandatory and does not replace this prompt's specific
preconditions, edit boundary, verification, or reporting requirements.

## Documentary prerequisites

Use the [canonical coverage and use map](../TEMPLATE-COVERAGE.md) and the
[shared preparation procedure](WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation).
The following metadata is a reference inventory of applicable canonical
record roles, not an action list or authority to create every listed record.
<!-- tadp-prerequisites: {"stage":5,"records":["profile","initial-suite","membership","decision-receipt"],"procedure":"WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation"} -->

The executable block below applies these prerequisites to this stage before
its substantive entry check. Existing records and actual events retain their
owners and authority; conditional roles require a cited applicability result.

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
Required inputs: stable assumption IDs and original source text, affected
initial-suite records, source evidence, recorded assignment and existing human
instructions/receipts. Use project/initiatives/assumption.template.md, project/initiatives/open-questions.template.md
and project/initiatives/decision-receipts/decision-receipt.template.md with its README.
For actual project-owned items without a suitable initiative owner, use the
conditional project/decisions/assumptions-and-open-questions.template.md source
and existing project decision index/receipt destinations through the coverage
map. Do not instantiate an unused register.
Recover missing documentary inputs through their owning stages; capture an
already sufficient exact human disposition before relying on it, preserving
original event and separate capture time. Reuse existing receipts without
asking the same decision again. Missing original text, identity or human
answer remains unresolved. Validate ID-to-receipt links before human review.

For a project with the version-scope revision adopted, verify exact scope
membership, originating and contributing suite/note IDs and paths, per-source
routing, current numeric revision cycle, recorded dedicated/shared execution
mode and branch, immutable captured base ref/commit and immediate integration
target. Shared source/scopes and declared shared scope branches are valid;
initiative identities and active per-cycle assignments remain unique. Preserve
historical allocation, closure and branch history. No later-stage repair by
inference is allowed; route inconsistencies to the owning preparation/intake.
Facilitate a human confirmation review of every current, unresolved assumption for {initiative} at {initiative_path}. The ordinary path is an interactive
review. Under that path, a human user must explicitly confirm,
correct, reject as not applicable, or turn each source assumption into an open
question before its disposition or dependent claims change. Defining an
independent unresolved item does not resolve or change an earlier disposition.

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
decision method for the named assumptions, first capture that authority and
the rule-specific exception. For those covered IDs only, use the recorded
method instead of the human presentation/wait loop below. Retain the source
inventory and all applicable reconciliation steps, label actual dispositions
as agent-made, and preserve actual agent author, method, evidence, result,
rationale, affected IDs, limits, and authority.
Do not fabricate a human response or repeat a covered confirmation. All other
assumptions retain the ordinary human path. Newly discovered IDs are not
covered by proximity to an authorized ID; assess their exact delegation scope.

Apply the ownership and approval convention at {project_profile_path}. Human
owner, reviewer, and approver roles resolve as recorded for the target project.
Preserve every technical component, profile, placement, external-party,
contract, and evidence dependency.

Read `{initiative_path}/README.md` to identify the initiative type and its
allowed output. The type does not change the ordinary human-review requirement:
assumptions can be confirmed, corrected, rejected as not applicable, or turned
into an open question only through an explicit human response.

Before asking the first assumption, verify that the active branch, canonical
correlation row, realization-suite index, initiative metadata, and captured
base identity are complete and reciprocal. Stop on drift or a partial mapping;
this review must not allocate or repair identity. If a response creates a
mandatory split or independent successor, record the effect and route the new
outcome to Stage 0 without overwriting this initiative's historical identity.

Before asking the first question, verify that the target has a readable
initiative index, assumption record, open-question register, and every
initiative record identified as affected by an assumption change. Read
`assumption.md` and any continuation explicitly identified by the initiative
index. Build a complete coverage inventory of every stable assumption ID, exact
source location, current disposition, dependencies, and documents named by its
`If corrected, revisit` fields.
Retain that original review set. Append each new item of either kind with its
unique stable ID, exact original text, originating review/evidence, canonical
owner/location, scope classification, dependencies, affected records and
current unresolved disposition. Link rather than duplicate another canonical
owner's item. Do not require an existing source ID or human correction as the
origin of discovery. Respect actual dependencies across both item kinds and
owners when selecting the next ready item.

Use a source assumption record's explicit dependencies first, then stable-ID
order to select the next ready source assumption. Do not silently omit a source
record. A supporting record may explain order or evidence and expose a new
unresolved item, but cannot replace original text or resolve an assumption.

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

Canonical owner and decision target:
{item_owner_location_scope_classification_and_authority_needed}

Human confirmation requested:
Does this exact assumption hold for its stated canonical owner and scope?
You may Confirm; Correct: {replacement}; Not applicable: {reason}; or Open
question: {question that must be decided}. You may also give another answer,
including one outside the original options or reviewed initiative's scope,
or define a new assumption or open question. Each new item gets its own stable
ID and disposition; assess authority and destination before applying an answer.

For a new or existing open question selected during this review, present its
stable ID, complete exact Original question, plain-language explanation,
faithful source options and clearly unaccepted recommendation, evidence/effect,
canonical owner/target and requested human answer. Do not invent source options.
The human may select a source option, provide another answer, ask for context,
or explicitly defer with a re-entry condition. Resolve that question here
when sufficiently authorized; a separate prompt invocation is not required.
Continue presenting exactly one ready item at a time.

Write the Plain-language explanation for approximately an eighth-grade reading
level. Use short, direct sentences and define necessary technical terms. Do not
use allegories about schoolchildren, including schools, teachers, classrooms,
or groups of friends. Another allegory may be used only when it makes the
meaning easier to understand. Do not hide the original assumption inside the
explanation; always show it separately and exactly as recorded.

Do not infer a human response from source evidence, a recommendation, an
earlier review, a previous chat message about a different source ID, silence,
or likely intent. Do not mark an assumption Confirmed, Corrected, or Not
applicable, resolve a question, change dependent claims, or continue to a
dependent item until its exact stable ID has an explicit human response or
a sufficient covered alternative disposition. This does not prohibit defining
and committing independent unresolved discoveries with their source evidence.
Do not fabricate a decision receipt for discovery alone. If the human asks for
more context, provide it and wait for a clear answer on the ordinary path.

After an explicit human response, create one decision receipt from
`{initiative_template_root}/project/initiatives/decision-receipts/decision-receipt.template.md`
before changing the source disposition. Use the canonical record owner's
receipt location and index from the coverage map; for this initiative's first
receipt, create `{initiative_path}/decision-receipts/README.md` from the shared
template. Preserve the originating review separately from the decision target,
exact prompt, exact response, actual human authority, evidence
presented, scope, date or event, resulting disposition, affected records, and
unresolved consequences. Give the receipt a stable ID and link every covered
source item and canonical consumer. A response covers multiple IDs only when
it explicitly and unambiguously identifies their complete set and outcomes.
If the response is ambiguous, insufficiently authorized or conflicts with
authoritative evidence, do not create a governing disposition; request
clarification or use the invariant-conflict procedure.

Then update the source assumption record using the applicable disposition rule
below. These numbered alternatives are a reference inventory, not instructions
to apply incompatible dispositions serially:

1. For Confirm, retain the original assumption verbatim, mark that exact row
   Confirmed, and record the confirmation note and date where the record's
   format supports them.
2. For Correct, retain the original assumption verbatim, mark the row
   Corrected, and record the human's intended replacement in the correction
   field. Do not rewrite the original source text to make it appear confirmed.
3. For Not applicable, retain the original assumption verbatim, record the
   explicit reason, and remove only the canonical owner's affected reliance
   on that assumption. Link any originating-initiative effect separately.
4. For Open question, preserve the source assumption and its unresolved state.
   Add or update a stable entry in the existing open-questions.md register,
   link the two records, and state that the assumption cannot be confirmed
   until that question receives its own sufficient disposition. Use an existing
   pending disposition when the assumption record defines one; otherwise retain
   its unresolved disposition and put the question ID in the note. Use the
   ordinary question presentation above to obtain that decision during this
   review, or link a later question review if it remains pending. Then resume
   this assumption and obtain its own explicit human outcome. A question answer
   does not automatically confirm the separate assumption ID.

Then reconcile only affected authorized canonical records, including the
initiative index, editable working proposal, architecture, source mapping,
open-question register, roadmap, implementation steps and linked consumers
when the disposition actually affects them. Independent discovery of either
kind is permitted before or after any answer. Preserve exact original wording,
options, earlier dispositions and receipt links; append replacements and
supersession relationships rather than silently rewriting source history.

Maintain the initiative's intended outcome, included work, excluded work, and
ownership boundaries. Do not broaden the initiative, introduce a new
capability, modify a shared contract or silently rewrite scope. Preserve frozen
proposals and prior claims. An item owned by another named initiative links to
its canonical register; a project-wide item or one with no suitable initiative
owner uses the conditional project-owned register without an umbrella initiative.

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

After each actual disposition and its reconciliation, inspect the diff. Stage
the decision receipt and only files changed for that source item or an
explicitly covered coherent complete set;
never include pre-existing or unrelated work. If there is a change to commit,
commit it before asking the next ready item, using exactly this format:

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

Retain complete coverage of the original assumptions and append every new item
of either kind, identifying canonical owners. Report actual authorized answers,
unresolved items, deferred triggers, transferred dependencies and blocked
handoffs. An assumption linked to a pending question remains unresolved until
the question has a sufficient decision and the assumption its own disposition.
Finishing bounded review coverage is distinct from resolving every discovery.
A nonblocking external item may remain pending without becoming an in-scope
deliverable. Do not call assumption confirmation complete while applicable
assumptions remain unresolved; report covered work and exact blockers instead.

Update applicable status documents truthfully from the actual coverage,
dispositions and reconciled affected records, including pending work and its
owner rather than falsely marking it complete. Update the initiative index's
Last updated field
and every applicable parent status record, such as {initiative_status_path}, to
record the bounded review's actual result. Change the initiative's
next milestone only when actual authorized outcomes support that change. Leave the
initiative lifecycle `Proposed`; this review does not accept the initiative.
An unresolved assumption, question or external dependency blocks only the
acceptance claim or handoff it actually affects. Applicable blocking decisions
must be resolved before initiative acceptance. Make final tracking updates
before committing the final disposition, and include them in that item's commit
scope.

Verify that the review coverage inventory is complete, every changed record
reflects either unresolved discovery with source evidence or a linked receipt
and traceable actual disposition, and no unrelated files are staged. Push the
new review commits for the current branch only after the final status changes
are committed. Use a normal push; do not force-push, guess an upstream, or
push pre-existing unrelated commits. If the branch has no configured upstream
or the push fails, report the exact blocker.

At the end, report the source assumptions reviewed in precedence order, each
explicit human response or covered agent-made disposition and its authorship,
documents changed, commit hashes/messages, status updates, push result, every
new assumption/question with provenance and owner, deferred trigger, transferred
dependency, blocked handoff and remaining blocker. When applicable blocking
decisions and required reviews are complete, identify the
initiative acceptance prompt as the next stage.
Do not create a separate report file.
~~~
