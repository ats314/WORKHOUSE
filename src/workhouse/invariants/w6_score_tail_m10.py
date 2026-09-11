"""Exact checks for the M10 reduction (W6 conditional score domination).

M10 itself is open. These checks establish only the exact pieces recorded in
docs/derivations/w6-conditional-score-tail-m10.md: the constrained minimum
potential, the S12 tangency for an arbitrary cutoff, the potential floor, the
supremum used by the rare-fiber term, the synthesis algebra that turns the
hypotheses H1-H5 into explicit constants, the M12/M15 coefficient algebra, and
the soft-mode divergence that obstructs a nine-dimensional Gaussian tube
estimate near the antipode. Nothing here bounds the actual ground state.
"""

from __future__ import annotations

import sympy as sp

from ._core import _suite
from .w6_antipodal import C, S, _quadratic_data

score_tail = _suite("W6 M10 reduction to three obligations")
CITE = "W6_CONDITIONAL_SCORE_TAIL_M10"

MINIMUM = "W6 M10 reduction: constrained minimum potential and antipodal value"
TANGENCY = "W6 M10 reduction: synchronized tangency for every cutoff"
FLOOR = "W6 M10 reduction: potential floor v_* >= |q|^2/(2 pi^2)"
SUPREMUM = "W6 M10 reduction: exact supremum of g^-p exp(-c/g^2)"
SYNTHESIS = "W6 M10 reduction: synthesis constants from the five hypotheses"
HARDY = "W6 M10 reduction: M12 and M15 coefficients from M11"
SOFT_MODE = "W6 M10 reduction: soft-mode moment diverges like 1/(2 sqrt2 delta)"

theta = sp.Symbol("theta", positive=True)


@score_tail.check(MINIMUM, CITE + " R2")
def constrained_minimum_potential():
    _, _, _, potential, _, _, t = _quadratic_data()
    constant = sp.expand(potential.coeff(t, 0))
    # A = (C, 0, 0, S) is the quarter-angle factor, so C = cos(theta/4).
    v_star = constant.subs({C: sp.cos(theta / 4), S: sp.sin(theta / 4)})
    closed = 16 * (1 - sp.cos(theta / 4))
    half_angle = 32 * sp.sin(theta / 8) ** 2
    at_pi = v_star.subs(theta, sp.pi)
    ok = (
        sp.simplify(v_star - closed) == 0
        and sp.simplify(closed - half_angle) == 0
        and sp.simplify(at_pi - (16 - 8 * sp.sqrt(2))) == 0
    )
    return (
        ok,
        "A2 constant term 16 - 16C with C = cos(theta/4) gives v_*(theta) = "
        "16(1 - cos(theta/4)) = 32 sin^2(theta/8); v_*(pi) = 16 - 8 sqrt2 matches A12.",
        {"V_STAR_ANTIPODE_THETA": 16 * (1 - sp.cos(theta / 4))},
    )


@score_tail.check(TANGENCY, CITE + " R3")
def synchronized_tangency_any_cutoff():
    chi = sp.Function("chi")
    r = sp.Symbol("r", positive=True)
    profiles = {
        "z0": r * chi(4 * r),
        "z1": r * chi(4 * r),
        "z2": r * chi(2 * r),
        "zQ": r * chi(r),
    }
    # Radii of the four factors on m(q): A, A, A^2, Q = A^4 with A = exp(theta n / 4).
    speeds = (
        profiles["z0"].subs(r, theta / 4),
        profiles["z1"].subs(r, theta / 4),
        profiles["z2"].subs(r, theta / 2),
    )
    z_q = profiles["zQ"].subs(r, theta)
    dm = (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2))
    drift = [sp.simplify(speed - d * z_q) for speed, d in zip(speeds, dm, strict=True)]
    return all(entry == 0 for entry in drift), (
        "With z0 = z1 = r chi(4r), z2 = r chi(2r), zQ = r chi(r) and chi arbitrary, "
        "Z_y(m(q),q) - Dm(q) Z_q(q) = 0 identically, so the S12 linear term vanishes."
    )


