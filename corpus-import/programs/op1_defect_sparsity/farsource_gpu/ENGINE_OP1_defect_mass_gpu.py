#!/usr/bin/env python3
"""
ENGINE_OP1_defect_mass_gpu.py — SU(2) defect/source-field mass m_J(beta).  (GPU-optimized rewrite.)

Fixes vs the earlier version:
  * heat-bath vMF sampler is now a FIXED-ROUND, fully vectorized rejection with NO
    per-iteration GPU->host sync (the old `while not all(done)` loop synced every
    iteration -> very slow on GPU). This is the main speedup.
  * LIVE PROGRESS: prints per-sweep timing + ETA during thermalization and measurement,
    so you can see it is alive and gauge throughput immediately.
  * a --quick / quick=True calibration mode (small L, few sweeps) to measure sweeps/sec
    before committing to a long run.

PHYSICS (the Z.B firewall question): J(p,r)=log(<X_p X_r>/<X_p><X_r>) is the single-source
log-amplification; m_J = mass of the defect field. Z.B holds iff m_J stays > 0 uniformly
along the AF trajectory; beta grows as a->0 and m_J grows, so the binding case is the COARSE
(small-beta) end. We measure the connected defect correlation C(d)=<X0 Xd>-<X>^2 (FFT) and
read m_J from the effective mass m_eff(d)=log(C(d)/C(d+1)) with jackknife errors.

COLAB (A100 GPU runtime):
    %run ENGINE_OP1_defect_mass_gpu.py
    run(quick=True, device='gpu')          # ~seconds: prints sweeps/sec so you can plan
    out = run(L=16, betas=[2.2,2.5,2.8,3.1,3.4,3.7,4.0], thetas=[0.9,1.2,1.5],
              nconfigs=120, nthermal=200, nsep=10, device='gpu', out='defect_mass_L16.json')
    from google.colab import files; files.download('defect_mass_L16.json')
Start at L=16 to calibrate; go to L=24 only once you know the per-sweep time.
"""
import json, math, time, sys
import numpy as np


def _backend(device):
    if device == 'gpu':
        try:
            import cupy as cp
            return cp, True
        except Exception as e:
            print(f'[warn] CuPy unavailable ({e}); running on NumPy/CPU', flush=True)
    return np, False


