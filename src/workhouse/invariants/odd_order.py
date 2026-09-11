"""The odd orders of the strong-coupling band are determinant families: a centre-parity theorem.

Every nonzero odd-order number of the corpus's band -- the SU(3) first-order
``+u``, the third-order hopping ``B_3 = 1975/124848``, the C-even third-order
hopping, the third-order leakage and towers -- is an SU(3) accident of the
following kind, and this module derives the general statement and tests it
with the third engine (``loopcalc``) at N = 3..7 and over Q(N).

**Theorem (centre parity).** Fix a finite set of plaquettes of Z^3 and a
history: a product of face words (each face in either orientation) whose Haar
integral is the matrix element of ``V R V ... V`` between two face words. Let
``c_f`` be the number of words of face ``f`` in the history and ``phi_f`` its
net flux (words of ``f`` minus words of ``f`` conjugate); ``phi_f = c_f mod 2``.
The integral vanishes unless every link's net flux is ``0 mod N``, and a
link's flux is a signed sum of the ``phi_f`` of the faces containing it.

* *N even.* Let ``T`` be the set of x-links at even y, y-links at even z and
  z-links at even x. Every plaquette of Z^3 contains an odd number of links of
  ``T`` (an (x,y)-face at (y, y+1) contains one x-link of ``T`` and its two
  y-links share one z; the other planes likewise). Summing the link fluxes
  over ``T`` mod 2 therefore gives ``sum_f phi_f = sum_f c_f mod 2``. Every
  link flux is ``0 mod N``, hence even, so ``sum_f c_f`` is even: **no history
  with an odd number of face words survives**. An order-``m`` matrix element
  of the des Cloizeaux operator has ``m + 2`` words, and every fold term is a
  product of elements whose orders sum to ``m``, one of them odd. So for even
  N every odd order of the effective Hamiltonian vanishes identically, on every
  cluster, in both C-parity sectors.
* *N odd.* If every link flux were even the same sum would force
  ``sum_f c_f`` even; so an odd-word history has a link of odd flux, hence of
  flux at least ``N`` in magnitude, hence touched by at least ``N`` words:
  ``m + 2 >= N``. The band is an even series in ``u`` through order ``N - 3``.
  At the first odd order ``m = N - 2`` all ``N`` words traverse the odd-flux
  link the same way, and two plaquettes through a link meet only there, so
  every other link of a face carrying ``c_f`` of them has flux ``+-c_f``,
  which is ``0 mod N`` only for ``c_f = N``: the history lies on one face,
  and only the one-plaquette diagonal survives, the ``P <-> P``
  conjugate vertex. On one plaquette the states are characters and ``V`` adds
  or removes one box, so the only path from ``F`` to ``F-bar = Lambda^(N-1)``
  in ``N - 2`` steps is through the columns ``Lambda^k``, and with
  ``E_k - E_0 = (k-1)(N-k-1)(N+1)/N`` (``E = 2 C_2`` on four private links)

      H_(N-2)(F-bar, F) = -(N/(N+1))^(N-3) / ((N-3)!)^2,

  which is ``-1`` at N = 3 (the first-order vertex, ``+u`` in the C-odd
  sector) and ``-25/144`` at N = 5. Hopping and leakage vanish at that order.

What the engine checks. At N = 3 the third-order operator
``H_3 = -(P V R V R V P - (1/2){P V R^2 V P, P V P})`` on the single plaquette
and on both shared-link pairs reproduces every registered SU(3) third-order
number, with the vacuum route ``<1|H_3|1> = -9/32`` accounting for the corpus's
vacuum-subtracted towers and leakage. At N = 4 and 6 every third-order element
is zero. At N = 5 the hops and leakages are zero and the towers split by
``+-25/144``. At N = 7 everything is zero. Over Q(N), where only balanced Haar
families exist, the third-order hops are identically zero.

Consequence for G16 (ADR 0046): the band's tau-series has no odd terms in the
planar limit at any fixed order; for odd N the first odd term is the baryonic
vertex at order ``N - 2``, whose size relative to the plaquette energy is
``(e^2 tau / 2)^N`` up to a power of N, so it is exponentially small in N
below ``tau = 2/e^2`` and exponentially large above it.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial

from .. import constants as K
from .. import loopcalc as LC
from .. import symbolic_rank as SR
from ._core import ROOT, _suite

odd = _suite("the odd orders of the band are determinant families (G16)")

_RUN = "runs/odd_order_band_2026-09-11"
_CITE = "G16; G14; G6; " + _RUN + "; ADR 0047; ADR 0046; MASTER_THEORY §4.4"
_P = ((0, 1), (0, 0, 0))
_COP = ((0, 1), (1, 0, 0))
_PERP = ((0, 2), (0, 0, 0))
_CLUSTERS = {"single": [_P], "coplanar": [_P, _COP], "perpendicular": [_P, _PERP]}
_ORDERS = (1, 2, 3)


def _certificate() -> dict:
    return json.loads((ROOT / _RUN / "certificate.json").read_text(encoding="utf-8"))


def _at_rank(n, fn):
    LC.set_rank(n)
    try:
        return fn()
    finally:
        LC.set_rank(3)


def _mm(a, b):
    m = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(m)) for j in range(m)] for i in range(m)]


def effective(faces) -> dict:
    """The des Cloizeaux operator through third order on the cluster's face words.

    Returns ``{1: H_1, 2: H_2, 3: H_3}`` as matrices in the word basis, in units
    of ``u`` with ``V = -u W`` and ``W`` the unit-coefficient multiplication by
    every face word in both orientations (``loopcalc.Cluster.V``):

        H_1 = -P W P
        H_2 =  P W R W P
        H_3 = -(P W R W R W P - (1/2){P W R^2 W P, P W P}).
    """
    cl = LC.Cluster(faces)
    m = len(cl.words)
    one = LC.F(1)
    h1 = [[LC.inner(cl.words[i], cl.V({cl.words[j]: one})) for j in range(m)] for i in range(m)]
    h2, v2 = cl.second_order()
    kets = [cl.V(cl.R(cl.V(cl.R(cl.V({w: one}))))) for w in cl.words]
    h3 = [[LC.inner(cl.words[i], kets[j]) for j in range(m)] for i in range(m)]
    ac, ca = _mm(v2, h1), _mm(h1, v2)
    return {
        1: [[-h1[i][j] for j in range(m)] for i in range(m)],
        2: h2,
        3: [[-(h3[i][j] - (ac[i][j] + ca[i][j]) / 2) for j in range(m)] for i in range(m)],
    }


def vacuum(order: int):
    """The vacuum energy of one plaquette at the given order: ``<1|H_r|1>`` with E_0 = 0."""
    cl = LC.Cluster([_P])
    one = {(): LC.F(1)}

    def r(v):
        return LC.resolvent(v, LC.F(0))

    if order == 2:
        return LC.inner((), cl.V(r(cl.V(one))))
    if order == 3:
        # <1|W|1> = 0, so the fold vanishes and H_3 = -<1|W R W R W|1>
        return -LC.inner((), cl.V(r(cl.V(r(cl.V(one))))))
    raise ValueError(order)


def band_numbers(n: int) -> dict:
    """Every order-1..3 tower, hop and leakage of the single plaquette and both pairs at rank n.

    ``tower`` is the one-plaquette diagonal, ``hop`` the off-diagonal between the
    two faces of a pair, ``leak`` the pair's diagonal minus the tower, each in
    the C-odd and C-even sectors; the corpus's vacuum-subtracted towers and
    leakages are ``tower - vac`` and ``leak - vac``.
    """
    ops = {name: effective(faces) for name, faces in _CLUSTERS.items()}
    out = {}
    for r in _ORDERS:
        for sector, proj in (("odd", LC.codd), ("even", LC.ceven)):
            single = proj(ops["single"][r], 0, 0)
            out[f"tower{r}_{sector}"] = single
            for pair in ("coplanar", "perpendicular"):
                out[f"hop{r}_{pair}_{sector}"] = proj(ops[pair][r], 0, 1)
                out[f"leak{r}_{pair}_{sector}"] = proj(ops[pair][r], 0, 0) - single
    out["vac2"] = vacuum(2)
    out["vac3"] = vacuum(3)
    return out


def first_odd_vertex(n: int) -> Fraction:
    """``H_(N-2)(F-bar, F) = -(N/(N+1))^(N-3) / ((N-3)!)^2`` for odd N >= 3."""
    if n < 3 or n % 2 == 0:
        raise ValueError("the first odd order exists for odd N >= 3 only")
    return -(Fraction(n, n + 1) ** (n - 3)) / Fraction(factorial(n - 3)) ** 2


def parity_links(box: int) -> tuple[bool, int]:
    """Whether the link set T hits every face of a ``box``^3 block of Z^3 an odd number of times.

    T is the x-links at even y, the y-links at even z and the z-links at even x.
    Returns (all odd, number of faces checked).
    """
    faces = 0
    for x in range(box):
        for y in range(box):
            for z in range(box):
                for plane in ((0, 1), (0, 2), (1, 2)):
                    site = (x, y, z)
                    d, e = plane
                    hits = 0
                    for lk_dir, base in (
                        (d, site),
                        (d, tuple(s + (1 if k == e else 0) for k, s in enumerate(site))),
                        (e, site),
                        (e, tuple(s + (1 if k == d else 0) for k, s in enumerate(site))),
                    ):
                        parity_coord = base[(lk_dir + 1) % 3]
                        hits += parity_coord % 2 == 0
                    faces += 1
                    if hits % 2 == 0:
                        return False, faces
    return True, faces


def odd_keys(row: dict) -> list[str]:
    """The first- and third-order towers, hops and leakages of a ``band_numbers`` row."""
    return [k for k in row if k.startswith(("tower1", "tower3", "hop1", "hop3", "leak1", "leak3"))]


def odd_order_survives(n: int, order: int) -> bool:
    """The theorem's criterion: an odd order ``m`` can be nonzero only for odd N with m >= N - 2."""
    return order % 2 == 0 or (n % 2 == 1 and order >= n - 2)


