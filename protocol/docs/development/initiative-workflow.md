# Initiative workflow

## Initiative types

Every initiative declares exactly one type:

| Type | Alignment direction | Permitted primary output | Prohibited shortcut |
|---|---|---|---|
| `implementation` | Product to accepted specification | Product source, configuration, tests, SDK/API implementation, product documentation, and operational artifacts | Changing an existing specification to fit implementation |
| `design` | Specification to observed product evidence | Initiative specifications and supporting initiative evidence | Creating a new product |
| `planning` | Evidence for later initiatives | Initiative-local analysis and evidence | Changing products or another initiative's specification |

Type boundaries apply throughout preparation, alignment, execution, and
completion. When evidence exposes work of another type, create or route a
separately scoped initiative.

## Narrow scope before workflow

Before acceptance, `scope-assessment.md` must show that the initiative has one
coherent outcome, owner, authority boundary, output type, acceptance claim, and
lifecycle. Split the work when a portion has an independently acceptable
outcome, different owner, different authority, different type, separable
verification or release, unrelated destination, or independent lifecycle.

Use siblings for independent outcomes. Use a subinitiative only when a real
parent specification owns a bounded requirement and the child owns one smaller
dependent outcome. A parent may coordinate; it may not hide partial or
unrelated work.

## Correlated work identity

Every work unit governed by the correlation revision has one canonical
`v<major>.<minor>` work version, one realization suite, one self-contained
initiative, and one version-bearing dedicated branch from a captured base
branch and commit. The project initiative index owns the canonical row.
Suites, initiatives, status, delivery, completion, and Git records link to it.

The tuple establishes identity, not authority or lifecycle standing. Every
mandatory split and substantive successor receives a new tuple. An unchanged-
claim reopening may retain its tuple; a pre-effective record follows its
migration-ledger disposition.

## Coherence across initiative work

Open initiatives (`Proposed`, `Accepted`, and `In progress`) represent work
that must be considered when another initiative changes a shared contract,
product, dependency, or ownership boundary. Include their specification
effort, decisions, planned steps, and partial outputs in the comparison.
Proposed effort remains proposed: recognizing its cost and dependencies does
not authorize its delivery or give it precedence over accepted authority.

The [initiative coherence specification](../../evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md)
governs this review. Preserve both sides of an incompatible work claim in
`initiatives/work-conflicts.md` and link the entry from the affected initiative
records. Record the exact claims, source revisions, lifecycle standing, effort
at risk, affected gates, owner, and resolution or required human decision.
An invariant contradiction also belongs in the authoritative invariant conflict
register. A conflict between proposed work items does not become an invariant
merely because it is recorded.

Pause only the acceptance, execution, or completion claims made incompatible
by the conflict. Do not silently discard earlier planning effort, rewrite
another initiative, or treat the latest completed work as the deciding
authority. Independent compatible work may continue.

## Numbered workflow

The prompt sequence under `../../template/prompts` is intentionally explicit.
Its binding stage order, entry and exit contracts, record ownership, and
recovery behavior come from the
[authoritative workflow specification](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md).
A stage is an activity; a lifecycle state is an evidence-backed standing.
Finishing a stage does not automatically change lifecycle state.

### 0. Prepare initiative

- Confirm a valid Git repository and clean worktree.
- Preflight canonical syntax and uniqueness for the proposed version, suite,
  initiative, branch, paths, base branch, and base commit without writing.
- Capture the actual current branch and commit as the immutable base.
- Create and switch to the new version-bearing dedicated branch.
- On that branch, create the suite index and initial realization note,
  canonical correlation row, reciprocal metadata, and minimal initiative and
  proposal-source README skeleton as one unit.

Preparation does not accept the initiative, create the proposal or complete
initiative record, or begin delivery.

### 1. Create proposal

- Use an existing realization as the primary source.
- Create only the canonical proposal.
- Preserve uncertainty and cite material sources.
- Do not treat proposal content as accepted architecture.

### 2. Align proposal

- Edit only the existing canonical working proposal.
- Compare it with authoritative evidence, accepted decisions, released
  contracts, verified implementation, and relevant initiatives.
- Preserve frozen historical inputs.
- Record rather than conceal conflicts.

### 3. Create initiative

- Complete the canonical initial suite from the shared templates.
- Record assumptions as unresolved rather than autonomously confirming them.
- Record active questions for human decision.
- Complete the scope assessment and stop broad acceptance when a split trigger
  applies.
- Add the initiative to applicable registry and status views.
- Reconcile the existing Stage 0 canonical row without changing its allocated
  identity.

### 4. Align initiative

- Reconcile the complete suite as one specification.
- Validate evidence standing before accepting an initiative claim.
- Keep scope, ownership, IDs, dependencies, roadmap, steps, and verification
  coherent.
- Stop and route decomposition if current evidence exposes an umbrella scope.
- Compare the claim with affected open initiative effort and record work
  conflicts before handing off to human review.

### 5. Confirm assumptions

- Review one stable assumption ID at a time.
- Present the exact assumption, plain-language explanation, evidence, and
  affected records.
- Wait for an explicit human response.
- Create and link a decision receipt before changing the disposition.
- Commit only the receipt and reconciliation for that decision.

### 6. Resolve open questions

- Review one ready question at a time in dependency order.
- Preserve the exact question, source options, recommendation status, and
  evidence limitations.
- Wait for an explicit human answer or explicit deferral with a re-entry
  condition.
- Create and link a decision receipt before recording the answer.

### 7. Accept initiative

- Verify that the complete proposed specification is coherent and
  invariant-compatible.
