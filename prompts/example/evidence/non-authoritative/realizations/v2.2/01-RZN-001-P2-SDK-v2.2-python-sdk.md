# Independently versioned Python SDK artifact

**Realization ID:** `RZN-001-P2-SDK-N01`  
**Suite:** [`RZN-001-P2-SDK-SUITE@v2.2`](00-RZN-001-P2-SDK-suite-index.md)  
**Suite version:** `v2.2`  
**Status:** Recorded; invariant-bounded proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation and [`RZN-001`](../v0.0/RZN-001-example-record-application.md)  
**Historical product lineage:** SDK portion of `RZN-001-P2-SDK-API`  
**Accepted delivery-unit alignment:** `D4 Python SDK artifact`  
**Related initiative or proposal:** None created  

> **Evidence standing:** This note records a candidate SDK outcome. It is not
> an accepted Python API, built wheel, compatibility promise, test result,
> implementation authorization, product release, or completion claim. The
> cited architecture owns all accepted SDK meaning.

## Realization

There is a bounded opportunity to deliver one independently versioned,
synchronous Python SDK wheel that converts typed calls into the accepted
`/api/v1` wire contract, converts exact responses and problems into immutable
models and stable exceptions, preserves write uncertainty and concurrency,
and is built, tested, and consumed only through declared containers.

The SDK would make D3 behavior usable by Python consumers and the future D5
CLI without owning the API, SQLite, Compose lifecycle, interactive command
surface, browser interface, or record/search semantics.

## Narrow outcome and beneficiary

| Dimension | Candidate record |
|---|---|
| Outcome | One hash-identified `example-records-sdk` wheel with the accepted public synchronous client contract and exact containerized build/test/consumption evidence |
| Primary beneficiaries | D5 CLI implementers, approved containerized Python integrators, API compatibility reviewers, and SDK release owners |
| Authority boundary | Typed client encoding/decoding, lifecycle, retries, exceptions, packaging, and SDK compatibility only |
| Output class | Python distribution metadata, public package, models, client, transport adapter, exception hierarchy, wheel, SDK documentation/examples, and D4 evidence |
| Independent review claim | The exact wheel conforms to the public SDK and live `/api/v1` contracts across the claimed pinned Linux/Python matrix |
| Explicit non-claim | No server, SQLite, API completion, CLI process, browser behavior, host Python install, async API, or remote/regulated-use support |

## Context and evidence

| Question | Record |
|---|---|
| What was requested? | `RZN-001` requested an SDK described by Product 1 and implemented with Product 2's API, but left language, packaging, public surface, and consumer behavior open. |
| What is now authoritative? | `ARC-BND-004` and `ARC-CTR-005` fix a synchronous Python/Pydantic/HTTPX wheel, public symbols, models, methods, retries, errors, compatibility, and container-only supported consumption. |
| Why separate it from the API? | `ADR-007` records independent packaging, consumers, blockers, live conformance, compatibility, and completion for D4 versus D3. |
| What is current status? | `ARC-CTR-009` records no supplied D4 implementation or conformance evidence. |
| What remains proposal-level? | Exact source/product destinations, dependency patch locks, documentation placement, test implementation, release owner, evidence storage, and any further narrow split justified by the cohesion assessment. |

## Binding source inventory

