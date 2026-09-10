"""Exact finite controls for the spatial Schur-excess analytic theorem.

These certify matrix/form interfaces and actual finite Wilson jets, not the
uniform interacting hypotheses or existence of a continuum measure.
"""

from __future__ import annotations

from math import factorial

from sympy import I, Matrix, Rational, cos, diff, expand, eye, simplify, sin, symbols, zeros

from ._core import _suite

spatial = _suite("Wilson spatial passage: complete Schur excess and scale budgets")
CITE = "WILSON_SPATIAL; G19"


def _zero(matrix):
    return all(simplify(entry) == 0 for entry in matrix)


def _blocks(h):
    return h[:2, :2], h[:2, 2:], h[2:, 2:]


def _example():
    h0 = Matrix([[7, 1, 1, 2], [1, 6, 2, -1], [1, 2, 4, 1], [2, -1, 1, 6]])
    w1 = Matrix([[1, 2, 0, 1], [2, -1, 1, 2], [0, 1, 2, -1], [1, 2, -1, 1]])
    w2 = Matrix([[2, -1, 1, 0], [-1, 3, 2, 1], [1, 2, -1, 2], [0, 1, 2, 1]])
    return h0, w1, w2


@spatial.check("Spatial Schur excess is exact with noncommuting fast blocks", CITE + " SP1-SP5")
def _exact_excess():
    h0, w1, w2 = _example()
    a0, b0, f0 = _blocks(h0)
    w3 = Matrix([[1, 0, 1, -1], [0, 1, 0, 2], [1, 0, 0, 1], [-1, 2, 1, -1]])
    good = True
    for g in (Rational(1, 5), -Rational(1, 7)):
        d = g * w1 + g**2 * w2 + g**3 * w3
        a, b, f = _blocks(h0 + d)
        for z in (Rational(0), Rational(1, 3)):
            inverse = (f0 - z * eye(2)).inv()
            j = eye(2).col_join(-inverse * b0.T)
            residual = (d * j)[2:, :]
            actual = a - b * (f - z * eye(2)).inv() * b.T - a0 + b0 * inverse * b0.T
            predicted = j.T * d * j - residual.T * (f - z * eye(2)).inv() * residual
            fast = f - z * eye(2)
            good &= _zero(actual - predicted) and fast[0, 0] > 0 and fast.det() > 0
    return good and f0 * w1[2:, 2:] != w1[2:, 2:] * f0, (
        "Two retained and two fast directions, nonzero reference cross coupling, "
        "two signed couplings and two energies; exact full rational inverses agree"
    )


@spatial.check(
    "Spatial second jet includes every baseline and fast-variation cross term", CITE + " SP7-SP10"
)
def _second_jet():
    h0, w1, w2 = _example()
    a0, b0, f0 = _blocks(h0)
    a1, b1, f1 = _blocks(w1)
    a2, b2, f2 = _blocks(w2)
    z = Rational(2, 5)
    r0 = (f0 - z * eye(2)).inv()
    # Independent coefficient extraction by ordered convolution of three jets.
    inverse = (r0, -r0 * f1 * r0, r0 * f1 * r0 * f1 * r0 - r0 * f2 * r0)
    bs = (b0, b1, b2)
    direct = []
    for n, an in enumerate((a0 - z * eye(2), a1, a2)):
        convolution = zeros(2)
        for i in range(n + 1):
            for j in range(n - i + 1):
                convolution += bs[i] * inverse[j] * bs[n - i - j].T
        direct.append(an - convolution)
    lift = eye(2).col_join(-r0 * b0.T)
    force = (w1 * lift)[2:, :]
    assembled = lift.T * w2 * lift - force.T * r0 * force
    naive = a2 - b1 * r0 * b1.T
    return (
        _zero(direct[1] - lift.T * w1 * lift)
        and _zero(direct[2] - assembled)
        and not _zero(direct[2] - naive)
        and not _zero(force - b1.T),
        "Direct three-factor inverse-series convolution matches the full graph coefficient; "
        "a2-b1(F0-z)^-1 b1* fails, as does the undressed cubic force",
    )


