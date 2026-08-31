import sys
sys.path.insert(0, "/home/user/WORKHOUSE/src")
import sympy as sp
from itertools import permutations

z = sp.symbols("z1 z2 z3")
d, dbar = [z[j]-1 for j in range(3)], [1/z[j]-1 for j in range(3)]
PLANES = [(1,2),(1,3),(2,3)]
psi     = sp.Matrix([dbar[2], -dbar[1], dbar[0]])
psi_dag = sp.Matrix([[d[2], -d[1], d[0]]])
CUBE = [((0,0,0),(1,2),-1), ((0,0,1),(1,2),+1),
        ((0,0,0),(1,3),+1), ((0,1,0),(1,3),-1),
        ((0,0,0),(2,3),-1), ((1,0,0),(2,3),+1)]
def bloch(pairs):
    H = sp.zeros(3,3)
    for (xa,Pa,ea),(xb,Pb,eb) in pairs:
        H[PLANES.index(Pb), PLANES.index(Pa)] += ea*eb*sp.prod([z[i]**(xb[i]-xa[i]) for i in range(3)])
    return H
cross = [(f,g) for f in CUBE for g in CUBE if f[1] != g[1]]
num = sp.cancel(sp.together((psi_dag * bloch(cross) * psi)[0,0]))

def same(e1, e2_): return sp.simplify(sp.cancel(sp.together(e1 - e2_))) == 0

# (a) permutation invariance of the three axes
perm_ok = all(same(num, num.subs({z[i]: z[p[i]] for i in range(3)}, simultaneous=True))
              for p in permutations(range(3)))
# (b) parity k -> -k in one axis (z1 -> 1/z1)
par_ok = same(num, num.subs({z[0]: 1/z[0]}, simultaneous=True))
print("cubic permutation invariant:", perm_ok)
print("axis-parity invariant     :", par_ok)

# (c) what RANGE does it carry? highest |exponent| after clearing denominators
p = sp.Poly(sp.expand(num * sp.prod([zz**2 for zz in z])), *z)
degs = [max(m[i] for m in p.monoms()) - 2 for i in range(3)]
mins = [min(m[i] for m in p.monoms()) - 2 for i in range(3)]
print("displacement range per axis: max %s, min %s" % (degs, mins))

# (d) the shape basis is {1, q, e2, 4e2/q, e3/q}. Try it, then try adding the
#     range-2 invariant sum_j a_j^2 = q^2 - 2 e2 (already in span) and the
#     genuinely new range-2 shape p2 = sum_j a_j * (a_j - ...)? Test the span directly.
a  = [2 - z[j] - 1/z[j] for j in range(3)]
q  = sum(a); e2 = a[0]*a[1]+a[0]*a[2]+a[1]*a[2]; e3 = a[0]*a[1]*a[2]
c0,A,B,C,D = sp.symbols("c0 A B C D")
resid = sp.expand(sp.cancel(sp.together(num - (c0*q + A*q**2 + B*e2*q + C*4*e2 + D*e3)) * sp.prod([zz**3 for zz in z])))
sol = sp.solve(sp.Poly(resid, *z).coeffs(), [c0,A,B,C,D], dict=True)
print("in the 4-shape span:", bool(sol))
