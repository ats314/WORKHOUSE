#!/usr/bin/env python3
"""Exact finite support-class checks for SU(3) torelon perturbation theory."""
from __future__ import annotations
import gzip,itertools,json,pathlib,time
from collections import Counter
import numpy as np
E=((1,0,0),(0,1,0),(0,0,1))
def gate(name,c,detail=''):
 print(('PASS' if c else 'FAIL'),name,detail)
 if not c:raise RuntimeError(f'{name}: {detail}')
def find(name):
 release=pathlib.Path(__file__).resolve().parents[1]
 for p in (release/'inputs'/name, release/name, pathlib.Path.cwd()/name, pathlib.Path.cwd()/'inputs'/name):
  if p.exists(): return p
 return None
def add(a,b):return tuple(a[i]+b[i] for i in range(3))
def pedges(p):
 x=tuple(p[:3]);a,b=p[3:];xa=add(x,E[a]);xb=add(x,E[b])
 return [((*x,a),1),((*xa,b),1),((*xb,a),-1),((*x,b),-1)]
def site_neighbors(p):
 x=tuple(p[:3]);a,b=p[3:];verts=[x,add(x,E[a]),add(add(x,E[a]),E[b]),add(x,E[b])]
 out=set()
 for v in verts:
  for u,w in ((0,1),(0,2),(1,2)):
   for iu in (0,1):
    for iw in (0,1):
     q=list(v);q[u]-=iu;q[w]-=iw;out.add((*q,u,w))
 return out
def charges(support,signs):
 c=Counter()
 for p,s in zip(support,signs):
  for l,v in pedges(p):c[l]+=s*v
 return {l:v for l,v in c.items() if v}
def scan_order3():
 root=(0,0,0,0,1);plaquettes=site_neighbors(root)
 # Every connected rooted multiset of three plaquettes can be grown in two site-adjacent steps.
 multisets=set()
 for q in plaquettes:
  for r in site_neighbors(root)|site_neighbors(q):
   multisets.add(tuple(sorted((root,q,r))))
 survivors=[]
 for support in sorted(multisets):
  for signs in itertools.product((-1,1),repeat=3):
   c=charges(support,signs)
   if all(v%3==0 for v in c.values()):survivors.append((support,signs,c))
 gate('O(y^3) rooted connected census nonempty',bool(multisets),str(len(multisets)))
 gate('O(y^3) only coincident supports',all(len(set(s))==1 for s,_,_ in survivors),str(len(survivors)))
 gate('O(y^3) only equal orientations',all(len(set(sg))==1 for _,sg,_ in survivors))
 gate('O(y^3) two charge-conjugate survivors',len(survivors)==2,str(survivors))
 return {'rooted_connected_multisets':len(multisets),'survivors':len(survivors),
         'representatives':[{'support':[list(p) for p in s],'signs':list(sg)} for s,sg,_ in survivors]}
def scan_order4():
 path=find('y4_connected_supports.json.gz')
 if path is None:raise FileNotFoundError('Missing y4_connected_supports.json.gz')
 supports=json.load(gzip.open(path,'rt'))['supports'];S=np.array(list(itertools.product((-1,1),repeat=4)),dtype=np.int8)
 counts=Counter();t=time.time()
 for sup in supports:
  links={};rows=[]
  for p in sup:
   e=pedges(p)
   for l,_ in e:
    if l not in links:links[l]=len(links)
   rows.append(e)
  A=np.zeros((4,len(links)),dtype=np.int8)
  for i,e in enumerate(rows):
   for l,v in e:A[i,links[l]]+=v
  C=S@A;tri=np.all(C%3==0,axis=1);exact=np.all(C==0,axis=1)
  counts['triality_assignments']+=int(tri.sum());counts['exact_assignments']+=int(exact.sum())
  counts['triality_only_assignments']+=int((tri&~exact).sum())
  for idx in np.flatnonzero(tri):
   mult=Counter(tuple(p) for p in sup);paired=sorted(mult.values()) in ([4],[2,2])
   signs=S[idx]
   sign_bal=all(sum(int(signs[i]) for i,p in enumerate(sup) if tuple(p)==q)==0 for q in mult)
   counts['paired_support_triality']+=int(paired);counts['sign_balanced_triality']+=int(sign_bal)
 gate('O(y^4) primitive support count',len(supports)==182440,str(len(supports)))
 gate('O(y^4) no triality-only assignments',counts['triality_only_assignments']==0,str(counts))
 gate('O(y^4) all survivors are paired supports',counts['paired_support_triality']==counts['triality_assignments'],str(counts))
 gate('O(y^4) all survivors sign-balanced by geometry',counts['sign_balanced_triality']==counts['triality_assignments'],str(counts))
 gate('O(y^4) exact survivor count',counts['triality_assignments']==636,str(counts))
 return {'primitive_supports':len(supports),**dict(counts),'walltime_seconds':time.time()-t}
def run():
 return {'order3':scan_order3(),'order4':scan_order4()}
if __name__=='__main__':
 import sys
 payload=run();text=json.dumps(payload,indent=2,sort_keys=True)
 if len(sys.argv)>1:pathlib.Path(sys.argv[1]).write_text(text)
 print(text)
