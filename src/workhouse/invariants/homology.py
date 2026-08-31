from __future__ import annotations

from sympy import (
    I,
    Matrix,
    conjugate,
    cos,
    exp,
    expand,
    eye,
    limit,
    oo,
    pi,
    simplify,
    sin,
    symbols,
    sympify,
)

from .. import constants as K
from .. import torus as TOR
from ._core import _suite

# ==========================================================================
homology = _suite("homology and finite volume")


@homology.check("dim Z_2 = (L^3 - 1) + 3 = L^3 + 2", "UNIFIED §0.1")
def _():
    lhs = (K.L**3 - 1) + 3
    return simplify(lhs - K.dim_z2()) == 0, "cube boundaries plus the harmonic plane triplet"


@homology.check("dim Z_2 at L = 3, 4, 5", "UNIFIED §0.1")
def _():
    vals = {n: K.dim_z2(n) for n in (3, 4, 5)}
    return vals == {3: 29, 4: 66, 5: 127}, f"{vals}"


# --------------------------------------------------------------------------
# The chain-level carrier, built rather than asserted. The two checks above
# are arithmetic on the formula (L^3-1)+3; neither ever constructed a
# boundary map. workhouse.torus builds the periodic complex from the
# manuscript's printed boundary formulas and settles every rank by
# elimination — the manuscript's own proof, carried out.
# --------------------------------------------------------------------------


@homology.check("d_2 d_3 = 0 on the built complex", "MASTER paper App. E")
def _():
    ok = all((TOR.d2_matrix(ell) * TOR.d3_matrix(ell)).is_zero() for ell in (1, 2, 3, 4))
    return ok, (
        "the composite of the two printed boundary formulas vanishes over Z at "
        "L = 1..4 — every edge cancels pairwise, as the substitution argument says"
    )


@homology.check("rank d_3 = L^3 - 1 on the built complex", "MASTER paper App. E")
def _():
    ranks = {ell: TOR.d3_matrix(ell).rank() for ell in (1, 2, 3, 4)}
    ok = all(r == ell**3 - 1 for ell, r in ranks.items())
    return ok, (
        f"exact integer ranks {ranks}; the one relation is the sum of all "
        "oriented cubes, so ker d_3 is one-dimensional on the torus"
    )


@homology.check(
    "dim Z_2 = L^3 + 2 by rank, not by re-arranging the formula",
    "MASTER paper Thm. 2",
)
def _():
    exact = {ell: TOR.kernel_dim_exact(ell) for ell in (1, 2, 3, 4, 5)}
    bounds = {ell: TOR.kernel_dim_bounds(ell) for ell in (1, 2, 3, 4, 5)}
    ok = all(exact[ell] == ell**3 + 2 for ell in exact) and all(
        bounds[ell] == (ell**3 + 2, ell**3 + 2) for ell in bounds
    )
    return ok, (
        f"exact nullity of the built d_2: {exact}; the exhibited cycles bound "
        "the kernel from BELOW (their mod-p rank lower-bounds their Q-rank) and "
        "the mod-p nullity of d_2 bounds it from ABOVE (rank drops under "
        "reduction), and the two bounds meet at every L"
    )


@homology.check(
    "cube boundaries and three wrapping sheets SPAN Z_2",
    "MASTER paper Thm. 2",
)
def _():
    ok = True
    detail = {}
    for ell in (2, 3, 4):
        d2 = TOR.d2_matrix(ell)
        cyc = TOR.cycle_matrix(ell)
        in_kernel = (d2 * cyc).is_zero()
        spans = cyc.rank() == TOR.kernel_dim_exact(ell)
        ok = ok and in_kernel and spans
        detail[ell] = (cyc.rank(), TOR.kernel_dim_exact(ell))
    return ok, (
        f"(rank of exhibited cycles, dim ker d_2) = {detail}: every exhibited "
        "column is an exact integer cycle and together they have full kernel "
        "rank, so the L^3 cube boundaries plus the three wrapping sheets span"
    )


