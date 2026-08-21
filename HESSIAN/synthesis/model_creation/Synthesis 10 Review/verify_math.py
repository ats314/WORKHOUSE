"""
Synthesis 10 Mathematical Verification Tools
=============================================
Tools for auditing mathematical claims in the synthesis document.
"""

import numpy as np
from scipy.optimize import brentq

# =============================================================================
# SU(2) Haar Hessian Eigenvalues (from 02_SU2_SingleLink_BetaC.md)
# =============================================================================

def haar_eigenvalue_radial(theta):
    """
    Radial Haar Hessian eigenvalue for SU(2).
    lambda^H_rad(theta) = (1/2) * (csc^2(theta) - 1/theta^2)
    
    At theta=0: limit = 1/6
    """
    if np.abs(theta) < 1e-8:
        return 1/6  # Taylor expansion limit
    return 0.5 * (1/np.sin(theta)**2 - 1/theta**2)

def haar_eigenvalue_tangential(theta):
    """
    Tangential Haar Hessian eigenvalue for SU(2).
    lambda^H_tan(theta) = (1 - theta*cot(theta)) / (2*theta^2)
    
    At theta=0: limit = 1/6
    """
    if np.abs(theta) < 1e-8:
        return 1/6  # Taylor expansion limit
    return (1 - theta/np.tan(theta)) / (2*theta**2)

def wilson_eigenvalue_radial(theta, beta):
    """Wilson contribution to radial eigenvalue."""
    return (beta/4) * np.cos(theta)

def wilson_eigenvalue_tangential(theta, beta):
    """Wilson contribution to tangential eigenvalue."""
    if np.abs(theta) < 1e-8:
        return beta/4
    return (beta/4) * np.sin(theta)/theta

def total_eigenvalue_radial(theta, beta):
    """Total (Haar + Wilson) radial eigenvalue."""
    return haar_eigenvalue_radial(theta) + wilson_eigenvalue_radial(theta, beta)

def total_eigenvalue_tangential(theta, beta):
    """Total (Haar + Wilson) tangential eigenvalue."""
    return haar_eigenvalue_tangential(theta) + wilson_eigenvalue_tangential(theta, beta)

# =============================================================================
# Verification Functions
# =============================================================================

def verify_haar_global_bound():
    """
    Verify the claim in Ch 25: "nabla^2 S_Haar >= (1/6) I for all alpha"
    
    EXPECTED: This is FALSE. The eigenvalues decay toward 0 as theta -> pi.
    """
    print("=" * 60)
    print("VERIFICATION: Haar Hessian Global Lower Bound")
    print("=" * 60)
    print("Claim (Ch 25, Line 1302): Haar Hessian >= (1/6) I globally")
    print()
    
    theta_values = np.linspace(0.01, np.pi - 0.01, 100)
    
    min_rad = float('inf')
    min_tan = float('inf')
    min_rad_theta = 0
    min_tan_theta = 0
    
    print("Sampling eigenvalues across theta in (0, pi):")
    print("-" * 50)
    for theta in [0.01, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.1]:
        lr = haar_eigenvalue_radial(theta)
        lt = haar_eigenvalue_tangential(theta)
        print(f"theta={theta:.2f}: lambda_rad={lr:.6f}, lambda_tan={lt:.6f}")
    print("-" * 50)
    
    for theta in theta_values:
        lr = haar_eigenvalue_radial(theta)
        lt = haar_eigenvalue_tangential(theta)
        if lr < min_rad:
            min_rad = lr
            min_rad_theta = theta
        if lt < min_tan:
            min_tan = lt
            min_tan_theta = theta
    
    print(f"Radial eigenvalue at theta=0:   {haar_eigenvalue_radial(0):.6f}")
    print(f"Minimum radial eigenvalue:      {min_rad:.6f} at theta={min_rad_theta:.4f}")
    print(f"Tangential eigenvalue at theta=0: {haar_eigenvalue_tangential(0):.6f}")
    print(f"Minimum tangential eigenvalue:  {min_tan:.6f} at theta={min_tan_theta:.4f}")
    print()
    
    if min_rad < 1/6 - 0.001 or min_tan < 1/6 - 0.001:
        print("[X] CLAIM IS FALSE: Eigenvalues drop below 1/6 away from origin")
        print(f"   Global minimum = {min(min_rad, min_tan):.6f} < 1/6 = {1/6:.6f}")
    else:
        print("[OK] Claim appears correct - eigenvalues stay >= 1/6")

    
    return min_rad, min_tan

