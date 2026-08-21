"""One search across everything this repository knows how to be asked.

The premise, measured rather than assumed: **the join keys of this corpus are
exact rationals, not concepts.** No embedding retrieves ``109151/249696`` from a
natural-language query, 454 of 855 corpus files carry nothing checkable at all,
and ``5/48`` alone lives in 44 code files the prose index cannot see.

So a query is resolved in four ways at once, cheapest first:

1. **exact rational** -- ``109151/249696`` matches by *value*, so ``-5/48`` finds
   ``-10/96`` and a decimal that rounds to it;
2. **decimal prefix** -- ``-0.88009871`` finds both sides of C20;
3. **symbol or alias** -- ``q_old`` finds ``q_band^(4)``, because the curated
   alias index knows the corpus spells it differently;
4. **claim id** -- ``C2``, ``G3``, ``R14``, ``U3``.

Corpus occurrences are looked up last and only on request, because scanning 928
files costs real time and is usually not what the question needed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from . import claims as claims_mod

RATIONAL = re.compile(r"^\s*(-?\d+)\s*/\s*(\d+)\s*$")
DECIMAL = re.compile(r"^\s*-?\d*\.\d+(?:[eE][-+]?\d+)?\s*$")
CLAIM_ID = re.compile(r"^[CGRU]\d+$", re.IGNORECASE)


@dataclass
class Hit:
    how: str
    claim: claims_mod.Claim


def _as_fraction(text: str) -> Fraction | None:
    m = RATIONAL.match(text)
    if m:
        try:
            return Fraction(int(m.group(1)), int(m.group(2)))
        except ZeroDivisionError:
            return None
    if DECIMAL.match(text):
        try:
            return Fraction(text.strip())
        except ValueError:
            return None
    return None


def _claim_value(claim: claims_mod.Claim) -> Fraction | None:
    if not claim.value:
        return None
    m = RATIONAL.match(claim.value)
    if m:
        try:
            return Fraction(int(m.group(1)), int(m.group(2)))
        except ZeroDivisionError:
            return None
    try:
        return Fraction(claim.value)
    except (ValueError, ZeroDivisionError):
        return None


def search(
    query: str,
    catalogue: list[claims_mod.Claim] | None = None,
    symbols: list[dict[str, Any]] | None = None,
) -> tuple[list[Hit], list[dict[str, Any]]]:
    """Return matching claims and the alias records that matched."""
    catalogue = catalogue if catalogue is not None else claims_mod.collect()
    symbols = symbols if symbols is not None else claims_mod.symbol_records(catalogue)
    needle = query.strip()
    lowered = needle.lower()

    hits: dict[str, Hit] = {}

    def add(how: str, claim: claims_mod.Claim) -> None:
        hits.setdefault(claim.id, Hit(how, claim))

    wanted = _as_fraction(needle)
    if wanted is not None:
        # Match by VALUE, not by spelling: -5/48 and -10/96 are the same claim,
        # and a decimal query should reach the exact rational behind it.
        for claim in catalogue:
            value = _claim_value(claim)
            if value is not None and value == wanted:
                add("exact value", claim)
        if DECIMAL.match(needle):
            digits = needle.strip().rstrip("0")
            for claim in catalogue:
                if claim.decimal is None:
                    continue
                if repr(claim.decimal).startswith(digits) or f"{claim.decimal!r}".startswith(
                    digits.lstrip("+")
                ):
                    add("decimal prefix", claim)

    if CLAIM_ID.match(needle):
        target = needle.upper()
        for claim in catalogue:
            if claim.id == target or target in claim.related:
                add("claim id", claim)

    matched_symbols = []
    for symbol in symbols:
        keys = [k for k in symbol["search_keys"] if k]
        # Forbidden spellings are matched deliberately. They are precisely what
        # someone types when they have the wrong mental model, so that query is
        # the one moment the warning can still do some good.
        banned = [f["text"] for f in symbol.get("forbidden", [])]
        if any(lowered == k.lower() or lowered in k.lower() for k in keys) or any(
            lowered == b.lower() for b in banned
        ):
            matched_symbols.append(symbol)
            for claim_id in symbol["mentioned_by"]:
                claim = next((c for c in catalogue if c.id == claim_id), None)
                if claim:
                    add(f"alias of {symbol['canonical']}", claim)
            for related in symbol.get("claims", []):
                claim = next((c for c in catalogue if c.id == related), None)
                if claim:
                    add(f"{symbol['canonical']} claims", claim)

    # Free-text fallback. Short needles need a token boundary or they match
    # noise: "m_4" is a substring of "LINKED_VACUUM_4" and that is not a hit.
    if len(needle) >= 3:
        if len(needle) <= 5:
            pattern = re.compile(rf"(?<![A-Za-z0-9]){re.escape(needle)}(?![A-Za-z0-9])", re.I)
        else:
            pattern = re.compile(re.escape(needle), re.I)
        for claim in catalogue:
            blob = f"{claim.id} {claim.statement} {claim.detail} {claim.value or ''}"
            if pattern.search(blob):
                add("text", claim)

    order = {"exact value": 0, "decimal prefix": 1, "claim id": 2}
    ranked = sorted(
        hits.values(),
        key=lambda h: (order.get(h.how, 3 if h.how.startswith("alias") else 4), h.claim.id),
    )
    return ranked, matched_symbols


@dataclass
class CorpusPresence:
    """Where an exact value lives in the corpus, shaped for independence
    counting: AGENTS.md's instruction is to count distinct originating
    computations, not raw occurrences, so files are the unit here."""

    total_occurrences: int
    #: (relative path, occurrences in that file, first line, sample text)
    files: list[tuple[str, int, int, str]]


def corpus_occurrences(query: str, limit: int = 10) -> CorpusPresence | None:
    """Where an exact rational actually appears across BOTH prose and code.

    Separate and opt-in: scanning the corpus costs real time. Prose files are
    included because ~200 values exist only there, and a front-door "no corpus
    occurrence" for a value sitting in six .md files is a confident false
    negative — the exact failure mode this repository's culture warns against.
    """
    from . import corpus_index

    wanted = _as_fraction(query)
    if wanted is None:
        return None
    table = corpus_index.scan_cached()
    record = table.get(wanted)
    if record is None:
        return CorpusPresence(0, [])
    seen: dict[str, list] = {}
    for o in record.occurrences:
        rel = str(o.path.relative_to(corpus_index.CORPUS_DIR))
        seen.setdefault(rel, []).append(o)
    files = []
    for rel in sorted(seen, key=lambda r: (-len(seen[r]), r))[:limit]:
        first = min(seen[rel], key=lambda o: o.line)
        files.append((rel, len(seen[rel]), first.line, " ".join(first.text.split())[:120]))
    return CorpusPresence(len(record.occurrences), files)


def format_results(
    query: str,
    hits: list[Hit],
    symbols: list[dict[str, Any]],
    occurrences: CorpusPresence | None = None,
    limit: int = 20,
) -> str:
    out: list[str] = []
    w = out.append

    for symbol in symbols:
        w(f"\033[1m{symbol['canonical']}\033[0m — {' '.join(str(symbol['meaning']).split())}")
        if symbol.get("coined_here"):
            w("  \033[33mCoined in this repository. The corpus does not use this name;")
            spellings = ", ".join(symbol["corpus_spellings"])
            w(f"  it writes {spellings}. Not finding it is not absence.\033[0m")
        else:
            w(f"  corpus spellings: {', '.join(symbol['corpus_spellings'])}")
        if symbol.get("code_names"):
            w(f"  in code: {', '.join(symbol['code_names'])}")
        for forbidden in symbol.get("forbidden", []):
            hit = query.strip().lower() == forbidden["text"].lower()
            lead = "YOU SEARCHED FOR A FORBIDDEN NAME: " if hit else "never call it "
            w(
                f"  \033[31m{lead}{forbidden['text']}\033[0m — "
                f"{' '.join(str(forbidden['why']).split())}"
            )
        w("")

    if not hits:
        w(f"no claim matches {query!r}.")
        w("")
        w("Try an exact rational (109151/249696), a decimal prefix (-0.88009871),")
        w("a claim id (C2, G3, R14, U3), or a symbol (q_old, C_shape, h4_side).")
        w("For the corpus itself, add --corpus, or grep it directly.")
        return "\n".join(out)

    w(f"\033[1m{len(hits)} matching claims\033[0m")
    for hit in hits[:limit]:
        c = hit.claim
        tier = f"T{c.tier}" if c.tier is not None else "  "
        w(f"\n  \033[1m{c.id}\033[0m  \033[2m[{hit.how}]\033[0m")
        w(f"    {tier} {c.kind:<13} {c.statement}")
        if c.value:
            w(f"    value: {c.value}" + (f"  ({c.decimal!r})" if c.decimal is not None else ""))
        if c.status:
            w(f"    status: {c.status}" + (f" · {c.evidence}" if c.evidence else ""))
        if c.cites:
            w(f"    cites: {c.cites}")
        if c.detail:
            w(f"    {c.detail[:200]}")
        if c.reproduce:
            w(f"    \033[2m{c.reproduce}\033[0m")
    if len(hits) > limit:
        w(f"\n  … {len(hits) - limit} more (raise --limit)")

    if occurrences is not None and occurrences.files:
        shown = len(occurrences.files)
        distinct = "file" if shown == 1 else "files"
        w(
            f"\n\033[1mIn the corpus\033[0m — {occurrences.total_occurrences} occurrences "
            f"(prose and code), showing {shown} {distinct}. Repetition is not "
            "independence: count originating computations, not copies."
        )
        for path, count, line, text in occurrences.files:
            times = f"  (x{count})" if count > 1 else ""
            w(f"  {path}:{line}{times}")
            w(f"    \033[2m{text}\033[0m")
    elif occurrences is not None:
        w("\n\033[2mNo corpus occurrence of that exact value, in prose or code.\033[0m")

    return "\n".join(out)
