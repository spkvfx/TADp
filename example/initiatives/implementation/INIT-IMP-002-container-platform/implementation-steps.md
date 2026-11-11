# Container platform and runtime packaging delivery steps

**Initiative:** Container platform and runtime packaging
**Status:** Proposed
**Last updated:** 2026-11-11
**Initiative type:** `implementation`

## Current-state analysis

| Path or system | Current behavior | Planned use or change | Evidence |
|---|---|---|---|
| Product paths | Not selected | Create accepted build/Compose/release paths | `PLT-01` |
| Architecture/security | Binding future requirements | Read-only product authority | Suites `2.0.1` / `1.0.1` |
| D3–D6 products | No evidence supplied | Consume only exact future handoffs | `ARC-CTR-009` current status |

## Delivery strategy

Implement products in dependency order: locked inputs/targets, effective
topology, then lifecycle and matrix qualification. Preserve state identities
and pair irreversible boundaries with explicit rollback limits.

## Step 1 - Create locked build and artifact graph

### Objective

Produce named targets and immutable artifact identities from reviewed inputs.

### Expected output locations

- Paths accepted by `PLT-01`
- Evidence destination accepted by `PLT-05`

### Planned output

- BuildKit stages for SDK wheel, web build, API, CLI, and test roles.
- Minimal runtime images, lock inputs, manifests, SBOM/provenance, and hash continuity.
- Failures on mutable/substituted/unsupported inputs.

### Dependencies

- Accepted `PLT-01`–`PLT-04` and reviewed assumptions.

### Evidence / authoritative

- `ADR-005`, `CNT-007`–`009`, `OPS-010`.
- `SEC-POL-04/10/12`, `HSP-009/013/014`.

### Migration and rollback

- **Migration or backfill:** New artifact graph; no existing release is rewritten.
- **Mixed-version behavior:** Only declared compatible exact hashes are assembled.
- **Rollback:** Retain and restore prior digest identities; never patch runtime.

### Verification

- Reproducible builds, content/layer scans, manifest/platform and substitution tests.
- Artifact hash continuity and locked dependency/license/vulnerability review.

### Acceptance

- Exact targets and bytes are traceable and minimal.
- Every claimed platform/identity has evidence.

## Step 2 - Implement effective Compose and hardening

### Objective

Create the accepted services, private network, volumes, ports, mounts,
configuration, limits, and runtime controls.

### Expected output locations

- Accepted Compose/configuration paths
- Image/runtime configuration from Step 1

### Planned output

- Exact API/CLI/maintenance/test roles and profiles.
- Loopback-only ingress, private network, separate volumes, no alternate mounts.
- UID/GID, read-only roots, tmpfs, capabilities, namespaces, limits, and health.

### Dependencies

- Step 1 images and accepted topology decisions.

### Evidence / authoritative

- `ADR-004`, `ARC-CTR-008`, `CNT-002`–`006`, `CNT-011/015`.
- `SEC-POL-02/03/07`, `HSP-004/005/009`.

### Migration and rollback

- **Migration or backfill:** New rendered configuration; no state mutation.
- **Mixed-version behavior:** Only declared compatible image/config identities start.
- **Rollback:** Stop candidate and use prior reviewed render/digests while preserving volumes.

### Verification

- Render inspection and Host/Origin/network/mount/privilege/resource negatives.
- Health/readiness, ignored-control detection, and one-owner/one-replica tests.

### Acceptance

- Effective runtime exactly matches the accepted topology/hardening.
- Prohibited path or ignored required setting prevents support/release.

## Step 3 - Implement lifecycle and isolation envelope

### Objective

Provide safe clean-host, initialization/start/stop/update/test/recovery-envelope
workflows without owning D3 state semantics.

### Expected output locations

- Accepted operator/runbook product paths
- Compose profiles and evidence configuration

### Planned output

- Preflight, start/use/stop/down, upgrade/rollback, isolated test, and maintenance commands.
- Volume-preserving ordinary lifecycle and conspicuous destructive boundaries.
- Exact consumer handoff metadata.

### Dependencies

- Steps 1–2 and compatible D3 resources for integration evidence.

### Evidence / authoritative

- `ARC-CTR-008` lifecycle, `CNT-001/010`–`015`, `OPS-004/011`–`013`.
- `SEC-POL-09/13`, `HSP-010/011/012`.

### Migration and rollback

- **Migration or backfill:** State migration remains D3-owned and backup-first.
- **Mixed-version behavior:** Refuse undeclared image/schema/config combinations.
- **Rollback:** Preserve prior digests/volumes and use validated D3 recovery path.

### Verification

- Clean-host workflow, test/live isolation, API/maintenance exclusion, volume preservation.
- Kill/OOM/daemon/recovery-envelope and destructive-command inventory tests.

### Acceptance

- Safe lifecycle makes no false state or consumer-behavior claim.
- Ordinary operations preserve state identities and unsafe paths fail.

## Step 4 - Qualify the D2 outcome

### Objective

Run the full platform, matrix, security, supply-chain, and claim gates.

### Expected output locations

- Exact release artifacts from Steps 1–3
- Evidence destination selected by `PLT-05`

### Planned output

- Per-vector/matrix/policy results and limitations.
- Release identity and consumer handoff manifest.
- Completion evidence only if every gate passes.

### Dependencies

- Steps 1–3 and no open blocker/split.

### Evidence / authoritative

- Full D2 gate in `ARC-CTR-009`.
- `SEC-NIST-VER-001` and `SEC-HIPAA-DEV-001`.

### Migration and rollback

- **Migration or backfill:** Release exact new D2 artifact family.
- **Mixed-version behavior:** Unsupported combinations remain unclaimed.
- **Rollback:** Withdraw candidate and retain prior artifacts/evidence/volumes.

### Verification

- All `CNT-*`, applicable `OPS-*`, `E2E-009`, and exact policy checks.
- Cross-check source, render, image, manifest, wheel/bundle, host, OCI, and evidence identities.

### Acceptance

- Exact artifact family passes every mandatory claimed gate.
- Status changes only through later authorized finalization.

## Validation matrix

| Requirement or authoritative evidence | Step | Verification | Evidence location |
|---|---|---|---|
| `ADR-005` build/release identity | 1 | Build, contents, manifest, provenance, continuity | Future secure build/release record |
| `ADR-004` / `ARC-CTR-008` topology | 2 | Render/runtime negative and hardening probes | Future platform evidence |
| Volume/lifecycle/recovery envelope | 2, 3 | Isolation, preservation, mutual exclusion, fault drills | Future operations evidence |
| `ARC-CTR-009` D2 gate | 1–4 | `CNT-*`, applicable `OPS-*`, `E2E-009` | Future qualification record |
| NIST/HIPAA suites | 1–4 | Exact policy applicability and evidence | Future security evidence |

## Final acceptance criteria

- [ ] Every step and exact verification passes.
- [ ] Every authoritative requirement maps to product and evidence.
- [ ] Upgrade, rollback limits, restart, isolation, and recovery envelope are exercised.
- [ ] Security/supply-chain/host findings are resolved within authority.
- [ ] Operator and consumer documentation states exact behavior and limits.
- [ ] Canonical tuple remains reciprocal.
- [ ] Status, index, artifacts, and completion evidence agree.

