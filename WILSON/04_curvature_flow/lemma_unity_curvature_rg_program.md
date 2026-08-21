# LEMMA UNITY — Towards a Continuum‑Relevant “Curvature RG”: Local Bakry–Émery, Typical Sets, and Riccati Flow

*Program note.* This file is deliberately forward‑leaning: it takes the finite‑cutoff curvature mechanism as a proven base and asks what would have to be true for a **continuum‑meaningful** theory.

The big idea is to replace “global convexity” (which provably dies) with a **scale‑dependent, localized curvature** that can be transported along coarse‑graining.

---

## 1. The obstruction: global Bakry–Émery curvature must go to \(-\infty\) as \(a\to 0\)

Consider the natural global Bakry–Émery constant
\[
\rho_{\mathrm{glob}}(a):=\inf_{U\in\mathcal{C}_a}\ \inf_{\|X\|=1}\Big(
\mathrm{Ric}(X,X)+\beta(a)\,\nabla^2 f(U)(X,X)
\Big),
\]
where \(\mathcal{C}_a=SU(N)^{|B|}\) and \(f(U)\) is the plaquette energy.

Two simple facts:

1. \(\mathrm{Ric}\) is bounded above and below by constants depending only on \(SU(N)\), not on volume.
2. Since \(f\) is smooth and nonconstant on compact \(\mathcal{C}_a\), it has a global maximum at some \(U^\*\). At that maximum, \(\nabla^2 f(U^\*)\preceq 0\), and there exists a direction \(Y\) with
   \[
   \nabla^2 f(U^\*)(Y,Y)=-\lambda<0.
   \]

Along the asymptotically free trajectory in \(4D\), \(\beta(a)\to\infty\) as \(a\to 0\). Evaluating at \((U^\*,Y)\) yields
\[
\rho_{\mathrm{glob}}(a)\ \le\ k_{\max}-\beta(a)\lambda\ \longrightarrow\ -\infty.
\]

**Conclusion.** Any attempt to prove the continuum theory via a **global** \(CD(\rho,\infty)\) lower bound is doomed: the global infimum necessarily dives to \(-\infty\).

This is not a disaster; it’s a signpost. It says: **look for a non‑global notion of curvature.**

---

## 2. Why a Riccati mechanism is the “right” mental model for coarse‑graining

A clean toy model shows why convexity wants to erode under smoothing.

### 2.1 Heat‑flow coarse‑graining ⇒ viscous Hamilton–Jacobi

Let \(\rho_t=e^{-S_t}\) solve the heat equation \(\partial_t\rho_t=\Delta\rho_t\) on \(\mathbb{R}^d\). Then
\[
\partial_t S_t=\Delta S_t-|\nabla S_t|^2.
\]

### 2.2 The Hessian equation is Riccati‑like

Let \(H_t=\nabla^2 S_t\). Differentiating twice gives
\[
\partial_t H_t=\Delta H_t-2H_t^2+R_t,
\]
where \(R_t\) is a “transport” remainder involving third derivatives weighted by \(\nabla S_t\).

Even ignoring \(R_t\), the term \(-2H_t^2\) is the signature:
it drives eigenvalues downward in a **Riccati** fashion.

### 2.3 Gaussian case: exact Riccati decay

If \(S_0(x)=\tfrac12 x^\top A_0 x\), then convolution with the heat kernel keeps the law Gaussian and
\[
\lambda_i(t)=\frac{\lambda_i(0)}{1+2t\lambda_i(0)},
\qquad
\lambda_i'(t)=-2\lambda_i(t)^2.
\]

So convexity remains positive but decays like \(1/t\). This matches the intuitive message:
**coarse‑graining bleeds curvature unless something replenishes it.**

---

## 3. Discrete coarse‑graining already contains a Riccati shadow: the block‑Hessian inequality

The project’s block convexity lemma says:

If \(S(x,y)\) is uniformly convex in both \(x\) and \(y\) and the mixed Hessian block is controlled by \(M\), then after marginalizing over \(y\),
\[
\nabla_x^2 S_{\mathrm{coarse}}(x)\ \succeq\ \left(\alpha-\frac{M^2}{\gamma}\right)I.
\]

In curvature language, if \(\rho=\min\{\alpha,\gamma\}\), then one step of coarse‑graining gives
\[
\rho_{\mathrm{new}}\ \gtrsim\ \rho-\frac{M^2}{\rho}.
\]

That is already a discrete Riccati‑type degradation.

### 3.1 A “curvature‑squared” conservation inequality (discrete budget law)

If (heuristically) \(\rho_{k+1}=\rho_k-\frac{M_k^2}{\rho_k}\), then
\[
\rho_{k+1}^2\ \ge\ \rho_k^2-2M_k^2,
\]
so
\[
\rho_k^2\ \ge\ \rho_0^2-2\sum_{j<k}M_j^2.
\]

This is a **budget law**: cumulative mixing energy \(\sum M_j^2\) controls how long convexity can persist across RG steps.

---

## 4. The novel proposal: replace global curvature by a *localized* / *typical‑set* curvature

