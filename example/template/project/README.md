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
branch, diff, and history evidence. Codex consumes `../../AGENTS.md` and the
Codex-specific workflow prompts. Another coding agent or automation system may
be usable only after its instruction loading, interaction model, editing,
Git safety, and verification behavior have been assessed and the project has
made any required adaptations.

## Start a project from this template

Follow this order when creating a new project. It creates a usable traceability
chain before there is enough material for the directories to become confusing.

1. Create or select the project root and initialize Git there. Confirm that the
   root has its own `.git` entry; a parent repository is not a substitute.
2. Copy the `project/` directory to the location that will hold the project's
   protocol records. Keep the README and `*.template.md` files until the team
   has adopted equivalent local guidance.
3. Copy the TADp distribution's authoritative `../../evidence/authoritative/LLM`
   suite into the same path in the new project. Keep the copied root
   `../../AGENTS.md`; it directs Codex to that suite.
4. Copy the distribution's canonical `../initiatives` and
   `../prompts` directories into a stable target template root, or
   record a pinned external template root in the project profile.
5. Copy [project-profile.template.md](project-profile.template.md) to
   `project-profile.md`. Replace every `{{double_brace_token}}`, remove the
   instructional HTML comment, and record the project owner, boundary, and
   review cadence.
6. Establish the binding sources in
   [evidence/authoritative/](evidence/authoritative/README.md) before accepting
   work that depends on them. Record contextual sources separately in
   [evidence/non-authoritative/](evidence/non-authoritative/README.md).
7. Create an [evidence register](evidence/evidence-register.template.md) once
   there is more than a small number of sources. Assign stable evidence IDs and
   cite a section or claim, not merely a directory.
8. Register each proposed effort in
   [initiatives/](initiatives/README.md), then create its type-specific record.
   An initiative cannot use a product change to silently revise its governing
   specification or evidence.
   Copy both [the initiative index](initiatives/initiative-index.template.md)
   and [the portfolio status record](initiatives/status.template.md) before
   accepting the first initiative. The index answers what exists; the status
   record answers what is active, blocked, or gated next.
9. Add a product record when an output has a declared destination, even if the
   output itself lives outside `../../products`. Link its governing initiative,
   specification, binding evidence, and verification.
10. At each review, reconcile changed evidence, initiative status, product
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
  location, owner, and high-level relationship.
- `status.md` is the current portfolio view of lifecycle standing, next gate,
  blockers, and the evidence that supports a status claim.
- Each initiative's own record remains authoritative for its scope, decisions,
  assumptions, and detailed state.

Do not create umbrella or multi-purpose initiatives for a release, version,
program, product line, or other collection of work. Create separately scoped
initiatives for independent outcomes. Use a subinitiative only when a genuine
parent specification owns the shared boundary and the child owns one smaller
dependent outcome. Keep root tracking, parent records, subinitiative records,
and status evidence coherent without merging their acceptance claims.

## How template files work

Every `*.template.md` file is a copy-and-specialize starting point. Do not fill
in the template in place if it is meant to remain reusable.

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

Treat artifacts in `../../evidence/authoritative` as binding until their named
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

- [ ] `project-profile.md` names the project boundary and owners.
- [ ] Binding evidence has a named owner, source, status, and precise claims.
- [ ] Contextual evidence and realization notes retain their original context.
- [ ] The initiative index lists every active effort and its next review gate.
- [ ] Each delivered product links to a governing initiative, specification or
      decision, applicable evidence, and verification.
- [ ] Open conflicts, exceptions, and missing evidence have named owners.
- [ ] Review dates are scheduled or tied to a release, decision, or source
      change event.

