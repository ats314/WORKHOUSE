from __future__ import annotations

import json

from sympy import (
    Rational,
    diff,
    lcm,
    pi,
    simplify,
    symbols,
    sympify,
)

from .. import constants as K
from .. import triage as TRIAGE
from ._core import PAPER_DIR, _suite
from ._shared import MASTER_EDITION, _master_edition_text

# ==========================================================================
pentagonal = _suite("isotropic pentagonal cap band (v4.3 §9.3)")
# A separate geometry and retained sector. Nothing here bears on the cubic
# SU(3) fourth-order kernel, and the checks say so where it would be tempting
# to borrow a number across.


@pentagonal.check("the two face energies differ, so the eigenspace must be chosen", "§9.3 / C8")
def _():
    # H_0 = (1/2) sum_e E_e^2 with E_cap = 10/3, E_side = 8/3. Because these are
    # unequal there is no single equal-energy one-face manifold to fall into by
    # default: the physical sector is the charge-odd cap sector, and the formal
    # cap-plus-side cycle space is a different object (R21).
    gap = K.E_CAP - K.E_SIDE
    return K.E_CAP != K.E_SIDE and gap == Rational(2, 3), (
        f"E_cap = {K.E_CAP}, E_side = {K.E_SIDE}, gap = {gap}; the degenerate "
        "space is not the whole one-face space"
    )


@pentagonal.check("h_4^side = A_+ - A_- exactly", "§9.3")
def _():
    diff_ = K.PENT_A_PLUS - K.PENT_A_MINUS
    return diff_ == K.H4_SIDE, (
        f"A_+ = {K.PENT_A_PLUS}, A_- = {K.PENT_A_MINUS}, "
        f"A_+ - A_- = {diff_} = h_4^side = {K.H4_SIDE}"
    )


@pentagonal.check("the h_4^side -> tau_4 factor is exactly 5", "§9.3")
def _():
    # Exact D_5 covariance. Recording the multiplier is the point: two printed
    # coefficients differing by an undocumented integer factor are
    # indistinguishable from a transcription error until someone names the group.
    ratio = K.TAU_4 / K.H4_SIDE
    return ratio == K.D5_COVARIANCE_FACTOR, (
        f"tau_4 / h_4^side = {ratio}, the order of the cyclic symmetry C_5 "
        f"of the pentagonal cap; tau_4 = {K.TAU_4}"
    )


@pentagonal.check("the tau_4 -> Delta E_cap factor is exactly 2", "§9.3")
def _():
    # The two terms of the Hermitian hop |a_z><a_{z+1}| + |a_{z+1}><a_z|, which
    # is why cos k rather than exp(ik) appears. Not a second convention.
    ratio = K.DELTA_E_CAP_4 / K.TAU_4
    return ratio == K.HOP_HERMITIAN_FACTOR, (
        f"Delta E_cap^(4) / tau_4 = {ratio}; the hop is Hermitian, so the "
        f"symbol is 2 tau_4 cos k with 2 tau_4 = {K.DELTA_E_CAP_4}"
    )


@pentagonal.check("bandwidth = 4|tau_4| and the band minimum sits at k = 0", "§9.3")
def _():
    k = symbols("k", real=True)
    symbol = K.DELTA_E_CAP_4 * sympify("cos(k)").subs(symbols("k"), k)
    width = simplify(symbol.subs(k, pi) - symbol.subs(k, 0))
    at_zero = symbol.subs(k, 0)
    at_pi = symbol.subs(k, pi)
    return (
        width == K.PENT_BANDWIDTH_4 and 4 * abs(K.TAU_4) == K.PENT_BANDWIDTH_4 and at_zero < at_pi
    ), (
        f"2 tau_4 (cos pi - cos 0) = {width} = 4|tau_4| = {K.PENT_BANDWIDTH_4}; "
        f"E(0) = {at_zero} < E(pi) = {at_pi}, so tau_4 < 0 puts the minimum at k = 0"
    )


