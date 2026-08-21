#!/usr/bin/env python3
"""
ENGINE_OP1_m4_cover_domination_audit.py - gated audit of M5_3 (COVER DOMINATION CLOSURE ROUTE)
====================================================================================
Audits the uploaded notebook `M5_3_-_COVER_DOMINATION_CLOSURE_ROUTE.ipynb`
(md5 089f6061) against the F028 reference constants and adds two derived gates.

Gates (all hard asserts):
  Q1  Cover domination Phi_L(t)^4 - L^-4 <= q(t)^4 on the notebook's multiscale
      t-grids for the notebook's 16 L values (sign gate; gaps reported), plus a
      4x-denser stress grid at L in {4, 16, 128}.
  Q2  Reproduction of the notebook's 22 C_inf rows (rtol 2e-9).
  Q3  Saturation constant C_sat == notebook value, and the CROSS-NORMALIZATION
      identity C_sat + (A/2) ln 6 == D_infty(F028)  (alpha-form vs beta-form;
      the (A/2) ln 6 offset is the alpha = beta/6 unit conversion).
  Q4  C_CRIT(M5.2/M5.3) == D_crit_3par(F028) - (A/2) ln 6.
  Q5  Closure floors: envelope maximization reproduces the notebook ceiling rows
      and gives floor(1/Tbar) >= 8 for all audited safe C values.
  Q6  DERIVED (this audit): the saturation constant has the integral
      representation
        C_sat = (3/4) K(T0) - (A/2) (gamma_E + ln T0 + ln 3),
        K(T0) = int_0^T0 t q^4 dt + int_T0^inf (t q^4 - c/t) dt,  c = 1/(16 pi^2),
      independent of T0 (checked at T0 = 32, 64, 128), equal to the audited
      saturation value.  This upgrades D_infty from "measured machine constant"
      (F028) to "renormalized lattice integral, machine-evaluated".
  Q7  Monotonicity: g(mu2) := Y_inf(mu2) - (A/2) ln(3/mu2) has g'(mu2) < 0 on a
      grid covering (0, mu2(x=0)] - numerically supports sup_x C_inf = C_sat.

Derivation notes for Q6/Q7 (recorded in F030):
  C_inf(x) = Y_inf(mu2) - A x - (A/2) ln beta == g(mu2) with mu2 = 48/(beta L^2),
  since A x + (A/2) ln beta = (A/2)(ln(1/mu2) + ln 3) exactly on L = 4 e^x.
  g'(mu2) = (A/2)/mu2 - (3/4) int_0^inf t^2 e^{-mu2 t} q(t)^4 dt.

Status of gate grounds: identity steps are classical (Poisson/E1 expansion);
all numerical values are float-grade (scipy quad + ive), not interval-certified.
Output: AUDIT_OP1_m4_cover_domination.json.  Dependencies: numpy, scipy.
"""
import json, math, os, sys, time
import numpy as np
from scipy.special import ive, exp1
from scipy.integrate import quad

BETA0 = 5.6
GAMMA = 11.0 / (8.0 * math.pi**2)
A = 3.0 / (32.0 * math.pi**2)
C_CRIT_M53 = 0.036241888089666857          # carried by M5.3 "from M5.2"
C_SAT_REF = 0.012792103146542376            # notebook max audited C_inf
LN6_HALF_A = 0.5 * A * math.log(6.0)
EULER_GAMMA = 0.5772156649015328606

def load_f028_refs():
    cands = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "AUDIT_OP1_m4_ceiling_pin.json"),
             "/sessions/beautiful-charming-knuth/mnt/THEORY/numerics/op12_theta/m4_scaling/AUDIT_OP1_m4_ceiling_pin.json",
             "/tmp/AUDIT_OP1_m4_ceiling_pin.json"]
    for c in cands:
        if os.path.exists(c):
            d = json.load(open(c))
            return d["D_infty"], d["D_crit_3par"], c
    raise RuntimeError("AUDIT_OP1_m4_ceiling_pin.json not found (F028 refs required)")

def q_infinite(t):
    return float(ive(0, 2.0 * t))

