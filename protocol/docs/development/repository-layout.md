# Repository layout

## Placement principle

TADp separates records by responsibility. Store an artifact according to what
it does, not merely its file type or author. A Markdown document can be
authoritative evidence, a proposal, an initiative specification, a product, or
an explanatory guide; its role and accepted authority determine its placement.

## Top-level structure

```text
.
|-- AGENTS.md
|-- README.md
|-- docs/
|   |-- README.md
|   |-- development/
|   `-- guides/
|-- evidence/
|   |-- authoritative/
|   |   `-- LLM/
|   `-- non-authoritative/
|-- initiatives/
|-- products/
|-- realizations/
|-- template/
|   |-- initiatives/
|   |-- project/
|   `-- prompts/
|-- tests/
`-- tools/
```

## Root files

### `../../AGENTS.md`

`../../AGENTS.md` is the persistent Codex entry point. It tells Codex to read the
authoritative suite, preserve evidence authority, enforce narrow initiatives,
pause for human decisions, use Git safely, and require lifecycle evidence.

Keep it concise enough to be loaded for every task. Put detailed explanations
in developer documentation and binding rules in authoritative evidence.

### `../../../README.md`

The root README is the human entry point. It explains the purpose, requirements,
core model, main workflow, validation commands, and documentation index. It
must not become a second invariant suite.

## Evidence

### `../../evidence/authoritative`

This is the single repository authority hierarchy. It contains accepted
architecture, binding rules, and other invariant evidence. The `LLM/` child
contains the Codex protocol suite.

Do not place exploratory alternatives here. Do not overwrite an earlier source
to make a later initiative appear aligned. Authorized revisions preserve their
predecessor, authority, reason, effective event, and compatibility effects.

### `../../evidence/non-authoritative`

This directory contains research, observations, examples, recommendations, and
other contextual evidence. These records can locate stronger evidence, expose
questions, or resolve ambiguity among invariant-compatible interpretations.
They cannot override authoritative evidence.

### `../../evidence/README.md`

The evidence README defines the classification boundary and points to the
canonical locations. Project-specific evidence registers may add stable IDs,
owners, revisions, and review dates.

## Realizations

`../../realizations` contains broad descriptions of opportunities, problems, or
desired outcomes. A realization is proposal input. It is not an accepted
requirement, a confirmed assumption, an implementation authorization, or
completion evidence.

Preserve the realization's source identity when creating a proposal. Correct
its interpretation in initiative records rather than rewriting historical
input silently.

## Initiatives

`../../initiatives` contains actual specifications for bounded work. Each initiative
must own one outcome, one coherent authority boundary, and one independently
reviewable acceptance claim.

The canonical initial suite contains:

- `../../../README.md` for identity, type, scope, lifecycle, and links;
- `proposal/README.md` and `proposal/proposal.md` for source inventory and the
  working proposal;
- `assumption.md` for stable assumptions and human dispositions;
- `scope-assessment.md` for cohesion and split-trigger analysis;
- `architecture.md` for the repository-specific specification;
- `source-mapping.md` for source-to-claim-to-output-to-verification tracing;
- `open-questions.md` for unresolved human decisions;
- `implementation-roadmap.md` for dependency and gate ordering; and
- `implementation-steps.md` for reviewable changes and verification.

Later-stage records include `decision-receipts/`,
`implementation-readiness.md`, `execution-record.md`, and
`completion-evidence.md`. Do not create a later-stage record merely to make the
initial suite look complete.

## Products

`../../products` contains product records or actual products when that placement is
appropriate. A product may also live in source, package, API, deployment, or
documentation paths elsewhere in the repository. Its product record should
identify the actual destination, governing initiative and specification,
applicable evidence, owner, and verification.

A product demonstrates delivered behavior; it does not revise the initiative
or invariant that governed it.

## Templates

### `../../template/initiatives`

This is the single canonical initiative template suite for implementation,
design, and planning initiatives. Type changes what output is permitted, not
which core records are required.

### `../../template/prompts`

The numbered prompts define stage-specific Codex workflows. The shared
`WORKFLOW-CONTRACT.md` centralizes common authority, scope, human-decision, Git,
lifecycle, and reporting rules. Numbered prompts remain detailed and retain
their own preconditions and edit boundaries.

Example sections use “attached initiative” as invocation language. Executable
prompt blocks use the `&#123;initiative&#125;` placeholder and must not depend on a
specific project name or filesystem location.

### `../../template/project`

This tree is copied when another repository adopts TADp. It provides project
instructions, evidence structure, profile, initiative indexes, status, and
product records. The authoritative LLM suite is copied separately into the
target's `../../evidence/authoritative/LLM` path.

## Documentation, tools, and tests

- `` explains adoption and maintenance.
- `../guides` contains focused non-authoritative procedures.
- `../../tools/tadp_validate.py` enforces machine-checkable protocol contracts.
- `../../tests/test_tadp_validate.py` protects validator behavior.

Do not move binding rules into `..` merely because prose is easier to edit.
Do not add validator behavior without a documented protocol reason and a
regression test.

