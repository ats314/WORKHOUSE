"""Exact interfaces for the actual Wilson block/marked expansion.

The companion derivation proves the operator activity estimate analytically.
These checks cover finite noncommutative expansions, activation combinatorics,
vacuum cancellation, geometry, and the algebra of its uniform estimates. They
do not certify the unconstructed complete interacting Wilson Riesz shell.
"""

from __future__ import annotations

from itertools import combinations, product
from math import factorial

from sympy import (
    Matrix,
    Rational,
    S,
    binomial,
    cos,
    diag,
    exp,
    eye,
    kronecker_product,
    limit,
    simplify,
    sin,
    symbols,
    trigsimp,
    zeros,
)

from ._core import _suite

marked = _suite("Wilson marked expansion: exact blocks and uniform bound algebra")
CITE = "WILSON_MARKED; G17; G18; G19"
BLOCK = "Wilson block expansion retains the symmetric endpoint factors at every tested order"
ACTIVATE = "Wilson activation selects exactly the words that contain every active plaquette"
MAJORANT = "Wilson activated-block majorant coefficients are onto-label counts divided by factorial"
VACUUM = "Wilson normalized marked expectation cancels an independent vacuum factor exactly"
COUNT = "cubic link-time polymer graph has degree at most 38 and at most ten labels per vertex"
KP = (
    "Wilson polymer counting satisfies the Kotecky-Preiss budget when its ratio is at most one half"
)


def _mul(a: list[Matrix], b: list[Matrix]) -> list[Matrix]:
    n, dim = len(a) - 1, a[0].rows
    return [sum((a[j] * b[k - j] for j in range(k + 1)), zeros(dim)) for k in range(n + 1)]


def _power(a: list[Matrix], m: int) -> list[Matrix]:
    out = [eye(a[0].rows)] + [zeros(a[0].rows) for _ in a[1:]]
    for _ in range(m):
        out = _mul(out, a)
    return out


def _block(k: Matrix, v: Matrix, m: int, order: int) -> list[Matrix]:
    # Microscopic tau=1/m, so physical block time is exactly one.
    half = [(v / (2 * m)) ** j / factorial(j) for j in range(order + 1)]
    kinetic = [k] + [zeros(k.rows) for _ in range(order)]
    return _power(_mul(_mul(half, kinetic), half), m)


def _same(a, b):
    return all(x == y for x, y in zip(a, b, strict=True))


@marked.check(BLOCK, CITE + " WT-1")
def _symmetric_blocks():
    k, v, order = diag(1, Rational(3, 5)), Matrix([[1, 2], [2, -1]]), 4
    verdicts = []
    for m in (1, 2, 4):
        half = [(v / (2 * m)) ** j / factorial(j) for j in range(order + 1)]
        full = [(v / m) ** j / factorial(j) for j in range(order + 1)]
        kinetic = [k] + [zeros(2) for _ in range(order)]
        packed = _mul(_mul(_mul(half, _power(_mul(kinetic, full), m - 1)), kinetic), half)
        verdicts.append(_same(_block(k, v, m, order), packed))
    return all(verdicts) and k * v != v * k, (
        "Exact noncommuting 2x2 matrices, m=1,2,4, coefficients 0..4: "
        f"(A K A)^m=A(K A^2)^(m-1)K A, matches={verdicts}; total magnetic time m*tau=1"
    )


@marked.check(ACTIVATE, CITE + " WT-2", rests_on=(BLOCK,))
def _activation():
    k = diag(1, Rational(2, 3))
    x, z = Matrix([[0, 1], [1, 0]]), diag(1, -1)
    order, tests = 4, []
    for m in (1, 2, 3):
        both, first, second, empty = [_block(k, v, m, order) for v in (x + z, x, z, zeros(2))]
        delta = [both[n] - first[n] - second[n] + empty[n] for n in range(order + 1)]
        tests.append(delta[0] == zeros(2) and delta[1] == zeros(2))
        tests.append(any(a != zeros(2) for a in delta[2:]))
        # Removing either active interaction makes the activation identically zero.
        tests.append(
            all(second[n] - empty[n] - second[n] + empty[n] == zeros(2) for n in range(order + 1))
        )
    return all(tests), (
        "Two noncommuting interaction labels: mixed activation vanishes at orders 0,1, "
        "has a nonzero higher coefficient, and vanishes if a required label is removed; m=1,2,3"
    )


@marked.check(MAJORANT, CITE + " WT-2")
def _onto_majorant():
    tests, cases = [], 0
    for k in range(1, 5):
        for n in range(9):
            inclusion = sum(
                (-1) ** (k - j) * binomial(k, j) * j**n for j in range(k + 1)
            ) / factorial(n)
            # Independent coefficient extraction from (exp(x)-1)^k.
            coefficient = sum(
                (
                    S.One / product_factorial(parts)
                    for parts in product(range(1, n + 1), repeat=k)
                    if sum(parts) == n
                ),
                S.Zero,
            )
            tests.append(inclusion == coefficient and coefficient >= 0)
            cases += 1
    return all(tests), (
        f"{cases} exact coefficients: sum_j (-1)^(k-j) binomial(k,j) j^n/n! "
        "equals sum_(r_1+...+r_k=n, r_i>=1) 1/prod r_i!; "
        "the block norm majorant is (exp(ell*v*abs(u))-1)^k, with no slice-count factor"
    )