@pentagonal.check("240 = 5 x 48 histories per adjacent direction", "§9.3")
def _():
    return K.PENT_HISTORIES_PER_DIRECTION == 5 * K.PENT_FIXED_SIDE_HISTORIES, (
        f"{K.PENT_HISTORIES_PER_DIRECTION} = 5 x {K.PENT_FIXED_SIDE_HISTORIES}: the "
        "48 fixed-side histories carried around the five cap positions, which is "
        "the same C_5 orbit that produced the factor 5 above"
    )


@pentagonal.check("hop range 4 refutes the r = w_min - 2 promotion", "§9.3 / C6")
def _():
    # C6: the promotion r_physical = w_min - 2 is falsified here. w_min = 7 for
    # this geometry, so the rule predicts 5 while the exact calculation gives 4.
    w_min = 7
    predicted = w_min - 2
    return K.PENT_HOP_RANGE == 4 and predicted == 5 and predicted > K.PENT_HOP_RANGE, (
        f"r_hop = {K.PENT_HOP_RANGE}, but w_min - 2 = {predicted}; the scoped "
        "bound r >= w_min - 2 does not survive as an equality"
    )


@pentagonal.check("the tuned cap-plus-side symbol is a different Hamiltonian", "§9.3 / R21")
def _():
    # mu(k) = 4 cos k (1 - cos k)/(7 - 2 cos k) is the OLD formal compression. It
    # is not proportional to the isotropic symbol cos k, so no rescaling carries
    # h_4^side across; the tuned model needs w_vertical = (3/2) w_horizontal.
    k = symbols("k", real=True)
    c = sympify("cos(k)").subs(symbols("k"), k)
    mu = 4 * c * (1 - c) / (7 - 2 * c)
    ratio = simplify(mu / c)
    return simplify(diff(ratio, k)) != 0 and Rational(3, 2) == K.PENT_TUNED_WEIGHT_RATIO, (
        f"mu(k)/cos k = {ratio} is k-dependent, so mu is not a multiple of the "
        f"isotropic symbol; the tuned model requires w_vertical/w_horizontal = "
        f"{K.PENT_TUNED_WEIGHT_RATIO} and a fresh anisotropic backend"
    )


@pentagonal.check("h_4^side and the cubic kernel share no denominator structure", "§9.3")
def _():
    # Guard against the most natural misuse: quoting the pentagonal coefficient
    # as though it constrained the disputed cubic fourth order.
    shared = K.H4_SIDE.q == K.Q_BAND_4.q
    return not shared, (
        f"h_4^side has denominator {K.H4_SIDE.q}, q_band^(4) has "
        f"{K.Q_BAND_4.q}; separate geometries, separate retained sectors, and "
        "the pentagonal theorem leaves the cubic fourth-order scalar untouched"
    )


