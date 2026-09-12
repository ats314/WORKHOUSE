"""Exact controls for recovered archive derivations, with their narrow scopes."""

from __future__ import annotations

import contextlib
import io
import runpy
from fractions import Fraction
from functools import cache
from itertools import permutations
from pathlib import Path

import sympy as sp

from ._core import _suite

recovery = _suite("Earlier proof recovery: exact controls")
SOURCE = "EARLIER_PROOF_RECOVERY"
ROOT = Path(__file__).resolve().parents[3]
SOURCES = ROOT / "runs" / "earlier_proof_recovery_2026-09-11" / "sources"


@cache
def _archived_module(name):
    """Load the retained, source-pinned exact instrument without its main block."""
    return runpy.run_path(str(SOURCES / name))


@recovery.check("archived singular geometry has all sixteen exact gates", f"{SOURCE} E1-E4")
def _():
    module = _archived_module("ENGINE_FLUX_singular_geometry_derivations.py")
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        module["main"]()
    lines = stream.getvalue().splitlines()
    return len(lines) == 17 and lines[-1] == "PASS 16/16 exact gates", (
        "Replayed the original exact ray, radial, incidence, derivative and endpoint algebra. "
        "The regularity, frame and analytic asymptotic proofs remain separate."
    )


@recovery.check(
    "frame ray limits differ and rank volume endpoint needs L at least three", f"{SOURCE} E3-E4"
)
def _():
    j = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    p1, p2 = j * sp.diag(1, 0, 0) * j.T, j * sp.diag(0, 1, 0) * j.T
    t3 = sp.Rational(5, 612)
    g33 = sp.simplify(4 * 27 * t3 * 9 * sp.sin(sp.pi / 3) ** 2)
    g32 = 4 * 27 * t3 * 4
    return (
        p1 != p2 and g33 == sp.Rational(405, 68) and g32 < g33,
        (
            "Two axis limits of J n n^T J^T differ. G(3,3)=405/68; G(3,2)=60/17 "
            "is smaller, retaining the theorem's N,L>=3 domain."
        ),
        {"RECOVERED_RANK_VOLUME_ENDPOINT": sp.Rational(405, 68)},
    )


@recovery.check("Gram null decoupling preserves the physical operator", f"{SOURCE} E5")
def _():
    synthesis = sp.Matrix([[1, 0, 1], [0, 1, 1]])
    gram = synthesis.T * synthesis
    physical = sp.Matrix([[2, 1], [1, 3]])
    overlap = synthesis.T * physical * synthesis
    coordinates = gram.pinv() * overlap
    null = sp.Matrix([-1, -1, 1])
    checks = [
        synthesis * null == sp.zeros(2, 1),
        overlap * null == sp.zeros(3, 1),
        synthesis * coordinates == physical * synthesis,
        synthesis * gram.pinv() * synthesis.T == sp.eye(2),
        synthesis * overlap != physical * synthesis,
    ]
    return all(checks), (
        "Exact nonorthogonal rank-two synthesis verifies null decoupling and G^+B, "
        "and rejects using the raw overlap B as coordinate action. No general history closure."
    )


@recovery.check("Hermitian Ritz residual bounds the nearest exact eigenvalue", f"{SOURCE} E6")
def _():
    matrix = sp.diag(1, 3, 7)
    v = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5), 0])
    lam = (v.T * matrix * v)[0]
    residual = matrix * v - lam * v
    nearest_squared = min((lam - e) ** 2 for e in (1, 3, 7))
    return v.dot(v) == 1 and nearest_squared <= residual.dot(residual), (
        "A rational three-level Hermitian model verifies the squared residual enclosure; "
        "this is not a rerun of the saved B6 numerical campaign or an all-coupling enclosure."
    )


@recovery.check(
    "positive matrix atom controls retain full rank and an empty annulus", f"{SOURCE} E7"
)
def _():
    weight = sp.diag(sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(2, 3))
    tail = sp.eye(3) - weight
    passed = all(x >= 0 for x in tail.diagonal())
    for n in range(4, 33):
        carrier = sp.Rational(2) + sp.Rational(1, n)
        passed = passed and carrier < 3 and 5 - carrier > 1
        passed = passed and all(x >= sp.Rational(1, 3) for x in weight.diagonal())
    return bool(passed), (
        "29 positive three-component finite measures have total I, atom floor I/3, "
        "and a fixed empty annulus. Weak convergence and Portmanteau are analytic, not this test."
    )