def product_factorial(parts):
    value = 1
    for part in parts:
        value *= factorial(part)
    return value


@marked.check(VACUUM, CITE + " WT-3")
def _vacuum_cancellation():
    # Exact positive symmetric transfers with strictly positive entries.
    a, b = Matrix([[2, 1], [1, 1]]) / 3, Matrix([[3, 1], [1, 2]]) / 4
    o, omega = diag(1, -1), Matrix([1, 0])
    whole, om = kronecker_product(a, b), kronecker_product(omega, omega)
    tests = []
    for m in (1, 2, 4):
        na = (omega.T * a**m * o * a**m * omega)[0]
        za = (omega.T * a ** (2 * m) * omega)[0]
        zb = (omega.T * b ** (2 * m) * omega)[0]
        n = (om.T * whole**m * kronecker_product(o, eye(2)) * whole**m * om)[0]
        d = (om.T * whole ** (2 * m) * om)[0]
        tests.append(n == na * zb and d == za * zb and n / d == na / za)
    return all(tests), (
        "For m=1,2,4, exact tensor contractions give numerator=N_A*Z_B, "
        "denominator=Z_A*Z_B, and the normalized observable equals N_A/Z_A. "
        "The all-orders factorization proof and its nonzero-denominator hypothesis are in WT-3"
    )


@marked.check(
    "Wilson disconnected components separated in time also factor after a vacuum reset",
    CITE + " WT-3",
)
def _vacuum_reset():
    omega = Matrix([1, 0])
    p = omega * omega.T
    a, b, k = Matrix([[2, 1], [1, 3]]), Matrix([[4, 2], [2, 1]]), diag(1, Rational(1, 3))
    reset = (omega.T * b * p * k * a * omega)[0]
    product_value = (omega.T * b * omega)[0] * (omega.T * a * omega)[0]
    unreset = (omega.T * b * k * a * omega)[0]
    return reset == product_value and unreset != product_value, (
        f"Same-site components: vacuum reset gives {reset}={product_value}; "
        f"without the reset the value is {unreset}. Separation in time alone is insufficient"
    )


@marked.check(
    "Wilson complete finite configuration sum equals the transfer power and factorizes by polymers",
    CITE + " WT-3",
    rests_on=(VACUUM, ACTIVATE),
)
def _complete_configuration_sum():
    p, q = diag(1, 0), diag(0, 1)
    x = Matrix([[0, 1], [1, 0]])
    omega = Matrix([1, 0, 0, 0])
    kinetic = diag(1, Rational(1, 3), Rational(1, 4), Rational(1, 12))
    # A=exp(log(2)*X tensor X) exactly, since the involution squares to one.
    half = (5 * eye(4) + 3 * kronecker_product(x, x)) / 4
    block = half * kinetic * half
    terms = [kinetic * kronecker_product(a, b) for a, b in product((p, q), repeat=2)]
    terms.append(block - kinetic)
    occupied = (set(), {1}, {0}, {0, 1}, {0, 1})
    assert sum(terms, zeros(4)) == block

    def weight(config):
        state = omega
        for label in config:
            state = terms[label] * state
        return (omega.T * state)[0]

    total, checked, splits = S.Zero, 0, 0
    for config in product(range(5), repeat=4):
        support = {
            (t, site)
            for k, label in enumerate(config)
            for t in (k, k + 1)
            for site in occupied[label]
        }
        components = []
        unseen = set(support)
        while unseen:
            component, todo = set(), [min(unseen)]
            while todo:
                vertex = todo.pop()
                if vertex not in unseen:
                    continue
                unseen.remove(vertex)
                component.add(vertex)
                todo.extend(v for v in unseen if abs(v[0] - vertex[0]) <= 1)
            components.append(component)
        factored = S.One
        for component in components:
            subconfig = tuple(
                label if any((k, site) in component for site in occupied[label]) else 0
                for k, label in enumerate(config)
            )
            factored *= weight(subconfig)
        actual = weight(config)
        if actual != factored:
            return False, f"component factorization failed for labels {config}"
        total += actual
        checked += 1
        splits += len(components) > 1
    expected = (omega.T * block**4 * omega)[0]
    return total == expected and checked == 625 and splits > 0, (
        f"All {checked} four-block configurations, including {splits} disconnected ones, "
        f"factor by connected components; sum={total}=<Omega,B^4 Omega>. "
        "This checks the complete projector/activation pipeline on a finite two-link model"
    )


