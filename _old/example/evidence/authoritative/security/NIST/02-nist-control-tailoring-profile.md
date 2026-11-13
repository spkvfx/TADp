# NIST control tailoring profile

**Profile ID:** `SEC-NIST-MAP-001`  
**Revision:** `1.0.1`  
**Status:** Accepted future-development profile  
**Owner and accepting authority:** User, project authority  
**Effective date:** 2026-11-10  
**Governing suite:** [`SEC-NIST-SUITE-001`](00-nist-security-policy-suite-index.md)  
**Architecture input:** [`ARC-SUITE-001@2.0.1`](../../architecture/00-architecture-suite-index.md)  
**Applicable peer profile:** [`SEC-HIPAA-SUITE-001@1.0.1`](../HIPPA/00-hipaa-security-policy-suite-index.md)  

## Purpose

This profile records why the NIST outcomes cited by
[`SEC-NIST-POL-001`](01-demonstrator-security-policy.md) are relevant to the
accepted demonstrator architecture and why other control areas are outside the
limited profile. It is a requirements crosswalk for future development, not an
assessment of the current implementation.

The official publication identities and locators used by this crosswalk are in
[`SEC-NIST-SRC-001`](04-nist-source-register.md). A citation to a NIST function,
category, control, task, or section is a documented justification for the
project policy. It is not a claim that the whole NIST publication, control, or
enhancement is implemented.

## Tailoring method

The project applied this order:

1. Use the accepted architecture as factual input describing system purpose,
   actors, data, deployment, trust boundaries, state ownership, lifecycle, and
   explicit exclusions; do not treat it as authority to weaken security policy.
2. Identify security risks created by those architectural facts.
3. Select only final NIST guidance that directly supports a proportionate
   future requirement for those risks.
4. Convert the selected outcome into a project security policy with a stable
   ID that guides and constrains architecture and future work, rather than
   copying a federal or enterprise baseline.
5. Record omitted areas, the reason for omission, and the change that would
   make each area relevant.
6. Require future evidence at the boundary where the architecture assigns the
   behavior; do not infer implementation from the architecture or crosswalk.

After acceptance, this policy is primary within its security and permitted-use
scope. Compatibility means the architecture satisfies the policy; it does not
mean policy is changed to preserve an architecture choice.

This is an outcome-based, risk-informed tailoring exercise. It is not a NIST
SP 800-53B baseline selection and does not perform the NIST Risk Management
Framework authorization process.

## Selected outcome crosswalk

