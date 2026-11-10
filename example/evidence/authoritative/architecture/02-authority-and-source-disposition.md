# Architecture authority and RZN-001 source disposition

**Architecture ID:** `ARC-AUT-001`  
**Status:** Accepted  
**Owner and accepting authority:** User, project authority  
**Decision method:** Codex best judgment, expressly authorized for this suite  
**Effective date:** 2026-11-10  
**Architecture revision:** `2.0.0`  
**Related records:** [`AUTH-EX-001`](01-accepted-architecture-baseline.md), [`RZN-001`](../../non-authoritative/realizations/v0/RZN-001-example-record-application.md)  

## Purpose

This record preserves the authority used to convert `RZN-001` into accepted
architecture and maps every unresolved source item to its binding disposition.
It prevents a later consumer from mistaking a Codex inference for an unstated
fact or from treating the original realization as if it accepted these
choices.

## Human authorization captured

### Initial instruction

> based on the attached realization note, create a highly detailed
> architectural specification for the example project. This should be
> considered authoratative and invariant evidence. Place the specification
> suite in the architecture directory provided.

### Decision-method instruction

> complete the architecture suite to your best judgement. I will read it and
> address any issues after it is created

### Dockerization and host-installation instructions

> make this fully dockerized.

> I don;t want to install all the services on teh host. make taht decision now
> and add to the architecturer invaraint

### Shared API-path instruction

> the CLI should use the same API path as teh web app.

### Resulting scope

The instructions authorize:

- creation of an accepted invariant architecture suite for the example
  project in this directory;
- Codex selection of one coherent disposition for `RZN-001-Q01` through
  `RZN-001-Q17`; and
- directly necessary v1 boundaries, contracts, technology choices, limits,
  failure behavior, and verification obligations.

The later Docker instructions specifically authorize revision `2.0.0`, which
supersedes native-host deployment/packaging choices and requires a Compose-only
runtime with no host application-service or toolchain installation. They do
not alter domain behavior or authorize implementation/completion.

The later API-path instruction specifically resolves consumer routing: CLI and
web must use the same versioned `/api/v1` contract and route set. It does not
collapse their distinct host-loopback and private-container network origins.

They do not authorize implementation, initiative acceptance, a completion
claim, alteration of the Codex protocol, changes to unrelated evidence, or an
implicit future revision. The User's planned later review does not make this
baseline provisional; issues found in review require explicit revision or
supersession records.

## Source-question dispositions

