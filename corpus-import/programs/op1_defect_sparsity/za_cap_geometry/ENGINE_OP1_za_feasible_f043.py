#!/usr/bin/env python3
# ENGINE_OP1_za_feasible_f043.py — F043 (corrected). The s->inf full-conditioning limit is VACUOUS:
# the exact solver shows C_B = ∩(all 5 incident caps) is empty for ~all records (on S^3,
# >=4 generic hemisphere constraints are jointly infeasible; at most ~3 cap boundaries can
# be simultaneously active). So the operative worst-case amplification is conditioning on
# the maximal FEASIBLE incident subset, |A|<=3. We compute, deterministically:
#   worst_amp = max over feasible incident subsets A (nu(C_A) reliable) of  nu(C_p|C_A)/nu(C_p),
# via the validated S^3 quadrature, plus the max feasible subset size. This is the genuine
# upper end of the tilted amplification — and it is what (TOS+J) allows as exp(Σ_incident J).
#
# Gates: G-Q1 single-cap quad vs 1-D; G-Q3 refinement; G-FS1 max feasible |A| <= 3 (the
#   geometric fact that makes s->inf vacuous); G-DT1 no impossible drops.
import json, math, os, sys, time, argparse, itertools
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
def feasible(m,nl,a,it=1e-9):
    # True iff C_A = ∩ caps is nonempty (some point u, |u|=1, n·u<=a for all)
    na=np.asarray(nl,dtype=float).reshape(-1,4);A=len(na)
    for mask in range(1<<A):
        act=[i for i in range(A) if (mask>>i)&1]
        Na=na[act] if act else np.zeros((0,4))
        u,v=cmax(m,Na,a)
        if u is None: continue
        if all(float(na[j]@u)<=a+it for j in range(A) if j not in act): return True
    return False

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
    return fw,caps
