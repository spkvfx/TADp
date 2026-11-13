# Update TADp documentation for current usage and features

Work in the TADp repository containing this prompt. Update its explanatory
documentation so a developer can understand, adopt, operate, and maintain the
features that are currently supported. Establish current behavior and authority
from inspected sources; do not assume that every existing document is stale or
that every stored proposal has been implemented.

This is a documentation maintenance task. Creating or reading this prompt does
not execute it. When a human explicitly invokes it, its scope is the explanatory
documentation described below, subject to the repository's ordinary protections.

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

Describe rebuilding the example application in a separate fork as future work.
The user will provide links when it is ready; until then, use a plain-text
future-work note without invented URLs, placeholder links, availability claims,
or a request for links. Missing links do not block this documentation task.
This task maintains the protocol and scoped repository documentation only;
it must not synchronize, rebuild, or validate the example application. Follow
the current target boundary in `prompts/AGENTS.md`, which supersedes earlier
example-mirroring instructions.

The following is a reference inventory of editable documentation, not a
parallel action list:

- Repository-root `README.md` as the entry point to TADp itself.
- `protocol/README.md`, `protocol/docs/README.md`, and explanatory Markdown
  guides under `protocol/docs/`, including development and migration guides.
- `protocol/tools/README.md` for supported tools, commands, and limitations.
- Explanatory READMEs under `protocol/initiatives/` and `protocol/products/`,
  without changing any initiative or product claim or record.
- `protocol/evidence/README.md`,
  `protocol/evidence/non-authoritative/README.md`, and
  `protocol/evidence/non-authoritative/realizations/README.md` for evidence
  orientation, without revising source evidence.
- `protocol/prompts/README.md` for the project-local prompt workspace. Preserve
  its complete canonical reusable-source text as a contiguous block, as the
  existing validator requires. Limit additions to compatible appended guidance;
  route corrections to canonical text through protected-source follow-up.

Add a focused guide under `protocol/docs/` when existing documentation cannot
explain a supported feature clearly. Prefer correcting and linking existing
guides to creating duplicates. Update navigation whenever a document is added
or its location changes; preserve valid incoming references.

Inventory other documentation as well, but do not treat every Markdown file
as editable documentation. In particular, this prompt does not authorize
changes to authoritative evidence, `protocol/template/**` (including its
READMEs and numbered workflow prompts), any `.tadp-lock.json`, any `AGENTS.md`,
historical decision receipts, source realizations, adoption records, initiative
specifications, lifecycle/status records, or product deliverables. It does not
authorize changes to implementation, validators, tests, hooks, configuration,
or other repository prompts, including this one.

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
   name or performing integration. Inventory the documentation throughout the
   scoped tree, including protected documents. Historical examples and the
   separate example fork are outside the documentation-update target.
   Classify each relevant document as editable, protected, historical, or out
   of scope. Inspect the maintained protocol sources before using examples or
   historical records. Run the existing read-only protection and validation
   checks to distinguish baseline findings from introduced findings.

2. **Build a coverage and evidence map.** For each topic in the reference table
   below, identify its owning specification or accepted authority, supporting
   implementation and tests where applicable, user-facing documentation, and
   any gap or contradiction. Compare the current sources with the existing
   explanations. Distinguish installed capability, project adoption, legacy
   behavior, proposed work, and verified operation. Account for proposed and
   partially performed effort when relevant without presenting it as shipped
   functionality. Never infer adoption, acceptance, migration, or completion
   from file presence, a branch, or a passing structural check.

   | Coverage topic | What the documentation must explain where supported |
   |---|---|
   | Purpose and prerequisites | TADp's use cases, Git and Codex requirements, and limits of compatibility with other tools |
   | Setup and adoption | Reference distribution versus adopted project, scaffold contents, first validation, hooks, and existing-project migration |
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

3. **Update the authorized documentation.** Correct stale terminology, paths,
   commands, prerequisites, feature descriptions, workflow explanations, and
   examples. Give a newcomer a clear route from the repository README to setup
   and first use, and give an existing user clear operation and migration
   guidance. Keep detailed procedures in their owning guides and reconcile
   summaries and indexes through precise relative links. Link material rules
   to their authoritative source instead of creating a competing specification.
   Mark examples, placeholders, and keyword demonstrations as reference-only;
   they must not imply that reading a guide executes work or satisfies a gate.
   Explain the purpose, required input, working directory, action, expected
   result, and limitations of each documented procedure. Check those details
   against the actual tools and tests. Describe observed implementation limits
   honestly; documentation must not advertise planned functionality as present
   or legitimize behavior that conflicts with an invariant.

4. **Verify the protocol documentation.** Use the project's configured
   Python environment and existing verification tools. Inspect a documented
   command before running it; use help, read-only checks, or isolated disposable
   fixtures when a real invocation could alter records, Git configuration,
   branches, integration state, locks, or external systems. Check relative links,
   anchors, referenced files, command syntax, indexes, and consistency of all
   changed explanations. Run the existing protected-source check and TADp
   validator from the correct root, plus repository-required regression checks
   and any focused checks needed for changed examples. Preserve actual check
   output and exit status. Investigate introduced failures within this scope;
   report pre-existing failures or required executable fixes separately. Do not
   change tools, fixtures, assertions, or evidence merely to obtain a pass.

5. **Verify the repository boundary.** Confirm that all changes are within the
   authorized documentation paths. Do not synchronize to `_old/example/`, create
   a replacement mirror, edit another scaffold such as `TADp-v1/`, or access
   the separate example fork as an update target. Honor `.gitignore`: do not
   change ignore rules or force-add `_old/`. Example presence, parity, and
   application validation are not completion gates for this documentation task.
   Preserve historical records and report stale references that require
   separately authorized corrections without rewriting their source identity.

6. **Review coverage and the final diff.** Revisit every inventoried document
   and topic. Assign a truthful disposition: updated, reviewed and current,
   historical and preserved, protected and unchanged, out of scope, or blocked
   with the exact missing authority/evidence. Confirm that navigation reaches
   every added guide, no source identity or historical claim was rewritten, and
   no excluded file or unrelated work entered the change. Inspect whitespace,
   the complete scoped diff, and target-boundary compliance. Use
   traceable commits as required by repository instructions, staging only this
   task's files.
   Do not push, merge, create a pull request, release, or deploy from this task.
   Claim documentation completeness only for the reviewed scope with all
   unresolved gaps and failed or unperformed checks visible.

## Completion report

Report the documentation areas brought up to date and the evidence used to
establish current usage and supported features. Include the coverage inventory
and dispositions and exact changed protocol and repository support paths.
Confirm that no example synchronization or separate-fork work was performed.

Give the actual verification commands, roots, exit results, and limitations;
distinguish baseline findings, introduced findings, and checks not performed.
Identify remaining documentation gaps, protected-source proposals, executable
defects, conflicts, and any required human decisions. Report documentation
maintenance separately from initiative acceptance, lifecycle completion,
protocol adoption, and release; none is established by this refresh.
