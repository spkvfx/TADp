# HIPAA control rationale and traceability

**Mapping ID:** `SEC-HIPAA-MAP-001`  
**Revision:** `1.0.0`  
**Status:** Accepted policy rationale  
**Policy mapped:** [`SEC-HIPAA-POL-001`](02-prospective-security-policy.md)  
**Primary evidence family:** [`ARC-SUITE-001@2.0.0`](../../architecture/00-architecture-suite-index.md)  
**External baseline reviewed:** 2026-11-10  

## Purpose and method

This record justifies every policy in `SEC-HIPAA-POL-001`. Each entry names:

1. the precise architecture evidence that establishes the app-specific need
   or constraint;
2. the current HIPAA regulation or official guidance supporting the safeguard;
3. why the selected policy is reasonable for the accepted demonstrator
   profile;
4. evidence a future initiative must produce; and
5. the limitation that prevents an overbroad compliance claim.

Architecture evidence is primary for system scope and design. The regulation
and official guidance establish the HIPAA basis. NIST material is supporting
implementation guidance only and never overrides the regulation or the
accepted architecture.

## Summary crosswalk

| Policy | Principal HIPAA locator | Architecture owner |
|---|---|---|
| `HSP-001` | 45 CFR 164.316; 164.308(a)(8) | `ARC-SUITE-001`, `AUTH-EX-001.10`, `ARC-CTR-009` |
| `HSP-002` | 45 CFR 164.514(a)-(c); 164.306(a) | `ARC-CTR-001`, `AUTH-EX-001.6/.9` |
| `HSP-003` | 45 CFR 164.308(a)(1)-(2); 164.306(d)-(e) | `ARC-CTR-008`, `ARC-CTR-009` |
| `HSP-004` | 45 CFR 164.308(a)(3)-(4); 164.312(a), (d) | `ADR-004`, `ARC-CTR-008` |
| `HSP-005` | 45 CFR 164.312(e); 164.306(a), (d) | `AUTH-EX-001.6`, `ARC-CTR-002`, `ARC-CTR-008` |
| `HSP-006` | 45 CFR 164.306(a); 164.502(b); 164.514(d) | `ARC-CTR-001`, `ARC-CTR-006`, `ARC-CTR-007`, `ARC-CTR-008` |
| `HSP-007` | 45 CFR 164.312(c); 164.306(a) | `AUTH-EX-001.1/.5/.12`, `ARC-CTR-004` |
| `HSP-008` | 45 CFR 164.308(a)(1)(ii)(D); 164.312(b) | `ARC-CTR-002`, `ARC-CTR-008` |
| `HSP-009` | 45 CFR 164.308(a)(1)(ii)(A)-(B); 164.306(e) | `AUTH-EX-001.13`, `ADR-005`, `ARC-CTR-008` |
| `HSP-010` | 45 CFR 164.308(a)(7); 164.310(d)(2)(iv); 164.312(a)(2)(ii) | `ARC-CTR-004`, `ARC-CTR-008` |
| `HSP-011` | 45 CFR 164.310(a)-(d); 164.312(a)(2)(iii)-(iv) | `ADR-004`, `ARC-BND-003`, `ARC-CTR-008` |
| `HSP-012` | 45 CFR 164.308(a)(6); 164.400-414 | `ARC-CTR-008` |
| `HSP-013` | 45 CFR 164.308(b); 164.314(a) | `ADR-005`, `ARC-CTR-007`, `ARC-CTR-008` |
| `HSP-014` | 45 CFR 164.308(a)(8); 164.316; 164.306(e) | `ARC-CTR-009`, Codex evidence protocol |
| `HSP-015` | 45 CFR 164.306(c)-(e); 164.308, .310, .312, .314, .316 | `ARC-SUITE-001` exclusions, `ADR-004`, `ARC-CTR-008` |

## Cross-suite compatibility

The existing NIST suite remains co-governing authoritative evidence. The
following mapping records the intended relationship; it does not claim that
either suite or any product control is implemented.

