# TADp documentation

This directory contains developer documentation and operating guides for the
Traceable Architecture Design Protocol.

These documents explain how to use and maintain TADp. They are not a second
source of architectural authority. The binding protocol remains under
[`../evidence/authoritative`](../evidence/authoritative/README.md), beginning
with the
[Codex invariant suite](../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md).
If explanatory documentation and authoritative evidence differ, the
authoritative evidence governs and the documentation must be corrected.

## Developer documentation

Read these documents in order when first adopting or maintaining TADp:

1. [Getting started](development/getting-started.md) — prerequisites, project
   setup, adoption choices, and the first validation run.
2. [Architecture and authority](development/architecture-and-authority.md) —
   authority layers, traceability, invariant handling, and conflicts.
3. [Repository layout](development/repository-layout.md) — where every class of
   record belongs and what must not be mixed.
4. [Initiative workflow](development/initiative-workflow.md) — the complete
   initiative process, stage boundaries, human gates, and lifecycle evidence.
5. [Git and Codex requirements](development/git-and-codex-requirements.md) —
   mandatory platform assumptions and their operational consequences.
6. [Validation and quality](development/validation-and-quality.md) — validator
   checks, regression tests, CI usage, and known limits.
7. [Developing TADp](development/developing-tadp.md) — changing protocol
   specifications, templates, prompts, documentation, and validation.
8. [Adapting TADp to other tools](development/adapting-other-tools.md) — the
   required compatibility assessment and modification checklist.

## Operating guides

- [Protected-source integrity migration](guides/protected-source-integrity-migration.md)
  explains how an existing adoption establishes reviewed template and Codex
  invariant locks without treating unexplained local drift as authority.
- [Project-local prompts migration](guides/project-local-prompts-migration.md)
  explains how an existing scaffold adds root prompt instructions, reconciles
  earlier local rules, and preserves the boundary from the numbered workflow.
- [Legacy initiative decomposition](guides/legacy-initiative-decomposition.md)
  explains how to split a broad historical initiative without rewriting its
  evidence or losing ownership.
- [Workflow stage 0–13 migration](guides/workflow-stage-0-13-migration.md)
  explains how to move active initiatives to the explicit acceptance gate and
  type-specific delivery paths without rewriting their history.
- [Version-realization-initiative correlation migration](guides/version-realization-correlation-migration.md)
  explains effective-point adoption, non-inferred legacy dispositions, and
  separately governed tuple migration.
- [Initiative coherence migration](guides/initiative-coherence-migration.md)
  explains how to account for open effort, document work conflicts, review
  completion feedback, and preserve closed claims during adoption.

## Documentation maintenance

- Keep root-level orientation in `../../README.md`; put durable explanations here.
- Link to authoritative specifications instead of copying normative text when
  the exact rule matters.
- Use repository-relative links and run the validator after changing them.
- Update the root documentation index and this index when adding, renaming, or
  removing a developer document.
- Do not place binding invariants in ``; authoritative material belongs in
  `../evidence/authoritative`.

