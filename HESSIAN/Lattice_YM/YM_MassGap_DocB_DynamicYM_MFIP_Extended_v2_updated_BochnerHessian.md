# Extended Derivations for the MFIP and Dynamic Yang–Mills

**Document:** YM_MassGap_DocB_DynamicYM_MFIP – Extended Derivations  
**Role:** Technical backbone for the dynamic route and the Multiscale Functional Inequality Program (MFIP).

This document deepens the derivations in Doc B, focusing on:

- The viscous Hamilton–Jacobi (vHJ) ansatz for effective actions.
- The Hessian evolution equation and its reaction–diffusion structure.
- The MFIP RG-step inequalities for Log–Sobolev and Poincaré constants.
- The variance decomposition into local vs topological contributions.

---

## 1. Finite-Dimensional Viscous Hamilton–Jacobi Derivation

We briefly recall the finite-dimensional vHJ derivation as a model for the YM case.

Let \(x \in \mathbb{R}^n\), and consider the heat equation for a density \(\rho_t(x)\):
\[
\partial_t \rho_t = \Delta \rho_t.
\]

We insert the exponential ansatz
\[
\rho_t(x) = Z_t^{-1} e^{-S_t(x)},
\]
where \(S_t : \mathbb{R}^n \to\mathbb{R}\) and normalizing factor \(Z_t>0\) such that \(\int e^{-S_t}\,dx = 1\). Then
\[
\partial_t\rho_t
= -Z_t^{-1}(\partial_t S_t)e^{-S_t} - Z_t^{-2}(\partial_t Z_t)e^{-S_t}
= -(\partial_tS_t)\rho_t - (\partial_t\log Z_t)\rho_t.
\]

Compute \(\Delta\rho_t\):
\[
\Delta\rho_t
= \Delta(e^{-S_t})
= e^{-S_t}(-\Delta S_t + |\nabla S_t|^2).
\]

Equating \(\partial_t\rho_t=\Delta\rho_t\) and dividing by \(\rho_t>0\) gives
\[
-(\partial_t S_t) - (\partial_t\log Z_t)
= -\Delta S_t + |\nabla S_t|^2.
\]

The normalizing factor contributes only a spatially constant term, absorbed into \(\partial_t\log Z_t\). Dropping this constant (i.e. working with \(S_t\) defined modulo an additive constant) yields the **viscous Hamilton–Jacobi equation**
\[
\partial_t S_t
= \Delta S_t - |\nabla S_t|^2.
\]

More generally, if the heat flow is modified by a source term \(J_t\) (coming from, e.g., a change of reference measure, drift, or anomaly), we obtain:
\[
\partial_t S_t
= \Delta S_t - |\nabla S_t|^2 + J_t.
\]

This is the vHJ equation used as a toy model for the RG evolution of effective actions.

---

## 2. Hessian Flow: Detailed Computation

We now derive the Hessian evolution equation. Let
\[
b_t := \nabla S_t, \quad
h_t := \nabla^2 S_t.
\]
We write component indices \(i,j,k\) for clarity.

Start from the vHJ equation
\[
\partial_t S_t
= \Delta S_t - |b_t|^2 + J_t.
\]
We differentiate in spatial variables.

### 2.1. Gradient evolution

Take a gradient:
\[
\partial_t b_{t,i}
= \partial_i (\Delta S_t) - \partial_i(|b_t|^2) + \partial_i J_t.
\]

Because \(\Delta\) is the divergence of the gradient, we have \(\partial_i\Delta S_t = \Delta \partial_i S_t\), so
\[
\partial_i(\Delta S_t) = \Delta b_{t,i}.
\]

For the nonlinear term:
\[
\partial_i(|b_t|^2)
= \partial_i(b_{t,j}b_{t,j})
= 2 b_{t,j} \partial_i b_{t,j}.
\]

Thus,
\[
\partial_t b_{t,i}
= \Delta b_{t,i} - 2\sum_j b_{t,j}\,\partial_i b_{t,j} + \partial_i J_t.
\]

In vector notation,
\[
\partial_t b_t
= \Delta b_t - 2\,\nabla S_t \,\cdot \nabla b_t + \nabla J_t.
\]

