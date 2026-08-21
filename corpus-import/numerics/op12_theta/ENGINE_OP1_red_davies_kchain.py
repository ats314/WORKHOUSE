#!/usr/bin/env python3
# ENGINE_OP1_red_davies_kchain.py — review unit #10d (June 12, 2026)
# Inserts the red_propositions Davies decay rates into the June-11 OP-7 chain
# accounting, replacing q_CT. Everything else in the chain (Xi shell sum,
# (2 v0/m^2) prefactor, |D| factor) is kept IDENTICAL to ENGINE_OP1_kchain_ledger.py, so
# any change in the bound is attributable to the decay constant alone.
#
# Sources (statements used as-is, no mathematical judgment):
#   E:\YANG\ORGANIZED\02_APPENDICES\red_propositions\
#     Red - 003: Prop 9.X   eta_DG  = arcosh(1 + m^2/(2 alpha D_E))
#     Red - 005: Def  C0    = max_b sum_{b'!=b} |(Delta_1)_{bb'}|_op
#     Red - 006: Prop 9.X'  eta_DG0 = arcosh(1 + m^2/(2 alpha C0))
#     Red - 007: Def  C_partial (boundary row-sum, |dphi|=1 neighbors only)
#     Red - 008: Cor  9.X'' eta_DGp = arcosh(1 + m^2/(2 alpha C_partial))
#   June-11 chain: ENGINE_OP1_kchain_ledger.py (q_CT = 1/(1+m^2/(2 alpha 18)),
#     Xi(q) = 8((1+q^2)/(1-q^2))^4, HS_bound = (2 v0/m^2) sqrt(|D| Xi)).
#
# CAVEAT carried verbatim from the June-11 ledger: the chain applies an
# M^{-1}-entry decay bound to the PROJECTED kernel G_P = P M^{-1} P. The red
# propositions bound M^{-1} entries only; whether the P-transfer is rigorous
# is part of OP-7's write-up, not established here. Gate G6 checks the
# resulting bounds still dominate the measured HS norms on stored cases.
#
# Hard gates (assert; any failure kills the run):
#  G1 formula reproduction of Red-006's printed sanity numbers
#  G2 C0 <= D_E = 18 and C_partial <= C0 (Defs 005/007), entries all |.|=1
#  G3 recomputed bound(q_CT) matches stored CERT_OP1_kchain_ledger.json to 1e-9 rel
#  G4 eta_DG(C) > eta_CT at every (L,beta,C) (strict rate improvement)
#  G5 pointwise Davies domination: |M^{-1} e_b0| <= (2/m^2) exp(-eta * dist)
#     at the SHARPEST admissible eta (C_partial), L=4 b=5.6 and L=6 b=6.4
#  G6 bound(q_DG) >= HS_meas on every stored case (chain stays an upper bound)
#  G7 JSON written and re-read identical
import json, math, sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import importlib.util

t0 = time.time()
sys.argv = ['rd', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('r', 'ENGINE_OP1_op12_runner.py')
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)

M2, V0, DE, CE = 0.5, 1.0, 18.0, 8.0
BETAS = (5.6, 6.0, 6.4, 6.8, 7.2)

def gate(name, ok, detail=''):
    print(f"{'PASS' if ok else 'FAIL'} {name}  {detail}")
    assert ok, f"GATE {name}: {detail}"

# ---- G1: reproduce Red-006 sanity numbers (alpha=1, m^2=0.3, C0=6) --------
eta_dg_s = math.acosh(1 + 0.3/12); eta_ct_s = math.log(1 + 0.3/12)
gate('G1_red006_sanity', abs(eta_dg_s - 0.2236) < 5e-4 and abs(eta_ct_s - 0.0247) < 5e-4,
     f"eta_DG={eta_dg_s:.4f} (vs 0.2236), eta_CT={eta_ct_s:.4f} (vs 0.0247)")

def Xi(q):            # shell sum, identical to ENGINE_OP1_kchain_ledger.py
    return CE * ((1 + q*q) / (1 - q*q))**4
def hs_bound(q, nD):  # identical to ENGINE_OP1_kchain_ledger.py
    return (2*V0/M2) * math.sqrt(nD * Xi(q))

out = {'meta': {'m2': M2, 'v0': V0, 'alpha_W': 'beta/6', 'D_E': DE, 'c_E': CE,
                'date': '2026-06-12', 'unit': '#10d',
                'caveat': 'chain transfers M^-1 decay to G_P=PM^-1P exactly as the June-11 ledger does; '
                          'red props bound M^-1 entries only (P-transfer = OP-7 write-up question)'},
       'row_sum_constants': [], 'rates': [], 'chain_recheck': [], 'decay_validation': [],
       'per_sqrtD_constants': []}

