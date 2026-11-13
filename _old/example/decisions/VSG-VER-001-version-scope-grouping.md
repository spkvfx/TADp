# Version scope revision verification and distribution record

**Record ID:** VSG-VER-001

**Authority:** [VSG-DR-001](VSG-DR-001-version-scope-grouping.md)

**Baseline:** `dab30d02c6c15c2cf6219f3378c68877aff7d9b3`

**Maintenance branch:** `protocol/version-scope-grouping`

**Capture date:** 2026-11-12

## Implemented contract

One initiative belongs to exactly one immutable major/minor/patch scope;
several narrow initiatives may share a scope and exact source notes. Scope
registry and membership index have distinct canonical ownership. New paths are
`initiatives/<scope>/<type>/<id-and-slug>/`, retaining initiative-local records.
Realizations remain proposal input. Per-source routing preserves source and
target scope, suite/note IDs and paths, fit, actual delegated decision author,
alternatives and consequences. Append preserves the claim; coherent revision
may retain identity; independent outcomes or incompatible boundaries split.

An identified human realization-processing instruction under explicit adoption
delegates placement and necessary initiative/scope reopening, recorded before
use. Changed closed claims return to `Proposed`; changed accepted/in-progress
claims pause delivery and return to `Proposed`. Renewed acceptance remains a
human gate. Earlier claims, replacement consequences, assignment history,
completion feedback and actual integration evidence remain historical.

Execution placement is dedicated or directly on a matching shared scope branch,
with per-initiative attribution and serialized shared writes. Creation follows
captured project base -> major -> matching minor -> matching patch, with
dedicated initiative children from the assigned scope. `v2.0` and `v2.1` remain
siblings from `v2`; `v2.1.1` comes from `v2.1`. Exact identities never normalize.

Merge down is closed child into immediate recorded parent, bottom-up. A human
close/finalize instruction supplies that identified unit's bounded local merge
authority after gates pass. Direct scope hosting records verified presence
without self-merge. Member closure leaves its scope open; separate scope
closure requires complete closed inventories, child integration or authorized
dispositions, aggregate checks and conflict reconciliation. Unqualified shared
work blocks whole-tip integration. Integration pending/blocked is separate
from truthful lifecycle closure. No live merge is authorized by installation.
Pull requests are independently human managed; no PR service or URL is needed
for local finalization. Pushes, deletions and remote operations remain separate.

## Verification checkpoints

Commands use the configured Python 3.11.11 environment, package manager `pip`,
at `../../../.venv/Scripts/python.exe`. No packages were installed. Git commands in this
sandbox use per-process safe-directory configuration for this exact worktree;
no global trust setting is changed. `$PY` below denotes that configured
executable. Runs preserve failures and expected negative-case stderr.

| Checkpoint | Command or review | Observed result |
|---|---|---|
| Before edits | `$PY protocol/tools/tadp_protect.py check protocol` and `check example` | Both zero errors; no pre-existing protected drift |
| Protocol link check | `$PY -c` importing `tadp_validate.validate_links(Path('protocol').resolve())` | Zero Markdown link findings |
| First regression checkpoint | `$PY -m unittest discover -s protocol/tests -q` | 124 tests passed in 58.116 seconds; expected negative lock initialize/refresh stderr retained |
| Pre-refresh structural review | Full protocol validator JSON inspection | Initial missing Stage 0/13 invocation fields repaired; Git safe-directory path separator issue corrected. Subsequent inspection had no non-integrity errors, one Deferred legacy warning, and 58 expected authorized pre-refresh integrity findings |

Final verification, independent review disposition, lock/mirror results and
exact changed-path inventory are appended after those operations finish.

## Legacy and project adoption boundary

This maintenance installs reusable protocol sources and distribution mirrors.
The effective event is its coherent delivery commit; the actual ID is recorded
after creation. Protocol and example project allocation remain explicitly
`Installed; adoption pending` for the scope model. No existing initiative,
realization, branch or accepted claim is migrated or reopened.

The protocol's historical `INIT-DSN-001` remains `Superseded` at its old path
and under its predecessor ledger. The example's six `Proposed` implementation
initiatives retain their old `v1.0`, `v2.0`, `v2.1`, `v2.2`, `v3.0`, `v4.0`
tuples, source suites, branches, captured bases, paths and governing revision.
Its broad `v0.0` realization remains unmigrated. Existing example branches do
not have the new major/minor parent topology; adoption/migration needs explicit
evidence-backed mappings and authority for any move or reparenting. Never infer
that existing `v1` or any legacy minor already satisfies a new role.

Remaining human decisions concern future project adoption and any separately
scoped live migration/intake or closure. No new protocol acceptance, product
completion, live merge, push, branch removal, release or deployment is claimed.