| Project policy | Architecture-derived security concern | NIST CSF 2.0 alignment | NIST SP 800-53 Rev. 5 alignment | Additional final NIST guidance |
|---|---|---|---|---|
| `SEC-POL-01` | Local single-user purpose, narrow data class, and explicit trust assumptions must remain visible | `GOVERN` Organizational Context and Policy; `IDENTIFY` Risk Assessment | `PL-2` System Security and Privacy Plans; `RA-3` Risk Assessment | SSDF `PW.1.1` risk modeling and data classification |
| `SEC-POL-02` | The unauthenticated app depends on loopback ingress, a private Compose network, exact Host/Origin, and the API-only path | `PROTECT` Platform Security and Technology Infrastructure Resilience | `AC-3` Access Enforcement; `CM-7` Least Functionality; `SC-7` Boundary Protection | SP 800-190 sections `4.3.3` and `4.4.2` on network separation and controlled container traffic |
| `SEC-POL-03` | A compromised container must have minimal host, kernel, filesystem, network, and resource authority | `PROTECT` Platform Security and Technology Infrastructure Resilience | `AC-6` Least Privilege; `CM-6` Configuration Settings; `CM-7` Least Functionality; `SC-6` Resource Availability | SP 800-190 sections `4.1.2`, `4.4.3`, and `4.5.5` on non-privileged images, enforced runtime configuration, minimal filesystem permissions, and avoiding sensitive host mounts |
| `SEC-POL-04` | One immutable, reviewable configuration must prevent drift and untraceable mutation | `GOVERN` Policy; `PROTECT` Platform Security | `CM-2` Baseline Configuration; `CM-3` Configuration Change Control; `CM-6` Configuration Settings; `SI-7` Software, Firmware, and Information Integrity | SSDF `PW.9.1/.2` secure defaults, configuration as code, and verification |
| `SEC-POL-05` | SQLite has one live owner; writes, migrations, and maintenance must preserve transaction and data integrity | `PROTECT` Data Security and Platform Security | `AC-3` Access Enforcement; `AC-6` Least Privilege; `CP-10(2)` Transaction Recovery; `SI-7` Software, Firmware, and Information Integrity | SP 800-190 sections `4.4.3` and `4.5.5` on constrained runtime access and volumes |
| `SEC-POL-06` | Untrusted HTTP, record, search, database, browser, and diagnostic values must never become executable control data | `PROTECT` Data Security and Platform Security | `SC-18` Mobile Code; `SI-10` Information Input Validation; `SI-11` Error Handling | SSDF `PW.5.1` secure coding, validation, output encoding, error handling, and safe logging |
| `SEC-POL-07` | The local unauthenticated service must bound resource consumption and fail without inventing a successful or complete result | `PROTECT` Technology Infrastructure Resilience | `SC-5` Denial-of-Service Protection; `SC-6` Resource Availability; `SI-10` Information Input Validation | SP 800-190 sections `4.4.2` and `4.4.3` on controlled network and runtime configuration |
| `SEC-POL-08` | Diagnostics must support bounded correlation without exposing record content or implying user accountability | `DETECT` Continuous Monitoring; `PROTECT` Data Security | `AU-2` Event Logging; `AU-3` Content of Audit Records; `AU-4` Audit Log Storage Capacity; `SI-4` System Monitoring | SSDF `PW.5.1` safe logging and tracing |
| `SEC-POL-09` | A single named-volume store needs validated, non-overwriting, known-state recovery with an explicit host-loss limitation | `RECOVER` Incident Recovery Plan Execution; `PROTECT` Data Security | `CP-9` System Backup; `CP-10` System Recovery and Reconstitution; `SI-7` Software, Firmware, and Information Integrity | SP 800-53 `CP-10(2)` transaction recovery reinforces the database recovery outcome |
| `SEC-POL-10` | Images and artifacts cross an external software supply chain and must retain immutable identity and provenance | `GOVERN` Cybersecurity Supply Chain Risk Management; `PROTECT` Platform Security | `SI-7` Software, Firmware, and Information Integrity; `SR-3` Supply Chain Controls and Processes; `SR-4` Provenance; `SR-11` Component Authenticity | SSDF `PS.2`, `PS.3`, and `PW.4`; SP 800-190 sections `4.1` and `4.2` on image and registry risks |
| `SEC-POL-11` | Future development needs traceable, layered, adversarial assurance at the exact architecture and release boundaries | `GOVERN` Roles, Responsibilities, and Authorities and Policy; `PROTECT` Platform Security | `CA-2` Control Assessments; `SA-11` Developer Testing and Evaluation | SP 800-53A assessment methods; SSDF `PO.1`, `PW.5`, `PW.7`, and `PW.8` |
| `SEC-POL-12` | Owned code, dependencies, runtimes, and base images change risk over time | `IDENTIFY` Risk Assessment; `DETECT` Continuous Monitoring; `GOVERN` Cybersecurity Supply Chain Risk Management | `RA-5` Vulnerability Monitoring and Scanning; `SI-2` Flaw Remediation | SSDF `RV.1`, `RV.2`, and `RV.3`; SP 800-190 sections `4.1.1` and `4.4.1` |
| `SEC-POL-13` | A local integrity, exposure, or artifact event needs evidence preservation and known-state recovery | `RESPOND` Incident Management, Analysis, and Mitigation; `RECOVER` Incident Recovery Plan Execution | `CP-10` System Recovery and Reconstitution; `IR-4` Incident Handling; `SI-7` Software, Firmware, and Information Integrity | SP 800-190 section `6.4` container-specific incident and forensic preparation |
| `SEC-POL-14` | Exceptions and boundary expansion must not silently replace accepted architecture or risk decisions | `GOVERN` Policy and Oversight; `IDENTIFY` Risk Assessment | `CM-3` Configuration Change Control; `PL-2` System Security and Privacy Plans; `RA-3` Risk Assessment | SSDF `PO.1.2` requirements and exception process; `PW.1` design-risk justification |

## Deliberately tailored-out areas

The following dispositions are limited to the accepted demonstrator profile.
"Tailored out" does not mean that the risk or NIST guidance is generally
inapplicable.

