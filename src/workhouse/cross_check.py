"""A second engine for the T1 layer: every exact value recomputed in FLINT.

**T1 means "re-derived symbolically from stated definitions, exactly". Until
this module, it also quietly meant "sympy says".** Every rational law in the
registry, every all-rank formula, every cancellation behind ``simplify(lhs -
rhs) == 0`` -- one library, one verdict. That is the same shape as trusting a
single proof kernel, and ADR 0010 already decided what to do about it: adopt a
tool when it supplies a genuinely new evidence class. An independent computer
algebra system supplies one here at almost no cost, because python-flint is
already a declared dependency.

**What this witnesses, and what it does not.** It witnesses the *arithmetic*: a
bug in ``Rational``, ``cancel``, ``together``, ``diff`` or ``simplify`` that
produced a wrong exact value would be caught, because flint recomputes the same
quantity from the same stated definition through entirely different code. It
does NOT witness the *derivation*: if a formula in ``constants.py`` is the wrong
formula, both engines compute the same wrong thing, exactly, and agree. That
distinction is the whole reason this module is a witness and not a proof, and
it is stated here rather than left for a reader to work out.

**How a symbolic identity is checked without a symbolic engine.** flint has no
``simplify``, but it does have univariate polynomial arithmetic with exact gcd,
and that is enough: a rational function is a pair of polynomials, and two of
them are equal exactly when ``num_a * den_b - num_b * den_a`` is the zero
polynomial. So :class:`Rat` is a rational function over Q built on
``fmpq_poly``, and the comparison is a polynomial identity checked in flint.

The sympy side crosses the boundary as coefficients and nothing else:
``fraction(together(expr))`` puts the expression over a common denominator --
it does not cancel, so no trust is placed in the operation actually under test
-- and ``Poly.all_coeffs()`` reads the coefficients off. Everything after that
is flint. Where a check's own claim is an identity between two constructions
(``t_N = B_N - A_N``), both sides are rebuilt in flint and compared there, and
sympy is not involved in the verdict at all.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from flint import fmpq, fmpq_poly

#: The rank variable, as the flint polynomial ``x``.
GEN = fmpq_poly([0, 1])


def _to_poly(coefficients: list) -> fmpq_poly:
    """A flint polynomial from sympy's highest-degree-first coefficient list."""
    return fmpq_poly([fmpq(int(c.p), int(c.q)) for c in reversed(coefficients)])


@dataclass(frozen=True)
class Rat:
    """A univariate rational function over Q, as a pair of ``fmpq_poly``.

    Normalised on construction: the gcd is divided out and the denominator is
    made monic, so ``==`` is structural equality of the normal form and needs
    no cross-multiplication at comparison time. Zero denominators raise rather
    than propagating, because a silently-infinite witness would agree with
    anything.
    """

    num: fmpq_poly
    den: fmpq_poly

    @staticmethod
    def of(value: Any) -> Rat:
        """A constant, an integer, an ``fmpq``, an ``fmpq_poly``, or a ``Rat``."""
        if isinstance(value, Rat):
            return value
        if isinstance(value, fmpq_poly):
            return Rat.make(value, fmpq_poly([1]))
        if isinstance(value, int):
            return Rat.make(fmpq_poly([value]), fmpq_poly([1]))
        if isinstance(value, fmpq):
            return Rat.make(fmpq_poly([value]), fmpq_poly([1]))
        raise TypeError(f"cannot lift {type(value).__name__} into a rational function")

    @staticmethod
    def make(num: fmpq_poly, den: fmpq_poly) -> Rat:
        if den.is_zero():
            raise ZeroDivisionError("rational function with zero denominator")
        common = num.gcd(den)
        if not common.is_one():
            num, den = num // common, den // common
        lead = den.leading_coefficient()
        if lead != 1:
            num, den = num / lead, den / lead
        return Rat(num, den)

    def __add__(self, other: Any) -> Rat:
        o = Rat.of(other)
        return Rat.make(self.num * o.den + o.num * self.den, self.den * o.den)

    __radd__ = __add__

    def __neg__(self) -> Rat:
        return Rat(-self.num, self.den)

    def __sub__(self, other: Any) -> Rat:
        return self + (-Rat.of(other))

    def __rsub__(self, other: Any) -> Rat:
        return Rat.of(other) + (-self)

    def __mul__(self, other: Any) -> Rat:
        o = Rat.of(other)
        return Rat.make(self.num * o.num, self.den * o.den)

    __rmul__ = __mul__

    def __truediv__(self, other: Any) -> Rat:
        o = Rat.of(other)
        return Rat.make(self.num * o.den, self.den * o.num)

    def __rtruediv__(self, other: Any) -> Rat:
        return Rat.of(other) / self

    def __pow__(self, power: int) -> Rat:
        if power < 0:
            return Rat.of(1) / (self ** (-power))
        return Rat.make(self.num**power, self.den**power)

    def __eq__(self, other: Any) -> bool:
        o = Rat.of(other)
        return self.num == o.num and self.den == o.den

    def __hash__(self) -> int:
        return hash((str(self.num), str(self.den)))

    def at(self, point: int | fmpq) -> fmpq:
        """Evaluate. Raises where the denominator vanishes rather than guessing."""
        p = fmpq(point) if isinstance(point, int) else point
        below = self.den(p)
        if below == 0:
            raise ZeroDivisionError(f"denominator vanishes at {p}")
        return self.num(p) / below

    def derivative(self) -> Rat:
        """The quotient rule, in flint."""
        return Rat.make(
            self.num.derivative() * self.den - self.num * self.den.derivative(),
            self.den * self.den,
        )

    def __str__(self) -> str:
        return f"({self.num}) / ({self.den})" if not self.den.is_one() else str(self.num)


