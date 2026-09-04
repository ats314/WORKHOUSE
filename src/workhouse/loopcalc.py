"""A from-scratch Wilson-loop calculus for SU(3) strong-coupling perturbation theory.

The third implementation of the fourth-order cluster cumulants (ADR 0024),
independent of the pinned engine in every primitive:

* states are formal products of traces of link matrices ("loop words"),
  canonical under cyclic rotation, never simplified by hand;
* ``H0 = (1/2) sum_links E^2`` acts through the Fierz identity
  ``sum_A T^A_ij T^A_kl = (1/2)(delta_il delta_jk - delta_ij delta_kl / N)``,
  realised as a rewiring of index ports: a U-U or Udag-Udag pair on one link
  swaps its row (column) wires, a U-Udag pair is cut out and its outer wires
  crossed, which is unitarity;
* Haar integrals use the U(N) Weingarten function, computed as the inverse --
  for n > N the pseudoinverse -- of the Gram matrix ``N^cycles`` on ``S_n``;
  a family one determinant away from balance is made balanced by inserting
  ``det U = 1`` as ``(1/N!) eps eps`` on N virtual slots;
* the resolvent ``Q (E0 - H0)^-1`` off the one-plaquette sector is applied by
  per-link irrep projectors (Lagrange polynomials in the single-link ``H0``
  over the SU(3) Casimir table), so every component is an exact ``H0``
  eigenvector with a known energy, and the ``E0`` components dropped can be
  verified to lie in the plaquette span.

Nothing here reads the engine, either kernel, or any run record. The
conventions are the runs' (``plaquette`` traverses i, j, -i, -j from the base;
``V`` multiplies by every face word of the cluster in both orientations with
unit coefficient; ``E0 = 2 C_F``), so its numbers compare with theirs directly.
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction as F
from functools import cache
from itertools import combinations, permutations

# ---------------------------------------------------------------- group data
N = 3
CF = F(N * N - 1, 2 * N)


def set_rank(n: int) -> None:
    """Switch the engine to SU(n). Every cache keyed on the rank is cleared.

    At n = 3 the per-link spectra come from the SU(3) Casimir table; at any
    other rank they are computed from the single-link H0 block's characteristic
    polynomial (`link_spectrum`), which needs no table at all. The two agree at
    n = 3 (tests/test_loopcalc.py)."""
    global N, CF
    N = int(n)
    CF = F(N * N - 1, 2 * N)
    weingarten.cache_clear()
    h0_link.cache_clear()
    integrate.cache_clear()
    link_spectrum.cache_clear()


def casimir2(p: int, q: int) -> F:
    """SU(3) quadratic Casimir of the irrep (p, q), normalised so C2(3) = 4/3."""
    return F(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def _tensor_fund(irreps: set, anti: bool) -> set:
    out = set()
    for p, q in irreps:
        cands = (
            [(p, q + 1), (p + 1, q - 1), (p - 1, q)]
            if anti
            else [(p + 1, q), (p - 1, q + 1), (p, q - 1)]
        )
        out |= {(a, b) for a, b in cands if a >= 0 and b >= 0}
    return out


@cache
def link_energies(a: int, b: int) -> tuple:
    """Distinct single-link energies C2/2 of the function space spanned by a link
    carrying a U's and b Udag's, every reduction (a-k, b-k) included."""
    irreps = set()
    for k in range(min(a, b) + 1):
        s = {(0, 0)}
        for _ in range(a - k):
            s = _tensor_fund(s, False)
        for _ in range(b - k):
            s = _tensor_fund(s, True)
        irreps |= s
    return tuple(sorted({casimir2(p, q) / 2 for p, q in irreps}))


# ---------------------------------------------------------------- Weingarten
def _cycles(perm: tuple) -> int:
    seen, c = set(), 0
    for i in range(len(perm)):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = perm[j]
    return c


def _compose(p: tuple, q: tuple) -> tuple:
    return tuple(p[q[i]] for i in range(len(p)))


def _inverse(p: tuple) -> tuple:
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def _perm_sign(p: tuple) -> int:
    return 1 if (len(p) - _cycles(p)) % 2 == 0 else -1


@cache
def weingarten(n: int) -> dict:
    """Wg(pi), pi in S_n: the pseudoinverse of the Gram matrix G[s,t] = N^cycles(s^-1 t).

    For n <= N the Gram matrix is invertible and Wg is its inverse; for n > N it is
    singular (Collins-Sniady) and Wg is the Moore-Penrose pseudoinverse, which for a
    symmetric matrix with rational eigenvalues is the Lagrange polynomial p(G) with
    p(lam) = 1/lam on the nonzero eigenvalues and p(0) = 0."""
    import flint
    from sympy import Poly, Rational, Symbol, interpolate, roots

    perms = list(permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    m = len(perms)
    gram = flint.fmpq_mat(m, m)
    for i, s in enumerate(perms):
        for j, t in enumerate(perms):
            gram[i, j] = flint.fmpq(N) ** _cycles(_compose(_inverse(s), t))
    cp = gram.charpoly()
    x = Symbol("x")
    coeffs = [Rational(int(cp[k].p), int(cp[k].q)) for k in range(cp.degree(), -1, -1)]
    eig = sorted(set(roots(Poly(coeffs, x), filter="Q")))
    if sum(1 for _ in eig) == 0 or any(e < 0 for e in eig):
        raise ArithmeticError("Gram matrix eigenvalues are not nonnegative rationals")
    pts = [(e, 1 / e) for e in eig if e != 0] + ([(Rational(0), Rational(0))] if 0 in eig else [])
    poly = Poly(interpolate(pts, x), x)
    acc = flint.fmpq_mat(m, m)
    ident = flint.fmpq_mat(m, m)
    for i in range(m):
        ident[i, i] = 1
    for c in poly.all_coeffs():  # highest degree first: Horner
        acc = acc * gram + ident * flint.fmpq(int(c.p), int(c.q))
    e = idx[tuple(range(n))]
    return {p: F(int(acc[e, idx[p]].p), int(acc[e, idx[p]].q)) for p in perms}


# ---------------------------------------------------------------- words
# A word is a tuple of traces; a trace is a tuple of letters (link, orient),
# orient +1 for U and -1 for U-dagger. Canonical: each trace at its minimal
# rotation, traces sorted. The representation is deliberately over-complete
# (Tr(A u u~) and Tr(A) are the same function): every operation below is a
# function-level identity, so a formal vector always represents the right
# function, and only functions are ever integrated.


def _canon_trace(tr: tuple) -> tuple:
    n = len(tr)
    return min(tr[i:] + tr[:i] for i in range(n))


def canon(traces) -> tuple:
    return tuple(sorted(_canon_trace(tuple(t)) for t in traces if t))


def conj(word: tuple) -> tuple:
    """Complex conjugate: every trace reversed with orientations flipped."""
    return canon(tuple((lk, -o) for lk, o in reversed(t)) for t in word)


def product(w1: tuple, w2: tuple) -> tuple:
    return canon(w1 + w2)


def slots(word: tuple):
    """Letters by slot id, and the successor map (out-port of s feeds in-port of succ[s])."""
    letters, succ, sid = [], {}, 0
    for t in word:
        first = sid
        for lk, o in t:
            letters.append((lk, o))
            succ[sid] = sid + 1
            sid += 1
        succ[sid - 1] = first
    return letters, succ


def rewire(word: tuple, through: dict, virt: tuple = (), vsucc: dict | None = None) -> tuple:
    """Apply a port rewiring and read the traces back.

    ``through`` maps an in-port (slot id) to ``(out-port slot id, letter or None)``;
    unlisted slots keep their own letter. Virtual slots ``virt`` carry no letter and
    the wire leaving a virtual out-port goes to ``vsucc``. Returns
    ``(closed empty loops, canonical word)``; each closed loop is worth N."""
    letters, succ = slots(word)
    n = len(letters)
    thr = {s: (s, letters[s]) for s in range(n)}
    thr.update(through)
    if vsucc:
        succ.update(vsucc)
    seen, traces, closed = set(), [], 0
    for start in list(range(n)) + list(virt):
        if start in seen:
            continue
        cur, tr = start, []
        while cur not in seen:
            seen.add(cur)
            out, letter = thr[cur]
            if letter is not None:
                tr.append(letter)
            cur = succ[out]
        if tr:
            traces.append(tuple(tr))
        else:
            closed += 1
    return closed, canon(traces)


def _crossing(s: int, t: int, keep: bool, letter_s=None, letter_t=None) -> dict:
    """Through-edges s.in -> t.out and t.in -> s.out: a swap (letters kept) or a cut."""
    if keep:
        return {s: (t, letter_t), t: (s, letter_s)}
    return {s: (t, None), t: (s, None)}


# ---------------------------------------------------------------- vectors
def vadd(a: dict, b: dict, s=F(1)) -> dict:
    out = defaultdict(F, a)
    for k, v in b.items():
        out[k] += s * v
    return {k: v for k, v in out.items() if v}


def vscale(a: dict, s) -> dict:
    return {k: v * s for k, v in a.items()} if s else {}


def multiply(vec: dict, word: tuple) -> dict:
    out = defaultdict(F)
    for w, c in vec.items():
        out[product(w, word)] += c
    return dict(out)


def content(word: tuple) -> dict:
    """link -> [#U, #Udag]."""
    cnt = defaultdict(lambda: [0, 0])
    for t in word:
        for lk, o in t:
            cnt[lk][0 if o > 0 else 1] += 1
    return cnt


def links_of(vec: dict) -> set:
    return {lk for w in vec for t in w for lk, _o in t}


# ---------------------------------------------------------------- H0
@cache
def h0_link(word: tuple, link: int) -> tuple:
    """The single-link part (1/2) E_link^2 of H0 on a word, as ((word, coeff), ...).

    E acts on a U slot by left multiplication with T^A and on a Udag slot by
    right multiplication with -T^A. Summing (E^A)^2 over A: each slot contributes
    C_F/2; each like pair (U-U or Udag-Udag) contributes (1/2)(swap of its row or
    column wires) - 1/(2N); each unlike pair contributes -(1/2)(cut and cross) +
    1/(2N), the cut being delta_il delta_jk = the unitarity contraction."""
    letters, _ = slots(word)
    ids = [s for s, (lk, _o) in enumerate(letters) if lk == link]
    out = defaultdict(F)
    out[word] += CF * len(ids) / 2
    for s, t in combinations(ids, 2):
        if letters[s][1] == letters[t][1]:
            closed, w = rewire(word, _crossing(s, t, True, letters[s], letters[t]))
            out[w] += F(1, 2) * F(N) ** closed
            out[word] -= F(1, 2 * N)
        else:
            closed, w = rewire(word, _crossing(s, t, False))
            out[w] -= F(1, 2) * F(N) ** closed
            out[word] += F(1, 2 * N)
    return tuple((w, c) for w, c in out.items() if c)


def apply_h0_link(vec: dict, link: int) -> dict:
    out = defaultdict(F)
    for w, c in vec.items():
        for w2, c2 in h0_link(w, link):
            out[w2] += c * c2
    return {k: v for k, v in out.items() if v}


def apply_h0(vec: dict) -> dict:
    out = {}
    for lk in links_of(vec):
        out = vadd(out, apply_h0_link(vec, lk))
    return out


@cache
def link_spectrum(word: tuple, link: int) -> tuple:
    """The rational spectrum of the single-link H0 on the closure of `word` under it.

    Rank-generic: the block is built by breadth-first closure under `h0_link`,
    its characteristic polynomial taken exactly (flint), and the rational roots
    kept. Over-complete formal words can add spurious roots; a superset of the
    true spectrum is harmless to the Lagrange projectors."""
    from collections import deque as _deque

    import flint
    from sympy import Poly, Rational, Symbol, roots

    words, seen, queue, act = [], {word}, _deque([word]), {}
    while queue:
        w = queue.popleft()
        words.append(w)
        act[w] = h0_link(w, link)
        for w2, _c in act[w]:
            if w2 not in seen:
                seen.add(w2)
                queue.append(w2)
    idx = {w: i for i, w in enumerate(words)}
    n = len(words)
    mat = flint.fmpq_mat(n, n)
    for j, w in enumerate(words):
        for w2, c in act[w]:
            mat[idx[w2], j] += flint.fmpq(c.numerator, c.denominator)
    cp = mat.charpoly()
    x = Symbol("x")
    coeffs = [Rational(int(cp[k].p), int(cp[k].q)) for k in range(cp.degree(), -1, -1)]
    return tuple(sorted({F(int(r.p), int(r.q)) for r in roots(Poly(coeffs, x), filter="Q")}))


def _project_link(vec: dict, link: int):
    """Split vec into single-link H0 eigencomponents on `link`: yields (energy, component)."""
    groups = defaultdict(dict)
    for w, c in vec.items():
        a, b = content(w).get(link, [0, 0])
        groups[(a, b)][w] = c
    for (a, b), sub in groups.items():
        if N == 3:
            energies = link_energies(a, b)
        else:
            energies = sorted(set().union(*(link_spectrum(w, link) for w in sub)))
        for e in energies:
            comp = dict(sub)
            for e2 in energies:
                if e2 != e:
                    comp = vscale(vadd(apply_h0_link(comp, link), comp, -e2), 1 / (e - e2))
            if comp:
                yield e, comp


def eigen_components(vec: dict):
    """Decompose vec into exact H0 eigencomponents: yields (total energy, component)."""
    lks = sorted(links_of(vec))

    def rec(v: dict, i: int, acc: F):
        if not v:
            return
        if i == len(lks):
            yield acc, v
            return
        for e, comp in _project_link(v, lks[i]):
            yield from rec(comp, i + 1, acc + e)

    yield from rec(vec, 0, F(0))


def resolvent(vec: dict, e0: F, power: int = 1) -> dict:
    """Q (e0 - H0)^-power vec, Q the projector off the e0 eigenspace."""
    out = {}
    for e, comp in eigen_components(vec):
        if e != e0:
            out = vadd(out, comp, 1 / (e0 - e) ** power)
    return out


def is_eigenvector(vec: dict, e: F) -> bool:
    return vadd(apply_h0(vec), vec, -e) == {}


# ---------------------------------------------------------------- Haar
def haar_link(word: tuple, link: int) -> dict:
    """Integrate one link of a formal word over SU(N) Haar measure.

    Balanced families (n, n) use the U(N) Weingarten function; U(N) and SU(N)
    agree on them. A family (n+N, n) or (n, n+N) is balanced by multiplying
    the integrand by det(U-dagger) = 1 or det(U) = 1, written as (1/N!) eps eps
    on N virtual slots; after the Weingarten deltas the two epsilons contract,
    eps(out-ports) eps(in-ports) = sum_pi sgn(pi) prod delta. Families further
    from balance are refused; families with charge not 0 mod N are zero."""
    letters, _ = slots(word)
    us = [s for s, (lk, o) in enumerate(letters) if lk == link and o > 0]
    ds = [s for s, (lk, o) in enumerate(letters) if lk == link and o < 0]
    diff = len(us) - len(ds)
    if diff % N != 0:
        return {}
    if abs(diff) > N:
        raise NotImplementedError(f"family ({len(us)},{len(ds)}) on link {link}")
    if not us and not ds:
        return {word: F(1)}
    virt = tuple(range(len(letters), len(letters) + abs(diff)))
    if diff > 0:
        ds = ds + list(virt)
    elif diff < 0:
        us = us + list(virt)
    n = len(us)
    wg = weingarten(n)
    perms_n = list(permutations(range(n)))
    eps_perms = list(permutations(range(abs(diff)))) if diff else [()]
    norm = F(1, math.factorial(abs(diff)))
    out = defaultdict(F)
    for sigma in perms_n:
        for tau in perms_n:
            coeff = wg[_compose(sigma, _inverse(tau))]
            through = {}
            for m in range(n):
                through[us[m]] = (ds[sigma[m]], None)  # delta(row of U_m, row of U*_sigma(m))
                through[ds[tau[m]]] = (us[m], None)  # delta(col of U_m, col of U*_tau(m))
            for pi in eps_perms:
                vsucc = {virt[p]: virt[pi[p]] for p in range(abs(diff))}
                sign = _perm_sign(pi) if diff else 1
                closed, w = rewire(word, through, virt, vsucc)
                out[w] += coeff * norm * sign * F(N) ** closed
    return {k: v for k, v in out.items() if v}


@cache
def integrate(word: tuple) -> F:
    """The full Haar integral of a formal word, link by link."""
    vec = {word: F(1)}
    while True:
        lks = links_of(vec)
        if not lks:
            return sum(vec.values(), F(0))
        lk = min(lks)
        out = defaultdict(F)
        for w, c in vec.items():
            for w2, c2 in haar_link(w, lk).items():
                out[w2] += c * c2
        vec = {k: v for k, v in out.items() if v}


def inner(bra: tuple, vec: dict) -> F:
    """<bra|vec> = int conj(bra) vec. Zero unless every link's charge is 0 mod N."""
    bc = conj(bra)
    tot = F(0)
    for w, c in vec.items():
        cnt = defaultdict(int)
        for t in bc + w:
            for lk, o in t:
                cnt[lk] += o
        if any(v % N for v in cnt.values()):
            continue
        tot += c * integrate(product(bc, w))
    return tot


# ---------------------------------------------------------------- geometry
LINKS: dict = {}
PLANES = ((0, 1), (0, 2), (1, 2))


def link(site, d) -> int:
    key = (tuple(site), d)
    if key not in LINKS:
        LINKS[key] = len(LINKS)
    return LINKS[key]


def _add(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def _e(j):
    v = [0, 0, 0]
    v[j] = 1
    return tuple(v)


def plaquette(plane, base, conjugate: bool = False) -> tuple:
    """The plaquette word: i-link at base, j-link at base + e_i, then back.

    The runs' traversal, so plane (0, 2) is x-then-z, the kernel's own basis,
    and (2, 0) is its conjugate."""
    i, j = plane
    steps = [
        (link(base, i), 1),
        (link(_add(base, _e(i)), j), 1),
        (link(_add(base, _e(j)), i), -1),
        (link(base, j), -1),
    ]
    if conjugate:
        steps = [(lk, -o) for lk, o in reversed(steps)]
    return canon([tuple(steps)])


def plaquette_links(plane, base) -> frozenset:
    return frozenset(lk for lk, _o in plaquette(plane, base)[0])


def plaquettes_sharing_a_link(faces) -> list:
    """Every plaquette (in the sorted-plane basis) sharing a link with one of
    `faces`, excluding the faces themselves; an independent census of the
    runs' `neighbours`."""
    seen = {plaquette_links(pl, b) for pl, b in faces}
    inv = {v: k for k, v in LINKS.items()}
    out = []
    for pl, b in faces:
        for lk in sorted(plaquette_links(pl, b)):
            site, d = inv[lk]
            for e in range(3):
                if e == d:
                    continue
                plane = (min(d, e), max(d, e))
                for base in (
                    tuple(site),
                    tuple(s - (1 if k == e else 0) for k, s in enumerate(site)),
                ):
                    ls = plaquette_links(plane, base)
                    if ls not in seen:
                        seen.add(ls)
                        out.append((plane, base))
    return out


# ---------------------------------------------------------------- clusters
class Cluster:
    """A set of faces, each in both orientations: words 2k (face k) and 2k+1 (its conjugate)."""

    def __init__(self, faces):
        self.faces = list(faces)
        self.words = []
        for pl, b in self.faces:
            self.words.append(plaquette(pl, b))
            self.words.append(plaquette(pl, b, True))
        self.e0 = 4 * CF / 2

    def V(self, vec: dict) -> dict:
        out = {}
        for w in self.words:
            out = vadd(out, multiply(vec, w))
        return out

    def R(self, vec: dict, power: int = 1) -> dict:
        return resolvent(vec, self.e0, power)

    def second_order(self):
        """H2 = P V R V P and V2 = P V R^2 V P on the model space, as matrices."""
        m = len(self.words)
        vd = [self.V({w: F(1)}) for w in self.words]
        r1 = [self.R(v) for v in vd]
        r2 = [self.R(v, 2) for v in vd]
        h2 = [[inner(self.words[i], self.V(r1[j])) for j in range(m)] for i in range(m)]
        v2 = [[inner(self.words[i], self.V(r2[j])) for j in range(m)] for i in range(m)]
        return h2, v2


def codd(m, i, j):
    a, b = 2 * i, 2 * j
    return (m[a][b] - m[a][b + 1] - m[a + 1][b] + m[a + 1][b + 1]) / 2


def ceven(m, i, j):
    a, b = 2 * i, 2 * j
    return (m[a][b] + m[a][b + 1] + m[a + 1][b] + m[a + 1][b + 1]) / 2


# ---------------------------------------------------------------- fourth order
def _split_V(cl: Cluster, by_flag: dict, x_words: set) -> dict:
    """Apply V to a flagged vector {touched: vec}; inserting an X word sets the flag."""
    out = {False: {}, True: {}}
    for flag, vec in by_flag.items():
        if not vec:
            continue
        for w in cl.words:
            f = flag or (w in x_words)
            out[f] = vadd(out[f], multiply(vec, w))
    return out


def _R_flagged(cl: Cluster, by_flag: dict) -> dict:
    return {f: cl.R(v) if v else {} for f, v in by_flag.items()}


def cumulant(faces3, x_index: int) -> dict:
    """The three-cluster cumulant W(faces3) - W(faces3 minus X) between the two
    non-X faces, at fourth order, in the Hermitian PVP = 0 form

        H4 = P V R V R V R V P - (1/2) {P V R V P, P V R^2 V P}.

    The direct term keeps only X-touched histories, the X-free ones being
    identical in both clusters; the fold term is the full difference. On the
    off-diagonal block the A-terms of the PVP != 0 assembly carry no X and
    cancel, and no epsilon family occurs (charge counting; both facts the
    runs also rely on). Returns W[(a, b)] for a in the end-face words (0, 1)
    and b in the other end's (2, 3), indexed as in the two-cluster."""
    cl3 = Cluster(faces3)
    ends = [f for k, f in enumerate(faces3) if k != x_index]
    cl2 = Cluster(ends)
    x_words = {cl3.words[2 * x_index], cl3.words[2 * x_index + 1]}
    end_ids3 = [k for k in range(6) if k // 2 != x_index]
    ket = {}
    for a in (0, 1):
        v = {False: {cl2.words[a]: F(1)}, True: {}}
        v = _R_flagged(cl3, _split_V(cl3, v, x_words))
        ket[a] = _R_flagged(cl3, _split_V(cl3, v, x_words))
    bra = {}
    for b in (2, 3):
        v = {False: {cl2.words[b]: F(1)}, True: {}}
        v = _R_flagged(cl3, _split_V(cl3, v, x_words))
        bra[b] = _split_V(cl3, v, x_words)
    direct = {}
    for a in (0, 1):
        for b in (2, 3):
            tot = F(0)
            for fb, bv in bra[b].items():
                for fa, kv in ket[a].items():
                    if fa or fb:
                        for w, c in bv.items():
                            tot += c * inner(w, kv)
            direct[(a, b)] = tot
    h2_3, v2_3 = cl3.second_order()
    h2_2, v2_2 = cl2.second_order()

    def fold(h2, v2, ids, a, b):
        return (
            sum(
                h2[ids[b]][k] * v2[k][ids[a]] + v2[ids[b]][k] * h2[k][ids[a]]
                for k in range(len(h2))
            )
            / 2
        )

    return {
        (a, b): direct[(a, b)]
        - (fold(h2_3, v2_3, end_ids3, a, b) - fold(h2_2, v2_2, list(range(4)), a, b))
        for a in (0, 1)
        for b in (2, 3)
    }


def block_odd(w: dict) -> F:
    return (w[(0, 2)] - w[(0, 3)] - w[(1, 2)] + w[(1, 3)]) / 2


def block_even(w: dict) -> F:
    return (w[(0, 2)] + w[(0, 3)] + w[(1, 2)] + w[(1, 3)]) / 2


def cube_completion(p, q, others) -> dict:
    """The direct fourth-order term between faces p and q through the four `others`
    inserted once each: W[(a, b)] for a in p's words (0, 1), b in q's (2, 3)."""
    cl = Cluster([p, q] + list(others))
    side = {cl.words[k]: k // 2 for k in range(4, len(cl.words))}

    def v_sides(vec):
        out = defaultdict(F)
        for (w, used), c in vec.items():
            for sw, f in side.items():
                if f not in used:
                    for w2, c2 in multiply({w: c}, sw).items():
                        out[(w2, used | {f})] += c2
        return {k: v for k, v in out.items() if v}

    def r(vec):
        by = defaultdict(dict)
        for (w, used), c in vec.items():
            by[used][w] = c
        out = {}
        for used, sub in by.items():
            for w, c in cl.R(sub).items():
                out[(w, used)] = c
        return out

    result = {}
    for a in (0, 1):
        v = {(cl.words[a], frozenset()): F(1)}
        for _ in range(3):
            v = r(v_sides(v))
        v = v_sides(v)
        final = defaultdict(F)
        for (w, _used), c in v.items():
            final[w] += c
        for b in (2, 3):
            result[(a, b)] = inner(cl.words[b], dict(final))
    return result
