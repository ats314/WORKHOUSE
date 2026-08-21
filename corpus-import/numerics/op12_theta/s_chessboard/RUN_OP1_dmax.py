#!/usr/bin/env python3
# Fresh-path run copy of ENGINE_OP1_delta_max_curvature.py (VM mount served a stale truncated
# view of the canonical file; host copy is correct — this is byte-equivalent logic).
import json, math
import numpy as np

lam = np.zeros((8, 3, 3), dtype=np.complex128)
lam[0][0,1]=lam[0][1,0]=1; lam[1][0,1]=-1j; lam[1][1,0]=1j
lam[2][0,0]=1; lam[2][1,1]=-1
lam[3][0,2]=lam[3][2,0]=1; lam[4][0,2]=-1j; lam[4][2,0]=1j
lam[5][1,2]=lam[5][2,1]=1; lam[6][1,2]=-1j; lam[6][2,1]=1j
lam[7][0,0]=lam[7][1,1]=1/math.sqrt(3); lam[7][2,2]=-2/math.sqrt(3)
T = lam/2.0
I3 = np.eye(3, dtype=np.complex128)

Csum = sum(T[a] @ T[a] for a in range(8))
assert np.allclose(Csum, (4.0/3.0)*I3, atol=1e-13), 'GATE FAIL G-DM0'

ANTI = np.zeros((8,8,3,3), dtype=np.complex128)
for a in range(8):
    for b in range(8):
        ANTI[a,b] = T[a] @ T[b] + T[b] @ T[a]

def hessian_block(U):
    H = np.zeros((8,8))
    for a in range(8):
        for b in range(a,8):
            v = (1.0/6.0)*np.real(np.trace(ANTI[a,b] @ U))
            H[a,b] = v; H[b,a] = v
    return H

def sp_of(U):
    return 1.0 - np.real(np.trace(U))/3.0

def U_class(th1, th2):
    th3 = -th1 - th2
    return np.diag([np.exp(1j*th1), np.exp(1j*th2), np.exp(1j*th3)]).astype(np.complex128)

rng = np.random.default_rng(20260612)
worst_trace = 0.0
for _ in range(400):
    th1 = rng.uniform(-math.pi, math.pi); th2 = rng.uniform(-math.pi, math.pi)
    U = U_class(th1, th2); H = hessian_block(U)
    worst_trace = max(worst_trace, abs(np.trace(H) - (4.0/3.0)*(1.0 - sp_of(U))))
assert worst_trace < 1e-12, f'GATE FAIL G-DM1: {worst_trace}'

def s_p_perturbed(U, tvec):
    X = sum(tvec[a]*T[a] for a in range(8))
    w, Vv = np.linalg.eigh(X)
    expiX = (Vv * np.exp(1j*w)) @ Vv.conj().T
    return 1.0 - np.real(np.trace(expiX @ U))/3.0
Utest = U_class(0.7, -0.3); H_an = hessian_block(Utest)
h = 1e-4; worst_fd = 0.0
for a in range(8):
    for b in range(8):
        ea = np.zeros(8); ea[a]+=h
        eb = np.zeros(8); eb[b]+=h
        d2 = (s_p_perturbed(Utest, ea+eb) - s_p_perturbed(Utest, ea-eb)
              - s_p_perturbed(Utest, -ea+eb) + s_p_perturbed(Utest, -ea-eb))/(4*h*h)
        worst_fd = max(worst_fd, abs(d2 - H_an[a,b]))
assert worst_fd < 1e-6, f'GATE FAIL G-DM2: {worst_fd}'

N = 240
grid = np.linspace(-math.pi, math.pi, N)
records = []; sp_star = None; sp_star_at = None
for th1 in grid:
    for th2 in grid:
        U = U_class(th1, th2); sp = sp_of(U)
        mineig = float(np.linalg.eigvalsh(hessian_block(U))[0])
        records.append((sp, mineig))
        if mineig < 0 and (sp_star is None or sp < sp_star):
            sp_star = sp; sp_star_at = (float(th1), float(th2))
records = np.array(records)
nb = 60; edges = np.linspace(0, 1.5, nb+1); binmid = 0.5*(edges[:-1]+edges[1:])
worst_min = np.full(nb, np.nan); best_min = np.full(nb, np.nan)
for i in range(nb):
    sel = (records[:,0] >= edges[i]) & (records[:,0] < edges[i+1])
    if sel.any():
        worst_min[i] = records[sel,1].min(); best_min[i] = records[sel,1].max()

viol = [(r[0], r[1]) for r in records if r[0] > 1.0 + 1e-9 and r[1] >= 0]
assert not viol, f'GATE FAIL G-DM3: {len(viol)}'
assert sp_star is not None and sp_star <= 1.0 + 1e-9, f'GATE FAIL G-DM4: {sp_star}'

out = {
    'gates': 'G-DM0..G-DM4 PASS',
    'casimir_CF': 4.0/3.0,
    'trace_law': 'trace H_ab = (4/3)(1 - s_p)  [exact; G-DM1 worst dev %.2e]' % worst_trace,
    'fd_crosscheck_worst': worst_fd,
    'sp_negcurv_onset_strict': sp_star,
    'sp_negcurv_onset_at_angles': sp_star_at,
    'sp_trace_signchange_hard': 1.0,
    'delta_max_hard': 1.0,
    'delta_max_strict': sp_star,
    'faithful_range': [sp_star, 1.0],
    'tier_R_needs_delta_gt_1': True,
    'window_disjoint_with_tierR': True,
    'bins_s_p': binmid.tolist(),
    'worst_min_eig': [None if np.isnan(x) else x for x in worst_min],
    'best_min_eig':  [None if np.isnan(x) else x for x in best_min],
}
json.dump(out, open('CERT_OP1_delta_max_curvature.json','w'), indent=1)
print('G-DM0 Casimir, G-DM1 trace law (%.1e), G-DM2 FD (%.1e), G-DM3, G-DM4 : ALL PASS' % (worst_trace, worst_fd))
print('per-plaquette block H_ab=(1/6)Re tr({T_a,T_b}U_p), trace=(4/3)(1-s_p)')
print('  strict neg-curv ONSET  s_p* = %.4f (=2/3, first negative direction)' % sp_star)
print('  HARD net(trace) signchange s_p = 1.0 (calibration-independent ceiling)')
print('=> faithful delta_max in [2/3, 1]; HARD ceiling delta_max <= 1; Tier-R needs delta>1 => DISJOINT')
print(' s_p   worst-min-eig')
for i in range(0, nb, 4):
    if not np.isnan(worst_min[i]):
        print('%.3f   %+.4f' % (binmid[i], worst_min[i]))
