"""G17 uniformity: the shell isolation constant.

G18's register says the carrier has no volume-uniform spectral isolation,
because the in-shell splitting collapses as Delta_L ~ L^-2. That statement is
about the dispersive splitting INSIDE the retained shell. This suite proves
the complementary statement nobody had written down: the shell as a whole is
isolated in the electric spectrum by a constant, uniformly in the volume.

Within the trivial-centre-flux sector, with the L = 4 straight loops excluded
as in the retained-shell lemma, the gauge-invariant spectrum of H_E below
5 C_F/2 is exactly {0, 2 C_F}: the vacuum, then the plaquette shell, then
nothing until C_F/2 above the shell. Both margins -- 2 C_F below, C_F/2
above -- are independent of L and closed rational functions of N.

The proof stacks arithmetic on the proved retained-shell census and needs no
new enumeration: every charged link costs at least C_F/2 (Casimir minimality,
already pinned on a bounded window by the assembly suite), the census
classifies everything with at most four charged links, five links already
cost 5 C_F/2, and a 4-cycle carrying any irrep beyond F, F-bar clears the
same shelf because every such irrep has C >= 5 C_F/4.

Why this matters for the crossings: C_F/2 is the constant a G17 free-energy
bound must beat -- the resolvent denominators of the proved second-order
theorem are already >= C_F >= 2*(C_F/2) uniformly in L, so the perturbative
expansion's denominators never degrade with volume, and what G17 still owes
is the promotion of the u = 0 isolation to small u > 0 against an EXTENSIVE
perturbation (cluster-expansion or gap-stability machinery; norm bounds
cannot do it). For G18 it corrects the frame: the L^-2 collapse is the
minimal-grid-momentum statement, not a fixed-momentum one -- at any fixed
nonzero momentum the in-shell splitting t_N u^2 q(k) is L-independent along
nested volumes, and the shell around it keeps this uniform electric
isolation. Nothing here is non-perturbative; G17 and G18 stay open.
"""

from __future__ import annotations

from itertools import product

from sympy import Rational, factor, simplify

from .. import constants as K
from ._core import _suite

# ==========================================================================
isolation = _suite("G17 uniformity: the shell isolation constant")

_CF = (K.N**2 - 1) / (2 * K.N)


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
        f"plaquette shell -- exactly C_F/2 = { {k: str(v) for k, v in at_ranks.items()} } "
        "at N = 3, 4, 5, each further link adding another C_F/2. The count k "
        "is local and the bound never mentions L: the margin is "
        "volume-uniform by construction"
    )


@isolation.check(
    "the second-Casimir shelf: every irrep beyond F and F-bar clears 5C_F/4",
    "G17 / PUB edition Lem. 14",
)
def _():
    # bounded-window sweep, same Casimir formula as the assembly suite
    def casimir(labels, n):
        mu = [sum(labels[i:]) for i in range(len(labels))]
        total = sum(mu)
        raw = sum(Rational(m * (m + n + 1 - 2 * (j + 1))) for j, m in enumerate(mu))
        return Rational(raw - Rational(total**2, n), 2)

    bound = 5
    ok = True
    binding = {}
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
            c = casimir(labels, n)
            ok = ok and c >= shelf
            least = c if least is None else min(least, c)
        binding[n] = f"{least} >= {shelf}"
    # the three named families, symbolically: 8N*(C - 5C_F/4) factors cleanly
    lam2 = (K.N + 1) * (K.N - 2) / K.N
    sym2 = (K.N - 1) * (K.N + 2) / K.N
    shelf_sym = Rational(5, 4) * _CF
    fac = {
        "Lambda^2": factor(8 * K.N * (lam2 - shelf_sym)),
        "Sym^2": factor(8 * K.N * (sym2 - shelf_sym)),
        "Adj": factor(8 * K.N * (K.N - shelf_sym)),
    }
    family_ok = (
        simplify(fac["Lambda^2"] - (3 * K.N - 11) * (K.N + 1)) == 0
        and simplify(fac["Sym^2"] - (3 * K.N + 11) * (K.N - 1)) == 0
        and simplify(fac["Adj"] - (3 * K.N**2 + 5)) == 0
    )
    return ok and family_ok, (
        "min C over nontrivial non-(anti)fundamental dominant weights with "
        f"label sum <= {bound}: { {k: v for k, v in binding.items()} } -- every one clears "
        "5C_F/4, so a 4-cycle carrying any such irrep costs 2C >= 5C_F/2, the "
        "same shelf as five links. Symbolically, 8N(C - 5C_F/4) is "
        "(3N-11)(N+1) for Lambda^2 F (nonnegative from N = 4; at N = 3 "
        "Lambda^2 F IS F-bar), (3N+11)(N-1) for Sym^2 F and 3N^2+5 for the "
        "adjoint -- the named families clear at every rank, and the window "
        "pins the rest; the unbounded statement is the same dominance-order "
        "classical input the shell lemma names"
    )


