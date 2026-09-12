"""Independent archive, boundary and structural checks for the Wick engine."""
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
import sympy as s
import wick_gap as w

root=Path(__file__).parent
src=root/"sources"/"ENGINE_SUN_codd_local_gap_exact.py"
spec=importlib.util.spec_from_file_location("archived_wick",src)
a=importlib.util.module_from_spec(spec);sys.modules[spec.name]=a;spec.loader.exec_module(a)
N=w.N
checks=[]
def gate(name,ok):
    assert ok,name
    checks.append(name)
    print("PASS",name,flush=True)

# Independent full-GUE cut/join followed by trace subtraction versus direct
# traceless Laplacian. Include mixed traces and degrees up to fourteen.
monomials=[(2,), (4,), (6,), (2,2), (3,3), (4,4), (3,3,4), (3,3,6), (3,4,3,4), (2,2,2,2,2,2,2)]
for rank in (2,3,4,5,7):
    other=a.TracelessWick(rank)
    for m in monomials:
        val=other.moment(m)
        exact=s.Rational(val.numerator,val.denominator)
        gate(f"independent moment N={rank} traces={m}",s.cancel(w.moment(tuple(sorted(m))).subs(N,rank)-exact)==0)
data=json.loads((root/"coefficients_order4.json").read_text())
def parse(z): return s.sympify(z,locals={"N":N})
even=list(map(parse,data["gaps"]["even"]["g_series"]))
odd=list(map(parse,data["gaps"]["odd"]["g_series"]))
for rank in (3,4,5,7):
    z=a.compute_odd_coefficients(rank)
    gate(f"archive odd c0 N={rank}",odd[1].subs(N,rank)==s.Rational(z.c0.numerator,z.c0.denominator))
    gate(f"archive odd c1 N={rank}",odd[2].subs(N,rank)==s.Rational(z.q_total.numerator,z.q_total.denominator))

expected_even=[2,-(2*N**2-3)/(16*N),-(6*N**4-24*N**2+41)/(1024*N**2),-(60*N**6-401*N**4+1522*N**2-2297)/(98304*N**3),-(2970*N**8-27878*N**6+166512*N**4-546024*N**2+734405)/(37748736*N**4)]
expected_odd=[3,-3*(N**2-3)/(16*N),-(14*N**4-97*N**2+290)/(1536*N**2),-(95*N**6-981*N**4+5853*N**2-15335)/(98304*N**3)]
for parity,got,expected in (("even",even,expected_even),("odd",odd,expected_odd)):
    for j,z in enumerate(expected):
        gate(f"archived {parity} coefficient j={j} symbolic N",s.cancel(got[j]-z)==0)
gate("SU3 angular contribution retained",even[2].subs(N,3)-s.Rational(-327,9216)==s.Rational(1,576))
gate("SU2 odd norm vanishes",w.inner({(3,):s.S.One},{(3,):s.S.One}).subs(N,2)==0)
gate("SU2 even norm positive",w.inner(w.heat(w.monomial((2,)),-1),w.heat(w.monomial((2,)),-1)).subs(N,2)>0)

for m in ((2,),(3,),(4,),(3,4),(2,2,3),(3,3,4)):
    p=w.monomial(m)
    gate(f"heat inverse {m}",not w.add(w.heat(w.heat(p,1),-1),w.scale(p,-1)))
    eigen=w.heat(p,-1)
    gate(f"shell eigen-equation {m}",not w.add(w.number(eigen),w.scale(eigen,-sum(m))))

# A genuinely different low-rank quotient: SU2 Weyl-antisymmetric oscillator
# uses a single Cartesian variable and P_(2k)=2^(1-k) x^(2k).
import independent_su3 as c
c.trace_even=lambda k: 2**(1-k//2)*c.x**k if k==2 else s.Rational(1,2**(k//2-1))*c.x**k
base=c.solve(c.x,4)
exc=c.solve(c.x**3,4)
for j,(hi,lo) in enumerate(zip(exc,base)):
    gate(f"independent SU2 even coefficient j={j}",s.cancel(hi-lo-even[j].subs(N,2))==0)

out={"schema":"local-class-wick-validation/v1","passed":len(checks),"failed":0,"checks":checks}
(root/"validation.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(f"ALL {len(checks)} CHECKS PASSED",flush=True)

