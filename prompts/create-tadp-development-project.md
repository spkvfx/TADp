# Establish the TADp development project and controlled promotion workflow

Create a new TADp-governed project named **TADp** in this repository. It is
the home for TADp development effort, including its evidence, initiatives,
candidate work, tests, and completion records. Establish the project and the
workflow below; do not implement an unrelated protocol feature or promote
existing work merely because this project now exists.

Creating, reading, or linking this prompt does not execute it. Execute it only
when a human explicitly invokes it. Future template introduction, promotion,
and rollout require an instruction identifying their exact work and targets.

## Governing instructions and authority

Read the repository-root `AGENTS.md`, [repository prompt instructions](AGENTS.md),
`protocol/AGENTS.md`, applicable directory instructions, and the
[invariant-suite index](../protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
Apply all governing specifications, beginning with the canonical
[prompt keyword specification](../protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
References and examples remain inert. This prompt activates no gate exception.

Explicit invocation authorizes establishing the new project, its local
development workflow, and the necessary repository entry-point guidance. It
does not authorize a substantive invariant revision, an unspecified reusable
source change, initiative acceptance, migration of existing work, or a release.
Preserve protected sources and their locks when copying the initial baseline.
Record required human authority and actual decisions without inventing them.

## Project and source identities

Resolve and record the following paths before writing. This table is a
reference inventory, not a parallel action list.

| Identity | Location and responsibility |
|---|---|
| Repository `R` | Verified enclosing repository containing this prompt and the existing `protocol/`. Discover its actual Git worktree root and branch. |
| Development project `P` | `R/TADp/`, with project name **TADp**. This is a separate installed project beneath the repository root, not a rename of `R/protocol/`. |
| Development protocol scope `C` | `P/protocol/`, an explicitly declared candidate product workspace. Develop protocol work here before introducing it into reusable sources. It is not another installed project or an authoritative baseline. |
| Development project's template `D` | `P/template/`, the project's protected reusable library. Candidate drafts and experiments belong outside this directory. |
| Actual protocol `U` | Existing `R/protocol/`. This remains the actual distributable protocol and is not the development workspace. |
| Protocol's template `S` | `R/protocol/template/`, the sole upstream write destination in the promotion workflow described here. |
| Downstream template target `T` | The exact template distribution or installation explicitly identified by a later rollout instruction. Do not assume a repository-root `template/`, another repository, a remote branch, or an installed project. |

Use the project-root definition in
[specification 05](../protocol/evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
The enclosing Git worktree provides shared history, refs, index, and hook
configuration without widening project ownership. Do not initialize a nested
Git repository. Reject ambiguous targets, escaping links, and collisions with
existing projects. Reuse a verified prior installation on rerun; do not
overwrite or silently adopt an unrelated directory.

**Do not modify `U` directly during setup or development.** This includes its
working files, authoritative suite, tools, tests, documentation, live records,
and reusable sources. Later, separately identified promotion may change only
`S` through the proven-work route below. That is a controlled exception to the
development write boundary, not permission to experiment in `U` or change its
other paths. If a coherent revision needs other upstream changes, report the
exact dependency and obtain a separately scoped instruction before promotion.

## Conformant development and context handling

Install `P` from the verified local protocol baseline using the canonical
[installation guidance](../protocol/docs/development/getting-started.md) and
[template coverage map](../protocol/template/TEMPLATE-COVERAGE.md). Record the
actual immutable source revision and distinguish any uncommitted source drift.
Do not package a dirty source tree as though it were that committed revision.
Keep the installed governing suite and protected library intact. Instantiate
the project profile and required coordination records outside `P/template/`,
using actual ownership, authority, adoption, Git, and verification evidence.
Missing owner or adoption decisions remain explicit; copying alone does not
prove adoption or full conformance.

Use narrow initiatives with one outcome and acceptance claim, canonical source
records, exact realization provenance, scope membership, recorded execution
assignments, and traceable commits. Preserve human decision and acceptance
gates and follow exactly one declared type-specific delivery path. Include
proposed, accepted, and partial effort in coherence reviews; record conflicts
in each affected project's canonical registers. Apply completion feedback and
record authorized reopening before refining closed claims. Changed accepted
claims require renewed acceptance.

Work may be invoked from `R` or from within `P`. Resolve the same explicit
project and candidate scope in either context; current working directory alone
does not select a target or grant upstream authority. Place project governance
and historical evidence at `P`, candidate deliverables at `C`, and declare the
precise mapping from candidate files to eventual reusable destinations.
Template drafts in `C` are product candidates, not editable aliases of `D` or
new governing authority. Protected copies remain protected wherever applicable.

Preserve the installed `P/prompts/AGENTS.md` boundary. Project-local prompts
must not acquire generic protocol-maintenance or outside-project authority.
Use an explicitly invoked repository-level protocol-maintenance instruction
for generic protocol changes, even when the shell is inside `P`. Upstream
promotion is always a separately scoped repository operation. Do not weaken
canonical project-local restrictions to make context switching convenient.

## Development, qualification, promotion, and rollout

Document and enforce this serial route in the new project's instructions and
development guide. These are future work contracts, not instructions to invent
or promote a feature during project setup.

1. **Develop in protocol scope.** Create and revise candidate work in `C`
   under the applicable initiative, specific change authority, and workflow
   gates. Keep experiments, proposal drafts, logs, and temporary outputs out
   of `D`, `S`, and `T`. A proposed invariant change remains a proposal until
   its exact revision is authorized; candidate status cannot bypass an
   applicable governing invariant.
2. **Validate and test before template introduction.** Verify candidate
   behavior and its consumers against the accepted claim. Run applicable
   structural and protection checks, regression tests, link checks, and a
   representative clean installation or workflow trial in isolated fixtures.
   Record actual commands, environment, source revision, results, limitations,
   compatibility, migration, and recovery effects in `P`. Retain failures;
   skipped or unavailable checks are not passes. Obtain independent review
   and reconcile its findings before qualification.
3. **Introduce proven work into `D`.** Require passed candidate qualification,
   applicable acceptance gates, and a reviewed, sanitized file manifest
   identifying exact source revisions, destinations, changes, exclusions,
   and verification. A specific
   human instruction must authorize the exact reusable-source change before
   editing protected `D`. Reconcile affected consumers and refresh only the
   specifically authorized affected locks after content verification. Recheck
   protection and validation and exercise a clean installation from the result.
4. **Promote completed work from `D` into `S`.** Require actual completion
   evidence for the development work, including its qualified introduction
   into `D`. A separate promotion instruction must identify that completed
   work, the qualified manifest, source revision, and exact protected-source
   changes. Compare the current destination with the tested
   base, preserve unrelated work, and reconcile drift before applying only
   those sanitized deliverables. Verify the resulting protocol template and
   its installable output with isolated fixtures. Update only affected locks
   under the same exact authority after coherent verification. Keep `U`
   unchanged outside `S`. A dependency outside `S` blocks this promotion until
   separately authorized and verified; do not ship an incoherent template.
5. **Roll out from `S` to `T`.** Only after successful promotion, process an
   explicit rollout instruction naming the target and pinned promoted source
   revision. Preview the exact mapping and conflicts before apply. Follow the
   existing installation or synchronization contract, preserving local work,
   protected-source authority, backups, and migration boundaries. Do not
   substitute an unpromoted candidate or assume an available tool can consume
   the intended local source. Publication, remote writes, and release require
   their separate authority. Rollout does not adopt a revision, migrate live
   work, accept an initiative, or prove downstream conformance automatically.

At every boundary, retain a traceable source-to-destination manifest, exact
authority, verification evidence, and recovery procedure outside the clean
payload. Recheck changed source or destination revisions rather than reusing
stale qualification. Reruns must detect already introduced work and preserve
customization and history without duplicate records or empty commits.

## Clean work product and historical records

Sanitize exported copies, not original development evidence. Export only
approved implementation-ready work product and the generic support required
to use it. Never copy the development project wholesale into a template.

The following table is a payload classification inventory.

| Retain in the clean payload when required | Retain only in development or audit history |
|---|---|
| Approved reusable record shapes with generic placeholders; runtime tools; workflow prompts; required tests or fixtures; usage and migration guidance; applicable instructions and valid integrity locks | Populated initiative records, realization notes, project-specific profiles, acceptance receipts, completion reports, development discussions, and test-run results |
| Binding protocol rules, required licenses, upstream source identity, revision provenance, and essential historical references required to interpret the governing baseline | Intermediate designs, abandoned alternatives, scratch files, logs, caches, local environments, sync state or backups, editor state, machine paths, credentials, and unrelated products |

Classify by role rather than extension or directory name. Do not remove
binding revision history or required provenance as cosmetic cleanup. Do not
rewrite an authoritative source, erase a conflict, or fabricate empty history
to make a payload appear clean. Preserve original records and Git history in
their owning project; use precise source references where distribution needs
provenance. New project instances must not inherit TADp's live work, ownership,
acceptance, active conflicts, or test outcomes. Check for broken links and
development-specific names after sanitation, and verify the clean payload in
isolation without relying on files excluded from it.

## Setup procedure and completion report

Perform setup in this numbered order; requirement tables above are not action
lists.

1. Inspect instructions, Git identity and complete worktree state, existing
   installations, source locks, source revision, and baseline checks. Preserve
   unrelated changes. Use a clean, traceable execution context under the Git
   rules; do not stash, move, discard, or commit someone else's work to obtain
   one. Report unavailable facts or authority and continue independent work.
2. Install and configure `P` as described above. Establish its project records
   and non-scaffold candidate protocol workspace. Do not import old initiatives
   or migrate historical work without a separately identified instruction.
3. Document the context rules, serial promotion route, sanitation contract,
   evidence ownership, required checks, and exact authority boundaries in
   `P/AGENTS.md`, `P/project-profile.md`, and a project development guide.
   Update only `R/README.md` and `R/AGENTS.md` where necessary to identify the
   new development home and prevent direct development in `U`; preserve their
   existing governing instructions. Do not edit `U` or canonical sources.
4. Verify project structure, adopted records, links, protected-source integrity,
   applicable regressions, and target resolution from both `R` and `P`. Use
   the configured interpreter. Verify that the development instructions do
   not redirect either context into `U`, and that upstream files and locks
   are unchanged from preflight. Report baseline failures separately from
   introduced failures. Structural validation alone proves no human decision
   or semantic conformance.
5. Review the complete scoped diff, reconcile independent-review findings,
   and create only permitted, traceable commits containing this setup's work.
   Do not merge, push, publish, release, or touch examples or another project.

Report exact created and changed paths, project and Git roots, baseline and
adopted revisions, context-resolution results, verification commands and
results, independent-review findings, and remaining gates or required human
decisions. State whether setup is actually conformant or still incomplete.
Confirm the observed upstream preservation result. Distinguish establishing
this development project from feature completion, reusable-source promotion,
downstream rollout, adoption, and release; claim only events that occurred.
