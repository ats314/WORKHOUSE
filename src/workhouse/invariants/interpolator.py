"""The G18 interpolator: local carrier operators and the sheet no-go.

G18 asks for a volume-uniform overlap of a smeared, dressed T_1^{+-} operator
with the transfer-matrix spectrum, and the published measurements (Schierholz
1988, BKS 1990) say the bare plaquette operator carries a few percent that
degrades toward the continuum. This suite establishes the exact finite-volume
half of that problem and localises what remains.

Four exact statements, each checked below:

1. The boundary of one elementary cube is an exact zero-mode of the face Gram
   d2^T d2 at every L -- so it is an exact eigenstate of every assembled
   symbol of the form alpha*I + beta*Gram (the proved order-u^2 theorem, the
   third-order factorisation, and every boundary-factorised correction of
   the rigidity proposition), with locality radius 1 and L-independent norm.
   In-sector, the overlap problem at nonzero momentum is not small-overlap:
   it is exactly solved by a named local operator.

2. Every vector in im d3 has exactly zero zone-average (k = 0) component,
   while each wrapping sheet carries zone-average L^2. The k = 0 carrier
   content lives entirely in the sheet summands.

3. A normalised sheet overlaps any single-face state by exactly 1/L: the
   sheets decouple from every fixed local observable as L grows, at an exact
   rate, so the locally visible carrier in the infinite-volume limit is
   im d3 alone.

4. On an open window with free boundary, the interior-supported 2-cycles are
   exactly the interior cube boundaries (compact H_2 vanishes on the checked
   windows; the unbounded statement is classical Alexander duality for R^3,
   named here as an input the way the Casimir facts are named in the shell
   lemma). Hence every finitely supported exactly-flat state is a sum of
   cube boundaries -- and by (2) it is Gamma-blind.

Together: the in-sector overlap deficit of the flat level is exactly zero at
every k != 0, uniformly in L, carried by radius-1 operators; and the
zero-momentum protected state provably cannot be interpolated by any exactly
flat local operator -- the obstruction G18 must dress away is confined to the
out-of-sector (multi-plaquette) components and to the Gamma point, where the
in-sector bands are degenerate through u^3 anyway. None of this crosses to
the transfer-matrix spectrum or the continuum; G18 stays open and tier 3.
"""

from __future__ import annotations

from itertools import product

from sympy import Rational

from .. import torus as TOR
from ._core import _suite

# ==========================================================================
interpolator = _suite("the G18 interpolator: local carrier operators and the sheet no-go")


@interpolator.check(
    "cube boundaries are exact flat eigenstates of every assembled symbol, L = 2..5",
    "G18 / PUB edition Thm. 16 / MASTER paper Thm. 2",
)
def _():
    ok = True
    detail = {}
    for ell in (2, 3, 4, 5):
        d2, d3 = TOR.d2_matrix(ell), TOR.d3_matrix(ell)
        gram_d3 = d2.transpose() * d2 * d3
        zero = all(gram_d3[i, j] == 0 for i in range(3 * ell**3) for j in range(ell**3))
        # norm^2 of one cube boundary: six faces, entries +-1 -> 6, at every L
        norm2 = sum(int(d3[i, 0]) ** 2 for i in range(3 * ell**3))
        ok = ok and zero and norm2 == 6
        detail[ell] = norm2
    return ok, (
        "(d2^T d2) d3 = 0 exactly over Z at L = 2..5, so alpha*I + beta*(d2^T d2) "
        "fixes every cube-boundary state at alpha for EVERY beta -- the proved "
        "order-u^2 symbol, the third-order factorisation alpha(u) + tau(u) BB^dag, "
        "and every correction of the boundary-factorised rigidity class alike; "
        f"each boundary has norm^2 = {detail} (six faces), locality radius 1, "
        "independent of L: an exact, volume-uniform, unit-in-sector-overlap "
        "local interpolator for the flat level at every nonzero momentum"
    )


@interpolator.check(
    "im d3 is Gamma-blind, and the sheets carry the whole zone-average",
    "G18 / MASTER paper Thm. 2",
)
def _():
    ok = True
    detail = {}
    for ell in (2, 3, 4, 5):
        d3 = TOR.d3_matrix(ell)
        col_sums_vanish = all(
            sum(int(d3[3 * s + pi, c]) for s in range(ell**3)) == 0
            for c in range(ell**3)
            for pi in range(3)
        )
        sheet_k0 = {pair: sum(TOR.wrapping_sheet(ell, pair)) for pair in TOR.FACE_PAIRS}
        ok = ok and col_sums_vanish and all(v == ell**2 for v in sheet_k0.values())
        detail[ell] = sorted(sheet_k0.values())
    return ok, (
        "per-orientation zone averages of every cube-boundary column vanish "
        "exactly (each face enters its two adjacent cubes with opposite signs), "
        f"while each wrapping sheet carries zone-average L^2 = {detail} -- the "
        "k = 0 component of the carrier ker d2 = im d3 (+) sheets lives "
        "entirely in the sheet summands, so every exactly-flat operator built "
        "from cube boundaries has amplitude ZERO on the zero-momentum "
        "protected states, at every L: the Gamma no-go that forces a G18 "
        "interpolator out of the exactly-flat local algebra"
    )


