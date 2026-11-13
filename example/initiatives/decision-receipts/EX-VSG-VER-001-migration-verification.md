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

## Assumption and question review preflight: 2026-11-12

**Run ID:** `EX-AQ-PREFLIGHT-001`

**Actual author:** Codex (`/root`), with independent read-only preparation
audit by `/root/preparation_audit` and source inventory by
`/root/coverage_discovery`.

**Result:** Blocked before templates 05/06; no autonomous source disposition
or next-stage readiness established.

### Invocation and execution baseline

The User instructed `execute the attached prompt` and attached
[`answer-assumptions-and-open-questions.md`](../../prompts/answer-assumptions-and-open-questions.md)
twice, identifying the same source rather than two review runs. Its last
changing commit is `8f2100579ca971904af3a4a16c8b4e8d44293d72`; its captured
file SHA-256 is
`b0ab685d90fb4385e9139b164d216093b250e988a3ad0dfd2cda8003fd4f59a0`.
The enclosing worktree is
`C:/Users/User/AppData/Local/JetBrains/PyCharm2026.2/aia/agents/views/codex/TADp-rzn-product-initiatives`,
on `v1` at `c592920f0b0e2114c4305464fb29605400486b2e`. Initial staged,
unstaged and untracked inventories were empty. The resolved project root is
its direct `example/` child; all required scaffold markers and the two
tracking paths changed by this preflight are contained there, without
symlink/junction indirection. [EX-GIT-DR-001](EX-GIT-DR-001-enclosing-worktree-exception.md)
covers the enclosing Git relationship, not review-branch preparation.

The operative block following the source's opening robotic directive requests
`human_gates=false`, `other_gates=true`, `preview=false`, `local=false`,
`review=false`; the final inverse restores human gates. Its explicit distinct
review requirement remains applicable. Numbered phases 1 through 5 and D1
through D6 are serial. Phase 1 verification found the failures below; only
independent read-only discovery and this required blocker capture continued.
No template was invoked, no per-item human gate was bypassed, and no phase 2
delegation/exception record was adopted or relied upon. Resume identity is
this run ID and captured source revision; recheck prerequisites before phase 2
and persist its complete authority records before any autonomous decision.

### Observed unexcepted blockers