| Source ID | Accepted disposition | Owning record |
|---|---|---|
| `RZN-001-Q01` | `name` is the user-chosen human-readable label for the record. It has no uniqueness meaning and is not an identity. | [`ARC-CTR-001`](11-record-domain-contract.md) |
| `RZN-001-Q02` | `name` and `value` are required Unicode strings. `name` is trimmed, single-line, NFC-normalized, non-empty, and limited to 120 code points/480 UTF-8 bytes. `value` is NFC-normalized text, permits empty and multiline content, preserves surrounding whitespace, and is limited to 4,096 code points/16 KiB. Neither is unique. | [`ARC-CTR-001`](11-record-domain-contract.md) |
| `RZN-001-Q03` | The API generates a random UUIDv4 from the operating system CSPRNG. The public and SQLite representation is the canonical lowercase hyphenated 36-character form. Callers cannot supply IDs. | [`ADR-002`](05-ADR-002-identity-order-and-concurrency.md), [`ARC-CTR-001`](11-record-domain-contract.md) |
| `RZN-001-Q04` | Edits use explicit Save and Cancel actions. All updates use optimistic concurrency with the last observed strong ETag; a stale edit fails without overwrite and requires refresh/reconciliation. | [`ARC-CTR-002`](13-record-http-contract.md), [`ARC-CTR-007`](22-web-interaction-contract.md) |
| `RZN-001-Q05` | An internal monotonic, non-reused ordinal defines total creation order. Next/previous select the adjacent ordinal in the full collection or the supplied search context. Boundaries return a successful explicit boundary result without wrapping. | [`ADR-002`](05-ADR-002-identity-order-and-concurrency.md), [`ARC-CTR-003`](14-search-navigation-contract.md) |
| `RZN-001-Q06` | A search contains at most one predicate: one field, one mode, and one query. Text is NFC-normalized and matched case-sensitively without implicit trimming. Nulls do not exist. Results use ordinal order. | [`ARC-CTR-003`](14-search-navigation-contract.md) |
| `RZN-001-Q07` | Regex uses the accepted RE2-compatible subset, unanchored search semantics, explicit user anchors, a 256-byte pattern limit, bounded record/value sizes, a 10,000-record database cap, and a request budget. Unsupported or invalid patterns are stable client errors. | [`ADR-003`](06-ADR-003-search-execution-semantics.md), [`ARC-CTR-003`](14-search-navigation-contract.md) |
| `RZN-001-Q08` | `exacth match` is treated as a typographical form of the mode named `exact`. | [`ARC-CTR-003`](14-search-navigation-contract.md) |
| `RZN-001-Q09` | The SDK is a separately versioned Python 3.12+ synchronous client library, modeled with Pydantic v2 and transported by HTTPX. Its wheel is built/tested in containers and installed into CLI/test/developer images; running the example never requires a host SDK/Python install. | [`ARC-BND-004`](17-python-sdk-boundary.md), [`ARC-CTR-005`](18-python-sdk-contract.md) |
| `RZN-001-Q10` | "Standalone CLI" means an independently versioned OCI image invoked as `docker compose run --rm record-cli`; it requires neither the web product nor host Python/SDK/CLI installation. It calls the API through its image-installed SDK and never mounts/opens SQLite. | [`ARC-BND-005`](19-cli-boundary.md), [`ARC-CTR-006`](20-cli-interaction-contract.md) |
| `RZN-001-Q11` | The CLI must call the API through the Python SDK. The browser app calls the same HTTP API directly through its browser adapter. Both consume the identical `/api/v1` resource paths, methods, representations, errors, search/navigation semantics, and version lifecycle; there is no CLI-only or web-only record API path. Their origins differ only because the host browser enters through Docker-published loopback while the CLI container uses private Compose DNS. Neither may share or invoke the SQLite adapter. | [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ARC-CTR-002`](13-record-http-contract.md) |
| `RZN-001-Q12` | The v2 target is pinned multi-stage Linux OCI images built with Docker BuildKit and orchestrated by Compose. Images contain Python 3.12+, FastAPI, Pydantic v2, `sqlite3`, official `google-re2`, HTTPX, Uvicorn, and container-built framework-free TypeScript assets. Ordered SQL migrations and all build/test tools run in containers. | [`ADR-005`](08-ADR-005-containerized-technology-stack.md) |
| `RZN-001-Q13` | V2 is a local single-user Compose application: host-loopback publication only, private internal network, no app auth/CORS/telemetry, non-root read-only images, named volumes, structured privacy-aware logs, WCAG 2.2 AA browser behavior, bounded resources, and offline networkless maintenance/backup/restore containers. | [`ADR-004`](07-ADR-004-container-only-deployment-trust-model.md), [`ARC-CTR-008`](23-operations-security-contract.md) |
| `RZN-001-Q14` | Deletion, bulk operations, record-level import/export, and record history are deliberately excluded from v1. Opaque validated backup-bundle transfer is an operations/recovery mechanism and does not expose record import/export. | [`AUTH-EX-001`](01-accepted-architecture-baseline.md), [`ARC-CTR-008`](23-operations-security-contract.md) |
| `RZN-001-Q15` | Sufficiency and conformance require record-level IDs; contract/schema tests; image/Compose/SBOM/provenance checks; containerized unit, API, persistence, SDK, CLI, web, migration and recovery tests; clean-host Compose vectors; and traceable completion evidence. | [`ARC-CTR-009`](24-conformance-contract.md) |
| `RZN-001-Q16` | Released documentation and contracts use immutable semantic revisions. Clarifications that cannot change conforming behavior may increment the patch revision; additive behavior increments minor; breaking meaning requires a new major/API version. Implementation evidence proposes a successor and never edits history silently. | [`ADR-006`](09-ADR-006-contract-versioning-and-feedback.md) |
| `RZN-001-Q17` | Compose/runtime packaging, API, SDK, CLI image, and web assets are separate architectural components and independently verifiable outputs. Coordinated phases are allowed, but future work uses narrow initiatives unless a human-authorized scope assessment records an invariant-compatible exception. | [`ADR-007`](10-ADR-007-product-and-delivery-decomposition.md) |

## Additional best-judgment choices

The source questions did not enumerate every detail needed for a usable
contract. This suite therefore also fixes:

- the v1 HTTP resource paths, media types, status behavior, problem format,
  request IDs, and ETag rules in `ARC-CTR-002`;
- the invariant that CLI and web use those same `/api/v1` paths and semantics,
  with origin differences limited to their Docker network boundaries;
- filter, pagination-cursor, weak-snapshot, and boundary behavior in
  `ARC-CTR-003`;
- physical SQLite schema, pragmas, write serialization, migrations, integrity
  checks, and restore rules in `ARC-CTR-004`;
- SDK method and exception surfaces in `ARC-CTR-005`;
- CLI commands, output streams, and exit codes in `ARC-CTR-006`;
- browser state transitions and accessible interaction behavior in
  `ARC-CTR-007`; and
- operational limits and readiness/failure behavior in `ARC-CTR-008`.

Revision `2.0.0` additionally fixes the Compose service/network/volume graph,
container-only host prerequisite, image hardening, internal/public API origins,
containerized CLI invocation, maintenance mutual exclusion, build/test
containerization, Docker-specific recovery/conformance behavior, and the
user-directed single `/api/v1` path shared by CLI and web consumers.

These choices have the same accepted standing as the source-question
dispositions because they fall within the expressly authorized architecture
scope. They remain subject to the suite's explicit change-control process.

## Source limitations preserved

- `RZN-001` is not implementation or completion evidence.
- No existing product was inspected or claimed to conform.
- No deployment benchmark, accessibility audit, package build, migration,
  backup restore, or end-to-end test has yet run.
- Future initiatives must supply that missing evidence rather than treating
  the detail of this architecture as proof of delivery.

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted all listed source dispositions and bounded best-judgment choices as architecture revision `1.0.0` | User's initial and decision-method instructions quoted above |
| 2026-11-10 | Superseded native-host deployment dispositions and accepted Docker Compose-only revision `2.0.0` with no host application-service/toolchain installation | User's exact Dockerization and host-installation instructions quoted above; predecessor preserved in `ARC-REV-001` |
| 2026-11-10 | Fixed CLI and web to the identical `/api/v1` path/semantic contract while retaining network-origin separation | User's exact shared API-path instruction quoted above |

