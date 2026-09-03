"""Second order at every rank: the scalar ledger and the charge-even symbol.

The manuscripts through revision 5 give the second-order hopping ``t_N`` at
every rank and the second-order *scalar* at ``N = 3`` only, calling the
diagonal "a scalar ``d_{2,N,L}``" and identifying the charge-even Bloch
symbol with the unsigned incidence as a hypothesis. Both are derivable from
the same three inputs the hopping uses -- the fusion table, the plaquette-loop
energies, and the centre-charge process census -- and this suite carries the
arithmetic out:

* the on-site second-order scalar is ``sigma_N + 1/C_F + 12 ell_N`` in both
  charge sectors, where ``sigma_N`` is the reduced same-face route and the
  rest is what the vacuum subtraction leaves of the other ``3L^3 - 1``
  plaquettes -- ``L`` cancels, and the flat scalar is that minus ``4 t_N``;
* the charge-even off-diagonal is ``ell_N`` on every adjacent pair whatever
  the orientations, and ZERO on every link-disjoint pair, because the
  vacuum-mediated route ``2/E_F`` is cancelled there by the doubly-excited
  exchange route ``2/(E_F - 2E_F)`` -- so the charge-even second-order symbol
  is ``ell_N`` times the unsigned incidence, unconditionally;
* the link-resolved census split the manuscript conjectured is the monomial
  bookkeeping of its own shared-link theorem, at every rank.

Everything is symbolic in ``N`` where the rank is generic and stated
separately at the two exceptional ranks: ``N = 3``, where ``Lambda^2 F`` is
the conjugate fundamental and lands in the retained shell, and ``N = 4``,
where it is self-conjugate. At ``N = 3`` every number is joined to the
registry and to an independent engine's second-order table
(``runs/g3_chain_amplitude_replication_2026-09-02``), which is what makes the
all-rank formulas more than an extrapolation of one rank.

Nothing here is a remainder estimate: these are finite-volume Taylor
coefficients, exactly as the manuscript says of the hopping.
"""

from __future__ import annotations

import json
import re
from fractions import Fraction

from sympy import Rational, Symbol, factor, limit, oo, series, simplify, sympify

from .. import constants as K
from ._core import ROOT, _suite

second_order = _suite("second order at every rank: the scalar ledger and the charge-even symbol")

_N = K.N
_L = Symbol("L", positive=True)
_REPLICATION = ROOT / "runs" / "g3_chain_amplitude_replication_2026-09-02"
_TWO_CUBE_CERT = (
    ROOT
    / "runs"
    / "two_cube_codd_o2_2026-08-29"
    / "two_cube_b6_codd_o2_connected_kernel_certificate.json"
)


def _cf(n):
    n = sympify(n)
    return (n**2 - 1) / (2 * n)


def _ef(n):
    """The one-plaquette electric energy, four fundamental half-links."""
    return 2 * _cf(n)


def _casimir(label, n):
    """Quadratic Casimirs in the normalisation C_2(F) = C_F."""
    n = sympify(n)
    return {
        "1": 0 * n,
        "Adj": n,
        "Sym": (n - 1) * (n + 2) / n,
        "SymBar": (n - 1) * (n + 2) / n,
        "Lam": (n + 1) * (n - 2) / n,
        "LamBar": (n + 1) * (n - 2) / n,
        "F": _cf(n),
        "FBar": _cf(n),
    }[label]


def _identify(label, n):
    """The rank-dependent coincidences among the two-flux irreps.

    ``Lambda^2 F`` is the conjugate fundamental at ``N = 3`` (the epsilon
    tensor) and self-conjugate at ``N = 4`` (the real six of su(4)); at every
    other rank the four like irreps are distinct, and ``Sym^2 F`` is never
    fundamental or self-conjugate for ``N >= 3``.
    """
    if n == 3:
        return {"Lam": "FBar", "LamBar": "F"}.get(label, label)
    if n == 4:
        return {"LamBar": "Lam"}.get(label, label)
    return label


def _same_face_vector(n, sector):
    """``sqrt2 * X_p |p, sector>`` as ``{irrep: coefficient}``, coincidences merged.

    ``(chi + chibar)(chi +- chibar)`` is ``chi^2 + 2 chi chibar + chibar^2``
    in the even sector and ``chi^2 - chibar^2`` in the odd one, with
    ``chi_F^2 = chi_Sym + chi_Lam`` and ``chi_F chibar_F = 1 + chi_Adj``.
    """
    sign = 1 if sector == "even" else -1
    raw = {"Sym": 1, "Lam": 1, "SymBar": sign, "LamBar": sign}
    if sector == "even":
        raw["1"] = 2
        raw["Adj"] = 2
    merged: dict[str, int] = {}
    for label, coefficient in raw.items():
        target = _identify(label, n)
        merged[target] = merged.get(target, 0) + coefficient
    return merged


