"""Exact algebra gates for NOTE_FLUX_singular_geometry_derivations_2026-08-28.

Standard output is deliberately compact: every gate is an exact SymPy identity.
"""

from __future__ import annotations

import sympy as sp


def gate(name: str, condition: bool) -> None:
    if not bool(condition):
        raise AssertionError(name)
    print(f"PASS {name}")


def main() -> None:
    # Generic four-shape ray tomography.
    a, A, B, C, D = sp.symbols("a A B C D", nonzero=True)

    def shape(vals: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
        q = sum(vals)
        e2 = sum(vals[i] * vals[j] for i in range(3) for j in range(i + 1, 3))
        e3 = vals[0] * vals[1] * vals[2]
        return sp.factor(A * q + B * e2 + 4 * C * e2 / q + D * e3 / q)

    gate("RAY_AXIS", sp.expand(shape((a, 0, 0)) - A * a) == 0)
    gate(
        "RAY_FACE",
        sp.expand(shape((a, a, 0)) - (2 * (A + C) * a + B * a**2)) == 0,
    )
    gate(
        "RAY_BODY",
        sp.expand(
            shape((a, a, a))
            - ((3 * A + 4 * C) * a + (3 * B + D / 3) * a**2)
        )
        == 0,
    )
    gate("RAY_BLIND_INTERCEPT", (3 * A + 4 * C) == 2 * (2 * (A + C)) - A)

    # Radial expansion through t^4, with x_i=n_i^2 and sum x_i=1.
    t = sp.symbols("t")
    x1, x2 = sp.symbols("x1 x2")
    x3 = 1 - x1 - x2
    xs = (x1, x2, x3)
    aa = tuple(
        t**2 * x - t**4 * x**2 / 12 + t**6 * x**3 / 360 for x in xs
    )
    q = sp.expand(sum(aa))
    e2 = sp.expand(sum(aa[i] * aa[j] for i in range(3) for j in range(i + 1, 3)))
    e3 = sp.expand(aa[0] * aa[1] * aa[2])
    s4 = sum(x**2 for x in xs)
    s6 = sum(x**3 for x in xs)
    p = sum(xs[i] * xs[j] for i in range(3) for j in range(i + 1, 3))
    r = x1 * x2 * x3
    delta = A * q + B * e2 + 4 * C * e2 / q + D * e3 / q
    series = sp.series(delta, t, 0, 6).removeO()
    expected = t**2 * (A + 4 * C * p) + t**4 * (
        -A * s4 / 12 + B * p + C * (p * s4 - s4 + s6) / 3 + D * r
    )
    gate("RADIAL_EXPANSION_T4", sp.simplify(series - expected) == 0)
    gate("P_RANGE_AXIS", sp.simplify(p.subs({x1: 1, x2: 0})) == 0)
    gate(
        "P_RANGE_DIAGONAL",
        sp.simplify(p.subs({x1: sp.Rational(1, 3), x2: sp.Rational(1, 3)}))
        == sp.Rational(1, 3),
    )

    # Exact incidence projector identity BB^dagger=qI-ww^dagger.
    d1, d2, d3, c1, c2, c3 = sp.symbols("d1 d2 d3 c1 c2 c3")
    boundary = sp.Matrix([[d2, -d1, 0], [d3, 0, -d1], [0, d3, -d2]])
    boundary_dag = sp.Matrix([[c2, c3, 0], [-c1, 0, c3], [0, -c1, -c2]])
    w = sp.Matrix([c3, -c2, c1])
    w_dag = sp.Matrix([[d3, -d2, d1]])
    qa = d1 * c1 + d2 * c2 + d3 * c3
    gate("INCIDENCE_PROJECTOR", boundary * boundary_dag == qa * sp.eye(3) - w * w_dag)
    gate("BOUNDARY_OF_BOUNDARY", boundary_dag * w == sp.zeros(3, 1))

    # Rank monotonicity and sharp upper bound.
    N, y = sp.symbols("N y", positive=True)
    tN = 2 * N * (N**2 - 4) / (
        (N**2 - 1) * (2 * N**2 - 1) * (4 * N**2 - 9)
    )
    gN = sp.factor(N**3 * tN)
    dt_num = sp.factor(sp.together(sp.diff(tN, N)).as_numer_denom()[0])
    dg_num = sp.factor(sp.together(sp.diff(gN, N)).as_numer_denom()[0])
    gate(
        "TN_DERIVATIVE_NUMERATOR",
        sp.expand(
            dt_num
            + 2 * (24 * N**8 - 190 * N**6 + 329 * N**4 - 97 * N**2 - 36)
        )
        == 0,
    )
    gate(
        "GN_DERIVATIVE_NUMERATOR",
        sp.expand(
            dg_num - 4 * N**3 * (2 * N**6 + 62 * N**4 - 151 * N**2 + 72)
        )
        == 0,
    )
    dec_poly = 24 * (9 + y) ** 4 - 190 * (9 + y) ** 3 + 329 * (9 + y) ** 2 - 97 * (9 + y) - 36
    inc_poly = 2 * (9 + y) ** 3 + 62 * (9 + y) ** 2 - 151 * (9 + y) + 72
    gate(
        "TN_DECREASE_POSITIVE_POLY",
        sp.Poly(sp.expand(dec_poly), y).all_coeffs() == [24, 674, 6863, 29639, 44694],
    )
    gate(
        "GN_INCREASE_POSITIVE_POLY",
        sp.Poly(sp.expand(inc_poly), y).all_coeffs() == [2, 116, 1451, 5193],
    )
    gate(
        "GN_QUARTER_GAP",
        sp.simplify(
            sp.Rational(1, 4)
            - gN
            - (2 * N**4 + 31 * N**2 - 9)
            / (
                4
                * (N - 1)
                * (N + 1)
                * (2 * N - 3)
                * (2 * N + 3)
                * (2 * N**2 - 1)
            )
        )
        == 0,
    )
    gate("TN_SU3", sp.factor(tN.subs(N, 3)) == sp.Rational(5, 612))
    scaled_33 = sp.factor(
        4 * 3**3 * tN.subs(N, 3) * 3**2 * sp.sin(sp.pi / 3) ** 2
    )
    gate("RANK_VOLUME_LOWER_ENDPOINT", scaled_33 == sp.Rational(405, 68))

    print("PASS 16/16 exact gates")


if __name__ == "__main__":
    main()
