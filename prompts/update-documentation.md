# Update TADp documentation for current usage and features

Work in the TADp repository containing this prompt. Refresh its explanatory
documentation so a developer can understand, adopt, operate, and maintain the
features that are currently supported. Maintain the distinction between
repository contribution guidance and portable guidance for adopting projects.
Establish current behavior and authority from inspected sources; do not assume
that every existing document is stale or that every stored proposal has been
implemented or delivered.

This is a documentation maintenance task. Creating, editing, reading, or linking
this prompt does not execute it. An explicit human invocation authorizes the
bounded candidate preparation and repository support documentation described
below; initiative acceptance and later delivery boundaries remain separate.

## Authority and scope

Read the repository-root `AGENTS.md`, [repository prompt instructions](AGENTS.md),
`protocol/AGENTS.md`, and the
[invariant-suite index](../protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
Read every applicable specification before deciding what the documentation
should say. Apply the canonical
[prompt keyword specification](../protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md),
including operative versus inert text, positional settings, list scheduling,
and required records. No directive or gate exception is activated by this
prompt's reference to that specification.

Resolve the actual enclosing Git worktree as `R`, the installed development
project as `P=R/TADp/`, and its candidate workspace as `C=P/protocol/`, from
either repository or project context. Read `P/AGENTS.md`,
[the project profile](../TADp/project-profile.md), its linked decisions, and the
[development workflow](../TADp/docs/development/tadp-development-workflow.md).
The exact candidate work is the explanatory documentation refresh described
here, prepared in `C`. `U=R/protocol/` is the implementation-ready distribution,
not the development target. `D=P/template/` is the protected installed reusable
library; `S=U/template/` is the protected upstream reusable library.

Prepare and qualify portable documentation in `C`; edit only the named
repository support documentation directly at `R`. Keep project governance,
decisions, manifests, verification, and completion history at their canonical
locations in `P`, outside the exported documentation. Follow applicable
initiative preparation, human-decision, acceptance, and type-specific gates;
this prompt does not accept an initiative or manufacture lifecycle facts.
Its explicit candidate target replaces the default distribution target in
`prompts/AGENTS.md` for this work. Changing cwd does not expand authority, and
`P/prompts/AGENTS.md` remains unchanged.

Preserve the serial route: qualify exact content in `C`, introduce specifically
authorized proven work into `D`, complete development, promote its sanitized
output into `S`, then roll out from the pinned promoted revision to exact mapped
consumers in `U`. Invocation alone grants no protected-source introduction,
promotion, or rollout. Before each such write, verify sufficient exact authority
and current evidence; reuse sufficient recorded authority without requesting it
again. If authority is missing, finish authorized preparation and present its
concrete diff, mapping, checks, and precise remaining decision. Do not edit `U`
directly to bypass that route.

## Existing documentation work and ownership

Inspect the current repository [documentation index](../docs/README.md),
[layout](../docs/repository-layout.md), and
[contributor guide](../docs/developing-tadp.md). Repository-specific explanations
belong in `R/docs/`; portable installation, adoption, operation, and migration
guidance belongs with the protocol. `P/docs/` and populated project records
retain their own owners; they are neither repository documentation to relocate
nor an automatic second rollout target.

The documentation split already has candidate drafts under
`C/documentation/` and an owning
[preparation record](../TADp/evidence/non-authoritative/documentation-split/preparation.md),
[verification record](../TADp/evidence/non-authoritative/documentation-split/verification.md),
and [manifest](../TADp/evidence/non-authoritative/documentation-split/manifest.json).
At this prompt revision, the portable split is prepared and qualified, pending
acceptance and authorized delivery; repository entry points link to the current
distributed guides and disclose that status. Re-establish actual status from
current content, Git, and records when executing; these observations are not
future delivery evidence or permission to overwrite existing work.

Inventory that effort before starting overlapping work. Reuse compatible drafts
and mappings after comparing their pinned provenance and current bytes. Preserve
prior evidence and findings; changed content needs fresh qualification. Retain
the existing `.md.in` fragment convention where applicable and verify links at
their declared assembled runtime destinations. Do not treat `C` as a second
scaffold or resolve fragment links into `P`'s live governance. Assess whether the
refresh belongs to the same coherent outcome or needs separate narrow work;
do not silently absorb the split, reopen claims, or infer acceptance.

Link the separate [example repository](https://github.com/spkvfx/TADp-example)
and provide its clone URL, `https://github.com/spkvfx/TADp-example.git`, where
useful in the entry-point and adoption documentation. These human-supplied
links identify the example's location; they do not prove rebuild completion,
feature parity, protocol adoption, or verified application behavior. Establish
any such claim from inspected evidence, or leave it explicitly unverified.
This task prepares portable protocol documentation and maintains named
repository support documentation only; it must not synchronize, rebuild, or
validate the example application. Follow the current target boundary in
`prompts/AGENTS.md`, which supersedes earlier example-mirroring instructions.

The following is a destination inventory, not a parallel action list. `U`
paths identify inspected runtime consumers, not permission for direct edits.

| Documentation owner or intended consumer | Authorized preparation or maintenance |
|---|---|
| `R/README.md` | Concise entry point with distinct adoption and contribution routes, linked to actual delivered guidance. |
| `R/docs/README.md`, `repository-layout.md`, `developing-tadp.md`, and `implementing-tadp-in-projects.md` | Repository navigation, checkout layout, contributor setup, maintenance boundaries, and short adoption entry point. Add focused repository guides under `R/docs/` only when needed and linked. |
| `U/README.md`, `U/docs/README.md`, and explanatory guides under `U/docs/` | Prepare portable revisions in `C`, including installation, project record layout, operation, development, and migration guides. |
| `U/tools/README.md` | Prepare supported-tool explanations, commands, and limitations in `C`. |
| Explanatory READMEs under `U/initiatives/` and `U/products/` | Prepare orientation in `C` without changing initiative or product claims or populated records. |
| `U/evidence/README.md`, `U/evidence/non-authoritative/README.md`, and `U/evidence/non-authoritative/realizations/README.md` | Prepare evidence orientation in `C`, preserving source evidence. |
| `U/prompts/README.md` | Prepare only compatible appended guidance in `C`; preserve the complete canonical reusable-source text as a contiguous block required by the validator. Corrections to that canonical text need exact protected-source follow-up. |

For each portable change, declare its candidate path, pinned source, actual
reusable destination in `D` and later `S`, runtime consumers in `U`, and any
sanitation or link transformation. Inspect the existing role-based map rather
than assuming identical paths or a wholesale directory sync. For example, the
split maps candidate `documentation/docs/development/developing-tadp.md.in` to
reusable `project/docs/development/README.md`, then to two runtime consumers.
File presence in `U` does not establish a supported reusable destination.

Prefer correcting and linking existing guides to creating duplicates. Add a
focused portable guide in `C` only with an explicit destination and consumer
map. Keep the complete reusable installation procedure with the protocol;
repository adoption guidance links to it. Portable procedures must work without
this checkout's `R/docs/`, populated `P` records, local paths, or appointments.
Update navigation and preserve incoming references and compatibility anchors.

Inventory other documentation as well, but do not treat every Markdown file
as editable documentation. This prompt alone does not authorize invariant
revisions, direct changes to `D`, `S`, or `U`, any `.tadp-lock.json` refresh,
any `AGENTS.md` change, or rewriting historical receipts, source realizations,
adoption records, initiative specifications, lifecycle/status records, or
product deliverables.
Necessary new governance and evidence records at `P` follow their owning stages
and actual triggers; they are not explanatory documentation edits. Implementation,
validators, tests, hooks, configuration, and other stored prompts, including
this one, remain outside the refresh. Candidate revisions to invariants,
reusable record shapes, workflow prompts, or executables are also outside this
documentation outcome.

If a protected or otherwise excluded source needs correction, identify its
exact path, claim, proposed correction, and required human authority. Continue
independent authorized documentation work. Do not revise a rule, refresh a
lock, or use a protected-update override to make the documentation task pass.
Record directly evidenced invariant contradictions through the required
conflict process; that factual record does not authorize their resolution.

## Required procedure

The numbered steps below are serial. Coverage tables and other reference
inventories within a step are not independent action lists.

1. **Capture the baseline and discover documentation.** Inspect the actual Git
   root, current branch and commit, staged/unstaged/untracked work, applicable
   directory instructions, and `.gitignore`. Preserve unrelated changes. Use
   the applicable traceable branch/commit workflow without assuming a branch
   name or performing integration. Resolve `R`, `P`, `C`, `D`, `U`, and `S`
   consistently from both operating contexts. Inspect project adoption and
   actual scope/execution assignments without inferring them from the current
   branch. Inventory relevant proposed, accepted, and partial effort, including
   the existing documentation split, and affected closed claims. Record
   incompatible efforts in the owning work-conflict register and affected
   records; preserve closed claims until authorized reopening. Inventory the
   documentation throughout the scoped tree, including protected documents.
   Historical examples and the separate example fork are outside the target.
   Classify each relevant document by audience, owner, standing, and edit
   boundary: repository support, portable candidate, installed project,
   protected, historical, or out of scope. Inspect governing sources and
   distributed behavior before using examples or historical records. Run
   existing read-only protection and validation checks at the explicit `P`
   and `U` roots to distinguish baseline findings from introduced findings.

2. **Build a coverage and evidence map.** For each topic in the reference table
   below, identify its owning specification or accepted authority, supporting
   implementation and tests where applicable, user-facing documentation, and
   any gap or contradiction. Compare the current sources with the existing
   explanations. Distinguish installed capability, project adoption, legacy
   behavior, proposed work, and verified operation. Account for proposed and
   partially performed effort when relevant without presenting it as shipped
   functionality. Never infer adoption, acceptance, migration, or completion
   from file presence, a branch, or a passing structural check.
   Map each proposed edit to its audience, candidate or repository path,
   reusable destination, runtime consumers, incoming links, operation, and
   current baseline identity. Reconcile the existing split's map and preserve
   unaffected drafts rather than creating a competing copy.

   | Coverage topic | What the documentation must explain where supported |
   |---|---|
   | Purpose and prerequisites | TADp's use cases, Git and Codex requirements, and limits of compatibility with other tools |
   | Setup and adoption | Reference distribution versus adopted project, scaffold contents, first validation, hooks, and existing-project migration |
   | Repository development and delivery | `R/docs/` ownership, installed `P` governance, candidate `C`, protected libraries `D` and `S`, qualification, development completion, promotion, mapped rollout, and exact authority at each boundary |
   | Evidence and authority | Binding invariants, accepted decisions, observed behavior, non-authoritative clues, traceability, and conflict handling |
   | Initiative workflow | Stages 0 through 13, stage versus lifecycle state, human decision receipts, separate acceptance, and implementation/design/planning delivery paths |
   | Version scopes and provenance | Major/minor/patch identities, scope membership, source catalogs and notes, exact routing, current paths, and legacy compatibility |
   | Intake and revision | Fit assessment, coherent same-outcome revision, bounded delegated placement/reopening, split boundaries, and renewed acceptance of changed claims |
   | Git operation and closure | Actual branch roles and captured bases, dedicated/shared execution, per-member attribution, immediate-parent local integration, separate scope closure, and separately authorized remote actions |
   | Coherence and feedback | Open effort as work, work-conflict records, completion feedback, historical closed claims, and reopening before refinement |
   | Prompt locations | Repository maintenance prompts, scaffold-local prompts, and the protected numbered workflow library, with their distinct targets and authority |
   | Prompt keywords | Canonical registry, defaults, positional composition, inverse forms, list scheduling, preview/local/review behavior, and exact exception authority |
   | Protected sources | Reusable sources versus instantiated copies, integrity locks, drift reporting, and the separately authorized maintenance process |
   | Tools and verification | Supported tool entry points, arguments, working directories, exit behavior, tests, machine-readable output, and what checks cannot prove |

   Treat this table as a coverage inventory, not authority to introduce or
   change a feature. Read current specifications and consumers rather than
   copying these summaries into normative text. Preserve historical contracts
   under their recorded revisions and explain the current adoption boundary.

3. **Prepare the authorized documentation.** Develop portable edits in `C`
   from pinned inspected sources and maintain the named `R` support docs.
   Correct stale terminology, paths, commands, prerequisites, feature
   descriptions, workflow explanations, and examples. Give a newcomer a clear
   route from the repository README to setup and first use, and give an existing
   user clear operation and migration guidance. Keep detailed procedures in
   their owning guides and reconcile
   summaries and indexes through precise relative links. Link material rules
   to their authoritative source instead of creating a competing specification.
   Mark examples, placeholders, and keyword demonstrations as reference-only;
   they must not imply that reading a guide executes work or satisfies a gate.
   Explain the purpose, required input, working directory, action, expected
   result, and limitations of each documented procedure. Check those details
   against the actual tools and tests. Describe observed implementation limits
   honestly; documentation must not advertise planned functionality as present
   or legitimize behavior that conflicts with an invariant.
   Keep adoption and contribution routes distinct, link project-specific
   governance to its existing owner, and disclose prepared replacements until
   their actual rollout. Keep a reviewed inclusion manifest, content identities,
   transformations, dependencies, exclusions, and scoped recovery plan at `P`.
   Sanitize exported copies without rewriting their source history.

4. **Qualify the exact candidate and repository documentation.** Use the
   project's configured Python environment, discovered through the environment
   tooling before any Python invocation, and existing verification tools.
   Inspect a documented command before running it; use help, read-only checks,
   or isolated disposable fixtures when a real invocation could alter records,
   Git configuration,
   branches, integration state, locks, or external systems. Check relative links,
   anchors, referenced files, command syntax, indexes, and consistency of all
   changed explanations at their intended destinations. Assemble an isolated
   clean installation from the pinned baseline plus exact candidate content
   and declared dependencies; verify portable guidance without repository docs
   or populated project history as hidden support. Use both Git-root and nested
   installations when setup/root guidance is affected. Do not initialize or
   refresh a fixture lock without exact applicable authority, and never use a
   fixture to change live locks. Run existing protection and TADp validation
   at `P`, read-only at `U`, and in the assembled installation, plus applicable
   existing regressions and focused checks for changed examples. `C` fragments
   alone are not an installed project to validate. Obtain independent review
   of the complete scoped diff, audience separation, factual claims, destination
   map, and authority boundaries; reconcile its findings. Preserve actual check
   output and exit status. Investigate introduced failures within this scope;
   report pre-existing failures or required executable fixes separately. Do not
   change existing tools, fixtures, assertions, or evidence merely to obtain a
   pass. Qualification applies only to the exact tested and reviewed content;
   later edits or sanitation require current comparison and relevant rechecks.

5. **Deliver only across authorized boundaries.** Check qualification,
   acceptance, exact authority, and the current manifest before introduction
   into `D`. Where separately authorized, introduce the proven reusable docs,
   reconcile consumers, verify coherent content before refreshing only affected
   authorized locks, and record actual development completion through its
   owning workflow. Only then may specifically authorized promotion change `S`,
   followed by authorized rollout to exact mapped `U` consumers from the pinned
   promoted revision. Compare source and destination drift at every boundary;
   preserve unrelated work, compatibility, provenance, and recovery. No wholesale
   scaffold sync or direct distribution development substitutes for this route.
   Missing authority leaves that boundary pending; report the prepared result
   and exact decision needed without claiming later delivery. Confirm writes
   stay within the authorized documentation and triggered governance paths.
   Do not create a replacement mirror, edit another scaffold such as `TADp-v1/`,
   or access the separate example fork as an update target. Honor `.gitignore`:
   do not change ignore rules or force-add ignored material. Example presence,
   parity, and application validation are not completion gates for this task.
   Preserve historical records and report stale references that require
   separately authorized corrections without rewriting their source identity.

6. **Review coverage and the final diff.** Revisit every inventoried document
   and topic. Assign a truthful disposition: repository docs updated, candidate
   prepared/qualified, library introduction/promotion/rollout verified, reviewed
   and current, historical and preserved, protected and unchanged, out of scope,
   or blocked with the exact missing authority/evidence. Final navigation must
   reach delivered guides and identify pending candidates truthfully. Confirm
   no source identity or historical claim was rewritten and no excluded file or
   unrelated work entered the change. Inspect whitespace,
   the complete scoped diff, and target-boundary compliance. Use
   traceable commits as required by repository instructions, staging only this
   task's files. Run final applicable checks against the actual reached boundary;
   do not reuse candidate results as proof of a later delivery.
   Do not push, merge, create a pull request, publish, release, or deploy.
   Claim documentation completeness only for the reviewed scope with all
   unresolved gaps and failed or unperformed checks visible.

## Completion report

Report the documentation areas brought up to date and the evidence used to
establish current usage and supported features. Include the coverage inventory
and dispositions, exact changed repository support, candidate, and triggered
project record paths, and source-to-reusable-to-runtime mapping. Identify each
boundary actually reached and its exact authority, revision/content identities,
checks, remaining consumers, and pending decisions. Report unchanged protected
and distribution paths explicitly when only preparation was performed.
Confirm that no example synchronization or separate-fork work was performed.

Give the actual verification commands, roots, exit results, and limitations;
distinguish baseline findings, introduced findings, and checks not performed.
Identify remaining documentation gaps, protected-source proposals, executable
defects, conflicts, independent review findings and dispositions, and any
required human decisions. Keep prompt editing, candidate qualification,
protected-library introduction, development completion, promotion, rollout,
initiative acceptance, protocol adoption, and release as distinct claims;
report each only from its own actual authority and evidence.
