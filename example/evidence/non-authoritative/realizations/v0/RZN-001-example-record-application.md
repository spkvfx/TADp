# Example record application

**Realization ID:** RZN-001  
**Status:** Recorded; authoritatively dispositioned  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation  
**Related initiative or proposal:** No initiative created; authoritative dispositions are recorded below  
**Reconciliation record:** [`REC-RZN-001-001`](../../reconciliations/RZN-001-architecture-security-reconciliation.md)  

> **Evidence standing:** This realization is non-authoritative proposal input.
> It preserves a requested outcome and candidate solution shape; it is not an
> accepted specification, architecture decision, implementation authorization,
> product commitment, or completion claim.

## Current authoritative reconciliation

The request and candidate wording below remain historical evidence of what was
asked on 2026-11-10. Statements such as "unresolved," "not yet chosen," and
"future decision" describe this note at recording time; they are not the
current source of truth for system design, security policy, or delivery
sequencing.

| Concern | Current authoritative disposition |
|---|---|
| System shape, data model, API, persistence, search, clients, deployment, and D1-D6 delivery | [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md), with question-by-question ownership in [`ARC-AUT-001`](../../../authoritative/architecture/02-authority-and-source-disposition.md) |
| NIST-aligned security and future assurance | [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) |
| HIPAA-aligned data use, safeguards, evidence, and regulated-use successor gate | [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) |
| Permitted profile | Local, single-user, non-production use with purpose-created synthetic data or externally documented de-identified data; no actual or possible ePHI |

Future consumers may cite this realization for requested intent and historical
context only. The two security suites are the primary invariants for security,
permitted data/use, safeguards, review, and evidence, and they guide both this
note and the architecture—not the other way around. Consumers must satisfy the
current architecture inside those policy limits and both applicable security
suites for the same exact artifact and claim; no passing evidence set
substitutes for another.

## Realization

There is a request for a small record-management example that demonstrates a
contract-first path from documentation for a hypothetical SDK and API to an
implemented SDK and Pydantic-modeled API, a standalone command-line interface,
and a web interface, with every executable surface operating on the same
SQLite-backed record capabilities.

The example is intended to make one compact data model usable through multiple
interfaces. A user should be able to create records, move to the next or
previous record, edit the mutable record content, and search by any field using
common text matching modes or regular expressions. The record identifier
remains immutable throughout those interactions.

## Context and evidence

| Question | Record |
|---|---|
| What was observed? | The User described an example web application and an ordered set of four supporting products needed to realize it. |
| Where and when? | Current TADp repository conversation on 2026-11-10; requested placement is this `v0` realization directory. |
| Who is affected? | Example-application users, API and SDK consumers, CLI users, web users, implementers, reviewers, and maintainers of the SQLite data contract. |
| What source supports it? | `SRC-RZN-001-USER-REQUEST`, the User's request in the current conversation. [The product placement guidance](../../../../products/README.md) supplies repository context but does not define application behavior. |
| What was uncertain when recorded? | Field details, update interaction, navigation order, search and regex semantics, API shape, SDK scope, CLI deployment model, operational constraints, and acceptance criteria had not yet been decided. They are now dispositioned by architecture `2.0.1` and the security suites identified above. |

## Source inventory and limits

