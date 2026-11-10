# Traceable Architecture Design Protocol (TADp)

TADp is a repository protocol for turning evidence and human decisions into
narrowly scoped, verifiable initiatives and products. It keeps architectural
authority, contextual evidence, proposals, initiative specifications, product
outputs, verification, and lifecycle claims separate while preserving the
links between them.

TADp is intended for work where it must remain possible to answer:

- Which evidence governed this decision?
- Who had authority to make it?
- What exact work was accepted?
- Which repository change implemented it?
- What evidence proves the bounded completion claim?
- What remains unresolved, deferred, cancelled, or owned elsewhere?

## Explicit requirements

TADp requires both **Git** and **Codex**.

- **Git is required** for repository identity, initiative branches, reviewable
  commits, change history, and finalization evidence. A copied directory or an
  external change log is not an equivalent substitute.
- **Codex is required** because the protocol uses repository-level
  `AGENTS.md`, Codex-oriented workflow prompts, persistent repository
  inspection, human decision pauses, and tool-supported editing and
  verification as part of its operating contract.

Other coding agents, IDE assistants, automation systems, or document tools may
be usable, but they are not drop-in replacements. Their instruction discovery,
prompt transport, human-interaction model, filesystem tools, Git behavior, and
verification reporting may differ. Adopting another tool therefore requires a
documented compatibility review and may require modifications to the prompts,
agent instructions, templates, validator, or workflow. See
[Adapting TADp to other tools](docs/development/adapting-other-tools.md).

## Core traceability model

```text
authoritative evidence and explicit human authority
                         |
                         v
realization -> proposal -> narrow initiative specification
                         |
                         v
          product or initiative-evidence output
                         |
                         v
        verification and completion evidence
                         |
                         v
             truthful lifecycle status
```

The arrow represents traceability, not automatic promotion. A realization does
not become a requirement merely because it produced a proposal. A proposal
does not authorize execution. A product does not revise its governing
specification. A status does not prove completion without the required
evidence.

## Authority model

TADp uses one canonical authority hierarchy:

1. [`evidence/authoritative/`](evidence/authoritative/README.md) contains
   binding invariant evidence.
2. Accepted decisions and initiative specifications govern only their recorded
   scope and must remain compatible with authoritative evidence.
3. Verified products show what exists, but implemented behavior does not
   override architectural authority.
4. [`evidence/non-authoritative/`](evidence/non-authoritative/README.md)
   contains clues, observations, research, examples, and recommendations that
   may resolve ambiguity but cannot override an invariant.

