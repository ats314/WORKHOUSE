#!/usr/bin/env python3
"""
ENGINE_FLUX_shell6_o2_engine2.py -- second-order (O(y^2)) degenerate PT for SU(3) glueball
shells via the geometric Wilson-loop-intermediate engine, EXACT rational SU(3)
Haar amplitudes (multi-link, built on certified su3_moments_ext).

Convention (pinned vs certified su3_domino_d3):
  H = H0 - y W,  W = sum_p (Tr U_p + Tr U_p^dag),  E_link = 2/3.
  Degenerate PT on a shell:  H1 = -W|_P,  H2[a,b] = sum_{m in Q} W[a,m]W[m,b]/(E0-E_m).

Why the OFF-DIAGONAL (splitting-determining) part is EXACT here: two DISTINCT
shell-6 loops are connected at O(y^2) only through genuine simple Wilson-loop
intermediates (higher-irrep / double-flux routes return to the SAME loop ->
diagonal self-energy = common shift only).  apply_plaq keeps BOTH the singlet
(3x3bar->1) and the eps-baryon (3x3->3bar) simple-loop routes; the Haar amplitude
itself (link_terms) carries the full SU(3) group theory.  Calibrated on shell-4
(C-odd hop = 5/612).
"""
import itertools, sys, os
from collections import defaultdict
from fractions import Fraction as F
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
    # process from fewest-term links first to keep partial products small
    term_lists.sort(key=len)
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
    return frozenset((((lo[0]-mn[0],lo[1]-mn[1],lo[2]-mn[2]),ax),pw) for ((lo,ax),pw) in es)
def apply_plaq(es, plaq_word):
    """Simple-loop component of Tr(U_p^eps)|L>.  Per plaquette edge e:
      (a) reverse(e) in L -> singlet 3x3bar->1 : REMOVE; (b) e in L -> eps 3x3->3bar :
      REVERSE; (c) neither -> ADD fundamental.  Octet/sextet (non-simple) dropped."""
    new=set(es)
    for (lid,pw) in plaq_word:
        if (lid,-pw) in new: new.discard((lid,-pw))
        elif (lid,pw) in new: new.discard((lid,pw)); new.add((lid,-pw))
        else: new.add((lid,pw))
    return frozenset(new)

ORIENT=[(0,1),(0,2),(1,2)]
def plaquette_word(corner,o,eps=+1):
    mu,nu=ORIENT[o]; dseq=[2*mu,2*nu,2*mu+1,2*nu+1]
    w,end=steps_to_word(corner,dseq); assert end==corner
    return w if eps==+1 else dagger(w)
def box_plaquettes(extent):
    rng=range(-extent,extent+1)
    return [((x,y,z),o) for x in rng for y in rng for z in rng for o in range(3)]

# ---------------- W action ----------------
_LINK2PLQ={}
def build_plaq_index(extent):
    if extent in _LINK2PLQ: return _LINK2PLQ[extent]
    l2p=defaultdict(list)
    for (corner,o) in box_plaquettes(extent):
        for eps in (+1,-1):
            pw=plaquette_word(corner,o,eps)
            for lid in frozenset(l for (l,_) in pw): l2p[lid].append(pw)
    _LINK2PLQ[extent]=l2p; return l2p

_WCACHE={}
def W_action(L_edges, extent, only_lens=None, skip_lens=()):
    """{m_edges: exact <m|W|L>} over simple-loop fusions; touching plaquettes only.
    only_lens/skip_lens filter intermediate length BEFORE the (sometimes costly) Haar
    integral -- lets H2 skip the first-order same-shell eps fusions."""
    sl=tuple(sorted(skip_lens)); ol=tuple(sorted(only_lens)) if only_lens is not None else None
    ck=(L_edges, extent, ol, sl)
    if ck in _WCACHE: return _WCACHE[ck]
    l2p=build_plaq_index(extent); Lw=edges_to_word(L_edges)
    touch=set()
    for (lid,_) in L_edges:
        for pw in l2p.get(lid,()): touch.add(tuple(pw))
    out=defaultdict(lambda:F(0))
    for pw in touch:
        pw=list(pw); m=apply_plaq(L_edges,pw)
        if m is None or not is_simple_loop(m): continue
        lm=len(m)
        if (ol is not None and lm not in ol) or lm in sl: continue
        amp=haar_loops([dagger(edges_to_word(m)), pw, Lw])
        if amp!=0: out[m]+=amp
    out=dict(out); _WCACHE[ck]=out; return out

