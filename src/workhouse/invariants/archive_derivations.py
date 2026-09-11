"""Exact controls of the archived functional and source-transport derivations.

Analytic manifold, integration and infinite-family claims retain their scope.
"""

from fractions import Fraction
from itertools import product

from sympy import Function, I, Matrix, Rational, cos, diff, exp, simplify, sin, symbols

from ._core import _suite

archive = _suite("Archive functional inequalities and source transport")


@archive.check(
    "Archive square-profile chain rule retains the signed action pairing", "ARCHIVE_FUNCTIONAL F5"
)
def square_chain():
    x, k = symbols("x k", real=True)
    z, action = Function("z")(x), Function("S")(x)
    weight = exp(k * z**2)
    actual = (diff(weight, x, 2) - diff(action, x) * diff(weight, x)) / weight
    expected = (
        k * (2 * z * diff(z, x, 2) + 2 * diff(z, x) ** 2 - 2 * z * diff(action, x) * diff(z, x))
        + 4 * k * k * z * z * diff(z, x) ** 2
    )
    return (
        simplify(actual - expected) == 0,
        "Exact arbitrary-function one-coordinate diffusion identity; product-manifold"
        " summation and overlap estimates are analytic.",
    )


@archive.check(
    "Archive nonnegative Taylor bound gives gradient domination", "ARCHIVE_FUNCTIONAL F2"
)
def taylor_gradient():
    h, g, z = symbols("h g z", positive=True)
    t = g / h
    remainder = simplify(z - t * g + h * t * t / 2)
    return (
        remainder == z - g * g / (2 * h),
        "At t=|grad z|/H, the upper Taylor bound is z-|grad z|^2/(2H); nonnegativity "
        "and a complete geodesic supply the analytic conclusion.",
    )


@archive.check("Archive drift-to-energy remainder is an exact square", "ARCHIVE_FUNCTIONAL F8")
def energy_square():
    a, b, f, h = symbols("a b f h", real=True)
    return (
        simplify(a * a - (2 * f * a * b / h - f * f * b * b / (h * h)) - (a - f * b / h) ** 2) == 0,
        "Pointwise completed-square identity; integration by parts and form-core "
        "hypotheses are not certified by this algebra.",
    )


@archive.check(
    "Archive overlap and defect budgets hold on an actual periodic four-dimensional complex",
    "ARCHIVE_FUNCTIONAL F3 F4 F5 F10 F14 F15",
)
def center_lattice():
    n = 3
    sites = list(product(range(n), repeat=4))

    def shift(x, d):
        return tuple((v + 1) % n if j == d else v for j, v in enumerate(x))

    plaquettes = []
    for x in sites:
        for i in range(4):
            for j in range(i + 1, 4):
                plaquettes.append({(x, i), (shift(x, i), j), (shift(x, j), i), (x, j)})
    incidence = {}
    for p, edges in enumerate(plaquettes):
        for edge in edges:
            incidence.setdefault(edge, []).append(p)
    bad = set(incidence[((0, 0, 0, 0), 0)])
    z = [2 if p in bad else 0 for p in range(len(plaquettes))]
    adjacent = {
        tuple(sorted((a, b))) for ps in incidence.values() for a in ps for b in ps if a != b
    }
    energy = sum((z[a] - z[b]) ** 2 for a, b in adjacent)
    ok = (
        len(plaquettes) == 486
        and all(len(v) == 6 for v in incidence.values())
        and len(bad) == 6
        and sum(z) == 12
        and energy > 0
    )
    return (
        ok,
        f"Actual L=3 four-dimensional incidence: P={len(plaquettes)}, six plaquettes "
        f"per link, D={sum(z)}, average={Fraction(sum(z), len(z))}, graph Dirichlet "
        f"energy={energy}>0 while center trace gradients vanish. This checks one "
        f"finite lattice; all-volume arguments are analytic.",
        {"ARCHIVE_CENTER_L3_DIRICHLET": energy},
    )


