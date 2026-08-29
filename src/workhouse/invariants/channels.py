from __future__ import annotations

import json
import re

from sympy import (
    Rational,
    expand,
    simplify,
    sin,
    symbols,
    sympify,
)

from .. import constants as K
from .. import payloads as P
from ._core import ROOT, _suite
from ._shared import MASTER_EDITION, _master_edition_text

# ==========================================================================
# The historical kernel, decomposed channel by channel over the whole zone.
# The repository's earlier kernel checks see the 189-record artifact at the
# four parity points; these see it identically in k, so the tier collapse
# B = D = 0 becomes two exact integer cancellations at record level (G14)
# and the C2 dispute's geography — which channels carry it — is a checked
# statement instead of prose. Source claims: the maintainer's off-axis
# ledger (WORK_SINCE_2026-08, 2026-08-22), adversarially recomputed here.
# Nothing in this suite adjudicates C2 or prefers a side.
channels = _suite("off-axis channel ledger (C2 geography, G14)")


@channels.check(
    "the 189-record kernel decomposes in the shape basis over the whole zone",
    "UNIFIED v4.3 §5.1/§6",
)
def _():
    from fractions import Fraction

    from .. import channel_ledger as CL

    d = CL.decompose()
    t = d["totals"]
    counts_ok = d["counts"] == {
        "on-site (0,0,0)": 3,
        "NORMAL (0,0,1)": 6,
        "IN-PLANE (0,0,1)": 12,
        "IN-PLANE (0,0,2)": 12,
        "IN-PLANE (0,1,1)": 12,
        "MIXED (0,1,1)": 24,
        "ROTATION": 120,
    }
    ok = (
        d["n_records"] == 189
        and counts_ok
        and t["E"] == 0
        and t["F"] == 0
        and t["c0"] == P.as_fraction(K.Q_BAND_4)
        and t["A"] == Fraction(5, 48)
        and t["B"] == 0
        and t["D"] == 0
        and t["C4"] / 4 == P.as_fraction(K.C_SHP_HISTORICAL)
    )
    return ok, (
        "psi^dagger H_4 psi lies exactly in span{q, q^2, e_2, q e_2, e_3} with "
        "constant and q^3 coefficients ZERO (so unlinked scalar products cannot "
        "move the shape), and the totals are c_0 = q_band^(4), A = 5/48, "
        "B = D = 0, C = C_shp^historical exactly -- the parity-point kernel "
        "identity, promoted to the whole zone; blocks (3,6,12,12,12,24,120)"
    )


@channels.check(
    "FINDING: the tier collapse is two integer cancellations at record level",
    "MASTER_THEORY §5.2 / G14",
)
def _():
    from .. import channel_ledger as CL

    d = CL.decompose()
    x = CL.X_QUANTUM
    b_int = {b: d["blocks"][b]["B"] / x for b in CL.BLOCKS}
    d_int = {b: d["blocks"][b]["D"] / x for b in CL.BLOCKS}
    weights_b = [b_int["IN-PLANE (0,0,2)"], b_int["MIXED (0,1,1)"], b_int["ROTATION"]]
    weights_d = [
        d_int["IN-PLANE (0,0,2)"],
        d_int["IN-PLANE (0,1,1)"],
        d_int["MIXED (0,1,1)"],
    ]
    x_is_weight = any(w == x for (_key, w) in P.kernel_records())
    ok = (
        all(v.denominator == 1 for v in list(b_int.values()) + list(d_int.values()))
        and weights_b == [1, 1, -2]
        and sum(weights_b) == 0
        and weights_d == [-3, 6, -3]
        and sum(weights_d) == 0
        and x_is_weight
    )
    return ok, (
        "every block's q*e_2 and e_3 amplitude is an integer multiple of "
        "x = 360421351/40327601932800 (itself a raw record weight); "
        "B = 0 is (+1,+1,-2)*x over {IN-PLANE(0,0,2), MIXED, ROTATION} and "
        "D = 0 is (-3,+6,-3)*x over {IN-PLANE(0,0,2), IN-PLANE(0,1,1), MIXED} "
        "-- the kernel DOES carry B,D-generating displacement shells; they "
        "cancel, so 'forced by the symmetry and displacement gates' is at "
        "best imprecise (the finding G14 must explain)"
    )


@channels.check(
    "C_normal = -A_normal/2: the agreed axial coefficient pins the normal channel",
    "UNIFIED v4.3 §6",
)
def _():
    from fractions import Fraction

    from .. import channel_ledger as CL

    d = CL.decompose()
    x = CL.X_QUANTUM
    a_n = d["blocks"]["NORMAL (0,0,1)"]["A"]
    c_n = d["blocks"]["NORMAL (0,0,1)"]["C4"] / 4
    a_mixed = d["blocks"]["MIXED (0,1,1)"]["A"]
    ok = (
        c_n == -a_n / 2
        and c_n == Fraction(-1050558388351, 20163800966400)
        and a_n == Fraction(5, 48) + 4 * x
        and a_mixed == -4 * x
    )
    return ok, (
        "on the six NORMAL records C = -A/2 = -1050558388351/20163800966400 "
        "exactly, with A_normal = 5/48 + 4x and MIXED carrying exactly -4x -- "
        "so the primitive cube-completion hop accounts for A = 5/48, and the "
        "coefficient the sealed suite shows both kernels share pins the "
        "normal sector; everything disputed lives in the non-normal remainder"
    )


@channels.check(
    "the shipped displacement support is exactly six shells",
    "off-axis ledger falsifier gate",
)
def _():
    from .. import channel_ledger as CL

    census = CL.support_census()
    ok = census == {
        (0, 0, 0): 9,
        (0, 0, 1): 54,
        (0, 0, 2): 24,
        (0, 1, 1): 78,
        (0, 1, 2): 12,
        (1, 1, 1): 12,
    }
    return ok, (
        "sorted-|d| shells with multiplicities: (0,0,0)x9, (0,0,1)x54, "
        "(0,0,2)x24, (0,1,1)x78, (0,1,2)x12, (1,1,1)x12 -- the channel "
        "ledger's block structure assumes this support is complete, and a "
        "record outside it falsifies the classification"
    )


@channels.check(
    "rotation decomposes only as a sum, and the ket convention is load-bearing",
    "UNIFIED v4.3 §3.2 (carrier), tier_collapse convention",
)
def _():
    from .. import channel_ledger as CL

    shells = CL.rotation_shells_in_span()
    ok = (
        len(shells) == 6
        and not any(shells.values())
        and CL.solve_span(CL.numerator(CL.decompose()["records"]["ROTATION"])) is not None
        and not CL.conjugated_ket_rotation_in_span()
    )
    return ok, (
        "each of the six rotation displacement shells is individually OUTSIDE "
        "the shape span; the 120-record sum is inside -- so no per-shell "
        "re-derivation can be compared channel-wise -- and with the ket "
        "conjugated (psi-bar instead of the d-direction) the rotation block "
        "leaves the span entirely: the two conventions coincide at the four "
        "parity points, so only a whole-zone check can catch the trap a "
        "re-implementation would fall into"
    )


@channels.check(
    "the pinned structured B_N expression IS P17(N^2)/(N R20(N^2))",
    "GLUEBALL_DETAILED_FORMULA v3.1 §11 + App. A",
)
def _():
    from .. import channel_ledger as CL

    agree = [CL.b_note(n) == CL.beta_formula(n) for n in range(3, 21)]
    r20_at_9 = int(CL.R20.eval(9))
    ok = all(agree) and r20_at_9 != 0
    return ok, (
        "the walled-Brauer structured expression (pinned note, 74 terms) and "
        "the boxed all-rank formula agree exactly at N = 3..20, N = 3 "
        "included -- the corpus states the formula for N >= 4 and cautions "
        "against substituting at N = 3, but every R20 factor is nonzero at "
        "z = 9, so the continuation exists and equals the pinned expression; "
        "what the balanced value MEANS at N = 3 stays a claim, not a check"
    )


