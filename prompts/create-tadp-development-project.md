# Establish the TADp development project and controlled promotion workflow

Create a new TADp-governed project named **TADp** in this repository. It is
the home for TADp development effort, including its evidence, initiatives,
candidate work, tests, and completion records. Establish the project and the
workflow below; do not implement an unrelated protocol feature or promote
existing work merely because this project now exists.

The intended result is a development home that uses TADp to develop TADp.
The existing `protocol/` remains the implementation-ready distribution.
Development records explain how a change was produced; the distribution
contains the clean work product needed to implement and use that change.

The following diagram is a reference summary of the required delivery order,
not an instruction to perform these future operations during setup:

```text
TADp/protocol/          Candidate work, developed and tested
       |
       v
TADp/template/          Proven reusable work in the development project
       |                Development completion required before promotion
       v
protocol/template/      Sanitized work promoted into the actual protocol's template
       |
       v
protocol/               Appropriate protocol files updated from that template
```

Creating, reading, or linking this prompt does not execute it. Execute it only
when a human explicitly invokes it. Future template introduction, promotion,
and rollout require an instruction identifying their exact work and targets.
This invocation establishes the project and documents the delivery process;
it does not automatically perform the later arrows in the diagram.

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

One sufficiently specific human instruction may cover several named delivery
steps. Capture and reuse that authority within its exact scope rather than
asking for the same approval at each step. Separate the steps operationally
and satisfy their prerequisites in order; their separation does not itself
require separate human messages. This setup instruction is not standing
authority for unspecified future features or protected-source changes.

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
| Protocol's template `S` | `R/protocol/template/`, the destination for proven development work before rollout into the actual protocol `U`. |

Paths in this prompt are repository-relative unless qualified by one of the
identities above. The project name and nested directory are both `TADp`:
`R/TADp/` is intentional even if the enclosing repository is also named TADp.
Do not rename the repository or relocate `R/protocol/` to create the project.

Use the project-root definition in
[specification 05](../protocol/evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement).
The enclosing Git worktree provides shared history, refs, index, and hook
configuration without widening project ownership. Do not initialize a nested
Git repository. Reject ambiguous targets, escaping links, and collisions with
existing projects. Reuse a verified prior installation on rerun; do not
overwrite or silently adopt an unrelated directory.

**Do not modify `U` directly during setup or development.** This includes its
working files, authoritative suite, tools, tests, documentation, live records,
and reusable sources. Later, separately identified promotion may change `S`
through the proven-work route below. Once introduced into the protocol's
template, work may be rolled out appropriately into the protocol. That rollout
may update only the exact applicable paths in `U` identified by its instruction
and verified source-to-destination mapping. These controlled steps do not permit
experimental development in `U` or bypass protected-source authority.

Here, **protocol scope** means the declared candidate work at `P/protocol/`,
not direct development in the existing `R/protocol/`. The development project
also owns governance outside that candidate workspace. Initiative records,
human decisions, verification reports, and historical evidence belong in
their canonical locations under `P`; they do not become protocol deliverables
merely because they concern the protocol.

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

Installing an unchanged, verified baseline into `P/template/` is bootstrap,
not introduction of new development work. It is permitted during setup.
The validation-before-introduction rule applies to subsequent changes to
that baseline; it does not require developing the initial template from scratch.
The complete protected library goes at `P/template/`; the placeholder under
its `project/template/` does not replace the installed library or recursively
embed another copy.

Establish the following project layout using canonical sources. This is a
placement inventory, not an instruction to create speculative work records.

| Project location | Required purpose |
|---|---|
| `P/AGENTS.md`, `P/README.md`, `P/project-profile.md` | Project entry points, purpose, ownership, exact boundaries, governing revision, adoption evidence, and Git relationship. |
| `P/evidence/authoritative/` | The installed governing suite and any separately authorized project authority. Proposed protocol replacements do not become governing rules here automatically. |
| `P/evidence/non-authoritative/` | Project context and realization inputs, with their original identity and standing. |
| `P/initiatives/` | Canonical scope, membership, status, conflict, decision, and type-specific work records, created at their actual owning triggers. |
| `P/products/` | Product records identifying delivered outputs and their actual locations, including candidate outputs under `P/protocol/`. Do not create a second authoritative copy of each output. |
| `P/protocol/` | Candidate protocol sources and supporting tests or fixtures, organized according to the accepted work and mapped to eventual destinations. |
| `P/template/` | The protected development library, initially installed unchanged and later updated only with qualified work and exact authority. |
| `P/tools/`, `P/tests/`, `P/prompts/` | Installed project support and the project-local prompt workspace. Candidate changes to generic tools or tests are developed in `P/protocol/` first. |
| `P/docs/development/tadp-development-workflow.md` | Project-specific instructions for the delivery route, required evidence, sanitation, and operating contexts in this prompt. |