@pentagonal.check(
    "the target-blind backend cold-reproduces A_+, A_- and h_4^side",
    "runs/blind_pentagonal_o4_2026-08-28",
)
def _():
    # h_4^side was registered and checked as A_+ - A_-, but A_+ and A_- were
    # themselves transcriptions: nothing here derived them. On 2026-08-28 a
    # cold pentagonal-prism backend reached this session -- one that had been
    # missing from every notes inventory -- and was run unmodified. It
    # enumerates all 48 fixed-side endpoint histories from oriented geometry,
    # exact Wilson trace-word algebra, the SU(N) Fierz identity and exact
    # SU(3) Haar projectors, and returns BOTH amplitudes, not just the gap.
    #
    # The blindness is measured, not accepted on the engine's word: the
    # coefficient-signature scanner finds no registered coefficient in the
    # pinned source, so the engine cannot have been fitted to a value it does
    # not contain. That is asserted below alongside the arithmetic.
    #
    # SCOPE: this is the pentagonal SIDE coefficient. It does not adjudicate
    # C2 -- the disputed off-axis C_shp lives in the cubic kernel, a separate
    # geometry, which the neighbouring denominator-structure check pins. G3
    # still wants a blind run of the marked-cluster CUBIC engine.
    run = PAPER_DIR.parent / "runs" / "blind_pentagonal_o4_2026-08-28"
    result = json.loads((run / "blind_result.json").read_text(encoding="utf-8"))
    source = (
        PAPER_DIR.parent
        / "notes"
        / "imported"
        / "UPLOADS_2026-08-28c"
        / "backend_full_link_balanced_control.py"
    )
    scanned = TRIAGE.scan(source.parent)
    carried = set(next(f for f in scanned.files if f.path.name == source.name).coefficients)

    subtotals = result["endpoint_direct_subtotals"]
    cold_plus = Rational(subtotals["+cap1"])
    cold_minus = -Rational(subtotals["-cap1_signed"])
    cold_h4 = Rational(result["h4_side"])
    gates = result["gates"]

    agrees = (
        cold_plus == K.PENT_A_PLUS
        and cold_minus == K.PENT_A_MINUS
        and cold_h4 == K.H4_SIDE
        and cold_h4 == cold_plus - cold_minus
    )
    return agrees and not carried and gates["all_pass"] and result["cold_run"], (
        f"cold A_+ = {cold_plus} and A_- = {cold_minus} reproduce the registry exactly, and their "
        f"difference is h_4^side = {cold_h4}; {gates['passed']}/{gates['total']} engine gates pass "
        f"and the pinned source carries {len(carried)} registered coefficient signatures, so the "
        "run was blind by measurement. Both amplitudes were transcriptions until this run; the "
        "pentagonal side geometry is separate from the cubic kernel, and this adjudicates "
        "no C_shp side"
    )


@pentagonal.check(
    "the fifth-order record is arithmetically self-consistent",
    "master edition 2026-08-28 §15",
)
def _():
    # The pentagonal fifth-order coefficient is ASSERTED by the master edition
    # -- two target-blind direct routes over 796 histories and a second ledger
    # over 572 canonical returns. Nothing here re-runs those histories, so the
    # physics stays T3 and this check does not promote it.
    #
    # What is checkable is the record's own internal arithmetic, and it is
    # worth checking for the reason this repository already has a one-ulp
    # transcription on file: a printed decomposition that does not sum to its
    # printed total is a transcription error, and nothing else would catch it.
    # The denominator test is the sharper half -- if the stated total had been
    # copied from a different computation, the odds of it landing exactly on
    # lcm(direct, folded) are negligible.
    #
    # The tau_4 tie is the link to evidence that IS checked here: the same
    # section prints tau_4 = -2861009/16877460600, which the target-blind
    # backend reproduced cold in runs/blind_pentagonal_o4_2026-08-28.
    total = K.C5_DIRECT + K.C5_FOLDED
    denominators_agree = K.C5_PENT.q == lcm(K.C5_DIRECT.q, K.C5_FOLDED.q)
    tau_tie = K.TAU_4 == K.D5_COVARIANCE_FACTOR * K.H4_SIDE
    # All three constants were entered here by one hand from one document. Sum
    # and lcm alone would therefore certify a self-consistent transcription of
    # the WRONG numbers, so read them back out of the pinned edition.
    source = _master_edition_text()
    quoted = all(
        str(value) in source
        for rational in (K.C5_DIRECT, K.C5_FOLDED, K.C5_PENT, K.TAU_4)
        for value in (abs(rational.p), rational.q)
    )
    return total == K.C5_PENT and denominators_agree and tau_tie and quoted, (
        f"direct + folded = {total} exactly, and its denominator is exactly "
        f"lcm({K.C5_DIRECT.q}, {K.C5_FOLDED.q}), so nothing cancelled silently; the same "
        f"section's tau_4 is {K.D5_COVARIANCE_FACTOR} x h_4^side, and every numerator and "
        f"denominator here appears verbatim in the pinned edition ({MASTER_EDITION.name}); "
        "h_4^side is the value the "
        "target-blind backend reproduced cold. The 796 direct and 572 folded histories are NOT "
        "re-run here: the fifth-order coefficient stays T3, asserted by the edition"
    )
