# Making the HOTRG → curvature map honest (physical-subspace, finite-dimensional)

This note replaces the current “embedding/resizing” surrogates with a principled statement:  
the object that must exist is a **linearization map** from *physical fine variables* to the *tensor degrees of freedom* acted on by HOTRG.

The guiding requirement is:

\[
\text{(correct tangent pushforward)} \qquad \delta T \;=\; L\,\delta x \quad\text{at the chosen background,}
\]
where \(x\) are *physical* coordinates (gauge-projected), \(T\) is the local tensor (flattened), and \(L\) is the Jacobian.

Once \(L\) is fixed, the HOTRG Jacobian \(J\) can be used without any proxy:
\[
\delta T' \;=\; J\,\delta T \;=\; (J L)\,\delta x .
\]

The rest of this note is finite-dimensional matrix algebra.

---

## Physical subspace: projector and coordinates

Let \(H\in\mathbb{R}^{n\times n}\) be a symmetric Hessian in fine variables \(x\in\mathbb{R}^n\).
Let \(G\in\mathbb{R}^{n\times g}\) have columns spanning the gauge directions (infinitesimal gauge transformations),
and assume \(G\) has full column rank.

Define the orthogonal projector onto the physical tangent space:
\[
P \;=\; I - G(G^\top G)^{-1}G^\top .
\]
Then \(P^2=P=P^\top\) and \(Px\) removes gauge directions.

A coordinate system for the physical subspace can be built from any orthonormal basis \(Q\in\mathbb{R}^{n\times r}\) of \(\operatorname{im}(P)\):
\[
Q^\top Q = I_r,\qquad QQ^\top = P.
\]
Physical coordinates are \(y = Q^\top x\), and the physical Hessian is
\[
H_{\rm phys} \;=\; Q^\top H Q \;\in\;\mathbb{R}^{r\times r}.
\]

---

## Honest HOTRG pushforward: the missing Jacobian \(L\)

Let \(T(x)\in\mathbb{R}^{D^4}\) be the local tensor built from fine variables \(x\)
(using whatever tensor-network representation you are actually coarse-graining).

Let \(x_\star\) be the background configuration (often the “identity / uniform tensor” point).

Define
\[
L \;:=\; \left.\frac{\partial\, \mathrm{vec}(T(x))}{\partial x}\right|_{x=x_\star}
\;\in\;\mathbb{R}^{D^4\times n}.
\]
Then the physical-to-tensor linearization is \(L_{\rm phys} := LQ \in \mathbb{R}^{D^4\times r}\).

With the HOTRG Jacobian \(J\in\mathbb{R}^{\chi^4\times D^4}\),
the total tangent map is
\[
C \;:=\; J L_{\rm phys} \;\in\;\mathbb{R}^{\chi^4\times r}.
\]

At this point, **there is no need for any embedding/resizing proxy**.
The dimensions match by construction.

---

## Two consistent coarse “Hessians” (stiffness vs covariance)

There are two mathematically consistent ways to define a coarse quadratic form, depending on whether you want
to push forward **stiffness** (Hessian) or **covariance** (inverse Hessian).

### A. Stiffness pushforward (what the current pipeline computes)

If you insist on pushing forward the quadratic form \( \frac12 y^\top H_{\rm phys} y\) through the tangent map \(C\),
the induced quadratic form in coarse tangent variables \(u\in\mathbb{R}^{\chi^4}\) is
\[
H_{\rm stiff}^{\rm coarse} \;=\; C\,H_{\rm phys}\,C^\top .
\]

This is algebraically valid, but **it is not the Gaussian integration rule**.

### B. Gaussian-consistent coarse action (recommended)

If the fine measure is Gaussian \( \propto \exp(-\tfrac12 y^\top H_{\rm phys} y)\),
then its covariance is \(\Sigma_{\rm phys} = H_{\rm phys}^{-1}\) (or Moore–Penrose pseudoinverse if needed).

The induced covariance in coarse variables \(u = C y\) is
\[
\Sigma_{\rm coarse} \;=\; C\,\Sigma_{\rm phys}\,C^\top .
\]
The Gaussian-consistent effective stiffness is then
\[
H_{\rm gauss}^{\rm coarse} \;=\; \Sigma_{\rm coarse}^{+}.
\]

This definition is exactly the “pushforward of the measure” and avoids spurious curvature blow-ups caused by
pushing Hessians instead of covariances.

---

## A practical algorithm that eliminates proxies immediately

Even before a full \(T(x)\) is implemented, you can remove the *arbitrary* resizing step by working only on physical tangent coordinates.

1. Build \(Q\) spanning \(\operatorname{im}(P)\), compute \(H_{\rm phys} = Q^\top H Q\).
2. Implement \(L_{\rm phys} = ( \partial \mathrm{vec}(T(x))/\partial x )|_{x_\star} \, Q\).
3. Compute \(C = J L_{\rm phys}\).
4. Choose either
   - \(H_{\rm stiff}^{\rm coarse} = C H_{\rm phys} C^\top\), or
   - \(H_{\rm gauss}^{\rm coarse} = (C H_{\rm phys}^{+} C^\top)^{+}\) (recommended).
5. Only then apply the Riccati envelope \(\Phi_\eta\) on the *coarse physical subspace*.

---

## Minimal code skeleton (drop-in replacement point)

```python
import numpy as np

def projector_from_gauge(G: np.ndarray) -> np.ndarray:
    # P = I - G (G^T G)^{-1} G^T
    GTG = G.T @ G
    return np.eye(G.shape[0]) - G @ np.linalg.inv(GTG) @ G.T

def orthonormal_basis_of_image(P: np.ndarray, tol=1e-10) -> np.ndarray:
    # Q columns span im(P), Q^T Q = I
    evals, evecs = np.linalg.eigh(P)
    keep = evals > tol
    Q = evecs[:, keep]
    # Orthonormal already, since P is symmetric.
    return Q

def coarse_hessian_gaussian(H_phys: np.ndarray, C: np.ndarray, tol=1e-12) -> np.ndarray:
    # H_gauss = ( C H_phys^+ C^T )^+
    evals, evecs = np.linalg.eigh(H_phys)
    inv = np.zeros_like(evals)
    inv[evals > tol] = 1.0 / evals[evals > tol]
    H_pinv = (evecs * inv) @ evecs.T
    Sigma = C @ H_pinv @ C.T
    # pseudoinverse of Sigma
    s_eval, s_vec = np.linalg.eigh(Sigma)
    s_inv = np.zeros_like(s_eval)
    s_inv[s_eval > tol] = 1.0 / s_eval[s_eval > tol]
    return (s_vec * s_inv) @ s_vec.T

def pushforward_stiffness(H_phys: np.ndarray, C: np.ndarray) -> np.ndarray:
    return C @ H_phys @ C.T
```

Where the *only physics-dependent object* is \(L_{\rm phys}\), i.e. the Jacobian of tensor construction at \(x_\star\).

---

## What remains “physics”, not linear algebra

The only thing you must specify to make the map honest is:

\[
T(x)\quad\text{and hence}\quad L=\partial \mathrm{vec}(T(x))/\partial x.
\]

Everything else is forced.

A good rule of thumb:  
if you can compute your fine Hessian \(H\) by autodiff, you can compute \(L\) by autodiff too — it’s the same class of object,
just for the tensor construction function.
