#!/usr/bin/env python3
"""Independent check of the O(y^5) des-Cloizeaux folded-coefficient identity
(-1/2, 1/3, 1/3, -1/4), against a NUMERICAL gold standard (mpmath eigenvalue
Taylor fit) that uses neither the uploaded RS engine nor a char-poly solve."""
import mpmath as mp, random, itertools
from fractions import Fraction as F
mp.mp.dps=70
def rand_model(n,seed):
    rng=random.Random(seed); h0=[0]+sorted(rng.sample(range(2,40),n-1))
    V=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            v=rng.randint(-4,4); V[i][j]=v; V[j][i]=v
    return h0,V
def identity_c5(h0,V,a=F(-1,2),b1=F(1,3),b2=F(1,3),c=F(-1,4)):
    E0=F(h0[0]); n=len(h0); Vm=[[F(x) for x in r] for r in V]; tot=F(0)
    for s in itertools.product(range(n),repeat=4):
        raw=Vm[0][s[3]]*Vm[s[3]][s[2]]*Vm[s[2]][s[1]]*Vm[s[1]][s[0]]*Vm[s[0]][0]
        if raw==0: continue
        d=[E0-F(h0[si]) for si in s]; nz=[x for x in d if x!=0]; z=4-len(nz)
        if z==0: x,y,w,v=d; tot+=raw/(x*y*w*v)
        elif z==1: p,q,r=nz; tot+=raw*a*(F(1)/(p*p*q*r)+F(1)/(p*q*q*r)+F(1)/(p*q*r*r))
        elif z==2: p,q=nz; tot+=raw*(b1*(F(1)/(p**3*q)+F(1)/(p*q**3))+b2*F(1)/(p*p*q*q))
        elif z==3: (p,)=nz; tot+=raw*c/(p**4)
    return tot
def numeric_c5(h0,V):
    n=len(h0)
    def Eg(y):
        M=mp.matrix([[(h0[i] if i==j else 0)+y*V[i][j] for j in range(n)] for i in range(n)])
        return mp.re(sorted(mp.eig(M,left=False,right=False),key=lambda z:abs(mp.re(z)))[0])
    pts=[mp.mpf(k)/mp.mpf(10**4) for k in range(-7,8) if k!=0]
    A=mp.matrix(len(pts),11); b=mp.matrix(len(pts),1)
    for r,yv in enumerate(pts):
        for c in range(11): A[r,c]=yv**c
        b[r]=Eg(yv)
    return mp.qr_solve(A,b)[0][5]
if __name__=='__main__':
    ok=True
    for seed in (401,402,403,404,405,406,407,408):
        for nn in (4,5):
            h0,V=rand_model(nn,seed); ps=identity_c5(h0,V); num=numeric_c5(h0,V)
            rel=abs(mp.mpf(ps.numerator)/ps.denominator-num)/(abs(num)+mp.mpf(10)**-30)
            m=rel<mp.mpf(10)**-8; ok&=m
            print(f"seed {seed} n{nn}: match={m}")
    print("\nH5 IDENTITY (-1/2,1/3,1/3,-1/4) == true c5 (gold standard):",ok)
