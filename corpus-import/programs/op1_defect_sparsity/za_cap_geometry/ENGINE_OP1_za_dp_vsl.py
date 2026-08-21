#!/usr/bin/env python3
# ENGINE_OP1_za_dp_vsl.py — measure the Z.A good-event margin min_A Delta_p(A) vs lattice size
# L, using the validated vectorized heat-bath (su2_hb_v3). Resumable thermalization
# (chunked, deadline-aware) so L=16 fits the bounded shell.
#   python3 ENGINE_OP1_za_dp_vsl.py --L 8  --target 80 --nlinks 40 --deadline 38
#   python3 ENGINE_OP1_za_dp_vsl.py --L 16 --target 80 --nlinks 40 --deadline 38   (call repeatedly)
import json, math, os, sys, time, itertools, argparse
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import ENGINE_PMBSF_su2_hb_v3 as hb
import ENGINE_FLUX_lci_typicality_diagnostic as lci

ap=argparse.ArgumentParser()
ap.add_argument('--L',type=int,required=True)
ap.add_argument('--target',type=int,default=80)
ap.add_argument('--nlinks',type=int,default=40)
ap.add_argument('--deadline',type=float,default=38.0)
ap.add_argument('--beta',type=float,default=3.5)
a_=ap.parse_args(); T0=time.time()
L=a_.L; BETA=a_.beta
t_param=1.0104245908659366; eta=0.005; aCAP=1.0-(t_param-eta)
statef=f'{HERE}/vsL_state_L{L}.npz'; metaf=f'{HERE}/vsL_meta_L{L}.json'

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
def min_obs(m,n_p,nb,a):
    K=len(nb);mc=np.inf;mdp=np.inf;neg=0.0;bdp=None;bchi=None
    for r in range(0,K+1):
        for A in itertools.combinations(range(K),r):
            NA=[nb[i] for i in A]; uA,hA=solve(m,NA,a)
            if uA is None: continue
            chi=float(uA@n_p)-a; _,hAp=solve(m,NA+[n_p],a); dp=hA-hAp
            if dp<-1e-9: neg=max(neg,-dp)
            dp=max(dp,0.0)
            if chi<mc: mc=chi
            if dp<mdp: mdp=dp
            if r==0: bdp=dp;bchi=chi
    return mc,mdp,neg,bdp,bchi

# ---- resumable thermalization ----
if os.path.exists(metaf):
    meta=json.load(open(metaf)); U=np.load(statef)['U']
else:
    meta={'sweeps':0}; U=np.zeros((L,L,L,L,4,4)); U[...,0]=1.0
# chunk sweeps until target or deadline
rng=np.random.default_rng(20260612+L)
while meta['sweeps']<a_.target and (time.time()-T0)<a_.deadline-6.0:
    hb.thermalize_vec(L,BETA,1,rng,log_every=0,U=U)
    meta['sweeps']+=1
np.savez_compressed(statef,U=U); json.dump(meta,open(metaf,'w'))
mp=hb.mean_plaq(U)
print('L=%d sweeps %d/%d <½ReTr>=%.5f (%.1fs)'%(L,meta['sweeps'],a_.target,mp,time.time()-T0))
if meta['sweeps']<a_.target:
    print('THERM_INCOMPLETE — call again'); sys.exit(0)

# ---- measure min_A Delta_p over a sample of core links ----
blk=lci.Block(origin=tuple([0]*4),side=L,core_margin=2)
# Use an INDEPENDENT, deterministically-seeded rng for the link subsample so the
# measurement reproduces from a saved (already-thermalized) state. Previously the
# thermalization rng was reused here, so resuming from a stored state (which skips
# the thermalization draws) selected a different 40-link subsample and the stored
# fractions did not reproduce. (Defect found in June-13 re-verification.)
rng_s=np.random.default_rng(770000+L)
links=sorted(lci.core_links(blk,L)); rng_s.shuffle(links); links=links[:a_.nlinks]
rows=[]; neg_worst=0.0; bare_viol=0.0
for (x,mu) in links:
    normals,ids=lci.link_normals(U,x,mu,L)
    He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
    if hn<1e-12: continue
    m_e=He/hn; kap=BETA*hn
    for tix in range(6):
        n_p=normals[tix]; nb=[normals[i] for i in range(6) if i!=tix]
        mc,mdp,neg,bd,bc=min_obs(m_e,n_p,nb,aCAP)
        neg_worst=max(neg_worst,neg)
        if bd is not None and bc is not None and bc>0: bare_viol=max(bare_viol,0.5*bc*bc-bd)
        rows.append((kap,mc,mdp))
    if (time.time()-T0)>a_.deadline-3.0: break
R=np.array(rows); kap=R[:,0]; mchi=R[:,1]; mdp=R[:,2]
assert neg_worst<1e-9, f'G-DT1 fail {neg_worst}'
assert bare_viol<1e-7, f'G-DT2 fail {bare_viol}'
def frac(x,t): return float(np.mean(x>t))
res={'L':L,'beta':BETA,'sweeps':meta['sweeps'],'mean_plaq':mp,'a':aCAP,'n_records':len(rows),
 'kappa_median':float(np.median(kap)),
 'min_chi0':{'median':float(np.median(mchi)),'frac_gt0':frac(mchi,0),'frac_gt0.05':frac(mchi,.05),'frac_gt0.10':frac(mchi,.10)},
 'min_Dp':{'median':float(np.median(mdp)),'q90':float(np.quantile(mdp,.90)),'max':float(np.max(mdp)),
           'frac_gt0':frac(mdp,0),'frac_gt0.02':frac(mdp,.02),'frac_gt0.05':frac(mdp,.05),'frac_gt0.10':frac(mdp,.10)},
 'overstatement_P_Dp_lt_0.01_given_chi0_gt_0.05': float(np.mean(mdp[mchi>0.05]<0.01)) if (mchi>0.05).any() else 0.0}
json.dump(res,open(f'{HERE}/vsL_result_L{L}.json','w'),indent=1)
print('G-DT1/G-DT2 PASS  L=%d records=%d kappa_med=%.2f'%(L,len(rows),np.median(kap)))
print('  min_Dp: median %.4f q90 %.4f max %.4f | frac>0 %.3f >0.05 %.3f >0.10 %.3f'%(
   np.median(mdp),np.quantile(mdp,.9),np.max(mdp),frac(mdp,0),frac(mdp,.05),frac(mdp,.10)))
print('  min_chi0: median %.4f frac>0 %.3f >0.05 %.3f'%(np.median(mchi),frac(mchi,0),frac(mchi,.05)))
print('  overstatement P(Dp<0.01|chi0>0.05)=%.3f'%res['overstatement_P_Dp_lt_0.01_given_chi0_gt_0.05'])
print('MEASURE_DONE')
