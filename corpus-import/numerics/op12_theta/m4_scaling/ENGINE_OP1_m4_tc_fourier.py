#!/usr/bin/env python3
# ENGINE_OP1_m4_tc_fourier.py — closes the M4 open item "T_C beyond x3 refinement".
# First engine written under DECISIONS #009 (agents do the mathematics).
#
# DERIVATION (momentum space; grounds: derived + machine-verified by gates below).
# On the flat 4-torus link complex, with g(k)_mu = e^{ik_mu}-1, lambda(k) = |g(k)|^2
# = sum_nu 4 sin^2(k_nu/2):
#   * exact sector (im d0):    symbol g g^dag / lambda,    Delta1up = 0 there
#   * transverse sector (ker d0^*): P_T(k) = I - g g^dag / lambda  (k != 0, dim 3)
#   * harmonic sector: the four k = 0 modes (dim 4 = deposited G1)
#   * Delta1 = lambda(k) I_4 componentwise  =>  Delta1up|_T = lambda(k) I.
# Source e_b, b = link(0,mu): e_b^hat(k)_nu = delta_{mu nu}/sqrt(Ns). Hence
#   T_C(mu) = (1/Ns) sum_{k!=0} (P_T(k))_{mu mu} / (m02 + alpha*lambda(k))^2 .
# Coordinate-permutation symmetry => T_C(mu) independent of mu; tr P_T = 3 exactly =>
#   T_C = (3/4) * S2,   S2 = (1/Ns) sum_{k!=0} (m02 + alpha*lambda(k))^{-2}      (*)
#   T_H = 1/(m02^2 Ns)  (k=0 block, matches deposited closed form), T_full = T_H + T_C.
# Route B (independent): 1/A^2 = int_0^inf t e^{-A t} dt  =>
#   S2 = int_0^inf t e^{-m02 t} ( q(alpha t)^4 - 1/Ns ) dt,
#   q(u) = (1/L) sum_n exp(-4 u sin^2(pi n / L)).                                 (**)
# IR asymptotics of (*) along the physical diagonal (m02 = mbar2/s^2, L = 4s):
#   alpha^2 T_C = (3/(64 pi^2)) [ 2 ln s + ln alpha + C(lhat) ] + O(1/s^2)
#   => slope d(alpha^2 T_C)/d ln s -> 3/(32 pi^2) = 0.0094986  (no saturation).
#
# HARD GATES (assert):
#   F1  per-mu transverse sum == (3/4) S2 on full 4D grids, L in {4,6}, rel <= 1e-12
#   F2  T_full reproduces every CERT_OP1_kernel_consts.json row (m02=0.5), rtol 1e-6
#   F3  T_C reproduces ALL deposited CERT_OP1_m4_harmonic_decomposition.json rows rtol 2e-5
#       (CG-side noise floor 1.5e-5 recorded in the DECOMP note); actual dev reported
#   F4  route A (k-sum) == route B (t-integral) at every k-sum L, rtol 1e-9
#   F5  route B self-check: panels+order+Tmax refined, rel <= 1e-9
# Resumable: state json updated after every row; L=256 k-sum chunked over k4 slices.
import os, sys, json, math, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)
os.chdir(TOP)
DEADLINE = time.time() + float(os.environ.get('M4F_BUDGET', '38'))
STATE = os.environ.get('M4F_STATE') or os.path.join(HERE, 'CERT_OP1_m4_tc_fourier.json')

C3_32PI2 = 3.0/(32.0*math.pi**2)

def lam_axis(L):
    n = np.arange(L)
    return 4.0*np.sin(np.pi*n/L)**2

# ---------------- route A: exact momentum sum -------------------------------
def S2_ksum(L, m02, alpha, resume=None, deadline=None):
    """Exact (1/Ns) sum_{k!=0} (m02+alpha*lam)^-2. Chunked over k4; resume dict."""
    s4 = lam_axis(L)
    l12 = (s4[:, None] + s4[None, :]).ravel()
    acc = 0.0 if resume is None else resume['acc']
    i0 = 0 if resume is None else resume['i4']
    for i4 in range(i0, L):
        d = m02 + alpha*(l12[:, None] + (s4 + s4[i4])[None, :])
        acc += float((1.0/(d*d)).sum())
        if deadline and time.time() > deadline and i4 < L-1:
            return None, {'acc': acc, 'i4': i4+1}
    return (acc - 1.0/m02**2)/float(L)**4, None

