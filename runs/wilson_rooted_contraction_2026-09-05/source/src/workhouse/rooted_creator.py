"""Exact bounded binary-link controls for the rooted creator construction.

This module checks a six-link finite model. Fractions never approximate the
Wilson Hilbert space or the analytic infinite-volume theorem. For Pauli flips,
exp(u X) is proportional to I + kappa X, where kappa=tanh(u); the scalar
proportionality cancels in the normalized magnetic creator map.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction
from math import factorial

Family = tuple[Fraction, ...]
ZERO = Fraction(0)
ONE = Fraction(1)
LINKS = 6
FACES = (0b001111, 0b111100, 0b110011)
KAPPA = Fraction(1, 100_000_000)
KINETIC_RATIO = Fraction(1, 2)
BALL_RADIUS = Fraction(1, 16)


def _links(family: Family) -> int:
    size = len(family)
    if size < 2 or size & (size - 1):
        raise ValueError("a family must have 2**links entries, with links >= 1")
    if any(not isinstance(value, (int, Fraction)) for value in family):
        raise TypeError("family coefficients must be exact integers or Fractions")
    return size.bit_length() - 1


def _same_size(left: Family, right: Family) -> int:
    links = _links(left)
    if links != _links(right):
        raise ValueError("family sizes differ")
    return links


def family(links: int, entries: Iterable[tuple[int, Fraction]] = ()) -> Family:
    """Build an exact-support family; mask zero is its vacuum coefficient."""
    if links < 1:
        raise ValueError("links must be positive")
    values = [ZERO] * (1 << links)
    for mask, value in entries:
        if not 0 <= mask < len(values):
            raise ValueError("support mask is outside the link set")
        if not isinstance(value, (int, Fraction)):
            raise TypeError("creator coefficients must be exact integers or Fractions")
        values[mask] += Fraction(value)
    return tuple(values)


def subtract(left: Family, right: Family) -> Family:
    _same_size(left, right)
    return tuple(a - b for a, b in zip(left, right, strict=True))


def star(left: Family, right: Family) -> Family:
    """Disjoint-support convolution, enumerated by partitions of the output."""
    _same_size(left, right)
    result = []
    for mask in range(len(left)):
        value = ZERO
        submask = mask
        while True:
            value += left[submask] * right[mask ^ submask]
            if not submask:
                break
            submask = (submask - 1) & mask
        result.append(value)
    return tuple(result)


def star_exp(creator: Family) -> Family:
    """Finite nilpotent exponential; a creator has zero vacuum coefficient."""
    links = _links(creator)
    if creator[0]:
        raise ValueError("creation exponential requires vacuum coefficient zero")
    result = list(family(links, ((0, ONE),)))
    power = tuple(result)
    for degree in range(1, links + 1):
        power = star(power, creator)
        divisor = factorial(degree)
        result = [a + b / divisor for a, b in zip(result, power, strict=True)]
    return tuple(result)


def star_log(vector: Family) -> Family:
    """Finite creation logarithm, after exact vacuum normalization."""
    links = _links(vector)
    if vector[0] != 1:
        raise ValueError("creation logarithm requires vacuum coefficient one")
    tail = (ZERO, *vector[1:])
    power = family(links, ((0, ONE),))
    result = [ZERO] * len(vector)
    for degree in range(1, links + 1):
        power = star(power, tail)
        coefficient = Fraction((-1) ** (degree + 1), degree)
        result = [a + coefficient * b for a, b in zip(result, power, strict=True)]
    return tuple(result)


def flip(vector: Family, mask: int) -> Family:
    """The product of Pauli-X operators on the links in mask."""
    _links(vector)
    if not 0 < mask < len(vector):
        raise ValueError("a magnetic support must be nonempty and inside the link set")
    return tuple(vector[index ^ mask] for index in range(len(vector)))


def magnetic_vector(vector: Family, faces: tuple[int, ...], kappa: Fraction) -> Family:
    """Apply every factor I+kappa X_p, retaining their mixed products."""
    if not isinstance(kappa, (int, Fraction)):
        raise TypeError("the magnetic parameter must be exact")
    for mask in faces:
        moved = flip(vector, mask)
        vector = tuple(a + kappa * b for a, b in zip(vector, moved, strict=True))
    return vector


def magnetic_map(
    creator: Family, faces: tuple[int, ...], kappa: Fraction
) -> tuple[Family, Fraction]:
    """Return F=log_star(normalized magnetic exp_star(v)) and its normalizer."""
    vector = magnetic_vector(star_exp(creator), faces, kappa)
    normalizer = vector[0]
    if not normalizer:
        raise ValueError("magnetic vacuum normalization vanished")
    return star_log(tuple(value / normalizer for value in vector)), normalizer


def composed_map(
    creator: Family,
    faces: tuple[int, ...] = FACES,
    kappa: Fraction = KAPPA,
    kinetic_ratio: Fraction = KINETIC_RATIO,
) -> Family:
    """G_X=d**|X|/(1-d**|X|)*(F_X-v_X), on nonempty exact supports."""
    if not isinstance(kinetic_ratio, (int, Fraction)):
        raise TypeError("the kinetic ratio must be exact")
    if not 0 < kinetic_ratio < 1:
        raise ValueError("the free excited kinetic ratio must lie strictly between zero and one")
    transformed, _ = magnetic_map(creator, faces, kappa)
    result = [ZERO]
    for mask, difference in enumerate(subtract(transformed, creator)[1:], start=1):
        ratio = kinetic_ratio ** mask.bit_count()
        result.append(ratio / (1 - ratio) * difference)
    return tuple(result)


def rooted_norm(creator: Family, weight: Fraction = Fraction(2), *, minus_one=False) -> Fraction:
    """Exact rooted l1 norm with weight**|X|; optionally divide by |X|."""
    links = _links(creator)
    if not isinstance(weight, (int, Fraction)):
        raise TypeError("the support weight must be exact")
    if weight <= 0:
        raise ValueError("the support weight must be positive")
    sums = [ZERO] * links
    for mask, value in enumerate(creator[1:], start=1):
        size = mask.bit_count()
        amount = weight**size * abs(value)
        if minus_one:
            amount /= size
        for link in range(links):
            if mask & (1 << link):
                sums[link] += amount
    return max(sums)


def sample_families() -> dict[str, Family]:
    """Three fixed inputs; the two nonzero inputs both have norm exactly 1/128."""
    return {
        "zero": family(LINKS),
        "six_link": family(LINKS, ((63, Fraction(1, 8192)),)),
        "mixed_63": family(
            LINKS,
            (
                (mask, Fraction((-1) ** mask.bit_count(), 4096 * 2 ** mask.bit_count()))
                for mask in range(1, 64)
            ),
        ),
    }


def creator_action(creator: Family, vector: Family) -> Family:
    """Independent basis-action path: apply the sum of nilpotent raising operators.

    This does not call star. It enumerates input basis vectors and checks whether
    each creator's vacuum bra survives on that input.
    """
    _same_size(creator, vector)
    if creator[0]:
        raise ValueError("a raising-operator family has no scalar term")
    result = [ZERO] * len(vector)
    for source, amplitude in enumerate(vector):
        if amplitude:
            for support, coefficient in enumerate(creator[1:], start=1):
                if coefficient and not source & support:
                    result[source | support] += coefficient * amplitude
    return tuple(result)


def creator_exponential_action(creator: Family, vector: Family) -> Family:
    """Apply the finite matrix exponential by repeated raising-operator action."""
    links = _same_size(creator, vector)
    result = list(vector)
    term = vector
    for degree in range(1, links + 1):
        term = tuple(value / degree for value in creator_action(creator, term))
        result = [a + b for a, b in zip(result, term, strict=True)]
    return tuple(result)


def _magnetic_derivative(vector: Family, faces: tuple[int, ...]) -> Family:
    result = [ZERO] * len(vector)
    for face in faces:
        result = [a + b for a, b in zip(result, flip(vector, face), strict=True)]
    return tuple(result)


def flow_tangent_controls(creator: Family, faces: tuple[int, ...] = FACES) -> dict[str, bool]:
    """Compare a normalized star-log differential with direct operator conjugation."""
    vector = star_exp(creator)
    derivative = _magnetic_derivative(vector, faces)
    normalized_derivative = tuple(
        a - derivative[0] * b for a, b in zip(derivative, vector, strict=True)
    )
    negative = tuple(-value for value in creator)
    tangent = star(star_exp(negative), normalized_derivative)

    # Independent operator path: exp(-hat v) V exp(hat v) Omega, then Q.
    omega = family(_links(creator), ((0, ONE),))
    operator_vector = creator_exponential_action(creator, omega)
    conjugated = creator_exponential_action(negative, _magnetic_derivative(operator_vector, faces))
    operator_tangent = (ZERO, *conjugated[1:])
    return {
        "exponential_action": operator_vector == vector,
        "normalized_creator_flow": tangent == operator_tangent,
        "removed_scalar": conjugated[0] == derivative[0],
    }


def theorem_constants() -> dict[str, Fraction]:
    """Recompute the explicit R=1/4 polynomials and the oracle's domain bounds."""
    radius = Fraction(1, 4)
    gamma, tau0, interaction, weight4 = Fraction(1, 2), ONE, ONE, Fraction(16)
    e2, e3, e4 = (sum((Fraction(1, factorial(k)) for k in range(n + 1)), ZERO) for n in (2, 3, 4))
    prefactor = interaction * weight4
    a = 16 * prefactor * e4**2
    b = 32 * prefactor * e3 * e4
    c = a + 5 * radius * b
    ell = 9 * b + 640 * radius * prefactor * (e2 * e4 + e3**2)
    candidates = (
        gamma / (2 * b),
        radius / (2 * tau0 * a),
        gamma * radius / (4 * c),
        gamma / (8 * ell),
    )
    return {
        "A": a,
        "B": b,
        "C": c,
        "L": ell,
        "radius": radius,
        "gamma": gamma,
        "tau0": tau0,
        "u_star": min(candidates),
        "u_upper": KAPPA / (1 - KAPPA),
        "flow_moment_margin": gamma / 2 - KAPPA / (1 - KAPPA) * b,
        "flow_radius_margin": radius / 2 - KAPPA / (1 - KAPPA) * tau0 * a,
        "selfmap_margin": radius / 4 - KAPPA / (1 - KAPPA) * c / gamma,
        "lipschitz_margin": Fraction(1, 2) - 4 * KAPPA / (1 - KAPPA) * ell / gamma,
    }


