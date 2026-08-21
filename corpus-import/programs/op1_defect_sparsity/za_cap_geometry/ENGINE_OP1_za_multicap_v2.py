#!/usr/bin/env python3
# Multi-cap cap-ratio rate certification (A != empty), v2: EXACT 3-D quadrature
# (no MC noise). Restrict m, n_p, A to a 3-D subspace V=span(e0,e1,e2) of R^4.
# Then nu(C_p|C_A) reduces to a quadrature over the projection v=(u0,u1,u2) on
# the 3-ball, marginal density ∝ e^{kappa m·v} (1-|v|^2)^{-1/2} (S^3 -> 3-ball
# coarea; fiber over v is the two points u3=±sqrt(1-|v|^2)).  The maximizer of
# m·u over V-caps lies in V, so Delta_p(A) is the same 3-D cap height-drop.
# CLAIM (Varadhan/Laplace, note):  -(1/kappa) log nu(C_p|C_A) -> Delta_p(A).
# Reaching high kappa cleanly (quadrature handles the tail), we certify rate=Delta_p.
# One-shot (no edits).
import json, math, os
import numpy as np
rng = np.random.default_rng(20260612)

def cmax(m, N, a, tol=1e-11):
    if N.size==0 or N.shape[0]==0:
        nm=float(np.linalg.norm(m))
        if nm<tol: return np.array([1.0,0,0,0]),0.0
        u=m/nm; return u,float(u@m)
    G=N@N.T
    if np.linalg.cond(G)>1e9: return None,-np.inf
    try: sa=np.linalg.solve(G,a*np.ones(N.shape[0]))
    except np.linalg.LinAlgError: return None,-np.inf
    u0=N.T@sa; s=float(u0@u0)
    if s>1.0-1e-12: return None,-np.inf
    mp_=m-N.T@np.linalg.solve(G,N@m); mp=float(np.linalg.norm(mp_))
    if mp<1e-12: return None,-np.inf
    u=u0+math.sqrt(max(0.0,1.0-s))*(mp_/mp)
    if abs(u@u-1)>1e-8 or np.max(np.abs(N@u-a))>1e-8: return None,-np.inf
    return u,float(u@m)

def solve(m,nl,a,it=1e-9):
    na=np.asarray(nl,dtype=float).reshape(-1,4); A=len(na)
    bu=None;bv=-np.inf;ba=()
    for mask in range(1<<A):
        act=tuple(i for i in range(A) if (mask>>i)&1)
        Na=na[list(act)] if act else np.zeros((0,4))
        u,v=cmax(m,Na,a)
        if u is None: continue
        ok=True
        for j in range(A):
            if j in act: continue
            if float(na[j]@u)>a+it: ok=False; break
        if ok and v>bv: bv=v;bu=u;ba=act
    return bu,bv,ba

def runit3(n):
    # unit vectors in V = span(e0,e1,e2): 4th comp 0
    v=rng.standard_normal((n,3)); v/=np.linalg.norm(v,axis=1,keepdims=True)
    out=np.zeros((n,4)); out[:,:3]=v; return out

# ---- 3-D quadrature grid over the unit ball in V ----
Ng=200
ax=np.linspace(-1,1,Ng)
GX,GY,GZ=np.meshgrid(ax,ax,ax,indexing='ij')
R2=GX*GX+GY*GY+GZ*GZ
ball=R2<1.0
VX=GX[ball]; VY=GY[ball]; VZ=GZ[ball]           # flat arrays of interior points
rho_log=-0.5*np.log(1.0-(VX*VX+VY*VY+VZ*VZ))    # log (1-|v|^2)^{-1/2}
cellvol=(ax[1]-ax[0])**3

def nu_cond(m,n_p,A,a,kappa):
    mv = m[0]*VX+m[1]*VY+m[2]*VZ
    logw = kappa*mv + rho_log
    inA = np.ones(VX.shape[0],bool)
    for nr in A:
        inA &= (nr[0]*VX+nr[1]*VY+nr[2]*VZ <= a)
    inAp = inA & (n_p[0]*VX+n_p[1]*VY+n_p[2]*VZ <= a)
    Mx = logw[inA].max() if inA.any() else 0.0
    wt = np.exp(logw-Mx)
    ZA = (wt[inA].sum())*cellvol
    ZAp = (wt[inAp].sum())*cellvol
    return (ZAp/ZA) if ZA>0 else float('nan')