@interpolator.check(
    "the sheets decouple from local observables at exact rate 1/L",
    "G18 / MASTER paper §3.1",
)
def _():
    ok = True
    detail = {}
    for ell in (2, 3, 4, 5):
        overlaps = set()
        for pair in TOR.FACE_PAIRS:
            sheet = TOR.wrapping_sheet(ell, pair)
            norm2 = sum(v * v for v in sheet)
            if norm2 != ell**2:
                ok = False
            # entries are 0/1, so a single-face overlap is 0 or 1/sqrt(L^2)
            overlaps.update({Rational(v**2, norm2) for v in sheet})
        ok = ok and overlaps == {Rational(0), Rational(1, ell**2)}
        detail[ell] = f"1/{ell}"
    return ok, (
        "each sheet has norm^2 = L^2 with 0/1 entries, so its normalised "
        f"overlap with any single-face state is exactly {detail} -- the "
        "wrapping (H_2) part of the carrier fades from every fixed local "
        "observable at rate 1/L, and the locally visible carrier in the "
        "infinite-volume limit is im d3 alone; the sheets are torus "
        "bookkeeping, not physics a local operator can see"
    )


def _open_box(n):
    """d2, d3 of the open n^3 vertex window with free boundary, over Z."""
    edges: dict = {}
    faces: dict = {}
    cubes: dict = {}
    for x in product(range(n), repeat=3):
        for i in range(3):
            y = list(x)
            y[i] += 1
            if y[i] < n:
                edges[(x, i)] = len(edges)
        for i, j in ((0, 1), (0, 2), (1, 2)):
            yi, yj = list(x), list(x)
            yi[i] += 1
            yj[j] += 1
            if yi[i] < n and yj[j] < n:
                faces[(x, (i, j))] = len(faces)
        if all(x[d] + 1 < n for d in range(3)):
            cubes[x] = len(cubes)
    d2 = [[0] * len(faces) for _ in range(len(edges))]
    for (x, (i, j)), fc in faces.items():
        xi, xj = list(x), list(x)
        xi[i] += 1
        xj[j] += 1
        d2[edges[(x, i)]][fc] += 1
        d2[edges[(tuple(xi), j)]][fc] += 1
        d2[edges[(tuple(xj), i)]][fc] -= 1
        d2[edges[(x, j)]][fc] -= 1
    d3 = [[0] * len(cubes) for _ in range(len(faces))]
    for x, cc in cubes.items():
        for sign, d, pair in ((1, 0, (1, 2)), (-1, 1, (0, 2)), (1, 2, (0, 1))):
            y = list(x)
            y[d] += 1
            d3[faces[(tuple(y), pair)]][cc] += sign
            d3[faces[(x, pair)]][cc] -= sign
    return TOR.flint.fmpz_mat(d2), TOR.flint.fmpz_mat(d3), len(faces), len(cubes)


@interpolator.check(
    "compact 2-cycles on open windows are exactly cube boundaries",
    "G18 / MASTER paper App. E",
)
def _():
    ok = True
    detail = {}
    for n in (2, 3, 4):
        d2, d3, n_faces, n_cubes = _open_box(n)
        composite = d2 * d3
        chain = all(
            composite[i, j] == 0 for i in range(composite.nrows()) for j in range(composite.ncols())
        )
        nullity = n_faces - d2.rank()
        rank3 = d3.rank()
        ok = ok and chain and nullity == rank3 == n_cubes
        detail[n] = (n_faces, n_cubes, nullity)
    return ok, (
        f"(faces, cubes, dim ker d2) = {detail} on the open n^3 windows with "
        "free boundary: d2 d3 = 0 and the kernel dimension equals the cube "
        "count exactly, so every 2-cycle a window supports is a sum of its "
        "cube boundaries -- compact H_2 = 0 on the checked windows (the "
        "unbounded-lattice statement is classical Alexander duality for R^3, "
        "a named input). Hence every finitely supported exactly-flat state is "
        "a boundary sum, and by the Gamma-blindness check it cannot "
        "interpolate the zero-momentum protected level at all"
    )
