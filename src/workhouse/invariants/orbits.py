"""The fourth-order kernel as six amplitudes.

Every check here decomposes the kernel exactly, over the whole zone, with no
tolerance: the shape ansatz cleared of its ``1/q`` is a linear system over
Laurent polynomials in ``z_j = exp(i k_j)``, so the coefficients are solved for
rather than fitted. See ``workhouse.kernel_orbits``.

The point of the decomposition is that the 189 records carry only six distinct
weight magnitudes, one per cubic orbit, and in terms of those six amplitudes
the whole shape table is closed form. Nothing here adjudicates C2; the last two
checks put both sides in the same basis, which is the opposite of preferring
one.
"""

from __future__ import annotations

from fractions import Fraction

from .. import constants as K
from .. import kernel_orbits as KO
from ..channel_ledger import beta_formula
from ..payloads import _eval_fraction as _eval
from ..payloads import b_evaluator, kernel_constants, kernel_records
from ._core import _suite

orbit = _suite("fourth-order kernel orbits")

_LEDGER = "C2; G14; OFF_AXIS_LEDGER (maintainer, WORK_SINCE_2026-08)"


def _shell(d):
    return tuple(sorted(abs(v) for v in d))


@orbit.check(
    "the shape coefficients are solved, not fitted: A = 5/48, B = D = 0 exactly",
    _LEDGER,
)
def _():
    # kernel_comparison fits at four points of the zone with condition number
    # 45.8 -- the v10a.26 transcript's own procedure, and the reason every
    # non-axial number in the dispute is a float. Clearing the 1/q turns the
    # ansatz into a linear system over Laurent polynomials in z_j, which has an
    # exact solution over the WHOLE zone or none at all.
    co, residual = KO.coefficients(kernel_records())
    ok = (
        co["A"] == Fraction(5, 48)
        and co["B"] == 0
        and co["D"] == 0
        and co["C"] == kernel_constants()["C_shp"]
        and not residual
    )
    return ok, (
        f"A = {co['A']}, B = {co['B']}, D = {co['D']}, C = {co['C']}, with the residual "
        f"Laurent polynomial identically zero ({len(residual)} nonzero terms). The exact "
        "solve reproduces the registry's C_shp -- itself computed from four parity points -- "
        "over the whole zone, so the four-shape form is not an artefact of where the "
        "transcript sampled"
    )


@orbit.check("the 189 records carry exactly six weight magnitudes", _LEDGER)
def _():
    by = KO.orbits(kernel_records())
    sizes = sorted(len(g) for g in by.values())
    mags = KO.orbit_magnitudes(kernel_records())
    amps = KO.amplitudes(kernel_records())
    registered = {
        "u": K.X_QUANTUM,
        "u2": K.U2_ORBIT,
        "rho": K.RHO_ORBIT,
        "pi": K.PI_ORBIT,
        "nu": K.NU_ORBIT,
        "sigma": K.SIGMA_ORBIT,
    }
    ok = (
        len(by) == 6
        and sizes == [3, 6, 12, 12, 24, 132]
        and sum(sizes) == 189
        and all(abs(amps[n]) == mags[n] for n in amps)
        and amps == registered
    )
    u = amps["u"]
    return ok, (
        f"orbit sizes {sizes} summing to {sum(sizes)}; amplitudes in units of "
        f"u = {u}: "
        + ", ".join(f"{n} = {amps[n] / u}" for n in ("u", "u2", "rho", "pi", "nu"))
        + f", sigma = {amps['sigma'] / u}. Each orbit's amplitude, read off its own shape "
        "contribution, equals the weight its records carry up to sign -- which is the "
        "statement that an orbit really is one amplitude and not a group of records that "
        "happen to be near each other. All six are registered by value, so each is reachable "
        "from its own rational through `workhouse search` -- the join keys of this corpus are "
        "exact rationals, and RHO_ORBIT and PI_ORBIT are the two the whole of C2 reduces to"
    )


