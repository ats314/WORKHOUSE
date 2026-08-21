#!/usr/bin/env python3
"""
DATA_HAAR_o2_v2.py -- link-variable word calculus with the fast TN Haar integrator AND
a GRAM (Galerkin / weak-form) resolvent that is robust to the function-space
linear dependencies the raw monomial basis carries (composite Cayley-Hamilton,
e.g. Tr(g^2)=Tr(g)^2-2Tr(g^-1), which canon_word does not see for composite loops).

Weak form: solve  sum_i c_i <m_k|(E0-H0)|m_i> = <m_k|Qx>  for all closure monomials
m_k, plus <manifold|y>=0.  Uses the Gram matrix G_ki=<m_k|m_i> -> the redundant
coefficient directions become a (zero-function) kernel, and the system stays
consistent.  Validated: single-plaquette Bridge (13/20,1/2); shell-4 hop (5/612).
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ENGINE_FLUX_su3_domino_d3 as D
from ENGINE_HAAR_fast_haar import haar_tn
D.integrate_monomial = lambda m: haar_tn(list(m))
from ENGINE_FLUX_su3_domino_d3 import (canon_word, expr_add, expr_scale, expr_mul, conj_expr,
                           inner, cas_monomial, solve_stacked)

GATES=[]
def gate(n,c):
    GATES.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}")
    if not c: raise SystemExit("FAIL "+n)

def make_H0_links():
    cache={}
    def H0_mono(m):
        if m in cache: return cache[m]
        gens=set(g for w in m for (g,p) in w); out={}
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

def gram_resolvent(H0, E0, manifold, x, tag):
    qx=dict(x)
    for f in manifold:
        ov=inner(f,x)
        if ov: qx=expr_add(qx,f,-ov)
    if not qx: return {}
    basis=list(qx.keys()); seen=set(basis); i=0
    while i<len(basis):
        for mm in H0.mono(basis[i]):
            if mm not in seen: seen.add(mm); basis.append(mm)
        i+=1
    n=len(basis); pos={m:k for k,m in enumerate(basis)}
    G=[[inner({basis[k]:F(1)},{basis[i]:F(1)}) for i in range(n)] for k in range(n)]
    Ac=[H0.mono(basis[i]) for i in range(n)]
    # <m_k|(E0-H0)|m_i> = E0 G_ki - sum_j A_ij G_kj
    S=[[E0*G[k][i]-sum(cf*G[k][pos[mm]] for mm,cf in Ac[i].items()) for i in range(n)]
       for k in range(n)]
    r=[inner({basis[k]:F(1)}, qx) for k in range(n)]
    rows=[row[:] for row in S]; rhs=list(r)
    for f in manifold:
        rows.append([inner(f,{basis[i]:F(1)}) for i in range(n)]); rhs.append(F(0))
    sol,kernel=solve_stacked(rows,rhs)
    gate(f"[{tag}] gram-resolvent consistent (n={n})", sol is not None)
    y={}
    for i,cf in enumerate(sol):
        if cf: y=expr_add(y,{basis[i]:cf})
    # verify weak residual: <m_k|(E0-H0)y> == <m_k|Qx> for all k
    res_ok=all(sum(S[k][i]*sol[i] for i in range(n))==r[k] for k in range(n))
    gate(f"[{tag}] weak residual zero", res_ok)
    return y

def second_order(manifold, E0, plaq_words, tag, gram=True):
    H0=make_H0_links(); n=len(manifold)
    if gram:
        for a in range(n):
            for b in range(n):
                gate(f"[{tag}] Gram[{a}{b}]={int(a==b)}",
                     inner(manifold[a],manifold[b])==(F(1) if a==b else F(0)))
    Wf=[apply_W_links(f,plaq_words) for f in manifold]
    B=[[inner(manifold[a],Wf[b]) for b in range(n)] for a in range(n)]
    h1=[[-B[a][b] for b in range(n)] for a in range(n)]
    y1=[gram_resolvent(H0,E0,manifold,Wf[b],tag+f'-y{b}') for b in range(n)]
    h2=[[inner(manifold[a],apply_W_links(y1[b],plaq_words)) for b in range(n)] for a in range(n)]
    return h1,h2

def main():
    print("="*72,"\nLINK-VARIABLE engine v2 (Gram resolvent + fast Haar)")
    print("="*72)
    P=((0,+1),(1,+1),(2,+1),(3,+1)); Pd=tuple((g,-p) for (g,p) in reversed(P))
    h1v,h2v=second_order([{():F(1)}],F(0),[P,Pd],'1p-vac',gram=False)
    man=[canon_word(P),canon_word(Pd)]
    h1,h2=second_order(man,F(8,3),[P,Pd],'1p-exc')
    eve=lambda h:F(1,2)*(h[0][0]+h[0][1]+h[1][0]+h[1][1])
    evo=lambda h:F(1,2)*(h[0][0]-h[0][1]-h[1][0]+h[1][1])
    print(f"  single-plaquette: order1 ({eve(h1)},{evo(h1)})  vac e2={h2v[0][0]}  gaps ({eve(h2)-h2v[0][0]},{evo(h2)-h2v[0][0]})")
    gate("single-plaquette order-1 == (-1,+1)", (eve(h1),evo(h1))==(F(-1),F(1)))
    gate("single-plaquette vacuum e2 == -3/4", h2v[0][0]==F(-3,4))
    gate("single-plaquette BRIDGE == (13/20,1/2)",
         (eve(h2)-h2v[0][0],evo(h2)-h2v[0][0])==(F(13,20),F(1,2)))
    # shell-4 neighbour hop
    pa=((0,+1),(1,+1),(2,+1),(3,+1)); pb=((4,+1),(5,+1),(6,+1),(1,-1))
    pad=tuple((g,-p) for (g,p) in reversed(pa)); pbd=tuple((g,-p) for (g,p) in reversed(pb))
    man4=[canon_word(pa),canon_word(pad),canon_word(pb),canon_word(pbd)]
    h1b,h2b=second_order(man4,F(8,3),[pa,pad,pb,pbd],'shell4')
    he=(h2b[2][0]+h2b[2][1]+h2b[3][0]+h2b[3][1])/2
    ho=(h2b[2][0]-h2b[2][1]-h2b[3][0]+h2b[3][1])/2
    print(f"  shell-4 hop: C-even={he}  C-odd={ho}")
    gate("shell-4 C-odd hop |.|==5/612", abs(ho)==F(5,612))
    gate("shell-4 C-even hop ==-11/306", he==F(-11,306))
    print("="*72); print(f"ALL {sum(GATES)}/{len(GATES)} GATES PASSED")

if __name__=="__main__":
    main()
