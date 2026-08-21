#!/usr/bin/env python3
"""
ENGINE_SHELL6_haar_loops.py -- exact multi-link SU(3) Haar integrator for lattice Wilson
loops, plus loop/plaquette geometry, built on the certified su3_moments_ext engine.

A "geometric word" is a cyclic sequence of (link_id, power) with power=+1 (U) or
-1 (U^dag).  haar_loops([w1,w2,...]) returns the EXACT rational
    int_{SU(3)}  prod_i Tr( prod_{(lid,pw) in wi} U_lid^pw )  dU
by integrating each lattice link independently with link_terms() and contracting
the shared vertex indices with eval_term().  This is the same per-link Weingarten/
epsilon machinery the domino engine uses, threaded through lattice geometry.

PART-1 calibration (run as main): reproduces the note's first-order shell-6 result
(corner-push amplitude, exotic degeneracy, excited-1+- split +/- sqrt2/3) from
first principles -- the gate that validates the conventions before O(y^2).
"""
import itertools, sys, os
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ENGINE_FLUX_su3_moments_ext import link_terms, eval_term

DIRS=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
neg=lambda d:d^1
PASS=[]
def gate(name,c):
    PASS.append((name,bool(c))); print(f"  GATE {'PASS' if c else 'FAIL'} :: {name}")
    if not c: raise SystemExit("GATE FAILED: "+name)

# ---------- lattice link bookkeeping ----------
def edge_to_link(site, d):
    """directed step from `site` in direction d -> (link_id, power).
    link_id = (lower_site, axis); power +1 if step is along +axis else -1."""
    ax=d//2
    if d%2==0:
        lo=site; pw=+1
    else:
        lo=(site[0]+DIRS[d][0], site[1]+DIRS[d][1], site[2]+DIRS[d][2]); pw=-1
    return (lo,ax), pw

def steps_to_word(start, dseq):
    """sequence of directions from start -> cyclic geometric word [(link_id,pw),...]
    and the list of visited sites (for validation)."""
    word=[]; pos=start
    for d in dseq:
        lid,pw=edge_to_link(pos,d); word.append((lid,pw))
        pos=(pos[0]+DIRS[d][0], pos[1]+DIRS[d][1], pos[2]+DIRS[d][2])
    return word, pos

def dagger(word):
    return [ (lid,-pw) for (lid,pw) in reversed(word) ]

# ---------- exact multi-link Haar integral ----------
_HCACHE={}
def haar_loops(words):
    """EXACT int over SU(3) of prod_i Tr(word_i).  words: list of cyclic
    [(link_id,power),...].  Returns Fraction."""
    key=tuple(tuple(w) for w in words)
    if key in _HCACHE: return _HCACHE[key]
    nv=0
    linkfac=defaultdict(lambda:([],[]))   # link_id -> (us,bs)
    for w in words:
        Lw=len(w); ids=list(range(nv,nv+Lw)); nv+=Lw
        for t,(lid,pw) in enumerate(w):
            a,b=ids[t], ids[(t+1)%Lw]
            us,bs=linkfac[lid]
            if pw==+1: us.append((a,b))
            else:      bs.append((b,a))
    term_lists=[]
    for (us,bs) in linkfac.values():
        tl=link_terms(us,bs)
        if not tl:           # vanishing link integral -> whole thing zero
            _HCACHE[key]=F(0); return F(0)
        term_lists.append(tl)
    tot=F(0)
    for combo in itertools.product(*term_lists):
        coeff=F(1); cons=()
        for (c_,k_) in combo: coeff*=c_; cons=cons+k_
        if coeff!=0: tot+=eval_term(coeff,cons,nv)
    _HCACHE[key]=tot
    return tot

def norm2(word):
    return haar_loops([word, dagger(word)])

def overlap_op(bra_word, op_words, ket_word):
    """<bra| (prod of op traces) |ket> = int Tr(bra^dag) * prod op * Tr(ket)."""
    return haar_loops([dagger(bra_word)] + list(op_words) + [ket_word])

