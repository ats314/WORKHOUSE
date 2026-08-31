from __future__ import annotations

from sympy import (
    Matrix,
    Poly,
    Rational,
    expand,
    eye,
    limit,
    pi,
    series,
    simplify,
    solve,
    symbols,
    zeros,
)

from .. import cellular as CELL
from .. import constants as K
from ._core import _suite

# ==========================================================================
sealed = _suite("fourth order, sealed core")


@sealed.check("alpha_3 = 4*A_shp = 5/12", "MASTER_THEORY §5.2")
def _():
    ok = K.alpha_pen(3) == 4 * K.A_SHP_3 == K.ALPHA_PEN_3
    return ok, f"alpha_3 = {K.alpha_pen(3)}"


@sealed.check("axial law reproduces alpha_4, alpha_5, alpha_6", "MASTER_THEORY §5.3")
def _():
    want = {4: Rational(32, 675), 5: Rational(1, 108), 6: Rational(64, 25725)}
    got = {n: K.alpha_pen(n) for n in want}
    return got == want, f"{ {k: str(v) for k, v in got.items()} }"


@sealed.check("alpha_3 = 4*|c_4^square(3)|", "MOB §4")
def _():
    # Exact: both sides are Rational. A second, independent route to alpha_3 --
    # the cube-completion coefficient rather than the shape coefficient A.
    route = 4 * abs(K.CUBE_COMPLETION_4)
    return route == K.ALPHA_PEN_3, (
        f"4*|c_4^square(3)| = 4*|{K.CUBE_COMPLETION_4}| = {route} = alpha_3, the "
        f"same value the shape route gives as 4*A_shp = 4*{K.A_SHP_3}"
    )


def _sealed_gaps():
    return {
        "A": abs(K.A_SHP_3_NUM - float(K.A_SHP_3)),
        "B": abs(K.B_SHP_3_NUM - float(K.B_SHP_3)),
        "D": abs(K.D_SHP_3_NUM - float(K.D_SHP_3)),
        "alpha": abs(K.ALPHA_PEN_3_NUM - float(K.ALPHA_PEN_3)),
    }


@sealed.check("v10a.26 A, B, D match the sealed rationals within 2.3e-13", "GLUEBALL §10", tier=2)
def _():
    gaps = _sealed_gaps()
    subset = {k: gaps[k] for k in ("A", "B", "D")}
    ok = all(g <= K.SEALED_CORE_TOLERANCE for g in subset.values())
    return ok, "; ".join(f"{k} {v:.3e}" for k, v in subset.items())


@sealed.check(
    "FINDING: alpha_new falls outside the corpus's own 2.3e-13 bound",
    "GLUEBALL §10",
    tier=2,
)
def _():
    gaps = _sealed_gaps()
    # alpha = 4A, so it inherits four times A's deviation. The corpus's stated
    # aggregate bound (2.3e-13) tracks D_new (2.23e-13) and does not cover alpha.
    # This is a bookkeeping slip in the quoted tolerance, not a discrepancy in
    # the sealed core itself: the run's own alpha and A stay mutually consistent.
    exceeds = gaps["alpha"] > K.SEALED_CORE_TOLERANCE
    consistent = abs(K.ALPHA_PEN_3_NUM - 4 * K.A_SHP_3_NUM) < 1e-14
    return exceeds and consistent, (
        f"alpha gap {gaps['alpha']:.4e} > stated {K.SEALED_CORE_TOLERANCE:.1e} "
        f"(= 4x the A gap {gaps['A']:.4e}); alpha_new vs 4*A_new agree to "
        f"{abs(K.ALPHA_PEN_3_NUM - 4 * K.A_SHP_3_NUM):.1e}, so the sealed core holds "
        "and only the quoted bound is too tight"
    )


@sealed.check("exceptional ranks are exactly {3,4,5,6}", "MASTER_THEORY §5.3")
def _():
    # A fourth-order word carries at most 6 character factors, so a determinant
    # channel needs |p-q| = N <= 6; and N >= 3 for the sector to exist at all.
    derived = tuple(n for n in range(2, 12) if 3 <= n <= 6)
    return derived == K.EXCEPTIONAL_RANKS, f"{derived}"


# ==========================================================================
dispute = _suite("fourth order, anchoring and the residual dispute")


@dispute.check("historical q_3 decimal expansion", "MASTER_THEORY §5.5", tier=2)
def _():
    d = abs(float(K.Q_BAND_4) - (-2.857915988114559))
    return d < 1e-15, f"|diff| = {d:.2e}"