def run(L=16, betas=(2.2, 2.5, 2.8, 3.1, 3.4, 3.7, 4.0), thetas=(0.9, 1.2, 1.5),
        nconfigs=120, nthermal=200, nsep=10, seed=20260613, device='cpu',
        out='CERT_OP1_defect_mass.json', rounds=24, log_every=25, quick=False, selftest=False):
    """Measure m_J(beta). Writes JSON to `out`, returns the results dict."""
    betas, thetas = list(betas), list(thetas)
    if quick:
        L, betas, thetas, nconfigs, nthermal, nsep = 16, [2.6, 3.4], [1.0], 6, 40, 5
    if selftest:
        L, betas, thetas, nconfigs, nthermal, nsep, device = 8, [2.3], [0.8], 50, 80, 3, 'cpu'

    xp, on_gpu = _backend(device)
    D, V = 4, L ** 4
    rng = xp.random.default_rng(seed)
    t0, gates = time.time(), {}
    to_np = (lambda a: a.get()) if on_gpu else (lambda a: np.asarray(a))

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

    a, b, c = (rng.standard_normal((6, 4)) for _ in range(3))
    gates['G-BK'] = float(xp.max(xp.abs(qmul(qmul(a, b), c) - qmul(a, qmul(b, c)))))
    assert gates['G-BK'] < 1e-10, f"G-BK {gates['G-BK']}"

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

    def rbeta(shape, n):                         # Beta(shape,shape) via two Gammas (CuPy-safe)
        g1 = rng.standard_gamma(shape, n); g2 = rng.standard_gamma(shape, n)
        return g1 / (g1 + g2)

    def vmf(meandir, kappa):
        """vMF_4 heat-bath sample. Fixed-round vectorized rejection, NO host sync inside."""
        n, pm = meandir.shape[0], 3
        big = kappa >= 1e-8
        kap = xp.where(big, kappa, 1.0)          # avoid div-by-zero in the formulas
        bb = (-2*kap + xp.sqrt(4*kap*kap + pm*pm)) / pm
        x0 = (1 - bb) / (1 + bb)
        cc = kap * x0 + pm * xp.log(xp.clip(1 - x0*x0, 1e-300, None))
        w = xp.ones(n); done = ~big              # tiny-kappa handled isotropically below
        for _ in range(rounds):                  # fixed rounds; ~1-(1-p)^rounds accepted
            z = rbeta(pm/2.0, n)
            wc = (1 - (1+bb)*z) / (1 - (1-bb)*z)
            acc = (kap*wc + pm*xp.log(xp.clip(1 - x0*wc, 1e-300, None)) - cc
                   >= xp.log(rng.random(n))) & (~done)
            w = xp.where(acc, wc, w); done = done | acc
        g = rng.standard_normal((n, 4))
        g = g - xp.sum(g*meandir, axis=1, keepdims=True)*meandir
        g = g / xp.linalg.norm(g, axis=1, keepdims=True)
        out = w[:, None]*meandir + xp.sqrt(xp.clip(1 - w*w, 0, None))[:, None]*g
        iso = ~big                               # isotropic for (rare) tiny kappa
        if bool(xp.any(iso)):
            v = rng.standard_normal((n, 4)); v = v / xp.linalg.norm(v, axis=1, keepdims=True)
            out = xp.where(iso[:, None], v, out)
        return out

    parity = (xp.indices((L,)*4).sum(axis=0)) % 2

    def sweep(U, beta):
        for mu in range(D):
            for p in (0, 1):
                H = staple(U, mu); hn = xp.linalg.norm(H, axis=-1)
                m = (parity == p) & (hn > 1e-12)
                if bool(xp.any(m)):
                    U[..., mu, :][m] = vmf(H[m] / hn[m][:, None], beta * hn[m])
        return U

    def plaq_w(U, mu, nu):
        Umu, Unu = U[..., mu, :], U[..., nu, :]
        return qmul3(Umu, xp.roll(Unu, -1, axis=mu),
                     qmul(qconj(xp.roll(Umu, -1, axis=nu)), qconj(Unu)))[..., 0]

    def mean_plaq(U):
        t = c = 0
        for mu in range(D):
            for nu in range(mu+1, D):
                w = plaq_w(U, mu, nu); t += float(xp.sum(w)); c += w.size
        return t / c

    Xr = (rng.random((L,)*4) < 0.3).astype(float)
    Cf = xp.fft.ifftn(xp.abs(xp.fft.fftn(Xr))**2).real / V
    gates['G-FFT'] = abs(float(Cf[0, 0, 1, 0]) - float(xp.mean(Xr * xp.roll(Xr, -1, axis=2))))
    assert gates['G-FFT'] < 1e-9, f"G-FFT {gates['G-FFT']}"

    dmax = L // 2
    res = {'meta': {'L': L, 'V': V, 'betas': betas, 'thetas': thetas, 'nconfigs': nconfigs,
                    'nthermal': nthermal, 'nsep': nsep, 'seed': seed, 'on_gpu': on_gpu,
                    'rounds': rounds,
                    'observable': 'm_eff(d)=log(Cconn(d)/Cconn(d+1)); m_J=defect-field mass'},
           'gates': gates, 'runs': []}
    print(f'[setup] L={L} V={V} device={"GPU" if on_gpu else "CPU"} '
          f'betas={betas} thetas={thetas}', flush=True)
    any_reliable = False

    for beta in betas:
        U = xp.zeros((L,)*4 + (D, 4)); U[..., 0] = 1.0
        # --- thermalize with live progress + a 1-sweep benchmark ---
        ts = time.time()
        for k in range(nthermal):
            U = sweep(U, beta)
            if on_gpu:
                try:
                    xp.cuda.Stream.null.synchronize()
                except Exception:
                    pass
            if k == 0:
                dt = time.time() - ts
                tot = (nthermal + nconfigs*nsep) * len(betas)
                print(f'[beta={beta:.2f}] sweep time ~{dt:.3f}s  '
                      f'=> ~{dt*(nthermal+nconfigs*nsep):.0f}s/beta, ~{dt*tot/60:.1f} min total',
                      flush=True)
            elif (k+1) % log_every == 0:
                sps = (k+1)/(time.time()-ts)
                print(f'[beta={beta:.2f}] thermalize {k+1}/{nthermal}  '
                      f'({sps:.2f} sweeps/s, {time.time()-ts:.0f}s)', flush=True)
        # --- measure ---
        plaqs, corr, xmean = [], {th: [] for th in thetas}, {th: [] for th in thetas}
        tm = time.time()
        for ci in range(nconfigs):
            for _ in range(nsep):
                U = sweep(U, beta)
            plaqs.append(mean_plaq(U))
            ang = xp.arccos(xp.clip(plaq_w(U, 0, 1), -1.0, 1.0))
            for th in thetas:
                X = (ang > th).astype(float); xmean[th].append(float(xp.mean(X)))
                C = xp.fft.ifftn(xp.abs(xp.fft.fftn(X))**2).real / V
                corr[th].append([0.5*(float(C[0, 0, d, 0]) + float(C[0, 0, 0, d]))
                                 for d in range(dmax+1)])
            if (ci+1) % max(1, nconfigs//5) == 0:
                print(f'[beta={beta:.2f}] measured {ci+1}/{nconfigs} configs '
                      f'({time.time()-tm:.0f}s)', flush=True)
        pa = to_np(xp.array(plaqs)); pac = pa - pa.mean()
        ac1 = float((pac[:-1] @ pac[1:]) / (pac @ pac)) if (pac @ pac) > 0 else 0.0
        for th in thetas:
            Xm = np.array(xmean[th]); Call = np.array(corr[th]); Xmean = float(Xm.mean())
            Cconn = Call.mean(axis=0) - Xmean**2
            G = (Cconn + Xmean**2) / Xmean**2 if Xmean > 0 else Cconn*np.nan
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
                    jk[d] = float(math.sqrt((len(vals)-1)/len(vals)*((vals-vals.mean())**2).sum()))
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
        summ = '  '.join('th%.1f:Xm=%.3f mJ=%s' % (
            r['theta'], r['X_mean'], ('%.2f' % r['m_J']) if r['m_J'] is not None else 'NA')
            for r in res['runs'] if r['beta'] == beta)
        print(f'[beta={beta:.2f}] DONE plaq={pa.mean():.4f} autocorr1={ac1:.2f}  {summ}', flush=True)

    gates['G-DECORR_ac1_max'] = max(r['autocorr_lag1'] for r in res['runs'])
    gates['G-HB_plaq_first'] = res['runs'][0]['plaquette_mean']
    res['gates'] = gates
    res['meta']['walltime_s'] = time.time() - t0
    with open(out, 'w') as f:
        json.dump(res, f, indent=1)
    if selftest:
        assert any_reliable, 'selftest: no reliable effective mass'
        print('SELFTEST_OK   G-BK %.1e  G-FFT %.1e' % (gates['G-BK'], gates['G-FFT']), flush=True)
    print('DONE -> %s   (%.1f s total, %s)' % (out, res['meta']['walltime_s'],
                                               'GPU' if on_gpu else 'CPU'), flush=True)
    return res


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='SU(2) defect-field mass m_J(beta)')
    ap.add_argument('--L', type=int, default=16)
    ap.add_argument('--betas', type=float, nargs='+', default=[2.2, 2.5, 2.8, 3.1, 3.4, 3.7, 4.0])
    ap.add_argument('--thetas', type=float, nargs='+', default=[0.9, 1.2, 1.5])
    ap.add_argument('--nconfigs', type=int, default=120)
    ap.add_argument('--nthermal', type=int, default=200)
    ap.add_argument('--nsep', type=int, default=10)
    ap.add_argument('--seed', type=int, default=20260613)
    ap.add_argument('--device', choices=['cpu', 'gpu'], default='cpu')
    ap.add_argument('--out', type=str, default='CERT_OP1_defect_mass.json')
    ap.add_argument('--rounds', type=int, default=24)
    ap.add_argument('--quick', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    args, _ = ap.parse_known_args()      # tolerate Jupyter's injected -f kernel.json
    run(L=args.L, betas=args.betas, thetas=args.thetas, nconfigs=args.nconfigs,
        nthermal=args.nthermal, nsep=args.nsep, seed=args.seed, device=args.device,
        out=args.out, rounds=args.rounds, quick=args.quick, selftest=args.selftest)
