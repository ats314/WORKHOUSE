#!/usr/bin/env python3
# ENGINE_OP1_m4_tc_realspace_check.py — independent REAL-SPACE verification of the Fourier
# closed form (ENGINE_OP1_m4_tc_fourier.py) inside the extension region, at (L=16,s=4) and
# (L=24,s=6) on the physical diagonal. Different formalism end-to-end: explicit
# sparse d0/d1 complex + Hodge-projected CG solves (the op12/M2/DECOMP route),
# vs the momentum-space sum. Agreement is the cross-route gate.
#
# Big-L enablement: vectorized operator builder (R.lattice's Python loops are
# O(minutes) at L>=16), gated EXACTLY against R.lattice at L=8; L1up built as
# kron(L0s, I4) - d0 d0^T (Fourier-identity construction), gated exactly against
# d1^T d1 at L=8 and L=16.
#
# HARD GATES (assert):
#   R0  vectorized d0,d1 == R.lattice(8) operators, exact (nnz of difference = 0)
#   R0b kron-built L1up == d1^T d1, exact at L=8,16
#   G1  harmonic eigenspace: |d1 h|=0, |d0^T h|=0, |P h - h| <= 1e-10
#   G5  every CG solution carries explicit residual check <= 1e-9 rel
#   G3  (L=16, mu=0) UNSPLIT full solve: T_H_closed + T_C == T_full rtol 1e-8,
#       cross-term <= 1e-10 scale   [at L=24 the unsplit solve is skipped: its
#       conditioning ~ alpha*16/m02 ~ 1.1e3 makes it a >45 s unit; independence
#       at L=24 rests on the Fourier cross gate + residual + G4-structure]
#   G4  harmonic amplitude of full column == closed form rtol 1e-10 (L=16)
#   SYM deflated T_C spread across computed directions <= 1e-8 rel
#   X   每 T_C(mu) vs Fourier row value rtol 1e-7 (the headline cross gate)
# Resumable per work-unit; operator cache on disk (opcache/).
import os, sys, json, math, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spla
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)
os.chdir(TOP)
DEADLINE = time.time() + float(os.environ.get('M4R_BUDGET', '38'))
STATE = os.environ.get('M4R_STATE') or os.path.join(HERE, 'CERT_OP1_m4_tc_realspace_check.json')
CACHE = os.path.join(HERE, 'opcache'); os.makedirs(CACHE, exist_ok=True)

sys.argv = ['m4r', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('r', 'ENGINE_OP1_op12_runner.py')
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)

N_ = 3; c_af = 11*N_/(48*math.pi**2)
beta0 = 5.6; x0 = math.exp(beta0/(2*c_af)); mbar2 = 0.5*x0**2
def diag_point(s):
    x = x0*s
    return mbar2/x**2, 2*c_af*math.log(x)

# ------------------ vectorized operator builder ------------------------------
def sidx(c, L):  # c: (...,4) coords -> site index, matching R.lattice
    return ((c[..., 3]*L + c[..., 2])*L + c[..., 1])*L + c[..., 0]

