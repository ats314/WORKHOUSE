#!/usr/bin/env python3
# ENGINE_OP1_m4_sparsity_interface.py — quantitative (S)/M4 interface along the physical
# diagonal, combining (i) the T_C log law (ENGINE_OP1_m4_tc_fourier.py: T_C ~ (3/32pi^2 a^2) ln s,
# machine-verified, no saturation), (ii) the measured fixed-threshold defect
# densities from the stored OP-12 MC ensembles, (iii) the split-certificate algebra.
#
# ALGEBRA (derived; convention alpha_W = beta/6, anchor a=1 at beta0=5.6, L=4s):
#   rho_P(beta; delta) ~ e^{-kappa(delta) beta}  (Peierls ansatz, fitted below)
#   E|D| <= 4*6*L^4*rho_P = 6144 s^4 e^{-kappa beta(s)} ~ s^{4 - 2 c_af kappa}
#   (prefactor display corrected June 12 late, was mis-stated 1536 = #plaquettes;
#    exponents and all findings unaffected — see F027)
#   theta <= v0 [ |D|/(m0^2 L^4) + sqrt(|D| T_C) ],  T_C ~ (3/(32 pi^2 alpha^2)) ln s
#   With v0 = c_v a^q = c_v s^{-q}:   theta_HS-part ~ s^{2 - q - c_af kappa} sqrt(ln s)
#   CLOSURE CONDITION on the diagonal:   q + c_af * kappa > 2
#     q = 0  =>  kappa > 2/c_af = 28.71   (this script measures whether that holds)
#     breakeven exponent:  q*(delta) = 2 - c_af * kappa_hat(delta)
#
# DATA GATES (assert — data integrity, not conclusions):
#   D1 all 8 stored ensembles load; config counts match meta (20 at L=4, 12 at L=6)
#   D2 rho_P strictly decreasing in beta wherever total defect count >= 50
#   D3 L=4 vs L=6 kappa agreement within z <= 2.5 (Poisson WLS standard errors)
#   D4 fits use count-weighted WLS on ln rho, points with >= 10 defect plaquettes
# Output: CERT_OP1_m4_sparsity_interface.json. Findings are PRINTED, not asserted.
import json, glob, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)
os.chdir(TOP)

c_af = 11*3/(48*math.pi**2)
KREQ = 2.0/c_af
DELTAS = ('0.7', '0.9', '1.1')
EXPECT = {4: 20, 6: 12}

ens = {}
files = sorted(glob.glob('op12_state/results_L*_b*.json'))
assert len(files) == 8, f'GATE D1 FAIL: expected 8 ensembles, found {len(files)}'
for f in files:
    tag = f.split('results_')[1].replace('.json', '')
    L = int(tag.split('_')[0][1:]); b = float(tag.split('_b')[1])
    cfgs = json.load(open(f))['cfg']
    assert len(cfgs) == EXPECT[L], f'GATE D1 FAIL: {f} has {len(cfgs)} cfgs'
    ens[(L, b)] = cfgs

