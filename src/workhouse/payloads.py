"""G1: the record-backed payloads, located and machine-checked.

The ledger said five payload families were "only record-backed": documents
describe them, quote reference SHAs, and nothing in the tree could be checked.
A targeted sweep (2026-08-21) found that **three of the five are shipped**,
pinned in ``corpus-import/``, and carry the exact reference SHAs the records
quote — the "absent" claim was stale, inherited from the superseded master.
Two remain genuinely absent, and one of those provably cannot be *restored*
at all: no reference SHA for a tetrahedral certificate exists anywhere in the
corpus, so only the G5 re-derivation can ever close C15.

This module does the loading and exact re-derivation; the checks registered
in ``invariants/restored.py`` (suite ``restored payloads (G1)``) assert the
results.
Everything is exact ``Fraction`` arithmetic over pinned files; nothing here
writes, and nothing trusts a document's number without recomputing it.

The chain for the SU(3) kernel, all exact:

    189 records  ->  H(Gamma) = q I         with q  = q_band^(4)
                 ->  c_X - q               = 5/12  = alpha_pen(3)
                 ->  2(c_M - c_X)          = beta_pen_3
                 ->  c_R = 2 c_M - c_X       (the pencil relation, on data)
                 ->  (beta - 2 alpha)/16   = C_shp (historical)

so the historical kernel's headline constants are re-derived from the raw
payload, not quoted from prose.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
from fractions import Fraction
from functools import cache
from pathlib import Path

from sympy import Poly, Symbol, sympify

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "corpus-import"
CORPUS_MANIFEST = CORPUS / "SHA256SUMS"
CANONICAL_MANIFEST = ROOT / "theory" / "GLUEBALL_CANONICAL_SOURCE_MANIFEST_2026-08-20_v4_3.csv"

# -- the SU(3) 189-record kernel (UNIFIED §6; manifest row A20K) -------------

_SOS_PACKAGE = CORPUS / "numerics/scratch_tmp/y4_sos_repro/Y4_REAL_SPACE_SOS_PACKAGE"
_FLATBAND = CORPUS / "programs/one_plaquette/y4_o3_flatband_verification"
KERNEL = _FLATBAND / "DATA_Y4_full_real_space_h4_kernel.json.gz"
#: The two other shipped copies of the same kernel. Their records are
#: identical; their meta blocks name two *different* upstream Stage-3I hashes,
#: which is what makes the copies independent builds rather than one paste.
KERNEL_COPIES = (
    KERNEL,
    _SOS_PACKAGE / "DATA_Y4_full_real_space_h4_kernel.json.gz",
    _FLATBAND / "y4_full_real_space_H4_kernel.json/CERT_Y4_full_real_space_h4_kernel.json",
)
#: File-level reference SHA: quoted by CERT_Y4_stage3j_verdict.json and by
#: canonical manifest row A20K (which stores it uppercase).
KERNEL_FILE_SHA = "635d40fa8a5d7da841fd30f36185eb96f14ec4c040678ddd8fb010379afb2900"
#: Semantic reference SHA: sha256 of the canonical sorted-record JSON dump,
#: quoted machine-readably by CERT_Y4_real_space_sos_certificate.json.
KERNEL_SEMANTIC_SHA = "48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77"
SOS_CERT = _SOS_PACKAGE / "CERT_Y4_real_space_sos_certificate.json"
STAGE3J_VERDICT = _FLATBAND / "CERT_Y4_stage3j_verdict.json"

_PLANES = ((0, 1), (0, 2), (1, 2))


def _load_json(path: Path):
    raw = path.read_bytes()
    if path.suffix == ".gz":
        raw = gzip.decompress(raw)
    return json.loads(raw)


@cache
def kernel_records(path: Path = KERNEL) -> tuple:
    """The kernel as an immutable record tuple: ((ip, op, d), weight)."""
    obj = _load_json(path)
    return tuple(
        (
            (tuple(r["input_plane"]), tuple(r["output_plane"]), tuple(r["displacement"])),
            Fraction(r["weight"]),
        )
        for r in obj["kernel"]
    )


def semantic_sha(path: Path = KERNEL) -> str:
    obj = _load_json(path)
    dump = json.dumps(obj["kernel"], sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(dump.encode()).hexdigest()


def symbol_at(parity: tuple[int, int, int], path: Path = KERNEL) -> list[list[Fraction]]:
    """The 3x3 plane-basis symbol at a parity point (k_i in {0, pi})."""
    idx = {pl: i for i, pl in enumerate(_PLANES)}
    s_matrix = [[Fraction(0)] * 3 for _ in range(3)]
    for (ip, op, d), w in kernel_records(path):
        sign = 1 - 2 * (sum(p * di for p, di in zip(parity, d, strict=True)) % 2)
        s_matrix[idx[op]][idx[ip]] += sign * w
    return s_matrix


def rayleigh(parity: tuple[int, int, int], path: Path = KERNEL) -> Fraction:
    """Carrier Rayleigh quotient at a parity point: psi = (d3bar, -d2bar, d1bar)."""
    d = [(-2 if p else 0) for p in parity]
    psi = [d[2], -d[1], d[0]]
    norm = sum(x * x for x in psi)
    s_matrix = symbol_at(parity, path)
    return sum(psi[i] * s_matrix[i][j] * psi[j] for i in range(3) for j in range(3)) / norm


@cache
def kernel_constants() -> dict[str, Fraction]:
    """q, alpha, beta, C_shp, bandwidth, and the parity-point corrections."""
    gamma = symbol_at((0, 0, 0))
    q = gamma[0][0]
    c_x = rayleigh((1, 0, 0))
    c_m = rayleigh((1, 1, 0))
    c_r = rayleigh((1, 1, 1))
    alpha = c_x - q
    beta = 2 * (c_m - c_x)
    return {
        "q": q,
        "alpha": alpha,
        "beta": beta,
        "C_shp": (beta - 2 * alpha) / 16,
        "bandwidth": alpha + beta,
        "c_X": c_x,
        "c_M": c_m,
        "c_R": c_r,
        "gamma_is_scalar": Fraction(
            int(
                gamma[0][0] == gamma[1][1] == gamma[2][2]
                and all(gamma[i][j] == 0 for i in range(3) for j in range(3) if i != j)
            )
        ),
    }


def kernel_is_hermitian(path: Path = KERNEL) -> bool:
    recs = dict(kernel_records(path))
    return all(recs.get((op, ip, tuple(-x for x in d))) == w for (ip, op, d), w in recs.items())


def stage3i_hashes() -> set[str]:
    """The upstream Stage-3I input hashes across the three shipped copies."""
    return {str(_load_json(p)["meta"]["stage3i_sha256"]) for p in KERNEL_COPIES}


# -- the Q_32 and P_402 Newton ledgers (UNIFIED §8) --------------------------

SUN_DIR = CORPUS / "programs/one_plaquette/sun_band_shape"
WALLED_BRAUER = SUN_DIR / "CERT_Y4_sun_walled_brauer_full_symbolic_certificate_2026-06-14.json"
Q_NOTE = SUN_DIR / "NOTE_Y4_sun_q_compact_z_formula.txt"
B_NOTE = SUN_DIR / "NOTE_Y4_sun_b_structured_expression.txt"
Q_LEDGER = CORPUS / "numerics/certificates/CERT_MISC_q_numerator_newton_coefficients.json"
B_LEDGER = CORPUS / "numerics/certificates/CERT_MISC_b_newton_coefficients.json"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def forward_differences(values: list[int]) -> list[int]:
    out = []
    current = list(values)
    for _ in range(len(values)):
        out.append(current[0])
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
    return out


@cache
def q_polynomials():
    """Q32 and D34 from the compact-formula note, as sympy polynomials in z."""
    z = Symbol("z")
    lines = Q_NOTE.read_text().splitlines()
    q32 = sympify(next(line for line in lines if line.startswith("Q32(z) =")).split("=", 1)[1])
    d34 = sympify(next(line for line in lines if line.startswith("D34(z) =")).split("=", 1)[1])
    return z, Poly(q32, z), d34


def _eval_fraction(compiled, n: int) -> Fraction:
    return eval(compiled, {"__builtins__": {}}, {"N": Fraction(n)})  # noqa: S307


@cache
def b_evaluator():
    """The structured B_N expression compiled for exact Fraction evaluation.

    The note is a single Python-syntax arithmetic expression over N (pinned,
    immutable, hash-bound to the walled-Brauer certificate); settlement.py set
    the precedent of executing literals extracted from pinned artifacts.
    """
    return compile(B_NOTE.read_text().strip(), str(B_NOTE), "eval")


@cache
def d409_evaluator():
    cert = _load_json(WALLED_BRAUER)
    factors = tuple(
        (compile(f["factor"], "<factor>", "eval"), int(f["exponent"]))
        for f in cert["B"]["denominator_factors"]
    )

    def evaluate(n: int) -> Fraction:
        out = Fraction(1)
        for code, exponent in factors:
            out *= _eval_fraction(code, n) ** exponent
        return out

    return evaluate


def no_real_root_at_or_above(expr, symbol, bound: int) -> bool:
    """True when a polynomial has no real root >= bound (exact, via sympy)."""
    roots = Poly(expr, symbol).real_roots()
    return all(root < bound for root in roots)


# -- the SU(5)/SU(6) exceptional certificates (GCSG, Aug 8; C16) -------------

SU6_CERT = CORPUS / "numerics/certificates/CERT_SU6_determinant_certificate.json"
STAGE1_CERT = CORPUS / "programs/y4_allrank/data/CERT_Y4_sun_stable_stage1_summary.json"


# -- manifests: what is pinned, what is promised, what is absent -------------


@cache
def corpus_pins() -> dict[str, str]:
    pins = {}
    for line in CORPUS_MANIFEST.read_text().splitlines():
        parts = line.split("  ", 1)
        if len(parts) == 2:
            pins[parts[1]] = parts[0]
    return pins


@cache
def canonical_rows() -> dict[str, dict[str, str]]:
    """The theory-side canonical source manifest, keyed by row id (A20K, A60...)."""
    rows = {}
    with CANONICAL_MANIFEST.open() as fh:
        for row in csv.reader(fh):
            if row and row[0] and row[0] != "id":
                rows[row[0]] = {
                    "path": row[3] if len(row) > 3 else "",
                    "description": row[4] if len(row) > 4 else "",
                    "size": row[6] if len(row) > 6 else "",
                    "sha256": (row[7] if len(row) > 7 else "").lower(),
                }
    return rows


def pinned_paths_matching(pattern: str) -> list[str]:
    rx = re.compile(pattern, re.IGNORECASE)
    return sorted(p for p in corpus_pins() if rx.search(p))


def as_fraction(value) -> Fraction:
    """A sympy Rational as an exact Fraction, so the two never mix silently."""
    return Fraction(int(value.p), int(value.q))


@cache
def walled_brauer() -> dict:
    return _load_json(WALLED_BRAUER)


@cache
def su6() -> dict:
    return _load_json(SU6_CERT)


@cache
def stage1() -> dict:
    return _load_json(STAGE1_CERT)


@cache
def q32_verification() -> dict:
    """The Q_32 ledger against the compact formula: exact, cached once."""
    ledger = _load_json(Q_LEDGER)
    coefficients = [int(c) for c in ledger["coefficients"]]
    base = int(ledger["base"])
    z, q32, _d34 = q_polynomials()
    values = [int(q32.eval(base + j)) for j in range(len(coefficients))]
    return {
        "matches": forward_differences(values) == coefficients,
        "count": len(coefficients),
        "positive": sum(1 for c in coefficients if c > 0),
        "zero": sum(1 for c in coefficients if c == 0),
        "negative": sum(1 for c in coefficients if c < 0),
        "base": base,
        "ledger_sha": sha256_of(Q_LEDGER),
        "note_sha": sha256_of(Q_NOTE),
    }


@cache
def p402_verification() -> dict:
    """The P_402 ledger against B_N * D_409(N): exact, cached once."""
    ledger = _load_json(B_LEDGER)
    coefficients = [int(c) for c in ledger["coefficients"]]
    base = int(ledger["base"])
    b_code = b_evaluator()
    d409 = d409_evaluator()
    values = []
    for j in range(len(coefficients)):
        product = _eval_fraction(b_code, base + j) * d409(base + j)
        if product.denominator != 1:
            return {"matches": False, "count": len(coefficients)}
        values.append(product.numerator)
    return {
        "matches": forward_differences(values) == coefficients,
        "count": len(coefficients),
        "positive": sum(1 for c in coefficients if c > 0),
        "zero": sum(1 for c in coefficients if c == 0),
        "negative": sum(1 for c in coefficients if c < 0),
        "last_nonzero": max(j for j, c in enumerate(coefficients) if c != 0),
        "base": base,
        "ledger_sha": sha256_of(B_LEDGER),
        "note_sha": sha256_of(B_NOTE),
    }


@cache
def denominator_sign_certificate() -> dict:
    """No D34 factor has a real root at z >= 49; no D409 factor at N >= 7.

    With every leading coefficient positive this fixes the denominators'
    sign for every integer N >= 7, which is what turns the ledgers' Newton
    nonnegativity into sign statements for the whole stable range.
    """
    z, _q32, d34 = q_polynomials()
    d34_ok = all(
        Poly(base, z).LC() > 0 and no_real_root_at_or_above(base, z, 49)
        for base, _exp in Poly(d34, z).factor_list()[1]
    )
    # sympify("N") resolves to sympy's numerical-eval function unless the
    # symbol is supplied explicitly — the factor strings are polynomials in N.
    n = Symbol("N")
    factors = walled_brauer()["B"]["denominator_factors"]
    d409_ok = all(
        Poly(sympify(f["factor"], locals={"N": n}), n).LC() > 0
        and no_real_root_at_or_above(sympify(f["factor"], locals={"N": n}), n, 7)
        for f in factors
    )
    return {"d34": d34_ok, "d409": d409_ok, "d409_factors": len(factors)}


@cache
def fixed_rank_verification() -> dict:
    """The stored q samples N = 7..18 against the compact law, exactly."""
    z, q32, d34 = q_polynomials()
    samples = walled_brauer()["q"]["fixed_rank_samples"]
    checked = []
    for sample in samples:
        n = int(sample["N"])
        law = Fraction(-2, 3 * n) * Fraction(int(q32.eval(n * n)), int(d34.subs(z, n * n)))
        checked.append(Fraction(sample["q"]) == law)
    return {"count": len(samples), "all_match": all(checked), "ranks": [s["N"] for s in samples]}
