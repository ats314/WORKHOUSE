#!/usr/bin/env python3
"""ENGINE_SHELL6_item.py -- exact shell-6 C-odd O(y^2) ordering, RESUMABLE.

Uses geometric link ids (lo,ax) as word generators so the Haar-integral cache key
is deterministic across runs, and persists fast_haar's cache to /tmp every few
computations.  Re-invoke until it completes in one call (cache fully warm).
"""
import sys, os, itertools, pickle, atexit
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_shell6_o2_engine2 as G
import ENGINE_HAAR_fast_haar
import link_o2_v2 as E

CACHE_PATH="/tmp/shell6_haar_cache.pkl"
# ---- persistent, periodically-saved Haar cache (deterministic geometric keys) ----
if os.path.exists(CACHE_PATH):
    try:
        raw=pickle.load(open(CACHE_PATH,"rb"))
        fast_haar._TNCACHE={k:F(v) for k,v in raw.items()}
        print(f"[cache] loaded {len(fast_haar._TNCACHE)} integrals",flush=True)
    except Exception as e:
        print("[cache] load failed",e,flush=True)
_orig_tn=fast_haar.haar_tn
_NEW=[0]
def _save():
    try: pickle.dump({k:str(v) for k,v in fast_haar._TNCACHE.items()}, open(CACHE_PATH,"wb"))
    except Exception: pass
def haar_tn_persist(words):
    key=tuple(tuple(w) for w in words)
    hit = key in fast_haar._TNCACHE
    r=_orig_tn(words)
    if not hit:
        _NEW[0]+=1
        if _NEW[0]%25==0: _save()
    return r
fast_haar.haar_tn=haar_tn_persist
E.D.integrate_monomial=lambda m: haar_tn_persist(list(m))
atexit.register(_save)

DIRS=G.DIRS; PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}",flush=True)
    if not c: raise SystemExit("FAIL "+n)
def word_of_edges(edges): return tuple((l,p) for (l,p) in G.edges_to_word(edges))   # gen = (lo,ax)
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
    return [tuple((l,p) for (l,p) in pwt) for pwt in plset]
def is_e0_loop(m): return len(m)==1 and len(m[0])==6 and len(set(g for g,p in m[0]))==6
def chargesig(m):
    d=defaultdict(int)
    for w in m:
        for (g,p) in w: d[g]+=p
    return frozenset((g,c%3) for g,c in d.items() if c%3)

def gram_resolvent(H0,E0,manifold,x,tag):
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
    sigs=[chargesig(m) for m in basis]; groups=defaultdict(list)
    for k in range(n): groups[sigs[k]].append(k)
    Gm=[[F(0)]*n for _ in range(n)]
    for grp in groups.values():
        for a in grp:
            for b in grp:
                Gm[a][b]=E.inner({basis[a]:F(1)},{basis[b]:F(1)})
    Ac=[H0.mono(basis[i]) for i in range(n)]
    S=[[E0*Gm[k][i]-sum(cf*Gm[k][pos[mm]] for mm,cf in Ac[i].items() if mm in pos) for i in range(n)] for k in range(n)]
    r=[E.inner({basis[k]:F(1)},qx) for k in range(n)]
    rows=[row[:] for row in S]; rhs=list(r)
    for f in manifold:
        rows.append([E.inner(f,{basis[i]:F(1)}) for i in range(n)]); rhs.append(F(0))
    sol,_=E.solve_stacked(rows,rhs)
    gate(f"[{tag}] resolvent consistent (closure {n})", sol is not None)
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
    man=[{m:F(1)} for m in basis if is_e0_loop(m)]
    print(f"  layers={layers} |W|={len(Ww)} closure={len(basis)} model={len(man)}",flush=True)
    y=gram_resolvent(H0,F(4),man,v,f'L{layers}'); Wy=E.apply_W_links(y,Ww); Wl0=E.apply_W_links(L0w,Ww)
    _save()
    wysig=set(chargesig(m) for m in Wy)
    H2={}; H1={}
    for s in SH:
        for tt in itertools.product(range(-rowbox,rowbox+1),repeat=3):
            es=edges_at(s,tt)
            if not G.is_simple_loop(es): continue
            w=E.canon_word(word_of_edges(es))
            if chargesig(next(iter(w))) not in wysig: continue
            val=E.inner(w,Wy)
            if val!=0: H2[s]=H2.get(s,F(0))+val
            b=E.inner(w,Wl0)
            if b!=0: H1[s]=H1.get(s,F(0))+(-b)
    _save()
    offh1=[abs(x) for s,x in H1.items() if s!=L0 and x!=0]
    gate(f"L{layers} first-order |H1|=1/3", len(offh1)>0 and all(x==F(1,3) for x in offh1))
    return SH,L0,H2

def channels(SH,L0,H2):
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
                num+=chi*H2.get(g,F(0))
                if g==L0: den+=chi
        return F(num,den) if den else None
    EX={'0^{--}':('A1',-1,-1),'3^{+-}':('A2',1,-1),'2^{--}(E)':('E',-1,-1),
        '2^{--}(T2)':('T2',-1,-1),'2^{+-}':('T2',1,-1),'1^{+-}exc':('T1',1,-1)}
    return {nm:cen(*g) for nm,g in EX.items()}

def main(layers=1):
    print("="*72,"\nSHELL-6 C-odd O(y^2) (exact, resumable)",flush=True); print("="*72)
    SH,L0,H2=run(layers)
    en=channels(SH,L0,H2)
    print(f"  channel energies (units y^2, layers={layers}):")
    for nm,v in en.items():
        print(f"    {nm:14s}: {v}  ~{float(v):+.6f}" if v is not None else f"    {nm}: --")
    pure={k:en[k] for k in ['0^{--}','3^{+-}','2^{--}(E)','2^{--}(T2)'] if en[k] is not None}
    if pure:
        order=sorted(pure,key=lambda k:pure[k]); b=pure['0^{--}']
        print(f"\n  ORDER (light->heavy): {' < '.join(order)}")
        print("  splittings vs 0--: "+", ".join(f'{k}:{pure[k]-b}~{float(pure[k]-b):+.4f}' for k in order))
    print(f"  gates {sum(PASS)}/{len(PASS)}")

if __name__=="__main__":
    main(int(sys.argv[1]) if len(sys.argv)>1 else 1)