@dataclass(frozen=True)
class SampleControl:
    input_norms: tuple[Fraction, ...]
    output_norms: tuple[Fraction, ...]
    pair_ratios: tuple[Fraction, ...]
    normalizers_nonzero: bool
    zero_formula: bool

    @property
    def passed(self) -> bool:
        return (
            all(value <= BALL_RADIUS for value in self.input_norms + self.output_norms)
            and all(value <= Fraction(1, 2) for value in self.pair_ratios)
            and self.normalizers_nonzero
            and self.zero_formula
        )


def sample_controls() -> SampleControl:
    """Evaluate each fixed input once; no fixed-point iteration is performed."""
    inputs = tuple(sample_families().values())
    outputs = tuple(composed_map(value) for value in inputs)
    ratios = tuple(
        rooted_norm(subtract(outputs[i], outputs[j])) / rooted_norm(subtract(inputs[i], inputs[j]))
        for i in range(len(inputs))
        for j in range(i)
    )
    normalizers = tuple(magnetic_map(value, FACES, KAPPA)[1] for value in inputs)
    # The three face masks XOR to zero. The exact mixed kicks give
    # (1+kappa^3)I + (kappa+kappa^2)(X_1+X_2+X_3).
    expected_zero = family(
        LINKS,
        ((face, (KAPPA + KAPPA**2) / (15 * (1 + KAPPA**3))) for face in FACES),
    )
    return SampleControl(
        tuple(rooted_norm(value) for value in inputs),
        tuple(rooted_norm(value) for value in outputs),
        ratios,
        all(normalizers),
        outputs[0] == expected_zero and normalizers[0] == 1 + KAPPA**3,
    )
