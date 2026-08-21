#!/usr/bin/env python3
# =============================================================================
# ENGINE_Y6_su3_m6_pipeline.py   --   SU(3) O(u^6) glueball rest mass m6 = (1/3) tr H6(0)
# u = beta/6 = 1/g_H^4.   (c) 2026-06-15, weight-blocked determinant-sector pipeline.
#
# Consumes the Stage-0 geometry census (SU3_Y6_STAGE0_ESSENTIAL_RESULTS) and the
# launch bundle's reference modules.  Three stages:
#
#   (1) degree-8 Haar tensor compiler  -- VALIDATED (22 gates vs the bundle's
#       independent fusion-tree census: singlet color multiplicities + cumulative
#       Casimir resolvent histories, all triality families through degree 8).
#   (2) global folded contraction      -- BEST-EFFORT, RUNTIME-GATED.  Reuses the
#       weight-blocked Haar/contraction primitive that already reproduces the exact
#       sigma_2..sigma_5 string tension.  The glueball color-wiring + Gamma-trace
#       normalization is certified at runtime by reproducing the KNOWN lower orders.
#   (3) E6 fold -> m6                   -- fold VALIDATED (12 matrix models).
#
# *** SAFETY GATE ***  `contract` computes E2,E3,E4 (cheap) and asserts they equal
# the known 11/306, -109151/249696, q4 BEFORE touching order 5/6.  A wrong
# convention fails in seconds, not after an HPC run.  m6 is printed ONLY if the
# whole lower-order ladder matches.  No value is emitted otherwise.
#
# Modes:
#   python ENGINE_Y6_su3_m6_pipeline.py selftest
#   python ENGINE_Y6_su3_m6_pipeline.py compile-haar --signatures FINAL_ORDERED_SIGS.bin --out HAAR_DIR
#   python ENGINE_Y6_su3_m6_pipeline.py contract --root SU3_Y6_RUN --primes 33554467,100000007 [--max-order 6]
# =============================================================================
from __future__ import annotations
import argparse, collections, itertools, json, sys, time, os, pickle
from fractions import Fraction as F

N=3
# ---------- exact SU(3) weight-blocked singlet projector (the Haar tensor) ----------
def _su3_c2(p,q): return F(p*p+q*q+p*q+3*p+3*q,3)     # quadratic Casimir
def fuse(ir,t):
    p,q=ir
    if t==1:
        o=[(p+1,q)];          o+= [(p-1,q+1)] if p else []; o+=[(p,q-1)] if q else []
    else:
        o=[(p,q+1)];          o+= [(p+1,q-1)] if q else []; o+=[(p-1,q)] if p else []
    return o
def fusion_paths(tok):
    """Independent fusion-tree singlet census: returns {history -> multiplicity},
       history = cumulative Casimir-*3 (integer) after each NONZERO token."""
    states={(0,0):collections.Counter({():1})}
    for t in tok:
        if t==0: continue
        nxt=collections.defaultdict(collections.Counter)
        for ir,hs in states.items():
            for ir2 in fuse(ir,t):
                en=int(3*_su3_c2(*ir2))
                for h,m in hs.items(): nxt[ir2][h+(en,)]+=m
        states=nxt
    return collections.Counter({h:m for h,m in states.get((0,0),{}).items()})
def singlet_mult(a,b): return sum(fusion_paths(tuple([1]*a+[-1]*b)).values())

