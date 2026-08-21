"""
Numerical experiment for testing positive definiteness of the Hessian
of the Haar action S_Haar(x) on balls in su(2).
"""

import jax
import jax.numpy as jnp
from jax import grad, jacfwd
import numpy as np


def build_su2_basis():
    """
    Build the su(2) basis {T^a}_{a=1}^3 where T^a = i * sigma^a.
    Each T^a is a 2x2 skew-Hermitian traceless matrix.
    
    Returns:
        A list of three 2x2 complex arrays.
    """
    # Pauli matrices
    sigma_1 = jnp.array([[0, 1], [1, 0]], dtype=jnp.complex128)
    sigma_2 = jnp.array([[0, -1j], [1j, 0]], dtype=jnp.complex128)
    sigma_3 = jnp.array([[1, 0], [0, -1]], dtype=jnp.complex128)
    
    # T^a = i * sigma^a
    T1 = 1j * sigma_1
    T2 = 1j * sigma_2
    T3 = 1j * sigma_3
    
    return [T1, T2, T3]


def A_from_coords(x):
    """
    Map coordinates x ∈ R^3 to A(x) ∈ su(2).
    
    A(x) = sum_{a=1}^3 x_a T^a
    
    Args:
        x: array of shape (3,), real coordinates.
    
    Returns:
        A 2x2 complex array in su(2).
    """
    basis = build_su2_basis()
    A = x[0] * basis[0] + x[1] * basis[1] + x[2] * basis[2]
    return A


def adjoint_matrix(A):
    """
    Compute the 3x3 matrix representation of ad_A in the basis {T^a}.
    
    ad_A(X) = [A, X] = A X - X A
    
    For X = sum_a c_a T^a, we have ad_A(X) = sum_b (ad_A)_{ba} T^b.
    
    Args:
        A: 2x2 complex array in su(2).
    
    Returns:
        3x3 real array representing ad_A.
    """
    basis = build_su2_basis()
    ad_matrix = jnp.zeros((3, 3), dtype=jnp.float64)
    
    for a in range(3):
        # Compute [A, T^a]
        commutator = A @ basis[a] - basis[a] @ A
        
        # Express commutator in the basis
        for b in range(3):
            # Coefficient: trace([A, T^a] @ T^{b dagger}) / trace(T^b @ T^{b dagger})
            # For our basis, T^{b dagger} = -T^b and trace(T^b @ T^{b dagger}) = 2
            coeff = jnp.trace(commutator @ (-basis[b])) / 2.0
            ad_matrix = ad_matrix.at[b, a].set(jnp.real(coeff))
    
    return ad_matrix


def log_sinh_over_x(lam, eps=1e-8):
    """
    Compute log(sinh(lam) / lam) with series expansion for small lam.
    
    For small lam: sinh(lam)/lam ≈ 1 + lam^2/6 + lam^4/120 + ...
    So log(sinh(lam)/lam) ≈ lam^2/6 + lam^4/180 - lam^6/2835 + ...
    
    Args:
        lam: eigenvalue (real).
        eps: threshold for using series expansion.
    
    Returns:
        log(sinh(lam) / lam).
    """
    lam_abs = jnp.abs(lam)
    
    # Series expansion for small |lam|
    # log(sinh(x)/x) ≈ x^2/6 + x^4/180 - x^6/2835
    series = lam**2 / 6.0 + lam**4 / 180.0 - lam**6 / 2835.0
    
    # Exact formula for large |lam|
    exact = jnp.log(jnp.sinh(lam) / lam)
    
    # Use series for small lam, exact otherwise
    return jnp.where(lam_abs < eps, series, exact)


