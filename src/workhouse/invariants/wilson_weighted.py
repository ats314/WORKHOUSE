"""Exact controls for the positive Wilson weighted-gradient and rotor repair.

The analytic eigenfunction, domain, min-max and tensorization arguments live
in the cited derivation. These checks do not formalize a continuum theorem.
"""

from sympy import (
    Function,
    Matrix,
    Rational,
    cos,
    coth,
    diff,
    exp,
    expand,
    log,
    simplify,
    sin,
    sinh,
    sqrt,
    summation,
    symbols,
    trigsimp,
)

from ._core import _suite

weighted = _suite("Wilson positive repair: weighted gradient, full rotor and shared-link residual")
CITE = "WILSON_WEIGHTED_REPAIR; G19; G23"


@weighted.check(
    "Wilson negative curvature cancels in a positive derivative supersolution", CITE + " WR1"
)
def _derivative_supersolution():
    theta, beta = symbols("theta beta", positive=True)
    w = beta * (1 - cos(theta)) - 2 * log(sin(theta))
    h = 1 / sin(theta)
    bh = -diff(h, theta, 2) + diff(w, theta) * diff(h, theta) + diff(w, theta, 2) * h
    v = diff(w, theta) ** 2 / 4 + diff(w, theta, 2) / 2
    expected_v = beta**2 * sin(theta) ** 2 / 4 - beta * cos(theta) / 2 + 2 / sin(theta) ** 2 - 1
    return (
        trigsimp(bh / h - (2 / sin(theta) ** 2 - 1)) == 0 and trigsimp(v - expected_v) == 0,
        "Exact Bh/h=2 csc^2(theta)-1 and conjugated one-form potential. The beta "
        "terms cancel in Bh/h; endpoint closure and the spectral argument are analytic",
    )


@weighted.check(
    "Weighted derivative energy differs from its positive form by an exact divergence",
    CITE + " WR2",
)
def _positive_form():
    x = symbols("x", real=True)
    u, h, w = (Function(name)(x) for name in ("u", "h", "w"))
    rho = exp(-w)
    bh = -diff(h, x, 2) + diff(w, x) * diff(h, x) + diff(w, x, 2) * h
    defect = rho * (
        diff(u, x) ** 2 + diff(w, x, 2) * u**2 - h**2 * diff(u / h, x) ** 2 - bh / h * u**2
    )
    boundary = diff(rho * diff(h, x) / h * u**2, x)
    return simplify(defect - boundary) == 0, (
        "For arbitrary differentiable u,h,W the positive-function factorization "
        "has exactly boundary derivative (exp(-W) h'/h u^2)'; no boundary term is omitted"
    )


@weighted.check(
    "The smooth sinh Wilson trial has the exact nonnegative physical residual", CITE + " WR4 WR5"
)
def _physical_trial():
    x, a, c = symbols("x a c", positive=True)
    f = sinh(a * x) / (a * x)
    d = ((1 - x**2) * diff(f, x, 2) + (2 / x - 5 * x) * diff(f, x)) / 4
    ode = simplify(diff(f, x, 2) + 2 * diff(f, x) / x - a**2 * f)
    residual = -c * d / f + c * a**2 * (1 - x**2) / 4
    expected = 3 * c * (a * x * coth(a * x) - 1) / 4
    return ode == 0 and simplify(residual - expected) == 0, (
        "Differentiation of sinh(a x)/(a x), with k=c a^2/8 and x=cos(theta/2), "
        "gives (H psi)/psi=3c[a x coth(a x)-1]/4. Its even series supplies smooth poles"
    )


@weighted.check(
    "The complete SU2 rotor separates into the Dirichlet radial and angular operators",
    CITE + " WR7",
)
def _radial_conjugation():
    theta, c, k, ell = symbols("theta c k ell", positive=True)
    u = Function("u")(theta)
    f = u / sin(theta)
    transformed = sin(theta) * (
        -c * (diff(f, theta, 2) + 2 * cos(theta) / sin(theta) * diff(f, theta))
        + (k * (1 - cos(theta)) + c * ell * (ell + 1) / sin(theta) ** 2) * f
    )
    expected = (
        -c * diff(u, theta, 2)
        + (-c + k * (1 - cos(theta)) + c * ell * (ell + 1) / sin(theta) ** 2) * u
    )
    return trigsimp(transformed - expected) == 0, (
        "Multiplication by sin(theta) gives -c d2-c+k(1-cos(theta)) "
        "+c ell(ell+1)csc^2(theta) for every angular sector; endpoint domains are stated in WR3"
    )


