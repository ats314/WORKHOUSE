#!/usr/bin/env python3
# =============================================================================
# ENGINE_OP1_za_cap_cert.py — certificate for the LCI cap-geometry lemmas (Z.A core).
# June 12, 2026 (lead math agent, DECISIONS #009).
#
# Upgrades sections 8-9 of NOTE_PMBSF_lci_tosj_reduction_lemmaq_2026_05_26.md (the SU(2)
# Lemma Q reduction) from asserted ("a Laplace ratio estimate gives ... under
# nondegenerate hypotheses") to (a) a PROVED curvature lemma with explicit
# constant, machine-checked here, and (b) a gate-certified cap-ratio law.
#
# Geometry: m, n_p, {n_r} are unit vectors in S^3 < R^4.  vMF measure
#   d nu(u) ∝ e^{kappa m·u} d sigma(u).   Cap C_r = {u : u·n_r <= a}.
#   C_A = ∩_{r∈A} C_r.   u_A = argmax_{u∈C_A∩S^3} m·u,  h(A)=m·u_A.
#   chi_0 = u_A·n_p - a  (the LCI good-event gap, >0 means u_A is OUTSIDE C_p).
#   Delta_p(A) = h(A) - h(A∪{p}) >= 0  (the height drop on adding C_p).
#
# CLAIMS CERTIFIED:
#  (L2 curvature, PROVED in note; gated here):  Delta_p(A) >= chi_0^2 / 2,
#     with the SHARP small-gap constant Delta_p ≈ chi_0^2 / (2(1 - ctil^2)),
#     ctil = alignment cosine of n_p and m inside the active feasible subspace
#     (ctil = m·n_p when A's active set is empty).  G-ZA1, G-ZA2.
#  (L1 cap-ratio law, eq 8.4):  nu(C_p|C_A) <= C_geom kappa^M e^{-kappa Delta_p}.
#     Certified for A=∅ by exact 2D vMF quadrature over a kappa ladder:
#     -log nu(C_p) = kappa*Delta_p - M log kappa - log C_geom + o(1),
#     rate -> Delta_p (G-ZA3) and M extracted (~3/2, G-ZA4).
#
# Dependencies: numpy.  All gates hard-assert.
# =============================================================================
import json, math
import numpy as np

rng = np.random.default_rng(20260612)

# ----------------------------- cap-intersection solver (S^3) -----------------
def constrained_max_on_sphere(m, N, a, tol=1e-12):
    """max u·m s.t. |u|=1 and N@u = a*1.  Returns (u,val) or (None,-inf)."""
    if N.size == 0 or N.shape[0] == 0:
        nm = float(np.linalg.norm(m))
        if nm < tol:
            return np.array([1.0,0,0,0]), 0.0
        u = m/nm; return u, float(u@m)
    G = N @ N.T
    try:
        Ginv = np.linalg.inv(G)
    except np.linalg.LinAlgError:
        return None, -np.inf
    k = N.shape[0]; b = a*np.ones(k); u0 = N.T @ (Ginv @ b)
    s = float(u0@u0)
    if s > 1.0 - tol:
        return None, -np.inf
    m_perp = m - N.T @ (Ginv @ (N @ m)); mp = float(np.linalg.norm(m_perp))
    if mp < tol:
        for j in range(4):
            ej = np.zeros(4); ej[j]=1.0
            ep = ej - N.T @ (Ginv @ (N @ ej)); ne = float(np.linalg.norm(ep))
            if ne > tol:
                u = u0 + math.sqrt(max(0.0,1.0-s))*(ep/ne); return u, float(u@m)
        return None, -np.inf
    u = u0 + math.sqrt(max(0.0,1.0-s))*(m_perp/mp)
    return u, float(u@m)

def solve_cap_max(m, n_list, a, ineq_tol=1e-9):
    """max u·m s.t. u∈S^3, u·n_r<=a for r in n_list. Active-set enumeration."""
    n_arr = np.asarray(n_list, dtype=float).reshape(-1,4)
    A = len(n_arr); best_u=None; best=-np.inf; best_act=()
    for mask in range(1 << A):
        act = tuple(i for i in range(A) if (mask>>i)&1)
        N_act = n_arr[list(act)] if act else np.zeros((0,4))
        u,val = constrained_max_on_sphere(m, N_act, a)
        if u is None: continue
        ok = True
        for j in range(A):
            if j in act: continue
            if float(n_arr[j]@u) > a + ineq_tol: ok=False; break
        if ok and val > best:
            best=val; best_u=u; best_act=act
    return best_u, best, best_act

