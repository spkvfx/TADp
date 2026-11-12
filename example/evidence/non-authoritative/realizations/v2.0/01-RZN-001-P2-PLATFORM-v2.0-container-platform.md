# Container platform and runtime packaging

**Realization ID:** `RZN-001-P2-PLATFORM-N01`  
**Suite:** [`RZN-001-P2-PLATFORM-SUITE@v2.0`](00-RZN-001-P2-PLATFORM-suite-index.md)  
**Suite version:** `v2.0`  
**Status:** Recorded; invariant-bounded proposal input  
**Recorded by:** Codex on behalf of the User  
**Recorded date:** 2026-11-10  
**Source:** User request in the current Codex conversation and [`RZN-001`](../v0.0/RZN-001-example-record-application.md)  
**Historical product relationship:** Architecture-required predecessor to `RZN-001-P2-SDK-API`; not a product originally named in `RZN-001`  
**Accepted delivery-unit alignment:** `D2 Container platform and runtime packaging`  
**Related initiative or proposal:** None created  

> **Evidence standing:** This note records the platform opportunity introduced
> by accepted architecture after the parent realization. It is not a Compose
> file, Dockerfile, product specification, implementation authorization,
> security assessment, release record, or completion claim.

## Realization

The accepted Compose-only architecture creates a distinct enabling-product
need that was absent from the original four-product wording: one reproducible,
hardened container platform must build, test, package, run, maintain, and
identify the later API, SDK, CLI, and web artifacts without installing their
toolchains or services on the host.

This need is independently reviewable because the BuildKit graph, Compose
topology, named-volume and network authorities, container controls, artifact
identity, supported-host/platform matrix, and safe lifecycle can pass, fail,
release, or change without claiming domain/API/SDK/CLI/web completion.

## Narrow outcome and beneficiary

| Dimension | Candidate record |
|---|---|
| Outcome | A reviewable D2 container-platform artifact set that realizes the accepted build/runtime topology and supplies exact identities for D3-D6 consumers |
| Primary beneficiaries | Local operators, release owners, D3-D6 implementers, security reviewers, and verification owners |
| Authority boundary | Platform packaging and operations only; no ownership of domain, API, SDK, CLI, or browser behavior |
| Output class | Root multi-stage Dockerfile/build graph, `.dockerignore`, Compose model and release lock/override material, service profiles, image metadata, lifecycle commands, and platform evidence |
| Independent review claim | Clean-host Compose-only build/run/test/maintenance topology, isolation, hardening, artifact identity, and supported-platform behavior conform to D2 gates |
| Explicit non-claim | No API capability, record semantics, SQLite domain behavior, SDK public API, CLI interaction, web accessibility, or D3-D6 completion |

## Context and evidence

| Question | Record |
|---|---|
| Why does this realization exist? | The User explicitly required full Dockerization and no host application services/toolchains after `RZN-001`; architecture revision 2.x added D2 as a separate delivery unit. |
| What is already decided? | Compose-only orchestration, BuildKit multi-stage targets, service/network/volume graph, host prerequisites, exact loopback ingress, private DNS, numeric user, read-only containers, resource limits, named volumes, maintenance exclusion, artifact identities, and platform matrix. |
| What remains proposal-level? | Exact repository product destinations, implementation sequencing inside D2, release tooling choices allowed by the invariant, owners, evidence storage, and whether an internal sub-scope needs separate work without changing D2's completion boundary. |
| Who is affected? | Every later product because all supported build, test, runtime, SDK consumption, CLI invocation, web delivery, maintenance, recovery, and release paths use D2 artifacts. |
| What is the current product status? | `ARC-CTR-009` records no supplied D2 implementation or conformance evidence. |

## Binding source inventory

