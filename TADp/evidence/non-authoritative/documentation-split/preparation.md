# Repository / protocol documentation split preparation

Recorded by Codex on 2026-11-14. This is non-authoritative preparation evidence,
not an initiative, acceptance receipt, execution record or completion record.

## Source, authority and baseline

The human instruction was `execute this prompt`, identifying
`prompts/separate-repository-and-protocol-documentation.md` twice (one invocation).
Source revision: `014d455e3d99213e0dc4a156cb198ac1a4a85747`.
The prompt's Governing instructions and targets authorizes bounded candidate
preparation and named repository support documentation, retaining acceptance
and all later delivery boundaries. No keyword or gate exception is activated.

Resolved R: `C:/Users/User/PycharmProjects/TADp`; P: `R/TADp`;
C: `P/protocol`; D: `P/template`; U: `R/protocol`; S: `U/template`.
All are existing ordinary directories in the same Git worktree. At preflight,
HEAD was the source revision above; branch was
`docs/separate-repository-protocol-docs-prompt`; staged, unstaged and untracked
inventories were empty. `.gitignore` contains editor/Python exclusions only;
the intended support/candidate/evidence paths are not ignored. No configured
`core.hooksPath` was found. Existing branch roles and integration conventions
are not changed by this preparation.

P's adopted governing source is `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`
under ADOPTION-001. SETUP-001, OWNERSHIP-001 and ADOPTION-001 contain no acceptance
or delivery authority for this split. P's integration branch is unassigned;
scope and initiative registries, status and work-conflict register have no
allocated work. No open initiative or affected closed P claim exists to refine
or reopen. The current preparation itself counts as proposed effort on rerun.
Upstream history is not imported as P initiative membership. No incompatible
work was identified; baseline validation findings are observations, not a
new accepted requirement or permission to edit governing records.

## Effective settings and serial ledger

Source blocks: Procedure items 1 through 6 in the pinned prompt, in written
order. Each has human_gates=true, other_gates=true, preview=false, local=false,
review=false. Independent review is nevertheless expressly required by item 4.
Parent: this single prompt invocation; no retry or resumed invocation yet.
Tables are reference inventories, not parallel action lists. Read-only
baseline inspection can run concurrently within item 1; shared writes are
serialized. Items 1 and 2 precede draft preparation; item 4 qualifies drafts;
item 5 must stop at missing exact boundary authority, so item 6's delivered
result cannot be claimed. Verification/reporting of the preparation remains
authorized. No switch, waiver or alternative lifecycle is inferred.

## Baseline checks

Configured SDK discovered through PyCharm: Python 3.11.1 at
`C:/Users/User/PycharmProjects/TADp/.venv/Scripts/python.exe`.
Commands below ran from R with that executable, after environment discovery.

| Arguments | Exit | Observed result |
|---|---|---|
| `TADp/tools/tadp_protect.py check TADp` | 0 | 0 errors |
| `TADp/tools/tadp_validate.py TADp --json` | 0 | 0 errors, 0 warnings |
| `protocol/tools/tadp_protect.py check protocol` | 0 | 0 errors |
| `protocol/tools/tadp_validate.py protocol --json` | 1 | Existing TADP041: adopted coherence baseline missing/disabled at project-profile.md |

Full baseline regressions were started from U using the same configured SDK,
`-m unittest discover -s tests`; final result is recorded in verification.
TADP041 also appears in setup history and is outside this documentation scope.
No lock, validator, profile or hook change is authorized to conceal it.

## Exact move and consumer map

All inspected source content is pinned by the source revision above. Original
files remain recoverable in Git; no distribution deletion is performed during
preparation. Draft byte identities and per-destination baseline identities
are recorded in manifest.json after qualification. Candidate sources use
`.md.in` to distinguish uninstalled fragments from governing project docs;
assembly strips only `.in`. This avoids treating fragment-relative links as
links into P's governance. No full scaffold is installed in C.

| Source / section | Candidate under C/documentation/ | Reusable D, then S path (relative to each library) | Rollout U path | Operation / rationale |
|---|---|---|---|---|
| U/README.md: overview, adoption, indexes; mixed contributor section | `README.md.in` | `project/README.md` | `README.md` | Split; retain portable overview, consolidate installation in getting-started |
| U/docs/README.md: index | `docs/README.md.in` | `project/docs/README.md` | `docs/README.md` | Split into portable project index and R/docs index |
| U/docs/development/getting-started.md | `docs/development/getting-started.md.in` | `project/docs/development/getting-started.md` | `docs/development/getting-started.md` | Split maintenance section to R/docs; expand one canonical installation procedure |
| U/docs/development/repository-layout.md | `docs/development/repository-layout.md.in` | `project/docs/development/repository-layout.md` | `docs/development/repository-layout.md` | Retain portable record ownership; move checkout layout to R/docs |
| U/docs/development/git-and-codex-requirements.md | `docs/development/git-and-codex-requirements.md.in` | `project/docs/development/git-and-codex-requirements.md` | `docs/development/git-and-codex-requirements.md` | Retain project requirements; remove reference-checkout framing |
| U/docs/development/validation-and-quality.md | `docs/development/validation-and-quality.md.in` | `project/docs/development/validation-and-quality.md` | `docs/development/validation-and-quality.md` | Split validator-authoring and checkout hook details into R/docs |
| U/docs/development/developing-tadp.md | `docs/development/developing-tadp.md.in` | `project/docs/development/README.md` | `docs/development/developing-tadp.md` AND `docs/development/README.md` | Compatibility pointer with original anchors; reusable location is allowed by inspected sync PROJECT_USE_GUIDES; do not add unsupported developing-tadp.md to library |

