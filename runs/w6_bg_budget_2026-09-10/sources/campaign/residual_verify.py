"""Exact finite controls for residual_analysis.md; no external packages."""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path

checks = []


def check(name, condition, detail):
    assert condition, (name, detail)
    checks.append({"name": name, "passed": True, "detail": str(detail)})


def dot(u, v):
    return sum(a*b for a, b in zip(u, v))


def mv(a, v):
    return [dot(row, v) for row in a]


def quad(a, u, v=None):
    return dot(u, mv(a, u if v is None else v))


# Coefficient jets of H_(1+x)=g^2*T/2+g^-2*V through x^3.
T = [[F(2), F(-1)], [F(-1), F(2)]]
V = [[F(0), F(0)], [F(0), F(3, 4)]]
kin = [F(1, 2), F(1), F(1, 2), F(0)]
pot = [F(1), F(-2), F(3), F(-4)]
Hs = [[[kin[k]*T[i][j]+pot[k]*V[i][j] for j in range(2)]
       for i in range(2)] for k in range(4)]
trace = [a[0][0]+a[1][1] for a in Hs]
det = [sum(Hs[i][0][0]*Hs[k-i][1][1]
           - Hs[i][0][1]*Hs[k-i][1][0] for i in range(k+1))
       for k in range(4)]

# Solve the characteristic equation for the simple ground eigenvalue jet.
es = [F(3, 4)]
for k in range(1, 4):
    rest = sum(es[i]*es[k-i] for i in range(1, k))
    rest -= sum(trace[i]*es[k-i] for i in range(1, k+1))
    rest += det[k]
    es.append(-rest/(2*es[0]-trace[0]))
ej = [es[0], es[1], 2*es[2], 6*es[3]]
check("noncommuting_ground_energy_jets", ej == [F(3, 4), F(9, 10), F(-51, 250), F(22446, 3125)], ej)

H0, H1 = Hs[:2]
H2 = [[2*x for x in row] for row in Hs[2]]
H3 = [[6*x for x in row] for row in Hs[3]]
omega, fast = [F(2), F(1)], [F(-1), F(2)]  # each has norm sqrt(5)
gap = F(5, 4)
chi_coeff = -quad(H1, fast, omega)/(5*gap)
chi_energy = gap*chi_coeff**2
check("ground_derivative_resolvent_coefficient", chi_coeff == F(24, 25), chi_coeff)
check("ground_second_derivative_identity", ej[2] == quad(H2, omega)/5 - 2*chi_energy, ej[2])
third = quad(H3, omega)/5 + 6*chi_coeff*quad(H2, fast, omega)/5
third += 6*chi_coeff**2*(quad(H1, fast)/5-ej[1])
check("ground_third_derivative_normalization_term", third == ej[3], third)

E, gamma = F(1), F(1)
h = 1+E/gamma
Ej = [2*E, E*(6+8*h), E*(24+72*h+48*h*(1+2*E/gamma))]
for j in range(3):
    check(f"ground_derivative_constant_{j+1}", abs(ej[j+1]) <= Ej[j], Ej[j])

# Normalization identities for a real normalized moving vector.
omega_jets = [[F(1), F(0)], [F(0), F(1)],
              [F(-1), F(0)], [F(0), F(-1)]]
for n in range(1, 4):
    rhs = -sum(F(comb(n, i), 2)*dot(omega_jets[i], omega_jets[n-i])
               for i in range(1, n))
    check(f"ground_jet_vacuum_normalization_{n}",
          dot(omega_jets[n], omega_jets[0]) == rhs, rhs)

# Exact multinomial enumeration for differentiated R* L R.
r = [F(1), F(2), F(7), F(31)]
v = [F(1), F(5), F(13), F(41)]
listed = [v[1]+2*r[1],
          v[2]+4*v[1]*r[1]+2*(r[1]**2+r[2]),
          v[3]+6*v[2]*r[1]+6*v[1]*(r[1]**2+r[2])
          +2*(3*r[1]*r[2]+r[3])]
for j in range(1, 4):
    expanded = sum(F(factorial(j), factorial(a)*factorial(b)*factorial(c))
                   *r[a]*v[b]*r[c]
                   for a in range(j+1) for b in range(j-a+1)
                   for c in [j-a-b])
    check(f"transport_leibniz_constant_{j}", expanded == listed[j-1], expanded)

for old, new, tau0, tau1 in [(F(2), F(3), F(1, 2), F(1, 3)),
                            (F(-2), F(1, 5), F(3), F(2))]:
    check("physical_clock_product_difference",
          new/tau1-old/tau0 == (new-old)/tau1+(1/tau1-1/tau0)*old,
          (old, new, tau0, tau1))

base = Path(__file__).resolve().parent
out = {"verification": "exact rational finite controls; analytic operator proof separate",
       "source_sha256": {name: sha256((base/name).read_bytes()).hexdigest()
                         for name in ["residual_analysis.md", "residual_verify.py"]},
       "passed": len(checks), "checks": checks}
Path(__file__).with_name("residual_checks.json").write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"passed": len(checks), "output": "residual_checks.json"}))
