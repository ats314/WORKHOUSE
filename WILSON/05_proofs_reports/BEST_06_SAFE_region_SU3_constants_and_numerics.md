# SAFE-Region SU(3) Constants and Numerics (Extracted + Reproducible)

This note collects the **explicit numerical constants** that your proof architecture tries to pin down, and includes a small reproducible scan script.

The project is unusually “engineering-minded” here: it wants concrete numbers like
\(\kappa_*\), \(\delta\), and \(\alpha\) that make the RG/LSI bookkeeping checkable.

---

## 1. The constants you keep using

You repeatedly use a SAFE ball radius
\[
R_0 = 0.05
\]
(in right-invariant exponential coordinates).

On this ball you want:

1. A **Haar / group-geometry convexity floor**
\[
\kappa_* \approx 0.25,
\]
interpreted as a curvature/convexity lower bound in the physical sector.

2. A **Wilson Hessian variation bound**
\[
\delta \approx 0.006,
\]
an upper bound on “how much the Wilson term can eat your convexity” in the SAFE region.

3. An **RG degradation factor**
\[
\alpha := \frac{\kappa_*-\delta}{\kappa_*} \approx 0.976.
\]

---

## 2. The project’s SU(3) Haar curvature scan (as stated in the notes)

The project file reports the following scan for a Haar-induced curvature proxy on \(SU(3)\) (minimum eigenvalue over random samples inside balls of radius \(r\)):

| radius \(r\) | min eigenvalue estimate |
|---:|---:|
| 0.00 | 0.291 |
| 0.01 | 0.275 |
| 0.02 | 0.265 |
| 0.03 | 0.260 |
| 0.04 | 0.257 |
| 0.05 | 0.255 |

and the reported global minimum over the SAFE ball:
\[
\min_{r\le 0.05}\lambda_{\min} \approx 0.252.
\]

Based on this, the notes adopt:
\[
\boxed{\kappa_* = 0.25.}
\]

---

## 3. Wilson Hessian error terms and the \(\delta\) ledger (as stated)

The same notes then estimate BCH/commutator remainder coefficients (example values quoted):

- \(C_2 \approx 0.011\)
- \(C_3 \approx 0.10\)
- \(C_4 \approx 1.1\)

and use them to produce a uniform SAFE-region bound:
\[
\boxed{\delta \approx 0.006, \qquad \alpha \approx 0.976.}
\]

One “engineering” interpretation: \(\alpha\) is the per-RG-step fractional retention of convexity.

---

## 4. A reproducible scan: Haar Jacobian potential Hessian (toy proxy)

Below is a small Python script that:

- builds an orthonormal basis for \(\mathfrak{su}(3)\),
- defines the “Haar Jacobian potential”
  \[
  V(X) = \sum_j \log\!\frac{s_j/2}{\sin(s_j/2)}
  \]
  where \(s_j\) are the singular values of \(\mathrm{ad}_X\),
- and estimates the minimum eigenvalue of the Euclidean Hessian of \(V\) via finite differences
  at random points \(X\) with \(\|X\|\le r\).

**Important:** this is a *proxy* computation in coordinates; depending on how you normalize BE curvature vs coordinate Hessians, you may need a conversion factor. It is still useful as a sanity check that the Haar term is strongly convex near the identity.

### Script
See: `haar_hessian_scan_su3.py` (included in the download set).

### Example output (from one run)
```
r=0.000: min eig ~ 0.500000000
r=0.010: min eig ~ 0.500001233
r=0.020: min eig ~ 0.500004961
r=0.030: min eig ~ 0.500011202
r=0.040: min eig ~ 0.500019993
r=0.050: min eig ~ 0.500031245
```

This suggests the scanned Hessian proxy is extremely flat in \(r\) at this resolution and comfortably positive.

---

## 5. What’s “publishable” about this constants module

Even setting the Clay claim aside, this constants work is valuable because it produces:

- explicit numeric convexity floors for compact group geometry,
- explicit BCH/commutator remainder bounds in a SAFE ball,
- and a quantitative framework to track what happens under coarse-graining.

That kind of explicitness is rare in mass-gap-level discussion, and it can be split into standalone notes/papers.

---

## 6. What would make this module stronger

If you want these constants to be “no-excuses” rigorous:

1. Replace random scanning by deterministic lower bounds (root-system formulas + analytic monotonicity).
2. State all normalizations (metric, basis, coordinate chart, Haar Jacobian definition) in one place.
3. Prove the Wilson BCH remainder bounds as inequalities with certified constants.
4. Prove the SAFE region is visited with high probability under \(\mu_\Lambda\) (ties into the Lyapunov module).
