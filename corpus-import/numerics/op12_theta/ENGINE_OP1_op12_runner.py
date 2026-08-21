#!/usr/bin/env python3
# =============================================================================
# ENGINE_OP1_op12_runner.py — OP-12 direct theta computation, deadline-chunked runner.
# June 11, 2026.  See header of op12_theta_scan.py (same math, same gates);
# this version checkpoints MC state so the scan can be driven in bounded
# slices (the execution environment kills background jobs between calls).
#
#   theta(U) = v0 * lambda_max( Pi_D P M^{-1} P Pi_D ),  M = m0^2 I + (beta/6) d1*d1
#   P = Hodge projector onto ker d0^* (commutes with M since d1 d0 = 0; gated)
#   defects: plaquette-seeded links, s_p = 1 - Re tr U_p/3 > delta
#
# Usage:  python3 ENGINE_OP1_op12_runner.py [--deadline 36]     (call repeatedly)
# Prints ALL_WORK_DONE when the full schedule below is complete.
# =============================================================================
import os, json, time, math, argparse
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.linalg import expm

T_START = time.time()
ap = argparse.ArgumentParser()
ap.add_argument('--deadline', type=float, default=36.0)
ap.add_argument('--statedir', type=str, default='op12_state')
args = ap.parse_args()
os.makedirs(args.statedir, exist_ok=True)

# ----------------------------- schedule --------------------------------------
M2, V0 = 0.5, 1.0
DELTAS = [0.70, 0.90, 1.10]
SCHEDULE = (
    [dict(L=4, beta=b, therm=120, ncfg=20, sep=4) for b in (5.6, 6.0, 6.4, 6.8, 7.2)] +
    [dict(L=6, beta=b, therm=100, ncfg=12, sep=4) for b in (5.6, 6.4, 7.2)]
)
SEED = 20260611

def left():
    return args.deadline - (time.time() - T_START)

