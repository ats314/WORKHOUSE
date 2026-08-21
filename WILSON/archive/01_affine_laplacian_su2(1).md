# Affine Laplacian Law and Split-Half Generator Decomposition in 4D SU(2)

## 1. Setup and notation

We consider a 4D periodic hypercubic lattice with link variables
\[
U_{x,\mu}\in {\rm SU}(2),\qquad \mu\in\{0,1,2,3\}.
\]
Let each plaquette be
\[
U_p = U_{x,\mu}U_{x+\hat\mu,\nu}U_{x+\hat\nu,\mu}^{-1}U_{x,\nu}^{-1}.
\]
Define the plaquette “energy density”
\[
B_p := 1 - \tfrac12 \mathrm{Re}\,\mathrm{Tr}(U_p),
\qquad
B_{\rm avg} := \frac{1}{N_p}\sum_p B_p.
\]
The project defines the tracked observable
\[
\bar V := 1 + B_{\rm avg}.
\]

For an overdamped SU(2) Langevin diffusion with potential \(S(U)\) (Wilson-type action),
the standard generator has the schematic form
\[
(\mathcal L f)(U) = \Delta f(U) - \langle \nabla S(U),\,\nabla f(U)\rangle,
\]
where \(\Delta\) is the configuration-space Laplace--Beltrami operator (sum over links),
and \(\langle\cdot,\cdot\rangle\) is the induced Riemannian inner product on tangent vectors.

The project computes Monte Carlo estimates of:

- \(\Delta \bar V(U)\) (called `lap`),
- \(\langle \nabla S,\nabla\bar V\rangle(U)\) (called `gip`),
- \((\mathcal L \bar V)(U)\) (called `LV`),

and then tests the decomposition:
\[
\boxed{
\mathcal L \bar V \stackrel{?}{=} \Delta \bar V - \langle \nabla S, \nabla \bar V\rangle
}.
\]

---

## 2. Empirical “Affine Laplacian Law”

### Observation

Across lattice sizes \(L\in\{8,12,16\}\), the data are extremely well fit by an affine law
\[
\boxed{
\Delta \bar V(U)\;\approx\; a + b\,B_{\rm avg}(U)
}
\qquad\text{with}\qquad
a\approx 12,\;\; b\approx -12.
\]
Equivalently,
\[
\Delta \bar V(U) \approx 12\,[1 - B_{\rm avg}(U)].
\]

This is striking because \(12=D(D-1)\) for \(D=4\).

### Evidence (L=12 fit)

One run reports the fit
\[
\Delta \bar V \approx a + b\,B_{\rm avg},
\qquad
\hat a=11.999259,\;\hat b=-11.999253,
\qquad
R^2=0.999999871795.
\]

### Evidence (cross-\(L\) summary)

A cross-\(L\) summary table reports:

| \(L\) | \(\hat a\) | \(\hat b\) | \(R^2\) | \(\max|\Delta \bar V - (12-12B_{\rm avg})|\) |
|---:|---:|---:|---:|---:|
| 8  | 11.999129 | -11.998889 | 0.999999 | \(1.92\times 10^{-2}\) |
| 12 | 11.999289 | -11.999223 | 1.000000 | \(8.34\times 10^{-3}\) |
| 16 | 11.999174 | -11.999189 | 1.000000 | \(5.10\times 10^{-3}\) |

---

## 3. Split-half decomposition test

### Why split-half matters

If one computes `LV` and then defines `LV := lap - gip` with the same random samples,
the identity holds tautologically and proves nothing.

Instead, the code uses **split-half MC**: compute `LV` from the first half of MC samples, and compute `(lap - gip)` from the second half, producing a residual
\[
r(U)=\mathrm{LV}_{\rm (half1)}(U)-(\mathrm{lap}-\mathrm{gip})_{\rm (half2)}(U),
\]
then standardizes by an estimated standard error to obtain a z-score.

