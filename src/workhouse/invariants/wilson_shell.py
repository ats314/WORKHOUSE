"""Exact controls for the analytic fixed-observable Wilson shell continuation.

The infinite-dimensional estimates are proved in the companion note. These
checks certify only finite tensors, exact constants and algebraic interfaces.
"""

from __future__ import annotations

from itertools import combinations, product

from sympy import Matrix, Rational, S, diag, eye, kronecker_product, simplify, symbols, zeros

from ._core import _suite

shell = _suite("Wilson complete shell: complex anchoring and weighted matching interfaces")
CITE = "WILSON_SHELL; G18; G19"


def _embed(local, support, sites):
    """Independent computational-basis embedding, with site zero leftmost."""
    bits = list(product((0, 1), repeat=sites))
    result = zeros(2**sites)
    outside = set(range(sites)) - set(support)
    for i, left in enumerate(bits):
        for j, right in enumerate(bits):
            if all(left[k] == right[k] for k in outside):
                a = sum(left[k] * 2 ** (len(support) - 1 - p) for p, k in enumerate(support))
                b = sum(right[k] * 2 ** (len(support) - 1 - p) for p, k in enumerate(support))
                result[i, j] = local[a, b]
    return result


@shell.check(
    "Wilson nonnormal anchored activities satisfy an exact full-tensor bilinear certificate",
    CITE + " S8",
)
def _nonnormal_anchoring():
    sites = 4
    supports = ((0, 1), (1, 2), (2, 3))
    local = zeros(4)
    local[1, 2], local[2, 3] = Rational(1, 1000), Rational(1, 2000)
    q = diag(0, 1, 1, 1)
    # a strictly exceeds the exact norm 1/1000 of this weighted shift.
    a, d = Rational(1, 500), diag(1, Rational(1, 2))
    perturbation, majorant, families = zeros(16), zeros(16), 0
    for size in range(1, len(supports) + 1):
        for family in combinations(supports, size):
            union = set().union(*map(set, family))
            if len(union) != sum(map(len, family)):
                continue
            term, bound = eye(16), eye(16)
            for support in family:
                term *= _embed(local, support, sites)
                bound *= a * _embed(q, support, sites)
            for site in set(range(sites)) - union:
                spectator = _embed(d, (site,), sites)
                term *= spectator
                bound *= spectator
            perturbation += term
            majorant += bound
            families += 1
    f, c = perturbation[1:, 1:], majorant[1:, 1:]
    # This is equivalent by the Schur complement to [[C,F],[F*,C]] >= 0.
    defect = c - f.T * c.inv() * f
    lower, diagonal = defect.LDLdecomposition(hermitian=False)
    certified = lower * diagonal * lower.T == defect and all(x > 0 for x in diagonal.diagonal())
    return (
        certified
        and local * local.T != local.T * local
        and local == q * local * q
        and families == 4,
        f"Four qubits, three overlapping pair activities, {families} nonempty disjoint families; "
        "the full 15-dimensional nonvacuum Schur complement has an exact positive LDL diagonal. "
        "Activities are nonnormal and annihilate both vacuum legs; no selected-source restriction",
    )


@shell.check(
    "FINDING: right vacuum annihilation alone does not give the anchored bilinear bound",
    CITE + " S8",
)
def _one_sided_falsifier():
    p, q = diag(1, 0), diag(0, 1)
    f = Matrix([[0, 1], [0, 0]])
    vacuum, excited = Matrix([1, 0]), Matrix([0, 1])
    lhs = (vacuum.T * f * excited)[0]
    rhs_squared = (vacuum.T * q * vacuum)[0] * (excited.T * q * excited)[0]
    return f * p == zeros(2) and p * f != zeros(2) and lhs == 1 and rhs_squared == 0, (
        "F=|0><1| has F P=0 but P F=F. The proposed two-sided bound gives "
        "|<0,F1>|=1 <= sqrt(<0,Q0><1,Q1>)=0, which is false"
    )


@shell.check(
    "Wilson complete-shell complex contour and Gram budgets are strict exact inequalities",
    CITE + " S9-S15",
)
def _complex_budgets():
    activity = Rational(1, 2500)
    error = activity / (2 * (Rational(1, 5) - activity))
    gap = Rational(1024, 15625)
    projection = error / (gap / 2 - error)
    gram = Rational(1, 9) * Rational(9, 8) ** 2 + 2 * Rational(1, 8) + Rational(1, 8) ** 2
    cmin = Rational(4, 5) ** 5
    return (
        error == Rational(1, 998)
        and 20 * error < gap
        and projection < Rational(1, 9)
        and gram == Rational(13, 32)
        and gram < Rational(1, 2)
        and cmin - gap / 2 > 0,
        f"error={error}; complex projection defect <= {projection}<1/9; "
        f"Gram defect <= {gram}<1/2; contour left bound={cmin - gap / 2}>0. "
        "These certify arithmetic once the analytic activity and synthesis bounds are supplied",
    )


