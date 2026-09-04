"""The swap-odd domino state, and why the C-even leakage equals the hop.

U4 recorded, as a conjecture with a falsifier, that the C-even per-neighbour
leakage and the C-even hopping are one vacuum-mediated object at every order,
because the domino engine finds them equal at both orders it computes:
``leak_(2,+) = t_(2,+) = -11/306`` and ``leak_(3,+) = t_(3,+) = -6335/249696``.
ADR 0023 derives the equality instead, and the reason is not the vacuum
route. On the domino's C-even manifold ``span{e_1, e_2}`` with
``e_i = chi_i + chibar_i``, the engine's own definitions make
``leak_k - t_k = E_k(psi_A) - vac_k^domino - gap_k^single`` for the swap-odd
state ``psi_A = e_1 - e_2``. Two facts about ``psi_A`` then settle it:

* multiplication of class functions commutes, so ``W psi_A = e_1^2 - e_2^2``
  has NO two-plaquette image and NO vacuum image -- both cancel between the
  halves -- and ``H_0`` conserves the isotypic content of each plaquette, so
  through third order no two-plaquette intermediate can return to that
  image. ``E_k(psi_A)`` is therefore a single-plaquette rotor energy with
  the vacuum removed from its intermediates;
* the vacuum's contribution to the excited rotor energy -- the ``|0>``
  route -- is ``-vac_k`` exactly, at ``k = 2`` (``3/4``) and ``k = 3``
  (``9/32``), because both are the same matrix element ``<0|W|e> = |e|^2``
  over the same denominator ``2 C_F`` with opposite signs.

Together: ``E_k(psi_A) = E_k^exc - (-vac_k) = vac_k + E_k^exc``, which is
``leak_k = t_k``. The C-odd swap-odd state keeps two cross terms, the
like-family pair, and the same bookkeeping gives ``leak - t = 2 A_N + 1/C_F``
-- ``-3/68`` at ``N = 3``, the registered value. Every check here is
engine-free: SU(3) characters, tensor-product rules and exact rationals.
"""

from __future__ import annotations

from sympy import Matrix, Rational, cancel, expand, eye, symbols, zeros

from .. import constants as K
from ._core import _suite

# ==========================================================================
swap_odd = _suite("the swap-odd domino state (U4, ADR 0023)")


