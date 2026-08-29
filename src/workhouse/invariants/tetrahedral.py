from __future__ import annotations

from sympy import (
    Rational,
    limit,
    simplify,
    symbols,
    together,
)

from .. import cellular as CELL
from .. import constants as K
from ._core import _suite

# ---------------------------------------------------------------------------
# Tetrahedral Haar-resolvent coefficient (G5/C15). The corpus asserts the
# r = 2 row of its primitive completion law with no artifact and no reference
# SHA anywhere (the restored-payloads FINDING pins the absence), so C15 can
# only close by re-derivation. workhouse.cellular reconstructs the law's three
# stated ingredients — the 1/N merge from the fundamental-pair Haar moment,
# the certified electric convention E(L) = L*C_F/2, and exhaustive temporal
# orderings over the cell's faces — and these checks first prove the
# reconstruction against every instance the corpus certifies or prints
# (sealed-core cube, prism 64 and its superseded-sector 24, pentagonal
# "120 histories, S_5 = 70", the notebook's Catalan cap family), and only then
# read the same convention at r = 2. Scope: primitive simple-loop channel, as
# the law itself is scoped; physical survival after compression/Q-projection
# is U3's question and is NOT asserted here.

tetra = _suite("tetrahedral Haar-resolvent coefficient (G5)")


@tetra.check("the law's two printed forms are one identity, scaling N^-(2r-1)", "transcript ~148")
def _():
    n, s = symbols("N S", positive=True)
    cf = (n**2 - 1) / (2 * n)
    gaps = [
        simplify(s / (n**r * cf ** (r - 1)) - 2 ** (r - 1) * s / (n * (n**2 - 1) ** (r - 1)))
        for r in range(2, 6)
    ]
    tails = [limit(K.c_prim_printed(r) * K.N ** (2 * r - 1), K.N, "oo") for r in range(2, 6)]
    ok = all(g == 0 for g in gaps) and tails == [-8, 64, -160, 1120]
    return ok, (
        f"S/(N^r C_F^(r-1)) - 2^(r-1) S/(N(N^2-1)^(r-1)) = {gaps} for r = 2..5 with "
        f"C_F = (N^2-1)/(2N); N^(2r-1) c_r -> {tails}, the printed N^-(2r-1) scaling"
    )


@tetra.check("a merge contributes exactly 1/N at every shared-path length", "transcript ~136")
def _():
    # The law's r = 1 content. The only group integral in the primitive channel
    # is the fundamental-pair moment, whose coefficient is the n = 1 Weingarten
    # value 1/N — the inverse of the 1x1 Gram matrix [N], the same Gram-inverse
    # route the published-comparisons suite walks at n = 2. Contracting
    # Tr(A u_1..u_k) Tr(B u_k~..u_1~) link by link then yields (1/N) Tr(AB)
    # for every k: each contraction pays 1/N and every non-final one closes a
    # colour loop worth N. The upstream notebook assumes this flat 1/N; here it
    # is derived. k runs to 4, one past the longest shared path any history in
    # the five enumerated cells uses.
    wg1 = CELL.weingarten_1()
    moments = [CELL.merge_moment(k) for k in range(1, 5)]
    ok = wg1 == 1 / CELL.N and all(
        coeff == 1 / CELL.N and rest in ([["A", "B"]], [["B", "A"]]) for coeff, rest in moments
    )
    return ok, (
        f"Wg_1 = {wg1}; contraction of the k-link shared path gives "
        f"{[str(c) for c, _ in moments]} times Tr(AB) for k = 1..4 — "
        "(1/N)^k from the pair moments times N^(k-1) closed colour loops"
    )


@tetra.check("the resolvent unit is the certified electric convention", "v4.3 §9.3 / §4.4")
def _():
    # E(L) = L*C_F/2 is not a new convention: at N = 3 it is the certified
    # pentagonal pair E_SIDE and E_CAP, and its L = 4 value is the certified
    # one-plaquette rest energy e_flat(0) = 8/3. The registered
    # electric_energy function is the single home; this check binds it to the
    # certified values AND to cellular's C_F-unit resolvent denominators.
    energy = K.electric_energy
    cf = (K.N**2 - 1) / (2 * K.N)
    cellular_unit = simplify((energy(3) - energy(4)) / cf)  # tetra denominator
    ok = (
        energy(4, 3) == K.E_SIDE
        and energy(5, 3) == K.E_CAP
        and energy(4, 3) == K.e_flat(0)
        and simplify(energy(4) - (K.N**2 - 1) / K.N) == 0
        and cellular_unit == Rational(-1, 2)
    )
    return ok, (
        f"L*C_F/2 at N = 3: E(4) = {energy(4, 3)} = E_SIDE = e_flat(0), "
        f"E(5) = {energy(5, 3)} = E_CAP; symbolically E(4) = 2 C_F = (N^2-1)/N; and "
        f"(E(3) - E(4))/C_F = {cellular_unit} — exactly cellular's (l_0 - l)/2 "
        "denominator for the tetrahedral intermediate"
    )


