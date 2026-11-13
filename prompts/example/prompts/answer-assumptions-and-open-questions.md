# Robotically resolve the example application's assumptions and open questions

[tadp:robotic]

Execute the initiative assumption and open-question reviews for the Example
Record Application through local prompt templates 05 and 06. Resolve every
in-scope assumption and question automatically, apply each decision to its
canonical initiative records, and leave each initiative ready for the next
applicable TADp workflow stage. Produce individual, reasoned LLM decisions
under the delegation below.

## Current project and authorized boundary

Resolve the current scaffold from this prompt's governing
[AGENTS.md](AGENTS.md), then read the scaffold's [root instructions](../AGENTS.md)
and [project profile](../project-profile.md). The installed `..`
directory is the project root, called `S` below. All unqualified paths in this
prompt are relative to `S`, regardless of the shell's initial directory.
Verify scaffold markers, resolved path containment, and the enclosing Git
relationship before acting. Apply the existing
[EX-GIT-DR-001 exception](../initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md):
the enclosing worktree supplies Git mechanics only.

Limit changes to the existing target initiatives' review records, decision
receipts, affected working specifications, and necessary project tracking and
work-conflict records inside `S`. Reconcile decisions directly in the app.
Keep coverage, authority, review findings, and handoffs in those canonical
records and their receipt indexes; do not create a separate report package.

Read reusable templates and authoritative sources as inputs. Preserve
`template/**`, `evidence/authoritative/LLM/**`, every lock, frozen proposal,
accepted architectural/security decision, and unrelated work. Do not change
TADp itself, validators, protection controls, project authority, immutable
correlation identity, or branch assignments. Do not create or reopen
initiatives or scopes, implement products, accept initiatives, change
lifecycle states, merge, push, publish, deploy, or release anything.

## Explicit autonomous decision delegation

The User directed this prompt revision as follows:

> I still want this to run robotically. i want all assumptions and questions resolved automatically by the LLM through this prompt.

> the initiatives should each be ready to progress through the tadp workflow once completed.

When I explicitly instruct execution of this prompt, I authorize the LLM to
resolve every currently unresolved assumption and question in the existing
Example Record Application initiatives selected from the canonical membership
index at the captured execution baseline. This includes in-scope decisions
discovered during review and assumptions or questions derived from their
answers within those same narrow outcomes. Enumerate each stable source ID
before deciding it. The delegation ends at this review run's verified handoff;
it does not carry into later unrelated work or reopen historical decisions.
Editing or reading this prompt does not execute it or record a disposition.

Use specification 02's alternative-decision-method clause and specifications
07, 08, and 11 to replace the per-item human presentation, response, wait, and
confirmation requirements in stages 5 and 6 with the LLM decision method below.
Cover the corresponding human-input requirements in templates 05 and 06,
the shared workflow contract, `../../../AGENTS.md`, `project-profile.md`, and affected
source records by exact rule locator and governing revision. Record the actual
human execution instruction and this bounded method in a decision receipt
and rule-specific exception record before the first autonomous disposition.
Do not ask for another approval to author these records or repeat a covered
per-item confirmation.

This expressly includes unresolved Deferred and conditional questions in the
design-decision review. Preserve their prior status and re-entry conditions,
record this status-change authority, and decide their in-scope policy now.
Do not claim an operational trigger has occurred or prematurely perform the
conditional work. Already resolved historical items remain historical.

The LLM must make each decision individually. Record actual agent authorship,
method, evidence, exact result, rationale, limits, and delegation links; never
invent a per-item human answer. All other gates remain required. This grants
no invariant revision, acceptance, reopening, delivery, or completion authority.
A missing future product or test is a delivery obligation, not automatically
an unresolved design decision. An actual invariant contradiction, unavailable
fact essential to a decision, or failed unexcepted prerequisite remains a
truthful blocker; do not fabricate a resolution to meet the requested totals.

## Required template execution