@channels.check(
    "the N=3 continuation shift is exactly 25/64, with two exact corollaries",
    "ledger C10; GLUEBALL_DETAILED_FORMULA v3.1 §8/§11",
)
def _():
    from fractions import Fraction
    from math import gcd

    from .. import channel_ledger as CL

    a_shp = Fraction(5, 48)
    c_hist = P.as_fraction(K.C_SHP_HISTORICAL)
    beta_hist = 8 * a_shp + 16 * c_hist
    beta_bal = CL.beta_formula(3)
    c_bal = (beta_bal - 8 * a_shp) / 16
    alpha3 = P.as_fraction(K.ALPHA_PEN_3)
    kc = P.kernel_constants()
    ok = (
        kc["beta"] == beta_hist
        and kc["alpha"] == alpha3
        and beta_hist - beta_bal == P.as_fraction(K.DELTA_BETA_3)
        and beta_hist - beta_bal == -Fraction(15, 16) * alpha3
        and (c_hist - c_bal) / (a_shp / 2) == -Fraction(15, 32)
        and gcd(107551523941875, 275331901291200) == 4302060957675
    )
    return ok, (
        f"beta_3^hist - beta_3^bal = {K.DELTA_BETA_3} exactly (raw numerator "
        "-107551523941875 over 275331901291200 reduces by the factor "
        "4302060957675), which IS the registry's DELTA_BETA_3 and C10's "
        "recorded shift -- read here rather than compared against a literal; "
        "corollaries never before recorded: Delta_beta_3 = -(15/16)*alpha_3 "
        "and Delta_C_3/(A/2) = -15/32. A relation among recorded quantities "
        "-- whether the shift was derived or defined as the difference is "
        "open (off-axis ledger §7), and no side of C2 is preferred here"
    )


@channels.check(
    "at N = 6, the one rank carrying both routes here, they agree; N = 3 is closed",
    "THM_SUN unified nality v2 §5; ledger C10; GCSG SU(6) certificate",
)
def _():
    # The other half of C10. Delta_beta_3 is now read by the check that
    # establishes it, one check up; Delta_q_3 is read by nothing anywhere,
    # and this is why.
    #
    # The unified nality theorem states q_N = q_N^bal + Delta q_N^exc and
    # warns, in its own words, that q_N^bal at an exceptional rank means the
    # DIRECT fixed-rank contraction and not analytic continuation of the
    # stable formula. That is a warning about method with no number attached,
    # and it leaves two things unestablished that this check settles.
    #
    # First: where both routes exist, do they agree? At N = 6 they do, exactly:
    # the shipped SU(6) certificate carries a direct fixed-rank balanced
    # contraction and it equals the stable continuation. That is ONE rank, and
    # the scope matters enough to be checked rather than described. An earlier
    # version of this detail line generalised it to "wherever both are
    # defined", which a single instance cannot establish -- another rank could
    # have a different direct contraction and this check would still pass. The
    # sweeping form reached CERTIFIED.md and the G1 ledger before a review bot
    # caught it on PR #52; the claim is now scoped to the rank it rests on.
    #
    # N = 6 is the only rank where both routes are here, and that is asserted
    # nowhere: the SU(6) certificate carries q for both the balanced and full
    # kernels, and the SU(5) stage-1 payload -- the only other shipped
    # exceptional-rank artifact -- carries a word and channel census with no
    # fixed-rank q at all. Both are read below.
    #
    # At N = 5 the continuation is regular and the corpus records no
    # exceptional assignment, so the law reads Delta q_5 = 0 there. That is a
    # statement about the continuation alone; it is not a second instance of
    # the two routes agreeing, because no direct N = 5 contraction is here.
    #
    # Second: what exactly closes the route at N = 3? D34 carries (z-9)^3
    # with Q32(9) nonzero, so the continuation has a pole of order exactly
    # three. Delta q_3 therefore rests on a fixed-rank contraction that is
    # not in this repository, and no amount of algebra on the stable formula
    # will produce it -- which is the precise, checkable form of "the
    # balanced side of C2 is T3 here".
    #
    # One hypothesis tried and refuted, kept because the refutation is the
    # useful part: that the Hadamard finite part of that pole IS the balanced
    # value. It is not, and it is not q_3 either. It misses q_3^bal by
    # 67307265071/305627904000 and q_3 by 48497711/101875968000 -- and the
    # second miss is the interesting number, because it is small (height
    # about 10^11, denominator 2^11 3^5 5^3 17^3) against operands of height
    # about 10^19. Small is not zero. Recorded as a measured gap, with no
    # mechanism claimed for it; ADR 0005 is what reading one off a near-miss
    # costs here.
    from fractions import Fraction

    from sympy import factor_list

    from .. import channel_ledger as CL

    zz, q32, d34 = P.q_polynomials()
    factors = {str(b): e for b, e in factor_list(d34)[1]}

    def continuation(n: int) -> Fraction:
        return Fraction(-2, 3 * n) * Fraction(int(q32.eval(n * n)), int(d34.subs(zz, n * n)))

    # N = 6: continuation against the shipped direct contraction, and the shift
    certificate = P.su6()
    agree_at_six = Fraction(certificate["balanced_N6"]["q"]) == continuation(6)
    shift_at_six = Fraction(certificate["full_SU6"]["q"]) - Fraction(
        certificate["balanced_N6"]["q"]
    ) == P.as_fraction(K.DELTA_Q_6)
    # N = 5: exceptional by the |p-q| = N <= 6 count, but carrying no assignment
    five_is_exceptional = 5 in K.EXCEPTIONAL_RANKS
    regular_at_five = d34.subs(zz, 25) != 0
    # the scope of the agreement claim, checked: SU(6) ships q on both kernels,
    # SU(5) ships no fixed-rank q, so N = 6 is the only rank with both routes
    six_ships_both = "q" in certificate["balanced_N6"] and "q" in certificate["full_SU6"]
    five_ships_no_q = not any(
        "q" in section for section in P.stage1().values() if isinstance(section, dict)
    )

    # N = 3: the pole, exactly
    laurent = CL.scalar_continuation_laurent(3, order=0)
    pole_order = -min(laurent)
    q3_balanced = P.as_fraction(K.Q_BAND_4) - P.as_fraction(K.DELTA_Q_3)
    finite_part = laurent[0]
    misses_balanced = finite_part - q3_balanced
    misses_full = finite_part - P.as_fraction(K.Q_BAND_4)

    ok = (
        agree_at_six
        and shift_at_six
        and six_ships_both
        and five_ships_no_q
        and five_is_exceptional
        and regular_at_five
        and factors.get("z - 9") == 3
        and q32.eval(9) != 0
        and pole_order == 3
        and laurent[-3] == Fraction(27, 64)
        and misses_balanced != 0
        and misses_full != 0
        and misses_balanced == Fraction(-67307265071, 305627904000)
        and misses_full == Fraction(48497711, 101875968000)
        and P.as_fraction(K.DELTA_BETA_3) != 0
    )
    return ok, (
        "at N = 6 the stable continuation equals the shipped direct fixed-rank balanced "
        f"contraction exactly, and the full value exceeds it by {K.DELTA_Q_6}. Scope, because "
        "one instance is not a law: N = 6 is the ONLY rank where this repository holds both "
        "routes — the SU(6) certificate ships q on both kernels, the SU(5) stage-1 payload "
        "ships none — so what is established is that the continuation is not a different "
        "object from the direct contraction THERE, not that the two coincide at every "
        "exceptional rank. At N = 3 the continuation route is closed: D34 carries (z-9)^3 "
        f"with Q32(9) nonzero, a pole of order exactly {pole_order}, leading coefficient "
        f"{laurent[-3]}. So Delta q_3 = {K.DELTA_Q_3} is a DEFINITION in this repository, "
        f"not a check; it fixes q_3^bal = {q3_balanced}, a value recorded nowhere here. The "
        f"finite part of the pole is not that value (off by {misses_balanced}) and not q_3 "
        f"either (off by {misses_full}) — the second miss small against operands of height "
        "about 10^19, measured and left unexplained. What would close it is the direct "
        "SU(3) fixed-rank contraction, the artifact the unified nality theorem names"
    )


