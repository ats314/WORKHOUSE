#!/usr/bin/env python3
"""Exact connected fourth-order SU(3) straight-torelon tension coefficient."""
from __future__ import annotations
import importlib.util,itertools,math,pathlib
from collections import defaultdict
from fractions import Fraction

E=((1,0,0),(0,1,0),(0,0,1))

def gate(name,condition,detail=""):
    print(("PASS" if condition else "FAIL"),name,detail)
    if not condition:raise RuntimeError(f"{name}: {detail}")

def recursive_find(name):
    release=pathlib.Path(__file__).resolve().parents[1]
    for p in (release/'inputs'/name, release/name, pathlib.Path.cwd()/name, pathlib.Path.cwd()/'inputs'/name):
        if p.exists(): return p
    return None

def load_wb():
    p=recursive_find('y4_sun_walled_brauer_fixed_rank.py')
    if p is None:raise FileNotFoundError('Missing y4_sun_walled_brauer_fixed_rank.py')
    spec=importlib.util.spec_from_file_location('tension_wb',p)
    m=importlib.util.module_from_spec(spec);assert spec.loader;spec.loader.exec_module(m);return m

wb=load_wb()
def vadd(a,b):return tuple(a[i]+b[i] for i in range(3))
def modx(v,L):return (v[0]%L,v[1],v[2])
def plaquette_edges(p,L):
    x=modx(p[:3],L);a,b=p[3:]
    xa=modx(vadd(x,E[a]),L);xb=modx(vadd(x,E[b]),L)
    return [((*x,a),+1,0,1),((*xa,b),+1,1,2),
            ((*xb,a),-1,2,3),((*x,b),-1,3,0)]
def plaquette_vertices(p,L):
    x=modx(p[:3],L);a,b=p[3:]
    return [x,modx(vadd(x,E[a]),L),modx(vadd(vadd(x,E[a]),E[b]),L),modx(vadd(x,E[b]),L)]
def torelon_edges(L):return [((x,0,0,0),+1,x,(x+1)%L) for x in range(L)]

def build_specs(L,insertions,signs,vacuum=False):
    if len(insertions)!=4 or len(signs)!=6:raise RuntimeError('four insertion slots required')
    eff=list(signs[:5])+[-signs[5]];events=[];offset=0
    ed=[] if vacuum else torelon_edges(L);events.append((ed,offset));offset+=0 if vacuum else L
    for p in insertions:
        ed=plaquette_edges(p,L);events.append((ed,offset));offset+=4
    ed=[] if vacuum else torelon_edges(L);events.append((ed,offset));offset+=0 if vacuum else L
    links=defaultdict(list)
    for ei,(edges,off) in enumerate(events):
        for edge,(link,inc,sc,ec) in enumerate(edges):
            token=eff[ei]*inc
            rv=off+(sc if inc==1 else ec);cv=off+(ec if inc==1 else sc)
            links[link].append((ei,edge,token,rv,cv))
    specs=[];groups=[]
    for link,occ in sorted(links.items()):
        occ=tuple(sorted(occ));sig=[0]*6
        for ei,edge,t,rv,cv in occ:
            if sig[ei]!=0:raise RuntimeError('duplicate event/link incidence')
            sig[ei]=t
        sig=tuple(sig)
        if sig.count(1)!=sig.count(-1):return None,None,offset
        specs.append((sig,tuple(x[3] for x in occ),tuple(x[4] for x in occ)));groups.append(occ)
    return specs,tuple(groups),offset

def min_fill(scopes,nvar):
    adj=[set() for _ in range(nvar)];used=set()
    for s in scopes:
        s=sorted(set(s));used.update(s)
        for i,a in enumerate(s):
            for b in s[i+1:]:adj[a].add(b);adj[b].add(a)
    alive=set(used);order=[];width=0
    while alive:
        best=None
        for v in alive:
            ns=adj[v]&alive;l=list(ns)
            fill=sum(b not in adj[a] for i,a in enumerate(l) for b in l[i+1:])
            cand=(fill,len(ns),v)
            if best is None or cand<best[0]:best=(cand,v,ns)
        _,v,ns=best;width=max(width,len(ns));l=list(ns)
        for i,a in enumerate(l):
            for b in l[i+1:]:adj[a].add(b);adj[b].add(a)
        alive.remove(v);order.append(v)
    return tuple(order),width

def folded(energy,N,L0):
    ds=[]
    for A,B,C in energy:ds.append(Fraction((L0-A)*N*N-B*N+C-L0,4*N))
    zero=sum(d==0 for d in ds);non=[d for d in ds if d]
    if zero==0:return 1/(ds[0]*ds[1]*ds[2])
    if zero==1:
        x,y=non;return -(1/(x*x*y)+1/(x*y*y))/2
    if zero==2:return Fraction(1,3)/(non[0]**3)
    return Fraction(0)

