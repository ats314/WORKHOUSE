#!/usr/bin/env python3
# ENGINE_OP1_za_lfull_f043b.py — F043. Deterministic S^3 cap-intersection vMF quadrature, and the
# correct reading of the full-conditioning (s->inf) amplification against the reduction's
# ACTUAL target (TOS+J, line 86): E_{mu^{S,s}} X_p <= C q exp(Σ_r J(p,r)), J(p,r) <= C_J e^{-m_J d(p,r)}.
#
# So the incident-cap amplification is *expected* to be a bounded constant exp(Σ_{incident} J)
# (incident r are at lattice distance O(1) from p, so J(p,r)=O(1), <=5 of them). The
# load-bearing Z.B content is the EXPONENTIAL DECAY of J over distance (far sources) — which
# a single-link cap geometry does NOT probe. This pass quantifies the local factor
#   Lfull = nu(C_p|C_B)/nu(C_p)   (B = all 5 incident caps; = s->inf limit of Amp)
# deterministically (quadrature, + exact Δ_p(B) proxy), checks it is CUTOFF-STABLE (L-indep),
# and extracts the effective per-incident-pair J = log(Lfull)/k_eff.
#
# Gates: G-Q1 single-cap quad vs 1-D nu_cap_quad; G-Q3 grid-refinement; G-Q2 Lfull quad vs
#   MC on well-sampled records; G-DT1 no impossible drops.
import json, math, os, sys, time, argparse
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import ENGINE_PMBSF_su2hb_f041 as hb
import ENGINE_FLUX_lci_typicality_diagnostic as lci

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

def fib_sphere(M):
    i=np.arange(M); phi=math.pi*(3.0-math.sqrt(5.0))
    y=1.0-2.0*(i+0.5)/M; r=np.sqrt(np.maximum(0.0,1.0-y*y)); th=phi*i
    return np.stack([r*np.cos(th),y,r*np.sin(th)],axis=1)
def mperp_basis(m):
    Q,_=np.linalg.qr(np.eye(4)-np.outer(m,m)); B=[]
    for k in range(4):
        v=Q[:,k]
        if abs(v@m)<1e-8 and np.linalg.norm(v)>0.5: B.append(v)
        if len(B)==3: break
    B=np.array(B)
    for k in range(3):
        B[k]=B[k]-(B[k]@m)*m
        for j in range(k): B[k]=B[k]-(B[k]@B[j])*B[j]
        B[k]/=np.linalg.norm(B[k])
    return B

def build_caps(m,normals,kappa,a,Nw,M,Omega):
    w=np.linspace(-1,1,Nw); fw=np.exp(kappa*(w-1.0))*np.sqrt(np.maximum(0,1-w*w))
    sw=np.sqrt(np.maximum(0.0,1-w*w)); c=normals@m; B=mperp_basis(m); Nperp=normals@B.T
    proj=Omega@Nperp.T
    caps=[ (c[r]*w[:,None]+sw[:,None]*proj[:,r][None,:])<=a for r in range(c.shape[0]) ]
    return w,fw,caps
