# Documentation refresh verification

Non-authoritative preparation evidence recorded by Codex on 2026-11-14.
Authority, source revision, settings and workflow limits are in
[preparation](preparation.md); reviewed areas are in [coverage](coverage.md).

## Exact result and source identity

The invoked prompt and captured Git baseline are
`345a05559afc177f50609ccc2bb819a050f284b3`. Work is retained on
`docs/refresh-current-documentation`, a preparation branch rather than an
invented initiative execution assignment. The [manifest](manifest.json) records
canonical UTF-8/LF SHA-256 identities, prior candidate/source/D/S baselines,
repository support bytes, transformations, exclusions and recovery.

There are 19 candidate sources: four reused split drafts, three revised split
drafts and twelve new explanatory drafts. They map to 19 existing reusable
destinations in each of D and S, then 20 U runtime consumers. The compatibility
guide uses `project/docs/development/README.md` as its reusable source, and both
runtime `developing-tadp.md` and `README.md` in that development directory as
consumers. All other mappings use `project/<runtime-path>`; the full exact list
is in the manifest, not an inferred directory synchronization.

The [review patch](../../../protocol/documentation-refresh.patch) is an
unapplied zero-context proposal against pinned U content. Use
`git apply --check --unidiff-zero` only in an isolated copy at the stated base;
that successful check supplies no live application or protected-edit authority.
The historical split patch and evidence remain unchanged. Prior results retain
their own exact source/content identities.

## Changed paths and scope

| Category | Paths relative to R and disposition |
|---|---|
| Repository support changed | README.md, docs/README.md, docs/developing-tadp.md; navigation discloses pending candidate work |
| Existing candidates revised | TADp/protocol/documentation/README.md.in, docs/README.md.in and docs/development/repository-layout.md.in (last two relative to the same documentation directory) |
| Existing candidates reused | docs/development/getting-started.md.in, git-and-codex-requirements.md.in, validation-and-quality.md.in and developing-tadp.md.in under the candidate documentation directory |
| New candidates | docs/guides/protected-source-integrity-migration.md.in, project-local-prompts-migration.md.in, version-scope-migration.md.in; tools/README.md.in; evidence/README.md.in, non-authoritative/README.md.in and non-authoritative/realizations/README.md.in; initiatives/README.md.in and implementation/design/planning/README.md.in; products/README.md.in (all under the candidate documentation directory; exact paths in manifest) |
| New candidate review artifact | TADp/protocol/documentation-refresh.patch |
| Project evidence navigation | TADp/evidence/evidence-register.md appends only EVD-005; existing source classifications and history preserved |
| Preparation/verification records | TADp/evidence/non-authoritative/documentation-refresh/: preparation.md, coverage.md, verification.md, qualify.py, baseline-checks.json, inventory.json, manifest.json, qualification.json, final-checks.json, regressions.json, named check logs and retained attempt-1/ evidence; actual final file list is in the scoped commit |
| Preserved | All U, D, S, P authoritative sources, all locks/AGENTS files, existing tools/tests/hooks/configuration, other stored prompts, P profile/decisions/scope/status/lifecycle, prior split/setup evidence, .gitignore, and examples |

[Coverage](coverage.md) reviews all 32 scoped existing portable documents and
five repository entry guides, with the full protected/historical/project-owned
Markdown inventory in inventory.json. Runtime documentation was changed only
inside isolated trials; no U move, split, replacement or rollout was performed.
No new guide was needed where an existing owner could explain the feature.

## Environment and actual checks

PyCharm get_python_environment selected Python 3.11.1, package manager pip, at
`C:/Users/User/PycharmProjects/TADp/.venv/Scripts/python.exe` before Python
invocations. No package was installed. `$TadpPython` below denotes that actual
executable. The helper passes it to child checks with `-B` and disables bytecode
writes in fixtures. Commands and output are recorded without converting a
failed check into a pass.

