"""
VERIFIED_Topological_Susceptibility_Chi_Top_Extraction_Fourier_Fit.py

==============================================================================
WHAT THIS SCRIPT DOES:
==============================================================================
Extracts the topological susceptibility chi_top from free energy data F(theta)
using Fourier series fitting. The susceptibility is the curvature at theta=0:
    chi_top = d^2 F / d(theta)^2 |_{theta=0}

Compares polynomial fit vs Fourier fit - demonstrates that Fourier respects
the periodic nature of theta and gives better fits.

SEARCH KEYWORDS:
    topological susceptibility, chi_top, theta angle, free energy, Fourier fit,
    CP violation, curvature, topology, QCD, lattice, tensor network

THEORY CONNECTION:
    In QFT: chi_top = <Q^2> / V where Q is the topological charge.
    The theta-dependence of free energy encodes vacuum topology.
    Correctly extracting chi_top is crucial for understanding confinement.

VERIFICATION STATUS: VERIFIED (2026-01-01)
    - Synthetic test with known chi_top = 0.5 recovered accurately
    - Fourier method correctly computes second derivative from coefficients

DEPENDENCIES: numpy only
==============================================================================
"""

import numpy as np


def chi_from_quadratic_fit(theta, F):
    """
    Method A: Fit F(theta) = a + b*theta + c*theta^2 near theta=0.
    chi_top = 2c (second derivative at origin).
    
    For CP-symmetric theory, b should be approximately 0.
    """
    theta = np.asarray(theta)
    F = np.asarray(F)
    
    # Design matrix for quadratic fit
    X = np.column_stack([np.ones_like(theta), theta, theta**2])
    coeffs, residuals, rank, s = np.linalg.lstsq(X, F, rcond=None)
    
    a, b, c = coeffs
    chi = 2 * c
    
    return chi, {'a': a, 'b': b, 'c': c}


def chi_from_finite_diff(theta, F):
    """
    Method B: Central finite difference.
    chi_top = (F(delta) - 2*F(0) + F(-delta)) / delta^2
    
    Uses periodicity: F(-delta) = F(2*pi - delta).
    """
    theta = np.asarray(theta)
    F = np.asarray(F)
    
    # Find points closest to 0, delta, 2*pi - delta
    idx_0 = np.argmin(np.abs(theta))
    
    # Use smallest positive theta as delta
    positive_mask = theta > 0.01
    if not np.any(positive_mask):
        return np.nan, {}
    
    delta = np.min(theta[positive_mask])
    idx_pos = np.argmin(np.abs(theta - delta))
    idx_neg = np.argmin(np.abs(theta - (2*np.pi - delta)))
    
    F_0 = F[idx_0]
    F_pos = F[idx_pos]
    F_neg = F[idx_neg]
    
    chi = (F_pos - 2*F_0 + F_neg) / (delta**2)
    
    return chi, {'delta': delta, 'F_0': F_0, 'F_pos': F_pos, 'F_neg': F_neg}


def chi_from_fourier_fit(theta, F, n_max=4):
    """
    Method C: Fourier series fit.
    F(theta) = a_0 + sum_{n=1}^{n_max} a_n * cos(n*theta)
    
    For even F(theta) (CP symmetric), we use only cosines.
    chi_top = d^2F/d(theta)^2 |_0 = -sum_{n=1}^{n_max} n^2 * a_n
    """
    theta = np.asarray(theta)
    F = np.asarray(F)
    
    # Design matrix: [1, cos(theta), cos(2*theta), ..., cos(n_max*theta)]
    X = [np.ones_like(theta)]
    for n in range(1, n_max + 1):
        X.append(np.cos(n * theta))
    X = np.column_stack(X)
    
    coeffs, residuals, rank, s = np.linalg.lstsq(X, F, rcond=None)
    
    a_0 = coeffs[0]
    a_n = coeffs[1:]  # cos coefficients
    
    # chi_top = -sum n^2 * a_n
    chi = -np.sum([(n + 1)**2 * a_n[n] for n in range(len(a_n))])
    
    # Compute R^2 for fit quality
    F_pred = X @ coeffs
    ss_res = np.sum((F - F_pred)**2)
    ss_tot = np.sum((F - np.mean(F))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    
    return chi, {'a_0': a_0, 'a_n': a_n, 'R_squared': r_squared}


def generate_test_data(chi_true=0.5, n_points=20, noise=0.01, seed=42):
    """
    Generate synthetic F(theta) data with known chi_top.
    F(theta) = chi_true/2 * theta^2 for small theta (Taylor approx)
    Actually use: F(theta) = -chi_true * cos(theta) (periodic, gives same curvature)
    """
    rng = np.random.default_rng(seed)
    theta = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    
    # F(theta) = const - chi * cos(theta) gives F''(0) = chi
    F = 1.0 - chi_true * np.cos(theta) + noise * rng.normal(size=n_points)
    
    return theta, F, chi_true


if __name__ == "__main__":
    print("=" * 70)
    print("Topological Susceptibility Extraction Methods")
    print("=" * 70)
    
    # Test with synthetic data
    print("\nTest with synthetic data (true chi_top = 0.5)")
    print("-" * 50)
    
    theta, F, chi_true = generate_test_data(chi_true=0.5, n_points=20, noise=0.01)
    
    # Method A: Quadratic
    chi_quad, info_quad = chi_from_quadratic_fit(theta[theta < 1.0], F[theta < 1.0])
    print(f"Quadratic fit: chi_top = {chi_quad:.4f} (b = {info_quad['b']:.4f})")
    
    # Method B: Finite difference
    chi_fd, info_fd = chi_from_finite_diff(theta, F)
    print(f"Finite diff:   chi_top = {chi_fd:.4f} (delta = {info_fd.get('delta', np.nan):.4f})")
    
    # Method C: Fourier (recommended)
    chi_fourier, info_fourier = chi_from_fourier_fit(theta, F, n_max=4)
    print(f"Fourier fit:   chi_top = {chi_fourier:.4f} (R^2 = {info_fourier['R_squared']:.4f})")
    
    print(f"\nTrue value:    chi_top = {chi_true:.4f}")
    
    # Check which method is best
    errors = {
        'Quadratic': abs(chi_quad - chi_true),
        'Finite diff': abs(chi_fd - chi_true),
        'Fourier': abs(chi_fourier - chi_true)
    }
    best = min(errors, key=errors.get)
    
    print()
    print(f"{'Method':>15} | {'Extracted':>10} | {'Error':>10}")
    print("-" * 42)
    for method, error in errors.items():
        chi_val = {'Quadratic': chi_quad, 'Finite diff': chi_fd, 'Fourier': chi_fourier}[method]
        status = " (best)" if method == best else ""
        print(f"{method:>15} | {chi_val:>10.4f} | {error:>10.4f}{status}")
    
    print()
    if errors['Fourier'] < 0.1:
        print("[PASS] Fourier method extracts chi_top correctly")
    else:
        print("[WARN] Fourier extraction has significant error")
