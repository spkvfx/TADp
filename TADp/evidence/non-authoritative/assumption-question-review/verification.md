# Assumption and open-question review preflight verification

Recorded by Codex on 2026-11-14. This is non-authoritative observed evidence.
[Preparation](preparation.md) owns the exact instruction, boundaries, source
revision, effective settings, work inventory and pending integration decision.

## Environment and actual checks

Working directory for all commands was R,
`C:/Users/User/PycharmProjects/TADp`. PyCharm `get_python_environment` selected
Python 3.11.1, venv, package manager pip, executable
`C:/Users/User/PycharmProjects/TADp/.venv/Scripts/python.exe`.
No package was installed. `$TadpPython` below is that exact returned executable.

| Actual command | Exit | Actual output/result |
|---|---|---|
| `& $TadpPython -B TADp/tools/tadp_protect.py check TADp` | 0 | `TADp protected-source check: 0 error(s)` |
| `& $TadpPython -B TADp/tools/tadp_validate.py TADp --json` | 0 | valid=true, errors=0, warnings=0, findings=[] |
| `& $TadpPython -B protocol/tools/tadp_protect.py check protocol` | 0 | `TADp protected-source check: 0 error(s)` |
| `& $TadpPython -B protocol/tools/tadp_validate.py protocol --json` | 1 | valid=false, errors=1, warnings=0; inherited TADP041 at project-profile.md: `cannot verify coherence Git baseline or comparison revision: adopted coherence baseline must not be removed or disabled` |

The U validation failure is retained, not relabelled as a pass or repaired.
It was already disclosed in setup and documentation qualification evidence.
These baseline checks verify no candidate behavior: no candidate has been
implemented and no lock was refreshed.

After writing these preflight records, the same P validator command returned
exit 0 again, with zero errors and warnings. A PowerShell check parsed the
source-map JSON and compared all 16 existing sources with their recorded raw
SHA-256 digests: zero mismatches. Checking six authored Markdown file links
outside fenced source quotations found zero missing targets. `git diff --check`
returned exit 0. The first lexical link check exited 1 because it treated the
two verbatim `file:///` links inside the quoted original human instruction as
authored relative links; excluding fenced quotations corrected that check.
The exact human text was preserved. No candidate qualification is inferred.

The first staged whitespace check found six Markdown hard-break lines with
trailing spaces in the new preparation record, which the earlier unstaged
check had not covered while that file was untracked. Replaced them with blank
paragraph separation before the final staged check. Git's LF/CRLF advisory
does not change the recorded raw source digests or authorize normalization
of existing sources.

A separate agent reviewed the complete step-1 evidence and EVD-006 index row.
All recorded source hashes and relative file links matched, and no material
governance finding remained. Its command-rendering correction (PowerShell call
operator) and clarification distinguishing question resolution from delegated
intake placement were applied. This is preflight documentation QA, not the
unperformed step-4 independent review of a complete candidate diff.

Initial read attempts used two incorrect guessed filenames (the suite index
and realization template); neither existed. The actual canonical filenames
were found and read before use. These were discovery errors, not validation
passes or unavailable governing material.

## Reached boundary and remaining checks

Execution item 1 remains incomplete on the exact integration-base decision in
preparation.md. No Stage 0 allocation, accepted initiative, execution record or
candidate modification is claimed. Steps 2–4 have not begun. Structural/link
checks on a candidate, focused semantic regressions, isolated installation or
workflow trial, candidate lock qualification, and independent complete-diff
review remain not performed. Read-only inventory assistance is not that review.

All source-map operations are proposed, not applied. A later exact qualified
manifest must replace no provenance: retain these initial digests, record
candidate identities and reconcile drift before delivery. Runtime navigation
files absent in a reusable library may be copied from a pinned declared
baseline only after that dependency is mapped in the owning suite.

