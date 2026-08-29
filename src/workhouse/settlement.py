"""Static reading of the settlement package, and location of its engine.

The package in ``settlement/`` is received evidence: two cold-rerun transcripts
and the frozen-protocol harness that would decide C2. The package's own README
records the engine it drives as absent from this repository. That record is
stale: the corpus-import rename manifest shows
``programs/hodge_o4_adjudication/src/Hodge_SU3_Exact_MarkedCluster_m4_Colab.py``
was renamed to ``DATA_SU3_Exact_MarkedCluster_m4_Colab.py`` during the
2026-08-20 import, so the engine has been in ``corpus-import/`` all along under
the import pipeline's prefix convention. The functions below locate it, chain
its provenance, and scan it; the received package itself is never edited.

The harness's central claim is that the engine is *target-blind* — that no
comparison target reaches the process that computes the answer. It enforces
this with a substring scan of the engine source against a list of forbidden
digit strings. Whether that list actually covers the harness's own quarantined
targets is a checkable property, and it is the thing most worth checking: a
scan that reports PASS while a scalar-determining constant sits unnoticed is
worse than no scan, because it converts an unknown into a false assurance.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

SETTLEMENT_DIR = Path(__file__).resolve().parents[2] / "settlement"
HARNESS = SETTLEMENT_DIR / "mce_adjudication_harness.py"

_REPO = Path(__file__).resolve().parents[2]

#: The marked-cluster engine, present in corpus-import under the import
#: pipeline's rename (the harness expects the pre-rename filename).
ENGINE = (
    _REPO
    / "corpus-import/programs/hodge_o4_adjudication/src"
    / "DATA_SU3_Exact_MarkedCluster_m4_Colab.py"
)
ENGINE_PRE_RENAME = "Hodge_SU3_Exact_MarkedCluster_m4_Colab.py"
RENAME_MANIFEST = _REPO / "corpus-import/records/RENAME_MANIFEST_2026-08-20.tsv"

#: Digit strings the harness's own scan misses (the FINDING in invariants/):
#: m_Gamma = q_band + Delta_Gamma exactly and Hamer's 8*a_4 is the scalar to 13
#: digits, so an engine carrying any of these is seeded with the answer even
#: though the harness scan passes it. Both roundings of Hamer's value are here.
EXTENDED_CONTAMINATION_STRINGS = (
    "0827701250956414",  # Delta_Gamma as printed
    "2082770125095641",  # Delta_Gamma with its integer part
    "7751458630184",  # Hamer 8*a_4 as printed
    "7751458630417",  # Hamer 8*a_4 correctly rounded
    "160506019419340168451",  # quarantined shortcut numerator
    "7250590288602460800",  # q_old denominator
    "4405310420659200",  # C_old denominator
)

#: Targets from which the disputed Gamma-point scalar can be recovered exactly.
#: m_Gamma = q_band + Delta_Gamma, and Hamer's 8*a_4 IS the scalar to 13 digits,
#: so an engine carrying either is seeded with the answer it must reconstruct.
SCALAR_DETERMINING = frozenset({"m_gamma_run15", "hamer_8a4", "delta_gamma"})

#: Sealed-core values both kernels agree on. Their presence is not a blindness
#: breach in the same sense, and their decimal forms are too generic to scan.
SEALED_CORE_TARGETS = frozenset({"A_target", "alpha_target"})


@dataclass(frozen=True)
class ScanAudit:
    targets: dict[str, object]
    strings: list[str]
    covered: frozenset[str]
    uncovered: frozenset[str]

    @property
    def uncovered_scalar_determining(self) -> frozenset[str]:
        return self.uncovered & SCALAR_DETERMINING


def _digit_forms(value) -> set[str]:
    """Literal digit strings an engine would plausibly contain for this value.

    Short forms are dropped: "5/48" as 5 and 48 would match any source text.
    """
    forms: set[str] = set()
    if isinstance(value, Fraction):
        forms.add(str(abs(value.numerator)))
        forms.add(str(abs(value.denominator)))
        forms.add(repr(float(value)).lstrip("-").replace(".", ""))
    else:
        forms.add(repr(abs(float(value))).replace(".", ""))
    return {f for f in forms if len(f) >= 10}


def audit_contamination_scan(path: Path | None = None) -> ScanAudit:
    """Does the harness's own scan list cover the harness's own quarantine list?"""
    src = (path or HARNESS).read_text()
    namespace: dict[str, object] = {"Fraction": Fraction}
    q_block = re.search(r"^Q = \{.*?^\}", src, re.S | re.M)
    c_block = re.search(r"^CONTAMINATION_STRINGS = \[.*?^\]", src, re.S | re.M)
    if not q_block or not c_block:
        raise ValueError("harness source does not expose Q / CONTAMINATION_STRINGS")
    exec(q_block.group(0), namespace)  # noqa: S102 - reading our own vendored literal
    exec(c_block.group(0), namespace)  # noqa: S102
    targets = namespace["Q"]
    strings = namespace["CONTAMINATION_STRINGS"]

    covered, uncovered = set(), set()
    for name, value in targets.items():
        forms = _digit_forms(value)
        if any(any(c in form for c in strings) for form in forms):
            covered.add(name)
        else:
            uncovered.add(name)
    return ScanAudit(dict(targets), list(strings), frozenset(covered), frozenset(uncovered))


def scans_a_single_file(path: Path | None = None) -> bool:
    """True when the contamination scan reads only the engine file itself.

    An engine that imports a helper module, loads a data file, or restores from
    the sqlite checkpoint carries that content past a single-file scan.
    """
    src = (path or HARNESS).read_text()
    return bool(re.search(r"src = open\(engine[^)]*\)\.read\(\)", src))


def verdict_can_be_complete(path: Path | None = None) -> bool:
    """True when some certificate could make the harness report COMPLETE.

    Protocol item 10 (the W22 order-schedule toggle) is assigned an ``OPEN``
    string unconditionally, and the completeness predicate rejects any ``OPEN``
    value, so the COMPLETE branch is unreachable until the engine exposes the
    toggle. Reporting PARTIAL forever is honest; it is not the same as being
    able to discharge the protocol.
    """
    src = (path or HARNESS).read_text()
    unconditional_open = bool(
        re.search(r'verdict\["protocol"\]\["item10_W22_toggle"\] = "OPEN', src)
    )
    rejects_open = 'startswith("OPEN")' in src or "startswith('OPEN')" in src
    return not (unconditional_open and rejects_open)


def harness_delta_gamma(path: Path | None = None) -> float:
    src = (path or HARNESS).read_text()
    return float(re.search(r'"delta_gamma": ([0-9.]+)', src).group(1))


@dataclass(frozen=True)
class EngineRename:
    source: str
    destination: str
    size: int


def engine_rename_record(path: Path | None = None) -> EngineRename | None:
    """The corpus-import rename manifest row that maps the harness's expected
    engine filename onto the file actually on disk."""
    manifest = path or RENAME_MANIFEST
    for line in manifest.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) >= 4 and parts[0].endswith(ENGINE_PRE_RENAME):
            return EngineRename(parts[0], parts[1], int(parts[2]))
    return None


def engine_scan_hits(extended: bool = True) -> list[str]:
    """Target digit strings present in the engine source: harness list plus,
    when ``extended``, the strings the harness's own scan misses."""
    audit = audit_contamination_scan()
    strings = list(audit.strings)
    if extended:
        strings += [s for s in EXTENDED_CONTAMINATION_STRINGS if s not in strings]
    src = ENGINE.read_text(errors="ignore")
    return [s for s in strings if s in src]