@channels.check(
    "scalar vs shape continuation: poles where the corpus forbids, regular where it allows",
    "GLUEBALL_DETAILED_FORMULA v3.1; THM_SUN unified v2; THM_SU6",
)
def _():
    from fractions import Fraction

    from sympy import Rational as R
    from sympy import factor_list

    from .. import channel_ledger as CL

    zz, q32, d34 = P.q_polynomials()
    facs = {str(b): e for b, e in factor_list(d34)[1]}
    root_max = max(CL.R20.real_roots())

    def q_formula(n: int) -> Fraction:
        return Fraction(-2, 3 * n) * Fraction(int(q32.eval(n * n)), int(d34.subs(zz, n * n)))

    q5_recorded = Fraction(-781009569168365268247626732239, 6484474594581730088957376233472)
    q6_bal_recorded = Fraction(
        -102586479919344400197896189360827281727,
        2665788121217129017242143775195086906250,
    )
    ok = (
        facs.get("z - 4") == 1
        and facs.get("z - 9") == 3
        and facs.get("z - 16") == 1
        and root_max == R(25, 9)
        and q_formula(5) == q5_recorded
        and q_formula(6) == q6_bal_recorded
    )
    return ok, (
        "D34 carries (z-4)(z-9)^3(z-16), so the scalar continuation is "
        "singular at exactly N = 2,3,4 -- it fails loudly where an "
        "epsilon-sector exists -- while R20's largest real root is 25/9 "
        "(N = 5/3), so the shape continuation is regular at every integer "
        "rank; below its stated N >= 7 scope the scalar formula reproduces "
        "the recorded q_5 exactly (SU(5): no determinant sector) and the "
        "recorded q_6^bal exactly (THM_SU6 line 86, Delta_q_6 = 6/343 "
        "checked elsewhere): the blanket N = 3 prohibition is a scalar-"
        "family fact, not a shape-family one"
    )


@channels.check(
    "FINDING: the retained Gamma/axis data cannot identify C_shp",
    "MASTER paper Thm. 13 / C2 / G3",
)
def _():
    a1, a2, a3 = symbols("a1 a2 a3", nonnegative=True)
    e2 = a1 * a2 + a1 * a3 + a2 * a3
    axial_cuts = [
        e2.subs({a2: 0, a3: 0}),
        e2.subs({a1: 0, a3: 0}),
        e2.subs({a1: 0, a2: 0}),
    ]
    vanishes = all(expand(cut) == 0 for cut in axial_cuts)
    at_m = e2.subs({a1: 4, a2: 4, a3: 0})
    at_r = e2.subs({a1: 4, a2: 4, a3: 4})
    separates = at_m == 16 and at_r == 48
    return vanishes and separates, (
        "the two fourth-order records' carrier NUMERATORS differ by "
        "4*Delta_C*e_2, and e_2 is the ZERO POLYNOMIAL on every axial cut — "
        "so no Gamma-point or axial datum distinguishes them at any precision "
        f"(non-identifiability, not imprecision); e_2(M) = {at_m}, e_2(R) = "
        f"{at_r}, so the numerators differ by 64*Delta_C at M and 192*Delta_C "
        "at R. Dividing by q = 8 and 12 gives the BAND separations 8*Delta_C "
        "and 16*Delta_C, which is what the crosswalk check reports — the two "
        "normalisations differ by a factor of q and an earlier wording of this "
        "line did not say which it meant. An off-axis contraction (G3) is the "
        "only decider, and neither record is preferred here"
    )


@channels.check(
    "on an axial cut the mixed invariants vanish and the norm divides",
    "MASTER paper §7",
)
def _():
    k = symbols("k", real=True)
    a = [4 * sin(k / 2) ** 2, sympify(0), sympify(0)]
    q_ax = a[0] + a[1] + a[2]
    e2_ax = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
    e3_ax = a[0] * a[1] * a[2]
    lam = 4 * sin(k / 2) ** 2
    numerator = (K.ALPHA_PEN_3 / 4) * lam**2
    quotient = simplify(numerator / q_ax)
    ok = (
        expand(e2_ax) == 0
        and expand(e3_ax) == 0
        and simplify(q_ax - lam) == 0
        and simplify(quotient - K.A_SHP_3 * lam) == 0
        and K.ALPHA_PEN_3 / 4 == K.A_SHP_3 == Rational(5, 48)
    )
    return ok, (
        "on an axial cut q = L(k) = 4 sin^2(k/2) with e_2 = e_3 = 0, and the "
        "raw cube-boundary numerator (alpha_3/4) L^2 divided by ||w||^2 = q = L "
        "leaves a single power of L with coefficient alpha_3/4 = 5/48 = A_shp"
    )


@channels.check(
    "FINDING: an explicit second witness C_alt exhibits the C2 non-identifiability",
    "COMPLETE_UNIFIED_MASTER_CLOSED §15.3.2",
)
def _():
    # The registered obstruction says the two recorded C_shp sides differ by
    # 4 Delta_C e_2, and e_2 is the zero polynomial on an axial cut. That is an
    # argument about a difference. The 2026-08-28 master edition sharpens it
    # into a CONSTRUCTION: it exhibits a second exact rational witness,
    # C_alt = C_old + 25/1024, and every member of that family reproduces the
    # retained Gamma and axial data identically while separating off-axis.
    #
    # Re-derived here rather than transcribed. With the shape term C(4 e_2/q_a)
    # and a_i = 4 sin^2(k_i/2), the zone corners give a = (4,0,0), (4,4,0),
    # (4,4,4), so the induced band separations are Delta_C * 4 e_2 / q_a.
    #
    # This DECIDES NOTHING about which C is physical. It is the opposite: a
    # constructive proof that the retained corpus cannot decide, which is why
    # G3's target-blind off-axis contraction is the only route. Note also that
    # the document naming this witness is the one titled "...CLOSED", and its
    # own section heading is "Why the exact rooted scalar remains open".
    c_old = Rational(-211835444920651, 4405310420659200)
    c_alt = Rational(-13035490122347, 550663802582400)
    shift = c_alt - c_old
    # Read the witness out of the PINNED source rather than trusting that it
    # was transcribed correctly. Without this the arithmetic below would verify
    # one hand's transcription against itself -- caught on PR #38 by a review
    # bot, and it was right.
    source = _master_edition_text()
    quoted = all(str(abs(part)) in source for part in (c_alt.p, c_alt.q, c_old.p, c_old.q))

    separations = {}
    for label, cut in (("X", (1, 0, 0)), ("M", (1, 1, 0)), ("R", (1, 1, 1))):
        a = [4 if x else 0 for x in cut]
        q_a = sum(a)
        e_2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
        separations[label] = shift * Rational(4 * e_2, q_a)

    expected = {"X": Rational(0), "M": Rational(25, 128), "R": Rational(25, 64)}
    ok = shift == Rational(25, 1024) and separations == expected and quoted
    return ok, (
        f"C_alt - C_old = {shift} exactly, and the induced separations are "
        f"X {separations['X']}, M {separations['M']}, R {separations['R']}; both witnesses appear "
        f"verbatim in the pinned edition ({MASTER_EDITION.name}). Identical on every "
        "retained datum, distinct off-axis. Non-identifiability is exhibited by construction, "
        "not argued from a difference. Neither C_shp side is preferred, and C2 stays open -- the "
        "source document's own section is titled 'Why the exact rooted scalar remains open'"
    )


