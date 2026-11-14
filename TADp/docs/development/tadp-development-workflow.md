# Developing TADp in the TADp project

This guide implements the local development contract established by the
explicitly invoked [setup prompt](../../../prompts/create-tadp-development-project.md).
Read the [project instructions](../../AGENTS.md), [profile](../../project-profile.md),
and [governing suite](../../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md)
before work. The suite governs where this guide summarizes it. Apply its
[keyword contract](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
to every request; examples and future procedures are inert until invoked.

## Current installation and authority

The project is named **TADp**, installed at the enclosing repository's
`TADp/` directory from committed source
`6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`. The
[setup receipt](../../decisions/SETUP-001.md) records the actual instruction;
[setup verification](../../evidence/non-authoritative/setup/verification.md)
records the assembly, checks, source identity and limitations. The unchanged
initial protected library is bootstrap material, not newly qualified development.

The current repository owner holds project ownership, accountable technical
stewardship and human approval authority unless explicitly delegated, as
recorded in [OWNERSHIP-001](../../decisions/OWNERSHIP-001.md). In a fork, these
roles belong to that fork's respective repository owner. The policy appoints
a role rather than a particular person; no hosting ownership lookup was
performed, and Git authorship supplies no evidence of current repository control.
Identify the actual role holder or duly recorded delegate when a decision is
required. Historical source authority and decision authorship remain unchanged.

The human explicitly adopted the verified installed baseline prospectively on
2026-11-14 in [ADOPTION-001](../../decisions/ADOPTION-001.md). The governing
source and actual pre-adoption coherence baseline are both immutable commit
`6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`; the latter was confirmed as HEAD
immediately before the adoption receipt. There is no predecessor project
revision or legacy work to migrate. Preserve that baseline and the original
pending-decision history on reruns. Adoption changes no protected source or
lock and accepts no initiative. The upstream structural finding `TADP041`
remains disclosed in setup verification; adoption neither repairs nor waives it.

The project's integration branch is now `v1`, appointed by the exact human
response in [INTEGRATION-001](../../decisions/INTEGRATION-001.md), with captured
appointment tip `9c9fd1daad655fd58349c005f8d31a4f52790cc9`. The earlier unassigned
state remains in setup and preflight history. This appointment does not allocate
a scope or permit v1 to become its own child scope. Before allocation inspect
actual integration configuration and coordinate branch-role collisions rather
than assuming an independent namespace. No feature, initiative acceptance, development
completion, reusable-source introduction, promotion, rollout or release is
established by setup. No historical work is migrated.

## Resolve the project in either operating context

| Identity | Repository-relative location | Role |
|---|---|---|
| `R` | Enclosing Git worktree root | Repository instructions, shared Git metadata and repository maintenance prompts |
| `P` | `R/TADp/` | This installed development project and its governance |
| `C` | `P/protocol/` | Candidate product workspace; no separate scaffold, profile or Git repository |
| `D` | `P/template/` | Protected reusable development library |
| `U` | `R/protocol/` | Existing implementation-ready protocol distribution |
| `S` | `U/template/` | Protected upstream reusable library, prior to mapped rollout |

Resolve the explicitly identified target before any decision or write. From
`R`, the project path is `TADp/` and candidate path is `TADp/protocol/`. From
`P`, they are `.` and `protocol/`. Both must resolve to the same `P`, `C`, Git
root, `D` and `S`. Working directory, an attached file or script location never
selects an upstream target. Resolve junctions and links, reject escaping or
ambiguous paths, and verify the installed markers and Git relationship. Another
scaffold, repository, submodule or worktree remains a separate boundary even
when nested physically inside `P`.

The Git root supplies shared refs, index, history and hooks; it does not enlarge
file authority. Do not initialize nested Git metadata. Retain enclosing
instructions and coordinate shared state before branch or index mutations.
Use `R` for Git operations and the verified `TADp/` prefix for project pathspecs.
Inspect staged, unstaged, untracked and ignored material before mutation;
preserve unrelated work without stashing, moving, discarding or committing it.
Do not activate or overwrite shared hooks implicitly.

Preserve [project-local prompt instructions](../../prompts/AGENTS.md) unchanged.
A stored prompt under `P/prompts/` remains confined to that scaffold and its
narrower declared subject. It cannot maintain generic invariants, reusable
sources, workflow contracts, numbered prompts, validation or protection
behavior, or generic adoption and migration guidance, including candidate
versions under `C`. It may record a possible defect and use installed checks.
Generic protocol development requires an explicitly invoked repository-level
protocol-maintenance instruction identifying the exact work and `C` target,
even when the shell is in `P`. That authority still requires applicable
initiative, type, human-decision and protection gates. Upstream promotion is
always a separately scoped repository operation.

Develop protocol work in `C`. Keep `U` unchanged throughout development and
setup. Read-only upstream inspection may establish provenance or compare a
declared destination. Future authorized promotion changes only `S`; future
authorized rollout changes only its exact mapped consumers in `U`.

## Record and evidence ownership

| Subject | Canonical owner and placement |
|---|---|
| Governance and adoption | `P/project-profile.md`, actual project-wide decisions under `P/decisions/`, and the installed authoritative suite |
| Context and realizations | Original sources under `P/evidence/non-authoritative/`, indexed with standing and precise locators in `P/evidence/evidence-register.md` |
| Scope identity and topology | `P/initiatives/version-scopes.md`; adoption and legacy dispositions in `version-scope-migration-ledger.md` |
| Membership, provenance and execution assignments | `P/initiatives/initiative-index.md`; portfolio status is a linked view in `status.md` |
| Bounded work and lifecycle | The owning initiative's canonical suite; initiative-specific human decisions in its `decision-receipts/` |
| Candidate output | Actual files under `C`, linked from the owning product record without a second authoritative output copy |
| Verification and delivery history | Owning execution/delivery and completion records, with supporting observations under `P/evidence/non-authoritative/` |
| Delivery manifest and recovery | Owning product or work records in `P`, outside the exported payload; reuse canonical records |
| Incompatible work | `P/initiatives/work-conflicts.md` and every affected record; invariant contradictions also follow the authoritative conflict-register procedure |

Canonical record stewardship belongs to the current repository owner or an
explicitly recorded delegate. Recording agents identify their actual authorship
rather than claiming that human role. Each decision receipt identifies the actual
responder, repository-owner or delegated authority, exact words and scope.
Forking creates no authority over upstream repositories, other forks or external
services and does not transfer the authority of historical decisions. Source IDs,
standing, immutable revisions, precise paths or locators, original event and
capture event must survive copying. Proposal input and realization catalogs
remain non-authoritative. Candidate invariant text does not replace the
installed governing suite merely by being written or tested.

Use the [coverage map](../../template/TEMPLATE-COVERAGE.md) for canonical
sources and declared destinations. Instantiate only records triggered by real
events, outside protected sources. Recover necessary documentary prerequisites
through their owning stages from sufficient evidence; missing authority,
identity, work and verification remain blockers. Copying a receipt template
does not produce a human decision. Reuse sufficient actual authority within
its recorded boundary without requesting the same decision again.

## Serial delivery route

The sequence below describes future delivery boundaries. It does not replace
or renumber [workflow stages 0 through 13](../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md#canonical-stage-sequence).
Follow exactly one type-specific delivery path. Qualification, promotion and
rollout describe actual operations, not new lifecycle states. Completion alone
proves neither promotion nor rollout.

1. **Develop the exact candidate in `C`.** Establish one narrow outcome,
   acceptance claim and authority boundary under the actual initiative and
   governing revision. Declare candidate files, authoritative sources,
   intended reusable destinations, downstream consumers, compatibility,
   migration, recovery and verification before delivery. Keep experiments,
   scratch output and proposed replacements outside `D`, `S` and `U`.
   Installed runtime tools and governing sources remain distinguishable from
   candidate replacements. A proposed invariant change requires its own exact
   authorization and remains a proposal until authorized.

2. **Qualify the candidate before introduction into a library.** Verify the
   accepted behavior, affected consumers, relevant failure cases and
   compatibility boundaries. Run applicable structural, protection, link and
   regression checks and a representative clean installation or workflow
   trial. Assemble that isolated trial from the pinned clean baseline plus
   the exact candidate changes and declared dependencies; a small change need
   not contain a full scaffold itself. Do not use undeclared development
   files, excluded material or the live installed project as hidden support.
   Any temporary candidate-fixture lock needs exact applicable authority and
   must be labelled fixture evidence; it cannot refresh a real project lock.
   Record actual commands, configured environment, source content identities,
   results, compatibility/migration/recovery effects and limitations in `P`.
   Preserve failures; skipped, unavailable and unperformed checks are not
   passes. Obtain independent review, reconcile findings, and retain the exact
   tested content and reviewed manifest. An experiment alone is insufficient.

3. **Introduce qualified reusable work into `D`.** Require passed qualification,
   applicable human acceptance gates, a reviewed sanitized manifest, and a
   specific human instruction naming the exact protected reusable-source
   changes. Verify current source/destination content against the tested base,
   resolve drift and apply only the declared payload at its reusable library
   locations. Keep generic placeholders in reusable records. Reconcile affected
   consumers, verify content, and only then refresh specifically authorized
   affected locks. Rerun protection/validation and a clean installation from
   the result. When introduction is part of the accepted deliverable,
   development completion follows this actual delivery; do not demand that
   completion already exist before delivering the accepted output.

4. **Complete development, then promote `D` into `S`.** Before promotion,
   require actual type-specific completion evidence, including qualified
   introduction into `D`. Recorded promotion authority must name that completed
   work, the reviewed manifest, immutable source revision and exact protected
   changes in `S`. Compare current destination with the tested base, preserve
   unrelated changes and reconcile drift before applying sanitized deliverables.
   Verify the resulting upstream template and its isolated installable output;
   update only authorized affected locks after coherent checks. Leave `U`
   outside `S` unchanged during promotion. Record actual writes, resulting
   revision, verification and recovery separately from development completion.
   A substantive defect in completed work requires recorded revision/reopening
   and renewed acceptance, rather than a silent correction during copying.
   Identify all consumers requiring rollout; template promotion cannot establish
   protocol-wide coherence while those consumers remain pending.

5. **Roll out the promoted `S` into mapped consumers in `U`.** After successful
   promotion, require recorded rollout authority naming the exact paths and
   pinned promoted revision. A single sufficiently specific human instruction
   may cover promotion and rollout, with each prerequisite satisfied in order.
   Preview the source-to-destination mapping and conflicts before writes.
   Apply only sanitized, proven work, preserving unrelated content, source
   identity, protection, compatibility and recovery. Do not copy the template
   tree wholesale over `U` or substitute an unpromoted candidate. Reconcile
   and verify affected consumers before refreshing only specifically authorized
   affected locks, then rerun protocol validation, protection and applicable
   regressions. Finish only when every required mapped consumer has a verified
   disposition; record unchanged or inapplicable consumers with their reasons.
   A partial rollout remains incomplete. Honor any requirement for coherent
   sources, consumers, checks and locks at the effective governing commit.
   Rollout alone cannot adopt a revision, migrate live work, accept an initiative,
   establish conformance or release anything. Remote writes, publication and
   release retain separate authority.

## Manifest and clean payload

At every delivery boundary maintain a deliberate inclusion manifest in the
owning product or work record outside the clean payload. Record each included
change with all fields below; a filename or earlier test run is insufficient.

| Manifest field | Required content |
|---|---|
| Work and authority | Exact initiative, accepted claim/baseline, source instruction or receipt, and each authorized delivery boundary/protected change |
| Source identity | Source project, immutable Git revision, file path, digest such as SHA-256, and distinction between tested content and later edits |
| Destination and operation | Exact source-to-destination mapping, add/update/remove operation, destination baseline revision/digest, and current comparison |
| Transformation | Generalization, placeholder treatment, link adjustment or other sanitation, rationale, and resulting exact content identity |
| Verification | Requirements and behavior covered, actual commands/environment, exact tested revision/digests, independent reviewer, findings/dispositions, results and evidence paths |
| Exclusions and dependencies | Excluded development material, declared dependencies and consumers, compatibility/migration requirements, unresolved blockers and responsible owners |
| Recovery and disposition | Prior revision/content, scoped recovery preserving subsequent work, actual resulting revision, operation status, remaining actions and their owners |

Review inclusions explicitly instead of exporting everything not caught by a
blacklist. Retest transformations after sanitation. Recompare source and
destination before the next write; qualification applies only to exact tested
content. Name and review removals explicitly: omission from a payload cannot
authorize deletion of an existing file.

Sanitize exported copies, preserving original evidence and Git history in `P`.
The clean payload contains only approved reusable work and support required to
install or use it: generic record shapes, runtime tools, workflow prompts,
required regression tests/fixtures, operational and migration guidance,
applicable instructions and valid integrity locks. Retain binding protocol
rules, licenses, upstream source identity, revision provenance and essential
historical references needed to interpret the governing baseline.

Keep populated initiative suites, project profiles, realization notes,
acceptance receipts, completion reports, discussions and actual test results
in their owning history. Exclude abandoned designs, scratch files, logs,
caches, environments, sync state/backups, editor state, machine-specific paths,
credentials and unrelated products from the payload. Classify by role: a
polished development report is still history; a fixture required for regression
coverage may be reusable work product. Do not purge upstream history, rewrite
an authoritative source, erase conflicts or invent empty history as sanitation.

Review for project-specific IDs, owners, active conflicts, test outcomes,
absolute paths, local configuration and links into excluded material. Generalize
instance values where their reusable role requires it without replacing binding
authority or genuine provenance with fictional placeholders. Verify links and
installation in isolation; the payload must not depend on this machine, live
project records or unexported temporary files. New instances inherit no live
work, appointment, acceptance or test outcome from this project.

## Role-based rollout mapping

The examples below explain source roles and supply no authority for a change.

| Reusable source | Possible consumer and handling |
|---|---|
| `S/project/tools/tadp_validate.py` | `U/tools/tadp_validate.py` when declared; verify imports, dependencies and regressions |
| `S/project/prompts/AGENTS.md` | `U/prompts/AGENTS.md`; retain project-local restrictions and compatible local requirements |
| `S/project/evidence/authoritative/LLM/` | Exact authorized files in `U/evidence/authoritative/LLM/`; preserve invariant authority, provenance, consumers and governed locks |
| `S/prompts/WORKFLOW-CONTRACT.md` | Already the protected workflow source at `U/template/prompts/WORKFLOW-CONTRACT.md`; no duplicate in project-local `U/prompts/` |
| Reusable `.template.md` shapes | Remain reusable; instantiate only on an actual separately governed record-creation trigger |

Recompute links when placement changes and merge entry-point requirements
without discarding them. Preserve placeholders at reusable destinations;
resolve them for actual instances only from sufficient evidence. Record why
each declared consumer changed, remained unchanged or was inapplicable.

## Checks, reporting and recovery

Use the project's configured Python SDK. Before execution, obtain its actual
executable through the Python environment tooling and assign that returned
path to `$TadpPython`; no machine-specific executable belongs in reusable work.
The following PowerShell commands are illustrative read-only checks after
resolving `$RepositoryRoot` to the verified `R`. They are not results or an
instruction to activate future work merely by reading this guide.

```powershell
# From R, with RepositoryRoot equal to that resolved directory:
& $TadpPython TADp/tools/tadp_protect.py check TADp
& $TadpPython TADp/tools/tadp_validate.py TADp
git -C $RepositoryRoot rev-parse --show-toplevel
git -C $RepositoryRoot status --short --branch

# From P, with the same explicit project identity:
& $TadpPython tools/tadp_protect.py check .
& $TadpPython tools/tadp_validate.py .
git -C $RepositoryRoot rev-parse --show-toplevel
```

Record the exact expanded commands, interpreter/version, working directories,
roots, revisions, outputs, exit codes and limitations in the owning verification
record. Run only applicable regression commands for the declared change and
record their actual source. The initial clean scaffold's `tests/` contains
navigation; upstream baseline regressions may be exercised as pinned external
verification without importing their history or claiming new project tests.
Compare preflight and final upstream manifests, including all locks, to prove
preservation during setup. Distinguish inherited baseline findings from new
failures, structural checks from semantic review, and unavailable checks from
passing evidence. Independent review must inspect the complete scoped diff and
have its findings reconciled or explicitly reported unresolved.

Before qualification, completion or refinement, inventory relevant proposed,
accepted and partially performed work and affected closed claims. Record
incompatible efforts in every affected project's work-conflict register and
affected records without promoting proposal authority. Follow specification
10's completion feedback review. Record required authorized reopening before
changing a closed claim; adopted specification 09 intake can delegate necessary
placement/reopening with actual agent authorship, but does not grant acceptance.
Same-outcome revision may retain identity; independent outcomes or incompatible
type, ownership or authority boundaries need separate initiatives. Changed
accepted claims require renewed human acceptance and fresh verification.

Reruns inspect the existing installation, receipt, adopted state, records and
content identities first. Reuse valid records and sufficient decisions;
preserve customization and history. Do not create another project, duplicate a
receipt, reset adoption, overwrite current work or create an empty commit.
Changed source or destination content requires current comparison and checks.

Recover through the manifest's retained prior content and scoped comparison,
preserving subsequent and unrelated changes. An observed failure is not
permission to refresh locks, erase evidence, disable guards or expand cleanup.
Record partial operations and retained backups, stop only affected work, and
resume after its precise authority/check/reopening conditions hold. No merge,
push, branch deletion, publication or release follows from this guide alone.
