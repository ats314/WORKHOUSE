# Conjectures A & B: Multiscale Stability as a Fixed-Point Problem  
*Research note / program skeleton*

This note isolates two conjectural inputs that, together, would convert a finite-cutoff lattice mass gap into a **continuum-stable** one via a multiscale recursion.

The project frames the “continuum hand-off” as a stability inequality of **fixed-point type**. The new conceptual move is to treat “mass gap persistence” as the existence of a **positive fixed point** of a coarse-graining recursion, with two independent failure modes:

- errors \(\varepsilon_j\) that accumulate across scales, and  
- loss of a positive source \(\sigma_*\) in the continuum limit.

---

## 1. The MFIP recursion and its fixed point

Let \(j\) index RG/coarse-graining steps from UV to IR. Let \(\rho_j\) be a “curvature / gap parameter” at scale \(j\). The Multiscale Fixed-Point Inequality (MFIP) is

\[
\rho_{j+1}\;\ge\; K\,\rho_j \;-\;\varepsilon_j \;+\;\sigma_*,
\qquad 0<K<1.
\]

Interpretation:

- \(K\) is the contraction/decay of curvature under coarse-graining **without** extra sources.
- \(\varepsilon_j\) is the “correlation / nonlocality error” produced by integrating out degrees of freedom.
- \(\sigma_*\) is a **positive source** that does not vanish in the continuum.

### Lemma (fixed point lower bound)

Assume:

1. \(0<K<1\),
2. \(\varepsilon_j\ge 0\) and \(\varepsilon_\infty:=\limsup_{j\to\infty}\varepsilon_j<\infty\).

Then any sequence satisfying the MFIP obeys
\[
\liminf_{j\to\infty}\rho_j
\;\ge\;
\frac{\sigma_*-\varepsilon_\infty}{1-K}.
\]
In particular, if \(\sigma_*>\varepsilon_\infty\), then \(\rho_j\) stays bounded away from 0 at large scales.

**Proof (sketch).** Iterating the inequality gives
\[
\rho_{j+n}\ge K^n\rho_j + \sum_{m=0}^{n-1}K^{n-1-m}(\sigma_*-\varepsilon_{j+m}).
\]
Take \(n\to\infty\), use \(K^n\to 0\), and estimate \(\varepsilon_{j+m}\le \varepsilon_\infty+\delta\) for large \(m\). \(\square\)

So the continuum problem becomes: ensure **(i)** \(\varepsilon_\infty\) is small (ideally \(0\)), and **(ii)** \(\sigma_*>0\).

That is where Conjectures A and B enter.

---

## 2. Conjecture A: Log-Forest UV Control (error suppression)

### Informal statement

Wilson-loop observables probe the UV roughness of gauge fields. Conjecture A asserts that their “roughness norm” grows only **polylogarithmically** with the UV cutoff.

### Precise form (one workable version)

Let \(W_C\) be a Wilson loop associated to a closed loop \(C\) of length \(L(C)\) at lattice spacing \(a\), with Yang–Mills measure \(\mu_a\). Then there exist constants \(C,\alpha>0\) such that

\[
\|\nabla W_C\|_{L^2(\mu_a)}
\;\le\;
C\,L(C)\,\Big(\log\frac{1}{a}\Big)^\alpha
\quad\text{uniformly in }a.
\]

Equivalently, for the Dirichlet form \( \mathcal{E}_a(f)=\int\|\nabla f\|^2\,d\mu_a\),
\[
\mathcal{E}_a(W_C)
\;\le\;
C\,L(C)^2\,\Big(\log\frac{1}{a}\Big)^{2\alpha}.
\]

### Why this controls \(\varepsilon_j\)

In many RG decompositions, \(\varepsilon_j\) is dominated by inter-block correlations and sensitivity of coarse observables to microscopic fields, i.e. by terms of the form \(\|\nabla f\|^2\) for key \(f\)’s. A polylog bound often implies a **summable** error profile, e.g.
\[
\varepsilon_j \;\lesssim\; j^{-\beta}(\log j)^\alpha
\quad(\beta>1)\quad\Rightarrow\quad \sum_j \varepsilon_j<\infty,
\]
hence \(\varepsilon_\infty=0\) in the fixed-point bound.

