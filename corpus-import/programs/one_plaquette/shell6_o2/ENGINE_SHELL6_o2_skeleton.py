#!/usr/bin/env python3
"""
ENGINE_SHELL6_o2_skeleton.py  --  SYMMETRY SKELETON for the shell-6 C-odd O(y^2) computation.

Rigorous, gate-backed precursor to the second-order amplitude engine.  It settles
the GROUP THEORY the O(y^2) result must respect, BEFORE any amplitude is computed:

  1. Re-enumerate the shell-6 model space (44 loops = 32 twisted hexagons + 12
     rectangles) and re-validate the FIRST-ORDER corner-push result on the full
     44-dim space (not just the hexagons) -- confirms rectangles are first-order
     isolated and reproduces the note's exotic-degeneracy + excited-1+- split.

  2. Decompose the FULL 44-loop permutation representation under O_h x C into
     J^{PC} channels, separately for hexagons and rectangles.  This tells us the
     MULTIPLICITY of every exotic C-odd channel (0--, 3+-, 2--, 2+-) across the
     whole shell, i.e. whether the O(y^2) energy of each is a single number
     (mult 1) or an eigenvalue of a mixing block (mult >= 2, hexagon<->rectangle).

Everything here is exact integer/rational linear algebra over the cubic group.
"""
import itertools, numpy as np
from fractions import Fraction as F
np.set_printoptions(precision=4, suppress=True)

DIRS=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; neg=lambda d:d^1
PASS=[]
def gate(name,c):
    PASS.append((name,bool(c))); print(f"  GATE {'PASS' if c else 'FAIL'} :: {name}")
    if not c: raise SystemExit("gate failed")

# ---- O_h as 48 signed permutation matrices; reversal; loop helpers ----
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

def shapes6_simple():
    r=set()
    def dfs(seq,pos,vis):
        if len(seq)==6:
            if pos==(0,0,0) and neg(seq[-1])!=seq[0]: r.add(canon(seq))
            return
        for d in range(6):
            if seq and neg(seq[-1])==d: continue
            p=(pos[0]+DIRS[d][0],pos[1]+DIRS[d][1],pos[2]+DIRS[d][2])
            if p==(0,0,0):
                if len(seq)+1!=6: continue
            elif p in vis: continue
            dfs(seq+[d],p,vis|{p})
    dfs([], (0,0,0),{(0,0,0)}); return r

