# Mass Gap Project — Curated Export (Chat + Project Files)

This bundle is a **high-signal export** of the most technically promising derivations, lemmas, and simulation results found in the chat + attached project files.

It is *not* a claim that the 4D Yang–Mills mass gap is solved.  
Instead, it collects the **pieces that (a) are correct on their own**, **(b) appear to scale in the right way**, or **(c) form a plausible research program**.

## What’s inside

- **A\_Curvature\_Program\_Status.md**  
  A cleaned blueprint: how local convexity / Bakry–Émery curvature, tails, and coarse-graining could imply a finite-cutoff gap; what is proven vs conjectured; and the continuum “race condition” bottlenecks.

- **B\_vHJ\_Hessian\_Flow.md**  
  Derivation of the viscous Hamilton–Jacobi (vHJ) equation and the exact Hessian evolution PDE.  
  Includes a careful note about *what the sign actually implies* (no fake “automatic restoration” claim).

- **C\_Polarity\_Capacity\_Gribov.md**  
  The Gaussian polarity / capacity-comparison approach to treating Gribov and reducible strata as analytically negligible (capacity-zero / polar sets), plus what still needs checking.

- **D\_Haar\_Jacobian\_SmallField.md**  
  A rigorous small-field expansion for the Haar Jacobian in exponential coordinates, and a clean “Haar Hessian lemma” with normalization bookkeeping.

- **E\_SU3\_Convexity\_Engine\_and\_Results.md**  
  The JAX SU(3) **convexity scanner** (HVP + Lanczos) and the actual **L=4,6,8** scan results (β × scale grid), plus derived “effective constants” from the boundary.  
  Also includes a **corrected plan** for estimating the Wilson Hessian constant \(C_W\) numerically.

- **F\_qRacah\_Doob\_Tq\_and\_q6j.md**  
  The q-Racah Doob toy model + q-flow “safe region” numerics, composite transfer operator \(T_q\), and the q–6j classical-limit error bound.

- **G\_Checklist\_OpenProblems.md**  
  A practical checklist of analytic tasks, explicitly marking which ones look *tractable now* vs *frontier open problems*.

## Quick-start (if you just want to reproduce the main SU(3) data)

The “convexity scan” is fully contained in **E\_SU3\_Convexity\_Engine\_and\_Results.md**, and includes:

- A **drop-in JAX script** for the scan
- The printed output tables for L=4,6,8
- Plotting code to compare \(L\)

## Conventions note

The Haar quadratic coefficient depends on **Lie algebra normalization** (choice of basis and inner product).  
This export keeps the **symbolic** coefficient explicit whenever possible, and only plugs numbers when the normalization is clearly specified.

---
End of README.