def Phi_L(L, t, rel_cut=1e-16):
    out = float(ive(0, 2.0 * t)); j = 1
    while True:
        term = 2.0 * float(ive(j * L, 2.0 * t))
        out_new = out + term
        if term <= rel_cut * max(abs(out_new), 1e-300):
            return out_new
        out = out_new; j += 1
        if j > 300000:
            raise RuntimeError(f"Phi_L runaway L={L} t={t}")

def beta_x(x): return BETA0 + GAMMA * x
def mu2_x(x):
    L = 4.0 * math.exp(x)
    return 48.0 / (beta_x(x) * L * L)

def Y_inf(mu2, T0=64.0):
    c = 1.0 / (16.0 * math.pi**2)
    f0 = lambda t: t * math.exp(-mu2 * t) * q_infinite(t)**4
    v0, e0 = quad(f0, 0.0, T0, epsabs=2e-13, epsrel=2e-12, limit=400)
    fres = lambda t: math.exp(-mu2 * t) * (t2q4(t) - c) / t
    vres, eres = quad(fres, T0, math.inf, epsabs=2e-13, epsrel=2e-11, limit=500)
    vlog = c * float(exp1(mu2 * T0))
    return 0.75 * (v0 + vres + vlog), 0.75 * (abs(e0) + abs(eres))

def C_inf_from_x(x):
    Y, err = Y_inf(mu2_x(x))
    return Y - A * x - 0.5 * A * math.log(beta_x(x)), err

def audit_cover(L, dens=1):
    abs_grid = np.logspace(-8, 4, 260 * dens)
    scaled_grid = (L * L) * np.logspace(-8, 2.5, 360 * dens)
    t_grid = np.unique(np.concatenate([abs_grid, scaled_grid]))
    worst_gap, worst_t = -1e300, None
    for t in t_grid:
        lhs = Phi_L(L, float(t))**4 - L**-4
        rhs = q_infinite(float(t))**4
        gap = lhs - rhs
        if gap > worst_gap: worst_gap, worst_t = gap, float(t)
    return worst_gap, worst_t

def C_sat_analytic(T0):
    c = 1.0 / (16.0 * math.pi**2)
    k1, e1_ = quad(lambda t: t * q_infinite(t)**4, 0.0, T0,
                   epsabs=1e-14, epsrel=1e-13, limit=500)
    k2, e2_ = quad(lambda t: (t2q4(t) - c) / t, T0, math.inf,
                   epsabs=1e-14, epsrel=1e-12, limit=600)
    val = 0.75 * (k1 + k2) - 0.5 * A * (EULER_GAMMA + math.log(T0) + math.log(3.0))
    return val, 0.75 * (abs(e1_) + abs(e2_))

def t2q4(t):
    if t > 1e8:    # asymptotic branch: q = (4 pi t)^-1/2 (1 + 1/(16t) + ...);
        # t^2 q^4 = c (1 + 1/(4t) + O(1/t^2)), switch error ~ 1e-17 relative
        # at the threshold. Guards scipy ive(0, z), which returns nan for
        # z in (2e8, 2e10] and at QUADPACK's huge infinite-interval probes.
        return (1.0 + 0.25 / t) / (16.0 * math.pi**2)
    s = t * q_infinite(t)**2
    return s * s

def g_prime(mu2, T0=8.0):
    c = 1.0 / (16.0 * math.pi**2)
    i0, _ = quad(lambda t: t2q4(t) * math.exp(-mu2 * t), 0.0, T0,
                 epsabs=1e-14, epsrel=1e-12, limit=500)
    ires, _ = quad(lambda t: math.exp(-mu2 * t) * (t2q4(t) - c - c / (4.0 * t)),
                   T0, math.inf, epsabs=1e-13, epsrel=1e-11, limit=600)
    closed = c * math.exp(-mu2 * T0) / mu2 + 0.25 * c * float(exp1(mu2 * T0))
    integral = i0 + ires + closed
    return 0.5 * A / mu2 - 0.75 * integral

COVER_LS = [4, 5, 6, 8, 12, 16, 24, 32, 47, 64, 96, 128, 192, 256, 384, 512]
XS = sorted(set([0.0, math.log(5/4), math.log(6/4), math.log(8/4), math.log(12/4),
                 math.log(16/4), math.log(32/4), math.log(47/4), math.log(64/4),
                 math.log(128/4), math.log(256/4), math.log(512/4), math.log(1024/4),
                 math.log(2048/4), math.log(4096/4), 10.0, 20.0, 30.774163829,
                 36.271356, 50.0, 75.0, 100.0]))
