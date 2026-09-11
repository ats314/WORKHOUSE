"""Exact ingredients and obstruction witnesses for the conditional M10 route.

No check here certifies the actual quantum all-fiber estimate. Analytic
implications and outstanding model identifications are stated in the source.
"""

from __future__ import annotations

import sympy as sp

from ._core import _suite

synchronized_m10 = _suite("W6 synchronized M10 conditional score")
CITE = "W6_SYNCHRONIZED_M10_DOMINATION"


@synchronized_m10.check("W6 synchronized: exact center tangency identity", CITE + " Section 2")
def check_synchronized_tangency():
    theta = sp.Symbol("theta", real=True)
    chi = sp.Function("chi")
    scales = (sp.Integer(4), sp.Integer(4), sp.Integer(2))
    drift = [sp.simplify(theta / k * chi(k * theta / k) - theta * chi(theta) / k) for k in scales]
    return all(v == 0 for v in drift), f"Zy-Dm ZQ={drift}; phase implication needs a smooth phase."


@synchronized_m10.check(
    "W6 synchronized: identical cutoffs need not be tangent", CITE + " Section 2"
)
def check_unsynchronized_failure():
    # One explicit profile value witness; no assertion that every cutoff fails.
    theta = sp.Integer(1)

    def chi(t):
        return 1 - t**2

    drift = [sp.simplify(theta * (chi(theta / k) - chi(theta)) / k) for k in (4, 4, 2)]
    return any(v != 0 for v in drift), f"Polynomial profile witness: {drift}."


@synchronized_m10.check(
    "W6 synchronized: Euler cancellation of any quadratic jet", CITE + " Section 3"
)
def check_euler_cancellation():
    x = sp.Matrix(sp.symbols("x0:3"))
    a, b, c, d, e, f = sp.symbols("a b c d e f")
    matrix = sp.Matrix([[a, b, c], [b, d, e], [c, e, f]])
    phase_jet = (x.T * matrix * x)[0] / 2
    defect = sp.expand(2 * phase_jet - sum(xi * sp.diff(phase_jet, xi) for xi in x))
    return (
        defect == 0,
        "Euler identity for a general quadratic jet; higher phase terms are retained.",
    )


@synchronized_m10.check(
    "W6 synchronized: sine-square potential-floor identity", CITE + " Section 3"
)
def check_potential_floor_identity():
    t = sp.Symbol("theta", real=True)
    potential = 16 * (1 - sp.cos(t / 4))
    defect = sp.trigsimp(potential - 32 * sp.sin(t / 8) ** 2)
    coefficient = sp.simplify(32 * (2 / (8 * sp.pi)) ** 2)
    return defect == 0 and coefficient == 2 / sp.pi**2, (
        "v=32 sin^2(theta/8); concavity sin(x)>=2x/pi supplies the analytic interval bound."
    )


@synchronized_m10.check(
    "W6 synchronized: logarithmic-parameter amplitude identity", CITE + " Section 5"
)
def check_log_parameter_amplitude():
    g, h, eta = sp.symbols("g h eta", positive=True)
    ell = sp.Function("ell")(eta, h)
    z, div = sp.Function("z")(eta), sp.Function("div")(eta)
    amplitude_score = 2 * g * sp.diff(ell, h) + (z * sp.diff(ell, eta) + div / 2 - 6) / g
    lhs = (g * sp.diff(amplitude_score, eta)).subs(g**2, h)
    rhs = 2 * h * sp.diff(ell, eta, h) + sp.diff(z * sp.diff(ell, eta) + div / 2, eta)
    return sp.simplify(lhs - rhs) == 0, (
        "g grad(a_g)=2 grad(h partial_h log A)+grad(Z log A+div Z/2). "
        "Uniform bounds for the actual amplitude remain hypotheses."
    )


def remainder_witness():
    g, eta = sp.symbols("g eta", positive=True)
    amplitude = 1 + eta * g**4 * sp.sin(g**-6)
    score = sp.diff(sp.log(amplitude), g) + eta * sp.diff(sp.log(amplitude), eta) / g
    return g, sp.simplify(sp.diff(score, eta).subs(eta, 0))


