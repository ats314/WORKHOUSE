"""Same computation, as Laurent polynomials in z_j = e^{i k_j}: exact and fast."""
import sys
sys.path.insert(0, "/home/user/WORKHOUSE/src")
import sympy as sp
from workhouse import cellular as CELL

z = sp.symbols("z1 z2 z3")
d    = [z[j] - 1 for j in range(3)]           # d_j = e^{ik_j} - 1
dbar = [1/z[j] - 1 for j in range(3)]         # conj on |z| = 1
a    = [2 - z[j] - 1/z[j] for j in range(3)]  # a_j = |d_j|^2
q  = sum(a)
e2 = a[0]*a[1] + a[0]*a[2] + a[1]*a[2]
e3 = a[0]*a[1]*a[2]
PLANES = [(1, 2), (1, 3), (2, 3)]
psi     = sp.Matrix([dbar[2], -dbar[1], dbar[0]])     # (d3bar, -d2bar, d1bar)
psi_dag = sp.Matrix([[d[2], -d[1], d[0]]])            # conjugate transpose

CUBE_FACES = [((0,0,0), (1,2), -1), ((0,0,1), (1,2), +1),
              ((0,0,0), (1,3), +1), ((0,1,0), (1,3), -1),
              ((0,0,0), (2,3), -1), ((1,0,0), (2,3), +1)]

def bloch(pairs, amp):
    H = sp.zeros(3, 3)
    for (xa, Pa, ea), (xb, Pb, eb) in pairs:
        phase = sp.prod([z[i] ** (xb[i] - xa[i]) for i in range(3)])
        H[PLANES.index(Pb), PLANES.index(Pa)] += amp * ea * eb * phase
    return H

same  = [(f, g) for f in CUBE_FACES for g in CUBE_FACES if f is not g and f[1] == g[1]]
cross = [(f, g) for f in CUBE_FACES for g in CUBE_FACES if f[1] != g[1]]

c_opp,  _, _ = CELL.c_prim(CELL.CUBE, 0, 1)
c_perp, _, _ = CELL.c_prim(CELL.CUBE, 0, 2)
print("c_opp  =", c_opp,  " N=3:", sp.nsimplify(c_opp.subs(CELL.N, 3)))
print("c_perp =", c_perp, " N=3:", sp.nsimplify(c_perp.subs(CELL.N, 3)))
print("pairs: same-plane %d, cross-plane %d" % (len(same), len(cross)))

c0s, As, Bs, Cs, Ds = sp.symbols("c0 A B C D")
CLEAR = sp.prod([zz**3 for zz in z])          # clears every negative power present

def shape(H, label):
    num = sp.expand((psi_dag * H * psi)[0, 0])
    resid = sp.expand(sp.together(num - (c0s*q + As*q**2 + Bs*e2*q + Cs*4*e2 + Ds*e3)) * CLEAR)
    resid = sp.expand(sp.cancel(resid))
    eqs = sp.Poly(resid, *z).coeffs()
    sol = sp.solve(eqs, [c0s, As, Bs, Cs, Ds], dict=True)
    print(f"{label}: {sol[0] if sol else 'NOT IN THE SHAPE SPAN'}")
    return sol[0] if sol else None

Hn, Hr = bloch(same, c_opp), bloch(cross, c_perp)
print("H_normal diagonal:", [sp.simplify(Hn[i, i]) for i in range(3)])
print("H_rot[1,0] =", sp.factor(sp.expand(Hr[1, 0])))
n = shape(Hn, "NORMAL   (opposite faces)")
r = shape(Hr, "ROTATION (perpendicular) ")
if n and r:
    print()
    for nm, s in (("normal", n), ("rotation", r)):
        print(f"  {nm:9s} A = {sp.simplify(s[As])}   C = {sp.simplify(s[Cs])}")
    print()
    print("  C_normal / A_normal =", sp.simplify(n[Cs]/n[As]), "   (convention-free ratio)")
    print("  C_rot    / A_normal =", sp.simplify(r[Cs]/n[As]), "   (convention-free ratio)")
    print("  A_rot               =", sp.simplify(r[As]))