@dispute.check("C_old = (beta_pen_3 - 2*alpha_3)/16", "MASTER_THEORY §5.5")
def _():
    v = (K.BETA_PEN_3 - 2 * K.ALPHA_PEN_3) / 16
    return v == K.C_SHP_HISTORICAL, f"= {v}"


@dispute.check("Delta_Gamma = m_Gamma^(4) - q_band^(4)", "MASTER_THEORY §5.5 / C1", tier=2)
def _():
    v = K.M_GAMMA_4_NUM - float(K.Q_BAND_4)
    # Double-precision evaluation lands one ulp below the correctly rounded
    # value; both are recorded, so accept either.
    ok = min(abs(v - K.DELTA_GAMMA_NUM), abs(v - K.DELTA_GAMMA_AS_PRINTED_NUM)) < 1e-15
    return ok, f"double eval {v!r}; exact rounds to {K.DELTA_GAMMA_NUM!r}"


@dispute.check("FINDING: the printed Delta_Gamma is one ulp low", "MASTER_THEORY §5.5", tier=2)
def _():
    from .. import rigor

    # Certified enclosure (ADR 0010): the double M_GAMMA_4_NUM enters exactly,
    # the rational q_band^(4) enters as a 128-bit ball, and the comparisons
    # below are True only if provable from disjoint enclosures — this replaces
    # the earlier "evalf(25) is surely enough" with a machine guarantee.
    exact = rigor.ball(K.M_GAMMA_4_NUM) - rigor.ball(K.Q_BAND_4)
    printed_low = rigor.certified_lt(rigor.ball(K.DELTA_GAMMA_AS_PRINTED_NUM), exact)
    recorded_closer = rigor.certified_closer(
        exact, rigor.ball(K.DELTA_GAMMA_NUM), rigor.ball(K.DELTA_GAMMA_AS_PRINTED_NUM)
    )
    gap = K.DELTA_GAMMA_NUM - K.DELTA_GAMMA_AS_PRINTED_NUM
    return printed_low and recorded_closer, (
        f"certified: true Delta_Gamma = {rigor.describe(exact)}; the corpus's printed "
        f"{K.DELTA_GAMMA_AS_PRINTED_NUM!r} lies provably below it, and "
        f"{K.DELTA_GAMMA_NUM!r} is provably the closer double (gap {gap:.3e} = 1 ulp). "
        "Cosmetic, but the printed digit is not the correctly rounded one."
    )


@dispute.check(
    "a translation-local scalar shift changes nothing observable",
    "MASTER_THEORY §5.5 / C1",
)
def _():
    # H_mass = H_band + Delta_Gamma*I  =>  centered forms coincide identically.
    h = Matrix(3, 3, symbols("h1:10"))
    dg, q = symbols("dg q")
    centered_mass = (h + dg * eye(3)) - (q + dg) * eye(3)
    centered_band = h - q * eye(3)
    same = simplify(centered_mass - centered_band) == zeros(3, 3)
    return same, (
        "centered operator, eigenvectors, SOS factorization, mobility "
        "coefficients and bandwidth are all invariant under the anchoring shift, "
        "so q_band^(4) and m_Gamma^(4) are not competing estimates"
    )


@dispute.check(
    "Delta_C = C_new - C_old > 0 (the real discrepancy)",
    "MASTER_THEORY §5.5 / C2",
    tier=2,
)
def _():
    v = K.C_SHP_NEW_NUM - float(K.C_SHP_HISTORICAL)
    d = abs(v - K.DELTA_C_NUM)
    return d < 1e-16 and v > 0, f"{v!r} vs recorded {K.DELTA_C_NUM!r} (|diff| {d:.1e})"


@dispute.check("beta_new = 8A + 16*C_new", "MASTER_THEORY §5.5", tier=2)
def _():
    v = 8 * float(K.A_SHP_3) + 16 * K.C_SHP_NEW_NUM
    return abs(v - K.BETA_PEN_NEW_NUM) < 1e-15, f"= {v!r}"


@dispute.check("off-axis band splits are 8*Delta_C and 16*Delta_C", "MASTER_THEORY §5.5", tier=2)
def _():
    m, r = 8 * K.DELTA_C_NUM, 16 * K.DELTA_C_NUM
    ok = abs(m - K.M_SPLIT_RECORDED_NUM) < 1e-15 and abs(r - K.R_SPLIT_RECORDED_NUM) < 1e-15
    return ok, f"M: {m!r}, R: {r!r}; axial cuts agree exactly"


