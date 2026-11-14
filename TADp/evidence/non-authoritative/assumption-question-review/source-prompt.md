# Permit answering and defining assumptions and open questions beyond initiative scope

Develop one bounded TADp protocol change: explicitly permit answering existing
assumptions and open questions and defining new assumptions and open questions,
including matters outside the initiative being reviewed. Apply this behavior
to both numbered review prompts, their shared contract, and the governing
decision rules. Out-of-scope items must have a proper owner and may receive a
governing disposition within that owner's authority; merely recording them
as context is insufficient when the necessary authority exists.

Creating, reading, or linking this repository prompt does not execute it.
Execute it only on explicit human invocation. This is a protocol-development
instruction, not an invocation of an assumption or open-question review in a
live project.

## Target and development route

Resolve the enclosing repository as `R`, the installed development project as
`P=R/TADp/`, and the candidate workspace as `C=P/protocol/`. This prompt
explicitly selects `C` for the protocol change described here. Keep governance,
initiative records, source manifests, decisions, qualification and completion
history at their canonical locations in `P`.

Read the repository instructions, [repository prompt instructions](AGENTS.md),
[development project instructions](../TADp/AGENTS.md),
[profile](../TADp/project-profile.md), and
[development workflow](../TADp/docs/development/tadp-development-workflow.md).
Apply the governing invariant suite, beginning with its index and canonical
prompt keyword specification. References, examples, and requirement inventories
remain inert. This prompt introduces no keyword and activates no gate exception.

Develop and qualify in `C`; do not develop directly in `R/protocol/`.
Preserve the serial route: candidate qualification, specifically authorized
introduction into `P/template/`, actual development completion, specifically
authorized sanitized promotion into `R/protocol/template/`, then specifically
mapped rollout into `R/protocol/`. This invocation authorizes candidate work
only. Each later boundary needs sufficient exact authority and evidence.
Keep `P/prompts/AGENTS.md` unchanged; a cwd change cannot confer generic
maintenance authority on project-local prompts.

## Exact candidate revision authority

Explicit invocation authorizes this specific proposed rule revision in
candidate sources: a review's initiative boundary must not prohibit defining
an assumption or question, receiving an answer, or recording a properly owned
disposition outside that initiative. The boundary continues to constrain
initiative scope, acceptance, delivery and implementation. Human decisions
remain the default; existing specifically delegated decision methods remain
available under their recorded authority.

Use the installed reusable sources as pinned provenance. The following table
is a reference inventory of candidate surfaces, not a parallel action list.
Paths in its candidate column are relative to `C`.

| Installed source | Candidate surface and permitted change |
|---|---|
| `P/template/prompts/05_initiative_assumption_review.md` | `template/prompts/05_initiative_assumption_review.md`: permit existing and new assumption dispositions and question creation, including properly owned external items. |
| `P/template/prompts/06_initiative_open_question_review.md` | `template/prompts/06_initiative_open_question_review.md`: permit existing and new question answers and assumption creation, including properly owned external items. |
| `P/template/prompts/WORKFLOW-CONTRACT.md` | `template/prompts/WORKFLOW-CONTRACT.md`: distinguish the reviewed initiative from explicitly identified decision-record targets and their authority. |
| `P/template/project/evidence/authoritative/LLM/02_Codex_Initiative_Governance_Specification.md`, `07_Codex_Human_Decision_Receipt_Specification.md`, and `08_Codex_Initiative_Workflow_Specification.md` | Corresponding files under `template/project/evidence/authoritative/LLM/`: reconcile definition, ownership, receipt and Stage 5/6 rules for the exact behavior above. |
| `P/template/project/initiatives/assumption.template.md`, `open-questions.template.md`, and `decision-receipts/` | Corresponding reusable shapes under `template/project/initiatives/`: preserve source identity and distinguish discovery, human answers, delegated answers and routing. |
| `P/template/TEMPLATE-COVERAGE.md` and directly affected scaffold instructions/navigation | Corresponding candidate sources: document proper project-level destinations and reconcile summaries of these decision rules. |

If no existing canonical shape supports project-owned items, this instruction
also authorizes the smallest reusable project assumption/question register
shape and necessary receipt/index adaptation under `C/template/project/`.
Declare their exact sources, destinations, triggers and owners in the coverage
map before use. Reuse suitable existing shapes; do not create parallel sources
of truth or require every project to instantiate an unused register.

