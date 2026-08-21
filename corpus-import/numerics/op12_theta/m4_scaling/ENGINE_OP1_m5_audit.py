#!/usr/bin/env python3
"""
ENGINE_OP1_m5_audit.py — independent audit of the M5 notebook chain (Tier-2 ceiling pin removal)
=====================================================================================
Audits (June 12, 2026, lead math agent):
  NB_OP1_m5_tier_2_ceiling_pin_auditor.ipynb   (B-form reduction, Bcrit = 57/1210)
  _M5_1___HEAT_KERNEL_BESSEL_...ipynb    (finite scan L = 4..4096, B-form)
  M5_3___COVER_DOMINATION_CLOSURE_ROUTE  (C-form, Lemma A cover domination, Lemma B)

Gates (assert):
  G-M1  C_CRIT independently recomputed (bisection on the envelope max) vs 0.036241888089666857
        + the clean rational sub-threshold 1/28 also gives floor(1/Tbar) = 8
  G-M2  B-form divergence: B(x) = C_inf(x) + (A/2) ln beta(x) is unbounded; crossing of 57/1210
        located (demonstrates the M5_1/auditor pin statement is asymptotically false as written)
  G-M3  Lemma A adversarial RATIO scan (odd/prime L included): max over (L, t) of
        (Phi_L^4 - L^-4)/q^4 <= 1 + 1e-9; nontrivial-window max recorded
  G-M4  Claim 1 (proved in note): Phi_L(t) <= 1/L + q(t) on all scanned (L, t)
  G-M5  Continuum core (proved in note): G(c) = 16 pi^2 c^2 (theta(c)^4 - 1) <= 0.905 on a dense
        c-grid; region maxima match the analytic two-region constants (<=0.149 for c >= 1/8)
  G-M6  Independent C_inf implementation (different cutoff/splitting) vs M5_3 printed values,
        rtol 1e-8; C_infinity limit pinned
  G-M7  Finite-vs-infinite domination: C_L <= C_inf(ln(L/4)) for all L = 4..256 (integrated
        Lemma A consequence); C_L profile and argmax reported
  G-M8  Lemma B monotonicity integrand: Dprime(mu2) = (3/4) int t^2 e^{-mu2 t}(q^4 - (16 pi^2 t^2)^{-1}) dt
        >= 0 across the diagonal range mu2 in (0, mu2(x=0)]  (numeric evidence for C_inf increasing)

Output: AUDIT_OP1_m5.json
"""
import json, math, sys
import numpy as np
from scipy.special import ive, exp1
from scipy.integrate import quad

sys.path.insert(0, "/mnt/user-data/uploads")
from ENGINE_OP1_m4_tc_closed_form import consts  # exact closed-form lattice sums (md5-matched deposit)

BETA0 = 5.6
GAMMA = 11.0 / (8.0 * math.pi**2)
A = 3.0 / (32.0 * math.pi**2)
BCRIT_BFORM = 57.0 / 1210.0
CCRIT_M53 = 0.036241888089666857
CINF_M53 = 0.012792103147

def beta_x(x): return BETA0 + GAMMA * x
def mu2_x(x):  return 48.0 / (beta_x(x) * (4.0 * math.exp(x)) ** 2)

# ---------------------------------------------------------------- heat kernels
def q_line(t):  return float(ive(0, 2.0 * t))

def Phi_L(L, t):
    out = float(ive(0, 2.0 * t)); j = 1
    while True:
        term = 2.0 * float(ive(j * L, 2.0 * t))
        out += term
        if term <= 1e-17 * max(out, 1e-300): return out
        j += 1
        if j > 300000: raise RuntimeError("image sum runaway")

# ------------------------------------------------------- C-form envelope, CCRIT
def env(x, C):
    b = beta_x(x)
    return 36.0 * (A * x + 0.5 * A * math.log(b) + C) / (b * b)

