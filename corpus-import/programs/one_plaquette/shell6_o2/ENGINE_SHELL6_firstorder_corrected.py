#!/usr/bin/env python3
"""
ENGINE_SHELL6_firstorder_corrected.py -- the shell-6 FIRST-ORDER C-odd spectrum recomputed
from the exact SU(3) Haar matrix element (not the uploaded script's hardcoded hop).

Finding: the corner-push matrix element <L'|W|L> = +1/3 (Haar, reproduced by
shell6_o2_engine2 and stated in the result note's point 3).  With H^(1) = -y W,
the first-order Hamiltonian on the shell is H1 = -(1/3) * (corner-push adjacency).
The uploaded shell6_first_order_codd_band.py instead uses hop = 1/6 (= half the
matrix element), so its excited-1+- split +/- sqrt2/3 is a FACTOR OF 2 LOW; the
correct value is +/- 2*sqrt2/3.  The qualitative conclusion (exotic channels
0--,3+-,2--,2+- degenerate at O(y); only the excited 1+- disperses) is unchanged.
"""
import sys, os, math, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_shell6_o2_engine2 as E
from fractions import Fraction as F

PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}")
    if not c: raise SystemExit("FAIL "+n)

DIRS=E.DIRS; neg=E.neg
def sp():
    o=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1,-1),repeat=3):
            M=np.zeros((3,3),int)
            for i in range(3): M[i,p[i]]=s[i]
            o.append(M)
    return o
OH=sp(); DV={d:np.array(v) for d,v in enumerate(DIRS)}
gd=lambda M,d:DIRS.index(tuple(M.dot(DV[d])))
canon=lambda s:min(tuple(list(s)[i:]+list(s)[:i]) for i in range(len(s)))

SH=E.shapes6(); N=len(SH); idx={s:i for i,s in enumerate(SH)}
# first-order matrix element matrix via the exact Haar engine (corner pushes only)
shape_edges,cmap=E.shell_states(SH)
M1=np.zeros((N,N))
for j,s in enumerate(SH):
    for m,amp in E.W_action(shape_edges[j],2,only_lens=(6,)).items():
        ck=E.canon_edges(m)
        if ck in cmap: M1[cmap[ck],j]+=float(amp)
gate("M1 symmetric", np.allclose(M1,M1.T,atol=1e-9))
vals=sorted(set(round(abs(M1[i,j]),6) for i in range(N) for j in range(N) if abs(M1[i,j])>1e-9))
gate("corner-push matrix element = 1/3 (96 entries)",
     vals==[round(1/3,6)] and int((np.abs(M1)>1e-9).sum())==96)

# symmetry projectors (O_h x C), as in the skeleton
gact=lambda s,M:canon(tuple(gd(M,d) for d in s))
revs=lambda s:canon(tuple(neg(d) for d in reversed(s)))
def permmat(f):
    P=np.zeros((N,N))
    for s in SH: P[idx[f(s)],idx[s]]=1
    return P
RHO=[permmat(lambda s,M=M:gact(s,M)) for M in OH]; Rmat=permmat(revs)
def oclass(M):
    R=M if round(np.linalg.det(M))==1 else -M; t=int(round(np.trace(R)))
    if t==3:return 'E'
    if t==0:return 'C3'
    if t==1:return 'C4'
    perm=[int(np.nonzero(R[i])[0][0]) for i in range(3)]
    return 'C2' if perm==[0,1,2] else 'C2p'
CLS=[oclass(M) for M in OH]; DET=[int(round(np.linalg.det(M))) for M in OH]
CHAR={'A1':{'E':1,'C3':1,'C2':1,'C4':1,'C2p':1},'A2':{'E':1,'C3':1,'C2':1,'C4':-1,'C2p':-1},
      'E':{'E':2,'C3':-1,'C2':2,'C4':0,'C2p':0},'T1':{'E':3,'C3':0,'C2':-1,'C4':1,'C2p':-1},
      'T2':{'E':3,'C3':0,'C2':-1,'C4':-1,'C2p':1}}
DIM={'A1':1,'A2':1,'E':2,'T1':3,'T2':3}; JOF={'A1':0,'A2':3,'E':2,'T1':1,'T2':2}
def proj(G,par):
    P=np.zeros((N,N))
    for mi in range(48):
        cv=CHAR[G][CLS[mi]]*(1 if DET[mi]==1 or par>0 else -1)
        P+=cv*RHO[mi]
    return DIM[G]/48.0*P
Podd=(np.eye(N)-Rmat)/2
H1=-M1
print("  Corrected first-order C-odd spectrum (units y; H1 = -(1/3)*adjacency):")
def chan(G,par):
    Pc=Podd@proj(G,par); u,s,_=np.linalg.svd(Pc); rk=int((s>1e-8).sum())
    if rk==0: return None,0
    B=u[:,:rk]; return sorted(np.round(np.linalg.eigvalsh(B.T@H1@B),6)), rk//DIM[G]
for G in ['A1','A2','E','T1','T2']:
    for par in (+1,-1):
        ev,mult=chan(G,par)
        if ev is None: continue
        print(f"    {JOF[G]}^{{{'+' if par>0 else '-'}-}} [{G}] mult={mult}: {[float(x) for x in sorted(set(ev))]}")
for G,par in [('A1',-1),('A2',1),('E',-1),('T2',-1),('T2',1)]:
    ev,_=chan(G,par); gate(f"exotic {JOF[G]} [{G}{'+' if par>0 else '-'}-] degenerate at O(y) (all 0)",
                           all(abs(x)<1e-9 for x in ev))
ev,_=chan('T1',1)
tgt=2*math.sqrt(2)/3
gate("CORRECTED excited 1+- split = +/- 2*sqrt2/3 (NOT sqrt2/3)",
     abs(min(ev)+tgt)<1e-6 and abs(max(ev)-tgt)<1e-6)
print(f"\n  excited 1+- O(y) split = +/- {tgt:.6f} y  (= 2*sqrt2/3; uploaded script gave sqrt2/3)")
print(f"ALL {sum(PASS)}/{len(PASS)} GATES PASSED")