def permu_gate(L, m02, alpha):
    """F1: explicit per-mu transverse sums on the full 4D grid == (3/4) S2."""
    s4 = lam_axis(L)
    lam = (s4[:, None, None, None] + s4[None, :, None, None]
           + s4[None, None, :, None] + s4[None, None, None, :])
    den = (m02 + alpha*lam)**2
    lam_safe = lam.copy(); lam_safe[0, 0, 0, 0] = 1.0
    s2ref, _ = S2_ksum(L, m02, alpha)
    for mu in range(4):
        sh = [1, 1, 1, 1]; sh[mu] = L
        w = 1.0 - s4.reshape(sh)/lam_safe
        w[0, 0, 0, 0] = 0.0
        tcmu = float((w/den).sum())/float(L)**4
        rel = abs(tcmu - 0.75*s2ref)/(0.75*s2ref)
        assert rel <= 1e-12, f'GATE F1 FAIL: mu={mu} L={L} rel={rel:.2e}'
    return s2ref

# ---------------- route B: heat-kernel t-integral ----------------------------
_GL = {}
def gl(n):
    if n not in _GL: _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]

def S2_quad(L, m02, alpha, npanel=80, ngl=64, tmax_fac=50.0):
    s4 = lam_axis(L)
    rmin = m02 + (alpha*s4[1] if L > 1 else 0.0)   # slowest tail rate
    Tmax = tmax_fac/rmin
    t0 = 1e-3/(m02 + 4.0*alpha + 1e-300)
    edges = np.concatenate([[0.0], np.geomspace(t0, Tmax, npanel)])
    xg, wg = gl(ngl)
    invNs = 1.0/float(L)**4
    tot = 0.0
    for a, b in zip(edges[:-1], edges[1:]):
        tn = 0.5*(b-a)*xg + 0.5*(a+b)
        ww = 0.5*(b-a)*wg
        q = np.exp(-alpha*np.outer(tn, s4)).mean(axis=1)
        tot += float((ww * tn*np.exp(-m02*tn)*(q**4 - invNs)).sum())
    return tot

def S2_quad_gated(L, m02, alpha):
    v1 = S2_quad(L, m02, alpha)
    v2 = S2_quad(L, m02, alpha, npanel=120, ngl=96, tmax_fac=75.0)
    rel = abs(v1-v2)/abs(v2)
    assert rel <= 1e-9, f'GATE F5 FAIL: L={L} quad refinement rel={rel:.2e}'
    return v2

# ---------------- AF diagonal bookkeeping (mirrors deposited engines) --------
N_ = 3; c_af = 11*N_/(48*math.pi**2)
beta0 = 5.6; x0 = math.exp(beta0/(2*c_af)); mbar2 = 0.5*x0**2
def diag_point(s):
    x = x0*s
    return mbar2/x**2, 2*c_af*math.log(x)           # m02, beta

def nstar_split(m02, Ns, Tc):
    n, ns = 1, 0
    while n/(m02*Ns) + math.sqrt(n*Tc) < 1.0:
        ns = n; n += 1
        if n > 10**7: break
    return ns

