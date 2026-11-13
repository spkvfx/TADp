# Project protocol structure

This directory is a reusable starting structure for a Traceable Architecture
Design Protocol (TADp) project. Its purpose is to keep four different kinds of
record separate and traceable:

1. **Evidence** says what is known and how strongly it governs work.
2. **Initiatives** say what work is proposed, accepted, or completed.
3. **Products** say what was actually delivered and where it lives.
4. This **project profile** says how the project uses the structure as a whole.

The separation is intentional. A proposal does not become a binding rule just
because it is stored near a rule, and delivered code does not retroactively
change the evidence or specification it was expected to follow.

## Requirements

This project structure requires Git and Codex. Git supplies repository,
branch, diff, and history evidence. Codex consumes the project-root
`../../../../AGENTS.md` and the Codex-specific workflow prompts. Another coding agent or
automation system may be usable only after its instruction loading,
interaction model, editing,
Git safety, and verification behavior have been assessed and the project has
made any required adaptations.

## Start a project from this template

Follow this order when creating a new project. It creates a usable traceability
chain before there is enough material for the directories to become confusing.

1. Create or select the project root and initialize Git there. Confirm that the
   root has its own `.git` entry; a parent repository is not a substitute.
2. Copy the distribution's complete `template/` tree to `template/` in the
   target repository. Preserve `template/AGENTS.md` and
   `template/.tadp-lock.json`; do not specialize any file in that source tree.
3. Copy the contents of `template/project/`, including `.gitattributes`,
   `../../../../.githooks`, and the canonical `../../../AGENTS.md` and
   `prompts/README.md`, to the target repository root without overwriting
   established files blindly. The root copies are the working project
   scaffold; `template/project/` remains protected reusable source. Reconcile
   pre-existing prompt instructions without weakening either instruction set.
4. Copy the distribution's authoritative `evidence/authoritative/LLM/` suite,
   including its `../../../../AGENTS.md` and `.tadp-lock.json`, to the same path in the new
   project. Keep the copied root `../../../../AGENTS.md`; it directs Codex to that suite.
   Preserve distribution authority receipts linked by the copied suite under
   `decisions/`, with their historical source identity. Those receipts do not
   decide the adopting project's assumptions or authorize its delivery work.
5. Copy the distribution's `docs/`, `tools/`, and `tests/` trees when using the
   complete reference workflow. Run `python tools/tadp_protect.py check .`,
   then enable the tracked guard with
   `git config core.hooksPath .githooks`.
6. Copy [project-profile.template.md](project-profile.template.md) to
   `project-profile.md`. Replace every `{{double_brace_token}}`, remove the
   instructional HTML comment, and record the project owner, boundary, review
   cadence, version-scope revision effective commit, branch convention, and
   scope-adoption migration-ledger link; preserve earlier correlation history. Capture the current Git commit as the coherence
   revision baseline before adopting the coherence controls.
7. Establish the binding sources in
   [evidence/authoritative/](evidence/authoritative/README.md) before accepting
   work that depends on them. Record contextual sources separately in
   [evidence/non-authoritative/](evidence/non-authoritative/README.md).
8. Create an [evidence register](evidence/evidence-register.template.md) once
   there is more than a small number of sources. Assign stable evidence IDs and
   cite a section or claim, not merely a directory.
9. Register each proposed effort in
   [initiatives/](initiatives/README.md), then create its type-specific record.
   An initiative cannot use a product change to silently revise its governing
   specification or evidence.
   Copy both [the initiative index](initiatives/initiative-index.template.md)
   and [the portfolio status record](initiatives/status.template.md) before
   accepting the first initiative. Copy the
   [version-correlation migration ledger](initiatives/version-correlation-migration-ledger.template.md)
   when adopting the correlation revision. The index owns canonical initiative membership/provenance; the status record answers what is active, blocked, or gated next.
   Copy [the work-conflict register](initiatives/work-conflicts.template.md) to
   `initiatives/work-conflicts.md`; preserve both claims and effort when work
   conflicts, including proposed open initiative work.
10. Add a product record when an output has a declared destination, even if the
   output itself lives outside `products`. Link its governing initiative,
   specification, binding evidence, and verification.
