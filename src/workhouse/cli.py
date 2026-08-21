"""``workhouse`` command line: verify the arithmetic, print the status."""

from __future__ import annotations

import argparse
import sys

from . import certified as certified_mod
from . import frontier as frontier_mod
from . import ledger as ledger_mod
from . import literature as literature_mod
from . import triage as triage_mod
from .invariants import SUITES


def _verify(verbose: bool, only: str | None = None, tier: int | None = None) -> int:
    """Run the checks, or one of them.

    ``--only`` exists so a single claim can be re-established on its own, in
    about a second, by someone who does not trust it. A certification nobody can
    cheaply reproduce is only a claim of authority. Matching is a
    case-insensitive substring, so the name from CERTIFIED.md can be pasted
    whole or abbreviated.
    """
    failures = 0
    total = 0
    needle = only.lower() if only else None
    for suite in SUITES:
        results = [
            r
            for r in suite.run()
            if (needle is None or needle in r.name.lower()) and (tier is None or r.tier == tier)
        ]
        if not results:
            continue
        print(f"\n\033[1m{suite.name}\033[0m")
        for r in results:
            total += 1
            mark = "\033[32mPASS\033[0m" if r.passed else "\033[31mFAIL\033[0m"
            print(f"  {mark}  \033[2mT{r.tier}\033[0m  {r.name}")
            # A filtered run is someone checking one thing: always show the
            # numbers, since the verdict alone is what they came not to trust.
            if r.detail and (verbose or needle or not r.passed):
                print(f"        {r.detail}")
            if r.detail and needle:
                print(f"        \033[2msrc/workhouse/invariants.py:{r.line}\033[0m")
            if not r.passed:
                failures += 1
    if total == 0:
        print(f"no check matches {only!r}" if only else f"no check at tier {tier}")
        return 1
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


def _frontier(write: bool, brief: bool) -> int:
    if brief:
        print(frontier_mod.brief())
        return 0
    if write:
        target = frontier_mod.write()
        print(f"wrote {target.relative_to(frontier_mod.ROOT)}")
        return 0
    print(frontier_mod.render(frontier_mod.compute()))
    return 0


def _certified(write: bool) -> int:
    if write:
        target = certified_mod.write()
        print(f"wrote {target.relative_to(certified_mod.ROOT)}")
        return 0
    print(certified_mod.render())
    return 0


def _lit(target: str | None) -> int:
    lit = literature_mod.load()
    problems = literature_mod.validate(lit)
    print(literature_mod.format_index(lit, target=target))
    if problems:
        print("\n\033[31mLiterature index problems\033[0m")
        for p in problems:
            print(f"  - {p}")
        return 1
    return 0


def _triage(directory: str, limit: int) -> int:
    from pathlib import Path

    try:
        report = triage_mod.scan(Path(directory))
    except NotADirectoryError as exc:
        print(f"not a directory: {exc}")
        return 1
    print(triage_mod.format_report(report, limit=limit))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="workhouse", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser("verify", help="re-derive the corpus's exact claims")
    v.add_argument("-v", "--verbose", action="store_true", help="show detail for passes too")
    v.add_argument("--only", metavar="TEXT", help="run just the checks whose name contains TEXT")
    v.add_argument("--tier", type=int, choices=(1, 2), help="run only T1 or only T2 checks")

    sub.add_parser("status", help="print the contradiction and gap registers")

    fr = sub.add_parser("frontier", help="what is established, disputed, refuted, and next")
    fr.add_argument("-w", "--write", action="store_true", help="regenerate FRONTIER.md")
    fr.add_argument(
        "-b", "--brief", action="store_true", help="the short form injected at session start"
    )

    li = sub.add_parser("lit", help="published work, and which claim each paper bears on")
    li.add_argument(
        "--for",
        dest="target",
        metavar="ID",
        help="show only work bearing on this claim (C2, G18, R14, U3, or a constant)",
    )

    ce = sub.add_parser(
        "certified", help="what is certified, ranked by tier, with how to re-check each claim"
    )
    ce.add_argument("-w", "--write", action="store_true", help="regenerate CERTIFIED.md")

    t = sub.add_parser(
        "triage",
        help="survey an unpinned archive against what this repository already knows",
    )
    t.add_argument("directory", help="path to the archive (read-only; nothing is copied)")
    t.add_argument("--limit", type=int, default=25, help="rows per section (default 25)")

    args = parser.parse_args(argv)
    if args.command == "verify":
        return _verify(args.verbose, args.only, args.tier)
    if args.command == "lit":
        return _lit(args.target)
    if args.command == "certified":
        return _certified(args.write)
    if args.command == "frontier":
        return _frontier(args.write, args.brief)
    if args.command == "triage":
        return _triage(args.directory, args.limit)
    return _status()


if __name__ == "__main__":
    sys.exit(main())