| Source ID | Source | Standing | Use in this note |
|---|---|---|---|
| `SRC-RZN-001-USER-REQUEST` | User requests and clarifications received 2026-11-10 | Direct request and realization source; not an accepted initiative | Preserves the requested application behavior, product order, stated technology choices, and documentation-to-implementation feedback loop. |
| `SRC-RZN-001-PRODUCT-CONTEXT` | [`example/products/README.md`](../../../../products/README.md) | Repository guidance | Establishes what may count as a product and that each product's actual destination belongs in its governing initiative. It supplies no app-specific requirement. |
| `SRC-RZN-001-PROTOCOL` | [Codex invariant suite](../../../authoritative/LLM/00_Codex_Invariant_Suite_Index.md) | Authoritative protocol | Governs the standing and later use of this note. It does not accept or prescribe the candidate application design. |
| `SRC-RZN-001-ARCH-DISPOSITION` | [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) | Subsequent authoritative architecture | Owns the accepted system decisions, question dispositions, delivery units, and conformance requirements. |
| `SRC-RZN-001-NIST-DISPOSITION` | [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Subsequent authoritative security policy | Owns applicable NIST-aligned security and assurance requirements. |
| `SRC-RZN-001-HIPAA-DISPOSITION` | [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Subsequent authoritative security policy | Owns the permitted data/use profile, HIPAA-aligned safeguards, evidence requirements, and successor gate. |

The word **should** below records the User's requested behavior. It does not
mean that the behavior has passed proposal alignment, human decision gates, or
initiative acceptance.

## Captured application concept

### System boundary

The requested end state is a web application that works with records persisted
in a SQLite database. The request also identifies documentation, API, and CLI
products that precede the web application and establish or reuse the same
capabilities.

At recording time, the request did not determine whether the web and CLI products access the
database only through the API, whether the CLI may open SQLite directly, or
whether a separately delivered SDK mediates either interface. Those are later
contract and architecture decisions. `ADR-001` and the accepted client
contracts now require API-exclusive live persistence and the identical
`/api/v1` route set; direct client access to SQLite is rejected.

### Record model

| Field | Requested role | Mutability | Unresolved detail |
|---|---|---|---|
| `ID` | Database-record UUID | Immutable after creation | UUID version, generator, canonical text form, SQLite representation, exposure at create time, and validation rules are unspecified. |
| `Name` | A user-chosen name | Editable | The source phrase, "A chosen name for the", is incomplete. The named subject, length, requiredness, normalization, and uniqueness rules need confirmation. |
| `Value` | A value supplied for the record | Editable | Data type, requiredness, size, normalization, and whether values are always textual are unspecified. |

At minimum, the requested immutability means an existing record's `ID` should
not change when `Name` or `Value` is edited. Whether callers may provide an ID
during creation or the system always generates it remains an open decision.

### Requested user capabilities

| Capability | Captured expectation | Details still needed |
|---|---|---|
| Next | Move from the current record to the next record. | Stable ordering, behavior at the last record, and whether navigation is global or limited to search results. |
| Previous | Move from the current record to the previous record. | Stable ordering, behavior at the first record, and interaction with newly created or edited records. |
| Create | Create and persist a record with an immutable UUID plus editable `Name` and `Value`. | Defaults, validation, who generates the UUID, duplicate handling, and post-create focus. |
| Edit | Change and persist `Name` and `Value` while displaying `ID` as read-only. This capability is implied by the fields being described as editable. | Save or auto-save behavior, cancellation, validation feedback, concurrency, and failed-write recovery. No explicit edit or save control was requested. |
| Search | Find records by `ID`, `Name`, or `Value` using the requested matching behaviors. | Query composition, result presentation, ordering, pagination, empty-query handling, and navigation within results. |

Deletion, bulk operations, import, export, authentication, authorization, and
audit history were not requested. They remain outside the captured outcome
unless a later proposal deliberately evaluates and accepts them.

### Search behavior

The requested search surface includes all three fields:

- `ID`
- `Name`
- `Value`

For each supported field, the request names these match choices:

- exact match;
- starts with;
- ends with;
- contains; and
- regular-expression matching.

The source spelling `exacth match` is recorded here as likely referring to
`exact match`, but that normalization has not been confirmed as a formal
decision. "Regex features" is also broader than a single defined operator.
The accepted contract will need to specify the regex engine or dialect,
full-match versus substring behavior, case sensitivity, Unicode behavior,
escaping, invalid-pattern errors, resource limits, and consistent behavior
across SQLite, the API, the CLI, and the web interface.

The request does not say whether one query can target several fields at once,
whether multiple predicates can be combined, or whether the match modes apply
identically to a canonical UUID and free-form text. These differences must not
be silently filled in by an implementation.

## Candidate product sequence

The User requested the following order. The identifiers are stable labels for
future realization handoffs; they are not product records or initiative IDs.

| Order | Candidate ID | Requested product | Candidate contribution | Dependency intent |
|---:|---|---|---|---|
| 1 | `RZN-001-P1-DOCS` | Documentation for a hypothetical SDK and API | Establish enough application, database, model, SDK, and API contract detail to guide later development without implementing the SDK or API. | Initial contract foundation for all later products. |
| 2 | `RZN-001-P2-SDK-API` | SDK and API implementation using Pydantic modeling | Build the SDK described by Product 1 and provide the record and search behaviors over SQLite through the documented, validated API. | Implements the first product's documented contracts and supplies evidence for controlled documentation refinement. |
| 3 | `RZN-001-P3-CLI` | Standalone CLI tool | Make all user-visible capabilities planned for the web app available from a command-line interface. | Reuses or conforms to the established data and API contracts. |
| 4 | `RZN-001-P4-WEB` | Web application | Present the requested record fields and next, previous, create, edit, and search experiences in a browser. | Uses the accepted contracts and the proven behavior of preceding products. |

The products have independent outputs, consumers, verification, and possible
release dispositions. A later proposal should therefore assess them as
separately scoped, dependency-ordered initiatives rather than assume that one
umbrella initiative may accept and complete all four. Product 2 also contains
both an SDK and an API; its future scope assessment must determine whether they
form one cohesive acceptance claim or need narrower coordinated initiatives
inside the Product 2 realization suite.

### Product 1: SDK and API documentation

The first requested product is documentation sufficient to guide the remaining
application and database work. It describes a hypothetical SDK and API: neither
the SDK nor the API is implemented as part of Product 1. Candidate documentation
subjects include:

- glossary, system boundary, component responsibilities, and the intended path
  between clients, API, and SQLite;
- SQLite record schema, UUID representation, constraints, indexes, transaction
  behavior, initialization, and schema-evolution policy;
- Pydantic model responsibilities for creation, stored records, updates,
  searches, results, and errors;
- API operations for creation, retrieval, mutable-field updates, deterministic
  next and previous navigation, and search;
- search field and mode enumerations, regex semantics, ordering, pagination or
  cursor behavior, empty results, and invalid-query responses;
- immutability enforcement for `ID` and validation rules for `Name` and
  `Value`;
- consistent error semantics for missing records, validation failures, invalid
  regex, database failures, and concurrency conflicts where applicable;
- the SDK's intended audience, public interface, examples, compatibility
  policy, and relationship to CLI and web consumers;
- security, resource-limit, observability, configuration, deployment,
  compatibility, migration, and recovery decisions appropriate to an example
  application; and
- requirement-to-contract and contract-to-verification traceability for each
  later product.

Product 1 should be versioned as the initial documented contract. Product 2
will test that contract against an implementation. Implementation experience
may identify omissions, contradictions, or impractical details, but it does not
silently make the original documentation say something different.

### Product 2: SDK and Pydantic-modeled API

The second requested product implements both the SDK described by Product 1 and
the executable API. The candidate outcome includes an SDK that:

- is built from the Product 1 documentation rather than from an unrelated
  interface invented during implementation;
- exposes the documented record, navigation, update, and search capabilities;
- communicates with the API or otherwise uses the exact accepted boundary
  established by the future Product 2 architecture;
- presents documented models, errors, and compatibility behavior to its
  consumers; and
- is verified against the current documented SDK contract.

The candidate outcome also includes an API that:

- persists the three-field record in SQLite;
- uses Pydantic models at its validated input and output boundaries;
- prevents an update from changing an existing `ID`;
- supports create, retrieve, mutable-field update, next, previous, and all
  accepted search modes;
- returns stable, documented response and error shapes; and
- is verified against the current contracts established by Product 1.

The SDK language, packaging, public surface, generated-versus-handwritten
status, and supported consumers were not chosen by this realization. The API framework,
transport, route layout, model names, synchronous or asynchronous execution,
database access library, migration mechanism, and deployment form are also not
chosen by this realization. Architecture `2.0.1`, especially `ADR-005` and the
SDK/API contracts, now owns those selections.

#### Documentation and implementation feedback loop

The requested development loop is:

1. Product 1 documents the proposed SDK, API, application, and SQLite contract.
2. Product 2 builds the SDK and API from that documentation.
3. Product 2 records conformance results and concrete implementation evidence.
4. Product 1 documentation is refined in a traceable new version when the
   implementation reveals a justified clarification, correction, or addition.
5. Product 2 is reconciled with the refined documentation, with compatibility
   consequences and verification kept visible.

This loop is intended to improve both the documentation and implementation. It
must preserve which documentation version guided each implementation version.
A discovered mismatch is evidence to reconcile; it is not automatic authority
to declare either side correct, retroactively edit historical documentation, or
change an accepted contract without its governing review and decision process.

### Product 3: standalone CLI

The third requested product is a standalone command-line tool with feature
parity with the intended web application. Its candidate command surface needs
to cover:

- displaying a record and its immutable ID;
- navigating to the next and previous record;
- creating a record;
- editing `Name` and `Value` without changing `ID`;
- searching each field with every accepted match mode, including regex; and
- reporting validation, no-result, boundary, invalid-regex, and persistence
  failures in a usable command-line form.

"Standalone" was not defined by the request. It could have meant a distributable executable, a
tool that does not require the web application, a tool that embeds direct
SQLite access, or an API client that can be installed and run independently.
The accepted architecture resolves it as an independently versioned, one-shot
Compose CLI image that uses the SDK/API and mounts no application state.

### Product 4: web application

The fourth requested product is the browser-facing application. Its candidate
experience includes:

- a read-only presentation of `ID`;
- editable controls for `Name` and `Value`;
- next, previous, create, and search controls;
- a defined way to persist or cancel field edits;
- field selection and match-mode selection for searches;
- a query input capable of accepting literal or regex text as appropriate;
- search-result presentation and deterministic navigation; and
- visible validation, empty-state, boundary, loading, success, and error
  feedback.

The request did not choose a web framework, visual design system, browser
support policy, accessibility target, API integration pattern, or deployment
model. Architecture `2.0.1`, especially `ARC-BND-006`, `ARC-CTR-007`, and
`ADR-005`, now owns those decisions.

## Candidate end-to-end experiences

These flows restate the requested outcome for later proposal analysis; they are
not accepted test cases.

### Create and view a record

1. The user begins a create action.
2. The user supplies the accepted `Name` and `Value` inputs.
3. The system validates the mutable fields and obtains a UUID according to the
   future creation contract.
4. SQLite persists one record atomically.
5. The active interface shows the saved record, including its read-only ID, or
   gives a stable error without claiming success.

### Edit mutable fields

1. The user opens an existing record.
2. The interface exposes `Name` and `Value` for editing and keeps `ID`
   read-only.
3. The user changes one or both mutable fields and invokes the future accepted
   persistence behavior.
4. Validation and persistence either succeed together or return a clear error.
5. A subsequent read shows the changed mutable values and the original ID.

### Navigate records

1. The user views a record in either the full collection or a search result.
2. Next or previous applies the future accepted stable ordering.
3. The interface shows the adjacent record or the defined collection boundary
   state.
4. Repeating the same operation against unchanged data produces consistent
   navigation.

### Search records

1. The user chooses `ID`, `Name`, or `Value`.
2. The user chooses an accepted match mode.
3. The user enters a literal or regex query appropriate to that mode.
4. The system validates the query and applies documented, consistent semantics.
5. Results are returned in a deterministic order and can be inspected or
   navigated, while no matches and invalid patterns have distinct outcomes.

## Cross-product consistency goals

The later product suites should evaluate these candidate goals:

- **One record contract:** all interfaces agree on field meaning, validation,
  serialization, and ID immutability.
- **One search contract:** equivalent supported searches produce equivalent
  result membership and ordering across API, CLI, and web surfaces.
- **Deterministic navigation:** next and previous use an explicit stable order
  and defined boundary behavior.
- **Contract-first traceability:** downstream behavior maps to an identified
  Product 1 documentation version rather than inventing incompatible local
  rules, and implementation-led refinements create a traceable successor
  documentation version.
- **Truthful feature parity:** "all the features" has a named capability map
  and verifiable exceptions rather than an informal similarity claim.
- **Safe failure behavior:** validation, regex, database, and concurrency
  errors do not corrupt a record or change its immutable ID.

## Historical assumptions and questions

These items were intentionally unresolved in the source request. They are kept
to preserve source identity, but their current dispositions belong to the
authoritative records listed after the table.

| ID | Question or assumption requiring a decision | Products affected |
|---|---|---|
| `RZN-001-Q01` | What complete meaning was intended by the truncated phrase describing `Name`? | All |
| `RZN-001-Q02` | Are `Name` and `Value` required strings, and what length, normalization, uniqueness, empty-value, and Unicode rules apply? | All |
| `RZN-001-Q03` | Which UUID version, generator, canonical representation, SQLite storage representation, and create-time ownership apply to `ID`? | Docs, API, CLI, web |
| `RZN-001-Q04` | What explicit user action saves edits, can edits be cancelled, and how are concurrent changes handled? | API, CLI, web |
| `RZN-001-Q05` | What total ordering defines next and previous, what happens at each boundary, and does navigation operate within search results? | Docs, API, CLI, web |
| `RZN-001-Q06` | Do searches target one field at a time or combine predicates, and what case, Unicode, whitespace, null, and escaping semantics apply? | Docs, API, CLI, web |
| `RZN-001-Q07` | What regex dialect and matching behavior apply, and what validation, timeout, pattern-size, and result limits prevent unsafe or inconsistent execution? | Docs, API, CLI, web |
| `RZN-001-Q08` | Is `exacth match` only a typographical form of `exact match`? | Docs |
| `RZN-001-Q09` | What language, packaging, public interface, compatibility policy, and consumers should the Product 2 SDK support? | Docs, SDK/API, CLI, web |
| `RZN-001-Q10` | Does the CLI call the API or access SQLite directly, and what distribution property makes it "standalone"? | Docs, API, CLI |
| `RZN-001-Q11` | Must the web app and CLI always use the API, or may either share a lower-level data-access component? | Docs, API, CLI, web |
| `RZN-001-Q12` | Which API framework, SQLite library, migration approach, web stack, and packaging approach are compatible with the intended example? | Product-specific |
| `RZN-001-Q13` | What authentication, authorization, privacy, logging, accessibility, browser, performance, backup, and deployment expectations apply? | Product-specific |
| `RZN-001-Q14` | Is deletion deliberately excluded, and are bulk, import, export, or history capabilities also out of scope? | All |
| `RZN-001-Q15` | What exact evidence will show that Product 1 is sufficient and that each later product conforms to it? | All |
| `RZN-001-Q16` | What versioning and decision process distinguishes a documentation clarification from a contract change when Product 2 implementation evidence feeds back into Product 1? | Docs, SDK/API |
| `RZN-001-Q17` | Do the SDK and API within Product 2 form one cohesive acceptance claim, or do their independent outputs and verification require coordinated narrow initiatives? | SDK/API |

| Historical question group | Current authoritative owner |
|---|---|
| `Q01`-`Q04` record model, creation, update, and concurrency | `AUTH-EX-001`, `ADR-002`, `ARC-CTR-001`, and `ARC-CTR-002` |
| `Q05`-`Q08` ordering, navigation, search, regex, and typo disposition | `ADR-002`, `ADR-003`, and `ARC-CTR-003` |
| `Q09`-`Q12` SDK, API-only access, CLI meaning, stack, and packaging | `ADR-001`, `ADR-005`, and `ARC-BND/CTR-002` through `008` |
| `Q13` security, privacy, logging, accessibility, performance, backup, browser, and deployment | `ADR-004`, `ARC-CTR-007`, `ARC-CTR-008`, NIST `1.0.1`, and HIPAA `1.0.1` |
| `Q14` excluded capabilities | `AUTH-EX-001.9` and `ARC-CTR-009` |
| `Q15`-`Q17` evidence, version feedback, cohesion, and delivery decomposition | `ADR-006`, `ADR-007`, and `ARC-CTR-009` |

## Risks and dependencies to carry forward

The authoritative suites now own the mitigations and evidence gates for these
risks. The bullets remain useful verification concerns, not open authority to
choose a conflicting architecture or security boundary.

- If the documentation product leaves data or search semantics ambiguous, each
  executable product may implement a different contract.
- If implementation feedback edits Product 1 in place, the repository will
  lose the identity of the contract that actually guided a Product 2 version.
- If the SDK and API are accepted as one scope without passing the required
  cohesion test, independent blockers or partial completion may be obscured.
- SQLite text operations and an application regex engine may disagree unless
  field normalization and match semantics are defined once and tested across
  every surface.
- Unbounded or unsafe regex evaluation may create availability or resource-use
  problems even in an example application.
- Next and previous cannot be reliable without a total order and an explicit
  policy for collection changes between requests.
- ID immutability can be weakened if update models, route parameters, database
  keys, and client forms enforce different rules.
- Direct database access from multiple products may duplicate validation and
  concurrency behavior; API-only access may affect the meaning of a standalone
  CLI. The contract and architecture work must decide the boundary.
- The four products are separable outcomes. Treating them as one completion
  claim would obscure independent blockers, verification, and release status.

## Candidate outcome

Users can manage a small SQLite-backed record set through a consistent web
experience: they can create records, view immutable UUIDs, edit names and
values, navigate deterministically, and search any field using defined literal
or regex matching. Developers and operators also have an accepted, versioned
contract, a conforming SDK and Pydantic-modeled API, and a standalone CLI that
exposes the same capabilities before the web product is delivered.

That outcome is permitted only inside the reconciled local, single-user,
non-production synthetic/documented-de-identified profile. It does not
authorize actual or possible ePHI, remote or multi-user access, a shared
workstation, production clinical use, third-party record processing, or a
compliance claim.

## Historical suggested next step and current handoff

The original suggested next step was to use `RZN-001` as source input and
create independent, versioned realization-note suites for these four candidate
products:

1. `RZN-001-P1-DOCS` - documentation for the hypothetical SDK and API;
2. `RZN-001-P2-SDK-API` - implemented SDK and Pydantic-modeled API;
3. `RZN-001-P3-CLI` - standalone CLI; and
4. `RZN-001-P4-WEB` - web application.

Each suite should cite this app-level realization, preserve its product-specific
source statements and unresolved items, and avoid treating another suite's
unaccepted interpretation as authority. Proposal creation should then assess
the narrow initiative boundary, dependency, product destination, acceptance
claim, and verification obligations for each product. No product implementation
is authorized by this note.

Current work must instead follow the accepted `D1`-`D6` decomposition in
`ADR-007`. Each narrow future initiative must cite architecture `2.0.1`, NIST
`1.0.1`, and HIPAA `1.0.1`; map the exact applicable vectors and policies; and
carry the permitted data profile and successor triggers into its specification
and evidence plan.

## Handoff notes

When this realization or a product-specific successor is used as proposal
input, cite its realization ID and source IDs in the proposal inventory.
Preserve the original request and historical wording. The User explicitly
authorized these in-place reconciliation annotations on 2026-11-10; future
interpretation, acceptance, rejection, correction, or supersession belongs in
linked authoritative or lifecycle records unless equally explicit authority
permits another source-preserving annotation.
