import numpy as np
from scipy.optimize import minimize

def legendre_check(potential_func, dim, x_start, epsilon=0.1, label="Model"):
    """
    Computes the Dual Hessian (k*) of the potential V.
    STRATEGY FOR CONJECTURE B (FLOW CONTAINMENT):
    This demonstrates the "Shielding" mechanism: modifying the potential barrier 
    to confine the system to the convex region (one minimum), or separating sectors
    with infinite barriers (topology decoupling).
    """
    print(f"\n--- Analysis: {label} ---")
    
    # 1. Primal Vacuum
    res_vac = minimize(potential_func, x_start, method='BFGS')
    x_vac = res_vac.x
    print(f"Vacuum x: {x_vac}, V: {res_vac.fun:.6f}")
    
    # 2. Dual Probe
    direction = np.ones(dim)
    direction /= np.linalg.norm(direction)
    y_probe = direction * epsilon
    
    def dual_obj(x, y):
        return potential_func(x) - np.dot(y, x)
        
    res_dual = minimize(dual_obj, x_vac, args=(y_probe,), method='BFGS')
    v_star = -res_dual.fun
    
    linear = np.dot(y_probe, x_vac)
    v_star_quad = v_star - linear
    
    k_star = 2 * v_star_quad / (epsilon**2)
    stiffness = 1.0 / k_star if abs(k_star) > 1e-9 else 0.0
    
    print(f"Primal Mass^2: {stiffness:.6f}")
    return stiffness

def tunneling_check(potential_func, x_start, x_end, label="Tunneling Model"):
    """
    Estimates the tunneling barrier between two minima.
    """
    print(f"\n--- Tunneling Check: {label} ---")
    
    # Find minima
    res_vac1 = minimize(potential_func, x_start, method='BFGS')
    res_vac2 = minimize(potential_func, x_end, method='BFGS')
    
    vac1 = res_vac1.fun
    vac2 = res_vac2.fun
    
    # Find barrier (approximate midpoint max)
    midpoint = (res_vac1.x + res_vac2.x) / 2
    barrier_height = potential_func(midpoint) - min(vac1, vac2)
    
    print(f"Vacuum 1: {vac1:.6f} at {res_vac1.x}")
    print(f"Vacuum 2: {vac2:.6f} at {res_vac2.x}")
    print(f"Barrier Height: {barrier_height:.6f} at {midpoint}")
    
    # WKB Tunneling Rate ~ exp(- Integral sqrt(2V) dx)
    # Crude approx: exp(- sqrt(Height) * Width)
    width = np.linalg.norm(res_vac1.x - res_vac2.x)
    suppression = np.exp(- np.sqrt(barrier_height) * width)
    print(f"Tunneling Suppression Factor (approx): {suppression:.6e}")
    return suppression

def run_verification():
    # Case 1: Standard Double Well V = (x^2 - 1)^2
    # Minima at +/- 1. Barrier at 0 is 1.
    print("\n=== CASE 1: Double Well (No Shield) ===")
    def v_double(x): return (x[0]**2 - 1)**2
    tunneling_check(v_double, [-1], [1], label="Standard Double Well")
    
    # Case 2: Shielded Double Well V = (x^2 - 1)^2 + mu * x^2
    # Shield penalizes the region near 0 (the barrier).
    # Wait, mu*x^2 fills the well. We need a shield that penalizes the *transition*?
    # No, the Shield penalizes *large fields*. In topology, the transition requires large fields (sphaleron).
    # If we add mu*x^2, does it kill the barrier or raise it?
    # At x=0, V = 1. With mu*x^2, V=1. It doesn't help at x=0?
    # Ah, topological shield is usually grad(A)^2.
    # Let's try V = (x^2-1)^2 + mu * (x^2) isn't right because x=0 is the barrier.
    # The 'Defect' is the barrier configuration.
    # If the Shield is mu * V(x) itself? No.
    # Let's assume Shield = mu * x^2 (mass term).
    mu = 10.0
    print(f"\n=== CASE 2: Shielded Double Well (Mass Term mu={mu}) ===")
    def v_shielded(x): return (x[0]**2 - 1)**2 + mu * x[0]**2
    # This might destroy the double well structure if mu is large.
    # (x^2-1)^2 + mu x^2 = x^4 - 2x^2 + 1 + mu x^2 = x^4 + (mu-2)x^2 + 1
    # If mu > 2, the double well becomes a single well!
    # THAT is the victory. Tunneling stops because the sectors merge or one disappears?
    # No, in YM we want sectors to remain but be decoupled.
    # But if the barrier goes to infinity...
    tunneling_check(v_shielded, [-1], [1], label="Shielded (Massive)")

    # Case 3: The True Shield (Penalizing Flux)
    # V = (x^2-1)^2 + mu * (x^4) ? 
    # Just increasing the barrier height without destroying minima.
    print(f"\n=== CASE 3: Barrier Enhancement ===")
    def v_enhanced(x): return (x[0]**2 - 1)**2 + 10.0 * np.exp(-x[0]**2) # Gaussian bump at 0
    tunneling_check(v_enhanced, [-1], [1], label="Enhanced Barrier")

if __name__ == "__main__":
    run_verification()