print("="*72,"\nSTEP 1: model space + hex/rect split")
ALL=sorted(shapes6_simple()); N=len(ALL)
idx={s:i for i,s in enumerate(ALL)}
naxes=lambda s: len(set(d//2 for d in s))
HEX=[s for s in ALL if naxes(s)==3]; RECT=[s for s in ALL if naxes(s)==2]
gate("shell-6 has 44 simple loops", N==44)
gate("44 = 32 twisted hexagons (3 axes) + 12 rectangles (2 axes)",
     len(HEX)==32 and len(RECT)==12)

# ---- first-order corner-push adjacency on ALL 44 ----
perp=lambda a,b:a//2!=b//2
A=np.zeros((N,N))
for s in ALL:
    for i in range(6):
        j=(i+1)%6; a,b=s[i],s[j]
        if perp(a,b):
            q=list(s); q[i],q[j]=q[j],q[i]; c=canon(q)
            if c in idx: A[idx[c],idx[s]]+=1
gate("first-order adjacency symmetric (Hermitian)", np.allclose(A,A.T))
rect_block=np.array([[A[idx[a],idx[b]] for b in RECT] for a in RECT])
gate("rectangles are first-order isolated (zero corner-push block)",
     np.allclose(rect_block,0))
# every corner-push edge sits inside the hexagon block
hex_idx=set(idx[s] for s in HEX)
offhex=sum(abs(A[i,j]) for i in range(N) for j in range(N)
           if (i in hex_idx)!=(j in hex_idx))
gate("all 96 corner-push edges live strictly among hexagons", offhex==0
     and int(A.sum())==96)

# ---- symmetry actions ----
gact=lambda s,M:canon(tuple(gd(M,d) for d in s))
rev =lambda s:canon(tuple(neg(d) for d in reversed(s)))
# permutation of the 44 loops by each O_h element, and by reversal
def perm_of(M):
    return [idx[gact(s,M)] for s in ALL]
PM=[perm_of(M) for M in OH]
RP=[idx[rev(s)] for s in ALL]

# class of each O_h element (E,8C3,3C2,6C4,6C2') via its proper-rotation part
def oclass(M):
    R = M if round(np.linalg.det(M))==1 else -M
    t=int(round(np.trace(R)))
    if t==3: return 'E'
    if t==0: return 'C3'
    if t==1: return 'C4'
    # t==-1: face-axis C2 (rotation part is diagonal) vs edge-axis C2'
    perm=[int(np.nonzero(R[i])[0][0]) for i in range(3)]
    return 'C2' if perm==[0,1,2] else 'C2p'
CLS=[oclass(M) for M in OH]
DET=[int(round(np.linalg.det(M))) for M in OH]

# character table of O on (E,8C3,3C2,6C4,6C2')
CHAR={'A1':{'E':1,'C3':1,'C2':1,'C4':1,'C2p':1},
      'A2':{'E':1,'C3':1,'C2':1,'C4':-1,'C2p':-1},
      'E' :{'E':2,'C3':-1,'C2':2,'C4':0,'C2p':0},
      'T1':{'E':3,'C3':0,'C2':-1,'C4':1,'C2p':-1},
      'T2':{'E':3,'C3':0,'C2':-1,'C4':-1,'C2p':1}}
DIM={'A1':1,'A2':1,'E':2,'T1':3,'T2':3}
JOF={'A1':0,'A2':3,'E':2,'T1':1,'T2':2}

# fixed-point counts chi_pi(M, c) on a chosen subset of loops
def chi_perm(subset, withrev):
    sset=set(idx[s] for s in subset)
    tot=0
    for mi,P in enumerate(PM):
        cnt=0
        for s in subset:
            i=idx[s]; j=P[i]
            if withrev: j=RP[j]
            if j==i and i in sset: cnt+=1
        # store per element handled below; here unused
    return tot
# multiplicities m(Gamma,P,Csign) over O_h x C (order 96)
def multiplicities(subset):
    sset=set(idx[s] for s in subset)
    # precompute chi_pi(M,+) and chi_pi(M,rev) restricted to subset
    chip=[]; chir=[]
    for P in PM:
        c0=sum(1 for s in subset if P[idx[s]]==idx[s])
        cr=sum(1 for s in subset if RP[P[idx[s]]]==idx[s])
        chip.append(c0); chir.append(cr)
    out={}
    for G in CHAR:
        for Psign in (+1,-1):
            for Csign in (+1,-1):
                tot=0
                for mi,M in enumerate(OH):
                    cg=CHAR[G][CLS[mi]]
                    pf=1 if DET[mi]==1 else Psign
                    tot+= chip[mi]*cg*pf*1
                    tot+= chir[mi]*cg*pf*Csign
                m=F(tot,96)
                assert m.denominator==1, (G,Psign,Csign,m)
                out[(G,Psign,Csign)]=int(m)
    return out

print("="*72,"\nSTEP 2: O_h x C content (full 44, and hex / rect separately)")
def show(name, subset):
    mult=multiplicities(subset)
    tot=sum(mult[k]*DIM[k[0]] for k in mult)
    print(f"\n  -- {name} (dim {len(subset)}; rep check sum={tot}) --")
    for (G,Ps,Cs),mu in sorted(mult.items()):
        if mu==0: continue
        pc=f"{'+' if Ps>0 else '-'}{'+' if Cs>0 else '-'}"
        print(f"     {JOF[G]}^{{{pc}}}  [{G}{pc}] : multiplicity {mu}")
    return mult,tot
mall,_=show("ALL 44", ALL)
mhex,_=show("HEXAGONS 32", HEX)
mrect,_=show("RECTANGLES 12", RECT)
gate("hex+rect multiplicities sum to full (rep additive)",
     all(mall[k]==mhex[k]+mrect[k] for k in mall))
gate("dim check: sum dim*mult == 44", sum(mall[k]*DIM[k[0]] for k in mall)==44)

print("="*72,"\nSTEP 3: the four exotic C-odd channels -- multiplicity & where they live")
EXOTIC={'0^{--}':('A1',-1,-1),'3^{+-}':('A2',+1,-1),
        '2^{--}_E':('E',-1,-1),'2^{--}_T2':('T2',-1,-1),'2^{+-}':('T2',+1,-1)}
for nm,(G,Ps,Cs) in EXOTIC.items():
    print(f"  {nm:10s} [{G}{'+' if Ps>0 else '-'}{'+' if Cs>0 else '-'}]: "
          f"full={mall[(G,Ps,Cs)]}  hex={mhex[(G,Ps,Cs)]}  rect={mrect[(G,Ps,Cs)]}")

# the excited 1+- that DOES split at first order
print(f"\n  excited 1^{{+-}} [T1+-]: full={mall[('T1',+1,-1)]} "
      f"hex={mhex[('T1',+1,-1)]} rect={mrect[('T1',+1,-1)]}")

print("="*72,"\nSTEP 4: first-order spectrum on the FULL space (C-odd), by channel")
# C-odd projector and O_h irrep projectors on the full 44-dim space
def permmat(perm):
    P=np.zeros((N,N))
    for i,j in enumerate(perm): P[j,i]=1
    return P
RHO=[permmat(P) for P in PM]; Rmat=permmat(RP)
def cval(G,par,mi):
    M=OH[mi]; dt=DET[mi]
    if dt==1: return CHAR[G][CLS[mi]]
    return CHAR[G][CLS[mi]]*(1 if par>0 else -1)
def proj(G,par):
    P=np.zeros((N,N))
    for mi in range(48): P+=cval(G,par,mi)*RHO[mi]
    return DIM[G]/48.0*P
Podd=(np.eye(N)-Rmat)/2
hop=1/6.0
print("  C-odd channel energies at O(y) on full 44 (units y, hop=+1/6):")
for G in ['A1','A2','E','T1','T2']:
    for par in (+1,-1):
        Pc=Podd@proj(G,par); u,s,_=np.linalg.svd(Pc); rk=int((s>1e-8).sum())
        if rk==0: continue
        B=u[:,:rk]; ev=np.linalg.eigvalsh(B.T@A@B)*hop
        pc=f"{'+' if par>0 else '-'}-"
        vals=sorted(set(np.round(ev,6)))
        print(f"    {JOF[G]}^{{{pc}}} [{G}{pc}] mult={rk//DIM[G]}: {[round(float(x),4) for x in vals]}")

# reproduce the note's headline numbers as gates
def chan_firstorder(G,par):
    Pc=Podd@proj(G,par); u,s,_=np.linalg.svd(Pc); rk=int((s>1e-8).sum())
    if rk==0: return []
    B=u[:,:rk]; return sorted(np.round(np.linalg.eigvalsh(B.T@A@B)*hop,6))
gate("exotic 0-- (A1--) first-order energy = 0", all(abs(x)<1e-9 for x in chan_firstorder('A1',-1)))
gate("exotic 3+- (A2+-) first-order energy = 0", all(abs(x)<1e-9 for x in chan_firstorder('A2',+1)))
gate("exotic 2-- (E--) first-order energy = 0", all(abs(x)<1e-9 for x in chan_firstorder('E',-1)))
gate("exotic 2-- (T2--) first-order energy = 0", all(abs(x)<1e-9 for x in chan_firstorder('T2',-1)))
gate("exotic 2+- (T2+-) first-order energy = 0", all(abs(x)<1e-9 for x in chan_firstorder('T2',+1)))
ev1pm=chan_firstorder('T1',+1)
import math
gate("excited 1+- (T1+-) first-order = +/- sqrt2/3",
     len(ev1pm)>=2 and abs(min(ev1pm)+math.sqrt(2)/3)<1e-6 and abs(max(ev1pm)-math.sqrt(2)/3)<1e-6)

print("="*72)
print(f"ALL {sum(p for _,p in PASS)}/{len(PASS)} GATES PASSED")
print("="*72)