No installed-source introduction, completion, promotion, rollout, integration,
push, release, adoption, external lookup or live review was performed. Optional
example-fork context was not consulted during this blocked preflight; it is
not a dependency or a verification target. Re-entry and subsequent boundaries
are described in preparation.md.

## Resumed preparation and alignment

The human answered the pending base question with exact words `TADp v1`.
[INTEGRATION-001](../../../decisions/INTEGRATION-001.md) captures that actual
appointment separately from Codex placement. At resumed inspection the worktree
was clean on v1 at `9c9fd1daad655fd58349c005f8d31a4f52790cc9`.
The original preflight remains at `f6df64c`. Intake placement was recorded in
`ca52e33` before refs were created. The distinct v2 scope and dedicated member
were then created from the captured base, without merging either preparation
branch. Stage 0 allocation and reused exact owned P records are in `7b38e61`.
Actual commands and before/after identities are in [intake](intake.md).

Stage 1 created the canonical proposal; Stage 2 aligned revision 2 against the
source, governing requirements and prior proposed/partial documentation effort.
Stage 3 copied/populated the ten canonical initial-suite roles, preserving
all required sections, immutable assignment and initial Proposed history.
Stage 4 reviewed the complete current suite. No independent speculative
assumption or active product question was identified: the proposed behavior and
boundaries come directly from the exact source instruction. No invented item
disposition, human answer, acceptance, start or completion is recorded.

### Commands, outputs and corrections

Working directory remains R. Before Python invocation PyCharm environment
discovery again returned Python 3.11.1, venv, pip and the same exact executable
recorded above. No dependency was installed or interpreter changed.

| Check | Actual result |
|---|---|
| `& $TadpPython -B TADp/tools/tadp_protect.py check TADp` | Exit 0; `TADp protected-source check: 0 error(s)` |
| PowerShell parse/hash comparison of 16 mapped sources and four protection dependencies | 20 inspected; zero raw SHA-256 mismatches |
| First `& $TadpPython -B TADp/tools/tadp_validate.py TADp --json` after complete suite creation | Exit 1; five errors, zero warnings: four TADP002 original-relative-link findings in archived source-prompt.md, one TADP048 missing linked routing evidence in initiative README |
| Corrected same validator command | Exit 0; valid=true, errors=0, warnings=0, findings=[] |
| PowerShell complete-suite placeholder, whitespace, local file/fragment check | All ten canonical files inspected; 163 authored local links; zero problems |
| `git diff --check` | Exit 0; no whitespace errors; LF/CRLF advisories retained |
| `git diff --name-only 9c9fd1daad655fd58349c005f8d31a4f52790cc9 -- protocol TADp/template TADp/evidence/authoritative TADp/prompts TADp/protocol prompts .gitignore` | Exit 0; empty output, proving no scoped installed/distribution/candidate/prompt/ignore changes |

The first validator failure is retained as failed evidence. The source snapshot
was renamed from `source-prompt.md` to [source-prompt.txt](source-prompt.txt)
because it is an exact archival input with original relative links, not a new
current Markdown guide. Its content was not rewritten to repair those links.
All owned references now use that snapshot; Git blob remains exactly
`394e97ad00ca98fd5adb21f21b4ad61c7f6ba53e`. Intake records original/canonical
and CRLF worktree digests. The README routing cell now links the exact intake
record instead of presenting an unlinked path. No validator, guard or lock was
changed to obtain a pass. One attempted evidence-patch insertion failed its
context check and changed no file; the subsequent append used the actual context.

### Independent Stage 4 review

The independent governance-review agent read the complete ten-file Proposed
suite and relevant appointment, scope/member/source records and mapping. It
found no material semantic blocker: one implementation outcome, C-only products,
REV-01 through REV-11 planned coverage, correct human/agent/owner/source and
later authority boundaries, preserved prior work and no fabricated decisions or
lifecycle events. It independently confirmed all 20 source/dependency hashes,
the source Git blob, v1/v2 base identities and the empty excluded-path diff.
Its remaining action was to reconcile status/evidence and capture the exact
immutable complete-suite commit for the human acceptance request; these updates
do that without inventing the acceptance itself.

