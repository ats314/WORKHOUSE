"""Independent SU(3) calculation in two Cartesian oscillator coordinates."""
from __future__ import annotations
import json
import math
from pathlib import Path
import sympy as s

x,y=s.symbols("x y")
R=s.Rational
def clean(p): return s.Poly(s.expand(p),x,y,domain=s.QQ).as_expr()
def D(p): return clean((s.diff(p,x,2)+s.diff(p,y,2))/2)
def L(p): return clean(x*s.diff(p,x)+y*s.diff(p,y)-D(p))
def heat(p,sign):
    term,out,k=p,p,0
    while term != 0:
        k+=1
        term=clean(sign*D(term)/(2*k))
        out=clean(out+term)
    return out
def bydegree(p,d):
    return sum(c*x**a*y**b for (a,b),c in s.Poly(p,x,y).terms() if a+b==d)
def resolvent(p,degree):
    h=heat(p,1)
    return heat(sum(c*x**a*y**b/(degree-a-b) for (a,b),c in s.Poly(h,x,y).terms() if a+b!=degree),-1)
def gaussian(p):
    out=0
    for (a,b),c in s.Poly(p,x,y).terms():
        if a%2==0 and b%2==0:
            out+=c*s.factorial2(a-1)*s.factorial2(b-1)/2**((a+b)//2)
    return out
def trace_even(k):
    # theta=(x/sqrt(2)+y/sqrt(6), -x/sqrt(2)+y/sqrt(6), -2y/sqrt(6)).
    # Binomial expansion removes radicals before any calculation.
    return clean(sum(2*s.binomial(k,j)*x**j*y**(k-j)/2**(j//2)/6**((k-j)//2) for j in range(0,k+1,2))+(-2)**k*y**k/6**(k//2))
def solve(seed,order):
    degree=s.Poly(seed,x,y).total_degree()
    p0=heat(seed,-1); norm=gaussian(p0*p0)
    assert clean(L(p0)-degree*p0)==0
    ps,es=[p0],[s.Integer(degree)]
    for n in range(1,order+1):
        forcing=clean(sum(R((-1)**j,2**j*math.factorial(2*j+2))*trace_even(2*j+2)*ps[n-j] for j in range(1,n+1)))
        en=gaussian(clean(p0*forcing))/norm
        es.append(en)
        rhs=clean(forcing-sum(es[j]*ps[n-j] for j in range(1,n+1)))
        assert clean(bydegree(heat(rhs,1),degree))==0
        psi=resolvent(rhs,degree)
        assert clean(degree*psi-L(psi)-rhs)==0
        assert gaussian(clean(p0*psi))==0
        ps.append(psi)
        print(f"cartesian degree={degree} order={n}: {en}",flush=True)
    return es
if __name__=="__main__":
    delta=x*(x*x-3*y*y)
    es=[solve(z,4) for z in (delta,delta*(x*x+y*y),delta*y*(3*x*x-y*y))]
    out={}
    generic=json.loads(Path(__file__).with_name("coefficients_order4.json").read_text())
    for name,vals in zip(("even","odd"),es[1:]):
        gap=[s.factor(a-b) for a,b in zip(vals,es[0])]
        expected=[s.sympify(z) for z in generic["gaps"][name]["SU3_g_series"]]
        assert gap==expected,(name,gap,expected)
        out[name]=[str(z) for z in gap]
    dest=Path(__file__).with_name("independent_su3.json")
    assert not dest.exists()
    dest.write_text(json.dumps({"method":"Cartesian Laplacian and elementary Gaussian monomial integration; no trace recursion","all_exact":True,"gaps":out},indent=2)+"\n")
    print("INDEPENDENT SU3: PASS",flush=True)

