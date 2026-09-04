"""The global-assembly premises, machine-checked.

The publication edition upgrades the conditional second-order torus assembly
to a theorem (PUB edition Thm. 16) by proving its two premises: the retained
shell (Lem. 14 — the E = 2 C_F eigenspace is exactly the one-plaquette span)
and second-order process exhaustion (Lem. 15 — every off-diagonal route's two
V-insertions sit on p and p' themselves). Both proofs rest on finite cubical
combinatorics plus two classical Casimir-minimality facts. This suite carries
the combinatorial cores exhaustively and pins the Casimir inputs on a bounded
window, so the premises stop being prose.

What is and is not established here, said plainly: the enumerations below are
exhaustive for the stated L and are the complete geometric content of the two
proofs (larger L adds translates of configurations that already fit in a
2-site-per-axis window). The two representation-theoretic inputs — C(rho) is
minimised on nontrivial irreps by F and F-bar alone, and on the nonzero root
lattice by the adjoint — are classical (minuscule / quasi-minuscule
minimality); the bounded-window check pins them on every dominant weight a
small shell can reach, it does not re-prove the general statements.
"""

from __future__ import annotations

from itertools import product

from sympy import Rational, simplify

from .. import constants as K
from ._core import _suite

# ==========================================================================
assembly = _suite("global assembly: retained shell and process completeness")


# --------------------------------------------------------------------------
# The periodic cubic link graph, in integers only. A link is (site, axis)
# with site a coordinate triple mod L; it joins x and x + e_axis. A face is
# the 4-link boundary of the elementary square at x spanned by axes i < j.
# Deliberately self-contained rather than reusing workhouse.torus: these are
# unsigned link SETS (which links a route can touch), not signed boundary
# matrices, and an independent construction is worth more than a shared one.
# --------------------------------------------------------------------------


def _shift(x, axis, ell, step=1):
    y = list(x)
    y[axis] = (y[axis] + step) % ell
    return tuple(y)


def _links(ell):
    return [(x, i) for x in product(range(ell), repeat=3) for i in range(3)]


def _endpoints(link, ell):
    x, i = link
    return x, _shift(x, i, ell)


def _incident(ell):
    """site -> list of (neighbour site, link)."""
    out = {x: [] for x in product(range(ell), repeat=3)}
    for link in _links(ell):
        a, b = _endpoints(link, ell)
        out[a].append((b, link))
        out[b].append((a, link))
    return out


def _cycles(ell, length):
    """Every simple cycle of the given length, as a frozenset of links."""
    incident = _incident(ell)
    found = set()
    for start in incident:
        stack = [(start, (), frozenset())]
        while stack:
            site, path, used = stack.pop()
            if len(path) == length - 1:
                for nxt, link in incident[site]:
                    if nxt == start and link not in used:
                        found.add(used | {link})
                continue
            for nxt, link in incident[site]:
                if link in used or nxt == start or nxt in {s for s, _l in path}:
                    continue
                stack.append((nxt, path + ((site, link),), used | {link}))
    return found


def _faces(ell):
    """The 3 L^3 elementary faces, each as its frozenset of 4 links."""
    out = []
    for x in product(range(ell), repeat=3):
        for i, j in ((0, 1), (0, 2), (1, 2)):
            out.append(frozenset({(x, i), (_shift(x, i, ell), j), (_shift(x, j, ell), i), (x, j)}))
    return out


def _straight_lines(ell):
    """The 3 L^2 straight winding loops: all L links of one axis-parallel line."""
    out = set()
    for i in range(3):
        for x in product(range(ell), repeat=3):
            if x[i] == 0:
                out.add(frozenset((_shift(x, i, ell, s), i) for s in range(ell)))
    return out


@assembly.check(
    "the L >= 3 torus link graph is simple, and L = 2 is the counterexample",
    "PUB edition Lem. 14",
)
def _():
    mult = {}
    for ell in (2, 3, 4, 5):
        pairs = {}
        for link in _links(ell):
            a, b = _endpoints(link, ell)
            pairs[frozenset((a, b))] = pairs.get(frozenset((a, b)), 0) + 1
        mult[ell] = max(pairs.values())
    ok = mult == {2: 2, 3: 1, 4: 1, 5: 1}
    return ok, (
        f"max links joining one site pair: { {k: v for k, v in mult.items()} } — at "
        "L = 2 the links (x, i) and (x + e_i, i) join the SAME pair, so the "
        "parallel-link configurations the junction argument must exclude "
        "genuinely occur there; at L = 3, 4, 5 no pair of sites is joined "
        "twice, which is the 'no parallel links' input the lemma's valence "
        "argument consumes, and why the lemma starts at L = 3"
    )