# ---------------------------------------------------------------- one plaquette, by characters
def _reduce(lam: tuple, n: int) -> tuple:
    """An SU(N) irrep as a partition with at most N rows, full columns removed."""
    lam = tuple(lam) + (0,) * (n - len(lam))
    lam = lam[:n]
    return tuple(x - lam[-1] for x in lam)


def casimir(lam: tuple, n: int) -> Fraction:
    """``C_2`` of the SU(N) irrep ``lam``: (1/2)(sum lam_i (lam_i + N + 1 - 2i) - |lam|^2/N)."""
    lam = _reduce(lam, n)
    boxes = sum(lam)
    return Fraction(sum(x * (x + n + 1 - 2 * i) for i, x in enumerate(lam, start=1)), 2) - Fraction(
        boxes * boxes, 2 * n
    )


def _add_box(lam: tuple, n: int):
    """Pieri: ``s_lam s_F`` is the sum over one added box."""
    lam = _reduce(lam, n)
    for i in range(n):
        if i == 0 or lam[i] < lam[i - 1]:
            mu = list(lam)
            mu[i] += 1
            yield _reduce(tuple(mu), n)


def _add_column(lam: tuple, n: int):
    """Pieri: ``s_lam s_F-bar`` is the sum over vertical strips of N - 1 boxes."""
    lam = _reduce(lam, n)
    for skip in range(n):
        mu = [x + (0 if i == skip else 1) for i, x in enumerate(lam)]
        if all(mu[i] >= mu[i + 1] for i in range(n - 1)):
            yield _reduce(tuple(mu), n)


