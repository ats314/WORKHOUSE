#!/usr/bin/env python3
"""Wilson temporal-link matching in WORKHOUSE's H_E=(1/2) sum C2 units.

The SU(3) quadrature is an independent Weyl integration, not a WORKHOUSE
contraction. The plaquette test is a declared finite character truncation,
not the 3+1-dimensional lattice or an infinite-volume spectral certificate.
Requires Python >=3.10, NumPy, SciPy, and SymPy.
"""
from __future__ import annotations
import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.special import ive
import sympy as sp

PIN = '31255abac3829cb0cc1ce7c36c1852db8cdafbea'

def casimir(p: int, q: int) -> Fraction:
    if min(p,q)<0:
        raise ValueError('Dynkin labels must be nonnegative')
    return Fraction(p*p+q*q+p*q+3*p+3*q,3)

def dimension(p: int, q: int) -> int:
    return (p+1)*(q+1)*(p+q+2)//2

def labels(cutoff: int) -> list[tuple[int,int]]:
    if cutoff < 1:
        raise ValueError('cutoff must be at least 1')
    return [(p,q) for s in range(cutoff+1) for p in range(s+1) for q in [s-p]]

def weyl_multipliers(epsilons: list[float], reps: list[tuple[int,int]], grid: int=512) -> dict[float, dict[tuple[int,int],float]]:
    """Normalized character averages at beta_t=6/epsilon, periodic 2D rule.

    Returns log(lambda_R), using lambda-1 for the logarithm when possible.
    Haar's Weyl constant cancels between numerator and normalization.
    """
    if grid<32 or any(e<=0 for e in epsilons):
        raise ValueError('positive epsilon and grid>=32 required')
    theta = -np.pi+(np.arange(grid)+0.5)*(2*np.pi/grid)
    a,b = np.meshgrid(theta,theta,indexing='ij')
    c = -a-b
    e1 = np.exp(1j*a)+np.exp(1j*b)+np.exp(1j*c)
    e2 = e1.conjugate()
    h=[np.ones_like(e1), e1]
    for n in range(2,max(p+q+1 for p,q in reps)+1):
        h.append(e1*h[n-1]-e2*h[n-2]+(h[n-3] if n>=3 else 0))
    vand = (4*np.sin((a-b)/2)**2)*(4*np.sin((a-c)/2)**2)*(4*np.sin((b-c)/2)**2)
    cost = 4*(np.sin(a/2)**2+np.sin(b/2)**2+np.sin(c/2)**2)
    weights={eps: vand*np.exp(-cost/eps) for eps in epsilons}
    norms={eps: float(w.sum()) for eps,w in weights.items()}
    result={eps: {} for eps in epsilons}
    for p,q in reps:
        char = h[p+q]*h[q]-(h[p+q+1]*h[q-1] if q else 0)
        normalized = char.real/dimension(p,q)
        for eps in epsilons:
            delta=float(np.sum(weights[eps]*(normalized-1))/norms[eps])
            lam=1+delta
            if not 0<lam<=1+2e-12:
                raise ArithmeticError(f'Nonpositive/unphysical multiplier {(p,q),eps,lam}; refine grid or reduce irrep range')
            result[eps][p,q]=float(np.log1p(delta))
    return result

def character_hamiltonian(cutoff: int, u: float):
    """One closed four-link plaquette, class functions, p+q<=cutoff.

    H0=2 C_R, V=chi_F+chi_Fbar with SU(3) tensor-product multiplicities.
    No inference about the many-plaquette carrier is made from this model.
    """
    reps=labels(cutoff); index={r:i for i,r in enumerate(reps)}
    V=np.zeros((len(reps),len(reps)))
    for i,(p,q) in enumerate(reps):
        for target in ((p+1,q),(p-1,q+1),(p,q-1),(p,q+1),(p+1,q-1),(p-1,q)):
            if min(target)>=0 and target in index:
                V[index[target],i]+=1
    if not np.array_equal(V,V.T):
        raise AssertionError('fusion adjacency is not Hermitian')
    C=np.array([float(casimir(*r)) for r in reps])
    even=[]; odd=[]
    for p,q in reps:
        if p<q:
            vec=np.zeros(len(reps)); vec[index[p,q]]=1/np.sqrt(2); vec[index[q,p]]=1/np.sqrt(2)
            even.append(vec)
            vec=vec.copy(); vec[index[q,p]]*=-1; odd.append(vec)
        elif p==q:
            vec=np.zeros(len(reps));vec[index[p,q]]=1;even.append(vec)
    return reps,2*C,V,np.array(even).T,np.array(odd).T

