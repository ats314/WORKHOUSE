"""Exact ground-state-transform algebra for the G20/G23 curvature route.

The source normalization is MMM 2019, II.2/II.9/II.16/II.23, with
c = hbar**2/(2*m).  Mondal 2023, 4.1/4.9/4.11, absorbs m into the metric.
These checks establish local differential and finite algebraic identities.
They do not construct an infinite-dimensional Yang--Mills measure/operator,
certify its curvature, or identify a sampling generator with physical time.
The conditional analytic bridge is derived in
docs/derivations/yangmills-weighted-curvature.md.
"""

from __future__ import annotations

from sympy import (
    Function,
    Matrix,
    Poly,
    Rational,
    diff,
    exp,
    expand,
    factor,
    simplify,
    symbols,
)

from ._core import _suite

ym_ground_state = _suite("Yang-Mills ground-state transform and residual certificates (G20, G23)")

CONJUGATION = "ground-state trial residual gives exact conjugation in two flat dimensions"
DIRICHLET = "weighted Dirichlet identity retains the trial residual"
BOCHNER = "flat weighted Bochner identity has Hessian coefficient 2/hbar"
MATRIX_RESIDUAL = "finite symmetric matrix ground-state residual identity"
OSCILLATOR = "anisotropic oscillator calibrates curvature gap to hbar omega_min"
RESIDUAL_BUDGET = "trial residual gap budget uses its mean above its floor"
QUARTIC = "pure quartic oscillator Gaussian residual certificate"
QUARTIC_OPTIMUM = (
    "quartic Gaussian certificate is optimized at frequency cubed 6 lambda hbar over mass squared"
)


@ym_ground_state.check(
    CONJUGATION, "YM_GROUND_STATE; G20; G23; MMM_2019_CURVATURE II.9; derivation GST-1"
)
def _conjugation():
    x, y = symbols("x y", real=True)
    hbar, mass = symbols("hbar mass", positive=True)
    coords = (x, y)
    action = Function("S")(*coords)
    potential = Function("V")(*coords)
    trial = exp(-action / hbar)
    test = Function("f")(*coords)
    c = hbar**2 / (2 * mass)

    def lap(expr):
        return sum(diff(expr, q, 2) for q in coords)

    def ham(expr):
        return -c * lap(expr) + potential * expr

    residual = potential + c * lap(action) / hbar
    residual -= c * sum(diff(action, q) ** 2 for q in coords) / hbar**2
    drift = lap(test) - 2 * sum(diff(action, q) * diff(test, q) for q in coords) / hbar
    defect = simplify(ham(trial * test) / trial - (-c * drift + residual * test))
    profile_defect = simplify(ham(trial) / trial - residual)
    return defect == profile_defect == 0, (
        f"conjugation defect={defect}; R=(H psi)/psi defect={profile_defect}; "
        "psi=exp(-S/hbar), U^-1 H U=-c L_S+R, c=hbar^2/(2m); "
        "arbitrary smooth S,V,f in flat dimension two, without an eigenstate assumption"
    )


@ym_ground_state.check(
    DIRICHLET,
    "YM_GROUND_STATE; G20; G23; MMM_2019_CURVATURE II.13; derivation GST-2",
    rests_on=(CONJUGATION,),
)
def _dirichlet():
    x, y = symbols("x y", real=True)
    hbar, c = symbols("hbar c", positive=True)
    coords = (x, y)
    action, test = Function("S")(*coords), Function("f")(*coords)
    rho = exp(-2 * action / hbar)
    drift = sum(diff(test, q, 2) - 2 * diff(action, q) * diff(test, q) / hbar for q in coords)
    energy = c * rho * sum(diff(test, q) ** 2 for q in coords)
    divergence = c * sum(diff(rho * test * diff(test, q), q) for q in coords)
    defect = simplify(rho * test * (-c * drift) - energy + divergence)
    return defect == 0, (
        f"pointwise weighted integration-by-parts defect={defect}; "
        "rho*f*(-c L_S f)=c*rho*|grad f|^2-c*div(rho*f*grad f). "
        "Add rho*R*f^2 to obtain the trial-state energy; integration needs boundary/core control"
    )


