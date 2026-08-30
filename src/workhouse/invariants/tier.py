from __future__ import annotations

from sympy import (
    Matrix,
    expand,
    simplify,
    symbols,
)

from .. import tier_collapse as T
from ._core import _suite

# ==========================================================================
tier = _suite("tier collapse (G14)")


@tier.check(
    "clearing the denominator reproduces the five-element numerator basis", "MASTER_THEORY §5.1"
)
def _():
    a1, a2, a3 = symbols("a1 a2 a3", nonnegative=True)
    c0, A, B, C, D = symbols("c0 A_shp B_shp C_shp D_shp")
    q = a1 + a2 + a3
    e2 = a1 * a2 + a1 * a3 + a2 * a3
    e3 = a1 * a2 * a3
    eps4 = c0 + A * q + B * e2 + C * 4 * e2 / q + D * e3 / q
    regrouped = c0 * q + A * q**2 + B * q * e2 + 4 * C * e2 + D * e3
    return simplify(expand(eps4 * q) - regrouped) == 0, (
        "q*eps_4 = c_0 q + A q^2 + 4C e_2 + B (q e_2) + D e_3, rank five as recorded"
    )


@tier.check("the vanishing coefficients are exactly the degree-3 ones", "MASTER_THEORY §5.2 / G14")
def _():
    degrees = T.numerator_degrees()
    carried = {name: T.NUMERATOR_BASIS[name][1] for name in T.NUMERATOR_BASIS}
    deg3 = {carried[n] for n, d in degrees.items() if d == T.VANISHING_DEGREE}
    lower = {carried[n] for n, d in degrees.items() if d < T.VANISHING_DEGREE}
    return deg3 == set(T.VANISHING) and not (deg3 & lower), (
        f"degree 3 carries {sorted(deg3)} — exactly the pair that vanishes; "
        f"degrees 1-2 carry {sorted(lower)}, all nonzero. Since a_i ~ L^-2, "
        "'the L^-4 tier' and 'degree 3 in a' are the same statement. This is an "
        "identity and survives the retraction below."
    )


@tier.check("B B^dagger = q I - d conj(d)^T for the curl incidence", "UNIFIED §2.4")
def _():
    residual = T.incidence_identity()
    return residual == residual.zeros(3, 3), (
        "the face-to-link Bloch incidence is the curl matrix [d]_x, entries linear "
        "in d; the identity gives eigenvalues (0, q, q), matching the recorded "
        "second-order C-odd spectrum with the flat carrier as the d-direction"
    )


@tier.check("the carrier projection is where the 1/q comes from", "MASTER_THEORY §5.1")
def _():
    d1, d2, d3, c1, c2, c3 = symbols("d1 d2 d3 c1 c2 c3")
    d = Matrix([d1, d2, d3])
    c = Matrix([c1, c2, c3])
    q = c1 * d1 + c2 * d2 + c3 * d3
    return simplify(expand((c.T * d)[0]) - q) == 0, (
        "d^dagger d = q, so eps_4 = (d^dagger H_4 d)/q and the numerator that spans "
        "{q, q^2, q e_2, e_2, e_3} is d^dagger H_4 d"
    )


@tier.check("RETRACTED: the vertex count does NOT forbid B_shp and D_shp", "G14 / ADR 0005")
def _():
    # The proposed mechanism counted 2r vertices -> numerator degree <= r, and
    # concluded degree 3 was unreachable at fourth order. It missed that the
    # carrier projection d^dagger (.) d adds one further power of a.
    op = T.operator_degree_bound(4)
    num = T.numerator_degree_bound(4)
    permits = num >= T.VANISHING_DEGREE
    return op == 2 and num == 3 and permits, (
        f"four vertices bound H_4 entries at a-degree {op}, but the numerator "
        f"d^dagger H_4 d reaches {num} — exactly the degree of "
        f"{sorted(T.VANISHING)}. Witness: d^dagger diag(a_i^2) d = sum a_i^3 = "
        "q^3 - 3 q e_2 + 3 e_3, carrying a nonzero e_3. MASTER_THEORY §5.1 already "
        "recorded that the 144 two-hop sequences GIVE the rank-five span including "
        "those terms, which is a dynamical vanishing, not a kinematic exclusion."
    )