### Bigger-theory connection

Conjecture A is a geometric encoding of **asymptotic freedom**: short-distance fluctuations are suppressed by a running coupling \(g^2(\mu)\sim 1/\log(\mu)\). It is also tightly linked to constructive RG technology (Balaban/Brydges–Yau style).

---

## 3. Conjecture B: Anomaly Source (a nonvanishing \(\sigma_*\))

### Informal statement

A positive source term survives the continuum limit. At finite cutoff, Haar measure provides a source that *vanishes* with \(a\). Conjecture B asserts that **trace anomaly and/or topology** take over and provide a positive, cutoff-independent \(\sigma_*\).

### A precise form

Let \(S_a\) be the effective action at spacing \(a\), with horizontal Hessian \(H_a=\nabla^2 S_a|_{\mathrm{hor}}\). Decompose:
\[
\lambda_{\min}(H_a)\;\ge\; -C_{\text{Wilson}} + \sigma_a.
\]
Conjecture B asserts:
\[
\liminf_{a\to 0}\sigma_a \;\ge\; \sigma_* \;>\;0.
\]

### Trace-anomaly heuristic candidate for \(\sigma_*\)

In continuum Yang–Mills,
\[
\langle T^\mu_{\ \mu}\rangle = \frac{\beta(g)}{2g}\,\langle F^a_{\mu\nu}F^{a\,\mu\nu}\rangle,
\qquad \beta(g)<0.
\]
Heuristically, if \(\langle F^2\rangle>0\), then the anomaly yields a **positive** scalar scale:
\[
\sigma_* \sim \frac{|\beta(g_*)|}{2g_*}\,\langle F^2\rangle.
\]

This is not yet a theorem; it is a target: identify an explicit map from anomaly data to a Bakry–Émery/Hessian lower bound.

### Topological route: \(\theta\)-curvature and \(\chi_t\)

If a \(\theta\)-dependent vacuum free energy \(F(\theta)\) exists, then
\[
F''(0)\;=\;\frac{\chi_t}{V}
\]
(where \(\chi_t\) is the topological susceptibility). Since \(\chi_t\ge 0\) in stable theories, this provides a natural convexity datum. A fully rigorous bridge would be:

- define \(\chi_t\) nonperturbatively (e.g. via gradient flow),  
- prove \(\chi_t\to\chi_*>0\) in the continuum,  
- convert that into a positive \(\sigma_*\) for the MFIP/Riccati mechanism.

---

## 4. Why A and B are coupled

The MFIP fixed point requires the inequality
\[
\sigma_* \;>\; \varepsilon_\infty.
\]

- Conjecture A makes \(\varepsilon_\infty\) small (ideally \(0\)).  
- Conjecture B makes \(\sigma_*\) positive and **scale-independent**.

Proving either one alone is not enough.

---

## 5. Concrete proof avenues (non-exhaustive)

### For Conjecture A
- Constructive RG / polymer expansions (Balaban-type).  
- Stochastic quantization + Malliavin calculus to bound derivatives.  
- Rigorous gradient-flow regularity bounds for Wilson loops.

### For Conjecture B
- Anomaly-to-curvature conversion via functional RG (Wetterich equation) with controlled truncations.  
- Topological susceptibility via gradient flow; prove a positive continuum limit and relate to convexity.  
- “Sector decomposition” arguments controlling topological contributions to effective action curvature.

---

## 6. What would count as a *real* milestone?

A meaningful intermediate theorem would be:

> **Milestone target.**  
> Construct a multiscale coarse-graining map \(S_{j}\mapsto S_{j+1}\) on finite lattices with:
> 1. a uniform quantitative estimate of \(\varepsilon_j\) in terms of \(\mathcal{E}_a(W_C)\), and  
> 2. an explicit lower bound \(\sigma_a\ge \sigma_0>0\) that improves (or at least does not degrade) for small \(a\).

That would turn the MFIP from a slogan into a lever.