class Contractor:
    def __init__(self,N=3):self.N=N;self.lib=wb.LocalLibrary(N);self.cache={}
    def amplitude(self,L,insertions,signs,vacuum=False):
        specs,groups,nvar=build_specs(L,insertions,signs,vacuum)
        if specs is None:return Fraction(0),0,0
        key=(0 if vacuum else L,groups)
        if key in self.cache:return self.cache[key]
        for sig,_,_ in specs:self.lib.get(sig)
        scopes=[]
        for _,r,c in specs:scopes.extend((r,c))
        order,width=min_fill(scopes,nvar);ranges=[range(len(self.lib.get(s))) for s,_,_ in specs]
        total=Fraction(0);paths=0
        for choices in itertools.product(*ranges):
            raw,energy=wb.contract_choice(specs,choices,self.lib,order)
            total+=raw*folded(energy,self.N,0 if vacuum else L);paths+=1
        self.cache[key]=(total,paths,width);return self.cache[key]

def adjacent_plaquettes(L):
    out=set()
    for x in range(L):
        for b in (1,2):
            out.add((x,0,0,0,b));anchor=[x,0,0];anchor[b]=-1;out.add((*anchor,0,b))
    return sorted(out)
def site_neighbors(p,L):
    out=set()
    for v in plaquette_vertices(p,L):
        for a,b in ((0,1),(0,2),(1,2)):
            for ia in (0,1):
                for ib in (0,1):
                    anc=[v[i] for i in range(3)];anc[a]-=ia;anc[b]-=ib;anc[0]%=L
                    out.add((*anc,a,b))
    return out
def sequences(p,q):
    if p==q:
        for plus in itertools.combinations(range(4),2):
            sg=[-1]*4
            for i in plus:sg[i]=1
            yield (p,p,p,p),tuple(sg)
    else:
        for ppos in itertools.combinations(range(4),2):
            qpos=tuple(i for i in range(4) if i not in ppos)
            for sp in ((1,-1),(-1,1)):
                for sq in ((1,-1),(-1,1)):
                    ins=[None]*4;sg=[0]*4
                    for pos,s in zip(ppos,sp):ins[pos]=p;sg[pos]=s
                    for pos,s in zip(qpos,sq):ins[pos]=q;sg[pos]=s
                    yield tuple(ins),tuple(sg)

def coefficient(L,N=3):
    con=Contractor(N);adj=adjacent_plaquettes(L);pairs=set()
    for p in adj:
        for q in site_neighbors(p,L):pairs.add(tuple(sorted((p,q))))
    total=Fraction(0);nonzero=0;sequence_count=0;path_count=0;ledger=[]
    for p,q in sorted(pairs):
        value=Fraction(0)
        for ins,sg4 in sequences(p,q):
            signs=(1,)+sg4+(1,)
            a,pa,_=con.amplitude(L,ins,signs,False);v,pv,_=con.amplitude(L,ins,signs,True)
            value+=a-v;path_count+=pa+pv;sequence_count+=1
        if value:
            nonzero+=1;total+=value;ledger.append({'p':p,'q':q,'value':value})
    return {'L':L,'total':total,'per_length':total/L,'adjacent_plaquettes':len(adj),
            'candidate_pairs':len(pairs),'nonzero_pairs':nonzero,'ordered_sequences':sequence_count,
            'local_path_evaluations':path_count,'cache_records':len(con.cache),'ledger':ledger}

def coefficients(lengths=(4,5)):
    rows=[coefficient(L) for L in lengths]
    gate('O(y^4) length independence',len({r['per_length'] for r in rows})==1,
         str([r['per_length'] for r in rows]))
    expected=Fraction(-737327120374220449,7250590288602460800)
    gate('O(y^4) exact coefficient',rows[0]['per_length']==expected,str(rows[0]['per_length']))
    gate('candidate-pair extensivity',all(r['candidate_pairs']==110*r['L'] for r in rows),
         str([r['candidate_pairs'] for r in rows]))
    gate('nonzero-pair extensivity',all(r['nonzero_pairs']==42*r['L'] for r in rows),
         str([r['nonzero_pairs'] for r in rows]))
    return expected,rows

if __name__=='__main__':
    import sys,json
    sigma4,rows=coefficients()
    def conv(x):
        if isinstance(x,Fraction):return str(x)
        if isinstance(x,tuple):return [conv(v) for v in x]
        if isinstance(x,list):return [conv(v) for v in x]
        if isinstance(x,dict):return {k:conv(v) for k,v in x.items()}
        return x
    payload={'sigma4':str(sigma4),'rows':conv(rows)}
    if len(sys.argv)>1:pathlib.Path(sys.argv[1]).write_text(json.dumps(payload,indent=2,sort_keys=True))
    print('SIGMA4',sigma4,float(sigma4))
    for r in rows:print({k:v for k,v in r.items() if k!='ledger'})
