# Create the v1.0 through v4.0 example initiatives

Resolve the current scaffold from this prompt's governing
[`AGENTS.md`](AGENTS.md). Work in the active repository or worktree that
directly contains that resolved `example/` scaffold. The target project is
`example/`; repository Git metadata is the only permitted target outside that
directory.

Create and align the proposed example-application initiatives associated with
the existing realization suites from `v1.0` through `v4.0`. In this prompt,
that range includes every existing dot version in the interval: `v1.0`,
`v2.0`, `v2.1`, `v2.2`, `v3.0`, and `v4.0`.

Use the following protected reusable prompts, in order, for each initiative:

0. [`00_initiative_preparation.md`](../template/prompts/00_initiative_preparation.md)
1. [`01_proposal_creation.md`](../template/prompts/01_proposal_creation.md)
2. [`02_proposal_alignment.md`](../template/prompts/02_proposal_alignment.md)
3. [`03_initiative_creation.md`](../template/prompts/03_initiative_creation.md)
4. [`04_initiative_alignment.md`](../template/prompts/04_initiative_alignment.md)

Apply
[`WORKFLOW-CONTRACT.md`](../template/prompts/WORKFLOW-CONTRACT.md) with every
stage. Read the templates as instructions; do not edit or fill any file under
`example/template/`.

## Example project-root resolution

The authoritative
[`INV-CONFLICT-001`](../evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant)
resolution and
[`EX-GIT-DR-001`](../initiatives/decision-receipts/EX-GIT-DR-001-enclosing-worktree-exception.md)
authorize a project-specific exception to the Git-root requirement for the
entire installed `example/` project. This prompt consumes that established
resolution for its six mappings; it does not define or limit the resolution.

For all work governed by the installed example, including these mappings:

- use the enclosing repository or worktree that directly contains `example/`
  only for source-base capture, local branch refs, staging, commits, history,
  and read-only Git verification;
- treat the resolved `example/` directory as the TADp project root and maximum
  project file boundary;
- permit only repository Git metadata to change outside `example/`;
- stage only initiative-traceable paths under `example/` on every mapped
  branch; and
- preserve the generic Git-root rule for the enclosing TADp repository, every
  sibling or parent scope, and every other scaffold or project.

Before consuming the exception, verify that the conflict resolution, receipt,
project instructions, synchronized generic prompt instructions, project
profile, status gate, migration ledger, and refreshed example invariant lock
agree. Verify that
`git rev-parse --show-toplevel` identifies the one enclosing worktree that
directly contains the resolved `example/` path and that its repository-root
`AGENTS.md` exists. Stop on any mismatch. This exception changes no lifecycle
state and does not relax any branch, clean-worktree, captured-base, commit,
scope, evidence, or verification rule.

## Explicit execution authority and limits

Execution of this prompt is the human instruction to begin the governed
proposal and initiative workflow for exactly the six mappings below. It
authorizes:

- preserving each named pre-effective work version and realization-suite
  identity;
- pairing that suite with the named new self-contained implementation
  initiative and dedicated branch;
- recording the corresponding `Migrate` disposition and canonical correlation
  row; and
- completing workflow stages 0 through 4 while every initiative remains
  `Proposed`.

The mapping is intended to preserve, not change, the one-future-initiative
boundary already recorded by each suite. If repository evidence shows that a
mapping changes meaning, combines outcomes, or triggers a split, stop that
mapping. Record the exact ambiguity and obtain the required human decision and
receipt instead of applying it.

This prompt does **not** authorize:

- an invariant or reusable-template change;
- editing `protocol/**`, `example/template/**`, or
  `example/evidence/authoritative/**`;
- rewriting an existing realization note or making it authoritative;
- resolving an assumption or open question;
- accepting, implementing, completing, releasing, or deploying an initiative
  or product;
- creating a seventh initiative or allocating another work version;
- merging, rebasing, force-pushing, deleting a branch, pushing a branch, or
  opening a pull request; or
- changing another initiative to make one of these initiatives appear aligned.

Do not execute the repository-level
[`version-realization-initiative-correlation-protocol-change.md`](../../prompts/version-realization-initiative-correlation-protocol-change.md)
from this prompt. It is historical authority for the protocol revision, not
an instruction to repeat that protocol work.

## Exact initiative map

All six initiatives are root initiatives of type `implementation`. A
dependency between delivery units is not a predecessor/successor identity
relationship. Record `None` for predecessor or successor unless authoritative
evidence establishes an actual replacement of the same bounded claim.