- Present the exact bounded claim, output boundary, gates, limitations, and
  accepted-baseline revision to the identified human authority.
- Wait for an explicit Accept, Reject, or Revise response.
- Create the acceptance receipt before changing lifecycle standing.
- Only an explicit Accept response may record `Proposed` to `Accepted`.

Assumption confirmation and question resolution make acceptance possible; they
do not perform acceptance.

### 8. Align SDK/API surfaces

This stage applies only to an accepted implementation initiative when affected
SDK/API surfaces exist. Align compatible existing SDK/API surfaces to the initiative
without using an existing limitation to narrow or reinterpret the initiative.
Route specification conflicts to design work.

### 9. Review implementation readiness

This is a read-only comparison immediately before product execution. Review the
requested phase or work set against current authoritative evidence, accepted
specifications, dependencies, owners, product state, and verification inputs.
A missing or non-ready gate blocks only the affected execution.

### 10. Execute implementation

- Create `execution-record.md` when implementation actually begins.
- Build the step-to-target ledger before changing products.
- Work in dependency order and maintain paths, commands, results, deviations,
  commits, and blockers in the record.
- Correct products that conflict with accepted specifications.
- Stop product work that would require a specification change.
- Create `completion-evidence.md` only when every in-scope gate passes.

### 11. Deliver design

- Create `delivery-record.md` when accepted specification work begins.
- Change only accepted specification destinations and supporting initiative
  evidence.
- Treat observed products as evidence, not edit targets.
- Record consumer, compatibility, migration, and verification effects.
- Route required product work to an implementation initiative.
- Create completion evidence only for the exact delivered design claim.

### 12. Deliver planning evidence

- Create `delivery-record.md` when accepted evidence work begins.
- Create only the accepted initiative-local evidence outputs.
- Preserve source classifications, methods, limitations, and missing evidence.
- Keep observations, inferences, recommendations, and human decisions distinct.
- Do not edit a product, specification, authoritative source, or another
  initiative.
- Create completion evidence only for the exact delivered evidence claim.

### 13. Finalize initiative

- Verify that lifecycle history, completion evidence, status, branch diff, and
  the type-specific execution or delivery record describe the same claim.
- Refresh the completion coherence review when target initiatives or their
  dependencies changed after that review.
- Stage and commit only traceable initiative work.
- Push and open one pull request when the repository is configured and the
  stage is authorized.
- Do not merge, deploy, enable auto-merge, or delete the branch as an implicit
  part of finalization.

## Lifecycle

| State | Meaning |
|---|---|
| `Proposed` | The bounded claim is under review and authorizes no delivery. |
| `Accepted` | Human authority accepted the coherent specification and gates. |
| `In progress` | Permitted work actually began with required Git and stage evidence. |
| `Completed` | The exact accepted claim passed every in-scope gate and has completion evidence. |
| `Cancelled` | Work stopped without a replacement; partial work and evidence remain disposed. |
| `Superseded` | A named replacement owns the claim and history is retained. |

`Reopened` is an event rather than a status. Reopening preserves the prior
accepted or completed claim, records human authority and impact, and returns to
`Proposed` unless the unchanged-claim exception is explicitly authorized.

Closed initiatives (`Completed`, `Cancelled`, and `Superseded`) must be
explicitly reopened before their specifications are refined. A completion
finding does not supply reopening authority. Keep factual history corrections
append-only and keep successor links distinct from changes to the closed
claim. A substantive change still requires a successor tuple; reopening does
not permit reuse of the old identity for a different claim.

Every transition is appended to lifecycle history. Shared status views mirror
the initiative; they do not create its state.

## Returning to an earlier stage

- A failed entry gate returns to the stage that owns the missing evidence.
- Correlation drift returns to Stage 0 recovery without inferring or reusing
  identity; pre-effective records return to their migration ledger.
- A human review resumes at the next unresolved stable ID without duplicating
  prior receipts.
- New authoritative evidence or a changed accepted premise returns to alignment
  and requires new acceptance before delivery resumes.
- Material base-branch or dependency drift requires comparison with the
  accepted baseline; drift that changes the claim returns to alignment.
- Partial delivery remains in progress, blocked, cancelled, or superseded. It
  is not completed by narrowing the claim after the fact.

## Completion rule

An initiative is complete only when every in-scope requirement maps to a
delivered product or evidence output, applicable invariant and acceptance gates
pass, verification supports the exact claim, all records agree, and remaining
work has a truthful owner and disposition.

Before recording completion, document a cross-initiative coherence review in
`completion-evidence.md`. Identify the inventory and source baseline reviewed,
every other open initiative and its effort, relevant closed claims, findings,
and linked dispositions. Include `Proposed` initiatives. A target outside the
affected boundary still receives an explicit no-impact finding with rationale;
record an evidenced no-target result when there are no other open initiatives.
Silence is not a review. Use the template's `Inventory baseline` and
`Work-conflict register` fields and its target review table.

Use completion findings to refine open initiatives through their owning
workflow. Proposed targets return through alignment and human decisions;
accepted or in-progress targets require the authorized revision and acceptance
steps when their baseline changes. Design work owns specification changes;
implementation and planning work record findings and route them within their
type boundaries. Evidence alone never answers a human open question.

A handoff to later work does not complete that work. The source initiative may
complete with a recorded follow-up only when its own exact claim remains
coherent and all of its gates pass. A conflict that invalidates its claim must
be resolved before completion. The receiving initiative keeps its own
lifecycle, decisions, branch, and verification obligations.

Closing a branch, version, parent, or portfolio does not make unfinished work
disappear.