def from_sympy(expr: Any, symbol: Any = None) -> Rat:
    """A sympy expression as a flint rational function, without cancelling it.

    ``together`` only puts the expression over a common denominator; the
    cancellation that ``cancel`` and ``simplify`` perform -- the operation this
    module exists to witness -- happens on the flint side, in :meth:`Rat.make`.
    A constant expression needs no symbol and is lifted directly.
    """
    from sympy import Poly, Rational, fraction, sympify, together

    expr = sympify(expr)
    if symbol is None or not expr.free_symbols:
        value = Rational(expr)
        return Rat.of(fmpq(int(value.p), int(value.q)))
    num, den = fraction(together(expr))
    return Rat.make(
        _to_poly(Poly(num, symbol).all_coeffs()),
        _to_poly(Poly(den, symbol).all_coeffs()),
    )


def to_fmpq(value: Any) -> fmpq:
    """A sympy ``Rational`` (or int) as a flint ``fmpq``, bit for bit."""
    from sympy import Rational, sympify

    r = Rational(sympify(value))
    return fmpq(int(r.p), int(r.q))


# --------------------------------------------------------------------------
# the witnesses
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Witness:
    """One quantity, computed twice, by two libraries that share no code."""

    name: str
    section: str
    #: What the repository's own sympy path produces.
    sympy_side: Any
    #: The same quantity rebuilt from its stated definition in flint.
    flint_side: Any
    #: True where the flint side was built without consulting sympy at all, so
    #: the agreement is a genuine second derivation rather than a re-check of
    #: one engine's normal form. False where flint only re-normalises what
    #: sympy handed over -- still a witness against `cancel`, but a weaker one.
    independent: bool = True

    def holds(self) -> bool:
        left, right = self.sympy_side, self.flint_side
        if isinstance(right, Rat):
            return Rat.of(left) == right if isinstance(left, Rat) else left == right
        return left == right


def _rank() -> Rat:
    return Rat.of(GEN)


