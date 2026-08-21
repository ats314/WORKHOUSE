#!/usr/bin/env python3
# ENGINE_OP1_m4_ceiling_pin_audit.py — F028 verification engine for the uploaded
# NB_OP1_m5_tier_2_ceiling_pin_auditor.ipynb (md5 7740d39b). Audits the Tier-2
# "B-window" reduction and repairs its quantifier:
#
#   THEIR REDUCTION (verified exact): T̄(B) = (27/44)/(28/5 − (44/3)B);
#   T̄ = 1/8 at B = BCRIT = 57/1210 exactly. If Y_L = α²T_C ≤ A·ln s + B with
#   B ≤ BCRIT then T_C ≤ 1/8, N*_C ≥ 8, T_full < 9/64, N* ≥ 7.
#
#   FLAW (measured here): under the ∞-volume law, B(x) = D∞ + (A/2)ln α(x)
#   with D∞ constant ⇒ B crosses BCRIT at x ≈ 9819 — "for every integer
#   L ≥ 4" is asymptotically FALSE as stated.
#
#   REPAIRS (both verified):
#   A) window+tail: Tier-1 (PROVED, F027) gives T_C < 1/8 for x ≥ x₁ ≈ 2632;
#      hypothesis needed only on [0, x₁]; true B there ≤ B(x₁) ≈ 0.0409 (13% margin).
#   B) three-parameter majorant (recommended target): Y ≤ A·x + (A/2)ln α + D
#      for all x, with D ≤ D_crit ≈ 0.044752; measured D∞ = 0.021302 (and the
#      finite-L diagonal sits lower still, D_lattice ≤ 0.018356) ⇒ uniform
#      ≈2.10× headroom, no window.
#
# HARD GATES (assert):
#   P1  BCRIT algebra: T̄(57/1210) == 1/8 exactly in rationals (fractions)
#   P2  D-constancy: max |D(x) − D∞| ≤ 1e-8 over x ∈ [40, 2e4]
#   P3  crossing bracket: B(9818) < BCRIT < B(9820)
#   P4  Tier-1 takeover: tier1(x₁) < 1/8 ≤ tier1(x₁−1); and x₁ < x_cross
#   P5  D_crit: T̄_3par(D_crit) = 1/8 ± 1e-9, and D_crit > D∞ (headroom > 1)
# Output: AUDIT_OP1_m4_ceiling_pin.json
import json, math, os
import numpy as np
from fractions import Fraction
from scipy.special import ive, exp1

HERE = os.path.dirname(os.path.abspath(__file__))
b0 = 5.6; gam = 11/(8*math.pi**2); A = 3/(32*math.pi**2); BCRIT = 57/1210
EUG = 0.5772156649015329
xg, wg = np.polynomial.legendre.leggauss(64); T1 = 1.0e6

# P1 — exact rational check of the threshold algebra (A/gam = 3/44 exactly)
Bc = Fraction(57, 1210)
Tbar = Fraction(27, 44) / (Fraction(28, 5) - Fraction(44, 3) * Bc)
assert Tbar == Fraction(1, 8), f'GATE P1 FAIL: {Tbar}'
print('GATE P1 pass: T̄(57/1210) = 1/8 exactly (rational arithmetic)')

edges = np.concatenate([[0.0], np.geomspace(1e-4, T1, 140)])
HEAD = sum(float((0.5*(b-a)*wg*(t := 0.5*(b-a)*xg+0.5*(a+b))*ive(0, 2*t)**4).sum())
           for a, b in zip(edges[:-1], edges[1:]))

def TCinf(x):
    beta = b0 + gam*x; al = beta/6.0
    lnmu2 = math.log(0.5) - 2*x - math.log(al)
    if lnmu2 + math.log(T1) < -30:
        tail = (-EUG - lnmu2 - math.log(T1))/(16*math.pi**2)
        tot = HEAD
    else:
        mu2 = math.exp(lnmu2)
        tot = sum(float((0.5*(b-a)*wg*(t := 0.5*(b-a)*xg+0.5*(a+b))*np.exp(-mu2*t)*ive(0, 2*t)**4).sum())
                  for a, b in zip(edges[:-1], edges[1:]))
        tail = exp1(mu2*T1)/(16*math.pi**2)
    return (3/(4*al*al))*(tot + tail), al