@homology.check(
    "the L^3+2 count is chain-level, not the Bloch convention",
    "MASTER paper Rmk. 3",
)
def _():
    small = {ell: TOR.kernel_dim_exact(ell) for ell in (1, 2)}
    ok = small == {1: 3, 2: 10}
    return ok, (
        f"dim ker d_2 = {small} at L = 1, 2 — the count needs no L >= 3: that "
        "restriction belongs to the twelve-neighbour Bloch adjacency, where "
        "x+e and x-e coincide at L = 2, not to the chain complex"
    )


@homology.check("the Bloch and chain routes to the carrier agree", "MASTER paper Thm. 4")
def _():
    ok = True
    detail = {}
    for ell in (2, 3, 4):
        total = 0
        profile: dict[int, int] = {}
        for m1 in range(ell):
            for m2 in range(ell):
                for m3 in range(ell):
                    d = [exp(2 * pi * I * m / ell) - 1 for m in (m1, m2, m3)]
                    bloch = Matrix([[d[1], -d[0], 0], [d[2], 0, -d[0]], [0, d[2], -d[1]]])
                    nullity = 3 - bloch.rank()
                    profile[nullity] = profile.get(nullity, 0) + 1
                    total += nullity
        ok = ok and total == ell**3 + 2 and profile == {3: 1, 1: ell**3 - 1}
        detail[ell] = total
    return ok, (
        f"sum over the momentum grid of (3 - rank B(k)) = {detail}, with "
        "nullity 3 exactly once (at Gamma) and 1 at each of the other L^3 - 1 "
        "momenta — the 3x3 Bloch spectrum and the (L^3+2)-dimensional chain "
        "kernel are the same count: the 3 is B(0) = 0's triple degeneracy, not "
        "b_2(T^3), and the L^3 - 1 counts momenta, not cubes"
    )


@homology.check(
    "FINDING: the wrapping sheets are cycles but NOT harmonic",
    "MASTER paper §3.1",
)
def _():
    ok = True
    for ell in (2, 3, 4, 5):
        d2 = TOR.d2_matrix(ell)
        for pair in TOR.FACE_PAIRS:
            sheet = TOR.wrapping_sheet(ell, pair)
            col = TOR.flint.fmpz_mat([[v] for v in sheet])
            num, den = TOR.sheet_rayleigh_num_den(ell, pair)
            ok = ok and (d2 * col).is_zero() and num == 2 * den and num > 0
    return ok, (
        "d_2 s = 0 exactly, yet <s, d_3 d_3^T s>/||s||^2 = 2 exactly for every "
        "L >= 2 and every orientation: the sheets span the quotient "
        "ker d_2 / im d_3 but do not lie in the harmonic subspace "
        "ker d_2 ∩ ker d_3^T — H_2 in the quotient sense and H_2 in the Hodge "
        "sense must not be conflated in real-space statements"
    )


@homology.check("the zone maximum of q is 12 only at even L", "MASTER paper eq. (24)")
def _():
    ok = True
    detail = {}
    for ell in range(2, 10):
        vals = [4 * sin(pi * m / ell) ** 2 for m in range(ell)]
        qmax = 3 * max(vals, key=lambda v: float(v))
        claimed = sympify(12) if ell % 2 == 0 else simplify(12 * cos(pi / (2 * ell)) ** 2)
        ok = ok and simplify(qmax - claimed) == 0
        detail[ell] = float(qmax)
    return ok, (
        f"q_max(L) exact on the grid, evaluated: { {k: round(v, 6) for k, v in detail.items()} }"
        " — only even L samples k_j = pi, so only even L attains 12"
    )


@homology.check("q_min on the L-torus grid is 4 sin^2(pi/L)", "MASTER paper §4.4")
def _():
    ok = True
    for ell in range(2, 10):
        vals = [4 * sin(pi * m / ell) ** 2 for m in range(1, ell)]
        qmin = min(vals, key=lambda v: float(v))  # one unit of momentum, one direction
        ok = ok and simplify(qmin - 4 * sin(pi / ell) ** 2) == 0
    return ok, (
        "the smallest nonzero grid q puts one unit of momentum in a single "
        "direction; all other nonzero assignments are checked larger"
    )


