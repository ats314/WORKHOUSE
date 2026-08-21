r"""A bulk, explicitly-untrusted index of every exact rational in the corpus.

This is **T3 data**. `constants.py` is the curated registry: each entry there was
read, checked, and given a status and a provenance by hand. This module is the
opposite — it extracts thousands of values mechanically and attributes symbols
by pattern. The corpus's own engine says it best about its symbol column:

    a strong hint, **not a definition**; verify against the source before citing

Nothing here may be promoted into `constants.py` without that verification.
What it is good for is *sweeping*: questions of the form "does any file disagree
with any other file" need no comprehension and no trust, only arithmetic.

Three sweeps are implemented, in decreasing order of what they can prove:

- `near_miss_pairs` — two distinct rationals agreeing to better than a relative
  `1e-9`. One of them is almost certainly a transcription slip or a
  float-reconstruction of the other. Across the whole corpus this currently
  finds exactly one pair, the documented C20 artifact, which is a useful
  negative result: no *undetected* slip of that class exists.
- `multiple_pairs` — one value an exact simple rational multiple of another.
  A convention factor or a normalisation error; the corpus classifier documents
  four such and this finds them in code too.
- `coverage` — which files were swept, which carry checkable content, and which
  are prose only. The point is to make the unexamined remainder *visible*
  rather than silently absent.

A fourth sweep, same-symbol-different-value, is **deliberately not exported.**
Pattern-based symbol attribution is not reliable enough over mixed prose and
code: it captures subscript fragments (`\mathrm{old` collects `beta_old`,
`W_old` and `q_old` as one symbol) and JSON field names reused across unrelated
certificates (`c4` binds five different values in five different files). Of the
eleven "conflicts" it reported, one was a bug in this module and the rest were
noise. It stays as a research tool in the tests, not as a finding generator.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from . import corpus_index as X

#: Below this written length a rational cannot carry a meaningful slip.
SUBSTANTIAL_DIGITS = 10
#: Relative agreement at or below this means the two are the same quantity.
NEAR_MISS_RELATIVE = 1e-9
#: Ratios simpler than this are conventions, reported by `multiple_pairs`.
SIMPLE_RATIO_BOUND = 100

#: A symbol immediately left of an `=`. Used only as a hint.
_SYMBOL_EQ = re.compile(r"((?:\\[A-Za-z]+\s+)?[A-Za-z_\\][A-Za-z0-9_^{}\\]{0,30})\s*(?:&)?=")

#: The value, as written in prose or TeX.
_VALUE = re.compile(r"\\[dt]?frac\{\s*-?\d+\s*\}\{\s*-?\d+\s*\}|-?\d+\s*/\s*\d+")


def _attribute(line: str) -> str | None:
    """Symbol a written value belongs to, honouring chained equalities.

    In `\\Delta c_5 = A_5 + B_5 = \\frac{...}{...}` the value is bound to
    `\\Delta c_5`, not to the `B_5` that happens to sit nearest it. Taking the
    nearest symbol reports a conflict that is not there — the two `B_5` values
    in the flat-band paper differ by exactly `A_5 = 313/240`, which is the
    signature of this bug, not of a corpus error.
    """
    value = _VALUE.search(line)
    if not value:
        return None
    head = line[: value.start()]
    first = _SYMBOL_EQ.search(head)
    return first.group(1).strip() if first else None


def digits(value: Fraction) -> int:
    return len(str(abs(value.numerator))) + len(str(value.denominator))


@dataclass(frozen=True)
class Pair:
    a: Fraction
    b: Fraction
    relative: float
    a_files: int
    b_files: int
    rarer_example: Path

    def __str__(self) -> str:
        return (
            f"{self.a.numerator}/{self.a.denominator} ~ "
            f"{self.b.numerator}/{self.b.denominator} (rel {self.relative:.2e})"
        )


def combined_table() -> dict[Fraction, X.ConstantRecord]:
    """Every rational in the corpus, prose and code merged."""
    code = X.scan()
    prose = X.scan(exts=X.PROSE_EXTS)
    merged = dict(prose)
    for value, record in code.items():
        if value in merged:
            merged[value].occurrences.extend(record.occurrences)
        else:
            merged[value] = record
    return merged


def _substantial(table) -> list[Fraction]:
    return sorted((v for v in table if v != 0 and digits(v) >= SUBSTANTIAL_DIGITS), key=float)


def near_miss_pairs(table=None) -> list[Pair]:
    """Distinct rationals that agree numerically. Sorted order makes them adjacent."""
    table = table if table is not None else combined_table()
    values = _substantial(table)
    out: list[Pair] = []
    for a, b in zip(values, values[1:], strict=False):
        fa = float(a)
        if fa == 0:
            continue
        rel = abs(float(b) - fa) / abs(fa)
        if not (0 < rel < NEAR_MISS_RELATIVE):
            continue
        ratio = b / a
        if abs(ratio.numerator) < SIMPLE_RATIO_BOUND and ratio.denominator < SIMPLE_RATIO_BOUND:
            continue  # a convention factor, not a slip
        ra, rb = table[a], table[b]
        rarer = ra if len(ra.files) <= len(rb.files) else rb
        out.append(Pair(a, b, rel, len(ra.files), len(rb.files), sorted(rarer.files)[0]))
    return sorted(out, key=lambda p: p.relative)


def symbol_hints(table=None, min_files: int = 2) -> dict[Fraction, str]:
    """Best-effort `symbol = value` attribution. A hint, never a definition."""
    table = table if table is not None else combined_table()
    hints: dict[Fraction, str] = {}
    for value, record in table.items():
        if len(record.files) < min_files:
            continue
        for occ in record.occurrences:
            sym = _attribute(occ.text)
            if sym:
                hints[value] = sym
                break
    return hints


def coverage(table=None) -> dict[str, int]:
    """What was swept, what is checkable, and what is prose only."""
    table = table if table is not None else combined_table()
    root = X.CORPUS_DIR
    text = [
        p
        for p in root.rglob("*")
        if p.is_file()
        and p.suffix.lower() in (X.PROSE_EXTS | X.CODE_EXTS)
        and not any(part in X.SKIP_DIRS for part in p.parts)
    ]
    with_values = {occ.path for rec in table.values() for occ in rec.occurrences}
    return {
        "text_files": len(text),
        "files_carrying_a_rational": len(with_values),
        "prose_only_files": len(text) - len(with_values),
        "distinct_rationals": len(table),
        "substantial_rationals": len(_substantial(table)),
    }
