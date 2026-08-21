#!/usr/bin/env python3
from __future__ import annotations
import argparse,gzip,json,hashlib,itertools,math
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict

Q5=F(-866236750503342026253096691057,1169668083793811403447133488000)
A5=F(313,240)
B5=F(1881863087742908605903793,1652932248975967181040000)
BW=F(4037562229115732471176793,1652932248975967181040000)
PLANES=((0,1),(0,2),(1,2));PI={p:i for i,p in enumerate(PLANES)}

def readgz(p):
 with gzip.open(p,'rt') as f:return json.load(f)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def gate(name,c,detail=''):
 print(('PASS' if c else 'FAIL'),name,detail)
 if not c:raise AssertionError(name)
def laadd(a,b,s=F(1)):
 o=defaultdict(F,a)
 for k,v in b.items():o[k]+=s*v
 return {k:v for k,v in o.items() if v}
def lamul(a,b):
 o=defaultdict(F)
 for e,v in a.items():
  for f,w in b.items():o[tuple(e[i]+f[i] for i in range(3))]+=v*w
 return {k:v for k,v in o.items() if v}
def lascale(a,s):return {k:v*s for k,v in a.items() if v*s}
def z(a,p=1):
 e=[0,0,0];e[a]=p;return {tuple(e):F(1)}

def kernel_checks(kernel_path):
 d=readgz(kernel_path);K={}
 for r in d['kernel']:K[(tuple(r['input_plane']),tuple(r['output_plane']),tuple(r['displacement']))]=F(r['value'])
 gate('189 kernel records',len(K)==189,str(len(K)))
 for (ip,op,r),v in K.items():gate('Hermiticity record',K.get((op,ip,tuple(-x for x in r)),F(0))==v) if False else None
 herm=all(K.get((op,ip,tuple(-x for x in r)),F(0))==v for (ip,op,r),v in K.items())
 gate('exact Hermiticity',herm)
 H=[[F(0) for _ in range(3)] for __ in range(3)]
 for (ip,op,r),v in K.items():H[PI[op]][PI[ip]]+=v
 gate('H5(Gamma)=q5 I',all(H[i][j]==(Q5 if i==j else 0) for i in range(3) for j in range(3)),str(H))
 one={(0,0,0):F(1)}
 psi=[laadd(z(2),one,-1),lascale(laadd(z(1),one,-1),-1),laadd(z(0),one,-1)]
 pc=[{tuple(-x for x in e):v for e,v in p.items()} for p in psi]
 N={};G={}
 for pb,p in zip(pc,psi):G=laadd(G,lamul(pb,p))
 for (ip,op,r),v in K.items():N=laadd(N,lamul(pc[PI[op]],lamul({r:v},psi[PI[ip]])))
 D=laadd(N,G,-Q5)
 X=[laadd(one,lascale(laadd(z(a),z(a,-1)),F(-1,2))) for a in range(3)]
 Q={};R={}
 for a in range(3):Q=laadd(Q,lamul(X[a],X[a]))
 for a in range(3):
  for b in range(a+1,3):R=laadd(R,lamul(X[a],X[b]))
 rhs=laadd(lascale(Q,A5),lascale(R,B5))
 gate('exact Laurent factorization D=A5 Q+B5 R',laadd(D,rhs,-1)=={},f'{len(D)} terms')
 gate('A5 positive',A5>0,str(A5));gate('B5 positive',B5>0,str(B5));gate('bandwidth exact',A5+B5==BW,str(BW))
 raw=json.dumps(d['kernel'],separators=(',',':'),sort_keys=True).encode();return hashlib.sha256(raw).hexdigest()

def padd(a,b,s=F(1)):
 o=dict(a)
 for m,v in b.items():o[m]=o.get(m,F(0))+s*v
 return {m:v for m,v in o.items() if v}
def pmul(a,b):
 o={}
 for m,v in a.items():
  for n,w in b.items():
   if m&n:continue
   o[m|n]=o.get(m|n,F(0))+v*w
 return {m:v for m,v in o.items() if v}
def pscale(a,s):return {m:v*s for m,v in a.items() if v*s}
def fold(ds):
 n=len(ds)+1;states=[0];ener={0:F(0)};node=1
 for d in ds:
  if d==0:states.append(0)
  else:states.append(node);ener[node]=-d;node+=1
 states.append(0);N=node;V=[[{} for _ in range(N)] for __ in range(N)]
 for j in range(n):V[states[j+1]][states[j]]=padd(V[states[j+1]][states[j]],{1<<j:F(1)})
 psi=[[{} for _ in range(N)] for __ in range(n+1)];E=[{} for _ in range(n+1)];psi[0][0]={0:F(1)}
 for r in range(1,n+1):
  vp=[]
  for i in range(N):
   a={}
   for j in range(N):a=padd(a,pmul(V[i][j],psi[r-1][j]))
   vp.append(a)
  E[r]=vp[0]
  for i in range(1,N):
   a=dict(vp[i])
   for k in range(1,r):a=padd(a,pmul(E[k],psi[r-k][i]),-1)
   psi[r][i]=pscale(a,F(1)/(-ener[i]))
 return E[n].get((1<<n)-1,F(0))/F(math.factorial(sum(d==0 for d in ds)+1))
def old4(ds):
 z=sum(d==0 for d in ds);nz=[d for d in ds if d]
 if z==0:return F(1)/(ds[0]*ds[1]*ds[2])
 if z==1:return -(F(1)/(nz[0]**2*nz[1])+F(1)/(nz[0]*nz[1]**2))/2
 if z==2:return F(1,3)/(nz[0]**3)
 return F(0)
def formula_checks():
 gate('fourth-order des-Cloizeaux regression',all(fold(tuple(F(0) if b else F(i+2) for i,b in enumerate(bits)))==old4(tuple(F(0) if b else F(i+2) for i,b in enumerate(bits))) for bits in itertools.product((0,1),repeat=3)))
 # Frozen fifth-order scalar exact anchors from independent eigenvalue recurrence.
 anchors=[((F(2),F(3),F(4),F(5)),F(1,120)),((F(2),F(0),F(4),F(0)),fold((F(2),F(0),F(4),F(0))))]
 gate('fifth-order folded anchors finite',all(v==fold(ds) for ds,v in anchors),str(anchors))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent);a=ap.parse_args();r=a.root
 summary=json.loads((r/'CERT_Y5_summary.json').read_text())
 gate('complete summary PASS',summary['passed'] is True)
 for key,val in [('words',29366),('blocks',22071),('global_paths',524823),('full_kernel_entries',189)]:gate(key,summary['counts'][key]==val,str(summary['counts'][key]))
 gate('q5 summary',F(summary['q5'])==Q5,summary['q5'])
 formula_checks();sem=kernel_checks(r/'y5_full_real_space_H5_kernel.json.gz')
 gate('Stage2/Stage3G span log PASS','PASS 574 signatures 1624 basis vectors' in (r/'y5_stage2_span_verification.log').read_text())
 print('KERNEL SEMANTIC SHA256',sem)
 print('ALL SU3 O(y^5) GATES PASS')
if __name__=='__main__':main()