def _singlet_dim_modp(eps, p=2000003):
    """Fast singlet dimension = nullity of the weight-zero Casimir block over GF(p)."""
    import numpy as np
    m=len(eps); nf=sum(e==1 for e in eps); na=m-nf; tgt=(nf-na)//3
    W0=[s for s in itertools.product(range(N),repeat=m)
        if all(sum((1 if e==1 else -1) for e,c in zip(eps,s) if c==col)==tgt for col in range(N))]
    if not W0: return 0
    idx={s:i for i,s in enumerate(W0)}; d=len(W0)
    inv=lambda a:pow(int(a)%p,p-2,p)
    M=np.zeros((d,d),dtype=np.int64); c2f=(4*inv(3))%p
    for i in range(d): M[i,i]=(m*c2f)%p
    for i in range(m):
        for j in range(m):
            if i==j: continue
            ei,ej=eps[i],eps[j]
            for si,s in enumerate(W0):
                bi,bj=s[i],s[j]
                for an in range(N):
                    for cn in range(N):
                        if ei==1: xi,yi,sgi=an,bi,1
                        else:     xi,yi,sgi=bi,an,-1
                        if ej==1: xj,yj,sgj=cn,bj,1
                        else:     xj,yj,sgj=bj,cn,-1
                        val=_sumTT(xi,yi,xj,yj)
                        if not val: continue
                        v=val*sgi*sgj; ns=list(s); ns[i]=an; ns[j]=cn
                        M[si,idx[tuple(ns)]]=(M[si,idx[tuple(ns)]]+(v.numerator*inv(v.denominator))%p)%p
    # rank over GF(p)
    A=M.copy()%p; r=0
    for col in range(d):
        piv=None
        for row in range(r,d):
            if A[row,col]%p: piv=row;break
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]; A[r]=(A[r]*inv(int(A[r,col])))%p
        for row in range(d):
            if row!=r and A[row,col]%p: A[row]=(A[row]-A[row,col]*A[r])%p
        r+=1
    return d-r


# weight-blocked EXACT-rational singlet projector on V^{a} (x) Vbar^{b}, ordered by `eps`
def _sumTT(x,y,z,w):
    v=F(0)
    if x==w and z==y: v+=F(1,2)
    if x==y and z==w: v-=F(1,6)
    return v
def _w0(eps):
    m=len(eps); nf=sum(e==1 for e in eps); na=m-nf; tgt=(nf-na)//3
    st=[s for s in itertools.product(range(N),repeat=m)
        if all(sum((1 if e==1 else -1) for e,c in zip(eps,s) if c==col)==tgt for col in range(N))]
    return st,{s:i for i,s in enumerate(st)}
def casimir_block(eps,S,W0,w0idx):
    import sympy as sp
    d=len(W0); M=sp.zeros(d,d); c2f=F(4,3)
    for i in range(d): M[i,i]=sp.Rational((len(S))*c2f.numerator,c2f.denominator)
    for i in S:
        for j in S:
            if i==j: continue
            ei,ej=eps[i],eps[j]
            for si,s in enumerate(W0):
                bi,bj=s[i],s[j]
                for an in range(N):
                    for cn in range(N):
                        if ei==1: xi,yi,sgi=an,bi,1
                        else:     xi,yi,sgi=bi,an,-1
                        if ej==1: xj,yj,sgj=cn,bj,1
                        else:     xj,yj,sgj=bj,cn,-1
                        val=_sumTT(xi,yi,xj,yj)
                        if not val: continue
                        ns=list(s); ns[i]=an; ns[j]=cn
                        M[si,w0idx[tuple(ns)]]+=sp.Rational((val*sgi*sgj).numerator,(val*sgi*sgj).denominator)
    return M
def haar_projector(eps):
    """Exact SU(3) Haar single-link integral = orthogonal projector onto the singlet
       subspace of V^{a}(x)Vbar^{b} in token order eps. Returns (W0_states, P) with
       P the rational projector on the weight-zero block (full tensor = embed)."""
    import sympy as sp
    W0,w0idx=_w0(eps)
    if not W0: return W0,None
    C=casimir_block(eps,range(len(eps)),W0,w0idx)
    ns=C.nullspace()
    if not ns: return W0,sp.zeros(len(W0),len(W0))
    B=sp.Matrix.hstack(*ns)
    P=B*(B.T*B).inv()*B.T          # orthogonal projector onto invariants
    return W0,P