### Typical outcome

The z-scores are close to standard normal, consistent with the generator identity being correct and the residual being just MC noise.

Example (reported values):

- For \(L=8\): \(\mathrm{mean}(z)=-0.0102\), \(\mathrm{std}(z)=0.9856\), and \(\Pr(|z|>2)\approx 3.66\%\).
- For \(L=16\): \(\mathrm{mean}(z)=0.0176\), \(\mathrm{std}(z)=0.9916\), and \(\Pr(|z|>2)\approx 4.69\%\).

---

## 4. Sign test for the gradient pairing

The project also checks the sign of the pairing term:
\[
\langle \nabla S,\nabla \bar V\rangle(U).
\]
A sign test reported, e.g. for \(L=8\) and \(L=16\), that *all* samples were positive (no negatives, no zeros), producing an astronomically small two-sided sign-test p-value (reported as \(\log_{10}p\approx -616.2\)).

This is consistent with \(\bar V\) being (almost) a monotone function of the same plaquette functional appearing in \(S\), so their gradients align.

---

## 5. Why the affine Laplacian law is “proof-adjacent”

The decomposition identity \(\mathcal L f = \Delta f - \langle\nabla S,\nabla f\rangle\) is standard for Langevin diffusions on manifolds.

The surprising part is the *special observable* \(\bar V=1+B_{\rm avg}\) yielding an almost-perfect affine Laplacian relationship with coefficients locked to \(12\).

A plausible analytic route:

1. Express each plaquette term \(B_p\) in terms of SU(2) characters \(\chi_{1/2}\) (fundamental representation).
2. Use the eigenfunction property of characters under the SU(2) Laplace--Beltrami operator:
   \[
   \Delta_{\rm SU(2)} \chi_j = -j(j+1)\chi_j.
   \]
3. Track how the configuration-space Laplacian (sum over links) acts on a plaquette product and then on the lattice average.
4. Show the resulting coefficient is exactly \(D(D-1)\) in \(D\) dimensions under the project’s normalization.

If this can be made exact, then \(\bar V\) becomes a “calibrated” observable with an analytically tractable Laplacian—useful for Lyapunov/drift arguments.

---

## 6. Minimal reproducibility skeleton (high-level)

The full implementation in the project uses GPU streaming + MC chunking; the core logic is:

```python
# Pseudocode / skeleton (not the full optimized implementation)

def Bavg(U):
    # compute average plaquette energy density
    return mean_over_plaquettes(1 - 0.5*ReTr(plaquette(U)))

def Vbar(U):
    return 1 + Bavg(U)

def laplacian_estimate(U, mc_samples):
    # sample tangent directions Xi and compute second directional derivative via FD
    return MC_average(second_dir_derivative(Vbar, U, Xi))

def gradpair_estimate(U, mc_samples):
    # estimate <∇S,∇V> via directional derivatives of S and V along same Xi
    return MC_average(dir_derivative(S,U,Xi) * dir_derivative(Vbar,U,Xi))

def generator_estimate(U, mc_samples):
    return laplacian_estimate(U, mc_samples) - gradpair_estimate(U, mc_samples)

# split-half test:
LV_half1  = generator_estimate(U, Xi[:mc//2])
lap_half2 = laplacian_estimate(U, Xi[mc//2:])
gip_half2 = gradpair_estimate(U, Xi[mc//2:])
z = (LV_half1 - (lap_half2 - gip_half2)) / SE_estimate(...)
```

---

## 7. Next steps

1. **Prove the affine law** (or determine precisely what normalization makes it exact).
2. Test whether the coefficient becomes \(D(D-1)\) for other \(D\) (e.g., 2D, 3D).
3. Extend from SU(2) to SU(3): do we get an affine law with a different pinned constant?
4. Use the affine law as an ingredient in a **core-set drift inequality**, which is the right structure for Harris-type geometric ergodicity proofs.
