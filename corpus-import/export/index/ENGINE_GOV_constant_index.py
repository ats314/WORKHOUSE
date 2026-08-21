#!/usr/bin/env python3
"""
ENGINE_GOV_constant_index.py — exact-rational index + ratio linter for the ALL THEORY corpus.

Step 1 of export/DOC_GOV_index_design_2026-08-20.md.

The corpus's join keys are exact rationals, not concepts: 174 distinct non-trivial
rationals carry ~851 occurrences, and no embedding model will ever retrieve
20721577909065127111/7250590288602460800 from a semantic query. This builds the
exact index, and lints it for the two documented traps -- the Y=4u label erratum
and the factor-2 metric-convention trap -- both of which show up as the same
signature: one quantity appearing at an exact 2x or 4x ratio in two places.

Usage
-----
  python ENGINE_GOV_constant_index.py                       # build index, print report
  python ENGINE_GOV_constant_index.py --jsonl out.jsonl     # emit the index
  python ENGINE_GOV_constant_index.py --check               # CI mode: exit 1 on UNCLASSIFIED pairs

Classifications live in CERT_GOV_constant_ratio_classifications.json next to this file:
each known-legitimate 2x/4x pair is recorded with a reason, so that any NEW
unclassified pair is a genuine alarm rather than noise.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CLASSIFICATIONS = os.path.join(HERE, "CERT_GOV_constant_ratio_classifications.json")

SKIP_DIRS = {"QUARANTINE", "archive", "__pycache__", ".git", "node_modules", "GITHUB"}
EXTS = (".md", ".tex")

# A rational is "non-trivial" -- i.e. an identity key rather than bookkeeping --
# when either part is large. Small fractions like 5/12 recur everywhere and carry
# no locating power.
MIN_MAGNITUDE = 1000

FRAC_PATTERNS = [
    re.compile(r"\\[dt]?frac\{\s*(-?\d+)\s*\}\{\s*(-?\d+)\s*\}"),
    re.compile(r"(?<![\w./])(-?\d{4,})\s*/\s*(\d{4,})(?![\w.])"),
]

RATIOS = (Fraction(2), Fraction(4))


def canon(fr: Fraction) -> str:
    return f"{fr.numerator}/{fr.denominator}"


def scan(root: str = ROOT):
    """-> {Fraction: [{'file','line','context'}]}"""
    occ: dict[Fraction, list] = collections.defaultdict(list)
    n_files = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(EXTS):
                continue
            path = os.path.join(dirpath, fn)
            try:
                lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
            except OSError:
                continue
            n_files += 1
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            for i, line in enumerate(lines, 1):
                for pat in FRAC_PATTERNS:
                    for num, den in pat.findall(line):
                        try:
                            if int(den) == 0:
                                continue
                            fr = Fraction(int(num), int(den))
                        except (ValueError, ZeroDivisionError):
                            continue
                        if abs(fr.numerator) < MIN_MAGNITUDE and fr.denominator < MIN_MAGNITUDE:
                            continue
                        occ[fr].append(
                            {"file": rel, "line": i, "context": line.strip()[:160]}
                        )
    return occ, n_files


def ratio_pairs(occ, min_occ: int = 3):
    """Pairs (a, b, r) with b == a*r for r in {2,4} and both well-attested."""
    keys = [k for k in occ if len(occ[k]) >= min_occ]
    keyset = set(keys)
    out, seen = [], set()
    for a in keys:
        for r in RATIOS:
            b = a * r
            if b in keyset and abs(a) < abs(b) and (a, b) not in seen:
                seen.add((a, b))
                out.append((a, b, r))
    return sorted(out, key=lambda t: -(len(occ[t[0]]) + len(occ[t[1]])))


def load_classifications() -> dict:
    if not os.path.exists(CLASSIFICATIONS):
        return {}
    with open(CLASSIFICATIONS, encoding="utf-8") as fh:
        return {tuple(k.split(" ~ ")): v for k, v in json.load(fh).items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--jsonl", help="write the constant index here")
    ap.add_argument("--check", action="store_true",
                    help="CI mode: exit 1 if any 2x/4x pair is unclassified")
    ap.add_argument("--min-occ", type=int, default=3)
    args = ap.parse_args()

    occ, n_files = scan(args.root)
    total = sum(len(v) for v in occ.values())

    if args.jsonl:
        with open(args.jsonl, "w", encoding="utf-8") as fh:
            for fr, hits in sorted(occ.items(), key=lambda kv: -len(kv[1])):
                fh.write(json.dumps({
                    "constant": canon(fr),
                    "numerator": str(fr.numerator),
                    "denominator": str(fr.denominator),
                    "float": float(fr),
                    "occurrences": len(hits),
                    "files": sorted({h["file"] for h in hits}),
                    "hits": hits,
                }, ensure_ascii=False) + "\n")

    known = load_classifications()
    pairs = ratio_pairs(occ, args.min_occ)
    unclassified = [p for p in pairs if (canon(p[0]), canon(p[1])) not in known]

    if not args.check:
        print(f"CONSTANT INDEX  —  {n_files} prose files scanned")
        print(f"  distinct non-trivial rationals : {len(occ)}")
        print(f"  total occurrences              : {total}\n")
        print("  most-cited (the corpus's join keys):")
        for fr, hits in sorted(occ.items(), key=lambda kv: -len(kv[1]))[:8]:
            ndocs = len({h["file"] for h in hits})
            print(f"     {canon(fr)[:46]:<46} {len(hits):>3} occ / {ndocs:>2} files")
        print()

    print(f"RATIO LINTER  —  {len(pairs)} pairs at exactly 2x or 4x, "
          f"{len(unclassified)} unclassified")
    for a, b, r in pairs:
        key = (canon(a), canon(b))
        mark = "  ok " if key in known else "  !! "
        note = known.get(key, "UNCLASSIFIED — classify or fix")
        print(f"{mark}{canon(a)}  x{r}  {canon(b)}")
        print(f"       {note}")
        if key not in known:
            for fr in (a, b):
                files = sorted({h['file'] for h in occ[fr]})[:3]
                print(f"       {canon(fr)}: {', '.join(files)}")

    if args.check and unclassified:
        print(f"\nFAIL: {len(unclassified)} unclassified 2x/4x constant pair(s).")
        print("Each is either the Y=4u erratum, a metric-convention factor of 2,")
        print("or a legitimate relationship that belongs in "
              f"{os.path.basename(CLASSIFICATIONS)}.")
        return 1
    if args.check:
        print("\nOK: every 2x/4x constant relationship in the corpus is classified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
