# Local operator to container platform operations and security contract

**Architecture ID:** `ARC-CTR-008`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Contract owner:** Container platform owner and project architecture authority  
**Producer:** Versioned OCI images, release Compose model, and maintenance commands  
**Consumer:** Local operator, product verification, and future release initiatives  
**Last reviewed:** 2026-11-10  
**Supersedes:** Native-runtime portions of `ARC-CTR-008@1.0.0`, preserved in [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)  

## Purpose and scope

This contract makes the local single-user, fully Dockerized trust decision
operationally enforceable. It defines host prerequisites, the effective
Compose topology, image and volume identity, configuration, lifecycle,
health, mutual exclusion, resource/security controls, logging, release
evidence, backup/restore, and failure handling.

It does not define remote/public deployment, accounts, high availability,
Kubernetes, a host-native fallback, or product-level record import/export.
Transfer of an opaque validated backup bundle is an operations capability, not
a bulk record API or user-data interchange format.

## Supported deployment profile

| Property | Binding v2 requirement |
|---|---|
| Orchestrator | Docker Compose v2 using the reviewed release `compose.yaml` and immutable release image references; no alternate orchestrator |
| Host prerequisites | Docker Engine plus Compose v2, or Docker Desktop including Compose v2; a supported browser; Git only for source-development hosts |
| Host exclusions | No host Python/pip/pipx/venv, SDK, `recordctl`, FastAPI/Uvicorn/Pydantic/HTTPX/RE2, SQLite tooling, Node/npm/TypeScript, migration, test, or application web service |
| Runtime topology | One long-lived `record-api`, disposable `record-cli`, stopped-API networkless `record-maintenance`, optional isolated `record-test`; no reverse proxy or separate web server |
| Public ingress | Container port 8000 published exactly as `127.0.0.1:${RECORDS_HOST_PORT}:8000`; no IPv6, hostname, wildcard, LAN, tunnel, proxy, or public publication |
| Internal ingress | `record-cli` and approved test consumers reach `http://record-api:8000` on private `record-net` |
| API path | Browser and CLI append the identical `/api/v1` routes and consume the same methods, representations, problems, search/navigation semantics, and API version lifecycle |
| State | Live SQLite in Compose named volume `record-data`; validated backups in separate named volume `record-backups`; no live bind mount |
| Availability | Best-effort local service; one replica/worker, no failover/SLO/zero-downtime migration claim |
| OCI targets | Released manifests declare and verify `linux/amd64` and `linux/arm64`; an untested manifest entry is not a supported target |

Minimum release-host verification covers Windows 11 x64 with Docker Desktop,
Ubuntu 24.04 LTS x86_64 with Docker Engine/Compose, a native Linux arm64 runner
for the arm64 image claim, and a Docker-Desktop-supported macOS environment
needed for the accepted Safari/manual web matrix. Exact Docker/Desktop/Compose,
kernel/VM, OS patch, and browser versions are fixed in each release evidence
record. Other hosts are unclaimed until their matrix passes.

## Effective Compose service contract

The rendered configuration, not an unrendered fragment or README example, is
the execution authority. Release verification must inspect
`docker compose config` output before starting anything.

| Service | Image/command | Network and ports | Volume authority | Lifecycle |
|---|---|---|---|---|
| `record-api` | Immutable digest-qualified `example-records-api` image; exec-form API entrypoint; one Uvicorn worker | `record-net`; internal `0.0.0.0:8000`; sole host mapping `127.0.0.1:${RECORDS_HOST_PORT}:8000` | `record-data:/var/lib/example-records` read-write; no backup volume | Long-running, exactly one replica, `restart: "no"`, health checked |
| `record-cli` | Immutable digest-qualified `example-records-cli` image; exec-form `recordctl` entrypoint | `record-net` only; no published/exposed host port | No volume or bind mount | One process per `docker compose run --rm record-cli ...`; never daemonized |
| `record-maintenance` | Same compatible API image digest or a separately identified maintenance target with identical persistence/migration resources; closed command allowlist | `network_mode: none`; no network, DNS, or port | `record-data` and `record-backups`; command opens only the required role/mode | One-shot profile, API stopped, exclusive instance lock required, `restart: "no"` |
| `record-test` | Pinned test target/image, never a release runtime image | Test-project private network only; random host port only when the test explicitly requires one | Fresh disposable test volumes only; never release/live volumes | Explicit test profile/project; one-shot; teardown after evidence capture |

