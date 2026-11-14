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


## Reusable-source location note

On 2026-11-13 the user explicitly requested consolidating initiative sources
under template/project/initiatives and making a clean project baseline.
INV-CONFLICT-001 retains its original detected source identity above. Its
current reusable source is
[the relocated proposal inventory](../../../template/project/initiatives/proposal/README.template.md).
The move changes no conflicting clause, disposition or required resolution
authority. The clean project register starts empty and does not inherit
TADp's active conflict entries.

## Subsequent baseline compatibility finding

### INV-CONFLICT-003 — Type navigation allocation and record copying

- **Detected:** 2026-11-13, Codex clean-project-baseline compatibility review.
- **Status:** Resolved for the revised reusable type navigation; no live
  initiative was changed. The earlier no-resolution statement above belongs
  to the preserved preceding register snapshot.
- **Governing claims:** Specification 09 owns scoped allocation at
  `initiatives/<scope>/<type>/<id-and-slug>/`; specifications 02 and 08 own
  stage-specific canonical selection and conditional record creation.
- **Conflicting sources:** The design, implementation and planning READMEs at
  `template/project/initiatives/<type>/README.md` in source revision `da87ad8`
  instructed creation directly beneath the unscoped type directory and copying
  the complete suite during initial preparation.
- **Authority and correction:** The user's 2026-11-13 explicit instruction to
  consolidate the project initiative sources and provide a completely clean
  baseline authorizes this affected navigation correction. The type READMEs
  now route allocation through Stage 0, name the scoped destination, and select
  only the current activity's sources through the coverage map. The existing
  protocol rules, stage ownership and live instance names are unchanged.
- **Verification:** Protocol regression run: 222 tests, OK, two environment
  skips. Review confirmed each corrected type README retains its output
  boundary and no late-stage record is created by baseline copying.
- **Scope and preservation:** Source history and INV-CONFLICT-001/002 remain
  intact. The clean copied project conflict register starts empty; this TADp
  maintenance finding is not copied into a new project's history.
- **Owner:** User; finding captured and correction authored by Codex.

### INV-CONFLICT-004 — Project root and enclosing Git worktree

- **Detected:** 2026-11-13, installation-root maintenance audit, source baseline
  `fc0c8e3ea01471d3a35f06a29d96f837070afd70`.
- **Prior governing claim:** Specification 05, Requirement: "Every TADp project
  must be the root of a Git repository."
- **Conflicting source and behavior:** `tools/README.md`, Project root and
  installation directory, describes the scaffold installation directory as
  the project root while acknowledging the own-Git-root restriction;
  `tools/tadp_sync.py:main` rejects any cwd other than Git top level.
  `tools/tadp_validate.py:validate_required_paths` requires the enclosing
  Git root's `AGENTS.md` rather than the checked project's entry point.
  Together these prevent an installation destination beneath the worktree
  from satisfying the requested single root contract. The prior restriction
  was authoritative until this specifically authorized revision; earlier
  enclosing-worktree exceptions and historical claims retain their identity.
- **Scope and immediate disposition:** Protocol sources and isolated fixtures
  only; no live initiative or project adoption is changed. Preserve baseline
  behavior and authority in Git while reconciling only the authorized revision.
- **Resolution authority:** User's 2026-11-13 explicit execution of
  `prompts/project-root-installation-directory-protocol-change.md`, captured
  in ROOT-DR-001, [maintenance record](../../../docs/development/project-root-installation-maintenance.md).
- **Selected resolution and rationale:** Specifically revise specification 05
  to require containment in a valid Git worktree and define project root as
  scaffold installation destination. Reconcile tools, instructions, reusable
  sources and guidance. Git remains required and enclosing Git cannot expand
  the authorized file boundary.
- **Status and verification:** Resolution authorized; implementation and
  verification are recorded in ROOT-DR-001 before the coherent revision commit.
  Final disposition applies only at that effective event. This record does
  not close INV-CONFLICT-001/002 or migrate historical projects.
- **Compatibility and owner:** Protocol maintainer/User; explicit prospective
  adoption, no file moves or changed initiative acceptance/lifecycle facts.