Do not turn `P/protocol/` into a second installed project with competing
profiles, live initiative indexes, or a separate Git repository. It is a
candidate product workspace, not a second source of governing authority.
Use isolated test installations to exercise a complete candidate scaffold.
Copy only the sources needed for the work, retaining their provenance and
applicable protection; do not seed the workspace with the existing protocol's
live development records or treat copied instructions as new authority.

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

For example, a direct instruction issued from either `R` or `P` may identify
the same accepted maintenance work and `P/protocol/` target. Both contexts must
resolve to that project and preserve the same authority boundary. An
instruction stored under `P/prompts/` still inherits its project-local
restrictions; changing the shell directory cannot elevate it to maintenance
authority. These examples describe context resolution only and execute nothing.

## Development, qualification, promotion, and rollout

Document and enforce this serial route in the new project's instructions and
development guide. These are future work contracts, not instructions to invent
or promote a feature during project setup.

The numbered steps below describe delivery boundaries. They do not replace,
renumber, or waive the canonical initiative workflow stages 0 through 13.
In this prompt, **qualified** means the exact candidate has passed its required
checks and review; **completed** means its development initiative has actual
completion evidence under TADp; **promoted** means the identified clean output
has been introduced into `S`; and **rolled out** means the mapped protocol
consumers have actually been updated and verified. Qualification, promotion,
and rollout are delivery descriptions, not additional initiative lifecycle
states. Completion alone proves neither promotion nor rollout.

1. **Develop in protocol scope.** Create and revise candidate work in `C`
   under the applicable initiative, specific change authority, and workflow
   gates. Keep experiments, proposal drafts, logs, and temporary outputs out
   of `D`, `S`, and `U`. A proposed invariant change remains a proposal until
   its exact revision is authorized; candidate status cannot bypass an
   applicable governing invariant.

   Declare the candidate files, governing sources, intended reusable
   destinations, required consumers, acceptance claim, and verification before
   delivery. Keep the project's currently adopted tools and governing suite
   distinguishable from candidate replacements. A successful experiment is
   evidence to review, not authority to change the baseline.

2. **Validate and test before template introduction.** Verify candidate
   behavior and its consumers against the accepted claim. Run applicable
   structural and protection checks, regression tests, link checks, and a
   representative clean installation or workflow trial in isolated fixtures.
   Record actual commands, environment, source revision, results, limitations,
   compatibility, migration, and recovery effects in `P`. Retain failures;
   skipped or unavailable checks are not passes. Obtain independent review
   and reconcile its findings before qualification.

   Tests must exercise the behavior being changed, including relevant failure
   cases and compatibility boundaries. Assemble a clean installation trial
   from the pinned clean baseline plus the exact candidate changes and
   declared dependencies. A small change need not contain a complete scaffold.
   Test the assembled payload without relying on undeclared development files
   or the installed project as hidden support. If a temporary integrity lock is
   needed for an isolated candidate fixture, create it only under applicable
   exact authority and label it as fixture evidence; it does not authorize or
   refresh a real project's protected sources. Retain the exact tested content
   and a reviewed manifest before proceeding.

3. **Introduce proven work into `D`.** Require passed candidate qualification,
   applicable acceptance gates, and a reviewed, sanitized file manifest
   identifying exact source revisions, destinations, changes, exclusions,
   and verification. A specific human instruction must authorize the exact
   reusable-source change before editing protected `D`. Reconcile affected
   consumers and refresh only the
   specifically authorized affected locks after content verification. Recheck
   protection and validation and exercise a clean installation from the result.

   Introduce the reusable source at its declared library location, retaining
   generic placeholders in reusable records. Do not populate the library with
   this project's decisions or results. Development completion may follow this
   step when introduction into `D` is part of the accepted deliverable; do not
   demand completion before delivering that same accepted output.

4. **Promote completed work from `D` into `S`.** Require actual completion
   evidence for the development work, including its qualified introduction
   into `D`. Recorded promotion authority must identify that completed
   work, the qualified manifest, source revision, and exact protected-source
   changes. Compare the current destination with the tested base, preserve
   unrelated work, and reconcile drift before applying only those sanitized
   deliverables. Verify the resulting protocol template and
   its installable output with isolated fixtures. Update only affected locks
   under the same exact authority after coherent verification. Keep `U`
   unchanged outside `S` during this step. Identify the protocol consumers
   requiring subsequent rollout; do not claim protocol-wide coherence until
   those consumers are reconciled and verified.

   Completion here refers to the development work supplying the promoted
   output. The promotion operation must have its own truthful execution and
   verification evidence; it cannot be called finished before its actual
   writes and checks. If promotion reveals a substantive defect in completed
   development work, route it through the required revision or reopening and
   renewed acceptance process. Do not silently alter a closed claim while
   copying it.

