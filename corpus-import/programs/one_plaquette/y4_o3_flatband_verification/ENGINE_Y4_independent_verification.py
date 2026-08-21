#!/usr/bin/env python3
"""
ENGINE_Y4_independent_verification.py — INDEPENDENT verification of the SU(3) O(y^4)
C-odd flat-band breaking result, written from scratch (does NOT import the
production engine). Reproduces from the archived 189-entry H4 kernel only:

  G2 folded formula : des-Cloizeaux H4 identity == brute-force 4th-order PT
  G3 Hermiticity    : the 189-entry H4 kernel is exactly Hermitian
  G4 momentum verdict: parity-momentum corrections match the published theorem;
                       dispersion witness c4(pi,pi,pi)-c4(pi,0,0) != 0  -> LIFT
  G5 real-space     : H4 * psi_cube leaks (max 5/48 on 6 plaquettes) -> LIFT
  + Wp,Wc parity weights, and demonstration that the 2-param closed form is
    valid ONLY on the high-symmetry sublattice (off by 5/24 at (pi/2,0,0)).

NOTEBOOK-SAFE: auto-finds the kernel; or set  KPATH = '...'  in a cell first.
(G1 engine calibration -- 3G contraction == all 2798 Stage-3F amplitudes -- is
 checked by the production engine y4_stage3h_nonresonant_corner.gate1, not here.)
"""
import random
import sympy as sp
from fractions import Fraction as F
from collections import defaultdict

# ---- notebook-safe kernel path resolution ----
import sys, os, glob, gzip, json
KPATH = globals().get("KPATH", None)   # set this in a cell to override, e.g. '/content/...json.gz'
def _find_kernel():
    fn = "DATA_Y4_full_real_space_h4_kernel.json.gz"
    cands = [a for a in sys.argv[1:] if a.endswith(".gz") and os.path.exists(a)]
    for r in [os.getcwd(), ".", "/content", "/tmp/work", "/tmp/y4/Y4_STAGE3H"]:
        cands.append(os.path.join(r, fn))
    cands += glob.glob(os.path.join(os.getcwd(), "**", fn), recursive=True)
    cands += glob.glob(os.path.join("/content", "**", fn), recursive=True)
    for c in cands:
        if c and os.path.exists(c):
            return c
    raise FileNotFoundError("kernel not found; set KPATH = '/path/to/"+fn+"' in a cell first.")
if not (KPATH and os.path.exists(KPATH)):
    KPATH = _find_kernel()
print("using kernel:", KPATH)
recs = json.load(gzip.open(KPATH))["kernel"]
print(f"loaded {len(recs)} kernel records")

PL = {(0,1):0,(0,2):1,(1,2):2}          # 0=xy 1=xz 2=yz
W = defaultdict(dict)
for r in recs:
    W[(PL[tuple(r['input_plane'])],PL[tuple(r['output_plane'])])][tuple(r['displacement'])]=F(r['weight'])

# ---- G3 exact Hermiticity ----
herm = all(W[(b,a)].get((-r[0],-r[1],-r[2]))==w for (a,b),d in W.items() for r,w in d.items())
print("G3 exact Hermiticity:", herm); assert herm

# ---- symbolic Bloch symbol + flat (cube-boundary) eigenvector ----
kx,ky,kz=sp.symbols('kx ky kz',real=True)
def expk(r): return sp.exp(sp.I*(r[0]*kx+r[1]*ky+r[2]*kz))
H=sp.zeros(3,3)
for (a,b),d in W.items():
    H[b,a]+=sum(sp.Rational(w.numerator,w.denominator)*expk(r) for r,w in d.items())
psi=sp.Matrix([sp.exp(sp.I*kz)-1,-(sp.exp(sp.I*ky)-1),sp.exp(sp.I*kx)-1])
def c4_at(v):
    s={kx:v[0],ky:v[1],kz:v[2]}; Hn=H.subs(s); pn=psi.subs(s)
    return sp.nsimplify(sp.simplify((pn.H*Hn*pn)[0]/(pn.H*pn)[0]))
pi=sp.pi
one,two,three=c4_at((pi,0,0)),c4_at((pi,pi,0)),c4_at((pi,pi,pi))
THEO=dict(one=sp.Rational(-17700498622147435111,7250590288602460800),
          two=sp.Rational(-4367164159624988707,1812647572150615200),
          three=sp.Rational(-3447362930970494909,1450118057720492160))