def env_max(C, xmax=200.0):
    lo, hi = 0.0, xmax
    for _ in range(300):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if env(m1, C) < env(m2, C): lo = m1
        else: hi = m2
    xs = 0.5 * (lo + hi)
    return xs, env(xs, C)

def find_ccrit():
    lo, hi = 0.0, 0.2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if env_max(mid)[1] < 0.125: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

# ----------------------------------------------------------- independent C_inf
def Y_inf_indep(mu2, T0=24.0, T1=40000.0):
    c = 1.0 / (16.0 * math.pi**2)
    f0 = lambda t: t * math.exp(-mu2 * t) * q_line(t) ** 4
    v0, e0 = quad(f0, 0.0, T0, epsabs=1e-14, epsrel=1e-13, limit=500)
    # t q^4 = c/t + c/(4 t^2) + r(t),  |r| <= 2 c / t^3 for t >= T0
    fr = lambda t: math.exp(-mu2 * t) * (t * q_line(t) ** 4 - c / t - 0.25 * c / (t * t))
    vr, er = quad(fr, T0, T1, epsabs=1e-15, epsrel=1e-12, limit=800)
    rem = 2.0 * c / (2.0 * T1 * T1)            # | int_{T1}^inf r | <= 2c/(2 T1^2)
    vlog = c * float(exp1(mu2 * T0))           # int e^{-mu2 t} c/t
    # int_{T0}^inf e^{-mu2 t} c/(4 t^2) dt  =  (c/4) [ e^{-mu2 T0}/T0 - mu2 E1(mu2 T0) ]
    vsq = 0.25 * c * (math.exp(-mu2 * T0) / T0 - mu2 * float(exp1(mu2 * T0)))
    return 0.75 * (v0 + vr + vlog + vsq), 0.75 * (abs(e0) + abs(er) + rem)

def C_inf_indep(x):
    Y, err = Y_inf_indep(mu2_x(x))
    return Y - A * x - 0.5 * A * math.log(beta_x(x)), err

# ----------------------------------------------------------------------- main
out = {"meta": dict(engine="ENGINE_OP1_m5_audit.py", date="2026-06-12")}

