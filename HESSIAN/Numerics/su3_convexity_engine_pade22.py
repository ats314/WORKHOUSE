#!/usr/bin/env python3
# SU(3) convexity scan (HVP + Lanczos), using Padé(2,2) for exp(A).
# Intended for GPU JAX runs (A100-friendly).
#
# NOTE: This is a reconstruction of the scan engine described in the project logs.
# It should be very close to the working code, but always sanity-check at small L.

import time
import numpy as np
import jax
import jax.numpy as jnp


def su3_generators_antihermitian():
    \"\"\"Return 8 anti-Hermitian generators T_a = i * lambda_a / 2 (Gell-Mann basis).\"\"\"
    # Gell-Mann matrices (Hermitian)
    lam = []
    lam.append(jnp.array([[0,1,0],[1,0,0],[0,0,0]], dtype=jnp.complex64))
    lam.append(jnp.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=jnp.complex64))
    lam.append(jnp.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=jnp.complex64))
    lam.append(jnp.array([[0,0,1],[0,0,0],[1,0,0]], dtype=jnp.complex64))
    lam.append(jnp.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=jnp.complex64))
    lam.append(jnp.array([[0,0,0],[0,0,1],[0,1,0]], dtype=jnp.complex64))
    lam.append(jnp.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=jnp.complex64))
    lam.append((1/jnp.sqrt(3))*jnp.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=jnp.complex64))
    lam = jnp.stack(lam, axis=0)  # (8,3,3)
    T = 1j * lam / 2.0  # anti-Hermitian
    return T


T_SU3 = su3_generators_antihermitian()


def pade22_expm(A):
    \"\"\"Padé(2,2) approximation to matrix exponential.
    exp(A) ≈ (I + A/2 + A^2/12) @ inv(I - A/2 + A^2/12)
    Stable for ||A|| small (used as local chart approximation).
    \"\"\"
    I = jnp.eye(3, dtype=A.dtype)
    A2 = A @ A
    N = I + 0.5 * A + (1.0/12.0) * A2
    D = I - 0.5 * A + (1.0/12.0) * A2
    return N @ jnp.linalg.inv(D)


def theta_to_links(theta, L):
    \"\"\"Map flat real vector theta -> link matrices U(x,mu) ∈ SU(3) (approx).
    theta has shape (V*4*8,), where V=L^4.
    \"\"\"
    V = L**4
    coeff = theta.reshape((V, 4, 8))  # real
    # Build A matrices: A = sum_a coeff_a * T_a
    A = jnp.einsum('vma,aij->v mij', coeff, T_SU3)  # (V,4,3,3)
    # Exponentiate each link
    U = jax.vmap(jax.vmap(pade22_expm))(A)  # v over V then mu
    return U


def build_neighbor_indices(L):
    \"\"\"Return neighbor index arrays nbr[mu][x] = x shifted by +mu with periodic BC on L^4.\"\"\"
    # Flatten site index: x = (((t*L + z)*L + y)*L + x)
    coords = np.indices((L, L, L, L), dtype=np.int32)  # (4,L,L,L,L)
    coords = coords.reshape((4, -1)).T  # (V,4) order: (x,y,z,t) from indices; adjust below
    # np.indices returns axes in order, so coords[:,0]=x0, coords[:,1]=x1, ...
    # We'll interpret dims as (x,y,z,t) in that order.
    def idx(c):
        x,y,z,t = c
        return (((t*L + z)*L + y)*L + x)
    V = L**4
    nbr = []
    for mu in range(4):
        c_shift = coords.copy()
        c_shift[:,mu] = (c_shift[:,mu] + 1) % L
        nbr_mu = np.array([idx(c) for c in c_shift], dtype=np.int32)
        nbr.append(nbr_mu)
    nbr = np.stack(nbr, axis=0)  # (4,V)
    return jnp.array(nbr)