def _w(vec: dict, n: int) -> dict:
    """The plaquette perturbation ``W = chi_F + chi_F-bar`` on a character vector."""
    out: dict = {}
    for lam, c in vec.items():
        for mu in list(_add_box(lam, n)) + list(_add_column(lam, n)):
            out[mu] = out.get(mu, 0) + c
    return {k: v for k, v in out.items() if v}


def character_series(n: int, order: int, start: str) -> list[Fraction]:
    """Rayleigh-Schrodinger energies ``[E_0, E_1, ..., E_order]`` of one plaquette at rank n.

    ``start`` is ``"odd"`` (``chi_F - chi_F-bar``), ``"even"`` (``chi_F + chi_F-bar``)
    or ``"vac"`` (``chi_0``); the sector state is nondegenerate in its sector, so
    the series is the des Cloizeaux diagonal there. ``H0 = 2 C_2`` on the four
    private links, ``V = -W``, intermediate normalisation ``<psi_0|psi_k> = 0``.
    """
    f, fbar = _reduce((1,), n), _reduce((1,) * (n - 1), n)
    if start == "vac":
        psi0 = {_reduce((), n): Fraction(1)}
    else:
        psi0 = {f: Fraction(1), fbar: Fraction(1 if start == "even" else -1)}
    e0 = 2 * casimir(next(iter(psi0)), n)
    norm = sum(c * c for c in psi0.values())
    psi = [psi0]
    energies = [e0]
    for k in range(1, order + 1):
        v = {lam: -c for lam, c in _w(psi[k - 1], n).items()}
        ek = sum(psi0.get(lam, 0) * c for lam, c in v.items()) / norm
        energies.append(ek)
        r = dict(v)
        for j in range(1, k + 1):
            for lam, c in psi[k - j].items():
                r[lam] = r.get(lam, 0) - energies[j] * c
        nxt = {}
        for lam, c in r.items():
            if c == 0:
                continue
            e = 2 * casimir(lam, n)
            if e == e0:
                if lam in psi0:
                    continue  # the sector's own state: zero by intermediate normalisation
                raise ArithmeticError(f"degenerate state {lam} outside the model space at N = {n}")
            nxt[lam] = c / (e0 - e)
        psi.append(nxt)
    return energies


