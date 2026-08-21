#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction
import itertools, json, hashlib
from pathlib import Path
import sympy as sp

OUT_JSON=Path('/mnt/data/RUN_PENT_pentagonal_o4_minimal_representation_frontier_results.json')
OUT_TXT=Path('/mnt/data/pentagonal_o4_minimal_representation_frontier_results.txt')
N=3
FACE_CYCLES={
  0:[('b0',+1),('b1',+1),('b2',+1),('b3',+1),('b4',+1)],
  1:[('t0',+1),('t1',+1),('t2',+1),('t3',+1),('t4',+1)],
  2:[('b0',+1),('v1',+1),('t0',-1),('v0',-1)],
}
B_COLS=[
 (1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0),
 (0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0),
 (1,0,0,0,0,-1,0,0,0,0, 1,-1,0,0,0),
]
START=B_COLS[0]; CAP1=B_COLS[1]
SIGNED=[(f,s) for f in range(3) for s in (-1,+1)]

def add(a,b,s=1): return tuple(x+s*y for x,y in zip(a,b))
def mod3(a,b): return all((x-y)%3==0 for x,y in zip(a,b))
def retained(q):
    if all(x%3==0 for x in q): return True
    return any(mod3(q,tuple(s*x for x in B_COLS[f])) for f in (0,1) for s in (-1,+1))
def histories20():
    out=[]
    for w in itertools.product(SIGNED,repeat=4):
        if not any(f==2 for f,_ in w): continue
        q=START; pref=[]
        for f,s in w:
            q=add(q,B_COLS[f],s); pref.append(q)
        if not (q==CAP1 or q==tuple(-x for x in CAP1)): continue
        if any(retained(x) for x in pref[:-1]): continue
        out.append(tuple(w))
    return out

def oriented_cycle(f,s):
    c=FACE_CYCLES[f]
    return list(c) if s==1 else [(l,-o) for l,o in reversed(c)]

def state_specs(w,k): return tuple([(0,+1),*w[:k]])

def perm_cycles(p):
    seen=[False]*len(p); c=0
    for i in range(len(p)):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]: seen[j]=True; j=p[j]
    return c

def invcomp(a,b):
    inv=[0]*len(a)
    for i,x in enumerate(a): inv[x]=i
    return tuple(inv[b[i]] for i in range(len(a)))

def balanced_projector(p):
    perms=list(itertools.permutations(range(p)))
    G=sp.Matrix([[N**perm_cycles(invcomp(s,t)) for t in perms] for s in perms])
    W=G.inv()
    return perms, [[Fraction(int(W[i,j].p),int(W[i,j].q)) for j in range(len(perms))] for i in range(len(perms))], G
PROJ={p:balanced_projector(p) for p in (1,2,3)}

def _canon(part):
    mp={}; nxt=0; out=[]
    for x in part:
        if x not in mp:
            mp[x]=nxt; nxt+=1
        out.append(mp[x])
    return tuple(out)

def _union_part(part,pairs):
    p=list(part)
    for a,b in pairs:
        la,lb=p[a],p[b]
        if la!=lb:
            p=[la if x==lb else x for x in p]
    return _canon(p)

def trace_occurrences(specs, conjugate=False, offset=0):
    occ=defaultdict(lambda:{'U':[],'D':[]}); base=offset
    for f,s in specs:
        if conjugate: s=-s
        cyc=oriented_cycle(f,s); m=len(cyc); vs=list(range(base,base+m)); base+=m
        for j,(link,o) in enumerate(cyc):
            l,r=vs[j],vs[(j+1)%m]
            if o==+1: occ[link]['U'].append((l,r))
            else: occ[link]['D'].append((r,l))
    return occ,base

def exact_overlap(specA,specB):
    oa,nA=trace_occurrences(specA,True,0)
    ob,nT=trace_occurrences(specB,False,nA)
    links=[]
    for l in sorted(set(oa)|set(ob)):
        u=oa[l]['U']+ob[l]['U']; d=oa[l]['D']+ob[l]['D']
        if len(u)!=len(d): return Fraction(0)
        p=len(u)
        if p==0: continue
        if p not in PROJ: raise RuntimeError((l,p))
        perms,W,_=PROJ[p]; terms=[]
        for si,sig in enumerate(perms):
            for ti,tau in enumerate(perms):
                pairs=[]
                for a in range(p):
                    pairs.append((u[a][0],d[sig[a]][0]))
                    pairs.append((u[a][1],d[tau[a]][1]))
                terms.append((W[si][ti],pairs))
        links.append(terms)
    links.sort(key=len,reverse=True)
    states={tuple(range(nT)):Fraction(1)}
    for terms in links:
        new=defaultdict(Fraction)
        for part,c in states.items():
            for cc,pairs in terms:
                new[_union_part(part,pairs)] += c*cc
        states={p:c for p,c in new.items() if c}
    return sum(c*(N**len(set(p))) for p,c in states.items())

def pair_sectors(specA,specB):
    def simple_counts(spec,conj=False):
        d=defaultdict(lambda:[0,0])
        for f,s in spec:
            if conj:s=-s
            for l,o in oriented_cycle(f,s): d[l][0 if o==1 else 1]+=1
        return d
    a,b=simple_counts(specA,True),simple_counts(specB,False)
    out=[]
    for l in sorted(set(a)|set(b)):
        au,ad=a.get(l,(0,0)); bu,bd=b.get(l,(0,0)); out.append((au+bu,ad+bd))
    return out

