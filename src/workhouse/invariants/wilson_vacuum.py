"""Exact controls for vacuum-aligned assembly; analytic scopes are in VA1-VA16."""

from itertools import product

from sympy import (
    I,
    Matrix,
    Rational,
    diag,
    diff,
    exp,
    eye,
    factorial,
    pi,
    simplify,
    sqrt,
    symbols,
    zeros,
)

from ._core import _suite

vacuum = _suite("Wilson vacuum assembly: connected-volume falsifier and true-conditional repair")
CITE = "WILSON_VACUUM_ASSEMBLY; G19; G23"
BLOCK_CITE = "WILSON_TRUE_BLOCK; G19; G23"


@vacuum.check(
    "Exact SU2 heat-kernel tail constants yield the volume-independent local ratio",
    CITE + " VA1 VA4",
)
def _heat_constants():
    r = Rational(1, 20)
    tail = (1 + r) / (1 - r) ** 3 - 1
    exp_lower = sum(Rational(3) ** j / factorial(j) for j in range(9))
    return (
        tail == Rational(1541, 6859) < Rational(1, 4)
        and exp_lower == Rational(89641, 4480) > 20
        and (1 + Rational(1, 4)) / (1 - Rational(1, 4)) == Rational(5, 3),
        "Exact character-tail majorant and Taylor lower bound certify 3/4<=p_1<=5/4. "
        "Feynman-Kac positivity and cancellation of the common outside integral in VA1-VA2 "
        "are analytic; the resulting true-ground local amplitude ratio is volume independent",
    )


@vacuum.check(
    "Cubic staple controls use four distinct opposite links and at most sixteen plaquettes",
    CITE + " VA6",
)
def _staple_geometry():
    outcomes = []
    for side in (3, 4, 5):
        vertices = list(product(range(side), repeat=3))

        def shifted(vertex, direction, amount=1, side=side):
            value = list(vertex)
            value[direction] = (value[direction] + amount) % side
            return tuple(value)

        faces = []
        for vertex in vertices:
            for i in range(3):
                for j in range(i + 1, 3):
                    faces.append(
                        frozenset(
                            (
                                (vertex, i),
                                (shifted(vertex, i), j),
                                (shifted(vertex, j), i),
                                (vertex, j),
                            )
                        )
                    )
        edge = ((0, 0, 0), 0)
        touching = [face for face in faces if edge in face]
        opposite = [
            next(link for link in face if link[1] == 0 and link != edge) for face in touching
        ]
        outcomes.append(
            len(touching) == len(set(opposite)) == 4
            and all(sum(link in face for face in touching) == 1 for link in opposite)
            and sum(bool(face.intersection(opposite)) for face in faces) <= 16
        )
    return all(outcomes), (
        "Exact incidence enumeration on periodic side lengths 3,4,5 verifies the four "
        "independently Haar-variable opposite links and touching-plaquette bound. "
        "VA2 states the analytic all-L>=3 geometric argument; these are finite controls"
    )


@vacuum.check(
    "The cancelled-staple region leaves fifteen local gap units in the discarded remainder",
    CITE + " VA5 VA8",
)
def _discarded_budget():
    threshold = sqrt(32) / 2 - 3 / sqrt(2)
    delta_coefficient = 1 / (16 * sqrt(2))
    count, probability, delta = symbols("count probability delta", positive=True)
    excitation_increase = 4 * delta
    discarded_lower = 15 * delta * probability * count
    return (
        simplify(threshold / delta_coefficient) == 16
        and simplify(threshold - delta_coefficient) == 15 * sqrt(2) / 32
        and simplify(excitation_increase - discarded_lower - delta * (4 - 15 * probability * count))
        == 0,
        "At k/epsilon=32 the bad-region lower floor is sixteen delta; subtracting "
        "delta Q retains fifteen delta. The physical local-phase test changes four "
        "bounded projections, yielding delta(4-15 p0 |E|) after true-vacuum subtraction",
    )


@vacuum.check(
    "A conditional one-coordinate projection commutes with every outside phase multiplier",
    CITE + " VA8",
)
def _outside_phase():
    a, b, c, d = symbols("a b c d", positive=True)
    phase = symbols("phase", real=True)
    # Coordinates are (active bit, outside bit). The two conditional ground
    # vectors can differ with the outside bit; no product-state assumption.
    projection = zeros(4)
    for indices, values in (((0, 2), (a, b)), ((1, 3), (c, d))):
        norm2 = sum(value**2 for value in values)
        for i, row in enumerate(indices):
            for j, column in enumerate(indices):
                projection[row, column] = values[i] * values[j] / norm2
    unitary = diag(1, exp(I * phase), 1, exp(I * phase))
    return (
        (projection**2 - projection).applyfunc(simplify) == zeros(4)
        and projection * unitary == unitary * projection,
        "An arbitrary positive fiber line depending on the outside bit is a projection "
        "and commutes exactly with an outside unit-modulus phase. The continuum VA8 "
        "proof uses this integration-variable identity, even for boundary-dependent kernels",
    )