@dispute.check("bandwidth ratio W4_new / W4_old ~ 1.93", "MASTER_THEORY §5.5", tier=2)
def _():
    ratio = K.W4_NEW_NUM / K.W4_HISTORICAL_NUM
    return abs(ratio - 1.93) < 5e-3, f"= {ratio:.6f}"


@dispute.check("Hamer 8*a_4 matches m_Gamma to ~5.2e-13", "GLUEBALL §2.3", tier=2)
def _():
    d = abs(8 * K.HAMER_A4_NUM - K.M_GAMMA_4_NUM)
    return d < K.HAMER_TOLERANCE, (
        f"|diff| = {d:.2e}; a_4 is an unverified notebook transcription, "
        "so this is a normalization cross-check, not primary-source proof"
    )


@dispute.check("quarantined scalar decimal", "MASTER_THEORY §5.5", tier=2)
def _():
    d = abs(float(K.QUARANTINED_SCALAR) - (-11.068479463778765))
    return d < 1e-14, f"|diff| = {d:.2e}; rejected by both sides"


@dispute.check("C20: exact gate value vs printed float-reconstruction", "MASTER_THEORY C20", tier=2)
def _():
    exact = float(K.LINKED_VACUUM_4)
    artifact = float(K.LINKED_VACUUM_4_ARTIFACT)
    gap = abs(exact - artifact)
    ulp = 2.0**-53 * abs(exact)
    # C20 records these as agreeing "to float precision". They do not: the gap is
    # ~31 ulps, and the decimal printed throughout the corpus (-0.8800987156226097)
    # is the artifact's value, not the exact gate value (-0.8800987156226127).
    agree_to_float = gap <= 2 * ulp
    return (
        not agree_to_float,
        f"exact {exact!r} vs artifact {artifact!r}; gap {gap:.2e} = {gap / ulp:.0f} ulps. "
        f"They agree to ~14 significant digits, NOT to float precision as C20 states; "
        f"the corpus's printed decimal tracks the artifact.",
    )


@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)
def _():
    # Gate 85's equality was produced by construction with this shift, so it
    # certifies internal bookkeeping rather than independent agreement.
    return (
        abs(K.RUN15_APPLIED_SHIFT_NUM - K.DELTA_GAMMA_NUM) > 1.0,
        f"applied {K.RUN15_APPLIED_SHIFT_NUM} vs Delta_Gamma {K.DELTA_GAMMA_NUM} "
        "— target-derived, so gate 85 is not an independent scalar verification",
    )


# ==========================================================================
crosswalk = _suite("old-to-new crosswalk")


@crosswalk.check("Phi_C vanishes at Gamma along every direction", "MASTER_THEORY §5.5")
def _():
    t, n1, n2, n3 = symbols("t n1 n2 n3", positive=True)
    radial = K.phi_c((t * n1, t * n2, t * n3))
    lead = simplify(series(radial, t, 0, 4).removeO())
    vanishes = limit(radial, t, 0) == 0
    return vanishes, (
        f"Phi_C = {lead} = O(|k|^2), since e_2 = O(|k|^4) and Q = O(|k|^2). "
        "A Gamma-point scalar therefore constrains Delta_Gamma but places no "
        "constraint whatsoever on Delta_C."
    )


@crosswalk.check("Phi_C at the high-symmetry points", "MASTER_THEORY §5.1")
def _():
    got = {
        "X": K.phi_c((pi, 0, 0)),
        "M": K.phi_c((pi, pi, 0)),
        "P": K.phi_c((pi, pi / 2, 0)),
        "R": K.phi_c((pi, pi, pi)),
    }
    want = {"X": 0, "M": 8, "P": Rational(16, 3), "R": 16}
    return got == want, f"{ {k: str(v) for k, v in got.items()} }"


@crosswalk.check(
    "crosswalk reproduces the recorded off-axis band splits",
    "MASTER_THEORY §5.5",
    tier=2,
)
def _():
    # c_4_new(k) - c_4_old(k) - Delta_Gamma == Delta_C * Phi_C(k)
    m = K.DELTA_C_NUM * float(K.phi_c((pi, pi, 0)))
    r = K.DELTA_C_NUM * float(K.phi_c((pi, pi, pi)))
    ok = abs(m - K.M_SPLIT_RECORDED_NUM) < 1e-15 and abs(r - K.R_SPLIT_RECORDED_NUM) < 1e-15
    return ok, f"M -> {m!r}, R -> {r!r}; independently recorded as 8*Delta_C and 16*Delta_C"


