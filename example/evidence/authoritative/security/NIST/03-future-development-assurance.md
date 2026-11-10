# Future development assurance and evidence standard

**Standard ID:** `SEC-NIST-VER-001`  
**Revision:** `1.0.0`  
**Status:** Accepted prospective standard  
**Owner and accepting authority:** User, project authority  
**Effective date:** 2026-11-10  
**Governing suite:** [`SEC-NIST-SUITE-001`](00-nist-security-policy-suite-index.md)  
**Primary design evidence:** [`ARC-SUITE-001@2.0.0`](../../architecture/00-architecture-suite-index.md)  

## Purpose and non-assessment statement

This standard tells future developers and reviewers what assurance evidence
must accompany an implementation of
[`SEC-NIST-POL-001`](01-demonstrator-security-policy.md). It derives the
expected evidence from the accepted architecture conformance contract and uses
the assessment-method vocabulary of NIST SP 800-53A Rev. 5.

This document does **not** assess the existing demonstrator. No source tree,
container, configuration, test, scan, backup, recovery operation, or release
has been assigned a result by this security suite. Every implementation result
therefore begins as **Not assessed**. Future evidence may change a result only
through the process below.

## Assurance principles

- The architecture and security policy specify required future behavior; they
  are not proof that behavior exists.
- Evidence must address the exact product version, source commit, artifact
  digest, Compose render, platform, data/schema version, and policy claim.
- Architecture conformance evidence should be reused rather than duplicated
  when it is current, exact, and independently reviewable.
- A document, source inspection, build, scanner result, health response, unit
  test, screenshot, or demonstration proves only what its method can observe.
- Required negative paths and failure behavior are evidence, not optional
  robustness work.
- Missing, skipped, stale, substituted, or scope-mismatched evidence remains
  visible and cannot be converted to a satisfied result.
- A risk decision may disposition an allowed residual risk; it cannot establish
  behavior that was not observed or waive an architecture invariant.

## Future assessment methods

The following tailored methods use NIST SP 800-53A's `EXAMINE`, `TEST`, and
`INTERVIEW` method types. They do not assert that the full SP 800-53A objective
for every cited SP 800-53 control has been performed.

| Method | Future use in this profile | Limitation |
|---|---|---|
| `EXAMINE` | Inspect accepted requirements, traceability, source/configuration, rendered Compose, dependency and route inventories, immutable identities, scan reports, logs, SBOM, provenance, runbooks, decisions, and preserved outputs | Cannot establish runtime behavior merely because a setting or requirement is present |
| `TEST` | Exercise the exact containerized artifact and boundary with normal, negative, adversarial, fault, resource, concurrency, recovery, and cross-surface cases; compare observed and required outcomes | Proves only the tested artifact, environment, platform, condition, and claim |
| `INTERVIEW` or witnessed demonstration | Confirm that a named owner understands and can execute a human-operated release, backup, recovery, incident, or exception procedure | Cannot replace artifact inspection or automated/runtime testing where the policy requires technical enforcement |

Method depth and coverage must be sufficient for the claim and risk. The
minimum architecture layers, vectors, delivery gates, and evidence fields are
defined by
[`ARC-CTR-009`](../../architecture/24-conformance-contract.md). This standard
adds security-policy traceability; it does not weaken that contract.

## Result model for future work

| Result | Meaning |
|---|---|
| `Not assessed` | Default. No reviewed, exact evidence establishes a result; this is not a pass or a failure finding |
| `Satisfied` | Required methods produced exact evidence and a named reviewer found the project policy requirement met for the stated scope |
| `Not satisfied` | Evidence shows a required outcome is absent, contradicted, or fails under a required condition |
| `Not applicable` | An explicit disposition in `SEC-NIST-MAP-001` excludes the requirement for the exact scope; convenience or missing implementation is not a basis |
| `Exception pending` | A bounded request under `SEC-POL-14` exists but has not received effective authority; the dependent claim remains open |
| `Exception accepted` | Named human authority accepted a time-bounded residual risk that the architecture permits; the record is not evidence that the underlying behavior is satisfied |

An evidence report must keep the result, limitation, and disposition separate.
No result in this table is assigned to current work by publishing this standard.

## Policy-to-evidence requirements

The vector IDs below are required future evidence anchors from `ARC-CTR-009`.
They are not results and do not assert that a test exists or passes.

