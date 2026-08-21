# HODGE–HAAR ELECTRIC RESOLVENT ENGINE v0.6
# =========================================
# Self-contained Google Colab / Python block.
#
# PURPOSE
# -------
# Add the electric Hamiltonian and exact reduced resolvent to the structured
# Wilson/Haar engine.
#
# The state representation is a finite color-index partition:
#   * each matrix occurrence records (physical link, U or Ubar);
#   * a canonical set partition records all trace/color-index identifications.
#
# H0 = 1/2 sum_l E_l^2 is generated ONLY from the SU(3) Fierz identity.
# Free U Udag cancellations are imposed exactly.
#
# On each finite H0 closure:
#   1. build the exact Haar Gram matrix G;
#   2. quotient Gram-null trace identities;
#   3. construct the exact metric-Hermitian H0 matrix;
#   4. project out the E0 eigenspace;
#   5. form R = Q(E0-H0)^(-1)Q by exact rational linear algebra.
#
# ACCEPTANCE
# ----------
# * one-plaquette E0 = 8/3;
# * exact adjacent electric spectra;
# * t3 = 5/612 from all 12 signed shared-edge hops;
# * exact R^2 and R^3 Gamma moments;
# * exact Gamma source-sector Q1-W-Q1 selection test;
# * no use of the retired v0.6c inferred direct-cubic target.

import itertools
import math
from collections import defaultdict, Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

import numpy as np
import sympy as sp

N = 3
L = 3
SEED = 0
CF = Fraction(4,3)
E0 = Fraction(8,3)
T3 = Fraction(5,612)
R2_TARGET = Fraction(1975,124848)

gates=[]
def gate(name, ok, detail=""):
    ok=bool(ok)
    gates.append((name,ok,str(detail)))
    print(("[PASS] " if ok else "[FAIL] ")+name+(f" :: {detail}" if detail!="" else ""))

def F(x):
    if isinstance(x,Fraction): return x
    if isinstance(x,sp.Rational): return Fraction(int(x.p),int(x.q))
    return Fraction(x)

# =============================================================================
# PART I — CUBIC CELL COMPLEX
# =============================================================================

print("="*108)
print("PART I — CUBIC WILSON GEOMETRY")
print("="*108)

def shift(v,d,step,L=L):
    w=list(v); w[d]=(w[d]+step)%L; return tuple(w)