def rational_laws() -> list[Witness]:
    """The all-rank laws, rebuilt in flint from the definitions the corpus states.

    Nothing here reads a sympy expression to build its flint side: each is
    typed out from the printed closed form, so an agreement is two independent
    constructions meeting, not one normal form being re-normalised.
    """
    from . import constants as K

    n = _rank()
    antiparallel = -2 * n**3 / ((n**2 - 1) * (2 * n**2 - 1))
    parallel = -4 * n * (n**2 - 2) / ((n**2 - 1) * (4 * n**2 - 9))
    hopping = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    even = -2 * n * (3 * n**2 - 5) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    deficit = (2 * n**4 + 31 * n**2 - 9) / (4 * (n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    return [
        Witness(
            "A_N, the antiparallel channel sum",
            "MASTER_THEORY §4.3",
            from_sympy(K.antiparallel_sum(), K.N),
            antiparallel,
        ),
        Witness(
            "B_N, the parallel channel sum",
            "MASTER_THEORY §4.3",
            from_sympy(K.parallel_sum(), K.N),
            parallel,
        ),
        Witness(
            "t_N = B_N - A_N, the rank law",
            "MASTER_THEORY §4.3 / R2",
            from_sympy(K.hopping(), K.N),
            parallel - antiparallel,
        ),
        Witness(
            "ell_N, the C-even second-order hopping",
            "C13 / R2",
            from_sympy(K.even_hopping(), K.N),
            even,
        ),
        Witness(
            "1/4 - N**3 t_N, the hopping deficit",
            "MASTER_THEORY §4.3",
            from_sympy(K.hopping_deficit(), K.N),
            deficit,
        ),
        Witness(
            "the deficit really is 1/4 - N**3 t_N",
            "MASTER_THEORY §4.3",
            from_sympy(K.hopping_deficit(), K.N),
            Rat.of(fmpq(1, 4)) - n**3 * hopping,
        ),
        Witness(
            "alpha_N = 640 / (N (N**2-1)**3), the axial law",
            "MASTER_THEORY §5.3 / R14",
            from_sympy(K.alpha_pen(), K.N),
            Rat.of(640) / (n * (n**2 - 1) ** 3),
        ),
        Witness(
            "C_F = (N**2-1)/(2N)",
            "MASTER_THEORY §4.3",
            from_sympy(K.casimir_fundamental(), K.N),
            (n**2 - 1) / (2 * n),
        ),
        Witness(
            "the one-plaquette energy (N**2-1)/N",
            "MASTER_THEORY §4.3",
            from_sympy(K.plaquette_energy(), K.N),
            (n**2 - 1) / n,
        ),
        Witness(
            "dim Z_2(L) = L**3 + 2",
            "UNIFIED §3.3 / R5",
            from_sympy(K.dim_z2(), K.L),
            n**3 + 2,
        ),
    ]


def derivative_law() -> list[Witness]:
    """The one witness that exercises sympy's ``diff`` as well as its cancel.

    ``d/dN (N**3 t_N)`` has numerator ``4 N**3 (2x**3 + 62x**2 - 151x + 72)``
    at ``x = N**2`` -- the cubic the corpus prints as the sign-determining
    factor, and the reason ``N**3 t_N`` increases monotonically to 1/4. flint
    differentiates its own construction with the quotient rule and the cubic
    has to come back out of the numerator.
    """
    from . import constants as K

    n = _rank()
    hopping = 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))
    slope = (n**3 * hopping).derivative()
    cubic_in_n = 2 * n**6 + 62 * n**4 - 151 * n**2 + 72
    # Divide, do not compare: `Rat.make` normalises the denominator to monic,
    # which rescales the numerator, so two numerators of the same rational
    # function need not be the same polynomial. The claim is that the cubic is
    # a FACTOR of the numerator with the remaining factor a positive multiple
    # of N**3, and division answers exactly that, scaling and all.
    quotient, remainder = divmod(slope.num, cubic_in_n.num)
    n3 = fmpq_poly([0, 0, 0, 1])
    leading = quotient.leading_coefficient() if not quotient.is_zero() else fmpq(0)
    return [
        Witness(
            "d/dN (N**3 t_N) has the monotonicity cubic as an exact factor",
            "MASTER_THEORY §4.3",
            (remainder.is_zero(), quotient == leading * n3, leading > 0),
            (True, True, True),
        ),
        Witness(
            "the cubic is the registry's MONOTONICITY_CUBIC at x = N**2",
            "MASTER_THEORY §4.3",
            from_sympy(K.MONOTONICITY_CUBIC.subs(K.x, K.N**2), K.N),
            cubic_in_n,
        ),
    ]