@vacuum.check(
    "True conditional projections share the correlated vacuum and are orthogonal in its measure",
    CITE + " VA9 VA11",
)
def _true_conditional():
    omega = Matrix([1, 2, 3, 4])
    probabilities = [Rational(value**2, 30) for value in omega]
    measure = diag(*probabilities)
    multiplication = diag(*omega)
    projections = []
    for groups in (((0, 2), (1, 3)), ((0, 1), (2, 3))):
        expectation = zeros(4)
        for group in groups:
            mass = sum(probabilities[j] for j in group)
            for i in group:
                for j in group:
                    expectation[i, j] = probabilities[j] / mass
        assert expectation**2 == expectation
        assert expectation.T * measure == measure * expectation
        projections.append(multiplication * expectation * multiplication.inv())
    parent = sum((eye(4) - p for p in projections), zeros(4))
    return (
        all(p == p.T and p * omega == omega for p in projections)
        and parent * omega == zeros(4, 1)
        and parent.rank() == 3
        and projections[0] * projections[1] != projections[1] * projections[0],
        "In an exact nonproduct four-state vacuum, conditional expectations become "
        "symmetric projections sharing the exact vacuum after multiplication by Omega. "
        "They need not commute; the sum has a unique zero vector. No frustration scalar is dropped",
    )


@vacuum.check(
    "The true-ground graph form cancels the complete vacuum before any local bound", CITE + " VA9"
)
def _centered_form():
    omega = Matrix([1, 2, 3, 4])
    edges = ((0, 1), (0, 2), (1, 3), (2, 3))
    h = zeros(4)
    for i, j in edges:
        h[i, j] = h[j, i] = -1
        h[i, i] += omega[j] / omega[i]
        h[j, j] += omega[i] / omega[j]
    f = Matrix(symbols("f0:4", real=True))
    state = diag(*omega) * f
    exact = (state.T * h * state)[0]
    dirichlet = sum(omega[i] * omega[j] * (f[i] - f[j]) ** 2 for i, j in edges)
    return h * omega == zeros(4, 1) and simplify(exact - dirichlet) == 0, (
        "An exact correlated-vacuum discrete ground transform cancels the full energy "
        "and yields only positive weighted edge differences. This checks the finite "
        "identity underlying the analytic Wilson form VA9, not a continuum statement"
    )


@vacuum.check(
    "The true-conditional Poincare coefficient and pair budget retain their coupling dependence",
    CITE + " VA10 VA16",
)
def _conditional_constants():
    epsilon, k = symbols("epsilon k", positive=True)
    r1 = Rational(5, 3) * exp(8 * k / epsilon)
    r2 = Rational(5, 3) ** 2 * exp(16 * k / epsilon)
    return (
        simplify(3 * epsilon / r1**2 - Rational(27, 25) * epsilon * exp(-16 * k / epsilon)) == 0
        and simplify(r2**-4 - Rational(3, 5) ** 8 * exp(-64 * k / epsilon)) == 0,
        "gamma_*=(27/25)epsilon exp(-16k/epsilon) and the pair minorization is "
        "(3/5)^8 exp(-64k/epsilon). These are volume-independent local bounds, "
        "not a summable physical influence budget or a continuum clock bound",
    )


@vacuum.check(
    "Two-projection angle algebra gives the exact sufficient assembly budget", CITE + " VA12 VA13"
)
def _projection_angle():
    r, eigenvalue = symbols("r eigenvalue", real=True)
    p = Matrix([[1, 0], [0, 0]])
    vector = Matrix([r, sqrt(1 - r**2)])
    q = vector * vector.T
    total = p + q
    anticommutator = p * q + q * p
    return (
        simplify((total - eigenvalue * eye(2)).det() - ((eigenvalue - 1) ** 2 - r**2)) == 0
        and (anticommutator - (total**2 - total)).applyfunc(simplify) == zeros(2),
        "In each nontrivial angle block the projection sum has eigenvalues 1+/-r "
        "and {p,q}=total^2-total, proving {p,q}>=-r(p+q) for 0<=r<=1. "
        "VA12 sums this inequality; VA13 proves the separate physical one-cycle identity",
    )


