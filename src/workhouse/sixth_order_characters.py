"""One face, any rank: the plaquette energy series in the SU(N) character basis.

An independent evaluation of the single-face sixth-order energies that shares
nothing with ``loopcalc``: no loop words, no Fierz rewiring, no Weingarten
function. The single plaquette holonomy is one Haar link; its gauge-invariant
functions are the characters ``chi_(lam; mu)`` of the mixed irreps of SU(N),
orthonormal under Haar measure, with

    H0 chi_(lam; mu) = 2 C2(lam; mu) chi_(lam; mu)       (four links of C2/2 each)
    chi_F chi_(lam; mu)    = sum_(lam + box) chi_(lam+box; mu) + sum_(mu - box) chi_(lam; mu-box)
    chi_Fbar chi_(lam; mu) = sum_(mu + box) chi_(lam; mu+box) + sum_(lam - box) chi_(lam-box; mu)

which are the Pieri rules for a rank large enough that no column reaches N
boxes and no determinant identification occurs. Through order six the words
carry at most eight boxes, so the rules hold for N >= 9; the Casimir is
``symbolic_rank.casimir_symbolic`` (rank-generic in the same range).

The model space is the degenerate pair {(F; -), (-; F)} (the plaquette and its
conjugate, which mix through the vacuum from second order on at every rank),
or the vacuum {(-; -)}. The Bloch recursion with intermediate normalisation,

    K_n = P V chi_(n-1),   chi_n = D (V chi_(n-1) - sum_(j=1..n-1) chi_(n-j) K_j),

gives K_n on the model space. Charge conjugation makes every K_n of the form
a I + b sigma_x, so all of them commute and the canonical Hermitian metric
changes nothing: the C-odd and C-even energies are ``a - b`` and ``a + b``
order by order. The sign of V is a parameter (``loopcalc`` uses +sum of face
words, the note ``G9_SIXTH_ORDER_COMBINED`` uses -(chi3+chi3bar); even orders
agree).
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction

from . import symbolic_rank as SR

PLAQUETTE = [((1,), ()), ((), (1,))]
VACUUM = [((), ())]


def _add_box(lam: tuple) -> list[tuple]:
    out = []
    for i in range(len(lam) + 1):
        new = list(lam) + [0]
        if i == 0 or new[i - 1] > new[i]:
            new[i] += 1
            out.append(tuple(x for x in new if x))
    return out


def _remove_box(lam: tuple) -> list[tuple]:
    out = []
    for i in range(len(lam)):
        if i == len(lam) - 1 or lam[i] > lam[i + 1]:
            new = list(lam)
            new[i] -= 1
            out.append(tuple(x for x in new if x))
    return out


def multiply_fundamental(vec: dict, anti: bool) -> dict:
    """chi_F (or chi_Fbar) times a vector of characters, by the Pieri rules."""
    out: dict = defaultdict(lambda: 0)
    for (lam, mu), c in vec.items():
        if anti:
            for nu in _add_box(mu):
                out[(lam, nu)] += c
            for nu in _remove_box(lam):
                out[(nu, mu)] += c
        else:
            for nu in _add_box(lam):
                out[(nu, mu)] += c
            for nu in _remove_box(mu):
                out[(lam, nu)] += c
    return {k: v for k, v in out.items() if v}


def casimir_rank(N: int):
    """The SU(N) Casimir of (lam; mu) at one integer rank, as a Fraction."""

    def c2(lam, mu):
        a, b = sum(lam), sum(mu)
        return (
            Fraction((a + b) * N + SR._content_sum(lam) + SR._content_sum(mu), 1)
            - Fraction((a - b) ** 2, N)
        ) / 2

    return c2


def bloch_series(order: int, model=None, sign: int = 1, casimir=None) -> dict:
    """K_0..K_order on the model space with V = sign * (chi_F + chi_Fbar).

    ``casimir(lam, mu)`` returns C2; by default the Q(N) form. Returns the K
    matrices (lists of lists), the odd/even energies when the model space is
    the plaquette pair, and every chi_n.
    """
    model = list(PLAQUETTE if model is None else model)
    c2 = casimir or SR.casimir_symbolic
    zero = c2((), ())
    zero = zero - zero
    m = len(model)

    def energy(state):
        lam, mu = state
        return 2 * c2(lam, mu)

    def V(vec):
        out = multiply_fundamental(vec, False)
        for k, v in multiply_fundamental(vec, True).items():
            out[k] = out.get(k, zero) + v
        return {k: v * sign for k, v in out.items() if v}

    e0 = energy(model[0])
    if any(energy(s) != e0 for s in model):
        raise ValueError("model states are not degenerate")
    chi = [[{s: zero + 1} for s in model]]
    K = [[[e0 if i == j else zero for j in range(m)] for i in range(m)]]
    for n in range(1, order + 1):
        vchi = [V(chi[n - 1][j]) for j in range(m)]
        Kn = [[vchi[j].get(model[i], zero) for j in range(m)] for i in range(m)]
        K.append(Kn)
        chi_n = []
        for j in range(m):
            rhs = dict(vchi[j])
            for lag in range(1, n):
                for i in range(m):
                    if K[lag][i][j]:
                        for state, c in chi[n - lag][i].items():
                            rhs[state] = rhs.get(state, zero) - c * K[lag][i][j]
            vec = {}
            for state, c in rhs.items():
                if state in model or not c:
                    continue
                e = energy(state)
                if e == e0:
                    raise ValueError(f"unprojected degeneracy with the model space: {state}")
                vec[state] = c / (e0 - e)
            chi_n.append(vec)
        chi.append(chi_n)
    out = {"K": K, "chi": chi, "model": model}
    if m == 2:
        out["odd"] = [k[0][0] - k[0][1] for k in K]
        out["even"] = [k[0][0] + k[0][1] for k in K]
        out["symmetric"] = all(k[0][1] == k[1][0] and k[0][0] == k[1][1] for k in K)
    else:
        out["energies"] = [k[0][0] for k in K]
    return out