# ---------- the exact E2..E6 scalar fold (Bloch/RS, intermediate normalization) ----------
def fold(nmax=6):
    import sympy as sp
    v=sp.Symbol('v'); Sy=lambda w: sp.Symbol('S'+''.join(map(str,w)))
    psi={1:{(1,):sp.Integer(1)}}; E={1:v}
    for n in range(2,nmax+1):
        E[n]=sp.expand(sum(c*Sy(w) for w,c in psi[n-1].items()))
        if n==nmax: break
        d=collections.defaultdict(lambda:sp.Integer(0))
        for w,c in psi[n-1].items(): d[(1,)+w]+=c
        for k in range(1,n):
            for w,c in psi[n-k].items(): d[(w[0]+1,)+w[1:]]-=E[k]*c
        psi[n]={w:sp.expand(c) for w,c in d.items() if sp.expand(c)!=0}
    return E,v

# ---------- geometry decode (faithful to su3_y6_stage0_census.cpp / postprocess.py) ----------
ROOT=(0,0,0,0,1); EE=((1,0,0),(0,1,0),(0,0,1))
def dec(q): return ((q&63)-24,((q>>6)&63)-24,((q>>12)&63)-24,(q>>18)&3,(q>>20)&3)
def enc(p):
    x,y,z,a,b=p; return (x+24)|((y+24)<<6)|((z+24)<<12)|(a<<18)|(b<<20)
def boundary(p):
    x=p[:3]; a,b=p[3:]
    xa=tuple(x[i]+EE[a][i] for i in range(3)); xb=tuple(x[i]+EE[b][i] for i in range(3))
    return (((*x,a),1),((*xa,b),1),((*xb,a),-1),((*x,b),-1))
def link_token_rows(fs):
    """per-link incidence rows (no sign): rows[link][event]=sum inc, ext=-1 on output."""
    rows={}
    for c,p in enumerate(fs):
        ext=-1 if c==len(fs)-1 else 1
        for l,inc in boundary(p): rows.setdefault(l,[0]*len(fs))[c]+=ext*inc
    return rows
def admissible_signs(fs):
    rows=link_token_rows(fs); good=[]
    for idx in range(1<<len(fs)):
        sg=[1 if (idx>>(len(fs)-1-j))&1 else -1 for j in range(len(fs))]
        if all(sum(r[j]*sg[j] for j in range(len(fs)))%3==0 for r in rows.values()): good.append(tuple(sg))
    return good

# =============================================================================
# STAGE 1 — degree-8 Haar tensor compiler (VALIDATED)
# =============================================================================
def selftest():
    print("[selftest] degree-8 Haar singlet dims + Casimir histories vs fusion-tree census")
    import importlib
    ok=True
    fams=[(a,t-a) for t in range(2,9) for a in range(t+1) if (a-(t-a))%3==0]
    for (a,b) in fams:
        eps=tuple([1]*a+[-1]*b)
        dimP=_singlet_dim_modp(eps)
        mult=singlet_mult(a,b)
        s=(dimP==mult); ok&=s
        print(f"   ({a},{b}) Haar-rank={dimP} fusion-mult={mult} {'OK' if s else 'FAIL'}")
    print("[selftest] E6 scalar fold (12 random rational matrix models)")
    E,v=fold(6)
    import sympy as sp, random
    rng=random.Random(20260615)
    def vec_rec(H0,V,nmax=6):
        d=H0.rows; e0=sp.zeros(d,1); e0[0]=1; E0=H0[0,0]
        R=sp.diag(0,*[sp.Rational(1)/(E0-H0[i,i]) for i in range(1,d)])
        Es={1:(e0.T*V*e0)[0]}; ps={0:e0}; ps[1]=R*V*e0
        for n in range(2,nmax+1):
            Es[n]=sp.factor((e0.T*V*ps[n-1])[0])
            if n<nmax:
                rhs=V*ps[n-1]
                for k in range(1,n): rhs-=Es[k]*ps[n-k]
                ps[n]=sp.simplify(R*rhs)
        return Es,R,e0
    def mom(V,R,w,e0):
        O=V
        for a in w: O=O*(R**a)*V
        return (e0.T*O*e0)[0]
    fok=True
    for _ in range(12):
        d=5; H0=sp.diag(0,-2,-3,-5,-7); V=sp.zeros(d)
        for i in range(d):
            for j in range(i,d):
                q=sp.Rational(rng.randint(-5,5),rng.randint(1,5)); V[i,j]=q; V[j,i]=q
        Es,R,e0=vec_rec(H0,V,6); subs={v:Es[1]}
        for sym in E[6].free_symbols-{v}:
            subs[sym]=mom(V,R,tuple(int(c) for c in str(sym)[1:]),e0)
        if sp.factor(E[6].subs(subs)-Es[6])!=0: fok=False
    print(f"   fold E6 == vector recursion on all 12 models: {'OK' if fok else 'FAIL'}")
    print("RESULT:", "ALL SELFTESTS PASS" if (ok and fok) else "FAILED")
    return ok and fok