def build_ops(L):
    t0 = time.time()
    fns = {k: os.path.join(CACHE, f'{k}_L{L}.npz') for k in ('d0', 'd1', 'L0', 'L1up')}
    if all(os.path.exists(f) for f in fns.values()):
        ops = {k: sp.load_npz(f) for k, f in fns.items()}
        ops.update(Ns=L**4, Nl=4*L**4); return ops
    Ns, Nl = L**4, 4*L**4
    s = np.arange(Ns)
    c = np.stack([s % L, (s//L) % L, (s//L**2) % L, (s//L**3) % L], 1)
    nbr = np.empty((Ns, 4), np.int64)
    for mu in range(4):
        cp = c.copy(); cp[:, mu] = (cp[:, mu]+1) % L; nbr[:, mu] = sidx(cp, L)
    # d0: row 4s+mu: +1 at nbr(s,mu), -1 at s
    l = (4*s[:, None] + np.arange(4)[None, :]).ravel()
    rows = np.repeat(l, 2)
    cols = np.stack([nbr.ravel(), np.repeat(s, 4)], 1).ravel()
    vals = np.tile([1.0, -1.0], Nl)
    d0 = sp.csr_matrix((vals, (rows, cols)), shape=(Nl, Ns))
    # d1: plaquette p=6s+oi, oi over ordered pairs mu<nu, links [+ (s,mu), + (nbr(s,mu),nu), - (nbr(s,nu),mu), - (s,nu)]
    ORIS = [(mu, nu) for mu in range(4) for nu in range(mu+1, 4)]
    rws, cls, vls = [], [], []
    for oi, (mu, nu) in enumerate(ORIS):
        p = 6*s + oi
        ls = np.stack([4*s+mu, 4*nbr[:, mu]+nu, 4*nbr[:, nu]+mu, 4*s+nu], 1)
        rws.append(np.repeat(p, 4)); cls.append(ls.ravel())
        vls.append(np.tile([1.0, 1.0, -1.0, -1.0], Ns))
    d1 = sp.csr_matrix((np.concatenate(vls), (np.concatenate(rws), np.concatenate(cls))),
                       shape=(6*Ns, Nl))
    assert abs(d1 @ d0).max() == 0.0, 'GATE FAIL: d1 d0 != 0'
    L0 = (d0.T @ d0).tocsr()
    # L1up by the Fourier-identity construction (gated vs d1^T d1 at L=8,16):
    L1up = (sp.kron(L0, sp.eye(4), format='csr') - (d0 @ d0.T)).tocsr()
    L1up.eliminate_zeros()
    for k, A in (('d0', d0), ('d1', d1), ('L0', L0), ('L1up', L1up)):
        sp.save_npz(fns[k], A)
    print(f'  built+cached ops L={L} [{time.time()-t0:.0f}s]')
    return dict(d0=d0, d1=d1, L0=L0, L1up=L1up, Ns=Ns, Nl=Nl)

def gate_R0(state):
    if state['gates'].get('R0'): return
    ref = R.lattice(8); v = build_ops(8)
    assert (ref['d0'] != v['d0']).nnz == 0, 'GATE R0 FAIL: d0 mismatch'
    assert (ref['d1'] != v['d1']).nnz == 0, 'GATE R0 FAIL: d1 mismatch'
    assert ((ref['d1'].T @ ref['d1']).tocsr() != v['L1up']).nnz == 0, 'GATE R0b FAIL: L1up L=8'
    v16 = build_ops(16)
    direct = (v16['d1'].T @ v16['d1']).tocsr(); direct.eliminate_zeros()
    assert (direct != v16['L1up']).nnz == 0, 'GATE R0b FAIL: L1up L=16'
    state['gates']['R0'] = True
    json.dump(state, open(STATE, 'w'), indent=1)
    print('GATE R0/R0b pass: vectorized ops == R.lattice(8) exactly; kron L1up == d1^T d1 (L=8,16)')

def harm_basis(L, Nl):
    H = np.zeros((4, Nl))
    for mu in range(4):
        H[mu, mu::4] = 1.0/math.sqrt(L**4)
    return H

def gate_G1(ops, H):
    for mu in range(4):
        h = H[mu]
        assert abs(ops['d1'] @ h).max() < 1e-12, 'GATE G1 FAIL: d1 h != 0'
        assert abs(ops['d0'].T @ h).max() < 1e-12, 'GATE G1 FAIL: div h != 0'
        ph = R.proj_P(ops, h)
        assert np.linalg.norm(ph - h) < 1e-10, 'GATE G1 FAIL: P h != h'

def cg(Mop, y, tag):
    z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=400000)
    assert info == 0, f'GATE FAIL: CG {tag}'
    r = np.linalg.norm(Mop @ z - y)/np.linalg.norm(y)
    assert r <= 1e-9, f'GATE G5 FAIL: {tag} residual {r:.2e}'
    return z

# ------------------------------ work units -----------------------------------
UNITS = [('build', 16, None), ('build', 24, None),
         ('defl', 16, 0), ('full', 16, 0),
         ('defl', 16, 1), ('defl', 16, 2), ('defl', 16, 3),
         ('defl', 24, 0), ('defl', 24, 1),
         ('finish', 0, None)]
SOFL = {16: 4.0, 24: 6.0}

def main():
    state = json.load(open(STATE)) if os.path.exists(STATE) else {
        'meta': {'engine': 'ENGINE_OP1_m4_tc_realspace_check.py',
                 'purpose': 'independent real-space CG verification of the Fourier '
                            'closed form at (16,s=4),(24,s=6); alpha_W=beta/6; v0=1',
                 'gates': 'R0/R0b exact ops, G1 eigenspace, G5 residuals, '
                          'G3/G4 unsplit identity (L=16), SYM, X=cross-vs-Fourier'},
        'gates': {}, 'units': {}}
    fou = {r['s']: r for r in json.load(open(os.path.join(HERE, 'CERT_OP1_m4_tc_fourier.json')))['rows']}
    gate_R0(state)
    for kind, L, mu in UNITS:
        key = f'{kind}_{L}_{mu}'
        if key in state['units']: continue
        if time.time() > DEADLINE - 2:
            print(f'DEADLINE before {key}; resume to continue'); return
        if kind == 'build':
            build_ops(L); state['units'][key] = True
        elif kind == 'finish':
            done = {k for k in state['units']}
            tcs = {}
            for LL in (16, 24):
                mus = sorted(int(k.split('_')[2]) for k in done
                             if k.startswith('defl_%d' % LL))
                vals = [state['units'][f'defl_{LL}_{m}']['T_C'] for m in mus]
                spread = (max(vals)-min(vals))/min(vals)
                assert spread <= 1e-8, f'GATE SYM FAIL: L={LL} spread={spread:.2e}'
                tcs[LL] = dict(T_C_mean=float(np.mean(vals)), n_dirs=len(vals),
                               spread=spread,
                               fourier_dev=abs(np.mean(vals)-fou[SOFL[LL]]['T_C'])/fou[SOFL[LL]]['T_C'])
            state['summary'] = tcs
            state['units'][key] = True
            print('GATE SYM pass; SUMMARY:', json.dumps(tcs))
            print('ALL GATES PASSED — real-space CG confirms the Fourier values at L=16 and L=24')
        else:
            s = SOFL[L]; m02, beta = diag_point(s); al = beta/6.0
            ops = build_ops(L); H = harm_basis(L, ops['Nl'])
            gate_G1(ops, H)
            Mop = (m02*sp.eye(ops['Nl']) + al*ops['L1up']).tocsr()
            e = np.zeros(ops['Nl']); e[mu] = 1.0
            y = R.proj_P(ops, e)
            t0 = time.time()
            Th_closed = 1.0/(m02*m02*ops['Ns'])
            if kind == 'defl':
                yC = y - H.T @ (H @ y)
                zC = cg(Mop, yC, f'defl L={L} mu={mu}')
                colC = R.proj_P(ops, zC); colC -= H.T @ (H @ colC)
                Tc = float(colC @ colC)
                dev = abs(Tc - fou[s]['T_C'])/fou[s]['T_C']
                assert dev <= 1e-7, f'GATE X FAIL: L={L} mu={mu} dev={dev:.2e}'
                state['units'][key] = {'T_C': Tc, 'fourier_dev': dev,
                                       'secs': round(time.time()-t0, 1)}
                print(f'GATE X pass: L={L} mu={mu} T_C={Tc:.9f} vs Fourier dev={dev:.2e} '
                      f'[{state["units"][key]["secs"]}s]')
            else:  # full, unsplit (L=16 only)
                z = cg(Mop, y, f'full L={L} mu={mu}')
                col = R.proj_P(ops, z)
                amp = H @ col
                Th_num = float(amp @ amp)
                assert abs(Th_num - Th_closed) <= 1e-10*Th_closed, 'GATE G4 FAIL'
                colC = col - H.T @ amp
                Tf = float(col @ col); Tc_sub = float(colC @ colC)
                ref = state['units'].get(f'defl_{L}_{mu}')
                assert ref is not None, 'unit order broken'
                assert abs((Th_closed + ref['T_C']) - Tf) <= 1e-8*Tf, \
                    f'GATE G3 FAIL: identity {Th_closed+ref["T_C"]} vs {Tf}'
                assert abs(Tc_sub - ref['T_C']) <= 1e-8*ref['T_C'], 'GATE G3 FAIL: subtract'
                state['units'][key] = {'T_full': Tf, 'T_H_num': Th_num,
                                       'secs': round(time.time()-t0, 1)}
                print(f'GATE G3+G4 pass: L={L} unsplit T_full={Tf:.9f} == T_H+T_C rtol 1e-8 '
                      f'[{state["units"][key]["secs"]}s]')
        json.dump(state, open(STATE, 'w'), indent=1)
    if 'finish_0_None' in state['units']:
        print('ALL_WORK_DONE')

if __name__ == '__main__':
    main()
