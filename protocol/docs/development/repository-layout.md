# Repository layout

## Placement principle

TADp separates records by responsibility. Store an artifact according to what
it does, not merely its file type or author. A Markdown document can be
authoritative evidence, a proposal, an initiative specification, a product, or
an explanatory guide; its role and accepted authority determine its placement.

## Top-level structure

The tree below describes a project after adoption of the current scope model.
In the reference checkout these paths live under `protocol/`; its enclosing
repository also has maintenance prompts. A legacy project keeps its recorded
paths and compatible revision until explicitly migrated.

```text
.
|-- .gitattributes
|-- .githooks/
|-- AGENTS.md
|-- README.md
|-- docs/
|   |-- README.md
|   |-- development/
|   `-- guides/
|-- evidence/
|   |-- authoritative/
|   |   `-- LLM/
|   |       |-- .tadp-lock.json
|   |       `-- AGENTS.md
|   `-- non-authoritative/
|       `-- realizations/
|-- initiatives/
|   |-- initiative-index.md
|   |-- version-scopes.md
|   |-- version-scope-migration-ledger.md
|   |-- version-correlation-migration-ledger.md
|   |-- work-conflicts.md
|   |-- status.md
|   `-- <scope>/<type>/<id-and-slug>/
|-- products/
|-- prompts/
|   |-- AGENTS.md
|   `-- README.md
|-- template/
|   |-- .tadp-lock.json
|   |-- AGENTS.md
|   |-- TEMPLATE-COVERAGE.md
|   |-- initiatives/
|   |-- project/
|   |   `-- prompts/
|   `-- prompts/
|-- tests/
`-- tools/
```

## Root files

### `../../.gitattributes`

The copied attributes keep protected UTF-8 text and executable hook scripts on
LF line endings across Git clients. Integrity hashing also normalizes UTF-8
line endings, so platform conversion does not create false drift.

### `../../AGENTS.md`

`../../AGENTS.md` is the persistent Codex entry point. It tells Codex to read the
authoritative suite, preserve evidence authority, enforce narrow initiatives,
pause for human decisions, use Git safely, and require lifecycle evidence.

Keep it concise enough to be loaded for every task. Put detailed explanations
in developer documentation and binding rules in authoritative evidence.

It also declares `template/**` and `evidence/authoritative/LLM/**` protected.
Directory-scoped `AGENTS.md` files repeat that boundary where Codex loads the
most local instructions.

### `../../.githooks/pre-commit`

The tracked hook runs validation and the staged protected-source guard. Git
does not activate tracked hooks automatically; every clone or worktree must set
`core.hooksPath` to `.githooks`.

### `README.md`

The root README is the human entry point. It explains the purpose, requirements,
core model, main workflow, validation commands, and documentation index. It
must not become a second invariant suite.

## Evidence

### `../../evidence/authoritative`

This is the single repository authority hierarchy. It contains accepted
architecture, binding rules, and other invariant evidence. The `LLM/` child
contains the Codex protocol suite. Its scoped `AGENTS.md` makes ordinary work
read-only, while `.tadp-lock.json` records the authorized file set and SHA-256
digests.

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

`../../evidence/non-authoritative/realizations` is the only realization
location. It contains broad descriptions of opportunities, problems, or
desired outcomes. A realization is permanently non-authoritative proposal
input. It is not an accepted requirement, a confirmed assumption, an
implementation authorization, or completion evidence.

When an authority accepts a claim derived from a realization, record that
claim in a separate authoritative evidence, decision, or accepted initiative
record. Do not promote or reclassify the source realization in place.

Preserve the realization's source identity when creating a proposal. Correct
its interpretation in initiative records rather than rewriting historical
input silently.

Under the adopted scope revision, the suite index catalogs exact source notes
and their routing to existing or new initiatives. Shared sources and several
targets are valid; each initiative still has one immutable scope membership.
Preserve source scope separately from the selected target scope and link the
canonical membership and source-mapping records. Earlier one-to-one tuples
retain their recorded predecessor contract until explicitly migrated. See
[scope operation](../guides/version-scope-migration.md).

## Initiatives

`../../initiatives` contains actual specifications for bounded work. Each initiative
must own one outcome, one coherent authority boundary, and one independently
reviewable acceptance claim.

`initiative-index.md` owns membership and exact multi-note provenance.
`version-scopes.md` owns scope identity, hierarchy, captured bases, closure and
integration. New paths are `initiatives/<scope>/<type>/<id-and-slug>/`.
Scope READMEs link to these owners; initiative READMEs own lifecycle. Project
status, migration ledgers and work-conflict registers remain project-level.
`version-correlation-migration-ledger.md` preserves pre-effective identities
and their `Unmigrated`, `Deferred`, or separately authorized migration
dispositions without inference.