def towers(n: int, order: int) -> dict:
    """``tower_r_odd``, ``tower_r_even`` and ``vac_r`` for r = 1..order, by characters."""
    out = {}
    series = {s: character_series(n, order, s) for s in ("odd", "even", "vac")}
    for r in range(1, order + 1):
        out[f"tower{r}_odd"] = series["odd"][r]
        out[f"tower{r}_even"] = series["even"][r]
        out[f"vac{r}"] = series["vac"][r]
    return out


# ---------------------------------------------------------------- the cheap N = 5 elements
def _flagged_third(faces, x_words: set):
    """``V R V R V`` on each first-face word, split by whether an X word was inserted."""
    cl = LC.Cluster(faces)
    kets = {}
    for a in (0, 1):
        v = {False: {cl.words[a]: LC.F(1)}, True: {}}
        for step in range(3):
            v = LC._split_V(cl, v, x_words)
            if step < 2:
                v = LC._R_flagged(cl, v)
        kets[a] = v
    return cl, kets


def pair_third_cheap(faces) -> dict:
    """The third-order hop and the X-touched leakage of a pair, for N >= 4 where ``P W P = 0``.

    Histories with no word of the second face are the single plaquette's own and
    cancel in the leakage; only the flagged ones are integrated, so no N-word
    determinant family of the first face is ever met. Returns ``hop3_odd``,
    ``hop3_even``, ``leak3_odd``, ``leak3_even`` in the conventions of
    ``band_numbers``.
    """
    if LC.N < 4:
        raise ValueError("pair_third_cheap assumes P W P = 0, which needs N >= 4")
    words = LC.Cluster(faces).words
    cl, kets = _flagged_third(faces, x_words={words[2], words[3]})
    full = [[LC.F(0)] * 4 for _ in range(4)]
    leak = [[LC.F(0)] * 2 for _ in range(2)]
    for a in (0, 1):
        both = LC.vadd(kets[a][False], kets[a][True])
        for b in (0, 1):
            leak[b][a] = -LC.inner(cl.words[b], kets[a][True])
            full[b + 2][a] = -LC.inner(cl.words[b + 2], both)
    return {
        "hop3_odd": LC.codd(full, 1, 0),
        "hop3_even": LC.ceven(full, 1, 0),
        "leak3_odd": LC.codd(leak, 0, 0),
        "leak3_even": LC.ceven(leak, 0, 0),
    }


# ---------------------------------------------------------------- the checks
_PARITY = (
    "centre parity: the link set T (x-links at even y, y-links at even z, z-links at even x) "
    "meets every plaquette of Z^3 an odd number of times, so a history with an odd number of "
    "face words has a link of odd flux; for even N every odd order vanishes identically, and "
    "for odd N the order m vanishes unless m >= N - 2"
)


