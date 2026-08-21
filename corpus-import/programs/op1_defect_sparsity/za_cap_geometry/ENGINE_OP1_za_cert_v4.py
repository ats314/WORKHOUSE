#!/usr/bin/env python3
# One-shot final (v4): G-ZA4 = fit-quality gate for the cap-ratio law form
# nu(C_p) ~ C_geom kappa^{-M} e^{-kappa Delta_p} (validate form + small residual,
# report M); the load-bearing certified claim is the RATE = Delta_p (G-ZA3).
import json, math, os
import numpy as np
rng = np.random.default_rng(20260612)

def cmax(m, N, a, tol=1e-12):
    if N.size == 0 or N.shape[0] == 0:
        nm = float(np.linalg.norm(m))
        if nm < tol: return np.array([1.0,0,0,0]), 0.0
        u = m/nm; return u, float(u@m)
    G = N @ N.T
    try: Ginv = np.linalg.inv(G)
    except np.linalg.LinAlgError: return None, -np.inf
    k = N.shape[0]; b = a*np.ones(k); u0 = N.T @ (Ginv @ b); s = float(u0@u0)
    if s > 1.0 - tol: return None, -np.inf
    mp_ = m - N.T @ (Ginv @ (N @ m)); mp = float(np.linalg.norm(mp_))
    if mp < tol:
        for j in range(4):
            ej = np.zeros(4); ej[j]=1.0
            ep = ej - N.T @ (Ginv @ (N @ ej)); ne = float(np.linalg.norm(ep))
            if ne > tol:
                u = u0 + math.sqrt(max(0.0,1.0-s))*(ep/ne); return u, float(u@m)
        return None, -np.inf
    u = u0 + math.sqrt(max(0.0,1.0-s))*(mp_/mp); return u, float(u@m)

def solve(m, nl, a, it=1e-9):
    na = np.asarray(nl, dtype=float).reshape(-1,4); A = len(na)
    bu=None; bv=-np.inf; ba=()
    for mask in range(1 << A):
        act = tuple(i for i in range(A) if (mask>>i)&1)
        Na = na[list(act)] if act else np.zeros((0,4))
        u,v = cmax(m, Na, a)
        if u is None: continue
        ok=True
        for j in range(A):
            if j in act: continue
            if float(na[j]@u) > a+it: ok=False; break
        if ok and v>bv: bv=v; bu=u; ba=act
    return bu, bv, ba

def runit(n):
    v = rng.standard_normal((n,4)); return v/np.linalg.norm(v,axis=1,keepdims=True)

vp=0.0; npri=0; rmp=np.inf; nm=0; rmm=np.inf; nmv=0; ng=0; nt=0
g2=0.0; n_asym=0; asym_dev=0.0; worst_multi=(0.0,0.0,1e9)
for _ in range(60000):
    k = int(rng.integers(0,5)); m = runit(1)[0]; n_p = runit(1)[0]
    A = runit(k) if k>0 else np.zeros((0,4)); a = float(rng.uniform(-0.2,0.95))
    uA,hA,act = solve(m,A,a)
    if uA is None: continue
    chi0 = float(uA@n_p)-a; nt += 1
    if chi0 <= 1e-6: continue
    ng += 1
    Aa = np.vstack([A,n_p[None,:]]) if k>0 else n_p[None,:]
    uAp,hAp,_ = solve(m,Aa,a)
    if uAp is None: continue
    Dp = hA-hAp; r = Dp/(chi0*chi0)
    if k == 0:
        npri += 1; rmp = min(rmp,r)
        if Dp < 0.5*chi0*chi0 - 1e-7: vp = max(vp, 0.5*chi0*chi0 - Dp)
        c0 = float(m@n_p)
        cf = 1.0 - (c0*a + math.sqrt(max(0.0,(1-c0*c0)*(1-a*a))))
        g2 = max(g2, abs(Dp - cf))
        if chi0 < 0.02*(1.0-c0*c0):
            n_asym += 1
            asym_dev = max(asym_dev, abs(r - 0.5/(1.0-c0*c0))/(0.5/(1.0-c0*c0)))
    else:
        nm += 1; rmm = min(rmm,r)
        if Dp < 0.5*chi0*chi0 - 1e-7:
            nmv += 1
            if r < worst_multi[2]: worst_multi = (chi0, Dp, r)

assert vp < 1e-7, f'GATE FAIL G-ZA1: {vp}'
assert g2 < 1e-7, f'GATE FAIL G-ZA2: {g2}'
mvr = (nmv/nm) if nm else 0.0

def nu_empty(c0,a,kap,Ng=1800):
    s0 = math.sqrt(1.0-c0*c0)
    w = np.linspace(-1,1,Ng); y = np.linspace(-1,1,Ng)
    W,Y = np.meshgrid(w,y,indexing='ij'); dk = (W*W+Y*Y)<1.0
    rad = np.zeros_like(W); rad[dk] = np.sqrt(1.0-W[dk]**2-Y[dk]**2)
    lw = kap*W; lw[~dk] = -1e18; Mx = lw.max()
    wt = np.exp(lw-Mx)*rad; g = c0*W+s0*Y
    cm = (g<=a)&dk; dA = (w[1]-w[0])*(y[1]-y[0])
    return (wt[cm].sum()*dA)/(wt.sum()*dA)