@assembly.check(
    "the only cycles shorter than 4 are the 3L^2 winding triangles, at L = 3 alone",
    "PUB edition Lem. 14",
)
def _():
    threes = {ell: _cycles(ell, 3) for ell in (3, 4, 5)}
    straight = _straight_lines(3)
    ok = len(threes[3]) == 27 and threes[3] == straight and not threes[4] and not threes[5]
    return ok, (
        f"3-cycles: L=3 -> {len(threes[3])} (= 3L^2 = 27, every one a straight "
        f"winding line), L=4 -> {len(threes[4])}, L=5 -> {len(threes[5])} — the "
        "odd-L torus is not bipartite and DOES have odd cycles, exactly these; "
        "a charged sublattice at E = 2 C_F has at most 4 links, every charged "
        "site has degree >= 2, and a min-degree-2 link set of size <= 4 is a "
        "single cycle (two disjoint cycles need >= 6 links), so with the "
        "4-cycle census this enumeration exhausts the lemma's geometry"
    )


@assembly.check(
    "every 4-cycle is an elementary face, except exactly the 3L^2 straight loops at L = 4",
    "PUB edition Lem. 14",
)
def _():
    detail = {}
    ok = True
    for ell in (3, 4, 5):
        cycles = _cycles(ell, 4)
        faces = set(_faces(ell))
        extra = cycles - faces
        expected_extra = _straight_lines(ell) if ell == 4 else set()
        ok = ok and faces <= cycles and extra == expected_extra
        detail[ell] = (len(cycles), len(faces), len(extra))
    ok = ok and detail == {3: (81, 81, 0), 4: (240, 192, 48), 5: (375, 375, 0)}
    return ok, (
        f"(4-cycles, elementary faces, non-face 4-cycles) = {detail}: at L = 3 "
        "and L = 5 every 4-cycle bounds an elementary square; at L = 4 exactly "
        "the 3L^2 = 48 straight winding loops appear besides the faces, and "
        "they are what the L = 4 sector qualification removes — so the "
        "E = 2 C_F eigenspace is spanned by plaquette states and nothing else"
    )


@assembly.check(
    "winding loops clear the shell: 3N/2 exceeds 2 C_F at every rank",
    "PUB edition Lem. 14",
)
def _():
    cf = (K.N**2 - 1) / (2 * K.N)
    margin = simplify(Rational(3, 2) * K.N - 2 * cf)
    closed = simplify(margin - (K.N**2 + 2) / (2 * K.N)) == 0
    at_ranks = {n: margin.subs(K.N, n) for n in (3, 4, 5)}
    plaquette = simplify(4 * cf / 2 - 2 * cf) == 0
    return closed and all(v > 0 for v in at_ranks.values()) and plaquette, (
        "a winding triangle carries one zero-N-ality irrep rho around a "
        "noncontractible cycle (nonzero N-ality is removed by the trivial "
        "centre-flux sector), and C(rho) >= C_Adj = N there, so its energy "
        "3C(rho)/2 >= 3N/2; the margin over the shell is 3N/2 - 2C_F = "
        f"(N^2+2)/(2N) exactly, at N = 3, 4, 5: "
        f"{ {k: str(v) for k, v in at_ranks.items()} }; "
        "a 4-cycle carrying F costs 4 * C_F/2 = 2 C_F exactly, which is why "
        "plaquettes and only plaquettes sit at the shell energy"
    )


