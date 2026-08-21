#!/usr/bin/env python3
# ENGINE_OP1_m4_scaling_tables.py - M4 prep (June 12, 2026): exact kernel constants under
# PHYSICAL scaling along the AF trajectory.
#   beta(a) = (11N/48pi^2) * log(1/(a*Lam)^2),  N=3   (OP-1's stated form)
#   m0^2(a) = mbar^2 * a^2   (physical mass mbar fixed; lattice-units m0^2 ~ a^2)
#   alpha_W(a) = beta(a)/6,  v0 = 1 (convention; rescaling tracked separately)
# Outputs T_full(a,L), g_diag, N* and the coexact-gap diagnostic alpha*lam_min.
# HARD GATE: the (m0^2=0.5, beta in scan ladder) reference reproduces
# CERT_OP1_kernel_consts.json rtol 1e-6 (machinery identity check).
import sys, json, math, time
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spla
import importlib.util
ARGV = sys.argv[1:]
sys.argv = ['m4', '--deadline', '0.0']
spec = importlib.util.spec_from_file_location('m2', 'm2_certificates/ENGINE_OP1_m2_pair_certificates.py')
m2 = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(m2)
except SystemExit: pass
R = m2.R
def consts(L, m02, alpha):
    lat = R.lattice(L)
    Mop = (m02*sp.eye(lat['Nl']) + alpha*lat['L1up']).tocsr()
    T = np.zeros((4, lat['Nl']))
    for mu in range(4):
        e = np.zeros(lat['Nl']); e[mu] = 1.0
        y = R.proj_P(lat, e)
        z, info = spla.cg(Mop, y, rtol=1e-12, atol=0, maxiter=80000)
        assert info == 0, 'GATE FAIL: CG'
        T[mu] = R.proj_P(lat, z)
    Tf = float((T**2).sum(1).max()); g = float(max(T[mu][mu] for mu in range(4)))
    return g, Tf
# GATE: reference reproduction
kc = {(r['L'], r['beta']): r['T_full_max'] for r in json.load(open('CERT_OP1_kernel_consts.json'))['tables']}
for (L, b) in [(4, 6.4), (6, 7.2)]:
    _, Tf = consts(L, 0.5, b/6.0)
    ref = kc[(L, b)]; assert abs(Tf-ref) <= 1e-6*ref, f'GATE FAIL ref {L},{b}'
print('GATE-REF pass (2 anchor points reproduce kernel_consts)')
# AF ladder: pick Lam*a0 so beta(a0)=5.6 ; then a_n = a0 * s^n
N = 3; c_af = 11*N/(48*math.pi**2)
out = {'meta': {'beta(a)': '11N/(48pi^2) log(1/(a Lam)^2), N=3',
 'm02(a)': 'mbar2 * a^2 with mbar2 chosen so m02=0.5 at beta=5.6 anchor',
 'alpha': 'beta/6', 'v0': 1.0,
 'note': 'finite-L exact computation; NOT a continuum statement'}, 'rows': []}
beta0 = 5.6; x0 = math.exp(beta0/(2*c_af))   # x = 1/(a Lam)
mbar2 = 0.5 * x0**2                           # so m02(a0)=0.5
which = [float(s) for s in ARGV] if ARGV else [1.0, 1.25, 1.5, 2.0, 3.0]
for L in (4, 6, 8):
    for sfac in which:
        x = x0*sfac                            # a = a0/sfac (finer lattice)
        beta = 2*c_af*math.log(x); m02 = mbar2/x**2; alpha = beta/6.0
        lat = R.lattice(L)
        # coexact gap diagnostic (smallest nonzero L1up eigenvalue on coexact):
        lam1 = 2*(1-math.cos(2*math.pi/L))*2   # analytic 4D coexact floor ~ 2-2cos(2pi/L) scale (diagnostic only)
        t0 = time.time(); g, Tf = consts(L, m02, alpha)
        row = {'L': L, 'scale': sfac, 'beta': round(beta, 4), 'm02': m02,
               'g_diag': g, 'T_full': Tf, 'Nstar': int(1/Tf),
               'alpha_lam_diag': alpha*lam1}
        out['rows'].append(row)
        print(f"L={L} s={sfac:4.2f} beta={beta:7.3f} m02={m02:.3e}: "
              f"T_full={Tf:.6f} Nstar={int(1/Tf):6d}  [{time.time()-t0:.0f}s]")
json.dump(out, open('m4_scaling/CERT_OP1_m4_scaling_tables.json', 'w'), indent=1)
print('wrote m4_scaling/CERT_OP1_m4_scaling_tables.json')