def wilson_action_from_links(U, nbr, L):
    \"\"\"Wilson plaquette action sum_p (1 - (1/3) Re Tr U_p).
    U shape: (V,4,3,3). nbr shape: (4,V).
    \"\"\"
    V = L**4
    action = 0.0
    for mu in range(4):
        for nu in range(mu+1, 4):
            U_mu = U[:, mu]
            U_nu = U[:, nu]
            U_nu_shift = U[nbr[mu], nu]
            U_mu_shift = U[nbr[nu], mu]
            # plaquette: U_mu(x) U_nu(x+mu) U_mu(x+nu)† U_nu(x)†
            P = U_mu @ U_nu_shift @ jnp.conjugate(jnp.swapaxes(U_mu_shift, -1, -2)) @ jnp.conjugate(jnp.swapaxes(U_nu, -1, -2))
            trP = jnp.trace(P, axis1=-2, axis2=-1)
            action = action + jnp.sum(1.0 - (1.0/3.0) * jnp.real(trP))
    return jnp.real(action)


def make_action(L, beta, c0=0.125):
    \"\"\"Return action(theta) = Haar_quadratic + beta * Wilson.\"\"\"
    nbr = build_neighbor_indices(L)

    def action(theta):
        # Haar quadratic surrogate on algebra coefficients (local chart core)
        S_haar = c0 * jnp.sum(theta**2)
        U = theta_to_links(theta, L)
        S_w = wilson_action_from_links(U, nbr, L)
        return S_haar + beta * S_w

    return action


def hvp_fn(action_fn, theta):
    g = jax.grad(action_fn)
    def hvp(v):
        return jax.jvp(g, (theta,), (v,))[1]
    return hvp


def lanczos_min_eig(hvp, dim, key, k=20):
    \"\"\"Estimate min eigenvalue of symmetric operator via k-step Lanczos.\"\"\"
    v = jax.random.normal(key, (dim,), dtype=jnp.float32)
    v = v / (jnp.linalg.norm(v) + 1e-12)

    alphas = []
    betas = []

    w_prev = jnp.zeros_like(v)
    beta_prev = 0.0

    for i in range(k):
        w = hvp(v)
        if i > 0:
            w = w - beta_prev * w_prev
        alpha = jnp.vdot(v, w).real
        w = w - alpha * v
        beta = jnp.linalg.norm(w)
        alphas.append(float(alpha))
        betas.append(float(beta))
        w_prev = v
        v = w / (beta + 1e-12)
        beta_prev = beta

    # Build tridiagonal matrix and compute eigenvalues on CPU
    T = np.zeros((k, k), dtype=np.float64)
    for i in range(k):
        T[i,i] = alphas[i]
        if i < k-1:
            T[i,i+1] = betas[i]
            T[i+1,i] = betas[i]
    evals = np.linalg.eigvalsh(T)
    return float(evals[0])


def run_scan(L=4, beta_vals=None, scales=(0.05,0.10,0.15), n_samples=3, k_lanczos=20, seed=0, c0=0.125):
    if beta_vals is None:
        beta_vals = np.linspace(0.4, 3.0, 8)

    key = jax.random.PRNGKey(seed)
    dim = (L**4) * 4 * 8

    print(f\"=== SU(3) convexity scan: L={L}, dim={dim}, c0={c0} ===\")
    t0 = time.time()

    for beta in beta_vals:
        action = make_action(L, float(beta), c0=c0)
        action_jit = jax.jit(action)  # compile once per beta
        # Warm-up compile
        _ = action_jit(jnp.zeros((dim,), dtype=jnp.float32)).block_until_ready()

        for scale in scales:
            lam_min = +1e9
            for s in range(n_samples):
                key, ks, kl = jax.random.split(key, 3)
                theta = scale * jax.random.normal(ks, (dim,), dtype=jnp.float32)
                hvp = hvp_fn(action_jit, theta)
                # one hvp warm-up
                _ = hvp(jnp.ones((dim,), dtype=jnp.float32)).block_until_ready()
                lam = lanczos_min_eig(hvp, dim, kl, k=k_lanczos)
                lam_min = min(lam_min, lam)
            print(f\"beta={beta:0.2f} scale={scale:0.3f} lam={lam_min:+0.6f}\")
    print(f\"Total Time: {time.time()-t0:.2f}s\")


if __name__ == \"__main__\":
    run_scan(L=4)
