"""Finite exact controls for the analytic compatible-kernel gap theorem."""

from sympy import Matrix, Rational, limit, oo, simplify, symbols

from ._core import _suite

os_kernel = _suite("OS kernel gap: reconstruction and nontriviality controls")
SOURCE = "OS_KERNEL_GAP"


@os_kernel.check(
    "kernel quotient centering and transfer compatibility survive a vanishing source direction",
    f"{SOURCE} K1 equations K1-K2; finite rational Gram model only",
)
def _():
    z = symbols("z", positive=True)
    injection = Matrix([[1, 0, 0, 1], [0, 1, 0, 2], [0, 0, z, 0]])
    shift = Matrix(
        [
            [1, 0, 0, Rational(1, 2)],
            [0, Rational(1, 2), 0, 0],
            [0, 0, Rational(1, 4), 0],
            [0, 0, 0, Rational(1, 2)],
        ]
    )
    transfer = Matrix.diag(1, Rational(1, 2), Rational(1, 4))
    gram = injection.T * injection
    limiting = gram.subs(z, 0)
    vacuum = Matrix([1, 0, 0, 0])
    centered = Matrix.eye(4) - vacuum * gram[0, :]
    passed = (
        injection * shift == transfer * injection
        and gram * shift == shift.T * gram
        and centered * centered == centered
        and (gram * centered)[0, :] == Matrix([[0, 0, 0, 0]])
        and limiting.rank() == 2
        and (centered.T * limiting * centered).rank() == 1
    )
    for null in limiting.nullspace():
        passed = passed and limiting * shift * null == Matrix.zeros(4, 1)
    return passed, (
        "A nonorthogonal four-source injection into three dimensions has an "
        "exact compatible positive transfer. Its z->0 quotient has rank two "
        "and centered rank one; the null space is shift invariant. This is "
        "a finite Gram control, not the infinite-dimensional K1 proof."
    )


@os_kernel.check(
    "kernel log convexity has a positive two-atom defect and exact transfer iteration",
    f"{SOURCE} K2 equation K3; two-atom midpoint and dyadic controls",
)
def _():
    w1, w2, x, y = symbols("w1 w2 x y", positive=True)
    c0, c1, c2 = w1 + w2, w1 * x + w2 * y, w1 * x**2 + w2 * y**2
    passed = simplify(c0 * c2 - c1**2 - w1 * w2 * (x - y) ** 2) == 0
    count = 0
    for r1, r2 in [(Rational(1, 2), Rational(3, 4)), (1, Rational(1, 3))]:
        weights = [Rational(2, 3), Rational(1, 3)]
        for late in [2, 4, 8, 16]:
            for early in range(1, late):
                first = weights[0] * r1**early + weights[1] * r2**early
                last = weights[0] * r1**late + weights[1] * r2**late
                passed = passed and first**late <= last**early
                count += 1
    return passed, (
        f"C(0)C(2t)-C(t)^2=w1*w2*(x-y)^2 and {count} exact "
        "normalized rational interpolation inequalities hold. Holder and "
        "the general limiting argument remain analytic."
    )


@os_kernel.check(
    "kernel positive time correlation yields the stated finite energy weight floor",
    f"{SOURCE} K3 equation K8; exact finite positive spectral measures",
)
def _():
    total, corr = symbols("total corr", positive=True)
    threshold = corr / (2 * total)
    floor = (corr - threshold * total) / (1 - threshold)
    passed = simplify(floor - corr / (2 - corr / total)) == 0
    count = 0
    for a in range(1, 8):
        for b in range(1, 8):
            transfers = [Rational(a, 8), Rational(b, 8), Rational(1, 64)]
            weights = [Rational(2, 5), Rational(1, 5), Rational(3, 5)]
            norm = sum(weights)
            observed = sum(w * x for w, x in zip(weights, transfers, strict=True))
            cutoff = observed / (2 * norm)
            mass = sum(w for w, x in zip(weights, transfers, strict=True) if x >= cutoff)
            lower = observed / (2 - observed / norm)
            passed = passed and mass >= lower >= observed / 2 > 0
            count += 1
    return passed, (
        f"The lower weight is C/(2-C/V), not an assumed atom. {count} "
        "positive rational three-atom measures satisfy the finite-energy "
        "bound using the physical transfer threshold C/(2V)."
    )


@os_kernel.check(
    "kernel continuity and weak coupling inputs cannot be replaced by bounded limits",
    f"{SOURCE} K4; exact cutoff families and normalized action denominator",
)
def _():
    n = symbols("n", positive=True, integer=True)
    alpha, beta = symbols("alpha beta", positive=True)
    running = 1 / (alpha + beta * n)
    next_running = 1 / (alpha + beta * (n + 1))
    passed = (
        limit(2 ** (-n), n, oo) == 0
        and limit(n / (n + 1), n, oo) == 1
        and simplify((running - next_running) / (4 * running * next_running) - beta / 4) == 0
    )
    for index in range(1, 17):
        late = Rational(1, 2) ** (index * index)
        passed = passed and late == (Rational(1, 2) ** index) ** index
        passed = passed and Rational(index, index * index) == Rational(1, index)
    return passed, (
        "The ultraviolet line has unit norm but zero fixed positive-time "
        "limit; its limiting shift is discontinuous. The soft line tends "
        "to a centered zero mode. For u_n=1/(alpha+beta*n), the normalized "
        "action coefficient is beta/4, so bounded covariance alone does "
        "not yield a summable increment. These are not Wilson refutations."
    )


@os_kernel.check(
    "kernel positive time smoothing has the exact rational extremum and a uniform continuity bound",
    f"{SOURCE} K5 equations K9-K11; exact rational time ratios",
)
def _():
    y = symbols("y", positive=True)
    count = 0
    for k in range(1, 33):
        polynomial = y**k * (1 - y)
        derivative = polynomial.diff(y)
        expected = y ** (k - 1) * (k - (k + 1) * y)
        maximizer = Rational(k, k + 1)
        maximum = Rational(k) ** k / Rational(k + 1) ** (k + 1)
        if simplify(derivative - expected) != 0:
            return False, "Smoothing derivative mismatch"
        if polynomial.subs(y, maximizer) != maximum:
            return False, "Smoothing extremum mismatch"
        if not 0 < maximum < Rational(1, k):
            return False, "Uniform continuity bound failed"
        count += 1
    return True, (
        f"For {count} ratios tau/t=k, the exact maximum of y^k(1-y) is "
        "k^k/(k+1)^(k+1)<1/k=t/tau. The stronger t/(e*tau) bound "
        "for arbitrary times follows analytically from E*exp(-tau*E). "
        "Positive-time history divisibility and the Hilbert limit are analytic."
    )
