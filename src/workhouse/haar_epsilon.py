"""Exact SU(3) Haar inner products of Wilson words by epsilon-network reduction.

The pinned exact engine (``corpus-import/programs/hodge_o4_adjudication``)
expands every epsilon pair of a Haar projector into its 3! permutation deltas
and carries the integrand as set partitions. That is exact and, for the
balanced families, efficient: partitions merge as links are contracted. For
the epsilon families it is not: a link in the determinant family multiplies
the number of partitions by six and nothing merges them back, so six such
links give 6^6 partitions before a pure-six link's 456 branches begin, and one
integral of the shared-link pair's baryonic history takes 400 s and gigabytes
(runs/g3_shared_link_pair_2026-09-02). This module evaluates the same integrals
with the epsilons kept as epsilons.

After the projectors are inserted, the integrand is a closed network of deltas
and epsilon_3 tensors, and such a network reduces by three identities alone:

    eps_{abc} eps_{abc} = 6
    eps_{abc} eps_{abd} = 2 delta_{cd}
    eps_{abc} eps_{ade} = delta_{bd} delta_{ce} - delta_{be} delta_{cd}

with every closed delta loop worth N = 3. Only the third identity branches,
two ways, so a word with sixteen epsilons costs at most 2^8 leaves. Balanced
links are still contracted first with the engine's own per-link contraction,
which merges partitions; the epsilon families are then applied to each
surviving partition here. Where both methods apply they agree exactly
(tests/test_haar_epsilon.py pins closed forms, fast engine cases, and two
pure-six integrals the engine took 400 s each to produce).

Per-link projectors are the engine's own, transcribed into epsilon form:
determinant (3,0) as eps(rows) eps(cols)/6; mixed (4,1) as the engine's 4x4
pseudoinverse with an epsilon on the three remaining fundamentals; pure six as
sum_{p,q} pinv[p][q] I_p(rows) I_q(cols), I_p the engine's ten eps-eps
invariants and pinv its Gram pseudoinverse. Slots follow the engine's
``combine_bra_ket``: row slot 2i, column slot 2i + 1, the bra conjugated.
"""

from __future__ import annotations

import itertools
import sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from types import MappingProxyType

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "corpus-import" / "programs" / "hodge_o4_adjudication" / "src"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))
# corpus-import/ is pinned evidence: importing the engine must not write a
# __pycache__ into it (the corpus-integrity test walks the tree)
_bytecode = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    import DATA_SU3_Exact_MarkedCluster_m4_Colab as M  # noqa: E402
finally:
    sys.dont_write_bytecode = _bytecode

N = 3
State = M.State


def _sign(p):
    return M.permutation_sign(p)


# ---------------------------------------------------------------- projectors
# A term is (coefficient, deltas, epsilons): deltas a list of slot pairs,
# epsilons a list of ordered slot triples.


def _determinant_terms(occ):
    rows = tuple(2 * o for o in occ)
    cols = tuple(2 * o + 1 for o in occ)
    return [(F(1, 6), [], [rows, cols])]


def _mixed_terms(fund, anti):
    out = []
    for r in range(4):
        row_rest = [o for k, o in enumerate(fund) if k != r]
        for c in range(4):
            col_rest = [o for k, o in enumerate(fund) if k != c]
            base = M.MIXED_41_PSEUDOINVERSE[r][c]
            deltas = [(2 * fund[r], 2 * anti), (2 * fund[c] + 1, 2 * anti + 1)]
            eps = [tuple(2 * o for o in row_rest), tuple(2 * o + 1 for o in col_rest)]
            out.append((base, deltas, eps))
    return out


def _pure_six_terms(occ):
    parts = M.pure_six_partitions()
    pinv = M.pure_six_gram_pseudoinverse()
    out = []
    for p, (a, b) in enumerate(parts):
        for q, (a2, b2) in enumerate(parts):
            coef = pinv[p][q]
            if not coef:
                continue
            eps = [
                tuple(2 * occ[i] for i in a),
                tuple(2 * occ[i] for i in b),
                tuple(2 * occ[i] + 1 for i in a2),
                tuple(2 * occ[i] + 1 for i in b2),
            ]
            out.append((coef, [], eps))
    return out


def epsilon_terms(u, ub):
    """The epsilon-form projector of one unbalanced link, or [] if it vanishes."""
    a, b = len(u), len(ub)
    if (a, b) == (3, 0):
        return _determinant_terms(u)
    if (a, b) == (0, 3):
        return _determinant_terms(ub)
    if (a, b) == (4, 1):
        return _mixed_terms(tuple(u), ub[0])
    if (a, b) == (1, 4):
        return _mixed_terms(tuple(ub), u[0])
    if (a, b) == (6, 0):
        return _pure_six_terms(tuple(u))
    if (a, b) == (0, 6):
        return _pure_six_terms(tuple(ub))
    if (a - b) % 3:
        return []
    raise ValueError(f"Haar family {(a, b)} is not one the engine defines")


# ---------------------------------------------------------------- reduction


class _UF:
    __slots__ = ("p",)

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[a] = b

    def copy(self):
        c = _UF.__new__(_UF)
        c.p = self.p[:]
        return c


