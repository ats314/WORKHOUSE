"""Theta-uniformity of the M10 conditional tube moments across the antipodal transition.

The conditional Hessian spectrum on a regular fixed-Q four-face SU(2) fiber is the
A5/A6 table of `docs/derivations/w6-antipodal-magnetic-geometry.md`, with
C = cos(theta/4):

    8C            x3
    (8-4sqrt2)C   x1
    (8+4sqrt2)C   x1
    8C - 4sqrt2   x2   <- soft branch, vanishes exactly at theta = pi
    8C + 4sqrt2   x2

Under the eikonal relation Omega_S = sqrt(Omega_V) the Born covariance is
Sigma_Y = (1/2) Omega_S^-1, and the centered Gaussian norm moments are
c2 = s1, c4 = s1^2 + 2 s2, c6 = s1^3 + 6 s1 s2 + 8 s3 with s_k = Tr(Sigma_Y^k).

This script establishes two things.

1. Divergence rates. Writing delta = pi - theta, the soft branch is
   sqrt2 delta + O(delta^2) (A6), so every tube moment diverges at the antipodal
   transition with an exact closed-form constant:

       c2 ~ 2^(-1/4) delta^(-1/2)
       c4 ~ 2^(1/2)  delta^(-1)
       c6 ~ 6*2^(-3/4) delta^(-3/2)

   and the interior gradient prefactor 4/lambda_min^S ~ 4*2^(-1/4) delta^(-1/2).
   No theta-uniform bound of fixed-radius tube form exists.

2. A spectrum discrimination test. The constant 4(sqrt2-1) of (A5) is a LOWER
   BOUND on the seven non-soft eigenvalues. In the actual spectrum it occurs only
   at theta = pi, as the (8-4sqrt2)C singlet, with multiplicity one. Treating it
   as a seven-fold eigenvalue produces moments that belong to no fiber: the
   scale-invariant ratio c4/c2^2 then falls strictly below its minimum over
   theta in [0, pi], which is attained at theta = 0.

Scope: exact spectral algebra on the stated chart-metric table, plus the
asymptotics it implies. This is a uniformity obstruction, not a proof of M10,
and it supplies no parameter-differentiated ground-state estimate and no
conditionally normalized complement bound.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp

R2 = sp.sqrt(2)


def spectrum(theta):
    """The A5/A6 conditional Hessian spectrum as a flat list of nine eigenvalues."""
    C = sp.cos(theta / 4)
    return (
        [8 * C] * 3
        + [(8 - 4 * R2) * C]
        + [(8 + 4 * R2) * C]
        + [8 * C - 4 * R2] * 2
        + [8 * C + 4 * R2] * 2
    )


def moments(theta):
    """(c2, c4, c6) of |Y|^2 under Sigma_Y = (1/2) Omega_S^-1, Omega_S = sqrt(Omega_V)."""
    sig = [sp.Rational(1, 2) / sp.sqrt(v) for v in spectrum(theta)]
    s1 = sum(sig)
    s2 = sum(v**2 for v in sig)
    s3 = sum(v**3 for v in sig)
    return s1, s1**2 + 2 * s2, s1**3 + 6 * s1 * s2 + 8 * s3


def exact_checks():
    """Exact symbolic facts about the spectrum and its antipodal degeneration."""
    delta = sp.Symbol("delta", positive=True)
    theta = sp.Symbol("theta", positive=True)
    out = {}

    out["nine_eigenvalues"] = len(spectrum(theta)) == 9

    soft = 8 * sp.cos((sp.pi - delta) / 4) - 4 * R2
    out["A6_expansion"] = (
        sp.simplify(sp.series(soft, delta, 0, 3).removeO() - (R2 * delta - R2 / 8 * delta**2)) == 0
    )
    out["soft_vanishes_at_pi"] = sp.simplify(soft.subs(delta, 0)) == 0

    # (A5)'s constant is the (8-4sqrt2)C singlet evaluated at theta = pi, not a 7-fold value.
    singlet_at_pi = sp.simplify(((8 - 4 * R2) * sp.cos(theta / 4)).subs(theta, sp.pi))
    out["A5_constant_is_the_pi_singlet"] = sp.simplify(singlet_at_pi - 4 * (R2 - 1)) == 0
    mult_at_pi = sum(1 for v in spectrum(sp.pi) if sp.simplify(v - 4 * (R2 - 1)) == 0)
    out["A5_constant_multiplicity_at_pi_is_one"] = mult_at_pi == 1
    out["A5_constant_absent_at_theta_zero"] = all(
        sp.simplify(v - 4 * (R2 - 1)) != 0 for v in spectrum(sp.Integer(0))
    )

    # Exact leading constants of the divergence, as delta -> 0.
    c2, c4, c6 = moments(sp.pi - delta)
    lam_min_S = sp.sqrt(8 * sp.cos((sp.pi - delta) / 4) - 4 * R2)
    limits = {
        "c2 * delta^(1/2)": (c2 * sp.sqrt(delta), 2 ** sp.Rational(-1, 4)),
        "c4 * delta": (c4 * delta, sp.sqrt(2)),
        "c6 * delta^(3/2)": (c6 * delta ** sp.Rational(3, 2), 6 * 2 ** sp.Rational(-3, 4)),
        "4/lambda_min_S * delta^(1/2)": (
            4 / lam_min_S * sp.sqrt(delta),
            4 * 2 ** sp.Rational(-1, 4),
        ),
    }
    rates = {}
    for name, (expr, claimed) in limits.items():
        value = sp.limit(expr, delta, 0, dir="+")
        rates[name] = {
            "limit": sp.nsimplify(sp.simplify(value)).__str__(),
            "claimed": claimed.__str__(),
            "agrees": sp.simplify(value - claimed) == 0,
        }
    out["divergence_constants"] = rates
    return out


def discrimination_test():
    """c4/c2^2 is scale-invariant, so it rules out theta independently of normalization."""
    grid = [i * math.pi / 400 for i in range(401)]

    def ratio(th):
        C = math.cos(th / 4)
        ev = (
            [8 * C] * 3
            + [(8 - 4 * math.sqrt(2)) * C, (8 + 4 * math.sqrt(2)) * C]
            + [8 * C - 4 * math.sqrt(2)] * 2
            + [8 * C + 4 * math.sqrt(2)] * 2
        )
        sig = [0.5 / math.sqrt(v) for v in ev if v > 0]
        s1 = sum(sig)
        return (s1 * s1 + 2 * sum(v * v for v in sig)) / s1**2

    values = [ratio(t) for t in grid]
    lo = min(values)
    reported = 13.912200 / 3.372386**2
    return {
        "min_c4_over_c2_squared": lo,
        "argmin_theta": grid[values.index(lo)],
        "submitted_c4_over_c2_squared": reported,
        "submitted_below_minimum": reported < lo,
        "note": "Scale-invariant, so this excludes every theta and every overall "
        "normalization of the chart metric.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    exact = exact_checks()
    discrimination = discrimination_test()

    flat = [v for k, v in exact.items() if isinstance(v, bool)]
    flat += [r["agrees"] for r in exact["divergence_constants"].values()]
    flat.append(discrimination["submitted_below_minimum"])
    passed = all(flat)

    payload = {
        "schema": "m10-antipodal-moment-scaling/v1",
        "passed": passed,
        "exact_checks": {k: v for k, v in exact.items() if isinstance(v, bool)},
        "divergence_constants": exact["divergence_constants"],
        "spectrum_discrimination": discrimination,
        "scope": "Exact spectral algebra on the A5/A6 chart-metric table and the "
        "antipodal asymptotics it implies. Establishes that no fixed-radius tube "
        "moment bound is uniform in theta, and that the (A5) lower bound is not a "
        "seven-fold eigenvalue. Supplies no parameter-differentiated ground-state "
        "estimate, no conditionally normalized complement bound, and no M10 closure.",
    }
    text = json.dumps(payload, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
    print(text, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
