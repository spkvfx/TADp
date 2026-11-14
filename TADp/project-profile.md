# TADp project profile

**Project:** TADp  
**Status:** Installed and prospectively adopted; role-based ownership recorded  
**Project owner:** Current repository owner (respective owner in a fork)  
**Technical owner:** Current repository owner (respective owner in a fork)  
**Human authority model:** Current repository owner holds human roles unless explicitly delegated; see decisions/OWNERSHIP-001.md  
**TADp project root:** R/TADp/ (verified local path C:/Users/User/PycharmProjects/TADp/TADp)
**Git worktree root:** R (C:/Users/User/PycharmProjects/TADp)
**Project path relative to Git root:** TADp/
**Project-root revision:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6
**Default integration branch:** v1
**Remote operations:** Separate explicit authority required; no remote action performed
**Version scope revision effective point:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6
**Version scope migration ledger:** [Scope migration](initiatives/version-scope-migration-ledger.md)
**Correlation revision effective point:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6
**Correlation migration ledger:** [Initial adoption ledger](initiatives/version-scope-migration-ledger.md)
**Coherence revision baseline:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6
**Work-conflict register:** [Work conflicts](initiatives/work-conflicts.md)
**Keyword revision effective point:** 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6
**Adoption authority:** [ADOPTION-001](decisions/ADOPTION-001.md), 2026-11-14; installation and adoption are separate events
**Last reviewed:** 2026-11-14  

Integration-base authority is [INTEGRATION-001](decisions/INTEGRATION-001.md),
with captured appointment tip `9c9fd1daad655fd58349c005f8d31a4f52790cc9`.

## Purpose

Home for developing TADp with TADp: project evidence, narrow initiatives, candidate protocol work, verification, and completion history. The enclosing protocol/ remains the clean distribution.

## Scope boundary

### Included

- Project governance, evidence, narrow initiatives and historical verification at P.
- Authorized candidate protocol development at C=P/protocol/; exact reusable changes require separate authority.

### Excluded

- R/protocol/ and R/protocol/template/ are upstream distribution targets, not development paths.
- Examples, other projects, external services and releases require separately identified instructions.

## Directory map

| Logical record | Location | What belongs there | Owner |
|---|---|---|---|
| Binding evidence | `evidence/authoritative` | Installed governing LLM suite, kept intact; no candidate replacement becomes authority automatically | Current repository owner; Codex records this setup only |
| Contextual evidence | `evidence/non-authoritative` | Context, realization inputs, and observed setup evidence with original identity | Current repository owner; Codex records this setup only |
| Initiative records | `initiatives` | Canonical independent suites; first allocation TADP-001 in v2 is Proposed | Current repository owner; Codex records actual preparation events |
| Delivered products | `products` or protocol/ (candidate product workspace) | Candidate deliverables and product records when actual workflow events require them | Current repository owner; Codex records this setup only |

## Human ownership and approval

The current repository owner is project owner, accountable technical steward and approval authority unless explicitly delegated. In a fork these roles belong to its respective repository owner. See [OWNERSHIP-001](decisions/OWNERSHIP-001.md) for the exact instruction. This policy is not tied to a personal name or Git author and changes no prior source authority. Record the actual responder and role authority for each future human decision. Prospective adoption is authorized in [ADOPTION-001](decisions/ADOPTION-001.md); the default integration branch is appointed in [INTEGRATION-001](decisions/INTEGRATION-001.md). Scope branches retain distinct roles and captured bases.

This convention applies only to human roles. Preserve every technical
component owner, source authority, external-party dependency, placement,
contract, security, environment, verification, and release gate. Record the
specific human authority whose explicit instruction is required to accept an
initiative, resolve an open decision, change an assumption disposition,
authorize product execution, and authorize publication.

## Authority and traceability

1. evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md governs evidence precedence, protection, decisions, workflow, Git, scope and coherence.
2. decisions/SETUP-001.md (bootstrap event; no initiative exists) authorizes this installation and its local workflow documentation only.
3. protocol/README.md realizes candidate workspace boundary only; no accepted feature or product is claimed.

Record a conflict instead of changing an earlier record to make a later one
appear aligned. Link the conflict to its owner, resolution, and effective date.

## Work identity and correlation

The scope registry initiatives/version-scopes.md owns exact major/minor/patch
scope identity and topology. The initiative index owns one membership row per
initiative, its exact source provenance and current cycle execution assignment.
Scope READMEs and status link those owners; initiative READMEs own lifecycle.
Sources remain non-authoritative and may route to several narrow targets.
Scopes and declared shared scope branches may be reused. Initiative IDs are
independent of scope numbers. Record fit choices, target/source scopes and
LLM authorship under the exact bounded intake delegation before applying them.

Adopt prospectively at the recorded coherent commit. Existing one-to-one
correlation records keep their compatible earlier revision and complete ledger
disposition until explicit evidence-backed migration. Preserve legacy scopes,
paths, branch/base and source identities, historical PR evidence and claims.
Neither synchronization nor scope notation authorizes migration, path moves,
reparenting, acceptance or completion.
## Operating cadence

