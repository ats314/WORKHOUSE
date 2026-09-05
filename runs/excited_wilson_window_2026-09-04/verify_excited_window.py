#!/usr/bin/env python3
"""Operator-level diagnostics for the actual blocked Wilson transfer.

Analytic infinite-dimensional results are proved in EXCITED_WINDOW_OPERATOR_BRIDGE.md.
These tests check finite algebra and declared finite models; they do not certify
an all-orders Wilson vacuum-dressing activity bound or full WORKHOUSE CI.
"""
from __future__ import annotations
import argparse
import json
import math
import sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import sympy as sp
from scipy.linalg import expm, null_space

sys.path.insert(0, str(Path(__file__).parent / 'prior'))
from wilson_clock import labels, weyl_multipliers, character_hamiltonian

PIN = 'd2f46c586d76d000c07369c6e83ae218bf897734'

def herm(a):
    return (a + a.conj().T) / 2

def opnorm(a):
    return float(np.linalg.norm(a, 2))

def invsqrt(a):
    d, v = np.linalg.eigh(herm(a))
    if d[0] <= 0:
        raise ValueError('Source Gram must be positive definite')
    return (v / np.sqrt(d)) @ v.conj().T

def source_diagnostic(D, J):
    """All complement directions of the INPUT MATRIX are inspected.

    This is floating-point diagnostics, not interval certification. Supplying
    only a retained matrix supplies no bound on an omitted physical complement.
    """
    D = herm(np.asarray(D, dtype=complex))
    J = np.asarray(J, dtype=complex)
    C0 = herm(J.conj().T @ J)
    C1 = herm(J.conj().T @ D @ J)
    C2 = herm(J.conj().T @ D @ D @ J)
    W = J @ invsqrt(C0)
    Z = null_space(W.conj().T)
    A = herm(W.conj().T @ D @ W)
    QD = herm(Z.conj().T @ D @ Z)
    R = Z.conj().T @ D @ W
    a = float(np.linalg.eigvalsh(A)[0])
    b = float(np.linalg.eigvalsh(QD)[-1]) if Z.shape[1] else 0.0
    leakage = opnorm(R)
    H = herm(invsqrt(C0) @ (C2-C1@np.linalg.solve(C0,C1)) @ invsqrt(C0))
    vals, vecs = np.linalg.eigh(D)
    mid = (a+b)/2
    high = vecs[:, vals > mid]
    Pi = high @ high.conj().T
    P = W @ W.conj().T
    return {
        'a': a, 'b': b, 'separation': a-b,
        'passes_full_input_complement_test': bool(a>b),
        'high_rank_at_midpoint': int(high.shape[1]), 'source_rank': J.shape[1],
        'leakage_norm': leakage,
        'leakage_moment_identity_error': opnorm(H-R.conj().T@R),
        'projector_error': opnorm(Pi-P),
        'projector_bound': leakage/(a-b) if a>b else None,
        'window_gram_min': float(np.linalg.eigvalsh(herm(J.conj().T@Pi@J))[0]),
        'gram_min': float(np.linalg.eigvalsh(C0)[0]),
        'eigenvalues': vals.real.tolist(),
        '_A': A, '_R': R, '_Q': QD, '_W': W, '_H': H,
        '_C0': C0, '_C1': C1, '_C2': C2,
    }

def public(d):
    return {k:v for k,v in d.items() if not k.startswith('_')}

def local_block_derivative(energies, V, tau, m):
    c = np.exp(-tau*np.asarray(energies))
    divided = np.zeros((len(c),len(c)))
    for j in range(m):
        divided += c[:,None]**j * c[None,:]**(m-1-j)
    return tau/2*(c[:,None]+c[None,:])*divided*V

def embed_local(a, sites, n, outside_delta=1.0):
    """a tensor product with diag(1,delta) on every unaffected qubit."""
    sites=tuple(sites); rest=tuple(i for i in range(n) if i not in sites)
    dim=1<<n
    bits=np.array([[(j>>i)&1 for i in range(n)] for j in range(dim)])
    ai=sum((bits[:,site]<<t for t,site in enumerate(sites)),start=np.zeros(dim,dtype=int))
    ri=sum((bits[:,site]<<t for t,site in enumerate(rest)),start=np.zeros(dim,dtype=int))
    fac=outside_delta**bits[:,rest].sum(axis=1) if rest else np.ones(dim)
    return a[ai[:,None],ai[None,:]]*(ri[:,None]==ri[None,:])*fac[:,None]

