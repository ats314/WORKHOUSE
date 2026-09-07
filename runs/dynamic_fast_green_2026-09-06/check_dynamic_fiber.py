"""Exact finite controls for dynamic-fiber algebra, Wick factors and denominators.

These controls do not certify the analytic Fourier/volume bounds.
Run with the repository Python and --output to write a fresh JSON report.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def clean(matrix):
    return matrix.applyfunc(s.cancel)


def zero(matrix, message):
    require(clean(matrix) == s.zeros(*matrix.shape), message)


def encode(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def dynamic_functional_calculus_control():
    # A rational isometry with a moving-space-shaped off-diagonal projection.
    orthogonal = s.Matrix([[3, 0, 4], [0, 5, 0], [-4, 0, 3]]) / 5
    j = orthogonal[:, :2]
    qf = j * j.T
    lam = s.diag(2, 5)
    cfast = j * lam.inv() * j.T
    precision = j * lam * j.T
    t = s.symbols("t", nonnegative=True)
    sigma = j * s.diag(s.exp(-2*t)/4, s.exp(-5*t)/10) * j.T
    zero(orthogonal.T * orthogonal-s.eye(3), "rational orthogonal coordinates")
    zero(cfast * precision-qf, "inverse on positive spectral island")
    zero(sigma.subs(t, 0)-cfast/2, "probability covariance factor one half")
    zero(sigma.diff(t).subs(t, 0)+qf/2, "first dynamic derivative is minus Q_F/2")
    zero(sigma.diff(t, 2).subs(t, 0)-precision/2, "second dynamic derivative")
    zero(sigma.diff(t)+precision*sigma, "complete conditional OU evolution")
    integrated = sigma.applyfunc(lambda x: s.integrate(x, (t, 0, s.oo)))
    zero(integrated-cfast*cfast/2, "integrated covariance is half squared fiber inverse")
    require(cfast != qf, "frequency denominator is nontrivial")
    return {
        "fast_projection": encode(qf),
        "twice_equal_time_covariance": encode(cfast),
        "integrated_probability_covariance": encode(integrated),
        "frequencies": [2, 5],
        "zero_island_retained": True,
        "first_and_second_time_derivatives_exact": True,
    }


def compressed_full_inverse_control():
    omega = s.Matrix([[2, 1], [1, 3]])
    covariance = omega.inv()/2
    r = s.Matrix([s.Rational(1, 3), 1])
    retained = s.Matrix([1, 0])
    require((retained.T*covariance*r)[0] == 0, "conditional residual orthogonal to y")
    variance = (r.T*covariance*r)[0]
    full_frequency = s.cancel((r.T*r)[0]/(2*variance))
    fiber_frequency = s.Integer(3)
    require(variance == s.Rational(1, 6), "conditional residual variance")
    require(full_frequency == s.Rational(10, 3), "actual first-chaos compressed frequency")
    zero(omega*r-full_frequency*r-s.Rational(5, 9)*retained,
         "nonzero baseline full retained-fast cross term")
    full_energy = variance/full_frequency
    fiber_energy = variance/fiber_frequency
    require(full_energy == s.Rational(1, 20), "actual full inverse energy")
    require(fiber_energy == s.Rational(1, 18), "fiber inverse energy")
    require(full_energy < fiber_energy, "strict inverse form domination")
    return {
        "precision": encode(omega), "observation": "x1",
        "conditional_residual": "x2+x1/3", "variance": str(variance),
        "fiber_frequency": str(fiber_frequency), "full_compressed_frequency": str(full_frequency),
        "fiber_inverse_energy": str(fiber_energy), "full_inverse_energy": str(full_energy),
        "false_inverse_identity_rejected": True,
    }


def lie_cubic_two_time_control():
    # SU(2), f_abc = epsilon_abc, hence C_A=2 and d=3.
    # Dense spatial covariance in a rational eigenbasis, with four unequal
    # frequencies, tests all cross-site contractions and unequal denominators.
    hadamard = s.Matrix([[1, 1, 1, 1], [1, -1, 1, -1],
                         [1, 1, -1, -1], [1, -1, -1, 1]])/2
    frequencies = (s.Integer(1), s.Integer(2), s.Integer(3), s.Integer(5))
    q = s.symbols("q1:5")
    sigma0 = hadamard*s.diag(*[1/(2*x) for x in frequencies])*hadamard.T
    sigmat = hadamard*s.diag(*[y/(2*x) for x, y in zip(frequencies, q)])*hadamard.T
    mean = s.Matrix([[1, 2, 0], [-1, 1, 3], [2, -2, 1], [0, 1, -1]])/7
    z = s.symbols("z0:12")
    zz = s.Matrix(4, 3, z)

    def cubic(support, weight):
        mat = mean+zz
        return s.Poly(s.expand(6*weight*(mat[list(support), :].det()
                                           -mean[list(support), :].det())), *z)

    pd = cubic((0, 1, 2), s.Integer(1))
    pe = cubic((1, 2, 3), s.Rational(2, 5))

    @lru_cache(maxsize=None)
    def moment(indices):
        if not indices:
            return s.Integer(1)
        if len(indices) % 2:
            return s.Integer(0)
        first, rest = indices[0], indices[1:]
        tm, site, color = first
        result = s.Integer(0)
        for position, other in enumerate(rest):
            tn, sj, cj = other
            if color != cj:
                continue
            covariance = sigma0[site, sj] if tm == tn else sigmat[site, sj]
            remaining = rest[:position]+rest[position+1:]
            result += covariance*moment(remaining)
        return s.expand(result)

    def variables(power, time):
        return tuple((time, i//3, i % 3) for i, count in enumerate(power)
                     for _ in range(count))

    direct = {(a, b): s.Integer(0) for a in (1, 2, 3) for b in (1, 2, 3)}
    for power, coefficient in pd.terms():
        require(moment(variables(power, 0)) == 0, "each Lie monomial internal contraction vanishes")
        for other_power, other_coefficient in pe.terms():
            degree = (sum(power), sum(other_power))
            direct[degree] += coefficient*other_coefficient*moment(
                tuple(sorted(variables(power, 0)+variables(other_power, 1))))
    direct = {key: s.Poly(s.expand(value), *q) for key, value in direct.items()}
    for (a, b), value in direct.items():
        if a != b:
            require(value.is_zero, "different Wick degrees orthogonal at two times")

    def tensor(support, weight):
        return [(indices, weight*s.LeviCivita(*[support.index(i) for i in indices]))
                for indices in itertools.permutations(support)]

    dterms = tensor((0, 1, 2), s.Integer(1))
    eterms = tensor((1, 2, 3), s.Rational(2, 5))
    formula = {1: s.Integer(0), 2: s.Integer(0), 3: s.Integer(0)}
    for (i, j, k), dcoef in dterms:
        for (ell, r, ss), ecoef in eterms:
            factor = dcoef*ecoef
            bracket = mean.row(i).cross(mean.row(j)).dot(mean.row(ell).cross(mean.row(r)))
            formula[1] += 9*factor*sigmat[k, ss]*bracket
            formula[2] += 36*factor*sigmat[j, r]*sigmat[k, ss]*mean.row(i).dot(mean.row(ell))
            formula[3] += 36*factor*sigmat[i, ell]*sigmat[j, r]*sigmat[k, ss]
    formula = {key: s.Poly(s.expand(value), *q) for key, value in formula.items()}

    def integrate_exponential(poly):
        result = s.Integer(0)
        denominators = set()
        for powers, coefficient in poly.terms():
            if coefficient == 0:
                continue
            frequency_sum = sum(n*w for n, w in zip(powers, frequencies))
            require(frequency_sum > 0, "connected term has positive frequency sum")
            denominators.add(int(frequency_sum))
            result += coefficient/frequency_sum
        return s.cancel(result), sorted(denominators)

    records = []
    for degree in (1, 2, 3):
        require(formula[degree] == direct[degree, degree], "independent two-time Wick formula")
        require(formula[degree].total_degree() == degree, "correct number of cross propagators")
        energy, denominators = integrate_exponential(direct[degree, degree])
        expected_energy, _ = integrate_exponential(formula[degree])
        require(energy == expected_energy, "exact frequency-denominator energy")
        equal_time = formula[degree].eval(dict.fromkeys(q, 1))
        records.append({
            "degree": degree,
            "cross_covariance_polynomial": str(formula[degree].as_expr()),
            "equal_time_cross_moment": str(equal_time),
            "integrated_cross_energy": str(energy),
            "frequency_sums": denominators,
        })
    require(len({str(integrate_exponential(formula[k])[0]) for k in (1, 2, 3)}) == 3,
            "all tested Wick energies nondegenerate")
    require(all(integrate_exponential(formula[k])[0] != formula[k].eval(dict.fromkeys(q, 1))
                for k in (1, 2, 3)), "equal-time substitution rejected")
    return {
        "Lie_algebra": "SU(2), f=epsilon, C_A=2, d=3",
        "frequencies": [int(x) for x in frequencies],
        "spatial_equal_time_covariance": encode(sigma0),
        "retained_mean": encode(mean),
        "first_vertex": "D_ijk=epsilon_ijk on sites (0,1,2)",
        "second_vertex": "E_ijk=(2/5)epsilon_ijk on sites (1,2,3)",
        "degree_records": records,
        "off_degree_two_time_moments_zero": True,
        "full_joint_gaussian_pairing_matches_connected_formula": True,
        "scope": "Exact finite SU(2) algebra with dense covariance; no Fourier-bound certification.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    source = Path(__file__).resolve()
    proof = source.with_name("DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY.md")
    paths = (source, proof)
    hashes = {x.name: hashlib.sha256(x.read_bytes()).hexdigest() for x in paths}
    controls = {
        "dynamic_spectral_island": dynamic_functional_calculus_control(),
        "full_complement_not_fiber_inverse": compressed_full_inverse_control(),
        "two_time_connected_Lie_cubic": lie_cubic_two_time_control(),
    }
    require(hashes == {x.name: hashlib.sha256(x.read_bytes()).hexdigest() for x in paths},
            "proof or control source changed during execution")
    payload = {"passed": True, "source_sha256": hashes, "controls": controls}
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(payload, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print("PASS: dynamic spectral identity, strict full/fiber inverse boundary, all two-time Wick degrees and denominators")


if __name__ == "__main__":
    main()
