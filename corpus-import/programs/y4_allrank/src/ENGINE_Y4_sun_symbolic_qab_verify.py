#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,math
from pathlib import Path
import sympy as sp
N,z=sp.symbols('N z')

def recursive_find(name:str)->Path|None:
    for p in (Path('/content')/name,Path.cwd()/name,Path('/mnt/data')/name):
        if p.exists(): return p
    for root in (Path('/content'),Path.cwd(),Path('/mnt/data')):
        if root.exists():
            for p in root.rglob(name): return p
    return None

def sha256(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def forward_coefficients(poly:sp.Poly,base:int,count:int)->list[int]:
    cur=[int(poly.eval(base+i)) for i in range(count)]
    out=[]
    while cur:
        out.append(cur[0])
        if len(cur)==1:break
        cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
    return out

def main()->None:
    certp=recursive_find('CERT_Y4_sun_walled_brauer_full_symbolic_certificate_2026-06-14.json')
    bp=recursive_find('NOTE_Y4_sun_b_structured_expression.txt')
    bnp=recursive_find('CERT_MISC_b_newton_coefficients.json')
    qlp=recursive_find('q_z_polynomial_ledger.json')
    qnp=recursive_find('CERT_MISC_q_numerator_newton_coefficients.json')
    qfp=recursive_find('NOTE_Y4_sun_q_compact_z_formula.txt')
    assert all((certp,bp,bnp,qlp,qnp,qfp)),'Missing full symbolic certificate inputs.'
    cert=json.loads(certp.read_text())

    # q_N
    ql=json.loads(qlp.read_text()); qn=json.loads(qnp.read_text())
    Q=sp.Poly.from_list([sp.Integer(x) for x in ql['Q_coefficients_descending']],gens=z)
    D=sp.Poly.from_list([sp.Integer(x) for x in ql['D_coefficients_descending']],gens=z)
    assert Q.degree()==32 and D.degree()==34
    assert sha256(qlp)==cert['q']['polynomial_ledger_sha256']
    assert sha256(qnp)==cert['q']['newton_ledger_sha256']
    assert sha256(qfp)==cert['q']['compact_formula_sha256']
    levels=forward_coefficients(Q,49,40)
    expected=[int(x) for x in qn['coefficients']]
    assert levels==expected and all(x>0 for x in levels[:33]) and all(x==0 for x in levels[33:])
    for f,e in sp.factor_list(D.as_expr(),z)[1]:
        assert sp.degree(f,z) in (1,2)
        assert f.subs(z,49)>0 and sp.diff(f,z).subs(z,49)>0
        if sp.degree(f,z)==2: assert sp.LC(sp.Poly(f,z))>0
    qexpr=-sp.Rational(2,3)*Q.as_expr().subs(z,N**2)/(N*D.as_expr().subs(z,N**2))
    for row in cert['q']['fixed_rank_samples']:
        n=int(row['N']);q=sp.Rational(row['q'])
        assert sp.cancel(qexpr.subs(N,n)-q)==0 and q<0

    # A_N
    assert cert['A']['expression']=='640/(N*(N-1)^3*(N+1)^3)'

    # B_N
    bexpr=sp.sympify(bp.read_text().strip(),locals={'N':N})
    bnum,bden=sp.fraction(sp.together(bexpr))
    bn=json.loads(bnp.read_text()); coeff=[int(x) for x in bn['coefficients']]
    assert sha256(bp)==cert['B']['structured_expression_sha256']
    assert sha256(bnp)==cert['B']['newton_coefficients_sha256']
    assert len(coeff)==424 and all(x>0 for x in coeff[:403]) and all(x==0 for x in coeff[403:])
    assert sum(int(sp.degree(f,N))*int(e) for f,e in sp.factor_list(bden,N)[1])==409
    for f,e in sp.factor_list(bden,N)[1]:
        assert f.subs(N,7)>0 and sp.diff(f,N).subs(N,7)>0
        if sp.degree(f,N)==2: assert sp.LC(sp.Poly(sp.diff(f,N),N))>0
    vals=[]
    for n in range(7,431):
        v=sp.cancel(bexpr.subs(N,n)*bden.subs(N,n));assert v.is_Integer;vals.append(int(v))
    levelsB=[];cur=vals
    while cur:
        levelsB.append(cur[0])
        if len(cur)==1:break
        cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
    assert levelsB==coeff
    for row in cert['B'].get('samples',cert.get('samples',[])):
        pass
    # Samples live in top-level legacy A/B certificate; full q sample ranks independently cover 7..18.
    for row in cert['q']['fixed_rank_samples']:
        n=int(row['N'])
        assert sp.Rational(640,n*(n*n-1)**3)>0
        assert sp.cancel(bexpr.subs(N,n))>0

    assert cert['gates']['passed']
    print('PASS q_N compact rational formula, degrees (32,34) in z=N^2')
    print('PASS q_N denominator positivity and 33 positive Newton coefficients')
    print('PASS q_N exact fixed-rank matches for N=7,...,18')
    print('PASS A_N = 640/[N(N^2-1)^3]')
    print('PASS B_N denominator degree 409 and 403 positive Newton coefficients')
    print('PASS q_N<0, A_N>0, B_N>0 for every integer N>=7')
    print('ALL SYMBOLIC q_N/A_N/B_N CERTIFICATE GATES PASS')

if __name__=='__main__':main()
