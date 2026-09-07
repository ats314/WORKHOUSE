"""Exact finite controls for the actual Gaussian fast Green identity.

These controls certify finite matrix identities, not infinite-volume estimates.
Run with the repository Python; only SymPy and the standard library are used.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import sympy as s


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exterior(a, degree):
    rows = list(itertools.combinations(range(a.rows), degree))
    cols = list(itertools.combinations(range(a.cols), degree))
    return s.Matrix(len(rows), len(cols), lambda i, j: a.extract(rows[i], cols[j]).det())


def additive_exterior(a, degree):
    t = s.Symbol("t")
    return exterior(s.eye(a.rows) + t * a, degree).diff(t).subs(t, 0)


def short(a, u):
    if not u.cols:
        return a
    return a - a * u * (u.T * a * u).inv() * u.T * a


def matrix_strings(a):
    return [[str(a[i, j]) for j in range(a.cols)] for i in range(a.rows)]


def family(name, b, w, degree):
    # b is the positive square root of the oscillator frequency Omega.
    omega = b * b
    d = additive_exterior(omega, degree)
    ell = exterior(b.inv(), degree)
    u = exterior(w, degree)
    source = ell * u
    p = source * (source.T * source).inv() * source.T if source.cols else s.zeros(d.rows)
    q = s.eye(d.rows) - p
    direct = ell * q * (q * d * q + p).inv() * q * ell
    prior = ell * d.inv() * ell
    proposed = short(prior, u)
    require(direct == proposed, f"{name}: projected inverse differs from shorted energy prior")
    require(proposed * u == s.zeros(d.rows, u.cols), f"{name}: retained sources not annihilated")

    # Independent constrained Euler-Lagrange solve, including its multiplier.
    if source.cols:
        kkt = d.row_join(source).col_join(source.T.row_join(s.zeros(source.cols)))
        rhs = ell.col_join(s.zeros(source.cols, d.rows))
        solution = kkt.inv() * rhs
        q_solution = solution[: d.rows, :]
    else:
        q_solution = d.inv() * ell
    require(ell * q_solution == proposed, f"{name}: constrained variational solve disagrees")
    require(source.T * q_solution == s.zeros(source.cols, d.rows), f"{name}: KKT constraint failed")

    probe = s.Matrix([(-1) ** i * (i + 1) for i in range(d.rows)])
    energy = (probe.T * proposed * probe)[0]
    require(energy > 0, f"{name}: chosen fast exchange must be nonzero")
    equal_time = short(ell * ell, u)
    require(equal_time != proposed, f"{name}: negative control lost energy denominator")

    return {
        "name": name,
        "degree": degree,
        "frequency": matrix_strings(omega),
        "observation_cotangents": matrix_strings(w),
        "nonreducing_source": p * d != d * p,
        "actual_coordinate_green": matrix_strings(proposed),
        "probe_energy": str(energy),
        "kkt_and_compressed_inverse_agree": True,
        "equal_time_substitution_rejected": True,
    }


def derive():
    records = [
        family(
            "first-chaos noncommuting frequency", s.Matrix([[2, 1], [1, 3]]), s.Matrix([1, 0]), 1
        ),
        family(
            "second exterior nonreducing source",
            s.Matrix([[2, 1, 0], [1, 3, 0], [0, 0, 4]]),
            s.Matrix([[1, 0], [0, 1], [1, 1]]),
            2,
        ),
        family(
            "Lie-cubic exterior nonreducing source",
            s.diag(1, 2, 3, 4),
            s.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]),
            3,
        ),
    ]
    require(
        all(r["nonreducing_source"] for r in records), "all witnesses must retain baseline coupling"
    )

    omega = s.diag(1, 4, 9, 16)
    w = s.eye(4)[:, :3]
    one = short(omega.inv() ** 2, w)
    b = s.diag(1, 2, 3, 4)
    ell3 = exterior(b.inv(), 3)
    three = short(ell3 * additive_exterior(omega, 3).inv() * ell3, exterior(w, 3))
    naive = exterior(one, 3)
    require(
        naive == s.zeros(4) and three.rank() == 3,
        "all-fast versus at-least-one-fast negative failed",
    )
    r, h = s.symbols("r h", positive=True)
    harmonic_prior = 1 / (r**2 * h * (2 * r + h))
    require(
        s.limit(r**2 * harmonic_prior, r, 0) == 1 / h**2, "harmonic divergence coefficient failed"
    )
    return {
        "schema": "workhouse-full-fast-green-controls/v1",
        "scope": (
            "finite exact matrices and exterior Lie-cubic sector; "
            "no continuum or uniform remainder certification"
        ),
        "families": records,
        "all_fast_tensorization_negative": {
            "naive_rank": naive.rank(),
            "actual_rank": three.rank(),
            "actual_diagonal": [str(x) for x in three.diagonal()],
        },
        "two_retained_harmonic_legs": {
            "coordinate_energy_factor": str(harmonic_prior),
            "rescaled_limit_at_fixed_fast_frequency": str(1 / h**2),
            "scope": (
                "algebraic denominator only; actual Wilson vertex is established "
                "in the separate analytic witness"
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = derive()
    if args.verify:
        require(
            json.loads(args.verify.read_text(encoding="utf-8")) == result,
            "saved exact report mismatch",
        )
        print("PASS: independent constrained solves, compressed inverses, and negative controls")
    else:
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