@crosswalk.check("the crosswalk is exactly scalar on the momentum axes", "MASTER_THEORY §5.5")
def _():
    axial = [K.phi_c(kv) for kv in ((pi, 0, 0), (pi / 2, 0, 0), (pi / 3, 0, 0))]
    return all(a == 0 for a in axial), (
        "Phi_C vanishes on every axial cut, so axial data cannot distinguish the "
        "two kernels — the whole residual disagreement lives off-axis"
    )


@crosswalk.check("bandwidth is preserved only if Delta_C vanishes", "MASTER_THEORY §5.5", tier=2)
def _():
    # The scalar term drops out of any difference of band values; only Phi_C survives.
    spread = K.DELTA_C_NUM * (float(K.phi_c((pi, pi, pi))) - float(K.phi_c((pi, 0, 0))))
    return abs(spread) > 1e-3, (
        f"scalar re-anchoring alone leaves the centered structure unchanged, but the "
        f"additional Delta_C*Phi_C term spreads R against X by {spread:.6f}. Bandwidth "
        "survives the crosswalk only if Delta_C is shown to vanish or is absorbed by an "
        "exact operator identity; neither is established."
    )


# ==========================================================================
pencil = _suite("fourth-order generalized Hodge pencil")


@pencil.check("Q4 cross coefficient = beta_pen_3 / 4", "GLUEBALL §8")
def _():
    return K.Q4_CROSS == K.BETA_PEN_3 / 4, f"= {K.Q4_CROSS}"


@pencil.check("historical Q4 numerator is positive definite", "UNIFIED §0.1")
def _():
    m = Matrix(3, 3, lambda i, j: K.A_SHP_3 if i == j else K.Q4_CROSS / 2)
    eig = m.eigenvals()
    ok = all(e > 0 for e in eig) and set(eig) == {
        K.A_SHP_3 + K.Q4_CROSS,
        K.A_SHP_3 - K.Q4_CROSS / 2,
    }
    return ok, f"eigenvalues {sorted(str(e) for e in eig)} — PSD, in fact PD"


@pencil.check("centered kernel difference is PSD (vanishes on axes)", "MASTER_THEORY §5.5", tier=2)
def _():
    # C^dagger[(H4_new - s_new) - (H4_old - q_old)]C = 4*Delta_C*sum_{i<j} L_i L_j.
    # The eigenstructure is exact algebra on a symbolic Delta_C — the matrix
    # 2d(J - I) has eigenvalues 4d, -2d, -2d — and only the SIGN of Delta_C
    # is a float fact, because C_new exists only as the v10a.26 float. That
    # sign is the whole verdict, so the check is T2, not T1.
    d = symbols("d", positive=True)
    m = Matrix(3, 3, lambda i, j: 0 if i == j else 2 * d)
    eig = {simplify(e): mult for e, mult in m.eigenvals().items()}
    structure_ok = eig == {4 * d: 1, -2 * d: 2}
    return structure_ok and K.DELTA_C_NUM > 0, (
        f"form eigenvalues exactly {{4d: 1, -2d: 2}} for symbolic d; with Delta_C = "
        f"{K.DELTA_C_NUM:.6e} > 0 (float — C_new exists only as v10a.26 output) the form is "
        "indefinite as a free quadratic form, PSD on the cube-amplitude sector where "
        "the pencil is scoped"
    )


# ==========================================================================
extraction = _suite("fourth-order checkpoint extraction")

_As, _Bs, _Cs, _Ds, _c0 = symbols("A_shp B_shp C_shp D_shp c0")


def _eps4(k):
    """Generic cubic-invariant fourth-order correction on the flat fiber."""
    q, e2, e3 = K.cubic_invariants(k)
    return simplify(_c0 + _As * q + _Bs * e2 + _Cs * 4 * e2 / q + _Ds * e3 / q)


def _deltas():
    g = _c0  # epsilon_4(Gamma) = c0
    return (
        simplify(_eps4([pi, 0, 0]) - g),
        simplify(_eps4([pi, pi, 0]) - g),
        simplify(_eps4([pi, pi / 2, 0]) - g),
        simplify(_eps4([pi, pi, pi]) - g),
    )


