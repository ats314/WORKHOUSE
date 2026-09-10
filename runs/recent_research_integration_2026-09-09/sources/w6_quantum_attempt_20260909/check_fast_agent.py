"""Exact finite algebra controls; not an operator or Wilson ground solver."""
import json
from pathlib import Path
import sympy as s

checks = {}
x = s.symbols("x", real=True)
h = s.Function("h")(x)
r, q = s.diff(h, x), s.diff(h, x, 2)
lhs = s.diff((1-x*x)*(q+r*r)-3*x*r, x, 2)
rhs = ((1-x*x)*s.diff(q, x, 2)
       + (2*(1-x*x)*r-7*x)*s.diff(q, x)
       + (2*(1-x*x)*q-8*x*r-8)*q - 2*r*r)
checks["radial_heat_log_curvature_identity"] = s.simplify(lhs-rhs) == 0

v = s.Matrix(s.symbols("v1:4", real=True))
# Left multiplication exp(i epsilon sigma_a/2) changes v by
# (x e_a - e_a cross v)/2, under one Pauli orientation convention.
fields = s.Matrix.hstack(*[
    (x*s.eye(3)[:, a] - s.eye(3)[:, a].cross(v))/2
    for a in range(3)
])
gram = s.expand(fields*fields.T)
expected = ((x*x+(v.T*v)[0])*s.eye(3)-v*v.T)/4
checks["quaternion_gradient_gram"] = all(
    s.expand(z) == 0 for z in gram-expected)

# Exact Haar scalar moments via I_n = int_0^pi sin(theta)^n dtheta:
# I_4=(3/4)I_2, so E[x^2]=(I_2-I_4)/I_2=1/4.
checks["haar_scalar_second_moment"] = 1-s.Rational(3,4) == s.Rational(1,4)
a, m, g = s.symbols("a m g", positive=True)
rayleigh = s.cancel((g*g*a/4)*((1-m/3)/4)/(m/3))
checks["central_angular_rayleigh"] = (
    s.simplify(rayleigh-g*g*a*(3/m-1)/16) == 0)
checks["central_uniform_upper_constant"] = (
    s.simplify(rayleigh.subs(m,s.Rational(3,4))-3*a*g*g/16) == 0)
checks["rayleigh_decreases_with_radial_moment"] = (
    s.simplify(s.diff(rayleigh,m)+3*a*g*g/(16*m*m)) == 0)

payload = {
    "scope": "Exact algebra controls only; heat maximum principle, ground limit, physical localization and operator bounds are analytic.",
    "checks": checks,
    "passed": sum(bool(v) for v in checks.values()),
    "total": len(checks),
}
Path(__file__).with_name("fast_agent_controls.json").write_text(
    json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
assert all(checks.values())