| Source | Exact relevance |
|---|---|
| [`ARC-BND-004`](../../../authoritative/architecture/17-python-sdk-boundary.md) | Wheel/package boundary, responsibilities, dependencies, state, invariants, failure, and containerized use. |
| [`ARC-CTR-005`](../../../authoritative/architecture/18-python-sdk-contract.md) | Exact public namespace, immutable models, constructor, methods, retries, exceptions, compatibility, and verification. |
| [`ARC-CTR-001`](../../../authoritative/architecture/11-record-domain-contract.md) | Canonical record and patch validation the SDK may mirror for feedback without becoming authoritative. |
| [`ARC-CTR-002`](../../../authoritative/architecture/13-record-http-contract.md) | Exact create/get/update encoding, headers, ETags, media, problems, and write uncertainty. |
| [`ARC-CTR-003`](../../../authoritative/architecture/14-search-navigation-contract.md) | Exact search spec, cursor, ceiling, paging, neighbor, and boundary wire meaning. |
| [`ADR-001`](../../../authoritative/architecture/04-ADR-001-api-exclusive-persistence.md) | SDK communicates only through `/api/v1`; no SQLite or server fallback. |
| [`ADR-005`](../../../authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | Python/Pydantic/HTTPX selection, wheel build stage, exact artifact copying, and no host toolchain. |
| [`ADR-006`](../../../authoritative/architecture/09-ADR-006-contract-versioning-and-feedback.md) | SDK semantic identity, compatibility change classes, and feedback governance. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | D4 predecessor evidence and independent claim. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | D4 gate, `SDK-*` vectors, applicable cross-contract vectors, and exact evidence schema. |
| [`SEC-NIST-POL-001`](../../../authoritative/security/NIST/01-demonstrator-security-policy.md) / [`SEC-NIST-VER-001`](../../../authoritative/security/NIST/03-future-development-assurance.md) | Security, safe input/output, release integrity, vulnerability, and assurance requirements. |
| [`SEC-HIPAA-POL-001`](../../../authoritative/security/HIPPA/02-prospective-security-policy.md) / [`SEC-HIPAA-DEV-001`](../../../authoritative/security/HIPPA/04-future-development-and-evidence-standard.md) | Permitted data, minimum handling, diagnostics, build evidence, external-service, and claim gates. |

## Candidate package boundary

| Concern | Accepted candidate behavior |
|---|---|
| Distribution/import | Distribution `example-records-sdk`; package `example_records_sdk`; explicit root export allowlist |
| Runtime | Synchronous Python; Pydantic v2 strict immutable public models; HTTPX transport |
| Supported matrix | Wheel claims only container-tested CPython `>=3.12,<3.15` on pinned Linux environments; released consumer images use the selected Python 3.13/base family |
| Dependencies | Pydantic v2 and HTTPX compatible ranges only; no FastAPI, Uvicorn, SQLite driver, API implementation, CLI, or web dependency |
| Build | PEP 517/518 wheel produced once in `sdk-wheel`, hashed, tested, and copied unchanged into consumer/test images |
| Import behavior | No network, file, environment, logging, server start, or global-client initialization side effect |
| Host boundary | No supported host Python, pip, pipx, virtual environment, or SDK installation; integrator use occurs in declared containers |

## Candidate public namespace

The architecture fixes these v1 root exports:

```text
RecordClient
Record
VersionedRecord
RecordPatch
RecordField
MatchMode
SearchSpec
RecordPage
Direction
Boundary
NeighborResult
ProblemIssue
RecordSdkError
ClientValidationError
ApiProblemError
InvalidSearchError
RecordNotFoundError
RevisionConflictError
CapacityExceededError
ServiceUnavailableError
IndeterminateWriteError
ProtocolError
```

HTTPX/Pydantic implementation objects, generated schemas, transport helpers,
internal module names, and underscore-prefixed symbols are not candidate
compatibility promises.

## Candidate model boundary

| Model | Candidate SDK responsibility | Boundary preserved |
|---|---|---|
| `Record` | Strict immutable canonical `id`, `name`, `value` | Server remains final domain authority; a response needing coercion/normalization is a protocol error. |
| `VersionedRecord` | Record plus opaque ETag and request ID | Revision is not a public record field. |
| `RecordPatch` | Presence-aware name/value, at least one, no ID/null/extra | Local validation improves feedback; it never proves server acceptance. |
| `RecordField`, `MatchMode`, `Direction`, `Boundary` | Exact lowercase wire enums | New/changed tokens require compatibility review. |
| `SearchSpec` | One field/mode/query triple with accepted local limits | SDK never evaluates membership or regex. |
| `RecordPage` | Ordered immutable records, opaque cursor, ceiling, request ID | SDK never resorts/refilters or decodes cursor meaning. |
| `NeighborResult` | Exactly record or boundary plus ceiling | Neighbor record retains its ETag; SDK never computes adjacency. |
| `ProblemIssue` | Validated safe path/code/message from API problem | SDK does not branch on or promise English message text. |

## Candidate client lifecycle and configuration

The candidate constructor is the exact architecture-owned synchronous shape:

```python
RecordClient(
    base_url: str,
    *,
    timeout: float = 5.0,
    transport: httpx.BaseTransport | None = None,
    user_agent_suffix: str | None = None,
) -> RecordClient
```

- The supported live base URL is exactly `http://record-api:8000`; arbitrary
  hosts, loopback, host gateway, credentials, queries/fragments, container IP,
  HTTPS, and discovery are rejected for v2.
- Mock transport injection exists for testing without authorizing another live
  origin or wire contract.
- Timeout is finite within `0.1..60.0` seconds.
- One explicit closeable context-managed HTTPX client owns its pool; close is
  idempotent; use after close fails locally.
- No module-global mutable client or implicit environment configuration exists.
- Import/construction makes no network call; the first explicit method is the
  first possible request.
- Thread sharing is not promised; consumers use separate instances unless a
  future evidence-backed release changes that contract.

## Candidate method surface

| Method | Candidate responsibility | Prohibited behavior |
|---|---|---|
| `create_record` | Send one strict POST and return one `VersionedRecord` | ID generation, deduplication search, automatic retry, or false rollback/success |
| `get_record` | Canonical ID validation and exact GET decoding | Alternate ID canonicalization or cached authority |
| `update_record` | One PATCH with caller-provided current ETag and strict patch | Refetch/merge/force/retry or conflict resolution |
| `search_page` | Encode optional `SearchSpec`, limit, opaque cursor and decode ordered page | Client membership, sorting, regex, or cursor mutation |
| `iter_records` | Lazily follow exact cursors, detect repetition, honor page/max bound | Full preload, hidden snapshot restart, cursor invention |
| `neighbor` | Encode exact context/ceiling and decode record or boundary | Local adjacency, wrapping, context guessing |

No raw-request escape hatch, delete, SQL, ID allocation, arbitrary route,
async API, service start, offline cache, or local database method is a
candidate public capability.

## Candidate retry and write-truth boundary

| Operation class | Accepted automatic retry | Candidate outcome on uncertainty |
|---|---:|---|
| `get_record`, `search_page`, `neighbor` | At most two retries, three attempts total, only for accepted pre-response/connect/timeout or qualifying `502/503/504` conditions | Exhaustion becomes a typed unavailable result with safe context. |
| Cursor GET through `iter_records` | Same bounded read policy using identical cursor/request | Repeated cursor is a protocol failure, not an infinite loop. |
| `create_record` | Never | Loss after dispatch that cannot prove outcome becomes `IndeterminateWriteError`. |
| `update_record` | Never | Conditional semantics do not authorize replay; unprovable outcome remains indeterminate. |

Read retry delays, bounded jitter, `Retry-After`, remaining-time budget, and
logical request ID retention must follow `ARC-CTR-005`. A write exception must
not imply that retry is safe merely because the client did not receive a
response.

## Candidate exception boundary

| Exception | Candidate meaning |
|---|---|
| `ClientValidationError` | Constructor, method, or model input rejected before HTTP |
| `InvalidSearchError` | Valid API problem for invalid search, regex, or cursor |
| `RecordNotFoundError` | Canonical requested ID absent |
| `RevisionConflictError` | Expected ETag stale; no automatic server-record merge |
| `CapacityExceededError` | Create blocked at accepted store capacity |
| `ServiceUnavailableError` | Exhausted safe-read transport path or typed server/store/search unavailability |
| `IndeterminateWriteError` | POST/PATCH dispatched and final state cannot be proved |
| `ApiProblemError` | Valid problem not mapped to a narrower stable type |
| `ProtocolError` | Malformed/nonconforming success, problem, media, ETag, or response |

All public exceptions derive from `RecordSdkError`, retain immutable safe
attributes, and omit full values and raw search text. HTTPX errors may be
causes, not the primary public contract.

## Observability and data handling

- SDK diagnostics may include safe method, route template, status, request ID,
  duration, and reason category only.
- Record `value`, full `name`, request bodies, raw query/regex, ETag, cursor,
  credentials, environment content, and transport repr are excluded from logs
  and normal exception text.
- The SDK persists no record, search, credential, cache, or retry queue to
  disk; returned models and cursors live only in caller process memory.
- Examples and fixtures use purpose-created synthetic data or the externally
  documented de-identification path, while also satisfying NIST restrictions.
- The wheel, source, build layers, documentation, test output, and evidence
  must not embed real or insufficiently classified records.

## Security-policy applicability

| SDK concern | NIST policy anchors | HIPAA policy anchors | Candidate evidence direction |
|---|---|---|---|
| Use and claims | `SEC-POL-01`, `SEC-POL-14` | `HSP-001`, `HSP-002`, `HSP-015` | Package/docs limitations, safe fixtures, no remote/ePHI/compliance claim |
| Input/output and retries | `SEC-POL-06`, `SEC-POL-07` | `HSP-006`, `HSP-007` | Strict models/decoders, malformed responses, bounded retries, indeterminate writes |
| Network/access boundary | `SEC-POL-02`, `SEC-POL-03` | `HSP-004`, `HSP-005` | Exact private base URL, no credentials, no alternate API/state path |
| Diagnostics | `SEC-POL-08` | `HSP-006`, `HSP-008` | Log/exception redaction with synthetic canaries and explicit non-audit role |
| Build/release | `SEC-POL-04`, `SEC-POL-10`, `SEC-POL-12` | `HSP-009`, `HSP-013` | Exact wheel hash, dependency/SBOM/provenance/license/vulnerability and no-data external-service evidence |
| Assurance | `SEC-POL-11` | `HSP-003`, `HSP-014` | Named owner/risk mapping, mock and live evidence, exact matrix/limitations/reviewer |
| Incident/recovery interface | `SEC-POL-13` | `HSP-012` | SDK evidence preserves transport facts and never invents transaction outcome; organizational escalation remains external |

Every policy requires an exact future applicability decision. This grouped
table creates no result or exception.

## Candidate conformance boundary

| Evidence group | Candidate D4 proof | Limitation |
|---|---|---|
| `SDK-001` | One wheel built once, exact hash reused, clean container install/import/construct/close, public export snapshot, no server/SQLite deps or import I/O | Installation alone does not prove wire behavior. |
| `SDK-002`-`004` | Every accepted success/problem and malformed response maps to exact immutable models/exceptions or `ProtocolError` | Mock transport is not live D3 interoperability. |
| `SDK-005`-`007` | Bounded read retries, no write retry, indeterminate distinction, lazy paging, repeated-cursor handling | Timing/fault seams must preserve production defaults. |
| `SDK-008` | Sensitive fixtures do not leak through logs/exceptions | One canary set does not prove absence of all privacy risk. |
| Applicable `DOM/HTTP/SRCH/NAV` | Local validation/encoding and live results match the accepted contracts | Server behavior remains D3-owned. |
| Applicable `E2E` | Exact wheel interoperates with the compatible live D3 image and later consumers | D5/D6 completion remains independent. |

The D4 gate requires mock fixtures and an accepted live D3 baseline, exact D2
container build/test identity, the claimed pinned Python matrix, public API and
dependency compatibility evidence, and all applicable NIST/HIPAA gates. The
future record must identify wheel hash, source commit, image digests, platform,
Python/Pydantic/HTTPX versions, D3 image/API identity, method, results,
limitations, dispositions, reviewer, time, and synthetic fixture manifest.
This note records no pass.

## Dependencies and handoffs

| Relationship | Required handoff | Boundary preserved |
|---|---|---|
| D1 -> D4 | Exact SDK contract/revision and derivative docs used | Documentation guides implementation but does not become behavior evidence. |
| D2 -> D4 | Exact `sdk-wheel` and test/developer build targets, pinned base/platform, provenance path | D4 does not claim D2 topology completion. |
| D3 -> D4 | Compatible live API image/version, exact `/api/v1`, problems, search/navigation, failure fixtures | SDK cannot change or compensate for a nonconforming server silently. |
| D4 -> D5 | Wheel filename/version/SHA-256, public symbols, compatible API major, exact artifact copy proof | CLI must consume the released wheel and cannot import SDK internals. |

## Risks to preserve for proposal analysis

| Risk | Consequence |
|---|---|
| SDK and API are recombined | Independent packaging, compatibility, blockers, and completion become obscured. |
| Client validation becomes authoritative | Server divergence may be hidden or valid server behavior rejected incorrectly. |
| Write transport failure maps to ordinary unavailable | Consumers may replay an operation whose commit status is unknown. |
| Generated models expose extra public symbols | Accidental API surface creates unreviewed compatibility obligations. |
| Wheel is rebuilt in CLI stage | Tested/published and consumed bytes can differ. |
| Host installation is documented as supported | The product conflicts with Compose-only architecture. |
| SDK logs raw problem or query content | Sensitive data is amplified into diagnostics/evidence. |
| Mock-only tests support a live claim | Real media, headers, routing, API version, and failure behavior remain unproved. |

## Questions that remain for a future proposal

1. Which exact repository and artifact destinations own SDK source, wheel,
   generated metadata, reference docs, examples, and evidence?
2. Which dependency patch versions and Python/platform images form the first
   supported matrix within the accepted ranges?
3. What public typing, documentation, and compatibility-diff tools run inside
   the declared D2 test path?
4. How are fault clocks/randomness/transports injected without expanding the
   public API or weakening live URL validation?
5. Who owns SDK security/risk review, vulnerability monitoring, release
   disposition, and D3 compatibility retirement?
6. Does any independently releasable documentation or adapter sub-scope
   trigger a narrower proposal while preserving one D4 wheel claim?

No answer is selected by this note.

## Candidate outcome

Containerized Python consumers receive one immutable, hash-identified SDK
wheel whose typed models, methods, errors, retries, and compatibility follow
the exact shared API contract; the wheel preserves server authority and write
uncertainty, contains no server/database path, and supplies reviewable mock and
live evidence without claiming D3, D5, D6, host installation, or regulated use.

## Suggested next step

Take no initiative action now. If later directed, prepare a D4-only proposal
from this note, name the exact compatible D2 and D3 identities, choose product
destinations, perform the mandatory scope assessment, and retain the six open
proposal questions for explicit human disposition.

## Handoff notes

A receiving proposal must cite this realization and its v2.2 suite, preserve
the accepted v2.1 API/v2.2 SDK split, map every public surface and failure path
to its authoritative contract and verification, and state precisely what the
wheel supplies to v3.0/D5 without accepting or completing the CLI.



## Version-scope migration addendum (2026-11-12)

**Version scope:** `v2.2`

**Migration authority:** [EX-VSG-DR-001](../../../../initiatives/decision-receipts/EX-VSG-DR-001-initiative-migration.md)

**Current initiative target:** [INIT-IMP-004](../../../../initiatives/v2.2/implementation/INIT-IMP-004-python-sdk/README.md)

**Exact source catalog:** [RZN-001-P2-SDK-N01](01-RZN-001-P2-SDK-v2.2-python-sdk.md)

The original headers and one-to-one allocation language remain historical evidence under the prior revision. This addendum adopts scope membership and many-target catalog capability without changing source identity, relabeling this note or promoting its non-authoritative standing. The existing target retains the same narrow Proposed claim. Future independent outcomes require their own initiative records, not necessarily another version. The initiative index owns current assignments; the historical branch and base above remain history.