# ---- row-sum constants C0, C_partial (exact, configuration-independent) ----
CONSTS = {}
for L in (4, 6):
    lat = R.lattice(L)
    A = lat['L1up'].tocsr()
    B = A.copy(); B.setdiag(0); B.eliminate_zeros()
    absB = abs(B)
    C0 = float(absB.sum(axis=1).max())
    entmax = float(absB.max())
    adj = (absB > 0).astype(np.int8).tocsr()
    Bc = B.tocoo()
    Cp = 0.0
    for mu in range(4):                       # orientation orbits of b'
        probe = mu                            # link (site 0, direction mu)
        dist = np.full(lat['Nl'], -1); dist[probe] = 0; fr = [probe]; d = 0
        while fr:
            d += 1; nxt = []
            for b in fr:
                for b2 in adj[b].indices:
                    if dist[b2] < 0: dist[b2] = d; nxt.append(b2)
            fr = nxt
        m = (np.abs(dist[Bc.row] - dist[Bc.col]) == 1)
        rs = np.zeros(lat['Nl']); np.add.at(rs, Bc.row[m], np.abs(Bc.data[m]))
        Cp = max(Cp, float(rs.max()))
    gate(f'G2_L{L}_rowsums', C0 <= DE + 1e-9 and Cp <= C0 + 1e-9 and abs(entmax-1.0) < 1e-12,
         f"C0={C0:.0f} (D_E={DE:.0f}), C_partial={Cp:.0f}, max|entry|={entmax:.1f}")
    CONSTS[L] = (C0, Cp)
    out['row_sum_constants'].append({'L': L, 'C0': C0, 'C_partial': Cp, 'D_E': DE})

# ---- rates and per-sqrt|D| chain constants for all (L, beta) ---------------
for L in (4, 6):
    C0, Cp = CONSTS[L]
    for beta in BETAS:
        al = beta/6.0
        row = {'L': L, 'beta': beta}
        qs = {}
        for tag, C in (('CT_DE', DE), ('DG_DE', DE), ('DG_C0', C0), ('DG_Cp', Cp)):
            x = M2/(2*al*C)
            eta = math.log(1+x) if tag == 'CT_DE' else math.acosh(1+x)
            q = math.exp(-eta)
            qs[tag] = q
            row[f'eta_{tag}'] = eta; row[f'q_{tag}'] = q
        gate(f'G4_L{L}_b{beta}', row['eta_DG_DE'] > row['eta_CT_DE'] and
             row['eta_DG_Cp'] >= row['eta_DG_C0'] >= row['eta_DG_DE'],
             f"eta CT={row['eta_CT_DE']:.4f} < DG(DE)={row['eta_DG_DE']:.4f} <= "
             f"DG(C0)={row['eta_DG_C0']:.4f} <= DG(Cp)={row['eta_DG_Cp']:.4f}")
        out['rates'].append(row)
        # chain per-sqrt|D| constant (2 v0/m^2) sqrt(Xi(q)) vs exact c=sqrt(T_full)
        pc = {'L': L, 'beta': beta,
              **{f'const_{t}': (2*V0/M2)*math.sqrt(Xi(q)) for t, q in qs.items()}}
        out['per_sqrtD_constants'].append(pc)

# attach exact c = sqrt(T_full) from CERT_OP1_kernel_consts.json for comparison
kc = json.load(open('CERT_OP1_kernel_consts.json'))
for pc in out['per_sqrtD_constants']:
    for t in kc['tables']:
        if t['L'] == pc['L'] and abs(t['beta'] - pc['beta']) < 1e-9:
            pc['c_exact_sqrt_Tfull'] = t['c_HS_pred']
            pc['slack_CT_vs_exact'] = pc['const_CT_DE']/t['c_HS_pred']
            pc['slack_DGCp_vs_exact'] = pc['const_DG_Cp']/t['c_HS_pred']

# ---- G3 + G6: re-run the stored kchain cases with the new rates ------------
kl = json.load(open('CERT_OP1_kchain_ledger.json'))
for case in kl['cases']:
    L, beta = case['L'], case['beta']
    al = beta/6.0
    C0, Cp = CONSTS[L]
    q_ct = 1.0/(1.0 + M2/(2*al*DE))
    gate(f'G3a_qCT_L{L}_b{beta}', abs(q_ct - case['q_CT']) < 1e-12, f"{q_ct:.6f}")
    for dl, v in case['deltas'].items():
        nD = v.get('nD', 0)
        if nD == 0: continue
        b_ct = hs_bound(q_ct, nD)
        gate(f'G3b_bound_L{L}_b{beta}_d{dl}', abs(b_ct - v['HS_bound_qCT'])/v['HS_bound_qCT'] < 1e-9,
             f"recomputed {b_ct:.3f} vs stored {v['HS_bound_qCT']:.3f}")
        rec = {'L': L, 'beta': beta, 'delta': float(dl), 'nD': nD,
               'theta_op': v['theta_op'], 'HS_meas': v['HS_meas'], 'HS_bound_qCT': b_ct}
        for tag, C in (('DG_DE', DE), ('DG_C0', C0), ('DG_Cp', Cp)):
            q = math.exp(-math.acosh(1 + M2/(2*al*C)))
            b_dg = hs_bound(q, nD)
            rec[f'HS_bound_{tag}'] = b_dg
            rec[f'improve_{tag}'] = b_ct/b_dg
            gate(f'G6_{tag}_L{L}_b{beta}_d{dl}', b_dg >= v['HS_meas'],
                 f"bound {b_dg:.1f} >= HS_meas {v['HS_meas']:.3f}")
        rec['S_kernel_CT'] = b_ct/v['HS_meas']
        rec['S_kernel_DG_Cp'] = rec['HS_bound_DG_Cp']/v['HS_meas']
        rec['S_total_CT'] = b_ct/v['theta_op']
        rec['S_total_DG_Cp'] = rec['HS_bound_DG_Cp']/v['theta_op']
        out['chain_recheck'].append(rec)

