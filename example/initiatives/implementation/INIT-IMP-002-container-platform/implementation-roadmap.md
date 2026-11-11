# Container platform and runtime packaging delivery roadmap

**Initiative:** Container platform and runtime packaging
**Status:** Proposed
**Last updated:** 2026-11-11
**Initiative type:** `implementation`

## Objective

Deliver one exact D2 platform artifact family and evidence without claiming
consumer-product behavior.

## Delivery scope

### Included

- Build/Compose/images/hardening/configuration/lifecycle/artifact identity.
- Clean-host, matrix, supply-chain, fault, isolation, recovery-envelope, and policy evidence.

### Excluded from this roadmap

- D3–D6 product semantics and regulated/remote/host-native operation.
- Specification changes or destructive-data automation.

## Type-specific delivery boundary

Implementation changes products only; a required specification change blocks
and routes to the owning design authority.

## Prerequisites

| Prerequisite | Required state | Evidence |
|---|---|---|
| Initiative | Explicitly Accepted | Future lifecycle receipt |
| Decisions/assumptions | Reviewed; blocking choices resolved | Receipts and reconciled records |
| Product scope | Paths/matrix/trust/evidence/split fixed | `PLT-01`–`PLT-06` |
| Sources | Exact architecture/security revisions | Source map and currency review |

## Phase summary

| Phase | Outcome | Depends on | Parallel work allowed |
|---|---|---|---|
| 0 | Accepted specification and D2 output boundary | None | No product work |
| 1 | Locked build graph and artifact identities | Phase 0 | Platform-specific builds from same inputs |
| 2 | Effective Compose, hardening, and safe lifecycle | Phase 1 | Independent negative probes on isolated projects |
| 3 | Cross-platform qualification and release evidence | Phases 1–2 | Matrix entries against same exact artifacts |

## Phase 0 - Accept the specifications and output boundary

### Objective

Resolve assumptions/decisions, verify mapping and no split, and accept only the
D2 product claim.

### Work

- Resolve blocking decisions and review assumptions.
- Confirm ownership, targets, topology, matrix, evidence, rollback, and handoffs.
- Map every authoritative requirement to a step and check.
- Verify tuple and migration reciprocity.

### Exit gate

- [ ] Assumptions and blocking decisions have explicit receipts.
- [ ] No mandatory split or hidden specification change remains.
- [ ] Initiative is explicitly Accepted.

## Phase 1 - Build immutable artifacts

### Objective

Create locked named targets and exact image/artifact identities.

### Work

- Implement multi-stage targets and minimal runtime contents.
- Lock inputs and record digests, SBOM/provenance, licenses/findings.
- Prove wheel/bundle hash continuity and multi-platform manifests.

### Exit gate

- [ ] Exact targets reproduce and runtime contents are minimal.
- [ ] Every claimed OCI platform has passing identity/provenance evidence.
- [ ] Mutable/substituted artifacts fail the release gate.

## Phase 2 - Compose topology and lifecycle

### Objective

Implement effective topology, hardening, isolation, configuration, health, and
safe lifecycle/recovery envelope.

### Work

- Implement services/profiles/network/volumes/ports/mounts/limits.
- Exercise initialize/start/use/stop/down/upgrade and maintenance exclusion.
- Run network, mount, privilege, resource, test-isolation, and destructive-command negatives.

### Exit gate

- [ ] Effective render and runtime match `ARC-CTR-008`.
- [ ] Ordinary lifecycle preserves volume identity and unsafe paths fail.
- [ ] Fault/restart results make no false state/product claim.

## Phase 3 - Outcome qualification

### Objective

Run complete D2 and policy gates on exact released artifacts.

### Work

- Execute all `CNT-*`, applicable `OPS-*`, and `E2E-009`.
- Complete supported-host/OCI, supply-chain, recovery, incident, and policy evidence.
- Reconcile limitations, nonpasses, docs, and handoffs.

### Exit gate

- [ ] Every mandatory matrix entry and D2 acceptance outcome passes.
- [ ] No unresolved blocker or unowned finding remains.
- [ ] Exact artifacts, evidence, and truthful lifecycle/status records agree.

## Rollout controls

| Control | Initial state | Enablement condition | Rollback or disable behavior |
|---|---|---|---|
| Release Compose use | Disabled | Exact render/artifacts pass D2 gate | Return to prior digest/config; preserve volumes |
| Consumer target handoff | Unavailable | Target/hash/compatibility evidence exists | Withdraw handoff without claiming consumer result |
| New platform claim | Unclaimed | Native/qualified evidence passes | Remove unsupported matrix claim |

## Release definition

Completion requires every phase and applicable architecture/NIST/HIPAA gate
for the same exact artifact family. This Proposed roadmap authorizes no release.