@score_tail.check(FLOOR, CITE + " R4", rests_on=(MINIMUM,))
def potential_floor():
    x = sp.Symbol("x", positive=True)
    f = sp.sin(x) - 2 * x / sp.pi
    endpoints = f.subs(x, 0) == 0 and sp.simplify(f.subs(x, sp.pi / 2)) == 0
    # f'' = -sin x < 0 on (0, pi/2): f is concave with zero endpoints, hence f >= 0.
    concave = sp.simplify(sp.diff(f, x, 2) + sp.sin(x)) == 0
    # Exact rational-grid confirmation of the squared consequence on [0, pi].
    grid_ok = all(
        (32 * sp.sin(th / 8) ** 2 - 2 * th**2 / sp.pi**2).evalf(60) >= 0
        for th in [sp.pi * sp.Rational(k, 64) for k in range(65)]
    )
    identity = sp.simplify(32 * (2 * x / sp.pi) ** 2 - 128 * x**2 / sp.pi**2) == 0
    return endpoints and concave and grid_ok and identity, (
        "sin x >= 2x/pi on [0, pi/2] by concavity with zero endpoints; with x = theta/8 "
        "this gives 32 sin^2(theta/8) >= 2 theta^2/pi^2 = |q|^2/(2 pi^2) for |q| = 2 theta."
    )


@score_tail.check(SUPREMUM, CITE + " R5")
def exact_supremum():
    t, c, p = sp.symbols("t c p", positive=True)
    h = t ** (p / 2) * sp.exp(-c * t)
    stationary = sp.solve(sp.Eq(sp.diff(sp.log(h), t), 0), t)
    value = sp.simplify(h.subs(t, p / (2 * c)))
    general = sp.simplify(value - (p / (2 * sp.E * c)) ** (p / 2)) == 0
    six = sp.simplify(value.subs(p, 6) - (3 / (sp.E * c)) ** 3) == 0
    second = sp.simplify(sp.diff(sp.log(h), t, 2))
    return (
        stationary == [p / (2 * c)] and general and six and second == -p / (2 * t**2),
        "sup_g g^-p exp(-c/g^2) = (p/(2ec))^(p/2), attained at g^-2 = p/(2c); "
        "p = 6 gives (3/(ec))^3. Any polynomial order is absorbed by the exponential.",
        {"SUP_G6_EXP_COEFFICIENT": (3 / (sp.E * c)) ** 3},
    )


