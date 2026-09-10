"""Exact finite controls; not certification of the general Wilson hypotheses."""
from fractions import Fraction as F
import json

def tr(a): return list(map(list, zip(*a)))
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a): return [[-x for x in r] for r in a]
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def inv(a):
    n=len(a)
    m=[[F(x) for x in r]+[F(i==j) for j in range(n)] for i,r in enumerate(a)]
    for i in range(n):
        k=next(k for k in range(i,n) if m[k][i])
        m[i],m[k]=m[k],m[i]
        d=m[i][i]; m[i]=[x/d for x in m[i]]
        for k in range(n):
            if k!=i:
                d=m[k][i]; m[k]=[x-d*y for x,y in zip(m[k],m[i])]
    return [r[n:] for r in m]
def quad(r,a): return mul(tr(r),mul(a,r))[0][0]
def block(d,b,c): return [d[i]+tr(b)[i] for i in range(len(d))]+[b[i]+c[i] for i in range(len(c))]

checks=0
for den in (2,3,4,8,16,32):
    g=F(1,den)
    c=[[F(2),F(1)],[F(1),F(3)]]
    b=[[g,2*g],[-g,g]]
    s=[[2*g*g,g*g],[g*g,3*g*g]]
    ci=inv(c); d=add(s,mul(tr(b),mul(ci,b))); a=block(d,b,c)
    for j in range(-3,4):
        rs=[[g*g*j],[g*g*(j+1)]]; rh=[[g],[g*j]]
        eta=add(rs,neg(mul(tr(b),mul(ci,rh))))
        assert quad(rs+rh,inv(a))==quad(rh,ci)+quad(eta,inv(s))
        checks+=1
    # Raw soft orthogonality fails with order-one mixing.
    a=[[1+g*g,F(1)],[F(1),F(1)]]
    assert quad([[F(0)],[g]],inv(a))==1+g*g
    # Complete residual: small mixing alone still fails.
    a=[[2*g*g,g],[g,F(1)]]; a0=[[g*g,F(0)],[F(0),F(1)]]
    t=[[F(0)],[F(1)]]; u=mul(inv(a0),t); rho=add(mul(a,u),neg(t))
    delta=quad(t,add(inv(a),neg(inv(a0))))
    assert delta==1==-quad(u,add(a,neg(a0)))+quad(rho,inv(a))
    # Complete successful residual realization with vanishing global floor.
    a=[[2*g*g,g*g],[g*g,F(1)]]; a0=[[2*g*g,F(0)],[F(0),F(1)]]
    u=mul(inv(a0),t); rho=add(mul(a,u),neg(t))
    delta=quad(t,add(inv(a),neg(inv(a0))))
    assert delta==g*g/(2-g*g)==quad(rho,inv(a))
    assert delta<=g*g<=g
    checks+=3
print(json.dumps({'status':'PASS','exact_cases':checks,'arithmetic':'fractions.Fraction',
 'scope':'finite identity and success/failure controls; no Wilson or Lean certification'},indent=2))
