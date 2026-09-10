"""September 8 anisotropy result, re-derived against the complete record kernel.

The original research package is preserved in the recent-integration run.
The induced sixth-order term is for the displayed fourth-order truncation;
it is not the full sixth-order Hamiltonian. Polynomial identities are T1,
and the finite-order spectral probes have their own explicit T2 tolerance.
"""

from __future__ import annotations

from fractions import Fraction as F

import mpmath as mp
import sympy as sp

from .. import kernel_orbits as KO
from ._core import _suite
from .gamma_isolation import _HODGE_ALGEBRA, _forms, _q_a_records

anisotropy = _suite("anisotropy variance: full-kernel mixing and induced sixth order")
_CITE = "RECENT_ANISOTROPY; THEORY.md sections 2-5; G9; G11; G14; G18"
_ALGEBRA = "anisotropy variance is exactly the simplex pair sum and cubic shape invariant"
_KERNEL = "anisotropy mixing residual matches the full assembled Laurent kernel"
_COEFFICIENT = "anisotropy induced sixth-order coefficient is minus four C squared over t3"


def _kernel():
    form = _forms()["assembled"]
    scalar = 2 * form["nu~"] + 16 * form["u"] + 4 * form["pi~"] + form["sigma~"]
    return form["C"], KO.combine((1, KO.hodge_records(form)), (-scalar, KO.identity()))


@anisotropy.check(_ALGEBRA, _CITE)
def _simplex_algebra():
    x, y, z = sp.symbols("x y z", nonnegative=True)
    pair = x * y * (x - y) ** 2 + x * z * (x - z) ** 2 + y * z * (y - z) ** 2
    variance = x**3 + y**3 + z**3 - (x**2 + y**2 + z**2) ** 2
    e2, e3 = x * y + x * z + y * z, x * y * z
    remainders = [
        sp.expand(expr.subs(z, 1 - x - y))
        for expr in (variance - pair, pair - e2 - 3 * e3 + 4 * e2**2)
    ]
    holdout = pair.subs({x: sp.Rational(1, 6), y: sp.Rational(1, 3), z: sp.Rational(1, 2)})
    return (
        remainders == [0, 0] and holdout == sp.Rational(5, 324),
        (
            f"simplex polynomial remainders={remainders}; pair sum at (1/6,1/3,1/2)={holdout}; "
            "each pair term is nonnegative on the nonnegative simplex, "
            "with shape coefficients 1:3:-4"
        ),
        {"ANISOTROPY_VARIANCE_HOLDOUT": holdout},
    )


@anisotropy.check(_KERNEL, _CITE, rests_on=(_HODGE_ALGEBRA, _ALGEBRA))
def _full_kernel_residual():
    c, h = _kernel()
    q = KO.bloch_matrix(_q_a_records())[KO.PLANES[0]][KO.PLANES[0]]
    mean, second = KO.bloch(h.items()), KO.bloch(KO.compose(h, h).items())
    lhs = KO._add(KO._mul(q, second), KO._mul(mean, mean), -1)
    coordinates = []
    for axis in range(3):
        terms = {(0, 0, 0): F(2)}
        for sign in (-1, 1):
            exponent = [0, 0, 0]
            exponent[axis] = sign
            terms[tuple(exponent)] = F(-1)
        coordinates.append(terms)
    rhs = {}
    for i in range(3):
        for j in range(i + 1, 3):
            delta = KO._add(coordinates[i], coordinates[j], -1)
            term = KO._mul(KO._mul(coordinates[i], coordinates[j]), KO._mul(delta, delta))
            rhs = KO._add(rhs, term, 4 * c * c)
    lhs = {k: v for k, v in lhs.items() if v}
    rhs = {k: v for k, v in rhs.items() if v}
    return lhs == rhs and bool(lhs), (
        f"all {len(lhs)} nonzero Laurent coefficients agree exactly; C={c}; "
        "q*(psi*H^2*psi)-(psi*H*psi)^2=4C^2 sum(i<j) ai aj (ai-aj)^2; "
        "division by q^2 for q>0 gives ||QHp||^2=4C^2 q^2 V"
    )


@anisotropy.check(_COEFFICIENT, _CITE, rests_on=(_KERNEL,))
def _induced_coefficient():
    c, _ = _kernel()
    coefficient = -4 * c * c / F(5, 612)
    expected = F(-169924002729806205028788409, 619343593697933825385600000)
    return (
        coefficient == expected and coefficient < 0,
        (
            f"C={c}, t3=5/612, induced coefficient={coefficient}; "
            "this multiplies q*V in the fourth-order matrix's virtual-mixing term; "
            "direct sixth-order contributions remain a separate G9 input"
        ),
        {"ANISOTROPY_INDUCED_SIXTH": coefficient},
    )


@anisotropy.check(
    "anisotropy finite-order overlap and energy bounds hold in scaled spectral probes",
    _CITE,
    tier=2,
    rests_on=(_KERNEL, _COEFFICIENT),
)
def _spectral_bounds():
    with mp.workdps(80):
        c, h = _kernel()
        hm, lm, carrier = KO.bloch_matrix(h), KO.bloch_matrix(KO.down_laplacian()), KO.carrier()

        def rational(value):
            return mp.mpf(value.numerator) / value.denominator

        def evaluate(poly, momentum):
            return sum(
                rational(v) * mp.expj(sum(e[i] * momentum[i] for i in range(3)))
                for e, v in poly.items()
            )

        def matrix(records, momentum):
            return mp.matrix(
                [[evaluate(records[o][i], momentum) for i in KO.PLANES] for o in KO.PLANES]
            )

        tolerance = mp.mpf("1e-28")
        max_error, probes = mp.mpf(0), 0
        points = [
            (".4", ".8", "1.2"),
            (".9", ".3", ".1"),
            (".4", "0", "0"),
            (".4", ".4", "0"),
            (".4", ".4", ".4"),
            ("1e-12", "2e-12", "3e-12"),
        ]
        for point in points:
            k = tuple(map(mp.mpf, point))
            av = [4 * mp.sin(t / 2) ** 2 for t in k]
            q = sum(av)
            x = [a / q for a in av]
            variance = sum(
                x[i] * x[j] * (x[i] - x[j]) ** 2 for i in range(3) for j in range(i + 1, 3)
            )
            p = mp.matrix([evaluate(carrier[o], k) for o in KO.PLANES]) / mp.sqrt(q)
            scaled_h, scaled_l = matrix(hm, k) / q, matrix(lm, k) / q
            for coupling in (".05", ".1", ".19"):
                u, t3, ci = mp.mpf(coupling), mp.mpf(5) / 612, mp.mpf(5) / 48
                delta = t3 - 2 * ci * u**2
                operator = t3 * u**2 * scaled_l + u**4 * scaled_h
                values, vectors = mp.eigh(operator)
                deficit = 1 - abs((p.H * vectors[:, 0])[0]) ** 2
                lowering = (p.H * operator * p)[0].real - values[0]
                overlap_bound = 4 * rational(c) ** 2 * u**4 * variance / delta**2
                energy_bound = 4 * rational(c) ** 2 * u**6 * variance / delta
                error = max(deficit - overlap_bound, lowering - energy_bound, -lowering, 0)
                max_error, probes = max(max_error, error), probes + 1
        return max_error <= tolerance, (
            f"{probes} probes at 80 digits, including q near 1e-23 and three nodal families; "
            f"largest violation={mp.nstr(max_error, 8)}, tolerance={tolerance}; "
            "energy is scaled by q before diagonalization; finite-order in-sector bounds only"
        )
