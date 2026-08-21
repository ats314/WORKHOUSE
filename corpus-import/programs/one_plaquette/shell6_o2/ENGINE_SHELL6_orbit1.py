#!/usr/bin/env python3
"""ENGINE_SHELL6_orbit1.py -- channel O(y^2) energy for an arbitrary reference hexagon
(needed for 3+-, which lives in the size-8 orbit separate from L0).  Same engine,
same persistent cache.  Computes the Rayleigh quotient E_Gamma from the reference
hexagon's H2 row."""
import sys, os, itertools
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_HAAR_shell6_final2 as Sf
import ENGINE_FLUX_shell6_o2_engine2 as G
import link_o2_v2 as E
DIRS=G.DIRS
import ENGINE_SHELL6_shell6_analyze as A   # OH, gact, rev, oclass, CH, DIM, JOF, CLS, DET

def hexrow(ref, rowbox=2):
    L0e=Sf.edges_at(ref,(0,0,0)); H0=E.make_H0_links(); Ww=Sf.connected_W(L0e,1)
    L0w=E.canon_word(Sf.woe(L0e)); v=E.apply_W_links(L0w,Ww)
    basis=set(v.keys()); fr=list(v.keys())
    while fr:
        m=fr.pop()
        for mm in H0.mono(m):
            if mm not in basis: basis.add(mm); fr.append(mm)
    man=[{m:F(1)} for m in basis if Sf.is_e0(m)]
    print(f"  ref={ref}: closure={len(basis)} model={len(man)}",flush=True)
    y=Sf.resolvent(H0,F(4),man,v,'ref'); Wy=E.apply_W_links(y,Ww); Sf._save()
    Wylinks=set(l for m in Wy for w in m for (l,p) in w); wysig=set(Sf.csig(m) for m in Wy)
    SH=G.shapes6(); HEX=[s for s in SH if len(set(d//2 for d in s))==3]
    H2={}
    for s in HEX:
        for tt in itertools.product(range(-rowbox,rowbox+1),repeat=3):
            es=Sf.edges_at(s,tt)
            if not G.is_simple_loop(es): continue
            if any(l not in Wylinks for (l,_) in es): continue
            w=E.canon_word(Sf.woe(es))
            if Sf.csig(next(iter(w))) not in wysig: continue
            val=E.inner(w,Wy)
            if val!=0: H2[s]=H2.get(s,F(0))+val
    Sf._save(); return H2

def rayleigh(ref,H2,Gname,Ps,Cs):
    num=F(0); den=0
    for c in (0,1):
        for mi,M in enumerate(A.OH):
            g=A.gact(ref,M); g=A.rev(g) if c else g
            chi=A.CH[Gname][A.CLS[mi]]*(1 if A.DET[mi]==1 else Ps)*(1 if c==0 else Cs)
            num+=chi*H2.get(g,F(0))
            if g==ref: den+=chi
    return (F(num,den), den) if den else (None,0)

def main():
    SH=G.shapes6(); HEX=[s for s in SH if len(set(d//2 for d in s))==3]
    # find orbit-1 (size-8) hexagon
    def orbit(h):
        o=set()
        for c in (0,1):
            for M in A.OH:
                t=A.gact(h,M); t=A.rev(t) if c else t; o.add(t)
        return o&set(HEX)
    L0=HEX[0]; orb0=orbit(L0)
    L1=next(h for h in HEX if h not in orb0)     # orbit-1 representative
    print(f"  L1 (orbit-1, carries 3+-) = {L1}",flush=True)
    H2=hexrow(L1)
    v,den=rayleigh(L1,H2,'A2',1,-1)
    print(f"  3^(+-) [A2+-] O(y^2) energy = {v}  ~ {float(v):+.6f}   (den={den})" if v is not None
          else f"  3+- den=0 again (ref still wrong)")
    # also self-diagonal of L1 for reference
    print(f"  (orbit-1 connected diagonal H2[L1,L1] = {H2.get(L1)})")

if __name__=="__main__":
    main()
