#!/usr/bin/env python3
# Fresh-path run copy of ENGINE_OP1_za_cap_cert.py (VM mount served a stale truncated view of
# the canonical file; host copy is correct). Byte-equivalent logic.
import json, math, os
import numpy as np
rng = np.random.default_rng(20260612)

def constrained_max_on_sphere(m, N, a, tol=1e-12):
    if N.size == 0 or N.shape[0] == 0:
        nm = float(np.linalg.norm(m))
        if nm < tol: return np.array([1.0,0,0,0]), 0.0
        u = m/nm; return u, float(u@m)
    G = N @ N.T
    try: Ginv = np.linalg.inv(G)
    except np.linalg.LinAlgError: return None, -np.inf
    k = N.shape[0]; b = a*np.ones(k); u0 = N.T @ (Ginv @ b); s = float(u0@u0)
    if s > 1.0 - tol: return None, -np.inf
    m_perp = m - N.T @ (Ginv @ (N @ m)); mp = float(np.linalg.norm(m_perp))
    if mp < tol:
        for j in range(4):
            ej = np.zeros(4); ej[j]=1.0
            ep = ej - N.T @ (Ginv @ (N @ ej)); ne = float(np.linalg.norm(ep))
            if ne > tol:
                u = u0 + math.sqrt(max(0.0,1.0-s))*(ep/ne); return u, float(u@m)
        return None, -np.inf
    u = u0 + math.sqrt(max(0.0,1.0-s))*(m_perp/mp); return u, float(u@m)

def solve_cap_max(m, n_list, a, ineq_tol=1e-9):
    n_arr = np.asarray(n_list, dtype=float).reshape(-1,4); A = len(n_arr)
    best_u=None; best=-np.inf; best_act=()
    for mask in range(1 << A):
        act = tuple(i for i in range(A) if (mask>>i)&1)
        N_act = n_arr[list(act)] if act else np.zeros((0,4))
        u,val = constrained_max_on_sphere(m, N_act, a)
        if u is None: continue
        ok = True
        for j in range(A):
            if j in act: continue
            if float(n_arr[j]@u) > a + ineq_tol: ok=False; break
        if ok and val > best: best=val; best_u=u; best_act=act
    return best_u, best, best_act

def runit(n):
    v = rng.standard_normal((n,4)); return v/np.linalg.norm(v,axis=1,keepdims=True)

viol_principal = 0.0; n_principal = 0; ratio_min_principal = np.inf
n_multi = 0; ratio_min_multi = np.inf; n_multi_viol = 0
const_checks = []; n_good = 0; n_total = 0
for trial in range(60000):
    k = int(rng.integers(0, 5)); m = runit(1)[0]; n_p = runit(1)[0]
    A = runit(k) if k>0 else np.zeros((0,4)); a = float(rng.uniform(-0.2, 0.95))
    uA, hA, act = solve_cap_max(m, A, a)
    if uA is None: continue
    chi0 = float(uA @ n_p) - a; n_total += 1
    if chi0 <= 1e-6: continue
    n_good += 1
    A_aug = np.vstack([A, n_p[None,:]]) if k>0 else n_p[None,:]
    uAp, hAp, _ = solve_cap_max(m, A_aug, a)
    if uAp is None: continue
    Delta_p = hA - hAp; ratio = Delta_p/(chi0*chi0)
    if k == 0:
        # A genuinely empty: the bare target cap. PROVED case.
        n_principal += 1; ratio_min_principal = min(ratio_min_principal, ratio)
        if Delta_p < 0.5*chi0*chi0 - 1e-7:
            viol_principal = max(viol_principal, 0.5*chi0*chi0 - Delta_p)
        c0 = float(m @ n_p); const_checks.append((chi0, Delta_p, 0.5/(1.0-c0*c0), c0))
    else:
        # incident neighbor caps present (k>=1): the chi_0-criterion may fail.
        n_multi += 1; ratio_min_multi = min(ratio_min_multi, ratio)
        if Delta_p < 0.5*chi0*chi0 - 1e-7: n_multi_viol += 1

assert viol_principal < 1e-7, f'GATE FAIL G-ZA1 (principal): {viol_principal}'
small = [(d/(x*x), p) for (x,d,p,c) in const_checks if x < 0.05]
g_za2 = max(abs(r - p)/p for (r,p) in small) if small else 0.0
assert g_za2 < 0.05, f'GATE FAIL G-ZA2: {g_za2}'
multi_violation_rate = (n_multi_viol / n_multi) if n_multi else 0.0

