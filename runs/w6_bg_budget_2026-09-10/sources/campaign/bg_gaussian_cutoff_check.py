"""Exact algebra controls of bg_analysis B2-B5a; no compact Wilson closure."""
import json
from pathlib import Path
import sympy as s

g, a, c, A = s.symbols('g a c A', positive=True)
theta = 2*s.sqrt(2)
h = theta*g**2
# Conditional u variance is g^2/2. Score is -chi(a) q.u/g^3.
chi = s.symbols('chi', real=True)
variance = s.simplify(chi**2*a*(g**2/s.Integer(2))/g**6)
assert variance == chi**2*a/(2*g**4)
# Lower integration factors on the two adjacent intervals; c is the
# actual probability normalization, which must cancel.
tail_lower = c*h*A**s.Rational(3,2)*s.exp(-A/h-1)/(2*g**4)
resistance_lower = h*s.exp(A/h-1)/(8*g**2*c*A**s.Rational(3,2))
product = s.simplify(tail_lower*resistance_lower)
assert s.simplify(product - s.exp(-2)/(2*g**2)) == 0
# Sharp endpoint-Laplace coefficient, independently from lower bounds.
assert s.simplify(theta**2/s.Integer(16)-s.Rational(1,2)) == 0
# Compact Haar endpoint product constants.
endpoint_product = s.simplify((s.Rational(2,3)*c*s.sqrt(2)) /
                             (g**2*c*s.sqrt(2)))
assert endpoint_product == 2/(3*g**2)
result = {'checks_passed': 4,
          'scope': 'Exact variance and tail-product algebra; analytic inequalities in bg_analysis.md',
          'gaussian_hardy_lower_bound': str(product),
          'actual_compact_uniform_Bg_proved': False}
Path(__file__).with_name('bg_gaussian_cutoff_checks.json').write_text(
    json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result))