## Protocol pass and independent review before synchronization

Independent agent `/root/independent_review` reviewed specifications, workflow,
provenance, migration, templates and tooling. Findings about numeric cycles,
source schemas, legacy reopening scope, source metadata/catalog/navigation,
current-cycle acceptance and integration evidence, and exact receipt fields
were reconciled. Final disposition: no blocking findings remain. Independent
`$PY -m unittest discover -s protocol/tests -p 'test_tadp_scope*.py'` passed
25 tests in 60.715 seconds. Producer's final 24-case scope suite passed in
46.991 seconds, including the last no-deliverable regression.

Root's expanded full suite passed 137 tests in 109.266 seconds before that
last additional case; root topology tests passed 2 tests in 14.523 seconds.
After substantive verification and review, `$PY protocol/tools/tadp_protect.py
refresh protocol --authority decisions/VSG-DR-001-version-scope-grouping.md`
refreshed only the authorized template and LLM locks. `check protocol` then
reported zero errors. Full protocol validation with `--base-ref
 dab30d02c6c15c2cf6219f3378c68877aff7d9b3` reported zero errors and one existing
Deferred legacy warning. This completed the protocol pass before any example
synchronization.

Machine limits: scope-table history compares current records with `HEAD`, not
every intermediate scope-table commit in a branch range. The coherence guard
retains its separate `--base-ref` history checks. Independent review must still
assess intermediate scope transitions, semantic fit, actual human authority,
complete aggregate inventories and verification quality. This revision changes
no live scope allocations or historical claims, so no intermediate allocation
transition is hidden by that limit. Structural passes are not human acceptance.

## Exact changed-path and mirror inventory

Paths below are relative to each project root. Each listed protocol path maps
to the same relative example path. Profile, index, status and migration ledger
receive project-specific installation addenda/dispositions; prior example rows
and evidence remain unchanged. All other non-lock mirrors are byte-identical.
Locks use the same authority; the LLM manifests retain their distinct unchanged
specification 03 conflict registers. No unexplained drift was refreshed.

