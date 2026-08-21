"""Static reading of the settlement package.

The package in ``settlement/`` is received evidence: two cold-rerun transcripts
and the frozen-protocol harness that would decide C2. The engine the harness
drives is not in this repository, so nothing here executes it. Everything below
is static analysis of the received text.

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
