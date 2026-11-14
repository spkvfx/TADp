# Development-project setup verification

**Standing:** Observed setup evidence; no new invariant or initiative acceptance  
**Captured:** 2026-11-14 by Codex, with independent agent review  
**Human steward:** Current repository owner, including the respective owner of a fork  
**Authority:** [SETUP-001](../../../decisions/SETUP-001.md), [OWNERSHIP-001](../../../decisions/OWNERSHIP-001.md), [ADOPTION-001](../../../decisions/ADOPTION-001.md)  
**Installation and governing source:** `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`  
**Captured pre-adoption HEAD / coherence baseline:** `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`  
**Execution branch:** `setup/tadp-development-project`, created from preflight `v1` at that commit

## Identity and preflight

R and the shared Git worktree root are `C:/Users/User/PycharmProjects/TADp`.
P is `R/TADp/`, named TADp, with Git prefix `TADp/`. C is `P/protocol/`, D is
`P/template/`, U is `R/protocol/`, and S is `U/template/`. No nested Git
repository, second installed candidate scaffold, project scope or initiative
was created. Absolute paths here record the actual environment; portable role
paths govern the workflow and payload.

Preflight `git status --porcelain=v1 --untracked-files=all` was empty. HEAD was
the source above, on `v1`, two commits ahead of its tracking ref. Git identity
was Shawn Kearney; that identifies commit attribution only. No `core.hooksPath`
was configured. Existing hooks and shared configuration were preserved, with no
activation. Initial branch creation failed because Git metadata was read-only
in the sandbox; the authorized metadata operation then succeeded with scoped
permission. Only this setup's untracked installation existed between attempts.
No unrelated work was moved, stashed, discarded or committed.

The source was exported with `git archive --format=zip HEAD protocol` into an
isolated temporary directory and expanded before installation. No uncommitted
source drift was present or silently packaged. [The preflight manifest](upstream-preflight.json)
retains SHA-256 hashes of all 195 upstream files, including both locks. The
archive's exact source revision is retained in [the installation manifest](installation-manifest.json).

## Assembly and source selection

Copy `protocol/template/project/` including dotfiles to P, then install the
complete outer `protocol/template/` as D. The outer library replaces only the
new scaffold's nonrecursive library README placeholder. The embedded suite,
runtime tools and project-use documentation remain unchanged. The manifest
records 226 initial payload files, including 139 protected files, exact source
paths/revision/hashes, installed hashes and working-entry-point customization.
It is source provenance, not a future promotion authorization.

The scaffold's README and tests README specifically exclude distribution
development reports and regression fixtures. The older distribution
getting-started manual broadly says to copy docs/tools/tests. This setup follows
the specific clean-scaffold assembly, retaining its required runtime support
and running the pinned distribution regressions without importing those
development fixtures into P. This guidance ambiguity is disclosed; it changes
no invariant. P/tests/ starts with its original project-verification README.
No upstream live initiatives, realization notes, decisions, products, ownership,
adoption, conflicts or historical test outcomes became new project records.
These setup logs record actual verification of the pinned source in this run.

Canonical instance sources are P/template/project/project-profile.template.md,
the evidence-register template, the initiative-index/status/version-scopes/
version-scope-migration-ledger/work-conflicts templates, and the common decision
receipt source. Required headings are retained; exemplar rows are removed from
empty live registries. All actual setup decisions are captured separately.
No speculative initiative, feature, scope, product, delivery, acceptance or
completion record was created. The candidate workspace has only its boundary
README. Existing template files outside D remain unchanged reusable shapes,
not populated historical records.

## Checks and actual results

Configured SDK discovery used PyCharm `get_python_environment` against the
validator in each context. It returned Python 3.11.1, a venv at
`R/.venv`, executable `R/.venv/Scripts/python.exe`, package manager pip. Commands
below abbreviate that exact executable as `$py`; no package was installed.
`PYTHONDONTWRITEBYTECODE=1` prevented source-tree cache writes. These commands
are recorded evidence, not instructions automatically executed by this report.