Codex must begin with the binding
[LLM invariant suite](evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
The root [`AGENTS.md`](AGENTS.md) is the repository entry point for those
instructions. A contradiction is recorded and routed; it is never hidden by
silently weakening a specification or completion claim.

## Repository structure

| Path | Role |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Persistent Codex instructions for working in this repository |
| [`evidence/`](evidence/README.md) | Repository evidence and its authority classification |
| [`evidence/authoritative/`](evidence/authoritative/README.md) | Binding invariants and the Codex protocol suite |
| [`evidence/non-authoritative/`](evidence/non-authoritative/README.md) | Context and clues that cannot supersede authority |
| [`realizations/`](realizations/README.md) | Broad observations or desired outcomes used as proposal inputs |
| [`initiatives/`](initiatives/README.md) | Narrow, coherent specifications for proposed, accepted, or completed work |
| [`products/`](products/README.md) | Product placements and records of delivered outputs |
| [`template/initiatives/`](template/initiatives/README.md) | Canonical initiative record templates |
| [`template/prompts/`](template/prompts/README.md) | Numbered Codex workflow prompts and shared workflow contract |
| [`template/project/`](template/project/README.md) | Reusable structure for adopting TADp in another repository |
| [`tools/`](tools/README.md) | Protocol validator and tool documentation |
| [`tests/`](tests/test_tadp_validate.py) | Validator regression tests |
| [`docs/`](docs/README.md) | Developer documentation and operating guides |

For the full placement rules, see
[Repository layout](docs/development/repository-layout.md).

## Initiative workflow

Every initiative owns one narrow outcome, one coherent authority boundary, and
one independently reviewable acceptance claim. Independent outcomes become
sibling initiatives. A subinitiative is permitted only inside a real parent
specification and retains its own decisions, lifecycle, and verification.

The standard workflow is:

1. Prepare a dedicated Git branch from the actual captured base branch.
2. Create a proposal from an existing realization.
3. Align the proposal to repository evidence.
4. Create the complete initial initiative record, including its scope
   assessment.
5. Align the initiative to authority and existing precedent.
6. Obtain explicit human dispositions for assumptions and open questions,
   recording a decision receipt for each governing response.
7. For implementation initiatives, align affected SDK/API surfaces and perform
   the read-only implementation-readiness review.
8. Execute only accepted work, maintaining the standard execution record.
9. Create completion evidence for the exact bounded claim.
10. Finalize the branch and pull request without silently merging, deploying,
    or deleting history.

The detailed sequence and artifact ownership are documented in
[Initiative workflow](docs/development/initiative-workflow.md).

## Getting started

### Work on TADp itself

1. Open this repository with Codex at the repository root.
2. Read `AGENTS.md` and the applicable authoritative LLM specifications.
3. Confirm the current Git branch and inspect the complete worktree before
   editing.
4. Make the smallest coherent change and update documentation, templates,
   prompts, tests, and validator rules that consume the changed contract.
5. Run the validator and its regression tests before review.

### Adopt TADp in another repository

1. Use a repository root with its own Git metadata.
2. Copy the reusable [`template/project/`](template/project/README.md)
   structure into the target repository.
3. Copy `template/initiatives/` and `template/prompts/` into a stable template
   root in the target, or record a pinned external TADp template root.
4. Copy the authoritative `evidence/authoritative/LLM/` suite into the same
   target path and retain the project-level `AGENTS.md`.
5. Complete `project-profile.md`, establish evidence ownership, and create the
   initiative index and status record.
6. Copy the developer documentation, validator, and tests when the target
   project is expected to enforce the complete reference structure.

See [Getting started](docs/development/getting-started.md) for prerequisites,
adoption paths, and the first validation run.

## Validation

The validator uses only the Python standard library. From the repository root:

```powershell
python tools/tadp_validate.py .
python -m unittest discover -s tests -v
```

For machine-readable output:

```powershell
python tools/tadp_validate.py . --json
```

Passing validation means the checked structural and traceability rules are
satisfied. It does not replace architectural review, human decisions, product
tests, release qualification, or production evidence. See
[Validation and quality](docs/development/validation-and-quality.md).

## Documentation index

The complete documentation index is at [`docs/README.md`](docs/README.md).

| Document | Purpose |
|---|---|
| [Getting started](docs/development/getting-started.md) | Prerequisites, setup, adoption, and first validation |
| [Architecture and authority](docs/development/architecture-and-authority.md) | Evidence precedence, authority boundaries, and conflict handling |
| [Repository layout](docs/development/repository-layout.md) | Directory and artifact placement rules |
| [Initiative workflow](docs/development/initiative-workflow.md) | End-to-end stages, records, human gates, and lifecycle |
| [Git and Codex requirements](docs/development/git-and-codex-requirements.md) | Required platform behavior and integration assumptions |
| [Validation and quality](docs/development/validation-and-quality.md) | Validator behavior, tests, limits, and CI use |
| [Developing TADp](docs/development/developing-tadp.md) | How to change the protocol, templates, prompts, and specifications |
| [Adapting other tools](docs/development/adapting-other-tools.md) | Compatibility analysis and modification checklist for non-Codex tools |
| [Legacy initiative decomposition](docs/guides/legacy-initiative-decomposition.md) | Safely splitting a historical broad initiative |

## Development and contribution

Changes to TADp must preserve the distinction between authoritative
specifications and explanatory developer documentation. A guide may explain a
rule but cannot weaken or replace it. Changes to a workflow contract normally
require coordinated updates to its authoritative specification, Codex
instructions, templates, prompts, validator, tests, and documentation.

Read [Developing TADp](docs/development/developing-tadp.md) before changing the
protocol itself.

## Status

This repository is the TADp reference implementation and reusable template.
Its validator checks protocol structure and traceability contracts; practical
adoption should still begin with a small pilot initiative before applying the
workflow to a large portfolio.