@vacuum.check(
    "Optimizing the actual block heat comparison yields a square-root coupling loss",
    BLOCK_CITE + " BA2 BA4",
)
def _optimized_block_time():
    r, p, k, eps, tau = symbols("r p k eps tau", positive=True)
    action = 4 * k * p * tau / eps + r * pi**2 / tau
    optimum = pi * sqrt(r * eps / (k * p)) / 2
    return (
        simplify(diff(action, tau).subs(tau, optimum)) == 0
        and simplify(action.subs(tau, optimum) - 4 * pi * sqrt(r * p * k / eps)) == 0
        and simplify(
            action
            - 4 * pi * sqrt(r * p * k / eps)
            - (2 * sqrt(k * p * tau / eps) - pi * sqrt(r / tau)) ** 2
        )
        == 0,
        "Exact minimization and nonnegative-square remainder give exp(-4pi sqrt(r p k/epsilon)); "
        "the heat Harnack, true-ground semigroup and full conditional Poincare proofs "
        "are analytic in BA2",
    )


@vacuum.check(
    "Tail-assigned cubic blocks partition links and have the stated plaquette boundary",
    BLOCK_CITE + " BA1",
)
def _block_partition_geometry():
    outcomes = []
    for ell, side in ((1, 3), (2, 4), (3, 6)):
        vertices = list(product(range(side), repeat=3))
        block = {(v, d) for v in product(range(ell), repeat=3) for d in range(3)}
        touching = 0
        for v in vertices:
            for i in range(3):
                for j in range(i + 1, 3):
                    vi, vj = list(v), list(v)
                    vi[i] = (vi[i] + 1) % side
                    vj[j] = (vj[j] + 1) % side
                    face = {(v, i), (tuple(vi), j), (tuple(vj), i), (v, j)}
                    touching += bool(face & block)
        outcomes.append(len(block) == 3 * ell**3 and touching == 3 * ell**3 + 6 * ell**2)
    return all(outcomes), (
        "Independent incidence counts for (ell,L)=(1,3),(2,4),(3,6) match r=3ell^3 and "
        "p=3ell^3+6ell^2. The all-size disjoint-tail partition proof is BA1; "
        "ell=2 uses 24 links, not 12"
    )


@vacuum.check(
    "The mixed density ratio averages to the joint-to-product marginal ratio",
    BLOCK_CITE + " BA6 BA7",
)
def _mixed_ratio_identity():
    a, b, c, d = symbols("a b c d", positive=True)
    table = Matrix([[a, b], [c, d]]) / (a + b + c + d)
    row = sum(table[0, j] for j in range(2))
    col = sum(table[i, 0] for i in range(2))
    weights = [table[0, j] * table[i, 0] / (row * col) for i in range(2) for j in range(2)]
    ratios = [
        table[0, 0] * table[i, j] / (table[0, j] * table[i, 0]) for i in range(2) for j in range(2)
    ]
    return (
        simplify(sum(weights) - 1) == 0
        and simplify(
            sum(w * z for w, z in zip(weights, ratios, strict=True)) - table[0, 0] / (row * col)
        )
        == 0,
        "For arbitrary positive 2x2 weights the averaging identity holds exactly. BA7 proves "
        "its integral version and the same-marginal minorization giving c_phys<=1-exp(-D)",
    )


@vacuum.check(
    "A correlated conditional pair has the predicted exact projection angle", BLOCK_CITE + " BA7"
)
def _correlated_angle_control():
    probs = [Rational(2, 5), Rational(1, 10), Rational(1, 10), Rational(2, 5)]
    coordinates = list(product(range(2), repeat=2))
    projections = []
    for kept in range(2):
        projection = zeros(4)
        for i in range(4):
            for j in range(4):
                if coordinates[i][kept] == coordinates[j][kept]:
                    projection[i, j] = 2 * sqrt(probs[i] * probs[j])
        projections.append(projection)
    omega = Matrix([sqrt(p) for p in probs])
    centered_product = projections[0] * projections[1] - omega * omega.T
    return (
        centered_product.rank() == 1
        and simplify((centered_product.T * centered_product).trace()) == Rational(9, 25)
        and Rational(3, 5) < 1 - Rational(1, 16),
        "Exact true-conditional projections in the four-state correlated measure have angle 3/5. "
        "Its maximum density cross ratio is 16 and the proved minorization bound is 15/16; "
        "this is a finite nonproduct control, not an assumed Wilson angle",
    )


