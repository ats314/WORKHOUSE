"""G14: why B_shp and D_shp vanish, proposed as a degree bound.

The corpus records the vanishing as an observation without a reason:

    B_shp_N = D_shp_N = 0 at every solved rank (N = 3,4,5,6 and stable N >= 7):
    the L^-4 tier allowed by cubic symmetry is not selected by the microscopic
    contraction — a dynamical selection rule with no proved mechanism.

This module proposes one, and makes it falsifiable.

Step 1 — the tier is a degree
-----------------------------
Clearing the denominator in the generic cubic-invariant ansatz,

    q * eps_4 = c_0 q + A_shp q^2 + 4 C_shp e_2 + B_shp (q e_2) + D_shp e_3,

and the five basis elements stratify by total degree in the a_i:

    degree 1:  q                 -> c_0
    degree 2:  q^2, e_2          -> A_shp, C_shp     (both nonzero)
    degree 3:  q e_2, e_3        -> B_shp, D_shp     (both zero)

Since a_i ~ L^-2, degree 3 is exactly the L^-4 tier. So "the L^-4 tier is not
selected" and "the numerator has no degree-3 part" are the same statement.

Step 2 — one hop costs one degree
---------------------------------
The face-to-link Bloch incidence is the curl matrix ``partial_2 = [d]_x`` with
``d_i = exp(i k_i) - 1``, whose entries are *linear* in d. It satisfies

    B B^dagger = q I - d conj(d)^T,        eigenvalues (0, q, q),

which reproduces the recorded second-order C-odd spectrum
``{E_flat, E_flat + t_N q(k) (x2)}`` exactly, with the flat carrier as the
d-direction. Each entry is bilinear in (d, conj d): one power of a.

Step 3 — the bound
------------------
Order ``u^(2r)`` is r hops, hence 2r vertices, each contributing at most one
power of d or conj(d). So the numerator has degree at most r in the a_i:

    r = 1, O(u^2):  degree <= 1  ->  span{q}                 observed: t_N q
    r = 2, O(u^4):  degree <= 2  ->  span{q, q^2, e_2}       forces B = D = 0
    r = 3, O(u^6):  degree <= 3  ->  adds {q e_2, e_3}       B, D may turn on

The r = 1 row is a genuine check, not a restatement: cubic symmetry would
permit a degree-2 second-order term and none appears.

Status
------
A conjectured mechanism, not a theorem. It rests on two assumptions, both
stated so they can be attacked:

1. every perturbative vertex is linear in d or conj(d) — true of the incidence
   entries, but the full amplitude also carries colour factors and resolvents;
2. the energy denominators are k-independent — true at the one-plaquette level,
   where the unperturbed flux energies do not disperse.

If either fails the count shifts. The prediction below is what makes this worth
recording rather than speculating about.
"""

from __future__ import annotations

from dataclasses import dataclass

from sympy import Matrix, Poly, expand, eye, symbols

#: Total degree in the a_i of each numerator basis element, and the coefficient
#: it carries. This is the whole reformulation in one table.
NUMERATOR_BASIS = {
    "q": (1, "c_0"),
    "q**2": (2, "A_shp"),
    "e_2": (2, "C_shp"),
    "q*e_2": (3, "B_shp"),
    "e_3": (3, "D_shp"),
}

#: The coefficients that vanish, and the degree that explains them.
VANISHING = frozenset({"B_shp", "D_shp"})
VANISHING_DEGREE = 3


def numerator_degrees():
    """Degree of each basis element, computed rather than asserted."""
    a1, a2, a3 = symbols("a1 a2 a3", nonnegative=True)
    q = a1 + a2 + a3
    e2 = a1 * a2 + a1 * a3 + a2 * a3
    e3 = a1 * a2 * a3
    exprs = {"q": q, "q**2": q**2, "e_2": e2, "q*e_2": q * e2, "e_3": e3}
    return {name: Poly(expand(expr), a1, a2, a3).total_degree() for name, expr in exprs.items()}


def incidence_identity():
    """Verify B B^dagger = q I - d conj(d)^T for the curl incidence matrix.

    Returns the residual matrix; the zero matrix means the identity holds.
    """
    d1, d2, d3, c1, c2, c3 = symbols("d1 d2 d3 c1 c2 c3")
    d = Matrix([d1, d2, d3])
    c = Matrix([c1, c2, c3])
    q = c1 * d1 + c2 * d2 + c3 * d3
    partial_2 = Matrix([[0, -d3, d2], [d3, 0, -d1], [-d2, d1, 0]])
    conj_partial_2 = Matrix([[0, -c3, c2], [c3, 0, -c1], [-c2, c1, 0]])
    bb = expand(conj_partial_2.T * partial_2)
    return expand(bb - (q * eye(3) - d * c.T))


def degree_bound(order: int) -> int:
    """Maximum numerator degree in the a_i available at O(u**order).

    Odd orders add no hop: the third-order operator retains the second-order
    incidence structure because every tromino numerator vanishes.
    """
    if order < 2:
        raise ValueError("the expansion starts at second order")
    return order // 2


@dataclass(frozen=True)
class Prediction:
    order: int
    newly_available: tuple[str, ...]
    coefficients: tuple[str, ...]


#: The falsifiable consequence. Sixth order is the first place a three-hop
#: process can reach degree 3, so it is the first place B_shp and D_shp may be
#: nonzero. This is testable by G9, which is already a planned computation:
#: if m_6 comes back with B_shp = D_shp = 0 again, the degree bound is not the
#: mechanism and G14 needs a different answer.
SIXTH_ORDER_PREDICTION = Prediction(
    order=6,
    newly_available=("q*e_2", "e_3"),
    coefficients=("B_shp", "D_shp"),
)
