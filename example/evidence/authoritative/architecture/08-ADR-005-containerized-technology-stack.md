# Normative containerized technology stack

**Decision ID:** `ADR-005`  
**Status:** Accepted  
**Architecture revision:** `2.0.1`  
**Decision owner:** User, project authority  
**Decision date:** 2026-11-10  
**Supersedes / superseded by:** Supersedes `ADR-005@1.0.0`, preserved in [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md); no successor  
**Related initiative:** Not applicable - direct project-architecture instruction  

## Decision question

Which container, application, build, packaging, and orchestration technologies
form the v2 compatibility target while requiring no application toolchain on
the host?

## Context and binding evidence

| Source | Precise claim or constraint | Effect on this decision |
|---|---|---|
| [`AUTH-EX-001.11`](01-accepted-architecture-baseline.md) | Compose is the only supported runtime and no application toolchain is installed on the host | Requires containerized runtime/build/test/maintenance |
| [`ADR-004`](07-ADR-004-container-only-deployment-trust-model.md) | Defines service/network/volume/host trust boundary | Constrains image and Compose roles |
| [Official `google-re2` distribution](https://pypi.org/project/google-re2/) | Official RE2 Python package currently publishes Linux wheels for selected CPython/platform targets | Supports feasibility; delivered wheel/version still requires locked matrix proof |
| [`ARC-REV-001`](revisions/1.0.0/00-superseded-native-runtime-deployment-baseline.md) | Preserves prior native-runtime stack | Requires explicit successor/migration effect |

## Decision

### Host prerequisites

The supported host needs Docker Engine with Compose v2, or Docker Desktop with
its Compose v2 plugin, plus a browser. Source developers also need Git. Nothing
else is a host prerequisite for building, testing, running, migrating, backing
up, restoring, using the CLI, or serving the web application.

### Container artifact set

| Artifact/target | Selected technology and contents | Runtime role |
|---|---|---|
| Root `Dockerfile` | Docker BuildKit multi-stage build with named `sdk-wheel`, `web-build`, `api-runtime`, `cli-runtime`, and `test` targets | Single reviewed build graph; stages copy artifacts, never package-manager state |
| `example-records-api` image | Pinned digest-derived Python 3.13 slim Linux base; FastAPI, Pydantic v2, Uvicorn, stdlib `sqlite3`, official `google-re2`, app packages, migrations, compiled web assets | Long-running `record-api`; alternate maintenance command from same compatible code/image |
| `example-records-cli` image | Same Python minor/base family; installed released SDK wheel, HTTPX, CLI package only; `recordctl` as exec-form entrypoint | One-shot `record-cli`; no API/server/SQLite package or state mount |
| SDK wheel | PEP 517/518 wheel built in `sdk-wheel` stage from locked inputs | Installed in CLI/test/developer images and published as a versioned artifact; never required on host |
| Web bundle | Semantic HTML/authored CSS/framework-free TypeScript compiled in a pinned build-only Node active-LTS stage | Copied into API runtime image; Node/npm/compiler absent at runtime/host |
| Test image(s) | Python test/static tooling and, where required, a pinned browser-automation image/profile | One-shot isolated tests with disposable volumes/network; never released as runtime |
| `compose.yaml` | Compose Specification model for API, CLI, maintenance, test profiles, network, named volumes, health, limits, security controls | Only supported orchestration entry point |
| Release override/lock | Image references by immutable digest, declared `linux/amd64` and `linux/arm64` manifests, version labels | Makes release execution independent of mutable tags/local source |

Exact dependency patch versions, base-image digests, lock hashes, image digests,
and tool versions belong in reproducible release/build records. They must be
current, supported, license/security reviewed, and conformance-tested at
delivery. A mutable tag or local cache does not establish release identity.

### Application stack inside images

| Area | Selected implementation |
|---|---|
| API | FastAPI with Pydantic v2 models/settings and generated OpenAPI 3.1; Uvicorn exactly one worker |
| Domain/application | Framework-independent Python modules; dependencies point inward under `ARC-BND-002` |
| Persistence | Python standard-library `sqlite3`, explicit parameterized SQL, reviewed ordered SQL migrations, no ORM |
| Regex | Official `google-re2` Python binding pinned to a conformance-tested build |
| SDK | Synchronous HTTPX client plus immutable strict Pydantic v2 public models |
| CLI | Python standard-library `argparse` over the installed public SDK |
| Web | Semantic HTML, authored CSS, framework-free TypeScript compiled to JavaScript in build stage |
| Configuration | Compose variables/secrets-free v2 settings validated inside containers; no host application config file outside declared `.env`/Compose inputs |
| Logs | Structured stdout/stderr consumed by Docker logging; no in-container log files |

The API executes synchronous SQLite/RE2 work in a bounded worker pool and uses
the accepted one-writer mutex. Containers are Linux; Windows/macOS hosts run
them through Docker rather than native wheels/runtime processes.

### Build and release rules

- Build context is the repository root with a deny-by-default `.dockerignore`
  excluding Git metadata, IDE state, local databases/backups, secrets,
  caches/venvs, test output, and unrelated artifacts.
- BuildKit stages use locked/hashes or equivalent reproducible dependency
  resolution, no floating install command, and cache/secret mounts that are not
  copied into images.
- Runtime images copy only wheels/application/migrations/web outputs needed by
  that target, use exec-form entrypoints, and run as `10001:10001`.
- Released images contain OCI labels for product version, Git commit,
  architecture revision `2.0.1`, source identity, build time, licenses/SBOM
  reference, and compatible API/schema versions.
- Release manifests cover each claimed platform. Building one platform locally
  does not prove multi-platform compatibility.
- Compose development mode may build from source. A released deployment uses
  immutable image digests; a mutable tag is convenience metadata only.
- Every automated check runs through a declared build/test target or Compose
  profile. CI may host Docker but may not install/use project Python/Node/
  SQLite toolchains as the normative path.

## Consequences

### Benefits

- Users avoid host Python/Node/SQLite/SDK/CLI/API dependency installation and
  receive one reproducible Linux runtime topology.
- The SDK wheel and web bundle are still independently versioned artifacts
  while their build/consumption paths remain containerized.
- Build/runtime separation reduces compiler/package-manager/test surface in
  released images.
- Identical image digests make API/CLI dependency alignment traceable.
- Named volumes and private networking isolate state and internal CLI traffic.
- Official RE2 and SQLite operate in tested Linux images instead of divergent
  host environments.

### Costs, risks, and required follow-up

- Docker/BuildKit/Compose, registry, image provenance, SBOM, multi-platform
  builds, base refresh, and container CVE response become product obligations.
- Python slim images still contain an OS/libc/OpenSSL/SQLite supply chain that
  must be pinned and reviewed.
- Cross-platform Docker host behavior, UID/volume initialization, emulation,
  resource limits, DNS, and health ordering require explicit tests.
- Build-time network access must be controlled and evidenced; offline rebuilds
  are not claimed unless all dependencies are mirrored.
- Safari/manual assistive-technology review may use a host browser because
  those are user agents, not application services; automated project tooling
  remains containerized.
- Exact official `google-re2` wheels must exist for every declared image
  Python/platform target or release is blocked; source compilation is not an
  unreviewed fallback.

## Alternatives considered

| Alternative | Why it was not selected | Reconsideration trigger |
|---|---|---|
| Native Python/Node/SQLite plus optional Docker | Violates the explicit no-host-services/toolchain invariant | Explicit architecture-authority revision |
| Separate Dockerfiles with unrelated dependency resolution | Encourages API/CLI/SDK drift and duplicated build policy | Evidence a single build graph cannot remain secure/maintainable |
| Separate nginx/web container | Adds reverse proxy/same-origin/version-skew surface for a compact app | Independent web-server/scaling requirement |
| Alpine/musl runtime | Increases binary-wheel/build compatibility risk for RE2/Python packages | Complete locked platform evidence and explicit successor |
| ORM/SQLAlchemy | Adds abstraction/migration surface without a multi-database need | Accepted multi-database/larger-schema requirement |
| Python standard `re` | Does not meet bounded regex design | Successor search decision with equivalent safety evidence |
| Host pipx CLI | Violates full Dockerization and duplicates dependency management | Explicit invariant revision |
| Kubernetes | Disproportionate, remote/distributed orchestration outside local scope | Separately accepted deployment product |

## Acceptance and verification

| Required result | How it is verified | Evidence location |
|---|---|---|
| Clean host builds/tests/runs/uses/maintains through Docker only | Host tool inventory plus scripted Compose lifecycle | [`ARC-CTR-009`](24-conformance-contract.md) |
| Runtime images contain only intended component dependencies | SBOM/layer/file/import scan and image-size review | Future release evidence |
| Multi-stage artifacts are identical to tested/published artifacts | Digest, provenance, wheel/bundle hash chain | Future build evidence |
| Both declared OCI platforms pass applicable vectors | Native or explicitly qualified emulation platform matrix | Future release evidence |
| RE2/SQLite/Python behavior matches contracts | Pinned engine/runtime conformance vectors | Future API evidence |
| No mutable tag/toolchain drift controls release | Rendered Compose/image digest/lock/provenance review | Future operations evidence |

## Revision record

| Date | Change | Authority |
|---|---|---|
| 2026-11-10 | Accepted native v1 Python/FastAPI/Pydantic/SQLite/HTTPX/framework-free web stack | User-authorized best-judgment method |
| 2026-11-10 | Retained application technologies inside mandatory multi-stage OCI images; made BuildKit/Compose/containerized build-test-run-maintenance the only supported path | User's exact full-Dockerization and no-host-services instructions preserved in `ARC-REV-001` |

