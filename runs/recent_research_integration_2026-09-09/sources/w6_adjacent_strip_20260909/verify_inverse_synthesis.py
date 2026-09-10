"""Exact algebra controls for the all-retained inverse synthesis proof."""
import json
from pathlib import Path
import sympy as s

checks=[]
def check(name, test):
    assert test, name
    checks.append({'name':name,'passed':True})

k=3*(s.sqrt(5)-s.sqrt(3))/160
sigma_t=s.sqrt(5)/2
K=6561*(4-s.sqrt(15))/5120
check('constant after covariance, tensor map and ladder estimates',
      s.simplify((k*k*sigma_t*sigma_t/2)*729*6/(s.Rational(3,2))-K)==0)
check('equivalent unsimplified constant', s.simplify(K-s.Rational(3645,2)*k*k)==0)

sv=s.Matrix(s.symbols('s0:3'))
tv=s.Matrix(s.symbols('t0:3'))
h=s.symbols('h')
a=sv.dot(sv)
B=tv.dot(tv)-3*sigma_t
C=sv.dot(tv)**2-sigma_t*a
Q=tv*tv.T-sigma_t*s.eye(3)
R=2*h*sv*sv.T
M=6*R-11*s.trace(R)*s.eye(3)
check('radial source tensor factorization',
      s.expand(sum(Q[i,j]*M[i,j] for i in range(3) for j in range(3))/2
               -(-11*a*B+6*C)*h)==0)

def moment_t(poly):
    result=0
    for powers,coeff in s.Poly(s.expand(poly),*tv).terms():
        if any(n%2 for n in powers):
            continue
        term=coeff
        for n in powers:
            term*=s.factorial2(n-1)*sigma_t**(n//2) if n else 1
        result+=term
    return s.simplify(result)
check('all centered quadratic tensor covariance entries',all(
    s.simplify(moment_t(Q[i,j]*Q[k,l])-sigma_t**2*((i==k)*(j==l)+(i==l)*(j==k)))==0
    for i in range(3) for j in range(3) for k in range(3) for l in range(3)))

entries=s.symbols('r0:9', real=True)
RR=s.Matrix(3,3,entries)
MM=6*RR-11*s.trace(RR)*s.eye(3)
check('Frobenius norm tensor-map identity',
      s.expand(sum(v*v for v in MM)-36*sum(v*v for v in RR)-231*s.trace(RR)**2)==0)
trace_vector=s.Matrix([1 if i==j else 0 for i in range(3) for j in range(3)])
T=6*s.eye(9)-11*trace_vector*trace_vector.T
check('tensor map exact eigenvalues and multiplicities', T.eigenvals()=={s.Integer(6):8,s.Integer(-27):1})
ni,other,extra=s.symbols('ni other extra',nonnegative=True)
# c=1+extra. Annihilation inputs have ni>=1; the two numerator gaps
# are nonnegative polynomials in other, extra.
check('annihilation weighted coefficient denominator margin',
      s.expand((ni+other-1+(1+extra))-ni)==other+extra)
check('creation weighted coefficient denominator margin',
      s.expand((ni+other+1+(1+extra))-(ni+1))==other+1+extra)

result={'passed':len(checks),'failed':0,'constant_exact':str(K),
        'constant_decimal':str(s.N(K,18)),'checks':checks,
        'scope':'Finite algebra controls; the accompanying note supplies the all-energy analytic proof.'}
Path(__file__).with_name('inverse_synthesis_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
