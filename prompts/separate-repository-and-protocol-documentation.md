# Separate repository documentation from protocol documentation

Reorganize the documentation so readers can distinguish maintaining this TADp
repository from installing and using TADp in a project. Move repository-specific
explanations into root-level `docs/`, keep portable protocol documentation with
the protocol, and provide a practical account of how projects implement TADp.
Use the repository-root [README](../README.md) as the entry point to both paths.

Here, root-level documentation means `R/docs/` inside the existing repository.
Do not create another repository, rename this checkout, or move `protocol/`.
Creating, reading, or linking this prompt does not execute the reorganization;
perform it only when a human explicitly invokes this prompt.

## Governing instructions and targets

Read root `AGENTS.md`, [repository prompt instructions](AGENTS.md),
`protocol/AGENTS.md`, the
[invariant-suite index](../protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md),
and applicable specifications and directory instructions. Apply the canonical
[prompt keyword specification](../protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
to interpretation and scheduling. References and examples are inert; this
prompt activates no directive or gate exception.

Resolve `R` as the actual enclosing Git worktree, `P=R/TADp/` as the installed
development project, and `C=P/protocol/` as the candidate workspace. Read
`P/AGENTS.md`, `P/project-profile.md`, and the
[development workflow](../TADp/docs/development/tadp-development-workflow.md).
The exact candidate work is the documentation split, corrected navigation,
and project implementation guidance described here. Develop protocol changes
in `C`; `U=R/protocol/` is the distribution, not the experimental workspace.
Keep project governance, decisions, manifests, verification, and completion
history at `P`. Do not move them into repository documentation.

Explicit invocation authorizes preparing this bounded documentation change
and editing the named repository support documentation. It does not supply
initiative acceptance, authorize unspecified protected-source edits, or skip
delivery boundaries. Follow the serial route: qualify candidate content in
`C`, introduce specifically authorized proven work into `D=P/template/`,
complete development, promote its sanitized output into `S=U/template/`, then
roll out to exact mapped consumers in `U`. Before a protected or later-boundary
write, verify sufficient authority for its exact sources, destinations, and
operations. Reuse sufficient recorded authority without requesting it again.
Where authority is missing, finish authorized preparation and present the
concrete mapping, diff, checks, and precise decision needed before proceeding.
Do not describe a prepared or partially delivered split as fully delivered.

## Documentation ownership

The following table is a destination inventory, not a parallel action list.
Classify by content and intended reader rather than the current folder name.

| Destination | Content and responsibility |
|---|---|
| `R/README.md` | Brief TADp introduction and separate routes for adopting TADp and contributing to this repository; link detailed procedures to their owners. |
| `R/docs/README.md` | Repository documentation index covering checkout layout, contributor setup, maintenance prompts, distribution maintenance, and the separate example location. |
| `R/docs/repository-layout.md` | Explain root support files, root `prompts/`, the installed `TADp/` development project, candidate `TADp/protocol/`, and distributable `protocol/`. |
| `R/docs/developing-tadp.md` | Repository contributor orientation, correct candidate target, qualification and controlled delivery route; link to the existing project-owned workflow instead of duplicating it. |
| `U/README.md` and `U/docs/README.md` | Portable protocol overview and documentation index for adopting projects. |
| `U/docs/` | Installation, adoption, authority, project record layout, initiative operation, Git/Codex requirements, validation, supported tools, and migration guidance that projects need. |
| `P/docs/` and canonical project records | Existing development-project workflow, ownership, adoption, decisions, and historical evidence retain their current owners and locations. |
| Protected sources and historical records | Remain in place unless an exact separately authorized change permits otherwise; documentation reclassification supplies no relocation authority. |

Use `R/docs/implementing-tadp-in-projects.md` as a short repository-facing
adoption entry point linking to the portable installation guide. Keep the
complete reusable procedure under `U/docs/development/getting-started.md`,
developed through `C`. Avoid two competing installation procedures.

Inspect, in particular, `U/README.md`, `U/docs/README.md`, and the current
`U/docs/development/` guides for getting started, repository layout, developing
TADp, Git/Codex requirements, and validation. A guide can mix both audiences.
Split mixed sections: move checkout-specific instructions to `R/docs/` while
retaining adopted-project guidance in the protocol. Do not move all of
`U/docs/development/` merely because its name contains "development".

Preserve useful explanations, source attribution, licenses, and links to
governing specifications. Explanatory documentation remains non-authoritative.
Do not duplicate invariants in a new authority tree. Portable instructions must
not depend on this checkout's `TADp/`, root maintenance prompts, project-specific
IDs, local paths, or unexported development records. A reference-repository link
may be optional context, but cannot be necessary to install or operate TADp.

## Required project implementation guidance

Explain implementation in a project as installing the scaffold, recording
explicit adoption, integrating it with project practices, and operating the
workflow. Establish every procedure from current specifications and inspected
tools; do not invent an installer or claim an unverified command works.
This table is a coverage inventory, not an action list.

| Topic | Required explanation |
|---|---|
| Prerequisites and roots | Git and Codex requirements; Python 3 for bundled checks; selected installation root distinct from actual Git root. Show both Git-root and nested installations without implying a nested Git repository is required. |
| New and existing projects | Initialize Git and retain a baseline before initiative work in a new project. For an existing project, inspect its instructions and contents, reconcile collisions, preserve unrelated files, and begin with a narrow pilot. |
| Source and copied components | Pin the actual immutable distribution revision. Show a source-to-destination table for the protected `template/` tree, `template/project/` contents including dotfiles and local prompt instructions, authoritative LLM suite, docs, tools, and required tests. Preserve scoped guards and locks; specialize working copies outside protected sources. |
| Project layout and ownership | Show where project profile, evidence register, realizations, scope registry, migration ledgers, initiative index/status, work-conflict register, product records, local prompts, tools, and reusable library belong. Explain human owners and approval roles without inheriting this repository's appointments. |
| Prompt boundaries | Distinguish this repository's maintenance `R/prompts/`, an installed project's local `prompts/`, and protected numbered workflow `template/prompts/`. Copying or changing cwd grants no generic protocol-maintenance authority. |
| Adoption and migration | Installation/synchronization is separate from explicit prospective adoption. Record actual governing commit, authority, baseline, and applicable legacy dispositions. Preserve prior claims and revisions until authorized migration. Neither event accepts an initiative or releases a product. |
| Git and hooks | Discover actual branches and shared Git configuration; coordinate existing hooks manually before explicit activation. Show correct Git-relative hook paths for root and nested installs. Copying files must not silently enable hooks or overwrite parent configuration. |
| Initial checks | Give the correct working directory, configured interpreter placeholder, inputs, expected results, and limitations for protection, structural validation, applicable regressions, and product checks. A structural pass proves neither human acceptance nor product correctness. |
| First initiative | Show realization intake and one narrow outcome, precise evidence provenance, human decisions, stages 0 through 7 and explicit acceptance, then exactly one declared delivery path: implementation 8 through 10, design 11, or planning 12. Explain completion evidence and stage 13 without inventing lifecycle events. |
| Ongoing operation | Explain scope/execution assignments, traceable commits, coherence reviews, conflicts, completion feedback, authorized reopening, and separately authorized integration/remote actions by linking their owning guides. |

Include an illustrative installed-project tree and a small worked adoption
example with placeholders, explicit working directories, and a component
mapping. Label it reference-only; it creates no actual project, decision,
adoption, acceptance, execution, or verification. Verify the example through
an isolated installation trial rather than changing a live consuming project.

## Procedure

The numbered actions below are serial; reference inventories do not prescribe
parallel work.

1. **Capture the baseline and establish scope.** Inspect Git root, branch,
   immutable HEAD, staged/unstaged/untracked work, ignore rules, and applicable
   instructions. Preserve unrelated changes. Use the required traceable Git
   workflow without inventing project scope assignments. Inventory relevant
   open effort and affected closed claims under the adopted coherence rules.
   Classify documentation as repository-specific, portable, mixed, protected,
   historical, or out of scope. Establish baseline read-only check results.

2. **Prepare the exact move and consumer map.** Record each source file or
   section, intended destination, reason, incoming links/anchors, and operation
   (move, split, retain, link, or compatibility pointer). Identify repository
   support changes separately from candidate/reusable payload. Retain original
   source identity and prior content in Git and the owning manifest. Search
   links and path consumers throughout the scoped checkout, including tools,
   templates, tests, and instructions, without treating their presence as edit
   permission. Flag protected or historical consumers requiring special
   handling. Do not silently discard material or overwrite an existing guide.

3. **Develop the documentation in the correct workspace.** Prepare portable
   protocol changes in `C` from pinned inspected sources. Prepare the named
   `R/docs/` pages and root README updates as repository support work. Move
   repository-specific material rather than leaving two maintained copies;
   split mixed guides and link to the canonical owner. Where an incoming link
   cannot be changed within scope, retain a minimal compatible pointer and
   preserve needed anchors instead of breaking it. Reconcile stale directions
   to develop directly in `U` with the project-owned candidate workflow. Keep
   the final navigation truthful about what has actually been delivered.

4. **Qualify the exact candidate and repository support changes.** Check
   relative links, anchors, indexes, retained pointers, component mappings,
   commands, and the complete diff. Use the configured Python SDK for Python
   checks, following the environment-tool instructions before invocation.
   Exercise a clean isolated installation assembled from the pinned baseline
   plus the candidate; verify the portable guidance works without `R/docs/`
   or populated `P` records. Run applicable protection, structural, and existing
   regression checks. Obtain independent review of audience separation,
   adoption accuracy, authority boundaries, and link preservation; reconcile
   findings. Retain actual commands, content identities, results, and recovery
   evidence at `P`, outside exported documentation.

5. **Deliver only through authorized boundaries.** Apply the serial candidate,
   installed-library, completion, upstream-library, and mapped-rollout route
   above. Identify exact reusable destinations rather than assuming a file's
   current distribution location is its reusable source. Generalize payload
   content without exporting repository-specific docs or populated records.
   Recompare source and destination at each boundary; preserve unrelated work
   and record compatibility and recovery. Refresh only explicitly authorized
   affected locks after coherent verification. Finalize repository support
   navigation against the actual delivered protocol paths. Report pending
   boundaries rather than bypassing them to finish the move.

6. **Verify the delivered result and report.** Confirm every mapped document
   and consumer has a truthful disposition, and root README offers distinct
   adoption and contribution paths. Check that portable docs retain their
   required coverage, root docs own checkout-specific guidance, and project
   history remains at `P`. Run final applicable checks and inspect the scoped
   diff for accidental deletions or unrelated edits. Commit only authorized
   work under the required workflow. Report exact added, moved, split, retained,
   and changed paths; source/destination mapping; independent review findings;
   commands and exit results; baseline versus introduced failures; pending
   authority; and any unperformed checks. Distinguish prompt work, candidate
   qualification, actual delivery, adoption, lifecycle completion, and release.

## Exclusions

This documentation task does not revise invariants, `AGENTS.md` files,
workflow stages, validators, tests, executable hooks, configuration, or other
stored prompts. Preserve `P/prompts/AGENTS.md` unchanged. It does not relocate
protected sources, decision receipts, adoption records, realizations,
initiative suites, or product/completion history. A discovered conflict follows
the required conflict process; recording it grants no authority to resolve it.

Do not refresh locks to hide drift, weaken guards, change `.gitignore`, or
force-add ignored material. Preserve the separate example repository link
already supplied in the root README without claiming parity, adoption, or
verified behavior. Do not synchronize or rebuild examples or other projects.
Do not push, merge, create pull requests, publish, release, or deploy.