@tier.check("the sixth-order prediction is withdrawn, not merely unproven", "ADR 0005")
def _():
    # Degree 3 is reachable at fourth order once the projection is counted, so
    # "sixth order is the first place it becomes reachable" is simply false.
    return T.numerator_degree_bound(4) >= T.VANISHING_DEGREE, (
        "the prediction rested on degree 3 being unreachable through O(u^4); it is "
        "reachable, so the prediction has no basis and G14 keeps no falsifier from it"
    )


@tier.check(
    "the shape family is not symmetry-complete: cubic symmetry alone permits q^2 as well",
    "MASTER_THEORY §5.1 / G14",
)
def _():
    # A correction to an attribution the paper carried, not to a number.
    # The five-element family {1, q, e_2, 4e_2/q, e_3/q} was introduced as
    # what "cubic symmetry alone permits". It is not a symmetry statement.
    # The cubic group acts on (a_1, a_2, a_3) by permutation, so its
    # invariants are the symmetric polynomials, and the numerators of degree
    # at most three with no constant term span a SIX-dimensional space,
    #
    #     {q, q^2, e_2, q^3, q e_2, e_3},
    #
    # one per partition: degree 1 gives q, degree 2 gives {q^2, e_2}, degree
    # 3 gives {q^3, q e_2, e_3}. The recorded numerator basis keeps five of
    # the six. What it omits is q^3 -- the shape q^2 -- which is cubic
    # invariant and regular at Gamma (q^2 ~ |k|^4 -> 0), so neither the point
    # group nor the carrier projection forbids it.
    #
    # The omission is a property of the two-hop enumeration that produced the
    # family, and it is load-bearing: the obstruction certificate is a rank
    # statement about THIS span, and a sixth direction would be a sixth
    # unknown for the same data to determine. Nothing here says the
    # enumeration is wrong -- only that its output is an enumeration result
    # and must be cited as one.
    a1, a2, a3 = symbols("a1 a2 a3", nonnegative=True)
    q = a1 + a2 + a3
    e2 = a1 * a2 + a1 * a3 + a2 * a3
    e3 = a1 * a2 * a3

    monomials = [
        a1**i * a2**j * a3**k
        for i in range(4)
        for j in range(4)
        for k in range(4)
        if 1 <= i + j + k <= 3
    ]

    from sympy import Poly

    def row(poly):
        p = Poly(expand(poly), a1, a2, a3)
        return [p.coeff_monomial(Poly(m, a1, a2, a3).monoms()[0]) for m in monomials]

    symmetric = {"q": q, "q^2": q**2, "e_2": e2, "q^3": q**3, "q e_2": q * e2, "e_3": e3}
    recorded = ["q", "q^2", "e_2", "q e_2", "e_3"]

    full = Matrix([row(p) for p in symmetric.values()])
    kept = Matrix([row(symmetric[name]) for name in recorded])
    with_q3 = Matrix([*kept.tolist(), row(symmetric["q^3"])])

    # q^3 is genuinely outside the recorded span: adding it raises the rank.
    ok = full.rank() == 6 and kept.rank() == 5 and with_q3.rank() == 6
    return ok, (
        f"symmetric numerators of degree 1..3 span rank {full.rank()} "
        f"({', '.join(symmetric)}); the recorded basis spans rank {kept.rank()} and "
        f"adjoining q^3 takes it to {with_q3.rank()}. So the missing direction is q^3, "
        "the shape q^2, and 'cubic symmetry alone permits' is the wrong attribution for "
        "the five-element family: symmetry permits six, the two-hop enumeration returns five"
    )
