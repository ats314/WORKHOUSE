#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
out = root / "SHA256SUMS.json"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

records = {}
for p in sorted(root.iterdir()):
    if p.is_file() and p.name != out.name:
        records[p.name] = {
            "sha256": sha256(p),
            "size_bytes": p.stat().st_size,
        }
out.write_text(
    json.dumps(records, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(out)
