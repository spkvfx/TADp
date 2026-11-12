# Traceable Architecture Design Protocol (TADp)

TADp organizes software work in a Git repository. It turns evidence and
explicit human decisions into focused initiatives whose results developers can
review and verify. To preserve traceability, TADp stores architectural
authority, background evidence, proposals, initiative specifications,
delivered products, verification, and lifecycle claims as separate but linked
records.

TADp is designed for work that must always provide clear answers to these
questions:

- What evidence governed this decision?
- Who had the authority to make it?
- What work did developers approve?
- Which change in the repository implemented the work?
- What evidence proves the exact completion claim?
- What remains unresolved, deferred, cancelled, or owned elsewhere?

## Explicit requirements

TADp requires both **Git** and **Codex**.

- **Git is required** because it gives the repository a stable identity and
  tracks initiative branches, reviewable commits, change history, and
  finalization evidence. A copied folder or a separate change log cannot
  replace Git.
- **Codex is required** because TADp's operating model is built around
  repository-level `AGENTS.md` instructions and workflow prompts written for
  Codex. The workflow also relies on Codex to inspect the repository, pause for
  human decisions, edit files, and verify work.

Other coding agents, IDE assistants, automation systems, or document tools may
be useful, but they are not direct replacements. They may differ in how they
find instructions, process prompts, request human input, manage files, use Git,
and report verification. Developers who adopt another tool must document a
compatibility review and may need to adapt the prompts, agent instructions,
templates, validator, or workflow. See
[Adapting TADp to other tools](docs/development/adapting-other-tools.md).

## Core traceability model

```text
binding evidence and explicit human decisions
                       |
                       v
version scope -> realization catalog -> focused initiatives
                       |
                       v
                    proposal
                       |
                       v
          delivered product or initiative evidence
                       |
                       v
             verification and completion evidence
                       |
                       v
             evidence-backed lifecycle status
```

The arrows show traceability between stages, not automatic promotion from one
stage to the next. A realization may lead to a proposal, but it is not a
requirement. A proposal does not authorize work. A product cannot revise its
governing specification, and a lifecycle status does not prove completion
without the required evidence.

The prospectively adopted scope revision gives each initiative exactly one
major (`vN`), minor (`vN.M`), or patch (`vN.M.P`) scope. Multiple narrow
initiatives may share a scope and source notes. New initiative paths are
`initiatives/<scope>/<type>/<id-and-slug>/`. Each initiative retains independent
acceptance, lifecycle and evidence. The LLM records exact source routing,
coherent same-initiative revision and necessary reopening under a human intake
instruction; changed claims require renewed human acceptance.

Execution uses a dedicated child or matching shared scope branch with per-member
attribution. Creation follows project base to major to minor to patch; dedicated
initiatives branch from their scope. Closure integrates child into recorded
immediate parent, bottom-up. Closing a member leaves its scope open; scope
closure is separately gated. See [adoption and operation](docs/guides/version-scope-migration.md).

Open initiative effort is also work to reconcile. Completion reviews account
for every other open initiative, preserve conflicting efforts in the
[work-conflict register](initiatives/work-conflicts.md), and route refinements
through their owning workflow. Closed claims require recorded authorized reopening before refinement;
adopted realization intake delegates necessary reopening, never acceptance. See the [coherence specification](evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md).

## Authority model

For every TADp request, Codex applies the canonical
[prompt keyword contract](evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md).
It defines positional directives, explicit exception records, action-list
scheduling, and an extensible registry. Defaults preserve existing gates;
reading examples grants no exception. See the
[adoption and extension guide](docs/guides/prompt-keywords-migration.md).

TADp uses a single authority hierarchy to decide which records govern the work:

1. [`evidence/authoritative/`](evidence/authoritative/README.md) contains
   binding invariant evidence. These invariants set rules that all
   lower-authority records must follow.
2. Accepted decisions and initiative specifications govern only their recorded
   scope and must remain compatible with authoritative evidence.
3. Verified products show what developers delivered, but existing code or
   behavior cannot override architectural authority.
4. [`evidence/non-authoritative/`](evidence/non-authoritative/README.md)
   contains clues, observations, research, examples, and advice. These sources
   may clarify an uncertain point, but they cannot override an invariant.