@extraction.check("checkpoint values at X, M, P, R", "MASTER_THEORY §5.1")
def _():
    dX, dM, dP, dR = _deltas()
    ok = (
        simplify(dX - 4 * _As) == 0
        and simplify(dM - (8 * _As + 16 * _Bs + 8 * _Cs)) == 0
        and simplify(dP - (6 * _As + 8 * _Bs + Rational(16, 3) * _Cs)) == 0
        and simplify(dR - (12 * _As + 48 * _Bs + 16 * _Cs + Rational(16, 3) * _Ds)) == 0
    )
    return ok, f"dX={dX}, dM={dM}, dP={dP}, dR={dR}"


@extraction.check("the four extraction formulas invert the ansatz", "MASTER_THEORY §5.1")
def _():
    dX, dM, dP, dR = _deltas()
    ok = (
        simplify(dX / 4 - _As) == 0
        and simplify((dX + 4 * dM - 6 * dP) / 16 - _Bs) == 0
        and simplify(3 * (2 * dP - dM - dX) / 8 - _Cs) == 0
        and simplify(3 * (dR - 6 * dM + 6 * dP) / 16 - _Ds) == 0
    )
    return ok, "A, B, C, D each recovered exactly from the checkpoint deltas"


@extraction.check("X is blind to B, C, D — it fixes A alone", "MASTER_THEORY §5.1")
def _():
    dX, *_ = _deltas()
    free = {s for s in dX.free_symbols if s in {_Bs, _Cs, _Ds}}
    return not free, "Delta_X = 4*A_shp exactly, which is why the axial cuts agree"


# --------------------------------------------------------------------------
# The operator-structure dictionary behind the off-axis route.
#
# C2 is routed to G3, whose live step is a 30-cluster exact-Haar assembly
# behind a measured performance wall. A cheaper route exists and rests on one
# claim: that each range-1 operator structure contributes a FIXED shape
# coefficient, so the disputed C can be assembled channel by channel from
# structures that workhouse.cellular already re-derives independently.
#
# That claim is pure polynomial algebra in the band variables and is checked
# here rather than taken on the page's word -- three of its four rows come out
# exactly as recorded, and the fourth is sign-convention dependent, which
# matters because that sector carries ~15% of the disputed gap.
# --------------------------------------------------------------------------


@sealed.check(
    "each range-1 structure has a fixed shape coefficient; the rotation sign is a convention",
    "C2; MASTER edition §8 (shape basis); the off-axis channel dictionary",
)
def _():
    a1, a2, a3, g, f = symbols("a1 a2 a3 g f", positive=True)
    a = (a1, a2, a3)
    q = a1 + a2 + a3
    e2 = a1 * a2 + a1 * a3 + a2 * a3
    e3 = a1 * a2 * a3
    cos = [1 - aj / 2 for aj in a]  # a_j = 4 sin^2(k_j/2) = 2 - 2 cos k_j
    c0, A, B, C, D = symbols("c0 A B C D")

    def fit(numerator):
        """Match psi^dag H psi against c0 q + A q^2 + B e2 q + 4 C e2 + D e3."""
        resid = expand(numerator - (c0 * q + A * q**2 + B * e2 * q + C * 4 * e2 + D * e3))
        answer = solve(Poly(resid, a1, a2, a3).coeffs(), [c0, A, B, C, D], dict=True)
        return answer[0] if answer else None

    # |psi_n|^2 = a_n with psi the cube-boundary direction, so a diagonal H
    # contributes sum_n a_n H_nn and q_a = q.
    scalar = fit(g * q)
    normal = fit(expand(g * sum(a[n] * cos[n] for n in range(3))))
    inplane = fit(expand(g * sum(a[n] * sum(cos[m] for m in range(3) if m != n) for n in range(3))))
    # Orbital rotation: psi^dag R psi = f sum_{n != m} eps_n eps_m a_n a_m.
    # Taken covariantly (one sign for every product) it lands on 2 f e2; taken
    # with the raw psi = (conj(d3), -conj(d2), conj(d1)) signs it does not lie
    # in the shape span at all, which is the convention the record must fix.
    rotation = fit(expand(f * 2 * e2))
    raw_signs = fit(expand(f * 2 * (-a1 * a2 + a1 * a3 - a2 * a3)))

    ok = (
        scalar == {c0: g, A: 0, B: 0, C: 0, D: 0}
        and normal == {c0: g, A: -g / 2, B: 0, C: g / 4, D: 0}
        and inplane == {c0: 2 * g, A: 0, B: 0, C: -g / 4, D: 0}
        and rotation == {c0: 0, A: 0, B: 0, C: f / 2, D: 0}
        and raw_signs is None
    )
    return ok, (
        "scalar I -> (A,B,C,D) = 0; normal translation g cos k_n -> A = -g/2, C = +g/4; "
        "in-plane translation -> C = -g/4; covariant orbital rotation -> C = +f/2. Every "
        "range-1 structure gives B = D = 0 identically, so the tier collapse is what range-1 "
        "looks like. FINDING: the recorded dictionary gives the rotation row as C = -f/2; the "
        "covariant operator gives +f/2, and the raw psi = (conj(d3), -conj(d2), conj(d1)) signs "
        "put it OUTSIDE the shape span entirely. The rotation sector carries about 15% of the "
        "disputed C2 gap, so that sign is load-bearing and is recorded here as unsettled rather "
        "than picked"
    )


