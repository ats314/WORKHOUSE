#!/usr/bin/env python3
"""
ENGINE_HAAR_fast_haar.py -- exact SU(3) Haar integral of a product of Wilson-loop traces in
LINK variables, by TENSOR-NETWORK variable elimination instead of the
cartesian-product-of-terms.  Every index variable has degree 2 (it is the vertex
between two consecutive links in a trace), so the contraction is cheap even when
several links carry 3 U's (the ε-baryon case that made the naive product blow up
to 36^k terms).  Validated bit-exactly against the naive integrator.
"""
import itertools, sys, os
from collections import defaultdict
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ENGINE_FLUX_su3_moments_ext import link_terms, eval_term

def _link_table(us, bs):
    """exact integrated tensor for ONE link with given U/U-dagger slots, as a dict
    {tuple(values in sorted-var order): Fraction} over the link's index variables."""
    tl=link_terms(us,bs)
    if not tl: return None, None
    vset=set()
    for (a,b) in us: vset.add(a); vset.add(b)
    for (a,b) in bs: vset.add(a); vset.add(b)
    vs=sorted(vset)
    table={}
    for assign in itertools.product(range(3),repeat=len(vs)):
        amap=dict(zip(vs,assign)); val=F(0)
        for coeff,cons in tl:
            ok=True
            for (x,y) in cons:
                vx=amap[x[1]] if x[0]=='v' else x[1]
                vy=amap[y[1]] if y[0]=='v' else y[1]
                if vx!=vy: ok=False; break
            if ok: val+=coeff
        if val!=0: table[assign]=val
    return vs, table

_TNCACHE={}
def haar_tn(words):
    key=tuple(tuple(w) for w in words)
    if key in _TNCACHE: return _TNCACHE[key]
    nv=0; link_slots=defaultdict(lambda:([],[]))
    for w in words:
        Lw=len(w); ids=list(range(nv,nv+Lw)); nv+=Lw
        for t,(lid,pw) in enumerate(w):
            a,b=ids[t],ids[(t+1)%Lw]; us,bs=link_slots[lid]
            if pw==+1: us.append((a,b))
            else: bs.append((b,a))
    factors=[]
    for lid,(us,bs) in link_slots.items():
        vs,table=_link_table(us,bs)
        if vs is None: _TNCACHE[key]=F(0); return F(0)
        factors.append((vs,table))
    allvars=set(range(nv))
    while allvars:
        v=min(allvars, key=lambda x: sum(1 for (vs,_) in factors if x in vs))
        inv=[f for f in factors if v in f[0]]; out=[f for f in factors if v not in f[0]]
        if not inv:
            allvars.discard(v); continue
        uvars=sorted(set().union(*[set(vs) for vs,_ in inv]))
        rvars=[x for x in uvars if x!=v]
        newtab=defaultdict(lambda:F(0))
        for assign in itertools.product(range(3),repeat=len(uvars)):
            amap=dict(zip(uvars,assign)); prod=F(1)
            for vs,tab in inv:
                c=tab.get(tuple(amap[x] for x in vs),F(0))
                if c==0: prod=F(0); break
                prod*=c
            if prod!=0:
                newtab[tuple(amap[x] for x in rvars)]+=prod
        factors=out+[(rvars, dict(newtab))]
        allvars.discard(v)
    res=F(1)
    for vs,tab in factors:
        res*= tab.get((),F(0))
    _TNCACHE[key]=res; return res

# ---- naive reference (cartesian product) for validation ----
def haar_naive(words):
    nv=0; linkfac=defaultdict(lambda:([],[]))
    for w in words:
        Lw=len(w); ids=list(range(nv,nv+Lw)); nv+=Lw
        for t,(lid,pw) in enumerate(w):
            a,b=ids[t],ids[(t+1)%Lw]; us,bs=linkfac[lid]
            if pw==+1: us.append((a,b))
            else: bs.append((b,a))
    term_lists=[]
    for (us,bs) in linkfac.values():
        tl=link_terms(us,bs)
        if not tl: return F(0)
        term_lists.append(tl)
    tot=F(0)
    for combo in itertools.product(*term_lists):
        coeff=F(1); cons=()
        for (c_,k_) in combo: coeff*=c_; cons=cons+k_
        if coeff!=0: tot+=eval_term(coeff,cons,nv)
    return tot

if __name__=="__main__":
    import time
    GATES=[]
    def gate(n,c):
        GATES.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}")
        if not c: raise SystemExit("FAIL")
    # plaquette + neighbours, in link variables
    P=[(0,+1),(1,+1),(2,+1),(3,+1)]
    Pd=[(g,-p) for (g,p) in reversed(P)]
    tests={
        "norm |Tr p|^2 =1": ([P,Pd], F(1)),
        "Tr p (single) =0": ([P], F(0)),
        "<p|Tr p|vac>^2 route Tr(p)^2*Tr(pd) (eps)": ([P,P,Pd], None),
        "Tr(p)^3 (4 eps links, the slow one)": ([P,P,P], None),
        "Tr(p)^3 conj": ([Pd,Pd,Pd], None),
    }
    for nm,(words,exp) in tests.items():
        t=time.time(); tn=haar_tn(words); dt_tn=time.time()-t
        t=time.time(); nv=haar_naive(words); dt_nv=time.time()-t
        gate(f"{nm}: tn==naive ({tn})  [tn {dt_tn:.2f}s vs naive {dt_nv:.2f}s]", tn==nv)
        if exp is not None:
            gate(f"{nm} == {exp}", tn==exp)
    print(f"ALL {sum(GATES)}/{len(GATES)} GATES PASSED")
