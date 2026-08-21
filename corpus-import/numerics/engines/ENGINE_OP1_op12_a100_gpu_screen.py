#!/usr/bin/env python3
# =============================================================================
# ENGINE_OP1_op12_a100_gpu_screen.py
#
# GPU-accelerated OP-12 theta screening for SU(3) Wilson gauge theory.
#
# WHAT THIS IS (and is not):
#   * This is the ONE part of the program that genuinely belongs on an A100:
#     Monte-Carlo SU(3) Wilson configuration generation + the float theta
#     observable, run massively in parallel so the scan can reach larger L,
#     more configs, and wider beta than the CPU runner.
#   * The arithmetic here is FLOATING POINT (FP64).  Per the verified GPU
#     assessment, GPU float output is SCREENING EVIDENCE, not a certificate.
#     The exact, gate-backed theta certificate stays on CPU (the M2 exact
#     pair-certificate machinery).  Use this to locate interesting (L,beta,delta)
#     points fast; certify the chosen points exactly afterwards.
#
# CONVENTION (identical to numerics/op12_theta/ENGINE_OP1_op12_runner.py):
#   theta(U) = v0 * lambda_max( Pi_D P M^{-1} P Pi_D )
#   M        = m0^2 I + (beta/6) d1^* d1            (up-Laplacian on 1-cochains)
#   P        = Hodge projector onto ker d0^*        ([M,P]=0 since d1 d0 = 0)
#   defects  = plaquette-seeded links, s_p = 1 - Re tr U_p / 3 > delta
#   sampler  = single-hit Metropolis, adaptive eps, checkerboard-parallel
#
# BACKEND: runs on GPU via CuPy if available, else NumPy on CPU (identical code
#   path -- so a passing CPU self-test validates the GPU run).  FP64 throughout;
#   the A100's strong IEEE FP64 (9.7 TF, 19.5 TF via tensor cores) is exactly
#   why it is the right card for a theta-near-1 observable.
#
# HARD GATES (assert, not warn): d1 d0 = 0 ; link unitarity ; P^2 = P ; [M,P]=0 ;
#   plaquette in physical range ; theta real & finite.
#
# USAGE
#   Self-test (tiny, validates all gates):    python3 ENGINE_OP1_op12_a100_gpu_screen.py --selftest
#   Real screening run on the A100:
#       python3 ENGINE_OP1_op12_a100_gpu_screen.py --L 8 --betas 5.6,6.0,6.4,6.8,7.2 \
#               --therm 200 --ncfg 40 --sep 5 --deltas 0.7,0.9,1.1 --out op12_gpu_out
#   Pure sampler throughput benchmark (no theta):
#       python3 ENGINE_OP1_op12_a100_gpu_screen.py --L 12 --betas 6.4 --therm 100 --ncfg 0 --no-theta
# =============================================================================
import os, sys, json, time, math, argparse
import numpy as np
from scipy.linalg import expm
import scipy.sparse as ssp

# ---------------------------------------------------------------- backend ----
USE_GPU = False
try:
    import cupy as cp
    import cupyx.scipy.sparse as xsp_gpu
    if cp.cuda.runtime.getDeviceCount() > 0:
        USE_GPU = True
except Exception:
    cp = None

if USE_GPU:
    xp = cp
    xsp = xsp_gpu
    _dev = cp.cuda.runtime.getDeviceProperties(cp.cuda.runtime.getDevice())
    BACKEND = f"CuPy / GPU [{_dev['name'].decode() if isinstance(_dev['name'], bytes) else _dev['name']}]"
else:
    xp = np
    xsp = ssp
    BACKEND = "NumPy / CPU"

def to_host(a):
    return cp.asnumpy(a) if (USE_GPU and isinstance(a, cp.ndarray)) else np.asarray(a)

def asdev(a):
    return cp.asarray(a) if USE_GPU else np.asarray(a)

def dag(M):
    # conjugate transpose over the last two axes of a stack of matrices
    return xp.conj(xp.swapaxes(M, -1, -2))