def _same_face_route(n, sector):
    """The reduced same-face route ``<p|X_p Q (E_F - H_E)^{-1} Q X_p|p>``.

    Returns ``(sigma, retained)``: the resolvent sum over the non-retained
    components, and the coefficient of ``|p, sector>`` inside ``X_p|p, sector>``
    (which is ``-P V P`` up to sign, and is removed by ``Q``). A single-plaquette
    loop in irrep ``R`` costs ``2 C_2(R)`` electrically; the vacuum costs zero.
    """
    n = sympify(n)
    vector = _same_face_vector(n, sector)
    sign = 1 if sector == "even" else -1
    retained = Rational(vector.get("F", 0) + sign * vector.get("FBar", 0), 2)
    sigma = 0
    for label, coefficient in vector.items():
        if label in ("F", "FBar") or coefficient == 0:
            continue
        energy = 2 * _casimir(label, n)
        sigma += Rational(coefficient**2, 2) / (_ef(n) - energy)
    return simplify(sigma), retained


def _channel_weights(n):
    """``w_rho = -(d_rho/N^2)/(C_F + C_rho/2)`` per fusion channel."""
    n = sympify(n)
    table = {
        "1": (1, 0 * n),
        "Adj": (n**2 - 1, n),
        "Lam": (n * (n - 1) / 2, (n + 1) * (n - 2) / n),
        "Sym": (n * (n + 1) / 2, (n - 1) * (n + 2) / n),
    }
    return {rho: -(d / n**2) / (_cf(n) + c / 2) for rho, (d, c) in table.items()}


_MIXED = ("1", "Adj")
_LIKE = ("Lam", "Sym")


def _cross_element(n, sector, s, s_prime):
    """``<p'|X_p Pi X_{p'}|p>`` summed over channels, by the monomial bookkeeping.

    Both states are expanded in oriented characters, ``|p,+->`` carrying
    coefficient ``eps/sqrt2`` in the odd sector and ``1/sqrt2`` in the even.
    For the monomial pair ``(eps, eps')`` the shared link carries the like
    family iff ``eps s = eps' s'`` and the mixed family otherwise, and the
    matrix element is the projected norm ``d_rho/N^2`` on that family. The
    channel weight then carries the resolvent. Returns the per-channel
    contributions as a dict, and the total including the vacuum route in the
    even sector.
    """
    n = sympify(n)
    w = _channel_weights(n)
    per_channel = dict.fromkeys(w, 0)
    for eps in (1, -1):
        for eps_p in (1, -1):
            coefficient = Rational(eps * eps_p, 2) if sector == "odd" else Rational(1, 2)
            family = _LIKE if eps * s == eps_p * s_prime else _MIXED
            for rho in family:
                per_channel[rho] += coefficient * w[rho]
    vacuum = 0 if sector == "odd" else 2 / _ef(n)
    return per_channel, simplify(sum(per_channel.values()) + vacuum)


def _diagonal(n, sector):
    """The vacuum-subtracted second-order diagonal, with the torus size symbolic.

    same-face route + 12 adjacent neighbours at ``A_N + B_N`` each + the
    ``3L^3 - 13`` link-disjoint plaquettes at ``2/(E_F - 2E_F)`` each, minus
    the vacuum energy ``3L^3 * 2/(0 - E_F)``.
    """
    n = sympify(n)
    sigma, _retained = _same_face_route(n, sector)
    adjacent = sum(_channel_weights(n).values())
    disjoint = 2 / (_ef(n) - 2 * _ef(n))
    vacuum_per_plaquette = 2 / (0 - _ef(n))
    total = sigma + 12 * adjacent + (3 * _L**3 - 13) * disjoint - 3 * _L**3 * vacuum_per_plaquette
    return simplify(total), sigma


def _ell(n):
    n = sympify(n)
    return simplify(K.antiparallel_sum(n) + K.parallel_sum(n) + 1 / _cf(n))


