#!/usr/bin/env python3
"""
ENGINE_OP1_defect_mass.py — measure the defect/source-field mass m_J of SU(2) lattice gauge theory.

WHY (the Z.B question, OP-1 far-source firewall)
-------------------------------------------------
The firewall reduction needs the source-source interaction to decay exponentially:
        J(p, r) <= C_J * exp(-m_J * dist(p, r)).
The single-source log-amplification is exactly the log normalized pair-correlation of the
defect-indicator field X:
        J(p, r) = log( <X_p X_r> / (<X_p> <X_r>) ),
so m_J IS the mass of the defect field. The firewall (Z.B) holds iff m_J stays bounded
away from 0 UNIFORMLY along the asymptotic-freedom trajectory. Along that trajectory beta
grows as a -> 0 and the field gets more ordered (m_J grows), so the binding/hardest case is
the COARSE, small-beta end. => scan beta downward and watch whether m_J(beta) collapses.

WHAT IT DOES
------------
SU(2) Wilson exact heat-bath (quaternion checkerboard) on an L^4 lattice. For each
thermalized, decorrelated configuration it builds the (0,1)-plaquette defect field
        X(x) = 1 if  arccos(½ Re Tr U_p(x)) > theta   else 0,
computes the connected correlation  C(d) = <X(0)X(d)> - <X>^2  (FFT, all pairs,
translation-averaged, along the two axes transverse to the plaquette plane), and reads the
mass from the effective mass  m_eff(d) = log( C(d) / C(d+1) )  with a jackknife error.
m_J is reported as the first reliable m_eff; the full m_eff(d) array lets you read a plateau.

USAGE
-----
Colab / Jupyter (GPU runtime, A100):
    %run ENGINE_OP1_defect_mass.py
    run(selftest=True)                       # ~10 s sanity check
    run(L=24, betas=[2.2,2.4,2.6,2.8,3.0,3.5,4.0], thetas=[0.9,1.2,1.5],
        nconfigs=200, nthermal=400, nsep=20, device='gpu', out='defect_mass_L24.json')
    from google.colab import files; files.download('defect_mass_L24.json')

Command line:
    python3 ENGINE_OP1_defect_mass.py --L 24 --betas 2.2 2.6 3.0 3.5 4.0 --device gpu --out run.json

GPU is auto-detected via CuPy when device='gpu'; if CuPy is missing it falls back to NumPy
and says so. Send the output JSON back for fitting/plotting of m_J(beta).
"""
import json, math, time
import numpy as np


# ---------------------------------------------------------------- backend
def _backend(device):
    """Return (array_module, on_gpu). device='gpu' tries CuPy, else NumPy."""
    if device == 'gpu':
        try:
            import cupy as cp
            return cp, True
        except Exception as e:
            print(f'[warn] CuPy unavailable ({e}); running on NumPy/CPU')
    return np, False


