#!/usr/bin/env python3
# ENGINE_OP1_m2_ensemble.py - fresh certified ensembles, resuming stored MC states.
# For each new config: defect sets D(delta) STORED (link indices), exact pair
# certificate + measured theta recorded. Deadline-chunked and resumable.
import sys, json, os, math, time
import numpy as np, scipy.sparse as sp
import importlib.util
ARGV = sys.argv[1:]
sys.argv = ['m2e', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('m2', 'ENGINE_OP1_m2_pair_certificates.py')
m2 = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(m2)
except SystemExit: pass
R = m2.R
DEADLINE = time.time() + float(ARGV[0])
L = int(ARGV[1]); NWANT = int(ARGV[2]); betas = [float(b) for b in ARGV[3:]]
os.makedirs('m2_ensemble', exist_ok=True)
for beta in betas:
    fn = f'm2_ensemble/ens_L{L}_b{beta}.json'
    ens = json.load(open(fn)) if os.path.exists(fn) else []
    if len(ens) >= NWANT:
        print(f'L={L} b={beta}: complete ({len(ens)})'); continue
    T, lat = m2.tensor(L, beta)
    Nstar = int(1/ (T**2).sum(1).max())
    job = dict(L=L, beta=beta, therm=120 if L == 4 else 100,
               ncfg=20 if L == 4 else 12, sep=4)
    latt, U, meta, res, rng = R.load_job(job)
    # continue the chain: advance rng state per stored draw count if tracked; we
    # accept chain continuation from final state (documented in results note)
    Mop = (0.5*sp.eye(lat['Nl']) + (beta/6.0)*lat['L1up']).tocsr()
    while len(ens) < NWANT and time.time() < DEADLINE - 8:
        for _ in range(job['sep']):
            R.sweep(lat, U, beta, meta['eps'], rng)
        spl = R.plaq_field(lat, U)
        rec = {'i': len(ens), 'plaq': float(1-spl.mean()), 'deltas': {}}
        for dl in (0.9, 1.1):
            bad = spl > dl
            D = np.unique(lat['plinks'][bad].ravel()) if bad.any() else np.array([], int)
            th, _, _, _ = R.theta_of(lat, spl, dl, Mop, rng)
            c = m2.cert_exact(T, L, D) if len(D) else 0.0
            assert c >= th - 1e-6, 'GATE FAIL: GATE-VALID'
            rec['deltas'][str(dl)] = {'nD': int(len(D)), 'theta': th, 'cert': c,
                'certified': bool(c < 1.0), 'count_cert': bool(len(D) <= Nstar),
                'D': [int(x) for x in D]}
        ens.append(rec)
        json.dump(ens, open(fn, 'w'))
        print(f"L={L} b={beta} cfg{rec['i']}: " + " | ".join(
            f"d={dl}: |D|={v['nD']:4d} cert={v['cert']:.3f} th={v['theta']:.3f} "
            f"{'C' if v['certified'] else '-'}" for dl, v in rec['deltas'].items()))
    print(f'L={L} b={beta}: {len(ens)}/{NWANT}')
print('CHUNK_DONE')