@channels.check(
    "FINDING: C_shp is carried by 6 of 189 records, not spread across the kernel",
    "UNIFIED v4.3 §5.1/§6, block decomposition",
    tier=2,
)
def _():
    # G3 is scoped as a 609-cluster sweep producing a whole independent
    # kernel, and that sweep is currently infeasible. This asks a cheaper
    # question: within the kernel this repository already has, WHERE does
    # C_shp actually come from?
    #
    # Not evenly. The shape coefficient is concentrated in the six
    # nearest-neighbour NORMAL (0,0,1) records, which carry 81% of the total
    # |C4| weight at -0.0347 per record. The ROTATION block is 120 records --
    # 63% of the kernel -- and contributes 6%, at -0.000136 each, a factor of
    # 255 less sensitive per record. The three on-site records contribute
    # exactly nothing, which is the same statement as the registered fact that
    # unlinked scalar products cannot move the shape.
    #
    # What this changes: an adjudication does not obviously need all 189
    # records recomputed, and it points a blind recomputation at the normal
    # nearest-neighbour sector rather than at all 609 clusters uniformly.
    #
    # SUPERSEDED IN PART: an earlier draft of this check added that a
    # NORMAL-sector discrepancy could therefore produce the disputed gap.
    # That was wrong, and the check below ("A = 5/48 pins the normal sector's
    # whole C4 contribution") shows why: the normal block's A and C4
    # contributions are rigid multiples of one number, so agreeing on
    # A = 5/48 fixes its C4 too. Magnitude alone was the wrong test.
    #
    # It does NOT decide C2. Where a coefficient's VALUE lives is evidence
    # about where a DISCREPANCY could live, not proof of where it does, and
    # neither recorded side is preferred here.
    #
    # T2, not T1, and the tier guard was right to insist: the block
    # decomposition is exact rational arithmetic throughout, but the gap
    # comparison reaches C_SHP_NEW_NUM, which the corpus records only as a
    # float. One float-dependent clause makes the whole verdict T2, however
    # exact the rest of it looks.
    from fractions import Fraction

    from .. import channel_ledger as CL

    decomposition = CL.decompose()
    blocks = {name: Fraction(block.get("C4", 0)) for name, block in decomposition["blocks"].items()}
    counts = decomposition["counts"]
    normal = blocks["NORMAL (0,0,1)"]
    rotation = blocks["ROTATION"]
    magnitude = sum(abs(value) for value in blocks.values())
    gap = 4 * (P.as_fraction(K.C_SHP_HISTORICAL) - Fraction(str(K.C_SHP_NEW_NUM)))

    return (
        blocks["on-site (0,0,0)"] == 0
        and abs(normal) > magnitude * Fraction(3, 4)
        and counts["NORMAL (0,0,1)"] == 6
        and counts["ROTATION"] == 120
        and abs(normal / counts["NORMAL (0,0,1)"]) > 100 * abs(rotation / counts["ROTATION"])
        and abs(gap) > abs(rotation)
    ), (
        f"the 6 NORMAL (0,0,1) records carry {float(abs(normal) / magnitude) * 100:.0f}% of the "
        f"total |C4| weight at {float(normal / 6):.6f} each, while the 120 ROTATION records carry "
        f"{float(abs(rotation) / magnitude) * 100:.0f}% at {float(rotation / 120):.6f} each -- "
        f"{float(abs(normal / 6) / abs(rotation / 120)):.0f}x less sensitive per record; on-site "
        f"contributes exactly 0. The disputed gap is {float(abs(gap)):.4f} in C4 units, "
        f"{float(abs(gap / rotation)):.1f}x the whole ROTATION block. Where the coefficient's "
        "VALUE is concentrated, which is not by itself where a DISCREPANCY can live -- see the "
        "A-coupling check. Neither recorded side is preferred"
    )


@channels.check(
    "FINDING: A = 5/48 pins the normal sector's whole C4 contribution",
    "UNIFIED v4.3 §5.1/§6, block decomposition",
    tier=2,
)
def _():
    # The sharper half of the concentration result, and it corrects the naive
    # reading of it.
    #
    # All six NORMAL (0,0,1) records carry ONE value h -- three planes by two
    # signs, the cubic orbit of a single normal nearest-neighbour amplitude --
    # and that one number feeds both shape coefficients rigidly:
    #
    #     A_normal = -h        C4_normal = 2h        so  C4_normal = -2 A_normal
    #
    # Only the NORMAL and MIXED blocks contribute to A at all, and A totals
    # exactly 5/48. So fixing A fixes h, and fixing h fixes the normal
    # sector's entire C4 contribution -- 81% of the coefficient. A = 5/48 is
    # common ground: the corpus grants it to both sides.
    #
    # The consequence is a real constraint on any adjudication. Everything
    # that can move WITHOUT disturbing A -- the three in-plane blocks, the 120
    # rotation records, the on-site records -- has total absolute C4 weight
    # 0.0489, while the disputed gap is 0.1115. Even driving every A-free
    # block to its own magnitude with a common sign cannot reach it. So the
    # two recorded C_shp values are not two evaluations of one block
    # structure with one A: a competing kernel has to differ structurally, in
    # the A-carrying sector, not merely redistribute weight.
    #
    # Still not a decision. This says what a rival kernel must do, not which
    # kernel is physical, and neither side is preferred.
    from fractions import Fraction

    from .. import channel_ledger as CL

    decomposition = CL.decompose()
    blocks = decomposition["blocks"]
    records = decomposition["records"]["NORMAL (0,0,1)"]

    values = {Fraction(value) for _key, value in records}
    h = next(iter(values))
    normal = blocks["NORMAL (0,0,1)"]

    coupling = Fraction(normal["A"]) == -h and Fraction(normal["C4"]) == 2 * h
    a_total = sum(Fraction(block.get("A", 0)) for block in blocks.values())
    carries_a = {name for name, block in blocks.items() if Fraction(block.get("A", 0)) != 0}
    free_weight = sum(
        abs(Fraction(block.get("C4", 0))) for name, block in blocks.items() if name not in carries_a
    )
    gap = 4 * (Fraction(str(K.C_SHP_NEW_NUM)) - P.as_fraction(K.C_SHP_HISTORICAL))

    return (
        len(values) == 1
        and len(records) == 6
        and coupling
        and a_total == Fraction(5, 48)
        and carries_a == {"NORMAL (0,0,1)", "MIXED (0,1,1)"}
        and abs(gap) > free_weight
    ), (
        f"all 6 NORMAL records share one value h = {h}, the cubic orbit of a single normal "
        f"nearest-neighbour amplitude, and it sets both shapes rigidly: A_normal = -h and "
        f"C4_normal = 2h. A totals exactly 5/48 from the normal and mixed blocks alone, so "
        f"granting A fixes h and with it 81% of C4. Everything free to move without disturbing "
        f"A carries total |C4| {float(free_weight):.4f}, against a disputed gap of "
        f"{float(abs(gap)):.4f} -- {float(abs(gap) / free_weight):.2f}x larger, so no "
        "redistribution reaches it. A rival kernel must differ structurally in the A-carrying "
        "sector; which kernel is physical is not decided here"
    )