# --------------------------------------------------------- self-contained CG --
# Backend-agnostic conjugate gradient on real SPD operators given as a matvec.
# Avoids scipy/cupy cg kwarg drift (rtol vs tol vs atol) entirely.
def cg_solve(matvec, b, tol=1e-10, maxiter=30000):
    x = xp.zeros_like(b)
    r = b - matvec(x)
    p = r.copy()
    rs = float(xp.dot(r, r))
    bnorm = math.sqrt(float(xp.dot(b, b))) + 1e-300
    if math.sqrt(rs) <= tol * bnorm:
        return x, 0
    for _ in range(maxiter):
        Ap = matvec(p)
        denom = float(xp.dot(p, Ap))
        if denom == 0.0:
            return x, 1
        alpha = rs / denom
        x = x + alpha * p
        r = r - alpha * Ap
        rs_new = float(xp.dot(r, r))
        if math.sqrt(rs_new) <= tol * bnorm:
            return x, 0
        p = r + (rs_new / rs) * p
        rs = rs_new
    return x, 1

# ---------------------------------------------------------------- lattice ----
def build_lattice(L):
    D = 4; Ns = L**D; Nl = D * Ns
    ORIS = [(mu, nu) for mu in range(D) for nu in range(mu + 1, D)]
    coords = np.array([[s % L, (s // L) % L, (s // L**2) % L, (s // L**3) % L]
                       for s in range(Ns)], dtype=np.int64)
    def sidx(x): return ((x[3] * L + x[2]) * L + x[1]) * L + x[0]
    nbr = np.zeros((Ns, D), dtype=np.int64); pbr = np.zeros((Ns, D), dtype=np.int64)
    for s in range(Ns):
        for mu in range(D):
            xp_ = coords[s].copy(); xp_[mu] = (xp_[mu] + 1) % L
            xm_ = coords[s].copy(); xm_[mu] = (xm_[mu] - 1) % L
            nbr[s, mu] = sidx(xp_); pbr[s, mu] = sidx(xm_)
    parity = (coords.sum(axis=1) % 2).astype(np.int64)

    # d0 : 0-cochains -> 1-cochains ; d1 : 1-cochains -> 2-cochains (plaquettes)
    rows, cols, vals = [], [], []
    for s in range(Ns):
        for mu in range(D):
            l = 4 * s + mu; rows += [l, l]; cols += [nbr[s, mu], s]; vals += [1.0, -1.0]
    d0 = ssp.csr_matrix((vals, (rows, cols)), shape=(Nl, Ns))
    rows, cols, vals = [], [], []
    Np_ = 6 * Ns; plinks = np.zeros((Np_, 4), dtype=np.int64)
    for s in range(Ns):
        for oi, (mu, nu) in enumerate(ORIS):
            p = 6 * s + oi
            ls = [4 * s + mu, 4 * nbr[s, mu] + nu, 4 * nbr[s, nu] + mu, 4 * s + nu]
            plinks[p] = ls
            rows += [p] * 4; cols += ls; vals += [1.0, 1.0, -1.0, -1.0]
    d1 = ssp.csr_matrix((vals, (rows, cols)), shape=(Np_, Nl))
    assert abs(d1 @ d0).max() == 0.0, 'GATE FAIL: d1 d0 != 0'

    L0 = (d0.T @ d0).tocsr(); L1up = (d1.T @ d1).tocsr()

    lat = dict(D=D, Ns=Ns, Nl=Nl, ORIS=ORIS, plinks=plinks,
               nbr_h=nbr, pbr_h=pbr,
               nbr=asdev(nbr), pbr=asdev(pbr),
               plinks_dev=asdev(plinks),
               d0=xsp.csr_matrix(d0), d0T=xsp.csr_matrix(d0.T.tocsr()),
               L0=xsp.csr_matrix(L0), L1up_h=L1up)
    return lat

# --------------------------------------------------------- SU(3) machinery ---
_lam = np.zeros((8, 3, 3), dtype=np.complex128)
_lam[0][0, 1] = _lam[0][1, 0] = 1; _lam[1][0, 1] = -1j; _lam[1][1, 0] = 1j
_lam[2][0, 0] = 1; _lam[2][1, 1] = -1
_lam[3][0, 2] = _lam[3][2, 0] = 1; _lam[4][0, 2] = -1j; _lam[4][2, 0] = 1j
_lam[5][1, 2] = _lam[5][2, 1] = 1; _lam[6][1, 2] = -1j; _lam[6][2, 1] = 1j
_lam[7][0, 0] = _lam[7][1, 1] = 1 / math.sqrt(3); _lam[7][2, 2] = -2 / math.sqrt(3)

def rotation_pool(eps, n, pool_rng):
    # built on CPU with scipy.expm (exact SU(3)), then shipped to the device.
    Rs = np.zeros((2 * n, 3, 3), dtype=np.complex128)
    for k in range(n):
        a = pool_rng.standard_normal(8)
        H = np.tensordot(a, _lam, axes=(0, 0))
        R = expm(1j * eps * H)
        Rs[2 * k] = R; Rs[2 * k + 1] = R.conj().T
    return asdev(Rs)

def reunitarize(U):
    # batched projection of (...,3,3) back onto SU(3): Gram-Schmidt columns,
    # third column fixed by conjugate cross product to force det = +1.
    c0 = U[..., :, 0]; c1 = U[..., :, 1]
    c0 = c0 / xp.linalg.norm(c0, axis=-1, keepdims=True)
    c1 = c1 - xp.sum(xp.conj(c0) * c1, axis=-1, keepdims=True) * c0
    c1 = c1 / xp.linalg.norm(c1, axis=-1, keepdims=True)
    c2 = xp.conj(xp.cross(c0, c1))
    return xp.stack([c0, c1, c2], axis=-1)

def staples(lat, U, mu):
    # sum of the 6 staples for every direction-mu link, vectorized over all sites
    Ns, D, nbr, pbr = lat['Ns'], lat['D'], lat['nbr'], lat['pbr']
    A = xp.zeros((Ns, 3, 3), dtype=xp.complex128)
    smu = nbr[:, mu]
    for nu in range(D):
        if nu == mu:
            continue
        snu = nbr[:, nu]
        A = A + U[smu, nu] @ dag(U[snu, mu]) @ dag(U[:, nu])          # forward
        sm = pbr[:, nu]; smmu = nbr[sm, mu]
        A = A + dag(U[smmu, nu]) @ dag(U[sm, mu]) @ U[sm, nu]         # backward
    return A

def metropolis_sweep(lat, U, beta, pool, parity_dev):
    # checkerboard, single hit per link; returns acceptance fraction.
    Ns, D = lat['Ns'], lat['D']
    npool = pool.shape[0]
    acc = 0; att = 0
    for mu in range(D):
        A = None
        for color in (0, 1):
            A = staples(lat, U, mu)                      # depends only on frozen links
            idx = xp.random.randint(0, npool, size=Ns)
            R = pool[idx]                                # (Ns,3,3) random SU(3)
            Uo = U[:, mu]
            Up = R @ Uo
            dlt = Up - Uo
            dS = -(beta / 3.0) * xp.real(xp.einsum('sij,sji->s', dlt, A))
            u = xp.random.random(Ns)
            accept = (dS <= 0) | (u < xp.exp(-xp.clip(dS, 0.0, 700.0)))
            sel = accept & (parity_dev == color)
            U[:, mu] = xp.where(sel[:, None, None], Up, Uo)
            acc += int(to_host(xp.count_nonzero(sel)))
            att += int(to_host(xp.count_nonzero(parity_dev == color)))
    return acc / max(att, 1)

def plaquette_field(lat, U):
    Ns, ORIS, nbr = lat['Ns'], lat['ORIS'], lat['nbr']
    out = xp.zeros(6 * Ns, dtype=xp.float64)
    for oi, (mu, nu) in enumerate(ORIS):
        smu = nbr[:, mu]; snu = nbr[:, nu]
        Upl = U[:, mu] @ U[smu, nu] @ dag(U[snu, mu]) @ dag(U[:, nu])
        tr = xp.real(xp.einsum('sii->s', Upl))
        out[oi::6] = 1.0 - tr / 3.0
    return out

# ---------------------------------------------------------------- theta ------
def make_M_matvec(lat, beta, m2):
    L1up = xsp.csr_matrix(lat['L1up_h'])
    def mv(v):
        return m2 * v + (beta / 6.0) * (L1up @ v)
    return mv

def proj_P(lat, f, tol=1e-11):
    Ns = lat['Ns']
    b = lat['d0T'] @ f
    b = b - b.mean()
    Iv = lambda v: lat['L0'] @ v + 1e-12 * v
    z, info = cg_solve(Iv, b, tol=tol, maxiter=30000)
    assert info == 0, 'GATE FAIL: CG(L0) did not converge'
    z = z - z.mean()
    return f - lat['d0'] @ z

def gate_PM(lat, Mmv, rng):
    v = asdev(rng.standard_normal(lat['Nl']))
    Pv = proj_P(lat, v); PPv = proj_P(lat, Pv)
    e1 = float(xp.linalg.norm(PPv - Pv)) / (1 + float(xp.linalg.norm(Pv)))
    assert e1 < 1e-6, f'GATE FAIL: P^2 != P ({e1:.2e})'
    MPv = Mmv(Pv); PMPv = proj_P(lat, MPv)
    e2 = float(xp.linalg.norm(PMPv - MPv)) / (1 + float(xp.linalg.norm(MPv)))
    assert e2 < 1e-5, f'GATE FAIL: [M,P] != 0 ({e2:.2e})'
    return e1, e2

def theta_of(lat, spl, delta, Mmv, v0, rng):
    bad = spl > delta
    nbad = int(to_host(xp.count_nonzero(bad)))
    if nbad == 0:
        return 0.0, 0.0, 0.0, 0
    bad_h = to_host(bad).astype(bool)
    dlinks = np.unique(lat['plinks'][bad_h].ravel())
    rho_p = nbad / spl.shape[0]
    rho_l = len(dlinks) / lat['Nl']
    mask = np.zeros(lat['Nl']); mask[dlinks] = 1.0
    mask = asdev(mask)
    def Bmat(x):
        y = proj_P(lat, mask * x)
        z, info = cg_solve(Mmv, y, tol=1e-10, maxiter=30000)
        assert info == 0, 'GATE FAIL: CG(M) did not converge'
        return mask * proj_P(lat, z)
    x = asdev(rng.standard_normal(lat['Nl'])) * mask
    x = x / xp.linalg.norm(x)
    lam_old = 0.0; lam_ = 0.0
    for it in range(160):
        y = Bmat(x); lam_ = float(xp.dot(x, y)); ny = float(xp.linalg.norm(y))
        if ny == 0.0:
            return 0.0, rho_p, rho_l, len(dlinks)
        x = y / ny
        if it > 8 and abs(lam_ - lam_old) < 1e-9 * max(1.0, abs(lam_)):
            break
        lam_old = lam_
    assert math.isfinite(lam_), 'GATE FAIL: theta not finite'
    return v0 * lam_, rho_p, rho_l, int(len(dlinks))

# ---------------------------------------------------------------- driver -----
def run(args):
    print(f"backend       : {BACKEND}")
    print(f"precision     : complex128 / float64 (FP64)")
    betas  = [float(b) for b in args.betas.split(',')]
    deltas = [float(d) for d in args.deltas.split(',')]
    os.makedirs(args.out, exist_ok=True)
    lat = build_lattice(args.L)
    print(f"lattice       : L={args.L}  sites={lat['Ns']}  links={lat['Nl']}")
    pool_rng = np.random.default_rng(args.seed + 7)
    if USE_GPU:
        cp.random.seed(args.seed)
    else:
        np.random.seed(args.seed)
    parity_dev = asdev((np.array(
        [[s % args.L, (s // args.L) % args.L, (s // args.L**2) % args.L,
          (s // args.L**3) % args.L] for s in range(lat['Ns'])]).sum(axis=1) % 2))
    gate_rng = np.random.default_rng(args.seed + 99)

    summary = {}
    for beta in betas:
        tag = f"L{args.L}_b{beta}"
        Mmv = make_M_matvec(lat, beta, args.m2)
        if not args.no_theta:
            e1, e2 = gate_PM(lat, Mmv, gate_rng)
            print(f"[{tag}] gates  P^2=P res={e1:.1e}  [M,P]=0 res={e2:.1e}  OK")

        # cold start
        U = xp.zeros((lat['Ns'], lat['D'], 3, 3), dtype=xp.complex128)
        U[:] = xp.eye(3, dtype=xp.complex128)
        eps = 0.22

        # thermalize with adaptive eps
        t0 = time.time(); sweeps = 0
        for it in range(args.therm):
            pool = rotation_pool(eps, args.npool, pool_rng)
            a = metropolis_sweep(lat, U, beta, pool, parity_dev)
            if a < 0.35: eps *= 0.94
            elif a > 0.65: eps *= 1.06
            if (it + 1) % args.reunit == 0:
                U = reunitarize(U)
            sweeps += 1
        if USE_GPU: cp.cuda.runtime.deviceSynchronize()
        t_therm = time.time() - t0
        # unitarity gate
        UU = U @ dag(U)
        uni = float(xp.max(xp.abs(UU - xp.eye(3, dtype=xp.complex128))))
        assert uni < 1e-8, f'GATE FAIL: link unitarity drift {uni:.2e}'

        res = {'cfg': []}
        t1 = time.time()
        for c in range(args.ncfg):
            for _ in range(args.sep):
                pool = rotation_pool(eps, args.npool, pool_rng)
                a = metropolis_sweep(lat, U, beta, pool, parity_dev)
                if a < 0.35: eps *= 0.94
                elif a > 0.65: eps *= 1.06
                sweeps += 1
            U = reunitarize(U)
            spl = plaquette_field(lat, U)
            mean_plaq = float(1.0 - spl.mean())
            assert -0.05 < mean_plaq < 1.05, f'GATE FAIL: plaquette out of range {mean_plaq}'
            entry = {'cfg': c, 'plaq': mean_plaq}
            if not args.no_theta:
                for dl in deltas:
                    th, rp, rl, nD = theta_of(lat, spl, dl, Mmv, args.v0, gate_rng)
                    entry[f'theta_d{dl}'] = th
                    entry[f'rhoL_d{dl}']  = rl
                    entry[f'rhoP_d{dl}']  = rp
                    entry[f'nD_d{dl}']    = nD
            res['cfg'].append(entry)
        if USE_GPU: cp.cuda.runtime.deviceSynchronize()
        t_meas = time.time() - t1

        sps = sweeps / max(t_therm + t_meas, 1e-9)
        json.dump(res, open(os.path.join(args.out, f'results_{tag}.json'), 'w'), indent=1)
        meta = dict(L=args.L, beta=beta, therm=args.therm, ncfg=args.ncfg, sep=args.sep,
                    m2=args.m2, v0=args.v0, deltas=deltas, backend=BACKEND,
                    sweeps=sweeps, sweeps_per_sec=sps,
                    t_therm=t_therm, t_meas=t_meas, eps_final=eps)
        json.dump(meta, open(os.path.join(args.out, f'meta_{tag}.json'), 'w'), indent=1)

        # console summary
        plaqs = [e['plaq'] for e in res['cfg']]
        line = f"[{tag}] sweeps/s={sps:8.1f}  <plaq>={np.mean(plaqs):.4f}" if plaqs \
               else f"[{tag}] sweeps/s={sps:8.1f}  (therm only)"
        if not args.no_theta and plaqs:
            for dl in deltas:
                ths = [e[f'theta_d{dl}'] for e in res['cfg']]
                line += f"  | d={dl}: theta_max={max(ths):.4f} theta_p50={np.median(ths):.4f}"
        print(line)
        summary[tag] = dict(sweeps_per_sec=sps,
                            mean_plaq=(float(np.mean(plaqs)) if plaqs else None))

    print("\nDONE.  GPU output is FLOAT SCREENING -- certify chosen (L,beta,delta) "
          "points exactly on CPU (M2 machinery).")
    return summary

def selftest():
    print("=" * 70)
    print("SELF-TEST  (tiny; validates the full pipeline + every hard gate)")
    print("=" * 70)
    ns = argparse.Namespace(L=4, betas='6.0', deltas='0.9', therm=30, ncfg=2, sep=2,
                            m2=0.5, v0=1.0, npool=64, reunit=10, seed=20260614,
                            out='op12_gpu_selftest', no_theta=False)
    s = run(ns)
    print("\nSELF-TEST PASS: ran end-to-end, all gates held, theta finite.")
    return s

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description="GPU OP-12 theta screening (A100).")
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--L', type=int, default=8)
    ap.add_argument('--betas', type=str, default='5.6,6.0,6.4,6.8,7.2')
    ap.add_argument('--deltas', type=str, default='0.7,0.9,1.1')
    ap.add_argument('--therm', type=int, default=200)
    ap.add_argument('--ncfg', type=int, default=40)
    ap.add_argument('--sep', type=int, default=5)
    ap.add_argument('--m2', type=float, default=0.5)
    ap.add_argument('--v0', type=float, default=1.0)
    ap.add_argument('--npool', type=int, default=96)
    ap.add_argument('--reunit', type=int, default=25, help='reunitarize every N sweeps')
    ap.add_argument('--seed', type=int, default=20260614)
    ap.add_argument('--out', type=str, default='op12_gpu_out')
    ap.add_argument('--no-theta', dest='no_theta', action='store_true',
                    help='generate configs only (pure sampler benchmark)')
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        run(args)
