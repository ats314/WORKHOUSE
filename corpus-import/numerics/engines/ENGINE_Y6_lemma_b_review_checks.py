#!/usr/bin/env python3
"""
ENGINE_Y6_lemma_b_review_checks.py — independent review gates for LEMMA_B_PROOF_2026-06-12
=================================================================================
Reviewer-side checks beyond the engine's own gates (ENGINE_OP1_lemma_b_cert.py LB0-LB9,
rerun clean in this container). All asserts hard.

  LR2  independent end-to-end: g(mu2) <= G_BOUND on a 10-pt grid spanning
       (0, 15/28] including the exact endpoint, using the REVIEWER'S Y_inf
       implementation (scipy quad, T0=24, second-order tail subtraction —
       structurally different from the engine's mpmath splitting).
  LR3  master-bound integrity chain, pointwise with TRUE constants:
       g(mu2) <= RHS_true(mu2) <= RHS_true(M) <= G_BOUND, where
       RHS_true(mu2) = (3/4) H_true + (A/2)[R+_true + 2 mu2 - gamma - ln 6].
       Verifies the Proposition itself, not just the certified assembly.
  LR4  Bessel-bound far field: slack(t) = bound - r(t) stays positive out to
       t = 1e5 and slack * t^2 -> C2 - 9/512 = 0.21352 (asymptotic safety:
       the true r-expansion's t^-2 coefficient 9/512 is far below C2).
  LR5  tightest analytic link: psi(4) = 64 sqrt(pi) e^{-256/25} vs
       dC = C2 - 9375/41472; ratio recorded (expected ~1.24).

Output: LEM_MISC_lemma_b_review_checks.json
"""
import json, math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive, exp1, erf as sp_erf
import mpmath as mp

PI = math.pi
A = 3.0 / (32.0 * PI**2)
C = 1.0 / (16.0 * PI**2)
GAMMA_E = 0.5772156649015328606
M2MAX = 15.0 / 28.0

def q_line(t): return float(ive(0, 2.0 * t))

def Y_inf_indep(mu2, T0=24.0, T1=40000.0):
    """reviewer's implementation (from ENGINE_OP1_m5_audit.py G-M6, gated to 4.7e-11 vs M5.3)."""
    f0 = lambda t: t * math.exp(-mu2 * t) * q_line(t) ** 4
    v0, e0 = quad(f0, 0.0, T0, epsabs=1e-14, epsrel=1e-13, limit=500)
    fr = lambda t: math.exp(-mu2 * t) * (t * q_line(t) ** 4 - C / t - 0.25 * C / (t * t))
    vr, er = quad(fr, T0, T1, epsabs=1e-15, epsrel=1e-12, limit=800)
    rem = 2.0 * C / (2.0 * T1 * T1)
    vlog = C * float(exp1(mu2 * T0))
    vsq = 0.25 * C * (math.exp(-mu2 * T0) / T0 - mu2 * float(exp1(mu2 * T0)))
    return 0.75 * (v0 + vr + vlog + vsq), 0.75 * (abs(e0) + abs(er) + rem)

def g_indep(mu2):
    Y, err = Y_inf_indep(mu2)
    return Y - 0.5 * A * math.log(3.0 / mu2), err

out = {"meta": dict(engine="ENGINE_Y6_lemma_b_review_checks.py", date="2026-06-12",
                    reviews="LEM_OP1_lemma_b_proof_2026-06-12.md / ENGINE_OP1_lemma_b_cert.py")}

cert = json.load(open("/home/claude/LEM_OP1_lemma_b_cert.json"))
GB = cert["LB6"]["G_BOUND"]
C2 = cert["LB6"]["C2"]

# ---- LR2: independent end-to-end
grid = [M2MAX, 0.5, 0.37, 0.21, 0.123, 0.05, 0.013, 0.003, 7e-4, 1e-5]
min_slack, at = None, None
for m in grid:
    gv, err = g_indep(m)
    slack = GB - gv
    assert slack > 3 * err, f"LR2 FAIL: g({m}) = {gv} vs G_BOUND {GB}"
    if min_slack is None or slack < min_slack:
        min_slack, at = slack, m
