#!/usr/bin/env python3
"""Export a real, deterministic G03 fixture ZIP and expected inventory for host acceptance."""
from pathlib import Path
import json
import zipfile
from test_g03_zip_inventory import FIXTURE, inventory

def main():
    out = Path("build/host-fixtures")
    out.mkdir(parents=True, exist_ok=True)
    path = out / "G03-stjarnstigen-project.zip"
    with zipfile.ZipFile(path, "w") as z:
        for name, content in sorted(FIXTURE.items()):
            info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, content.encode("utf-8"))
    actual = inventory(path.read_bytes())
    (out / "G03-expected-inventory.json").write_text(
        json.dumps(actual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    assert actual["missing_metadata"] == []
    assert actual["generated_output"] == ["output/board.pdf"]
    print(f"Fixture: {path}; entries={len(actual['files'])}")

if __name__ == "__main__":
    main()