@archive.check(
    "Archive covariance decomposition is exact for a two-event mixture", "ARCHIVE_FUNCTIONAL F12"
)
def covariance_split():
    p, f0, f1, g0, g1, c0, c1 = symbols("p f0 f1 g0 g1 c0 c1")
    actual = (
        p * (c0 + f0 * g0)
        + (1 - p) * (c1 + f1 * g1)
        - (p * f0 + (1 - p) * f1) * (p * g0 + (1 - p) * g1)
    )
    expected = p * c0 + (1 - p) * c1 + p * (1 - p) * (f0 - f1) * (g0 - g1)
    return (
        simplify(actual - expected) == 0,
        "Exact conditional moment identity for arbitrary symbolic probability, means "
        "and covariances; bounded-error inequalities are analytic.",
    )


@archive.check(
    "Archive mean threshold is independent of concentration around the mean",
    "ARCHIVE_FUNCTIONAL F11",
)
def mean_threshold():
    # A deterministic badness has perfect centered concentration but can lie outside K.
    h, threshold = Rational(3, 2), Rational(1, 2)
    return (
        h - h == 0 and h > threshold,
        "A deterministic badness H=3/2 has zero centered fluctuations yet P(H>1/2)=1."
        " Centered concentration alone cannot imply good-set typicality.",
    )


@archive.check(
    "Archive Chernoff optimization has the stated Herbst exponent", "ARCHIVE_FUNCTIONAL F11"
)
def chernoff():
    rho, d, ell = symbols("rho d ell", positive=True)
    t = rho * d / ell**2
    return (
        simplify(-t * d + t * t * ell**2 / (2 * rho)) == -rho * d * d / (2 * ell**2),
        "Exact optimization arithmetic under an assumed logarithmic moment bound; "
        "this does not prove Wilson LSI.",
    )


@archive.check(
    "Archive normalized envelope tilts violate the claimed ordering", "ARCHIVE_SOURCE_TRANSPORT S3"
)
def tilt_order():
    q, s = Rational(1, 100), 100
    actual = q * (1 + s) / (1 + s * q)
    envelope = q * (1 + s) / (1 + s * (q + Rational(1, 2)))
    return (
        actual == Rational(101, 200) and envelope == Rational(101, 5200) and actual > envelope,
        f"Actual tilt={actual}, envelope tilt={envelope}, despite pointwise source domination.",
        {"ARCHIVE_TILT_ACTUAL": actual, "ARCHIVE_TILT_ENVELOPE": envelope},
    )


@archive.check(
    "Archive source log-partition Hessian equals a finite tilted covariance",
    "ARCHIVE_SOURCE_TRANSPORT S1 S2",
)
def source_hessian():
    t, u = symbols("t u", real=True)
    weights = [Rational(1, 5), Rational(3, 10), Rational(1, 2)]
    values = [(0, 1), (2, -1), (3, 2)]
    terms = [w * exp(t * a + u * b) for w, (a, b) in zip(weights, values, strict=True)]
    z = sum(terms)
    first = sum(term * a for term, (a, _) in zip(terms, values, strict=True))
    second = sum(term * b for term, (_, b) in zip(terms, values, strict=True))
    mixed = sum(term * a * b for term, (a, b) in zip(terms, values, strict=True))
    actual = (diff(z, t, u) * z - diff(z, t) * diff(z, u)) / z**2
    expected = mixed / z - first * second / z**2
    return (
        simplify(actual - expected) == 0,
        "Three-state non-product tilted law: mixed log-partition derivative is "
        "covariance for all real t,u; general bounded-measure differentiation remains"
        " analytic.",
    )


@archive.check(
    "Archive likelihood-ratio transfer bounds normalized event probabilities",
    "ARCHIVE_SOURCE_TRANSPORT S4",
)
def likelihood_transfer():
    p = [Rational(1, 5), Rational(3, 10), Rational(1, 2)]
    v = [1, 2, 3]
    w = [2, 1, 6]
    ratios = [Rational(a, b) for a, b in zip(w, v, strict=True)]
    a, b = min(ratios), max(ratios)
    zv = sum(pi * vi for pi, vi in zip(p, v, strict=True))
    zw = sum(pi * wi for pi, wi in zip(p, w, strict=True))
    ok = True
    for mask in product((0, 1), repeat=3):
        pv = sum(pi * vi * x for pi, vi, x in zip(p, v, mask, strict=True)) / zv
        pw = sum(pi * wi * x for pi, wi, x in zip(p, w, mask, strict=True)) / zw
        ok = ok and a * pv / b <= pw <= b * pv / a
    return (
        ok,
        "All eight events in a nonuniform three-state measure satisfy the normalized "
        "likelihood-ratio bound; no general LCI premise inferred.",
    )


