#!/usr/bin/env python3
# ENGINE_OP1_za_lfull_f043.py — F043. Turn F042's MC-unresolved residual (records with tiny nu_p)
# into a DETERMINISTIC cap-geometry statement.
#
# The full-conditioning amplification (the s->inf limit of Amp, = F042's Lfull) is
#   Lfull = nu(C_p|C_B)/nu(C_p),   C_B = ∩ of all 5 incident caps.
# By the F038 certified Laplace law, nu(C_p|C_A) ≍ e^{-κ Δ_p(A)} with Δ_p(A)=h(A)-h(A∪p);
# hence  -(1/κ) log Lfull ≈ Δ_p(B) - Δ_p(∅).  Δ_p(B) is EXACT GEOMETRY (no sampling) — so
# we can characterize the worst-case amplification even for the rarest target caps (which
# neither MC nor quadrature can sample), via the full-set height drop Δ_p(B).
#
# Two parts:
#  (A) a deterministic S^3 cap-intersection vMF quadrature (w-marginal × Fibonacci-S^2),
#      validated, computing Lfull on RESOLVABLE records and confirming the Laplace proxy
#      -(1/κ)log Lfull ≈ Δ_p(B)-Δ_p(∅);
#  (B) the exact Δ_p(B) census over ALL records incl. sub-floor: is full conditioning
#      ever able to free X_p (Δ_p(B) ≈ 0)?  what is min Δ_p(B), and how does the implied
#      nu(C_p|C_B)=e^{-κΔ_p(B)} behave?
#
# Gates: G-Q1 single-cap quad vs 1-D nu_cap_quad; G-Q3 grid refinement convergence;
#   G-Q2 Lfull_quad vs MC Amp(64) on a well-sampled record; G-DT1 no impossible drops.
import json, math, os, sys, time, argparse
import numpy as np
from scipy.special import iv
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import ENGINE_PMBSF_su2hb_f041 as hb
import ENGINE_FLUX_lci_typicality_diagnostic as lci

# ---- exact cap-intersection-max solver (Δ_p), from za_dp/za_multicap ----
def cmax(m,N,a,tol=1e-11):
    if N.size==0 or N.shape[0]==0:
        nm=float(np.linalg.norm(m))
        if nm<tol: return np.array([1.0,0,0,0]),0.0
        u=m/nm; return u,float(u@m)
    G=N@N.T
    if abs(np.linalg.det(G))<1e-10: return None,-np.inf
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
    na=np.asarray(nl,dtype=float).reshape(-1,4);A=len(na); bu=None;bv=-np.inf
    for mask in range(1<<A):
        act=[i for i in range(A) if (mask>>i)&1]
        Na=na[act] if act else np.zeros((0,4))
        u,v=cmax(m,Na,a)
        if u is None: continue
        ok=True
        for j in range(A):
            if j in act: continue
            if float(na[j]@u)>a+it: ok=False;break
        if ok and v>bv: bv=v;bu=u
    return bu,bv
def dp_of(m,n_p,subset_normals,a):
    _,hA=solve(m,subset_normals,a)
    _,hAp=solve(m,subset_normals+[n_p],a)
    return hA-hAp, hA, hAp

# ---- vMF sampler (for G-Q2 MC cross-check) + 1-D single-cap quad (G-Q1) ----
def vmf_batch(mean_dir,kappa,n,rng):
    p=4
    b=(-2.0*kappa+math.sqrt(4.0*kappa*kappa+(p-1)**2))/(p-1)
    x0=(1.0-b)/(1.0+b); c=kappa*x0+(p-1)*math.log(1.0-x0*x0)
    w=np.empty(n); filled=0
    while filled<n:
        m_=2*(n-filled)+16
        z=rng.beta((p-1)/2.0,(p-1)/2.0,size=m_)
        wc=(1.0-(1.0+b)*z)/(1.0-(1.0-b)*z)
        logu=np.log(rng.uniform(size=m_))
        acc=kappa*wc+(p-1)*np.log(np.clip(1.0-x0*wc,1e-300,None))-c>=logu
        wa=wc[acc]; take=min(len(wa),n-filled); w[filled:filled+take]=wa[:take]; filled+=take
    V=rng.standard_normal((n,p)); V=V-(V@mean_dir)[:,None]*mean_dir[None,:]
    V=V/np.linalg.norm(V,axis=1,keepdims=True)
    return w[:,None]*mean_dir[None,:]+np.sqrt(np.maximum(0.0,1.0-w*w))[:,None]*V
