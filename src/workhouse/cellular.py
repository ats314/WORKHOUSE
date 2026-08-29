"""G5: the primitive cell-completion Haar-resolvent coefficients, re-derived.

The corpus prints (transcript ``#-Final-unified-theory.txt`` ~170; GLUEBALL v3_1
~1174) the restricted primitive color law

    c_{r,prim}(N) = S_r / (N^r C_F^(r-1)) = 2^(r-1) S_r / (N (N^2-1)^(r-1)),

with the table: tetrahedron r=2 -> -8/(N(N^2-1)); triangular prism r=3 ->
64/(N(N^2-1)^2); cube r=4 -> -160/(N(N^2-1)^3); pentagonal prism r=5 ->
1120/(N(N^2-1)^4). For the tetrahedral row NO artifact and NO reference SHA
exist anywhere (C15; the restored-payloads FINDING pins the absence), and the
mobility theorem itself says the coefficient "remains to be calculated"
(THM_FLUX_hodge_cellular_circuit_mobility_theorem.md §5). This module is the
re-derivation that closes C15, from three stated ingredients, each anchored to
something this repository already certifies or the corpus independently prints:

1. **Merge factor.** A primitive insertion merges a fundamental Wilson loop
   with the current loop along a connected, oppositely oriented shared path.
   The only group integral involved is the fundamental-pair Haar moment

       int dU U_ij (U^dag)_kl = (1/N) delta_il delta_jk,

   whose 1/N is the n=1 Weingarten value — the inverse of the 1x1 Gram matrix
   [N], the same Gram-inverse route the published-comparisons suite uses at
   n=2. ``merge_moment`` below contracts Tr(A u_1..u_k) Tr(B u_k~..u_1~) link
   by link and shows the result is exactly (1/N) Tr(AB) for every shared-path
   length k: the transcript's "contributes 1/N, independently of the length of
   that common path", derived rather than assumed. (The shipped prism notebook
   NB_HAAR_prismatic_minimal_cell_escape_test.ipynb *assumes* this flat 1/N;
   this is the missing group-theoretic step.)

2. **Electric convention.** Isotropic Kogut-Susskind H_0 = (1/2) sum_e E_e^2,
   so a simple fundamental loop of length L costs L*C_F/2 with
   C_F = (N^2-1)/(2N). At N=3 this is the certified pair E_SIDE = 8/3 (L=4)
   and E_CAP = 10/3 (L=5) of the pentagonal suite, and the L=4 case is the
   certified one-plaquette rest energy e_flat(0) = 8/3. Each intermediate
   simple loop supplies one resolvent 1/(E_0 - E_j); all intermediates are
   longer than the endpoints, so every denominator is negative and the history
   sign is (-1)^(r-1) — which is exactly the (-1)^(r+1) the quarantined master
   records as erratum 9 ("Positive counts S_r require the factor (-1)^(r+1)").

3. **Geometry.** Endpoints are two faces of the cell in that family's retained
   sector; the other faces are inserted in every temporal order; the state
   after each insertion must remain a single simple loop, each merge must be
   along a connected oppositely oriented path (both enforced, not assumed).

The engine reproduces, from this one convention, every certified or printed
instance at once: the cube's three temporal classes (-8,-8,-4) of multiplicity
eight (818.txt ~3963) and c_4 = -160/(N(N^2-1)^3) -> -5/48 = CUBE_COMPLETION_4
with alpha_pen = 4|c_4|; the prism square-sector S_3 = 16 -> 64/(N(N^2-1)^2);
the pentagonal cap sector's "120 histories, S_5 = 70" -> 35/384 at SU(3); and
the shipped notebook's cap-sector Catalan family 2^(n-1) C(2n-2,n-1) — whose
n=3 value 24 is a *different endpoint sector* of the same prism, not a rival
value of 64 (818.txt ~3402 records the supersession). Only then is the same
convention read at r=2: the tetrahedron has two histories, each with the single
4-link intermediate loop, S_2 = -4, and

    c_{2,prim}(N) = -8 / (N (N^2-1)),

exactly the asserted C15 value.

Scope: these are the *primitive* (square-free, simple-loop channel)
coefficients. Adjoint/Fierz channel resolvents, folded and linked terms, and
determinant sectors are explicitly outside the law — the corpus itself keeps
them separate (the SU(3) fifth-order determinant dressing delta c_{5,det} != 0
corrects the pentagonal primitive value, C18). Nothing here asserts full
physical mobility of the tetrahedral carrier; that survival question (Q
projection, compression) is U3's, not this module's.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations

from sympy import Matrix, Rational, Symbol, binomial, simplify, sympify

N = Symbol("N", positive=True)

#: Fundamental Casimir, the unit the corpus's law is written in.
C_F = (N**2 - 1) / (2 * N)


# ---------------------------------------------------------------------------
# The merge lemma: 1/N per insertion, independent of the shared-path length
# ---------------------------------------------------------------------------


def weingarten_1():
    """The n=1 Weingarten value: inverse of the 1x1 Gram matrix [N]."""
    return Matrix([[N]]).inv()[0, 0]


def weingarten_2():
    """The order-2 Weingarten pair (Wg(e), Wg((12))), from the Gram inverse.

    The Gram matrix on S_2 is G[s,t] = N**cycles(s·t^-1): cycles(e) = 2,
    cycles((12)) = 1. One home for the matrix the published-comparisons suite
    previously built inline three times.
    """
    wg = Matrix([[N**2, N], [N, N**2]]).inv()
    return simplify(wg[0, 0]), simplify(wg[0, 1])


def _rotate_to_last(word, pos):
    return word[pos + 1 :] + word[: pos + 1]


def _contract_link(traces, link):
    """Integrate one link over Haar measure inside a product of trace words.

    A trace word is a list of ``(letter, orientation)`` with orientation +1 for
    U, -1 for U-dagger, 0 for an opaque spectator segment. The link must occur
    exactly once with each orientation. The two consequences of the
    fundamental-pair moment are applied verbatim:

        Tr(X u) Tr(Y u~) -> (1/N) Tr(X Y)        (different traces)
        Tr(X u Y u~)     -> (1/N) Tr(X) Tr(Y)    (same trace)

    with Tr(empty) = Tr(I) = N. Returns ``(factor, new_traces)``.
    """
    locs = [
        (t_i, w_i, orient)
        for t_i, word in enumerate(traces)
        for w_i, (letter, orient) in enumerate(word)
        if letter == link
    ]
    if len(locs) != 2 or locs[0][2] != -locs[1][2]:
        raise ValueError(f"{link}: not a fundamental (U, U-dagger) pair")
    (t1, w1, _), (t2, w2, _) = sorted(locs, key=lambda x: -x[2])
    factor = 1 / N
    if t1 != t2:
        merged = _rotate_to_last(traces[t1], w1)[:-1] + _rotate_to_last(traces[t2], w2)[:-1]
        new = [w for i, w in enumerate(traces) if i not in (t1, t2)] + [merged]
    else:
        rot = _rotate_to_last(traces[t1], w1)
        k = next(i for i, (le, o) in enumerate(rot) if le == link and o == -1)
        new = [w for i, w in enumerate(traces) if i != t1] + [rot[:k], rot[k + 1 : -1]]
    closed = sum(1 for w in new if not w)
    return factor * N**closed, [w for w in new if w]


def merge_moment(path_length):
    """Integrate Tr(A u_1..u_k) Tr(B u_k~..u_1~) over the k shared links.

    Returns ``(coefficient, remaining_trace_letters)``; the lemma is that the
    coefficient is exactly 1/N for every k and the remainder is Tr(AB).
    """
    k = path_length
    t1 = [("A", 0)] + [(f"u{i}", +1) for i in range(1, k + 1)]
    t2 = [("B", 0)] + [(f"u{i}", -1) for i in range(k, 0, -1)]
    traces, coeff = [t1, t2], sympify(1)
    for i in range(1, k + 1):
        factor, traces = _contract_link(traces, f"u{i}")
        coeff *= factor
    return simplify(coeff), [[letter for letter, _ in word] for word in traces]


# ---------------------------------------------------------------------------
# Oriented cells and the primitive history enumeration
# ---------------------------------------------------------------------------


def _face_edges(face):
    return [(face[i], face[(i + 1) % len(face)]) for i in range(len(face))]


@dataclass(frozen=True)
class Cell:
    """A closed coherently oriented cell surface: every edge in exactly two
    faces, with opposite orientations — which is what makes every shared path
    oppositely oriented and every primitive circuit have unit coefficients."""

    name: str
    faces: tuple[tuple, ...]

    def __post_init__(self):
        directed = [e for f in self.faces for e in _face_edges(f)]
        counts = Counter(directed)
        if any(v != 1 for v in counts.values()):
            raise ValueError(f"{self.name}: repeated directed edge")
        for a, b in directed:
            if (b, a) not in counts:
                raise ValueError(f"{self.name}: edge {(a, b)} lacks its opposite partner")

    def undirected_edges(self):
        return sorted({frozenset(e) for f in self.faces for e in _face_edges(f)}, key=sorted)

    def boundary_matrix(self):
        """Signed edge-by-face incidence B_2 (each edge oriented by sorted order)."""
        index = {e: i for i, e in enumerate(self.undirected_edges())}
        m = Matrix.zeros(len(index), len(self.faces))
        for j, f in enumerate(self.faces):
            for a, b in _face_edges(f):
                m[index[frozenset((a, b))], j] += 1 if (a, b) == tuple(sorted((a, b))) else -1
        return m


def _connected(undirected_edges):
    verts = {v for e in undirected_edges for v in e}
    adj = {v: set() for v in verts}
    for a, b in undirected_edges:
        adj[a].add(b)
        adj[b].add(a)
    stack, seen = [next(iter(verts))], set()
    while stack:
        v = stack.pop()
        if v not in seen:
            seen.add(v)
            stack.extend(adj[v] - seen)
    return seen == verts


def _merge(loop, face):
    """Merge an oriented face into a directed loop, enforcing every hypothesis
    of the primitive law: the shared edges are oppositely oriented, form one
    connected path, and the residue is a single simple closed loop."""
    fedges = _face_edges(face)
    loopset = set(loop)
    if any(e in loopset for e in fedges):
        raise ValueError("shared edge with the SAME orientation: not a fundamental-pair merge")
    shared = [e for e in fedges if (e[1], e[0]) in loopset]
    if not shared:
        raise ValueError("disconnected insertion: no shared edge")
    if not _connected([tuple(e) for e in shared]):
        raise ValueError("shared edges do not form a connected path")
    reversed_shared = {(b, a) for a, b in shared}
    new = [e for e in loop if e not in reversed_shared] + [e for e in fedges if e not in shared]
    if len({frozenset(e) for e in new}) != len(new):
        raise ValueError("residue repeats an undirected edge: not square-free")
    succ = {}
    for a, b in new:
        if a in succ:
            raise ValueError("residue is not a simple loop")
        succ[a] = b
    v, steps = new[0][0], 0
    while True:
        v, steps = succ[v], steps + 1
        if v == new[0][0] or steps > len(new):
            break
    if steps != len(new):
        raise ValueError("residue splits into more than one loop")
    return new, len(shared)


@dataclass
class History:
    """One temporal ordering of the insertions, with its exact resolvent data."""

    order: tuple[int, ...]
    lengths: tuple[int, ...]  # intermediate simple-loop lengths
    max_shared: int  # longest merged shared path, for the merge lemma's reach

    def weight_cf(self, endpoint_length):
        """prod_j 1/((E_0 - E_j)/C_F) with E(L) = L*C_F/2: the law's S-unit."""
        w = Rational(1)
        for length in self.lengths:
            w *= Rational(2, endpoint_length - length)
        return w

    def weight_e0(self, endpoint_length):
        """The same product in units of E_0 = endpoint rest energy — the
        '(common units)' of 818.txt's cube amplitudes (-8, -8, -4)."""
        w = Rational(1)
        for length in self.lengths:
            w *= Rational(endpoint_length, endpoint_length - length)
        return w