#: Everything the engine imports is stdlib; sympy is optional and vendored by
#: the runtime. A single-file engine with no third-party or sibling imports is
#: exactly the case where the harness's single-file scan is sufficient.
ENGINE_ALLOWED_IMPORTS = frozenset(
    {
        "__future__",
        "argparse",
        "base64",
        "collections",
        "dataclasses",
        "enum",
        "errno",
        "fractions",
        "functools",
        "gzip",
        "hashlib",
        "hmac",
        "itertools",
        "json",
        "os",
        "pathlib",
        "secrets",
        "shutil",
        "sqlite3",
        "stat",
        "sys",
        "tempfile",
        "time",
        "tracemalloc",
        "types",
        "typing",
        "sympy",
    }
)


def engine_import_roots() -> frozenset[str]:
    src = ENGINE.read_text(errors="ignore")
    names = re.findall(r"^(?:from|import)\s+([A-Za-z_][\w.]*)", src, re.M)
    return frozenset(name.split(".")[0] for name in names)


RUNS_DIR = _REPO / "runs" / "mce_freeze_and_first_run_2026-08-22"


def read_freeze() -> dict:
    """The vendored FREEZE.json from the 2026-08-22 in-repo freeze stage."""
    import json

    return json.loads((RUNS_DIR / "FREEZE.json").read_text())


