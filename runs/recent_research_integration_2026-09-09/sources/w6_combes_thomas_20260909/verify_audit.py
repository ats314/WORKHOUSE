"""Exact controls for compression and lattice summation; not a Wilson solver."""
from fractions import Fraction as F
from pathlib import Path
import json

checks = {}
for n in (4, 8, 16, 32):
    q = [[F(int(i == j))-F(1,n) for j in range(n)] for i in range(n)]
    checks[f"cycle_{n}_projection"] = all(
        sum(q[i][k]*q[k][j] for k in range(n)) == q[i][j]
        for i in range(n) for j in range(n))
    checks[f"cycle_{n}_long_range_inverse_entry"] = q[0][n//2] == -F(1,n)
    # The embedded inverse is Q since A on range(Q) is the identity.
    checks[f"cycle_{n}_constant_annihilation"] = all(sum(row)==0 for row in q)

# r=e^{-mu}=1/2: sum_{j in Z} r^{|j|}=3, hence M_4=81.
r = F(1,2)
one_dim = 1+2*r/(1-r)
checks["geometric_one_dimensional_sum"] = one_dim == (1+r)/(1-r)
checks["four_dimensional_geometric_sum"] = one_dim**4 == 81
# Example relative hopping J=1/2 and kappa=1: e^mu=2 is admissible.
checks["relative_hopping_conjugation_threshold"] = F(1,2)*(1/r-1) == F(1,2)

# Four evaluations certify each displayed monic cubic characteristic
# polynomial identically: the difference has degree at most three.
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
hh=[[F(16,25),-F(12,25),F(0)],[-F(12,25),F(9,25),F(0)],
    [F(0),F(0),F(1,100)]]
vv=[[F(99,200),-F(99,200),F(0)],[-F(99,200),F(99,200),F(0)],
    [F(0),F(0),F(0)]]
def char_at(matrix, lam):
    return det3([[lam*int(i==j)-matrix[i][j] for j in range(3)] for i in range(3)])
points=list(map(F,(-2,0,1,3)))
checks["positive_jump_initial_characteristic_polynomial"] = all(
    char_at(hh,lam)==lam*(lam-F(1,100))*(lam-1) for lam in points)
hh1=[[hh[i][j]+vv[i][j] for j in range(3)] for i in range(3)]
checks["positive_jump_final_characteristic_polynomial"] = all(
    char_at(hh1,lam)==(lam-F(1,100))**2*(lam-F(99,50)) for lam in points)

payload = {"scope":"exact projection and geometric-series controls; CT and Wilson application have separate analytic hypotheses", "checks":checks, "passed":sum(checks.values()), "total":len(checks)}
assert all(checks.values())
Path(__file__).with_name("audit_checks.json").write_text(json.dumps(payload,indent=2)+"\n", encoding="utf-8")
print(json.dumps(payload,indent=2))
