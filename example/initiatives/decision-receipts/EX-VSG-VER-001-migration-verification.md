# EX-VSG-VER-001: migration verification

**Authority:** [EX-VSG-DR-001](EX-VSG-DR-001-initiative-migration.md)

**Capture date:** 2026-11-12

**Migration baseline:** `9ab8c991222a026277a6f238bd0b64704b97f840`

## Baseline

The initial worktree was clean. `example/tools/tadp_protect.py check example`
passed with zero errors. `example/tools/tadp_validate.py example --json`
passed with zero errors and one TADP033 warning for the original unmigrated
broad realization. Commands used the configured `.venv/Scripts/python.exe`
and a per-process `safe.directory` setting for the enclosing worktree.

## Record migration and branch topology

Six complete initiative suites are grouped by their unchanged recorded source
scopes. The canonical scope registry has four major ancestors and six minor
scopes; membership has exactly six initiatives and six dedicated cycle 2
assignments. All remain Proposed. The six original exclusive branch refs and
their bases are retained. No branch was merged, deleted or rewritten.

| Ref set | Actual captured base/tip after preparation | Creation parent evidence |
|---|---|---|
| Existing `v1` | `7b9d302b3dc7a94627518e42819a3130b5ba17d3` | Reflog: created from `main^0` at `d39ea1545a74897e239fa5f0809363ac218596cf` |
| New `v2`, `v3`, `v4` | `36bb20c88802191e13b873a36a07531fcfab5f42` | Created from captured `main` |
| New `v1.0` | `7b9d302b3dc7a94627518e42819a3130b5ba17d3` | Created from `v1` |
| New `v2.0`, `v2.1`, `v2.2` | `36bb20c88802191e13b873a36a07531fcfab5f42` | Created from `v2`, independently |
| New `v3.0`, `v4.0` | `36bb20c88802191e13b873a36a07531fcfab5f42` | Created from `v3`, `v4` respectively |
| Six new `initiative/<scope>-<ID-and-slug>` continuations | Same initial tip as their matching minor scope above | Created from that exact scope, with no initiative work performed |

## Branch checkout availability and preparation recovery

**Preparation recovery disposition:** Blocked pending exact baseline installation authority

The migrated records reside on `migration/example-version-scopes`. The new
branch refs establish topology only. `git ls-tree -r --name-only main -- example`
returns only `example/TODO.md`: the new v2/v3/v4 descendants therefore lack
the installed scaffold and migrated suites. v1 descendants contain the prior
scaffold and ungrouped suites; they also lack this adopted migration. A check
of the new INIT-IMP-001 continuation's grouped path returns no files.

Before Stage 5, install or otherwise explicitly prepare the adopted scaffold
and exact suite on the actual assigned checkout, then rerun integrity,
membership/provenance, branch-base and link checks there. Do not treat the
passing validator on the migration branch as verification of those checkouts.
No delivery or human-review readiness is claimed.

Installing the pinned existing `example/template/**` and
`example/evidence/authoritative/LLM/**` baseline onto these refs would write
protected sources. Root `AGENTS.md` requires an explicit instruction naming
that change; the ordinary conformity request did not name it. No protected
file or lock was changed and no protected-update override was used. The
proposed recovery is to install the exact baseline from `9ab8c99`, retaining
its locks, and current migrated project records on the four major scopes,
then fast-forward still-empty minor/continuation refs to their prepared
parents. Main and historical initiative refs remain untouched; no closure
or delivery integration is inferred. This recovery is a proposal, not an
executed or approved disposition.

## Verification performed

Configured interpreter: `.venv/Scripts/python.exe` (Python 3.11.11), confirmed
through PyCharm's environment tool. Commands inherit a per-process Git
`safe.directory` for this worktree; no global Git configuration was changed.

| Command or review | Result |
|---|---|
| `example/tools/tadp_protect.py check example` | Passed, zero errors |
| `example/tools/tadp_validate.py example --json` | Passed, zero errors; one TADP049 warning for retained contextual RZN-001 / v0.0 |
| `example/tools/tadp_validate.py example --base-ref 9ab8c991222a026277a6f238bd0b64704b97f840` | Passed, zero errors and the same retained warning |
| `git diff --check` | Passed |
| Initial staged whitespace review | One inherited two-space Markdown line ending on the rebased INIT-IMP-001 proposal suite link was reported; trimmed that line ending, preserving its text and target |
| `-m unittest discover -s example/tests -v` | Passed: 138 tests in 107.154 seconds |
| Protected-source and protocol diff inventory | No changed paths under protocol, example/template or example/evidence/authoritative/LLM; no locks refreshed |
| Ref inventory, reflogs and checkout tree inspection | Correct recorded topology; operational baseline availability blocked as described above |
| Independent preservation review (`/root/review_preservation`) | Proposal text, assumptions, questions, architecture, scope, roadmaps and steps preserved apart from navigation; source notes receive append-only addenda |
| Independent semantic review (`/root/audit_migration`) | Exact scopes/provenance and prior claims preserved; stale profile/status installation language, old anchor and next-gate ordering identified and corrected; branch readiness limitation retained explicitly |

## Recorded delivery commits

- `9edc7f3`: authority and placement plan, committed before planned ref creation.
- `c3b9b13f48b850855ebefe567fa12123e7f4fd1a`: record migration, grouped suites,
  reciprocal membership/provenance, historical mappings and recovery blocker.

The migration commit ran `.githooks/pre-commit`: both project validators
reported zero errors and one retained legacy warning each; both protected
staged guards passed without overrides. The worktree was clean afterward.
`git diff --check 9ab8c99 HEAD` passed, and the same range contained no changed
protocol or example protected-source paths. This verification addendum records
those actual results without changing the branch readiness disposition.

These checks verify record structure and preservation;
they do not resolve initiative questions, accept work or qualify a merge.