| Event | Required review | Record to update |
|---|---|---|
| Source intake | Classify standing, precise provenance, limitations and conflicts | evidence/evidence-register.md and original source |
| Actual acceptance or lifecycle event | Verify authority, reciprocal identity, workflow and coherence | initiative README, initiative-index.md and status.md |
| Separately authorized product release | Exact accepted claim, verification, migration and recovery | owning product record and initiative |
| At source, authority or boundary changes | Review owner appointments, adoption, source drift and pending gates | project-profile.md and affected canonical records |
| Initiative alignment or completion | Compare current open effort and affected closed claims; preserve and route incompatibilities | Owning review, completion evidence, and work-conflict register |

The coherence revision baseline identifies the Git commit immediately before
adoption. Historical terminal claims are preserved without retroactive review;
new or changed work follows the adopted coherence rule. Open effort counts as
work to reconcile, not as authority or execution approval. Refine closed claims only after recorded reopening under adopted bounded
intake delegation or separate human authority; coherent same-outcome claim changes may retain identity; independent outcomes
and incompatible type/owner/authority boundaries require separate initiatives.

## Git workflow

### Operating contexts and delivery boundary

Use the same explicit P and C from R or P. Installed `template/` is D; upstream
`R/protocol/template/` is S and `R/protocol/` is U. Follow the
[development guide](docs/development/tadp-development-workflow.md): develop and
qualify exact candidate content in C, introduce specifically authorized proven
work into D, complete the development claim, promote sanitized output into S,
then roll out from its pinned source to the declared applicable U consumers.
These are serial prerequisites, not automatic lifecycle transitions. Keep
historical records, reviews, manifests and recovery outside the clean payload;
never export this project's populated records into reusable sources. Setup
authorizes no future arrow. The [project-local prompt boundary](prompts/AGENTS.md)
remains unchanged and supplies no generic maintenance authority in either context.

The installation source is exactly `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`,
whose working source tree was clean at preflight. Installation and adoption are distinct events; the human explicitly adopted this pinned baseline for the new project in ADOPTION-001. The
[setup receipt](decisions/SETUP-001.md) and
[verification](evidence/non-authoritative/setup/verification.md) own the actual
bootstrap event and evidence. The captured pre-adoption Git snapshot is the commit above, verified immediately before ADOPTION-001. Preserve it on rerun; future adoption is a separately recorded event.

### Shared Git configuration

No `core.hooksPath` is configured. Existing root hook files were inspected and
preserved; installation did not activate or overwrite shared hooks. The installed
hook is copied unchanged. It will treat bootstrap protected additions as changes;
do not bypass it or refresh locks to commit unchanged copies. Coordinate any
future hook activation explicitly at R with the correct P-relative path. Git
user Shawn Kearney supplies commit attribution only. The integration branch is
now `v1` under INTEGRATION-001. That appointment does not allocate a project
scope or authorize any merge; scope branches must have a distinct compatible role.

The project root is the installed scaffold directory, contained in a valid Git
worktree under specification 05. The Git root supplies shared refs, index,
worktree state and hook configuration without widening file ownership.
Record hook coordination and any incompatible branch roles before action.
This project requires Git and recorded dedicated/shared execution per cycle.
Use exact scope branches, major from captured project integration base, minor
from matching major, patch from matching minor, and dedicated member from scope.
Record immutable creation bases and initiative-specific shared-branch evidence.
Human close/finalize instructions supply bounded local immediate-parent merge
authority after all gates; pushes require separate authority.

- **Initiative branch convention:** After adoption use specification 05/09 scope and dedicated/shared assignments; this bootstrap uses setup/tadp-development-project from v1 at 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6 without creating a scope or initiative
- **Required checks:** Protection, structural validation, exact-content provenance and upstream preservation, links, both operating contexts, rerun review, applicable regressions, independent semantic review; see setup verification and development guide
- **Commit requirements:** Scope commits to authorized paths, retain immutable source/base identities and actual checks; no signing policy inferred
- **Merge authority:** Separate exact authority required; no merge authorized by this setup

## Change record

| Date | Change | Reason | Owner |
|---|---|---|---|
| 2026-11-14 | Installed pinned clean project baseline and documented development boundaries; adoption remains pending | Explicit invocation of create-tadp-development-project.md, recorded in decisions/SETUP-001.md | Current repository owner; Codex records this setup only |
| 2026-11-14 | Appointed the current repository-owner role, including respective fork owners | Exact human response in [OWNERSHIP-001](decisions/OWNERSHIP-001.md); prior authorship and source authority preserved | Current repository owner |
| 2026-11-14 | Prospectively adopted source 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6; captured actual pre-adoption HEAD at that same immutable commit | Explicit separate human decision in [ADOPTION-001](decisions/ADOPTION-001.md); no legacy initiatives or scopes to migrate | Current repository owner |
| 2026-11-14 | Appointed v1 as project integration base; earlier unassigned configuration retained in Git and preflight evidence | Exact response `TADp v1` in [INTEGRATION-001](decisions/INTEGRATION-001.md); no scope, acceptance or merge inferred | Current repository owner |
