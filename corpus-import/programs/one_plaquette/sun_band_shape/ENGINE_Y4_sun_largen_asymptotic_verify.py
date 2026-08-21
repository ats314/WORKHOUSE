#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

N,z=sp.symbols('N z')
MAX_POWER=13

def recursive_find(name:str)->Path|None:
    for p in (Path.cwd()/name,Path('/content')/name,Path('/mnt/data')/name):
        if p.exists(): return p
    for root in (Path.cwd(),Path('/content'),Path('/mnt/data')):
        if root.exists():
            for p in root.rglob(name): return p
    return None

def rational_series_at_infinity(expr:sp.Expr,max_power:int=MAX_POWER)->dict[int,sp.Rational]:
    num,den=sp.fraction(sp.together(expr))
    p=sp.Poly(sp.expand(num),N,domain=sp.QQ)
    q=sp.Poly(sp.expand(den),N,domain=sp.QQ)
    dp,dq=p.degree(),q.degree(); shift=dq-dp
    pr=[p.nth(dp-k) for k in range(dp+1)]
    qr=[q.nth(dq-k) for k in range(dq+1)]
    need=max_power-shift
    if need<=0:return {}
    coeff=[]
    for n in range(need):
        pn=pr[n] if n<len(pr) else sp.Integer(0)
        convolution=sum((qr[k] if k<len(qr) else 0)*coeff[n-k] for k in range(1,n+1))
        coeff.append(sp.cancel((pn-convolution)/qr[0]))
    return {shift+n:sp.Rational(c) for n,c in enumerate(coeff) if shift+n<max_power and c}

def add_series(a:dict[int,sp.Rational],b:dict[int,sp.Rational])->dict[int,sp.Rational]:
    out=dict(a)
    for k,v in b.items():out[k]=sp.cancel(out.get(k,0)+v)
    return {k:sp.Rational(v) for k,v in out.items() if v}

def main()->None:
    qlp=recursive_find('q_z_polynomial_ledger.json')
    bp=recursive_find('NOTE_Y4_sun_b_structured_expression.txt')
    assert qlp and bp,'Missing q polynomial ledger or B structured expression.'
    ledger=json.loads(qlp.read_text())
    Q=sp.Poly.from_list([sp.Integer(v) for v in ledger['Q_coefficients_descending']],z).as_expr()
    D=sp.Poly.from_list([sp.Integer(v) for v in ledger['D_coefficients_descending']],z).as_expr()
    q=-sp.Rational(2,3)*Q.subs(z,N**2)/(N*D.subs(z,N**2))
    A=sp.Rational(640)/(N*(N**2-1)**3)
    B=sp.sympify(bp.read_text(),locals={'N':N},evaluate=False)
    qs=rational_series_at_infinity(q)
    As=rational_series_at_infinity(A)
    Bs={}
    for term in B.args:Bs=add_series(Bs,rational_series_at_infinity(term))
    Ws=add_series(As,Bs)
    assert qs[5]==-227 and qs[7]==-sp.Rational(1638943,864)
    assert As[7]==640 and As[9]==1920
    assert Bs[7]==sp.Rational(6170,9) and Bs[9]==sp.Rational(677903,324)
    assert Ws[7]==sp.Rational(11930,9) and Ws[9]==sp.Rational(1299983,324)
    # Leading ratio coefficient after factoring N^-2.
    assert sp.cancel(Ws[7]/(-qs[5]))==sp.Rational(11930,2043)
    print('PASS q_N = -227/N^5 - 1638943/(864 N^7) + O(N^-9)')
    print('PASS A_N = 640/N^7 + 1920/N^9 + O(N^-11)')
    print('PASS B_N = 6170/(9 N^7) + 677903/(324 N^9) + O(N^-11)')
    print('PASS Delta c_4,N = 11930/(9 N^7) + 1299983/(324 N^9) + O(N^-11)')
    print('PASS Delta c_4,N/|q_N| = 11930/(2043 N^2) + O(N^-4)')
    print('ALL LARGE-N ASYMPTOTIC CERTIFICATE GATES PASS')

if __name__=='__main__':main()