@assembly.check(
    "Casimir minimality pinned on a bounded window: F and F-bar, then the adjoint",
    "PUB edition Lem. 14",
)
def _():
    # C(lambda) for SU(N) from the partition mu_j = sum_{i >= j} a_i of the
    # Dynkin labels a: C = (sum_j mu_j (mu_j + N + 1 - 2j) - |mu|^2 / N) / 2,
    # normalised so C(F) = (N^2 - 1)/(2N) and C(Adj) = N.
    def casimir(labels, n):
        mu = [sum(labels[i:]) for i in range(len(labels))]
        total = sum(mu)
        raw = sum(Rational(m * (m + n + 1 - 2 * (j + 1))) for j, m in enumerate(mu))
        return Rational(raw - Rational(total**2, n), 2)

    bound = 5
    ok = True
    window = {}
    for n in range(3, 9):
        cf = Rational(n**2 - 1, 2 * n)
        fund = tuple([1] + [0] * (n - 2))
        antifund = tuple([0] * (n - 2) + [1])
        adjoint = tuple([1] + [0] * (n - 3) + [1])
        seen = 0
        for labels in product(range(bound + 1), repeat=n - 1):
            if not any(labels) or sum(labels) > bound:
                continue
            seen += 1
            c = casimir(labels, n)
            nality = sum((i + 1) * a for i, a in enumerate(labels)) % n
            if c < cf or (c == cf and labels not in (fund, antifund)):
                ok = False
            if nality == 0 and (c < n or (c == n and labels != adjoint)):
                ok = False
        checked = casimir(fund, n) == cf and casimir(antifund, n) == cf and casimir(adjoint, n) == n
        ok = ok and checked
        window[n] = seen
    return ok, (
        f"every nontrivial dominant weight with label sum <= {bound} at N = 3..8 "
        f"({window} weights) has C >= C_F, equality exactly at omega_1 and "
        "omega_(N-1), and every zero-N-ality one has C >= N, equality exactly "
        "at the adjoint — the bounded-window pin of the lemma's two classical "
        "inputs (minuscule and quasi-minuscule minimality); the unbounded "
        "statements are classical, not re-proved here"
    )


@assembly.check(
    "two distinct faces share at most one link, exhaustively at L = 3, 4, 5",
    "PUB edition Thm. 10 / Lem. 15",
)
def _():
    detail = {}
    ok = True
    for ell in (3, 4, 5):
        faces = _faces(ell)
        max_shared = 0
        neighbours = 0
        for a in range(len(faces)):
            for b in range(a + 1, len(faces)):
                shared = len(faces[a] & faces[b])
                max_shared = max(max_shared, shared)
                neighbours += shared == 1
        per_face = Rational(2 * neighbours, len(faces))
        detail[ell] = (max_shared, per_face)
        ok = ok and max_shared == 1 and per_face == 12
    return ok, (
        f"(max links shared by a face pair, shared-link neighbours per face) = "
        f"{ {k: (v[0], str(v[1])) for k, v in detail.items()} } at L = 3, 4, 5 — "
        "the opening geometric input of the shared-link law, enumerated over "
        "every distinct face pair rather than asserted; two faces sharing a "
        "link span at most two sites per axis, so these windows already "
        "exhibit every local configuration and larger L adds translates only"
    )


@assembly.check(
    "the two insertions are pinned to p and p': coverage arithmetic, exhaustively",
    "PUB edition Lem. 15",
)
def _():
    detail = {}
    ok = True
    for ell in (3, 4, 5):
        faces = _faces(ell)
        min_private = {1: 8, 0: 8}  # |p \ p'| keyed by shared-link count
        for a in range(len(faces)):
            for b in range(len(faces)):
                if a == b:
                    continue
                shared = len(faces[a] & faces[b])
                private = len(faces[a] - faces[b])
                min_private[shared] = min(min_private[shared], private)
        detail[ell] = (min_private[1], min_private[0])
        ok = ok and min_private == {1: 3, 0: 4}
    return ok, (
        f"min |p \\ p'| over distinct face pairs = {detail} (3 sharing a link, "
        "4 otherwise), while any face other than p carries at most one link of "
        "p (previous check) — so two V-insertions with neither equal to p "
        "cover at most 2 of the >= 3 links in p \\ p', which the resolvent "
        "leaves untouched: one insertion must BE p, and symmetrically p'. "
        "Disjoint pairs then die on the C-parity selection rule <0|V|p,-> = 0 "
        "recorded with ell_N (C13), and shared-link pairs are exhausted by the "
        "four fusion channels of the all-rank law — process completeness"
    )
