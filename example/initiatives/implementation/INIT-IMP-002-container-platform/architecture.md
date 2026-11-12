# Container platform and runtime packaging architecture and specification

**Initiative:** Container platform and runtime packaging
**Status:** Proposed
**Last updated:** 2026-11-11

Related documents: [initiative](README.md), [proposal](proposal/README.md),
[assumptions](assumption.md), [mapping](source-mapping.md), [decisions](open-questions.md),
[roadmap](implementation-roadmap.md), and [steps](implementation-steps.md).

## Proposal standing

Proposal sources are non-authoritative. This Proposed specification applies
accepted evidence but resolves no assumption or `PLT-*` choice.

## Specification boundary

This implementation specification aligns future D2 products to existing
architecture/security contracts. It cannot modify those contracts or claim
D3–D6 behavior.

## Current repository baseline

| Area | Current contract or evidence | Consequence for this initiative |
|---|---|---|
| Trust/topology | `ADR-004`, `ARC-CTR-008` | Exact loopback/private-network roles and hardening are binding |
| Build/release | `ADR-005` | Multi-stage targets, minimal images, and artifact continuity are binding |
| Qualification | `ARC-CTR-009`, D2 gate | All `CNT-*`, applicable `OPS-*`, and `E2E-009` remain prospective |
| Product paths | None selected | `PLT-01` blocks execution |

## Goals and non-goals

### Goals

1. Reproducibly build exact minimal platform artifacts.
2. Enforce the effective Compose topology, hardening, isolation, and safe lifecycle.
3. Preserve exact handoff identities and additive architecture/security evidence.

### Non-goals

- Implement or prove D3–D6 behavior.
- Support host-native, remote/public, production, ePHI, or HA deployment.

## Terms and identity

| Term or identity | Definition | Authority or lifecycle |
|---|---|---|
| Effective Compose | Fully rendered runtime authority | Hash and inspect before execution |
| Image/manifest digest | Immutable OCI release identity | Bound to source, platform, SBOM, provenance |
| Artifact handoff | Exact wheel/bundle/target interface | Does not transfer completion |
| Named volume | Docker-managed live or backup state identity | Access only by accepted role |

Duplicate or mutable identities fail release; supported matrices record exact
host, Docker, Compose, BuildKit, and OCI-platform versions.

## Architectural decisions

| Decision ID | Direction used by this design | Status |
|---|---|---|
| `PLT-01` | Prefer one root product family whose ownership and generated outputs are explicit. | Open, blocking |
| `PLT-02` | Select the narrowest reproducible matrix that covers the architecture-required hosts and native OCI targets. | Open, blocking |
| `PLT-03` | Choose one authenticated, documented mechanism and keep signatures as evidence rather than proof by assertion. | Open, blocking |
| `PLT-04` | Use declared external runners/hosts without making them application runtime dependencies. | Open |
| `PLT-05` | Use a content-addressed project evidence destination that excludes prohibited data. | Open |
| `PLT-06` | Keep one D2 initiative only if the complete scope remains one platform artifact family and gate. | Open |

## Boundaries and ownership

| Component or package | Responsibility | Authoritative state | Must not own |
|---|---|---|---|
| Build graph | Produce sdk-wheel, web-build, API, CLI, and test targets | Locked source/build inputs | Consumer semantics |
| Release Compose | Services, network, ports, volumes, profiles, limits | Rendered configuration | Domain/API behavior |
| Runtime images | Minimal role-specific execution | Digest-qualified manifests | Mutable install or host tools |
| Maintenance envelope | Networkless stopped-API command role | D3-compatible resources and shared lock | Arbitrary shell, network, or state meaning |
| Test profile | Disposable isolated verification | Unique project/network/volumes | Live user state |

## Domain model and evidence/authoritative

### Model

D2 consists of immutable build inputs, named targets, OCI manifests, one release
Compose model, role-specific runtime configurations, artifact hashes, and
release/verification metadata. Product semantics remain owned by consumers.

### Binding requirements

- Exact Compose-only topology, loopback publication, private network, separate
  named volumes, one API replica/worker, and networkless maintenance.
- UID/GID 10001, read-only roots, bounded tmpfs/resources/logs, dropped
  capabilities, no-new-privileges, and prohibited host/socket/device access.
- Locked inputs, minimal runtime contents, digest identity, SBOM/provenance,
  vulnerability/license review, and exact wheel/bundle continuity.
- Synthetic/de-identified-only, non-production use and additive NIST/HIPAA evidence.

## State and persistence

| State | Durable source | Live or derived state | Write owner | Recovery rule |
|---|---|---|---|---|
| Platform configuration | Reviewed source and locks | Rendered Compose | D2 release process | Reject render drift; rebuild reviewed artifact |
| Runtime images | Registry/content store by digest | Containers | Build/release process | Replace with verified digest; never patch |
| Live/backup volumes | Docker named volumes | Mounted state | D3 API/maintenance contracts | D2 preserves mounts/identity; D3 owns contents |
| Test state | Disposable named volumes | Isolated test containers | Test profile | Tear down only test identities |
| Evidence | Selected evidence destination | Reports/SBOM/provenance | Evidence owner | Preserve prior results and rerun changed artifacts |

## Primary workflows