def reduce_network(uf, eps, nlabels, dead=frozenset()):
    """The value of a closed delta/epsilon network.

    ``uf`` identifies labels (the deltas), ``eps`` is a list of
    ``(sign, [l1, l2, l3])``, and ``dead`` holds the labels an already
    contracted epsilon pair consumed, which are not loops. Every label of a
    closed network appears exactly twice among the epsilons or is a loop.
    """
    if not eps:
        roots = {uf.find(x) for x in range(nlabels)} - dead
        return F(N) ** len(roots)
    sign0, (a, b, c) = eps[0]
    a, b, c = uf.find(a), uf.find(b), uf.find(c)
    if len({a, b, c}) < 3:
        return F(0)
    rest = eps[1:]
    where = {}
    for k, (_s, labs) in enumerate(rest):
        for lab in labs:
            r = uf.find(lab)
            if r in (a, b, c):
                if r in where:
                    raise AssertionError("a label appears three times")
                where[r] = k
    if len(where) != 3:
        raise AssertionError("open index in a closed network")
    ka, kb, kc = where[a], where[b], where[c]
    if ka == kb == kc:
        s, labs = rest[ka]
        labs_r = [uf.find(lab) for lab in labs]
        order = [labs_r.index(x) for x in (a, b, c)]
        new = [e for k, e in enumerate(rest) if k != ka]
        return (
            6 * sign0 * s * _sign(tuple(order)) * reduce_network(uf, new, nlabels, dead | {a, b, c})
        )
    if ka in (kb, kc) or kb == kc:
        if ka == kb:
            k, shared, lone = ka, (a, b), c
        elif ka == kc:
            k, shared, lone = ka, (a, c), b
        else:
            k, shared, lone = kb, (b, c), a
        s, labs = rest[k]
        labs_r = [uf.find(lab) for lab in labs]
        perm0 = [[a, b, c].index(x) for x in (shared[0], shared[1], lone)]
        other = next(x for x in labs_r if x not in shared)
        perm1 = [labs_r.index(x) for x in (shared[0], shared[1], other)]
        coef = 2 * sign0 * s * _sign(tuple(perm0)) * _sign(tuple(perm1))
        uf2 = uf.copy()
        uf2.union(lone, other)
        new = [e for kk, e in enumerate(rest) if kk != k]
        return coef * reduce_network(uf2, new, nlabels, dead | set(shared))
    k = ka
    s, labs = rest[k]
    labs_r = [uf.find(lab) for lab in labs]
    ia = labs_r.index(a)
    d, e = [x for i, x in enumerate(labs_r) if i != ia]
    perm1 = [labs_r.index(x) for x in (a, d, e)]
    coef = sign0 * s * _sign(tuple(perm1))
    new = [ee for kk, ee in enumerate(rest) if kk != k]
    uf_p = uf.copy()
    uf_p.union(b, d)
    uf_p.union(c, e)
    uf_m = uf.copy()
    uf_m.union(b, e)
    uf_m.union(c, d)
    dead2 = dead | {a}
    return coef * (
        reduce_network(uf_p, new, nlabels, dead2) - reduce_network(uf_m, new, nlabels, dead2)
    )


# ---------------------------------------------------------------- the integral


def triality(word) -> tuple:
    """Per-link net charge mod 3; two words with different signatures are orthogonal."""
    sig = defaultdict(int)
    for lab, is_u in word.occ:
        sig[lab] += 1 if is_u else -1
    return tuple(sorted((lab, n % 3) for lab, n in sig.items() if n % 3))


def haar_inner(left: State, right: State) -> F:
    """<left|right>, exact.

    Balanced links (a, a) are contracted first with the engine's own per-link
    contraction, which merges the resulting set partitions; the epsilon
    families (determinant, mixed, pure six) are then applied to each surviving
    partition by network reduction.
    """
    occurrences, partition = M.combine_bra_ket(left, right)
    by_link: dict = defaultdict(lambda: {True: [], False: []})
    for index, (link, is_u) in enumerate(occurrences):
        by_link[link][is_u].append(index)
    balanced, epsilon = [], []
    for link in sorted(by_link):
        a, b = len(by_link[link][True]), len(by_link[link][False])
        if (a - b) % 3:
            return F(0)
        (balanced if a == b else epsilon).append(link)
    states = {tuple(partition): F(1)}
    for link in balanced:
        u, ub = by_link[link][True], by_link[link][False]
        nxt: dict = defaultdict(F)
        for current, coefficient in states.items():
            for merged, c in M.contract_link_partition(
                current, u, ub, M.DEFAULT_HAAR_ROUTER, MappingProxyType({})
            ).items():
                nxt[merged] += coefficient * c
        states = {k: v for k, v in nxt.items() if v}
        if not states:
            return F(0)
    if not epsilon:
        return sum((c * F(N ** len(set(item)), 1) for item, c in states.items()), F(0))
    per_link = [epsilon_terms(by_link[link][True], by_link[link][False]) for link in epsilon]
    total = F(0)
    for part, weight in states.items():
        nlabels = max(part) + 1
        for combo in itertools.product(*per_link):
            coef = weight
            uf = _UF(nlabels)
            eps = []
            for c, deltas, epsl in combo:
                coef *= c
                for s1, s2 in deltas:
                    uf.union(part[s1], part[s2])
                for tri in epsl:
                    eps.append((1, [part[s] for s in tri]))
            if coef:
                total += coef * reduce_network(uf, eps, nlabels)
    return total


def inner(bra: State, vec: dict) -> F:
    """sum_w c_w <bra|w>, skipping every word the triality signature rules out."""
    tb = triality(bra)
    total = F(0)
    for w, c in vec.items():
        if triality(w) == tb:
            total += c * haar_inner(bra, w)
    return total