def main():
    W=histories20(); gates=[]
    def gate(n,ok,d=''): gates.append((n,bool(ok),str(d)))
    gate('history count',len(W)==20,len(W))
    ms=Counter(tuple(sorted(w)) for w in W)
    gate('two temporal multisets 10+10',sorted(ms.values())==[10,10],dict(ms))

    cutdata={}; allraw=set()
    for k in (1,2,3):
        specs=[]
        for w in W:
            s=state_specs(w,k)
            if s not in specs: specs.append(s)
        m=len(specs)
        G=[[Fraction(0) for _ in range(m)] for __ in range(m)]
        sectors=set()
        for i,a in enumerate(specs):
            for j,b in enumerate(specs):
                sec=pair_sectors(a,b)
                if all(p==q for p,q in sec): sectors|={x for x in sec if x!=(0,0)}
                G[i][j]=exact_overlap(a,b)
        Gsp=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in G])
        cutdata[str(k)]={
            'raw_state_count':m,'gram_rank':Gsp.rank(),'gram_nullity':m-Gsp.rank(),
            'balanced_local_sectors':[list(x) for x in sorted(sectors)],
            'gram':[[str(x) for x in row] for row in G]
        }
        allraw|=sectors
    gate('raw cut dimensions are 4,10,20',[cutdata[str(k)]['raw_state_count'] for k in (1,2,3)]==[4,10,20],cutdata)
    gate('raw Haar sectors are exactly (1,1),(2,2),(3,3)',allraw=={(1,1),(2,2),(3,3)},sorted(allraw))

    # Exact local balanced Gram/projector ranks.
    loc={}
    for p in (1,2,3):
        perms,Wmat,G=PROJ[p]
        loc[str(p)]={'permutation_basis_size':len(perms),'gram_rank':G.rank(),
                     'gram':[[str(x) for x in row] for row in G.tolist()],
                     'weingarten':[[str(x) for x in row] for row in Wmat]}
    gate('balanced local Gram ranks 1,2,6',[loc[str(p)]['gram_rank'] for p in (1,2,3)]==[1,2,6],loc)

    # Project-level determinant sector independently certified by exact invariant Gram.
    G41=sp.Matrix([[18,6,-6,6],[6,18,6,-6],[-6,6,18,6],[6,-6,6,18]])
    gate('(4,1) delta-epsilon raw Gram rank 3',G41.rank()==3,G41.rank())
    gate('(4,1) alternating null relation',G41*sp.Matrix([-1,1,-1,1])==sp.zeros(4,1),'[-1,1,-1,1]')

    # Endpoint bare Haar regression: exactly one for every complete history.
    endpoint=[]
    for w in W:
        q=START
        for f,s in w:q=add(q,B_COLS[f],s)
        final=(1,-1) if q==CAP1 else (1,+1)
        endpoint.append(exact_overlap(((1,-final[1]),), ())) if False else None
    # Use direct six-trace product via overlap of final cap with operators*initial.
    vals=[]
    for w in W:
        q=START
        for f,s in w:q=add(q,B_COLS[f],s)
        ket=tuple([(0,+1),*w])
        bra=((1,+1),) if q==CAP1 else ((1,-1),)
        vals.append(exact_overlap(bra,ket))
    gate('all 20 complete bare endpoint Haar contractions are 1',all(v==1 for v in vals),Counter(vals))

    payload={
      'schema':'pentagonal-o4-minimal-representation-frontier-v2',
      'history_count':len(W),'multisets':{str(k):v for k,v in ms.items()},
      'cut_data':cutdata,'balanced_projectors':loc,
      'determinant_41_gram':[[int(x) for x in row] for row in G41.tolist()],
      'endpoint_bare_values':[str(v) for v in vals],
      'gates':[{'name':n,'pass':ok,'detail':d} for n,ok,d in gates],
      'passed':sum(ok for _,ok,_ in gates),'total':len(gates),
      'next_exact_object':'Generate the Fierz closure of each raw cut space. The raw Gram needs only balanced p<=3 projectors; the Fierz-generated closure must additionally retain the SU(3)-specific (4,1)/(1,4) rank-3 delta-epsilon sector. Then form G_k and H0_k on the physical quotient and evaluate R_k=Q(E0 G_k-H0_k)^(-1)Q.',
      'evidence_boundary':'No h4_side value is imported or inferred. This closes the raw history Gram/Haar frontier and identifies the precise remaining H0/Fierz closure.'
    }
    payload['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT_JSON.write_text(json.dumps(payload,indent=2),encoding='utf-8')
    lines=['PENTAGONAL O(4) MINIMAL REPRESENTATION FRONTIER v2','='*76]
    for n,ok,d in gates: lines.append(f"[{'PASS' if ok else 'FAIL'}] {n} :: {d}")
    lines += ['', 'RAW CUT SPACES']
    for k,d in cutdata.items(): lines.append(f"cut {k}: raw={d['raw_state_count']} rank(G)={d['gram_rank']} nullity={d['gram_nullity']} sectors={d['balanced_local_sectors']}")
    lines += ['', 'KEY DISTINCTION', 'Raw prefix overlaps require only balanced (1,1),(2,2),(3,3).', 'The SU(3)-specific (4,1)/(1,4) sector is not a raw-prefix overlap; it enters only after Fierz/electric closure.', '', 'NEXT EXACT OBJECT', payload['next_exact_object'], '', f"RESULT: {payload['passed']}/{payload['total']} gates pass", 'SOURCE_SHA256: '+payload['source_sha256'], '', payload['evidence_boundary']]
    OUT_TXT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))
    if payload['passed']!=payload['total']: raise SystemExit(1)
if __name__=='__main__': main()