@second_order.check(
    "the second-order on-site scalar is closed form at every rank: "
    "same-face route + 1/C_F + 12 ell_N, and L cancels",
    "PUBLICATION rev5 Cor. (global torus assembly), which names the scalar d_{2,N,L} "
    "and gives it at N = 3 only; C13; G24",
    rests_on=(
        "ell_N = A_N + B_N + 1/C_F, the vacuum-mediated route at every rank",
        "second-order off-diagonal processes are exactly the adjacent shared-link channels",
        "the plaquette graph is 12-regular and two faces share at most one link",
    ),
)
def _():
    # The manuscript's corollary proves the second-order diagonal is a scalar
    # by symmetry and never writes it down. It is three routes: the reduced
    # same-face route, twelve adjacent neighbours each worth A_N + B_N, and
    # the 3L^3 - 13 link-disjoint plaquettes each worth -1/C_F -- against a
    # vacuum subtraction of 3L^3 (-1/C_F). The volume cancels and thirteen
    # bubbles survive: one for the plaquette itself and one per neighbour,
    # which is exactly why the per-neighbour leakage is ell_N = A_N + B_N + 1/C_F
    # rather than the bare channel sum.
    diagonal, sigma = _diagonal(_N, "odd")
    closed = simplify(sigma + 1 / _cf(_N) + 12 * _ell(_N))
    l_free = simplify(diagonal - closed) == 0 and _L not in diagonal.free_symbols
    # the generic same-face route is two resolvents at the two-flux gaps
    gaps = {
        "Sym": simplify(_ef(_N) - 2 * _casimir("Sym", _N) + (_N - 1) * (_N + 3) / _N) == 0,
        "Lam": simplify(_ef(_N) - 2 * _casimir("Lam", _N) + (_N + 1) * (_N - 3) / _N) == 0,
    }
    sigma_closed = -_N / ((_N - 1) * (_N + 3)) - _N / ((_N + 1) * (_N - 3))
    tower = simplify(sigma + 1 / _cf(_N))
    tower_closed = -12 * _N / ((_N**2 - 1) * (_N**2 - 9))
    flat = simplify(closed - 4 * K.hopping(_N))
    values = {
        n: {"tower": tower.subs(_N, n), "onsite": closed.subs(_N, n), "flat": flat.subs(_N, n)}
        for n in (5, 6, 7)
    }
    # N = 3 and N = 4 go through the exceptional same-face routes below
    diag3, sigma3 = _diagonal(3, "odd")
    diag4, sigma4 = _diagonal(4, "odd")
    at3 = diag3 == K.D_MINUS_2 and diag3 - 4 * K.hopping(3) == K.BAND_ODD_FLAT
    at4 = diag4 == sigma4 + 1 / _cf(4) + 12 * _ell(4)
    ok = (
        l_free
        and all(gaps.values())
        and simplify(sigma - sigma_closed) == 0
        and simplify(tower - tower_closed) == 0
        and at3
        and at4
        and values[5]
        == {
            "tower": Rational(-5, 32),
            "onsite": Rational(-4785, 20384),
            "flat": Rational(-4945, 20384),
        }
        and values[6]["tower"] == Rational(-8, 105)
    )
    return (
        ok,
        (
            "d_2^- = sigma_N^- + 1/C_F + 12 ell_N with L cancelling exactly; for N >= 5 the "
            "same-face route is -N/((N-1)(N+3)) - N/((N+1)(N-3)), the two denominators being the "
            "two-flux gaps E_F - 2C_2(Sym^2 F) and E_F - 2C_2(Lambda^2 F), and the tower "
            f"sigma + 1/C_F collapses to {factor(tower_closed)} -- order N^-3, the same-face route "
            f"and the vacuum bubble cancelling at leading order. Flat scalar {factor(flat)}. "
            f"At N = 3 the route gives {diag3} on-site and {diag3 - 4 * K.hopping(3)} flat, the "
            f"register's values; at N = 4 on-site {diag4}, flat "
            f"{diag4 - 4 * K.hopping(4)}; at N = 5 "
            f"tower -5/32, on-site -4785/20384, flat -4945/20384; at N = 6 tower -8/105, flat "
            f"{values[6]['flat']}"
        ),
        {
            "TOWER_2_ODD_N": factor(tower_closed),
            "ONSITE_2_ODD_N": factor(closed),
            "FLAT_2_ODD_N": factor(flat),
            "TOWER_2_ODD_4": sigma4 + 1 / _cf(4),
            "ONSITE_2_ODD_4": diag4,
            "FLAT_2_ODD_4": diag4 - 4 * K.hopping(4),
            "TOWER_2_ODD_5": values[5]["tower"],
            "ONSITE_2_ODD_5": values[5]["onsite"],
            "FLAT_2_ODD_5": values[5]["flat"],
            "FLAT_2_ODD_6": values[6]["flat"],
        },
    )


@second_order.check(
    "the same-face route is exceptional at N = 3 and N = 4: "
    "Lambda^2 F is the conjugate fundamental, then self-conjugate",
    "PUBLICATION rev5 Lemma (reduced same-face route), which proves the N = 3 case; C13",
    rests_on=("each channel gap is C_F + C_R/2, and the weights sum to one",),
)
def _():
    # The manuscript's lemma does N = 3 by hand: Lambda^2 F = Fbar, so the
    # same-face vector carries a retained-shell component -|p,-> that Q_-
    # removes, and only the sextet survives at gap 8/3 - 20/3 = -4. At N = 4
    # the six of su(4) is real, so chi_Lam - chibar_Lam cancels in the odd
    # sector and DOUBLES in the even one; from N = 5 on the four like irreps
    # are distinct. The retained coefficient is P V P, which the manuscript
    # gives as -+ delta_{N,3}: the first-order term is SU(3)-only because
    # only the epsilon tensor can turn two fluxes back into one.
    odd = {n: _same_face_route(n, "odd") for n in (3, 4, 5)}
    even = {n: _same_face_route(n, "even") for n in (3, 4, 5)}
    generic_odd = _same_face_route(_N, "odd")[0]
    generic_even = _same_face_route(_N, "even")[0]
    ok = (
        odd[3] == (Rational(-1, 4), -1)
        and even[3] == (Rational(-1, 10), 1)
        and odd[4] == (Rational(-4, 21), 0)
        and even[4][1] == 0
        and even[4][0] == Rational(8, 15) - Rational(8, 17) - Rational(4, 21) - Rational(8, 5)
        and odd[5] == (generic_odd.subs(_N, 5), 0)
        and even[5] == (generic_even.subs(_N, 5), 0)
        and simplify(generic_even - (1 / _cf(_N) - 2 * _N / (_N**2 + 1) + generic_odd)) == 0
        # the same-face pieces the manuscript names at N = 3: sextet -1/4;
        # even: vacuum 3/4, adjoint -3/5, sextet -1/4
        and Rational(3, 4) - Rational(3, 5) - Rational(1, 4) == Rational(-1, 10)
    )
    return (
        ok,
        (
            "odd: N = 3 sextet only, -1/4, with P V P = -1 removed by Q_-; N = 4 Sym^2 F only, "
            "-4/21, the self-conjugate six cancelling; N >= 5 both like irreps, "
            f"{factor(generic_odd)}. Even: N = 3 vacuum 3/4 + adjoint -3/5 + sextet -1/4 = -1/10 "
            f"with P V P = +1; N = 4 the real six enters doubled, {even[4][0]}; N >= 5 "
            f"{factor(generic_even)} = 1/C_F - 2N/(N^2+1) + sigma^-. The retained coefficient is "
            "-+1 at N = 3 and 0 above, which is the manuscript's [u] H_eff = +-delta_{N,3}"
        ),
        {
            "SAME_FACE_2_ODD_3": odd[3][0],
            "SAME_FACE_2_EVEN_3": even[3][0],
            "SAME_FACE_2_ODD_4": odd[4][0],
            "SAME_FACE_2_EVEN_4": even[4][0],
            "SAME_FACE_2_ODD_N": factor(generic_odd),
            "SAME_FACE_2_EVEN_N": factor(generic_even),
        },
    )


