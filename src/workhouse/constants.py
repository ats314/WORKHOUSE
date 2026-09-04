"""Exact-constant registry for the SU(N) cubic flux-band spectral program.

Every entry carries its provenance and its corpus status, because in this corpus
a number's *truth status* and its *evidence status* are independent (MASTER_THEORY
§1.1-1.2). Nothing here is promoted: the two disputed fourth-order kernels are
both recorded, side by side, exactly as the corpus insists.

Exact values are ``sympy.Rational``. Values the corpus records only as floating
point (the v10a.26 folded run) are Python floats and are named ``*_NUM`` so a
reader can never mistake one for an exact rational.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sympy import Integer, Rational, Symbol, sympify

N = Symbol("N", positive=True)  # gauge rank
L = Symbol("L", positive=True)  # torus extent
u = Symbol("u", positive=True)  # canonical strong-coupling coordinate, u = beta_lat/6
x = Symbol("x", positive=True)  # rank-squared coordinate, x = N**2

# Corpus status vocabulary (MASTER_THEORY §1.1).
STATUSES = frozenset({"proven", "conditional", "disputed", "open", "superseded", "falsified"})
# Corpus evidence vocabulary (MASTER_THEORY §1.2).
EVIDENCE = frozenset(
    {
        "analytic",
        "cold-reproduced",
        "output-certified",
        "numerical",
        "record-backed",
        "prose-only",
    }
)


@dataclass(frozen=True)
class Constant:
    """One archived number, with the provenance needed to argue about it."""

    name: str
    value: Any
    status: str
    evidence: str
    source: str
    note: str = ""

    def __post_init__(self) -> None:
        if self.status not in STATUSES:
            raise ValueError(f"{self.name}: unknown status {self.status!r}")
        if self.evidence not in EVIDENCE:
            raise ValueError(f"{self.name}: unknown evidence level {self.evidence!r}")


# --------------------------------------------------------------------------
# Canonical coordinate
# --------------------------------------------------------------------------
# u = beta_lat/6 = 1/g_H**4.  The archived "Y = 2*beta_lat/3 = 4u" line is a
# definition-label erratum: the printed coefficients were already generated in u
# and must never be rescaled by 4**r.  (UNIFIED §2.1, GLUEBALL §2.2, C4.)


# --------------------------------------------------------------------------
# Second order, all ranks  (MASTER_THEORY §4.3, PROVEN)
# --------------------------------------------------------------------------
def antiparallel_sum(n=N):
    """Channel sum A_N over the antiparallel (Lambda^2 + Sym^2) pairing."""
    n = sympify(n)
    return -2 * n**3 / ((n**2 - 1) * (2 * n**2 - 1))


def parallel_sum(n=N):
    """Channel sum B_N over the parallel pairing."""
    n = sympify(n)
    return -4 * n * (n**2 - 2) / ((n**2 - 1) * (4 * n**2 - 9))


# --------------------------------------------------------------------------
# The shared-link fusion channels that A_N and B_N are built from
# --------------------------------------------------------------------------
# A_N and B_N above were registered as printed closed forms. These are the
# representation-theoretic inputs, so the two sums can be *derived* rather than
# transcribed:
#
#   F (x) Fbar = 1 + Adj              the mixed (antiparallel) family -> A_N
#   F (x) F    = Lambda^2 + Sym^2     the like (parallel) family      -> B_N
#
# The resolvent denominator: six nonshared half-links cost 3 C_F, the fused
# link costs C_R/2, and the external one-plaquette state sits at 2 C_F, so the
# gap is (3 C_F + C_R/2) - 2 C_F = C_F + C_R/2. The numerator weight d_R/N**2
# is the manuscript's "isotropy of the normalized shared-link tensor" — the one
# input of the chain this repository does NOT derive, recorded here so the
# boundary is visible at the definition rather than buried in a check.

CHANNELS = ("1", "Adj", "Lambda2", "Sym2")

#: Which family each channel belongs to, and hence which sum it feeds.
CHANNEL_FAMILY = {"1": "mixed", "Adj": "mixed", "Lambda2": "like", "Sym2": "like"}


def channel_data(rank=N):
    """``(d_R, C_2(R))`` for the four shared-link fusion channels."""
    n = sympify(rank)
    return {
        "1": (Integer(1), Integer(0)),
        "Adj": (n**2 - 1, n),
        "Lambda2": (n * (n - 1) / 2, (n + 1) * (n - 2) / n),
        "Sym2": (n * (n + 1) / 2, (n - 1) * (n + 2) / n),
    }


def casimir_fundamental(rank=N):
    """``C_F = (N**2 - 1)/(2N)``."""
    n = sympify(rank)
    return (n**2 - 1) / (2 * n)


def plaquette_energy(rank=N):
    """The unperturbed one-plaquette energy, ``4 * (C_F/2) = 2 C_F``."""
    return 2 * casimir_fundamental(rank)


def channel_gap(channel, rank=N):
    """``E_intermediate - E_external`` for one channel: ``C_F + C_R/2``."""
    _, casimir = channel_data(rank)[channel]
    return 3 * casimir_fundamental(rank) + casimir / 2 - plaquette_energy(rank)


def channel_weight(channel, rank=N):
    """``w_R = -(d_R/N**2) / (C_F + C_R/2)``, the resolvent weight."""
    dim, _ = channel_data(rank)[channel]
    return -(dim / sympify(rank) ** 2) / channel_gap(channel, rank)


def channel_weight_printed(channel, rank=N):
    """The closed forms the corpus prints for the four weights."""
    n = sympify(rank)
    return {
        "1": -2 / (n * (n - 1) * (n + 1)),
        "Adj": -2 * (n - 1) * (n + 1) / (n * (2 * n**2 - 1)),
        "Lambda2": -(n - 1) / ((2 * n - 3) * (n + 1)),
        "Sym2": -(n + 1) / ((2 * n + 3) * (n - 1)),
    }[channel]


def even_hopping(rank=N):
    """``ell_N``, the all-rank C-even second-order hopping.

    Printed in the corpus (``records/audits/03-prism-selection-shape.md``) and
    gated inside ``NB_O2_prism_square_second_order_falsification.ipynb`` as
    ``factor(Wmix + Wlike + 1/CF)`` — never checked here until now. The
    ``1/C_F`` is the vacuum-mediated route, which is exactly what C13 records
    as having been omitted.
    """
    n = sympify(rank)
    return -2 * n * (3 * n**2 - 5) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))


def hopping(n=N):
    """C-odd shared-link hopping t_N = B_N - A_N, positive for N >= 3."""
    n = sympify(n)
    return 2 * n * (n**2 - 4) / ((n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))


def hopping_deficit(n=N):
    """1/4 - N**3 t_N, the positive gap left by the N**-3 cancellation."""
    n = sympify(n)
    return (2 * n**4 + 31 * n**2 - 9) / (4 * (n**2 - 1) * (2 * n**2 - 1) * (4 * n**2 - 9))


#: Sign-determining factor of d/dN (N**3 t_N), in x = N**2.
#: The corpus prints the prefactor as 2*x**2; sympy reports 2*x after cancelling
#: the gcd with the denominator. Only this cubic controls the sign, and it is
#: strictly positive for x >= 4, so N**3 t_N increases monotonically to 1/4.
MONOTONICITY_CUBIC = 2 * x**3 + 62 * x**2 - 151 * x + 72

#: Large-rank expansion coefficients of t_N in powers of 1/N.
HOPPING_LARGE_N = {
    3: Rational(1, 4),
    5: Rational(-1, 16),
    7: Rational(-77, 64),
    9: Rational(-1021, 256),
}

# SU(3) second-order ledger (PAPER eq. 7; CERTIFIED).
D_PLUS_2 = Rational(223, 1020)  # C-even diagonal
T_PLUS_2 = Rational(-11, 306)  # C-even hopping; corrects a superseded -481/612 (C13)
D_MINUS_2 = Rational(7, 102)  # C-odd diagonal
T_MINUS_2 = Rational(5, 612)  # C-odd hopping = t_3

# Exact O(u**2) band data (PAPER App. B).
BAND_EVEN_BOTTOM = Rational(-217, 1020)  # A_1^{++} at lambda = 12
BAND_EVEN_TOP = Rational(1109, 3060)
BAND_EVEN_WIDTH = Rational(88, 153)
BAND_ODD_FLAT = Rational(11, 306)
BAND_ODD_TOP = Rational(41, 306)
BAND_ODD_WIDTH = Rational(5, 51)

# One-plaquette bridge tower coefficients as functions of beta/4
# (PAPER_FLUX_glueball_flat_band_v1_1.tex; UNIFIED §2.1). These pin the
# canonical coordinate: written in u = beta/6 they reproduce the printed
# u-towers verbatim, and under the archived Y = 4u reading they would be
# off by 4**r — the C4/G2 conversion statement, checkable.
TOWER_B2_PLUS = Rational(13, 180)  # C-even, order (beta/4)**2
TOWER_B3_PLUS = Rational(101, 2700)  # C-even, order (beta/4)**3
TOWER_B2_MINUS = Rational(1, 18)  # C-odd, order (beta/4)**2
TOWER_B3_MINUS = Rational(7, 432)  # C-odd, order (beta/4)**3

# --------------------------------------------------------------------------
# Third order, SU(3)  (MASTER_THEORY §4.4, COLD-CERTIFIED)
# --------------------------------------------------------------------------
B_3 = Rational(1975, 124848)  # third-order hopping
LEAK_3 = Rational(-12331, 249696)  # renamed from ell_3 to avoid collision with all-rank ell_N
D_3 = Rational(-109151, 249696)  # = 7/32 + 12*LEAK_3 - 4*B_3
#: Vacuum-subtracted C-even A1++ mass coefficient at k = 0, order u^3, from the
#: corpus certificate RUN_TROM_d3_results.json ("m3_even_k0"). Not
#: independently re-derived here; registered because Hamer's 1989 table
#: corroborates it externally (published-comparisons suite).
M3_EVEN_K0 = Rational(-54049, 520200)

#: Domino-engine certificate locks (ENGINE_FLUX_su3_domino_d3.py, 251 gates;
#: conditional on that engine's census, same lineage as B_3/LEAK_3/D_3).
#: The engine's structural identity leak_{r,+} = t_{r,+} holds at both
#: computed orders; T3_EVEN is therefore both the C-even third-order hopping
#: and the C-even third-order per-neighbour leakage. The engine calls the
#: mechanism the vacuum route; ADR 0023 derives the identity and it is not
#: (the swap-odd state e_1 - e_2 has no vacuum image at all).
T3_EVEN = Rational(-6335, 249696)  # C-even third-order hopping, engine lock
D3_ODD_DOMINO = Rational(-24541, 62424)  # domino C-odd diagonal at order 3
D3_EVEN_DOMINO = Rational(-517313, 6242400)  # domino C-even diagonal at order 3
VAC3_DOMINO = Rational(-9, 16)  # two-plaquette vacuum piece = 2 x (-9/32)
D3_TOP = Rational(-61751, 249696)  # C-odd dispersive top (lambda = 8) at order 3

# --------------------------------------------------------------------------
# The domino ledger  (RUN_TROM_d3_results.json; CERT_FLUX_d3_certificate_results.md)
# --------------------------------------------------------------------------
# The repository already carried the band VALUES these assemble into, and
# checked them by subtracting one from another. These are the ingredients they
# are assembled FROM, in both charge sectors and at both orders, from the
# abstract-domino engine's 251-gate run.

LEAK_2 = Rational(-11, 306)  # second-order per-neighbour leakage, C-odd
LEAK_2_EVEN = Rational(-11, 306)  # ... and C-even. The same rational; see below.
LEAK_3_EVEN = Rational(-6335, 249696)  # ... and its leakage, = T3_EVEN. Again.

#: The C-even band edge at lambda = -4, order 3. The certificate key is
#: "m3_even_bandmin (lambda=-4)" and that key name is wrong: t_{3,+} < 0, so
#: lambda = -4 is the band TOP, which is what PAPER's third-order theorem, the
#: manuscript patch's constant table and the master program note all call it.
#: Renamed here to stop the registry contradicting BAND_EVEN_TOP, which is the
#: same edge one order down; the FINDING check keeps the discrepancy visible.
M3_EVEN_BANDTOP = Rational(471353, 1560600)  # C-even at lambda = -4, the TOP

#: The E++ doublet at lambda = 0, order 3. PAPER derives it from the certified
#: band form ("101/200 + 12 T_3^e = 52163/260100") and flags it as following
#: from that form rather than computed independently -- so it is exactly the
#: kind of value that is worth re-deriving here rather than transcribing.
M3_EVEN_EPP = Rational(52163, 260100)

#: The C-even A1++ curvature coefficients, PAPER's "curvature +22/459 |k|^2 y^2"
#: and its third-order correction. Both are (4/3)|t_{r,+}|; the 4/3 is the
#: Gamma expansion of the unsigned adjacency, not a convention.
CEVEN_CURVATURE_2 = Rational(22, 459)
CEVEN_CURVATURE_3 = Rational(6335, 187272)

# This block once re-registered five values the certificate-lock block above
# already carried, under names differing by an underscore or a suffix:
# T_3_EVEN, D3_ODD, D3_EVEN, E_VAC3_DOMINO and D_3_TOP duplicated T3_EVEN,
# D3_ODD_DOMINO, D3_EVEN_DOMINO, VAC3_DOMINO and D3_TOP. Every one of the
# duplicates was read by nothing, and the harm was not hypothetical: a note
# review's bears_on pointed at three of the dead names, so following it
# reached a constant no check uses.
#
# The give-away was this comment's own census. It used to read "three labels
# on -11/306, two on -6335/249696" -- and the second count was wrong, because
# T_3_EVEN was a third label nobody had noticed. A file that miscounts its own
# coincidences is exactly the state DECLARED_COINCIDENCES now prevents.
#
# Recorded, not explained: leak_r = t_r in the C-even sector at BOTH orders,
# and at second order the C-odd leakage equals them too. Three labels on
# -11/306, two on -6335/249696. Nothing here shows why, and a mechanism must
# not be read off a coincidence of values -- ADR 0005 is what happens when one
# is. The -11/306 coincidence is now half explained: all three second-order
# labels are ell_N = A_N + B_N + 1/C_F, an all-rank closed form, so at that
# order it is one object rather than three (charge-even suite). The C-even
# identity one order up is still bare, and is registered as the unifying
# candidate U4 -- with a falsifier -- rather than as a result.

#: Values this registry deliberately carries under more than one name, and why.
#: Distinct physical quantities may of course be equal -- a hopping and a
#: leakage in the same sector are different objects that happen to coincide,
#: and recording both is the point. What must NOT happen is the same quantity
#: registered twice under near-identical names, because the join keys here are
#: exact rationals: `workhouse search` then returns two "different" constants
#: and a reader can cite them as independent corroboration of each other.
#: `tests/test_constants.py` fails on any shared value not declared here.
DECLARED_COINCIDENCES: dict[str, tuple[tuple[str, ...], str]] = {
    "-11/306": (
        ("LEAK_2", "LEAK_2_EVEN", "T_PLUS_2"),
        "second-order per-neighbour leakage in both charge sectors, and the "
        "C-even hopping: three distinct quantities, and one object -- all "
        "three are ell_N = A_N + B_N + 1/C_F at N = 3, checked at symbolic N "
        "by the charge-even suite, so the coincidence is derived not observed",
    ),
    "-6335/249696": (
        ("T3_EVEN", "LEAK_3_EVEN"),
        "the engine's structural identity leak_{r,+} = t_{r,+} at third order; "
        "hopping and leakage are different objects that this run finds equal, and "
        "the swap-odd suite derives why (ADR 0023): the swap-odd domino state is a "
        "single excited plaquette beside an inert one through third order",
    ),
}

#: The adjacency eigenvalues the band assembly is evaluated at. The C-odd
#: sector sees the SIGNED incidence, spec S = {-4, q-4, q-4} with q in [0, 12],
#: so its carrier sits at -4 and its dispersive top at +8. The C-even sector
#: sees the UNSIGNED incidence, spec {12, 0, 0} at Gamma and {-4,-4,-4} at the
#: corner. The two spans, 12 and 16, are the two bandwidths.
BAND_LAMBDA = {"odd": (-4, 8), "even": (12, -4)}


def band_tower(sector, order):
    """The within-plaquette tower coefficient in canonical u, at this order.

    Not a new input: this is the certified coupling conversion
    ``tower(u) = 4 * Delta(3u/2)`` applied to the registered (beta/4) towers --
    the same statement the coupling-erratum suite checks. Writing it here is
    what lets ``band_assembly`` take no unregistered ingredient.
    """
    printed = {
        ("odd", 2): TOWER_B2_MINUS,
        ("odd", 3): TOWER_B3_MINUS,
        ("even", 2): TOWER_B2_PLUS,
        ("even", 3): TOWER_B3_PLUS,
    }[(sector, order)]
    return 4 * Rational(3, 2) ** order * printed


def band_assembly(sector, order, lam):
    """The band coefficient at adjacency eigenvalue ``lam``.

        E_s(lambda, r) = tower_{r,s} + 12 * leak_{r,s} + lambda * t_{r,s}

    Twelve neighbours, one leakage each; the hop enters through the adjacency.
    """
    leak = {
        ("odd", 2): LEAK_2,
        ("odd", 3): LEAK_3,
        ("even", 2): LEAK_2_EVEN,
        ("even", 3): LEAK_3_EVEN,
    }[(sector, order)]
    hop = {
        ("odd", 2): T_MINUS_2,
        ("odd", 3): B_3,
        ("even", 2): T_PLUS_2,
        ("even", 3): T3_EVEN,
    }[(sector, order)]
    return band_tower(sector, order) + 12 * leak + lam * hop


def e_flat(coupling=u):
    """Flat charge-odd carrier energy through O(u**3)."""
    return Rational(8, 3) + coupling + Rational(11, 306) * coupling**2 + D_3 * coupling**3


def t_series(coupling=u):
    """Hopping prefactor t(u) through O(u**3)."""
    return T_MINUS_2 * coupling**2 + B_3 * coupling**3


# --------------------------------------------------------------------------
# Fourth order — sealed core (MASTER_THEORY §5.2, CERTIFIED by BOTH kernels)
# --------------------------------------------------------------------------
A_SHP_3 = Rational(5, 48)
B_SHP_3 = Rational(0)
D_SHP_3 = Rational(0)
ALPHA_PEN_3 = Rational(5, 12)  # = 4 * A_SHP_3
CUBE_COMPLETION_4 = Rational(-5, 48)  # c_4^square(3); alpha_3 = 4*|c_4^square(3)|

#: v10a.26 folded-run values for the sealed core. Consistent with the exact
#: rationals above but NOT exact rational equalities from that run (GLUEBALL §10).
A_SHP_3_NUM = 0.104166666666728
B_SHP_3_NUM = 3.55e-16
D_SHP_3_NUM = 2.23e-13
ALPHA_PEN_3_NUM = 0.41666666666691
SEALED_CORE_TOLERANCE = 2.3e-13


def alpha_pen(n=N):
    """All-rank axial law alpha_N = 640 / (N (N**2-1)**3)."""
    n = sympify(n)
    return Rational(640) / (n * (n**2 - 1) ** 3)


# --------------------------------------------------------------------------
# Fourth order — anchoring and the residual dispute (MASTER_THEORY §5.5)
#
# TERMINOLOGY. These are NOT two competing estimates of one scalar. Calling
# them "two m_4 values" manufactures a contradiction that does not exist:
#
#   Q_BAND_4       q_band^(4)  — a band-kernel anchor
#   M_GAMMA_4_NUM  m_Gamma^(4) — a vacuum-subtracted physical Gamma-point coefficient
#
# They are differently anchored coordinates related by a translation-local
# scalar shift, which cannot change the centered operator, its eigenvectors,
# the SOS factorization, the mobility coefficients, or the bandwidth. C1 is an
# anchoring distinction, not a dispute.
#
# What remains genuinely open is C2, the off-axis shape coefficient. See the
# crosswalk at the foot of this module for why a Gamma-point match is
# structurally incapable of settling it.
# --------------------------------------------------------------------------
#: Band-kernel anchor from the historical 189-record kernel (exact rational).
Q_BAND_4 = Rational(-20721577909065127111, 7250590288602460800)
#: Historical off-axis shape coefficient (exact rational) = (BETA_PEN_3 - 2*alpha)/16.
C_SHP_HISTORICAL = Rational(-211835444920651, 4405310420659200)
#: Historical diagonal coefficient.
BETA_PEN_3 = Rational(17607806155349, 275331901291200)
#: The degree-3 record quantum of the historical kernel: every block's q*e_2
#: and e_3 channel amplitude is an integer multiple of this, itself a raw
#: record weight; the tier collapse is (+1,+1,-2)*x and (-3,+6,-3)*x exactly
#: (suite "off-axis channel ledger"; source: the maintainer's off-axis
#: ledger, WORK_SINCE_2026-08).
X_QUANTUM = Rational(360421351, 40327601932800)

# The six cubic orbits of the historical 189-record kernel (suite "fourth-order
# kernel orbits"). Registered by VALUE because the join keys of this corpus are
# exact rationals: RHO_ORBIT and PI_ORBIT are the two amplitudes the whole of C2
# reduces to, and until they were entries here `workhouse search` could not find
# either one from its own number -- the checks printed them as ratios to
# X_QUANTUM, which is a different rational.
#
# X_QUANTUM is the skeleton amplitude u of that decomposition; the doubled orbit
# is exactly 2u, which is the entire content of the e_3 tier collapse.
#: Doubled orbit (12 records, same-plane (0,1,1) in-plane): exactly 2*X_QUANTUM.
U2_ORBIT = Rational(360421351, 20163800966400)
#: Rotation orbit (24 cross-plane records). Contributes to C alone, at -rho/2.
RHO_ORBIT = Rational(238714892212171339, 29002361154409843200)
#: In-plane orbit (12 records, same-plane nearest neighbour). C alone, at -pi/2.
PI_ORBIT = Rational(-20535103905179, 1264270320593280)
#: Normal orbit (6 records). Not independently disputed: A = 5/48 forces
#: nu = -(5/48 + 4u) exactly, and C_normal = -A_normal/2.
NU_ORBIT = Rational(-1050558388351, 10081900483200)
#: On-site orbit (3 records). Enters c_0 alone; no effect on A, B, C or D.
SIGMA_ORBIT = Rational(-780864191400383617, 302107928691769200)
#: RETRACTED 2026-08-30, the same day it was added. Registered as "the exact
#: eps-free branch of C2"; it is not one. It is C_SHP_HISTORICAL + 25/1024,
#: where 25/64 is the gap between BETA_PEN_3 and b_evaluator(3) -- and
#: b_evaluator(3) is bit-identical to P17(9)/(3 R20(9)), the substitution
#: GLUEBALL_DETAILED_FORMULA v3.1 forbids at N = 3 ("use the separate exact
#: SU(3) value"), at a rank where the continuation route is separately closed
#: by a third-order pole in D34.
#:
#: Kept, not deleted, because the relation is real and DELTA_BETA_3 records it,
#: and because deleting a refuted claim destroys the evidence it was tried.
#: Read it as "historical plus the forbidden-substitution shift", never as a
#: balanced value of C_shp. No direct balanced contraction at N = 3 is held in
#: this repository.
C_SHP_CONTINUATION_SHIFTED = Rational(-13035490122347, 550663802582400)

#: Vacuum-subtracted physical Gamma-point coefficient, from the blind
#: finite-cluster/rooted oracle (float only). Reproduces Hamer's a_4 through the
#: bridge m_n = 2**(n-1) * a_n with no historical target in its data flow, which
#: makes it substantive external validation rather than internal bookkeeping.
M_GAMMA_4_NUM = -0.7751458630189173
C_SHP_NEW_NUM = -0.020213328886166577

#: Anchoring offset, m_Gamma^(4) - q_band^(4). In high precision the difference
#: is 2.082770125095641678..., which correctly rounds to ...417. The corpus
#: prints ...414, one ulp low, because it rounds q_band^(4) to a double before
#: subtracting. Benign, but the printed digit is not the correctly rounded one.
DELTA_GAMMA_NUM = 2.0827701250956417
DELTA_GAMMA_AS_PRINTED_NUM = 2.0827701250956414
#: The residual off-axis discrepancy, C_new - C_old. This one is real.
DELTA_C_NUM = 0.027873054295192174
#: Corpus-recorded off-axis band splits at M and R (8*Delta_C and 16*Delta_C)
#: and the recorded new-kernel diagonal beta_new = 8A + 16*C_new. Registered so
#: search-by-value reaches them and the two suites that quote them cannot
#: drift apart via independently edited inline literals.
M_SPLIT_RECORDED_NUM = 0.2229844343615374
R_SPLIT_RECORDED_NUM = 0.4459688687230748
BETA_PEN_NEW_NUM = 0.5099200711546681

W4_HISTORICAL_NUM = 0.48061786909826
W4_NEW_NUM = 0.9265867378213348

#: Hamer (1989), Phys. Lett. B 224, 339 — Table 1 of the digest-pinned primary
#: (sha256 in literature/index.yaml; the paper itself is publisher-copyright
#: and is NOT stored). Read 2026-08-21 and verified against the rendered page
#: image, not OCR. Convention: x = 2/g**4 = 2u; the dimensionless gap M of
#: W = (2/g**2) a H obeys m a = (g**2/2) M, so u-coefficients bridge as
#: m_n = 2**(n-1) a_n. Orders 0 and 1 are exact in the paper (16/3 with a
#: recurring-decimal dot, and -1/+1/-1) and appear directly in the checks;
#: the printed decimals below are floats, orders n = 2..7. Trailing printed
#: zeros (e.g. 0.106372549020) are precision information a float cannot carry;
#: the per-check bounds account for the printed half-ulp.
HAMER_A4_NUM = -0.0968932328773  # = HAMER_MA_NUM[2]; kept under its long-standing name
HAMER_MA_NUM = (  # 1+- (axial vector) — the program's C-odd carrier
    0.0179738562092,
    -0.109283889209,
    -0.0968932328773,
    -0.06981386378,
    -0.041089676435,
    -0.017154548532,
)
HAMER_MS_NUM = (  # 0++ (scalar)
    -0.10637254902,
    -0.0259751057286,
    -0.1388695423,
    -0.1343376068,
    -0.099473993,
    -0.0232246442,
)
HAMER_MT_NUM = (  # 2++ (tensor) — external data with no in-program counterpart yet
    0.10931372549,
    0.0501374471357,
    0.00481356764,
    0.01315377296,
    0.00495936854,
    -0.00042445283,
)
HAMER_TOLERANCE = 5.3e-13

#: Kogut-Pearson-Shigemitsu, "The string tension, confinement and roughening
#: in SU(3) Hamiltonian lattice gauge theory" (KPS_1981 in the literature
#: index). Transcribed 2026-08-21 from the KEK library scan of the September
#: 1980 preprint ILL-(TH)-80-41, pinned by digest in literature/index.yaml;
#: the Phys. Lett. B 98 (1981) 63 journal pages remain unread. Conventions,
#: eqs. (1)-(2): H = (g**2/2a)(Sum E**2 - x Sum tr[U(p)+h.c.]), x = 2/g**4
#: = 2u, T = (g**2/2a**2) W(x), W(x) = Sum t_n x**n -- the same electric
#: normalization and coupling as the Hamer table, so the same
#: sigma_n = 2**(n-1) t_n bridge. Table 2 (3+1 dimensions) prints the t_n as
#: EXACT rationals ("the glorious, exact coefficients", computed in MACSYMA);
#: they are Rational here because the paper's own printing is exact, and the
#: published-comparisons suite holds them against the certified SIGMA_n.
#: The t_2..t_5 transcriptions are confirmed EXACTLY by that agreement; t_6
#: has no certified counterpart yet (it is the published target for G7's
#: native sigma_6 rerun), so its 56-digit numerator rests on the scan plus
#: agreement with the paper's own 7-digit float (5.8e-11) -- a future native
#: run must re-verify the digit string, not trust this transcription.
KPS_T0 = Rational(4, 3)
KPS_T2 = Rational(-11, 153)
KPS_T3 = Rational(-61, 1632)
KPS_T4 = Rational(-737327120374220449, 58004722308819686400)
KPS_T5 = Rational(-137767222189182735950309, 32156851302637820478720000)
KPS_T6 = Rational(
    -13130661661034190772935959348816444649800714410750015999,
    5396526208239719926042764329601696551230239968145408000000,
)
#: The same series as eq. (6a) prints it, W(x) = 4/3 (1 + sum w_n x**n),
#: w_n = t_n / (4/3), 7 printed digits, n = 2..6. Kept beside the exact
#: table so the internal cross-check (floats vs rationals, one printed ulp)
#: guards the transcription of both.
KPS_W_NUM = (
    -0.05392157,
    -0.02803309,
    -0.009533626,
    -0.003213169,
    -0.001824877,
)

#: The errata-resolved EUCLIDEAN strong-coupling glueball series of the
#: Munster-Seo line, SU(3), 4 dimensions: am = -4 ln u + sum_k m_k u**k with
#: u the fundamental-character coefficient (Wilson action). EUCLIDEAN, not
#: Hamiltonian: corpus section 12 forbids comparing these against the
#: certified Gamma-point series — they are recorded as the corrected
#: published record and for the completion-family novelty scope, nothing
#: else. Two independent primary sources, both read 2026-08-21: Smit's
#: ITFA-82-3 Table 1 (KEK scan, sha256 in the SMIT_1982 stub), which credits
#: "G. Munster, private communication" and "K. Seo, EFI preprint (4/82)",
#: and — for the scalar channel — the definitive erratum Nucl. Phys. B205
#: (1982) 648 itself (maintainer-supplied copy, sha256 in the MUNSTER_1981
#: entry). The published-comparisons suite asserts the two transcriptions
#: agree exactly; the A and T channels rest on Smit's table alone.
SMIT_EUC_MS = (  # 0++ (S), k = 1..8
    Rational(-3),
    Rational(9),
    Rational(-27, 2),
    Rational(-7),
    Rational(-297, 2),
    Rational(858827, 10240),
    Rational(47641149, 71680),
    Rational(-179208453, 40960),
)
SMIT_EUC_MA = (  # 1+- (A), k = 1..8
    Rational(3),
    Rational(0),
    Rational(9, 2),
    Rational(-99, 4),
    Rational(33, 4),
    Rational(-36771, 1280),
    Rational(117897, 448),
    Rational(-1559, 2),
)
SMIT_EUC_MT = (  # 2++ (T), k = 1..8
    Rational(-3),
    Rational(9),
    Rational(-27, 2),
    Rational(17),
    Rational(-153, 2),
    Rational(1104587, 10240),
    Rational(29577789, 71680),
    Rational(-92578053, 40960),
)
#: The SU(3) row of the Nucl. Phys. B205 (1982) 648 erratum table itself —
#: transcribed independently of the Smit column above, so their exact
#: equality is a check on both transcriptions and on the claim that Smit's
#: openly scanned table IS the errata-resolved series.
MUNSTER_ERR_MS = (
    Rational(-3),
    Rational(9),
    Rational(-27, 2),
    Rational(-7),
    Rational(-297, 2),
    Rational(858827, 10240),
    Rational(47641149, 71680),
    Rational(-179208453, 40960),
)

#: Munster's 1985 effective-transfer-matrix paper (Nucl. Phys. B256 (1985)
#: 67, MUNSTER_1985_TM in the literature index; maintainer-supplied DESY
#: 85-007 copy, sha256 in the index entry) recomputes the same Euclidean
#: SU(3) mass series by an independent method — an effective matrix on the
#: degenerate plaquette-orientation triplet — and its Table 1 DISAGREES
#: with the 1982 erratum at exactly eighth order: m_8 shifts by -96 for
#: SU(3) (and by -32, -18, -1/6 for Z3, SU(infinity), U(1)-Wilson, whose
#: u^6 also shifts by -1/8), while SU(2), Z2, U(1)-Villain and every lower
#: order agree. A FINDING check in the published suite asserts the shift;
#: neither side is promoted — this repository records the discrepancy in
#: Munster's own corrected line, it does not adjudicate it. Euclidean, as
#: above: no Hamiltonian comparison exists or is permitted.
MUNSTER_TM_MS = (
    Rational(-3),
    Rational(9),
    Rational(-27, 2),
    Rational(-7),
    Rational(-297, 2),
    Rational(858827, 10240),
    Rational(47641149, 71680),
    Rational(-183140613, 40960),
)
#: The same paper's dispersion decomposition for the SU(3) scalar glueball,
#: E(p) = m + f p^2 + g ((p^2)^2 - 3 sum p_i^4) + h (p^2)^2 + O(p^6):
#: f_k for k = 4..8, g_k for k = 4..8, and h_8. The g series is the
#: CUBIC-HARMONIC (shape) channel — the Euclidean counterpart of the role
#: the disputed off-axis coefficient C_shp plays in the Hamiltonian band —
#: which is why it is recorded; its values transfer nothing across the
#: regime boundary.
MUNSTER_TM_F = (
    Rational(7, 3),
    Rational(7),
    Rational(3, 2),
    Rational(-25),
    Rational(1771, 8),
)
MUNSTER_TM_G = (
    Rational(-1, 27),
    Rational(-1, 9),
    Rational(7, 108),
    Rational(5, 12),
    Rational(533, 216),
)
MUNSTER_TM_H8 = Rational(-25, 18)

#: The sibling-group entries the eighth-order FINDING names, registered so
#: the check certifies every shift it asserts rather than only SU(3)'s.
#: Order: (Z3 m_8, SU(infinity) m_8, U(1)-Wilson m_6, U(1)-Wilson m_8);
#: _ERR_ rows from the NPB 205 (1982) 648 erratum table, _TM_ rows from the
#: NPB 256 (1985) Table 1, both read at 200 dpi from the pinned copies.
#: Euclidean, comparison-only, like everything in this block.
MUNSTER_ERR_SIB = (
    Rational(-8207, 8),
    Rational(-546),
    Rational(-445, 6),
    Rational(-1659829, 2880),
)
MUNSTER_TM_SIB = (
    Rational(-8463, 8),
    Rational(-564),
    Rational(-1783, 24),
    Rational(-1660309, 2880),
)

#: Rejected by both sides; recorded so it is never silently resurrected.
QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600)
RAW_FOLDED_AXIAL_GAMMA_NUM = -11.9485781794007
#: Exact gate value for the linked vacuum O(u**4) subtraction around the mark.
LINKED_VACUUM_4 = Rational(-1474623, 1675520)
#: The float-reconstruction that RUN15 printed instead (C20).
LINKED_VACUUM_4_ARTIFACT = Rational(-521965902, 593076541)
#: Diagonal shift actually applied in the 15-hour run. Target-derived, NOT
#: DELTA_GAMMA_NUM, and disclosed as such (GLUEBALL §9.2; C22).
RUN15_APPLIED_SHIFT_NUM = 11.17343231638178

#: Cross-coefficient of the historical fourth-order sum-of-squares numerator.
Q4_CROSS = Rational(17607806155349, 1101327605164800)  # = BETA_PEN_3 / 4

# --------------------------------------------------------------------------
# Isotropic pentagonal-prism cap band  (UNIFIED v4.3 §9.3, PROVEN for its
# own retained sector -- a *separate geometry*, outside the cubic SU(3) kernel)
# --------------------------------------------------------------------------
# Standard isotropic Kogut-Susskind electric Hamiltonian H_0 = (1/2) sum_e E_e^2.
# The two face energies differ, which is what forces the choice of physical
# degenerate eigenspace before anything else (C8, R21).


def electric_energy(length, n=N):
    """Rest energy of a simple fundamental-flux loop of `length` links.

    THE electric convention, in one place: H_0 = (1/2) sum_e E_e^2, so each
    excited link costs C_F/2 with C_F = (N**2-1)/(2N). E_CAP and E_SIDE below
    are its length-5 and length-4 SU(3) values, and workhouse.cellular's
    resolvent denominators (E_0 - E_j)/C_F = (l_0 - l_j)/2 are the same
    convention in C_F units — the cellular suite checks the coincidence.
    """
    n = sympify(n)
    return sympify(length) * (n**2 - 1) / (4 * n)


E_CAP = electric_energy(5, 3)  # = 10/3, the pentagonal cap face
E_SIDE = electric_energy(4, 3)  # = 8/3, a square face; also e_flat(0)

#: Endpoint subtotals over the 48 fixed-side histories; their difference IS the
#: coefficient, derived by two independent backends without embedding the target.
PENT_A_PLUS = Rational(6482621, 21879000)
PENT_A_MINUS = Rational(9714969, 32784500)
#: h_4^side = A_+ - A_-.
H4_SIDE = Rational(-2861009, 84387303000)
#: tau_4, from h_4^side by exact D_5 covariance. The factor is 5 = |C_5|, and
#: recording it here is the point: an undocumented multiplier between two
#: printed coefficients is indistinguishable from a transcription error.
D5_COVARIANCE_FACTOR = 5
TAU_4 = Rational(-2861009, 16877460600)

# --------------------------------------------------------------------------
# Pentagonal FIFTH order (2026-08-28 master edition, section 15)
# --------------------------------------------------------------------------
# Asserted by the master edition, not derived here: two target-blind direct
# routes across all 796 histories, plus a second ledger over all 572 canonical
# returns matching the dual-backend derivative fold. T3 until something here
# recomputes the histories. What IS checked is the record's internal
# arithmetic -- see "the fifth-order record is arithmetically self-consistent".
#
# SIGN CONVENTION, recorded because it is the whole difference between the two
# printed forms: these are for H = H_0 + u W. For H = H_0 - u W the coefficient
# reverses sign. An unrecorded convention is how a sign erratum is born.
C5_DIRECT = Rational(37373840041427, 407461473619200)  # 796 direct histories
C5_FOLDED = Rational(110572494623989, 1898991175363682400)  # 572 canonical returns
C5_PENT = Rational(4183029870024709967, 45575788208728377600)  # their sum, H = H_0 + uW
#: Coefficient of u^4 cos k in Delta E_cap^(4). The factor 2 is the two terms
#: of the Hermitian hop |z><z+1| + |z+1><z|, not a second convention.
HOP_HERMITIAN_FACTOR = 2
DELTA_E_CAP_4 = Rational(-2861009, 8438730300)
#: Continuous fourth-order bandwidth 4|tau_4|; band minimum at k = 0.
PENT_BANDWIDTH_4 = Rational(2861009, 4219365150)
#: Hop range: nearest-neighbour cap transfer only, 240 = 5 x 48 histories each way.
PENT_HOP_RANGE = 4
PENT_HISTORIES_PER_DIRECTION = 240
PENT_FIXED_SIDE_HISTORIES = 48
#: The formal cap-plus-side compression mu(k) belongs to a DIFFERENT, tuned
#: Hamiltonian with w_vertical = (3/2) w_horizontal. The isotropic h_4^side may
#: not be transferred to it (R21).
PENT_TUNED_WEIGHT_RATIO = Rational(3, 2)


# --------------------------------------------------------------------------
# Native string tension through fifth order  (UNIFIED v4.3 §11.2)
# --------------------------------------------------------------------------
#: sigma(u) in the canonical *physical* perturbation convention.
SIGMA_0 = Rational(2, 3)
SIGMA_2 = Rational(-22, 153)
SIGMA_3 = Rational(-61, 408)
SIGMA_4 = Rational(-737327120374220449, 7250590288602460800)
SIGMA_5 = Rational(-137767222189182735950309, 2009803206414863779920000)
#: The native engine reconstructs positive unit-insertion magnitudes; the
#: physical series follows from V = -sum_p (chi_p + chi_p_bar), giving
#: sigma_n^phys = (-1)^n sigma_n^raw. C5's -61/408 is the n = 3 instance.
SIGMA_5_RAW = -SIGMA_5
#: Seven-prime CRT reconstruction: 189-bit modulus, so the uniqueness bound is
#: 94 bits and the recovered 77-bit numerator and 81-bit denominator clear it.
SIGMA_5_CRT_PRIMES = 7
SIGMA_5_MODULUS_BITS = 189
SIGMA_5_UNIQUENESS_BITS = 94
SIGMA_5_TOPOLOGIES = 22820

#: Scale-matched ratio m_{1+-}/sqrt(sigma), undisputed part only: the u^4 and
#: higher coefficients inherit the fourth-order mass-kernel dispute (C2).
RATIO_UNDISPUTED = (Rational(4, 3), Rational(1, 2), Rational(11, 68), Rational(-7559, 499392))


# --------------------------------------------------------------------------
# Exceptional (determinant) sectors
# --------------------------------------------------------------------------
DELTA_BETA_3 = Rational(-25, 64)
DELTA_Q_3 = Rational(-16863189551, 76406976000)
DELTA_Q_6 = Rational(6, 343)
#: A fourth-order word carries at most 6 character factors, so determinant
#: channels need |p-q| = N <= 6: the exceptional set is exactly {3,4,5,6}.
EXCEPTIONAL_RANKS = (3, 4, 5, 6)


# --------------------------------------------------------------------------
# Primitive cell-completion family (G5 / C15)
# --------------------------------------------------------------------------
# The corpus's restricted primitive color law (transcript
# #-Final-unified-theory.txt ~148-173; GLUEBALL v3_1 ~1174, unsigned form):
#
#     c_{r,prim}(N) = S_r/(N^r C_F^(r-1)) = 2^(r-1) S_r/(N (N^2-1)^(r-1)),
#
# printed table: tetrahedron r=2, triangular prism (square sector) r=3, cube
# (opposite faces) r=4, pentagonal prism (cap sector) r=5. The tetrahedral row
# is asserted with NO artifact and NO reference SHA anywhere in the corpus
# (C15; the restored-payloads FINDING pins the absence) — its corpus evidence
# level is prose-only, and it is certified only because workhouse.cellular
# re-derives it (G5, T1). These are PRIMITIVE simple-loop-channel values:
# folded/linked terms, Fierz side channels, and determinant sectors are outside
# the law by its own statement (the SU(3) fifth-order determinant dressing
# corrects the pentagonal row's physical value — C18).
_C_PRIM_NUMERATORS = {2: Rational(-8), 3: Rational(64), 4: Rational(-160), 5: Rational(1120)}


def c_prim_printed(r, n=N):
    """The corpus's printed primitive completion coefficient at order r."""
    n = sympify(n)
    return _C_PRIM_NUMERATORS[r] / (n * (n**2 - 1) ** (r - 1))