| Policy | Minimum future examination | Minimum future test or demonstration anchors |
|---|---|---|
| `SEC-POL-01` | Examine approved use/data statement, operator guidance, product claims, architecture version, and inventory of routes, commands, UI actions, and schema | `E2E-007` excluded-capability inventory; demonstrate that delivery documentation forbids production, regulated, remote, and multi-user use |
| `SEC-POL-02` | Examine rendered Compose network/port topology, Host/Origin configuration, route inventory, and absence of proxy/CORS/auth substitutes | `CNT-002/003/014`, `OPS-002/003/009`, and `E2E-008/010`; reachability and negative boundary tests must include undeclared interfaces and services |
| `SEC-POL-03` | Examine image metadata/content, service user, capabilities, namespaces, mounts, networks, tmpfs, resource bounds, and absence of secrets/Docker socket | `CNT-004/005/006/007/015` and `OPS-001`; runtime probes must exercise forbidden writes, privileges, namespaces, mounts, devices, and resource excess |
| `SEC-POL-04` | Examine reviewed source and rendered Compose, digest-qualified images, accepted inputs, unknown-input rejection, Git traceability, and compatibility/change decisions | `CNT-002/009/012` and `OPS-001/004/010/013`; substitute mutable, unknown, unsafe, and destructive configurations and observe fail-closed behavior |
| `SEC-POL-05` | Examine SQLite ownership, lock, schema, migrations, fixed SQL, transaction boundaries, volume identity, and maintenance allowlist | `DOM-012`, `HTTP-003/004/010/012`, `DB-002/003/005/006/007/010`, and `CNT-004/011/015`; include races, I/O faults, corruption, overlap, and direct-update attempts |
| `SEC-POL-06` | Examine validators, parsers, SQL construction, RE2 integration, browser sinks, CSP/security headers, error schemas, and redaction rules | `DOM-003/007/008/009`, `HTTP-005/009/010`, `SRCH-011/012/014/017`, `WEB-008/009/012`, and `OPS-002/009`; use malformed, oversized, injection, XSS, control-character, and disclosure fixtures |
| `SEC-POL-07` | Examine all architecture limit values and enforcement locations across app, Compose, and Docker logging | `SRCH-017`, `CNT-006`, and `OPS-006/007`; exceed admission, CPU, memory, PID, tmpfs, body/header, worker, deadline, search, and log limits and verify safe restart |
| `SEC-POL-08` | Examine event schema, log driver/rotation, all log levels, diagnostic destinations, telemetry/storage inventory, and incident preservation procedure | `CLI-009`, `WEB-009`, and `OPS-008`; inspect output for required fields and prohibited data under success, validation, fault, and sensitive fixtures |
| `SEC-POL-09` | Examine backup/restore formats, hashes, metadata, overwrite protection, locks, runbooks, host-loss statement, export decision, and exact artifact identity | `DB-008/009`, `CNT-010/011/012/015`, `OPS-011/012/013`, and `E2E-006`; inject interruption, invalid artifacts, smoke failure, and rollback conditions |
| `SEC-POL-10` | Examine lock files, source identities, BuildKit graph, image contents, digests/manifests, wheel/bundle hashes, SBOM, provenance, license/secret/vulnerability reports, and finding dispositions | `CNT-007/008/009` and `OPS-010`; rebuild and substitution tests must demonstrate artifact continuity on every claimed OCI platform |
| `SEC-POL-11` | Examine requirement-to-policy/architecture/vector traceability, review/static-analysis records, test design, exact environment, limitations, skips, and reviewer identity | All applicable `ARC-CTR-009` verification layers and delivery gates `D1` through `D6`; required negative, fault, recovery, platform, and browser entries may not be silently skipped |
| `SEC-POL-12` | Examine supported-component inventory, monitoring sources, dated findings, applicability/reachability analysis, owner, remediation/disposition, rebuilt digest, root cause, and regression updates | Re-run applicable security/regression vectors and `OPS-010` against the remediated immutable artifacts; demonstrate that a material unresolved finding keeps the dependent claim open |
| `SEC-POL-13` | Examine the local incident runbook, detection criteria, evidence manifest, chain of custody, containment record, recovery source, hashes, lessons learned, and external-responsibility boundary | Witness a tabletop or controlled local drill using `DB-010`, `OPS-007/008/012`, and applicable recovery smoke vectors; do not damage or substitute real evidence |
| `SEC-POL-14` | Examine every exception/expansion record for exact policy and architecture IDs, scope, risk, owner, authority, dates, compensating measures, evidence, and review outcome | Demonstrate that an expired, unauthorized, invariant-conflicting, or trigger-crossing request cannot support a release or conformance claim |

## Evidence record schema

Each future assessment record must preserve the fields required by
`ARC-CTR-009` without weakening or renaming their meaning:

| Field | Required future content |
|---|---|
| Evidence ID | Stable initiative- or product-scoped identifier |
| Architecture and policy | `ARC-SUITE-001@2.0.0`, `SEC-NIST-SUITE-001@1.0.0`, and exact policy/vector IDs |
| Product | D1-D6 unit, semantic version, source Git commit, and OCI/wheel/bundle/Compose artifact hashes |
| Environment | Host OS/architecture; Docker, Desktop, Compose, and BuildKit versions; platform/image digests; rendered Compose hash; relevant runtime/browser/database/dependency versions; test-volume identities; schema/migrations |
| Method | `EXAMINE`, `TEST`, or `INTERVIEW`; exact containerized command, target, profile, configuration, fixture seed, and static/mock/live/end-to-end/native-or-qualified-platform classification |
| Time | Start and end in UTC plus duration |
| Results | Total/satisfied/not-satisfied/not-assessed/skipped counts, per-policy and per-vector mapping, and output/artifact location |
| Limitations | Missing environment, nondeterminism, untested branch, scanner limits, scope mismatch, or unavailable required platform/browser |
| Disposition | Owner plus linked defect, conflict, exception, or decision for every non-satisfied, skipped, or limited item |
| Reviewer | Human or automation identity, review role, review date, and approval boundary |

Evidence should be immutable or content-addressed where practical. Records
containing demonstration data, logs, scan detail, or backup metadata must be
protected according to `SEC-POL-08` and `SEC-POL-09`.

## Future claim gate

A future release may use the narrow conformance wording in
`SEC-NIST-POL-001` only when:

1. every applicable policy is `Satisfied`, or an allowed residual risk has an
   effective `Exception accepted` record that does not contradict architecture;
2. all applicable architecture delivery gates and mandatory matrix entries are
   satisfied by evidence for the exact released artifacts;
3. every non-satisfied, skipped, stale, missing, substituted, and limited item
   remains visible and is resolved or prevents the dependent claim;
4. a named reviewer confirms that the evidence supports only the stated local,
   single-user demonstrator scope; and
5. the release avoids all certification, authorization, FISMA, full-control,
   or general NIST-compliance language prohibited by the governing policy.

Publishing this prospective gate does not open or close any gate for the
existing application. Current implementation status remains **Not assessed**.
