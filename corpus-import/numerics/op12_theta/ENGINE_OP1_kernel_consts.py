#!/usr/bin/env python3
# ENGINE_OP1_kernel_consts.py - exact configuration-INDEPENDENT kernel constants for the
# projected massive Maxwell resolvent G_P = P M^{-1} P  (M = m0^2 I + (beta/6) d1^T d1).
# Since M, P depend only on the lattice (not on U), the HS step of the BS chain,
#   tr K^2 = v0^2 * sum_{b,b' in D} G_P(b,b')^2,
# is a quadratic sum of a FIXED kernel over the random defect set. This script
# computes, exactly (up to CG tol 1e-12):
#   g_diag    = G_P(b,b)                  (translation-invariant; orientation orbit)
#   T_full(b) = sum_{b'} G_P(b,b')^2      (full row square sum)
# giving the elementary worst-case certificate (no probability, no CT):
#   ||K||_HS^2 <= v0^2 |D| max_b T_full(b)   ==>   theta < 1 whenever
#   |D| < (1/v0^2) / max_b T_full(b) =: Nstar.
# Also: L=6 shell-decay profile of G_P columns (L=4 graph too small to resolve).
import json, math
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spla
import importlib.util, sys
sys.argv = ['k', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('r', 'ENGINE_OP1_op12_runner.py')
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
M2, V0 = 0.5, 1.0
out = {'meta': {'m2': M2, 'v0': V0, 'alpha_W': 'beta/6',
                'note': 'G_P column computed per orientation orbit (translation invariance)'},
       'tables': []}
for L in (4, 6):
    lat = R.lattice(L)
    for beta in (5.6, 6.0, 6.4, 6.8, 7.2):
        alpha = beta/6.0
        Mop = (M2*sp.eye(lat['Nl']) + alpha*lat['L1up']).tocsr()
        row = {'L': L, 'beta': beta}
        Ts, gs = [], []
        for mu in range(4):   # orientation orbits of links
            b = 4*0 + mu      # link (site 0, direction mu)
            e = np.zeros(lat['Nl']); e[b] = 1.0
            y = R.proj_P(lat, e)
            z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=40000)
            assert info == 0
            col = R.proj_P(lat, z)          # G_P e_b
            gs.append(float(col[b])); Ts.append(float((col**2).sum()))
        T = max(Ts); g = max(gs)
        row['g_diag'] = g; row['T_full_max'] = T
        row['c_HS_pred'] = math.sqrt(T)     # ||K||_HS ~ c sqrt(|D|) worst case
        row['Nstar_theta_lt_1'] = int(1.0/(V0**2*T))
        out['tables'].append(row)
        print(f"L={L} beta={beta}: g_diag={g:.5f}  T_full={T:.6f}  "
              f"c=sqrt(T)={math.sqrt(T):.4f}  Nstar={row['Nstar_theta_lt_1']}")
    # decay profile at L=6 only (graph big enough)
    if L == 6:
        adj = ((abs(lat['d1']).T @ abs(lat['d1'])) > 0).astype(np.int8)
        adj.setdiag(0); adj.eliminate_zeros()
        beta = 6.4; alpha = beta/6.0
        Mop = (M2*sp.eye(lat['Nl']) + alpha*lat['L1up']).tocsr()
        e = np.zeros(lat['Nl']); e[0] = 1.0
        y = R.proj_P(lat, e)
        z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=40000)
        col = np.abs(R.proj_P(lat, z))
        dist = np.full(lat['Nl'], -1); dist[0] = 0; fr=[0]; d=0
        while fr:
            d += 1; nxt=[]
            for b in fr:
                for b2 in adj[b].indices:
                    if dist[b2] < 0: dist[b2]=d; nxt.append(b2)
            fr = nxt
        prof = {}
        for dd in range(1, int(dist.max())+1):
            m_ = col[dist==dd]
            prof[dd] = {'median': float(np.median(m_)), 'max': float(m_.max()), 'n': int(len(m_))}
        out['decay_L6_b6.4'] = prof
        print('L=6 b=6.4 G_P column profile (dist: median / max):')
        for dd, v in prof.items():
            print(f"  d={dd}: {v['median']:.3e} / {v['max']:.3e}  (n={v['n']})")
json.dump(out, open('CERT_OP1_kernel_consts.json','w'), indent=1)
print('wrote CERT_OP1_kernel_consts.json')
