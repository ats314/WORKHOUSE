#!/usr/bin/env python3
"""
Real-world predictions of the SU(N) strong-coupling glueball program, confronted with
lattice data (Athenodorou-Teper, arXiv:2106.00364, continuum-extrapolated, units of sqrt(sigma)).

Three results, ordered by how *controlled* each is:

  TIER 1  (fully controlled, lattice-confirmed): the spectrum ORDERING 0++ < 2++ < 1+-,
          and the EXISTENCE of the 1+- only for N>=3.  These are sign/ordering statements,
          NOT convergent-series claims -- so they are immune to the divergent-series problem.

  TIER 2  (exact, parameter-free, but N-scaling mismatched): the leading-order ratio
          m(1+-)/sqrt(sigma) = 2*sqrt((N^2-1)/N) ~ 2 sqrt(N), which diverges, while the
          lattice ratio is N-independent (-> 5.76).  This precisely demarcates where the
          strong-coupling expansion and the continuum part ways.

  TIER 3  (consistent, not controlled): Borel-Pade resummation of the divergent rest-mass
          series, using the CORRECT band-minimum coefficient c4(Gamma) = -2.857916.

Usage:  python3 ENGINE_SUN_realworld_predictions.py  DATA_SUN_glueball_jpc_core_benchmark_v2.csv
"""
import sys, csv, math
from fractions import Fraction as F
import numpy as np, mpmath as mp
mp.mp.dps = 40

CSV = sys.argv[1] if len(sys.argv) > 1 else 'DATA_SUN_glueball_jpc_core_benchmark_v2.csv'

# ---------- load lattice data ----------
lat = {}
with open(CSV) as f:
    for row in csv.DictReader(f):
        lat[row['N_label']] = {
            'm0': float(row['m_0pp']) if row['m_0pp'] else None,
            'm2': float(row['m_2pp']) if row['m_2pp'] else None,
            'm1': float(row['m_1pm']) if row['m_1pm'] else None,
            'e1': float(row['err_1pm']) if row['err_1pm'] else None,
            'invN2': float(row['inv_N2']),
        }

# ======================================================================================
# TIER 1a -- ORDERING 0++ < 2++ < 1+-  from the certified SU(3) strong-coupling band edges
# ======================================================================================
# Exact band edges (gate-backed: ENGINE_FLUX_glueball_band_certificate_v2.py 36 gates; flat-band theorem).
# O(y) coefficient is the eigenvalue of PWP = charge conjugation (verified [[0,1],[1,0]]):
#   +1 on C-even -> h1=-1 -> -y ;  -1 on C-odd -> h1=+1 -> +y.
m_0pp = {0: F(8,3), 1: F(-1), 2: F(-217,1020)}   # A1++  scalar  (lowest C-even branch)
m_2pp = {0: F(8,3), 1: F(-1), 2: F( 223,1020)}   # E++   tensor
m_1pm = {0: F(8,3), 1: F( 1), 2: F(  11, 306)}   # T1+-  (exactly flat C-odd band)

val = lambda s, y: sum(float(c)*y**k for k, c in s.items())

print("="*78)
print("TIER 1a -- spectrum ordering 0++ < 2++ < 1+-  (exact, gate-backed, robust in y)")
print("="*78)
print("  0++ (A1++):  8/3 - y - (217/1020) y^2     [C-even: PWP eigenvalue +1 -> -y]")
print("  2++ (E++ ):  8/3 - y + (223/1020) y^2     [C-even: PWP eigenvalue +1 -> -y]")
print("  1+- (T1+-):  8/3 + y + (11/306)  y^2      [C-odd : PWP eigenvalue -1 -> +y, flat]")
print()
d20 = F(223,1020) + F(217,1020)                 # m(2++) - m(0++) coefficient of y^2
print(f"  m(2++)-m(0++) = {d20} y^2 > 0  for all y      => 0++ < 2++ (exact)")
print(f"  m(1+-)-m(2++) = 2y + ({F(11,306)-F(223,1020)}) y^2 ; the +2y term (C-parity)")
print(f"                  dominates -> 1+- is the heaviest up to y ~ "
      f"{float(2/abs(F(11,306)-F(223,1020))):.0f} (past where the leading series is valid)")
print()
print(f"  {'y':>5} | {'m0++':>7} {'m2++':>7} {'m1+-':>7} | ordering")
for y in (0.3, 0.6, 1.0, 1.5, 2.0):
    a, b, c = val(m_0pp, y), val(m_2pp, y), val(m_1pm, y)
    order = " < ".join(s for _, s in sorted([(a,'0++'), (b,'2++'), (c,'1+-')]))
    print(f"  {y:>5} | {a:>7.3f} {b:>7.3f} {c:>7.3f} | {order}")