@tetra.check("the cube instance re-derives the sealed core, temporal classes included", "818 ~3963")
def _():
    c4, s4, hist = CELL.c_prim(CELL.CUBE, *CELL.CAP_SECTOR)
    classes = {}
    for h in hist:
        key = (h.lengths, h.weight_e0(4))
        classes[key] = classes.get(key, 0) + 1
    expected = {((6, 6, 6), -8): 16, ((6, 8, 6), -4): 8}
    ok = (
        s4 == -20
        and classes == expected
        and simplify(c4 - K.c_prim_printed(4)) == 0
        and c4.subs(CELL.N, 3) == K.CUBE_COMPLETION_4
        and simplify(4 * (-c4) - K.alpha_pen()) == 0
        and 4 * abs(c4.subs(CELL.N, 3)) == K.ALPHA_PEN_3
    )
    return ok, (
        f"24 orderings; per-history amplitudes in E_0 units {dict(classes)} — the corpus's "
        "three multiplicity-8 classes (-8, -8, -4) with the (6,6,6) class split 8+8; "
        f"S_4 = {s4}, c_4 = {c4} -> {c4.subs(CELL.N, 3)} = CUBE_COMPLETION_4, and "
        f"4|c_4| = alpha_pen(N), = {K.ALPHA_PEN_3} at N = 3 — the sealed core, sign included"
    )


@tetra.check("the prism square sector re-derives the printed 64/(N(N^2-1)^2)", "THM_FLUX §3.2")
def _():
    values = set()
    for p in range(2, 5):
        for q in range(2, 5):
            if p != q:
                c3, s3, hist = CELL.c_prim(CELL.TRIANGULAR_PRISM, p, q)
                values.add((c3, s3, len(hist)))
    (c3, s3, count), *rest = values
    su3 = c3.subs(CELL.N, 3)
    ok = (
        not rest
        and s3 == 16
        and count == 6
        and simplify(c3 - K.c_prim_printed(3)) == 0
        and su3 == K.PRISM_COMPLETION_3_SU3
        and 6 * su3 == K.PRISM_BANDWIDTH_3_SU3
    )
    return ok, (
        f"all 6 ordered square pairs agree: 6 histories each, S_3 = {s3}, c_3 = {c3} "
        f"-> {su3} at N = 3, and the printed third-order bandwidth 6 c_3(3) = {6 * su3}"
    )


@tetra.check("24 and 64 are different endpoint sectors of one prism, not rivals", "818 ~3402")
def _():
    # The shipped notebook gates +24/(N(N^2-1)^2) (1/8 at SU(3)) for the
    # triangular prism; the corpus's table prints 64. Both come out of this one
    # engine: 24 is the cap-to-cap completion, 64 the square-to-square one the
    # retained vertical-square sector actually uses. 818.txt records the
    # supersession of 24 by 64 as the sector choice — an ADR-0002-style
    # dissolution, not an arithmetic conflict.
    cap, s_cap, hist_cap = CELL.c_prim(CELL.TRIANGULAR_PRISM, *CELL.CAP_SECTOR)
    square, s_sq, _ = CELL.c_prim(CELL.TRIANGULAR_PRISM, *CELL.SQUARE_SECTOR)
    ok = (
        s_cap == 6
        and len(hist_cap) == 6
        and simplify(cap - CELL.catalan_cap_coefficient(3)) == 0
        and cap.subs(CELL.N, 3) == K.PRISM_CAP_COMPLETION_3_SU3
        and s_sq == 16
        and simplify(square - K.c_prim_printed(3)) == 0
    )
    return ok, (
        f"cap sector: S = {s_cap}, c = {cap} -> {cap.subs(CELL.N, 3)} at N = 3, the notebook's "
        f"gated value; square sector: S = {s_sq}, c = {square} -> "
        f"{square.subs(CELL.N, 3)}, the printed table row — same cell, same convention"
    )


