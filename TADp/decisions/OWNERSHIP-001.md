# OWNERSHIP-001 decision receipt

**Receipt ID:** OWNERSHIP-001  
**Initiative:** Not applicable; project ownership appointment  
**Source ID or lifecycle event:** Human authority model for the TADp development project  
**Human authority:** Requesting human defining the repository's role-based ownership policy  
**Response date or event:** Current Codex session, 2026-11-14  
**Capture date or event:** 2026-11-14, immediately after the explicit response  
**Recorded by:** Codex, primary agent  
**Capture context:** Reply to the ownership/adoption question during setup  
**Disposition:** Repository-owner role appointed; adoption not decided by this response  
**Git commit:** See the scoped setup commits containing this receipt in Git history  
**Scope:** Not applicable; no version scope allocated  
**Revision cycle:** Not applicable; project authority decision  
**Claim revision:** Installation from `6120bd10bb2e368274fd5bd4ff5481d33f61c4c6`

## Exact prompt or question

To finish the project’s human authority records, should Shawn Kearney be the project owner, technical owner, and approval authority, and should the project prospectively adopt verified source revision 6120bd10bb2e368274fd5bd4ff5481d33f61c4c6? The prompt requires those explicit decisions before full conformance can be claimed.

## Evidence and limitations presented

- **Authoritative evidence:** Installed suite specifications 02, 05, 07, and 08 retain human authority, ownership, adoption, acceptance and evidence requirements.
- **Other evidence:** Git identity Shawn Kearney was explicitly described as insufficient to establish ownership.
- **Material limitations:** No hosting ownership lookup was performed. A role appointment is not evidence of a particular person's current repository control. This reply did not explicitly decide adoption.
- **Affected scope described to the human:** Project owner, technical owner and approval authority for this new project, distinct from initiative acceptance.

## Exact human response

```text
ownership should be the current repository owner. This repository may be forked and updated by the respective owner, not limited to me personally.
```

## Resulting scope and rationale

Ownership is attached to the current repository-owner role, not a named person
or Git author. In each fork, the respective repository owner holds that role.
Project ownership, accountable technical stewardship, approval and register
stewardship resolve to that role unless its current holder explicitly delegates
a narrower responsibility in a durable record. This convention does not confer
ownership of upstream repositories, other forks, components or external services.

For a future human decision, record the actual responder, their repository-owner
or delegated authority, exact words and scope in the owning receipt. Forking does
not retroactively transfer the authorship or authority of earlier decisions,
accept an initiative, adopt a revision, or permit an upstream write. Installed
source and historical records retain their identities.

## Reconciled records

| Record | Change required by this decision | Verification |
|---|---|---|
| [Profile](../project-profile.md) | Use repository-owner role for human authority and stewardship | Semantic review |
| [Project instructions](../AGENTS.md), [README](../README.md), [workflow](../docs/development/tadp-development-workflow.md) | Discover role-based policy without naming a personal owner | Links and scoped diff |
| [Coordination](../initiatives/initiative-index.md), [work conflicts](../initiatives/work-conflicts.md), [status](../initiatives/status.md), [evidence register](../evidence/evidence-register.md) | Assign canonical record stewardship to current repository owner | Structural review |
| [Setup receipt](SETUP-001.md) | Preserve initial missing decision; append resolution link | History preserved |

## Unresolved consequences and re-entry conditions

Prospective adoption remains a separate explicit decision. No personal identity,
hosting permission, initiative acceptance, protected edit or lifecycle event is
inferred from this ownership policy. Before acting on a decision, identify the
actual current authority; explicit delegation must preserve its scope and source.
