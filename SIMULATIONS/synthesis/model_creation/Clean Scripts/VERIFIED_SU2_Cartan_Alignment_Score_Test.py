"""
VERIFIED_SU2_Cartan_Alignment_Score_Test.py

==============================================================================
WHAT THIS SCRIPT DOES:
==============================================================================
Implements a "Cartan Alignment Score" metric for SU(2) link configurations.
It detects whether SU(2) links U_mu(x) are collectively aligned along a single 
Abelian subgroup (U(1) subset of SU(2)).

The score is defined via the spectrum of the covariance matrix of the 
Lie algebra components.
    Score = 1.0 - lambda_max(Covariance)
    
    Score ~ 0.0  => Links are highly collinear (Abelian/Cartan-like)
    Score ~ 0.66 => Links are isotropically distributed (Full SU(2))

SEARCH KEYWORDS:
    SU(2), Cartan subalgebra, Abelian projection, alignment score,
    covariance matrix, symmetry breaking, lattice gauge theory

THEORY CONNECTION:
    In the mass gap proof, we must distinguish between "rough" non-Abelian 
    configurations (which have a mass gap) and "smooth" Abelian-like ones
    (which might drift). This score provides a quantitative order parameter
    for this distinction.

VERIFICATION STATUS: VERIFIED (2026-01-01)
    - Random SU(2) (Haar) -> Score ~ 0.66 (expected isotropic)
    - Exp(Gaussian) (Small field) -> Score ~ 0.66 (isotropic near identity)
    - Forced Cartan (exp(i*theta*sigma_z)) -> Score ~ 0.0 (perfectly aligned)

DEPENDENCIES: numpy only
==============================================================================
"""

import numpy as np
import math

# Pauli matrices
sigma = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex)
]
I2 = np.eye(2, dtype=complex)

def su2_random_matrix(rng):
    # Random SU(2) via unit quaternion
    v = rng.normal(size=4)
    v /= np.linalg.norm(v)
    a, b, c, d = v
    # Map quaternion to matrix:
    # U = a*I + i(b*sx + c*sy + d*sz)
    return np.array([
        [a + 1j*d, b + 1j*c],
        [-b + 1j*c, a - 1j*d]
    ], dtype=complex)

def get_su2_algebra_components(U):
    """
    Extract Lie algebra components (v_1, v_2, v_3) from U.
    U = cos(theta) I + i sin(theta) (n . sigma)
    We want the vector sin(theta)*n, which is the imaginary part.
    
    Actually simpler: U = a*I + i(v . sigma). 
    We extract v = (b, c, d) from the quaternion representation.
    """
    # Numerical projection to SU(2) just in case
    # quaternion: a = Re(U[0,0]), d = Im(U[0,0]), b = Re(U[0,1]), c = Im(U[0,1])
    # Note: definition of b,c signs depends on convention.
    # Using standard: U = [[a+id, b+ic], [-b+ic, a-id]]
    
    a = U[0,0].real
    d = U[0,0].imag
    b = U[0,1].real
    c = U[0,1].imag
    
    # Check unitarity roughly
    norm = math.sqrt(a*a + b*b + c*c + d*d)
    
    return np.array([b, c, d]) / norm

def compute_cartan_alignment_score(U_list):
    """
    Compute alignment score for a list of SU(2) matrices.
    1. Extract imaginary 3-vectors v_i for each U_i.
    2. Form covariance matrix C = sum(v_i * v_i^T) / sum(|v_i|^2).
    3. Score = 1 - max_eigenvalue(C).
    """
    vectors = [get_su2_algebra_components(U) for U in U_list]
    vectors = np.array(vectors)
    
    # Outer product sum
    # C_unnorm = vectors^T @ vectors (3x3)
    C_unnorm = vectors.T @ vectors
    
    # Normalization
    norm_sq_sum = np.sum(vectors**2)
    if norm_sq_sum < 1e-12:
        return 0.0 # Trivial identity case
    
    C = C_unnorm / norm_sq_sum
    
    eigvals = np.linalg.eigvalsh(C)
    lam_max = np.max(eigvals)
    
    return 1.0 - lam_max

if __name__ == "__main__":
    print("=" * 70)
    print("SU(2) Cartan Alignment Score Verification")
    print("=" * 70)
    
    rng = np.random.default_rng(42)
    N_samples = 1000
    
    # Case 1: Random Haar (Isotropic)
    # -------------------------------
    print("Test 1: Random Haar (Should be Isotropic)")
    U_haar = [su2_random_matrix(rng) for _ in range(N_samples)]
    score_haar = compute_cartan_alignment_score(U_haar)
    print(f"  Score: {score_haar:.4f}")
    print(f"  Target: ~0.666 (eigenvalues 1/3, 1/3, 1/3 -> max=0.33 -> score=0.67)")
    
    # Case 2: Forced Cartan (Perfectly Aligned)
    # -----------------------------------------
    print("\nTest 2: Forced Cartan Aligned (U = exp(i theta sigma_z))")
    U_cartan = []
    for _ in range(N_samples):
        theta = rng.uniform(0, 2*np.pi)
        # exp(i theta sigma_z) = diag(e^itheta, e^-itheta)
        # quaternion: cos(th), 0, 0, sin(th) -> vector (0,0,sin(th))
        # This is perfectly aligned along z-axis.
        U_c = np.array([[np.exp(1j*theta), 0], [0, np.exp(-1j*theta)]])
        U_cartan.append(U_c)
    
    score_cartan = compute_cartan_alignment_score(U_cartan)
    print(f"  Score: {score_cartan:.4f}")
    print(f"  Target: ~0.000 (eigenvalues 0, 0, 1 -> max=1.0 -> score=0.0)")

    # Case 3: Small perturbations around Identity (Gaussian)
    # ------------------------------------------------------
    print("\nTest 3: Small Gaussian fluctuations around Identity")
    U_gauss = []
    for _ in range(N_samples):
        v = rng.normal(size=3) * 0.1 # small sigma
        # exp(i v.sigma) approx 1 + i v.sigma
        # vector is v. Direction of v is isotropic.
        # So distribution of vectors should be isotropic.
        norm = np.linalg.norm(v)
        n = v/norm if norm > 0 else np.array([0,0,1])
        a = math.cos(norm)
        b, c, d = math.sin(norm) * n
        U_g = np.array([
            [a + 1j*d, b + 1j*c],
            [-b + 1j*c, a - 1j*d]
        ], dtype=complex)
        U_gauss.append(U_g)
        
    score_gauss = compute_cartan_alignment_score(U_gauss)
    print(f"  Score: {score_gauss:.4f}")
    print(f"  Target: ~0.666 (Isotropic fluctuations)")

    print("-"*50)
    
    # Verification Logic
    success = True
    if abs(score_haar - 0.66) > 0.05: success = False
    if abs(score_cartan) > 0.01: success = False
    if abs(score_gauss - 0.66) > 0.05: success = False
    
    if success:
        print("[PASS] Score correctly detects isotropic vs aligned distributions.")
    else:
        print("[FAIL] Score behavior did not match expectations.")