def verify_c0_coefficient():
    """
    Verify the c_0 = (N^2-1)/2N formula for SU(N).
    """
    print("=" * 60)
    print("VERIFICATION: c_0 Coefficient Values")
    print("=" * 60)
    
    for N in [2, 3, 4]:
        c0 = (N**2 - 1) / (2*N)
        print(f"SU({N}): c_0 = (N²-1)/2N = ({N**2}-1)/{2*N} = {c0:.6f}")
    
    print()
    print("Compare to Haar eigenvalue at origin (axis-angle): 1/6 = 0.1667")
    print("Ratio for SU(2): c_0 / (1/6) = 0.75 / 0.1667 = 4.5")
    print()
    print("⚠️ These are DIFFERENT normalizations!")

def find_beta_critical():
    """
    Find the critical beta where convexity first fails.
    """
    print("=" * 60)
    print("VERIFICATION: Critical Beta for Convexity Loss")
    print("=" * 60)
    
    # For each theta in (pi/2, pi), find beta that makes radial eigenvalue = 0
    def beta_zero_crossing(theta):
        """Beta value that makes lambda_rad = 0 at given theta."""
        if theta <= np.pi/2:
            return float('inf')
        hr = haar_eigenvalue_radial(theta)
        # lambda_rad = hr + (beta/4)*cos(theta) = 0
        # beta = -4*hr / cos(theta)
        return -4 * hr / np.cos(theta)
    
    theta_scan = np.linspace(np.pi/2 + 0.01, np.pi - 0.01, 1000)
    beta_values = [beta_zero_crossing(t) for t in theta_scan]
    
    beta_c = min(beta_values)
    theta_c = theta_scan[np.argmin(beta_values)]
    
    print(f"Critical beta: β_c ≈ {beta_c:.6f}")
    print(f"At theta:      θ_* ≈ {theta_c:.6f} rad")
    print()
    print("Compare to source file (02_SU2_SingleLink_BetaC.md):")
    print("  β_c ≈ 4.413914663162")
    print("  θ_* ≈ 2.118504915119")
    
    return beta_c, theta_c

def verify_riccati_fixed_point():
    """
    Verify the Riccati fixed point formula.
    ODE: d lambda/dt = sigma - 2*lambda^2
    Fixed point: lambda_* = sqrt(sigma/2)
    """
    print("=" * 60)
    print("VERIFICATION: Riccati Fixed Point")
    print("=" * 60)
    
    print("ODE: dλ/dt = σ - 2λ²")
    print()
    print("At fixed point: 0 = σ - 2λ²")
    print("                λ² = σ/2")
    print("                λ_* = √(σ/2)")
    print()
    print("NOT √σ (which would be from dλ/dt = σ - λ²)")
    
    # Numerical verification
    from scipy.integrate import odeint
    
    sigma = 1.0
    def riccati(lam, t):
        return sigma - 2*lam[0]**2
    
    t = np.linspace(0, 20, 1000)
    lam0 = [0.1]
    sol = odeint(riccati, lam0, t)
    
    theoretical = np.sqrt(sigma/2)
    numerical = sol[-1, 0]
    
    print(f"For σ = {sigma}:")
    print(f"  Theoretical fixed point: √(σ/2) = {theoretical:.6f}")
    print(f"  Numerical limit:                 = {numerical:.6f}")
    print(f"  Match: {'✓' if abs(theoretical - numerical) < 0.001 else '❌'}")

# =============================================================================
# Run All Verifications
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SYNTHESIS 10 MATHEMATICAL AUDIT")
    print("="*60 + "\n")
    
    verify_haar_global_bound()
    print()
    verify_c0_coefficient()
    print()
    find_beta_critical()
    print()
    verify_riccati_fixed_point()