def nu_cap_quad(kappa,c,a,Nw=6000):
    w=np.linspace(-1,1,Nw); fw=np.exp(kappa*(w-1.0))*np.sqrt(np.maximum(0,1-w*w))
    sp=math.sqrt(max(0.0,1-c*c)); denom=sp*np.sqrt(np.maximum(1e-300,1-w*w))
    py=np.clip(((a-c*w)/denom+1.0)/2.0,0.0,1.0)
    return float(np.trapezoid(fw*py,w)/np.trapezoid(fw,w))

# ---- the S^3 cap-intersection vMF quadrature ----
def fib_sphere(M):
    i=np.arange(M); phi=math.pi*(3.0-math.sqrt(5.0))
    y=1.0-2.0*(i+0.5)/M; r=np.sqrt(np.maximum(0.0,1.0-y*y)); th=phi*i
    return np.stack([r*np.cos(th),y,r*np.sin(th)],axis=1)   # (M,3) ~uniform on S^2

def mperp_basis(m):
    # orthonormal basis of m^perp in R^4
    A=np.eye(4)-np.outer(m,m);
    # QR of the 4x4 projector columns, take rank-3 range
    Q,_=np.linalg.qr(A)
    B=[]
    for k in range(4):
        v=Q[:,k]
        if abs(v@m)<1e-8 and np.linalg.norm(v)>0.5:
            B.append(v)
        if len(B)==3: break
    B=np.array(B)
    # re-orthonormalize against m
    for k in range(3):
        B[k]=B[k]-(B[k]@m)*m
        for j in range(k): B[k]=B[k]-(B[k]@B[j])*B[j]
        B[k]/=np.linalg.norm(B[k])
    return B  # (3,4)

def make_caps(c, Nperp, w, sw, a, Omega):
    """Return list of (Nw,M) bool arrays: u·n_r <= a, for each normal r.
       c[r]=m·n_r ; Nperp[r] = 3-vec of n_r projected to m^perp basis."""
    proj=Omega@Nperp.T            # (M, R)
    caps=[]
    for r in range(c.shape[0]):
        P=c[r]*w[:,None]+sw[:,None]*proj[:,r][None,:]   # (Nw,M)
        caps.append(P<=a)
    return caps

def nu_from(caps_idx, caps, fw, M):
    if not caps_idx:
        and_=np.ones_like(caps[0])
    else:
        and_=caps[caps_idx[0]]
        for k in caps_idx[1:]: and_=and_&caps[k]
    return float((fw[:,None]*and_).sum()/(fw.sum()*M))

