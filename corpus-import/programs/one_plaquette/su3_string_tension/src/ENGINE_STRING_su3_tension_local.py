#!/usr/bin/env python3
"""Exact SU(3) straight-torelon coefficients at O(y^2) and O(y^3).

Uses denominator-resolved local SU(3) fusion-tree tensors.  The O(y^2)
coefficient is an internal normalization regression; O(y^3) is the genuine
triality contribution from three coincident plaquette insertions.
"""
from __future__ import annotations
import gzip, importlib.util, itertools, json, pathlib, zipfile
from collections import defaultdict
from fractions import Fraction
import sympy as sp

E=((1,0,0),(0,1,0),(0,0,1))

def gate(name, condition, detail=""):
    print(("PASS" if condition else "FAIL"), name, detail)
    if not condition:
        raise RuntimeError(f"{name}: {detail}")

def recursive_find(name: str) -> pathlib.Path | None:
    release=pathlib.Path(__file__).resolve().parents[1]
    for p in (release/'inputs'/name, release/name, pathlib.Path.cwd()/name, pathlib.Path.cwd()/'inputs'/name):
        if p.exists(): return p
    return None

def load_module(name, path):
    spec=importlib.util.spec_from_file_location(name,str(path))
    module=importlib.util.module_from_spec(spec); assert spec.loader
    spec.loader.exec_module(module); return module

def ensure_sources():
    s3b=recursive_find('stage3b.py'); s3g=recursive_find('stage3g.py')
    if s3b and s3g: return s3b,s3g
    z=recursive_find('y4_extracted_sources.zip')
    if z is None: raise FileNotFoundError('Missing y4_extracted_sources.zip')
    out=z.parent/'_y4_sources_for_tension';out.mkdir(exist_ok=True)
    with zipfile.ZipFile(z) as f:f.extractall(out)
    s3b=next(out.rglob('stage3b.py'));s3g=next(out.rglob('stage3g.py'))
    return s3b,s3g

def vadd(a,b): return tuple(a[i]+b[i] for i in range(3))
def modx(v,L): return (v[0]%L,v[1],v[2])
def plaquette_edges(p,L):
    x=modx(p[:3],L);a,b=p[3:]
    xa=modx(vadd(x,E[a]),L);xb=modx(vadd(x,E[b]),L)
    return [((*x,a),+1,0,1),((*xa,b),+1,1,2),
            ((*xb,a),-1,2,3),((*x,b),-1,3,0)]
def torelon_edges(L):
    return [((x,0,0,0),+1,x,(x+1)%L) for x in range(L)]

def build_specs(L,p,ins_signs,vacuum=False):
    k=len(ins_signs); gate('order is 2 or 3',k in (2,3),str(k))
    eff=[1]+list(ins_signs)+[0]*(4-k)+[-1]
    events=[];off=0
    ed=[] if vacuum else torelon_edges(L);events.append((ed,off));off+=0 if vacuum else L
    for i in range(4):
        ed=plaquette_edges(p,L) if i<k else []
        events.append((ed,off));off+=4 if i<k else 0
    ed=[] if vacuum else torelon_edges(L);events.append((ed,off));off+=0 if vacuum else L
    links=defaultdict(list)
    for ei,(eds,o) in enumerate(events):
        for edge,(link,inc,sc,ec) in enumerate(eds):
            token=eff[ei]*inc
            rv=o+(sc if inc==1 else ec);cv=o+(ec if inc==1 else sc)
            links[link].append((ei,edge,token,rv,cv))
    specs=[]
    for link,occ in sorted(links.items()):
        sig=[0]*6
        for ei,edge,tok,rv,cv in occ:
            if sig[ei]!=0: raise RuntimeError('duplicate event/link incidence')
            sig[ei]=tok
        specs.append((tuple(sig),tuple(x[3] for x in occ),tuple(x[4] for x in occ),link))
    return specs