This is initial-suite alignment review. It is not the required independent
review of the eventual complete candidate diff. Candidate implementation,
semantic regressions, clean isolated candidate trial and qualification remain
not performed. Source prompt execution item 1 reaches the distinct acceptance
gate; items 2–4 remain serially unstarted. The earlier U TADP041 finding is not
rechecked or claimed repaired by P's passing validation.

### Exact changed-path ownership and next gate

All changes since the appointed base belong to P governance or initial records:

- `decisions/INTEGRATION-001.md`, `project-profile.md`,
  `docs/development/tadp-development-workflow.md`.
- `evidence/evidence-register.md` and
  `evidence/non-authoritative/assumption-question-review/`: `preparation.md`,
  `intake.md`, `source-map.json`, `source-prompt.txt`, `verification.md`.
- `evidence/non-authoritative/realizations/v2/`:
  `00-review-decisions-suite-index.md`, `RZN-001-owned-review-decisions.md`.
- `initiatives/version-scopes.md`, `initiatives/initiative-index.md`,
  `initiatives/status.md`, `initiatives/v2/README.md`.
- `initiatives/v2/implementation/tadp-001-owned-review-decisions/`:
  `README.md`, `proposal/README.md`, `proposal/proposal.md`, `assumption.md`,
  `scope-assessment.md`, `architecture.md`, `source-mapping.md`,
  `open-questions.md`, `implementation-roadmap.md`, `implementation-steps.md`.

The complete-suite commit containing this verification is the exact proposed
baseline; its actual immutable hash is supplied to the human after commit,
never fabricated inside a self-referential record. TADP-001 remains Proposed.
Ask for distinct Stage 7 acceptance of that exact baseline for implementation
and qualification in C only. The source explicitly retains initiative gates;
the integration-base answer is not acceptance. After actual acceptance,
applicable Stage 9 readiness and standard start evidence still precede product
work. D introduction, actual development completion, S promotion, mapped U
rollout, adoption, integration, remote operations and release retain their
separate authority/evidence boundaries.

## Candidate implementation and qualification

After the unimplemented state was explicitly clarified, the human responded
`but I do want this implemented.` with the same example-file attachment.
[ACCEPT-001](../../../initiatives/v2/implementation/tadp-001-owned-review-decisions/decision-receipts/ACCEPT-001.md)
preserves the full exact message and accepts the already presented baseline
`294d70d1b7b313bd46cab481b714c8cbb5c0e612` for C-only implementation and
qualification. Acceptance was committed as `0b13549` before product work.
The example attachment remains contextual; no separate scaffold was edited.

Stage 9 assessed readiness read-only after that acceptance: clean entry/exit
at `0b13549`, correct original branch/base/assignment, all20 pinned source hashes
matching and structural validation passing. SDK/API alignment is inapplicable
because none is affected. Actual implementation start followed with copies of
the four declared protection dependencies in C, then the [standard execution
record](../../../initiatives/v2/implementation/tadp-001-owned-review-decisions/execution-record.md)
and Accepted-to-In-progress event. No readiness artifact was created by the
assessment. One initial combined patch for copied acceptance templates was
rejected before changes because duplicate delete/add operations targeted the
same file; scoped population then succeeded. No authority or test was inferred
from that tool failure.

### Actual candidate changes

The [exact manifest](manifest.json) lists23 candidate files with canonical
content hashes, pinned provenance, future source/destination mappings and
operations/transformations. They include reviews05/06 and shared contract;
candidate specifications02/07/08; assumption/question/receipt/index shapes;
coverage/project navigation; one conditional combined project item shape;
four guard/lock dependencies; focused tests, synthetic scenarios and their
minimal generic directory navigation. The optional validator was not changed:
existing generic structure/link/coverage validation supports the new declared
source roles, while authority and meaning remain semantic/human obligations.

