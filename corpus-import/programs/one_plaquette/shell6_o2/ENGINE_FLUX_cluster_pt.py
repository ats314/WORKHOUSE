#!/usr/bin/env python3
"""
ENGINE_FLUX_cluster_pt.py -- generalize the certified su3_domino_d3 des-Cloizeaux engine from
the 2-plaquette domino to an ARBITRARY simply-connected cluster of plaquette
holonomies g_1..g_n.  H0 = sum_i 2*Cas(g_i) + sum_{shared link (i,j,s)} cross(i,j,s).
This keeps the word degree low (Cayley-Hamilton) -> no blow-up; it is the efficient
exact route to the shell-6 hexagon O(y^2).

STEP 1 (this file): reproduce the domino constants (C-odd hop 5/612, flat band
11/306) with the generalized cluster H0 -> validates the cross-term generalization.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ENGINE_FLUX_su3_domino_d3 import (expr_of, expr_add, expr_scale, apply_W, inner, Resolvent,
                           sandwich, cas_monomial, _occurrences, _ins_data, _cut_of,
                           pair_fierz, make_H0)

GATES=[]
def gate(n,c):
    GATES.append(c); print(f"  GATE {'PASS' if c else 'FAIL'} :: {n}")
    if not c: raise SystemExit("FAIL "+n)

# ---- generalized cross term between two holonomy generators ----
def cross_pair(m, gi, gj, s):
    occi=_occurrences(m,gi); occj=_occurrences(m,gj)
    modej='R' if s==+1 else 'L'
    out={}
    for (w1,t1,p1) in occi:
        for (w2,t2,p2) in occj:
            wh1,sub1,eta1=_ins_data(p1,'R')
            wh2,sub2,eta2=_ins_data(p2,modej)
            L1,L2=len(m[w1]),len(m[w2])
            ins1=(w1,_cut_of(L1,t1,wh1),sub1)
            ins2=(w2,_cut_of(L2,t2,wh2),sub2)
            fz=pair_fierz(m,ins1,ins2)
            out=expr_add(out, expr_scale(fz, F(1)*eta1*eta2))
    return out

def make_H0_cluster(gens, shared):
    """gens: list of holonomy labels. shared: list of (gi,gj,s)."""
    cache={}
    def H0_mono(m):
        if m in cache: return cache[m]
        out={}
        for g in gens:
            out=expr_add(out, expr_scale(cas_monomial(m,g), F(2)))
        for (gi,gj,s) in shared:
            out=expr_add(out, cross_pair(m,gi,gj,s))
        cache[m]=out; return out
    def H0(e):
        out={}
        for m,cf in e.items(): out=expr_add(out, expr_scale(H0_mono(m),cf))
        return out
    H0.mono=H0_mono; return H0

def pt2(H0, manifold, E0, chars, tag):
    R=Resolvent(H0,E0,manifold,tag); n=len(manifold)
    for a in range(n):
        for b in range(n):
            gate(f"[{tag}] Gram[{a}{b}]={int(a==b)}",
                 inner(manifold[a],manifold[b])==(F(1) if a==b else F(0)))
    Wf=[apply_W(f,chars) for f in manifold]
    B=[[inner(manifold[a],Wf[b]) for b in range(n)] for a in range(n)]
    h1=[[-B[a][b] for b in range(n)] for a in range(n)]
    y1=[R.apply(Wf[b]) for b in range(n)]
    h2=[[inner(manifold[a],apply_W(y1[b],chars)) for b in range(n)] for a in range(n)]
    for h,nm in ((h1,'h1'),(h2,'h2')):
        gate(f"[{tag}] {nm} Hermitian", all(h[a][b]==h[b][a] for a in range(n) for b in range(n)))
    return h1,h2

def main():
    CHI1,CHIB1=((1,+1),),((1,-1),); CHI2,CHIB2=((2,+1),),((2,-1),)
    print("="*72,"\nSTEP 1: cluster H0 reproduces the certified domino")
    print("="*72)
    # cross-term generalization must match the hardcoded domino H0 monomial-by-monomial
    for s in (+1,-1):
        Hd=make_H0({'gens':[1,2],'s':s})
        Hc=make_H0_cluster([1,2],[(1,2,s)])
        tests=[expr_of([CHI1,CHI2]), expr_of([CHI1,CHIB2]), expr_of([CHI1,CHI1]),
               expr_of([CHI1,CHIB1]), expr_of([CHI1,CHI2,CHIB2])]
        ok=all(expr_add(Hd(e),expr_scale(Hc(e),F(-1)))=={} for e in tests)
        gate(f"cluster H0 == domino H0 (s={s:+d}) on 5 test states", ok)
    # full O(y^2) domino via the cluster H0
    chars=[(1,+1),(1,-1),(2,+1),(2,-1)]
    man=[expr_of([CHI1]),expr_of([CHIB1]),expr_of([CHI2]),expr_of([CHIB2])]
    for s in (+1,-1):
        H0=make_H0_cluster([1,2],[(1,2,s)])
        h1,h2=pt2(H0, man, F(8,3), chars, f'dom-s{s:+d}')
        o1=[F(1),F(-1),F(0),F(0)]; o2=[F(0),F(0),F(1),F(-1)]
        e1=[F(1),F(1),F(0),F(0)]; e2=[F(0),F(0),F(1),F(1)]
        To2=sandwich(h2,o1,o2); Te2=sandwich(h2,e1,e2)
        Do2=sandwich(h2,o1,o1)
        print(f"  s={s:+d}: C-odd hop To2={To2}  C-even hop Te2={Te2}  diag Do2={Do2}")
        gate(f"s={s:+d}: C-odd hop == s*5/612", To2==F(5,612)*s)
        gate(f"s={s:+d}: C-even hop == -11/306", Te2==F(-11,306))
    # vacuum + flat-band assembly check
    H0p=make_H0_cluster([1,2],[(1,2,+1)])
    hv1,hv2=pt2(H0p,[{():F(1)}],F(0),chars,'dom-vac')
    print(f"  vacuum e2 = {hv2[0][0]} (expect -3/2)")
    gate("domino vacuum e2 == -3/2", hv2[0][0]==F(-3,2))
    print("="*72); print(f"ALL {sum(GATES)}/{len(GATES)} GATES PASSED -- cluster engine validated")
    print("="*72)

if __name__=="__main__":
    main()