There is no SDK daemon. The SDK wheel is an artifact installed into the CLI,
test, and declared developer images. There is no web service: the
container-built bundle is copied into and served by `record-api`.

### Mandatory service hardening

All runtime and maintenance services declare:

- numeric `user: "10001:10001"`, `read_only: true`, and exec-form
  entrypoint/command;
- `cap_drop: [ALL]` and `security_opt: ["no-new-privileges:true"]`;
- no `privileged`, device, Docker socket, host PID/IPC/network, extra host,
  or daemon-control access;
- a bounded `/tmp` tmpfs with `nosuid,nodev,noexec` and no other writable
  container layer;
- `pids_limit`, memory, CPU, stop-grace, and log-size controls in the
  effective Compose model; and
- no secret in an image layer, label, environment value, command line, log,
  health response, or Compose file.

The acceptance ceilings are:

| Service | CPU | Memory | PIDs | `/tmp` | Stop grace |
|---|---:|---:|---:|---:|---:|
| `record-api` | 1.0 CPU | 512 MiB | 128 | 32 MiB | 10 s |
| `record-cli` | 0.5 CPU | 256 MiB | 64 | 16 MiB | 5 s |
| `record-maintenance` | 1.0 CPU | 512 MiB | 128 | 64 MiB | 30 s |

An accepted successor may tune a ceiling only with load/fault evidence and
compatibility analysis. A platform that silently ignores a required security
or resource field does not pass the supported-host matrix.

## Network, Host, Origin, and shared-path rules

- `record-net` is an application-private bridge network. Only declared
  project services attach; arbitrary containers, external networks, and host
  network mode are prohibited.
- Docker publishes only API port 8000 to the selected IPv4 loopback host port.
  The API intentionally listens on all interfaces *inside* the container so
  private-network clients can connect; that is not authority for wildcard host
  publication.
- The API accepts the exact public Host
  `127.0.0.1:${RECORDS_HOST_PORT}` and internal Host `record-api:8000`.
  Its image-provided health command uses the internal Host. Missing, malformed,
  repeated, hostname, IP-container, alternate-port, or proxy-derived Host
  identity is rejected.
- Browser requests use exact origin
  `http://127.0.0.1:${RECORDS_HOST_PORT}`. Browser state-changing requests
  require that exact `Origin`; mismatched or `null` Origin fails before body
  processing. CORS is disabled.
- CLI/SDK containers use `http://record-api:8000`, omit Origin, and call the
  same `/api/v1` router as the web adapter. Private DNS does not authorize a
  CLI-only path or behavior.
- `Forwarded`, `X-Forwarded-*`, proxy protocol, host-gateway discovery,
  `host.docker.internal`, and container IP literals never establish request
  identity.
- The release has no outbound runtime dependency. Registry/package access is
  a declared build/pull concern, not a request-time service dependency.

The no-auth design relies on OS/Docker access plus loopback/private-network
confinement. Anyone with Docker-daemon, host administrator/root, or volume
access is inside the administrative trust boundary and can inspect/control the
application. The architecture does not claim protection against that actor.

## Volume, filesystem, and ownership rules

| State | Required placement and access |
|---|---|
| Live database | `record-data` at `/var/lib/example-records/records.sqlite3`; API read-write normally; maintenance only under exclusive stopped-API guard |
| Instance lock/WAL/SHM | Adjacent inside `record-data`; never copied independently as a backup |
| Backup artifacts | `record-backups` at `/var/lib/example-record-backups`; maintenance only; never mounted by API/CLI/web/test |
| Runtime temporary data | Bounded `/tmp` tmpfs; non-authoritative and discarded with container |
| Logs | stdout/stderr to a bounded Docker logging driver; no application log volume/file |
| Host export | Explicit validated backup bundle streamed through maintenance stdout to an operator-selected host file; never a mount of live state |

Image directories underlying the empty named-volume mount points are created
at build time with numeric ownership `10001:10001`; volume initialization and
maintenance verify ownership/mode before use. No runtime container elevates to
root to repair a volume. A mismatch fails closed and requires a reviewed
containerized recovery procedure.

