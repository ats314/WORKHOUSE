"""Exact magnetic controls for the actual square's antipodal conditional fiber.

The Hessian is that of V in quaternion-angle coordinates, not of the Agmon
phase or of minus the logarithm of the actual quantum ground.
"""

from __future__ import annotations

from functools import cache

import sympy as sp

from ._core import _suite

antipodal = _suite("W6 antipodal conditional magnetic geometry")
CITE = "W6_ANTIPODAL_MAGNETIC_GEOMETRY"
CHART = "W6 antipodal: exact noncommuting fixed-Q chart"
QUADRATIC = "W6 antipodal: original four-face quadratic expansion"
SPECTRUM = "W6 antipodal: complete nine-dimensional Hessian spectrum"
BOUND = "W6 antipodal: seven uniform normal eigenvalues and soft scaling"
KERNEL = "W6 antipodal: gauge tangent equals the two-dimensional kernel"
METRIC = "W6 antipodal: original-edge metric comparison constants"
ANGULAR = "W6 antipodal: exact displaced-orbit angular potential"
C, S = sp.symbols("C S", real=True)


def _mul(q, r):
    """Quaternion product, with positive vector cross product."""
    q, r = sp.Matrix(q), sp.Matrix(r)
    v, w = q[1:4, 0], r[1:4, 0]
    return sp.Matrix([q[0] * r[0] - v.dot(w), *(q[0] * w + r[0] * v + v.cross(w))])


def _conj(q):
    return sp.Matrix([q[0], -q[1], -q[2], -q[3]])


def _circle(expr):
    return sp.rem(sp.expand(expr), S**2 + C**2 - 1, S).expand()


def _zero(value):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    return all(sp.simplify(entry) == 0 for entry in entries)


@antipodal.check(CHART, CITE + " A1")
def fixed_q_chart():
    # Arbitrary unit quaternions: no commuting-axis restriction.
    ea, eb, ec = (sp.Matrix(sp.symbols(f"{name}0:4")) for name in ("u", "v", "w"))
    aa = sp.Matrix([C, 0, 0, S])
    bb = _mul(aa, aa)
    u0 = _mul(aa, ea)
    u1 = _mul(_mul(_conj(aa), eb), bb)
    u2, u3 = _mul(bb, ec), _mul(_conj(ec), bb)
    defect = (_mul(u2, u3) - _mul(bb, bb)).applyfunc(_circle)
    constraint = sum(entry**2 for entry in ec) - 1
    constraint_ok = all(sp.rem(entry, constraint, ec[0]) == 0 for entry in defect)
    original = u0[0] + u1[0] + _mul(u2, _conj(u0))[0] + _mul(u3, _conj(u1))[0]
    reduced = (
        _mul(aa, ea)[0]
        + _mul(_mul(aa, ec), _conj(ea))[0]
        + _mul(aa, eb)[0]
        + _mul(_mul(aa, _conj(ec)), _conj(eb))[0]
    )
    return constraint_ok and _circle(original - reduced) == 0, (
        "Direct quaternion products give U2 U3=A^4 and the exact four scalar "
        "terms of A1, modulo |A|=|Ec|=1; arbitrary noncommuting axes are retained."
    )


@cache
def _quadratic_data():
    t = sp.Symbol("t", real=True)
    a, b, c = (sp.Matrix(sp.symbols(f"{name}1:4", real=True)) for name in ("a", "b", "c"))

    def jet(v):
        return sp.Matrix([1 - t**2 * v.dot(v) / 2, *(t * v)])

    def product(*factors):
        value = sp.Matrix([1, 0, 0, 0])
        for factor in factors:
            value = _mul(value, factor).applyfunc(
                lambda expr: _circle(sum(sp.expand(expr).coeff(t, j) * t**j for j in range(3)))
            )
        return value

    aa = sp.Matrix([C, 0, 0, S])
    bb = product(aa, aa)
    u0 = product(aa, jet(a))
    u1 = product(_conj(aa), jet(b), bb)
    u2, u3 = product(bb, jet(c)), product(jet(-c), bb)
    potential = sp.expand(
        16 - 4 * (u0[0] + u1[0] + product(u2, _conj(u0))[0] + product(u3, _conj(u1))[0])
    )
    quadratic = potential.coeff(t, 2)
    return a, b, c, potential, quadratic, sp.hessian(quadratic, [*a, *b, *c]), t


