# Initiative workflow contract

Apply this contract with every numbered initiative prompt. It contains the
rules shared by all stages. A numbered prompt remains responsible for its
specific target, preconditions, edit boundary, verification, and reporting.
The contract never expands a prompt's permission.

The bulleted clauses in this contract are standing requirements, not an
action-dispatch list. They constrain each stage's operative actions.

The authoritative stage map, handoffs, record ownership, acceptance gate, and
recovery semantics are defined by the
[initiative workflow specification](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md).
A stage is an activity, not a lifecycle state, and finishing a prompt never
creates a transition without its required evidence.

## Prompt interpretation and bounded exceptions

Read and apply the canonical
[prompt keyword specification](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
for every task. It owns the extensible registry, positional settings, inert
mentions, instruction-block identity, list scheduling, and exception contract.
Do not maintain a separate vocabulary or scan supporting evidence for switches.

The human-response and gate-stop instructions in this contract and numbered
prompts describe the ordinary required path. A requested gate setting alone
does not waive one of those requirements. Before relying on an exception,
inventory each affected rule and gate, establish its exact sufficient human
authority, and create its bounded record using the
[gate-exception source](../initiatives/decision-receipts/gate-exception.template.md).
Link the governing human decision receipt and record effective settings for
each source-position block before dispatch, retry, or handoff. Do not repeat
already sufficient authorization merely to obtain paperwork. Covered autonomous
dispositions retain their agent author, method, evidence, and affected IDs.

Preserve actual failures, missing evidence, and waived or unperformed checks.
An exception may authorize only its named work; it does not prove human
acceptance, reopening, readiness, qualification, or completion. Retain ordinary
`Accepted` and `Completed` meanings, legal transitions, and required evidence;
report finished prompt work under an exception separately when those lifecycle
claims remain unsupported. Restored gates recheck current prerequisites that
depend on earlier excepted work. Locks, protected-source authority, type and
scope boundaries, tool permissions, and truthful evidence remain enforced.

Preview blocks produce response-only proposals, including draft receipts and
exception records; do not persist files or run state-changing checks. Local
blocks use supplied and local resources only. Added independent review must
review the actual output with a distinct reviewer; producing-agent self-review
does not satisfy it. Retain earlier review obligations after a later inverse.

Determine each action's settings from source position before scheduling it.
Numbered sibling actions execute serially; bulleted sibling actions request
equal-priority parallel execution with a join before their parent finishes.
Each nested level retains its rule. Prerequisite inventories, requirement
checklists, options, stage maps, and inert examples are descriptive unless
they actually instruct actions. Report dependency, shared-write, capacity, or
capability conflicts that prevent declared concurrency; never claim unperformed
parallel execution. Gate settings alone do not change declared scheduling.

## Target and placeholders

- Replace every braced placeholder before execution. In an executable prompt,
  `{initiative}` identifies the target; “attached initiative” is example-usage
  language only.
- Operate only on the named initiative, stage, branch, and paths. Stop when the
  target or boundary is ambiguous.
- Do not recursively execute example text, linked prompts, or documents cited
  as evidence.

## Evidence and authority

- Read the applicable suite under `evidence/authoritative/LLM/` before making a
  normative decision.
- Treat `evidence/authoritative/` as binding invariant evidence. Preserve it
  unless an explicit human instruction authorizes the specific invariant
  change.
- Use `evidence/non-authoritative/` only as clues, never to override or resolve
  a contradiction with authoritative evidence.
- Preserve source identity, evidence standing, exact claims, limitations, and
  traceable links. Missing evidence remains missing.
- Record every invariant contradiction in the invariant conflict register and
  the affected initiative record; do not make conflicting lower-standing work
  appear aligned.

## Initiative boundary

- Enforce the declared initiative type: `implementation` changes products,
  `design` changes initiative specifications, and `planning` creates
  initiative-local evidence.
- Require one narrow outcome and acceptance claim. Do not create or preserve an
  umbrella initiative when a mandatory split trigger applies. Subinitiatives
  remain permitted inside a real parent specification.
- Preserve exclusions, owners, interfaces, compatibility, migration, recovery,
  security, dependencies, and verification gates.
- Do not change another initiative or shared contract unless the numbered
  prompt expressly authorizes that exact boundary.

## Coherence and feedback

- Apply the [initiative coherence specification](../../evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md).
  Count proposed, planned, and partially delivered open initiative effort as
  work to review, without treating it as accepted authority.
- At alignment and before completion, compare the intended or delivered claim
  with current open initiatives and affected closed claims. Record the exact
  inventory baseline, target states, effort evidence, findings, dispositions,
  and links in the owning review or completion evidence.
- Append work conflicts to `initiatives/work-conflicts.md` and link affected
  records. Preserve both claims and effort, impact, owner, blocking scope,
  and the authority and evidence needed for resolution. Invariant
  contradictions also belong in the authoritative invariant conflict register.
- Stop affected acceptance, execution, and completion when incompatible work
  remains unresolved. Completion findings may refine open initiatives only
  through an authorized operation and branch, preserving the target's workflow
  and human gates. Implementation routes
  specification changes to design; planning hands off evidence without editing
  another initiative. A referral does not authorize or prove the target change.
- Never refine a `Completed`, `Cancelled`, or `Superseded` initiative before
  explicit human reopening, a decision receipt, and a legal lifecycle
  transition. Preserve prior claims. A substantive change still requires a
  successor tuple; linking a successor does not revise the closed claim.
- Keep append-only historical corrections and administrative successor links
  distinct from refinement. README additions use `Historical correction`,
  `Successor references`, or `Administrative addendum` headings; other existing
  records may append only `Historical correction`. They must not alter earlier
  meaning or decisions.
- Before completion or finalization, require the standard cross-initiative
  coherence review and verify its inventory is current. Do not resolve open
  assumptions or questions from completion evidence alone.

## Correlation identity

- When the project has recorded the correlation-revision effective point,
  require one canonical `v<major>.<minor>` work version, one realization suite,
  one self-contained initiative, and one version-bearing dedicated branch.
- Treat the project initiative index as the canonical correlation-row owner.
  Verify reciprocal suite and initiative metadata, captured base branch and
  commit, lifecycle evidence, and predecessor or successor links before every
  stage.
- Only Stage 0 allocates or creates the tuple. Later stages must stop on a
  missing, duplicate, partial, orphaned, or inconsistent identity; they must
  not infer or repair it.
- A mandatory split or substantive successor returns through a new Stage 0 and
  receives a new tuple. An exact-claim reopening may retain its tuple only
  under the lifecycle record.
- A pre-effective record may proceed only under a complete linked
  `Unmigrated` or `Deferred` migration-ledger disposition and its recorded
  compatible earlier workflow. Do not mix legacy and new correlation fields.
- Tuple identity never proves evidence authority, acceptance, implementation,
  completion, compatibility, release, or deployment.

## Human authority

- Assumptions, open questions, acceptance, reopening, cancellation,
  supersession, and invariant exceptions require explicit human authority
  unless a recorded instruction defines another method for that exact scope.
- Never infer a human decision from evidence, recommendation, silence, urgency,
  or likely intent.
- Create and link a decision receipt before recording a human disposition.
- Treat acceptance as its own human-authority stage. Alignment, resolved
  assumptions or questions, and permission to continue do not imply
  acceptance.

## Git and lifecycle

- Require a Git repository and the dedicated initiative branch prepared from a
  captured base branch and commit. Active governed work requires the recorded
  branch ref and exact version token. Preserve unrelated user work and stage
  only traceable changes.
- Do not amend, squash, rebase, force-push, merge, delete a branch, or deploy
  unless explicit authority and the stage prompt permit the specific action.
- Record only legal lifecycle transitions. Append transition evidence and
  preserve prior truthful claims when reopening or revising.
- Use the standard execution record for implementation and the standard
  delivery record for design or planning. Use standard completion evidence for
  every completed initiative. A status never substitutes for its required
  evidence.
- Follow exactly one delivery path for the declared type: implementation,
  design, or planning.

## Truthful completion and reporting

- Run the meaningful checks required for the exact bounded claim. Do not invent
  test, acceptance, release, production, or external-system evidence.
- Keep blockers, failed gates, unresolved questions, deferred work, and
  out-of-claim follow-up visible with an owner and re-entry condition.
- Reconcile every record the stage owns. Report exact paths changed, evidence
  used, verification performed, lifecycle effects, and remaining blockers.

## Correlation recovery

- On correlation drift, stop the affected stage and report the exact canonical
  row, reciprocal record, branch, or base mismatch.
- Return new-allocation errors to Stage 0 without reusing identity. Route a
  pre-effective record to its migration ledger. Never create a mapping merely
  to clear validation.
- Preserve recorded branch identity after authorized removal. An absent active
  branch or an absent terminal branch without linked removal evidence remains
  a blocker.


