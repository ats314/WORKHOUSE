"""
Generic-order native SU(N) torelon string-tension engine.
Reuses the validated walled-Brauer contraction primitives + generic PT history core
+ generic des-Cloizeaux folding. Order-generalizes sigma4.py's cluster enumeration.
HARD GATE: must reproduce sigma2, sigma3, sigma4 before any sigma5 is trusted.
"""
import importlib.util, itertools, pathlib, sys
from collections import defaultdict
from fractions import Fraction

INP = pathlib.Path('/home/claude/batch/SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2/SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2/inputs')
PRE = pathlib.Path('/home/claude/batch/SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14/SU3_O5_CONSOLIDATED_AND_Y6_PREFLIGHT_2026-06-14')

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path)); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m

st = load('st', INP/'y4_sun_stable_rank_stage1.py')
fpm = load('fp', PRE/'ENGINE_Y6_folded_descloizeaux_preflight.py')
GEN_FOLDED = fpm.folded_coefficient

# ---- generic PT history (validated 729/729 vs 4th order) ----
def generic_histories(tokens, n_insertions):
    cut_events = set(range(1, n_insertions))
    states = {((), ()): __import__('collections').Counter({(): 1})}
    from collections import Counter
    for ei, token in enumerate(tokens):
        nxt = defaultdict(Counter)
        for state, hs in states.items():
            for s2 in st.branch(state, token):
                for h, m in hs.items():
                    h2 = h + (st.casimir_key(s2),) if ei in cut_events else h
                    nxt[s2][h2] += m
        states = nxt
    from collections import Counter as C
    return C(states.get(((), ()), {}))

# set N_INS dynamically; patch the wb-internal st + CUTS to match the order
_NINS = {'n': 4}
wb = load('wb', INP/'y4_sun_walled_brauer_fixed_rank.py')
def set_order(n):
    _NINS['n']=n
    wb.st.local_channel_histories = lambda tokens: generic_histories(tokens, n)
    wb.CUTS = tuple(range(1, n))
set_order(4)

E = ((1,0,0),(0,1,0),(0,0,1))
def vadd(a,b): return tuple(a[i]+b[i] for i in range(3))
def modx(v,L): return (v[0]%L, v[1], v[2])
def pedges(p,L):
    x=modx(p[:3],L);a,b=p[3:];xa=modx(vadd(x,E[a]),L);xb=modx(vadd(x,E[b]),L)
    return [((*x,a),+1,0,1),((*xa,b),+1,1,2),((*xb,a),-1,2,3),((*x,b),-1,3,0)]
def pverts(p,L):
    x=modx(p[:3],L);a,b=p[3:]
    return [x,modx(vadd(x,E[a]),L),modx(vadd(vadd(x,E[a]),E[b]),L),modx(vadd(x,E[b]),L)]
def torelon_edges(L): return [((x,0,0,0),+1,x,(x+1)%L) for x in range(L)]

def build_specs(L, insertions, signs, vacuum=False):
    n = len(insertions)
    assert len(signs) == n+2
    eff = list(signs[:n+1]) + [-signs[n+1]]
    events=[]; offset=0
    ed=[] if vacuum else torelon_edges(L); events.append((ed,offset)); offset += 0 if vacuum else L
    for p in insertions:
        ed=pedges(p,L); events.append((ed,offset)); offset+=4
    ed=[] if vacuum else torelon_edges(L); events.append((ed,offset)); offset += 0 if vacuum else L
    links=defaultdict(list)
    for ei,(edges,off) in enumerate(events):
        for edge,(link,inc,sc,ec) in enumerate(edges):
            token=eff[ei]*inc; rv=off+(sc if inc==1 else ec); cv=off+(ec if inc==1 else sc)
            links[link].append((ei,edge,token,rv,cv))
    specs=[]; groups=[]
    for link,occ in sorted(links.items()):
        occ=tuple(sorted(occ)); sig=[0]*(n+2)
        for ei,edge,t,rv,cv in occ:
            if sig[ei]!=0: raise RuntimeError('dup')
            sig[ei]=t
        sig=tuple(sig)
        if sig.count(1)!=sig.count(-1): return None,None,offset
        specs.append((sig,tuple(x[3] for x in occ),tuple(x[4] for x in occ))); groups.append(occ)
    return specs, tuple(groups), offset

