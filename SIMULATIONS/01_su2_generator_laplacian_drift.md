# SU(2) Drift Proofs: Affine Laplacian Law, Generator Decomposition, and Volume/Beta Stability

## 1. Definitions (as used in the simulations)

We consider a 4D periodic lattice of linear size \(L\) with link variables
\[
U_\ell \in \mathrm{SU}(2),\qquad \ell\in\text{links}.
\]
Let the Wilson action be
\[
S[U] \;=\; \beta\sum_{p}\Big(1-\tfrac12\operatorname{Re}\operatorname{Tr}(U_p)\Big),
\qquad U_p=\prod_{\ell\in\partial p} U_\ell.
\]

Define the **plaquette defect**
\[
B_p(U)\;:=\; 1-\tfrac12\operatorname{Re}\operatorname{Tr}(U_p),
\qquad
B_{\rm avg}(U)\;:=\;\frac{1}{N_p}\sum_p B_p(U),
\]
and the **Lyapunov candidate**
\[
V(U)\;:=\;1 + B_{\rm avg}(U).
\]

The simulation pipeline estimates, for each configuration \(U\),

- \(\Delta V\): the (configuration-space) Laplace–Beltrami operator applied to \(V\)  
  (estimated by finite differences along random Haar directions).
- \(gip := \langle \nabla S, \nabla V\rangle\) (estimated by Monte Carlo directional derivatives).
- \(LV := \mathcal L V\), the **drift / generator application** (estimated by a split-half test and by checking the identity below).

## 2. Proof A (structural): affine Laplacian law for the plaquette defect

### Proposition A.1 (single plaquette)
Let \(B_p(U)=1-w(U_p)\) where \(w\) is the scalar/character coordinate on \(\mathrm{SU}(2)\cong S^3\).
With the standard right-invariant Laplacian on \(\mathrm{SU}(2)\) normalized so that
\[
\Delta_{\mathrm{SU}(2)} w = -3 w,
\]
and with the configuration-space Laplacian \(\Delta\) defined as the sum of link Laplacians,
\[
\Delta \;=\;\sum_{\ell}\Delta_\ell,
\]
then for a plaquette \(p\) (which depends on 4 links),
\[
\Delta B_p \;=\; 12 - 12\,B_p.
\]

### Proof sketch
Fix three links in the plaquette and view \(U_p\) as a function of one remaining link:
\(U_p = A\,U_\ell\,B\) for fixed \(A,B\in \mathrm{SU}(2)\).
Then \(w(U_p)\) is a matrix element / character in the fundamental representation as a function of \(U_\ell\).
Right-invariance implies \(\Delta_\ell w(U_p) = -3 w(U_p)\) for each of the 4 links in \(\partial p\). Therefore,
\[
\Delta w(U_p)=\sum_{\ell\in\partial p}\Delta_\ell w(U_p)= -12\,w(U_p).
\]
Since \(B_p=1-w(U_p)\),
\[
\Delta B_p = -\Delta w(U_p)=12w(U_p)=12(1-B_p)=12-12B_p.\qedhere
\]

### Corollary A.2 (averaged defect)
By linearity,
\[
\Delta B_{\rm avg} \;=\; 12 - 12\,B_{\rm avg}.
\]

## 3. Proof B (structural): positivity and alignment of \(\langle\nabla S,\nabla V\rangle\)

### Proposition B.1
If \(S=\beta\sum_p B_p\) and \(V=1+\frac1{N_p}\sum_p B_p\), then
\[
\nabla S \;=\; \beta\,\nabla\Big(\sum_p B_p\Big),\qquad
\nabla V \;=\; \frac{1}{N_p}\,\nabla\Big(\sum_p B_p\Big),
\]
and therefore
\[
\langle\nabla S,\nabla V\rangle \;=\; \frac{\beta}{N_p}\,\Big\|\nabla\Big(\sum_p B_p\Big)\Big\|^2 \;\ge\;0,
\]
with equality only when \(\nabla(\sum_p B_p)=0\).

This explains two robust empirical facts:

- **sign test:** all observed values of \(gip\) were positive across thousands of configs;
- **alignment:** gradients \(\nabla S\) and \(\nabla V\) are (nearly) colinear.

## 4. Proof C (structural): the generator identity

The overdamped Langevin generator with invariant density proportional to \(e^{-S}\) is
\[
\mathcal L f \;=\; \Delta f \;-\;\langle \nabla S,\nabla f\rangle.
\]

### Proposition C.1 (candidate identity tested in simulations)
For the Lyapunov candidate \(V\),
\[
LV \;\stackrel{?}{=}\; \Delta V - \langle \nabla S,\nabla V\rangle \;=\; \Delta V - gip.
\]
The simulations check this **pointwise** via a split-half strategy:
estimate \(LV\) on one half of MC samples and \(\Delta V - gip\) on the other half, then test the normalized residual.

## 5. Empirical validation (from the chat runs)

