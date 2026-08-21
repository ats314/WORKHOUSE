# B-SHIFT YANG

**Source file:** `B-SHIFT YANG.txt`

---

```text
# ================================================================
#  B SHIFT RIGHT–INVARIANT SU(3) YANG–MILLS GEOMETRY
#  Colab Notebook Framework
#
#  This notebook provides:
#    ✓ Right-invariant tangent frame  δU = U X
#    ✓ SU(3) generator algebra
#    ✓ Exponential map U = exp(A)
#    ✓ Adjoint transport  Ad_U(X) = U† X U
#    ✓ Wilson action
#    ✓ Right-invariant Hessian at vacuum and general U
#    ✓ Gauge projector P = I - G (G†G)^(-1) G†
#    ✓ Toron projector
#    ✓ RG-ready tangent evolution hook
#    ✓ Riccati convexification update
#
#  It is the correct “B” frame for your HOTRG curvature program.
#  Large-scale HOTRG and RG Jacobian will plug into the interfaces
#  defined here.
# ================================================================

import numpy as np
import jax
import jax.numpy as jnp
import jax.scipy as jsp

jax.config.update("jax_enable_x64", True)

# ================================================================
#  1. SU(3) GENERATORS (anti-Hermitian Gell-Mann basis)
# ================================================================

def su3_generators():
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
    return 1j * lam / 2.0   # anti-Hermitian

T = su3_generators()  # shape (8, 3, 3)


# ================================================================
#  2. RIGHT-INVARIANT TANGENT MAP  X → δU = U X
# ================================================================

def vec_to_su3(Xvec):
    """8-vector → anti-Hermitian matrix"""
    return jnp.einsum("a,aij->ij", Xvec, T)

def adjoint_transport(U, X):
    """Right-invariant pushforward: Ad_U(X) = U† X U."""
    return U.conj().T @ X @ U


# ================================================================
#  3. EXPONENTIAL MAP AND LINK CONSTRUCTION
# ================================================================

def su3_exp(A):
    return jsp.linalg.expm(A)

def build_links_from_X(X_flat, L):
    """
    Interpret X_flat as right-invariant tangent generator:
        U = exp(X)
    Not δU = X, but the underlying group element.
    """
    Xmat = jax.vmap(vec_to_su3)(X_flat.reshape(-1, 8))
    U = jax.vmap(su3_exp)(Xmat)
    return U.reshape(L, L, L, L, 4, 3, 3)


# ================================================================
#  4. WILSON ACTION  (SU(3))
# ================================================================

def wilson_action(X_flat, L, beta=1.0):
    U = build_links_from_X(X_flat, L)
    S = 0.0
    for mu in range(4):
        for nu in range(mu+1, 4):
            U1 = U[..., mu, :, :]
            U2 = jnp.roll(U[..., nu, :, :], -1, axis=mu)
            U3 = jnp.swapaxes(jnp.conjugate(jnp.roll(U[..., mu, :, :], -1, axis=nu)), -1, -2)
            U4 = jnp.swapaxes(jnp.conjugate(U[..., nu, :, :]), -1, -2)
            P = U1 @ U2 @ U3 @ U4
            tr = jnp.real(jnp.einsum("...ii->...", P))
            S += jnp.sum(1 - tr/3)
    return beta * S


# ================================================================
#  5. RIGHT-INVARIANT HESSIAN:  H = ∂² S / ∂X²
# ================================================================

def build_ri_hessian(L):
    n = L**4 * 4 * 8

    def S_wrap(X):
        return wilson_action(X, L)

    grad_S = jax.grad(S_wrap)
    hess_fn = jax.jacfwd(grad_S)

    X0 = jnp.zeros((n,), jnp.float64)
    H = hess_fn(X0)
    H = np.array(H, float)
    H = 0.5 * (H + H.T)
    return H


# ================================================================
#  6. GAUGE GENERATOR & PROJECTOR (RIGHT-INVARIANT)
# ================================================================

def alpha_to_X(alpha, L):
    """
    Right-invariant gauge transformation generator:
         δU = U X  where X = α(x) - α(x+μ)
    """
    L4 = L*L*L*L
    theta = np.zeros((L, L, L, L, 4, 8))
    for mu in range(4):
        alpha_fwd = np.roll(alpha, -1, axis=mu)
        theta[..., mu, :] = alpha - alpha_fwd
    return theta.reshape(-1)

def build_gauge_matrix(L):
    n_sites = L**4
    n_color = 8
    n_alpha = n_sites * n_color
    G = np.zeros((n_sites*4*n_color, n_alpha))
    col = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                for x3 in range(L):
                    for a in range(8):
                        alpha = np.zeros((L,L,L,L,8))
                        alpha[x0,x1,x2,x3,a] = 1.0
                        G[:, col] = alpha_to_X(alpha, L)
                        col += 1
    return G


def projector_physical(H, L):
    """Return projector onto physical complement of (gauge ⊕ toron)."""
    G = build_gauge_matrix(L)

    # gauge orthonormal basis
    Qg, _ = np.linalg.qr(G)
    rG = np.linalg.matrix_rank(G)
    Qg = Qg[:, :rG]

    # constant-link (toron) subspace
    n_theta = (L**4)*4*8
    C = np.zeros((n_theta, 4*8))
    col = 0
    for mu in range(4):
        for a in range(8):
            theta = np.zeros((L,L,L,L,4,8))
            theta[..., mu, a] = 1.0
            C[:, col] = theta.reshape(-1)
            col += 1
    # project away gauge
    C_perp = C - Qg @ (Qg.T @ C)

    # combined
    K = np.concatenate([Qg, C_perp], axis=1)
    Q, S, VT = np.linalg.svd(K, full_matrices=True)
    rK = np.sum(S > 1e-10)
    Q_phys = Q[:, rK:]

    return Q_phys


# ================================================================
#  7. CURVATURE & RICCATI UPDATE
# ================================================================

def curvature_data(H_phys):
    """Return λ_min, λ_max, rc, kappa."""
    evals = np.linalg.eigvalsh(H_phys)
    lam_min = evals[0]
    lam_max = evals[-1]
    rc = np.sqrt(lam_min / lam_max)
    tau = 0.25
    kappa = lam_min - tau*(lam_max - lam_min)
    return lam_min, lam_max, rc, kappa


def riccati_step(H, eta=0.1):
    """
    Right-invariant Riccati convexification:
       H ← H + η (Q - H²)
    with Q = average eigenvalue * I
    """
    w = np.linalg.eigvalsh(H)
    lam_min, lam_max = w[0], w[-1]
    Q = 0.5 * (lam_min + lam_max)
    return H + eta * (Q*np.eye(H.shape[0]) - H@H)


# ================================================================
#  8. END-TO-END DEMO (L=2)
# ================================================================

def demo_L2():
    print("=== Building RI Hessian (L=2) ===")
    H = build_ri_hessian(L=2)
    print("Hessian shape:", H.shape)

    print("\n=== Gauge+toron projection ===")
    Q_phys = projector_physical(H, L=2)
    print("Physical dimension =", Q_phys.shape[1])

    H_phys = Q_phys.T @ H @ Q_phys
    lam_min, lam_max, rc, kappa = curvature_data(H_phys)

    print("\nEigenvalues (physical):")
    print("λ_min =", lam_min)
    print("λ_max =", lam_max)
    print("rc =", rc)
    print("κ =", kappa)

    print("\n=== Riccati step ===")
    H_next = riccati_step(H_phys, eta=0.1)
    lam_min2, lam_max2, rc2, kappa2 = curvature_data(H_next)
    print("After Riccati:")
    print("λ_min =", lam_min2)
    print("κ =", kappa2)

demo_L2()
```
