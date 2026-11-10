# Prospective HIPAA-aligned security policy

**Policy ID:** `SEC-HIPAA-POL-001`  
**Revision:** `1.0.1`  
**Status:** Accepted prospective policy  
**Owner:** User, project authority  
**Applies to:** Future TADp example-app initiatives and delivery units `D2`-`D6`  
**Architecture input:** [`ARC-SUITE-001@2.0.1`](../../architecture/00-architecture-suite-index.md)  
**Complete rationale:** [`SEC-HIPAA-MAP-001`](03-control-rationale-and-traceability.md)  
**Applicable peer policy:** [`SEC-NIST-SUITE-001@1.0.1`](../NIST/00-nist-security-policy-suite-index.md)  

## Reconciliation standing

This policy applies together with architecture `2.0.1` and NIST policy `1.0.1`.
This policy remains primary for its security and data-use scope and guides the
architecture, whose technical design must stay within these requirements. The
security suites require independent evidence. `RZN-001` supplies
historical intent only: its free-text model and previously open questions do
not authorize actual or possible ePHI or any successor-gate trigger.

## Policy objective

Future development must preserve the demonstrator's accepted local trust
boundary while applying reasonable, architecture-relevant safeguards derived
from the currently effective HIPAA Security Rule. The objective is to produce
a demonstrator whose security decisions, limitations, and verification are
explicit and traceable without representing it as a regulated ePHI system.

## Applicability

These policies apply to future specifications, source code, dependencies,
containers, Compose configuration, API, SQLite store, SDK, CLI, browser app,
test fixtures, logs, backup artifacts, release material, and operating
instructions for the example application.

Each `HSP-*` section below is one normative policy. Its linked entry in
[`SEC-HIPAA-MAP-001`](03-control-rationale-and-traceability.md) supplies the
required architecture evidence, HIPAA source, justification, and future proof.
No policy is considered implemented merely because it appears here.

## HSP-001 — Prospective standing and truthful claims

Future work must treat this suite as a design and delivery constraint, not as
evidence of current product behavior. Initiative, product, release, and user
documentation must distinguish all of the following:

- a policy requirement;
- an implemented control;
- passing verification for a named artifact and environment; and
- an organization-level HIPAA compliance conclusion.

Only the first is established by this suite. A future product may claim
conformance to named `HSP-*` policies only when its accepted initiative links
passing evidence for the exact artifact and architecture revision. No product
or repository may be described as "HIPAA compliant," "HIPAA certified," or
approved for ePHI on the strength of this policy, an architecture document, a
scanner result, or a local test.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-001--prospective-standing-and-truthful-claims)

## HSP-002 — Synthetic or documented de-identified data only

The accepted demonstrator profile must use only:

1. purpose-created synthetic data that is not derived from a real person; or
2. data accompanied by an organization-owned record showing that it was
   de-identified through Expert Determination or Safe Harbor under 45 CFR
   164.514 and that no actual knowledge defeats that determination.

Future fixtures, examples, screenshots, demonstrations, seed files, backup
drills, and tests must follow the same restriction. The app must not claim to
perform or validate de-identification. Its generated record UUID is an
application identity, not proof that the `name` or free-text `value` is
de-identified.

A HIPAA de-identification determination does not override
[`SEC-NIST-POL-001`, `SEC-POL-01`](../NIST/01-demonstrator-security-policy.md#sec-pol-01---authorized-use-and-information-boundary):
production records, confidential business data, and other information whose
loss or disclosure requires controls outside the demonstrator profile remain
prohibited even when they are not PHI.

If provenance or de-identification evidence is absent, incomplete, or
ambiguous, the data must be treated as possible ePHI and must not be entered,
imported, pasted, streamed, restored, or displayed in the demonstrator. A
future regulated-data request must follow `HSP-015`; it cannot be accepted as
a routine policy exception.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-002--synthetic-or-documented-de-identified-data-only)

## HSP-003 — Assigned security responsibility and risk management

Every future initiative that changes a security-relevant part of `D2`-`D6`
must identify one accountable security owner. Before execution, the initiative
must contain or link an application-specific risk analysis covering at least:

- every path by which record data could be created, received, maintained,
  transmitted, displayed, logged, backed up, exported, or placed in a test or
  build artifact;
- the host OS, browser, Docker daemon/Desktop VM, Compose services, images,
  private network, named volumes, logs, backup exports, build/registry path,
  developer tooling, and physical workstation;
- threats, vulnerabilities, likelihood, impact, existing safeguards,
  residual risk, owner, and disposition; and
- each addressable HIPAA implementation specification relevant to the change,
  with the required implementation or documented alternative analysis.