# ---------------- degenerate PT on a shell ----------------
def shell_states(shapes):
    edges=[edgeset((0,0,0),s) for s in shapes]
    cmap={canon_edges(e):i for i,e in enumerate(edges)}
    return edges, cmap

def build_H1_H2(shape_edges, cmap, shell_len, E0, extent, progress=False):
    N=len(shape_edges)
    H1=[[F(0)]*N for _ in range(N)]; H2=[[F(0)]*N for _ in range(N)]
    for j in range(N):
        if progress: print(f"    column {j+1}/{N}",flush=True)
        # first hop: keep first-order (len==shell) AND second-order (len!=shell)
        for m,amp_mj in W_action(shape_edges[j], extent).items():
            lm=len(m); ck=canon_edges(m)
            if lm==shell_len:
                if ck in cmap: H1[cmap[ck]][j]+= -amp_mj   # H1 = -W|_P
                continue
            denom=E0 - lm*F(2,3)
            for Lp,amp_pm in W_action(m, extent, only_lens=(shell_len,)).items():
                ck2=canon_edges(Lp)
                if ck2 in cmap: H2[cmap[ck2]][j]+= amp_pm*amp_mj/denom
    return H1,H2

def H2_element(ket_edges, bra_edges, shell_len, E0, extent):
    tot=F(0)
    for m,amp_mk in W_action(ket_edges, extent, skip_lens=(shell_len,)).items():
        denom=E0 - len(m)*F(2,3)
        amp_bm=W_action(m, extent, only_lens=(shell_len,)).get(bra_edges, F(0))
        if amp_bm!=0: tot+=amp_bm*amp_mk/denom
    return tot

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

# ---------------- calibration + drivers ----------------
def calibrate_shell4():
    print("="*72,"\nSHELL-4 CALIBRATION: C-odd off-diagonal hop must equal 5/612",flush=True)
    print("="*72)
    pa=edgeset((0,0,0),[0,2,1,3]); pb=edgeset((1,0,0),[0,2,1,3])
    dag=lambda es:frozenset((lid,-pw) for (lid,pw) in es)
    EXT=2; basis=[pa, dag(pa), pb, dag(pb)]
    H2=[[H2_element(basis[j],basis[i],4,F(8,3),EXT) for j in range(4)] for i in range(4)]
    he=(H2[2][0]+H2[2][1]+H2[3][0]+H2[3][1])/2
    ho=(H2[2][0]-H2[2][1]-H2[3][0]+H2[3][1])/2
    print(f"  C-even connected hop = {he}  (su3_domino as-written: -481/612)")
    print(f"  C-odd  connected hop = {ho}  (su3_domino certified: +/-5/612)")
    gate("shell-4 C-odd hop magnitude == 5/612", abs(ho)==F(5,612))
    gate("shell-4 C-even connected hop == -481/612", he==F(-481,612))
    return he,ho

def compute_shell6(extent=2, dump='/tmp/shell6_exact.pkl', progress=True):
    SH=shapes6(); shape_edges,cmap=shell_states(SH)
    print(f"  shell-6 shapes: {len(SH)}; building H1,H2 (extent={extent})...",flush=True)
    H1,H2=build_H1_H2(shape_edges,cmap,6,F(4),extent,progress=progress)
    import pickle
    pickle.dump({'H1':[[str(x) for x in r] for r in H1],
                 'H2':[[str(x) for x in r] for r in H2],'SH':SH}, open(dump,'wb'))
    print(f"  saved -> {dump}",flush=True)
    return SH,H1,H2

def main():
    calibrate_shell4()
    print("="*72,"\nSHELL-6 H1,H2",flush=True); print("="*72)
    SH,H1,H2=compute_shell6(2)
    nz1=[abs(H1[a][b]) for a in range(len(SH)) for b in range(len(SH)) if H1[a][b]!=0]
    print(f"  |H1| nonzero: {sorted(set(str(x) for x in nz1))} (#{len(nz1)}; expect 96 at 1/3)")
    nz2=sum(1 for a in range(len(SH)) for b in range(len(SH)) if a!=b and H2[a][b]!=0)
    print(f"  H2 off-diag nonzero: {nz2}; GATES {sum(p for _,p in PASS)}/{len(PASS)}")

if __name__=="__main__":
    main()
