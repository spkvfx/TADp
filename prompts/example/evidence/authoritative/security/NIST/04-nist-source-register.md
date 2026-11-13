# NIST source register

**Register ID:** `SEC-NIST-SRC-001`  
**Revision:** `1.0.1`  
**Status:** Accepted source register  
**Owner and accepting authority:** User, project authority  
**Effective date:** 2026-11-10  
**Governing suite:** [`SEC-NIST-SUITE-001`](00-nist-security-policy-suite-index.md)  
**Source access date:** 2026-11-10  

## Purpose

This register preserves the official NIST publication identities, versions,
and locators used to justify the prospective TADp demonstrator security
policies. Only final NIST publications are normative alignment sources for
this revision. The architecture is technical input describing the system;
the accepted security policy remains primary for its scope, and these NIST
sources justify its selected security outcomes.

The summaries below are project paraphrases, not substitutes for the source
text. NIST identifiers are kept so future reviewers can inspect the complete
context, organization-defined parameters, related controls, examples, and
limitations before applying a requirement.

## Registered publications

| Source ID | Official final publication | Version/date used | Project use | Official locator |
|---|---|---|---|---|
| `NIST-CSF2` | *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29 | Final, 2024-02-26 | Risk-governance and outcome taxonomy used to organize the limited profile | [NIST publication page](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20); [DOI](https://doi.org/10.6028/NIST.CSWP.29) |
| `NIST-80053` | *Security and Privacy Controls for Information Systems and Organizations*, NIST SP 800-53 Rev. 5 | September 2020, including the official Release 5.2.0 minor update issued 2025-08-27 | Specific control objectives used as policy rationale; no baseline or full-control implementation claim | [CSRC final publication and Release 5.2.0 note](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final); [DOI](https://doi.org/10.6028/NIST.SP.800-53r5) |
| `NIST-80053A` | *Assessing Security and Privacy Controls in Information Systems and Organizations*, NIST SP 800-53A Rev. 5 | Final, January 2022, including the official Release 5.2.0 minor update issued 2025-08-27 | `EXAMINE`, `INTERVIEW`, and `TEST` method vocabulary for prospective assurance; no current assessment result | [CSRC final publication and Release 5.2.0 note](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final); [DOI](https://doi.org/10.6028/NIST.SP.800-53Ar5) |
| `NIST-800190` | *Application Container Security Guide*, NIST SP 800-190 | Final, September 2017 | Container image, registry, network, runtime, host-mount, vulnerability, and incident guidance | [CSRC final publication](https://csrc.nist.gov/pubs/sp/800/190/final); [DOI](https://doi.org/10.6028/NIST.SP.800-190) |
| `NIST-800218` | *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities*, NIST SP 800-218 | Final, February 2022 | Secure-development, release-integrity, configuration, and vulnerability-response practices | [CSRC final publication](https://csrc.nist.gov/pubs/sp/800/218/final); [DOI](https://doi.org/10.6028/NIST.SP.800-218) |

NIST CSF 2.0 is non-prescriptive and supplies high-level outcomes. NIST SP
800-53 is a flexible control catalog. This project therefore cites outcomes
and controls as rationale and tailors them to the accepted architecture; it
does not treat the crosswalk as one-to-one equivalence or certification.

NIST SP 800-218 Version 1.1 is the final SSDF source for this revision. A draft
or potential update does not silently replace it. A later final publication
must pass the maintenance review below before it can change project policy.

## CSF 2.0 outcome locators

| Function/category used | Relevance to this suite | Project policies |
|---|---|---|
| `GOVERN`: Organizational Context (`GV.OC`), Roles/Responsibilities/Authorities (`GV.RR`), Policy (`GV.PO`), Oversight (`GV.OV`), and Cybersecurity Supply Chain Risk Management (`GV.SC`) | Establish boundary, ownership, policy control, review, and supply-chain risk decisions | `SEC-POL-01`, `04`, `10`, `11`, `14` |
| `IDENTIFY`: Risk Assessment (`ID.RA`) | Relate policy and vulnerability decisions to the local demonstrator risk and data boundary | `SEC-POL-01`, `12`, `14` |
| `PROTECT`: Data Security (`PR.DS`), Platform Security (`PR.PS`), and Technology Infrastructure Resilience (`PR.IR`) | Protect data, immutable configuration, container/runtime boundaries, safe processing, and availability | `SEC-POL-02` through `10` as mapped in `SEC-NIST-MAP-001` |
| `DETECT`: Continuous Monitoring (`DE.CM`) | Support bounded diagnostic monitoring and ongoing vulnerability awareness | `SEC-POL-08`, `12` |
| `RESPOND`: Incident Management (`RS.MA`), Incident Analysis (`RS.AN`), and Incident Mitigation (`RS.MI`) | Structure local incident triage, evidence preservation, containment, and correction | `SEC-POL-13` |
| `RECOVER`: Incident Recovery Plan Execution (`RC.RP`) | Restore validated artifacts and data to a known state and verify recovery | `SEC-POL-09`, `13` |

## SP 800-53 Rev. 5 control locators

The project uses the following base controls and the one explicitly named
enhancement. Each row states only the aspect relied on by the associated
project policies.

| Control | Relied-on outcome | Project policies |
|---|---|---|
| `AC-3` Access Enforcement | Enforce approved logical access to resources | `SEC-POL-02`, `05` |
| `AC-6` Least Privilege | Give users and processes only necessary authority | `SEC-POL-03`, `05` |
| `AU-2` Event Logging | Select and justify security-relevant event types | `SEC-POL-08` |
| `AU-3` Content of Audit Records | Capture useful event context while recognizing record-content risk | `SEC-POL-08` |
| `AU-4` Audit Log Storage Capacity | Allocate and manage bounded log capacity | `SEC-POL-08` |
| `CA-2` Control Assessments | Use scoped assessment plans, methods, and evidence | `SEC-POL-11` |
| `CM-2` Baseline Configuration | Establish and maintain a reviewed baseline | `SEC-POL-04` |
| `CM-3` Configuration Change Control | Analyze, authorize, document, and review controlled change | `SEC-POL-04`, `14` |
| `CM-6` Configuration Settings | Establish and enforce restrictive settings | `SEC-POL-03`, `04` |
| `CM-7` Least Functionality | Limit functions, ports, protocols, services, and software to need | `SEC-POL-02`, `03` |
| `CP-9` System Backup | Back up system information at a risk-appropriate frequency and protect backups | `SEC-POL-09` |
| `CP-10` System Recovery and Reconstitution | Restore components to a known state after disruption or failure | `SEC-POL-09`, `13` |
| `CP-10(2)` Transaction Recovery | Recover transaction-based systems after disruption | `SEC-POL-05`, `09` |
| `IR-4` Incident Handling | Prepare for, detect/analyze, contain, eradicate, recover, and learn from incidents | `SEC-POL-13` |
| `PL-2` System Security and Privacy Plans | Document system boundary, environment, requirements, and protection approach | `SEC-POL-01`, `14` |
| `RA-3` Risk Assessment | Assess threats, vulnerabilities, likelihood, impact, and risk | `SEC-POL-01`, `14` |
| `RA-5` Vulnerability Monitoring and Scanning | Monitor, scan, analyze, and remediate relevant vulnerabilities | `SEC-POL-12` |
| `SA-11` Developer Testing and Evaluation | Plan and perform developer analysis/testing, preserve evidence, and correct flaws | `SEC-POL-11` |
| `SC-5` Denial-of-Service Protection | Protect against or limit effects of resource-exhaustion conditions | `SEC-POL-07` |
| `SC-6` Resource Availability | Allocate resources by priority, quota, or other limitation | `SEC-POL-03`, `07` |
| `SC-7` Boundary Protection | Monitor and control communications at external and key internal interfaces | `SEC-POL-02` |
| `SC-18` Mobile Code | Define, authorize, monitor, and control mobile-code technologies | `SEC-POL-06` |
| `SI-2` Flaw Remediation | Identify, test, install, and track security-relevant corrections | `SEC-POL-12` |
| `SI-4` System Monitoring | Monitor the system for events and indicators relevant to security | `SEC-POL-08` |
| `SI-7` Software, Firmware, and Information Integrity | Detect and respond to unauthorized changes and integrity failures | `SEC-POL-04`, `05`, `09`, `10`, `13` |
| `SI-10` Information Input Validation | Check external input validity and prevent input data becoming control information | `SEC-POL-06`, `07` |
| `SI-11` Error Handling | Produce useful errors without exposing exploitable or sensitive detail | `SEC-POL-06` |
| `SR-3` Supply Chain Controls and Processes | Define and apply supply-chain controls across the lifecycle | `SEC-POL-10` |
| `SR-4` Provenance | Preserve and validate component provenance | `SEC-POL-10` |
| `SR-11` Component Authenticity | Validate component authenticity and address counterfeit/substituted components | `SEC-POL-10` |

## SP 800-218 SSDF Version 1.1 task locators

| Practice/task | Relied-on outcome | Project policies |
|---|---|---|
| `PO.1` Define Security Requirements for Software Development | Identify, maintain, communicate, and manage security requirements and exceptions | `SEC-POL-11`, `14` |
| `PS.2` Provide a Mechanism for Verifying Software Release Integrity | Make release-integrity verification information available | `SEC-POL-10` |
| `PS.3` Archive and Protect Each Software Release | Protect release files, integrity information, provenance, and SBOM data | `SEC-POL-10` |
| `PW.1` Design Software to Meet Security Requirements and Mitigate Security Risks | Model risk, classify data, preserve decisions, and justify any relaxation | `SEC-POL-01`, `14` |
| `PW.4` Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality | Select, review, maintain, and track third-party components | `SEC-POL-10` |
| `PW.5` Create Source Code by Adhering to Secure Coding Practices | Apply input validation, output encoding, safe errors/logging, and other secure coding practices | `SEC-POL-06`, `08`, `11` |
| `PW.7` Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements | Scope, conduct, record, and triage code review and analysis | `SEC-POL-11` |
| `PW.8` Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements | Scope, conduct, record, and triage executable-code security testing | `SEC-POL-11` |
| `PW.9` Configure Software to Have Secure Settings by Default | Define, implement, document, verify, and change-control secure defaults | `SEC-POL-04` |
| `RV.1` Identify and Confirm Vulnerabilities on an Ongoing Basis | Gather credible reports and analyze/test code and components | `SEC-POL-12` |
| `RV.2` Assess, Prioritize, and Remediate Vulnerabilities | Evaluate risk, plan remediation, and communicate resolution | `SEC-POL-12` |
| `RV.3` Analyze Vulnerabilities to Identify Their Root Causes | Find root causes and improve practices to prevent recurrence | `SEC-POL-12` |

## SP 800-190 section locators

| Section | Relied-on container-security guidance | Project policies |
|---|---|---|
| `4.1.1` Image vulnerabilities | Use container-aware image vulnerability management across the lifecycle and enforce quality gates | `SEC-POL-10`, `12` |
| `4.1.2` Image configuration defects | Validate secure image configuration, use non-privileged users, trusted/minimal bases, and policy enforcement | `SEC-POL-03`, `10` |
| `4.1.3` through `4.1.5` | Address embedded malware/secrets and restrict execution to trusted, verified images | `SEC-POL-10` |
| `4.2.1` Insecure connections to registries | Protect image push/pull traffic between trusted endpoints | `SEC-POL-10` |
| `4.2.2` Stale images in registries | Avoid unsafe stale images and use immutable names that identify discrete image versions | `SEC-POL-10` |
| `4.3.3` Poorly separated inter-container network traffic | Segment container traffic and define expected network flows | `SEC-POL-02` |
| `4.4.1` Vulnerabilities within the runtime software | Monitor and promptly remediate runtime vulnerabilities | `SEC-POL-12` |
| `4.4.2` Unbounded network access from containers | Define app-aware network surfaces and detect or prevent unexpected traffic | `SEC-POL-02`, `07` |
| `4.4.3` Insecure container runtime configurations | Assess and enforce secure runtime settings and constrain accessible paths, processes, sockets, and system calls | `SEC-POL-03`, `05`, `07` |
| `4.5.5` Host file system tampering | Grant minimal filesystem permission, use allocated storage volumes, and avoid sensitive host mounts | `SEC-POL-03`, `05` |
| `6.4` Container Technology-Specific Incident Response Process | Prepare container-aware logging, evidence collection, forensics, and response processes | `SEC-POL-13` |

## Source maintenance and conflict handling

The HIPAA source basis in
[`SEC-HIPAA-AUT-001@1.0.1`](../HIPPA/01-authority-scope-and-source-basis.md)
is a peer regulatory source register for its policy scope. It does not replace
or reinterpret the NIST publications here. `RZN-001` is not an external
security authority and supplies no basis for weakening either source family.

- Review this register when NIST publishes a final revision or release that
  changes a cited outcome, at each security-suite review, and at least when the
  architecture or profile boundary changes.
- External publication changes are evidence for review; they do not silently
  modify an accepted project policy or architecture invariant.
- Record the exact new publication identity, affected policy/control mappings,
  impact analysis, and human decision before changing this suite.
- If final NIST guidance conflicts with the architecture, preserve both source
  identities and use the repository invariant-conflict process. Do not conceal
  the conflict by misquoting NIST, weakening architecture, or claiming a broad
  control is fully implemented.
- Drafts may inform planning only. A draft cannot override this final-source
  register or serve as the sole justification for a binding policy change.

## Revision record

| Date | Revision | Change | Authority |
|---|---|---|---|
| 2026-11-10 | `1.0.0` | Established the NIST source register | User's NIST policy instruction and clarification |
| 2026-11-10 | `1.0.1` | Clarified the independent HIPAA source basis and RZN-001's non-authoritative standing | User's explicit instruction to apply the reconciliation findings in place |