The analysis must be reviewed after a material architecture, dependency,
host, deployment, data-flow, threat, incident, or legal-source change. A risk
acceptance may authorize only a lawful, architecture-compatible residual risk;
it may not authorize ePHI in the current profile or erase a failing gate.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-003--assigned-security-responsibility-and-risk-management)

## HSP-004 — Local identity and access boundary

Future products and operating documentation must preserve the architecture's
single-user identity model:

- one named, authorized person uses one unique host OS account for a
  demonstrator instance;
- shared OS accounts, guest use, simultaneous users, unattended public
  access, and credential sharing are prohibited;
- membership in the host administrator/root and Docker-daemon control groups
  is restricted to explicitly authorized operators and reviewed when access
  changes;
- only declared project containers may attach to `record-net`; the CLI, web,
  tests, build containers, and host must not acquire a second path to live
  SQLite state; and
- termination or role change must remove OS, Docker, backup, and repository
  access through the owning organization's access process.

The application has no accounts, roles, login, sessions, or per-user
authorization. Future documentation must say so and must not present exact
Host/Origin checking, loopback, a UUID, or possession of the Compose files as
person authentication. Multi-user or regulated access requires `HSP-015`.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-004--local-identity-and-access-boundary)

## HSP-005 — Network and transmission confinement

Future implementations must enforce the exact accepted topology:

- the only host publication is
  `127.0.0.1:${RECORDS_HOST_PORT}:8000`;
- only declared services attach to the private `record-net` network;
- CLI/SDK traffic uses `http://record-api:8000/api/v1` inside that network;
- browser traffic uses the exact loopback same origin and the same `/api/v1`
  contract;
- Host and browser Origin checks fail closed before body processing;
- CORS, proxy-derived identity, wildcard/IPv6/LAN binding, host networking,
  tunnels, port forwarding, reverse proxies, public exposure, runtime
  telemetry, and arbitrary outbound runtime dependencies remain absent; and
- future verification must prove both permitted paths and prohibited
  reachability.

HTTP without TLS is permitted only inside this local, non-ePHI profile. The
policy makes no claim that loopback HTTP or the private Docker bridge satisfies
an ePHI transmission-security determination. Any remote or ePHI transmission
requires a successor architecture under `HSP-015`.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-005--network-and-transmission-confinement)

## HSP-006 — Minimum data and safe presentation

Future development must minimize data used, retained, exposed, and reproduced:

- fixtures and demonstrations contain only the smallest synthetic or
  documented de-identified content needed for the exact test or scenario;
- record `value` and full `name` are treated as sensitive by default even in
  the demonstrator profile;
- record data and raw searches must not enter source control, commit messages,
  issue trackers, chat or AI prompts, CI annotations, image layers, SBOMs,
  provenance, environment variables, command histories, process titles,
  URLs, browser history, telemetry, screenshots, or support bundles;
- browser record state remains in memory only, API/data responses remain
  `no-store`, record text is rendered only as text, and third-party browser
  content and storage remain absent;
- CLI success output may contain the explicitly requested synthetic or
  de-identified record, but diagnostics, logs, completion data, and process
  metadata must not amplify it; and
- any evidence artifact must use safe identifiers, hashes, counts, and
  redacted excerpts rather than record content unless the exact test requires
  a purpose-created synthetic value.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-006--minimum-data-and-safe-presentation)

## HSP-007 — Persistence, integrity, and controlled change

Future products must preserve the architecture's integrity model:

- the API is the sole normal runtime reader/writer of the live SQLite store;
- the live database remains in `record-data`; clients, build/test services,
  the host, and arbitrary containers never mount or open it;
- maintenance is networkless, allowlisted, and mutually exclusive with the
  stopped API through the shared instance lock;
- writes use validated parameterized operations and atomic transactions;
- record identity and creation order remain immutable, updates require the
  current strong ETag, and force/last-write-wins paths remain absent;
- startup and maintenance verify ownership, application/schema/migration
  identity, row invariants, and SQLite integrity before a ready or successful
  claim; and
- migrations, image changes, restores, and backup artifacts retain hashes,
  versions, provenance, pre-change recovery, and truthful failure behavior.

No future implementation may trade these controls for convenience or use a
successful response, health check, or log entry as proof of a committed or
intact record when the authoritative transaction/evidence says otherwise.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-007--persistence-integrity-and-controlled-change)

## HSP-008 — Privacy-aware logging, activity review, and audit limitation