def histories(cell, p_idx, q_idx):
    """Every primitive temporal history from face p to face q."""
    p, q = cell.faces[p_idx], cell.faces[q_idx]
    if len(p) != len(q):
        raise ValueError("endpoints are not degenerate")
    others = [f for k, f in enumerate(cell.faces) if k not in (p_idx, q_idx)]
    target = {(b, a) for a, b in _face_edges(q)}
    out = []
    for order in permutations(range(len(others))):
        loop, lengths, widest = list(_face_edges(p)), [], 1
        try:
            for k in order[:-1]:
                loop, shared = _merge(loop, others[k])
                lengths.append(len(loop))
                widest = max(widest, shared)
            loop, shared = _merge(loop, others[order[-1]])
            widest = max(widest, shared)
        except ValueError:
            continue
        if set(loop) != target:
            raise ValueError("completed loop is not the reversed endpoint boundary")
        out.append(History(order, tuple(lengths), widest))
    return out


def s_value(cell, p_idx, q_idx):
    """The signed count S_r: sum over histories of the resolvent product in
    C_F units. The corpus's unsigned S_r is |S_r|; the sign is the parity
    (-1)^(r-1) of the r-1 negative denominators (erratum 9)."""
    ell = len(cell.faces[p_idx])
    hist = histories(cell, p_idx, q_idx)
    return sum(h.weight_cf(ell) for h in hist), hist