@second_order.check(
    "at N = 3 the all-rank second-order ledger is the register and an "
    "independent engine's table, line by line",
    "runs/g3_chain_amplitude_replication_2026-09-02/chain_amplitude_certificate.json; "
    "PAPER App. B; MASTER paper §5",
    rests_on=(
        "the second-order on-site scalar is closed form at every rank: "
        "same-face route + 1/C_F + 12 ell_N, and L cancels",
        "the engine's primitives plus textbook second-order theory return t_3 S_sq, "
        "the C-even hop and the leakage",
    ),
)
def _():
    # One rank is where the all-rank formulas can be tested against numbers
    # that were not derived from them. Two sources: the registry's SU(3)
    # ledger (towers, diagonals, band edges), and the replication run's
    # second-order table, computed from the corpus engine's Haar primitives
    # by a resolvent that reads no register value -- including the two
    # same-face routes, the leakage per neighbour before and after the
    # vacuum bubble, and the disjoint-pair hop in BOTH sectors.
    certificate = json.loads(
        (_REPLICATION / "chain_amplitude_certificate.json").read_text(encoding="utf-8")
    )
    table = {k: Rational(v) for k, v in certificate["second_order"].items()}
    console = (_REPLICATION / "console.log").read_text(encoding="utf-8")
    even_disjoint = re.search(r"disjoint-pair C-even hop\s*=\s*(\S+)", console)
    sigma_odd, _ = _same_face_route(3, "odd")
    sigma_even, _ = _same_face_route(3, "even")
    diag_odd, _ = _diagonal(3, "odd")
    diag_even, _ = _diagonal(3, "even")
    ell3 = _ell(3)
    engine = (
        table["single_codd_diagonal"] == sigma_odd
        and table["single_ceven_diagonal"] == sigma_even
        and table["codd_leakage_per_shared_link_neighbour"]
        == K.antiparallel_sum(3) + K.parallel_sum(3)
        and table["codd_leakage_per_disjoint_neighbour"] == -1 / _cf(3)
        and table["disjoint_pair_codd_hop"] == 0
        and even_disjoint is not None
        and Rational(even_disjoint.group(1)) == 0
        and table["shared_link_ceven_hop_coplanar"] == ell3
        and table["shared_link_ceven_hop_perpendicular"] == ell3
        and table["coplanar_shared_link_codd_hop"] == -K.hopping(3)
        and table["perpendicular_shared_link_codd_hop"] == K.hopping(3)
    )
    register = (
        sigma_odd + 1 / _cf(3) == K.band_tower("odd", 2) == Rational(1, 2)
        and sigma_even + 1 / _cf(3) == K.band_tower("even", 2) == Rational(13, 20)
        and diag_odd == K.D_MINUS_2 == K.band_assembly("odd", 2, 0)
        and diag_odd - 4 * K.hopping(3) == K.BAND_ODD_FLAT
        and diag_odd + 8 * K.hopping(3) == K.BAND_ODD_TOP
        and diag_even == K.D_PLUS_2 == K.band_assembly("even", 2, 0)
        and diag_even + 12 * ell3 == K.BAND_EVEN_BOTTOM
        and diag_even - 4 * ell3 == K.BAND_EVEN_TOP
    )
    return engine and register, (
        f"engine: same-face routes {table['single_codd_diagonal']} and "
        f"{table['single_ceven_diagonal']}, leakage per shared-link neighbour "
        f"{table['codd_leakage_per_shared_link_neighbour']} = A_3 + B_3 and per disjoint "
        f"neighbour {table['codd_leakage_per_disjoint_neighbour']} = -1/C_F, disjoint-pair hop 0 "
        "in both sectors, C-even shared-link hop -11/306 on the coplanar AND the perpendicular "
        "pair (orientation-blind, as the unsigned incidence requires), C-odd hop -+5/612 with the "
        f"signed incidence. Register: towers 1/2 and 13/20, on-site {diag_odd} and {diag_even}, "
        f"flat {K.BAND_ODD_FLAT}, A1++ at Gamma {K.BAND_EVEN_BOTTOM}, C-even top "
        f"{K.BAND_EVEN_TOP}. "
        "Every line of the all-rank ledger specialises to a number two independent sources hold"
    )


