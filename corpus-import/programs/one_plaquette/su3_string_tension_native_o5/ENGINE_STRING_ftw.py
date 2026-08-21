"""Weight-blocked GF(p) SU(3) torelon engine (gate-grade, exact-by-residue).
Per-link SU(3) singlet projector built INSIDE the weight-zero block (dim ~O(100), not 3^m),
all linear algebra pure int64 mod p. Removes the m=7 (dim-2187) determinant-link wall.
Modes: validate p | phase1 n | phase2 n p [deadline] | finalize n p [L]
"""
import itertools, importlib.util as iu, sys, time, pickle, os
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
spec=iu.spec_from_file_location('T','/tmp/se/ENGINE_STRING_su3_torelon.py'); T=iu.module_from_spec(spec); spec.loader.exec_module(T)
GEN_FOLDED=T.GEN_FOLDED
N=3
def inv(a,p): return pow(int(a)%p,p-2,p)
def _sumTT(x,y,z,w):
    v=F(0)
    if x==w and z==y: v+=F(1,2)
    if x==y and z==w: v-=F(1,6)
    return v
KERr={}
for ei in (1,-1):
  for ej in (1,-1):
    B=[[[[F(0)]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for bi in range(3):
     for bj in range(3):
      for an in range(3):
       for cn in range(3):
         if ei==1: xi,yi,si=an,bi,1
         else: xi,yi,si=bi,an,-1
         if ej==1: xj,yj,sj=cn,bj,1
         else: xj,yj,sj=bj,cn,-1
         B[an][cn][bi][bj]=si*sj*_sumTT(xi,yi,xj,yj)
    KERr[(ei,ej)]=B
def ker_modp(p):
    out={}
    for k,B in KERr.items():
        A=np.zeros((3,3,3,3),dtype=np.int64)
        for a in range(3):
         for c in range(3):
          for b in range(3):
           for d in range(3):
            v=B[a][c][b][d]
            if v: A[a,c,b,d]=(v.numerator*inv(v.denominator,p))%p
        out[k]=A
    return out
def _su3_casimirs():
    s=set()
    for pp in range(8):
        for qq in range(8):
            s.add(F(pp*pp+qq*qq+pp*qq+3*pp+3*qq,3))
    return sorted(s)
KNOWN_C2=_su3_casimirs()
def rref_modp(A,p):
    A=(A%p).copy(); rows,cols=A.shape; r=0; piv=[]
    for c in range(cols):
        if r>=rows: break
        sub=A[r:,c]%p; nz=np.nonzero(sub)[0]
        if nz.size==0: continue
        pr=r+int(nz[0])
        if pr!=r: A[[r,pr]]=A[[pr,r]]
        A[r]=(A[r]*inv(int(A[r,c]),p))%p
        col=A[:,c].copy(); col[r]=0
        if np.any(col%p): A=(A-np.outer(col,A[r]))%p
        piv.append(c); r+=1
    return A,piv,r
def nullspace_modp(A,p):
    R,piv,rank=rref_modp(A,p); n=A.shape[1]; pivset=set(piv); free=[c for c in range(n) if c not in pivset]
    basis=[]
    for fc in free:
        v=np.zeros(n,dtype=np.int64); v[fc]=1
        for ri,pc in enumerate(piv): v[pc]=(-R[ri,fc])%p
        basis.append(v%p)
    return (np.array(basis,dtype=np.int64).T%p) if basis else np.zeros((n,0),dtype=np.int64)
def matinv_modp(A,p):
    n=A.shape[0]; M=np.concatenate([A%p,np.eye(n,dtype=np.int64)],axis=1)
    R,piv,rank=rref_modp(M,p)
    assert rank==n,"singular mod p"
    return R[:,n:]%p
def mm(A,B,p): return (A.astype(np.int64)@B.astype(np.int64))%p
_w0cache={}
def w0_states(eps):
    if eps in _w0cache: return _w0cache[eps]
    m=len(eps); nf=sum(1 for e in eps if e==1); na=m-nf; tgt=(nf-na)//3
    out=[]
    for s in itertools.product(range(N),repeat=m):
        w=[0,0,0]
        for e,c in zip(eps,s): w[c]+=(1 if e==1 else -1)
        if w[0]==tgt and w[1]==tgt and w[2]==tgt: out.append(s)
    res=(out,{s:i for i,s in enumerate(out)})
    _w0cache[eps]=res; return res
def cas_block(eps,S,p,W0,w0idx,c2f,KER):
    d0=len(W0); M=np.zeros((d0,d0),dtype=np.int64)
    S=list(S); diag=(len(S)*c2f)%p
    for i in range(d0): M[i,i]=diag
    for i in S:
        for j in S:
            if i==j: continue
            B=KER[(eps[i],eps[j])]
            for si,s in enumerate(W0):
                bi=s[i]; bj=s[j]
                for an in range(N):
                    row=B[an,:,bi,bj]
                    for cn in range(N):
                        v=int(row[cn])
                        if v==0: continue
                        ns=list(s); ns[i]=an; ns[j]=cn
                        jdx=w0idx[tuple(ns)]
                        M[si,jdx]=(M[si,jdx]+v)%p
    return M
def link_lib_w(eps,cuts,p,KER,cache):
    key=(eps,cuts)
    if key in cache: return cache[key]
    m=len(eps); dim=3**m; c2f=(4*inv(3,p))%p
    W0,w0idx=w0_states(eps); d0=len(W0)
    if d0==0: cache[key]=[]; return []
    Cf=cas_block(eps,range(m),p,W0,w0idx,c2f,KER)
    Bn=nullspace_modp(Cf,p)
    r=Bn.shape[1]
    if r==0: cache[key]=[]; return []
    G=mm(Bn.T,Bn,p)
    try: Gi=matinv_modp(G,p)
    except Exception: cache[key]=None; return None
    L=mm(Gi,Bn.T,p)
    Xs=[mm(L,mm(cas_block(eps,S,p,W0,w0idx,c2f,KER),Bn,p),p) for S in cuts]
    groups=[((),np.eye(r,dtype=np.int64))]
    for X in Xs:
        ng=[]
        for hist,V in groups:
            k=V.shape[1]; GV=mm(V.T,V,p)
            try: GVi=matinv_modp(GV,p)
            except Exception: cache[key]=None; return None
            Y=mm(GVi,mm(V.T,mm(X,V,p),p),p)
            for lam in KNOWN_C2:
                lm=(lam.numerator*inv(lam.denominator,p))%p
                Kk=(Y-lm*np.eye(k,dtype=np.int64))%p
                nsp=nullspace_modp(Kk,p)
                if nsp.shape[1]: ng.append((hist+(lam,),mm(V,nsp,p)))
        groups=ng
    if not groups: cache[key]=None; return None
    out=[]; tot=0
    for hist,V in groups:
        Ub=mm(Bn,V,p)
        Gu=mm(Ub.T,Ub,p)
        try: Giu=matinv_modp(Gu,p)
        except Exception: cache[key]=None; return None
        kk=Ub.shape[1]; Uf=np.zeros((dim,kk),dtype=np.int64)
        for bi,s in enumerate(W0):
            idx=0
            for c in s: idx=idx*3+c
            Uf[idx]=Ub[bi]
        out.append((hist,Uf.reshape((3,)*m+(kk,)),Giu)); tot+=kk
    if tot!=r: cache[key]=None; return None
    cache[key]=out; return out
def contract_modp(tensors,p):
    factors=list(tensors)
    legs=set().union(*[set(l) for _,l in factors]) if factors else set()
    while legs:
        v=min(legs,key=lambda x:sum(1 for _,l in factors if x in l))
        sel=[f for f in factors if v in f[1]]; rest=[f for f in factors if v not in f[1]]
        cur_a,cur_l=sel[0]
        for a2,l2 in sel[1:]:
            ul=list(dict.fromkeys(list(cur_l)+list(l2)))
            sub1=[ul.index(x) for x in cur_l]; sub2=[ul.index(x) for x in l2]
            out=list(range(len(ul)))
            cur_a=np.einsum(cur_a,sub1,a2,sub2,out)%p; cur_l=tuple(ul)
        ax=cur_l.index(v); cur_a=cur_a.sum(axis=ax)%p; cur_l=tuple(x for x in cur_l if x!=v)
        factors=rest+[(cur_a,cur_l)]; legs.discard(v)
    res=1
    for a,l in factors: res=(res*int(a))%p
    return res%p
def amp_modp(specs,n,p,KER,cache):
    per=[]
    for sig,rows,cols in specs:
        ev=[e for e in range(len(sig)) if sig[e]!=0]; eps=tuple(sig[e] for e in ev)
        cs=tuple(tuple(k for k,e in enumerate(ev) if e<=c) for c in range(1,n))
        lib=link_lib_w(eps,cs,p,KER,cache)
        if lib is None: return None
        if not lib: return 0
        g=[k for k,e in enumerate(ev) if e==0]
        per.append((lib,rows,cols,F(4,3)*len(g)))
    E0=sum(p4[3] for p4 in per)/2
    total=0
    allv=sorted({v for (lib,rows,cols,g) in per for v in list(rows)+list(cols)}); nb=len(allv)
    for combo in itertools.product(*[x[0] for x in per]):
        ds=[]
        for ci in range(n-1):
            Eint=sum(hist[ci] for (hist,U,Gi) in combo)/2
            ds.append(E0-Eint)
        w=GEN_FOLDED(ds)
        if w==0: continue
        wm=(w.numerator*inv(w.denominator,p))%p
        tensors=[]; bond=nb
        for (hist,U,Gi),(lib,rows,cols,g) in zip(combo,per):
            rl=tuple(list(rows)+[bond]); cl=tuple(list(cols)+[bond+1])
            tensors.append((U,rl)); tensors.append((U,cl)); tensors.append((Gi,(bond,bond+1)))
            bond+=2
        col=contract_modp(tensors,p)
        total=(total+col*wm)%p
    return total
def canon(specs):
    relab={}
    for sig,rows,cols in specs:
        for v in list(rows)+list(cols):
            if v not in relab: relab[v]=len(relab)
    return tuple((sig,tuple(relab[v] for v in rows),tuple(relab[v] for v in cols)) for sig,rows,cols in specs)
def all_sequences(n,L):
    for S in T.connected_sets(L,n):
        for ins,sg in T.sequences_over_set(S,n):
            yield ins,(1,)+sg+(1,)
def phase1(n,L=4):
    counts=defaultdict(int)
    for ins,signs in all_sequences(n,L):
        for vac,sgn in ((False,1),(True,-1)):
            specs=T.build_specs(L,ins,signs,vac)
            if specs is None: continue
            counts[canon(specs)]+=sgn
    counts={k:v for k,v in counts.items() if v!=0}
    pickle.dump({'n':n,'L':L,'counts':dict(counts)}, open(f'/tmp/se/s{n}_p1.pkl','wb'))
    print(f"phase1 sigma{n}: distinct nonzero topos={len(counts)}")
def phase2(n,p,deadline=38):
    d=pickle.load(open(f'/tmp/se/s{n}_p1.pkl','rb')); counts=d['counts']
    libpk=f'/tmp/se/libw_{p}.pkl'
    cache=pickle.load(open(libpk,'rb')) if os.path.exists(libpk) else {}
    KER=ker_modp(p)
    pf=f'/tmp/se/s{n}_mod_{p}.pkl'
    res=pickle.load(open(pf,'rb')) if os.path.exists(pf) else {}
    t0=time.time(); done=0
    for c in counts:
        if c in res: continue
        a=amp_modp(list(c),n,p,KER,cache)
        res[c]=('BAD' if a is None else int(a)); done+=1
        if time.time()-t0>deadline: break
    pickle.dump(res,open(pf,'wb')); pickle.dump(cache,open(libpk,'wb'))
    bad=sum(1 for v in res.values() if v=='BAD')
    print(f"phase2 sigma{n} p={p}: +{done} this run; {len(res)}/{len(counts)} done; bad={bad}; {time.time()-t0:.1f}s")
KNOWN={2:F(-22,153),3:F(61,408),4:F(-737327120374220449,7250590288602460800),
       5:F(137767222189182735950309,2009803206414863779920000)}
def finalize(n,p,L=4):
    counts=pickle.load(open(f'/tmp/se/s{n}_p1.pkl','rb'))['counts']
    res=pickle.load(open(f'/tmp/se/s{n}_mod_{p}.pkl','rb'))
    miss=sum(c not in res for c in counts)
    assert miss==0, f"missing {miss}"
    if any(res[c]=='BAD' for c in counts): print(f"sigma{n} p={p}: BAD PRIME"); return None
    tot=sum(counts[c]*res[c] for c in counts)%p
    sig=(tot*inv(L,p))%p
    exp=(KNOWN[n].numerator*inv(KNOWN[n].denominator,p))%p
    print(f"sigma{n} mod {p} = {sig}")
    print(f"      expected   {exp}")
    print(f"      MATCH={sig==exp}")
    return sig
def validate(p):
    KER=ker_modp(p); cache={}
    for n in (2,3,4):
        t=time.time(); tot=0
        for ins,signs in all_sequences(n,4):
            for vac,sgn in ((False,1),(True,-1)):
                specs=T.build_specs(4,ins,signs,vac)
                if specs is None: continue
                a=amp_modp(specs,n,p,KER,cache)
                assert a is not None, f"BAD prime at sigma{n}"
                tot=(tot+sgn*a)%p
        sig=(tot*inv(4,p))%p; exp=(KNOWN[n].numerator*inv(KNOWN[n].denominator,p))%p
        print(f"sigma{n} mod {p} = {sig}  expected {exp}  MATCH={sig==exp}  [{time.time()-t:.1f}s]")
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='validate':
        p=int(sys.argv[2]); assert all(p%d for d in range(2,int(p**0.5)+1)),'not prime'; validate(p)
    elif mode=='phase1': phase1(int(sys.argv[2]))
    elif mode=='phase2':
        n=int(sys.argv[2]); p=int(sys.argv[3]); dl=float(sys.argv[4]) if len(sys.argv)>4 else 38
        assert all(p%d for d in range(2,int(p**0.5)+1)),'not prime'; phase2(n,p,dl)
    elif mode=='finalize': finalize(int(sys.argv[2]),int(sys.argv[3]))
