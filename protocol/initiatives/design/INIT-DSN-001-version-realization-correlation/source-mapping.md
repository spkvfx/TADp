# Version-realization-suite-initiative correlation evidence mapping

**Initiative:** INIT-DSN-001-version-realization-correlation

**Status:** Proposed

**Last updated:** 2026-11-10

**Decision prefix:** VRC

This map connects authoritative evidence and contextual sources to the
proposed specification, design destinations, and verification. It does not
replace the proposal, assumptions, decisions, architecture, or lifecycle
records.

## Evidence inventory

| Evidence ID | Source | Evidence label | Governs | Conflict rule |
|---|---|---|---|---|
| EVD-01 | [Current invariant suite index](../../../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md) and specifications 01-08 | Authoritative evidence | Evidence precedence, governance, lifecycle, Git, scope, receipts, workflow, and revision process | Binding until the authorized successor becomes effective |
| EVD-02 | [Source realization](../../../evidence/non-authoritative/realizations/v1.0/RZN-TADP-001-VERSION-CORRELATION.md) and [suite index](../../../evidence/non-authoritative/realizations/v1.0/00-RZN-TADP-001-VERSION-CORRELATION-suite-index.md) | Non-authoritative evidence | Requested outcome, bootstrap identity, source limits, and uncertainty | Cannot override EVD-01 or prove acceptance |
| EVD-03 | User instructions and realization-placement clarification dated 2026-11-10, preserved in the source inventory and proposal | Explicit human authority for the exact revision; not acceptance | Canonical version rule, bijection, permanent non-authoritative realization standing, sole `evidence/non-authoritative/realizations/**` placement, protected scope, synchronization, migration/validation requirements, and limits | Applies only to named invariant revision; separate receipts required for decisions and acceptance |
| EVD-04 | [Observed example v4.0 suite](../../../../example/evidence/non-authoritative/realizations/v4.0/00-RZN-001-P4-WEB-suite-index.md) and sibling note | Non-authoritative evidence | Mandatory migration/validation case and observed D6 boundary | Preserve standing and source identity; cannot supply missing v4/v4.1 meaning |
| EVD-05 | Git commits 80c0ee0 and d05f334 plus current branch history | Observed repository evidence | Creation of v1.0-v4.0 suites, v0 relocation, captured base, and absence of tracked v3.1/v4.1 | Observation cannot resolve semantic mapping or lifecycle |
| EVD-06 | [Scope specification](../../../evidence/authoritative/LLM/06_Codex_Initiative_Scope_Specification.md) and [workflow specification](../../../evidence/authoritative/LLM/08_Codex_Initiative_Workflow_Specification.md) | Authoritative evidence | Mandatory design/implementation split and stage ownership | Product work must move to a separate initiative |
| EVD-07 | Current protected templates, prompts, tools, tests, and documentation at base d05f334 | Protected reusable sources and observed products | Consumer inventory and implementation handoff | Must conform to EVD-01/EVD-03; presence is not authority to revise |

## Concept and contract mapping