The accepted Compose mounts retain Docker's empty-volume copy-up behavior
(`nocopy` omitted or explicitly false) so the image-owned mount-point metadata
seeds a new volume. A release using `nocopy: true` must instead provide and
prove an equally non-root, containerized ownership bootstrap before it can
supersede this rule; root entrypoint `chown` is not an accepted fallback.

Bind mounts, anonymous volumes, external live-state volumes, container writable
layers, NFS/SMB/cloud-sync/removable paths, and direct host volume paths are
prohibited for live state. CLI host input uses bounded stdin redirection, not a
mount. Test profiles use distinct Compose project/volume identities and must
prove they cannot resolve or mount release volumes.

## Configuration surface

The release intentionally has a narrow host configuration surface:

| Host/Compose input | Default | Validation and effect |
|---|---|---|
| `RECORDS_HOST_PORT` | `8000` | Decimal 1024-65535; fixes Docker loopback publication, public Host, and browser origin; collision/invalid value fails rather than selecting another port |
| `RECORDS_LOG_LEVEL` | `INFO` | Closed enum `DEBUG|INFO|WARNING|ERROR`; all levels retain redaction |
| `RECORDS_WORKER_THREADS` | `8` | Decimal 2-32 for bounded synchronous work; never changes Uvicorn process count |
| `RECORDS_SHUTDOWN_SECONDS` | `10` | Decimal 1-60 and not greater than the Compose stop grace |

Unknown inputs beginning `RECORDS_` or `EXAMPLE_RECORDS_` are fatal.
Compose/project name, internal bind/port, service DNS name, database/backup
paths, volume identities, API base path, image references, user, and security
controls are release-fixed, not ordinary operator variables. The application
receives validated effective values; it never reads a host config file or
auto-discovers Docker.

V2 has no application secrets, credentials, tokens, or account configuration.
Release image digests may not be replaced through an undocumented environment
override. Source development may use reviewed Compose build targets, but a
release claim uses immutable registry digests and the same effective topology.

## Image, build, and release identity

- The root BuildKit multi-stage graph produces named `sdk-wheel`,
  `web-build`, `api-runtime`, `cli-runtime`, and `test` targets under
  [`ADR-005`](08-ADR-005-containerized-technology-stack.md).
- Runtime images copy only accepted wheels, application code, migrations, web
  outputs, licenses, and runtime libraries. Compilers, Node/npm, test tools,
  source checkout, package caches, and shell mutation are absent.
- Release references are immutable digest-qualified. Each claimed platform has
  a manifest digest and passing native or explicitly qualified evidence.
- OCI labels identify product/version, source commit, architecture revision
  `2.0.0`, API/schema compatibility, build identity, licenses, and
  SBOM/provenance references. Labels are metadata, not proof by themselves.
- Dependency inputs are locked/hashes or equivalent, license/vulnerability
  reviewed, and represented in SBOMs. Material findings require explicit human
  disposition; a silent ignore or scanner absence is not acceptance.
- The exact SDK wheel and web bundle tested are copied into consumer/runtime
  images. Hash/provenance mismatch blocks release.
- Automated build, lint, unit, contract, integration, migration, recovery,
  security, and browser automation executes through BuildKit/Compose
  targets/profiles. CI hosts Docker; it does not establish a native project
  toolchain as the normative path.

## Lifecycle contract

### Preflight and first initialization

1. Verify Docker/Compose availability and record exact versions/platform.
2. Render and validate `docker compose config`; inspect effective image
   digests, one loopback port, one private network, named volumes, mounts,
   replica count, user, capabilities, root filesystem, limits, and profiles.
3. Pull immutable release images or build declared development targets.
   Verify platform, signatures/provenance policy, labels, SBOM linkage, and
   architecture/API/schema compatibility before executing application code.
4. Ensure `record-api` is stopped. For a new empty `record-data` volume run
   `docker compose run --rm record-maintenance initialize`. It acquires the
   exclusive lock, refuses nonempty/foreign state, creates schema v1, validates
   it, records safe metadata, and exits zero.
5. Start only the API with
   `docker compose up -d --wait record-api`. Docker must fail on an invalid
   or occupied host port; no automatic port/wildcard fallback is allowed.
6. Confirm Compose health, public loopback readiness, asset manifest, Host/
   Origin negatives, and one canonical domain smoke flow before normal use.

