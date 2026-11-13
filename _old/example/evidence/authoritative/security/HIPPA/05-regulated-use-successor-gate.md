# Regulated-use successor architecture gate

**Gate ID:** `SEC-HIPAA-GATE-001`  
**Revision:** `1.0.1`  
**Status:** Active prospective gate  
**Governing policy:** [`HSP-015`](02-prospective-security-policy.md#hsp-015--successor-architecture-and-exception-gate)  
**Architecture input:** [`ARC-SUITE-001@2.0.1`](../../architecture/00-architecture-suite-index.md)  
**Applicable peer gate:** [`SEC-NIST-POL-001`, `SEC-POL-14`](../NIST/01-demonstrator-security-policy.md#sec-pol-14---exceptions-risk-decisions-and-expansion-triggers)  

## Purpose

This record identifies accepted architecture premises that make the current
demonstrator profile unsuitable for actual or possible ePHI. It guides future
scope decisions; it is not a test or assessment of existing code.

A trigger in this record stops only the proposed regulated or expanded use.
Independent future work that remains inside the synthetic/de-identified,
local, single-user profile may continue through its normal initiative.

## Gate triggers

The gate is triggered by any proposal, requirement, fixture, deployment,
integration, or operating instruction involving:

- actual, possible, or insufficiently classified ePHI;
- a real patient, member, beneficiary, provider record, or production-derived
  data set;
- more than one human user or a shared OS/workstation identity;
- LAN, remote, VPN, tunnel, proxy, cloud, public, or cross-host access;
- an external service that can receive, maintain, process, log, back up, or
  transmit record content;
- a claim of HIPAA compliance, HIPAA certification, regulated production
  readiness, or authorization for clinical use; or
- a proposed exception to `HSP-002`, `HSP-004`, `HSP-005`, or `HSP-008`.

## Architecture-declared limits requiring successor decisions

| Gate area | Accepted architecture evidence | HIPAA relevance | Required successor outcome |
|---|---|---|---|
| Human identity and authorization | [`AUTH-EX-001.6/.9`](../../architecture/01-accepted-architecture-baseline.md); [`ADR-004`, Application identity boundary](../../architecture/07-ADR-004-container-only-deployment-trust-model.md) | 45 CFR 164.308(a)(3)-(4), 164.312(a), (d) | Unique app identity, authentication, authorization, access lifecycle/review, emergency access, and session/logoff design |
| Activity attribution and audit | [`ARC-CTR-002`, Contract rules](../../architecture/13-record-http-contract.md); [`ARC-CTR-008`, Logging and diagnostics](../../architecture/23-operations-security-contract.md) | 45 CFR 164.308(a)(1)(ii)(D), 164.312(b) | Tamper-protected, reviewable audit design tied to unique users/entities, retention and response procedures |
| Data-at-rest encryption and keys | [`ARC-CTR-004`, Database identity and placement / backup contract](../../architecture/16-sqlite-persistence-contract.md) defines SQLite and hashed backups but no encryption/key lifecycle | 45 CFR 164.312(a)(2)(iv), 164.306(d) | Risk-based encryption and key generation, storage, access, rotation, recovery, destruction, and backup/export coverage |
| Network encryption and remote trust | [`ARC-CTR-002`, Protocol baseline](../../architecture/13-record-http-contract.md) and [`ARC-CTR-008`, HTTP and browser security](../../architecture/23-operations-security-contract.md) use local HTTP and prohibit remote access | 45 CFR 164.312(e) | TLS termination and certificate lifecycle, proxy/source trust, remote authentication/authorization, integrity, rate-limit and administration design |
| Administrator and Docker-daemon trust | [`ADR-004`, Container controls](../../architecture/07-ADR-004-container-only-deployment-trust-model.md) places host/Docker administrators inside the trust boundary | 45 CFR 164.308(a)(3)-(4), 164.312(a), (d) | Privileged-access governance, separation/monitoring, platform hardening, break-glass and incident design appropriate to the risk analysis |
| Organizational safeguards | [`ARC-SUITE-001`, Explicit exclusions](../../architecture/00-architecture-suite-index.md) and this limited policy do not define enterprise workforce, facility, vendor, privacy, or breach programs | 45 CFR 164.308, .310, .314, .316 and applicable Privacy/Breach rules | Owning regulated entity supplies and maps all applicable administrative, physical, organizational, privacy, and breach obligations |
| Data lifecycle and media | [`AUTH-EX-001.9`](../../architecture/01-accepted-architecture-baseline.md) excludes record deletion/history; [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md) defines opaque backup export and destructive-volume limits | 45 CFR 164.310(d); entity retention/privacy obligations | Accepted retention, legal hold, correction/deletion where applicable, media inventory, encrypted export, sanitization, disposal, and migration plan |
| Product evidence | [`ARC-CTR-009`, Current evidence status](../../architecture/24-conformance-contract.md) makes no D2-D6 implementation/conformance claim | 45 CFR 164.308(a)(8), 164.316 | Separately accepted product initiatives and exact technical/nontechnical evidence; no architecture-only readiness claim |

The table describes missing successor decisions, not a conclusion that a
particular implementation failed a test.

## Required entry record for successor work

Before successor design begins, the proposing authority must supply or
authorize creation of a record containing:

1. the exact proposed use, users, regulated entity/business-associate roles,
   data classes, locations, and jurisdictions;
2. why synthetic or documented de-identified data is insufficient;
3. the complete current legal and contractual source inventory;
4. a risk analysis covering all ePHI and all systems that create, receive,
   maintain, or transmit it;
5. an owner and decision authority for every administrative, physical,
   technical, organizational, privacy, breach, and state-law area;
6. the current architecture records to revise or supersede and the migration,
   compatibility, recovery, and rollback consequences; and
7. a narrow decomposition into independently acceptable design and product
   initiatives.

Unresolved facts remain open questions for explicit human disposition. Codex
or a developer must not infer covered-entity status, lawful use, risk
acceptance, or a final security design.

## Minimum successor design outputs

The successor architecture must, at minimum, produce:

- a revised system/trust/data boundary and threat model;
- identity, authentication, authorization, privileged access, session, and
  emergency-access contracts;
- audit-event, identity attribution, integrity, review, alerting, retention,
  and incident-use contracts;
- at-rest and in-transit encryption and complete key/certificate lifecycle;
- remote ingress/egress, proxy, API, browser, CLI/SDK, administration,
  monitoring, and rate/abuse controls;
- secrets, dependency, vulnerability, patch, build, release, and platform
  management;
- backup, disaster recovery, emergency mode, availability, recovery
  objectives, testing, and host-loss procedures;
- workstation, facility, device/media, export, sanitization, and disposal
  requirements;
- vendor/business-associate and subcontractor boundaries;
- Privacy Rule, Breach Notification Rule, minimum-necessary, retention, and
  applicable state/contractual mappings owned by qualified authorities; and
- a replacement conformance contract with positive and negative verification
  vectors for every accepted control.

This list is a minimum design inventory, not a decision that any particular
technology is required or sufficient.

## Exit conditions

The gate closes only for the exact successor scope when all of the following
exist:

1. explicit human authority for the named architecture revision;
2. current legal/risk evidence and resolved blocking decisions;
3. an accepted successor architecture preserving the prior revision and
   documenting every impact;
4. revised security policy and conformance contracts;
5. separately accepted, narrowly scoped implementation initiatives; and
6. later product evidence proving the accepted claims for exact artifacts and
   environments.

Architecture acceptance closes the design gate but does not prove product
implementation, release readiness, or HIPAA compliance.

## Prohibited shortcuts

None of the following closes this gate:

- changing `127.0.0.1` to a network address;
- adding a reverse proxy, TLS certificate, VPN, password prompt, API key, or
  log collector without a successor design;
- relying only on Docker isolation, host login, disk encryption, a BAA,
  de-identification by inspection, or a vulnerability scan;
- describing an addressable implementation specification as optional;
- accepting risk without the authority to revise the architecture or satisfy
  applicable law;
- relying on `RZN-001`, its generic data model, or a formerly open question as
  authority to bypass this gate;
- narrowing a claim after implementation to hide an unmet control; or
- treating a successful demo as regulated-use evidence.

## Source links

The controlling regulatory safeguards are in [45 CFR Part 164, Subpart C](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C).
Official HHS material reviewed for this revision is cataloged in
[`SEC-HIPAA-AUT-001`](01-authority-scope-and-source-basis.md). Future successor
work must verify the then-current law and guidance rather than assuming this
2026-11-10 source snapshot remains current.

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established the regulated-use successor gate | User's HIPAA policy instruction and future-development clarification |
| 2026-11-10 | `1.0.1` | Bound the gate to architecture 2.0.1 and prohibited RZN-001 as bypass authority | User's explicit instruction to apply the reconciliation findings in place |