@orbit.check("every orbit's carrier projection is closed form in e1, e2, e3", _LEDGER)
def _():
    # Not a fit and not a table: five of the six follow from the orbit's
    # displacement set in two lines. With s_j = 4 sin^2(k_j/2), n the plane's
    # normal and {i, j} its own axes,
    #
    #   on-site   S_P = sigma                  -> sigma * sum_n s_n = sigma e1
    #   normal    S_P = nu (2 - s_n)           -> nu sum_n s_n (2 - s_n)
    #                                             = nu (2 e1 - e1^2 + 2 e2)
    #   in-plane  S_P = pi ((2 - s_i)+(2 - s_j))  = pi (4 - e1 + s_n)
    #                                             -> pi (4 e1 - 2 e2)
    #   doubled   S_P = u2 (2 - s_i)(2 - s_j)  -> u2 (4 e1 - 4 e2 + 3 e3)
    #   rotation  S_PQ = -eps_P eps_Q rho dbar_{n(Q)} conj(dbar_{n(P)}), so the
    #             carrier kills the phases outright:
    #             T = -rho sum_{m != n} s_m s_n = -2 rho e2
    #
    # -- using T = sum_P s_{n(P)} S_P for the diagonal orbits, since
    # |psi_P|^2 = s_{n(P)}. The skeleton's displacement set is larger and its
    # row is solved from its records; its residual is zero like the rest.
    recs = kernel_records()
    amps = KO.amplitudes(recs)
    groups = KO.orbit_groups(recs)
    ok = all(
        KO.bloch(groups[n]) == {e: amps[n] * c for e, c in KO.symmetric(**f).items()}
        for n, f in KO.CLOSED_FORMS.items()
    )
    return ok, (
        "T = "
        + " + ".join(f"{n}*({KO.CLOSED_FORMS[n]})" for n in ("sigma", "nu", "pi"))
        + f" + u2*({KO.CLOSED_FORMS['u2']}) + rho*({KO.CLOSED_FORMS['rho']}) + "
        f"u*({KO.CLOSED_FORMS['u']}), each an exact Laurent identity on that orbit's own "
        "records. Collecting: A = -nu - 4u, D = 3*u2 - 6u, 4C = 2nu - 2pi - 4*u2 - 2rho + 12u, "
        "and B = 0 because NO orbit produces the e1*e2 monomial at all. Substituting u2 = 2u "
        "and nu = -(5/48 + 4u) gives C = -5/96 - u - (rho + pi)/2. The master formula is "
        "derived from the six displacement sets, not fitted to the kernel"
    )


@orbit.check("A = 5/48 forces the normal amplitude: nu = -(5/48 + 4u)", _LEDGER)
def _():
    a = KO.amplitudes(kernel_records())
    ok = a["nu"] == -(Fraction(5, 48) + 4 * a["u"])
    return ok, (
        f"nu = {a['nu']} = -(5/48 + 4u) with u = {a['u']}. Only two orbits carry A -- the "
        f"skeleton at -4u and the normal hop at -nu -- so the agreed axial value fixes the "
        "normal amplitude completely once the skeleton unit is known. The normal channel is "
        "not independently disputed: it is a consequence of A"
    )


@orbit.check("C_shp = -5/96 - u - (rho + pi)/2, exactly", _LEDGER)
def _():
    a = KO.amplitudes(kernel_records())
    predicted = Fraction(-5, 96) - K.X_QUANTUM - (K.RHO_ORBIT + K.PI_ORBIT) / 2
    ok = predicted == kernel_constants()["C_shp"] == K.C_SHP_HISTORICAL and (
        a["u"],
        a["rho"],
        a["pi"],
    ) == (K.X_QUANTUM, K.RHO_ORBIT, K.PI_ORBIT)
    return ok, (
        f"three signed amplitudes reproduce C_shp = {predicted} exactly. In units of u: "
        f"rho = {a['rho'] / a['u']}, pi = {a['pi'] / a['u']}. The -5/96 is -A/2 from the "
        "normal hop, already fixed by A = 5/48; the on-site amplitude enters c_0 alone. So "
        "the whole off-axis dispute is three numbers, not a seven-row table"
    )


