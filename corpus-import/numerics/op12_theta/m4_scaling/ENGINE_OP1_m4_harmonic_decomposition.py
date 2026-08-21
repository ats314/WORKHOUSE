#!/usr/bin/env python3
# ENGINE_OP1_m4_harmonic_decomposition.py - resolves the open diagnostic of
# NOTE_OP1_m4_scaling_2026-06-12.md: decompose T_full(b) = sum_b' G_P(b,b')^2 into
# the HARMONIC sector (the 4 torus zero-modes h_mu of L1up inside im P, where
# M^{-1} = 1/m0^2) and the COEXACT remainder.
#
# Exact structure (gated below, not assumed):
#   im P = H (+) C orthogonally, dim H = 4,  h_mu(link(s,nu)) = delta_{mu,nu},
#   M h_mu = m0^2 h_mu  =>  G_P = G_H + G_C with G_H G_C = 0, hence
#   T_full(b) = T_H + T_C(b) exactly, with CLOSED FORM
#   T_H = 1/(m0^4 * Ns),  g_H = 1/(m0^2 * Ns),  Ns = L^4.
#   Physical diagonal (m0^2 = mbar2*a^2, L = l_phys/a):  m0^4*Ns = mbar2^2*l^4
#   => T_H is EXACTLY CONSTANT along the diagonal; all scaling drift sits in T_C.
#
# Split certificate (sharper than the pure-HS N*): the harmonic block of
# Pi_D G_P Pi_D is rank<=4 with EXACT norm max_mu |D_mu|/(m0^2 Ns) (the 4x4
# Gram is diagonal); the coexact block keeps the HS bound sqrt(|D| T_C). So
#   theta <= v0*[ |D|/(m0^2 Ns) + sqrt(|D| T_C) ]  and N*_split = max |D| with RHS < 1.
#
# HARD GATES (assert):
#   G1 exact harmonic eigenspace: |L1up h|=0, |d0^T h|=0, |P h - h| <= 1e-10
#   G2 anchor reproduction: (L,beta) in CERT_OP1_kernel_consts.json rtol 1e-6
#   G3 per-row decomposition identity: T_C(direct CG on deflated source)
#      + T_H(closed) == T_full(direct) rtol 1e-8; cross-term <= 1e-10*scale
#   G4 closed-form T_H == numerically projected harmonic part rtol 1e-10
# Resumable: state JSON written after every row; rerun skips done rows.
import sys, json, math, time, os
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spla
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)
os.chdir(TOP)
DEADLINE = time.time() + float(os.environ.get('M4H_BUDGET', '38'))

sys.argv = ['m4h', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('m2', 'm2_certificates/ENGINE_OP1_m2_pair_certificates.py')
m2 = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(m2)
except SystemExit: pass
R = m2.R

def harm_basis(lat):
    Ns, Nl = lat['Ns'], lat['Nl']
    H = np.zeros((4, Nl))
    for mu in range(4):
        H[mu, mu::4] = 1.0 / math.sqrt(Ns)   # links indexed 4*s+mu
    return H

def gate_G1(lat, H):
    for mu in range(4):
        h = H[mu]
        assert abs(lat['d1'] @ h).max() < 1e-12, 'GATE G1 FAIL: L1up h != 0'
        assert abs(lat['d0'].T @ h).max() < 1e-12, 'GATE G1 FAIL: div h != 0'
        ph = R.proj_P(lat, h)
        assert np.linalg.norm(ph - h) < 1e-10, 'GATE G1 FAIL: P h != h'

def row_compute(lat, H, m02, alpha):
    """Direct decomposition with per-orbit CG; returns dict + gate checks."""
    Ns, Nl = lat['Ns'], lat['Nl']
    Mop = (m02*sp.eye(Nl) + alpha*lat['L1up']).tocsr()
    T_H_closed = 1.0/(m02*m02*Ns)
    g_H_closed = 1.0/(m02*Ns)
    Tf_list, Tc_list, cross_max = [], [], 0.0
    for mu in range(4):
        e = np.zeros(Nl); e[mu] = 1.0           # link (site 0, dir mu)
        y = R.proj_P(lat, e)
        # full solve
        z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=120000)
        assert info == 0, 'GATE FAIL: CG full'
        col = R.proj_P(lat, z)                   # G_P e_b
        # harmonic component of the column (numeric) vs closed form
        amp = H @ col                            # 4 coefficients
        colH = H.T @ amp
        colC = col - colH
        T_H_num = float(colH @ colH)
        assert abs(T_H_num - T_H_closed) <= 1e-10*T_H_closed + 1e-14, \
            f'GATE G4 FAIL: T_H num {T_H_num} vs closed {T_H_closed}'
        # direct coexact solve: deflate source, solve, deflate again
        yC = y - H.T @ (H @ y)
        zC, info = spla.cg(Mop, yC, rtol=1e-12, atol=0, maxiter=120000)
        assert info == 0, 'GATE FAIL: CG coexact'
        colC_dir = R.proj_P(lat, zC); colC_dir -= H.T @ (H @ colC_dir)
        Tc_dir = float(colC_dir @ colC_dir)
        Tc_sub = float(colC @ colC)
        assert abs(Tc_dir - Tc_sub) <= 1e-8*max(Tc_dir, 1e-30), \
            f'GATE G3 FAIL: T_C direct {Tc_dir} vs subtract {Tc_sub}'
        cross = abs(float(colH @ colC_dir))
        cross_max = max(cross_max, cross)
        Tf = float(col @ col)
        assert abs((Tc_dir + T_H_closed) - Tf) <= 1e-8*Tf, \
            f'GATE G3 FAIL: T_H+T_C {Tc_dir+T_H_closed} vs T_full {Tf}'
        Tf_list.append(Tf); Tc_list.append(Tc_dir)
    assert cross_max < 1e-10*max(Tf_list), 'GATE G3 FAIL: cross term'
    Tf = max(Tf_list); Tc = max(Tc_list)
    # split certificate: v0=1: largest integer n with n/(m02*Ns) + sqrt(n*Tc) < 1
    nstar_split = 0
    n = 1
    while n/(m02*Ns) + math.sqrt(n*Tc) < 1.0:
        nstar_split = n; n += 1
        if n > 10**7: break
    return dict(T_full=Tf, T_H=T_H_closed, T_C=Tc, g_H=g_H_closed,
                frac_H=T_H_closed/Tf, Nstar=int(1/Tf), Nstar_C=int(1/Tc),
                Nstar_split=nstar_split, cross_max=cross_max)

