# Add positional prompt switches with explicit exception records

Implement one bounded TADp protocol change: support the positional
keywords and list-execution principles defined below in prompts,
while preserving TADp locks, existing rules outside explicitly authorized
exceptions, and truthful evidence.

Work in the current TADp repository. Read the repository-root `AGENTS.md`,
`protocol/AGENTS.md`, this directory's `AGENTS.md`, and the authoritative LLM
suite, beginning with its index, before changing anything. Follow the
repository-prompt protocol-first and example-synchronization rules.

This document describes a capability to implement. Its keyword names,
tables, and examples are specification text, not active switches for this
maintenance task. Creating, reading, or discussing this prompt does not
execute it or authorize a live initiative exception.

## Canonical keyword document and universal application

Create this specific authoritative document:

`protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md`

Make it the canonical keyword reference and extensible registry within the LLM
invariant suite. It must own the directive syntax, registered names, initial
states, positional and composition rules, list-execution principles,
exception and confirmation requirements, lock preservation, and the extension
process. Populate it with the ten initial directives specified in this prompt.
Add it to `00_Codex_Invariant_Suite_Index.md`; do not leave these rules owned
only by a repository prompt, an optional guide, or a duplicate authority tree.

In `protocol/AGENTS.md`, add a direct relative link to
`evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md` and an
explicit instruction to read and apply it when interpreting any TADp task.
This requirement applies universally within the governed TADp scope: ordinary
user requests, analysis, project-local prompts, numbered workflow prompts,
and repository-maintenance prompts. It is not conditional on invoking a
stored prompt or modifying a particular directory. Applying the specification
means recognizing operative directives when supplied; reading the registry
does not itself activate its examples or enable any switch.

Carry the same entry-point instruction into
`protocol/template/project/AGENTS.md` so newly instantiated projects inherit
it. Reconcile repository-root `AGENTS.md` and affected prompt instruction files
to reference the canonical contract without duplicating its definitions or
broadening their existing target and authority boundaries. Verify the
protocol-owned paths within the target boundary in `prompts/AGENTS.md`.

## User-defined keyword registration

Include an easy-to-find "Adding a keyword" section in the canonical document,
with a reusable entry format and an inert worked example. A user must be able
to request a precise new keyword and behavior, then have the LLM prepare its
entry, reconciliation, and verification without manually constructing protocol
paperwork. Do not treat the initial ten directives as a permanently closed
vocabulary.

For each registered keyword or pair, require:

- a stable definition ID, exact bracketed spelling, and inverse spelling;
- purpose, initial state, positive effect, inverse effect, and the exact
  settings changed or retained by each form;
- positional scope, interactions with existing settings, and applicability
  to nested lists, parallel branches, retries, and resumed work;
- required authority, affected rules, permitted exception behavior, and
  explicit limits, including the invariant that TADp locks remain enforced;
- examples of operative use and inert mentions, plus acceptance cases; and
- the human instruction or confirmation, revision and effective event,
  compatibility consequences, and links to implementation or consumer changes
  when the behavior requires them.

Use lowercase names beginning with a letter and continuing with letters,
digits, or hyphens; `!` remains the inverse marker immediately after `tadp:`.
Reject duplicate spellings, conflicting definitions, implicit aliases, and
attempts to redefine an existing name without explicit revision authority.
An unregistered directive presented as an operative instruction remains inert
and is reported as unregistered; the LLM may propose a definition but must
not invent and activate its semantics.

Registration changes an authoritative protected source. Require explicit
human authority identifying the precise addition or revision before adopting
it. The LLM may automatically document that authority and author the entry;
automatic authorship does not supply approval. If the LLM infers a keyword,
its meaning, or an invariant exception beyond the explicit instruction,
obtain the required confirmation before adoption or use.

An approved addition must preserve earlier definitions and history, reconcile
affected consumers and verification, and update only the specifically
authorized locks after coherent verification. Keep the canonical registry as
the source of recognized names and semantics; avoid separate hardcoded
ten-keyword allowlists in agents, prompts, or validators. A registry entry
does not manufacture unavailable tool support or authorize an external action.
Do not add an unprotected override registry that can weaken these invariants.