@vacuum.check("Conditional pressure can change a frozen finite-block gap", BLOCK_CITE + " BA9 BA10")
def _pressure_gap_control():
    frozen = Matrix([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
    pressure = diag(0, Rational(5, 2), 0)
    actual = frozen + pressure
    omega = Matrix([2, 1, 2])
    return (
        set(frozen.eigenvals()) == {0, 1, 3}
        and set(actual.eigenvals()) == {Rational(1, 2), 1, 5}
        and actual * omega == omega / 2,
        "An exact irreducible three-state example has frozen gap 1 and pressure-corrected "
        "gap 1/2 with positive ground (2,1,2). A frozen spectral value is not automatically "
        "a true conditional gap; BA9 proves the oscillation comparison by min-max",
    )


@vacuum.check(
    "Differentiating a normalized tilted expectation gives the signed connected force identity",
    BLOCK_CITE + " BA11",
)
def _tilted_covariance_identity():
    s, t = symbols("s t", real=True)
    av, bv, cv = [1, -2, 3], [2, 1, -1], [3, -1, 2]
    weights = [Rational(1, 6), Rational(1, 3), Rational(1, 2)]
    z = sum(
        w * exp(-s * a - t * b - s * t * c) for w, a, b, c in zip(weights, av, bv, cv, strict=True)
    )
    subs = {s: 0, t: 0}
    mixed_log = (diff(z, s, t) / z - diff(z, s) * diff(z, t) / z**2).subs(subs)

    def mean(values):
        return sum(w * value for w, value in zip(weights, values, strict=True))

    target = mean([a * b for a, b in zip(av, bv, strict=True)]) - mean(av) * mean(bv) - mean(cv)
    return simplify(mixed_log - target) == 0, (
        "An independent finite tilted measure gives d_s d_t log Z=Cov(A,B)-E(C), with "
        "the direct second-derivative sign retained. BA11 derives the compact Brownian "
        "path identity and its finite-volume limit analytically; "
        "no uniform spatial decay is checked"
    )


@vacuum.check(
    "Exact Brownian slab factor incidence obeys the bounded-degree polymer geometry",
    BLOCK_CITE + " BA20 BA23",
)
def _slab_factor_geometry():
    side, slabs = 3, 3
    links = [(v, d) for v in product(range(side), repeat=3) for d in range(3)]
    faces = []
    for v in product(range(side), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                vi, vj = list(v), list(v)
                vi[i] = (vi[i] + 1) % side
                vj[j] = (vj[j] + 1) % side
                faces.append(((v, i), (tuple(vi), j), (tuple(vj), i), (v, j)))
    factors = []
    for time in range(slabs):
        factors.extend({("U", edge, time), ("U", edge, time + 1)} for edge in links)
        for face in faces:
            factors.append(
                {("U", edge, t) for edge in face for t in (time, time + 1)}
                | {("bridge", edge, time) for edge in face}
            )
    incidences = {}
    for i, factor in enumerate(factors):
        for variable in factor:
            incidences.setdefault(variable, set()).add(i)
    degree = max(
        len(set().union(*(incidences[v] for v in factor)) - {i}) for i, factor in enumerate(factors)
    )
    boundary_links = [((0, 0, 0), d) for d in range(3)]
    boundary_factors = set().union(*(incidences[("U", edge, 0)] for edge in boundary_links))
    return (
        degree <= 84
        and len(boundary_factors) <= 15
        and max(len(incidences[v]) for v in incidences if v[0] == "U") == 10
        and max(len(incidences[v]) for v in incidences if v[0] == "bridge") == 4,
        "Exact side-3, three-slab incidence control has endpoint multiplicity 10, bridge "
        "multiplicity 4, factor degree at most 84 and at most 15 roots per three-link block. "
        "BA20 constructs the actual continuous-path factors; this is its finite geometric control",
    )


@vacuum.check(
    "The constructed slab activities meet a strict uniform physical angle budget",
    BLOCK_CITE + " BA21 BA25",
)
def _slab_budget_constants():
    alpha = Rational(1, 32000)
    exp_upper = sum(Rational(1, factorial(n)) for n in range(4)) + Rational(5, 96)
    x = 8 * alpha
    pinned = x / (1 - 4 * 84 * x)
    row = 160 * 3 * pinned
    return (
        exp_upper == Rational(87, 32)
        and exp_upper**2 < 8
        and Rational(1541, 6859) / 20**3 < alpha
        and 8 * Rational(1, 256000) == alpha
        and pinned == Rational(1, 3664)
        and 85 * pinned < 1
        and row == Rational(30, 229) < 1
        and 40 * 3 * pinned == Rational(15, 458)
        and 1 - row == Rational(199, 229),
        "The actual path-factor envelope alpha=1/32000 follows for k/epsilon<=1/256000. "
        "Exact KP constants give rooted weighted sum 1/3664, angle row <=30/229 and "
        "gap factor 199/229. The analytic polymer construction and ground limit are BA20-BA25",
    )
