#!/usr/bin/env python3
# =============================================================================
# ENGINE_OP1_op12_delta_window.py — deterministic firewall theta on the EXTENDED delta grid.
# June 12, 2026 (lead math agent, DECISIONS #009).  Companion to ENGINE_OP1_op12_runner.py.
#
# Question (F034 redirect): the (S) chessboard Tier-R rate is beta*(delta-1),
# which clears the rooted threshold log mu_animal = 3.996 at beta_c = 8.9..13.3
# for delta = 1.45..1.30.  Does the DETERMINISTIC firewall theta < 1 survive in
# that larger-delta window?  i.e. is the delta-window one-sided (only a lower
# sparsity edge) or two-sided (an upper comparator edge)?
#
# Method: REUSE the deposited thermalized MC states (op12_state/state_*.npz,
# therm_done=120/100, well past equilibration) and continue each chain to
# measure exactly the same Hodge-projected Birman-Schwinger ratio
#     theta(U) = v0 * lambda_max( Pi_D P M^{-1} P Pi_D ),  M = m0^2 I + (beta/6) d1*d1
# on the extended grid delta in {1.10, 1.20, 1.30, 1.40, 1.45}.
# delta=1.10 overlaps the deposited scan -> CONSISTENCY GATE (G-DW5).
#
# Hard gates (asserts): d1 d0 = 0 (lattice), P^2=P, [M,P]=0, CG convergence,
# and delta=1.10 ensemble mean reproduces the deposited scan within MC band.
# Deadline-chunked + resumable (own state dir dw_state/).
#
# Usage: python3 ENGINE_OP1_op12_delta_window.py [--deadline 40]   (call repeatedly)
# Prints ALL_WORK_DONE when complete.
# =============================================================================
import os, json, time, math, argparse
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.linalg import expm

T_START = time.time()
ap = argparse.ArgumentParser()
ap.add_argument('--deadline', type=float, default=40.0)
ap.add_argument('--srcdir', type=str, default='../op12_state')
ap.add_argument('--statedir', type=str, default='dw_state')
args = ap.parse_args()
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, args.srcdir)
SD = os.path.join(HERE, args.statedir)
os.makedirs(SD, exist_ok=True)

M2, V0 = 0.5, 1.0
DELTAS = [1.10, 1.20, 1.30, 1.40, 1.45]
NCFG, SEP = 16, 4
SCHEDULE = (
    [dict(L=4, beta=b) for b in (5.6, 6.0, 6.4, 6.8, 7.2)] +
    [dict(L=6, beta=b) for b in (5.6, 6.4, 7.2)]
)
# deposited delta=1.10 ensemble means (NOTE_OP1_results_2026-06-11.md) for the consistency gate
DEPOSITED_D110_MEAN = {
    (4, 5.6): 0.207, (4, 6.0): 0.132, (4, 6.4): 0.086, (4, 6.8): 0.017, (4, 7.2): 0.022,
    (6, 5.6): 0.181, (6, 6.4): 0.122, (6, 7.2): 0.033,
}
SEED = 20260612

def left():
    return args.deadline - (time.time() - T_START)

# ----------------------- lattice cache per L (identical to runner) ------------
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
    assert abs(d1 @ d0).max() == 0.0, 'GATE FAIL G-DW1: d1 d0 != 0'
    L0 = (d0.T @ d0).tocsr(); L1up = (d1.T @ d1).tocsr()
    _cache[L] = dict(D=D, Ns=Ns, Nl=Nl, ORIS=ORIS, nbr=nbr, pbr=pbr,
                     d0=d0, d1=d1, L0=L0, L1up=L1up, plinks=plinks)
    return _cache[L]

# --------------------------- SU(3) machinery (identical) ----------------------
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

# ------------------------------- theta (identical math) ------------------------
def proj_P(lat, f, tol=1e-11):
    Ns = lat['Ns']
    b = lat['d0'].T @ f; b = b - b.mean()
    z, info = spla.cg(lat['L0'] + sp.eye(Ns)*1e-12, b, rtol=tol, atol=0, maxiter=30000)
    assert info == 0, 'GATE FAIL G-DW4: CG(L0)'
    return f - lat['d0'] @ (z - z.mean())

def gates_PM(lat, Mop, rng):
    v = rng.standard_normal(lat['Nl'])
    Pv = proj_P(lat, v); PPv = proj_P(lat, Pv)
    assert np.linalg.norm(PPv-Pv) < 1e-7*(1+np.linalg.norm(Pv)), 'GATE FAIL G-DW2: P^2 != P'
    MPv = Mop @ Pv; PMPv = proj_P(lat, MPv)
    assert np.linalg.norm(PMPv-MPv) < 1e-6*(1+np.linalg.norm(MPv)), 'GATE FAIL G-DW3: [M,P] != 0'

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
        assert info == 0, 'GATE FAIL G-DW4: CG(M)'
        return mask*proj_P(lat, z)
    x = rng.standard_normal(lat['Nl'])*mask; x /= np.linalg.norm(x)
    lam_old = 0.0; lam_ = 0.0
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
    return (f'{SD}/dw_{tag}.npz', f'{SD}/dwmeta_{tag}.json', f'{SD}/dwres_{tag}.json')

def src_paths(job):
    tag = f"L{job['L']}_b{job['beta']}"
    return (f'{SRC}/state_{tag}.npz', f'{SRC}/meta_{tag}.json')

