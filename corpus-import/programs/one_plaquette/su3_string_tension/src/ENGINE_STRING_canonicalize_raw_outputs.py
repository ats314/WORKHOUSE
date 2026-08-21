#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
payload = json.loads(path.read_text(encoding="utf-8"))
payload.get("order4", {}).pop("walltime_seconds", None)
path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"canonicalized {path}")