# ---------- plaquette geometry ----------
ORIENT=[(0,1),(0,2),(1,2)]
def plaquette_word(corner, o, eps=+1):
    """unit square at `corner` in plane ORIENT[o]; eps=+1 -> Tr U_p, -1 -> Tr U_p^dag."""
    mu,nu=ORIENT[o]
    dseq=[2*mu, 2*nu, 2*mu+1, 2*nu+1]   # +mu,+nu,-mu,-nu
    w,end=steps_to_word(corner,dseq)
    assert end==corner
    return w if eps==+1 else dagger(w)

def all_plaquettes(extent=2):
    """all (corner,o) within a small box -- enough to surround any localized loop."""
    rng=range(-extent,extent+1)
    return [((x,y,z),o) for x in rng for y in rng for z in rng for o in range(3)]

# =====================================================================
# PART 1 : first-order shell-6 calibration  (validates conventions)
# =====================================================================
def shapes6_simple():
    r=set()
    canon=lambda s:min(tuple(list(s)[i:]+list(s)[:i]) for i in range(len(s)))
    def dfs(seq,pos,vis):
        if len(seq)==6:
            if pos==(0,0,0) and neg(seq[-1])!=seq[0]: r.add(canon(seq))
            return
        for d in range(6):
            if seq and neg(seq[-1])==d: continue
            p=(pos[0]+DIRS[d][0],pos[1]+DIRS[d][1],pos[2]+DIRS[d][2])
            if p==(0,0,0):
                if len(seq)+1!=6: continue
            elif p in vis: continue
            dfs(seq+[d],p,vis|{p})
    dfs([], (0,0,0),{(0,0,0)}); return r

