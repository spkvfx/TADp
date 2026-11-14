# Developing TADp

This guide orients contributors to this repository. It is explanatory; read
[root instructions](../AGENTS.md), the invoked
[maintenance-prompt instructions](../prompts/AGENTS.md) when applicable, and
[P's instructions](../TADp/AGENTS.md). The installed
[project-owned workflow](../TADp/docs/development/tadp-development-workflow.md)
owns the detailed procedure. Project governance, decisions, manifests, test
results and completion history stay in P, never in this repository guide.

## Contributor setup and targets

Resolve [the checkout layout](repository-layout.md): R is Git root,
P=`R/TADp`, C=`P/protocol`, D=`P/template`, U=`R/protocol`, S=`U/template`.
Read the project [profile](../TADp/project-profile.md), actual owner/adoption
decisions and governing suite. Inspect branch, immutable HEAD, staged,
unstaged, untracked and ignored work before writes. Preserve unrelated work;
do not create an initiative execution assignment from a suggestive branch name.
The project integration branch was unassigned at documentation preflight;
resolve the actual current configuration before scope allocation.

An explicitly invoked root `prompts/` maintenance instruction must name the
exact candidate work and target. It cannot silently reuse an older distribution
target for experimentation. P's local `prompts/AGENTS.md` stays unchanged:
copying a prompt or changing cwd cannot elevate it into generic maintenance.
The protected numbered workflow is separately located at `template/prompts/`.

Develop and qualify candidate work in C. After the required human acceptance
and exact protected-source authority, introduce proven reusable content into D.
Record actual type-specific development completion. Then promote the sanitized
manifest from its immutable completed revision into S under exact authority;
only afterward roll out from the pinned promoted revision to mapped U consumers.
The workflow owns gates at every boundary. Qualification proves no introduction;
completion proves no promotion; rollout proves no adoption or release.

## Change classification

Classify the requested work before editing, against its authoritative basis.

| Class | Examples | Handling |
|---|---|---|
| Authoritative revision | Evidence precedence, lifecycle, Git or decision rule | Exact human revision authority, preserved predecessor and reconciled consumers |
| Reusable workflow | Prompt prerequisite, template field, scaffold | Invariant compatibility, exact protected-change authority and consumer checks |
| Validator | Structural rule, finding code or parser | Governing protocol basis and meaningful regressions |
| Explanatory docs | Clarification, tutorial or navigation | Preserve authority and source identity; create no implicit rule |
| Focused guide | Adoption, migration or decomposition | Link the owning specifications and preserve earlier compatible claims |

Do not move an invariant into a guide to avoid revision requirements or change
an invariant to fit convenient implementation. The applicable
[suite](../TADp/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md)
governs; candidate replacements are proposals until actually authorized.

## Before editing

Read applicable specifications, inspect actual Git state, inventory open and
partially performed effort and affected closed claims, and locate every
consumer of changed paths, terms, fields and contracts. Record compatibility,
migration, exact source/destination operations, authority and recovery in P.
Use the required traceable scope/branch assignment before initiative execution.
Missing authority permits preparation and proposals within their authorized
boundary, not inferred acceptance or protected edits.

## Coordinated update surfaces

Review governing specifications, root/scoped instructions, initiative templates,
profile fields, shared workflow contract, numbered prompts, tools, regressions,
documentation and migration guides. Inspect actual correlation and initiative
consumers without turning their existence into edit permission. Record why each
mapped consumer changes, remains unchanged or needs separately authorized work.
Do not rewrite historical records to conceal incompatibility. The separate
example repository is not a mirror or protocol validation target.

## Template rules

Select existing canonical sources with the
[coverage map](../TADp/template/TEMPLATE-COVERAGE.md), including embedded,
conditional and response-shape sources. Copy to the declared destination
outside protected trees before specialization. Keep required sections and
explain conditional non-applicability. Preserve one canonical initiative suite
across types, later-stage record triggers, scoped placeholders and subinitiative
support without umbrella claims. Never embed a project's appointment, decision,
path or current verification result in a reusable source.

## Protected-source changes

The installed and upstream reusable libraries and authoritative suites have
scoped guards and SHA-256 locks. For an exact authorized revision, preserve
the prior Git/lock identities, review consumers and migration, make coherent
changes through the serial route, and verify before refreshing only the
explicitly authorized affected lock. Recheck integrity, structure and regressions
afterward. A stale lock records drift; it cannot authorize a change. Matching
one-commit protected-update variables are permissible only under that same
actual exact authority; never leave them set for unrelated later work.

## Prompt rules

The [keyword specification](../TADp/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
owns directives and list scheduling. Keep inert examples distinct from
operative instructions and preserve exact authorization. A new keyword needs
its exact registry revision authority, consumers, checks and governed lock;
no competing allowlist or override registry is permitted.

Numbered prompts retain the shared contract link, stage-specific prerequisites,
documentary preparation, edit boundary, verification and reporting. They have
reference-only examples using “attached initiative” and executable placeholders
such as `&#123;initiative&#125;`. Centralize only shared rules; preserve the
distinction between missing paperwork and missing facts/authority. Stage 9's
assessment remains read-only after disclosed lawful preparation. Review actual
semantics as well as structural fixture results.

## Git workflow for TADp changes

Discover actual integration configuration and recorded dedicated/shared scope
placement; preserve captured bases and initiative-specific commits. Serialize
shared writes and stage only the authorized diff. A coherent governing revision
includes authorized sources, consumers, verification and matching locks. Record
actual commit identities after creation, never a predicted self-reference.
Workflow revisions need separately authorized migration and historical prompt
identities. No merge, push, PR, branch deletion, publication or release follows
from a documentation change.

## Verification checklist

Use the configured Python SDK obtained from environment tooling. From R, the
following reference commands select P and U explicitly:

```powershell
& $TadpPython TADp/tools/tadp_protect.py check TADp
& $TadpPython TADp/tools/tadp_validate.py TADp
& $TadpPython protocol/tools/tadp_protect.py check protocol
& $TadpPython protocol/tools/tadp_validate.py protocol
# Existing distribution regressions: working directory U
& $TadpPython -m unittest discover -s tests
```

Qualify candidate fragments in a clean isolated assembly of pinned baseline
plus exact declared changes, without populated P records or R/docs. Check
relative links and anchors, indexes, component maps, commands, protected
identities, compatible consumers and sanitation; obtain independent review.
Retain actual commands, environment, bytes/digests, findings and recovery in P.
The [owning verification record](../TADp/evidence/non-authoritative/documentation-split/preparation.md#baseline-checks)
records this task's baseline findings. A baseline failure is not permission
to repair profiles, weaken checks or refresh locks in a documentation task.

For separately authorized validator development, identify the governing
contract, choose a stable precise finding, avoid inferring semantic authority,
add meaningful passing/failing regressions, update tool/user documentation,
and run checks in C through the same controlled delivery route. No validator
or regression source is changed by this split.

## Hook coordination

Inspect default hooks and `git config --show-origin --get core.hooksPath`
at R before a deliberate local configuration decision. A selected protocol
distribution hook uses Git-relative `protocol/.githooks`; P uses
`TADp/.githooks`. They share one configuration and need a manually coordinated
dispatcher if both apply. Copying installs no hook. Set `TADP_PYTHON` to the
configured executable as needed. The older root `.githooks/pre-commit` expects
an `example/` tree and requires separately authorized executable maintenance;
this task neither enables nor repairs it.

## Releasing a protocol revision

A release is separately authorized. It needs an actual version/revision,
authoritative-change and migration record, preserved baseline and representative
workflow evidence. Markdown quality alone proves no executable workflow or
production readiness. The supplied separate example location establishes no
parity, conformance or adoption.

## Source attribution and current split

This page extracts maintenance explanations from the distribution's
`docs/development/developing-tadp.md`, `getting-started.md`,
`repository-layout.md` and `validation-and-quality.md`, and the old root README,
at source commit `014d455e3d99213e0dc4a156cb198ac1a4a85747`. The original content
and prior authority remain in Git. No license or governing source is moved.
Portable revisions are candidate preparation only; see the
[exact map and pending gates](../TADp/evidence/non-authoritative/documentation-split/preparation.md).
The distributed guides remain unchanged until authorized delivery, so the
transition currently has historical overlap rather than a completed move.