# ---------------- main --------------------------------------------------------
def main():
    state = json.load(open(STATE)) if os.path.exists(STATE) else {
        'meta': {'engine': 'ENGINE_OP1_m4_tc_fourier.py',
                 'formula': 'T_C=(3/4)(1/Ns)sum_{k!=0}(m02+alpha*lam(k))^-2; '
                            'T_H=1/(m02^2 Ns); alpha_W=beta/6 (Casimir, theory/DOC_GOV_conventions.md); v0=1',
                 'routes': 'A=exact k-sum; B=heat-kernel t-integral (independent)',
                 'gates': 'F1 per-mu==3/4*S2; F2 kernel_consts anchors; '
                          'F3 all deposited DECOMP rows; F4 A==B; F5 quad self-refinement',
                 'asymptote': 'alpha^2 T_C ~ (3/64pi^2)(2 ln s + ln alpha + C); slope3_32pi2=%.10f' % C3_32PI2},
        'gates': {}, 'rows': [], 'ksum_partial': {}}
    rows_done = {r['s'] for r in state['rows']}

    # ---- F1 ----
    if not state['gates'].get('F1'):
        for (L, m02, al) in [(4, 0.5, beta0/6), (6, 0.2222222222222222, 5.6565/6)]:
            permu_gate(L, m02, al)
        state['gates']['F1'] = True
        json.dump(state, open(STATE, 'w'), indent=1)
        print('GATE F1 pass: per-mu transverse sums == (3/4)S2 exactly (L=4,6, rel<=1e-12)')

    # ---- F2 ----
    if not state['gates'].get('F2'):
        kc = json.load(open('CERT_OP1_kernel_consts.json'))['tables']
        worst = 0.0
        for r in kc:
            L, beta = r['L'], r['beta']
            s2, _ = S2_ksum(L, 0.5, beta/6.0)
            tf = 1.0/(0.25*float(L)**4) + 0.75*s2
            rel = abs(tf - r['T_full_max'])/r['T_full_max']
            worst = max(worst, rel)
            assert rel <= 1e-6, f'GATE F2 FAIL: L={L} b={beta} rel={rel:.2e}'
        state['gates']['F2'] = {'n_anchors': len(kc), 'worst_rel': worst}
        json.dump(state, open(STATE, 'w'), indent=1)
        print(f'GATE F2 pass: {len(kc)} kernel_consts anchors, worst rel {worst:.2e}')

    # ---- F3 ----
    if not state['gates'].get('F3'):
        dep = json.load(open(os.path.join(HERE, 'CERT_OP1_m4_harmonic_decomposition.json')))['rows']
        worst = 0.0
        for r in dep:
            L, m02, al = r['L'], r['m02'], r['beta']/6.0
            s2, _ = S2_ksum(L, m02, al)
            tc = 0.75*s2
            th = 1.0/(m02*m02*float(L)**4)
            relC = abs(tc - r['T_C'])/r['T_C']
            relH = abs(th - r['T_H'])/r['T_H']
            worst = max(worst, relC)
            assert relH <= 1e-12, f'GATE F3 FAIL (T_H closed form): L={L} s={r["scale"]}'
            assert relC <= 2e-5, f'GATE F3 FAIL: L={L} s={r["scale"]} relC={relC:.2e}'
        state['gates']['F3'] = {'n_rows': len(dep), 'worst_rel_TC': worst}
        json.dump(state, open(STATE, 'w'), indent=1)
        print(f'GATE F3 pass: all {len(dep)} deposited DECOMP rows reproduced, worst T_C rel {worst:.2e}')

    # ---- production diagonal ----
    SLIST = [1, 1.5, 2, 3, 4, 5, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128]
    KSUM_MAX_L = 256
    for s in SLIST:
        if s in rows_done: continue
        if time.time() > DEADLINE - 2:
            print(f'DEADLINE before s={s}; resume to continue'); break
        L = int(round(4*s)); Ns = float(L)**4
        m02, beta = diag_point(s); al = beta/6.0
        t0 = time.time()
        s2B = S2_quad_gated(L, m02, al)
        row = {'s': s, 'L': L, 'beta': round(beta, 4), 'm02': m02, 'alpha': al}
        if L <= KSUM_MAX_L:
            key = str(s)
            res = state['ksum_partial'].get(key)
            s2A, part = S2_ksum(L, m02, al, resume=res, deadline=DEADLINE-1.5)
            if s2A is None:
                state['ksum_partial'][key] = part
                json.dump(state, open(STATE, 'w'), indent=1)
                print(f's={s} (L={L}): k-sum chunk saved at i4={part["i4"]}/{L}; resume')
                break
            state['ksum_partial'].pop(key, None)
            rel = abs(s2A - s2B)/abs(s2A)
            assert rel <= 1e-9, f'GATE F4 FAIL: s={s} L={L} A-vs-B rel={rel:.2e}'
            row['S2_route_dev'] = rel
            s2 = s2A
        else:
            s2 = s2B
            row['S2_route_dev'] = None     # quad-only (scheme gated at L<=256 by F4 ladder)
        Tc = 0.75*s2; Th = 1.0/(m02*m02*Ns); Tf = Th + Tc
        row.update(T_C=Tc, T_H=Th, T_full=Tf,
                   Nstar=int(1/Tf), Nstar_C=int(1/Tc),
                   Nstar_split=nstar_split(m02, Ns, Tc),
                   a2TC=al*al*Tc, secs=round(time.time()-t0, 2))
        state['rows'].append(row)
        json.dump(state, open(STATE, 'w'), indent=1)
        print(f"s={s:6.1f} L={L:4d} b={beta:.4f}: T_C={Tc:.6f} a2TC={al*al*Tc:.6f} "
              f"N*={row['Nstar']} N*_C={row['Nstar_C']} N*_split={row['Nstar_split']} "
              f"[{row['secs']}s dev={row['S2_route_dev']}]")

    # ---- analysis (only when diagonal complete) ----
    done = {r['s'] for r in state['rows']}
    if all(s in done for s in SLIST):
        rows = sorted(state['rows'], key=lambda r: r['s'])
        ana = {}
        for wname, smin in [('s_ge_8', 8), ('s_ge_24', 24)]:
            W = [r for r in rows if r['s'] >= smin]
            x = np.array([math.log(r['s']) for r in W])
            y = np.array([r['a2TC'] for r in W])
            m, b = np.polyfit(x, y, 1)
            ana[wname] = {'slope': m, 'intercept': b,
                          'slope_over_3_32pi2': m/C3_32PI2,
                          'resid_rms': float(np.sqrt(np.mean((y-(m*x+b))**2)))}
        # two-parameter law with the ln(alpha) term included
        W = [r for r in rows if r['s'] >= 8]
        X = np.array([2*math.log(r['s']) + math.log(r['alpha']) for r in W])
        Y = np.array([r['a2TC'] for r in W])
        a, c = np.polyfit(X, Y, 1)
        ana['law_2lns_plus_lnalpha'] = {'coef': a, 'coef_over_3_64pi2': a/(C3_32PI2/2),
                                        'C': c/a if a else None,
                                        'resid_rms': float(np.sqrt(np.mean((Y-(a*X+c))**2)))}
        # saturating-fit refutation: fit c0 - c1/s on s in [2..6], extrapolate
        F = [r for r in rows if 2 <= r['s'] <= 6]
        xs = np.array([1.0/r['s'] for r in F]); ys = np.array([r['T_C'] for r in F])
        c1m, c0 = np.polyfit(xs, ys, 1)
        big = rows[-1]
        ana['saturating_fit'] = {'c0_pred_limit': c0, 'fit_window': '2<=s<=6',
                                 'pred_at_s128': c0 - (-c1m)/128 if False else c0 + c1m/128,
                                 'actual_at_s128': big['T_C'],
                                 'excess_of_actual_over_pred': big['T_C']/(c0 + c1m/128)}
        # local slopes
        ana['local_slopes_a2TC_dlns'] = [
            {'between': [rows[i]['s'], rows[i+1]['s']],
             'slope': (rows[i+1]['a2TC']-rows[i]['a2TC']) /
                      (math.log(rows[i+1]['s'])-math.log(rows[i]['s']))}
            for i in range(len(rows)-1)]
        state['analysis'] = ana
        json.dump(state, open(STATE, 'w'), indent=1)
        print('ANALYSIS written; ALL GATES PASSED; diagonal complete '
              f"(slope/['3/(32pi^2)'] = {ana['s_ge_8']['slope_over_3_32pi2']:.4f} on s>=8, "
              f"{ana['s_ge_24']['slope_over_3_32pi2']:.4f} on s>=24)")
    else:
        print(f"{len(done)}/{len(SLIST)} diagonal rows done; ALL GATES PASSED on completed work")

if __name__ == '__main__':
    main()