| Check / working root | Actual command or method | Exit and result |
|---|---|---|
| Baseline P from R | `$TadpPython -B TADp/tools/tadp_protect.py check TADp` | 0; zero integrity findings |
| Baseline P from R | `$TadpPython -B TADp/tools/tadp_validate.py TADp --json` | 0; zero errors/warnings |
| Baseline U from R | `$TadpPython -B protocol/tools/tadp_protect.py check protocol` | 0; zero integrity findings |
| Baseline U from R | `$TadpPython -B protocol/tools/tadp_validate.py protocol --json` | 1; inherited TADP041 at project-profile.md, adopted coherence baseline missing/disabled |
| First qualification from R | `$TadpPython -B TADp/evidence/non-authoritative/documentation-refresh/qualify.py` | 1; all trial checks and links passed, but two old split anchors were missing; retained under attempt-1/ |
| Corrected qualification from R | Same helper after two compatibility anchors were added | 0; exact report in qualification.json; no lost anchors |
| Patch check in pinned isolated source | `git apply --check --unidiff-zero` with the exact review patch path | 0; candidate-patch-check.log |
| Root trial, P=G | Inline PowerShell component-copy sequence from the installation guide, retaining complete embedded suite/lock, then exact candidate overlay | 0; root-assembly.log; required dotfiles, guards and locks present; no hook activation |
| Root trial from P | `$TadpPython -B tools/tadp_protect.py check .`; `$TadpPython -B tools/tadp_validate.py . --json` | Each 0; zero errors/warnings |
| Nested trial, P=G/projects/widget | Same assembly and exact overlay | 0; nested-assembly.log; required dotfiles, guards and locks present; no hook activation |
| Nested trial from P | Same two explicit P checks | Each 0; zero errors/warnings |
| Nested trial from G | `$TadpPython -B projects/widget/tools/tadp_protect.py check projects/widget`; corresponding validator with `projects/widget --json` | Each 0; selected nested project remains the checked target |
| Assembled portable docs | Authored local Markdown destinations/fragments from all 20 mapped runtime files | 205 links each trial; zero missing targets/fragments; all original heading anchors retained |
| Repository support links | Root README and four docs pages | 39 links; zero missing targets/fragments |
| Excluded source identities | Canonical-content comparison with immutable baseline | 358 tracked source/instruction/config paths checked; zero changes |
| Full pinned regressions in corrected root fixture | `$TadpPython -B TADp/evidence/non-authoritative/documentation-refresh/qualify.py --regressions`, launching `-B -m unittest discover -s tests -v` from its root P | 0; 292 tests in 322.162 seconds, OK, 4 skipped; exact command/root in regressions.json and full output in fixture-regressions.log |
| First final-check helper invocation from R | Same helper with `--final` | 1 before checks, due to a syntax error in the added evidence-only aggregate condition; final-attempt-1.log retained |
| Corrected final checks from R | Same helper with `--final`; protection plus validation using explicit P/U roots and `--base-ref 345a05559afc177f50609ccc2bb819a050f284b3` | Aggregate 0; P checks 0/0, U protection 0, U validation still 1 with exactly the original TADP041; no validation failure relabelled as a pass |
| Final link/identity checks | final-checks.json | 39 repository links and 13 evidence links resolve; all 19 candidate hashes unchanged; 358 excluded paths unchanged |

The corrected temporary workspace is recorded in qualification.json as
`C:/Users/User/AppData/Local/Temp/tadp-doc-refresh-b_gh31j6`. Fixtures use only
the immutable U archive plus exact declared candidates, without R/docs or
populated P history. Their fresh Git baselines are disposable fixture identity,
not project adoption. The protected library and embedded suite remain pinned
and unmodified. This verifies manual runtime assembly and documentation; it
does not verify introduction into a revised library or later synchronization
of that library. Those operations require actual authority and fresh checks.

## Retained failure and correction

