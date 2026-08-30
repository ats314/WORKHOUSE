"""Structure dictionary, worked in the band variables a_j where everything is polynomial."""
import sympy as sp

a1, a2, a3, g, f = sp.symbols("a1 a2 a3 g f", positive=True)
a = [a1, a2, a3]
q = a1 + a2 + a3
e2 = a1*a2 + a1*a3 + a2*a3
e3 = a1*a2*a3
cos = [1 - aj/2 for aj in a]          # a_j = 2 - 2 cos k_j

c0, A, B, C, D = sp.symbols("c0 A B C D")

def fit(num):
    """num = psi^dag H psi. Match eps4 = num/q against the shape ansatz."""
    resid = sp.expand(num - (c0*q + A*q**2 + B*e2*q + C*4*e2 + D*e3))
    eqs = sp.Poly(resid, a1, a2, a3).coeffs()
    sol = sp.solve(eqs, [c0, A, B, C, D], dict=True)
    return sol[0] if sol else "NOT IN THE SHAPE SPAN"

# |psi_n|^2 = a_n, so a diagonal H contributes sum_n a_n * H_nn.
print("scalar I                    ", fit(g * q))
print("normal translation g cos k_n", fit(sp.expand(g * sum(a[n]*cos[n] for n in range(3)))))
print("in-plane translation        ",
      fit(sp.expand(g * sum(a[n]*sum(cos[m] for m in range(3) if m != n) for n in range(3)))))

# Orbital rotation: psi^dag R psi = f * sum_{n != m} eps_n eps_m a_n a_m.
# The cubic-covariant choice is all products entering with one sign.
print("orbital rotation (covariant)", fit(sp.expand(f * 2 * e2)))
print("orbital rotation (raw signs)", fit(sp.expand(f * 2 * (-a1*a2 + a1*a3 - a2*a3))))
