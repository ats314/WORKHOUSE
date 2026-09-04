import sys
sys.path.insert(0, "/home/user/WORKHOUSE/src")
import sympy as sp
from workhouse import cellular as CELL

z = sp.symbols("z1 z2 z3")
d    = [z[j] - 1 for j in range(3)]
dbar = [1/z[j] - 1 for j in range(3)]
a    = [sp.expand(2 - z[j] - 1/z[j]) for j in range(3)]
PLANES = [(1, 2), (1, 3), (2, 3)]
psi     = sp.Matrix([dbar[2], -dbar[1], dbar[0]])
psi_dag = sp.Matrix([[d[2], -d[1], d[0]]])
CUBE_FACES = [((0,0,0),(1,2),-1), ((0,0,1),(1,2),+1),
              ((0,0,0),(1,3),+1), ((0,1,0),(1,3),-1),
              ((0,0,0),(2,3),-1), ((1,0,0),(2,3),+1)]
def bloch(pairs, amp=1):
    H = sp.zeros(3, 3)
    for (xa,Pa,ea),(xb,Pb,eb) in pairs:
        H[PLANES.index(Pb), PLANES.index(Pa)] += amp*ea*eb*sp.prod([z[i]**(xb[i]-xa[i]) for i in range(3)])
    return H
cross = [(f,g) for f in CUBE_FACES for g in CUBE_FACES if f[1] != g[1]]
H = bloch(cross)
print("rotation matrix, unit amplitude:")
for i in range(3):
    print("   ", [sp.factor(sp.expand(H[i,j])) for j in range(3)])
num = sp.expand(sp.cancel(sp.together((psi_dag * H * psi)[0,0])))
print()
print("psi^dag H psi =", sp.factor(sp.simplify(num)))
# is it real? compare with its conjugate (z -> 1/z)
conj = sp.expand(sp.cancel(num.subs({z[i]: 1/z[i] for i in range(3)}, simultaneous=True)))
print("Hermitian (num == conj)?", sp.simplify(sp.cancel(num - conj)) == 0)
# express in a_j if possible
A1,A2,A3 = sp.symbols("a1 a2 a3")
sub = sp.solve([a[i] - [A1,A2,A3][i] for i in range(3)], list(z), dict=True)
print()
print("as a polynomial in a_j?")
try:
    p = sp.Poly(sp.cancel(num), *z)
    print("   Laurent degrees:", p.monoms()[:6], "...")
except Exception as exc:
    print("   ", exc)
