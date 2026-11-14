# TADp repository instructions for Codex

## Development project and distribution

The installed development home is [TADp/](TADp/README.md), with its own
[profile](TADp/project-profile.md) and
[development workflow](TADp/docs/development/tadp-development-workflow.md).
For new TADp development, resolve project `P=R/TADp/` and candidate workspace
`C=P/protocol/` explicitly from either repository or project context. Do not
develop directly in `R/protocol/`; it is the implementation-ready distribution.
The candidate directory is not another scaffold or governing baseline.

Keep project governance and history at `P`, candidate work at `C`, and the
protected installed library at `P/template/`. Preserve the full serial route:
develop and qualify in `C`, introduce exact authorized proven work into
`P/template/`, complete the development work, promote its sanitized output into
`R/protocol/template/`, then roll out to specifically mapped `R/protocol/`
consumers. Each later boundary requires sufficient exact authority and evidence;
the project setup grants no future protected-source change, promotion or rollout.

An invoked repository-level maintenance instruction must identify the exact
candidate work and target before generic development begins. Do not silently
retarget an older prompt or use its distribution target for experimental work.
Keep `P/prompts/AGENTS.md` unchanged: project-local prompts cannot gain generic
protocol-maintenance or outside-project authority through a cwd change. Existing
governing requirements below remain binding. Ownership follows the current
repository-owner role, including each fork's respective owner; prospective
adoption is recorded separately in the profile. Setup creates no initiative acceptance.

For every TADp task, read and apply the canonical
[prompt keyword specification](protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md),
including ordinary requests, analysis, and all prompt types. Its registry owns
directive interpretation and list scheduling; references and examples remain
inert. This entry point grants no exception, protected-source edit, or wider
target authority.

Before changing any file in this repository, read and apply
`protocol/AGENTS.md`. Before changing architecture, specifications,
initiatives, products, evidence, lifecycle behavior, templates, prompts, or
validation, also read the applicable documents under
`protocol/evidence/authoritative/LLM`, beginning with the suite index.

The authoritative baseline is binding. Do not modify it unless the user
explicitly authorizes the specific invariant change. Non-authoritative
evidence may provide clues only and cannot override an invariant. Preserve
source identity, record invariant conflicts, require explicit human decisions
where the protocol requires them, keep initiatives narrowly scoped, and use
the declared type-specific workflow.

Reusable templates and the Codex invariant suite are protected sources. In
this repository, that protection covers `protocol/template/**`,
`protocol/evidence/authoritative/LLM/**`, and the corresponding paths under
`example/`. Ordinary work may read or copy those sources but must not edit,
fill, rename, move, or delete them. A protected-source change requires an
explicit human instruction naming that change. Never refresh a
`.tadp-lock.json` file or use the protected-update commit override merely to
make an unintended change pass validation.

Git and Codex are required parts of the protocol. Preserve unrelated work,
use traceable branches and commits, and report only claims supported by the
required records and verification.

Include proposed, accepted, and partially performed initiative effort as work
in coherence reviews without promoting its authority. Record incompatible
efforts in each project's work-conflict register and affected records. Apply
specification 10's completion feedback review and require recorded authorized reopening before
refining closed claims. Under adopted specification 09, a human instruction to
process an identified realization delegates placement and necessary reopening.
Coherent same-outcome revision is permitted; independent outcomes and incompatible
boundaries require separate initiatives. Changed claims require renewed human
acceptance.

## Repository prompts

When executing a prompt stored under `prompts/`, also read and apply
`prompts/AGENTS.md`. Its protocol-first execution authority and example-sync
rules apply only to those repository prompts and do not broaden ordinary work
outside that directory.