def c_prim(cell, p_idx, q_idx):
    """The primitive local coefficient c_{r,prim}(N) = S_r/(N^r C_F^(r-1))."""
    r = len(cell.faces) - 2
    s, hist = s_value(cell, p_idx, q_idx)
    return simplify(s / (N**r * C_F ** (r - 1))), s, hist


# ---------------------------------------------------------------------------
# The cells
# ---------------------------------------------------------------------------


def prism(sides):
    """The n-gonal prism, coherently oriented: 2 caps + n squares. n=4 is the
    (combinatorial) cube. Cap endpoints are faces 0, 1."""
    bot = tuple(f"A{i}" for i in range(sides, 0, -1))
    top = tuple(f"B{i}" for i in range(1, sides + 1))
    squares = tuple(
        (f"A{i}", f"A{i % sides + 1}", f"B{i % sides + 1}", f"B{i}") for i in range(1, sides + 1)
    )
    return Cell(f"{sides}-gonal prism", (bot, top, *squares))


TETRAHEDRON = Cell("tetrahedron", ((1, 2, 3), (1, 3, 4), (1, 4, 2), (2, 4, 3)))
TRIANGULAR_PRISM = prism(3)
CUBE = prism(4)
PENTAGONAL_PRISM = prism(5)

#: Endpoint sectors, BY NAME. The 24-vs-64 pair is exactly a sector mixup
#: waiting to happen: a printed completion coefficient is (cell, sector), not
#: a number. CAP_SECTOR is the two n-gon caps of a prism — for the cube, the
#: opposite-face pair of the retained xy sector. SQUARE_SECTOR is two vertical
#: squares — the triangular-prism program's retained space, whose printed row
#: is 64, not the cap sector's 24.
CAP_SECTOR = (0, 1)
SQUARE_SECTOR = (2, 3)