# ======================================================================================
# TIER 1b -- EXISTENCE: the 1+- requires complex reps (N>=3); SU(2) has none
# ======================================================================================
print()
print("="*78)
print("TIER 1b -- existence of the 1+- channel")
print("="*78)
print("  The 1+- single-plaquette operator is Im Tr(U_p).  For SU(2), Tr(U) is real")
print("  (U ~ U*), so Im Tr(U_p) == 0: NO C-odd single-plaquette glueball.  The channel")
print("  exists only for N>=3 (complex fundamental).  Lattice: SU(2) row has no 1+-.")
print(f"    SU(2) m(1+-) in data = {lat['2']['m1']}   (absent, as predicted)")

# ======================================================================================
# Lattice confirmation of TIER 1 across all N
# ======================================================================================
print()
print("  Lattice ordering check, every N (Athenodorou-Teper):")
print(f"  {'N':>4} | {'m0++':>6} {'m2++':>6} {'m1+-':>6} | holds")
for N in ('2','3','4','5','6','8','10','12','inf'):
    d = lat[N]
    if d['m1'] is None:
        print(f"  {N:>4} | {d['m0']:>6.3f} {d['m2']:>6.3f} {'  -  ':>6} | 0++<2++ {d['m0']<d['m2']} (no 1+-)")
    else:
        print(f"  {N:>4} | {d['m0']:>6.3f} {d['m2']:>6.3f} {d['m1']:>6.3f} | {d['m0']<d['m2']<d['m1']}")

# ======================================================================================
# TIER 2 -- exact leading-order SU(N) ratio vs lattice  (the N-scaling demarcation)
# ======================================================================================
# E_link = (1/2) C2(fund) = (N^2-1)/(4N) ; sigma a^2 = E_link ; 1+- band = 4 E_link.
#   m(1+-)/sqrt(sigma)|_0 = (N^2-1)/N / sqrt((N^2-1)/(4N)) = 2*sqrt((N^2-1)/N).
sc = lambda N: 2.0*math.sqrt((N*N-1)/N)
print()
print("="*78)
print("TIER 2 -- exact leading-order ratio  m(1+-)/sqrt(sigma) = 2*sqrt((N^2-1)/N)")
print("="*78)
print(f"  {'N':>4} | {'lattice':>14} | {'SC leading':>11} | SC/lat")
for N in ('3','4','5','6','8','10','12'):
    d = lat[N]; s = sc(int(N))
    print(f"  {N:>4} | {d['m1']:>7.3f}+/-{d['e1']:<5.3f} | {s:>11.3f} | {s/d['m1']:.2f}")
print(f"  {'inf':>4} | {lat['inf']['m1']:>7.3f}+/-{lat['inf']['e1']:<5.3f} | "
      f"{'-> inf (~2 sqrt N)':>11} |  div")
a = (lat['inf']['m1']/2)**2
Ncross = (a + math.sqrt(a*a+4))/2
print(f"\n  Lattice: N-INDEPENDENT, N=inf limit 5.76(25).  SC leading: ~2 sqrt(N), DIVERGES.")
print(f"  They cross near N ~ {Ncross:.1f} (accidental: a rising sqrt-N line through a flat band).")
print(f"  => the leading SC ratio has the WRONG large-N scaling; this is the precise")
print(f"     statement of why strong coupling != continuum for this observable.")

# ======================================================================================
# TIER 3 -- continuum extrapolation with the CORRECT rest-mass coefficient
# ======================================================================================
c4_rest = F(-20721577909065127111, 7250590288602460800)   # band minimum c4(Gamma) = -2.857916
a_coeffs = [F(8,3), F(1), F(11,306), F(-109151,249696), c4_rest]
K0 = 2.0/3.0
af = [float(x) for x in a_coeffs]
borel = [mp.mpf(str(af[i]))/mp.factorial(i) for i in range(5)]
print()
print("="*78)
print("TIER 3 -- Borel-Pade resummation, rest-mass series (correct c4 = -2.857916)")
print("="*78)
print(f"  coeffs a0..a4 = {[f'{x:.4f}' for x in af]}  (magnitudes grow -> divergent)")
for (L, M) in [(2,1), (1,1), (1,2), (1,3)]:
    p, q = mp.pade(borel, L, M)
    Bp = lambda t, p=p, q=q: (sum(p[i]*t**i for i in range(len(p))) /
                              sum(q[i]*t**i for i in range(len(q))))
    vals = []
    for y in (1.5, 2.0, 2.5):
        v = mp.quad(lambda t: mp.e**(-t)*Bp(y*t), [0, mp.inf])
        vals.append(f"y={y}:{float(v)/np.sqrt(K0):6.3f}")
    print(f"  [{L}/{M}]: " + "  ".join(vals))
print("  Stable [2/1],[1/1] cross the lattice 6.07 near y~2.3-2.5 but the series is")
print("  divergent: CONSISTENT, not controlled.  (Gated on the O(y^5+) inter-plaquette")
print("  leakage; the H5 folded-coefficient identity for it is derived & validated.)")
