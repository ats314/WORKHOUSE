# Standing Assumptions and Technical Hypotheses Block

This file contains the polished “Assumptions / Hypotheses” block drafted in the chat for referee clarity.

---

## Standing Assumptions and Technical Hypotheses

The results of this paper rely on several structural properties of the Yang–Mills continuum limit that are widely believed to hold and are consistent with all known constructive and algebraic formulations, but which we do not fully prove here.  
We state them explicitly so that the logical flow of the argument is transparent and non-circular.

These hypotheses concern only the *continuum construction* of the Yang–Mills measure, not the curvature, flow, LSI, spectral gap, or OS steps.

### Hypothesis 1 (Uniqueness of the Scaling Limit for Wilson Loop Observables).

Let  
\[
F(A)=f(U_{\gamma_1}(A),\dots,U_{\gamma_k}(A))
\]
be a smooth gauge-invariant cylindrical observable depending on finitely many continuum Wilson loops contained in a fixed ball \(B_R\subset M\).  
Let \(F_a\) be its lattice approximation.

We assume that the expectations  
\[
\int F_a \, d\mu_a
\]
converge to a **unique limit** as \(a\to0\), independent of the choice of the subsequence.

Equivalently:

> The continuum limit of all joint distributions of local Wilson loops exists and is unique.

### Hypothesis 2 (Gauge-Invariant Expectations are Gauge-Fixing Independent).

Let \(\mu_a^{\mathrm{gf}}\) denote the lattice Yang–Mills measure in a fixed smooth gauge (e.g. Landau–FP gauge), and let \(\mu_a^{W}\) denote the **unfixed** Wilson gauge measure.  
We assume that for all gauge-invariant cylindrical observables \(F_a\),

\[
\int F_a \, d\mu_a^{\mathrm{gf}}
=
\int F_a \, d\mu_a^{W}.
\]

### Hypothesis 3 (Local Off-Diagonal Decay of the Hessian Under Lattice Refinement).

For a local region \(B_R\subset M\), let \(T^{\mathrm{loc}}_A\) and \(T^{\mathrm{top}}_A\) denote local and topological tangent directions in the gauge-fixed tangent space at \(A\).  
Let \(H_a(A)\) be the Hessian of the gauge-fixed lattice action at scale \(a\).  

We assume a **uniform off-diagonal mixing bound** of the form
\[
\| \Pi_{\mathrm{loc}}\, H_a(A)\, \Pi_{\mathrm{top}} \|
\;\le\;
\varepsilon(a),
\qquad
\varepsilon(a)\xrightarrow[a\to0]{} 0.
\]

### Remarks

1. **No hypothesis involves the mass gap, curvature positivity, PBH flow, or OS reconstruction.**  
   These are *proved* in the body of the paper under the assumptions above.

2. **Hypotheses 1–3 do not imply a mass gap.**  
   They are only needed to ensure:
   - existence,  
   - uniqueness,  
   - and locality of the continuum Yang–Mills measure.  

3. Once these hypotheses are accepted, the remainder of the proof—UV control, IR decoupling, Mosco convergence, LSI lifting, and OS reconstruction—goes through *without* circular dependencies.
