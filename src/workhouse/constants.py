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

from sympy import Rational, Symbol, sympify

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

# --------------------------------------------------------------------------
# Third order, SU(3)  (MASTER_THEORY §4.4, COLD-CERTIFIED)
# --------------------------------------------------------------------------
B_3 = Rational(1975, 124848)  # third-order hopping
LEAK_3 = Rational(-12331, 249696)  # renamed from ell_3 to avoid collision with all-rank ell_N
D_3 = Rational(-109151, 249696)  # = 7/32 + 12*LEAK_3 - 4*B_3


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
# Fourth order — THE DISPUTE (MASTER_THEORY §5.5; C1, C2). Neither is promoted.
# --------------------------------------------------------------------------
#: Historical 189-record kernel: rest scalar at Gamma (exact rational).
Q_3_HISTORICAL = Rational(-20721577909065127111, 7250590288602460800)
#: Historical off-axis shape coefficient (exact rational) = (BETA_PEN_3 - 2*alpha)/16.
C_SHP_HISTORICAL = Rational(-211835444920651, 4405310420659200)
#: Historical diagonal coefficient.
BETA_PEN_3 = Rational(17607806155349, 275331901291200)

#: v10a.26 folded run + linked-cluster oracle (float only).
M_GAMMA_4_NUM = -0.7751458630189173
C_SHP_NEW_NUM = -0.020213328886166577

#: The two discrepancies. Signs follow the corpus: new minus historical.
DELTA_GAMMA = 2.0827701250956414  # M_GAMMA_4_NUM - Q_3_HISTORICAL
DELTA_C = 0.027873054295192174  # C_SHP_NEW_NUM - C_SHP_HISTORICAL

W4_HISTORICAL = 0.48061786909826
W4_NEW_NUM = 0.9265867378213348

#: Hamer-convention cross-check. a_4 is a notebook transcription that has NOT
#: been pinned to a hashed primary table (GLUEBALL §2.3) — a local normalization
#: check, not primary-source verification.
HAMER_A4 = -0.0968932328773
HAMER_TOLERANCE = 5.3e-13

#: Rejected by both sides; recorded so it is never silently resurrected.
QUARANTINED_SCALAR = Rational(-160506019419340168451, 14501180577204921600)
RAW_FOLDED_AXIAL_GAMMA = -11.9485781794007
#: Exact gate value for the linked vacuum O(u**4) subtraction around the mark.
LINKED_VACUUM_4 = Rational(-1474623, 1675520)
#: The float-reconstruction that RUN15 printed instead (C20).
LINKED_VACUUM_4_ARTIFACT = Rational(-521965902, 593076541)
#: Diagonal shift actually applied in the 15-hour run. Target-derived, NOT
#: DELTA_GAMMA, and disclosed as such (GLUEBALL §9.2; C22).
RUN15_APPLIED_SHIFT = 11.17343231638178

#: Cross-coefficient of the historical fourth-order sum-of-squares numerator.
Q4_CROSS = Rational(17607806155349, 1101327605164800)  # = BETA_PEN_3 / 4

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
        "q_3 (historical)",
        Q_3_HISTORICAL,
        "disputed",
        "output-certified",
        "MASTER_THEORY §5.5",
        "C1 — do not promote",
    ),
    Constant(
        "m_Gamma_4 (v10a.26)",
        M_GAMMA_4_NUM,
        "disputed",
        "numerical",
        "MASTER_THEORY §5.5",
        "C1 — do not promote",
    ),
    Constant(
        "C_shp (historical)",
        C_SHP_HISTORICAL,
        "disputed",
        "output-certified",
        "MASTER_THEORY §5.5",
        "C2 — scalar re-anchoring cannot reconcile",
    ),
    Constant(
        "C_shp (v10a.26)",
        C_SHP_NEW_NUM,
        "disputed",
        "numerical",
        "MASTER_THEORY §5.5",
        "C2 — scalar re-anchoring cannot reconcile",
    ),
    Constant(
        "Hamer a_4",
        HAMER_A4,
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
)