def generic_contract(link_specs, choices, lib, order, ncuts):
    factors=[]; norm=Fraction(1); energy=[[0,0,0] for _ in range(ncuts)]
    for (sig,rows,cols),pi in zip(link_specs,choices):
        path=lib.get(sig)[pi]
        factors.append(wb.factor_from_vector(sig,rows,path)); factors.append(wb.factor_from_vector(sig,cols,path)); norm*=path['norm']
        for cut,key in enumerate(path['history']):
            for j,x in enumerate(key): energy[cut][j]+=x
    for var in order:
        sel=[f for f in factors if var in f[0]]; factors=[f for f in factors if var not in f[0]]
        if not sel: continue
        c=sel[0]
        for f in sel[1:]: c=wb.multiply_factor(c,f)
        terms=defaultdict(Fraction)
        for p,x in c[1].items():
            q,m=wb.eliminate_partition(p,var,lib.N); terms[q]+=x*m
        scope=tuple(x for x in c[0] if x!=var); factors.append((scope,{p:x for p,x in terms.items() if x}))
    c=factors[0]
    for f in factors[1:]: c=wb.multiply_factor(c,f)
    assert c[0]==()
    if not c[1]: return Fraction(0), tuple(tuple(x) for x in energy)
    assert set(c[1])=={()}
    return c[1][()]/norm, tuple(tuple(x) for x in energy)

def folded_from_energy(energy, N, L0):
    ds=[Fraction((L0-A)*N*N - B*N + C - L0, 4*N) for (A,B,C) in energy]
    return GEN_FOLDED(ds)

class Contractor:
    def __init__(self,N,n): self.N=N; self.n=n; self.lib=wb.LocalLibrary(N); self.cache={}
    def amplitude(self, L, insertions, signs, vacuum=False):
        specs,groups,nvar = build_specs(L,insertions,signs,vacuum)
        if specs is None: return Fraction(0)
        key=(0 if vacuum else L, groups)
        if key in self.cache: return self.cache[key]
        for sig,_,_ in specs: self.lib.get(sig)
        scopes=[]
        for _,r,c in specs: scopes.extend((r,c))
        order,width = wb.min_fill(scopes,nvar)
        ranges=[range(len(self.lib.get(s))) for s,_,_ in specs]
        total=Fraction(0)
        for choices in itertools.product(*ranges):
            raw,energy = generic_contract(specs,choices,self.lib,order,self.n-1)
            total += raw*folded_from_energy(energy,self.N, 0 if vacuum else L)
        self.cache[key]=total; return total

# ---- generic cluster enumeration ----
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

def connected_sets(L, n):
    """connected plaquette sets (frozensets), size 1..n, each containing >=1 torelon-adjacent plaquette."""
    adj=adjacent_plaquettes(L)
    seen=set(); frontier=[frozenset([p]) for p in adj]
    for s in frontier: seen.add(s)
    out=list(frontier)
    while frontier:
        nf=[]
        for s in frontier:
            if len(s)>=n: continue
            # neighbors of the whole set
            nb=set()
            for p in s: nb|=site_neighbors(p,L)
            for q in nb:
                if q in s: continue
                t=s|{q}
                if t not in seen:
                    seen.add(t); nf.append(t); out.append(t)
        frontier=nf
    return [s for s in out if len(s)<=n]

def sequences_over_set(S, n):
    """all ordered length-n (plaquette,sign) draws using every plaquette in S."""
    S=list(S); k=len(S)
    for assign in itertools.product(range(k), repeat=n):
        if len(set(assign))!=k: continue   # every plaquette used
        for sgn in itertools.product((1,-1), repeat=n):
            yield tuple(S[i] for i in assign), tuple(sgn)

def sigma_reduced(n, lengths=(4,5), N=3):
    set_order(n)
    rows={}
    for L in lengths:
        con=Contractor(N,n)
        sets=connected_sets(L,n)
        total=Fraction(0)
        for S in sets:
            for ins,sg in sequences_over_set(S,n):
                signs=(1,)+sg+(1,)
                a=con.amplitude(L,ins,signs,False); v=con.amplitude(L,ins,signs,True)
                total+=a-v
        rows[L]=total/L
    return rows

if __name__=='__main__':
    known={2:Fraction(-22,153),3:Fraction(61,408),4:Fraction(-737327120374220449,7250590288602460800)}
    import time
    for n in (2,3,4):
        t0=time.time()
        rows=sigma_reduced(n)
        vals=set(rows.values())
        Lind = len(vals)==1
        val=rows[4]
        ok = (val==known[n])
        print(f"sigma{n}: per_length={val}  L-independent={Lind}  matches_known={ok}  [{time.time()-t0:.1f}s]  rows={ {k:str(v) for k,v in rows.items()} }")