| Relative path under protocol/ and example/ | Distribution handling |
|---|---|
| `../../../AGENTS.md` | Exact same-relative-path mirror |
| `decisions/VSG-DR-001-version-scope-grouping.md` | Exact same-relative-path mirror |
| `decisions/VSG-VER-001-version-scope-grouping.md` | Exact same-relative-path mirror |
| `docs/development/developing-tadp.md` | Exact same-relative-path mirror |
| `docs/development/getting-started.md` | Exact same-relative-path mirror |
| `docs/development/git-and-codex-requirements.md` | Exact same-relative-path mirror |
| `docs/development/initiative-workflow.md` | Exact same-relative-path mirror |
| `docs/development/repository-layout.md` | Exact same-relative-path mirror |
| `docs/development/validation-and-quality.md` | Exact same-relative-path mirror |
| `docs/guides/initiative-coherence-migration.md` | Exact same-relative-path mirror |
| `docs/guides/legacy-initiative-decomposition.md` | Exact same-relative-path mirror |
| `docs/guides/version-realization-correlation-migration.md` | Exact same-relative-path mirror |
| `docs/guides/version-scope-migration.md` | Exact same-relative-path mirror |
| `docs/README.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/.tadp-lock.json` | Authorized refresh; preserve local protected source identity |
| `evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md` | Exact same-relative-path mirror |
| `evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md` | Exact same-relative-path mirror |
| `evidence/non-authoritative/realizations/README.md` | Exact same-relative-path mirror |
| `initiatives/initiative-index.md` | Project-specific installation record; historical content preserved |
| `initiatives/README.md` | Exact same-relative-path mirror |
| `initiatives/status.md` | Project-specific installation record; historical content preserved |
| `initiatives/version-scope-migration-ledger.md` | Project-specific installation record; historical content preserved |
| `initiatives/version-scopes.md` | Exact same-relative-path mirror |
| `project-profile.md` | Project-specific installation record; historical content preserved |
| `../../../prompts/AGENTS.md` | Exact same-relative-path mirror |
| `prompts/README.md` | Exact same-relative-path mirror |
| `../../../README.md` | Exact same-relative-path mirror |
| `template/.tadp-lock.json` | Authorized refresh; preserve local protected source identity |
| `template/initiatives/completion-evidence.md` | Exact same-relative-path mirror |
| `template/initiatives/decision-receipts/decision-receipt.template.md` | Exact same-relative-path mirror |
| `template/initiatives/delivery-record.md` | Exact same-relative-path mirror |
| `template/initiatives/execution-record.md` | Exact same-relative-path mirror |
| `template/initiatives/implementation-readiness.md` | Exact same-relative-path mirror |
| `template/initiatives/implementation-roadmap.md` | Exact same-relative-path mirror |
| `template/initiatives/preparation-README.template.md` | Exact same-relative-path mirror |
| `template/initiatives/proposal/preparation-README.template.md` | Exact same-relative-path mirror |
| `template/initiatives/proposal/proposal.md` | Exact same-relative-path mirror |
| `template/initiatives/proposal/README.md` | Exact same-relative-path mirror |
| `template/initiatives/README.md` | Exact same-relative-path mirror |
| `template/initiatives/scope-assessment.md` | Exact same-relative-path mirror |
| `template/initiatives/source-mapping.md` | Exact same-relative-path mirror |
| `template/project/AGENTS.md` | Exact same-relative-path mirror |
| `template/project/evidence/non-authoritative/realizations/README.md` | Exact same-relative-path mirror |
| `template/project/evidence/non-authoritative/realizations/realization.template.md` | Exact same-relative-path mirror |
| `template/project/evidence/non-authoritative/realizations/realization-suite-index.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/initiative-index.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/integration-receipt.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/README.md` | Exact same-relative-path mirror |
| `template/project/initiatives/scope-README.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/status.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/version-correlation-migration-ledger.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/version-scope-migration-ledger.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/version-scopes.template.md` | Exact same-relative-path mirror |
| `template/project/initiatives/work-conflicts.template.md` | Exact same-relative-path mirror |
| `template/project/project-profile.template.md` | Exact same-relative-path mirror |
| `template/project/prompts/AGENTS.md` | Exact same-relative-path mirror |
| `template/project/prompts/README.md` | Exact same-relative-path mirror |
| `template/project/README.md` | Exact same-relative-path mirror |
| `template/prompts/00_initiative_preparation.md` | Exact same-relative-path mirror |
| `template/prompts/01_proposal_creation.md` | Exact same-relative-path mirror |
| `template/prompts/02_proposal_alignment.md` | Exact same-relative-path mirror |
| `template/prompts/03_initiative_creation.md` | Exact same-relative-path mirror |
| `template/prompts/04_initiative_alignment.md` | Exact same-relative-path mirror |
| `template/prompts/05_initiative_assumption_review.md` | Exact same-relative-path mirror |
| `template/prompts/06_initiative_open_question_review.md` | Exact same-relative-path mirror |
| `template/prompts/07_initiative_acceptance.md` | Exact same-relative-path mirror |
| `template/prompts/08_initiative_sdk_api_alignment.md` | Exact same-relative-path mirror |
| `template/prompts/09_initiative_implementation_readiness_review.md` | Exact same-relative-path mirror |
| `template/prompts/10_initiative_execution.md` | Exact same-relative-path mirror |
| `template/prompts/11_design_delivery.md` | Exact same-relative-path mirror |
| `template/prompts/12_planning_delivery.md` | Exact same-relative-path mirror |
| `template/prompts/13_initiative_finalization.md` | Exact same-relative-path mirror |
| `template/prompts/README.md` | Exact same-relative-path mirror |
| `template/prompts/scope_closure.md` | Exact same-relative-path mirror |
| `template/prompts/WORKFLOW-CONTRACT.md` | Exact same-relative-path mirror |
| `template/README.md` | Exact same-relative-path mirror |
| `tests/test_tadp_scope_topology.py` | Exact same-relative-path mirror |
| `tests/test_tadp_scopes.py` | Exact same-relative-path mirror |
| `tools/README.md` | Exact same-relative-path mirror |
| `tools/tadp_scopes.py` | Exact same-relative-path mirror |
| `tools/tadp_validate.py` | Exact same-relative-path mirror |

Intentionally unmirrored repository support: root `../../../AGENTS.md` and `../../../README.md`.
The human's pre-existing modified repository prompt remains unstaged and unchanged;
historical prompts and prior receipts are not revised. Total corresponding
protocol paths: 90.

## Final distribution verification

| Command/check | Observed result |
|---|---|
| `$PY -m unittest discover -s protocol/tests -q` | 138 tests passed in 121.426 seconds |
| `$PY -m unittest discover -s example/tests -q` | 138 tests passed in 121.184 seconds |
| `$PY protocol/tools/tadp_protect.py check protocol` | Zero errors after authorized refresh |
| `$PY example/tools/tadp_protect.py refresh example --authority decisions/VSG-DR-001-version-scope-grouping.md`, then `check example` | Both affected example locks refreshed coherently; zero protection errors |
| `$PY protocol/tools/tadp_validate.py protocol` | Zero errors, one retained Deferred legacy warning |
| `$PY example/tools/tadp_validate.py example` | Zero errors, one retained Unmigrated v0.0 warning |
| Both full validators with `--base-ref dab30d02c6c15c2cf6219f3378c68877aff7d9b3` | Zero errors, the same existing warning in each tree |
| `$PY -c` invoking `validate_links` for both roots | Zero Markdown link findings |
| SHA-256 comparison for all 84 direct-copy paths | Zero mismatches; independently repeated with the same result |
| `git -c core.safecrlf=false diff --check -- . ':(exclude)prompts/version-scope-grouping-and-branching-protocol-change.md'` | Passed; human's unrelated source edit excluded from authored-diff review |
| Focused Git preservation review | Zero changed live initiative, application architecture/security or realization-note paths; prior COH/KWD receipts preserved |