| Area not selected as a current project requirement | Reason within the accepted architecture | Trigger requiring successor architecture and policy review |
|---|---|---|
| Application account management and identity proofing (`AC-2`, `IA-2`, `IA-5`, and the account-oriented portions of CSF `PR.AA`) | The architecture permits one local user, no app accounts, no roles, and relies on the OS account plus Docker access as the trust boundary | More than one actor, remote access, differentiated authorization, attribution, sessions, or an identity provider |
| TLS and cryptographic session protection for app traffic (`SC-8`, `SC-13`) | Public ingress is IPv4 loopback only; private traffic remains on the project bridge; the architecture does not define keys, certificates, or proxy trust | Any non-loopback or untrusted-network path, proxy, tunnel, LAN/Internet exposure, or regulated transport requirement |
| Record encryption at rest (`SC-28`) and cryptographic key management | Approved records are non-production demonstration/test data and Docker-host administrators are inside the trust boundary; the policy prohibits data that would require stronger protection | Sensitive, regulated, confidential, multi-tenant, production, removable-media, or Docker-host-threat requirements |
| Formal per-user audit, audit review, non-repudiation, and retention (`AU-6`, `AU-9`, `AU-10`, `AU-11`) | There is no application identity, and architecture-classified logs are bounded diagnostics rather than an audit ledger | User attribution, compliance retention, legal evidence, privileged administration, non-repudiation, or centralized audit requirements |
| Fixed RTO/RPO, alternate sites, failover, and high availability (`CP-2`, `CP-4`, `CP-6`, `CP-7`) | The local demonstrator defines safe backup/restore behavior but makes no service-level, host-loss, or availability promise | Production use, availability commitments, multi-host service, disaster-recovery objectives, or business-continuity dependency |
| Organization-wide incident program and mandatory external reporting (`IR-1`, `IR-6`, and related organizational controls) | The app can define local evidence preservation and recovery, but no organization, regulator, reporting channel, or response team is in product scope | Production operation, regulated data, contractual notification, remote response, or a formal security operations function |
| Enterprise SIEM, IDS/IPS, endpoint detection, and continuous operations monitoring | The architecture requires local structured diagnostics and no default telemetry; it has no central monitoring service | Remote/production operation, multiple hosts or users, telemetry approval, central operations, or threat-detection objectives |
| Privacy program and `PT`-family controls | The profile forbids intentionally storing regulated personal data and does not define a PII processing purpose | Any approved PII, profiling, privacy notice, consent, deletion, subject-rights, or privacy-risk requirement |
| Physical, personnel, training, and organization-wide program controls (`PE`, `PS`, `AT`, `PM`, and organizational portions of other families) | Those safeguards belong to the operator and development organization, not to the demonstrator product boundary | A formal organizational control baseline, inherited-control model, hosted service, or authorization package |
| RMF authorization, `CA-6` authorization decisions, a complete SP 800-53B baseline, and FISMA claims | The requested deliverable is a narrow future-development policy, not a federal system authorization package | A named authorizing official, categorization, selected baseline, inherited controls, assessment plan, residual-risk decision, and authorization boundary |
| Mandatory FIPS-validated cryptographic modules or a universal release-signature technology | The architecture requires artifact integrity, SHA-256 metadata, provenance, and an explicit signature/authenticated-provenance policy, but does not choose a federal cryptographic module | A regulatory cryptography requirement, protected key lifecycle, federal use, or accepted architecture decision naming the technology and trust root |

## Inheritance and operator dependencies

The policy assumes that the local operator protects the host OS, user account,
Docker daemon access, exported backup destination, and release credentials.
Those are dependencies, not controls implemented by the application. Future
delivery documentation must state them so the product does not imply that
container isolation protects against a trusted Docker administrator or a
compromised host.

## Review rule

Any trigger in the tailored-out table suspends reliance on this limited
profile for the affected change. The change must follow `SEC-POL-14` and the
architecture feedback process before implementation. A scan, test, or risk
acceptance record cannot silently add a new system boundary or waive an
architecture invariant.

The same trigger review must check the HIPAA successor gate. A tailoring
decision cannot use `RZN-001`, a passing architecture vector, or an accepted
NIST exception as a substitute for an applicable `HSP-*` requirement.

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established the limited control-tailoring profile | User's NIST policy instruction and clarification |
| 2026-11-10 | `1.0.1` | Reconciled tailoring triggers with architecture 2.0.1 and the HIPAA successor gate | User's explicit instruction to apply the reconciliation findings in place |
