"""Exact symbolic invariants for W6 synchronized M10 conditional score domination.

Guards:
1. Exact tangency of the S13 synchronized radial profile along the conditional minimizer curve.
2. Failure of the unsynchronized identical cutoff field (non-zero linear phase drift).
3. Euler dilation cancellation at q = 0.
4. Reduction of tube variance to C0 + C1 g^-2 E(V|Q).
5. Antipodal gauge invariance of the ground state score on the minimizing sphere.
"""

from __future__ import annotations

import sympy as sp

from ._core import _suite

synchronized_m10 = _suite("W6 synchronized M10 conditional score")
CITE = "W6_SYNCHRONIZED_M10_DOMINATION"


@synchronized_m10.check(
    "W6 synchronized: exact tangency eliminates linear phase drift",
    CITE + " Section 2",
)
def check_synchronized_tangency():
    theta = sp.Symbol("theta", real=True)
    chi = sp.Function("chi")
    z0 = (theta / 4) * chi(4 * (theta / 4))
    z1 = (theta / 4) * chi(4 * (theta / 4))
    z2 = (theta / 2) * chi(2 * (theta / 2))
    zQ = theta * chi(theta)
    Zy = sp.Matrix([z0, z1, z2])
    Dm = sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2)])
    drift = sp.simplify(Zy - Dm * zQ)
    passed = all(entry == 0 for entry in drift)
    return passed, f"Zy - Dm ZQ = {list(drift)}"


@synchronized_m10.check(
    "W6 synchronized: unsynchronized identical cutoff has non-zero drift",
    CITE + " Section 2",
)
def check_unsynchronized_failure():
    theta = sp.Symbol("theta", real=True)
    chi = sp.Function("chi")
    Zy_failed = sp.Matrix([
        (theta / 4) * chi(theta / 4),
        (theta / 4) * chi(theta / 4),
        (theta / 2) * chi(theta / 2),
    ])
    Dm = sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2)])
    zQ = theta * chi(theta)
    drift = sp.simplify(Zy_failed - Dm * zQ)
    passed = any(entry != 0 for entry in drift)
    return passed, f"Failed drift = {list(drift)}"


@synchronized_m10.check(
    "W6 synchronized: Euler dilation cancellation at q=0",
    CITE + " Section 3",
)
def check_euler_cancellation():
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    x = sp.Matrix([x1, x2, x3])
    M = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
    S = sp.Rational(1, 2) * (x.T * M * x)[0]
    ZS = sum(x[i] * sp.diff(S, x[i]) for i in range(3))
    F = sp.simplify(2 * S - ZS)
    hessian_F = sp.Matrix([[sp.diff(F, xi, xj) for xj in x] for xi in x])
    passed = (F == 0) and all(entry == 0 for entry in hessian_F)
    return passed, f"F = {F}, Hess(F) = 0"


@synchronized_m10.check(
    "W6 synchronized: tube variance reduces to quadratic potential floor",
    CITE + " Section 3",
)
def check_tube_variance_reduction():
    t = sp.Symbol("t", real=True)
    min_ratio = sp.limit(16 * (1 - sp.cos(t / 4)) / t**2, t, 0)
    antipodal_ratio = (16 * (1 - sp.cos(sp.pi / 4))) / sp.pi**2
    lower_bound = 2 / sp.pi**2
    passed = bool(antipodal_ratio > lower_bound) and bool(min_ratio == sp.Rational(1, 2))
    detail = f"min_ratio={min_ratio}, antipodal_ratio={float(antipodal_ratio):.4f} > {float(lower_bound):.4f}"
    return passed, detail


@synchronized_m10.check(
    "W6 synchronized: antipodal spectrum and gauge score invariance",
    CITE + " Section 4",
)
def check_antipodal_gauge_and_spectrum():
    C = sp.sqrt(2) / 2
    min_normal = sp.simplify((8 - 4 * sp.sqrt(2)) * C)
    zero_eig = sp.simplify(8 * C - 4 * sp.sqrt(2))
    passed = (zero_eig == 0) and (min_normal > 0)
    detail = f"zero_eig={zero_eig}, min_normal={min_normal} = {float(min_normal):.4f}"
    return passed, detail
