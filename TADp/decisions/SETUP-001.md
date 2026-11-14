# SETUP-001 decision receipt

**Receipt ID:** SETUP-001  
**Initiative:** Not applicable; project bootstrap, no initiative allocated  
**Source ID or lifecycle event:** Project installation requested in this session  
**Human authority:** Requesting human, explicitly invoking the repository setup prompt; personal identity and continuing ownership not established  
**Response date or event:** User invocation in the current session, 2026-11-14  
**Capture date or event:** 2026-11-14, during setup, after instruction inspection and before project-specific configuration  
**Recorded by:** Codex, primary agent  
**Capture context:** Codex session in the enclosing TADp repository  
**Disposition:** Authorized project setup only  
**Git commit:** See the scoped setup commits containing this receipt in Git history  
**Scope:** Not applicable; no version scope allocated  
**Revision cycle:** Not applicable; bootstrap is not initiative delivery  
**Claim revision:** Setup prompt at `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`

## Exact prompt or question

The human identified [create-tadp-development-project.md](../../prompts/create-tadp-development-project.md)
twice in one invocation. Its operative text is the version at the immutable
commit above. The duplicate attachment identifies one execution, not two projects.
No separate ownership or adoption question has been answered.

## Evidence and limitations presented

- **Authoritative evidence:** Installed [suite index](../evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md), particularly adoption and protection; specifications 02, 05, 07, 08, 09, 10, and 11 retain their ordinary gates.
- **Other evidence:** The explicitly invoked repository prompt defines the setup boundary. Git identity is Shawn Kearney; this is commit authorship evidence only.
- **Material limitations:** The invocation appoints no named project/technical owner and records no explicit prospective adoption decision. Baseline structural validation reports TADP041; see the verification report.
- **Affected scope described to the human:** Establish `R/TADp/`, document its workflow, and change only necessary root `README.md` and `AGENTS.md` guidance. Preserve `R/protocol/` and examples.

## Exact human response

```text
execute this prompt[@create-tadp-development-project.md](file:///C:/Users/User/PycharmProjects/TADp/prompts/create-tadp-development-project.md)[@create-tadp-development-project.md](file:///C:/Users/User/PycharmProjects/TADp/prompts/create-tadp-development-project.md)
```

## Resulting scope and rationale

Install one project named TADp from the verified committed source at
`6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`. Copy the unchanged protected library
and suite; create truthful initial records and local instructions. The prompt's
specific bootstrap permission covers these copies. No source lock is refreshed.
No invariant revision, initiative acceptance, feature implementation, introduction
of new reusable work, upstream promotion, rollout, migration, release, merge,
push, publication, or hook activation is authorized by this event.

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| [Profile](../project-profile.md) | Record project/Git roots, installed revision, pending decisions and scope | Setup report and Git inspection |
| [Coordination](../initiatives/initiative-index.md) | Empty registries, no invented membership or lifecycle | Structural and semantic review |
| [Project instructions](../AGENTS.md), [workflow](../docs/development/tadp-development-workflow.md) | Candidate scope, protection, serial delivery route, context rules | Context checks and independent review |
| [Root instructions](../../AGENTS.md), [root README](../../README.md) | Discover development home and preserve upstream | Scoped diff and upstream hashes |
| [Setup verification](../evidence/non-authoritative/setup/verification.md) | Actual commands, results, limitations, manifest and recovery | Read-only checks and review |

## Unresolved consequences and re-entry conditions

The requesting human must appoint the project owner, technical owner, and
approval authority, and explicitly authorize adoption of an identified verified
revision. Capture that actual decision before activating adoption fields or
allocating governed work; capture the real pre-adoption Git baseline at that time.
Installation is complete only to the extent supported by verification and is
not full project conformance while those decisions remain pending. Future work
retains its exact authority and workflow gates.

## Execution settings and scheduling ledger

Source: the setup prompt at the immutable revision above. No operative keyword
switch occurs. Every setup step uses `human_gates=true`, `other_gates=true`,
`preview=false`, `local=false`, `review=false`; the prompt independently requires
review. No exception was requested, inferred, or used. Reference diagrams,
requirement tables, future delivery steps, and examples are inert setup actions.

| Block | Scheduling and target | Disposition / retry identity |
|---|---|---|
| Setup procedure 1: inspect | Serial parent; Git, source and upstream read-only preflight | Clean base captured; validation failure retained; baseline regressions run as independent verification |
| Setup procedure 2: install | After preflight; `P=TADp/`, canonical project records and `C=P/protocol/` | One installation; initial branch creation denied by filesystem sandbox, then succeeded with metadata permission; no unrelated work changed |
| Setup procedure 3: document | After installation; P instructions/profile/guide and R entry points | Local project documentation only |
| Setup procedure 4: verify | After documentation; explicit P/R contexts, source and upstream checks | Actual results in linked verification report; unavailable evidence remains explicit |
| Setup procedure 5: review/commit | After verification; setup diff only | Independent review reconciled in report; scoped local commits only |

Independent read-only requirements discovery ran alongside primary inspection.
Future numbered delivery steps are documented contracts, not operations executed
by this invocation. A rerun resumes this same setup identity, verifies existing
records and content, and makes no duplicate installation, receipt or empty commit.

## Subsequent authority events

The later [OWNERSHIP-001](OWNERSHIP-001.md) decision appoints the current
repository-owner role, including each fork's respective owner. It resolves the
initial missing ownership policy without rewriting this setup invocation or
attributing a personal appointment to it. Adoption remains a separate decision.

The subsequent [ADOPTION-001](ADOPTION-001.md) records the human's separate
prospective adoption decision and captured immutable pre-adoption baseline.
The initial limitations above remain the truthful history of setup authority.