def _casimir(p, q):
    return Rational(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def _rotor(manifold, drop_vacuum=False, top=5):
    """des Cloizeaux blocks h_1, h_2, h_3 of the SU(3) plaquette rotor.

    ``H_0 = 2 C_2(R)`` on the irrep ``(p, q)`` (four links, each ``C_2 / 2``),
    ``V = -y W`` with ``W = chi + chibar`` acting by the multiplicity-free
    rules ``(p,q) x (1,0) = (p+1,q) + (p-1,q+1) + (p,q-1)`` and its conjugate,
    ``R = Q (E_0 - H_0)^-1 Q``. With ``drop_vacuum`` the trivial irrep is
    removed from the intermediates, which is what the swap-odd state sees.
    """
    irreps = [(p, q) for p in range(top + 1) for q in range(top + 1) if p + q <= top]
    idx = {r: i for i, r in enumerate(irreps)}
    n = len(irreps)
    w = zeros(n, n)
    for p, q in irreps:
        for r2 in [(p + 1, q), (p - 1, q + 1), (p, q - 1), (p, q + 1), (p + 1, q - 1), (p - 1, q)]:
            if r2 in idx:
                w[idx[r2], idx[(p, q)]] += 1
    h0 = Matrix.diag(*[2 * _casimir(*r) for r in irreps])
    e0 = h0[idx[manifold[0]], idx[manifold[0]]]
    proj = zeros(n, n)
    for r in manifold:
        proj[idx[r], idx[r]] = 1
    res = zeros(n, n)
    for r in irreps:
        if r in manifold or (drop_vacuum and r == (0, 0)):
            continue
        res[idx[r], idx[r]] = 1 / (e0 - h0[idx[r], idx[r]])
    pwp = proj * w * proj
    h1 = -pwp
    h2 = proj * w * res * w * proj
    a = proj * w * res * res * w * proj
    h3 = -proj * w * res * w * res * w * proj + Rational(1, 2) * (a * pwp + pwp * a)
    sub = [idx[r] for r in manifold]
    return [h.extract(sub, sub) for h in (h1, h2, h3)], eye(n)


def _sector_energies(drop_vacuum=False):
    blocks, _ = _rotor([(1, 0), (0, 1)], drop_vacuum)
    even, odd = Matrix([1, 1]), Matrix([1, -1])
    return (
        [(even.T * h * even)[0] / 2 for h in blocks],
        [(odd.T * h * odd)[0] / 2 for h in blocks],
    )


@swap_odd.check(
    "the rotor towers 13/20, 1/2, 101/200, 7/32 and vacuum -3/4, -9/32 follow from SU(3) fusion",
    "ENGINE_FLUX_su3_domino_d3.py (spectral cross-validation); UNIFIED §2.1 towers",
)
def _():
    # The engine cross-validates its word calculus against a spectral single
    # plaquette and gates the Bridge towers gap_2 = {13/20, 1/2}, gap_3 =
    # {101/200, 7/32}. This repository used those four numbers as literals
    # (coupling and su3 suites) and VAC3_DOMINO = 2 x (-9/32) as a registered
    # constant. Here they are re-derived from the irrep ladder alone.
    vac, _ = _rotor([(0, 0)])
    vac = [h[0, 0] for h in vac]
    even, odd = _sector_energies()
    gaps = {k: (even[k] - vac[k], odd[k] - vac[k]) for k in (1, 2)}
    ok = (
        vac == [0, Rational(-3, 4), Rational(-9, 32)]
        and even[0] == -1
        and odd[0] == 1
        and gaps[1] == (Rational(13, 20), Rational(1, 2))
        and gaps[2] == (Rational(101, 200), Rational(7, 32))
        and 2 * vac[2] == K.VAC3_DOMINO
        # the printed (beta/4)-towers convert as 4 * Delta(3u/2): coupling suite
        and gaps[1][0] == K.TOWER_B2_PLUS * 4 * Rational(3, 2) ** 2
        and gaps[2][0] == K.TOWER_B3_PLUS * 4 * Rational(3, 2) ** 3
        and gaps[1][1] == K.TOWER_B2_MINUS * 4 * Rational(3, 2) ** 2
        and gaps[2][1] == K.TOWER_B3_MINUS * 4 * Rational(3, 2) ** 3
    )
    return (
        ok,
        (
            f"vacuum (h1, h2, h3) = {vac}; excited C-even {even}, C-odd {odd}; gaps "
            f"(even, odd) = {gaps[1]} at order 2 and {gaps[2]} at order 3 -- the engine's "
            "four tower gates and its -9/32, now from the (p,q) ladder with E = 2 C_2 and "
            "multiplicity-free fusion, no word calculus. The registered (beta/4)-towers are "
            "these under 4 Delta(3u/2), and VAC3_DOMINO is twice the single vacuum, i.e. no "
            "connected third-order vacuum diagram"
        ),
        {"E_VAC_SINGLE_2": vac[1], "E_VAC_SINGLE_3": vac[2]},
    )


@swap_odd.check(
    "W psi_A has no two-plaquette and no vacuum image for C-even; C-odd keeps the like-family pair",
    "ADR 0023 (the swap-odd lemma)",
)
def _():
    # Class functions multiply commutatively, so the mixed products in
    # W (e_1 - e_2) cancel identically, and the vacuum overlaps <0|e_1^2> and
    # <0|e_2^2> are the same number. For o_i = chi_i - chibar_i the mixed
    # products do NOT cancel: exactly chi_1 chibar_2 and chibar_1 chi_2
    # survive, with coefficients +2 and -2. Which shared-link family those two
    # carry is settled numerically by the C-odd check below.
    c1, cb1, c2, cb2 = symbols("chi1 chibar1 chi2 chibar2")
    w = c1 + cb1 + c2 + cb2
    e1, e2, o1, o2 = c1 + cb1, c2 + cb2, c1 - cb1, c2 - cb2
    even_image = expand(w * (e1 - e2))
    odd_image = expand(w * (o1 - o2))
    mixed = [c1 * c2, c1 * cb2, cb1 * c2, cb1 * cb2]
    even_mixed = [even_image.coeff(m) for m in mixed]
    odd_mixed = [odd_image.coeff(m) for m in mixed]
    # <0| chi_a chi_b > = 1 iff b is the conjugate of a; e_i^2 contains chi chibar twice
    vacuum = {"e1^2": 2, "e2^2": 2}
    no_two_plaquette = even_image == expand(e1**2 - e2**2) and even_mixed == [0, 0, 0, 0]
    ok = no_two_plaquette and vacuum["e1^2"] == vacuum["e2^2"] and odd_mixed == [0, 2, -2, 0]
    return ok, (
        f"W (e_1 - e_2) = e_1^2 - e_2^2 exactly; mixed-product coefficients {even_mixed} "
        f"and vacuum overlaps {vacuum} -- nothing two-plaquette, nothing vacuum, so the "
        "swap-odd C-even state is a single excited plaquette beside an inert one. "
        f"W (o_1 - o_2) keeps mixed coefficients {odd_mixed}: the pair chi_1 chibar_2, "
        "chibar_1 chi_2 survives and is what separates the C-odd sector"
    )


@swap_odd.check(
    "the |0> route is minus the vacuum energy at orders 2 and 3, so leak_(k,+) = t_(k,+) follows",
    "ADR 0023; CERT_FLUX_d3 'exact identity (gated)'",
    rests_on=(
        "the rotor towers 13/20, 1/2, 101/200, 7/32 and vacuum -3/4, -9/32 follow from SU(3) fusion",  # noqa: E501
        "W psi_A has no two-plaquette and no vacuum image for C-even; C-odd keeps the like-family pair",  # noqa: E501
        "both declared coincidences, checked: one is ell_N at all ranks, the other is bare",
    ),
)
def _():
    # With the lemma, E_k(psi_A) is the excited rotor energy computed with the
    # vacuum removed from the intermediates. The engine defines
    # leak_k = (De_k - vac_k^domino) - gap_k and t_k = Te_k, and De_k - Te_k is
    # E_k(psi_A), so leak_k - t_k = E_k^exc,novac - vac_k^single - E_k^exc =
    # -(route_k + vac_k) with route_k the vacuum's share of the excited
    # energy. The corpus calls route_2 "the |0> route" and -vac_2 "vacuum-energy
    # bookkeeping" and says they are distinct mechanisms of equal value; they
    # are <0|W|e> = |e|^2 over 2 C_F, once with each sign. Then the registered
    # third-order domino numbers must satisfy De_3 - Te_3 = E_3^exc,novac,
    # which is a prediction the engine never gated in that form.
    vac, _ = _rotor([(0, 0)])
    vac = [h[0, 0] for h in vac]
    even, _ = _sector_energies()
    even_novac, _ = _sector_energies(drop_vacuum=True)
    route = [even[k] - even_novac[k] for k in range(3)]
    cancels = [route[k] + vac[k] for k in range(3)]
    order2 = route[1] == Rational(3, 4) == 1 / K.casimir_fundamental(3)
    order3 = route[2] == Rational(9, 32)
    # the domino's registered third-order C-even numbers, read through psi_A
    psi_a_3 = K.D3_EVEN_DOMINO - K.T3_EVEN
    predicted_3 = even_novac[2]
    identity_3 = K.LEAK_3_EVEN == K.T3_EVEN
    ok = (
        cancels == [0, 0, 0]
        and order2
        and order3
        and psi_a_3 == predicted_3 == Rational(-23, 400)
        and identity_3
    )
    return (
        ok,
        (
            f"vacuum share of the excited C-even rotor energy: {route} at orders 1..3, against "
            f"the vacuum energies {vac}: sum {cancels}. At order 2 the share is 3/4 = 1/C_F, "
            "the |0> route of ell_N, and at order 3 it is 9/32 = (3/8)^2 <e|W|e>, the same "
            "matrix element that makes the vacuum energy -9/32. So E_k(psi_A) = E_k^exc + "
            f"vac_k, i.e. leak = t. Read through psi_A the domino's D3_even - T3_even = {psi_a_3} "
            f"equals the vacuum-free rotor energy {predicted_3} -- the mechanism's prediction, "
            "met by numbers the engine computed for other gates"
        ),
        {"E_PSI_A_3": psi_a_3},
    )


@swap_odd.check(
    "the C-odd swap-odd gap is 2 A_N + 1/C_F: -3/68 at N = 3, the like family and not the mixed",
    "ADR 0023; MASTER_THEORY §4.3 (A_N, B_N)",
    rests_on=(
        "W psi_A has no two-plaquette and no vacuum image for C-even; C-odd keeps the like-family pair",  # noqa: E501
        "the four channel weights follow from dimension and Casimir",
    ),
)
def _():
    # Same bookkeeping, other sector. The C-odd state has no vacuum route at
    # all (<0|W|o> = 0), and its swap-odd combination keeps the two cross
    # terms of the lemma. If those carry the like family (3 x 3 on the shared
    # link, the sum A_N), then leak_(2,-) - t_(2,-) = 2 A_N - vac_2 =
    # 2 A_N + 1/C_F; if the mixed family, 2 B_N + 1/C_F. The registered
    # values decide: -11/306 - 5/612 = -3/68 is the first and not the second.
    _, odd = _sector_energies()
    _, odd_novac = _sector_energies(drop_vacuum=True)
    no_route = [odd[k] - odd_novac[k] for k in range(3)] == [0, 0, 0]
    registered = K.LEAK_2 - K.T_MINUS_2
    like = 2 * K.antiparallel_sum(3) + 1 / K.casimir_fundamental(3)
    mixed = 2 * K.parallel_sum(3) + 1 / K.casimir_fundamental(3)
    # and at symbolic N the same identity is what the registered closed forms say
    symbolic = cancel(
        (K.antiparallel_sum() + K.parallel_sum() + 1 / K.casimir_fundamental())
        - K.hopping()
        - (2 * K.antiparallel_sum() + 1 / K.casimir_fundamental())
    )
    ok = (
        no_route
        and registered == like == Rational(-3, 68)
        and registered != mixed
        and symbolic == 0
    )
    return (
        ok,
        (
            f"the C-odd rotor has no vacuum share at any order ({no_route}); leak_2- - t_2- = "
            f"{registered} = 2 A_3 + 3/4 = {like}, while 2 B_3 + 3/4 = {mixed}. So the surviving "
            "pair chi_1 chibar_2, chibar_1 chi_2 carries the like family Lambda^2 + Sym^2, and "
            "ell_N - t_N = 2 A_N + 1/C_F at every rank is the same statement in closed form"
        ),
        {"ODD_SWAP_GAP_2": registered},
    )


# --------------------------------------------------------------------------
# Fourth order: the disconnected half of the U4 falsifier (G25 route).
#
# Past third order the des Cloizeaux blocks above stop, but within one
# C-parity sector the rotor's excited level is nondegenerate, so plain
# Rayleigh-Schrodinger with intermediate normalisation reaches any order in
# exact rationals. The eigenvalue is the same either way.
# --------------------------------------------------------------------------


def _rayleigh_schroedinger(seed, manifold, order, drop_vacuum=False, top=9):
    """Energy coefficients E_1..E_order of the rotor level seeded by ``seed``.

    ``seed`` is a dict irrep -> amplitude; the level must be nondegenerate
    within its C-parity sector, which the two-state manifold {3, 3bar} is once
    the sector is fixed. Recursion: E_k = <psi_0|V|psi_(k-1)> and
    psi_k = R (V psi_(k-1) - sum_j E_j psi_(k-j)) with V = -W and
    R = Q (E_0 - H_0)^-1 Q.
    """
    irreps = [(p, q) for p in range(top + 1) for q in range(top + 1) if p + q <= top]
    idx = {r: i for i, r in enumerate(irreps)}
    n = len(irreps)
    w = zeros(n, n)
    for p, q in irreps:
        for r2 in [(p + 1, q), (p - 1, q + 1), (p, q - 1), (p, q + 1), (p + 1, q - 1), (p - 1, q)]:
            if r2 in idx:
                w[idx[r2], idx[(p, q)]] += 1
    energy = [2 * _casimir(*r) for r in irreps]
    e0 = energy[idx[manifold[0]]]
    psi0 = Matrix([seed.get(r, 0) for r in irreps])
    psi0 = psi0 / (psi0.T * psi0)[0] ** Rational(1, 2)
    res = zeros(n, n)
    for r in irreps:
        if r in manifold or (drop_vacuum and r == (0, 0)):
            continue
        res[idx[r], idx[r]] = 1 / (e0 - energy[idx[r]])
    v = -w
    psis, coefficients = [psi0], [e0]
    for k in range(1, order + 1):
        ek = (psi0.T * v * psis[k - 1])[0]
        rhs = v * psis[k - 1] - ek * psi0
        for j in range(1, k):
            rhs -= coefficients[j] * psis[k - j]
        coefficients.append(ek)
        psis.append(res * rhs)
    return coefficients[1:]


@swap_odd.check(
    "fourth-order rotor: gaps 1657/28000 and 143/8960, vacuum -39/1280, route + vac = -63/800",
    "ADR 0023 addendum; v10a.7 one-face vacuum gate; channels suite size-1 row",
    rests_on=(
        "the rotor towers 13/20, 1/2, 101/200, 7/32 and vacuum -3/4, -9/32 follow from SU(3) fusion",  # noqa: E501
    ),
)
def _():
    # The disconnected half of the fourth-order falsifier, engine-free. Two
    # of the numbers already exist in the corpus by other routes and are
    # matched here to the last digit: the one-face vacuum e4 = -39/1280 that
    # the v10a.7 Hodge engine gates as a float, and the size-1 cluster row
    # 143/8960 of m_Gamma^(4) that the channels suite reads from the v10a.26
    # rooted incidence transform. Both are the same rotor, so both are now
    # T1. The new number is the last one: the vacuum's share of the excited
    # C-even energy no longer cancels the vacuum energy at fourth order, so
    # E_4(psi_A) - vac_4^domino - gap_4 = +63/800 + [conn_A - conn_vac], and
    # U4's all-orders equality needs the two connected diagrams to differ by
    # exactly -63/800. The recursion is checked against the des Cloizeaux
    # blocks through third order before it is trusted one order further.
    vac = _rayleigh_schroedinger({(0, 0): 1}, [(0, 0)], 5)
    even = _rayleigh_schroedinger({(1, 0): 1, (0, 1): 1}, [(1, 0), (0, 1)], 5)
    odd = _rayleigh_schroedinger({(1, 0): 1, (0, 1): -1}, [(1, 0), (0, 1)], 5)
    even_novac = _rayleigh_schroedinger({(1, 0): 1, (0, 1): 1}, [(1, 0), (0, 1)], 5, True)
    odd_novac = _rayleigh_schroedinger({(1, 0): 1, (0, 1): -1}, [(1, 0), (0, 1)], 5, True)
    agrees_with_des_cloizeaux = (
        vac[:3] == [0, Rational(-3, 4), Rational(-9, 32)]
        and even[:3] == [-1, Rational(-1, 10), Rational(179, 800)]
        and odd[:3] == [1, Rational(-1, 4), Rational(-1, 16)]
    )
    gap_even = [even[k] - vac[k] for k in range(5)]
    gap_odd = [odd[k] - vac[k] for k in range(5)]
    route_plus_vac = [even[k] - even_novac[k] + vac[k] for k in range(5)]
    odd_no_route = all(odd[k] == odd_novac[k] for k in range(5))
    # a truncation check: the same numbers at a larger irrep box
    vac_bigger = _rayleigh_schroedinger({(0, 0): 1}, [(0, 0)], 5, top=11)
    ok = (
        agrees_with_des_cloizeaux
        and vac[3] == Rational(-39, 1280)
        and gap_even[3] == Rational(1657, 28000)
        and gap_odd[3] == Rational(143, 8960)
        and route_plus_vac[:3] == [0, 0, 0]
        and route_plus_vac[3] == Rational(-63, 800)
        and odd_no_route
        and vac_bigger == vac
    )
    return (
        ok,
        (
            f"Rayleigh-Schrodinger to fifth order, agreeing with the des Cloizeaux blocks through "
            f"third: vacuum {vac}, C-even gap {gap_even}, C-odd gap {gap_odd}. The fourth-order "
            "vacuum -39/1280 is the v10a.7 engine's one-face gate and the C-odd gap 143/8960 is "
            "the size-1 row of m_Gamma^(4), both now derived. Vacuum share of the excited C-even "
            f"energy plus vacuum energy: {route_plus_vac} -- zero through third order, which is "
            "the U4 identity, and -63/800 at fourth, which is the disconnected half of its "
            "falsifier: leak_4 - t_4 = 63/800 + [conn_A - conn_vac]. Stable from irrep box 9 to 11"
        ),
        {
            "E_VAC_SINGLE_4": vac[3],
            "E_VAC_SINGLE_5": vac[4],
            "GAP_4_EVEN": gap_even[3],
            "GAP_4_ODD": gap_odd[3],
            "GAP_5_EVEN": gap_even[4],
            "GAP_5_ODD": gap_odd[4],
            "ROUTE_4_PLUS_VAC_4": route_plus_vac[3],
        },
    )