def main():
    state_path = os.environ.get('M4H_STATE') or os.path.join(HERE, 'CERT_OP1_m4_harmonic_decomposition.json')
    state = json.load(open(state_path)) if os.path.exists(state_path) else \
        {'meta': {'engine': 'ENGINE_OP1_m4_harmonic_decomposition.py',
                  'conventions': 'alpha_W = beta/6 (Casimir convention, theory/DOC_GOV_conventions.md); v0=1',
                  'closed_forms': 'T_H=1/(m0^4 Ns), g_H=1/(m0^2 Ns), Ns=L^4; exact, gated',
                  'split_cert': 'theta <= |D|/(m0^2 Ns) + sqrt(|D| T_C) (harmonic rank-4 exact + coexact HS)',
                  'gates': 'G1 eigenspace, G2 anchors, G3 decomposition identity + cross term, G4 closed form'},
         'gates_G2': False, 'rows': []}
    done = {(r['L'], r['scale']) for r in state['rows']}

    # SELF-CONTAINED ladder (the deposited CERT_OP1_m4_scaling_tables.json is missing its
    # s=1.0/1.25 rows - its engine overwrites rather than accumulates; recorded
    # in M4_HARMONIC_DECOMP note). Full grid + L=12 extension of the diagonal.
    N_ = 3; c_af = 11*N_/(48*math.pi**2)
    beta0 = 5.6; x0 = math.exp(beta0/(2*c_af)); mbar2 = 0.5*x0**2
    rows_in = []
    for L in (4, 6, 8):
        for sfac in (1.0, 1.25, 1.5, 2.0, 3.0):
            x = x0*sfac; rows_in.append((L, sfac, mbar2/x**2, 2*c_af*math.log(x)))
    for sfac in (1.0, 3.0):                      # L=12: fixed-s point + 3rd diagonal step
        x = x0*sfac; rows_in.append((12, sfac, mbar2/x**2, 2*c_af*math.log(x)))

    # G2 anchors (cheap, every run)
    kc = {(r['L'], r['beta']): r['T_full_max'] for r in json.load(open('CERT_OP1_kernel_consts.json'))['tables']}
    for (L, b) in [(4, 6.4), (6, 7.2)]:
        lat = R.lattice(L); H = harm_basis(lat); gate_G1(lat, H)
        Mop = (0.5*sp.eye(lat['Nl']) + (b/6.0)*lat['L1up']).tocsr()
        e = np.zeros(lat['Nl']); Tfm = 0.0
        for mu in range(4):
            e[:] = 0; e[mu] = 1.0
            y = R.proj_P(lat, e)
            z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=120000)
            assert info == 0
            col = R.proj_P(lat, z); Tfm = max(Tfm, float(col @ col))
        ref = kc[(L, b)]
        assert abs(Tfm-ref) <= 1e-6*ref, f'GATE G2 FAIL {L},{b}'
    state['gates_G2'] = True
    print('GATE G1+G2 pass (eigenspace exact; anchors reproduce kernel_consts)')

    for (L, sfac, m02, beta) in rows_in:
        if (L, sfac) in done: continue
        if time.time() > DEADLINE:
            print(f'DEADLINE: stopping before (L={L}, s={sfac}); resume to continue')
            break
        lat = R.lattice(L); H = harm_basis(lat); gate_G1(lat, H)
        t0 = time.time()
        r = row_compute(lat, H, m02, beta/6.0)
        if sfac == 1.0 and (L, 5.6) in kc:       # extra anchor: s=1 IS the scan point
            assert abs(r['T_full']-kc[(L, 5.6)]) <= 1e-6*kc[(L, 5.6)], f'GATE G2b FAIL {L},s=1'
        r.update(L=L, scale=sfac, beta=round(beta, 4), m02=m02)
        state['rows'].append(r)
        json.dump(state, open(state_path, 'w'), indent=1)
        print(f"L={L} s={sfac:4.2f} m02={m02:.3e}: T_full={r['T_full']:.6f} "              f"T_H={r['T_H']:.6f} ({100*r['frac_H']:.0f}%) T_C={r['T_C']:.6f} "
              f"N*={r['Nstar']} N*_C={r['Nstar_C']} N*_split={r['Nstar_split']} [{time.time()-t0:.0f}s]")
    ntot = len(rows_in); ndone = len(state['rows'])
    print(f'{ndone}/{ntot} rows done; ALL GATES PASSED on completed rows')

if __name__ == '__main__':
    main()
