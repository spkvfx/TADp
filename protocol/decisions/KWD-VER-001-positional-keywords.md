# Positional prompt keywords maintenance verification

**Record ID:** KWD-VER-001

**Authority:** [KWD-DR-001](KWD-DR-001-positional-keywords.md)

**Status:** Verified 2026-11-12 and recorded through the guarded delivery commit

**Captured Git baseline:** `fb1e241ca89303abf6376bf53a897d54ab42c617`

**Maintenance branch:** `protocol/positional-prompt-keywords`

This record describes direct protocol maintenance. It makes no initiative
acceptance, reopening, product-delivery, release, or deployment claim.

## Work and effort inventory

The protocol index records closed `INIT-DSN-001` as `Superseded`. Its claim
and records remain untouched. The example index records `INIT-IMP-001`
through `INIT-IMP-006` as `Proposed`: documentation, platform, API/SQLite,
SDK, CLI, and web-bundle work remain open effort. Their source mappings,
questions, acceptance and intended product boundaries were considered for
impact. This capability does not authorize their delivery or resolve their
questions; they retain their governing revision and future adoption boundary.
No directly evidenced incompatible work with this maintenance change was
identified. This is an impact review, not a comprehensive semantic audit of
all future example products. Existing work-conflict registers are preserved.

## Baseline observations

Before protected edits, both source-integrity checks returned zero errors.
The original protocol regression suite passed all 77 tests. Initial full
validation encountered the sandbox account's Git ownership check; supplying
command-scoped `safe.directory` with normalized forward slashes resolved
that environment limitation. The untouched example then validated with zero
errors and its existing `TADP033` warning. The protocol check while parallel
edits were in progress reported only then-missing new references and expected
protected drift; final results below supersede that intermediate snapshot.

## Final verification

All Python checks used the configured PyCharm Python 3.11.11 virtual
environment. The baseline was captured before mutation; protocol work was
reviewed and verified before example synchronization.

| Check | Protocol | Installed example |
|---|---|---|
| Full final regression suite (`-m unittest discover -s TREE/tests -q`) | 112 passed | 112 passed |
| Focused keyword suite | 35 passed | Included identical 35 cases in full run |
| Full validator with `--base-ref fb1e241ca89303abf6376bf53a897d54ab42c617` | 0 errors, 1 existing warning | 0 errors, 1 existing warning |
| Protected-source check after authorized refresh | 0 errors | 0 errors |
| Mirrored path inventory and parity | 51 paths reviewed | 51 corresponding paths reviewed |
| Existing initiative, product, question, profile, and conflict-register preservation | Unchanged | Unchanged |
| Git whitespace check | Passed | Passed |
| Shared CLI smoke check | Two correct source-position blocks; preview affects only following text | Identical shared implementation |

The retained `TADP033` warnings are the protocol's `Deferred` pre-effective
v1.0 bootstrap and the example's `Unmigrated` original v0.0 realization.
They retain their original evidence, owners, and re-entry conditions. Initial
ownership-check errors were environment issues resolved by command-scoped Git
trust; no repository invariant or validation rule was weakened.

Before each lock refresh, validation found exactly 32 changed protected
files (`TADP024`), two new protected files (`TADP025`), and the existing
warning, with no other errors. The two affected locks per tree were refreshed
with authority `decisions/KWD-DR-001-positional-keywords.md`. Their prior
revisions remain in the captured Git baseline. Template locks match exactly;
the LLM locks retain different digests only for the unchanged example-specific
`03_Codex_Invariant_Conflict_Register.md`. Their authority and all other
content digests agree.

Of 51 mirrored paths, 49 are byte-identical. `AGENTS.md` retains the example's
pre-existing embedded-project Git-root exception; removing just that section
leaves the same shared text. The LLM lock differs only as described above.
No example-specific migration, question answer, acceptance, execution,
completion, or release record was created or changed.

## Contract coverage and independent review

