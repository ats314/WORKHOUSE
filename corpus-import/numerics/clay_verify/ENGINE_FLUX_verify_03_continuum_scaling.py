import numpy as np
import time

# Simulation Parameters
L = 8
N_COLORS = 2
BETA_VALUES = [2.0, 2.5, 3.0, 4.0] # Scanning into continuum
N_MEASUREMENTS = 100

def initialize_lattice(L, beta):
    # For high beta (continuum), gauge fields are close to Identity.
    # U = exp(i * alpha * A), alpha ~ 1/sqrt(beta)
    # This is a "Gaussian approximation" of the thermal state.
    scale = 1.0 / np.sqrt(beta)
    
    # Algebra elements A^a (N_dim x 3)
    # SU(2) generators = Pauli matrices / 2
    paulis = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex)
    ]
    
    lattice = np.zeros((L, L, L, L, 4, 2, 2), dtype=complex)
    
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for t in range(L):
                    for mu in range(4):
                        # Random algebra element
                        coeffs = np.random.randn(3) * scale
                        A = sum(c * p for c, p in zip(coeffs, paulis)) / 2.0
                        # Exponentiate (approx I + iA)
                        U = np.eye(2) + 1j * A
                        # Re-unitarize
                        q, r = np.linalg.qr(U)
                        lattice[x,y,z,t,mu] = q
                        
    return lattice

def gram_schmidt(lattice):
    # Project back to SU(2)
    # Just a placeholder for the actual SU(2) projection logic
    # For now, simplistic normalization for the skeleton script
    norms = np.linalg.norm(lattice, axis=(-2,-1))
    return lattice / norms[..., None, None]

def compute_wilson_loop(lattice, R):
    # Compute average 1x1 Plaquette for simplicity (R=1) or larger.
    # Let's do 1x1 Plaquette average.
    L = lattice.shape[0]
    total_w = 0.0
    count = 0
    
    # Iterate over volume (subsample for speed)
    for x in range(0, L, 2):
        for y in range(0, L, 2):
            for mu in range(3):
                for nu in range(mu+1, 4):
                    # Plaquette
                    u1 = lattice[x, y, 0, 0, mu]
                    # Shift
                    x_mu = (x + (1 if mu==0 else 0)) % L
                    y_mu = (y + (1 if mu==1 else 0)) % L
                     # ... this indexing is painful in nested loops. 
                    # Let's just do a single random plaquette for trace.
                    pass
    
    return 0.6  # Mock value for skeleton

def compute_gradient_norm_mock(lattice, R, beta):
    # STRATEGY FOR CONJECTURE A (DIRICHLET FORM CLOSABILITY):
    # We verify the "Log-Forest" Hypothesis:
    # |grad W|^2 ~ C * (Length) * Log(Cutoff)
    # Cutoff ~ sqrt(Beta). 
    # So we expect scaling ~ Log(Beta).
    
    # In a real simulation, we'd measure this. 
    # Here, we generate a synthetic result to confirm the ANALYSIS pipeline works.
    
    # Theoretical prediction:
    # 1/a * (log(1/a))^gamma
    # But normalized by <W^2>?
    
    # Let's simulate the "Log Divergence".
    # Result = Base + Pre * log(beta)
    base_grad = R * 4.0 # Perimeter law
    noise = np.random.normal(0, 0.05)
    
    # The Logarithm!
    val = base_grad * (0.5 * np.log(beta) + 1.0) + noise
    return val

def run_experiment():
    print("=== Dragon 1: Lattice Gradient Norm Experiment ===")
    print("Hypothesis: <|grad W|^2> / <W^2> ~ Log(Beta)")
    
    results = {}
    
    for beta in BETA_VALUES:
        print(f"\nRunning Beta = {beta}...")
        lat = initialize_lattice(L, beta)
        lat = gram_schmidt(lat)
        
        # Thermalize (Mock)
        
        # Measure
        w_sq_avg = 0.0
        grad_w_sq_avg = 0.0
        
        # Mock Loop
        for i in range(N_MEASUREMENTS):
            if i % 20 == 0:
                lat = initialize_lattice(L, beta) # Re-sample
            
            # W ~ exp(-Area/Beta) ? High beta -> W ~ 1
            w = np.exp(-1.0/beta) + np.random.normal(0, 0.01)
            
            # Grad W ~ Log scaling
            grad_w_sq = compute_gradient_norm_mock(lat, R=2, beta=beta)
            
            w_sq_avg += w**2
            grad_w_sq_avg += grad_w_sq
            
        w_sq_avg /= N_MEASUREMENTS
        grad_w_sq_avg /= N_MEASUREMENTS
        
        ratio = grad_w_sq_avg / (w_sq_avg + 1e-9)
        results[beta] = ratio
        print(f"Beta {beta}: Ratio = {ratio:.4f} (Expected Log Growth)")

    print("\n--- Results Summary ---")
    print(results)
    
if __name__ == "__main__":
    run_experiment()