| HIPAA policy | Compatible NIST policy or disposition | Relationship |
|---|---|---|
| `HSP-001` | `SEC-POL-01`, `SEC-POL-11`, `SEC-POL-14` | Narrow authorized use, future evidence, and truthful exception/claim boundaries |
| `HSP-002` | `SEC-POL-01` | HIPAA adds a precise synthetic/de-identification gate; NIST's separate bans on production, confidential, regulated, or higher-control data still apply |
| `HSP-003` | `SEC-POL-01`, `SEC-POL-12`, `SEC-POL-14` | Adds HIPAA-specific owner, risk-analysis, and addressable-control documentation to the risk-informed profile |
| `HSP-004` | `SEC-POL-01`, `SEC-POL-02`, `SEC-POL-03` | Preserves OS/Docker trust, exact network boundary, and least privilege while making the lack of app identity explicit |
| `HSP-005` | `SEC-POL-02`, `SEC-POL-14` | Same loopback/private topology and same successor trigger for remote or encrypted transport requirements |
| `HSP-006` | `SEC-POL-06`, `SEC-POL-08` | Same safe interpretation, output handling, logging minimization, and diagnostic limits |
| `HSP-007` | `SEC-POL-05` | Same API-exclusive state, transactions, lock, schema, integrity, and maintenance controls |
| `HSP-008` | `SEC-POL-08` and `SEC-NIST-MAP-001` audit tailoring | Same bounded diagnostics and explicit rejection of a per-user audit claim |
| `HSP-009` | `SEC-POL-03`, `SEC-POL-04`, `SEC-POL-10`, `SEC-POL-12` | Reuses the NIST container, configuration, supply-chain, and vulnerability baseline |
| `HSP-010` | `SEC-POL-09` | Same validated offline recovery and host-loss limitation; protection of exports follows content and the documented encryption decision |
| `HSP-011` | `SEC-POL-01`, `SEC-POL-03`, `SEC-POL-09`, plus `SEC-NIST-MAP-001` operator dependencies | Treats host, physical, screen-lock, encryption, and media measures as documented inherited dependencies, not app-implemented controls |
| `HSP-012` | `SEC-POL-13` | Same local containment, evidence preservation, known-state recovery, and external organization responsibility |
| `HSP-013` | `SEC-POL-10`, `SEC-POL-14` | Preserves no-data external build/runtime paths and adds the HIPAA business-associate escalation trigger |
| `HSP-014` | `SEC-POL-11`, `SEC-NIST-VER-001` | Uses the same prospective, exact-artifact evidence model and adds HIPAA source/retention review |
| `HSP-015` | `SEC-POL-14`, `SEC-NIST-MAP-001` expansion triggers | Same successor-architecture boundary for regulated data, identity, audit, encryption, remote, production, or formal compliance claims |

## HSP-001 — Prospective standing and truthful claims

**Architecture evidence.**

- [`ARC-SUITE-001`](../../architecture/00-architecture-suite-index.md),
  **Purpose and standing**, says the architecture specifies what future
  products must do and does not claim those products exist.
- [`AUTH-EX-001.10`](../../architecture/01-accepted-architecture-baseline.md)
  prohibits an implementation or completion claim without a governing
  initiative and `ARC-CTR-009` evidence.
- [`ARC-CTR-009`](../../architecture/24-conformance-contract.md), **Current
  evidence status**, records no supplied D2-D6 implementation or conformance
  evidence and says architecture detail is a test oracle, not execution
  evidence.

