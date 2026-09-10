"""Exact algebra checks supporting quantile_scale.md.

The analytic moment/elliptic/spectral arguments are in the report; these
checks do not replace them or assert conditional essential-supremum bounds.
"""
import json
from pathlib import Path
import sympy as s

checks = []
def check(name, condition):
    passed = bool(condition)
    checks.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)

k, V, E, g = s.symbols("k V E g", positive=True)
x = s.symbols("x", real=True)
check("one-face gradient comparison remainder",
      s.expand(8*4*(1-x)-16*(1-x*x)-16*(x-1)**2) == 0)
check("four-face Casimir", s.expand(12*(4-V/4)) == 48-3*V)
delta_upper = k*V**(k-1)*(48-3*V)+16*k*(k-1)*V**(k-1)
check("moment Laplacian upper bound difference",
      s.simplify(16*k*(k+2)*V**(k-1)-delta_upper-3*k*V**k) == 0)
check("Agmon exponent gradient coefficient", s.Rational(1,2)*s.Rational(1,4)**2*16 == s.Rational(1,2))
moments = [s.Integer(1), E]
for n in range(1, 5):
    moments.append(s.expand(E*moments[-1]+4*n*(n+2)*moments[-2]))
check("second quantum moment", moments[2] == E**2+12)
check("third quantum moment", moments[3] == E**3+44*E)
check("fourth quantum moment", moments[4] == E**4+104*E**2+720)

M=E+4
check("factorial moment majorant polynomial",
      s.expand(M*M*(k+1)-E*M-4*(k+2)-((E**2+8*E+12)*k+4*E+8)) == 0)
check("twelve-dimensional ground score variance", 12*(s.Rational(3,4)-s.Rational(1,2)**2) == 6)
check("nine-dimensional conditional score variance", 9*(s.Rational(3,4)-s.Rational(1,2)**2) == s.Rational(9,2))
check("dyadic ground overlap", s.Rational(4,5)**6 == s.Rational(4096,15625))
check("dyadic squared ground distance", 2-2*s.Rational(4,5)**6 == s.Rational(23058,15625))
a=s.symbols("a", positive=True)
P=s.diag(1,0)
Pprime=s.Matrix([[0,a],[a,0]])
K=Pprime*P-P*Pprime
check("projection derivative singular values", Pprime.T*Pprime == a*a*s.eye(2))
check("Kato generator singular values", K.T*K == a*a*s.eye(2))
check("antipodal constrained potential", s.expand(4*(4-2*s.sqrt(2))) == 16-8*s.sqrt(2))

result={"checks": checks, "passed":len(checks),
        "failed":0, "moment_polynomials":[str(p) for p in moments],
        "scope":"Exact supporting algebra only; analytic proof is in quantile_scale.md."}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"passed":len(checks), "failed":0}))