#: SU(3) values of the printed rows. The cube row's is CUBE_COMPLETION_4 above.
TETRA_COMPLETION_2_SU3 = Rational(-1, 3)
PRISM_COMPLETION_3_SU3 = Rational(1, 3)
PENT_COMPLETION_5_SU3 = Rational(35, 384)
#: The shipped notebook's CAP-sector value for the triangular prism
#: (NB_HAAR_prismatic_minimal_cell_escape_test.ipynb, 24/24 gates). NOT a rival
#: of PRISM_COMPLETION_3_SU3: same cell, different endpoint sector (caps vs the
#: retained vertical squares). 818.txt ~3402 records the supersession of 24 by
#: 64 as the choice of physical sector, not an arithmetic correction.
PRISM_CAP_COMPLETION_3_SU3 = Rational(1, 8)
#: Printed third-order prism bandwidth: 6 * c_3(3) (THM_FLUX §3.2).
PRISM_BANDWIDTH_3_SU3 = Rational(2)


# --------------------------------------------------------------------------
# Homology / finite volume
# --------------------------------------------------------------------------
def dim_z2(extent=L):
    """dim ker(partial_2) on T_L^3 = (L**3 - 1) cube boundaries + 3 harmonic planes."""
    return sympify(extent) ** 3 + 2