class LocalPathCompiler:
    def __init__(self):
        p3b,p3g=ensure_sources();self.s3b=load_module('tension_stage3b',p3b)
        self.s3g=load_module('tension_stage3g',p3g);M=self.s3g.M;self.M=M
        cp=recursive_find('y4_irrep_carriers.json.gz')
        ep=recursive_find('y4_exact_edge_intertwiners.json.gz')
        if cp is None or ep is None: raise FileNotFoundError('Missing carrier/intertwiner inputs')
        carrier_payload=json.load(gzip.open(cp,'rt'))
        self.carriers={tuple(r['irrep']):M.Carrier(r) for r in carrier_payload['carriers']}
        edge_payload=json.load(gzip.open(ep,'rt'))
        def matrix(rec):
            m=sp.zeros(rec['rows'],rec['cols'])
            for i,j,a,b in rec['entries']:m[i,j]=sp.Rational(a,b)
            return m
        self.edges={(tuple(r['source']),int(r['token']),tuple(r['target'])):matrix(r['embedding'])
                    for r in edge_payload['edges']}
        self.cache={}
    def records(self,signature):
        signature=tuple(signature)
        if signature in self.cache:return self.cache[signature]
        out=[];M=self.M
        for path in self.s3b.full_irrep_paths(signature):
            emb=sp.Matrix([[1]]);source=(0,0)
            for ei,tok in enumerate(signature):
                target=path[ei+1]
                if tok==0:
                    if target!=source:raise RuntimeError('zero-token irrep changed')
                else:
                    emb=sp.kronecker_product(emb,sp.eye(3))*self.edges[(source,tok,target)]
                source=target
            v=M.canonical_to_standard_vector(emb,signature,self.carriers)
            norm=sp.Rational((v.T*v)[0]);active=tuple(i for i,t in enumerate(signature) if t)
            table={};degree=len(active)
            for idx in range(v.rows):
                value=sp.Rational(v[idx])
                if value:
                    n=idx;digits=[0]*degree
                    for j in range(degree-1,-1,-1):digits[j]=n%3;n//=3
                    table[tuple(digits)]=Fraction(int(value.p),int(value.q))
            e6=tuple(self.s3b.c2_num(path[i]) for i in (2,3,4))
            out.append({'table':table,'norm':Fraction(int(norm.p),int(norm.q)),'E6':e6})
        if not out:raise RuntimeError(f'No invariant path for {signature}')
        self.cache[signature]=out;return out

def multiply(f,g):
    sf,tf=f;sg,tg=g;setf=set(sf);common=[x for x in sf if x in set(sg)]
    if not common:
        scope=sf+sg;out=defaultdict(Fraction)
        for af,cf in tf.items():
            for ag,cg in tg.items():out[af+ag]+=cf*cg
        return scope,{a:c for a,c in out.items() if c}
    pf=[sf.index(x) for x in common];pg=[sg.index(x) for x in common]
    buckets=defaultdict(list)
    for ag,cg in tg.items():buckets[tuple(ag[i] for i in pg)].append((ag,cg))
    extra=[i for i,x in enumerate(sg) if x not in setf]
    scope=sf+tuple(sg[i] for i in extra);out=defaultdict(Fraction)
    for af,cf in tf.items():
        for ag,cg in buckets.get(tuple(af[i] for i in pf),[]):
            out[af+tuple(ag[i] for i in extra)]+=cf*cg
    return scope,{a:c for a,c in out.items() if c}

def eliminate(f,var):
    scope,table=f;i=scope.index(var);new=scope[:i]+scope[i+1:];out=defaultdict(Fraction)
    for a,c in table.items():out[a[:i]+a[i+1:]]+=c
    return new,{a:c for a,c in out.items() if c}

