"""Re-derivation of the corpus's exact claims from their stated definitions.

Each check answers one question: *does this printed number follow from the
definition the corpus gives for it?* A check that fails is not automatically a
physics error — it is usually a transcription slip, a normalization erratum, or
a presentation difference. It is always worth knowing about.

Checks never adjudicate the fourth-order dispute. They verify the arithmetic
each side reports, and the exact size of the disagreement between them.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from itertools import product
from pathlib import Path

from sympy import (
    I,
    Integer,
    Matrix,
    Rational,
    cos,
    diff,
    exp,
    expand,
    eye,
    limit,
    nsimplify,
    numer,
    oo,
    pi,
    series,
    simplify,
    sin,
    solve,
    sqrt,
    symbols,
    sympify,
    together,
    zeros,
)

from . import cellular as CELL
from . import constants as K
from . import near_gamma as G
from . import payloads as P
from . import settlement as S
from . import tier_collapse as T
from . import torus as TOR
from . import triage as TRIAGE


@dataclass
class Result:
    """Outcome of one invariant check."""

    name: str
    passed: bool
    detail: str = ""
    section: str = ""
    #: T1 = re-derived exactly; T2 = float agreement within a stated tolerance.
    tier: int = 1
    #: Line of the check's body, so a reader can go argue with the source.
    line: int = 0


@dataclass
class Suite:
    """A named group of checks."""

    name: str
    checks: list[tuple[str, str, int, Callable[[], tuple[bool, str]]]] = field(default_factory=list)

    def check(self, name: str, section: str = "", tier: int = 1):
        """Register a check.

        ``tier`` is the verification tier the check establishes, and it is
        declared rather than inferred because the difference is the whole point:
        T1 is exact re-derivation, T2 is float agreement within a tolerance. A
        check that compares against a ``*_NUM`` constant or a stated tolerance
        is T2 however exact its inputs look.
        """
        if tier not in (1, 2):
            raise ValueError(f"{name}: a check establishes T1 or T2, not T{tier}")

        def register(fn):
            self.checks.append((name, section, tier, fn))
            return fn

        return register

    def run(self, names: set[str] | None = None) -> list[Result]:
        """Run the checks, or just the named subset.

        ``names`` exists so ``verify --only`` can keep its promise of one
        claim in about a second — filtering after a full run cannot.
        """
        out = []
        for name, section, tier, fn in self.checks:
            if names is not None and name not in names:
                continue
            try:
                passed, detail = fn()
            except Exception as exc:  # a broken check is a failure
                passed, detail = False, f"raised {type(exc).__name__}: {exc}"
            out.append(Result(name, passed, detail, section, tier, fn.__code__.co_firstlineno))
        return out


SUITES: list[Suite] = []


def _suite(name: str) -> Suite:
    s = Suite(name)
    SUITES.append(s)
    return s


# ==========================================================================
rank_law = _suite("second order, all ranks")


@rank_law.check("t_N = B_N - A_N", "MASTER_THEORY §4.3")
def _():
    lhs = K.parallel_sum() - K.antiparallel_sum()
    return simplify(lhs - K.hopping()) == 0, "channel difference reproduces the rank law"


@rank_law.check("t_2 = 0 and t_3 = 5/612", "MASTER_THEORY §4.3")
def _():
    ok = K.hopping(2) == 0 and K.hopping(3) == Rational(5, 612)
    return ok, f"t_2={K.hopping(2)}, t_3={K.hopping(3)}"


@rank_law.check("t_N > 0 for N >= 3", "MASTER_THEORY §4.3")
def _():
    bad = [n for n in range(3, 40) if not K.hopping(n) > 0]
    return not bad, "positive for N=3..39" if not bad else f"non-positive at {bad}"


@rank_law.check("deficit identity 1/4 - N^3 t_N", "MASTER_THEORY §4.3")
def _():
    lhs = Rational(1, 4) - K.N**3 * K.hopping()
    return simplify(lhs - K.hopping_deficit()) == 0, "closed form matches"


@rank_law.check("deficit positive at N = 3, 5, 9", "MASTER_THEORY §4.3")
def _():
    vals = {n: K.hopping_deficit(n) for n in (3, 5, 9)}
    return all(v > 0 for v in vals.values()), f"{ {k: str(v) for k, v in vals.items()} }"


@rank_law.check("large-N expansion of t_N through 1/N^9", "GLUEBALL §4")
def _():
    inv = symbols("inv", positive=True)
    ser = series(K.hopping(1 / inv), inv, 0, 10).removeO()
    got = {k: ser.coeff(inv, k) for k in K.HOPPING_LARGE_N}
    return got == K.HOPPING_LARGE_N, f"{ {k: str(v) for k, v in got.items()} }"


@rank_law.check("N^3 t_N increases monotonically to 1/4", "CANON §10.2/§10.5")
def _():
    num = simplify(numer(together(diff(K.N**3 * K.hopping(), K.N))))
    cubic_in_N = K.MONOTONICITY_CUBIC.subs(K.x, K.N**2)
    # sympy cancels one power of x that the corpus leaves in the printed prefactor;
    # the sign-determining cubic is what must agree.
    matches = simplify(num - 4 * K.N**3 * cubic_in_N) == 0
    positive = all(K.MONOTONICITY_CUBIC.subs(K.x, v) > 0 for v in (4, 9, 16, 10**6))
    roots = [complex(r).real for r in solve(K.MONOTONICITY_CUBIC, K.x)]
    return (
        matches and positive,
        f"d/dN numerator = 4N^3*cubic(N^2); cubic roots {[round(r, 4) for r in roots]} "
        f"all < 4, so cubic > 0 on the physical range",
    )


# ==========================================================================
@rank_law.check(
    "the four channel weights follow from dimension and Casimir",
    "PAPER_FLATBAND eq. (18)-(19), App. A",
)
def _():
    bad = [
        c for c in K.CHANNELS if simplify(K.channel_weight(c) - K.channel_weight_printed(c)) != 0
    ]
    at3 = {c: K.channel_weight(c, 3) for c in K.CHANNELS}
    return not bad, (
        "w_R = -(d_R/N^2)/(C_F + C_R/2) reproduces all four printed closed forms as identities "
        f"in N; at N = 3 they are {at3}"
    )


@rank_law.check(
    "each channel gap is C_F + C_R/2, and the weights sum to one", "PAPER_FLATBAND eq. (4), (18)"
)
def _():
    # The energy bookkeeping the weight rests on: six nonshared half-links at
    # 3 C_F, the fused link at C_R/2, against an external one-plaquette state
    # at 2 C_F. And the numerator weights are a probability distribution per
    # family -- which is what makes "isotropy" a normalization rather than a
    # free constant. That premise itself is NOT derived here; it is the one
    # unproved physical input of the whole second-order chain.
    gaps = all(
        simplify(K.channel_gap(c) - (K.casimir_fundamental() + K.channel_data()[c][1] / 2)) == 0
        for c in K.CHANNELS
    )
    families = {}
    for fam in ("mixed", "like"):
        members = [c for c in K.CHANNELS if K.CHANNEL_FAMILY[c] == fam]
        families[fam] = simplify(sum(K.channel_data()[c][0] for c in members) / K.N**2)
    energy = simplify(K.plaquette_energy() - (K.N**2 - 1) / K.N) == 0
    return gaps and set(families.values()) == {1} and energy, (
        f"gaps are C_F + C_R/2 for all four channels; sum of d_R/N^2 is {families} per family, "
        "exactly 1; and the external energy is 2 C_F = (N^2-1)/N, which is 8/3 at N = 3. The "
        "isotropy premise that makes d_R/N^2 the numerator is asserted by the corpus, not derived"
    )


@rank_law.check(
    "the shared-link weights are Weingarten, not an isotropy assumption",
    "PAPER_FLATBAND eq. (18) / G24",
)
def _():
    # The one sentence the whole second-order chain rested on: "Isotropy of the
    # normalized shared-link tensor assigns squared norm d_R/N^2 to the channel
    # projector." It is not an assumption. It follows from the order-2
    # Weingarten values in two steps.
    #
    # The six nonshared links collapse first: each plaquette contributes a
    # product of three independent Haar links, and a product of independent
    # Haar matrices is Haar, so the amplitude is Tr(A U) Tr(B U^(+-1)) with A
    # and B independent Haar. What survives is a pure degree-(2,2) moment of
    # the shared link, and two of those settle both families.
    #
    # This is the check G24 asked for. It imports nothing from the corpus: the
    # Weingarten pair is the inverse of the S_2 Gram matrix and the index sums
    # are explicit, which is why agreement here moves the manuscript's central
    # input from asserted to derived.
    rows, ok = {}, True
    for rank in (3, 4, 5):
        derived = CELL.shared_link_weights(rank)
        for channel, weight in derived.items():
            claimed = Rational(K.channel_data(rank)[channel][0]) / rank**2
            ok = ok and Rational(weight.numerator, weight.denominator) == claimed
        rows[rank] = tuple(str(m) for m in CELL.shared_link_moments(rank))
    return ok, (
        f"(M_direct, M_cross) = {rows}, i.e. (N^2, N) at every rank, so the like family "
        "splits as (N+1)/(2N) and (N-1)/(2N) and the mixed family's singlet weight is 1/N^2 -- "
        "all four exactly d_R/N^2, from the S_2 Gram inverse and explicit index sums. The "
        "manuscript asserts this in one word; nothing in the corpus derived it"
    )


@rank_law.check(
    "A_N and B_N are the channel sums, not transcriptions", "PAPER_FLATBAND eq. (20)-(21)"
)
def _():
    mixed = K.channel_weight("1") + K.channel_weight("Adj")
    like = K.channel_weight("Lambda2") + K.channel_weight("Sym2")
    ok = simplify(mixed - K.antiparallel_sum()) == 0 and simplify(like - K.parallel_sum()) == 0
    return ok, (
        "A_N = w_1 + w_Adj over F (x) Fbar and B_N = w_L2 + w_S2 over F (x) F, so the registered "
        f"closed forms follow from (d_R, C_R); at N = 3, A = {K.antiparallel_sum(3)}, "
        f"B = {K.parallel_sum(3)}"
    )


@rank_law.check(
    "ell_N = A_N + B_N + 1/C_F, the vacuum-mediated route at every rank",
    "03-prism-selection-shape ~93 / C13",
)
def _():
    # The corpus prints the all-rank C-even hopping and gates it inside
    # NB_O2_prism_square_second_order_falsification.ipynb as
    # factor(Wmix + Wlike + 1/CF). Nothing here checked it.
    #
    # It earns registration because of what the 1/C_F term is. C13 records
    # -481/612 as superseded by -11/306 "because the vacuum-mediated route was
    # omitted" -- and A_3 + B_3 is EXACTLY -481/612, with 1/C_F(3) = 3/4 the
    # omitted route. A one-rank ledger note becomes a formula. The C-odd
    # difference B_N - A_N never sees the route at all, because <0|V|p,-> = 0
    # by charge conjugation: that is why t_N carries no such term, and it is
    # the clause the manuscript's Theorem 3 proof leaves unstated.
    identity = (
        simplify(
            K.antiparallel_sum() + K.parallel_sum() + 1 / K.casimir_fundamental() - K.even_hopping()
        )
        == 0
    )
    superseded = K.antiparallel_sum(3) + K.parallel_sum(3)
    return identity and superseded == Rational(-481, 612) and K.even_hopping(3) == K.T_PLUS_2, (
        f"identity in N; at N = 3, A_3 + B_3 = {superseded} (C13's superseded value) plus "
        f"1/C_F = {1 / K.casimir_fundamental(3)} gives {K.even_hopping(3)} = T_PLUS_2"
    )


# ==========================================================================
su3_series = _suite("SU(3) second and third order")


@su3_series.check("d_- - 4 t_- = 11/306", "PAPER eq. (7)")
def _():
    v = K.D_MINUS_2 - 4 * K.T_MINUS_2
    return v == Rational(11, 306), f"= {v}"


@su3_series.check("t_- equals the rank law at N = 3", "MASTER_THEORY §4.3")
def _():
    return K.hopping(3) == K.T_MINUS_2, f"{K.T_MINUS_2} == {K.hopping(3)}"


@su3_series.check("C-even bandwidth = top - bottom = 88/153", "PAPER App. B")
def _():
    w = K.BAND_EVEN_TOP - K.BAND_EVEN_BOTTOM
    return w == K.BAND_EVEN_WIDTH, f"= {w}"


@su3_series.check("C-odd manifold width = 5/51", "PAPER App. B")
def _():
    w = K.BAND_ODD_TOP - K.BAND_ODD_FLAT
    return w == K.BAND_ODD_WIDTH, f"= {w}"


@su3_series.check("d_3 = 7/32 + 12*leak_3 - 4*b_3", "MASTER_THEORY §4.4")
def _():
    v = Rational(7, 32) + 12 * K.LEAK_3 - 4 * K.B_3
    return v == K.D_3, f"= {v}"


@su3_series.check("E_flat and t(u) carry the ledger coefficients", "MASTER_THEORY §4.4")
def _():
    e, t = K.e_flat(), K.t_series()
    ok = (
        e.coeff(K.u, 0) == Rational(8, 3)
        and e.coeff(K.u, 1) == 1
        and e.coeff(K.u, 2) == Rational(11, 306)
        and e.coeff(K.u, 3) == K.D_3
        and t.coeff(K.u, 2) == K.T_MINUS_2
        and t.coeff(K.u, 3) == K.B_3
    )
    return ok, "E_flat = 8/3 + u + 11/306 u^2 - 109151/249696 u^3"


# ==========================================================================
@su3_series.check("d_- = 1/2 + 12*leak_2, and leak_2 = -11/306", "PAPER_FLATBAND eq. (28)")
def _():
    # The second-order assembly: the within-plaquette tower's u^2 term, plus
    # twelve neighbours' leakage, is the C-odd diagonal; the -4 t_- shift then
    # produces the flat scalar. Recorded with what it collides with, not with
    # an explanation of it: leak_2 = T_PLUS_2 = ell_3 = -11/306, three labels
    # on one rational, and nothing here shows they are one object.
    diagonal = Rational(1, 2) + 12 * K.LEAK_2
    flat = diagonal - 4 * K.T_MINUS_2
    return diagonal == K.D_MINUS_2 and flat == K.BAND_ODD_FLAT, (
        f"1/2 + 12*({K.LEAK_2}) = {diagonal} = d_-, and d_- - 4 t_- = {flat} = the flat scalar. "
        f"leak_2 equals T_PLUS_2 = {K.T_PLUS_2} (the C-even hopping) and equals -(flat scalar); "
        "the collision is equivalent to 13*(11/306) = 1/2 - 4 t_-, which is arithmetic"
    )


@su3_series.check(
    "leak_3 is assembled from the domino diagonal and the vacuum piece",
    "corpus-import/numerics/results/CERT_FLUX_d3_certificate_results.md",
)
def _():
    assembled = (K.D3_ODD - K.E_VAC3_DOMINO) - Rational(7, 32)
    return assembled == K.LEAK_3, (
        f"({K.D3_ODD} - ({K.E_VAC3_DOMINO})) - 7/32 = {assembled} = leak_3; the vacuum piece is "
        "-9/16 = 2*(-9/32), the certificate's 'no connected third-order vacuum piece'. leak_3 was "
        "registered as a bare number; this is where it comes from"
    )


@su3_series.check(
    "one assembly formula gives every registered band value",
    "corpus-import/numerics/results/CERT_FLUX_d3_certificate_results.md / PAPER App. B",
)
def _():
    # E_s(lambda, r) = tower_{r,s} + 12 leak_{r,s} + lambda t_{r,s}, with
    # lambda the adjacency eigenvalue. Eight independently registered
    # rationals, and the tower term is the certified coupling conversion
    # 4*Delta(3u/2), so nothing unregistered enters. What this joins: the
    # C-odd third-order assembly was one instance of a formula with four more;
    # the C-even band values were checked only by subtracting one from
    # another; and the coupling erratum and the band ledger were unconnected
    # parts of this repository. They are the same statement.
    expected = {
        ("odd", 2, -4): K.BAND_ODD_FLAT,
        ("odd", 2, 8): K.BAND_ODD_TOP,
        ("odd", 3, -4): K.D_3,
        ("odd", 3, 8): K.D_3_TOP,
        ("even", 2, 12): K.BAND_EVEN_BOTTOM,
        ("even", 2, -4): K.BAND_EVEN_TOP,
        ("even", 3, 12): K.M3_EVEN_K0,
        ("even", 3, -4): K.M3_EVEN_BANDMIN,
    }
    bad = {k: K.band_assembly(*k) for k in expected if K.band_assembly(*k) != expected[k]}
    towers = {
        (sector, order): K.band_tower(sector, order)
        for sector in ("odd", "even")
        for order in (2, 3)
    }
    return not bad, (
        f"8/8 exact across both charge sectors and both orders; recovered towers {towers}"
        + (f"; MISMATCH {bad}" if bad else "")
    )


@su3_series.check(
    "FINDING: no Gamma-point datum can constrain the hopping", "PAPER_FLATBAND Table 1 / HAMER_1989"
)
def _():
    # tau(u) enters the spectrum only as tau(u) q(k), and q(0) = 0, so every
    # rest-frame series -- E_flat, Hamer's 1+- table, the whole Gamma-point
    # comparison -- is blind to the hopping. A one-parameter family moves both
    # third-order coefficients and leaves d_3, hence the Hamer agreement,
    # exactly invariant. The band top is what separates them, at lambda = 8.
    #
    # Recorded so that the Hamer agreement -- which is real, and which the
    # published-comparisons suite measures -- is never read as validating the
    # dispersive half. It does not weaken b_3, which the abstract-domino
    # engine computes directly.
    eps = symbols("epsilon")
    shifted = Rational(7, 32) + 12 * (K.LEAK_3 + eps / 3) - 4 * (K.B_3 + eps)
    invariant = simplify(shifted - K.D_3) == 0
    q_at_gamma = 4 * sum(sin(0 / 2) ** 2 for _ in range(3))
    separated = (K.D_3_TOP - K.D_3) / 12 == K.B_3
    return invariant and q_at_gamma == 0 and separated, (
        "q(0) = 0, so the Gamma-point spectrum is E_flat with multiplicity 3 and carries no "
        "trace of tau; (b_3 + e, leak_3 + e/3) leaves d_3 identically unchanged, so Hamer pins "
        f"12 leak_3 - 4 b_3 = {12 * K.LEAK_3 - 4 * K.B_3} and neither coefficient alone. The "
        f"lambda = 8 band top separates them: (d_3^top - d_3)/12 = {(K.D_3_TOP - K.D_3) / 12} = b_3"
    )


# ==========================================================================
sealed = _suite("fourth order, sealed core")


@sealed.check("alpha_3 = 4*A_shp = 5/12", "MASTER_THEORY §5.2")
def _():
    ok = K.alpha_pen(3) == 4 * K.A_SHP_3 == K.ALPHA_PEN_3
    return ok, f"alpha_3 = {K.alpha_pen(3)}"


@sealed.check("axial law reproduces alpha_4, alpha_5, alpha_6", "MASTER_THEORY §5.3")
def _():
    want = {4: Rational(32, 675), 5: Rational(1, 108), 6: Rational(64, 25725)}
    got = {n: K.alpha_pen(n) for n in want}
    return got == want, f"{ {k: str(v) for k, v in got.items()} }"


@sealed.check("alpha_3 = 4*|c_4^square(3)|", "MOB §4")
def _():
    # Exact: both sides are Rational. A second, independent route to alpha_3 --
    # the cube-completion coefficient rather than the shape coefficient A.
    route = 4 * abs(K.CUBE_COMPLETION_4)
    return route == K.ALPHA_PEN_3, (
        f"4*|c_4^square(3)| = 4*|{K.CUBE_COMPLETION_4}| = {route} = alpha_3, the "
        f"same value the shape route gives as 4*A_shp = 4*{K.A_SHP_3}"
    )


def _sealed_gaps():
    return {
        "A": abs(K.A_SHP_3_NUM - float(K.A_SHP_3)),
        "B": abs(K.B_SHP_3_NUM - float(K.B_SHP_3)),
        "D": abs(K.D_SHP_3_NUM - float(K.D_SHP_3)),
        "alpha": abs(K.ALPHA_PEN_3_NUM - float(K.ALPHA_PEN_3)),
    }


@sealed.check("v10a.26 A, B, D match the sealed rationals within 2.3e-13", "GLUEBALL §10", tier=2)
def _():
    gaps = _sealed_gaps()
    subset = {k: gaps[k] for k in ("A", "B", "D")}
    ok = all(g <= K.SEALED_CORE_TOLERANCE for g in subset.values())
    return ok, "; ".join(f"{k} {v:.3e}" for k, v in subset.items())


@sealed.check(
    "FINDING: alpha_new falls outside the corpus's own 2.3e-13 bound",
    "GLUEBALL §10",
    tier=2,
)
def _():
    gaps = _sealed_gaps()
    # alpha = 4A, so it inherits four times A's deviation. The corpus's stated
    # aggregate bound (2.3e-13) tracks D_new (2.23e-13) and does not cover alpha.
    # This is a bookkeeping slip in the quoted tolerance, not a discrepancy in
    # the sealed core itself: the run's own alpha and A stay mutually consistent.
    exceeds = gaps["alpha"] > K.SEALED_CORE_TOLERANCE
    consistent = abs(K.ALPHA_PEN_3_NUM - 4 * K.A_SHP_3_NUM) < 1e-14
    return exceeds and consistent, (
        f"alpha gap {gaps['alpha']:.4e} > stated {K.SEALED_CORE_TOLERANCE:.1e} "
        f"(= 4x the A gap {gaps['A']:.4e}); alpha_new vs 4*A_new agree to "
        f"{abs(K.ALPHA_PEN_3_NUM - 4 * K.A_SHP_3_NUM):.1e}, so the sealed core holds "
        "and only the quoted bound is too tight"
    )


@sealed.check("exceptional ranks are exactly {3,4,5,6}", "MASTER_THEORY §5.3")
def _():
    # A fourth-order word carries at most 6 character factors, so a determinant
    # channel needs |p-q| = N <= 6; and N >= 3 for the sector to exist at all.
    derived = tuple(n for n in range(2, 12) if 3 <= n <= 6)
    return derived == K.EXCEPTIONAL_RANKS, f"{derived}"


# ==========================================================================
dispute = _suite("fourth order, anchoring and the residual dispute")


@dispute.check("historical q_3 decimal expansion", "MASTER_THEORY §5.5", tier=2)
def _():
    d = abs(float(K.Q_BAND_4) - (-2.857915988114559))
    return d < 1e-15, f"|diff| = {d:.2e}"


@dispute.check("C_old = (beta_pen_3 - 2*alpha_3)/16", "MASTER_THEORY §5.5")
def _():
    v = (K.BETA_PEN_3 - 2 * K.ALPHA_PEN_3) / 16
    return v == K.C_SHP_HISTORICAL, f"= {v}"


@dispute.check("Delta_Gamma = m_Gamma^(4) - q_band^(4)", "MASTER_THEORY §5.5 / C1", tier=2)
def _():
    v = K.M_GAMMA_4_NUM - float(K.Q_BAND_4)
    # Double-precision evaluation lands one ulp below the correctly rounded
    # value; both are recorded, so accept either.
    ok = min(abs(v - K.DELTA_GAMMA_NUM), abs(v - K.DELTA_GAMMA_AS_PRINTED_NUM)) < 1e-15
    return ok, f"double eval {v!r}; exact rounds to {K.DELTA_GAMMA_NUM!r}"


@dispute.check("FINDING: the printed Delta_Gamma is one ulp low", "MASTER_THEORY §5.5", tier=2)
def _():
    from . import rigor

    # Certified enclosure (ADR 0010): the double M_GAMMA_4_NUM enters exactly,
    # the rational q_band^(4) enters as a 128-bit ball, and the comparisons
    # below are True only if provable from disjoint enclosures — this replaces
    # the earlier "evalf(25) is surely enough" with a machine guarantee.
    exact = rigor.ball(K.M_GAMMA_4_NUM) - rigor.ball(K.Q_BAND_4)
    printed_low = rigor.certified_lt(rigor.ball(K.DELTA_GAMMA_AS_PRINTED_NUM), exact)
    recorded_closer = rigor.certified_closer(
        exact, rigor.ball(K.DELTA_GAMMA_NUM), rigor.ball(K.DELTA_GAMMA_AS_PRINTED_NUM)
    )
    gap = K.DELTA_GAMMA_NUM - K.DELTA_GAMMA_AS_PRINTED_NUM
    return printed_low and recorded_closer, (
        f"certified: true Delta_Gamma = {rigor.describe(exact)}; the corpus's printed "
        f"{K.DELTA_GAMMA_AS_PRINTED_NUM!r} lies provably below it, and "
        f"{K.DELTA_GAMMA_NUM!r} is provably the closer double (gap {gap:.3e} = 1 ulp). "
        "Cosmetic, but the printed digit is not the correctly rounded one."
    )


@dispute.check(
    "a translation-local scalar shift changes nothing observable",
    "MASTER_THEORY §5.5 / C1",
)
def _():
    # H_mass = H_band + Delta_Gamma*I  =>  centered forms coincide identically.
    h = Matrix(3, 3, symbols("h1:10"))
    dg, q = symbols("dg q")
    centered_mass = (h + dg * eye(3)) - (q + dg) * eye(3)
    centered_band = h - q * eye(3)
    same = simplify(centered_mass - centered_band) == zeros(3, 3)
    return same, (
        "centered operator, eigenvectors, SOS factorization, mobility "
        "coefficients and bandwidth are all invariant under the anchoring shift, "
        "so q_band^(4) and m_Gamma^(4) are not competing estimates"
    )


@dispute.check(
    "Delta_C = C_new - C_old > 0 (the real discrepancy)",
    "MASTER_THEORY §5.5 / C2",
    tier=2,
)
def _():
    v = K.C_SHP_NEW_NUM - float(K.C_SHP_HISTORICAL)
    d = abs(v - K.DELTA_C_NUM)
    return d < 1e-16 and v > 0, f"{v!r} vs recorded {K.DELTA_C_NUM!r} (|diff| {d:.1e})"


@dispute.check("beta_new = 8A + 16*C_new", "MASTER_THEORY §5.5", tier=2)
def _():
    v = 8 * float(K.A_SHP_3) + 16 * K.C_SHP_NEW_NUM
    return abs(v - K.BETA_PEN_NEW_NUM) < 1e-15, f"= {v!r}"


@dispute.check("off-axis band splits are 8*Delta_C and 16*Delta_C", "MASTER_THEORY §5.5", tier=2)
def _():
    m, r = 8 * K.DELTA_C_NUM, 16 * K.DELTA_C_NUM
    ok = abs(m - K.M_SPLIT_RECORDED_NUM) < 1e-15 and abs(r - K.R_SPLIT_RECORDED_NUM) < 1e-15
    return ok, f"M: {m!r}, R: {r!r}; axial cuts agree exactly"


@dispute.check("bandwidth ratio W4_new / W4_old ~ 1.93", "MASTER_THEORY §5.5", tier=2)
def _():
    ratio = K.W4_NEW_NUM / K.W4_HISTORICAL_NUM
    return abs(ratio - 1.93) < 5e-3, f"= {ratio:.6f}"


@dispute.check("Hamer 8*a_4 matches m_Gamma to ~5.2e-13", "GLUEBALL §2.3", tier=2)
def _():
    d = abs(8 * K.HAMER_A4_NUM - K.M_GAMMA_4_NUM)
    return d < K.HAMER_TOLERANCE, (
        f"|diff| = {d:.2e}; a_4 is an unverified notebook transcription, "
        "so this is a normalization cross-check, not primary-source proof"
    )


@dispute.check("quarantined scalar decimal", "MASTER_THEORY §5.5", tier=2)
def _():
    d = abs(float(K.QUARANTINED_SCALAR) - (-11.068479463778765))
    return d < 1e-14, f"|diff| = {d:.2e}; rejected by both sides"


@dispute.check("C20: exact gate value vs printed float-reconstruction", "MASTER_THEORY C20", tier=2)
def _():
    exact = float(K.LINKED_VACUUM_4)
    artifact = float(K.LINKED_VACUUM_4_ARTIFACT)
    gap = abs(exact - artifact)
    ulp = 2.0**-53 * abs(exact)
    # C20 records these as agreeing "to float precision". They do not: the gap is
    # ~31 ulps, and the decimal printed throughout the corpus (-0.8800987156226097)
    # is the artifact's value, not the exact gate value (-0.8800987156226127).
    agree_to_float = gap <= 2 * ulp
    return (
        not agree_to_float,
        f"exact {exact!r} vs artifact {artifact!r}; gap {gap:.2e} = {gap / ulp:.0f} ulps. "
        f"They agree to ~14 significant digits, NOT to float precision as C20 states; "
        f"the corpus's printed decimal tracks the artifact.",
    )


@dispute.check("run's applied shift is not Delta_Gamma", "GLUEBALL §9.2 / C22", tier=2)
def _():
    # Gate 85's equality was produced by construction with this shift, so it
    # certifies internal bookkeeping rather than independent agreement.
    return (
        abs(K.RUN15_APPLIED_SHIFT_NUM - K.DELTA_GAMMA_NUM) > 1.0,
        f"applied {K.RUN15_APPLIED_SHIFT_NUM} vs Delta_Gamma {K.DELTA_GAMMA_NUM} "
        "— target-derived, so gate 85 is not an independent scalar verification",
    )


# ==========================================================================
crosswalk = _suite("old-to-new crosswalk")


@crosswalk.check("Phi_C vanishes at Gamma along every direction", "MASTER_THEORY §5.5")
def _():
    t, n1, n2, n3 = symbols("t n1 n2 n3", positive=True)
    radial = K.phi_c((t * n1, t * n2, t * n3))
    lead = simplify(series(radial, t, 0, 4).removeO())
    vanishes = limit(radial, t, 0) == 0
    return vanishes, (
        f"Phi_C = {lead} = O(|k|^2), since e_2 = O(|k|^4) and Q = O(|k|^2). "
        "A Gamma-point scalar therefore constrains Delta_Gamma but places no "
        "constraint whatsoever on Delta_C."
    )


@crosswalk.check("Phi_C at the high-symmetry points", "MASTER_THEORY §5.1")
def _():
    got = {
        "X": K.phi_c((pi, 0, 0)),
        "M": K.phi_c((pi, pi, 0)),
        "P": K.phi_c((pi, pi / 2, 0)),
        "R": K.phi_c((pi, pi, pi)),
    }
    want = {"X": 0, "M": 8, "P": Rational(16, 3), "R": 16}
    return got == want, f"{ {k: str(v) for k, v in got.items()} }"


@crosswalk.check(
    "crosswalk reproduces the recorded off-axis band splits",
    "MASTER_THEORY §5.5",
    tier=2,
)
def _():
    # c_4_new(k) - c_4_old(k) - Delta_Gamma == Delta_C * Phi_C(k)
    m = K.DELTA_C_NUM * float(K.phi_c((pi, pi, 0)))
    r = K.DELTA_C_NUM * float(K.phi_c((pi, pi, pi)))
    ok = abs(m - K.M_SPLIT_RECORDED_NUM) < 1e-15 and abs(r - K.R_SPLIT_RECORDED_NUM) < 1e-15
    return ok, f"M -> {m!r}, R -> {r!r}; independently recorded as 8*Delta_C and 16*Delta_C"


@crosswalk.check("the crosswalk is exactly scalar on the momentum axes", "MASTER_THEORY §5.5")
def _():
    axial = [K.phi_c(kv) for kv in ((pi, 0, 0), (pi / 2, 0, 0), (pi / 3, 0, 0))]
    return all(a == 0 for a in axial), (
        "Phi_C vanishes on every axial cut, so axial data cannot distinguish the "
        "two kernels — the whole residual disagreement lives off-axis"
    )


@crosswalk.check("bandwidth is preserved only if Delta_C vanishes", "MASTER_THEORY §5.5", tier=2)
def _():
    # The scalar term drops out of any difference of band values; only Phi_C survives.
    spread = K.DELTA_C_NUM * (float(K.phi_c((pi, pi, pi))) - float(K.phi_c((pi, 0, 0))))
    return abs(spread) > 1e-3, (
        f"scalar re-anchoring alone leaves the centered structure unchanged, but the "
        f"additional Delta_C*Phi_C term spreads R against X by {spread:.6f}. Bandwidth "
        "survives the crosswalk only if Delta_C is shown to vanish or is absorbed by an "
        "exact operator identity; neither is established."
    )


# ==========================================================================
pencil = _suite("fourth-order generalized Hodge pencil")


@pencil.check("Q4 cross coefficient = beta_pen_3 / 4", "GLUEBALL §8")
def _():
    return K.Q4_CROSS == K.BETA_PEN_3 / 4, f"= {K.Q4_CROSS}"


@pencil.check("historical Q4 numerator is positive definite", "UNIFIED §0.1")
def _():
    m = Matrix(3, 3, lambda i, j: K.A_SHP_3 if i == j else K.Q4_CROSS / 2)
    eig = m.eigenvals()
    ok = all(e > 0 for e in eig) and set(eig) == {
        K.A_SHP_3 + K.Q4_CROSS,
        K.A_SHP_3 - K.Q4_CROSS / 2,
    }
    return ok, f"eigenvalues {sorted(str(e) for e in eig)} — PSD, in fact PD"


@pencil.check("centered kernel difference is PSD (vanishes on axes)", "MASTER_THEORY §5.5", tier=2)
def _():
    # C^dagger[(H4_new - s_new) - (H4_old - q_old)]C = 4*Delta_C*sum_{i<j} L_i L_j.
    # The eigenstructure is exact algebra on a symbolic Delta_C — the matrix
    # 2d(J - I) has eigenvalues 4d, -2d, -2d — and only the SIGN of Delta_C
    # is a float fact, because C_new exists only as the v10a.26 float. That
    # sign is the whole verdict, so the check is T2, not T1.
    d = symbols("d", positive=True)
    m = Matrix(3, 3, lambda i, j: 0 if i == j else 2 * d)
    eig = {simplify(e): mult for e, mult in m.eigenvals().items()}
    structure_ok = eig == {4 * d: 1, -2 * d: 2}
    return structure_ok and K.DELTA_C_NUM > 0, (
        f"form eigenvalues exactly {{4d: 1, -2d: 2}} for symbolic d; with Delta_C = "
        f"{K.DELTA_C_NUM:.6e} > 0 (float — C_new exists only as v10a.26 output) the form is "
        "indefinite as a free quadratic form, PSD on the cube-amplitude sector where "
        "the pencil is scoped"
    )


# ==========================================================================
extraction = _suite("fourth-order checkpoint extraction")

_As, _Bs, _Cs, _Ds, _c0 = symbols("A_shp B_shp C_shp D_shp c0")


def _eps4(k):
    """Generic cubic-invariant fourth-order correction on the flat fiber."""
    q, e2, e3 = K.cubic_invariants(k)
    return simplify(_c0 + _As * q + _Bs * e2 + _Cs * 4 * e2 / q + _Ds * e3 / q)


def _deltas():
    g = _c0  # epsilon_4(Gamma) = c0
    return (
        simplify(_eps4([pi, 0, 0]) - g),
        simplify(_eps4([pi, pi, 0]) - g),
        simplify(_eps4([pi, pi / 2, 0]) - g),
        simplify(_eps4([pi, pi, pi]) - g),
    )


@extraction.check("checkpoint values at X, M, P, R", "MASTER_THEORY §5.1")
def _():
    dX, dM, dP, dR = _deltas()
    ok = (
        simplify(dX - 4 * _As) == 0
        and simplify(dM - (8 * _As + 16 * _Bs + 8 * _Cs)) == 0
        and simplify(dP - (6 * _As + 8 * _Bs + Rational(16, 3) * _Cs)) == 0
        and simplify(dR - (12 * _As + 48 * _Bs + 16 * _Cs + Rational(16, 3) * _Ds)) == 0
    )
    return ok, f"dX={dX}, dM={dM}, dP={dP}, dR={dR}"


@extraction.check("the four extraction formulas invert the ansatz", "MASTER_THEORY §5.1")
def _():
    dX, dM, dP, dR = _deltas()
    ok = (
        simplify(dX / 4 - _As) == 0
        and simplify((dX + 4 * dM - 6 * dP) / 16 - _Bs) == 0
        and simplify(3 * (2 * dP - dM - dX) / 8 - _Cs) == 0
        and simplify(3 * (dR - 6 * dM + 6 * dP) / 16 - _Ds) == 0
    )
    return ok, "A, B, C, D each recovered exactly from the checkpoint deltas"


@extraction.check("X is blind to B, C, D — it fixes A alone", "MASTER_THEORY §5.1")
def _():
    dX, *_ = _deltas()
    free = {s for s in dX.free_symbols if s in {_Bs, _Cs, _Ds}}
    return not free, "Delta_X = 4*A_shp exactly, which is why the axial cuts agree"


# ==========================================================================
homology = _suite("homology and finite volume")


@homology.check("dim Z_2 = (L^3 - 1) + 3 = L^3 + 2", "UNIFIED §0.1")
def _():
    lhs = (K.L**3 - 1) + 3
    return simplify(lhs - K.dim_z2()) == 0, "cube boundaries plus the harmonic plane triplet"


@homology.check("dim Z_2 at L = 3, 4, 5", "UNIFIED §0.1")
def _():
    vals = {n: K.dim_z2(n) for n in (3, 4, 5)}
    return vals == {3: 29, 4: 66, 5: 127}, f"{vals}"


@homology.check("d_2 d_3 = 0 on the built complex", "PAPER_FLATBAND eq. (6), App. B")
def _():
    sizes = (1, 2, 3, 4)
    bad = [n for n in sizes if not TOR.chain_condition(n)]
    return not bad, (
        f"exact over Z at L = {sizes}, from the printed face and cube boundary formulas: the "
        "composite links-by-cubes matrix is identically zero"
    )


@homology.check("rank d_3 = L^3 - 1 on the built complex", "PAPER_FLATBAND eq. (14), App. B")
def _():
    got = {n: TOR.ranks(n)["rank_d3"] for n in (1, 2, 3, 4, 5)}
    return got == {n: n**3 - 1 for n in got}, (
        f"{got}; the single relation among translated cube boundaries is the oriented sum over "
        "all cubes, and both primes agree at every size"
    )


@homology.check(
    "dim Z_2 = L^3 + 2 by rank, not by re-arranging the formula", "PAPER_FLATBAND eq. (15)"
)
def _():
    got = {n: TOR.ranks(n)["dim_ker_d2"] for n in (1, 2, 3, 4, 5)}
    return got == {n: n**3 + 2 for n in got}, (
        f"{got} = L^3 + 2 at L = 1..5, from rank(d_2) on the built complex. This is the check the "
        "suite did not have: the two above it simplify (L^3-1)+3 to L^3+2 and evaluate that "
        "formula, which is arithmetic, not homology"
    )


@homology.check("cube boundaries and three wrapping sheets SPAN Z_2", "PAPER_FLATBAND Thm. 2")
def _():
    rows = {
        n: (TOR.ranks(n)["span_generators"], TOR.ranks(n)["dim_ker_d2"]) for n in (1, 2, 3, 4, 5)
    }
    ok = all(a == b for a, b in rows.values()) and all(TOR.sheets_are_cycles(n) for n in rows)
    return ok, (
        f"rank[d_3 | sheets] vs dim ker d_2: {rows}. Each sheet is a cycle over Z and the two "
        "bounds meet, so Z_2 = im d_3 (+) H_2 with an explicit basis rather than a dimension count"
    )


@homology.check(
    "the L^3+2 count is chain-level, not the Bloch convention", "PAPER_FLATBAND Thm. 2 remark"
)
def _():
    # The manuscript's abstract attaches "L >= 3" to the count, and its Thm. 2
    # does not. The caveat belongs to the twelve-neighbour Bloch adjacency,
    # where x+e and x-e coincide at L = 2; the chain complex has no such
    # problem. Pinned so the small cases are never "fixed".
    small = {n: TOR.ranks(n)["dim_ker_d2"] for n in (1, 2)}
    return small == {1: 3, 2: 10}, (
        f"{small} = L^3+2 at L = 1, 2. At L = 1 every boundary formula degenerates and d_2 = 0, "
        "so all three faces are cycles; at L = 2 the multigraph caveat bites S, not d_2"
    )


@homology.check(
    "FINDING: the wrapping sheets are cycles but NOT harmonic", "PAPER_FLATBAND §6 vs Thm. 2"
)
def _():
    # The manuscript uses H_2 in two senses four pages apart. In Theorem 2 it
    # is the quotient ker d_2 / im d_3, which the wrapping sheets span. In §6
    # it is the harmonic subspace ker d_2 ^ ker d_3*, on which a term
    # proportional to L_up = d_3 d_3* is said to act trivially -- "leaving the
    # three harmonic sheets pinned". The only generators the paper exhibits
    # belong to the first sense: they are cycles, but d_3* does not kill them,
    # and L_up moves them by the same Rayleigh quotient at every size.
    #
    # Nothing downstream breaks: Proposition 7 rests on B* w = 0, which covers
    # all of ker d_2. It is §6's real-space restatement that does not cover the
    # objects Theorem 2 constructs.
    ratios = {n: TOR.sheet_up_laplacian_ratio(n) for n in (2, 3, 4)}
    cycles = all(TOR.sheets_are_cycles(n) for n in (2, 3, 4))
    return cycles and all(a == 2 * b for a, b in ratios.values()), (
        f"<s, L_up s> vs ||s||^2: {ratios} -- the Rayleigh quotient is exactly 2 at every L >= 2, "
        "while d_2 s = 0 exactly. The sheets represent the three H_2 classes and are not harmonic"
    )


def run_all() -> list[Result]:
    """Run every suite and return a flat list of results."""
    return [r for s in SUITES for r in s.run()]


# ==========================================================================
adjudication = _suite("settlement package and adjudication harness")


@adjudication.check("cold reruns re-certify both in-corpus audits", "SETTLEMENT.md §2")
def _():
    runs = S.read_cold_runs()
    ok = len(runs) == 2 and all(r.passed == r.total == 8 for r in runs)
    detail = "; ".join(f"{r.name.replace('cold_rerun_', '')} {r.passed}/{r.total}" for r in runs)
    return ok, detail


@adjudication.check("stranded-flux zero backend stays falsified (C7)", "MASTER_THEORY C7")
def _():
    run = next(r for r in S.read_cold_runs() if "stranded_flux" in r.name)
    # Cold rerun, so C7's evidence class rises from in-corpus to cold-reproduced.
    return run.verdict == "ZERO_BACKEND_FALSIFIED", (
        f"{run.passed}/{run.total}, verdict {run.verdict}; generating script "
        f"sha256 {run.source_sha256[:16]}... (the script is absent from this repo; "
        "settlement/SHA256SUMS pins the transcript, not the script)"
    )


@adjudication.check(
    "FINDING: the target-blindness scan cannot see two scalar-determining targets",
    "settlement/mce_adjudication_harness.py",
)
def _():
    audit = S.audit_contamination_scan()
    missed = audit.uncovered_scalar_determining
    # Asserting the gap, per the repository's convention for findings. When the
    # harness's CONTAMINATION_STRINGS is extended upstream this check will fail,
    # and the correct response is to retire it, not to widen it.
    return missed == {"delta_gamma", "hamer_8a4"}, (
        f"quarantined targets {len(audit.targets)}, scan strings {len(audit.strings)}; "
        f"uncovered {sorted(audit.uncovered)}. Two of those determine the disputed "
        "scalar: m_Gamma = q_band + Delta_Gamma exactly, and Hamer's 8*a_4 IS the "
        "scalar to 13 digits. The scan covers the 16-digit oracle form "
        "7751458630189173, but that string does NOT contain 7751458630184 — they "
        "diverge at index 12 — so an engine carrying either constant passes the scan. "
        "Closing it means adding 0827701250956414, 7751458630184 (and the ...417 "
        "rounding), 160506019419340168451, 7250590288602460800, 4405310420659200."
    )


@adjudication.check(
    "FINDING: the contamination scan reads only the engine file",
    "settlement/mce_adjudication_harness.py",
)
def _():
    return S.scans_a_single_file(), (
        "src = open(engine).read() — an engine that imports a helper module, loads a "
        "JSON/npz, or restores from the sqlite checkpoint carries that content past "
        "the scan entirely"
    )


@adjudication.check(
    "FINDING: the harness can never report COMPLETE",
    "settlement/mce_adjudication_harness.py",
)
def _():
    # item10_W22_toggle is assigned "OPEN (...)" unconditionally and the
    # completeness predicate rejects any OPEN value.
    return not S.verdict_can_be_complete(), (
        "protocol item 10 (W22 order-schedule toggle) is hardcoded OPEN, and the "
        "completeness predicate rejects any OPEN value, so even a certificate that "
        "discharges items 8 and 9 with a full shape block yields PARTIAL. Honest as a "
        "default, but the protocol has no path to closure until the engine exposes "
        "the toggle."
    )


@adjudication.check(
    "the harness carries the printed Delta_Gamma, not the rounded one",
    "settlement/mce_adjudication_harness.py",
    tier=2,
)
def _():
    # Byte-for-byte float equality, no tolerance — but both sides ARE floats,
    # so by this repository's own rule the check is T2 however exact it looks.
    v = S.harness_delta_gamma()
    return v == K.DELTA_GAMMA_AS_PRINTED_NUM, (
        f"harness has {v!r}, matching the corpus's printed value exactly (float identity, "
        f"not a tolerance); the correctly rounded value is {K.DELTA_GAMMA_NUM!r}. Harmless "
        "after unblinding, but if the digit string is added to the scan, add both forms."
    )


@adjudication.check("quarantined targets never reach the engine process", "GLUEBALL §18.1 item 6")
def _():
    audit = S.audit_contamination_scan()
    src = S.HARNESS.read_text()
    # The architecture itself is sound: Q is module-local and the engine is
    # launched with a plain env, so no target is exported. The weakness audited
    # above is detection of a target already inside the engine, not leakage.
    leaks = re.findall(r"env\s*=\s*dict\(os\.environ,([^)]*)\)", src)
    exported = [seg for seg in leaks if any(t in seg for t in audit.targets)]
    return not exported, (
        f"{len(audit.targets)} targets held module-local; engine env carries only "
        "HODGE_SU3_M4_SEALED_SOURCE_FD. Quarantine architecture is sound — the gap "
        "is in detecting a target already present in the engine."
    )


@adjudication.check(
    "the engine the harness drives IS in the repository, renamed by the import",
    "corpus-import/records/RENAME_MANIFEST_2026-08-20.tsv via settlement.py",
)
def _():
    rename = S.engine_rename_record()
    on_disk = S.ENGINE.stat().st_size if S.ENGINE.exists() else -1
    first_line = S.ENGINE.read_text(errors="ignore").splitlines()[0]
    ok = (
        rename is not None
        and rename.source.endswith("Hodge_SU3_Exact_MarkedCluster_m4_Colab.py")
        and rename.destination.endswith("DATA_SU3_Exact_MarkedCluster_m4_Colab.py")
        and rename.size == on_disk
        and "marked-cluster fourth-order engine" in first_line
    )
    sha = hashlib.sha256(S.ENGINE.read_bytes()).hexdigest()
    return ok, (
        f"rename manifest: {rename.source.split('/')[-1]} -> "
        f"{rename.destination.split('/')[-1]}, {rename.size} bytes = on-disk size; "
        f"sha256 {sha[:16]}...; the settlement package's received README records "
        "this engine as absent — that record described the filename, not the corpus"
    )


@adjudication.check(
    "the engine is clean under the harness scan AND the extended scan",
    "settlement/mce_adjudication_harness.py + the scan-gap FINDING above",
)
def _():
    hits = S.engine_scan_hits(extended=True)
    # The FINDING above stands: the harness's own list misses two
    # scalar-determining targets. This check closes the question it left open —
    # whether the engine actually carries one of the missed constants. It does
    # not: blind under both lists.
    return hits == [], (
        f"harness strings ({len(S.audit_contamination_scan().strings)}) plus "
        f"extension strings ({len(S.EXTENDED_CONTAMINATION_STRINGS)}) all absent "
        f"from the engine source; hits = {hits!r}"
    )


@adjudication.check(
    "the engine imports stdlib only, so the single-file scan bounds it",
    "settlement/mce_adjudication_harness.py + corpus engine source",
)
def _():
    roots = S.engine_import_roots()
    extras = roots - S.ENGINE_ALLOWED_IMPORTS
    # The single-file-scan FINDING above stands as a property of the harness.
    # For THIS engine the exposure is bounded: no helper module, no third-party
    # import, so nothing rides in past the scan at import time.
    return not extras, (
        f"{len(roots)} import roots, all in the allowed stdlib+sympy set; "
        f"unexpected = {sorted(extras)!r}"
    )


@adjudication.check(
    "freeze passes here: the corpus engine is behaviorally the verified one",
    "runs/mce_freeze_and_first_run_2026-08-22/FREEZE.json",
)
def _():
    fz = S.read_freeze()
    coverage_pin, preflight_pin = S.harness_preflight_pins()
    engine_sha = hashlib.sha256(S.ENGINE.read_bytes()).hexdigest()
    ok = (
        fz["contamination_scan"] == "clean"
        and fz["self_test"].startswith("47/47")
        and fz["engine_sha256"] == engine_sha
        and fz["preflight"]["candidate_coverage_certificate_sha256"] == coverage_pin
        and fz["preflight"]["preflight_sha256"] == preflight_pin
        and fz["preflight"]["total_exact_cluster_evaluations"] == 609
    )
    return ok, (
        f"self-test {fz['self_test']}; preflight coverage and output SHA256 both "
        "match the harness pins, so the imported engine reproduces the sealed "
        "geometry layer of the upstream-verified engine exactly; engine sha256 "
        f"{engine_sha[:16]}... recorded in FREEZE.json. Reproduce: harness freeze, "
        "~5 s"
    )


@adjudication.check(
    "FINDING: the run stage fail-closes on cluster 1 of 609 — the shipped "
    "closure cap is below the first cluster's own demand",
    "runs/mce_freeze_and_first_run_2026-08-22/README.md",
)
def _():
    cap = S.engine_closure_cap()
    error = S.first_run_error()
    probe = S.first_run_probe()
    ok = (
        cap == 100
        and error == "ExactEngineError: unexpectedly large H0 closure"
        and probe["cap_in_transcript"] == cap
        and probe["max_measured_closure"] > cap
        and probe["first_support_size"] == 1
    )
    return ok, (
        f"first production cluster (support size {probe['first_support_size']}) "
        f"demands an H0 orbit of {probe['max_measured_closure']} states against "
        f"the shipped cap of {cap}, inherited from the electric-resolvent "
        "lineage; the guard aborts rather than truncates, so the frozen protocol "
        "as received cannot start on any hardware. No pre-production path "
        "exercises it: the self-test contracts no real half-history, the "
        "preflight runs zero physics, and the upstream sandbox only *started* "
        "cluster 1. The orbit is finite and barely 2x the cap — an operational "
        "miscalibration, not an explosion — but even the 1-face cluster (the "
        "smallest of 609; 474 are 3-face) exceeded 13 CPU-minutes without "
        "completing, so run-stage feasibility is a cost question upstream too"
    )


# ==========================================================================
near_gamma = _suite("near-Gamma uniformity (G11)")


@near_gamma.check("Jordan bound q(k) >= (4/pi^2)|k|^2 holds on the whole zone", "GLUEBALL §18.3")
def _():
    xs = symbols("xs", real=True)
    diff_expr = 4 * sin(xs / 2) ** 2 - G.JORDAN * xs**2
    # sin'' = -sin <= 0 on [0,pi] so sin is concave and lies above its chord.
    concave = simplify(diff(sin(xs), xs, 2) + sin(xs)) == 0
    samples = [diff_expr.subs(xs, pi * Rational(i, 200)) for i in range(201)]
    never_negative = all(v >= 0 for v in samples)
    tight = simplify(diff_expr.subs(xs, pi)) == 0
    return concave and never_negative and tight, (
        "sin is concave on [0,pi] so it exceeds its chord 2x/pi; substituting "
        "x -> x/2 and squaring gives the bound, with equality at k=0 and at the "
        "zone corner — so the bound is tight, not slack"
    )


@near_gamma.check("t(u) >= t_3 u^2 for u > 0, so the gap bound is safe", "MASTER_THEORY §4.4")
def _():
    # b_3 > 0, so dropping the cubic term can only understate the gap.
    return K.B_3 > 0, f"b_3 = {K.B_3} > 0; t(u) - t_3 u^2 = b_3 u^3 >= 0"


@near_gamma.check("crossover constant K = (pi/2) sqrt(W_4 / (theta t_3))", "GLUEBALL §18.3", tier=2)
def _():
    theta = Rational(1, 2)
    got = G.crossover_constant(K.W4_HISTORICAL_NUM, theta)
    want = (pi / 2) * sqrt(nsimplify(K.W4_HISTORICAL_NUM, rational=True) / (theta * K.T_MINUS_2))
    return simplify(got - want) == 0, f"K_historical(theta=1/2) = {float(got):.4f}"


@near_gamma.check(
    "the criterion survives C2: K depends on the kernel only through sqrt(W_4)",
    "MASTER_THEORY §5.5 / C2",
    tier=2,
)
def _():
    theta = Rational(1, 2)
    k_hist = float(G.crossover_constant(K.W4_HISTORICAL_NUM, theta))
    k_new = float(G.crossover_constant(K.W4_NEW_NUM, theta))
    ratio = k_new / k_hist
    expected = (K.W4_NEW_NUM / K.W4_HISTORICAL_NUM) ** 0.5
    conservative = float(G.conservative_constant(theta))
    return abs(ratio - expected) < 1e-12 and conservative >= max(k_hist, k_new), (
        f"K_hist = {k_hist:.4f}, K_new = {k_new:.4f}, ratio {ratio:.6f} = "
        f"sqrt(W4_new/W4_old); the larger constant {conservative:.4f} bounds both, so "
        "the exclusion radius can be stated now without adjudicating C2"
    )


@near_gamma.check(
    "the statement is non-vacuous only below an explicit coupling",
    "GLUEBALL §18.3",
    tier=2,
)
def _():
    theta = Rational(1, 2)
    u_max = float(G.max_coupling(theta))
    # At u_max the excluded ball exactly fills the inscribed sphere of the zone.
    at_max = G.excluded_zone_fraction(u_max * 1.01, theta)
    return 0 < u_max < 1 and at_max == 1.0, (
        f"K*u < pi requires u < {u_max:.6f} at theta=1/2 "
        f"(u < {float(G.max_coupling(1)):.6f} at theta=1). Above that the excluded "
        "ball covers the zone and the near-Gamma claim says nothing."
    )


@near_gamma.check("excluded zone fraction grows as u^3", "GLUEBALL §18.3", tier=2)
def _():
    f1 = G.excluded_zone_fraction(0.02)
    f2 = G.excluded_zone_fraction(0.04)
    return abs(f2 / f1 - 8) < 1e-9, (
        f"u=0.02 excludes {100 * f1:.2f}%, u=0.04 excludes {100 * f2:.2f}% "
        "— a factor of 8, as a ball volume must"
    )


# ==========================================================================
tier = _suite("tier collapse (G14)")


@tier.check(
    "clearing the denominator reproduces the five-element numerator basis", "MASTER_THEORY §5.1"
)
def _():
    a1, a2, a3 = symbols("a1 a2 a3", nonnegative=True)
    c0, A, B, C, D = symbols("c0 A_shp B_shp C_shp D_shp")
    q = a1 + a2 + a3
    e2 = a1 * a2 + a1 * a3 + a2 * a3
    e3 = a1 * a2 * a3
    eps4 = c0 + A * q + B * e2 + C * 4 * e2 / q + D * e3 / q
    regrouped = c0 * q + A * q**2 + B * q * e2 + 4 * C * e2 + D * e3
    return simplify(expand(eps4 * q) - regrouped) == 0, (
        "q*eps_4 = c_0 q + A q^2 + 4C e_2 + B (q e_2) + D e_3, rank five as recorded"
    )


@tier.check("the vanishing coefficients are exactly the degree-3 ones", "MASTER_THEORY §5.2 / G14")
def _():
    degrees = T.numerator_degrees()
    carried = {name: T.NUMERATOR_BASIS[name][1] for name in T.NUMERATOR_BASIS}
    deg3 = {carried[n] for n, d in degrees.items() if d == T.VANISHING_DEGREE}
    lower = {carried[n] for n, d in degrees.items() if d < T.VANISHING_DEGREE}
    return deg3 == set(T.VANISHING) and not (deg3 & lower), (
        f"degree 3 carries {sorted(deg3)} — exactly the pair that vanishes; "
        f"degrees 1-2 carry {sorted(lower)}, all nonzero. Since a_i ~ L^-2, "
        "'the L^-4 tier' and 'degree 3 in a' are the same statement. This is an "
        "identity and survives the retraction below."
    )


@tier.check("B B^dagger = q I - d conj(d)^T for the curl incidence", "UNIFIED §2.4")
def _():
    residual = T.incidence_identity()
    return residual == residual.zeros(3, 3), (
        "the face-to-link Bloch incidence is the curl matrix [d]_x, entries linear "
        "in d; the identity gives eigenvalues (0, q, q), matching the recorded "
        "second-order C-odd spectrum with the flat carrier as the d-direction"
    )


@tier.check("the carrier projection is where the 1/q comes from", "MASTER_THEORY §5.1")
def _():
    d1, d2, d3, c1, c2, c3 = symbols("d1 d2 d3 c1 c2 c3")
    d = Matrix([d1, d2, d3])
    c = Matrix([c1, c2, c3])
    q = c1 * d1 + c2 * d2 + c3 * d3
    return simplify(expand((c.T * d)[0]) - q) == 0, (
        "d^dagger d = q, so eps_4 = (d^dagger H_4 d)/q and the numerator that spans "
        "{q, q^2, q e_2, e_2, e_3} is d^dagger H_4 d"
    )


@tier.check("RETRACTED: the vertex count does NOT forbid B_shp and D_shp", "G14 / ADR 0005")
def _():
    # The proposed mechanism counted 2r vertices -> numerator degree <= r, and
    # concluded degree 3 was unreachable at fourth order. It missed that the
    # carrier projection d^dagger (.) d adds one further power of a.
    op = T.operator_degree_bound(4)
    num = T.numerator_degree_bound(4)
    permits = num >= T.VANISHING_DEGREE
    return op == 2 and num == 3 and permits, (
        f"four vertices bound H_4 entries at a-degree {op}, but the numerator "
        f"d^dagger H_4 d reaches {num} — exactly the degree of "
        f"{sorted(T.VANISHING)}. Witness: d^dagger diag(a_i^2) d = sum a_i^3 = "
        "q^3 - 3 q e_2 + 3 e_3, carrying a nonzero e_3. MASTER_THEORY §5.1 already "
        "recorded that the 144 two-hop sequences GIVE the rank-five span including "
        "those terms, which is a dynamical vanishing, not a kinematic exclusion."
    )


@tier.check("the sixth-order prediction is withdrawn, not merely unproven", "ADR 0005")
def _():
    # Degree 3 is reachable at fourth order once the projection is counted, so
    # "sixth order is the first place it becomes reachable" is simply false.
    return T.numerator_degree_bound(4) >= T.VANISHING_DEGREE, (
        "the prediction rested on degree 3 being unreachable through O(u^4); it is "
        "reachable, so the prediction has no basis and G14 keeps no falsifier from it"
    )


# ==========================================================================
pentagonal = _suite("isotropic pentagonal cap band (v4.3 §9.3)")
# A separate geometry and retained sector. Nothing here bears on the cubic
# SU(3) fourth-order kernel, and the checks say so where it would be tempting
# to borrow a number across.


@pentagonal.check("the two face energies differ, so the eigenspace must be chosen", "§9.3 / C8")
def _():
    # H_0 = (1/2) sum_e E_e^2 with E_cap = 10/3, E_side = 8/3. Because these are
    # unequal there is no single equal-energy one-face manifold to fall into by
    # default: the physical sector is the charge-odd cap sector, and the formal
    # cap-plus-side cycle space is a different object (R21).
    gap = K.E_CAP - K.E_SIDE
    return K.E_CAP != K.E_SIDE and gap == Rational(2, 3), (
        f"E_cap = {K.E_CAP}, E_side = {K.E_SIDE}, gap = {gap}; the degenerate "
        "space is not the whole one-face space"
    )


@pentagonal.check("h_4^side = A_+ - A_- exactly", "§9.3")
def _():
    diff_ = K.PENT_A_PLUS - K.PENT_A_MINUS
    return diff_ == K.H4_SIDE, (
        f"A_+ = {K.PENT_A_PLUS}, A_- = {K.PENT_A_MINUS}, "
        f"A_+ - A_- = {diff_} = h_4^side = {K.H4_SIDE}"
    )


@pentagonal.check("the h_4^side -> tau_4 factor is exactly 5", "§9.3")
def _():
    # Exact D_5 covariance. Recording the multiplier is the point: two printed
    # coefficients differing by an undocumented integer factor are
    # indistinguishable from a transcription error until someone names the group.
    ratio = K.TAU_4 / K.H4_SIDE
    return ratio == K.D5_COVARIANCE_FACTOR, (
        f"tau_4 / h_4^side = {ratio}, the order of the cyclic symmetry C_5 "
        f"of the pentagonal cap; tau_4 = {K.TAU_4}"
    )


@pentagonal.check("the tau_4 -> Delta E_cap factor is exactly 2", "§9.3")
def _():
    # The two terms of the Hermitian hop |a_z><a_{z+1}| + |a_{z+1}><a_z|, which
    # is why cos k rather than exp(ik) appears. Not a second convention.
    ratio = K.DELTA_E_CAP_4 / K.TAU_4
    return ratio == K.HOP_HERMITIAN_FACTOR, (
        f"Delta E_cap^(4) / tau_4 = {ratio}; the hop is Hermitian, so the "
        f"symbol is 2 tau_4 cos k with 2 tau_4 = {K.DELTA_E_CAP_4}"
    )


@pentagonal.check("bandwidth = 4|tau_4| and the band minimum sits at k = 0", "§9.3")
def _():
    k = symbols("k", real=True)
    symbol = K.DELTA_E_CAP_4 * sympify("cos(k)").subs(symbols("k"), k)
    width = simplify(symbol.subs(k, pi) - symbol.subs(k, 0))
    at_zero = symbol.subs(k, 0)
    at_pi = symbol.subs(k, pi)
    return (
        width == K.PENT_BANDWIDTH_4 and 4 * abs(K.TAU_4) == K.PENT_BANDWIDTH_4 and at_zero < at_pi
    ), (
        f"2 tau_4 (cos pi - cos 0) = {width} = 4|tau_4| = {K.PENT_BANDWIDTH_4}; "
        f"E(0) = {at_zero} < E(pi) = {at_pi}, so tau_4 < 0 puts the minimum at k = 0"
    )


@pentagonal.check("240 = 5 x 48 histories per adjacent direction", "§9.3")
def _():
    return K.PENT_HISTORIES_PER_DIRECTION == 5 * K.PENT_FIXED_SIDE_HISTORIES, (
        f"{K.PENT_HISTORIES_PER_DIRECTION} = 5 x {K.PENT_FIXED_SIDE_HISTORIES}: the "
        "48 fixed-side histories carried around the five cap positions, which is "
        "the same C_5 orbit that produced the factor 5 above"
    )


@pentagonal.check("hop range 4 refutes the r = w_min - 2 promotion", "§9.3 / C6")
def _():
    # C6: the promotion r_physical = w_min - 2 is falsified here. w_min = 7 for
    # this geometry, so the rule predicts 5 while the exact calculation gives 4.
    w_min = 7
    predicted = w_min - 2
    return K.PENT_HOP_RANGE == 4 and predicted == 5 and predicted > K.PENT_HOP_RANGE, (
        f"r_hop = {K.PENT_HOP_RANGE}, but w_min - 2 = {predicted}; the scoped "
        "bound r >= w_min - 2 does not survive as an equality"
    )


@pentagonal.check("the tuned cap-plus-side symbol is a different Hamiltonian", "§9.3 / R21")
def _():
    # mu(k) = 4 cos k (1 - cos k)/(7 - 2 cos k) is the OLD formal compression. It
    # is not proportional to the isotropic symbol cos k, so no rescaling carries
    # h_4^side across; the tuned model needs w_vertical = (3/2) w_horizontal.
    k = symbols("k", real=True)
    c = sympify("cos(k)").subs(symbols("k"), k)
    mu = 4 * c * (1 - c) / (7 - 2 * c)
    ratio = simplify(mu / c)
    return simplify(diff(ratio, k)) != 0 and Rational(3, 2) == K.PENT_TUNED_WEIGHT_RATIO, (
        f"mu(k)/cos k = {ratio} is k-dependent, so mu is not a multiple of the "
        f"isotropic symbol; the tuned model requires w_vertical/w_horizontal = "
        f"{K.PENT_TUNED_WEIGHT_RATIO} and a fresh anisotropic backend"
    )


@pentagonal.check("h_4^side and the cubic kernel share no denominator structure", "§9.3")
def _():
    # Guard against the most natural misuse: quoting the pentagonal coefficient
    # as though it constrained the disputed cubic fourth order.
    shared = K.H4_SIDE.q == K.Q_BAND_4.q
    return not shared, (
        f"h_4^side has denominator {K.H4_SIDE.q}, q_band^(4) has "
        f"{K.Q_BAND_4.q}; separate geometries, separate retained sectors, and "
        "the pentagonal theorem leaves the cubic fourth-order scalar untouched"
    )


# ==========================================================================
string_tension = _suite("native string tension through fifth order (v4.3 §11.2)")


@string_tension.check("sigma_n^phys = (-1)^n sigma_n^raw, and C5 is the n = 3 case", "§11.2 / C5")
def _():
    # C5 recorded "-61/408 (the earlier +61/408 was an odd-order convention
    # error)" without saying which rule produced it. R14 states the rule; this
    # check is that C5's number is what the rule gives at n = 3.
    raw_3 = -K.SIGMA_3
    phys_3 = (-1) ** 3 * raw_3
    return (
        phys_3 == K.SIGMA_3
        and raw_3 == Rational(61, 408)
        and K.SIGMA_5_RAW == -K.SIGMA_5
        and K.SIGMA_5 < 0
    ), (
        f"sigma_3^raw = +{raw_3} -> sigma_3^phys = {phys_3}, exactly C5's "
        f"correction; sigma_5^raw = +{K.SIGMA_5_RAW} -> sigma_5^phys = {K.SIGMA_5}, "
        "so both odd physical coefficients are negative"
    )


@string_tension.check("the even coefficients are not sign-flipped", "§11.2")
def _():
    # A rule applied to the wrong parity is the classic way this erratum comes
    # back. (-1)^n is +1 at n = 2 and n = 4, so those printed signs are the raw
    # signs and must be left alone.
    return all((-1) ** n == 1 for n in (2, 4)) and K.SIGMA_2 < 0 and K.SIGMA_4 < 0, (
        f"sigma_2 = {K.SIGMA_2} and sigma_4 = {K.SIGMA_4} are negative in BOTH "
        "conventions; only odd n flips"
    )


@string_tension.check("sigma_4 shares the historical-branch denominator", "§11.2 / §6")
def _():
    # Same 7250590288602460800 as q_band^(4). Both are historical-branch fourth
    # order, so this is a provenance fingerprint, not a coincidence -- and it is
    # the reason sigma_4 inherits whatever the fourth-order kernel dispute
    # settles on.
    return K.SIGMA_4.q == K.Q_BAND_4.q, (
        f"sigma_4 and q_band^(4) both have denominator {K.SIGMA_4.q}; "
        f"q_band^(4)/sigma_4 = {K.Q_BAND_4 / K.SIGMA_4}"
    )


@string_tension.check("the seven-prime CRT reconstruction clears its uniqueness bound", "§11.2")
def _():
    numerator_bits = K.SIGMA_5_RAW.p.bit_length()
    denominator_bits = K.SIGMA_5_RAW.q.bit_length()
    bound = K.SIGMA_5_MODULUS_BITS // 2
    return (
        numerator_bits == 77
        and denominator_bits == 81
        and bound == K.SIGMA_5_UNIQUENESS_BITS
        and max(numerator_bits, denominator_bits) < bound
    ), (
        f"189-bit modulus gives a {bound}-bit rational-reconstruction bound; the "
        f"recovered numerator is {numerator_bits} bits and the denominator "
        f"{denominator_bits} bits, so the pair is the unique preimage"
    )


@string_tension.check("the ratio and sigma series reproduce E_flat exactly", "§11.2 vs §4.4")
def _():
    # The strongest thing in §11.2, and it is not stated there. Two independent
    # routes meet:
    #   §11.2 gives sigma(u) and m/sqrt(sigma) = sqrt(6)(4/3 + u/2 + 11/68 u^2
    #         - 7559/499392 u^3 + O(u^4));
    #   §4.4 gives E_flat(u) = 8/3 + u + 11/306 u^2 + D_3 u^3 from the C-even /
    #         C-odd hopping ledger, with D_3 = 7/32 + 12 leak_3 - 4 b_3.
    # Multiplying the first two recovers the third term by term, D_3 included.
    # Nothing was fitted: the ratio coefficients and sigma come from the string
    # sector, D_3 from the mass sector.
    coupling = symbols("u", positive=True)
    sigma = K.SIGMA_0 + sum(
        c * coupling**n for n, c in ((2, K.SIGMA_2), (3, K.SIGMA_3), (4, K.SIGMA_4), (5, K.SIGMA_5))
    )
    ratio = sqrt(6) * sum(c * coupling**n for n, c in enumerate(K.RATIO_UNDISPUTED))
    recovered = series(ratio * sqrt(sigma), coupling, 0, 4).removeO()
    expected = K.e_flat(coupling)
    residual = simplify(expand(recovered - expected))
    coefficients = [simplify(recovered.coeff(coupling, n)) for n in range(4)]
    return residual == 0, (
        f"sqrt(6) * ratio(u) * sqrt(sigma(u)) = {coefficients} through u^3, which "
        f"is E_flat term by term: 8/3, 1, 11/306, and D_3 = {K.D_3}. The u^3 "
        "coefficient is the discriminating one -- a normalization slip anywhere in "
        "either series would not land on it"
    )


@string_tension.check("m_{1+-}(0) = 8/3 follows from sigma(0) = 2/3 alone", "§11.2")
def _():
    # The constant term separately, because it is the one an eye can check:
    # sqrt(6) * (4/3) * sqrt(2/3) = 8/3, the free one-plaquette energy.
    leading = simplify(sqrt(6) * K.RATIO_UNDISPUTED[0] * sqrt(K.SIGMA_0))
    return leading == Rational(8, 3), (
        f"sqrt(6) * {K.RATIO_UNDISPUTED[0]} * sqrt({K.SIGMA_0}) = {leading}, the "
        "u -> 0 flat-band energy; the ratio's constant term is fixed by sigma(0), "
        "not free"
    )


@string_tension.check("the ratio series stops before the disputed order", "§11.2 / C2")
def _():
    # Four coefficients, ending at u^3. The u^4 term is withheld because it
    # inherits C2, not because it is unknown -- and the check above shows the
    # first four are tightly constrained, so the omission is load-bearing.
    return len(K.RATIO_UNDISPUTED) == 4, (
        f"the quoted ratio is sqrt(6) * {K.RATIO_UNDISPUTED} through u^3; C2 "
        "reaches every higher coefficient through the fourth-order mass kernel"
    )


# ==========================================================================
published = _suite("published comparisons (literature/index.yaml)")
# An external result is not authority either -- it is T3 until something checks
# it. What makes one valuable is independence: it was produced without any
# knowledge of this program, so agreement is evidence rather than bookkeeping.


@published.check("SU(3) Weingarten values follow from the general formula", "CS_2006 / C7")
def _():
    # C7's decisive witness quotes Wg(e) = 1/8 and Wg((12)) = -1/24 for SU(3)
    # from a transcript. Re-derive them, symbolically in N, from the definition:
    # the order-n Weingarten matrix is the inverse of the Gram matrix
    # G[s,t] = N**(number of cycles of s*t^-1) on the symmetric group S_n —
    # built once, in cellular.weingarten_2, beside the n = 1 case the
    # tetrahedral merge lemma rests on.
    n = CELL.N
    identity, transposition = CELL.weingarten_2()
    return (
        simplify(identity - 1 / (n**2 - 1)) == 0
        and simplify(transposition + 1 / (n * (n**2 - 1))) == 0
        and identity.subs(n, 3) == Rational(1, 8)
        and transposition.subs(n, 3) == Rational(-1, 24)
    ), (
        f"Wg(e) = {identity} and Wg((12)) = {transposition} for all N; "
        f"at N = 3 they are {identity.subs(n, 3)} and {transposition.subs(n, 3)}, "
        "exactly the values C7 quotes"
    )


@published.check("the fourth moment integral |U_11|^4 = 1/6 at N = 3", "CS_2006 / C7")
def _():
    # The other half of C7's witness. All four indices are 1, so every pair
    # (sigma, tau) in S_2 x S_2 contributes and the integral is the full sum of
    # the Weingarten matrix: 2 Wg(e) + 2 Wg((12)).
    n = CELL.N
    identity, transposition = CELL.weingarten_2()
    moment = simplify(2 * identity + 2 * transposition)
    return simplify(moment - 2 / (n * (n + 1))) == 0 and moment.subs(n, 3) == Rational(1, 6), (
        f"integral |U_11|^4 dU = {moment} = 2/(N(N+1)); at N = 3 that is "
        f"{moment.subs(n, 3)}, nonzero -- which is what refuted the claimed Haar zero "
        "for the balanced (n_U, n_Udag) = (2,2) sector"
    )


@published.check("the Weingarten route is independent of the corpus", "CS_2006 / C7")
def _():
    # Worth stating explicitly, because it is the reason C7 is settled rather
    # than merely disputed. The derivation above uses only the symmetric group
    # and the rank; it imports no constant, convention, or coefficient from the
    # corpus, so it cannot inherit an error from it.
    identity, _transposition = CELL.weingarten_2()
    generic = simplify(identity * (CELL.N**2 - 1))
    return generic == 1, (
        "the identity-permutation Weingarten value times (N^2 - 1) is exactly 1 for "
        "symbolic N, so the SU(3) numbers are a specialization of a rank-generic "
        "formula rather than a fitted pair"
    )


@published.check(
    "the Hamer table is pinned, and the a_4 agreement is primary-source",
    "HAMER_1989",
    tier=2,
)
def _():
    # This check used to assert its own caveat: the strongest external
    # agreement rested on an unhashed transcription. On 2026-08-21 the
    # four-page primary was obtained, digest-pinned (sha256 in the index; the
    # publisher-copyright PDF is NOT stored), and Table 1 (M_A, order 4) reads
    # -0.968932328773 E-1 — digit for digit the registry's a_4, verified
    # against the rendered page image rather than OCR. The caveat is retired,
    # not forgotten: the bound is unchanged, and the pin is asserted here so
    # it cannot quietly disappear.
    from . import literature as lit_mod

    lit = lit_mod.load()
    paper = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    edges = lit.bearing_on("HAMER_A4_NUM")
    supplies = [e for _p, e in edges if e["relation"] == "supplies-value"]
    bridged = 8 * K.HAMER_A4_NUM
    gap = abs(bridged - K.M_GAMMA_4_NUM)
    digest = str(paper.get("source_sha256", ""))
    return (
        len(supplies) == 1
        and supplies[0]["status"] == "verified"
        and len(digest) == 64
        and K.HAMER_MA_NUM[2] == K.HAMER_A4_NUM
        and len(paper.get("answered_questions", [])) == 5
        and gap < K.HAMER_TOLERANCE
    ), (
        f"8 * a_4 = {bridged} against m_Gamma^(4) = {K.M_GAMMA_4_NUM}, gap {gap:.2e} "
        f"(bound {K.HAMER_TOLERANCE:.1e}); the copy read is pinned as sha256 "
        f"{digest[:16]}…, a_4 equals Table 1's M_A order-4 entry, and the corpus "
        "audit's five open questions carry answers from the pinned copy"
    )


@published.check(
    "Hamer's 1+- series matches the C-odd Gamma-point coefficients through x^3",
    "HAMER_1989 / C1",
    tier=2,
)
def _():
    # Table 1's M_A column against the program's vacuum-subtracted C-odd
    # series under the bridge m_n = 2**(n-1) a_n. Orders 0 and 1 are exact in
    # the paper: a_0 = 16/3 (recurring-decimal dot) halves to the free
    # plaquette energy 8/3, and a_1 = +1 is the u-coefficient of e_flat.
    # Orders 2 and 3 are printed to 12 significant digits; the bounds are a
    # few times the printed half-ulp times the bridge factor, and the detail
    # carries the measured gaps so nobody has to trust the bound choice.
    exact_ok = Rational(16, 3) / 2 == K.e_flat(0) == Rational(8, 3)
    gap2 = abs(2 * K.HAMER_MA_NUM[0] - float(Rational(11, 306)))
    gap3 = abs(4 * K.HAMER_MA_NUM[1] - float(K.D_3))
    return exact_ok and gap2 < 2e-13 and gap3 < 3e-12, (
        f"n=0: 16/3 / 2 = 8/3 = e_flat(0) exactly; n=1: a_1 = +1 = the u-coefficient; "
        f"n=2: 2 a_2 = {2 * K.HAMER_MA_NUM[0]!r} vs 11/306, gap {gap2:.2e} (bound 2e-13); "
        f"n=3: 4 a_3 = {4 * K.HAMER_MA_NUM[1]!r} vs D_3 = -109151/249696, gap {gap3:.2e} "
        "(bound 3e-12 = printed half-ulp x 4 with margin) — a 1989 table agreeing with "
        "rationals this program computed cold, at every shared order"
    )


@published.check(
    "Hamer's 0++ series matches the C-even Gamma-point coefficients through x^3",
    "HAMER_1989",
    tier=2,
)
def _():
    # The C-even sector too: Table 1's M_S column against the corpus's
    # vacuum-subtracted A1++ coefficients at k = 0. The n = 3 target is a
    # corpus certificate value (RUN_TROM d3) not independently re-derived
    # here, so this check binds two INDEPENDENT sources to each other: a 1989
    # journal table and a 2026 cold run, neither computed with knowledge of
    # the other.
    exact_ok = Rational(16, 3) / 2 == Rational(8, 3) and K.HAMER_MS_NUM[0] < 0
    gap2 = abs(2 * K.HAMER_MS_NUM[0] - float(K.BAND_EVEN_BOTTOM))
    gap3 = abs(4 * K.HAMER_MS_NUM[1] - float(K.M3_EVEN_K0))
    return exact_ok and gap2 < 2e-12 and gap3 < 5e-13, (
        f"n=2: 2 a_2 = {2 * K.HAMER_MS_NUM[0]!r} vs -217/1020, gap {gap2:.2e} "
        f"(bound 2e-12); n=3: 4 a_3 = {4 * K.HAMER_MS_NUM[1]!r} vs -54049/520200, "
        f"gap {gap3:.2e} (bound 5e-13); a_1 = -1 in the scalar channel where the "
        "carrier's is +1 — the sign structure matches too"
    )


@published.check("the m_n = 2^(n-1) a_n bridge is the x = 2u conversion", "HAMER_1989")
def _():
    # The bridge the corpus asserts, proved as algebra: with x = 2/g^4 = 2u
    # and m a = (g^2/2) M (Hamer eqs. (1)-(2)), the series m(u) = M(x=2u)/2
    # term by term, so the u^n coefficient is a_n 2^n / 2 = 2^(n-1) a_n. Not
    # a fit and not a convention choice — the two printed equations force it.
    u_, x_ = symbols("u x", positive=True)
    a = symbols("a0:5", positive=True)
    series_m = sum(coefficient * x_**n for n, coefficient in enumerate(a)).subs(x_, 2 * u_) / 2
    bridged = [simplify(series_m.coeff(u_, n) - 2 ** (n - 1) * a[n]) for n in range(5)]
    return all(b == 0 for b in bridged), (
        "M(2u)/2 has u^n coefficient 2^(n-1) a_n for n = 0..4 identically — the "
        "half from m a = (g^2/2) M, the 2^n from x = 2u; no 4**r ambiguity anywhere"
    )


@published.check(
    "the series Hamer supersedes is Kogut-SINCLAIR-Susskind 1976, not KS 1975", "HAMER_1989"
)
def _():
    # Hamer's reference [7] — the series his x^3 and x^4 terms disagree with —
    # is the THREE-author Nucl. Phys. B114 (1976) 199, not the two-author
    # Hamiltonian-formulation paper this program's coordinate convention rests
    # on. An earlier revision of the index note conflated them ("supersedes
    # KS_1975"); INSPIRE's reference list for Hamer's recid 25468 carries both
    # papers as separate entries. This check pins the disentanglement so it
    # cannot silently regress: the reported disagreement lands on KSS_1976 as
    # contradiction edges, KS_1975 carries none, and the citation web records
    # Hamer citing both.
    from . import literature as lit_mod

    # The exact two-element target set is pinned in tests/test_literature.py;
    # here the fourth-order constant stays unnamed because this check is T1
    # and the tier guard reads the float-registry suffix anywhere in a check
    # body as a float dependency. The verdict below is pure structure:
    # recids, author counts, relations, and the citation web.
    lit = lit_mod.load()
    kss = next(p for p in lit.papers if p["id"] == "KSS_1976")
    ks = next(p for p in lit.papers if p["id"] == "KS_1975")
    hamer = next(p for p in lit.papers if p["id"] == "HAMER_1989")
    kss_targets = {e["target"] for e in kss["bears_on"]}
    return (
        kss["inspire_recid"] == 3785
        and ks["inspire_recid"] == 1336
        and len(kss["authors"]) == 3
        and len(ks["authors"]) == 2
        and {e["relation"] for e in kss["bears_on"]} == {"contradicts"}
        and len(kss_targets) == 2
        and "D_3" in kss_targets
        and all(e["relation"] != "contradicts" for e in ks["bears_on"])
        and {"KS_1975", "KSS_1976"} <= set(hamer.get("cites", []))
    ), (
        "Hamer 1989 cites both recid 1336 (Kogut-Susskind, 2 authors, the "
        "Hamiltonian) and recid 3785 (Kogut-Sinclair-Susskind, 3 authors, the "
        "series); the x^3/x^4 disagreement Hamer reports lands on KSS_1976 as "
        "contradiction edges against D_3 and the Gamma-point fourth-order "
        "registry value, pending a read of the primary, and KS_1975 carries "
        "no contradiction edge"
    )


@published.check(
    "the KPS 1980 string-tension table equals the certified sigma series EXACTLY",
    "KPS_1981 / G7",
)
def _():
    # The strongest kind of external agreement this repository has: Table 2
    # of the pinned Kogut-Pearson-Shigemitsu preprint (KEK scan, ILL-(TH)-
    # 80-41, September 1980) prints the 3+1 dimensional SU(3) Hamiltonian
    # string-tension coefficients as exact rationals, and under the same
    # x = 2u bridge as the Hamer table (sigma_n = 2**(n-1) t_n, from
    # T = (g**2/2a**2) W(x) against the corpus's vacuum-normalized sigma(u))
    # they equal the certified SIGMA_n rational for rational -- including the
    # CRT-certified SIGMA_4 and SIGMA_5, whose 18- and 24-digit numerators
    # appear digit for digit in a table printed in 1980, 46 years before this
    # program recomputed them cold. The paper's p.5 records that its own
    # earlier x^5 (KPS PRL 43, 484) was wrong and is corrected here: the
    # certified value agrees with the CORRECTION, not the original. Exact
    # equality, so T1: no tolerance anywhere.
    rows = {
        2: 2 * K.KPS_T2 == K.SIGMA_2,
        3: 4 * K.KPS_T3 == K.SIGMA_3,
        4: 8 * K.KPS_T4 == K.SIGMA_4,
        5: 16 * K.KPS_T5 == K.SIGMA_5,
    }
    edges = K.KPS_T0 / 2 == K.SIGMA_0 == Rational(2, 3)
    return all(rows.values()) and edges, (
        f"2^(n-1) t_n = sigma_n exactly for n = 2..5: {rows}; t_0/2 = 2/3 = sigma_0 "
        "and t_1 = 0 matches the absent sigma_1. The printed sign is negative at "
        "every order, i.e. the R14 physical convention sigma_n^phys, and the n = 5 "
        "row agrees with KPS's own 1980 correction of their 1979 PRL x^5 error"
    )


@published.check(
    "the KPS eq. (6a) decimals are its own Table 2, to a printed ulp",
    "KPS_1981",
    tier=2,
)
def _():
    # The transcription guard: eq. (6a)'s seven-digit decimals and Table 2's
    # exact rationals were transcribed independently from different pages of
    # the scan, so their agreement within one printed ulp checks both -- in
    # particular the 56-digit t_6 numerator, which no certified value can
    # cross-check yet. The n = 2, 3, 5 entries are truncations rather than
    # roundings of the exact decimal, hence the full-ulp rather than
    # half-ulp bound.
    gaps = {
        n: abs(float(t / K.KPS_T0) - w)
        for (n, t), w in zip(
            ((2, K.KPS_T2), (3, K.KPS_T3), (4, K.KPS_T4), (5, K.KPS_T5), (6, K.KPS_T6)),
            K.KPS_W_NUM,
            strict=True,
        )
    }
    bounds = {2: 5e-9, 3: 5e-9, 4: 5e-10, 5: 1e-9, 6: 5e-10}
    return all(gaps[n] < bounds[n] for n in gaps), (
        "eq. (6a) w_n vs Table 2 t_n/(4/3): "
        + ", ".join(f"n={n}: gap {gaps[n]:.1e} (bound {bounds[n]:.0e})" for n in gaps)
        + " — sigma_6 = 32 t_6 = -0.07786141620… is the published target G7's "
        "native rerun must hit"
    )


@published.check(
    "the errata-resolved Euclidean series is doubly sourced, transcription for transcription",
    "MUNSTER_1981 / SMIT_1982",
)
def _():
    # The corrected Munster-Seo Euclidean SU(3) glueball series had a messy
    # history: NPB 190 (1981), an erratum-and-addendum (NPB 200), then a
    # second erratum (NPB 205 648) fixing the 8th order again — "Murphy's
    # sixth law", thanking Ukawa and Seo. Two primary sources for the final
    # coefficients were obtained and read on 2026-08-21: the definitive NPB
    # 205 erratum itself (maintainer-supplied) and Smit's ITFA-82-3 Table 1
    # (open KEK scan), which reprints all three channels crediting Munster
    # and Seo. The scalar rows were transcribed independently from the two
    # documents; this check asserts the transcriptions agree exactly, and
    # pins Smit's own stated structure that the tensor channel's first three
    # coefficients equal the scalar's. EUCLIDEAN throughout: nothing here
    # touches the certified Hamiltonian series, by corpus section 12.
    same = K.SMIT_EUC_MS == K.MUNSTER_ERR_MS
    tensor_head = K.SMIT_EUC_MT[:3] == K.SMIT_EUC_MS[:3]
    lengths = len(K.SMIT_EUC_MS) == len(K.SMIT_EUC_MA) == len(K.SMIT_EUC_MT) == 8
    return same and tensor_head and lengths, (
        "the NPB 205 (1982) 648 erratum's SU(3) row and Smit's Table 1 scalar "
        "column agree rational for rational through u^8 (m_8 = -179208453/40960); "
        "the tensor channel's first three coefficients equal the scalar's, as "
        "Smit states; Euclidean record only — no Hamiltonian comparison exists "
        "or is permitted"
    )


@published.check(
    "FINDING: Munster's 1985 table shifts his 1982 erratum at eighth order",
    "MUNSTER_1985_TM / MUNSTER_1981",
)
def _():
    # Both documents were obtained (maintainer-supplied) and read on
    # 2026-08-21, both tables re-read at 200 dpi before transcription. The
    # 1985 effective-transfer-matrix recomputation reproduces the 1982
    # erratum's SU(3) row through u^7 and then shifts m_8 by EXACTLY -96
    # (-3932160/40960); the same table shifts Z3 by -32, SU(infinity) by
    # -18, and U(1)-Wilson by -1/8 at u^6 and -1/6 at u^8, while SU(2), Z2
    # and U(1)-Villain are untouched.
    #
    # The history was then reconstructed from the record (same day): the
    # SU(3) shift is a FOURTH correction round that no erratum ever
    # recorded — Drouffe-Zuber's 1983 review (Phys. Rep. 102, Table 10)
    # already prints -183140613/40960, attributing its table to Seo NPB 209
    # (1982) 200 and Munster PLB 121 (1983) 53, and the 1985 paper agrees;
    # the NPB 205 erratum value is orphaned in the later literature. The
    # SU(infinity), U(1)-Wilson and Z3 shifts are different: DZ 1983 still
    # carries the ERRATUM values there (-546, -445/6, -1659829/2880), so
    # those corrections first appear in 1985 and rest on a single printing.
    # Langelage-Munster-Philipsen 2007 reprints every channel through u^7
    # only. This check asserts the discrepancy so it stays visible; it
    # promotes neither value — every source in the chain shares
    # Munster/Seo provenance, and only an independent recomputation would
    # close it. Euclidean throughout: no certified Hamiltonian quantity is
    # touched either way.
    agree_low = K.MUNSTER_TM_MS[:7] == K.MUNSTER_ERR_MS[:7]
    shift = K.MUNSTER_TM_MS[7] - K.MUNSTER_ERR_MS[7]
    sibling_shifts = tuple(
        tm - err for tm, err in zip(K.MUNSTER_TM_SIB, K.MUNSTER_ERR_SIB, strict=True)
    )
    expected_siblings = (
        Rational(-32),  # Z3 m_8
        Rational(-18),  # SU(infinity) m_8
        Rational(-1, 8),  # U(1)-Wilson m_6
        Rational(-1, 6),  # U(1)-Wilson m_8
    )
    return agree_low and shift == -96 and sibling_shifts == expected_siblings, (
        "SU(3): 1985 Table 1 equals the 1982 erratum row for k = 1..7 and differs "
        f"at k = 8 by {shift} exactly (-183140613/40960 vs -179208453/40960) — a "
        "fourth correction already in print by 1983 (DZ Phys. Rep. 102 Table 10, "
        "citing Seo NPB 209 and Munster PLB 121) that no erratum records; the "
        "registered sibling shifts are asserted too: Z3 m_8 by -32, SU(inf) m_8 "
        "by -18, U(1)-Wilson by -1/8 at u^6 and -1/6 at u^8, all 1985-only (DZ "
        "1983 still carries the erratum values there). The SU(2), Z2 and "
        "U(1)-Villain rows were read as identical in both tables but are not "
        "registered, so this check does not certify them. Recorded, not "
        "adjudicated: every printing shares Munster/Seo provenance"
    )


@published.check(
    "the cap family's signed counts are n x Catalan, the published sewing weights",
    "OBZ_1985 / G5",
)
def _():
    # The completion-family novelty search (docs/referee/novelty_search_
    # 2026-08-21.md) surfaced O'Brien-Zuber 1985: eq. (2.5) attaches signed
    # central binomials (2k)!/(k!)^2 as the weights sewing closed plaquette
    # surfaces at large N, systematizing Kazakov's cyclic contractions. The
    # cellular cap family's signed count is S_n = (-1)^(n-1) C(2n-2, n-1),
    # and C(2m, m) = (m+1) Cat(m) makes that exactly n times a Catalan
    # number -- the same combinatorial family, in print in 1985, in a
    # different limit (N -> infinity, Euclidean free energy) and different
    # dynamics (no resolvents). This check proves the bridge as algebra and
    # anchors it on the enumerated cube; whether the finite-N family is
    # DERIVABLE from those cumulant weights is the open adjudication the
    # novelty record states, and this check decides nothing about it.
    from sympy import Symbol, binomial, catalan, factorial

    n = Symbol("n", positive=True, integer=True)
    # The factorial rewrite is what lets sympy cancel: both sides become
    # (2n-2)!/((n-1)!)^2 exactly.
    identity = simplify((binomial(2 * n - 2, n - 1) - n * catalan(n - 1)).rewrite(factorial))
    _c4, s4, hist4 = CELL.c_prim(CELL.CUBE, *CELL.CAP_SECTOR)
    return identity == 0 and s4 == -20 == (-1) ** 3 * 4 * catalan(3), (
        "C(2n-2, n-1) = n Cat(n-1) identically, so S_n = (-1)^(n-1) n Cat(n-1); "
        f"the enumerated cube instance gives S_4 = {s4} = -4 Cat(3) over "
        f"{len(hist4)} histories -- the completion counts are n times the "
        "Kazakov/O'Brien-Zuber cyclic-contraction Catalan weights"
    )


@published.check("the overlap obstruction was published in 1988, and it scales", "SCHIERHOLZ_1988")
def _():
    # G18 is the largest unpaid debt in the program: the claim that the
    # protected carrier is the glueball. Its own statement records the bare
    # operator carrying under 4% of the physical state -- as a fixed number.
    # Schierholz 1988 measured the same few-percent overlap independently and
    # showed it falls like a^5 for a local dimension-4 operator, which is the
    # class the bare T_1^{+-} operator belongs to. A power law, not a constant:
    # it degrades toward the continuum, so the smeared basis is structural.
    #
    # This check exists so the connection cannot quietly fall out of the ledger.
    from . import ledger as led_mod
    from . import literature as lit_mod

    edges = lit_mod.load().bearing_on("G18")
    schierholz = [e for p, e in edges if p["id"] == "SCHIERHOLZ_1988"]
    g18 = next(g for g in led_mod.load().gaps if g["id"] == "G18")
    sharpening = str(g18.get("external_sharpening", ""))
    return (
        len(schierholz) == 1
        and schierholz[0]["status"] == "verified"
        and "a^5" in sharpening
        and g18.get("load_bearing") is True
    ), (
        "G18 records the bare operator at <4% (2 sigma) as a fixed number; "
        "Schierholz 1988 §2 measures 'a couple of percent' at beta = 5.9 AND "
        "gives the scaling a^5 for a local dimension-4 operator. Independent, "
        "38 years earlier, and it makes the smeared basis structural rather than "
        "a convenience — better statistics cannot recover a power law"
    )


@published.check("a cross-regime paper never supplies a value", "KRS_2023 / §12")
def _():
    # The firewall that corpus §12 states in prose, made binding. KRS_2023 is
    # 1+1 dimensional with dynamical quarks; this program is 3+1 and pure gauge,
    # and the chain complex C_3 -> C_2 -> C_1 does not exist below three spatial
    # dimensions. So the paper is comparable and citable and its numbers are not
    # admissible, and `literature.validate` refuses any entry that mixes the two.
    from . import literature as lit_mod

    lit = lit_mod.load()
    walled = [p for p in lit.papers if str(p.get("scope_firewall", "")).strip()]
    offenders = [
        (p["id"], e["target"])
        for p in walled
        for e in p["bears_on"]
        if e["relation"] == "supplies-value"
    ]
    return bool(walled) and not offenders, (
        f"{len(walled)} indexed paper(s) declare a scope firewall and none supplies "
        f"a value: {[p['id'] for p in walled]}. The rule is enforced in "
        "literature.validate, not just recorded in the entry"
    )


@published.check("stored full text is verbatim, and the licence is checked", "KRS_2023")
def _():
    # Storing a paper is republishing it. One indexed paper is openly licensed
    # enough to store (CC BY-NC-ND); NoDerivatives means the bytes must be the
    # original, so the stored file is hashed against the digest of the copy that
    # was read rather than trusted to be unmodified.
    import hashlib

    from . import literature as lit_mod

    lit = lit_mod.load()
    stored = [p for p in lit.papers if p.get("fulltext")]
    verified = []
    for paper in stored:
        path = lit_mod.LITERATURE_DIR / paper["fulltext"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        licence = str(paper["licence"]).lower()
        ok = digest == paper["source_sha256"] and licence in (
            lit_mod.REDISTRIBUTABLE | lit_mod.VERBATIM_ONLY
        )
        verified.append(ok)
    unstored = len(lit.papers) - len(stored)
    return bool(stored) and all(verified), (
        f"{len(stored)} of {len(lit.papers)} papers are stored, each hash-verified "
        f"against the copy that was read; the other {unstored} are under publisher "
        "copyright or the arXiv assumed-1991-2003 licence and are pinned by digest "
        "without being redistributed"
    )


# ---------------------------------------------------------------------------
# Restored payloads (G1). The ledger said five payload families were "only
# record-backed". The 2026-08-21 sweep found three of them shipped in
# corpus-import/ carrying the exact reference SHAs the records quote; these
# checks bind file, digest, and content to the registry so the claim is
# machine-checked rather than asserted. Two families remain absent, and the
# FINDING checks pin exactly what is missing — including that no reference
# SHA for a tetrahedral certificate exists anywhere, so shipping cannot close
# C15 and only the G5 re-derivation can.

restored = _suite("restored payloads (G1)")


@restored.check(
    "the 189-record kernel is shipped and carries both reference SHAs", "UNIFIED §6 / G1"
)
def _():
    pins = P.corpus_pins()
    rel = str(P.KERNEL.relative_to(P.CORPUS))
    actual = P.sha256_of(P.KERNEL)
    semantic = P.semantic_sha()
    row = P.canonical_rows().get("A20K", {})
    count = len(P.kernel_records())
    ok = (
        count == 189
        and actual == P.KERNEL_FILE_SHA == pins.get(rel) == row.get("sha256")
        and semantic == P.KERNEL_SEMANTIC_SHA
        and P.kernel_is_hermitian()
    )
    return ok, (
        f"{count} records; file sha {actual[:16]}… equals manifest row A20K, the corpus pin, "
        f"and the stage-3J verdict's quote; semantic sha {semantic[:16]}… equals the SOS "
        "certificate's reference; record set exactly Hermitian under (ip,op,d) -> (op,ip,-d)"
    )


@restored.check(
    "the kernel re-derives q, alpha, beta, and the historical C_shp exactly", "UNIFIED §6 / G1"
)
def _():
    c = P.kernel_constants()
    ok = (
        c["gamma_is_scalar"] == 1
        and c["q"] == P.as_fraction(K.Q_BAND_4)
        and c["alpha"] == P.as_fraction(K.ALPHA_PEN_3)
        and c["beta"] == P.as_fraction(K.BETA_PEN_3)
        and c["C_shp"] == P.as_fraction(K.C_SHP_HISTORICAL)
        and c["c_R"] == 2 * c["c_M"] - c["c_X"]
        and c["bandwidth"] == P.as_fraction(K.ALPHA_PEN_3) + P.as_fraction(K.BETA_PEN_3)
    )
    return ok, (
        f"H(Gamma) = q I with q = {c['q']} = q_band^(4); c_X - q = {c['alpha']} = alpha_pen(3); "
        f"2(c_M - c_X) = {c['beta']} = beta_pen_3; (beta - 2 alpha)/16 = {c['C_shp']} = "
        "C_shp (historical); c_R = 2 c_M - c_X (the pencil relation, on the raw records); "
        f"bandwidth = {c['bandwidth']}"
    )


@restored.check(
    "three kernel copies agree record-for-record, from two independent builds", "UNIFIED §6 / G1"
)
def _():
    record_sets = [dict(P.kernel_records(p)) for p in P.KERNEL_COPIES]
    identical = all(rs == record_sets[0] for rs in record_sets[1:])
    upstream = P.stage3i_hashes()
    return identical and len(upstream) == 2, (
        f"{len(P.KERNEL_COPIES)} shipped copies, {len(record_sets[0])} records each, "
        f"record-identical; meta names {len(upstream)} distinct upstream Stage-3I hashes "
        "(one a from-scratch rebuild), so the copies are independent builds of one content"
    )


@restored.check("the Q_32 ledger is the Newton transcript of the compact q law", "UNIFIED §8 / G1")
def _():
    v = P.q32_verification()
    quoted = P.walled_brauer()["q"]
    ok = (
        v["matches"]
        and (v["count"], v["positive"], v["zero"], v["negative"]) == (40, 33, 7, 0)
        and v["ledger_sha"] == quoted["newton_ledger_sha256"]
        and v["note_sha"] == quoted["compact_formula_sha256"]
    )
    return ok, (
        f"all {v['count']} coefficients equal the forward differences of Q32 at z = {v['base']}: "
        f"{v['positive']} positive, {v['zero']} zero tail, {v['negative']} negative; ledger and "
        "formula files hash-match the walled-Brauer certificate's quotes"
    )


@restored.check("the P_402 ledger is the Newton transcript of B_N * D_409", "UNIFIED §8 / G1")
def _():
    v = P.p402_verification()
    quoted = P.walled_brauer()["B"]
    ok = (
        v["matches"]
        and (v["count"], v["positive"], v["zero"], v["negative"]) == (424, 403, 21, 0)
        and v["last_nonzero"] == 402
        and v["ledger_sha"] == quoted["newton_coefficients_sha256"]
        and v["note_sha"] == quoted["structured_expression_sha256"]
    )
    return ok, (
        f"all {v['count']} coefficients equal the forward differences of B_N * D_409(N) at "
        f"N = {v['base']}, with B_N evaluated exactly from the structured 80-term expression: "
        f"{v['positive']} positive, {v['zero']} zero tail, degree {v['last_nonzero']}; ledger "
        "and expression files hash-match the walled-Brauer certificate's quotes"
    )


@restored.check(
    "q_N < 0 and beta_pen_N > 0 for every integer N >= 7 follow from the ledgers", "UNIFIED §8 / G1"
)
def _():
    signs = P.denominator_sign_certificate()
    q = P.q32_verification()
    b = P.p402_verification()
    ok = (
        signs["d34"]
        and signs["d409"]
        and q["negative"] == 0
        and q["positive"] > 0
        and b["negative"] == 0
        and b["positive"] > 0
    )
    return ok, (
        "no D34 factor has a real root at z >= 49 and no D409 factor at N >= 7, all leading "
        "coefficients positive, so both denominators are positive on the stable range; Newton "
        "nonnegativity with a positive lead then gives Q32(N^2) > 0 and P_402(N) > 0, hence "
        f"q_N = -(2/3N) Q32/D34 < 0 and beta_pen_N = P_402/D_409 > 0 for every integer N >= 7 "
        f"({signs['d409_factors']} denominator factors checked exactly)"
    )


@restored.check(
    "the stored fixed-rank q samples N = 7..18 match the compact law exactly", "UNIFIED §8 / C17"
)
def _():
    v = P.fixed_rank_verification()
    ok = v["all_match"] and v["count"] == 12 and v["ranks"] == list(range(7, 19))
    return ok, (
        f"{v['count']} stored samples at N = {v['ranks'][0]}..{v['ranks'][-1]}, each equal to "
        "-(2/3N) Q32(N^2)/D34(N^2) as an exact rational — the machine half of C17's resolution"
    )


@restored.check(
    "the SU(6) determinant correction is exactly 6/343 and momentum-independent",
    "GCSG (Aug 8) / C16",
)
def _():
    from fractions import Fraction

    cert = P.su6()
    balanced, full = cert["balanced_N6"], cert["full_SU6"]
    shifts = {key: Fraction(full[key]) - Fraction(balanced[key]) for key in ("q", "X", "M", "R")}
    unchanged = all(balanced[key] == full[key] for key in ("A", "B", "bandwidth"))
    ok = (
        all(shift == P.as_fraction(K.DELTA_Q_6) for shift in shifts.values())
        and unchanged
        and cert["gates"]["passed"]
        and cert["exceptional_geometry"]["determinant_permutation_terms"] == 720
    )
    return ok, (
        "full_SU6 minus balanced_N6 equals 6/343 at q, X, M, and R while A, B, and the "
        "bandwidth are unchanged — the determinant correction is a scalar shift, re-derived "
        "from the shipped certificate; 720 determinant permutation terms, 11/11 gates"
    )


@restored.check(
    "the SU(5) stage-1 scan is shipped: 895,524 pairs, zero determinant sectors",
    "GCSG (Aug 8) / C16",
)
def _():
    cert = P.stage1()
    geometry = cert["geometry"]
    ok = (
        geometry["candidate_support_output_pairs"] == 895524
        and cert["local_haar"]["epsilon_or_determinant_sectors"] == 0
        and geometry["exact_balance_sign_assignments"] == 33500
        and cert["passed"] is True
    )
    return ok, (
        "895,524 candidate support/output pairs with 0 epsilon-or-determinant sectors — the "
        "recorded SU(5) mod-5 emptiness, from the pinned stage-1 summary; 33,500 exact-balance "
        "sign assignments, passed: true"
    )


@restored.check(
    "FINDING: manifest row A60 names the pentagonal dual-cold bundle, and the tree lacks it",
    "UNIFIED §9.3 / G1",
)
def _():
    bundle = P.canonical_rows().get("A60", {})
    frontier = P.canonical_rows().get("A60F2", {})
    frontier_path = (
        "numerics/certificates/RUN_PENT_pentagonal_o4_minimal_representation_frontier_results.json"
    )
    frontier_shipped = P.corpus_pins().get(frontier_path) == frontier.get("sha256")
    absent = not P.pinned_paths_matching(r"pentagonal_o4_dual_cold")
    ok = (
        bundle.get("sha256") == "f2a8b30de1ba5f23f34c10a3102c42f000ca23f8f7eb1bbfdd9b068bb14da54a"
        and bundle.get("size") == "111743"
        and absent
        and frontier_shipped
    )
    return ok, (
        "the frontier certificate (row A60F2) IS shipped and hash-matched, but the dual-cold "
        "bundle (row A60, 111743 bytes) is not: any restoration must hash to "
        f"{bundle.get('sha256', '?')}; until then h_4^side, A_+, and A_- stay record-backed "
        "and their registry identities are the only machine evidence"
    )


@restored.check(
    "FINDING: no tetrahedral certificate exists, and no reference SHA is recorded for one",
    "corpus THM_FLUX_hodge_cellular_circuit_mobility_theorem.md / C15",
)
def _():
    in_corpus = P.pinned_paths_matching(r"tetrahedr")
    in_manifest = [
        row_id
        for row_id, row in P.canonical_rows().items()
        if "tetrahedr" in (row.get("path", "") + row.get("description", "")).lower()
    ]
    return not in_corpus and not in_manifest, (
        "no pinned path and no canonical-manifest row mentions a tetrahedral artifact, and no "
        "digest for one is recorded anywhere — so C15 cannot be closed by shipping; only the "
        "G5 re-derivation of the claimed -8/(N(N^2-1)) can close it"
    )


# ---------------------------------------------------------------------------
# Coupling erratum (C4/G2). The archived Y = 2*beta/3 = 4u line was a label
# error; the printed coefficients were already canonical-u. G2 asked for "a
# single conversion statement" — here it is as arithmetic: the printed tower
# coefficients written as functions of beta/4 reproduce the printed u-towers
# under u = beta/6 exactly, and would be off by 4^r under the Y reading.

coupling = _suite("coupling erratum (C4/G2)")


def _bridge_towers():
    u, x = symbols("u x")
    minus = Rational(2, 3) + x / 6 + K.TOWER_B2_MINUS * x**2 + K.TOWER_B3_MINUS * x**3
    plus = Rational(2, 3) - x / 6 + K.TOWER_B2_PLUS * x**2 + K.TOWER_B3_PLUS * x**3
    return u, expand(4 * minus.subs(x, 3 * u / 2)), expand(4 * plus.subs(x, 3 * u / 2))


@coupling.check(
    "the printed towers are canonical-u: 4*Delta(3u/2) reproduces them verbatim",
    "UNIFIED §2.1 / C4",
)
def _():
    u, bridge_minus, bridge_plus = _bridge_towers()
    tower_minus = expand(Rational(8, 3) + u + u**2 / 2 + Rational(7, 32) * u**3)
    tower_plus = expand(Rational(8, 3) - u + Rational(13, 20) * u**2 + Rational(101, 200) * u**3)
    ok = bridge_minus == tower_minus and bridge_plus == tower_plus
    return ok, (
        "with b2- = 1/18, b3- = 7/432, b2+ = 13/180, b3+ = 101/2700 as printed, "
        "4*Delta_-(3u/2) = 8/3 + u + u^2/2 + 7/32 u^3 and 4*Delta_+(3u/2) = "
        "8/3 - u + 13/20 u^2 + 101/200 u^3 exactly — both sides printed tables, "
        "consistent only in u = beta/6"
    )


@coupling.check(
    "the 4**r rescaling breaks the bridge: order 2 off by 16, order 3 by 64",
    "UNIFIED §2.1 / C4 / G2",
)
def _():
    u, bridge_minus, _bridge_plus = _bridge_towers()
    rescaled = expand(Rational(8, 3) + u / 4 + u**2 / 32 + Rational(7, 2048) * u**3)
    ratio2 = bridge_minus.coeff(u, 2) / rescaled.coeff(u, 2)
    ratio3 = bridge_minus.coeff(u, 3) / rescaled.coeff(u, 3)
    ok = bridge_minus != rescaled and ratio2 == 16 and ratio3 == 64
    return ok, (
        f"reading the archived Y = 4u line as a coordinate would demand coefficient_r/4^r; "
        f"the printed table differs from that by exactly {ratio2} at u^2 and {ratio3} at u^3 "
        "— the single conversion statement G2 asked for, as arithmetic"
    )


# ---------------------------------------------------------------------------
# Tetrahedral Haar-resolvent coefficient (G5/C15). The corpus asserts the
# r = 2 row of its primitive completion law with no artifact and no reference
# SHA anywhere (the restored-payloads FINDING pins the absence), so C15 can
# only close by re-derivation. workhouse.cellular reconstructs the law's three
# stated ingredients — the 1/N merge from the fundamental-pair Haar moment,
# the certified electric convention E(L) = L*C_F/2, and exhaustive temporal
# orderings over the cell's faces — and these checks first prove the
# reconstruction against every instance the corpus certifies or prints
# (sealed-core cube, prism 64 and its superseded-sector 24, pentagonal
# "120 histories, S_5 = 70", the notebook's Catalan cap family), and only then
# read the same convention at r = 2. Scope: primitive simple-loop channel, as
# the law itself is scoped; physical survival after compression/Q-projection
# is U3's question and is NOT asserted here.

tetra = _suite("tetrahedral Haar-resolvent coefficient (G5)")


@tetra.check("the law's two printed forms are one identity, scaling N^-(2r-1)", "transcript ~148")
def _():
    n, s = symbols("N S", positive=True)
    cf = (n**2 - 1) / (2 * n)
    gaps = [
        simplify(s / (n**r * cf ** (r - 1)) - 2 ** (r - 1) * s / (n * (n**2 - 1) ** (r - 1)))
        for r in range(2, 6)
    ]
    tails = [limit(K.c_prim_printed(r) * K.N ** (2 * r - 1), K.N, "oo") for r in range(2, 6)]
    ok = all(g == 0 for g in gaps) and tails == [-8, 64, -160, 1120]
    return ok, (
        f"S/(N^r C_F^(r-1)) - 2^(r-1) S/(N(N^2-1)^(r-1)) = {gaps} for r = 2..5 with "
        f"C_F = (N^2-1)/(2N); N^(2r-1) c_r -> {tails}, the printed N^-(2r-1) scaling"
    )


@tetra.check("a merge contributes exactly 1/N at every shared-path length", "transcript ~136")
def _():
    # The law's r = 1 content. The only group integral in the primitive channel
    # is the fundamental-pair moment, whose coefficient is the n = 1 Weingarten
    # value 1/N — the inverse of the 1x1 Gram matrix [N], the same Gram-inverse
    # route the published-comparisons suite walks at n = 2. Contracting
    # Tr(A u_1..u_k) Tr(B u_k~..u_1~) link by link then yields (1/N) Tr(AB)
    # for every k: each contraction pays 1/N and every non-final one closes a
    # colour loop worth N. The upstream notebook assumes this flat 1/N; here it
    # is derived. k runs to 4, one past the longest shared path any history in
    # the five enumerated cells uses.
    wg1 = CELL.weingarten_1()
    moments = [CELL.merge_moment(k) for k in range(1, 5)]
    ok = wg1 == 1 / CELL.N and all(
        coeff == 1 / CELL.N and rest in ([["A", "B"]], [["B", "A"]]) for coeff, rest in moments
    )
    return ok, (
        f"Wg_1 = {wg1}; contraction of the k-link shared path gives "
        f"{[str(c) for c, _ in moments]} times Tr(AB) for k = 1..4 — "
        "(1/N)^k from the pair moments times N^(k-1) closed colour loops"
    )


@tetra.check("the resolvent unit is the certified electric convention", "v4.3 §9.3 / §4.4")
def _():
    # E(L) = L*C_F/2 is not a new convention: at N = 3 it is the certified
    # pentagonal pair E_SIDE and E_CAP, and its L = 4 value is the certified
    # one-plaquette rest energy e_flat(0) = 8/3. The registered
    # electric_energy function is the single home; this check binds it to the
    # certified values AND to cellular's C_F-unit resolvent denominators.
    energy = K.electric_energy
    cf = (K.N**2 - 1) / (2 * K.N)
    cellular_unit = simplify((energy(3) - energy(4)) / cf)  # tetra denominator
    ok = (
        energy(4, 3) == K.E_SIDE
        and energy(5, 3) == K.E_CAP
        and energy(4, 3) == K.e_flat(0)
        and simplify(energy(4) - (K.N**2 - 1) / K.N) == 0
        and cellular_unit == Rational(-1, 2)
    )
    return ok, (
        f"L*C_F/2 at N = 3: E(4) = {energy(4, 3)} = E_SIDE = e_flat(0), "
        f"E(5) = {energy(5, 3)} = E_CAP; symbolically E(4) = 2 C_F = (N^2-1)/N; and "
        f"(E(3) - E(4))/C_F = {cellular_unit} — exactly cellular's (l_0 - l)/2 "
        "denominator for the tetrahedral intermediate"
    )


@tetra.check("the cube instance re-derives the sealed core, temporal classes included", "818 ~3963")
def _():
    c4, s4, hist = CELL.c_prim(CELL.CUBE, *CELL.CAP_SECTOR)
    classes = {}
    for h in hist:
        key = (h.lengths, h.weight_e0(4))
        classes[key] = classes.get(key, 0) + 1
    expected = {((6, 6, 6), -8): 16, ((6, 8, 6), -4): 8}
    ok = (
        s4 == -20
        and classes == expected
        and simplify(c4 - K.c_prim_printed(4)) == 0
        and c4.subs(CELL.N, 3) == K.CUBE_COMPLETION_4
        and simplify(4 * (-c4) - K.alpha_pen()) == 0
        and 4 * abs(c4.subs(CELL.N, 3)) == K.ALPHA_PEN_3
    )
    return ok, (
        f"24 orderings; per-history amplitudes in E_0 units {dict(classes)} — the corpus's "
        "three multiplicity-8 classes (-8, -8, -4) with the (6,6,6) class split 8+8; "
        f"S_4 = {s4}, c_4 = {c4} -> {c4.subs(CELL.N, 3)} = CUBE_COMPLETION_4, and "
        f"4|c_4| = alpha_pen(N), = {K.ALPHA_PEN_3} at N = 3 — the sealed core, sign included"
    )


@tetra.check("the prism square sector re-derives the printed 64/(N(N^2-1)^2)", "THM_FLUX §3.2")
def _():
    values = set()
    for p in range(2, 5):
        for q in range(2, 5):
            if p != q:
                c3, s3, hist = CELL.c_prim(CELL.TRIANGULAR_PRISM, p, q)
                values.add((c3, s3, len(hist)))
    (c3, s3, count), *rest = values
    su3 = c3.subs(CELL.N, 3)
    ok = (
        not rest
        and s3 == 16
        and count == 6
        and simplify(c3 - K.c_prim_printed(3)) == 0
        and su3 == K.PRISM_COMPLETION_3_SU3
        and 6 * su3 == K.PRISM_BANDWIDTH_3_SU3
    )
    return ok, (
        f"all 6 ordered square pairs agree: 6 histories each, S_3 = {s3}, c_3 = {c3} "
        f"-> {su3} at N = 3, and the printed third-order bandwidth 6 c_3(3) = {6 * su3}"
    )


@tetra.check("24 and 64 are different endpoint sectors of one prism, not rivals", "818 ~3402")
def _():
    # The shipped notebook gates +24/(N(N^2-1)^2) (1/8 at SU(3)) for the
    # triangular prism; the corpus's table prints 64. Both come out of this one
    # engine: 24 is the cap-to-cap completion, 64 the square-to-square one the
    # retained vertical-square sector actually uses. 818.txt records the
    # supersession of 24 by 64 as the sector choice — an ADR-0002-style
    # dissolution, not an arithmetic conflict.
    cap, s_cap, hist_cap = CELL.c_prim(CELL.TRIANGULAR_PRISM, *CELL.CAP_SECTOR)
    square, s_sq, _ = CELL.c_prim(CELL.TRIANGULAR_PRISM, *CELL.SQUARE_SECTOR)
    ok = (
        s_cap == 6
        and len(hist_cap) == 6
        and simplify(cap - CELL.catalan_cap_coefficient(3)) == 0
        and cap.subs(CELL.N, 3) == K.PRISM_CAP_COMPLETION_3_SU3
        and s_sq == 16
        and simplify(square - K.c_prim_printed(3)) == 0
    )
    return ok, (
        f"cap sector: S = {s_cap}, c = {cap} -> {cap.subs(CELL.N, 3)} at N = 3, the notebook's "
        f"gated value; square sector: S = {s_sq}, c = {square} -> "
        f"{square.subs(CELL.N, 3)}, the printed table row — same cell, same convention"
    )


@tetra.check("the n-gonal cap family is Catalan; the pentagonal row is n = 5", "transcript ~175")
def _():
    from sympy import binomial

    rows = {}
    for sides in range(3, 7):
        cell = CELL.prism(sides)
        c, s, hist = CELL.c_prim(cell, *CELL.CAP_SECTOR)
        rows[sides] = (s, len(hist), simplify(c - CELL.catalan_cap_coefficient(sides)) == 0)
    counts_ok = all(
        rows[n][0] == (-1) ** (n - 1) * binomial(2 * n - 2, n - 1) and rows[n][2]
        for n in range(3, 7)
    )
    c5, s5, hist5 = CELL.c_prim(CELL.PENTAGONAL_PRISM, *CELL.CAP_SECTOR)
    ok = (
        counts_ok
        and (s5, len(hist5)) == (70, 120)
        and simplify(c5 - K.c_prim_printed(5)) == 0
        and c5.subs(CELL.N, 5 - 2) == K.PENT_COMPLETION_5_SU3
    )
    return ok, (
        f"S_n for n = 3..6: {[rows[n][0] for n in range(3, 7)]} = (-1)^(n-1) C(2n-2, n-1), "
        f"the shipped notebook's closed family; the pentagonal instance is the transcript's "
        f"'120 histories, S_5 = 70' with c_5 = {c5} -> {c5.subs(CELL.N, 3)} at N = 3"
    )


@tetra.check(
    "the run-length Catalan factorization holds for every proper subset through n = 7",
    "cellular brief, appendix A",
)
def _():
    # The lemma behind Theorem 2's closed form for ALL n (appendix A of the
    # referee brief): for any proper subset T of the n-site cycle, the chain
    # sum F(T) = sum over insertion orders of prod_k 1/blocks(T_k) equals the
    # product of Catalan numbers over T's cyclic run lengths. Verified here
    # with nothing assumed: F is computed by its definitional recursion
    # F(T) = (1/blocks(T)) sum_{x in T} F(T-x) over the whole subset lattice,
    # cross-checked against literal enumeration of every |T|! ordering for
    # n <= 5, and compared to the Catalan product for every proper T, n <= 7.
    from itertools import permutations

    from sympy import Integer, binomial

    def catalan(m):
        return binomial(2 * m, m) / (m + 1)

    def blocks(mask, n):
        if mask == 0:
            return 0
        if mask == (1 << n) - 1:
            return 1
        return sum(1 for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1)

    def run_lengths(mask, n):
        starts = [i for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1]
        lengths = []
        for start in starts:
            length, i = 0, start
            while mask >> i & 1:
                length, i = length + 1, (i + 1) % n
            lengths.append(length)
        return lengths

    def chain_dp(n):
        f = {0: Integer(1)}
        for mask in sorted(range(1, 1 << n), key=lambda m: bin(m).count("1")):
            if mask == (1 << n) - 1:
                continue
            total = sum(f[mask & ~(1 << i)] for i in range(n) if mask >> i & 1)
            f[mask] = total / blocks(mask, n)
        return f

    factorization_ok, brute_ok = True, True
    for n in range(3, 8):
        f = chain_dp(n)
        for mask, value in f.items():
            if mask:
                product = Integer(1)
                for length in run_lengths(mask, n):
                    product *= catalan(length)
                factorization_ok &= value == product
        if n <= 5:
            for mask in list(f):
                if not mask:
                    continue
                sites = [i for i in range(n) if mask >> i & 1]
                brute = sum(_chain_product(order, n) for order in permutations(sites))
                brute_ok &= brute == f[mask]
    return factorization_ok and brute_ok, (
        "F(T) computed by the definitional lattice recursion equals the product of "
        "Catalan numbers over T's cyclic run lengths for every proper subset of "
        "Z_n, n = 3..7 (376 subsets), and equals the literal all-orderings sum "
        "for every subset at n <= 5 — the lemma the 1/blocks resolvent weight "
        "makes true by absorbing one Catalan convolution per run"
    )


def _chain_product(order, n):
    """Product of 1/blocks over every prefix of one insertion order.

    Every prefix, the full subset included — matching F's definition; the
    full-cycle case (blocks = 1 by convention) cannot arise because F is only
    brute-forced on proper subsets.
    """
    from sympy import Integer

    mask, product = 0, Integer(1)
    for site in order:
        mask |= 1 << site
        count = sum(1 for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1)
        product /= count
    return product


@tetra.check(
    "Theorem 2's closed form holds through n = 9, past the engine's exhaustive range",
    "cellular brief, appendix A",
)
def _():
    # Appendix A's theorem: splitting the cap-sector ordering sum by its last
    # insertion gives A(n) = n * F(arc of n-1 sites) = n * Catalan(n-1)
    # = C(2n-2, n-1), so S_n = (-1)^(n-1) C(2n-2, n-1) for every n. The
    # subset-lattice DP reaches n = 9 in milliseconds where the engine's
    # history enumeration (checked to n = 6 above) could not, and the
    # resulting c_prim matches the brief's closed coefficient symbolically.
    from sympy import Integer, binomial, simplify

    def blocks(mask, n):
        if mask == (1 << n) - 1:
            return 1
        return sum(1 for i in range(n) if mask >> i & 1 and not mask >> (i - 1) % n & 1)

    closed_ok, coeff_ok = True, True
    for n in range(2, 10):
        f = {0: Integer(1)}
        for mask in sorted(range(1, 1 << n), key=lambda m: bin(m).count("1")):
            if mask == (1 << n) - 1:
                continue
            total = sum(f[mask & ~(1 << i)] for i in range(n) if mask >> i & 1)
            f[mask] = total / blocks(mask, n)
        full = (1 << n) - 1
        a_n = sum(f[full & ~(1 << x)] for x in range(n))
        closed_ok &= a_n == binomial(2 * n - 2, n - 1)
        s_n = Integer(-1) ** (n - 1) * a_n
        c_closed = 2 ** (n - 1) * s_n / (CELL.N * (CELL.N**2 - 1) ** (n - 1))
        coeff_ok &= simplify(c_closed - CELL.catalan_cap_coefficient(n)) == 0
    return closed_ok and coeff_ok, (
        "A(n) from the subset-lattice DP equals C(2n-2, n-1) for n = 2..9 "
        "(2, 6, 20, 70, 252, 924, 3432, 12870), and the signed count assembles "
        "into the brief's closed coefficient symbolically at every n — the cap "
        "family is now a theorem for all n, with instances n <= 6 still "
        "independently exhausted by the history engine above"
    )


@tetra.check("the primitive sign is the resolvent parity", "quarantined master v3 erratum 9")
def _():
    # Every intermediate loop in every admissible history of all five cells is
    # LONGER than the endpoint face, so all r-1 denominators are negative and
    # sign(S_r) = (-1)^(r-1). That is exactly the (-1)^(r+1) the quarantined
    # master v3 bolts onto its unsigned counts as erratum 9 — corroboration
    # from a document this repository never treats as current; the sign here
    # comes from the derivation, anchored by the even-order certified cube row.
    cells = [
        (CELL.TETRAHEDRON, 0, 1),  # any pair; face-transitive
        (CELL.TRIANGULAR_PRISM, *CELL.SQUARE_SECTOR),
        (CELL.CUBE, *CELL.CAP_SECTOR),
        (CELL.PENTAGONAL_PRISM, *CELL.CAP_SECTOR),
    ]
    all_longer, signed = True, []
    for cell, p, q in cells:
        s, hist = CELL.s_value(cell, p, q)
        ell = len(cell.faces[p])
        all_longer &= all(length > ell for h in hist for length in h.lengths)
        signed.append(s)
    unsigned = [abs(s) for s in signed]
    parity = [(-1) ** (r - 1) * u for r, u in zip(range(2, 6), unsigned, strict=True)]
    ok = all_longer and signed == parity and unsigned == [4, 16, 20, 70]
    return ok, (
        f"signed S_r = {signed}; every intermediate exceeds the endpoint length, so "
        f"S_r = (-1)^(r-1) |S_r| with |S_r| = {unsigned} — the quarantined master's "
        "unsigned counts (4, 16, 20, 70) and its erratum-9 sign, derived not asserted"
    )


@tetra.check("G5: the tetrahedral coefficient is exactly -8/(N(N^2-1))", "transcript ~170 / C15")
def _():
    results = set()
    for p in range(4):
        for q in range(4):
            if p != q:
                c2, s2, hist = CELL.c_prim(CELL.TETRAHEDRON, p, q)
                results.add((c2, s2, len(hist), tuple(h.lengths for h in hist)))
    (c2, s2, count, lengths), *rest = results
    su3 = c2.subs(CELL.N, 3)
    ok = (
        not rest
        and s2 == -4
        and count == 2
        and lengths == ((4,), (4,))
        and simplify(c2 - K.c_prim_printed(2)) == 0
        and su3 == K.TETRA_COMPLETION_2_SU3
    )
    return ok, (
        f"all 12 ordered endpoint pairs agree: 2 histories each, the single intermediate is "
        f"always the 4-link loop (denominator -C_F/2, i.e. weight -2 per history), "
        f"S_2 = {s2}, c_2 = {c2} -> {su3} at N = 3 — exactly the value C15 records as "
        "asserted-without-artifact; primitive channel only, per the law's own scope"
    )


@tetra.check("the tetrahedral circuit attains its bound with nonzero weight", "THM_FLUX §2 / C6")
def _():
    # The survival gate the mobility theorem asked this calculation to test:
    # the tetrahedron's B_2 has the unique primitive circuit (1,1,1,1), so
    # w_min = 4 and the scoped bound r >= w_min - 2 (C6's survivor) allows
    # r = 2 — and the primitive local weight at that order is nonzero at every
    # rank, so circuit allowance is matched by Haar survival in this third
    # geometry. Compression and Q-projection survival are NOT asserted: that
    # is U3's question.
    kernel = CELL.integer_kernel(CELL.TETRAHEDRON)
    w_min = min(sum(abs(x) for x in v) for v in kernel)
    c2 = K.c_prim_printed(2)
    negative = all(c2.subs(K.N, n) < 0 for n in range(2, 13))
    from sympy import together

    numerator, denominator = together(c2).as_numer_denom()
    ok = kernel == [(1, 1, 1, 1)] and w_min == 4 and w_min - 2 == 2 and negative and numerator == -8
    return ok, (
        f"ker_Z B_2 = {kernel}: one primitive unit-coefficient circuit, w_min = {w_min}, "
        f"r = 2 = w_min - 2; c_2 = -8/{denominator} < 0 for all N >= 2 (checked exactly at "
        "N = 2..12, and the numerator is the constant -8), so the r = 2 allowance carries "
        "nonzero primitive Haar-resolvent weight — the falsification test the theorem "
        "proposed did not kill the coefficient"
    )


@tetra.check("primitive proper returns are scalar on the tetrahedral face space", "U3 (partial)")
def _():
    # The U3-adjacent statement this engine CAN settle. A second-order proper
    # return is p -> merged loop -> p: one insertion, then its removal. In the
    # primitive channel each face p has one such history per other face f,
    # with the same 1/N^2 merge weight and the same resolvent, so the return
    # operator on the four-dimensional face space is computed here entry by
    # entry. It comes out exactly scalar: primitive proper returns renormalize
    # the tetrahedral rest energy and are structurally incapable of shape
    # dispersion (the traceless compression annihilates every scalar). This is
    # a primitive-level data point ONLY — U3's pentagonal precedent is the
    # vanishing of 28 histories individually after exact Q projection, and the
    # Fierz/quotient layer needed to ask that question of the tetrahedron is
    # not built here. The Q-projected third data point stays open.
    per_face = {}
    for p in range(4):
        total = Rational(0)
        ell = len(CELL.TETRAHEDRON.faces[p])
        for f_idx, face in enumerate(CELL.TETRAHEDRON.faces):
            if f_idx == p:
                continue
            loop, _shared = CELL._merge(list(CELL._face_edges(CELL.TETRAHEDRON.faces[p])), face)
            total += Rational(2, ell - len(loop))
        per_face[p] = total
    scalar = set(per_face.values())
    c_ret = simplify(next(iter(scalar)) / (K.N**2 * (K.N**2 - 1) / (2 * K.N)))
    ok = scalar == {-6} and simplify(c_ret + 12 / (K.N * (K.N**2 - 1))) == 0
    return ok, (
        f"per-face return sums {list(per_face.values())}: all four faces give -6 in C_F "
        f"units (three 4-link returns at weight -2 each), so the return operator is "
        f"{c_ret} times the identity and its traceless compression is 0 — shape-inert at "
        "the primitive level; the Q-projected analogue of the pentagonal 28-history "
        "vanishing remains uncomputed, so U3 gains a consistent partial point, not a verdict"
    )


# ==========================================================================
notes_prog = _suite("notes program: SAFE, Davies, coercivity (G20-G23)")


@notes_prog.check(
    "G21 exponent identity: arcosh(1 + 2x^2) = 2 arsinh(x)",
    "notes review 2026-08-22 / G21",
)
def _():
    from sympy import acosh, asinh, cosh, expand_trig

    x = symbols("x", positive=True)
    # acosh is monotone on [1, oo) and 2 asinh(x) >= 0, so the identity holds
    # iff cosh(2 asinh(x)) = 1 + 2x^2 — which is the double-angle formula
    # cosh(2t) = 1 + 2 sinh(t)^2 evaluated at t = asinh(x). sympy closes that
    # form directly where the acosh difference resists simplification.
    residual = simplify(expand_trig(cosh(2 * asinh(x))) - (1 + 2 * x**2))
    small = series(acosh(1 + 2 * x**2), x, 0, 2).removeO()
    return residual == 0 and simplify(small - 2 * x) == 0, (
        f"cosh(2 asinh x) - (1+2x^2) = {residual} with both sides' arguments nonnegative, "
        f"so acosh(1+2x^2) = 2 asinh(x); leading order {small} = 2x, "
        "so the Davies exponent is O(m), not O(m^2) — the identity the G21 bound rides on"
    )


@notes_prog.check(
    "V_Haar Hessian at the identity is exactly I/4 (adjoint Casimir 3)",
    "notes review 2026-08-22 / G20",
)
def _():
    from sympy import I as i_unit
    from sympy import im, trace

    # Gell-Mann matrices, exact; T_a = i lambda_a / 2 is orthonormal under
    # <A,B> = -2 Re Tr(AB) — the archive code's own normalization.
    s3 = sqrt(3)
    lam = [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -i_unit, 0], [i_unit, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -i_unit], [0, 0, 0], [i_unit, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -i_unit], [0, i_unit, 0]]),
        Matrix([[1 / s3, 0, 0], [0, 1 / s3, 0], [0, 0, -2 / s3]]),
    ]
    T = [i_unit * m / 2 for m in lam]

    def inner(a: Matrix, b: Matrix):
        return simplify(-2 * ((trace(a * b)) - i_unit * im(trace(a * b))))

    ortho = all(inner(T[a], T[b]) == (1 if a == b else 0) for a in range(8) for b in range(8))
    f = {}
    for a in range(8):
        for b in range(8):
            comm = T[a] * T[b] - T[b] * T[a]
            for c in range(8):
                v = inner(comm, T[c])
                if v != 0:
                    f[(a, b, c)] = v
    # Adjoint Casimir: sum_cd f_acd f_bcd = 3 delta_ab, so -tr(ad_X^2) = 3|x|^2,
    # log J = -sum theta_k^2 / 24 + O(4), V_Haar = |x|^2 * (3/24) = |x|^2 / 8.
    casimir_ok = True
    for a in range(8):
        for b in range(8):
            s = sum(f.get((a, c, d), 0) * f.get((b, c, d), 0) for c in range(8) for d in range(8))
            if simplify(s - (3 if a == b else 0)) != 0:
                casimir_ok = False
    coeff = Rational(3, 24)
    ok = ortho and casimir_ok and coeff == Rational(1, 8) and 2 * coeff == Rational(1, 4)
    return ok, (
        "T_a orthonormal under -2ReTr; sum_cd f_acd f_bcd = 3 delta_ab exactly, so "
        "-tr(ad_X^2) = 3|x|^2 and V_Haar = |x|^2/8 + O(|x|^4): Hessian(0) = I/4. This is "
        "the only well-defined constant in the SAFE ledger, and it equals 1/4 — not the "
        "draft's 0.291 (a reverse-fitted normalization artifact, see the notes register)"
    )


@notes_prog.check(
    "FINDING: the alpha^n RG iteration contradicts its own one-step bound",
    "notes review 2026-08-22 / G20",
)
def _():
    kappa, delta = Rational(1, 4), Rational(6, 1000)
    alpha = 1 - delta / kappa
    subtractive_100 = kappa - 100 * delta
    multiplicative_100 = alpha**100 * kappa
    ok = (
        alpha == Rational(122, 125)
        and subtractive_100 == Rational(-7, 20)
        and subtractive_100 < 0 < multiplicative_100
    )
    return ok, (
        f"one-step bound is subtractive (kappa - delta), so 100 steps give "
        f"kappa - 100 delta = {subtractive_100} < 0 (zero crossed at step "
        f"{kappa / delta} = 41.67); the boxed multiplicative form alpha = {alpha} gives "
        f"alpha^100 kappa = {float(multiplicative_100):.4f} > 0 forever. The two are "
        "inconsistent and no archive document derives the multiplicative one"
    )


@notes_prog.check(
    "FINDING: six bounded vectors in R^3 refute the 6-vs-3 Cartan counting",
    "notes review 2026-08-22 / G22",
)
def _():
    e1, e2, e3 = Matrix([1, 0, 0]), Matrix([0, 1, 0]), Matrix([0, 0, 1])
    six = [e1, -e1, e2, -e2, e3, -e3]
    total = sum(six, zeros(3, 1))
    span = Matrix.hstack(*six).rank()
    ok = total == zeros(3, 1) and span == 3
    return ok, (
        "three orthogonal antipodal unit pairs: sum = 0 with the six directions spanning "
        "all of R^3 (rank 3) — zero force with no common Cartan direction, so 'small sum "
        "implies near-alignment' is false for six vectors, and stationarity at a link is 3 "
        "scalar equations, not 6. G22's conjecture must rest on gauge coupling, not this "
        "counting"
    )


@notes_prog.check(
    "center elements are critical points of Re Tr, with exact heights",
    "notes review 2026-08-22 / G20",
)
def _():
    from sympy import I as i_unit
    from sympy import cos, re

    a, b, c = symbols("a b c")
    x2 = Matrix([[a, b], [c, -a]])  # generic traceless 2x2
    d_su2 = simplify(re((-eye(2) * x2).trace()))
    phi_su2 = 1 - Rational(1, 2) * re((-eye(2)).trace())
    om = cos(2 * pi / 3) + i_unit * sin(2 * pi / 3)
    x3 = Matrix(3, 3, lambda r, s: symbols(f"y{r}{s}"))
    x3[2, 2] = -x3[0, 0] - x3[1, 1]  # traceless
    d_su3 = simplify((om * x3).trace())
    phi_su3 = simplify(1 - Rational(1, 3) * re(3 * om))
    ok = (
        d_su2 == 0
        and phi_su2 == 2
        and simplify(d_su3 - om * (x3[0, 0] + x3[1, 1] + x3[2, 2])) == 0
        and phi_su3 == Rational(3, 2)
    )
    return ok, (
        f"d/dt ReTr(-I e^(tX))|_0 = -ReTr(X) = 0 for traceless X, phi(-I) = {phi_su2} "
        f"(SU(2)); Tr(omega X) = omega TrX = 0, phi(omega I) = {phi_su3} (SU(3)) — the "
        "center sectors are large-height critical points, so the action-built Lyapunov "
        "candidates genuinely fail there; the universal impossibility claim stays out"
    )


@notes_prog.check(
    "G21 Davies bound verified on the 3x3 periodic 2D lattice, arb-certified",
    "notes review 2026-08-22 / G21",
    tier=2,
)
def _():
    # M = m^2 I + d1^T d1 on 1-forms of the 3x3 periodic square lattice
    # (m^2 = alpha = 1), G = M^-1 exact; assert |G(b,b')| < (2/m^2) e^{-eta d}
    # for every pair, with eta = arcosh(1 + m^2/(2 alpha D_E)) evaluated in
    # certified ball arithmetic (ADR 0010) — the comparison is provable, not
    # approximate.
    from . import rigor

    L = 3
    links = [(x, y, mu) for x in range(L) for y in range(L) for mu in (0, 1)]
    idx = {b: i for i, b in enumerate(links)}
    plaqs = [(x, y) for x in range(L) for y in range(L)]
    d1 = zeros(len(plaqs), len(links))
    for p, (x, y) in enumerate(plaqs):
        d1[p, idx[(x, y, 0)]] += 1
        d1[p, idx[((x + 1) % L, y, 1)]] += 1
        d1[p, idx[(x, (y + 1) % L, 0)]] -= 1
        d1[p, idx[(x, y, 1)]] -= 1
    M = eye(len(links)) + d1.T * d1
    G = M.inv()

    # link graph: adjacent iff they co-bound a plaquette
    co = {i: set() for i in range(len(links))}
    for p in range(len(plaqs)):
        members = [i for i in range(len(links)) if d1[p, i] != 0]
        for i in members:
            for j in members:
                if i != j:
                    co[i].add(j)
    d_e = max(len(v) for v in co.values())

    def bfs(src: int) -> dict[int, int]:
        dist, frontier = {src: 0}, [src]
        while frontier:
            nxt = []
            for u in frontier:
                for v in co[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        nxt.append(v)
            frontier = nxt
        return dist

    eta = rigor.ball(1) + rigor.ball(Rational(1, 2 * d_e))
    eta = eta.acosh()
    worst = None
    certified = True
    for i in range(len(links)):
        dist = bfs(i)
        for j in range(len(links)):
            ratio = abs(rigor.ball(G[i, j])) / (rigor.ball(2) * (-eta * dist[j]).exp())
            if not rigor.certified_lt(ratio, rigor.ball(1)):
                certified = False
            if worst is None or float(ratio.mid()) > float(worst.mid()):
                worst = ratio
    return certified and d_e == 6, (
        f"18 links, D_E = {d_e}, eta = {rigor.describe(eta)}; every |G(b,b')| is provably "
        f"below (2/m^2) e^(-eta dist) in 128-bit ball arithmetic, worst ratio "
        f"{rigor.describe(worst)} — the review's 6x6 margin (<= 0.31) reproduced here as a "
        "standing certified check at m^2 = alpha = 1"
    )


@notes_prog.check(
    "one-step bridge spectral lemma: inf over the orthocomplement is 1 - lambda_1",
    "notes review 2026-08-22 / G23 (Exciting_03 Lemma 3.1)",
)
def _():
    # T = e^{-aH} on a finite spectrum, exactly: with T = diag(1, t1, t2),
    # 1 > t1 >= t2 > 0 and Omega the first basis vector, the constrained
    # infimum of <psi,(I-T)psi> over psi perp Omega, |psi| = 1, is 1 - t1.
    t1, t2 = Rational(3, 4), Rational(1, 5)
    a, b = symbols("a b", real=True)
    psi = Matrix([0, a, b])
    q = expand((psi.T * (eye(3) - Matrix.diag(1, t1, t2)) * psi)[0, 0])
    # q = (1-t1) a^2 + (1-t2) b^2 with a^2 + b^2 = 1: minimum at b = 0.
    at_min = q.subs({a: 1, b: 0})
    general = expand(q - ((1 - t1) * (a**2 + b**2) + ((1 - t2) - (1 - t1)) * b**2))
    ok = at_min == 1 - t1 and general == 0 and (1 - t2) - (1 - t1) > 0
    return ok, (
        f"q = (1-t1)(a^2+b^2) + (t1-t2) b^2 exactly, so inf = 1 - t1 = {1 - t1} at the "
        "second eigenvector -- the verified spectral lemma that reduces G23's bridge to "
        "the single bottleneck inequality (4.3)"
    )


@notes_prog.check(
    "FINDING: the naive diffusion-to-OS bridge fails in the Gaussian model",
    "notes review 2026-08-22 / G23 (06_toy)",
    tier=2,
)
def _():
    from . import rigor

    # 1D Gaussian chain: lambda_diff = m^2, exact transfer gap
    # omega = arccosh(1 + m^2/2). Naive bridge claims Delta >= lambda_diff.
    # At m^2 = 4: omega = arccosh(3) < 4 -- certified strict violation.
    # At m^2 = 1/4: omega/lambda ~ 1.98 -- the ratio is not constant, and
    # omega tracks sqrt(lambda) (continuum dispersion), the toy's point.
    om4 = rigor.ball(3).acosh()
    om_quarter = (rigor.ball(1) + rigor.ball(Rational(1, 8))).acosh()
    violated = rigor.certified_lt(om4, rigor.ball(4))
    also_below_sqrt = rigor.certified_lt(om4, rigor.ball(2))
    ratio_small_m = om_quarter / rigor.ball(Rational(1, 4))
    near_two = rigor.certified_lt(abs(ratio_small_m - 2), rigor.ball(Rational(3, 100)))
    return violated and also_below_sqrt and near_two, (
        f"at m^2 = 4 the exact transfer gap arccosh(3) = {rigor.describe(om4)} is provably "
        f"below lambda_diff = 4 (and below sqrt = 2); at m^2 = 1/4 the ratio omega/lambda = "
        f"{rigor.describe(ratio_small_m)} ~ 2, not 1 -- Delta >= lambda_diff is false and "
        "the true scaling is the square root, exactly as the archive's toy note states"
    )


@notes_prog.check(
    "FINDING: the localization error is n-independent, so the boxed gap does not follow",
    "notes review 2026-08-22 / G23 (iter2 8.2 -> 9.3)",
    tier=2,
)
def _():
    from . import rigor

    # iter2's unconditional covariance bound is e^{-eta n} + 8|F||G| mu(K^c).
    # The second term does not decay in n: with mu(K^c) = 10^-6, eta = 1/2,
    # unit norms, the bound plateaus at 8e-6 while pure decay at n = 50 is
    # e^{-25} -- certified orders below the plateau. Hence (9.3)'s
    # "for all n >= n_0" extraction fails as written.
    plateau = rigor.ball(Rational(8, 10**6))
    decay_50 = (-rigor.ball(25)).exp()
    ok = rigor.certified_lt(decay_50, plateau)
    return ok, (
        f"e^-25 = {rigor.describe(decay_50)} is provably below the n-independent plateau "
        f"8 mu(K^c) = {rigor.describe(plateau)}: from n ~ 28 the localization error "
        "dominates, so exponential decay in n -- and with it the boxed gap(H) >= eta/a -- "
        "does not follow from (8.2); only 'spectral mass below eta/a is O(mu(K^c))' does"
    )


@notes_prog.check(
    "FINDING: the curvature-mass fit is the placeholder dataset fitted to itself",
    "notes review 2026-08-22 / TENSOR_NETWORK contamination chain",
)
def _():
    # The template's "(EDIT)" placeholder arrays, transcribed exactly; the
    # "results you reported" downstream are the template run on these very
    # numbers. Exact rational least squares through the origin pins it.
    mu = [
        Rational(92, 100),
        Rational(81, 100),
        Rational(74, 100),
        Rational(68, 100),
        Rational(63, 100),
    ]
    m = [
        Rational(88, 100),
        Rational(78, 100),
        Rational(71, 100),
        Rational(66, 100),
        Rational(61, 100),
    ]
    k = sum(a * b for a, b in zip(mu, m, strict=True)) / sum(a * a for a in mu)
    mean = sum(m) / 5
    ss_res = sum((b - k * a) ** 2 for a, b in zip(mu, m, strict=True))
    ss_tot = sum((b - mean) ** 2 for b in m)
    r2 = 1 - ss_res / ss_tot
    ok = k == Rational(9333, 9698) and r2 == Rational(21627127, 21665332)
    return ok, (
        f"through-origin fit of the (EDIT) placeholders gives exactly k = {k} = "
        f"{float(k):.6f} and R^2 = {r2} = {float(r2):.6f} -- digit-for-digit the numbers "
        "the EVIDENCE document (inside best_of_bundle_v2.zip) presents as 'STRONG EVIDENCE "
        "FOR MECHANISM'. The fit measured its own example data; no independent measurement "
        "ever existed, and this check keeps that fact permanent"
    )


@notes_prog.check(
    "FINDING: Riccati blow-up adjudicates the archive's 10/10 proof against its SIM note",
    "notes review 2026-08-22 / RICCATI",
    tier=2,
)
def _():
    from sympy import tanh

    # T1 half: the explicit solution and rate for lambda' = -2 lambda^2 + sigma.
    t = symbols("t", positive=True)
    sig = symbols("sigma", positive=True)
    lam_star = sqrt(sig / 2)
    sol = lam_star * tanh(2 * lam_star * t)  # lambda(0) = 0 branch
    residual = simplify(diff(sol, t) - (-2 * sol**2 + sig))
    rate_ok = simplify(2 * sqrt(2 * sig) - 4 * lam_star) == 0  # gamma = 2 sqrt(2 sigma)

    # T2 half: RK4 at sigma = 1, reproducing the SIM note's digits and the
    # blow-up the "10/10" proof document denies.
    def rk4(lam0, t_end, n):
        h, lam = t_end / n, lam0
        for _ in range(n):
            if abs(lam) > 1e6:
                return lam

            def f(x):
                return -2 * x * x + 1.0

            k1 = f(lam)
            k2 = f(lam + h * k1 / 2)
            k3 = f(lam + h * k2 / 2)
            k4 = f(lam + h * k3)
            lam += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return lam

    converges = rk4(-0.7, 10.0, 40000)
    blows = rk4(-1.0, 0.7, 40000)
    sim_match = abs(converges - 0.707106781041) < 1e-9
    blow_confirmed = blows < -1e6
    ok = residual == 0 and rate_ok and sim_match and blow_confirmed
    return ok, (
        f"tanh solution verified symbolically (residual {residual}), rate 2 sqrt(2 sigma); "
        f"RK4 at sigma = 1: lambda_0 = -0.7 -> {converges:.12f} (SIM note prints "
        f"0.707106781041, matched to 1e-9) while lambda_0 = -1.0 blows down past -1e6 "
        "before t = 0.7 -- the archive's 'Rigor 10/10' Theorem 2.2 (global existence for "
        "all initial data) is false and its own SIM verification note is right"
    )


@notes_prog.check(
    "fundamental Casimir: c_0 = (N^2-1)/(2N) exactly, with the convention trap pinned",
    "notes review 2026-08-22 / G20, G22 (DOC4)",
)
def _():
    from sympy import I as i_unit

    s3 = sqrt(3)
    pauli = [
        Matrix([[0, 1], [1, 0]]),
        Matrix([[0, -i_unit], [i_unit, 0]]),
        Matrix([[1, 0], [0, -1]]),
    ]
    gell = [
        Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        Matrix([[0, -i_unit, 0], [i_unit, 0, 0], [0, 0, 0]]),
        Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        Matrix([[0, 0, -i_unit], [0, 0, 0], [i_unit, 0, 0]]),
        Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        Matrix([[0, 0, 0], [0, 0, -i_unit], [0, i_unit, 0]]),
        Matrix([[1 / s3, 0, 0], [0, 1 / s3, 0], [0, 0, -2 / s3]]),
    ]
    c2_su2 = simplify(
        sum(((m / 2) * (m / 2) for m in pauli), zeros(2, 2)) - Rational(3, 4) * eye(2)
    )
    c2_su3 = simplify(sum(((m / 2) * (m / 2) for m in gell), zeros(3, 3)) - Rational(4, 3) * eye(3))
    formula = all(
        Rational(n**2 - 1, 2 * n) == v for n, v in ((2, Rational(3, 4)), (3, Rational(4, 3)))
    )
    ok = c2_su2 == zeros(2, 2) and c2_su3 == zeros(3, 3) and formula
    return ok, (
        "sum (sigma_a/2)^2 = (3/4) I and sum (lambda_a/2)^2 = (4/3) I exactly -- DOC4's "
        "c_0 = (N^2-1)/(2N) is the fundamental Casimir, the correct Haar gap scale in the "
        "orthonormal normalization. Convention trap pinned: the archive's SU(2) simulations "
        "use T_a = -i sigma_a, where the same eigenvalue reads 4 x 3/4 = 3 (their "
        "Delta B_p = 12 - 12 B_p is 4 links x 3) -- a factor-4 join hazard, not a conflict"
    )


@notes_prog.check(
    "drift-constant closure: two independent derivations agree exactly",
    "notes review 2026-08-22 / G22 (Section 7 vs G_drift_full_algebra)",
)
def _():
    s = symbols("s", positive=True)
    c_delta, c_grad, nu, kappa, c_pair, cap_pair, d = symbols(
        "C_Delta C_grad nu kappa c_pair Cpair D", positive=True
    )
    # K_Phi for Phi = s^2 on (0, 2]: s * (2s)^2 / s^2 = 4s, sup = 8 at s = 2.
    k_phi = (s * (2 * s) ** 2 / s**2).subs(s, 2)
    v_le_2d = simplify(2 * s - s**2)  # s(2 - s) >= 0 on [0, 2]
    # G_drift C_1 with B_Phi = A_Phi = 2 equals Section 7's C_V; C_2 = C_Gamma.
    c1 = 4 * (2 * c_delta + 2 * c_grad)
    c_v = 8 * c_delta + 8 * c_grad
    c2_const = 64 * nu * c_grad
    # Prop 7.39 closure: the drift bound rearranges exactly.
    lhs = (kappa * c_v + kappa**2 * c2_const) * d - 2 * kappa * (c_pair * d - cap_pair)
    rhs = -kappa * (2 * c_pair - c_v - kappa * c2_const) * d + 2 * kappa * cap_pair
    ok = (
        k_phi == 8
        and simplify(v_le_2d.subs(s, 1)) == 1  # positive at interior point
        and expand(c1 - c_v) == 0
        and expand(lhs - rhs) == 0
    )
    return ok, (
        "K_Phi = 8 at the endpoint s = 2; C_1(Phi = s^2) = 4(2C_Delta + 2C_grad) equals "
        "Section 7's C_V = 8C_Delta + 8C_grad identically, C_2 = C_Gamma = 64 nu C_grad; "
        "and Prop 7.39's rearrangement is an exact identity -- the manuscript spine and "
        "G_drift_full_algebra derive the same G22 reduction independently and agree"
    )


# ==========================================================================
# The historical kernel, decomposed channel by channel over the whole zone.
# The repository's earlier kernel checks see the 189-record artifact at the
# four parity points; these see it identically in k, so the tier collapse
# B = D = 0 becomes two exact integer cancellations at record level (G14)
# and the C2 dispute's geography — which channels carry it — is a checked
# statement instead of prose. Source claims: the maintainer's off-axis
# ledger (WORK_SINCE_2026-08, 2026-08-22), adversarially recomputed here.
# Nothing in this suite adjudicates C2 or prefers a side.
channels = _suite("off-axis channel ledger (C2 geography, G14)")


@channels.check(
    "the 189-record kernel decomposes in the shape basis over the whole zone",
    "UNIFIED v4.3 §5.1/§6",
)
def _():
    from fractions import Fraction

    from . import channel_ledger as CL

    d = CL.decompose()
    t = d["totals"]
    counts_ok = d["counts"] == {
        "on-site (0,0,0)": 3,
        "NORMAL (0,0,1)": 6,
        "IN-PLANE (0,0,1)": 12,
        "IN-PLANE (0,0,2)": 12,
        "IN-PLANE (0,1,1)": 12,
        "MIXED (0,1,1)": 24,
        "ROTATION": 120,
    }
    ok = (
        d["n_records"] == 189
        and counts_ok
        and t["E"] == 0
        and t["F"] == 0
        and t["c0"] == P.as_fraction(K.Q_BAND_4)
        and t["A"] == Fraction(5, 48)
        and t["B"] == 0
        and t["D"] == 0
        and t["C4"] / 4 == P.as_fraction(K.C_SHP_HISTORICAL)
    )
    return ok, (
        "psi^dagger H_4 psi lies exactly in span{q, q^2, e_2, q e_2, e_3} with "
        "constant and q^3 coefficients ZERO (so unlinked scalar products cannot "
        "move the shape), and the totals are c_0 = q_band^(4), A = 5/48, "
        "B = D = 0, C = C_shp^historical exactly -- the parity-point kernel "
        "identity, promoted to the whole zone; blocks (3,6,12,12,12,24,120)"
    )


@channels.check(
    "FINDING: the tier collapse is two integer cancellations at record level",
    "MASTER_THEORY §5.2 / G14",
)
def _():
    from . import channel_ledger as CL

    d = CL.decompose()
    x = CL.X_QUANTUM
    b_int = {b: d["blocks"][b]["B"] / x for b in CL.BLOCKS}
    d_int = {b: d["blocks"][b]["D"] / x for b in CL.BLOCKS}
    weights_b = [b_int["IN-PLANE (0,0,2)"], b_int["MIXED (0,1,1)"], b_int["ROTATION"]]
    weights_d = [
        d_int["IN-PLANE (0,0,2)"],
        d_int["IN-PLANE (0,1,1)"],
        d_int["MIXED (0,1,1)"],
    ]
    x_is_weight = any(w == x for (_key, w) in P.kernel_records())
    ok = (
        all(v.denominator == 1 for v in list(b_int.values()) + list(d_int.values()))
        and weights_b == [1, 1, -2]
        and sum(weights_b) == 0
        and weights_d == [-3, 6, -3]
        and sum(weights_d) == 0
        and x_is_weight
    )
    return ok, (
        "every block's q*e_2 and e_3 amplitude is an integer multiple of "
        "x = 360421351/40327601932800 (itself a raw record weight); "
        "B = 0 is (+1,+1,-2)*x over {IN-PLANE(0,0,2), MIXED, ROTATION} and "
        "D = 0 is (-3,+6,-3)*x over {IN-PLANE(0,0,2), IN-PLANE(0,1,1), MIXED} "
        "-- the kernel DOES carry B,D-generating displacement shells; they "
        "cancel, so 'forced by the symmetry and displacement gates' is at "
        "best imprecise (the finding G14 must explain)"
    )


@channels.check(
    "C_normal = -A_normal/2: the agreed axial coefficient pins the normal channel",
    "UNIFIED v4.3 §6",
)
def _():
    from fractions import Fraction

    from . import channel_ledger as CL

    d = CL.decompose()
    x = CL.X_QUANTUM
    a_n = d["blocks"]["NORMAL (0,0,1)"]["A"]
    c_n = d["blocks"]["NORMAL (0,0,1)"]["C4"] / 4
    a_mixed = d["blocks"]["MIXED (0,1,1)"]["A"]
    ok = (
        c_n == -a_n / 2
        and c_n == Fraction(-1050558388351, 20163800966400)
        and a_n == Fraction(5, 48) + 4 * x
        and a_mixed == -4 * x
    )
    return ok, (
        "on the six NORMAL records C = -A/2 = -1050558388351/20163800966400 "
        "exactly, with A_normal = 5/48 + 4x and MIXED carrying exactly -4x -- "
        "so the primitive cube-completion hop accounts for A = 5/48, and the "
        "coefficient the sealed suite shows both kernels share pins the "
        "normal sector; everything disputed lives in the non-normal remainder"
    )


@channels.check(
    "the shipped displacement support is exactly six shells",
    "off-axis ledger falsifier gate",
)
def _():
    from . import channel_ledger as CL

    census = CL.support_census()
    ok = census == {
        (0, 0, 0): 9,
        (0, 0, 1): 54,
        (0, 0, 2): 24,
        (0, 1, 1): 78,
        (0, 1, 2): 12,
        (1, 1, 1): 12,
    }
    return ok, (
        "sorted-|d| shells with multiplicities: (0,0,0)x9, (0,0,1)x54, "
        "(0,0,2)x24, (0,1,1)x78, (0,1,2)x12, (1,1,1)x12 -- the channel "
        "ledger's block structure assumes this support is complete, and a "
        "record outside it falsifies the classification"
    )


@channels.check(
    "rotation decomposes only as a sum, and the ket convention is load-bearing",
    "UNIFIED v4.3 §3.2 (carrier), tier_collapse convention",
)
def _():
    from . import channel_ledger as CL

    shells = CL.rotation_shells_in_span()
    ok = (
        len(shells) == 6
        and not any(shells.values())
        and CL.solve_span(CL.numerator(CL.decompose()["records"]["ROTATION"])) is not None
        and not CL.conjugated_ket_rotation_in_span()
    )
    return ok, (
        "each of the six rotation displacement shells is individually OUTSIDE "
        "the shape span; the 120-record sum is inside -- so no per-shell "
        "re-derivation can be compared channel-wise -- and with the ket "
        "conjugated (psi-bar instead of the d-direction) the rotation block "
        "leaves the span entirely: the two conventions coincide at the four "
        "parity points, so only a whole-zone check can catch the trap a "
        "re-implementation would fall into"
    )


@channels.check(
    "the pinned structured B_N expression IS P17(N^2)/(N R20(N^2))",
    "GLUEBALL_DETAILED_FORMULA v3.1 §11 + App. A",
)
def _():
    from . import channel_ledger as CL

    agree = [CL.b_note(n) == CL.beta_formula(n) for n in range(3, 21)]
    r20_at_9 = int(CL.R20.eval(9))
    ok = all(agree) and r20_at_9 != 0
    return ok, (
        "the walled-Brauer structured expression (pinned note, 74 terms) and "
        "the boxed all-rank formula agree exactly at N = 3..20, N = 3 "
        "included -- the corpus states the formula for N >= 4 and cautions "
        "against substituting at N = 3, but every R20 factor is nonzero at "
        "z = 9, so the continuation exists and equals the pinned expression; "
        "what the balanced value MEANS at N = 3 stays a claim, not a check"
    )


@channels.check(
    "the N=3 continuation shift is exactly 25/64, with two exact corollaries",
    "ledger C10; GLUEBALL_DETAILED_FORMULA v3.1 §8/§11",
)
def _():
    from fractions import Fraction
    from math import gcd

    from . import channel_ledger as CL

    a_shp = Fraction(5, 48)
    c_hist = P.as_fraction(K.C_SHP_HISTORICAL)
    beta_hist = 8 * a_shp + 16 * c_hist
    beta_bal = CL.beta_formula(3)
    c_bal = (beta_bal - 8 * a_shp) / 16
    alpha3 = P.as_fraction(K.ALPHA_PEN_3)
    kc = P.kernel_constants()
    ok = (
        kc["beta"] == beta_hist
        and kc["alpha"] == alpha3
        and beta_bal - beta_hist == Fraction(25, 64)
        and beta_hist - beta_bal == -Fraction(15, 16) * alpha3
        and (c_hist - c_bal) / (a_shp / 2) == -Fraction(15, 32)
        and gcd(107551523941875, 275331901291200) == 4302060957675
    )
    return ok, (
        "beta_3^bal - beta_3^hist = 25/64 exactly (raw numerator "
        "-107551523941875 over 275331901291200 reduces by the factor "
        "4302060957675), matching C10's recorded Delta_beta_3 = -25/64; "
        "corollaries never before recorded: Delta_beta_3 = -(15/16)*alpha_3 "
        "and Delta_C_3/(A/2) = -15/32. A relation among recorded quantities "
        "-- whether the shift was derived or defined as the difference is "
        "open (off-axis ledger §7), and no side of C2 is preferred here"
    )


@channels.check(
    "scalar vs shape continuation: poles where the corpus forbids, regular where it allows",
    "GLUEBALL_DETAILED_FORMULA v3.1; THM_SUN unified v2; THM_SU6",
)
def _():
    from fractions import Fraction

    from sympy import Rational as R
    from sympy import factor_list

    from . import channel_ledger as CL

    zz, q32, d34 = P.q_polynomials()
    facs = {str(b): e for b, e in factor_list(d34)[1]}
    root_max = max(CL.R20.real_roots())

    def q_formula(n: int) -> Fraction:
        return Fraction(-2, 3 * n) * Fraction(int(q32.eval(n * n)), int(d34.subs(zz, n * n)))

    q5_recorded = Fraction(-781009569168365268247626732239, 6484474594581730088957376233472)
    q6_bal_recorded = Fraction(
        -102586479919344400197896189360827281727,
        2665788121217129017242143775195086906250,
    )
    ok = (
        facs.get("z - 4") == 1
        and facs.get("z - 9") == 3
        and facs.get("z - 16") == 1
        and root_max == R(25, 9)
        and q_formula(5) == q5_recorded
        and q_formula(6) == q6_bal_recorded
    )
    return ok, (
        "D34 carries (z-4)(z-9)^3(z-16), so the scalar continuation is "
        "singular at exactly N = 2,3,4 -- it fails loudly where an "
        "epsilon-sector exists -- while R20's largest real root is 25/9 "
        "(N = 5/3), so the shape continuation is regular at every integer "
        "rank; below its stated N >= 7 scope the scalar formula reproduces "
        "the recorded q_5 exactly (SU(5): no determinant sector) and the "
        "recorded q_6^bal exactly (THM_SU6 line 86, Delta_q_6 = 6/343 "
        "checked elsewhere): the blanket N = 3 prohibition is a scalar-"
        "family fact, not a shape-family one"
    )


# ==========================================================================
manuscript = _suite("the flat-band manuscript")

PAPER_DIR = Path(__file__).resolve().parents[2] / "paper"
#: The pinned manuscripts, by the text extracted from each. The flat-band paper
#: is the one that cites this repository by commit; the master document unites
#: it with the nested-quotient circuit theory.
PAPER_TEXTS = (
    "homological_flat_bands_2026-08-28.txt",
    "nested_quotient_master_2026-08-28.txt",
)


@manuscript.check("no fourth-order coefficient enters the manuscript", "PAPER_FLATBAND §6")
def _():
    # §6 makes a claim about the manuscript itself: "no fourth-order band,
    # bandwidth, or derived higher-order quantity is used in this paper. This
    # is a scientific boundary, not merely a choice of presentation." That is a
    # statement about a document, so it is checkable against the document --
    # with the same coefficient-signature scanner `workhouse triage` points at
    # any unpinned archive. A future revision that crosses the firewall fails
    # here rather than passing unread.
    report = TRIAGE.scan(PAPER_DIR)
    carried = {
        name: set(next(f for f in report.files if f.path.name == name).coefficients)
        for name in PAPER_TEXTS
    }
    third_order = {"d_3", "b_3", "leak_3"}
    return all(v == third_order for v in carried.values()), (
        f"both pinned manuscripts carry exactly {sorted(third_order)} and no fourth-order "
        "signature: not q_band^(4), not m_Gamma^(4), not either C_shp side, not the quarantined "
        "scalar. The firewall is measured, not taken on the word of §6"
    )


@manuscript.check(
    "the manuscript's SU(3) ledger is this registry, value by value", "PAPER_FLATBAND Table 2"
)
def _():
    printed = {
        "u^0 electric plaquette": (Rational(8, 3), K.e_flat(0)),
        "u^1 scalar": (Rational(1), K.e_flat().coeff(K.u, 1)),
        "u^2 BB* coefficient": (Rational(5, 612), K.T_MINUS_2),
        "u^2 flat scalar": (Rational(11, 306), K.BAND_ODD_FLAT),
        "u^3 BB* coefficient": (Rational(1975, 124848), K.B_3),
        "u^3 per-neighbour leakage": (Rational(-12331, 249696), K.LEAK_3),
        "u^3 flat scalar": (Rational(-109151, 249696), K.D_3),
    }
    bad = [k for k, (paper, repo) in printed.items() if paper != repo]
    return not bad, (
        f"all {len(printed)} rows of Table 2 are the registry's values exactly. Scope worth "
        "stating: six rows are SU(3) specialisations of all-rank statements, but the u^1 row is "
        "SU(3)-ONLY -- it is -<p,-|V|p,-> = 1, which needs the epsilon channel and vanishes at "
        "N >= 4" + (f"; MISMATCH at {bad}" if bad else "")
    )


@manuscript.check(
    "the Bloch and chain routes to the carrier agree", "PAPER_FLATBAND Thm. 1 + Thm. 2"
)
def _():
    # The manuscript's only two structural theorems are never joined. Theorem 1
    # is a 3x3 statement; Theorem 2 counts an (L^3+2)-dimensional carrier.
    # Summing the Bloch nullity over the allowed momenta is the bridge, and the
    # two decompositions produce the same two numbers from DIFFERENT objects:
    # the 3 is B(0) = 0's triple degeneracy, not b_2(T^3), and the L^3 - 1 is
    # the count of non-Gamma momenta, not a count of cubes.
    rows = {}
    for size in (2, 3, 4):
        profile = TOR.bloch_nullities(size)
        rows[size] = (profile, sum(k * v for k, v in profile.items()))
    ok = all(
        profile == {3: 1, 1: size**3 - 1} and total == size**3 + 2
        for size, (profile, total) in rows.items()
    )
    return ok, (
        f"nullity profiles { ({s: p for s, (p, _) in rows.items()}) }: 3 at Gamma exactly once and "
        "1 at each of the other L^3 - 1 momenta, summing to L^3 + 2 -- the same count the chain "
        "complex gives, from different objects"
    )


@manuscript.check("q_min on the L-torus grid is 4 sin^2(pi/L)", "PAPER_FLATBAND eq. (16)")
def _():
    sizes = range(2, 7)
    for size in sizes:
        values = {
            sum(4 * sin(pi * n / size) ** 2 for n in t) for t in product(range(size), repeat=3)
        }
        nonzero = sorted((v for v in values if simplify(v) != 0), key=float)
        if simplify(nonzero[0] - 4 * sin(pi / size) ** 2) != 0:
            return False, f"grid minimum at L = {size} is {nonzero[0]}, not 4 sin^2(pi/L)"
    return True, (
        f"exhaustive over the whole momentum grid at L = {list(sizes)}: the smallest nonzero q "
        "puts one unit of momentum in a single direction, because sin^2(pi n/L) over n = 1..L-1 "
        "is smallest at n = 1 and n = L-1"
    )


@manuscript.check(
    "Delta_L = 4 tau(u) sin^2(pi/L) is positive and falls as L^-2", "PAPER_FLATBAND eq. (35)"
)
def _():
    tau = K.t_series()
    positive = tau.coeff(K.u, 2) > 0 and tau.coeff(K.u, 3) > 0
    scaled = limit(K.L**2 * (4 * tau * sin(pi / K.L) ** 2), K.L, oo)
    return positive and simplify(scaled - 4 * pi**2 * tau) == 0, (
        f"tau(u) = {tau} has both coefficients positive, so Delta_L > 0 for every u > 0 and "
        f"L >= 2; and L^2 Delta_L -> {scaled}, the L^-2 decay that is exactly why the manuscript "
        "does not claim volume-uniform isolation"
    )


@manuscript.check(
    "the two band spans ARE the two incidence spectra", "PAPER_FLATBAND §4 / PAPER App. B"
)
def _():
    # The manuscript introduces the unsigned incidence as a control: strip the
    # orientation signs and the adjacency has spectrum {12,0,0} at Gamma and
    # {-4,-4,-4} at the corner, disjoint, so nothing can be momentum
    # independent. That control is not hypothetical -- it is the C-even sector,
    # and both spans are certified corpus numbers. The difference between 12
    # and 16 is exactly the orientation sign §4 says is doing the work.
    def spectrum(momenta, signed):
        d = [exp(I * k) - 1 if signed else exp(I * k) + 1 for k in momenta]
        rows = (
            Matrix([[d[1], -d[0], 0], [d[2], 0, -d[0]], [0, d[2], -d[1]]])
            if signed
            else Matrix([[d[1], d[0], 0], [d[2], 0, d[0]], [0, d[2], d[1]]])
        )
        adjacency = simplify(rows * rows.H - 4 * eye(3))
        return sorted(int(simplify(e)) for e in adjacency.eigenvals(multiple=True))

    unsigned = (spectrum([0, 0, 0], False), spectrum([pi, pi, pi], False))
    signed = (spectrum([0, 0, 0], True), spectrum([pi, pi, pi], True))
    spectra_ok = (
        unsigned == ([0, 0, 12], [-4, -4, -4])
        and signed == ([-4, -4, -4], [-4, 8, 8])
        and not (set(unsigned[0]) & set(unsigned[1]))
        and set(signed[0]) & set(signed[1]) == {-4}
    )
    odd = K.BAND_ODD_TOP - K.BAND_ODD_FLAT
    even = K.BAND_EVEN_TOP - K.BAND_EVEN_BOTTOM
    widths_ok = (
        odd == 12 * K.T_MINUS_2 == K.BAND_ODD_WIDTH
        and even == 16 * abs(K.T_PLUS_2) == K.BAND_EVEN_WIDTH
    )
    return spectra_ok and widths_ok, (
        f"unsigned {unsigned[0]} at Gamma and {unsigned[1]} at R, disjoint; signed {signed[0]} "
        f"and {signed[1]}, sharing exactly -4 -- the flat branch. The spans are 16 and 12, and "
        f"they are the two bandwidths: C-even 16|t_+| = {even}, C-odd 12 t_- = {odd}. The "
        "certificate's own key for the first is 'corrected_Ceven_bandwidth_16|t|'"
    )


@manuscript.check("the zone maximum of q is 12 only at even L", "MASTER_DOC eq. (34)")
def _():
    # The master document refines the flat-band paper's flat "12". On the
    # periodic L^3 momentum grid the largest sampled q is 12 only when L is
    # even, because only then does some k_j reach pi exactly; at odd L the
    # closest allowed momentum is pi(L-1)/L and the maximum is 12 cos^2(pi/2L).
    # The manifold width W = q_max(L) t_N u^2 inherits the parity.
    rows = {}
    for size in range(2, 10):
        values = {
            sum(4 * sin(pi * n / size) ** 2 for n in t) for t in product(range(size), repeat=3)
        }
        attained = max(values, key=float)
        claimed = Integer(12) if size % 2 == 0 else 12 * cos(pi / (2 * size)) ** 2
        if simplify(attained - claimed) != 0:
            return False, f"q_max at L = {size} is {attained}, not {claimed}"
        rows[size] = attained
    return True, (
        f"exhaustive over the whole grid at L = 2..9: { ({k: str(v) for k, v in rows.items()}) }. "
        "The 12 the flat-band paper prints is the even-L and thermodynamic value; the width "
        "W = q_max(L) t_N u^2 is smaller at every odd L"
    )


@manuscript.check("q at the four high-symmetry points is 0, 4, 8, 12", "MASTER_DOC Fig. 2")
def _():
    # Figure 2 plots the incidence spectrum along Gamma-X-M-R-Gamma and is
    # asserted rather than generated. Its four corners are arithmetic, and the
    # branch set at each is {0, q, q} by the factorization theorem -- so the
    # figure is reproducible from two checked statements rather than trusted.
    points = {
        "Gamma": (0, 0, 0),
        "X": (pi, 0, 0),
        "M": (pi, pi, 0),
        "R": (pi, pi, pi),
    }
    got = {name: simplify(sum(4 * sin(k / 2) ** 2 for k in ks)) for name, ks in points.items()}
    return got == {"Gamma": 0, "X": 4, "M": 8, "R": 12}, (
        f"{got}; the plotted branch set at each point is {{0, q, q}}, and R attains the zone "
        "maximum 12 that sets the full-manifold width"
    )


@manuscript.check(
    "on an axial cut the mixed invariants vanish and the norm divides",
    "MASTER_DOC §9, eq. (60)-(64)",
)
def _():
    # Why the axial datum is decidable while the off-axis one is not, one order
    # below C2's usual statement. On k = (k, 0, 0) the Bloch invariants collapse
    # to q = L(k) with e_2 = e_3 = 0, so every mixed invariant is blind there --
    # which is exactly why an axial measurement cannot determine C_shp, and why
    # both disputed kernels agree on alpha.
    #
    # The second half is the norm division the master document's Conditional
    # corollary 12 turns on: the raw cube-boundary numerator is (alpha/4)L^2
    # while ||w||^2 = q = L, so the carrier eigenvalue carries a single power
    # of L and its coefficient is alpha_3/4 = 5/48 = A_shp.
    k = symbols("k", real=True)
    axis = [k, 0, 0]
    a = [4 * sin(component / 2) ** 2 for component in axis]
    q = simplify(sum(a))
    e2 = simplify(a[0] * a[1] + a[0] * a[2] + a[1] * a[2])
    e3 = simplify(a[0] * a[1] * a[2])
    lk = 4 * sin(k / 2) ** 2
    collapse = simplify(q - lk) == 0 and e2 == 0 and e3 == 0
    divided = simplify((K.ALPHA_PEN_3 / 4) * lk**2 / lk - (K.ALPHA_PEN_3 / 4) * lk) == 0
    coefficient = K.ALPHA_PEN_3 / 4 == K.A_SHP_3
    return collapse and divided and coefficient, (
        f"on k = (k,0,0): q = L(k) = {lk}, e_2 = {e2}, e_3 = {e3}. Dividing the raw numerator "
        f"(alpha/4)L^2 by ||w||^2 = q = L leaves one power of L with coefficient "
        f"alpha_3/4 = {K.ALPHA_PEN_3 / 4} = A_shp. The mixed invariants are zero on the whole "
        "axis, which is why the axial datum both kernels share cannot determine C_shp"
    )


@manuscript.check(
    "FINDING: the retained Gamma/axis data cannot identify C_shp", "MASTER_DOC closure audit / C2"
)
def _():
    # The closure-audited synthesis states an "exact obstruction certificate":
    # two exact rational carrier-energy witnesses agree on every retained
    # Gamma/axis datum and differ at M and R. It holds, and it is stronger than
    # a statement about sampled points.
    #
    # The two recorded C_shp sides differ on the mixed-gradient ray alone, so
    # their shape difference is 4 Delta_C e_2. On a one-dimensional axial cut
    # two of the three a_i vanish, so e_2 vanishes IDENTICALLY in the remaining
    # momentum -- not at sampled points, as a polynomial. No amount of Gamma or
    # axial data can therefore separate the two kernels, whatever its precision.
    #
    # This is why G3 is the decider and why no re-anchoring closes C2. It
    # decides nothing about which side is right, and must not be read as
    # preferring either.
    momenta = symbols("k1 k2 k3", real=True)
    a = [4 * sin(k / 2) ** 2 for k in momenta]
    e2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
    delta = symbols("Delta_C")
    difference = 4 * delta * e2
    axis = simplify(difference.subs({momenta[1]: 0, momenta[2]: 0}))
    corner = simplify(difference.subs(dict(zip(momenta, (pi, pi, pi), strict=True))))
    face = simplify(difference.subs(dict(zip(momenta, (pi, pi, 0), strict=True))))
    return axis == 0 and face != 0 and corner != 0, (
        f"4 Delta_C e_2 vanishes identically on every axial cut ({axis}), and is {face} at M and "
        f"{corner} at R. The vanishing is polynomial, not numerical: two of the three a_i are "
        "zero on an axis, so e_2 is the zero polynomial there. The retained corpus is "
        "non-identifying for C_shp by construction, and neither side is preferred here"
    )


@manuscript.check(
    "every \\chk in the united paper names a check that exists and passes",
    "PAPER_MASTER, every displayed result",
)
def _():
    # The united paper's one device is that each displayed result carries the
    # name of the machine check that establishes it, so a reader can re-run any
    # line in about a second. That device is worth exactly as much as its
    # weakest label: a renamed or deleted check leaves the paper printing a
    # command that no longer resolves, and a paper that has drifted still reads
    # as current -- the same failure mode FRONTIER.md's staleness test guards.
    #
    # So resolve every label against the live registry here, and require the
    # named check to be one that passes. This does not re-run them (the suites
    # do that); it asserts the paper cites nothing that has gone missing or red.
    source = (PAPER_DIR / "master_paper_2026-08-28.tex").read_text(encoding="utf-8")
    cited = [
        m.replace("\\_", "_").replace("\\^", "^") for m in re.findall(r"\\chk\{([^}]*)\}", source)
    ]
    known = {check[0] for suite in SUITES for check in suite.checks}
    unresolved = sorted(set(cited) - known)
    return not unresolved and len(cited) > 0, (
        f"{len(cited)} \\chk labels across {len(set(cited))} distinct checks, every one of them "
        f"a registered check name; {len(unresolved)} unresolved. Each displayed result in the "
        "paper is reproducible by the command printed beneath it"
    )