Codex must start by reading the binding
[LLM invariant suite](evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
The root [`AGENTS.md`](AGENTS.md) is the repository entry point for those
instructions. When records conflict, TADp records the conflict and routes it to
a person with authority to resolve it. The conflict must never be hidden by
quietly weakening a specification or completion claim.

## Repository structure

| Path | Role |
|---|---|
| [`.gitattributes`](.gitattributes) | Portable LF handling for protected text and hook scripts |
| [`.githooks/pre-commit`](.githooks/pre-commit) | Tracked validation and protected-source commit guard |
| [`AGENTS.md`](AGENTS.md) | Repository-wide Codex instructions |
| [`evidence/`](evidence/README.md) | Evidence and the authority level of each source |
| [`evidence/authoritative/`](evidence/authoritative/README.md) | Binding invariants and Codex protocol rules |
| [`evidence/non-authoritative/`](evidence/non-authoritative/README.md) | Background context that cannot override authority |
| [`evidence/non-authoritative/realizations/`](evidence/non-authoritative/realizations/README.md) | Permanently non-authoritative problems or goals that may lead to proposals |
| [`initiatives/`](initiatives/README.md) | Focused specifications for proposed, accepted, or completed work |
| [`products/`](products/README.md) | Locations and records for delivered products |
| [`prompts/`](prompts/README.md) | Non-authoritative project-local instructions confined to this scaffold |
| [`template/initiatives/`](template/initiatives/README.md) | Standard templates for initiative records |
| [`template/prompts/`](template/prompts/README.md) | Numbered Codex prompts and the shared workflow rules |
| [`template/project/`](template/project/README.md) | Reusable structure for adding TADp to another repository |
| [`tools/`](tools/README.md) | Protocol validator and instructions for using it |
| [`tests/`](tests/test_tadp_validate.py) | Tests for the validator |
| [`docs/`](docs/README.md) | Development and operating guides |

See [Repository layout](docs/development/repository-layout.md) for the full
rules about where each record belongs.

## Initiative workflow

Each initiative covers one focused outcome, one clear authority boundary, and
one acceptance claim that reviewers can judge on its own. The authority
boundary identifies the people and records that can approve the work. Outcomes
that can be accepted, verified, released, or cancelled separately become
sibling initiatives. A subinitiative is allowed only within a real parent
specification and must keep its own decisions, lifecycle, and verification.

The standard workflow is:

1. Assess realization fit and record append, revision/reopening or new narrow
   initiative placement. Preflight scope ancestors, membership, exact provenance
   and shared/dedicated assignment; create a branch only when required.
2. Create a proposal from an existing realization.
3. Compare the proposal with the evidence in the repository.
4. Create the complete initial initiative record, including its scope review.
5. Check the initiative against authoritative evidence and earlier accepted
   decisions.
6. Ask a human to resolve open assumptions and questions, then record each
   response in a decision receipt.
7. Present the complete bounded baseline for a separate explicit human
   acceptance decision and receipt.
8. Follow exactly one delivery path: implementation, design, or planning.
   Implementation also performs applicable SDK/API alignment and the read-only
   readiness review before product execution.
9. Maintain the type-specific execution or delivery record while performing
   only accepted work.
10. Create completion evidence and the cross-initiative coherence review for
    the exact accepted claim. Record `Completed` only when every in-scope gate
    passes and incompatible efforts have a compatible disposition.
11. Finalize traceable commits and perform authorized local child-to-parent
    integration or record verified direct scope hosting. Scope closure remains
    separate. Pull requests are independently human managed.

For the full sequence and the ownership of each record, see
[Initiative workflow](docs/development/initiative-workflow.md).

## Getting started

### Work on TADp itself

1. Open this repository with Codex at the repository root.
2. Read `AGENTS.md` and the authoritative LLM rules that apply to the work.
3. Confirm the current Git branch and inspect the complete worktree before
   editing.
4. Make the smallest coherent change, then update every document, template,
   prompt, test, and validator rule that depends on it.
5. Run the validator and its regression tests before review.

### Adopt TADp in another repository

1. Start with a repository root that has its own Git history.
2. Copy the complete protected [`template/`](template/README.md) tree into the
   target, preserving its `AGENTS.md` and `.tadp-lock.json`.
3. Copy the contents of [`template/project/`](template/project/README.md),
   including `.gitattributes`, `.githooks/`, and the canonical
   `prompts/AGENTS.md` and `prompts/README.md`, into the repository root.
   Specialize only destination copies, never the reusable source tree, and do
   not confuse root project-local `prompts/` with the protected numbered
   workflow at `template/prompts/`.
4. Copy the protected authoritative `evidence/authoritative/LLM/` suite into
   the same path in the target, preserving its scoped instructions and lock.
   Preserve the distribution decision receipts linked by that suite under
   `decisions/`; they retain their historical source identity and do not
   constitute decisions for the adopting project's work.
5. Copy the developer documentation, tools, and tests; run the protection check
   and configure `core.hooksPath=.githooks` in each clone or worktree.
6. Complete `project-profile.md`, assign ownership for each source of evidence,
   and create the initiative index, status record, and work-conflict register.
   Capture the pre-adoption Git commit in the coherence baseline field.

See [Getting started](docs/development/getting-started.md) for prerequisites,
setup options, and the first validation run.

## Validation

The validator uses only the Python standard library. From the protocol root
(`protocol/` in the reference repository and normally the project root in an
adopted repository):

```powershell
python tools/tadp_protect.py check .
python tools/tadp_validate.py .
python -m unittest discover -s tests -v
```

For machine-readable output:

```powershell
python tools/tadp_validate.py . --json
```

Passing validation confirms that the checked records follow TADp's structure
and traceability rules. It does not replace architecture review, human
decisions, product tests, release checks, or evidence from a production system.
See [Validation and quality](docs/development/validation-and-quality.md) for
details.

## Documentation index

The complete documentation index is at [`docs/README.md`](docs/README.md).

| Document | Purpose |
|---|---|
| [Getting started](docs/development/getting-started.md) | Requirements, setup, adoption, and first validation |
| [Architecture and authority](docs/development/architecture-and-authority.md) | Evidence order, authority boundaries, and conflicts |
| [Repository layout](docs/development/repository-layout.md) | Rules for where folders and records belong |
| [Initiative workflow](docs/development/initiative-workflow.md) | Workflow stages, records, human decisions, and lifecycle |
| [Git and Codex requirements](docs/development/git-and-codex-requirements.md) | Required behavior from Git and Codex |
| [Validation and quality](docs/development/validation-and-quality.md) | Validator behavior, tests, limits, and continuous integration (CI) |
| [Developing TADp](docs/development/developing-tadp.md) | How to change TADp and its supporting files |
| [Adapting other tools](docs/development/adapting-other-tools.md) | How to check and adapt a tool other than Codex |
| [Protected-source integrity migration](docs/guides/protected-source-integrity-migration.md) | How existing adopters establish reviewed template and invariant locks |
| [Project-local prompts migration](docs/guides/project-local-prompts-migration.md) | How existing adopters add the scoped root prompt workspace without weakening local instructions |
| [Legacy initiative decomposition](docs/guides/legacy-initiative-decomposition.md) | How to split an older, overly broad initiative safely |
| [Workflow stage 0–13 migration](docs/guides/workflow-stage-0-13-migration.md) | How to migrate an active initiative to explicit acceptance and type-specific delivery paths |
| [Version-realization-initiative correlation migration](docs/guides/version-realization-correlation-migration.md) | How to record the effective point and disposition or migrate legacy identities without inference |
| [Initiative coherence migration](docs/guides/initiative-coherence-migration.md) | How to adopt open-work reviews, conflict records, feedback, and closed-claim preservation |

## Development and contribution

Authoritative specifications set TADp's rules, while developer guides explain
them. A guide cannot weaken or replace a rule. Because many files depend on the
workflow contract, changing it usually requires matching updates to the
specification, Codex instructions, templates, prompts, validator, tests, and
documentation.

Read [Developing TADp](docs/development/developing-tadp.md) before changing the
protocol itself.

## Status

This repository is TADp's reference implementation and reusable template. Its
validator checks the protocol structure and traceability rules. Even so,
developers should begin with one small trial initiative before using the
workflow for many initiatives.