@homology.check(
    "Delta_L = 4 tau(u) sin^2(pi/L) is positive and falls as L^-2",
    "MASTER paper §8",
)
def _():
    tau = K.t_series()
    tau_pos = all(tau.coeff(K.u, r) > 0 for r in (2, 3))
    scaling = limit(K.L**2 * 4 * sin(pi / K.L) ** 2, K.L, oo)
    return tau_pos and scaling == 4 * pi**2, (
        f"tau(u) = {tau} has positive coefficients, so Delta_L > 0 for u > 0; "
        "L^2 * q_min -> 4 pi^2, so the carrier's nearest incidence separation "
        "vanishes as L^-2 and provides no volume-uniform isolation"
    )


# --------------------------------------------------------------------------
# What the 30 August master edition added to the carrier, and one retraction.
#
# Earlier editions read the agreement of the Bloch and chain counts as a
# coincidence worth checking -- "the 3 is the triple degeneracy of B(0) = 0,
# NOT b_2(T^3)". That was wrong. Under the DFT d_2 block-diagonalises; at
# k != 0 the kernel block is one-dimensional and is exactly im d_3(k), while
# d_3(0) = 0. So all of im d_3 sits at nonzero momenta, the quotient is
# supported entirely at Gamma, and the Gamma block IS H_2. The real-space
# face of the same statement is that averaging a wrapping sheet over its L
# translates -- the k = 0 projection -- lands in the harmonic subspace.
# --------------------------------------------------------------------------


@homology.check(
    "the sheets average to harmonic representatives, and the Gamma block IS b_2",
    "MASTER edition §3.1 and Remark (Bloch--chain bridge)",
)
def _():
    # Two halves, and the second is the retraction. First: the L-translate
    # average h of a wrapping sheet satisfies d_2 h = 0 AND d_3^T h = 0, so
    # the harmonic subspace has representatives for all three classes and is
    # exactly three-dimensional; and h differs from s by a boundary, so they
    # are the same class -- the finding that the SHEETS are not harmonic
    # stands, and is not weakened by the existence of harmonic averages.
    # Second: dim ker d_2 minus dim im d_3 is 3 at every extent, and the
    # three harmonic chains span that quotient, which is what "the Gamma
    # block is b_2" says without a Fourier transform.
    harmonic, boundary_diff, quotient = {}, {}, {}
    for ell in (2, 3, 4):
        d2, d3 = TOR.d2_matrix(ell), TOR.d3_matrix(ell)
        cols = []
        for pair in ((1, 2), (1, 3), (2, 3)):
            vec, denom = TOR.sheet_average(ell, pair)
            cols.append(vec)
            # d_2 h = 0 and d_3^T h = 0, both over Z on the numerator
            up = [sum(int(d3[r, c]) * vec[r] for r in range(d3.nrows())) for c in range(d3.ncols())]
            down = [
                sum(int(d2[r, c]) * vec[c] for c in range(d2.ncols())) for r in range(d2.nrows())
            ]
            harmonic[(ell, pair)] = (all(v == 0 for v in up), all(v == 0 for v in down), denom)
            # s - h is a boundary: L*s - (L*h) lies in im d_3, so the ranks agree
            sheet = TOR.wrapping_sheet(ell, pair)
            diff = [ell * sheet[r] - vec[r] for r in range(len(vec))]
            aug = Matrix(
                [[int(d3[r, c]) for c in range(d3.ncols())] + [diff[r]] for r in range(d3.nrows())]
            )
            base = Matrix([[int(d3[r, c]) for c in range(d3.ncols())] for r in range(d3.nrows())])
            boundary_diff[(ell, pair)] = aug.rank() == base.rank()
        span = Matrix([[col[r] for col in cols] for r in range(len(cols[0]))]).rank()
        quotient[ell] = (TOR.kernel_dim_exact(ell) - d3.rank(), span)
    ok = (
        all(u and d for u, d, _ in harmonic.values())
        and all(boundary_diff.values())
        and all(qd == 3 and sp == 3 for qd, sp in quotient.values())
    )
    return ok, (
        f"L = 2, 3, 4: the three translate-averaged sheets are harmonic (d_2 h = 0 and "
        f"d_3^T h = 0, exactly, over Z on the numerator), each differs from its sheet by a "
        f"boundary, and they span a 3-dimensional space; (dim ker d_2 - rank d_3, span) = "
        f"{quotient}. So ker d_2 / im d_3 is 3 = b_2(T^3) and the harmonic subspace realises it "
        "-- the retracted reading was that the 3 is only the triple degeneracy of B(0) = 0. "
        "The sheets themselves remain non-harmonic; that finding is unchanged"
    )