@antipodal.check(QUADRATIC, CITE + " A2")
def original_quadratic():
    a, b, c, potential, quadratic, _, t = _quadratic_data()
    expected = 2 * C * (a.dot(a) + (c - a).dot(c - a) + b.dot(b) + (c + b).dot(c + b))
    expected -= 4 * S * c.cross(a - b)[2]
    return (
        _zero(potential.coeff(t, 0) - (16 - 16 * C))
        and potential.coeff(t, 1) == 0
        and _zero(quadratic - expected),
        "Original face words give 2C(|a|^2+|c-a|^2+|b|^2+|c+b|^2)"
        "-4S n.(c cross (a-b)), with zero linear term; n=e3 by rotation covariance.",
    )


@antipodal.check(SPECTRUM, CITE + " A3", rests_on=(QUADRATIC,))
def full_spectrum():
    hessian = _quadratic_data()[5]
    lam, root2 = sp.Symbol("lambda"), sp.sqrt(2)
    identity, zero = sp.eye(3), sp.zeros(3)
    transform = sp.BlockMatrix(
        [
            [identity / root2, identity / root2, zero],
            [identity / root2, -identity / root2, zero],
            [zero, zero, identity],
        ]
    ).as_explicit()
    j = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    coupling = C * identity - S * j
    expected_matrix = sp.BlockMatrix(
        [
            [8 * C * identity, zero, zero],
            [zero, 8 * C * identity, -4 * root2 * coupling.T],
            [zero, -4 * root2 * coupling, 8 * C * identity],
        ]
    ).as_explicit()
    expected_charpoly = (lam - 8 * C) ** 3 * ((lam - 8 * C) ** 2 - 32 * C**2)
    expected_charpoly *= ((lam - 8 * C) ** 2 - 32) ** 2
    return (
        _zero(transform.T * transform - sp.eye(9))
        and _zero(transform.T * hessian * transform - expected_matrix)
        and _zero((coupling * coupling.T - sp.diag(1, 1, C**2)).applyfunc(_circle))
        and _circle(hessian.charpoly(lam).as_expr() - expected_charpoly) == 0,
        "Characteristic polynomial: (lambda-8C)^3 ((lambda-8C)^2-32C^2) "
        "((lambda-8C)^2-32)^2. Orthogonal p,m,c change and singular values C,1,1 "
        "are checked from the original Hessian.",
    )


@antipodal.check(BOUND, CITE + " A3", rests_on=(SPECTRUM,))
def uniform_bound_and_scaling():
    root2 = sp.sqrt(2)
    lower = 4 * (root2 - 1)
    branches = [8 * C, (8 - 4 * root2) * C, (8 + 4 * root2) * C, 8 * C + 4 * root2]
    positive = all(
        sp.diff(value, C).is_positive is True
        and sp.simplify(value.subs(C, 1 / root2) - lower).is_nonnegative is True
        for value in branches
    )
    delta = sp.Symbol("delta", real=True)
    soft = 8 * sp.cos((sp.pi - delta) / 4) - 4 * root2
    expected = root2 * delta - root2 * delta**2 / 8
    return (
        positive and _zero(sp.series(soft, delta, 0, 3).removeO() - expected),
        "Seven eigenvalues >=4(sqrt(2)-1)>0 on 0<=theta<=pi. The double soft "
        "branch is 8cos(theta/4)-4sqrt(2), with expansion "
        "sqrt(2)delta-sqrt(2)delta^2/8+O(delta^3).",
    )


