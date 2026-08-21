"""From-scratch exact SU(3) torelon string-tension engine (adjoint + determinant sectors).
Validates against known sigma2,sigma3,sigma4; then computes sigma5,sigma6 (vs KPS targets)."""
import itertools, importlib.util, sys, time
from collections import defaultdict
from fractions import Fraction as F
import sympy as sp
sys.setrecursionlimit(10000)

# ---- folded des-Cloizeaux (certified order-generic) ----
PRE='/tmp/batch/SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14/SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14/ENGINE_Y6_folded_descloizeaux_preflight.py'
spec=importlib.util.spec_from_file_location('fp',PRE); fp=importlib.util.module_from_spec(spec); spec.loader.exec_module(fp)
GEN_FOLDED=fp.folded_coefficient

# ---- SU(3) core ----
N=3
def _sumTT(x,y,z,w):
    v=F(0)
    if x==w and z==y: v+=F(1,2)
    if x==y and z==w: v-=F(1,6)
    return v
C2_fund=F(4,3)
_states_cache={}
def states_of(m):
    if m not in _states_cache: _states_cache[m]=list(itertools.product(range(N),repeat=m))
    return _states_cache[m]
def casimir_subset(eps,S):
    m=len(eps); states=states_of(m); sidx={s:k for k,s in enumerate(states)}; M={}
    S=sorted(S)
    for k in range(len(states)): M[(k,k)]=M.get((k,k),F(0))+len(S)*C2_fund
    for i in S:
        for j in S:
            if i==j: continue
            ei,ej=eps[i],eps[j]
            for s in states:
                row=sidx[s]; bi=s[i]; bj=s[j]
                for an in range(N):
                    for cn in range(N):
                        if ei==1: xi,yi,si=an,bi,1
                        else: xi,yi,si=bi,an,-1
                        if ej==1: xj,yj,sj=cn,bj,1
                        else: xj,yj,sj=bj,cn,-1
                        val=_sumTT(xi,yi,xj,yj)
                        if not val: continue
                        val*=si*sj
                        ns=list(s); ns[i]=an; ns[j]=cn; col=sidx[tuple(ns)]
                        M[(row,col)]=M.get((row,col),F(0))+val
    return M
def _mat(Md,dim):
    A=sp.zeros(dim,dim)
    for (r,c),v in Md.items(): A[r,c]=sp.Rational(v.numerator,v.denominator)
    return A

_blk_cache={}
def link_blocks(eps,cut_subsets):
    key=(eps,cut_subsets)
    if key in _blk_cache: return _blk_cache[key]
    m=len(eps); dim=N**m
    Cf=_mat(casimir_subset(eps,range(m)),dim)
    nb=Cf.nullspace()
    if not nb:
        _blk_cache[key]={}; return {}
    cutmats=[_mat(casimir_subset(eps,S),dim) for S in cut_subsets]
    groups=[((),nb)]
    for Cm in cutmats:
        ng=[]
        for hist,vecs in groups:
            U=sp.Matrix.hstack(*vecs)
            X=(U.T*U).inv()*(U.T*Cm*U)
            for val,mult,bas in X.eigenvects():
                lam=sp.nsimplify(val); lamF=F(int(lam.p),int(lam.q))
                newvecs=[U*b for b in bas]
                ng.append((hist+(lamF,),newvecs))
        groups=ng
    states=states_of(m); out={}
    for hist,vecs in groups:
        U=sp.Matrix.hstack(*vecs)
        P=U*(U.T*U).inv()*U.T
        blk={}
        for p in range(dim):
            row=P.row(p)
            for q in range(dim):
                v=row[q]
                if v!=0: blk[(states[p],states[q])]=F(int(v.p),int(v.q))
        out[hist]=blk
    _blk_cache[key]=out; return out

# ---- geometry (from generic_sigma_engine conventions) ----
E=((1,0,0),(0,1,0),(0,0,1))
def vadd(a,b): return tuple(a[i]+b[i] for i in range(3))
def modx(v,L): return (v[0]%L,v[1],v[2])
def pedges(p,L):
    x=modx(p[:3],L);a,b=p[3:];xa=modx(vadd(x,E[a]),L);xb=modx(vadd(x,E[b]),L)
    return [((*x,a),+1,0,1),((*xa,b),+1,1,2),((*xb,a),-1,2,3),((*x,b),-1,3,0)]