11. At each review, reconcile changed evidence, initiative status, product
   verification, unresolved conflicts, and ownership in the records that they
   affect.

## Directory map and order of authority

| Directory | Put this there | Do not use it for | Read first when |
|---|---|---|---|
| [evidence/](evidence/README.md) | Source artifacts and their classifications | Unattributed design decisions | Determining what a proposal or product must respect |
| [evidence/authoritative/](evidence/authoritative/README.md) | Binding architecture, rules, and other accepted constraints | Exploratory notes or unaccepted alternatives | A claim must govern an initiative or product |
| [evidence/non-authoritative/](evidence/non-authoritative/README.md) | Research, observations, examples, and realization notes | A binding requirement without explicit acceptance | Understanding context or discovering a proposal |
| [initiatives/](initiatives/README.md) | Records of scoped work and its accepted outcome | Durable repository-wide evidence unless explicitly accepted there | Deciding what work is authorized and who owns it |
| [products/](products/README.md) | Output indexes and product records | The source of a new product requirement | Locating a delivered artifact and its verification |
| [prompts/](prompts/README.md) | Non-authoritative instructions confined to the current project scaffold | Generic TADp maintenance or the protected numbered workflow | Invoking stored work instructions about this project |

Use the standard terms and directory names **authoritative** and
**non-authoritative** for evidence classification. Do not introduce alternate
spellings or legacy aliases; one canonical path keeps links, automation, and
source mappings unambiguous.

## Project ownership convention

Record the project's human ownership model in `project-profile.md`. A solo
project may resolve human owner, reviewer, and approver roles to one named
project owner, but that convention removes only duplicate personnel gates. It
never removes technical ownership, source authority, external-party,
placement, contract, security, environment, verification, or release gates.

Only an explicit instruction from the recorded human authority may accept an
initiative, resolve an open initiative decision, change an assumption's
disposition, authorize product execution, or authorize publication. Templates
must link to the local profile instead of assuming a particular repository
path or a solo-project arrangement.

## Portfolio and status tracking

The initiative index and portfolio status record are coordination artifacts,
not sources of substantive authority:

- `initiative-index.md` is the stable registry of initiative identity, type,
  location, relationships, exact scope/source provenance, revision assignment,
  execution mode/branch, captured base and integration evidence.
- `status.md` is the current portfolio view of lifecycle standing, next gate,
  blockers, and the evidence that supports a status claim.
- `work-conflicts.md` preserves incompatible work claims, their effort,
  impact, owner, blocking scope, and governed disposition. It does not accept
  a claim or override the authoritative invariant conflict register.
- Each initiative's own record remains authoritative for its scope, decisions,
  assumptions, and detailed state.

Do not create umbrella or multi-purpose initiatives for a release, version,
program, product line, or other collection of work. Create separately scoped
initiatives for independent outcomes. Use a subinitiative only when a genuine
parent specification owns the shared boundary and the child owns one smaller
dependent outcome. Keep root tracking, parent records, subinitiative records,
and status evidence coherent without merging their acceptance claims.

## How template files work

The complete `template/` tree is protected reusable source, including numbered
prompts, scaffold files, and every `*.template.md` file. The authoritative
Codex suite at `evidence/authoritative/LLM/` is protected separately. Ordinary
work must not edit, fill, rename, move, or delete either tree.

The protection is layered:

- root and directory-scoped `../../../../AGENTS.md` files establish the Codex edit
  boundary;
- each protected root carries a `.tadp-lock.json` with SHA-256 digests for
  every other file in that root;
- the validator rejects missing locks, unrecorded files, missing files, and
  content drift; and
- the tracked pre-commit hook rejects staged protected-source changes unless a
  deliberate update uses an authority reference matching the refreshed lock.

To use a template, copy it to its declared destination outside `template/` and
specialize only that copy. For example, copy `rule.template.md` to
`RULE-003-data-retention.md`, then edit the new record. An intentional reusable
source or invariant revision requires an explicit human instruction naming the
change, compatibility and migration review, affected-consumer updates,
verification, and a governed lock refresh. Do not refresh a lock simply to
make validation pass.