@sealed.check(
    "SELF-TEST: cellular's cube completion gives |A| = alpha_N/4 and C = -A/2 at every rank",
    "C2; G3 off-axis channel route; MOB §4",
)
def _():
    # The validation the off-axis route has to pass before it is trusted on
    # anything disputed, and it is target-blind by construction: it lands on
    # the ONE fourth-order shape coefficient both sides of C2 already agree on.
    #
    # Two independent pieces meet here. workhouse.cellular derives the
    # primitive cube-completion coefficient from Haar moments, the electric
    # convention and the history geometry -- it never reads either disputed
    # kernel. The shape dictionary, verified in the check above, converts a
    # range-1 normal hop into (A, C). Composed, they must return A = 5/48.
    #
    # They do, at SYMBOLIC N rather than only at N = 3, so the agreement is a
    # rank-generic identity and not a coincidence at one rank.
    #
    # CORRECTED 2026-08-30. An earlier form of this check asserted
    # A_normal = +alpha_N/4, which overstated it: the sign was CHOSEN, by
    # taking the hop amplitude as +2 c_prim. Rebuilding the same channel in
    # the Bloch basis from the repository's own cube boundary d_3 -- where
    # the two opposite faces of a cube carry OPPOSITE signs, so the hop is
    # -2 c_prim -- gives A_normal = -alpha_N/4 instead. What survives the
    # convention, and what this check therefore asserts, is the magnitude
    # |A_normal| = alpha_N/4 and the RATIO C_normal/A_normal = -1/2, which is
    # sign-free. The corpus itself fixes the overall sign by taking |c_4|
    # (see `alpha_3 = 4*|c_4^square(3)|`), so the convention is its, not this
    # module's, and the ratio is the part that carries information.
    a_normal, c_normal = CELL.shape_from_normal_hop(CELL.CUBE, CELL.CAP_SECTOR)
    alpha = K.alpha_pen(CELL.N)
    # Compare squares rather than absolute values: N is declared positive but
    # not >= 2, so sympy will not reduce Abs(N^2 - 1), and the point here is
    # precisely that the sign is not being asserted.
    rank_generic = simplify(a_normal**2 - (alpha / 4) ** 2) == 0
    ratio = simplify(c_normal / a_normal + Rational(1, 2)) == 0
    at_three = simplify(abs(a_normal.subs(CELL.N, 3)))
    ok = rank_generic and ratio and at_three == K.A_SHP_3
    return ok, (
        "cellular's c_4,prim = -160/(N(N^2-1)^3) (S_4 = -20 over 24 histories) is a range-1 "
        "normal hop, and the dictionary sends a hop of amplitude g to A = -g/2, C = +g/4. The "
        f"result is |A_normal(N)| = alpha_N/4 IDENTICALLY in N, giving {at_three} at N = 3 -- "
        "the agreed A_SHP_3, reached without reading either disputed kernel -- and the "
        "sign-free ratio C_normal/A_normal = -1/2 exactly. The OVERALL sign is a convention: "
        "built from the repository's own cube boundary d_3, whose opposite faces carry opposite "
        "signs, the same channel gives A_normal = -alpha_N/4, and the corpus fixes the choice by "
        "taking |c_4|. This validates the machinery on a channel both sides of C2 agree on. It "
        "adjudicates nothing: the in-plane channel is not a fourth-order completion at all "
        "(the minimal closed cell carrying a coplanar edge-sharing pair is the 1x2x1 box, ten "
        "unit faces, r = 8), and the perpendicular channel is a different off-diagonal "
        "structure from the recorded rotation row"
    )


