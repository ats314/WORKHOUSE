#!/usr/bin/env python3
"""
ENGINE_SHELL6_link_o2.py -- LINK-VARIABLE word calculus with the fast tensor-network Haar
integrator (fast_haar.haar_tn).  This is the CORRECT exact engine for multi-face
Wilson loops (the plaquette-holonomy 2*Cas model mis-energies them; link H0 =
sum_links (1/2)Cas is exact).  The integration blow-up that stalled it before is
removed.  Validation: single-plaquette Bridge towers (13/20, 1/2) and the shell-4
neighbour hop (5/612) -- the certified su3_domino_d3 numbers.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_su3_domino_d3 as D
from ENGINE_HAAR_fast_haar import haar_tn
# patch the (2-generator-only) integrator with the general fast one
D.integrate_monomial = lambda m: haar_tn(list(m))
from ENGINE_FLUX_su3_domino_d3 import (canon_word, expr_add, expr_scale, expr_mul, conj_expr,
                           inner, cas_monomial, Resolvent, sandwich)

GATES=[]
def gate(n,c):
    GATES.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}")
    if not c: raise SystemExit("FAIL "+n)

def make_H0_links():
    cache={}
    def H0_mono(m):
        if m in cache: return cache[m]
        gens=set(g for w in m for (g,p) in w)
        out={}
        for g in gens: out=expr_add(out, expr_scale(cas_monomial(m,g), F(1,2)))
        cache[m]=out; return out
    def H0(e):
        out={}
        for mm,cf in e.items(): out=expr_add(out, expr_scale(H0_mono(mm),cf))
        return out
    H0.mono=H0_mono; return H0

def apply_W_links(e, plaq_words):
    out={}
    for pw in plaq_words: out=expr_add(out, expr_mul(e, canon_word(tuple(pw))))
    return out

def second_order(manifold, E0, plaq_words, tag, check_gram=True):
    H0=make_H0_links(); R=Resolvent(H0,E0,manifold,tag); n=len(manifold)
    if check_gram:
        for a in range(n):
            for b in range(n):
                gate(f"[{tag}] Gram[{a}{b}]={int(a==b)}",
                     inner(manifold[a],manifold[b])==(F(1) if a==b else F(0)))
    Wf=[apply_W_links(f,plaq_words) for f in manifold]
    B=[[inner(manifold[a],Wf[b]) for b in range(n)] for a in range(n)]
    h1=[[-B[a][b] for b in range(n)] for a in range(n)]
    y1=[R.apply(Wf[b]) for b in range(n)]
    h2=[[inner(manifold[a],apply_W_links(y1[b],plaq_words)) for b in range(n)] for a in range(n)]
    return h1,h2

def main():
    print("="*72,"\nLINK-VARIABLE engine (fast TN Haar): reproduce certified constants")
    print("="*72)
    # ---- single plaquette Bridge: links 0..3, only p0 acts ----
    P=((0,+1),(1,+1),(2,+1),(3,+1)); Pd=tuple((g,-p) for (g,p) in reversed(P))
    plaqs=[P,Pd]
    h1v,h2v=second_order([{():F(1)}],F(0),plaqs,'1p-vac',check_gram=False)
    man=[canon_word(P),canon_word(Pd)]
    h1,h2=second_order(man,F(8,3),plaqs,'1p-exc')
    eve=lambda h:F(1,2)*(h[0][0]+h[0][1]+h[1][0]+h[1][1])
    evo=lambda h:F(1,2)*(h[0][0]-h[0][1]-h[1][0]+h[1][1])
    print(f"  single-plaquette: order1 (even,odd)=({eve(h1)},{evo(h1)})  vac e2={h2v[0][0]}")
    print(f"  order2 gaps (even,odd) = ({eve(h2)-h2v[0][0]},{evo(h2)-h2v[0][0]})")
    gate("single-plaquette order-1 == (-1,+1)", (eve(h1),evo(h1))==(F(-1),F(1)))
    gate("single-plaquette vacuum e2 == -3/4", h2v[0][0]==F(-3,4))
    gate("single-plaquette BRIDGE gaps == (13/20, 1/2)",
         (eve(h2)-h2v[0][0],evo(h2)-h2v[0][0])==(F(13,20),F(1,2)))
    # ---- shell-4 neighbour hop: pa, pb share link 1 (opposite) ----
    pa=((0,+1),(1,+1),(2,+1),(3,+1)); pb=((4,+1),(5,+1),(6,+1),(1,-1))
    pad=tuple((g,-p) for (g,p) in reversed(pa)); pbd=tuple((g,-p) for (g,p) in reversed(pb))
    W4=[pa,pad,pb,pbd]
    man4=[canon_word(pa),canon_word(pad),canon_word(pb),canon_word(pbd)]
    h1b,h2b=second_order(man4,F(8,3),W4,'shell4-hop')
    # C-even/odd hop between pa and pb
    he=(h2b[2][0]+h2b[2][1]+h2b[3][0]+h2b[3][1])/2
    ho=(h2b[2][0]-h2b[2][1]-h2b[3][0]+h2b[3][1])/2
    print(f"  shell-4 hop: C-even={he}  C-odd={ho}  (certified |odd|=5/612, even=-11/306)")
    gate("shell-4 C-odd hop magnitude == 5/612", abs(ho)==F(5,612))
    gate("shell-4 C-even hop == -11/306", he==F(-11,306))
    print("="*72); print(f"ALL {sum(GATES)}/{len(GATES)} GATES PASSED -- link engine exact & fast")
    print("="*72)

if __name__=="__main__":
    main()