@archive.check(
    "Archive rooted series retains the animal-count factor", "ARCHIVE_SOURCE_TRANSPORT S5 S6"
)
def rooted_series():
    q, mu = Rational(1, 1000), 400
    bound = q / (1 - mu * q)
    partial = sum(mu ** (n - 1) * q**n for n in range(1, 21))
    return (
        bound == Rational(1, 600)
        and partial < bound
        and simplify(bound - partial - q * (mu * q) ** 20 / (1 - mu * q)) == 0,
        "With the proved conservative count mu=400 and q=1/1000, the series equals "
        "1/600; the 20-term tail is exact. No Wilson free-energy estimate supplied.",
    )


@archive.check(
    "Archive reflection-equivariant map has a negative coarse OS form",
    "ARCHIVE_SOURCE_TRANSPORT S7 S9",
)
def reflection_counterexample():
    outcomes = list(product((-1, 1), repeat=2))

    def pi(x, y):
        return (x - y, y - x)

    commutes = all(pi(y, x) == tuple(reversed(pi(x, y))) for x, y in outcomes)
    os = sum(Rational(pi(x, y)[0] * pi(x, y)[1], 4) for x, y in outcomes)
    return (
        commutes and os == -2,
        "Four-point RP product law; the map commutes with reflection but its first "
        "coordinate has OS form -2. It fails positive-time pullback.",
        {"ARCHIVE_RP_EQUIVARIANCE_WITNESS": os},
    )


@archive.check(
    "Archive support-preserving pushforward has an exact positive OS Gram matrix",
    "ARCHIVE_SOURCE_TRANSPORT S7 S8",
)
def reflection_positive():
    outcomes = list(product((-1, 1), repeat=4))
    # Two independent positive variables and their reflected negative variables.
    functions = [lambda a, b: 1, lambda a, b: a + 2 * b, lambda a, b: a * b]
    gram = Matrix(
        3,
        3,
        lambda i, j: sum(
            Rational(functions[i](x[2], x[3]) * functions[j](x[0], x[1]), 16) for x in outcomes
        ),
    )
    means = Matrix(
        [sum(Rational(f(a, b), 4) for a, b in product((-1, 1), repeat=2)) for f in functions]
    )
    return (
        gram == means * means.T and gram == Matrix.diag(1, 0, 0),
        "Exact three-observable OS Gram matrix of an actual positive-side block map; "
        "arbitrary projective systems remain an analytic theorem.",
    )


@archive.check(
    "Archive finite-range inverse bound holds on a nontrivial exact tridiagonal family",
    "ARCHIVE_SOURCE_TRANSPORT S10 S11 S12",
)
def finite_range_inverse():
    for n in range(3, 10):
        # I plus the path graph Laplacian, gap a0=1, row bound B=2.
        incidence = Matrix(n - 1, n, lambda i, j: 1 if j == i else -1 if j == i + 1 else 0)
        a = Matrix.eye(n) + incidence.T * incidence
        inverse = a.inv()
        for i, j in product(range(n), repeat=2):
            if abs(inverse[i, j]) > 2 * Rational(4, 5) ** abs(i - j):
                return False, f"Failed exact bound at n={n}, pair={(i, j)}"
    return (
        True,
        "Seven exact path Laplacian inverses satisfy the Combes-Thomas bound with "
        "exp(-eta)=4/5; the all-graph Schur/Neumann proof is analytic.",
    )