| Order | Work version | Realization suite | Intended note | Initiative ID | Initiative name and slug | Initiative path | Dedicated branch | Decision prefix |
|---:|---|---|---|---|---|---|---|---|
| 1 | `v1.0` | `RZN-001-P1-DOCS-SUITE` at `evidence/non-authoritative/realizations/v1.0/00-RZN-001-P1-DOCS-suite-index.md` | `evidence/non-authoritative/realizations/v1.0/01-RZN-001-P1-DOCS-contract-documentation.md` | `INIT-IMP-001` | Contract documentation / `contract-documentation` | `initiatives/implementation/INIT-IMP-001-contract-documentation` | `initiative/v1.0-contract-documentation` | `DOC` |
| 2 | `v2.0` | `RZN-001-P2-PLATFORM-SUITE` at `evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md` | `evidence/non-authoritative/realizations/v2.0/01-RZN-001-P2-PLATFORM-v2.0-container-platform.md` | `INIT-IMP-002` | Container platform and runtime packaging / `container-platform` | `initiatives/implementation/INIT-IMP-002-container-platform` | `initiative/v2.0-container-platform` | `PLT` |
| 3 | `v2.1` | `RZN-001-P2-API-SQLITE-SUITE` at `evidence/non-authoritative/realizations/v2.1/00-RZN-001-P2-API-SQLITE-suite-index.md` | `evidence/non-authoritative/realizations/v2.1/01-RZN-001-P2-API-SQLITE-v2.1-api-runtime.md` | `INIT-IMP-003` | API and SQLite runtime image / `api-sqlite-runtime` | `initiatives/implementation/INIT-IMP-003-api-sqlite-runtime` | `initiative/v2.1-api-sqlite-runtime` | `API` |
| 4 | `v2.2` | `RZN-001-P2-SDK-SUITE` at `evidence/non-authoritative/realizations/v2.2/00-RZN-001-P2-SDK-suite-index.md` | `evidence/non-authoritative/realizations/v2.2/01-RZN-001-P2-SDK-v2.2-python-sdk.md` | `INIT-IMP-004` | Python SDK artifact / `python-sdk` | `initiatives/implementation/INIT-IMP-004-python-sdk` | `initiative/v2.2-python-sdk` | `SDK` |
| 5 | `v3.0` | `RZN-001-P3-CLI-SUITE` at `evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md` | `evidence/non-authoritative/realizations/v3.0/01-RZN-001-P3-CLI-command-image.md` | `INIT-IMP-005` | Standalone CLI image / `standalone-cli-image` | `initiatives/implementation/INIT-IMP-005-standalone-cli-image` | `initiative/v3.0-standalone-cli-image` | `CLI` |
| 6 | `v4.0` | `RZN-001-P4-WEB-SUITE` at `evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md` | `evidence/non-authoritative/realizations/v4.0/01-RZN-001-P4-WEB-browser-bundle.md` | `INIT-IMP-006` | Web application bundle / `web-application-bundle` | `initiatives/implementation/INIT-IMP-006-web-application-bundle` | `initiative/v4.0-web-application-bundle` | `WEB` |

Resolve every path in the table relative to `example/`. Do not reinterpret
`v2.0`, `v2.1`, and `v2.2` as one umbrella version or initiative.

## Required project records

Use these project-local paths:

- template root: `example/template` when working from the repository root, or
  `template` when working from `example/`;
- project profile: `example/project-profile.md`;
- canonical initiative and correlation register:
  `example/initiatives/initiative-index.md`;
- portfolio status: `example/initiatives/status.md`;
- version-correlation migration ledger:
  `example/initiatives/version-correlation-migration-ledger.md`; and
- initiative registry root: `example/initiatives`.

Before allocating any tuple, verify that these project records already exist,
are complete, and record the correlation revision's actual effective commit,
the project's human ownership and approval convention, branch convention, and
migration-ledger location. Also verify that the synchronized example template
set contains the effective versions of prompts 00 through 04 and the workflow
contract.

If project adoption is incomplete, the effective commit is missing, the
example mirror is stale, or the applicable Stage 0 procedure has no governed
way to migrate an existing pre-effective suite, stop before branch creation.
Report the exact missing adoption or migration support. Do not invent project
owners, fill governance records with placeholders, alter protected sources,
or run the new-allocation path against an existing suite merely to proceed.

## Global preflight

Read and apply, in precedence order:

1. the repository and `example/` `AGENTS.md` files;
2. `EX-GIT-DR-001`, resolved `INV-CONFLICT-001`,
   `example/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md`, and
   every applicable specification, including the effective correlation and
   workflow specifications;
3. the example architecture and security suite indexes and the precise
   authoritative records cited by each realization suite;
4. the six suite indexes and their intended realization notes; and
5. prompts 00 through 04 and their shared workflow contract.

Then perform a read-only inventory and verify that:

- the protocol correlation revision is complete, committed, synchronized to
  `example/`, and adopted by the example project;
- the project-wide example-root resolution is authoritative, locked, and
  consistent across every named consumer, and this prompt independently limits
  execution authority to the six exact mappings;
