#!/usr/bin/env python3
import sympy as sp, math
from collections import Counter
E={1:(0,0,2),2:(1,0,1),3:(-1,0,1),4:(0,-1,-1),5:(0,1,-1)}
loops={
"10a":[(5,1),(4,-1),(1,1),(3,1),(1,1),(5,-1),(4,1),(1,-1),(3,-1),(1,-1)],
"10b":[(5,1),(1,-1),(3,-1),(1,-1),(4,1),(5,-1),(1,1),(3,1),(1,1),(4,-1)],
"10c":[(5,1),(1,-1),(2,-1),(1,-1),(4,1),(5,-1),(1,1),(2,1),(1,1),(4,-1)],
"10d":[(5,1),(4,-1),(1,1),(2,1),(1,1),(5,-1),(4,1),(1,-1),(2,-1),(1,-1)],
"10e":[(5,1),(1,-1),(2,-1),(3,1),(1,1),(5,-1),(1,1),(2,1),(3,-1),(1,-1)],
"10f":[(5,1),(1,-1),(3,-1),(2,1),(1,1),(5,-1),(1,1),(3,1),(2,-1),(1,-1)],
"10g":[(4,1),(1,-1),(2,-1),(3,1),(1,1),(4,-1),(1,1),(2,1),(3,-1),(1,-1)],
"10h":[(4,1),(1,-1),(3,-1),(2,1),(1,1),(4,-1),(1,1),(3,1),(2,-1),(1,-1)],
"12a":[(5,1),(4,-1),(1,1),(2,1),(3,-1),(1,-1),(4,1),(5,-1),(1,1),(3,1),(2,-1),(1,-1)],
"12b":[(5,1),(4,-1),(1,1),(3,1),(2,-1),(1,-1),(4,1),(5,-1),(1,1),(2,1),(3,-1),(1,-1)],
"12c":[(5,1),(1,-1),(3,-1),(2,1),(1,1),(5,-1),(4,1),(1,-1),(2,-1),(3,1),(1,1),(4,-1)],
"12d":[(5,1),(1,-1),(2,-1),(3,1),(1,1),(5,-1),(4,1),(1,-1),(3,-1),(2,1),(1,1),(4,-1)]}
def add(a,b,s): return tuple(a[i]+s*b[i] for i in range(3))
def verts(seq):
    v=(0,0,0); r=[v]
    for d,s in seq: v=add(v,E[d],s); r.append(v)
    return r
assert all(verts(s)[-1]==(0,0,0) for s in loops.values())
edges={}; cols={}; names=list(loops)
for n,s in loops.items():
    c=Counter(); vs=verts(s)
    for u,v in zip(vs[:-1],vs[1:]):
        if u<=v: k,sg=(u,v),1
        else: k,sg=(v,u),-1
        edges.setdefault(k,len(edges)); c[k]+=sg
    cols[n]=c
B=sp.zeros(len(edges),len(names))
for j,n in enumerate(names):
    for k,c in cols[n].items(): B[edges[k],j]=c
print("shape",B.shape,"rank",B.rank(),"nullity",len(B.nullspace()))
for v in B.nullspace():
    L=sp.ilcm(*[sp.denom(x) for x in v]); a=[int(x*L) for x in v]
    g=abs(math.gcd(*a)); a=[x//g for x in a]
    print({names[i]:c for i,c in enumerate(a) if c}, "weight",sum(abs(x) for x in a),
          "exact",B*sp.Matrix(a)==sp.zeros(B.rows,1))