print("G4 parity match:", one==THEO['one'], two==THEO['two'], three==THEO['three'])
assert one==THEO['one'] and two==THEO['two'] and three==THEO['three']
witness=sp.nsimplify(three-one)
print("   dispersion witness c4(pi,pi,pi)-c4(pi,0,0) =",witness,"=",float(witness))
assert witness==sp.Rational(17607806155349,275331901291200) and witness!=0
print("   -> band LIFTS at O(y^4)")

# ---- parity-extracted geometry weights ----
Wp=sp.nsimplify(one/12); Wc=sp.nsimplify((three+4*Wp)/16)
print("Wp =",Wp); print("Wc =",Wc); print("Wp-Wc =",sp.nsimplify(Wp-Wc),"!= 0 -> LIFT")

# ---- closed form fails off the parity sublattice ----
def closed(v):
    a=[2-2*sp.cos(x) for x in v]; e1=sum(a); e2=a[0]*a[1]+a[0]*a[2]+a[1]*a[2]
    return sp.nsimplify(12*Wp-4*(Wp-Wc)*e2/e1)
g=(pi/2,0,0)
print("closed-form @(pi/2,0,0): kernel - closed =",sp.nsimplify(c4_at(g)-closed(g)),
      "(both have e2/e1=0) -> closed form holds only on parity sublattice")

# ---- G5 real-space cube residual ----
psi_c={(2,(1,0,0)):F(1),(2,(0,0,0)):F(-1),(1,(0,1,0)):F(-1),(1,(0,0,0)):F(1),(0,(0,0,1)):F(1),(0,(0,0,0)):F(-1)}
img=defaultdict(lambda:F(0))
for (a,R),c in psi_c.items():
    for (aa,b),d in W.items():
        if aa==a:
            for r,w in d.items(): img[(b,(R[0]+r[0],R[1]+r[1],R[2]+r[2]))]+=c*w
img={k:v for k,v in img.items() if v}
cset={img[f]/c for f,c in psi_c.items()}; assert len(cset)==1
c4r=cset.pop()
resid={k:(img[k]-(c4r*psi_c[k] if k in psi_c else 0)) for k in img}; resid={k:v for k,v in resid.items() if v}
mx=max(abs(v) for v in resid.values())
print("G5 cube image",len(img),"| residual",len(resid),"| max leakage",mx,"on",
      sum(1 for v in resid.values() if abs(v)==mx),"plaquettes | rigid c4=",c4r)
assert len(img)==36 and len(resid)==30 and mx==F(5,48)

# ---- G2 folded des-Cloizeaux formula vs brute-force PT ----
def folded_ok(seed):
    random.seed(seed); n=5; E0=F(0); diag=[E0]+[F(random.randint(2,6)) for _ in range(n-1)]
    V=sp.Matrix(n,n,lambda i,j:random.randint(-3,3)); V=V+V.T; y=sp.symbols('y')
    P=sp.zeros(n,n); P[0,0]=1; Q=sp.eye(n)-P; a=(P*V*P)[0,0]
    Rd=sp.zeros(n,n)
    for i in range(1,n): Rd[i,i]=1/(E0-diag[i])
    R=Q*Rd*Q; s=lambda X:(P*X*P)[0,0]
    H4f=(s(V*R*V*R*V*R*V)-a*(s(V*R*R*V*R*V)+s(V*R*V*R*R*V))+a*a*s(V*R*R*R*V)
         -sp.Rational(1,2)*(s(V*R*V)*s(V*R*R*V)+s(V*R*R*V)*s(V*R*V)))
    M=sp.diag(*[int(d) for d in diag])+y*V; lam=sp.symbols('lam'); cp=M.charpoly(lam).as_expr(); cks=[E0]
    for o in range(1,5):
        ck=sp.symbols('ck'); ls=sum(cks[i]*y**i for i in range(len(cks)))+ck*y**o
        cks.append(sp.nsimplify(sp.solve(sp.series(cp.subs(lam,ls),y,0,o+1).removeO().coeff(y,o),ck)[0]))
    return sp.simplify(cks[4]-sp.nsimplify(H4f))==0
g2=all(folded_ok(s) for s in (1,2,3))   # 3 seeds (fast); add more for extra assurance
print("G2 folded formula == brute-force PT:",g2); assert g2
print("\nALL INDEPENDENT GATES PASS -> C-odd flat band LIFTS at O(y^4).")
