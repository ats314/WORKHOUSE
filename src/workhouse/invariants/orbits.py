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

# The Hodge-form checks at the end of the module; named here because the
# corrected prediction rests on one of them.
_HODGE = "C2; G14; U5; GLUEBALL v3.1 §6.1-6.2, §7; THM_FLUX Prop. 2; " + _LEDGER
_SQUARE = "the 144 agreed records are u S_sq^2, the shared-link adjacency squared"
_FORM = (
    "H4 = -nu~(L_up - 2) + u S_sq^2 - pi~ S_sq + sigma~ - 2 C_shp R exactly: "
    "C_shp is the coefficient of the one non-Hodge operator"
)


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


@orbit.check(
    "C_shp = -5/96 - u - (rho + pi)/2, exactly",
    _LEDGER,
    rests_on=("every orbit's carrier projection is closed form in e1, e2, e3",),
)
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
    "CORRECTED PREDICTION: the eps-sector at N=3 is Delta(rho + pi~) = -25/512; "
    "u is NOT constrained",
    "U5; C2; C10; G3; " + _LEDGER,
    rests_on=(_FORM,),
)
def _():
    # A falsifiable consequence of the orbit basis, not a measurement -- and a
    # correction, 2026-09-01, of the form this check carried since 2026-08-30.
    #
    # As first written it concluded "Delta u = Delta u2 = Delta nu = 0 and the
    # whole eps-sector effect is Delta(rho + pi) = -25/512, and nothing else".
    # The step was: A = -nu - 4u, both sides agree A = 5/48, so Delta nu =
    # -4 Delta u; the primitive cube-completion channel is link-balanced and
    # eps-blind, "and that channel IS the normal orbit", so Delta nu = 0 and
    # hence Delta u = 0. The identification in quotes is false. The normal
    # orbit is nu = -5/48 - 4u: the primitive completion PLUS the diagonal
    # shadow of the two-hop sector u S_sq^2 (check "the 144 agreed records are
    # u S_sq^2 ..."). Eps-blindness of the primitive channel fixes nu~ = nu + 4u
    # = -5/48, which is the SAME statement as Delta A = 0 -- it constrains u not
    # at all. The two recorded kernels are the witness: both have nu~ = -5/48
    # exactly and their u differ by a factor of 4.13.
    #
    # What survives is the C-identity. In the Hodge form C = -5/96 - (rho +
    # pi~)/2 with pi~ = pi + 2u, so with Delta beta_3 = +25/64 and C_shp =
    # (beta - 2 alpha)/16, Delta C = +25/1024 and Delta(rho + pi~) = -25/512.
    # The number is unchanged; the quantity it constrains is rho + pi~, not
    # rho + pi, and u, u2, sigma~ are free. The former yields
    # RHO_PLUS_PI_BALANCED_N3_PREDICTED and DELTA_RHO_PLUS_PI_N3_PREDICTED are
    # withdrawn with the "nothing else" clause; their replacements follow.
    delta_c = Fraction(25, 1024)
    delta_sum = -2 * delta_c
    form = KO.hodge_form(KO.amplitudes(kernel_records()))
    hist_sum = K.RHO_ORBIT + form["pi~"]
    predicted = hist_sum + delta_sum
    # the cold witness -- nu~ = -5/48 with u 4.13x larger -- is the T2 check
    # "FINDING: the cold kernel has the same Hodge form ..."; this check stays exact
    consistent = (
        form["C"] == K.C_SHP_HISTORICAL
        and Fraction(-5, 96) - hist_sum / 2 == K.C_SHP_HISTORICAL
        and form["nu~"] == Fraction(-5, 48)
        and -8 * hist_sum == K.BETA_PEN_3
    )
    ok = consistent and delta_sum == Fraction(-25, 512)
    return (
        ok,
        (
            f"given Delta A_3 = 0 and an eps-blind primitive channel, nu~ = -5/48 is fixed and the "
            f"eps-sector's effect on the N = 3 fourth-order shape is Delta(rho + pi~) = "
            f"{delta_sum}: historical rho + pi~ = {hist_sum}, so a direct balanced contraction "
            f"at N = 3 must give rho + pi~ = {predicted}. RETRACTED from the 2026-08-30 form: "
            "'Delta u = Delta u2 "
            "= Delta nu = 0 ... and nothing else'. That rested on identifying the normal orbit "
            "with the primitive channel; the normal orbit is the primitive channel plus the -4u "
            "shadow of u S_sq^2, so Delta A = 0 constrains u not at all -- the two recorded "
            "kernels both have nu~ = -5/48 with u differing by a factor 4.13 (the T2 Hodge-form "
            "finding). In the register's terms the prediction is beta_bal = beta_pen + 25/64 "
            f"with beta_pen = -8 (rho + pi~) = {K.BETA_PEN_3}. "
            "FALSIFIER: any direct N = 3 balanced contraction whose nu~ is not -5/48, or whose "
            "rho + pi~ shift from the historical value is not exactly -25/512. It prefers neither "
            "side of C2 and does not rest on the forbidden P17/R20 substitution at N = 3 -- only "
            "on Delta beta_3, which the register records independently"
        ),
        {
            "RHO_PLUS_PI_REDUCED_BALANCED_N3_PREDICTED": predicted,
            "DELTA_RHO_PLUS_PI_REDUCED_N3_PREDICTED": delta_sum,
        },
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


# -- G3: the covariance sign test ---------------------------------------------
#
# The route recorded on G3 as untried: rho and pi flip sign together between
# the two kernels while nu does not, and "two orbits flipping together while a
# third does not" reads like a convention. Ask the question exactly. Symmetry
# is Hermiticity plus covariance under the cubic group O_h acting on plaquette
# CENTRES with the orientation character (PSI_SIGN read at the identity); a
# convention is a change of basis of the plane fibre alone. The first cannot
# fix any orbit's sign, and the second cannot reach the flip. So the flip is
# not a convention -- which does not say which kernel is right.

_SIGN_TEST = "C2; G3 covariance sign test; " + _LEDGER
_ORIENTED = "every orbit is separately Hermitian and cubic-covariant, so symmetry fixes no sign"
_REGAUGE = "no plane-basis convention flips rho or pi: only +-1 keeps the 144 agreed records"


@orbit.check(_ORIENTED, _SIGN_TEST)
def _():
    # Corner-based displacements are not what the cubic group rotates: the
    # geometric displacement is between plaquette centres, d + c(op) - c(ip).
    # With that, and the orientation character chi_g(P) = s_i s_j sgn(order),
    # every one of the six orbits is invariant under all 48 elements on its
    # own. Two controls show the two ingredients are load-bearing: without the
    # character the cross-plane orbits keep only 12 elements, and on the raw
    # corner-based d they keep only 6.
    recs = kernel_records()
    groups = KO.orbit_groups(recs)
    with_chi = {n: len(KO.covariant_elements(g)) for n, g in groups.items()}
    without_chi = {n: len(KO.covariant_elements(g, use_character=False)) for n, g in groups.items()}
    herm = {n: KO.is_hermitian(g) for n, g in groups.items()}
    swap = {n: KO.is_transposition_symmetric(g) for n, g in groups.items()}
    # the raw-d control: act on d as if it were the centre displacement
    raw = {
        n: sum(
            all(
                (KO.act_plane(g, ip)[0], KO.act_plane(g, op)[0], KO.act_vector(g, d)) in dict(grp)
                and dict(grp)[(KO.act_plane(g, ip)[0], KO.act_plane(g, op)[0], KO.act_vector(g, d))]
                == KO.act_plane(g, ip)[1] * KO.act_plane(g, op)[1] * w
                for (ip, op, d), w in grp
            )
            for g in KO.cubic_group()
        )
        for n, grp in groups.items()
        if n in ("u", "rho")
    }
    # and symmetry is linear: flipping rho alone, pi alone, or both, is still a
    # Hermitian covariant kernel, so all four sign patterns are admissible
    flips = {}
    for pattern in ((-1, 1), (1, -1), (-1, -1)):
        flipped = [
            (k, (pattern[0] if n == "rho" else pattern[1] if n == "pi" else 1) * w)
            for n, g in groups.items()
            for k, w in g
        ]
        flips[pattern] = KO.is_hermitian(flipped) and len(KO.covariant_elements(flipped)) == 48
    ok = (
        all(herm.values())
        and all(swap.values())
        and all(v == 48 for v in with_chi.values())
        and without_chi["u"] == without_chi["rho"] == 12
        and raw == {"u": 6, "rho": 6}
        and all(flips.values())
    )
    return ok, (
        "on plaquette-centred displacements Delta = d + c(op) - c(ip), with the orientation "
        "character chi_g(P) = s_i s_j sgn(order) -- PSI_SIGN read at the identity, i.e. the cube "
        f"boundary d_3 -- every orbit is invariant under all 48 elements of O_h: {with_chi}. "
        f"Each is Hermitian and each is symmetric under swapping input and output plane at fixed "
        "centre displacement, so which plane a dump calls the row cannot matter. Controls: without "
        f"the character the cross-plane orbits keep only {without_chi['u']} and "
        f"{without_chi['rho']} elements, and on the raw corner-based d they keep only "
        f"{raw['u']} and {raw['rho']}. "
        "Symmetry is linear, so the kernel with rho flipped, with pi flipped, and with both "
        "flipped is Hermitian and fully covariant too: all four sign patterns of (rho, pi) are "
        "admissible, and Hermiticity plus cubic covariance fix NO orbit's sign relative to the "
        "normal orbit. The sign test therefore cannot pick a side of C2 -- what it can do is "
        "decide whether the flip is a convention, which the next check does"
    )


@orbit.check(_REGAUGE, _SIGN_TEST, rests_on=(_ORIENTED,))
def _():
    # The conventions available in the plane basis are exactly the 48 signed
    # permutations of the fibre with k untouched: which plaquette is called
    # which, and which way round each is traversed. Both kernels agree, up to
    # one scale, on the 144 skeleton and doubled records. Only +-1 preserves
    # those, so no convention distinguishes the two bases -- and the flip
    # itself is out of reach anyway: pi is a same-plane orbit, which a
    # regauging cannot touch at all, and every diagonal regauging other than
    # +-1 flips exactly two of the three cross-plane pairs, which throws rho
    # (and the cross-plane skeleton with it) out of the cubic shape span.
    recs = kernel_records()
    groups = KO.orbit_groups(recs)
    amps = KO.amplitudes(recs)
    agreed = set(groups["u"]) | set(groups["u2"])
    keep = [g for g in KO.cubic_group() if agreed <= set(KO.regauge(recs, g))]
    identity = ((0, 1, 2), (1, 1, 1))
    minus = ((0, 1, 2), (-1, -1, -1))
    diagonal = [g for g in KO.cubic_group() if g[0] == (0, 1, 2)]
    cross = [r for r in groups["u"] if r[0][0] != r[0][1]]
    table = {}
    for g in diagonal:
        co_rho, res_rho = KO.coefficients(KO.regauge(groups["rho"], g))
        co_pi, res_pi = KO.coefficients(KO.regauge(groups["pi"], g))
        _, res_cross = KO.coefficients(KO.regauge(cross, g))
        table[g[1]] = (
            co_rho["C"] / amps["rho"],
            bool(res_rho),
            co_pi["C"] / amps["pi"],
            bool(res_pi),
            bool(res_cross),
        )
    trivial = {(1, 1, 1), (-1, -1, -1)}
    ok = (
        set(keep) == {identity, minus}
        and len(agreed) == 144
        and all(
            row[2] == Fraction(-1, 2) and not row[3]  # pi untouched by every regauging
            for row in table.values()
        )
        and all(
            table[s][0] == Fraction(-1, 2) and not table[s][1] and not table[s][4] for s in trivial
        )
        and all(table[s][1] and table[s][4] for s in table if s not in trivial)
    )
    return ok, (
        f"of the 48 fibre regaugings U S U^T (k untouched) exactly {len(keep)} preserve the 144 "
        "skeleton and doubled records both kernels agree on: the identity and -1. Every plane "
        "permutation moves a normal hop onto an in-plane displacement, and every diagonal "
        "orientation change other than +-1 flips two of the three cross-plane pairs. For the "
        "eight diagonal regaugings, (C_rho/rho, rho off-span, C_pi/pi, pi off-span, cross-skeleton "
        f"off-span) = {table}. So pi, a same-plane orbit, is untouched by every convention the "
        "plane basis has, and rho can only be flipped together with two-thirds of the cross-plane "
        "skeleton -- which leaves the cubic shape span entirely, so no cubic-covariant kernel in "
        "any plane-basis convention carries the historical skeleton with the cold sign of rho. "
        "FINDING: the (rho, pi) sign flip between the two kernels is not a basis convention. "
        "Combined with the previous check -- symmetry admits every sign pattern -- the two "
        "kernels are two different Hermitian, cubic-covariant operators, and C2 is a disagreement "
        "about which fourth-order operator the theory produces, not about how to write one down"
    )


@orbit.check(
    "FINDING: the cold kernel carries the same orientation character, so its flips are real",
    _SIGN_TEST,
    tier=2,
    rests_on=(_ORIENTED, _REGAUGE),
)
def _():
    # The regauging result applies to the cold kernel only if it is in the same
    # basis. Run the identical symmetry test on the v10a.26 dump: same centred
    # displacements, same character. Float weights, so T2; a record matches its
    # image within 1e-9 relative, three orders looser than the dump's own
    # within-orbit spread.
    tol = 1e-9
    cold = {n: g for _, n, g in KO.cold_orbits()}
    herm = {n: KO.is_hermitian(g, tol) for n, g in cold.items()}
    swap = {n: KO.is_transposition_symmetric(g, tol) for n, g in cold.items()}
    with_chi = {n: len(KO.covariant_elements(g, tol=tol)) for n, g in cold.items()}
    without_chi = {
        n: len(KO.covariant_elements(g, use_character=False, tol=tol)) for n, g in cold.items()
    }
    hist_without = {
        len(g): len(KO.covariant_elements(g, use_character=False))
        for g in KO.orbit_groups(kernel_records()).values()
    }
    ok = (
        sorted(cold) == [3, 6, 12, 24, 132]
        and all(herm.values())
        and all(swap.values())
        and all(v == 48 for v in with_chi.values())
        and without_chi == hist_without
    )
    return ok, (
        f"the v10a.26 dump's orbits (by size) are Hermitian to {tol:.0e} relative and invariant "
        f"under all 48 elements of O_h with the SAME orientation character: {with_chi}; without "
        f"the character they keep {without_chi}, exactly the historical pattern {hist_without}. "
        "Both kernels are therefore written in the same plane basis up to the sign +-1 that fixes "
        "everything, and the previous check's conclusion transfers: the opposite signs of rho "
        "and pi are not a convention of either computation. The route recorded on G3 as the "
        "covariance sign test closes here with a negative result -- it eliminates 'convention' "
        "as the explanation of C2 and leaves the independent cross-amplitude computation as the "
        "only open route. Nothing here prefers either side"
    )


# -- the Hodge form of the kernel ---------------------------------------------
#
# The corpus's own algebra, GLUEBALL v3.1 §6.2 and THM_FLUX Prop. 2: the signed
# shared-edge square adjacency satisfies S_sq + 4I = L_down, the cube boundary
# gives L_up, L_down L_up = 0, and every polynomial in the two acts on the
# carrier by a scalar. What was not recorded: BOTH fourth-order kernels ARE such
# a polynomial, plus one operator -- the cross-plane half of S_sq -- and the
# coefficient of that one operator is -2 C_shp exactly.


@orbit.check(_SQUARE, _HODGE)
def _():
    # Three exact facts. (i) The unit shared-link pattern -- the rho orbit's
    # sign structure on the 24 cross-plane pairs plus the pi orbit's on the 12
    # coplanar ones -- is exactly the off-diagonal of L_down = d_1 d_1^dagger,
    # so it is S_sq = L_down - 4I. (ii) Its square, as an operator product on
    # records, is the skeleton plus the doubled orbit at unit weight, plus a
    # diagonal shadow: -4 on the six normal keys, -2 on the twelve in-plane
    # keys, +12 on site. That is the whole of the 144 agreed records AND the
    # exact -4u the normal orbit carries beyond -5/48. (iii) L_down annihilates
    # the cube-boundary carrier, so S_sq psi = -4 psi and S_sq^2 psi = 16 psi:
    # the entire two-hop sector is a constant on the carrier.
    recs = kernel_records()
    groups = KO.orbit_groups(recs)
    amps = KO.amplitudes(recs)
    u = amps["u"]
    pattern = {k: w / abs(amps["rho"]) for k, w in groups["rho"]}
    pattern.update({k: w / abs(amps["pi"]) for k, w in groups["pi"]})
    ident = KO.identity()
    s_sq = KO.combine((1, KO.down_laplacian()), (-4, ident))
    square = KO.compose(s_sq, s_sq)
    agreed = dict(groups["u"]) | dict(groups["u2"])
    shadow = {k: v for k, v in square.items() if k not in agreed}
    shadow_classes: dict = {}
    for (ip, op, d), v in shadow.items():
        key = ("same" if ip == op else "cross", tuple(sorted(abs(x) for x in d)))
        shadow_classes.setdefault(key, set()).add(v)
    ok = (
        pattern == s_sq
        and all(square.get(k) == w / u for k, w in agreed.items())
        and len(agreed) == 144
        and shadow_classes
        == {("same", (0, 0, 1)): {Fraction(-4), Fraction(-2)}, ("same", (0, 0, 0)): {Fraction(12)}}
        and {
            v
            for (ip, op, d), v in shadow.items()
            if ip == op and any(d) and d[KO.NORMAL_OF[ip]] == 0
        }
        == {Fraction(-2)}
        and {v for (ip, op, d), v in shadow.items() if ip == op and d[KO.NORMAL_OF[ip]] != 0}
        == {Fraction(-4)}
        and KO.acts_as(KO.down_laplacian(), {})
        and KO.acts_as(s_sq, KO._mono((0, 0, 0), -4))
        and KO.acts_as(square, KO._mono((0, 0, 0), 16))
        and amps["nu"] + 4 * u == Fraction(-5, 48)
    )
    return ok, (
        "the unit sign pattern of the rho and pi orbits IS the off-diagonal of L_down = d_1 "
        "d_1^dagger (diagonal 4), i.e. S_sq = L_down - 4I, exactly. Its operator square "
        "reproduces every one of the 144 skeleton and doubled records at weight u = "
        f"{u}, with u2 = 2u as the two coplanar paths, and nothing else off the "
        "nearest-neighbour shell; its diagonal shadow is -4 on the normal keys, -2 on the "
        "in-plane keys and +12 on site -- so nu + 4u = -5/48 is the primitive cube completion "
        "with the shadow removed, and the -4u the normal orbit carries is not a correction to "
        "the cube channel but the two-hop sector's own diagonal. L_down psi = 0 for the "
        "cube-boundary carrier (d_1^dagger d_2^dagger = 0), hence S_sq psi = -4 psi and "
        "S_sq^2 psi = 16 psi: the whole two-hop sector, 144 records and their shadow, is the "
        "constant 16u on the carrier. That is why the 4.13x disagreement of the two kernels "
        "on u is invisible in C"
    )


@orbit.check(_FORM, _HODGE, rests_on=(_SQUARE,))
def _():
    # The identity, as records, on all 189: with the reduced amplitudes
    # nu~ = nu + 4u = -5/48, pi~ = pi + 2u, sigma~ = sigma - 12u,
    #
    #   H4 = -nu~ (L_up - 2I) + u S_sq^2 - pi~ S_sq + sigma~ I - 2 C_shp R,
    #
    # where R is the cross-plane half of S_sq (equivalently minus the
    # cross-plane half of L_up). On the carrier, L_up psi = e1 psi and
    # S_sq psi = -4 psi, so every term but the last is a scalar there and the
    # carrier projection is T = -nu~ e1^2 + (2 nu~ + 16u + 4 pi~ + sigma~) e1
    # - 2 (-2 C_shp) e2 / ... -- i.e. A = -nu~, B = D = 0 with no cancellation
    # to explain, and 4C = the coefficient of R. So C_shp is not an off-axis
    # fit parameter: it is the weight of the single operator in the kernel
    # that is not a polynomial in the two Hodge Laplacians, and the carrier is
    # an exact eigenvector of H4 if and only if C_shp = 0.
    recs = kernel_records()
    amps = KO.amplitudes(recs)
    form = KO.hodge_form(amps)
    ident = KO.identity()
    s_sq = KO.combine((1, KO.down_laplacian()), (-4, ident))
    up = KO.combine((1, KO.up_laplacian()), (-2, ident))
    r_half = KO.cross_half(s_sq)
    # R is where the two Laplacians overlap: minus the cross half of L_up
    overlap = KO.cross_half(KO.up_laplacian()) == {k: -v for k, v in r_half.items()}
    # the Hodge part alone, and the residual it leaves, which must be -2C R
    hodge_part = KO.combine(
        (-form["nu~"], up),
        (form["u"], KO.compose(s_sq, s_sq)),
        (-form["pi~"], s_sq),
        (form["sigma~"], ident),
    )
    residual = KO.combine((1, dict(recs)), (-1, hodge_part))
    ok = (
        KO.hodge_records(form) == dict(recs)
        and form["nu~"] == Fraction(-5, 48)
        and form["C"] == K.C_SHP_HISTORICAL == kernel_constants()["C_shp"]
        and overlap
        and residual == {k: -2 * form["C"] * v for k, v in r_half.items()}
        and KO.acts_as(KO.up_laplacian(), KO.E1)
        and KO.acts_as(KO.compose(KO.down_laplacian(), KO.up_laplacian()), {})
        and KO.acts_as(KO.compose(KO.up_laplacian(), KO.down_laplacian()), {})
        # the eigenvector criterion: H4 psi - lambda psi = -2C R psi, nonzero here
        and not KO.acts_as(r_half, {})
        # and the registered diagonal coefficient is the reduced shared-link sum
        and -8 * (amps["rho"] + form["pi~"]) == K.BETA_PEN_3
    )
    return (
        ok,
        (
            f"all 189 records equal -nu~ (L_up - 2) + u S_sq^2 - pi~ S_sq + sigma~ - 2C R with "
            f"nu~ = {form['nu~']}, u = {form['u']}, pi~ = {form['pi~']}, sigma~ = "
            f"{form['sigma~']} and C = {form['C']} = C_shp exactly. L_down L_up = 0 and "
            "L_up psi = e1 psi, S_sq psi = -4 psi, so on the cube-boundary carrier every term "
            "but the last is a scalar: A = -nu~ = 5/48 with NO u in it, B = D = 0 with nothing "
            "to cancel, and 4C e2 is the projection of -2C R alone. The tier collapse G14 asked "
            "a mechanism for is therefore the Hodge structure of the kernel: the only operator "
            "outside the algebra of the two Laplacians is R, the cross-plane half of the "
            "shared-link adjacency, and R projects to pure e2. And the carrier is an exact "
            "eigenvector of H4 if and only if C_shp = 0 -- C2 is the question of how far the "
            "cube boundary is from being an eigenvector. The disagreement between the two "
            "kernels is four numbers (u, rho, pi~, sigma~); u and sigma~ enter the carrier "
            "band only through its constant, so C_shp = -5/96 - (rho + pi~)/2 rests on the two "
            "shared-link amplitudes and nothing else. In the register's own terms, "
            f"beta_pen = -8 (rho + pi~) = {K.BETA_PEN_3} exactly"
        ),
        {"PI_REDUCED": form["pi~"], "SIGMA_REDUCED": form["sigma~"]},
    )


@orbit.check(
    "FINDING: the cold kernel has the same Hodge form, with nu~ = -5/48 and its own "
    "(u, rho, pi~, sigma~)",
    _HODGE,
    tier=2,
    rests_on=(_FORM,),
)
def _():
    cold = dict(KO.cold_records())
    form = KO.hodge_form(KO.cold_amplitudes())
    built = KO.hodge_records(form)
    scale = max(abs(v) for v in cold.values())
    gap = max(abs(float(built.get(k, 0)) - cold.get(k, 0.0)) for k in set(built) | set(cold))
    ok = (
        gap < 1e-11 * scale
        and abs(form["nu~"] + 5 / 48) < 1e-12
        and abs(form["C"] - K.C_SHP_NEW_NUM) < 1e-12
    )
    return ok, (
        f"the v10a.26 dump is -nu~ (L_up - 2) + u S_sq^2 - pi~ S_sq + sigma~ - 2C R to "
        f"{gap:.1e} absolute on records of size up to {scale:.2f} ({gap / scale:.1e} relative), "
        f"with nu~ = {form['nu~']:.15f} (-5/48 to {abs(form['nu~'] + 5 / 48):.1e}), "
        f"u = {form['u']:.10e}, pi~ = {form['pi~']:.12f}, sigma~ = {form['sigma~']:.10f}, and "
        f"C = {form['C']:.15f} against the registered {K.C_SHP_NEW_NUM!r}. So the two rival "
        "kernels share the Hodge form and the primitive cube completion; they differ in the "
        "two-hop weight u (band-invisible on the carrier), the on-site anchor, and the two "
        "shared-link amplitudes rho and pi~ -- and C2 is exactly the last two. Nothing here "
        "prefers either side"
    )


# -- G3: the chain amplitude u, computed independently --------------------------
#
# The route ADR 0019 opened. ``workhouse.chain_cluster`` uses the pinned exact
# engine for three primitives only (Wilson words, Haar inner products, the H0
# action) and assembles degenerate perturbation theory itself. Its second order
# reproduces the register; its fourth order returns the two-hop weight u on a
# ten-link cluster in seconds.

_CHAIN = "C2; G3 chain amplitude route; G14; ADR 0019; RUN g3_chain_amplitude_2026-09-02"
_SECOND = (
    "the engine's primitives plus textbook second-order theory return t_3 S_sq, "
    "the C-even hop and the leakage"
)


@orbit.check(_SECOND, _CHAIN)
def _():
    from .. import chain_cluster as CC

    v = CC.validate()
    ok = (
        v["ok"]
        and v["coplanar_hop"] == -Fraction(5, 612)
        and v["perpendicular_hop"] == Fraction(5, 612)
        and v["c_even_hop"] == K.T_PLUS_2
        and v["leakage"] == K.LEAK_2
        and -v["coplanar_hop"] == K.T_MINUS_2
    )
    return ok, (
        f"C-odd shared-link hop {v['coplanar_hop']} for a coplanar pair and "
        f"{v['perpendicular_hop']} for a perpendicular pair -- t_3 = 5/612 with exactly the sign "
        "pattern of S_sq, the shared-link adjacency the Hodge form is built on; C-even hop "
        f"{v['c_even_hop']} = T_PLUS_2; C-odd per-neighbour leakage {v['leakage']} = LEAK_2 once "
        "the neighbour's own vacuum bubble -3/4 is "
        "subtracted. Nothing here read either fourth-order kernel: the numbers come from Haar "
        "integrals, the Fierz action and P V R V P on one- and two-plaquette clusters"
    )


@orbit.check(
    "FINDING: the chain amplitude is u = X_QUANTUM exactly, on the coplanar and the bent chain; "
    "the cold kernel's 4.13 u is wrong",
    _CHAIN,
    rests_on=(_SECOND, _SQUARE),
)
def _():
    # The cluster cumulant W({P,Q,R}) - W({P,R}) of the P -> R element, fourth
    # order, Hermitian form with PVP = 0, Q-touched histories only (the others
    # cancel between the clusters). Two chain geometries: coplanar P-Q-R along
    # an axis, and bent (bottom face, side face, top face of a cube). The Hodge
    # form says both carry the SAME weight u with sign S_PQ S_QR: +1 for two
    # coplanar junctions, -1 for two perpendicular ones.
    from .. import chain_cluster as CC

    cop_odd, cop_even = CC.chain_amplitude("coplanar")
    bent_odd, bent_even = CC.chain_amplitude("bent")
    cold_ratio = 4.132743700859149
    ok = (
        cop_odd == K.X_QUANTUM
        and bent_odd == -K.X_QUANTUM
        and cop_even == bent_even
        and abs(float(cop_odd) / float(K.X_QUANTUM) - cold_ratio) > 3
    )
    return (
        ok,
        (
            f"coplanar chain u = {cop_odd}, bent chain u = {bent_odd}: equal to X_QUANTUM = "
            f"{K.X_QUANTUM} exactly, as rationals, with the sign S_PQ S_QR the Hodge form "
            "requires (+1 coplanar, -1 bent). Universality holds: two geometrically different "
            "two-hop chains carry one weight, which is the single dynamical input G14 had left. "
            "The historical exact "
            "kernel is reproduced on the one quantity in the agreed sector the two pipelines "
            f"disagree on; the v10a.26 dump's u is {cold_ratio:.7f} times this and is therefore "
            "WRONG there. That does not decide C2 -- u is the constant 16u on the carrier -- but "
            "the cold pipeline has a demonstrated error in a sector whose shape it shares with the "
            "historical kernel, and until that error is located and shown not to reach rho and pi~ "
            f"its sign-flipped values have no independent weight. The C-even chain amplitude "
            f"{cop_even} is new to the register"
        ),
        {"U_CHAIN_C_EVEN": cop_even},
    )


_REPLICATION = "runs/g3_chain_amplitude_replication_2026-09-02"


@orbit.check(
    "REPLICATION: a second implementation, with the engine's PVP assembly and a Krylov "
    "resolvent, gives u = X_QUANTUM on three chain types",
    _CHAIN + "; " + _REPLICATION + "; ADR 0020",
    rests_on=(
        "FINDING: the chain amplitude is u = X_QUANTUM exactly, on the coplanar and the bent "
        "chain; the cold kernel's 4.13 u is wrong",
        _SQUARE,
    ),
)
def _():
    # Written the same day without reading chain_cluster, and differing from
    # it where it matters: the resolvent is a Krylov minimal polynomial of H0
    # relative to each vector rather than a block characteristic polynomial;
    # the fourth-order assembly is the engine's own with A = PVP = the SU(3)
    # baryonic vertex (<P|V|Pbar> = 1, not zero -- the two agree on the
    # cumulant only because the A-terms cancel between link-disjoint
    # endpoints); and it adds the coplanar-perpendicular chain, on which the
    # two hops carry opposite signs, with the incidence sign computed from
    # link traversals. Reads the pinned certificate (the run takes two
    # minutes) and compares with the live first implementation.
    import json

    from .. import chain_cluster as CC
    from ._core import ROOT

    cert = json.loads(
        (ROOT / _REPLICATION / "chain_amplitude_certificate.json").read_text(encoding="utf-8")
    )
    u = Fraction(K.X_QUANTUM.p, K.X_QUANTUM.q)
    chains = cert["chains"]
    by = {
        name: (Fraction(c["codd_chain_amplitude"]), c["incidence_sign"])
        for name, c in chains.items()
    }
    even = {Fraction(c["ceven_chain_amplitude"]) for c in chains.values()}
    signs = {name: s for name, (_a, s) in by.items()}
    so = {k: Fraction(v) for k, v in cert["second_order"].items()}
    t3 = Fraction(K.T_MINUS_2.p, K.T_MINUS_2.q)
    cop_odd, cop_even = CC.chain_amplitude("coplanar")
    ok = (
        set(chains) == {"coplanar_chain", "bent_chain", "zigzag_chain"}
        and all(a == s * u for a, s in by.values())
        and signs == {"coplanar_chain": 1, "bent_chain": -1, "zigzag_chain": -1}
        and even == {cop_even}
        and cop_odd == u
        and so["coplanar_shared_link_codd_hop"] == -t3
        and so["perpendicular_shared_link_codd_hop"] == t3
        and so["shared_link_ceven_hop_coplanar"] == so["shared_link_ceven_hop_perpendicular"]
        and so["shared_link_ceven_hop_coplanar"] == Fraction(K.T_PLUS_2.p, K.T_PLUS_2.q)
    )
    (u_even,) = even
    return ok, (
        f"C-odd cumulant W(P,Q,R) - W(P,R) = s * {u} on every chain, s = "
        + ", ".join(f"{s:+d} ({name.replace('_chain', '')})" for name, s in signs.items())
        + ", s the product of the two signed shared-link incidences -- the (S_sq^2)_PR entry -- "
        f"and the C-even cumulant {u_even} on all three, equal to the first implementation's "
        f"{cop_even}. Same second-order gate ({so['coplanar_shared_link_codd_hop']}, "
        f"{so['perpendicular_shared_link_codd_hop']}, {so['shared_link_ceven_hop_coplanar']}). "
        "Two implementations, different resolvents, different assemblies (PVP = 0 against the "
        "engine's PVP = +-1 per C-sector), three chain types: one rational. Nothing here "
        "prefers either side of C2"
    )
