#!/usr/bin/env python3
"""
ENGINE_SHELL6_o2_compute.py -- THE shell-6 C-odd O(y^2) ordering, exact.

Engine: link-variable Gram resolvent (link_o2_v2, 39 gates: Bridge 13/20,1/2;
shell-4 hops 5/612, -11/306) with the fast TN Haar integrator.

H2[L',L0] = <L'|W R W|L0> with W = the CONNECTED plaquette neighbourhood of the
reference hexagon L0, R the Gram resolvent projecting the degenerate length-6 model
space (auto-detected in the closure).  Connected W gives the EXACT off-diagonal
(distinct hexagons couple only through connected intermediates); the diagonal
self-energy is connected-only = a common shift, so it does not affect the ORDERING.
Channel energies by O_h x C symmetry projection of the reference-hexagon H2 row.
"""
import sys, os, itertools
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_shell6_o2_engine2 as G
import link_o2_v2 as E

PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}",flush=True)
    if not c: raise SystemExit("FAIL "+n)
DIRS=G.DIRS

_LID={}
def lid_int(geo):
    if geo not in _LID: _LID[geo]=len(_LID)
    return _LID[geo]
def word_of_edges(edges):
    return tuple((lid_int(lid),pw) for (lid,pw) in G.edges_to_word(edges))
def edges_at(shape,t):
    base=G.edgeset((0,0,0),shape)
    return frozenset((((lo[0]+t[0],lo[1]+t[1],lo[2]+t[2]),ax),pw) for ((lo,ax),pw) in base)

def connected_W(L0e, layers=2):
    l2p=G.build_plaq_index(3)
    def touching(links):
        s=set()
        for lid in links:
            for pw in l2p.get(lid,()): s.add(tuple(pw))
        return s
    cur=set(lid for (lid,_) in L0e); allp=set()
    for _ in range(layers):
        p=touching(cur); allp|=p
        cur=set(lid for pwt in allp for (lid,_) in pwt)
    return [tuple((lid_int(lid),pw) for (lid,pw) in pwt) for pwt in allp]

def is_e0_loop(m):
    """canonical monomial m is a single length-6 loop of distinct links (energy 4)."""
    return len(m)==1 and len(m[0])==6 and len(set(g for g,p in m[0]))==6

