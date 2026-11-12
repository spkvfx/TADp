# Versioned derivative contract documentation

**Realization ID:** `RZN-001-P1-DOCS-N01`  
**Suite:** [`RZN-001-P1-DOCS-SUITE@v1.0`](00-RZN-001-P1-DOCS-suite-index.md)  
**Suite version:** `v1.0`  
**Status:** Recorded; invariant-bounded proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation and [`RZN-001`](../v0.0/RZN-001-example-record-application.md)  
**Historical product lineage:** `RZN-001-P1-DOCS`  
**Accepted delivery-unit alignment:** `D1 Architecture and contract documentation`  
**Related initiative or proposal:** None created  

> **Evidence standing:** This note records a detailed candidate documentation
> outcome constrained by accepted invariants. It is not the documentation
> product itself and does not accept requirements, choose a repository
> destination, authorize delivery, or prove any executable behavior.

## Realization

There is a bounded opportunity to publish one versioned, audience-oriented
documentation set that makes the accepted example-record contracts usable by
future implementers and consumers while preserving the authoritative sources
as the sole owners of normative meaning.

The candidate set would explain the record, HTTP, search/navigation, SQLite,
Python SDK, CLI, web, container, operations, security, compatibility, and
verification boundaries needed to guide later products. It would not create
those products, repeat the architecture as a competing source, or report that
any future behavior has been observed.

## Narrow outcome and beneficiary

| Dimension | Candidate record |
|---|---|
| Outcome | A coherent derivative documentation set tied to exact architecture and security revisions, with clear normative-source links and no implementation claim |
| Primary beneficiaries | Future D2-D6 implementers, SDK consumers, CLI and web reviewers, local operators, verification owners, and maintainers evaluating contract changes |
| Authority boundary | Explanatory publication only; accepted architecture and security suites retain every normative decision |
| Output class | Versioned documentation, examples, diagrams, compatibility tables, and source-to-verification indexes; no executable artifact |
| Independent review claim | The derivative set is complete, internally coherent, source-accurate, navigable, and honest about missing implementation evidence |
| Explicit non-claim | No API, SDK, database, image, Compose deployment, CLI, browser bundle, test result, security control, or release is delivered |

## Context and evidence

| Question | Record |
|---|---|
| What was requested? | Product 1 in `RZN-001` requested documentation for a hypothetical SDK and API before their implementation, including the application, database, models, behavior, and feedback loop. |
| What changed after that request? | `ARC-SUITE-001@2.0.1` accepted the complete technical architecture, and the NIST/HIPAA suites accepted primary future-development security and permitted-use gates. The documentation opportunity is now derivative rather than a place to invent unresolved contracts. |
| Where does this apply? | A future documentation destination selected by a governed proposal; no path, publishing system, or release channel is chosen here. |
| Who is affected? | Developers, reviewers, container-platform owners, API/SQLite implementers, SDK/CLI/web consumers, local operators, security reviewers, and future proposal authors. |
| What is uncertain? | Exact document destinations, audience segmentation, generated-versus-authored boundaries, publication tooling, release cadence, and whether any independently acceptable document group needs its own initiative. |
| What is already decided? | System shape, technology stack, record/search/API/persistence/SDK/CLI/web/operations contracts, D1-D6 decomposition, versioning, data/use profile, security policies, successor triggers, and conformance vectors. |

## Source inventory and limits

| Source | Standing | Permitted use in a future documentation product |
|---|---|---|
| [`RZN-001`](../v0.0/RZN-001-example-record-application.md) | Non-authoritative historical realization | Explain the requested outcome and product lineage only; do not revive resolved questions as current choices. |
| [`ARC-AUT-001`](../../../authoritative/architecture/02-authority-and-source-disposition.md) | Accepted architecture authority record | Identify the authoritative dispositions of `RZN-001-Q01` through `Q17`. |
| [`ARC-SUITE-001@2.0.1`](../../../authoritative/architecture/00-architecture-suite-index.md) and records `01`-`24` | Accepted invariant architecture | Own all technical boundaries, contracts, decisions, exclusions, delivery units, and conformance meaning. |
| [`SEC-NIST-SUITE-001@1.0.1`](../../../authoritative/security/NIST/00-nist-security-policy-suite-index.md) | Accepted future-development security invariant | Own NIST-aligned security requirements, limitations, evidence methods, and claim wording. |
| [`SEC-HIPAA-SUITE-001@1.0.1`](../../../authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md) | Accepted prospective security/data-use invariant | Own allowed data/use, HIPAA-aligned safeguards, inherited dependencies, evidence obligations, and regulated-use gate. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | Accepted conformance contract | Supply exact vector and delivery-gate locators; never use planned vectors as passing evidence. |
| [`REC-RZN-001-001`](../../reconciliations/RZN-001-architecture-security-reconciliation.md) | Non-authoritative applied-comparison record | Explain source relationships and applied dispositions only; do not substitute it for a binding source. |