REGISTRY: tuple[Constant, ...] = (
    Constant(
        "t_N",
        hopping(),
        "proven",
        "analytic",
        "MASTER_THEORY §4.3",
        "positive for N>=3; t_2 = 0; t_3 = 5/612",
    ),
    Constant(
        "E_flat(u)",
        e_flat(),
        "proven",
        "cold-reproduced",
        "MASTER_THEORY §4.4",
        "k-independent through O(u**3)",
    ),
    Constant(
        "A_shp_3",
        A_SHP_3,
        "proven",
        "analytic",
        "MASTER_THEORY §5.2",
        "sealed: both disputed kernels agree",
    ),
    Constant(
        "alpha_pen_N",
        alpha_pen(),
        "conditional",
        "output-certified",
        "MASTER_THEORY §5.3",
        "conditional on the historical kernel family",
    ),
    Constant(
        "q_band^(4)",
        Q_BAND_4,
        "proven",
        "output-certified",
        "MASTER_THEORY §5.5",
        "band-kernel anchor; not a competing estimate of m_Gamma^(4)",
    ),
    Constant(
        "m_Gamma^(4)",
        M_GAMMA_4_NUM,
        "conditional",
        "numerical",
        "MASTER_THEORY §5.5",
        "vacuum-subtracted Gamma-point coefficient; blind match to Hamer a_4",
    ),
    Constant(
        "C_shp (historical)",
        C_SHP_HISTORICAL,
        "disputed",
        "output-certified",
        "MASTER_THEORY §5.5",
        "C2 — the one genuinely open fourth-order coefficient",
    ),
    Constant(
        "C_shp (v10a.26)",
        C_SHP_NEW_NUM,
        "disputed",
        "numerical",
        "MASTER_THEORY §5.5",
        "C2 — the one genuinely open fourth-order coefficient",
    ),
    Constant(
        "Hamer a_4",
        HAMER_A4_NUM,
        "conditional",
        "record-backed",
        "GLUEBALL §2.3",
        "notebook transcription; primary table not hashed",
    ),
    Constant(
        "quarantined scalar",
        QUARANTINED_SCALAR,
        "falsified",
        "record-backed",
        "MASTER_THEORY §5.5",
        "rejected by both sides",
    ),
    Constant(
        "c_2^tet (primitive)",
        c_prim_printed(2),
        "conditional",
        "prose-only",
        "transcript #-Final-unified-theory ~170; THM_FLUX mobility theorem §5",
        "asserted with no artifact or reference SHA (C15); re-derived at T1 by "
        "workhouse.cellular (G5) — conditional on the primitive-channel scope",
    ),
)


