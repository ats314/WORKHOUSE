"""The fourth-order kernel as six amplitudes, exactly.

One investigation, one module — the shape of ``tier_collapse.py`` and
``kernel_comparison.py``.

``kernel_comparison`` fits the shape coefficients at four points of the zone
with condition number 45.8, which is what the v10a.26 transcript did and why
every non-axial number in the dispute is a float. This module does the
decomposition instead of the fit. The Bloch symbol of the carrier projection,

    T(k) = psi(k)^dagger S(k) psi(k),   psi = (dbar_3, -dbar_2, dbar_1),

is a *Laurent polynomial* in z_j = exp(i k_j) with rational coefficients, and
the shape ansatz cleared of its denominator,

    T = c0*e1 + A*e1^2 + B*e1*e2 + 4C*e2 + D*e3,   e_r = elementary sym in s_j,
    s_j = 4 sin^2(k_j/2) = 2 - z_j - z_j^{-1},

is a linear system over that same ring. Solving it exactly gives the shape
coefficients over the *whole* zone, with a residual that is either zero or a
witness that the kernel is outside the four-shape span. No tolerance appears
anywhere, so the result is T1 and blockwise.

What that buys, and why the module exists: the 189 records of the historical
kernel carry only **six** distinct weight magnitudes, and each magnitude is one
orbit of the cubic symmetry. In terms of those six amplitudes the shape data is
closed form —

    A = 5/48,   B = 0,   D = 0,   C = -5/96 - u - (rho + pi)/2,

with ``nu = -(5/48 + 4u)`` forced by A and the on-site amplitude entering c0
alone. Three signed numbers, not a seven-row table of floats. The cold v10a.26
dump reproduces the same six orbits and the same normalized coefficients, which
is what makes the two kernels comparable amplitude by amplitude rather than
through one aggregate C.

Nothing here prefers either side of C2. It reports both in the same basis.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COLD_DUMP = ROOT / "runs" / "g3_kernel_record_dump_2026-08-28" / "g3_kernel_records.json"

PLANES = ((0, 1), (0, 2), (1, 2))
#: The direction a plane does not contain — psi_P is +-dbar of it.
NORMAL_OF = {(0, 1): 2, (0, 2): 1, (1, 2): 0}
#: psi = (dbar_3, -dbar_2, dbar_1) in plane order, per ``payloads.rayleigh``.
PSI_SIGN = {(0, 1): 1, (0, 2): -1, (1, 2): 1}

Exponent = tuple[int, int, int]
Laurent = dict[Exponent, Fraction]

# -- exact Laurent arithmetic in three variables -----------------------------


def _add(a: Laurent, b: Laurent, scale=1) -> Laurent:
    out = dict(a)
    for e, c in b.items():
        v = out.get(e, 0) + scale * c
        if v:
            out[e] = v
        else:
            out.pop(e, None)
    return out


def _mul(a: Laurent, b: Laurent) -> Laurent:
    out: Laurent = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = (e1[0] + e2[0], e1[1] + e2[1], e1[2] + e2[2])
            v = out.get(e, 0) + c1 * c2
            if v:
                out[e] = v
            else:
                out.pop(e, None)
    return out


def _mono(exp, coeff=Fraction(1)) -> Laurent:
    return {tuple(exp): Fraction(coeff)}


def _s(j: int) -> Laurent:
    """s_j = 4 sin^2(k_j/2) = 2 - z_j - z_j^{-1}."""
    up, down = [0, 0, 0], [0, 0, 0]
    up[j], down[j] = 1, -1
    return _add(_add(_mono((0, 0, 0), 2), _mono(up, -1)), _mono(down, -1))


def _dbar(j: int, conj: bool = False) -> Laurent:
    """dbar_j = z_j - 1, or its conjugate z_j^{-1} - 1."""
    e = [0, 0, 0]
    e[j] = -1 if conj else 1
    return _add(_mono(e), _mono((0, 0, 0), -1))


_S = [_s(0), _s(1), _s(2)]
E1 = _add(_add(_S[0], _S[1]), _S[2])
E2 = _add(_add(_mul(_S[0], _S[1]), _mul(_S[0], _S[2])), _mul(_S[1], _S[2]))
E3 = _mul(_mul(_S[0], _S[1]), _S[2])

#: T = c0*e1 + A*e1^2 + B*e1*e2 + 4C*e2 + D*e3.  The ansatz is written for
#: eps = T/q with q = e1; clearing q keeps every entry polynomial.
BASIS: dict[str, Laurent] = {
    "c0": E1,
    "A": _mul(E1, E1),
    "B": _mul(E1, E2),
    "4C": E2,
    "D": E3,
}
ORDER = ("c0", "A", "B", "4C", "D")


# -- the carrier projection, and its exact shape ------------------------------


def bloch(records) -> Laurent:
    """T(k) = psi^dagger S(k) psi as an exact Laurent polynomial."""
    out: Laurent = {}
    for (ip, op, d), w in records:
        term = _mul(_mul(_dbar(NORMAL_OF[op], conj=True), _dbar(NORMAL_OF[ip])), _mono(d))
        out = _add(out, term, PSI_SIGN[op] * PSI_SIGN[ip] * Fraction(w))
    return out


def shape(target: Laurent) -> tuple[dict[str, Fraction], Laurent]:
    """Exact shape coefficients of a Laurent target, and what is left over.

    A nonempty residual is the statement that this record group does not lie in
    the four-shape span at all — that is a finding, not a fitting error, so it
    is returned rather than minimized.
    """
    exps = sorted(set().union(*(b.keys() for b in BASIS.values())) | set(target))
    rows = [
        [BASIS[n].get(e, Fraction(0)) for n in ORDER] + [target.get(e, Fraction(0))] for e in exps
    ]
    pivots, r = [], 0
    for col in range(len(ORDER)):
        p = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = rows[r][col]
        rows[r] = [v / inv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col]:
                f = rows[i][col]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r], strict=True)]
        pivots.append(col)
        r += 1
    coeffs = dict.fromkeys(ORDER, Fraction(0))
    for i, col in enumerate(pivots):
        coeffs[ORDER[col]] = rows[i][len(ORDER)]
    fit: Laurent = {}
    for n in ORDER:
        fit = _add(fit, BASIS[n], coeffs[n])
    return coeffs, _add(target, fit, -1)


def coefficients(records) -> tuple[dict[str, Fraction], Laurent]:
    """``(A, B, C, D, c0)`` of a record group, with C already halved out of 4C."""
    co, residual = shape(bloch(records))
    co = dict(co)
    co["C"] = co["4C"] / 4
    return co, residual


# -- the six orbits -----------------------------------------------------------


def orbits(records) -> dict[Fraction, list]:
    """Records grouped by weight magnitude — one group per cubic orbit."""
    by = defaultdict(list)
    for key, w in records:
        by[abs(w)].append((key, w))
    return dict(by)


#: What each orbit contributes, per unit of its own amplitude. Both
#: independently computed kernels give exactly this table, which is what makes
#: the amplitudes comparable across them.
#:
#:   orbit        n    A      B     D      C
#:   skeleton   132   -4      0    -6     +3
#:   doubled     12    0      0    +3     -1
#:   rotation    24    0      0     0   -1/2
#:   in-plane    12    0      0     0   -1/2
#:   normal       6   -1      0     0   +1/2
#:   on-site      3    0      0     0      0
ORBIT_SIZES = (("skeleton", 132), ("rotation", 24), ("normal", 6), ("on-site", 3))


def amplitudes(records, solver=coefficients) -> dict[str, Fraction]:
    """The six signed orbit amplitudes: u, u2, rho, pi, nu, sigma.

    Read off the orbit's *shape contribution*, not its record signs: the
    rotation orbit carries both signs by construction (twelve of each), so a
    sign taken from the weights would be a convention, while

        C_skeleton = 3u,  C_doubled = -u2,  C_rot = -rho/2,
        C_in-plane = -pi/2,  A_normal = -nu,  c0_on-site = sigma

    is forced. ``orbit_amplitude_matches_record_weight`` then checks that each
    one equals the orbit's record weight up to sign, which is the statement
    that the orbit really is a single amplitude.
    """
    by = orbits(records)
    twelves = sorted(m for m in by if len(by[m]) == 12)
    groups = {
        "u": by[max(by, key=lambda m: len(by[m]))],
        "u2": by[twelves[0]],
        "rho": by[next(m for m in by if len(by[m]) == 24)],
        "pi": by[twelves[1]],
        "nu": by[next(m for m in by if len(by[m]) == 6)],
        "sigma": by[next(m for m in by if len(by[m]) == 3)],
    }
    co = {name: solver(g)[0] for name, g in groups.items()}
    return {
        "u": co["u"]["C"] / 3,
        "u2": -co["u2"]["C"],
        "rho": -2 * co["rho"]["C"],
        "pi": -2 * co["pi"]["C"],
        "nu": -co["nu"]["A"],
        "sigma": co["sigma"]["c0"],
    }


def orbit_magnitudes(records) -> dict[str, Fraction]:
    """The weight magnitude carried by each orbit's records."""
    by = orbits(records)
    twelves = sorted(m for m in by if len(by[m]) == 12)
    return {
        "u": max(by, key=lambda m: len(by[m])),
        "u2": twelves[0],
        "rho": next(m for m in by if len(by[m]) == 24),
        "pi": twelves[1],
        "nu": next(m for m in by if len(by[m]) == 6),
        "sigma": next(m for m in by if len(by[m]) == 3),
    }