@orbit.check("the tier collapse is one identity: D = -6u + 3*u2 with u2 = 2u", "G14; " + _LEDGER)
def _():
    # G14's recorded form of the collapse is two integer cancellations across
    # displacement blocks. In the orbit basis it is smaller than that. D is
    # carried by exactly two orbits, and the doubled orbit's amplitude is
    # exactly twice the skeleton's -- so D vanishes identically in u, for any
    # value of u. It is not a numerical coincidence between sectors.
    recs = kernel_records()
    by = KO.orbits(recs)
    a = KO.amplitudes(recs)
    skeleton = by[max(by, key=lambda m: len(by[m]))]
    doubled = by[sorted(m for m in by if len(by[m]) == 12)[0]]
    d_skel = KO.coefficients(skeleton)[0]["D"]
    d_two = KO.coefficients(doubled)[0]["D"]
    ok = (
        a["u2"] == 2 * a["u"]
        and d_skel == -6 * a["u"]
        and d_two == 3 * a["u2"]
        and d_skel + d_two == 0
        and all(KO.coefficients(by[m])[0]["D"] == 0 for m in by if len(by[m]) not in (132, 12))
    )
    return ok, (
        f"D = {d_skel / a['u']}u from the 132-record skeleton and {d_two / a['u']}u from the "
        f"12-record doubled orbit, whose amplitude is u2 = {a['u2'] / a['u']}u exactly. Every "
        "other orbit has D = 0. So D = -6u + 3*u2 = 0 holds for ANY u -- the whole content of "
        "the e_3 collapse is that the same-plane (0,1,1) in-plane orbit carries exactly twice "
        "the generic weight. That single equality is what a mechanism has to explain"
    )


@orbit.check("u2 = 2u is the cross term of a perfect square", "G14; " + _LEDGER)
def _():
    # The one equality the e_3 collapse reduces to, explained. Take a plane
    # with own axes {i, j} and normal n, and write X = z_i + z_i^{-1} = 2 cos
    # k_i and likewise Y, Z. Everything the plane sends to itself beyond
    # nearest neighbour is sixteen records:
    #
    #   (0,0,2), amplitude u    ->  (X^2 - 2) + (Y^2 - 2)
    #   (0,1,1) mixed, u        ->  (X + Y) Z
    #   (0,1,1) in-plane, u2    ->  (u2/u) X Y
    #
    # and their sum is u[(X + Y)(X + Y + Z) - 4] if and only if the cross term
    # is 2XY -- that is, if and only if u2 = 2u. So the doubling is not an
    # independent coincidence: it is the condition for the same-plane
    # long-range symbol to be a product rather than an inhomogeneous
    # quadratic, and D = 0 in that sector follows.
    recs = kernel_records()
    u = KO.amplitudes(recs)["u"]
    blocks = KO.same_plane_long_range(recs)
    ok = len(blocks) == 3 and all(
        len(g) == 16 and g == KO.perfect_product(plane, u) for plane, g in blocks.items()
    )
    # and the factorisation is what kills e_3 there
    same = [
        ((ip, op, d), w)
        for (ip, op, d), w in recs
        if ip == op and any(d) and sorted(abs(x) for x in d) != [0, 0, 1]
    ]
    d_same = KO.coefficients(same)[0]["D"]
    cross, cross_form = KO.cross_plane_skeleton(recs, u)
    d_cross = KO.coefficients(cross)[0]["D"]
    ok = ok and d_same == 0 and d_cross == 0 and KO.bloch(cross) == cross_form
    return ok, (
        "for each of the three planes the sixteen same-plane records at shells (0,0,2) and "
        "(0,1,1) sum to exactly u[(X+Y)(X+Y+Z) - 4] with X = 2 cos k_i, Y = 2 cos k_j, "
        "Z = 2 cos k_n. The (0,0,2) records supply X^2 + Y^2, the mixed (0,1,1) records "
        "supply (X+Y)Z, and the in-plane (0,1,1) records supply the cross term -- which "
        "completes (X+Y)^2 only at coefficient 2, i.e. only if u2 = 2u. With the product "
        f"form, D = {d_same} in the same-plane sector and D = {d_cross} in the 96-record "
        "cross-plane skeleton, separately. So the e_3 collapse is not a cancellation between "
        "sectors either: each sector is free of e_3 on its own. The same-plane one is free "
        "of it because its symbol factorises; the cross-plane one because it is "
        "-2u e_2 (e_1 - 8) exactly -- pure e_2 times a linear factor, which is also why it "
        "carries no A"
    )