def Drate(c0,a): return 1.0-(c0*a+math.sqrt((1-c0*c0)*(1-a*a)))
c0=0.80; a=0.50; Dp0=Drate(c0,a)
kaps = np.array([60,90,130,180,250,350,500,700],dtype=float)
nl = np.array([-math.log(nu_empty(c0,a,k)) for k in kaps])
# fit  nl = kappa*Dp0 - M*log(kappa) - logCgeom  (3 unknowns? Dp0 known -> 2)
res = nl - kaps*Dp0
Am = np.vstack([-np.log(kaps), -np.ones_like(kaps)]).T
co,(*_,),rk,sv = np.linalg.lstsq(Am,res,rcond=None); Mf,lcg = co[0],co[1]
fitvals = kaps*Dp0 - Mf*np.log(kaps) - lcg
fit_res = float(np.max(np.abs(nl - fitvals)))           # max abs residual of the law
# also a 3-param check: fit Dp as free slope and compare to Dp0
Am3 = np.vstack([kaps, -np.log(kaps), -np.ones_like(kaps)]).T
co3,*_ = np.linalg.lstsq(Am3,nl,rcond=None); Dp_fit = co3[0]
sl = (nl[-1]-nl[-2])/(kaps[-1]-kaps[-2])
assert abs(sl-Dp0) < 0.02, f'GATE FAIL G-ZA3: slope {sl} vs Dp {Dp0}'
assert abs(Dp_fit-Dp0) < 0.01, f'GATE FAIL G-ZA3b: 3-param slope {Dp_fit} vs {Dp0}'
# G-ZA4: the kappa^{-M} e^{-kappa Dp} FORM fits with small residual (law validated)
assert fit_res < 0.05, f'GATE FAIL G-ZA4: cap-ratio law residual {fit_res}'

out = {
 'gates':'G-ZA1,G-ZA2,G-ZA3,G-ZA3b,G-ZA4 PASS; G-ZA5 recorded',
 'part1_curvature':{
   'proved_case':'k=0 bare target cap',
   'G-ZA1_lower_bound':'Delta_p >= chi0^2/2 (PASS; k=0 min ratio %.4f)'%rmp,
   'G-ZA2_closed_form':'Delta_p = 1-(c0*a+sqrt((1-c0^2)(1-a^2))) exact, worst dev %.2e'%g2,
   'leading_const':'Delta_p/chi0^2 -> 1/(2(1-c0^2)); asymptotic-regime dev %.2e (n=%d)'%(asym_dev,n_asym),
   'n_good':ng,'n_total':nt,'k0_n':npri,
   'incident_n':nm,'incident_min_ratio':float(rmm),'incident_violation_rate':mvr,
   'worst_incident_exhibit':{'chi0':worst_multi[0],'Delta_p':worst_multi[1],'ratio':worst_multi[2]},
   'finding':'incident caps (k>=1) VIOLATE Delta_p>=chi0^2/2 (rate %.2f): LCI-reduction Sec.9 (9.4)-(9.5) chi0-at-u_A criterion is INVALID for incident subsets; the good event must be parametrized by the true height-drop Delta_p (exactly what cap-ratio law (8.4) needs)'%mvr,
 },
 'part2_capratio':{
   'geometry':{'c0':c0,'a':a,'chi0':c0-a,'Delta_p_rate':Dp0},
   'kappas':kaps.tolist(),'neglog_nu':nl.tolist(),
   'rate_2pt_slope':sl,'rate_3param_fit':float(Dp_fit),
   'M_prefactor_power':float(Mf),'logC_geom':float(lcg),'law_max_residual':fit_res,
   'note':'nu(C_p) ~ C_geom kappa^{-M} e^{-kappa Delta_p}; RATE = Delta_p certified (G-ZA3/3b); M extracted (corner-Laplace, density vanishes at the dominant point => M<0, prefactor ~ kappa^{+|M|})',
 },
}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here,'CERT_OP1_za_cap.json'),'w'), indent=1)
print('G-ZA1 (k=0 Delta_p>=chi0^2/2): PASS  min ratio %.4f (>=0.5)' % rmp)
print('G-ZA2 (k=0 closed form Delta_p): PASS  worst dev %.2e' % g2)
print('  leading const 1/(2(1-c0^2)): asym-regime dev %.2e (n=%d)' % (asym_dev,n_asym))
print('G-ZA5 RECORDED: incident k>=1 n=%d min ratio %.4f VIOLATION rate %.2f' % (nm,rmm,mvr))
print('  worst incident exhibit: chi0=%.3f Delta_p=%.4f ratio=%.4f (<<0.5)' % worst_multi)
print('G-ZA3 (rate->Delta_p=%.5f): PASS slope %.5f ; 3-param %.5f' % (Dp0,sl,Dp_fit))
print('G-ZA4 (cap-ratio law form fits): PASS  max residual %.4f ; M=%.3f logCgeom=%.3f' % (fit_res,Mf,lcg))
print('ALL_GATES_PASS')
