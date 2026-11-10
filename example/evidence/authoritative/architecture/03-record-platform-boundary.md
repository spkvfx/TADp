# Example record platform system boundary

**Architecture ID:** `ARC-BND-001`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Owner:** User, project authority  
**Last reviewed:** 2026-11-10  
**Supersedes:** Native-host boundary preserved in [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)  
**Related records:** [`AUTH-EX-001`](01-accepted-architecture-baseline.md), [`ADR-001`](04-ADR-001-api-exclusive-persistence.md), [`ADR-004`](07-ADR-004-container-only-deployment-trust-model.md), [`ADR-007`](10-ADR-007-product-and-delivery-decomposition.md)  

## Boundary statement

The example record platform is one Docker Compose application comprising
accepted architecture/contracts, pinned OCI build/runtime artifacts, an API
container with embedded web assets, a one-shot CLI container with the Python
SDK installed, a networkless one-shot maintenance container, a private bridge
network, and separate Docker named volumes for the live SQLite store and
backups. Together they provide create, retrieve, update, browse, search, next,
and previous behavior for the accepted three-field record. The host boundary
contains only Docker Engine/Desktop with Compose, a browser, operator-selected
host port/configuration values, and explicitly exported backup artifacts. No
application service, Python/Node/database runtime, SDK, CLI, migration tool, or
test tool is installed on the host as a supported path.

## Compose component graph

| Component | Lifecycle | Network | Volume access | Owned outcome |
|---|---|---|---|---|
| `record-api` | Long-running, one replica | Private `record-net`; port 8000 published only to host `127.0.0.1` | `record-data` read-write; no backup volume during normal serving | API/domain/search, SQLite adapter, health, static web assets |
| `record-cli` | One-shot `docker compose run --rm` | Private `record-net` only | None | Human/JSON CLI through image-installed public SDK |
| `record-maintenance` | One-shot, API stopped | `network_mode: none` | `record-data` and `record-backups` read-write only for named command | Initialize/check/migrate/backup/restore/export/import validation |
| `record-test` | One-shot profile, isolated test project | Test-only private network | Disposable test volumes only | Containerized unit/contract/integration/e2e evidence; never live state |
| Host browser | User agent, not a service | Host loopback public origin | None | Accessible web interaction |
| Build stages | Ephemeral BuildKit execution | Dependency-fetch network only when declared | Build cache/artifact outputs; never live volumes | Compile web, build wheels/images, run static/unit checks |

Only `record-api`, `record-cli`, and the browser participate in normal user
operation. Maintenance and test profiles are not started by default. Build
containers and tests cannot attach to `record-data`.

## Actors and intended outcome

| Actor | Permitted interaction | Expected outcome |
|---|---|---|
| Local browser user | Open `http://127.0.0.1:${RECORDS_HOST_PORT}/app/` | View immutable IDs; create, edit, search, and navigate with accessible feedback |
| Local CLI user | Run `docker compose run --rm record-cli ...` | Perform the same capabilities without host Python/SDK/CLI installation |
| Python integrator | Build/run a declared developer container using the published SDK wheel or SDK image stage | Consume `/api/v1` through typed models without mounting state |
| Local operator | Use Docker Compose and one-shot maintenance commands | Start/stop/inspect/backup/restore one recoverable instance without host SQLite tools |
| Product implementer | Build and test through pinned container targets under an accepted initiative | Produce separately verifiable OCI/package/web artifacts |

## Responsibilities

| Responsibility | Boundary owner | Explicitly outside this boundary |
|---|---|---|
| Define record, API, search, navigation, error, deployment, and compatibility meaning | This accepted architecture suite | Product-local reinterpretation or generated configuration as authority |
| Orchestrate normal runtime | Reviewed `compose.yaml` plus pinned release override/digests | Native service managers, host scripts that start application runtimes, or Kubernetes |
| Validate and execute record commands/queries | `record-api` application layers | CLI, browser, SDK, Compose, or direct SQL business rules |
| Persist the live record set | SQLite inside `record-api` on `record-data` | Host paths, bind mounts, CLI/web/SDK/test containers, or backup volume |
| Perform storage maintenance | `record-maintenance` while API is proved stopped | Concurrent second database owner or ad hoc host SQLite |
| Present Python/CLI/browser access | SDK artifact/developer image, `record-cli`, and embedded web assets | Host-installed application tools, user accounts, remote collaboration, plug-ins |
| Build/test/package | Docker BuildKit and declared test images | Required host Python/Node/pip/npm/pytest/browser automation services |
| Prove product conformance | Future governed initiatives | Architecture detail or successful image build treated as completion proof |

## Inputs and outputs

| Direction | Counterparty | Interface or artifact | Validated by | Compatibility rule |
|---|---|---|---|---|
| Inbound | Browser user | Same-origin web form actions through host loopback publication | Browser adapter then API | UI cannot accept or reinterpret data the API rejects |
| Inbound | CLI user | Compose command followed by CLI args or explicitly selected stdin; host files use redirection, never a mount | Compose service contract, CLI parser, SDK, API | Host-facing Compose invocation and container entrypoint follow CLI major version |
| Inbound | Python integrator | SDK calls from an approved container image/network | SDK models then API | SDK semantic version plus API `/api/v1` compatibility |
| Inbound | Local operator | `.env`/Compose variables and maintenance subcommands | Compose preflight, container startup, maintenance guard | Unknown/unsafe settings and simultaneous API/maintenance fail closed |
| Inbound | Image registry/build context | Pinned base/application artifacts and source | BuildKit, lock/hash/provenance policies | Release uses immutable digests and declared platforms |
| Outbound | Browser/CLI/SDK | Versioned JSON/resources/problems | API models and consumer decoding | `/api/v1` and client compatibility rules |
| Outbound | Local operator | Container health/status/logs, image digests, backup/export artifacts, exit status | Operations/maintenance contracts | Logs exclude values/raw searches; exports are explicit artifacts |
| Outbound | Future initiatives | Architecture IDs, image/service/volume contracts, verification vectors | Evidence/scope review | Precise citations; no copied/narrowed authority |