@orbit.check("B = 0 is unpopulated, not cancelled", "G14; " + _LEDGER)
def _():
    # G14 records the B-cancellation as (+1, +1, -2) coupling the translation
    # sector to the 120-record rotation sector. In the orbit basis it is
    # (+1, +1, -1, -1) INSIDE the skeleton orbit: each same-plane block is
    # cancelled by the off-plane block of the same displacement shell, at
    # unit weight, within a single amplitude. Nothing couples across orbits.
    recs = kernel_records()
    by = KO.orbits(recs)
    a = KO.amplitudes(recs)
    skeleton = by[max(by, key=lambda m: len(by[m]))]

    blocks: dict[str, list] = {}
    for key, w in skeleton:
        ip, op, d = key
        same = ip == op
        blocks.setdefault(f"{'same' if same else 'off'}{_shell(d)}", []).append((key, w))
    weights = {name: KO.coefficients(g)[0]["B"] / a["u"] for name, g in blocks.items()}
    carrying = {n: v for n, v in weights.items() if v}
    paired = all(
        weights.get(f"same{sh}", 0) + weights.get(f"off{sh}", 0) == 0
        for sh in {n[4:] for n in weights}
    )
    ok = (
        sum(weights.values()) == 0
        and paired
        and set(carrying.values()) == {1, -1}
        and all(KO.coefficients(by[m])[0]["B"] == 0 for m in by)
    )
    return ok, (
        "no orbit's closed form contains the e1*e2 monomial, so at orbit level B is "
        f"unpopulated and there is nothing to cancel. Inside the skeleton, B/u by "
        f"displacement block is {carrying}; every other block is 0, and every orbit has "
        "B = 0. That inner cancellation is same-plane against off-plane at "
        "the SAME shell, at unit weight: (0,0,2) gives +1 and -1, (0,1,1) gives +1 and -1. So "
        "the q e_2 collapse involves one amplitude and one displacement shell at a time -- it "
        "does not couple the translation sector to the rotation sector as a whole, and the "
        "(+1, +1, -2) recorded in G14 is that pair with the two rotation blocks summed. But "
        "the displacement grouping is the wrong one: at orbit level the monomial is never "
        "generated, so B needs no mechanism at all"
    )


@orbit.check(
    "RETRACTED: B_3 - beta_historical = 25/64 is a forbidden substitution, not an exact branch",
    "C2; walled-Brauer eps-sector; " + _LEDGER,
)
def _():
    # RETRACTED 2026-08-30, same day it was added. The check as written said
    # "the balanced branch is exact" and the value was registered as
    # K.C_SHP_CONTINUATION_SHIFTED, as though B_3^bal were an established quantity.
    #
    # It is not. payloads.b_evaluator() at N = 3 returns exactly
    # channel_ledger.beta_formula(3) = P17(9)/(3 R20(9)), and
    # GLUEBALL_DETAILED_FORMULA_2026-08-20_v3.1.md says at line ~1511:
    # "The compact beta_N formula is not to be substituted at N=3; use the
    # separate exact SU(3) value." So the 25/64 is the gap between the
    # historical value and a substitution the corpus explicitly forbids, at a
    # rank where the continuation route is separately known to be closed (D34
    # carries (z-9)^3, a pole of order exactly 3 -- see the "at N = 6" check in
    # the off-axis channel ledger suite).
    #
    # The arithmetic was never wrong and is kept, because the relation is real
    # and is what the register's DELTA_BETA_3 records. What is withdrawn is the
    # word "exact branch" and any reading of C_historical + 25/1024 as an
    # established balanced value of C_shp. The pre-existing check "the N=3
    # continuation shift is exactly 25/64, with two exact corollaries" already
    # stated this correctly, including that whether the shift is derived or
    # defined as a difference is open; this check duplicated it with a stronger
    # claim and no additional evidence.
    beta = kernel_constants()["beta"]
    b3 = _eval(b_evaluator(), 3)
    delta_beta = b3 - beta
    substitution = beta_formula(3)
    ok = (
        delta_beta == Fraction(25, 64)
        and b3 == substitution  # the whole point: B_3 IS the forbidden substitution
        and beta == K.BETA_PEN_3
        # the withdrawn value is kept and read here, so the retraction is
        # anchored to the number it withdraws rather than floating free
        and K.C_SHP_HISTORICAL + Fraction(25, 1024) == K.C_SHP_CONTINUATION_SHIFTED
    )
    return ok, (
        f"FINDING: b_evaluator(3) = {b3} is bit-identical to beta_formula(3) = P17(9)/(3 R20(9)), "
        "the substitution GLUEBALL_DETAILED_FORMULA v3.1 forbids at N = 3. Its gap to the "
        f"historical beta = {beta} is exactly 25/64, which is the register's DELTA_BETA_3 and "
        "is a true relation among recorded quantities. It is NOT an exact balanced branch of "
        "C2, and C_historical + 25/1024 is NOT an established value of C_shp: no direct "
        "balanced contraction at N = 3 is held in this repository, and the continuation route "
        "to N = 3 is closed by a third-order pole. What the exceptional ranks do show is that "
        "the determinant sector does not reach B elsewhere -- SU(5) ships 895,524 pairs with "
        "zero determinant sectors, and SU(6)'s sole determinant orbit shifts the scalar by "
        "6/343 leaving A, B and the bandwidth unchanged -- which is evidence about the "
        "mechanism, not a licence for the N = 3 substitution"
    )


