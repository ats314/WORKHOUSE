"""Exact controls for the selected-inverse repair and its stated limitations.

The complete spectral obstruction and conditional form reduction are analytic
proofs. These controls do not prove the interacting Wilson estimate W6.
"""

from __future__ import annotations

from sympy import (
    Matrix,
    Rational,
    chebyshevu,
    diag,
    diff,
    eye,
    kronecker_product,
    simplify,
    symbols,
    zeros,
)

from ._core import _suite

selected = _suite("Wilson spatial inverse: compact spectral obstruction and selected repair")
CITE = "WILSON_SELECTED; G19"


@selected.check("SU2 character kinetic normalization uses all four plaquette links", CITE + " W2")
def _character_kinetic():
    z, t = symbols("z t", real=True)
    generating = 1 / (1 - 2 * z * t + t**2)
    good = (
        simplify(
            (1 - z**2) * diff(generating, z, 2)
            - 3 * z * diff(generating, z)
            + t**2 * diff(generating, t, 2)
            + 3 * t * diff(generating, t)
        )
        == 0
    )
    for n in range(9):
        character = chebyshevu(n, z)
        laplacian = ((1 - z**2) * diff(character, z, 2) - 3 * z * diff(character, z)) / 4
        good &= simplify(-2 * laplacian - Rational(n * (n + 2), 2) * character) == 0
    return good, (
        "The rational generating function satisfies the character differential identity; "
        "Chebyshev U_n for n=0,...,8 independently satisfies the SU2 radial Laplacian "
        "equation: four original links give -2 Delta eigenvalue n(n+2)/2"
    )


@selected.check(
    "FINDING: compact Wilson spectral growth defeats a full Gaussian upper form bound",
    CITE + " W2-W3",
    rests_on=("SU2 character kinetic normalization uses all four plaquette links",),
)
def _spectral_growth():
    g, r, n = Rational(1, 4), 1, 1024
    lower = g**2 * n * (n + 2) / 2 - 4 / g**2
    upper = (1 + g) * 4 * (n + r)
    # The analytic min-max proof chooses k>=max(C,1), m>=1/g and n=32*k*m^2>=r.
    k, m = symbols("k m", integer=True, positive=True)
    margin = simplify((512 * k**2 - 4) * m**2 - 256 * k**2 * m**2)
    return (
        lower == 32768
        and upper == 5125
        and lower > upper
        and simplify(margin - (252 + 256 * (k**2 - 1)) * m**2) == 0,
        "g=1/4, rank r=1, n=1024: actual min-max lower bound 32768 exceeds "
        "the proposed Gaussian upper bound 5125. The all-C analytic margin "
        "is [252+256(k^2-1)]m^2>0 for integer k,m>=1; finite-rank retention only",
        {"WILSON_COMPACT_LOWER_WITNESS": lower, "WILSON_GAUSSIAN_UPPER_WITNESS": upper},
    )


@selected.check(
    "Selected inverse variation can be bounded with unbounded relative perturbation",
    CITE + " W4-W5",
)
def _selected_diagonal():
    g, n = symbols("g n", positive=True)
    identity = simplify(1 / n - 1 / (n + g**2 * n**2) - g**2 / (1 + g**2 * n)) == 0
    t = Matrix([1, 2, 1])
    f0 = diag(1, 2, 3)
    good = identity
    for coupling in (Rational(1, 4), Rational(1, 2), Rational(2)):
        fg = f0 + coupling**2 * f0**2
        loss = (t.T * (f0.inv() - fg.inv()) * t)[0]
        good &= 0 < loss <= coupling**2 * (t.T * t)[0]
    relative = simplify((n + g**2 * n**2 - n) / n)
    return good and relative == g**2 * n, (
        "Exact diagonal resolvent identity gives g^2/(1+g^2 n) per coefficient "
        "while the relative perturbation is g^2 n; three rational couplings "
        "check 0<selected loss<=6g^2 independently by matrix inversion"
    )


@selected.check(
    "FINDING: true vacuum subtraction reverses the bare positive-perturbation inverse order",
    CITE + " section 4",
)
def _vacuum_order():
    h0, v, g = diag(0, 2), diag(100, 0), Rational(1, 20)
    hg = h0 + g**2 * v
    vacuum = min(hg.eigenvals())
    f0, fg = h0[1, 1], hg[1, 1] - vacuum
    return (
        all(value >= 0 for value in v.eigenvals())
        and vacuum == Rational(1, 4)
        and fg == Rational(7, 4)
        and 1 / fg == Rational(4, 7) > 1 / f0,
        "H0=diag(0,2), V=diag(100,0)>=0, g=1/20: true vacuum is 1/4, "
        "so fast energy 7/4<2 and inverse 4/7>1/2 despite bare positivity",
    )


def _tensor(factors):
    out = Matrix([[1]])
    for factor in factors:
        out = kronecker_product(out, factor)
    return out


@selected.check(
    "FINDING: spectator reference moments grow despite an exact unit excitation gap",
    CITE + " section 4",
)
def _spectator_moments():
    g = Rational(1, 2)
    p = g**2 / (1 + g**2)
    ground = Matrix([[1, g], [g, g**2]]) / (1 + g**2)
    excited = Matrix([[g**2, -g], [-g, 1]]) / (1 + g**2)
    rotation = Matrix([[1, -g], [g, 1]])
    good = rotation.T * ground * rotation / (1 + g**2) == diag(1, 0)
    for count in range(1, 5):
        rho = _tensor([excited] + [ground] * (count - 1))
        h, number = zeros(2**count), zeros(2**count)
        for i in range(count):
            factors = [eye(2)] * count
            factors[i] = eye(2) - ground
            h += _tensor(factors)
            factors[i] = diag(0, 1)
            number += _tensor(factors)
        mean = 1 + (count - 2) * p
        second = mean**2 + count * p * (1 - p)
        good &= (
            rho.trace() == 1
            and rho * rho == rho
            and h * rho == rho
            and (number * rho).trace() == mean
            and (number**2 * rho).trace() == second
        )
    return good, (
        "Independent exact tensor matrices for M=1,...,4 and g=1/2 verify H rho=rho, "
        "<N0>=1+(M-2)p and <N0^2>=<N0>^2+Mp(1-p), p=1/5. "
        "The all-M product proof has quadratic spectator growth; local rotation "
        "repairs the product vacuum, with no coupled-Wilson estimate inferred"
    )