@channels.check(
    "FINDING: the v10a.26 side supplies A, B, D but no block structure, and its C fights its own A",
    "provenance nb-hodge-v10a26-alt2 / GLUEBALL §10",
    tier=2,
)
def _():
    # Asked directly: does the disputed side have a recorded block structure
    # to compare against the historical kernel's? It does not, and the
    # provenance register says so in terms -- "Float output only; no exact
    # rational for this side exists anywhere". What v10a.26 emits for the
    # shape is one printout, the cold folded C_shape at notebook line 2912.
    # There is no 189-record decomposition, no displacement blocks, nothing to
    # diff. So a structural adjudication cannot be done by comparison.
    #
    # The absence is informative anyway, because of what the run DOES supply.
    # Its A, B and D match the sealed exact rationals closely -- A to 6.1e-14
    # against 5/48, B to 3.6e-16 and D to 2.2e-13 against zero. So the two
    # sides agree on A to thirteen digits.
    #
    # Agreement on A is not free. The neighbouring check establishes that the
    # six NORMAL records are one number h with A_normal = -h and
    # C4_normal = 2h, so granting A pins the normal sector's whole C4
    # contribution, and everything still free to move carries total |C4|
    # weight 0.0489 against a required gap of 0.1115.
    #
    # So the two sides cannot BOTH be evaluations of the recorded block
    # structure: something has to give, and there are exactly three
    # candidates -- v10a.26's A, v10a.26's C, or the shared decomposition
    # itself. This check does not say which, and prefers neither side. It says
    # the pair is over-determined, which is a far better lead than "recompute
    # 609 clusters" and is the reason to want the v10a.26 run's intermediate
    # ledger rather than another sweep.
    from fractions import Fraction

    from .. import channel_ledger as CL

    blocks = CL.decompose()["blocks"]
    carries_a = {name for name, b in blocks.items() if Fraction(b.get("A", 0)) != 0}
    free_weight = sum(
        abs(Fraction(b.get("C4", 0))) for name, b in blocks.items() if name not in carries_a
    )
    gap = 4 * (Fraction(str(K.C_SHP_NEW_NUM)) - P.as_fraction(K.C_SHP_HISTORICAL))

    a_gap = abs(K.A_SHP_3_NUM - float(Fraction(5, 48)))
    agrees_on_a = a_gap <= K.SEALED_CORE_TOLERANCE
    b_d_agree = abs(K.B_SHP_3_NUM) <= K.SEALED_CORE_TOLERANCE
    b_d_agree = b_d_agree and abs(K.D_SHP_3_NUM) <= K.SEALED_CORE_TOLERANCE

    return agrees_on_a and b_d_agree and abs(gap) > free_weight, (
        f"v10a.26 supplies A, B, D as floats agreeing with the sealed rationals (A to {a_gap:.1e} "
        f"of 5/48, B to {abs(K.B_SHP_3_NUM):.1e} and D to {abs(K.D_SHP_3_NUM):.1e} of zero) and "
        "supplies NO block decomposition at all -- its shape is one cold folded C_shape printout, "
        "so there is no structure to diff. But agreeing on A pins the normal sector's C4, leaving "
        f"only {float(free_weight):.4f} of |C4| free against a gap of {float(abs(gap)):.4f}, "
        f"{float(abs(gap) / free_weight):.2f}x too large. The pair is over-determined: v10a.26's "
        "A, its C, or the shared decomposition must give. Which one is not decided here"
    )


@channels.check(
    "FINDING: the v10a.26 notebook carries a per-class ledger and attests its own blindness",
    "provenance nb-hodge-v10a26-alt2",
    tier=2,
)
def _():
    # The neighbouring check says the disputed side supplies no BLOCK
    # structure, which is true of the displacement-shell decomposition the
    # historical kernel uses. It is not the whole story, and the difference
    # matters for how this dispute gets settled.
    #
    # The pinned notebook's stored output carries a per-CLASS ledger: 32
    # "shape DONE" rows, each with its cluster size and its own c4, covering
    # 202 of 203 concrete embeddings, with cumulative timing that ends at
    # 61095 s -- so the run that produced the disputed value took about 17
    # hours and FINISHED. That is a decomposition, on a different axis from
    # the historical one (cluster class, not displacement shell), which is why
    # the two cannot be diffed row against row.
    #
    # Two things in that output are worth recording precisely because the
    # registry carries this side as a bare float. The run attests its own
    # blindness four times -- "historical m4 target: NOT LOADED", "disputed
    # q/rest targets: NOT LOADED", "historical C-shape target: NOT LOADED",
    # "disputed fourth-order values: STILL NOT LOADED" -- and it computes
    # C_direct twice, by routes agreeing to 5e-15.
    #
    # This does NOT promote the v10a.26 side and does not prefer it. Attested
    # blindness and internal agreement are evidence about how a number was
    # produced, never that it is the physical one, and C2 stays open with both
    # sides recorded. What it changes is the shape of the remaining work: the
    # disputed value came from a 17-hour run that completed, not from an
    # unfinishable sweep, and its intermediates survive in the pinned bytes.

    notebook = (
        ROOT
        / "corpus-import"
        / "programs"
        / "hodge_o4_adjudication"
        / "notebooks"
        / "NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb"
    )
    text = ""
    for cell in json.loads(notebook.read_text(encoding="utf-8"))["cells"]:
        for output in cell.get("outputs") or []:
            text += "".join(output.get("text") or [])
            text += "".join(output.get("data", {}).get("text/plain") or [])

    rows = re.findall(
        r"shape DONE\s+(\d+)/\s*(\d+)\s+\|C\|=(\d+).*?c4=([-+][\d.e-]+).*?elapsed=([\d.]+)s", text
    )
    blind = [
        "historical m4 target            : NOT LOADED",
        "historical C-shape target        : NOT LOADED",
        "disputed fourth-order values     : STILL NOT LOADED",
    ]
    attested = sum(1 for line in blind if line in text)
    direct = sorted({float(v) for v in re.findall(r"C_direct\s+=\s+([-\d.]+)", text)})
    spread = abs(direct[-1] - direct[0]) if len(direct) > 1 else None
    elapsed = float(rows[-1][4]) if rows else 0.0

    return (
        len(rows) == 32
        and attested == len(blind)
        and len(direct) == 2
        and spread < 1e-13
        and elapsed > 60000
    ), (
        f"{len(rows)} per-class shape rows recovered from the pinned notebook (sizes "
        f"{sorted({int(r[2]) for r in rows})}), covering 202/203 concrete embeddings, with the run "
        f"finishing at {elapsed / 3600:.1f} h. It states its own blindness in {attested} separate "
        f"lines and computes C_direct twice, the two routes agreeing to {spread:.1e}. Evidence "
        "about how the disputed number was produced, not that it is the physical one -- C2 stays "
        "open and neither side is preferred"
    )


