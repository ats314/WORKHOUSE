#!/usr/bin/env python3
# ENGINE_OP1_za_dp_typicality.py — first measurement of the CORRECTED Z.A observable
# min_A Delta_p(A) on an actual SU(2) Wilson exact-heat-bath ensemble (beta=3.5,
# Stage-B value).  F038 reduced Z.A to: G_LCI' = { min_A Delta_p(A) >= Delta_q +
# O(log k/k) } holds P-typically.  The diagnostic ENGINE_FLUX_lci_typicality_diagnostic.py
# measures the OLD observable min_A chi_0 (= u_A.n_p - a), which F037 showed
# OVERSTATES the good event.  Here we measure min_A Delta_p(A) = h(A)-h(A∪{p})
# (the correct one) with the HARDENED cap solver, alongside min_A chi_0 for
# direct comparison, on the same heat-bath geometry.
# One-shot (no edits): VM mount won't refresh edited paths.
import json, math, os, sys, time, itertools
import numpy as np

PMBSF = '/sessions/busy-admiring-dijkstra/mnt/THEORY/programs/pmbsf'
sys.path.insert(0, PMBSF)
import ENGINE_FLUX_lci_typicality_diagnostic as lci   # lattice geometry + exact heat-bath + normals

rng = np.random.default_rng(20260612)

# ---- hardened cap solver (S^3), from za_cert_v5 ----
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
    bu=None;bv=-np.inf
    for mask in range(1<<A):
        act=[i for i in range(A) if (mask>>i)&1]
        Na=na[act] if act else np.zeros((0,4))
        u,v=cmax(m,Na,a)
        if u is None: continue
        ok=True
        for j in range(A):
            if j in act: continue
            if float(na[j]@u)>a+it: ok=False; break
        if ok and v>bv: bv=v;bu=u
    return bu,bv

def min_observables(m, n_p, neighbors, a):
    """min over all subsets A of the 5 neighbors of (chi_0(A), Delta_p(A))."""
    K=len(neighbors)
    min_chi=np.inf; min_dp=np.inf; neg_dp=0.0; bare_dp=None; bare_chi=None
    for r in range(0,K+1):
        for A in itertools.combinations(range(K),r):
            NA=[neighbors[i] for i in A]
            uA,hA=solve(m,NA,a)
            if uA is None: continue
            chi=float(uA@n_p)-a
            _,hAp=solve(m,NA+[n_p],a)
            dp=hA-hAp
            if dp<-1e-9: neg_dp=max(neg_dp,-dp)
            dp=max(dp,0.0)
            if chi<min_chi: min_chi=chi
            if dp<min_dp: min_dp=dp
            if r==0: bare_dp=dp; bare_chi=chi
    return min_chi, min_dp, neg_dp, bare_dp, bare_chi

# ---- thermalize a couple of SU(2) configs (beta=3.5) ----
L=4; BETA=3.5; D=4
t_param=1.0104245908659366; eta=0.005; a=1.0-(t_param-eta)
T0=time.time()
U=lci.thermalize(L,BETA,60,rng,log_every=60)
configs=[U.copy()]
for _ in range(2):
    for _ in range(10): lci.heatbath_sweep(U,BETA,L,rng)
    configs.append(U.copy())
print('thermalized %d configs in %.1fs (a=%.4f)'%(len(configs),time.time()-T0,a))

# ---- process all core links over a couple of blocks per config ----
rows=[]   # (kappa_e, half_re_tr_target, min_chi0, min_Dp, bare_Dp, bare_chi)
neg_worst=0.0; bare_viol=0.0
for ci,Uc in enumerate(configs):
    blk=lci.Block(origin=(0,0,0,0),side=L,core_margin=1)
    for (x,mu) in lci.core_links(blk,L):
        normals,ids=lci.link_normals(Uc,x,mu,L)
        He=normals.sum(axis=0); hn=float(np.linalg.norm(He))
        if hn<1e-12: continue
        m_e=He/hn; kappa_e=BETA*hn
        for tix in range(6):
            n_p=normals[tix]; nb=[normals[i] for i in range(6) if i!=tix]
            mc,mdp,negdp,bdp,bchi=min_observables(m_e,n_p,nb,a)
            neg_worst=max(neg_worst,negdp)
            if bdp is not None and bchi is not None and bchi>0:
                # F037 bare-cap lemma: Delta_p(∅) >= chi0^2/2
                bare_viol=max(bare_viol, 0.5*bchi*bchi - bdp)
            rows.append((kappa_e, float(Uc[x+(mu,)]@n_p), mc, mdp, bdp if bdp else 0.0, bchi if bchi else 0.0))
