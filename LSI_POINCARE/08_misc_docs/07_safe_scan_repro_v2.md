# Reproducing the SAFE eigenvalue scan (what we can lock down today)

*Generated 2025-12-29.*

This note is about **reproducibility**, not ideology.

The project draft reports a SAFE-region eigenvalue scan for the *physical* projected Hessian
and gives a representative radius table, including numbers like:

- Haar-only in physical subspace: $\lambda_{\min}^{\mathrm{Haar}}(0.00)=0.291$,
- physical: $\lambda_{\min}^{\mathrm{phys}}(0.05)=0.249$,
- global scanned minimum $\approx 0.248$.

(Those targets live in the project writeup; this note focuses on the code-level definition and what is currently reproduced.)

---

## 1. What is **fully reproduced** here

### 1.1 Single-link Haar Hessian (no gauge projector, no cluster)

We reproduce the **Haar Jacobian potential** near the identity using the standard formula
\[
V_{\mathrm{Haar}}(x)=-\log\det\Bigl(\phi_1(\operatorname{ad}_X)\Bigr),\qquad
X=\sum_a x_a T_a,\quad \phi_1(A)=\frac{e^A-I}{A}.
\]

The script `safe_scan_tracked_v2.py` computes:

1. structure constants $f_{abc}$ for an orthonormal basis of $\mathfrak{su}(3)$,
2. the adjoint matrix $A(x)$ for $\operatorname{ad}_X$,
3. $V_{\mathrm{Haar}}(x)$ from $\log\det\phi_1(A)$,
4. the Hessian of $V_{\mathrm{Haar}}$ by symmetric finite differences,
5. the minimum eigenvalue over random directions on a radial grid.

#### Normalization knob (`--metric_scale`)

There is a genuine normalization ambiguity: your coordinate vector $x$ depends on the chosen inner product
and how you identify “radius”.

In the code, `--metric_scale` implements the map
\[
x\mapsto X(x)=\sum_a (\texttt{metric\_scale}\cdot x_a)\,T_a,
\]
*inside* the Haar potential. This rescales the Hessian at the origin by approximately $(\texttt{metric\_scale})^2$.

With:
- `--metric_scale 1.0`, we see $\lambda_{\min}(0)\approx 0.250$ (the conservative constant used in the SAFE ledger).
- `--metric_scale 1.078689...`, we see $\lambda_{\min}(0)\approx 0.290893$, matching the draft’s **0.291 at $r=0$** at the single-link level.

Files:
- `safe_scan_tracked_v2.py`
- `safe_scan_results_scaled.csv`, `safe_scan_results_scaled.png`

---

## 2. What is **not** reproduced yet (and why)

### 2.1 The repo’s radius table is *not* just a single-link Haar scan

In the draft, the reported $\lambda_{\min}^{\mathrm{Haar}}(r)$ decreases with radius (e.g. $0.291\to 0.255$ by $r=0.05$),
which is **too large** to be explained by single-link Haar curvature variation at such tiny $r$.

The most plausible explanation is that the draft’s “Haar-only in physical subspace” already includes:

- a **link-cluster** (multiple links),
- a **configuration-dependent gauge projector** $\Pi_{\mathrm{phys}}(U)$ (or an equivalent Schur complement),
- thus nontrivial mixing between “Haar directions” and “gauge directions” as you move in the SAFE ball.

That is: the *projector* is doing real work.

### 2.2 Therefore the missing ingredient is algorithmic $H_{\mathrm{phys}}$

To reproduce (or falsify) the target minimum $\approx 0.248$ you need a concrete, executable definition of:

- the cluster (set of links, incidence structure),
- the gauge directions at a configuration $U$,
- how you project out gauge directions (explicit projector vs Schur complement),
- which inner products are used at each step.

That spec is provided separately in:

- `H_phys_spec.md`
- `h_phys_tools.py`

Once the draft’s $\Pi_{\mathrm{phys}}$ is *pinned down in code*, extending the scan from “Haar only” to “Haar+Wilson physical”
is straightforward engineering.

---

## 3. How to get to the full target scan

Minimal reproducibility plan:

1. Choose a concrete cluster (e.g. one plaquette or two plaquettes sharing a link).
2. Build the gauge generator matrix $G(U)$ and compute $\Pi_{\mathrm{phys}}(U)$ (QR/SVD or Schur complement).
3. Implement the total potential $V_{\mathrm{tot}}=V_{\mathrm{Haar}}+S_W$ on that cluster.
4. Compute the projected Hessian eigenvalues along the same radial/directional sampling scheme.

This note gives you step (1) for Haar, and the tooling/spec needed for step (2).