The API never initializes or migrates state during startup. A missing,
uninitialized, old, new, foreign, corrupt, or incorrectly owned database keeps
it unready or exited.

### Normal use and shutdown

- Browser entry is
  `http://127.0.0.1:${RECORDS_HOST_PORT}/app/`.
- CLI entry is `docker compose run --rm record-cli ...`; redirected stdin
  uses Compose `-T`. The service has no `depends_on` side effect that starts
  the API; an unavailable API is reported normally.
- SDK examples and developer workflows run in a declared container attached to
  `record-net` and use the same `/api/v1` path.
- Graceful stop is `docker compose stop -t 10 record-api`. It stops
  admission, drains within the accepted bound, completes or rolls back
  transactions, closes SQLite/checkpoints safely, releases the lock, and exits.
- `docker compose down` may remove containers/network after a clean stop and
  must preserve named volumes. `docker compose down -v`, `docker volume rm`,
  pruning project volumes, or deleting Docker Desktop data is destructive and
  is never part of a safe stop/update/repair instruction.

### Upgrade

1. Preserve current Compose, image digests, volume identity, schema, and health
   evidence; pull/verify successor images without starting them.
2. Stop API and prove it is not running.
3. Run `record-maintenance check` and a mandatory validated
   `record-maintenance backup`.
4. If required, run `record-maintenance migrate` with a declared source/target
   schema and image compatibility. Failure leaves API stopped and prior state
   recoverable.
5. Start the successor API, wait for readiness, and run domain/search/web/CLI
   smoke vectors. Retain old image digest and pre-migration backup until the
   release rollback window closes.

No in-place image patch, serving-time migration, automatic downgrade, or
zero-downtime update is supported.

## Maintenance mutual exclusion and commands

Every maintenance command requires both:

1. host-side confirmation that `record-api` is stopped; and
2. successful acquisition of the same exclusive instance lock used by API.

The lock is authoritative against races; host Compose state alone is
insufficient. Maintenance has no Docker socket and therefore cannot weaken
isolation to inspect/control the daemon. API startup likewise fails while a
maintenance lock is held. Commands are allowlisted and reject arbitrary shell,
SQL, Python module, path, URL, and command execution.

| Command | Mount behavior | Required result |
|---|---|---|
| `initialize` | Data read-write; backup unused | Create only a provably empty accepted store; validate; refuse overwrite |
| `check` | Data opened read-only at application level | Validate identity/schema/migrations/ownership/capacity/row decoding/`quick_check`; no mutation |
| `backup` | Data source plus backup destination | Create new generated artifact, validate, hash, sidecar, and atomic finalize; never overwrite |
| `migrate` | Data and backup read-write | Require fresh validated backup, apply ordered accepted migrations, validate, record result |
| `restore BACKUP_ID` | Backup source plus data destination | Validate source/candidate, preserve old live set, atomic switch, validate; never merge |
| `export-backup BACKUP_ID` | Backup source only | Stream a framed, hashed validated bundle to stdout; diagnostics to stderr; no live data mount/export |
| `import-backup` | Backup destination only | Read bounded framed bundle from stdin, validate before atomic acceptance; does not restore or alter live data |

Backup export/import moves an opaque recovery artifact only. It is not a
record-level import/export feature, public API route, SDK method, CLI command,
or alternate means to merge/edit records.

## Health and readiness

| Endpoint | Success | Failure | Restrictions |
|---|---|---|---|
| `GET /health/live` | `200 {"status":"ok"}` when process/event loop responds | Connection/process failure | No DB query, version/path/count; exact allowed Host; no-store |
| `GET /health/ready` | `200 {"status":"ready"}` after compatible store/lock/assets are usable | `503 {"status":"not_ready","code":"..."}` with closed safe code | No record/path/version detail; no-store |

The image supplies a minimal health executable that performs an HTTP request
with the internal Host; no curl/wget/package manager is added solely for
health. Readiness becomes false for persistent database I/O/read-only/full/
corruption, lost lock, incompatible schema, or required-asset failure. A user
validation/not-found/conflict or one recovered busy result does not change
readiness.

Health signals do not prove end-to-end correctness and are not product data.
They receive request IDs, accepted security headers, GET/HEAD only, and never
trigger initialization, migration, checkpoint, or record mutation.

## HTTP and browser security