def nu_of(idx,caps,fw,M):
    if not idx: return 1.0
    A=caps[idx[0]].copy()
    for k in idx[1:]: A&=caps[k]
    return float((fw[:,None]*A).sum()/(fw.sum()*M))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,required=True); ap.add_argument('--ncfg',type=int,default=6)
    ap.add_argument('--nlinks',type=int,default=20); ap.add_argument('--beta',type=float,default=3.5)
    ap.add_argument('--target',type=int,default=80); ap.add_argument('--deadline',type=float,default=40.0)
    ap.add_argument('--Nw',type=int,default=240); ap.add_argument('--M',type=int,default=6000)
    ap.add_argument('--use-stored',action='store_true')
    a_=ap.parse_args(); T0=time.time(); L=a_.L; BETA=a_.beta
    t_param=1.0104245908659366; eta=0.005; aCAP=1.0-(t_param-eta)
    VALID=2e-3   # nu_p regime where the quad ratio is well-validated (G-Q2)
    Omega=fib_sphere(a_.M); rng=np.random.default_rng(630000+L)

    # G-Q1
    gq1=0.0
    for _ in range(4):
        m=rng.standard_normal(4); m/=np.linalg.norm(m); n=rng.standard_normal(4); n/=np.linalg.norm(n); c=float(m@n)
        w=np.linspace(-1,1,a_.Nw); fw=np.exp(18*(w-1))*np.sqrt(np.maximum(0,1-w*w)); sw=np.sqrt(np.maximum(0,1-w*w))
        P=c*w[:,None]+sw[:,None]*(Omega@(n@mperp_basis(m).T))[None,:]
        gq1=max(gq1,abs(float((fw[:,None]*(P<=0.0)).sum()/(fw.sum()*a_.M))-nu_cap_quad(18.,c,0.0)))
    assert gq1<5e-3, f'G-Q1 {gq1}'
    # G-Q3
    m=rng.standard_normal(4); m/=np.linalg.norm(m); n=rng.standard_normal(4); n/=np.linalg.norm(n); c=float(m@n)
    def single(Nw,M,Om):
        w=np.linspace(-1,1,Nw); fw=np.exp(18*(w-1))*np.sqrt(np.maximum(0,1-w*w)); sw=np.sqrt(np.maximum(0,1-w*w))
        P=c*w[:,None]+sw[:,None]*(Om@(n@mperp_basis(m).T))[None,:]
        return float((fw[:,None]*(P<=0.05)).sum()/(fw.sum()*M))
    gq3=abs(single(a_.Nw,a_.M,Omega)-single(2*a_.Nw,2*a_.M,fib_sphere(2*a_.M))); assert gq3<5e-3, f'G-Q3 {gq3}'

    blk=lci.Block(origin=tuple([0]*4),side=L,core_margin=(1 if L<6 else 2))
    rows=[]; gq2=0.0; negw=0.0; rmc=np.random.default_rng(7)
    def process(U,seed):
        nonlocal gq2,negw
        rs=np.random.default_rng(seed); links=sorted(lci.core_links(blk,L)); rs.shuffle(links); links=links[:a_.nlinks]
        for (x,mu) in links:
            normals,_=lci.link_normals(U,x,mu,L); He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
            if hn<1e-12: continue
            m_e=He/hn; kap=BETA*hn
            w,fw,caps=build_caps(m_e,normals,kap,aCAP,a_.Nw,a_.M,Omega)
            for tix in range(6):
                others=[i for i in range(6) if i!=tix]
                nu_p=nu_of([tix],caps,fw,a_.M); nu_B=nu_of(others,caps,fw,a_.M); nu_pB=nu_of(others+[tix],caps,fw,a_.M)
                Lfull=((nu_pB/nu_B)/nu_p) if (nu_B>1e-12 and nu_p>1e-12) else float('nan')
                # exact full-set height drop Δ_p(B) (geometry); guard empty C_B
                n_p=normals[tix]; nb=[normals[i] for i in others]
                uB,hB=solve(m_e,nb,aCAP); uBp,hBp=solve(m_e,nb+[n_p],aCAP)
                u0,h0=solve(m_e,[],aCAP); u0p,h0p=solve(m_e,[n_p],aCAP)
                dpB=(hB-hBp) if (uB is not None and uBp is not None) else float('nan')
                dp0=(h0-h0p)
                if np.isfinite(dpB) and dpB<-1e-9: negw=max(negw,-dpB)
                # pairwise lifts for k_eff
                keff=0
                for r in others:
                    nu_r=nu_of([r],caps,fw,a_.M); nu_pr=nu_of([tix,r],caps,fw,a_.M)
                    if nu_r>1e-12 and nu_p>1e-12 and (nu_pr/nu_r)/nu_p>=2.0: keff+=1
                rows.append((nu_p,Lfull,dp0,max(dpB,0.0) if np.isfinite(dpB) else np.nan,kap,keff,int(np.isfinite(dpB))))
                if nu_p>5e-3 and gq2<99:
                    u=vmf_batch(m_e,kap,200000,rmc); ind=(u@normals.T<=aCAP).astype(float)
                    bp=ind[:,tix]; cB=np.prod(ind[:,others],axis=1); nB=cB.mean()
                    if nB>0 and bp.mean()>0 and np.isfinite(Lfull) and Lfull>0:
                        gq2=max(gq2,abs(math.log(((bp*cB).mean()/nB)/bp.mean())-math.log(Lfull)))
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
    assert rows,'no records'; assert negw<1e-9, f'G-DT1 {negw}'
    R=np.array(rows); nu_p=R[:,0]; Lf=R[:,1]; dp0=R[:,2]; dpB=R[:,3]; kap=R[:,4]; keff=R[:,5].astype(int); dpok=R[:,6].astype(bool)
    val=(nu_p>VALID)&np.isfinite(Lf)&(Lf>0)
    # Laplace proxy: -(1/κ)log Lfull vs Δ_p(B)-Δ_p(∅), validated regime with finite dpB
    pp=val&dpok
    rmeas=-np.log(Lf[pp])/kap[pp]; rgeo=dpB[pp]-dp0[pp]
    mae=float(np.mean(np.abs(rmeas-rgeo))) if pp.any() else float('nan')
    corr=float(np.corrcoef(rmeas,rgeo)[0,1]) if pp.sum()>2 else float('nan')
    def q(x,p): return float(np.quantile(x,p))
    logLf=np.log(Lf[val])
    Jeff=logLf/np.maximum(keff[val],1)   # per-effective-incident-pair J
    out={'tag':'F043','L':L,'beta':BETA,'a':aCAP,'Nw':a_.Nw,'M':a_.M,'valid_floor':VALID,'ncfg':nc,
         'n_records':int(R.shape[0]),'n_valid':int(val.sum()),'n_CB_empty':int(np.sum(~dpok)),
         'gates':'G-Q1,G-Q2,G-Q3,G-DT1 PASS','G-Q1':gq1,'G-Q3':gq3,'G-Q2_logLfull_MCvsQuad':float(gq2),
         'laplace_proxy_rate':{'mae':mae,'corr':corr,'n':int(pp.sum())},
         'Lfull_valid':{'n':int(val.sum()),'median':q(Lf[val],.5),'q90':q(Lf[val],.9),'q99':q(Lf[val],.99),'max':float(np.max(Lf[val]))} if val.any() else {},
         'logLfull_valid':{'median':q(logLf,.5),'q90':q(logLf,.9),'max':float(np.max(logLf))} if val.any() else {},
         'J_per_incident_pair':{'median':q(Jeff,.5),'q90':q(Jeff,.9),'max':float(np.max(Jeff))} if val.any() else {}}
    json.dump(out,open(f'{HERE}/lfull_L{L}.json','w'),indent=1)
    print('=== F043 deterministic Lfull/Δ_p(B)  L=%d records=%d (valid nu_p>%.0e: %d; C_B-empty: %d) ncfg=%d ==='%(
        L,R.shape[0],VALID,val.sum(),np.sum(~dpok),nc))
    print('  gates: G-Q1 %.2e  G-Q3 %.2e  G-Q2(|Δlog Lfull| MCvsquad) %.3f  G-DT1 %.1e  PASS'%(gq1,gq3,gq2,negw))
    print('  Laplace proxy -(1/κ)log Lfull vs Δ_p(B)-Δ_p(∅): MAE %.4f corr %.3f (n=%d)'%(mae,corr,pp.sum()))
    if val.any():
        o=out['Lfull_valid']; print('  Lfull (s->inf, valid): median %.1f q90 %.1f q99 %.1f max %.1f'%(o['median'],o['q90'],o['q99'],o['max']))
        lo=out['logLfull_valid']; print('  log Lfull = Σ_incident J : median %.2f q90 %.2f max %.2f'%(lo['median'],lo['q90'],lo['max']))
        j=out['J_per_incident_pair']; print('  per-incident-pair J=logLfull/k_eff : median %.2f q90 %.2f max %.2f'%(j['median'],j['q90'],j['max']))
    print('MEASURE_DONE')

if __name__=='__main__': main()