def minfill(scopes):
    variables=set(x for s in scopes for x in s);adj={v:set() for v in variables}
    for s in scopes:
        for i,a in enumerate(s):
            for b in s[i+1:]:adj[a].add(b);adj[b].add(a)
    alive=set(variables);order=[]
    while alive:
        candidates=[]
        for v in alive:
            ns=adj[v]&alive;l=list(ns)
            fill=sum(b not in adj[a] for i,a in enumerate(l) for b in l[i+1:])
            candidates.append(((fill,len(ns),v),v,ns))
        _,v,ns=min(candidates,key=lambda x:x[0]);l=list(ns)
        for i,a in enumerate(l):
            for b in l[i+1:]:adj[a].add(b);adj[b].add(a)
        alive.remove(v);order.append(v)
    return order

def contract(factors):
    factors=list(factors)
    for var in minfill([f[0] for f in factors]):
        selected=[f for f in factors if var in f[0]]
        factors=[f for f in factors if var not in f[0]]
        h=selected[0]
        for f in selected[1:]:h=multiply(h,f)
        factors.append(eliminate(h,var))
    h=factors[0]
    for f in factors[1:]:h=multiply(h,f)
    if h[0] or any(k!=() for k in h[1]):raise RuntimeError('non-scalar contraction')
    return h[1].get((),Fraction(0))

def amplitude(compiler,L,p,signs,vacuum=False):
    specs=build_specs(L,p,signs,vacuum);libraries=[compiler.records(s) for s,_,_,_ in specs]
    total=Fraction(0)
    for choice in itertools.product(*[range(len(x)) for x in libraries]):
        factors=[];norm=Fraction(1);energies=[0,0,0]
        for (_,rows,cols,_),paths,index in zip(specs,libraries,choice):
            path=paths[index];factors.extend(((tuple(rows),path['table']),(tuple(cols),path['table'])))
            norm*=path['norm']
            for j,e in enumerate(path['E6']):energies[j]+=e
        raw=contract(factors)/norm;base=0 if vacuum else 4*L
        denominators=[Fraction(base-energies[j],6) for j in range(len(signs)-1)]
        if any(d==0 for d in denominators):raise RuntimeError('unexpected resonant denominator')
        value=raw
        for d in denominators:value/=d
        total+=value
    return total

def coefficients(lengths=(4,5)):
    compiler=LocalPathCompiler();rows=[]
    for L in lengths:
        p=(0,0,0,0,1)
        d2=[]
        for signs in ((1,-1),(-1,1)):
            d2.append(amplitude(compiler,L,p,signs)-amplitude(compiler,L,p,signs,True))
        d3=[]
        for signs in ((1,1,1),(-1,-1,-1)):
            d3.append(amplitude(compiler,L,p,signs)-amplitude(compiler,L,p,signs,True))
        # four plaquettes touch each string link.
        sigma2=4*sum(d2,Fraction(0));sigma3=4*sum(d3,Fraction(0))
        rows.append({'L':L,'sigma2':sigma2,'sigma3':sigma3,'orientation_differences_o2':d2,
                     'orientation_differences_o3':d3})
    gate('O(y^2) length independence',len({r['sigma2'] for r in rows})==1,str(rows))
    gate('O(y^3) length independence',len({r['sigma3'] for r in rows})==1,str(rows))
    gate('O(y^2) normalization regression',rows[0]['sigma2']==Fraction(-22,153),str(rows[0]['sigma2']))
    gate('O(y^3) charge-conjugate equality',all(r['orientation_differences_o3'][0]==r['orientation_differences_o3'][1] for r in rows))
    gate('O(y^3) exact coefficient',rows[0]['sigma3']==Fraction(61,408),str(rows[0]['sigma3']))
    return rows[0]['sigma2'],rows[0]['sigma3'],rows

if __name__=='__main__':
    import sys,json
    s2,s3,rows=coefficients()
    payload={'sigma2':str(s2),'sigma3':str(s3),'rows':[{k:([str(x) for x in v] if isinstance(v,list) else str(v) if isinstance(v,Fraction) else v) for k,v in r.items()} for r in rows]}
    if len(sys.argv)>1:pathlib.Path(sys.argv[1]).write_text(json.dumps(payload,indent=2,sort_keys=True))
    print('SIGMA2',s2);print('SIGMA3',s3)
