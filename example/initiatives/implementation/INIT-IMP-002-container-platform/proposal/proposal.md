# Container platform and runtime packaging proposal

**Initiative:** Container platform and runtime packaging
**Proposal status:** Draft
**Revision:** 0.1
**Last updated:** 2026-11-11
**Owner:** User
**Initiative type:** `implementation`
**Work version:** `v2.0`
**Realization suite:** [`RZN-001-P2-PLATFORM-SUITE`](../../../../evidence/non-authoritative/realizations/v2.0/00-RZN-001-P2-PLATFORM-suite-index.md)
**Type requirements:** See [the initiative template](../README.md#initiative-type-and-output-boundary).

## Executive proposal

Propose one D2 implementation initiative for the container build graph, release
Compose topology, runtime packaging, artifact identity, platform hardening, and
safe lifecycle envelope required by architecture `2.0.1`. It supplies the
platform used by later products without implementing or claiming their
domain/API, SDK, CLI, or web behavior.

## Initiative type and permitted output

This `implementation` initiative may create platform products such as the
root BuildKit graph, Compose model, image targets, locks, release metadata, and
platform verification. It may not change accepted specifications or absorb
D3–D6 product semantics.

## Problem and evidence

The architecture fixes a Docker-only, loopback/private-network, named-volume,
hardened multi-stage platform and a D2 delivery gate, but no D2 product or
conformance evidence exists. `RZN-001-P2-PLATFORM-N01` preserves a bounded
candidate outcome and six unresolved implementation/release choices.

## Intended outcomes

1. One digest-identified, reproducible platform supplies the accepted API, CLI,
   maintenance, test, SDK-wheel, and web-build roles without host project tools.
2. Effective Compose, image, network, mount, user, capability, resource, health,
   and lifecycle behavior matches `ARC-CTR-008`.
3. D2 evidence proves only platform packaging and additive security gates,
   leaving every D3–D6 claim independent.

## Scope

### Included

- BuildKit stages, Compose services/profiles, private network, named volumes,
  immutable image/artifact identity, hardening, configuration, and safe
  lifecycle/recovery commands.
- D2 `CNT-*`, applicable `OPS-*`, `E2E-009`, supply-chain, supported-host,
  OCI-platform, policy, and negative-boundary evidence planning.

### Excluded

- Domain/API/SQLite behavior, SDK public behavior, CLI command semantics, web
  interaction/accessibility, or completion of D3–D6.
- Remote/public deployment, host-native fallback, real/possible ePHI,
  production use, destructive volume automation, or specification changes.

## Users and stakeholders

| Stakeholder or affected party | Need or responsibility | Expected change |
|---|---|---|
| Local operator | One safe Compose lifecycle | Uses exact release topology and preserves named volumes |
| D3–D6 owners | Stable platform/artifact handoffs | Consume exact targets and hashes without inheriting D2 completion |
| Security/release reviewer | Traceable hardened artifacts | Reviews render, digests, SBOM/provenance, findings, and matrix evidence |
| User, Sole Project Owner | Decide unresolved platform choices | Reviews six open decisions and later lifecycle gates |

## Terms

| Term | Meaning in this proposal |
|---|---|
| D2 | Container platform and runtime-packaging delivery unit |
| Effective Compose | Fully rendered configuration that governs runtime behavior |
| Release identity | Digest-qualified images plus source, manifest, wheel/bundle, Compose, and provenance identities |
| Maintenance role | Stopped-API, networkless, allowlisted one-shot state operation |

## Proposed direction

### Product behavior or placement

Implement the accepted multi-stage build and Compose graph at exact repository
paths selected by `PLT-01`. Runtime images remain minimal and immutable;
`record-api`, `record-cli`, `record-maintenance`, and isolated
`record-test` retain their exact roles and mounts.

### Domain and authority model

Architecture owns topology and behavior; security suites own use, safeguards,
and evidence. D2 owns build/release packaging only. Rendered Compose is runtime
authority; image/manifest/artifact hashes are release identity.

### System boundaries

The host supplies Docker/Compose and a supported browser, plus Git for source
development. No host Python, Node, SQLite, SDK, CLI, app service, proxy, or
native fallback is supported. Only the API port is published to IPv4 loopback.

### Primary workflows

1. Build and verify exact locked targets for supported OCI platforms.
2. Render and inspect Compose before initialization/start/use.
3. Exercise safe start, stop, upgrade, isolated test, backup/restore envelope,
   and negative network/mount/privilege/resource behavior.

### Data and lifecycle

Live state remains in `record-data`; backups remain in `record-backups`;
tests use fresh isolated volumes. Platform evidence uses purpose-created
synthetic data. Ordinary stop/down preserves volumes; destructive commands are
outside safe automation.

## Operational behavior

### Failure and recovery

Invalid config, unsupported security fields, digest/platform mismatch,
ownership/lock conflict, unsafe publication, resource failure, or recovery
failure blocks readiness/release and cannot be relabelled success. Recovery
uses exact prior artifacts and validated backups under the D3 persistence
contract without D2 claiming persistence correctness.

### Security and authorization

Containers use UID/GID 10001, read-only roots, bounded tmpfs/resources/logs,
all capabilities dropped, no-new-privileges, no socket/host namespace/device
access, and exact networks/mounts. The accepted local/non-ePHI profile and both
security evidence families remain additive.

### Observability

Evidence records rendered Compose hash, source and image/manifest identities,
host/OCI matrix, SBOM/provenance/license/vulnerability disposition, negative
runtime probes, limits, lifecycle results, limitations, reviewer, and time.

## Compatibility and transition

The initial platform binds architecture `2.0.1`, NIST/HIPAA `1.0.1`, and
exact consumer artifact interfaces. Upgrades preserve prior digests and state,
require check/backup and compatible migration where applicable, and make no
zero-downtime or automatic-downgrade claim.

## Alternatives considered

| Alternative | Benefit | Cost or reason not selected |
|---|---|---|
| Host-native toolchain | Faster ad hoc development | Violates Compose-only/no-host-services architecture |
| One monolithic runtime image | Fewer artifacts | Breaks role isolation and independent D3–D6 claims |
| Kubernetes or remote proxy | Broader deployment | Outside accepted local architecture and security profile |

## Risks and tradeoffs

| Risk or tradeoff | Impact | Mitigation or evidence needed |
|---|---|---|
| Effective render differs from source | Security/topology drift | Hash and inspect rendered config |
| Mutable/rebuilt artifacts | Tested bytes differ from release | Digest/hash continuity and substitution negatives |
| Test can resolve live volumes | User-state exposure | Isolated project/volume/network negatives |
| Host ignores controls | False supported-platform claim | Runtime probes on every claimed host |
| D2 smoke tests overclaim D3–D6 | Lifecycle/evidence collapse | Explicit gate boundaries and exact claim review |

## Assumptions requiring assumption

- One D2 platform artifact family can retain one owner, lifecycle, and
  independently reviewable platform claim.
- D2 can provide target and topology interfaces without claiming consumer
  behavior.
- The accepted Docker-only trust boundary and synthetic/de-identified-only use
  remain unchanged.

## Questions requiring decisions

- Which repository paths own D2 artifacts and release locks?
- Which Docker/Compose/BuildKit patch versions and registry trust roots form the
  first matrix?
- Which provenance/signature mechanism and trust root are selected?
- How are the native OCI and supported host/browser evidence environments
  provisioned?
- Where are machine-readable evidence, SBOMs, findings, and dispositions kept?
- Does any implementation sub-scope require a narrower initiative while
  retaining one D2 completion boundary?

## Acceptance outcomes

- Exact D2 artifacts pass all `CNT-*`, applicable `OPS-*`, `E2E-009`,
  clean-host, platform, supply-chain, recovery-envelope, and policy evidence
  gates for the claimed matrix.
- The platform exposes only accepted roles/interfaces, preserves state and
  destructive boundaries, and makes no D3–D6, production, regulated-use, or
  general compliance claim.

## References

- [Platform realization note](../../../../evidence/non-authoritative/realizations/v2.0/01-RZN-001-P2-PLATFORM-v2.0-container-platform.md) — primary non-authoritative proposal input.
- [`ADR-004`](../../../../evidence/authoritative/architecture/07-ADR-004-container-only-deployment-trust-model.md), [`ADR-005`](../../../../evidence/authoritative/architecture/08-ADR-005-containerized-technology-stack.md), and [`ARC-CTR-008`](../../../../evidence/authoritative/architecture/23-operations-security-contract.md) — binding platform contracts.
- [`ARC-CTR-009`](../../../../evidence/authoritative/architecture/24-conformance-contract.md), NIST `1.0.1`, and HIPAA `1.0.1` — exact qualification and security gates.

## Revision history

| Revision | Date | Owner | Change |
|---|---|---|---|
| 0.1 | 2026-11-11 | User | Initial D2 proposal; all six implementation choices remain open |