| Map ID | Concept or contract | Authoritative evidence | Assumption | Decision | Specification location | Product destination | Verification evidence | Status |
|---|---|---|---|---|---|---|---|---|
| MAP-001 | Canonical work-version grammar and numeric ordering | EVD-03 exact canonical rule; EVD-01 revision process | VRC-A04 | VRC-03 | [architecture.md](architecture.md#terms-and-identity) | Authoritative specification 09; no product in this initiative | Specification review plus future parser tests | Proposed |
| MAP-002 | Project-local bijection and reverse uniqueness | EVD-03 cardinality; EVD-01 governance/Git | VRC-A02, VRC-A04 | VRC-04 | [architecture.md](architecture.md#domain-model-and-authoritative-evidence) | Specification 09 and correlation templates | Graph review plus future duplicate/orphan tests | Proposed |
| MAP-003 | Canonical project row versus lifecycle authority | EVD-01 specifications 04/08; EVD-03 record ownership | VRC-A02 | VRC-04 | [architecture.md](architecture.md#boundaries-and-ownership) | Initiative-index, status, README, delivery/completion templates | Cross-record ownership review | Proposed |
| MAP-004 | Self-contained initiative and mandatory split tuple | EVD-01 specification 06; EVD-03 self-contained rule | VRC-A01, VRC-A06 | VRC-05, VRC-07 | [scope-assessment.md](scope-assessment.md#split-trigger-review) | Specification 09 and scope/workflow consumers | Scope matrix and future split fixture | Proposed |
| MAP-005 | Substantive successor versus unchanged-claim reopening | EVD-01 specifications 02/04/06; EVD-03 successor rule | VRC-A06 | VRC-05 | [architecture.md](architecture.md#mandatory-split-or-substantive-successor) | Specification 09, README/lifecycle prompts | Lifecycle/successor review and future tests | Proposed |
| MAP-006 | Stage 0 preflight and atomic preparation | EVD-01 specifications 05/08; EVD-03 workflow integration | VRC-A02, VRC-A04 | VRC-06 | [architecture.md](architecture.md#new-tuple-preparation) | Workflow spec, contract, Stage 0 prompt, suite/index/README templates | Prompt contract review and future fixture | Proposed |
| MAP-007 | Later-stage tuple continuity and recovery | EVD-01 specifications 05/08; EVD-03 recovery rules | VRC-A02, VRC-A05 | VRC-06 | [architecture.md](architecture.md#later-stage-continuity) | Stages 1-13 and delivery/completion templates | Stage consumer matrix | Proposed |
| MAP-008 | Evidence and lifecycle non-collapse | EVD-01 specifications 01/02/04/07/08; EVD-03 explicit preservation | VRC-A02 | VRC-04 | [architecture.md](architecture.md#boundaries-and-ownership) | Specification 09 and all identity copies | Authority/lifecycle wording audit | Proposed |
| MAP-009 | Protocol/example protected-source parity | EVD-03 synchronization clarification; EVD-01 protected revision process | VRC-A03, VRC-A05 | Not applicable — source-directed boundary | [README.md](README.md#scope) | Both LLM suites, templates, prompts, and locks | Counterpart parity report and protected checks | Proposed |
| MAP-010 | Legacy notation-only normalization and meaning preservation | EVD-03 migration rules; EVD-01 evidence preservation | VRC-A06 | VRC-01, VRC-02 | [architecture.md](architecture.md#legacy-migration) | Initiative-local migration ledger and future migration guide | Source/Git comparison and decision receipts | Proposed |
| MAP-011 | Mandatory v4 migration/validation case | EVD-03 exact test-case instruction; EVD-04/EVD-05 observed limits | VRC-A06 | VRC-01 | [open-questions.md](open-questions.md#vrc-01---v4-v41-source-identity-and-mapping) | Migration ledger and future validator fixture | Exact source inventory and human receipt | Blocked |
| MAP-012 | Separate executable validation consumer | EVD-01 type boundary; EVD-03 validation requirements | VRC-A01 | VRC-07 | [scope-assessment.md](scope-assessment.md#assessment-result) | Future implementation initiative | Accepted handoff and separate execution evidence | Proposed |
| MAP-013 | Protected lock authority and refresh order | EVD-01 suite protection and developer workflow; EVD-03 exact lock authority | VRC-A05 | Not applicable — source-directed boundary | [architecture.md](architecture.md#failure-and-recovery) | Four affected protected locks | Pre-refresh explained drift, refresh authority, post-refresh checks | Proposed |

| MAP-014 | Permanent realization standing and canonical placement | EVD-03 exact clarification; EVD-01 evidence-authority and governance requirements | VRC-A02, VRC-A03 | VRC-08 | [architecture.md](architecture.md#terms-and-identity) | LLM evidence/governance references, realization/proposal templates, prompts, protocol guides, and worked-example consumers | Exhaustive consumer-path audit, local-link validation, protected parity review, and future validator fixtures | Proposed |

## Mapping rules

- Cite precise sections and stable IDs wherever available.
- Authoritative evidence owns normative requirements; non-authoritative sources
  preserve context and ambiguity.
- Each concept has one canonical map row. Other records link here.
- Product destination is Not applicable for design delivery; future product
  destinations belong to the implementation consumer.
- Proposed rows become Mapped only after the accepted specification,
  destination, and verification agree.
- Missing or conflicting authoritative evidence blocks the affected claim.

## Coverage audit

| Area | Expected concepts or contracts | Mapped | Gaps | Gate |
|---|---|---|---|---|
| Product and scope | Design boundary, implementation split, legacy migration separation | MAP-004, MAP-012 | None | Pass for proposal alignment |
| Domain and identity | Grammar, ordering, tuple, reverse uniqueness, lineage | MAP-001, MAP-002, MAP-005 | Acceptance pending | Open |
| Interfaces and integration | Canonical row, reciprocal records, Stage 0, later-stage continuity, canonical realization path | MAP-003, MAP-006, MAP-007, MAP-014 | Protected consumer matrix pending delivery | Open |
| Data and lifecycle | Immutability, lifecycle ownership, reopening/successor, evidence standing | MAP-003, MAP-005, MAP-008, MAP-014 | Acceptance receipts pending | Open |
| Security and authority | Exact human authority, source standing, lock authority | MAP-008, MAP-009, MAP-013 | Decision and acceptance receipts pending | Open |
| Operations and recovery | Duplicate/orphan/drift handling, migration, protected refresh | MAP-007, MAP-010, MAP-011, MAP-013 | VRC-01 unresolved | Blocked |

## Unresolved mappings

| ID | Missing or conflicting evidence | Affected rows | Decision or owner | Required resolution |
|---|---|---|---|---|
| MAP-Q01 | User names a legacy v4 path and v4.1 relationship; captured tree/history exposes only v4.0 created directly at 80c0ee0 | MAP-010, MAP-011 | VRC-01; User | Exact human mapping/source decision before any meaning-changing disposition |
| MAP-Q02 | User requests v3/v3.1 inventory; captured tree/history exposes only v3.0 | MAP-010 | VRC-02; User | Preserve separately in ledger unless explicit evidence/decision maps them |
| MAP-Q03 | Validator/test/documentation product paths cannot be delivered by this design initiative | MAP-012 | Future implementation initiative | Allocate a new tuple after this design is accepted and its handoff is stable |