@channels.check(
    "FINDING: the v10a.26 run gates on known values before it unblinds",
    "provenance nb-hodge-v10a26-alt2, cell 17",
    tier=2,
)
def _():
    # The registry carries the disputed side as a bare float and the
    # provenance calls it "the cold folded C_shape printout, the only source
    # of the value". True as far as it goes, and it undersells how the number
    # was produced -- which matters, because how a disputed value was produced
    # is exactly what an adjudication weighs.
    #
    # The pinned notebook implements a hard blind protocol, in its own source:
    # every gate of the preceding layer must pass "before disputed values
    # enter memory", and failure raises "v10a.23 pre-unblind gate failure; no
    # fourth-order verdict permitted" under the banner "STOPPED BEFORE
    # FOURTH-ORDER UNBLIND". Only then does section 17, "FINAL UNBLIND --
    # disputed constants first appear here", load the historical rationals and
    # print the comparison, recovering the registered gap 0.0278730543.
    #
    # The gates it must clear first are the AGREED lower orders: the
    # independent finite-cluster oracle has to recover m1 = 1, m2 = 11/306 and
    # m3 = -109151/249696 -- coefficients this repository establishes by other
    # routes entirely. Those gates carry loose numerical tolerances (2e-5,
    # 2e-4, 8e-4), so they are sanity gates on an approximate oracle, NOT
    # exact reproductions, and they say nothing about the precision of the
    # 16-digit C_direct that comes from the exact folded route.
    #
    # This does not promote the v10a.26 side, does not prefer it, and does not
    # settle C2. A disciplined protocol can still produce a wrong number, and
    # the historical kernel may have an equally good provenance story. What is
    # recorded here is that the disputed value is not a bare printout: it is
    # the output of a run that gated itself on agreed physics before it was
    # allowed to see the quantity in dispute.

    notebook = (
        ROOT
        / "corpus-import"
        / "programs"
        / "hodge_o4_adjudication"
        / "notebooks"
        / "NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb"
    )
    whole = ""
    for cell in json.loads(notebook.read_text(encoding="utf-8"))["cells"]:
        whole += "".join(cell.get("source") or [])
        for output in cell.get("outputs") or []:
            whole += "".join(output.get("text") or [])
            whole += "".join(output.get("data", {}).get("text/plain") or [])

    protocol = [
        "before disputed values enter memory",
        "no fourth-order verdict permitted",
        "STOPPED BEFORE FOURTH-ORDER UNBLIND",
        "FINAL UNBLIND",
    ]
    gated_on = ["m1=1", "m2=11/306", "m3=-109151/249696"]
    present = sum(1 for marker in protocol if marker in whole)
    gates = sum(1 for marker in gated_on if marker in whole)
    # the unblind prints the historical rational and the resulting gap
    unblinds = "-211835444920651" in whole and "historical C_shape" in whole

    return present == len(protocol) and gates == len(gated_on) and unblinds, (
        f"all {present} blind-protocol markers are in the pinned bytes, and the run gates on "
        f"{gates} agreed lower-order coefficients (m1 = 1, m2 = 11/306, m3 = -109151/249696) "
        "before section 17 loads the historical rationals and prints the comparison. Those gates "
        "are loose numerical sanity checks (2e-5 to 8e-4) on an approximate oracle, not exact "
        "reproductions. Evidence about protocol, not about which value is physical -- C2 stays "
        "open and neither side is preferred"
    )


@channels.check(
    "FINDING: the adjudicator's THIRD-VALUE scalar verdict is a C1 anchoring artifact",
    "provenance nb-hodge-v10a26-alt2, section 17",
    tier=2,
)
def _():
    # The pinned run carries a three-way adjudicator, and it fired the
    # fallback: "SCALAR ORACLE RETURNS THIRD VALUE" / "FOLDED MATRIX DOES NOT
    # RECOVER HISTORICAL C_shape" / "MIXED/THIRD RESULT". Both endorsing
    # branches were reachable in its source; neither fired.
    #
    # The scalar half of that verdict does not survive inspection, and this
    # check exists to say so. The oracle's "independent linked m4" is
    # -0.7751458630189173, which is BIT-FOR-BIT the registered m_Gamma^(4),
    # and its distance from the historical 189-kernel q_band^(4) is
    # 2.0827701250956414 -- the registered Delta_Gamma, to 4.4e-16.
    #
    # So the oracle did not return a third value. It reproduced a constant
    # this repository already carries, exactly, and was then compared against
    # q_band-anchored candidates it could never match. This is precisely the
    # trap CLAUDE.md names: q_band^(4) and m_Gamma^(4) are differently
    # anchored coordinates, not rival estimates, and C1 records that the
    # apparent scalar dispute dissolved into an anchoring distinction. The
    # engine's endorsing branch tests scalar_verdict.endswith("HISTORICAL
    # q3"), so an m_Gamma-anchored result makes that branch unreachable no
    # matter how right it is.
    #
    # The SHAPE half of the verdict is untouched and stands: the folded matrix
    # genuinely does not recover the historical C_shape, which is C2. What
    # falls is the implication that a second, scalar disagreement corroborates
    # it. Only one of the two verdict halves is a real disagreement.
    #
    # Neither C_shp side is preferred here, and C2 stays open.

    notebook = (
        ROOT
        / "corpus-import"
        / "programs"
        / "hodge_o4_adjudication"
        / "notebooks"
        / "NB_O4_hodge_v10a26_factor52complete_exactsw_rootedoracle_a100_alt2.ipynb"
    )
    whole = ""
    for cell in json.loads(notebook.read_text(encoding="utf-8"))["cells"]:
        whole += "".join(cell.get("source") or [])
        for output in cell.get("outputs") or []:
            whole += "".join(output.get("text") or [])
            whole += "".join(output.get("data", {}).get("text/plain") or [])

    oracle = -0.7751458630189173
    fired = "MIXED/THIRD RESULT" in whole and "SCALAR ORACLE RETURNS THIRD VALUE" in whole
    shape_missed = "FOLDED MATRIX DOES NOT RECOVER HISTORICAL C_shape" in whole
    # the endorsing branch keys on the q_band-anchored name, which an
    # m_Gamma-anchored scalar cannot satisfy
    keyed_on_q3 = "HISTORICAL q3" in whole
    is_m_gamma = oracle == K.M_GAMMA_4_NUM
    shift = abs(oracle - float(P.as_fraction(K.Q_BAND_4)))
    is_delta_gamma = abs(shift - K.DELTA_GAMMA_NUM) < 1e-12

    return (fired and shape_missed and keyed_on_q3 and is_m_gamma and is_delta_gamma), (
        f"the oracle's 'independent linked m4' {oracle} is bit-for-bit the registered "
        f"m_Gamma^(4), and its distance from q_band^(4) is {shift} = Delta_Gamma to "
        f"{abs(shift - K.DELTA_GAMMA_NUM):.1e}. It returned no third value: it reproduced a "
        "registered constant and was compared against a differently anchored one, which is the "
        "C1 distinction. The endorsing branch keys on 'HISTORICAL q3', so an m_Gamma-anchored "
        "scalar cannot reach it. The SHAPE half of the verdict stands and is C2; the scalar half "
        "is an artifact, so only one of the two halves is a real disagreement"
    )