## Requested behavior

Use bracketed, namespaced directives of the form `[tadp:keyword]` or
`[tadp:!keyword]`. The `!` appears immediately before the keyword. Match the
exact lowercase spelling, colon, and closing bracket, with no internal
whitespace. The ten concrete directives defined in the tables below are the
initial registered vocabulary; additional directives become operative only
through the canonical registration process. The generic forms in this
paragraph are explanatory placeholders, not registered names.
Unbracketed spellings and former slash forms are not active aliases. These are
TADp prompt directives, not filesystem paths or registered ChatGPT commands.

Allow these exact, case-sensitive directives at any position in a prompt,
including between instructions on the same line:

| Keyword | Human-input gates | Other gates |
|---|---|---|
| Initial state | Required | Required |
| `[tadp:robotic]` | Lifted | Unchanged |
| `[tadp:ungated]` | Lifted | Lifted |
| `[tadp:!robotic]` | Required | Unchanged |
| `[tadp:!ungated]` | Required | Required |

The two gate settings are independent. In particular, after `[tadp:ungated]`,
`[tadp:!robotic]` restores only human-input gates; other gates remain lifted until
`[tadp:!ungated]` restores them. Conversely, `[tadp:robotic]` never silently restores
other gates that were already lifted.

`[tadp:robotic]` requests completion of its following block without further human
input. `[tadp:ungated]` requests completion of its following block without gate
stops. Both retain TADp locks. These settings take effect through the explicit
exception process below, not through an assumed override of existing rules.

## Preview, local access, and independent review

Support these additional exact, case-sensitive keywords using the same
positional interpretation. Each pair controls one independent setting:

| Keyword | Effect on following instructions |
|---|---|
| `[tadp:preview]` | Produce proposed changes or diffs without applying edits or causing external effects. |
| `[tadp:!preview]` | End preview-only handling; ordinary permitted execution may resume. |
| `[tadp:local]` | Use only local resources; do not access the network or external services. |
| `[tadp:!local]` | End the added local-only restriction; ordinary permitted resource access may resume. |
| `[tadp:review]` | Require independent review of the block's output before considering its work finished. |
| `[tadp:!review]` | End the added independent-review requirement for following work; retain any ordinarily mandatory reviews. |

Initially, preview-only handling, the additional local-only restriction, and
the additional independent-review requirement are off. That initial state
never grants write permission, network access, external side effects, or
permission to omit an existing required review.

`[tadp:preview]` permits analysis, read-only inspection, and proposed changes shown
in the response. Do not create or modify files, commit changes, persist
exception records, run state-changing checks, or perform external side effects
for previewed instructions. Show proposed exception records as drafts in the
response; do not represent them as adopted receipts or executed exceptions.
Read-only external lookup remains possible only when local-only handling is
off and the lookup is otherwise permitted. `[tadp:!preview]` applies to following
instructions; it does not apply earlier proposed changes retroactively.

`[tadp:local]` constrains resource access and tool actions. Use already available
local files, local tools, and supplied context; do not browse, fetch, push,
publish, or call external services for the affected instructions. Independent
agents may work on supplied or local material under the same restriction;
ordinary model inference is not itself external resource access under this
setting. Report unavailable remote evidence rather than claiming it was
checked. `[tadp:!local]` grants no new authority to send messages, publish, or
perform another external action.

`[tadp:review]` requests a distinct review activity and its result, normally from
an independent agent or reviewer. Review the actual output and its applicable
requirements, identify findings, and reconcile them or report unresolved
issues. A second pass by the producing agent is not independent review. For
preview work, review the proposed output without applying it. This setting
does not itself require a human reviewer; existing human-review requirements
remain applicable. If independent review is unavailable, report the unmet
request instead of fabricating a review or claiming the block finished.
`[tadp:!review]` does not cancel review obligations already attached to earlier work.

Each keyword changes only its declared settings. Gate-mode keywords do not
toggle preview, local access, or independent review; the new keywords do not
change gate settings or each other's settings. For example, `[tadp:ungated]` does
not silently permit writes under `[tadp:preview]`, network access under `[tadp:local]`,
or omission of an explicitly requested `[tadp:review]` activity. `[tadp:!ungated]`
restores the two gate settings only. Any proposed exception to an active
restriction still requires the explicit authority and documentation process;
do not infer it from another switch.