Future application and container logs must remain bounded, structured,
local, and redacted as required by `ARC-CTR-008`. They may contain safe event,
route-template, status, duration, request ID, build identity, and error-code
metadata, but never record values, full names, raw bodies/searches/regexes,
ETags, cursors, bound SQL values, secrets, environment contents, backup bytes,
or unredacted stack data.

Future operating documentation must define who reviews Docker, host, build,
vulnerability, maintenance, and incident records, the review trigger or
frequency selected by the risk analysis, and how findings are recorded and
routed. Security-relevant records must be preserved when an incident is
suspected.

These diagnostic and development records are **not** a HIPAA audit-control
system and do not provide per-user activity attribution. Future work must not
make that claim. An initiative proposing ePHI must resolve audit controls and
information-system activity review through `HSP-015` before implementation.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-008--privacy-aware-logging-activity-review-and-audit-limitation)

## HSP-009 — Container, configuration, and supply-chain hardening

Future build and release work must implement and verify the accepted hardened
baseline, including:

- immutable digest-qualified images and locked or hashed dependencies;
- reviewed provenance, SBOM, licenses, supported platforms, and vulnerability
  findings for the exact released artifacts;
- minimal runtime contents with no compiler, package-manager cache, test
  fixtures, source checkout, host toolchain dependency, or embedded secret;
- numeric non-root user `10001:10001`, read-only root filesystem, bounded
  `tmpfs`, all capabilities dropped, `no-new-privileges`, no Docker socket or
  host namespaces/devices, and enforced CPU/memory/PID/log bounds;
- closed, typed configuration that fails on unsafe or unknown input; and
- timely assessment of supported host, Docker, browser, image, OS-library,
  Python, SQLite, RE2, SDK, and web dependency vulnerabilities and patches.

A material vulnerability, unsupported component, provenance mismatch, or
ignored platform security setting blocks the affected release until an owner
records remediation or an explicit, time-bounded, risk-based disposition.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-009--container-configuration-and-supply-chain-hardening)

## HSP-010 — Backup, recovery, and emergency access

Future operations and product documentation must implement the architecture's
offline backup and restore contracts and must define the data criticality and
recovery objective appropriate to the demonstrator use. At minimum:

- a validated backup is required before every migration and before a change
  that could make the current store unreadable;
- backup, export, import, restore, and integrity work runs only in the
  networkless, stopped-API maintenance boundary under exclusive ownership;
- backup candidates are new, hashed, schema/row/integrity checked, and kept in
  `record-backups`, separate from live state;
- a future release must exercise a restore drill and prove the expected
  record/search/metadata result and rollback behavior before claiming the
  recovery control;
- same-host backups must be described as protection from logical failure, not
  host loss;
- an off-volume export, when the declared recovery objective requires one,
  must use the validated opaque bundle, a destination protected according to
  the content and the documented encryption decision, documented custody, and
  a tested import/restore path; and
- emergency access is a documented recovery procedure, never a hidden bypass,
  direct SQLite access, authentication override, or unsafe always-on service.

Backups inherit the sensitivity and use restrictions of their source data.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-010--backup-recovery-and-emergency-access)

## HSP-011 — Workstation, physical, and media safeguards

Future user and operator documentation must define a supported host baseline
for the local trust boundary. The baseline must require:

- a vendor-supported, security-patched host OS, Docker/Compose platform, and
  browser, with host firewall and endpoint protections selected by the owning
  organization's risk analysis;
- a documented addressable-control decision for encryption of host storage
  containing Docker state and of every authorized backup destination,
  including the implementation, or the reason and equivalent alternative
  measure required by 45 CFR 164.306(d)(3); an ePHI-driven encryption
  requirement triggers `HSP-015` rather than changing this profile silently;
- a unique authorized OS account protected by the organization's
  authentication policy, with an automatic screen-lock interval selected and
  documented through its risk analysis and manual lock whenever the operator
  leaves the workstation;
- physical placement and screen handling that prevent unauthorized viewing,
  theft, tampering, and use of the local loopback application;
- no live or backup state on removable, network, cloud-synchronized, shared,
  or untracked media; and
- documented custody, movement, reuse, and final sanitization or destruction
  for any media that held a backup export or Docker data.

These are inherited operator and organization dependencies, not controls
implemented by the demonstrator application. HIPAA does not prescribe a
universal screen-lock interval or a single encryption decision; the owning
organization must preserve the risk-based parameters and rationale. Removing
a Docker volume, using `docker compose down -v`, deleting a file, or emptying
a trash directory must not be represented as verified media sanitization.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-011--workstation-physical-and-media-safeguards)

## HSP-012 — Security incident and possible-breach response

Future runbooks must define a security incident to include, at minimum:

