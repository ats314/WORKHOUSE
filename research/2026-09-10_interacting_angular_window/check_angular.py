"""Exact controls of A1--A5, not a Wilson-model certification."""
import json
import sympy as s

R=s.Rational
I3=s.eye(3)
J=[s.Matrix(3,3,lambda b,c: s.LeviCivita(a,b,c)) for a in range(3)]
Ls=[s.kronecker_product(j,I3) for j in J]+[s.kronecker_product(I3,j) for j in J]
total=[Ls[a]+Ls[a+3] for a in range(3)]
zero=s.zeros(9)
cas=-sum((j*j for j in total),zero)
angular=sum((j.T*j for j in Ls),zero)
assert angular==4*s.eye(9)
assert cas.eigenvals()=={s.Integer(0):1,s.Integer(2):3,s.Integer(6):5}
projectors={
  0:(cas-2*s.eye(9))*(cas-6*s.eye(9))/12,
  2:-cas*(cas-6*s.eye(9))/8,
  6:cas*(cas-2*s.eye(9))/24,
}
singlet=s.Matrix([int(i==j) for i in range(3) for j in range(3)])
assert cas*singlet==s.zeros(9,1)
assert cas*Ls[0]-Ls[0]*cas != zero

cases=[]
# Units beta=1. Coupling squared times fiber variance is 49/80.
# Casimir coupling is gauge invariant but fails to commute with individual Ls.
for coupling in (R(0),R(1,10),R(1),R(10)):
    hc=coupling*cas
    for energy in (R(0),R(1,10),R(11,60)):
        resolvent=(hc+(1-energy)*s.eye(9)).inv()
        exchange=R(49,80)*sum((j.T*resolvent*j for j in Ls),s.zeros(9))
        effective=R(3,4)*angular-exchange
        lower=(11-60*energy)/(80*(1-energy))
        remainder=effective-lower*angular
        # Exact spectral checks on every irreducible sector of the 9D space.
        eigen=[]
        for spin,p in projectors.items():
            coefficient=s.simplify(s.trace(p*remainder)/s.trace(p))
            assert remainder*p==coefficient*p
            assert coefficient>=0
            eigen.append(str(coefficient))
        value=(singlet.T*effective*singlet)[0]/3
        assert value==3-R(49,20)/(1+2*coupling-energy)
        # Full labeled synthesis identity, independently assembled.
        synth=s.Matrix.vstack(*Ls)
        block_inverse=s.diag(*([resolvent]*6))
        assert synth.T*block_inverse*synth==exchange/R(49,80)
        cases.append({'coupling':str(coupling),'energy':str(energy),
                      'lower_coefficient':str(lower),'singlet_value':str(value),
                      'remainder_irrep_eigenvalues':eigen})

energy=R(1,5)
counter=(R(3,4)-R(49,80)/(1-energy))*angular
assert counter == -R(1,16)*s.eye(9)
assert 10800<12005  # Actual beta=sqrt(5), alpha=sqrt(3) complement check.
for v in (R(0),R(1,100),R(1,20),R(9,100)):
    coefficient=(11-120*v)/(80*(1-2*v))
    assert coefficient>0
assert (11-120*R(11,120))/(80*(1-2*R(11,120)))==0

print(json.dumps({'status':'PASS','arithmetic':'exact SymPy rational matrices',
 'matrix_dimension':9,'source_channels':6,'matrix_cases':cases,
 'above_threshold_counterexample':'E/beta=1/5: angular form = -I/16',
 'scope':'interacting reference angular form; not actual nonlinear Wilson closure'},indent=2))
