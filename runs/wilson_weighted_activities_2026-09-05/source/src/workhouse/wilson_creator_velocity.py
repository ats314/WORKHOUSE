"""Exact finite tensor controls for the creator-velocity chart.

The support-convolution path never constructs an operator matrix. The second
path constructs local rank-one tensor matrices and their nilpotent exponential.
Complex creator velocity is conjugate linear, so its inverse is real linear.
These small tensor controls do not prove the volume-uniform Wilson estimates.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from functools import cached_property, lru_cache
from math import factorial

import sympy as sp


def _clean(value):
    return sp.expand(value)


def _l1(value):
    """Rational upper bound on complex absolute value, exact for real scalars."""
    return abs(sp.re(value)) + abs(sp.im(value))


def _support(word):
    return frozenset(i for i, value in enumerate(word) if value)


@dataclass(frozen=True)
class TensorSpace:
    dimensions: tuple[int, ...]

    def __post_init__(self):
        if not self.dimensions or any(not isinstance(d, int) or d < 2 for d in self.dimensions):
            raise ValueError(
                "A nonempty tensor space with local dimensions at least two is required"
            )

    @cached_property
    def basis(self):
        return tuple(itertools.product(*(range(d) for d in self.dimensions)))

    @cached_property
    def indices(self):
        return {word: i for i, word in enumerate(self.basis)}

    @property
    def vacuum(self):
        return self.basis[0]

    @property
    def modes(self):
        return self.basis[1:]

    def validate(self, coefficients, *, creators=False):
        if any(word not in self.indices for word in coefficients):
            raise ValueError("A coefficient word is outside the tensor basis")
        if creators and coefficients.get(self.vacuum, 0) != 0:
            raise ValueError("Creator families have zero empty-support coefficient")
        if any(
            not (sp.re(value).is_Rational and sp.im(value).is_Rational)
            for value in coefficients.values()
        ):
            raise TypeError(
                "Finite controls require exact rational real and imaginary coefficients"
            )

    def vector(self, coefficients):
        self.validate(coefficients)
        return sp.Matrix([coefficients.get(word, 0) for word in self.basis])

    def family(self, vector):
        if vector.shape != (len(self.basis), 1):
            raise ValueError("Wrong tensor-vector shape")
        return {
            word: _clean(value) for word, value in zip(self.basis, vector, strict=True) if value
        }

    def star(self, left, right):
        """Disjoint-support multiplication, with excited labels retained."""
        self.validate(left)
        self.validate(right)
        answer = {}
        for x, a in left.items():
            for y, b in right.items():
                if _support(x).isdisjoint(_support(y)):
                    z = tuple(max(i, j) for i, j in zip(x, y, strict=True))
                    answer[z] = answer.get(z, 0) + a * b
        return {word: _clean(value) for word, value in answer.items() if _clean(value)}

    def exponential(self, creators):
        self.validate(creators, creators=True)
        answer = {self.vacuum: sp.S.One}
        power = answer
        for degree in range(1, len(self.dimensions) + 1):
            power = self.star(power, creators)
            for word, value in power.items():
                answer[word] = answer.get(word, 0) + value / factorial(degree)
        return {word: _clean(value) for word, value in answer.items() if _clean(value)}

    def lowering(self, creators, vector):
        """Adjoint rank-one action, by matching and erasing excited labels."""
        self.validate(creators, creators=True)
        self.validate(vector)
        answer = {}
        for x, a in creators.items():
            support = _support(x)
            for y, b in vector.items():
                if all(y[i] == x[i] for i in support):
                    z = tuple(0 if i in support else v for i, v in enumerate(y))
                    answer[z] = answer.get(z, 0) + sp.conjugate(a) * b
        return {word: _clean(value) for word, value in answer.items() if _clean(value)}

    def velocity_map(self, w, b):
        """T_w b = Q exp_star(-w) star (B(b)^dag exp_star(w))."""
        self.validate(w, creators=True)
        answer = self.star(
            self.exponential({x: -a for x, a in w.items()}),
            self.lowering(b, self.exponential(w)),
        )
        answer.pop(self.vacuum, None)
        return answer

    def creator_matrix(self, creators):
        """Independent Kronecker construction with identity spectators."""
        self.validate(creators, creators=True)
        answer = sp.zeros(len(self.basis))
        for word, value in creators.items():
            factors = []
            for dim, level in zip(self.dimensions, word, strict=True):
                factor = sp.eye(dim) if level == 0 else sp.zeros(dim)
                if level:
                    factor[level, 0] = 1
                factors.append(factor)
            answer += value * sp.kronecker_product(*factors)
        return answer

    def matrix_exponential(self, w):
        matrix = self.creator_matrix(w)
        answer = sp.eye(len(self.basis))
        power = answer
        for degree in range(1, len(self.dimensions) + 1):
            power = power * matrix
            answer += power / factorial(degree)
        assert power * matrix == sp.zeros(len(self.basis))
        return answer.applyfunc(_clean)

    def conjugate_matrix(self, w):
        """K such that T_w(b)=K conjugate(b), using the support path only."""
        columns = [self.vector(self.velocity_map(w, {x: sp.S.One}))[1:, :] for x in self.modes]
        return sp.Matrix.hstack(*columns)

    def invert_velocity(self, w, tangent):
        self.validate(tangent, creators=True)
        matrix = self.conjugate_matrix(w)
        real = matrix.applyfunc(sp.re)
        imag = matrix.applyfunc(sp.im)
        identity = sp.eye(len(self.modes))
        # b - K conjugate(b), with b=x+i y.
        real_linear = (identity - real).row_join(-imag).col_join((-imag).row_join(identity + real))
        rhs = self.vector(tangent)[1:, :]
        solution = real_linear.inv() * rhs.applyfunc(sp.re).col_join(rhs.applyfunc(sp.im))
        count = len(self.modes)
        b = sp.Matrix([_clean(solution[i] + sp.I * solution[count + i]) for i in range(count)])
        assert (b - matrix * b.conjugate() - rhs).applyfunc(_clean) == sp.zeros(count, 1)
        return {x: a for x, a in zip(self.modes, b, strict=True) if a}, matrix

    def rooted_norm(self, family, *, cardinality=False):
        """Weight 2^|X|, with a coefficient-l1 upper bound for each Hilbert norm."""
        self.validate(family, creators=True)
        return max(
            sum(
                2 ** len(_support(x)) * (len(_support(x)) if cardinality else 1) * _l1(a)
                for x, a in family.items()
                if i in _support(x)
            )
            for i in range(len(self.dimensions))
        )

    def rooted_matrix_bound(self, matrix):
        """Exact finite bound using column anchors, valid for all complex inputs.

        Assign every input mode to its first site. The mass assigned to each
        site is bounded by the rooted input norm. Summing the maximum column
        coefficient per anchor then bounds each output root. This is a finite
        matrix certificate, not the analytic volume-uniform estimate.
        """
        roots = range(len(self.dimensions))
        return max(
            sum(
                max(
                    (
                        sum(
                            sp.Rational(2) ** (len(_support(y)) - len(_support(x)))
                            * _l1(matrix[row, col])
                            for row, y in enumerate(self.modes)
                            if root in _support(y)
                        )
                        for col, x in enumerate(self.modes)
                        if min(_support(x)) == anchor
                    ),
                    default=sp.S.Zero,
                )
                for anchor in roots
            )
            for root in roots
        )


def _difference(left, right):
    return {x: _clean(left.get(x, 0) - right.get(x, 0)) for x in left.keys() | right.keys()}


def verify_model(name, space, w, tangent):
    """Compare independent operator/support paths and certify exact transport."""
    b, matrix = space.invert_velocity(w, tangent)
    phi = space.vector(space.exponential(w))
    exponential = space.matrix_exponential(w)
    inverse = space.matrix_exponential({x: -a for x, a in w.items()})
    omega = sp.eye(len(space.basis))[:, 0]
    assert exponential * inverse == sp.eye(len(space.basis))
    assert (exponential * omega - phi).applyfunc(_clean) == sp.zeros(len(space.basis), 1)
    for column, mode in enumerate(space.modes):
        direct = inverse * space.creator_matrix({mode: 1}).H * exponential * omega
        assert (direct[1:, :] - matrix[:, column]).applyfunc(_clean) == sp.zeros(
            len(space.modes), 1
        )
    creator = space.creator_matrix(b)
    generator = creator - creator.H
    derivative = space.creator_matrix(tangent) * phi
    assert derivative == space.vector(space.star(tangent, space.exponential(w)))
    scalar = _clean((generator * phi - derivative)[0])
    assert (generator * phi - derivative - scalar * phi).applyfunc(_clean) == sp.zeros(
        len(space.basis), 1
    )
    norm_squared = _clean((phi.H * phi)[0])
    normalization_rate = _clean(sp.re((phi.H * derivative)[0]) / norm_squared)
    assert _clean(sp.re(scalar) + normalization_rate) == 0
    assert (
        generator * phi - derivative + normalization_rate * phi - sp.I * sp.im(scalar) * phi
    ).applyfunc(_clean) == sp.zeros(len(space.basis), 1)
    assert generator.H + generator == sp.zeros(len(space.basis))
    # A complex mode witnesses conjugate linearity independently of inversion.
    probe = {space.modes[0]: sp.I}
    assert (space.vector(space.velocity_map(w, probe))[1:, :] + sp.I * matrix[:, 0]).applyfunc(
        _clean
    ) == sp.zeros(len(space.modes), 1)
    a = space.rooted_norm(w)
    m1 = space.rooted_norm(w, cardinality=True)
    q = space.rooted_matrix_bound(matrix)
    assert a < sp.Rational(1, 2)
    assert 0 < q < 1
    assert q <= 2 * m1
    analytic_envelope = m1 / (2 * (1 - 2 * a))
    assert q <= analytic_envelope
    # Finite Neumann sum and its nonzero error, with the certified operator bound.
    term = tangent
    partial = dict(tangent)
    for _ in range(3):
        term = space.velocity_map(w, term)
        for x, value in term.items():
            partial[x] = partial.get(x, 0) + value
    error = space.rooted_norm(_difference(b, partial))
    tail_bound = q**4 / (1 - q) * space.rooted_norm(tangent)
    assert 0 < error <= tail_bound
    return {
        "name": name,
        "dimensions": list(space.dimensions),
        "creator_supports": [
            sorted(s) for s in sorted({_support(x) for x in w}, key=lambda s: tuple(s))
        ],
        "map_columns_checked": len(space.modes),
        "independent_exponential_and_map": True,
        "real_linear_inverse_residual_zero": True,
        "normalized_vacuum_line_transport": True,
        "phase_rate": str(sp.im(scalar)),
        "weight_two_coefficient_l1_mass": str(a),
        "weight_two_cardinality_mass": str(m1),
        "finite_rooted_matrix_bound": str(q),
        "rational_upper_envelope_of_analytic_bound": str(analytic_envelope),
        "neumann_terms": 4,
        "neumann_remainder_nonzero": True,
        "neumann_remainder_within_bound": True,
        "neumann_remainder_norm": str(error),
        "neumann_remainder_bound": str(tail_bound),
    }


def phase_control():
    space = TensorSpace((2,))
    w = {(1,): sp.Rational(1, 10)}
    tangent = {(1,): sp.I / 20}
    b, _ = space.invert_velocity(w, tangent)
    assert b[(1,)] == 5 * sp.I / 99
    phi = space.vector(space.exponential(w))
    creator = space.creator_matrix(b)
    defect = (creator - creator.H) * phi - space.creator_matrix(tangent) * phi
    assert defect == sp.I / 198 * phi
    return {
        "velocity": "5*I/99",
        "normalized_vector_phase_rate": "1/198",
        "line_transport_exact": True,
    }


def factorization_control():
    left = TensorSpace((2, 2))
    right = TensorSpace((2, 2))
    full = TensorSpace((2, 2, 2, 2))
    wl = {(1, 0): sp.Rational(1, 50), (1, 1): sp.Rational(1, 80)}
    wr = {(0, 1): sp.Rational(1, 60), (1, 1): -sp.Rational(1, 90)}
    dl = {(0, 1): sp.Rational(1, 70), (1, 1): sp.Rational(1, 110)}
    dr = {(1, 0): -sp.Rational(1, 100), (1, 1): sp.Rational(1, 120)}

    def combine(a, b):
        return {**{(*x, 0, 0): v for x, v in a.items()}, **{(0, 0, *x): v for x, v in b.items()}}

    bl, _ = left.invert_velocity(wl, dl)
    br, _ = right.invert_velocity(wr, dr)
    bg, matrix = full.invert_velocity(combine(wl, wr), combine(dl, dr))
    assert bg == combine(bl, br)
    global_creator = full.creator_matrix(bg)
    local_creator = sp.kronecker_product(left.creator_matrix(bl), sp.eye(4)) + sp.kronecker_product(
        sp.eye(4), right.creator_matrix(br)
    )
    assert global_creator == local_creator
    assert full.vector(full.exponential(combine(wl, wr))) == sp.kronecker_product(
        left.vector(left.exponential(wl)), right.vector(right.exponential(wr))
    )
    assert full.rooted_matrix_bound(matrix) < 1
    return {
        "sites": 4,
        "global_inverse_equals_embedded_local_inverses": True,
        "cross_component_velocities_zero": True,
        "generator_is_tensor_sum": True,
        "creation_exponential_factorizes": True,
    }


def scalar_bounds():
    """Rational implication checks; analytic transcendental premises are named."""
    q = sp.Rational(1, 10000)
    primitive = sp.Rational(568, 145) * q
    eta = sp.Rational(1, 2500)
    full_operator = eta / (2 * (sp.Rational(1, 5) - eta))
    threshold = sp.Rational(1024, 15625) / 10
    variable = sp.Symbol("q")
    weighted_sum = 3 * variable * sp.diff(1 / (1 - variable), variable) + variable / (1 - variable)
    assert sp.cancel(weighted_sum - variable * (4 - variable) / (1 - variable) ** 2) == 0
    m1 = sp.Rational(1, 8) / (sp.Rational(8, 3) * sp.Rational(1, 3))
    theta = 2 * sp.Rational(1, 2) * sp.Rational(4, 3) * m1
    assert m1 == sp.Rational(9, 64)
    assert theta == sp.Rational(3, 16) <= sp.Rational(1, 4)
    assert sp.Rational(4, 3) * sp.Rational(1, 8) == sp.Rational(1, 6)
    assert 145 * 216 * 4 / sp.Integer(1252800000) == q
    assert sp.Rational(24, 145) * (1 + sp.Rational(17, 3) * 4) == sp.Rational(568, 145)
    assert primitive <= eta
    assert full_operator == sp.Rational(1, 998)
    assert full_operator < threshold
    return {
        "q_upper": str(q),
        "primitive_upper": str(primitive),
        "eta_upper": str(eta),
        "full_operator_upper": str(full_operator),
        "relative_gap_threshold": str(threshold),
        "chart_cardinality_moment_upper": str(m1),
        "chart_contraction_upper": str(theta),
        "chart_velocity_upper": "1/6",
        "transcendental_premises": [
            "log(5/4) >= 1/5",
            "8/3 <= e < 3",
            "log(2)/2 >= 1/3",
            "exp(1/4) <= 4/3",
        ],
        "scope": "Exact rational consequences of the stated analytic premises and majorant formula",
    }


def contour_control():
    """Third-order ordered insertions versus the three-site partition cumulant.

    Two noncommuting edge projectors flank a product kinetic contraction.
    Connected terms are enumerated as words, separately from matrix powers
    and partition subtraction. This is a finite polynomial identity only.
    """
    edge = sp.Matrix([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) / 2
    h = (sp.kronecker_product(edge, sp.eye(2)), sp.kronecker_product(sp.eye(2), edge))
    d = sp.kronecker_product(*(sp.diag(1, sp.Rational(1, 4)) for _ in range(3)))
    left_weights = (sp.Rational(1, 2), sp.Rational(1, 3))
    right_weights = (sp.Rational(1, 5), sp.Rational(1, 7))

    def coefficient(active, degree):
        a = sum((left_weights[i] * h[i] for i in active), sp.zeros(8))
        b = sum((right_weights[i] * h[i] for i in active), sp.zeros(8))
        return sum(
            (
                a**k * d * b ** (degree - k) / (factorial(k) * factorial(degree - k))
                for k in range(degree + 1)
            ),
            sp.zeros(8),
        )

    counts = []
    for degree in range(4):
        # C_012=G_012-G_01 D_2-G_12 D_0+D_012; the absent edge 02
        # and the triple-singleton terms combine to the final free product.
        cumulant = (
            coefficient((0, 1), degree) - coefficient((0,), degree) - coefficient((1,), degree)
        )
        if degree == 0:
            cumulant += d
        connected = sp.zeros(8)
        count = 0
        for split in range(degree + 1):
            for word in itertools.product((0, 1), repeat=degree):
                if set(word) != {0, 1}:
                    continue
                term = sp.eye(8)
                for label in word[:split]:
                    term = term * left_weights[label] * h[label]
                term = term * d
                for label in word[split:]:
                    term = term * right_weights[label] * h[label]
                connected += term / (factorial(split) * factorial(degree - split))
                count += 1
        assert cumulant == connected
        assert connected[:, 0] == sp.zeros(8, 1)
        assert connected[0, :] == sp.zeros(1, 8)
        counts.append(count)
    commutator = h[0] * h[1] - h[1] * h[0]
    commutator_square = sum(a * a for a in commutator)
    assert commutator_square == sp.Rational(3, 4)
    return {
        "sites": 3,
        "orders": 4,
        "connected_words_per_order": counts,
        "connected_words_equal_partition_cumulants": True,
        "overlap_commutator_frobenius_squared": str(commutator_square),
        "scope": (
            "Degrees zero through three of a finite ordered noncommuting contour "
            "with kinetic contractions"
        ),
    }


@lru_cache(maxsize=1)
def exact_controls():
    real_space = TensorSpace((3, 3, 2))
    w = {
        (1, 1, 0): sp.Rational(1, 300),
        (2, 2, 0): -sp.Rational(1, 400),
        (0, 1, 1): sp.Rational(1, 500),
        (0, 2, 1): sp.Rational(1, 600),
        (1, 0, 1): -sp.Rational(1, 450),
        (2, 0, 0): sp.Rational(1, 200),
        (1, 2, 1): sp.Rational(1, 900),
    }
    tangent = {x: sp.Rational((-1) ** i, 500 + 10 * i) for i, x in enumerate(real_space.modes)}
    complex_space = TensorSpace((3, 2))
    wc = {(1, 0): (1 + sp.I) / 100, (2, 1): (2 - sp.I) / 200, (1, 1): sp.Rational(1, 120)}
    dc = {(1, 0): sp.I / 70, (2, 0): (1 - sp.I) / 90, (1, 1): sp.Rational(1, 110)}
    return {
        "models": [
            verify_model("entangled_overlap", real_space, w, tangent),
            verify_model("complex", complex_space, wc, dc),
        ],
        "phase_control": phase_control(),
        "factorization": factorization_control(),
        "scalar_bounds": scalar_bounds(),
        "ordered_contour": contour_control(),
        "scope": (
            "Exact finite creator algebra, real-linear inverse, vacuum line and component "
            "transport; not a Wilson rotor or uniform analytic proof"
        ),
    }
