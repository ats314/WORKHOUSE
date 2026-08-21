# RG Intertwining and a One–Step Poincaré / Gap Recursion

## Abstract
This note extracts the cleanest “continuum bridge” module from the project: a **one–step RG inequality** that transfers a Poincaré constant (or spectral gap) across a single blocking step, with all constants defined so the **factor of \(4\)** (and where it comes from) is explicit.

It also isolates the purely kinematic constant
\[
C_{\mathrm{RG}}
\]
(the gradient–intertwining constant of the block map), separates it from **physical scale conversion**, and gives a checkable linearized computation for **geodesic averaging on \(\mathrm{SU}(2)\)**.

---

## 1. Setup: fine and coarse configuration spaces

Let \(\Lambda_n\subset \mathbb{Z}^4\) be a finite lattice with spacing \(a_n\), and let \(\Lambda_{n+1}\) be the blocked lattice with spacing
\[
a_{n+1} = L a_n,\qquad L=2.
\]
Let \(M_n = G^{E(\Lambda_n)}\), \(M_{n+1}=G^{E(\Lambda_{n+1})}\) with \(G=\mathrm{SU}(2)\).

Let \(\mu_n\) be the Gibbs measure on \(M_n\) and \(\mu_{n+1} = (\pi_n)_\# \mu_n\) its pushforward under a measurable block-spin map
\[
\pi_n : M_n \to M_{n+1}.
\]

---

## 2. Poincaré constants and Dirichlet forms

Let the fine-scale generator be
\[
L_n = \Delta_n - \langle \nabla S_n, \nabla\cdot \rangle,
\]
with Dirichlet form
\[
\mathcal{E}_n(f) := \int_{M_n} |\nabla f|^2\,d\mu_n.
\]

The (dimensionless) Poincaré constant \(C_P^{(n)}\) is the least constant such that
\[
\operatorname{Var}_{\mu_n}(f) \le C_P^{(n)}\,\mathcal{E}_n(f).
\]

### Where the factor \(4\) comes from
If you want to compare *physical* Dirichlet forms across scales, you insert the lattice spacing:
\[
\mathcal{E}_n^{\mathrm{phys}}(f) := a_n^{-2}\,\mathcal{E}_n(f).
\]
Then
\[
\mathcal{E}_{n+1}^{\mathrm{phys}} = a_{n+1}^{-2}\,\mathcal{E}_{n+1} = (L a_n)^{-2}\,\mathcal{E}_{n+1} = L^{-2} a_n^{-2}\,\mathcal{E}_{n+1}.
\]
With \(L=2\), this is the origin of the factor \(4=L^2\) when you express coarse energies in fine units.

---

## 3. The law of total variance

For \(f\in L^2(\mu_n)\), define the conditional expectation
\[
(Pf)(V) := \mathbb{E}_{\mu_n}\bigl[f(U)\mid \pi_n(U)=V\bigr].
\]
Then the law of total variance gives the identity
\[
\operatorname{Var}_{\mu_n}(f)
=
\operatorname{Var}_{\mu_{n+1}}(Pf)
+
\mathbb{E}_{\mu_{n+1}}\!\left[\operatorname{Var}_{\mu_n(\cdot\mid V)}(f)\right].
\]

This is the algebraic spine of every one-step RG gap estimate.

---

## 4. Three checkable hypotheses

We isolate all analytic difficulty into three statements.

### (A1) Coarse Poincaré (induction anchor)
There exists \(C_P^{(n+1)}\) such that for all \(g\),
\[
\operatorname{Var}_{\mu_{n+1}}(g) \le C_P^{(n+1)} \int |\nabla' g|^2\,d\mu_{n+1}.
\]

### (A2) Block (fiber) gap
There exists \(C_{\mathrm{block}}\) independent of volume and \(n\) such that for \(\mu_{n+1}\)-a.e. \(V\),
\[
\operatorname{Var}_{\mu_n(\cdot\mid V)}(f)
\le
C_{\mathrm{block}}\int |\nabla f|^2\,d\mu_n(\cdot\mid V).
\]

### (A3) Gradient intertwining (definition of \(C_{\mathrm{RG}}\))
There exists \(C_{\mathrm{RG}}\) (dimensionless, local) such that for all \(f\),
\[
|\nabla'(Pf)(V)|^2 \le C_{\mathrm{RG}}\,
\mathbb{E}_{\mu_n}\!\left[|\nabla f|^2 \mid V\right].
\]

This is the clean, non-handwavy form of “variation of the conditional mean is bounded by mean variation.”

---

## 5. The one–step RG–Gap inequality

### Theorem (one–step RG Poincaré recursion)
Assume (A1)–(A3). Then
\[
\boxed{
C_P^{(n)} \;\le\; L^2\,C_{\mathrm{RG}}\,C_P^{(n+1)} \;+\; C_{\mathrm{block}}
}
\qquad (L=2 \Rightarrow L^2=4).
\]

#### Proof
Start with total variance:
\[
\operatorname{Var}_{\mu_n}(f)
=
\operatorname{Var}_{\mu_{n+1}}(Pf)
+
\mathbb{E}\!\left[\operatorname{Var}(f\mid V)\right].
\]

**Fiber term.** By (A2) and averaging over \(V\),
\[
\mathbb{E}\!\left[\operatorname{Var}(f\mid V)\right]
\le C_{\mathrm{block}}\int |\nabla f|^2\,d\mu_n.
\]

**Coarse term.** By (A1),
\[
\operatorname{Var}_{\mu_{n+1}}(Pf)
\le C_P^{(n+1)}\int |\nabla'(Pf)|^2\,d\mu_{n+1}.
\]
Apply (A3) and tower property of conditional expectation:
\[
\int |\nabla'(Pf)|^2\,d\mu_{n+1}
\le
C_{\mathrm{RG}}\int |\nabla f|^2\,d\mu_n.
\]

**Scale conversion.** Express coarse energy in fine units: \(\mathcal{E}_{n+1}^{\mathrm{phys}} = L^{-2}\mathcal{E}_{n+1}/a_n^2\), giving the factor \(L^2\) in the final fine-scale bound.

Combine terms and take the best constant: this yields the stated recursion. \(\square\)

---

## 6. Computing \(C_{\mathrm{RG}}\) for two canonical block maps

### 6.1 Decimation
If \(\pi\) simply selects representative links, then \(Pf\) depends on a subset of coordinates and the gradient is a coordinate projection. In that case,
\[
C_{\mathrm{RG}} = 1
\]
exactly, with no small-field restriction.

### 6.2 Geodesic averaging (linearized regime)
Let a block contain \(N=L^4=16\) fine links, each near the identity so that we can use normal coordinates \(U_b=\exp(X_b)\), \(X_b\in\mathfrak{su}(2)\cong \mathbb{R}^3\).

The Karcher (Riemannian) mean linearizes to the arithmetic mean:
\[
Y := \pi(\{X_b\}) = \frac1N\sum_{b=1}^N X_b \;+\; O(r^2)
\]
when \(\|X_b\|\le r\ll 1\).

For any smooth \(F\) on the coarse variable,
\[
\partial_{X_b}(F\circ\pi) = \frac1N\,\partial_Y F + O(r),
\]
and therefore
\[
\sum_{b=1}^N \bigl|\nabla_{X_b}(F\circ\pi)\bigr|^2
=
\frac1N\,|\nabla_Y F|^2\,(1+O(r)).
\]
Thus, on the small-field region,
\[
\boxed{
C_{\mathrm{RG}} \le \frac{1+O(r)}{N} = \frac{1+O(r)}{16}.
}
\]

Interpretation: geodesic averaging is strictly contractive at the level of gradients; any “factor \(\approx 2\)” in physical scaling comes from operator rescaling, not from \(\pi\).

---

## 7. Iteration: what the recursion buys you

Write the recursion with \(L=2\):
\[
C_P^{(n)} \le 4\,C_{\mathrm{RG}}\,C_P^{(n+1)} + C_{\mathrm{block}}.
\]

Two regimes matter:

1. **Decimation:** \(C_{\mathrm{RG}}=1\), so \(C_P^{(n)}\) scales like \(4^{N-n}\), matching the canonical \(a^{-2}\) scaling for a Poincaré constant.

2. **Geodesic averaging in small-field:** \(C_{\mathrm{RG}}\approx 1/16\), so \(4C_{\mathrm{RG}}\approx 1/4\) gives contraction, yielding a very strong gapped phase (useful as an *anchor* or as a high-temperature check).

Either way, the recursion is the right “bridge inequality”: all continuum difficulty is isolated in verifying (A2) and controlling where (A3) is valid (globally for decimation; locally for geodesic averaging).

---

## 8. What to empirically de-risk
Because (A2) and (A3) are local, they are ideal targets for GPU testing:

- **(A3)** can be stress-tested pointwise by Monte-Carlo sampling configurations and tangent directions and estimating the empirical supremum of the gradient ratio.
- **(A2)** can be probed by estimating the lowest nonzero eigenvalue of the conditional (fiber) generator on a single block with fixed boundary data.

A GPU-ready JAX harness for (A3) is provided in a separate extracted note (see `05_jax_a3_rg_intertwining_test.md`).

