#!/usr/bin/env python3
"""
ENGINE_SHELL6_o2.py -- second-order (O(y^2)) degenerate PT for the SU(3) glueball
shells, geometric Wilson-loop-intermediate engine, EXACT rational amplitudes.

Convention pinned by reproducing the certified shell-4 constants (su3_domino_d3):
  H = H0 - y W,  W = sum_p (Tr U_p + Tr U_p^dag),  E_link = 2/3.
  Degenerate PT on a shell:  H1 = -W|_P ,  H2[a,b] = sum_{m in Q} W[a,m]W[m,b]/(E0-E_m).
All matrix elements are exact SU(3) Haar integrals (multi-link, su3_moments_ext).

Claims about the OFF-DIAGONAL splitting are exact in this engine because distinct
shell loops are connected only through genuine Wilson-loop intermediates (higher-
irrep/double-flux routes return to the same loop -> diagonal shift only).  The
diagonal self-energy is captured only at the Wilson-loop-intermediate level (its
higher-irrep completion is a common shift, label noted).  Calibrated on shell-4.
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

# ---------------- lattice / Haar primitives ----------------
def edge_to_link(site,d):
    ax=d//2
    if d%2==0: lo=site; pw=+1
    else: lo=(site[0]+DIRS[d][0],site[1]+DIRS[d][1],site[2]+DIRS[d][2]); pw=-1
    return (lo,ax),pw
def steps_to_word(start,dseq):
    word=[]; pos=start
    for d in dseq:
        lid,pw=edge_to_link(pos,d); word.append((lid,pw))
        pos=(pos[0]+DIRS[d][0],pos[1]+DIRS[d][1],pos[2]+DIRS[d][2])
    return word,pos
def dagger(word): return [(lid,-pw) for (lid,pw) in reversed(word)]

_HCACHE={}
def haar_loops(words):
    key=tuple(tuple(w) for w in words)
    if key in _HCACHE: return _HCACHE[key]
    nv=0; linkfac=defaultdict(lambda:([],[]))
    for w in words:
        Lw=len(w); ids=list(range(nv,nv+Lw)); nv+=Lw
        for t,(lid,pw) in enumerate(w):
            a,b=ids[t],ids[(t+1)%Lw]; us,bs=linkfac[lid]
            if pw==+1: us.append((a,b))
            else: bs.append((b,a))
    term_lists=[]
    for (us,bs) in linkfac.values():
        tl=link_terms(us,bs)
        if not tl: _HCACHE[key]=F(0); return F(0)
        term_lists.append(tl)
    tot=F(0)
    for combo in itertools.product(*term_lists):
        coeff=F(1); cons=()
        for (c_,k_) in combo: coeff*=c_; cons=cons+k_
        if coeff!=0: tot+=eval_term(coeff,cons,nv)
    _HCACHE[key]=tot; return tot

# ---------------- edge-set geometry ----------------
def edgeset(start,dseq):
    s=set(); pos=start
    for d in dseq:
        lid,pw=edge_to_link(pos,d); s.add((lid,pw)); pos=tuple(pos[k]+DIRS[d][k] for k in range(3))
    return frozenset(s)
def link_endpoints(lid):
    (lo,ax)=lid; hi=tuple(lo[k]+(1 if k==ax else 0) for k in range(3)); return lo,hi
def is_simple_loop(es):
    if len(es)==0: return False
    deg=defaultdict(int); links=set()
    for (lid,pw) in es:
        if lid in links: return False
        links.add(lid); a,b=link_endpoints(lid)
        if pw==+1: deg[a]+=1; deg[b]-=1
        else: deg[a]-=1; deg[b]+=1
    if any(d!=0 for d in deg.values()): return False
    # single cycle: walk
    nxt={}
    for (lid,pw) in es:
        a,b=link_endpoints(lid)
        if pw==+1: nxt[a]=(b,(lid,pw))
        else: nxt[b]=(a,(lid,pw))
    start=next(iter(nxt)); cur=start; cnt=0
    while True:
        if cur not in nxt: return False
        cur=nxt[cur][0]; cnt+=1
        if cur==start: break
        if cnt>len(es): return False
    return cnt==len(es)
def edges_to_word(es):
    nxt={}
    for (lid,pw) in es:
        a,b=link_endpoints(lid)
        if pw==+1: nxt[a]=(b,(lid,pw))
        else: nxt[b]=(a,(lid,pw))
    start=next(iter(nxt)); cur=start; word=[]
    while True:
        b,lp=nxt[cur]; word.append(lp); cur=b
        if cur==start: break
    return word
def canon_edges(es):
    sites=[link_endpoints(lid)[0] for (lid,pw) in es]
    mn=(min(s[0] for s in sites),min(s[1] for s in sites),min(s[2] for s in sites))
    return frozenset((((lo[0]-mn[0],lo[1]-mn[1],lo[2]-mn[2]),ax),pw)
                     for ((lo,ax),pw) in es)
def apply_plaq(es, plaq_word):
    """Simple-loop component of Tr(U_p^eps)|L>.  Per plaquette edge e:
      (a) reverse(e) in L  -> 3 x 3bar = 1 (+) 8 : keep singlet, REMOVE the edge;
      (b) e in L           -> 3 x 3   = 3bar (+) 6 : keep 3bar, REVERSE the edge (eps route);
      (c) neither          -> add e as a fresh fundamental.
    The octet/sextet (higher-irrep) components are non-simple-loop and are dropped
    here (they feed only the diagonal self-energy / common shift, not the splitting).
    Returns the resulting edge-set (validate simple-loop + amplitude downstream)."""
    new=set(es)
    for (lid,pw) in plaq_word:
        if (lid,-pw) in new: new.discard((lid,-pw))                 # (a) singlet cancel
        elif (lid,pw) in new: new.discard((lid,pw)); new.add((lid,-pw))  # (b) eps reverse
        else: new.add((lid,pw))                                     # (c) fresh fundamental
    return frozenset(new)

ORIENT=[(0,1),(0,2),(1,2)]
def plaquette_word(corner,o,eps=+1):
    mu,nu=ORIENT[o]; dseq=[2*mu,2*nu,2*mu+1,2*nu+1]
    w,end=steps_to_word(corner,dseq); assert end==corner
    return w if eps==+1 else dagger(w)
def box_plaquettes(extent):
    rng=range(-extent,extent+1)
    return [((x,y,z),o) for x in rng for y in rng for z in rng for o in range(3)]

# ---------------- W action: <m|W|L> over Wilson-loop fusions ----------------
_LINK2PLQ={}; _PLQWORDS={}
def build_plaq_index(extent):
    """map each lattice link -> list of plaquette words (both eps) whose boundary contains it."""
    key=extent
    if key in _LINK2PLQ: return _LINK2PLQ[key]
    l2p=defaultdict(list)
    for (corner,o) in box_plaquettes(extent):
        for eps in (+1,-1):
            pw=plaquette_word(corner,o,eps)
            links=frozenset(lid for (lid,_) in pw)
            for lid in links: l2p[lid].append(pw)
    _LINK2PLQ[key]=l2p; return l2p

_WCACHE={}
def W_action(L_edges, extent):
    """{m_edges: exact <m|W|L>} over simple-loop fusions; only plaquettes touching L."""
    ck=(L_edges, extent)
    if ck in _WCACHE: return _WCACHE[ck]
    l2p=build_plaq_index(extent)
    Lw=edges_to_word(L_edges)
    touch=set()
    for (lid,_) in L_edges:
        for pw in l2p.get(lid,()): touch.add(tuple(pw))
    out=defaultdict(lambda:F(0))
    for pw in touch:
        pw=list(pw)
        m=apply_plaq(L_edges,pw)
        if m is None or not is_simple_loop(m): continue
        amp=haar_loops([dagger(edges_to_word(m)), pw, Lw])
        if amp!=0: out[m]+=amp
    out=dict(out); _WCACHE[ck]=out; return out

# ---------------- degenerate PT on a shell ----------------
def shell_states(shapes):
    """shapes: list of dseq tuples. Return canonical-edge -> index, and origin edge-sets."""
    edges=[edgeset((0,0,0),s) for s in shapes]
    cmap={canon_edges(e):i for i,e in enumerate(edges)}
    return edges, cmap

def build_H1_H2(shape_edges, cmap, shell_len, E0, extent):
    N=len(shape_edges)
    H1=[[F(0)]*N for _ in range(N)]
    H2=[[F(0)]*N for _ in range(N)]
    for j in range(N):
        a1=W_action(shape_edges[j], extent)
        for m,amp_mj in a1.items():
            lm=len(m)
            ck=canon_edges(m)
            if lm==shell_len and ck in cmap:
                # first-order: H1 = -W|_P
                i=cmap[ck]; H1[i][j]+= -amp_mj
                continue
            if lm==shell_len:   # length-6 but not one of our shapes (shouldn't happen in-model)
                continue
            denom=E0 - lm*F(2,3)
            a2=W_action(m, extent)
            for Lp,amp_pm in a2.items():
                if len(Lp)!=shell_len: continue
                ck2=canon_edges(Lp)
                if ck2 not in cmap: continue
                i=cmap[ck2]
                H2[i][j]+= amp_pm*amp_mj/denom
    return H1,H2

# =====================================================================
def shapes6():
    r=set(); canon=lambda s:min(tuple(list(s)[i:]+list(s)[:i]) for i in range(len(s)))
    def dfs(seq,pos,vis):
        if len(seq)==6:
            if pos==(0,0,0) and neg(seq[-1])!=seq[0]: r.add(canon(seq))
            return
        for d in range(6):
            if seq and neg(seq[-1])==d: continue
            p=tuple(pos[k]+DIRS[d][k] for k in range(3))
            if p==(0,0,0):
                if len(seq)+1!=6: continue
            elif p in vis: continue
            dfs(seq+[d],p,vis|{p})
    dfs([], (0,0,0),{(0,0,0)}); return sorted(r)

def H2_element(ket_edges, bra_edges, shell_len, E0, extent):
    """exact <bra| W Q(E0-H0)^-1 Q W |ket> over simple-loop intermediates (len!=shell_len)."""
    tot=F(0)
    for m,amp_mk in W_action(ket_edges, extent).items():
        lm=len(m)
        if lm==shell_len: continue
        denom=E0 - lm*F(2,3)
        amp_bm=W_action(m, extent).get(bra_edges, F(0))
        if amp_bm!=0: tot+=amp_bm*amp_mk/denom
    return tot

def calibrate_shell4():
    print("="*72,"\nSHELL-4 CALIBRATION: off-diagonal hop between neighbour plaquettes")
    print("  (validates the eps-route engine vs su3_domino: C-odd hop must be 5/612)")
    print("="*72)
    pa=edgeset((0,0,0),[0,2,1,3])               # xy plaquette at origin
    pb=edgeset((1,0,0),[0,2,1,3])               # xy plaquette at +x (shares the x=1 +y link)
    dag=lambda es:frozenset((lid,-pw) for (lid,pw) in es)
    EXT=2
    # 4x4 second-order block on {pa, pa^dag, pb, pb^dag}
    basis=[pa, dag(pa), pb, dag(pb)]
    H2=[[H2_element(basis[j],basis[i],4,F(8,3),EXT) for j in range(4)] for i in range(4)]
    # C-even/odd combos for each plaquette: e=(p+p^dag)/sqrt2, o=(p-p^dag)/sqrt2
    # hop_even = <pb_e|H2|pa_e>, hop_odd = <pb_o|H2|pa_o>
    he=(H2[2][0]+H2[2][1]+H2[3][0]+H2[3][1])/2
    ho=(H2[2][0]-H2[2][1]-H2[3][0]+H2[3][1])/2
    print(f"  C-even connected hop  = {he}   (su3_domino as-written Thm6.2: -481/612)")
    print(f"  C-odd  connected hop  = {ho}   (su3_domino certified:        +/-5/612)")
    gate("shell-4 C-odd hop magnitude == 5/612 (off-diagonal engine EXACT, eps-route)",
         abs(ho)==F(5,612))
    gate("shell-4 C-even connected hop == -481/612 (vacuum route correctly excluded)",
         he==F(-481,612))
    return he,ho

def compute_shell6(extent=2, dump='/tmp/shell6_exact.pkl'):
    SH=shapes6(); shape_edges,cmap=shell_states(SH)
    H1,H2=build_H1_H2(shape_edges,cmap,6,F(4),extent)
    import pickle
    pickle.dump({'H1':[[str(x) for x in r] for r in H1],
                 'H2':[[str(x) for x in r] for r in H2],'SH':SH}, open(dump,'wb'))
    return SH,H1,H2

def main():
    calibrate_shell4()
    print("="*72,"\nSHELL-6 H1,H2 (exact off-diagonal)")
    print("="*72)
    SH,H1,H2=compute_shell6(2)
    nz1=[abs(H1[a][b]) for a in range(len(SH)) for b in range(len(SH)) if H1[a][b]!=0]
    print(f"  |H1| nonzero: {sorted(set(str(x) for x in nz1))}  (#{len(nz1)}; expect 96 at 1/3)")
    nz2=sum(1 for a in range(len(SH)) for b in range(len(SH)) if a!=b and H2[a][b]!=0)
    print(f"  H2 off-diagonal nonzero entries: {nz2}")
    print(f"  saved -> /tmp/shell6_exact.pkl ; GATES {sum(p for _,p in PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
