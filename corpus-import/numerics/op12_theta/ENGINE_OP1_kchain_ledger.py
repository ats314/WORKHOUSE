#!/usr/bin/env python3
# ENGINE_OP1_kchain_ledger.py - slack decomposition of the OP-7 deterministic chain
# against measured Birman-Schwinger quantities (June 11, 2026). Diagnostics
# only; no claim beyond the printed numbers. See ENGINE_OP1_op12_runner.py for the
# operator conventions (m0^2=0.5, alpha_W=beta/6, v0=1, plaquette-seeded D).
import json, math, time, sys
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import importlib.util

sys.argv = ['kchain', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('r', 'ENGINE_OP1_op12_runner.py')
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)

M2, V0 = 0.5, 1.0
CASES = [(4, 5.6, [0.7, 0.9]), (4, 6.4, [0.9]), (4, 7.2, [0.9])]
out = {'meta': {'m2': M2, 'v0': V0, 'alpha_W': 'beta/6', 'c_E': 8, 'D_E': 18,
        'theta_def': 'v0*lmax(Pi_D P M^-1 P Pi_D)'}, 'cases': []}

for L, beta, deltas in CASES:
    lat = R.lattice(L)
    job = dict(L=L, beta=beta, therm=120 if L == 4 else 100,
               ncfg=20 if L == 4 else 12, sep=4)
    latt, U, meta, res, rng = R.load_job(job)
    alpha = beta / 6.0
    Mop = (M2 * sp.eye(lat['Nl']) + alpha * lat['L1up']).tocsr()
    spl = R.plaq_field(lat, U)

    # (1) measured M^{-1} column decay vs Combes-Thomas q
    adj = ((abs(lat['d1']).T @ abs(lat['d1'])) > 0).astype(np.int8)
    adj.setdiag(0); adj.eliminate_zeros()
    q_CT = 1.0 / (1.0 + M2 / (2 * alpha * 18.0))
    probe = int(rng.integers(lat['Nl']))
    dist = np.full(lat['Nl'], -1); dist[probe] = 0
    frontier = [probe]; d = 0
    while frontier:
        d += 1; nxt = []
        for b in frontier:
            for b2 in adj[b].indices:
                if dist[b2] < 0:
                    dist[b2] = d; nxt.append(b2)
        frontier = nxt
    e = np.zeros(lat['Nl']); e[probe] = 1.0
    z, info = spla.cg(Mop, e, rtol=1e-12, atol=0, maxiter=30000)
    assert info == 0
    shells, meds = [], []
    for dd in range(1, int(dist.max()) + 1):
        m_ = np.abs(z[dist == dd])
        if len(m_) > 0 and np.median(m_) > 1e-14:
            shells.append(dd); meds.append(float(np.median(m_)))
    ratios = [meds[i+1]/meds[i] for i in range(len(meds)-1)]
    ratios2 = [r for r in ratios if r < 1.0] or ratios
    q_meas = float(np.exp(np.mean(np.log(ratios2)))) if ratios2 else float('nan')
    case = {'L': L, 'beta': beta, 'plaq': float(1 - spl.mean()), 'q_CT': q_CT,
            'q_meas_median_shell_ratio': q_meas,
            'decay_profile': {'shells': shells, 'medians': meds}, 'deltas': {}}

    # (2)-(4) per delta
    for dl in deltas:
        bad = spl > dl
        dlinks = np.unique(lat['plinks'][bad].ravel()) if bad.any() else np.array([], int)
        nD = len(dlinks)
        if nD == 0:
            case['deltas'][str(dl)] = {'nD': 0}; continue
        mask = np.zeros(lat['Nl']); mask[dlinks] = 1.0
        def Bcol(i):
            y = np.zeros(lat['Nl']); y[dlinks[i]] = 1.0
            y = R.proj_P(lat, y)
            w, info = spla.cg(Mop, y, rtol=1e-10, atol=0, maxiter=30000)
            assert info == 0
            return (mask * R.proj_P(lat, w))[dlinks]
        t0 = time.time()
        if nD <= 260:
            G = np.zeros((nD, nD))
            for i in range(nD):
                G[:, i] = Bcol(i)
            G = 0.5 * (G + G.T)
            ev = np.linalg.eigvalsh(G)
            hs_meas = float(np.sqrt((ev ** 2).sum()))
            op_meas = float(ev.max())
            method = f'exact Gram ({nD} CG solves, {time.time()-t0:.0f}s)'
        else:
            th, rp, rl, _ = R.theta_of(lat, spl, dl, Mop, rng)
            op_meas = th
            tr2, nprobe = 0.0, 24
            for _ in range(nprobe):
                v = rng.choice([-1.0, 1.0], lat['Nl']) * mask
                y = R.proj_P(lat, v)
                w, info = spla.cg(Mop, y, rtol=1e-9, atol=0, maxiter=30000)
                assert info == 0
                w = mask * R.proj_P(lat, w)
                tr2 += float(w @ w)
            hs_meas = float(math.sqrt(tr2 / nprobe))
            method = f'Hutchinson({nprobe}) + power iter ({time.time()-t0:.0f}s)'
        def hs_bound(q):
            Xi = 8.0 * ((1 + q*q) / (1 - q*q)) ** 4
            return (2 * V0 / M2) * math.sqrt(nD * Xi)
        hb_CT, hb_q = hs_bound(q_CT), hs_bound(q_meas)
        case['deltas'][str(dl)] = {
            'nD': int(nD), 'rho_link': nD / lat['Nl'], 'theta_op': op_meas,
            'HS_meas': hs_meas, 'HS_bound_qCT': hb_CT, 'HS_bound_qmeas': hb_q,
            'S_CT': hb_CT / hb_q, 'S_vol': hb_q / hs_meas,
            'S_int': hs_meas / op_meas, 'S_total': hb_CT / op_meas,
            'method': method}
    out['cases'].append(case)
    print(f"L={L} beta={beta}  q_CT={q_CT:.4f}  q_meas={q_meas:.4f}  shells={meds}")
    for dl, d_ in case['deltas'].items():
        if d_.get('nD', 0) == 0: continue
        print(f"  d={dl}: |D|={d_['nD']:4d} theta={d_['theta_op']:.4f} HS={d_['HS_meas']:.3f} "
              f"bound(qCT)={d_['HS_bound_qCT']:.0f} S_CT={d_['S_CT']:.1f} "
              f"S_vol={d_['S_vol']:.1f} S_int={d_['S_int']:.2f} S_tot={d_['S_total']:.0f}")

json.dump(out, open('CERT_OP1_kchain_ledger.json', 'w'), indent=1)
print('wrote CERT_OP1_kchain_ledger.json')