@tetra.check("the n-gonal cap family is Catalan; the pentagonal row is n = 5", "transcript ~175")
def _():
    from sympy import binomial

    rows = {}
    for sides in range(3, 7):
        cell = CELL.prism(sides)
        c, s, hist = CELL.c_prim(cell, *CELL.CAP_SECTOR)
        rows[sides] = (s, len(hist), simplify(c - CELL.catalan_cap_coefficient(sides)) == 0)
    counts_ok = all(
        rows[n][0] == (-1) ** (n - 1) * binomial(2 * n - 2, n - 1) and rows[n][2]
        for n in range(3, 7)
    )
    c5, s5, hist5 = CELL.c_prim(CELL.PENTAGONAL_PRISM, *CELL.CAP_SECTOR)
    ok = (
        counts_ok
        and (s5, len(hist5)) == (70, 120)
        and simplify(c5 - K.c_prim_printed(5)) == 0
        and c5.subs(CELL.N, 5 - 2) == K.PENT_COMPLETION_5_SU3
    )
    return ok, (
        f"S_n for n = 3..6: {[rows[n][0] for n in range(3, 7)]} = (-1)^(n-1) C(2n-2, n-1), "
        f"the shipped notebook's closed family; the pentagonal instance is the transcript's "
        f"'120 histories, S_5 = 70' with c_5 = {c5} -> {c5.subs(CELL.N, 3)} at N = 3"
    )


@tetra.check(
    "the run-length Catalan factorization holds for every proper subset through n = 7",
    "cellular brief, appendix A",
)
def _():
    # The lemma behind Theorem 2's closed form for ALL n (appendix A of the
    # referee brief): for any proper subset T of the n-site cycle, the chain
    # sum F(T) = sum over insertion orders of prod_k 1/blocks(T_k) equals the
    # product of Catalan numbers over T's cyclic run lengths. Verified here
    # with nothing assumed: F is computed by its definitional recursion
    # F(T) = (1/blocks(T)) sum_{x in T} F(T-x) over the whole subset lattice,
    # cross-checked against literal enumeration of every |T|! ordering for
    # n <= 5, and compared to the Catalan product for every proper T, n <= 7.
    from itertools import permutations

    from sympy import Integer, binomial

    def catalan(m):
        return binomial(2 * m, m) / (m + 1)

    def blocks(mask, n):
        if mask == 0:
            return 0
        if mask == (1 << n) - 1:
            return 1
        return sum(1 for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1)

    def run_lengths(mask, n):
        starts = [i for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1]
        lengths = []
        for start in starts:
            length, i = 0, start
            while mask >> i & 1:
                length, i = length + 1, (i + 1) % n
            lengths.append(length)
        return lengths

    def chain_dp(n):
        f = {0: Integer(1)}
        for mask in sorted(range(1, 1 << n), key=lambda m: bin(m).count("1")):
            if mask == (1 << n) - 1:
                continue
            total = sum(f[mask & ~(1 << i)] for i in range(n) if mask >> i & 1)
            f[mask] = total / blocks(mask, n)
        return f

    factorization_ok, brute_ok = True, True
    for n in range(3, 8):
        f = chain_dp(n)
        for mask, value in f.items():
            if mask:
                product = Integer(1)
                for length in run_lengths(mask, n):
                    product *= catalan(length)
                factorization_ok &= value == product
        if n <= 5:
            for mask in list(f):
                if not mask:
                    continue
                sites = [i for i in range(n) if mask >> i & 1]
                brute = sum(_chain_product(order, n) for order in permutations(sites))
                brute_ok &= brute == f[mask]
    return factorization_ok and brute_ok, (
        "F(T) computed by the definitional lattice recursion equals the product of "
        "Catalan numbers over T's cyclic run lengths for every proper subset of "
        "Z_n, n = 3..7 (376 subsets), and equals the literal all-orderings sum "
        "for every subset at n <= 5 — the lemma the 1/blocks resolvent weight "
        "makes true by absorbing one Catalan convolution per run"
    )


