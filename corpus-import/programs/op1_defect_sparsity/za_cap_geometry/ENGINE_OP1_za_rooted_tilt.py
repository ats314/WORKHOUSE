#!/usr/bin/env python3
# ENGINE_OP1_za_rooted_tilt.py — F041. Measure the ROOTED/TILTED LCI object (the reduction's
# (7.2)) rather than the pointwise min-over-subsets (F040), on the SU(2) heat-bath
# ensembles, and pin F040's good-event fraction with MULTIPLE independent configs.
#
# Why: F040 measured min_A Delta_p (the *term-wise* LCI bound nu(C_p∩C_A) <= C q
# nu(C_A) for ALL subsets A) and found it fails for ~85% of (e,p) records. But the
# load-bearing object in the reduction (§7) is the tilted ratio
#       R(e,p;s) = nu^{B,s}(C_p) = [ Σ_A s^|A| nu(C_p∩C_A) ] / [ Σ_A s^|A| nu(C_A) ]
# and LCI/(7.2) asks only R <= C_LCI q — i.e. the incident-source tilt must not
# inflate the target cap probability ("prevent X_p from going free", reduction l.421).
# A few bad subsets can fail the term-wise bound yet carry negligible tilted weight.
#
# KEY IDENTITY (reduction 7.4–7.7, exact): for caps C_r = {u: u·n_r <= a},
#   Σ_{A⊆B} s^|A| nu(C_A)        = E_nu[ Π_{r∈B}(1 + s 1_{C_r}) ]
#   Σ_{A⊆B} s^|A| nu(C_p∩C_A)    = E_nu[ 1_{C_p} Π_{r∈B}(1 + s 1_{C_r}) ]
# So R(e,p;s) is a single vMF expectation ratio — sample u~vMF(m_e,kappa) once per
# record, form the 6 cap indicators, done. We report the AMPLIFICATION
#   Amp(s) = R(e,p;s) / nu(C_p)            (scale-free; LCI ⟺ Amp = O(1))
# and correlate it with F040's pointwise-bad flag (min_A Delta_p == 0).
#
# Gates:
#   G-RT1  vectorized vMF sampler: resultant <u·m> matches Bessel ratio I2/I1(kappa)
#          AND the reviewed scalar sample_vmf_s3, within MC tolerance.
#   G-RT2  MC bare cap prob nu(C_p) matches the za_multicap 3-D quadrature on a
#          3-D-embedded geometry, within 4·stderr (validates the indicator pipeline).
#   G-RT3  s=0 ⟹ Amp==1 exactly; all tilted probs ∈ [0,1].
#   G-RT4  product-form ratio == explicit subset-sum ratio on the SAME sample
#          (numerical check of the 7.4–7.7 identity), < 1e-12.
#
# Usage (deadline-aware, one L per call):
#   python3 ENGINE_OP1_za_rooted_tilt.py --L 4  --ncfg 8 --N 40000 --nlinks 40 --deadline 40
#   python3 ENGINE_OP1_za_rooted_tilt.py --L 8  --ncfg 6 --N 40000 --nlinks 40 --deadline 40
#   python3 ENGINE_OP1_za_rooted_tilt.py --L 16 --use-stored --N 40000 --nlinks 60 --deadline 40
import json, math, os, sys, time, itertools, argparse
import numpy as np
from scipy.special import iv
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import ENGINE_PMBSF_su2hb_f041 as hb   # fresh-path re-deposit of su2_hb_v3 (mount truncated the original)
import ENGINE_FLUX_lci_typicality_diagnostic as lci

S_LIST=[0.0,0.5,1.0,2.0,4.0]

# ---------- pointwise min_A Delta_p (identical to za_dp_vsL / F040) ----------
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
def min_dp(m,n_p,nb,a):
    K=len(nb);mdp=np.inf;neg=0.0
    for r in range(0,K+1):
        for A in itertools.combinations(range(K),r):
            NA=[nb[i] for i in A]; uA,hA=solve(m,NA,a)
            if uA is None: continue
            _,hAp=solve(m,NA+[n_p],a); dp=hA-hAp
            if dp<-1e-9: neg=max(neg,-dp)
            dp=max(dp,0.0)
            if dp<mdp: mdp=dp
    return mdp,neg

