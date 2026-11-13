<!-- Replace every braced placeholder before execution. -->

# 0. Assess realization fit and prepare execution placement

Use this prompt when a human requests processing of an identified realization
under the adopted version-scope workflow. Assess existing targets before
allocating anything. An existing complete initiative reuses its records;
Stages 1 and 3 must not recreate them. New allocations remain `Proposed`.

## Shared workflow contract

Apply [WORKFLOW-CONTRACT.md](WORKFLOW-CONTRACT.md) and the
[workflow specification](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md).

## Example usage

> **Reference only — do not execute this example.**
>
> Using [initiative preparation](00_initiative_preparation.md), process the
> attached initiative's identified realization and record its target fit and
> execution placement.

Only the **Prepare initiative prompt** block below is executable when invoked.

## Prepare initiative prompt

```text
Apply {initiative_template_root}/prompts/WORKFLOW-CONTRACT.md and the canonical
prompt keyword specification at evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md.
Preserve source-position effective settings, locks, evidence and all unexcepted
gates. Use the adopted specification 09 revision, never inferred migration.

Process the identified realization {realization_note_path} for candidate
{initiative} in suite
{realization_suite_index_path}. Capture the actual human intake instruction,
its authority, source IDs and paths, source scope, governing revision and Git
baseline before applying any routing disposition. A note alone supplies no
intake authority. This delegation covers placement, coherent revision and
necessary initiative/scope reopening for this intake only; it does not accept
a claim, answer unrelated questions, authorize delivery or pass completion.

Perform the following actions serially:
1. Inspect Git, the recorded project integration configuration, staged,
   unstaged and untracked work, scope registry, initiative index, realization
   catalogs and existing open and closed initiatives. Include accepted claims,
   partial effort, dependencies, branches, conflicts and historical removals.
   Determine actual integration base from evidence; never assume main, master,
   a remote or a hosting service. Verify project adoption and migration records.
2. Assess every independent outcome and suitable target. Record candidate
   targets, rejected alternatives, fit rationale, source and selected target
   scopes separately, compatibility effects, risks and required reconciliation.
   Append unchanged-claim evidence/detail to an existing target; revise a
   coherent existing narrow outcome; split independently acceptable outcomes
   and incompatible type/owner/authority boundaries into separate initiatives
   or successors. A source note or suite may route to several targets, and
   several notes may contribute to one target. Every disposition is independent.
3. Before each existing-target change, record the actual LLM choice, author,
   method, source links, governing delegation, prior state and claim revision,
   change boundary and affected records in a decision receipt/routing record.
   Reopen Completed, Cancelled or Superseded targets before substantive edits
   and return them to Proposed; reconcile replacement ownership explicitly.
   Accepted/In progress changed claims pause delivery, preserve partial work
   and return to Proposed. Renew human acceptance before changed delivery.
   Direct closed-to-Accepted return requires a separate human unchanged-claim
   decision. A historical addendum preserving the exact claim is append-only.
   Record each necessary closed-scope/ancestor reopening; no silent reopening
   or reclosing. Preserve all prior claims, receipts and integration evidence.
4. Select execution placement for each new initiative or revision cycle using
   fit, dependencies, existing work and integration risk. Reuse an open matching
   scope and its declared shared integration branch, or select a dedicated child
   initiative/{version_scope}-{initiative_id_and_slug}. Inspect branch role and
   ownership before reuse; never convert an exclusive initiative branch into
   a shared container or reuse historical identity for unrelated work. Record
   one active assignment per initiative cycle and continuation history.
5. Preflight any branch creation with a clean worktree, readable templates,
   unique initiative ID/path, canonical scope syntax, reciprocal mappings,
   open parent and no conflicting branch role. Accept exact vN, vN.M, vN.M.P
   components without leading zeros; preserve v1, v1.0 and v1.0.0 identities.
   Numeric ordering never changes parentage. Prepare missing ancestors in
   major-to-minor-to-patch order with their own records. Capture actual base
   ref and immutable tip before creation: major from project integration base,
   minor directly from matching major, patch directly from matching minor,
   dedicated initiative directly from assigned scope. Existing parents are
   reused. A new minor never branches from an earlier minor. Detect cycles,
   orphans, wrong parents and undeclared branch sharing before writing.
6. For a new allocation only, prepare initiatives/{version_scope}/{initiative_type}/
   {initiative_id_and_slug}/ with README.md and proposal/README.md from the
   preparation templates. Type is implementation, design or planning. Preserve
   exact originating notes and suite catalog rather than relabeling sources;
   create a missing source catalog/note only when this intake includes that
   preparation authority, never fabricate provenance. Register the scope in
   initiatives/version-scopes.md, its navigation README and reciprocal member/
   child links. Register exactly one row per initiative in initiative-index.md
   with source notes/routing dispositions, type/path, scope, execution mode/
   branch, captured base ref/commit, target, cycle, relationships, lifecycle
   and integration evidence. Multiple initiatives may share scope/source/
   declared scope branch. Shared records preserve concurrent additions.
7. For existing targets, retain identity and scope, append source routing and
   revision/branch history, and reconcile assumptions, decisions, architecture,
   source mapping, scope assessment, dependencies, roadmap, steps, verification,
   compatibility, membership, status and work conflicts within authorized
   boundaries. No new-initiative skeleton may overwrite a complete record.
   Preserve unrelated and unaccepted work. Serialize shared writes and record
   initiative-specific paths, commits, revision bases and mixed-change limits.
8. Verify reciprocal scope/member/source mappings, active assignment, captured
   creation bases, exact parent topology and legal lifecycle evidence. Stop on
   missing authority, unresolved ambiguity or invariant conflict; preserve the
   blocker and continue independent authorized dispositions. Never infer or
   normalize a legacy identity to clear validation. Review and commit only
   traceable prepared/routing records, then record the actual commit when it
   exists; no empty commit and no remote operation.

For new targets create no proposal/proposal.md, full initiative suite,
implementation-readiness.md, execution-record.md, delivery-record.md,
completion-evidence.md, product or portfolio acceptance/completion claim.
Record the minimal preparation lifecycle as Proposed only. Existing-target
revision records are not new-initiative creation or delivery evidence.

Report each source-to-target disposition, rationale, exact source/target scopes,
initiative/type/path, execution mode/branch, captured base ref/commit, immediate
integration target, cycle, reciprocal records, reopened events, authority,
verification, commits and remaining blockers. New skeletons hand off to Stage 1;
existing complete targets hand off to alignment/decisions/renewed acceptance as
required by their recorded change boundary. No existing acceptance certifies
changed claims.
```