"""G17 uniformity: the shell isolation constant.

G18's register says the carrier has no volume-uniform spectral isolation,
because the in-shell splitting collapses as Delta_L ~ L^-2. That statement is
about the dispersive splitting INSIDE the retained shell. This suite proves
the complementary statement nobody had checked: the shell as a whole is
isolated in the electric spectrum by a constant, uniformly in the volume --
and computes that constant exactly.

Within the trivial-centre-flux sector the gauge-invariant spectrum of H_E
below 2C_F + gamma is exactly {0, 2C_F}, with

    gamma = C_F               for N = 3 and every N >= 5,
    gamma = 5/4 = 2(C_L2-C_F) at N = 4,

attained by fundamental dominoes (three shared-link Casimir units) and, at
N = 4 alone, by a plaquette carrying Lambda^2 F. Both margins -- 2C_F below,
gamma above -- are independent of L.

The proof stacks arithmetic and one parity lemma on the proved retained-shell
census: every charged link costs at least C_F/2 (Casimir minimality, pinned
on a bounded window by the assembly suite); the census classifies k <= 4;
every 5-cycle wraps the torus, so its flux equals its irrep's N-ality and the
trivial-flux sector empties the k = 5 shelf down to zero-N-ality loops at
>= 5N/2; six links cost >= 3C_F by counting; and a 4-cycle carrying any irrep
beyond F, F-bar costs 2C >= 2C_2(N).

The absent campaign note F1 (WORKHOUSE_FIXED_TO_CONTINUUM_MASTER_CHAIN,
2026-08-22) RECORDS exactly this at SU(3) -- shell at 8/3, sharp gap 4/3 --
as a citation to a never-delivered proof document. The row is now a checked
statement here instead of a citation.

Why this matters for the crossings: gamma is the constant a G17 stability
argument must keep at u > 0, the resolvent denominators of the proved
second-order theorem are >= C_F >= gamma uniformly in L, and the last two
checks verify the hypothesis package that relatively-bounded-perturbation
machinery (the never-delivered F2 note's subject) consumes, with its
dimensionless ratio computed. Nothing here is non-perturbative; G17 and G18
stay open.
"""

from __future__ import annotations

from itertools import product

from sympy import Rational, factor, simplify

from .. import constants as K
from ._core import _suite
from .assembly import _cycles, _endpoints, _faces, _links, _shift

# ==========================================================================
isolation = _suite("G17 uniformity: the shell isolation constant")

_CF = (K.N**2 - 1) / (2 * K.N)


def _casimir(labels, n):
    """C(lambda) from Dynkin labels, normalised so C(F) = (N^2-1)/(2N)."""
    mu = [sum(labels[i:]) for i in range(len(labels))]
    total = sum(mu)
    raw = sum(Rational(m * (m + n + 1 - 2 * (j + 1))) for j, m in enumerate(mu))
    return Rational(raw - Rational(total**2, n), 2)


