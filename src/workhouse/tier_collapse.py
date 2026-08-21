"""G14: the tier collapse. A reformulation that holds, and a mechanism that did not.

The degree-bound mechanism proposed here was RETRACTED after stress-testing.
See ADR 0005. What survives is the reformulation in Step 1, which is exact and
independent of any mechanism; Steps 2-3 are kept only to document the failure.

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

Why the bound fails
-------------------
The count above is wrong, and the error is one step, not a subtlety.

The numerator is not H_4 itself. The carrier is the d-direction, so

    eps_4 = (d^dagger H_4 d) / (d^dagger d),      d^dagger d = q,

which is where the 1/q in the ansatz comes from. The numerator is therefore
``d^dagger H_4 d``, and the projection ``d^dagger (.) d`` adds one further d and
one further conj(d) — one more power of a — on top of whatever H_4 carries.

So four vertices give H_4 entries of degree <= 2, and the numerator degree <= 3.
Degree 3 is exactly {q e_2, e_3}: the B_shp/D_shp pair. The count permits them.

A concrete witness: ``diag(a_i**2)`` is a legal degree-2 entry structure, and

    d^dagger diag(a_i**2) d = sum a_i**3 = q**3 - 3 q e_2 + 3 e_3,

which carries a nonzero e_3 component.

The corpus said as much already. MASTER_THEORY 5.1 records that the enumeration
of 144 ordered two-hop sequences *gives* the rank-five span including q e_2 and
e_3 — the sequences produce those terms and the dynamics then sets their
coefficients to zero. That is a dynamical statement, not a kinematic exclusion,
and it was available before the mechanism was proposed.

The sixth-order prediction derived from the bound is retracted with it.

What still stands
-----------------
Step 1 is an exact identity and needs no mechanism: the vanishing pair IS the
degree-3 part of the numerator, and since a_i ~ L^-2 that is the same set as the
L^-4 tier. G14 is better posed for it, and no closer to answered.

The incidence identity in Step 2 also stands on its own — it reproduces the
recorded second-order spectrum and explains the 1/q — it simply does not bound
what the fourth order can reach.
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


def operator_degree_bound(order: int) -> int:
    """Maximum a-degree of the H_(2r) matrix entries at O(u**order).

    Odd orders add no hop: the third-order operator retains the second-order
    incidence structure because every tromino numerator vanishes.
    """
    if order < 2:
        raise ValueError("the expansion starts at second order")
    return order // 2


def numerator_degree_bound(order: int) -> int:
    """Maximum a-degree of d^dagger H d, the quantity that actually spans.

    One greater than the operator bound: the carrier projection contributes an
    extra d and conj(d). Missing this term is what refuted the mechanism —
    at fourth order it is the difference between forbidding {B_shp, D_shp} and
    permitting them.
    """
    return operator_degree_bound(order) + 1


@dataclass(frozen=True)
class Prediction:
    order: int
    newly_available: tuple[str, ...]
    coefficients: tuple[str, ...]


#: RETRACTED. This claimed sixth order was the first place degree 3 becomes
#: reachable. With the projection counted, degree 3 is already reachable at
#: fourth order, so the prediction has no basis. Kept as a record of the
#: retraction rather than deleted; ADR 0005 explains why.
RETRACTED_SIXTH_ORDER_PREDICTION = Prediction(
    order=6,
    newly_available=("q*e_2", "e_3"),
    coefficients=("B_shp", "D_shp"),
)