C_INF_REF = [0.010666266672, 0.011226842349, 0.011593044092, 0.012022190191,
             0.012393247754, 0.012546085706, 0.012718115650, 0.012754714524,
             0.012770626632, 0.012786016015, 0.012790407738, 0.012791637249,
             0.012791976482, 0.012792069010, 0.012792094013, 0.012792103131,
             0.012792103147, 0.012792103147, 0.012792103147, 0.012792103147,
             0.012792103147, 0.012792103147]

def TC_env(x, C): b = beta_x(x); return 36.0 * (A * x + 0.5 * A * math.log(b) + C) / (b * b)

def maximize_envelope(C, xmax=200.0):
    lo, hi = 0.0, xmax
    for _ in range(240):
        m1 = lo + (hi - lo) / 3.0; m2 = hi - (hi - lo) / 3.0
        if TC_env(m1, C) < TC_env(m2, C): lo = m1
        else: hi = m2
    xs = 0.5 * (lo + hi)
    return xs, TC_env(xs, C)

CEIL_REF = [(0.012792103147, 35.645172, 0.116919161069, 8),
            (0.013,          35.601969, 0.116986238982, 8),
            (0.015,          35.186363, 0.117635466507, 8),
            (0.020,          34.147483, 0.119290290186, 8),
            (0.025,          33.108794, 0.120992013961, 8),
            (0.030,          32.070305, 0.122742650916, 8)]