@second_order.check(
    "the charge-even second-order symbol is ell_N times the unsigned incidence: "
    "the vacuum route cancels the doubly-excited route on every link-disjoint pair",
    "PUBLICATION rev5 Prop. (vacuum-mediated route) and §6 (the symbol hypothesis); C13; G25",
    rests_on=(
        "ell_N = A_N + B_N + 1/C_F, the vacuum-mediated route at every rank",
        "the two Bloch incidence symbols, and the determinant asymmetry between them",
        "the C-even Gamma point pins t_+, exactly where no C-odd Gamma datum can",
    ),
)
def _():
    # The manuscript identifies the charge-even Bloch symbol with the
    # unsigned incidence as a HYPOTHESIS, because the vacuum-mediated route
    # <p'|V|0><0|V|p>/E_F reaches every pair of plaquettes and "taken over all
    # pairs would be a rank-one operator supported at k = 0". It is not: on a
    # link-disjoint pair the exchange route goes through the one doubly
    # excited vector sqrt2 |p,+>|p',+>, which X_{p'}|p,+> and X_p|p',+> BOTH
    # are, at energy 2E_F, and its -2/E_F cancels the vacuum route's +2/E_F
    # exactly. On an adjacent pair the four oriented monomials all carry
    # coefficient +1/2, so every channel enters with sign +1 whatever the
    # boundary orientations, and the total is A_N + B_N + 1/C_F = ell_N. The
    # symbol is therefore ell_N (N N^dagger - 4I) plus the scalar, with N the
    # unsigned incidence -- a theorem at second order, at every rank.
    e_f = _ef(_N)
    disjoint = simplify(2 / e_f + 2 / (e_f - 2 * e_f)) == 0
    # the same two routes in the odd sector vanish separately: <0|V|p,-> = 0
    # and the two exchange vectors are orthogonal
    adjacent = {}
    for s in (1, -1):
        for s_p in (1, -1):
            per_channel, total = _cross_element(_N, "even", s, s_p)
            _odd_channels, odd_total = _cross_element(_N, "odd", s, s_p)
            adjacent[(s, s_p)] = (
                simplify(total - _ell(_N)) == 0
                and all(
                    simplify(v - _channel_weights(_N)[rho]) == 0 for rho, v in per_channel.items()
                )
                and simplify(odd_total - s * s_p * K.hopping(_N)) == 0
            )
    # the even ledger that follows, at every rank
    diag_even, sigma_even = _diagonal(_N, "even")
    tower_even = simplify(sigma_even + 1 / _cf(_N))
    onsite_even = simplify(tower_even + 12 * _ell(_N))
    gamma_a1 = simplify(onsite_even + 12 * _ell(_N))
    top_even = simplify(onsite_even - 4 * _ell(_N))
    d4, s4 = _diagonal(4, "even")
    d5, _s5 = _diagonal(5, "even")
    ledger_ok = (
        simplify(diag_even - onsite_even) == 0
        and _L not in diag_even.free_symbols
        and onsite_even.subs(_N, 5) == d5 == Rational(-12395, 61152)
        and d4 == s4 + 1 / _cf(4) + 12 * _ell(4) == Rational(-4126292, 3043425)
        and simplify(gamma_a1 - onsite_even - 12 * _ell(_N)) == 0
    )
    ok = disjoint and all(adjacent.values()) and ledger_ok
    return (
        ok,
        (
            "link-disjoint pair: vacuum route 2/E_F plus doubly-excited route 2/(E_F - 2E_F) = 0 "
            "identically in N; adjacent pair: all four oriented monomials carry +1/2 in the even "
            "sector, so each channel contributes w_rho with sign +1 for every (s, s') and the "
            "total is A_N + B_N + 1/C_F = ell_N, while the same bookkeeping in the odd sector "
            "gives s s' (B_N - A_N) = s s' t_N. The even Gamma splitting A1++ - E++ = 12 ell_N "
            f"and the even bandwidth 16|ell_N| are therefore unconditional at order u^2. Ledger: "
            f"tower {factor(tower_even)}, on-site {factor(onsite_even)}; at N = 4 on-site {d4}, "
            f"at N = 5 on-site {d5} and A1++ at Gamma {gamma_a1.subs(_N, 5)}"
        ),
        {
            "TOWER_2_EVEN_N": factor(tower_even),
            "ONSITE_2_EVEN_N": factor(onsite_even),
            "GAMMA_A1PP_2_N": factor(gamma_a1),
            "TOP_2_EVEN_N": factor(top_even),
            "ONSITE_2_EVEN_4": d4,
            "GAMMA_A1PP_2_4": d4 + 12 * _ell(4),
            "TOWER_2_EVEN_5": tower_even.subs(_N, 5),
            "ONSITE_2_EVEN_5": d5,
            "GAMMA_A1PP_2_5": gamma_a1.subs(_N, 5),
        },
    )


