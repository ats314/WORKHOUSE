# Exponential Decay Bounds for Lattice Green’s Functions (Combes–Thomas / Graph Bounds)

## What this note extracts

Two different but related numerical experiments test **exponential decay** bounds for lattice Green’s functions:

1. A **link-field propagator** constructed in Fourier space with an explicit gauge projector (a “Proposition 9.X / 9.X'” check).
2. A simpler **scalar massive Laplacian** propagator on \(T^d\) measured by shell envelopes and compared with a **Combes–Thomas exponent**.

The key result: the measured envelope slopes are typically **much larger** than the conservative Combes–Thomas exponent, i.e. the bound is safe but loose.

---

## 1. Model operators

### 1.1 Scalar model on \(T^d\)

Let \(\Delta\) be the standard discrete Laplacian on an \(L^d\) periodic grid. Consider
\[
M = m^2 I + \alpha \Delta,
\qquad
G = M^{-1}.
\]
Fourier space gives
\[
\widehat{G}(p)=\frac{1}{m^2+\alpha \,\widehat{\Delta}(p)}.
\]

### 1.2 Gauge-fixed link propagator (1-form structure)

A vector (link) propagator in momentum space typically decomposes into transverse and longitudinal parts:
\[
M^{-1}_{\mu\nu}(p) =
\frac{1}{m^2+\alpha p^2}\,P^T_{\mu\nu}(p)
+
\frac{1}{m^2}\,P^L_{\mu\nu}(p),
\]
or in a Feynman-gauge variant with \(\xi\) replacing the longitudinal massless piece.

The project files build these projectors explicitly using \(\hat p_\mu = 2\sin(p_\mu/2)\) and
\[
P^L_{\mu\nu} = \frac{\hat p_\mu \hat p_\nu}{\hat p^2}.
\]

---

## 2. A generic exponential decay statement

A common form of Combes–Thomas (CT) bounds is:
\[
|G(x)| \le C \exp(-\eta\, \text{dist}(x,0)),
\]
for some metric \(\text{dist}\) and exponent \(\eta>0\) depending on \(m,\alpha\) and on operator norms like row sums / bandwidth.

A very conservative CT-type exponent used in the project is
\[
\eta_{\rm CT}(m^2,\alpha) = \log\!\Bigl(1+\frac{m^2}{2\alpha C_0}\Bigr),
\]
where \(C_0\) is a row-sum constant for the underlying Laplacian-like operator.

---

## 3. Link-propagator “Proposition 9.X” numeric verification (FFT + BFS)

One experiment constructs:

- a link adjacency graph (two links are neighbors if they share a plaquette),
- graph distances \(\mathrm{dist}_E(b,b_0)\) by BFS,
- the propagator \(G_{\mu\nu}(x)\) by inverse FFT,
- and a constant \(C_0\) by inverse FFT of the 1-form Laplacian symbol and taking a max row sum.

Example parameters:

- \(L=16\), \(d=4\)
- \(m^2=0.3\), \(\alpha=1.0\)
- BFS yields max degree \(D_E=18\)
- computed \(C_0(\Delta_1)\approx 43.9077\)

Three candidate exponents were computed:

\[
\eta_{\rm DG}(D_E)=2\sinh^{-1}\!\Bigl(\frac{m}{2\sqrt{\alpha D_E}}\Bigr),\qquad
\eta_{\rm DG}(C_0)=2\sinh^{-1}\!\Bigl(\frac{m}{2\sqrt{\alpha C_0}}\Bigr),
\]
\[
\eta_{\rm CT}(C_0)=\log\!\Bigl(1+\frac{m^2}{2\alpha C_0}\Bigr).
\]

The check evaluates the ratio
\[
R(b)= \frac{m^2}{2}\,|G_{b,b_0}|\,e^{\eta\,\mathrm{dist}_E(b,b_0)},
\]
and reports \(\max_b R(b)\). If \(\max R\le 1\), the bound holds with prefactor \(2/m^2\).

In the shown run, all three choices produced \(\max R \approx 0.1412\), with the maximum occurring at distance \(0\), so the bound is easily satisfied (though that makes it a weak test of the exponent itself).

---

## 4. Shell-envelope slopes vs CT exponent (FFT on \(T^4\))

A second experiment studies the scalar \(G(x)\) on \(T^4\), but *measures* decay by:

1. computing the envelope by \(\ell_1\) shells:
   \[
   \mathrm{env}(r)=\max_{\|x\|_1=r} |G(x)|,
   \]
2. computing local slopes
   \[
   s(r+\tfrac12) = -\log \mathrm{env}(r+1)+\log \mathrm{env}(r),
   \]
3. taking a median slope over a window \(r\in[r_{\min}, r_{\max}]\):
   \[
   c_{\rm shell} := \mathrm{median}\{s(r): r_{\min}\le r\le r_{\max}\}.
   \]

Then it compares \(c_{\rm shell}\) to a CT exponent using a particular \(C_0\) specialization (noted in-file as “\(R=1, C_0=8\)”):
\[
\eta_{\rm CT}=\log\!\Bigl(1+\frac{m^2}{16\alpha}\Bigr).
\]

Example results (device=cuda, \(d=4\), \(L=64\), \(\alpha=1\), slope window \(r\in[6,20]\)):

| \(m^2\) | \(c_{\rm shell}\) | \(\eta_{\rm CT}\) | \(c_{\rm shell}/\eta_{\rm CT}\) |
|---:|---:|---:|---:|
| 0.05 | 0.22713 | 0.003120 | 72.8 |
| 0.10 | 0.27489 | 0.006231 | 44.1 |
| 0.20 | 0.34319 | 0.012423 | 27.6 |
| 0.30 | 0.39035 | 0.018576 | 21.0 |
| 0.50 | 0.45451 | 0.030772 | 14.8 |
| 1.00 | 0.59238 | 0.060625 | 9.77 |

So the CT exponent is extremely conservative here; the observed envelope decay is much faster.

---

## 5. Why this matters

If one is trying to build a **mass gap / clustering** argument, one repeatedly needs statements like:

- “a Green’s function decays exponentially with a rate controlled from below by \(m\) (or by some effective mass).”

CT-type bounds are attractive because they can be made **nonperturbative** and work for large classes of operators.  
The experiments suggest the bound is likely safe but may be far from sharp; sharpening \(\eta\) would pay off directly in any “constant-chasing” proof skeleton.

---

## 6. Next steps that would increase proof-relevance

1. Ensure the *max ratio* test actually stresses large distances (e.g. normalize away the \(r=0\) dominance; test sup over \(r\ge r_0\)).
2. Compare different metrics: \(\ell_1\) shells, graph distance, Euclidean distance on the torus.
3. Extend to random-coefficient elliptic operators (quenched disorder), which is closer to gauge backgrounds after gauge-fixing.
4. Systematically estimate the best exponent \(c\) from data and compare to candidate theoretical \(\eta\) formulas.

---

## Sources used

- `RUN 125.pdf` (link-graph BFS + FFT propagator + constants \(D_E\), \(C_0\); exponent definitions).
- `RUN 122.pdf` (shell-envelope slope method; CT exponent comparison table).