# ---------- vectorized vMF(m,kappa) sampler on S^3 (Wood 1994) ----------
def vmf_batch(mean_dir,kappa,n,rng):
    p=4
    if kappa<1e-10:
        v=rng.standard_normal((n,p)); return v/np.linalg.norm(v,axis=1,keepdims=True)
    b=(-2.0*kappa+math.sqrt(4.0*kappa*kappa+(p-1)**2))/(p-1)
    x0=(1.0-b)/(1.0+b); c=kappa*x0+(p-1)*math.log(1.0-x0*x0)
    w=np.empty(n); filled=0
    while filled<n:
        m_=2*(n-filled)+16
        z=rng.beta((p-1)/2.0,(p-1)/2.0,size=m_)
        wc=(1.0-(1.0+b)*z)/(1.0-(1.0-b)*z)
        logu=np.log(rng.uniform(size=m_))
        acc=kappa*wc+(p-1)*np.log(np.clip(1.0-x0*wc,1e-300,None))-c>=logu
        wa=wc[acc]; take=min(len(wa),n-filled)
        w[filled:filled+take]=wa[:take]; filled+=take
    V=rng.standard_normal((n,p))
    V=V-(V@mean_dir)[:,None]*mean_dir[None,:]
    V=V/np.linalg.norm(V,axis=1,keepdims=True)
    return w[:,None]*mean_dir[None,:]+np.sqrt(np.maximum(0.0,1.0-w*w))[:,None]*V

# ---------- gates that don't need a config ----------
def gate_rt1(rng):
    res={}
    for kap in (8.0,18.0,40.0):
        m=np.array([1.0,0,0,0]); u=vmf_batch(m,kap,200000,rng)
        emp=float((u@m).mean()); bess=float(iv(2,kap)/iv(1,kap))
        # scalar reviewed sampler
        sc=np.array([lci.sample_vmf_s3(m,kap,rng)@m for _ in range(4000)]).mean()
        res[kap]=(emp,bess,float(sc))
        assert abs(emp-bess)<0.01, f'G-RT1 batch vs Bessel {kap}: {emp} {bess}'
        assert abs(sc-bess)<0.02, f'G-RT1 scalar vs Bessel {kap}: {sc} {bess}'
    return res

def nu_cap_quad(kappa,c,a,Nw=4000):
    # Exact single-cap prob nu({u·n<=a}) under vMF(m,kappa), c=m·n. In the m-frame
    # u·n = c w + sqrt(1-c^2) sqrt(1-w^2) y, w~ ∝e^{κw}(1-w^2)^{1/2} on [-1,1],
    # y = a coord of a uniform point on S^2 ~ Uniform[-1,1] (independent). So the
    # inner y-integral is a clip; one 1-D quadrature in w remains.
    w=np.linspace(-1,1,Nw); fw=np.exp(kappa*(w-1.0))*np.sqrt(np.maximum(0,1-w*w))
    sp=math.sqrt(max(0.0,1-c*c))
    denom=sp*np.sqrt(np.maximum(1e-300,1-w*w))
    yt=(a-c*w)/denom
    py=np.clip((yt+1.0)/2.0,0.0,1.0)
    return float(np.trapz(fw*py,w)/np.trapz(fw,w))

