# SU(3) Wilson Action: Volume-Stable Convex Core from Hessian Minimum-Eigenvalue Scans

This document extracts the clearest SU(3) result with “mass-gap flavor”:
a multi-volume scan showing a stable region in field amplitude where the Wilson action Hessian appears positive.

## 1. Setup (as implemented in the project)

- Gauge group: \(\mathrm{SU}(3)\)
- Lattice: 4D periodic \(L^4\)
- Link parametrization: \(U=\exp(A)\) with \(A\in\mathfrak{su}(3)\) represented by an 8-vector of coefficients.
- Action: Wilson plaquette action (sum over plaquettes of \(1-\frac13\mathrm{ReTr}(U_p)\)) with inverse coupling \(\beta\).

The code constructs a random field at a controlled amplitude scale \(s\):
\[
\theta \sim s\,\mathcal N(0,1),
\]
builds links \(U(\theta)\), computes the action \(S(\theta)\), and estimates the **minimum eigenvalue of the Hessian**
\(\lambda_{\min}(\nabla^2 S)\) via a Lanczos routine.

Interpretation:
- \(\lambda_{\min}>0\): locally convex (no negative curvature directions)
- \(\lambda_{\min}<0\): locally nonconvex (tachyonic/unstable direction in this local quadratic model)

## 2. Empirical results (exported arrays)

For three volumes \(L\in\{4,6,8\}\), the project file `12-3-25 CODE RUN.txt` contains reconstructed results.
Each tuple is \((\beta,\; s,\; \lambda_{\min})\).

### L = 4 (selected)
\[
\begin{array}{c|ccc}
\beta & s=0.05 & s=0.10 & s=0.15\\\hline
0.40 & +0.1076 & +0.0849 & +0.0602\\
0.77 & +0.0910 & +0.0497 & +0.0006\\
1.14 & +0.0740 & +0.0115 & -0.0637\\
1.51 & +0.0586 & -0.0283 & -0.1219\\
1.89 & +0.0428 & -0.0613 & -0.1729\\
2.26 & +0.0250 & -0.0978 & -0.2300\\
2.63 & +0.0061 & -0.1320 & -0.2871\\
3.00 & -0.0082 & -0.1722 & -0.3766\\
\end{array}
\]

### L = 6 (selected)
\[
\begin{array}{c|ccc}
\beta & s=0.05 & s=0.10 & s=0.15\\\hline
0.40 & +0.1090 & +0.0874 & +0.0631\\
0.77 & +0.0938 & +0.0527 & +0.0067\\
1.14 & +0.0791 & +0.0165 & -0.0528\\
1.51 & +0.0635 & -0.0171 & -0.1119\\
1.89 & +0.0488 & -0.0565 & -0.1738\\
2.26 & +0.0339 & -0.0857 & -0.2326\\
2.63 & +0.0187 & -0.1206 & -0.2789\\
3.00 & +0.0034 & -0.1549 & -0.3482\\
\end{array}
\]

### L = 8 (scale 0.05 only, selected)
\[
(\beta,0.05,\lambda_{\min}) \in
\{(0.40,+0.1092),(0.77,+0.0943),(1.14,+0.0800),(1.51,+0.0647),(1.89,+0.0504),(2.26,+0.0354),(2.63,+0.0216),(3.00,+0.0065)\}.
\]

## 3. What is “novel” here?

The striking feature is **volume stability**:

- For fixed amplitude \(s=0.05\), \(\lambda_{\min}(\beta)\) is nearly identical across \(L=4,6,8\).
- The transition to negative curvature occurs primarily by increasing \(s\) (field amplitude) and/or \(\beta\),
  not by increasing volume (at least in this scan range).

Working theory:
- There exists a **convex core** in configuration space that is robust as volume increases.
- This is precisely the kind of local coercivity one needs for Bakry–Émery / Lyapunov-based approaches to mixing and mass-gap-like behavior.

## 4. Suggested next runs (to turn “convex core” into a quantitative theorem candidate)

1. **Increase \(L\)** (e.g. 10, 12) but keep the same \(s\) grid.
2. **Increase sample count** at each \((\beta,s)\) to estimate uncertainty on \(\lambda_{\min}\).
3. **Replace random Gaussian fields by structured excitations** (single-plaquette flux, plane waves, instanton-like seeds)
   to map the shape of the convex core boundary.
4. **Measure how the Hessian spectrum organizes into plateaus** (connect to `04_su3_plaquette_hessian_quantization.md`).
5. **Connect to dynamics:** run a short Langevin evolution and measure escape time from the convex core as a function of \(\beta\) and \(L\).

If the convex core remains stable and the escape time grows with \(\beta\), that becomes a concrete “route” toward mass-gap style statements.