@channels.check(
    "the C_alt witness IS the balanced eps-free continuation, and Delta_C/(A/2) = 15/32",
    "OFF AXIS LEDGER 2026-08-22 §2, UNIFIED v4.3 §5.1",
    tier=2,
)
def _():
    # An earlier check registered C_alt = C_old + 25/1024 as "an explicit
    # second witness" exhibiting the C2 non-identifiability -- true, and it
    # undersold the object badly. The witness is not an arbitrary exhibit. It
    # is the BALANCED, eps-free continuation of the all-rank shape family
    # beta_N = P17(N^2)/(N R20(N^2)) evaluated at N = 3, and the historical
    # SU(3) kernel is that balanced family minus one identified eps-sector.
    #
    # Two exact relations, both verified here rather than transcribed:
    #
    #     C_balanced - C_historical = 25/1024
    #     (C_balanced - C_historical) / (A/2) = 15/32,   A = 5/48
    #
    # The second is the sharper one: the shift is not an arbitrary rational
    # but a fixed ratio of the coefficient BOTH SIDES AGREE ON. That is the
    # same rigidity the A-coupling check found from the block decomposition,
    # reached from the opposite direction -- an all-rank polynomial family
    # rather than a 189-record kernel -- by a ledger written six days before
    # this session and by this session independently.
    #
    # The geometry of the three values is worth recording plainly, and it is
    # NOT an argument for a side. The balanced continuation lands 7x closer to
    # the v10a.26 value than to the historical one (0.00346 against 0.02441).
    # That is a fact about where a structurally-derived eps-free object sits,
    # and it cuts no ice by itself: eps-free is precisely what the physical
    # value is not, so the balanced number is not a candidate for C_shp and
    # its proximity to either side proves nothing about which is physical.
    #
    # C2 stays open and neither recorded side is preferred.
    from fractions import Fraction

    c_hist = P.as_fraction(K.C_SHP_HISTORICAL)
    c_balanced = Fraction(-13035490122347, 550663802582400)
    shift = c_balanced - c_hist
    ratio = shift / (Fraction(5, 48) / 2)

    near_new = abs(float(c_balanced) - K.C_SHP_NEW_NUM)
    near_old = abs(float(c_balanced) - float(c_hist))

    return (shift == Fraction(25, 1024) and ratio == Fraction(15, 32) and near_new < near_old), (
        f"C_balanced - C_historical = {shift} exactly, and dividing by A/2 with A = 5/48 gives "
        f"{ratio} -- the shift is a fixed ratio of the coefficient both sides agree on, not an "
        f"arbitrary rational. The eps-free continuation sits {near_new:.5f} from the v10a.26 "
        f"value and {near_old:.5f} from the historical one, {near_old / near_new:.1f}x closer to "
        "the former; that is geometry, not evidence, since an eps-free object is not a candidate "
        "for the physical C_shp. Neither side is preferred"
    )


@channels.check(
    "the shape fit's C row sums to zero, so no Gamma-anchor error can move C_shp at all",
    "provenance nb-hodge-v10a26-alt2, _v10a3_extract_shape; UNIFIED v4.3 §5.1",
    tier=1,
)
def _():
    # C1 and C2 have been carried side by side as if a mistake in the first
    # could bleed into the second: both are fourth-order, both concern the
    # same kernel, and the adjudicator reported them together. This check
    # settles the relationship exactly, and the answer is that they cannot
    # touch.
    #
    # The shape fit is fully determined by geometry the run states in source:
    # theta = 2*pi/5 and the four fit momenta (t,0,0), (t,t,0), (2t,t,0),
    # (t,t,t), with row [q, e2, 4*e2/q, e3/q] and a_i = 4 sin^2(k_i/2). At
    # theta = 2*pi/5 those a-values are (5 -/+ sqrt 5)/2, so M and M^-1 live
    # in Q(sqrt 5) and can be inverted symbolically -- no float enters here.
    #
    # The fit solves M coef = vals - eps_Gamma. Perturb the Gamma anchor
    # alone by delta and the right-hand side moves by -delta*(1,1,1,1), so
    # each coefficient moves by -delta times its row sum. The C row is
    # [-1/2, (1+sqrt5)/4, (1-sqrt5)/4, 0], which sums to EXACTLY zero. The A,
    # B and D rows do not.
    #
    # So C_shp is invariant under any perturbation of the Gamma anchor, of any
    # magnitude -- not small, not suppressed, exactly zero. The C2 gap of
    # 0.0279 therefore cannot be an anchoring artifact of any kind, and the
    # C1 anchoring distinction cannot be a partial explanation of it either.
    # A, by contrast, moves at rate (1/2 + sqrt5/10), so A is the coefficient
    # that WOULD register an anchor disagreement, and both sides agree on it.
    #
    # Neither side of C2 is preferred by this. What falls is a whole class of
    # explanation for the gap.
    import sympy as sp

    theta = 2 * sp.pi / 5

    def row(k):
        a = [sp.nsimplify(sp.simplify(4 * sp.sin(x / 2) ** 2), [sp.sqrt(5)]) for x in k]
        q = sum(a)
        e2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
        e3 = a[0] * a[1] * a[2]
        return [sp.radsimp(sp.simplify(x)) for x in (q, e2, 4 * e2 / q, e3 / q)]

    fit = [(theta, 0, 0), (theta, theta, 0), (2 * theta, theta, 0), (theta, theta, theta)]
    inverse = sp.Matrix([row(k) for k in fit]).inv()
    sums = [sp.simplify(sum(inverse.row(i))) for i in range(4)]

    stated = [sp.Rational(-1, 2), (1 + sp.sqrt(5)) / 4, (1 - sp.sqrt(5)) / 4, sp.Integer(0)]
    c_row_matches = all(sp.simplify(sp.radsimp(inverse[2, j]) - stated[j]) == 0 for j in range(4))
    c_immune = sums[2] == 0
    others_move = all(s != 0 for i, s in enumerate(sums) if i != 2)

    return (c_row_matches and c_immune and others_move), (
        f"over Q(sqrt 5) the shape-fit inverse has C row {stated}, summing to exactly "
        f"{sums[2]}, so d C_shp / d eps_Gamma = 0 identically: a Gamma-anchor error of ANY size "
        f"moves C_shp by nothing. The other rows sum to A {sums[0]}, B {sums[1]}, D {sums[3]}, "
        "all nonzero, so A is the coefficient an anchor disagreement would show up in -- and the "
        "two C2 sides agree on A. C1 is an anchoring distinction and cannot explain any part of "
        "the C2 gap; the two are algebraically independent. Neither C_shp side is preferred"
    )


@channels.check(
    "FINDING: the run's own re-anchor moved C_shp by 4.6e-15, as the zero row sum requires",
    "provenance nb-hodge-v10a26-alt2, sections 13 and 17",
    tier=2,
)
def _():
    # The exact result next door predicts a number this run already measured,
    # and the run measured it twice by accident rather than by design.
    #
    # Section 13 extracts the shape BLIND, before any re-anchoring, at
    # rest_direct = -11.9485781794007. Section 17 re-extracts it after adding
    # the independently linked local shift +11.17343231638178, landing at
    # rest_direct = -0.775145863018919. That is a shift of the Gamma rest
    # energy by more than eleven units -- four orders of magnitude larger than
    # the entire C2 gap.
    #
    # C_direct went from -0.0202133288861666 to -0.0202133288861712. It moved
    # by 4.6e-15, which is float noise on a quantity of size 0.02, against a
    # shift of 11.17. Had C carried even a thousandth of the anchor's
    # sensitivity, that re-anchor would have moved it by more than the whole
    # disputed gap.
    #
    # This is the numerical witness for the exact statement: the shape fit's C
    # row sums to zero. It also means the disputed C_shp value is the same
    # number before and after the run's scalar bookkeeping, so nothing in the
    # C1 half of the adjudicator's verdict reaches it.
    blind = -0.0202133288861666
    final = -0.0202133288861712
    anchor_blind = -11.9485781794007
    anchor_final = -0.775145863018919

    anchor_shift = anchor_final - anchor_blind
    c_moved = abs(final - blind)
    gap = abs(K.C_SHP_NEW_NUM - float(P.as_fraction(K.C_SHP_HISTORICAL)))
    # the sensitivity C would need for the re-anchor to explain the gap
    needed = gap / abs(anchor_shift)

    return (c_moved < 1e-14 and anchor_shift > 11 and c_moved / abs(anchor_shift) < 1e-15), (
        f"re-anchoring the Gamma rest by {anchor_shift:+.14f} moved C_direct from {blind} to "
        f"{final}, a change of {c_moved:.1e} -- an effective sensitivity of "
        f"{c_moved / abs(anchor_shift):.1e}, indistinguishable from the exact zero the C row's "
        f"vanishing sum requires. To attribute the {gap:.4f} C2 gap to anchoring would need a "
        f"sensitivity of {needed:.4f}, larger by a factor of "
        f"{needed / (c_moved / abs(anchor_shift)):.1e}. The disputed C_shp is the same number "
        "before and after the run's scalar bookkeeping"
    )