- the enclosing Git worktree directly contains the resolved `example/`
  scaffold without expanding its project file boundary;
- the Git worktree is clean, including untracked paths;
- the current checked-out branch and commit are captured as the source base;
- all six versions, suites, notes, initiative IDs, paths, and branch names are
  unique and match the table;
- no initiative, canonical row, migration action, local branch, or retained
  historical identity already owns one of the proposed mappings;
- every legacy suite explicitly describes the same single boundary represented
  by its mapped initiative;
- the initiative and proposal preparation templates and all Stage 3 document
  templates exist; and
- no partial prior attempt or correlation drift exists.

An existing truthful partial attempt is recovery work, not permission to
overwrite or duplicate it. Stop the affected tuple and report its owning stage
and exact recovery evidence. Continue with another tuple only when its work is
independent and returning to the captured source branch cannot alter or hide
the blocker.

## Branch and stage orchestration

Process the tuples in table order. Use one dedicated branch per tuple. Before
each Stage 0 run, return to the originally captured source branch and verify
that it is still at the captured source commit and that the worktree is clean.
Do not merge one initiative branch into another or silently change the common
base.

For each tuple:

1. Apply prompt 00 as the Stage 0 contract for branch creation, captured-base
   identity, canonical correlation, reciprocal metadata, minimal skeleton,
   verification, and reporting. Because the suite and note are pre-effective
   records, use the protocol's recorded migration-ledger path rather than the
   new-suite allocation path. Preserve the existing suite ID, version, path,
   note, evidence standing, and original recorded claims. Do not duplicate or
   overwrite them. Any reciprocal migration metadata must be recorded through
   the current protocol-defined migration or addendum mechanism with its
   effective date and authority; it must not rewrite history to imply that the
   correlation always existed.
2. On the resulting dedicated branch, apply prompt 01 to create only the
   canonical working proposal from the mapped suite index and intended note.
3. Apply prompt 02 to align only that proposal to authoritative evidence and
   established precedent. Preserve every unresolved choice.
4. Apply prompt 03 with the table's initiative ID, name, path, and decision
   prefix to create the complete initial initiative suite and required
   tracking entries. Keep the lifecycle state `Proposed`.
5. Apply prompt 04 to align the complete initiative as one coupled proposed
   specification. Re-run every mandatory split trigger. Do not confirm an
   assumption, answer a question, or accept the initiative.

Use the mapped realization note as proposal input, never as specification
authority. Derive dependencies, gates, exclusions, owners, product
destinations, compatibility obligations, and verification from the precise
authoritative evidence. Do not treat work-version order as proof that a
dependency is satisfied. Keep D1 through D6 as separate acceptance and
completion claims.

After each stage, verify its exact edit boundary and handoff before proceeding.
Commit only the current stage's initiative-traceable changes with a clear
message containing the initiative ID and stage. Do not create an empty commit.
Stage 0's preparation commit and every later commit must remain on the mapped
initiative branch. Finish each branch with a clean worktree before returning
to the captured source branch for the next tuple.

Read committed records on earlier initiative branches when they provide
relevant cross-initiative context, but preserve their standing and do not edit
or cherry-pick them. Report any coordinated correction that another branch
would require.

## Verification

For every initiative branch:

- verify the exact work version, suite ID and path, initiative ID and path,
  dedicated branch, base branch, and base commit;
- verify the canonical row, migration disposition, reciprocal links, and
  lifecycle evidence agree without promoting the realization suite;
- verify the complete Stage 3 artifact set exists and contains no unresolved
  template tokens or instructional comments;
- verify the proposal and full initiative remain type-correct, narrow,
  internally coherent, mutually coherent with available sibling evidence, and
  aligned with authoritative architecture and security records;
- verify every assumption and question still has a truthful unresolved or
  explicitly human-dispositioned state;
- verify the initiative and status records say `Proposed` and make no
  acceptance, implementation, completion, conformance, release, or deployment
  claim;
- run the repository-defined protected-source check, validator, link or
  structure checks, and applicable unit tests using the configured project
  environment; and
- verify the branch diff contains no protected-source or unrelated change.

Run a final read-only cross-branch audit for duplicate versions, suites,
initiative IDs, paths, or branch names. Do not merge branches to perform that
audit.

## Completion report

Report one row per mapped version containing:

- stage reached and whether stages 0 through 4 completed;
- suite, initiative, branch, captured base, canonical row, and migration-ledger
  location;
- commits created and exact changed paths;
- validation and test results;
- remaining assumptions, open questions, conflicts, split findings, or other
  blockers; and
- the next permitted prompt, which may be stage 5 only when Stage 4 completed
  without a blocking conflict or decomposition requirement.

Also report any tuple not created and why. Do not summarize a blocked or
partial tuple as created, aligned, accepted, implemented, or complete.