@odd.check(_PARITY, _CITE)
def _():
    ok, faces = parity_links(6)
    table = {(n, m): odd_order_survives(n, m) for n in range(3, 13) for m in range(1, 12)}
    even_n_closed = all(not v for (n, m), v in table.items() if n % 2 == 0 and m % 2 == 1)
    first_odd = {n: min(m for m in range(1, 12, 2) if table[(n, m)]) for n in (3, 5, 7, 9, 11)}
    ok = ok and even_n_closed and first_odd == {3: 1, 5: 3, 7: 5, 9: 7, 11: 9}
    return ok, (
        f"T hits all {faces} faces of a 6^3 block an odd number of times; a link flux is 0 mod N, "
        "so sum_f c_f = sum_(links in T) flux = 0 mod 2 for even N, and for odd N some link "
        "carries |flux| >= N, hence >= N words: the first odd order is m = N - 2 "
        f"({', '.join(f'N = {n}: m = {m}' for n, m in first_odd.items())}); every fold term "
        "contains an odd-order factor"
    )


_SU3 = (
    "the third engine reproduces the SU(3) third order: B_3 = 1975/124848, t_3+ = -6335/249696, "
    "the domino diagonals -24541/62424 and -517313/6242400, the vacuum route -9/32, the towers "
    "7/32 and 101/200, leak_3 = -12331/249696 and d_3 = -109151/249696"
)


@odd.check(_SU3, _CITE + "; ENGINE_FLUX_su3_domino_d3.py; ADR 0023")
def _():
    # Live: the single plaquette and the coplanar pair at N = 3 (about two minutes; every
    # history is a (3,0) determinant family). Pinned: the perpendicular pair from the run.
    def live():
        ops = {name: effective(_CLUSTERS[name]) for name in ("single", "coplanar")}
        out = {}
        for r in _ORDERS:
            for sector, proj in (("odd", LC.codd), ("even", LC.ceven)):
                out[f"tower{r}_{sector}"] = proj(ops["single"][r], 0, 0)
                out[f"hop{r}_{sector}"] = proj(ops["coplanar"][r], 0, 1)
                out[f"leak{r}_{sector}"] = (
                    proj(ops["coplanar"][r], 0, 0) - out[f"tower{r}_{sector}"]
                )
        out["vac2"], out["vac3"] = vacuum(2), vacuum(3)
        return out

    b = _at_rank(3, live)
    perp = _certificate()["ranks"]["3"]
    vac2, vac3 = b["vac2"], b["vac3"]
    t3 = -b["hop3_odd"]  # coplanar incidence -1, as at second order
    tower3_odd, tower3_even = b["tower3_odd"] - vac3, b["tower3_even"] - vac3
    leak3 = b["leak3_odd"] - vac3
    d3 = tower3_odd + 12 * leak3 - 4 * t3
    ok = (
        b["tower1_odd"] == 1
        and b["tower1_even"] == -1
        and vac2 == Fraction(-3, 4)
        and b["tower2_odd"] - vac2 == Fraction(1, 2)
        and b["hop2_odd"] == -Fraction(5, 612)
        and vac3 == Fraction(-9, 32)
        and t3 == Fraction(K.B_3.p, K.B_3.q)
        and Fraction(perp["hop3_perpendicular_odd"]) == t3
        and b["hop3_even"] == Fraction(perp["hop3_perpendicular_even"]) == Fraction(-6335, 249696)
        and b["tower3_odd"] + b["leak3_odd"] == Fraction(-24541, 62424)
        and b["tower3_even"] + b["leak3_even"] == Fraction(-517313, 6242400)
        and tower3_odd == Fraction(7, 32)
        and tower3_even == Fraction(101, 200)
        and leak3 == Fraction(K.LEAK_3.p, K.LEAK_3.q)
        and Fraction(perp["leak3_perpendicular_odd"]) == b["leak3_odd"]
        and d3 == Fraction(K.D_3.p, K.D_3.q)
    )
    return (
        ok,
        (
            f"live at N = 3: first-order vertex +-1, vacuum route {vac2} and {vac3}, tower_3 = "
            f"{tower3_odd} (C-odd) and {tower3_even} (C-even) after vacuum subtraction, "
            f"t_3 = {t3} (coplanar -t_3, perpendicular +t_3 pinned), t_3+ = {b['hop3_even']} in "
            f"both geometries, leak_3 = {leak3} in both geometries, so d_3 = 7/32 + 12 leak_3 - "
            f"4 t_3 = {d3}: the whole SU(3) third-order ledger from an independent engine, every "
            "number a (3,0) determinant family"
        ),
        {"VAC3_SINGLE": vac3},
    )


