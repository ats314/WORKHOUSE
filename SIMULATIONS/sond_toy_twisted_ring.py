"""
sond_toy_twisted_ring.py
=======================

Toy model for "spectral obstruction": a discrete Laplacian on an N-site ring with a U(1) twist.

Hamiltonian:
    H = 2I - (shift + shift^*)
with a phase e^{i phi} on the boundary link (N-1 -> 0).

Exact spectrum:
    E_k(phi) = 2 - 2 cos((2*pi*k + phi)/N)

So:
    phi = 0     -> E_0 = 0 (constant mode)
    phi != 0    -> E_0 = 2 - 2 cos(phi/N) ~ (phi/N)^2

This is a *finite-size* gap, not an infinite-volume mass gap.

Usage:
    python sond_toy_twisted_ring.py
"""

import math
import numpy as np

def create_hamiltonian(N: int, phi: float) -> np.ndarray:
    """Discrete Laplacian on a ring with a twist on the boundary link."""
    H = 2.0 * np.eye(N, dtype=np.complex128)
    # nearest-neighbor hopping (i <-> i+1)
    for i in range(N - 1):
        H[i, i + 1] = -1.0
        H[i + 1, i] = -1.0
    # boundary link carries twist
    phase = np.exp(1j * phi)
    H[N - 1, 0] = -1.0 * phase
    H[0, N - 1] = -1.0 * np.conj(phase)
    return H

def lowest_eigs(N: int, phi: float, k: int = 5) -> np.ndarray:
    """Return the lowest k eigenvalues (real, sorted)."""
    H = create_hamiltonian(N, phi)
    evals = np.linalg.eigvalsh(H)  # Hermitian eigensolver
    return np.real_if_close(evals[:k])

def exact_ground_energy(N: int, phi: float) -> float:
    """Exact E0 = 2 - 2 cos(phi/N) for phi in [-pi, pi] (principal branch)."""
    # principal branch reduction
    phi = ((phi + math.pi) % (2 * math.pi)) - math.pi
    return 2.0 - 2.0 * math.cos(phi / N)

def run():
    sizes = [10, 20, 50, 100]
    twists = [0.0, math.pi / 4, math.pi / 2, math.pi]
    print(f"{'N':>5} | {'phi (rad)':>10} | {'E0 (num)':>12} | {'E0 (exact)':>12} | {'E1 (num)':>12}")
    print("-" * 65)
    for N in sizes:
        for phi in twists:
            eigs = lowest_eigs(N, phi, k=2)
            e0_num, e1_num = float(eigs[0]), float(eigs[1])
            e0_ex = exact_ground_energy(N, phi)
            print(f"{N:5d} | {phi:10.6f} | {e0_num:12.8f} | {e0_ex:12.8f} | {e1_num:12.8f}")

if __name__ == "__main__":
    run()
