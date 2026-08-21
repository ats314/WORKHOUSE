# SU(2) lattice Wilson curvature and SU(2)-covariant blocking: explicit Hessian spectra

This note extracts the SU(2) Wilson-action Hessian computations at the identity configuration, plus an SU(2)-covariant blocking map (product → projection) and the resulting coarse-lattice Hessian spectrum.

---

## Fine lattice Wilson action and Hessian at the identity

The Wilson plaquette action on a periodic \(L^4\) lattice (here \(L=2\)) is implemented as a sum over oriented plaquettes,
\begin{equation}
S_W(U) = \beta \sum_{x}\sum_{\mu<\nu}\left(1-\frac12\Re\operatorname{tr}U_{\mu\nu}(x)\right).
\end{equation}

A JAX implementation builds link matrices via an exponential map \(U_\mu(x)=\exp(i\,a_\mu(x)\cdot \sigma)\) and differentiates twice to obtain the Hessian at the identity (all \(a=0\)).

The printed fine-lattice eigenvalues at \(\beta=2.2\) are:
\begin{align}
\text{Smallest eigenvalues (10 shown)} &:\; 3.3,3.3,\dots,3.3,\\
\text{Largest eigenvalues (10 shown)} &:\; 9.9, 12.1,12.1,\dots,12.1.
\end{align}

---

## SU(2)-covariant block-spin: product then project

A coarse link is constructed by multiplying two fine links and projecting back to \(\mathrm{SU}(2)\) by polar decomposition:
\begin{equation}
U_c \;=\; \Pi_{\mathrm{SU}(2)}(U_1U_2),
\end{equation}
followed by axis-angle extraction \(U_c=\cos\theta\,I+i\sin\theta\,(\mathbf{n}\cdot \sigma)\) and mapping back to a Lie algebra coordinate \(a_c=\theta\,\mathbf{n}\).

This is explicitly coded (including the \(\theta\to 0\) branch):

---

## Coarse lattice action and Hessian

After blocking \(L_{\text{fine}}=2\to L_{\text{coarse}}=1\), the coarse action is computed using the same Wilson plaquette formula, with \(\beta\) rescaled by the 4D volume factor \(\beta\mapsto \beta (L_{\mathrm{fine}}^4/L_{\mathrm{coarse}}^4)\).

The printed coarse-lattice Hessian spectrum is strikingly isotropic:
\begin{align}
\text{Smallest eigenvalues (10 shown)} &:\; 52.8, 52.8, \dots, 52.8,\\
\text{Largest eigenvalues (10 shown)} &:\; 52.8, 52.8, \dots, 52.8.
\end{align}

Since the coarse space has 12 degrees of freedom (4 links \(\times\) 3 algebra components), this printout indicates **all coarse Hessian eigenvalues coincide** at the identity in this setup.

---

## Minimal reproducibility snippet (structure)

```python
# 1) define su2_exp(alpha) and su2_project(M)
# 2) define make_wilson_action(L, beta) returning W(v)
# 3) H(v) = jacfwd(jacrev(W))(v)
# 4) fine: L=2, v0=0, evals_fine = eigvalsh(H_fine(v0))
# 5) block v0 via gauge_covariant_block(v0)
# 6) coarse: L=1, beta_rescaled = beta*(2**4/1**4), evals_coarse = eigvalsh(H_coarse(v0_blocked))
```

---

## What looks “theory-usable” here

- The coarse spectrum collapsing to a single value suggests an emergent **scalar stiffness** at the coarse scale for this particular block map at the identity.
- If this behavior persists (or has controlled deviations) away from the identity and for larger lattices, it is exactly the kind of phenomenon that could support a curvature-based renormalization narrative: coarse dynamics becoming effectively massive and isotropic.