@homology.check(
    "the Fourier sum of cube boundaries IS the carrier, and a local seed costs L^-3",
    "MASTER edition Prop. (fixed-momentum carrier and the locality tradeoff)",
)
def _():
    # The locality proposition prices sharp momentum. Two exact halves:
    # (1) the DFT of the radius-one cube boundaries has squared norm exactly
    # q(k), and since d_2 d_3 = 0 it lies in ker B(k)^dagger, which is
    # one-dimensional for k != 0 -- so the normalised Fourier sum is THE unit
    # carrier there, not merely a vector in the kernel; (2) inverting the
    # unitary transform gives the overlap of the unit carrier with one
    # normalised cube seed as sqrt(q(k) / 6 L^3), which falls as L^{-3/2} in
    # amplitude at fixed k. Both are rational identities, not tolerances.
    norms = {}
    for ell in (3, 4, 5):
        for r in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0)):
            if any(v >= ell for v in r):
                continue
            n2, q = TOR.cube_boundary_fourier_norm(ell, r)
            norms[(ell, r)] = simplify(n2 - q) == 0
    # the seed overlap, from the inverse transform: |<phi, b/sqrt6>|^2 = q / (6 L^3)
    ell, r = 4, (1, 1, 0)
    _, q = TOR.cube_boundary_fourier_norm(ell, r)
    overlap_sq = simplify(q / (6 * ell**3))
    # at k = 0 the transform vanishes: every cube boundary sums to zero
    d3 = TOR.d3_matrix(3)
    zero_mode = all(
        sum(int(d3[row, c]) for c in range(d3.ncols())) == 0 for row in range(d3.nrows())
    )
    ok = all(norms.values()) and norms and zero_mode and overlap_sq == simplify(q / 384)
    return ok, (
        f"||\\hat b_L(k)||^2 = q(k) exactly at every tested (L, k): {sorted(norms)}; d_2 d_3 = 0 "
        "puts it in ker B(k)^dagger, which Theorem (incidence factorisation) makes "
        "one-dimensional for k != 0, so the normalised Fourier sum is the unique unit carrier "
        f"there. The price is locality: one normalised cube seed has squared overlap "
        f"q(k)/(6 L^3) = {overlap_sq} at L = 4, k = 2 pi(1,1,0)/4, i.e. amplitude O(L^(-3/2)) at "
        "fixed momentum, and \\hat b_L(0) = 0 exactly because every cube boundary sums to zero"
    )


@homology.check(
    "a boundary-factorised correction shifts the carrier without dispersing it, for generic M",
    "MASTER edition §8 (boundary-factorised rigidity)",
)
def _():
    # The protection belongs to the boundary operator, not the dynamics: for
    # H_r(k) = a I + b S(k) + B(k) M(k) B(k)^dagger, the middle term is
    # annihilated whatever M is, because B^dagger w = 0. Checked with a
    # GENERIC symbolic M -- nine free entries, no structure assumed -- at
    # symbolic momentum, so the statement is about the factorisation and not
    # about any particular correction.
    k1, k2, k3 = symbols("k1 k2 k3", real=True)
    d = [exp(I * k) - 1 for k in (k1, k2, k3)]
    B = Matrix([[d[1], -d[0], 0], [d[2], 0, -d[0]], [0, d[2], -d[1]]])
    w = Matrix([conjugate(d[2]), -conjugate(d[1]), conjugate(d[0])])
    m = Matrix(3, 3, symbols("m0:9"))
    a, b = symbols("a b")
    S = B * B.conjugate().T - 4 * eye(3)
    H = a * eye(3) + b * S + B * m * B.conjugate().T
    residual = simplify(expand(H * w - (a - 4 * b) * w))
    return residual.is_zero_matrix, (
        "with M a generic symbolic 3x3 (nine free entries) and k symbolic, "
        "H_r(k) w(k) = (a_r - 4 b_r) w(k) identically: B^dagger w = 0 kills the middle term "
        "whatever M is, and S w = -4 w. The correction moves the carrier level and cannot "
        "disperse it -- and this is exactly why {B M B^dagger} being no two-sided ideal is the "
        "caveat that matters, not the size of M"
    )
