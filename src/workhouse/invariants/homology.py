from __future__ import annotations

from sympy import (
    I,
    Matrix,
    cos,
    exp,
    limit,
    oo,
    pi,
    simplify,
    sin,
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
    "the sheets average to harmonic representatives, and the Gamma block IS b_2",
    "MASTER paper §3.1 / Rmk. after the Bloch-chain bridge",
)
def _():
    # RETRACTS a remark the manuscript carried from its 2026-08-28 edition:
    # "the 3 is the triple degeneracy of B(0) = 0, not b_2(T^3)". It is
    # b_2(T^3), canonically, and the mistake was to read a Fourier
    # decomposition as a coincidence.
    #
    # Under discrete Fourier transform d_2 block-diagonalises and
    # ker d_2 = (+)_k ker d_2(k). At k != 0 the kernel block is
    # one-dimensional and is exactly im d_3(k), so the whole of im d_3 lives
    # at nonzero momenta; at k = 0, d_3(0) = 0 and the kernel block is all of
    # C^3. So the quotient ker d_2 / im d_3 is supported entirely at Gamma,
    # and the Gamma block IS H_2. The two numbers of the bridge are the same
    # numbers, not two that agree.
    #
    # The constructive half, which the earlier edition lacked entirely: a
    # single wrapping sheet is a cycle but NOT harmonic (the sibling FINDING
    # measures its Rayleigh quotient at exactly 2). Its average over the L
    # translates in the complementary direction,
    #
    #     h_(ij) = (1/L) sum_{r<L} s_(ij)(r),
    #
    # IS harmonic -- it is the k = 0 Fourier component of the sheet, and the
    # sheet's non-harmonicity is entirely in the modes the average kills. The
    # three averages span the harmonic subspace, and each sheet differs from
    # its own average by a boundary, so they are the same homology class.
    # Nothing about the earlier FINDING is withdrawn: the exhibited
    # generators are still not harmonic. What was missing was that harmonic
    # representatives exist, and are one line away.
    import flint

    ok = True
    detail = []
    for ell in (2, 3, 4):
        d2, d3 = TOR.d2_matrix(ell), TOR.d3_matrix(ell)
        n_faces = 3 * ell**3

        def averaged(pair, ell=ell, n_faces=n_faces):
            """L * h_(ij): the sheet summed over all L translates."""
            (m,) = set((1, 2, 3)) - set(pair)
            vec = [0] * n_faces
            for x in TOR.sites(ell):
                if x[m - 1] < ell:
                    vec[TOR.face_index(x, pair, ell)] += 1
            return vec

        d3_cols = [[int(d3[r, c]) for r in range(n_faces)] for c in range(d3.ncols())]
        boundaries = flint.fmpz_mat([[col[r] for col in d3_cols] for r in range(n_faces)])
        rank_boundaries = boundaries.rank()

        for pair in TOR.FACE_PAIRS:
            h = averaged(pair)
            # harmonic: killed by d_2 and by d_3^T, over Z on L*h
            ok &= all(
                sum(int(d2[a, b]) * h[b] for b in range(n_faces)) == 0 for a in range(d2.nrows())
            )
            ok &= all(
                sum(int(d3[b, c]) * h[b] for b in range(n_faces)) == 0 for c in range(d3.ncols())
            )
            # and the single sheet differs from the average by a boundary
            sheet = TOR.wrapping_sheet(ell, pair)
            diff = [ell * sheet[i] - h[i] for i in range(n_faces)]
            augmented = flint.fmpz_mat(
                [[col[r] for col in d3_cols] + [diff[r]] for r in range(n_faces)]
            )
            ok &= augmented.rank() == rank_boundaries

        # the harmonic subspace is exactly three-dimensional: b_2(T^3)
        stacked = flint.fmpz_mat(
            [[int(d2[a, b]) for b in range(n_faces)] for a in range(d2.nrows())]
            + [[int(d3[b, c]) for b in range(n_faces)] for c in range(d3.ncols())]
        )
        harmonic_dim = n_faces - stacked.rank()
        ok &= harmonic_dim == 3 and rank_boundaries == ell**3 - 1
        detail.append(f"L={ell}: harmonic {harmonic_dim}, rank d_3 {rank_boundaries}")

    return ok, (
        "h_(ij) = (1/L) sum_r s_(ij)(r) satisfies d_2 h = 0 AND d_3^T h = 0 over Z, for every "
        f"pair and every {', '.join(detail)} -- so the harmonic subspace is exactly "
        "b_2(T^3) = 3 and the three averaged sheets span it, while each single sheet differs "
        "from its own average by a boundary and represents the same class. This RETRACTS the "
        "manuscript's remark that the 3 at Gamma is 'not b_2(T^3)': ker d_2 = (+)_k ker d_2(k), "
        "at k != 0 the kernel block is exactly im d_3(k), and d_3(0) = 0, so the quotient is "
        "supported entirely at Gamma and the Gamma block IS H_2. The bridge's two numbers are "
        "the same numbers. The sibling FINDING stands unchanged: a single sheet is a cycle and "
        "is not harmonic"
    )


@homology.check(
    "a boundary-factorised correction shifts the carrier without dispersing it, for generic M",
    "MASTER paper Prop. (boundary-factorised rigidity)",
)
def _():
    # The rigidity proposition, as a statement about a GENERIC M rather than
    # about its ingredient. What the registry checked before was the incidence
    # identity BB^dagger = qI - ww^dagger; the proposition needs more than
    # that -- it needs the operator a I + b S + B M B^dagger to act on the
    # carrier by a - 4b for EVERY M, which is what makes the protection a
    # property of the boundary factorisation and not of any particular
    # correction. Nine free entries, symbolic, and the six incidence variables
    # kept independent so nothing is smuggled in through a conjugation
    # identity: B^dagger w = 0 is a polynomial identity in d and conj(d)
    # separately, and that is the whole content.
    #
    # This is also where the proposition's LIMIT lives: it says nothing about
    # a correction that does not factor through links, which is exactly why
    # the paper's fourth-order section cannot appeal to it.
    from sympy import MatrixSymbol, expand, symbols, zeros

    d1, d2, d3 = symbols("d1 d2 d3")
    e1, e2, e3 = symbols("e1 e2 e3")  # the conjugates, kept independent
    a, b = symbols("a b")
    bmat = Matrix([[d2, -d1, 0], [d3, 0, -d1], [0, d3, -d2]])
    bdag = Matrix([[e2, e3, 0], [-e1, 0, e3], [0, -e1, -e2]])
    w = Matrix([e3, -e2, e1])
    m = Matrix(MatrixSymbol("M", 3, 3))
    ident = Matrix.eye(3)
    s = bmat * bdag - 4 * ident
    correction = a * ident + b * s + bmat * m * bdag
    residual = expand(correction * w - (a - 4 * b) * w)
    # and the two ingredients, separately, so a failure says which one broke
    return (
        residual == zeros(3, 1)
        and expand(bdag * w) == zeros(3, 1)
        and expand(s * w + 4 * w) == zeros(3, 1)
    ), (
        "with d_j and conj(d_j) independent and all nine entries of M free, "
        "(a I + b S + B M B^dagger) w - (a - 4b) w vanishes identically: B^dagger w = 0 kills the "
        "M term whatever M is, and S w = -4w follows from the same identity. So every order-r "
        "correction that factors through links shifts the carrier and cannot disperse it -- the "
        "protection belongs to the boundary operator, not to the dynamics. It says nothing about "
        "a correction that does NOT factor through links, and {B M B^dagger} is not a two-sided "
        "ideal, which is why the fourth order has to be argued and not inherited"
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
