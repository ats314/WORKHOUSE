"""Exact finite spectral models and localization algebra for the OS interface.

The analytic spectral-measure argument is in the companion derivation. These
checks certify the identities and counterexamples stated in their names; they
do not certify the continuum reconstruction theorem or its hypotheses.
"""

from sympy import Matrix, Rational, diag, diff, expand, simplify, symbols

from ._core import SUITES, Suite

reconstruction = Suite("Yang-Mills source extraction: reconstruction and localization")
SUITES.append(reconstruction)


@reconstruction.check(
    "two-atom reflection kernel is an exact Gram matrix with determinant w1*w2*(r1-r2)^2",
    "YM_RECONSTRUCTION section 2; OS_1975 p. 291 equations (5.2)-(5.3); G23",
)
def _():
    w1, w2, r1, r2 = symbols("w1 w2 r1 r2", positive=True)
    hankel = Matrix(4, 4, lambda i, j: w1 * r1 ** (i + j) + w2 * r2 ** (i + j))
    evaluation = Matrix([[r1**i, r2**i] for i in range(4)])
    gram = evaluation * diag(w1, w2) * evaluation.T
    determinant = expand(hankel[:2, :2].det())
    return hankel == gram and expand(determinant - w1 * w2 * (r1 - r2) ** 2) == 0, (
        "The 4x4 reflected kernel C(i+j) factors as V diag(w1,w2) V^T; its 2x2 "
        "minor is w1*w2*(r1-r2)^2. Positive weights give reflection positivity "
        "in this finite spectral model, independently of a continuum QFT construction."
    )


@reconstruction.check(
    "a complete observable frame detects both excited sectors with exact lower frame bound 2",
    "YM_RECONSTRUCTION section 3; OS_1975 p. 291 totality statement; G18 G23",
)
def _():
    x, y, r1, r2 = symbols("x y r1 r2", real=True)
    frame = Matrix([[1, 1], [1, -1], [0, 1]])
    v = Matrix([x, y])
    remainder = expand((frame * v).dot(frame * v) - 2 * v.dot(v))
    aggregate = (frame * diag(r1, r2) * frame.T).trace()
    incomplete = Matrix([[0, 1]])
    return (
        (
            frame.T * frame == diag(2, 3)
            and remainder == y**2
            and aggregate == 2 * r1 + 3 * r2
            and incomplete * Matrix([1, 0]) == Matrix([0])
        ),
        (
            "A^T A=diag(2,3), ||Av||^2-2||v||^2=y^2, and the summed correlator is "
            "2*r1+3*r2. The one-row subframe (0,1) has an invisible first sector. "
            "This checks a finite observable-completeness mechanism, not QFT density."
        ),
        {"YM_FINITE_FRAME_FLOOR": Rational(2)},
    )


@reconstruction.check(
    "a positive three-state transfer matrix realizes a hidden slow mode "
    "under an arbitrarily small plateau",
    "YM_RECONSTRUCTION sections 3-4; JW_2006 p. 6; G18 G23",
)
def _():
    # u is a free real amplitude: its square may be arbitrarily small.
    u = symbols("u", real=True)
    transfer = diag(1, Rational(15, 16), Rational(3, 4))
    vacuum, observable = Matrix([1, 0, 0]), Matrix([0, u, 1])
    checked = all(
        expand(
            (observable.T * transfer**n * observable)[0]
            - (u**2 * Rational(15, 16) ** n + Rational(3, 4) ** n)
        )
        == 0
        for n in range(9)
    )
    return checked and vacuum.dot(observable) == 0 and transfer * vacuum == vacuum, (
        "T=diag(1,15/16,3/4), F=(0,u,1) gives C_n=u^2*(15/16)^n+(3/4)^n "
        "(checked exactly n=0..8). Its spectral weights are nonnegative and the "
        "slow atom is u^2. For every n>=0 the second term u^2*(15/16)^n <= u^2, "
        "so any positive plateau admits a slow physical mode; u=0 hides it entirely."
    )


@reconstruction.check(
    "spectral leakage optimization has stationary x=A*(1-theta)/(epsilon*theta) "
    "with a positive derivative slope",
    "YM_RECONSTRUCTION section 4; G23 localization error refinement",
)
def _():
    A, epsilon, x = symbols("A epsilon x", positive=True)
    theta = symbols("theta", positive=True)
    bound = A * x ** (theta - 1) + epsilon * x**theta
    normalized_derivative = simplify(x ** (2 - theta) * diff(bound, x))
    affine = A * (theta - 1) + epsilon * theta * x
    critical = A * (1 - theta) / (epsilon * theta)
    return (
        simplify(normalized_derivative - affine) == 0
        and simplify(affine.subs(x, critical)) == 0
        and diff(affine, x) == epsilon * theta
    ), (
        "For 0<theta<1, the derivative of A*x^(theta-1)+epsilon*x^theta has the "
        "sign of A*(theta-1)+epsilon*theta*x, with positive slope. On x>=1 the "
        "minimum is at max(1,A*(1-theta)/(epsilon*theta)). Positivity of a "
        "nonzero optimized bound does not establish spectral exclusion."
    )


@reconstruction.check(
    "adaptive localization balances both exponents at delta=eta*beta/(alpha+beta)",
    "YM_RECONSTRUCTION section 5; G23 conditional localization repair",
)
def _():
    alpha = symbols("alpha", nonnegative=True)
    beta, eta, time = symbols("beta eta time", positive=True)
    radius = eta * time / (alpha + beta)
    delta = eta * beta / (alpha + beta)
    equalities = [
        simplify(-eta * time + alpha * radius + delta * time),
        simplify(-beta * radius + delta * time),
        simplify(eta - delta - eta * alpha / (alpha + beta)),
    ]
    return all(value == 0 for value in equalities) and delta.is_positive, (
        "R(t)=eta*t/(alpha+beta) converts both exponents -eta*t+alpha*R and "
        "-beta*R to -delta*t with delta=eta*beta/(alpha+beta)>0. This is the "
        "exact rate balance for a hypothesized two-parameter bound; no source "
        "or check here supplies that bound for the Yang-Mills measure."
    )
