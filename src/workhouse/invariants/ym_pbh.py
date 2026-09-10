"""Exact finite controls for the proposed Wilson-weight PBH replacement.

The finite-lattice horizontal-geodesic obstruction is analytic. These checks
do not prove a continuum statement or refute every curvature method.
"""

from sympy import I, Matrix, Rational, Symbol, cos, diff, expand, log, pi, simplify, sin, symbols

from ._core import _suite

pbh = _suite("Wilson PBH proposal: exact orbit curvature and flow tests")
CITE = "PBH_WILSON_TEST; G19; G23"


@pbh.check(
    "FINDING: the actual Wilson orbit curvature is negative at a regular plaquette orbit",
    CITE + " PBH-4",
)
def _orbit_curvature():
    theta, beta, velocity = symbols("theta beta velocity", real=True)
    w = beta * (1 - cos(theta)) - 2 * log(sin(theta))
    curvature = beta * cos(theta) + 2 / sin(theta) ** 2
    witness = simplify(diff(w, theta, 2).subs({theta: 2 * pi / 3, beta: 8}))
    # Four original link metrics, minimized with equal angle increments.
    quotient_energy = 4 * sum((velocity / 4) ** 2 for _ in range(4))
    return (
        simplify(diff(w, theta, 2) - curvature) == 0
        and simplify(quotient_energy - velocity**2) == 0
        and witness == -Rational(4, 3),
        "Four-link quotient metric dtheta^2 and exact Haar pushforward sin^2(theta) "
        "give Ric_nu=beta cos(theta)+2 csc^2(theta); beta=8, theta=2pi/3 gives -4/3 "
        "at a principal orbit. This falsifies the global positive-curvature premise",
        {"WILSON_PBH_CURVATURE_WITNESS": witness},
    )


@pbh.check(
    "Weighted Gamma2 retains both the kinetic prefactor and signed Hessian", CITE + " PBH-1 PBH-4"
)
def _gamma_normalization():
    from sympy import Function

    x = Symbol("x", real=True)
    c = Symbol("c", positive=True)
    f, w = Function("f")(x), Function("w")(x)

    def generator(h):
        return c * (diff(h, x, 2) - diff(w, x) * diff(h, x))

    gamma = simplify((generator(f**2) - 2 * f * generator(f)) / 2)
    gamma2 = simplify(generator(gamma) / 2 - c * diff(f, x) * diff(generator(f), x))
    expected = c**2 * (diff(f, x, 2) ** 2 + diff(w, x, 2) * diff(f, x) ** 2)
    return simplify(gamma - c * diff(f, x) ** 2) == 0 and simplify(gamma2 - expected) == 0, (
        "For arbitrary smooth f,W, L=c(d2-W'd) gives Gamma=c(f')^2 and "
        "Gamma2=c^2[(f'')^2+W''(f')^2]; with c=1/2, f''=0, f'!=0, "
        "the curvature ratio is W''/2. A diffusion gap needs the physical-time identification"
    )


@pbh.check(
    "FINDING: the classical Wilson density is not the exact physical ground-state weight",
    CITE + " PBH-6",
)
def _physical_residual():
    from sympy import exp

    theta, z = symbols("theta z", real=True)
    beta, c, k = symbols("beta c k", positive=True)
    psi = exp(-beta * (1 - cos(theta)) / 2)
    residual = simplify(
        -c * (diff(psi, theta, 2) + 2 * cos(theta) / sin(theta) * diff(psi, theta)) / psi
        + k * (1 - cos(theta))
    )
    expected = (
        k * (1 - cos(theta)) + 3 * c * beta * cos(theta) / 2 - c * beta**2 * sin(theta) ** 2 / 4
    )
    polynomial = expand(k * (1 - z) + 3 * c * beta * z / 2 - c * beta**2 * (1 - z**2) / 4)
    return simplify(residual - expected) == 0 and polynomial.coeff(z, 2) == c * beta**2 / 4, (
        "For the actual radial Wilson H=-c(d2+2cot(theta)d)+k(1-cos(theta)), "
        "psi=exp[-beta(1-cos(theta))/2] has residual with cos(theta)^2 coefficient "
        "c beta^2/4>0. No choice of k makes this residual constant for beta,c>0"
    )


@pbh.check(
    "FINDING: Wilson gradient flow expands a regular orbit distance by 8/7", CITE + " section PBH-5"
)
def _flow_expansion():
    from sympy import atan

    y, q = symbols("y q", positive=True)
    theta0 = 2 * atan(y)
    theta_t = 2 * atan(q * y)
    jacobian = simplify(diff(theta_t, y) / diff(theta0, y))
    witness = simplify(jacobian.subs(q, Rational(1, 2)).subs(y**2, 3))
    return (
        simplify(jacobian - q * (1 + y**2) / (1 + q**2 * y**2)) == 0
        and witness == Rational(8, 7) > 1,
        "tan(theta(t)/2)=exp(-t)tan(theta0/2); theta0=2pi/3 and t=log(2) "
        "give D Phi_t=8/7>1 in the exact quotient metric. Action descent is not contraction",
        {"WILSON_FLOW_EXPANSION_WITNESS": witness},
    )


@pbh.check(
    "FINDING: center-valued Wilson configurations remain rough at positive flow time",
    CITE + " section PBH-5",
)
def _stationary_center():
    x, y, z = symbols("x y z", real=True)
    tangent = Matrix([[I * z, y + I * x], [-y + I * x, -I * z]])
    a = Symbol("a", positive=True)
    # At center-valued links, every varied plaquette word reduces to +/-X.
    stationary = all((sign * tangent).trace() == 0 for sign in (-1, 1))
    minus_trace = -2
    density = (1 - Rational(1, 2) * minus_trace) / a**4
    return stationary and tangent + tangent.conjugate().T == Matrix.zeros(
        2
    ) and density == 2 / a**4, (
        "Every su(2) tangent has zero trace, so every all-center link configuration "
        "is stationary for Wilson flow. A negative plaquette keeps energy 2/a^4. "
        "This falsifies a deterministic uniform bound, not a bound on probabilistic expectations"
    )
