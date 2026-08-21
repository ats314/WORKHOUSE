"""SU(3) explicit-tensor primitives: subset Casimir, singlet fusion-tree basis, single-link Haar integral."""
from fractions import Fraction as F
import itertools, sympy as sp

N=3
# Fierz: sum_a (Ta)_{xy}(Ta)_{zw} = 1/2 dxw dzy - 1/6 dxy dzw
def _sumTT(x,y,z,w):
    v=F(0)
    if x==w and z==y: v+=F(1,2)
    if x==y and z==w: v-=F(1,6)
    return v
C2_fund=F(4,3)

def casimir_subset(eps, S):
    """C2 over legs in S (set of indices into eps), as full-space matrix dict on 3^m. eps: tuple of +/-1."""
    m=len(eps); states=list(itertools.product(range(N),repeat=m)); sidx={s:k for k,s in enumerate(states)}
    M={}
    S=sorted(S)
    # diagonal: sum_{i in S} C2_fund
    for k in range(len(states)): M[(k,k)]=M.get((k,k),F(0))+len(S)*C2_fund
    # cross i!=j in S
    for i in S:
        for j in S:
            if i==j: continue
            ei,ej=eps[i],eps[j]
            for s in states:
                row=sidx[s]; bi=s[i]; bj=s[j]
                for an in range(N):
                    for cn in range(N):
                        if ei==1: xi,yi,si=an,bi,1
                        else:     xi,yi,si=bi,an,-1
                        if ej==1: xj,yj,sj=cn,bj,1
                        else:     xj,yj,sj=bj,cn,-1
                        val=_sumTT(xi,yi,xj,yj)
                        if not val: continue
                        val*=si*sj
                        ns=list(s); ns[i]=an; ns[j]=cn; col=sidx[tuple(ns)]
                        M[(row,col)]=M.get((row,col),F(0))+val
    return M,states,sidx

def _mat(Md,dim): 
    A=sp.zeros(dim,dim)
    for (r,c),v in Md.items(): A[r,c]=sp.Rational(v.numerator,v.denominator)
    return A

def fusion_basis(eps, cut_subsets):
    """Return list of (history, vec) : orthonormal basis of overall singlet subspace,
       simultaneous eigvecs of cumulative Casimirs (cut_subsets = list of leg-subsets).
       history = tuple of C2 (Fraction) at each cut subset."""
    m=len(eps); dim=N**m
    Cfull,_,_=casimir_subset(eps, range(m))
    A=_mat(Cfull,dim)
    ns=A.nullspace()  # overall singlets
    if not ns: return []
    # orthonormalize singlet basis (rational Gram-Schmidt)
    B=sp.GramSchmidt(ns, orthonormal=False)
    # build cut operators
    cutmats=[_mat(casimir_subset(eps,Sub)[0],dim) for Sub in cut_subsets]
    # simultaneously diagonalize within the singlet space
    # Represent each singlet vec; act cut operator, express in basis -> small matrices, diagonalize.
    import sympy
    Bm=sp.Matrix.hstack(*B) if B else sp.zeros(dim,0)
    k=Bm.shape[1]
    # Gram
    G=(Bm.T*Bm)
    Ginv=G.inv()
    smallmats=[]
    for Cm in cutmats:
        # projection of Cm onto singlet basis: Ginv * (B^T Cm B)
        smallmats.append(Ginv*(Bm.T*Cm*Bm))
    # simultaneous eigvecs: iteratively refine common eigenbasis
    # start: columns = standard basis of R^k
    vecs=[sp.eye(k)[:,i] for i in range(k)]
    histories=[[] for _ in range(k)]
    groups=[list(range(k))]
    coordbasis=sp.eye(k)
    # We'll compute joint eigen-decomposition by handling one cut matrix at a time using eigenvects
    # Simpler: since all smallmats commute, diagonalize their random combination, then read off each.
    import random
    comb=sum(sp.Rational(p+1)*Sm for p,Sm in enumerate(smallmats)) if smallmats else sp.zeros(k,k)
    if smallmats:
        evd=comb.eigenvects()
        outvecs=[]; 
        for val,mult,basis in evd:
            for vv in basis:
                # vv in coordinate space (k-dim); history = eigenvalue of each smallmat
                hist=[]
                for Sm in smallmats:
                    Av=Sm*vv
                    # Rayleigh: (vv^T G? ) careful: smallmats act in coord space already
                    # eigenvalue = (Av)_i/(vv)_i for nonzero comp
                    lam=None
                    for ii in range(k):
                        if vv[ii]!=0: lam=Av[ii]/vv[ii]; break
                    hist.append(F(int(sp.nsimplify(lam).p), int(sp.nsimplify(lam).q)) if lam is not None else F(0))
                fullvec=Bm*vv
                # normalize fullvec to unit
                nrm=sp.sqrt((fullvec.T*fullvec)[0])
                outvecs.append((tuple(hist), fullvec/nrm))
        return outvecs
    else:
        out=[]
        for i in range(k):
            fv=Bm[:,i]; nrm=sp.sqrt((fv.T*fv)[0]); out.append(((),fv/nrm))
        return out

def link_integral(eps):
    """Single-link Haar integral tensor T[rows][cols] = sum_a L_a(rows) L_a(cols), rows,cols in {0..2}^m.
       Returns dict {(rowtuple,coltuple): Fraction}."""
    basis=fusion_basis(eps, [])  # no cuts; just singlet basis
    m=len(eps); states=list(itertools.product(range(N),repeat=m))
    T={}
    for _,vec in basis:
        comps=[vec[k] for k in range(len(states))]
        for a,sa in enumerate(states):
            if comps[a]==0: continue
            for b,sb in enumerate(states):
                if comps[b]==0: continue
                val=comps[a]*comps[b]
                val=sp.nsimplify(val)
                T[(sa,sb)]=T.get((sa,sb),sp.Integer(0))+val
    return T

if __name__=='__main__':
    # Test (1,-1): expect (1/3) d_{ik} d_{jl}  i.e. T[(i,k),(j,l)] = 1/3 if i==k and j==l? 
    # Our rows=(i,k) are the two row-indices (of U and U*), cols=(j,l). integral U_{ij}U*_{kl}=1/3 d_ik d_jl
    T=link_integral((1,-1))
    ok=True
    for (rw,cl),v in T.items():
        i,k=rw; j,l=cl
        exp=sp.Rational(1,3) if (i==k and j==l) else 0
        if sp.simplify(v-exp)!=0: ok=False
    # also check zeros
    print("(1,-1) integral matches (1/3)d_ik d_jl :", ok, " nonzero entries:",len(T))
    # Test (1,1,1): expect (1/6) eps_{i1i2i3} eps_{j1j2j3}
    T3=link_integral((1,1,1))
    def lev(a,b,c):
        p={(0,1,2):1,(1,2,0):1,(2,0,1):1,(2,1,0):-1,(1,0,2):-1,(0,2,1):-1}
        return p.get((a,b,c),0)
    ok3=True
    for (rw,cl),v in T3.items():
        exp=sp.Rational(1,6)*lev(*rw)*lev(*cl)
        if sp.simplify(v-exp)!=0: ok3=False; 
    # check completeness: all eps*eps/6 present
    cnt=sum(1 for rw in itertools.product(range(3),repeat=3) for cl in itertools.product(range(3),repeat=3) if lev(*rw)*lev(*cl)!=0)
    print("(1,1,1) integral matches (1/6)eps eps :", ok3, " nonzero:",len(T3),"expected",cnt)
    # Test (1,1): no singlet
    print("(1,1) singlets:", len(fusion_basis((1,1),[])), "(expect 0)")