- Enforce exact Host and Origin rules above before body parsing or command
  dispatch. Do not trust proxy headers or derive identity from source IP alone.
- Emit no permissive CORS or credential headers. There are no cookies, bearer
  tokens, Basic auth, sessions, or CSRF token subsystem.
- Require accepted JSON media type and body/header limits for writes; ordinary
  cross-site forms cannot form a valid command.
- Emit the CSP and browser headers in
  [`ARC-CTR-007`](22-web-interaction-contract.md) on entry, asset, API, health,
  and error routes as applicable.
- Disable directory listing, framework debug pages, dynamic code evaluation,
  unreviewed source maps, SQLite extension loading, remote assets/telemetry, and
  user-controlled HTTP filesystem paths.
- API/data/problem responses are `no-store`; content-addressed first-party
  static assets may be immutable-cached while entry HTML is revalidated.

Any remote/LAN access requires a successor architecture for identity,
authorization, TLS/proxy trust, audit/privacy, rate limiting, and incident
response. A port-forwarding recipe is not a compatible configuration.

## Application resource and overload behavior

| Resource | Limit/behavior |
|---|---|
| HTTP body | 32 KiB encoded; reject before JSON/application execution |
| Headers | At most 32 KiB total and 100 fields where server controls support it |
| In-flight requests | At most 64 admitted; excess receives safe `503 overloaded` without command execution |
| Blocking work | 2-32 threads, default 8; one SQLite write mutex |
| SQLite busy wait | At most 5 seconds per operation |
| Records/page/search | 10,000 records; page 100; search 2 seconds plus `ARC-CTR-003` limits |
| Normal application deadline | 10 seconds, with write outcome treated as indeterminate if disconnect/deadline occurs after dispatch |
| Shutdown | Stop admission, drain at most configured/Compose grace, atomically finish/rollback, close and release lock |

Queues, thread pools, request bodies, cursor decoding, regex compilation, and
logs are bounded. Container CPU/memory/PID limits complement rather than
replace application admission control. OOM/forced-kill recovery requires
startup lock/schema/integrity checks before readiness; no client receives a
fabricated rollback/success result.

## Logging and diagnostics

Containers emit structured UTF-8 JSON events to stdout/stderr. A completion
event includes UTC timestamp, level, stable event name, request ID, method,
route template, status, duration, image/build identity, and safe error code
where applicable. Optional safe fields include field/mode, page size, result
count, query byte length, schema version, and a reviewed one-way correlation
fingerprint.

Logs never contain:

- record `value`, full `name`, raw body, query, regex, ETag, or cursor;
- SQL bound values, environment contents, secret material, full host/volume/
  database/backup paths, or backup bytes;
- framework debug output or client-visible stack traces; or
- remote telemetry by default.

ERROR stack traces are permitted only in local container logs after structured
redaction and never with bound/domain values. Docker log rotation is bounded in
the effective Compose model (for example `json-file` with fixed size/count)
and is diagnostic, not an audit or record-recovery store.

## Backup, recovery, and incident handling

Backup/restore behavior follows
[`ARC-CTR-004`](16-sqlite-persistence-contract.md). Operational requirements:

- API is stopped and exclusive lock acquired for backup, migration, restore,
  and integrity recovery; v2 chooses offline consistency over availability.
- Backup IDs/filenames are generated, never arbitrary paths. Existing
  destinations are not overwritten.
- Every accepted backup has architecture/schema/image/source metadata and a
  SHA-256 sidecar, passes identity/migration/row/capacity/`quick_check`, and is
  distinct from live state.
- Restore validates before and after copying, preserves the former live set,
  and starts API only after the switch. Failed smoke/readiness restores or
  leaves recoverable prior state; it never reports success.
- `record-backups` on the same Docker host protects against logical failure,
  not host loss. Operators needing host-loss recovery explicitly stream a
  validated bundle off-volume and protect that file according to its sensitive
  record contents.
- Import validates an opaque backup bundle into `record-backups`; it never
  opens it as live state until a separate stopped-API restore.

For corruption or suspected disclosure: stop API, preserve volume identity,
WAL/SHM/lock context, logs, image/Compose/config metadata, hashes, and relevant
backup artifacts without editing originals; create a forensic export through a
reviewed maintenance path where safe; restore a verified backup to preserved/
new state; then run readiness and canonical domain/search/client smoke vectors.
V2 has no remote incident responder or per-user audit attribution.