The 35 new regression cases cover prompt acceptance cases 1-25 through the
shared registry consumer and objective checks, alongside the 77 retained
validator/protection cases. Coverage includes defaults and separate prompt
scope; same-line, repeated, alternating and adjacent directives; all ten
forms and extensions; inert quoted, code, supporting and explanatory ranges;
wrong case, malformed tokens, paths and unknowns; exact rule/revision/block/
target/active-duration authority; inference confirmation; preserved lock
failures; preview writes and draft exceptions; local external-access limits;
independent actual-output review; immutable settings across concurrent
branches; real asynchronous serial and parallel scheduling, mixed nesting,
joins, sibling blockers, and reported capacity limits.

Actual asyncio events verify concurrency and joins. A regression verifies that
earlier numbered preparation completes before a later capacity-blocked item.
The registry extension case adds a precise definition to a temporary canonical
registry without changing an agent or validator name allowlist. Objective
registry/link checks preserve pre-adoption fixtures and ordinary lifecycle
validation. Git preservation review covers the historical/project-specific
acceptance cases that must not be satisfied by fabricating records.

The canonical author independently reviewed the changed workflow consumers
and mirror parity. The consumer author independently reviewed the shared
helper and tests. Review findings about smart-quoted and indented examples,
immutable block settings, nested capacity, missing reviewer identity, and
whitespace-only exception authority were reconciled with regression coverage.
The mirror review's sole whitespace finding was corrected in both READMEs;
the final independent audit reported no remaining findings.

Machine checks cannot authenticate a human, classify every explanatory phrase,
establish semantic authority, intercept arbitrary tools, or prove product
correctness. The helper requires caller-designated operative/action ranges,
actual authority and tool permissions. Agents must enforce preview/local and
review requirements in their real actions. No live gate waiver was exercised
by this maintenance prompt; the exact maintenance authority, rather than an
inert keyword example, authorized protected-source changes.

## Git recording

**Guarded delivery and effective revision commit:** `1fecb0dbca4133bfa65008e95fc7e842b7fd034b`

The combined repository hook ran both installed validators and both staged
protected-source guards successfully for that commit. Each validator reported
zero errors and its single retained warning. Only that commit used the exact
protected-update authority above; the override variables were removed after
the operation. The worktree was clean after delivery. This follow-up adds
the observed immutable commit ID and hook result, as required by the developer
workflow. No push, merge, release, deployment, history rewrite, or branch
deletion occurred.

## Exact path inventory

The following table maps each changed protocol path to its downstream mirror.
Repository-only support files intentionally remain unmirrored: `AGENTS.md`,
`README.md`, and `prompts/AGENTS.md`. They describe this enclosing reference
repository's entry points and maintenance boundary; copying them as project
instructions would broaden that boundary.