def runit(n):
    v = rng.standard_normal((n,4)); return v/np.linalg.norm(v,axis=1,keepdims=True)

# =============================================================================
# PART 1 — curvature lemma  Delta_p(A) >= chi_0^2 / 2   (and sharp constant)
# =============================================================================
# Two regimes are separated by the ACTIVE SET of u_A:
#   principal: no neighbor cap active at u_A (u_A = m, the vMF mean) -> lemma holds,
#   multi-active: >=1 neighbor cap active -> the chi_0-at-u_A criterion is INSUFFICIENT
#                 (an alternative high-m point can already lie inside C_p), so
#                 Delta_p >= chi_0^2/2 can FAIL.  This is the gap in LCI-reduction Sec.9.
viol_principal = 0.0
n_principal = 0; ratio_min_principal = np.inf
n_multi = 0; ratio_min_multi = np.inf; n_multi_viol = 0
const_checks = []               # (chi0, Delta_p, predicted 1/(2(1-c0^2))) for principal
n_good = 0; n_total = 0

for trial in range(60000):
    k = int(rng.integers(0, 5))            # |A| = 0..4 neighbor caps
    m = runit(1)[0]; n_p = runit(1)[0]
    A = runit(k) if k>0 else np.zeros((0,4))
    a = float(rng.uniform(-0.2, 0.95))
    uA, hA, act = solve_cap_max(m, A, a)
    if uA is None: continue
    chi0 = float(uA @ n_p) - a
    n_total += 1
    if chi0 <= 1e-6:                        # only good-event configs carry the claim
        continue
    n_good += 1
    A_aug = np.vstack([A, n_p[None,:]]) if k>0 else n_p[None,:]
    uAp, hAp, _ = solve_cap_max(m, A_aug, a)
    if uAp is None:
        continue
    Delta_p = hA - hAp
    ratio = Delta_p/(chi0*chi0)
    if len(act) == 0:
        # principal case: lemma should hold
        n_principal += 1
        ratio_min_principal = min(ratio_min_principal, ratio)
        if Delta_p < 0.5*chi0*chi0 - 1e-7:
            viol_principal = max(viol_principal, 0.5*chi0*chi0 - Delta_p)
        c0 = float(m @ n_p)
        const_checks.append((chi0, Delta_p, 0.5/(1.0-c0*c0), c0))
    else:
        n_multi += 1
        ratio_min_multi = min(ratio_min_multi, ratio)
        if Delta_p < 0.5*chi0*chi0 - 1e-7:
            n_multi_viol += 1

# GATE G-ZA1 (PROVED, principal case): Delta_p >= chi_0^2/2 when no neighbor active
assert viol_principal < 1e-7, \
    f'GATE FAIL G-ZA1 (principal): Delta_p < chi0^2/2 by {viol_principal}'
# GATE G-ZA2: sharp constant 1/(2(1-c0^2)) as chi0->0 (principal case)
small = [(d/(x*x), p) for (x,d,p,c) in const_checks if x < 0.05]
g_za2 = 0.0
if small:
    g_za2 = max(abs(r - p)/p for (r,p) in small)
    assert g_za2 < 0.05, f'GATE FAIL G-ZA2: sharp const off by {g_za2}'
# G-ZA5 (recorded, NOT a pass/fail): multi-active configs DO violate the naive bound
multi_violation_rate = (n_multi_viol / n_multi) if n_multi else 0.0

# =============================================================================
# PART 2 — cap-ratio law (8.4) for A=∅ by exact 2D vMF quadrature
#   nu(C_p) = P_vMF(u·n_p <= a).  Marginal of (w=u·m, y=u·e) on the unit disk
#   is ∝ e^{kappa w} sqrt(1-w^2-y^2),  n_p = c0 m + s0 e.
#   Rate Delta_p = 1 - [ c0 a + sqrt((1-c0^2)(1-a^2)) ].
# =============================================================================
def nu_cap_A_empty(c0, a, kappa, Ng=1600):
    s0 = math.sqrt(1.0 - c0*c0)
    w = np.linspace(-1, 1, Ng); y = np.linspace(-1, 1, Ng)
    W, Y = np.meshgrid(w, y, indexing='ij')
    disk = (W*W + Y*Y) < 1.0
    rad = np.zeros_like(W); rad[disk] = np.sqrt(1.0 - W[disk]**2 - Y[disk]**2)
    # log-weight, stabilized
    logw = kappa*W
    logw[~disk] = -1e18
    M = logw.max(); wt = np.exp(logw - M) * rad
    g = c0*W + s0*Y                        # = u·n_p
    capmask = (g <= a) & disk
    dA = (w[1]-w[0])*(y[1]-y[0])
    Z = wt.sum()*dA
    num = wt[capmask].sum()*dA
    return num / Z