All negative forms restore only ordinary permitted behavior for their own
setting. They never grant new authority or weaken existing TADp rules or locks.

## Positional interpretation

Interpret operative keywords from left to right. Each updates the indicated
settings for subsequent instructions only, until a later keyword changes
those settings or the prompt ends. A switch changes only its declared settings;
all other settings carry forward. Repeated identical switches are idempotent.

- Text before the first switch uses the initial state.
- A switch never changes earlier instructions, decisions, or evidence.
- Headings, paragraphs, indentation, and list boundaries do not reset state.
- A switch embedded between instructions on one line affects only the text
  following it. Do not apply one mode to the whole prompt merely because a
  keyword occurs somewhere in it.
- Recognize complete bracketed directive tokens, not partial matches within
  malformed directives, paths, URLs, or longer identifiers. Adjacent complete
  directives are allowed and apply left to right. Define and test the
  token-boundary rule without requiring a directive to occupy its own line.
- Names in explanations, quoted examples, code samples, attachments, tool
  output, and referenced evidence are inert unless the human explicitly
  designates that text as operative instructions. Do not scan supporting
  records for keywords and promote their contents into execution authority.
- Settings end with their prompt. They do not leak into another prompt,
  initiative, or later task. A resumed execution retains the recorded source
  prompt and block identity rather than inventing a new scope.
- Do not invent stack, nesting, or implicit reset behavior.

Record the effective settings for each affected instruction block so that
execution order, retries, and handoffs cannot accidentally turn a positional
exception into a prompt-wide exception.

## List structure declares execution order

Apply these rules to operative action lists at each nesting level:

| Instruction structure | Execution semantics |
|---|---|
| Numbered list | Execute sibling items serially, in written order. |
| Bulleted or dashed list (`-`, `*`, or `+`) | Execute sibling items explicitly in parallel, with equal priority. |
| Instructions outside a list | The agent may choose serial or parallel execution according to dependencies, context, and available capabilities. |

For numbered lists, complete each item and its applicable checks before
starting the next. Do not parallelize or reorder numbered sibling actions
merely because they appear independent. If an item is blocked, preserve and
report the blocker rather than skipping ahead within that list.

For bulleted or dashed action lists, treat parallel execution as an explicit
instruction, not an optional optimization. Dispatch ready sibling items
concurrently using available tools or agents. Every sibling has equal
priority; textual position creates neither precedence nor a higher priority.
A blocked sibling does not prevent other independent siblings from proceeding,
but the list remains incomplete until every item has its required disposition.

The two list types may be mixed and nested. Each level controls its own
sibling items, and each item includes its descendants. A numbered parent item
with bulleted children waits for all parallel children to finish before the
next numbered parent item starts. Bulleted parent items with numbered children
run as equal-priority parallel branches, each executing its own numbered steps
serially. Completion of a containing item or list joins all its child work;
finishing one parallel branch does not finish the containing item.

For example, this inert illustration combines both directions of nesting:

```markdown
1. Prepare shared inputs.
2. Run both equal-priority branches in parallel:
   - Review contracts:
     1. Read the current contract.
     2. Compare the proposed changes.
   - Review validation:
     1. Read the current checks.
     2. Identify missing coverage.
3. Reconcile both branch results after both finish.
```

Instructions outside lists make no explicit serial or parallel declaration.
The agent may schedule those instructions at its discretion while respecting
actual dependencies and applicable rules. This discretion does not change the
declared scheduling of an embedded action list.

Determine each instruction's effective switch settings from its position in the
source prompt before dispatching parallel work. Runtime interleaving must not
change another branch's settings or turn positional switches into shared,
mutable global execution state.

Numbered or bulleted reference, requirement, option, and verification-case
lists do not become execution steps merely because of their markers. Apply
the scheduling rules to actions the prompt actually instructs the agent to
perform, not to quoted examples or descriptive inventories.