## Candidate documentation architecture

The following publication areas are candidate members of one derivative set.
They are not accepted filenames or destinations.

| Candidate area | Content boundary | Authoritative owner to cite | Content explicitly excluded |
|---|---|---|---|
| Orientation and glossary | Actors, components, artifact identities, record/search vocabulary, and reading order | `ARC-SUITE-001`, `ARC-BND-001`, `ADR-007` | New topology, inferred implementation status, or alternate terminology that changes accepted meaning |
| Record and model reference | Exact `id`, `name`, `value`, normalization, limits, mutability, ETag wrapper, and exclusions | `ARC-CTR-001`, `ADR-002` | A fourth public field, caller-selected ID, delete/history, permissive coercion, or undocumented defaults |
| HTTP API reference | Bases, `/api/v1`, media types, create/get/update, problems, headers, status, ETags, and unsupported methods | `ARC-CTR-002`, `ARC-BND-002` | A CLI-only/web-only route, force update, idempotency guarantee, auth/TLS claim, or implementation-generated semantics |
| Search and navigation reference | One-predicate model, field/mode tokens, NFC/case behavior, RE2 subset, cursors, ceilings, budgets, order, neighbors, and boundaries | `ADR-003`, `ARC-CTR-003` | Client-side membership, SQLite `LIKE` semantics, arbitrary predicates, wraparound, or unsafe regex behavior |
| Persistence and recovery reference | Schema identity, internal metadata, transactions, locks, migrations, named volumes, backup, restore, and integrity behavior | `ARC-BND-003`, `ARC-CTR-004`, `ARC-CTR-008` | Public SQL contract, host SQLite path, direct edits, concurrent maintenance, merge/import shortcut, or claimed host-loss objective without evidence |
| Python SDK reference | Public imports, immutable models, client lifecycle, methods, retries, exceptions, compatibility, wheel/container use | `ARC-BND-004`, `ARC-CTR-005` | Async API, raw request escape hatch, SQLite/server dependency, host-install promise, or write retry |
| CLI user reference | Compose invocation, commands, stdin boundaries, human/JSON output, diagnostics, exit codes, and isolation | `ARC-BND-005`, `ARC-CTR-006` | Native host CLI, file-mount input, direct HTTP/SQLite, hidden prompts, force overwrite, server control, or background daemon |
| Web user reference | Routes, states, create/edit/search/navigation flows, accessibility, conflict/race behavior, storage and same-origin security | `ARC-BND-006`, `ARC-CTR-007` | Durable browser records, cross-origin endpoint, service worker, remote assets, separate web server, or false accessibility claim |
| Container/operator guide | Host prerequisites, BuildKit stages, Compose topology, configuration, health, hardening, safe lifecycle, maintenance, and destructive boundaries | `ADR-004`, `ADR-005`, `ARC-CTR-008` | Native fallback, wildcard/LAN access, unreviewed overrides, `down -v` as routine, or unsupported platform claim |
| Security and permitted-use guide | Local/single-user profile, data classification, safe handling, inherited host controls, incident/recovery limits, and successor triggers | NIST `SEC-POL-01`-`14`; HIPAA `HSP-001`-`015` | NIST certification, HIPAA compliance, ePHI authorization, legal conclusion, or policy weakening |
| Compatibility and evidence guide | Architecture/API/schema/artifact versions, feedback workflow, vectors, evidence schema, limitations, and claim vocabulary | `ADR-006`, `ARC-CTR-009`, `SEC-NIST-VER-001`, `SEC-HIPAA-DEV-001` | Passing results, completion status, or compatibility inferred without exact artifacts and evidence |

## Normative-source presentation rules

A future documentation product should preserve these distinctions because they
are material to its candidate usefulness:

1. **Binding requirement:** cite the exact architecture or security record,
   revision, section, claim, policy, or vector ID.
2. **Derivative explanation:** state that it paraphrases a named source and
   provide a direct repository link.
3. **Example:** use synthetic values, label the example non-normative, and
   ensure it satisfies the accepted contract.
4. **Observed implementation:** include only when exact product/version/
   environment evidence exists, and never present observation as authority.
