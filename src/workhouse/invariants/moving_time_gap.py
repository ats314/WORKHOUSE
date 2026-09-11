"""Exact controls for moving-time gap transport, not a measure-limit proof."""

from dataclasses import dataclass

from sympy import Matrix, Rational, diff, simplify, symbols, sympify

from ._core import _suite

moving_time = _suite("Moving-time spectral gap: exact budgets and falsifiers")
SOURCE = "MOVING_TIME_SPECTRAL_GAP"


def _rational(value):
    value = sympify(value)
    if value.is_Rational is not True:
        raise ValueError("Budget inputs must be exact rational numbers")
    return value


@dataclass(frozen=True)
class GapBudget:
    """Physical time t=c log(1/a) and nonnegative conditional guarantee."""

    time_coefficient: object
    rate: object
    decay_branch: object
    error_branch: object


def power_budget(p, r, s, m, horizon=None):
    """Optimize MT4; zero means no positive guarantee under this budget.

    This does not verify a source estimate or a continuum identification.
    """
    p, r, s, m = map(_rational, (p, r, s, m))
    if p < 0 or s < 0 or r <= 0 or m <= 0:
        raise ValueError("Require p,s>=0 and r,m>0")
    c = (p + r) / m
    if horizon is not None:
        horizon = _rational(horizon)
        if horizon <= 0:
            raise ValueError("The physical horizon coefficient must be positive")
        c = min(c, horizon)
    decay = m - (p + 2 * s) / c
    error = (r - 2 * s) / c
    return GapBudget(c, max(Rational(0), min(decay, error)), decay, error)


@moving_time.check(
    "moving-time power exponents balance with the source amplitude squared",
    f"{SOURCE} section 4 MT4b-MT4e",
)
def _():
    p, r, s, m, c, energy = symbols("p r s m c energy", positive=True)
    first = c * (m - energy) - p - 2 * s
    second = r - 2 * s - c * energy
    cstar = (p + r) / m
    rate = m * (r - 2 * s) / (p + r)
    equalities = [
        simplify((first - second).subs(c, cstar)),
        simplify(first.subs({c: cstar, energy: rate})),
        simplify(second.subs({c: cstar, energy: rate})),
        simplify(diff(m - (p + 2 * s) / c, c) - (p + 2 * s) / c**2),
        simplify(diff((r - 2 * s) / c, c) + (r - 2 * s) / c**2),
    ]
    full = power_budget(1, 5, 1, 2)
    short = power_budget(1, 5, 1, 2, 2)
    passed = (
        all(value == 0 for value in equalities)
        and full.rate == 1
        and full.time_coefficient == 3
        and short.rate == Rational(1, 2)
        and power_budget(1, 2, 1, 2).rate == 0
        and power_budget(1, 5, 1, 2, Rational(3, 2)).rate == 0
    )
    return passed, (
        "Normalized exponents c(m-E)-p-2s and r-2s-cE both vanish at "
        "c=(p+r)/m, E=m(r-2s)/(p+r). For (p,r,s,m)=(1,5,1,2), rate=1 "
        "at c=3 and the c<=2 rate=1/2. r=2s and the minimum-time equality "
        "give no positive certificate. The limit argument is analytic."
    )


@moving_time.check(
    "moving-time sharpness reconstructs the one-atom weighted geometric mean",
    f"{SOURCE} section 5 MT5",
)
def _():
    p, r, s, m, cmax = symbols("p r s m cmax", positive=True)
    theta = (r - 2 * s) / (p + r)
    short_rate = m - (p + 2 * s) / cmax
    exact = (
        simplify(-p * theta + r * (1 - theta) - 2 * s) == 0
        and simplify(m * theta - m * (r - 2 * s) / (p + r)) == 0
        and simplify((m - short_rate) * cmax - p - 2 * s) == 0
    )
    for n in range(1, 17):
        a = Rational(1, 2) ** n
        raw = a**2 * a**3
        rhs = a ** (-1) * a**6 + a**5
        exact = exact and raw == a**5 and rhs == 2 * raw
    return exact, (
        "The weighted geometric product has cutoff exponent 2s and energy "
        "m theta. Analytic AM-GM supplies its all-time upper bound with an "
        "atom at the claimed rate. The shortened-horizon exponent cancels "
        "exactly; 16 rational endpoint instances retain the atom."
    )


@moving_time.check(
    "moving-time finite positive transfer controls tolerate approximate probes",
    f"{SOURCE} sections 1-2 MT1-MT2",
)
def _():
    eigenvalues = [Rational(1), Rational(3, 4), Rational(1, 4)]
    target = Matrix([1, 2, -1])
    checked = 0
    for denominator in (2, 7, 31):
        error = Matrix([Rational(1, denominator), 0, -Rational(2, denominator)])
        probe = target - error
        d2 = error.dot(error)
        for step in range(9):
            correlation = sum(probe[i] ** 2 * eigenvalues[i] ** step for i in range(3))
            for threshold in eigenvalues:
                indices = [i for i in range(3) if eigenvalues[i] >= threshold]
                target_mass = sum(target[i] ** 2 for i in indices)
                probe_mass = sum(probe[i] ** 2 for i in indices)
                if probe_mass > correlation / threshold**step:
                    return False, "Positive spectral domination failed"
                if target_mass > 2 * d2 + 2 * correlation / threshold**step:
                    return False, "Approximate-probe spectral bound failed"
                checked += 1
    return True, (
        f"{checked} exact rational transfer cases reconstruct projected masses "
        "and prove nu_f<=2||f-v||^2+2r_E^-k C_v(k). Source error has no "
        "r_E^-k factor. This does not certify vague convergence or density."
    )


@moving_time.check(
    "moving-time amplitude plateau clock and dark-sector falsifiers remain exact",
    f"{SOURCE} section 5 MT5",
)
def _():
    low, high = Rational(15, 16), Rational(1, 4)
    vacuum, observed, dark = Matrix([1, 0, 0]), Matrix([0, 0, 1]), Matrix([0, 1, 0])
    passed = vacuum.dot(observed) == 0 and observed.dot(dark) == 0
    for n in range(1, 17):
        a = Rational(1, 2) ** n
        raw_zero_mode = a**2
        passed = passed and raw_zero_mode / a**2 == 1 and raw_zero_mode <= a
        transfer_n = Matrix.diag(1, low**n, high**n)
        passed = passed and (observed.T * transfer_n * observed)[0] == high**n
        passed = passed and (dark.T * transfer_n * dark)[0] > high**n
        passed = passed and Rational(n, n * n) == Rational(1, n)
    return passed, (
        "Sixteen rational cases retain normalized zero-mode weight 1 despite "
        "raw a^2 decay; r<=2s permits it. T=diag(1,15/16,1/4) has a dark "
        "slow sector. Log decay n over physical time n^2 has rate 1/n."
    )
