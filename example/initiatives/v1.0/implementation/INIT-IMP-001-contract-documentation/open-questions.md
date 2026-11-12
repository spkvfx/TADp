# Contract documentation open questions and decisions

**Initiative:** Contract documentation  
**Status:** Open  
**Last updated:** 2026-11-11

Recommendations are proposed defaults only. No question below is answered or
accepted. An explicit human decision must be recorded and reconciled across
the complete initiative.

**Human ownership:** Under the [project ownership convention](../../../../project-profile.md),
the User fulfills the human owner, reviewer, and approver roles; technical
source, publication, and evidence responsibilities remain explicit.

## Status vocabulary

`Open, blocking` prevents the affected product work. `Open` requires a later
decision before its named phase. `Proposed; confirm` is not accepted.
`Accepted YYYY-MM-DD` requires a linked receipt. `Deferred` requires a re-entry
condition. Superseded entries remain as history.

## Decision register

| ID | Decision | Recommendation | Status | Blocks |
|---|---|---|---|---|
| `DOC-01` | Product repository or publishing destination | Prefer one repository-owned, versioned destination with link/structure checks | Open, blocking | Product placement and execution |
| `DOC-02` | Audience grouping and mandatory splits | Keep one set only if all areas share owner, lifecycle, and acceptance | Open, blocking | Scope acceptance |
| `DOC-03` | Authored versus generated boundary | Author normative explanations; generate only exact observed derivatives with drift checks | Open, blocking | Content architecture and tooling |
| `DOC-04` | Documentation version and release cadence | Use a documentation revision bound to exact source revisions and classify changes under `ADR-006` | Open | Compatibility and release identity |
| `DOC-05` | Accessibility and usability review | Combine automated structure checks with keyboard, zoom, navigation, and representative reader review | Open | Qualification gate |
| `DOC-06` | Source-currency, disclaimer, and product-review ownership | Assign named responsibilities under the Sole Project Owner convention | Open | Security/legal-source and release review |

## Earliest blocking decisions

1. `DOC-01` — no product path may be created without an owned destination.
2. `DOC-02` and `DOC-03` — scope and generated-output boundaries must be known
   before the initiative can be accepted as one claim.

## DOC-01 - Product destination

**Question:** Will the derivative set live in a repository documentation tree,
a separately versioned published site, or another explicitly owned placement?

**Context and evidence:** D1 permits documentation products but no current
record selects a path, tooling system, or release channel.

**Options:**

1. Repository-owned Markdown with local structure/link qualification.
2. A separately versioned documentation site whose source and build remain
   traceable to the repository.
3. Another named placement with equivalent ownership, rollback, and evidence.

**Recommendation:** Prefer repository-owned Markdown unless audience needs
justify additional publishing infrastructure.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Name exact destinations, product owner, build/publish path,
rollback, link roots, and review-evidence location.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## DOC-02 - Audience cohesion and split boundary

**Question:** Do implementer, consumer, operator, security, and evidence guides
share one product lifecycle and acceptance claim, or must one or more become
separate initiatives?

**Context and evidence:** `ADR-007` permits one D1 unit, but the protocol
requires a split if an audience area has its own owner, destination, lifecycle,
or independently acceptable claim.

**Options:**

1. One navigable set with one review and release claim.
2. One core set plus separately governed audience products.
3. Reduce this initiative to one narrower audience and allocate others later.

**Recommendation:** Retain one set only after the cohesion test proves shared
ownership, destination family, lifecycle, and verification.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Identify every included area and document why no split trigger
applies, or authorize separate Stage 0 work.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## DOC-03 - Authored and generated derivatives

**Question:** Which content is authored, which may be generated from exact
future artifacts, and what comparison blocks generated drift?

**Context and evidence:** Generated schemas/help can aid readers but cannot
replace accepted contracts or create observed results before products exist.

**Options:**

1. Author all initial content; add generated appendices only after products.
2. Generate structure from accepted source metadata with reviewed templates.
3. Mix authored guidance with hash-bound artifact derivatives and explicit
   semantic comparisons.

**Recommendation:** Start authored and source-linked; permit generated
appendices only with exact inputs, observed labels, and drift blocking.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Define content classes, input/output identity, drift method,
failure behavior, and authority precedence.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## DOC-04 - Version identity and cadence

**Question:** What documentation version scheme and release cadence bind a
derivative to architecture, policy, API, schema, and later product identities?

**Context and evidence:** `v1.0` is the work/suite identity, not automatically
the semantic version of the documentation product.

**Options:**

1. Independent semantic documentation version plus consumed-source manifest.
2. Source-suite-aligned version with explicit product compatibility table.
3. Date/revision identity plus immutable source and artifact hashes.

**Recommendation:** Use a distinct semantic documentation version with a
machine-reviewable consumed-source manifest and `ADR-006` classification.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Define identity, predecessor/successor rules, cadence,
compatibility declaration, and retention of prior revisions.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## DOC-05 - Documentation accessibility and usability

**Question:** Which review method and environments qualify documentation
accessibility and usability without being confused with the D6 web-product
accessibility gate?

**Context and evidence:** D1 needs navigable documentation; `WEB-*` vectors
belong to D6 and cannot be borrowed as D1 evidence.

**Options:**

1. Automated Markdown/rendered-HTML structure and link checks only.
2. Automated checks plus keyboard, zoom, contrast, and representative reader
   task review in the selected destination.
3. A destination-specific accessibility audit with named support matrix.

**Recommendation:** Combine automated checks with manual keyboard/zoom and
reader task review, expanding only if the destination warrants it.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Name standards, environments, tasks, result vocabulary,
reviewer, and evidence destination.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## DOC-06 - Review and source-currency responsibilities

**Question:** Who performs architecture/security source-currency review,
legal-source disclaimer review, product editorial review, and release evidence
review?

**Context and evidence:** Human ownership is unified under the project profile,
but technical review responsibilities and external-source dependencies must
remain visible.

**Options:**

1. The User performs every review with separate recorded review roles.
2. Named component/security/accessibility reviewers advise the User, who
   retains acceptance authority.
3. Defer publication until specific external expertise is available.

**Recommendation:** Record distinct technical review responsibilities while
retaining the User's sole human approval authority.

**Decision:** Open.

**Rationale:** To be recorded when accepted.

**Owner:** User

**Decision date:** -

**Acceptance:** Name each responsibility, required source-currency checks,
review cadence, escalation boundary, and evidence record.

**Affected documents:** `assumption.md`, `architecture.md`,
`source-mapping.md`, `implementation-roadmap.md`, and
`implementation-steps.md`.

## Decision dependencies

| Decision | Depends on | Unblocks |
|---|---|---|
| `DOC-01` | None | Product placement, tool selection, operational review |
| `DOC-02` | `DOC-01` destination family and audience evidence | Scope acceptance or required split |
| `DOC-03` | `DOC-01`, exact future artifact availability | Content architecture and drift checks |
| `DOC-04` | `DOC-01`, `DOC-03` | Compatibility and publication identity |
| `DOC-05` | `DOC-01` | Qualification environment and evidence |
| `DOC-06` | `DOC-01`–`DOC-05` responsibility needs | Review ownership and release gate |

## Decision process

1. Confirm current sources and owner boundaries.
2. Compare options against scope, assumptions, compatibility, and failure
   behavior.
3. Record the selected answer, rationale, owner, date, and exact receipt.
4. Reconcile every affected initiative record in the same change.
5. Link product verification only when the decision is first exercised.
