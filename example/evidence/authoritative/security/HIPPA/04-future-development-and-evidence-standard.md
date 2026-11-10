# Future HIPAA-aligned development and evidence standard

**Standard ID:** `SEC-HIPAA-DEV-001`  
**Revision:** `1.0.1`  
**Status:** Accepted prospective development standard  
**Governing policy:** [`SEC-HIPAA-POL-001`](02-prospective-security-policy.md)  
**Architecture input:** [`ARC-SUITE-001@2.0.1`](../../architecture/00-architecture-suite-index.md)  
**Applies to:** Future delivery units `D2`-`D6` and their governing initiatives  

## Purpose

This standard defines the records and verification that future development
must plan and produce before claiming conformance to the security policy. It
does not execute those checks, inspect an implementation, create or accept an
initiative, or record any current pass/fail result.

The architecture conformance contract remains the product-behavior oracle.
This standard adds policy-specific evidence and claim controls; it does not
replace an `ARC-CTR-009` vector or lower its expected result.

## Workflow integration

### Proposal and alignment

A future proposal affecting `D2`-`D6` must:

1. identify the exact delivery unit, architecture revision, and affected
   `HSP-*` policies;
2. state that the accepted profile permits only synthetic or documented
   de-identified data;
3. classify every intended data path, fixture, output, log, backup, and
   external service;
4. identify the security owner and the risk-analysis owner;
5. record every architecture-declared limitation without proposing a product
   convenience as an exception; and
6. route any ePHI, multi-user, remote, shared-workstation, or third-party
   processing premise to `SEC-HIPAA-GATE-001` before product work.

It must also map the change to the applicable requirements of
[`SEC-NIST-SUITE-001@1.0.1`](../NIST/00-nist-security-policy-suite-index.md).
The two mappings may share evidence only when the artifact, environment,
method, and expected outcome are exact for both claims.

### Initiative creation and acceptance

The complete initiative specification must contain or precisely link:

- a policy applicability matrix covering `HSP-001` through `HSP-015`;
- the data-provenance and fixture plan;
- an application-specific risk analysis and addressable-control decisions;
- the security architecture/data-flow/threat boundary for the exact change;
- owned product destinations and negative boundaries;
- policy-specific acceptance criteria and verification methods;
- incident, recovery, compatibility, migration, and documentation effects;
- unresolved questions and assumptions requiring human disposition; and
- a bounded acceptance claim that does not include HIPAA compliance or ePHI
  authorization.

Human acceptance of an initiative does not prove that a control is
implemented. It authorizes only the future work and evidence named by that
initiative.

### Implementation or design delivery

Future delivery must:

- implement only the accepted, architecture-compatible policy scope;
- preserve safe synthetic fixtures and prevent record data from entering
  source, build, test, diagnostic, and collaboration systems;
- maintain a live requirement-to-change-to-test ledger for each applicable
  `HSP-*` policy;
- record every failed, unavailable, skipped, or newly inapplicable check and
  its owner rather than modifying the expected policy result;
- stop and route an architecture conflict, policy conflict, possible ePHI
  event, or successor-gate trigger; and
- avoid a conformance, completion, release, or compliance claim until the
  exact required evidence exists.

### Completion and release review

A future completion claim must reconcile the accepted initiative, changed
paths, exact artifact identities, `ARC-CTR-009` vectors, this policy evidence,
runbooks, product documentation, limitations, and lifecycle status. Release
review must repeat the external-source currency check and risk review for
environmental or operational changes.

## Required prospective records

