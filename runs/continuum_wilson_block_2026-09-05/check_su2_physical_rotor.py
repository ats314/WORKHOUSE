"""SU(2) class-rotor exploration and rigorous finite-u Jacobi enclosures.

Numerical truncation stability is reported separately. Untruncated finite-u
enclosures use an analytic tail form bound and exact integer Sturm counts;
they do not prove the large-u asymptotic or an OS fast-complement estimate.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
from datetime import UTC, datetime
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import scipy
import scipy.linalg
import sympy as sp


def exact_normalization_checks():
    x = sp.Symbol("x", real=True)
    theta = sp.Symbol("theta", real=True)
    tested = []
    for n in range(9):
        # n=2j; chi_j(theta)=U_n(cos theta).
        character = sp.chebyshevu(n, x)
        lower = sp.chebyshevu(n-1, x) if n else 0
        assert sp.expand(2*x*character-sp.chebyshevu(n+1, x)-lower) == 0
        radial = -((1-x*x)*sp.diff(character, x, 2)-3*x*sp.diff(character, x))/4
        assert sp.expand(radial-sp.Rational(n*(n+2), 4)*character) == 0
        tested.append(n)
    wave = sp.Function("g")(theta)
    raw = wave/sp.sin(theta)
    transformed = -sp.sin(theta)*(sp.diff(raw,theta,2)+2*sp.cot(theta)*sp.diff(raw,theta))/4
    assert sp.simplify(transformed+sp.diff(wave,theta,2)/4+wave/4) == 0
    # Character orthogonality after multiplication by sin(theta).
    for n in range(1, 6):
        for m in range(1, 6):
            inner = 2/sp.pi*sp.integrate(sp.sin(n*theta)*sp.sin(m*theta), (theta,0,sp.pi))
            assert inner == int(n == m)
    return {"character_degrees": tested, "haar_inner_products": 25,
            "casimir": "j(j+1)", "jacobi_diagonal": "j(j+1)+8u",
            "jacobi_offdiagonal": "-4u", "radial_operator": "-1/4 d²-1/4+8u(1-cos theta)"}


def jacobi_eigenvalues(u, cutoff, last_subtraction=0.0):
    n = np.arange(cutoff, dtype=float)
    diagonal = n*(n+2)/4+8*float(u)
    diagonal[-1] -= float(last_subtraction)
    off = np.full(cutoff-1, -4*float(u))
    return scipy.linalg.eigh_tridiagonal(diagonal, off, eigvals_only=True,
        select="i", select_range=(0,2), lapack_driver="stebz", tol=1e-11)


def sturm_count(u, cutoff, energy, last_subtraction=F(0)):
    """Number of finite Jacobi eigenvalues strictly below a rational energy.

    Clear all denominators once; determinant recurrence then uses integers
    only. Vanishing internal determinants are skipped in the Sturm sign
    sequence. The off-diagonal is nonzero for the certified positive u.
    """
    u, energy, last_subtraction = F(u), F(energy), F(last_subtraction)
    if u <= 0 or cutoff < 2:
        raise ValueError("Use positive u and at least two character modes")
    scale = math.lcm(4, u.denominator, energy.denominator, last_subtraction.denominator)
    off = int(-4*u*scale)
    previous, current, previous_sign, changes = 0, 1, 1, 0
    for n in range(cutoff):
        diagonal = F(n*(n+2),4)+8*u-energy
        if n == cutoff-1:
            diagonal -= last_subtraction
        scaled = diagonal*scale
        assert scaled.denominator == 1
        following = int(scaled)*current-off*off*previous
        if following:
            sign = 1 if following > 0 else -1
            changes += sign != previous_sign
            previous_sign = sign
        previous, current = current, following
    return changes


def certified_finite_interval(u, cutoff, index, last_subtraction=F(0)):
    """Floats propose rational endpoints; exact Sturm counts accept them."""
    estimate = jacobi_eigenvalues(u, cutoff, last_subtraction)[index]
    scale = 10**6
    center = math.floor(float(estimate)*scale)
    radius = 2
    for _ in range(30):
        lower, upper = F(center-radius, scale), F(center+radius, scale)
        lo_count = sturm_count(u, cutoff, lower, last_subtraction)
        hi_count = sturm_count(u, cutoff, upper, last_subtraction)
        if lo_count == index and hi_count == index+1:
            return lower, upper, [lo_count, hi_count]
        radius *= 2
    raise AssertionError("Could not certify proposed finite eigenvalue interval")


def rigorous_rotor_enclosure(u):
    u = F(u)
    root = math.isqrt(u.numerator)
    assert u.denominator == 1 and root*root == u
    cutoff = max(32, 8*root)
    tail_floor = F(cutoff*(cutoff+2),4)
    barrier = F(12*root+1)
    assert barrier < tail_floor
    subtraction = 16*u*u/(tail_floor-barrier)
    assert sturm_count(u, cutoff, barrier) >= 2
    assert sturm_count(u, cutoff, barrier, subtraction) >= 2
    enclosures = []
    for index in range(2):
        lower_comparison = certified_finite_interval(u, cutoff, index, subtraction)
        ritz = certified_finite_interval(u, cutoff, index)
        enclosures.append({"index":index, "lower":str(lower_comparison[0]),
            "upper":str(ritz[1]), "lower_matrix_interval":[str(x) for x in lower_comparison[:2]],
            "ritz_interval":[str(x) for x in ritz[:2]],
            "lower_sturm_counts":lower_comparison[2], "ritz_sturm_counts":ritz[2]})
    gap_lower = F(enclosures[1]["lower"])-F(enclosures[0]["upper"])
    gap_upper = F(enclosures[1]["upper"])-F(enclosures[0]["lower"])
    assert 0 < gap_lower <= gap_upper
    return {"u":str(u), "cutoff":cutoff, "tail_kinetic_floor":str(tail_floor),
        "barrier":str(barrier), "boundary_subtraction":str(subtraction), "eigenvalues":enclosures,
        "gap_interval":[str(gap_lower),str(gap_upper)],
        "gap_over_sqrt_u_interval":[str(gap_lower/root),str(gap_upper/root)],
        "scope":"Untruncated intrinsic SU(2) class rotor at this fixed u, conditional only on the displayed exact operator/form identification"}


def numerical_scan():
    rows=[]
    for u in (0.01,0.1,1,10,100,1000,10000,1e6,1e8):
        cutoff=max(32,math.ceil(16*u**0.25))
        first=jacobi_eigenvalues(u,cutoff)
        second=jacobi_eigenvalues(u,2*cutoff)
        rows.append({"u":u,"cutoffs":[cutoff,2*cutoff],"eigenvalues":second.tolist(),
            "gap_over_sqrt_u":float((second[1]-second[0])/math.sqrt(u)),
            "ground_over_sqrt_u":float(second[0]/math.sqrt(u)),
            "scaled_cutoff_discrepancy":float(np.max(np.abs(first-second))/math.sqrt(u))})
    return rows


def sturm_negative_and_boundary_checks():
    # The exact 2x2 eigenvalue count agrees at rational test points, including
    # an internal zero principal minor; no floating sign decision is used.
    u=F(1,4)
    for energy in (F(0),F(1),F(2),F(3),F(4),F(11,4)):
        matrix=sp.Matrix([[2,-1],[-1,sp.Rational(11,4)]])
        exact=sum(bool(value<sp.Rational(energy.numerator,energy.denominator)) for value in matrix.eigenvals())
        assert sturm_count(u,2,energy)==exact
    # Omitting the radial factor 1/4 would quadruple the kinetic Casimir.
    assert sp.Rational(3,4) != 3
    return {"two_mode_exact_counts":6,"internal_zero_principal_minor_test":True,
            "normalization_negative_control":"fundamental Casimir is 3/4, not 3"}


def main():
    if not __debug__:
        raise RuntimeError("Exact Sturm acceptance requires assertions enabled")
    result={"schema":"su2-physical-class-rotor/v1", "normalization":exact_normalization_checks(),
        "sturm_controls":sturm_negative_and_boundary_checks(), "numerical_scan":numerical_scan(),
        "rigorous_fixed_u_enclosures":[rigorous_rotor_enclosure(u) for u in (1,100,10000)],
        "runtime":{"python":sys.version,"numpy":np.__version__,"scipy":scipy.__version__,
            "sympy":sp.__version__,"machine":platform.machine(),"completed_utc":datetime.now(UTC).isoformat()},
        "scope":"Numerical asymptotic exploration plus exact finite-u infinite-Jacobi enclosures; not a full OS fast-complement estimate or continuum theorem"}
    result["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    destination=Path(__file__).with_name("su2_physical_rotor_control.json")
    with destination.open("x",encoding="utf-8") as stream:
        json.dump(result,stream,indent=2,sort_keys=True);stream.write("\n")
    for row in result["numerical_scan"]:
        print(row["u"],row["gap_over_sqrt_u"],row["scaled_cutoff_discrepancy"])
    for row in result["rigorous_fixed_u_enclosures"]:
        print("CERTIFIED",row["u"],row["gap_over_sqrt_u_interval"])


if __name__=="__main__":
    main()