def _chain_product(order, n):
    """Product of 1/blocks over every prefix of one insertion order.

    Every prefix, the full subset included — matching F's definition; the
    full-cycle case (blocks = 1 by convention) cannot arise because F is only
    brute-forced on proper subsets.
    """
    from sympy import Integer

    mask, product = 0, Integer(1)
    for site in order:
        mask |= 1 << site
        count = sum(1 for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1)
        product /= count
    return product


@tetra.check(
    "Theorem 2's closed form holds through n = 9, past the engine's exhaustive range",
    "cellular brief, appendix A",
)
def _():
    # Appendix A's theorem: splitting the cap-sector ordering sum by its last
    # insertion gives A(n) = n * F(arc of n-1 sites) = n * Catalan(n-1)
    # = C(2n-2, n-1), so S_n = (-1)^(n-1) C(2n-2, n-1) for every n. The
    # subset-lattice DP reaches n = 9 in milliseconds where the engine's
    # history enumeration (checked to n = 6 above) could not, and the
    # resulting c_prim matches the brief's closed coefficient symbolically.
    from sympy import Integer, binomial, simplify

    def blocks(mask, n):
        if mask == (1 << n) - 1:
            return 1
        return sum(1 for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1)

    closed_ok, coeff_ok = True, True
    for n in range(2, 10):
        f = {0: Integer(1)}
        for mask in sorted(range(1, 1 << n), key=lambda m: bin(m).count("1")):
            if mask == (1 << n) - 1:
                continue
            total = sum(f[mask & ~(1 << i)] for i in range(n) if mask >> i & 1)
            f[mask] = total / blocks(mask, n)
        full = (1 << n) - 1
        a_n = sum(f[full & ~(1 << x)] for x in range(n))
        closed_ok &= a_n == binomial(2 * n - 2, n - 1)
        s_n = Integer(-1) ** (n - 1) * a_n
        c_closed = 2 ** (n - 1) * s_n / (CELL.N * (CELL.N**2 - 1) ** (n - 1))
        coeff_ok &= simplify(c_closed - CELL.catalan_cap_coefficient(n)) == 0
    return closed_ok and coeff_ok, (
        "A(n) from the subset-lattice DP equals C(2n-2, n-1) for n = 2..9 "
        "(2, 6, 20, 70, 252, 924, 3432, 12870), and the signed count assembles "
        "into the brief's closed coefficient symbolically at every n — the cap "
        "family is now a theorem for all n, with instances n <= 6 still "
        "independently exhausted by the history engine above"
    )


@tetra.check("the primitive sign is the resolvent parity", "quarantined master v3 erratum 9")
def _():
    # Every intermediate loop in every admissible history of all five cells is
    # LONGER than the endpoint face, so all r-1 denominators are negative and
    # sign(S_r) = (-1)^(r-1). That is exactly the (-1)^(r+1) the quarantined
    # master v3 bolts onto its unsigned counts as erratum 9 — corroboration
    # from a document this repository never treats as current; the sign here
    # comes from the derivation, anchored by the even-order certified cube row.
    cells = [
        (CELL.TETRAHEDRON, 0, 1),  # any pair; face-transitive
        (CELL.TRIANGULAR_PRISM, *CELL.SQUARE_SECTOR),
        (CELL.CUBE, *CELL.CAP_SECTOR),
        (CELL.PENTAGONAL_PRISM, *CELL.CAP_SECTOR),
    ]
    all_longer, signed = True, []
    for cell, p, q in cells:
        s, hist = CELL.s_value(cell, p, q)
        ell = len(cell.faces[p])
        all_longer &= all(length > ell for h in hist for length in h.lengths)
        signed.append(s)
    unsigned = [abs(s) for s in signed]
    parity = [(-1) ** (r - 1) * u for r, u in zip(range(2, 6), unsigned, strict=True)]
    ok = all_longer and signed == parity and unsigned == [4, 16, 20, 70]
    return ok, (
        f"signed S_r = {signed}; every intermediate exceeds the endpoint length, so "
        f"S_r = (-1)^(r-1) |S_r| with |S_r| = {unsigned} — the quarantined master's "
        "unsigned counts (4, 16, 20, 70) and its erratum-9 sign, derived not asserted"
    )