This is still in flat space (no curvature).

### 2.2. Hessian evolution

Differentiate again:
\[
\partial_t h_{t,ik}
= \partial_k\partial_t b_{t,i}
= \partial_k\Delta b_{t,i}
  - 2\partial_k\Big(\sum_j b_{t,j}\partial_i b_{t,j}\Big)
  + \partial_{ik}^2 J_t.
\]

We compute term by term.

1. \(\partial_k\Delta b_{t,i} = \Delta h_{t,ik}\).

2. For the nonlinear term:
   \[
   \partial_k(b_{t,j}\partial_i b_{t,j})
   = (\partial_k b_{t,j})(\partial_i b_{t,j}) + b_{t,j}(\partial_{ik}^2 b_{t,j}).
   \]
   Recognize:
   \[
   \partial_k b_{t,j} = h_{t,jk},
   \quad
   \partial_{ik}^2 b_{t,j} = \partial_i h_{t,jk}.
   \]
   So
   \[
   \partial_k(b_{t,j}\partial_i b_{t,j})
   = h_{t,jk} h_{t,ji} + b_{t,j}\partial_i h_{t,jk}.
   \]

Putting this in the evolution equation:
\[
\partial_t h_{t,ik}
= \Delta h_{t,ik}
  - 2\left(h_{t,jk} h_{t,ji} + b_{t,j}\partial_i h_{t,jk}\right)
  + \partial_{ik}^2 J_t.
\]

In compact notation:

- The term \(\sum_j h_{t,jk} h_{t,ji}\) is precisely the \((i,k)\) component of the matrix product \(h_t^2\).
- The term \(b_{t,j}\partial_i h_{t,jk}\) is the directional derivative of \(h_t\) in the direction of \(b_t\), i.e. \((\nabla_{b_t}h_t)_{ik}\).

Thus we can write
\[
\partial_t h_t
= \Delta h_t
  - 2\,\nabla_{b_t} h_t
  - 2 h_t^2
  + \nabla^2 J_t.
\]

Since \(b_t = \nabla S_t\), we may equally write
\[
\partial_t h_t
= \Delta h_t
  - 2(\nabla S_t\cdot\nabla h_t)
  - 2 h_t^2
  + \nabla^2 J_t.
\]

This is the reaction–diffusion equation for the Hessian in flat space:

- **Diffusion:** \(\Delta h_t\).
- **Drift:** \(-2(\nabla S_t\cdot\nabla h_t)\).
- **Nonlinear flattening:** \(-2h_t^2\).
- **Source:** \(\nabla^2 J_t\), which we interpret as anomaly-driven curvature injection.

### 2.3. Projected Bochner–Hessian Flow on the Gauge Quotient

The flat computation above takes place on a Euclidean configuration space. For Yang–Mills we ultimately want a **horizontal** version of the Hessian flow on the gauge quotient
\[
\mathcal{M}_{\mathrm{reg}} = \mathcal{A}_{\mathrm{reg}} / \mathcal{G},
\]
where we restrict to the regular (irreducible) stratum so that the quotient is a smooth Hilbert–Riemannian manifold. This subsection records the formal derivation; it is rigorous at any finite cutoff where \(\mathcal{M}_{\mathrm{reg}}\) is finite dimensional (e.g., lattice configuration manifolds or Galerkin truncations).

We denote by \(\nabla_H\) and \(\Delta_H\) the horizontal gradient and horizontal Laplacian, i.e. the Riemannian gradient and Laplace–Beltrami operator on \(\mathcal{M}_{\mathrm{reg}}\). Let \(\mathrm{Ric}\) and \(\mathrm{Rm}\) be the Ricci and Riemann curvature tensors of this metric.

We assume that the effective action \(S_t : \mathcal{M}_{\mathrm{reg}} \to \mathbb{R}\) satisfies the **horizontal vHJ equation**
\[
\partial_t S_t
= \Delta_H S_t - |\nabla_H S_t|^2 + J_t,
\]
with anomaly/source term \(J_t\). Set the horizontal gradient and Hessian
\[
V_t := \nabla_H S_t, \qquad
h_t := \nabla_H^2 S_t.
\]