@ym_ground_state.check(
    BOCHNER, "YM_GROUND_STATE; G20; G23; MMM_2019_CURVATURE II.15-II.16; derivation GST-3"
)
def _bochner():
    x, y = symbols("x y", real=True)
    hbar = symbols("hbar", positive=True)
    coords = (x, y)
    action, test = Function("S")(*coords), Function("f")(*coords)

    def drift(expr):
        return sum(diff(expr, q, 2) - 2 * diff(action, q) * diff(expr, q) / hbar for q in coords)

    grad_sq = sum(diff(test, q) ** 2 for q in coords)
    lhs = drift(grad_sq) / 2 - sum(diff(test, q) * diff(drift(test), q) for q in coords)
    hess_sq = sum(diff(test, p, q) ** 2 for p in coords for q in coords)
    curvature = (
        2
        * sum(diff(action, p, q) * diff(test, p) * diff(test, q) for p in coords for q in coords)
        / hbar
    )
    defect = simplify(lhs - hess_sq - curvature)
    return defect == 0, (
        f"flat weighted Bochner defect={defect}; "
        "(L_S |grad f|^2)/2-<grad f,grad L_S f>=|Hess f|^2+(2/hbar)Hess S(grad f,grad f); "
        "the curved-manifold Ricci term and analytic domain extension are separate premises"
    )


@ym_ground_state.check(MATRIX_RESIDUAL, "YM_GROUND_STATE; G23; derivation GST-4")
def _matrix_residual():
    h00, h01, h02, h11, h12, h22 = symbols("h00 h01 h02 h11 h12 h22", real=True)
    ham = Matrix([[h00, h01, h02], [h01, h11, h12], [h02, h12, h22]])
    psi = Matrix(symbols("p0:3", positive=True))
    test = Matrix(symbols("f0:3", real=True))
    physical = Matrix([psi[i] * test[i] for i in range(3)])
    row = ham * psi
    residual = [row[i] / psi[i] for i in range(3)]
    qh = (physical.T * ham * physical)[0]
    qr = sum(residual[i] * psi[i] ** 2 * test[i] ** 2 for i in range(3))
    edges = -Rational(1, 2) * sum(
        ham[i, j] * psi[i] * psi[j] * (test[i] - test[j]) ** 2 for i in range(3) for j in range(3)
    )
    defect = expand(qh - qr - edges)
    return defect == 0, (
        f"generic symmetric 3x3 residual quadratic-form defect={defect}; "
        "R_i=(H psi)_i/psi_i. Off-diagonal H_ij<=0 makes edge energy nonnegative; "
        "an arbitrary Hamiltonian basis need not satisfy that sign hypothesis"
    )


@ym_ground_state.check(
    OSCILLATOR,
    "YM_GROUND_STATE; G20; G23; MMM_2019_CURVATURE II.24-II.27; derivation GST-5",
    rests_on=(CONJUGATION, BOCHNER),
)
def _oscillator():
    hbar, mass = symbols("hbar mass", positive=True)
    w0, dw1, dw2 = symbols("omega_min domega1 domega2", positive=True)
    coords = symbols("x0:3", real=True)
    omega = (w0, w0 + dw1, w0 + dw2)
    action = mass * sum(w * x**2 for w, x in zip(omega, coords, strict=True)) / 2
    potential = mass * sum(w**2 * x**2 for w, x in zip(omega, coords, strict=True)) / 2
    c = hbar**2 / (2 * mass)
    residual = potential + c * sum(diff(action, x, 2) for x in coords) / hbar
    residual -= c * sum(diff(action, x) ** 2 for x in coords) / hbar**2
    ground = hbar * sum(omega) / 2
    curvature = [2 * diff(action, x, 2) / hbar for x in coords]
    kappa = 2 * mass * w0 / hbar
    drift_x0 = -2 * diff(action, coords[0]) / hbar
    excitation_defect = simplify(-c * drift_x0 - hbar * w0 * coords[0])
    defects = [simplify(residual - ground), simplify(c * kappa - hbar * w0), excitation_defect]
    return (
        all(d == 0 for d in defects) and all(simplify(k - kappa).is_nonnegative for k in curvature),
        (
            f"defects={defects}; R=(hbar/2)*sum omega; "
            "Ric_weighted diagonal=2m*omega/hbar; c*kappa=hbar*omega_min, attained by f=x0. "
            "This tests both the factor of two and the physical-energy normalization"
        ),
        {"YM_GST_OSCILLATOR_GAP": hbar * w0},
    )


