"""Exact finite controls for the actual-complement proof mechanism.

A rational four-state family checks full-vacuum subtraction, complete low
projection leakage, and the small projected-trial energy cost. An invariant
harmonic polynomial checks the mixed-shell energy. These are controls of
the proof's finite algebra, not a finite replacement for the actual Wilson
projection-convergence or infinite-dimensional compression theorem.
"""

import json
from pathlib import Path

import sympy as s


def controls():
    if not __debug__:
        raise RuntimeError("Exact controls require assertions enabled")
    rows = []
    for g in (s.Rational(1, 2), s.Rational(1, 4), s.Rational(1, 8)):
        t = g**2
        c, r = (1-t**2)/(1+t**2), 2*t/(1+t**2)
        retained = s.Matrix([[c, 0], [0, c], [r, 0], [0, r]])
        complement = s.Matrix([[-r, 0], [0, -r], [c, 0], [0, c]])
        assert retained.T * retained == complement.T * complement == s.eye(2)
        assert retained.T * complement == s.zeros(2)
        p, q = retained * retained.T, complement * complement.T
        low = s.diag(1, 1, 0, 0)
        h = s.diag(11, 15, 18, 23)/g**2
        vacuum = s.eye(4)[:, 0]
        mixed = s.eye(4)[:, 2]
        assert (q*vacuum).dot(q*vacuum) == r**2 > 0
        assert low*q*low == r**2*low
        floor = 7*c**2/g**2
        fast = complement.T*(h-11*s.eye(4)/g**2)*complement
        assert fast[0, 0] == floor
        assert fast[1, 1] >= floor and fast[0, 1] == fast[1, 0] == 0
        assert floor == (18-11)*(1-r**2)/g**2
        projected = p*mixed
        projected_norm2 = projected.dot(projected)
        projected_energy = (projected.T*h*projected)[0]
        assert projected_norm2 == r**2
        assert projected_energy == r**2*(11*c**2+18*r**2)/g**2
        assert projected_norm2 <= 4*g**4
        assert projected_energy <= 72*g**2
        constrained = q*mixed
        rayleigh = (constrained.T*(h-11*s.eye(4)/g**2)*constrained)[0]/constrained.dot(constrained)
        assert rayleigh == floor
        rows.append({"g": str(g), "vacuum_Q_norm_squared": str(r**2),
                     "actual_compressed_floor": str(floor),
                     "complete_low_leakage_bound_attained": True,
                     "projected_trial_norm_squared": str(projected_norm2),
                     "projected_trial_energy": str(projected_energy),
                     "projection_energy_over_g_squared": str(projected_energy/g**2)})
    g = s.Symbol("g", positive=True)
    c, r = (1-g**4)/(1+g**4), 2*g**2/(1+g**4)
    assert s.limit(r**2*(11*c**2+18*r**2)/g**4, g, 0) == 44
    assert s.limit(7*c**2, g, 0) == 7

    # After conjugating by the normalized product Gaussian, the oscillator
    # above its vacuum acts as -k/2 Delta+sqrt(k) x.grad in each factor.
    qv = s.symbols("q0:3")
    zv = s.symbols("z0:3")
    mixed = sum(a*b for a, b in zip(qv, zv, strict=True))

    def excitation(poly):
        return s.expand(sum(-s.Rational(3, 2)*s.diff(poly, a, 2)
                            +s.sqrt(3)*a*s.diff(poly, a) for a in qv)
                        +sum(-s.Rational(5, 2)*s.diff(poly, b, 2)
                             +s.sqrt(5)*b*s.diff(poly, b) for b in zv))

    assert s.expand(excitation(mixed)-(s.sqrt(3)+s.sqrt(5))*mixed) == 0
    for axis in range(3):
        e = s.eye(3)[:, axis]
        dq, dz = e.cross(s.Matrix(qv)), e.cross(s.Matrix(zv))
        derivative = sum(dq[i]*s.diff(mixed, qv[i])+dz[i]*s.diff(mixed, zv[i])
                         for i in range(3))
        assert s.expand(derivative) == 0
    assert mixed.subs(dict(zip(zv, [-x for x in zv], strict=True)), simultaneous=True) == -mixed
    assert s.sqrt(3)+s.sqrt(5) > 2*s.sqrt(3)
    assert s.sqrt(3)+s.sqrt(5) < 2*s.sqrt(5)
    return {"passed": True, "scope": __doc__, "rational_cases": rows,
            "normalized_projection_energy_limit": "44",
            "scaled_compressed_floor_limit": "7",
            "physical_mixed_harmonic_excitation": "sqrt(3)+sqrt(5)",
            "mixed_polynomial_Gauss_invariant": True,
            "mixed_fiber_inversion_odd": True,
            "no_inference_that_P_contains_true_vacuum": True}


if __name__ == "__main__":
    result = controls()
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2))