@spatial.check(
    "Spatial energy derivative retains the full induced graph metric",
    CITE + " SP6; WILSON_SPATIAL_SCHUR_INPUT sections 1 and 5",
)
def _induced_metric():
    z = symbols("z", real=True)
    a, b, f = 5, 2, 3
    schur = a - z - b**2 / (f - z)
    metric = 1 + b**2 / (f - z) ** 2
    return simplify(-diff(schur, z) - metric) == 0 and metric.subs(z, 0) == Rational(13, 9), (
        "The derivative of the exact energy pencil is -(1+B(F-z)^-2 B*); "
        "discarding memory would falsely give a unit metric"
    )


@spatial.check(
    "Spatial source straightening has both commutators and the nested term", CITE + " SP16"
)
def _unitary_jet():
    h0, h1, h2 = _example()
    k1 = Matrix([[0, 1, 0, 2], [-1, 0, 1, 0], [0, -1, 0, 1], [-2, 0, -1, 0]])
    k2 = Matrix([[0, 0, 1, -1], [0, 0, 2, 1], [-1, -2, 0, 0], [1, -1, 0, 0]])
    u = (eye(4), k1, k2 + k1 * k1 / 2)
    h = (h0, h1, h2)
    coefficients = []
    for n in (1, 2):
        c = zeros(4)
        for i in range(n + 1):
            for j in range(n - i + 1):
                c += u[i].T * h[j] * u[n - i - j]
        coefficients.append(c)

    def comm(a, b):
        return a * b - b * a

    expected = h2 + comm(h1, k1) + comm(h0, k2) + comm(comm(h0, k1), k1) / 2
    return (
        _zero(coefficients[0] - h1 - comm(h0, k1))
        and _zero(coefficients[1] - expected)
        and _zero(u[2] + u[2].T + u[1].T * u[1])
        and not _zero(comm(comm(h0, k1), k1)),
        "Independent coefficient multiplication of U*HU with a noncommuting, "
        "second-order unitary jet verifies the source terms and their signs",
    )


@spatial.check(
    "Actual SU2 harmonic commutator has nonzero quartic Wilson energy", CITE + " SP12-SP13 SP19"
)
def _harmonic_quartic():
    x, y = symbols("x y", real=True)
    t1 = Matrix([[0, -I / 2], [-I / 2, 0]])
    t2 = Matrix([[0, -Rational(1, 2)], [Rational(1, 2), 0]])
    word = (x * t1, y * t2, -x * t1, -y * t2)
    jet = [eye(2)] + [zeros(2) for _ in range(4)]
    for vertex in word:
        old = jet
        jet = [
            sum((old[n - k] * vertex**k / factorial(k) for k in range(n + 1)), zeros(2))
            for n in range(5)
        ]
    quartic = simplify(-2 * jet[4].trace())
    return (
        _zero(jet[1])
        and simplify(jet[2].trace()) == 0
        and simplify(jet[3].trace()) == 0
        and quartic == x**2 * y**2 / 2,
        "The actual ordered four-link SU2 word has zero linear curl yet "
        "2 g^-2 v = (g^2/2)x^2 y^2 + higher orders; harmonic coordinates remain interacting",
    )


@spatial.check(
    "Actual nonzero-curl Wilson quartic retains all three logarithmic terms", CITE + " SP12-SP13"
)
def _full_quartic():
    t1 = Matrix([[0, -I / 2], [-I / 2, 0]])
    t2 = Matrix([[0, -Rational(1, 2)], [Rational(1, 2), 0]])
    t3 = Matrix([[-I / 2, 0], [0, I / 2]])
    word = (t1, 2 * t2, t3 + t1)
    jet = [eye(2)] + [zeros(2) for _ in range(4)]
    for vertex in word:
        old = jet
        jet = [
            sum((old[n - k] * vertex**k / factorial(k) for k in range(n + 1)), zeros(2))
            for n in range(5)
        ]
    f1 = jet[1]
    f2 = jet[2] - f1**2 / 2
    f3 = jet[3] - (f1 * jet[2] + jet[2] * f1) / 2 + f1**3 / 3
    terms = (-(f2**2).trace(), -2 * (f1 * f3).trace(), -(f1**4).trace() / 12)
    direct = simplify(-2 * jet[4].trace())
    return all(simplify(t) != 0 for t in terms) and simplify(sum(terms) - direct) == 0, (
        f"An actual three-loop SU2 word gives quartic terms {tuple(map(simplify, terms))}; "
        f"their sum {direct} agrees with direct exponential-word multiplication"
    )