def catalan_cap_coefficient(sides):
    """The shipped notebook's closed form for the n-gonal-prism cap sector:
    (-1)^(n-1) 2^(n-1) C(2n-2, n-1) / (N (N^2-1)^(n-1))."""
    n = sides
    return (-1) ** (n - 1) * 2 ** (n - 1) * binomial(2 * n - 2, n - 1) / (N * (N**2 - 1) ** (n - 1))


def integer_kernel(cell):
    """Primitive integer kernel vectors of B_2, scaled to coprime integers."""
    from sympy import gcd, lcm

    vecs = []
    for v in cell.boundary_matrix().nullspace():
        denom = lcm([x.q for x in v])
        w = [x * denom for x in v]
        g = gcd(w)
        vecs.append(tuple(x / g for x in w))
    return vecs


# ==========================================================================
# The shared-link channel weights, derived rather than assumed (G24)
# ==========================================================================
# The manuscript's second-order chain rests on one asserted sentence:
# "Isotropy of the normalized shared-link tensor assigns squared norm d_R/N^2
# to the channel projector." Everything in its Section 4 -- A_N, B_N, t_N, the
# flat branch, the whole color/geometry separation -- follows from it, and it
# was the single unproved physical input.
#
# It follows from the order-2 Weingarten values, in two steps.
#
# 1. The six nonshared links collapse. Each plaquette contributes a product of
#    three independent Haar links, and a product of independent Haar matrices
#    is Haar, so the two-plaquette amplitude is Tr(A U) Tr(B U^(+-1)) with A
#    and B independent Haar. Integrating them contributes delta/N each and
#    leaves a pure degree-(2,2) moment of the shared link U.
#
# 2. Two moments settle both families:
#        M_direct = sum_ijkl <|U_ij|^2 |U_kl|^2>                = N^2
#        M_cross  = sum_ijkl <U_ij U_kl conj(U_il) conj(U_kj)>  = N
#    The like family splits as (M_direct +- M_cross)/(2 M_direct), giving
#    (N+1)/(2N) and (N-1)/(2N); the mixed family's singlet component of
#    U_ij conj(U_lk) is delta_il delta_jk / N, of squared norm 1, giving
#    1/N^2 and 1 - 1/N^2. All four are exactly d_R/N^2.


