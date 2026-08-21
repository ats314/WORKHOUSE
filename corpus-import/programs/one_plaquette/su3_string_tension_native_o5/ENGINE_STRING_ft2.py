"""Fast resumable SU(3) torelon engine: numpy Casimir + low-rank link tensors + exact folded weights.
Modes: validate | phase1 N | phase2 N | finalize N"""
import itertools, importlib.util, sys, time, pickle, os
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
spec=importlib.util.spec_from_file_location('T','/tmp/su3eng/ENGINE_STRING_su3_torelon.py'); T=importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
GEN_FOLDED=T.GEN_FOLDED
N=3; C2F=F(4,3)
# ---- 2-body kernels B[an,cn,bi,bj] for (ei,ej) ----
def _sumTT(x,y,z,w):
    v=0.0
    if x==w and z==y: v+=0.5
    if x==y and z==w: v-=1.0/6
    return v
def kernel(ei,ej):
    B=np.zeros((3,3,3,3))
    for bi in range(3):
     for bj in range(3):
      for an in range(3):
       for cn in range(3):
        if ei==1: xi,yi,si=an,bi,1
        else: xi,yi,si=bi,an,-1
        if ej==1: xj,yj,sj=cn,bj,1
        else: xj,yj,sj=bj,cn,-1
        B[an,cn,bi,bj]=si*sj*_sumTT(xi,yi,xj,yj)
    return B
KER={(a,b):kernel(a,b) for a in(1,-1) for b in(1,-1)}
_lib={}
KNOWN_C2=[F(0),F(4,3),F(3),F(10,3),F(6),F(16,3),F(28,3),F(25,3),F(40,3),F(9),F(12),F(46,3),F(7),F(64,3),F(22,3),F(34,3),F(2,1),F(20,3),F(43,3),F(52,3)]
def near(x):
    return min(KNOWN_C2,key=lambda q:abs(float(q)-x))
def _applyC(eps,S,X):
    # X shape (3,)*m + (r,); return C2(S) @ X (same shape)
    m=len(eps); S=list(S)
    out=len(S)*float(C2F)*X
    src=list(range(m)); rax=m  # X axes: 0..m-1 factors, m = vector index
    for i in S:
        for j in S:
            if i==j: continue
            B=KER[(eps[i],eps[j])]; LA=m+1; LB=m+2
            subX=list(range(m))+[rax]
            subB=[LA,LB,i,j]
            o=[(LA if a==i else LB if a==j else a) for a in range(m)]+[rax]
            out=out+np.einsum(X,subX,B,subB,o)
    return out
def casimir_full(eps):
    m=len(eps); dim=3**m
    I=np.eye(dim).reshape((3,)*m+(dim,))
    return _applyC(eps,range(m),I).reshape(dim,dim) if False else None
import pickle as _pk, os as _os
_LIBPK='/tmp/su3eng/libcache.pkl'
def _load_libpk():
    global _lib
    if _os.path.exists(_LIBPK):
        try: _lib.update(_pk.load(open(_LIBPK,'rb')))
        except: pass
def _save_libpk():
    _pk.dump(_lib, open(_LIBPK,'wb'))
def link_lib(eps,cuts):
    key=(eps,cuts)
    if key in _lib: return _lib[key]
    m=len(eps); dim=3**m
    # full casimir matrix via action on identity (once)
    I=np.eye(dim).reshape((3,)*m+(dim,))
    Cf=_applyC(eps,range(m),I).reshape(dim,dim)
    u,sv,vt=np.linalg.svd(Cf); tol=1e-7*max(1.0,sv.max())
    Bn=vt[sv<tol].T
    r=Bn.shape[1]
    if r==0: _lib[key]=[]; return []
    Bt=Bn.reshape((3,)*m+(r,))
    smalls=[]
    for S in cuts:
        CS=_applyC(eps,S,Bt).reshape(dim,r)
        smalls.append(Bn.T@CS)
    comb=sum((p+1.7)*(2.0+0.3*p)*Sm for p,Sm in enumerate(smalls)) if smalls else np.zeros((r,r))
    w,V=np.linalg.eigh((comb+comb.T)/2) if smalls else (np.zeros(r),np.eye(r))
    groups=defaultdict(list)
    for i in range(r):
        vec=Bn@V[:,i]
        hist=tuple(near(float(vec@_full_apply(eps,S,vec)/(vec@vec))) for S in cuts)
        groups[hist].append(vec)
    out=[]
    for hist,vecs in groups.items():
        U=np.array(vecs).T; Q,_=np.linalg.qr(U)
        out.append((hist,Q.reshape((3,)*m+(Q.shape[1],))))
    _lib[key]=out; return out
def _full_apply(eps,S,vec):
    m=len(eps); dim=3**m
    return _applyC(eps,S,vec.reshape((3,)*m+(1,))).reshape(dim)

