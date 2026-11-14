# Installation-root protocol maintenance

## Authority and baseline

Record ID: ROOT-DR-001. Captured 2026-11-13 by Codex from the User's
instruction, `execute this prompt`, identifying
`prompts/project-root-installation-directory-protocol-change.md` (the same
attachment appeared twice). This is one execution of that exact prompt.
The prompt is preserved at repository revision
`fc0c8e3ea01471d3a35f06a29d96f837070afd70`; its authorization inventory and
required root definition are the exact bounded revision authority. No directive
switch is active. Specification 11 defaults apply throughout all five serial
procedure items: human_gates=true, other_gates=true, preview=false, local=false,
review=false. No gate exception or live initiative decision is inferred.

The selected maintenance root is `protocol/`, in Git worktree
`C:/Users/User/PycharmProjects/TADp`, branch `v1`, baseline commit above.
Git identity is Shawn Kearney, `shawn@splicehere.com`; no configured hooksPath
was returned. The baseline has 276 unstaged tracked deletions under
`_old/example/`, no staged paths, and no nonignored untracked files. These
unrelated deletions and `.gitignore` are preserved. Specification 05 requires
a clean worktree for new branch creation, so this bounded maintenance uses the
existing branch and path-specific commits; no branch switch, merge or push
is authorized or performed.

Baseline commands with the configured `.venv/Scripts/python.exe`:

- `protocol/tools/tadp_protect.py check protocol`: exit 0, zero errors.
- `protocol/tools/tadp_validate.py protocol`: exit 1, two TADP002 errors for
  historical `example/` links in the design initiative's `architecture.md:46`
  and `source-mapping.md:23`; one TADP033 Deferred legacy migration warning.
  No baseline lock drift exists. These records are not revised by this task.
- Full regression baseline, `-m unittest discover -s protocol/tests -v`:
  249 tests in 169.304 seconds, OK, three environment skips, exit 0.
  The process loaded its modules before the source changes and used isolated
  fixtures; these are baseline results, not verification of the revision.

## Exact pre-edit inventory and execution ledger

The following is a coverage inventory, not an operative action list. Procedure
items 1 through 5 execute serially. Within item 2, independent agents own
disjoint sync, Git-path and documentation consumers; their settings are the
same defaults above. The root agent owns the invariant and reconciliation.
Every branch joins before item 3 verification and item 4 lock refresh. No retry
changes the source, target or authority. This record is also the authority
reference for the two affected outer locks; it does not authorize a refresh
before reviewed content and focused verification.

Owning sources and conflict history:

- `protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md`
- `protocol/evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md`
- `protocol/evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md`
- Their installed reusable counterparts under
  `protocol/template/project/evidence/authoritative/LLM/`, with the clean
  reusable conflict register remaining free of maintenance history.
- `protocol/evidence/authoritative/LLM/.tadp-lock.json`
- `protocol/template/.tadp-lock.json`
- `protocol/template/project/evidence/authoritative/LLM/.tadp-lock.json`
  (embedded suite lock, refreshed before the enclosing template lock).

Runtime and fixture consumers:

- `protocol/tools/tadp_sync.py`
- `protocol/tools/tadp_validate.py`
- `protocol/tools/tadp_scopes.py`
- `protocol/tools/tadp_protect.py` (project-root CLI help and read-only import
  handling, identified during the Git-path branch's consumer reconciliation).
- Corresponding exact filenames under `protocol/template/project/tools/`.
- `protocol/template/project/.githooks/pre-commit`
- `protocol/.githooks/pre-commit` (working scaffold counterpart discovered
  during final consumer review, before updating it).
- `protocol/tests/test_tadp_sync.py`
- `protocol/tests/test_tadp_validate.py`
- `protocol/tests/test_tadp_scopes.py`
- `protocol/tests/test_tadp_protect.py`
- `protocol/tests/test_tadp_project_roots.py` (new focused nested fixtures).

Documentation and instructions:

- `README.md`
- `protocol/README.md`
- `protocol/AGENTS.md`
- `protocol/prompts/AGENTS.md`
- `protocol/tools/README.md`
- `protocol/docs/README.md`
- `protocol/docs/development/getting-started.md`
- `protocol/docs/development/git-and-codex-requirements.md`
- `protocol/docs/development/repository-layout.md`
- `protocol/docs/development/validation-and-quality.md`
- `protocol/docs/development/adapting-other-tools.md`
- This maintenance record.
- `protocol/docs/guides/project-local-prompts-migration.md`
- `protocol/docs/guides/project-root-installation-migration.md` (new).
- `protocol/template/TEMPLATE-COVERAGE.md`
- `protocol/template/README.md`
- `protocol/template/project/README.md`
- `protocol/template/project/AGENTS.md`
- `protocol/template/project/project-profile.template.md`
- `protocol/template/project/prompts/AGENTS.md`
- `protocol/template/project/tools/README.md`
- `protocol/template/project/docs/development/getting-started.md`
- `protocol/template/project/docs/development/git-and-codex-requirements.md`
- `protocol/template/project/docs/development/validation-and-quality.md`
- `protocol/template/project/docs/guides/project-local-prompts-migration.md`
- `protocol/template/project/docs/guides/project-root-installation-migration.md`
  (new).
- `protocol/template/project/docs/guides/README.md`

Protection and reset tools were inspected: staged protection already maps
project paths to Git paths; its CLI help and bytecode behavior are reconciled
with project-root read-only checks. Reset already selects the installed script's
project and reports its Git context. They retain their target contracts.
Any newly discovered necessarily affected path will be recorded before editing.

## Revision disposition

Replace only specification 05's requirement that a project equal a repository
root: project root P is the resolved scaffold installation destination and
must be contained in valid worktree G. Preserve mandatory Git, historical
source revisions, evidence authority, identity, lifecycle, acceptance, branch
rules and the project-local maximum file boundary. No separate `.git` entry
at P is needed. Installation/synchronization does not adopt this revision.

The selected sync contract is explicit `--target DIRECTORY`, otherwise exact
cwd. The destination must already exist within a valid worktree. No ancestor
search or script-directory redirection selects a sync destination. Verified
project-local prompts retain their own parent-of-prompts root. Conflicting
contexts, protected template sources and unsafe paths block affected writes.

The effective event is the first coherent commit containing this record,
the revised sources, reconciled consumers, verification and authorized locks.
Its immutable hash is discoverable through this record's Git history.
Earlier projects retain their recorded governing revision until explicit
prospective adoption with captured baseline and impact record. No live file
move, adoption, reopening, initiative acceptance, completion or release occurs.

## Verification and final review

Step 2's disjoint consumer branches joined before aggregate verification.
The sync branch's focused pre-lock run passed 52 tests in 22.393 seconds,
with three symlink-privilege skips, exit 0 (the full-current-distribution case
requires the reviewed locks and is exercised after refresh). The existing
validator suite passed 80 tests in 80.507 seconds, exit 0. The initial nested
suite passed 10 tests in 12.427 seconds; subsequent review added more boundary
cases, whose final results are recorded below.

Independent reviewers checked the invariant/documentation and runtime deltas.
Review corrections include rejecting ambiguous uninstalled default children
without blocking valid installed nested roots, recognizing incomplete manually
installed scaffolds without requiring sync state, preserving source-side rename
inspection with `--no-renames`, inspecting imported commit history even when
outside-project edits were reverted, checking deleted gitlinks, and retaining
read-only CLI behavior without target bytecode caches. Ordinary restoration
after a protected rename is caught by existing dirty-file/lock checks; the
added fixture tests the narrower ignored-restoration case, where the source
side must be inspected explicitly. A copied guide's unrelated regression-suite wording was
restored to preserve the clean scaffold's original project-owned verification.

Transient fixture failures were repaired and retained as observed development
history: linked-worktree checkout converted sentinel newlines, so tests now
compare actual pre-apply bytes; an isolated conflict fixture needed its explicit
empty-register phrase. Neither required weakening a protocol gate.

Final aggregate results and exact changed paths follow before the scoped
maintenance commit. Remaining shared-ref/index/hook coordination is manual;
no hook is configured or enabled by this maintenance.

Final nested-root focused run:
`-m unittest discover -s protocol/tests -p test_tadp_project_roots.py` passed
16 tests in 19.034 seconds, exit 0, with no skips. It includes actual manual
Git Bash invocation of the nested installed hook with relative Git/index
environment, preservation of unrelated staged work, read-only CLI snapshots,
old/new gitlink history and portable Git-index symbolic-link rejection.
Three independent reviews (documentation/invariant, sync and Git-path branches)
found no remaining blocking issue after reconciliation. The root agent reviewed
every protected delta against the captured baseline; only inventoried root/path
sources and clean-source consumers changed. No unrelated lock drift is absorbed.

The existing scope regressions also passed:
`-m unittest discover -s protocol/tests -p test_tadp_scopes.py`, 24 tests in
49.168 seconds, exit 0. The three inventoried locks were then refreshed with
authority `ROOT-DR-001: protocol/docs/development/project-root-installation-maintenance.md`,
embedded suite first, then outer suite/library. All refresh commands exited 0.

### Concurrent work and isolated final verification

During final verification another actor added
`protocol/tests/test_tadp_sync_local.py` and changed
`protocol/tools/tadp_sync.py`, `protocol/tools/README.md` and the sync test
helpers in `protocol/tests/test_tadp_sync.py` for a distinct
local-template authority/refresh feature. None of those additional changes is
authorized by this maintenance prompt. Their working content is preserved.
The root-change sync version is retained in the matching protected embedded
runtime. The documentation and sync agents reconstructed their own final tools
README and tests into temporary files, comparing the remaining working deltas
to the other actor's feature. Partial staging commits only root-change versions.
The unrelated test stays untracked and outside this commit.

Final aggregate verification therefore uses an isolated local history clone
at `C:/Users/User/AppData/Local/Temp/tadp-root-verification-4b357f7adc2146ffa896d7d7b5e4c5c2`.
It contains the scoped source snapshot, the root-change sync runtime/README,
and inert baseline prompt records required by historical links; it excludes
the concurrent test and creates no example mirror. The original mixed-worktree
test run is not qualification evidence for this change. An initial validation
of the snapshot lacked those inert prompts and reported seven extra missing
links; restoring the baseline prompt records removed those fixture omissions.
Subsequent full validation with the captured `--base-ref` reports exactly the
baseline two TADP002 errors and one TADP033 warning, exit 1. Protection passes
with zero errors, exit 0. No introduced validation or link findings remain.

The mixed-worktree run reported 286 tests, one error, four skips, exit 1 in
302.380 seconds (backup expectation under the concurrent feature). The first
snapshot run still contained that actor's modified helper: 277 tests, six
failures from unsupported local-template flags, four skips, exit 1 in 207.819
seconds. Those failed runs remain recorded. Restoring only our intended test
helpers in the snapshot removes the cross-task interface mismatch; the final
snapshot run's actual result follows. No working file belonging to the other
actor was restored or overwritten.

Staged snapshot whitespace review and its exact-authority protected-update
guard both exited 0. The staged snapshot contains 48 scoped files. No example,
live profile, initiative, adoption, branch assignment or lifecycle record is
included. The clean reusable conflict register remains unchanged.

Final isolated full regression command:
`C:/Users/User/PycharmProjects/TADp/.venv/Scripts/python.exe -m unittest discover -s protocol/tests`
from the snapshot root: 277 tests in 188.011 seconds, OK, four platform skips,
exit 0. This includes the actual locked distribution's nested
preview/apply/rerun and installed validation/protection fixture. This result
qualifies the scoped commit, not the concurrent local-template feature.

Full protocol validation, including local Markdown links and the captured
base-ref comparison, remains exit 1 with exactly the two baseline errors and
one baseline warning; no check is waived or relabeled as passing. Existing
INV-CONFLICT-001/002 remain outside this root revision and need separately
specific maintainer authority. INV-CONFLICT-004 records the authorized root
revision and takes its final disposition at the coherent commit event.
Shared branch-role inventory and manual hook coordination remain adopter
obligations. No remote sync, push, merge, PR, live adoption or release occurs.

### Exact final changed paths

The following is the reviewed commit inventory; initial inventory entries not
listed here were inspected without changes.

- `README.md`
- `protocol/.githooks/pre-commit`
- `protocol/AGENTS.md`
- `protocol/README.md`
- `protocol/docs/README.md`
- `protocol/docs/development/adapting-other-tools.md`
- `protocol/docs/development/getting-started.md`
- `protocol/docs/development/git-and-codex-requirements.md`
- `protocol/docs/development/project-root-installation-maintenance.md`
- `protocol/docs/development/repository-layout.md`
- `protocol/docs/development/validation-and-quality.md`
- `protocol/docs/guides/project-local-prompts-migration.md`
- `protocol/docs/guides/project-root-installation-migration.md`
- `protocol/evidence/authoritative/LLM/.tadp-lock.json`
- `protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md`
- `protocol/evidence/authoritative/LLM/03_Codex_Invariant_Conflict_Register.md`
- `protocol/evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md`
- `protocol/prompts/AGENTS.md`
- `protocol/template/.tadp-lock.json`
- `protocol/template/README.md`
- `protocol/template/TEMPLATE-COVERAGE.md`
- `protocol/template/project/.githooks/pre-commit`
- `protocol/template/project/AGENTS.md`
- `protocol/template/project/README.md`
- `protocol/template/project/docs/development/getting-started.md`
- `protocol/template/project/docs/development/git-and-codex-requirements.md`
- `protocol/template/project/docs/development/validation-and-quality.md`
- `protocol/template/project/docs/guides/README.md`
- `protocol/template/project/docs/guides/project-local-prompts-migration.md`
- `protocol/template/project/docs/guides/project-root-installation-migration.md`
- `protocol/template/project/evidence/authoritative/LLM/.tadp-lock.json`
- `protocol/template/project/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md`
- `protocol/template/project/evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md`
- `protocol/template/project/project-profile.template.md`
- `protocol/template/project/prompts/AGENTS.md`
- `protocol/template/project/tools/README.md`
- `protocol/template/project/tools/tadp_protect.py`
- `protocol/template/project/tools/tadp_scopes.py`
- `protocol/template/project/tools/tadp_sync.py`
- `protocol/template/project/tools/tadp_validate.py`
- `protocol/tests/test_tadp_project_roots.py`
- `protocol/tests/test_tadp_sync.py`
- `protocol/tests/test_tadp_validate.py`
- `protocol/tools/README.md`
- `protocol/tools/tadp_protect.py`
- `protocol/tools/tadp_scopes.py`
- `protocol/tools/tadp_sync.py`
- `protocol/tools/tadp_validate.py`