@recovery.check("conditional spectral floor accepts noncommuting matrices", f"{SOURCE} E8")
def _():
    a, b = sp.Matrix([[3, 1], [1, 3]]), sp.diag(5, 1)
    average = (a + b) / 2
    return a * b != b * a and min(average.eigenvals()) >= sp.Rational(3, 2), (
        "A and B do not commute; lambda_min((A+B)/2)>=3/2, the average of their "
        "floors. This checks a finite instance, not a coarse-marginal Hessian identification."
    )


def disjoint_staples(length, direction):
    """Return whether the six displayed D=4 star coordinates are exclusive."""
    if length < 3 or direction not in range(4):
        raise ValueError("The nondegenerate periodic D=4 geometry requires L>=3 and 0<=mu<4")

    def point(*shifts):
        coordinates = [0] * 4
        for axis, value in shifts:
            coordinates[axis] += value
        return tuple(value % length for value in coordinates)

    staples, selected = [], []
    for nu in range(4):
        if nu == direction:
            continue
        staples.append({(point((direction, 1)), nu), (point((nu, 1)), direction), (point(), nu)})
        selected.append((point((direction, 1)), nu))
        staples.append(
            {
                (point((direction, 1), (nu, -1)), nu),
                (point((nu, -1)), direction),
                (point((nu, -1)), nu),
            }
        )
        selected.append((point((direction, 1), (nu, -1)), nu))
    return len(set(selected)) == 6 and all(
        link in staples[j] and sum(link in staple for staple in staples) == 1
        for j, link in enumerate(selected)
    )


@recovery.check("all twelve nondegenerate staple incidence controls pass", f"{SOURCE} E9")
def _():
    return all(disjoint_staples(length, mu) for length in (3, 4, 5) for mu in range(4)), (
        "Every selected link belongs to its own incident staple only in twelve exact "
        "periodic cases. This asserts coordinate incidence, not statistical independence."
    )


@recovery.check("positive sector transfer retains Laurent coefficients", f"{SOURCE} E10")
def _():
    z = sp.symbols("z")
    transfer = sp.Matrix([[1 + z, 2], [1 / z, 3]])
    polynomial = sp.Poly(sp.expand(z**3 * sp.trace(transfer**3)), z)
    return all(c >= 0 for c in polynomial.all_coeffs()), (
        "All coefficients of z^3 tr(T(z)^3) are nonnegative exactly. "
        "General gauge-theory positivity and final Fourier cancellation are not supplied."
    )


@recovery.check("VSU action derivatives and both energy asymptotics are exact", f"{SOURCE} E11")
def _():
    x = sp.symbols("x", positive=True)
    energy = x**2 - 2 + 2 * (x + 1) * sp.exp(-x)
    mu = 1 - sp.exp(-x)
    passed = (
        sp.simplify(sp.diff(energy, x) / (2 * x) - mu) == 0
        and sp.simplify(sp.diff(x * mu, x) - mu - x * sp.exp(-x)) == 0
        and sp.limit(energy / x**3, x, 0) == sp.Rational(2, 3)
        and sp.limit(energy / x**2, x, sp.oo) == 1
    )
    return passed, (
        "The constitutive primitive, radial Hessian factor, cubic small-gradient and "
        "quadratic large-gradient limits hold exactly. Bounded-domain existence is analytic."
    )


@recovery.check("determinant reduction retains every row permutation sign", f"{SOURCE} E12")
def _():
    x = sp.symbols("x0:3")
    u = sp.symbols("u0:3")
    w = sp.symbols("w0:3")
    for r, p, q in permutations(range(3)):
        vector = list(w)
        vector[r] = 0
        matrix = sp.Matrix.hstack(sp.Matrix(x), sp.Matrix(u), sp.Matrix(vector))
        expression = x[r] * (u[p] * w[q] - u[q] * w[p]) - u[r] * (x[p] * w[q] - x[q] * w[p])
        order = (r, p, q)
        inversions = sum(order[i] > order[j] for i in range(3) for j in range(i + 1, 3))
        sign = (-1) ** inversions
        if sp.expand(matrix.det() - sign * expression) != 0:
            return False, f"Parity failed at row {r}"
    return (
        True,
        "All six symbolic row permutations pass; the historical middle-row formula needs -1.",
    )