@isolation.check(
    "the retained shell is isolated by C_F/2 above and 2C_F below, uniformly in L and N",
    "G17 / G18 / PUB edition Thm. 16",
)
def _():
    gamma = {n: simplify((_CF / 2).subs(K.N, n)) for n in (3, 4, 5)}
    below = {n: simplify((2 * _CF).subs(K.N, n)) for n in (3, 4, 5)}
    # triangle case at L = 3: zero-N-ality winding triangles clear even the
    # C_F/2 shelf, with margin (N^2+5)/(4N) beyond it
    triangle = simplify((Rational(3, 2) * K.N - 2 * _CF - _CF / 2) - (K.N**2 + 5) / (4 * K.N)) == 0
    # resolvent corollary: every channel gap C_F + C_rho/2 >= C_F = 2*(C_F/2)
    channels = {
        "singlet": 0,
        "adjoint": K.N,
        "antisym": (K.N + 1) * (K.N - 2) / K.N,
        "sym": (K.N - 1) * (K.N + 2) / K.N,
    }
    denominators = all(
        simplify((_CF + c / 2) - (2 * (_CF / 2) + c / 2)) == 0 for c in channels.values()
    )
    gaps_ok = all(
        simplify((_CF + c / 2 - 2 * (_CF / 2)).subs(K.N, n)) >= 0
        for c in channels.values()
        for n in (3, 4, 5, 7)
    )
    return triangle and denominators and gaps_ok, (
        "assembling the census and the two arithmetic checks: in the "
        "trivial-flux sector with the L = 4 loops excluded, k <= 4 charged "
        "links means vacuum (k = 0), impossible (k = 1, 2), a zero-N-ality "
        "winding triangle at L = 3 costing 3C/2 >= 3N/2 = 2C_F + C_F/2 + "
        "(N^2+5)/(4N) (k = 3), or a 4-cycle -- a plaquette at 2C_F, or a "
        "heavier irrep clearing 5C_F/2 by the shelf check; k >= 5 clears "
        "5C_F/2 by counting. So spec(H_E) below 5C_F/2 is exactly {0, 2C_F}: "
        f"the shell floats 2C_F = { {k: str(v) for k, v in below.items()} } above the vacuum and "
        f"gamma = C_F/2 = { {k: str(v) for k, v in gamma.items()} } below everything else, at "
        "EVERY L >= 3 -- the volume-uniform isolation the register said the "
        "carrier lacks is real once stated of the shell rather than of its "
        "internal splitting; every proved resolvent denominator C_F + C_rho/2 "
        "is >= 2*gamma, so no perturbative denominator degrades with volume. "
        "What stays open for G17: promoting gamma to u > 0 against the "
        "extensive perturbation, which norm bounds cannot do"
    )


@isolation.check(
    "the L = 4 loop exclusion is load-bearing exactly at N = 4",
    "G17 / PUB edition Lem. 14",
)
def _():
    flux = {n: 4 % n for n in range(3, 13)}
    in_sector = [n for n, f in flux.items() if f == 0]
    at_shell = simplify(4 * _CF / 2 - 2 * _CF) == 0
    return in_sector == [4] and at_shell, (
        "a straight L = 4 winding loop carries one irrep around a "
        "noncontractible 4-cycle, so with F its centre flux is 4 mod N: "
        f"{flux} -- nonzero, hence removed by the trivial-flux sector, for "
        "every N except exactly N = 4, where the loop sits in-sector at "
        "energy 4*C_F/2 = 2C_F, exactly ON the shell. The retained-shell "
        "lemma's explicit L = 4 exclusion is therefore redundant at every "
        "rank but SU(4), and load-bearing there: without it the SU(4), L = 4 "
        "shell would contain 48 non-plaquette states and the isolation "
        "statement would fail at that one rank-volume pair"
    )