@second_order.check(
    "the link-resolved census split is a theorem at every rank: -w_rho on the self-conjugate "
    "mixed channels, w_rho/2 on each like channel and its conjugate",
    "PUBLICATION rev5 Conj. (all-rank even split) and Reported result (the census is the "
    "Weingarten ledger); runs/two_cube_codd_o2_2026-08-29",
    rests_on=(
        "the B=6 six-channel census IS the Weingarten four-channel ledger, channel by channel",
        "the shared-link weights are Weingarten, not an isotropy assumption",
    ),
)
def _():
    # The manuscript states the even split as a conjecture and says a
    # link-resolved census at N >= 4 would test it. No census is needed: in
    # the odd cross element the like family is reached by exactly two
    # monomials, (+,+) and (-,-) when s s' = 1, each with coefficient
    # eps eps'/2 = 1/2; one puts F (x) F on the shared link and the other
    # Fbar (x) Fbar, i.e. rho and rho-bar, with the same Weingarten weight
    # d_rho/N^2 (Haar measure is conjugation invariant). The mixed channels
    # are self-conjugate and their two monomials add. So c_rho = c_rhobar =
    # w_rho/2 on the like channels and c_rho = -w_rho on the mixed ones, at
    # every rank -- the delivered N = 3 census included.
    w = _channel_weights(_N)
    resolved: dict[str, object] = {}
    for eps in (1, -1):
        for eps_p in (1, -1):
            coefficient = Rational(eps * eps_p, 2)
            s = s_p = (
                1  # the coplanar-pair convention of the census; s s' = -1 relabels rho <-> rho-bar
            )
            if eps * s == eps_p * s_p:
                # like family: the shared link carries F (x) F for eps = +1 and Fbar (x) Fbar for -1
                for rho in _LIKE:
                    key = rho if eps == 1 else rho + "Bar"
                    resolved[key] = resolved.get(key, 0) + coefficient * w[rho]
            else:
                for rho in _MIXED:
                    resolved[rho] = resolved.get(rho, 0) + coefficient * w[rho]
    generic = (
        simplify(resolved["Lam"] - w["Lam"] / 2) == 0
        and simplify(resolved["LamBar"] - w["Lam"] / 2) == 0
        and simplify(resolved["Sym"] - w["Sym"] / 2) == 0
        and simplify(resolved["SymBar"] - w["Sym"] / 2) == 0
        and simplify(resolved["1"] + w["1"]) == 0
        and simplify(resolved["Adj"] + w["Adj"]) == 0
        and simplify(sum(resolved.values()) - K.hopping(_N)) == 0
    )
    certificate = json.loads(_TWO_CUBE_CERT.read_text(encoding="utf-8"))
    delivered = {
        k.split(":")[1]: Fraction(v["rational"])
        for k, v in certificate["graph"]["channel_coefficients"].items()
    }
    at3 = {k: Fraction(int(v.subs(_N, 3).p), int(v.subs(_N, 3).q)) for k, v in resolved.items()}
    census = (
        delivered["1"] == at3["1"]
        and delivered["8"] == at3["Adj"]
        and delivered["3"] == at3["Lam"]
        and delivered["bar3"] == at3["LamBar"]
        and delivered["6"] == at3["Sym"]
        and delivered["bar6"] == at3["SymBar"]
    )
    return (
        generic and census,
        (
            "c_Lam = c_Lambar = w_Lam/2, c_Sym = c_Symbar = w_Sym/2, c_1 = -w_1, c_Adj = -w_Adj at "
            "symbolic N, summing to t_N; at N = 3 that is (1/12, -1/12, -1/12, -1/9, -1/9, 16/51), "
            "the delivered B = 6 census channel for channel. The conjecture is the orientation "
            "bookkeeping of the shared-link theorem: two like monomials at +1/2 each, one per "
            "orientation of the shared link, with conjugation-symmetric Weingarten weights"
        ),
        {"CENSUS_LAM_N": factor(resolved["Lam"]), "CENSUS_SYM_N": factor(resolved["Sym"])},
    )