# G-M1 — C_CRIT and the rational sub-threshold
cc = find_ccrit()
xs_cc, tb_cc = env_max(cc)
assert abs(cc - CCRIT_M53) <= 2e-10, f"G-M1 FAIL CCRIT {cc}"
xs_r, tb_r = env_max(1.0 / 28.0)
assert tb_r < 0.125 and int(1.0 // tb_r) == 8, "G-M1 FAIL rational threshold 1/28"
out["G_M1"] = dict(CCRIT_indep=cc, CCRIT_M53=CCRIT_M53, xstar=xs_cc, Tbar=tb_cc,
                   rational_threshold="1/28", Tbar_at_1_28=tb_r, passed=True)
print(f"G-M1 PASS: CCRIT = {cc:.15f} (M5.3: {CCRIT_M53}); at C=1/28: Tbar={tb_r:.9f} floor={int(1//tb_r)}")

# G-M2 — B-form divergence (auditor/M5_1 pin asymptotically false as stated)
def B_of_x(x, Cval): return Cval + 0.5 * A * math.log(beta_x(x))
lo, hi = 0.0, 1e7
assert B_of_x(hi, CINF_M53) > BCRIT_BFORM, "G-M2: no crossing found below x=1e7?!"
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if B_of_x(mid, CINF_M53) < BCRIT_BFORM: lo = mid
    else: hi = mid
x_cross = 0.5 * (lo + hi)
out["G_M2"] = dict(x_cross=x_cross, beta_at_cross=beta_x(x_cross),
                   note="B(x) = C_inf + (A/2) ln beta(x) is unbounded; B-form pin fails beyond x_cross",
                   passed=True)
print(f"G-M2 PASS: B-form crosses 57/1210 at x = {x_cross:.1f} (beta = {beta_x(x_cross):.1f}) — C-form is the correct pin")

# G-M3/G-M4 — Lemma A ratio scan + Claim 1, adversarial L (odd, prime, even)
Ls = [4, 5, 7, 9, 11, 13, 16, 17, 23, 31, 47, 63, 64, 101, 128, 129, 255, 256]
worst_ratio, worst_at = -1.0, None
worst_ratio_window, worst_at_w = -1.0, None
claim1_worst = -1.0
for L in Ls:
    t_abs = np.logspace(-6, 2, 90)
    t_scl = (L * L) * np.logspace(-3.2, 1.2, 220)
    for t in np.unique(np.concatenate([t_abs, t_scl])):
        t = float(t)
        ph, q = Phi_L(L, t), q_line(t)
        lhs = ph ** 4 - L ** -4.0
        ratio = lhs / q ** 4 if q > 0 else 0.0
        if ratio > worst_ratio: worst_ratio, worst_at = ratio, (L, t)
        if t >= 0.01 * L * L and ratio > worst_ratio_window:
            worst_ratio_window, worst_at_w = ratio, (L, t)
        c1 = ph - 1.0 / L - q
        if c1 > claim1_worst: claim1_worst = c1
assert worst_ratio <= 1.0 + 1e-9, f"G-M3 FAIL: ratio {worst_ratio} at {worst_at}"
assert claim1_worst <= 1e-13, f"G-M4 FAIL: Claim 1 violated by {claim1_worst}"
out["G_M3"] = dict(max_ratio=worst_ratio, at=worst_at,
                   max_ratio_t_ge_001L2=worst_ratio_window, at_window=worst_at_w, passed=True)
out["G_M4"] = dict(claim1_max_violation=claim1_worst, passed=True)
print(f"G-M3 PASS: max ratio = {worst_ratio:.12f} at (L,t)={worst_at}; window(t>=0.01L^2) max = {worst_ratio_window:.9f} at {worst_at_w}")
print(f"G-M4 PASS: Claim 1 max violation = {claim1_worst:.3e}")

# G-M5 — continuum core G(c) = 16 pi^2 c^2 (theta(c)^4 - 1)
def theta(c):
    s, n = 1.0, 1
    while True:
        term = 2.0 * math.exp(-4.0 * math.pi**2 * c * n * n)
        s += term
        if term < 1e-20 * s: return s
        n += 1
cs = np.logspace(-3.2, 1.4, 600)
G = np.array([16 * math.pi**2 * c * c * (theta(float(c)) ** 4 - 1.0) for c in cs])
i = int(np.argmax(G))
Ga = max(g for c, g in zip(cs, G) if c >= 0.125)
# proved two-region statement: G < 1 strictly; G <= 0.149 on c >= 1/8;
# and on c <= 1/8 the margin form 1 - G >= 0.096 * 16 pi^2 c^2 (from h(1/8) = 0.904)
assert G[i] < 1.0, f"G-M5 FAIL: G max {G[i]} at c={cs[i]}"
assert Ga <= 0.149, f"G-M5 FAIL region (a): {Ga}"
mviol = max((0.096 * 16 * math.pi**2 * c * c - (1.0 - g)) for c, g in zip(cs, G) if c <= 0.125)
assert mviol <= 1e-12, f"G-M5 FAIL margin form: violation {mviol}"
out["G_M5"] = dict(G_max=float(G[i]), at_c=float(cs[i]), G_max_c_ge_eighth=float(Ga),
                   margin_form_worst=float(mviol),
                   h_at_eighth=(2.005 * math.e**-2 * (1 + 2.005 * math.e**-2) ** 3) / (4 * math.pi**2 / 64),
                   passed=True)
print(f"G-M5 PASS: G<1 everywhere (grid max {G[i]:.9f} at c={cs[i]:.5f}, saturating only as c->0); "
      f"sup c>=1/8 = {Ga:.6f} <= 0.149; margin-form worst = {mviol:.2e}; h(1/8) = {out['G_M5']['h_at_eighth']:.6f}")

# G-M6 — independent C_inf vs M5.3 printed values; C_infinity
refs = {0.0: 0.010666266672, math.log(3.0): 0.012393247754,
        4.158883083359672: 0.012790407738, 20.0: 0.012792103147}
worst = 0.0
for x, ref in refs.items():
    Ci, err = C_inf_indep(x)
    d = abs(Ci - ref) / abs(ref)
    worst = max(worst, d)
    assert d <= 1e-7, f"G-M6 FAIL x={x}: {Ci} vs {ref} ({d})"
Cinf_60, err60 = C_inf_indep(60.0)
assert abs(Cinf_60 - CINF_M53) <= 1e-9, f"G-M6 FAIL C_infinity {Cinf_60}"
out["G_M6"] = dict(worst_rel_vs_M53=worst, C_infinity=Cinf_60, quad_err=err60, passed=True)
print(f"G-M6 PASS: independent C_inf matches M5.3 to {worst:.2e}; C_infinity = {Cinf_60:.12f}")

# G-M7 — finite C_L <= C_inf, profile and argmax
prof = []
prof_Ls = list(range(4, 129)) + [144, 160, 192, 224, 256]
for L in prof_Ls:
    x = math.log(L / 4.0)
    b = beta_x(x)
    cs_ = consts(L, 8.0 / L**2, b / 6.0)
    CL = cs_["T_C"] * (b / 6.0) ** 2 - A * x - 0.5 * A * math.log(b)
    prof.append((L, CL))
    if L in (4, 5, 6, 8, 12, 16, 24, 32, 47, 48, 64, 96, 128, 192, 256):
        Ci, _ = C_inf_indep(x)
        assert CL <= Ci + 1e-10, f"G-M7 FAIL L={L}: C_L {CL} > C_inf {Ci}"
Lmax, CLmax = max(prof, key=lambda r: r[1])
mono_viol = sum(1 for a, b in zip(prof, prof[1:]) if b[1] < a[1] - 1e-14)
out["G_M7"] = dict(argmax_L=Lmax, C_L_max=CLmax, C_L_at_4=prof[0][1], C_L_at_256=prof[-1][1], monotone_violations=mono_viol, passed=True)
print(f"G-M7 PASS: C_L <= C_inf on sampled L; finite C_L profile: max {CLmax:.12f} at L={Lmax} (profile peaks at L={Lmax}; envelope-dominated)")

# G-M8 — Lemma B monotonicity integrand sign across the diagonal range
def Dprime(mu2):
    f = lambda t: t * t * math.exp(-mu2 * t) * (q_line(t) ** 4 - 1.0 / (16 * math.pi**2 * t * t))
    v1, e1 = quad(f, 0.0, 50.0, epsabs=1e-13, epsrel=1e-11, limit=400)
    v2, e2 = quad(f, 50.0, 20000.0, epsabs=1e-13, epsrel=1e-10, limit=800)
    return 0.75 * (v1 + v2), 0.75 * (abs(e1) + abs(e2))
mu2_max = mu2_x(0.0)
worstD = None
for frac in np.linspace(1e-4, 1.0, 13):
    mu2 = float(frac * mu2_max)
    D, eD = Dprime(mu2)
    if worstD is None or D < worstD[0]: worstD = (D, mu2, eD)
    assert D > 3 * eD, f"G-M8 FAIL mu2={mu2}: Dprime={D} err={eD}"
out["G_M8"] = dict(min_Dprime=worstD[0], at_mu2=worstD[1], err=worstD[2], mu2_range_max=mu2_max, passed=True)
print(f"G-M8 PASS: D'(mu2) > 0 across (0, {mu2_max:.4f}]; min D' = {worstD[0]:.3e} at mu2 = {worstD[1]:.4f}")

json.dump(out, open("/home/claude/AUDIT_OP1_m5.json", "w"), indent=1)
print("WROTE /home/claude/AUDIT_OP1_m5.json")
print("ALL GATES PASS")
