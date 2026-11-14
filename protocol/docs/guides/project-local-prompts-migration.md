# Project-local prompts migration

## Purpose and standing

This guide adds the canonical project-local prompt boundary to an existing
TADp scaffold. It is procedural guidance, not evidence that an initiative was
accepted, a workflow gate passed, or project or protocol work was authorized.

The reusable sources are
`template/project/prompts/AGENTS.md` and
`template/project/prompts/README.md`. They are protected by the template
integrity lock. Their installed copies at root `prompts/AGENTS.md` and
`prompts/README.md` are working project files governed by normal Git history.

## Preconditions

1. Use a dedicated, traceable branch and inspect staged, unstaged, and
   untracked work.
2. Run the protected-source check and preserve any unexplained drift.
3. Identify one intended scaffold root from existing project records and Git
   evidence. Confirm that its required markers resolve inside that root and
   that no parent, sibling, nested scaffold, worktree, submodule, or indirection
   creates an ambiguous boundary.
4. Inventory an existing root `prompts/` directory, including every scoped
   instruction and local prompt. Do not overwrite or weaken established
   instructions blindly.
5. Confirm that this is project adoption work. A project-local prompt cannot be
   used to perform the migration because adding or revising its own generic
   boundary is protocol adoption or maintenance work.

## Migration

1. Copy `template/project/prompts/AGENTS.md` to root
   `prompts/AGENTS.md` and `template/project/prompts/README.md` to root
   `prompts/README.md`.
2. If either destination already exists, reconcile it deliberately. Preserve
   the complete canonical boundary text and every compatible stricter local
   instruction. Move a genuinely narrower rule to an appropriate descendant
   `AGENTS.md` when that preserves its original scope more accurately.
3. Keep additional project-local prompt files in root `prompts/`. They remain
   non-authoritative working material and inherit the root prompt instructions.
4. Do not copy the numbered workflow from `template/prompts/`. That protected
   library and its shared contract keep their distinct initiative-workflow
   role.
5. Review every local reference that names a prompt path. A reference to root
   `prompts/` means project-local work; a reference to
   `template/prompts/` means the protected numbered workflow.
6. Commit the migration as a reviewable project-scaffold change. Do not refresh
   the template lock: copying protected sources to their working destinations
   does not change the protected baseline.

## Verification

From the scaffold root, run the protected-source check, the TADp validator, and
the regression suite. Confirm that:

- root `prompts/AGENTS.md` and `prompts/README.md` exist as direct scaffold
  children and preserve the canonical reusable content;
- the two reusable source files remain recorded by
  `template/.tadp-lock.json`;
- existing local prompt files remain present and outside the protected template
  file set;
- no resolved prompt or side-effect path crosses the scaffold boundary; and
- the enclosing Git root has not been treated as wider project-work authority.
  Project root `P` is the installation directory and may be beneath Git root
  `G` under [specification 05](../../evidence/authoritative/LLM/05_Codex_Git_Workflow_Specification.md#requirement);
  necessary Git metadata operations retain project-scoped file boundaries.

A passing validator proves only the checked structure and content relationship.
It does not establish prompt authority, initiative standing, lifecycle state,
completion, release, or permission to touch another scaffold.