#### 2.3.1. Gradient evolution via Bochner identity

Apply \(\nabla_H\) to the vHJ equation:
\[
\nabla_H(\partial_t S_t)
= \nabla_H(\Delta_H S_t) - \nabla_H|\nabla_H S_t|^2 + \nabla_H J_t.
\]
Because the geometry is fixed in time, \(\nabla_H\) and \(\partial_t\) commute, so
\[
\partial_t V_t
= \nabla_H(\Delta_H S_t) - \nabla_H|V_t|^2 + \nabla_H J_t.
\]

On a Riemannian manifold, the Bochner–Weitzenböck identity for scalar functions gives
\[
\nabla_H(\Delta_H f)
= \Delta_H(\nabla_H f) + \mathrm{Ric}(\nabla_H f).
\]
Applying this with \(f=S_t\) yields the **Bochner-corrected gradient flow**
\[
\partial_t V_t
= \Delta_H V_t
  + \mathrm{Ric}(V_t)
  - \nabla_H|V_t|^2
  + \nabla_H J_t.
\]

#### 2.3.2. Hessian evolution and the geometric correction

Define the horizontal Hessian
\[
h_t := \nabla_H V_t = \nabla_H^2 S_t.
\]
Taking \(\nabla_H\) of the gradient flow gives
\[
\partial_t h_t = \nabla_H(\partial_t V_t).
\]
We now treat the terms in \(\partial_t V_t\) one by one.

1. **Nonlinear term.** In local horizontal coordinates with orthonormal frame \((e_i)\), write \(V_t = V^k e_k\) and \(h_{ij} = \nabla_i V_j\). Then
   \[
   \nabla_i\nabla_j(|V|^2)
   = \nabla_i\nabla_j(V_k V_k)
   = 2\nabla_i(V_k\nabla_j V_k)
   = 2(\nabla_i V_k)(\nabla_j V_k) + 2V_k\nabla_i\nabla_j V_k.
   \]
   Identifying
   \[
   (\nabla_i V_k)(\nabla_j V_k) = (h^2)_{ij}, \qquad
   V_k\nabla_i\nabla_j V_k = (\nabla_{V_t}h_t)_{ij},
   \]
   we obtain the tensor identity
   \[
   \nabla_H^2 |V_t|^2 = 2 h_t^2 + 2 \nabla_{V_t} h_t.
   \]
   Thus
   \[
   -\nabla_H\nabla_H|V_t|^2 = -2h_t^2 - 2\nabla_{V_t} h_t.
   \]

2. **Laplacian term.** Commuting \(\nabla_H\) with \(\Delta_H\) on vector fields and tensors produces Riemann curvature terms. For a vector field \(W\),
   \[
   \nabla_H(\Delta_H W)
   = \Delta_H(\nabla_H W) + \mathcal{R}_1(\nabla_H W),
   \]
   where \(\mathcal{R}_1\) is a linear operator on symmetric 2-tensors built from \(\mathrm{Rm}\). Writing \(h_t = \nabla_H W\), this gives
   \[
   \nabla_H(\Delta_H V_t)
   = \Delta_H h_t + \mathcal{R}_1(h_t).
   \]

3. **Ricci term.** Differentiating \(\mathrm{Ric}(V_t)\) gives another curvature contribution, which we denote
   \[
   \nabla_H(\mathrm{Ric}(V_t)) = \mathcal{R}_2(V_t),
   \]
   where \(\mathcal{R}_2\) is affine-linear in \(h_t\) and linear in \(V_t\), with coefficients given by \(\mathrm{Rm}\) and its covariant derivatives.

4. **Anomaly term.** Finally,
   \[
   \nabla_H(\nabla_H J_t) = \nabla_H^2 J_t =: \mathbf{S}_{\mathrm{anom}}(t).
   \]

