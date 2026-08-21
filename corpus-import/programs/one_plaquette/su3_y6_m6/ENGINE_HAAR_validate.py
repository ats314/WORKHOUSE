import importlib.util as iu, sys
sys.path.insert(0,'/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6')
# reference: their fusion-tree census
lc=iu.spec_from_file_location('lc','/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6/ENGINE_Y6_su3_local_channel_census.py')
LC=iu.module_from_spec(lc); lc.loader.exec_module(LC)
# mine: weight-blocked GF(p) engine
we=iu.spec_from_file_location('W','/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6/ftw.py'); W=iu.module_from_spec(we); we.loader.exec_module(W)
import numpy as np
p=2_000_003  # prime; singlet dim = nullspace rank of Casimir over GF(p)

def their_mult(a,b):
    # total singlet (0,0) multiplicity for family (a,b): fuse a fundamentals then b antifundamentals
    tok=tuple([1]*a+[-1]*b)
    # replicate paths() final (0,0) multiplicity (order-independent for the total)
    import collections
    states={(0,0):collections.Counter({():1})}
    for t in tok:
        nxt=collections.defaultdict(collections.Counter)
        for ir,hs in states.items():
            for ir2 in LC.fuse(ir,t):
                for h,m in hs.items(): nxt[ir2][h]+=m
        states=nxt
    return sum(states.get((0,0),collections.Counter()).values())

def my_dim(a,b):
    eps=tuple([1]*a+[-1]*b)
    KER=W.ker_modp(p)
    W0,w0idx=W.w0_states(eps); 
    if not W0: return 0
    c2f=(4*W.inv(3,p))%p
    Cf=W.cas_block(eps,range(len(eps)),p,W0,w0idx,c2f,KER)
    Bn=W.nullspace_modp(Cf,p)
    return Bn.shape[1]

print("family (a,b)  their_mult  my_dim  match  [det-sector?]")
allok=True
fams=[]
for tot in range(2,9):
    for a in range(0,tot+1):
        b=tot-a
        if (a-b)%3!=0: continue
        fams.append((a,b))
for (a,b) in fams:
    tm=their_mult(a,b); md=my_dim(a,b); ok=(tm==md); allok&=ok
    det = "det" if (a-b)!=0 else ""
    print(f"  ({a},{b})        {tm:>4}      {md:>4}    {ok}   {det}")
print("\nDEGREE-8 HAAR SINGLET-DIM GATE:", "ALL PASS" if allok else "FAIL")
