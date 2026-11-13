# Standalone CLI image delivery steps

**Initiative:** `INIT-IMP-005`
**Status:** Proposed planning only
**Last updated:** 2026-11-11

## Current-state analysis

Contracts and notes exist; governed CLI source/image and D5 evidence do not.

## Delivery strategy

Build interaction core, image/process envelope, compatible live behavior, then
qualify one exact image after later authority.

## Step 1 - Establish source and image graph

### Objective

Create authorized D5 structure and reproducible locked build.

### Expected output locations

Open under `CLI-01`.

### Planned output

CLI skeleton, locked stack/wheel, image definition, help/completion lineage,
artifact/evidence identity.

### Dependencies

`CLI-01`, `CLI-02`, `CLI-06` and exact D2-D4 interfaces.

### Evidence / authoritative

CLI boundary/contract, ADR-007, conformance, security suites.

### Migration and rollback

No data migration; immutable image fallback.

### Verification

Reproducible build, contents/provenance, non-root startup, scans.

### Acceptance

Later review only.

## Step 2 - Implement commands output and exits

### Objective

Implement parser, validation, public-SDK dispatch, rendering, and exit mapping.

### Expected output locations

Authorized D5 paths.

### Planned output

Commands, help, human/JSON renderers, diagnostics, exit taxonomy, safe prompts.

### Dependencies

Step 1 and `CLI-02`, `CLI-03`.

### Evidence / authoritative

CLI contract and CLI-001..CLI-008.

### Migration and rollback

Public changes obey semantic policy and retain migration notes.

### Verification

Parser/property, golden output, JSON schema, terminal, stream, and exit tests.

### Acceptance

Exact interaction outcomes pass for candidate image.

## Step 3 - Implement process and fault envelope

### Objective

Handle signals, pipes, timeouts, pre/post-dispatch faults, and Compose failures.

### Expected output locations

Authorized runtime/test/evidence paths.

### Planned output

Process harness, interruption/ambiguity behavior, cleanup, compatibility matrix,
safe diagnostics.

### Dependencies

Step 2 and `CLI-04`, `CLI-05`.

### Evidence / authoritative

CLI/operations contracts, CLI-009..CLI-011, security policies.

### Migration and rollback

Define fallback and indeterminate write handling by immutable artifact.

### Verification

Signal, broken pipe, non-TTY, entrypoint, API/SDK fault, leak, and live tests.

### Acceptance

No critical issue or unsupported process/compatibility claim.

## Step 4 - Qualify D5 outcome

### Objective

Produce artifact-bound D5 conformance record.

### Expected output locations

Authorized product/evidence records.

### Planned output

Manifest, matrix, source/risk/license review, release disposition, review packet.

### Dependencies

Steps 1-3 and all blocking decisions.

### Evidence / authoritative

Conformance and source mapping.

### Migration and rollback

Record fallback, compatibility retirement, and evidence invalidation.

### Verification

Clean Compose invocation, interaction/process/security/E2E matrix.

### Acceptance

Only later explicit human authority advances lifecycle/accepts product.

## Validation matrix

| Area | Required evidence | Blocking gap |
|---|---|---|
| Commands/help | CLI-001..CLI-004 | Ambiguity or drift |
| Output/exits | CLI-005..CLI-008, schemas/golden | Unsafe or unstable surface |
| Process | CLI-009..CLI-011, fault harness | Signal/pipe/ambiguity gap |
| Artifact | reproducibility/scan/Compose | Mutable or privileged image |
| Compatibility | exact D2-D4 live matrix | Unsupported pairing |
| Security/data | terminal/leak/risk review | Secret/content/ePHI risk |

## Final acceptance criteria

Binding outcomes map to passing image-specific evidence; decisions/products
have authority; no predecessor or D6 completion is inferred. Planning only.