def canon(specs):
    relab={}
    for sig,rows,cols in specs:
        for v in list(rows)+list(cols):
            if v not in relab: relab[v]=len(relab)
    return tuple((sig,tuple(relab[v] for v in rows),tuple(relab[v] for v in cols)) for sig,rows,cols in specs)

_AMPMEMO={}
def amp_from_specs(specs,n):
    ck=(n,canon(specs))
    if ck in _AMPMEMO: return _AMPMEMO[ck]
    per=[]
    for sig,rows,cols in specs:
        ev=[e for e in range(len(sig)) if sig[e]!=0]; eps=tuple(sig[e] for e in ev)
        cs=tuple(tuple(k for k,e in enumerate(ev) if e<=c) for c in range(1,n))
        lib=link_lib(eps,cs)
        if not lib: return 0.0
        g=[k for k,e in enumerate(ev) if e==0]
        per.append((lib,rows,cols,C2F*len(g)))
    allvars=sorted({v for (lib,rows,cols,g) in per for v in list(rows)+list(cols)})
    vlab={v:i for i,v in enumerate(allvars)}; nb=len(allvars)
    E0=sum(p[3] for p in per)/2
    total=0.0
    for combo in itertools.product(*[p[0] for p in per]):
        ds=[]
        for ci in range(n-1):
            Eint=sum(hist[ci] for (hist,Q) in combo)/2
            ds.append(E0-Eint)
        w=GEN_FOLDED(ds)
        if w==0: continue
        ops=[]; bond=nb
        for (hist,Q),(lib,rows,cols,g) in zip(combo,per):
            rlab=[vlab[v] for v in rows]+[bond]
            clab=[vlab[v] for v in cols]+[bond]
            ops+= [Q,rlab,Q,clab]; bond+=1
        val=float(np.einsum(*ops,[],optimize=True))
        total+=val*float(w)
    _AMPMEMO[ck]=total
    return total

def all_sequences(n,L):
    for S in T.connected_sets(L,n):
        for ins,sg in T.sequences_over_set(S,n):
            yield ins,(1,)+sg+(1,)

def phase1(n,L=4):
    counts=defaultdict(int); reps={}
    for ins,signs in all_sequences(n,L):
        for vac,sgn in ((False,1),(True,-1)):
            specs=T.build_specs(L,ins,signs,vac)
            if specs is None: continue
            c=canon(specs); counts[c]+=sgn
            if c not in reps: reps[c]=c
    counts={k:v for k,v in counts.items() if v!=0}
    pickle.dump({'n':n,'L':L,'counts':dict(counts)}, open(f'/tmp/su3eng/s{n}_p1.pkl','wb'))
    print(f"phase1 sigma{n}: distinct nonzero topos={len(counts)}")

def phase2(n,deadline=40):
    _load_libpk()
    d=pickle.load(open(f'/tmp/su3eng/s{n}_p1.pkl','rb')); counts=d['counts']
    pf=f'/tmp/su3eng/s{n}_p2.pkl'
    res=pickle.load(open(pf,'rb')) if os.path.exists(pf) else {}
    t0=time.time(); done=0
    for c in counts:
        if c in res: continue
        res[c]=amp_from_specs(list(c),n); done+=1
        if time.time()-t0>deadline:
            break
    pickle.dump(res,open(pf,'wb')); _save_libpk()
    print(f"phase2 sigma{n}: computed {done} this run; total {len(res)}/{len(counts)}; {time.time()-t0:.1f}s")

def finalize(n,L=4):
    d=pickle.load(open(f'/tmp/su3eng/s{n}_p1.pkl','rb')); counts=d['counts']
    res=pickle.load(open(f'/tmp/su3eng/s{n}_p2.pkl','rb'))
    assert all(c in res for c in counts), f"missing {sum(c not in res for c in counts)}"
    tot=sum(counts[c]*res[c] for c in counts)
    sig=tot/L
    print(f"sigma{n}_reduced(float) = {sig:.15g}")
    return sig

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='validate':
        known={2:-22/153,3:61/408,4:-737327120374220449/7250590288602460800}
        for n in (2,3,4):
            t=time.time()
            tot=0.0
            for ins,signs in all_sequences(n,4):
                for vac,sgn in ((False,1),(True,-1)):
                    specs=T.build_specs(4,ins,signs,vac)
                    if specs is None: continue
                    tot+=sgn*amp_from_specs(specs,n)
            sig=tot/4; print(f"sigma{n}={sig:.14g} known={known[n]:.14g} d={abs(sig-known[n]):.1e} [{time.time()-t:.1f}s]")
    elif mode=='phase1': phase1(int(sys.argv[2]))
    elif mode=='phase2': phase2(int(sys.argv[2]), float(sys.argv[3]) if len(sys.argv)>3 else 40)
    elif mode=='finalize': finalize(int(sys.argv[2]))
