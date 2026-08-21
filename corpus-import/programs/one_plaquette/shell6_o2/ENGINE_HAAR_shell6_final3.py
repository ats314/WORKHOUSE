#!/usr/bin/env python3
"""ENGINE_HAAR_shell6_final3.py -- CONVERGENCE-correct shell-6 C-odd O(y^2).
The resolvent input W_inner = plaquettes touching the reference (complete for the
first W, exact: H0 is per-link so R stays on those links).  The OUTER W that reads
<L'|W|y> must include plaquettes touching the intermediate m (= y's support), which
extend beyond the reference -> use W_outer = plaquettes touching y's links.  This
captures the m->L' routes the single-layer run missed, with NO enlargement of the
resolvent closure.  Resumable (persistent cache)."""
import sys, os, itertools, pickle, atexit, tempfile
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_shell6_o2_engine2 as G
import ENGINE_HAAR_fast_haar
import link_o2_v2 as E
import ENGINE_SHELL6_shell6_analyze as A

CACHE="/tmp/shell6_hc.pkl"
if os.path.exists(CACHE):
    try: fast_haar._TNCACHE={k:F(v) for k,v in pickle.load(open(CACHE,"rb")).items()}; print(f"[cache]{len(fast_haar._TNCACHE)}",flush=True)
    except Exception as e: print("[cache] load fail",e,flush=True)
def _save():
    try:
        fd,tmp=tempfile.mkstemp(dir="/tmp")
        with os.fdopen(fd,"wb") as f: pickle.dump({k:str(v) for k,v in fast_haar._TNCACHE.items()},f)
        os.replace(tmp,CACHE)
    except Exception: pass
_orig=fast_haar.haar_tn; _N=[0]
def _persist(words):
    key=tuple(tuple(w) for w in words); hit=key in fast_haar._TNCACHE; r=_orig(words)
    if not hit:
        _N[0]+=1
        if _N[0]%50==0: _save()
    return r
fast_haar.haar_tn=_persist; E.D.integrate_monomial=lambda m:_persist(list(m)); atexit.register(_save)

DIRS=G.DIRS; PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}",flush=True)
    if not c: raise SystemExit("FAIL "+n)
def woe(es): return tuple((l,p) for (l,p) in G.edges_to_word(es))
def edges_at(shape,t):
    base=G.edgeset((0,0,0),shape)
    return frozenset((((lo[0]+t[0],lo[1]+t[1],lo[2]+t[2]),ax),p) for ((lo,ax),p) in base)
def plqs_touching(links):
    l2p=G.build_plaq_index(3); s=set()
    for lid in links:
        for pw in l2p.get(lid,()): s.add(tuple(pw))
    return [tuple((l,p) for (l,p) in pwt) for pwt in s]
def is_e0(m): return len(m)==1 and len(m[0])==6 and len(set(g for g,p in m[0]))==6
def csig(m):
    d=defaultdict(int)
    for w in m:
        for (g,p) in w: d[g]+=p
    return frozenset((g,c%3) for g,c in d.items() if c%3)

def resolvent(H0,E0,man,x,tag):
    qx=dict(x)
    for f in man:
        ov=E.inner(f,x)
        if ov: qx=E.expr_add(qx,f,-ov)
    if not qx: return {}
    basis=list(qx.keys()); seen=set(basis); i=0
    while i<len(basis):
        for mm in H0.mono(basis[i]):
            if mm not in seen: seen.add(mm); basis.append(mm)
        i+=1
    n=len(basis); pos={m:k for k,m in enumerate(basis)}
    sg=[csig(m) for m in basis]; grp=defaultdict(list)
    for k in range(n): grp[sg[k]].append(k)
    Gm=[[F(0)]*n for _ in range(n)]
    for g_ in grp.values():
        for a in g_:
            for b in g_: Gm[a][b]=E.inner({basis[a]:F(1)},{basis[b]:F(1)})
    Ac=[H0.mono(basis[i]) for i in range(n)]
    S=[[E0*Gm[k][i]-sum(cf*Gm[k][pos[mm]] for mm,cf in Ac[i].items() if mm in pos) for i in range(n)] for k in range(n)]
    r=[E.inner({basis[k]:F(1)},qx) for k in range(n)]
    rows=[row[:] for row in S]; rhs=list(r)
    for f in man:
        rows.append([E.inner(f,{basis[i]:F(1)}) for i in range(n)]); rhs.append(F(0))
    sol,_=E.solve_stacked(rows,rhs)
    gate(f"[{tag}] resolvent consistent (closure {n})", sol is not None); _save()
    y={}
    for i,cf in enumerate(sol):
        if cf: y=E.expr_add(y,{basis[i]:cf})
    return y

