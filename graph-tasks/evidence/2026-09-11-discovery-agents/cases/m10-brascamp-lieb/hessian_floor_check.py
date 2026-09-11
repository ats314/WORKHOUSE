"""Scratch check (i)-(iii) for case m10-brascamp-lieb. Not repository evidence.
Conventions: transport-obstruction S7: S_2 - min S_2 = |a+b|^2/4 + |c|^2/4 + (sqrt6/12)|a-b-c|^2,
per color (a,b,c) in R^3 each; B(0) = Hess S_2 so q = (1/2) x^T B(0) x, B(0) = 2M.
Psi_g = g^-6 A_g exp(-S/g^2)  =>  -2 log Psi_g = 12 log g - 2 log A_g + 2 S/g^2.
"""
import json, sympy as sp
a,b,c,g=sp.symbols('a b c g',positive=True)
q=(a+b)**2/4+c**2/4+sp.sqrt(6)/12*(a-b-c)**2
x=sp.Matrix([a,b,c])
M=sp.hessian(q,(a,b,c))/2            # q = x^T M x
B0=2*M                                # S7 quadratic Hessian per color
ev=[sp.nsimplify(sp.simplify(e)) for e in B0.eigenvals()]
evn=sorted([float(sp.N(e)) for e in B0.eigenvals() for _ in range(B0.eigenvals()[e])])
# check drift coefficient m(q)^T B(0) m(q) = (6+sqrt6)|q|^2/24 with m = (1/4,1/4,1/2)|q|
m=sp.Matrix([sp.Rational(1,4),sp.Rational(1,4),sp.Rational(1,2)])
drift=sp.simplify((m.T*B0*m)[0])
# Hessian of -2 log Psi in fast coordinates: (2/g^2) B(0) + O(1) amplitude term
floor_c = 2*min(evn)       # Hess(-2 log Psi) >= (2 lambda_min(B0)/g^2) I  - 2 Hess log A_g
# Brascamp-Lieb for quadratic S with fiber potential W = 2S/g^2 (+ const), f arbitrary:
# Var(f) <= E[ grad f^T (2 B/g^2)^{-1} grad f ] = (g^2/2) E[grad f^T B^{-1} grad f]
# For f = 2S/g^3 (undilated score fast part): grad f = 2 B eta / g^3, so
# Var <= (g^2/2) (4/g^6) E[eta^T B eta] = (2/g^4) E[eta^T B eta] = (4/g^4) E[S - Smin]
# Under the Gaussian fiber law exp(-2S/g^2): E[S - Smin] = 9 g^2/4 (equipartition: 9 dims, each (1/2)*(g^2/2))
lam=sp.symbols('lambda',positive=True)
eta=sp.symbols('eta',real=True)
# one-dimensional check of equipartition and independence of lambda:
dens=sp.exp(-2*(lam*eta**2/2)/g**2)
Z=sp.integrate(dens,(eta,-sp.oo,sp.oo))
ES=sp.simplify(sp.integrate(lam*eta**2/2*dens,(eta,-sp.oo,sp.oo))/Z)          # = g^2/4, independent of lambda
VarS=sp.simplify(sp.integrate((lam*eta**2/2)**2*dens,(eta,-sp.oo,sp.oo))/Z-ES**2)  # = g^4/8, independent of lambda
BL_bound=sp.simplify((g**2/2)*sp.integrate((lam*eta)**2/lam*dens,(eta,-sp.oo,sp.oo))/Z)  # (g^2/2) E[(S')^2/lambda]
out={
 "B0_per_color":str(B0),
 "B0_eigenvalues_exact":[str(e) for e in ev],
 "B0_eigenvalues_numeric":evn,
 "drift_coefficient_m^T B0 m (expect (6+sqrt6)/24 = %.6f)"%float((6+sp.sqrt(6))/24):str(drift),
 "drift_numeric":float(drift),
 "fast_Hessian_floor_of_-2logPsi (times g^-2), c = 2*lambda_min(B0)":floor_c,
 "1d Gaussian S=lambda eta^2/2 under exp(-2S/g^2): E[S-Smin]":str(ES),
 "1d Var(S)":str(VarS),
 "1d Brascamp-Lieb bound on Var(S) = (g^2/2)E[S'^2/lambda]":str(BL_bound),
 "ratio BL/Var":str(sp.simplify(BL_bound/VarS)),
 "undilated fast score 2S/g^3: Var = 4 Var(S)/g^6 per dim":str(sp.simplify(4*VarS/g**6)),
 "note":"Var(S) and the BL bound are independent of lambda: BL applied to f=S is degeneration-uniform for a quadratic phase; H1 shape kappa_0 g^-2 per fast dimension (9 dims => 9/(2 g^2)).",
}
print(json.dumps(out,indent=1))
json.dump(out,open(__file__.replace('.py','.json'),'w'),indent=1)