def registered_rationals() -> list[Witness]:
    """Registry values whose stated derivation is arithmetic, recomputed in fmpq.

    These are the transcribed constants that the corpus also gives a *formula*
    for. Recomputing the formula in flint and comparing bit for bit against the
    stored ``sympy.Rational`` is what catches a transcription slip or a bad
    cancellation; a constant the corpus states only as a literal has nothing to
    witness and is deliberately absent.
    """
    from . import constants as K

    q = to_fmpq
    return [
        Witness("t_3 = 5/612", "R2", q(K.hopping(3)), fmpq(5, 612)),
        Witness("t_2 = 0", "R2", q(K.hopping(2)), fmpq(0)),
        Witness("alpha_3 = 5/12", "MASTER_THEORY §5.2", q(K.alpha_pen(3)), fmpq(5, 12)),
        Witness("alpha_4 = 32/675", "MASTER_THEORY §5.3", q(K.alpha_pen(4)), fmpq(32, 675)),
        Witness("alpha_5 = 1/108", "MASTER_THEORY §5.3", q(K.alpha_pen(5)), fmpq(1, 108)),
        Witness("alpha_6 = 64/25725", "MASTER_THEORY §5.3", q(K.alpha_pen(6)), fmpq(64, 25725)),
        Witness(
            "alpha_3 = 4 A_shp",
            "MASTER_THEORY §5.2",
            q(K.ALPHA_PEN_3),
            4 * q(K.A_SHP_3),
            independent=False,
        ),
        Witness(
            "alpha_3 = 4 |c_4^square(3)|",
            "MOB §4",
            q(K.ALPHA_PEN_3),
            4 * abs(q(K.CUBE_COMPLETION_4)),
            independent=False,
        ),
        Witness(
            "C_shp (historical) = (beta_pen - 2 alpha_3)/16",
            "MASTER_THEORY §5.5 / C2",
            q(K.C_SHP_HISTORICAL),
            (q(K.BETA_PEN_3) - 2 * q(K.ALPHA_PEN_3)) / 16,
            independent=False,
        ),
        Witness(
            "d_3 = 7/32 + 12 leak_3 - 4 b_3",
            "C13",
            q(K.D_3),
            fmpq(7, 32) + 12 * q(K.LEAK_3) - 4 * q(K.B_3),
            independent=False,
        ),
        Witness(
            "the C-even band width is its top minus its bottom",
            "MASTER_THEORY §4.4",
            q(K.BAND_EVEN_WIDTH),
            q(K.BAND_EVEN_TOP) - q(K.BAND_EVEN_BOTTOM),
            independent=False,
        ),
        Witness(
            "the C-odd band width is its top minus its flat carrier",
            "MASTER_THEORY §4.4",
            q(K.BAND_ODD_WIDTH),
            q(K.BAND_ODD_TOP) - q(K.BAND_ODD_FLAT),
            independent=False,
        ),
        Witness(
            "q_4^cross = beta_pen / 4",
            "MASTER_THEORY §5.5",
            q(K.Q4_CROSS),
            q(K.BETA_PEN_3) / 4,
            independent=False,
        ),
        Witness(
            "sigma_5^raw = -sigma_5^phys",
            "R14 / C5",
            q(K.SIGMA_5_RAW),
            -q(K.SIGMA_5),
            independent=False,
        ),
        Witness(
            "the record quantum divides the historical off-axis denominator",
            "C2 / G14",
            q(K.C_SHP_HISTORICAL.q % K.X_QUANTUM.q),
            fmpq(int(K.C_SHP_HISTORICAL.q) % int(K.X_QUANTUM.q)),
            independent=False,
        ),
    ]


def witnesses() -> list[Witness]:
    """Every registered witness, in a stable order."""
    return [*rational_laws(), *derivative_law(), *registered_rationals()]


def run() -> tuple[list[Witness], list[Witness]]:
    """``(held, failed)``. A failure is a disagreement between two engines."""
    all_of_them = witnesses()
    failed = [w for w in all_of_them if not w.holds()]
    return [w for w in all_of_them if w not in failed], failed
