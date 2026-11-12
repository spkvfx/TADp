# Python SDK artifact delivery steps

**Initiative:** `INIT-IMP-004`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Current-state analysis

Contracts and realization notes exist; governed SDK source, wheel, metadata,
docs, and D4 qualification do not.

## Delivery strategy

Build the strict public surface, private transport, package, live compatibility,
then qualify one exact wheel. Later lifecycle authority is required.

## Step 1 - Establish source and package graph

### Objective

Create the authorized D4 structure and reproducible build.

### Expected output locations

Open under `SDK-01`.

### Planned output

Package skeleton, locked inputs, build metadata, public namespace, evidence ID.

### Dependencies

`SDK-01`, `SDK-02`, `SDK-06` and D2 build target.

### Evidence / authoritative

SDK boundary/contract, ADR-007, conformance, security suites.

### Migration and rollback

No data migration; immutable wheel identities permit package fallback.

### Verification

Reproducible wheel build, metadata/content inspection, provenance, scans.

### Acceptance

Later review only.

## Step 2 - Implement public behavior and transport

### Objective

Implement strict models, methods, exceptions, URL policy, and private transport.

### Expected output locations

Authorized D4 paths.

### Planned output

Models, client, error mapping, pagination/search/navigation, timeouts,
cancellation, cleanup, and eligible read retry.

### Dependencies

Step 1, `SDK-03`, `SDK-04`, compatible D3 contract.

### Evidence / authoritative

SDK/HTTP contracts and SDK-001..SDK-008 plus applicable vectors.

### Migration and rollback

Public changes follow compatibility policy; internal transport stays private.

### Verification

Model/property, URL, mock, fault, retry, write-no-retry, exception, cleanup tests.

### Acceptance

Exact public outcomes pass for the candidate wheel.

## Step 3 - Complete docs and compatibility

### Objective

Prove typing/docs/public surface and compatible mock/live behavior.

### Expected output locations

Authorized docs/examples/evidence paths.

### Planned output

Typed surface, reference docs, safe examples, compatibility matrix/diff,
live-D3 results, vulnerability/license records.

### Dependencies

Step 2 and `SDK-02` through `SDK-05`.

### Evidence / authoritative

D4 conformance and security/data-use policies.

### Migration and rollback

Identify previous compatible wheel and retirement/rollback conditions.

### Verification

Typing, docs, public diff, install/import, mock/live, leak, scan, matrix checks.

### Acceptance

No critical finding or unsupported compatibility claim.

## Step 4 - Qualify D4 outcome

### Objective

Produce an artifact-bound D4 conformance record.

### Expected output locations

Authorized product and evidence records.

### Planned output

Evidence manifest, matrix, source-currency/risk review, release disposition,
and human review packet.

### Dependencies

Steps 1-3 and all blocking decisions.

### Evidence / authoritative

Conformance contract and initiative source mapping.

### Migration and rollback

Document compatibility retirement, fallback, and evidence invalidation.

### Verification

Fresh install, public behavior, faults, compatibility, security, and E2E matrix.

### Acceptance

Only later explicit human authority can advance lifecycle or accept the product.

## Validation matrix

| Area | Required evidence | Blocking gap |
|---|---|---|
| Public API | SDK vectors and typing/docs | Semantic or public drift |
| Transport/failure | URL, timeout, retry, exception tests | Unsafe or ambiguous behavior |
| Packaging | Reproducibility and inspection | Mutable/untraceable wheel |
| Compatibility | Mock/live D3 matrix | Unsupported server pairing |
| Security/data | Scans and leak/data review | Secret, payload, ePHI, dependency risk |
| Boundary | D4 manifest | Reliance on D5 completion |

## Final acceptance criteria

All binding requirements map to passing wheel-specific evidence; decisions and
products have authority; tracking records are coherent; no D3 or D5 completion
is inferred. This file records planning only.