@ym_ground_state.check(RESIDUAL_BUDGET, "YM_GROUND_STATE; G23; derivation GST-6")
def _residual_budget():
    gamma, excess = symbols("gamma excess", positive=True)
    floor = symbols("r_min", real=True)
    lower_slack, upper_slack = symbols("lower_slack upper_slack", nonnegative=True)
    mean = floor + excess
    level1 = gamma + floor + lower_slack
    level0 = mean - upper_slack
    bound = gamma - (mean - floor)
    defect = simplify(level1 - level0 - bound - lower_slack - upper_slack)
    margin = symbols("margin", positive=True)
    positive_budget = simplify(bound.subs(gamma, excess + margin) - margin)
    return (
        defect == positive_budget == 0,
        (
            f"level comparison defect={defect}; positive-budget defect={positive_budget}; "
            "E1>=gamma+r_min and E0<=meanR imply E1-E0>=gamma-(meanR-r_min). "
            "This check proves the exact arithmetic implication; min-max, domain, and curvature "
            "hypotheses are stated in GST-6 and are not proved by symbolic reparameterization"
        ),
        {"YM_GST_RESIDUAL_GAP_BUDGET": gamma - excess},
    )


@ym_ground_state.check(
    QUARTIC,
    "YM_GROUND_STATE; G23; derivation GST-7",
    rests_on=(CONJUGATION, OSCILLATOR, RESIDUAL_BUDGET),
)
def _quartic():
    x = symbols("x", real=True)
    hbar, mass, omega = symbols("hbar mass omega", positive=True)
    # This exact substitution states omega^3=6*lambda*hbar/mass^2.
    lam = mass**2 * omega**3 / (6 * hbar)
    c = hbar**2 / (2 * mass)
    action = mass * omega * x**2 / 2
    residual = lam * x**4 + c * diff(action, x, 2) / hbar - c * diff(action, x) ** 2 / hbar**2
    floor = hbar * omega / 8
    square = lam * (x**2 - mass * omega**2 / (4 * lam)) ** 2
    square_defect = expand(residual - floor - square)
    # Derive Gaussian moments from the integration-by-parts recurrence
    # E[x^(n+2)] = (n+1)/(2a)*E[x^n], rho proportional to exp(-a*x^2).
    a = mass * omega / hbar
    moment2 = 1 / (2 * a)
    moment4 = 3 * moment2 / (2 * a)
    mean = hbar * omega / 2 - mass * omega**2 * moment2 / 2 + lam * moment4
    mean_defect = simplify(mean - 3 * hbar * omega / 8)
    gamma = hbar * omega
    bound = simplify(gamma + floor - mean)
    bound_defect = simplify(bound - 3 * hbar * omega / 4)
    # Check the recurrence's pointwise total-derivative integrands independently.
    rho = exp(-a * x**2)
    moment_defects = [
        simplify(diff(x ** (n + 1) * rho, x) - ((n + 1) * x**n - 2 * a * x ** (n + 2)) * rho)
        for n in (0, 2)
    ]
    defects = [square_defect, mean_defect, bound_defect, *moment_defects]
    return (
        all(d == 0 for d in defects),
        (
            f"defects={defects}; lambda=m^2*omega^3/(6*hbar); "
            "R-hbar*omega/8=lambda*(x^2-m*omega^2/(4*lambda))^2; "
            "meanR=3*hbar*omega/8 from exact Gaussian moments; "
            "conditional gap>=3*hbar*omega/4 for the pure quartic oscillator, "
            "with omega=(6*lambda*hbar/m^2)^(1/3). R is unbounded above "
            "but the certificate remains finite"
        ),
        {
            "YM_GST_QUARTIC_RESIDUAL_FLOOR": hbar * omega / 8,
            "YM_GST_QUARTIC_RESIDUAL_MEAN": 3 * hbar * omega / 8,
            "YM_GST_QUARTIC_GAP_CERTIFICATE": bound,
        },
    )


@ym_ground_state.check(
    QUARTIC_OPTIMUM,
    "YM_GROUND_STATE; G23; derivation GST-7",
    rests_on=(QUARTIC,),
)
def _quartic_optimum():
    q = symbols("frequency_ratio", positive=True)
    candidate = 5 * q / 4 - 1 / (8 * q**2) - 3 * q**4 / 8
    loss = Rational(3, 4) - candidate
    positive_poly = 3 * q**4 + 6 * q**3 + 9 * q**2 + 2 * q + 1
    certificate = (q - 1) ** 2 * positive_poly / (8 * q**2)
    defect = simplify(loss - certificate)
    return defect == 0 and positive_poly.is_positive and candidate.subs(q, 1) == Rational(3, 4), (
        f"optimization defect={defect}; loss={factor(loss)}; "
        "for every positive trial-frequency ratio q, the loss from omega_* is nonnegative, "
        "and zero only at q=1. This optimizes this Gaussian residual-floor bound, not the true gap"
    )


