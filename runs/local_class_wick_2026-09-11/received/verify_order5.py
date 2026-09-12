"""Verify the fifth perturbative order using independent Cartesian operators."""
import json
from pathlib import Path
import sympy as s
import wick_gap as w
import independent_su3 as c
root=Path(__file__).parent
data=json.loads((root/"coefficients_order5.json").read_text())
prior=json.loads((root/"coefficients_order4.json").read_text())
checks=[]
out={}
def gate(name,ok):
    assert ok,name
    checks.append(name)
    print("PASS",name,flush=True)
for parity in ("even","odd"):
    gate(f"{parity} reproducible overlapping orders",data["gaps"][parity]["g_series"][:5]==prior["gaps"][parity]["g_series"])
N=w.N
def parse(z): return s.sympify(z,locals={"N":N})
for parity in ("even","odd"):
    vals=list(map(parse,data["gaps"][parity]["g_series"]))
    for j,coef in enumerate(vals[1:],1):
        numerator,denominator=s.fraction(s.factor(-coef))
        gate(f"{parity} order {j} Laurent denominator",s.Poly(denominator,N).length()==1)
        z=s.Symbol("z")
        shift=4 if parity=="even" else 9
        poly=s.Poly(numerator,N)
        # Factoring introduces (N-1),(N+1) only in energies, not gap coefficients.
        in_z=sum(v*z**(m[0]//2) for m,v in poly.terms())
        gate(f"{parity} order {j} even numerator powers",all(m[0]%2==0 for m,v in poly.terms()))
        shifted=s.Poly(s.expand(in_z.subs(z,z+shift)),z)
        gate(f"{parity} order {j} strictly negative allowed-rank coefficient",all(q>0 for q in shifted.all_coeffs()))
        out.setdefault("positivity_witnesses",{})[f"{parity}_{j}"]={"shift":shift,"positive_coefficients_descending":[str(v) for v in shifted.all_coeffs()]}
    expected=s.Rational(-56673445,1528823808) if parity=="even" else s.Rational(-290599777,6115295232)
    gate(f"{parity} archived SU3 c4",s.cancel(36*vals[5].subs(N,3)-expected)==0)
delta=c.x*(c.x*c.x-3*c.y*c.y)
series=[c.solve(seed,5) for seed in (delta,delta*(c.x*c.x+c.y*c.y),delta*c.y*(3*c.x*c.x-c.y*c.y))]
for parity,es in zip(("even","odd"),series[1:]):
    gap=[s.factor(hi-lo) for hi,lo in zip(es,series[0])]
    target=list(map(s.sympify,data["gaps"][parity]["SU3_g_series"]))
    gate(f"independent Cartesian SU3 {parity} all six coefficients",gap==target)
    out.setdefault("SU3",{})[parity]=list(map(str,gap))
c.trace_even=lambda k:s.Rational(1,2**(k//2-1))*c.x**k
base=c.solve(c.x,5);exc=c.solve(c.x**3,5)
target=[parse(z).subs(N,2) for z in data["gaps"]["even"]["g_series"]]
gate("independent Cartesian SU2 even all six coefficients",[s.factor(a-b) for a,b in zip(exc,base)]==target)
out.update({"schema":"local-class-wick-order5-checks/v1","passed":len(checks),"failed":0,"checks":checks})
dest=root/"validation_order5.json"
assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(f"ALL {len(checks)} ORDER-FIVE CHECKS PASSED",flush=True)