@spatial.check(
    "Actual SU2 radial Haar flattening retains its electric second-order scalar", CITE + " SP14"
)
def _haar_electric():
    r = symbols("r", positive=True)
    root_j = sin(r / 2) / (r / 2)
    good = True
    for psi in (r**2, 1 + r**4, r**6 - r**2):
        raw = psi / root_j
        flat = -root_j * (diff(raw, r, 2) + cos(r / 2) / sin(r / 2) * diff(raw, r)) / 2
        euclidean = -(diff(psi, r, 2) + 2 * diff(psi, r) / r) / 2
        good &= simplify(flat - euclidean + psi / 8) == 0
    return good, (
        "On SU2 class functions the exact flattened radial electric operator is "
        "-1/2(d_r^2+2/r d_r)-1/8, yielding -g^2/8 after dilation; metric and Haar are combined"
    )


@spatial.check(
    "Actual averaged-path polar source has the complete second correction",
    CITE + " SP17a; WILSON_SPATIAL_FLAT_INPUT section 4, actual redundant observation geometry",
)
def _polar_source_jet():
    t1 = Matrix([[0, -I / 2], [-I / 2, 0]])
    t2 = Matrix([[0, -Rational(1, 2)], [Rational(1, 2), 0]])
    t3 = Matrix([[-I / 2, 0], [0, I / 2]])

    def word_jet(word):
        jet = [eye(2)] + [zeros(2) for _ in range(3)]
        for vertex in word:
            old = jet
            jet = [
                sum((old[n - k] * vertex**k / factorial(k) for k in range(n + 1)), zeros(2))
                for n in range(4)
            ]
        return jet

    first = word_jet((t1, 2 * t2, t3))
    second = word_jet((-t2, t1 + t3))
    m = [first[n] / 3 + 2 * second[n] / 3 for n in range(4)]
    gram = [sum((m[k].H * m[n - k] for k in range(n + 1)), zeros(2)) for n in range(4)]
    inverse_root = (eye(2), zeros(2), -gram[2] / 2, -gram[3] / 2)
    polar = [sum((m[k] * inverse_root[n - k] for k in range(n + 1)), zeros(2)) for n in range(4)]
    log2 = polar[2] - polar[1] ** 2 / 2
    log3 = polar[3] - (polar[1] * polar[2] + polar[2] * polar[1]) / 2 + polar[1] ** 3 / 3
    a, b, c = m[1:]
    y1 = (b - b.H) / 2
    y2 = (c - c.H) / 2 - (a * (b + b.H) + (b + b.H) * a) / 4 + a**3 / 3
    return (
        _zero(gram[1])
        and _zero(log2 - y1)
        and _zero(log3 - y2)
        and _zero(y2 + y2.H)
        and simplify(y2.trace()) == 0
        and not _zero(y2),
        "Two noncommuting actual SU2 path words with weights 1/3 and 2/3: "
        "direct polar/log series reproduce the nonzero second source correction",
    )