| Protocol path | Example mirror |
|---|---|
| `protocol/AGENTS.md` | `example/AGENTS.md` |
| `protocol/decisions/KWD-DR-001-positional-keywords.md` | `example/decisions/KWD-DR-001-positional-keywords.md` |
| `protocol/decisions/KWD-VER-001-positional-keywords.md` | `example/decisions/KWD-VER-001-positional-keywords.md` |
| `protocol/docs/development/developing-tadp.md` | `example/docs/development/developing-tadp.md` |
| `protocol/docs/development/getting-started.md` | `example/docs/development/getting-started.md` |
| `protocol/docs/development/validation-and-quality.md` | `example/docs/development/validation-and-quality.md` |
| `protocol/docs/guides/prompt-keywords-migration.md` | `example/docs/guides/prompt-keywords-migration.md` |
| `protocol/docs/README.md` | `example/docs/README.md` |
| `protocol/evidence/authoritative/LLM/.tadp-lock.json` | `example/evidence/authoritative/LLM/.tadp-lock.json` |
| `protocol/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md` | `example/evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md` |
| `protocol/evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md` | `example/evidence/authoritative/LLM/01_Codex_Evidence_Authority_Specification.md` |
| `protocol/evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md` | `example/evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md` |
| `protocol/evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md` | `example/evidence/authoritative/LLM/04_Codex_Initiative_Lifecycle_Specification.md` |
| `protocol/evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md` | `example/evidence/authoritative/LLM/07_Codex_Human_Decision_Receipt_Specification.md` |
| `protocol/evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md` | `example/evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md` |
| `protocol/evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md` | `example/evidence/authoritative/LLM/10_Codex_Initiative_Coherence_Specification.md` |
| `protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md` | `example/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md` |
| `protocol/prompts/AGENTS.md` | `example/prompts/AGENTS.md` |
| `protocol/prompts/README.md` | `example/prompts/README.md` |
| `protocol/README.md` | `example/README.md` |
| `protocol/template/.tadp-lock.json` | `example/template/.tadp-lock.json` |
| `protocol/template/initiatives/completion-evidence.md` | `example/template/initiatives/completion-evidence.md` |
| `protocol/template/initiatives/decision-receipts/decision-receipt.template.md` | `example/template/initiatives/decision-receipts/decision-receipt.template.md` |
| `protocol/template/initiatives/decision-receipts/gate-exception.template.md` | `example/template/initiatives/decision-receipts/gate-exception.template.md` |
| `protocol/template/initiatives/decision-receipts/README.md` | `example/template/initiatives/decision-receipts/README.md` |
| `protocol/template/initiatives/delivery-record.md` | `example/template/initiatives/delivery-record.md` |
| `protocol/template/initiatives/execution-record.md` | `example/template/initiatives/execution-record.md` |
| `protocol/template/initiatives/implementation-readiness.md` | `example/template/initiatives/implementation-readiness.md` |
| `protocol/template/project/AGENTS.md` | `example/template/project/AGENTS.md` |
| `protocol/template/project/prompts/AGENTS.md` | `example/template/project/prompts/AGENTS.md` |
| `protocol/template/project/prompts/README.md` | `example/template/project/prompts/README.md` |
| `protocol/template/prompts/00_initiative_preparation.md` | `example/template/prompts/00_initiative_preparation.md` |
| `protocol/template/prompts/01_proposal_creation.md` | `example/template/prompts/01_proposal_creation.md` |
| `protocol/template/prompts/02_proposal_alignment.md` | `example/template/prompts/02_proposal_alignment.md` |
| `protocol/template/prompts/03_initiative_creation.md` | `example/template/prompts/03_initiative_creation.md` |
| `protocol/template/prompts/04_initiative_alignment.md` | `example/template/prompts/04_initiative_alignment.md` |
| `protocol/template/prompts/05_initiative_assumption_review.md` | `example/template/prompts/05_initiative_assumption_review.md` |
| `protocol/template/prompts/06_initiative_open_question_review.md` | `example/template/prompts/06_initiative_open_question_review.md` |
| `protocol/template/prompts/07_initiative_acceptance.md` | `example/template/prompts/07_initiative_acceptance.md` |
| `protocol/template/prompts/08_initiative_sdk_api_alignment.md` | `example/template/prompts/08_initiative_sdk_api_alignment.md` |
| `protocol/template/prompts/09_initiative_implementation_readiness_review.md` | `example/template/prompts/09_initiative_implementation_readiness_review.md` |
| `protocol/template/prompts/10_initiative_execution.md` | `../../prompts/example/template/prompts/10_initiative_execution.md` |
| `protocol/template/prompts/11_design_delivery.md` | `../../prompts/example/template/prompts/11_design_delivery.md` |
| `protocol/template/prompts/12_planning_delivery.md` | `../../prompts/example/template/prompts/12_planning_delivery.md` |
| `protocol/template/prompts/13_initiative_finalization.md` | `../../prompts/example/template/prompts/13_initiative_finalization.md` |
| `protocol/template/prompts/README.md` | `../../prompts/example/template/prompts/README.md` |
| `protocol/template/prompts/WORKFLOW-CONTRACT.md` | `../../prompts/example/template/prompts/WORKFLOW-CONTRACT.md` |
| `protocol/tests/test_tadp_keywords.py` | `../../prompts/example/tests/test_tadp_keywords.py` |
| `protocol/tools/README.md` | `../../prompts/example/tools/README.md` |
| `protocol/tools/tadp_keywords.py` | `../../prompts/example/tools/tadp_keywords.py` |
| `protocol/tools/tadp_validate.py` | `../../prompts/example/tools/tadp_validate.py` |