@second_order.check(
    "the large-N second-order ledger: the towers and flat scalar are O(N^-3), and the leading "
    "same-face and bubble terms cancel",
    "GLUEBALL §4 (large-N expansion of t_N); PUBLICATION rev5 eq. (tsmall)",
    rests_on=(
        "the second-order on-site scalar is closed form at every rank: "
        "same-face route + 1/C_F + 12 ell_N, and L cancels",
        "large-N expansion of t_N through 1/N^9",
    ),
)
def _():
    # The same-face route is O(1/N) and so is the vacuum bubble 1/C_F, and
    # they cancel at that order in both sectors: what survives is O(N^-3),
    # the same order as the hopping. So the whole projected second-order
    # sector -- scalar and dispersion alike -- switches off as N^-3 at fixed
    # canonical u, and the flat scalar's planar coefficient is -22.
    x = Symbol("x", positive=True)  # x = 1/N
    _diag_odd, sigma_odd = _diagonal(_N, "odd")
    _diag_even, sigma_even = _diagonal(_N, "even")
    tower_odd = simplify(sigma_odd + 1 / _cf(_N))
    tower_even = simplify(sigma_even + 1 / _cf(_N))
    flat = simplify(tower_odd + 12 * _ell(_N) - 4 * K.hopping(_N))
    gamma_a1 = simplify(tower_even + 24 * _ell(_N))

    def expand(expr, order=6):
        return series(expr.subs(_N, 1 / x), x, 0, order).removeO()

    e = {
        "sigma_odd": expand(sigma_odd, 2),
        "bubble": expand(1 / _cf(_N), 2),
        "tower_odd": expand(tower_odd),
        "tower_even": expand(tower_even),
        "flat": expand(flat),
        "gamma_a1": expand(gamma_a1),
        "ell": expand(_ell(_N)),
    }
    ok = (
        e["sigma_odd"].coeff(x, 1) == -2
        and e["bubble"].coeff(x, 1) == 2
        and e["tower_odd"].coeff(x, 1) == 0
        and e["tower_odd"].coeff(x, 3) == -12
        and e["tower_even"].coeff(x, 1) == 0
        and e["tower_even"].coeff(x, 3) == -8
        and e["flat"].coeff(x, 3) == -22
        and e["ell"].coeff(x, 3) == Rational(-3, 4)
        and e["gamma_a1"].coeff(x, 3) == -26
        and limit(tower_odd, _N, oo) == 0
    )
    return ok, (
        f"1/N expansions: sigma_odd = {e['sigma_odd']}, bubble 1/C_F = {e['bubble']} -- the O(1/N) "
        f"terms cancel; tower_odd = {e['tower_odd']}; tower_even = {e['tower_even']}; "
        f"ell_N = {e['ell']}; flat scalar = {e['flat']}; A1++ at Gamma = {e['gamma_a1']}. Every "
        "second-order coefficient of the projected sector is O(N^-3) in canonical u"
    )


_TWO_CUBE_FACES = (
    ((0, 0, 0), (1, 2)),
    ((0, 0, 0), (1, 3)),
    ((0, 0, 0), (2, 3)),
    ((0, 0, 1), (1, 2)),
    ((0, 1, 0), (1, 3)),
    ((1, 0, 0), (1, 2)),
    ((1, 0, 0), (1, 3)),
    ((1, 0, 0), (2, 3)),
    ((1, 0, 1), (1, 2)),
    ((1, 1, 0), (1, 3)),
    ((2, 0, 0), (2, 3)),
)
_I_L, _I_R, _I_F = (0, 1, 2, 3, 4, 7), (5, 6, 7, 8, 9, 10), (7,)


def _face_links(x, plane):
    a, b = plane
    xa = tuple(v + (1 if k == a - 1 else 0) for k, v in enumerate(x))
    xb = tuple(v + (1 if k == b - 1 else 0) for k, v in enumerate(x))
    return {(x, a), (xa, b), (xb, a), (x, b)}


@second_order.check(
    "the two-cube B=6 connected diagonal is the per-neighbour ledger face by face: "
    "one shared-link neighbour and four disjoint faces in the other cube",
    "runs/two_cube_codd_o2_2026-08-29 certificate graph.connected_diagonal; "
    "PUBLICATION rev5 Prop. (where the truncation lives) and App. (the two-cube geometry)",
    rests_on=(
        "the second-order on-site scalar is closed form at every rank: "
        "same-face route + 1/C_F + 12 ell_N, and L cancels",
        "the connected diagonal is orbit-constant, and only the transporting orbit moves",
        "the B=6 connected kernel is (5/612) G_conn + diag, with the certified spectrum",
    ),
)
def _():
    # The manuscript treats the two-cube connected diagonal D as eleven
    # delivered numbers, "the open boundary showing up in the diagonal". It is
    # the per-neighbour ledger of the scalar theorem, counted on the prism:
    # the Möbius fold cancels the same-face route (every face is covered
    # exactly once) and leaves, for each face, the cross-cell neighbours only
    # -- A_3 + B_3 per face sharing a link, -1/C_F per link-disjoint face in
    # the other cube, whose doubly-excited state the B = 6 budget retains.
    # A side face sees one of the first and four of the second, an end cap
    # five of the second, and the shared face nothing. That is a second,
    # engine-independent confirmation of the two per-neighbour numbers at
    # N = 3: the delivery is built from Clebsch-Gordan amplitudes and folded
    # at operator level, and reads nothing of the chain-amplitude run.
    certificate = json.loads(_TWO_CUBE_CERT.read_text(encoding="utf-8"))
    delivered = [Fraction(v) for v in certificate["graph"]["connected_diagonal"]]
    shared_link = K.antiparallel_sum(3) + K.parallel_sum(3)
    disjoint = -1 / _cf(3)
    links = [_face_links(x, plane) for x, plane in _TWO_CUBE_FACES]

    def contribution(f, q):
        return shared_link if links[f] & links[q] else disjoint

    def block_sum(f, block):
        return sum((contribution(f, q) for q in block if q != f), Rational(0))

    everything = tuple(range(11))
    predicted, census = [], []
    for f in everything:
        total = block_sum(f, everything)
        if f in _I_L:
            total -= block_sum(f, _I_L)
        if f in _I_R:
            total -= block_sum(f, _I_R)
        if f in _I_F:
            total += block_sum(f, _I_F)
        predicted.append(total)
        other = (
            [q for q in everything if (q in _I_R) != (f in _I_R) or q in _I_F]
            if f not in _I_F
            else []
        )
        other = [q for q in other if q != f and q not in (_I_L if f in _I_L else _I_R)]
        census.append(
            (
                sum(1 for q in other if links[f] & links[q]),
                sum(1 for q in other if not links[f] & links[q]),
            )
        )
    same_face_cancels = all(1 - (f in _I_L) - (f in _I_R) + (f in _I_F) == 0 for f in everything)
    ok = (
        same_face_cancels
        and [Fraction(int(v.p), int(v.q)) for v in predicted] == delivered
        and census[0] == (1, 4)
        and census[2] == (0, 5)
        and census[7] == (0, 0)
        and shared_link + 4 * disjoint == Rational(-2317, 612)
        and 5 * disjoint == Rational(-15, 4)
    )
    return ok, (
        "the Möbius weights 1 - [f in L] - [f in R] + [f in F] vanish on every face, so the "
        "same-face route cancels; what is left per face is the cross-cell census: side faces "
        f"(1 shared-link, 4 disjoint) give {shared_link} + 4({disjoint}) = -2317/612, the two end "
        f"caps (0, 5) give -15/4, the shared face 0 -- the delivered D_(B=6) "
        f"{[str(v) for v in delivered]} face by face. The per-neighbour numbers A_3 + B_3 and "
        "-1/C_F are thereby confirmed by a Clebsch-Gordan lineage that shares nothing with the "
        "chain-amplitude engine"
    )


