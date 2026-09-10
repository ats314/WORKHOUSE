"""The Feshbach channel of the plaquette Hodge algebra, and what it costs.

G14 reduced the tier collapse ``B_shp = D_shp = 0`` to the Hodge form of the
fourth-order kernel (ADR 0019),

    H4 = -nu~ (L_up - 2) + u S^2 - pi~ S + sigma~ I - 2 C_shp R,

and stopped at "on the carrier every term but the last is a scalar". This
module asks the next question, the one U3 asks in general: **what does the
Feshbach complement Q see?** The answer here is exact and, on the cubic
geometry, complete.

At each Bloch point with q > 0 the three-dimensional plaquette fibre splits as

    C psi  (+)  psi^perp  =  ker L_down  (+)  ker L_up,

because ``L_down + L_up`` is the scalar Laplacian ``q I`` per plane component
and ``L_down psi = 0``. So the Feshbach projector ``Q = 1 - P_psi`` is exactly
the projector onto ``ker L_up``, and both Laplacians act on the carrier by
scalars: ``Q L_down psi = Q L_up psi = 0``. Neither Hodge generator can leave
the retained sector. **Every excursion off the carrier costs one insertion of
the one non-Hodge operator R**, the cross-plane half of ``S``, whose amplitude
in the kernel is ``-2 C_shp`` -- the coefficient the C2 dispute is about.

Two exact consequences, computed here as Laurent identities over the whole
zone, no tolerance:

1. The actual fourth-order support {I, U, S, S^2, R} has carrier symbols
   in span{q, q^2, e_2}, so B = D = 0. R-degree alone is insufficient:
   sigma(UR) = -2 q e_2 populates B despite containing only one R. The
   original broader assertion and checker are preserved in the intake run.
   This module verifies the one-R word formula for lengths at most three,
   then distinguishes it from the stronger claim about the actual kernel.

2. Two R insertions unlock the ``L^-4`` tier, in a fixed ratio.
   ``sigma(RR) = q e_2 + 3 e_3`` exactly, so the ``R^2`` channel carries the
   B-monomial and the D-monomial locked at 1 : 3.

And one falsifier-shaped prediction, recorded as such and proved as an
identity of the algebra rather than of any dynamics: ``sigma(RUR) = 4 e_2^2``,
whose shape symbol ``4 e_2^2 / q`` is **outside** the five-element span of the
shape ansatz. U2 says the obstruction space is spanned by elementary symmetric
polynomials and nothing else appears; the algebra that produced the
fourth-order kernel contains a word that violates that at sixth order. Whether
the sixth-order dynamics populates that word is G9/G10's question -- this
module does not claim it does. The cleared Laurent identities also hold at
Gamma, where q = 0 and psi = 0, but no normalized carrier projector is defined
there by this calculation.

ADR 0005 is the reason the last paragraph is phrased that way. A degree bound
was once read off a vertex count, predicted the ``L^-4`` tier first at sixth
order, and was retracted. Nothing here is a vertex count: the statements below
are Laurent-polynomial identities of the recorded operators, and the sixth
order enters only as "which words the dynamics populates", which is open.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

from .. import kernel_orbits as KO
from ._core import _suite

hodge = _suite("the Feshbach channel of the plaquette Hodge algebra")

_SEC = "HODGE_FESHBACH; G14; U2; U3; C2; ADR 0019; GLUEBALL v3.1 6.2; THM_FLUX Prop. 2"

_REACH = 3


# -- the algebra, built once ---------------------------------------------------


def _ops():
    ident = KO.identity()
    l_down = KO.down_laplacian(_REACH)
    l_up = KO.up_laplacian(_REACH)
    s_sq = KO.combine((1, l_down), (-4, ident))
    return ident, l_down, l_up, s_sq, KO.cross_half(s_sq)


def _conj(lp):
    return {tuple(-x for x in e): c for e, c in lp.items()}


def _ip(v, w):
    acc: dict = {}
    for p in KO.PLANES:
        acc = KO._add(acc, KO._mul(_conj(v[p]), w[p]))
    return {k: c for k, c in acc.items() if c}


def _psi():
    return KO.carrier()


def _a(j: int):
    d, dm = [0, 0, 0], [0, 0, 0]
    d[j], dm[j] = 1, -1
    return {(0, 0, 0): Fraction(2), tuple(d): Fraction(-1), tuple(dm): Fraction(-1)}


def _elementary():
    """q = e_1, e_2, e_3 as Laurent polynomials in z."""
    a = [_a(j) for j in range(3)]
    e1: dict = {}
    for x in a:
        e1 = KO._add(e1, x)
    e2: dict = {}
    for i, j in ((0, 1), (0, 2), (1, 2)):
        e2 = KO._add(e2, KO._mul(a[i], a[j]))
    e3 = KO._mul(KO._mul(a[0], a[1]), a[2])
    return e1, e2, e3


def _word(letters: str, gens: dict, ident):
    op = ident
    for g in letters:
        op = KO.compose(op, gens[g])
    return op


def _sigma(letters: str, gens: dict, ident, psi):
    return _ip(psi, KO.apply(_word(letters, gens, ident), psi))


def _scale(lp, c: Fraction):
    return {k: v * c for k, v in lp.items() if v * c}


def _sub(a, b):
    return KO._add(a, b, -1)


# -- 1. the splitting ----------------------------------------------------------


@hodge.check(
    "for q > 0, Q projects onto ker L_up; the cleared Hodge identities hold everywhere", _SEC
)
def _():
    # L_down + L_up is the scalar Laplacian q I per plane component -- no
    # cross-plane entries survive the sum -- so on the three-dimensional fibre
    # L_up = q I - L_down. The carrier is the kernel of L_down, hence the
    # eigenvector of L_up with eigenvalue q, hence L_up vanishes on psi^perp.
    # That identifies the Feshbach complement with a Hodge summand, which is
    # the whole reason the rest of this module is exact.
    ident, l_down, l_up, _s, _r = _ops()
    total = KO.combine((1, l_down), (1, l_up))
    diagonal = {k: v for k, v in total.items() if k[0] == k[1]}
    e1, _e2, _e3 = _elementary()
    scalar = {(p, p, d): c for p in KO.PLANES for d, c in e1.items()}
    psi = _psi()
    outer = {
        (ip, op, d): value
        for ip in KO.PLANES
        for op in KO.PLANES
        for d, value in KO._mul(psi[op], _conj(psi[ip])).items()
    }
    ok = (
        total == diagonal
        and total == scalar
        and not KO.compose(l_down, l_up)
        and l_up == outer
        and _ip(psi, psi) == e1
    )
    return (
        ok,
        (
            f"L_down + L_up has {len(total)} records, all plane-diagonal, and equals q I "
            f"exactly (q = e_1 = sum_j 4 sin^2(k_j/2)); L_down L_up = 0. So on the fibre "
            "L_up = psi psi^dagger and |psi|^2 = q. For q > 0 the two kernels are "
            "complementary and Q = 1 - P_psi projects onto ker L_up. At Gamma q = 0, "
            "psi = 0: only the cleared identities apply, not the normalized projector"
        ),
        {"HODGE_FIBRE_DIM": Fraction(3)},
    )


@hodge.check("neither Hodge generator leaves the carrier: Q L_down psi = Q L_up psi = 0", _SEC)
def _():
    # The Feshbach statement of homological protection. L_down psi = 0 is the
    # protection itself; L_up psi = q psi is its Hodge partner. Both are
    # scalars on the carrier line, so the off-diagonal Feshbach coupling
    # generated by the Hodge algebra is identically zero -- no resolvent, no
    # intermediate state, nothing to expand.
    _ident, l_down, l_up, s_sq, _r = _ops()
    e1, _e2, _e3 = _elementary()
    zero = KO.acts_as(l_down, {})
    up = KO.acts_as(l_up, e1)
    s = KO.acts_as(s_sq, {(0, 0, 0): Fraction(-4)})
    return zero and up and s, (
        "L_down psi = 0 exactly (homological protection, B^dagger psi = 0), L_up psi = q psi, "
        "S psi = -4 psi. All three are scalars on the carrier line, so Q L_down psi = "
        "Q L_up psi = Q S psi = 0: the Hodge algebra generates no Feshbach coupling at all"
    )


@hodge.check("the R-excitation is up-harmonic: L_up (Q R psi) = 0 exactly", _SEC)
def _():
    # R -- the cross-plane half of S, the one operator of the fourth-order
    # kernel that is not a polynomial in the two Laplacians -- does move the
    # carrier. Its excitation phi = Q R psi is nonzero and lies in ker L_up,
    # which is forced by the splitting above but is checked here as a Laurent
    # identity rather than argued: this is the vector every Feshbach excursion
    # of this geometry passes through.
    _ident, _ld, l_up, _s, r = _ops()
    psi = _psi()
    q = _ip(psi, psi)
    r_psi = KO.apply(r, psi)
    num = _ip(psi, r_psi)
    # phi = q (R psi) - <psi, R psi> psi, the Feshbach excitation cleared of 1/q
    phi = {p: _sub(KO._mul(q, r_psi[p]), KO._mul(num, psi[p])) for p in KO.PLANES}
    nonzero = any(phi[p] for p in KO.PLANES)
    orthogonal = not _ip(psi, phi)
    killed = not any(KO.apply(l_up, phi).values())
    return nonzero and orthogonal and killed, (
        "phi = q R psi - <psi, R psi> psi is not identically zero, is orthogonal to the "
        "carrier over the whole zone, and L_up phi = 0 record by record. Every excursion "
        "off the retained sector in this geometry is an R insertion, and it lands in the "
        "up-harmonic summand"
    )


# -- 2. the word table ---------------------------------------------------------


def _table(max_len: int = 3):
    ident, _ld, l_up, s_sq, r = _ops()
    gens = {"S": s_sq, "U": l_up, "R": r}
    psi = _psi()
    q = _ip(psi, psi)
    eps = {g: _sigma(g, gens, ident, psi) for g in "SUR"}
    out = {}
    for n in range(1, max_len + 1):
        for w in itertools.product("SUR", repeat=n):
            word = "".join(w)
            sigma = _sigma(word, gens, ident, psi)
            # the fully factorized value, cleared of denominators:
            #   q^n * sigma(W)  ==  prod_g sigma(g)   when W factorizes
            lhs = sigma
            for _ in range(n - 1):
                lhs = KO._mul(lhs, q)
            rhs = {(0, 0, 0): Fraction(1)}
            for g in w:
                rhs = KO._mul(rhs, eps[g])
            out[word] = (sigma, _sub(lhs, rhs))
    return out


@hodge.check("the Feshbach defect of a word vanishes unless two R's meet unseparated by U", _SEC)
def _():
    # The exact selection rule. sigma(W) factorizes over the letters -- i.e.
    # its total carrier symbol factorizes -- for every word of length <= 3 except
    # RR, RRS, SRR, RSR, RRU, URR, RRR. RUR factorizes and RSR does not,
    # because the intermediate letter acts on phi, and L_up phi = 0 while
    # S phi does not vanish. So it is not "two R's" that costs: it is two R's
    # whose intermediate excursion is not annihilated.
    table = _table()
    defective = sorted(w for w, (_s, d) in table.items() if d)
    expected = sorted(["RR", "RRS", "SRR", "RSR", "RRU", "URR", "RRR"])
    two_r_no_u = sorted(
        w
        for w in table
        if any(
            w[i] == "R" and w[j] == "R" and "U" not in w[i + 1 : j]
            for i in range(len(w))
            for j in range(i + 1, len(w))
        )
    )
    return defective == expected and defective == two_r_no_u, (
        f"{len(table)} words of length <= 3 in (S, U, R); exactly {len(defective)} have a "
        f"nonzero Feshbach defect: {', '.join(defective)}. Every one of them contains two R "
        "insertions with no U between them, and every word with at most one R factorizes "
        "completely. RUR factorizes (L_up phi = 0) and RSR does not -- the rule is about the "
        "intermediate excursion, not about counting R's"
    )


@hodge.check(
    "words of length at most three with at most one R obey the exact carrier formula", _SEC
)
def _():
    # This word formula is valid; the original inference that q^n e_2
    # cannot populate B was false. The next check preserves its counterexample.
    table = _table(3)
    e1, e2, _e3 = _elementary()
    ok = True
    for word, (sigma, defect) in table.items():
        if word.count("R") > 1:
            continue
        ok = ok and not defect
        n_u = word.count("U")
        n_r = word.count("R")
        scale = Fraction((-4) ** word.count("S")) * Fraction((-2) ** n_r)
        base = {(0, 0, 0): Fraction(1)}
        for _ in range(n_u + (1 - n_r)):
            base = KO._mul(base, e1)
        if n_r:
            base = KO._mul(base, e2)
        ok = ok and sigma == _scale(base, scale)
    return ok, (
        "every word with at most one R has carrier symbol (-4)^#S (-2)^#R q^(#U + 1 - #R) "
        "e_2^#R exactly, verified for lengths at most three as cleared Laurent identities. "
        "The U count matters: UR already has sigma = -2 q e_2, so R-degree alone "
        "does not exclude the B tier"
    )


@hodge.check("FINDING: one R does not exclude B; sigma(UR) = sigma(RU) = -2 q e_2", _SEC)
def _():
    table = _table(2)
    q, e2, _e3 = _elementary()
    target = _scale(KO._mul(q, e2), Fraction(-2))
    ok = bool(target) and all(table[w][0] == target and not table[w][1] for w in ("UR", "RU"))
    return (
        ok,
        (
            "UR and RU each contain exactly one R, have zero Feshbach defect, and have "
            "sigma = -2 q e_2 exactly. Thus sigma/q = -2 e_2 populates B. The actual "
            "fourth-order support excludes these words; its tier collapse survives"
        ),
        {"UR_CLEARED_B_WEIGHT": Fraction(-2)},
    )


@hodge.check("two R insertions unlock the L^-4 tier locked at B : D = 1 : 3", _SEC)
def _():
    # The first word that populates degree 3, and the constraint it carries.
    # sigma(RR) = q e_2 + 3 e_3 is an exact Laurent identity, so the R^2
    # channel cannot contribute the B-monomial without contributing the
    # D-monomial at three times the weight. Any future order whose e_3
    # coefficient comes from R^2 alone has D = 3 B; a measured departure
    # localizes the other words (R U R, R S R, R^3) instead of being a free
    # fit parameter.
    table = _table(2)
    e1, e2, e3 = _elementary()
    sigma_rr, _defect = table["RR"]
    target = KO._add(KO._mul(e1, e2), _scale(e3, Fraction(3)))
    ok = sigma_rr == target and sigma_rr != KO._mul(e1, e2)
    return (
        ok,
        (
            "sigma(RR) = q e_2 + 3 e_3 exactly over the whole zone. The B-monomial and the "
            "D-monomial enter the R^2 channel at fixed relative weight 1 : 3, so D = 3 B for "
            "any kernel whose degree-3 tier is carried by R^2 alone"
        ),
        {"RR_TIER_RATIO": Fraction(3)},
    )


@hodge.check(
    "FINDING: the algebra contains a shape monomial the four-shape ansatz cannot hold", _SEC
)
def _():
    # U2 states that every fourth-order shape coefficient is a symmetric
    # function of the Bloch scalars in the span {c_0, A q, B e_2, C (4 e_2/q),
    # D (e_3/q)}, and its falsifier is a coefficient of the retained operator
    # that cannot be written in {q, e_2, e_3}. This is not that -- 4 e_2^2 / q
    # IS a function of the Bloch scalars -- but it is outside the FIVE-ELEMENT
    # SPAN the ansatz actually fits, which is the form U2 is used in. Recorded
    # as a finding, scoped to the algebra: R U R is a word of the operator
    # algebra that produced the fourth-order kernel, and no dynamics is claimed
    # to populate it. ADR 0005 retracted a sixth-order prediction read off a
    # degree count; the statement here is an identity of the recorded
    # operators, and what stays open is exactly which words order six turns on.
    table = _table(3)
    e1, e2, e3 = _elementary()
    sigma_rur, defect = table["RUR"]
    target = _scale(KO._mul(e2, e2), Fraction(4))
    # the ansatz span, cleared of 1/q: {q, q^2, e_2, q e_2, e_3}
    span = [e1, KO._mul(e1, e1), e2, KO._mul(e1, e2), e3]
    exps = sorted({k for m in [*span, sigma_rur] for k in m})
    import sympy as sp

    matrix = sp.Matrix([[sp.Rational(m.get(k, 0)) for m in span] for k in exps])
    rhs = sp.Matrix([sp.Rational(sigma_rur.get(k, 0)) for k in exps])
    solvable = matrix.rank() == matrix.row_join(rhs).rank()
    return (
        sigma_rur == target and not defect and not solvable,
        (
            "sigma(RUR) = 4 e_2^2 exactly, and R U R has zero Feshbach defect, so the value is "
            "the honest carrier symbol of that word and not an artefact of a truncation. Its "
            "shape symbol 4 e_2^2 / q is NOT in the span of the ansatz's cleared monomials "
            "{q, q^2, e_2, q e_2, e_3} (rank test, exact). A nonzero RUR contribution "
            "would require an enlarged ansatz unless other contributions cancel its "
            "out-of-span part. Which words order six populates and how they combine "
            "remain open (G9, G10)"
        ),
        {"RUR_SHAPE_WEIGHT": Fraction(4)},
    )


@hodge.check("the actual fourth-order support I, U, S, S^2, R forces B = D = 0", _SEC)
def _():
    # The actual support is narrower than arbitrary words linear in R:
    # UR and RU are absent. Check each supported word's full coefficient
    # polynomial rather than testing inequality with one unscaled monomial.
    from ..payloads import kernel_constants, kernel_records

    amps = KO.amplitudes(kernel_records())
    form = KO.hodge_form(amps)
    built = KO.hodge_records(form)
    c_shp = kernel_constants()["C_shp"]
    q, e2, _e3 = _elementary()
    table = _table(2)
    supported = {
        "U": KO._mul(q, q),
        "S": _scale(q, Fraction(-4)),
        "SS": _scale(q, Fraction(16)),
        "R": _scale(e2, Fraction(-2)),
    }
    ok = (
        built == dict(kernel_records())
        and form["C"] == c_shp
        and all(table[word][0] == value for word, value in supported.items())
        and _ip(_psi(), _psi()) == q
    )
    return ok, (
        f"the 189 records are -nu~(L_up - 2) + u S^2 - pi~ S + sigma~ I - 2 C R exactly, with "
        f"C = {form['C']} = C_shp. The supported words I,U,S,SS,R have symbols "
        "q,q^2,-4q,16q,-2e_2, so their span contains no q e_2 or e_3 tier. "
        "This proves B = D = 0 for this support, not for every R-linear kernel"
    )


# -- 3. the hypothesis, tested in two more geometries --------------------------


@hodge.check(
    "the Hodge-word statement needs only L_down psi = 0 and L_up psi = lambda psi, "
    "and both hold in three geometries",
    "HODGE_FESHBACH Hodge-word hypotheses in other cells; U3; G5; ADR 0008",
)
def _():
    # The preserved source's proposed U7 asked for L_down + L_up to be scalar -- "link
    # regularity" -- because that is what the cubic lattice does. This check
    # is here because that hypothesis is WRONG, and the pentagonal prism says
    # so: its two caps carry five links and its five sides four, so the sum is
    # diag(6, 6, 5, 5, 5, 5, 5) and not a scalar. The hypothesis actually
    # needed is weaker and holds in all three: psi spans ker L_down, and psi is
    # an eigenvector of L_up. That alone makes every word in the two Laplacians
    # scalar on the carrier -- a word ending in L_down annihilates it, a word
    # ending in L_up rescales it. The proposed U7 is a branch-local label;
    # the integration review is the registered source for this exact check.
    # Recorded as a check rather than as prose because the over-strong version
    # would have excluded the pentagonal cap, the geometry U3 is about.
    import sympy as sp

    from .. import cellular as CELL

    rows = {}
    for name, cell in (
        ("tetrahedron", CELL.TETRAHEDRON),
        ("pentagonal prism", CELL.PENTAGONAL_PRISM),
    ):
        boundary = sp.Matrix(cell.boundary_matrix())
        l_down = boundary.T * boundary
        kernel = CELL.integer_kernel(cell)
        psi = sp.Matrix(kernel[0])
        l_up = psi * psi.T  # the single top cell: d_3^dagger d_3 on faces
        total = l_down + l_up
        rows[name] = {
            "nullity": l_down.shape[0] - l_down.rank(),
            "carrier": l_down * psi == sp.zeros(l_down.shape[0], 1),
            "eigen": l_up * psi == (psi.T * psi)[0] * psi,
            "orthogonal": l_down * l_up == sp.zeros(*l_down.shape),
            "scalar_sum": total == sp.eye(total.shape[0]) * total[0, 0],
            "lambda": (psi.T * psi)[0],
            "diag": [total[i, i] for i in range(total.shape[0])],
        }
    hypothesis = all(
        r["nullity"] == 1 and r["carrier"] and r["eigen"] and r["orthogonal"] for r in rows.values()
    )
    regular = {n: r["scalar_sum"] for n, r in rows.items()}
    return hypothesis and regular == {"tetrahedron": True, "pentagonal prism": False}, (
        "in both cells ker L_down is one-dimensional and spanned by the face-sign carrier, "
        "L_down L_up = 0, and L_up psi = |psi|^2 psi (4 psi on the tetrahedron, 7 psi on the "
        "prism). So every word in the two Laplacians is scalar on the carrier in both. "
        f"L_down + L_up is a scalar on the tetrahedron (4 I) and is NOT on the prism "
        f"({rows['pentagonal prism']['diag']}: five links on a cap, four on a side), so the "
        "link-regularity hypothesis is refuted as a requirement and the weaker eigenvector "
        "hypothesis suffices for scalar Hodge words. No proper-return calculation "
        "or general U3 conclusion is established in these two cells by this check"
    )
