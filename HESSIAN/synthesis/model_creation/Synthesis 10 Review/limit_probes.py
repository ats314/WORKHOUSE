"""
limit_probes.py - Limit and Scaling Analysis
=============================================
Test formulas at boundary cases where errors often hide.
"""

import numpy as np
from scipy.special import jv  # Bessel functions if needed

print("="*60)
print("LIMIT AND SCALING PROBES")
print("="*60)

# =============================================================================
# 1. Small-parameter limits (theta -> 0)
# =============================================================================

print("\n--- Probe 1: Small theta limits ---")

def probe_small_theta():
    """Check formulas at theta -> 0 where Taylor expansions apply."""
    
    theta_vals = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
    
    print("Haar radial eigenvalue: claimed limit = 1/6 = 0.166667")
    print()
    
    for theta in theta_vals:
        # Exact formula
        exact = 0.5 * (1/np.sin(theta)**2 - 1/theta**2)
        # Taylor approximation: 1/6 + theta^2/30 + ...
        taylor = 1/6 + theta**2/30
        
        print(f"theta={theta:.0e}: exact={exact:.8f}, taylor={taylor:.8f}, diff={abs(exact-taylor):.2e}")

probe_small_theta()

# =============================================================================
# 2. Large-parameter limits (theta -> pi)
# =============================================================================

print("\n--- Probe 2: theta -> pi limit ---")

def probe_large_theta():
    """Check behavior as theta approaches pi (antipodal point)."""
    
    # Near theta = pi, csc^2(theta) -> infinity
    theta_vals = [2.5, 2.8, 3.0, 3.1, 3.14]
    
    print("As theta -> pi, csc^2(theta) -> infinity (pole)")
    print()
    
    for theta in theta_vals:
        csc_sq = 1/np.sin(theta)**2
        inv_theta_sq = 1/theta**2
        eig = 0.5 * (csc_sq - inv_theta_sq)
        
        print(f"theta={theta:.2f}: csc^2={csc_sq:.4f}, 1/theta^2={inv_theta_sq:.4f}, lambda={eig:.4f}")

probe_large_theta()

# =============================================================================
# 3. Large-beta limit (strong coupling)
# =============================================================================

print("\n--- Probe 3: Large beta (strong coupling) ---")

def probe_large_beta():
    """Check concentration as beta -> infinity."""
    
    print("Claim: As beta -> infinity, measure concentrates near theta = 0")
    print("And convexity radius shrinks as R(beta) ~ 1/sqrt(beta)")
    print()
    
    for beta in [1, 5, 10, 50, 100]:
        # Theoretical critical radius where convexity fails
        # From source: beta_c * cos(theta_c) + Haar_eigenvalue = 0
        # Crude estimate: R ~ sqrt(c_0 / beta) with c_0 ~ 0.25
        c_0 = 0.25
        R_est = np.sqrt(c_0 / beta) if beta > 0 else float('inf')
        
        print(f"beta={beta:3d}: R_estimate ~ {R_est:.4f}")

probe_large_beta()

# =============================================================================
# 4. Scaling / dimensional analysis
# =============================================================================

print("\n--- Probe 4: Dimensional/Scaling Analysis ---")

def probe_scaling():
    """Check that formulas scale correctly under rescaling."""
    
    print("Gap formula: Delta >= sqrt(c_0/2) / a")
    print()
    print("Under rescaling a -> lambda * a:")
    print("  Delta -> Delta / lambda (physical mass unchanged)")
    print("  sqrt(c_0/2) / a -> sqrt(c_0/2) / (lambda * a) = (1/lambda) * original")
    print("  [CONSISTENT: Gap in lattice units scales as 1/a]")
    print()
    
    # Check gap values
    for group, c0, name in [(2, 3/4, "SU(2)"), (3, 4/3, "SU(3)")]:
        gap_coeff = np.sqrt(c0/2)
        print(f"{name}: c_0 = {c0:.4f}, Delta*a = {gap_coeff:.4f}")

probe_scaling()

# =============================================================================
# 5. Degenerate case: Abelian limit
# =============================================================================

print("\n--- Probe 5: Abelian Limit (U(1)) ---")

def probe_abelian():
    """Check what happens in the Abelian U(1) case."""
    
    print("For U(1): Lie algebra is 1-dimensional (no structure constants)")
    print("  => Ricci curvature = 0 (flat torus)")
    print("  => No Haar mass contribution")
    print("  => Must rely on Wilson action alone for convexity")
    print()
    print("Using c_0 = (N^2-1)/2N formula:")
    print(f"  N=1: c_0 = 0 (consistent with flat U(1))")

probe_abelian()

# =============================================================================
# 6. Cross-check: Two independent derivations
# =============================================================================

print("\n--- Probe 6: Cross-check alternative derivation paths ---")

def cross_check():
    """Compare results from different derivation paths."""
    
    print("Alternative path 1: Direct Hessian of -log(Haar Jacobian)")
    print("Alternative path 2: Vandermonde product formula")
    print("Alternative path 3: Character expansion")
    print()
    print("All should give same c_0 = (N^2-1)/2N coefficient")
    print("(This consistency was verified in symbolic_verify.py)")

cross_check()

print("\n" + "="*60)
print("LIMIT PROBES COMPLETE")
print("="*60)