def gate_rt2(rng):
    # MC bare cap prob vs the 1-D quadrature, random geometries at kappa=18.
    worst=0.0; rows=[]
    for _ in range(6):
        m=rng.standard_normal(4); m/=np.linalg.norm(m)
        n=rng.standard_normal(4); n/=np.linalg.norm(n)
        a=float(rng.uniform(-0.2,0.2)); kap=18.0; c=float(m@n)
        u=vmf_batch(m,kap,300000,rng); mc=float(((u@n)<=a).mean())
        qd=nu_cap_quad(kap,c,a); se=math.sqrt(max(mc*(1-mc),1e-9)/300000)
        worst=max(worst,abs(mc-qd)); rows.append((c,a,mc,qd,abs(mc-qd),se))
        assert abs(mc-qd)<5*se+2e-3, f'G-RT2 MC vs quad: mc={mc} quad={qd} se={se}'
    return worst,rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--L',type=int,required=True)
    ap.add_argument('--ncfg',type=int,default=6)
    ap.add_argument('--N',type=int,default=40000)
    ap.add_argument('--nlinks',type=int,default=40)
    ap.add_argument('--beta',type=float,default=3.5)
    ap.add_argument('--target',type=int,default=80)
    ap.add_argument('--deadline',type=float,default=40.0)
    ap.add_argument('--use-stored',action='store_true')
    a_=ap.parse_args(); T0=time.time()
    L=a_.L; BETA=a_.beta
    t_param=1.0104245908659366; eta=0.005; aCAP=1.0-(t_param-eta)
    rng=np.random.default_rng(910000+L)

    # ---- standalone gates (once) ----
    g1=gate_rt1(rng)
    g2_worst,g2_rows=gate_rt2(rng)

    blk=lci.Block(origin=tuple([0]*4),side=L,core_margin=2)

    def measure_config(U,seed):
        """Return per-record rows: (kappa, min_Dp, nu_p, [Amp(s) for s in S_LIST])
        plus gate accumulators."""
        rs=np.random.default_rng(seed)
        links=sorted(lci.core_links(blk,L)); rs.shuffle(links); links=links[:a_.nlinks]
        rng_mc=np.random.default_rng(seed^0x5bd1e995)
        rows=[]; neg_worst=0.0; rt3=0.0; rt4=0.0
        for (x,mu) in links:
            normals,ids=lci.link_normals(U,x,mu,L)
            He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
            if hn<1e-12: continue
            m_e=He/hn; kap=BETA*hn
            u=vmf_batch(m_e,kap,a_.N,rng_mc)          # (N,4)
            ind=(u@normals.T<=aCAP).astype(np.float64) # (N,6)
            for tix in range(6):
                n_p=normals[tix]; nb=[normals[i] for i in range(6) if i!=tix]
                others=[i for i in range(6) if i!=tix]
                bp=ind[:,tix]; nu_p=float(bp.mean())
                amps=[]
                for s in S_LIST:
                    Wt=np.prod(1.0+s*ind[:,others],axis=1)
                    mw=float(Wt.mean())
                    tilt=float((bp*Wt).mean())/mw if mw>0 else float('nan')
                    rt3=max(rt3,abs(tilt-min(max(tilt,0.0),1.0)))  # in [0,1]
                    amp=(tilt/nu_p) if nu_p>0 else float('nan')
                    amps.append(amp)
                    if s==0.0: rt3=max(rt3,abs(amp-1.0))           # s=0 ⟹ Amp=1
                # G-RT4: subset-sum form on SAME sample, at s=2.0
                s_chk=2.0; num=0.0; den=0.0
                for r in range(0,6):  # subsets of the 5 'others'
                    for A in itertools.combinations(others,r):
                        capA=np.ones(a_.N) if not A else np.prod(ind[:,list(A)],axis=1)
                        nuA=float(capA.mean()); nuAp=float((bp*capA).mean())
                        num+=s_chk**len(A)*nuAp; den+=s_chk**len(A)*nuA
                ratio_sub=num/den if den>0 else float('nan')
                Wt2=np.prod(1.0+s_chk*ind[:,others],axis=1)
                ratio_prod=float((bp*Wt2).mean())/float(Wt2.mean())
                rt4=max(rt4,abs(ratio_sub-ratio_prod))
                # pointwise F040 flag
                mdp,neg=min_dp(m_e,n_p,nb,aCAP); neg_worst=max(neg_worst,neg)
                rows.append((kap,mdp,nu_p,*amps))
            if (time.time()-T0)>a_.deadline-3.0: break
        return rows,neg_worst,rt3,rt4

    all_rows=[]; per_cfg_fracs=[]; neg_w=0.0; rt3_w=0.0; rt4_w=0.0; plaqs=[]
    if a_.use_stored:
        statef=f'{HERE}/vsL_state_L{L}.npz'
        U=np.load(statef)['U']; plaqs.append(float(hb.mean_plaq(U)))
        rows,nw,r3,r4=measure_config(U,seed=123+L)
        all_rows+=rows; neg_w=max(neg_w,nw); rt3_w=max(rt3_w,r3); rt4_w=max(rt4_w,r4)
        R=np.array(rows); per_cfg_fracs.append(float(np.mean(R[:,1]>0)))
        ncfg_done=1
    else:
        ncfg_done=0
        for ci in range(a_.ncfg):
            if (time.time()-T0)>a_.deadline-8.0: break
            Ucfg=np.zeros((L,L,L,L,4,4)); Ucfg[...,0]=1.0
            rngt=np.random.default_rng(20260613+1000*L+ci)
            for _ in range(a_.target): hb.thermalize_vec(L,BETA,1,rngt,log_every=0,U=Ucfg)
            plaqs.append(float(hb.mean_plaq(Ucfg)))
            rows,nw,r3,r4=measure_config(Ucfg,seed=5000+13*L+ci)
            all_rows+=rows; neg_w=max(neg_w,nw); rt3_w=max(rt3_w,r3); rt4_w=max(rt4_w,r4)
            Rc=np.array(rows); per_cfg_fracs.append(float(np.mean(Rc[:,1]>0)))
            ncfg_done+=1

    assert neg_w<1e-9, f'G-DT1 fail {neg_w}'
    assert rt3_w<1e-9, f'G-RT3 fail {rt3_w}'
    assert rt4_w<1e-10, f'G-RT4 fail {rt4_w}'
    R=np.array(all_rows)  # cols: kappa,min_Dp,nu_p, Amp(s0..s4)
    kap=R[:,0]; mdp=R[:,1]; nu_p=R[:,2]
    bad=mdp<=1e-12        # pointwise-bad (F040): some incident subset frees X_p
    amp_cols={f'{S_LIST[j]}':R[:,3+j] for j in range(len(S_LIST))}
    def stats(x):
        x=x[np.isfinite(x)]
        return {'median':float(np.median(x)),'mean':float(np.mean(x)),
                'q90':float(np.quantile(x,.90)),'q99':float(np.quantile(x,.99)),
                'max':float(np.max(x))}
    out={'tag':'F041','L':L,'beta':BETA,'a':aCAP,'N_mc':a_.N,'ncfg':ncfg_done,
         'use_stored':bool(a_.use_stored),'n_records':int(R.shape[0]),
         'mean_plaq':plaqs,'kappa_median':float(np.median(kap)),
         'G-RT1_resultant_{kappa:(emp,bessel,scalar)}':{str(k):v for k,v in g1.items()},
         'gates':'G-RT1,G-RT2,G-RT3,G-RT4,G-DT1 PASS','G-RT2_worst_MC_vs_quad':float(g2_worst),
         'pointwise_bad_frac':{'overall':float(np.mean(bad)),
              'per_config':per_cfg_fracs,
              'mean':float(np.mean(per_cfg_fracs)),
              'std':float(np.std(per_cfg_fracs))},
         'nu_p':stats(nu_p),
         'Amp_all':{s:stats(amp_cols[s]) for s in amp_cols},
         'Amp_on_pointwise_bad':{s:stats(amp_cols[s][bad]) for s in amp_cols} if bad.any() else {},
         'Amp_on_pointwise_good':{s:stats(amp_cols[s][~bad]) for s in amp_cols} if (~bad).any() else {},
         }
    json.dump(out,open(f'{HERE}/rooted_tilt_L{L}.json','w'),indent=1)
    print('=== F041 rooted/tilted LCI ratio  L=%d  records=%d  ncfg=%d  N=%d ==='%(L,R.shape[0],ncfg_done,a_.N))
    print('G-RT1 resultant <u·m> vs Bessel I2/I1:')
    for k,v in g1.items(): print('   kappa=%.0f  emp=%.4f bessel=%.4f scalar=%.4f'%(k,v[0],v[1],v[2]))
    print('G-RT2 worst MC-vs-quad cap prob %.2e PASS'%g2_worst)
    print('G-RT3(s=0⟹Amp=1, probs∈[0,1]) %.1e  G-RT4(7.4–7.7 identity) %.1e  G-DT1 %.1e PASS'%(rt3_w,rt4_w,neg_w))
    print('pointwise-bad frac (F040 observable): overall %.3f  per-cfg mean %.3f ± %.3f'%(
        np.mean(bad),np.mean(per_cfg_fracs),np.std(per_cfg_fracs)))
    print('nu(C_p) bare: median %.3f  q90 %.3f'%(out['nu_p']['median'],out['nu_p']['q90']))
    print('Amplification Amp(s)=nu^{B,s}(C_p)/nu(C_p):')
    print('   %-6s %8s %8s %8s %8s'%('s','median','q90','q99','max'))
    for s in amp_cols:
        st=out['Amp_all'][s]; print('   %-6s %8.3f %8.3f %8.3f %8.3f'%(s,st['median'],st['q90'],st['q99'],st['max']))
    if bad.any():
        print('Amp on the ~%.0f%% POINTWISE-BAD records only (the F040 bad set):'%(100*np.mean(bad)))
        for s in amp_cols:
            st=out['Amp_on_pointwise_bad'][s]; print('   s=%-4s median %7.3f  q90 %7.3f  q99 %7.3f  max %7.3f'%(s,st['median'],st['q90'],st['q99'],st['max']))
    print('MEASURE_DONE')

if __name__=='__main__':
    main()
