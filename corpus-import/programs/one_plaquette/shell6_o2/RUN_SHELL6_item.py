#!/usr/bin/env python3
"""RUN_SHELL6_item.py -- exact shell-6 C-odd O(y^2) channel energies (link-variable Gram
resolvent).  W = plaquettes touching the reference hexagon's links (connected, k
layers).  Validate via Hermiticity + first-order recovery + layer convergence."""
import sys, os, itertools
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_shell6_o2_engine2 as G
import link_o2_v2 as E
DIRS=G.DIRS
PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}",flush=True)
    if not c: raise SystemExit("FAIL "+n)

_LID={}
def lid_int(geo):
    if geo not in _LID: _LID[geo]=len(_LID)
    return _LID[geo]
def word_of_edges(edges): return tuple((lid_int(l),p) for (l,p) in G.edges_to_word(edges))
def edges_at(shape,t):
    base=G.edgeset((0,0,0),shape)
    return frozenset((((lo[0]+t[0],lo[1]+t[1],lo[2]+t[2]),ax),p) for ((lo,ax),p) in base)

def connected_W(L0e, layers):
    l2p=G.build_plaq_index(3)
    def touching(links):
        s=set()
        for lid in links:
            for pw in l2p.get(lid,()): s.add(tuple(pw))
        return s
    seedlinks=set(l for (l,_) in L0e); plset=set()
    cur=seedlinks
    for _ in range(layers):
        newp=touching(cur); plset|=newp
        cur=set(l for pwt in plset for (l,_) in pwt)
    return [tuple((lid_int(l),p) for (l,p) in pwt) for pwt in plset]

def is_e0_loop(m): return len(m)==1 and len(m[0])==6 and len(set(g for g,p in m[0]))==6

def run(layers):
    SH=G.shapes6(); naxes=lambda s:len(set(d//2 for d in s))
    HEX=[s for s in SH if naxes(s)==3]; L0=HEX[0]; L0e=edges_at(L0,(0,0,0))
    H0=E.make_H0_links(); Ww=connected_W(L0e,layers)
    L0w=E.canon_word(word_of_edges(L0e)); v=E.apply_W_links(L0w,Ww)
    basis=set(v.keys()); fr=list(v.keys())
    while fr:
        m=fr.pop()
        for mm in H0.mono(m):
            if mm not in basis: basis.add(mm); fr.append(mm)
    manifold=[{m:F(1)} for m in basis if is_e0_loop(m)]
    print(f"  layers={layers}: |W|={len(Ww)}; closure={len(basis)}; model 6-loops={len(manifold)}",flush=True)
    y=E.gram_resolvent(H0,F(4),manifold,v,f'L{layers}')
    Wy=E.apply_W_links(y,Ww); Wl0=E.apply_W_links(L0w,Ww)
    inv={i:l for l,i in _LID.items()}
    def shape_pos(m):
        es=frozenset((inv[g],p) for (g,p) in m[0]); ck=G.canon_edges(es)
        for s in SH:
            if G.canon_edges(edges_at(s,(0,0,0)))==ck: return s
        return None
    H2shape={}; h1shape={}
    for f in manifold:
        m=next(iter(f)); sh=shape_pos(m)
        if sh is None: continue
        H2shape[sh]=H2shape.get(sh,F(0))+E.inner(f,Wy)
        h1shape[sh]=h1shape.get(sh,F(0))+(-E.inner(f,Wl0))
    offh1=[abs(v) for s,v in h1shape.items() if s!=L0 and v!=0]
    gate(f"L{layers} first-order corner-push |H1|=1/3", len(offh1)>0 and all(x==F(1,3) for x in offh1))
    return SH,HEX,L0,H2shape

def channel_energies(SH,L0,H2shape):
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
        return 'C2' if [int(np.nonzero(R[i])[0][0]) for i in range(3)]==[0,1,2] else 'C2p'
    CH={'A1':{'E':1,'C3':1,'C2':1,'C4':1,'C2p':1},'A2':{'E':1,'C3':1,'C2':1,'C4':-1,'C2p':-1},
        'E':{'E':2,'C3':-1,'C2':2,'C4':0,'C2p':0},'T1':{'E':3,'C3':0,'C2':-1,'C4':1,'C2p':-1},
        'T2':{'E':3,'C3':0,'C2':-1,'C4':-1,'C2p':1}}
    JOF={'A1':0,'A2':3,'E':2,'T1':1,'T2':2}
    CLS=[oclass(M) for M in OH]; DET=[int(round(np.linalg.det(M))) for M in OH]
    def ce(G_,Ps,Cs):
        num=F(0); den=0
        for c in (0,1):
            for mi,M in enumerate(OH):
                g=gact(L0,M); g=rev(g) if c else g
                chi=CH[G_][CLS[mi]]*(1 if DET[mi]==1 else Ps)*(1 if c==0 else Cs)
                num+=chi*H2shape.get(g,F(0))
                if g==L0: den+=chi
        return F(num,den) if den else None
    EX={'0^{--}':('A1',-1,-1),'3^{+-}':('A2',1,-1),'2^{--}(E)':('E',-1,-1),
        '2^{--}(T2)':('T2',-1,-1),'2^{+-}':('T2',1,-1),'1^{+-}exc':('T1',1,-1)}
    return {nm:ce(*g) for nm,g in EX.items()}

def main():
    print("="*72,"\nSHELL-6 C-odd O(y^2) channel energies (exact)")
    print("="*72,flush=True)
    res={}
    for layers in (1,2):
        SH,HEX,L0,H2=run(layers)
        en=channel_energies(SH,L0,H2)
        res[layers]=en
        print(f"  channel energies (units y^2, layers={layers}):")
        for nm,v in en.items():
            print(f"    {nm:14s}: {v}  ~{float(v):+.5f}" if v is not None else f"    {nm}: --")
        pure={k:en[k] for k in ['0^{--}','3^{+-}','2^{--}(E)','2^{--}(T2)'] if en[k] is not None}
        order=sorted(pure,key=lambda k:pure[k])
        b=pure['0^{--}']
        print(f"  ORDER: {' < '.join(order)}")
        print(f"  splittings vs 0--: "+", ".join(f'{k}:{pure[k]-b}' for k in order),flush=True)
    print(f"\n  gates {sum(PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
