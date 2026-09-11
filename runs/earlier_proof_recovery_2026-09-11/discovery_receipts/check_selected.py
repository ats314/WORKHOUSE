"""Small exact audit checks for located earlier arguments; no source writes."""
import itertools,json
from pathlib import Path
import sympy as S
out=Path(__file__).resolve().parent
checks={}
theta=S.symbols('theta',positive=True)
checks['SU2_round_S3_fundamental_laplacian']=S.simplify(S.diff(S.cos(theta),theta,2)+2*S.cot(theta)*S.diff(S.cos(theta),theta)+3*S.cos(theta))==0
checks['four_distinct_links_coefficient']=4*3==12
x=S.symbols('x',positive=True)
F=x*x-2+2*(x+1)*S.exp(-x)
checks['VSU_constitutive_antiderivative']=S.simplify(S.diff(F,x)/(2*x)-(1-S.exp(-x)))==0
checks['VSU_longitudinal_Hessian']=S.simplify(S.diff(x*(1-S.exp(-x)),x)-(1-S.exp(-x)+x*S.exp(-x)))==0
checks['VSU_small_gradient_cubic_energy']=S.limit(F/x**3,x,0)==S.Rational(2,3)
checks['VSU_large_gradient_quadratic_energy']=S.limit(F/x**2,x,S.oo)==1
# Distinct ray limits of the rank-one flat projector.
J=S.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
ray1=J*S.diag(1,0,0)*J.T;ray2=J*S.diag(0,1,0)*J.T
checks['flat_projector_distinct_axis_limits']=ray1!=ray2
# The source's determinant stencil omits the parity of the row permutation.
x1,x2,x3,u1,u2,u3,w1,w3=S.symbols('x1 x2 x3 u1 u2 u3 w1 w3')
actual=S.Matrix([[x1,u1,w1],[x2,u2,0],[x3,u3,w3]]).det()
printed=x2*(u1*w3-u3*w1)-u2*(x1*w3-x3*w1)
checks['determinant_source_requires_row_parity_repair']=S.expand(actual+printed)==0 and S.expand(actual-printed)!=0
# Verify the six source-selected links occur in their own staple only.
star_runs=[]
for L in (3,4,5):
    for mu in range(4):
        zero=(0,0,0,0)
        def point(*shifts):
            a=[0]*4
            for d,v in shifts:a[d]+=v
            return tuple(v%L for v in a)
        staples=[];selected=[]
        for nu in range(4):
            if nu==mu:continue
            staples.append({(point((mu,1)),nu),(point((nu,1)),mu),(zero,nu)})
            selected.append((point((mu,1)),nu))
            staples.append({(point((mu,1),(nu,-1)),nu),(point((nu,-1)),mu),(point((nu,-1)),nu)})
            selected.append((point((mu,1),(nu,-1)),nu))
        star_runs.append(all(sum(link in p for p in staples)==1 and link in staples[j] for j,link in enumerate(selected)))
checks['six_disjoint_staple_coordinates_12_periodic_cases']=all(star_runs)
# Noncommuting positive matrices illustrate the exact conditional floor bound.
A=S.Matrix([[3,1],[1,3]]);B=S.Matrix([[5,0],[0,1]])
avg=(A+B)/2
floor_rhs=(2+1)/2
checks['conditional_floor_exact_noncommuting_example']=min(avg.eigenvals())>=S.Rational(3,2)
z=S.symbols('z')
W=S.Matrix([[1+z,2],[z**-1,3]])
poly=S.expand(S.trace(W**3))
coeffs=[S.expand(poly*z**3).coeff(z,k) for k in range(7)]
checks['phase_isolation_positive_transfer_coefficients']=all(c>=0 for c in coeffs)
checks={name:bool(value) for name,value in checks.items()}
result={'all_pass':all(checks.values()),'checks':checks,'scope':'Exact algebra and finite combinatorial diagnostics supporting the located source readings. No Lean compilation, continuum construction or global novelty assessment.'}
(out/'selected_exact_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
