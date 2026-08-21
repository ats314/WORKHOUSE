# Simulation diagnostics for the Lyapunov program (drift decomposition + \(\Phi_{\mathrm{proxy}}\))

> **What this file is.** A compact record of the most “physics-relevant” numerical diagnostics in the project
> related to the Lyapunov drift bottleneck.  
> These simulations do **not** prove the missing coercivity lemma, but they do (i) validate the algebraic
> decomposition being used, and (ii) quantify an obstruction term \(\Phi_{\mathrm{proxy}}\) that survives
> gauge/Hodge projection and blocking.

---

## 1. Diagnostic A: drift decomposition identity is numerically exact

The project tests the decomposition (schematic)
\[
(\mathcal L V)(U) \stackrel{?}{=} \Delta V(U) \;-\; \langle \nabla S_W(U), \nabla V(U)\rangle
\]
by computing:

- \(LV := (\mathcal L V)(U)\) directly from the generator implementation,
- \(\mathrm{lap} := \Delta V(U)\),
- \(\mathrm{gip} := \langle \nabla S_W,\nabla V\rangle\),

and then checking the residual \(LV - (\mathrm{lap}-\mathrm{gip})\).

**Reported residual.** The max absolute residual is about \(3\times 10^{-14}\), i.e. at floating precision,
for a batch of 6144 Monte Carlo samples.

This is useful because it confirms that what remains is *not a coding artifact*:
the missing coercivity is genuinely about the sign/size of \(\mathrm{gip}\).

---

## 2. Diagnostic B: an “affine Laplacian law” for \(\overline V\)

A striking empirical observation is that the Laplacian term for the averaged Lyapunov \(\overline V\)
fits extremely well to an affine function of an averaged badness \(B_{\mathrm{avg}}\):
\[
\mathrm{lap}(\overline V) \approx a + b\,B_{\mathrm{avg}},
\]
with a near-perfect \(R^2\) on the tested sample.

One example reported is
\[
\mathrm{lap} \approx 12 - 12\,B_{\mathrm{avg}},
\]
with \(R^2\approx 0.999999\).

Interpretation: the Laplacian term behaves almost like a linear response in the defect variable,
which makes it plausible that a matching *lower bound* for \(\mathrm{gip}\) should exist (at least on a good set).

---

## 3. Diagnostic C: \(\Phi_{\mathrm{proxy}}\) under gauge/Hodge projection + blocking

A separate experiment computes an obstruction statistic
\[
\Phi_{\mathrm{proxy}} \quad (\text{details in the run script}),
\]
after applying:
- a gauge/Hodge projector step, and
- a \(2\times\) blocking / coarse-graining step.

**Reported value (representative run).**
\[
\Phi_{\mathrm{proxy}} \approx 0.193333
\quad\text{at}\quad \kappa_\* = 0.5.
\]

Additionally, the report notes that blocking a random configuration can strongly amplify defects
(e.g. negative \(\lambda_{\min}\) and large normalized curvature defect), suggesting that
coarse-graining needs a carefully designed “reflection-positive” or “defect-non-amplifying” map.

---

## 4. Minimal code skeleton for these diagnostics (structure only)

The full scripts are long; the conceptual core is:

```python
# Pseudocode structure

# 1) Sample configurations U ~ (approx) Gibbs
U_batch = sample_configs(N)

# 2) Compute Lyapunov and its Laplacian term
V = V_bar(U_batch)                  # average of local proxy
lap = laplacian_V_bar(U_batch)      # ΔV term

# 3) Compute gradient inner product term
gS = grad_S_W(U_batch)
gV = grad_V_bar(U_batch)
gip = inner_product(gS, gV)

# 4) Generator evaluation
LV = generator_apply_to_V_bar(U_batch)

# 5) Check residual
resid = LV - (lap - gip)
print(resid.abs().max())

# 6) Fit affine law lap ≈ a + b*Bavg
a,b = linear_regression(Bavg, lap)

# 7) Gauge/Hodge projection and blocking
U_proj = hodge_project(U_batch)
U_blk  = block_2x(U_proj)

# 8) Compute Φ_proxy on the blocked field
Phi_proxy = compute_phi_proxy(U_blk, kappa_star=0.5)
print(Phi_proxy)
```

---

## 5. What these sims suggest (conservatively)

1. The drift identity is solid.
2. The Laplacian term is well-behaved and may be expressible in closed form (or bounded sharply).
3. The difficult part is the **pairing/coercivity** of \(\langle \nabla S_W,\nabla V\rangle\).
4. Coarse-graining can introduce new defect energy unless the block map is designed to control it.

---