The canonical project-local prompt instructions are copied from
`template/project/prompts/` to root `../../..`. The reusable copies are
protected; the installed root directory and any additional local prompt files
are working project material. Root `../../..` must not contain or replace the
numbered workflow library at `template/prompts/`.

1. Copy it to a descriptive, stable filename. For example,
   `rule.template.md` becomes `RULE-003-data-retention.md`.
2. Replace each `{{token}}` with a precise value. A token is not a suggestion
   to omit the field; write `Not applicable — {{reason}}` when a field does not
   apply.
3. Keep tables and required headings unless a documented local convention
   replaces them. They make review and cross-record comparisons predictable.
4. Remove the leading HTML instruction comment only after replacement is
   complete. Comments exist to guide authors without appearing in rendered
   documentation.
5. Link to the most precise supporting artifact available: an evidence ID and
   heading, an initiative ID and record, a product path and test, or a rule ID.
6. Give the record an owner, status, and review date. An otherwise good record
   cannot be maintained if its authority and stewardship are unknown.

## Traceability workflow

Use this chain for any material change:

```text
source or observation
        │
        ▼
evidence record and classification
        │
        ▼
initiative decision / specification / plan
        │
        ▼
product destination and verification evidence
        │
        ▼
review, release, and durable status update
```

The same item may appear in several records, but each record has a different
job. Evidence stores the source claim. An initiative states how the claim is
interpreted for a bounded effort. A product record identifies implementation
and proof. Link between them rather than copying a requirement into several
places without a source of truth.

## Conflict and change discipline

Treat artifacts in `evidence/authoritative` as binding until their named
authority revises them. Preserve the original source and record the replacement
or correction relationship; never overwrite history merely to make a later
initiative appear aligned. Contextual evidence may explain ambiguity or support
a proposal, but it cannot override binding evidence by itself.

When records disagree, create a visible conflict entry in the affected
initiative, evidence register, or rule/decision record. State the conflicting
claims, affected products, owner, required decision, and resolution date. Do
not change an earlier record without authority and do not release a product on
the assumption that the conflict has been resolved.

## Initial adoption checklist

- [ ] The complete template and LLM invariant trees retain their scoped
      `../../../../AGENTS.md` instructions and valid `.tadp-lock.json` files.
- [ ] `../../../../.githooks/pre-commit` is tracked and `core.hooksPath` points to
      `.githooks`.
- [ ] Root `../../../AGENTS.md` and `prompts/README.md` preserve the
      project-local scaffold boundary, and any additional prompt files remain
      non-authoritative working material.
- [ ] `project-profile.md` names the project boundary and owners.
- [ ] Binding evidence has a named owner, source, status, and precise claims.
- [ ] Contextual evidence and realization notes retain their original context.
- [ ] The initiative index lists every active effort and its next review gate.
- [ ] The project profile captures the coherence revision baseline, and
      `initiatives/work-conflicts.md` exists with an owner and review date.
- [ ] Each delivered product links to a governing initiative, specification or
      decision, applicable evidence, and verification.
- [ ] Open conflicts, exceptions, and missing evidence have named owners.
- [ ] Review dates are scheduled or tied to a release, decision, or source
      change event.


## Version-scope adoption

For newly adopted work, group initiatives physically at
initiatives/<scope>/<type>/<id-and-slug>/. Instantiate
[the scope registry](initiatives/version-scopes.template.md),
[scope navigation](initiatives/scope-README.template.md) and
[scope adoption ledger](initiatives/version-scope-migration-ledger.template.md).
Version scopes have exact major/minor/patch identity and one integration branch;
multiple narrow initiatives and source notes may share a scope. An actual human
intake request delegates fit-based routing and necessary reopening under adopted
specification 09, with each LLM-authored event recorded before changes. Existing
complete targets reuse their records and changed claims need renewed acceptance.

Branch topology is project integration base -> major -> matching minor ->
matching patch; a dedicated member branches from its scope, or the scope branch
hosts it directly. Local integration runs child into recorded immediate parent
after required closure gates and bounded human close/finalize authority. Shared
whole-tip integration blocks on unfinished/unaccepted inclusions. Scope closure
is separate from member lifecycle. Pull requests are human-managed, and remote
operations need separate authority. Preserve legacy revision/path/branch/source
identity until explicit evidence-backed migration; installation is not migration.