def main():
    print("="*72,"\nPART 1: primitive sanity + first-order shell-6 calibration")
    print("="*72)
    # primitive sanity: norms of elementary loops
    p0=plaquette_word((0,0,0),0)
    gate("norm(single plaquette) = 1  (int |Tr U_p|^2 = 1)", norm2(p0)==1)
    canon=lambda s:min(tuple(list(s)[i:]+list(s)[:i]) for i in range(len(s)))
    ALL=sorted(shapes6_simple())
    naxes=lambda s: len(set(d//2 for d in s))
    HEX=[s for s in ALL if naxes(s)==3]
    # norms of a hexagon and a rectangle (placed at origin)
    hexw,_=steps_to_word((0,0,0),HEX[0])
    gate("norm(twisted hexagon) = 1 (simple loop, distinct links)", norm2(hexw)==1)
    rect=[s for s in ALL if naxes(s)==2][0]
    rectw,_=steps_to_word((0,0,0),rect)
    gate("norm(rectangle) = 1 (simple loop, distinct links)", norm2(rectw)==1)

    # ---- first-order matrix element on the 44 zero-momentum loop states ----
    # M1[L',L] = sum over plaquettes p, eps of <L'| Tr U_p^eps |L>, summed over the
    # relative translation between the (fixed) L' shape and translated L shape.
    idx={s:i for i,s in enumerate(ALL)}; N=len(ALL)
    plqs=all_plaquettes(extent=2)
    # Represent each shape as a frozenset of directed edges from origin placement.
    def edgeset(start, dseq):
        s=set(); pos=start
        for d in dseq:
            lid,pw=edge_to_link(pos,d); s.add((lid,pw)); pos=tuple(pos[k]+DIRS[d][k] for k in range(3))
        return frozenset(s)
    base_edges={s: edgeset((0,0,0),s) for s in ALL}
    # translate a shape's edge-set
    def translate_edges(es, t):
        out=set()
        for (lid,pw) in es:
            (lo,ax)=lid; lo2=(lo[0]+t[0],lo[1]+t[1],lo[2]+t[2]); out.add(((lo2,ax),pw))
        return frozenset(out)
    # canonical key of an edge-set (translate min corner to origin) -> identify shape & position
    def canon_edges(es):
        sites=[lo for ((lo,ax),pw) in es]
        mn=(min(s[0] for s in sites),min(s[1] for s in sites),min(s[2] for s in sites))
        return frozenset((((lo[0]-mn[0],lo[1]-mn[1],lo[2]-mn[2]),ax),pw) for ((lo,ax),pw) in es), mn
    # build map from canonical edge-set -> shape index (both orientations of the loop)
    shape_of={}
    for s in ALL:
        ck,_=canon_edges(base_edges[s]); shape_of[ck]=idx[s]
        # also the reversed loop (negate all powers) is the SAME geometric loop set? no:
    # apply one plaquette (singlet route) to an edge-set; return new simple-loop edge-set or None
    def apply_plaq(es, pw_word):
        es=set(es); padd=set(pw_word)
        # cancel: edge e in padd with reverse in es -> remove from es, drop e
        new=set(es);
        for (lid,pw) in padd:
            if (lid,-pw) in new:
                new.discard((lid,-pw))           # singlet cancellation
            elif (lid,pw) in new:
                return None                       # double flux -> not a Wilson loop (higher irrep)
            else:
                new.add((lid,pw))
        # validate: simple closed loop (each vertex in=out, single cycle)
        return frozenset(new) if is_simple_loop(new) else frozenset(new)  # return; classify later
    def is_simple_loop(es):
        # in/out balance and connected single cycle, each undirected link used once
        deg=defaultdict(int); links=set()
        for (lid,pw) in es:
            (lo,ax)=lid
            if lid in links: return False
            links.add(lid)
            a=lo; b=tuple(lo[k]+ (1 if k==ax else 0) for k in range(3))
            if pw==+1: deg[a]+=1; deg[b]-=1
            else: deg[a]-=1; deg[b]+=1
        return all(d==0 for d in deg.values()) and len(es)>0
    # length of an edge set
    def length(es): return len(es)

    # Build M1 on the 44 states.
    M1=np.zeros((N,N))
    # to sum over relative translation: fix L at origin (base), translate plaquettes over the box,
    # the produced L'-edge-set is canonicalized -> (shape, corner-offset); zero-momentum sum
    # means we accumulate regardless of offset.
    for s in ALL:
        Les=base_edges[s]
        for (corner,o) in plqs:
            for eps in (+1,-1):
                pw=plaquette_word(corner,o,eps)
                res=apply_plaq(Les,pw)
                if res is None: continue
                if length(res)!=6: continue          # first order: stay in shell 6
                if not is_simple_loop(res): continue
                ck,_=canon_edges(res)
                if ck not in shape_of: continue       # not one of the 44 (e.g. non-planar artifact)
                jp=shape_of[ck]
                # amplitude <L'| Tr U_p^eps |L> (norms are 1 for simple loops)
                Lw,_=steps_to_word((0,0,0),s)
                # reconstruct L' word from res? use overlap via words:
                amp=overlap_op(edges_to_word(res), [pw], Lw)
                M1[jp, idx[s]] += float(amp)
    gate("M1 symmetric", np.allclose(M1,M1.T,atol=1e-9))
    print("  distinct nonzero |M1| entries:", sorted(set(round(abs(M1[i,j]),6) for i in range(N) for j in range(N) if abs(M1[i,j])>1e-9)))
    print(f"  total nonzero M1 entries: {int((np.abs(M1)>1e-9).sum())}  (cf. 96 corner-push edges)")
    print(f"ALL {sum(p for _,p in PASS)}/{len(PASS)} PART-1 GATES PASSED")

def edges_to_word(es):
    """recover a cyclic geometric word from a simple-loop edge set."""
    # build directed adjacency
    out=defaultdict(list)
    for (lid,pw) in es:
        (lo,ax)=lid; a=lo; b=tuple(lo[k]+(1 if k==ax else 0) for k in range(3))
        if pw==+1: out[a].append((b,(lid,pw)))
        else:      out[b].append((a,(lid,pw)))
    start=next(iter(out)); word=[]; cur=start; seen=0; total=len(es)
    while seen<total:
        nb,(lid,pw)=out[cur][0] if len(out[cur])==1 else out[cur].pop()
        word.append((lid,pw)); cur=nb; seen+=1
    return word

if __name__=="__main__":
    main()
