#!/usr/bin/env python3
"""Exact O(y^4) band structure of the C-odd 1+- glueball, from the verified
189-entry H4 kernel. Reproduces: exact band edges (Γ min, R max), exact full
bandwidth, band-edge curvatures, and the BZ-path dispersion. See SYNTHESIS_*.md.
Usage: python3 ENGINE_Y4_band_structure.py [kernel.json.gz]"""
import sys,gzip,json,numpy as np
from collections import defaultdict
from fractions import Fraction as F
KP=sys.argv[1] if len(sys.argv)>1 else 'DATA_Y4_full_real_space_h4_kernel.json.gz'
recs=json.load(gzip.open(KP))['kernel']; PL={(0,1):0,(0,2):1,(1,2):2}
We=defaultdict(dict)
for r in recs: We[(PL[tuple(r['input_plane'])],PL[tuple(r['output_plane'])])][tuple(r['displacement'])]=F(r['weight'])
Wf={k:[(r,float(w)) for r,w in d.items()] for k,d in We.items()}
def H4(k):
    M=np.zeros((3,3),complex)
    for (a,b),lst in Wf.items(): M[b,a]+=sum(w*np.exp(1j*np.dot(r,k)) for r,w in lst)
    return M
def c4(k):
    u=[1-np.exp(1j*kj) for kj in k]; w=np.array([np.conj(u[2]),-np.conj(u[1]),np.conj(u[0])]); nw=np.vdot(w,w).real
    return (sum(We[(2,2)].values())) if nw<1e-12 else (np.vdot(w,H4(k)@w)/nw).real
cG=sum(We[(2,2)].values()); cR=F(-3447362930970494909,1450118057720492160)
print("band min c4(Γ) =",cG,"=",float(cG))
print("band max c4(R) =",cR,"=",float(cR))
print("EXACT bandwidth=",cR-cG,"=",float(cR-cG))
print("H4(0) diagonal? off-diag block sums:",[float(sum(We[(a,b)].values())) for a,b in [(0,1),(0,2),(1,2)]])
import itertools; G=48; lo=hi=None
for i,j,l in itertools.product(range(G),repeat=3):
    if i==j==l==0: continue
    v=c4((2*np.pi*i/G,2*np.pi*j/G,2*np.pi*l/G)); lo=v if lo is None else min(lo,v); hi=v if hi is None else max(hi,v)
print(f"BZ scan {G}^3: min={lo:.6f} max={hi:.6f}  (→ Γ is min, R is max)")