# ----------------------- lattice cache per L ----------------------------------
_cache = {}
def lattice(L):
    if L in _cache: return _cache[L]
    D = 4; Ns = L**D; Nl = D*Ns
    ORIS = [(mu, nu) for mu in range(D) for nu in range(mu+1, D)]
    coords = np.array([[s % L, (s//L) % L, (s//L**2) % L, (s//L**3) % L]
                       for s in range(Ns)], dtype=np.int64)
    def sidx(x): return ((x[3]*L + x[2])*L + x[1])*L + x[0]
    nbr = np.zeros((Ns, D), dtype=np.int64); pbr = np.zeros((Ns, D), dtype=np.int64)
    for s in range(Ns):
        for mu in range(D):
            xp = coords[s].copy(); xp[mu] = (xp[mu]+1) % L
            xm = coords[s].copy(); xm[mu] = (xm[mu]-1) % L
            nbr[s, mu] = sidx(xp); pbr[s, mu] = sidx(xm)
    rows, cols, vals = [], [], []
    for s in range(Ns):
        for mu in range(D):
            l = 4*s+mu; rows += [l, l]; cols += [nbr[s, mu], s]; vals += [1.0, -1.0]
    d0 = sp.csr_matrix((vals, (rows, cols)), shape=(Nl, Ns))
    rows, cols, vals = [], [], []
    Np_ = 6*Ns; plinks = np.zeros((Np_, 4), dtype=np.int64)
    for s in range(Ns):
        for oi, (mu, nu) in enumerate(ORIS):
            p = 6*s+oi
            ls = [4*s+mu, 4*nbr[s, mu]+nu, 4*nbr[s, nu]+mu, 4*s+nu]
            plinks[p] = ls
            rows += [p]*4; cols += ls; vals += [1.0, 1.0, -1.0, -1.0]
    d1 = sp.csr_matrix((vals, (rows, cols)), shape=(Np_, Nl))
    assert abs(d1 @ d0).max() == 0.0, 'GATE FAIL: d1 d0 != 0'
    L0 = (d0.T @ d0).tocsr(); L1up = (d1.T @ d1).tocsr()
    _cache[L] = dict(D=D, Ns=Ns, Nl=Nl, ORIS=ORIS, nbr=nbr, pbr=pbr,
                     d0=d0, d1=d1, L0=L0, L1up=L1up, plinks=plinks)
    return _cache[L]

# --------------------------- SU(3) machinery ----------------------------------
lam = np.zeros((8, 3, 3), dtype=np.complex128)
lam[0][0,1]=lam[0][1,0]=1; lam[1][0,1]=-1j; lam[1][1,0]=1j
lam[2][0,0]=1; lam[2][1,1]=-1
lam[3][0,2]=lam[3][2,0]=1; lam[4][0,2]=-1j; lam[4][2,0]=1j
lam[5][1,2]=lam[5][2,1]=1; lam[6][1,2]=-1j; lam[6][2,1]=1j
lam[7][0,0]=lam[7][1,1]=1/math.sqrt(3); lam[7][2,2]=-2/math.sqrt(3)
I3 = np.eye(3, dtype=np.complex128)

def r_pool(rng, eps, n=96):
    Rs = np.zeros((2*n, 3, 3), dtype=np.complex128)
    for k in range(n):
        a = rng.standard_normal(8)
        H = np.tensordot(a, lam, axes=(0, 0))
        R = expm(1j*eps*H); Rs[2*k] = R; Rs[2*k+1] = R.conj().T
    return Rs

def sweep(lat, U, beta, eps, rng):
    nbr, pbr, D, Ns = lat['nbr'], lat['pbr'], lat['D'], lat['Ns']
    Rs = r_pool(rng, eps); nR = Rs.shape[0]; acc = 0
    for s in range(Ns):
        for mu in range(D):
            A = np.zeros((3, 3), dtype=np.complex128)
            for nu in range(D):
                if nu == mu: continue
                A += U[nbr[s, mu], nu] @ U[nbr[s, nu], mu].conj().T @ U[s, nu].conj().T
                sm = pbr[s, nu]
                A += U[nbr[sm, mu], nu].conj().T @ U[sm, mu].conj().T @ U[sm, nu]
            Uo = U[s, mu]; Up = Rs[rng.integers(nR)] @ Uo
            dS = -(beta/3.0) * (np.trace((Up - Uo) @ A).real)
            if dS <= 0 or rng.random() < math.exp(-dS):
                U[s, mu] = Up; acc += 1
    return acc / (Ns*D)

def plaq_field(lat, U):
    Ns, ORIS, nbr = lat['Ns'], lat['ORIS'], lat['nbr']
    out = np.zeros(6*Ns)
    for s in range(Ns):
        for oi, (mu, nu) in enumerate(ORIS):
            Upl = U[s, mu] @ U[nbr[s, mu], nu] @ U[nbr[s, nu], mu].conj().T @ U[s, nu].conj().T
            out[6*s+oi] = 1.0 - np.trace(Upl).real/3.0
    return out

# ------------------------------- theta -----------------------------------------
def proj_P(lat, f, tol=1e-11):
    Ns = lat['Ns']
    b = lat['d0'].T @ f; b = b - b.mean()
    z, info = spla.cg(lat['L0'] + sp.eye(Ns)*1e-12, b, rtol=tol, atol=0, maxiter=30000)
    assert info == 0, 'GATE FAIL: CG(L0)'
    return f - lat['d0'] @ (z - z.mean())

def gates_PM(lat, Mop, rng):
    v = rng.standard_normal(lat['Nl'])
    Pv = proj_P(lat, v); PPv = proj_P(lat, Pv)
    assert np.linalg.norm(PPv-Pv) < 1e-7*(1+np.linalg.norm(Pv)), 'GATE FAIL: P^2 != P'
    MPv = Mop @ Pv; PMPv = proj_P(lat, MPv)
    assert np.linalg.norm(PMPv-MPv) < 1e-6*(1+np.linalg.norm(MPv)), 'GATE FAIL: [M,P] != 0'

def theta_of(lat, spl, delta, Mop, rng):
    bad = spl > delta
    if not bad.any():
        return 0.0, 0.0, 0.0, 0
    dlinks = np.unique(lat['plinks'][bad].ravel())
    rho_p = float(bad.mean()); rho_l = len(dlinks)/lat['Nl']
    mask = np.zeros(lat['Nl']); mask[dlinks] = 1.0
    def Bmat(x):
        y = proj_P(lat, mask*x)
        z, info = spla.cg(Mop, y, rtol=1e-10, atol=0, maxiter=30000)
        assert info == 0, 'GATE FAIL: CG(M)'
        return mask*proj_P(lat, z)
    x = rng.standard_normal(lat['Nl'])*mask; x /= np.linalg.norm(x)
    lam_old = 0.0
    for it in range(120):
        y = Bmat(x); lam_ = float(x @ y); ny = np.linalg.norm(y)
        if ny == 0: return 0.0, rho_p, rho_l, len(dlinks)
        x = y/ny
        if it > 8 and abs(lam_-lam_old) < 1e-9*max(1.0, abs(lam_)): break
        lam_old = lam_
    return V0*lam_, rho_p, rho_l, int(len(dlinks))

# ------------------------------ state I/O --------------------------------------
def paths(job):
    tag = f"L{job['L']}_b{job['beta']}"
    sd = args.statedir
    return (f'{sd}/state_{tag}.npz', f'{sd}/meta_{tag}.json', f'{sd}/results_{tag}.json')

def load_job(job):
    spz, smeta, sres = paths(job)
    lat = lattice(job['L'])
    if os.path.exists(smeta):
        meta = json.load(open(smeta))
        U = np.load(spz)['U']
    else:
        meta = dict(therm_done=0, cfgs_done=0, eps=0.22, plaqs=[], rngstate=SEED)
        U = np.tile(I3, (lat['Ns'], lat['D'], 1, 1)).astype(np.complex128)
    res = json.load(open(sres)) if os.path.exists(sres) else {'cfg': []}
    rng = np.random.default_rng(meta['rngstate'])
    return lat, U, meta, res, rng

def save_job(job, U, meta, res):
    spz, smeta, sres = paths(job)
    np.savez_compressed(spz, U=U)
    meta['rngstate'] = int(np.random.default_rng(meta['rngstate']).integers(2**62))
    json.dump(meta, open(smeta, 'w'))
    json.dump(res, open(sres, 'w'))

# ------------------------------ work loop ---------------------------------------
def job_done(job):
    _, smeta, _ = paths(job)
    if not os.path.exists(smeta): return False
    m = json.load(open(smeta))
    return m['therm_done'] >= job['therm'] and m['cfgs_done'] >= job['ncfg']

did = []
for job in SCHEDULE:
    if job_done(job): continue
    lat, U, meta, res, rng = load_job(job)
    Mop = (M2*sp.eye(lat['Nl']) + (job['beta']/6.0)*lat['L1up']).tocsr()
    if meta['therm_done'] == 0:
        gates_PM(lat, Mop, rng)
    # estimate sweep cost on the fly
    t0 = time.time(); a = sweep(lat, U, job['beta'], meta['eps'], rng)
    sweep_cost = time.time() - t0
    meta['therm_done'] += 1
    if a < 0.35: meta['eps'] *= 0.94
    elif a > 0.65: meta['eps'] *= 1.06
    # thermalization chunks
    while meta['therm_done'] < job['therm'] and left() > sweep_cost*1.6 + 2.0:
        a = sweep(lat, U, job['beta'], meta['eps'], rng)
        meta['therm_done'] += 1
        if a < 0.35: meta['eps'] *= 0.94
        elif a > 0.65: meta['eps'] *= 1.06
    # measurement chunks (one cfg = sep sweeps + plaq + theta for all deltas)
    cfg_cost = sweep_cost*job['sep'] + sweep_cost*4 + 3.0   # rough; refined after first cfg
    while (meta['therm_done'] >= job['therm'] and meta['cfgs_done'] < job['ncfg']
           and left() > cfg_cost + 2.0):
        t0 = time.time()
        for _ in range(job['sep']):
            a = sweep(lat, U, job['beta'], meta['eps'], rng)
            if a < 0.35: meta['eps'] *= 0.94
            elif a > 0.65: meta['eps'] *= 1.06
        spl = plaq_field(lat, U)
        entry = {'cfg': meta['cfgs_done'], 'plaq': float(1.0 - spl.mean())}
        for dl in DELTAS:
            th, rp, rl, nD = theta_of(lat, spl, dl, Mop, rng)
            entry[f'theta_d{dl}'] = th; entry[f'rhoL_d{dl}'] = rl
            entry[f'rhoP_d{dl}'] = rp; entry[f'nD_d{dl}'] = nD
        res['cfg'].append(entry)
        meta['cfgs_done'] += 1
        meta['plaqs'].append(entry['plaq'])
        cfg_cost = time.time() - t0
    save_job(job, U, meta, res)
    did.append(f"L{job['L']} b{job['beta']}: therm {meta['therm_done']}/{job['therm']}"
               f" cfgs {meta['cfgs_done']}/{job['ncfg']}")
    if left() < 4.0: break

print('PROGRESS :: ' + (' | '.join(did) if did else 'nothing to do'))
if all(job_done(j) for j in SCHEDULE):
    print('ALL_WORK_DONE')