@second_order.check(
    "FINDING: revision 5 called the charge-even vacuum-route cancellation underived; "
    "the pinned corpus proves it for distant pairs at N = 3",
    "PUBLICATION rev5 Prop. (vacuum-mediated route) remark and §6 opening; PAPER Lemma "
    "(vacuum-mediated route); corpus-import/programs/one_plaquette/"
    "PAPER_FLUX_manuscript_section6_patch.tex Lemma 6.1'",
    rests_on=(
        "the charge-even second-order symbol is ell_N times the unsigned incidence: "
        "the vacuum route cancels the doubly-excited route on every link-disjoint pair",
    ),
)
def _():
    # A document contradicting its own pinned corpus, recorded rather than
    # silently corrected. Revision 5 says twice that the cancellation of the
    # charge-even all-pairs vacuum route "has not been derived" and "remains
    # a separate requirement". The flat-band manuscript it descends from --
    # and the June 2026 section-6 patch -- state the cancellation for distant
    # pairs at N = 3 in one sentence, with the two numbers +3/4 and
    # 2/(8/3 - 16/3) = -3/4. The all-rank symbol theorem in this suite is the
    # lift of that sentence to every N and to an operator identity; the
    # N = 3 mechanism is the corpus's, and the sentences are stale. Found by
    # the adversarial review of 2026-09-02 (corpus-novelty lens), which is
    # exactly the failure mode AGENTS.md names: re-deriving what exists under
    # other notation. Revision 6 cites the lemma and withdraws the sentences.
    rev5 = (ROOT / "paper" / "workhouse_publication_edition_rev5_2026-08-30.tex").read_text(
        encoding="utf-8"
    )
    stale = (
        "charge-even all-pairs term remains a separate requirement" in rev5
        and "has not been derived" in rev5
    )
    flat_band = (
        ROOT / "corpus-import" / "papers" / "flat_band" / "PAPER_FLUX_glueball_flat_band_v1_1.tex"
    ).read_text(encoding="utf-8")
    patch = (
        ROOT
        / "corpus-import"
        / "programs"
        / "one_plaquette"
        / "PAPER_FLUX_manuscript_section6_patch.tex"
    ).read_text(encoding="utf-8")
    corpus_says = (
        "exactly cancels the free two-flux channel sum $2/(8/3-16/3)=-3/4$" in flat_band
        and "recovering the vanishing of distant hops" in flat_band
        and "the two routes cancel" in patch
    )
    # and the two numbers the corpus quotes are the theorem's at N = 3
    numbers = 2 / _ef(3) == Rational(3, 4) and 2 / (_ef(3) - 2 * _ef(3)) == Rational(-3, 4)
    return stale and corpus_says and numbers, (
        "rev5 prints 'has not been derived' and 'remains a separate requirement' for the "
        "charge-even all-pairs vacuum route; the pinned flat-band manuscript's Lemma "
        "(vacuum-mediated route) and the section-6 patch's Lemma 6.1' prove the distant-pair "
        "cancellation at N = 3 with the theorem's own numbers, +3/4 against 2/(8/3-16/3) = -3/4. "
        "The all-rank symbol statement is new; the N = 3 mechanism is the corpus's, and the two "
        "sentences are stale against it"
    )
