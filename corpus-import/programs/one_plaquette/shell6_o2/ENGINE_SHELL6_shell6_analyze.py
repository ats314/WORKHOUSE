#!/usr/bin/env python3
"""ENGINE_SHELL6_shell6_analyze.py -- build the full 32x32 zero-momentum H2 on hexagon shapes
from the reference-hexagon row (cache-warm run of shell6_final2), gate Hermiticity
+ O_h x C commutation, and read ALL C-odd channel O(y^2) energies by irrep
projection (robust to the single-reference den=0 that hid 3+-)."""
import sys, os, itertools
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_HAAR_shell6_final2 as Sf
import ENGINE_FLUX_shell6_o2_engine2 as G
DIRS=G.DIRS
PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}",flush=True)
    if not c: raise SystemExit("FAIL "+n)

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
gact=lambda s,M:canon(tuple(gd(M,d) for d in s)); rev=lambda s:canon(tuple((d^1) for d in reversed(s)))
def oclass(M):
    Rm=M if round(np.linalg.det(M))==1 else -M; t=int(round(np.trace(Rm)))
    if t==3:return 'E'
    if t==0:return 'C3'
    if t==1:return 'C4'
    return 'C2' if [int(np.nonzero(Rm[i])[0][0]) for i in range(3)]==[0,1,2] else 'C2p'
CH={'A1':{'E':1,'C3':1,'C2':1,'C4':1,'C2p':1},'A2':{'E':1,'C3':1,'C2':1,'C4':-1,'C2p':-1},
    'E':{'E':2,'C3':-1,'C2':2,'C4':0,'C2p':0},'T1':{'E':3,'C3':0,'C2':-1,'C4':1,'C2p':-1},
    'T2':{'E':3,'C3':0,'C2':-1,'C4':-1,'C2p':1}}
DIM={'A1':1,'A2':1,'E':2,'T1':3,'T2':3}; JOF={'A1':0,'A2':3,'E':2,'T1':1,'T2':2}
CLS=[oclass(M) for M in OH]; DET=[int(round(np.linalg.det(M))) for M in OH]

def main():
    SH,L0,Hrow=Sf.run(1)            # Hrow[shape] = H2[shape, L0] (cache warm => fast)
    HEX=[s for s in SH if len(set(d//2 for d in s))==3]; N=len(HEX); idx={s:i for i,s in enumerate(HEX)}
    gate("L0 is a hexagon", L0 in HEX)
    # group element mapping L0 -> each hexagon (and inverse action)
    def applyg(s,M,c): t=gact(s,M); return rev(t) if c else t
    gof={}
    for c in (0,1):
        for M in OH:
            t=applyg(L0,M,c)
            if t not in gof: gof[t]=(M,c)
    gate("all 32 hexagons are one O_hxC orbit of L0", all(h in gof for h in HEX) and len(gof)>=N)
    # full matrix: M2[i][j] = H2[hex_i, hex_j] = Hrow[ g_j^{-1} . hex_i ]
    def ginv_apply(s,M,c):
        # g=(M,c): s-> (rev^c)(gact(s,M)); inverse = (M^T, c) applied as gact then rev^c... careful order
        # g^{-1}: first undo reversal (rev is involutive, commutes), then gact(.,M^T)
        t=rev(s) if c else s
        return gact(t, M.T)
    M2=[[F(0)]*N for _ in range(N)]
    for j,hj in enumerate(HEX):
        Mj,cj=gof[hj]
        for i,hi in enumerate(HEX):
            pre=ginv_apply(hi,Mj,cj)
            M2[i][j]=Hrow.get(pre,F(0))
    M2n=np.array([[float(x) for x in r] for r in M2])
    gate("full H2 symmetric (Hermitian)", np.allclose(M2n,M2n.T,atol=1e-9))
    # commutes with O_h x C
    def permmat(M,c):
        P=np.zeros((N,N))
        for h in HEX: P[idx[applyg(h,M,c)],idx[h]]=1
        return P
    okcomm=all(np.allclose(M2n@permmat(M,c),permmat(M,c)@M2n,atol=1e-9) for M in OH[:12] for c in (0,1))
    gate("H2 commutes with O_h x C (sampled)", okcomm)
    # irrep projectors on the 32 hexagons; read channel energies as block eigenvalues
    def proj(Gname,Ps,Cs):
        P=np.zeros((N,N))
        for c in (0,1):
            for mi,M in enumerate(OH):
                chi=CH[Gname][CLS[mi]]*(1 if DET[mi]==1 else Ps)*(1 if c==0 else Cs)
                P+=chi*permmat(M,c)
        return DIM[Gname]/96.0*P
    print("\n  C-odd channel O(y^2) energies (units y^2; common self-energy incl.):",flush=True)
    energies={}
    for Gname in ['A1','A2','E','T1','T2']:
        for Cs in (-1,1):
            for Ps in (-1,1):
                P=proj(Gname,Ps,Cs)
                if Cs==1 and Ps==1: pass
                u,s,_=np.linalg.svd(P); rk=int((s>1e-8).sum())
                if rk==0: continue
                B=u[:,:rk]; ev=np.linalg.eigvalsh(B.T@M2n@B)
                lab=f"{JOF[Gname]}^{{{'+' if Ps>0 else '-'}{'+' if Cs>0 else '-'}}}"
                vals=sorted(set(round(float(x),6) for x in ev))
                energies[(Gname,Ps,Cs)]=vals
                if Cs==-1:
                    print(f"    {lab:9s}[{Gname}] mult={rk//DIM[Gname]}: {vals}",flush=True)
    # headline C-odd exotic channels
    def one(Gn,Ps,Cs):
        v=energies.get((Gn,Ps,Cs)); return v[0] if v else None
    chans={'0^{--}':('A1',-1,-1),'3^{+-}':('A2',1,-1),'2^{--}(E)':('E',-1,-1),
           '2^{--}(T2)':('T2',-1,-1),'2^{+-}':('T2',1,-1)}
    print("\n  EXOTIC C-odd channels:",flush=True)
    got={}
    for nm,(Gn,Ps,Cs) in chans.items():
        v=one(Gn,Ps,Cs); got[nm]=v
        print(f"    {nm:12s}: {v}")
    pure={k:got[k] for k in ['0^{--}','3^{+-}','2^{--}(E)','2^{--}(T2)'] if got[k] is not None}
    order=sorted(pure,key=lambda k:pure[k])
    print(f"\n  ORDERING (light->heavy at O(y^2)): {' < '.join(order)}")
    b=got['0^{--}']
    print("  splittings vs 0--:")
    for k in order: print(f"    {k:12s}: {pure[k]-b:+.6f}")
    print(f"\n  gates {sum(PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
