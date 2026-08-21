#!/usr/bin/env python3
"""ENGINE_SHELL6_final4.py -- shell-6 C-odd O(y^2), convergence-correct AND fast.
Uses the self-adjointness of W (=Sum 2 Re Tr U_p, real): H2[L',L0]=<L'|W|y>=<W L'|y>.
W L' is small (L' a single loop -> one 2-trace per plaquette), so the row read is
inner(apply_W(L',W_all), y) over ~|W_all| monomials, vs |W y|~1e4.  W_all = plaquettes
touching y's support (proved complete).  Resumable persistent cache."""
import sys, os, itertools, pickle, atexit, tempfile
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_shell6_o2_engine2 as G
import ENGINE_HAAR_fast_haar
import link_o2_v2 as E
import ENGINE_SHELL6_shell6_analyze as A
import ENGINE_HAAR_shell6_final3 as S3      # edges_at, plqs_touching, resolvent, woe, csig, is_e0, orbit, gate

CACHE=os.environ.get("SHELL6_CACHE","/tmp/shell6_hc.pkl")
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
        if _N[0]%100==0: _save()
    return r
fast_haar.haar_tn=_persist; E.D.integrate_monomial=lambda m:_persist(list(m)); atexit.register(_save)

PASS=[]
def gate(n,c):
    PASS.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}",flush=True)
    if not c: raise SystemExit("FAIL "+n)

def hexrow(ref, rowbox=1):
    L0e=S3.edges_at(ref,(0,0,0)); H0=E.make_H0_links()
    Winner=S3.plqs_touching(set(l for (l,_) in L0e))
    L0w=E.canon_word(S3.woe(L0e)); v=E.apply_W_links(L0w,Winner)
    basis=set(v.keys()); fr=list(v.keys())
    while fr:
        m=fr.pop()
        for mm in H0.mono(m):
            if mm not in basis: basis.add(mm); fr.append(mm)
    man=[{m:F(1)} for m in basis if S3.is_e0(m)]
    y=S3.resolvent(H0,F(4),man,v,'r'); _save()
    ylinks=set(l for m in y for w in m for (l,p) in w)
    W_all=S3.plqs_touching(ylinks)          # plaquettes touching the intermediate (complete outer W)
    ysig=set(S3.csig(m) for m in y)
    SH=G.shapes6(); HEX=[s for s in SH if len(set(d//2 for d in s))==3]
    H2={}; H1={}; cnt=0
    for s in HEX:
        for tt in itertools.product(range(-rowbox,rowbox+1),repeat=3):
            es=S3.edges_at(s,tt)
            if not G.is_simple_loop(es): continue
            # L' must share >=1 link with y's support, else <W L'|y>=0
            if not any(l in ylinks for (l,_) in es): continue
            Lp=E.canon_word(S3.woe(es))
            # H2 = <W L'|y>;  H1 = -<L'|W|L0> = -<W L'|L0>
            WLp=E.apply_W_links(Lp, W_all)
            val=E.inner(WLp, y)                 # note inner(a,b)=int conj(a) b; WLp,y real-rational
            if val!=0: H2[s]=H2.get(s,F(0))+val
            b=E.inner(WLp, {L0w:F(1)})
            if b!=0: H1[s]=H1.get(s,F(0))+(-b)
            cnt+=1
    _save()
    off=[abs(x) for s,x in H1.items() if s!=ref and x!=0]
    gate("first-order |H1|=1/3", len(off)>0 and all(x==F(1,3) for x in off))
    print(f"  ref={ref}: |Winner|={len(Winner)} |W_all|={len(W_all)} |y|={len(y)} positions={cnt} H2-entries={len(H2)}",flush=True)
    return H2

def main():
    SH=G.shapes6(); HEX=[s for s in SH if len(set(d//2 for d in s))==3]
    L0=HEX[0]; orb0=sorted(S3.orbit(L0,HEX))
    print("="*70,"\nshell-6 O(y^2) FAST convergence-correct (W self-adjoint flip)")
    print("="*70,flush=True)
    print(f"ORBIT 0 (size {len(orb0)}):",flush=True)
    R0=hexrow(L0)
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
    # exact diagonal (Rayleigh denominators)
    diagshape=R0.get(L0,F(0))
    print(f"  exact orbit-0 diagonal H2[L0,L0] = {diagshape} ~{float(diagshape):.6f}",flush=True)
    energies={}
    for Gn,Ps,Cs,nm in [('A1',-1,-1,'0--'),('E',-1,-1,'2--(E)'),('T2',-1,-1,'2--(T2)'),('T2',1,-1,'2+-'),('T1',1,-1,'1+-exc')]:
        # exact rational Rayleigh quotient from the row
        num=F(0); den=0
        for c in (0,1):
            for mi,M in enumerate(A.OH):
                g=A.gact(L0,M); g=A.rev(g) if c else g
                chi=A.CH[Gn][A.CLS[mi]]*(1 if A.DET[mi]==1 else Ps)*(1 if c==0 else Cs)
                num+=chi*R0.get(g,F(0))
                if g==L0: den+=chi
        if den==0: continue
        energies[nm]=F(num,den)
        print(f"  {nm:8s}[{Gn}]: {F(num,den)}  ~{float(F(num,den)):+.6f}  (offdiag {F(num,den)-diagshape})",flush=True)
    # orbit 1 -> 3+-
    L1=next(h for h in HEX if h not in orb0)
    print(f"ORBIT 1 (size {len(S3.orbit(L1,HEX))}):",flush=True)
    R1=hexrow(L1)
    num=F(0); den=0
    for c in (0,1):
        for mi,M in enumerate(A.OH):
            g=A.gact(L1,M); g=A.rev(g) if c else g
            chi=A.CH['A2'][A.CLS[mi]]*(1 if A.DET[mi]==1 else 1)*(1 if c==0 else -1)
            num+=chi*R1.get(g,F(0))
            if g==L1: den+=chi
    e3=F(num,den) if den else None
    if e3 is not None: energies['3+-']=e3; print(f"  3+- [A2+-]: {e3}  ~{float(e3):+.6f}",flush=True)
    print("\nFINAL O(y^2) ORDERING (converged outer-W):",flush=True)
    items=sorted([(k,v) for k,v in energies.items() if k in('0--','2--(E)','2--(T2)','3+-')], key=lambda kv:float(kv[1]))
    print("  "+" < ".join(k for k,_ in items),flush=True)
    if '0--' in energies:
        b=energies['0--']
        for k,v in items: print(f"    {k:8s}: {v}  ~{float(v):+.6f}   vs 0--: {v-b}",flush=True)
    print(f"  gates {sum(PASS)}/{len(PASS)}",flush=True)

if __name__=="__main__":
    main()
