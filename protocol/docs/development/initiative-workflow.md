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

## Numbered workflow

The prompt sequence under `../../template/prompts` is intentionally explicit.
Its binding stage order, entry and exit contracts, record ownership, and
recovery behavior come from the
[authoritative workflow specification](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md).
A stage is an activity; a lifecycle state is an evidence-backed standing.
Finishing a stage does not automatically change lifecycle state.

### 0. Prepare initiative

- Confirm a valid Git repository and clean worktree.
- Capture the actual current branch as the base branch.
- Create and switch to a new dedicated initiative branch.
- Create only the minimal initiative and proposal-source README skeleton when
  the target is new.

Preparation does not create the proposal or complete initiative record.

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

### 4. Align initiative

- Reconcile the complete suite as one specification.
- Validate evidence standing before accepting an initiative claim.
- Keep scope, ownership, IDs, dependencies, roadmap, steps, and verification
  coherent.
- Stop and route decomposition if current evidence exposes an umbrella scope.

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

Every transition is appended to lifecycle history. Shared status views mirror
the initiative; they do not create its state.

## Returning to an earlier stage

- A failed entry gate returns to the stage that owns the missing evidence.
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

Closing a branch, version, parent, or portfolio does not make unfinished work
disappear.