| Record | Minimum content | Policy owners |
|---|---|---|
| Policy applicability matrix | Every `HSP-*` ID; applicable/not applicable; exact rationale; product owner; evidence owner; no blanket `N/A` | `HSP-001`, `HSP-014` |
| Data and fixture manifest | Synthetic provenance or de-identification record link; intended fields; purpose; destinations; copies; deletion/sanitization disposition | `HSP-002`, `HSP-006`, `HSP-011` |
| Risk analysis and treatment plan | System/data-flow scope, threats, vulnerabilities, likelihood, impact, controls, residual risk, addressable decisions, owner, review triggers | `HSP-003`, `HSP-015` |
| Access and trust-boundary record | Named operator model; OS/Docker authority; services, networks, volumes, ingress/egress, administrators, excluded actors | `HSP-004`, `HSP-005` |
| Secure build and release record | Locks, digests, SBOM, provenance, signatures policy, platforms, vulnerabilities, licenses, hardening, patch disposition | `HSP-009` |
| Activity-review procedure | Safe record sources, owner, trigger/frequency, review method, finding route, retention, explicit non-audit limitation | `HSP-008` |
| Recovery plan and drill record | Criticality, recovery objective, backup identity/hash, exclusivity, restore/rollback result, off-volume protection if required | `HSP-010` |
| Host and media baseline | Supported versions, patching, addressable encryption decision, account/risk-selected lock/firewall/endpoint baseline, physical use, export custody and sanitization | `HSP-011` |
| Incident procedure and exercise | Triggers, containment, evidence preservation, contacts, possible-PHI escalation, synthetic table-top result, revisions | `HSP-012` |
| External-service inventory | Runtime/build/browser dependencies, data access, egress, vendor disposition, BAA/successor gate where applicable | `HSP-013` |
| Security verification record | Exact policy/vector mapping, artifacts, environment, method, results, limitations, dispositions, reviewer, timestamps | `HSP-014` |
| Release limitation statement | Local/single-user/non-ePHI scope, no app identity/audit/TLS claim, unsupported uses, source and policy revisions | `HSP-001`, `HSP-004`, `HSP-005`, `HSP-008`, `HSP-015` |

Records may be combined only when one canonical owner and one coherent
acceptance claim remain unambiguous. Similar text in another document does not
replace a missing required record.

## Policy verification catalog

The methods below are required planning inputs. A future initiative must select
the applicable architecture vectors and add exact commands, tools, fixtures,
platforms, and expected results.

| Policy | Minimum future verification | Principal architecture vectors or evidence |
|---|---|---|
| `HSP-001` | Claim-language and lifecycle review separates policy, implementation, conformance, and compliance | `AUTH-EX-001.10`; `ARC-CTR-009` D1-D6 gates |
| `HSP-002` | Data/fixture manifest review; repository/image/artifact scan; de-identification record review when used | `WEB-008/009`, `OPS-008/010`, `CNT-007`; additional source/artifact scans |
| `HSP-003` | Risk analysis completeness and owner review; trace each treatment to a product/test or successor gate | `ARC-CTR-009` evidence-record requirements; risk record review |
| `HSP-004` | OS/Docker access-procedure review; container/network/mount inventory; alternate-state-path negatives | `AUTH-EX-001.1/.6`, `CNT-003/004/011/015`, `E2E-008` |
| `HSP-005` | Rendered/runtime network, Host, Origin, proxy, IPv4/IPv6, LAN, arbitrary-container, egress tests | `CNT-002/003/014`, `OPS-002/003`, `WEB-013`, `E2E-010` |
| `HSP-006` | Sensitive synthetic fixtures through logs, errors, URLs, browser storage, CLI/process output, screenshots, build and CI artifacts | `HTTP-009/010`, `SDK-008`, `CLI-009`, `WEB-008/009`, `OPS-008/009` |
| `HSP-007` | Atomicity, ETag, immutable identity, schema/migration/hash, lock, mount, corruption, and restore tests | `DOM-011/012`, `HTTP-003/004/012`, `DB-001`-`010`, `CNT-004/011` |
| `HSP-008` | Log-schema/redaction/rotation tests and a documented activity-review exercise; verify non-audit disclaimer | `OPS-008`; `HTTP-010/011`; additional review-record inspection |
| `HSP-009` | Image/layer/content/dependency scan; effective security probes; SBOM/provenance/platform/vulnerability review | `CNT-005`-`009`, `OPS-001/006/010`, `E2E-009` |
| `HSP-010` | Offline backup/export/import/restore/rollback, host-loss limitation, and content/risk-appropriate off-volume protection when required | `DB-008/009`, `OPS-011/012`, `E2E-006` |
| `HSP-011` | Supported-host baseline inspection; addressable encryption decision and selected-control evidence; OS lock and physical/media procedure exercise; destructive-command review | `CNT-001/012`, `OPS-013`; additional inherited host/media record review |
| `HSP-012` | Synthetic incident table-top and technical stop/preserve/hash/restore exercise; escalation/contact validation | `DB-010`, `OPS-007/011/012`; incident record review |
| `HSP-013` | Runtime/browser/build dependency and egress inventory; prove no data reaches third parties; vendor gate review | `WEB-009/012`, `CNT-007/008`, `OPS-010`; external-service inventory |
| `HSP-014` | Evidence completeness, source-currency, failed-check disposition, retention owner, and policy/product revision reconciliation | All applicable `ARC-CTR-009` vectors and delivery gates |
| `HSP-015` | Scope review finds no successor trigger, or product work remains blocked pending an accepted successor architecture | Route/command/schema inventory `E2E-007/008`; successor-gate record |