@orbit.check(
    "the on-site orbit IS the momentum-independent channel",
    "U5; C2; C10; GCSG SU(6) certificate; " + _LEDGER,
)
def _():
    # Needed to read the exceptional-rank record in this basis. The on-site
    # orbit's carrier projection is exactly sigma*e_1, so eps = T/q = sigma is
    # CONSTANT over the zone: it moves every band value together and carries no
    # A, B, C or D. Conversely, a correction reported as "momentum-independent"
    # or "a scalar shift" is, in this basis, an on-site-orbit shift and nothing
    # else. That is what makes the SU(6) determinant record readable here.
    recs = kernel_records()
    groups = KO.orbit_groups(recs)
    amps = KO.amplitudes(recs)
    co, residual = KO.coefficients(groups["sigma"])
    exact = KO.bloch(groups["sigma"]) == {e: amps["sigma"] * c for e, c in KO.E1.items()}
    ok = (
        exact
        and co["A"] == co["B"] == co["C"] == co["D"] == 0
        and co["c0"] == amps["sigma"]
        and not residual
    )
    return ok, (
        f"T_on-site = sigma * e_1 exactly, so eps = T/q = sigma = {amps['sigma']} is constant "
        "over the zone and A = B = C = D = 0. The converse is the useful direction: a "
        "determinant correction recorded as a pure scalar shift IS an on-site-orbit shift. "
        "Reading the exceptional ranks that way -- SU(6)'s sole determinant orbit shifts q, X, "
        "M and R by 6/343 with A, B and the bandwidth unchanged, and SU(5) has no determinant "
        "sector at all -- says the eps-sector stays inside the on-site orbit wherever it has "
        "been computed independently. N = 3 is the one rank where it does not"
    )


@orbit.check(
    "PREDICTION: the eps-sector at N=3 is Delta(rho + pi) = -25/512 and nothing else",
    "U5; C2; C10; G3; " + _LEDGER,
)
def _():
    # A falsifiable consequence of the orbit basis, not a measurement. Two
    # inputs, both recorded elsewhere:
    #
    #   (i)  Delta A_3 = 0 -- both sides of C2 agree on alpha = 5/12, hence
    #        A = 5/48. Since A = -nu - 4u exactly, this FORCES Delta nu = -4 Delta u.
    #   (ii) the primitive cube-completion channel is link-balanced (one U and
    #        one U-dagger on every link, so nu_l = 0) and therefore eps-blind.
    #        That channel is the normal orbit, so Delta nu = 0, hence Delta u = 0,
    #        and since u2 = 2u holds exactly in both recorded kernels, Delta u2 = 0.
    #
    # Then C = -5/96 - u - (rho + pi)/2 leaves the eps-sector only one place to
    # go. With Delta beta_3 = +25/64 (balanced minus historical) and
    # C_shp = (beta - 2 alpha)/16, Delta C = +25/1024 and therefore
    # Delta(rho + pi) = -2 Delta C = -25/512.
    #
    # This does NOT adjudicate C2 and does not assume the forbidden N = 3
    # substitution: it says what a direct balanced contraction at N = 3, if one
    # is ever computed, must produce.
    delta_c = Fraction(25, 1024)
    delta_sum = -2 * delta_c
    hist_sum = K.RHO_ORBIT + K.PI_ORBIT
    predicted = hist_sum + delta_sum
    # the prediction has to be consistent with the recorded historical value
    consistent = (
        Fraction(-5, 96) - K.X_QUANTUM - hist_sum / 2 == K.C_SHP_HISTORICAL
        and -(Fraction(5, 48) + 4 * K.X_QUANTUM) == K.NU_ORBIT
        and K.U2_ORBIT == 2 * K.X_QUANTUM
    )
    ok = consistent and delta_sum == Fraction(-25, 512)
    return ok, (
        f"given Delta A_3 = 0 and an eps-blind primitive channel, Delta u = Delta u2 = "
        f"Delta nu = 0 and the whole eps-sector effect on the N = 3 fourth-order shape is "
        f"Delta(rho + pi) = {delta_sum}. Historical rho + pi = {hist_sum}; a direct balanced "
        f"contraction at N = 3 must therefore give {predicted}. FALSIFIER: any direct N = 3 "
        "balanced contraction whose six orbit amplitudes differ from the historical ones "
        "anywhere except in rho + pi, or whose rho + pi shift is not exactly -25/512. This is "
        "a prediction about a computation nobody here has run; it prefers neither side of C2, "
        "and it does not rest on the forbidden P17/R20 substitution at N = 3 -- only on "
        "Delta beta_3, which the register records independently"
    )