Both candidate reviews support independent either-kind discovery without a
prior answer and each item's own authorized same-review disposition, including
external canonical owners. The conditional project shape reuses existing
receipt/index sources; it is not an unused live register or umbrella initiative.
No installed reusable source, installed governing suite, distribution consumer,
example file, real lock, unrelated documentation draft or `.gitignore` changed.

### Exact commands, environment and observed results

All shell commands start from R unless their captured log states the isolated
fixture cwd. PyCharm environment checks selected the same venv executable,
Python3.11.1 and pip; no package or interpreter was changed. `$TadpPython` is
the exact executable recorded earlier. Child checks use that same executable
and `-B`; bytecode writes are disabled. The following are actual observations.

| Actual command or method | Result and scope |
|---|---|
| `& $TadpPython -B TADp/protocol/tests/test_assumption_question_review.py -v` | Initial10 tests passed; after review correction11 tests passed. These are document-contract regressions, not authority authentication or a guarantee of future LLM output. |
| `& $TadpPython -B TADp/evidence/non-authoritative/assumption-question-review/qualify.py` | Four retained attempts passed. The first tested22 files, then generic fixture navigation and scoped locks brought the candidate to23; third attempt `20261114T200403Z-9d5ded0f` tests the receipt correction; final EOF-normalized attempt `20261114T201704Z-509920ed` tests all23 exact files. |
| Pinned clean assembly | Git archive of `294d70d:TADp/template` plus exact candidate; complete outer library and runtime scaffold; fresh inert fixture Git baseline. No live P history, profile, adoption, example input or hooks. Exact tree/source identities and fixture paths are in qualification.json. |
| Changed-source file/fragment checks in installed roles |77 authored links pass;2 dynamic template links remain explicitly uninstantiated. Project sources are checked after runtime placement, not as a standalone partial scaffold. |
| Fixture-only lock refresh order | Embedded suite, outer library, runtime suite; all exit0 under explicit fixture-only authority. Full target inventories are generated instead of copying partial candidate locks as installed-valid. |
| Fixture `tools/tadp_protect.py check .` and `tools/tadp_validate.py . --json` | Each exit0; validation0 errors/0 warnings. |
| Fixture focused unittest discovery | Exit0; final11 tests pass using `TADP_REVIEW_ROOT` pointing to the actual clean fixture. |
| Deliberately tampered fixture prompt05 | Protection check exit1 as expected, naming the changed source; exact bytes restored and protection rechecked exit0. This is a negative test, not a failed passing gate. |
| Scoped C lock refresh | Installed protection tool with explicit C target and covered candidate-only authority; nested `--protected-root evidence/authoritative/LLM`, then outer `--protected-root template`, both exit0. Outer refreshed again after reviewed receipt correction. No installed lock refreshed. |
| Scoped C canonical inventory/digest checks |19 outer entries and4 embedded-suite entries match; zero problems. This partial-overlay integrity check is not a claim that C is an installed project. |
| Final identities |23 manifest/qualified candidate hashes and18 semantic-source hashes match current files; no drift. |
| Preservation before/after each clean trial |358 pinned excluded files compared; zero content changes, Git diffs or untracked additions in excluded scopes. |
| `& $TadpPython -B TADp/tools/tadp_protect.py check TADp` | Exit0, zero errors. |
| Raw live `& $TadpPython -B TADp/tools/tadp_validate.py TADp --json` after candidate source creation | Exit1 with46 TADP002 findings, all inside `protocol/template/...`; zero findings outside that partial-source link scan. Actual failed output retained in final-project-validation.json; never relabelled as a whole-P pass. |

