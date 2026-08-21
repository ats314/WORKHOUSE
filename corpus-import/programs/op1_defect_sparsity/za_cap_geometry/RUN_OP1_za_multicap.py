#!/usr/bin/env python3
# Multi-cap cap-ratio rate certification (A != empty): completes F037's bare-cap
# result.  CLAIM (proved via Varadhan/Laplace in the note):
#   lim_{kappa->inf} -(1/kappa) log nu(C_p | C_A) = Delta_p(A) = h(A)-h(A∪{p}),
# the TRUE height-drop, for any incident cap set A.  (vMF rate function is
# I(u)=1-m·u; nu(C_A)~e^{-k(1-h(A))}, nu(C_p∩C_A)~e^{-k(1-h(A∪p))}, ratio~e^{-k Delta_p}.)
# Here we CERTIFY the rate numerically by vMF Monte Carlo restricted to C_A over a
# kappa-ladder, for several A!=empty geometries of differing active-set codimension.
# One-shot (no edits): VM mount won't refresh edited paths.
import json, math, os
import numpy as np
rng = np.random.default_rng(20260612)

# ---- cap solver (hardened, from za_cert_v5) ----
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

def runit(n):
    v=rng.standard_normal((n,4)); return v/np.linalg.norm(v,axis=1,keepdims=True)

# ---- batched vMF(m,kappa) sampler on S^3 ----
def vmf(m,kappa,N):
    if kappa<1e-8:
        V=rng.standard_normal((N,4)); return V/np.linalg.norm(V,axis=1,keepdims=True)
    p=4; pm=p-1
    b=(-2*kappa+math.sqrt(4*kappa*kappa+pm*pm))/pm
    x0=(1-b)/(1+b); c=kappa*x0+pm*math.log(1-x0*x0)
    w=np.empty(N); fill=0
    while fill<N:
        M=int((N-fill)*1.6)+16
        z=rng.beta(pm/2.0,pm/2.0,M)
        wc=(1-(1+b)*z)/(1-(1-b)*z)
        logu=np.log(rng.random(M))
        acc=kappa*wc+pm*np.log(np.clip(1-x0*wc,1e-300,None))-c>=logu
        wa=wc[acc]; take=min(len(wa),N-fill); w[fill:fill+take]=wa[:take]; fill+=take
    Abasis=rng.standard_normal((4,3)); Abasis=Abasis-np.outer(m,m@Abasis)
    Q,_=np.linalg.qr(Abasis)              # 4x3 orthonormal cols ⊥ m
    g=rng.standard_normal((N,3)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    perp=g@Q.T
    return w[:,None]*m + np.sqrt(np.clip(1-w*w,0,None))[:,None]*perp

# ---- pick A!=empty geometries with good event + samplable C_A ----
KAPPAS=[6.,10.,15.,21.,28.,37.]
geoms=[]
tries=0
while len(geoms)<4 and tries<200000:
    tries+=1
    k=int(rng.integers(1,5)); m=runit(1)[0]; n_p=runit(1)[0]; A=runit(k)
    a=float(rng.uniform(0.2,0.8))
    uA,hA,act=solve(m,A,a)
    if uA is None: continue
    chi0=float(uA@n_p)-a
    if chi0<=0.02: continue
    Aa=np.vstack([A,n_p[None,:]]); uAp,hAp,actp=solve(m,Aa,a)
    if uAp is None: continue
    Dp=hA-hAp
    if Dp<0.05 or Dp>0.30: continue
    # require C_A to hold appreciable vMF mass at the top kappa (samplable)
    U=vmf(m,KAPPAS[-1],200000)
    inA=np.ones(len(U),bool)
    for nr in A: inA &= (U@nr<=a)
    fracA=inA.mean()
    if fracA<0.02: continue
    if any(abs(g['Dp']-Dp)<0.01 and g['k']==k for g in geoms): continue
    geoms.append({'m':m,'n_p':n_p,'A':A,'a':a,'k':k,'Dp':float(Dp),
                  'act_size':len(act),'actp_size':len(actp),'chi0':float(chi0)})

assert len(geoms)>=3, f'only found {len(geoms)} geometries'

# ---- certify the rate for each geometry ----
results=[]; worst_rate_err=0.0
for g in geoms:
    m=g['m'];n_p=g['n_p'];A=g['A'];a=g['a'];Dp=g['Dp']
    negs=[]
    for kap in KAPPAS:
        U=vmf(m,kap,3000000)
        inA=np.ones(len(U),bool)
        for nr in A: inA &= (U@nr<=a)
        inAp = inA & (U@n_p<=a)
        nA=int(inA.sum()); nAp=int(inAp.sum())
        ratio=(nAp/nA) if nA>0 else float('nan')
        negs.append(-math.log(ratio) if ratio>0 else float('nan'))
    negs=np.array(negs); ka=np.array(KAPPAS)
    good=np.isfinite(negs)
    # 3-param fit  neg = kappa*Dpfit - M log kappa - c  (Dp free)
    Am=np.vstack([ka[good],-np.log(ka[good]),-np.ones(good.sum())]).T
    co,*_=np.linalg.lstsq(Am,negs[good],rcond=None)
    Dp_fit,M_fit,cfit=co
    rate_err=abs(Dp_fit-Dp)
    worst_rate_err=max(worst_rate_err,rate_err)
    results.append({'k':g['k'],'act_size':g['act_size'],'actp_size':g['actp_size'],
                    'Dp_solver':Dp,'Dp_fit':float(Dp_fit),'M_prefactor':float(M_fit),
                    'chi0':g['chi0'],'kappas':KAPPAS,'neglog':[None if not np.isfinite(x) else float(x) for x in negs]})

# GATE G-ZB1: fitted rate matches the solver height-drop Delta_p(A) for every geometry
assert worst_rate_err<0.02, f'GATE FAIL G-ZB1: rate err {worst_rate_err}'

out={'gates':'G-ZB1 PASS (multi-cap rate = Delta_p(A))',
     'claim':'nu(C_p|C_A) ~ C kappa^{-M} e^{-kappa Delta_p(A)} for A!=empty; rate = true height-drop',
     'worst_rate_err':worst_rate_err,'n_geoms':len(geoms),'geometries':results}
here=os.path.dirname(os.path.abspath(__file__))
json.dump(out,open(os.path.join(here,'CERT_OP1_za_multicap.json'),'w'),indent=1)
print('G-ZB1 (multi-cap rate = Delta_p(A)): PASS  worst rate err %.4f' % worst_rate_err)
for r in results:
    print('  k=%d act=%d/%d  Dp_solver=%.4f  Dp_fit=%.4f  M=%.2f  chi0=%.3f'
          % (r['k'],r['act_size'],r['actp_size'],r['Dp_solver'],r['Dp_fit'],r['M_prefactor'],r['chi0']))
print('ALL_GATES_PASS')