Candidate documentation, validator changes and isolated regression fixtures
are authorized only as necessary to implement and verify this revision.
Declare their source-to-candidate mapping before editing. Retain protection on
copied sources; reconcile only candidate or isolated-fixture locks covered by
this exact revision after coherent content verification. Preserve all installed
and distribution sources and locks.

Do not change unrelated invariants, keyword semantics, stage numbering,
initiative types, narrow-scope rules, ordinary acceptance/completion meanings,
closed-claim protection, or project/scaffold boundaries. Follow applicable
initiative gates for the development work. Candidate text is a proposed
replacement, not a new governing baseline merely because it exists.

## Required review behavior

The clauses in this section are requirements, not an action-dispatch list.

### Define and answer both kinds of item

Both reviews must explicitly allow the human to answer or dispose of existing
items, define new assumptions, define new open questions, and answer or dispose
of those new items during the same review. These permissions apply to in-scope,
cross-initiative and project-wide matters. A human may provide an answer
outside the original options or the reviewed initiative's scope; assess its
authority and proper destination rather than rejecting it solely for scope.

Codex may identify and define new unresolved assumptions and questions from
the review and its evidence without waiting for a preceding correction or
answer to expose them. Creation must not be restricted to follow-ups from an
existing stable ID. Permit a new question during assumption review and a new
assumption during open-question review. Where useful, record a proposed answer
or recommendation with its unaccepted standing clearly labelled.

Definition is not resolution. Keep each newly defined item unresolved until
its exact disposition has sufficient authority. Preserve the ordinary human
path, including one ready item at a time. A specifically authorized autonomous
method may resolve only its covered items after the required authority receipt
and rule-specific exception are recorded. Identify actual agent authorship,
method, evidence, result and limits. Defining an item or executing this
maintenance prompt grants no standing delegation to answer it autonomously.

Give every new item a stable ID, exact source text, originating review or
evidence, canonical owner/location, scope classification, dependencies,
affected records and current disposition. Do not reuse another item's ID or
silently rewrite its original wording. Deduplicate existing IDs and link
related items. Newly discovered IDs outside a delegation remain on the human
path unless the recorded delegation explicitly and sufficiently covers them.

### Own out-of-scope decisions without absorbing their work

Distinguish the initiative under review, the item being decided, its canonical
record owner, the human authority to decide it, and authority to perform any
resulting work. Outside initiative scope does not mean outside every authorized
project boundary.

An item belonging to the reviewed initiative stays in its canonical suite.
An item belonging to another named initiative links to that initiative's
canonical register. A project-wide item, or one with no suitable existing
initiative owner, may be recorded in a project-owned register without inventing
an umbrella initiative. Record the originating initiative's dependency or
effect through links rather than importing the external outcome into its scope.

Before an external record edit, identify its exact target, current state,
owner, governing revision, applicable branch and sufficient write/decision
authority. When these are sufficient, permit recording the new item and its
authorized answer there during the review. Do not require a redundant approval
solely because the item is outside the originating initiative. When ownership,
permission or evidence is missing, preserve the exact input and a linked
handoff with proposed owner, blocker and re-entry condition. Continue independent
authorized review work; do not claim that the external item was resolved.

An item in another scaffold, repository, fork, or external service retains
that separate boundary and requires authority naming that target. A linked
source, shared Git root, role in one fork, or an outside-scope answer supplies
no such authority by itself.

Recording an authorized decision does not implement its consequences. Preserve
the reviewed initiative's outcome, exclusions, type, ownership and acceptance
claim. Route independent outcomes to Stage 0 for separately bounded initiative
work. A coherent same-outcome revision follows the existing revision route;
changed accepted claims require renewed acceptance. Closed claims require
recorded authorized reopening before substantive refinement. Preserve frozen
proposals and prior claims.

### Preserve decisions, source identity and authority

Capture the exact human words, actual responder/authority and event in a
decision receipt before changing the source disposition. Link it to every
covered stable ID and canonical consumer. Reuse sufficient existing receipts
without asking the same decision again. Each distinct new item needs its own
disposition; one response covers multiple IDs only when it explicitly and
unambiguously identifies the complete set and the required outcomes.