The two regression processes used isolated temporary repositories and ran
concurrently after synchronization. Expected negative-case lock-management
stderr is test evidence, not a failed suite. No network was used.

`core.hooksPath` was unset in this worktree; the maintenance commit invokes
`.githooks` explicitly through per-command Git configuration. The protected
update environment and both lock authorities use the exact VSG-DR-001 reference.
Staged guards and hook results are recorded with the delivery commit below.

Independent distribution review found no late blockers: 84 mirrors match,
profile/index/status changes are append-only installation records, existing
rows and claims remain intact, and the source prompt hash and unstaged status
are preserved. No new invariant/work conflict was discovered. Existing legacy
warnings and future migration needs remain visible rather than being waived.

## Verification-case reconciliation

Automated coverage is in `tests/test_tadp_scopes.py`,
`tests/test_tadp_scope_topology.py`, and the unchanged existing governance,
coherence, protection and keyword regressions. Semantic/procedural obligations
are reviewed by the independent agent; no test result authenticates human words
or proves completeness of a natural-language work inventory.

| Required case family | Evidence and limits |
|---|---|
| Two initiatives from one v1.0 note | Dedicated/shared fixture validates independent IDs, records and branches; ordinary acceptance checks remain independently active |
| Several sources, mixed types, v2.1 source into v1.0 target | Mixed-type/cross-scope append regression preserves source/target metadata and exact provenance |
| One realization to several existing/new targets | Multi-target fixture plus per-source fit/authority records and Stage 0 semantic review; no live routing performed |
| Coherent revision versus independent outcome split | Normative and workflow semantic review; acceptance is separately checked and never inferred by fit |
| Completed/Cancelled/Superseded reopening | Full adopted-project regressions preserve historical records, advance cycle, return to Proposed and reject implied Accepted |
| Direct shared-scope placement and member closure | Shared-placement and no-self-merge tests; member/scope lifecycle separation reviewed |
| Shared writes, unqualified work, reopened delta | Read-only reciprocal membership checks, qualified-change block and current-cycle receipt tests; operational serialized writes/latest-index preservation reviewed; no general concurrent index writer is supplied |
| Exact scope syntax and numeric ordering | Accepted/rejected syntax and arity-preserving numeric ordering tests |
| Major/minor/patch creation topology | Real Git topology fixture covers v1.0/v1.1 and v2.0/v2.1 sibling minors and matching patches |
| Wrong parents/cycles/orphans/duplicates/roles/mappings | Negative topology, unique identity, role and reciprocal inventory checks |
| Member versus scope closure and reopening | Open-member, pending-integration and closed-scope history gates; complete scope closure inventory/aggregate quality reviewed semantically |
| Bottom-up integration and no-deliverable dispositions | Recorded-parent helper tests, actual merge conflict, exclusion/no-deliverable contracts and child-integration checks; no live upward merge |
| Reruns, drift, shared index and fast-forwards | Real fast-forward/already-integrated, target-tip and callback-drift tests; append-only/shared-index preservation contract reviewed |
| Bounded authority and no remote permission | Missing authority/arbitrary target tests; helper contains no remote operations; semantic authority authenticity remains reviewed |
| Human-managed PRs | Independent operational prompt/contract review confirms no PR action, URL requirement or hosting dependency; no hosting command invoked |
| Legacy, protection, standing, acceptance and coherence | Full old/new regression suites, protection and both validators, preserved historical diffs and unchanged directive registry |

**Delivery recording status:** Verified, ready for traceable maintenance commit.
The exact effective commit and staged guard/hook result are recorded afterward;
no future commit identifier is guessed here.

## Recorded effective delivery

**Recording and effective delivery commit:** `873021eef226576aebfc60b94f69886eb4da4a1c`

The coherent 182-path revision committed successfully with explicit per-command
`core.hooksPath=.githooks`. Both project validators reported zero errors and
one retained legacy warning each; both staged protected-source guards passed
under the exact VSG-DR-001 authority. The original modified source prompt was
not staged. Project scope adoption/migration remains pending as recorded; the
commit installs protocol capability and grants no live merge authority.