- actual or suspected real-person health information entering the system;
- non-loopback, proxy, tunnel, public, LAN, or unauthorized-container
  reachability;
- unauthorized host, Docker, volume, backup, repository, terminal, browser,
  or log access;
- record data in a prohibited log, cache, URL, screenshot, artifact, service,
  or communication;
- image/provenance compromise, malware, lost media, integrity failure,
  destructive command, or unexplained data change; and
- loss of the ability to prove whether a write, backup, restore, or migration
  succeeded.

The runbook must direct the operator to stop affected access without altering
source evidence, preserve the volume/WAL/SHM/lock, logs, effective Compose
configuration, image and artifact identities, hashes, and backups, notify the
named security owner, contain and mitigate harm, document actions and outcome,
and recover only through the accepted maintenance path.

If possible PHI is involved, the security owner must immediately route the
event to the owning organization's privacy/legal/breach process. The app,
developer, and this suite do not decide whether notification is required.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-012--security-incident-and-possible-breach-response)

## HSP-013 — External services and business-associate boundary

Future runtime products must preserve the architecture's absence of outbound
dependencies, telemetry, analytics, remote assets, and third-party browser
content. Build and registry access may retrieve pinned development inputs but
must never receive record data, live volumes, backups, logs containing record
content, or real-person fixtures.

Before a future service, support provider, cloud platform, CI system, registry,
monitoring product, or subcontractor is allowed to create, receive, maintain,
or transmit ePHI on behalf of a regulated entity, the owning organization must
complete the applicable vendor risk review and written business-associate or
other required arrangement. That event also triggers `HSP-015`; an agreement
alone does not make the current architecture suitable for ePHI.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-013--external-services-and-business-associate-boundary)

## HSP-014 — Verification, documentation, retention, and review

Every future initiative in scope must:

- source-map each applicable `HSP-*` policy to its specification, product
  destination, and exact verification;
- execute the applicable architecture vectors plus the policy-specific
  evidence in [`SEC-HIPAA-DEV-001`](04-future-development-and-evidence-standard.md);
- preserve exact artifact, image, dependency, source commit, architecture,
  policy, environment, method, result, limitation, reviewer, and date identity;
- treat every failed, skipped, unavailable, or non-applicable check as an
  explicit disposition rather than silently excluding it;
- recheck the current regulation, official HHS guidance, risks, and policy
  fit at initiative alignment and before release; and
- update affected policies, procedures, and evidence after environmental or
  operational change.

When adopted by a HIPAA regulated entity, the entity must retain the written
policies and required action/activity/assessment records for at least six
years from creation or last effective date, whichever is later, make them
available to responsible people, and apply any longer organizational or legal
schedule. Git history may contribute to integrity and traceability but must
not be claimed as the complete legal retention system without evidence.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-014--verification-documentation-retention-and-review)

## HSP-015 — Successor architecture and exception gate

The current suite has no exception path that permits actual or possible ePHI.
Any request for ePHI, production clinical use, multiple users, remote access,
shared workstations, third-party record processing, or another excluded
deployment must stop before implementation and create a separately governed
successor architecture/design initiative.

That work must reassess the complete HIPAA and organizational scope and must,
at minimum, decide and verify:

- unique application identity, authentication, authorization, access review,
  termination, emergency access, and automatic logoff;
- audit controls, per-user attribution, activity review, retention, and
  tamper protection;
- encryption and key management for live data, backups, exports, and every
  transmission path, including TLS/proxy trust for any network exposure;
- secrets, session, CSRF, rate-limit, remote administration, monitoring, and
  incident-response architecture;
- regulated-entity responsibilities, workforce procedures, physical
  safeguards, vendor/business-associate arrangements, Privacy Rule, Breach
  Notification Rule, data retention/disposal, and applicable state law; and
- migration, compatibility, recovery, threat, and conformance consequences
  for every current component and consumer.

For in-profile addressable specifications, an alternative may be used only
after the `HSP-003` assessment documents why the specification is not
reasonable and appropriate and identifies an equivalent alternative when
reasonable and appropriate. No exception may contradict an invariant, waive a
required HIPAA standard, or turn missing evidence into a passing claim.

[Rationale and required evidence](03-control-rationale-and-traceability.md#hsp-015--successor-architecture-and-exception-gate)

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established policies `HSP-001` through `HSP-015` | User's HIPAA policy instruction and future-development clarification |
| 2026-11-10 | `1.0.1` | Made policy primacy and the architecture, NIST, and RZN-001 relationship explicit without changing a policy outcome | User's explicit reconciliation instruction and policy-primacy clarification |