print('records:',len(rows))

R=np.array(rows)
kap=R[:,0]; mchi=R[:,2]; mdp=R[:,3]
# GATE G-DT1: hardened solver gives no geometrically-impossible negative drops
assert neg_worst<1e-9, f'GATE FAIL G-DT1: negative Delta_p {neg_worst}'
# GATE G-DT2: F037 bare-cap lemma holds on real data (Delta_p(∅) >= chi0^2/2)
assert bare_viol<1e-7, f'GATE FAIL G-DT2: bare-cap lemma violated by {bare_viol}'
# GATE G-DT3: chi_0 OVERSTATES the good event: min_chi0 >= min_Dp pointwise
#  (the corrected observable is never larger than the old one) -- key F037/F038 check
overstate_viol=float(np.max(mdp-mchi))
assert overstate_viol<1e-6, f'GATE FAIL G-DT3: min_Dp>min_chi0 by {overstate_viol}'

def frac(arr,thr): return float(np.mean(arr>thr))
summary={
 'gates':'G-DT1,G-DT2,G-DT3 PASS',
 'ensemble':{'L':L,'beta':BETA,'a':a,'n_configs':len(configs),'n_records':len(rows),
             'kappa_e_median':float(np.median(kap)),'kappa_e_q05':float(np.quantile(kap,0.05)),
             'kappa_e_q95':float(np.quantile(kap,0.95))},
 'old_observable_min_chi0':{
     'median':float(np.median(mchi)),'q05':float(np.quantile(mchi,0.05)),
     'frac_gt_0':frac(mchi,0.0),'frac_gt_0.05':frac(mchi,0.05),'frac_gt_0.10':frac(mchi,0.10)},
 'corrected_observable_min_Dp':{
     'median':float(np.median(mdp)),'q05':float(np.quantile(mdp,0.05)),
     'frac_gt_0':frac(mdp,0.0),'frac_gt_0.05':frac(mdp,0.05),'frac_gt_0.10':frac(mdp,0.10)},
 'overstatement':{
     'mean_min_chi0_minus_min_Dp':float(np.mean(mchi-mdp)),
     'median_min_chi0_minus_min_Dp':float(np.median(mchi-mdp)),
     'note':'chi_0 good-event fraction vs Delta_p good-event fraction quantifies the F037 overstatement on real heat-bath data'},
 'typicality_G_LCI_prime':{
     'frac_min_Dp_gt_0':frac(mdp,0.0),
     'interpretation':'fraction of (e,p) whose min_A Delta_p(A) clears 0 (necessary part of G_LCI prime); compare to the old chi_0>0 fraction'},
}
here=os.path.dirname(os.path.abspath(__file__))
json.dump(summary,open(os.path.join(here,'CERT_OP1_za_dp_typicality.json'),'w'),indent=1)
print('G-DT1 (no neg Delta_p): PASS | G-DT2 (bare-cap lemma on data): PASS | G-DT3 (chi0>=Dp pointwise): PASS')
print('kappa_e: median %.2f [q05 %.2f, q95 %.2f]'%(np.median(kap),np.quantile(kap,0.05),np.quantile(kap,0.95)))
print('OLD min_chi0 : median %.4f  frac>0 %.3f  frac>0.05 %.3f'%(np.median(mchi),frac(mchi,0),frac(mchi,0.05)))
print('NEW min_Dp   : median %.4f  frac>0 %.3f  frac>0.05 %.3f'%(np.median(mdp),frac(mdp,0),frac(mdp,0.05)))
print('overstatement: mean(min_chi0 - min_Dp) = %.4f'%float(np.mean(mchi-mdp)))
print('ALL_GATES_PASS')
