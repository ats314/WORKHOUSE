import importlib.util as iu, collections
lc=iu.spec_from_file_location('lc','/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6/ENGINE_Y6_su3_local_channel_census.py')
LC=iu.module_from_spec(lc); lc.loader.exec_module(LC)
we=iu.spec_from_file_location('W','/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6/ftw.py'); W=iu.module_from_spec(we); we.loader.exec_module(W)
from fractions import Fraction as F
p=2_000_003

def their_histories(tok):
    # cumulative irrep Casimir (c2num) after EVERY fusion step, for singlet-ending paths
    states={(0,0):collections.Counter({():1})}
    for t in tok:
        nxt=collections.defaultdict(collections.Counter)
        for ir,hs in states.items():
            for ir2 in LC.fuse(ir,t):
                en=LC.c2num(ir2)
                for h,m in hs.items(): nxt[ir2][h+(en,)]+=m
        states=nxt
    out=collections.Counter()
    for h,m in states.get((0,0),{}).items(): out[h]+=m
    return out  # {history tuple of c2num : multiplicity}

def my_histories(tok):
    # weight-blocked engine: cut after every leg; history = Casimir eigenvalues (Fraction) -> *3 to match c2num
    eps=tok
    cuts=tuple(tuple(range(j+1)) for j in range(len(eps)))  # prefixes after legs 1..n
    KER=W.ker_modp(p)
    lib=W.link_lib_w(eps,cuts,p,KER,{})
    if lib in (None,[]): return collections.Counter()
    out=collections.Counter()
    for hist,U,Gi in lib:
        # hist = tuple of Fraction Casimirs at each cut; the last cut (full set) must be 0 (singlet)
        c2nums=tuple(int(3*c) for c in hist)
        kk=U.shape[-1]
        out[c2nums]+=kk
    return out

# test a battery incl the degree-8 determinant token
toks=[(1,-1),(1,1,1),(1,1,-1,-1),(1,1,1,1,-1),(1,1,1,-1,-1,-1),(1,1,1,1,1,-1,-1),(1,1,1,1,-1,-1,-1,-1),(1,1,1,1,1,1,1,-1)]
allok=True
for tok in toks:
    th=their_histories(tok); mh=my_histories(tok)
    # compare final-cut singlet multiplicity and the multiset of FULL histories
    th_full=collections.Counter({h:m for h,m in th.items()})
    ok = (th_full==mh)
    allok&=ok
    a=sum(1 for x in tok if x==1); b=len(tok)-a
    print(f"tok deg{len(tok)} (a,b)=({a},{b}): their_paths={sum(th.values())} my_dim={sum(mh.values())} histories_match={ok}")
    if not ok and len(tok)<=4:
        print("  their:",dict(th)); print("  mine :",dict(mh))
print("\nENERGY/CASIMIR-HISTORY GATE:", "ALL PASS" if allok else "PARTIAL (see above)")
