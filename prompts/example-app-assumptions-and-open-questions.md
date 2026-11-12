# Independently assess every example-app assumption and open question

Execute this task from the TADp repository root. Read the repository
`AGENTS.md`, `prompts/AGENTS.md`, and the canonical prompt keyword specification
before acting. This is a repository-level analysis of the Example Record
Application, with
`example/evidence/non-authoritative/realizations/v0.0/RZN-001-example-record-application.md`
as the original intent and sequencing reference, and
`example/initiatives/v1/README.md` as the initiative entry reference.
The requested deliverable is a complete decision report outside the example
app; do not apply the report to the app.

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

## Decision authority and truthful meaning

When I explicitly instruct you to execute this prompt, use the independent
evaluation method below to make an agent-authored selection for every
in-scope question and an evidence-based assessment for every assumption.
Complete the analysis without asking me to choose between options that you
can assess from the available evidence. The complete bounded set is the
source-ID inventory discovered from the example app at the captured baseline;
record it before making selections.

These are analytical results in the repository report. They do not change the
canonical app records or satisfy their human decision gates. Preserve that
distinction under specifications 02, 07, and 11: an agent-selected answer is
not a human response, a supported assumption is not a recorded human
confirmation, and this report does not establish initiative acceptance,
execution readiness, verification, or completion. No gate exception or
protected-source change is requested. Applying the results later is a
separately authorized operation with its required receipts and reconciliation
inside the app.

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

3. Evaluate every item independently using the following method.

   Execute these analytical phases serially, in this exact order. Complete
   every item's assessment, phase consistency check, and recorded handoff
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
   not invent it to advance the report. An unresolved item must receive its
   precise evidence-gap disposition before handoff, and any dependent later
   answer must remain conditional or unresolved. Do not skip an unassessed
   item or claim a blocked phase finished.

   At the D4-to-D5 handoff, review D2-D4 findings against the D1 baseline under
   the v0 feedback loop and `ADR-006`. Preserve which documentation/contract
   revision guided each API/SDK selection. Distinguish proposed design
   implications from actual observed implementation evidence. If a finding
   warrants documentation or contract refinement, record the proposed change
   classification, successor/revision identity, compatibility consequences,
   and required authority in the report; retain the previous baseline and
   re-evaluate affected D2-D4 answers against the proposed revision before
   handing off. An unaccepted change remains a proposal, and dependent answers
   stay conditional. Never rewrite the app documentation or simulate live
   verification as part of this checkpoint.

   Independent reasoning does not mean ignoring another decision's constraints
   or inventing a separate answer to an already binding contract.

   For each assumption, identify its exact claim and test it against the
   governing architecture, security boundaries, source evidence, and other
   work. Record a separate report assessment: `Supported`, `Correction
   proposed`, `Not applicable`, or `Unresolved: evidence missing`. Explain why
   and cite precise evidence. For corrections, supply replacement wording
   and its consequences. For non-applicability, prove the exclusion. Separate
   a reasonable future design premise from a verified fact about an existing
   product. Do not confirm every assumption merely to finish the list.

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

   Answer every part of the original question and its stated acceptance
   requirements. Specify exact proposed paths, identities, ownership roles,
   mechanisms, matrices, failure behavior, evidence locations, and split
   consequences wherever requested. Proposed app paths are text in the report
   only. Do not invent available reviewers, provisioned infrastructure,
   credentials, observed test results, or current tool versions. Distinguish
   a selected future requirement from its unverified availability. Use primary
   sources for external technical claims and verify changeable facts when
   access permits; capture citations and access dates in the report only.

   Exhaust available evidence before declaring an item unresolved. If a fact,
   authority, or capability is genuinely unavailable, preserve the precise
   gap, its owner, consequence, and smallest next step. Give a conditional
   selection when defensible and state the condition; do not call it an
   unconditional answer. Continue independent items. Do not fabricate certainty
   or replace the entire analysis with a request for blanket approval.

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

5. Produce and independently review the complete decision report.

   Create `README.md` for the baseline, scope, authority boundary, actual
   author, execution date, source prompt path and Git revision, effective
   settings and scheduling, source inventory, counts, remaining gaps, and
   navigation. Create `decisions.md` with a separate anchored record for every
   assumption and open question. Each record must retain its source ID/text,
   current source disposition, evidence and standing, constraints, analysis,
   report assessment or selected answer, rationale, alternatives where
   applicable, recommendation comparison, dependencies, risks, evidence
   limits, future verification, and affected app records. Label all results
   as agent-authored analysis, with canonical app dispositions unchanged.

   Create `coverage.md` with one row per source item mapping its exact source
   to its decision anchor, result, dependencies, and unresolved obligations.
   Account for every discovered initiative and all exclusions. Reconcile
   total discovered assumptions and open questions against assessed, answered,
   conditional, and unresolved totals; repeats must not inflate coverage.
   Include the v0-product-to-D1-D6 mapping, each item's owning phase, and the
   serial phase/handoff record, including feedback revisions and unmet actual
   product gates. Present decision records in that phase order.
   A summary or shared rationale must not substitute for individual records.

   Obtain a distinct independent review of coverage, evidence quality,
   anti-anchoring reasoning, concrete answer quality, cross-initiative
   coherence, v0/ADR-007 phase order and ADR-006 feedback, authority limits,
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
   answer and assessment totals, independent review outcome, remaining
   conditional or unresolved items, and the example-boundary verification
   result. Claim exhaustive resolution only when every item has sufficient
   evidence; otherwise state exactly what remains. State plainly that the
   report is complete analysis outside the example app and that no canonical
   app decisions or lifecycle states were changed.