| Check | Actual command or procedure | Result and evidence |
|---|---|---|
| Baseline protection | `$py protocol/tools/tadp_protect.py check protocol` from R | Exit 0, zero errors; [log](baseline-protect.txt) |
| Baseline structure | `$py protocol/tools/tadp_validate.py protocol` from R | Exit 1, one TADP041 error, zero warnings; [log](baseline-validate.txt) |
| Pinned regression behavior | `$py -m unittest discover -s protocol/tests -v` from R | Exit 0: 292 tests in 247.565 seconds, 4 skipped, no failures; [full log](baseline-tests.txt). Skipped cases remain unverified |
| Initial installed protection | `$py TADp/tools/tadp_protect.py check TADp` | Exit 0, zero errors; [log](installed-protect.txt) |
| Initial installed validation from R/P | Explicit P and `.` respectively | Each exited 1 with five missing links to this report before it existed; [R log](installed-validate-R.txt), [P log](installed-validate-P.txt). Retained as failed runs, then rechecked |
| Final installed protection | `$py TADp/tools/tadp_protect.py check TADp` | Exit 0, zero errors; [log](final-protect.txt) |
| Final structure from R | `$py TADp/tools/tadp_validate.py TADp --base-ref 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6` | Exit 0, zero errors and warnings; [log](final-validate-R.txt) |
| Final structure from P | `$py tools/tadp_validate.py . --base-ref 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6` | Exit 0, zero errors and warnings; [log](final-validate-P.txt) |
| Root entry-point links | Resolve every local Markdown file target in R/AGENTS.md and R/README.md | All 30 targets resolve; P file links are also checked by its validator |
| Upstream preservation | Rehash all U files and compare paths/digests to preflight | 195 before, 195 after, zero additions/removals/content changes; [result](upstream-preservation.json) |
| Context and path safety | Resolve explicit P/G/C/D/U/S/suite/prompts from R and P; inspect reparse points and candidate markers | Same identities in both contexts, no nested .git or candidate profile, zero reparse points; [result](context-resolution.json) |
| Rerun inspection | Resolve the repository prompt from both contexts; inspect 10 existing canonical records/receipts and compare project hashes before/after | Same installation and preserved adoption baseline, no duplicate project, no writes; 253 files unchanged during inspection; [result](rerun-inspection.json) |

The upstream failure is exactly `TADP041 project-profile.md: cannot verify
coherence Git baseline or comparison revision: adopted coherence baseline must
not be removed or disabled`. Source locks passed. Its historical profile state
is outside the authorized setup edit boundary. It is preserved and not waived,
repaired, or counted as a pass. P has distinct project-root history and is
checked independently. Baseline success is limited to protection and the
exercised regression cases; there is no upstream-wide conformance claim.

The four skipped regressions cover three symlink cases unavailable without
Windows symlink privilege and one POSIX executable-mode case unavailable on
Windows. Their precise names and reasons remain in the full log. No claim is
made that those platform-specific cases passed.

## Context and rerun verification

Read-only checks from R explicitly select `R/TADp`; from P they explicitly
select `.`. Verify both resolve the same P, enclosing Git root, C, D, governing
suite, and local prompt boundary. C has no project-profile, .git, initiative
index or authoritative suite. Reparse points or escaping links are not allowed.
P/prompts/AGENTS.md remains byte-identical to the pinned clean scaffold, and
protected D/suite copies retain their original locks unchanged.

On rerun, verify those identities, locks, receipt source identity, adoption
baseline and current customization before writing. Reuse this project, the
stable receipts, the existing canonical registries and recorded human
decisions; do not create a second nested TADp directory or new adoption event.
Re-resolve from the identified repository prompt, not cwd alone. A candidate
file cannot redirect the target into U. No feature introduction or upstream
promotion has occurred. Changed source/destination content requires a current
comparison, not reuse of stale qualification. Collision or incompatible work
blocks the affected write rather than overwriting it.

