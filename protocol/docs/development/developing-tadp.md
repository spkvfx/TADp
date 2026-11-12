# Developing TADp

## Change classification

Classify a proposed change before editing. The classification determines the
authority and reconciliation required.

| Change class | Examples | Required handling |
|---|---|---|
| Authoritative protocol change | Evidence precedence, lifecycle transition, Git rule, scope trigger, human-decision rule | Explicit human instruction, preserved prior state, affected-scope analysis, and coordinated consumer updates |
| Reusable workflow change | Prompt precondition, template field, standard record, project scaffold | Compatibility check against all authoritative specifications and updates to prompts, templates, docs, validator, and tests as applicable |
| Validator change | New structural rule, finding code, parsing behavior | Documented protocol basis and regression coverage |
| Explanatory documentation | Clarification, tutorial, example, developer guidance | Must remain compatible with authority and must not create a new rule implicitly |
| Focused guide | Migration or decomposition procedure | Preserve evidence standing and link to the governing specification |

Do not place an authoritative rule in a guide to avoid the invariant revision
process. Do not change an invariant merely because an existing template or
implementation is inconvenient.

## Before editing

1. Read `../../AGENTS.md` and the suite index.
2. Read every authoritative specification that governs the intended change.
3. Inspect Git branch and complete worktree state.
4. Search for every consumer of the term, path, status, field, or workflow
   being changed.
5. Decide whether existing initiatives, projects, or products require a
   migration note.
6. Confirm that the requested scope authorizes any authoritative change.

If authorization is missing, limit work to analysis or a proposal and ask for
the required human decision.

## Coordinated update surfaces

A material protocol change may affect:

- `../../evidence/authoritative/LLM` specifications and index;
- root and reusable `../../AGENTS.md` instructions;
- canonical initiative templates;
- project templates and profile fields;
- the shared workflow contract;
- one or more numbered prompts;
- the validator and regression tests;
- root and developer documentation;
- migration or decomposition guidance; and
- canonical version, realization-suite, initiative, and branch correlation
  records, including any pre-effective migration ledger; and
- existing initiative records that explicitly adopt the changed revision.

Not every change touches every surface. Review them all and document why an
apparently related consumer is unaffected.

## Template rules

- Maintain one canonical initiative suite for all initiative types.
- Preserve required sections; use an explicit not-applicable explanation
  instead of deleting a field.
- Keep later-stage records out of initial initiative creation.
- Use double-braced tokens in record templates and single-braced placeholders
  in executable prompt blocks according to existing conventions.
- Never add a project-specific name, path, decision ID, or authority assumption
  to a reusable template.
- Keep subinitiatives supported without reintroducing umbrella initiatives.

## Protected-source changes

`template/**` and `evidence/authoritative/LLM/**` are protected source trees.
Their scoped `AGENTS.md` files and SHA-256 locks apply even when the intended
change is otherwise authorized. Before editing either tree:

1. Confirm an explicit human instruction identifies the exact reusable
   template or invariant change. A request to use the source is not permission
   to revise it.
2. Capture the prior lock, Git revision, affected consumers, compatibility and
   migration effects, and required verification.
3. Make the coherent source and consumer changes without weakening unrelated
   rules or overwriting historical authority.
4. Run regression tests and full validation except for the expected stale-lock
   findings.
5. Refresh only the affected lock with `tadp_protect.py refresh`, using the
   human instruction or decision record as its `--authority` value.
6. Re-run the protected-source check, validator, and regression tests.
7. Commit through the staged guard using the same authority value. Do not leave
   the override environment variables set for later work.

The lock refresh is the final recording step, not a way to decide whether a
change was authorized. Existing adopters use the protected-source migration
guide; do not silently rewrite their baseline.

## Prompt rules

The canonical
[prompt keyword specification](../../evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md)
owns recognized names and interpretation for every TADp request. New names
require precise human revision authority, a complete **Adding a keyword**
entry, consumer reconciliation, verification, and governed lock refresh.
Keep machine consumers registry-driven; no competing allowlist or unprotected
override registry may redefine behavior. An inferred keyword or invariant
exception needs explicit confirmation before use. Distinguish numbered
workflow stages and reference inventories from operative action lists.

Every numbered prompt must:

- link and apply `WORKFLOW-CONTRACT.md`;
- include a clearly marked reference-only example;
- use “attached initiative” in example invocation language;
- use the `&#123;initiative&#125;` placeholder and other declared placeholders in
  the executable block;
- preserve stage-specific preconditions, edit boundaries, verification, and
  reporting;
- distinguish evidence from human decisions; and
- stop instead of silently expanding authority.

Centralize only genuinely shared rules. Do not shorten a prompt until the
result still defines the task with enough detail to behave consistently.

## Git workflow for TADp changes

Use a dedicated branch for material protocol work. Preserve existing user
changes, commit coherent updates, and include validator results in review
evidence. Do not combine unrelated protocol revisions merely because they touch
the same README or prompt directory.

When an authoritative revision is accepted, the commit and review description
should identify the prior rule, new rule, human authority, affected consumers,
migration consequence, and verification.

When a revision defines a Git commit as its effective point, keep the
authoritative rule, all affected reusable consumers, validator coverage,
distribution mirrors, and refreshed protected locks in that coherent commit.
Record the resulting immutable commit ID in a follow-up traceability commit; do
not guess or predeclare the self-referential identifier.

When the revision adds, removes, renumbers, or changes a workflow stage,
publish a migration guide for active initiatives. Preserve historical prompt
identity and require an explicit change record before an active initiative
mixes workflow revisions. Never rewrite a prior stage number as though the
initiative originally used the current workflow.

## Verification checklist

- [ ] Applicable authoritative specifications were read.
- [ ] The change classification and authority are explicit.
- [ ] All affected consumers were inspected.
- [ ] Repository-relative links resolve.
- [ ] Prompt examples and executable placeholders remain separated.
- [ ] No umbrella or multi-purpose initiative construct was introduced.
- [ ] Correlated work has exactly one canonical version, realization suite,
      initiative, and dedicated branch, or a complete legacy disposition.
- [ ] Git and Codex requirements remain explicit.
- [ ] Non-Codex compatibility is not claimed without an adapter review.
- [ ] Protected-source locks match the reviewed template and invariant suite.
- [ ] Any protected-source change cites its explicit authority and migration
      consequence.
- [ ] Validator regression tests pass.
- [ ] Full repository validation reports zero errors.
- [ ] Documentation indexes reflect added, renamed, or removed documents.

## Releasing a protocol revision

Before a formal TADp release, record a version or revision identifier, summarize
authoritative changes, identify migration requirements, preserve the earlier
baseline, and test the workflow on a representative narrow initiative. A
template edit is not complete merely because all Markdown renders correctly;
the workflow must remain executable and evidence-preserving.

