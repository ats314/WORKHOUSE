import gzip,json,itertools,mpmath as mp
from collections import defaultdict
from fractions import Fraction as F
mp.mp.dps=50
recs=json.load(gzip.open('DATA_Y4_full_real_space_h4_kernel.json.gz'))['kernel']
basis=[(0,1),(0,2),(1,2)]; idx={frozenset(p):i for i,p in enumerate(basis)}
H=[[defaultdict(F) for _ in range(3)] for __ in range(3)]
for r in recs:
    a=idx[frozenset(r['input_plane'])]; b=idx[frozenset(r['output_plane'])]
    H[b][a][tuple(r['displacement'])]+=F(r['weight'])
def pmul(A,B):
    o=defaultdict(F)
    for ea,ca in A.items():
        for eb,cb in B.items(): o[(ea[0]+eb[0],ea[1]+eb[1],ea[2]+eb[2])]+=ca*cb
    return {e:c for e,c in o.items() if c}
def padd(*ps):
    o=defaultdict(F)
    for p in ps:
        for e,c in p.items(): o[e]+=c
    return {e:c for e,c in o.items() if c}
def conj(p): return {(-e[0],-e[1],-e[2]):c for e,c in p.items()}
zx={(1,0,0):F(1)};zy={(0,1,0):F(1)};zz={(0,0,1):F(1)};one={(0,0,0):F(1)}
psi=[padd(zz,{e:-c for e,c in one.items()}),padd(one,{e:-c for e,c in zy.items()}),padd(zx,{e:-c for e,c in one.items()})]
bp=[conj(p) for p in psi]
N=defaultdict(F); D=defaultdict(F)
for i in range(3):
    for j in range(3):
        for e,c in pmul(pmul(bp[i],dict(H[i][j])),psi[j]).items(): N[e]+=c
    for e,c in pmul(bp[i],psi[i]).items(): D[e]+=c
N={e:c for e,c in N.items() if c}; D={e:c for e,c in D.items() if c}
print("N terms",len(N),"D terms",len(D))
# (B) INDEPENDENT symmetry check: N,D invariant under all 8 reflections AND 6 permutations
def tf(p,perm,flip): return {tuple(flip[i]*((e[perm[0]],e[perm[1]],e[perm[2]])[i]) for i in range(3)):c for e,c in p.items()}
refl_ok=all(tf(P,(0,1,2),f)==P for P in (N,D) for f in itertools.product((-1,1),repeat=3))
perm_ok=all(tf(P,p,(1,1,1))==P for P in (N,D) for p in itertools.permutations(range(3)))
print("INDEP reflection symmetry of N,D:",refl_ok,"  permutation symmetry:",perm_ok,
      " => [0,pi]^3 reduction valid" if (refl_ok and perm_ok) else " => REDUCTION INVALID")
# (C) INDEP curvatures d^2 c4/d|k|^2 at Gamma and R along [100],[110],[111]
def cN(k):
    s=mp.mpc(0)
    for e,c in N.items(): s+=mp.mpf(c.numerator)/c.denominator*mp.e**(1j*(e[0]*k[0]+e[1]*k[1]+e[2]*k[2]))
    return s
def cD(k):
    s=mp.mpf(0)
    for e,c in D.items(): s+=(mp.mpf(c.numerator)/c.denominator*mp.e**(1j*(e[0]*k[0]+e[1]*k[1]+e[2]*k[2]))).real
    return s
cG=F(-20721577909065127111,7250590288602460800); cR=F(-3447362930970494909,1450118057720492160)
def curv(center,dvec):
    import math
    d=[mp.mpf(x) for x in dvec]; nrm=mp.sqrt(sum(x*x for x in d)); d=[x/nrm for x in d]
    t=mp.mpf('1e-4'); k=[center[i]+t*d[i] for i in range(3)]
    c4=(cN(k)/cD(k)).real
    base=mp.mpf(cG.numerator)/cG.denominator if center[0]==0 else mp.mpf(cR.numerator)/cR.denominator
    return 2*(c4-base)/t**2
aud={'G[100]':F(5,24),'G[110]':F(247051057231349,2202655210329600),'G[111]':F(132329431693349,1651991407747200),
     'R[100]':F(-132329431693349,1651991407747200)}
import math
G=(0,0,0); R=(math.pi,math.pi,math.pi)
print("\nINDEP curvature d^2c4/d|k|^2 vs audit:")
for nm,ctr,dv in [('G[100]',G,(1,0,0)),('G[110]',G,(1,1,0)),('G[111]',G,(1,1,1)),('R[100]',R,(1,0,0))]:
    got=curv(ctr,dv); a=mp.mpf(aud[nm].numerator)/aud[nm].denominator
    print(f"  {nm}: indep={mp.nstr(got,8)}  audit={mp.nstr(a,8)}  match={abs(got-a)<mp.mpf('1e-4')}")
print("\nGamma curvature anisotropic (5/24 axis vs ~0.08 diagonal) => NO single effective mass at Γ (corrects my synthesis).")