## State and authority

| State or decision | System of record | Write authority | Recovery or reconciliation rule |
|---|---|---|---|
| Accepted architecture meaning | Active root records at revision `2.0.1` | User/later named authority through explicit revision | Preserve predecessor through Git/explicit revision records and reconcile consumers |
| Runtime topology | Reviewed Compose model plus pinned release image digests | Governing delivery initiative/release owner | Render/inspect exact effective config; generated output cannot override source |
| Live records/internal metadata | SQLite file in `record-data` named volume | `record-api`; `record-maintenance` only while API stopped | Validate/restore through maintenance container; never merge databases |
| Backups | `record-backups` named volume and explicitly exported backup artifacts | Networkless maintenance command | Validate hashes/schema before restore/export; preserve prior live volume |
| Browser/CLI/SDK transient state | Owning browser/container process memory | Owning client | Discard with process/container; refetch authority after failure |
| Images/wheels/web bundle | Immutable registry/artifact digest | Containerized build/release process | Rebuild from pinned inputs; verify digest/provenance and architecture revision |
| Logs | Docker logging driver/operator destination | Containers emit safe structured events | Diagnostic only; never reconstruct records from logs |

## End-to-end invariants

- Docker Compose is the only supported runtime/orchestration interface. A
  native host API, host `recordctl`, host SDK/Python, host SQLite, or host web
  service is nonconforming even if behavior appears correct.
- The host publishes exactly one application port on IPv4 loopback. The API
  binds `0.0.0.0:8000` only inside the private container network.
- There is one `record-api` replica and one live SQLite database per Compose
  project. Scaling the API above one is prohibited.
- `record-data` is a Docker named volume, never a host bind mount. Normal CLI,
  web, SDK, build, and test containers never mount it.
- `record-maintenance` may mount live data only when the API container is
  stopped and its instance lock is absent; it has no network.
- A record is successful only after the API transaction commits. Container
  exit, logs, UI/SDK objects, or HTTP bytes before commit are not authority.
- Every client-visible record passes `ARC-CTR-001`; every query/neighbor is
  computed by the API; no container implements an alternate state authority.
- Released runtime containers run non-root/read-only with dropped capabilities,
  bounded resources, no Docker socket, no host PID/IPC/network mode, and only
  declared mounts/network.
- An unavailable API makes browser/SDK/CLI operations unavailable. No client
  starts a second embedded service or opens state directly.
- CLI and web use the same `/api/v1` routes and wire semantics. The browser's
  host-loopback origin and CLI's private-DNS origin may differ, but neither
  consumer has an alternate route set, gateway, or product-specific API.

## Failure boundaries

| Failure | Containment | Required externally visible behavior | Recovery owner |
|---|---|---|---|
| Docker daemon/Compose unavailable | Host prerequisite boundary | No application starts; clear prerequisite error; no native fallback | Local operator |
| Image pull/build/digest/platform failure | Build/release/start boundary | No partially trusted runtime; retain previous images/volumes | Release owner/operator |
| Host port collision or unsafe publication | Compose preflight/start | Fail start; never select arbitrary port or wildcard silently | Local operator |
| API unhealthy/unavailable | Container HTTP/health boundary | CLI/browser report unavailable; no direct-volume fallback | Operator/API owner |
| CLI one-shot failure | CLI container boundary | Stable stdout/stderr/exit; API/data unaffected except proven commit | User |
| API and maintenance overlap | Instance-lock/container-state guard | Maintenance refuses before DB mutation | Operator |
| Named-volume permission/full/corruption | SQLite/container storage boundary | No false success; readiness unhealthy; use maintenance/recovery | Operator/persistence owner |
| Stale edit or invalid/over-budget query | API domain/query boundary | Existing stable conflict/search response; no partial write/page | User/API |
| Backup/export/restore failure | Maintenance/explicit artifact boundary | Live volume preserved; candidate quarantined; no success claim | Operator |

## Verification and change control

| Claim | Verification | Evidence location |
|---|---|---|
| Host has no application service/toolchain prerequisite | Clean-host inventory followed by build/start/use/test/maintenance through Docker only | Required by [`ARC-CTR-009`](24-conformance-contract.md) |
| Effective Compose graph matches this boundary | `docker compose config` inspection plus mount/network/port/security assertions | Future operations evidence |
| Every executable surface shares one API/state authority and CLI/web share `/api/v1` | Image dependency/mount/network/route scan and cross-origin end-to-end vectors | Future product evidence |
| API/maintenance mutual exclusion and volume recovery are safe | Competing-container, backup/export/restore, corruption/failure tests | Future persistence evidence |
| Image artifacts are immutable and constrained | Digest/SBOM/provenance/config/runtime inspection | Future release evidence |

Changes require User/later named architecture authority and synchronized review
of the predecessor record, Compose/image contracts, API/clients, persistence,
operations, conformance, initiatives, products, and migration/recovery effects.

