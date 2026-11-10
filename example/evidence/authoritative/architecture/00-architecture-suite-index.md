# Example record application architecture

**Suite ID:** `ARC-SUITE-001`  
**Revision:** `2.0.1`  
**Status:** Accepted  
**Owner and accepting authority:** User, project authority  
**Technical author:** Codex, using the User-authorized best-judgment method  
**Effective date:** 2026-11-10  
**Primary source:** [`RZN-001`](../../non-authoritative/realizations/v0.0/RZN-001-example-record-application.md)  
**Authority record:** [`AUTH-EX-001`](01-accepted-architecture-baseline.md)  
**Supersedes:** `ARC-SUITE-001@2.0.0`, preserved at Git commit `5f0c325`; revision `2.0.0` superseded [`ARC-SUITE-001@1.0.0`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)  

## Purpose and standing

This suite is the binding architecture for the example record application. It
turns the requested outcome captured by `RZN-001` into accepted project-level
boundaries, contracts, decisions, and conformance obligations. The realization
remains non-authoritative source material; this suite owns the accepted
interpretation.

The User explicitly requested that the resulting suite be authoritative and
invariant evidence and subsequently authorized Codex to complete it using best
judgment. The exact scope and effect of that authority are preserved in
[`ARC-AUT-001`](02-authority-and-source-disposition.md).

The User subsequently required a fully Dockerized result and explicitly
prohibited installing application services and toolchains on the host. That
instruction creates revision `2.0.0`; the superseded native-runtime deployment
claims are retained in [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md).

The User then explicitly instructed Codex to reconcile the architecture,
security-policy, and `RZN-001` files in place according to the recorded
reconciliation findings. That instruction creates patch revision `2.0.1`.
The patch makes the already-binding NIST and HIPAA security policies and their
data/use limits explicit in this suite; it does not change the v2 component
graph, public contracts, runtime behavior, or product-completion status.

This suite specifies what future products must do. It does **not** claim that
the API, SDK, CLI, web application, database, tests, release, or operational
environment already exists. It does not accept an initiative or authorize
implementation. Product work still requires separately governed, narrowly
scoped initiatives under the
[Codex invariant suite](../LLM/00_Codex_Invariant_Suite_Index.md).

## Normative language

`Must`, `must not`, `required`, and `may only` are binding. `Should` identifies
the expected design unless a later accepted architecture revision, still
conforming to every applicable security policy, records a compatible reason to
differ. `May` grants permission only within the stated
boundary. Examples are non-normative unless a record labels them as a required
conformance vector.

When records appear to disagree, apply them in this order:

1. the project evidence protocol and any explicit accepted revision;
2. the applicable accepted NIST and HIPAA security-policy invariants for
   security, permitted data/use, safeguards, review, and evidence;
3. [`AUTH-EX-001`](01-accepted-architecture-baseline.md) for technical system
   shape inside those policy limits;
4. the most narrowly applicable accepted contract or decision in this suite;
5. a broader boundary record; and
6. explanatory text and examples.

An apparent contradiction is not resolved by this order alone. It must be
recorded and reconciled through the invariant-conflict process.

## Applicable security invariants

The following accepted suites are the primary security invariants that guide
this architecture and every future product under it:

- [`SEC-NIST-SUITE-001@1.0.1`](../security/NIST/00-nist-security-policy-suite-index.md)
  defines the limited NIST-aligned future-development security baseline; and
- [`SEC-HIPAA-SUITE-001@1.0.1`](../security/HIPPA/00-hipaa-security-policy-suite-index.md)
  defines the limited HIPAA-aligned prospective policy and regulated-use gate.

This architecture owns the technical description of system shape, components,
interfaces, and state behavior only inside the security-policy boundary. The
security suites remain primary for security, permitted data/use, safeguards,
review, and evidence, and this architecture must conform to them—not the other
way around. Neither peer security suite silently weakens the other; future
work must satisfy both, and the stricter compatible gate controls the bounded
claim. If a technical architecture statement cannot satisfy an applicable
policy, affected work stops and the architecture requires an explicitly
accepted successor; the policy is not edited to fit the architecture.

## Architectural shape

```text
Host browser -- http://127.0.0.1:HOST_PORT -- Docker port publication
                                                     |
                                                     v
                              +---------------- record-api container
                              |                    |       |
record-cli container -- SDK --+                    |       +-- embedded web assets
                                                   v
                                      record-data named volume

record-maintenance container -- offline/exclusive --+
        `-- record-backups named volume; no network