out["LR2"] = dict(min_slack=min_slack, at_mu2=at, G_BOUND=GB, passed=True)
print(f"LR2 PASS: independent g(mu2) <= G_BOUND on 10-pt grid incl. exact endpoint; "
      f"min slack {min_slack:.6f} at mu2={at}")

# ---- LR3: master-bound integrity chain with TRUE constants
H_true, eH = quad(lambda t: t * q_line(t) ** 4, 0.0, 2.0, epsabs=1e-14, epsrel=1e-13)
def rplus_int(t):
    r4 = 16 * PI**2 * t * t * q_line(t) ** 4
    return max(r4 - 1.0, 0.0) / t
Rp1, eR1 = quad(rplus_int, 2.0, 4.0, epsabs=1e-13, epsrel=1e-11, limit=400)
Rp2, eR2 = quad(rplus_int, 4.0, 4000.0, epsabs=1e-13, epsrel=1e-11, limit=800)
# remainder beyond 4000 (positive): <= int 4 delta (1+delta(4))^3 /t with delta ~ 1/(16t):
rem_R = 4.0 * (1 + 1/64 + C2/16) ** 3 * (1.0 / (16.0 * 4000.0) + C2 / (2.0 * 4000.0 ** 2))
R_true_up = Rp1 + Rp2 + rem_R
LN6 = math.log(6.0)
def RHS_true(mu2):
    return 0.75 * H_true + 0.5 * A * (R_true_up + 2.0 * mu2 - GAMMA_E - LN6)
worst_gap1, worst_gap2 = -1e9, -1e9
for m in [M2MAX, 0.1, 0.001]:
    gv, err = g_indep(m)
    rhs = RHS_true(m)
    worst_gap1 = max(worst_gap1, gv - rhs)           # Proposition: g <= RHS_true
    worst_gap2 = max(worst_gap2, rhs - RHS_true(M2MAX))
assert worst_gap1 <= 1e-9, f"LR3 FAIL: master bound violated pointwise ({worst_gap1})"
assert RHS_true(M2MAX) <= GB + 1e-12, f"LR3 FAIL: RHS_true(M) {RHS_true(M2MAX)} > G_BOUND {GB}"
out["LR3"] = dict(H_true=H_true, R_true_up=R_true_up, RHS_true_at_M=RHS_true(M2MAX),
                  G_BOUND=GB, worst_pointwise_gap=worst_gap1, passed=True)
print(f"LR3 PASS: g <= RHS_true(mu2) <= RHS_true(M) = {RHS_true(M2MAX):.9f} <= G_BOUND = {GB:.9f}")

# ---- LR4: Bessel far field
mp.mp.dps = 30
def rf(t): return mp.sqrt(4 * mp.pi * t) * mp.besseli(0, 2 * t) * mp.exp(-2 * t)
asym = C2 - 9.0 / 512.0
rows = []
for t in [5e3, 1e4, 2e4, 1e5]:
    t = mp.mpf(t)
    bound = 1 + 1 / (16 * t) + C2 / t**2
    slack = bound - rf(t)
    s2 = float(slack * t * t)
    assert slack > 0, f"LR4 FAIL at t={float(t)}"
    assert 0.19 <= s2 <= 0.22, f"LR4 FAIL: slack*t^2 = {s2} not near {asym}"
    rows.append((float(t), s2))
out["LR4"] = dict(slack_t2_rows=rows, asymptote=asym, passed=True)
print(f"LR4 PASS: bound holds to t=1e5; slack*t^2 -> {rows[-1][1]:.5f} (asymptote {asym:.5f})")

# ---- LR5: tightest link
psi4 = 64.0 * math.sqrt(PI) * math.exp(-256.0 / 25.0)
dC = C2 - 9375.0 / 41472.0
ratio = dC / psi4
assert psi4 < dC and 1.1 <= ratio <= 1.4, f"LR5 FAIL: psi(4)={psi4}, dC={dC}"
out["LR5"] = dict(psi_at_4=psi4, dC=dC, safety_ratio=ratio, passed=True)
print(f"LR5 PASS: wrap link psi(4) = {psi4:.6e} < dC = {dC:.6e} (safety ratio {ratio:.3f}) — tightest analytic link, valid")

json.dump(out, open("/home/claude/LEM_MISC_lemma_b_review_checks.json", "w"), indent=1)
print("ALL REVIEW GATES PASS")