if __name__ == "__main__":
    t_start = time.time()
    D_INFTY, D_CRIT_3PAR, refpath = load_f028_refs()
    out = {"meta": {"engine": "ENGINE_OP1_m4_cover_domination_audit.py", "date": "2026-06-12",
                    "audits": "M5_3 COVER_DOMINATION_CLOSURE_ROUTE.ipynb (md5 089f6061)",
                    "f028_refs": refpath, "gates": "Q1..Q7 hard asserts"}}

    q1 = []
    for L in COVER_LS:
        gap, wt = audit_cover(L)
        assert gap <= 1e-13, f"Q1 FAIL L={L}: worst gap {gap} > 0"
        q1.append({"L": L, "worst_gap": gap, "worst_t": wt})
    q1s = []
    for L in [4, 16, 128]:
        gap, wt = audit_cover(L, dens=4)
        assert gap <= 1e-13, f"Q1-stress FAIL L={L}: {gap}"
        q1s.append({"L": L, "worst_gap": gap, "worst_t": wt})
    out["Q1_cover"] = {"grid": q1, "stress_4x": q1s}
    print(f"Q1 PASS  cover domination holds, 16 L values + 4x stress at L=4/16/128 "
          f"(worst gap {max(r['worst_gap'] for r in q1):.3e})")

    q2 = []
    worst = 0.0
    for x, ref in zip(XS, C_INF_REF):
        C, err = C_inf_from_x(x)
        rel = abs(C - ref) / abs(ref)
        worst = max(worst, rel)
        assert rel <= 2e-9, f"Q2 FAIL x={x}: C_inf {C} vs ref {ref} (rel {rel:.2e})"
        q2.append({"x": x, "C_inf": C, "ref": ref, "rel": rel, "quad_err": err})
    out["Q2_cinf_rows"] = q2
    print(f"Q2 PASS  22 C_inf rows reproduce (worst rel {worst:.2e})")

    C_sat = max(r["C_inf"] for r in q2)
    d3 = abs(C_sat - C_SAT_REF)
    assert d3 <= 1e-11, f"Q3 FAIL sat vs notebook: {C_sat} vs {C_SAT_REF}"
    cross = C_sat + LN6_HALF_A
    d3b = abs(cross - D_INFTY)
    assert d3b <= 2e-9, f"Q3 FAIL cross-normalization: {cross} vs D_infty {D_INFTY}"
    out["Q3_saturation"] = {"C_sat": C_sat, "C_sat_ref": C_SAT_REF,
                            "C_sat_plus_halfAln6": cross, "D_infty_F028": D_INFTY,
                            "abs_diff": d3b, "halfA_ln6": LN6_HALF_A}
    print(f"Q3 PASS  C_sat = {C_sat:.15f}; C_sat + (A/2)ln6 - D_infty(F028) = {cross - D_INFTY:+.3e}")

    pred = D_CRIT_3PAR - LN6_HALF_A
    d4 = abs(C_CRIT_M53 - pred)
    assert d4 <= 2e-9, f"Q4 FAIL C_CRIT: {C_CRIT_M53} vs {pred}"
    out["Q4_ccrit"] = {"C_CRIT_M53": C_CRIT_M53, "D_crit_3par_F028": D_CRIT_3PAR,
                       "predicted": pred, "abs_diff": d4}
    print(f"Q4 PASS  C_CRIT(M5.3) - [D_crit - (A/2)ln6] = {C_CRIT_M53 - pred:+.3e}")

    q5 = []
    for Cs, xref, tref, fref in CEIL_REF:
        xs, tb = maximize_envelope(Cs)
        fl = int(1.0 // tb)
        assert abs(tb - tref) <= 1e-9, f"Q5 FAIL Tbar at C={Cs}: {tb} vs {tref}"
        assert fl >= 8 and fl == fref, f"Q5 FAIL floor at C={Cs}: {fl}"
        q5.append({"C": Cs, "x_star": xs, "Tbar": tb, "floor": fl})
    xs_b, tb_b = maximize_envelope(C_CRIT_M53)
    out["Q5_ceiling"] = {"rows": q5, "boundary_at_CCRIT":
                         {"x_star": xs_b, "Tbar": tb_b, "floor_float": int(1.0 // tb_b),
                          "note": "boundary row; float artifact species of F028"}}
    print(f"Q5 PASS  floors >= 8 on all safe rows; boundary Tbar = {tb_b:.12f}")

    vals = {}
    for T0 in (32.0, 64.0, 128.0):
        v, e = C_sat_analytic(T0)
        vals[T0] = v
    spread = max(vals.values()) - min(vals.values())
    assert spread <= 1e-10, f"Q6 FAIL T0-invariance spread {spread}"
    v64 = vals[64.0]
    C50, _ = C_inf_from_x(50.0)
    d6 = abs(v64 - C50)
    assert d6 <= 2e-9, f"Q6 FAIL analytic vs audited saturation: {v64} vs {C50}"
    alpha_form = v64 + LN6_HALF_A
    d6b = abs(alpha_form - D_INFTY)
    assert d6b <= 2e-9, f"Q6 FAIL alpha-form vs F028 D_infty: {alpha_form} vs {D_INFTY}"
    out["Q6_integral_representation"] = {
        "formula": "C_sat = (3/4)[int_0^T0 t q^4 + int_T0^inf (t q^4 - c/t)] - (A/2)(gamma_E + ln T0 + ln 3)",
        "values_by_T0": {str(k): v for k, v in vals.items()}, "spread": spread,
        "vs_audited_sat": d6, "alpha_form_D_infty": alpha_form,
        "vs_F028_D_infty": d6b}
    print(f"Q6 PASS  integral rep: C_sat = {v64:.15f} (T0-spread {spread:.2e}); "
          f"alpha-form = {alpha_form:.15f} vs F028 D_infty (diff {alpha_form - D_INFTY:+.3e})")

    q7 = []
    for mu2 in [48.0 / (5.6 * 16.0), 0.3, 0.1, 0.03, 0.01, 1e-3, 1e-4, 1e-6]:
        gp = g_prime(mu2)
        assert gp < 0.0, f"Q7 FAIL g'({mu2}) = {gp} not negative"
        q7.append({"mu2": mu2, "g_prime": gp})
    out["Q7_monotonicity"] = q7
    print("Q7 PASS  g'(mu2) < 0 on grid: " +
          " ".join(f"{r['g_prime']:.2e}" for r in q7))

    out["meta"]["elapsed_s"] = time.time() - t_start
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(out, open(os.path.join(here, "AUDIT_OP1_m4_cover_domination.json"), "w"), indent=1)
    print(f"WROTE AUDIT_OP1_m4_cover_domination.json  ({out['meta']['elapsed_s']:.1f}s)")
    print("ALL GATES PASS (Q1-Q7)")