| Source | Exact relevance |
|---|---|
| [`AUTH-EX-001.11`-`.15`](../../../authoritative/architecture/01-accepted-architecture-baseline.md#binding-claims) | Compose-only host boundary, named volumes, hardened images, additive security evidence, and permitted data/use profile. |
| [`ARC-BND-001`](../../../authoritative/architecture/03-record-platform-boundary.md) | Whole-system component graph, actors, state authority, end-to-end invariants, and platform failure boundaries. |
| [`ADR-004`](../../../authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md) | Exact host prerequisite, trust topology, runtime controls, and local identity boundary. |
| [`ADR-005`](../../../authoritative/architecture/08-ADR-005-containerized-technology-stack.md) | Required artifact targets, application stack inside images, build/release rules, and no-host-toolchain constraint. |
| [`ADR-006`](../../../authoritative/architecture/09-ADR-006-contract-versioning-and-feedback.md) | Compose, OCI, wheel, bundle, schema, and source identities and change classification. |
| [`ADR-007`](../../../authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md) | D2 output boundary, predecessors, independent claim, and dependencies. |
| [`ARC-CTR-008`](../../../authoritative/architecture/23-operations-security-contract.md) | Effective Compose service contract, hardening, limits, network, volumes, configuration, lifecycle, health, logging, maintenance, and release behavior. |
| [`ARC-CTR-009`](../../../authoritative/architecture/24-conformance-contract.md) | D2 gate; `CNT-*`, applicable `OPS-*`, and clean-host/end-to-end evidence requirements. |
| [`SEC-NIST-POL-001`](../../../authoritative/security/NIST/01-demonstrator-security-policy.md) | `SEC-POL-01`-`14` security requirements for platform, release, recovery, and assurance. |
| [`SEC-NIST-VER-001`](../../../authoritative/security/NIST/03-future-development-assurance.md) | Exact-artifact `EXAMINE`, `TEST`, and witnessed-evidence expectations. |
| [`SEC-HIPAA-POL-001`](../../../authoritative/security/HIPPA/02-prospective-security-policy.md) | `HSP-001`-`015` data/use, trust, hardening, recovery, inherited-control, and evidence gates. |
| [`SEC-HIPAA-DEV-001`](../../../authoritative/security/HIPPA/04-future-development-and-evidence-standard.md) | Prospective risk, fixture, build, host, recovery, incident, external-service, and verification records. |

## Candidate artifact boundary

The following items are candidate D2 product outputs because the architecture
assigns their behavior to the platform. Their exact paths are not selected by
this realization.

| Candidate artifact | Candidate role | Required identity or constraint |
|---|---|---|
| Root BuildKit graph | Produce `sdk-wheel`, `web-build`, `api-runtime`, `cli-runtime`, and `test` targets from one reviewed graph | Pinned inputs; staged artifact copies; no mutable install in runtime stages; source commit and build identity retained |
| Deny-by-default `.dockerignore` | Exclude Git/IDE state, local databases/backups, secrets, caches, virtual environments, test output, and unrelated material | Reviewable source file plus build-context inspection; no protected or user data unintentionally copied |
| `compose.yaml` | Define API, CLI, maintenance, test roles, private network, named volumes, health, security, and resource controls | Rendered effective configuration is the execution evidence; fragments/examples are insufficient |
| Release image lock/override | Bind API/CLI images to immutable multi-platform manifest digests and compatible identities | Mutable tags are convenience only; exact digest and platform evidence required |
| Service entrypoints and profiles | Preserve long-running API, one-shot CLI, stopped-API networkless maintenance, and isolated test lifecycles | Exec form, allowlisted maintenance, no hidden daemon or service auto-start |
| Health executable/config | Query internal health without adding general shell/network tooling | Exact internal Host, no data/schema/path disclosure, no mutation, readiness tied to safe store/assets |
| Build/test profiles | Run all automated project checks inside declared targets/services with isolated disposable state | No host project Python/Node/SQLite/SDK/CLI/test toolchain; no live-volume access |
| Lifecycle/runbook material | Initialize, start, stop, update, backup, export/import, restore, and failure recovery through accepted roles | Preserve volumes during ordinary use; destructive commands excluded and explicitly classified |
| Release metadata and evidence | Identify manifests, image digests, wheel/bundle hashes, labels, SBOM, provenance, vulnerability/license results, and supported matrices | Exact tested bytes and clear limitations; labels alone are not proof |

## Accepted effective topology to preserve

| Role | Candidate D2 responsibility | Boundary that must remain visible |
|---|---|---|
| `record-api` | One long-running replica/worker; private `record-net`; exact loopback host publication; `record-data` only; health checked | D3 owns API and persistence behavior; D2 owns service placement, mounts, network, limits, and image reference |
| `record-cli` | One-shot `docker compose run --rm`; private network; no port or volume; exact CLI image/wheel identity | D5 owns command behavior; D2 owns isolation and invocation envelope |
| `record-maintenance` | One-shot, `network_mode: none`, data/backup mounts, stopped-API and shared-lock preconditions, closed commands | D3 persistence/operations code owns maintenance behavior; D2 owns topology and access envelope |
| `record-test` | Explicit profile/project, test-only private network, disposable named volumes, no release-state resolution | Product owners own tests; D2 owns isolation primitives and no-live-state guarantee |
| Build stages | Ephemeral dependency/build/test execution; never live-volume mounts | D3-D6 own source outputs; D2 owns reproducible stage boundaries |

## Host and network boundary

The candidate D2 outcome is useful only if it makes these accepted facts
observable and enforceable:

- The host requires Docker Engine/Desktop with Compose v2 and a supported
  browser; Git is additionally permitted on source-development hosts.
- Python, pip/pipx/venv, the SDK, CLI, FastAPI, Uvicorn, Pydantic, HTTPX, RE2,
  SQLite, Node/npm/TypeScript, migrations, maintenance, and test tooling are
  not supported host prerequisites or execution paths.
- The only public application mapping is
  `127.0.0.1:${RECORDS_HOST_PORT}:8000`; wildcard, IPv6, hostname, LAN, public,
  proxy, tunnel, host-network, and random fallback bindings are excluded.
- `record-net` contains only declared services. The CLI reaches
  `record-api:8000`; maintenance has no network; runtime has no outbound
  dependency.
- Browser and container clients terminate on one `/api/v1` router. D2 must not
  introduce a gateway or consumer-specific API.
- The Docker daemon and authorized host administrators remain inside the
  administrative trust boundary; container controls do not claim protection
  against them.

## Runtime hardening boundary

Every runtime and maintenance role must be representable in the effective
configuration with the accepted controls, and a future product claim would
need to prove those controls are effective rather than merely present:

| Control area | Accepted platform outcome |
|---|---|
| Identity | Numeric `10001:10001`; no root repair entrypoint or runtime privilege escalation |
| Filesystem | Read-only root; bounded `/tmp` tmpfs with `nosuid,nodev,noexec`; only declared named volumes writable |
| Privilege | All Linux capabilities dropped; `no-new-privileges:true`; no privileged mode, devices, Docker socket, host PID/IPC/network, or arbitrary host paths |
| Resources | Effective CPU, memory, PID, temporary-storage, stop-grace, request, and bounded logging controls from `ARC-CTR-008` |
| Contents | Runtime images omit compiler, package-manager cache, test fixtures, source checkout, build secrets, unrelated tools, and mutable install steps |
| Secrets | No credentials, tokens, keys, or secrets in layers, labels, environment, commands, logs, health, or Compose files; v2 has no application secret |
| Mutability | Replace reviewed immutable images; never patch a running or released image in place |

## Volume and maintenance boundary

| State | Candidate platform responsibility | Prohibited shortcut |
|---|---|---|
| Live database | Docker named volume `record-data` at the fixed API path; API normal read-write authority | Host bind, anonymous/external live volume, Docker Desktop path, host SQLite, CLI/test/build mount |
| Backups | Separate named volume `record-backups`; maintenance only | API/CLI mount, same file as live state, arbitrary host path, overwrite of existing artifact |
| Maintenance ownership | API stopped plus shared lock; networkless allowlisted command; fixed paths and numeric ownership | Concurrent maintenance, Docker-socket inspection, arbitrary shell/SQL/Python/path/URL execution |
| Test state | Fresh disposable named volumes under unique project identities | Resolving, copying, mounting, or deleting release/user volumes |
| Host export/import | Explicit opaque validated bundle through bounded stdin/stdout framing | Live-volume mount, record-level interchange, merge, direct host database access |

The platform note does not claim that maintenance logic is implemented. It
records the D2 access envelope needed by D3's persistence and recovery
behavior.

## Configuration and lifecycle boundary

The accepted ordinary configuration surface is deliberately limited to
`RECORDS_HOST_PORT`, `RECORDS_LOG_LEVEL`, `RECORDS_WORKER_THREADS`, and
`RECORDS_SHUTDOWN_SECONDS`, with exact type/range rules in `ARC-CTR-008`.
Unknown `RECORDS_*` or `EXAMPLE_RECORDS_*` inputs must fail before readiness.
Internal names, paths, image references, volume identities, API base, user,
and security controls are not ordinary overrides.

Candidate lifecycle coverage includes:

1. preflight Docker/Compose/platform identity and render inspection;
2. immutable pull or declared development build;
3. stopped-API maintenance initialization of an empty accepted store;
4. one-replica API start with health and exact-loopback checks;
5. browser, CLI, and declared developer-container use through their accepted
   origins;
6. graceful stop and ordinary `down` that preserves named volumes;
7. upgrade with exact predecessor evidence, preflight check, mandatory backup,
   optional accepted migration, successor smoke verification, and rollback
   identity; and
8. offline backup/export/import/restore operations with no false success.

`docker compose down -v`, volume removal or prune, and deletion of Docker
Desktop data are destructive operations. They are not candidate safe lifecycle
steps and require separate human data-loss authority and verified backup.

## Security-policy applicability

| Platform concern | NIST policy anchors | HIPAA policy anchors | Candidate evidence direction |
|---|---|---|---|
| Permitted profile and claim limits | `SEC-POL-01`, `SEC-POL-14` | `HSP-001`, `HSP-002`, `HSP-015` | Release limitation statement, data/fixture classification, no expansion trigger |
| Network and container access | `SEC-POL-02`, `SEC-POL-03` | `HSP-004`, `HSP-005` | Render/runtime/reachability negatives, declared membership, privilege/mount probes |
| Baseline configuration and resources | `SEC-POL-04`, `SEC-POL-07` | `HSP-003`, `HSP-009` | Effective config hashes, input-negative tests, resource exhaustion and restart checks |
| State and recovery envelope | `SEC-POL-05`, `SEC-POL-09` | `HSP-007`, `HSP-010`, `HSP-011` | Mount graph, lock overlap, offline role, backup/restore/rollback, host/media decisions |
| Safe handling and logging | `SEC-POL-06`, `SEC-POL-08` | `HSP-006`, `HSP-008` | Build-context/data leak scan, bounded logs, no secret or record amplification |
| Supply chain and vulnerability response | `SEC-POL-10`, `SEC-POL-12` | `HSP-009`, `HSP-013` | Locks, digests, SBOM, provenance, scans, external-service inventory, dated dispositions |
| Assurance and incident response | `SEC-POL-11`, `SEC-POL-13` | `HSP-012`, `HSP-014` | Exact vector records, platform matrix, incident table-top, source/risk review |

A future proposal must still assess every policy ID individually. The grouped
mapping above is not a completed applicability matrix or risk analysis.

## Candidate verification boundary

The authoritative D2 gate requires all `CNT-*`, applicable `OPS-*`, and
`E2E-009` vectors plus exact NIST and HIPAA evidence. Important candidate
evidence clusters include:

| Evidence cluster | Principal vector anchors | Exact candidate claim bounded by the evidence |
|---|---|---|
| Clean-host path | `CNT-001`, `E2E-009` | Build, test, initialize, start, use, backup/restore, and stop need no host project toolchain |
| Effective topology | `CNT-002`-`005`, `CNT-011`, `CNT-015` | Roles, network, port, volumes, users, privileges, mounts, and maintenance boundaries match the accepted graph |
| Resource and failure behavior | `CNT-006`, `OPS-006`, `OPS-007` | Bounds are effective and kill/OOM/restart cannot produce false success or unsafe readiness |
| Runtime contents and artifact continuity | `CNT-007`-`009`, `OPS-010` | Minimal images, exact wheel/bundle bytes, immutable manifests, platform evidence, SBOM/provenance, and findings agree |
| State preservation and isolation | `CNT-010`-`013`, `OPS-004`, `OPS-011`-`013` | Ordinary lifecycle preserves state; tests isolate it; maintenance and destructive boundaries fail safely |
| Network and shared API | `CNT-003`, `CNT-014`, `OPS-002`, `OPS-003` | Only exact permitted ingress works, and platform routing creates no second API |
| Configuration and health | `OPS-001`, `OPS-005`, `OPS-009` | Closed inputs, fail-closed readiness, and browser security headers operate in the exact release configuration |

Every run would need the evidence fields in `ARC-CTR-009`,
`SEC-NIST-VER-001`, and `SEC-HIPAA-DEV-001`, including exact artifact hashes,
host and OCI platform, Docker/Compose/BuildKit versions, rendered config hash,
method, results, limitations, dispositions, reviewer, and synthetic fixture
identity. This note records no result.

## Required prospective records to carry forward

The platform scope makes these future records materially relevant:

- policy applicability matrix for every `SEC-POL-*` and `HSP-*` ID;
- data and fixture manifest covering build contexts, test state, logs,
  screenshots, backups, and evidence artifacts;
- platform/data-flow threat and risk analysis with a named security owner;
- access and trust-boundary record for OS, Docker, services, networks, volumes,
  administrators, and excluded actors;
- secure build/release record for locks, digests, SBOM, provenance, signatures
  policy, platforms, vulnerabilities, licenses, and artifact continuity;
- host and media baseline with supported versions, patch posture, encryption
  decision, unique account/screen lock, physical use, export custody, and
  sanitization;
- recovery plan and drill record;
- activity-review and incident procedures;
- external-service and runtime/build egress inventory; and
- exact architecture/NIST/HIPAA verification record and release limitation
  statement.

These records are prospective requirements from the invariants, not files
created by this realization.

## Dependencies and handoffs

| Dependency | Required handoff identity | What D2 must not infer |
|---|---|---|
| D1 | Exact accepted architecture/contract and derivative-doc revision used | That architecture existence equals D1 initiative completion |
| D3 | Image target contract, service/mount/network envelope, schema/health/maintenance compatibility | That building an API image proves API/domain/persistence conformance |
| D4 | `sdk-wheel` build artifact and declared consumer/test image path | That wheel bytes or install success prove SDK behavior |
| D5 | CLI runtime target, fixed private DNS, exact wheel hash, no-mount/no-port envelope | That Compose invocation proves command semantics |
| D6 | `web-build` output copy/hash chain into API image and same-origin delivery envelope | That embedded assets prove accessibility or browser behavior |

## Risks to preserve for proposal analysis

| Risk | Consequence |
|---|---|
| D2 absorbs D3-D6 behavior | A platform build or smoke test could be misreported as product completion. |
| Rendered Compose differs from reviewed source | Effective ports, mounts, privileges, or image references can violate the trust boundary. |
| Mutable tags or rebuilt wheel/bundle bytes | The released artifact is not the tested artifact. |
| Platform ignores required security/resource settings | A nominally supported host silently weakens the accepted controls. |
| Test profile can resolve live volumes | Verification may disclose or corrupt user state. |
| Root entrypoint repairs volume permissions | Runtime privilege and mutability become an undocumented dependency. |
| Same-host backup is described as disaster recovery | Users may rely on a host-loss guarantee that does not exist. |
| Unsafe convenience commands enter the runbook | Ordinary maintenance can irreversibly delete state. |
| Build or evidence fixtures contain real or sensitive data | Source, layers, logs, scans, and provenance leave the permitted profile. |

## Questions that remain for a future proposal

1. Which exact repository paths own the D2 artifacts and release locks?
2. Which supported Docker/Compose/BuildKit patch versions and registry trust
   roots will be fixed for the first evidence run?
3. Which provenance/signature mechanism is selected within the accepted
   policy, and who owns its trust root and verification procedure?
4. How are native `linux/amd64`, native `linux/arm64`, Windows, Linux, macOS,
   and Safari/manual evidence environments provisioned without making them
   product runtime dependencies?
5. Where will machine-readable evidence, SBOMs, findings, and review
   dispositions be retained without leaking prohibited data?
6. Does any implementation sub-scope have an independently acceptable owner,
   lifecycle, or release that requires a narrower proposal while retaining one
   D2 completion boundary?

No answer is selected by this note.

## Candidate outcome

A local operator and every later product owner can rely on one exact,
digest-identified Compose platform that builds and runs only the accepted
roles, confines network and state access, enforces the declared runtime
controls, preserves safe lifecycle and recovery boundaries, and supplies
reviewable artifact identities without claiming any D3-D6 behavior.

## Suggested next step

Take no initiative action now. If later directed, prepare a D2-only proposal
from this note, cite the exact invariant sections and policy IDs, choose the
artifact destinations, perform the narrow-scope assessment, and retain the six
unresolved proposal questions for explicit human disposition.

## Handoff notes

A future D2 proposal must cite this realization and its v2.0 suite index,
preserve the fact that D2 was introduced by accepted architecture rather than
the original `RZN-001` wording, and state precisely what D2 supplies to the
v2.1/D3, v2.2/D4, v3.0/D5, and v4.0/D6 suites without accepting or completing any
of them.



## Version-scope migration addendum (2026-11-12)

**Version scope:** `v2.0`

**Migration authority:** [EX-VSG-DR-001](../../../../initiatives/decision-receipts/EX-VSG-DR-001-initiative-migration.md)

**Current initiative target:** [INIT-IMP-002](../../../../initiatives/v2.0/implementation/INIT-IMP-002-container-platform/README.md)

**Exact source catalog:** [RZN-001-P2-PLATFORM-N01](01-RZN-001-P2-PLATFORM-v2.0-container-platform.md)

The original headers and one-to-one allocation language remain historical evidence under the prior revision. This addendum adopts scope membership and many-target catalog capability without changing source identity, relabeling this note or promoting its non-authoritative standing. The existing target retains the same narrow Proposed claim. Future independent outcomes require their own initiative records, not necessarily another version. The initiative index owns current assignments; the historical branch and base above remain history.
