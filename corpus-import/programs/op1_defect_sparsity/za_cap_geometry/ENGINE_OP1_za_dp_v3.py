#!/usr/bin/env python3
# ENGINE_OP1_za_dp_v3.py — measure the corrected Z.A observable min_A Delta_p(A) on the SU(2)
# heat-bath ensemble; gates G-DT1 (no neg drops, hardened solver) + G-DT2 (F037
# bare-cap lemma holds on real data). Overstatement reported as a cross-tab, not
# a (wrong) pointwise ordering. One-shot.
import json, math, os, sys, time, itertools
import numpy as np
PMBSF='/sessions/busy-admiring-dijkstra/mnt/THEORY/programs/pmbsf'
sys.path.insert(0,PMBSF)
import ENGINE_FLUX_lci_typicality_diagnostic as lci
rng=np.random.default_rng(20260612)

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
    na=np.asarray(nl,dtype=float).reshape(-1,4);A=len(na)
    bu=None;bv=-np.inf
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
    K=len(nb);min_chi=np.inf;min_dp=np.inf;negdp=0.0;bdp=None;bchi=None
    for r in range(0,K+1):
        for A in itertools.combinations(range(K),r):
            NA=[nb[i] for i in A]
            uA,hA=solve(m,NA,a)
            if uA is None: continue
            chi=float(uA@n_p)-a
            _,hAp=solve(m,NA+[n_p],a)
            dp=hA-hAp
            if dp<-1e-9: negdp=max(negdp,-dp)
            dp=max(dp,0.0)
            if chi<min_chi: min_chi=chi
            if dp<min_dp: min_dp=dp
            if r==0: bdp=dp;bchi=chi
    return min_chi,min_dp,negdp,bdp,bchi

L=4;BETA=3.5;t_param=1.0104245908659366;eta=0.005;a=1.0-(t_param-eta)
T0=time.time()
U=lci.thermalize(L,BETA,50,rng,log_every=50)
print('therm %.1fs a=%.4f'%(time.time()-T0,a))
rows=[];neg_worst=0.0;bare_viol=0.0
blk=lci.Block(origin=(0,0,0,0),side=L,core_margin=1)
links=list(lci.core_links(blk,L)); rng.shuffle(links); links=links[:24]
for (x,mu) in links:
    normals,ids=lci.link_normals(U,x,mu,L)
    He=normals.sum(axis=0);hn=float(np.linalg.norm(He))
    if hn<1e-12: continue
    m_e=He/hn;kappa_e=BETA*hn
    for tix in range(6):
        n_p=normals[tix];nb=[normals[i] for i in range(6) if i!=tix]
        mc,mdp,negdp,bd,bc=min_obs(m_e,n_p,nb,a)
        neg_worst=max(neg_worst,negdp)
        if bd is not None and bc is not None and bc>0:
            bare_viol=max(bare_viol,0.5*bc*bc-bd)
        rows.append((kappa_e,mc,mdp))
    if time.time()-T0>35: break
R=np.array(rows);kap=R[:,0];mchi=R[:,1];mdp=R[:,2]
# GATES (the real ones)
assert neg_worst<1e-9,f'G-DT1 fail {neg_worst}'           # hardened solver: no impossible drops
assert bare_viol<1e-7,f'G-DT2 fail {bare_viol}'           # F037 bare-cap lemma on real data
def frac(x,t): return float(np.mean(x>t))
# overstatement cross-tab: among "good under old chi0" how many are marginal under Dp
good_chi=mchi>0.05
overstated = float(np.mean((mdp[good_chi]<0.01))) if good_chi.any() else 0.0
summ={'gates':'G-DT1,G-DT2 PASS','ensemble':{'L':L,'beta':BETA,'a':a,'n_records':len(rows),
   'kappa_median':float(np.median(kap)),'kappa_q05':float(np.quantile(kap,.05)),'kappa_q95':float(np.quantile(kap,.95))},
 'min_chi0':{'median':float(np.median(mchi)),'q05':float(np.quantile(mchi,.05)),
   'frac_gt0':frac(mchi,0),'frac_gt0.05':frac(mchi,.05),'frac_gt0.10':frac(mchi,.10)},
 'min_Dp':{'median':float(np.median(mdp)),'q05':float(np.quantile(mdp,.05)),
   'frac_gt0':frac(mdp,0),'frac_gt0.05':frac(mdp,.05),'frac_gt0.10':frac(mdp,.10)},
 'overstatement':{'frac_chi0_good_but_Dp_marginal':overstated,
   'def':'P(min_Dp<0.01 | min_chi0>0.05): cases the OLD chi0 criterion calls good but the corrected Delta_p says marginal'},
 'caveat':'L=4 single thermalized config, beta=3.5 (Stage-B); evidence-grade, finite-size; the local cap geometry is a per-link object so L=4 is indicative'}
here=os.path.dirname(os.path.abspath(__file__))
json.dump(summ,open(os.path.join(here,'CERT_OP1_za_dp_typicality.json'),'w'),indent=1)
print('G-DT1 (no neg Delta_p): PASS  | G-DT2 (bare-cap lemma on real data): PASS  | records=%d'%len(rows))
print('kappa_e median %.2f [%.2f,%.2f]'%(np.median(kap),np.quantile(kap,.05),np.quantile(kap,.95)))
print('OLD min_chi0: median %.4f frac>0 %.3f frac>0.05 %.3f frac>0.10 %.3f'%(np.median(mchi),frac(mchi,0),frac(mchi,.05),frac(mchi,.10)))
print('NEW min_Dp  : median %.4f frac>0 %.3f frac>0.05 %.3f frac>0.10 %.3f'%(np.median(mdp),frac(mdp,0),frac(mdp,.05),frac(mdp,.10)))
print('overstatement P(min_Dp<0.01 | min_chi0>0.05) = %.3f'%overstated)
print('ALL_GATES_PASS')