[Canonical membership](../initiative-index.md#initiative-and-correlation-register)
still assigns dedicated cycle 2 execution, whereas the actual checkout is
`v1`. Read-only `git rev-parse` and `git ls-tree -r --name-only` found:

| Unit | Recorded execution branch | Observed tip | Files under example | Files in its canonical grouped initiative suite |
|---|---|---|---:|---:|
| D1 | `initiative/v1.0-INIT-IMP-001-contract-documentation` | `7b9d302b3dc7a94627518e42819a3130b5ba17d3` | 229 | 0 |
| D2 | `initiative/v2.0-INIT-IMP-002-container-platform` | `36bb20c88802191e13b873a36a07531fcfab5f42` | 1 | 0 |
| D3 | `initiative/v2.1-INIT-IMP-003-api-sqlite-runtime` | `36bb20c88802191e13b873a36a07531fcfab5f42` | 1 | 0 |
| D4 | `initiative/v2.2-INIT-IMP-004-python-sdk` | `36bb20c88802191e13b873a36a07531fcfab5f42` | 1 | 0 |
| D5 | `initiative/v3.0-INIT-IMP-005-standalone-cli-image` | `36bb20c88802191e13b873a36a07531fcfab5f42` | 1 | 0 |
| D6 | `initiative/v4.0-INIT-IMP-006-web-application-bundle` | `36bb20c88802191e13b873a36a07531fcfab5f42` | 1 | 0 |

D1 also lacks the current keyword specification; D2 through D6 contain only
`example/TODO.md`. No assigned continuation is checked out in another worktree.
These observations confirm the existing preparation blocker above rather
than authorize an assignment repair or use of an obsolete branch.

The full validator additionally reports pre-existing `TADP048` at
[`project-profile.md`](../../project-profile.md#version-scope-installation):
`effective point is not in current history`. The recorded effective point
`873021eef226576aebfc60b94f69886eb4da4a1c` is not an ancestor of the captured
HEAD (`git merge-base --is-ancestor` exit 1). Its identity was preserved.

Controlling requirements are the invoked prompt's execution sequence 2
(valid prepared checkout; no later-stage preparation repair), specification
[05, Version-scope hierarchy and execution placement](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#version-scope-hierarchy-and-execution-placement),
and the [shared contract's recovery rules](../../template/prompts/WORKFLOW-CONTRACT.md#scope-and-correlation-recovery).
The per-item autonomous delegation excepts none of these requirements.

### Discovery coverage and unchanged source outcomes

This is a source-ID discovery baseline, not completed decision review or a
complete phase 2 evidence inventory. Source text remains in each canonical
`assumption.md` and `open-questions.md` linked by the membership record.

| Initiative | Unique unresolved assumption IDs | Unique unresolved question IDs | Confirmed / Corrected / Not applicable this run | Answered this run | Handoff |
|---|---|---|---|---:|---|
| INIT-IMP-001 | DOC-A01 through DOC-A06 (6) | DOC-01 through DOC-06 (6) | 0 / 0 / 0 | 0 | Blocked before 05 |
| INIT-IMP-002 | PLT-A01 through PLT-A06 (6) | PLT-01 through PLT-06 (6) | 0 / 0 / 0 | 0 | Not started; serial dependency and preparation blocked |
| INIT-IMP-003 | API-A01 through API-A06 (6) | API-01 through API-06 (6) | 0 / 0 / 0 | 0 | Not started; serial dependency and preparation blocked |
| INIT-IMP-004 | SDK-A01 through SDK-A06 (6) | SDK-01 through SDK-06 (6) | 0 / 0 / 0 | 0 | Not started; serial dependency and preparation blocked |
| INIT-IMP-005 | CLI-A01 through CLI-A06 (6) | CLI-01 through CLI-06 (6) | 0 / 0 / 0 | 0 | Not started; serial dependency and preparation blocked |
| INIT-IMP-006 | WEB-A01 through WEB-A06 (6) | WEB-01 through WEB-07 (7) | 0 / 0 / 0 | 0 | Not started; serial dependency and preparation blocked |

All 36 assumptions remain `Assumed aligned`. DOC-01 through DOC-03 and
PLT-01 through PLT-03 remain `Open, blocking`; the other 31 questions remain
`Open`. Repeated table/detail representations count once. No additional
continuation or Deferred source ID was found. Historical RZN-001-Q01 through
RZN-001-Q17 have accepted dispositions in
[ARC-AUT-001](../../evidence/authoritative/architecture/02-authority-and-source-disposition.md)
and remain excluded without reopening. All six initiatives remain `Proposed`;
no proposed acceptance baseline or D1-D6 design handoff is qualified.

### Checks, remaining work and recovery ownership

- Protected-source check on the current `example/`: passed, zero errors.
- Initial validator attempt: 18 Git-verification errors caused by Windows
  safe-directory path spelling, plus one retained warning. Repeated with the
  exact forward-slash worktree path in process-only Git configuration:
  one `TADP048` error above and one retained `TADP049` legacy RZN-001/v0.0
  warning. No global configuration or validator was changed. The retry does
  not erase the failed attempt.
- Independent preparation and inventory audits confirmed the branch mismatch,
  missing assigned-checkout contents and 36/37 unresolved source counts.
- Independent review of the actual two-file diff by `/root/preparation_audit`:
  passed with no corrective findings. The reviewer verified source revision
  and hash, branch contents, failed effective-point ancestry, unique source
  counts, tracking-only authority, preserved history and statuses, serial
  non-execution, and recovery ownership. This reviews the blocked preflight
  output only; the required review of completed source decisions remains
  unperformed because those decisions could not begin.
- Post-addendum full validation/local-link check: the same one pre-existing
  `TADP048` error and one `TADP049` warning, with no local-link findings.
  Protection and `git diff --check` passed; the final path inventory contained
  only the two intended tracking files, with an empty index and unchanged HEAD.
- No regression suite or future product tests were run for this blocked
  preflight; no template execution, whole-app decision coherence or acceptance
  readiness verification is claimed.
- No invariant or incompatible product-work claim was changed or approved.
  This is preparation recovery, not a resolved work/invariant conflict.

**Recovery owner:** User-authorized Stage 0/preparation and adoption recovery,
not stages 5 or 6. Obtain separately scoped explicit authority to install the
exact adopted protected baseline and current migrated records on the recorded
scope/continuation checkouts and reconcile the effective-point ancestry failure
with actual Git evidence. Preserve locked content, creation bases, assignments,
historical branches and main; do not substitute a convenient effective point.
The earlier `9ab8c99` installation proposal above remains historical and
unapproved, not a newly verified current installation plan.

**Re-entry:** Verify a coherent adopted baseline in history, intact protection,
reciprocal membership/provenance and a complete current suite on each actual
assigned checkout. Rerun validation and local links there, then capture the
run's bounded authority and enumerate the complete current sources before
executing 05/06 in D1-D6 order. The existing autonomous decision authority
requires no repeated per-item human approval within that run's exact scope.

**Git disposition:** Only this existing verification record and the project
status addendum are updated. They remain unstaged and uncommitted on `v1`:
the prompt requires source-review commits on valid assigned branches, and no
such checkout passed preparation. No source decision, protected file, lock,
assignment, ref, merge or remote publication was changed. Push: not performed,
outside this invocation's authority.

## Authorized preparation recovery: EX-PREP-001

Following the blocked preflight, the User explicitly instructed local merges
and repository cleanup. [EX-PREP-DR-001](EX-PREP-DR-001-branch-recovery.md)
captures the exact instruction, inspected source/target tips, administrative
installation boundary, serialized merge plan and required verification before
action. This is a new preparation operation; the preceding blocked review
and its failures remain historical evidence. Execution is pending, and no
source decision or readiness claim changes merely by recording authority.