@score_tail.check(SYNTHESIS, CITE + " R6", rests_on=(FLOOR,))
def synthesis_constants():
    cF, ca, c2, c4, c6, C_out, C_ant, g, W = sp.symbols(
        "c_F c_a c_2 c_4 c_6 C_out C_ant g W", positive=True
    )
    s, p = sp.symbols("s p", nonnegative=True)  # |q|^2 = 2 pi^2 g^2 W s, tube mass p
    v_b = sp.Symbol("v_b", positive=True)  # v_*(theta_b)
    q2 = 2 * sp.pi**2 * g**2 * W * s
    s14 = 4 * cF**2 * (c4 * q2 / g**2 + c6) + 2 * ca**2 * c2
    C0 = 4 * cF**2 * c6 + 2 * ca**2 * c2 + C_out
    C1_tube = 8 * sp.pi**2 * cF**2 * c4
    C1 = sp.Max(C1_tube, C_ant / v_b)
    # Region theta < theta_b: K <= p * S14 + C_out with p, s in [0, 1].
    slack_tube = sp.expand(C0 + C1_tube * W - (p * s14 + C_out))
    # slack = (1 - p)(4 cF^2 c6 + 2 ca^2 c2) + 8 pi^2 cF^2 c4 W (1 - p s): nonnegative.
    target = (1 - p) * (4 * cF**2 * c6 + 2 * ca**2 * c2) + C1_tube * W * (1 - p * s)
    tube_ok = sp.expand(slack_tube - target) == 0
    # Region theta >= theta_b: W >= v_b / g^2, so C_ant / g^2 <= (C_ant / v_b) W.
    W_ant = v_b / g**2 + sp.Symbol("excess", nonnegative=True)
    ant_ok = (
        sp.simplify((C_ant / v_b) * W_ant - C_ant / g**2)
        == C_ant * sp.Symbol("excess", nonnegative=True) / v_b
    )
    # C1 = Max(C1_tube, C_ant/v_b) dominates each candidate by definition of Max.
    return bool(tube_ok and ant_ok and set(C1.args) == {C1_tube, C_ant / v_b}), (
        "H1-H5 give M10 with C0 = 4 c_F^2 c_6 + 2 c_a^2 c_2 + C_out and "
        "C1 = max(8 pi^2 c_F^2 c_4, C_ant / v_*(theta_b)); the tube slack is "
        "(1-p)(4 c_F^2 c_6 + 2 c_a^2 c_2) + 8 pi^2 c_F^2 c_4 W (1 - p s) >= 0.",
        {"C1_TUBE_COEFFICIENT": C1_tube},
    )


@score_tail.check(HARDY, CITE + " R6 (M11-M15)")
def hardy_coefficients():
    C0, C1, E, gamma, b, e_g = sp.symbols("C0 C1 E gamma b e_g", positive=True)
    # M11: int K |f|^2 <= C1 b + (C0 + C1 e_g) ||f||^2 with e_g <= E.
    m11 = C1 * b + (C0 + C1 * E) * b / gamma  # ||f||^2 <= b / gamma (centered, gap)
    m12 = (C1 + (C0 + C1 * E) / gamma) * b
    m14 = C1 * b + (C0 + C1 * E) * 2 * b / gamma  # ||h||^2 <= 2 b / gamma (median half)
    m15 = (C1 + 2 * (C0 + C1 * E) / gamma) * b
    monotone = sp.simplify((C0 + C1 * E) - (C0 + C1 * e_g)).subs(e_g, E) == 0
    return sp.expand(m11 - m12) == 0 and sp.expand(m14 - m15) == 0 and monotone, (
        "Given M10 (C0, C1), e_g <= E and gap gamma: M12 coefficient C1 + (C0 + C1 E)/gamma, "
        "median Hardy constant C1 + 2 (C0 + C1 E)/gamma. Both remain conditional on M10."
    )


@score_tail.check(SOFT_MODE, CITE + " R7")
def soft_mode_divergence():
    delta, g = sp.symbols("delta g", positive=True)
    # A6 soft branch of the fixed-Q Hessian near the antipode.
    lam_soft = sp.sqrt(2) * delta - sp.sqrt(2) / 8 * delta**2
    # Gaussian weight exp(-lam eta^2 / g^2) has second moment g^2 / (2 lam).
    moment = g**2 / (2 * lam_soft)
    series = sp.series(moment, delta, 0, 1).removeO()
    leading = sp.simplify(series - (g**2 / (2 * sp.sqrt(2) * delta) + g**2 / (16 * sp.sqrt(2))))
    diverges = sp.limit(moment / g**2, delta, 0, "+") == sp.oo
    return leading == 0 and diverges, (
        "With lambda_soft = sqrt2 delta - (sqrt2/8) delta^2, E[eta_soft^2] = "
        "g^2/(2 sqrt2 delta) + g^2/(16 sqrt2) + O(delta): the H1 constant c_2 is not "
        "uniform up to the antipode, so H5 cannot come from a nine-dimensional Gaussian tube.",
        {"SOFT_MODE_MOMENT_LEADING": 1 / (2 * sp.sqrt(2) * delta)},
    )
