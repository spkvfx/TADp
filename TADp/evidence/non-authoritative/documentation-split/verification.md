# Documentation split: preparation verification

Recorded by Codex on 2026-11-14. Non-authoritative observation, not initiative
acceptance, an execution/delivery record, or completion evidence. Read the
[preparation record](preparation.md) for authority, scheduling, scope and recovery.

## Exact prepared output

Source Git revision: `014d455e3d99213e0dc4a156cb198ac1a4a85747`.
Branch: `docs/separate-repository-protocol-docs-prompt`, the existing bounded
prompt/preparation branch, not an invented initiative execution assignment.
The [manifest](manifest.json) records canonical SHA-256 identities for every
candidate, original source, D/S baseline and repository support file. The
[candidate diff](../../../../TADp/protocol/documentation-split.patch) compares
all eight proposed runtime consumers with the pinned distribution. It is a
reviewable proposal; none of that distribution diff has been applied.

| Disposition | Exact paths relative to R |
|---|---|
| Changed repository entry point | `README.md` |
| Added repository guides | `docs/README.md`, `docs/repository-layout.md`, `docs/developing-tadp.md`, `docs/implementing-tadp-in-projects.md` |
| Added candidate drafts | `TADp/protocol/documentation/README.md.in`, `TADp/protocol/documentation/docs/README.md.in`, `TADp/protocol/documentation/docs/development/getting-started.md.in`, `repository-layout.md.in`, `git-and-codex-requirements.md.in`, `validation-and-quality.md.in`, `developing-tadp.md.in` (last four under the same development directory) |
| Added candidate review artifact | `TADp/protocol/documentation-split.patch` |
| Added owning preparation evidence | `TADp/evidence/non-authoritative/documentation-split/`: preparation.md, verification.md, qualify.py, manifest.json, qualification.json, qualification-attempt-1.json, qualification-attempt-2.json and named check logs |
| Evidence navigation | `TADp/evidence/evidence-register.md` links this preparation without promoting its standing |
| Retained without change | All `protocol/**`, P's protected library/suite, P/prompts/AGENTS.md, governance/adoption receipts, scope/initiative registries, project workflow, all AGENTS.md files, tools/tests/hooks/configuration, .gitignore and separate examples |
| Moves/splits actually delivered to U | None. Root maintenance explanations are extracted; portable splits and compatibility replacements remain prepared only |

The manifest maps seven candidates to existing D/project sources, then the
same S/project sources, then eight U consumers. The development compatibility
guide maps to the already supported library `project/docs/development/README.md`
and rolls out to both U's original `developing-tadp.md` path and its development
index. This preserves old consumers without changing sync's allowlist or tests.
No protected-source removal, invariant revision or LLM lock refresh is proposed.

The diff uses zero context (`-U0` equivalent); `git apply --check --unidiff-zero`
against the clean pinned distribution exits 0 (candidate-patch-check.log).
Only extra blank lines at EOF were trimmed in four imported drafts after the
first passing trial. No text, heading, command or link changed. Both installations
were reassembled/rechecked successfully against the final formatted hashes.
The prior successful fixture and manifest are preserved as
qualification-before-formatting.json and manifest-before-formatting.json;
the 80-test isolated regression result belongs to that prior exact trial
(`C:/Users/User/AppData/Local/Temp/tadp-doc-split-z2xftf32/root-git`).
It was not rerun for EOF-only formatting. Existing baseline regressions and
current structural/protection/link/patch checks remain separately identified.

## Baseline and actual checks

SDK selected through PyCharm get_python_environment before Python commands:
Python 3.11.1, `R/.venv/Scripts/python.exe`, package manager pip. No dependency
was installed. `$py` below abbreviates that actual configured executable.

| Check and working directory | Actual command / method | Exit and result |
|---|---|---|
| Baseline P, from R | `$py TADp/tools/tadp_protect.py check TADp` | 0; 0 errors |
| Baseline P, from R | `$py TADp/tools/tadp_validate.py TADp --json` | 0; 0 errors, 0 warnings |
| Baseline U, from R | `$py protocol/tools/tadp_protect.py check protocol` | 0; 0 errors |
| Baseline U, from R | `$py protocol/tools/tadp_validate.py protocol --json` | 1; exactly TADP041 at project-profile.md, adopted coherence baseline missing/disabled |
| Baseline regressions, from U | `$py -m unittest discover -s tests` | 0; 292 tests in 310.252 seconds, OK, 4 skipped. Full run observed through tool session 32761; skips remain unverified |
| Corrected isolated assembly/checks, from R | `$py TADp/evidence/non-authoritative/documentation-split/qualify.py` | 0; actual commands, temporary roots, identities and logs in qualification.json |
| Root fixture, from its P=G | `$py tools/tadp_protect.py check .`; `$py tools/tadp_validate.py . --json` | Each 0; 0 errors, 0 warnings |
| Nested fixture, from P=G/projects/widget | Same two explicit P commands | Each 0; 0 errors, 0 warnings |
| Portable documentation | Inline PowerShell assembly of the guide's component copy sequence, pinned Git archive plus exact runtime candidate overlay | Root and nested assembly each 0; required dotfiles/guards/locks present; no shared hooks configured |
| Scoped local links/anchors | Evidence helper reads authored links/fragments in assembled candidate docs | 144 each installation, no missing targets/anchors; no R/docs or populated P dependency |
| Root navigation | Same helper on R README and four root guides | 34 links, no failures |
| Isolated validator regressions, from root fixture P | `$py -m unittest discover -s tests -p test_tadp_validate.py -v` | 0; 80 tests in 78.356 seconds, OK; fixture-regressions.log |
| Initial tracked diff hygiene, from R | `git diff --check` before staging new files | 0; Git's CRLF conversion notice is informational |

