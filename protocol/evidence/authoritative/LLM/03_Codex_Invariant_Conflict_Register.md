# Codex invariant conflict register

## Purpose and authority

This register is the durable authoritative record of contradictions Codex
discovers between an invariant and a proposal, realization, initiative,
product, implementation, test, status claim, or other source.

An entry establishes that a conflict is known and blocks the affected claim.
It does not make the conflicting claim authoritative, revise the invariant,
approve an exception, or select a resolution.

Codex is explicitly authorized by the
[evidence authority specification](01_Codex_Evidence_Authority_Specification.md)
to append a factual entry when direct evidence demonstrates a contradiction.
Codex must not rewrite or remove existing entries. Resolution requires the
authority stated by the governing invariant or an explicit human instruction.

## Active conflicts

### INV-CONFLICT-001 — Realization template standing and scope

- **Detected:** 2026-11-13, Codex template coverage audit.
- **Status:** Open.
- **Governing invariant:** Specification 09, Realization provenance and fit
  assessment: suites and notes remain permanently non-authoritative and a
  catalog may contain several narrow outcomes.
- **Conflicting source:** `template/initiatives/proposal/README.md`, Realization
  handling, permits an owning authority to classify a realization otherwise and
  instructs a stop if suite notes do not share one narrow boundary.
- **Impact and disposition:** Do not rely on those clauses to promote standing
  or reject an otherwise valid many-outcome catalog; specification 09 governs.
  Preserve the reusable source pending a specifically authorized correction.
- **Owner and required decision:** Protocol maintainer; explicitly authorize
  correction of those realization-handling clauses and affected consumers.
- **Affected records and evidence:** No live initiative is changed. The
  [maintenance audit](../../../docs/development/template-prerequisites-maintenance.md#audit-findings-outside-the-revision)
  records the inspected source, limitation, and independent work.

### INV-CONFLICT-002 — Unconditional review pushes

- **Detected:** 2026-11-13, Codex workflow prompt audit.
- **Status:** Open.
- **Governing invariant:** Specification 05, Worktree, commits and history
  safety, and Finalization and human-managed pull requests: remote pushes
  require separate explicit authority.
- **Conflicting sources:** `template/prompts/05_initiative_assumption_review.md`
  and `template/prompts/06_initiative_open_question_review.md`, unconditional
  instructions to push new review commits.
- **Impact and disposition:** No push is authorized by those clauses alone.
  Preserve source identity and continue independent local preparation work;
  do not perform a remote action without sufficient separate authority.
- **Owner and required decision:** Protocol maintainer; explicitly authorize
  correction of those remote-action clauses and affected consumers.
- **Affected records and evidence:** No live initiative is changed. See the
  [maintenance audit](../../../docs/development/template-prerequisites-maintenance.md#audit-findings-outside-the-revision).

<!--
When a conflict is discovered, replace the statement above with the first
entry and append later entries without renumbering or reusing IDs. Preserve
resolved entries under the resolution history.

### INV-CONFLICT-001 — {{short title}}

- **Detected:** {{yyyy-mm-dd}}
- **Status:** Open
- **Governing invariant:** {{precise file, section, and claim}}
- **Conflicting source or behavior:** {{precise file, symbol, test, or claim}}
- **Exact contradiction:** {{state both incompatible claims}}
- **Affected scope:** {{initiatives, products, releases, or decisions}}
- **Immediate disposition:** {{blocked work and independent work that may continue}}
- **Required authority:** {{human or invariant owner}}
- **Required resolution:** {{lower-standing correction or explicitly authorized invariant revision/exception}}
- **Linked initiative records:** {{source mapping, decision, and status links}}
- **Evidence:** {{verification or observation proving the conflict}}
-->

## Resolution history

No invariant conflicts have been resolved.

For each resolved entry, retain the original conflict text and add:

- resolution authority and date;
- selected resolution and rationale;
- invariant revision, exception, or lower-standing correction;
- affected initiative and product changes;
- compatibility, migration, and recovery disposition; and
- verification proving the conflict is no longer active for the stated scope.

## Register rules

- Use one stable ID per distinct contradiction.
- Cite exact claims; a directory-level reference is insufficient.
- Preserve both sources and their original standing.
- Do not mark an entry resolved because work stopped, a test passed, or a lower
  record was edited unless the actual contradiction was removed or an explicit
  invariant exception was accepted.
- Keep the affected initiative and portfolio status synchronized with this
  register.