def disjoint_families(supports, start=0, used=frozenset(), chosen=()):
    yield chosen
    for j in range(start,len(supports)):
        S=frozenset(supports[j])
        if S.isdisjoint(used):
            yield from disjoint_families(supports,j+1,used|S,chosen+(j,))

def study(grid=384, refined_grid=768):
    checks=[]
    def check(name, passed, **detail):
        r={'name':name,'passed':bool(passed),**detail}
        checks.append(r)
        if not passed:
            raise AssertionError(json.dumps(r,indent=2))

    # Optimal physical block and rounded spectral constants.
    x=sp.symbols('x',positive=True)
    g=x**4*(1-x)
    check('optimal_block_stationary_point_exact',sp.diff(g,x).subs(x,sp.Rational(4,5))==0,
          delta='4/5', optimal_gap=str(g.subs(x,sp.Rational(4,5))))
    check('optimal_block_global_maximum_exact',sp.simplify(sp.diff(g,x)-x**3*(4-5*x))==0)
    gstar=F(1024,15625)
    check('rounded_uniform_gap_exact', F(4,5)**5/F(5)==gstar,
          rounded_gap=str(gstar), optimal_gap=str(F(256,3125)))
    eta=F(1,400)
    E=eta/(F(2)*(F(1,5)-eta))
    check('activity_threshold_exact', E==F(1,158) and E<gstar/10,
          activity_limit='1/400',operator_error_bound=str(E),gap_tenth=str(gstar/10))
    check('finite_volume_projector_margin_exact',F(1,40)/(F(1,3)-F(1,40))==F(3,37))
    check('finite_volume_literal_source_margin_exact',F(3,37)+F(1,16)<F(1,4))

    # Support-count lemma, including its exact endpoint n=4,5.
    n=np.arange(0,20001)
    cnt=4*n*0.8**np.maximum(n-4,0)
    check('volume_independent_anchor_count',float(cnt.max())<=16+1e-12,
          max_count=float(cnt.max()),maximizers=np.where(abs(cnt-16)<1e-11)[0].tolist())
    # The comparison is not valid without the rounding direction.
    check('wrong_short_block_negative_control',4*5*(0.81)>16)

    rng=np.random.default_rng(41227)
    gamma=2/3; Es=4*gamma
    energies=gamma*np.array([j.bit_count() for j in range(16)])
    V=np.zeros((16,16));V[0,15]=V[15,0]=np.sqrt(2)
    q=rng.normal(size=(15,15));q=herm(q);q/=opnorm(q)
    V[1:,1:]=q
    Jnorm=opnorm(V)
    errors=[];bounds=[]
    for tau in (0.05,0.025,0.0125):
        sopt=math.log(5/4)/gamma;m=math.ceil(sopt/tau);s=m*tau
        B0=np.diag(np.exp(-s*energies))
        B1=local_block_derivative(energies,V,tau,m)
        d=tau/2/np.tanh(tau*Es/2)
        P0=np.zeros((16,16));P0[0,0]=1
        S=d*(V@P0-P0@V)
        R=B1+B0@S-S@B0
        errors.append(float(np.linalg.norm(R[:,0])))
        bounds.append({'tau':tau,'m':m,'local_norm':opnorm(R),'bound':Jnorm*(s+2*d)})
        check(f'local_first_derivative_anchor_tau_{tau}',errors[-1]<2e-14 and opnorm(R)<=bounds[-1]['bound'])
    check('local_generator_is_antihermitian',opnorm(S+S.conj().T)<1e-14)

    # Overlapping supports: this is a qubit hypergraph, not a Wilson lattice.
    overlap=[]
    for nsite in (5,6,7):
        supp=[tuple((j+t)%nsite for t in range(4)) for j in range(nsite)]
        local=R/opnorm(R)
        total=sum((embed_local(local,X,nsite,0.8) for X in supp),start=np.zeros((1<<nsite,1<<nsite)))
        val=opnorm(total)
        overlap.append({'sites':nsite,'norm':val,'upper_bound':16.0})
        check(f'overlapping_anchor_operator_{nsite}',val<=16+1e-11)

    # Full, all-orders locally anchored polymer model with exact disjoint-family sum.
    nsite=6;delta=0.8
    supports=[(i,) for i in range(nsite)]+[(i,(i+1)%nsite) for i in range(nsite)]
    atoms=[]
    for X in supports:
        d=1<<len(X)
        a=herm(rng.normal(size=(d,d)));a[0,:]=0;a[:,0]=0
        a/=opnorm(a);atoms.append(a)
    act=max(sum(delta**(-len(X))*opnorm(A) for X,A in zip(supports,atoms) if i in X) for i in range(nsite))
    scale=0.002/act;atoms=[a*scale for a in atoms]
    act=max(sum(delta**(-len(X))*opnorm(A) for X,A in zip(supports,atoms) if i in X) for i in range(nsite))
    D0=np.diag([delta**j.bit_count() for j in range(1<<nsite)])
    Bt=np.zeros_like(D0);families=0
    for fam in disjoint_families(supports):
        used=set().union(*(set(supports[j]) for j in fam)) if fam else set()
        term=np.eye(1<<nsite)
        for j in fam: term=term@embed_local(atoms[j],supports[j],nsite)
        # The untouched free product, no extra free factors on touched sites.
        diag=np.array([delta**sum((bits>>i)&1 for i in range(nsite) if i not in used) for bits in range(1<<nsite)])
        Bt+=term*diag[None,:];families+=1
    bd=act/(math.e*(math.log(1/delta)-act))
    err=opnorm(Bt-D0)
    check('all_orders_anchored_polymer_norm_bound',err<=bd+1e-12,
          eta=act,operator_error=err,bound=bd,disjoint_families=families)
    check('all_orders_polymer_exact_vacuum',np.linalg.norm(Bt[:,0]-D0[:,0])<1e-14)
    eigs=np.linalg.eigvalsh(Bt)
    check('all_orders_toy_positive_contraction',eigs[0]>0 and eigs[-1]<=1+1e-12)

    # Exact source/complement and memory identities in a full finite triplet model.
    A=np.diag([0.405,0.419,0.438]);Dq=np.diag(np.linspace(0.07,0.30,9))
    Rm=rng.normal(size=(9,3))*0.004
    D=np.block([[A,Rm.T],[Rm,Dq]])
    U,_=np.linalg.qr(rng.normal(size=(12,12)));D=U@D@U.T
    root=np.array([[1.0,.08,0],[0,.92,.06],[0,0,1.07]])
    src=U[:,:3]@root
    diag=source_diagnostic(D,src)
    check('three_source_complete_input_spectrum',diag['passes_full_input_complement_test'] and diag['high_rank_at_midpoint']==3,
          diagnostic=public(diag))
    check('irreducible_leakage_moment_identity',diag['leakage_moment_identity_error']<2e-13)
    check('source_to_spectral_projector_angle',diag['projector_error']<=diag['projector_bound']+2e-12)
    G=diag['_C0'];C1=diag['_C1'];C2=diag['_C2'];c=.4096
    ident=invsqrt(G)@(C2-2*c*C1+c*c*G)@invsqrt(G)-(diag['_A']-c*np.eye(3))@(diag['_A']-c*np.eye(3))-diag['_H']
    check('centered_variance_splits_into_drift_and_leakage',opnorm(ident)<3e-13)
    z=.51+0.03j
    W=diag['_W'];Rs=diag['_R'];As=diag['_A'];Qs=diag['_Q']
    reduced=W.conj().T@np.linalg.solve(z*np.eye(12)-D,W)
    schur=np.linalg.inv(z*np.eye(3)-As-Rs.conj().T@np.linalg.solve(z*np.eye(9)-Qs,Rs))
    check('exact_memory_resolvent_identity',opnorm(reduced-schur)<4e-12)
    moment0=Rs.conj().T@Rs
    check('memory_leading_coefficient_is_leakage',opnorm(moment0-diag['_H'])<2e-13)
    # A fourth invisible state: exact moments of the original sources are unchanged.
    Dh=np.block([[D,np.zeros((12,1))],[np.zeros((1,12)),np.array([[.425]])]])
    Jh=np.vstack([src,np.zeros((1,3))]);hidden=source_diagnostic(Dh,Jh)
    check('dark_state_complement_negative_control',not hidden['passes_full_input_complement_test'] and opnorm(hidden['_C0']-G)<1e-14 and opnorm(hidden['_C2']-C2)<1e-14,
          complement_top=hidden['b'],source_bottom=hidden['a'],source_moments_unchanged=True)

    # First-order rotation is not an all-orders chart: independent-site counterexample.
    tau=.04;m=6;s=tau*m;E1=1.0
    v=np.array([[0.,1.],[1.,.7]])
    dd=tau/2/math.tanh(tau*E1/2)
    s1=dd*np.array([[0.,-1.],[1.,0.]])
    def dressed2(u):
        a=expm(tau*u*v/2);t=a@np.diag([1.,math.exp(-tau*E1)])@a
        vals,vecs=np.linalg.eigh(t)
        normB=(vecs@(np.diag((vals/vals[-1])**m))@vecs.T)
        rot=expm(u*s1)
        return rot.T@normB@rot,rot.T@vecs[:,-1]
    hh=2e-4
    F0,_=dressed2(0);Fp,_=dressed2(hh);Fm,_=dressed2(-hh)
    deriv=(Fp-Fm)/(2*hh);second=(Fp+Fm-2*F0)/(hh*hh)
    Fp2,_=dressed2(hh/2);Fm2,_=dressed2(-hh/2)
    second2=(Fp2+Fm2-2*F0)/(hh*hh/4)
    check('first_rotation_cancels_linear_vacuum_column',abs(deriv[1,0])<3e-8)
    check('first_rotation_leaves_quadratic_vacuum_creation',abs(second[1,0])>.05 and abs(second[1,0]-second2[1,0])<2e-6,
          second_offdiagonal=float(second[1,0]))
    fu,w=dressed2(.04)
    one_overlap=float(abs(w[0])**2)
    many_overlap=math.exp(10_000_000*math.log(one_overlap))
    check('finite_order_rotation_not_uniform_all_orders',many_overlap<1e-4,
          u=.04,sites=10_000_000,one_site_ground_overlap_squared=one_overlap,
          product_ground_overlap_squared=many_overlap,
          interpretation='exact product formula; no 2^sites matrix was formed')

    # Actual SU(3) finite-character transfer. Same retained space on both sides.
    epss=[.05,.025,.0125,.00625];reps=labels(5)
    logs1=weyl_multipliers(epss,reps,grid)
    logs2=weyl_multipliers(epss,reps,refined_grid)
    qerr=max(abs(logs1[e][r]-logs2[e][r])/e for e in epss for r in reps)
    check('SU3_Weyl_grid_refinement',qerr<2e-9,max_energy_difference=qerr,grids=[grid,refined_grid])
    rr,H0,V,ev,od=character_hamiltonian(5,.05)
    idx={r:i for i,r in enumerate(rr)};VF=np.zeros_like(V)
    for i,(p,q) in enumerate(rr):
        for target in ((p+1,q),(p-1,q+1),(p,q-1)):
            if min(target)>=0 and target in idx: VF[idx[target],i]+=1
    O=(VF-VF.T)/math.sqrt(2)
    rows=[];u=.05
    for e in epss:
        tau=-1.5*logs2[e][1,0]
        sopt=1.5*math.log(5/4);m=math.ceil(sopt/tau);s=m*tau
        a=expm(tau*u*V/2);T=a@np.diag([math.exp(4*logs2[e][r]) for r in rr])@a
        ve,ue=np.linalg.eigh(herm(ev.T@T@ev));vac=ev@ue[:,-1]
        to=herm(od.T@T@od);vo,uo=np.linalg.eigh(to)
        Bo=uo@np.diag((vo/ve[-1])**m)@uo.T
        source=(od.T@O@vac)[:,None]
        ddg=source_diagnostic(Bo,source)
        row={'epsilon':e,'tau':tau,'steps':m,'block_time':s,'u':u,**public(ddg)}
        row['input_model_gap_bound_formula']=math.log(row['a']/row['b'])/s
        evalgap=-math.log(vo[-2]/vo[-1])/tau
        row['actual_input_model_energy_gap']=float(evalgap)
        rows.append(row)
        check(f'SU3_full_retained_odd_complement_eps_{e}',row['passes_full_input_complement_test'] and row['high_rank_at_midpoint']==1 and row['input_model_gap_bound_formula']<=evalgap+1e-10,
              a=row['a'],b=row['b'],residual=row['leakage_norm'],gap_bound=row['input_model_gap_bound_formula'])
    return {'status':'PASS','checks_passed':len(checks),'checks':checks,
            'repository_reference':PIN,'SU3_model':{'character_cutoff':5,'total_dimension':len(rr),'odd_dimension':od.shape[1],'rows':rows},
            'overlapping_anchor_model':overlap,'local_anchor_model':bounds,
            'scope':'Analytic implications proved in note; numerical tests are finite-model diagnostics, not validated interval bounds.',
            'not_established':['all-orders Wilson anchored-activity bound uniform in volume','thermodynamic Wilson shell completeness','spatially weighted sharp-shell matching','full WORKHOUSE CI or Lean replay']}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--grid',type=int,default=384)
    ap.add_argument('--refined-grid',type=int,default=768)
    ap.add_argument('--output',type=Path,default=Path('excited_window_certificate.json'))
    args=ap.parse_args()
    result=study(args.grid,args.refined_grid)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks_passed':result['checks_passed'],
                      'SU3_model':result['SU3_model']},indent=2))

if __name__=='__main__':
    main()