@antipodal.check(KERNEL, CITE + " A4", rests_on=(QUADRATIC,))
def gauge_kernel():
    root2 = sp.sqrt(2)
    aa, bb = sp.Matrix([1 / root2, 0, 0, 1 / root2]), sp.Matrix([0, 0, 0, 1])
    columns = []
    for v in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])):
        da, db = sp.Matrix([0, *(v / root2)]), sp.Matrix([0, *v])
        # Inverse chart differential along the actual rotating-axis family.
        a = _mul(_conj(aa), da)[1:4, 0]
        b = _mul(_mul(aa, da), _conj(bb))[1:4, 0]
        c = _mul(_conj(bb), db)[1:4, 0]
        columns.append(a.col_join(b).col_join(c))
    tangent = sp.Matrix.hstack(*columns)
    hessian = _quadratic_data()[5].subs({C: 1 / root2, S: 1 / root2})
    return (
        tangent.rank() == 2
        and hessian.rank() == 7
        and _zero(hessian * tangent)
        and _zero(tangent.T * tangent - 2 * sp.eye(2)),
        "Rotating-axis tangents have Gram matrix 2I and lie in the endpoint "
        "Hessian kernel. Its exact rank seven proves they exhaust that kernel; "
        "the global conjugation-orbit identification is supplied analytically.",
    )


@antipodal.check(METRIC, CITE + " A5", rests_on=(BOUND, KERNEL))
def electric_metric_constants():
    q = sp.Matrix(sp.symbols("q0:4", real=True))
    # Original T=i sigma/2 has speed 1/2 in the quaternion-angle metric.
    fields = sp.Matrix.hstack(*[_mul(sp.Matrix([0, *(sp.eye(3)[:, j] / 2)]), q) for j in range(3)])
    frame_gram = fields.T * fields - q.dot(q) * sp.eye(3) / 4
    pullback = sp.diag(*([1] * 6 + [2] * 3))
    normal = 4 * (sp.sqrt(2) - 1)
    return (
        _zero(frame_gram)
        and all(value.is_nonnegative is True for value in (2 * sp.eye(9) - pullback).diagonal())
        and _zero(normal / 8 - (sp.sqrt(2) - 1) / 2),
        "Original independent non-tree generators contribute cometric I/4 on "
        "each factor, hence G<=4G_product. Fixed-Q pullback diag(I,I,2I)<=2I "
        "gives the quotient-distance coefficient (sqrt(2)-1)/2. Inversion and "
        "the distance implication are analytic arguments, not ground-score bounds.",
    )


@antipodal.check(ANGULAR, CITE + " A6")
def displaced_orbit_potential():
    n = sp.Matrix(sp.symbols("n1:4", real=True))
    delta = sp.Symbol("delta", real=True)
    aa = sp.Matrix([1 / sp.sqrt(2), *(n / sp.sqrt(2))])
    bb = sp.Matrix([0, *n])
    coarse = sp.Matrix([-sp.cos(delta), 0, 0, sp.sin(delta)])
    u3 = _mul(_conj(bb), coarse)
    potential = 16 - 4 * (2 * aa[0] + _mul(bb, _conj(aa))[0] + _mul(u3, _conj(aa))[0])
    expected = 16 - 2 * sp.sqrt(2) * (3 + sp.cos(delta) + sp.sin(delta) * n[2])
    defect = sp.rem(sp.expand(potential - expected), n.dot(n) - 1, n[0])
    leading = 16 - 8 * sp.sqrt(2) - 2 * sp.sqrt(2) * delta * n[2]
    return (
        defect == 0 and _zero(sp.series(expected, delta, 0, 2).removeO() - leading),
        "Original potential on the old orbit: 16-2sqrt(2)(3+cos(delta)+sin(delta)n3). "
        "Leading term -2sqrt(2)delta n3; the O(delta^2) normal-relaxation assertion "
        "uses the separate compact implicit-function argument.",
    )