@archive.check(
    "Archive horizontal inverse zero-extension is nonlocal on exact cycles",
    "ARCHIVE_SOURCE_TRANSPORT S13 S14",
)
def projected_cycle():
    for n in (4, 6, 8, 10, 12):
        d0 = Matrix(n, n, lambda i, j, size=n: -1 if j == i else 1 if j == (i + 1) % size else 0)
        h = Matrix.ones(n, 1)
        projection = h * h.T / n
        if (
            d0.T * h != Matrix.zeros(n, 1)
            or projection * projection != projection
            or projection[0, n // 2] != Rational(1, n)
        ):
            return False, f"Failed cycle construction n={n}"
    n = 20
    return (
        Rational(1, n) > 2 * Rational(1, 2) ** (n // 2),
        "Actual cyclic incidence has constant horizontal space and ambient inverse "
        "projection 11^T/n. At n=20, entry 1/20 exceeds 2*(1/2)^10; exponential "
        "uniformity fails analytically as n grows.",
    )


@archive.check(
    "Archive reported full-rank fit and held-out fit are different formulas",
    "ARCHIVE_REVIEW_SOURCES numerical provenance",
)
def separate_fits():
    full = Rational("5.759") + Rational("2.91") / 9
    held = Rational("5.7408") + Rational("3.691") / 9
    return (
        full == Rational(18247, 3000)
        and held != full
        and abs(held - Rational("6.151")) < Rational(1, 10000),
        f"Displayed full-rank fit at N=3 is {full}; held-out fit is {held}. Arithmetic"
        f" only; both use lattice measurements.",
    )


@archive.check(
    "Archive even tori realize extensive stationary center defects", "ARCHIVE_FUNCTIONAL F16"
)
def extensive_center_lattice():
    observations = []
    for n in (2, 4, 6):

        def link(x, mu):
            return (-1) ** sum(x[:mu])

        def shift(x, mu, size=n):
            return tuple((v + 1) % size if j == mu else v for j, v in enumerate(x))

        signs = [
            link(x, mu) * link(shift(x, mu), nu) * link(shift(x, nu), mu) * link(x, nu)
            for x in product(range(n), repeat=4)
            for mu in range(4)
            for nu in range(mu + 1, 4)
        ]
        if len(signs) != 6 * n**4 or any(s != -1 for s in signs):
            return False, f"Center plaquette construction failed at L={n}."
        observations.append((n, len(signs), sum(1 - s for s in signs)))
    generators = [Matrix([[0, 1], [-1, 0]]), Matrix([[0, I], [I, 0]]), Matrix([[I, 0], [0, -I]])]
    traceless = all(g.trace() == 0 for g in generators)
    return (
        traceless,
        f"Exact sign plaquettes on L=2,4,6 tori give (L,P,D)={observations}; "
        "traceless su(2) generators give zero first variations at center fields. "
        "The all-even-L construction and volume-uniform obstruction are analytic.",
    )


@archive.check(
    "Archive SU2 signed diffusion is exact in quaternion generator coordinates",
    "ARCHIVE_FUNCTIONAL F17",
)
def signed_su2_diffusion():
    t, a1, a2, a3, s, z = symbols("t a1 a2 a3 s z", real=True)
    paths = [1 - t * cos(s) + a * sin(s) for a in (a1, a2, a3)]
    group_laplacian = sum(diff(p**2, s, 2).subs(s, 0) for p in paths)
    plaquette_laplacian = 4 * group_laplacian.subs(a3**2, 1 - t**2 - a1**2 - a2**2)
    actual = simplify(plaquette_laplacian.subs(t, 1 - z))
    first_square = sum(diff(p, s).subs(s, 0) ** 2 for p in paths)
    gradient = simplify(4 * first_square.subs(a3**2, 1 - t**2 - a1**2 - a2**2).subs(t, 1 - z))
    return (
        simplify(actual - (40 * z - 32 * z**2)) == 0
        and simplify(gradient - 4 * z * (2 - z)) == 0
        and actual.subs(z, 2) == -48
        and actual.subs(z, 0) == 0,
        "Exact three-generator unit-quaternion paths and four distinct link lifts "
        "give Delta(z_p^2)=40z_p-32z_p^2 and Gamma(z_p)=4z_p(2-z_p). "
        "The manifold identification, overlap inequality and all-volume sum are analytic.",
        {"ARCHIVE_CENTER_SIGNED_DRIFT_PER_PLAQUETTE": -48},
    )