def lowest_gap(H: np.ndarray, even: np.ndarray, odd: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(odd.T@H@odd)[0]-np.linalg.eigvalsh(even.T@H@even)[0])

def transfer_gap(T: np.ndarray, clock: float, even: np.ndarray, odd: np.ndarray) -> float:
    tvac=float(np.linalg.eigvalsh(even.T@T@even)[-1])
    todd=float(np.linalg.eigvalsh(odd.T@T@odd)[-1])
    return float(-(np.log(todd)-np.log(tvac))/clock)

def study(grid: int=512, refined_grid: int=1024, cutoff: int=5) -> dict:
    epss=[0.2,0.1,0.05,0.025,0.0125]
    reps=labels(cutoff)
    if cutoff<4:
        raise ValueError('study cutoff must be >=4 to retain held-out (2,2)')
    a=weyl_multipliers(epss,reps,grid)
    b=weyl_multipliers(epss,reps,refined_grid)
    checks=[]
    def check(name, passed, **detail):
        checks.append({'name':name,'passed':bool(passed),**detail})
        if not passed:
            raise AssertionError(json.dumps(checks[-1],indent=2))
    # Reconstruct the second-order Laplace correction, rather than fit it.
    n,c=sp.symbols('n c', positive=True)
    D=n*n-1
    gaussian_fundamental_fourth=D*(2*n*n-3)/(4*n)
    covariance=D*(n*n-3)/(12*n)
    char_quartic=(3*c*c-n*c/2)/24
    laplace2=sp.factor(char_quartic-c*covariance/(2*D))
    expected=c*c/8-c*(n*n-2)/(16*n)
    check('all_rank_Gaussian_and_Jacobian_assembly',sp.simplify(laplace2-expected)==0,
          lambda_second_coefficient=str(laplace2))
    check('SU3_clock_coefficient_exact',sp.simplify((n*n-2)/(8*n)).subs(n,3)==sp.Rational(7,24))
    check('SU2_clock_coefficient_exact',sp.simplify((n*n-2)/(8*n)).subs(n,2)==sp.Rational(1,8))
    diff=max(abs(a[e][r]-b[e][r])/e for e in epss for r in reps)
    check('Weyl_quadrature_grid_doubling',diff<2e-9,max_energy_difference=diff,grids=[grid,refined_grid],irreps=len(reps))
    check('conjugate_character_multipliers',max(abs(b[e][p,q]-b[e][q,p]) for e in epss for p,q in reps)<2e-12)
    # SU(2) exact Bessel-character check at held-out j=1/2,1,3/2.
    su2=[]
    for j in (0.5,1,1.5):
        e=0.002
        loglam=float(np.log(ive(int(2*j+1),4/e)/ive(1,4/e)))
        coeff=(-2*loglam/(j*(j+1)*e)-1)/e
        su2.append({'j':j,'effective_clock_coefficient':coeff})
    check('independent_SU2_Bessel_limit',max(abs(r['effective_clock_coefficient']-0.125) for r in su2)<3e-4,rows=su2)
    held=[(1,0),(1,1),(2,0),(3,0),(2,2)]
    link=[]
    for e in epss:
        tau=-2*b[e][1,0]/float(casimir(1,0))
        for r in held:
            C=float(casimir(*r));E=-b[e][r]/e;Ec=-b[e][r]/tau
            link.append({'epsilon':e,'irrep':list(r),'dimension':dimension(*r),
                         'target_energy':C/2,'raw_energy':E,'matched_energy':Ec,
                         'raw_error':E-C/2,'matched_error':Ec-C/2,
                         'clock':tau,'clock_linear_coefficient':(tau/e-1)/e})
    final=[r for r in link if r['epsilon']==epss[-1]]
    check('SU3_universal_first_temporal_correction',
          max(abs(r['raw_error']/r['epsilon']-r['target_energy']*7/24) for r in final)<0.013,
          expected_clock_coefficient='7/24',max_energy_slope_deviation=max(abs(r['raw_error']/r['epsilon']-r['target_energy']*7/24) for r in final))
    # Grid sequences are halved, so error ratios determine convergence order.
    slopes={}
    for r in held[1:]:
        rr=[x for x in link if x['irrep']==list(r)]
        raw=math.log(abs(rr[-2]['raw_error']/rr[-1]['raw_error']),2)
        matched=math.log(abs(rr[-2]['matched_error']/rr[-1]['matched_error']),2)
        slopes[str(r)]={'raw_order':raw,'matched_order':matched}
    check('held_out_irreps_improve_one_order',all(0.95<v['raw_order']<1.1 and 1.8<v['matched_order']<2.2 for v in slopes.values()),slopes=slopes)
    cases=[]
    for u in (0.05,0.2):
        rr,H0,V,ev,od=character_hamiltonian(cutoff,u)
        H=np.diag(H0)-u*V;reference=lowest_gap(H,ev,od)
        rows=[]
        for e in epss:
            logs=np.array([b[e][r] for r in rr])
            W=np.diag(np.exp(4*logs))
            tau=-2*b[e][1,0]/float(casimir(1,0))
            Mr=expm(e*u*V/2); Mc=expm(tau*u*V/2)
            Tr=Mr@W@Mr; Tc=Mc@W@Mc
            Th=Mr@np.diag(np.exp(-e*H0))@Mr
            gr=transfer_gap(Tr,e,ev,od);gc=transfer_gap(Tc,tau,ev,od);gh=transfer_gap(Th,e,ev,od)
            rows.append({'epsilon':e,'clock':tau,'reference_gap':reference,'raw_gap':gr,
                         'matched_gap':gc,'heat_gap':gh,'raw_abs_error':abs(gr-reference),
                         'matched_abs_error':abs(gc-reference),'heat_abs_error':abs(gh-reference)})
        orders={mode:math.log(rows[-2][mode+'_abs_error']/rows[-1][mode+'_abs_error'],2) for mode in ('raw','matched','heat')}
        check(f'finite_plaquette_convergence_u_{u}',0.9<orders['raw']<1.1 and 1.7<orders['matched']<2.3 and 1.8<orders['heat']<2.2,orders=orders)
        cases.append({'u':u,'cutoff_p_plus_q':cutoff,'dimension':len(rr),'orders':orders,'rows':rows})
    # The fundamental matching is fixed independently of t_3 and C_shp.
    check('wrong_time_factor_negative_control',abs(final[0]['raw_energy']/4-final[0]['target_energy'])>0.45)
    return {'status':'PASS','source_commit':PIN,'checks_passed':len(checks),'checks':checks,
            'one_link_data':link,'plaquette_cases':cases,
            'scope':'Exact asymptotic assembly plus numerical SU(3) Weyl quadrature and declared finite one-plaquette character truncation.',
            'not_established':['volume-uniform Wilson-band construction','3+1-dimensional carrier transfer spectrum','renormalized physical anisotropy','continuum limit','full WORKHOUSE test suite']}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--grid',type=int,default=512)
    ap.add_argument('--refined-grid',type=int,default=1024)
    ap.add_argument('--cutoff',type=int,default=5)
    ap.add_argument('--output',type=Path,default=Path('wilson_clock_certificate.json'))
    args=ap.parse_args()
    result=study(args.grid,args.refined_grid,args.cutoff)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'checks_passed':result['checks_passed'],
                      'checks':result['checks'],'plaquette_orders':[x['orders'] for x in result['plaquette_cases']]},indent=2))
if __name__=='__main__':
    main()