_CHARACTERS = (
    "the one-plaquette character engine (Pieri rule, Rayleigh-Schrodinger) agrees with the third "
    "engine's towers and vacuum at N = 3, 4, 6, 7 through third order, and shows the first odd "
    "order of odd N at m = N - 2 with vertex (N/(N+1))^(N-3)/((N-3)!)^2 at N = 5, 7, 9 and no odd "
    "order through 7 at N = 4, 6, 8"
)


@odd.check(_CHARACTERS, _CITE, rests_on=(_PARITY,))
def _():
    cert = _certificate()["ranks"]
    agree = True
    for n in ("3", "4", "6", "7"):
        t = towers(int(n), 3)
        for k in (
            "tower1_odd",
            "tower1_even",
            "tower2_odd",
            "tower2_even",
            "tower3_odd",
            "tower3_even",
            "vac2",
            "vac3",
        ):
            agree = agree and Fraction(cert[n][k]) == t[k]
    even_zero = all(
        towers(n, 7)[f"tower{m}_{s}"] == 0 and towers(n, 7)[f"vac{m}"] == 0
        for n in (4, 6, 8)
        for m in (1, 3, 5, 7)
        for s in ("odd", "even")
    )
    vertex_ok, first = True, {}
    for n in (5, 7, 9):
        t = towers(n, n - 2)
        v = -first_odd_vertex(n)
        first[n] = t[f"tower{n - 2}_odd"]
        vertex_ok = (
            vertex_ok
            and t[f"tower{n - 2}_odd"] == v
            and t[f"tower{n - 2}_even"] == -v
            and all(t[f"tower{m}_odd"] == t[f"tower{m}_even"] == 0 for m in range(1, n - 2, 2))
        )
    ok = agree and even_zero and vertex_ok
    return ok, (
        "characters agree with loopcalc on 8 towers/vacua at each of N = 3, 4, 6, 7; odd orders "
        "1, 3, 5, 7 of the towers and the vacuum vanish at N = 4, 6, 8; the first odd tower of N = "
        f"5, 7, 9 is {first[5]}, {first[7]}, {first[9]} in the C-odd sector at orders 3, 5, 7, the "
        "negatives in the C-even sector, with every lower odd order zero"
    )


_EVEN_RANK = (
    "at N = 4 and N = 6 every third-order element of the single plaquette and of both pairs "
    "is zero in both sectors, and so is the first order: the band is even in u"
)


@odd.check(_EVEN_RANK, _CITE, rests_on=(_PARITY,))
def _():
    live = _at_rank(4, lambda: band_numbers(4))
    live_zero = all(live[k] == 0 for k in odd_keys(live)) and live["vac3"] == 0
    live_second = live["hop2_coplanar_odd"] == -Fraction(K.hopping(4).p, K.hopping(4).q)
    cert = _certificate()["ranks"]
    pinned = {
        n: all(Fraction(cert[n][k]) == 0 for k in odd_keys(cert[n]))
        and Fraction(cert[n]["vac3"]) == 0
        for n in ("4", "6")
    }
    ok = live_zero and live_second and all(pinned.values()) and len(odd_keys(live)) == 20
    return ok, (
        "live at N = 4: all 20 first- and third-order towers, hops and leakages are 0 and the "
        f"second-order hop is -t_4 = {live['hop2_coplanar_odd']}; pinned at N = 4 and 6: the same "
        "20 elements and the third-order vacuum are 0"
    )


_FIVE = (
    "at N = 5 the third order is the one-plaquette five-word vertex alone: the towers split by "
    "-+25/144 = -+(5/6)^2/(2!)^2, the hops and leakages vanish; at N = 7 everything vanishes"
)


