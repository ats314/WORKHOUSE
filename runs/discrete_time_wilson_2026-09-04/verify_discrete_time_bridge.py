#!/usr/bin/env python3
"""Finite checks for the time-block / scalar-polymer / source-window argument.

Analytic proofs, not these finite tests, establish uniformity. The clock models
and finite SU(3) character space are declared test models, not the full lattice.
No historical C_shp or microscopic fourth-order target is used.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
from scipy.linalg import eigh, expm
from scipy.stats import binom
import sympy as sp

from wilson_clock import casimir, character_hamiltonian, labels, weyl_multipliers

PIN = "8e44da1fbd4b8643a12d514a1fb83ac636edf094"


def subsets(n: int):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if mask >> i & 1)


def connected_components(indices: tuple[int, ...], supports: list[set[int]]):
    remain = set(indices)
    out = []
    while remain:
        seed = min(remain)
        remain.remove(seed)
        comp = {seed}
        stack = [seed]
        while stack:
            a = stack.pop()
            neighbors = [b for b in remain if supports[a] & supports[b]]
            for b in neighbors:
                remain.remove(b)
                comp.add(b)
                stack.append(b)
        out.append(tuple(sorted(comp)))
    return out


def run(grid: int = 192, refined_grid: int = 384) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(name: str, ok: bool, **detail: Any) -> None:
        row = {"name": name, "passed": bool(ok), **detail}
        checks.append(row)
        if not ok:
            raise AssertionError(json.dumps(row, indent=2))

    # The condition is arithmetic, not a numerical proof of the cluster theorem.
    s = sp.Rational(1, 8) + sp.Rational(8, 256) / (1 - sp.Rational(144, 256))
    check("KP_margin_exact", s == sp.Rational(11, 56) and s < sp.Rational(1, 4),
          value=str(s), slack_to_quarter=str(sp.Rational(1, 4)-s))
    xi = 0.1
    delta = math.exp(-(4+2*xi))/32
    y = 1/1024
    b = y / (math.exp(16+8*xi)*(1+delta)**4)
    activity = 2*math.exp(4+2*xi)*delta + 8*y/(1-144*y)
    check("explicit_positive_coupling_domain", b > 0 and activity < 0.25,
          xi=xi, delta=delta, bridge_b=b, activity_sum=activity,
          note="dimensionless sufficient-condition arithmetic, not evaluated SU(3) heat constants")

    # Exact integer geometry used by the space-time atom count.
    geometry=[]
    for L in (3,5):
        plaquettes=[]; link_faces={}
        def shift(x,axis):
            y=list(x);y[axis]=(y[axis]+1)%L;return tuple(y)
        for x in itertools.product(range(L),repeat=3):
            for a0 in range(3):
                for b0 in range(a0+1,3):
                    edges={(x,a0),(shift(x,a0),b0),(shift(x,b0),a0),(x,b0)}
                    pi=len(plaquettes);plaquettes.append(edges)
                    for edge in edges:link_faces.setdefault(edge,set()).add(pi)
        counts=[]
        for pi,edges in enumerate(plaquettes):
            adjacent=set().union(*(link_faces[e] for e in edges))-{pi}
            counts.append(len(adjacent))
        geometry.append({'L':L,'plaquettes':len(plaquettes),
            'link_incidence':sorted(set(map(len,link_faces.values()))),
            'plaquette_degrees':sorted(set(counts))})
    check("cubical_atom_count_exact_geometry",
        all(r0['link_incidence']==[4] and r0['plaquette_degrees']==[12] for r0 in geometry),rows=geometry)

    # Binomial lower-tail estimate used for uniform smoothing.
    tail_worst = 0.0
    for a in (0.01, 0.1, 0.25, 0.49):
        for m in (1, 2, 5, 20, 100, 1000):
            last = math.ceil(a*m/2)-1
            tail = float(binom.cdf(last, m, a)) if last >= 0 else 0.0
            ratio = tail / math.exp(-a*m/8)
            tail_worst = max(tail_worst, ratio)
    check("binomial_bad_block_bound", tail_worst <= 1+1e-13, max_ratio=tail_worst)

    # Convolution mixture on Z_11, with a genuine positive central heat kernel.
    q = 11
    P = np.ones((q,q))/q
    lap = 2*np.eye(q)-np.roll(np.eye(q),1,axis=1)-np.roll(np.eye(q),-1,axis=1)
    a, eps, m = 0.3, 0.04, 23
    heat = expm(-eps*lap/8)
    r = 0.8*np.eye(q)+0.2*P
    C = a*heat+(1-a)*r
    mix = np.zeros_like(C)
    for k in range(m+1):
        mix += binom.pmf(k,m,a) * np.linalg.matrix_power(heat,k) @ np.linalg.matrix_power(r,m-k)
    err = float(np.max(np.abs(mix-np.linalg.matrix_power(C,m))))
    check("convolution_binomial_identity_finite_group", err < 1e-13, max_error=err)

    # Fine steps do not mix uniformly if their count is held fixed.
    q = 3
    P = np.ones((q,q))/q
    K = np.eye(q)-P
    ds=[]
    for tau in (0.1,0.01,0.001):
        fine=expm(-tau*K)
        fixed= q*np.linalg.matrix_power(fine,4)-np.ones((q,q))
        mb=math.ceil(8/tau)
        blocked=q*np.linalg.matrix_power(fine,mb)-np.ones((q,q))
        ds.append({"tau":tau,"fixed_count_density_error":float(np.max(np.abs(fixed))),
                   "physical_block_density_error":float(np.max(np.abs(blocked))),"m":mb})
    check("fixed_time_block_mixing", max(r0['physical_block_density_error'] for r0 in ds)<0.00068, rows=ds)
    check("fixed_fine_count_negative_control", ds[-1]['fixed_count_density_error']>1.9 and
          ds[-1]['fixed_count_density_error']>ds[0]['fixed_count_density_error'])

    # Four q=3 sites, three overlapping diagonal pair interactions. This is a
    # positive finite-state test model, not an SU(3) lattice truncation.
    q, nsite = 3, 4
    states=np.array(list(itertools.product(range(q),repeat=nsite)))
    p=np.ones((q,q))/q
    kl=np.eye(q)-p
    I=np.eye(q)
    dim=q**nsite
    def kron_many(factors):
        out=np.array([[1.0]])
        for f in factors:
            out=np.kron(out,f)
        return out
    Ktot=sum(kron_many([kl if j==i else I for j in range(nsite)]) for i in range(nsite))
    supports=[{0,1},{1,2},{2,3}]
    potentials=[np.cos(2*np.pi*(states[:,min(ss)]-states[:,max(ss)])/q) for ss in supports]
    records=[]
    factor_err=0.0
    power_err=0.0
    for m in (1,2,5,10):
        tau=1/m; duration=1.0; u=0.04
        free=expm(-tau*Ktot)
        freeblock=expm(-duration*Ktot)
        blocks={}
        for X in subsets(3):
            v=sum((potentials[i] for i in X), np.zeros(dim))
            mult=np.exp(tau*u*v/2)
            T=(mult[:,None]*free)*mult[None,:]
            blocks[X]=np.linalg.matrix_power(T,m)
        M={}
        for X in subsets(3):
            raw=np.zeros((dim,dim))
            for local in subsets(len(X)):
                Y=tuple(X[i] for i in local)
                raw += (-1)**(len(X)-len(Y))*blocks[Y]
            M[X]=raw/freeblock
        max_recon=float(np.max(np.abs(sum(M.values())-blocks[(0,1,2)]/freeblock)))
        factor_err=max(factor_err,float(np.max(np.abs(M[(0,2)]-M[(0,)]*M[(2,)]))))
        b0=math.expm1(duration*abs(u))
        max_ratio=max(float(np.max(np.abs(M[X])))/b0**len(X) for X in subsets(3) if X)
        records.append({"fine_steps":m,"activity_bound_max_ratio":max_ratio,"reconstruction_error":max_recon})
        # Energies and projectors are unchanged under a positive power.
        vals, vec=eigh(blocks[(0,1,2)])
        v=sum(potentials)
        mult=np.exp(tau*u*v/2)
        T=(mult[:,None]*free)*mult[None,:]
        tv,tu=eigh(T)
        E1=-np.log(tv/tv[-1])/tau
        Em=-np.log(vals/vals[-1])/duration
        power_err=max(power_err,float(np.max(np.abs(E1-Em))))
    check("all_order_bridge_activity_bound_toy", max(r0['activity_bound_max_ratio'] for r0 in records)<=1+2e-7,rows=records)
    check("bridge_subset_reconstruction_toy", max(r0['reconstruction_error'] for r0 in records)<2e-12)
    check("disconnected_bridge_factorization_toy", factor_err<2e-11,max_error=factor_err)
    check("blocking_preserves_all_finite_spectrum_toy",power_err<1e-10,max_energy_error=power_err)
    check("wrong_block_clock_negative_control", np.max(np.abs(m*Em-E1))>1)

    # Independent exact atomic / scalar-polymer reconstruction in a small
    # periodic space-time lattice: two binary sites and three coarse slices.
    q=2; p=np.ones((2,2))/2; kl=np.eye(2)-p
    K2=np.kron(kl,np.eye(2))+np.kron(np.eye(2),kl)
    tau=0.4;m=5;duration=m*tau;u=0.03
    v=np.array([1,-1,-1,1],float)
    F=expm(-tau*K2); mult=np.exp(tau*u*v/2)
    T=(mult[:,None]*F)*mult[None,:]
    B=np.linalg.matrix_power(T,m)
    density_B=4*B
    P1=2*expm(-duration*kl)
    P2=np.kron(P1,P1)
    magnetic=density_B-P2
    config=list(itertools.product(range(2),repeat=6))
    atom_supp=[]; atom_vals=[]; tags=[]
    for t in range(3):
        tt=(t+1)%3
        for site in range(2):
            atom_supp.append({2*t+site,2*tt+site})
            atom_vals.append(np.array([P1[c[2*tt+site],c[2*t+site]]-1 for c in config]))
            tags.append(('q',t,site))
        atom_supp.append({2*t,2*t+1,2*tt,2*tt+1})
        atom_vals.append(np.array([magnetic[2*c[2*tt]+c[2*tt+1],2*c[2*t]+c[2*t+1]] for c in config]))
        tags.append(('mag',t,-1))
    atomic_sum=0.0; polymer_sum=0.0; admissible=0
    for choice in subsets(9):
        ok=True
        for t in range(3):
            chosen=[tags[a] for a in choice if tags[a][1]==t]
            if any(a[0]=='mag' for a in chosen) and len(chosen)>1:
                ok=False
        if not ok: continue
        admissible+=1
        val=np.ones(64)
        for ai in choice: val*=atom_vals[ai]
        atomic_sum+=float(np.mean(val))
        prod=1.0
        for comp in connected_components(choice,atom_supp):
            val=np.ones(64)
            for ai in comp: val*=atom_vals[ai]
            prod*=float(np.mean(val))
        polymer_sum+=prod
    direct=float(np.trace(np.linalg.matrix_power(B,3)))
    check("coarse_spacetime_atomic_identity",abs(atomic_sum-direct)<2e-13,
          admissible_configurations=admissible,atomic_sum=atomic_sum,direct_trace=direct)
    check("coarse_spacetime_scalar_polymer_identity",abs(polymer_sum-direct)<2e-13,
          polymer_sum=polymer_sum,direct_trace=direct)

    # Rooted-tree majorant checked against all connected subsets of a small
    # hypergraph, independently of the polymer identity above.
    smallsupports=[{0,1},{1,2},{2,3},{0,3},{1,3}]
    bb=np.array([0.0008,0.0004,0.0007,0.0003,0.0005])
    maxq=max(sum(bb[a]*math.exp((2+xi)*len(smallsupports[a])) for a in range(5) if z in smallsupports[a]) for z in range(4))
    cc=[]
    for z in range(4):
        total=0.0
        for ch in subsets(5):
            if not ch or len(connected_components(ch,smallsupports))!=1:continue
            union=set().union(*(smallsupports[a] for a in ch))
            if z not in union:continue
            total+=math.prod(bb[a] for a in ch)*math.exp(len(union)+xi*sum(len(smallsupports[a]) for a in ch))
        cc.append(total)
    check("atom_to_polymer_majorant_enumerated",max(cc)<=maxq and maxq<0.25,
          exact_finite_positive_sums=cc,majorant=maxq)

    # Matrix-valued second-moment window inequality, with actual off-diagonal
    # source covariances and a three-dimensional degenerate free seed.
    rng=np.random.default_rng(20260904)
    Eseed=8/3; half=1/12; duration=1.1
    H0=np.diag([Eseed]*3+[4.2,5.1,6.3,7.2])
    R=rng.normal(size=(7,7))+1j*rng.normal(size=(7,7))
    V=(R+R.conj().T)/8
    Jmat=np.eye(7)[:,:3]
    moment_rows=[]
    for u in (0.02,0.01,0.005):
        evals,U=eigh(H0-u*V)
        psi=U.conj().T@Jmat
        lam=np.exp(-duration*evals)
        Cj=[psi.conj().T@(lam[:,None]**j*psi) for j in range(3)]
        c=math.exp(-duration*Eseed)
        W=Cj[2]-2*c*Cj[1]+c*c*Cj[0]
        d=c*(1-math.exp(-duration*half))
        inside=np.abs(evals-Eseed)<half
        Z=psi[inside].conj().T@psi[inside]
        lower=Cj[0]-W/(d*d)
        margin=float(np.linalg.eigvalsh(Z-lower)[0])
        moment_rows.append({'u':u,'variance_norm':float(np.linalg.norm(W,2)),
            'inside_gram_min':float(np.linalg.eigvalsh(Z)[0]),'inequality_margin':margin})
    check("matrix_spectral_window_Chebyshev",min(x['inequality_margin'] for x in moment_rows)>-1e-12,rows=moment_rows)
    order=math.log(moment_rows[-2]['variance_norm']/moment_rows[-1]['variance_norm'],2)
    check("matrix_window_variance_quadratic",1.9<order<2.1,observed_order=order)

    # Three sources can span only three directions even when a fourth,
    # completely dark state belongs to the same spectral window.
    dark_energies=np.array([8/3,8/3,8/3,8/3+1/24])
    dark_sources=np.eye(4)[:,:3]
    dark_window=np.diag((np.abs(dark_energies-8/3)<1/12).astype(float))
    gram=dark_sources.T@dark_window@dark_sources
    check("positive_window_Gram_is_not_totality_negative_control",
          np.linalg.matrix_rank(dark_window)==4 and np.array_equal(gram,np.eye(3)),
          window_dimension=4,source_rank=3)
    one=np.diag([1.,0.,0.,0.])
    one_gram=dark_sources.T@one@dark_sources
    check("rank_one_projection_cannot_have_full_Gram_negative_control",
          np.linalg.matrix_rank(one_gram)==1 and np.linalg.eigvalsh(one_gram)[0]==0)

    # SU(3) one-plaquette diagnostic: actual Wilson multipliers, not a
    # heat-kernel replacement; same declared 21-character truncation on both sides.
    epss=[0.1,0.05,0.025,0.0125]
    reps=labels(5)
    log1=weyl_multipliers(epss,reps,grid)
    log2=weyl_multipliers(epss,reps,refined_grid)
    qerror=max(abs(log1[e][r]-log2[e][r])/e for e in epss for r in reps)
    check("SU3_Weyl_refinement",qerror<2e-9,energy_unit_error=qerror,grids=[grid,refined_grid],irreps=len(reps))
    reps,H0vec,V,even,odd=character_hamiltonian(5,0.01)
    idx={r:i for i,r in enumerate(reps)}
    MF=np.zeros_like(V)
    for col,(p0,q0) in enumerate(reps):
        for r in ((p0+1,q0),(p0-1,q0+1),(p0,q0-1)):
            if r in idx:MF[idx[r],col]+=1
    O=(MF-MF.T)/math.sqrt(2)
    check("SU3_literal_odd_source_normalization",abs(np.linalg.norm(O[:,idx[0,0]])-1)<1e-14 and np.max(np.abs(O+O.T))<1e-14)
    su3=[]
    for u in (0.005,0.01,0.02):
        H=np.diag(H0vec)-u*V
        eev,Uev=eigh(even.T@H@even)
        eod,Uod=eigh(odd.T@H@odd)
        vac=even@Uev[:,0]
        sourceH=Uod.T@odd.T@O@vac
        gapH=eod-eev[0]
        for eps in epss:
            tau=-1.5*log2[eps][1,0]
            m=math.ceil(1/tau);dur=m*tau
            C=np.diag(np.exp([4*log2[eps][r] for r in reps]))
            M=expm(tau*u*V/2)
            T=M@C@M
            ve,Ue=eigh(even.T@T@even)
            vo,Uo=eigh(odd.T@T@odd)
            vacW=even@Ue[:,-1]
            sourceW=Uo.T@odd.T@O@vacW
            gapW=-(np.log(vo)-np.log(ve[-1]))/tau
            rates=np.exp(-dur*gapW)
            ratesH=np.exp(-dur*gapH)
            Cw=[float(np.dot(sourceW**2,rates**j)) for j in range(3)]
            Ch=[float(np.dot(sourceH**2,ratesH**j)) for j in range(3)]
            c=math.exp(-dur*Eseed);d=c*(1-math.exp(-dur*half))
            variance=Cw[2]-2*c*Cw[1]+c*c*Cw[0]
            actual=float(np.sum(sourceW[np.abs(gapW-Eseed)<half]**2))
            lower=Cw[0]-variance/(d*d)
            su3.append({'u':u,'epsilon':eps,'clock':tau,'fine_steps':m,'duration':dur,
                        'moments_W':Cw,'moments_H_same_duration':Ch,
                        'max_moment_error':max(abs(a0-b0) for a0,b0 in zip(Cw,Ch)),
                        'variance':variance,'window_weight':actual,'certified_moment_lower_bound':lower,
                        'lowest_odd_gap':float(np.min(gapW))})
    check("SU3_finite_plaquette_window_inequality",all(r0['window_weight']+1e-11>=r0['certified_moment_lower_bound'] for r0 in su3))
    check("SU3_finite_plaquette_positive_window_weight",min(r0['window_weight'] for r0 in su3)>0.97,
          min_weight=min(r0['window_weight'] for r0 in su3),
          min_moment_bound=min(r0['certified_moment_lower_bound'] for r0 in su3),
          note="finite 21-character model, not evaluation of the conservative infinite-lattice coupling domain")
    orders={}
    for u in (0.005,0.01,0.02):
        rr=[r0 for r0 in su3 if r0['u']==u]
        orders[str(u)]=math.log(rr[-2]['max_moment_error']/rr[-1]['max_moment_error'],2)
    check("SU3_source_moments_temporal_matching",all(1.8<p0<2.2 for p0 in orders.values()),orders=orders)

    # A continuum of arbitrarily small weight destroys isolation despite
    # uniformly converging full time correlations and a uniform vacuum gap.
    Eseed=8/3;Delta=0.2;nu=0.5;times=np.arange(41,dtype=float)
    cont=np.exp(-Eseed*times)*np.sinh(Delta*times)/np.where(times==0,1,Delta*times)
    cont[0]=1
    pure=np.exp(-Eseed*times)
    neg=[]
    for eta in (0.2,0.1,0.05):
        c=(1-eta**2)*pure+eta**2*cont
        norm=float(np.sum(np.exp(nu*times)*np.abs(c-pure)))
        neg.append({'eta':eta,'weighted_correlation_error':norm,
                    'continuous_mass':eta**2,'spectral_support_has_no_gap_at_Eseed':True})
    check("correlation_convergence_not_pole_isolation_negative_control",
          abs(neg[0]['weighted_correlation_error']/neg[1]['weighted_correlation_error']-4)<1e-10 and
          all(r0['continuous_mass']>0 for r0 in neg),rows=neg)
    check("continuum_contaminant_still_has_vacuum_gap",Eseed-Delta>2.4,
          lower_spectral_edge=Eseed-Delta)

    return {'status':'PASS','source_commit':PIN,'checks_passed':len(checks),'checks':checks,
            'SU3_diagnostic_rows':su3,
            'scope':'Finite tests of the proof ingredients. SU(3) diagnostic is one closed plaquette in p+q<=5 (21 characters). Clock toy models are explicitly non-SU(3).',
            'not_established_by_tests':['infinite-volume cluster theorem','numerical physical coupling threshold',
               'isolated complete Wilson excited band','totality of the Riesz-source frame',
               'continuum limit','full WORKHOUSE CI or Lean proof']}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grid',type=int,default=192)
    parser.add_argument('--refined-grid',type=int,default=384)
    parser.add_argument('--output',type=Path,default=Path('discrete_time_certificate.json'))
    args=parser.parse_args()
    if args.grid < 32 or args.refined_grid <= args.grid:
        parser.error('require refined-grid > grid >= 32')
    result=run(args.grid,args.refined_grid)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'checks_passed':result['checks_passed'],
                      'checks':result['checks']},indent=2))

if __name__=='__main__':
    main()
