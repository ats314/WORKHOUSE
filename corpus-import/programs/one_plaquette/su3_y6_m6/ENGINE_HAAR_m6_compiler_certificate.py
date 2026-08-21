"""Degree-8 SU(3) Haar tensor compiler — validation certificate for the m6 pipeline.
Cross-checks the weight-blocked GF(p) singlet projector (ftw.py) against the bundle's
independent fusion-tree census (ENGINE_Y6_su3_local_channel_census.py): singlet dimensions and
cumulative-Casimir histories, for every triality family through degree 8 (incl determinant
sectors). Hard-gated. Does NOT compute m6 (global folded contraction is the remaining HPC stage)."""
import importlib.util as iu, collections, json, hashlib
LCP='/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6/ENGINE_Y6_su3_local_channel_census.py'
lc=iu.spec_from_file_location('lc',LCP); LC=iu.module_from_spec(lc); lc.loader.exec_module(LC)
we=iu.spec_from_file_location('W','/sessions/nice-great-einstein/mnt/THEORY/programs/one_plaquette/su3_y6_m6/ftw.py'); W=iu.module_from_spec(we); we.loader.exec_module(W)
p=2_000_003; GATES=[]
def gate(n,c,d=""):
    assert c, f"FAIL {n} {d}"; GATES.append({"gate":n,"pass":True,"detail":d}); print(f"PASS {n} {d}")
def their_hist(tok):
    states={(0,0):collections.Counter({():1})}
    for t in tok:
        nxt=collections.defaultdict(collections.Counter)
        for ir,hs in states.items():
            for ir2 in LC.fuse(ir,t):
                en=LC.c2num(ir2)
                for h,m in hs.items(): nxt[ir2][h+(en,)]+=m
        states=nxt
    return collections.Counter({h:m for h,m in states.get((0,0),{}).items()})
def my_hist(tok):
    cuts=tuple(tuple(range(j+1)) for j in range(len(tok)))
    lib=W.link_lib_w(tok,cuts,p,W.ker_modp(p),{})
    out=collections.Counter()
    if lib in (None,[]): return out
    for hist,U,Gi in lib: out[tuple(int(3*c) for c in hist)]+=U.shape[-1]
    return out
# Gate 1: singlet dimension per family (a,b), all triality families through degree 8
fams=[(a,t-a) for t in range(2,9) for a in range(t+1) if (a-(t-a))%3==0]
famres={}
for (a,b) in fams:
    tok=tuple([1]*a+[-1]*b); tm=sum(their_hist(tok).values()); md=sum(my_hist(tok).values())
    famres[f"({a},{b})"]={"mult":tm,"my_dim":md,"determinant":a!=b}
    gate(f"singlet_dim_({a},{b})", tm==md, f"mult={tm}")
# Gate 2: full Casimir-history multiset agreement, representative tokens incl degree-8 det
toks=[(1,-1),(1,1,1),(1,1,-1,-1),(1,1,1,1,-1),(1,1,1,-1,-1,-1),(1,1,1,1,1,-1,-1),(1,1,1,1,-1,-1,-1,-1),(1,1,1,1,1,1,1,-1)]
for tok in toks:
    gate(f"casimir_history_deg{len(tok)}_{''.join('p' if x>0 else 'm' for x in tok)}", their_hist(tok)==my_hist(tok), f"channels={sum(their_hist(tok).values())}")
cert={"title":"Degree-8 SU(3) Haar tensor compiler validation (m6 pipeline next stage)",
 "date":"2026-06-15",
 "method":"weight-blocked GF(p) singlet projector (ftw.py) vs independent fusion-tree census (ENGINE_Y6_su3_local_channel_census.py)",
 "families_through_degree_8":famres,
 "n_gates":len(GATES),"all_pass":all(g["pass"] for g in GATES),
 "validated":"singlet color multiplicity AND cumulative-Casimir resolvent histories, all triality families incl determinant sectors (7,1)/(1,7)/(6,0)/(0,6)/(5,2)/(2,5)/(4,1)/(1,4)/(3,0)/(0,3) through degree 8",
 "fold_identity":"E6 32-monomial scalar fold validated by ENGINE_Y6_su3_scalar_fold_formula.py (12 matrix models)",
 "remaining_for_m6":"global folded contraction: sum over ~1.22M ordered six-insertion geometries of (per-link Haar tensor x resolvent denominators) -> chain moments S -> E6=m6; external-memory/HPC scale; per-link layer now validated",
 "m6_value":"NOT computed (no value fabricated)",
 "gates":GATES}
json.dump(cert,open('/tmp/y6/CERT_HAAR_m6_compiler_certificate.json','w'),indent=2)
print(f"\nALL {len(GATES)} GATES PASS — degree-8 Haar tensor compiler validated against the independent fusion-tree census.")
print("m6 NOT claimed (global contraction is HPC).")