Global curvature fails because it looks at the worst configuration in all of \(\mathcal{C}_a\). Physics, meanwhile, lives on configurations typical under \(\mu_a\).

### 4.1 A candidate definition: typical‑set Bakry–Émery constant

Fix \(\varepsilon\in(0,1)\). Define \(\rho_{\mathrm{typ}}(a;\varepsilon)\) as the largest number such that there exists a measurable set \(T_{a,\varepsilon}\subset\mathcal{C}_a\) with \(\mu_a(T_{a,\varepsilon})\ge 1-\varepsilon\) and
\[
\mathrm{Ric}+\nabla^2 S_{\mathrm{eff}}(U)\ \succeq\ \rho_{\mathrm{typ}}(a;\varepsilon)\,I
\qquad\text{for all }U\in T_{a,\varepsilon}.
\]

This trades “worst‑case over all \(U\)” for “worst‑case over typical \(U\)”.

### 4.2 Why this could matter

If one can prove two things:

1. **a Poincaré/log‑Sobolev inequality on \(T_{a,\varepsilon}\)** with constant \(1/\rho_{\mathrm{typ}}\), and
2. **fast return / stability**: the Langevin diffusion returns to \(T_{a,\varepsilon}\) quickly whenever it exits,

then one can often bootstrap to a global spectral gap (or at least to robust exponential mixing on observables of interest).

This is the same vibe as metastability theory and “two‑scale” functional inequalities:  
a good inequality on a high‑probability set plus control of exits can imply global convergence.

(Details depend on the precise decomposition method used; the point here is the *structure*.)

---

## 5. The real target: a curvature RG inequality *on typical sets*

The block‑Hessian inequality is deterministic. In real RG, the mixed block \(B\) and the fine‑scale curvature \(\gamma\) fluctuate with the configuration.

A continuum‑relevant theory would therefore aim for a probabilistic block inequality of the form:

> with high \(\mu\)-probability, coarse‑graining maps a typical set at scale \(a\) to a typical set at scale \(2a\), and the curvature parameter updates by a controlled inequality
> \[
> \rho_{k+1}\ \gtrsim\ \rho_k-\frac{M_k^2}{\rho_k},
> \]
> with \(M_k\) small on the typical set.

This would create an **iterable curvature RG flow**.

At that point, the “curvature‑squared budget law”
\[
\rho_k^2\ \ge\ \rho_0^2-2\sum_{j<k}M_j^2
\]
starts to look like a computable control knob:
if \(\sum M_j^2\) stays bounded as \(k\to\infty\), convexity survives; if it grows, convexity dies at a predictable scale.

Either way, you get a **scale** — and scales are what mass gaps feed on.

---

## 6. How this links back to physics without cheating

Three bridges to build (none are “free”):

1. **From Langevin spectral gap to Euclidean correlators.**  
   The Langevin operator is not the transfer matrix. But functional inequalities control fluctuations and can be used to bound variances of Wilson loop observables; one can then compare to strong‑coupling/cluster‑expansion estimates of correlators.

2. **From curvature along RG to correlation length.**  
   If you can show curvature survives to scale \(L\) (after \(k\sim\log(L/a)\) steps), then you can often turn that into an upper bound on a correlation length (a mass lower bound). This is where the curvature‑budget inequality becomes valuable.

3. **From typical‑set control to uniform statements.**  
   Ultimately you need “high‑probability” statements to imply the spectral property you care about. That usually means coupling local functional inequalities with recurrence/exit estimates.

---

## 7. Concrete next steps (tractable, and genuinely informative even if they fail)

1. **Make the mixing norm \(M\) structural, not worst‑case.**  
   The current \(M\) is a uniform operator‑norm bound. In practice, on typical configurations the effective \(M\) might be much smaller. Prove concentration estimates for the mixed block.

2. **Iterate the block inequality.**  
   Write down a multi‑step version with \(M_k\) and \(\rho_k\). Even bounding the number of steps before \(\rho_k\) drops below \(0\) would produce a scale.

3. **Replace global Hessian bounds by “energy‑conditioned” bounds.**  
   Condition on a plaquette energy band \(f(U)\le E\). On such sets, the Wilson Hessian may have improved lower bounds. This is the most plausible route to a nontrivial \(\rho_{\mathrm{typ}}\) at large \(\beta\).

4. **Integrate the polar‑set technology.**  
   Any typical‑set argument should be done on the irreducible stratum; polarity lets you do this without losing the physical measure.

5. **Check the toy model numerics.**  
   The discrete Riccati budget law is so simple you can test it in scalar or reduced gauge models: compute empirical \(M_k\) and \(\rho_k\) under blocking and see if the inequality tracks reality.

---

## 8. The “novel thing” in one sentence

The finite‑cutoff proofs give a *deterministic* curvature mechanism; the proposed next step is a **probabilistic curvature RG** in which convexity is tracked on typical sets by a discrete Riccati‑type budget inequality.

That framework is not standard lattice strong‑coupling expansion, not reflection‑positivity technology, and not continuum perturbation theory — it’s a geometric/analytic lane that could, with luck and sweat, connect mass‑gap questions to a new family of RG‑stable functional inequalities.