Use the executable instruction blocks of these installed sources, with their
mandatory shared contract, for one named initiative at a time:

| Source | Role in this run |
| --- | --- |
| [05_initiative_assumption_review.md](../template/prompts/05_initiative_assumption_review.md) | Confirm or otherwise resolve each source assumption and reconcile its consumers |
| [06_initiative_open_question_review.md](../template/prompts/06_initiative_open_question_review.md) | Answer each source question and reconcile its consumers |
| [WORKFLOW-CONTRACT.md](../template/prompts/WORKFLOW-CONTRACT.md) | Preserve stage ownership, evidence, identity, scope, Git, and handoff rules |

Execute those two named instruction blocks under their recorded
alternative-method provisions; do not merely use them as background reading
or substitute an external analysis report. Do not execute template examples
or recursively execute other referenced prompts. Resolve every placeholder
before invoking a template: use `template` for the initiative-template root,
`project-profile.md` for the project profile, and the target's canonical
README, membership, branch, registry, and status records for its remaining
bindings. Do not edit or fill the reusable template files themselves.

## Execution sequence

1. Establish the baseline and applicable authority.

   Read the local invariant suite beginning with
   `evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md`, including the
   applicable evidence, governance, lifecycle, Git, scope, receipt, workflow,
   correlation, coherence, and canonical keyword specifications. Read the
   accepted architecture and security suites beginning with their indexes.
   Check protected-source integrity without refreshing locks. Capture the
   actual worktree, branch, HEAD, staged, unstaged, and untracked paths;
   preserve pre-existing changes separately.

   Use `initiatives/initiative-index.md` and `initiatives/version-scopes.md`
   to discover canonical membership and assignments, rather than a historical
   version container or redirect. At authoring time the review covers
   `INIT-IMP-001` through `INIT-IMP-006`, owning D1 contract documentation,
   D2 container platform, D3 API/SQLite runtime, D4 Python SDK, D5 standalone
   CLI image, and D6 web bundle. Re-discover actual membership at execution.
   Read each complete initiative suite and its linked decisions, source notes,
   assumptions, questions, dependencies, and tracking records.

   Preserve the intent of
   `evidence/non-authoritative/realizations/v0.0/RZN-001-example-record-application.md`
   without promoting it over accepted `ADR-007` decomposition or `ADR-006`
   versioned feedback. Map historical realization questions to their current
   dispositions without reopening them. Inventory relevant Proposed, Accepted,
   partially performed, and affected closed work without promoting its authority.

2. Prepare complete coverage and record the delegation.

   Inventory every source assumption and question, including full detail
   sections, explicit continuations, conditional/deferred entries, and genuine
   unresolved decisions discovered in supporting records. Preserve stable IDs,
   exact original text, source locators, current dispositions, dependencies,
   affected records, and ownership. Count repeated representations of one ID
   once; distinguish historical redirects and already resolved exclusions.
   Register a newly discovered in-scope item in its owner's canonical source
   record with a stable ID before deciding it.

   Verify each target's lifecycle, exact scope, originating/contributing note
   provenance, current revision cycle, dedicated/shared execution assignment,
   actual branch, immutable captured base, and immediate integration target.
   Use only a valid prepared checkout containing the governing scaffold and
   current suite. Preserve the enclosing worktree's unrelated work. Templates
   05 and 06 cannot repair missing preparation or correlation; record the exact
   recovery blocker and owning stage instead of inferring an assignment or
   silently switching to an obsolete branch.

   In `initiatives/decision-receipts/`, capture the run's human delegation and
   bounded exception using the local receipt and gate-exception templates as
   read-only field references. Link them from the receipt index and every
   covered initiative's receipt index. Include the source prompt revision,
   exact execution instruction, actual author, complete covered source-ID set,
   exact original/replacement human-input rules, duration, risks, remaining
   obligations, and restoration. Extend the enumerated coverage before using
   the same bounded method on a derived in-scope ID.

   Record the source-position settings ledger before dispatch or retry:
   `human_gates=false`, `other_gates=true`, `preview=false`, `local=false`,
   and `review=false`. The explicit independent review below still applies.
   Link instruction blocks, target paths, per-rule authority, serial phase
   schedule, and resume identity. Persist these records before relying on the
   delegation; preserve all unexcepted checks and actual failures.