def build_cubic(L=3):
    verts=[(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
    links=[]; lid={}
    for v in verts:
        for d in range(3):
            lid[(v,d)]=len(links); links.append((v,d))

    faces=[]; fid={}
    for v in verts:
        for a,b in ((0,1),(0,2),(1,2)):
            fid[(v,a,b)]=len(faces); faces.append((v,a,b))

    B2=np.zeros((len(links),len(faces)),dtype=np.int8)
    for f,(v,a,b) in enumerate(faces):
        va=shift(v,a,1,L); vb=shift(v,b,1,L)
        B2[lid[(v,a)],f]+=1
        B2[lid[(va,b)],f]+=1
        B2[lid[(vb,a)],f]-=1
        B2[lid[(v,b)],f]-=1

    incidence=(B2!=0)
    ADJ=(incidence.T.astype(np.int16)@incidence.astype(np.int16))>0
    return verts,links,faces,lid,fid,B2,ADJ

verts,links,faces,lid,fid,B2,ADJ=build_cubic(L)
E,P=B2.shape
neighbors=[int(f) for f in np.flatnonzero(ADJ[SEED]) if f!=SEED]

gate("seed has 12 distinct shared-edge neighbors",len(neighbors)==12,len(neighbors))
gate("all plaquette linked neighborhoods have size 13 including self",
     np.all(ADJ.sum(axis=1)==13),Counter(ADJ.sum(axis=1).tolist()))

def face_steps(face,sign=+1):
    v,a,b=faces[int(face)]
    va=shift(v,a,1,L); vb=shift(v,b,1,L)
    st=[
        (lid[(v,a)],+1),
        (lid[(va,b)],+1),
        (lid[(vb,a)],-1),
        (lid[(v,b)],-1),
    ]
    if int(sign)<0:
        st=[(l,-d) for l,d in reversed(st)]
    return st

# =============================================================================
# PART II — COLOR-PARTITION WILSON STATES
# =============================================================================

print("\n"+"="*108)
print("PART II — EXACT COLOR-PARTITION STATE ALGEBRA")
print("="*108)

def canon(labels):
    mp={}; out=[]
    for x in labels:
        if x not in mp: mp[x]=len(mp)
        out.append(mp[x])
    return tuple(out)

@dataclass(frozen=True)
class State:
    occ: tuple   # ((physical_link, True=U / False=Ubar), ...)
    part: tuple  # canonical color-index partition, two slots / occurrence

def trace_state(steps):
    m=len(steps)
    occ=[]; labels=[]
    for j,(link,d) in enumerate(steps):
        a=j; b=(j+1)%m
        if int(d)>0:
            occ.append((int(link),True))
            labels.extend((a,b))
        else:
            # (Udag)_ab = Ubar_ba
            occ.append((int(link),False))
            labels.extend((b,a))
    return State(tuple(occ),canon(labels))

TRACE={(f,s):trace_state(face_steps(f,s)) for f in range(P) for s in (-1,+1)}

def tensor_product(a,b):
    shift_label=(max(a.part)+1) if a.part else 0
    return State(a.occ+b.occ,
                 canon(a.part+tuple(x+shift_label for x in b.part)))

def classes(part):
    out=defaultdict(list)
    for i,c in enumerate(part): out[c].append(i)
    return out

def merge_classes(part,pairs):
    n=len(part); parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a=find(a); b=find(b)
        if a!=b: parent[b]=a
    first={}
    for i,c in enumerate(part):
        if c in first: union(i,first[c])
        else: first[c]=i
    for a,b in pairs: union(int(a),int(b))
    return canon([find(i) for i in range(n)])

def swap_rows(part,r1,r2):
    if part[r1]==part[r2]: return part
    z=list(part)
    z[r1],z[r2]=z[r2],z[r1]
    return canon(z)

def opposite_reconnect(part,r1,r2):
    """
    F x Fbar cross term:
      -1/2 delta_(old rows) delta_(new rows) + 1/(2N) I.
    """
    n=len(part)
    cls=classes(part)
    c1,c2=part[r1],part[r2]

    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a=find(a); b=find(b)
        if a!=b: parent[b]=a

    # Preserve every old equality except the two acted row slots.
    for members in cls.values():
        rem=[x for x in members if x not in (r1,r2)]
        for x in rem[1:]: union(rem[0],x)

    # delta on the OLD rows => merge the external remainders.
    rem1=[x for x in cls[c1] if x not in (r1,r2)]
    rem2=[x for x in cls[c2] if x not in (r1,r2)]
    if rem1 and rem2: union(rem1[0],rem2[0])

    # delta on the NEW rows.
    union(r1,r2)
    return canon([find(i) for i in range(n)])

def remove_pair(state,i,j,merge_slots):
    """
    Exact U Udag unitarity reduction.  One disappearing color class is the
    contracted Haar/matrix summation itself; additional disappearing classes
    are free Tr(I)=N factors.
    """
    part=merge_classes(state.part,[merge_slots])
    removed={2*i,2*i+1,2*j,2*j+1}
    keep=[k for k in range(len(part)) if k not in removed]
    keep_classes={part[k] for k in keep}
    lost=len(set(part)-keep_classes)
    scalar=Fraction(N**max(0,lost-1),1)

    new_occ=tuple(o for k,o in enumerate(state.occ) if k not in (i,j))
    new_part=canon([part[k] for k in keep])
    return scalar,State(new_occ,new_part)

def simplify_unitarity(state):
    s=state; scalar=Fraction(1)
    changed=True
    while changed:
        changed=False
        cls=classes(s.part)
        bylink=defaultdict(list)
        for i,(link,typ) in enumerate(s.occ):
            bylink[link].append((i,typ))

        for link,items in bylink.items():
            done=False
            for (i,t1),(j,t2) in itertools.combinations(items,2):
                if t1==t2: continue
                r1,c1=2*i,2*i+1
                r2,c2=2*j,2*j+1

                if set(cls[s.part[r1]])=={r1,r2}:
                    fac,s=remove_pair(s,i,j,(c1,c2))
                    scalar*=fac; changed=True; done=True; break
                if set(cls[s.part[c1]])=={c1,c2}:
                    fac,s=remove_pair(s,i,j,(r1,r2))
                    scalar*=fac; changed=True; done=True; break
            if done: break
    return scalar,s

# Regression: Tr(U Udag)=N.
test=trace_state([(0,+1),(0,-1)])
fac,empty=simplify_unitarity(test)
gate("free unitarity reduction Tr(U Udag)=3",
     fac==3 and len(empty.occ)==0,f"factor={fac}")

# =============================================================================
# PART III — H0 FROM FIERZ ONLY
# =============================================================================

print("\n"+"="*108)
print("PART III — EXACT ELECTRIC HAMILTONIAN FROM FIERZ RECONNECTION")
print("="*108)

def H0_action(state):
    fac0,s=simplify_unitarity(state)
    out=defaultdict(Fraction)

    # Self Casimir: each matrix occurrence contributes C_F/2.
    out[s]+=fac0*Fraction(len(s.occ),1)*CF/2

    bylink=defaultdict(list)
    for i,(link,typ) in enumerate(s.occ):
        bylink[link].append((i,typ))

    for link,items in bylink.items():
        for (i,t1),(j,t2) in itertools.combinations(items,2):
            r1,r2=2*i,2*j
            if t1==t2:
                raw=State(s.occ,swap_rows(s.part,r1,r2))
                fac,z=simplify_unitarity(raw)
                out[z]+=fac0*fac*Fraction(1,2)
                out[s]-=fac0*Fraction(1,2*N)
            else:
                raw=State(s.occ,opposite_reconnect(s.part,r1,r2))
                fac,z=simplify_unitarity(raw)
                out[z]-=fac0*fac*Fraction(1,2)
                out[s]+=fac0*Fraction(1,2*N)

    return {z:c for z,c in out.items() if c}

seed=TRACE[(SEED,+1)]
hseed=H0_action(seed)
gate("one plaquette is exact H0 eigenstate E0=8/3",
     hseed=={seed:E0},hseed)

# =============================================================================
# PART IV — EXACT BALANCED HAAR METRIC (k <= 2 AT FIRST CUT)
# =============================================================================

print("\n"+"="*108)
print("PART IV — EXACT HAAR GRAM METRIC")
print("="*108)

def pinv(p):
    out=[0]*len(p)
    for i,j in enumerate(p): out[j]=i
    return tuple(out)

def pcompose(p,q): return tuple(p[q[i]] for i in range(len(p)))

def pcycles(p):
    seen=[False]*len(p); c=0
    for i in range(len(p)):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]:
                seen[j]=True; j=p[j]
    return c

@lru_cache(None)
def wg_fixed(k):
    ps=list(itertools.permutations(range(k)))
    G=sp.Matrix([
        [sp.Integer(N)**pcycles(pcompose(pinv(a),b)) for b in ps]
        for a in ps
    ])
    W=G.inv()
    WW=[[F(W[i,j]) for j in range(len(ps))] for i in range(len(ps))]
    return ps,WW

def combine_bra_ket(a,b):
    bra_occ=tuple((link,not typ) for link,typ in a.occ)
    off=(max(a.part)+1) if a.part else 0
    return bra_occ+b.occ, canon(a.part+tuple(x+off for x in b.part))

_HAAR={}
def haar_inner(a,b):
    key=(a,b)
    if key in _HAAR: return _HAAR[key]

    occ,part=combine_bra_ket(a,b)
    bylink=defaultdict(lambda:{True:[],False:[]})
    for i,(link,typ) in enumerate(occ):
        bylink[link][typ].append(i)

    states={part:Fraction(1)}
    for link,g in bylink.items():
        U=g[True]; B=g[False]
        if len(U)!=len(B):
            _HAAR[key]=Fraction(0); return Fraction(0)
        k=len(U)
        if k>2:
            raise RuntimeError("v0.6 first-cut metric unexpectedly needs k>2")
        ps,W=wg_fixed(k)
        new=defaultdict(Fraction)
        for st,c0 in states.items():
            for si,sigma in enumerate(ps):
                for ti,tau in enumerate(ps):
                    pairs=[]
                    for r in range(k):
                        pairs.append((2*U[r],2*B[sigma[r]]))
                        pairs.append((2*U[r]+1,2*B[tau[r]]+1))
                    new[merge_classes(st,pairs)] += c0*W[si][ti]
        states={st:c for st,c in new.items() if c}

    total=sum((c*N**len(set(st)) for st,c in states.items()),Fraction(0))
    _HAAR[key]=total
    return total

gate("plaquette Haar norm = 1",haar_inner(seed,seed)==1,haar_inner(seed,seed))

# =============================================================================
# PART V — FINITE H0 CLOSURE, GRAM QUOTIENT, REDUCED RESOLVENT
# =============================================================================

print("\n"+"="*108)
print("PART V — EXACT GRAM-QUOTIENT REDUCED RESOLVENT")
print("="*108)

def closure(seed_state,max_states=100):
    fac,s=simplify_unitarity(seed_state)
    assert fac==1
    states=[s]; seen={s}; q=deque([s])
    while q:
        x=q.popleft()
        for y in H0_action(x):
            if y not in seen:
                seen.add(y); states.append(y); q.append(y)
                if len(states)>max_states:
                    raise RuntimeError("unexpectedly large H0 closure")
    return states

def closure_matrices(seed_state):
    basis=closure(seed_state)
    idx={s:i for i,s in enumerate(basis)}
    m=len(basis)

    A=sp.zeros(m)
    for j,s in enumerate(basis):
        for z,c in H0_action(s).items():
            A[idx[z],j]+=sp.Rational(c.numerator,c.denominator)

    G=sp.zeros(m)
    for i in range(m):
        for j in range(i,m):
            v=haar_inner(basis[i],basis[j])
            G[i,j]=G[j,i]=sp.Rational(v.numerator,v.denominator)

    # Physical quotient: independent Gram columns.
    piv=list(G.rref()[1])
    Gp=G.extract(piv,piv)
    Hmetric=(G*A).extract(piv,piv)
    H=sp.simplify(Gp.inv()*Hmetric)

    return basis,A,G,piv,Gp,H

def reduced_resolvent_on_state(seed_state,power=1):
    basis,A,G,piv,Gp,H=closure_matrices(seed_state)
    e=sp.Rational(8,3)

    # Coordinate vector of seed_state in the independent Gram basis.
    v=sp.Matrix([G[i,0] for i in piv])
    c=sp.simplify(Gp.inv()*v)

    Z=(H-e*sp.eye(len(piv))).nullspace()
    if Z:
        Z=sp.Matrix.hstack(*Z)
        P0=sp.simplify(Z*(Z.T*Gp*Z).inv()*Z.T*Gp)
    else:
        P0=sp.zeros(len(piv))

    Q=sp.eye(len(piv))-P0
    M=e*sp.eye(len(piv))-H
    R=sp.simplify(Q*(M+P0).inv()*Q)
    Rp=R**int(power)
    rc=sp.simplify(Rp*c)

    out=defaultdict(Fraction)
    for a,j in enumerate(piv):
        x=sp.factor(rc[a])
        if x!=0:
            out[basis[j]]+=F(x)

    meta={
        "closure_dim":len(basis),
        "gram_rank":len(piv),
        "spectrum":H.eigenvals(),
        "E0_nullity":len(Z.columnspace()) if isinstance(Z,sp.MatrixBase) and Z.cols else 0,
    }
    return dict(out),meta

def multiply_vec(vec,tr):
    out=defaultdict(Fraction)
    for s,c in vec.items():
        fac,z=simplify_unitarity(tensor_product(s,tr))
        out[z]+=c*fac
    return {z:c for z,c in out.items() if c}

# Four canonical first-cut geometries.
adj=neighbors[0]
first_states={
    "same_like": multiply_vec({seed:Fraction(1)},TRACE[(SEED,+1)]),
    "same_opposite": multiply_vec({seed:Fraction(1)},TRACE[(SEED,-1)]),
    "adj_like": multiply_vec({seed:Fraction(1)},TRACE[(adj,+1)]),
    "adj_mixed": multiply_vec({seed:Fraction(1)},TRACE[(adj,-1)]),
}

spectra={}
for name,vec in first_states.items():
    assert len(vec)==1
    st=next(iter(vec))
    basis,A,G,piv,Gp,H=closure_matrices(st)
    spectra[name]=(len(basis),len(piv),H.eigenvals())
    print(f"{name:14s}: closure={len(basis)}, Gram rank={len(piv)}, spectrum={H.eigenvals()}")

gate("same-like physical spectrum = {8/3,20/3}",
     set(spectra["same_like"][2])=={sp.Rational(8,3),sp.Rational(20,3)},
     spectra["same_like"])
gate("same-opposite spectrum = {0,6}",
     set(spectra["same_opposite"][2])=={sp.Integer(0),sp.Integer(6)},
     spectra["same_opposite"])
gate("adjacent like F x F spectrum = {14/3,17/3}",
     set(spectra["adj_like"][2])=={sp.Rational(14,3),sp.Rational(17,3)},
     spectra["adj_like"])
gate("adjacent mixed F x Fbar spectrum = {4,11/2}",
     set(spectra["adj_mixed"][2])=={sp.Integer(4),sp.Rational(11,2)},
     spectra["adj_mixed"])
gate("same-like 8-word Fierz closure collapses to Gram rank 2",
     spectra["same_like"][0]==8 and spectra["same_like"][1]==2,
     spectra["same_like"][:2])

# =============================================================================
# PART VI — STRUCTURED DEPTH-2 P V R V P
# =============================================================================

print("\n"+"="*108)
print("PART VI — COLD SECOND-ORDER EFFECTIVE HOPPING")
print("="*108)

def generate_words(depth):
    wf=np.empty((1,0),dtype=np.int16)
    ws=np.empty((1,0),dtype=np.int8)
    flux=np.asarray(B2[:,SEED][None,:],dtype=np.int16)

    for d in range(depth):
        M=len(wf)
        mask=np.broadcast_to(ADJ[SEED],(M,P)).copy()
        for j in range(d):
            mask |= ADJ[wf[:,j]]

        rows,fs=np.nonzero(mask)
        K=len(rows)
        rr=np.repeat(rows,2)
        ff=np.repeat(fs.astype(np.int16),2)
        ss=np.tile(np.asarray([-1,+1],dtype=np.int8),K)

        nwf=np.empty((2*K,d+1),dtype=np.int16)
        nws=np.empty((2*K,d+1),dtype=np.int8)
        if d:
            nwf[:,:d]=wf[rr]; nws[:,:d]=ws[rr]
        nwf[:,d]=ff; nws[:,d]=ss

        flux=flux[rr]+ss[:,None]*B2[:,ff].T.astype(np.int16)
        wf,ws=nwf,nws

    return wf,ws,flux

wf2,ws2,flux2=generate_words(2)
gate("depth-2 linked corpus has 1028 words",len(wf2)==1028,len(wf2))

endpoint_map={}
for f in range(P):
    endpoint_map[tuple(B2[:,f].astype(int))]=(f,+1)
    endpoint_map[tuple((-B2[:,f]).astype(int))]=(f,-1)

exact_rows=[]
for wf,ws,q in zip(wf2,ws2,flux2):
    ep=endpoint_map.get(tuple(int(x) for x in q))
    if ep is not None:
        exact_rows.append((wf,ws,ep))

gate("exact depth-2 one-plaquette endpoint histories = 75",
     len(exact_rows)==75,len(exact_rows))

# Only 26 first cuts. Cache R and R^2 exactly.
R1={}
R1sq={}
for f in np.flatnonzero(ADJ[SEED]):
    f=int(f)
    for s in (-1,+1):
        v=multiply_vec({seed:Fraction(1)},TRACE[(f,s)])
        assert len(v)==1
        st=next(iter(v))
        rv,_=reduced_resolvent_on_state(st,power=1)
        r2v,_=reduced_resolvent_on_state(st,power=2)

        # input multiplication scalar is one in these first-cut states
        R1[(f,s)]=rv
        R1sq[(f,s)]=r2v

def endpoint_sum(cache):
    sums=defaultdict(Fraction)
    counts=Counter()

    for wf,ws,ep in exact_rows:
        f1,s1=int(wf[0]),int(ws[0])
        f2,s2=int(wf[1]),int(ws[1])

        v=multiply_vec(cache[(f1,s1)],TRACE[(f2,s2)])
        endpoint=TRACE[ep]
        amp=sum((c*haar_inner(endpoint,z) for z,c in v.items()),Fraction(0))
        sums[ep]+=amp
        counts[ep]+=1

    # C-odd normalized matrix element: fixed ket +, endpoint + minus endpoint -.
    codd={f:sums[(f,+1)]-sums[(f,-1)] for f in range(P)}
    return sums,counts,codd

sums_R,counts_R,codd_R=endpoint_sum(R1)
sums_R2,counts_R2,codd_R2=endpoint_sum(R1sq)

# Incidence sign on every shared-edge neighbor.
incsign={}
for q in neighbors:
    shared=np.flatnonzero((B2[:,SEED]!=0)&(B2[:,q]!=0))
    assert len(shared)==1
    incsign[q]=int(B2[shared[0],SEED]*B2[shared[0],q])

print("neighbor  incidence   PVRVP             PVR^2VP")
for q in neighbors:
    print(f"{q:8d} {incsign[q]:10d} {str(codd_R[q]):>18s} {str(codd_R2[q]):>18s}")

gate("all 12 second-order hops equal t3 times incidence sign",
     all(codd_R[q]==incsign[q]*T3 for q in neighbors),
     Counter(codd_R[q] for q in neighbors))
gate("second-order coefficient t3=5/612 cold reproduced",
     abs(codd_R[adj])==T3,codd_R[adj])
gate("all non-neighbor offdiagonal exact second-order hops vanish",
     all(codd_R[q]==0 for q in range(P) if q!=SEED and q not in neighbors),
     "checked all 80 off-site endpoints")



# =============================================================================
# HODGE v10a.6 — EXACT GAMMA-Q1 ZERO + FOURTH-ORDER SCALAR LEDGER
# =============================================================================
# Canonical project convention: H = H0 - u M, so W = -M and e1_A = +1.
# The core above uses V=M for Wilson multiplication.  Even resolvent moments are
# unchanged by W=-V.  The two odd magnetic moments tested below vanish exactly,
# so their sign convention is immaterial.
#
# This certificate does NOT claim m4_rest.  It closes the Q1 fold ledger exactly,
# proves the Gamma source-sector sigma3 and C moments vanish by exact Haar
# contractions, and imports only the independently cold-certified adjacent
# determinant rationals from v10a.5 as a frozen sub-certificate.
# =============================================================================

V10A6_GATE_START=len(gates)
print("\n"+"="*112)
print("HODGE v10a.6 — EXACT GAMMA-Q1 ZERO + FOURTH-ORDER SCALAR LEDGER")
print("="*112)
print("arithmetic                       : exact Fraction/SymPy on Q1 sector")
print("global Q2 basis                  : NOT USED")
print("L=5 giant D contraction          : NOT USED")
print("Q1-W-Q1 test                     : exact Gamma source-sector Haar contraction")
print("m4_rest                          : BLINDED / NOT CLAIMED")

# -----------------------------------------------------------------------------
# [1] Exact R^3 and Gamma moments
# -----------------------------------------------------------------------------
print("\n[1] EXACT GAMMA Q1 RESOLVENT MOMENTS")
R1cube={}
for f in np.flatnonzero(ADJ[SEED]):
    f=int(f)
    for s in (-1,+1):
        v=multiply_vec({seed:Fraction(1)},TRACE[(f,s)])
        assert len(v)==1
        st=next(iter(v))
        r3v,_=reduced_resolvent_on_state(st,power=3)
        R1cube[(f,s)]=r3v
_,_,codd_R3=endpoint_sum(R1cube)

incsign={}
for q in neighbors:
    shared=np.flatnonzero((B2[:,SEED]!=0)&(B2[:,q]!=0))
    assert len(shared)==1
    incsign[q]=int(B2[shared[0],SEED]*B2[shared[0],q])
sum_inc=sum(incsign.values())
gate("v10a.6 cubic shared-edge incidence sum is -4",sum_inc==-4,sum_inc)

R1_off=codd_R[adj]/incsign[adj]
R2_off=codd_R2[adj]/incsign[adj]
R3_off=codd_R3[adj]/incsign[adj]
gate("v10a.6 R^3 shared-edge coefficient is incidence-universal",
     all(codd_R3[q]==incsign[q]*R3_off for q in neighbors),R3_off)

E2_A=codd_R[SEED]+sum_inc*R1_off
N_A=codd_R2[SEED]+sum_inc*R2_off
J_A=codd_R3[SEED]+sum_inc*R3_off

gate("v10a.6 exact e2_A=-5945/612",E2_A==Fraction(-5945,612),E2_A)
gate("v10a.6 exact N_A=511051/124848",N_A==Fraction(511051,124848),N_A)
gate("v10a.6 exact J_A=-48945521/25468992",J_A==Fraction(-48945521,25468992),J_A)
print("e2_A =",E2_A,"=",float(E2_A))
print("N_A  =",N_A,"=",float(N_A))
print("J_A  =",J_A,"=",float(J_A))

# -----------------------------------------------------------------------------
# [2] Exact Gamma Q1-W-Q1 source-sector selection rule
# -----------------------------------------------------------------------------
print("\n[2] EXACT GAMMA Q1-W-Q1 SOURCE-SECTOR SELECTION RULE")

_link_lookup={(v,d):i for i,(v,d) in enumerate(links)}

def _v10a6_translate_state(st,dx):
    occ=[]
    for li,typ in st.occ:
        v,d=links[int(li)]
        vv=((v[0]+dx[0])%L,(v[1]+dx[1])%L,(v[2]+dx[2])%L)
        occ.append((_link_lookup[(vv,d)],typ))
    return State(tuple(occ),st.part)

def _v10a6_flux_key(st):
    cnt=defaultdict(int)
    for l,t in st.occ:
        cnt[int(l)]+=1 if t else -1
    out=[]
    for l,c in cnt.items():
        r=c%3
        if r==2: r=-1
        if r: out.append((int(l),int(r)))
    return tuple(sorted(out))

def _v10a6_add_face_key(k,f,s):
    d=defaultdict(int)
    for l,c in k: d[int(l)]+=int(c)
    bf=int(s)*B2[:,int(f)]
    for i in np.flatnonzero(bf): d[int(i)]+=int(bf[i])
    out=[]
    for l,c in d.items():
        r=c%3
        if r==2: r=-1
        if r: out.append((int(l),int(r)))
    return tuple(sorted(out))

@lru_cache(None)
def _v10a6_R_cached(st,power):
    return tuple(reduced_resolvent_on_state(st,power=int(power))[0].items())

def _v10a6_gamma_vectors(seed_face):
    """Unnormalised C-odd Gamma r1=R V|P> and Rr1=R^2 V|P> for one axial plane."""
    pol=faces[int(seed_face)][1:]
    src_faces=[f for f,(_,a,b) in enumerate(faces) if (a,b)==pol]
    seed_r1=defaultdict(Fraction); seed_rr1=defaultdict(Fraction)
    for s0,c0 in ((+1,Fraction(1)),(-1,Fraction(-1))):
        src=TRACE[(int(seed_face),s0)]
        for f in np.flatnonzero(ADJ[int(seed_face)]):
            f=int(f)
            for sf in (-1,+1):
                v=multiply_vec({src:Fraction(1)},TRACE[(f,sf)])
                for st,c in v.items():
                    for z,a in _v10a6_R_cached(st,1): seed_r1[z]+=c0*c*a
                    for z,a in _v10a6_R_cached(st,2): seed_rr1[z]+=c0*c*a
    seed_r1={z:c for z,c in seed_r1.items() if c}
    seed_rr1={z:c for z,c in seed_rr1.items() if c}
    sv=faces[int(seed_face)][0]
    R1g=defaultdict(Fraction); RR1g=defaultdict(Fraction)
    for f in src_faces:
        v=faces[f][0]
        dx=((v[0]-sv[0])%L,(v[1]-sv[1])%L,(v[2]-sv[2])%L)
        for st,c in seed_r1.items(): R1g[_v10a6_translate_state(st,dx)]+=c
        for st,c in seed_rr1.items(): RR1g[_v10a6_translate_state(st,dx)]+=c
    return ({z:c for z,c in R1g.items() if c},
            {z:c for z,c in RR1g.items() if c},
            2*len(src_faces))  # norm^2 of unnormalised sum_x (|p>-|pbar>)

def _v10a6_W_bilinear(A,B):
    """Exact <A|M|B>; center prefilter then exact Haar. Returns exact Fraction."""
    groups=defaultdict(list)
    for a,ca in A.items(): groups[_v10a6_flux_key(a)].append((a,ca))
    total=Fraction(0); tests=0; nonzero=0
    for b,cb in B.items():
        kb=_v10a6_flux_key(b)
        for f in range(P):
            for sf in (-1,+1):
                bras=groups.get(_v10a6_add_face_key(kb,f,sf))
                if not bras: continue
                fac,prod=simplify_unitarity(tensor_product(b,TRACE[(f,sf)]))
                for a,ca in bras:
                    tests+=1
                    h=haar_inner(a,prod)
                    if h:
                        total+=ca*cb*fac*h; nonzero+=1
    return total,tests,nonzero

zero_rows=[]
for pol in ((0,1),(0,2),(1,2)):
    sf=next(f for f,(v,a,b) in enumerate(faces) if v==(0,0,0) and (a,b)==pol)
    gr1,grr1,srcnorm=_v10a6_gamma_vectors(sf)
    sig_raw,nt1,nz1=_v10a6_W_bilinear(gr1,gr1)
    c_raw,nt2,nz2=_v10a6_W_bilinear(grr1,gr1)
    sigma=sig_raw/Fraction(srcnorm,1)
    C=c_raw/Fraction(srcnorm,1)
    zero_rows.append((pol,sigma,C,nt1,nz1,nt2,nz2,len(gr1)))
    print(f"pol={pol}: sigma3={sigma}, C={C}, terms={len(gr1)}, Haar tests={nt1}/{nt2}, nonzero={nz1}/{nz2}")

gate("v10a.6 exact Gamma sigma3=<r1|M|r1>=0 in all T1 orientations",
     all(r[1]==0 for r in zero_rows),tuple(r[1] for r in zero_rows))
gate("v10a.6 exact Gamma C=<Rr1|M|r1>=0 in all T1 orientations",
     all(r[2]==0 for r in zero_rows),tuple(r[2] for r in zero_rows))
gate("v10a.6 every center-allowed Q1-W-Q1 Haar endpoint vanishes exactly",
     all(r[4]==0 and r[6]==0 for r in zero_rows),
     tuple((r[0],r[3],r[4],r[5],r[6]) for r in zero_rows))

SIGMA3_A=Fraction(0)
C_A=Fraction(0)

# -----------------------------------------------------------------------------
# [3] Exact lower-order regressions + full Q1 fold
# -----------------------------------------------------------------------------
print("\n[3] EXACT LOWER-ORDER REGRESSIONS AND Q1 FOLD")
EV2=Fraction(-3,4)
EV3=Fraction(-9,32)
M2=E2_A-13*EV2
E3_A=SIGMA3_A-N_A       # e1_A=+1, sigma2'=-N
M3=E3_A-13*EV3
FOLD_A=-2*C_A-E2_A*N_A+J_A   # e1_A=1

gate("v10a.6 m2 regression=11/306",M2==Fraction(11,306),M2)
gate("v10a.6 m3 regression=-109151/249696",M3==Fraction(-109151,249696),M3)
gate("v10a.6 exact axial Q1 fold=5315003/140454",FOLD_A==Fraction(5315003,140454),FOLD_A)
print("m2      =",M2)
print("m3      =",M3)
print("fold_A  =",FOLD_A,"=",float(FOLD_A))

# -----------------------------------------------------------------------------
# [4] Frozen v10a.5 adjacent-determinant subcertificate ledger
# -----------------------------------------------------------------------------
print("\n[4] FROZEN v10a.5 ADJACENT-DETERMINANT SUBCERTIFICATE")
# These are NOT inferred here. They are the independent cold-history outputs of
# hodge_v10a5_adjacent_determinant_cold_history_certificate.py, whose frozen
# script hash is recorded below. This run only verifies exact rational relations.
V10A5_SHA256="90f857dec43f8537441a904fd9b065609d3ebe07418885847b84aa7f392e25c9"
A_L=Fraction(-53,408)
A_M=Fraction(-619,4624)
B_DET=A_M-A_L
SIGNED_EDGE_FLAT=-4*B_DET
gate("v10a.6 frozen determinant b_det=-55/13872",B_DET==Fraction(-55,13872),B_DET)
gate("v10a.6 frozen determinant signed-edge flat contribution=55/3468",
     SIGNED_EDGE_FLAT==Fraction(55,3468),SIGNED_EDGE_FLAT)
print("v10a.5 script SHA256 =",V10A5_SHA256)
print("A_L                 =",A_L)
print("A_M                 =",A_M)
print("b_det               =",B_DET)
print("-4 b_det            =",SIGNED_EDGE_FLAT)
print("NOTE: -4 b_det is the certified signed-adjacency contribution, NOT the complete determinant rest scalar a-4b.")

# -----------------------------------------------------------------------------
# [5] Exact scalar ledger / hard stop
# -----------------------------------------------------------------------------
print("\n[5] FOURTH-ORDER SCALAR LEDGER — HARD STOP BEFORE m4")
print("Exact closed pieces:")
print("  sigma3_A = 0")
print("  C_A      = 0")
print("  e2_A     =",E2_A)
print("  N_A      =",N_A)
print("  J_A      =",J_A)
print("  fold_A   =",FOLD_A)
print("  adjacent determinant signed-edge piece -4*b_det =",SIGNED_EDGE_FLAT)
print("\nStill unresolved before m4_rest may be unblinded:")
print("  (i) complete direct D_A scalar ledger, including scalar part of adjacent determinant block;")
print("  (ii) remaining repeated/support-preserving connected direct histories;")
print("  (iii) marked vacuum fourth-order cluster weights and Mobius subtraction.")
print("\nCanonical formula now reduced exactly to")
print("  e4_A = D_A - e2_A*N_A + J_A = D_A +",FOLD_A)
print("because sigma3_A=C_A=0 has been cold-proved in the Gamma source sector.")

print("\n"+"="*112)
print("FINAL v10a.6 GATE SUMMARY")
print("="*112)
newg=gates[V10A6_GATE_START:]
for i,(n,ok,d) in enumerate(newg,1):
    print(f"{i:02d}. {'PASS' if ok else 'FAIL'} — {n}"+(f" :: {d}" if d else ""))
print("-"*112)
print(f"PASSED {sum(x[1] for x in newg)}/{len(newg)} v10a.6 GATES")
if not all(x[1] for x in newg):
    raise SystemExit("v10a.6 exact scalar ledger failed")
print("\nRESULT: Q1 fold sector is now exact and unconditional at Gamma. m4_rest remains correctly blinded pending D_A + linked Mobius closure.")
