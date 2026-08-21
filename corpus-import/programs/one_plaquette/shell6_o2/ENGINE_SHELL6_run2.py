#!/usr/bin/env python3
"""ENGINE_SHELL6_run2.py -- exact shell-6 C-odd O(y^2) channel energies, with a
charge-signature-pruned Gram resolvent (the SU(3) per-link U-count mod 3 must
match for any nonzero Haar overlap, so the Gram is block-diagonal -> fast)."""
import sys, os, itertools, time
from collections import defaultdict
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
def connected_W(L0e,layers):
    l2p=G.build_plaq_index(3)
    def touching(links):
        s=set()
        for lid in links:
            for pw in l2p.get(lid,()): s.add(tuple(pw))
        return s
    cur=set(l for (l,_) in L0e); plset=set()
    for _ in range(layers):
        plset|=touching(cur); cur=set(l for pwt in plset for (l,_) in pwt)
    return [tuple((lid_int(l),p) for (l,p) in pwt) for pwt in plset]
def is_e0_loop(m): return len(m)==1 and len(m[0])==6 and len(set(g for g,p in m[0]))==6

def chargesig(m):
    d=defaultdict(int)
    for w in m:
        for (g,p) in w: d[g]+=p
    return frozenset((g,c%3) for g,c in d.items() if c%3)

def gram_resolvent_fast(H0,E0,manifold,x,tag):
    qx=dict(x)
    for f in manifold:
        ov=E.inner(f,x)
        if ov: qx=E.expr_add(qx,f,-ov)
    if not qx: return {}
    basis=list(qx.keys()); seen=set(basis); i=0
    while i<len(basis):
        for mm in H0.mono(basis[i]):
            if mm not in seen: seen.add(mm); basis.append(mm)
        i+=1
    n=len(basis); pos={m:k for k,m in enumerate(basis)}
    sigs=[chargesig(m) for m in basis]
    groups=defaultdict(list)
    for k in range(n): groups[sigs[k]].append(k)
    G_=[[F(0)]*n for _ in range(n)]
    for grp in groups.values():
        for a in grp:
            for b in grp:
                G_[a][b]=E.inner({basis[a]:F(1)},{basis[b]:F(1)})
    Ac=[H0.mono(basis[i]) for i in range(n)]
    S=[[E0*G_[k][i]-sum(cf*G_[k][pos[mm]] for mm,cf in Ac[i].items() if mm in pos) for i in range(n)]
       for k in range(n)]
    r=[E.inner({basis[k]:F(1)},qx) for k in range(n)]
    rows=[row[:] for row in S]; rhs=list(r)
    for f in manifold:
        rows.append([E.inner(f,{basis[i]:F(1)}) for i in range(n)]); rhs.append(F(0))
    sol,kernel=E.solve_stacked(rows,rhs)
    gate(f"[{tag}] resolvent consistent (closure {n})", sol is not None)
    ok=all(sum(S[k][i]*sol[i] for i in range(n))==r[k] for k in range(n))
    gate(f"[{tag}] weak residual zero", ok)
    y={}
    for i,cf in enumerate(sol):
        if cf: y=E.expr_add(y,{basis[i]:cf})
    return y

def run(layers, rowbox=2):
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
    t=time.time(); y=gram_resolvent_fast(H0,F(4),manifold,v,f'L{layers}')
    Wy=E.apply_W_links(y,Ww); Wl0=E.apply_W_links(L0w,Ww)
    print(f"  layers={layers}: |W|={len(Ww)} closure={len(basis)} model={len(manifold)} "
          f"resolvent {round(time.time()-t,1)}s; |Wy|={len(Wy)}",flush=True)
    # read H2 + H1 rows over positioned length-6 loops (links must be in registry; sig must match Wy)
    wysig=set(chargesig(m) for m in Wy)
    H2shape={}; H1shape={}
    for s in SH:
        for tt in itertools.product(range(-rowbox,rowbox+1),repeat=3):
            es=edges_at(s,tt)
            if not G.is_simple_loop(es): continue
            if any(l not in _LID for (l,_) in es): continue
            w=E.canon_word(word_of_edges(es))
            if chargesig(next(iter(w))) not in wysig: continue
            val=E.inner(w,Wy)
            if val!=0: H2shape[s]=H2shape.get(s,F(0))+val
            b=E.inner(w,Wl0)
            if b!=0: H1shape[s]=H1shape.get(s,F(0))+(-b)
    offh1=[abs(x) for s,x in H1shape.items() if s!=L0 and x!=0]
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
        Rm=M if round(np.linalg.det(M))==1 else -M; t=int(round(np.trace(Rm)))
        if t==3:return 'E'
        if t==0:return 'C3'
        if t==1:return 'C4'
        return 'C2' if [int(np.nonzero(Rm[i])[0][0]) for i in range(3)]==[0,1,2] else 'C2p'
    CH={'A1':{'E':1,'C3':1,'C2':1,'C4':1,'C2p':1},'A2':{'E':1,'C3':1,'C2':1,'C4':-1,'C2p':-1},
        'E':{'E':2,'C3':-1,'C2':2,'C4':0,'C2p':0},'T1':{'E':3,'C3':0,'C2':-1,'C4':1,'C2p':-1},
        'T2':{'E':3,'C3':0,'C2':-1,'C4':-1,'C2p':1}}
    JOF={'A1':0,'A2':3,'E':2,'T1':1,'T2':2}
    CLS=[oclass(M) for M in OH]; DET=[int(round(np.linalg.det(M))) for M in OH]
    def cen(G_,Ps,Cs):
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
    return {nm:cen(*g) for nm,g in EX.items()}

def main():
    print("="*72,"\nSHELL-6 C-odd O(y^2) channel energies (exact, sig-pruned)")
    print("="*72,flush=True)
    for layers in (1,2):
        try: SH,HEX,L0,H2=run(layers)
        except SystemExit as e: print("  stop:",e); break
        en=channel_energies(SH,L0,H2)
        print(f"  energies (units y^2, layers={layers}):")
        for nm,v in en.items():
            print(f"    {nm:14s}: {v}  ~{float(v):+.5f}" if v is not None else f"    {nm}: --")
        pure={k:en[k] for k in ['0^{--}','3^{+-}','2^{--}(E)','2^{--}(T2)'] if en[k] is not None}
        if pure:
            order=sorted(pure,key=lambda k:pure[k]); b=pure['0^{--}']
            print(f"  ORDER (light->heavy): {' < '.join(order)}")
            print("  splittings vs 0--: "+", ".join(f'{k}:{pure[k]-b}~{float(pure[k]-b):+.4f}' for k in order),flush=True)
    print(f"\n  gates {sum(PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
