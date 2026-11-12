# Standalone CLI image proposal

**Initiative:** Standalone CLI image

**Proposal status:** Draft

**Revision:** 0.1

**Last updated:** 2026-11-11

**Owner:** User

**Initiative type:** `implementation`

**Work version:** `v3.0`

**Realization suite:** [`RZN-001-P3-CLI-SUITE`](../../../../../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md)

**Type requirements:** See [the initiative skeleton](../README.md).

## Executive proposal

Create one one-shot Compose CLI image that uses only the D4 public wheel to
call the fixed private D3 endpoint `record-api:8000/api/v1`. It provides
predictable commands, human and JSON output, stable exit codes, help and
completion, with no host mounts, ports, Docker socket, direct HTTP layer, or
SQLite access. Exact destinations, libraries, versions, seams, and owners stay
open.

## Initiative type and permitted output

This implementation initiative may eventually deliver CLI source, help and
completion assets, one immutable image, metadata, and D5 evidence. It cannot
deliver D2-D4 or D6 outcomes.

## Problem and evidence

Authoritative CLI contracts exist but no governed D5 artifact does. The v3.0
realization suite is planning evidence only and cannot create requirements,
acceptance, or conformance.

## Intended outcomes

- A one-shot non-interactive-capable CLI image using the exact D4 public wheel.
- Deterministic parsing, output, prompts, JSON, exit codes, signals, and pipes.
- Fixed private API targeting with no direct HTTP or SQLite implementation.
- Safe diagnostics and explicit handling of partial/indeterminate outcomes.
- CLI-001 through CLI-011 and applicable contract/security evidence.

## Scope

### Included

Commands, parsing, validation, help/completion, human/JSON rendering, exit
mapping, prompts, signals/broken pipes, image packaging, compatibility, and D5
verification.

### Excluded

Direct HTTP/SQLite access, internal SDK imports, mounts/ports/Docker socket,
long-running service behavior, D2-D4 or D6 delivery, production/regulated use,
actual or possible ePHI, and unresolved destinations/tools.

## Users and stakeholders

Local operators invoke the image through Compose. Automation consumes JSON and
exit codes. Owners/reviewers govern lifecycle, usability, safety, compatibility,
security, and evidence.

## Terms

- **D5:** the standalone CLI artifact family from ADR-007.
- **One-shot:** one invocation performs one bounded command then exits.
- **Human output:** stable readable output for an operator.
- **JSON output:** machine-readable schema with diagnostics kept separate.

## Proposed direction

### Product behavior or placement

Deliver one immutable CLI image. Exact source, help/completion, image, metadata,
and evidence paths remain open under `CLI-01`.

### Domain and authority model

Use only public D4 models/methods/exceptions. Preserve authoritative command,
output, error, and process behavior without duplicating API/domain logic.

### System boundaries

Run in D2 Compose, target only the fixed private D3 URL, use the exact D4 wheel,
and expose no host path, port, socket, or direct persistence boundary.

### Primary workflows

Show help/version/completion; validate arguments; dispatch SDK operations;
render human or JSON output; map errors and partial outcomes; handle signals
and broken pipes; exit deterministically.

### Data and lifecycle

Keep command data in memory only, emit record content only as explicit success
output for permitted synthetic/de-identified data, and redact diagnostics.

## Operational behavior

### Failure and recovery

Parse/validation failure, unavailable API, SDK exception, timeout, cancellation,
pre/post-dispatch interruption, broken pipe, rendering failure, and
indeterminate write outcome must map to bounded output and exit behavior.

### Security and authorization

Use fixed private targeting, least-privilege image/runtime, locked dependencies,
safe terminal rendering, redacted diagnostics, and no remote/production or
regulated data use.

### Observability

Diagnostics go to the defined stream, remain bounded, and never leak secrets,
payloads, host paths, or unsafe control sequences.

## Compatibility and transition

D5 depends on exact D2, D3, and D4 artifacts. CLI semantic versioning is
separate from suite v3.0 and needs an explicit compatibility policy.

## Alternatives considered

Host-installed CLI, direct HTTP, direct SQLite, Docker-socket control, and a
long-running CLI service conflict with boundaries. Multiple D5 artifacts are
not justified; `CLI-06` retains evidence-based split review.

## Risks and tradeoffs

Risks include parser ambiguity, unstable output, secret/payload leakage,
terminal injection, wrong exit codes, duplicated SDK logic, unsafe signal
handling, and compatibility overclaims.

## Assumptions requiring assumption

Initial assumptions cover one D5 image, exclusive D4 public-wheel use, fixed
private API, no mounts/ports/socket, safe data/output, and blocking evidence
gaps. Stage 3 records them as unconfirmed.

## Questions requiring decisions

- `CLI-01`: exact source, help/completion, image, metadata, and evidence paths.
- `CLI-02`: parser/formatting libraries and dependency patch locks.
- `CLI-03`: CLI semantic version and compatibility policy.
- `CLI-04`: process-level pre/post-dispatch, signal, pipe, and entrypoint faults.
- `CLI-05`: risk, vulnerability, license, output, incident, and evidence owner.
- `CLI-06`: whether completion/automation integration requires a split.

All remain open.

## Acceptance outcomes

A later human review may assess whether D5 is narrow, traceable, safe, usable,
and testable. Artifact acceptance/conformance require later authority/evidence.

## References

- [Architecture suite](../../../../../evidence/authoritative/architecture/00-architecture-suite-index.md)
- [ADR-007](../../../../../evidence/authoritative/architecture/10-ADR-007-product-and-delivery-decomposition.md)
- [CLI boundary](../../../../../evidence/authoritative/architecture/19-cli-boundary.md)
- [CLI contract](../../../../../evidence/authoritative/architecture/20-cli-interaction-contract.md)
- [Operations/security](../../../../../evidence/authoritative/architecture/23-operations-security-contract.md)
- [Conformance](../../../../../evidence/authoritative/architecture/24-conformance-contract.md)
- [NIST suite](../../../../../evidence/authoritative/security/NIST/00-nist-security-policy-suite-index.md)
- [HIPAA-aligned suite](../../../../../evidence/authoritative/security/HIPPA/00-hipaa-security-policy-suite-index.md)
- [v3.0 suite](../../../../../evidence/non-authoritative/realizations/v3.0/00-RZN-001-P3-CLI-suite-index.md)

## Revision history

| Revision | Date | Change | Authority |
|---|---|---|---|
| 0.1 | 2026-11-11 | Initial D5 proposal; implementation choices remain open | User prompt and cited evidence |