### Build and qualify

**Preconditions:** Accepted initiative, locked inputs, selected matrix.

1. Build named targets and record exact identities.
2. Inspect contents, manifests, SBOM/provenance, licenses/findings, and continuity.
3. Run effective-config, hardening, clean-host, platform, isolation, and fault vectors.

**Success result:** One exact D2 artifact family has complete reviewable evidence.
**Failure result:** Affected artifact/claim is blocked; no mutable repair.

### Operate and upgrade

**Preconditions:** Exact release artifacts and compatible D3 resources.

1. Render/inspect configuration, initialize only through stopped maintenance,
   then start one API and verify boundaries.
2. Use safe stop/down that preserves volumes.
3. For upgrade, verify successor, stop/check/backup, migrate only under D3
   authority, smoke, and retain rollback identities.

**Success result:** Safe lifecycle preserves topology and state identity.
**Failure result:** Service remains stopped/unready or prior artifacts remain recoverable.

## Interfaces and integration

| Interface | Producer or caller | Consumer or handler | Compatibility rule |
|---|---|---|---|
| Named BuildKit targets | D2 build | D3–D6 packaging | Exact names, hashes, platforms, and source identity |
| Release Compose roles | Operator | Docker/containers | Fully rendered exact topology |
| Volume/network envelope | D2 Compose | D3 API/maintenance, D5 CLI, D6 browser origin | No alternate mount/network/state path |
| Artifact metadata | Release process | Reviewers/consumers | Digest/hash continuity and declared compatibility |

## Failure and recovery

| Failure | Detection | Durable effect | Recovery | Required evidence |
|---|---|---|---|---|
| Invalid/unknown config | Render/preflight | No ready service | Correct reviewed input | Negative config result |
| Digest/platform mismatch | Inspect/pull/build | Candidate blocked | Use verified immutable artifact | Manifest/provenance result |
| Ignored hardening/limit | Runtime probe | Host unsupported | Fix platform/product or remove claim | Per-host probe |
| API/maintenance overlap | Lock/topology test | Second owner fails | Stop and retry accepted role | Mutual-exclusion result |
| OOM/kill/daemon restart | Docker/health | Client outcome may be indeterminate | Verify lock/store/readiness before reuse | Fault/recovery result |
| Backup/upgrade failure | Maintenance result | No success; prior state retained | D3-governed recovery/rollback | Exact recovery evidence |

## Security and authorization

- **Trust boundary:** One local OS account, Docker daemon, exact loopback and private network.
- **Authentication:** No application authentication; inherited host/Docker control only.
- **Authorization:** Service/mount/network role confinement; no partial remote substitute.
- **Secrets:** None in images, config, commands, logs, health, or evidence.
- **Audit:** Bounded diagnostics and release evidence, not per-user audit.
- **Data handling:** Synthetic or externally documented de-identified data that also satisfies NIST restrictions.

## Observability and operations

| Signal or operation | Purpose | Required dimensions or safeguards |
|---|---|---|
| Rendered config inspection | Prove effective topology | Hash, ports, roles, mounts, security, limits |
| Image/manifest inspection | Prove identity/content | Digest, platform, labels, SBOM/provenance, findings |
| Health/readiness | Gate safe runtime | Coarse status; no sensitive paths/data |
| Lifecycle/recovery drill | Prove state-preserving operations | Exact artifacts, volumes, commands, outcomes |
| Runtime negative probes | Prove confinement and bounds | No socket/host/mount/network/privilege escape |

## Compatibility migration and rollout

Artifacts declare architecture/API/schema compatibility and exact platforms.
Upgrades are stopped-service, backup-first where state compatibility changes,
and preserve prior digests/volumes until rollback closes. No automatic
migration/downgrade, mutable patch, zero-downtime, or host-native fallback is
supported.

## Testing strategy

| Level | Behavior proved | Required environment or fixture |
|---|---|---|
| Static/build | Targets, locks, minimal contents, metadata | Clean BuildKit build and scans |
| Contract | Rendered roles/networks/mounts/config | Compose config and negative variants |
| Integration | Initialize/start/use/stop and artifact handoffs | Isolated named volumes and compatible stubs/products |
| Failure and recovery | Limits, kill/OOM, overlap, backup/rollback envelope | Supported host/OCI matrix with synthetic state |
| Acceptance | Complete D2 clean-host and policy claim | Exact released digest family |

## Risks and edge cases

| Risk or edge case | Impact | Mitigation or decision |
|---|---|---|
| Platform ignores Compose control | False hardening claim | Per-host runtime probes |
| Rebuilt wheel/bundle | Consumer mismatch | Hash continuity and substitution test |
| Test resolves live volume | Disclosure/corruption | Unique identities and negative resolution tests |
| Destructive command enters runbook | Irrecoverable loss | Exclusion review and explicit separate authority |
| Smoke test overclaims consumer | False completion | D2-only claim review |

## Deferred work

- D3–D6 semantics and conformance remain with their independent initiatives.
- Any independent platform subproduct identified by `PLT-06` re-enters Stage 0.

## Architecture and specification acceptance

Not accepted. Readiness requires explicit assumption review, accepted blocking
decisions, no split, exact source/destination/verification mapping, and a later
human lifecycle decision.

