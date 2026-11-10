# Container-only local deployment trust model

**Decision ID:** `ADR-004`  
**Status:** Accepted  
**Architecture revision:** `2.0.0`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Supersedes `ADR-004@1.0.0`, preserved in [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md); no successor  
**Related initiative:** Not applicable - direct project-architecture instruction  

## Decision question

What deployment and trust boundary ensures that no application service,
language runtime, SDK, CLI, database tool, or build tool must be installed on
the host?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.6`](01-accepted-architecture-baseline.md) | V2 is a local single-user application exposed only on host loopback | Requires local-only host publication |
| [`AUTH-EX-001.11`](01-accepted-architecture-baseline.md) | Every application runtime/build/test/maintenance path is containerized | Prohibits native-host application prerequisites |
| [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md) | Preserves the replaced native-host deployment meaning | Supplies revision history and compatibility boundary |
| User instruction on 2026-11-10 | "I don;t want to install all the services on teh host. make taht decision now and add to the architecturer invaraint" | Explicitly authorizes the invariant change |

## Decision

Revision `2.0.0` has exactly one supported deployment path: a Docker Compose
application assembled from pinned Linux OCI images. The host installs only:

- Docker Engine with Docker Compose v2, or Docker Desktop including Compose;
- a supported browser for the web interface; and
- Git only when the host is used for source development.

The host must not need Python, pip/pipx, FastAPI, Uvicorn, Pydantic, HTTPX,
RE2, SQLite, the SDK, `recordctl`, Node.js/npm/TypeScript, migration tooling,
or test runners. Those dependencies exist only in image build stages or
runtime/test/maintenance containers.

### Compose trust topology

```text
Host browser
    |
    | http://127.0.0.1:${RECORDS_HOST_PORT}
    v
Docker loopback publication
    |
    v
record-api container (0.0.0.0:8000 inside private network)
    |                         ^
    |                         |
record-data named volume     +--- record-cli one-shot container

record-maintenance one-shot container
    |-- mounts record-data and record-backups
    `-- network_mode: none; API must be stopped
```

- Compose publishes container port 8000 only as
  `127.0.0.1:${RECORDS_HOST_PORT}:8000`. IPv6, wildcard, LAN, public, proxy,
  tunnel, and arbitrary interface publication are outside the accepted file
  and must fail conformance review.
- `record-api` binds `0.0.0.0:8000` **inside** its isolated bridge network so
  the CLI container can reach it. This internal bind is not authority for host
  wildcard publication.
- `record-cli` is a one-shot Compose service/image on the private application
  network and calls `http://record-api:8000/api/v1`; it mounts no state volume.
- The browser calls the host-loopback public origin. Browser writes require
  that exact Origin. CORS remains disabled.
- CLI/SDK and browser use the identical `/api/v1` route/semantic contract;
  private DNS versus loopback publication changes only their network entrance.
- `record-maintenance` has no network, runs only while `record-api` is stopped,
  and is the only component other than `record-api` permitted to mount the
  data volume read-write. It owns initialization checks, offline backup,
  integrity, migration recovery, and restore commands.
- The web assets are built in a container stage and embedded in the API image;
  there is no host web server or separate native web service.
- Automated build, unit, contract, integration, migration, security, and
  browser-test support services run in pinned containers. A host browser may
  perform required manual accessibility/Safari review because it is a user
  agent, not an installed application service.

### Container controls

Runtime services use non-root numeric UID/GID `10001:10001`, read-only root
filesystems, a bounded tmpfs for `/tmp`, `cap_drop: [ALL]`,
`no-new-privileges:true`, bounded PIDs/memory/CPU, an explicit stop grace
period, and no Docker socket mount. Only declared named volumes and the private
network are attached. Images contain no compiler, package manager cache, test
fixture, source checkout, shell-based entrypoint mutation, or embedded secret
unless a separately justified runtime requirement proves it necessary.

