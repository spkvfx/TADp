# EX-VSG-DR-001: migrate the six example initiatives

**Receipt ID:** `EX-VSG-DR-001`

**Source ID or lifecycle event:** Explicit project version-scope adoption and legacy migration

**Human authority:** User, sole project owner

**Decision author:** Codex

**Response date or event:** 2026-11-12, current Codex conversation

**Disposition:** Adopt and migrate the six identified Proposed initiatives

## Exact human instruction and target

> conform initiatives to the protocol branching and grouping policy

The instruction identifies `example/initiatives/` and
`prompts/version-scope-grouping-and-branching-protocol-change.md`.
The latter identifies the policy; it is not being re-executed as protocol
maintenance. Its requirement inventories and examples are inert.

## Governing evidence and bounded interpretation

Adopt the installed specification 09 revision at
`873021eef226576aebfc60b94f69886eb4da4a1c`, with project migration baseline
`9ab8c991222a026277a6f238bd0b64704b97f840`. Specifications
[05](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md),
[09](../../evidence/authoritative/LLM/09_Codex_Version_Realization_Initiative_Correlation_Specification.md)
and [11](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
govern. The existing [Git-root exception](EX-GIT-DR-001-enclosing-worktree-exception.md)
continues to apply.

The User authorizes conformity of these existing records. Codex selects the
following evidence-backed migration; this is not a human answer to any
initiative assumption, question, acceptance or completion gate. Exact source
suite headers establish the six separate minor scope identities. Product 2
lineage does not make `v2.0`, `v2.1` and `v2.2` interchangeable.

## Recorded placement plan, before ref creation

The initial worktree was clean on `protocol/version-scope-grouping` at the
migration baseline. A separate maintenance branch,
`migration/example-version-scopes`, preserves that baseline and serializes
shared writes. Only example project records and enclosing Git metadata are
within the migration edit boundary.

| Initiative | Scope | New directory under initiatives | Historical branch | Continuation branch |
|---|---|---|---|---|
| INIT-IMP-001 | v1.0 | `v1.0/implementation/INIT-IMP-001-contract-documentation` | `initiative/v1.0-contract-documentation` | `initiative/v1.0-INIT-IMP-001-contract-documentation` |
| INIT-IMP-002 | v2.0 | `v2.0/implementation/INIT-IMP-002-container-platform` | `initiative/v2.0-container-platform` | `initiative/v2.0-INIT-IMP-002-container-platform` |
| INIT-IMP-003 | v2.1 | `v2.1/implementation/INIT-IMP-003-api-sqlite-runtime` | `initiative/v2.1-api-sqlite-runtime` | `initiative/v2.1-INIT-IMP-003-api-sqlite-runtime` |
| INIT-IMP-004 | v2.2 | `v2.2/implementation/INIT-IMP-004-python-sdk` | `initiative/v2.2-python-sdk` | `initiative/v2.2-INIT-IMP-004-python-sdk` |
| INIT-IMP-005 | v3.0 | `v3.0/implementation/INIT-IMP-005-standalone-cli-image` | `initiative/v3.0-standalone-cli-image` | `initiative/v3.0-INIT-IMP-005-standalone-cli-image` |
| INIT-IMP-006 | v4.0 | `v4.0/implementation/INIT-IMP-006-web-application-bundle` | `initiative/v4.0-web-application-bundle` | `initiative/v4.0-INIT-IMP-006-web-application-bundle` |

Discover and record `main` as the project integration base for this adoption.
The previous project default `v1` cannot also be its own major scope parent.
Git reflog establishes that existing `v1` was created from `main^0` at
`d39ea1545a74897e239fa5f0809363ac218596cf`; adopt that actual history without
reparenting. Its pre-migration tip is
`7b9d302b3dc7a94627518e42819a3130b5ba17d3`. Capture `main` at
`36bb20c88802191e13b873a36a07531fcfab5f42` for new major siblings `v2`, `v3`
and `v4`. Do not switch or update `main`, which is used by another worktree.

Prepare missing ancestors before children: `v1.0` from existing `v1`;
`v2.0`, `v2.1`, `v2.2` from new `v2`; `v3.0` from new `v3`; `v4.0` from new
`v4`. Prepare each dedicated continuation from its matching minor. Existing
exclusive refs remain immutable history, not shared scope branches. The six
historical assignments all retain `v1` at
`5a0ea0bd9f51edf97f9eddd39c6a3509c271503b`. The new assignments are migration
cycle 2, with the prior cycle preserved in the historical index and ledger.
Dedicated placement avoids mixing independently gated delivery on one branch.

## Reconciliation and limits

Move complete suites, preserve proposal/source contents and all lifecycle
history, rebase relative navigation, retain old-path redirect mappings, append
source addenda rather than rewrite original notes, and reconcile profile,
scope/membership/status views and both migration ledgers. No initiative changes
its intended outcome, type, ID, owner, unresolved decisions or Proposed state.
No reopening is needed. New administrative preparation is not Stage 5 review.

Branch creation captures topology, not delivery readiness. The new refs start
at their actual historical parents. Before using a continuation, verify that
its checkout contains the adopted scaffold and the exact migrated suite;
missing baseline material requires explicit preparation recovery, never a
fabricated ready handoff or an implicit merge. Record actual availability in
the migration verification record.

The legacy `v1` tip contains all six Proposed suites through earlier merges.
Those merges are historical Git facts, not accepted delivery. Whole-tip
integration remains blocked until every included change qualifies or has an
authorized exclusion/transfer. Adoption closes no scope. No merge, push,
branch deletion, history rewrite, product delivery, protected-source revision
or lock refresh is authorized by this migration.

## Effective-settings ledger

Source: current human instruction above; block/resume identity `EX-VSG-001`.
Settings are `human_gates=true`, `other_gates=true`, `preview=false`,
`local=false`, `review=false`. No operative directive occurs. Scheduling is
agent discretion outside an action list; independent read-only auditing runs
in parallel, and shared mutations run serially. Authority is this exact
bounded migration instruction; no exception is inferred. Targets are the six
suites and their necessarily affected project records and Git assignments.

## Verification and re-entry

Baseline: protected-source check passed with zero errors; example validator
passed with zero errors and one retained broad-source legacy warning.
Final commands, actual refs, results and any remaining branch preparation
limits are recorded in [migration verification](EX-VSG-VER-001-migration-verification.md).
The commit containing this receipt is discoverable through Git history.