def harness_preflight_pins() -> tuple[str, str]:
    """(AUTH_COVERAGE_SHA, EXPECT_PREFLIGHT_SHA) as pinned in the harness."""
    src = HARNESS.read_text()
    coverage = re.search(r'AUTH_COVERAGE_SHA = "([0-9a-f]{64})"', src)
    preflight = re.search(r'EXPECT_PREFLIGHT_SHA = "([0-9a-f]{64})"', src)
    if not coverage or not preflight:
        raise ValueError("harness no longer pins the preflight hashes")
    return coverage.group(1), preflight.group(1)


def first_run_probe() -> dict:
    """Measured closure demand from the diagnostic probe transcript.

    The probe (engine unmodified, module-global ``closure`` wrapped with a
    10^6 cap) was terminated at session budget before completing the full
    first-cluster evaluation; the measurement that matters — the first
    oversize orbit — was flushed to the transcript before termination.
    """
    text = (RUNS_DIR / "probe_console.log").read_text(errors="ignore")
    size = re.search(r"closure size (\d+) exceeds the shipped cap (\d+)", text)
    support = re.search(r"first support size (\d+)", text)
    if not size or not support:
        raise ValueError("probe transcript no longer carries the measurements")
    return {
        "max_measured_closure": int(size.group(1)),
        "cap_in_transcript": int(size.group(2)),
        "first_support_size": int(support.group(1)),
        "complete_cluster": "[PROBE] DONE" in text,
    }


def first_run_error() -> str:
    """The run-stage failure line from the vendored production log."""
    text = (RUNS_DIR / "harness_production.log").read_text(errors="ignore")
    m = re.search(r"^ExactEngineError: .*$", text, re.M)
    return m.group(0) if m else ""


def engine_closure_cap() -> int:
    """The shipped H0-closure BFS cap. The guard never truncates — it either
    returns the complete finite orbit or aborts the run — so the cap's only
    effect is operational: too small and the sweep cannot start."""
    src = ENGINE.read_text(errors="ignore")
    m = re.search(r"def closure\(seed_state: State, max_states: int = (\d+)\)", src)
    if not m:
        raise ValueError("engine no longer exposes the closure cap in its signature")
    return int(m.group(1))


@dataclass(frozen=True)
class ColdRun:
    name: str
    passed: int
    total: int
    verdict: str
    source_sha256: str


def read_cold_runs(directory: Path | None = None) -> list[ColdRun]:
    """Parse the gate tallies and verdicts out of the rerun transcripts.

    ``SOURCE_SHA256`` in these files hashes the *generating script*, which is
    not in this repository. It is not the hash of the transcript, and the two
    must never be conflated: ``settlement/SHA256SUMS`` pins the artifact.
    """
    out = []
    for path in sorted((directory or SETTLEMENT_DIR).glob("cold_rerun_*.txt")):
        text = path.read_text()
        tally = re.search(r"(\d+)/(\d+)\s+(?:gates|checks) pass", text)
        verdict = re.search(r"VERDICT:\s*(\S+)", text)
        sha = re.search(r"SOURCE_SHA256:\s*([0-9a-f]{64})", text)
        out.append(
            ColdRun(
                name=path.stem,
                passed=int(tally.group(1)) if tally else 0,
                total=int(tally.group(2)) if tally else 0,
                verdict=verdict.group(1) if verdict else "",
                source_sha256=sha.group(1) if sha else "",
            )
        )
    return out