# ---- G5: pointwise Davies domination on exact M^{-1} columns ---------------
for L, beta in ((4, 5.6), (6, 6.4)):
    lat = R.lattice(L)
    al = beta/6.0
    Mop = (M2*sp.eye(lat['Nl']) + al*lat['L1up']).tocsr()
    B = lat['L1up'].tocsr().copy(); B.setdiag(0); B.eliminate_zeros()
    adj = (abs(B) > 0).astype(np.int8).tocsr()
    worst = 0.0; prof = {}
    for probe in range(4):                    # all 4 orientation orbits
        dist = np.full(lat['Nl'], -1); dist[probe] = 0; fr = [probe]; d = 0
        while fr:
            d += 1; nxt = []
            for b in fr:
                for b2 in adj[b].indices:
                    if dist[b2] < 0: dist[b2] = d; nxt.append(b2)
            fr = nxt
        e = np.zeros(lat['Nl']); e[probe] = 1.0
        z, info = spla.cg(Mop, e, rtol=1e-12, atol=0, maxiter=40000)
        assert info == 0
        eta_p = math.acosh(1 + M2/(2*al*CONSTS[L][1]))   # sharpest: C_partial
        bnd = (2.0/M2)*np.exp(-eta_p*dist)
        ratio = np.abs(z)/bnd
        worst = max(worst, float(ratio.max()))
        for dd in range(int(dist.max())+1):
            m_ = np.abs(z[dist == dd])
            if len(m_):
                prev = prof.get(dd, {'max_abs': 0.0, 'bound': float((2.0/M2)*math.exp(-eta_p*dd)), 'n': 0})
                prof[dd] = {'max_abs': max(prev['max_abs'], float(m_.max())),
                            'bound': prev['bound'], 'n': prev['n'] + len(m_)}
    gate(f'G5_davies_dominates_L{L}_b{beta}', worst <= 1.0 + 1e-9, f"max |M^-1|/bound = {worst:.4f}")
    out['decay_validation'].append({'L': L, 'beta': beta, 'eta_used': eta_p,
                                    'max_ratio_meas_over_bound': worst,
                                    'profile': {str(k): v for k, v in sorted(prof.items())}})

# ---- write + G7 -------------------------------------------------------------
json.dump(out, open('CERT_OP1_red_davies_kchain.json', 'w'), indent=1)
back = json.load(open('CERT_OP1_red_davies_kchain.json'))
gate('G7_json_roundtrip', back['meta']['unit'] == '#10d' and
     len(back['chain_recheck']) == len(out['chain_recheck']), f"{len(out['chain_recheck'])} case rows")

# ---- console summary --------------------------------------------------------
print('\n=== #10d summary (all gates passed) ===')
print(f"row-sum constants: L=4 C0={CONSTS[4][0]:.0f} Cp={CONSTS[4][1]:.0f} | "
      f"L=6 C0={CONSTS[6][0]:.0f} Cp={CONSTS[6][1]:.0f}  (D_E=18)")
for rec in out['chain_recheck']:
    print(f"L={rec['L']} b={rec['beta']} d={rec['delta']}: |D|={rec['nD']:4d}  "
          f"bound CT={rec['HS_bound_qCT']:.2e} -> DG(Cp)={rec['HS_bound_DG_Cp']:.2e}  "
          f"(x{rec['improve_DG_Cp']:.0f} tighter)  S_kernel {rec['S_kernel_CT']:.1e}->{rec['S_kernel_DG_Cp']:.1e}")
for pc in out['per_sqrtD_constants']:
    if 'c_exact_sqrt_Tfull' in pc:
        print(f"L={pc['L']} b={pc['beta']}: per-sqrt|D| const CT={pc['const_CT_DE']:.3e} "
              f"DG(Cp)={pc['const_DG_Cp']:.3e} exact={pc['c_exact_sqrt_Tfull']:.3f}  "
              f"residual slack DG/exact={pc['slack_DGCp_vs_exact']:.1e}")
print(f"runtime {time.time()-t0:.1f}s")
