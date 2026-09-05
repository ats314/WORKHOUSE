#!/usr/bin/env python3
"""Exact SU(3) local Weyl--Laplace coefficients; no fitted rational numbers.

Integrates the Vandermonde-weighted rank-two Gaussian in Cartan coordinates.
This independently extends the supplied kinetic expansion through epsilon**3.
"""
from functools import lru_cache
import json
from pathlib import Path
import sympy as s

a,b,z=s.symbols('a b z', real=True)
x=(a,b,-a-b)
delta=(a-b,2*a+b,a+2*b)
V=s.prod(y*y for y in delta)
# exp[-2(a*a+a*b+b*b)] has covariance [[1/3,-1/6],[-1/6,1/3]].
@lru_cache(None)
def moment(i:int,j:int):
    if i<0 or j<0: return s.S.Zero
    if i+j==0: return s.S.One
    if (i+j)%2: return s.S.Zero
    if i:
        return (i-1)*s.Rational(1,3)*moment(i-2,j) - j*s.Rational(1,6)*moment(i-1,j-1)
    return (j-1)*s.Rational(1,3)*moment(0,j-2)

def gaussian(poly):
    return s.expand(sum(c*moment(i,j) for (i,j),c in s.Poly(s.expand(poly),a,b).terms()))

norm=gaussian(V)
def E(poly): return s.factor(gaussian(V*poly)/norm)
A4=sum(y**4 for y in x)/12
A6=-sum(y**6 for y in x)/360
J1=-sum(y*y for y in delta)/12
J2=sum(y**4 for y in delta)/360+sum(delta[i]**2*delta[j]**2 for i in range(3) for j in range(i+1,3))/144
D1=s.expand(A4+J1)
D2=s.expand(A6+A4*A4/2+J2+A4*J1)

def trunc(p): return s.Poly(s.expand(p),z).as_dict()
def series_mul(p,q):
    return {k: s.expand(sum(p.get(i,0)*q.get(k-i,0) for i in range(k+1))) for k in range(7)}
F={j:s.expand(s.I**j*sum(y**j for y in x)/s.factorial(j)) for j in range(7)}
Fb={j:(-1)**j*v for j,v in F.items()}
prod=series_mul(F,Fb)
FF=series_mul(F,F)
chars={'F':(F,3),'Adj':({j:prod[j]-(1 if j==0 else 0) for j in range(7)},8),
       'Sym2':({j:FF[j]-Fb[j] for j in range(7)},6)}

def coefficients(char,dim):
    f=[s.expand(char[2*j]/dim) for j in range(4)]
    d1,d2=E(D1),E(D2)
    n1=E(f[1])
    n2=E(f[2]+f[1]*D1)
    n3=E(f[3]+f[2]*D1+f[1]*D2)
    lam=[s.S.One,n1,s.factor(n2-d1*n1),s.factor(n3-d1*n2+(d1*d1-d2)*n1)]
    log=[0,lam[1],s.factor(lam[2]-lam[1]**2/2),s.factor(lam[3]-lam[1]*lam[2]+lam[1]**3/3)]
    return lam,log

def derive():
    coeff={name:coefficients(*v) for name,v in chars.items()}
    eps=s.symbols('eps')
    tau=s.expand(-s.Rational(3,2)*sum(coeff['F'][1][j]*eps**j for j in range(1,4)))
    results={}
    for name,(lam,log) in coeff.items():
        energy=s.series(-sum(log[j]*eps**j for j in range(1,4))/tau,eps,0,3).removeO().expand()
        results[name]={'lambda_coefficients':[str(v) for v in lam], 'log_coefficients':[str(v) for v in log],
                       'calibrated_energy_through_epsilon2':str(energy)}
    return {'method':'exact Cartan Gaussian moments with Weyl Vandermonde, not interpolation',
            'gaussian_vandermonde_normalization':str(norm),'density_correction_means':[str(E(D1)),str(E(D2))],
            'fundamental_clock_through_epsilon3':str(tau),'representations':results}

if __name__=='__main__':
    out=derive()
    print(json.dumps(out,indent=2))
    Path(__file__).with_name('exact_laplace_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