# -- the cold (v10a.26) dump, in the same basis -------------------------------


def cold_records() -> list:
    """The v10a.26 record dump keyed like ``payloads.kernel_records``.

    Displacements are stored on a 5^3 torus; ``(x + 2) % 5 - 2`` recenters
    them, the convention ``kernel_comparison.load_cold`` already established.
    Weights are floats: everything downstream of here is T2.
    """
    obj = json.loads(COLD_DUMP.read_text(encoding="utf-8"))
    return [
        (
            (
                tuple(r["anchor_pol"]),
                tuple(r["row_pol"]),
                tuple((x + 2) % 5 - 2 for x in r["displacement"]),
            ),
            r["re"],
        )
        for r in obj["records"]
    ]


def cold_orbits(tol: float = 1e-9) -> list[tuple[float, int, list]]:
    """Cold records clustered by weight magnitude: ``(magnitude, count, group)``.

    The clusters are not close calls — within each one the spread is below
    1e-15 relative, and the gaps between them are factors of two or more.
    """
    groups: list[list] = []
    for key, w in sorted(cold_records(), key=lambda r: abs(r[1])):
        if groups and abs(abs(w) - abs(groups[-1][-1][1])) <= tol * max(1.0, abs(w)):
            groups[-1].append((key, w))
        else:
            groups.append([(key, w)])
    return [(sum(abs(w) for _, w in g) / len(g), len(g), g) for g in groups]