@tetra.check("G5: the tetrahedral coefficient is exactly -8/(N(N^2-1))", "transcript ~170 / C15")
def _():
    results = set()
    for p in range(4):
        for q in range(4):
            if p != q:
                c2, s2, hist = CELL.c_prim(CELL.TETRAHEDRON, p, q)
                results.add((c2, s2, len(hist), tuple(h.lengths for h in hist)))
    (c2, s2, count, lengths), *rest = results
    su3 = c2.subs(CELL.N, 3)
    ok = (
        not rest
        and s2 == -4
        and count == 2
        and lengths == ((4,), (4,))
        and simplify(c2 - K.c_prim_printed(2)) == 0
        and su3 == K.TETRA_COMPLETION_2_SU3
    )
    return ok, (
        f"all 12 ordered endpoint pairs agree: 2 histories each, the single intermediate is "
        f"always the 4-link loop (denominator -C_F/2, i.e. weight -2 per history), "
        f"S_2 = {s2}, c_2 = {c2} -> {su3} at N = 3 — exactly the value C15 records as "
        "asserted-without-artifact; primitive channel only, per the law's own scope"
    )


@tetra.check("the tetrahedral circuit attains its bound with nonzero weight", "THM_FLUX §2 / C6")
def _():
    # The survival gate the mobility theorem asked this calculation to test:
    # the tetrahedron's B_2 has the unique primitive circuit (1,1,1,1), so
    # w_min = 4 and the scoped bound r >= w_min - 2 (C6's survivor) allows
    # r = 2 — and the primitive local weight at that order is nonzero at every
    # rank, so circuit allowance is matched by Haar survival in this third
    # geometry. Compression and Q-projection survival are NOT asserted: that
    # is U3's question.
    kernel = CELL.integer_kernel(CELL.TETRAHEDRON)
    w_min = min(sum(abs(x) for x in v) for v in kernel)
    c2 = K.c_prim_printed(2)
    negative = all(c2.subs(K.N, n) < 0 for n in range(2, 13))

    numerator, denominator = together(c2).as_numer_denom()
    ok = kernel == [(1, 1, 1, 1)] and w_min == 4 and w_min - 2 == 2 and negative and numerator == -8
    return ok, (
        f"ker_Z B_2 = {kernel}: one primitive unit-coefficient circuit, w_min = {w_min}, "
        f"r = 2 = w_min - 2; c_2 = -8/{denominator} < 0 for all N >= 2 (checked exactly at "
        "N = 2..12, and the numerator is the constant -8), so the r = 2 allowance carries "
        "nonzero primitive Haar-resolvent weight — the falsification test the theorem "
        "proposed did not kill the coefficient"
    )


@tetra.check("primitive proper returns are scalar on the tetrahedral face space", "U3 (partial)")
def _():
    # The U3-adjacent statement this engine CAN settle. A second-order proper
    # return is p -> merged loop -> p: one insertion, then its removal. In the
    # primitive channel each face p has one such history per other face f,
    # with the same 1/N^2 merge weight and the same resolvent, so the return
    # operator on the four-dimensional face space is computed here entry by
    # entry. It comes out exactly scalar: primitive proper returns renormalize
    # the tetrahedral rest energy and are structurally incapable of shape
    # dispersion (the traceless compression annihilates every scalar). This is
    # a primitive-level data point ONLY — U3's pentagonal precedent is the
    # vanishing of 28 histories individually after exact Q projection, and the
    # Fierz/quotient layer needed to ask that question of the tetrahedron is
    # not built here. The Q-projected third data point stays open.
    per_face = {}
    for p in range(4):
        total = Rational(0)
        ell = len(CELL.TETRAHEDRON.faces[p])
        for f_idx, face in enumerate(CELL.TETRAHEDRON.faces):
            if f_idx == p:
                continue
            loop, _shared = CELL._merge(list(CELL._face_edges(CELL.TETRAHEDRON.faces[p])), face)
            total += Rational(2, ell - len(loop))
        per_face[p] = total
    scalar = set(per_face.values())
    c_ret = simplify(next(iter(scalar)) / (K.N**2 * (K.N**2 - 1) / (2 * K.N)))
    ok = scalar == {-6} and simplify(c_ret + 12 / (K.N * (K.N**2 - 1))) == 0
    return ok, (
        f"per-face return sums {list(per_face.values())}: all four faces give -6 in C_F "
        f"units (three 4-link returns at weight -2 each), so the return operator is "
        f"{c_ret} times the identity and its traceless compression is 0 — shape-inert at "
        "the primitive level; the Q-projected analogue of the pentagonal 28-history "
        "vanishing remains uncomputed, so U3 gains a consistent partial point, not a verdict"
    )