Preserve real dependencies, shared-write constraints, available capacity,
applicable gates, and TADp locks. Report a conflict or capability limit that
prevents the declared parallel execution; do not silently serialize a parallel
list, invent priority, or claim concurrency that did not occur. Gate switches
do not themselves authorize changing declared scheduling. Any exception uses
the explicit authority and documentation process below. No separate switch for
execution order is required.

## Existing rules and explicit exceptions

Do not assume that a keyword bypasses existing rules. A requested mode and
the authority to except a particular rule are distinct. Inventory the
applicable rules and identify each gate that the block would otherwise have
to satisfy. Apply a waiver only when its exact scope and authority support it.
All rules not covered by an authorized exception remain binding.

The LLM may create the exception documentation automatically. Do not require
the human to write an exception record or repeat an already sufficient
authorization merely because documentation is missing. Instead, create the
record before relying on the exception, preserving the actual instruction
that authorizes it.

An explicit human-supplied keyword and its bounded instructions express the
requested gate behavior. Record them as the source of that request, and
determine whether they supply the specific exception authority required by
the governing rule. Do not treat the keyword alone as unrestricted permission
to contradict invariants, edit protected sources, expand scope, or claim a
gate passed. When required authority is absent or ambiguous, preserve the
existing rule and obtain the exact missing confirmation before affected work.

Each exception record must explicitly preserve:

- a stable ID, authoring agent, and capture date or event;
- the exact existing rule, source path or stable ID, and governing revision;
- the affected gate and whether it requires human input or another check;
- the original requirement and the precise authorized replacement or waiver;
- the source prompt, operative keyword, exact affected instruction block,
  target initiative or records, and duration or end condition;
- the exact human instruction or confirmation, its authority and receipt
  link where required, without inventing a human response;
- the reason, rationale, known consequences, risks, and evidence limitations;
- any autonomous decision method and the resulting agent-made dispositions;
- remaining obligations, especially locks, and any necessary reconciliation
  of decisions, lifecycle, status, verification, and dependent records; and
- the disposition, restoration or re-entry conditions, and Git evidence when
  available.

Use existing decision-receipt and conflict-record conventions where they
apply. A record may cover multiple gates only when it names each gate and the
human authority clearly covers that complete bounded set. Never write only
"robotic enabled" or "ungated enabled" as a substitute for identifying the
actual exceptions.

Automatic documentation records authority; it does not create authority.
Once sufficient authority and its records exist, do not introduce repeated
human-input stops inside the authorized robotic block. Resolve covered
questions by the recorded autonomous method, label the decisions as
agent-made under that authority, and reconcile their consumers.

## Confirmation of inferred keywords and invariant exceptions

An LLM may interpret a request as suggesting these explicit keywords. Before
inserting them as operative instructions or implementing their inferred
effects, it must present the proposed keywords, placement, affected blocks,
setting changes, and exceptions, and receive explicit human confirmation.

The same rule applies to any other LLM-proposed invariant exception, whether
or not a keyword is involved. A general request to continue, finish, work
autonomously, or avoid questions is not silently converted into permission
for an invariant exception.

The LLM may automatically draft and record the proposal. Drafting is not
approval. After confirmation, it may automatically capture the exact response,
complete the exception record, and perform only the confirmed scope.

No switch can waive the confirmation needed to authorize its own
inferred use or a further unapproved invariant exception. Existing sufficient
explicit authority remains usable within its recorded scope; do not ask for
the same decision again solely to produce paperwork.

## Locks and evidence remain explicit

TADp locks and their protection rules remain enforced in every gate setting,
including `[tadp:ungated]`. A keyword is never authority to edit a protected source,
refresh or remove a `.tadp-lock.json`, disable a guard, use a protected-update
override, or conceal pre-existing protected-source drift.

Separately authorized protected-source maintenance follows the existing
specific-authority, coherent-change, verification, and lock-reconciliation
process. Preserve the lock mechanism and check its integrity; do not use a
mode switch to make an unintended protected edit pass.

Lifted gates must be recorded as excepted, waived, skipped, or not performed,
as appropriate, never as passed. Preserve actual failures and missing evidence.
Do not fabricate a human approval, review, test result, ownership decision,
readiness result, acceptance, release, or completion evidence.

