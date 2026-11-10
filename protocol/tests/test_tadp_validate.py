from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

from tadp_validate import validate  # noqa: E402


class ValidatorTests(unittest.TestCase):
    def make_repository(self, root: Path) -> None:
        git_directory = root / ".git"
        git_directory.mkdir()
        (git_directory / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        (git_directory / "config").write_text("[core]\n\trepositoryformatversion = 0\n", encoding="utf-8")
        files = {
            "README.md": "# Project\n",
            "AGENTS.md": "# Instructions\n",
            "docs/README.md": "# Documentation\n",
            "docs/development/getting-started.md": "# Getting started\n",
            "docs/development/architecture-and-authority.md": "# Architecture\n",
            "docs/development/repository-layout.md": "# Layout\n",
            "docs/development/initiative-workflow.md": "# Workflow\n",
            "docs/development/git-and-codex-requirements.md": "# Requirements\n",
            "docs/development/validation-and-quality.md": "# Validation\n",
            "docs/development/developing-tadp.md": "# Development\n",
            "docs/development/adapting-other-tools.md": "# Adapting tools\n",
            "evidence/README.md": "# Evidence\n",
            "evidence/authoritative/README.md": "# Authoritative\n",
            "evidence/authoritative/LLM/00_Codex_Invariant_Suite_Index.md": "# Suite\n",
            "evidence/non-authoritative/README.md": "# Context\n",
            "initiatives/README.md": "# Initiatives\n",
            "template/initiatives/README.md": "# Initiative template\n",
            "template/project/AGENTS.md": "# Instructions\n",
            "template/prompts/README.md": "# Prompts\n",
            "template/prompts/WORKFLOW-CONTRACT.md": "# Contract\n",
        }
        for number, name in enumerate(
            (
                "initiative_preparation",
                "proposal_creation",
                "proposal_alignment",
                "initiative_creation",
                "initiative_alignment",
                "initiative_assumption_review",
                "initiative_open_question_review",
                "initiative_sdk_api_alignment",
                "initiative_implementation_readiness_review",
                "initiative_execution",
                "initiative_finalization",
            )
        ):
            files[f"template/prompts/{number:02d}_{name}.md"] = (
                "# Prompt\n\n## Example usage\n\nattached initiative\n\n"
                "WORKFLOW-CONTRACT.md\n\n```text\nUse {initiative}.\n```\n"
            )
        for number, name in enumerate(
            (
                "Evidence_Authority_Specification",
                "Initiative_Governance_Specification",
                "Invariant_Conflict_Register",
                "Initiative_Lifecycle_Specification",
                "Git_Workflow_Specification",
                "Initiative_Scope_Specification",
                "Human_Decision_Receipt_Specification",
            ),
            start=1,
        ):
            files[f"evidence/authoritative/LLM/{number:02d}_Codex_{name}.md"] = "# Specification\n"
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def make_initiative(
        self,
        root: Path,
        *,
        status: str = "Proposed",
        initiative_type: str = "planning",
        history: str = "| 2026-11-10 | Initial | Proposed | proposal | initial | start | pending |",
    ) -> Path:
        initiative = root / "initiatives" / "example"
        files = {
            "README.md": (
                "# Example\n\n"
                f"**Status:** {status}\n"
                f"**Initiative type:** `{initiative_type}`\n\n"
                "### Lifecycle history\n\n"
                "| Effective date or event | From | To | Authority or evidence | Claim revision | Reason and affected scope | Git commit |\n"
                "|---|---|---|---|---|---|---|\n"
                f"{history}\n"
            ),
            "proposal/README.md": "# Sources\n",
            "proposal/proposal.md": "# Proposal\n",
            "assumption.md": "# Assumptions\n",
            "scope-assessment.md": "# Scope\n",
            "architecture.md": "# Architecture\n",
            "source-mapping.md": "# Mapping\n\nAuthoritative evidence\n\nVerification evidence\n",
            "open-questions.md": "# Questions\n",
            "implementation-roadmap.md": "# Roadmap\n",
            "implementation-steps.md": "# Steps\n",
        }
        for name, content in files.items():
            path = initiative / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return initiative

    def test_minimal_repository_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.assertEqual([], validate(root))

    def test_broken_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "README.md").write_text("[missing](missing.md)\n", encoding="utf-8")
            self.assertIn("TADP002", {item.code for item in validate(root)})

    def test_unresolved_token_is_reported_outside_templates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / "README.md").write_text("{{project_name}}\n", encoding="utf-8")
            self.assertIn("TADP003", {item.code for item in validate(root)})

    def test_incomplete_initiative_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative = root / "initiatives" / "example"
            initiative.mkdir()
            (initiative / "architecture.md").write_text("# Architecture\n", encoding="utf-8")
            self.assertIn("TADP004", {item.code for item in validate(root)})

    def test_git_repository_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            (root / ".git" / "HEAD").unlink()
            (root / ".git" / "config").unlink()
            (root / ".git").rmdir()
            self.assertIn("TADP012", {item.code for item in validate(root)})

    def test_illegal_lifecycle_transition_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.make_initiative(
                root,
                status="Completed",
                history="| 2026-11-10 | Proposed | Completed | none | initial | skipped | pending |",
            )
            self.assertIn("TADP009", {item.code for item in validate(root)})

    def test_completed_initiative_requires_completion_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            self.make_initiative(root, status="Completed")
            self.assertIn("TADP010", {item.code for item in validate(root)})

    def test_resolved_decision_requires_linked_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            initiative = self.make_initiative(root)
            (initiative / "assumption.md").write_text(
                "# Assumptions\n\n| ID | Disposition |\n|---|---|\n| A-01 | Confirmed |\n",
                encoding="utf-8",
            )
            codes = {item.code for item in validate(root)}
            self.assertIn("TADP013", codes)
            self.assertIn("TADP014", codes)

    def test_numbered_prompt_requires_shared_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            prompt = root / "template" / "prompts" / "00_initiative_preparation.md"
            prompt.write_text(
                "# Prompt\n\n## Example usage\n\nattached initiative\n\nUse {initiative}.\n",
                encoding="utf-8",
            )
            self.assertIn("TADP016", {item.code for item in validate(root)})


if __name__ == "__main__":
    unittest.main()