The first preservation comparison attempt incorrectly wrapped PowerShell's
JSON array in another array. It failed its audit assertion without demonstrating
upstream drift. Correcting the read-only comparison's array shape produced the
195-to-195, zero-difference result above; no source repair was performed.

## Independent semantic review

Requirements discovery and the project-specific workflow guide were delegated
to a separate agent. That agent identified the clean-scaffold/manual-guide
ambiguity, no-owner-inference requirement, unchanged local prompt restriction,
bootstrap library placeholder handling and event-specific record requirements.
Those findings were reconciled in the assembly and instructions above.

The distinct final reviewer `/root/independent_review` assessed the complete
setup after structural verification. One evidence finding was raised: context
results identified D but omitted S, the upstream protected library. Both context
checks were rerun with explicit U/S resolution and equality assertions, and
the context JSON and this report were reconciled. The reviewer confirmed the
correction and reported no remaining blocking or medium findings.

The reviewer independently confirmed all 226 installation mappings against
current content, all 139 protected copies against their pinned source hashes,
and all 195 upstream files against preflight; it also confirmed the unchanged
local prompt boundary, candidate README-only state, role-based ownership,
separate adoption receipt, full serial delivery route and absence of invented
lifecycle events. It confirmed the rerun inspection and the appropriateness of
the disclosed upstream error, skipped tests and future branch-coordination gate.
Automated structure/protection and independent semantic review remain separate
evidence; neither authenticates personal repository control or accepts an initiative.

## Changed-path inventory and recovery

Only R/AGENTS.md and R/README.md are changed outside the new P. P contains the
manifested baseline plus canonical live coordination/profile instances,
project-specific instructions/guide, candidate README, three actual decision
receipts, and this setup's observed evidence. The final exact path inventory
is retained in [changed-paths.txt](changed-paths.txt). No .gitignore, repository prompt, U file,
upstream lock, example or other project changes are in scope.

The complete staged inventory contains 256 files (254 beneath P and the two
root entry points), exactly matching the path list, with no outside-scope
staged paths. The staged diff and source mappings were reviewed. Default
`git diff --cached --check` flags Markdown hard-break spaces and final blank
lines in unchanged canonical copies as well as intentional hard-break fields
in instances. Those source bytes are preserved. The nonpersistent
`git -c core.whitespace=-blank-at-eol,-blank-at-eof diff --cached --check`
check passes; no validation, protection guard or lock was disabled or changed.

Recovery is a separately scoped Git operation. Preserve this branch and the
immutable base. Compare each setup path against its prior content and any later
work; restore only the authorized setup delta. Never recursively remove P over
new work or reset shared history. Existing upstream content is not a recovery
target because it was not changed. Source locks are copied, not regenerated.
Do not run reset/sync apply to simulate a rerun or fix evidence.

## Final disposition

The requested bootstrap is complete: the installed/adopted project passes its
structural and protection checks, resolves both operating contexts, preserves
upstream bytes and locks, and has independent semantic review with findings
reconciled. This is setup conformance to the bounded prompt, not a claim of
upstream-wide or future product conformance. Ownership is role-based under
OWNERSHIP-001 and adoption is explicit under ADOPTION-001. The integration base
and branch-role assignment for future work must be coordinated at its actual
allocation event; no scope allocation needs to be invented for bootstrap.
Establishing this project completes no feature,
initiative, reusable-source introduction, promotion, rollout, live migration,
integration, publication or release. Those remain separately governed events.

The scoped setup commit contains this report, the exact path inventory and all
three receipts. Its immutable identity is discoverable with
`git log --diff-filter=A --format=%H -- TADp/evidence/non-authoritative/setup/verification.md`
from R. No self-referential future commit identifier is invented in the report;
the final execution response reports the actual resulting hash. No merge or
remote operation follows that local commit.