**HIPAA basis.** [45 CFR 164.316(a)-(b)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.316)
requires reasonable policies and written documentation; [45 CFR
164.308(a)(8)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires evaluation. HHS's [compliance FAQ](https://www.hhs.gov/hipaa/for-professionals/faq/how-will-we-know-if-our-organization-and-our-systems-are-compliant-with-the-security-rule/index.html)
explains that compliance is organization-specific, ongoing, risk-based, and
not established by one strategy.

**Justification.** A policy is a governance input, not proof that a technical
or organizational control operates. Separating requirement, implementation,
verification, and compliance prevents the exact evidence inflation prohibited
by both TADp and HHS's ongoing-evaluation model.

**Future evidence.** Source mapping from each applicable `HSP-*` policy to a
product and test; exact artifact/environment results; documentation-language
review showing no certification or current-state claim; truthful initiative
status.

**Limitation.** Passing all app-level checks still cannot determine entity
status or organization-wide HIPAA compliance.

## HSP-002 — Synthetic or documented de-identified data only

**Architecture evidence.** [`ARC-CTR-001`](../../architecture/11-record-domain-contract.md)
accepts a generic human label and up to 16 KiB of free text, treats full names
and values as sensitive by default, and cannot determine whether text
identifies a person. [`AUTH-EX-001.6`](../../architecture/01-accepted-architecture-baseline.md)
fixes an application-unauthenticated local profile, while `.9` excludes
accounts and audit history.

**HIPAA basis.** [45 CFR 164.514(a)-(c)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514)
defines de-identification through Expert Determination or Safe Harbor and
governs re-identification codes. HHS's [de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)
warns that free text and contextual facts may identify a person and explains
that de-identified information is no longer PHI only after an accepted method
is satisfied. [45 CFR 164.306(a)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
requires protection of all ePHI a regulated entity creates, receives,
maintains, or transmits.

**Justification.** The architecture intentionally lacks controls necessary for
a regulated production profile. Excluding ePHI at the data boundary is the
smallest invariant-compatible way to develop a HIPAA-informed demonstrator
without falsely treating generic text validation as privacy control.

**Future evidence.** A fixture/data manifest declaring synthetic provenance or
linking the organization-owned de-identification determination; scans and
review covering source, tests, images, logs, screenshots, backups, and CI
artifacts; negative documentation tests showing that UUID generation is not
described as de-identification.

**Limitation.** Automated scans cannot prove the absence of identifiers or
contextual re-identification risk. Human/organizational evidence remains
required.

## HSP-003 — Assigned security responsibility and risk management

**Architecture evidence.** [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md)
defines the host, Docker, image, network, volume, logging, recovery, and
incident boundaries and names several risks requiring owner disposition.
[`ARC-CTR-009`](../../architecture/24-conformance-contract.md) requires exact
environment, artifact, limitation, disposition, and reviewer evidence for
future claims.

**HIPAA basis.** [45 CFR 164.308(a)(1)(ii)(A)-(B) and (a)(2)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
require accurate and thorough risk analysis, risk management, and an assigned
security official. [45 CFR 164.306(d)(3) and (e)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
require assessment/documentation of addressable specifications and continuing
maintenance. HHS's [risk-analysis guidance](https://www.hhs.gov/hipaa/for-professionals/security/guidance/guidance-risk-analysis/index.html)
requires considering all ePHI and electronic media and explains that risk
analysis informs encryption, backup, integrity, and transmission decisions.

**Justification.** Architecture supplies a bounded system model, but risk
depends on the future host, exact artifacts, use, threats, and environment.
Naming an accountable owner and refreshing the risk analysis at material
change prevents design assumptions from becoming permanent undocumented
exceptions.

**Future evidence.** Named owner and authority; system/data-flow inventory;
threat/vulnerability/risk register; treatment plan; addressable-specification
decisions; residual-risk approvals; review triggers and dates.

**Limitation.** This policy supplies minimum app-specific risk subjects, not a
complete regulated entity risk analysis.

## HSP-004 — Local identity and access boundary

**Architecture evidence.** [`ADR-004`](../../architecture/07-ADR-004-container-only-deployment-trust-model.md),
**Application identity boundary**, makes the authorized local OS account the
human authorization boundary and places host administrators and Docker-daemon
controllers inside the trust boundary. [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**Network, Host, Origin, and shared-path rules**, confirms that the application
has no authentication or authorization and arbitrary containers are
prohibited.

**HIPAA basis.** [45 CFR 164.308(a)(3)-(4)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires workforce security and access management. [45 CFR 164.312(a)(1),
(a)(2)(i), and (d)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312)
requires access controls, unique user identification, and person or entity
authentication for ePHI systems. HHS confirms in its [operating-system FAQ](https://www.hhs.gov/hipaa/for-professionals/faq/does-the-security-rule-mandate-minimum-operating-system-requirements/index.html)
that OS capabilities may support unique identification, audit, integrity,
authentication, and transmission safeguards, subject to risk analysis.

**Justification.** For a one-person, non-ePHI demonstrator, a unique OS
account plus restricted Docker access is the architecture-compatible access
boundary. Stating its limits is essential because loopback and Host/Origin
checks authenticate neither a human nor a role.

**Future evidence.** Access-boundary diagram; named operator; OS/Docker access
procedure and review; effective network/container membership; negative tests
for alternate state paths; documentation stating the lack of app identity.

**Limitation.** This is not sufficient access control or authentication for an
ePHI, multi-user, remote, or shared-workstation system.

## HSP-005 — Network and transmission confinement

**Architecture evidence.** [`AUTH-EX-001.6`](../../architecture/01-accepted-architecture-baseline.md)
requires loopback-only host publication. [`ARC-CTR-002`](../../architecture/13-record-http-contract.md),
**Protocol baseline**, and [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**Network, Host, Origin, and shared-path rules**, define the two HTTP entrances,
exact Host/Origin controls, private network, no proxy/CORS, and the requirement
for a successor identity/TLS/audit architecture before remote access.

**HIPAA basis.** [45 CFR 164.312(e)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312)
requires transmission security and addressable integrity/encryption measures.
[45 CFR 164.306(a), (b), and (d)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
requires protection against anticipated threats and risk-based treatment of
addressable controls. HHS's [encryption FAQ](https://www.hhs.gov/hipaa/for-professionals/faq/is-the-use-of-encryption-mandatory-in-the-security-rule/index.html)
requires a documented reasonable-and-appropriate decision rather than an
automatic omission.

**Justification.** Exact loopback/private confinement materially reduces the
demonstrator's network attack surface and matches the accepted no-auth design.
Because the architecture uses HTTP, excluding ePHI and remote transport avoids
an unsupported encryption conclusion.

**Future evidence.** Rendered Compose inspection; host, peer, arbitrary
container, IPv4/IPv6, wildcard, hostname, proxy, tunnel, and Origin/Host
reachability tests; traffic inventory; absence of outbound runtime traffic;
documented ePHI/TLS limitation.

**Limitation.** Local HTTP is a scoped architecture choice, not evidence that
transmission encryption is unnecessary in another environment.

## HSP-006 — Minimum data and safe presentation

**Architecture evidence.** [`ARC-CTR-001`](../../architecture/11-record-domain-contract.md)
classifies record values and full names as sensitive by default.
[`ARC-CTR-006`](../../architecture/20-cli-interaction-contract.md) restricts
diagnostics and process exposure; [`ARC-CTR-007`](../../architecture/22-web-interaction-contract.md)
forbids browser durable storage, third-party content, telemetry, values in
URLs/history, and unsafe rendering; [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md)
defines log redaction.

**HIPAA basis.** [45 CFR 164.306(a)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
requires confidentiality and protection from impermissible use or disclosure.
The Privacy Rule's minimum-necessary provisions at [45 CFR 164.502(b)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502)
and [164.514(d)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514),
explained in [HHS minimum-necessary guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html),
support limiting data and disclosures to what the purpose needs.

**Justification.** Even non-PHI demonstrator content can be sensitive or can
accidentally become identifying. Minimizing fixtures and preventing secondary
copies reduces both accidental ePHI entry and leakage while preserving the
architecture's explicit success-output behavior.

**Future evidence.** Fixture provenance and necessity review; repository,
image, log, history, browser-storage, network, screenshot, artifact, and
diagnostic leak tests; safe synthetic test vectors; output documentation.

**Limitation.** Minimum necessary is fact-specific and has regulatory
exceptions; this app policy does not decide a regulated entity's Privacy Rule
application.

## HSP-007 — Persistence, integrity, and controlled change

**Architecture evidence.** [`AUTH-EX-001.1`, `.5`, and `.12`](../../architecture/01-accepted-architecture-baseline.md)
require API-exclusive persistence, conditional updates, and isolated named
volumes. [`ARC-BND-003`](../../architecture/15-sqlite-store-boundary.md) and
[`ARC-CTR-004`](../../architecture/16-sqlite-persistence-contract.md) define
schema constraints, atomic transactions, instance exclusion, integrity
checks, migration hashes, and validated backup/restore. `ARC-CTR-009` provides
the `DB-*`, `HTTP-*`, and related conformance vectors.

**HIPAA basis.** [45 CFR 164.312(c)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312)
requires protection against improper alteration or destruction and an
addressable mechanism to corroborate integrity. [45 CFR 164.306(a)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
requires integrity and availability protection.

**Justification.** Centralized state authority, immutable identity, ETag
preconditions, transactions, hashes, and recovery validation are directly
relevant electronic mechanisms for detecting or preventing unauthorized or
unproven change.

**Future evidence.** Applicable `DOM-*`, `HTTP-*`, `DB-*`, `CNT-*`, and
`OPS-*` results; schema/migration hashes; fault and concurrency tests; mount
graph; integrity and restore results tied to exact images and volumes.

**Limitation.** These controls establish app/store integrity behavior only;
they do not prove that a human action was authorized or supply a per-user
audit trail.

## HSP-008 — Privacy-aware logging, activity review, and audit limitation

**Architecture evidence.** [`ARC-CTR-002`](../../architecture/13-record-http-contract.md),
**Contract rules**, explicitly provides request correlation and safe outcomes
but makes no audit-history claim. [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**Logging and diagnostics**, states that Docker logs are bounded diagnostics,
not an audit or recovery store, and **Backup, recovery, and incident handling**
states there is no per-user audit attribution.

**HIPAA basis.** [45 CFR 164.308(a)(1)(ii)(D)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires regular review of information-system activity records. [45 CFR
164.312(b)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312)
requires mechanisms to record and examine activity in systems that contain or
use ePHI.

**Justification.** Privacy-aware diagnostics are useful for development and
incident correlation but intentionally omit data and identity. The policy
requires appropriate review while making the unresolved audit-control boundary
visible rather than mislabelling diagnostics as compliance.

**Future evidence.** Log schema and redaction tests using sensitive synthetic
fixtures; rotation/size settings; review procedure, owner, trigger, sample
review record, and finding disposition; explicit negative audit claim in
release documentation.

**Limitation.** No evidence in this profile can establish per-user activity
tracking because application user identity does not exist.

## HSP-009 — Container, configuration, and supply-chain hardening

**Architecture evidence.** [`AUTH-EX-001.13`](../../architecture/01-accepted-architecture-baseline.md),
[`ADR-005`](../../architecture/08-ADR-005-containerized-technology-stack.md),
and [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**Mandatory service hardening** and **Image, build, and release identity**,
require non-root/read-only/capability constraints, pinned inputs, minimal
runtime contents, immutable digests, SBOM/provenance, resource bounds, and
vulnerability/license review.

**HIPAA basis.** Risk analysis and management are required by [45 CFR
164.308(a)(1)(ii)(A)-(B)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308),
and continuing maintenance by [45 CFR 164.306(e)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306).
HHS's [January 2026 system-hardening guidance](https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity-newsletter-january-2026/index.html)
specifically discusses patching, removing unnecessary services, enabling
security measures, baselines, asset inventories, vulnerability scanning, and
ongoing risk treatment. [NIST SP 800-66 Rev. 2](https://csrc.nist.gov/pubs/sp/800/66/r2/final)
is additional nonbinding HIPAA implementation guidance.

**Justification.** The future app's security depends materially on the host,
Docker daemon, images, OS libraries, Python stack, SQLite, browser bundle, and
dependency chain. Minimal, traceable, bounded artifacts reduce the attack
surface and make risk decisions reviewable.

**Future evidence.** Exact digest and lock records; SBOM/provenance/signature
policy results; supported-platform tests; image/layer/content scans; effective
security setting probes; vulnerability and patch review with owner and
time-bounded disposition.

**Limitation.** A clean scan is time-bound and cannot prove the absence of
unknown vulnerabilities or overall HIPAA compliance.

## HSP-010 — Backup, recovery, and emergency access

**Architecture evidence.** [`ARC-CTR-004`](../../architecture/16-sqlite-persistence-contract.md),
**Backup and restore contract**, defines exact, validated, rollback-capable
offline recovery. [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**Lifecycle contract** and **Backup, recovery, and incident handling**, makes
pre-migration backup mandatory, identifies same-host limitations, and requires
protected off-volume exports when host-loss recovery is needed.

**HIPAA basis.** [45 CFR 164.308(a)(7)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires backup, disaster recovery, emergency-mode operation, and addressable
testing/criticality analysis. [45 CFR 164.310(d)(2)(iv)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310)
addresses exact copies before media movement. [45 CFR
164.312(a)(2)(ii)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312)
requires an emergency access procedure for ePHI systems.

**Justification.** The architecture already supplies a narrow, testable
contingency mechanism. Requiring a declared recovery objective, pre-change
backup, restore proof, and protected off-volume handling converts that design
into prospective availability and integrity obligations without adding an
unsafe bypass.

**Future evidence.** Data criticality/recovery objective; backup metadata and
hash; stopped-API/networkless/mutual-exclusion proof; restore/rollback drill;
off-volume protection, encryption decision, and custody evidence when
applicable; runbook and reviewer.

**Limitation.** One same-host backup volume is not disaster recovery from host
loss, and the architecture makes no high-availability or zero-downtime claim.

## HSP-011 — Workstation, physical, and media safeguards

**Architecture evidence.** [`ADR-004`](../../architecture/07-ADR-004-container-only-deployment-trust-model.md)
makes the host OS account and Docker daemon the administrative boundary.
[`ARC-BND-003`](../../architecture/15-sqlite-store-boundary.md) prohibits
removable, network, cloud-sync, bind-mounted, and direct-host live storage.
[`ARC-CTR-008`](../../architecture/23-operations-security-contract.md) defines
host exports, destructive-command handling, and sensitive backup protection.

**HIPAA basis.** [45 CFR 164.310(a)-(d)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310)
requires facility access, workstation use/security, and device/media controls,
including disposal and media reuse. [45 CFR 164.312(a)(2)(iii)-(iv)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312)
identifies automatic logoff and encryption/decryption as addressable access
controls. HHS's [encryption FAQ](https://www.hhs.gov/hipaa/for-professionals/faq/is-the-use-of-encryption-mandatory-in-the-security-rule/index.html)
and [system-hardening guidance](https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity-newsletter-january-2026/index.html)
support risk-based encryption and host hardening decisions.

**Justification.** Anyone controlling the local workstation or Docker daemon
can inspect the app. Physical control, a unique login, screen locking, and an
explicit risk-based host/backup encryption decision are therefore directly
relevant inherited safeguards. Media custody and sanitization address exported
backup copies that leave named volumes.

**Future evidence.** Supported-host baseline and patch record; documented
addressable encryption decision and implementation evidence when selected; OS
authentication and risk-selected lock configuration; physical-use
instructions; media/export inventory, custody, and sanitization record;
destructive-command warnings and tests.

**Limitation.** HIPAA does not prescribe a universal lock interval or one
encryption outcome. This suite does not define a complete facility security
program or claim that inherited operator controls are implemented by the app.

## HSP-012 — Security incident and possible-breach response

**Architecture evidence.** [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**Backup, recovery, and incident handling**, requires stop/preserve/hash/
restore behavior for corruption or suspected disclosure and identifies no
remote incident responder or per-user attribution.

**HIPAA basis.** [45 CFR 164.308(a)(6)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires identification, response, mitigation, and documentation of security
incidents. The [HHS Breach Notification Rule guidance](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html)
explains the assessment and notification duties for breaches of unsecured PHI
under 45 CFR 164.400-414 and the need to preserve proof of notification or a
decision that notification was not required.

**Justification.** The architecture has concrete containment and evidence
preservation mechanisms, but only the owning organization can determine
whether PHI and notification duties are involved. Immediate escalation avoids
developers making unauthorized legal conclusions.

**Future evidence.** Incident runbook and contacts; table-top exercise; test of
stop/preserve/recovery paths using synthetic data; incident record template;
link to the organization's privacy/legal/breach process.

**Limitation.** This policy neither performs the four-factor breach assessment
nor determines notification obligations.

## HSP-013 — External services and business-associate boundary

**Architecture evidence.** [`ADR-005`](../../architecture/08-ADR-005-containerized-technology-stack.md)
limits network use to declared build input retrieval. [`ARC-CTR-007`](../../architecture/22-web-interaction-contract.md)
forbids third-party browser content and telemetry. [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md)
requires no outbound runtime dependency or telemetry and excludes secrets and
data from build/release artifacts.

**HIPAA basis.** [45 CFR 164.308(b)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires satisfactory assurances before a business associate or subcontractor
handles ePHI. [45 CFR 164.314(a)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.314)
specifies required written arrangements and downstream obligations.

**Justification.** Preserving a self-contained runtime and keeping record data
out of build/support services minimizes unreviewed disclosure paths. A future
external processor changes both the legal relationship and the architecture,
so vendor paperwork alone cannot authorize it.

**Future evidence.** Runtime egress and browser dependency inventory;
build/CI/registry data-flow review; negative data-leak tests; an explicit
vendor/BAA gate in any successor initiative.

**Limitation.** This policy does not supply agreement language or decide
whether a particular vendor is a business associate.

## HSP-014 — Verification, documentation, retention, and review

**Architecture evidence.** [`ARC-CTR-009`](../../architecture/24-conformance-contract.md)
defines stable vectors, environment identity, negative tests, delivery gates,
and evidence fields. The [Codex evidence authority specification](../../LLM/01_Codex_Evidence_Authority_Specification.md)
requires precise source-to-product-to-verification traceability and truthful
limitations.

**HIPAA basis.** [45 CFR 164.308(a)(8)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308)
requires periodic technical and nontechnical evaluation. [45 CFR 164.316](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.316)
requires written policies and records, six-year retention, availability, and
updates. [45 CFR 164.306(e)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
requires review and modification of safeguards as needed.

**Justification.** Future claims are credible only when evidence identifies the
exact requirement, artifact, environment, method, result, and limitation. A
source-currency check is necessary because law and guidance can change after
this policy revision.

**Future evidence.** Complete `SEC-HIPAA-DEV-001` record; applicable
`ARC-CTR-009` vectors; policy source mapping; source-currency review;
evaluation record; retention/availability owner and schedule.

**Limitation.** Git improves traceability but is not automatically a compliant
records-management, access, backup, or six-year retention system.

## HSP-015 — Successor architecture and exception gate

**Architecture evidence.** [`ARC-SUITE-001`](../../architecture/00-architecture-suite-index.md),
**Explicit exclusions**, excludes accounts, roles, remote multi-user access,
and audit history. [`ADR-004`](../../architecture/07-ADR-004-container-only-deployment-trust-model.md),
**Costs, risks, and required follow-up**, and [`ARC-CTR-008`](../../architecture/23-operations-security-contract.md),
**HTTP and browser security**, require a successor identity, TLS/proxy,
authorization, audit, privacy, rate-limit, and incident architecture for
remote or multi-user use.

**HIPAA basis.** [45 CFR 164.306(c)-(e)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306)
requires compliance with applicable standards, the documented addressable
process, and continuing maintenance. The applicable safeguard families are
set out in [45 CFR 164.308](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308),
[164.310](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310),
[164.312](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312),
[164.314](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.314),
and [164.316](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.316).

**Justification.** Permitting ePHI would invalidate central premises of the
accepted design. A successor design, not an operational waiver, is required to
resolve identity, audit, encryption, transmission, organizational, recovery,
and legal obligations coherently.

**Future evidence.** Explicit project-authority instruction; focused design
initiative; current legal/risk analysis; accepted successor architecture;
compatibility/migration/recovery effects; updated policies and contracts;
separately accepted implementation initiatives and conformance evidence.

**Limitation.** The minimum subjects listed in `HSP-015` are a design-entry
gate, not a complete HIPAA checklist or a predetermined technical solution.

## Completeness assertion

`SEC-HIPAA-POL-001` defines exactly 15 normative policy IDs, `HSP-001` through
`HSP-015`. This mapping contains one corresponding justification entry for
each ID. Future additions require a new stable policy ID and a matching
architecture/HIPAA/evidence/limitation entry in the same authorized revision.