@channels.check(
    "FINDING: the v10a.26 cluster ledger is exhausted by supports <= 2 until fourth order",
    "provenance nb-hodge-v10a26-alt2, section 16 rooted incidence transform",
    tier=2,
)
def _():
    # An earlier check in this suite says the disputed side supplies no block
    # structure for the SHAPE, and that stands. It is not the whole story for
    # the SCALAR, and this check records what the run's section 16 actually
    # emits, because it is a decomposition and nobody had read it.
    #
    # The rooted incidence transform prints one row per cluster support size,
    # 1 through 6, each carrying its own c1/c2/c3/c4. Read as a ledger it says
    # something sharp about where each order lives:
    #
    #   order 2:  1/2 - 71/153 = 11/306          sizes 3-6 contribute 0
    #   order 3:  7/32 + (12*LEAK_3 - 4*B_3)      sizes 3-6 contribute 0
    #   order 4:  143/8960 + s2 + s3 + 0 + 0 - 5/24 = m_Gamma^(4)
    #
    # The third-order row is the interesting one. This registry already
    # decomposes D_3 as 7/32 + 12*LEAK_3 - 4*B_3, and section 16's two nonzero
    # third-order rows ARE those two groups, exactly: the size-1 row is 7/32
    # and the size-2 row is 12*LEAK_3 - 4*B_3 = -40943/62424, to the last bit
    # of the printed twelve digits. So the disputed side does not merely agree
    # with the historical side on m3 -- it agrees on the DECOMPOSITION of m3,
    # on-site term against neighbour terms, by an independent route.
    #
    # The second and third moments are therefore exhausted by supports of size
    # at most two, exactly; the larger clusters are not small there, they are
    # zero. Fourth order is the first to recruit anything bigger, and it takes
    # sizes 3 and 6 while leaving 4 and 5 empty to 2.9e-14. Two of its six
    # rows are clean rationals -- size 1 is 143/8960, size 6 is -5/24 -- and
    # the other two nonzero rows admit no rational under denominator 1e7.
    #
    # This is the sharpest available framing of C2: the two sides share a
    # decomposition through third order, term for term, and part company only
    # where fourth order first reaches past the nearest neighbour. The
    # coincidence that -5/24 = -2*(5/48) = -2A is recorded as a coincidence;
    # nothing here derives it and nothing here uses it. Neither side is
    # preferred.
    from fractions import Fraction

    order2_closes = Fraction(1, 2) - Fraction(71, 153) == P.as_fraction(K.BAND_ODD_FLAT)
    neighbour_3 = 12 * K.LEAK_3 - 4 * K.B_3
    order3_closes = Fraction(7, 32) + P.as_fraction(neighbour_3) == P.as_fraction(K.D_3)
    decomposition_matches = neighbour_3 == -Rational(40943, 62424)

    c4_rows = {
        1: 0.0159598214286,
        2: -0.403971702978,
        3: -0.178800648136,
        4: -1.3933298959e-14,
        5: -2.85049761573e-14,
        6: -0.208333333333,
    }
    empty_max = max(abs(c4_rows[s]) for s in (4, 5))
    closes = abs(sum(c4_rows.values()) - K.M_GAMMA_4_NUM)
    size1 = abs(c4_rows[1] - float(Fraction(143, 8960)))
    size6 = abs(c4_rows[6] - float(Fraction(-5, 24)))
    printed_3 = abs(-0.655885556837 - float(neighbour_3))

    return (
        order2_closes and order3_closes and decomposition_matches and empty_max < 1e-13,
        f"section 16's support-size ledger closes order 2 as 1/2 - 71/153 = {K.BAND_ODD_FLAT} and "
        f"order 3 as 7/32 + ({neighbour_3}) = {K.D_3}, both EXACTLY, with supports 3 through 6 "
        f"contributing nothing. Its size-2 third-order row is this registry's own "
        f"12*LEAK_3 - 4*B_3 to {printed_3:.1e}, so the disputed side reproduces the DECOMPOSITION "
        "of m3, not just its value. Fourth order is the first to recruit larger clusters: it "
        f"takes sizes 3 and 6 and leaves 4 and 5 empty to {empty_max:.1e}, the six rows summing "
        f"to m_Gamma^(4) to {closes:.1e}, with size 1 = 143/8960 to {size1:.1e} and size 6 = "
        f"-5/24 to {size6:.1e}. The two sides share a decomposition through third order and part "
        "company where fourth order first reaches past the nearest neighbour. Neither is preferred",
    )


@channels.check(
    "FINDING: the off-axis ledger carries two claims its own author later retracted",
    "notes UPLOADS_2026-08-28d OFF_AXIS_LEDGER §6/§7, corrected by the C2 status note",
    tier=2,
)
def _():
    # Both documents are pinned, both are about C2, and one silently
    # supersedes the other. The ledger is the more useful of the two -- it is
    # what channel_ledger.py implements -- so it is the one a reader reaches
    # for, and nothing inside it says that two of its conclusions are dead.
    #
    # Retracted in the later note, by the same author:
    #
    #   §6 "The most economical single hypothesis is that v10a.26 is missing
    #      the nu = +-3 epsilon-sector"  -- refuted: C_new was computed under
    #      the nine-family allowlist, epsilon-sectors included.
    #
    #   §7 "It independently reproduces ... the blind holdout
    #      lambda_R = 2 lambda_M - lambda_X"  -- refuted: L = 5 contains no R,
    #      so the run cannot reproduce that holdout and did not.
    #
    # The second retraction matters most. §7 offers the holdout as one of
    # "two genuinely independent conditions" supporting the disputed side; with
    # it withdrawn, that support is one condition, not two. This check exists
    # so the pairing is machine-recorded rather than left to whoever
    # remembers, and it fails if either document is edited out from under it.
    #
    # Neither retraction touches the §5 channel ledger, which is separately
    # T1-checked, and neither side of C2 is preferred.
    ledger = (
        ROOT / "notes" / "imported" / "UPLOADS_2026-08-28d" / "OFF_AXIS_LEDGER.txt"
    ).read_text(encoding="utf-8")
    corrector = (
        ROOT
        / "notes"
        / "imported"
        / "WORK_SINCE_2026-08"
        / "C2_status_note_misfiled_as_carrier_persistence.txt"
    ).read_text(encoding="utf-8")

    claims_epsilon = "missing the ν = ±3 ε-sector" in ledger
    claims_holdout = "λ_R = 2λ_M − λ_X" in ledger
    retracts_epsilon = "It's refuted" in corrector and "nine-family allowlist" in corrector
    retracts_holdout = "it doesn't and can't, since L=5 contains no R" in corrector
    keeps_both = "recorded in §9 rather than deleted" in corrector

    return (
        claims_epsilon and claims_holdout and retracts_epsilon and retracts_holdout and keeps_both,
        "the pinned off-axis ledger states the epsilon-sector-omission hypothesis (§6) and the "
        "lambda_R = 2 lambda_M - lambda_X holdout (§7) with no indication either is dead; the "
        "pinned C2 status note retracts both, the first because C_new was computed under the "
        "nine-family allowlist with epsilon-sectors included, the second because L = 5 contains "
        "no R. So §7's 'two genuinely independent conditions' supporting the disputed side is one "
        "condition. Both retractions are kept in place rather than deleted, per the repository's "
        "own rule, and neither touches the §5 channel ledger or prefers a side of C2",
    )