def shared_link_moments(rank: int):
    """``(M_direct, M_cross)`` at integer ``rank``, by explicit index summation.

    No hand algebra: every one of the ``N**4`` index quadruples is summed
    against the order-2 Weingarten delta products,

        <U[r0,c0] U[r1,c1] conj(U[q0,d0]) conj(U[q1,d1])>
            = sum over (sigma, tau) in S_2 x S_2 of Wg(sigma tau^-1)
              * prod_a delta[r_a, q_sigma(a)] delta[c_a, d_tau(a)],

    written out rather than table-driven, because the index bookkeeping is the
    whole content of the claim. The Weingarten pair is evaluated once and the
    sums run in exact ``Fraction`` arithmetic -- substituting into a sympy
    expression inside an ``N**4`` loop costs a minute for no added rigour.
    """
    identity, transposition = weingarten_2()
    same = Fraction(int(identity.subs(N, rank).p), int(identity.subs(N, rank).q))
    diff = Fraction(int(transposition.subs(N, rank).p), int(transposition.subs(N, rank).q))
    span = range(rank)
    direct = cross = Fraction(0)
    for i in span:
        for j in span:
            for k in span:
                for lo in span:
                    rows, rows_conj = (i, k), (i, k)
                    # direct: conj indices (i,j),(k,l) -- columns (j,l)
                    # cross:  conj indices (i,l),(k,j) -- columns (l,j)
                    for cols, cols_conj, bucket in (
                        ((j, lo), (j, lo), "direct"),
                        ((j, lo), (lo, j), "cross"),
                    ):
                        total = Fraction(0)
                        for sigma in ((0, 1), (1, 0)):
                            if any(rows[a] != rows_conj[sigma[a]] for a in (0, 1)):
                                continue
                            for tau in ((0, 1), (1, 0)):
                                if any(cols[a] != cols_conj[tau[a]] for a in (0, 1)):
                                    continue
                                total += same if sigma == tau else diff
                        if bucket == "direct":
                            direct += total
                        else:
                            cross += total
    return direct, cross


def shared_link_weights(rank: int):
    """The four channel weights at integer ``rank``, derived from the moments.

    The like family splits by ``(M_direct +- M_cross)/(2 M_direct)``; the mixed
    family's singlet component of ``U_ij conj(U_lk)`` is ``delta_il delta_jk/N``,
    of squared norm 1 against ``M_direct``.
    """
    direct, cross = shared_link_moments(rank)
    return {
        "1": Fraction(1) / direct,
        "Adj": 1 - Fraction(1) / direct,
        "Lambda2": (direct - cross) / (2 * direct),
        "Sym2": (direct + cross) / (2 * direct),
    }
