# Block convexity, coarse-graining, and an MFIP-style recursion for gap persistence

## This is the speculative-but-structured part

The earlier pieces yield a **finite-cutoff** lower bound \(\rho_*(a)\) on (horizontal) convexity.  
This section extracts the project’s attempt to turn that into a *multi-scale* statement: after repeated coarse-graining / RG steps, does a strictly positive lower bound survive?

The key technical object is a matrix inequality for the Hessian of a marginal (coarse) effective action, which is basically a Schur-complement story dressed as RG.

---

## 1. Coarse-graining as a block decomposition

Split variables into coarse/IR (\(x\)) and fine/UV (\(y\)), and write a joint effective action
\[
S(x,y).
\]

Block the Hessian:
\[
\nabla^2 S=
\begin{pmatrix}
A & B\\
B^\top & C
\end{pmatrix},
\]
where \(A=\nabla_x^2 S\), \(C=\nabla_y^2 S\), \(B=\nabla_x\nabla_y S\).

Assume:
- \(A\succeq \alpha I\),
- \(C\succeq \gamma I\),
- \(\|B\|\le M\).

---

## 2. Hessian bound for the *marginal* effective action

Define the coarse density \(\rho_{\mathrm{coarse}}(x)=\int e^{-S(x,y)}dy\), and the coarse effective action
\[
S_{\mathrm{coarse}}(x):=-\log \int e^{-S(x,y)}dy.
\]

A standard computation (and a place where Brascamp–Lieb-type inequalities enter) yields
\[
\nabla_x^2 S_{\mathrm{coarse}}(x)
\succeq A - B C^{-1}B^\top.
\]

Using \(C^{-1}\preceq \gamma^{-1}I\), one gets
\[
\nabla_x^2 S_{\mathrm{coarse}}(x)
\succeq \alpha I - \gamma^{-1} B B^\top
\succeq \left(\alpha - \frac{M^2}{\gamma}\right)I.
\]

A natural symmetric choice is \(\alpha=\gamma=\rho_*\), giving
\[
\boxed{\;\rho_{\mathrm{new}}
\;\ge\;\rho_* - \frac{M^2}{\rho_*}
=\frac{\rho_*^2-M^2}{\rho_*}.\;}
\]

So convexity survives one block step if \(\rho_*>M\).

---

## 3. Iteration and a recursion

Let \(\rho_j\) be the convexity constant after \(j\) RG steps.  
A stylized recursion is:
\[
\rho_{j+1} \;\ge\; \rho_j - \frac{M_j^2}{\rho_j} - \varepsilon_j,
\]
where
- \(M_j\) controls cross-scale couplings,
- \(\varepsilon_j\) are truncation / approximation / non-idealities (a catch-all error term).

The project’s **Conjecture A** is essentially that \(\sum_j \varepsilon_j <\infty\) (summable error).

---

## 4. MFIP-style fixed point and “anomaly source” condition

The project also records a more “solved-form” persistence condition (a fixed-point inequality):
\[
\rho_* := \frac{\sigma_* - \varepsilon_\infty}{1-K} > 0,
\]
where
- \(\sigma_*\) is a positive “source” term (heuristically: curvature/anomaly that keeps feeding convexity),
- \(\varepsilon_\infty\) is the limiting total error,
- \(K\in(0,1)\) is a contraction factor for the recursion.

Interpretation:
- If the recursion is contractive enough (\(K<1\)),
- and the positive source dominates the accumulated error,
then the fixed point stays positive, i.e. there is a **persistent mass scale** after infinitely many RG steps.

---

## 5. The geometric–spectral stability hypothesis (what needs proving)

The project hints at a conjectural mechanism (“geometric–spectral stability”) that would supply the required \(\sigma_*>0\) even as the explicit Haar mass term vanishes with \(a\to 0\).

To make this non-handwavy, one would want:

1. A precise identification of \(\sigma(t)\) in the Riccati inequality coming from the vHJ/RG flow on the gauge configuration manifold.
2. A proof that \(\sigma(t)\) has a strictly positive lower bound along the renormalization trajectory \(\beta(a)\).
3. Uniform bounds on the cross terms \(M_j\) compatible with asymptotic freedom.

This is a plausible research direction: the *structure* is clear; the hard analysis is in verifying the hypotheses in a true 4D \(SU(N)\) RG scheme.