def nu_cap_A_empty(c0, a, kappa, Ng=1600):
    s0 = math.sqrt(1.0 - c0*c0)
    w = np.linspace(-1,1,Ng); y = np.linspace(-1,1,Ng)
    W,Y = np.meshgrid(w,y,indexing='ij'); disk = (W*W+Y*Y) < 1.0
    rad = np.zeros_like(W); rad[disk] = np.sqrt(1.0 - W[disk]**2 - Y[disk]**2)
    logw = kappa*W; logw[~disk] = -1e18; Mx = logw.max()
    wt = np.exp(logw-Mx)*rad; g = c0*W + s0*Y
    capmask = (g <= a) & disk; dA = (w[1]-w[0])*(y[1]-y[0])
    return (wt[capmask].sum()*dA)/(wt.sum()*dA)

def Delta_rate(c0,a): return 1.0 - (c0*a + math.sqrt((1-c0*c0)*(1-a*a)))

c0 = 0.80; a = 0.50; Dp = Delta_rate(c0,a)
kappas = np.array([40,60,80,120,160,220,300,420], dtype=float)
neglogs = np.array([-math.log(nu_cap_A_empty(c0,a,k)) for k in kappas])
resid = neglogs - kappas*Dp
Amat = np.vstack([-np.log(kappas), -np.ones_like(kappas)]).T
coef, *_ = np.linalg.lstsq(Amat, resid, rcond=None)
M_fit, logCgeom = coef[0], coef[1]
slope_hi = (neglogs[-1]-neglogs[-2])/(kappas[-1]-kappas[-2])
assert abs(slope_hi - Dp) < 0.02, f'GATE FAIL G-ZA3: {slope_hi} vs {Dp}'
assert 0.5 < M_fit < 2.5, f'GATE FAIL G-ZA4: {M_fit}'

out = {
 'gates': 'G-ZA1,G-ZA2,G-ZA3,G-ZA4 PASS; G-ZA5 recorded',
 'part1_curvature': {
   'claim_principal': 'Delta_p(A) >= chi_0^2/2 when no neighbor cap active at u_A (PROVED)',
   'n_good_configs': n_good, 'n_total': n_total, 'principal_n': n_principal,
   'principal_min_ratio_Delta_over_chi2': float(ratio_min_principal),
   'sharp_const_emptyA': '1/(2(1-c0^2)); G-ZA2 worst rel dev %.3e' % g_za2,
   'multi_active_n': n_multi, 'multi_active_min_ratio': float(ratio_min_multi),
   'multi_active_violation_rate': multi_violation_rate,
   'G_ZA5_finding': 'multi-active configs VIOLATE Delta_p>=chi0^2/2; Sec.9 chi_0 criterion insufficient there',
 },
 'part2_capratio': {
   'geometry': {'c0': c0, 'a': a, 'chi_0': c0-a, 'Delta_p_rate': Dp},
   'kappas': kappas.tolist(), 'neglog_nu': neglogs.tolist(),
   'high_kappa_slope': slope_hi, 'M_prefactor_power': float(M_fit),
   'logC_geom': float(logCgeom),
   'note': 'nu(C_p) ~ C_geom kappa^{-M} e^{-kappa Delta_p}; M~3/2',
 },
}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here,'CERT_OP1_za_cap.json'),'w'), indent=1)
print('G-ZA1 (PRINCIPAL Delta_p>=chi0^2/2): PASS | n=%d, min ratio %.4f (>=0.5)' % (n_principal, ratio_min_principal))
print('G-ZA2 (sharp const 1/(2(1-c0^2))): PASS  worst rel dev %.2e' % g_za2)
print('G-ZA5 (RECORDED): multi-active n=%d, min ratio %.4f, VIOLATION rate %.2f' % (n_multi, ratio_min_multi, multi_violation_rate))
print('G-ZA3 (cap-ratio rate -> Delta_p=%.5f): PASS  slope %.5f' % (Dp, slope_hi))
print('G-ZA4 (prefactor power M): PASS  M_fit=%.3f (pred 3/2), logC_geom=%.3f' % (M_fit, logCgeom))
print('ALL_GATES_PASS')