### 5.1 Laplacian law persists across volume \(L\in\{8,12,16\}\)
A linear fit on HOLDOUT of the form
\[
\Delta V \approx a + b\,B_{\rm avg}
\]
yields approximately \(a\simeq 12\), \(b\simeq -12\) with \(R^2\approx 1\).  
The maximal deviation from the hypothesis \(\Delta V \approx 12-12B_{\rm avg}\) decreases with \(L\).

### 5.2 Decomposition test
For each \(L\), the split-half normalized residual \(z\) for
\(LV \approx \Delta V - gip\) is close to a standard normal:

- mean \(z\approx 0\), std \(z\approx 1\),
- max \(|z|\) around \(3.2\)–\(3.5\),
- no \(|z|>5\) outliers in the reported sweeps.

### 5.3 Drift certificate: negative drift outside a core set
A Foster–Lyapunov-style certificate is established on HOLDOUT on domains
\(\{B_{\rm avg}\ge \tau\}\) of the form
\[
LV + n_\sigma\,\mathrm{SE}(LV)\;\le\; -\lambda\,B_{\rm avg}.
\]
Empirically, for \(\beta=6\) the first certified domain appears near \(\tau\approx 0.216\) with \(\lambda\approx 10.76\),
and \(\lambda\) scales nearly linearly with \(\beta\) for \(\beta\ge 4\).

## 6. Next steps (what would strengthen this into a real theorem)

1. **Analytic normalization audit.**  
   Fix the precise Laplacian normalization used in code and match it to the group-theory eigenvalue
   for the fundamental character. This would turn “empirical =12” into an exact structural constant.

2. **Derive a deterministic drift bound outside a core.**  
   Combine the exact affine Laplacian law with a lower bound on
   \(\|\nabla(\sum_p B_p)\|^2\) in terms of \(B_{\rm avg}\) on \(\{B_{\rm avg}\ge\tau\}\).

3. **Upgrade to volume-uniform constants.**  
   Prove \(\tau,\lambda\) do not degrade with \(L\). Numerically, they appear stable for \(L=8,12,16\).

4. **Generalize to SU(3).**  
   Repeat the Laplacian-law derivation using Casimir eigenvalues in the fundamental representation.


## Appendix: key numerical summaries (copied from run outputs)

### A. L-sweep (β=6, mc=256, K_total=2048)

The project’s streamed L-sweep reported the following “structural checks”:

\[
\begin{array}{c|ccc|c|cc|cc}
L & \hat a & \hat b & R^2 & \max|\Delta V-(12-12B)| & \%(|z|>2) & \max|z| & \lambda_{\rm affine} & b_{\rm affine}\\\hline
8  & 11.999129 & -11.998889 & 0.9999993 & 1.9225\times 10^{-2} & 3.66\% & 3.231 & -30 & -17.975449\\
12 & 11.999289 & -11.999223 & 0.9999999 & 8.3439\times 10^{-3} & 4.30\% & 3.224 & -30 & -17.987228\\
16 & 11.999174 & -11.999189 & 1.0000000 & 5.1037\times 10^{-3} & 4.69\% & 3.498 & -30 & -17.994020\\
\end{array}
\]

Here \((\hat a,\hat b)\) are from fitting \(\Delta V \approx a + b\,B_{\rm avg}\),
and \(z\) is the split-half decomposition normalized residual for \(LV\approx \Delta V-gip\).
The “affine” \((\lambda,b)\) correspond to the separate drift-line fit reported in the same outputs.

### B. Ratio-style negative drift certificate (volume comparison)

A cleaned HOLDOUT-only report (constructed from `decomp_Lsweep_results.npz`) produced:

\[
\begin{array}{c|ccc}
L & \tau^\* & \lambda^\* & \text{coverage}\\\hline
8  & 0.2158 & 11.0012 & 68.9\%\\
12 & 0.2157 & 10.7230 & 70.2\%\\
16 & 0.2159 & 10.9799 & 70.8\%\\
\end{array}
\]

This is “volume-uniform” evidence: \(\tau^\*\) and \(\lambda^\*\) remain stable as \(L\) increases.

### C. β-sweep certificate (L=16)

For the HOLDOUT-domain certificate
\[
LV + 2\sigma \le -\lambda\,B_{\rm avg}\quad \text{on }\{B_{\rm avg}\ge\tau\},
\]
the run reported:

\[
\begin{array}{c|cc|c}
\beta & \tau_0 & \lambda_0 & \text{coverage at }\tau_0\\\hline
2  & 0.6361 & 2.1158 & 60.6\%\\
4  & 0.6361 & 7.1795 & 60.6\%\\
6  & 0.2158 & 10.7627 & 69.3\%\\
8  & 0.2158 & 14.3460 & 69.3\%\\
10 & 0.2158 & 17.9292 & 69.3\%\\
\end{array}
\]

For \(\beta\ge 4\), \(\lambda_0/\beta\) is approximately constant (\(\approx 1.79\) in this dataset),
which is exactly the sort of scaling one expects if the drift term is dominated by \(-\beta\langle\nabla(\sum B_p),\nabla V\rangle\).