5. **Verification result:** identify exact artifact, method, vector, result,
   limitation, reviewer, and time; planned tests remain plans.
6. **Open proposal question:** keep it visibly unresolved and do not present a
   recommendation as an accepted decision.

Generated OpenAPI, JSON Schema, command help, image labels, Compose renders,
and SDK signatures may become useful derivative appendices only after they
exist. They must be checked against the accepted Markdown contracts and cannot
silently take ownership when they disagree.

## Exact profile and limitation content

Every candidate entry point that could be read without the rest of the set
would need a concise, consistent limitation statement covering:

- local, single-user operation under one authorized host OS account;
- Docker Compose as the only supported runtime and Docker/Compose plus a
  supported browser as the host runtime prerequisites;
- exact IPv4-loopback browser ingress and private Compose-network client
  ingress to the same `/api/v1` router;
- non-production records using purpose-created synthetic data or externally
  documented de-identified data, subject to the NIST suite's independent data
  restrictions;
- prohibition of actual, possible, or insufficiently classified ePHI;
- absence of application accounts, roles, sessions, remote access, TLS,
  per-user audit, high availability, and regulated-use authorization;
- API-exclusive live SQLite with stopped-API networkless maintenance;
- no delete, bulk mutation, record import/export, history, offline writes, or
  alternate state path; and
- successor-architecture requirements for remote, multi-user, shared-
  workstation, third-party-processing, production, sensitive/regulated, or
  compliance-expansion requests.

## Security-policy applicability carried into documentation

| Documentation concern | Primary NIST policy anchors | Primary HIPAA anchors | Candidate treatment |
|---|---|---|---|
| Authorized use and claims | `SEC-POL-01`, `SEC-POL-14` | `HSP-001`, `HSP-002`, `HSP-015` | State exact permitted profile and prohibited claim language at every relevant entry point. |
| Network and access boundary | `SEC-POL-02`, `SEC-POL-03` | `HSP-004`, `HSP-005`, `HSP-011` | Explain OS/Docker inherited identity, loopback/private network, and lack of app authentication without implying equivalence to regulated controls. |
| Data handling and diagnostics | `SEC-POL-06`, `SEC-POL-08` | `HSP-006`, `HSP-008` | Use safe synthetic examples and document no-store, redaction, explicit success-output boundaries, and non-audit limitation. |
| State, recovery, and operations | `SEC-POL-05`, `SEC-POL-07`, `SEC-POL-09`, `SEC-POL-13` | `HSP-007`, `HSP-010`, `HSP-012` | Document transaction truth, resource failure, offline recovery, incident preservation, and host-loss limitations. |
| Build and release | `SEC-POL-04`, `SEC-POL-10`, `SEC-POL-12` | `HSP-009`, `HSP-013` | Describe immutable identity, supply-chain evidence, vulnerability handling, and external-service limits without asserting a scan result. |
| Assurance and retention | `SEC-POL-11` | `HSP-003`, `HSP-014` | Link exact planned vectors and required risk/source/evidence records; do not pre-fill future results. |

Every future proposal would still need a policy-by-policy applicability review;
this summary is not that decision record.

## Candidate examples and fixture discipline

- Use unmistakably fictional names and values created for the explanation.
- Do not derive examples by modifying a real person's details.
- Do not place record content in URLs, environment examples, image labels,
  logs, issue text, screenshots, or command histories when the same point can
  be shown with safe placeholders or documented synthetic canaries.
- When a full record is necessary to explain round-trip behavior, identify its
  synthetic origin and keep the example consistent across API, SDK, CLI, and
  web representations.
- Never present a UUID as de-identification evidence.
- Show dangerous lifecycle commands, if they must be named for warning, only
  in a conspicuous prohibited/destructive context and never in a safe runbook
  sequence.

## Candidate verification boundary

The candidate documentation outcome would be reviewable through documentation
evidence only. Relevant checks include:

| Check | Candidate evidence | Limitation |
|---|---|---|
| Source identity | Every normative statement links to an exact active source/revision/ID | A correct link does not prove the explanation is semantically complete. |
| Contract coverage | Coverage matrix for architecture records `00`-`24`, policies, and owned consumer topics | Coverage does not prove product implementation. |
| Internal coherence | Terms, paths, field/mode tokens, status/problem codes, limits, versions, and exclusions agree across the set | Review cannot replace executable conformance. |
| Local links and structure | Link checker, one H1 per record, balanced fences, no template residue, version/index reconciliation | Structural success is not acceptance or correctness. |
| Example validity | Static review or later containerized contract checks prove examples are invariant-compatible | A passing example is not full behavior coverage. |
| Claim-language review | No implementation, conformance, release, NIST certification, HIPAA compliance, or ePHI authorization claim | Absence of overclaim does not deliver a control. |
| Revision traceability | Exact predecessor/successor and compatibility classification under `ADR-006` | Version metadata does not authorize a semantic change. |

