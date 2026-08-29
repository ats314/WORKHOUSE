"""Exact-form identification, and the budget that decides when a hit is evidence.

Contradiction C2 records the off-axis coefficient ``C_shp`` twice: an exact
rational on the historical side, and on the v10a.26 side a float and nothing
else. The obvious move is to hand that float to an integer-relation algorithm
-- PSLQ, LLL, ``mpmath.identify`` -- and see what comes back. Something always
comes back. That is the problem this module exists to solve.

**The pigeonhole law.** Search for a relation ``sum a_i x_i = 0`` over ``n``
reals with ``|a_i| <= H``. There are ``(2H+1)**n`` coefficient vectors and their
values spread over a fixed range, so the smallest residual any of them attains
is about ``H**-n``. A relation is therefore *guaranteed* to exist at
``H ~ 10**(p/n)`` for ``p`` reliable decimal digits, whatever the numbers are.
Measured here on hash-derived targets with no structure (the check named
``the integer-relation false-positive law``): at ``p = 16`` the median
coefficient found is 3.3e7 for ``n = 2`` (law: 1e8), 1.1e5 for ``n = 3``
(2.2e5), 3.9e3 for ``n = 4`` (1e4), 9.7e2 for ``n = 5`` (1.6e3), 2.9e2 for
``n = 6`` (4.6e2) -- the law, to within the factor of two LLL's approximation
guarantee allows.

So a hit is judged on two questions, neither of which is "is the residual
small" (it always is). **Does it reproduce the target inside the target's own
uncertainty ``h``**, i.e. ``|residual| <= |a_0| h``? And **would a relation
that good have turned up anyway**, which is a counting question with an answer:

    expected = kappa * H**n * h,
    kappa = (6/pi**2) * 2**m * sqrt(3 / (2 pi sum b_i**2))

over a basis of ``m`` constants ``b_i``, with ``n = m + 1``. The margin is
``-log10(expected)``; below three digits the relation was going to be there.
Both the formula and its constant are checked -- against exhaustive enumeration
of the coefficient box, and against the measured smallest window-consistent
height on meaningless targets, where predicted 959/5033/7909 met measured
936/4419/7378.

Nothing here promotes anything: a positive margin makes a T3 *candidate*, and
the candidate's falsifier is that it must survive at higher precision.

**The rational ceiling.** For a plain rational ``p/q`` the count is exact rather
than heuristic. The reduced fractions with ``q <= Q`` in an interval of width
``w`` number ``w * sum_{q<=Q} phi(q) ~ (3/pi**2) w Q**2``, so a value known to
``+-e`` cannot single out any denominator past

    Q_max = sqrt(pi**2 / (6 e))

and below that ceiling the admissible rationals can simply be *enumerated*,
exactly, by Stern-Brocot descent. That converts "no exact form was found" from
a failed search into a stated exclusion.

**Two engines.** The lattice reduction runs in exact integer arithmetic through
python-flint (``fmpz_mat.lll``); the same question goes independently to
mpmath's PSLQ, and a relation one engine finds and the other cannot is a bug in
one of them, not a discovery. PSLQ earns its place twice over, because a
*completed* PSLQ search that returns nothing carries a proved norm bound: "no
relation of norm below 196450 exists at 16 digits" is an exclusion, where
LLL's silence would only have been a silence.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction

from flint import fmpz_mat

#: Reduced fractions with denominator <= Q in an interval of width w number
#: w * sum_{q<=Q} phi(q), and sum_{q<=Q} phi(q) ~ 3 Q**2 / pi**2.
_FAREY_DENSITY = 3.0 / math.pi**2

#: A double carries 53 bits. Nothing recorded as a Python float can support a
#: relation claim past this, whatever precision the search is run at.
DOUBLE_DIGITS = 53 * math.log10(2)  # 15.95...

#: Margin, in decimal digits, below which a relation is a pigeonhole certainty
#: rather than a finding. Three digits = one spurious hit per thousand searches,
#: the same bar `oeis.MAX_EXPECTED` sets for a sequence match.
EVIDENCE_MARGIN = 3.0


# --------------------------------------------------------------------------
# what a recorded number actually knows about itself
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Window:
    """A recorded value and the interval its true value provably lies in.

    ``halfwidth`` is the honest uncertainty, and it is a required argument
    because the tempting default is wrong. The half-ulp of a double is the
    accuracy of the *transcription*, not of the *computation*: the v10a.26
    shape coefficient is printed to 17 digits and reproduces to 7.6e-16, so
    treating its half-ulp of 1.7e-18 as the uncertainty overstates what the
    run knows by a factor of 400 -- and squaring that factor in the ceiling
    below is exactly how a spurious identification gets published.
    """

    value: float
    halfwidth: float
    provenance: str

    def __post_init__(self) -> None:
        if not self.halfwidth > 0:
            raise ValueError("halfwidth must be positive: an exact value needs no window")

    @property
    def digits(self) -> float:
        """Reliable significant decimal digits, capped at what a double holds."""
        rel = self.halfwidth / abs(self.value) if self.value else self.halfwidth
        return min(-math.log10(rel), DOUBLE_DIGITS)

    def interval(self) -> tuple[Fraction, Fraction]:
        """The window as exact rationals, so enumeration never rounds."""
        v, h = Fraction(self.value), Fraction(self.halfwidth)
        return v - h, v + h

    @classmethod
    def half_ulp(cls, value: float, provenance: str) -> Window:
        """The transcription window: every real that rounds to this double.

        Correct only for a value whose *exact* form was rounded once on the way
        in -- a table entry, a printed rational. A computed float is wider.
        """
        return cls(value, math.ulp(value) / 2, provenance)


# --------------------------------------------------------------------------
# rationals: an exact count, and an exact enumeration
# --------------------------------------------------------------------------
def simplest_between(lo: Fraction, hi: Fraction) -> Fraction:
    """The rational of least denominator in ``[lo, hi]``.

    Continued-fraction descent in exact arithmetic. Iterative rather than
    recursive: the float version of this recurses without bound once the
    interval falls below double precision, which is precisely the regime the
    caller is asking about.
    """
    if lo > hi:
        raise ValueError(f"empty interval [{lo}, {hi}]")
    num, den, prev_num, prev_den = 1, 0, 0, 1  # continued-fraction convergents
    while True:
        ceil_lo = -((-lo.numerator) // lo.denominator)
        if ceil_lo <= hi:  # an integer sits in the interval
            p, q = ceil_lo * num + prev_num, ceil_lo * den + prev_den
            return Fraction(p, q)
        floor_lo = lo.numerator // lo.denominator
        num, den, prev_num, prev_den = (
            floor_lo * num + prev_num,
            floor_lo * den + prev_den,
            num,
            den,
        )
        lo, hi = 1 / (hi - floor_lo), 1 / (lo - floor_lo)


def admissible_rationals(
    window: Window, qmax: int, cap: int = 100_000
) -> tuple[list[Fraction], bool]:
    """Every reduced ``p/q`` with ``q <= qmax`` that the window admits.

    Output-sensitive Stern-Brocot descent: the cost is the number of answers,
    not ``qmax``, so a ceiling of 1e9 is as cheap as one of 1e3 when the window
    is narrow. Returns ``(fractions, truncated)``; ``truncated`` is True when
    the cap was reached, and a truncated list is a count, never an inventory.
    """
    lo, hi = window.interval()
    found: list[Fraction] = []
    stack = [(lo, hi)]
    while stack:
        a, b = stack.pop()
        if a > b:
            continue
        s = simplest_between(a, b)
        if s.denominator > qmax:
            continue
        found.append(s)
        if len(found) >= cap:
            return sorted(found), True
        # Split on s. The gap 1/(q * qmax) is below any q' <= qmax spacing, so
        # no admissible fraction is skipped and none is counted twice.
        gap = Fraction(1, s.denominator * qmax + 1)
        stack.append((a, s - gap))
        stack.append((s + gap, b))
    return sorted(found), False


def saturation_denominator(window: Window) -> int:
    """The denominator past which the window constrains nothing at all -- exactly.

    Elementary and free of asymptotics, which is why this is the bound the
    findings are stated in. The admissible numerators for denominator ``q`` are
    the integers in ``[q(x-h), q(x+h)]``, an interval of length ``2hq``. Once
    ``2hq >= 1`` that interval contains an integer whatever ``x`` is, so **every**
    denominator at or above ``ceil(1/(2h))`` admits at least one matching
    fraction. No search, however clever, can exclude a single candidate there.

    One care in the statement: the guaranteed numerator ``p`` need not be
    coprime to ``q``, so this bound promises a fraction *representable over*
    denominator ``q``, not one whose reduced denominator is exactly ``q`` --
    the window ``[-1/4, 1/4]`` saturates at 2, yet its only numerator at
    ``q = 2`` is 0, which reduces to denominator 1. A claim about one specific
    reduced denominator goes through :func:`reduced_match_exists` instead.

    The corollary is the one that decides C2: the historical ``C_shp`` has
    denominator 4405310420659200, and the v10a.26 record saturates at 6.6e14.
    The recorded float rules out nothing at that scale -- and
    :func:`reduced_match_exists` confirms the coprime witness at the
    historical denominator itself.
    """
    return math.ceil(1.0 / (2.0 * window.halfwidth))


def reduced_match_exists(window: Window, q: int) -> bool:
    """Does the window admit a fraction with reduced denominator exactly ``q``?

    Exact and elementary: the admissible numerators are the integers in
    ``[q(x-h), q(x+h)]``, and the fraction has reduced denominator ``q`` iff
    one of them is coprime to ``q``. The saturation bound alone cannot supply
    this -- consecutive integers need not contain one coprime to ``q`` -- so
    exclusion claims about a named denominator check it here rather than
    inferring it from interval length. Cost is the number of admissible
    numerators, so keep ``2h*q`` modest.
    """
    lo, hi = window.interval()
    first = math.ceil(lo * q)
    last = math.floor(hi * q)
    return any(math.gcd(p, q) == 1 for p in range(first, last + 1))


def brute_force_count(window: Window, qmax: int) -> int:
    """The same count as :func:`admissible_rationals`, by trial over every ``q``.

    Deliberately the stupid algorithm. It exists so the Stern-Brocot descent --
    which is subtle enough to be wrong in a way that looks right -- is checked
    against a method with no cleverness in it. Only usable for small ``qmax``.
    """
    lo, hi = window.interval()
    total = 0
    for q in range(1, qmax + 1):
        first = math.ceil(lo * q)
        last = math.floor(hi * q)
        for pnum in range(first, last + 1):
            if math.gcd(abs(pnum), q) == 1:
                total += 1
    return total


def farey_count(window: Window, qmax: int) -> float:
    """Expected number of admissible reduced rationals with ``q <= qmax``.

    ``width * sum_{q<=Q} phi(q)``. Checked against exact enumeration in
    ``tests/test_identify.py``: on the C_shp window at Q = 1e9 it predicts 2800
    and the enumeration finds 2798.
    """
    return 2.0 * window.halfwidth * _FAREY_DENSITY * float(qmax) ** 2


def identification_ceiling(window: Window, expected: float = 1.0) -> float:
    """Largest denominator the window can single out.

    Inverts :func:`farey_count`: past this, more than ``expected`` rationals fit
    and the value discriminates between none of them. This is the number that
    decides whether an identification attempt is worth running at all.
    """
    return math.sqrt(expected / (2.0 * window.halfwidth * _FAREY_DENSITY))


def digits_required(value: float, qmax: int, expected: float = 0.01) -> float:
    """Significant digits a recomputation needs to identify a ``q <= qmax`` rational.

    The actionable direction of the ceiling: not "the search failed" but "a run
    carrying this many digits would decide it". Grows as ``2*log10(qmax)``, so
    the answer is a precision requirement on the next computation, not a longer
    search over the same recorded float.
    """
    halfwidth = expected / (2.0 * _FAREY_DENSITY * float(qmax) ** 2)
    return -math.log10(halfwidth / abs(value))


# --------------------------------------------------------------------------
# integer relations, and what they cost
# --------------------------------------------------------------------------
#: Basis entries are supplied as Python floats, which are dyadic rationals and
#: therefore Q-linearly DEPENDENT as a set. Past a precision threshold the
#: lattice returns that dependency with residual exactly zero -- the most
#: convincing-looking false positive available, and one no type check catches.
#: Measured thresholds against a float basis {1, pi, e, sqrt2, ln2}: residual
#: zero first appears at 36 digits for n = 2, 28 for n = 3, 23 for n = 4 and 5,
#: 22 for n = 6. Every target this tool takes is recorded as a double, so its
#: window never justifies more than ~16 digits and the trap is out of reach --
#: but the cap is asserted rather than assumed, because "out of reach" stops
#: being true the moment someone passes a tighter window.
MAX_FLOAT_BASIS_DIGITS = 20


@dataclass(frozen=True)
class Relation:
    """One integer relation, with the two questions that decide whether it counts.

    **Does it reproduce the target?** Solving the relation for the target gives
    ``x_0 = -(sum_{i>0} c_i x_i)/c_0``, which differs from the recorded value by
    ``residual/c_0``. That has to sit inside the target's own uncertainty, so
    the test is ``|residual| <= |c_0| * halfwidth`` -- and it is a real filter,
    not a formality: over the three registered bases, not one of the relations
    LLL returns for ``C_shp`` reproduces it within its window, missing by
    factors of 12 to 500. Reporting those as near-misses on a digit budget
    would be scoring them on a question nobody asked.

    **Would it have happened anyway?** Counting: for each leading coefficient
    ``c_0`` in ``[1, H]`` the basis sum has to land in a window of width
    ``2 c_0 h``; the ``(2H+1)**m`` basis vectors spread that sum with density
    ``1/(sigma sqrt(2 pi))`` at the origin, ``sigma = H sqrt(sum b_i**2 / 3)``;
    summing over ``c_0`` and multiplying by the ``6/pi**2`` density of coprime
    coefficient tuples gives

        expected = kappa * H**n * halfwidth,
        kappa = (6/pi**2) * 2**m * sqrt(3 / (2 pi sum b_i**2))

    with ``m`` the basis size and ``n = m + 1``. Checked against exhaustive
    enumeration over the whole coefficient box (observed/predicted 0.4 to 1.6,
    linear in ``halfwidth`` as predicted) and against the measured smallest
    window-consistent height over 40 meaningless targets: predicted 959 / 5033 /
    7909 for the three registered bases, measured 936 / 4419 / 7378.
    """

    coefficients: tuple[int, ...]
    residual: float
    halfwidth: float
    basis_norm2: float
    names: tuple[str, ...]

    @property
    def height(self) -> int:
        return max(abs(c) for c in self.coefficients)

    @property
    def allowance(self) -> float:
        """Largest residual that still reproduces the target within its window."""
        return abs(self.coefficients[0]) * self.halfwidth

    @property
    def window_consistent(self) -> bool:
        return abs(self.residual) <= self.allowance

    @property
    def kappa(self) -> float:
        m = len(self.coefficients) - 1
        return (6 / math.pi**2) * 2**m * math.sqrt(3 / (2 * math.pi * self.basis_norm2))

    @property
    def expected(self) -> float:
        """Relations of this height or less expected by counting alone."""
        n = len(self.coefficients)
        return self.kappa * float(self.height) ** n * self.halfwidth

    @property
    def margin(self) -> float:
        """Digits of surprise: ``-log10(expected)``."""
        return -math.log10(self.expected) if self.expected > 0 else math.inf

    @property
    def verdict(self) -> str:
        if not self.window_consistent:
            return "off-window"
        return "candidate" if self.margin >= EVIDENCE_MARGIN else "pigeonhole"

    def __str__(self) -> str:
        pairs = zip(self.coefficients, self.names, strict=True)
        terms = " ".join(f"{c:+d}*{n}" for c, n in pairs if c)
        if not self.window_consistent:
            return (
                f"{terms} = {self.residual:+.3e}  [H={self.height}, misses the target's "
                f"window by {abs(self.residual) / self.allowance:.0f}x -> off-window]"
            )
        return (
            f"{terms} = {self.residual:+.3e}  "
            f"[H={self.height}, expected by counting {self.expected:.2e}, "
            f"margin {self.margin:+.1f} -> {self.verdict}]"
        )


def as_fraction(value: float | Fraction | int) -> Fraction:
    """Exact ``Fraction`` for a float, an int, a Fraction, or a sympy Rational.

    A float converts to the exact binary value it holds, never to a rounded
    decimal: the lattice must reduce the number that was recorded, not a
    prettier one nearby.
    """
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if hasattr(value, "p") and hasattr(value, "q"):  # sympy.Rational
        return Fraction(int(value.p), int(value.q))
    return Fraction(float(value))


def rational_basis_entries(basis: dict[str, float | Fraction]) -> list[str]:
    """The exactly-rational entries of a basis, which must not be searched over.

    A basis of rationals is Q-linearly dependent by construction, so LLL returns
    a relation *among the basis elements* with a zero coefficient on the target
    and a residual of exactly zero -- ``4*(5/48) - 5/12 = 0`` is the one this
    corpus hands you first. It looks like a spectacular hit and says nothing
    about the target. Rational entries contribute exactly one degree of freedom
    between them (the constant 1), and the only question they can answer --
    "is the target rational?" -- is settled exactly, without search, by
    :func:`admissible_rationals`.

    Exactness is read from the type, not guessed from the value: pass a
    ``Fraction`` (or ``sympy.Rational``, whose ``p``/``q`` this accepts) for a
    constant that is exact, and a ``float`` for one the corpus records only
    numerically. A float that happens to be near a simple rational is still a
    float, and this repository's whole boundary rule is that the two never blur.
    """
    return [name for name, value in basis.items() if not isinstance(value, float)]


def lll_relations(
    values: list[float], digits: int, *, limit: int = 8
) -> list[tuple[tuple[int, ...], Fraction]]:
    """Integer relations among ``values``, by exact-integer LLL.

    The standard relation lattice: row ``i`` is ``e_i`` followed by
    ``round(x_i * 10**digits)``. Reducing it in exact integer arithmetic
    (python-flint, ADR 0010) leaves short vectors whose leading block is a
    candidate coefficient tuple. No floating point enters the reduction, so the
    search itself cannot be the source of an error.
    """
    n = len(values)
    scale = 10**digits
    rows = [
        [1 if j == i else 0 for j in range(n)] + [round(as_fraction(x) * scale)]
        for i, x in enumerate(values)
    ]
    reduced = fmpz_mat(rows).lll()
    out = []
    for i in range(reduced.nrows()):
        coeffs = tuple(int(reduced[i, j]) for j in range(n))
        if not any(coeffs):
            continue
        residual = sum(c * as_fraction(x) for c, x in zip(coeffs, values, strict=True))
        out.append((coeffs, residual))
    # Ranked by residual, which is the relation a caller would actually quote,
    # and tie-broken by height. Ranking by coefficient height instead promotes
    # short vectors that are not relations at all, and it understates the
    # measured false-positive height by an order of magnitude -- in the
    # reassuring direction, which is the worst way for a guard to be wrong.
    out.sort(key=lambda cr: (abs(cr[1]), max(abs(c) for c in cr[0])))
    return out[:limit]


def pslq_relation(
    values: list[float], digits: int, maxcoeff: int = 10**9, maxsteps: int = 5000
) -> dict:
    """The same question put to mpmath's PSLQ, as an independent engine.

    Returns ``{"relation": tuple|None, "norm_bound": float|None, "exhausted": bool}``.
    Two details of mpmath's API are load-bearing and both default badly:

    * ``tol`` defaults to ``2**-int(0.75*prec)``, a BINARY power -- at
      ``mp.dps = 15`` that is 1.8e-12, an 11.7-digit search, not a 15-digit one.
      It is always passed explicitly here.
    * ``maxsteps`` defaults to 100, and at that budget PSLQ returns ``None`` on
      a six-element vector in 24 of 25 cases where a relation exists. A ``None``
      then means "ran out of steps", not "there is no relation" -- opposite
      epistemic states, and mpmath prints its "Norm bound:" line on BOTH exits,
      so the line's presence does not tell them apart. The discriminator is the
      bound itself: mpmath breaks out early precisely when its proved lower
      bound on any relation's norm reaches ``maxcoeff``, so ``norm >= maxcoeff``
      is the completed search and anything less is exhaustion. Only the former
      establishes that no relation of norm below the bound exists at this
      tolerance, and only the former is reported as an exclusion here.
    """
    import contextlib
    import io
    import re as _re

    from mpmath import mp, pslq

    old_dps = mp.dps
    buffer = io.StringIO()
    try:
        mp.dps = max(digits + 10, 30)
        with contextlib.redirect_stdout(buffer):
            found = pslq(
                [mp.mpf(v) for v in values],
                tol=mp.mpf(10) ** (-digits),
                maxcoeff=maxcoeff,
                maxsteps=maxsteps,
                verbose=True,
            )
    finally:
        mp.dps = old_dps
    trace = buffer.getvalue()
    match = _re.search(r"Norm bound:\s*([\d.eE+-]+)", trace)
    bound = float(match.group(1)) if match else None
    return {
        "relation": tuple(int(c) for c in found) if found else None,
        "norm_bound": bound,
        # An exclusion only where mpmath's proved lower bound actually reached
        # the coefficient ceiling. Below it, the search stopped because it ran
        # out of steps and has proved nothing.
        "exhausted": found is None and not (bound is not None and bound >= maxcoeff),
    }


def scale_digits(window: Window) -> int:
    """Decimal places the relation lattice must resolve.

    The lattice's last column is an ABSOLUTE residual, so the scale is set by
    the target's absolute uncertainty and not by its significant digits.
    Getting this wrong is not a false positive but something subtler: at
    10**13 for a target whose window is 7.6e-16, every relation LLL returns
    misses that window by 100x to 1600x, and the search quietly answers a
    different question than the verdict is written against.
    """
    return math.ceil(math.log10(1.0 / window.halfwidth))


def sweep(
    target: Window,
    basis: dict[str, float | Fraction],
    *,
    digits: int | None = None,
    limit: int = 6,
) -> list[Relation]:
    """Relations between ``target`` and ``basis``, each carrying its own verdict.

    Two things are refused rather than reported, because both produce hits that
    read as discoveries and are not:

    * a basis with more than one exactly-rational entry (see
      :func:`rational_basis_entries`) -- use :func:`admissible_rationals`;
    * any relation whose coefficient on the target is zero, which is a statement
      about the basis alone.

    A third is reported but labelled: a relation that does not reproduce the
    target inside its own window is ``off-window``, and no budget applies to it.
    """
    exact = rational_basis_entries(basis)
    if len(exact) > 1:
        raise ValueError(
            f"basis is Q-linearly dependent through its exact entries {exact}: "
            "LLL will return a relation among them and not about the target. "
            "Keep at most one rational entry (the constant 1) and settle "
            "rationality with admissible_rationals() instead."
        )
    p = scale_digits(target) if digits is None else digits
    if p > MAX_FLOAT_BASIS_DIGITS and len(exact) < len(basis):
        raise ValueError(
            f"{p} digits against a float basis: past ~22 the lattice returns the "
            "basis's own dyadic dependency with residual exactly zero. Supply the "
            "basis as exact Fractions at that precision, or narrow the window."
        )
    names = ("target", *basis)
    values = [target.value, *basis.values()]
    norm2 = sum(float(v) ** 2 for v in basis.values())
    out = []
    for coeffs, residual in lll_relations(values, p, limit=limit * 4):
        if coeffs[0] == 0:
            continue
        out.append(Relation(coeffs, float(residual), target.halfwidth, norm2, names))
    # Window-consistent relations first, then by how surprising they are.
    out.sort(key=lambda r: (not r.window_consistent, -r.margin))
    return out[:limit]


# --------------------------------------------------------------------------
# the recorded floats worth putting to an identification, and what they know
# --------------------------------------------------------------------------
def targets() -> dict[str, Window]:
    """Registered float targets, keyed by the name ``--claim`` takes.

    The halfwidth is the whole argument, so each one is sourced rather than
    defaulted. Taking the half-ulp of the double instead would overstate what
    the v10a.26 run knows by three orders of magnitude -- and the ceiling goes
    as the square root of the halfwidth, so the overstatement lands squarely on
    the conclusion.
    """
    from . import constants as K

    return {
        # The one genuinely open item, windowed by the run's OWN shift-invariance
        # failure: the transcript prints the shape fit twice, before and after a
        # scalar diagonal shift of 11.17343231638178, and a scalar shift moves
        # `rest` and nothing else -- Phi_C(0) = 0. C moves by 4.6e-15 anyway.
        # That is six times wider than the cross-implementation agreement
        # (7.6e-16 against the cold rerun) suggests, and the conservative number
        # is the honest one.
        "C_shp": Window(
            K.C_SHP_NEW_NUM,
            4.6e-15,
            "v10a.26 shift-invariance violation, 15_hour_RUN.txt [13] vs [17] (C2, G3)",
        ),
        # A = 5/48 is agreed by both kernels, which makes this the positive
        # control: an identification whose answer is known independently.
        "A_shp": Window(
            K.A_SHP_3_NUM,
            K.SEALED_CORE_TOLERANCE,
            "v10a.26 sealed core, the corpus's own stated bound (GLUEBALL §10)",
        ),
        # alpha = 4A inherits four times A's deviation, which is exactly why the
        # corpus's aggregate bound does not cover it -- the registered FINDING
        # in the sealed-core suite. Windowed honestly here, so the same fact
        # shows up as "5/12 is admissible after all".
        "alpha_pen": Window(
            K.ALPHA_PEN_3_NUM,
            4 * K.SEALED_CORE_TOLERANCE,
            "v10a.26 sealed core; 4x the A bound, per the alpha_new FINDING",
        ),
        # The blind Gamma-point scalar. Window from the run's own spread across
        # the Gamma evaluations, which is what the transcript reports.
        "m_Gamma": Window(
            K.M_GAMMA_4_NUM,
            2.1671553440683056e-13,
            "v10a.26 rooted oracle, the run's own gamma_spread",
        ),
    }


#: Named search bases for :func:`sweep`, each with at most one rational entry.
#:
#: A note on what these are for. Every coefficient in this program comes out of
#: Haar integration over SU(N) -- Weingarten values, resolvent denominators,
#: lattice sums -- and all of that is rational arithmetic. There is no reason to
#: expect pi or a zeta value in ``C_shp`` at all. The bases exist to TEST that
#: expectation rather than assume it, and the expected outcome is exactly what
#: they return: nothing that clears its own digit budget.
def bases() -> dict[str, dict[str, float]]:
    return {
        "circle": {
            "1": 1.0,
            "pi": math.pi,
            "sqrt3": math.sqrt(3),
            "pi/sqrt3": math.pi / math.sqrt(3),
        },
        "logs": {"1": 1.0, "log2": math.log(2), "log3": math.log(3)},
        "zeta": {"1": 1.0, "pi^2": math.pi**2, "zeta3": 1.2020569031595942854},
    }