3. Execute templates 05 and 06 serially for each delivery unit.

   Process D1, D2, D3, D4, D5, then D6 in that order, using the canonical
   initiative for each unit. Complete the current unit's decisions,
   reconciliation, checks, and handoff before evaluating the next unit.
   Whole-app discovery may precede this sequence; it is not permission to
   preselect a later unit's decisions. Serialize shared writes and Git actions.

   For each initiative, execute template 05, then template 06. Use explicit
   source dependencies and stable-ID order within each review. If an assumption
   needs a question resolved first, preserve its pending state, use template
   06 on that dependency, then resume template 05 for that exact assumption.
   If a question answer creates or materially changes an assumption, give it
   its own template 05 decision. Repeat the affected 05/06 reviews until all
   in-scope source items and derived decisions have their own final outcomes;
   do not call a review complete while this loop remains open.

   Replace only the covered human interaction with this decision method:

   For each assumption, test the exact claim against applicable invariants,
   accepted boundaries, evidence, and other decisions. Confirm supported
   wording explicitly. Distinguish an intended design commitment from an
   observed fact. If wording needs correction, preserve the original verbatim
   with its truthful `Corrected` disposition, record the replacement and
   consequences, and give the corrected premise its own explicit confirmation
   under template 05. Use `Not applicable` only with a substantiated reason.
   Never label a contradicted or unverifiable factual premise `Confirmed`.

   For each question, derive constraints and an initial concrete answer before
   comparing the source recommendation. Compare at least two feasible
   alternatives when they exist, explaining why the strongest competitor loses;
   identify the controlling rule when only one answer is compatible. Select
   the best in-scope solution for this app using correctness, security,
   compatibility, maintainability, operational burden, failure/recovery, and
   verifiability as applicable. Record agreement, modification, or rejection
   of the recommendation with item-specific reasons. Resolve every subpart,
   requested path, ownership role, interface, matrix, and acceptance condition
   without inventing provisioned infrastructure, available reviewers, test
   results, or product existence.

   Exercise the delegated judgment to choose design requirements and future
   verification obligations. Do not defer a decidable item, leave it
   `Proposed; confirm`, or ask for human choice merely because the LLM made
   the decision. Exhaust safe invariant-compatible alternatives before recording
   a factual blocker. Preserve conditional policy boundaries and separate
   missing delivery evidence from a missing design answer.

   Before changing each source disposition, create its individual initiative
   decision receipt, linking the delegation and exception. Keep the original
   source wording and options, actual LLM answer or confirmation, rationale,
   evidence, author, and affected records. Use the source register's vocabulary:
   confirmed assumptions are `Confirmed`; final question answers use
   `Accepted YYYY-MM-DD` with a linked receipt and an explicit agent-made
   `Answered` result. Question acceptance is not initiative acceptance.
   Reconcile every canonical representation of that ID and each actually
   affected working proposal, architecture, source mapping, scope assessment,
   roadmap, steps, README, and tracking record. Preserve frozen artifacts.

   Follow each template's per-source-ID commit and final tracking rules.
   Inspect the diff and commit only that item's receipt and reconciliation
   before moving to the next ready item, using the prescribed source-ID,
   initiative-name, and comma-delimited scope format. Never absorb unrelated
   staged work or create an empty commit. Keep commits on the target's valid
   recorded execution branch. Remote publication is outside this invocation;
   record the templates' push step as not performed without separate authority.

   Before advancing to the next unit, verify the current unit's complete
   source coverage, applicable template exit evidence, and consistency with
   earlier decisions and the current work inventory. Record a provisional
   design-decision handoff in its review records. Final next-stage readiness
   requires the whole-app checks and independent review in steps 4 and 5.
   If later feedback changes a decision made in this run, resume its owning
   review under this delegation and create a superseding receipt; preserve
   the earlier result and handoff rather than rewriting receipt history.

   At the D4-to-D5 handoff, check D2-D4 decisions against the exact D1 contract
   baseline and `ADR-006`. Route any feedback to the owning initiative and its
   authorized review branch; re-evaluate affected decisions and handoffs before
   advancing. A proposed change to accepted contract meaning remains a blocked
   proposal requiring its own authority, not an LLM-approved invariant revision.
   Later feedback uses the same explicit versioned process. Preserve D6's
   after-D5 sequencing without claiming any product has been delivered.