Putting everything together, we arrive at the **Projected Bochner–Hessian Flow**
\[
\boxed{
\partial_t h_t
= \Delta_H h_t
  - 2\nabla_{V_t} h_t
  - 2 h_t^2
  + \mathbf{S}_{\mathrm{anom}}(t)
  + \mathfrak{G}(S_t,h_t),
}
\]
where the **geometric correction**
\[
\mathfrak{G}(S_t,h_t)
:= \mathcal{R}_1(h_t) + \mathcal{R}_2(V_t)
\]
is linear in \(h_t\) and \(V_t\) with coefficients determined by the curvature of the quotient geometry and the non-integrability of the horizontal distribution.

In particular, when the configuration space is flat and the horizontal distribution is integrable (as in the toy flat model), the curvature tensors vanish, \(\mathfrak{G}\equiv0\), and we recover exactly the flat reaction–diffusion equation derived in §2.2.

#### 2.3.3. Minimal eigenvalue inequality

Let \(\lambda_{\min}(t,x)\) be the smallest eigenvalue of the symmetric bilinear form \(h_t(x)\) on \(T_x\mathcal{M}_{\mathrm{reg}}\), and define
\[
\lambda_{\min}(t) := \inf_{x\in\mathcal{M}_{\mathrm{reg}}} \lambda_{\min}(t,x).
\]
Assuming bounded geometry at finite cutoff (uniform bounds on \(|\mathrm{Rm}|\) and its derivatives, so that \(\mathcal{R}_1,\mathcal{R}_2\) are bounded operators), a standard parabolic maximum principle argument applied to the tensor equation above yields a scalar differential inequality of the form
\[
\partial_t \lambda_{\min}(t)
\gtrsim
-2\lambda_{\min}(t)^2
- C_{\mathrm{geom}}\big(1 + \lambda_{\min}(t) + \lambda_{\min}(t)^2\big)
+ \sigma_{\mathrm{anom}}(t),
\]
where
\[
\sigma_{\mathrm{anom}}(t)
:= \inf_{x\in\mathcal{M}_{\mathrm{reg}}}\;\inf_{\|v\|=1}
   \langle v,\mathbf{S}_{\mathrm{anom}}(t,x)v\rangle
\]
is the minimal horizontal eigenvalue of the anomaly source, and \(C_{\mathrm{geom}}\) depends only on curvature bounds.

The “toy” inequality used in the Bridging Proposition,
\[
\partial_t \lambda_{\min} \ge -2\lambda_{\min}^2 + \sigma_*,
\]
is obtained from this by (formally) neglecting the geometric term and assuming \(\sigma_{\mathrm{anom}}(t)\approx\sigma_*\) in the IR. The projected flow shows precisely what is required of the anomaly source in the true gauge-quotient geometry: it must dominate **both** the Riccati flattening \(-2h_t^2\) and the negative part of the geometric correction \(\mathfrak{G}\).

This completes the continuum counterpart of the lattice Hessian analysis: in both pictures, a curvature-driven source (Haar-measure mass term on the lattice, anomaly source \(\mathbf{S}_{\mathrm{anom}}\) in the continuum) can force the minimal Hessian eigenvalue away from zero provided it is strong enough to overcome the flattening and geometric corrections.

---

## 3. Bakry–Émery Curvature and MFIP

We recall the core connection between curvature and functional inequalities, then explain how MFIP tracks these quantities across scales.

### 3.1. Bakry–Émery curvature and LSI

For a diffusion on a Riemannian manifold with generator
\[
L f = \Delta f - \nabla S\cdot\nabla f,
\]
the carré du champ is
\[
\Gamma(f) = \tfrac12 L(f^2) - fLf = |\nabla f|^2,
\]
and the iterated carré du champ is
\[
\Gamma_2(f)
= \tfrac12 L(\Gamma(f)) - \Gamma(f,Lf).
\]

A standard computation (Bakry–Émery) gives
\[
\Gamma_2(f)
= \|\nabla^2 f\|^2_{\mathrm{HS}} + \langle \nabla^2 S\,\nabla f,\nabla f\rangle
  + \mathrm{Ric}(\nabla f,\nabla f),
\]
so that a curvature lower bound of the form
\[
\nabla^2 S + \mathrm{Ric} \;\ge\; \rho\, I
\]
implies
\[
\Gamma_2(f)\;\ge\;\rho\,\Gamma(f)
\quad\text{for all smooth }f.
\]

