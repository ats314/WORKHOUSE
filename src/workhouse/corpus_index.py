"""Extend the corpus constants index to code, certificates and notebooks.

`corpus-import/export/index/ENGINE_GOV_build_constants_index.py` states the
retrieval principle exactly right:

    The join keys of this corpus are exact rationals, not concepts. No semantic
    search will ever retrieve those from a natural-language query, so an exact
    index is the primary retrieval surface.

It then scans `.md` and `.tex` only — 322 of 928 files. The other 606 are the
engines, certificates, notebooks and data tables, and they carry the same
rationals: `5/48` alone appears in 73 of them.

It also applies a magnitude floor (`MIN_MAG = 1000`, and a slash pattern
requiring four digits on both sides), which makes the *sealed core* invisible:
`5/48`, `5/12`, `5/612`, `11/306`, `7/102` have no index entry at all. Those are
the values both disputed fourth-order kernels agree on — the most load-bearing
numbers in the program.

This module closes both gaps. It does not replace the prose engine; it covers
what that engine skips, and cross-references the two so a constant can be traced
from an authority document into the code that consumes it — or, more usefully,
found sitting in code with no authority vouching for it at all.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

CORPUS_DIR = Path(__file__).resolve().parents[2] / "corpus-import"

#: What the prose engine scans, and therefore what this one must not duplicate.
PROSE_EXTS = {".md", ".tex"}
#: What it skips. These are the engines, certificates, notebooks and tables.
CODE_EXTS = {".py", ".json", ".ipynb", ".txt", ".csv", ".tsv", ".yaml", ".yml"}

SKIP_DIRS = {"archive", "__pycache__", ".git", "GITHUB", ".venv", "node_modules"}
MAX_BYTES = 12 * 1024 * 1024

#: A rational written with at least this many total digits is distinctive on its
#: own. Below it, numerator and denominator must both be present as a pair —
#: "612" alone is noise, "5/612" is t_3.
SELF_EVIDENT_DIGITS = 8

#: Exact rationals written as `a/b`, `Fraction(a, b)`, or `\frac{a}{b}`.
PATTERNS = (
    re.compile(r"(?<![\w.])(-?\d{1,30})\s*/\s*(\d{1,30})(?![\w.])"),
    re.compile(r"Fraction\(\s*(-?\d{1,30})\s*,\s*(\d{1,30})\s*\)"),
    re.compile(r"\\[dt]?frac\{\s*(-?\d{1,30})\s*\}\{\s*(-?\d{1,30})\s*\}"),
)

#: Denominators this small are almost always array indices or dates, not corpus
#: constants. Kept deliberately low so the sealed core (denominator 12, 48)
#: survives; the pair requirement does the real filtering.
MIN_DENOMINATOR = 8


@dataclass
class Occurrence:
    path: Path
    line: int
    raw: str
    #: The whole source line. Symbol attribution needs the context around the
    #: match, not just the matched digits.
    text: str = ""


@dataclass
class ConstantRecord:
    value: Fraction
    occurrences: list[Occurrence] = field(default_factory=list)

    @property
    def files(self) -> set[Path]:
        return {o.path for o in self.occurrences}

    @property
    def as_ratio(self) -> str:
        return f"{self.value.numerator}/{self.value.denominator}"


def _iter_files(root: Path, exts: set[str]):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in exts:
            continue
        try:
            if path.stat().st_size > MAX_BYTES:
                continue
        except OSError:
            continue
        yield path


def _extract(text: str, path: Path) -> list[tuple[Fraction, Occurrence]]:
    found: list[tuple[Fraction, Occurrence]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for pattern in PATTERNS:
            for m in pattern.finditer(line):
                try:
                    num, den = int(m.group(1)), int(m.group(2))
                except ValueError:
                    continue
                if den == 0 or abs(den) < MIN_DENOMINATOR:
                    continue
                digits = len(str(abs(num))) + len(str(abs(den)))
                if digits < SELF_EVIDENT_DIGITS and abs(num) > 999:
                    # A long numerator over a short denominator is likely a
                    # timestamp or an id, not a corpus rational.
                    continue
                found.append(
                    (
                        Fraction(num, den),
                        Occurrence(path, lineno, m.group(0), line[:400]),
                    )
                )
    return found


def scan(root: Path | None = None, exts: set[str] | None = None) -> dict[Fraction, ConstantRecord]:
    """Index every exact rational in the given file classes. Read-only."""
    root = root or CORPUS_DIR
    table: dict[Fraction, ConstantRecord] = {}
    for path in _iter_files(root, exts or CODE_EXTS):
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        if path.suffix.lower() == ".ipynb":
            try:  # notebooks: index the source cells, not the base64 outputs
                nb = json.loads(text)
                text = "\n".join("".join(c.get("source", [])) for c in nb.get("cells", []))
            except Exception:
                pass
        for value, occ in _extract(text, path):
            rec = table.setdefault(value, ConstantRecord(value))
            rec.occurrences.append(occ)
    return table


def scan_cached(
    root: Path | None = None, exts: set[str] | None = None
) -> dict[Fraction, ConstantRecord]:
    """`scan`, memoised on disk across invocations.

    The corpus is pinned and effectively immutable, so one full build (a few
    seconds over 928 files) can be amortised across a whole session of
    `workhouse search --corpus` calls. The key is a fingerprint over the file
    list, sizes, and mtimes; any corpus change silently misses and rebuilds.
    The cache lives outside the repository so it can never dirty the tree.
    """
    import hashlib
    import os
    import pickle
    import tempfile

    root = root or CORPUS_DIR
    exts = exts if exts is not None else (CODE_EXTS | PROSE_EXTS)
    files = sorted(_iter_files(root, exts))
    hasher = hashlib.sha256()
    for path in files:
        try:
            st = path.stat()
        except OSError:
            continue
        hasher.update(f"{path}|{st.st_size}|{st.st_mtime_ns}\n".encode())
    cache_dir = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "workhouse"
    cache = cache_dir / f"corpus-scan-{hasher.hexdigest()[:24]}.pkl"
    if cache.exists():
        try:
            return pickle.loads(cache.read_bytes())
        except Exception:
            pass  # corrupt cache: rebuild below
    table = scan(root, exts)
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=cache_dir, delete=False) as tmp:
            tmp.write(pickle.dumps(table))
        Path(tmp.name).replace(cache)
    except OSError:
        pass  # caching is a convenience, never a requirement
    return table


def unvouched(code_table, prose_table, min_files: int = 2) -> list[ConstantRecord]:
    """Constants that live in code but that no prose file carries.

    A value consumed by an engine and never stated in a document is exactly the
    drift class this corpus has a documented history of: nothing in the
    authority stack vouches for it, and no reader would find it.
    """
    return sorted(
        (
            rec
            for value, rec in code_table.items()
            if value not in prose_table and len(rec.files) >= min_files
        ),
        key=lambda r: (-len(r.files), str(r.value)),
    )


def sealed_core_locations(code_table, prose_table) -> dict[str, dict[str, int]]:
    """Where the sealed core actually lives — the rows the prose index omits."""
    core = {
        "A_shp = 5/48": Fraction(5, 48),
        "alpha_pen = 5/12": Fraction(5, 12),
        "t_3 = 5/612": Fraction(5, 612),
        "E_flat u^2 = 11/306": Fraction(11, 306),
        "d_minus_2 = 7/102": Fraction(7, 102),
    }
    out = {}
    for label, value in core.items():
        out[label] = {
            "code_files": len(code_table[value].files) if value in code_table else 0,
            "prose_files": len(prose_table[value].files) if value in prose_table else 0,
        }
    return out


def coverage(root: Path | None = None) -> dict[str, int]:
    root = root or CORPUS_DIR
    prose = sum(1 for _ in _iter_files(root, PROSE_EXTS))
    code = sum(1 for _ in _iter_files(root, CODE_EXTS))
    return {"prose_files": prose, "code_files": code, "total": prose + code}


#: Ratios simple enough that a match means a convention factor, not coincidence.
SIMPLE_RATIOS = frozenset(Fraction(n, d) for n in range(1, 17) for d in range(1, 17)) - {
    Fraction(1)
}


@dataclass(frozen=True)
class MultipleFinding:
    code_value: Fraction
    prose_value: Fraction
    ratio: Fraction
    code_files: int
    code_occurrences: int
    prose_files: int
    example: Path

    def __str__(self) -> str:
        return (
            f"{self.code_value.numerator}/{self.code_value.denominator} "
            f"= {self.ratio} x {self.prose_value.numerator}/{self.prose_value.denominator}"
        )


def rational_multiples(code_table, prose_table, min_digits: int = 12, min_files: int = 2):
    """Unvouched code constants that are simple rational multiples of vouched ones.

    This is the hazard class `CERT_GOV_constant_ratio_classifications.json`
    exists for — it already records three legitimate convention factors and one
    live symbol collision, with the standing warning that "neither document is
    wrong; anyone quoting across them will be". That classifier is prose-only,
    so a convention factor living in an engine or a certificate is invisible to
    it. This finds those.

    A hit is not a defect. It is an undocumented factor: either a convention
    that belongs in the classifier, or a transcription that does not.
    """
    vouched = {v: r for v, r in prose_table.items() if len(r.files) >= min_files}
    out: list[MultipleFinding] = []
    for rec in unvouched(code_table, prose_table, min_files=min_files):
        digits = len(str(abs(rec.value.numerator))) + len(str(rec.value.denominator))
        if digits < min_digits or rec.value == 0:
            continue
        for vval, vrec in vouched.items():
            if vval == 0:
                continue
            ratio = rec.value / vval
            if abs(ratio) in SIMPLE_RATIOS:
                out.append(
                    MultipleFinding(
                        code_value=rec.value,
                        prose_value=vval,
                        ratio=ratio,
                        code_files=len(rec.files),
                        code_occurrences=len(rec.occurrences),
                        prose_files=len(vrec.files),
                        example=sorted(rec.files)[0],
                    )
                )
                break
    return sorted(out, key=lambda f: (-f.code_occurrences, str(f.code_value)))


def classifier_entries(path: Path | None = None) -> set[str]:
    """Ratio pairs the corpus classifier already documents."""
    path = path or (
        CORPUS_DIR / "export" / "index" / "CERT_GOV_constant_ratio_classifications.json"
    )
    if not path.exists():
        return set()
    return set(json.loads(path.read_text()))
