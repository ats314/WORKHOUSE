"""Full-zone channel decomposition of the historical fourth-order kernel.

The corpus's own shape decomposition (UNIFIED v4.3 §5.1/§6) writes the
carrier dispersion as eps_4 = c_0 + A q_a + B e_2 + C (4 e_2/q_a) + D e_3/q_a.
The repository's existing kernel checks evaluate the 189-record artifact at
the four parity points; this module decomposes it *identically in k* — exact
Laurent polynomials in z_j = e^{i k_j} over ``fractions.Fraction`` — and
classifies the records into physical transfer channels, so the tier collapse
B = D = 0 becomes two exact integer cancellations at record level rather
than a parity-point observation.

Convention (the one trap): the numerator is psi^dagger H_4 psi with the KET
in the d-direction, ket = (d_3, -d_2, d_1) with d_j = 1 - z_j, and the bra
its conjugate — the same convention as ``tier_collapse``. The conjugated
ket coincides with this one at the four parity points (d is real there), so
parity-point checks cannot distinguish them; over the whole zone only the
d-ket makes the rotation block a function of the cubic invariants. The
records enter with Fourier factor z^{+d} against this bra/ket pairing.

Everything here characterizes the historical kernel artifact and recorded
corpus formulas. Nothing adjudicates C2; no side is promoted.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache

from sympy import Poly, Symbol

from . import payloads as P

Monomial = tuple[int, int, int]
Laurent = dict[Monomial, Fraction]

#: Every degree-3 channel amplitude is an integer multiple of this — itself a
#: raw record weight (96 of the 120 rotation records carry +-x).
X_QUANTUM = Fraction(360421351, 40327601932800)

BLOCKS = (
    "on-site (0,0,0)",
    "NORMAL (0,0,1)",
    "IN-PLANE (0,0,1)",
    "IN-PLANE (0,0,2)",
    "IN-PLANE (0,1,1)",
    "MIXED (0,1,1)",
    "ROTATION",
)


def _add(p: Laurent, q: Laurent) -> Laurent:
    r: dict[Monomial, Fraction] = defaultdict(Fraction, p)
    for m, c in q.items():
        r[m] += c
    return {m: c for m, c in r.items() if c}


def _mul(p: Laurent, q: Laurent) -> Laurent:
    r: dict[Monomial, Fraction] = defaultdict(Fraction)
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            r[m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2]] += c1 * c2
    return {m: c for m, c in r.items() if c}


def _scale(p: Laurent, s: Fraction) -> Laurent:
    return {m: c * s for m, c in p.items() if c * s}


def _mono(e1: int = 0, e2: int = 0, e3: int = 0, c: Fraction = Fraction(1)) -> Laurent:
    return {(e1, e2, e3): c}


_ONE = _mono()
_Z = [_mono(*(1 if i == j else 0 for j in range(3))) for i in range(3)]
_ZINV = [_mono(*(-1 if i == j else 0 for j in range(3))) for i in range(3)]

# d_j = 1 - z_j ; conj(d_j) = 1 - 1/z_j ; a_j = 2 - z_j - 1/z_j
_D = [_add(_ONE, _scale(_Z[j], Fraction(-1))) for j in range(3)]
_DBAR = [_add(_ONE, _scale(_ZINV[j], Fraction(-1))) for j in range(3)]
_A = [
    _add(
        _scale(_ONE, Fraction(2)),
        _add(_scale(_Z[j], Fraction(-1)), _scale(_ZINV[j], Fraction(-1))),
    )
    for j in range(3)
]

_q = _add(_A[0], _add(_A[1], _A[2]))
_e2 = _add(_mul(_A[0], _A[1]), _add(_mul(_A[0], _A[2]), _mul(_A[1], _A[2])))
_e3 = _mul(_A[0], _mul(_A[1], _A[2]))

#: Numerator basis: N = E*1 + c0*q + A*q^2 + F*q^3 + (4C)*e2 + B*(q e2) + D*e3.
_BASIS: list[tuple[str, Laurent]] = [
    ("E", _ONE),
    ("c0", _q),
    ("A", _mul(_q, _q)),
    ("F", _mul(_q, _mul(_q, _q))),
    ("C4", _e2),
    ("B", _mul(_q, _e2)),
    ("D", _e3),
]

_PLANES = ((0, 1), (0, 2), (1, 2))
_IDX = {pl: i for i, pl in enumerate(_PLANES)}
#: ket = (d_3, -d_2, d_1); bra = its conjugate (tier_collapse convention).
_KET = [_D[2], _scale(_D[1], Fraction(-1)), _D[0]]
_BRA = [_DBAR[2], _scale(_DBAR[1], Fraction(-1)), _DBAR[0]]
#: The wrong pairing: ket conjugated too. Coincides at parity points only.
_KET_CONJ = [_DBAR[2], _scale(_DBAR[1], Fraction(-1)), _DBAR[0]]


def numerator(records, ket=None) -> Laurent:
    """psi^dagger H psi as an exact Laurent polynomial."""
    ket = _KET if ket is None else ket
    total: Laurent = {}
    for (ip, op, d), w in records:
        zd = _mono(*d, c=Fraction(w))
        total = _add(total, _mul(_BRA[_IDX[op]], _mul(zd, ket[_IDX[ip]])))
    return total


def solve_span(num: Laurent) -> dict[str, Fraction] | None:
    """Exact coefficients of ``num`` in the seven-element basis, or None."""
    monos = sorted(set().union(*(set(b) for _, b in _BASIS), set(num)))
    rows = [[b.get(m, Fraction(0)) for _, b in _BASIS] + [num.get(m, Fraction(0))] for m in monos]
    ncols = len(_BASIS)
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        pv = rows[r][c]
        rows[r] = [v / pv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [v - f * w for v, w in zip(rows[i], rows[r], strict=True)]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    sol = {name: Fraction(0) for name, _ in _BASIS}
    names = [name for name, _ in _BASIS]
    for i, c in enumerate(pivots):
        sol[names[c]] = rows[i][ncols]
    recon: Laurent = {}
    for name, b in _BASIS:
        recon = _add(recon, _scale(b, sol[name]))
    return sol if recon == num else None


def classify(ip, op, d) -> str:
    """Physical transfer channel of one record."""
    if ip != op:
        return "ROTATION"
    normal_axis = ({0, 1, 2} - set(ip)).pop()
    shell = tuple(sorted(abs(v) for v in d))
    nz = [i for i, v in enumerate(d) if v != 0]
    if shell == (0, 0, 0):
        return "on-site (0,0,0)"
    if shell == (0, 0, 1):
        return "NORMAL (0,0,1)" if nz == [normal_axis] else "IN-PLANE (0,0,1)"
    if shell == (0, 0, 2):
        return "IN-PLANE (0,0,2)"
    if shell == (0, 1, 1):
        return "IN-PLANE (0,1,1)" if normal_axis not in nz else "MIXED (0,1,1)"
    raise AssertionError(f"unclassifiable record {ip} {op} {d}")


@lru_cache(maxsize=1)
def decompose() -> dict:
    """Per-block exact shape coefficients of the 189-record kernel."""
    recs = P.kernel_records()
    blocks: dict[str, list] = defaultdict(list)
    for rec in recs:
        blocks[classify(*rec[0])].append(rec)
    per_block: dict[str, dict[str, Fraction]] = {}
    totals: dict[str, Fraction] = defaultdict(Fraction)
    for b in BLOCKS:
        sol = solve_span(numerator(blocks[b]))
        if sol is None:
            raise AssertionError(f"block {b} is not in the seven-element span")
        per_block[b] = sol
        for k, v in sol.items():
            totals[k] += v
    return {
        "n_records": len(recs),
        "counts": {b: len(blocks[b]) for b in BLOCKS},
        "blocks": per_block,
        "totals": dict(totals),
        "records": {b: tuple(blocks[b]) for b in BLOCKS},
    }


def support_census() -> dict[tuple[int, int, int], int]:
    """Sorted-|d| displacement shells with multiplicities."""
    census: dict[tuple[int, int, int], int] = defaultdict(int)
    for (_ip, _op, d), _w in P.kernel_records():
        census[tuple(sorted(abs(v) for v in d))] += 1
    return dict(census)


def rotation_shells_in_span() -> dict[tuple[int, int, int], bool]:
    """Span membership per rotation displacement shell, individually."""
    shells: dict[tuple[int, int, int], list] = defaultdict(list)
    for rec in decompose()["records"]["ROTATION"]:
        shells[tuple(sorted(abs(v) for v in rec[0][2]))].append(rec)
    return {sh: solve_span(numerator(rr)) is not None for sh, rr in shells.items()}


def conjugated_ket_rotation_in_span() -> bool:
    """The trap: with the ket conjugated, is the rotation block in the span?"""
    return solve_span(numerator(decompose()["records"]["ROTATION"], ket=_KET_CONJ)) is not None


# --------------------------------------------------------------------------
# The all-rank balanced shape formula, transcribed from the corpus.
# GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md: the boxed
# beta_N = P17(z)/(N R20(z)), z = N^2, stated "For N>=4" (line ~1074, R20 at
# lines ~1080-1088, P17 in Appendix A lines ~1490-1508), with the caution at
# line ~1511: "The compact beta_N formula is not to be substituted at N=3;
# use the separate exact SU(3) value." Every R20 factor is nonzero at z = 9,
# so the continuation exists; what it means at N = 3 is a claim, not a check.

_z = Symbol("z")

P17 = Poly(
    2096187310080 * _z**17
    - 45206560309248 * _z**16
    + 448972002607104 * _z**15
    - 2723575470882816 * _z**14
    + 11288692151812096 * _z**13
    - 33888218411529728 * _z**12
    + 76218901019673664 * _z**11
    - 131068691814847264 * _z**10
    + 174326341061538992 * _z**9
    - 180230597250871976 * _z**8
    + 144751635142984472 * _z**7
    - 89742150515602808 * _z**6
    + 42388925672412712 * _z**5
    - 14916377727371552 * _z**4
    + 3768794520714128 * _z**3
    - 641987460459360 * _z**2
    + 65414604672000 * _z
    - 2967321600000,
    _z,
)

R20 = Poly(
    (_z - 1) ** 3
    * (2 * _z - 3)
    * (2 * _z - 1) ** 3
    * (3 * _z - 2)
    * (3 * _z - 1)
    * (4 * _z - 9) ** 3
    * (4 * _z - 5)
    * (4 * _z - 1)
    * (9 * _z - 25)
    * (9 * _z - 16)
    * (16 * _z**2 - 44 * _z + 25)
    * (16 * _z**2 - 33 * _z + 16),
    _z,
)


def beta_formula(n: int) -> Fraction:
    """P17(N^2)/(N R20(N^2)), evaluated exactly."""
    return Fraction(int(P17.eval(n * n)), n * int(R20.eval(n * n)))


def b_note(n: int) -> Fraction:
    """The pinned structured expression, evaluated exactly at rank ``n``."""
    return eval(P.b_evaluator(), {"__builtins__": {}}, {"N": Fraction(n)})  # noqa: S307
