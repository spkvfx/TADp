# EX-GIT-DR-001 decision receipt

**Receipt ID:** `EX-GIT-DR-001`

**Initiative:** Example Record Application project-root governance, including
the current pre-allocation set `INIT-IMP-001` through `INIT-IMP-006`

**Source ID or lifecycle event:** `INV-CONFLICT-001` example-project invariant
exception

**Human authority:** User, recorded sole project owner, reviewer, approver, and
invariant-exception authority

**Response date or event:** 2026-11-11

**Capture context:** Codex chat following the read-only preflight that identified
the embedded-scaffold conflict and the explanation that a prompt edit alone
could not waive the invariant

**Disposition:** Accepted — treat `../..` as the TADp project root for the
entire installed example while using the enclosing repository or worktree only
for Git mechanics

**Git commit:** `553b1d386623908bdf244cc35c9bc2cea06985fd` — commit
containing this receipt, resolution, reconciled consumers, and protected lock

## Decision sequence

### Initial exact question

> Do you explicitly authorize those changes for only these six example
> initiatives using the enclosing repository’s Git worktree?

## Evidence and limitations presented

- **Authoritative evidence:**
  [`05_Codex_Git_Workflow_Specification.md`, Requirement](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement)
  requires every TADp project to be a Git repository root;
  [`01_Codex_Evidence_Authority_Specification.md`, Invariant contradictions](../../evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md#invariant-contradictions)
  permits resolution only through a lower-standing correction or explicitly
  authorized invariant revision or exception; and
  [`07_Codex_Human_Decision_Receipt_Specification.md`](../../evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md)
  requires a durable receipt.
- **Other evidence:** The
  [project-local prompt guard](../../prompts/AGENTS.md#resolve-the-current-scaffold-first)
  fixes `../..` as the scaffold boundary, and the
  [migration prompt](../../prompts/create-v1.0-through-v4.0-initiatives.md)
  names exactly six mappings and permits only Git metadata outside that
  directory.
- **Material limitations:** A project-local prompt is non-authoritative and
  could not create this exception by wording or invocation. No initiative,
  canonical row, or migration action existed when the decision was requested.
- **Initial affected scope described to the human:** Only work versions `v1.0`,
  `v2.0`, `v2.1`, `v2.2`, `v3.0`, and `v4.0`; initiatives `INIT-IMP-001` through
  `INIT-IMP-006`; their exact realization suites, paths, and branches in the
  migration prompt; and the enclosing worktree that directly contains the
  resolved `../..` scaffold.

## Exact human response

> ok. then yes. lets make it possible to make this exception

### Supplemental exact human directions

> I think for the example app, because it's an example, the correct approach
> would be to treat /example as root.
>
> But lets set this up as a conflict and resolution, just as we're doing here

> yes, but don;t limit it to just these files - basically we want to treat
> /example as if it were root

## Resulting scope and rationale

The combined decision authorizes a project-specific exception to the Git-root
invariant for the entire installed example. `../..` is the TADp project root
for every project file, evidence source, prompt, initiative, product, lifecycle
record, validation run, and scope decision. The directly enclosing repository
or worktree supplies Git metadata, captured base identity, branch refs,
staging, commits, history, and Git verification only. No non-Git project side
effect may escape `../..`.

The exception is not limited to the current six initiatives, their branches,
or the files reconciled by this decision. It does not make the parent or a
sibling part of the example project, alter the generic Git-root rule for the
enclosing TADp repository or another project, accept an initiative, resolve an
initiative assumption or question, migrate a legacy row, or establish product
conformance. Every governed action must still pass its own workflow and
authority gates.

## Current initiative consumers

The following mappings are the first planned consumers of the project-wide
resolution. They describe the migration prompt's authority, not the limit of
the example-root exception.

| Work version | Suite | Initiative | Dedicated branch |
|---|---|---|---|
| `v1.0` | `RZN-001-P1-DOCS-SUITE` | `INIT-IMP-001` | `initiative/v1.0-contract-documentation` |
| `v2.0` | `RZN-001-P2-PLATFORM-SUITE` | `INIT-IMP-002` | `initiative/v2.0-container-platform` |
| `v2.1` | `RZN-001-P2-API-SQLITE-SUITE` | `INIT-IMP-003` | `initiative/v2.1-api-sqlite-runtime` |
| `v2.2` | `RZN-001-P2-SDK-SUITE` | `INIT-IMP-004` | `initiative/v2.2-python-sdk` |
| `v3.0` | `RZN-001-P3-CLI-SUITE` | `INIT-IMP-005` | `initiative/v3.0-standalone-cli-image` |
| `v4.0` | `RZN-001-P4-WEB-SUITE` | `INIT-IMP-006` | `initiative/v4.0-web-application-bundle` |

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| [Invariant conflict register](../../evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md#inv-conflict-001--embedded-example-project-root-and-git-root-invariant) | Preserve the conflict and record the project-wide example exception | Protected-source check and lock review |
| [Project instructions](../../AGENTS.md#embedded-example-project-root) | Resolve `../..` as the project root for all work governed by the installed example | Instruction and path-boundary review |
| [Prompt instructions](../../prompts/AGENTS.md#resolve-the-current-scaffold-first) | Remain synchronized to the generic template; the installed exception is supplied by the project instructions and authoritative resolution before a prompt narrows scope | Template-sync and prompt-boundary review |
| [Project profile](../../project-profile.md#git-workflow) | Replace the open Git-root blocker with the project-wide exception and exact boundaries | Profile, receipt, and Git-root comparison |
| [Initiative index](../initiative-index.md#adoption-gate) | Permit governed allocation under the project-wide Git boundary while retaining every tuple gate | Canonical table remains empty before Stage 0 |
| [Status view](../status.md#portfolio-gates) | Resolve `EX-ADOPT-GIT-01` for the installed example project | Gate and receipt links agree |
| [Migration ledger](../version-correlation-migration-ledger.md#migration-ledger) | Remove the Git-root blocker from the six `Deferred` rows without allocating identity | Validator retains six actionable warnings |
| [Migration prompt](../../prompts/create-v1.0-through-v4.0-initiatives.md#example-project-root-resolution) | Cite and enforce the exception during every preflight and stage | Prompt scope and exact map review |

## Unresolved consequences and re-entry conditions

The six current tuples remain unallocated until their individual Stage 0
preparation commits. A new example work version, suite, initiative, branch, or
file does not require another Git-root exception, but it still requires its own
ordinary authority and workflow gates. The resolution must be reconciled if
the example moves to its own Git root, its containment relationship changes,
or work attempts to make a non-Git side effect outside `../..`.