Reconcile the gate-exception model with acceptance, reopening, execution,
completion, and their decision receipts explicitly. Identify which rules are
excepted before using an autonomous decision or bypassed prerequisite in a
lifecycle event. Distinguish finishing the requested prompt work under an
exception from satisfying ordinary TADp acceptance or qualification. Do not
silently give existing lifecycle labels a weaker, unrecorded meaning.

Restoring gates does not retroactively validate earlier skipped checks or
erase decisions made under a recorded exception. Recheck current prerequisites
when a later gated instruction depends on earlier excepted work.

These keywords do not override tool permissions, higher-priority instructions,
unavailable capabilities, or factual limits. Report an actual blocker and
complete independent authorized work rather than promising unconditional
execution or inventing evidence.

## Exact implementation authority and affected surfaces

Execution of this repository prompt authorizes adding the positional-switch
mechanism, including preview, local access, and independent review, together
with the explicit-exception mechanism and list-execution principles
described here. It does not itself waive a gate for any existing project or
initiative, answer an open question, accept work, reopen a closed claim, or
authorize unrelated invariant revisions.

For this exact mechanism, explicitly reconcile the affected gate and exception
clauses in the authoritative suite index and specifications 01, 02, 04, 07,
08, and 10 under `protocol/evidence/authoritative/LLM/`. Explicitly create
`protocol/evidence/authoritative/LLM/11_Codex_Prompt_Keyword_Specification.md`
as the canonical document required above. This execution authority includes
that exact protected-source addition, its registry and extension contract,
the suite-index entry, and the universal references in `protocol/AGENTS.md`
and `protocol/template/project/AGENTS.md`. Preserve every unrelated invariant,
existing source identity, prior revision, and historical human decision.

This execution authority covers the exact protected-source additions and
revisions needed for that contract, including the corresponding affected
consumers under `protocol/template/`: the shared prompt workflow contract,
numbered prompts, project instruction sources, and decision-receipt sources.
It covers affected working instructions, project-local prompt guidance,
developer and adoption documentation, validator behavior, regression tests,
and repository instruction summaries. Inventory the exact paths before
editing and keep changes limited to this one capability.

Document the authority, reason, affected scope, effective event, compatibility
and migration effects, and successor relationship. Adding vocabulary must
not retroactively waive an existing gate or reinterpret a historical prompt.
Existing projects and initiatives retain their recorded governing revision
until the applicable adoption and exception authority are recorded.

Reconcile only locks affected by these specifically authorized protected-source
changes, after those changes are coherent and verified. The authority is this
explicit maintenance instruction, not the keywords. Do not absorb unrelated
working-tree changes into that authority or refresh locks for unrelated drift.

Complete and verify the protocol pass within the target boundary in
`prompts/AGENTS.md`. Example-specific products, questions, acceptance,
lifecycle, and completion records remain outside this work. Historical example
recommendations remain contextual proposals; this maintenance instruction does
not resolve their questions or authorize changes to their initiatives.

## Verification and acceptance

Add meaningful regression coverage for the interpretation and exception
contract, using a shared implementation where machine interpretation is
needed. Do not leave contradictory instructions in prompts, authoritative
specifications, templates, or validation. Verify at least:

1. With no keyword, all gates are required and existing behavior is retained.
2. A mid-prompt or same-line switch changes only following instructions.
3. `[tadp:robotic]` lifts only human-input gates; an unexcepted automated failure
   still blocks the affected work.
4. `[tadp:ungated] A [tadp:!robotic] B` requests both classes lifted for A and only other
   gates lifted for B. Human-input gates are required for B.
5. `[tadp:ungated] A [tadp:robotic] B` leaves other gates lifted for B.
6. `[tadp:ungated] A [tadp:!ungated] B` restores all gates for B; prior skipped checks do
   not become passed checks.
7. Repetition, alternating switches, paragraph boundaries, inert examples,
   token boundaries, and separate prompts follow the positional contract.
8. An operative switch without sufficient exception authority or its explicit
   record does not silently bypass an existing rule. The LLM can automatically
   create a record from sufficient authority before proceeding.
