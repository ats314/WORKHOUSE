"""Gate-grade modular (GF(p)) SU(3) torelon engine: exact-by-residue color amplitudes.
Same fusion-tree algorithm as ft2 but over GF(p); compares sigma_n mod p to known/KPS rationals."""
import itertools, importlib.util, sys, time, pickle, os
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
spec=importlib.util.spec_from_file_location('T','/tmp/su3eng/ENGINE_STRING_su3_torelon.py'); T=importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
GEN_FOLDED=T.GEN_FOLDED
N=3
def inv(a,p): return pow(int(a)%p,p-2,p)
# rational 2-body kernels (exact), reduced mod p on demand
def _sumTT(x,y,z,w):
    v=F(0)
    if x==w and z==y: v+=F(1,2)
    if x==y and z==w: v-=F(1,6)
    return v
KERr={}
for ei in(1,-1):
 for ej in(1,-1):
  Bk=[[[[F(0)]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
  for bi in range(3):
   for bj in range(3):
    for an in range(3):
     for cn in range(3):
       if ei==1: xi,yi,si=an,bi,1
       else: xi,yi,si=bi,an,-1
       if ej==1: xj,yj,sj=cn,bj,1
       else: xj,yj,sj=bj,cn,-1
       Bk[an][cn][bi][bj]=si*sj*_sumTT(xi,yi,xj,yj)
  KERr[(ei,ej)]=Bk
def ker_modp(p):
    out={}
    for k,Bk in KERr.items():
        A=np.zeros((3,3,3,3),dtype=np.int64)
        for a in range(3):
         for c in range(3):
          for b in range(3):
           for d in range(3):
            v=Bk[a][c][b][d]
            if v: A[a,c,b,d]=(v.numerator*inv(v.denominator,p))%p
        out[k]=A
    return out
def cas_modp(eps,S,p,KP):
    m=len(eps); dim=3**m
    I=np.eye(dim,dtype=np.int64).reshape((3,)*m+(dim,))
    c2f=(4*inv(3,p))%p
    M=(len(list(S))*c2f % p)*I % p
    for i in S:
        for j in S:
            if i==j: continue
            B=KP[(eps[i],eps[j])]; rax=m; LA=m+1; LB=m+2
            subI=list(range(m))+[rax]
            subB=[LA,LB,i,j]
            o=[(LA if a==i else LB if a==j else a) for a in range(m)]+[rax]
            M=(M+np.einsum(I,subI,B,subB,o))%p
    return M.reshape(dim,dim)%p
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
    # right null space basis (columns), A: n x n
    R,piv,rank=rref_modp(A,p); n=A.shape[1]; pivset=set(piv); free=[c for c in range(n) if c not in pivset]
    basis=[]
    for fc in free:
        v=np.zeros(n,dtype=np.int64); v[fc]=1
        for ri,pc in enumerate(piv): v[pc]=(-R[ri,fc])%p
        basis.append(v%p)
    return (np.array(basis).T%p) if basis else np.zeros((n,0),dtype=np.int64)
def matinv_modp(A,p):
    n=A.shape[0]; M=np.concatenate([A%p,np.eye(n,dtype=np.int64)],axis=1)
    R,piv,rank=rref_modp(M,p)
    assert rank==n, "singular mod p"
    return R[:,n:]%p
KNOWN_C2=[F(0),F(4,3),F(3),F(10,3),F(6),F(16,3),F(28,3),F(25,3),F(40,3),F(9),F(12),F(46,3),F(7),F(64,3),F(22,3),F(34,3),F(2,1),F(20,3),F(43,3),F(52,3)]
def link_lib_modp(eps,cuts,p,KP,cache):
    key=(eps,cuts)
    if key in cache: return cache[key]
    m=len(eps); dim=3**m
    Cf=cas_modp(eps,range(m),p,KP)
    Bn=nullspace_modp(Cf,p).astype(object)%p   # dim x r (exact ints)
    r=Bn.shape[1]
    if r==0: cache[key]=[]; return []
    def mmo(A,B): return (A@B)%p
    G=mmo(Bn.T,Bn)
    try: Gi=matinv_modp(G,p).astype(object)%p
    except Exception: cache[key]=None; return None
    L=mmo(Gi,Bn.T)
    Xs=[mmo(L,mmo(cas_modp(eps,S,p,KP).astype(object)%p,Bn)) for S in cuts]
    groups=[((),np.eye(r,dtype=object))]
    for X in Xs:
        ng=[]
        for hist,V in groups:
            k=V.shape[1]; GV=mmo(V.T,V)
            try: GVi=matinv_modp(GV,p).astype(object)%p
            except Exception: cache[key]=None; return None
            Y=mmo(GVi,mmo(V.T,mmo(X,V)))
            for lam in KNOWN_C2:
                lm=(lam.numerator*inv(lam.denominator,p))%p
                Kmat=(Y-lm*np.eye(k,dtype=object))%p
                ns=nullspace_modp(Kmat,p)
                if ns.shape[1]: ng.append((hist+(lam,),mmo(V,ns.astype(object)%p)))
        groups=ng
    if not groups: cache[key]=None; return None   # incomplete split => bad prime
    out=[]; tot=0
    for hist,V in groups:
        U=mmo(Bn,V)   # dim x kk (object)
        Gu=mmo(U.T,U)
        try: Giu=matinv_modp(Gu,p)
        except Exception: cache[key]=None; return None
        out.append((hist,U.astype(np.int64).reshape((3,)*m+(U.shape[1],)),Giu.astype(np.int64))); tot+=U.shape[1]
    if tot!=r: cache[key]=None; return None
    cache[key]=out; return out

def contract_modp(tensors,p):
    # tensors: list of (np.int64 array, tuple legs). eliminate one leg at a time.
    factors=list(tensors)
    legs=set().union(*[set(l) for _,l in factors]) if factors else set()
    while legs:
        v=min(legs,key=lambda x:sum(1 for _,l in factors if x in l))
        sel=[f for f in factors if v in f[1]]; rest=[f for f in factors if v not in f[1]]
        # multiply all sel over union legs
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
def amp_modp(specs,n,p,KP,cache):
    per=[]
    for sig,rows,cols in specs:
        ev=[e for e in range(len(sig)) if sig[e]!=0]; eps=tuple(sig[e] for e in ev)
        cs=tuple(tuple(k for k,e in enumerate(ev) if e<=c) for c in range(1,n))
        lib=link_lib_modp(eps,cs,p,KP,cache)
        if lib is None: return None
        if not lib: return 0
        g=[k for k,e in enumerate(ev) if e==0]
        per.append((lib,rows,cols,F(4,3)*len(g)))
    allv=sorted({v for (lib,rows,cols,g) in per for v in list(rows)+list(cols)})
    nb=len(allv)
    E0=sum(p4[3] for p4 in per)/2
    total=0
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
def sigma_modp(n,p,Ls=(4,)):
    KP=ker_modp(p); cache={}
    rows={}
    for L in Ls:
        tot=0
        import importlib.util as iu
        for ins,signs in T_all(n,L):
            for vac,sgn in ((False,1),(True,-1)):
                sp=T.build_specs(L,ins,signs,vac)
                if sp is None: continue
                a=amp_modp(sp,n,p,KP,cache)
                if a is None: return None
                tot=(tot+sgn*a)%p
        rows[L]=(tot*inv(L,p))%p
    return rows[Ls[0]]
def T_all(n,L):
    for S in T.connected_sets(L,n):
        for ins,sg in T.sequences_over_set(S,n):
            yield ins,(1,)+sg+(1,)

def phase2_modp(n,p,deadline=35):
    counts=pickle.load(open(f'/tmp/su3eng/s{n}_p1.pkl','rb'))['counts']
    libpk=f'/tmp/su3eng/libmod_{p}.pkl'
    cache=pickle.load(open(libpk,'rb')) if os.path.exists(libpk) else {}
    KP=ker_modp(p)
    pf=f'/tmp/su3eng/s{n}_mod_{p}.pkl'
    res=pickle.load(open(pf,'rb')) if os.path.exists(pf) else {}
    t0=time.time(); done=0
    for c in counts:
        if c in res: continue
        a=amp_modp(list(c),n,p,KP,cache)
        res[c]=('BAD' if a is None else int(a)); done+=1
        if time.time()-t0>deadline: break
    pickle.dump(res,open(pf,'wb')); pickle.dump(cache,open(libpk,'wb'))
    bad=sum(1 for v in res.values() if v=='BAD')
    print(f"phase2_modp sigma{n} p={p}: +{done} this run; {len(res)}/{len(counts)} done; bad={bad}; {time.time()-t0:.1f}s")
def finalize_modp(n,p,L=4):
    counts=pickle.load(open(f'/tmp/su3eng/s{n}_p1.pkl','rb'))['counts']
    res=pickle.load(open(f'/tmp/su3eng/s{n}_mod_{p}.pkl','rb'))
    assert all(c in res for c in counts), f"missing {sum(c not in res for c in counts)}"
    if any(res[c]=='BAD' for c in counts): print(f"sigma{n} p={p}: BAD PRIME"); return None
    tot=sum(counts[c]*res[c] for c in counts)%p
    sig=(tot*inv(L,p))%p
    known={2:F(-22,153),3:F(61,408),4:F(-737327120374220449,7250590288602460800),5:F(137767222189182735950309,2009803206414863779920000)}
    exp=(known[n].numerator*inv(known[n].denominator,p))%p
    print(f"sigma{n} mod {p} = {sig}  expected {exp}  MATCH={sig==exp}")
    return sig==exp

if __name__=='__main__':
    P=33554467  # ~2^25 (keep dim*p^2 < 2^63); will assert primality
    n=int(sys.argv[1]); p=int(sys.argv[2]) if len(sys.argv)>2 else P
    assert all(p%d for d in range(2,int(p**0.5)+1)), 'not prime'
    known={2:F(-22,153),3:F(61,408),4:F(-737327120374220449,7250590288602460800),5:F(137767222189182735950309,2009803206414863779920000)}
    mode=sys.argv[3] if len(sys.argv)>3 else 'direct'
    if mode=='p2': phase2_modp(n,p)
    elif mode=='fin': finalize_modp(n,p)
    else:
        t=time.time(); r=sigma_modp(n,p)
        if r is None: print(f"sigma{n} mod {p}: BAD PRIME"); sys.exit()
        exp=(known[n].numerator*inv(known[n].denominator,p))%p
        print(f"sigma{n} mod {p} = {r}  expected {exp}  MATCH={r==exp}  [{time.time()-t:.1f}s]")