```

- Docker Compose is the only supported application runtime. The host installs
  Docker/Compose and a browser, not Python, SDK, CLI, SQLite, Node, API, web,
  migration, maintenance, or test services/toolchains.
- The API container is the only normal runtime component permitted to open the
  live SQLite database. The networkless maintenance container may mount it only
  while the API is stopped.
- The one-shot CLI container uses its installed Python SDK over the private
  Compose network; it never mounts or opens SQLite.
- The browser application uses the versioned HTTP API directly from the same
  host-loopback origin; its built assets are embedded in the API image.
- CLI and browser use the identical `/api/v1` paths, methods,
  representations, problems, search/navigation behavior, and API version;
  private-DNS versus host-loopback origin does not create a second API.
- Every surface consumes the same record, search, navigation, error, and
  concurrency semantics owned by this suite.
- The API listens on the private container network, while Compose publishes it
  only to host `127.0.0.1`. A network-accessible or multi-user deployment
  requires an explicit successor decision.

## Suggested reading order and record catalog

Filenames are intentionally numbered. Read them in ascending order: authority
and source interpretation first, then the overall boundary and durable choices,
then each domain/component boundary beside its detailed contract, and finally
operations and conformance. The sequence is continuous from `00` through `24`.

| Order | ID | Record | Why it appears here |
|---:|---|---|---|
| `00` | `ARC-SUITE-001` | **This index** | Establishes standing, architecture shape, navigation, and change control |
| `01` | `AUTH-EX-001` | [Accepted architecture baseline](01-accepted-architecture-baseline.md) | Fixes binding scope, top-level claims, source standing, and authority |
| `02` | `ARC-AUT-001` | [Authority and source disposition](02-authority-and-source-disposition.md) | Preserves the exact authorization and resolves `RZN-001-Q01` through `Q17` |
| `03` | `ARC-BND-001` | [Record platform boundary](03-record-platform-boundary.md) | Defines the whole system, actors, state authority, and exclusions |
| `04` | `ADR-001` | [API-exclusive persistence](04-ADR-001-api-exclusive-persistence.md) | Selects the central component topology before component detail |
| `05` | `ADR-002` | [Identity, order, and concurrency](05-ADR-002-identity-order-and-concurrency.md) | Selects core metadata that later domain/storage contracts consume |
| `06` | `ADR-003` | [Search execution semantics](06-ADR-003-search-execution-semantics.md) | Selects the consistent matching/safety model |
| `07` | `ADR-004` | [Container-only deployment trust model](07-ADR-004-container-only-deployment-trust-model.md) | Makes Compose mandatory and prohibits host application/service installs |
| `08` | `ADR-005` | [Normative containerized technology stack](08-ADR-005-containerized-technology-stack.md) | Selects compatible implementation and OCI build/runtime families |
| `09` | `ADR-006` | [Contract versioning and feedback](09-ADR-006-contract-versioning-and-feedback.md) | Defines how all later records/products evolve |
| `10` | `ADR-007` | [Product and delivery decomposition](10-ADR-007-product-and-delivery-decomposition.md) | Defines narrow delivery units and dependency order |
| `11` | `ARC-CTR-001` | [Record domain contract](11-record-domain-contract.md) | Defines the shared public record before transport/storage/client detail |
| `12` | `ARC-BND-002` | [API service boundary](12-api-service-boundary.md) | Defines the component that owns domain execution and live state access |
| `13` | `ARC-CTR-002` | [Record HTTP contract](13-record-http-contract.md) | Defines create/retrieve/update and shared HTTP/error semantics |
| `14` | `ARC-CTR-003` | [Search and navigation contract](14-search-navigation-contract.md) | Completes the API query, paging, and neighbor surface |
| `15` | `ARC-BND-003` | [SQLite store boundary](15-sqlite-store-boundary.md) | Defines durable-state ownership and failure boundary |
| `16` | `ARC-CTR-004` | [SQLite persistence contract](16-sqlite-persistence-contract.md) | Defines schema, transactions, migration, backup, and restore |
| `17` | `ARC-BND-004` | [Python SDK boundary](17-python-sdk-boundary.md) | Defines the typed client component and exclusions |
| `18` | `ARC-CTR-005` | [Python SDK contract](18-python-sdk-contract.md) | Defines public SDK models, methods, retries, errors, and compatibility |
| `19` | `ARC-BND-005` | [CLI boundary](19-cli-boundary.md) | Defines the independently versioned one-shot CLI image |
| `20` | `ARC-CTR-006` | [CLI interaction contract](20-cli-interaction-contract.md) | Defines commands, streams, output, exit codes, and configuration |
| `21` | `ARC-BND-006` | [Web application boundary](21-web-application-boundary.md) | Defines browser state ownership and exclusions |
| `22` | `ARC-CTR-007` | [Web interaction contract](22-web-interaction-contract.md) | Defines flows, accessibility, conflicts, races, and browser security |
| `23` | `ARC-CTR-008` | [Operations and security contract](23-operations-security-contract.md) | Defines executable local deployment, observability, and recovery controls |
| `24` | `ARC-CTR-009` | [Conformance contract](24-conformance-contract.md) | Ends with the cross-record test vectors and delivery gates |

## Capability ownership

| Capability | Normative owner | Realizing surfaces |
|---|---|---|
| Record identity and field rules | `ARC-CTR-001` | API, SDK, CLI, web, SQLite constraints |
| Create, retrieve, and update | `ARC-CTR-002` | API; SDK/CLI/web as consumers |
| Exact, prefix, suffix, contains, and regex search | `ARC-CTR-003` | API only; all clients consume results |
| Next and previous navigation | `ARC-CTR-003` | API only; all clients present results |
| Durable storage and recovery | `ARC-CTR-004` | SQLite adapter owned by the API service |
| Client transport behavior | `ARC-CTR-005` | Python SDK and CLI |
| Human command behavior | `ARC-CTR-006` | CLI |
| Browser interaction behavior | `ARC-CTR-007` | Web application |
| Deployment and operational controls | `ARC-CTR-008` | Compose project, OCI images, containers, named volumes, and operator procedures |
| Proof of conformance | `ARC-CTR-009` | Future product initiatives and their completion evidence |

## Explicit exclusions

The v2 architecture excludes deletion, undelete, bulk mutation, record-level
import/export, history/audit timelines, user accounts, roles, remote multi-user
access, actual or possible ePHI, regulated production or clinical use, shared
workstation identities, third-party record processing, offline writes,
synchronization between databases, plug-in fields, binary values, arbitrary
query composition, native-host application services, host-installed
SDK/CLI/database/build toolchains, host bind-mounted live SQLite, and
non-Compose runtime orchestration. Their absence is intentional; an
implementation must not add them as undocumented convenience features.
Streaming an opaque validated backup artifact under `ARC-CTR-008` is recovery,
not a record import/export capability.

## Reconciliation revision record

- **Authority:** The User's 2026-11-10 instruction to reconcile the named
  architecture, security-policy, and v0 realization files in place according
  to `REC-RZN-001-001`.
- **Reason:** Make the already-binding cross-suite ownership, permitted data
  profile, successor triggers, and future-consumer rules explicit at every
  source that owns them.
- **Affected scope:** Architecture standing, `RZN-001` disposition, operations
  and conformance gates, both security suites, and their future consumers.
- **Effective point:** The Git commit carrying the coordinated `2.0.1`,
  `1.0.1`, and realization-note edits.
- **Compatibility and migration:** No API, schema, component, Compose,
  persistence, SDK, CLI, browser, backup, or product behavior changes. No data
  migration is required. Future specifications and claims must cite the patch
  revisions and the already-applicable security gates.
- **Successor relationship:** `ARC-SUITE-001@2.0.1` succeeds `2.0.0` only for
  cross-source reconciliation. Git commit `5f0c325` preserves the complete
  predecessor; revision `1.0.0` remains preserved by `ARC-REV-001`.

## Change control

Every active root record in this directory is accepted invariant evidence at
revision `2.0.1`. Superseded history below `revisions/` is immutable evidence
but not active architecture. The prior deployment baseline is preserved by
`ARC-REV-001`. A change
requires an explicit instruction from the User or a later
named project authority, an impact review of all linked records, a new revision
entry or successor record, compatibility and migration consequences, and
reconciliation with every consuming initiative or product. Historical
accepted meaning must remain recoverable from Git and explicit revision or
supersession links.

Implementation evidence may motivate a change but cannot silently revise this
suite. A discovered contradiction must be recorded in the
[invariant conflict register](../LLM/03_Codex_Invariant_Conflict_Register.md)
before affected delivery continues.