5. **Roll out from `S` appropriately into `U`.** Only after successful
   promotion, use recorded rollout authority naming the applicable protocol
   paths and pinned promoted source revision. That authority may be part of
   the same sufficiently specific instruction covering promotion. Preview the exact
   source-to-destination mapping and conflicts before applying the sanitized
   work product. Update the appropriate protocol files and consumers from
   that proven template source, preserving unrelated work, source identity,
   protected-source authority, recovery evidence, and migration boundaries.
   Do not copy the template tree wholesale over the protocol or substitute an
   unpromoted candidate. Reconcile and verify affected consumers before
   refreshing only specifically authorized affected locks. Then rerun protocol
   validation, protection checks, and applicable regressions. Publication,
   remote writes, and release require
   their separate authority. Rollout does not automatically adopt a revision,
   migrate live work, accept an initiative, or establish protocol conformance.

   Finish only when every required mapped consumer has a verified disposition.
   A template-only checkpoint or partially applied rollout remains explicitly
   pending or incomplete. If a governing revision requires coherent sources,
   consumers, checks, and locks at its effective commit, honor that requirement;
   do not treat an intermediate template checkpoint as an adopted revision.

At every boundary, retain a traceable source-to-destination manifest, exact
authority, verification evidence, and recovery procedure outside the clean
payload. Recheck changed source or destination revisions rather than reusing
stale qualification. Reruns must detect already introduced work and preserve
customization and history without duplicate records or empty commits.

### Promotion manifest and evidence

Maintain the manifest with the owning product or work records outside the
clean payload, reusing canonical records rather than inventing parallel
registers. Its format may follow existing project conventions, but it must
identify the following information for every included change:

| Information | Required detail |
|---|---|
| Work and authority | Exact development initiative and accepted baseline; actual instruction or receipt authorizing each affected delivery boundary and protected-source change. |
| Source identity | Source project, immutable revision, file path, and content digest or equivalent exact content identity; distinguish tested content from later edits. |
| Destination and operation | Exact source-to-destination path and whether the operation adds, updates, or removes a file; record the destination baseline and current comparison. |
| Transformation | Any generalization, placeholder handling, link adjustment, or other sanitation, with the reason and resulting content identity. |
| Verification | Requirements and checks covering the result, actual commands and environment, independent review, results, and evidence locations. |
| Exclusions and dependencies | Deliberately excluded development material, affected consumers, compatibility and migration requirements, and any unresolved blocking dependency. |
| Recovery and disposition | Prior content or revision, a scoped recovery method preserving subsequent work, actual result revision, and remaining owned actions. |

Qualification applies to exact content, not just to a filename or a test run
on an earlier version. Verify any transformation after candidate testing;
sanitation is not a reason to distribute an untested variant. Recheck source
or destination drift before the next write. A required removal must be named
and reviewed; omission from a payload never authorizes deleting existing files.

### What appropriate protocol rollout means

Select destinations by the role of each reusable source. The following
examples are reference mappings only; they authorize no particular change.

| Reusable source role | Possible protocol consumer and handling |
|---|---|
| `S/project/tools/tadp_validate.py` | `U/tools/tadp_validate.py`, when this is a declared runtime consumer; verify imports, dependencies, and regression behavior. |
| `S/project/prompts/AGENTS.md` | `U/prompts/AGENTS.md`, preserving the project-local workspace boundary and compatible local instructions. |
| `S/project/evidence/authoritative/LLM/` | The corresponding suite under `U/evidence/authoritative/LLM/` only for the specifically authorized invariant revision, with source identity, consumer reconciliation, and governed locks. |
| `S/prompts/WORKFLOW-CONTRACT.md` | The protected workflow library already at `U/template/prompts/WORKFLOW-CONTRACT.md`; do not duplicate it into the project-local `U/prompts/` workspace. |
| Reusable `.template.md` record shapes | Remain reusable sources unless a real, separately governed record-creation trigger requires an instance; rollout alone does not create live initiatives, profiles, decisions, or completion records. |

Recalculate links where placement changes and merge applicable entry-point
instructions without discarding established requirements. Preserve template
placeholders where the destination is still a reusable source. Resolve them
only for a real instance using sufficient evidence. An unchanged or
inapplicable consumer needs a recorded reason, not a fabricated edit.

## Clean work product and historical records