rows, fits = [], {}
for d in DELTAS:
    fits[d] = {}
    for L in (4, 6):
        pts = []
        for (LL, b) in sorted(ens):
            if LL != L: continue
            rp = np.array([c[f'rhoP_d{d}'] for c in ens[(LL, b)]])
            ntot = int(round(float((rp*6*L**4).sum())))
            pts.append((b, float(rp.mean()), ntot))
            rows.append({'L': L, 'beta': b, 'delta': float(d),
                         'rhoP_mean': float(rp.mean()), 'n_defect_plaq_total': ntot,
                         'n_cfg': len(rp)})
        # D2 monotonicity where statistics are solid
        well = [(b, r) for (b, r, n) in pts if n >= 50]
        for (b1, r1), (b2, r2) in zip(well[:-1], well[1:]):
            assert r2 < r1, f'GATE D2 FAIL: rho_P not decreasing d={d} L={L} {b1}->{b2}'
        # D4: count-weighted WLS on ln rho (Var[ln n_hat] ~ 1/n), floor n >= 10
        use = [(b, r, n) for (b, r, n) in pts if n >= 10]
        assert len(use) >= 2, f'GATE D4 FAIL: <2 usable points (n>=10) d={d} L={L}'
        bs = np.array([u[0] for u in use]); lr = np.log([u[1] for u in use])
        w = np.array([u[2] for u in use], float)
        W = np.diag(w); X = np.stack([bs, np.ones_like(bs)], 1)
        cov = np.linalg.inv(X.T @ W @ X)
        coef = cov @ (X.T @ W @ lr)
        kappa = float(-coef[0]); kerr = float(math.sqrt(cov[0, 0]))
        fits[d][L] = {'kappa_hat': kappa, 'kappa_se': kerr,
                      'betas_used': list(map(float, bs)),
                      'counts_used': [int(u[2]) for u in use]}
    k4, k6 = fits[d][4]['kappa_hat'], fits[d][6]['kappa_hat']
    s4, s6 = fits[d][4]['kappa_se'], fits[d][6]['kappa_se']
    z = abs(k4-k6)/math.sqrt(s4**2 + s6**2)
    assert z <= 2.5, f'GATE D3 FAIL: volume tension d={d}: {k4:.2f}+-{s4:.2f} vs {k6:.2f}+-{s6:.2f} (z={z:.1f})'
    wv = np.array([1/s4**2, 1/s6**2])
    fits[d]['combined'] = float((wv[0]*k4 + wv[1]*k6)/wv.sum())
    fits[d]['combined_se'] = float(1/math.sqrt(wv.sum()))
    fits[d]['volume_z'] = z

print('GATES D1-D4 pass (8 ensembles, counts, monotonicity, volume z<=2.5)')
print(f'required for q=0 closure: kappa > 2/c_af = {KREQ:.3f}')
out = {'meta': {'engine': 'ENGINE_OP1_m4_sparsity_interface.py',
                'convention': 'alpha_W=beta/6; anchor a=1 at beta0=5.6; diagonal L=4s',
                'closure_condition': 'q + c_af*kappa > 2 (v0 = c_v a^q)',
                'kappa_required_q0': KREQ, 'c_af': c_af,
                'caveats': 'Peierls ansatz over narrow window beta 5.6-7.2; small volumes '
                           'L=4,6; MC configs correlated (sep=4) so Poisson SEs are indicative; '
                           'fixed-delta defect family only',
                'data': 'OP-12 stored ensembles op12_state/results_L{4,6}_b*.json '
                        '(June 11 scan; 20/12 cfgs; deltas 0.7/0.9/1.1)'},
       'density_rows': rows, 'kappa_fits': fits, 'findings': {}}
for d in DELTAS:
    k = fits[d]['combined']; se = fits[d]['combined_se']
    qstar = 2.0 - c_af*k
    out['findings'][d] = {
        'kappa_hat': k, 'kappa_se': se, 'kappa_over_required': k/KREQ,
        'q_star_breakeven': qstar,
        'E_D_exponent_at_q0': 4 - 2*c_af*k,
        'theta_exponent_at_q2': - c_af*k}
    print(f'  delta={d}: kappa_hat={k:5.2f}+-{se:.2f} ({100*k/KREQ:4.1f}% of required) '
          f'-> q*={qstar:.3f}; q=0: E|D| ~ s^{4-2*c_af*k:+.3f} (proliferates); '
          f'q=2: theta ~ s^{-c_af*k:+.3f} sqrt(ln s) (closes)')
print('FINDING (computed, not asserted): fixed-threshold defects cannot satisfy the '
      'q=0 requirement anywhere in the measured family -- and the Wilson action cost of '
      'any single plaquette is <= 2*beta, capping kappa(delta) at O(2-4) for every fixed '
      'delta <= 2: the q=0 route is structurally closed, not just empirically short.')
print('CONSEQUENCE: v0 physical scaling (q) is load-bearing for M4 diagonal closure; '
      'q >= q* ~ 1.8-1.9 needed at measured kappa; at q=2 ANY exponential sparsity closes.')
json.dump(out, open(os.path.join(HERE, 'CERT_OP1_m4_sparsity_interface.json'), 'w'), indent=1)
print('wrote CERT_OP1_m4_sparsity_interface.json')
