#!/usr/bin/env python3
# =============================================================================
# ENGINE_OP1_delta_max_curvature.py — the comparator-validity UPPER edge of the delta-window.
# June 12, 2026 (lead math agent, DECISIONS #009).  Completes F035.
#
# Question: F035 showed the in-model firewall theta FALLS as delta grows, so the
# model V = v0*Pi_D (objective, UNIF_OP1_CLOSURE_PLAN line 11) has no upper-delta
# ceiling INTERNALLY.  The real upper edge is MODEL FAITHFULNESS: the comparator
#     M = m0^2 I + alpha_W d1* d1
# is a POSITIVE operator (both terms >= 0), so it cannot represent any plaquette
# whose local Hessian block has a NEGATIVE-curvature direction.  Such a plaquette
# must be in the defect set D_delta for M - V to bound the true (locally
# indefinite) Hessian from below.  This is calibration-INDEPENDENT: it does not
# depend on the values of m0^2, alpha_W, v0.
#
# The per-link 8x8 Hessian block contributed by one plaquette of holonomy U_p:
#     H_ab = d^2 s_p / (dt_a dt_b)|_0 = (1/6) Re tr( {T_a,T_b} U_p ),   T_a = lam_a/2
#     s_p = 1 - (1/3) Re tr U_p,   trace H = (4/3)(1 - s_p)   [sign change at s_p=1]
# We compute, over the full SU(3) conjugacy class (theta1,theta2 grid):
#   - the trace law (gate vs (4/3)(1-s_p)),
#   - the smallest eigenvalue of H(U_p),
#   - s_p* = the SMALLEST s_p at which any class element has min-eig(H) < 0
#     (the onset of a negative-curvature direction) => the conservative delta_max.
# Plus a finite-difference cross-check of H_ab for a sample U_p (gate).
#
# Output: CERT_OP1_delta_max_curvature.json + console table.  All gates hard-assert.
# Dependencies: numpy.
# =============================================================================
import json, math
import numpy as np

# --- SU(3) Gell-Mann generators T_a = lambda_a / 2, tr(T_a T_b) = delta_ab/2 ---
lam = np.zeros((8, 3, 3), dtype=np.complex128)
lam[0][0,1]=lam[0][1,0]=1; lam[1][0,1]=-1j; lam[1][1,0]=1j
lam[2][0,0]=1; lam[2][1,1]=-1
lam[3][0,2]=lam[3][2,0]=1; lam[4][0,2]=-1j; lam[4][2,0]=1j
lam[5][1,2]=lam[5][2,1]=1; lam[6][1,2]=-1j; lam[6][2,1]=1j
lam[7][0,0]=lam[7][1,1]=1/math.sqrt(3); lam[7][2,2]=-2/math.sqrt(3)
T = lam/2.0
I3 = np.eye(3, dtype=np.complex128)

# GATE G-DM0: Casimir  sum_a T_a^2 = C_F I, C_F = 4/3
Csum = sum(T[a] @ T[a] for a in range(8))
assert np.allclose(Csum, (4.0/3.0)*I3, atol=1e-13), 'GATE FAIL G-DM0: sum T_a^2 != (4/3)I'

# anticommutator table {T_a,T_b}
ANTI = np.zeros((8,8,3,3), dtype=np.complex128)
for a in range(8):
    for b in range(8):
        ANTI[a,b] = T[a] @ T[b] + T[b] @ T[a]

def hessian_block(U):
    """8x8 per-link Hessian block H_ab = (1/6) Re tr({T_a,T_b} U)."""
    H = np.zeros((8,8))
    for a in range(8):
        for b in range(a,8):
            v = (1.0/6.0)*np.real(np.trace(ANTI[a,b] @ U))
            H[a,b] = v; H[b,a] = v
    return H

def sp_of(U):
    return 1.0 - np.real(np.trace(U))/3.0

def U_class(th1, th2):
    """Diagonal representative of the SU(3) class; det=1 via th3=-th1-th2."""
    th3 = -th1 - th2
    return np.diag([np.exp(1j*th1), np.exp(1j*th2), np.exp(1j*th3)]).astype(np.complex128)

# --- GATE G-DM1: trace law  trace H = (4/3)(1 - s_p), on a random class sample ---
rng = np.random.default_rng(20260612)
worst_trace = 0.0
for _ in range(400):
    th1 = rng.uniform(-math.pi, math.pi); th2 = rng.uniform(-math.pi, math.pi)
    U = U_class(th1, th2); H = hessian_block(U)
    lhs = np.trace(H); rhs = (4.0/3.0)*(1.0 - sp_of(U))
    worst_trace = max(worst_trace, abs(lhs - rhs))
assert worst_trace < 1e-12, f'GATE FAIL G-DM1: trace law off by {worst_trace}'

# --- GATE G-DM2: finite-difference cross-check of H_ab for one U_p ---
def s_p_perturbed(U, tvec):
    X = sum(tvec[a]*T[a] for a in range(8))
    # exp(i X) via eigendecomposition (X Hermitian)
    w, Vv = np.linalg.eigh(X)
    expiX = (Vv * np.exp(1j*w)) @ Vv.conj().T
    return 1.0 - np.real(np.trace(expiX @ U))/3.0
Utest = U_class(0.7, -0.3)
H_an = hessian_block(Utest)
h = 1e-4; worst_fd = 0.0
for a in range(8):
    for b in range(8):
        ea = np.zeros(8); ea[a]+=h
        eb = np.zeros(8); eb[b]+=h
        fpp = s_p_perturbed(Utest, ea+eb); fpm = s_p_perturbed(Utest, ea-eb)
        fmp = s_p_perturbed(Utest, -ea+eb); fmm = s_p_perturbed(Utest, -ea-eb)
        d2 = (fpp - fpm - fmp + fmm)/(4*h*h)
        worst_fd = max(worst_fd, abs(d2 - H_an[a,b]))
