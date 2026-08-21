# Numerical Evidence Pack and Reproducible Code

## Scope

This document extracts the simulations and numerics in the corpus that support the curvature-flow / mass-gap mechanism, and provides reproducible code sketches.

No numerical claim is treated as a proof; the goal is to identify robust diagnostics.

---

## 1. Curvature flow numerics: viscous HJ model

### 1.1 PDE model used in simulations

The corpus uses the viscous Hamilton–Jacobi equation
\[
\partial_t S = \Delta S - |\nabla S|^2,
\]
motivated by \(S=-\log u\) for the heat equation \(\partial_t u=\Delta u\).

### 1.2 Reported findings (E03)

- Convexity preservation: the minimal Hessian eigenvalue \(\lambda_{\min}(t)\) remains positive in the tested regimes.
- A Riccati-like decay law (in regimes without constant source):
  \[
  \frac{d\lambda}{dt}\approx -\alpha \lambda^2
  \quad\Rightarrow\quad
  \frac{1}{\lambda(t)}=\frac{1}{\lambda(0)}+\alpha t.
  \]

A representative fitted value reported:
\[
\alpha \approx 1.02\times 10^{-3}.
\]

---

## 2. “Curvature phase diagram” (universality band)

The corpus reports that a range of non-quadratic potentials collapse into a narrow \(\alpha\)-band, suggesting that a “Haar-like” term dominates curvature dynamics.

### Reported \(\alpha\)-values across phases (E03)

| Phase | \(\alpha_1\) | \(\alpha_2\) | \(\alpha_3\) | \(\alpha_4\) |
|---|---:|---:|---:|---:|
| Quadratic-only | 0.001002 | — | — | — |
| Haar-only | 0.000788 | — | — | — |
| Haar + YM quartic | 0.000781 | — | — | — |
| Haar + SU(2) adjoint | 0.0007875 | 0.0007933 | 0.0007628 | 0.0007981 |
| Haar + SU(3) mass | 0.0007973 | 0.0007992 | 0.0008004 | 0.0008012 |
| Haar + SU(3) commutator | 0.0007967 | 0.0007977 | 0.0007861 | 0.0008002 |

---

## 3. SU(3) local algebraic convexity test

### Potential tested (E03)

The corpus tests convexity for an \(\mathfrak{su}(3)\)-algebra model
\[
S(A) = \frac{1}{2}m^2 \sum_{a=1}^8 A_a^2
\;+\;
\kappa \sum_{a=1}^8\Bigl(\sum_{b,c} f_{abc}A_bA_c\Bigr)^2,
\qquad A\in\mathbb{R}^8.
\]
Reported outcome (for \(m^2=2\), \(\kappa=1\)): the minimal Hessian eigenvalue at random configurations is numerically equal to \(m^2\) (convex), supporting the claim:

> The nonabelian commutator structure does not by itself destroy global convexity once a quadratic term is present.

---

## 4. SU(2) lattice Hessian (vacuum test) and gauge modes

### 4.1 What a direct computation shows

A direct autodiff Hessian computation of the pure Wilson action at the vacuum typically exhibits near-zero modes (gauge directions).
A stable way to compute the vacuum Hessian uses a Taylor expansion of the link exponential: this avoids autodiff NaNs at \(\theta=0\).

### 4.2 Reproducible JAX code (Colab-ready) for the vacuum Hessian

**Notes for Colab/A100:** do *not* downgrade JAX/JAXLIB; use Colab’s built-in JAX to avoid CUDA plugin mismatches.

```python
import jax
import jax.numpy as jnp
jax.config.update("jax_enable_x64", True)

# Pauli matrices
SIGMA = jnp.stack([
    jnp.array([[0,1],[1,0]], dtype=jnp.complex128),
    jnp.array([[0,-1j],[1j,0]], dtype=jnp.complex128),
    jnp.array([[1,0],[0,-1]], dtype=jnp.complex128),
], axis=0)

def su2_exp_taylor(a):
    # exp(i/2 a·σ) ≈ I + iX - (1/2)X^2, with X=(1/2)a·σ
    X = 0.5 * jnp.tensordot(a, SIGMA, axes=1)
    I = jnp.eye(2, dtype=jnp.complex128)
    return I + 1j*X - 0.5*(X@X)

def plaquette_term(U1,U2,U3,U4):
    Up = U1 @ U2 @ jnp.conjugate(U3.T) @ jnp.conjugate(U4.T)
    return 1.0 - 0.5*jnp.real(jnp.trace(Up))

def wilson_action_flat(x, L=2, beta=2.0):
    links = x.reshape(L,L,L,L,4,3)
    S = 0.0
    for X in range(L):
        for Y in range(L):
            for Z in range(L):
                for T in range(L):
                    for mu in range(4):
                        for nu in range(mu+1,4):
                            xm = [X,Y,Z,T]; xm[mu]=(xm[mu]+1)%L
                            xn = [X,Y,Z,T]; xn[nu]=(xn[nu]+1)%L

                            U1 = su2_exp_taylor(links[X,Y,Z,T,mu])
                            U2 = su2_exp_taylor(links[tuple(xm)][nu])
                            U3 = su2_exp_taylor(links[tuple(xn)][mu])
                            U4 = su2_exp_taylor(links[X,Y,Z,T,nu])
                            S = S + (beta/2.0)*(2.0 - jnp.real(jnp.trace(U1@U2@jnp.conjugate(U3.T)@jnp.conjugate(U4.T))))
    return jnp.asarray(jnp.real(S), dtype=jnp.float64)

def vacuum_hessian_spectrum(L=2, beta=2.0, m2=0.0):
    dof = (L**4)*4*3
    x0 = jnp.zeros((dof,), dtype=jnp.float64)

    def S_eff(x):
        return wilson_action_flat(x,L=L,beta=beta) + 0.5*m2*jnp.dot(x,x)

    H = jax.jacfwd(jax.jacrev(S_eff))(x0)
    H = 0.5*(H+H.T)
    eigs = jnp.linalg.eigvalsh(H)
    return eigs

eigs = vacuum_hessian_spectrum(L=2, beta=2.0, m2=0.0)
print("min eig (pure Wilson):", float(eigs[0]))
print("max eig (pure Wilson):", float(eigs[-1]))

eigs_m = vacuum_hessian_spectrum(L=2, beta=2.0, m2=1.0)
print("min eig (+mass term):", float(eigs_m[0]))
```

- With \(m^2=0\) one expects near-zero modes (gauge directions).
- With \(m^2>0\) all modes are lifted by at least \(m^2\).

This gives a controlled way to reproduce “Hessian floors” in gauge-fixed models.

---

## 5. Results explicitly reported in the corpus

The simulation report (E03) claims:

- a positive “Hessian floor” on the \(2^4\) SU(2) lattice at the vacuum, with smallest eigenvalues \(\lambda_{\min}\approx 3.3\) (repeated);
- a narrow \(\alpha\)-band across non-quadratic potentials;
- a q-Racah Doob chain toy model with gap closing near \(q\to 1\) approximately linearly.

Because E02 code fragments in the corpus are incomplete, the code above is supplied as a minimal reproducible scaffold for the lattice Hessian diagnostic.

---

## 6. What these simulations are actually diagnostic for

1. Whether a **local convexity floor** exists (and how it depends on gauge fixing).
2. Whether curvature evolution behaves like a **Riccati law** with stable fitted parameters.
3. Whether nonabelian algebra alone obstructs convexity (the SU(3) test suggests it does not).

All three feed directly into the PBH/Riccati mass-gap pipeline.