# ---------------------------------------------------------------- main entry
def run(L=16, betas=(2.4, 2.8, 3.2, 3.6, 4.0), thetas=(0.9, 1.2, 1.5),
        nconfigs=120, nthermal=400, nsep=20, seed=20260613,
        device='cpu', out='CERT_OP1_defect_mass.json', selftest=False):
    """Run the measurement. Returns the results dict and writes it to `out` as JSON."""
    betas, thetas = list(betas), list(thetas)
    if selftest:
        L, betas, thetas = 8, [2.3], [0.8]
        nconfigs, nthermal, nsep, device = 50, 80, 3, 'cpu'

    xp, on_gpu = _backend(device)
    D, V = 4, L ** 4
    rng = xp.random.default_rng(seed)
    t0, gates = time.time(), {}
    to_np = (lambda a: a.get()) if on_gpu else (lambda a: np.asarray(a))

    # ---- quaternion algebra (SU(2) ~ unit quaternions) ----
    def qmul(A, B):
        a0, a1, a2, a3 = A[..., 0], A[..., 1], A[..., 2], A[..., 3]
        b0, b1, b2, b3 = B[..., 0], B[..., 1], B[..., 2], B[..., 3]
        return xp.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                         a0*b1 + a1*b0 + a2*b3 - a3*b2,
                         a0*b2 - a1*b3 + a2*b0 + a3*b1,
                         a0*b3 + a1*b2 - a2*b1 + a3*b0], axis=-1)

    def qconj(A):
        o = A.copy(); o[..., 1:] *= -1.0; return o

    def qmul3(A, B, C):
        return qmul(qmul(A, B), C)

    # gate G-BK: backend associativity
    a, b, c = (rng.standard_normal((6, 4)) for _ in range(3))
    gates['G-BK'] = float(xp.max(xp.abs(qmul(qmul(a, b), c) - qmul(a, qmul(b, c)))))
    assert gates['G-BK'] < 1e-10, f"G-BK {gates['G-BK']}"

    # ---- heat-bath (validated su2_hb_v3 checkerboard) ----
    def staple(U, mu):
        Umu = U[..., mu, :]; H = xp.zeros(Umu.shape)
        for nu in range(D):
            if nu == mu:
                continue
            Unu = U[..., nu, :]
            fwd = qconj(qmul3(xp.roll(Unu, -1, axis=mu),
                              qconj(xp.roll(Umu, -1, axis=nu)), qconj(Unu)))
            Unu_m = xp.roll(Unu, +1, axis=nu); Umu_m = xp.roll(Umu, +1, axis=nu)
            bwd = qmul3(qconj(Unu_m), Umu_m, xp.roll(Unu_m, -1, axis=mu))
            H = H + fwd + bwd
        return H

    def rbeta(shape, size):                       # Beta(shape,shape) via two Gammas (CuPy-safe)
        g1 = rng.standard_gamma(shape, size); g2 = rng.standard_gamma(shape, size)
        return g1 / (g1 + g2)

    def vmf(meandir, kappa):                       # vMF_4 sample (Wood 1994), vectorized
        n, pm = meandir.shape[0], 3
        o = xp.zeros((n, 4)); small = kappa < 1e-8
        if bool(xp.any(small)):
            v = rng.standard_normal((int(xp.sum(small)), 4))
            o[small] = v / xp.linalg.norm(v, axis=1, keepdims=True)
        big = ~small
        if bool(xp.any(big)):
            kp, M = kappa[big], meandir[big]; nb = kp.shape[0]
            bb = (-2*kp + xp.sqrt(4*kp*kp + pm*pm)) / pm
            x0 = (1 - bb) / (1 + bb); cc = kp*x0 + pm*xp.log(1 - x0*x0)
            w = xp.empty(nb); done = xp.zeros(nb, bool); it = 0
            while not bool(xp.all(done)) and it < 20000:
                it += 1; idx = xp.where(~done)[0]
                z = rbeta(pm/2.0, idx.shape[0])
                wc = (1 - (1+bb[idx])*z) / (1 - (1-bb[idx])*z)
                acc = kp[idx]*wc + pm*xp.log(xp.clip(1 - x0[idx]*wc, 1e-300, None)) - cc[idx] \
                      >= xp.log(rng.random(idx.shape[0]))
                ai = idx[acc]; w[ai] = wc[acc]; done[ai] = True
            g = rng.standard_normal((nb, 4)); g = g - xp.sum(g*M, axis=1, keepdims=True)*M
            g /= xp.linalg.norm(g, axis=1, keepdims=True)
            o[big] = w[:, None]*M + xp.sqrt(xp.clip(1 - w*w, 0, None))[:, None]*g
        return o

    parity = (xp.indices((L,)*4).sum(axis=0)) % 2

    def sweep(U, beta):
        for mu in range(D):
            for p in (0, 1):                       # update even then odd; recompute staple between
                H = staple(U, mu); hn = xp.linalg.norm(H, axis=-1)
                m = (parity == p) & (hn > 1e-12)
                if bool(xp.any(m)):
                    U[..., mu, :][m] = vmf(H[m] / hn[m][:, None], beta * hn[m])
        return U

    def plaq_w(U, mu, nu):                          # ½ Re Tr U_p  in [-1,1]
        Umu, Unu = U[..., mu, :], U[..., nu, :]
        return qmul3(Umu, xp.roll(Unu, -1, axis=mu),
                     qmul(qconj(xp.roll(Umu, -1, axis=nu)), qconj(Unu)))[..., 0]

    def mean_plaq(U):
        t = c = 0
        for mu in range(D):
            for nu in range(mu+1, D):
                w = plaq_w(U, mu, nu); t += float(xp.sum(w)); c += w.size
        return t / c

    # gate G-FFT: FFT 2-point == direct
    Xr = (rng.random((L,)*4) < 0.3).astype(float)
    Cf = xp.fft.ifftn(xp.abs(xp.fft.fftn(Xr))**2).real / V
    gates['G-FFT'] = abs(float(Cf[0, 0, 1, 0]) - float(xp.mean(Xr * xp.roll(Xr, -1, axis=2))))
    assert gates['G-FFT'] < 1e-9, f"G-FFT {gates['G-FFT']}"

    dmax = L // 2
    res = {'meta': {'L': L, 'V': V, 'betas': betas, 'thetas': thetas, 'nconfigs': nconfigs,
                    'nthermal': nthermal, 'nsep': nsep, 'seed': seed, 'on_gpu': on_gpu,
                    'observable': 'm_eff(d)=log(Cconn(d)/Cconn(d+1)); m_J = defect-field mass'},
           'gates': gates, 'runs': []}
    any_reliable = False

    for beta in betas:
        U = xp.zeros((L,)*4 + (D, 4)); U[..., 0] = 1.0
        for _ in range(nthermal):
            U = sweep(U, beta)
        plaqs, corr, xmean = [], {th: [] for th in thetas}, {th: [] for th in thetas}
        for _ in range(nconfigs):
            for _ in range(nsep):
                U = sweep(U, beta)
            plaqs.append(mean_plaq(U))
            ang = xp.arccos(xp.clip(plaq_w(U, 0, 1), -1.0, 1.0))
            for th in thetas:
                X = (ang > th).astype(float); xmean[th].append(float(xp.mean(X)))
                C = xp.fft.ifftn(xp.abs(xp.fft.fftn(X))**2).real / V
                corr[th].append([0.5*(float(C[0, 0, d, 0]) + float(C[0, 0, 0, d]))
                                 for d in range(dmax+1)])
        pa = to_np(xp.array(plaqs)); pac = pa - pa.mean()
        ac1 = float((pac[:-1] @ pac[1:]) / (pac @ pac)) if (pac @ pac) > 0 else 0.0

        for th in thetas:
            Xm = np.array(xmean[th]); Call = np.array(corr[th]); Xmean = float(Xm.mean())
            Cmean = Call.mean(axis=0); Cconn = Cmean - Xmean**2
            G = Cmean / Xmean**2 if Xmean > 0 else Cmean * np.nan
            meff = [math.log(Cconn[d]/Cconn[d+1]) if (Cconn[d] > 0 and Cconn[d+1] > 0) else None
                    for d in range(dmax)]
            jk = {}
            for d in range(dmax):
                vals = []
                for k in range(len(Xm)):
                    Cm = np.delete(Call, k, axis=0).mean(axis=0) - np.delete(Xm, k).mean()**2
                    if Cm[d] > 0 and Cm[d+1] > 0:
                        vals.append(math.log(Cm[d]/Cm[d+1]))
                if len(vals) > 2:
                    vals = np.array(vals)
                    jk[d] = float(math.sqrt((len(vals)-1)/len(vals) * ((vals - vals.mean())**2).sum()))
            reliable = [d for d in range(dmax) if meff[d] is not None and Cconn[d] > 1e-6]
            mJ = meff[reliable[0]] if reliable else None
            mJe = jk.get(reliable[0]) if reliable else None
            any_reliable = any_reliable or bool(reliable)
            res['runs'].append({'beta': beta, 'theta': th, 'plaquette_mean': float(pa.mean()),
                                'autocorr_lag1': ac1, 'X_mean': Xmean,
                                'Cconn': [float(x) for x in Cconn],
                                'G_normpair': [float(x) for x in G], 'm_eff': meff,
                                'm_eff_err': {int(k): v for k, v in jk.items()},
                                'm_J': mJ, 'm_J_err': mJe,
                                'corr_len_xi': (1.0/mJ if (mJ and mJ > 0) else None),
                                'n_reliable_d': len(reliable)})
        summ = '  '.join(
            'th%.1f:Xm=%.3f mJ=%s' % (
                th, [r for r in res['runs'] if r['beta'] == beta and r['theta'] == th][0]['X_mean'],
                ('%.2f' % [r for r in res['runs'] if r['beta'] == beta and r['theta'] == th][0]['m_J'])
                if [r for r in res['runs'] if r['beta'] == beta and r['theta'] == th][0]['m_J'] is not None
                else 'NA')
            for th in thetas)
        print('[beta=%.2f plaq=%.4f autocorr1=%.2f]  %s' % (beta, pa.mean(), ac1, summ))

    gates['G-DECORR_ac1_max'] = max(r['autocorr_lag1'] for r in res['runs'])
    gates['G-HB_plaq_first'] = res['runs'][0]['plaquette_mean']
    res['gates'] = gates
    res['meta']['walltime_s'] = time.time() - t0
    with open(out, 'w') as f:
        json.dump(res, f, indent=1)
    if selftest:
        assert any_reliable, 'selftest: no reliable effective mass produced'
        print('SELFTEST_OK   G-BK %.1e  G-FFT %.1e' % (gates['G-BK'], gates['G-FFT']))
    print('DONE -> %s   (%.1f s, %s)' % (out, res['meta']['walltime_s'], 'GPU' if on_gpu else 'CPU'))
    return res


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='SU(2) defect-field mass m_J(beta)')
    ap.add_argument('--L', type=int, default=16)
    ap.add_argument('--betas', type=float, nargs='+', default=[2.4, 2.8, 3.2, 3.6, 4.0])
    ap.add_argument('--thetas', type=float, nargs='+', default=[0.9, 1.2, 1.5])
    ap.add_argument('--nconfigs', type=int, default=120)
    ap.add_argument('--nthermal', type=int, default=400)
    ap.add_argument('--nsep', type=int, default=20)
    ap.add_argument('--seed', type=int, default=20260613)
    ap.add_argument('--device', choices=['cpu', 'gpu'], default='cpu')
    ap.add_argument('--out', type=str, default='CERT_OP1_defect_mass.json')
    ap.add_argument('--selftest', action='store_true')
    args, _ = ap.parse_known_args()      # tolerate Jupyter's injected -f kernel.json
    run(L=args.L, betas=args.betas, thetas=args.thetas, nconfigs=args.nconfigs,
        nthermal=args.nthermal, nsep=args.nsep, seed=args.seed, device=args.device,
        out=args.out, selftest=args.selftest)