def hexrow(ref, rowbox=1):
    L0e=edges_at(ref,(0,0,0)); H0=E.make_H0_links()
    Winner=plqs_touching(set(l for (l,_) in L0e))           # touching ref (complete first W)
    L0w=E.canon_word(woe(L0e)); v=E.apply_W_links(L0w,Winner)
    basis=set(v.keys()); fr=list(v.keys())
    while fr:
        m=fr.pop()
        for mm in H0.mono(m):
            if mm not in basis: basis.add(mm); fr.append(mm)
    man=[{m:F(1)} for m in basis if is_e0(m)]
    y=resolvent(H0,F(4),man,v,'r'); _save()
    Wouter=plqs_touching(set(l for m in y for w in m for (l,p) in w))   # touching the intermediate
    Wy=E.apply_W_links(y,Wouter); Wl0=E.apply_W_links(L0w,Wouter); _save()
    Wylinks=set(l for m in Wy for w in m for (l,p) in w); wysig=set(csig(m) for m in Wy)
    SH=G.shapes6(); HEX=[s for s in SH if len(set(d//2 for d in s))==3]
    H2={}; H1={}
    for s in HEX:
        for tt in itertools.product(range(-rowbox,rowbox+1),repeat=3):
            es=edges_at(s,tt)
            if not G.is_simple_loop(es): continue
            if any(l not in Wylinks for (l,_) in es): continue
            w=E.canon_word(woe(es))
            if csig(next(iter(w))) not in wysig: continue
            val=E.inner(w,Wy)
            if val!=0: H2[s]=H2.get(s,F(0))+val
            b=E.inner(w,Wl0)
            if b!=0: H1[s]=H1.get(s,F(0))+(-b)
    _save()
    off=[abs(x) for s,x in H1.items() if s!=ref and x!=0]
    gate("first-order |H1|=1/3", len(off)>0 and all(x==F(1,3) for x in off))
    print(f"  ref={ref}: |Winner|={len(Winner)} |Wouter|={len(Wouter)} H2-entries={len(H2)}",flush=True)
    return H2

def orbit(h,HEX):
    o=set()
    for c in (0,1):
        for M in A.OH:
            t=A.gact(h,M); t=A.rev(t) if c else t; o.add(t)
    return o&set(HEX)

def main():
    SH=G.shapes6(); HEX=[s for s in SH if len(set(d//2 for d in s))==3]
    L0=HEX[0]; orb0=sorted(orbit(L0,HEX))
    print("="*70,"\nshell-6 O(y^2) convergence-correct (outer W = touching intermediate)")
    print("="*70,flush=True)
    print("ORBIT 0 (size %d):"%len(orb0),flush=True)
    R0=hexrow(L0)
    # build full orbit-0 matrix + Hermiticity + channel eigenvalues
    N=len(orb0); idx={s:i for i,s in enumerate(orb0)}
    gof={}
    for c in (0,1):
        for M in A.OH:
            t=A.gact(L0,M); t=A.rev(t) if c else t
            if t not in gof: gof[t]=(M,c)
    ginv=lambda s,M,c:A.gact(A.rev(s) if c else s, M.T)
    M2=np.array([[float(R0.get(ginv(orb0[i],*gof[orb0[j]]),F(0))) for j in range(N)] for i in range(N)])
    gate("orbit-0 H2 Hermitian", np.allclose(M2,M2.T,atol=1e-9))
    def pm(M,c):
        P=np.zeros((N,N))
        for h in orb0:
            t=A.gact(h,M); t=A.rev(t) if c else t
            if t in idx: P[idx[t],idx[h]]=1
        return P
    gate("orbit-0 H2 commutes O_hxC", all(np.allclose(M2@pm(M,c),pm(M,c)@M2,atol=1e-9) for M in A.OH[:8] for c in (0,1)))
    energies={}
    for Gn,Ps,Cs,nm in [('A1',-1,-1,'0--'),('E',-1,-1,'2--(E)'),('T2',-1,-1,'2--(T2)'),('T2',1,-1,'2+-'),('T1',1,-1,'1+-exc')]:
        P=np.zeros((N,N))
        for c in (0,1):
            for mi,M in enumerate(A.OH):
                P+=A.CH[Gn][A.CLS[mi]]*(1 if A.DET[mi]==1 else Ps)*(1 if c==0 else Cs)*pm(M,c)
        P*=A.DIM[Gn]/96.0
        u,s,_=np.linalg.svd(P); rk=int((s>1e-8).sum())
        if rk==0: continue
        B=u[:,:rk]; ev=sorted(set(round(x,6) for x in np.linalg.eigvalsh(B.T@M2@B)))
        energies[nm]=ev[0]; print(f"  {nm:8s}[{Gn}]: {ev}",flush=True)
    # orbit 1 -> 3+-
    L1=next(h for h in HEX if h not in orb0)
    print("ORBIT 1 (size %d), 3+-:"%len(orbit(L1,HEX)),flush=True)
    R1=hexrow(L1)
    num=F(0); den=0
    for c in (0,1):
        for mi,M in enumerate(A.OH):
            g=A.gact(L1,M); g=A.rev(g) if c else g
            chi=A.CH['A2'][A.CLS[mi]]*(1 if A.DET[mi]==1 else 1)*(1 if c==0 else -1)
            num+=chi*R1.get(g,F(0))
            if g==L1: den+=chi
    e3=F(num,den) if den else None
    energies['3+-']=float(e3) if e3 is not None else None
    print(f"  3+- [A2+-]: {e3}  ~{float(e3):+.6f}" if e3 is not None else "  3+- den=0",flush=True)
    print("\nFULL O(y^2) ORDERING:",flush=True)
    items=sorted([(k,v) for k,v in energies.items() if v is not None and k in('0--','2--(E)','2--(T2)','3+-')], key=lambda kv:kv[1])
    print("  "+" < ".join(k for k,_ in items))
    for k,v in items: print(f"    {k:8s}: {v:+.6f}")
    print(f"  gates {sum(PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
