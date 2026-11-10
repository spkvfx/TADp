# Traceable Architecture Design Protocol (TADp)

TADp is a protocol for organizing software work in a Git repository. It turns
evidence and human decisions into focused initiatives with results that a team
can verify. TADp stores each type of record separately, including authoritative
architecture rules, background evidence, proposals, initiative specifications,
delivered products, verification, and lifecycle status. It also keeps clear
links between these records.

TADp is intended for work where it must remain possible to answer:

- What evidence governed this decision?
- Who had the authority to make it?
- What work did the team approve?
- Which change in the repository carried out the work?
- What evidence proves the exact completion claim?
- What is still open, delayed, cancelled, or owned somewhere else?

## Explicit requirements

TADp requires both **Git** and **Codex**.

- **Git is required** to identify the repository and track initiative branches,
  commits, change history, and the evidence used to finalize the work. A copied
  folder or a separate change log cannot replace Git.
- **Codex is required** because TADp depends on repository-level `AGENTS.md`
  instructions and workflow prompts written for Codex. It also depends on how
  Codex inspects the repository, pauses for human decisions, edits files, and
  verifies work.

Other coding agents, IDE assistants, automation systems, or document tools may
be useful, but they are not direct replacements. They may handle instructions,
prompts, human input, files, Git, and verification reports in different ways.
Before using another tool, document a review of its compatibility with TADp.
You may also need to change the prompts, agent instructions, templates,
validator, or workflow. See
[Adapting TADp to other tools](docs/development/adapting-other-tools.md).

## Core traceability model

```text
binding evidence and approved human decisions
                       |
                       v
realization -> proposal -> focused initiative specification
                       |
                       v
          delivered product or initiative evidence
                       |
                       v
             verification and completion evidence
                       |
                       v
                 supported lifecycle status
```

The arrows show how the records link to each other. They do not mean that one
record automatically becomes another. A realization does not become a
requirement just because it led to a proposal. A proposal does not approve
work. A product cannot change the specification that governs it. A status does
not prove completion without the required evidence.

## Authority model

TADp uses one order of authority to decide which records govern the work:

1. [`evidence/authoritative/`](evidence/authoritative/README.md) contains
   binding invariant evidence. An invariant is a rule that work with less
   authority must follow.
2. Accepted decisions and initiative specifications govern only the scope they
   record. They must follow the authoritative evidence.
3. Verified products show what the team delivered, but existing code or
   behavior cannot override an architecture rule.
4. [`evidence/non-authoritative/`](evidence/non-authoritative/README.md)
   contains clues, observations, research, examples, and advice. These sources
   may help explain an unclear point, but they cannot override an invariant.

Codex must start by reading the binding
[LLM invariant suite](evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
The root [`AGENTS.md`](AGENTS.md) is the repository entry point for those
instructions. If two records conflict, TADp records the conflict and sends it
to the proper decision-maker. It never hides a conflict by quietly weakening a
specification or completion claim.

## Repository structure

| Path | Role |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Repository-wide Codex instructions |
| [`evidence/`](evidence/README.md) | Evidence and the authority level of each source |
| [`evidence/authoritative/`](evidence/authoritative/README.md) | Binding invariants and Codex protocol rules |
| [`evidence/non-authoritative/`](evidence/non-authoritative/README.md) | Background context that cannot override authority |
| [`realizations/`](realizations/README.md) | Broad problems or goals that may lead to proposals |
| [`initiatives/`](initiatives/README.md) | Focused specifications for proposed, accepted, or completed work |
| [`products/`](products/README.md) | Locations and records for delivered products |
| [`template/initiatives/`](template/initiatives/README.md) | Standard templates for initiative records |
| [`template/prompts/`](template/prompts/README.md) | Numbered Codex prompts and the shared workflow rules |
| [`template/project/`](template/project/README.md) | Reusable structure for adding TADp to another repository |
| [`tools/`](tools/README.md) | Protocol validator and instructions for using it |
| [`tests/`](tests/test_tadp_validate.py) | Tests for the validator |
| [`docs/`](docs/README.md) | Development and operating guides |

To learn where each record belongs, see
[Repository layout](docs/development/repository-layout.md).

## Initiative workflow

Each initiative has one focused outcome, one clear authority boundary, and one
acceptance claim that reviewers can judge on its own. Separate outcomes become
sibling initiatives. The authority boundary identifies the people and records
that can approve the work. A subinitiative is allowed only under a real parent
specification. It must still have its own decisions, lifecycle, and
verification.

The standard workflow is:

1. Record the real base branch, then create a separate Git branch for the
   initiative.
2. Create a proposal from an existing realization.
3. Check the proposal against the evidence in the repository.
4. Create the full initial initiative record, including a review of its scope.
5. Check the initiative against authoritative evidence and earlier accepted
   decisions.
6. Ask a human to decide open assumptions and questions. Save each answer in a
   decision receipt.
7. For coding initiatives, check the affected SDKs and APIs. Then complete the
   read-only readiness review before coding begins.
8. Perform only approved work and keep the standard execution record, or work
   log, up to date.
9. Create completion evidence for the exact approved claim.
10. Prepare the branch and pull request for review. Do not merge, deploy, or
    delete history without explicit approval.

For the full sequence and the owner of each record, see
[Initiative workflow](docs/development/initiative-workflow.md).

## Getting started

### Work on TADp itself

1. Open this repository with Codex at the repository root.
2. Read `AGENTS.md` and the authoritative LLM rules that apply to the work.
3. Confirm the current Git branch and review all current changes before
   editing files.
4. Make the smallest complete change. Update every document, template, prompt,
   test, and validator rule that depends on it.
5. Run the validator and its regression tests before review.

### Adopt TADp in another repository

1. Start with a repository that has its own Git history.
2. Copy the reusable [`template/project/`](template/project/README.md)
   structure into that repository.
3. Copy `template/initiatives/` and `template/prompts/` into a stable template
   folder in the target. Another option is to record a fixed, or pinned,
   external TADp template root.
4. Copy the authoritative `evidence/authoritative/LLM/` suite into the same
   path in the target, and keep the project-level `AGENTS.md`.
5. Complete `project-profile.md`. Assign an owner to each source of evidence,
   then create the initiative index and status record.
6. Copy the developer documentation, validator, and tests when the target
   project needs to enforce the full TADp structure.

See [Getting started](docs/development/getting-started.md) for prerequisites,
setup options, and the first validation run.

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

Passing validation means the checked records follow TADp's structure and
traceability rules. It does not replace architecture review, human decisions,
product tests, release checks, or evidence from a production system. See
[Validation and quality](docs/development/validation-and-quality.md).

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
| [Legacy initiative decomposition](docs/guides/legacy-initiative-decomposition.md) | How to split an older, overly broad initiative safely |

## Development and contribution

TADp keeps authoritative specifications separate from developer guides.
Specifications set the rules, while guides explain them. A guide cannot weaken
or replace a rule. A change to the workflow will usually require matching
updates to the specification, Codex instructions, templates, prompts,
validator, tests, and documentation.

Read [Developing TADp](docs/development/developing-tadp.md) before changing the
protocol itself.

## Status

This repository is TADp's reference implementation, or official example, and a
reusable template. Its validator checks the protocol structure and traceability
rules. Teams should still begin with one small trial initiative before using
the workflow for many initiatives.

