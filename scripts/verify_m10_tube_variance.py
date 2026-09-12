"""Replay scoped M10 ingredients; never certify full actual-ground domination."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from workhouse.invariants.w6_synchronized_m10 import synchronized_m10


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    needles = ["center tangency", "identical cutoffs", "quadratic jet", "potential-floor"]
    names = {name for name, *_ in synchronized_m10.checks if any(s in name for s in needles)}
    checks = [asdict(result) for result in synchronized_m10.run(names=names)]
    report = {
        "schema": "w6-m10-scoped-controls/v2",
        "passed": bool(checks) and all(c["passed"] for c in checks),
        "checks": checks,
        "actual_m10_status": "open",
        "scope": "Exact identities, obstruction witnesses, and reference-law moments. "
        "No actual-ground amplitude, normalized complement, or full-fiber score certification.",
    }
    text = json.dumps(report, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    print(text)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