@synchronized_m10.check(
    "W6 synchronized: spatial remainder does not control parameter derivative", CITE + " Section 5"
)
def check_remainder_obstruction():
    g, actual = remainder_witness()
    expected = 5 * g**3 * sp.sin(g**-6) - 6 * g**-3 * sp.cos(g**-6)
    return sp.simplify(actual - expected) == 0, (
        "For A=1+eta*g^4*sin(g^-6), gradient=5g^3 sin(g^-6)-6g^-3 cos(g^-6). "
        "At g=(2pi n)^(-1/6), g*gradient=-6/g^2: no O(1/g) bound. "
        "Counterexample to a remainder inference, not to the Wilson ground."
    )


@synchronized_m10.check(
    "W6 synchronized: centered numerator retains fiber normalization", CITE + " Section 6"
)
def check_score_variance_denominator():
    psi, hq = sp.symbols("psi h_Q", positive=True)
    numerator, beta = sp.symbols("N beta", real=True)
    actual = (numerator / psi - beta) ** 2 * psi**2 / hq
    expected = (numerator - beta * psi) ** 2 / hq
    return sp.simplify(
        actual - expected
    ) == 0, "Centered integrand=(N-beta*Psi)^2/h_Q; h_Q remains."


@synchronized_m10.check(
    "W6 synchronized: positive potential Hessian is not an action Hessian", CITE + " Section 6"
)
def check_hessian_distinction():
    x = sp.Symbol("x", real=True)
    potential, action = 2 * x**2, x**2
    eikonal = sp.diff(action, x) ** 2 / 2 - potential
    claimed_gap_defect = action - sp.diff(potential, x, 2) * x**2 / 2
    return sp.expand(eikonal) == 0 and sp.expand(claimed_gap_defect) == -(x**2), (
        "V=2x^2, S=x^2 solve |S'|^2/2=V; Hess V=4, Hess S=2. "
        "The asserted magnetic-Hessian action-gap constant fails even here."
    )


def angular_moments():
    """Exact moments of x=lambda*(1-t); density proportional to exp(-x)."""
    x, length = sp.symbols("x L", positive=True)
    integrals = [sp.integrate(x**j * sp.exp(-x), (x, 0, length)) for j in range(3)]
    return length, [sp.simplify(v / integrals[0]) for v in integrals]


@synchronized_m10.check("W6 synchronized: exact angular crossover moments", CITE + " Section 4")
def check_angular_moments():
    length, moments = angular_moments()
    expected = [
        1,
        1 - length / (sp.exp(length) - 1),
        2 - (length**2 + 2 * length) / (sp.exp(length) - 1),
    ]
    return all(sp.simplify(a - b) == 0 for a, b in zip(moments, expected, strict=True)), (
        "For L=2lambda>0: E[x]=1-L/(exp(L)-1)<=1; "
        "E[x^2]=2-(L^2+2L)/(exp(L)-1)<=2. Reference angular law only."
    )


@synchronized_m10.check("W6 synchronized: angular crossover endpoint limits", CITE + " Section 4")
def check_angular_limits():
    length, moments = angular_moments()
    zero = [sp.limit(v, length, 0, dir="+") for v in moments[1:]]
    large = [sp.limit(v, length, sp.oo) for v in moments[1:]]
    return zero == [0, 0] and large == [1, 2], f"Moment limits: L->0 {zero}; L->infinity {large}."


@synchronized_m10.check("W6 synchronized: seven-normal reference score budget", CITE + " Section 4")
def check_normal_angular_budget():
    x = sp.Symbol("x", real=True)
    mass = sp.integrate(sp.exp(-(x**2)), (x, -sp.oo, sp.oo))
    second = sp.integrate(x**2 * sp.exp(-(x**2)), (x, -sp.oo, sp.oo)) / mass
    fourth = sp.integrate(x**4 * sp.exp(-(x**2)), (x, -sp.oo, sp.oo)) / mass
    k = 7
    radial_second = k * fourth + k * (k - 1) * second**2
    budget = radial_second + 2 * (k * second) * 1 + 2
    return budget == sp.Rational(99, 4), (
        "Independent seven-normal Gaussian plus truncated-exponential angle: "
        "E[(|z|^2/g^2+lambda(1-t))^2]<=99/4 for every lambda>=0. "
        "Actual-law comparison and score error must still be supplied."
    )