def S_haar(x):
    """
    Compute the Haar action S_Haar(x) = -log det(sinh(X)/X)
    where X = ad_A(x).
    
    Args:
        x: array of shape (3,), coordinates in R^3.
    
    Returns:
        Scalar value of S_Haar(x).
    """
    # Build A(x)
    A = A_from_coords(x)
    
    # Get the adjoint matrix X = ad_A
    X = adjoint_matrix(A)
    
    # Compute eigenvalues of X
    eigenvalues = jnp.linalg.eigvals(X)
    
    # Make sure eigenvalues are real (should be for skew-symmetric matrix)
    eigenvalues = jnp.real(eigenvalues)
    
    # Compute sum of log(sinh(lambda_i) / lambda_i)
    log_sum = jnp.sum(jax.vmap(log_sinh_over_x)(eigenvalues))
    
    # S_Haar = -log det(sinh(X)/X) = -sum log(sinh(lambda_i)/lambda_i)
    return -log_sum


def hessian_S_haar(x):
    """
    Compute the Hessian matrix of S_Haar at x.
    
    Args:
        x: array of shape (3,).
    
    Returns:
        3x3 Hessian matrix.
    """
    return jacfwd(grad(S_haar))(x)


def sample_ball_uniform(radius, key):
    """
    Sample a point uniformly from a ball of given radius in R^3.
    
    Args:
        radius: radius of the ball.
        key: JAX random key.
    
    Returns:
        Array of shape (3,) sampled uniformly from the ball.
    """
    # Sample direction uniformly on sphere
    key1, key2 = jax.random.split(key)
    direction = jax.random.normal(key1, (3,))
    direction = direction / jnp.linalg.norm(direction)
    
    # Sample radius with correct distribution for volume
    r = radius * jax.random.uniform(key2)**(1.0/3.0)
    
    return r * direction


def compute_min_eigenvalue_hessian(x):
    """
    Compute the minimum eigenvalue of the Hessian of S_Haar at x.
    
    Args:
        x: array of shape (3,).
    
    Returns:
        Minimum eigenvalue of H(x).
    """
    H = hessian_S_haar(x)
    eigenvalues = jnp.linalg.eigvalsh(H)
    return jnp.min(eigenvalues)


def run_experiment(R_list, n_samples=1000, seed=42):
    """
    Run the numerical experiment for various radii.
    
    Args:
        R_list: list of radii to test.
        n_samples: number of samples per radius.
        seed: random seed.
    """
    key = jax.random.PRNGKey(seed)
    
    print("="*70)
    print("Numerical Experiment: Hessian of Haar Action on su(2)")
    print("="*70)
    print(f"Number of samples per radius: {n_samples}")
    print()
    
    for R in R_list:
        print(f"Radius R = {R:.2f}")
        print("-" * 50)
        
        min_eigenvalues = []
        
        for i in range(n_samples):
            key, subkey = jax.random.split(key)
            x = sample_ball_uniform(R, subkey)
            lam_min = compute_min_eigenvalue_hessian(x)
            min_eigenvalues.append(lam_min)
        
        min_eigenvalues = np.array(min_eigenvalues)
        
        print(f"  Min λ_min:  {np.min(min_eigenvalues):.6e}")
        print(f"  Max λ_min:  {np.max(min_eigenvalues):.6e}")
        print(f"  Mean λ_min: {np.mean(min_eigenvalues):.6e}")
        print(f"  Std λ_min:  {np.std(min_eigenvalues):.6e}")
        
        # Simple histogram
        print(f"\n  Histogram of λ_min:")
        hist, bins = np.histogram(min_eigenvalues, bins=10)
        for i in range(len(hist)):
            bar = "#" * int(50 * hist[i] / max(hist))
            print(f"    [{bins[i]:8.3e}, {bins[i+1]:8.3e}): {bar} ({hist[i]})")
        
        print()
    
    print("="*70)
    print("Experiment complete.")
    print("="*70)


if __name__ == "__main__":
    # List of radii to test
    R_list = [0.1, 0.5, 1.0, 2.0]
    
    # Number of samples per radius
    n_samples = 500
    
    # Run the experiment
    run_experiment(R_list, n_samples=n_samples)
