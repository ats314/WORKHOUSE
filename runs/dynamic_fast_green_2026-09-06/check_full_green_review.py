"""Independent exact physical-polynomial review of the full fast Green formula.

Unlike the reviewed script's exterior-space calculation, this constructs
all 64 monomials x_i^0 x_j^1 x_k^2 for four sites and three SU(2) colors,
then compresses the Gaussian generator against all 27 retained monomials.
No function or output from the reviewed script is imported.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s


def require(condition, message):
    if not condition:
        raise ValueError(message)


def encode(a):
    return [[str(a[i, j]) for j in range(a.cols)] for i in range(a.rows)]


def permutation_sign(indices):
    return s.Integer((-1)**sum(indices[i] > indices[j]
                              for i in range(len(indices))
                              for j in range(i+1, len(indices))))


def derive():
    omega = s.diag(1, 4, 9, 16)
    b = s.diag(1, 2, 3, 4)
    ell1 = b.inv()
    covariance = omega.inv()/2
    w = s.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]])
    source_gram = w.T*omega.inv()*w
    source_isometry = ell1*w*s.diag(4/s.sqrt(17), 2, 3)
    require(source_isometry.T*source_isometry == s.eye(3), "correct marginal-normalized source")
    require(w.T*covariance*w == source_gram/2, "marginal probability covariance factor")

    # Coordinate coefficients carry the Gaussian, rather than Euclidean, norm.
    p_coordinate = w*(w.T*covariance*w).inv()*w.T*covariance
    p_fock = source_isometry*source_isometry.T
    require(ell1*p_coordinate*b == p_fock, "coordinate/Fock projection conjugacy")
    wrong_fock = w*(w.T*w).inv()*w.T
    require(wrong_fock != p_fock, "unweighted Fock source rejected")
    require(p_fock*omega != omega*p_fock, "independent source is nonreducing")

    sites = list(itertools.product(range(4), repeat=3))
    position = {indices: i for i, indices in enumerate(sites)}
    wedge_basis = list(itertools.combinations(range(4), 3))
    coefficients = s.Matrix([1, -2, 3, -4])
    dvalue = {}
    for triple, coefficient in zip(wedge_basis, coefficients):
        for perm in itertools.permutations(triple):
            dvalue[perm] = coefficient*permutation_sign(perm)

    # Expand the literal ordered D_ijk epsilon_abc polynomial without inserting
    # its known determinant factor. Commutativity of fields is built into the
    # one-monomial-per-color representation, which is bosonic.
    polynomial = s.zeros(64, 1)
    for (i, j, k), dijk in dvalue.items():
        for colors in itertools.permutations(range(3)):
            monomial = [0, 0, 0]
            for site, color in zip((i, j, k), colors):
                monomial[color] = site
            polynomial[position[tuple(monomial)]] += dijk*permutation_sign(colors)
    require(all(polynomial[position[indices]] == 6*dvalue.get(indices, 0)
                for indices in sites), "ordered Lie cubic has factor six in color monomials")

    gram = s.kronecker_product(covariance, covariance, covariance)
    generator = s.diag(*[sum(omega[i, i] for i in indices) for indices in sites])
    source = s.kronecker_product(w, w, w)
    constraint = source.T*gram
    null_columns = constraint.nullspace()
    null = s.Matrix.hstack(*null_columns)
    require(null.shape == (64, 37), "all 27 retained and all 37 complementary monomials")
    require(constraint*null == s.zeros(27, 37), "exact conditional-centering constraint")

    # This direct variational compression is in the full 64-dimensional
    # polynomial sector; no exterior shortcut is used in the solve.
    restricted_form = null.T*gram*generator*null
    forcing = null.T*gram*polynomial
    solution = null*restricted_form.inv()*forcing
    energy = (polynomial.T*gram*solution)[0]
    require(constraint*solution == s.zeros(27, 1), "full solution remains conditionally centered")
    require(null.T*gram*(generator*solution-polynomial) == s.zeros(37, 1),
            "full compressed Euler-Lagrange equation")

    # Independently test the proposed energy-prior formula in wedge coordinates.
    prior = s.diag(*[1/(s.prod(omega[i, i] for i in triple)
                         *sum(omega[i, i] for i in triple)) for triple in wedge_basis])
    u3 = s.Matrix([w.extract(triple, range(3)).det() for triple in wedge_basis])
    proposed = prior-prior*u3*(u3.T*prior*u3).inv()*u3.T*prior
    spatial_wedge_energy = (coefficients.T*proposed*coefficients)[0]
    ordered_spatial_energy = 6*spatial_wedge_energy
    # 3! C_A d / 8 = 6*2*3/8 = 9/2; ordered-to-wedge contributes six.
    require(energy == s.Rational(9, 2)*ordered_spatial_energy,
            "3! C_A d/8 factor verified in full bosonic polynomial representation")
    require(energy == 27*spatial_wedge_energy, "equivalent SU2 wedge factor twenty-seven")

    # The solution lies in the alternating spatial Lie-color sector despite
    # solving in the larger colored polynomial space.
    for indices in sites:
        if len(set(indices)) < 3:
            require(solution[position[indices]] == 0, "solution has no repeated spatial legs")
        else:
            sorted_indices = tuple(sorted(indices))
            require(solution[position[indices]]
                    == permutation_sign(indices)*solution[position[sorted_indices]],
                    "full solution preserves the spatial exterior Lie-color sector")

    wrong_prior = s.diag(*[1/s.prod(omega[i, i] for i in triple)
                          for triple in wedge_basis])
    wrong_green = wrong_prior-wrong_prior*u3*(u3.T*wrong_prior*u3).inv()*u3.T*wrong_prior
    wrong_energy = 27*(coefficients.T*wrong_green*coefficients)[0]
    require(wrong_energy != energy, "equal-time conditioning does not compute energy")
    return {
        "passed": True,
        "scope": "Exact nonreducing four-site SU2 Gaussian polynomial computation; no locality estimate.",
        "frequency": encode(omega), "observation_cotangents": encode(w),
        "source_Gram_without_probability_half": encode(source_gram),
        "unweighted_Fock_source_rejected": True,
        "polynomial_dimension": 64, "retained_dimension": 27, "complement_dimension": 37,
        "full_compressed_polynomial_energy": str(energy),
        "ordered_spatial_energy": str(ordered_spatial_energy),
        "orthonormal_wedge_energy": str(spatial_wedge_energy),
        "ordered_tensor_prefactor": "9/2 = 3! C_A d/8 for SU2",
        "equivalent_wedge_prefactor": 27,
        "equal_time_wrong_energy": str(wrong_energy),
        "combined_color_bosonic_and_exterior_results_agree": True,
        "full_solution_preserves_Lie_color_sector": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = derive()
    source = Path(__file__).resolve()
    result["review_script_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    if args.verify:
        require(result == json.loads(args.verify.read_text(encoding="utf-8")), "full review payload replay")
    else:
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(result, stream, sort_keys=True, indent=2)
            stream.write("\n")
    print("PASS: full colored bosonic polynomial compression, source normalization, and ordered Lie-cubic factor")


if __name__ == "__main__":
    main()