4. Reconcile coherence and verify each next-stage handoff.

   Check decisions across all reviewed initiatives for compatible scope,
   ownership, interfaces, version identity, dependency order, security/data
   limits, failure/recovery, compatibility, and verification obligations.
   Revisit any affected review through its owning template and branch,
   preserving prior decisions and receipt history. Record incompatible work
   in `initiatives/work-conflicts.md` and affected initiative records.
   Use the required invariant-conflict procedure for invariant contradictions;
   if a required register action is barred by protected-source rules, preserve
   the blocker and identify the separately scoped maintenance handoff. Do not
   revise protected sources or treat an unrecorded conflict as resolved.

   For each initiative, check the entry requirements of template 07 read-only:
   a complete coherent current suite, one narrow outcome, no undisposed split
   trigger, invariant-compatible architecture/mapping, resolved assumptions and
   questions with linked receipts, current coherence inventory, unambiguous
   type/output boundaries, explicit owners and dependencies, valid preparation
   and Git identity, and an exact proposed baseline revision. Use the recorded
   alternative-method outcomes as authorized by specifications 02, 08, and 11;
   do not demand invented per-item human responses. Reconcile missing details
   that templates 05/06 own. Record any remaining earlier-stage repair with
   its exact owner and re-entry condition; never waive it to label a handoff
   ready. Future delivery tests and human acceptance remain future gates.

   Update each initiative's review coverage, Last updated fields, next-stage
   milestone, registry/status views, and parent tracking through the owning
   review's final-item commit. Keep lifecycle `Proposed`. Record readiness
   for `07_initiative_acceptance.md` only when all its applicable entry
   requirements are met; identify its exact proposed baseline and remaining
   delivery obligations. Do not execute acceptance or any delivery stage.

5. Obtain independent review and verify the final result.

   Have a distinct reviewer check source-ID coverage, authority captured before
   dispositions, actual template execution, individual reasoning, source text
   preservation, canonical statuses, receipt links, coherence, D1-D6 handoffs,
   branch/commit boundaries, and each initiative's next-stage readiness.
   Record and reconcile findings in the existing review/receipt records.
   An unavailable reviewer or unresolved finding remains an unmet requirement.

   Run the applicable existing protection, validation, local-link, and Git diff
   checks. Inspect staged, unstaged, untracked, and committed paths against
   the baseline and each initiative's recorded scope. Preserve failures and
   pre-existing drift; do not refresh a lock or alter a validator to pass.
   Confirm all task output stayed within `S` apart from the authorized Git
   mechanics, and all protected sources and unrelated work were preserved.

   Report each initiative's confirmed/corrected/not-applicable assumption
   counts, answered question counts, any precise unresolved exceptions,
   delegation and receipt links, changed records, commit IDs, checks and review
   results, and next-stage readiness with its baseline. Successful execution
   requires every in-scope assumption and question resolved in the app itself
   and every initiative ready for its next applicable TADp stage. If that is
   prevented by an unexcepted gate or essential unavailable fact, report the
   exact unmet objective and recovery path. Do not request per-item approval
   for decisions covered by this delegation or claim initiative acceptance,
   delivery, or completion.

[tadp:!robotic]
