"""``workhouse`` command line: verify the arithmetic, print the status."""

from __future__ import annotations

import argparse
import sys

from . import ledger as ledger_mod
from .invariants import SUITES


def _verify(verbose: bool) -> int:
    failures = 0
    total = 0
    for suite in SUITES:
        results = suite.run()
        print(f"\n\033[1m{suite.name}\033[0m")
        for r in results:
            total += 1
            mark = "\033[32mPASS\033[0m" if r.passed else "\033[31mFAIL\033[0m"
            print(f"  {mark}  {r.name}")
            if r.detail and (verbose or not r.passed):
                print(f"        {r.detail}")
            if not r.passed:
                failures += 1
    print(f"\n{total - failures}/{total} checks passed")
    return 1 if failures else 0


def _status() -> int:
    led = ledger_mod.load()
    problems = ledger_mod.validate(led)

    print("\033[1mContradiction register\033[0m")
    for c in led.contradictions:
        flag = "\033[31m*\033[0m" if c["status"] == "open" else " "
        print(f"  {flag} {c['id']:<4} {c['status']:<22} {c['title']}")

    print("\n\033[1mGap analysis\033[0m")
    labels = {
        0: "tier 0 — bookkeeping (days)",
        1: "tier 1 — decisive finite computations (weeks)",
        2: "tier 2 — hard but structured (months)",
        3: "tier 3 — genuine open theorems (unbounded)",
    }
    for tier in sorted(labels):
        print(f"  {labels[tier]}")
        for g in led.gaps_by_tier(tier):
            bearing = " \033[33m[load-bearing]\033[0m" if g.get("load_bearing") else ""
            print(f"    {g['id']:<4} {g['title']}{bearing}")

    print("\n\033[1mDependency spine\033[0m")
    for line in led.dependency_spine:
        print(f"  - {line}")

    print(f"\n\033[1mHeadline\033[0m\n  {led.headline}")

    if problems:
        print("\n\033[31mLedger problems\033[0m")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\n\033[32mLedgers structurally sound.\033[0m")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="workhouse", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser("verify", help="re-derive the corpus's exact claims")
    v.add_argument("-v", "--verbose", action="store_true", help="show detail for passes too")

    sub.add_parser("status", help="print the contradiction and gap registers")

    args = parser.parse_args(argv)
    if args.command == "verify":
        return _verify(args.verbose)
    return _status()


if __name__ == "__main__":
    sys.exit(main())