def run(layers=2):
    SH=G.shapes6(); naxes=lambda s:len(set(d//2 for d in s))
    HEX=[s for s in SH if naxes(s)==3]; L0=HEX[0]; L0e=edges_at(L0,(0,0,0))
    H0=E.make_H0_links()
    Wwords=connected_W(L0e,layers)
    L0w=E.canon_word(word_of_edges(L0e))
    v=E.apply_W_links(L0w,Wwords)
    # closure (no integration) -> auto model space = E0 single 6-loops
    basis=set(v.keys()); fr=list(v.keys())
    while fr:
        m=fr.pop()
        for mm in H0.mono(m):
            if mm not in basis: basis.add(mm); fr.append(mm)
    manifold=[{m:F(1)} for m in basis if is_e0_loop(m)]
    print(f"  L0={L0}; |W|={len(Wwords)}; closure={len(basis)}; model-space 6-loops={len(manifold)}",flush=True)
    y=E.gram_resolvent(H0,F(4),manifold,v,'shell6')
    Wy=E.apply_W_links(y,Wwords)
    # first-order corner-push check
    Wl0=E.apply_W_links(L0w,Wwords)
    h1=set()
    for f in manifold:
        b=E.inner(f,Wl0); m0=next(iter(f))
        if b!=0 and m0!=next(iter(E.canon_word(word_of_edges(L0e)) if False else {next(iter(E.canon_word(word_of_edges(L0e)))):1})):
            pass
    # simpler first-order check below using shapes
    # H2 row by shape (zero momentum): sum h2[L'] over positions of each shape
    def shape_pos(m):
        # recover edge-set of a single-loop monomial via the inverse link map
        inv={i:lid for lid,i in _LID.items()}
        es=frozenset((inv[g],p) for (g,p) in m[0])
        ck=G.canon_edges(es)
        for s in SH:
            if G.canon_edges(edges_at(s,(0,0,0)))==ck: return s
        return None
    H2shape={}
    h1shape={}
    for f in manifold:
        m=next(iter(f)); sh=shape_pos(m)
        if sh is None: continue
        H2shape[sh]=H2shape.get(sh,F(0))+E.inner(f,Wy)
        h1shape[sh]=h1shape.get(sh,F(0))+(-E.inner(f,Wl0))
    # first-order: off-diagonal H1 entries should be -/+1/3 (corner pushes), L0 diagonal 0
    offh1=[abs(v) for s,v in h1shape.items() if s!=L0 and v!=0]
    gate("first-order corner-push |H1|=1/3", all(x==F(1,3) for x in offh1) and len(offh1)>0)
    return SH,HEX,L0,H2shape

def symmetry_energies(SH,HEX,L0,H2shape):
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
        R=M if round(np.linalg.det(M))==1 else -M; t=int(round(np.trace(R)))
        if t==3:return 'E'
        if t==0:return 'C3'
        if t==1:return 'C4'
        perm=[int(np.nonzero(R[i])[0][0]) for i in range(3)]
        return 'C2' if perm==[0,1,2] else 'C2p'
    CHAR={'A1':{'E':1,'C3':1,'C2':1,'C4':1,'C2p':1},'A2':{'E':1,'C3':1,'C2':1,'C4':-1,'C2p':-1},
          'E':{'E':2,'C3':-1,'C2':2,'C4':0,'C2p':0},'T1':{'E':3,'C3':0,'C2':-1,'C4':1,'C2p':-1},
          'T2':{'E':3,'C3':0,'C2':-1,'C4':-1,'C2p':1}}
    JOF={'A1':0,'A2':3,'E':2,'T1':1,'T2':2}
    CLS=[oclass(M) for M in OH]; DET=[int(round(np.linalg.det(M))) for M in OH]
    def channel_energy(G_,Ps,Cs):
        num=F(0); den=0
        for c in (0,1):
            for mi,M in enumerate(OH):
                gL0=gact(L0,M)
                if c: gL0=rev(gL0)
                chi=CHAR[G_][CLS[mi]]*(1 if DET[mi]==1 else Ps)*(1 if c==0 else Cs)
                num+= chi*H2shape.get(gL0,F(0))
                if gL0==L0: den+=chi
        return F(num,den) if den!=0 else None
    EX={'0^{--}':('A1',-1,-1),'3^{+-}':('A2',1,-1),'2^{--}(E)':('E',-1,-1),
        '2^{--}(T2)':('T2',-1,-1),'2^{+-}':('T2',1,-1),'1^{+-}exc':('T1',1,-1)}
    return {nm:channel_energy(*gpc) for nm,gpc in EX.items()}

def main():
    print("="*72,"\nSHELL-6 C-odd O(y^2) ENERGIES (exact link-variable Gram resolvent)")
    print("="*72,flush=True)
    SH,HEX,L0,H2shape=run(2)
    print(f"  H2[shape',hexagon] nonzero shapes: {len(H2shape)}",flush=True)
    en=symmetry_energies(SH,HEX,L0,H2shape)
    print("  O(y^2) channel energies (units y^2; common self-energy included):")
    for nm,v in en.items():
        print(f"    {nm:14s}: {v}  ~ {float(v):+.6f}" if v is not None else f"    {nm}: --")
    pure={k:en[k] for k in ['0^{--}','3^{+-}','2^{--}(E)','2^{--}(T2)'] if en[k] is not None}
    order=sorted(pure,key=lambda k:pure[k])
    print(f"\n  ORDERING (light->heavy): {' < '.join(order)}")
    base=pure['0^{--}']
    print("  splittings vs 0--:")
    for k in order: print(f"    {k:12s}: {pure[k]-base}  ~ {float(pure[k]-base):+.6f}")
    print(f"\n  gates {sum(PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