@orbit.check(
    "FINDING: the cold kernel is the same six orbits with rho and pi sign-flipped",
    "C2; G3 step 1; " + _LEDGER,
    tier=2,
)
def _():
    # G3's step 1 is recorded as unanswerable -- "NO recorded per-record
    # v10a.26 kernel exists". One does exist, in
    # runs/g3_kernel_record_dump_2026-08-28/, and it decomposes in this basis.
    # Float weights, so T2; the tolerances below are the dump's own, whose
    # within-orbit spread is under 1e-12 relative.
    hist = KO.amplitudes(kernel_records())
    cold = KO.cold_amplitudes()
    sizes = sorted(n for _, n, _ in KO.cold_orbits())
    u, hu = cold["u"], float(hist["u"])
    c_cold = -5 / 96 - u - (cold["rho"] + cold["pi"]) / 2
    ok = (
        sizes == [3, 6, 12, 12, 24, 132]
        and abs(cold["u2"] / u - 2) < 1e-9
        and abs(cold["nu"] + (5 / 48 + 4 * u)) < 1e-9 * abs(cold["nu"])
        and cold["rho"] * float(hist["rho"]) < 0
        and cold["pi"] * float(hist["pi"]) < 0
        and abs(c_cold - K.C_SHP_NEW_NUM) < 1e-12
    )
    return ok, (
        f"the v10a.26 record dump has the same six orbit sizes {sizes}, satisfies u2 = 2u to "
        f"{abs(cold['u2'] / u - 2):.1e} and nu = -(5/48 + 4u) to "
        f"{abs(cold['nu'] + (5 / 48 + 4 * u)) / abs(cold['nu']):.1e}, and its skeleton unit is "
        f"r = {u / hu:.9f} times the historical one. Its rho and pi are OPPOSITE IN SIGN: "
        f"rho/u = {cold['rho'] / u:.6f} against {float(hist['rho'] / hist['u']):.6f}, "
        f"pi/u = {cold['pi'] / u:.6f} against {float(hist['pi'] / hist['u']):.6f}. The master "
        f"formula then returns C = {c_cold:.15g} against the transcript's own four-point fit "
        f"{K.C_SHP_NEW_NUM!r}, a gap of {abs(c_cold - K.C_SHP_NEW_NUM):.1e}. "
        "runs/g3_kernel_record_dump_2026-08-28/ already established the scale factor and the "
        "cross-plane sign flip through a four-point fit; what the exact orbit basis adds is "
        "that the SAME-PLANE nearest-neighbour block is not one disagreement but two -- six "
        "of its eighteen records are the normal orbit, which A = 5/48 fixes at "
        "nu = -(5/48 + 4u) in BOTH kernels and which therefore cannot disagree freely, and "
        "the remaining twelve are the in-plane orbit, which flips sign exactly as the "
        "cross-plane one does. So the two kernels agree on all six orbits, on the normalized "
        "shape table, and on both tier-collapse identities, and their free disagreement is "
        "two sign-flipped amplitudes and one scale. This does not decide C2; it says the "
        "disagreement is not a re-weighting"
    )
