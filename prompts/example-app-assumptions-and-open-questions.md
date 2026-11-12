# Robotically answer every example-app question and confirm its assumptions

[tadp:robotic]

Execute this task from the TADp repository root. Read the repository
`AGENTS.md`, `prompts/AGENTS.md`, and the canonical prompt keyword specification
before acting. This is a repository-level analysis of the Example Record
Application, with
`example/evidence/non-authoritative/realizations/v0.0/RZN-001-example-record-application.md`
as the original intent and sequencing reference, and
`example/initiatives/v1/README.md` as the initiative entry reference.
The requested deliverable is a complete delegated-decision package outside
the example app: record every in-scope open question as `Answered` and every
in-scope assumption as `Confirmed` through individual independent decisions,
without further human input. Do not apply the package to the app.

## Explicit target and output boundary

This prompt explicitly selects repository-owned analytical support files as
its target instead of the default protocol-maintenance target described in
`prompts/AGENTS.md`. All new files, reports, inventories, notes, review results,
logs, and temporary artifacts must remain under
`prompts/reports/example-app-decisions/<run-id>/` at the repository root. Use
an unused run ID and preserve earlier reports. This task has no protocol-owned
change to synchronize to the example.

Treat the entire `example/` tree as read-only evidence. Do not create, edit,
rename, move, delete, or generate anything there, including decision receipts,
conflict entries, assumption dispositions, question answers, status updates,
caches, test output, or links back to this report. Do not run the application
or tools that might write there. Do not switch to or alter its initiative or
scope branches. Do not remove pre-existing evidence to make the tree appear
untouched. Leave its existing content and history intact.

Do not change `protocol/`, reusable templates, authoritative sources, locks,
validators, or protection controls. Do not implement products, allocate or
reopen initiatives, change lifecycle states, accept work, merge, push, publish,
or release anything. Preserve all unrelated work. Use the enclosing repository
Git context for this report and scope any staging or commits to its output
directory.

## Explicit robotic decision authority and limits

The User explicitly instructed this prompt revision as follows:

> I am expecting this to run "robotically" i want all open questions recorded as answered and all assumptions confirmed without human input

On explicit execution of this prompt, I authorize the agent to answer each
in-scope open question and confirm each in-scope assumption using the
independent decision method below. The complete bounded set is the source-ID
inventory discovered from the example app at the captured baseline, including
report-local IDs for newly found items. Record that set before relying on the
delegation. It does not extend to later unrelated work or previously resolved
historical decisions.

Under specification 02's "Assumptions and questions" alternate-method clause,
replace the requirement for a separate human response on each covered item
with the agent's independently reasoned decision, recorded under this human
delegation. Under specifications 07 and 11, capture the exact human authority
and named human-input rules in a receipt and bounded exception record before
the first disposition. Include the corresponding assumption/question
human-input requirements in the applicable `AGENTS.md`, project profile, and
source records, with exact locators and governing revisions. Do not ask for
another approval to create these records or repeat per-item confirmation
within this covered set. This is a delegation of decisions, not a blanket
endorsement of the existing recommendations or assumption wording.

Record actual agent-made `Answered` and `Confirmed` dispositions in the
repository package, rather than recommendations awaiting human review. Keep
the author, method, human authority, evidence, and exact confirmed wording
explicit for each item. An agent-made disposition is not a human answer or
human confirmation; the receipt preserves the delegation, not invented
per-item human responses. Keep the original app disposition in a separate
source-status field: its files remain unchanged under the read-only boundary.
Do not treat that unchanged source status as a reason to request human input
or leave the package's covered design decisions open.

The robotic switch requests lifting only human-input gates, and this
delegation covers only assumption/question decisions in this package. All
other gates, independent review, source identity, evidence truth, protected
sources, and locks remain enforced. It supplies no initiative acceptance,
execution readiness, verification, reopening, or completion. Applying these
decisions to canonical app records remains a separate operation requiring
its own authorized reconciliation; this prompt leaves no records there.

## Execution sequence

