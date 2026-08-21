#!/usr/bin/env python3
# Exact closed form for ENGINE_TROM_tromino_o3_candidate_lift_diagnostic.py's Rayleigh function
# (W_path+ = W_path- = Wp, W_corner = Wc on the C-odd flat line):
#   alpha(k) = 12*Wp + 2*(Wp - Wc)*<S_perp>(k),  <S_perp>(k) = -2*e2(a)/e1(a),
#   a_j = 2 - 2*cos(k_j);  candidate (2/9, 2/9, 2/27): alpha = 8/3 - (16/27)*e2/e1,
#   range [8/27, 8/3], bandwidth 64/27; maxima on the BZ axes, minimum at R.
# Closed form for the candidate-lift Rayleigh function alpha(k):
#   With W_path+ = W_path- = Wp and W_corner = Wc, on the flat line:
#     alpha(k) = 12*Wp + 2*(Wp - Wc) * <S_perp>(k)
#     <S_perp>(k) = -2*e2(a)/e1(a),  a_j = 2 - 2cos k_j = 4 sin^2(k_j/2)
#   Candidate (2/9, 2/9, 2/27):
#     alpha(k) = 8/3 - (16/27)*e2(a)/e1(a)  in [8/27, 8/3], width 64/27.
import itertools, json
from collections import Counter, defaultdict
from fractions import Fraction as F
import numpy as np, sympy as sp

ORIENT=[(0,1),(0,2),(1,2)]; L=6
def shift(x,d,n=1):
    z=list(x); z[d]=(z[d]+n)%L; return tuple(z)
def boundary(x,o):
    mu,nu=ORIENT[o]; x=tuple(x)
    return [((x,mu),1),((shift(x,mu),nu),1),((shift(x,nu),mu),-1),((x,nu),-1)]
def cen(x,y): return tuple(((y[i]-x[i]+L//2)%L)-L//2 for i in range(3))
plaqs=[(x,o) for x in itertools.product(range(L),repeat=3) for o in range(3)]
pidx={p:i for i,p in enumerate(plaqs)}
link_inc=defaultdict(list)
for p in plaqs:
    for ln,sg in boundary(*p): link_inc[ln].append((pidx[p],sg))
nbrs={i:{} for i in range(len(plaqs))}
for ln,inc in link_inc.items():
    for (i,si),(j,sj) in itertools.combinations(inc,2):
        nbrs[i][j]=(si*sj,ln); nbrs[j][i]=(si*sj,ln)
bsets=[set(ln for ln,_ in boundary(*p)) for p in plaqs]
def classify(i,q,r):
    if r==i: return "bt"
    s1,s2=nbrs[i][q][0],nbrs[q][r][0]; com3=bsets[i]&bsets[q]&bsets[r]
    if r in nbrs[i]:
        return ("sl" if len(com3)==1 else "co")
    return "p+" if s1*s2>0 else "p-"
tables=defaultdict(Counter)
for i in [pidx[((0,0,0),o)] for o in range(3)]:
    oi=plaqs[i][1]
    for q in nbrs[i]:
        for r in nbrs[q]:
            cls=classify(i,q,r); xr,orr=plaqs[r]
            tables[cls][(oi,orr,cen((0,0,0),xr),nbrs[i][q][0]*nbrs[q][r][0])]+=1
k1,k2,k3=sp.symbols("k1 k2 k3",real=True); kk=(k1,k2,k3)
def bloch(cls):
    M=sp.zeros(3,3)
    for (oi,orr,d,s),m in tables[cls].items():
        M[oi,orr]+=m*s*sp.exp(sp.I*sum(kk[t]*d[t] for t in range(3)))
    return sp.expand(M)
Bp,Bm,Bc=bloch("p+"),bloch("p-"),bloch("co")
u=[1-sp.exp(sp.I*q) for q in kk]
w=sp.Matrix([sp.conjugate(u[2]),-sp.conjugate(u[1]),sp.conjugate(u[0])])
a=[2-2*sp.cos(q) for q in kk]
e1=sum(a); e2=a[0]*a[1]+a[0]*a[2]+a[1]*a[2]
Wp,Wc=sp.Rational(2,9),sp.Rational(2,27)
M=Wp*(Bp+Bm)+Wc*Bc
num=sp.expand((w.H*M*w)[0]); den=sp.expand((w.H*w)[0])
target=12*Wp - 2*(Wp-Wc)*2*e2/e1   # alpha = 12Wp + 2(Wp-Wc)<S_perp>, <S_perp>=-2 e2/e1
ident = num*e1 - (12*Wp*e1 - 4*(Wp-Wc)*e2)*den
expr = sp.simplify(sp.expand(ident.rewrite(sp.exp)))
assert expr == 0, "closed-form identity failed"
print("GATE PASS :: symbolic identity  alpha(k) = 12*Wp - 4*(Wp-Wc)*e2(a)/e1(a)  with a_j = 2-2cos k_j")
# numeric spot checks + extrema statement
fA=sp.lambdify(kk,num/den,"numpy")
rng=np.random.default_rng(1)
ok=True
for _ in range(40):
    kv=rng.uniform(0.2,2*np.pi-0.2,3)
    av=[2-2*np.cos(x) for x in kv]
    pred=12*float(Wp)-4*float(Wp-Wc)*(av[0]*av[1]+av[0]*av[2]+av[1]*av[2])/sum(av)
    ok &= abs(complex(fA(*kv)).real-pred)<1e-10
print("40 random-k numeric checks:",ok)
print("extrema: alpha=8/3 on the entire BZ axes (e2=0), alpha=8/27 at R; width 8/3-8/27 =",F(8,3)-F(8,27))