The canonical initial suite contains:

- `README.md` for identity, type, scope, lifecycle, and links;
- `proposal/README.md` and `proposal/proposal.md` for source inventory and the
  working proposal;
- `assumption.md` for stable assumptions and human dispositions;
- `scope-assessment.md` for cohesion and split-trigger analysis;
- `architecture.md` for the repository-specific specification;
- `source-mapping.md` for source-to-claim-to-output-to-verification tracing;
- `open-questions.md` for unresolved human decisions;
- `implementation-roadmap.md` for dependency and gate ordering; and
- `implementation-steps.md` for reviewable changes and verification.

Later-stage durable records include `decision-receipts/`, `execution-record.md`,
`delivery-record.md`, and `completion-evidence.md`, only when their actual
decisions, work or verification trigger them. `implementation-readiness.md` is
a reusable response shape for Stage 9, not a required initiative-local file;
a durable readiness record needs an explicit governing requirement. Do not
create later records merely to make the initial suite look complete.

## Products

`../../products` contains product records or actual products when that placement is
appropriate. A product may also live in source, package, API, deployment, or
documentation paths elsewhere in the repository. Its product record should
identify the actual destination, governing initiative and specification,
applicable evidence, owner, and verification.

A product demonstrates delivered behavior; it does not revise the initiative
or invariant that governed it.

## Project-local prompts

`../../prompts` is the current scaffold's workspace for non-authoritative
instructions about that project. Its direct `AGENTS.md` resolves the scaffold
from its own installed location, applies recursively below root `prompts/`,
and confines every side effect to that scaffold and any narrower invoked-prompt
boundary. `README.md` explains suitable project subjects and the protocol
maintenance work excluded from this location.

The canonical reusable files live at
`../../template/project/prompts/AGENTS.md` and
`../../template/project/prompts/README.md`. Those sources are protected by
the template lock; their installed root copies and additional project-local
prompt files are ordinary working material. The installed canonical content
must remain present, but compatible stricter local instructions may narrow it.

Root `prompts/` is distinct from `../../template/prompts`. The latter is the
protected numbered initiative workflow and shared contract. Do not duplicate
that library into the project-local workspace or treat a local prompt as
authoritative evidence, initiative acceptance, gate evidence, or lifecycle
proof.

In this reference repository, outer repository-level `prompts/` contains
maintenance requests for TADp itself. Its instructions determine that target;
the nested `protocol/prompts/` remains the distributable project-local
workspace. Neither location becomes the protected workflow library merely
because it contains Markdown instructions.

When the scaffold is embedded in a larger Git repository for distribution or
testing, the enclosing Git root does not enlarge the project-local boundary or
make the embedded scaffold a compliant governed project.

## Templates

The entire `../../template` tree is protected reusable source. Its scoped
`AGENTS.md` prohibits in-place specialization, and `.tadp-lock.json` makes
unexpected additions, removals, and byte changes validator errors. Copy a
record to its declared destination outside this tree before editing it.

The [canonical coverage map](../../template/TEMPLATE-COVERAGE.md) selects file,
embedded-section, conditional and response-shape sources by role and owning
stage. The [preparation contract](../../template/prompts/WORKFLOW-CONTRACT.md#documentary-prerequisite-preparation)
permits recovery of necessary documentary inputs from sufficient actual
evidence before a substantive step's entry check; it never invents identity,
authority, work or verification. Recompute relative links from the instance's
actual directory depth.

### `../../template/initiatives`

This is the single canonical initiative template suite for implementation,
design, and planning initiatives. Type changes what output is permitted, not
which core records are required.

It also contains Stage 0 preparation skeletons and type-specific execution,
delivery, and completion templates. Realization-suite and migration-ledger
templates live under `template/project` at their project destinations.

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
product records, plus the canonical project-local `prompts/AGENTS.md` and
`prompts/README.md`. The authoritative LLM suite is copied separately into
the target's `../../evidence/authoritative/LLM` path.

## Documentation, tools, and tests

- `docs/` explains adoption and maintenance.
- `../guides` contains focused non-authoritative procedures.
- `../../tools/tadp_validate.py` enforces machine-checkable protocol contracts.
- `../../tools/tadp_protect.py` checks and deliberately maintains the two
  protected-source locks and provides the staged-change guard.
- `../../tests/test_tadp_validate.py` protects validator behavior.

Do not move binding rules into `..` merely because prose is easier to edit.
Do not add validator behavior without a documented protocol reason and a
regression test.