def pverts(p,L):
    x=modx(p[:3],L);a,b=p[3:]
    return [x,modx(vadd(x,E[a]),L),modx(vadd(vadd(x,E[a]),E[b]),L),modx(vadd(x,E[b]),L)]
def torelon_edges(L): return [((x,0,0,0),+1,x,(x+1)%L) for x in range(L)]
def adjacent_plaquettes(L):
    out=set()
    for x in range(L):
        for b in (1,2):
            out.add((x,0,0,0,b)); anchor=[x,0,0]; anchor[b]=-1; out.add((*anchor,0,b))
    return sorted(out)
def site_neighbors(p,L):
    out=set()
    for v in pverts(p,L):
        for a,b in ((0,1),(0,2),(1,2)):
            for ia in (0,1):
                for ib in (0,1):
                    anc=[v[i] for i in range(3)]; anc[a]-=ia; anc[b]-=ib; anc[0]%=L
                    out.add((*anc,a,b))
    return out
def connected_sets(L,n):
    cap=n//2  # each distinct plaquette must appear >=2 times (bare-link); so <= floor(n/2) distinct
    adj=adjacent_plaquettes(L); seen=set(); frontier=[frozenset([p]) for p in adj]
    for s in frontier: seen.add(s)
    out=list(frontier)
    while frontier:
        nf=[]
        for s in frontier:
            if len(s)>=cap: continue
            nb=set()
            for p in s: nb|=site_neighbors(p,L)
            for q in nb:
                if q in s: continue
                t=s|{q}
                if t not in seen: seen.add(t); nf.append(t); out.append(t)
        frontier=nf
    return [s for s in out if len(s)<=n//2]
def sequences_over_set(S,n):
    from collections import Counter as _C
    S=list(S); k=len(S)
    for assign in itertools.product(range(k),repeat=n):
        c=_C(assign)
        if len(c)!=k or any(v<2 for v in c.values()): continue
        for sgn in itertools.product((1,-1),repeat=n):
            yield tuple(S[i] for i in assign),tuple(sgn)

def build_specs(L,insertions,signs,vacuum=False):
    n=len(insertions); assert len(signs)==n+2
    eff=list(signs[:n+1])+[-signs[n+1]]; events=[]; offset=0
    ed=[] if vacuum else torelon_edges(L); events.append((ed,offset)); offset+=0 if vacuum else L
    for p in insertions:
        ed=pedges(p,L); events.append((ed,offset)); offset+=4
    ed=[] if vacuum else torelon_edges(L); events.append((ed,offset)); offset+=0 if vacuum else L
    links=defaultdict(list)
    for ei,(edges,off) in enumerate(events):
        for edge,(link,inc,sc,ec) in enumerate(edges):
            token=eff[ei]*inc; rv=off+(sc if inc==1 else ec); cv=off+(ec if inc==1 else sc)
            links[link].append((ei,edge,token,rv,cv))
    specs=[]
    for link,occ in sorted(links.items()):
        occ=tuple(sorted(occ)); sig=[0]*(n+2)
        for ei,edge,t,rv,cv in occ:
            if sig[ei]!=0: raise RuntimeError('dup')
            sig[ei]=t
        sig=tuple(sig)
        if (sig.count(1)-sig.count(-1))%3!=0: return None
        rows=tuple(x[3] for x in occ); cols=tuple(x[4] for x in occ)
        specs.append((sig,rows,cols))
    return specs

# ---- contraction ----
def link_factor(blk,row_vars,col_vars):
    scope=tuple(sorted(set(row_vars)|set(col_vars))); d=defaultdict(F)
    for (rt,ct),co in blk.items():
        assign={}; ok=True
        for v,val in list(zip(row_vars,rt))+list(zip(col_vars,ct)):
            if v in assign and assign[v]!=val: ok=False;break
            assign[v]=val
        if ok: d[tuple(assign[v] for v in scope)]+=co
    return scope,dict(d)
def merge2(f1,f2):
    s1,d1=f1; s2,d2=f2; s2set=set(s2)
    shared=[v for v in s1 if v in s2set]
    scope=tuple(s1)+tuple(v for v in s2 if v not in set(s1))
    p1=[s1.index(v) for v in shared]; p2=[s2.index(v) for v in shared]
    idx=defaultdict(list)
    for a2,c2 in d2.items(): idx[tuple(a2[i] for i in p2)].append((a2,c2))
    posnew2=[scope.index(v) for v in s2]; posnew1=[scope.index(v) for v in s1]
    out=defaultdict(F)
    for a1,c1 in d1.items():
        key=tuple(a1[i] for i in p1)
        for a2,c2 in idx.get(key,[]):
            full=[None]*len(scope)
            for i,v in enumerate(a1): full[posnew1[i]]=v
            for i,v in enumerate(a2): full[posnew2[i]]=v
            out[tuple(full)]+=c1*c2
    return scope,dict(out)
def contract(factors):
    factors=[f for f in factors]
    allv=set().union(*[set(s) for s,_ in factors]) if factors else set()
    while allv:
        v=min(allv,key=lambda x:sum(1 for s,_ in factors if x in s))
        sel=[f for f in factors if v in f[0]]; rest=[f for f in factors if v not in f[0]]
        m=sel[0]
        for f in sel[1:]: m=merge2(m,f)
        s,d=m; vi=s.index(v); ns=tuple(x for x in s if x!=v)
        nd=defaultdict(F)
        for a,c in d.items(): nd[a[:vi]+a[vi+1:]]+=c
        factors=rest+[(ns,dict(nd))]; allv.discard(v)
    res=F(1)
    for s,d in factors: res*=d.get((),F(0))
    return res

def amplitude(L,insertions,signs,n,vacuum):
    specs=build_specs(L,insertions,signs,vacuum)
    if specs is None: return F(0)
    per=[]
    for sig,rows,cols in specs:
        ev=[e for e in range(len(sig)) if sig[e]!=0]; eps=tuple(sig[e] for e in ev)
        cut_subsets=tuple(tuple(k for k,e in enumerate(ev) if e<=c) for c in range(1,n))
        blocks=link_blocks(eps,cut_subsets)
        # ground C2 = C2 of event0-only content
        g_legs=[k for k,e in enumerate(ev) if e==0]
        Cg=casimir_subset(eps,g_legs) if g_legs else {}
        # ground C2 value: it's m_g*C2_fund-ish; compute as C2 of that sub-rep on its singlet? 
        # ground content is a single fundamental (flux) or empty -> C2 = (4/3 if one fund else 0)
        gC2=C2_fund*len(g_legs)
        per.append((blocks,rows,cols,gC2))
    if any(len(b[0])==0 for b in per): return F(0)
    total=F(0)
    hl=[list(b[0].items()) for b in per]
    for combo in itertools.product(*hl):
        ds=[]
        for ci in range(n-1):
            Eint=sum(hist[ci] for (hist,blk) in combo)/2
            E0=sum(p[3] for p in per)/2
            ds.append(E0-Eint)
        w=GEN_FOLDED(ds)
        if w==0: continue
        facs=[link_factor(blk,per[i][1],per[i][2]) for i,(hist,blk) in enumerate(combo)]
        col=contract(facs)
        total+=col*w
    return total

def sigma_reduced(n,Ls=(4,)):
    rows={}
    for L in Ls:
        sets=connected_sets(L,n); tot=F(0)
        for S in sets:
            for ins,sg in sequences_over_set(S,n):
                signs=(1,)+sg+(1,)
                tot+=amplitude(L,ins,signs,n,False)-amplitude(L,ins,signs,n,True)
        rows[L]=tot/L
    return rows

if __name__=='__main__':
    known={2:F(-22,153),3:F(61,408),4:F(-737327120374220449,7250590288602460800)}
    import sys
    ns=[int(x) for x in sys.argv[1:]] or [2]
    for n in ns:
        t=time.time(); r=sigma_reduced(n); v=r[4 if 4 in r else list(r)[0]]
        kk=known.get(n)
        print(f"sigma{n}_reduced={v}  match={'?' if kk is None else v==kk}  expected={kk}  [{time.time()-t:.1f}s]")