#: The unit cube at the origin in the standard cubical basis: (position, plane,
#: boundary sign), read off the repository's own ``torus.d3_matrix``. The signs
#: are what convert the coherently oriented cell ``cellular`` works in into the
#: basis the Wilson loops actually live in, and they are load-bearing: the two
#: opposite faces of a cube carry OPPOSITE signs.
_CUBE_BLOCH = (
    ((0, 0, 0), (1, 2), -1),
    ((0, 0, 1), (1, 2), +1),
    ((0, 0, 0), (1, 3), +1),
    ((0, 1, 0), (1, 3), -1),
    ((0, 0, 0), (2, 3), -1),
    ((1, 0, 0), (2, 3), +1),
)


@sealed.check(
    "the perpendicular cube sector is a second fourth-order primitive channel, S_4 = -11",
    "C2; G3 off-axis channel route; MOB §4",
)
def _():
    # A unit cube offers exactly TWO fourth-order primitive completions, and
    # only one of them was on the books. Its three OPPOSITE face pairs are the
    # normal hop (S_4 = -20 over 24 histories, the registered c_4). Its twelve
    # ADJACENT pairs are perpendicular, so they change the face orientation --
    # a distinct channel, uniform over all 24 ordered pairs, and not recorded
    # anywhere in the corpus.
    #
    # What it does NOT license is reading it through the dictionary's rotation
    # row, and the reason is structural rather than a matter of range.
    #
    # CORRECTED 2026-08-30. An earlier form of this check said the channel is
    # "range-2", inferred from displacements reaching +-2 on every axis. That
    # measured the carrier projection psi^dag H psi, not the operator: psi
    # itself carries displacement content (each d_j spans 0 and 1), so the
    # projection inherits it. The OPERATOR has max |displacement| = 1 -- it is
    # range-1, over the shells (0,0,0), (0,0,1) and (0,1,1).
    #
    # The real reason the dictionary's row does not apply: in the Bloch basis
    # built from the repository's own cube boundary, this channel's entry is
    # H_[(12),(13)] = -conj(d_2) d_3, whereas the recorded rotation row is
    # +conj(d_n) d_m. Those are MINUS THE CONJUGATE of one another, so the two
    # are different off-diagonal structures, and the recorded C = -f/2 is a
    # statement about the other one. The flagged sign stays open.
    perpendicular = {}
    opposite = {}
    for p in range(6):
        for qq in range(6):
            if p == qq:
                continue
            shared = {frozenset(e) for e in CELL._face_edges(CELL.CUBE.faces[p])} & {
                frozenset(e) for e in CELL._face_edges(CELL.CUBE.faces[qq])
            }
            coefficient, signed, hist = CELL.c_prim(CELL.CUBE, p, qq)
            bucket = perpendicular if shared else opposite
            bucket[(simplify(coefficient), signed, len(hist))] = (
                bucket.get((simplify(coefficient), signed, len(hist)), 0) + 1
            )

    # The record census, which is what compares against the corpus's own block
    # table: (input plane, output plane, displacement) triples, by shell. The
    # normal channel's 6 records at (0,0,1) match the recorded NORMAL (0,0,1)
    # block exactly, which is the corroboration that this mapping is the right
    # one; the perpendicular channel's 24 span THREE shells and so do not sit
    # in any single recorded block.
    def _census(cross_plane):
        seen = {}
        for xa, Pa, ea in _CUBE_BLOCH:
            for xb, Pb, eb in _CUBE_BLOCH:
                if (Pa != Pb) != cross_plane or (not cross_plane and (xa, Pa) == (xb, Pb)):
                    continue
                seen[(Pa, Pb, tuple(xb[i] - xa[i] for i in range(3)))] = ea * eb
        out = {}
        for _p, _q, delta in seen:
            key = tuple(sorted(abs(c) for c in delta))
            out[key] = out.get(key, 0) + 1
        return out

    shells = _census(True)
    normal_shells = _census(False)
    perp_key = next(iter(perpendicular))
    opp_key = next(iter(opposite))
    c_perp, s_perp, n_perp = perp_key
    c_opp, s_opp, _ = opp_key
    ok = (
        len(perpendicular) == 1
        and len(opposite) == 1
        and perpendicular[perp_key] == 24
        and opposite[opp_key] == 6
        and s_perp == -11
        and n_perp == 14
        and s_opp == -20
        and simplify(c_perp - (-88) / (CELL.N * (CELL.N**2 - 1) ** 3)) == 0
        and simplify(c_perp.subs(CELL.N, 3) + Rational(11, 192)) == 0
        and simplify(c_perp / c_opp - Rational(11, 20)) == 0
        and shells == {(0, 0, 0): 6, (0, 0, 1): 12, (0, 1, 1): 6}
        and normal_shells == {(0, 0, 1): 6}
    )
    return ok, (
        "the cube's 24 ordered perpendicular pairs all give S_4 = -11 over 14 histories, "
        "c_4,perp = -88/(N(N^2-1)^3) = -11/192 at N = 3, against the 6 opposite pairs' "
        "S_4 = -20 over 24 histories and -160/(N(N^2-1)^3) = -5/48. The ratio is exactly "
        "11/20 at every rank. This is a fourth-order primitive coefficient the corpus does not "
        "record. Its records are 6 at shell (0,0,0), 12 at (0,0,1) and 6 at (0,1,1) -- 24 in "
        "all, max |displacement| 1, so the OPERATOR is range-1 (an earlier form of this check "
        "said range-2, having measured the carrier projection, which inherits psi's own "
        "displacement content). It is still NOT the dictionary's rotation row: this channel's "
        "entry is H_[(12),(13)] = -conj(d_2) d_3 against the recorded +conj(d_n) d_m, which are "
        "minus the conjugate of one another -- different off-diagonal structures. That, not "
        "range, is why its carrier projection lies outside the four-shape span"
    )


