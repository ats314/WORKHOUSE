#!/usr/bin/env python3
"""
ENGINE_SHELL6_link_calculus_validate.py -- validate the LINK-VARIABLE word calculus.

Reuses the certified su3_domino_d3 word machinery, but with generators = LATTICE
LINKS and H0 = sum_links (1/2) Cas(link).  No cross-terms (links are the
fundamental variables).  If this reproduces the single-plaquette Bridge towers
  order-2 gaps (C-even, C-odd) = (13/20, 1/2)
that the plaquette-holonomy engine certified, the link calculus is exact and can
be carried to the shell-6 hexagon basis.
"""
import sys, os, itertools
from collections import defaultdict
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ENGINE_FLUX_su3_domino_d3 as D
from ENGINE_FLUX_su3_domino_d3 import (canon_word, expr_add, expr_scale, expr_mul, conj_expr,
                           cas_monomial, Resolvent, _min_rotation)
from ENGINE_FLUX_su3_moments_ext import link_terms, eval_term

# ---- generalize integrate_monomial to ARBITRARY link generators, monkeypatch ----
_ICACHE={}
def integrate_monomial_links(m):
    if m in _ICACHE: return _ICACHE[m]
    nv=0; linkfac=defaultdict(lambda:([],[]))
    for w in m:
        Lw=len(w); ids=list(range(nv,nv+Lw)); nv+=Lw
        for t,(gen,pw) in enumerate(w):
            a,b=ids[t],ids[(t+1)%Lw]; us,bs=linkfac[gen]
            if pw==+1: us.append((a,b))
            else: bs.append((b,a))
    term_lists=[]
    for (us,bs) in linkfac.values():
        tl=link_terms(us,bs)
        if not tl: _ICACHE[m]=F(0); return F(0)
        term_lists.append(tl)
    tot=F(0)
    for combo in itertools.product(*term_lists):
        coeff=F(1); cons=()
        for (c_,k_) in combo: coeff*=c_; cons=cons+k_
        if coeff!=0: tot+=eval_term(coeff,cons,nv)
    _ICACHE[m]=tot; return tot
D.integrate_monomial = integrate_monomial_links     # inner/integrate_expr now general
from ENGINE_FLUX_su3_domino_d3 import inner

GATES=[]
def gate(name,c):
    GATES.append((name,bool(c))); print(f"  GATE {'PASS' if c else 'FAIL'} :: {name}")
    if not c: raise SystemExit("GATE FAILED: "+name)

def make_H0_links():
    cache={}
    def H0_mono(m):
        if m in cache: return cache[m]
        gens=set(g for w in m for (g,p) in w)
        out={}
        for g in gens:
            out=expr_add(out, expr_scale(cas_monomial(m,g), F(1,2)))
        cache[m]=out; return out
    def H0(e):
        out={}
        for mm,cf in e.items(): out=expr_add(out, expr_scale(H0_mono(mm),cf))
        return out
    H0.mono=H0_mono; return H0

def word_expr(word): return canon_word(tuple(word))

def apply_W_links(e, plaq_words):
    out={}
    for pw in plaq_words:
        out=expr_add(out, expr_mul(e, canon_word(tuple(pw))))
    return out

def second_order(manifold, E0, plaq_words, tag):
    H0=make_H0_links(); R=Resolvent(H0,E0,manifold,tag)
    n=len(manifold)
    # gate manifold orthonormal
    for a in range(n):
        for b in range(n):
            gate(f"[{tag}] Gram[{a}{b}]={int(a==b)}",
                 inner(manifold[a],manifold[b])==(F(1) if a==b else F(0)))
    Wf=[apply_W_links(f,plaq_words) for f in manifold]
    B=[[inner(manifold[a],Wf[b]) for b in range(n)] for a in range(n)]
    h1=[[-B[a][b] for b in range(n)] for a in range(n)]
    y1=[R.apply(Wf[b]) for b in range(n)]
    h2=[[inner(manifold[a],apply_W_links(y1[b],plaq_words)) for b in range(n)] for a in range(n)]
    for h,nm in ((h1,'h1'),(h2,'h2')):
        gate(f"[{tag}] {nm} Hermitian", all(h[a][b]==h[b][a] for a in range(n) for b in range(n)))
    return h1,h2

def main():
    # single plaquette p0: links 0,1,2,3 ; P = Tr U0 U1 U2 U3
    P=((0,+1),(1,+1),(2,+1),(3,+1))
    Pd=tuple((g,-p) for (g,p) in reversed(P))   # Tr U3^-1 U2^-1 U1^-1 U0^-1
    print("="*72,"\nLINK CALCULUS: single-plaquette self-energy (only p0 acts)")
    print("="*72)
    plaqs=[P,Pd]
    # H0 sanity
    H0=make_H0_links()
    gate("H0 Tr(p0) = 8/3 Tr(p0)", expr_add(H0(word_expr(P)), expr_scale(word_expr(P),F(-8,3)))=={})
    # vacuum
    h1v,h2v=second_order([{():F(1)}], F(0), plaqs, 'L-vac')
    print(f"  vacuum e2 = {h2v[0][0]}  (expect -3/4)")
    gate("vacuum e2 == -3/4", h2v[0][0]==F(-3,4))
    # excited manifold {P, Pd}
    man=[word_expr(P), word_expr(Pd)]
    h1,h2=second_order(man, F(8,3), plaqs, 'L-exc')
    # C-even/odd combinations
    ev_e=lambda h:F(1,2)*(h[0][0]+h[0][1]+h[1][0]+h[1][1])
    ev_o=lambda h:F(1,2)*(h[0][0]-h[0][1]-h[1][0]+h[1][1])
    e1e,e1o=ev_e(h1),ev_o(h1); e2e,e2o=ev_e(h2),ev_o(h2)
    print(f"  order-1 (even,odd) = ({e1e},{e1o})   (expect -1,+1)")
    print(f"  order-2 (even,odd) = ({e2e},{e2o})")
    print(f"  order-2 GAPS vs vacuum = ({e2e-h2v[0][0]},{e2o-h2v[0][0]})  (expect 13/20, 1/2)")
    gate("order-1 levels (even,odd) == (-1,+1)", (e1e,e1o)==(F(-1),F(1)))
    gate("order-2 BRIDGE gaps (even,odd) == (13/20, 1/2)",
         (e2e-h2v[0][0], e2o-h2v[0][0])==(F(13,20),F(1,2)))
    print("="*72)
    print(f"ALL {sum(p for _,p in GATES)}/{len(GATES)} GATES PASSED -- link calculus is EXACT")
    print("="*72)

if __name__=="__main__":
    main()
