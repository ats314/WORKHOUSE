#!/usr/bin/env python3
# L=8 kernel constants (third volume) + W(r) distance-shell tables (rho_2 interface).
import sys, json, math, time
ARGV = sys.argv[1:]
import numpy as np
import importlib.util
sys.argv = ['m2x', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('m2', 'ENGINE_OP1_m2_pair_certificates.py')
m2 = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(m2)
except SystemExit: pass
R = m2.R
out = {'L8_constants': [], 'shells': {}}
which = ARGV[0] if ARGV else 'all'
betas_L8 = [float(b) for b in ARGV[1:]] if len(ARGV) > 1 else [5.6, 6.4, 7.2]
if which in ('all', 'l8'):
    for beta in betas_L8:
        t0 = time.time()
        T, lat = m2.tensor(8, beta)
        Tf = float((T**2).sum(1).max()); g = float(max(T[mu][mu] for mu in range(4)))
        out['L8_constants'].append({'L': 8, 'beta': beta, 'g_diag': g, 'T_full': Tf,
                                    'c': math.sqrt(Tf), 'Nstar': int(1/Tf)})
        print(f"L=8 beta={beta}: g_diag={g:.5f} T_full={Tf:.6f} c={math.sqrt(Tf):.4f} "
              f"Nstar={int(1/Tf)}  [{time.time()-t0:.0f}s]")
if which in ('all', 'shells'):
    for L in (6, 8):
        for beta in (6.4,):
            import os
            f = f'm2_kernel/tensor_L{L}_b{beta}.npz'
            if not os.path.exists(f): continue
            T = np.load(f)['T']; cs = m2.lat_coords(L)
            d = cs.copy(); d = np.minimum(d, L - d)   # min-image per coord
            r2 = (d**2).sum(1)                         # site displacement r^2
            shells = {}
            for mu in range(4):
                G = T[mu].reshape(-1, 4)               # (Ns, 4) by target site
                for s_ in range(len(r2)):
                    key = int(r2[s_])
                    m_ = float(np.abs(G[s_]).max()); q = float((G[s_]**2).sum())
                    e = shells.setdefault(key, [0.0, 0.0, 0])
                    e[0] = max(e[0], m_); e[1] += q; e[2] += 4
            tab = {str(k): {'maxG': v[0], 'sumG2': v[1], 'n': v[2]}
                   for k, v in sorted(shells.items())[:10]}
            out['shells'][f'L{L}_b{beta}'] = tab
            print(f'W(r) shells L={L} b={beta} (r2: maxG / sumG2):')
            for k, v in list(tab.items())[:7]:
                print(f"  r2={k}: {v['maxG']:.5f} / {v['sumG2']:.6f}")
json.dump(out, open('CERT_OP1_m2_l8_shells.json', 'w'), indent=1)
print('wrote CERT_OP1_m2_l8_shells.json')