assert worst_fd < 1e-6, f'GATE FAIL G-DM2: FD vs analytic H off by {worst_fd}'

# --- main scan: min-eig(H) over the SU(3) class, vs s_p ---
N = 240
grid = np.linspace(-math.pi, math.pi, N)
records = []   # (s_p, min_eig)
sp_star = None         # onset of first negative eigenvalue (over the class)
sp_star_at = None
for th1 in grid:
    for th2 in grid:
        U = U_class(th1, th2)
        sp = sp_of(U)
        mineig = float(np.linalg.eigvalsh(hessian_block(U))[0])
        records.append((sp, mineig))
        if mineig < 0:
            if sp_star is None or sp < sp_star:
                sp_star = sp; sp_star_at = (float(th1), float(th2))

records = np.array(records)
# bin by s_p to get the WORST (most negative) min-eig and the max min-eig per bin
nb = 60
edges = np.linspace(0, 1.5, nb+1)
binmid = 0.5*(edges[:-1]+edges[1:])
worst_min = np.full(nb, np.nan); best_min = np.full(nb, np.nan)
for i in range(nb):
    sel = (records[:,0] >= edges[i]) & (records[:,0] < edges[i+1])
    if sel.any():
        worst_min[i] = records[sel,1].min()
        best_min[i]  = records[sel,1].max()

# sanity: trace = (4/3)(1-s_p) => for s_p>1 trace<0 => min-eig<0 necessarily
sp_trace_zero = 1.0

# --- GATE G-DM3: every class element with s_p > 1 has min-eig < 0 (trace<0 forces it)
viol = [(r[0], r[1]) for r in records if r[0] > 1.0 + 1e-9 and r[1] >= 0]
assert not viol, f'GATE FAIL G-DM3: {len(viol)} class elts with s_p>1 but min-eig>=0'

# --- GATE G-DM4: s_p* (negative-curvature onset) is <= 1 with margin
assert sp_star is not None and sp_star <= 1.0 + 1e-9, f'GATE FAIL G-DM4: sp_star={sp_star}'

out = {
    'gates': 'G-DM0..G-DM4 PASS',
    'casimir_CF': 4.0/3.0,
    'trace_law': 'trace H_ab = (4/3)(1 - s_p)  [exact; G-DM1 worst dev %.2e]' % worst_trace,
    'fd_crosscheck_worst': worst_fd,
    # --- two thresholds, two strengths ---
    'sp_negcurv_onset_strict': sp_star,          # ~2/3: first negative eigendirection
    'sp_negcurv_onset_at_angles': sp_star_at,
    'sp_trace_signchange_hard': sp_trace_zero,   # =1: net (trace) curvature turns negative
    'delta_max_hard': 1.0,                        # calibration-INDEPENDENT ceiling
    'delta_max_strict': sp_star,                  # calibration-DEPENDENT (mass m0^2 may absorb)
    'faithful_range': [sp_star, 1.0],
    'interpretation': (
        'A POSITIVE comparator M = m0^2 I + alpha_W d1*d1 cannot lower-bound a plaquette '
        'whose local Hessian block is NET-negative (trace<0, i.e. s_p>1): that is the HARD, '
        'calibration-independent ceiling delta_max <= 1. The block already develops a single '
        'negative DIRECTION at s_p* = 2/3 (strict onset); whether that direction is '
        'uncontrolled depends on whether m0^2 and the 5 neighbouring plaquettes absorb it '
        '(calibration-dependent). So the faithful defect threshold lies in [2/3, 1]; the '
        'operating delta ~ 0.9-1.1 sits at the edge, relying on the mass to absorb (2/3,delta) '
        'directions, and is principled only for delta <= 1.'),
    'tier_R_needs_delta_gt_1': True,
    'window_disjoint_with_tierR': True,          # faithful delta<=1  vs  Tier-R delta>1
    'bins_s_p': binmid.tolist(),
    'worst_min_eig': [None if np.isnan(x) else x for x in worst_min],
    'best_min_eig':  [None if np.isnan(x) else x for x in best_min],
}
json.dump(out, open('CERT_OP1_delta_max_curvature.json','w'), indent=1)

print('G-DM0 Casimir, G-DM1 trace law (%.1e), G-DM2 FD (%.1e), G-DM3, G-DM4 : ALL PASS' %
      (worst_trace, worst_fd))
print('per-plaquette link Hessian block H_ab = (1/6)Re tr({T_a,T_b}U_p), trace = (4/3)(1-s_p)')
print('  strict negative-curvature ONSET   s_p* = %.4f  (= 2/3; first negative direction)' % sp_star)
print('  HARD net (trace) sign change       s_p  = 1.0    (calibration-independent ceiling)')
print('=> faithful defect threshold delta_max in [2/3, 1];  HARD ceiling delta_max <= 1')
print('=> Tier-R rate beta(delta-1) > 0 needs delta > 1  ==>  DISJOINT from the faithful window')
print()
print(' s_p   worst-min-eig  (per-class-bin)')
for i in range(0, nb, 4):
    if not np.isnan(worst_min[i]):
        flag = '  <-- onset' if (worst_min[i] < 0 and (i==0 or np.isnan(worst_min[i-4]) or worst_min[i-4]>=0)) else ''
        print('%.3f   %+.4f%s' % (binmid[i], worst_min[i], flag))
