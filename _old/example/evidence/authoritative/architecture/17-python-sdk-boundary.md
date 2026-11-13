# Python record SDK system boundary

**Architecture ID:** `ARC-BND-004`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Owner:** SDK component owner under a future accepted initiative  
**Last reviewed:** 2026-11-10  
**Related records:** [`ARC-CTR-001`](11-record-domain-contract.md), [`ARC-CTR-002`](13-record-http-contract.md), [`ARC-CTR-003`](14-search-navigation-contract.md), [`ARC-CTR-005`](18-python-sdk-contract.md), [`ADR-006`](09-ADR-006-contract-versioning-and-feedback.md)  

## Boundary statement

The Python SDK boundary is the versioned `example-records-sdk` wheel built by
the `sdk-wheel` stage, installed into approved consumer/test image stages, and
its documented synchronous public package. It translates typed Python calls
into `/api/v1` HTTP requests and accepted responses/problems into immutable
Pydantic models and stable SDK exceptions. Supported use is containerized; the
wheel remains an independently identifiable artifact but is never a required
host installation. The SDK does not own record rules, persistence, search
membership, interactive prompting, Compose control, UI state, API startup, or
SQLite access.

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| Expose a small typed, synchronous Python client | SDK package | Async client, ORM, database adapter, or web framework integration |
| Validate obvious client-side shape before transport | Public Pydantic models and method signatures | Final domain acceptance; API always revalidates |
| Encode paths, query parameters, headers, JSON, and cursors | Transport adapter | Creating alternate wire semantics or undocumented routes |
| Preserve ETags with retrieved records and send conditional updates | SDK result wrappers | Resolving conflicts or silently refetching/overwriting |
| Decode problem documents into stable exception classes | Error adapter | Leaking HTTPX internals as the primary public contract |
| Apply the accepted safe-read retry policy | Transport policy | Retrying create/update or hiding an indeterminate write outcome |
| Support injection of an HTTPX transport for tests | Client constructor | Global monkey-patching or a second fake domain implementation |
| Publish semantic versions and deprecation metadata | SDK release owner | Changing server contracts or claiming server compatibility without tests |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | Containerized Python integrator or `record-cli` | Constructor arguments, method values, public models | Python types and Pydantic v2 strict models | Public symbols follow SDK semantic versioning |
| Inbound | API service | JSON, ETag, cursor, request ID, and problem responses | Status-specific decoder and response models | Compatible with `/api/v1`; malformed success is `ProtocolError` |
| Outbound | API service | HTTP requests under the accepted contracts | Request models and transport encoder | No undocumented fields, routes, or direct database behavior |
| Outbound | Containerized Python integrator or CLI | Immutable records/pages/neighbors and SDK exceptions | Public result/exception model | Stable meaning within SDK major version |
| Outbound | Diagnostic hook | Method, route template, status, request ID, duration | Redaction policy | Never emit record values or raw search query text by default |

## Package and dependency boundary

- The distribution name is `example-records-sdk`; the import package is
  `example_records_sdk`.
- The public namespace is an explicit allowlist documented in
  `ARC-CTR-005`. Internal modules and HTTPX/Pydantic implementation objects not
  re-exported there are not compatibility promises.
- Released API/CLI images use the ADR-005-selected Python 3.13 minor and base
  family. The wheel's claimed CPython `>=3.12,<3.15` matrix is tested only in
  pinned Linux containers; no host-Python support or prerequisite is implied.
  A later Python/platform may be added only after its containerized conformance
  matrix passes.
- Runtime dependencies are Pydantic v2 and HTTPX in accepted compatible major
  ranges. The package must not depend on FastAPI, Uvicorn, SQLite drivers, the
  API implementation package, the CLI package, or the web product.
- The wheel must install in a clean pinned container without the repository
  checkout and may not start an API server as an import side effect.
- The CLI runtime installs the exact wheel produced/tested by the same build
  graph. Rebuilding an untracked wheel in a later stage or installing from a
  mutable package index is prohibited.
- Host `python`, `pip`, `pipx`, virtual environments, and SDK installation are
  outside the supported architecture. Developer use occurs through the test or
  explicitly declared developer image.

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| Live records | API/SQLite | None in SDK except through accepted API commands | Refetch after uncertainty; never reconstruct from cache |
| Base URL, timeouts, transport, and open connection pool | `RecordClient` instance | Constructing integrator | Close client or construct a new instance |
| Returned record/page models | Calling process memory | SDK decoder only | Immutable snapshot; refetch to observe change |
| Current ETag | `VersionedRecord` or neighbor result | API response | Required for update; stale value produces conflict |
| Paging cursor | API-produced opaque string held by caller | API only | Pass back unchanged with identical filter; restart search if rejected |
| SDK artifact identity | Wheel filename, version, SHA-256, SBOM/provenance linkage | `sdk-wheel` build stage/release process | Consumer images must copy that exact artifact; digest mismatch blocks release |

## Invariants and failure boundaries

- Importing the package performs no network, file, environment, logging, or
  global-client initialization.
- `RecordClient` is an explicit closeable context manager. No module-global
  mutable client or implicit base URL is permitted.
- SDK model validation improves feedback but does not claim a write succeeded.
  Only a successfully decoded API response does.
- The SDK never evaluates regex, filters records, computes neighbors, generates
  record IDs, edits cursors, or opens the SQLite database.
- GET requests may be retried only under the bounded rules in `ARC-CTR-005`.
  POST and PATCH are attempted once per explicit method call.
- Connection loss during a write produces `IndeterminateWriteError` when the
  SDK cannot prove whether the API committed. It must not report ordinary
  `ServiceUnavailableError` in a way that suggests safe automatic replay.
- A nonconforming or malformed server success response raises `ProtocolError`;
  it is never coerced into a partial model.
- SDK logging and exception text must redact `value` and raw search query text.

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| SDK artifact is independently installable and has no API/SQLite dependency | Clean container wheel installation and dependency/SBOM inspection | Future SDK completion evidence |
| Host application toolchains are unnecessary | SDK build/test/use performed from a clean Docker-only host through declared targets | Required by `ARC-CTR-009` |
| CLI consumes the exact tested wheel | Build provenance and wheel hash comparison across SDK/test/CLI stages | Future build evidence |
| Every method conforms to the HTTP contract | Mock transport contract tests plus live API matrix | Required by `ARC-CTR-009` |
| Errors and indeterminate writes retain precise meaning | Fault-injected transport/status tests | Future SDK evidence |
| Public API remains compatible within a major version | Export snapshot, type-check fixtures, and prior-client conformance | Future SDK release evidence |

Changes require SDK owner review and project architecture authority. Any
change to a server-facing method must be reviewed against the HTTP, search,
versioning, CLI, and conformance records.

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined the independent synchronous Python SDK boundary | User-authorized best-judgment architecture completion |
| 2026-11-10 | Made SDK build, test, and supported consumption container-only while preserving the wheel as an independent artifact | User's explicit full-Dockerization/no-host-services instruction |

