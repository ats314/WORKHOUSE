"""The third engine over Q(N): the fourth-order cumulants as rational functions of N, derived.

``workhouse.loopcalc`` computes a cumulant at one integer rank with exact
rationals. Nothing in it but the rank predicates (``charge = 0 mod N``,
``|diff| <= N``), the Weingarten function and the single-link spectra depends
on N in any way other than through rational arithmetic in the constants
``C_F = (N^2-1)/(2N)``, ``1/(2N)`` and ``N^closed``. This module runs the same
code with those constants replaced by elements of the field Q(N) (``RF``, a
numerator and a monic denominator in ``flint.fmpq_poly``), the Weingarten
function replaced by the symbolic inverse of the Gram matrix ``N^cycles`` on
S_n, and the single-link spectra replaced by the SU(N) quadratic Casimirs of
the irreps a link's flux content can carry. Every cumulant then comes out as
ONE rational function of N, computed rather than reconstructed.

Why the result is the value the per-rank engine returns at every N >= 5, and
what the run certifies to make that a theorem about the engine rather than a
plausibility:

1. *The words are the same.* Word arithmetic (products, canonical forms,
   rewiring) never looks at N. The only rank-dependent branching is the
   charge filter of ``inner`` and the family test of ``haar_link``. For
   N >= 5 a word passes the integer engine's filter iff every link's net flux
   is 0 mod N; the symbolic engine passes it iff every net flux is 0. These
   agree when no word has all its nonzero fluxes of magnitude >= 5, which the
   context manager asserts on every word ``inner`` sees (``max_charge`` and
   the audit in ``_inner_audited``). Consequently every Haar family met is
   balanced, and the largest one, ``max_weingarten_n``, is recorded.
2. *The Weingarten function is the same.* For a balanced family (n, n) with
   n <= N the Gram matrix is invertible and the integer engine's pseudoinverse
   is its inverse, which is the specialisation of the symbolic inverse.
3. *The resolvent is the same.* ``Q (E0 - H0)^-1`` on a finite word block is
   one rational function of N wherever E0 - H0 is invertible off the E0
   eigenspace; both engines compute it from a spectral decomposition, and a
   spectral decomposition is unique. The symbolic decomposition is certified
   component by component: each component is checked to be an exact
   eigenvector of every single-link H0 (``components_verified``) and the
   components are checked to sum to the vector. The energies it meets are
   recorded so the run can check that no resolvent denominator ``E0 - E``
   vanishes at an integer rank >= 4 (``resolvent_denominators``).

Nothing here is a statement about physics. It is a statement about a
program: the function of N the engine computes is this rational function.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations

import flint

from . import loopcalc as L

_ZERO = flint.fmpq_poly([0])
_ONE = flint.fmpq_poly([1])
_X = flint.fmpq_poly([0, 1])


def _poly(x) -> flint.fmpq_poly:
    if isinstance(x, flint.fmpq_poly):
        return x
    if isinstance(x, Fraction):
        return flint.fmpq_poly([flint.fmpq(x.numerator, x.denominator)])
    if isinstance(x, (int, flint.fmpq)):
        return flint.fmpq_poly([x])
    raise TypeError(f"not a scalar for Q(N): {type(x).__name__}")


class RF:
    """An element of Q(N): ``num/den`` with ``den`` monic and the gcd removed.

    Supports the arithmetic ``loopcalc`` performs on its scalars, mixed with
    ``int`` and ``Fraction`` (the engine's own literals), hashing and a total
    order by coefficients (the engine sorts energy sets)."""

    __slots__ = ("num", "den", "_h")

    def __init__(self, num=0, den=None):
        if isinstance(num, RF):
            n, d = num.num, num.den
        else:
            n, d = _poly(num), _ONE
        if den is not None:
            if isinstance(den, RF):
                n, d = n * den.den, d * den.num
            else:
                d = d * _poly(den)
        self._set(n, d)

    @classmethod
    def _make(cls, n, d):
        obj = object.__new__(cls)
        obj._set(n, d)
        return obj

    def _set(self, n, d):
        if d == 0:
            raise ZeroDivisionError("rational function with zero denominator")
        if n == 0:
            self.num, self.den, self._h = _ZERO, _ONE, None
            return
        g = n.gcd(d)
        if g.degree() > 0:
            n = n // g
            d = d // g
        lc = d.coeffs()[-1]
        if lc != 1:
            n = n / lc
            d = d / lc
        self.num, self.den, self._h = n, d, None

    @staticmethod
    def _co(x):
        if isinstance(x, RF):
            return x
        if isinstance(x, (int, Fraction, flint.fmpq)):
            return RF(x)
        return NotImplemented

    def __add__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return o
        if self.den == o.den:
            return RF._make(self.num + o.num, self.den)
        return RF._make(self.num * o.den + o.num * self.den, self.den * o.den)

    __radd__ = __add__

    def __neg__(self):
        return RF._make(-self.num, self.den)

    def __sub__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return o
        if self.den == o.den:
            return RF._make(self.num - o.num, self.den)
        return RF._make(self.num * o.den - o.num * self.den, self.den * o.den)

    def __rsub__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return o
        return o.__sub__(self)

    def __mul__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return o
        return RF._make(self.num * o.num, self.den * o.den)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return o
        return RF._make(self.num * o.den, self.den * o.num)

    def __rtruediv__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return o
        return o.__truediv__(self)

    def __pow__(self, k: int):
        if k < 0:
            return RF._make(self.den ** (-k), self.num ** (-k))
        return RF._make(self.num**k, self.den**k)

    def __bool__(self):
        return self.num != 0

    def __eq__(self, o):
        o = RF._co(o)
        if o is NotImplemented:
            return False
        return self.num == o.num and self.den == o.den

    def __ne__(self, o):
        return not self.__eq__(o)

    def _key(self):
        return (
            tuple((int(c.p), int(c.q)) for c in self.num.coeffs()),
            tuple((int(c.p), int(c.q)) for c in self.den.coeffs()),
        )

    def __hash__(self):
        if self._h is None:
            self._h = hash(self._key())
        return self._h

    def __lt__(self, o):
        return self._key() < RF._co(o)._key()

    def __gt__(self, o):
        return self._key() > RF._co(o)._key()

    def __repr__(self):
        return f"RF({self.num}, {self.den})"

    def degrees(self) -> tuple[int, int]:
        return (self.num.degree(), self.den.degree())

    def at(self, n) -> Fraction:
        """Specialise at rank ``n`` (an int or Fraction)."""
        n = Fraction(n)
        nq = flint.fmpq(n.numerator, n.denominator)
        d = self.den(nq)
        if d == 0:
            raise ZeroDivisionError(f"pole at N = {n}")
        v = self.num(nq) / d
        return Fraction(int(v.p), int(v.q))

    def to_sympy(self):
        from sympy import Rational, Symbol

        n = Symbol("N")
        num = sum(Rational(int(c.p), int(c.q)) * n**i for i, c in enumerate(self.num.coeffs()))
        den = sum(Rational(int(c.p), int(c.q)) * n**i for i, c in enumerate(self.den.coeffs()))
        return num / den

    def coefficient_lists(self) -> dict:
        """Integer-cleared numerator and denominator coefficient lists, constant term first."""
        nq = self.num.coeffs() or [flint.fmpq(0)]
        dq = self.den.coeffs()
        from math import lcm

        m = 1
        for c in nq + dq:
            m = lcm(m, int(c.q))
        return {
            "num": [int(c.p) * (m // int(c.q)) for c in nq],
            "den": [int(c.p) * (m // int(c.q)) for c in dq],
        }


#: The indeterminate N.
N_SYM = RF(_X)
#: C_F(N) = (N^2 - 1)/(2N), and a fundamental link's energy C_F/2.
CF_SYM = (N_SYM * N_SYM - 1) / (2 * N_SYM)
E_FUND = CF_SYM / 2


def rational_roots(p: flint.fmpq_poly) -> list[Fraction]:
    """Every rational root of ``p``, from its factorisation over Q."""
    out = []
    _c, factors = p.factor()
    for f, _mult in factors:
        if f.degree() == 1:
            b, a = f.coeffs()
            r = -b / a
            out.append(Fraction(int(r.p), int(r.q)))
    return sorted(out)


# ---------------------------------------------------------------- Weingarten over Q(N)
_WG: dict[int, dict] = {}


def weingarten_symbolic(n: int) -> dict:
    """Wg(pi; N) for pi in S_n: the inverse of the Gram matrix ``N^cycles(s^-1 t)`` over Q(N).

    Valid wherever the Gram matrix is invertible, i.e. for every integer N >= n
    (Collins-Sniady); the per-rank engine's Moore-Penrose pseudoinverse is the
    inverse there, so this is its specialisation."""
    if n in _WG:
        return _WG[n]
    perms = list(permutations(range(n)))
    m = len(perms)
    gram = [[N_SYM ** L._cycles(L._compose(L._inverse(s), t)) for t in perms] for s in perms]
    aug = [row[:] + [RF(1 if i == j else 0) for j in range(m)] for i, row in enumerate(gram)]
    for c in range(m):
        piv = next(r for r in range(c, m) if aug[r][c])
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]
        aug[c] = [v / pv for v in aug[c]]
        for r in range(m):
            if r != c and aug[r][c]:
                f = aug[r][c]
                aug[r] = [v - f * w for v, w in zip(aug[r], aug[c], strict=True)]
    e = perms.index(tuple(range(n)))
    _WG[n] = {p: aug[e][m + i] for i, p in enumerate(perms)}
    return _WG[n]


# ---------------------------------------------------------------- spectra over Q(N)
def partitions(k: int, maxpart: int | None = None):
    if k == 0:
        yield ()
        return
    if maxpart is None or maxpart > k:
        maxpart = k
    for first in range(maxpart, 0, -1):
        for rest in partitions(k - first, first):
            yield (first,) + rest


def _content_sum(lam) -> int:
    """sum_i lam_i (lam_i - 2i + 1), rows indexed from 1: twice the sum of the contents."""
    return sum(part * (part - 2 * (i + 1) + 1) for i, part in enumerate(lam))


def casimir_symbolic(lam, mu) -> RF:
    """The quadratic Casimir of the SU(N) irrep with highest weight (lam; mu-bar),
    normalised so that C2(F) = (N^2-1)/(2N):
    ``(1/2)[(|lam|+|mu|) N + s(lam) + s(mu) - (|lam|-|mu|)^2 / N]``.
    Rank-generic for N at least the number of rows of lam plus those of mu."""
    a, b = sum(lam), sum(mu)
    return ((a + b) * N_SYM + _content_sum(lam) + _content_sum(mu) - RF((a - b) ** 2, N_SYM)) / 2


def irrep_name(lam, mu) -> str:
    """A rank-independent name; conjugate irreps (lam; mu) and (mu; lam) share it."""
    first, second = sorted((tuple(lam), tuple(mu)), reverse=True)
    special = {
        ((), ()): "1",
        ((1,), ()): "F",
        ((1,), (1,)): "adj",
        ((2,), ()): "sym",
        ((1, 1), ()): "lam",
    }
    if (first, second) in special:
        return special[(first, second)]
    return "".join(map(str, first)) + "|" + "".join(map(str, second))


def _energy_table(max_boxes: int = 6) -> dict:
    """energy (C2/2) -> irrep name, for every (lam; mu) with at most ``max_boxes`` boxes."""
    table: dict[RF, str] = {}
    for total in range(max_boxes + 1):
        for a in range(total + 1):
            for lam in partitions(a):
                for mu in partitions(total - a):
                    e = casimir_symbolic(lam, mu) / 2
                    name = irrep_name(lam, mu)
                    if e in table and name not in table[e].split("/"):
                        # a genuine Casimir coincidence, e.g. (4,1,1) and (3,3) at six
                        # boxes; no intermediate state of a fourth-order history
                        # carries more than four boxes on a link, so it never labels
                        table[e] = table[e] + "/" + name
                    else:
                        table[e] = name
    return table


ENERGY_NAME = _energy_table()


def link_spectrum_symbolic(word, link) -> tuple:
    """Every energy a link with the word's flux content (a, b) can carry: the
    Casimirs of the irreps of F^a x Fbar^b including every reduction (a-k, b-k).
    A superset of the true spectrum on the block is harmless to the Lagrange
    projectors, and each component is verified afterwards anyway."""
    a, b = L.content(word).get(link, [0, 0])
    weight = L.link_weight(link)
    out = set()
    for k in range(min(a, b) + 1):
        for lam in partitions(a - k):
            for mu in partitions(b - k):
                out.add(weight * casimir_symbolic(lam, mu) / 2)
    return tuple(sorted(out))


# ---------------------------------------------------------------- the verified decomposition
def labelled_components(vec: dict):
    """Exact H0 eigencomponents of ``vec`` with their per-link energies, each verified.

    Yields ``(total energy, {link: energy}, component)``. Every component is
    checked to be an eigenvector of the single-link H0 on every link it
    touches, so it is a simultaneous eigenvector whatever the projectors did;
    the per-link energies sum to the total."""
    links = sorted(L.links_of(vec))

    def rec(v: dict, i: int, acc):
        if not v:
            return
        if i == len(links):
            yield acc, v
            return
        for e, comp in L._project_link(v, links[i]):
            yield from rec(comp, i + 1, acc + e)

    for e, comp in rec(vec, 0, RF(0)):
        per_link = {}
        w0 = next(iter(comp))
        for lk in sorted(L.links_of(comp)):
            h = L.apply_h0_link(comp, lk)
            e_lk = h.get(w0, RF(0)) / comp[w0]
            if L.vscale(comp, e_lk) != h:
                raise AssertionError(f"component is not an eigenvector of H0 on link {lk}")
            per_link[lk] = e_lk
        if sum(per_link.values(), RF(0)) != e:
            raise AssertionError("per-link energies do not sum to the total")
        yield e, per_link, comp


def state_label(per_link: dict) -> tuple:
    """(extra fundamental links beyond the plaquette's four, sorted irrep names of the
    links carrying anything else) -- the rank-independent channel label of ADR 0026,
    read off the per-link energies rather than searched for."""
    extra, names = -4, []
    for lk, e in per_link.items():
        if not e:
            continue
        weight = L.link_weight(lk)
        unit = e / weight
        if unit == E_FUND:
            extra += weight
        else:
            names.extend([ENERGY_NAME[unit]] * weight)
    return (extra, tuple(sorted(names)))


class Symbolic:
    """Run ``loopcalc`` over Q(N). A context manager; ``stats`` is the certificate.

    with Symbolic() as S:
        w = L.cumulant(faces, 1)          # every entry an RF
    S.stats  # components verified, largest Weingarten family, energies met

    ``max_weingarten_n`` and ``max_charge`` count the Haar integrals actually
    performed: ``loopcalc._integrate`` caches per word, so a warm cache from an
    earlier symbolic run in the same process under-reports them. The run
    records are produced in fresh processes.
    """

    def __init__(self):
        self.stats = {
            "components_verified": 0,
            "max_weingarten_n": 0,
            "max_charge": 0,
            "energies": set(),
            "link_energies": set(),
            "labels_by_energy": defaultdict(set),
        }

    def __enter__(self):
        self._saved = {
            k: getattr(L, k)
            for k in (
                "F",
                "N",
                "CF",
                "weingarten",
                "link_spectrum",
                "eigen_components",
                "_charge_zero",
                "_family_supported",
                "inner",
            )
        }
        st = self.stats
        L.F = RF
        L.N = N_SYM
        L.CF = CF_SYM
        L.link_spectrum = link_spectrum_symbolic
        L._charge_zero = lambda charge: charge == 0

        def unsupported(diff):
            if diff == 0:
                return True
            raise AssertionError(f"an unbalanced family (diff {diff}) reached the Haar integral")

        L._family_supported = unsupported

        def weingarten(n):
            st["max_weingarten_n"] = max(st["max_weingarten_n"], n)
            return weingarten_symbolic(n)

        L.weingarten = weingarten

        def eigen_components(vec):
            total: dict = {}
            for e, per_link, comp in labelled_components(vec):
                st["components_verified"] += 1
                st["energies"].add(e)
                st["link_energies"].update(per_link.values())
                st["labels_by_energy"][e].add(state_label(per_link))
                total = L.vadd(total, comp)
                yield e, comp
            if total != vec:
                raise AssertionError("the components do not sum to the vector")

        L.eigen_components = eigen_components
        original_inner = self._saved["inner"]

        def inner(bra, vec):
            # The audit behind premise 1 of the module docstring: a word whose
            # nonzero fluxes are all of magnitude >= 5 would pass the integer
            # engine's filter at N = 5 and fail this one; none may occur.
            bc = L.conj(bra)
            for w in vec:
                cnt: dict = defaultdict(int)
                for t in bc + w:
                    for lk, o in t:
                        cnt[lk] += o
                nonzero = [abs(v) for v in cnt.values() if v]
                if nonzero:
                    st["max_charge"] = max(st["max_charge"], max(nonzero))
                    if min(nonzero) >= 5:
                        raise AssertionError(f"a word with every nonzero flux >= 5: {nonzero}")
            return original_inner(bra, vec)

        L.inner = inner
        return self

    def __exit__(self, *exc):
        for k, v in self._saved.items():
            setattr(L, k, v)
        return False

    def resolvent_denominators(self, e0=None) -> dict:
        """The distinct ``E0 - E`` met, each with its rational roots, and the integer
        roots >= 4 among them (which must be none for the specialisation argument)."""
        e0 = 2 * CF_SYM if e0 is None else e0
        out = {}
        bad = {}
        for e in sorted(self.stats["energies"]):
            if e == e0:
                continue
            d = e0 - e
            roots = rational_roots(d.num)
            labels = sorted(label_text(("state", lab)) for lab in self.stats["labels_by_energy"][e])
            out[str(d.to_sympy())] = {"roots": [str(r) for r in roots], "states": labels}
            for r in roots:
                if r.denominator == 1 and r >= 4:
                    bad.setdefault(str(r), []).extend(labels)
        return {"denominators": out, "integer_roots_at_least_4": bad}


# ---------------------------------------------------------------- channels over Q(N)
def _apply_V_flagged(cl, vec, flag, x_words):
    out = {False: {}, True: {}}
    for w in cl.words:
        f = flag or (w in x_words)
        out[f] = L.vadd(out[f], L.multiply(vec, w))
    return out


def _resolvent_labelled(vec, e0):
    """Q (e0 - H0)^-1 vec split by channel label."""
    out: dict = defaultdict(dict)
    for e, per_link, comp in labelled_components(vec):
        if e != e0:
            lab = state_label(per_link)
            out[lab] = L.vadd(out[lab], comp, 1 / (e0 - e))
    return out


def channels(faces3, x_index: int, reduced: bool = False) -> dict:
    """The three-cluster cumulant of ``loopcalc.cumulant`` split by channel, over Q(N).

    Returns ``{key: {(a, b): RF}}`` with ``key = ("direct", l1, l2, l3)`` for the
    direct term tagged by the labels of its three intermediate states and
    ``("fold3", l, l')`` / ``("fold2", l, l')`` for the fold terms tagged by the
    labels of the H2 and V2 intermediates; the entries sum to the cumulant's.
    Labels are ``state_label`` values, read off each component's per-link
    energies, so the same channel means the same thing on every cluster."""
    cl3 = L.Cluster(faces3, reduced)
    ends = [f for k, f in enumerate(faces3) if k != x_index]
    cl2 = L.Cluster(ends, reduced)
    x_words = {cl3.words[2 * x_index], cl3.words[2 * x_index + 1]}
    end_ids3 = [k for k in range(6) if k // 2 != x_index]
    e0 = cl3.e0
    kets = {}
    for a in (0, 1):
        stage: dict = {}
        for f1, vec1 in _apply_V_flagged(
            cl3, {cl3.words[end_ids3[a]]: RF(1)}, False, x_words
        ).items():
            if not vec1:
                continue
            for l1, c1 in _resolvent_labelled(vec1, e0).items():
                for f2, vec2 in _apply_V_flagged(cl3, c1, f1, x_words).items():
                    if not vec2:
                        continue
                    for l2, c2 in _resolvent_labelled(vec2, e0).items():
                        key = (l1, l2, f2)
                        stage[key] = L.vadd(stage.get(key, {}), c2)
        kets[a] = stage
    bras = {}
    for b in (2, 3):
        stage = {}
        for f1, vec1 in _apply_V_flagged(
            cl3, {cl3.words[end_ids3[b]]: RF(1)}, False, x_words
        ).items():
            if not vec1:
                continue
            for l3, c3 in _resolvent_labelled(vec1, e0).items():
                for f2, vec2 in _apply_V_flagged(cl3, c3, f1, x_words).items():
                    if vec2:
                        key = (l3, f2)
                        stage[key] = L.vadd(stage.get(key, {}), vec2)
        bras[b] = stage
    out: dict = defaultdict(lambda: defaultdict(RF))
    for a in (0, 1):
        for b in (2, 3):
            for (l1, l2, fa), kv in kets[a].items():
                for (l3, fb), bv in bras[b].items():
                    if not (fa or fb):
                        continue
                    tot = RF(0)
                    for w, c in bv.items():
                        tot += c * L.inner(w, kv)
                    if tot:
                        out[("direct", l1, l2, l3)][(a, b)] += tot

    def moments(cl):
        m = len(cl.words)
        h2: dict = defaultdict(lambda: [[RF(0)] * m for _ in range(m)])
        v2: dict = defaultdict(lambda: [[RF(0)] * m for _ in range(m)])
        for j in range(m):
            v = cl.V({cl.words[j]: RF(1)})
            for e, per_link, comp in labelled_components(v):
                if e == e0:
                    continue
                lab = state_label(per_link)
                vc = cl.V(comp)
                for i in range(m):
                    val = L.inner(cl.words[i], vc)
                    if val:
                        h2[lab][i][j] += val / (e0 - e)
                        v2[lab][i][j] += val / (e0 - e) ** 2
        return h2, v2

    h3, v3 = moments(cl3)
    h2_, v2_ = moments(cl2)
    ids3 = end_ids3
    for a in (0, 1):
        for b in (2, 3):
            for lab, hm in h3.items():
                for labp, vm in v3.items():
                    val = (
                        sum(
                            hm[ids3[b]][k] * vm[k][ids3[a]] + vm[ids3[b]][k] * hm[k][ids3[a]]
                            for k in range(6)
                        )
                        / 2
                    )
                    if val:
                        out[("fold3", lab, labp)][(a, b)] += -val
            for lab, hm in h2_.items():
                for labp, vm in v2_.items():
                    val = sum(hm[b][k] * vm[k][a] + vm[b][k] * hm[k][a] for k in range(4)) / 2
                    if val:
                        out[("fold2", lab, labp)][(a, b)] += val
    return {k: dict(v) for k, v in out.items()}


def blocks(entries: dict) -> tuple[RF, RF]:
    """(C-odd, C-even) of a ``{(a, b): RF}`` block with missing entries zero."""
    g = {k: entries.get(k, RF(0)) for k in ((0, 2), (0, 3), (1, 2), (1, 3))}
    return L.block_odd(g), L.block_even(g)


def label_text(label) -> str:
    """A channel key as one readable string, e.g. ``direct (2, adj) (4, adj sym) (2, sym)``."""
    parts = [label[0]]
    for extra, names in label[1:]:
        parts.append(f"({extra}, {' '.join(names) if names else '-'})")
    return " ".join(parts)