def _float_shape(records) -> dict[str, float]:
    """Shape coefficients of float-weighted records, over the same exact basis.

    Least squares over the whole zone rather than the transcript's four points
    (condition number 45.8). The basis is exact; only the weights are floats,
    so anything reached through here is T2.
    """
    target: dict[Exponent, float] = {}
    for (ip, op, d), w in records:
        term = _mul(_mul(_dbar(NORMAL_OF[op], conj=True), _dbar(NORMAL_OF[ip])), _mono(d))
        sign = PSI_SIGN[op] * PSI_SIGN[ip]
        for e, c in term.items():
            target[e] = target.get(e, 0.0) + sign * w * float(c)
    exps = sorted(set().union(*(b.keys() for b in BASIS.values())) | set(target))
    cols = [[float(BASIS[n].get(e, 0)) for e in exps] for n in ORDER]
    y = [target.get(e, 0.0) for e in exps]
    m = len(ORDER)
    gram = [
        [sum(cols[i][r] * cols[j][r] for r in range(len(exps))) for j in range(m)] for i in range(m)
    ]
    rhs = [sum(cols[i][r] * y[r] for r in range(len(exps))) for i in range(m)]
    for i in range(m):
        p = max(range(i, m), key=lambda r: abs(gram[r][i]))
        gram[i], gram[p] = gram[p], gram[i]
        rhs[i], rhs[p] = rhs[p], rhs[i]
        if abs(gram[i][i]) < 1e-30:
            continue
        for r in range(m):
            if r != i and gram[r][i]:
                f = gram[r][i] / gram[i][i]
                gram[r] = [a - f * b for a, b in zip(gram[r], gram[i], strict=True)]
                rhs[r] -= f * rhs[i]
    co = {ORDER[i]: (rhs[i] / gram[i][i] if abs(gram[i][i]) > 1e-30 else 0.0) for i in range(m)}
    co["C"] = co["4C"] / 4
    return co


def cold_amplitudes() -> dict[str, float]:
    """The v10a.26 dump's six signed amplitudes, by the same definitions.

    Float throughout, so T2. Orbits are told apart exactly as in the exact
    path: by record count, and the two 12-record orbits by magnitude.
    """
    cold = cold_orbits()
    groups = {n: g for _, n, g in cold}
    twelves = sorted((m, g) for m, n, g in cold if n == 12)
    return {
        "u": _float_shape(groups[132])["C"] / 3,
        "u2": -_float_shape(twelves[0][1])["C"],
        "rho": -2 * _float_shape(groups[24])["C"],
        "pi": -2 * _float_shape(twelves[1][1])["C"],
        "nu": -_float_shape(groups[6])["A"],
        "sigma": _float_shape(groups[3])["c0"],
    }


