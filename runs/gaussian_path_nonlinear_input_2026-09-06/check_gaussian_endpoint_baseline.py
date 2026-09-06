"""Exact finite controls for the Gaussian path endpoint baseline.

These algebraic checks do not replace the all-size analytic proof.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

import sympy as s


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def simple(matrix: s.MatrixBase) -> s.Matrix:
    return s.Matrix(matrix).applyfunc(s.simplify)


def psd(matrix: s.MatrixBase) -> list[str]:
    current = simple(matrix)
    require(current == current.conjugate().T, "Hermitian matrix required")
    out = []
    for i in range(current.rows):
        pivot = s.simplify(current[i, i])
        require(pivot.is_nonnegative is True, "negative or undecidable pivot")
        out.append(str(pivot))
        if pivot == 0:
            require(
                all(current[i, j] == 0 for j in range(i + 1, current.cols)),
                "zero pivot has nonzero remaining row",
            )
            continue
        for j in range(i + 1, current.rows):
            for k in range(j, current.cols):
                value = s.simplify(current[j, k] - current[j, i] * current[i, k] / pivot)
                current[j, k] = value
                current[k, j] = s.conjugate(value)
    return out


def tensor_power(matrix: s.MatrixBase, n: int) -> s.Matrix:
    out = s.ones(1)
    for _ in range(n):
        out = s.kronecker_product(out, matrix)
    return out


def symmetric_basis(d: int, n: int) -> s.Matrix:
    words = list(itertools.product(range(d), repeat=n))
    labels = sorted({tuple(sorted(word)) for word in words})
    index = {label: i for i, label in enumerate(labels)}
    counts = Counter(tuple(sorted(word)) for word in words)
    out = s.zeros(len(words), len(labels))
    for row, word in enumerate(words):
        label = tuple(sorted(word))
        out[row, index[label]] = 1 / s.sqrt(counts[label])
    require(simple(out.T * out) == s.eye(len(labels)), "orthonormal symmetric basis")
    return out


def functor_controls() -> dict:
    j = s.Matrix([[s.Rational(3, 5), 0], [s.Rational(4, 5), 0], [0, 1]])
    t = s.Matrix(
        [
            [s.Rational(1, 2), s.Rational(1, 8), s.Rational(1, 16)],
            [s.Rational(1, 8), s.Rational(2, 3), s.Rational(1, 12)],
            [s.Rational(1, 16), s.Rational(1, 12), s.Rational(3, 4)],
        ]
    )
    psd(t)
    psd(s.eye(3) - t)
    require(j.T * j == s.eye(2), "one-particle isometry")
    m = j.T * t * j
    sectors = []
    for n in range(4):
        f = symmetric_basis(3, n)
        c = symmetric_basis(2, n)
        jn = simple(f.T * tensor_power(j, n) * c)
        tn = simple(f.T * tensor_power(t, n) * f)
        lhs = simple(jn.T * tn * jn)
        rhs = simple(c.T * tensor_power(m, n) * c)
        require(lhs == rhs, "Gamma compression failed")
        sectors.append({"particles": n, "fine_dimension": f.cols, "source_dimension": c.cols})
    defect = simple(j.T * t * t * j - m * m)
    omitted = simple(j.T * t * (s.eye(3) - j * j.T) * t * j)
    require(defect == omitted and defect != s.zeros(2), "nonsemigroup defect")
    return {
        "scope": "Exact tensor functor through three bosons; nonzero memory defect.",
        "sectors": sectors,
        "endpoint_matrix": [[str(x) for x in row] for row in m.tolist()],
        "memory_defect_pivots": psd(defect),
    }


def marginal_and_static_controls() -> dict:
    omega = s.Matrix([[2, 1], [1, 2]])
    w = s.Matrix([1, 0])
    gram = (w.T * omega.inv() * w)[0]
    require(gram == s.Rational(2, 3), "true marginal Gram")
    source = s.Matrix([s.sqrt(3) / 2, s.Rational(1, 2)])
    fiber = s.Matrix([-s.Rational(1, 2), s.sqrt(3) / 2])
    rotation = source.row_join(fiber)
    h1 = simple(rotation.T * s.diag(1, 3) * rotation)
    require(
        h1 == s.Matrix([[s.Rational(3, 2), s.sqrt(3) / 2], [s.sqrt(3) / 2, s.Rational(5, 2)]]),
        "source normalization",
    )
    sym = symmetric_basis(2, 2)
    h2 = simple(
        sym.T * (s.kronecker_product(h1, s.eye(2)) + s.kronecker_product(s.eye(2), h1)) * sym
    )
    expected = s.Matrix(
        [
            [3, s.sqrt(s.Rational(3, 2)), 0],
            [s.sqrt(s.Rational(3, 2)), 4, s.sqrt(s.Rational(3, 2))],
            [0, s.sqrt(s.Rational(3, 2)), 5],
        ]
    )
    require(h2 == expected, "two-boson normalization")
    colors = 3
    occupations = [
        tuple(word.count(i) for i in range(2 * colors))
        for word in itertools.combinations_with_replacement(range(2 * colors), 2)
    ]
    occupation_index = {occupation: i for i, occupation in enumerate(occupations)}
    one_colored = s.kronecker_product(h1, s.eye(colors))
    many_colored = s.zeros(len(occupations))
    for col, occupation in enumerate(occupations):
        for destroyed in range(2 * colors):
            if occupation[destroyed] == 0:
                continue
            remainder = list(occupation)
            remainder[destroyed] -= 1
            for created in range(2 * colors):
                coefficient = one_colored[created, destroyed]
                if coefficient == 0:
                    continue
                final = remainder.copy()
                final[created] += 1
                row = occupation_index[tuple(final)]
                many_colored[row, col] += coefficient * s.sqrt(
                    occupation[destroyed] * (remainder[created] + 1)
                )
    singlets = s.zeros(len(occupations), 3)
    for color in range(colors):
        for column, modes in enumerate(
            [(color, color), (color, colors + color), (colors + color, colors + color)]
        ):
            occupation = tuple(modes.count(i) for i in range(2 * colors))
            singlets[occupation_index[occupation], column] = 1 / s.sqrt(colors)
    require(simple(singlets.T * singlets) == s.eye(3), "invariant pair normalization")
    require(
        simple(many_colored * singlets - singlets * h2) == s.zeros(len(occupations), 3),
        "complete invariant pair intertwining",
    )
    rows = []
    for h in [h1, h2]:
        f = h[1:, 1:]
        b = h[1:, :1]
        u = simple(f.inv() * b)
        loss = s.simplify((b.T * u)[0])
        k = s.simplify(h[0, 0] - loss)
        metric = s.simplify(1 + (u.T * u)[0])
        rows.append(
            {
                "retained_energy": str(h[0, 0]),
                "loss": str(loss),
                "schur": str(k),
                "graph_metric": str(metric),
                "normalized_schur": str(s.simplify(k / metric)),
            }
        )
    require(rows[0]["schur"] == "6/5" and rows[1]["schur"] == "96/37", "exact static values")
    require(
        rows[0]["normalized_schur"] == "15/14" and rows[1]["normalized_schur"] == "444/191",
        "normalized graph values",
    )
    require(
        s.Rational(rows[1]["schur"]) != 2 * s.Rational(rows[0]["schur"]),
        "static Schur must not falsely second-quantize",
    )
    return {
        "scope": (
            "Actual marginal and exact one/two-particle static Schur, "
            "including invariant pair sector."
        ),
        "gram": str(gram),
        "frequency_source_weights": ["3/4", "1/4"],
        "colored_two_boson_dimension": len(occupations),
        "invariant_pair_rank": 3,
        "static": rows,
        "two_particle_relative_loss": "5/37",
    }


def gaussian_score_controls() -> dict:
    q, z, b = s.symbols("q z b", real=True)
    c, g = s.symbols("c g", positive=True)
    log_density = -c * (z + b * q / c) ** 2 / g**2
    score = s.diff(log_density, q)
    require(s.simplify(score + 2 * b * (z + b * q / c) / g**2) == 0, "normalized conditional score")
    fisher = s.simplify(4 * b**2 / g**4 * g**2 / (2 * c))
    require(fisher == 2 * b**2 / (c * g**2), "conditional Fisher")
    root = (1 + s.I * s.sqrt(3)) / 2
    aliases = [root, -root]
    weights = [s.simplify((1 + t) * (1 + s.conjugate(t)) / 4) for t in aliases]
    frequencies2 = [s.simplify(2 - t - s.conjugate(t)) for t in aliases]
    require(
        weights == [s.Rational(3, 4), s.Rational(1, 4)] and frequencies2 == [1, 3],
        "actual n6 L2 transverse alias",
    )
    rotation = s.Matrix([[s.sqrt(3) / 2, -s.Rational(1, 2)], [s.Rational(1, 2), s.sqrt(3) / 2]])
    precision = simple(rotation.T * s.diag(1, s.sqrt(3)) * rotation)
    require(
        s.simplify(precision[0, 1] - (3 - s.sqrt(3)) / 4) == 0, "actual path conditional coupling"
    )
    coefficient = s.simplify(2 * precision[0, 1] ** 2 / precision[1, 1])
    require(coefficient.is_positive is True, "strictly positive path Fisher")
    return {
        "scope": ("Exact Gaussian density algebra and actual n6 L2 K=(2pi/3,0,0) transverse path."),
        "score": str(score),
        "fisher": str(fisher),
        "alias_weights": list(map(str, weights)),
        "frequency_squares": list(map(str, frequencies2)),
        "path_fisher_coefficient": str(coefficient),
        "physical_scale": "coefficient/g^2; no nonlinear Wilson ground claim",
    }


def gram_sandwich_controls() -> dict:
    low = s.Matrix([[2, s.Rational(1, 2)], [s.Rational(1, 2), 1]])
    high = s.diag(s.Rational(1, 10), s.Rational(1, 20))
    epsilon = s.Rational(1, 4)
    require(low * high != high * low, "noncommuting Gram control")
    psd(epsilon * low - high)
    gram = low + high
    slow, fast = s.Rational(4, 5), s.Rational(2, 5)
    lag = slow * low + fast * high
    lower = lag - slow * gram / (1 + epsilon)
    upper = slow * gram - lag
    pi, k, ell, v, time, energy = s.symbols("pi k L v s E", positive=True)
    eta = pi**8 * k**2 / 1536
    eps = s.simplify(eta * k / 2)
    relative = s.simplify(eps / (time * 2 * k / pi))
    window = s.simplify(relative.subs(k, pi * ell * energy / (2 * v)))
    require(eps == pi**8 * k**3 / 3072, "inverse frequency improvement")
    require(relative == pi**9 * k**2 / (6144 * time), "relative low frequency constant")
    require(window == pi**11 * ell**2 * energy**2 / (24576 * time * v**2), "whole-window constant")
    return {
        "scope": ("A noncommuting matrix sandwich and exact algebra of all-size bound constants."),
        "lower_pivots": psd(lower),
        "upper_pivots": psd(upper),
        "epsilon": str(eps),
        "relative": str(relative),
        "window": str(window),
    }


def row_gram_controls() -> dict:
    cases = []
    for ell in range(1, 13):
        counts = Counter(a - b + c - d for a, b, c, d in itertools.product(range(ell), repeat=4))
        constant = s.Rational(counts[0], ell**3)
        cosine = s.Rational(2 * counts[ell], ell**3)
        expected_a = s.Rational(2 * ell**2 + 1, 3 * ell**2)
        expected_b = s.Rational(ell**2 - 1, 3 * ell**2)
        require(constant == expected_a and cosine == expected_b, "fourth alias coefficient count")
        require(
            expected_a + expected_b == 1 and expected_b / expected_a < s.Rational(1, 2),
            "local row inverse ratio",
        )
        cases.append({"L": ell, "A": str(constant), "B": str(cosine)})
    kernel_cases = []
    for ell, period in itertools.product([2, 3, 5], [1, 2, 3, 4, 7]):
        a = s.Rational(2 * ell**2 + 1, 3 * ell**2)
        b = s.Rational(ell**2 - 1, 3 * ell**2)
        shift = s.zeros(period)
        for i in range(period):
            shift[i, (i + 1) % period] = 1
        operator = (a * s.eye(period) + b * (shift + shift.T) / 2) / ell
        inverse = operator.inv()
        for i in range(period):
            for j in range(period):
                distance = min((i - j) % period, (j - i) % period)
                require(
                    abs(inverse[i, j]) <= s.Rational(3 * ell, 2**distance),
                    "periodic row inverse bound",
                )
        kernel_cases.append({"L": ell, "period": period})
    return {
        "scope": (
            "Exact unconstrained row Gram counts L1..12 and periodic inverse entries; "
            "not physical/marginal locality."
        ),
        "moments": cases,
        "inverse_cases": kernel_cases,
    }


def controls() -> dict:
    return {
        "functor": functor_controls(),
        "marginal_static": marginal_and_static_controls(),
        "gaussian_score": gaussian_score_controls(),
        "gram_sandwich": gram_sandwich_controls(),
        "row_gram": row_gram_controls(),
    }


def main() -> None:
    require(__debug__, "python -O is not an accepted verification mode")
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument("--replay", type=Path)
    args = parser.parse_args()
    if args.output:
        require(not args.output.exists(), "refusing to overwrite evidence")
    here = Path(__file__).resolve().parent
    names = [Path(__file__).name, "EXACT_GAUSSIAN_PATH_ENDPOINT_BASELINE.md"]
    pins = {name: hashlib.sha256((here / name).read_bytes()).hexdigest() for name in names}
    payload = {"schema": 1, "source_sha256": pins, "checks": controls()}
    if args.replay:
        saved = json.loads(args.replay.read_text(encoding="utf-8"))
        require(saved == payload, "replayed payload or source pins differ")
        print("All five exact Gaussian endpoint families replayed.")
    else:
        args.output.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"All five exact Gaussian endpoint families passed: {args.output}")


if __name__ == "__main__":
    main()
