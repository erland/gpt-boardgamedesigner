#!/usr/bin/env python3
"""G03 deterministic ZIP inventory contract, with positive and negative fixtures.

Tests archive treatment only; does not claim an LLM host test.
"""
import io
import json
import unittest
import zipfile
from pathlib import PurePosixPath

FIXTURE = {
    "README.md": "# Stjärnstigen\nEtt print-and-play-spel.",
    "PROJECT_STATUS.md": "version: 0.1.0\nstate: prototype\n",
    "CHANGELOG.md": "# Changelog\n- Skapad prototyp",
    "docs/rules.md": "# Regler\n",
    "data/cards.json": '{"cards":[{"id":"a"}]}',
    "assets/board.svg": "<svg xmlns='http://www.w3.org/2000/svg'/>",
    "output/board.pdf": "%PDF-1.4\n",
}
SOURCE_DIRS = ("docs/", "data/", "assets/", "schemas/", "templates/", "scripts/")
OUTPUT_PREFIX = "output/"

def fixture_zip(entries):
    memory = io.BytesIO()
    with zipfile.ZipFile(memory, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)
    return memory.getvalue()

def inventory(data):
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        if z.testzip() is not None:
            raise ValueError("corrupt archive")
        names = [item.filename for item in z.infolist() if not item.is_dir()]
        for name in names:
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or "\\" in name:
                raise ValueError("unsafe archive path")
        return {
            "files": sorted(names),
            "has_readme": "README.md" in names,
            "has_status": "PROJECT_STATUS.md" in names,
            "has_changelog": "CHANGELOG.md" in names,
            "sources": sorted(n for n in names if n.startswith(SOURCE_DIRS)),
            "generated_output": sorted(n for n in names if n.startswith(OUTPUT_PREFIX)),
            "missing_metadata": [n for n in ("README.md", "PROJECT_STATUS.md", "CHANGELOG.md") if n not in names],
        }

class G03FixtureTests(unittest.TestCase):
    def test_positive_inventory(self):
        result = inventory(fixture_zip(FIXTURE))
        self.assertTrue(result["has_readme"] and result["has_status"] and result["has_changelog"])
        self.assertEqual(result["generated_output"], ["output/board.pdf"])
        self.assertEqual(result["sources"], ["assets/board.svg", "data/cards.json", "docs/rules.md"])
        self.assertEqual(result["missing_metadata"], [])
    def test_missing_status_is_reported(self):
        result = inventory(fixture_zip({k:v for k,v in FIXTURE.items() if k != "PROJECT_STATUS.md"}))
        self.assertFalse(result["has_status"])
        self.assertEqual(result["missing_metadata"], ["PROJECT_STATUS.md"])
    def test_rejects_parent_traversal(self):
        with self.assertRaisesRegex(ValueError, "unsafe archive path"):
            inventory(fixture_zip({"../evil.txt": "x"}))
    def test_rejects_absolute_path(self):
        with self.assertRaisesRegex(ValueError, "unsafe archive path"):
            inventory(fixture_zip({"/evil.txt": "x"}))

if __name__ == "__main__":
    unittest.main(verbosity=2)
