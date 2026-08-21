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
DELTA_GAMMA = 2.0827701250956417
DELTA_GAMMA_AS_PRINTED = 2.0827701250956414
#: The residual off-axis discrepancy, C_new - C_old. This one is real.
DELTA_C = 0.027873054295192174

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
# Isotropic pentagonal-prism cap band  (UNIFIED v4.3 §9.3, PROVEN for its
# own retained sector -- a *separate geometry*, outside the cubic SU(3) kernel)
# --------------------------------------------------------------------------
# Standard isotropic Kogut-Susskind electric Hamiltonian H_0 = (1/2) sum_e E_e^2.
# The two face energies differ, which is what forces the choice of physical
# degenerate eigenspace before anything else (C8, R21).
E_CAP = Rational(10, 3)
E_SIDE = Rational(8, 3)

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


# --------------------------------------------------------------------------
# The old-to-new crosswalk
# --------------------------------------------------------------------------
def phi_c(k):
    """Off-axis shape function Phi_C(k) = 4*e_2(k)/Q(k).

    Since e_2 = O(|k|**4) and Q = O(|k|**2), Phi_C = O(|k|**2), so its
    continuous extension satisfies Phi_C(0) = 0 along every direction. That is
    exactly why a Gamma-point scalar can pin the anchoring offset while leaving
    the off-axis kernel wholly unconstrained.
    """
    from sympy import sin as _sin

    a = [4 * _sin(sympify(ki) / 2) ** 2 for ki in k]
    q = a[0] + a[1] + a[2]
    e2 = a[0] * a[1] + a[0] * a[2] + a[1] * a[2]
    return 4 * e2 / q


def crosswalk(c_old, k):
    """c_4_new(k) = c_4_old(k) + Delta_Gamma + Delta_C * Phi_C(k).

    The scalar term re-anchors and moves nothing observable. Only the Phi_C
    term can change the dispersion, so bandwidth is preserved only if DELTA_C
    vanishes or is absorbed by an exact operator identity. Neither is
    established.
    """
    return c_old + DELTA_GAMMA + DELTA_C * phi_c(k)