@ym_ground_state.check(
    "FINDING: omitting a nonconstant ground-state residual overstates a finite gap",
    "YM_GROUND_STATE; G23; derivation GST-8",
    rests_on=(MATRIX_RESIDUAL,),
)
def _residual_falsifier():
    psi = Matrix([1, 2])
    base = Matrix([[2, -1], [-1, Rational(1, 2)]])
    residual = Matrix.diag(-Rational(3, 4), Rational(3, 4))
    ham = base + residual
    base_eigenvalues = sorted(base.eigenvals())
    true_eigenvalues = sorted(ham.eigenvals())
    gamma = base_eigenvalues[1] - base_eigenvalues[0]
    actual = true_eigenvalues[1] - true_eigenvalues[0]
    mean = (psi.T * residual * psi)[0] / (psi.T * psi)[0]
    floor = -Rational(3, 4)
    bound = gamma + floor - mean
    ok = (
        base * psi == Matrix.zeros(2, 1)
        and gamma == Rational(5, 2)
        and actual == 2
        and mean == Rational(9, 20)
        and bound == Rational(13, 10)
        and bound <= actual < gamma
    )
    return ok, (
        f"positive trial psi=(1,2): conjugated diffusion gap={gamma}, "
        f"actual Hamiltonian gap={actual}; "
        f"R=(-3/4,3/4), meanR={mean}, certified lower bound={bound}. "
        "Treating this trial profile as an exact ground state would claim 5/2<=2, which is false"
    )


@ym_ground_state.check(
    "FINDING: quartic logarithmic trial state has an unbounded negative residual "
    "for a quartic potential",
    "YM_GROUND_STATE; G20; G23; derivation GST-8",
    rests_on=(CONJUGATION,),
)
def _tail_falsifier():
    x = symbols("x", real=True)
    alpha, beta, lam, hbar, mass = symbols("alpha beta lambda hbar mass", positive=True)
    action = alpha * x**2 / 2 + beta * x**4 / 4
    c = hbar**2 / (2 * mass)
    residual = lam * x**4 + c * diff(action, x, 2) / hbar - c * diff(action, x) ** 2 / hbar**2
    polynomial = Poly(expand(residual), x)
    leading = polynomial.LC()
    expected = -(beta**2) / (2 * mass)
    return polynomial.degree() == 6 and simplify(leading - expected) == 0 and leading.is_negative, (
        f"R degree={polynomial.degree()}, leading coefficient={leading}; "
        "S=alpha*x^2/2+beta*x^4/4 has globally positive Hessian but R tends to -infinity "
        "for V=lambda*x^4. The global residual-floor certificate fails for this trial tail; "
        "this does not refute a gap or other trial states (the Gaussian check succeeds)"
    )


@ym_ground_state.check(
    "FINDING: global residual budget loses the tensor product gap at four quartic copies",
    "YM_GROUND_STATE; G20; G23; derivation GST-9",
    rests_on=(QUARTIC,),
)
def _tensor_budget_falsifier():
    x, y = symbols("x y", real=True)
    hbar, mass, omega = symbols("hbar mass omega", positive=True)
    copies = symbols("copies", integer=True, positive=True)
    lam = mass**2 * omega**3 / (6 * hbar)
    c = hbar**2 / (2 * mass)
    action = mass * omega * (x**2 + y**2) / 2
    potential = lam * (x**4 + y**4)
    two_residual = potential + c * sum(diff(action, q, 2) for q in (x, y)) / hbar
    two_residual -= c * sum(diff(action, q) ** 2 for q in (x, y)) / hbar**2
    sum_of_residuals = sum(
        hbar * omega / 2 - mass * omega**2 * q**2 / 2 + lam * q**4 for q in (x, y)
    )
    additivity_defect = expand(two_residual - sum_of_residuals)
    floor = copies * hbar * omega / 8
    mean = copies * 3 * hbar * omega / 8
    gamma = hbar * omega  # Tensorized Gaussian gap is the minimum one-body gap.
    bound = simplify(gamma + floor - mean)
    expected = (1 - copies / 4) * hbar * omega
    one_body_certificate = 3 * hbar * omega / 4
    ok = (
        additivity_defect == 0
        and simplify(bound - expected) == 0
        and bound.subs(copies, 4) == 0
        and bound.subs(copies, 5).is_negative
        and one_body_certificate.is_positive
    )
    return (
        ok,
        (
            f"two-copy residual additivity defect={additivity_defect}; "
            f"n-copy global residual budget={bound}, zero at n=4 and negative at n=5. "
            "Tensorizing the one-body spectral certificates instead preserves gap>=3*hbar*omega/4 "
            "for every number of independent copies; the global mean-minus-floor comparison "
            "accumulates volume even when the physical tensor product gap does not"
        ),
        {"YM_GST_TENSOR_GLOBAL_RESIDUAL_BUDGET": bound},
    )
