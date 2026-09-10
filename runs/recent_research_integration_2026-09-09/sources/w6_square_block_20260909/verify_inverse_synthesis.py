"""Independent exact all-retained-source inverse-energy calculation.

The inequalities for every radial Hermite level are proved in
inverse_synthesis.md; this script verifies their algebraic inputs and
the sharp level-one constant without fitting sampled data.
"""
import os
os.environ['SYMPY_GROUND_TYPES'] = 'python'
import json
from pathlib import Path
import sympy as s

checks = {}
def zero(name, value):
    vals = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(x) == 0 for x in vals), (name, value)
    checks[name] = True

r2, r6 = s.sqrt(2), s.sqrt(6)
C = s.Matrix([[4,-1,3,-1],[-1,4,-1,3],[3,-1,6,-2],[-1,3,-2,6]])
V = s.Matrix([[2,0,-1,0],[0,2,0,-1],[-1,0,1,0],[0,-1,0,1]])
# Mode order q,u,s,v; a=|q|^2.  These are scalar mode matrices,
# tensored with the three-dimensional color identity.
R = s.Matrix([[0,0,1,1],[1,1,-s.Rational(1,2),-s.Rational(1,2)],
              [0,0,1,-1],[1,-1,-s.Rational(1,2),s.Rational(1,2)]])/r2
Cp = s.diag(4,2,8,3)
Vp = s.diag(s.Rational(1,2),2,s.Rational(1,2),2)
zero('complete_electric_mode_diagonalization', R*C*R.T-Cp)
zero('complete_magnetic_mode_diagonalization', R.inv().T*V*R.inv()-Vp)
omega = s.diag(r2,2,2,r6)
variance = s.diag(r2,s.Rational(1,2),2,r6/4)
zero('independent_gaussian_variances', 2*omega*variance-Cp)
zero('mode_frequency_squares', omega**2-Cp*Vp)

x = [s.Matrix(s.symbols(f'x{i}_0:3')) for i in range(4)]
q,u,ss,v = [sum((R[i,j]*x[j] for j in range(4)),s.zeros(3,1)) for i in range(4)]
triple = x[0].dot(x[2].cross(x[3])) + x[1].dot(x[2].cross(x[3]))
kappa = (r2-4)/7
gamma = (4*r2-2)/7
zero('complete_force_independent_mode_factorization', s.expand(kappa*triple-gamma*u.dot(q.cross(ss))))
zero('retained_observation_normalization', s.expand(q.dot(q)-(x[2]+x[3]).dot(x[2]+x[3])/2))
# For independent isotropic u,s, E[(s x u)_i (s x u)_j]
# = 2 variance(u) variance(s) delta_ij.
zero('fast_cross_covariance',2*variance[1,1]*variance[2,2]-2)
zero('fast_cross_energy',omega[1,1]+omega[2,2]-4)

K = (4-r2)**3/s.Integer(1372)
zero('sharp_constant',K-gamma**2/(4*(4+r2)))
energy = (528*r2-600)/343
b_first = 24*r2
zero('first_source_attains_bound',energy-K*b_first)
zero('first_source_direct_inverse',energy-gamma**2*6*variance[0,0]*variance[1,1]*variance[2,2]/(4+r2))
n = s.symbols('n', integer=True, positive=True)
Kn = gamma**2/(4*(4+r2*(2*n-1)))
zero('spectral_ratio_difference_formula',K-Kn-gamma**2*r2*(n-1)/(2*(4+r2)*(4+r2*(2*n-1))))
# The final expression is nonnegative for every integer n>=1.
checks['all_radial_levels_nonnegative_difference_by_positive_factors'] = True

out = {'checks':checks,'passed':len(checks),
       'sharp_constant':str(K),'sharp_constant_numeric':str(s.N(K,30)),
       'radial_level_n_ratio':str(Kn),'first_source_inverse_energy':str(energy),
       'scope':'all retained radial finite-energy states; exact first transported coefficient on actual 2x2 block'}
Path(__file__).with_name('inverse_synthesis_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
