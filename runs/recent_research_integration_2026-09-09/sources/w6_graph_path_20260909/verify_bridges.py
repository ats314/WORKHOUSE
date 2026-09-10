"""Exact controls for two analytic bridges; not a coupled Wilson proof."""
import json
from pathlib import Path
import sympy as s

OUT=Path(__file__).resolve().parent
checks=[]


def check(name, ok, detail):
    assert bool(ok),name
    checks.append(dict(name=name,passed=True,detail=detail))


alpha,kappa,C=s.symbols("alpha kappa C", positive=True)
radius=kappa/(2*C)
check("fast Hessian radius cancels coupling",
      s.simplify(alpha*(kappa-C*radius)-alpha*kappa/2)==0,
      "The local tangent conclusion is analytic under the stated Hessian and fast-source form estimates.")

# Correlated Gaussian controls. The energy is sum_i |partial_i f|^2.
# Q=I+theta L_path >= I for every size; its Gaussian is nonproduct.
theta=s.Rational(1,3)
for n in (2,3,4,6):
    lap=s.zeros(n)
    for i in range(n-1):
        v=s.zeros(n,1); v[i]=1; v[i+1]=-1
        lap+=v*v.T
    Q=s.eye(n)+theta*lap
    cov=Q.inv()
    check(f"correlated linear inverse energy n={n}",
          s.eye(n)-cov**2 == cov*(2*theta*lap+theta**2*lap**2)*cov
          and cov[0,1]!=0,
          "Inverse energy a*Q^-2 a <= ||a||^2 follows from the displayed positive factorization. Offdiagonal covariance is nonzero.")

# The inverse energy differs from the covariance: the Witten power is two.
D=s.Matrix([[2,1],[0,1]])
H=D.T*D
W=D*D.T
check("Witten inverse-square bridge",
      D.T*W.inv()**2*D == H.inv()
      and D.T*W.inv()*D == s.eye(2)
      and H.inv()!=s.eye(2),
      "On the centered scalar sector H=D*D; the single inverse gives covariance, the double inverse gives H^-1.")

# Nonlinear centered local profiles f_i=x_i^2-Cov_ii in a correlated Gaussian.
# Solve D_OU^{-1} q by QB+BQ=A for diagonal profile coefficient A.
n=3
lap=s.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
Q=s.eye(n)+theta*lap
cov=Q.inv()
A=s.diag(1,-2,1)
unknowns=s.symbols("b0:9")
B=s.Matrix(n,n,unknowns)
sol=s.solve(list(Q*B+B*Q-A),unknowns)
B=B.subs(sol)
inverse_energy=s.simplify(2*s.trace(A*cov*B*cov))
gradient_energy=s.simplify(4*s.trace(A*A*cov))
check("coupled nonlinear derivative synthesis",
      B==B.T and Q*B+B*Q==A and 0<inverse_energy<=gradient_energy<=4*s.trace(A*A),
      f"Centered local squares: exact inverse energy {inverse_energy}, gradient energy {gradient_energy}; bound 4 sum a_i^2={4*s.trace(A*A)}. Independence is not used.")

report={"scope":"Exact finite controls plus an all-size positive matrix factorization. General closed-form, fiber and Wilson claims retain their stated analytic hypotheses.","checks":checks}
(OUT/"bridge_checks.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(f"{len(checks)}/{len(checks)} exact bridge controls passed")