1. Establish the read-only baseline and applicable authority.

   Read `protocol/AGENTS.md` and the protocol invariant-suite index, then the
   applicable authority, governance, decision-receipt, coherence, and keyword
   specifications. Read `example/AGENTS.md`, `example/project-profile.md`, its
   adopted invariant-suite index and applicable specifications. Read the
   authoritative architecture suite beginning with
   `example/evidence/authoritative/architecture/00-architecture-suite-index.md`,
   and the applicable security suites beginning with their indexes under
   `example/evidence/authoritative/security/`. Follow exact normative source
   links needed for each decision before drawing conclusions. Preserve source
   identity, governing revision, standing, and existing exceptions; copying a
   source into the report does not promote its authority.

   Then read the original `v0.0/RZN-001` realization named above, especially
   "Candidate product sequence", "Documentation and implementation feedback
   loop", and "Historical suggested next step and current handoff". Follow
   its authoritative reconciliation to `ADR-007` for the current D1-D6
   decomposition and order, and `ADR-006` for versioned feedback. Preserve the
   original intent without promoting historical wording over those accepted
   decisions. Map historical `RZN-001-Q01` through `Q17` to their current
   authoritative dispositions; their presence in v0 does not reopen them.

   Resolve the repository root and verify that the output directory is outside
   `example/` and all protected trees, including after path indirection. Capture
   the current branch, commit, staged, unstaged, and untracked paths before any
   write. Record a file-path and content-hash inventory of `example/`, including
   pre-existing untracked files, in the report directory so the final check can
   detect additions, removals, and changed content. Avoid commands that create
   caches or other output under the example.

2. Discover and reconcile the complete app inventory.

   Start at `example/initiatives/v1/README.md`, but discover actual membership
   through `example/initiatives/initiative-index.md` and
   `example/initiatives/version-scopes.md`. Cover the whole example app across
   all registered scopes, not only the `v1` container. At authoring time the
   six initiatives cover contract documentation, container platform, API and
   SQLite runtime, Python SDK, standalone CLI image, and web application
   bundle. Re-discover current membership rather than treating this list as
   exhaustive or as authority.

   Read each initiative's README, `assumption.md`, `open-questions.md`, proposal,
   architecture, source mapping, scope assessment, roadmap, steps, linked
   decisions, originating and contributing realizations, and relevant product
   evidence. Include proposed, accepted, and partially performed effort in the
   coherence inventory without promoting its authority. Inspect relevant
   closed work as context while preserving its claims.

   Inventory every assumption and unresolved decision, including blocking,
   deferred, implied, or unregistered questions found outside the main tables.
   Preserve each existing source ID, exact text, source path and heading or
   line locator, initiative and scope, current disposition, authority,
   dependencies, and affected records. Give newly discovered questions
   report-local IDs; never invent canonical app IDs. Distinguish canonical
   entries from repeated summaries, legacy redirects, and already resolved
   historical decisions. Preserve every distinct item even when several share
   wording. Record exclusions with reasons and source links. Do not silently
   reopen a previously answered question.

   Assign each item to its owning D1-D6 analytical phase below, retaining its
   source-ID links and cross-phase dependencies. Map v0 Product 1 to D1,
   Product 2 to D2-D4 (the accepted Docker-platform addition and API/SDK split),
   Product 3 to D5, and Product 4 to D6. Scope numbers, directory order, and
   apparent lack of a code dependency must not replace this schedule. A
   cross-cutting item retains one owner and is checked by later consumers;
   earlier phases may state requirements for it without preselecting a later
   phase's implementation answer.

   Before recording any autonomous answer or confirmation, create
   `authority.md` as the specification 07 human delegation receipt and
   `gate-exception.md` as its specification 11 bounded exception record in
   this run's repository output directory. Read the protected
   `protocol/template/initiatives/decision-receipts/gate-exception.template.md`
   as a field reference without modifying it. Preserve the exact instruction
   quoted above and actual execution instruction separately from the agent's
   interpretation, the human authority, capture event, actual author,
   source-prompt path/revision, complete covered source-ID list, and exact
   original/replacement human-input requirements. Record the duration as this
   inventory's decision run through final verification, with no carryover
   authority to other tasks. Include risks, limits, remaining obligations,
   restoration, and actual Git evidence when available.

   Record the source-position settings ledger before dispatch: the operative
   robotic block requests `human_gates=false`; `other_gates=true`,
   `preview=false`, `local=false`, and `review=false` retain their defaults.
   The explicit independent review requirement below still applies. Link
   block ranges, serial D1-D6 scheduling, retry/resume identity, output paths,
   and the exact per-rule authority. The receipt/exception may cover the
   enumerated set, but each resulting decision requires its own source-ID
   record linking both. Reconcile package consumers; identify source-app
   reconciliation as not performed, never as a passed or waived product gate.

   Initialize `decisions.md` and `coverage.md` after recording that authority.
   Persist each source-ID disposition as it is made and reconcile its phase
   handoff before advancing; do not wait for final reporting to record the
   answers and confirmations. Step 5 finalizes these same records.