# --------------------------------------------------------------------------
# The old-to-new crosswalk
# --------------------------------------------------------------------------
def cubic_invariants(k):
    """The Bloch scalars (q, e_2, e_3) of a_i = 4 sin^2(k_i/2).

    The single home of the cubic-invariant basis (U2's claim is that every
    fourth-order shape coefficient is a symmetric function of exactly these).
    Built here once so phi_c, the extraction ansatz, and the tier-collapse
    analysis cannot drift into three separately edited copies.
    """
    from sympy import sin as _sin

    a = [4 * _sin(sympify(ki) / 2) ** 2 for ki in k]
    q = a[0] + a[1] + a[2]
    e2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
    e3 = a[0] * a[1] * a[2]
    return q, e2, e3


def phi_c(k):
    """Off-axis shape function Phi_C(k) = 4*e_2(k)/Q(k).

    Since e_2 = O(|k|**4) and Q = O(|k|**2), Phi_C = O(|k|**2), so its
    continuous extension satisfies Phi_C(0) = 0 along every direction. That is
    exactly why a Gamma-point scalar can pin the anchoring offset while leaving
    the off-axis kernel wholly unconstrained.
    """
    q, e2, _e3 = cubic_invariants(k)
    return 4 * e2 / q


def crosswalk(c_old, k):
    """c_4_new(k) = c_4_old(k) + Delta_Gamma + Delta_C * Phi_C(k).

    The scalar term re-anchors and moves nothing observable. Only the Phi_C
    term can change the dispersion, so bandwidth is preserved only if DELTA_C_NUM
    vanishes or is absorbed by an exact operator identity. Neither is
    established.
    """
    return c_old + DELTA_GAMMA_NUM + DELTA_C_NUM * phi_c(k)
