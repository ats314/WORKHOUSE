#!/usr/bin/env python3
# ENGINE_OP1_m2_pair_certificates.py - M2 of PLAN_OP1_unif_closure.md (June 12, 2026).
# Exact pair-level deterministic certificates for theta < 1:
#   tr K^2 = v0^2 sum_{b,b' in D} G_P(b,b')^2   with G_P = P M^{-1} P fixed.
# By translation invariance G_P((s,mu),(s',mu')) = T[mu][4*sidx(c'-c mod L)+mu'],
# so 4 projected solves per (L,beta) give the WHOLE kernel; per-config certificates
# are then exact lookups (no estimate, no probability). HARD GATES:
#   GATE-TR    translation lookup == direct solve column at a random source link
#   GATE-NSTAR T_full from tensor == CERT_OP1_kernel_consts.json (independent computation)
#   GATE-VALID certificate >= measured theta on every config (HS dominates op)
# Usage: python3 ENGINE_OP1_m2_pair_certificates.py L beta1 [beta2 ...]
import sys, json, os, math, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spla
import importlib.util
sys.argv, argv = ['m2', '--deadline', '0.0'], sys.argv
spec = importlib.util.spec_from_file_location('r', 'ENGINE_OP1_op12_runner.py')
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
M2C, V0 = 0.5, 1.0
os.makedirs('m2_kernel', exist_ok=True)

def tensor(L, beta):
    f = f'm2_kernel/tensor_L{L}_b{beta}.npz'
    lat = R.lattice(L)
    if os.path.exists(f):
        return np.load(f)['T'], lat
    Mop = (M2C*sp.eye(lat['Nl']) + (beta/6.0)*lat['L1up']).tocsr()
    T = np.zeros((4, lat['Nl']))
    for mu in range(4):
        e = np.zeros(lat['Nl']); e[mu] = 1.0           # link (site 0, mu)
        y = R.proj_P(lat, e)
        z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=60000)
        assert info == 0, 'GATE FAIL: CG tensor'
        T[mu] = R.proj_P(lat, z)
    np.savez_compressed(f, T=T)
    # GATE-TR: direct column at random source link vs lookup
    rng = np.random.default_rng(7)
    s = int(rng.integers(1, lat['Ns'])); mu = int(rng.integers(4))
    e = np.zeros(lat['Nl']); e[4*s+mu] = 1.0
    z, info = spla.cg(Mop, R.proj_P(lat, e), rtol=1e-12, atol=0, maxiter=60000)
    col = R.proj_P(lat, z); cs = lat_coords(L)
    bp = rng.integers(0, lat['Nl'], 200)
    lk = np.array([lookup(T, L, cs, 4*s+mu, int(b)) for b in bp])
    err = float(np.abs(lk - col[bp]).max())
    assert err < 1e-8, f'GATE FAIL: GATE-TR err={err}'
    print(f'GATE-TR pass (L={L} b={beta}, err={err:.2e})')
    return T, lat

_cc = {}
def lat_coords(L):
    if L not in _cc:
        s = np.arange(L**4)
        _cc[L] = np.stack([s % L, (s//L) % L, (s//L**2) % L, (s//L**3) % L], 1)
    return _cc[L]

def lookup(T, L, cs, b, bp):
    s, mu = b//4, b % 4; sp_, mup = bp//4, bp % 4
    d = (cs[sp_] - cs[s]) % L
    return T[mu][4*(((d[3]*L + d[2])*L + d[1])*L + d[0]) + mup]

def cert_exact(T, L, D):
    cs = lat_coords(L); tot = 0.0
    sD, muD = D//4, D % 4
    for mu in range(4):                       # group source links by orientation
        idx = np.where(muD == mu)[0]
        if len(idx) == 0: continue
        Tm = T[mu]
        for i0 in range(0, len(idx), 128):    # chunk rows
            ii = idx[i0:i0+128]
            d = (cs[sD][None, :, :] - cs[sD[ii]][:, None, :]) % L   # (chunk,|D|,4)
            si = ((d[..., 3]*L + d[..., 2])*L + d[..., 1])*L + d[..., 0]
            tot += float((Tm[4*si + muD[None, :]]**2).sum())
    return V0*math.sqrt(tot)

if __name__ == '__main__':
    L = int(argv[1]); betas = [float(b) for b in argv[2:]]
    kc = {(r['L'], r['beta']): r for r in json.load(open('CERT_OP1_kernel_consts.json'))['tables']} \
         if os.path.exists('CERT_OP1_kernel_consts.json') else {}
    out = []
    for beta in betas:
        t0 = time.time(); T, lat = tensor(L, beta)
        Tf = float((T**2).sum(1).max())
        if (L, beta) in kc:
            ref = kc[(L, beta)]['T_full_max']
            assert abs(Tf-ref) <= 1e-6*ref, f'GATE FAIL: GATE-NSTAR {Tf} vs {ref}'
            print(f'GATE-NSTAR pass (L={L} b={beta}: T_full={Tf:.6f})')
        row = {'L': L, 'beta': beta, 'T_full': Tf, 'Nstar': int(1/(V0**2*Tf)), 'configs': []}
        # stored final state, all deltas
        job = dict(L=L, beta=beta, therm=120 if L == 4 else 100,
                   ncfg=20 if L == 4 else 12, sep=4)
        latt, U, meta, res, rng = R.load_job(job)
        spl = R.plaq_field(lat, U)
        Mop = (M2C*sp.eye(lat['Nl']) + (beta/6.0)*lat['L1up']).tocsr()
        for dl in (0.7, 0.9, 1.1):
            bad = spl > dl
            D = np.unique(lat['plinks'][bad].ravel()) if bad.any() else np.array([], int)
            if len(D) == 0:
                row['configs'].append({'delta': dl, 'nD': 0, 'cert': 0.0, 'theta': 0.0,
                                       'certified': True}); continue
            th, _, _, _ = R.theta_of(lat, spl, dl, Mop, rng)
            c = cert_exact(T, L, D)
            assert c >= th - 1e-6, f'GATE FAIL: GATE-VALID cert {c} < theta {th}'
            row['configs'].append({'delta': dl, 'nD': int(len(D)), 'cert': c,
                                   'theta': th, 'certified': bool(c < 1.0),
                                   'count_cert_NStar': bool(len(D) <= row['Nstar'])})
            print(f"  L={L} b={beta} d={dl}: |D|={len(D):4d} cert={c:.4f} "
                  f"theta={th:.4f} {'CERT' if c < 1 else 'no'} "
                  f"(count-only: {'CERT' if len(D) <= row['Nstar'] else 'no'})")
        out.append(row); print(f'  [{time.time()-t0:.0f}s]')
    fn = f'm2_certs_L{L}.json'
    old = json.load(open(fn)) if os.path.exists(fn) else []
    json.dump(old + out, open(fn, 'w'), indent=1)
    print('GATE-VALID pass (all configs); wrote', fn)