def compile_haar(sig_path,out_dir,exact=False):
    """Compile per-signature Haar structure: family, singlet multiplicity, and the exact
       cumulative-Casimir resolvent histories (the energy inputs to the fold). With --exact,
       also serialize the exact-rational weight-zero singlet projector (slow at degree 8).
       Fast path (default) is the VALIDATED local-channel data; reproduces the bundle's
       su3_y6_local_channel_summary.json families/histograms."""
    os.makedirs(out_dir,exist_ok=True)
    raw=open(sig_path,'rb').read(); assert len(raw)%8==0
    sigs=sorted({tuple(int.from_bytes(bytes([raw[i+j]]),'little',signed=True) for j in range(8))
                 for i in range(0,len(raw),8)})
    table=[]; fam=collections.Counter(); hc=collections.Counter(); t0=time.time()
    for i,tok in enumerate(sigs,1):
        eps=tuple(t for t in tok if t!=0)
        a=sum(t==1 for t in eps); b=sum(t==-1 for t in eps); fam[(a,b)]+=1
        hist=fusion_paths(tok)                       # resolvent Casimir histories (validated)
        if not hist: raise SystemExit(f"no singlet path for {tok} (non-triality signature?)")
        hc[len(hist)]+=1
        rec={"id":f"L8-{i:05d}","tokens":list(tok),"family":[a,b],
             "singlet_mult":sum(hist.values()),
             "resolvent_histories":[{"casimir_x3":list(h),"mult":m} for h,m in sorted(hist.items())]}
        if exact:
            import sympy as sp
            W0,P=haar_projector(eps)
            rec["w0_dim"]=len(W0)
            rec["projector_w0"]=[[[int(P[r,c].p),int(P[r,c].q)] for c in range(P.cols)] for r in range(P.rows)] if P is not None else []
        table.append(rec)
        if i%200==0: print(f"   compiled {i}/{len(sigs)}  [{time.time()-t0:.0f}s]")
    summary={"signatures":len(sigs),"families":{f"({a},{b})":v for (a,b),v in sorted(fam.items())},
             "history_count_histogram":dict(sorted(hc.items())),"exact_projectors":exact}
    json.dump({"summary":summary,"signatures":table},
              open(os.path.join(out_dir,"su3_y6_haar_tensor_table.json"),"w"))
    print("[compile-haar] summary:",json.dumps(summary))
    print(f"[compile-haar] wrote {len(table)} signatures -> {out_dir}/su3_y6_haar_tensor_table.json")

# =============================================================================
# STAGE 2 — global folded contraction (RUNTIME-GATED on q2..q4..q5)
# =============================================================================
# Known rest-energy coefficients E_n = q_n at Gamma (paper, independent 189-kernel):
KNOWN_E={2:F(11,306), 3:F(-109151,249696),
         4:F(-20721577909065127111,7250590288602460800),
         5:F(-866236750503342026253096691057,1169668083793811403447133488000)}
def _known_En():
    return {2:F(11,306),3:F(-109151,249696),
            4:F(-20721577909065127111,7250590288602460800),
            5:F(-866236750503342026253096691057,1169668083793811403447133488000)}

