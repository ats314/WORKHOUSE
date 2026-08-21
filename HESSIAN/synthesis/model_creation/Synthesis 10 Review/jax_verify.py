"""
jax_verify.py - JAX Automatic Differentiation Verification
===========================================================
Verify Hessian formulas by computing them directly via autodiff.
This catches errors where manual differentiation went wrong.
"""

import jax
import jax.numpy as jnp
from jax import grad, hessian, jvp, vjp
import numpy as np

# Enable 64-bit precision for numerical accuracy
jax.config.update("jax_enable_x64", True)

print("="*60)
print("JAX AUTODIFF VERIFICATION")
print("="*60)

# =============================================================================
# 1. Verify vHJ: If P = exp(-S), and P evolves by heat, what does S do?
# =============================================================================

print("\n--- Test 1: vHJ Derivation Check ---")

def test_vhj_derivation():
    """
    Verify the vHJ equation by computing derivatives of exp(-S).
    
    If partial_t P = Delta P, and P = exp(-S), then:
    S_t = Delta S - |grad S|^2
    """
    
    # Define a test action S(x) = (1/2) x^T A x for quadratic case
    A = jnp.array([[2.0, 0.5], [0.5, 3.0]])  # Positive definite
    
    def S(x):
        return 0.5 * x @ A @ x
    
    def P(x):
        return jnp.exp(-S(x))
    
    # Compute Laplacian of P at test point
    x0 = jnp.array([0.3, 0.7])
    
    # Hessian of P
    H_P = hessian(P)(x0)
    laplacian_P = jnp.trace(H_P)
    
    # Gradient and Hessian of S
    grad_S = grad(S)(x0)
    H_S = hessian(S)(x0)
    laplacian_S = jnp.trace(H_S)
    grad_S_squared = jnp.dot(grad_S, grad_S)
    
    # vHJ prediction: S_t = Delta S - |grad S|^2
    # For stationary P, this should give: laplacian_P / P = -(laplacian_S) + |grad S|^2
    
    P_val = P(x0)
    lhs = laplacian_P / P_val  # Delta P / P
    rhs = -laplacian_S + grad_S_squared  # predicted from S
    
    print(f"Test point: x = {x0}")
    print(f"S(x) = {S(x0):.6f}")
    print(f"Delta P / P = {lhs:.6f}")
    print(f"-Delta S + |grad S|^2 = {rhs:.6f}")
    print(f"Match: {jnp.abs(lhs - rhs) < 1e-10}")

test_vhj_derivation()

# =============================================================================
# 2. Verify Hessian of |grad S|^2 gives 2H^2 + drift term
# =============================================================================

print("\n--- Test 2: Hessian of |grad S|^2 ---")

def test_hessian_grad_squared():
    """
    Verify that nabla^2(|grad S|^2) = 2 H^2 + drift terms
    """
    
    # Test action: cubic to have nontrivial third derivatives
    def S(x):
        return x[0]**3 + x[1]**3 + 2*x[0]*x[1]**2 + x[0]**2
    
    def grad_S_squared(x):
        g = grad(S)(x)
        return jnp.dot(g, g)
    
    x0 = jnp.array([0.5, 0.8])
    
    # Compute Hessian of |grad S|^2 via autodiff
    H_gs = hessian(grad_S_squared)(x0)
    
    # Compute H = nabla^2 S
    H = hessian(S)(x0)
    
    # Compute H^2
    H_squared = H @ H
    
    # The leading term should be 2 * H^2
    two_H_squared = 2 * H_squared
    
    print(f"Hessian of |grad S|^2:")
    print(H_gs)
    print(f"\n2 * H^2:")
    print(two_H_squared)
    print(f"\nDifference (drift term):")
    print(H_gs - two_H_squared)
    print(f"\nNote: Difference is NOT zero - it contains the drift term (grad S . grad H)")

test_hessian_grad_squared()

# =============================================================================
# 3. Verify SU(2) Haar Hessian eigenvalue formula
# =============================================================================

print("\n--- Test 3: SU(2) Haar Action Hessian ---")

def test_su2_haar():
    """
    Verify the Haar action S_H = -2*log(sin(theta)/theta) has
    eigenvalues matching the claimed formulas at theta = 0.
    """
    
    def S_haar_radial(theta_val):
        """Haar action as function of theta = |a|/2"""
        # Avoid singularity at theta=0
        theta = jnp.maximum(theta_val, 1e-8)
        return -2.0 * jnp.log(jnp.sin(theta) / theta)
    
    # For radial function, second derivative is just d^2/dtheta^2
    def d2_S_haar(theta_val):
        return grad(grad(S_haar_radial))(theta_val)
    
    # Test at several theta values
    print("Verifying radial eigenvalue formula:")
    print("lambda_rad(theta) = (1/2)(csc^2(theta) - 1/theta^2)")
    print()
    
    for theta in [0.1, 0.5, 1.0, 2.0]:
        # Autodiff value
        autodiff_val = d2_S_haar(theta)
        
        # Formula value
        formula_val = 0.5 * (1/np.sin(theta)**2 - 1/theta**2)
        
        print(f"theta={theta:.1f}: autodiff={float(autodiff_val):.6f}, formula={formula_val:.6f}, match={abs(float(autodiff_val)-formula_val)<1e-6}")

test_su2_haar()

# =============================================================================
# 4. Random falsification test
# =============================================================================

print("\n--- Test 4: Random Point Falsification ---")

def random_falsification():
    """
    Generate random test cases to try to falsify bounds.
    """
    
    key = jax.random.PRNGKey(42)
    
    # Test: Haar eigenvalues should always be >= 1/6
    print("Testing claim: Haar eigenvalues >= 1/6 at all theta in (0, pi)")
    
    theta_samples = jax.random.uniform(key, (1000,), minval=0.01, maxval=3.1)
    
    def haar_eig_rad(theta):
        return 0.5 * (1/jnp.sin(theta)**2 - 1/theta**2)
    
    min_eig = float('inf')
    min_theta = 0
    violations = 0
    
    for theta in theta_samples:
        eig = float(haar_eig_rad(theta))
        if eig < min_eig:
            min_eig = eig
            min_theta = float(theta)
        if eig < 1/6 - 0.001:
            violations += 1
    
    print(f"Samples: 1000")
    print(f"Minimum eigenvalue found: {min_eig:.6f} at theta={min_theta:.4f}")
    print(f"Violations (< 1/6): {violations}")
    print(f"Claim verified: {violations == 0}")

random_falsification()

print("\n" + "="*60)
print("JAX VERIFICATION COMPLETE")
print("="*60)
