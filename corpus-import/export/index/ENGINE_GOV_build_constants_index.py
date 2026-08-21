#!/usr/bin/env python3
"""
ENGINE_GOV_build_constants_index.py — generate theory/DOC_FLUX_constants_index.md from the corpus.

The corpus's join keys are exact rationals: ~174 distinct non-trivial constants
in the live tree, several appearing in 30-70 separate files. Nothing in the tree
listed them. theory/DOC_GOV_conventions.md section 3 is the designated "citable
constants" table but covers only the June Birman-Schwinger era and contains none
of the flux-band constants.

This builds that missing table: every constant, the symbol it is assigned to,
where it is defined, how widely it is cited, and which document tiers vouch for
it. QUARANTINE is scanned too, but only ever ranks last -- a superseded or
duplicate file must never win the "defined in" column -- and constants that live
ONLY in QUARANTINE get their own section, because each is either a corrected
value or a dropped result.

  python ENGINE_GOV_build_constants_index.py            # write theory/DOC_FLUX_constants_index.md
  python ENGINE_GOV_build_constants_index.py --stdout   # preview
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "theory", "DOC_FLUX_constants_index.md")

SKIP_DIRS = {"archive", "__pycache__", ".git", "GITHUB"}
EXTS = (".md", ".tex")
MIN_MAG = 1000

FRAC_TEX = re.compile(r"\\[dt]?frac\{\s*(-?\d+)\s*\}\{\s*(-?\d+)\s*\}")
FRAC_SLASH = re.compile(r"(?<![\w./])(-?\d{4,})\s*/\s*(\d{4,})(?![\w.])")

# A symbol is the token immediately left of the "=" preceding the fraction.
# It contains no whitespace and is bounded -- an earlier greedy version captured
# whole clauses ("m_{1^{+-}}(k,u)") for a constant that is really d_3.
SYMBOL_TAIL = re.compile(r"([\\A-Za-z][A-Za-z0-9_^{}\\,()]{0,28})$")
BAD_SYMBOL = re.compile(r"frac|begin|end|left|right|cdot|quad|text|approx", re.I)

# Most authoritative first. QUARANTINE is pinned last by construction.
TIERS = [
    ("authority",  lambda r: r.startswith("corpus/")),
    ("theorem",    lambda r: r.startswith("theory/theorems/")),
    ("convention", lambda r: r.startswith("theory/") and "CONVENTIONS" in r),
    ("manuscript", lambda r: r.startswith("papers/")),
    ("campaign",   lambda r: r.startswith("programs/")),
    ("numerics",   lambda r: r.startswith("numerics/")),
    ("note",       lambda r: r.startswith("theory/")),
    ("record",     lambda r: r.startswith("records/")),
    ("other",      lambda r: not r.startswith("QUARANTINE/")),
    ("superseded", lambda r: True),
]
TIER_ORDER = {name: i for i, (name, _) in enumerate(TIERS)}


def tier_of(rel: str) -> str:
    if rel.startswith("QUARANTINE/"):
        return "superseded"
    for name, test in TIERS:
        if test(rel):
            return name
    return "other"


def clean_symbol(s: str) -> str:
    s = re.sub(r"\s+", "", s.strip())
    s = re.sub(r"\\(?:mathrm|mathsf|text|operatorname)\{([^}]*)\}", r"\1", s)
    s = s.replace("\\left", "").replace("\\right", "").strip("&$ ")
    if not s or len(s) > 32:
        return ""
    if BAD_SYMBOL.search(s) or not re.match(r"^[\\A-Za-z]", s):
        return ""
    if s.lower() in {"and", "the", "with", "where", "then", "is", "be"}:
        return ""
    return s


def symbol_from_left(left: str) -> str:
    """Recover the assigned symbol from the text left of a fraction."""
    s = re.sub(r"[-+]\s*$", "", left.rstrip()).rstrip()
    if not s.endswith("="):
        return ""
    s = s[:-1].rstrip()
    if s.endswith(("=", "<", ">", "\\leq", "\\geq", "\\neq")):
        return ""          # chained or non-defining relation
    m = SYMBOL_TAIL.search(s)
    return clean_symbol(m.group(1)) if m else ""


def canon(fr: Fraction) -> str:
    return f"{fr.numerator}/{fr.denominator}"


def scan():
    occ = collections.defaultdict(list)
    nfiles = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(EXTS):
                continue
            path = os.path.join(dirpath, fn)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            nfiles += 1
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            tier = tier_of(rel)
            lines = text.split("\n")
            for i, line in enumerate(lines):
                for pat in (FRAC_TEX, FRAC_SLASH):
                    for m in pat.finditer(line):
                        try:
                            if int(m.group(2)) == 0:
                                continue
                            fr = Fraction(int(m.group(1)), int(m.group(2)))
                        except (ValueError, ZeroDivisionError):
                            continue
                        if abs(fr.numerator) < MIN_MAG and fr.denominator < MIN_MAG:
                            continue
                        left = line[: m.start()]
                        sym = symbol_from_left(left)
                        if not sym and left.strip() in ("", "-", "=-", "="):
                            for back in (1, 2):
                                if i - back < 0:
                                    break
                                prev = lines[i - back].strip()
                                sym = symbol_from_left(prev)
                                if sym or (prev and not prev.endswith(("=", "\\\\", "&"))):
                                    break
                        occ[fr].append({"file": rel, "line": i + 1,
                                        "tier": tier, "symbol": sym})
    return occ, nfiles


def live(hits):
    return [h for h in hits if h["tier"] != "superseded"]


def best_symbol(hits):
    """Prefer the symbol asserted by the most authoritative tier that names one."""
    named = [h for h in hits if h["symbol"]]
    if not named:
        return ""
    top = min(TIER_ORDER[h["tier"]] for h in named)
    best = [h["symbol"] for h in named if TIER_ORDER[h["tier"]] == top]
    return collections.Counter(best).most_common(1)[0][0]


def defining_hit(hits):
    named = [h for h in hits if h["symbol"]] or hits
    return sorted(named, key=lambda h: (TIER_ORDER[h["tier"]], h["file"], h["line"]))[0]


def fmt(v: str, width: int = 44) -> str:
    return f"`{v}`" if len(v) <= width else f"`{v[:width]}…`"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    occ, nfiles = scan()
    live_map = {f: h for f, h in occ.items() if live(h)}
    quarantine_only = {f: h for f, h in occ.items() if not live(h)}

    ranked = sorted(live_map.items(), key=lambda kv: (-len(live(kv[1])), str(kv[0])))
    cited = [(f, h) for f, h in ranked if len(live(h)) >= 2]
    single = [(f, h) for f, h in ranked if len(live(h)) == 1]
    n_live_occ = sum(len(live(h)) for h in live_map.values())

    L: list[str] = []
    A = L.append
    A("# CONSTANTS INDEX — every exact rational in the corpus\n")
    A("**Generated** by `export/index/ENGINE_GOV_build_constants_index.py`. "
      "Regenerate after any corpus edit; do not hand-edit.\n")
    A(f"Scanned **{nfiles}** prose files (`.md` + `.tex`, excluding `archive/`). "
      f"**{len(live_map)}** distinct non-trivial exact rationals live in the tree "
      f"across **{n_live_occ}** occurrences; **{len(quarantine_only)}** more appear "
      "only in `QUARANTINE/`.\n")

    A("## Why this file exists\n")
    A("The join keys of this corpus are exact rationals, not concepts. "
      "`109151/249696` appears in dozens of separate files; so does "
      "`20721577909065127111/7250590288602460800`. No semantic search will ever "
      "retrieve those from a natural-language query, so an exact index is the "
      "primary retrieval surface — and until this file, nothing in the tree listed "
      "them. `theory/DOC_GOV_conventions.md` §3 is the designated citable-constants table "
      "but covers only the June Birman–Schwinger era (κ, ceiling-law, Lemma A/B); "
      "this file covers the flux-band program.\n")

    A("**Reading the columns.** *Symbol* is recovered mechanically from the most "
      "authoritative occurrence that assigns the value to a name — a strong hint, "
      "**not a definition**; verify against the source before citing. *Cited* counts "
      "live occurrences and distinct live files. *Tiers* lists the document classes "
      "carrying the constant, so you can see whether it is vouched for by the "
      "authority stack or only by a manuscript. A constant carried by `manuscript` "
      "but not `authority` is a candidate for exactly the kind of drift this corpus "
      "has a documented history of.\n")

    A("> **Before quoting any row:** pin the convention via `theory/DOC_GOV_conventions.md`, "
      "then check `export/index/CERT_GOV_constant_ratio_classifications.json`. Four constants "
      "here stand in exact 2× or 4× relationships with another. Three are legitimate "
      "convention (real-space `β/4` vs symbol `β`; `τ₄` vs `2τ₄`); the fourth is a "
      "**live symbol collision** — `κ` denotes `2a(n)` in `corpus/` and `a(n)` in "
      "flat-band manuscript v1.1. Neither is wrong; anyone quoting across them "
      "would be.\n")
    A("---\n")

    A(f"## Cited constants ({len(cited)})\n")
    A("| Symbol | Value | Cited | Tiers | Defined in |")
    A("|---|---|---:|---|---|")
    for fr, hits in cited:
        lh = live(hits)
        sym = best_symbol(lh) or best_symbol(hits)
        d = defining_hit(lh)
        tiers = sorted({h["tier"] for h in lh}, key=lambda t: TIER_ORDER[t])
        if len(hits) > len(lh):
            tiers.append("+quarantine")
        A(f"| {('`'+sym+'`') if sym else '—'} | {fmt(canon(fr))} | "
          f"{len(lh)} / {len({h['file'] for h in lh})}f | {', '.join(tiers)} | "
          f"`{d['file']}`:{d['line']} |")
    A("")

    if single:
        A(f"## Single-citation constants ({len(single)})\n")
        A("Cited exactly once in the live tree. Either genuinely one-off, or a "
          "constant that lost its cross-references — worth knowing which.\n")
        A("| Value | Symbol | Where |")
        A("|---|---|---|")
        for fr, hits in single:
            d = live(hits)[0]
            sym = best_symbol(hits)
            A(f"| {fmt(canon(fr))} | {('`'+sym+'`') if sym else '—'} | "
              f"`{d['file']}`:{d['line']} |")
        A("")

    if quarantine_only:
        A(f"## Constants appearing only in QUARANTINE ({len(quarantine_only)})\n")
        A("These occur in **no live document**. Each is either a value that was "
          "corrected — in which case the correction should be traceable — or a "
          "result that was dropped without a successor. Both are worth knowing; "
          "neither is citable.\n")
        A("| Value | Symbol | Where | Occ |")
        A("|---|---|---|---:|")
        for fr, hits in sorted(quarantine_only.items(), key=lambda kv: -len(kv[1])):
            d = defining_hit(hits)
            sym = best_symbol(hits)
            A(f"| {fmt(canon(fr))} | {('`'+sym+'`') if sym else '—'} | "
              f"`{d['file']}`:{d['line']} | {len(hits)} |")
        A("")

    text = "\n".join(L)
    if args.stdout:
        sys.stdout.write(text)
    else:
        open(OUT, "w", encoding="utf-8", newline="\n").write(text)
        print(f"wrote theory/DOC_FLUX_constants_index.md  "
              f"({len(cited)} cited, {len(single)} single, "
              f"{len(quarantine_only)} quarantine-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