@weighted.check(
    "Exact scalar budgets certify the conservative complete-rotor gap constants", CITE + " WR8 WR11"
)
def _gap_budgets():
    # The analytic potential comparisons and oscillator min-max precede these
    # scalar checks. pi<22/7 and pi^2<10 are the explicit analytic inputs.
    radial_d_lower = sqrt(2) * (7 / Rational(22, 7) - Rational(3, 2))
    angular_upper_square = Rational(73, 16) + Rational(3, 4) * Rational(3, 2)
    radial_small = 3 - Rational(5, 2)
    radial_large_squared_margin = Rational(5, 2) - Rational(3, 2) ** 2
    return (
        simplify(radial_d_lower**2 - 1) == Rational(7, 121) > 0
        and angular_upper_square == Rational(91, 16) < Rational(29, 5)
        and radial_small == Rational(1, 2)
        and radial_large_squared_margin > 0
        and sqrt(64) / 16 == Rational(1, 2)
        and (Rational(1, 4) - Rational(1, 16)) * sqrt(64) - 1 > 0,
        "Exact margins for D0>1, delta>1/4, the k/c=5/2 radial split and k/c=64 "
        "complete-spectrum split. Together with WR8-WR10 these give max{c/2,sqrt(ck)/16}",
        {"WILSON_ROTOR_GAP_COEFFICIENT": Rational(1, 16)},
    )


@weighted.check(
    "The rotor gap scale restores the stated four-link Wilson kinetic normalization", CITE + " WR12"
)
def _physical_clock():
    g = symbols("g", positive=True)
    c, k = g**2 / 2, 4 / g**2
    return simplify(c * k) == 2 and simplify(c / 2 - g**2 / 4) == 0, (
        "For H_g=-2g^2 Delta_radius2+2g^-2(2-Tr U), Delta_radius2=Delta_unit/4, "
        "c=g^2/2, k=4/g^2, and sqrt(ck)/16=sqrt(2)/16. This clock is fixed-cell scaled"
    )


@weighted.check(
    "Shared-link incidence loss is an exact sum of nonnegative pair differences",
    CITE + " WR13 WR16",
)
def _incidence_defect():
    # An arbitrary coordinate of q=4 incident gradients in three spatial
    # dimensions. Sum this identity over the three Lie-algebra coordinates.
    entries = symbols("v0:4", real=True)
    v = Matrix(entries)
    total = sum(entries)
    defect = 4 * (v.dot(v)) - total**2
    pairs = sum((entries[i] - entries[j]) ** 2 for i in range(4) for j in range(i))
    return expand(defect - pairs) == 0, (
        "For four arbitrary incident gradient coordinates, 4 sum v_i^2-(sum v_i)^2 "
        "equals sum_(i<j)(v_i-v_j)^2. Zero padding handles boundary edges; the proof "
        "for general q is the same exact expansion, without a volume factor"
    )


@weighted.check(
    "Damping the compact trial absorbs the complete shared-link residual algebra",
    CITE + " WR14 WR16",
)
def _interacting_residual():
    a, c, q, s, r, grad2, total2 = symbols("a c q s r grad2 total2", real=True)
    k = q * c * a**2 / 8
    # s,r,grad2 are sums over plaquettes; total2 is sum_e |sum_p grad_e phi_p|^2.
    # Four edges per plaquette give sum_e sum_p |grad_e phi_p|^2=4 grad2.
    dlog = a**2 * s / 8 - 3 * r / 4 - grad2
    residual = k * s - c * dlog - c * total2 / 4
    floor = 3 * c * r / 4
    remainder = (q - 1) * c * (a**2 * s / 8 - grad2) + c * (4 * q * grad2 - total2) / 4
    theta = symbols("theta", real=True)
    phi = log(sinh(a * cos(theta / 2)) / (a * cos(theta / 2)))
    expected_derivative = (
        -a * sin(theta / 2) * (coth(a * cos(theta / 2)) - 1 / (a * cos(theta / 2))) / 2
    )
    return (
        expand(residual - floor - remainder) == 0
        and simplify(diff(phi, theta) - expected_derivative) == 0,
        "For k=q c a^2/8 the exact interacting residual minus 3c sum(z coth z-1)/4 "
        "is (q-1)c sum[a^2 s/8-|phi'|^2] plus the incidence defect. Positivity uses "
        "0<=coth(z)-1/z<=1. This is a residual-floor result, not a many-body gap",
    )


@weighted.check(
    "A complete boundary link carries the exact Haar Casimir and growing rank budget",
    CITE + " WR20 WR21",
)
def _boundary_rank():
    n, cutoff = symbols("n cutoff", integer=True, nonnegative=True)
    rank = summation((n + 1) ** 2, (n, 0, cutoff))
    expected = (cutoff + 1) * (cutoff + 2) * (2 * cutoff + 3) / 6
    # For a real unit-S3 coordinate x, Haar symmetry gives E[x^2]=1/4
    # and the intrinsic identity |grad x|^2=1-x^2 gives its exact quotient.
    variance = Rational(1, 4)
    return simplify(rank - expected) == 0 and (1 - variance) / variance == 3, (
        "The fundamental Haar coordinate has Rayleigh quotient 3, and SU2 degrees "
        "0 through N have dimension (N+1)(N+2)(2N+3)/6. WR20 analytically embeds "
        "this entire form in the true-ground four-link patch at every k; the "
        "resulting low boundary modes do not themselves satisfy the global Gauss law"
    )