Sanitize exported copies, not original development evidence. Export only
approved implementation-ready work product and the generic support required
to use it. Never copy the development project wholesale into a template.

For this workflow, **work product** is the accepted reusable result: for
example, a generic tool change, workflow rule, template shape, or user guide.
**Historical records** explain the actual development and decisions that led
to that result. **Intermediate files** supported exploration, transformation,
or testing but are not required to implement or use the result. A polished
report is still history if its role is to document this project's work; a
test fixture may be work product when it is required regression coverage.

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

Use a deliberate inclusion manifest rather than exporting everything except
files caught by a blacklist. Review the payload for development-specific
initiative IDs, owners, absolute paths, active conflicts, local configuration,
test outcomes, and links back into non-exported material. Generalize instance
values only where the reusable role requires it; do not replace binding
authority or source attribution with fictitious placeholders.

The clean result must supply everything needed for its declared implementation
or installation, with generic examples, required dependencies, and working
links. It must not depend on the developer's machine, current workspace, live
initiative records, or unexported temporary files. Required provenance may
refer precisely to retained Git history or source records without importing
the development history as new protocol records.

Sanitation authorizes preparing the declared export, not purging historical
records already in `U`, moving someone else's evidence, or revising an
immutable claim. Existing protocol content is preserved unless the exact
promotion or rollout scope separately identifies and authorizes its change.
Record any cleanup dependency instead of silently expanding the operation.

## Setup procedure and completion report

Perform setup in this numbered order; requirement tables above are not action
lists.

1. Inspect instructions, Git identity and complete worktree state, existing
   installations, source locks, source revision, and baseline checks. Preserve
   unrelated changes. Use a clean, traceable execution context under the Git
   rules; do not stash, move, discard, or commit someone else's work to obtain
   one. Report unavailable facts or authority and continue independent work.

   Capture the current protocol file and lock state so preservation can be
   checked later. Select a verified committed installation source. If the
   current source tree contains uncommitted work, preserve it and distinguish
   it from the selected immutable baseline; do not silently incorporate it
   into the new project's claimed source revision.

2. Install and configure `P` as described above. Establish its project records
   and non-scaffold candidate protocol workspace. Do not import old initiatives
   or migrate historical work without a separately identified instruction.

   Follow the canonical installation assembly, including the governing suite,
   complete reusable library, and required runtime support. Create a candidate
   workspace README explaining its role and boundaries. Instantiate the
   required profile, coordination, and conflict records from their canonical
   sources with truthful initial content. Create scope members, initiatives,
   decision receipts, or delivery records only when the actual event and
   owning workflow require them; do not invent a pilot feature to fill space.

3. Document the context rules, serial promotion route, sanitation contract,
   evidence ownership, required checks, and exact authority boundaries in
   `P/AGENTS.md`, `P/project-profile.md`, and
   `P/docs/development/tadp-development-workflow.md`. Link those instructions
   from `P/README.md` so work started in the project can discover them.
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

   Exercise target resolution from both operating contexts using explicit
   paths and read-only checks. Both must identify the same `P`, Git root,
   candidate scope, and protected libraries. Check that a rerun would reuse
   valid records rather than create another project, change adoption history,
   or repeat already sufficient human decisions. Record semantic review and
   structural checks separately.
5. Review the complete scoped diff, reconcile independent-review findings,
   and create only permitted, traceable commits containing this setup's work.
   Do not merge, push, publish, release, or touch examples or another project.

Setup is complete only when the following requirements have actual evidence.
This table is a verification inventory, not a new lifecycle or approval scheme.

| Requirement | Evidence needed |
|---|---|
| Project identity and placement | One installed project named TADp at `R/TADp/`, its verified Git relationship, and an unambiguous non-scaffold candidate workspace. |
| Governing baseline and records | Exact source and adopted revisions, actual ownership and authority, required canonical records, and no fabricated lifecycle events or inherited development claims. |
| Protection and upstream preservation | Matching installed source locks and unchanged `R/protocol/` content and locks compared with preflight, with any baseline findings disclosed. |
| Usable instructions | Discoverable guidance covering both operating contexts, the complete serial delivery route, manifest contents, sanitation, rollout mapping, and recovery. |
| Verification and review | Actual checks appropriate to setup, resolved local links, context and rerun checks, independent review with reconciled findings, and honest disposition of remaining issues. |

Report exact created and changed paths, project and Git roots, baseline and
adopted revisions, context-resolution results, verification commands and
results, independent-review findings, and remaining gates or required human
decisions. State whether setup is actually conformant or still incomplete.
Confirm the observed upstream preservation result. Distinguish establishing
this development project from feature completion, reusable-source promotion,
protocol rollout, adoption, and release; claim only events that occurred.