@sealed.check(
    "the in-plane transfer is order eight, not four, in the primitive channel",
    "C2; G3 off-axis channel route",
)
def _():
    # The off-axis route's step 2 asks for the in-plane nearest-neighbour
    # transfer -- two COPLANAR edge-sharing plaquettes -- through the same
    # cellular machinery. It is not reachable there, and the reason is
    # geometric rather than a matter of effort.
    #
    # c_prim completes a CLOSED cell: every edge in exactly two faces with
    # opposite orientations, and the order is r = faces - 2. So a fourth-order
    # completion needs a closed cell of exactly six unit squares, which on the
    # cubic lattice is the unit cube alone -- and the unit cube has no coplanar
    # face pair at all. The smallest closed cell that carries one is the 1x2x1
    # box, whose surface is ten unit squares, giving r = 8.
    #
    # Recorded so the route is not planned around a step that cannot be taken
    # in this channel: the fourth-order in-plane record has to come from the
    # folded/linked or adjoint terms cellular's own scope note excludes.
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def faces_of_box(dims):
        out = []
        for n in range(3):
            i, j = (n + 1) % 3, (n + 2) % 3
            for side, lo in ((+1, dims[n]), (-1, 0)):
                for u in range(dims[i]):
                    for v in range(dims[j]):
                        base = [0, 0, 0]
                        base[n], base[i], base[j] = lo, u, v
                        base = tuple(base)
                        step = [tuple(base[c] + e[i][c] for c in range(3))]
                        step.append(tuple(step[0][c] + e[j][c] for c in range(3)))
                        cyc = (base, step[0], step[1], tuple(base[c] + e[j][c] for c in range(3)))
                        oriented = cyc if side > 0 else (cyc[0], cyc[3], cyc[2], cyc[1])
                        out.append((oriented, n, side))
        return out

    report = {}
    for name, dims in (("cube", (1, 1, 1)), ("1x2x1", (1, 2, 1))):
        meta = faces_of_box(dims)
        cell = CELL.Cell(name, tuple(m[0] for m in meta))  # raises unless closed and coherent
        coplanar = sum(
            1
            for x in range(len(meta))
            for y in range(x + 1, len(meta))
            if meta[x][1] == meta[y][1]
            and meta[x][2] == meta[y][2]
            and len(
                {frozenset(ed) for ed in CELL._face_edges(cell.faces[x])}
                & {frozenset(ed) for ed in CELL._face_edges(cell.faces[y])}
            )
            == 1
        )
        report[name] = (len(cell.faces), len(cell.faces) - 2, coplanar)
    ok = report["cube"] == (6, 4, 0) and report["1x2x1"] == (10, 8, 4)
    return ok, (
        f"(unit faces, r, coplanar edge-sharing pairs): {report}. Both validate as closed "
        "coherently oriented cells, so the count is the geometry and not a construction "
        "artefact. A fourth-order primitive completion needs six unit faces, which is the unit "
        "cube, which has NO coplanar pair; the smallest closed cell that has one is the 1x2x1 "
        "box at r = 8. So the in-plane nearest-neighbour transfer is order eight in this "
        "channel, and the fourth-order in-plane record must come from the folded/linked or "
        "adjoint terms that cellular's scope note excludes -- not from extending this module"
    )