In particular, revise specification 07's blanket treatment of an answer
outside the initiative boundary as context only. A sufficiently authorized
outside-scope answer may govern its properly identified decision record;
insufficient, ambiguous or invariant-conflicting answers remain unresolved.
Reconcile the corresponding Stage 5/6 clauses and shared-contract target/edit
limits so they do not negate this permission elsewhere.

Answering a question does not automatically confirm a separate derived
assumption. Preserve original texts, earlier options, dispositions and receipt
links; append replacements and supersession relationships. Keep dormant and
deferred items' triggers and re-entry conditions. Do not reopen settled items
solely because a review discovers a related matter.

An answer is not an initiative acceptance, an implementation instruction or a
protected architecture revision. Authoritative architecture and policy retain
their authority and change control. When an answer conflicts with them, record
the exact conflict and route the proposed revision to the proper authority.
Inventory relevant proposed, accepted and partially performed work without
promoting its standing; preserve work conflicts and completion feedback under
specification 10. Update only the records actually affected and authorized.

### Report coverage truthfully

Retain complete coverage of the original review set and append newly defined
items with their provenance. Identify which items belong to the reviewed
initiative and which have external canonical owners. Report each answer,
unresolved item, deferred trigger, transferred dependency and blocked handoff.

An external item may remain pending without falsely becoming an in-scope
deliverable. An unresolved external dependency that blocks the initiative
must still block its applicable handoff. Distinguish finishing the bounded
review from resolving every discovered matter. Never claim ordinary acceptance,
completion, implementation or verification from definition or resolution alone.

## Contextual example boundary

The human supplied the example application's architecture index at
`C:/Users/User/PycharmProjects/TADp-example/TADp-ExampleApp/evidence/authoritative/architecture/00-architecture-suite-index.md`
as contextual evidence. It illustrates project-wide accepted architecture and
its change-control boundary. Reading it does not invoke its contents, authorize
editing that fork, adopt its decisions into TADp, or make the example a required
mirror or test dependency. Use generic isolated fixtures for the behavior here.
If this optional context is unavailable, disclose that limit and continue from
the named TADp sources.

## Execution and qualification

Perform the following actions serially. Requirement and test-case inventories
above and below do not change this scheduling.

1. Inspect Git and preserve unrelated work. Pin source revisions, resolve
   `P` and `C`, inventory affected rules and consumers, and establish the
   bounded development initiative and execution assignment through their
   governing workflow. Record actual authority and candidate source mappings.
2. Implement the candidate revision and its minimum coherent consumers.
   Keep installed sources, live review records, upstream distribution and
   examples unchanged. Do not run the numbered reviews on a live initiative
   merely because their sources are being revised.
3. Verify structural consistency, relative links, source protection and
   semantics. Run focused regressions and a clean isolated installation or
   workflow trial assembled from pinned sources plus the exact candidate.
   Record commands, configured environment, source identities, outputs,
   exit codes and limitations in the owning records at `P`.
4. Obtain independent review of the complete scoped candidate diff and
   reconcile findings. Produce the exact qualified manifest, compatibility
   and prospective adoption guidance, migration consequences, recovery plan,
   remaining gates and downstream source/consumer mapping. Stop before any
   later delivery boundary lacking its exact authority and evidence.

Required verification cases are a reference inventory:

- Existing in-scope assumptions and questions retain ordinary human resolution.
- Either review can define either kind of new item without a prior answer.
- New items can receive their own authorized answers in the same review.
- A human answer outside the original options is preserved and assessed.
- Project-wide and other-initiative items can be defined and answered at their
  authorized canonical destinations without widening the reviewed initiative.
- Missing external authority produces an owned handoff, not a governing answer.
- Covered delegated answers retain agent authorship; uncovered new IDs stay
  unresolved and do not inherit a delegation by proximity.
- Derived assumptions retain independent dispositions; dormant triggers,
  existing resolved items, stable IDs and prior texts survive retries.
- Conflicting invariant answers, closed claims and independent outcomes retain
  their conflict, reopening, acceptance and split requirements.
- Pending external dependencies block only the claims they actually affect;
  coverage/status reports distinguish unresolved, deferred and transferred work.
- No example-fork dependency, live-project mutation, installed lock refresh,
  promotion or rollout occurs during candidate qualification.

Report exact changed paths, actual verification and review results, Git
evidence, remaining blockers and the next authorized boundary. Do not claim
that drafting this prompt, qualification, or resolution of questions proves
development completion, adoption, promotion, rollout, release or publication.