The initial aggregate qualification exited 1 because the earlier split had
renamed two headings without compatibility anchors: `#developer-documentation`
in docs/README and `#adopt-tadp-in-another-repository` in the portable README.
Every installation/protection/validation/link check itself passed. The result
was not treated as a qualification pass. Its JSON reports, logs and the two
pre-correction candidate byte sequences are retained in attempt-1/ under their
original relative basenames; links to logs resolve inside that retained folder.

Explicit HTML compatibility anchors restore the prior fragments without a
second installation procedure or changed workflow rule. Both installations,
the patch, hashes, links and heading-anchor coverage were rerun successfully
against the corrected content. No lock, validator, assertion or protection
mechanism was changed to obtain success.

The first `--final` invocation did not execute any checks: adding a stricter
comparison with the inherited U finding introduced an extra closing parenthesis
in the evidence helper. That failed invocation is recorded in final-attempt-1.log.
The syntax was corrected and the helper rerun. The final aggregate checks actual
preservation, links, P validation, both protection results and exact agreement
with U's original failed finding; it does not claim U validation passed.
This changed no candidate content, governing tool, fixture assertion or live lock.

The four regression skips are three symlink tests unavailable without the
platform privilege and one POSIX execution-mode test unsupported by Windows
chmod. Those cases are not verified in this environment. No second full suite
was run in live U: this invocation runs the pinned complete suite in the exact
qualified root fixture. No product behavior changed, so no consuming-project
product test is claimed. Sync/reset applies, hook activation and protected
library introduction were not run on live projects. Regression fixtures exercise
their own isolated operations; those results grant no live action authority.
Remote example behavior and external link availability were not checked.

## Independent review

The distinct reviewer is `/root/independent_review`; producing agents were
`/root`, `/root/review_scope` and `/root/tools_baseline`. Review covered the
complete scoped tracked/untracked diff, all 19 candidate fragments, R entry
guides, coverage/preparation, exact mappings, evidence helper and trial output.
The reviewer independently recomputed all 19 current candidate hashes, checked
all 20 runtime payload hashes in both corrected fixtures, and confirmed the
205/205 link results, zero missing anchors, patch check, live preservation and
root/nested check results. The two compatibility-anchor losses were the sole
content finding and were reconciled as above. No further content blocker was
found. The final result review includes the actual full regression report and
live-check evidence; skipped tests remain unverified. The reviewer gave final
signoff with no remaining blockers after reviewing both retained failures and
the final report. This is independent agent review, not human acceptance.

## Pending delivery and precise next authority

This reaches qualified candidate preparation only, with the actual regression
and final check results above. It does not establish initiative execution or
development completion. Step 5 cannot introduce these files into D from this
invocation alone. P still has no appointed project integration base, allocated
scope/execution assignment, or accepted initiative for this work. Its owning
workflow must prepare narrow claim(s) from the split and refresh sources,
resolve actual human gates and obtain explicit acceptance of an exact baseline.

The concrete protected-update proposal is the manifest's 19 exact D sources and
the affected D template lock, after acceptance/current drift comparison. No LLM
suite change is proposed. Introduction must be tested from the resulting library;
only actual standard completion evidence can then establish completed development.
Promotion needs a human instruction naming that immutable completed source,
the sanitized 19-file S mapping and affected lock. Rollout then needs exact
authority for the 20 U consumers from the pinned promoted revision. No future
commit can be named before it exists. Do not infer these decisions from a
passing structural check, a preparation commit or ownership/adoption receipts.

The prompt's serial delivery block remains pending; later delivered-result
claims cannot advance. Its independent reporting clauses authorize this
preparation review and scoped traceable commit, which is not Stage 13.
No initiative acceptance/completion, protocol adoption, integration, PR, remote
write, publication, deployment or release is claimed. No example synchronization,
separate-fork work, mirror validation or external behavior assertion occurred.

Remaining protected shape proposals and executable/governance defects are
listed with exact paths and required authority in coverage.md. They do not
authorize changing the protected payload, disabling TADP041, or enabling the
older root hook. Recovery compares the manifest and retained prior bytes with
current content, preserves later/unrelated work, and performs no automatic rollback.