## Failure and recovery

| Failure | Detection | Required behavior | Recovery owner |
|---|---|---|---|
| Docker/Compose unavailable or required feature ignored | Preflight/version/effective-config test | Do not start or claim support | Operator/platform owner |
| Image digest/platform/provenance mismatch | Pull/inspect/release verification | Do not execute candidate; retain prior image/volumes | Release owner |
| Invalid/occupied host port or nonloopback publication | Compose render/start and reachability tests | Fail; never choose alternate/wildcard automatically | Operator |
| API image/config/schema/integrity startup failure | Container exit/readiness | No normal ready service or initialization/migration | Operator/persistence owner |
| API and maintenance overlap | Compose-state precondition plus shared exclusive lock | Second owner refuses before state mutation | Operator |
| Named-volume ownership/full/read-only/I/O/corruption | Preflight, SQLite error, readiness | No false success; stop and use accepted maintenance/recovery | Operator/persistence owner |
| CLI/API network unavailable | SDK/CLI typed transport result | Stable unavailable/indeterminate semantics; no direct-state fallback | User/operator |
| Container OOM/kill/daemon restart | Docker state plus missing response/health | Client treats write as indeterminate where applicable; verify integrity/readiness before reuse | Operator |
| Backup/migrate/restore/export/import validation failure | Maintenance checks/hash/exit | Preserve live/prior state and candidate evidence; no success claim | Operator/persistence owner |
| Dependency vulnerability/license conflict | Release review | Block release or record explicit human risk disposition | Product/security owner |
| Destructive volume command | Command/documentation review and operator guard | Never include in safe automation; require explicit out-of-band destructive-data decision and verified backup | Human project/operator authority |

## Compatibility and verification

Changing host prerequisites, orchestrator, service/network/port topology,
shared API path, authentication, public origin, volume/mount authority,
container user/security controls, image identity, supported OCI platform,
maintenance mutual exclusion, or recovery guarantee is an architecture change.

| Required proof | Scenario | Evidence location |
|---|---|---|
| Docker-only clean host | Build, test, initialize, start, web use, CLI use, backup, restore, stop with no host project toolchain | [`ARC-CTR-009`](24-conformance-contract.md) |
| Effective topology | Rendered Compose/image/network/mount/security/resource/profile inspection | Future platform evidence |
| Loopback/private confinement | Host/peer/container reachability plus Host/Origin/proxy negatives | Future operations/security evidence |
| Shared API | CLI and web route inventories and identical direct-API vectors against one `/api/v1` router | Future cross-surface evidence |
| Volume ownership/mutual exclusion | Empty-volume initialization, UID/mode, concurrent API/maintenance, and no-bind tests | Future persistence evidence |
| Lifecycle/recovery | Fresh install, restart, upgrade/migrate, backup/export/import/restore/rollback, daemon/OOM/fault drills | Future operations evidence |
| Supply chain | Locked inputs, digests, multi-platform manifests, SBOM, provenance/signature policy, licenses/vulnerabilities | Future release evidence |
| No host fallback | Documentation/command/package inventory rejects native Python/SDK/CLI/SQLite/Node/application-service paths | Future release evidence |

## Related records

- System boundaries: [`ARC-BND-001`](03-record-platform-boundary.md), [`ARC-BND-002`](12-api-service-boundary.md), [`ARC-BND-003`](15-sqlite-store-boundary.md)
- Decisions: [`ADR-004`](07-ADR-004-container-only-deployment-trust-model.md), [`ADR-005`](08-ADR-005-containerized-technology-stack.md)
- Persistence contract: [`ARC-CTR-004`](16-sqlite-persistence-contract.md)
- Governing evidence: [`AUTH-EX-001`](01-accepted-architecture-baseline.md)
- Superseded native deployment baseline: [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md)

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Defined native local-process operations/security contract | User-authorized best-judgment architecture completion |
| 2026-11-10 | Replaced native operation with mandatory Compose topology, container hardening, named volumes, offline maintenance, and Docker-only lifecycle | User's explicit full-Dockerization/no-host-services instruction |
| 2026-11-10 | Required CLI and web to consume the same `/api/v1` path while retaining their distinct Docker network origins | User's explicit shared-API-path instruction |
