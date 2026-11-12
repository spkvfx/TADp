# TADp repository instructions for Codex

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
