"""Audit the radial residual profile directly against the original X operator."""
import contextlib
import io
import json
from pathlib import Path
import runpy
import sympy as sp

folder=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    geo=runpy.run_path(str(folder/'verify_complete_force_geometry.py'))
    mom=runpy.run_path(str(folder/'residual_radial_moments.py'))
X=geo['X'];P=geo['P'];W=geo['W'];Y=geo['Y'];av=geo['a0']
flatX=[x for vec in X for x in vec];flatP=[p for vec in P for p in vec]
Tv=(X[0]+X[1]).dot(X[2].cross(X[3]))/sp.sqrt(2)
symbolterms=sp.Poly(W,*flatP).terms()
def principal_apply(f):
    result=0
    for powers,coef in symbolterms:
        indices=[flatX[i] for i,power in enumerate(powers) for _ in range(power)]
        result+=coef*sp.diff(f,*indices)
    return sp.expand(result)
subP=dict(zip(flatP,[-x for vec in Y for x in vec]))
drift=[sp.expand(sp.diff(W,p).subs(subP,simultaneous=True)) for p in flatP]
def normal_apply(f):return sp.expand(principal_apply(f)+sum(d*sp.diff(f,x) for d,x in zip(drift,flatX)))
U_actual=normal_apply(Tv)
# Coefficient of psi' in Wbar[T psi(a)]: derive using T*a and the constant part.
V_actual=sp.expand(normal_apply(Tv*av)-av*U_actual)
q,u,z,v=mom['q'],mom['u'],mom['z'],mom['v']
qb=u+q/2;rb=v+z/2
newX=[(qb+rb)/sp.sqrt(2),(qb-rb)/sp.sqrt(2),(q+z)/sp.sqrt(2),(q-z)/sp.sqrt(2)]
subsX=dict(zip(flatX,[x for vec in newX for x in vec]))
res1=sp.expand(U_actual.subs(subsX,simultaneous=True)-mom['WT'])
res2=sp.expand(V_actual.subs(subsX,simultaneous=True)-2*mom['A']*(mom['du']-mom['T']**2))
checks=[{'name':'original-complete-W1-on-triple-product','passed':res1==0},{'name':'original-complete-W1-first-radial-derivative','passed':res2==0}]
assert all(x['passed'] for x in checks),[sp.factor(res1),sp.factor(res2)]
result={'checks':checks,'passed':2,'total':2,'method':'Apply complete original X operator and source commutator before transforming to independent modes; then compare every coefficient.'}
(folder/'residual_original_operator_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
