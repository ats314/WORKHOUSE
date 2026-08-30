"""Near-Gamma uniformity: turning the G11 caveat into an explicit radius.

The corpus records a warning it never discharges. Fixed-momentum perturbation
theory controls the fourth order at any *given* k, but near Gamma the O(u**2)
isolation gap closes like ``u**2 |k|**2`` while the O(u**4) operator does not
shrink at all. Below some radius the two meet and the ordering of the expansion
fails. Until that radius is named, a coefficient theorem at fixed momentum
"must not be promoted to a uniformly isolated near-Gamma band theorem"
(GLUEBALL Section 18.3).

This module names it.

The competition, exactly
-----------------------
The charge-odd carrier sits at ``E_flat(u)``; the dispersive branches sit at
``E_flat(u) + t(u) q(k)``. So the isolation gap is

    Delta_2(k, u) = t(u) q(k),      q(k) = sum_i 4 sin^2(k_i / 2).

Since ``b_3 > 0``, ``t(u) >= t_3 u**2`` for ``u > 0``, and the fourth-order
operator varies over the zone by at most its bandwidth ``W_4``. Requiring the
fourth-order spread to stay below a fraction ``theta`` of the gap gives

    theta * t_3 u**2 * q(k)  >=  W_4 u**4.

Replacing ``q`` by a rigorous lower bound rather than the small-k
approximation ``|k|**2`` keeps the statement valid across the whole zone:
Jordan's inequality gives ``q(k) >= (4/pi**2) |k|**2``, with equality exactly at
the zone corner, so nothing is given away. Solving,

    |k|  >=  K(W_4, theta) * u,     K = (pi/2) sqrt(W_4 / (theta t_3)).

What this does and does not settle
----------------------------------
It is a *sufficient* criterion built from a conservative bound: outside the
radius the isolated-band statement is safe. It is not the sharp constant, it
says nothing about what happens inside the ball, and it is not the
outward-rounded interval arithmetic over the zone edges that forms the other
half of G11. It converts an unquantified caveat into an explicit exclusion.
"""

from __future__ import annotations

from sympy import Rational, nsimplify, pi, sqrt

from . import constants as K

#: Jordan's inequality constant: q(k) >= JORDAN * |k|**2 on the whole zone.
#: Proof: sin'' = -sin <= 0 on [0, pi], so sin is concave and lies above its
#: chord 2x/pi on [0, pi/2]; substitute x -> x/2 and square. Equality holds at
#: k = 0 and at the corner k_i = pi, so the bound is tight.
JORDAN = 4 / pi**2

#: Default safety factor: the fourth-order spread may occupy at most this
#: fraction of the second-order isolation gap.
DEFAULT_THETA = Rational(1, 2)


def crossover_constant(bandwidth_4, theta=DEFAULT_THETA):
    """K such that the isolated-band statement is safe on |k| >= K*u.

    ``bandwidth_4`` is the fourth-order bandwidth W_4 of whichever kernel is
    being assumed. K enters only through sqrt(W_4).
    """
    w4 = nsimplify(bandwidth_4, rational=True)
    return (pi / 2) * sqrt(w4 / (theta * K.T_MINUS_2))


def conservative_constant(theta=DEFAULT_THETA):
    """The larger K of the two disputed kernels — valid whichever wins.

    C2 is unresolved, so the criterion must not depend on picking a side. It
    does not: K scales as sqrt(W_4), so the kernel with the larger bandwidth
    gives a bound that also holds for the smaller one.
    """
    return max(
        (crossover_constant(w, theta) for w in (K.W4_HISTORICAL_NUM, K.W4_NEW_NUM)),
        key=float,
    )


def max_coupling(theta=DEFAULT_THETA):
    """Above this u the excluded ball swallows the zone and the claim is vacuous.

    The statement only says something when K*u < pi.
    """
    return pi / conservative_constant(theta)


def excluded_zone_fraction(u, theta=DEFAULT_THETA):
    """Fraction of the Brillouin zone [-pi, pi]**3 the criterion gives up."""
    radius = conservative_constant(theta) * nsimplify(u, rational=True)
    if float(radius) >= float(pi):
        return 1.0
    return float((Rational(4, 3) * pi * radius**3) / (8 * pi**3))


def exact_crossover_constant(bandwidth_4, theta=DEFAULT_THETA):
    """The same radius constant, from the exact zone minimum instead of Jordan.

    Jordan's inequality is tight at the zone corner, but the constraint the
    criterion needs is a lower bound on ``q`` over the region ``|k| >= r``, and
    there the minimiser is on a coordinate AXIS, not at the corner. The exact
    minimum is ``4 sin^2(r/2)`` (see the invariant of the same name), so the
    sufficient radius is

        r  >=  2 arcsin( (u/2) sqrt(W_4 / (theta t_3)) ),

    whose leading term is ``sqrt(W_4 / (theta t_3)) * u``. That is smaller than
    the Jordan constant by exactly ``pi/2``: same theorem, sharper constant.
    """
    w4 = nsimplify(bandwidth_4, rational=True)
    return sqrt(w4 / (theta * K.T_MINUS_2))