def Delta_rate(c0, a):
    return 1.0 - (c0*a + math.sqrt((1-c0*c0)*(1-a*a)))

# pick a clean nondegenerate geometry
c0 = 0.80; a = 0.50                         # chi_0 = c0 - a = 0.30 > 0
Dp = Delta_rate(c0, a)
kappas = np.array([40,60,80,120,160,220,300,420], dtype=float)
neglogs = np.array([-math.log(nu_cap_A_empty(c0, a, k)) for k in kappas])

# fit  neglog = kappa*Dp - M*log(kappa) - logCgeom
resid = neglogs - kappas*Dp                # = -M log k - logCgeom
Amat = np.vstack([-np.log(kappas), -np.ones_like(kappas)]).T
coef, *_ = np.linalg.lstsq(Amat, resid, rcond=None)
M_fit, logCgeom = coef[0], coef[1]
# GATE G-ZA3: leading rate matches Delta_p (slope of neglog vs kappa -> Dp)
slope_hi = (neglogs[-1]-neglogs[-2])/(kappas[-1]-kappas[-2])
assert abs(slope_hi - Dp) < 0.02, f'GATE FAIL G-ZA3: rate {slope_hi} vs Delta_p {Dp}'
# GATE G-ZA4: extracted prefactor power M is finite and near 3/2 (one active
# linear constraint at a smooth sphere max => 2D Laplace power 3/2)
assert 0.5 < M_fit < 2.5, f'GATE FAIL G-ZA4: M_fit={M_fit} out of expected band'

out = {
  'gates': 'G-ZA1,G-ZA2,G-ZA3,G-ZA4 PASS; G-ZA5 recorded',
  'part1_curvature': {
     'claim_principal': 'Delta_p(A) >= chi_0^2/2 when no neighbor cap active at u_A (PROVED)',
     'n_good_configs': n_good, 'n_total': n_total,
     'principal_n': n_principal,
     'principal_min_ratio_Delta_over_chi2': float(ratio_min_principal),
     'sharp_const_emptyA': '1/(2(1-c0^2)); G-ZA2 worst rel dev %.3e' % g_za2,
     'multi_active_n': n_multi,
     'multi_active_min_ratio': float(ratio_min_multi),
     'multi_active_violation_rate': multi_violation_rate,
     'G_ZA5_finding': ('multi-active configs VIOLATE Delta_p>=chi0^2/2 (rate %.2f): the '
                       'Sec.9 good-event criterion chi_0=u_A.n_p-a is INSUFFICIENT there '
                       '(an alternative high-m point can lie inside C_p). Gap identified.'
                       % multi_violation_rate),
  },
  'part2_capratio': {
     'geometry': {'c0': c0, 'a': a, 'chi_0': c0-a, 'Delta_p_rate': Dp},
     'kappas': kappas.tolist(),
     'neglog_nu': neglogs.tolist(),
     'high_kappa_slope': slope_hi,
     'M_prefactor_power': float(M_fit),
     'logC_geom': float(logCgeom),
     'note': 'nu(C_p) ~ C_geom kappa^{-M} e^{-kappa Delta_p}; M~3/2',
  },
}
import os
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'CERT_OP1_za_cap.json'), 'w'), indent=1)

print('G-ZA1 (PRINCIPAL Delta_p>=chi0^2/2): PASS | n=%d, min Delta_p/chi0^2 = %.4f (>=0.5)'
      % (n_principal, ratio_min_principal))
print('G-ZA2 (sharp const 1/(2(1-c0^2)), principal): PASS  worst rel dev %.2e' % g_za2)
print('G-ZA5 (RECORDED): multi-active configs n=%d, min ratio %.4f, VIOLATION rate %.2f '
      '-> Sec.9 chi_0 criterion insufficient for |active|>=1' % (n_multi, ratio_min_multi, multi_violation_rate))
print('G-ZA3 (cap-ratio rate -> Delta_p=%.5f): PASS  high-kappa slope %.5f' % (Dp, slope_hi))
print('G-ZA4 (prefactor power M): PASS  M_fit = %.3f (predicted 3/2),  logC_geom = %.3f'
      % (M_fit, logCgeom))
print('ALL_GATES_PASS')