#: Each orbit's carrier projection T = psi^dagger S psi, as a polynomial in the
#: elementary symmetric functions of s_j, per unit of the orbit's amplitude.
#: Five of the six follow from the orbit's displacement set in two lines; the
#: sixth (the skeleton) is solved from its records, with residual zero.
#:
#:   on-site    S_P = sigma                     -> sigma * e1
#:   normal     S_P = nu (2 - s_n)              -> nu (2 e1 - e1^2 + 2 e2)
#:   in-plane   S_P = pi sum_{i in P} (2 - s_i) -> pi (4 e1 - 2 e2)
#:   doubled    S_P = u2 (2 - s_i)(2 - s_j)     -> u2 (4 e1 - 4 e2 + 3 e3)
#:   rotation   S_PQ = -eps_P eps_Q rho dbar_{n(Q)} conj(dbar_{n(P)})
#:                                              -> rho (-2 e2)
#:   skeleton                                   -> u (12 e1 - 4 e1^2 + 12 e2 - 6 e3)
#:
#: No orbit produces the e1*e2 monomial, which is B: the q e_2 collapse is that
#: none of the six generates it, not a cancellation between them.
CLOSED_FORMS = {
    "sigma": {"e1": 1},
    "nu": {"e1": 2, "e1e1": -1, "e2": 2},
    "pi": {"e1": 4, "e2": -2},
    "u2": {"e1": 4, "e2": -4, "e3": 3},
    "rho": {"e2": -2},
    "u": {"e1": 12, "e1e1": -4, "e2": 12, "e3": -6},
}


def symmetric(**terms) -> Laurent:
    """A combination of e1, e1^2 (``e1e1``), e2, e3 as a Laurent polynomial."""
    parts = {"e1": E1, "e1e1": _mul(E1, E1), "e2": E2, "e3": E3}
    out: Laurent = {}
    for name, coeff in terms.items():
        out = _add(out, parts[name], coeff)
    return out


def orbit_groups(records) -> dict[str, list]:
    """Records keyed by orbit name, the same six the amplitudes are named for."""
    by = orbits(records)
    twelves = sorted(m for m in by if len(by[m]) == 12)
    return {
        "u": by[max(by, key=lambda m: len(by[m]))],
        "u2": by[twelves[0]],
        "rho": by[next(m for m in by if len(by[m]) == 24)],
        "pi": by[twelves[1]],
        "nu": by[next(m for m in by if len(by[m]) == 6)],
        "sigma": by[next(m for m in by if len(by[m]) == 3)],
    }


def two_cos(m: int) -> Laurent:
    """X_m = z_m + z_m^{-1} = 2 cos k_m = 2 - s_m."""
    up, down = [0, 0, 0], [0, 0, 0]
    up[m], down[m] = 1, -1
    return _add(_mono(up), _mono(down))


def same_plane_long_range(records) -> dict[tuple[int, int], Laurent]:
    """Per plane, the same-plane records at shells (0,0,2) and (0,1,1).

    That is everything a plane sends to itself except the two
    nearest-neighbour orbits (nu along its normal, pi in its own axes) and the
    on-site term: sixteen records, four at u2 and twelve at u.
    """
    out: dict[tuple[int, int], Laurent] = {}
    for (ip, op, d), w in records:
        if ip == op and any(d) and sorted(abs(x) for x in d) != [0, 0, 1]:
            out.setdefault(ip, {})[tuple(d)] = Fraction(w)
    return out


def perfect_product(plane: tuple[int, int], u: Fraction) -> Laurent:
    """u * [(X + Y)(X + Y + Z) - 4] for a plane with axes {i, j} and normal n."""
    i, j = plane
    xy = _add(two_cos(i), two_cos(j))
    form = _add(_mul(xy, _add(xy, two_cos(NORMAL_OF[plane]))), _mono((0, 0, 0), -4))
    return {e: u * c for e, c in form.items() if c}


def cross_plane_skeleton(records, u: Fraction) -> tuple[list, Laurent]:
    """The 96 cross-plane records at amplitude u, and their closed form.

    ``-2 u e_2 (e_1 - 8)``: pure e_2 times a linear factor, which is why the
    sector carries no e_3 and no A at all.
    """
    group = [r for r in records if r[0][0] != r[0][1] and abs(r[1]) == u]
    form = _mul(E2, _add(E1, _mono((0, 0, 0), -8)))
    return group, {e: -2 * u * c for e, c in form.items() if c}