@spatial.check(
    "Spatial normalized moving-source density has the complete second jet", CITE + " SP15 SP17-SP18"
)
def _source_density():
    x, g = symbols("x g", real=True)

    def moment(poly):
        poly = expand(poly)
        answer = 0
        for (degree,), coefficient in poly.as_poly(x).terms():
            if degree % 2 == 0:
                answer += coefficient * Rational(
                    factorial(degree), 4 ** (degree // 2) * factorial(degree // 2)
                )
        return simplify(answer)

    def weighted_derivative(poly):
        return diff(poly, x) - 2 * x * poly

    r1, r2, y1, y2 = 2 * x, x**2 - Rational(1, 2), x**2, x**3
    d1 = r1 - weighted_derivative(y1)
    d2 = expand(
        r2 - weighted_derivative(y2 + r1 * y1) + weighted_derivative(weighted_derivative(y1**2)) / 2
    )
    good = moment(d1) == moment(d2) == 0
    for degree in range(5):
        phi = x**degree
        direct1 = moment(phi * r1 + diff(phi, x) * y1)
        direct2 = moment(phi * r2 + diff(phi, x) * (y2 + r1 * y1) + diff(phi, x, 2) * y1**2 / 2)
        good &= direct1 == moment(phi * d1) and direct2 == moment(phi * d2)
    omitted_cross = d2 + weighted_derivative(r1 * y1)
    return good and moment(x**2 * omitted_cross) != moment(x**2 * d2), (
        f"Five exact Gaussian test moments agree with normalized pushforward; d1={expand(d1)}, "
        f"d2={d2}. Omitting the ground/source cross term changes the second moment"
    )


@spatial.check(
    "Spatial third-order remainder constant bounds a nonzero exact defect", CITE + " SP8-SP9"
)
def _remainder_budget():
    g0, theta = Rational(1, 4), Rational(1, 4)
    c3 = 1 + (2 + g0 + 1) / (1 - theta)
    good = c3 == Rational(16, 3)
    for g in (Rational(1, 4), -Rational(1, 4), Rational(1, 9), -Rational(1, 11)):
        # A=g+2g^2+g^3, V=g+g^2, C=g meet the stated unit constants.
        actual = g + 2 * g**2 + g**3 - (g + g**2) ** 2 / (1 + g)
        polynomial = g + g**2
        good &= abs(actual - polynomial) <= c3 * abs(g) ** 3
    # A variant has a genuinely nonzero cubic remainder.
    g = Rational(1, 4)
    actual = g + 2 * g**2 + g**3 - (g + g**2) ** 2 / (1 - g)
    defect = actual - g - g**2
    return good and 0 < abs(defect) <= c3 * g**3, (
        "Exact positive and negative coupling controls satisfy C3=16/3; "
        "a sign-changed fast-form variation leaves a nonzero bounded cubic defect"
    )


@spatial.check(
    "Spatial gap iteration carries every accumulated comparison loss", CITE + " SP20-SP22"
)
def _scale_budget():
    alphas = (Rational(9, 10), Rational(7, 8), Rational(11, 12), Rational(15, 16))
    floors = (4, 8, 16, 32)
    inverse_gap, initial = Rational(3, 2), Rational(3, 2)
    product, weighted = Rational(1), Rational(0)
    good = True
    for alpha, floor in zip(alphas, floors, strict=True):
        inverse_gap = inverse_gap / alpha + Rational(1, floor)
        product *= alpha
        weighted += product / floor
        good &= inverse_gap == (initial + weighted) / product
    undressed = initial + sum((Rational(1, f) for f in floors), Rational(0))
    return good and inverse_gap > undressed, (
        "Four distinct loss factors and doubling physical fast energies reproduce "
        "the exact weighted reciprocal-gap formula; omitting accumulated losses fails"
    )


@spatial.check(
    "Spatial onto frames alone cannot preserve a specified observable", CITE + " SP23-SP24"
)
def _frame_observable():
    frame = Matrix([[1, 0]])
    invisible = Matrix([0, 1])
    eta, amplitude = (Rational(1, 8), Rational(1, 16), Rational(1, 32)), Rational(1, 2)
    remaining = amplitude - sum(eta)
    return frame * frame.T == eye(1) and frame * invisible == zeros(1, 1) and remaining == Rational(
        9, 32
    ), (
        "A frame of lower bound one can annihilate a chosen source; the separate "
        "telescoping amplitude budget leaves 9/32 and spectral weight at least 81/1024"
    )
