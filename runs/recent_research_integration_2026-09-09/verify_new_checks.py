"""Replay every newly integrated check; print exact source locations and verdicts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from workhouse.invariants import SUITES  # noqa: E402

MODULES = {"anisotropy_variance", "hodge_feshbach", "feshbach_resolvent"}


def main():
    records = []
    for suite in SUITES:
        names = {
            name
            for name, _section, _tier, fn in suite.checks
            if fn.__module__.rsplit(".", 1)[-1] in MODULES
        }
        if not names:
            continue
        for result in suite.run(names=names):
            records.append(
                {
                    "suite": suite.name,
                    "name": result.name,
                    "tier": result.tier,
                    "passed": result.passed,
                    "detail": result.detail,
                    "source": result.source,
                    "yields": result.yields,
                }
            )
    report = {
        "cache_used": False,
        "total": len(records),
        "passed": sum(row["passed"] for row in records),
        "checks": records,
    }
    print(json.dumps(report, indent=2, sort_keys=True, default=str))
    return 0 if len(records) == 19 and all(row["passed"] for row in records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
