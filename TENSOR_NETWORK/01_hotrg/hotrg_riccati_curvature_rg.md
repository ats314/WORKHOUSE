# HOTRG curvature distortion and Riccati curvature restoration: a finite-dimensional RG prototype

This note packages a very concrete “curvature RG” toy pipeline:

1. Linearize a single HOTRG merge step around an identity tensor to obtain a Jacobian \(J\).
2. Push a (physical) Hessian forward by \(H \mapsto J H J^\top\) (a change-of-variables / coarse-graining proxy).
3. Apply a Riccati-type spectral contraction map that damps large curvature modes.

The point is not that this is the full Yang–Mills RG; it’s that the *mechanism* is explicit and numerically testable end-to-end with finite-dimensional linear algebra.

---

## HOTRG linearization (Jacobian)

A Jacobian \(J\) is computed by finite-differencing the HOTRG merge map about a trivial tensor \(T=\mathbf{1}\):

```python
import jax.numpy as jnp
import numpy as np

def hotrg_merge_vertical(T1, T2, chi):
    D = T1.shape[0]
    M = jnp.tensordot(T1, T2, axes=((1,), (1,)))      # merge over one index
    l1,r1,d1,l2,r2,d2 = M.shape
    Mmat = M.reshape(l1*l2, r1*r2*d1*d2)

    U,S,Vh = jnp.linalg.svd(Mmat, full_matrices=False)
    Uc = U[:, :chi]
    Sc = S[:chi]
    Vc = Vh[:chi, :]

    T = (Uc @ jnp.diag(jnp.sqrt(Sc))).reshape(l1, l2, chi)
    N = (jnp.diag(jnp.sqrt(Sc)) @ Vc).reshape(chi, r1, r2, d1, d2)

    out = jnp.einsum("a b c, c d e f g -> a c d e", T, N)
    return out

def hotrg_jacobian_tensor(D=4, chi=4):
    T  = jnp.ones((D,D,D,D), dtype=jnp.float64)
    T0 = hotrg_merge_vertical(T, T, chi).reshape(-1)

    dim_old = D**4
    dim_new = T0.size

    J = np.zeros((dim_new, dim_old))
    eye = np.eye(dim_old)
    eps = 1e-6

    for i in range(dim_old):
        Tpert = (T.reshape(-1) + eps*eye[i]).reshape(D,D,D,D)
        T1 = hotrg_merge_vertical(Tpert, Tpert, chi).reshape(-1)
        J[:, i] = (np.array(T1) - np.array(T0))/eps

    return J.astype(float)
```

---

## Riccati spectral contraction

The Riccati step is applied eigenvalue-wise:
\begin{equation}
\lambda \mapsto \frac{\lambda}{1+\eta\lambda},
\end{equation}
implemented as:

```python
def riccati_step(H, eta=0.1):
    w, v = np.linalg.eigh(H)
    w_new = w/(1 + eta*w)
    Hn = (v * w_new) @ v.T
    return 0.5*(Hn + Hn.T)
```

---

## Observed curvature behavior (key output)

Two “headline” behaviors were printed in the project logs:

### Single coarse Hessian + repeated Riccati steps

Starting from a coarse Hessian \(H_{\mathrm{coarse}}\) obtained from a HOTRG pushforward, the spectrum diagnostics were:

- Before Riccati: \(\lambda_{\min}\approx -6\times 10^{-11}\), \(\lambda_{\max}\approx 2.654\times 10^{5}\).
- After Riccati step 1: \(\lambda_{\max}\approx 10.0\).
- Then: \(10 \to 5 \to 3.333\to 2.5\to 2.0 \to 1.666\to 1.428\) as Riccati iterates continue.

This is the exact scalar Riccati trajectory \(\lambda_{t+1}=\lambda_t/(1+\eta\lambda_t)\) acting on a dominant large eigenvalue.

### Multi-step “RG + Riccati” loop

A loop repeats:

\begin{equation}
H_{k}^{\text{RG}} = J_k\,H_{k-1}\,J_k^\top,
\qquad
H_k = \Phi_{\text{Riccati}}(H_k^{\text{RG}}).
\end{equation}

The printed diagnostics show at multiple RG layers:

- Before Riccati: \(\lambda_{\max}\sim 10^5\) (order \(10^{5}\)–\(10^{5.5}\)).
- After Riccati: \(\lambda_{\max}\approx 10\) consistently across layers.
- \(\lambda_{\min}\) stays near numerical zero.

---

## Why this is a serious “theory seed”

- It’s an explicit, finite-dimensional **counterterm mechanism**: a coarse-graining map \(J\) that amplifies curvature is followed by a universal spectral damper \(\Phi\) that restores a bounded curvature envelope.
- If the same qualitative behavior survives when (i) \(J\) is built from nontrivial tensors, (ii) the “physical Hessian” is defined more faithfully, and (iii) the background configuration is moved off-identity, you essentially have a computational laboratory for a curvature-controlled RG scheme.