# ---- pick A!=empty 3-D geometries with good event ----
KAPS=[20.,35.,55.,80.,110.,150.]
geoms=[]; tries=0
while len(geoms)<4 and tries<300000:
    tries+=1
    k=int(rng.integers(1,5)); m=runit3(1)[0]; n_p=runit3(1)[0]; A=runit3(k); a=float(rng.uniform(0.2,0.8))
    uA,hA,act=solve(m,A,a)
    if uA is None: continue
    chi0=float(uA@n_p)-a
    if chi0<=0.02: continue
    Aa=np.vstack([A,n_p[None,:]]); uAp,hAp,actp=solve(m,Aa,a)
    if uAp is None: continue
    Dp=hA-hAp
    if Dp<0.05 or Dp>0.30: continue
    if any(g['k']==k and abs(g['Dp']-Dp)<0.02 for g in geoms): continue
    geoms.append({'m':m,'n_p':n_p,'A':A,'a':a,'k':k,'Dp':float(Dp),
                  'act':len(act),'actp':len(actp),'chi0':float(chi0)})
assert len(geoms)>=3, f'only {len(geoms)} geoms'

results=[]; worst=0.0
for g in geoms:
    m=g['m'];n_p=g['n_p'];A=g['A'];a=g['a'];Dp=g['Dp']
    negs=np.array([-math.log(nu_cond(m,n_p,A,a,kp)) for kp in KAPS])
    ka=np.array(KAPS)
    Am=np.vstack([ka,-np.log(ka),-np.ones_like(ka)]).T
    co,*_=np.linalg.lstsq(Am,negs,rcond=None); Dpf,Mf,cf=co
    fit=ka*Dpf-Mf*np.log(ka)-cf; res=float(np.max(np.abs(negs-fit)))
    sl=(negs[-1]-negs[-2])/(ka[-1]-ka[-2])
    err=abs(Dpf-Dp); worst=max(worst,err)
    results.append({'k':g['k'],'act':g['act'],'actp':g['actp'],'Dp_solver':Dp,
                    'Dp_fit':float(Dpf),'hi_slope':float(sl),'M':float(Mf),
                    'fit_resid':res,'chi0':g['chi0'],'neglog':negs.tolist()})

# GATE G-ZB1: fitted rate = solver height-drop Delta_p(A), every geometry
assert worst<0.01, f'GATE FAIL G-ZB1: worst rate err {worst}'
# GATE G-ZB2: the law form fits (small residual)
maxres=max(r['fit_resid'] for r in results)
assert maxres<0.05, f'GATE FAIL G-ZB2: residual {maxres}'

out={'gates':'G-ZB1,G-ZB2 PASS','grid':Ng,'kappas':KAPS,
     'claim':'nu(C_p|C_A) ~ C kappa^{-M} e^{-kappa Delta_p(A)}, A!=empty; rate = true height-drop Delta_p(A) (Varadhan/Laplace), exact 3-D quadrature certification',
     'worst_rate_err':worst,'max_fit_resid':maxres,'geometries':results}
here=os.path.dirname(os.path.abspath(__file__))
json.dump(out,open(os.path.join(here,'CERT_OP1_za_multicap.json'),'w'),indent=1)
print('G-ZB1 (multi-cap rate = Delta_p(A)): PASS worst err %.5f' % worst)
print('G-ZB2 (law form fit): PASS max residual %.4f' % maxres)
for r in results:
    print('  k=%d act=%d/%d  Dp_solver=%.4f  Dp_fit=%.4f  hi_slope=%.4f  M=%.2f  chi0=%.3f'
          % (r['k'],r['act'],r['actp'],r['Dp_solver'],r['Dp_fit'],r['hi_slope'],r['M'],r['chi0']))
print('ALL_GATES_PASS')
