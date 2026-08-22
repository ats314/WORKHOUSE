"""Certified numerical enclosures for T2 checks (Arb ball arithmetic).

The working agreement's sharpest numerical rule — never widen a tolerance —
has a quiet dual: never trust a precision that is merely asserted. A check
that compares through ``evalf(25)`` is trusting that 25 digits were enough;
nothing proves it. Arb balls carry a midpoint and a radius with a machine
inclusion guarantee, and python-flint's comparisons return True only when
the enclosures are disjoint, so an inequality certified here is a theorem
of interval arithmetic rather than a hope about rounding.

This module does NOT create a new tier (ADR 0010). An enclosure-certified
check is still T2: "certified" qualifies the comparison, never the claim.
Rule 5 of the working agreement stands — certified is not a synonym for
proved.

Entry semantics, the part worth being paranoid about:

- a Python int or float enters EXACTLY (a double is a dyadic rational);
- a ``sympy.Rational`` enters as p/q evaluated in ball arithmetic, so the
  true rational lies inside the returned enclosure;
- nothing else is accepted, because a silent ``str`` or ``sympy.Float``
  path is exactly the exact/float boundary bug ``test_constants.py``
  guards against.
"""

from __future__ import annotations

from flint import arb, ctx
from sympy import Rational

#: Working precision, in bits, for every enclosure built here. 128 bits is
#: ~38 decimal digits — far beyond any corpus double — and the point is not
#: the size but that the radius is CARRIED, so "was it enough?" is answered
#: by the ball itself.
PREC = 128
ctx.prec = PREC


def ball(value: int | float | Rational) -> arb:
    """An enclosure of ``value``, entered exactly (see module docstring)."""
    if isinstance(value, Rational):
        return arb(int(value.p)) / arb(int(value.q))
    if isinstance(value, (int, float)):
        return arb(value)
    raise TypeError(
        f"ball() accepts int, float, or sympy.Rational, not {type(value).__name__}: "
        "convert deliberately at the call site, never implicitly"
    )


def certified_lt(a: arb, b: arb) -> bool:
    """True only if a < b is PROVABLE (enclosures disjoint). Overlap -> False."""
    return bool(a < b)


def certified_closer(x: arb, near: arb, far: arb) -> bool:
    """True only if |x - near| < |x - far| is provable."""
    return bool(abs(x - near) < abs(x - far))


def describe(x: arb) -> str:
    """Midpoint and radius, for detail lines a reader can argue with."""
    return x.str(20, radius=True)


def bessel_i(order: int, x: arb) -> arb:
    """Enclosure of the modified Bessel function ``I_order(x)``.

    Lives here rather than at the call site because ``src/workhouse/CLAUDE.md``
    makes this module the only sanctioned route to Arb: a second import of
    ``flint`` is a second place where the working precision could be set, and
    the whole point of the enclosure discipline is that there is exactly one.

    ``I_{-n} = I_n`` for integer order, so the sign of ``order`` is ignored.
    """
    return x.bessel_i(abs(order))