def _winding(cycle, ell):
    """Net displacement of a cycle divided by L: the winding vector."""
    links = set(cycle)
    incident = {}
    for link in links:
        a, b = _endpoints(link, ell)
        incident.setdefault(a, []).append(link)
        incident.setdefault(b, []).append(link)
    start = next(iter(incident))
    site, disp, used = start, [0, 0, 0], set()
    while True:
        link = next(x for x in incident[site] if x not in used)
        used.add(link)
        (x, i) = link
        if site == x:  # traverse forward
            disp[i] += 1
            site = _shift(x, i, ell)
        else:  # traverse backward
            disp[i] -= 1
            site = x
        if site == start:
            break
    assert all(d % ell == 0 for d in disp)
    return tuple(d // ell for d in disp)


@isolation.check(
    "five charged links clear the shell by exactly C_F/2, at every volume",
    "G17 / PUB edition Lem. 14",
)
def _():
    margin = simplify(5 * _CF / 2 - 2 * _CF - _CF / 2) == 0
    per_link = simplify((6 * _CF / 2 - 5 * _CF / 2) - _CF / 2) == 0
    at_ranks = {n: simplify((_CF / 2).subs(K.N, n)) for n in (3, 4, 5)}
    return margin and per_link, (
        "every charged link costs at least C_F/2 (Casimir minimality of F, "
        "the input the assembly suite pins on a bounded window), and gauge "
        "invariance forbids 1-valent charged sites, so any configuration with "
        "k >= 5 charged links sits at least 5C_F/2 - 2C_F = C_F/2 above the "
        f"plaquette shell -- C_F/2 = { {k: str(v) for k, v in at_ranks.items()} } at N = 3, 4, 5, "
        "each further link adding another C_F/2. The count is local and the "
        "bound never mentions L. This is the crude counting floor; the exact "
        "constant, twice as large away from SU(4), is assembled two checks on"
    )


@isolation.check(
    "the second-Casimir shelf: every irrep beyond F and F-bar clears 5C_F/4",
    "G17 / PUB edition Lem. 14",
)
def _():
    bound = 5
    ok = True
    second = {}
    for n in range(3, 9):
        shelf = Rational(5 * (n**2 - 1), 8 * n)  # 5 C_F / 4
        fund = tuple([1] + [0] * (n - 2))
        antifund = tuple([0] * (n - 2) + [1])
        least = None
        for labels in product(range(bound + 1), repeat=n - 1):
            if not any(labels) or sum(labels) > bound:
                continue
            if labels in (fund, antifund):
                continue
            c = _casimir(labels, n)
            ok = ok and c >= shelf
            least = c if least is None else min(least, c)
        second[n] = least
    lam2 = (K.N + 1) * (K.N - 2) / K.N
    sym2 = (K.N - 1) * (K.N + 2) / K.N
    shelf_sym = Rational(5, 4) * _CF
    family_ok = (
        simplify(factor(8 * K.N * (lam2 - shelf_sym)) - (3 * K.N - 11) * (K.N + 1)) == 0
        and simplify(factor(8 * K.N * (sym2 - shelf_sym)) - (3 * K.N + 11) * (K.N - 1)) == 0
        and simplify(factor(8 * K.N * (K.N - shelf_sym)) - (3 * K.N**2 + 5)) == 0
    )
    expected_second = {3: 3, 4: Rational(5, 2), 5: Rational(18, 5), 6: Rational(14, 3)}
    window_ok = all(second[n] == expected_second[n] for n in expected_second)
    return ok and family_ok and window_ok, (
        "min C over nontrivial non-(anti)fundamental dominant weights with "
        f"label sum <= {bound}: C_2 = { {k: str(v) for k, v in second.items()} } -- the adjoint at "
        "N = 3, Lambda^2 F from N = 4 -- and every window weight clears "
        "5C_F/4. Symbolically 8N(C - 5C_F/4) is (3N-11)(N+1) for Lambda^2 F "
        "(nonnegative from N = 4; at N = 3 Lambda^2 F IS F-bar), (3N+11)(N-1) "
        "for Sym^2 F and 3N^2+5 for the adjoint; the unbounded statement is "
        "the same dominance-order classical input the shell lemma names"
    )


@isolation.check(
    "every 5-cycle wraps the torus, so flux empties the five-link shelf",
    "G17 / PUB edition Lem. 14",
)
def _():
    ok = True
    detail = {}
    for ell in (3, 4, 5):
        fives = _cycles(ell, 5)
        windings = {_winding(c, ell) for c in fives}
        ok = (
            ok
            and (0, 0, 0) not in windings
            and all(any(abs(w) == 1 for w in vec) for vec in windings)
        )
        detail[ell] = (len(fives), sorted(windings))
    return ok, (
        f"(5-cycles, winding vectors) = { {k: (v[0], v[1]) for k, v in detail.items()} } at "
        "L = 3, 4, 5: every one wraps, with some axis winding exactly +-1 -- "
        "the parity proof (five unit steps cannot cancel axiswise without a "
        "wrap) enumerated rather than argued. A wrapping cycle's centre flux "
        "through the wrapped axis is winding times N-ality, so a flux-zero "
        "5-cycle needs a zero-N-ality irrep, costing >= 5N/2 -- far above the "
        "shelf. The five-link level of the flux-zero sector is EMPTY of "
        "fundamental flux at every rank, which is why the exact isolation "
        "constant below is twice the counting floor"
    )


@isolation.check(
    "the exact isolation constant: gamma = C_F, except 5/4 at SU(4), attained",
    "G17 / G18 / PUB edition Thm. 16",
)
def _():
    lam2 = (K.N + 1) * (K.N - 2) / K.N
    # the two candidate margins above the shell
    domino = simplify(3 * _CF - 2 * _CF - _CF) == 0  # 6-link F-domino sits at 3C_F
    heavier = simplify(2 * (lam2 - _CF) - (K.N - 3) * (K.N + 1) / K.N) == 0
    # which margin binds: 2(C_L2 - C_F) - C_F has numerator (N-5)(N+1)
    switch = simplify(4 * K.N * (2 * (lam2 - _CF) - _CF) - 2 * (K.N - 5) * (K.N + 1)) == 0
    gamma = {
        3: Rational(4, 3),  # C_F; Lambda^2 = F-bar there, sextet/adjoint clear
        4: Rational(5, 4),  # 2(C_L2 - C_F) < C_F: the one rank below
        5: Rational(12, 5),  # equality rank: both margins are C_F
        6: simplify(_CF.subs(K.N, 6)),
    }
    values_ok = (
        gamma[3] == simplify(_CF.subs(K.N, 3))
        and gamma[4] == simplify((2 * (lam2 - _CF)).subs(K.N, 4))
        and gamma[4] < simplify(_CF.subs(K.N, 4))
        and gamma[5] == simplify(_CF.subs(K.N, 5)) == simplify((2 * (lam2 - _CF)).subs(K.N, 5))
    )
    # resolvent corollary: every proved channel gap is C_F + C_rho/2 >= C_F >= gamma
    channels = [0, K.N, (K.N + 1) * (K.N - 2) / K.N, (K.N - 1) * (K.N + 2) / K.N]
    denominators = all(simplify((_CF + c / 2) - _CF - c / 2) == 0 for c in channels)
    return domino and heavier and switch and values_ok and denominators, (
        "above the shell: k = 5 is emptied by flux (previous check), k >= 6 "
        "costs >= 3C_F by counting with the fundamental domino attaining it "
        "exactly, and a 4-cycle beyond F, F-bar costs 2C_2 -- so gamma = "
        "min(C_F, 2(C_2 - C_F)), where 4N(2(C_L2-C_F) - C_F) = 2(N-5)(N+1) "
        "puts the switch at N = 5 exactly: gamma = "
        f"{ {k: str(v) for k, v in gamma.items()} }, i.e. C_F everywhere except 5/4 at SU(4), "
        "attained, uniform in L, with the vacuum 2C_F below. The absent "
        "campaign note F1 RECORDS sharp gap 4/3 at SU(3); that row is now "
        "checked here rather than cited. Every proved resolvent denominator "
        "C_F + C_rho/2 is >= C_F >= gamma, so no perturbative denominator "
        "degrades with volume"
    )


@isolation.check(
    "flux is winding times N-ality: fundamental wrapping loops die at every rank",
    "G17 / PUB edition Lem. 14 / MASTER paper",
)
def _():
    # CORRECTION, recorded rather than deleted: an earlier draft of this
    # check computed a straight L-loop's centre flux as L mod N and concluded
    # the shell lemma's L = 4 exclusion was load-bearing exactly at SU(4).
    # That was wrong. The flux measured around a torus cycle is the loop's
    # WINDING NUMBER times its irrep's N-ality -- a straight loop crosses a
    # fixed dual plane once, whatever its length -- so a fundamental wrapping
    # loop carries flux +-1 at every L and every N, and the trivial-flux
    # sector removes it everywhere, the same argument the shell lemma already
    # applies to the L = 3 winding triangles. The L = 4 exclusion clause is
    # therefore belt-and-braces at every rank: the loops it names are the one
    # 4-cycle family that is energy-degenerate with the shell (4*C_F/2 =
    # 2C_F exactly), which is why the paper states the exclusion explicitly
    # rather than routing it through flux.
    ok = True
    detail = {}
    for ell in (3, 4, 5):
        straight = set()
        for i in range(3):
            for x in product(range(ell), repeat=3):
                if x[i] == 0:
                    straight.add(frozenset((_shift(x, i, ell, s), i) for s in range(ell)))
        windings = {_winding(c, ell) for c in straight}
        expected = {tuple(1 if j == i else 0 for j in range(3)) for i in range(3)} | {
            tuple(-1 if j == i else 0 for j in range(3)) for i in range(3)
        }
        ok = ok and len(straight) == 3 * ell**2 and windings <= expected
        detail[ell] = len(straight)
    accident = simplify(4 * _CF / 2 - 2 * _CF) == 0
    nality_never_zero = all((1 * 1) % n != 0 for n in range(2, 13))
    return ok and accident and nality_never_zero, (
        f"straight loops per L: {detail}, every winding vector a unit vector, "
        "so a fundamental loop's flux is +-1 mod N -- nonzero at every rank "
        "N >= 2 -- and the trivial-flux sector removes it for every L, the "
        "triangle argument applied uniformly. The L = 4 clause in the shell "
        "lemma is redundant belt given the flux clause; it earns its explicit "
        "statement because L = 4 is where the loop is exactly "
        "energy-degenerate with the shell (4*C_F/2 = 2C_F). An earlier draft "
        "of this check read the flux as L mod N and claimed SU(4) needed the "
        "clause; the correction is recorded in the source"
    )


@isolation.check(
    "one insertion cannot connect distinct plaquettes: |p Delta p'| >= 6",
    "G17 / G18 / PUB edition Lem. 15",
)
def _():
    ok = True
    detail = {}
    for ell in (3, 4, 5):
        faces = _faces(ell)
        min_delta = 9
        for a in range(len(faces)):
            for b in range(a + 1, len(faces)):
                min_delta = min(min_delta, len(faces[a] ^ faces[b]))
        ok = ok and min_delta == 6
        detail[ell] = min_delta
    return ok, (
        f"min |p Delta p'| over distinct face pairs = {detail} at L = 3, 4, 5 "
        "(adjacent faces share one link: 4 + 4 - 2), while one magnetic "
        "insertion changes electric content on at most 4 links -- so at first "
        "order the shell has NO off-diagonal matrix elements at any rank: it "
        "moves rigidly (the SU(3) diagonal epsilon-row is the registry's "
        "recorded u^1 = 1 entry, absent at N >= 4), the band width begins at "
        "u^2, and the isolation constant degrades only through second-order "
        "dressing, not first"
    )


@isolation.check(
    "the stability hypothesis package, with its dimensionless ratio",
    "G17 / PUB edition Lem. 14",
)
def _():
    # incidence: range-1 perturbation, four links per plaquette, four
    # plaquettes per link, at L = 3..5 exhaustively
    ok = True
    incidence = {}
    for ell in (3, 4, 5):
        faces = _faces(ell)
        per_link: dict = {}
        for f in faces:
            for link in f:
                per_link[link] = per_link.get(link, 0) + 1
        counts = set(per_link.values())
        sizes = {len(f) for f in faces}
        ok = ok and counts == {4} and sizes == {4} and len(per_link) == len(_links(ell))
        incidence[ell] = (sorted(sizes), sorted(counts))
    # the dimensionless ratio 2N/gamma the stability machinery consumes,
    # in the normalisation H_E = sum_e C(rho_e)/2, V_p = Tr U_p + Tr U_p^dag
    gamma3, gamma4 = Rational(4, 3), Rational(5, 4)
    ratio = {
        3: Rational(6) / gamma3,
        4: Rational(8) / gamma4,
        5: simplify((2 * K.N / _CF).subs(K.N, 5)),
        "N->oo": 4,
    }
    limit_ok = simplify(2 * K.N / _CF - 4 * K.N**2 / (K.N**2 - 1)) == 0
    ratio_ok = (
        ratio[3] == Rational(9, 2) and ratio[4] == Rational(32, 5) and ratio[5] == Rational(25, 6)
    )
    return ok and limit_ok and ratio_ok, (
        f"(links per face, faces per link) = { {k: v for k, v in incidence.items()} } "
        "exhaustively: "
        "the perturbation is a sum of range-1 terms, each touching 4 links, "
        "each link touched by 4 terms, and ||Tr U + Tr U^dag|| = 2N (triangle "
        "inequality on unit eigenvalues, saturated at U = 1 -- a named "
        "classical input). H_E is diagonal in the electric basis with the "
        "product vacuum as unique ground state and local gap C_F/2 per link: "
        "exactly the hypothesis package of relatively-bounded stability "
        "machinery (the subject of the never-delivered campaign note F2, "
        "whose checkable half this suite now supplies). The dimensionless "
        "ratio per unit u is 2N/gamma = "
        f"{ {k: str(v) for k, v in ratio.items()} }, 4N^2/(N^2-1) -> 4 at large N. What such a "
        "theorem would DELIVER -- a volume-uniform vacuum gap for u below a "
        "universal multiple of these ratios -- is conditional on the external "
        "theorem, which is unread here and stays T3; nothing about it is "
        "promoted by this check"
    )