9. Confirmed autonomous decisions retain their actual author, method, source
   authority, affected IDs, and reconciliation; no repeated human confirmation
   is required inside that exact approved scope.
10. An inferred switch or other inferred invariant exception remains inactive
    until explicit human confirmation is captured. Neither mode can authorize
    a new exception merely by suppressing its confirmation gate.
11. Protected-source edits and lock drift remain blocked in every mode without
    separate specific maintenance authority. Legitimate lock reconciliation
    remains traceable to that separate authority.
12. Waived or failed checks remain distinguishable from passing evidence in
    receipts, lifecycle records, completion records, and reports.
13. Default projects, historical records, and the linked documentation open
    questions are unchanged by feature adoption alone.
14. Numbered sibling actions execute serially in written order. A blocked item
    prevents starting later items in the same list unless an explicitly
    authorized and documented exception permits it.
15. Bulleted or dashed sibling actions execute explicitly in parallel with
    equal priority. Textual position creates no precedence, and a blocked item
    does not stop independent siblings. Material concurrency constraints are
    reported rather than silently changing the declaration.
16. Mixed and nested lists retain each level's scheduling rule. Numbered
    parents wait for every parallel child; parallel branches execute their
    numbered children serially. Gate settings come from source position, not
    runtime interleaving. Gate switches alone do not alter list scheduling.
17. Instructions outside lists permit agent discretion between serial and
    parallel execution without changing the semantics of embedded action
    lists. Descriptive lists and quoted examples remain inert.
18. `[tadp:preview]` produces proposals without file changes or external side effects;
    checks remain read-only and exception records remain response-only drafts.
    `[tadp:!preview]` affects following instructions without applying earlier drafts.
19. `[tadp:local]` prevents network and external-service access while allowing work
    on supplied and local material. `[tadp:!local]` removes only that added
    restriction without granting permission for an external action.
20. `[tadp:review]` obtains an independent review of actual or previewed output and
    records findings and their disposition. An unavailable reviewer remains an
    unmet request. `[tadp:!review]` removes only the added requirement for following
    work, retaining earlier obligations and ordinarily mandatory reviews.
21. Settings compose independently. `[tadp:preview] [tadp:robotic] [tadp:review]` retains
    preview-only output and independent review while using only authorized
    human-gate exceptions. `[tadp:local] [tadp:ungated]` still forbids external access.
    `[tadp:!ungated]` does not reset any of the three added settings.
22. All initially registered directives and authorized extensions follow the
    same source-position, inert-example, scope, confirmation, and lock-
    preservation rules. Negative forms create no new permissions, and the
    default state leaves existing rules unchanged.
23. Only exact bracketed directives activate a setting. Adjacent directives
    apply left to right. Wrong case, internal whitespace, missing brackets,
    unknown keywords, generic placeholders, and former slash spellings do not
    activate settings; quoted examples remain inert unless explicitly invoked.
24. The named specification exists in the authoritative LLM suite, is listed
    in its index, and is directly referenced by `protocol/AGENTS.md` and the
    reusable project entry point. Ordinary TADp requests apply the contract
    without invoking a stored prompt; installed example references resolve to
    the corresponding mirrored specification.
25. The canonical registry includes all ten initial directives, a reusable
    addition format, and an inert extension example. A specifically authorized
    new keyword can be registered without editing a competing name allowlist.
    Duplicate, conflicting, unregistered, or unconfirmed inferred definitions
    cannot silently become active. Registration preserves locks, authority,
    prior definitions, and the established default behavior.

Inspect Git first and preserve unrelated staged, unstaged, and untracked work.
Use traceable Git records without committing unrelated changes or rewriting
history. Run the applicable protection checks, validator, and focused tests;
report pre-existing failures separately from failures introduced by this work.
Verify corresponding example paths and parity after synchronization.

Report the canonical keyword document and extension procedure, universal
entry-point references, implemented switch semantics, exception-record
contract, exact protocol paths changed, example mirrors, intentionally
unmirrored support files, lock authority, verification results, and remaining
blockers. Claim only outcomes supported by the records and observed
verification.