@recovery.check("moving adjoint force retains its own derivative", f"{SOURCE} E13")
def _():
    t = sp.symbols("t", real=True)
    rotation = sp.Matrix([[sp.cos(t), -sp.sin(t), 0], [sp.sin(t), sp.cos(t), 0], [0, 0, 1]])
    force = sp.Matrix([sp.cos(t), sp.sin(t), 1])
    omitted = sp.diff(rotation * force, t) - sp.diff(rotation, t) * force
    return (omitted - rotation * sp.diff(force, t)).applyfunc(sp.simplify) == sp.zeros(
        3, 1
    ) and omitted.subs(t, 0) == sp.Matrix([0, 1, 0]), (
        "The missing Ad_g dX term is nonzero in an exact rotating force example. "
        "This repairs the differentiation rule, not the archive's subsequent rank/tube theorem."
    )


@recovery.check("same coupling score covariance is a positive pair sum", f"{SOURCE} E14")
def _():
    a = sp.symbols("a0:3", positive=True)
    c = sp.symbols("c0:3", positive=True)
    cp = sp.symbols("d0:3", real=True)
    z = sum(a[i] * c[i] ** 2 for i in range(3))
    numerator = (
        z * sum(a[i] * cp[i] ** 2 for i in range(3))
        - sum(a[i] * c[i] * cp[i] for i in range(3)) ** 2
    )
    pairs = sum(
        a[i] * a[j] * (c[i] * cp[j] - c[j] * cp[i]) ** 2 for i in range(3) for j in range(i + 1, 3)
    )
    return sp.expand(numerator - pairs) == 0, (
        "The equal-score covariance numerator is an exact positive weighted square sum. "
        "The SU3 sphere character integration and infinite-series limit are analytic."
    )


@recovery.check(
    "SU3 twice wound covariance and crossed Haar coefficient are negative", f"{SOURCE} E15"
)
def _():
    half = sp.Rational(1, 2)
    first = {(1, 0): half, (0, 1): half}
    second = {(2, 0): half, (0, 1): -half, (0, 2): half, (1, 0): -half}
    haar_pairing = sum(value * second.get((q, p), 0) for (p, q), value in first.items())
    n = sp.Integer(3)
    crossed = -1 / (n * (n**2 - 1))
    return (
        haar_pairing == -half
        and haar_pairing / 9 == -sp.Rational(1, 18)
        and crossed == -sp.Rational(1, 24),
        (
            "Character orthogonality gives normalized covariance -1/18 for a twice-wound loop, "
            "and the balanced rank-three crossed Weingarten coefficient is -1/24. "
            "Neither is an elementary-plaquette counterexample."
        ),
        {"SU3_TWICE_WOUND_COVARIANCE": -sp.Rational(1, 18)},
    )


@recovery.check(
    "literal Balaban corner paths have exact fourth order trace defect", f"{SOURCE} E17"
)
def _():
    module = _archived_module("verify_balaban_corner_reflection_exact.py")
    before = module["plaquette_trace"]((9, 9), True)
    after = module["plaquette_trace"]((9, 9), False)
    difference = tuple(
        module["gadd"](a, module["gneg"](b)) for a, b in zip(before, after, strict=True)
    )
    return (
        difference[:4] == (module["ZERO"],) * 4
        and difference[4]
        == (
            Fraction(4, 81),
            Fraction(0),
        ),
        (
            "Replayed exact Q(i) matrix-log/exp arithmetic for SU2 on 12x12, L=3: "
            "degrees 0..3 vanish and epsilon^4=4/81. Distinct gauge-invariant traces "
            "exclude reflection equivariance modulo coarse gauge for this convention."
        ),
        {"BALABAN_CORNER_TRACE_DEFECT": sp.Rational(4, 81)},
    )
