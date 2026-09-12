"""Exact Taylor-coefficient counterexample for the literal Balaban corner trees.

The calculation uses only rational arithmetic in Q(i).  It implements the
Balaban CMP 98 equation (15)/(42) through fourth order for SU(2), L=3, on a
12x12 periodic lattice.  The only nonidentity fine links are

    U((0,0), e_0) = exp(i epsilon sigma_x),
    U((0,0), e_1) = exp(i epsilon sigma_y).

Time is coordinate 1.  The fine site reflection is (x,t) -> (x,2-t), which
maps every lower-corner L=3 block to a lower-corner block as a set, and the
induced block-label reflection is (X,T) -> (X,-T).  Balaban's coordinate-order
tree is 0 then 1, exactly the convention in equation (1.7) of CMP 95 (1984).

If block-after-reflection and reflection-after-block differed only by a coarse
gauge transformation, every coarse plaquette trace would have identical Taylor
coefficients.  The script prints the exact nonzero coefficient witnessing the
failure.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import math


ORDER = 4
L = 3
SIZE = 12
DIMENSION = 2
TIME_AXIS = 1
REFLECTION_PARAMETER = L - 1
TREE_ORDER = (0, 1)

Gaussian = tuple[Fraction, Fraction]
Matrix = tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]]
Series = tuple[Matrix, ...]


ZERO: Gaussian = (Fraction(0), Fraction(0))
ONE: Gaussian = (Fraction(1), Fraction(0))
I_UNIT: Gaussian = (Fraction(0), Fraction(1))


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] + b[0], a[1] + b[1]


def gneg(a: Gaussian) -> Gaussian:
    return -a[0], -a[1]


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(a: Gaussian, scalar: Fraction) -> Gaussian:
    return a[0] * scalar, a[1] * scalar


def gconjugate(a: Gaussian) -> Gaussian:
    return a[0], -a[1]


MZERO: Matrix = ((ZERO, ZERO), (ZERO, ZERO))
MIDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))


def madd(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(gadd(a[row][column], b[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mneg(a: Matrix) -> Matrix:
    return tuple(
        tuple(gneg(a[row][column]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mscale(a: Matrix, scalar: Fraction) -> Matrix:
    return tuple(
        tuple(gscale(a[row][column], scalar) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(
            gadd(gmul(a[row][0], b[0][column]), gmul(a[row][1], b[1][column]))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def mdagger(a: Matrix) -> Matrix:
    return tuple(
        tuple(gconjugate(a[column][row]) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def mtrace(a: Matrix) -> Gaussian:
    return gadd(a[0][0], a[1][1])


SZERO: Series = tuple(MZERO for _ in range(ORDER + 1))
SIDENTITY: Series = (MIDENTITY,) + tuple(MZERO for _ in range(ORDER))


def sadd(a: Series, b: Series) -> Series:
    return tuple(madd(a[degree], b[degree]) for degree in range(ORDER + 1))


def sneg(a: Series) -> Series:
    return tuple(mneg(value) for value in a)


def sscale(a: Series, scalar: Fraction) -> Series:
    return tuple(mscale(value, scalar) for value in a)


def smul(a: Series, b: Series) -> Series:
    coefficients = []
    for degree in range(ORDER + 1):
        value = MZERO
        for left_degree in range(degree + 1):
            value = madd(value, mmul(a[left_degree], b[degree - left_degree]))
        coefficients.append(value)
    return tuple(coefficients)


def sdagger(a: Series) -> Series:
    return tuple(mdagger(value) for value in a)


def sexp(argument: Series) -> Series:
    result = SIDENTITY
    power = SIDENTITY
    for degree in range(1, ORDER + 1):
        power = smul(power, argument)
        result = sadd(result, sscale(power, Fraction(1, math.factorial(degree))))
    return result


def slog(unit_near_identity: Series) -> Series:
    displacement = sadd(unit_near_identity, sneg(SIDENTITY))
    result = SZERO
    power = SIDENTITY
    for degree in range(1, ORDER + 1):
        power = smul(power, displacement)
        sign = 1 if degree % 2 else -1
        result = sadd(result, sscale(power, Fraction(sign, degree)))
    return result


def generator_exponential(generator: Matrix) -> Series:
    result = []
    power = MIDENTITY
    for degree in range(ORDER + 1):
        if degree:
            power = mmul(power, generator)
        result.append(mscale(power, Fraction(1, math.factorial(degree))))
    return tuple(result)


I_SIGMA_X: Matrix = ((ZERO, I_UNIT), (I_UNIT, ZERO))
I_SIGMA_Y: Matrix = ((ZERO, ONE), (gneg(ONE), ZERO))


def step(point: tuple[int, int], axis: int, amount: int) -> tuple[int, int]:
    result = list(point)
    result[axis] = (result[axis] + amount) % SIZE
    return tuple(result)  # type: ignore[return-value]


def axial_path(
    root: tuple[int, int], endpoint: tuple[int, int]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    current = root
    path = []
    for axis in TREE_ORDER:
        while current[axis] != endpoint[axis]:
            following = step(current, axis, 1)
            path.append((current, following))
            current = following
    return path


def straight_path(
    root: tuple[int, int], axis: int, amount: int
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    current = root
    path = []
    direction = 1 if amount >= 0 else -1
    for _ in range(abs(amount)):
        following = step(current, axis, direction)
        path.append((current, following))
        current = following
    return path


LINKS = {
    ((0, 0), 0): generator_exponential(I_SIGMA_X),
    ((0, 0), 1): generator_exponential(I_SIGMA_Y),
}


def fine_reflection(point: tuple[int, int]) -> tuple[int, int]:
    result = list(point)
    result[TIME_AXIS] = (REFLECTION_PARAMETER - result[TIME_AXIS]) % SIZE
    return tuple(result)  # type: ignore[return-value]


def block_reflection(point: tuple[int, int]) -> tuple[int, int]:
    result = list(point)
    result[TIME_AXIS] = -result[TIME_AXIS] % SIZE
    return tuple(result)  # type: ignore[return-value]


def fine_link(
    start: tuple[int, int], finish: tuple[int, int], reflected: bool
) -> Series:
    if reflected:
        start, finish = fine_reflection(start), fine_reflection(finish)
    for axis in range(DIMENSION):
        if step(start, axis, 1) == finish:
            return LINKS.get((start, axis), SIDENTITY)
        if step(finish, axis, 1) == start:
            return sdagger(LINKS.get((finish, axis), SIDENTITY))
    raise ValueError((start, finish))


def holonomy(
    path: list[tuple[tuple[int, int], tuple[int, int]]], reflected: bool
) -> Series:
    result = SIDENTITY
    for start, finish in path:
        result = smul(result, fine_link(start, finish, reflected))
    return result


@lru_cache(maxsize=None)
def balaban_link(root: tuple[int, int], axis: int, reflected: bool) -> Series:
    target_root = step(root, axis, L)
    carrier = holonomy(straight_path(root, axis, L), reflected)
    mean_log = SZERO
    for offset_0 in range(L):
        for offset_1 in range(L):
            x = ((root[0] + offset_0) % SIZE, (root[1] + offset_1) % SIZE)
            target_x = step(x, axis, L)
            target_tree = axial_path(target_root, target_x)
            path = (
                axial_path(root, x)
                + straight_path(x, axis, L)
                + [(finish, start) for start, finish in reversed(target_tree)]
            )
            relative_loop = smul(holonomy(path, reflected), sdagger(carrier))
            mean_log = sadd(mean_log, sscale(slog(relative_loop), Fraction(1, L**DIMENSION)))
    return smul(sexp(mean_log), carrier)


def coarse_link(
    start: tuple[int, int], finish: tuple[int, int], reflected_first: bool
) -> Series:
    for axis in range(DIMENSION):
        if step(start, axis, L) == finish:
            return balaban_link(start, axis, reflected_first)
        if step(finish, axis, L) == start:
            return sdagger(balaban_link(finish, axis, reflected_first))
    raise ValueError((start, finish))


def reflected_coarse_link(start: tuple[int, int], finish: tuple[int, int]) -> Series:
    return coarse_link(block_reflection(start), block_reflection(finish), False)


def plaquette_trace(root: tuple[int, int], reflected_first: bool) -> tuple[Gaussian, ...]:
    along_0 = step(root, 0, L)
    along_1 = step(root, 1, L)
    diagonal = step(along_0, 1, L)
    getter = coarse_link if reflected_first else reflected_coarse_link
    if reflected_first:
        links = (
            getter(root, along_0, True),
            getter(along_0, diagonal, True),
            getter(diagonal, along_1, True),
            getter(along_1, root, True),
        )
    else:
        links = (
            getter(root, along_0),
            getter(along_0, diagonal),
            getter(diagonal, along_1),
            getter(along_1, root),
        )
    product = SIDENTITY
    for link in links:
        product = smul(product, link)
    return tuple(mtrace(coefficient) for coefficient in product)


if __name__ == "__main__":
    witness_root = (9, 9)
    block_after_reflection = plaquette_trace(witness_root, True)
    reflection_after_block = plaquette_trace(witness_root, False)
    difference = tuple(
        gadd(block_after_reflection[degree], gneg(reflection_after_block[degree]))
        for degree in range(ORDER + 1)
    )
    print("trace_difference_coefficients", difference)
    assert difference[:4] == (ZERO, ZERO, ZERO, ZERO)
    assert difference[4] == (Fraction(4, 81), Fraction(0))
    print("PASS exact epsilon^4 coefficient = 4/81")
