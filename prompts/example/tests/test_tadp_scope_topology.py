"""Protocol-owned fixtures for the complete structural branch hierarchy."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from tadp_scopes import SCOPE_HEADERS, git
import test_tadp_scopes as fixtures


class ScopeTopologyTests(unittest.TestCase):
    setUp = fixtures.ScopeTests.setUp
    write = fixtures.ScopeTests.write
    save = fixtures.ScopeTests.save
    fixture = fixtures.ScopeTests.fixture
    flush = fixtures.ScopeTests.flush
    findings = fixtures.ScopeTests.findings

    def topology(self):
        self.fixture()
        for name, kind, parent in (
            ("v1.1", "Minor", "v1"),
            ("v1.0.1", "Patch", "v1.0"),
            ("v2", "Major", "trunk"),
            ("v2.0", "Minor", "v2"),
            ("v2.1", "Minor", "v2"),
            ("v2.1.1", "Patch", "v2.1"),
        ):
            git(self.root, "branch", name, parent)
            self.scopes.append(dict(zip(SCOPE_HEADERS, (
                name, kind, parent, name, parent, self.base, parent,
                "[note](../notes/note.md), [suite](../notes/README.md)",
                "None", "None", "Open", "Pending", "Not closed",
                "Not integrated", self.base,
            ))))
            self.write(f"initiatives/{name}/README.md", (
                f"**Scope:** {name}\n\n[registry](../version-scopes.md)\n\n"
                "[membership](../initiative-index.md)\n"
            ))
        children = {
            "v1": "v1.0, v1.1", "v1.0": "v1.0.1",
            "v2": "v2.0, v2.1", "v2.1": "v2.1.1",
        }
        for row in self.scopes:
            row["Child scopes"] = children.get(row["Scope"], "None")

    def test_complete_major_minor_patch_topology_is_valid(self):
        self.topology()
        self.assertEqual(self.findings(), [])
        # The fixture creates each ref from its actual declared parent tip.
        for row in self.scopes:
            self.assertEqual(git(self.root, "rev-parse", row["Captured base ref"]), row["Captured base commit"])

    def test_minor_siblings_patch_parent_major_orphan_and_cycle_rejected(self):
        self.topology()
        baseline = deepcopy(self.scopes)
        for scope, wrong_parent in (
            ("v1.1", "v1.0"), ("v2.1", "v2.0"),
            ("v2.1", "v1"), ("v2.1.1", "v2.0"),
            ("v2", "v1"), ("v1", "v1.0.1"),
        ):
            with self.subTest(scope=scope, wrong_parent=wrong_parent):
                self.scopes = deepcopy(baseline)
                row = next(item for item in self.scopes if item["Scope"] == scope)
                for field in ("Structural parent", "Captured base ref", "Integration target"):
                    row[field] = wrong_parent
                self.assertTrue(self.findings())
        self.scopes = [row for row in deepcopy(baseline) if row["Scope"] != "v2.1"]
        self.assertIn("missing ancestor v2.1", " ".join(self.findings()))


if __name__ == "__main__":
    unittest.main()