3. Evaluate every item independently using the following method.

   Execute these decision phases serially, in this exact order. Complete
   every item's decision, phase consistency check, and recorded handoff
   before beginning the next phase's evaluation. Whole-app discovery and
   read-only dependency inspection may precede the phases; they do not permit
   speculative decisions in later phases. Parallel assessment is permitted
   only for independent items within the current phase, with separate records
   and serialized shared writes. Use the per-item method below in every phase.

   1. D1: Assess contract-documentation assumptions and questions. Identify the
      exact governing contract revision and the proposed documentation baseline
      that subsequent analytical phases will consume; claim no SDK/API
      implementation or observed behavior.
   2. D2: Assess container-platform and runtime-packaging items against the D1
      baseline, keeping platform topology and artifact evidence distinct from
      API/domain behavior.
   3. D3: Assess API and SQLite runtime-image items against the identified D1
      contract and compatible D2 platform selections.
   4. D4: Assess Python SDK items against D1/D2 and the D3 API contract and
      compatibility selections. Complete the documentation-feedback checkpoint
      described below before handing off to D5.
   5. D5: Assess standalone CLI-image items against the recorded D1-D4
      selections, including the exact proposed SDK/API compatibility boundary.
   6. D6: Assess web-bundle items last. Preserve the explicit after-D5
      sequencing gate even though the browser does not depend on CLI code.

   Record each phase's input revisions or report anchors, per-item results,
   checks, remaining evidence gaps, and output handoff. These are analytical
   checkpoints, not accepted or completed products. Missing acceptance, live
   API conformance, artifact hashes, or release evidence remains missing; do
   not invent it to advance the package. Choose design requirements and
   verification plans autonomously; missing future product verification does
   not keep an otherwise decidable design question open. Carry those unmet
   verification obligations in the handoff separately from decision status.
   A genuine invariant conflict or unverifiable factual premise must retain
   its precise blocker and affected dependency; do not label it confirmed
   or claim a blocked phase finished merely to meet the requested totals.

   At the D4-to-D5 handoff, review D2-D4 findings against the D1 baseline under
   the v0 feedback loop and `ADR-006`. Preserve which documentation/contract
   revision guided each API/SDK selection. Distinguish proposed design
   implications from actual observed implementation evidence. If a finding
   warrants documentation or contract refinement, record the proposed change
   classification, successor/revision identity, compatibility consequences,
   and required authority in the report; retain the previous baseline and
   re-evaluate affected D2-D4 answers against the proposed revision before
   handing off. An invariant-compatible documentation refinement may be fully
   decided in this package without another human approval; applying it inside
   the app remains outside scope. A change to accepted contract meaning stays
   a proposal, not operative authority. Keep any incompatible claim blocked
   and distinguish its required acceptance from the package's delegated
   decisions and future delivery compatibility. Never rewrite the app
   documentation or simulate live verification as part of this checkpoint.

   Independent reasoning does not mean ignoring another decision's constraints
   or inventing a separate answer to an already binding contract.

   For each assumption, identify its exact claim and test it against the
   governing architecture, security boundaries, source evidence, and other
   work. Make the confirmation yourself under the recorded delegation; do
   not leave a supported premise merely `Assumed aligned`, `Supported`, or
   awaiting human validation. Record `Disposition: Confirmed`, the precise
   confirmed wording, confirmation basis, actual author, rationale, evidence,
   and authority/exception links. Distinguish `Design commitment` from
   `Observed fact`: confirmation of an intended boundary does not assert
   that a product exists or has passed future tests.

   Resolve a design ambiguity autonomously. If compatible corrected wording
   is necessary, preserve the original claim and its assessment, explain the
   correction and consequences, and explicitly confirm the corrected premise
   in the package. Do not report the original wording as confirmed unchanged.
   A non-applicable, contradicted, or unverifiable factual claim cannot be
   relabelled true; record its exact exception/blocker and exclude it from
   confirmed totals. Seek an invariant-compatible resolution within the
   delegation before declaring that the all-confirmed objective is unmet.

   For each open question, first restate the concrete problem and derive its
   hard constraints and decision criteria from authoritative evidence and the
   app's intended outcome. Form an initial answer from those constraints
   before comparing it with the source's recommendation. A recommendation is
   a candidate, not a default, tie-breaker, or authority.

   Compare at least two genuinely feasible alternatives when alternatives
   exist; add better alternatives beyond the source's menu when justified.
   Generic choices such as "adopt the recommendation" or "use a compatible
   alternative" are not solutions: name concrete mechanisms and boundaries.
   If only one solution is invariant-compatible, identify the controlling
   rule and explain why the alternatives fail rather than inventing options.

   Select the best solution for this app using item-specific reasoning about
   correctness, scope cohesion, security, compatibility, maintainability,
   operational burden, reproducibility, failure/recovery, and verifiability
   where relevant. Explain the tradeoffs and why the strongest competing
   option loses. Then compare the independently derived selection with the
   existing recommendation and record agreement, modification, or rejection
   with reasons. Neither agreement nor disagreement is a quota.

   Record each selected question result as `Disposition: Answered`, with the
   exact answer, actual agent author, decision method, rationale, and linked
   authority/exception. Do not leave the result `Open`, `Proposed; confirm`,
   or awaiting human approval merely because the agent made the decision.

   Answer every part of the original question and its stated acceptance
   requirements. Specify exact proposed paths, identities, ownership roles,
   mechanisms, matrices, failure behavior, evidence locations, and split
   consequences wherever requested. Proposed app paths are text in the report
   only. Do not invent available reviewers, provisioned infrastructure,
   credentials, observed test results, or current tool versions. Distinguish
   a selected future requirement from its unverified availability. Use primary
   sources for external technical claims and verify changeable facts when
   access permits; capture citations and access dates in the report only.

   Exercise the delegated judgment to settle scope, tooling, ownership roles,
   compatible mechanisms, and verification requirements yourself. An absent
   future implementation, runner, or test result is a delivery obligation,
   not automatically an unanswered design question. Do not use deferral,
   conditional recommendations, or a request for human choice to avoid an
   in-scope decision that this method can make. Where an answer genuinely
   depends on an unavailable fact, exhaust the available evidence and safe
   alternatives, then record the precise condition/blocker, owner, and
   smallest next step without asking for another per-item decision. Do not
   call a conditionally selected answer unconditional or count a blocked
   question as answered. Continue only the work permitted by the serial
   phase contract, preserving truthful failures and unmet objectives.