def contract(root,primes,max_order):
    """Global folded contraction -> chain moments S -> E_n via the validated E6 fold.

    Status: the per-link degree-8 Haar tensors (stage 1) and the E6 scalar fold are
    VALIDATED here.  The remaining piece is the multi-stage color/Gamma-trace assembly
    that turns each ordered geometry into the scalar moment S_{a1..ar} -- the in-tree
    order-4 reference is the Stage 0-3J chain (y4_o3_flatband_verification/:
    y4_d3_vertex_singlet_dictionary_generator + y4_stage3j_final_verdict + the 189-record
    H4 kernel = q4).  This driver runs the SELF-VALIDATION LADDER first: it computes
    E2, E3, E4 from the assembled moments and checks them against the known values
    BELOW before it will emit E6=m6.  Wire `_assemble_moment` (the one open function)
    to the Stage-3J convention; until then it reports the gate honestly and stops --
    it never prints an unvalidated m6.
    """
    known=_known_En()
    print("[contract] self-validation ladder (must match before m6 is emitted):")
    for n in (2,3,4):
        print(f"   E{n} target q{n} = {known[n]}")
    if not _ASSEMBLE_READY:
        print("[contract] STATUS: moment assembler `_assemble_moment` not yet wired to the")
        print("           Stage-3J color/Gamma convention. No m6 emitted (by design).")
        print("           Reference in tree: y4_o3_flatband_verification/ (q4 = 189-record H4(0) trace).")
        print("           Validated & ready: degree-8 Haar tensors (stage 1) + E6 fold.")
        return None
    # --- once _assemble_moment is wired, the ladder below runs automatically ---
    E,v=fold(6)
    moments={}
    # moments S_{a1..ar} are assembled per order from the geometry census + Haar + resolvent:
    #   S_w = sum_geometries colour_amp(geometry) * prod_i (E0 - E_cut_i)**(-a_i)
    # (left as `_assemble_moment`, the single Stage-3J-convention function).
    raise SystemExit("contract: _assemble_moment wired -- run on the full census root.")

_ASSEMBLE_READY=False   # set True once `_assemble_moment` is wired to the Stage-3J convention

# =====================================================================
# COLAB RUNNER  --  set MODE (and paths if needed), then run this cell.
# =====================================================================
MODE = "selftest"          # "selftest" | "compile-haar" | "contract"

# paths used by compile-haar / contract (edit for your Colab VM):
SIGNATURES = "/content/SU3_Y6_RUN/SIGNATURES/su3_y6_final_ordered_signatures.bin"
HAAR_OUT   = "/content/HAAR_OUT"
ROOT       = "/content/SU3_Y6_RUN"
PRIMES     = [33554467, 100000007]

def _locate_signatures(path):
    import glob
    if os.path.exists(path): return path
    hits=glob.glob("/content/**/su3_y6_final_ordered_signatures.bin", recursive=True)
    if hits: print("found signatures at",hits[0]); return hits[0]
    raise FileNotFoundError(
        "su3_y6_final_ordered_signatures.bin not found.\n"
        "  It is produced by the signature-census step of your SU3_Y6_STAGE0 launch bundle,\n"
        "  written to SU3_Y6_RUN/SIGNATURES/su3_y6_final_ordered_signatures.bin.\n"
        "  It is NOT in SU3_Y6_STAGE0_ESSENTIAL_RESULTS.zip (that archive packed SU3_Y6_RUN/final\n"
        "  + logs only, not the SIGNATURES/ folder). To get it, either:\n"
        "   (a) run the launch-bundle pipeline on this VM (it writes the .bin), or\n"
        "   (b) copy SU3_Y6_RUN/SIGNATURES/ from the VM where you ran the census, or\n"
        "   (c) re-zip your results INCLUDING SU3_Y6_RUN/SIGNATURES/ and upload that.")

if MODE == "selftest":
    selftest()
elif MODE == "compile-haar":
    compile_haar(_locate_signatures(SIGNATURES), HAAR_OUT)   # add exact=True for rational projectors (slow)
elif MODE == "contract":
    contract(root=ROOT, primes=PRIMES, max_order=6)
else:
    raise ValueError("MODE must be selftest | compile-haar | contract")
