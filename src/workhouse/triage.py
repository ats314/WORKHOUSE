"""Survey an unpinned archive against what the repository already knows.

A large theory archive is mostly noise: superseded drafts, re-exports, near
copies. The signal is narrow and specific — which files carry the disputed
fourth-order coefficients, which carry the coupling erratum, and which are
byte-identical to something already pinned.

This module answers those questions and nothing else. It never copies, moves,
promotes, or edits anything. Deciding what belongs in ``theory/`` stays a
human judgement; this only shortens the list you have to judge.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from sympy import Rational

from . import constants as K
from . import settlement as S

#: Files larger than this are hashed but not scanned for content.
MAX_SCAN_BYTES = 8 * 1024 * 1024
TEXTLIKE = {".md", ".txt", ".tex", ".py", ".json", ".csv", ".yaml", ".yml", ".org", ".rst"}

#: A digit string this long is distinctive on its own. Shorter ones (612, 48)
#: would fire on any document.
MIN_SIGNATURE_DIGITS = 8


def _signatures() -> dict[str, list[list[str]]]:
    """Digit patterns identifying each coefficient, drawn from the registry.

    Each label maps to a list of alternatives; an alternative matches when ALL
    of its parts are present. A long numerator stands alone, but a short
    numerator and denominator must co-occur — "249696" by itself is noise,
    while "109151" together with it is d_3 and nothing else.
    """
    named: dict[str, object] = {
        "q_band^(4)": K.Q_BAND_4,
        "C_shp historical": K.C_SHP_HISTORICAL,
        "beta_pen_3": K.BETA_PEN_3,
        "Q4 cross": K.Q4_CROSS,
        "quarantined scalar": K.QUARANTINED_SCALAR,
        "Delta_q_3": K.DELTA_Q_3,
        "d_3": K.D_3,
        "b_3": K.B_3,
        "leak_3": K.LEAK_3,
        "linked vacuum": K.LINKED_VACUUM_4,
        "m_Gamma^(4)": K.M_GAMMA_4_NUM,
        "C_shp v10a.26": K.C_SHP_NEW_NUM,
        "Hamer a_4": K.HAMER_A4_NUM,
        "Delta_Gamma": K.DELTA_GAMMA_AS_PRINTED_NUM,
    }
    out: dict[str, list[list[str]]] = {}
    for label, value in named.items():
        alternatives: list[list[str]] = []
        if isinstance(value, Rational):
            num, den = str(abs(value.p)), str(abs(value.q))
            long_forms = [f for f in (num, den) if len(f) >= MIN_SIGNATURE_DIGITS]
            if long_forms:
                alternatives.extend([f] for f in long_forms)
            else:
                alternatives.append([num, den])  # both, or it is noise
        else:
            digits = repr(abs(float(value))).replace(".", "").rstrip("0")
            if len(digits) >= MIN_SIGNATURE_DIGITS:
                alternatives.append([digits])
        if alternatives:
            out[label] = alternatives
    return out


SIGNATURES = _signatures()

#: The Y = 2*beta/3 = 4u definition-label erratum (C4). Coefficients printed in
#: a file carrying this line were already in canonical u and must never be
#: rescaled by 4**r. Finding these files is the point of G2.
ERRATUM_PATTERNS = (
    re.compile(r"Y\s*[=:]\s*2\s*\\?beta[^=\n]{0,12}/\s*3"),
    re.compile(r"Y\s*[=:]\s*2\s*β\s*/\s*3"),
    re.compile(r"Y\s*[=:]\s*4\s*u\b"),
)

#: Filename cues that usually mark a file as not-controlling. Matched against a
#: name whose separators have been normalised to spaces: underscore is a word
#: character, so "\bold\b" would never fire on "GLUE_old_copy.md" — and
#: underscores are how most archives name things.
SUPERSEDED_HINTS = re.compile(
    r"\b(old|prev|previous|draft|backup|bak|copy|superseded|deprecated|obsolete|archive)\b",
    re.I,
)


def _normalise_name(name: str) -> str:
    return re.sub(r"[_\-.]+", " ", name)


DATE_IN_NAME = re.compile(r"(20\d{2})[-_]?(\d{2})[-_]?(\d{2})")


@dataclass
class FileReport:
    path: Path
    size: int
    sha256: str
    duplicate_of: str | None = None
    coefficients: list[str] = field(default_factory=list)
    has_erratum: bool = False
    scanned: bool = False
    date_hint: str | None = None
    superseded_hint: bool = False

    @property
    def signal(self) -> int:
        """Rough ranking: coefficient-bearing files matter most."""
        return len(self.coefficients) * 10 + (5 if self.has_erratum else 0)


@dataclass
class Report:
    root: Path
    files: list[FileReport]

    @property
    def duplicates(self) -> list[FileReport]:
        return [f for f in self.files if f.duplicate_of]

    @property
    def coefficient_bearing(self) -> list[FileReport]:
        return sorted(
            (f for f in self.files if f.coefficients),
            key=lambda f: (-f.signal, str(f.path)),
        )

    @property
    def erratum_carriers(self) -> list[FileReport]:
        return [f for f in self.files if f.has_erratum]

    def coefficient_census(self) -> Counter:
        c: Counter = Counter()
        for f in self.files:
            c.update(f.coefficients)
        return c

    def internal_duplicate_groups(self) -> dict[str, list[FileReport]]:
        by_hash: dict[str, list[FileReport]] = {}
        for f in self.files:
            by_hash.setdefault(f.sha256, []).append(f)
        return {h: g for h, g in by_hash.items() if len(g) > 1}


def _pinned() -> dict[str, str]:
    """sha256 -> label, for everything the repository already pins."""
    out: dict[str, str] = {}
    root = Path(__file__).resolve().parents[2]
    for directory in (root / "theory", S.SETTLEMENT_DIR):
        if not directory.is_dir():
            continue
        # rglob, not iterdir: theory/superseded/ holds archived documents that
        # must still be recognised when an archive copy turns up.
        for path in directory.rglob("*"):
            if path.is_file() and path.name != "SHA256SUMS":
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                rel = path.relative_to(directory)
                out[digest] = f"{directory.name}/{rel.as_posix()}"
    return out


def scan(root: Path, max_scan_bytes: int = MAX_SCAN_BYTES) -> Report:
    """Walk ``root`` and report what each file carries. Read-only throughout."""
    root = Path(root).expanduser().resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)
    pinned = _pinned()
    reports: list[FileReport] = []

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in {".git", "node_modules", "__pycache__", ".venv"} for part in path.parts):
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        digest = hashlib.sha256(data).hexdigest()
        rel = path.relative_to(root)
        rep = FileReport(path=rel, size=len(data), sha256=digest, duplicate_of=pinned.get(digest))

        date = DATE_IN_NAME.search(path.name)
        rep.date_hint = "-".join(date.groups()) if date else None
        rep.superseded_hint = bool(SUPERSEDED_HINTS.search(_normalise_name(path.name)))

        if path.suffix.lower() in TEXTLIKE and len(data) <= max_scan_bytes:
            try:
                text = data.decode("utf-8", errors="ignore")
            except Exception:
                text = ""
            rep.scanned = True
            digits = re.sub(r"[^\d]", "", text)
            for label, alternatives in SIGNATURES.items():
                if any(all(part in digits for part in alt) for alt in alternatives):
                    rep.coefficients.append(label)
            rep.has_erratum = any(p.search(text) for p in ERRATUM_PATTERNS)
        reports.append(rep)

    return Report(root=root, files=reports)


def format_report(report: Report, limit: int = 25) -> str:
    """Human-readable summary, ordered by what actually needs a decision."""
    lines: list[str] = []
    add = lines.append
    total = len(report.files)
    scanned = sum(1 for f in report.files if f.scanned)
    add(f"Archive: {report.root}")
    add(f"{total} files, {scanned} scanned for content")
    add("")

    dups = report.duplicates
    add(f"ALREADY PINNED ({len(dups)}) — byte-identical to a repository artifact")
    for f in dups[:limit]:
        add(f"  {f.path}  ==  {f.duplicate_of}")
    if not dups:
        add("  none")
    add("")

    groups = report.internal_duplicate_groups()
    add(f"DUPLICATED WITHIN THE ARCHIVE ({len(groups)} groups)")
    for _digest, group in list(groups.items())[:limit]:
        add(f"  {len(group)}x  " + "  |  ".join(str(f.path) for f in group[:4]))
    if not groups:
        add("  none")
    add("")

    bearing = report.coefficient_bearing
    add(f"COEFFICIENT-BEARING ({len(bearing)}) — ranked by how much they carry")
    for f in bearing[:limit]:
        flags = " [ERRATUM]" if f.has_erratum else ""
        flags += " [name suggests superseded]" if f.superseded_hint else ""
        flags += f" [{f.date_hint}]" if f.date_hint else ""
        flags += f" [== {f.duplicate_of}]" if f.duplicate_of else ""
        add(f"  {f.path}{flags}")
        add(f"      {', '.join(f.coefficients)}")
    if not bearing:
        add("  none")
    add("")

    census = report.coefficient_census()
    add("COEFFICIENT CENSUS — how many files carry each")
    for label, count in census.most_common():
        add(f"  {count:>4}  {label}")
    if not census:
        add("  none")
    add("")

    err = report.erratum_carriers
    add(f"COUPLING ERRATUM (C4) ({len(err)}) — coefficients here are ALREADY in u;")
    add("  never rescale them by 4**r")
    for f in err[:limit]:
        add(f"  {f.path}")
    if not err:
        add("  none")
    return "\n".join(lines)
