"""Independent SU(2) strip Rayleigh correction in original product logarithms.

Uses the original seven-link electric form, not the balanced fiber metric.
Gaussian expectations are exact; this is a coefficient control, not an
independent global asymptotic remainder proof.
"""
import json
from pathlib import Path
import sympy as s

q = s.Matrix(s.symbols('q0:3'))
z = s.Matrix(s.symbols('z0:3'))
variables = list(q) + list(z)
aq, az = 1/s.sqrt(3), 1/s.sqrt(5)
x1, x2 = (q+z)/s.sqrt(2), (q-z)/s.sqrt(2)


def ad(x):
    return s.Matrix([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])


def average(expr):
    result = 0
    for powers, coefficient in s.Poly(s.expand(expr), *variables).terms():
        if any(n % 2 for n in powers):
            continue
        moment = s.Integer(1)
        for i, n in enumerate(powers):
            if n:
                moment *= s.factorial2(n-1) / (2*(aq if i < 3 else az))**(n//2)
        result += coefficient*moment
    return s.simplify(result)


def correction(p):
    dq = s.Matrix([s.diff(p, v)-aq*v*p for v in q])
    dz = s.Matrix([s.diff(p, v)-az*v*p for v in z])
    d1, d2 = (dq+dz)/s.sqrt(2), (dq-dz)/s.sqrt(2)
    a1, a2 = ad(x1), ad(x2)
    kinetic = -(d1.dot(a1*a1*d1)+d2.dot(a2*a2*d2))/6
    kinetic -= d1.dot(((a1*a1+a2*a2)/12+a1*a2/4)*d2)
    potential = -(x1.dot(x1)**2+x2.dot(x2)**2)*p*p/96
    norm = average(p*p)
    # Product Haar correction to a harmonic eigenfunction's quotient is
    # the state-independent constant -1, so it cancels in excitation gaps.
    return {"kinetic": s.simplify(average(kinetic)/norm),
            "potential": s.simplify(average(potential)/norm),
            "haar": s.Integer(-1), "norm": norm}


def main():
    ground = correction(s.Integer(1))
    excited = correction(q.dot(q)-3*s.sqrt(3)/2)
    delta = s.simplify(sum(excited[k]-ground[k] for k in ('kinetic','potential','haar')))
    announced = -3*s.sqrt(15)/160-s.Rational(15,64)
    adjoint = correction(q[0])
    # In product logarithms the first electric operator correction is
    # -(1/sqrt(2)) [Q,grad_Q].grad_Z. Its image of q0*phi0 has
    # unchanged coarse degree and one fiber quantum, hence denominator
    # sqrt(5) at this fixed coarse energy. This differs from the balanced
    # coordinate coefficient and is an independent self-energy check.
    angular = q.cross(s.Matrix([1, 0, 0]))
    h1_polynomial = angular.dot(z)/s.sqrt(10)
    self_energy = s.simplify(average(h1_polynomial**2)/adjoint['norm']/s.sqrt(5))
    assert self_energy == s.Rational(1, 10)
    adjoint_gap = s.simplify(sum(adjoint[k]-ground[k] for k in ('kinetic','potential','haar'))-self_energy)
    mixed_gap = 2*adjoint_gap
    splitting = s.simplify(mixed_gap-delta)
    assert s.simplify(delta-announced) == 0
    assert s.simplify(adjoint_gap-(s.Rational(63,320)-3*s.sqrt(15)/320)) == 0
    assert splitting == s.Rational(201,320)
    report = {"ground": {k:str(v) for k,v in ground.items()},
              "excited": {k:str(v) for k,v in excited.items()},
              "gap_correction":str(delta), "balanced_BO_candidate":str(announced),
              "difference":str(s.simplify(delta-announced)),
              "adjoint": {k:str(v) for k,v in adjoint.items()},
              "product_log_self_energy_magnitude": str(self_energy),
              "adjoint_gap_correction":str(adjoint_gap),
              "two_strip_mixed_gap_correction":str(mixed_gap),
              "mixed_minus_local_splitting":str(splitting),
              "scope":"Exact original-link SU2 first Rayleigh coefficients only"}
    print(json.dumps(report, indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
