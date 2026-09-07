"""Exact actual path, local Wilson cubic and harmonic fast-Green controls."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as s


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shifted(x, axis, amount, n):
    y = list(x)
    y[axis] = (y[axis] + amount) % n
    return tuple(y)


def geometry(n):
    require(isinstance(n, int) and n >= 4 and n % 2 == 0, "even fine period >=4")
    vertices = list(itertools.product(range(n), repeat=3))
    volume = n**3
    modes = []
    for axis, oscillatory in ((0, False), (1, False), (1, True)):
        modes.append(
            {
                (x, i): int(i == axis) * ((-1) ** x[0] if oscillatory else 1)
                for x in vertices
                for i in range(3)
            }
        )
    gram = [[sum(a[key] * b[key] for key in a) for b in modes] for a in modes]
    require(
        gram == [[volume * int(i == j) for j in range(3)] for i in range(3)],
        "three unit modes after division by sqrt(volume)",
    )
    for field, eigenvalue in zip(modes, (0, 0, 4), strict=True):
        require(
            all(
                sum(field[(shifted(x, i, -1, n), i)] - field[(x, i)] for i in range(3)) == 0
                for x in vertices
            ),
            "physical divergence",
        )
        curls = {}
        for x in vertices:
            for i, j in itertools.combinations(range(3), 2):
                curls[(x, i, j)] = (
                    field[(x, i)]
                    + field[(shifted(x, i, 1, n), j)]
                    - field[(shifted(x, j, 1, n), i)]
                    - field[(x, j)]
                )
        laplace = dict.fromkeys(field, 0)
        for (x, i, j), value in curls.items():
            for key, sign in (
                ((x, i), 1),
                ((shifted(x, i, 1, n), j), 1),
                ((shifted(x, j, 1, n), i), -1),
                ((x, j), -1),
            ):
                laplace[key] += sign * value
        require(
            all(laplace[key] == eigenvalue * field[key] for key in field),
            "original curl-adjoint eigenvalue",
        )
    coarse = list(itertools.product(range(n // 2), repeat=3))
    offsets = list(itertools.product(range(2), repeat=3))
    images = []
    adjoint_constant = [{key: Fraction(0) for key in modes[0]} for _ in range(2)]
    for mode in modes:
        values = {}
        for b in coarse:
            for axis in range(3):
                total = 0
                for y in offsets:
                    base = tuple((2 * b[i] + y[i]) % n for i in range(3))
                    for step in range(2):
                        total += mode[(shifted(base, axis, step, n), axis)]
                values[(b, axis)] = Fraction(total, 8)
        images.append(values)
    for index in range(2):
        require(
            all(value == (2 if axis == index else 0) for (_, axis), value in images[index].items()),
            "retained constant path",
        )
        for b in coarse:
            for y in offsets:
                base = tuple((2 * b[i] + y[i]) % n for i in range(3))
                for step in range(2):
                    adjoint_constant[index][(shifted(base, index, step, n), index)] += Fraction(
                        1, 8
                    )
        require(
            all(
                adjoint_constant[index][key] == Fraction(modes[index][key], 4)
                for key in modes[index]
            ),
            "harmonic belongs to actual cotangent range",
        )
    require(all(value == 0 for value in images[2].values()), "actual path-null fast mode")
    signs = [(-1) ** x[0] for x in vertices]
    require(sum(signs) == 0, "summed parallel plaquette coefficient cancels")
    return {
        "period": n,
        "vertices": volume,
        "unnormalized_mode_Gram": gram,
        "curl_eigenvalues": [0, 0, 4],
        "actual_path_fast_image_zero": True,
        "cotangent_harmonic_factor": "1/4",
        "plaquette_sign_sum": sum(signs),
    }


def bch_and_character():
    x = s.Matrix(s.symbols("x0:3", real=True))
    y = s.Matrix(s.symbols("y0:3", real=True))
    z = s.Matrix(s.symbols("z0:3", real=True))
    checked = []
    pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    basis = [-s.I * matrix / 2 for matrix in pauli]
    require(
        all(
            s.simplify(-2 * s.trace(a * b)) == int(i == j)
            for i, a in enumerate(basis)
            for j, b in enumerate(basis)
        ),
        "SU2 metric",
    )
    require(
        all(
            s.simplify(-s.trace(a * b)) == s.Rational(int(i == j), 2)
            for i, a in enumerate(basis)
            for j, b in enumerate(basis)
        ),
        "SU2 b_rep=1/2",
    )
    for sign in (1, -1):
        words = [x, y - sign * z, -x, -y - sign * z]
        f1 = sum(words, s.zeros(3, 1))
        f2 = sum(
            (words[i].cross(words[j]) / 2 for i in range(4) for j in range(i + 1, 4)), s.zeros(3, 1)
        ).applyfunc(s.expand)
        require(f1 == -2 * sign * z, "first BCH term")
        require(
            f2 == (x.cross(y) - sign * x.cross(z) - sign * y.cross(z)).applyfunc(s.expand),
            "full second BCH term",
        )
        require(s.expand(f1.dot(f2) + 2 * sign * z.dot(x.cross(y))) == 0, "cubic contraction")
        # Independent ordered SU2 matrix exponentials, through degree three.
        a, b, c = s.symbols("a b c", real=True)
        matrix_words = [
            a * basis[0],
            b * basis[1] - sign * c * basis[2],
            -a * basis[0],
            -b * basis[1] - sign * c * basis[2],
        ]
        product = [s.eye(2), s.zeros(2), s.zeros(2), s.zeros(2)]
        for word in matrix_words:
            exponential = [word**degree / s.factorial(degree) for degree in range(4)]
            product = [
                sum(
                    (product[k] * exponential[degree - k] for k in range(degree + 1)), s.zeros(2)
                ).applyfunc(s.expand)
                for degree in range(4)
            ]
        cubic_character = s.expand(-s.trace(product[3]))
        require(cubic_character == -sign * a * b * c, "direct fundamental Wilson character")
        require(
            s.expand(2 * cubic_character + 2 * sign * a * b * c) == 0,
            "magnetic 2u character has coefficient v squared when v squared=u",
        )
        checked.append(
            {
                "plaquette_sign": sign,
                "character_cubic": str(cubic_character),
                "BCH_contraction_factor": -2 * sign,
            }
        )
    # With the commutator discarded the selected cubic is exactly lost.
    require(all(row["BCH_contraction_factor"] != 0 for row in checked), "omitted BCH negative")
    return {"SU2_b_rep": "1/2", "ordered_word_cases": checked, "omitted_BCH_negative": True}


def invariant_and_energy():
    indices = range(3)
    eps = {
        (a, b, c): int(s.LeviCivita(a, b, c)) for a, b, c in itertools.product(indices, repeat=3)
    }
    norm = sum(value**2 for value in eps.values())
    require(norm == 6, "physical color tensor norm C_A d")
    for generator, a, b, c in itertools.product(indices, repeat=4):
        image = sum(
            eps[(generator, a, k)] * eps[(k, b, c)]
            + eps[(generator, b, k)] * eps[(a, k, c)]
            + eps[(generator, c, k)] * eps[(a, b, k)]
            for k in indices
        )
        require(image == 0, "complete common Gauss annihilates the triple tensor")
    rho, omega, volume, speed = s.symbols("rho omega V v", positive=True)
    energy = 2 * rho + omega
    coefficient_squared = 4 * speed**4 / (volume**3 * (2 * rho) * (2 * rho) * (2 * omega))
    selected = s.factor(norm * coefficient_squared / energy)
    require(
        s.cancel(selected - 3 * speed**4 / (volume**3 * rho**2 * omega * (2 * rho + omega))) == 0,
        "all coordinate and Fock normalization factors",
    )
    limit = s.limit(rho**2 * selected.subs(omega, s.sqrt(4 * speed**2 + rho**2)), rho, 0, dir="+")
    require(s.simplify(limit - 3 * speed**2 / (4 * volume**3)) == 0, "strict divergent coefficient")
    m = s.symbols("m", positive=True, integer=True)
    rational_rho = (4 * m + 1) / (2 * m * (2 * m + 1))
    rational_omega = (8 * m * m + 4 * m + 1) / (2 * m * (2 * m + 1))
    require(s.cancel(rational_omega**2 - rational_rho**2 - 4) == 0, "fixed v=1 rational regulator")
    sequence = s.factor(
        selected.subs({rho: rational_rho, omega: rational_omega, speed: 1, volume: 64})
    )
    sequence_limit = s.limit(sequence / m**2, m, s.oo)
    require(sequence_limit == s.Rational(3, 4 * 64**3), "unbounded exact rational sequence")
    rows = [
        {
            "m": k,
            "rho": str(rational_rho.subs(m, k)),
            "omega_h": str(rational_omega.subs(m, k)),
            "selected_resolvent_diagonal": str(sequence.subs(m, k)),
        }
        for k in (1, 10, 100)
    ]
    # Independent spatial exterior-three realization of the color singlet.
    spatial = s.Matrix([eps[index] for index in itertools.product(indices, repeat=3)])
    retained = s.diag(1, 1, 0)
    one_fast = s.eye(3) - retained
    source_cube = s.kronecker_product(retained, retained, retained)
    fast_cube = s.kronecker_product(one_fast, one_fast, one_fast)
    omega_matrix = s.diag(rho, rho, omega)
    energy_matrix = sum(
        (
            s.kronecker_product(*[omega_matrix if j == leg else s.eye(3) for j in indices])
            for leg in indices
        ),
        s.zeros(27),
    )
    require((s.eye(27) - source_cube) * spatial == spatial, "full Q retains mixed occupation")
    require(energy_matrix * spatial == energy * spatial, "exact mixed-sector F energy")
    require(
        fast_cube * spatial == s.zeros(27, 1) and spatial.dot(spatial) == 6,
        "all-fast tensorization loses the nonzero physical spatial tensor",
    )
    return {
        "SU2_color_tensor_norm_squared": norm,
        "Gauss_generator_components_checked": 81,
        "selected_energy": str(energy),
        "selected_resolvent_diagonal": str(selected),
        "rho_squared_diagonal_limit": str(limit),
        "rational_sequence": rows,
        "sequence_over_m_squared_limit": str(sequence_limit),
        "all_fast_tensor_negative": True,
        "scope": (
            "Actual physical harmonic occupation sector; no claim for the globally summed forcing."
        ),
    }


def controls():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls reject optimized Python execution")
    return {
        "actual_path_geometry": [geometry(4), geometry(6)],
        "ordered_Wilson_cubic": bch_and_character(),
        "physical_harmonic_fast_energy": invariant_and_energy(),
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact controls reject optimized Python execution")
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    require(bool(args.output) != bool(args.replay), "choose output or replay")
    if args.output and args.output.exists():
        raise FileExistsError("Output must be fresh")
    source = Path(__file__).resolve()
    paths = [source, source.with_name("LOCAL_PLAQUETTE_HARMONIC_FAST_OBSTRUCTION.md")]
    hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    payload = controls()
    require(
        hashes == {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
        "sources changed during control",
    )
    if args.replay:
        report = json.loads(args.replay.read_text(encoding="utf-8"))
        require(report["source_sha256"] == hashes, "source hash mismatch")
        require(report["controls"] == payload, "complete payload mismatch")
        require(report["passed"] is True, "report success marker")
        print("PASS: full local plaquette obstruction payload and pins replayed")
        return
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(
            {"passed": True, "source_sha256": hashes, "controls": payload},
            stream,
            indent=2,
            sort_keys=True,
        )
        stream.write("\n")
    print("PASS: actual path geometry, ordered Wilson cubic and invariant fast energy")


if __name__ == "__main__":
    main()