## Data and fixture rules for future tests

- Use clearly fictional names and values created for the test. Do not derive a
  fixture by changing a real person's name, UUID, date, or one identifier.
- Use a stable fixture ID and purpose, not a patient-like label. The fixture
  manifest must record its author and synthetic origin.
- Exercise sensitive-data leakage controls with unmistakably synthetic canary
  strings. A canary must not resemble an actual identifier or secret.
- Never copy a live database or backup into a development, test, CI, demo, or
  support environment.
- Test Compose projects use fresh disposable named volumes and cannot resolve
  release/user volumes, as required by `ARC-CTR-009`.
- Test output retained as evidence must use hashes, safe IDs, counts, and
  redacted samples. If a complete synthetic record is needed to prove exact
  round-trip behavior, its manifest and evidence destination must be explicit.

## Future security evidence record schema

Each verification run must preserve at least:

| Field | Required value |
|---|---|
| Evidence ID | Stable initiative/product-scoped identifier |
| Claim boundary | Exact `HSP-*` policies and `ARC-CTR-009` vectors being tested |
| Authority | `SEC-HIPAA-SUITE-001@1.0.1`, `SEC-NIST-SUITE-001@1.0.1`, `ARC-SUITE-001@2.0.1`, accepted initiative revision |
| Product identity | D2-D6 unit, version, Git commit, image/manifest/wheel/bundle/Compose hashes |
| Data classification | Fixture manifest ID and synthetic/de-identification basis; no raw record content |
| Environment | Host/OS/architecture, Docker/Desktop/Compose/BuildKit, browser, image digests, network and named test-volume identities |
| Method | Exact containerized command, tool/version, configuration, fixture, static/mock/live/end-to-end level |
| Time | UTC start/end and duration |
| Results | Per-policy/per-vector pass/fail/skip/unavailable result and machine-readable artifact location |
| Negative proof | Prohibited route, network, mount, storage, log, data, or dependency checks applicable to the claim |
| Limitations | Scanner limits, untested environment, nondeterminism, assumptions, source staleness |
| Disposition | Owner, due/review event, and linked defect/decision/conflict for every nonpass |
| Review | Reviewer identity, review date, decision, and next source/risk review event |

The record must not contain record values, raw searches, backup bytes,
credentials, secrets, host-sensitive paths, or unredacted diagnostic content.

## Release documentation requirements

Future release material must state, prominently and consistently:

- this is a local, single-user demonstrator for synthetic or externally
  documented de-identified data;
- application accounts, roles, per-user audit, remote access, TLS, high
  availability, and ePHI authorization are absent;
- the exact supported Compose invocation, loopback origin, and private CLI
  path;
- the host security and physical/media prerequisites from `HSP-011`;
- safe start, stop, backup, restore, upgrade, and destructive-command
  boundaries;
- incident contacts and the possible-PHI stop/escalation rule;
- exact architecture/policy/product revisions and verified platforms; and
- what was not tested or supported.

Documentation must not offer a workaround for a prohibited topology or
describe an unsafe path as an advanced configuration.

## Gate result vocabulary

Future records may use only these meanings:

- **Pass:** the exact expected result was observed for the identified artifact
  and environment.
- **Fail:** the expected result was not observed; the affected claim is
  blocked.
- **Unavailable:** required evidence could not be obtained; the affected claim
  remains blocked.
- **Not applicable:** a precise, reviewed scope reason proves the policy does
  not govern the named product; it is not a risk acceptance.
- **Deferred:** the work has a truthful future owner and is excluded from the
  current accepted claim; it cannot be required in-scope work.

No `warning`, scanner suppression, test skip, or human confidence statement is
equivalent to `Pass`.

## No current-state conclusion

This standard intentionally contains no completed checklist, test output,
artifact identity, risk acceptance, release approval, or compliance result.
Those records belong to future, separately accepted initiatives and must be
created only when the relevant work and evidence actually exist.

`RZN-001` may be cited for requested intent but never as authority for a data
classification, security exception, delivery gate, or product claim.

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established prospective development and evidence requirements | User's HIPAA policy instruction and future-development clarification |
| 2026-11-10 | `1.0.1` | Required exact architecture, NIST, and HIPAA identities for one additive evidence record | User's explicit instruction to apply the reconciliation findings in place |

