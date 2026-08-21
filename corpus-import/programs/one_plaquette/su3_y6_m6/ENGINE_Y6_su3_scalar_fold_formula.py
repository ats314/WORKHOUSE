#!/usr/bin/env python3
"""Exact sixth-order scalar Bloch/Rayleigh-Schrödinger fold identity.

For H=H0+uV, one isolated symmetry branch, intermediate normalization,
R=Q(E0-H0)^{-1}Q, v=<0|V|0>, and
S_{a1...ar}=<0|V R^{a1} V ... R^{ar} V|0>, derive E2..E6.
At Gamma the T1 triplet is scalar by cubic symmetry, so the identity applies
componentwise after all matrix-valued lower-order blocks are reduced to their
T1 scalar.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
import random
import sympy as sp

v=sp.Symbol('v')
def S(w):return sp.Symbol('S'+''.join(map(str,w)))

def derive(nmax=6):
    psi={1:{(1,):sp.Integer(1)}};E={1:v}
    for n in range(2,nmax+1):
        E[n]=sp.expand(sum(c*S(w) for w,c in psi[n-1].items()))
        if n==nmax:break
        d=defaultdict(lambda:sp.Integer(0))
        for w,c in psi[n-1].items():d[(1,)+w]+=c
        for k in range(1,n):
            for w,c in psi[n-k].items():d[(w[0]+1,)+w[1:]]-=E[k]*c
        psi[n]={w:sp.expand(c) for w,c in d.items() if sp.expand(c)!=0}
    return E

def moment(V,R,w,e0):
    x=V*e0
    for a in reversed(w):
        x=(R**a)*x
        x=V*x
    # Above adds one V too many on left if read literally; use direct construction instead.
    raise RuntimeError

def eval_moment(V,R,w,e0):
    x=V*e0
    for a in reversed(w):
        x=(R**a)*x
        if a!=w[0] or True:
            pass
    # Direct left-to-right operator construction.
    O=V
    for a in w:O=O*(R**a)*V
    return (e0.T*O*e0)[0]

def vector_recursion(H0,V,nmax=6):
    d=H0.rows;e0=sp.zeros(d,1);e0[0]=1;E0=H0[0,0]
    Q=sp.eye(d)-e0*e0.T
    # Reduced inverse on Q; the reference component is exactly zero.
    R=sp.diag(0,*[sp.factor(1/(E0-H0[i,i])) for i in range(1,d)])
    Es={1:(e0.T*V*e0)[0]};psis={0:e0}
    psis[1]=R*V*e0
    for n in range(2,nmax+1):
        Es[n]=sp.factor((e0.T*V*psis[n-1])[0])
        if n<nmax:
            rhs=V*psis[n-1]
            for k in range(1,n):rhs-=Es[k]*psis[n-k]
            psis[n]=sp.simplify(R*rhs)
    return Es,R,e0

def main():
    E=derive(6);formula=E[6]
    expected=(
        S((1,))**2*S((3,))-S((1,))*S((1,1,2))-S((1,))*S((1,2,1))+2*S((1,))*S((1,3))*v
        +S((1,))*S((2,))**2-S((1,))*S((2,1,1))+2*S((1,))*S((2,2))*v+2*S((1,))*S((3,1))*v-3*S((1,))*S((4,))*v**2
        -S((1,1))*S((1,2))-S((1,1))*S((2,1))+2*S((1,1))*S((3,))*v-S((1,1,1))*S((2,))
        +S((1,1,1,1,1))-S((1,1,1,2))*v-S((1,1,2,1))*v+S((1,1,3))*v**2+2*S((1,2))*S((2,))*v
        -S((1,2,1,1))*v+S((1,2,2))*v**2+S((1,3,1))*v**2-S((1,4))*v**3+2*S((2,))*S((2,1))*v
        -3*S((2,))*S((3,))*v**2-S((2,1,1,1))*v+S((2,1,2))*v**2+S((2,2,1))*v**2-S((2,3))*v**3
        +S((3,1,1))*v**2-S((3,2))*v**3-S((4,1))*v**3+S((5,))*v**4
    )
    assert sp.expand(formula-expected)==0
    # Exact rational matrix tests.
    rng=random.Random(20260614)
    for trial in range(12):
        d=5;energies=[0,-2,-3,-5,-7];H0=sp.diag(*energies)
        V=sp.zeros(d)
        for i in range(d):
            for j in range(i,d):
                q=sp.Rational(rng.randint(-5,5),rng.randint(1,5));V[i,j]=q;V[j,i]=q
        Es,R,e0=vector_recursion(H0,V,6);subs={v:Es[1]}
        for sym in formula.free_symbols-{v}:
            digits=tuple(int(c) for c in str(sym)[1:]);subs[sym]=eval_moment(V,R,digits,e0)
        assert sp.factor(formula.subs(subs)-Es[6])==0
    print('ALL SIXTH-ORDER SCALAR FOLD GATES PASS')
    print('E2 =',E[2]);print('E3 =',E[3]);print('E4 =',E[4]);print('E5 =',E[5]);print('E6 =',formula)

if __name__=='__main__':main()
