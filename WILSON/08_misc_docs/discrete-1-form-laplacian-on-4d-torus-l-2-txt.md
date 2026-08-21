# Discrete 1-form Laplacian on 4D torus, L=2

**Source file:** `Discrete 1-form Laplacian on 4D torus, L=2.txt`

---

```text
# ============================================
# Discrete 1-form Laplacian on 4D torus, L=2
# Check: ker(Δ_1) = gauge ⊕ toron (SU(3) colors)
# ============================================
import numpy as np

# ---------------------------
# Basic 4D lattice indexing
# ---------------------------
def site_index_4d(x, y, z, t, L):
    return ((x * L + y) * L + z) * L + t

def shift_site(x, y, z, t, mu, L, delta=1):
    if mu == 0:
        x = (x + delta) % L
    elif mu == 1:
        y = (y + delta) % L
    elif mu == 2:
        z = (z + delta) % L
    else:
        t = (t + delta) % L
    return x, y, z, t

# -------------------------------------------------
# Build discrete exterior derivative d_1 : C^1 -> C^2
# F_{μν}(x) = Δ_μ A_ν(x) - Δ_ν A_μ(x)
# with forward differences and periodic BCs.
# We work in θ-space of shape (L^4, 4, n_color)
# flattened as index = (((site*4)+mu)*n_color + a)
# -------------------------------------------------
def build_D_1(L, n_color=8):
    n_sites = L**4
    n_dir   = 4
    pairs   = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
    n_pairs = len(pairs)

    n_theta = n_sites * n_dir * n_color         # link DOFs (1-forms)
    n_plaq  = n_sites * n_pairs * n_color       # plaquette DOFs (2-forms)

    D = np.zeros((n_plaq, n_theta), dtype=float)
    pair_index = {p: i for i, p in enumerate(pairs)}

    for x in range(L):
        for y in range(L):
            for z in range(L):
                for t in range(L):
                    s = site_index_4d(x, y, z, t, L)
                    for (mu, nu) in pairs:
                        pidx = pair_index[(mu, nu)]
                        for a in range(n_color):
                            row = ((s * n_pairs + pidx) * n_color + a)

                            # sites for A_ν(x+μ) and A_μ(x+ν)
                            sx_mu, sy_mu, sz_mu, st_mu = shift_site(x, y, z, t, mu, L, +1)
                            s_mu_fwd = site_index_4d(sx_mu, sy_mu, sz_mu, st_mu, L)

                            sx_nu, sy_nu, sz_nu, st_nu = shift_site(x, y, z, t, nu, L, +1)
                            s_nu_fwd = site_index_4d(sx_nu, sy_nu, sz_nu, st_nu, L)

                            # Column indices in θ for the four links in F_{μν}(x)
                            col_Anu_fwd = (((s_mu_fwd * 4 + nu) * n_color) + a)
                            col_Anu     = (((s        * 4 + nu) * n_color) + a)
                            col_Amu_fwd = (((s_nu_fwd * 4 + mu) * n_color) + a)
                            col_Amu     = (((s        * 4 + mu) * n_color) + a)

                            # F_{μν}(x) = A_ν(x+μ) - A_ν(x) - (A_μ(x+ν) - A_μ(x))
                            D[row, col_Anu_fwd] += 1.0
                            D[row, col_Anu]     -= 1.0
                            D[row, col_Amu_fwd] -= 1.0
                            D[row, col_Amu]     += 1.0

    return D

# -------------------------------------------------
# Gauge map alpha(x,a) -> θ (link space) via
#   A_μ(x) = α(x) - α(x+μ)
# -------------------------------------------------
def alpha_to_theta(alpha, L, n_color=8):
    """
    alpha: shape (L,L,L,L,n_color)
    return theta_flat: length L^4 * 4 * n_color,
    with ordering consistent with build_D_1.
    """
    alpha = np.asarray(alpha, float)
    theta = np.zeros((L, L, L, L, 4, n_color), dtype=float)
    for mu in range(4):
        alpha_fwd = np.roll(alpha, shift=-1, axis=mu)
        delta = alpha - alpha_fwd  #  Δ_μ α
        theta[..., mu, :] = delta
    return theta.reshape(-1)

def build_gauge_matrix(L, n_color=8):
    n_sites = L**4
    n_alpha = n_sites * n_color
    n_theta = n_sites * 4 * n_color
    G = np.zeros((n_theta, n_alpha), dtype=float)

    col = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for t in range(L):
                    for a in range(n_color):
                        alpha = np.zeros((L, L, L, L, n_color), dtype=float)
                        alpha[x, y, z, t, a] = 1.0
                        G[:, col] = alpha_to_theta(alpha, L, n_color)
                        col += 1
    assert col == n_alpha
    return G

# -------------------------------------------------
# Constant-link (toron) directions:
#   A_μ(x) = const in x, one basis per (μ,a).
# -------------------------------------------------
def build_constant_link_matrix(L, n_color=8):
    n_sites = L**4
    n_theta = n_sites * 4 * n_color
    n_const = 4 * n_color   # 4 dirs × 8 colors

    C = np.zeros((n_theta, n_const), dtype=float)

    col = 0
    for mu in range(4):
        for a in range(n_color):
            theta = np.zeros((L, L, L, L, 4, n_color), dtype=float)
            theta[..., mu, a] = 1.0
            C[:, col] = theta.reshape(-1)
            col += 1
    assert col == n_const
    return C

def matrix_rank(A, tol=1e-10):
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > tol))

# -------------------------------------------------
# Main diagnostic
# -------------------------------------------------
def main():
    L        = 2
    n_color  = 8
    n_sites  = L**4
    n_theta  = n_sites * 4 * n_color

    print(f"Building Δ_1 = d^T d for L={L}, n_color={n_color}")
    print(f"Total link DOFs n_theta = {n_theta}")

    D = build_D_1(L, n_color)
    Delta = D.T @ D
    # Sanity check symmetry
    print("Symmetric check:", np.allclose(Delta, Delta.T))

    # Spectrum of Δ_1
    evals, evecs = np.linalg.eigh(Delta)
    evals_sorted = np.sort(evals)

    print("\n--- Global spectrum summary (Δ_1) ---")
    print("Smallest 10 eigenvalues:")
    for i in range(10):
        print(f"  λ[{i}] = {evals_sorted[i]:+.6e}")
    print(f"Largest eigenvalue: λ_max = {evals_sorted[-1]:.6e}")

    zero_tol = 1e-8
    n_zero = int(np.sum(np.abs(evals_sorted) < zero_tol))
    print(f"\nNumber of |λ| < {zero_tol:g} modes in Δ_1: {n_zero}")

    # Gauge and toron subspaces
    print("\nBuilding explicit gauge-direction matrix G ...")
    G = build_gauge_matrix(L, n_color)
    rank_G = matrix_rank(G)
    print(f"Gauge parameter space dim          = {G.shape[1]}")
    print(f"Rank(Im G) in link space           = {rank_G}")

    print("\nBuilding constant-link matrix C (torons before mod gauge) ...")
    C = build_constant_link_matrix(L, n_color)
    rank_C = matrix_rank(C)
    print(f"Constant-link direction count      = {C.shape[1]} (4 dirs × {n_color} colors)")
    print(f"Rank(span of constant-link cols)   = {rank_C}")

    # Combined subspace
    GC = np.concatenate([G, C], axis=1)
    rank_GC = matrix_rank(GC)
    dim_intersection = rank_G + rank_C - rank_GC
    toron_dim = rank_C - dim_intersection

    print(f"\nRank(Im G ⊕ Const)                 = {rank_GC}")
    print(f"Intersection dim (pure-gauge const)= {dim_intersection}")
    print(f"Toron dim (const links mod gauge)  = {toron_dim}")

    # Check that Δ_1 annihilates these directions
    DG = Delta @ G
    DC = Delta @ C
    max_DG = np.linalg.norm(DG, axis=0).max()
    max_DC = np.linalg.norm(DC, axis=0).max()
    print(f"\nMax ||Δ_1 * gauge|| over columns   = {max_DG:.3e}")
    print(f"Max ||Δ_1 * const|| over columns   = {max_DC:.3e}")

    print("\nTotal dim(gauge ⊕ toron) from GC   =", rank_GC)
    print("Compare with # of zero modes       =", n_zero)

    # Project to orthogonal complement = physical sector
    print("\nDiagonalizing Δ_1 on physical subspace ...")
    U, S, VT = np.linalg.svd(GC, full_matrices=True)
    rK = np.sum(S > 1e-10)
    Q_gc   = U[:, :rK]      # gauge⊕toron
    Q_phys = U[:, rK:]      # orthogonal complement

    print("dim(physical subspace)             =", Q_phys.shape[1],
          f"= {n_theta - rK}")

    Delta_phys = Q_phys.T @ Delta @ Q_phys
    evals_phys, _ = np.linalg.eigh(Delta_phys)
    evals_phys_sorted = np.sort(evals_phys)

    print("\nLowest 10 eigenvalues in physical sector (Δ_1):")
    for i in range(min(10, len(evals_phys_sorted))):
        print(f"  λ_phys[{i}] = {evals_phys_sorted[i]:.6e}")

    print("\nMorale:")
    print("  • ker(Δ_1) has dimension 152.")
    print("  • rank(gauge⊕toron) = 152, and Δ_1 annihilates that subspace.")
    print("  • The first eigenvalue in the orthogonal complement is > 0")
    print("    (here ≈ 4), i.e. a genuine 'massive' physical mode.")
    print("So the discrete 1-form Laplacian reproduces the same gauge⊕toron kernel\n"
          "you saw with the Wilson Hessian — two independent constructions agreeing.")

if __name__ == "__main__":
    main()









Building Δ_1 = d^T d for L=2, n_color=8
Total link DOFs n_theta = 512
Symmetric check: True

--- Global spectrum summary (Δ_1) ---
Smallest 10 eigenvalues:
  λ[0] = -8.796669e-15
  λ[1] = -8.104055e-15
  λ[2] = -7.988120e-15
  λ[3] = -7.257829e-15
  λ[4] = -6.209907e-15
  λ[5] = -5.991500e-15
  λ[6] = -5.754126e-15
  λ[7] = -5.706556e-15
  λ[8] = -5.041570e-15
  λ[9] = -4.768014e-15
Largest eigenvalue: λ_max = 1.600000e+01

Number of |λ| < 1e-08 modes in Δ_1: 152

Building explicit gauge-direction matrix G ...
Gauge parameter space dim          = 128
Rank(Im G) in link space           = 120

Building constant-link matrix C (torons before mod gauge) ...
Constant-link direction count      = 32 (4 dirs × 8 colors)
Rank(span of constant-link cols)   = 32

Rank(Im G ⊕ Const)                 = 152
Intersection dim (pure-gauge const)= 0
Toron dim (const links mod gauge)  = 32

Max ||Δ_1 * gauge|| over columns   = 0.000e+00
Max ||Δ_1 * const|| over columns   = 0.000e+00

Total dim(gauge ⊕ toron) from GC   = 152
Compare with # of zero modes       = 152

Diagonalizing Δ_1 on physical subspace ...
dim(physical subspace)             = 360 = 360

Lowest 10 eigenvalues in physical sector (Δ_1):
  λ_phys[0] = 4.000000e+00
  λ_phys[1] = 4.000000e+00
  λ_phys[2] = 4.000000e+00
  λ_phys[3] = 4.000000e+00
  λ_phys[4] = 4.000000e+00
  λ_phys[5] = 4.000000e+00
  λ_phys[6] = 4.000000e+00
  λ_phys[7] = 4.000000e+00
  λ_phys[8] = 4.000000e+00
  λ_phys[9] = 4.000000e+00

Morale:
  • ker(Δ_1) has dimension 152.
  • rank(gauge⊕toron) = 152, and Δ_1 annihilates that subspace.
  • The first eigenvalue in the orthogonal complement is > 0
    (here ≈ 4), i.e. a genuine 'massive' physical mode.
So the discrete 1-form Laplacian reproduces the same gauge⊕toron kernel
you saw with the Wilson Hessian — two independent constructions agreeing.
```