The last row is a role-based mapping, not a wholesale directory sync. Both U
consumers use identical portable pointer bytes. D/S `project/docs/development/README.md`
already exists; its prior navigation is retained by links in the replacement.
All other mapped reusable files also already exist: this is an exact update
proposal, not permission to overwrite them. Sources differ from U and require
their own baseline comparisons. No protected write or refresh occurs now.

Repository support map (applied preparation, not exported): R/README.md becomes
a brief entry point; R/docs/README.md owns repository navigation;
R/docs/repository-layout.md owns checkout structure;
R/docs/developing-tadp.md owns contributor setup, maintenance prompts,
distribution route, extracted maintenance explanations and check limitations;
R/docs/implementing-tadp-in-projects.md links to the portable installation guide.
The supplied separate example link and clone URL are preserved. Root navigation
must disclose that portable revisions are prepared, not delivered.

## Incoming consumers and preservation

Searches cover the scoped checkout, including tools, tests, instructions,
templates and historical records. U README/docs index link the old development
guide and layout; tools/tadp_validate.py and its protected embedded copies
name the compatibility development path as a legacy required path. Existing
tests reference it too. Retain the path and every original heading anchor;
do not edit excluded code/tests to remove those consumers. Preserve all
headings of split guides where practical. No anchor rename is required.

Protected copies under D/project/docs and S/project/docs, their locks,
instructions, and historical setup reports/manifests are read-only consumers.
P/docs continues to describe its adopted baseline; it is not a second rollout
target. Historical path strings retain their original identity. No AGENTS.md,
stored prompt, test, tool, configuration, license, authoritative source,
populated history, example or other project is relocated or revised.

## Qualification and recovery plan

Assemble isolated Git-root and nested installations from immutable Git blobs:
complete U/template library; U/template/project contents including dotfiles,
excluding only its nonrecursive template/README placeholder; U authoritative
suite, docs, tools and required tests at the corresponding project paths.
Overlay only the seven candidate source files at their declared runtime
destinations (plus the compatibility index). Do not change either fixture lock:
the fixture library retains the pinned baseline. This tests portable runtime
documentation and the manual component map, not yet library introduction or
the synchronization of an approved revised library. No R/docs or populated P
records may supply hidden dependencies. Run protection, structure, link/anchor
checks and applicable existing regressions; independently review the exact diff.

Keep fixture logs and hashes in P; temporary installation trees remain outside
the live checkout. No fixture creates project adoption, owner appointments,
acceptance or actual initiative work. For recovery, compare manifest hashes
and restore only this preparation's exact paths from the pinned Git baseline
or retained draft bytes, preserving subsequent edits. Do not auto-rollback.

## Pending boundary decisions

First establish P's actual integration configuration and scope/execution
placement through the owning workflow; do not infer it from existing v1 or
this prompt branch. Prepare and align the canonical implementation initiative
for this single audience-separation outcome, resolve its human gates, and
obtain explicit acceptance of its exact baseline. This preparation supplies
no lifecycle state or standard completion record.

Only after qualification and acceptance may an exact instruction authorize
the seven mapped D/project sources and the affected D template lock. After
actual introduction and development completion, a later instruction must name
the immutable completed source and exact S changes and affected lock; then
authorize the eight mapped U consumers from the pinned promoted source.
One sufficiently specific instruction may cover promotion and rollout, with
all prerequisites met in sequence. No invariant/LLM lock change is proposed.
No merge, push, PR, release, publication, deployment or adoption is performed.

## Qualification corrections (preserved observations)

The first trial attempted to execute a generated local PowerShell script file;
the machine's script policy rejected it before assembly. The wrapper initially
continued missing-file checks and returned 0 despite their failures. Those
results are retained as attempt 1 and are not passing evidence. The evidence
runner was corrected to stop dependent checks after assembly failure and to
return a nonzero aggregate result. It now exercises the example as inline
PowerShell commands, changing no execution policy or shared configuration.

Attempt 2 assembled both installations but exposed TADP025: overlaying U's
separately locked authoritative suite on the scaffold's embedded suite left
an unrecorded README.md. This is a finding in the proposed installation
procedure, not drift in a live protected source. The draft map and example
were corrected to retain the complete `template/project/evidence/authoritative/LLM/`
suite and its matching lock already supplied by the scaffold copy. No suite
overlay or lock refresh is performed. The isolated trial uses that corrected
source selection; the earlier qualification plan above is preserved as history.
