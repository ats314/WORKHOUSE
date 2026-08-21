# L2 SU3 Wilson Hessian

**Source file:** `L2 SU3 Wilson Hessian.txt`

---

```text
# ================================
#  L=2 SU(3) Wilson Hessian: gauge vs toron vs physical
#  Self-contained script for a fresh Colab notebook
# ================================
import jax
import jax.numpy as jnp
import jax.scipy as jsp
import numpy as np

jax.config.update("jax_enable_x64", True)

# ---------------------------
# SU(3) generators & Wilson action
# ---------------------------
def su3_generators():
    """Anti-Hermitian su(3) basis T_a = i/2 * lambda_a (Gell-Mann)."""
    lam = []
    lam.append(jnp.array([[0,1,0],[1,0,0],[0,0,0]], jnp.complex128))
    lam.append(jnp.array([[0,-1j,0],[1j,0,0],[0,0,0]], jnp.complex128))
    lam.append(jnp.array([[1,0,0],[0,-1,0],[0,0,0]], jnp.complex128))
    lam.append(jnp.array([[0,0,1],[0,0,0],[1,0,0]], jnp.complex128))
    lam.append(jnp.array([[0,0,-1j],[0,0,0],[1j,0,0]], jnp.complex128))
    lam.append(jnp.array([[0,0,0],[0,0,1],[0,1,0]], jnp.complex128))
    lam.append(jnp.array([[0,0,0],[0,0,-1j],[0,1j,0]], jnp.complex128))
    lam.append(jnp.array([[1,0,0],[0,1,0],[0,0,-2]], jnp.complex128)/jnp.sqrt(3.0))
    lam = jnp.stack(lam, axis=0)
    return 1j * lam / 2.0  # anti-Hermitian

T = su3_generators()  # shape (8,3,3)

def su3_alg_from_vec(a):
    # a[...,8] -> su(3) matrix
    return jnp.einsum("...a,aij->...ij", a, T)

def su3_exp(A):
    # Matrix exponential in double precision
    return jsp.linalg.expm(A)

def build_links(theta, L):
    """
    theta: flat real vector of length L^4 * 4 * 8
    returns U[x,y,z,t,mu,i,j]
    """
    flat = theta.reshape(-1, 8)
    A = jax.vmap(su3_alg_from_vec)(flat)   # (...,3,3) anti-Hermitian
    U = jax.vmap(su3_exp)(A)               # (...,3,3) unitary
    return U.reshape(L, L, L, L, 4, 3, 3)

def wilson_action(theta, L, beta=1.0):
    U = build_links(theta, L)
    S = 0.0
    # Wilson plaquettes
    for mu in range(4):
        for nu in range(mu+1, 4):
            U1 = U[..., mu, :, :]
            U2 = jnp.roll(U[..., nu, :, :], -1, axis=mu)
            U3 = jnp.swapaxes(jnp.conjugate(jnp.roll(U[..., mu, :, :], -1, axis=nu)), -1, -2)
            U4 = jnp.swapaxes(jnp.conjugate(U[..., nu, :, :]), -1, -2)
            P  = U1 @ U2 @ U3 @ U4
            tr = jnp.real(jnp.einsum("...ii->...", P))
            S  = S + jnp.sum(1.0 - tr/3.0)
    return beta * S

# ---------------------------
# Full Hessian at the vacuum
# ---------------------------
def build_hessian(L):
    n_params = (L**4) * 4 * 8

    def action_wrap(theta):
        return wilson_action(theta, L)

    grad_S = jax.grad(action_wrap)
    hess_fn = jax.jacfwd(grad_S)

    theta0 = jnp.zeros((n_params,), dtype=jnp.float64)
    H = hess_fn(theta0)           # JAX array
    H = np.array(H, dtype=float)  # to NumPy
    # Symmetrize for safety
    H = 0.5 * (H + H.T)
    return H

# ---------------------------
# Gauge and constant-link directions as explicit matrices
# ---------------------------
def alpha_to_theta(alpha, L):
    """
    Map gauge parameter alpha[x,y,z,t,a] (8 per site) to link variation
    theta[x,y,z,t,mu,a] at the vacuum via:
      δA_mu(x) = alpha(x) - alpha(x+mu)
    Returns flat vector of length L^4 * 4 * 8.
    """
    # alpha: (L,L,L,L,8)
    alpha = np.asarray(alpha)
    theta = np.zeros((L, L, L, L, 4, 8), dtype=float)
    for mu in range(4):
        alpha_fwd = np.roll(alpha, shift=-1, axis=mu)
        delta = alpha - alpha_fwd  # (...,8)
        theta[..., mu, :] = delta
    return theta.reshape(-1)

def build_gauge_matrix(L):
    """
    Build matrix G of shape (n_theta, n_alpha) such that
        delta_theta = G @ alpha_flat
    where alpha_flat enumerates alpha(x,a) basis vectors.
    """
    n_sites = L**4
    n_color = 8
    n_alpha = n_sites * n_color
    n_theta = n_sites * 4 * n_color

    G = np.zeros((n_theta, n_alpha), dtype=float)

    col = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    for a in range(n_color):
                        alpha = np.zeros((L, L, L, L, n_color), dtype=float)
                        alpha[x0, x1, x2, x3, a] = 1.0
                        G[:, col] = alpha_to_theta(alpha, L)
                        col += 1
    assert col == n_alpha
    return G

def build_constant_link_matrix(L):
    """
    Build matrix C of constant link variations:
    for each (mu,a), theta[x,...,mu,a] = 1 for all sites.
    """
    n_sites = L**4
    n_color = 8
    n_theta = n_sites * 4 * n_color
    n_const = 4 * n_color  # 4 directions * 8 color

    C = np.zeros((n_theta, n_const), dtype=float)

    col = 0
    for mu in range(4):
        for a in range(n_color):
            theta = np.zeros((L, L, L, L, 4, 8), dtype=float)
            theta[..., mu, a] = 1.0
            C[:, col] = theta.reshape(-1)
            col += 1
    assert col == n_const
    return C

def matrix_rank(A, tol=1e-10):
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > tol))

# ---------------------------
# Main diagnostic
# ---------------------------
def main():
    L = 2
    print(f"Building Hessian for L={L} (n_params = { (L**4)*4*8 }) ...")
    H = build_hessian(L)
    n = H.shape[0]

    # Eigenvalues of full Hessian
    evals, _ = np.linalg.eigh(H)
    evals_sorted = np.sort(evals)
    print("\n--- Global spectrum summary ---")
    print("Smallest 10 eigenvalues:")
    for i in range(10):
        print(f"  λ[{i}] = {evals_sorted[i]:+.6e}") # Fixed format specifier
    print(f"Largest eigenvalue: λ_max = {evals_sorted[-1]:.6e}")

    # Count near-zero modes with a numerical tolerance
    zero_tol = 1e-8
    n_zero = int(np.sum(np.abs(evals_sorted) < zero_tol))
    print(f"\nNumber of |λ| < {zero_tol:g} modes in full Hessian: {n_zero}")

    # ---- Gauge Jacobian ----
    print("\nBuilding explicit gauge-direction matrix G ...")
    G = build_gauge_matrix(L)
    rank_G = matrix_rank(G)
    print(f"Gauge parameter space dim        = {G.shape[1]}")
    print(f"Rank(Im G) (independent gauge directions in θ-space) = {rank_G}")

    # Check that H annihilates the gauge directions
    Hg = H @ G
    max_Hg = np.linalg.norm(Hg, axis=0).max()
    print(f"Max ||H * g|| over gauge columns = {max_Hg:.3e}")

    # ---- Constant link directions (torons before modding out gauge) ----
    print("\nBuilding constant-link matrix C ...")
    C = build_constant_link_matrix(L)
    rank_C = matrix_rank(C)
    print(f"Constant-link direction count     = {C.shape[1]} (4 directions × 8 colors)")
    print(f"Rank(span of constant-link columns) = {rank_C}")

    # Check how many constant-link directions are pure gauge
    # Intersection dimension: dim(Im G ∩ span C)
    GC = np.concatenate([G, C], axis=1)
    rank_GC = matrix_rank(GC)
    dim_intersection = rank_G + rank_C - rank_GC
    toron_dim = rank_C - dim_intersection

    print(f"\nRank(Im G ⊕ Const) = {rank_GC}")
    print(f"Intersection dim (pure-gauge constants) = {dim_intersection}")
    print(f'Toron dim (const links modulo gauge)   = {toron_dim}')

    # Project constant-link directions orthogonal to gauge space
    # so we keep only genuine torons
    # QR on G to get an orthonormal basis for gauge subspace
    Qg, _ = np.linalg.qr(G)  # n×rank_G (plus extra, but SVD rank already)
    Qg = Qg[:, :rank_G]
    # P_perp = I - Qg Qg^T
    C_perp = C - Qg @ (Qg.T @ C)
    rank_C_perp = matrix_rank(C_perp)
    print(f"Rank of C after projection orthogonal to gauge = {rank_C_perp}")

    # Check H on toron subspace
    Hc = H @ C_perp
    max_Hc = np.linalg.norm(Hc, axis=0).max()
    print(f"Max ||H * t|| over toron columns = {max_Hc:.3e}")

    # Combined gauge+toron subspace
    K = np.concatenate([G, C_perp], axis=1)
    rank_K = matrix_rank(K)
    print(f"\nTotal dim(gauge ⊕ toron) from explicit K = {rank_K}")
    print(f"Compare with # of near-zero eigenvalues  = {n_zero}")

    # ---------------------------
    # Project Hessian to orthogonal complement: physical sector
    # ---------------------------
    print("\nDiagonalizing H on the orthogonal complement of (gauge ⊕ toron) ...")
    U, S, VT = np.linalg.svd(K, full_matrices=True)
    rK = np.sum(S > 1e-10)
    Q_gc = U[:, :rK]   # basis for gauge+toron subspace
    Q_phys = U[:, rK:] # orthogonal complement (physical directions)

    print(f"dim physical subspace = {Q_phys.shape[1]} = {n - rK}")

    # Restrict Hessian: H_phys = Q_phys^T H Q_phys
    H_phys = Q_phys.T @ H @ Q_phys
    evals_phys, _ = np.linalg.eigh(H_phys)
    evals_phys_sorted = np.sort(evals_phys)

    print("\nLowest 10 eigenvalues in the physical sector:")
    for i in range(min(10, len(evals_phys_sorted))):
        print(f"  λ_phys[{i}] = {evals_phys_sorted[i]:.6e}")

    print("\nIf the story is correct, you should see:")
    print("  * H kills gauge directions up to numerical precision (max_Hg tiny).")
    print("  * H kills projected constant-link directions (torons) as well (max_Hc tiny).")
    print("  * number of near-zero eigenvalues ≈ dim(gauge ⊕ toron).")
    print("  * the first physical eigenvalue ≈ the 'mass gap' (~ 2/3 for L=2).")

if __name__ == "__main__":
    main()


Building Hessian for L=2 (n_params = 512) ...

--- Global spectrum summary ---
Smallest 10 eigenvalues:
  λ[0] = -1.947027e-15
  λ[1] = -1.752525e-15
  λ[2] = -1.627042e-15
  λ[3] = -1.263730e-15
  λ[4] = -1.245319e-15
  λ[5] = -1.151618e-15
  λ[6] = -1.097265e-15
  λ[7] = -1.089948e-15
  λ[8] = -1.076836e-15
  λ[9] = -1.073051e-15
Largest eigenvalue: λ_max = 2.666667e+00

Number of |λ| < 1e-08 modes in full Hessian: 152

Building explicit gauge-direction matrix G ...
Gauge parameter space dim        = 128
Rank(Im G) (independent gauge directions in θ-space) = 120
Max ||H * g|| over gauge columns = 5.035e-16

Building constant-link matrix C ...
Constant-link direction count     = 32 (4 directions × 8 colors)
Rank(span of constant-link columns) = 32

Rank(Im G ⊕ Const) = 152
Intersection dim (pure-gauge constants) = 0
Toron dim (const links modulo gauge)   = 32
Rank of C after projection orthogonal to gauge = 32
Max ||H * t|| over toron columns = 6.433e-16

Total dim(gauge ⊕ toron) from explicit K = 152
Compare with # of near-zero eigenvalues  = 152

Diagonalizing H on the orthogonal complement of (gauge ⊕ toron) ...
dim physical subspace = 360 = 360

Lowest 10 eigenvalues in the physical sector:
  λ_phys[0] = 6.666667e-01
  λ_phys[1] = 6.666667e-01
  λ_phys[2] = 6.666667e-01
  λ_phys[3] = 6.666667e-01
  λ_phys[4] = 6.666667e-01
  λ_phys[5] = 6.666667e-01
  λ_phys[6] = 6.666667e-01
  λ_phys[7] = 6.666667e-01
  λ_phys[8] = 6.666667e-01
  λ_phys[9] = 6.666667e-01

If the story is correct, you should see:
  * H kills gauge directions up to numerical precision (max_Hg tiny).
  * H kills projected constant-link directions (torons) as well (max_Hc tiny).
  * number of near-zero eigenvalues ≈ dim(gauge ⊕ toron).
  * the first physical eigenvalue ≈ the 'mass gap' (~ 2/3 for L=2).
/usr/local/lib/python3.12/dist-packages/jax/_src/lax/lax.py:5473: ComplexWarning: Casting complex values to real discards the imaginary part
  x_bar = _convert_element_type(x_bar, x.aval.dtype, x.aval.weak_type)
```
