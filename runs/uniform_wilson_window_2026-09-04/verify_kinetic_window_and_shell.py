#!/usr/bin/env python3
"""Checks for the Wilson kinetic window and finite-order dressed-shell matching.

Analytic high-irrep exclusion is proved in UNIFORM_WILSON_WINDOW.md. A finite
numerical sweep cannot prove that exclusion or an all-orders interacting band.
The local multiplier quadrature is reused unmodified from the supplied bundle.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp
import mpmath as mp
from wilson_clock import casimir, dimension, labels, weyl_multipliers, character_hamiltonian
from exact_su3_laplace import derive

CF=Fraction(4,3); ES=Fraction(8,3); T3=Fraction(5,612)

def D(tau:float,gap:float)->float:
    if tau<=0 or gap==0: raise ValueError('positive clock and nonzero gap required')
    return tau/(2*math.tanh(tau*gap/2))

def shell_data(logs:dict[tuple[int,int],float])->dict:
    tau=-2*logs[1,0]/float(CF)
    energy=lambda r: -logs[r]/tau
    channels=[('singlet',1/9,0.0),('adjoint',8/9,energy((1,1))),
              ('antisymmetric',1/3,energy((1,0))),('symmetric',2/3,energy((2,0)))]
    weights={name:-n*D(tau,float(CF)+e) for name,n,e in channels}
    A=weights['singlet']+weights['adjoint']
    B=weights['antisymmetric']+weights['symmetric']
    t=B-A
    dF=D(tau,float(ES))
    ell=A+B+2*dF
    sigma=-D(tau,4*energy((2,0))-float(ES))
    flat=sigma+2*dF+12*ell-4*t
    return {'clock':tau,'t':t,'ell':ell,'flat_scalar':flat,'source_gram_u_coefficient':-2*dF,
            'weights':weights,'adjoint_energy':energy((1,1)), 'sextet_energy':energy((2,0))}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--grid',type=int,default=384)
    ap.add_argument('--refined-grid',type=int,default=768)
    ap.add_argument('--cutoff',type=int,default=20)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('window_shell_certificate.json'))
    args=ap.parse_args()
    if args.cutoff<5: raise ValueError('cutoff at least 5 required')
    checks=[]
    def ck(name, condition, **detail):
        checks.append({'name':name,'passed':bool(condition),**detail})
        if not condition: raise AssertionError(json.dumps(checks[-1],indent=2))
    exact=derive()
    ck('Cartan_exact_fundamental_clock_through_cubic',exact['fundamental_clock_through_epsilon3']=='13*eps**3/144 + 7*eps**2/24 + eps')
    ck('Cartan_exact_adjoint_and_sextet_calibrated_corrections',
       exact['representations']['Adj']['calibrated_energy_through_epsilon2']=='3/2 - 5*eps**2/96'
       and exact['representations']['Sym2']['calibrated_energy_through_epsilon2']=='5/3 - 5*eps**2/72')
    # Exact second-order transfer perturbation: direct T2 plus reduced T1T1.
    c,d,tau=sp.symbols('c d tau', positive=True)
    raw=sp.factor(tau**2*(c+d)/4+tau**2*(c+d)**2/(4*(c-d)))
    ck('transfer_direct_and_fold_terms_give_coth',sp.simplify(-raw/(tau*c)+tau*(c+d)/(2*(c-d)))==0)
    # The four channel moments. Signs are mixed positive, like negative in t.
    channel=[(sp.Rational(1,9),sp.Rational(4,3),1),
             (sp.Rational(8,9),sp.Rational(17,6),1),
             (sp.Rational(1,3),sp.Rational(2),-1),
             (sp.Rational(2,3),sp.Rational(3),-1)]
    ck('continuous_time_four_channel_hopping',sum(n*sg/g for n,g,sg in channel)==sp.Rational(5,612))
    ck('heat_kernel_quadratic_temporal_error_cancels',sum(n*sg*g for n,g,sg in channel)==0)
    hk4=-sum(n*sg*g**3 for n,g,sg in channel)/720
    ck('heat_kernel_first_hopping_error_is_quartic',hk4==sp.Rational(1,3888),coefficient=str(hk4))
    # Exact leading calibrated coefficients, no interpolation.
    t2=sp.Rational(175,280908)
    calculated=sp.Rational(2,3)*(-sp.Rational(5,72))/9-sp.Rational(8,9)*(-sp.Rational(5,96))/(sp.Rational(17,6)**2)
    ell2=-sp.Rational(5,972)-sp.Rational(5,867)
    flat2=sp.Rational(3,32)+12*ell2-4*t2
    ck('calibrated_hopping_error_exact',calculated==t2,coefficient=str(t2))
    ck('calibrated_flat_scalar_error_exact',flat2==-sp.Rational(89159,2247264),coefficient=str(flat2))
    ck('source_first_Gram_coefficient_error',-sp.Rational(8,3)/6==-sp.Rational(4,9))
    # Free SU(3) arithmetic independent of the old kernel.
    nums=sorted({p*p+q*q+p*q+3*p+3*q for p in range(8) for q in range(8)}-{0})
    low=[x for x in nums if x<18]
    sem={0}
    for _ in range(4): sem|={a+b for a in list(sem) for b in low if a+b<=18}
    ck('kinematic_neighbours_14_16_17',low==[4,9,10,16] and 15 not in sem and {14,16,17}<=sem)
    ck('common_contour_clearance', min(sp.Rational(1,12)-sp.Rational(1,24), sp.Rational(17,6)-sp.Rational(1,24)-(sp.Rational(8,3)+sp.Rational(1,12)))==sp.Rational(1,24))
    # Grid refinement scan, never labelled an all-irrep certificate.
    epss=[0.1,0.05,0.025,0.0125,0.00625]
    reps=labels(args.cutoff)
    first=weyl_multipliers(epss,reps,args.grid)
    refined=weyl_multipliers(epss,reps,args.refined_grid)
    err=max(abs(first[e][r]-refined[e][r])/e for e in epss for r in reps)
    ck('finite_irrep_scan_grid_refinement',err<2e-8,maximum_energy_unit_difference=err,irreps=len(reps),grids=[args.grid,args.refined_grid])
    rows=[]; windows=[]
    for e in epss:
        row=shell_data(refined[e]);row['epsilon']=e
        row['t_error']=row['t']-float(T3)
        row['flat_error']=row['flat_scalar']-float(Fraction(11,306))
        row['source_gram_coefficient_error']=row['source_gram_u_coefficient']+.75
        row['t_error_over_epsilon2']=row['t_error']/e**2
        row['flat_error_over_epsilon2']=row['flat_error']/e**2
        row['source_error_over_epsilon2']=row['source_gram_coefficient_error']/e**2
        rows.append(row)
        tau=row['clock']
        energies={r:-refined[e][r]/tau for r in reps}
        ordinary=[v for r,v in energies.items() if r not in [(0,0),(1,0),(0,1)]]
        # Enumerate all low-energy multisets within the scan, grouping conjugates.
        rr=[r for r in reps if r!=(0,0) and r[0]>=r[1] and energies[r]<3.1]
        sums=[]
        for n in range(1,5):
            for comb in itertools.combinations_with_replacement(rr,n):
                E=sum(energies[r] for r in comb)
                if E<3.1:
                    classical=sum(float(casimir(*r))/2 for r in comb)
                    sums.append((E,classical,comb))
        cluster=[v for v,c,_ in sums if abs(c-float(ES))<1e-12]
        other=[v for v,c,_ in sums if abs(c-float(ES))>=1e-12]
        clearance=min([1/12-abs(v-float(ES)) for v in cluster]+[abs(v-float(ES))-1/12 for v in other])
        windows.append({'epsilon':e,'smallest_nonfundamental_energy_in_scan':min(ordinary),
                        'kinematic_target_cluster_min':min(cluster),'kinematic_target_cluster_max':max(cluster),
                        'contour_clearance_in_scanned_multisets':clearance,'multiset_count_below_3_1':len(sums)})
    ck('finite_scan_preserves_one_link_shelves',all(r['smallest_nonfundamental_energy_in_scan']>1.49 for r in windows),rows=windows)
    ck('finite_scan_common_contour_clearance',min(r['contour_clearance_in_scanned_multisets'] for r in windows)>1/24)
    ck('actual_transfer_hopping_positive_in_scan',all(r['t']>0 for r in rows))
    ck('hopping_leading_coefficient_holdout',abs(rows[-1]['t_error_over_epsilon2']/float(t2)-1)<.025)
    ck('flat_scalar_leading_coefficient_holdout',abs(rows[-1]['flat_error_over_epsilon2']/float(flat2)-1)<.025)
    ck('source_Gram_leading_coefficient_holdout',abs(rows[-1]['source_error_over_epsilon2']/(-4/9)-1)<.025)
    orders={key:math.log(abs(rows[-2][key]/rows[-1][key]),2) for key in ['t_error','flat_error','source_gram_coefficient_error']}
    ck('weighted_local_coefficients_second_order_in_epsilon',all(1.9<x<2.1 for x in orders.values()),orders=orders)
    # High precision heat-kernel coth test, so quartic cancellation is not lost to rounding.
    mp.mp.dps=60
    he=[]
    for h in [mp.mpf('0.05'),mp.mpf('0.025'),mp.mpf('0.0125')]:
        val=sum(mp.mpf(str(n))*sg*h/(2*mp.tanh(h*mp.mpf(str(g))/2)) for n,g,sg in channel)
        he.append((val-mp.mpf(5)/612)/h**4)
    ck('heat_kernel_quartic_coefficient_numeric',abs(float(he[-1])*3888-1)<1e-3,ratios=[str(v) for v in he])
    # Source-derivative test in the supplied one-plaquette character model.
    smallreps,H0,V,ev,od=character_hamiltonian(5,0)
    ix={r:i for i,r in enumerate(smallreps)}
    f=np.zeros_like(V)
    for j,(p,q) in enumerate(smallreps):
        for r in [(p+1,q),(p-1,q+1),(p,q-1)]:
            if r in ix: f[ix[r],j]+=1
    O=(f-f.T)/math.sqrt(2)
    e=0.05; logs=refined[e];tau=rows[1]['clock']
    C=np.diag([math.exp(4*logs[r]) for r in smallreps])
    def residue(u):
        A=expm(tau*u*V/2);T=A@C@A
        _,qev=np.linalg.eigh(ev.T@T@ev);_,qod=np.linalg.eigh(od.T@T@od)
        vac=ev@qev[:,-1];odd=od@qod[:,-1]
        return abs(odd@O@vac)**2
    h=1e-4
    deriv=(residue(h)-residue(-h))/(2*h)
    expected=-2*D(tau,float(ES))
    ck('literal_Wilson_source_derivative_finite_model',abs(deriv-expected)<2e-7,derivative=deriv,expected=expected,cutoff=5)
    # Counterexample to replacing a uniform high-irrep bound by pointwise convergence.
    # Every fixed label eventually stays unchanged, while the moving label remains low.
    ck('moving_label_pollution_negative_control',all((m*m+3*m)/6>float(ES) and float(ES)/2<5*float(CF)/2 for m in [20,40,80]),
       explanation='artificial e_m(m)=E_shell/2 while all other labels retain Casimir values; pointwise convergence alone permits pollution')
    # Standard bad sequence for summing fixed-order convergence without a common bound.
    ck('nonuniform_Taylor_tail_negative_control',all((2*.5)**m==1 for m in [10,20,40]),
       explanation='f_m(u)=(2u)^m has every fixed coefficient eventually zero, but f_m(1/2)=1')
    result={'status':'PASS','checks_passed':len(checks),'checks':checks,'shell_rows':rows,'window_rows':windows,
            'exact_laplace':exact,'source_commit':'31255abac3829cb0cc1ce7c36c1852db8cdafbea',
            'environment':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
            'scope':'Exact local algebra and numerical checks. The uniform kinetic theorem is analytical. Complete interacting Wilson-shell all-orders matching is NOT established.',
            'not_established':['numerical universal epsilon threshold','Wilson uniform all-orders marked-cluster bound','complete nonperturbative Wilson source frame','spatial continuum limit','remote WORKHOUSE CI']}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks_passed':len(checks),'orders':orders,'shell_rows':rows,'window_rows':windows},indent=2))

if __name__=='__main__': main()