@odd.check(_FIVE, _CITE, rests_on=(_PARITY,))
def _():
    cert = _certificate()["ranks"]
    five, seven = cert["5"], cert["7"]
    vertex = first_odd_vertex(5)
    t = towers(5, 3)
    cheap = _at_rank(5, lambda: pair_third_cheap(_CLUSTERS["coplanar"]))
    ok = (
        vertex == Fraction(-25, 144)
        and t["tower3_odd"] == -vertex
        and t["tower3_even"] == vertex
        and all(v == 0 for v in cheap.values())
        and all(Fraction(five[k]) == 0 for k in five if k.startswith(("hop3", "leak3")))
        and all(Fraction(seven[k]) == 0 for k in odd_keys(seven))
        and Fraction(seven["vac3"]) == 0
        and first_odd_vertex(3) == -1
    )
    # the Peter-Weyl path with the explicit energies
    e0 = 2 * casimir((1,), 5)
    e2 = 2 * casimir((1, 1), 5)
    e3 = 2 * casimir((1, 1, 1), 5)
    path = -1 / ((e0 - e2) * (e0 - e3))
    ok = ok and path == vertex and e0 == Fraction(24, 5) and e2 == e3 == Fraction(36, 5)
    return ok, (
        f"at N = 5: tower_3 = {t['tower3_odd']} (C-odd), {t['tower3_even']} (C-even) by "
        "characters; "
        "the coplanar hop_3 and X-touched leak_3 are 0 live in both sectors and both pairs' are 0 "
        "pinned; the vertex is the one path F -> Lambda^2 -> Lambda^3 -> F-bar, "
        f"-1/((E_0 - E_2)(E_0 - E_3)) = {path} with E_0 = {e0}, E_2 = E_3 = {e2}; at N = 7 all "
        "first- and third-order elements are 0 (first odd order m = 5)"
    )


_SYMBOLIC = (
    "over Q(N) the third-order hops of both pairs are identically zero in both sectors: no "
    "balanced Haar family reaches an odd order, so every nonzero odd-order number of the corpus "
    "is a determinant-family number"
)


@odd.check(_SYMBOLIC, _CITE + "; ADR 0029")
def _():
    with SR.Symbolic() as S:
        hops = {}
        for pair in ("coplanar", "perpendicular"):
            cl = LC.Cluster(_CLUSTERS[pair])
            one = LC.F(1)
            for a in (2, 3):
                ket = cl.V(cl.R(cl.V(cl.R(cl.V({cl.words[a]: one})))))
                for b in (0, 1):
                    hops[(pair, b, a)] = LC.inner(cl.words[b], ket)
    zero = all(x == 0 for x in hops.values())
    ok = zero and len(hops) == 8 and S.stats["max_charge"] <= 5
    return ok, (
        f"8 third-order pair elements over Q(N) all 0; largest flux met {S.stats['max_charge']} "
        "(the shared link under four words of one face and the other's conjugate), largest "
        f"balanced Weingarten family n = {S.stats['max_weingarten_n']}: the third order has no "
        "balanced-family content at any rank, and its determinant families are the N = 3 and "
        "N = 5 ones"
    )


_TAU = (
    "consequence for G16: for even N the band is even in u at every order, for odd N through "
    "order N - 3, so the tau-series of ADR 0046 has no odd terms in the planar limit; the first "
    "odd term at odd N is the baryonic vertex (N/(N+1))^(N-3)/((N-3)!)^2 at order N - 2"
)


@odd.check(_TAU, _CITE + "; NOTE_O4 §11", rests_on=(_PARITY, _CHARACTERS))
def _():
    vals = {n: -first_odd_vertex(n) for n in (3, 5, 7, 9, 11)}
    # with u = N^2 tau/2 the term relative to 2 C_F ~ N is vals[n] (N^2 tau/2)^(N-2) / N; by
    # Stirling, ((N-3)!)^2 ~ (N/e)^(2N) N^-6, so this is (e^2 tau/2)^N times a power of N.
    # Checked exactly: the two-step growth factor of the tau-free part lies within a factor 2
    # of (e^2/2)^2 from N = 7 on, the power-of-N corrections.
    free = {n: v * Fraction(n * n, 2) ** (n - 2) / n for n, v in vals.items()}
    growth = {n: free[n + 2] / free[n] for n in (3, 5, 7, 9)}
    e2_half_sq = Fraction(1365, 100)  # (e^2/2)^2 = 13.65...
    ok = (
        vals[3] == 1
        and vals[5] == Fraction(25, 144)
        and vals[7] == Fraction(7**4, 8**4 * 24**2)
        and all(e2_half_sq / 2 < growth[n] < e2_half_sq * 2 for n in (7, 9))
    )
    return ok, (
        f"vertex at N = 3, 5, 7: {vals[3]}, {vals[5]}, {vals[7]}; with u = N^2 tau/2 the term "
        "relative to the plaquette energy is (e^2 tau/2)^N up to a power of N: exponentially "
        "small below tau = 2/e^2 = 0.27 and large above it; the even orders' N^-(4k-1) law is "
        "untouched"
    )