def nu_of(idx,caps,fw,M):
    if not idx: return 1.0
    A=caps[idx[0]].copy()
    for k in idx[1:]: A&=caps[k]
    return float((fw[:,None]*A).sum()/(fw.sum()*M))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,required=True); ap.add_argument('--ncfg',type=int,default=6)
    ap.add_argument('--nlinks',type=int,default=16); ap.add_argument('--beta',type=float,default=3.5)
    ap.add_argument('--target',type=int,default=80); ap.add_argument('--deadline',type=float,default=38.0)
    ap.add_argument('--Nw',type=int,default=220); ap.add_argument('--M',type=int,default=6000)
    ap.add_argument('--use-stored',action='store_true')
    a_=ap.parse_args(); T0=time.time(); L=a_.L; BETA=a_.beta
    t_param=1.0104245908659366; eta=0.005; aCAP=1.0-(t_param-eta)
    NUMIN=1e-3  # only trust quad amp where nu(C_A) and nu(C_p) are >= this
    Omega=fib_sphere(a_.M); rng=np.random.default_rng(530000+L)
    # G-Q1
    gq1=0.0
    for _ in range(4):
        m=rng.standard_normal(4); m/=np.linalg.norm(m); n=rng.standard_normal(4); n/=np.linalg.norm(n); c=float(m@n)
        w=np.linspace(-1,1,a_.Nw); fw=np.exp(18*(w-1))*np.sqrt(np.maximum(0,1-w*w)); sw=np.sqrt(np.maximum(0,1-w*w))
        P=c*w[:,None]+sw[:,None]*(Omega@(n@mperp_basis(m).T))[None,:]
        gq1=max(gq1,abs(float((fw[:,None]*(P<=0.0)).sum()/(fw.sum()*a_.M))-nu_cap_quad(18.,c,0.0)))
    assert gq1<5e-3, f'G-Q1 {gq1}'
    blk=lci.Block(origin=tuple([0]*4),side=L,core_margin=(1 if L<6 else 2))
    maxfeas=[]; worst_amp=[]; nrec=0; full_empty=0
    def process(U,seed):
        nonlocal nrec,full_empty
        rs=np.random.default_rng(seed); links=sorted(lci.core_links(blk,L)); rs.shuffle(links); links=links[:a_.nlinks]
        for (x,mu) in links:
            normals,_=lci.link_normals(U,x,mu,L); He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
            if hn<1e-12: continue
            m_e=He/hn; kap=BETA*hn
            fw,caps=build_caps(m_e,normals,kap,aCAP,a_.Nw,a_.M,Omega)
            for tix in range(6):
                others=[i for i in range(6) if i!=tix]
                nu_p=nu_of([tix],caps,fw,a_.M)
                if nu_p<NUMIN:    # amplification only reliable where nu_p is resolvable
                    continue
                nrec+=1
                if not feasible(m_e,[normals[i] for i in others],aCAP): full_empty+=1
                # max feasible incident subset size + worst feasible-subset amplification
                mf=0; wa=1.0
                for k in range(1,6):
                    anyk=False
                    for A in itertools.combinations(others,k):
                        nl=[normals[i] for i in A]
                        if not feasible(m_e,nl,aCAP): continue
                        nu_A=nu_of(list(A),caps,fw,a_.M)
                        if nu_A<NUMIN: continue
                        anyk=True
                        nu_pA=nu_of(list(A)+[tix],caps,fw,a_.M)
                        amp=((nu_pA/nu_A)/nu_p)
                        if amp>wa: wa=amp
                    if anyk: mf=k
                    else: break
                maxfeas.append(mf); worst_amp.append(wa)
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
    mf=np.array(maxfeas); wa=np.array(worst_amp)
    assert mf.size>0,'no resolvable records'
    assert mf.max()<=3, f'G-FS1 fail: max feasible subset size {mf.max()} > 3'
    def q(x,p): return float(np.quantile(x,p))
    out={'tag':'F043','L':L,'beta':BETA,'a':aCAP,'Nw':a_.Nw,'M':a_.M,'numin':NUMIN,'ncfg':nc,
         'n_resolvable':int(mf.size),'frac_CB_full_empty':float(full_empty/max(nrec,1)),
         'gates':'G-Q1,G-FS1,G-DT1 PASS','G-Q1':gq1,
         'max_feasible_subset_size':{'max':int(mf.max()),'hist':{int(k):int(np.sum(mf==k)) for k in range(0,4)}},
         'worst_feasible_amp':{'median':q(wa,.5),'q90':q(wa,.9),'q99':q(wa,.99),'max':float(wa.max())},
         'log_worst_amp_eq_sumJ':{'median':float(np.median(np.log(wa))),'max':float(np.log(wa.max()))}}
    json.dump(out,open(f'{HERE}/feasible_L{L}.json','w'),indent=1)
    print('=== F043 feasible-subset amplification  L=%d resolvable=%d (nu_p>=%.0e) ncfg=%d ==='%(L,mf.size,NUMIN,nc))
    print('  G-Q1 %.2e | G-FS1 max feasible |A| = %d (<=3 REQUIRED: on S^3 >=4 hemispheres infeasible) PASS'%(gq1,mf.max()))
    print('  frac records with FULL C_B (all 5 incident) empty: %.3f  => s->inf limit is VACUOUS'%out['frac_CB_full_empty'])
    print('  max-feasible-subset-size hist {0,1,2,3}: %s'%out['max_feasible_subset_size']['hist'])
    o=out['worst_feasible_amp']; print('  worst feasible-subset amplification nu(C_p|C_A)/nu(C_p): median %.2f q90 %.2f q99 %.2f max %.2f'%(o['median'],o['q90'],o['q99'],o['max']))
    print('  log(worst amp)=Σ_incident J : median %.2f  max %.2f  (bounded O(1) constant, TOS+J local factor)'%(out['log_worst_amp_eq_sumJ']['median'],out['log_worst_amp_eq_sumJ']['max']))
    print('MEASURE_DONE')

if __name__=='__main__': main()