4. Reconcile the selections across the application.

   Check every assessment and answer against all applicable invariants and
   the other selected answers. Review scope and split boundaries, D1-D6
   ownership, source authority, version identities, artifact placement,
   interfaces, dependency order, security/data limits, environments, review
   responsibilities, compatibility, failure/recovery, and verification gates.
   Revisit affected individual answers when reconciliation changes them,
   preserving the rationale and dependencies for each source ID. Later CLI or
   web findings that affect an earlier phase must use the same explicit
   versioned feedback process and renewed downstream consistency checks;
   retain the original phase sequence and every revised handoff. Do not merge
   separately acceptable outcomes into an umbrella initiative.

   Preserve discovered invariant contradictions and incompatible efforts in
   the repository report with both exact claims, source standing, affected
   IDs, owner, blocked action, and required decision. Identify the canonical
   app conflict registers and affected records that would need reconciliation
   on later authorized application. Do not write those entries inside
   `example/`, claim canonical conflict recording is complete, or treat a
   conflict as resolved merely because it is listed in the report. If a
   required app record cannot be written within this read-only boundary,
   report that as an outstanding application obligation and stop only the
   conflicting conclusion.

5. Finalize and independently review the complete decision package.

   Create `README.md` for the baseline, scope, authority boundary, actual
   author, execution date, source prompt path and Git revision, effective
   settings and scheduling, source inventory, counts, remaining gaps, and
   navigation. Finalize `decisions.md` with a separate anchored record for every
   assumption and open question. Each record must retain its source ID/text,
   current source disposition, evidence and standing, constraints, analysis,
   delegated `Confirmed` or `Answered` disposition, actual decision author,
   method, exact confirmed wording or answer, authority/exception links,
   rationale, alternatives where applicable, recommendation comparison,
   dependencies, risks, evidence
   limits, future verification, and affected app records. Label all results
   as agent-made decisions under human delegation, with source-app
   dispositions unchanged. Reconcile `authority.md` and `gate-exception.md`
   with every actual per-ID result and package consumer.

   Finalize `coverage.md` with one row per source item mapping its exact source
   to its decision anchor, result, dependencies, and unresolved obligations.
   Account for every discovered initiative and all exclusions. Reconcile
   total discovered assumptions against confirmed-as-written,
   corrected-and-confirmed, and exceptional/unconfirmed totals; reconcile
   questions against answered and exceptional/unanswered totals. Keep future
   delivery/verification obligations separate from unresolved decisions.
   Repeats must not inflate coverage. Require all covered questions answered
   and all covered assumptions confirmed for the requested successful result;
   no row may remain pending human input merely for a delegated decision.
   Include the v0-product-to-D1-D6 mapping, each item's owning phase, and the
   serial phase/handoff record, including feedback revisions and unmet actual
   product gates. Present decision records in that phase order.
   A summary or shared rationale must not substitute for individual records.

   Obtain a distinct independent review of coverage, evidence quality,
   anti-anchoring reasoning, concrete answer quality, cross-initiative
   coherence, v0/ADR-007 phase order and ADR-006 feedback, receipt/exception
   coverage before dispositions, actual agent authorship, authority limits,
   and the read-only example boundary. Record findings and their
   reconciliation in `review.md` in the same report
   directory. An unavailable reviewer remains an unmet review requirement.

6. Verify the output boundary and report the actual result.

   Compare the final `example/` path/hash inventory with the initial snapshot
   and inspect its Git diff and status, including untracked paths. Verify
   that all task-created or changed files are within this run's repository
   report directory and that no protocol/mirror or protected-source changes
   occurred. Preserve and report pre-existing changes separately. If drift
   appears, identify it without overwriting concurrent work or deleting
   evidence. Check report links, source-ID coverage, and whitespace. Record
   verification commands and observed results in the report.

   Finish with the report link, per-initiative assumption/question counts,
   answered/confirmed totals, receipt and exception links, independent review
   outcome, outstanding delivery/verification obligations, any genuine
   exceptional/unresolved items, and the example-boundary verification
   result. Successful execution requires every covered question recorded
   `Answered` and every covered assumption `Confirmed` with individual
   reasoning and authority links. If an unexcepted invariant or factual
   limitation prevents that result, report the exact unmet objective rather
   than fabricate success. Do not end by asking for human approval of
   delegated items. State plainly that these decisions are recorded outside
   the example app and that no canonical app files or lifecycle states were
   changed. At prompt end the robotic setting does not carry into another
   task; resumed work retains its recorded source prompt and block identity.

[tadp:!robotic]
