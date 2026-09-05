"""Independent finite creation-log computations and exact SU(3) moment checks.

The output verifies finite algebra and numerical examples, not an infinite-
volume theorem or a nonlinear rooted-ball estimate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

try:
    import numpy as np
    import scipy.linalg
    import scipy.special
except ImportError:
    np = None
    scipy = None

ROOT = Path(__file__).resolve().parents[1]


def star(left, right):
    """Disjoint-support product on flattened exact excitation basis vectors."""
    out = {}
    for x, a in left.items():
        for y, b in right.items():
            if any(i and j for i, j in zip(x, y, strict=True)):
                continue
            z = tuple(i or j for i, j in zip(x, y, strict=True))
            out[z] = out.get(z, 0) + a * b
    return {x: a for x, a in out.items() if a != 0}


def add(left, right, scale=1):
    out = dict(left)
    for x, a in right.items():
        out[x] = out.get(x, 0) + scale * a
    return {x: a for x, a in out.items() if a != 0}


def tensor(vector, n):
    return {
        x: math.prod(vector[i] for i in x) for x in itertools.product(range(len(vector)), repeat=n)
    }


def creation_log(vector, n):
    zero = (0,) * n
    assert vector.get(zero) == 1
    h = dict(vector)
    del h[zero]
    power = {zero: F(1)}
    result = {}
    for j in range(1, n + 1):
        power = star(power, h)
        result = add(result, power, F((-1) ** (j + 1), j))
    return result


def creation_exp(vector, n):
    result = {(0,) * n: F(1)}
    power = dict(result)
    for j in range(1, n + 1):
        power = star(power, vector)
        result = add(result, power, F(1, math.factorial(j)))
    return result


def log_derivative(base, derivative, n):
    zero = (0,) * n
    assert base.get(zero) == 1 and derivative.get(zero, 0) == 0
    h = dict(base)
    del h[zero]
    power = {zero: F(1)}
    result = {}
    for j in range(1, n + 1):
        result = add(result, star(power, derivative), (-1) ** (j + 1))
        power = star(power, h)
    return result


def exact_tensor_case(matrix, n):
    p = matrix[0][0]
    theta = matrix[0][1] / p
    e0 = [row[0] / p for row in matrix]
    e1 = [row[1] / p for row in matrix]
    base = tensor(e0, n)
    derivative = add(tensor(e1, n), base, -(theta**n))
    direct = log_derivative(base, derivative, n)
    ell = [theta] + [e1[i] - theta * e0[i] for i in range(1, len(matrix))]
    expected = tensor(ell, n)
    del expected[(0,) * n]
    assert direct == expected
    expected_base_log = {}
    for i in range(n):
        for excitation in range(1, len(matrix)):
            x = [0] * n
            x[i] = excitation
            expected_base_log[tuple(x)] = e0[excitation]
    assert creation_log(base, n) == expected_base_log

    z = F(1, 17)
    numerator = add(base, tensor(e1, n), z)
    normalized = {x: a / (1 + z * theta**n) for x, a in numerator.items()}
    assert creation_exp(creation_log(normalized, n), n) == normalized
    return direct, theta, ell


def exact_checks():
    rows = []
    two = [[F(1), F(1, 5)], [F(1, 5), F(6, 5)]]
    three = [
        [F(3, 2), F(1, 5), F(1, 7)],
        [F(1, 5), F(4, 3), F(1, 11)],
        [F(1, 7), F(1, 11), F(5, 4)],
    ]
    for n in range(1, 8):
        direct, theta, ell = exact_tensor_case(two, n)
        delta = ell[1]
        assert delta == (two[0][0] * two[1][1] - two[0][1] ** 2) / two[0][0] ** 2
        difference = add(direct, {(1,) * n: F(1)}, -1)
        norm = sum(
            F(2 ** sum(bool(i) for i in x), sum(bool(i) for i in x)) * abs(a)
            for x, a in difference.items()
            if x[0]
        ) / (2**n)
        s, d = abs(theta) / 2, abs(delta)
        formula = ((s + d) ** n - s**n - d**n + abs(delta**n - 1)) / n
        assert norm == formula
        rows.append({"dimension": 2, "blocks": n, "all_coefficients": len(direct)})
    for n in range(1, 5):
        direct, _theta, _ell = exact_tensor_case(three, n)
        rows.append({"dimension": 3, "blocks": n, "all_coefficients": len(direct)})
    return rows


def laurent_mul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, 0) + x * y
    return {key: value for key, value in out.items() if value}


def su3_moments():
    """Exact Weyl constant term for z3=(z1*z2)^(-1), including 1/|W|."""
    eigenvalues = [(1, 0), (0, 1), (-1, -1)]
    v = {x: 1 for x in eigenvalues + [(-i, -j) for i, j in eigenvalues]}
    weyl = {(0, 0): 1}
    for x, y in itertools.combinations(eigenvalues, 2):
        difference = (x[0] - y[0], x[1] - y[1])
        weyl = laurent_mul(weyl, {(0, 0): 1, difference: -1})
        weyl = laurent_mul(weyl, {(0, 0): 1, tuple(-i for i in difference): -1})
    power = {(0, 0): 1}
    moments = []
    for _ in range(9):
        moments.append(F(laurent_mul(weyl, power).get((0, 0), 0), 6))
        power = laurent_mul(power, v)
    assert moments[:4] == [1, 0, 2, 2]
    t = sp.Symbol("t", real=True)
    partition = sum(
        sp.Rational(x.numerator, x.denominator) * t**k / math.factorial(k)
        for k, x in enumerate(moments)
    )
    mean = sp.diff(partition, t) / partition
    norm_sq = (
        sp.diff(partition, t, 2).subs(t, 2 * t)
        - 2 * mean * sp.diff(partition, t).subs(t, 2 * t)
        + mean**2 * partition.subs(t, 2 * t)
    ) / (2 * partition**2)
    series = sp.series(norm_sq, t, 0, 2)
    assert series.removeO() == 1 + 2 * t
    return {"moments_0_to_8": list(map(str, moments)), "norm_squared_series": str(series)}


def norm_ratios(theta, delta, n, tau, mu, gamma):
    s, d = math.exp(-mu) * abs(theta), abs(delta)
    h = tau * gamma
    full_difference = abs(delta**n - 1)
    proper_log = []
    damped_log = []
    for k in range(1, n):
        if not s or not d:
            continue
        log_term = (
            scipy.special.gammaln(n)
            - scipy.special.gammaln(k)
            - scipy.special.gammaln(n - k + 1)
            + (n - k) * math.log(s)
            + k * math.log(d)
        )
        proper_log.append(log_term - math.log(tau * k))
        damped_log.append(log_term - math.log(math.expm1(h * k)))
    if full_difference:
        proper_log.append(math.log(full_difference) - math.log(tau * n))
        damped_log.append(math.log(full_difference) - math.log(math.expm1(h * n)))
    undamped = float(np.exp(scipy.special.logsumexp(proper_log))) if proper_log else 0.0
    damped = float(np.exp(scipy.special.logsumexp(damped_log))) if damped_log else 0.0
    q0 = math.exp(-h / 2)
    half_base = s + q0 * max(1, d)
    half_bound = (s + q0 * abs(delta - 1)) / h * half_base ** (n - 1)
    assert damped <= half_bound * (1 + 2e-12) + 1e-14
    return {
        "n": n,
        "full_support_undamped": full_difference / (tau * n),
        "rooted_undamped": undamped,
        "rooted_damped": damped,
        "half_damping_bound": half_bound,
    }


def numerical_checks():
    cases = [
        ("real_positive_diagonal", 1.0, 1.0, 0.1),
        ("real_pure_offdiagonal", 1.0, 0.0, 0.1),
        ("imaginary_pure_offdiagonal", 1.0, 0.0, 0.1j),
        ("small_coupling_positive_diagonal", 1.0, 1.0, 0.01),
    ]
    reports = []
    tau, mu, gamma = 0.1, 1.0, 1.0
    for name, a, b, t in cases:
        matrix = scipy.linalg.expm(t * np.array([[0.0, a], [a, b]]))
        p, q, r = matrix[0, 0], matrix[0, 1], matrix[1, 1]
        theta = q / p
        delta = (p * r - q * q) / p**2
        rho = math.sqrt(a * a + b * b / 4)
        denominator = np.cosh(rho * t) - b / (2 * rho) * np.sinh(rho * t)
        closed_delta = denominator ** (-2)
        closed_theta = a / rho * np.sinh(rho * t) / denominator
        assert abs(delta - closed_delta) < 1e-13
        assert abs(theta - closed_theta) < 1e-13

        for n in range(1, 5):
            transfer = np.array([[1.0]])
            for _ in range(n):
                transfer = np.kron(transfer, matrix)
            states = list(itertools.product(range(2), repeat=n))
            base = {x: complex(y) for x, y in zip(states, transfer[:, 0] / p**n, strict=True)}
            base[(0,) * n] = 1
            deriv = {x: complex(y) for x, y in zip(states, transfer[:, -1] / p**n, strict=True)}
            deriv = add(deriv, base, -(theta**n))
            deriv.pop((0,) * n, None)
            direct = log_derivative(base, deriv, n)
            for x, value in direct.items():
                k = sum(x)
                assert abs(value - theta ** (n - k) * delta**k) < 2e-13
            direct = add(direct, {(1,) * n: 1}, -1)
            damped_direct = sum(
                math.exp(mu * (sum(x) - n)) * abs(value) / math.expm1(tau * gamma * sum(x))
                for x, value in direct.items()
                if x[0]
            )
            expected = norm_ratios(theta, delta, n, tau, mu, gamma)["rooted_damped"]
            assert abs(damped_direct - expected) < 2e-12

        s, d = math.exp(-mu) * abs(theta), abs(delta)
        reports.append(
            {
                "case": name,
                "a": a,
                "b": b,
                "t": {"real": float(np.real(t)), "imag": float(np.imag(t))},
                "tau": tau,
                "mu": mu,
                "gamma": gamma,
                "theta": {"real": float(np.real(theta)), "imag": float(np.imag(theta))},
                "delta": {"real": float(np.real(delta)), "imag": float(np.imag(delta))},
                "undamped_base": s + d,
                "damped_base": s + d * math.exp(-tau * gamma),
                "half_damped_base": s + max(1, d) * math.exp(-tau * gamma / 2),
                "rows": [
                    norm_ratios(theta, delta, n, tau, mu, gamma)
                    for n in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024)
                ],
            }
        )
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "outputs" / "rooted_creator_obstruction" / "verification.json",
        help="Fresh JSON output path; existing files are never overwritten.",
    )
    numerical = parser.add_mutually_exclusive_group()
    numerical.add_argument(
        "--skip-numerics",
        action="store_true",
        help="Run only the exact rational and symbolic checks.",
    )
    numerical.add_argument(
        "--require-numerics",
        action="store_true",
        help="Fail if optional NumPy/SciPy examples cannot run.",
    )
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"refusing to overwrite existing output: {args.output}")
    available = np is not None and scipy is not None
    if args.require_numerics and not available:
        parser.error("--require-numerics needs the optional NumPy and SciPy packages")
    numerical_status = (
        "skipped by request"
        if args.skip_numerics
        else "passed"
        if available
        else "unavailable: optional NumPy/SciPy not installed"
    )
    report = {
        "schema": "rooted-disjoint-block-linearization/1",
        "scope": (
            "Finite algebra and illustrative numerical examples supporting the analytic "
            "proof; this certificate is not itself a nonlinear or infinite-volume proof."
        ),
        "exact_tensor_cases": exact_checks(),
        "su3_exact_moments": su3_moments(),
        "numerical_cases": numerical_checks() if numerical_status == "passed" else [],
        "numerical_status": numerical_status,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "script": str(Path(__file__).resolve()),
        "passed": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(report, indent=2) + "\n")
    except FileExistsError:
        parser.error(f"refusing to overwrite existing output: {args.output}")
    print("PASS: exact normalized creation logarithms, all tensor derivatives, SU(3) moments")
    if numerical_status == "passed":
        print("PASS: independent matrix exponentials, finite free damping, half-damping bound")
    else:
        print(f"NUMERICAL EXAMPLES: {numerical_status}")
    print(f"Certificate: {args.output}")
    for case in report["numerical_cases"]:
        last = case["rows"][-1]
        print(
            f"{case['case']}: undamped base={case['undamped_base']:.9f}, "
            f"damped base={case['damped_base']:.9f}, n=1024 ratios "
            f"{last['rooted_undamped']:.6g} -> {last['rooted_damped']:.6g}"
        )


if __name__ == "__main__":
    main()