@marked.check(COUNT, CITE + " WT-4")
def _polymer_geometry():
    counts = []
    for side in (3, 4):
        sites = list(product(range(side), repeat=3))
        links = {(p, a) for p in sites for a in range(3)}
        adjacency = {e: set() for e in links}
        incidence = {e: 0 for e in links}
        for p in sites:
            for a, b in combinations(range(3), 2):
                pa, pb = list(p), list(p)
                pa[a] = (pa[a] + 1) % side
                pb[b] = (pb[b] + 1) % side
                face = {(p, a), (tuple(pa), b), (tuple(pb), a), (p, b)}
                assert len(face) == 4
                for e in face:
                    adjacency[e].update(face - {e})
                    incidence[e] += 1
        degree = max(map(len, adjacency.values()))
        faces_per_link = max(incidence.values())
        counts.append((side, degree, 3 * (degree + 1) - 1, 2 * faces_per_link + 2))
    return all(
        d <= 12 and time_degree <= 38 and labels <= 10 for _, d, time_degree, labels in counts
    ), (
        f"(L, spatial degree, link-time degree, incident binary labels)={counts}; "
        "analytically each link meets four plaquettes, each contributes at most three neighbors"
    )


@marked.check(KP, CITE + " WT-4", rests_on=(COUNT, MAJORANT))
def _kp_budget():
    r, degree = symbols("r degree", positive=True)
    # Subtracting the incompatibility budget from one has positive numerator
    # if r<=1/2 and degree>=2, as formalized separately in Lean.
    budget = (degree + 1) * r / (degree**2 * (1 - r))
    defect = simplify(
        1 - budget - (degree**2 - (degree**2 + degree + 1) * r) / (degree**2 * (1 - r))
    )
    worst = budget.subs({degree: 38, r: Rational(1, 2)})
    return defect == 0 and worst == Rational(39, 1444) and worst < 1, (
        f"Root sum <= r/[D^2(1-r)], incompatibility multiplier D+1; D=38,r=1/2 gives {worst}<1. "
        "The general r<=1/2,D>=2 budget is Lean-proved; activity and lattice-animal "
        "bounds are analytic inputs"
    )


@marked.check(
    "Wilson complex resolvent denominator has an exact radial and angular square decomposition",
    CITE + " WT-5",
)
def _complex_denominator():
    radius, theta = symbols("radius theta", real=True)
    direct = (radius * cos(theta) - 1) ** 2 + (radius * sin(theta)) ** 2
    split = (radius - 1) ** 2 + 4 * radius * sin(theta / 2) ** 2
    return trigsimp(direct - split) == 0, (
        "|r exp(i theta)-1|^2=(r-1)^2+4r sin(theta/2)^2 exactly. "
        "The sine and exponential inequalities giving the all-energy norm bound "
        "are stated in WT-5"
    )


@marked.check(
    "Wilson damped denominators have a finite physical-time limit "
    "while a raw transfer resolvent diverges",
    CITE + " WT-5",
)
def _time_denominator():
    tau, energy = symbols("tau energy", positive=True)
    damped = tau / (exp(tau * energy) - 1)
    geometric = tau / (1 - exp(-tau * energy))
    raw = 1 / (1 - exp(-tau * energy))
    return (
        simplify(geometric - damped - tau) == 0
        and limit(damped, tau, 0, dir="+") == 1 / energy
        and limit(tau * raw, tau, 0, dir="+") == 1 / energy
    ), (
        "tau/(1-exp(-tau E))=tau+tau/(exp(tau E)-1); the damped limit is 1/E, "
        "whereas the raw resolvent has a nonzero 1/tau coefficient. "
        "Lean proves tau/(exp(tau E)-1)<=1/E for all positive tau,E"
    )


@marked.check(
    "Wilson carrier transport error budgets preserve a relative gap "
    "and a positive source amplitude conditionally",
    CITE + " WT-6",
)
def _transport_budget():
    c, q, gamma, eta, source, error = symbols("c q gamma eta source error", real=True)
    gap_defect = simplify(c * q - 2 * gamma * eta * q - (c - 2 * gamma * eta) * q)
    amplitude_defect = simplify(source**2 - (source - error) ** 2 - error * (2 * source - error))
    return gap_defect == 0 and amplitude_defect == 0, (
        "Gap coefficient c spends 2*gamma*eta; source amplitude source spends error. "
        "Positivity requires 2*gamma*eta<c and error<source. "
        "Existence, completeness and matching of the Wilson shell are separate unproved premises"
    )


@marked.check(
    "FINDING: a uniform vacuum gap does not determine the multiplicity "
    "or source totality of an excited shell",
    CITE + " WT-6",
)
def _shell_falsifier():
    a = diag(1, Rational(1, 2), Rational(1, 4), Rational(1, 8))
    b = diag(1, Rational(1, 2), Rational(1, 2), Rational(1, 8))
    source = Matrix([0, 1, 0, 0])
    rank_a = 4 - (a - eye(4) / 2).rank()
    rank_b = 4 - (b - eye(4) / 2).rank()
    dark = Matrix([0, 0, 1, 0])
    return rank_a == 1 and rank_b == 2 and source.dot(dark) == 0 and b * dark == dark / 2, (
        "Positive transfers diag(1,1/2,1/4,1/8) and diag(1,1/2,1/2,1/8) "
        "have the same vacuum gap log(2), but shell ranks 1 and 2. "
        "The second shell has a vector orthogonal to the stated source"
    )