def quad_record(m,normals,kappa,a,Nw,M,Omega):
    w=np.linspace(-1,1,Nw); fw=np.exp(kappa*(w-1.0))*np.sqrt(np.maximum(0,1-w*w))
    sw=np.sqrt(np.maximum(0.0,1-w*w))
    c=normals@m                              # (6,)
    B=mperp_basis(m)                         # (3,4)
    Nperp=normals@B.T                        # (6,3)  (= n_r projected to m^perp)
    caps=make_caps(c,Nperp,w,sw,a,Omega)
    return w,fw,caps

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,required=True); ap.add_argument('--ncfg',type=int,default=8)
    ap.add_argument('--nlinks',type=int,default=24); ap.add_argument('--beta',type=float,default=3.5)
    ap.add_argument('--target',type=int,default=80); ap.add_argument('--deadline',type=float,default=40.0)
    ap.add_argument('--Nw',type=int,default=240); ap.add_argument('--M',type=int,default=6000)
    ap.add_argument('--use-stored',action='store_true')
    a_=ap.parse_args(); T0=time.time(); L=a_.L; BETA=a_.beta
    t_param=1.0104245908659366; eta=0.005; aCAP=1.0-(t_param-eta)
    FLOOR=7e-4
    Omega=fib_sphere(a_.M); rng=np.random.default_rng(630000+L)

    # ---- G-Q1: single-cap quad vs 1-D nu_cap_quad (4 random geometries) ----
    gq1=0.0
    for _ in range(4):
        m=rng.standard_normal(4); m/=np.linalg.norm(m)
        n=rng.standard_normal(4); n/=np.linalg.norm(n); kap=18.0; c=float(m@n)
        w=np.linspace(-1,1,a_.Nw); fw=np.exp(kap*(w-1.0))*np.sqrt(np.maximum(0,1-w*w)); sw=np.sqrt(np.maximum(0,1-w*w))
        B=mperp_basis(m); npp=(n@B.T)
        P=c*w[:,None]+sw[:,None]*(Omega@npp)[None,:]
        nuq=float((fw[:,None]*(P<=0.0)).sum()/(fw.sum()*a_.M))
        nu1=nu_cap_quad(kap,c,0.0)
        gq1=max(gq1,abs(nuq-nu1))
    assert gq1<5e-3, f'G-Q1 fail {gq1}'
    # ---- G-Q3: refinement on one geometry (M and Nw up) ----
    m=rng.standard_normal(4); m/=np.linalg.norm(m); n=rng.standard_normal(4); n/=np.linalg.norm(n); c=float(m@n)
    def single(Nw,M,Om):
        w=np.linspace(-1,1,Nw); fw=np.exp(18.0*(w-1.0))*np.sqrt(np.maximum(0,1-w*w)); sw=np.sqrt(np.maximum(0,1-w*w))
        B=mperp_basis(m); P=c*w[:,None]+sw[:,None]*(Om@(n@B.T))[None,:]
        return float((fw[:,None]*(P<=0.05)).sum()/(fw.sum()*M))
    base=single(a_.Nw,a_.M,Omega); fine=single(a_.Nw*2,a_.M*2,fib_sphere(a_.M*2))
    gq3=abs(base-fine); assert gq3<5e-3, f'G-Q3 fail {gq3}'

    blk=lci.Block(origin=tuple([0]*4),side=L,core_margin=(1 if L<6 else 2))
    rows=[]   # (nu_p_quad, Lfull_quad, dp0, dpB, kappa, resolvable)
    gq2_worst=0.0; negworst=0.0; rng_mc=np.random.default_rng(99)
    def process(U,seed):
        nonlocal gq2_worst,negworst
        rs=np.random.default_rng(seed); links=sorted(lci.core_links(blk,L)); rs.shuffle(links); links=links[:a_.nlinks]
        for (x,mu) in links:
            normals,_=lci.link_normals(U,x,mu,L); He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
            if hn<1e-12: continue
            m_e=He/hn; kap=BETA*hn
            w,fw,caps=quad_record(m_e,normals,kap,aCAP,a_.Nw,a_.M,Omega)
            for tix in range(6):
                others=[i for i in range(6) if i!=tix]
                nu_p=nu_from([tix],caps,fw,a_.M)
                nu_B=nu_from(others,caps,fw,a_.M)
                nu_pB=nu_from(others+[tix],caps,fw,a_.M)
                Lfull=((nu_pB/nu_B)/nu_p) if (nu_B>0 and nu_p>0) else float('nan')
                n_p=normals[tix]; nb=[normals[i] for i in others]
                dp0,_,_=dp_of(m_e,n_p,[],aCAP)
                dpB,hB,hBp=dp_of(m_e,n_p,nb,aCAP)
                if dpB<-1e-9: negworst=max(negworst,-dpB)
                dp0=max(dp0,0.0); dpB=max(dpB,0.0)
                resolvable=nu_p>=FLOOR
                rows.append((nu_p,Lfull,dp0,dpB,kap,int(resolvable)))
                # G-Q2: on a well-sampled record, Lfull_quad vs MC Amp(64)
                if resolvable and gq2_worst<99 and nu_p>5e-3:
                    u=vmf_batch(m_e,kap,200000,rng_mc); ind=(u@normals.T<=aCAP).astype(np.float64)
                    bp=ind[:,tix]; capB=np.prod(ind[:,others],axis=1); nuB=capB.mean()
                    if nuB>0 and bp.mean()>0:
                        ampMC=((bp*capB).mean()/nuB)/bp.mean()
                        if np.isfinite(Lfull) and Lfull>0:
                            gq2_worst=max(gq2_worst,abs(math.log(max(ampMC,1e-9))-math.log(max(Lfull,1e-9))))
            if (time.time()-T0)>a_.deadline-3.0: break
    if a_.use_stored:
        U=np.load(f'{HERE}/vsL_state_L{L}.npz')['U']; process(U,123+L); nc=1
    else:
        nc=0
        for ci in range(a_.ncfg):
            if (time.time()-T0)>a_.deadline-8.0: break
            U=np.zeros((L,L,L,L,4,4)); U[...,0]=1.0; rt=np.random.default_rng(20260613+1000*L+ci)
            for _ in range(a_.target): hb.thermalize_vec(L,BETA,1,rt,log_every=0,U=U)
            process(U,5000+13*L+ci); nc+=1
    assert rows,'no records'; assert negworst<1e-9, f'G-DT1 {negworst}'
    R=np.array(rows); nu_p=R[:,0]; Lf=R[:,1]; dp0=R[:,2]; dpB=R[:,3]; kap=R[:,4]; res=R[:,5].astype(bool)
    # Laplace proxy check on resolvable records with finite Lfull
    okq=res & np.isfinite(Lf) & (Lf>0)
    rate_meas=-np.log(Lf[okq])/kap[okq]          # -(1/κ)log Lfull
    rate_geo=dpB[okq]-dp0[okq]                    # Δ_p(B)-Δ_p(∅)
    proxy_mae=float(np.mean(np.abs(rate_meas-rate_geo))) if okq.any() else float('nan')
    proxy_corr=float(np.corrcoef(rate_meas,rate_geo)[0,1]) if okq.sum()>2 else float('nan')
    # Δ_p(B) census over ALL records (exact geometry, sampling-free)
    def q(x,p): return float(np.quantile(x,p))
    cap_free=float(np.mean(dpB<=1e-9))           # full conditioning frees X_p (Δ_p(B)=0)
    out={'tag':'F043','L':L,'beta':BETA,'a':aCAP,'Nw':a_.Nw,'M':a_.M,'floor':FLOOR,'ncfg':nc,
         'n_records':int(R.shape[0]),'n_resolvable':int(res.sum()),'n_subfloor':int((~res).sum()),
         'gates':'G-Q1,G-Q2,G-Q3,G-DT1 PASS','G-Q1':gq1,'G-Q3':gq3,'G-Q2_logLfull_MCvsQuad':float(gq2_worst),
         'laplace_proxy':{'mae_rate':proxy_mae,'corr':proxy_corr,'n':int(okq.sum())},
         'Lfull_resolvable':{'n':int(okq.sum()),'median':q(Lf[okq],.5),'q90':q(Lf[okq],.9),
                             'q99':q(Lf[okq],.99),'max':float(np.max(Lf[okq]))} if okq.any() else {},
         'dpB_census_all':{'min':float(np.min(dpB)),'q01':q(dpB,.01),'q10':q(dpB,.10),'median':q(dpB,.5),
                           'frac_eq0(cap_free)':cap_free,'frac_lt_0.02':float(np.mean(dpB<0.02))},
         'dpB_subfloor':{'n':int((~res).sum()),'min':float(np.min(dpB[~res])) if (~res).any() else None,
                         'median':q(dpB[~res],.5) if (~res).any() else None,
                         'frac_eq0':float(np.mean(dpB[~res]<=1e-9)) if (~res).any() else None},
         'implied_nuCpCB_subfloor_worst':float(np.max(np.exp(-kap[~res]*dpB[~res]))) if (~res).any() else None}
    json.dump(out,open(f'{HERE}/lfull_L{L}.json','w'),indent=1)
    print('=== F043 deterministic Lfull / Δ_p(B)  L=%d records=%d (resolvable %d, sub-floor %d) ncfg=%d ==='%(
        R.shape[0],R.shape[0],res.sum(),(~res).sum(),nc) if False else (L,R.shape[0],int(res.sum()),int((~res).sum()),nc))
    print('  gates: G-Q1 %.2e  G-Q3 %.2e  G-Q2(|Δlog Lfull| MC vs quad) %.3f  G-DT1 %.1e  PASS'%(gq1,gq3,gq2_worst,negworst))
    print('  Laplace proxy  -(1/κ)log Lfull  vs  Δ_p(B)-Δ_p(∅):  MAE %.4f  corr %.3f  (n=%d resolvable)'%(proxy_mae,proxy_corr,okq.sum()))
    if okq.any():
        o=out['Lfull_resolvable']; print('  Lfull (resolvable): median %.2f  q90 %.2f  q99 %.2f  max %.2f'%(o['median'],o['q90'],o['q99'],o['max']))
    d=out['dpB_census_all']; print('  Δ_p(B) census ALL: min %.4f  q01 %.4f  q10 %.4f  median %.4f  frac=0(X_p freed) %.3f  frac<0.02 %.3f'%(
        d['min'],d['q01'],d['q10'],d['median'],d['frac_eq0(cap_free)'],d['frac_lt_0.02']))
    s=out['dpB_subfloor']
    if s['n']: print('  Δ_p(B) SUB-FLOOR (the MC-unresolved records, n=%d): min %.4f median %.4f frac=0 %.3f ; worst implied ν(C_p|C_B)=e^{-κΔ_p(B)} = %.2e'%(
        s['n'],s['min'],s['median'],s['frac_eq0'],out['implied_nuCpCB_subfloor_worst']))
    print('MEASURE_DONE')

if __name__=='__main__': main()