The authoritative D1 gate in `ARC-CTR-009` remains the minimum structural
oracle. Any future product-completion claim would additionally require its
governing workflow records; this realization creates none.

## Dependencies and feedback handling

- The active architecture and security suite revisions are required inputs.
- D2-D6 implementation evidence may later reveal a defect or ambiguity, but
  the documentation must route it through `ADR-006`; it must not edit accepted
  meaning to match behavior.
- A pure explanatory correction that cannot change conforming behavior may be
  a patch; any changed vector, accepted value, route, schema, topology, trust
  boundary, or existing behavior requires the appropriate authoritative
  revision and compatibility analysis.
- Each executable product must declare the exact documentation/architecture
  version it consumed. A newer document does not retroactively govern an older
  artifact without explicit reconciliation.

## Risks to preserve for proposal analysis

| Risk | Consequence | Candidate control to evaluate later |
|---|---|---|
| Copying invariant text creates drift | Readers may follow a stale derivative instead of authority | Prefer precise links, generated source maps, and revision-diff review. |
| Generated docs become de facto authority | Implementation defects can overwrite accepted meaning | Treat generated artifacts as observed derivatives and run drift checks. |
| One guide mixes operator, consumer, and implementer concerns | Independent audiences or acceptance claims become hard to review | Assess document-level cohesion and split triggers before initiative creation. |
| Examples leak sensitive or real-person data | Documentation and collaboration artifacts leave the permitted profile | Require synthetic provenance and artifact scanning. |
| Security disclaimers are buried | Users may infer remote, production, or regulated suitability | Repeat concise profile limits at entry points and risky procedures. |
| Planned vectors look like passing tests | Future work may overclaim readiness | Label all vector catalogs as prospective until exact results exist. |
| SDK/API documentation implies host installation | The derivative conflicts with Compose-only architecture | Show only containerized consumption paths and exact private API origin. |

## Questions that remain for a future proposal

These are product-publication decisions, not reopened architecture questions:

1. Which repository paths or publishing destination own the derivative set?
2. Which audience-specific documents form one coherent acceptance claim, and
   which would require separate narrow work?
3. What portion is authored versus generated, and what drift check protects
   each generated derivative?
4. What version identity and release cadence tie the set to architecture,
   policy, API, schema, SDK, CLI, web, and container artifacts?
5. What review method verifies accessibility and usability of the
   documentation itself without confusing that with D6 accessibility?
6. Who owns security-source currency, legal-source disclaimers, and product
   documentation review?

No answer is selected by this realization.

## Candidate outcome

Future developers and users can locate one versioned documentation set that
accurately explains how to build and consume the accepted example-record
contracts, how to operate only inside the approved profile, which exact
invariants own each statement, and what evidence would be needed before any
implementation or conformance claim.

## Suggested next step

Take no initiative action now. If the User later requests continuation, create
a documentation-only proposal from this note, inventory the exact active
invariants, select the product destinations, perform the mandatory scope
assessment, and retain all unresolved publication choices for explicit human
disposition.

## Handoff notes

A receiving proposal must cite this realization ID and the parent `RZN-001`
source separately. It must state which candidate publication areas it accepts,
changes, defers, or rejects; map every normative statement to its authoritative
owner; and avoid treating the detail in this note as specification acceptance.



## Version-scope migration addendum (2026-11-12)

**Version scope:** `v1.0`

**Migration authority:** [EX-VSG-DR-001](../../../../initiatives/decision-receipts/EX-VSG-DR-001-initiative-migration.md)

**Current initiative target:** [INIT-IMP-001](../../../../initiatives/v1.0/implementation/INIT-IMP-001-contract-documentation/README.md)

**Exact source catalog:** [RZN-001-P1-DOCS-N01](01-RZN-001-P1-DOCS-contract-documentation.md)

The original headers and one-to-one allocation language remain historical evidence under the prior revision. This addendum adopts scope membership and many-target catalog capability without changing source identity, relabeling this note or promoting its non-authoritative standing. The existing target retains the same narrow Proposed claim. Future independent outcomes require their own initiative records, not necessarily another version. The initiative index owns current assignments; the historical branch and base above remain history.