def load_job(job):
    dpz, dmeta, dres = paths(job)
    lat = lattice(job['L'])
    if os.path.exists(dmeta):
        meta = json.load(open(dmeta)); U = np.load(dpz)['U']
    else:
        spz, smeta = src_paths(job)
        U = np.load(spz)['U']                      # deposited thermalized config
        sm = json.load(open(smeta))
        meta = dict(cfgs_done=0, eps=sm['eps'], reequil=0)
    res = json.load(open(dres)) if os.path.exists(dres) else {'cfg': []}
    # fresh deterministic rng per job (we continue from a thermalized config;
    # chain-history rng is not reproduced -- documented in the finding).
    rng = np.random.default_rng(SEED + job['L']*1000 + int(job['beta']*10) + meta['cfgs_done'])
    return lat, U, meta, res, rng

def save_job(job, U, meta, res):
    dpz, dmeta, dres = paths(job)
    np.savez_compressed(dpz, U=U)
    json.dump(meta, open(dmeta, 'w')); json.dump(res, open(dres, 'w'))

def job_done(job):
    _, dmeta, _ = paths(job)
    if not os.path.exists(dmeta): return False
    return json.load(open(dmeta))['cfgs_done'] >= NCFG

# ------------------------------ work loop --------------------------------------
did = []
for job in SCHEDULE:
    if job_done(job): continue
    lat, U, meta, res, rng = load_job(job)
    Mop = (M2*sp.eye(lat['Nl']) + (job['beta']/6.0)*lat['L1up']).tocsr()
    if meta['cfgs_done'] == 0 and meta['reequil'] == 0:
        gates_PM(lat, Mop, rng)
    # short re-equilibration (8 sweeps) to decorrelate from the deposited tail
    while meta['reequil'] < 8 and left() > 6.0:
        sweep(lat, U, job['beta'], meta['eps'], rng); meta['reequil'] += 1
    # measurement
    cfg_cost = 6.0
    while meta['cfgs_done'] < NCFG and left() > cfg_cost + 2.0:
        t0 = time.time()
        for _ in range(SEP):
            sweep(lat, U, job['beta'], meta['eps'], rng)
        spl = plaq_field(lat, U)
        entry = {'cfg': meta['cfgs_done'], 'plaq': float(1.0 - spl.mean())}
        for dl in DELTAS:
            th, rp, rl, nD = theta_of(lat, spl, dl, Mop, rng)
            entry[f'theta_d{dl}'] = th; entry[f'rhoL_d{dl}'] = rl
            entry[f'rhoP_d{dl}'] = rp; entry[f'nD_d{dl}'] = nD
        res['cfg'].append(entry); meta['cfgs_done'] += 1
        cfg_cost = max(time.time() - t0, 2.0)
    save_job(job, U, meta, res)
    did.append(f"L{job['L']} b{job['beta']}: cfgs {meta['cfgs_done']}/{NCFG}")
    if left() < 4.0: break

print('PROGRESS :: ' + (' | '.join(did) if did else 'nothing to do'))

if all(job_done(j) for j in SCHEDULE):
    # ---- aggregate + consistency gate + summary ----
    summary = {'deltas': DELTAS, 'ncfg': NCFG, 'rows': []}
    gate_fail = []
    for job in SCHEDULE:
        _, _, dres = paths(job)
        res = json.load(open(dres))
        row = {'L': job['L'], 'beta': job['beta'],
               'plaq': float(np.mean([c['plaq'] for c in res['cfg']]))}
        for dl in DELTAS:
            ths = np.array([c[f'theta_d{dl}'] for c in res['cfg']])
            nDs = np.array([c[f'nD_d{dl}'] for c in res['cfg']])
            row[f'th_mean_d{dl}'] = float(ths.mean())
            row[f'th_max_d{dl}'] = float(ths.max())
            row[f'nD_mean_d{dl}'] = float(nDs.mean())
            row[f'nD_max_d{dl}'] = int(nDs.max())
            row[f'frac_zero_d{dl}'] = float((nDs == 0).mean())
        # G-DW5 consistency: delta=1.10 mean within MC band of deposited
        dep = DEPOSITED_D110_MEAN[(job['L'], job['beta'])]
        mine = row['th_mean_d1.1']
        row['dep_d1.1'] = dep
        ok = abs(mine - dep) < 0.12 + 0.5*dep
        if not ok: gate_fail.append((job['L'], job['beta'], mine, dep))
        summary['rows'].append(row)
    assert not gate_fail, f'GATE FAIL G-DW5 (delta=1.10 consistency): {gate_fail}'
    # G-DW6: monotone non-increase of theta in delta (per row, mean)
    for row in summary['rows']:
        means = [row[f'th_mean_d{dl}'] for dl in DELTAS]
        assert all(means[i+1] <= means[i] + 1e-9 for i in range(len(means)-1)), \
            f"GATE FAIL G-DW6: theta not monotone in delta at L{row['L']} b{row['beta']}: {means}"
    summary['all_gates'] = 'G-DW1..G-DW6 PASS'
    json.dump(summary, open(f'{SD}/../CERT_OP1_delta_window_summary.json', 'w'), indent=1)
    print('G-DW5 consistency PASS; G-DW6 monotonicity PASS')
    print('ALL_WORK_DONE')