The trial retains the pinned protected library and embedded authoritative
suite unchanged; it overlays candidate documentation only at runtime paths.
This demonstrates portable manual assembly and runtime docs, not revised-library
synchronization or D/S introduction. Those require authority and fresh checks
after actual protected changes. Root and nested fixture Git baselines identify
disposable trials only; no live adoption, appointment, initiative or release
occurred. No product behavior changed, so no product-specific suite applies;
future adopting projects must run their actual product checks.

## Failed attempts and recovery evidence

Attempt 1: local PowerShell script-file execution was disabled by system policy.
Assembly exited 1; missing-script protection/validation calls exited 2. The
first helper incorrectly continued dependent checks and itself exited 0; that
wrapper status is not qualification success. The helper was repaired to stop
failed assembly and return aggregate failures. Inline PowerShell execution
exercises the reference commands without any execution-policy modification.

Attempt 2: both assemblies exited 0 but protection/validation each exited 1
with TADP025 for the unrecorded authoritative-suite README. The component map
was corrected to retain the complete embedded suite and its matching lock,
instead of unioning two separately locked suite sets. No live protected source
or fixture lock was refreshed. Corrected attempt 3 passed all stated checks.

Historical JSON reports retain their original text, including original log
basenames. The logs were renamed before the next run; use this explicit mapping
when interpreting the historical report, not the current successful logs:

| Report | Original basename in that report | Retained historical artifact |
|---|---|---|
| qualification-attempt-1.json | `root-assembly.log`, `root-tadp_protect.log`, `root-tadp_validate.log`, and corresponding `nested-` names | Same basenames with `-attempt-1` before `.log` |
| qualification-attempt-2.json | Same six basenames | Same basenames with `-attempt-2` before `.log` |
| qualification.json | Same six basenames | Current unrenamed successful logs |

Temporary failed/successful assemblies are retained at their recorded paths.
They are outside the clean payload and live checkout. Do not restore their
files over later project work. Recovery of this preparation uses pinned prior
Git blobs and exact manifest comparisons, preserving later/unrelated changes.

## Independent review

Reviewer: distinct agent `/root/independent_review`, not the producing agent.
Reviewed root README/docs, all seven candidates, exact mapping and qualification.
The reviewer independently recomputed all candidate hashes and confirmed both
passing fixture results, 144 scoped links each and 34 root links.

| Finding | Disposition |
|---|---|
| Worked installation lacked a small worked adoption record sketch | Added reference-only profile/receipt/root/baseline/legacy-ledger sketch with placeholders and no invented decision |
| Component union mixed separately locked authoritative suites | Corrected source map and commands; retained complete embedded suite and lock; reran both installations successfully |
| Historical JSON log basenames now refer to renamed artifacts | Explicit historical rename map above; original failed reports/logs preserved |

Reviewer reported no remaining content blockers. Encoding audit by the other
agent confirmed proper UTF-8 source/candidate quotes, no introduced mojibake
and no changes to its four candidate files; exact qualification hashes remain
valid. Producer's final checks also inspect scoped changes and excluded trees.

## Authority and completion limits

This finishes the authorized preparation and its qualification, not the full
prompt's delivery. The invoked prompt explicitly retains initiative acceptance
and exact D introduction, actual development completion, S promotion and mapped
U rollout. P still needs an actual coordinated integration base and scope/
execution placement before its initiative can be prepared/accepted through the
owning workflow. Neither the prompt branch nor tested drafts supplies that fact.

The concrete protected update proposal is exactly manifest.json's seven D
sources and the affected D template lock, after acceptance and current drift
comparison. Subsequent promotion must name the actual completed immutable
source, seven S sources/affected lock and eight U rollout consumers. No future
commit identity can be predeclared. Until those gates hold, there is no ordinary
initiative execution/completion, delivery, adoption, merge, remote operation,
release or publication claim. Root navigation accurately links current U
guides while disclosing pending portable replacements.

## Final preparation checks

`$py TADp/evidence/non-authoritative/documentation-split/qualify.py --final`
from R reported P protection/validation exits 0, U protection exit 0, and U
validation exit 1 with the identical inherited TADP041 finding. The preservation
assessment itself exited 0: seven candidate hashes still match, root links
remain 34/0 failures, and all tracked U files, D, P's authoritative suite,
P/prompts/AGENTS.md, root AGENTS.md and .gitignore match the pinned baseline.
There is no candidate or excluded-tree drift. Exact commands and logs are
retained under qualification.json's `final` field. No newly introduced
structural/protection failure remains in the authorized preparation.

A scoped preparation commit may retain these authorized drafts, support pages
and evidence on the existing prompt branch. It is not Stage 13 finalization,
scope allocation, accepted initiative execution or a completed deliverable.
Use actual Git history for its identifier; no future hash is fabricated here.

Final staged diff inspection accounts for every added/changed path.
`git diff --cached --check` exits 1 solely for four trailing-space lines in the
two retained raw attempt-1 PowerShell error logs. Their original bytes are
preserved as failure evidence. The same check scoped to all authored Markdown,
candidate sources/patch, evidence navigation and qualification script exits 0.
No whitespace configuration or integrity gate was changed to hide those logs.
The independent reviewer rechecked all seven final manifest hashes after EOF
formatting and confirmed no substantive review change or remaining blocker.