The Docker daemon remains a privileged local dependency. Any actor with daemon
or host administrator/root control is inside the administrative trust boundary
and can inspect volumes/processes; application-level controls do not claim to
protect against that actor.

### Application identity boundary

V2 remains single-user and has no application accounts, authentication,
authorization roles, cookies, or remote sessions. The local OS account allowed
to use Docker and access host loopback is the human authorization boundary.
Other project-controlled containers on the private network are trusted build/
runtime components; arbitrary containers must not be attached.

## Consequences

### Benefits

- A user installs one platform prerequisite instead of multiple language,
  database, SDK, CLI, and build toolchains.
- Image digests, Compose configuration, health, volume, network, user, and
  resource settings make the runtime reproducible and reviewable.
- Windows, Linux, and macOS Docker hosts execute the same Linux application
  artifacts rather than platform-specific native dependency sets.
- The live SQLite file stays in a Docker-managed local volume with consistent
  Linux locking semantics, including on Docker Desktop hosts.
- CLI and maintenance remain isolated from the browser/public host port and
  from each other's state authority.

### Costs, risks, and required follow-up

- Docker/Compose becomes mandatory and materially increases image/build/
  volume/network lifecycle complexity.
- Docker Desktop licensing/resource behavior and daemon privileges are outside
  application control and must be documented by the release owner.
- Users must understand that `docker compose down` preserves named volumes but
  `down -v` destroys them; destructive commands require explicit warnings and
  backup confirmation in documentation.
- Host port collision, daemon outage, image pull/build failure, volume
  permission, and architecture mismatch become first-class failure modes.
- Named data and backup volumes on the same host do not protect against host
  loss; an explicit containerized export procedure is required for off-volume
  backup copies.
- Multi-platform image manifests and dependency wheels must pass conformance
  on every claimed `linux/amd64` or `linux/arm64` target.
- Remote/multi-user exposure still requires a successor identity, TLS/proxy,
  authorization, audit, privacy, rate-limit, and incident architecture.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| Native host API plus pipx CLI | Directly conflicts with the User's no-host-services invariant | Only an explicit invariant revision by project authority |
| Containerized API but host CLI/SDK/build | Not fully Dockerized and still requires Python/tool installs | Only an explicit invariant revision |
| Bind-mount host SQLite file | Host filesystem sharing can weaken Linux locking/ownership semantics, especially under Docker Desktop | A verified storage architecture and migration with equivalent locking/recovery evidence |
| Separate web-server container | Adds reverse proxy/same-origin/configuration surface without a v1 need | Independent web scaling or server requirement |
| Public/LAN container port | Unsafe under no-auth single-user model | Accepted remote security architecture |
| Docker socket inside application container | Grants host-equivalent control and violates least privilege | Not accepted for this application |
| Kubernetes | Disproportionate and conflicts with compact local single-user scope | A separately accepted distributed deployment product |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| Host runbook requires only Docker/Compose and browser | Clean-host install/run audit with tool inventory | [`ARC-CTR-009`](24-conformance-contract.md) |
| No host application command is a supported path | Documentation, package, script, and release inventory | Future release evidence |
| Host publication is loopback-only while CLI uses private DNS | Rendered Compose/config/network tests from host and peer machine/container | Future operations/security evidence |
| Only API/maintenance mount data under mutual exclusion | Rendered Compose mount graph plus competing-container tests | Future persistence evidence |
| Images enforce non-root/read-only/capability/resource constraints | Image/config inspection and runtime negative tests | Future release evidence |
| Build/test/migrate/backup/restore all execute in containers | CI/runbook command and artifact evidence | Future product evidence |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted local native-runtime, loopback-only trust model as `ADR-004@1.0.0` | User-authorized best-judgment method |
| 2026-11-10 | Superseded native runtime with container-only Compose deployment; prohibited host application/service/toolchain installation | User's exact Dockerization and no-host-services instructions quoted above and in `ARC-REV-001` |