The inequality \(\Gamma_2\ge \rho\Gamma\) is equivalent to a family of functional inequalities, including:

- A Log–Sobolev inequality with constant \(\alpha \ge \rho\).
- A Poincaré inequality with constant \(\lambda \ge \rho\).

This is the rigorous sense in which a **curvature lower bound** forces an **LSI\(/\)spectral gap**, and it motivates tracking \(\nabla^2 S_t\) (or its horizontal projection in YM) along RG time.

### 3.2. MFIP constants and RG steps

In the MFIP, at each scale \(j\) we have:

- An effective measure \(\mu_j\) on coarse fields.
- An associated Dirichlet form \(\mathcal{E}_j(f,f)\).
- A horizontal Log–Sobolev constant \(\alpha_j\) and Poincaré constant \(\lambda_j\).

An RG step from scale \(j\) to \(j+1\) is decomposed schematically as:

1. **Block decomposition:** write the field \(A\) as coarse + fine modes at scale \(j\).
2. **Conditional measures:** integrate out fine modes to get the effective measure on coarse modes.
3. **Reweighting:** incorporate the integrated-out fluctuations into a new effective action \(S_{j+1}\).

On each block, the Bakry–Émery curvature of the conditional measure is controlled if:

- The effective Hessian on that block has a uniform positive lower bound (local convexity).
- Curvature of the configuration manifold (gauge quotient, lattice configuration space) is bounded.

Heuristically, the RG update of \(S_t\) at the coarse scale induces an update of the Hessian and thus an update of the block LSI constants \(\alpha_j\). The projected Bochner–Hessian flow derived in §2.3 is the continuum PDE version of this RG update.

### 3.3. Dynamic picture for \(\alpha_j\) and \(\lambda_j\)

We can think of the MFIP as tracking the evolution of \(\alpha_j\) and \(\lambda_j\) under a discrete version of the Hessian flow. The flat model suggests a schematic inequality of the form
\[
\alpha_{j+1} - \alpha_j
\;\gtrsim\;
- C\,\alpha_j^2 + \sigma_{\mathrm{anom}}(j),
\]
where:

- The term \(-C\,\alpha_j^2\) represents the Riccati-type flattening coming from the \(-2h_t^2\) nonlinearity.
- \(\sigma_{\mathrm{anom}}(j)\) corresponds to the positive curvature injected by the anomaly source (e.g. Haar measure, measure reweighting).

The curvature term \(\mathfrak{G}\) in the projected Bochner–Hessian flow translates into additional error terms in this inequality, which must be dominated by \(\sigma_{\mathrm{anom}}\) if we want \(\alpha_j\) to converge to a strictly positive fixed point in the IR.

---

## 4. Variance Decomposition and Local vs Topological Sectors

Finally, we recall the basic variance decomposition that separates local (bulk) fluctuations from global/topological contributions.

Let \(\mu\) be a Gibbs measure on a configuration space with a decomposition into “local” variables \(\xi\) and a finite set of “topological” variables \(\tau\) (e.g. magnetic fluxes, center vortices). Then for any observable \(F\),
\[
\mathrm{Var}_\mu(F)
= \mathbb{E}_tau[\mathrm{Var}(F|\tau)] + \mathrm{Var}_\tau(\mathbb{E}[F|\tau]).
\]

If:

- Each conditional measure \(\mu(\cdot|\tau)\) has a uniform LSI\(/\)spectral gap with constant \(\lambda_{\mathrm{loc}}>0\).
- The number of topological sectors is finite (or controlled) and their weights are comparable.

then the **local sector** already carries a mass gap, and the only remaining issue is how different topological sectors glue together in the infinite-volume limit. In the YM mass-gap program:

- The local, curvature-driven gap is handled by the MFIP and the projected Bochner–Hessian flow.
- The topological issues are handled by the constructive lattice analysis, polymer expansions, and cluster arguments in Doc D.

This document provides the detailed flat and curved Hessian flows and the Bakry–Émery framework that underlie those arguments.