[qualification.json](qualification.json) captures exact commands, cwd, exits,
logs, interpreter/version, library tree, all file hashes and the final fixture
`C:/Users/User/AppData/Local/Temp/tadp-owned-review-ren3pire/installed`.
Each earlier attempt and its logs remain under `qualification-attempts/`.
[candidate-protection.json](candidate-protection.json) records current scoped
lock checks. The helper's drift check was strengthened to include added and
removed candidate filenames before the final run; that change alters no tool
or governing validator.

### Semantic trial and independent review

[workflow-trial.json](workflow-trial.json) records the actual separate agent's
bounded interpretation of both entrypoints for all11 fixture inputs,22 pairs,
with exact supporting references and source hashes. It explicitly does not
manufacture literal answers or authority absent from abstract inputs. The
fixture is synthetic and is no standing delegation or live decision receipt.
The final report adds3 shared-receipt compatibility probes and preserves the
initial walkthrough's missed wording defect in its reconciliation history.

The independent non-producing reviewer inspected the complete candidate,
governing requirements, tests/helper, manifest and actual qualification evidence.
It found one medium wording issue: a generic receipt paragraph prohibited
acceptance/reopening without limiting that prohibition to item answers, even
though the same shape also supports actual lifecycle receipts. The correction
limits the statement to an assumption/question disposition by itself and
explicitly preserves separately authorized lifecycle/exception events. A
focused regression was added; the source agent rechecked affected semantic
cases/probes, preserving prior hashes and the missed finding. The outer scoped
lock, all manifests/hashes and the clean trial were refreshed/re-run against
the correction. [independent-review.json](independent-review.json) records the
reviewers, resolved finding, exact23 reviewed digests, final checks and limits.

### Live project scan limitation

The installed general checker recursively treats nested C Markdown as current
project documents. This partial overlay intentionally omits unchanged pinned
dependencies and retains reusable runtime-relative links, so that raw scan
reports46 missing-link findings. The assembled pinned project resolves those
same references and passes the full validator. The raw failure remains in
[final-project-validation.json](final-project-validation.json); no installed
validator, link destination or integrity guard was changed to hide it. C is
not an installed scaffold. This limits claims to the exact assembled candidate
and scoped source integrity; it is not a passing whole-P validation claim.

### Reached boundary, compatibility and recovery

Original execution items2–4 have actual candidate implementation, bounded
verification and independent-review evidence. Exact qualified inclusions and
future D/S/U mappings/transformations, compatibility, prospective adoption,
migration consequences, dependencies/exclusions, recovery and remaining gates
are in manifest.json and [PRD-001](../../../products/owned-review-decisions.md).
Existing projects retain their recorded governing revisions, item history and
accepted/closed claims until separately authorized adoption/migration. The
project-owned register is additive and conditional; no live register was created.

Candidate scoped locks and fixture locks must not be exported as complete
installed inventories. A future specifically authorized D introduction must
recompare source/destination drift, package the exact reusable manifest, verify
complete directory/runtime links and regenerate only affected full locks after
coherent checks, then run a fresh clean installation trial. Actual development
completion, S promotion and mapped U rollout remain subsequent serial boundaries.
No ordinary Completed, installed introduction, adoption, further merge, push,
publication or release is claimed here. The initiative truthfully remains
In progress at that next delivery boundary.

Recover only by exact declared file identity, retained prior Git content and
current comparison preserving subsequent/unrelated work. The actual candidate
commit is recorded in Git after this evidence is coherent; no future self-hash
is invented in these records. Only the declared C sources/tests and owning P
governance/evidence/product records are committed; all locks outside C are intact.

The first staged whitespace check found two extra EOF blank lines in the newly
copied prompt files that earlier unstaged checks had not covered. Only those
empty EOF lines were removed. Candidate outer-lock digests, exact trial,
manifest and independent/walkthrough identity evidence were refreshed afterward;
the semantic text, prior source words and referenced line contents did not
change. The failed staged check is retained as a correction event, not a pass.