B_of = lambda x: (lambda r: r[1]**2*r[0] - A*x)(TCinf(x))
D_of = lambda x: B_of(x) - (A/2)*math.log((b0+gam*x)/6)

# P2 — D-constancy
Ds = [D_of(x) for x in np.geomspace(40, 2e4, 25)]
Dinf = float(np.mean(Ds))
dev = max(abs(d-Dinf) for d in Ds)
assert dev <= 1e-8, f'GATE P2 FAIL: D spread {dev}'
print(f'GATE P2 pass: D(x) constant = {Dinf:.9f} (spread {dev:.1e} over x in [40, 2e4])')

# P3 — crossing bracket
assert B_of(9818) < BCRIT < B_of(9820), 'GATE P3 FAIL'
xc = 9819
print(f'GATE P3 pass: B(x) crosses BCRIT between x = 9818 and 9820 (quantifier fails beyond)')

# P4 — Tier-1 takeover (Tier-1 from F027, overflow-safe log form)
c0 = 25.323344671201777
t1B = lambda x: 3/(1024*((b0+gam*x)/6)**2)*(c0 + (4/3)**4*2*math.pi**2*(x + math.log(2) + math.log1p(0.25*math.exp(-min(x, 700)))))
lo, hi = 10.0, 1e5
while hi - lo > 0.25:
    m = 0.5*(lo+hi)
    if t1B(m) < 0.125: hi = m
    else: lo = m
x1 = math.ceil(hi)
assert t1B(x1) < 0.125 <= t1B(x1-1), 'GATE P4 FAIL: takeover bracket'
assert x1 < xc, 'GATE P4 FAIL: x1 >= crossing'
Bx1 = B_of(x1)
print(f'GATE P4 pass: Tier-1 gives T_C < 1/8 for x >= x1 = {x1}; x1 << crossing; '
      f'B(x1) = {Bx1:.6f}, window margin {BCRIT-Bx1:.6f} ({100*(BCRIT-Bx1)/BCRIT:.0f}%)')

# P5 — three-parameter D_crit
def Tbar3(D):
    X = np.linspace(0.0, 200.0, 400001)
    al = (b0 + gam*X)/6
    return float((36*(A*X + (A/2)*np.log(al) + D)/(b0 + gam*X)**2).max())
lo2, hi2 = 0.01, 0.06
while hi2 - lo2 > 1e-12:
    m = 0.5*(lo2+hi2)
    if Tbar3(m) > 0.125: hi2 = m
    else: lo2 = m
Dcrit = lo2
assert abs(Tbar3(Dcrit) - 0.125) <= 1e-9, 'GATE P5 FAIL: Tbar3(Dcrit) != 1/8'
assert Dcrit > Dinf, 'GATE P5 FAIL: no headroom'
print(f'GATE P5 pass: D_crit = {Dcrit:.9f}; D∞ = {Dinf:.9f}; uniform headroom ×{Dcrit/Dinf:.2f} '
      f'(lattice diagonal lower still: D ≤ 0.018356)')

json.dump({'meta': {'engine': 'ENGINE_OP1_m4_ceiling_pin_audit.py', 'audits': 'NB_OP1_m5_tier_2_ceiling_pin_auditor.ipynb (md5 7740d39b)',
                    'gates': 'P1 rational BCRIT; P2 D-constancy; P3 crossing bracket; P4 Tier-1 takeover; P5 D_crit'},
           'BCRIT': BCRIT, 'A': A, 'gamma': gam,
           'D_infty': Dinf, 'D_spread': dev, 'D_lattice_max_observed': 0.018355229678,
           'crossing_x': xc, 'tier1_takeover_x1': x1, 'B_at_x1': Bx1,
           'D_crit_3par': Dcrit, 'headroom_3par': Dcrit/Dinf,
           'patched_theorems': {
               'A_window_tail': 'Y <= A x + 57/1210 on [0, x1] (+ Tier-1 for x >= x1) => T_C <= 1/8, N*_C >= 8, N* >= 7 for ALL s',
               'B_three_param': 'Y <= A x + (A/2) ln alpha + D with D <= D_crit for all x => same floors, no window'}},
          open(os.path.join(HERE, 'AUDIT_OP1_m4_ceiling_pin.json'), 'w'), indent=1)
print('ALL GATES PASSED; wrote AUDIT_OP1_m4_ceiling_pin.json')