@shell.check(
    "Wilson disconnected-shell source matrix element excludes an independently rotated spectator",
    CITE + " S2 and support lemma",
)
def _disconnected_shell():
    t, z = symbols("t z", real=True)

    def rotated(value):
        c, s = (1 - value**2) / (1 + value**2), 2 * value / (1 + value**2)
        rotation = Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])
        return rotation * diag(0, 1, 0) * rotation.T

    pa, pb, vacuum = rotated(t), rotated(z), diag(1, 0, 0)
    complete = kronecker_product(pa, vacuum) + kronecker_product(vacuum, pb)
    mark_a = kronecker_product(Matrix([0, 1, 0]), Matrix([1, 0, 0]))
    mark_b = kronecker_product(Matrix([1, 0, 0]), Matrix([0, 1, 0]))
    diagonal = simplify((mark_a.T * complete * mark_a)[0])
    cross = simplify((mark_a.T * complete * mark_b)[0])
    return diagonal == (t**2 - 1) ** 2 / (
        t**2 + 1
    ) ** 2 and z not in diagonal.free_symbols and cross == 0, (
        "Complete rank-two single-excitation shell on two three-level factors: "
        f"marked diagonal={diagonal}, cross={cross}; every spectator-parameter coefficient vanishes"
    )


@shell.check(
    "Wilson Taylor range counting has a certified exponential envelope at every order",
    CITE + " S17",
)
def _range_envelope():
    n = symbols("n", integer=True, nonnegative=True)
    # Independent polynomial expansion checks the induction inequality n>=4.
    difference = (2 * (n + 4) ** 3 - (n + 5) ** 3).expand()
    coefficients = [difference.coeff(n, j) for j in range(4)]
    bases = [S(k) ** 3 <= 4 * S(2) ** k for k in range(5)]
    return all(bases) and all(c >= 0 for c in coefficients) and 3 * 25**3 * 4 == 187500, (
        f"2(n+4)^3-(n+5)^3={difference}, coefficients={coefficients}; "
        "base orders 0..4 pass, so n^3<=4*2^n at every natural order. "
        "3(24n+1)^3<=187500*2^n for n>=1; spatial support is an analytic input"
    )


@shell.check(
    "Wilson holomorphic source Gram uses adjoint reflection rather than conjugating the variable",
    CITE + " S11-S14",
)
def _adjoint_reflection():
    z = symbols("z")
    j = Matrix([[1, z], [0, 1], [z, 0]])
    sharp = j.applyfunc(lambda entry: entry.conjugate().subs(z.conjugate(), z)).T
    gram = sharp * j
    wrong = j.H * j
    return gram == Matrix([[1 + z**2, z], [z, 1 + z**2]]) and wrong != gram, (
        f"Real-coefficient analytic source: J# J={gram.tolist()} is polynomial in z; "
        "J(z)* J(z) contains conjugate(z). This checks the continuation convention, "
        "not a Wilson model"
    )


@shell.check(
    "Wilson matching after removal of its equal constant and linear terms "
    "has an exact shifted tail",
    CITE + " S18-S20",
)
def _shifted_matching():
    u, radius, bound = symbols("u radius bound", positive=True)
    order = symbols("order", integer=True, nonnegative=True)
    direct = 2 * bound * (u / radius) ** (order + 3) / ((1 - u / radius) * u**2)
    shifted = 2 * bound / radius**2 * (u / radius) ** (order + 1) / (1 - u / radius)
    t, gamma, xi = symbols("t gamma xi", real=True)
    budget = (t / 2 - 2 * gamma * xi).subs(xi, t / (8 * gamma))
    return simplify(direct - shifted) == 0 and simplify(budget - t / 4) == 0, (
        "Dividing the degree-(M+3) remainder by u^2 gives "
        "(2B/R^2)(u/R)^(M+1)/(1-u/R); xi=t/(8 gamma) leaves coefficient t/4. "
        "The two equal Taylor coefficients and common analytic radius are required inputs"
    )
