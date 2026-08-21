# Core-Set Lyapunov Certificate for 4D SU(2): Negative Drift Outside a Threshold

## 1. Why a “core set” is the right shape

A global drift inequality of the form
\[
\mathcal L \bar V \le -\lambda \bar V + b
\]
is often too strong (and frequently false) on large compact manifolds with complicated energy landscapes.

The Harris/Foster--Lyapunov strategy replaces it with a **core-set** (a “small set”):
\[
\mathcal L \bar V \le -\lambda \bar V + b
\quad\text{on}\quad \Omega\setminus C,
\]
plus a separate minorization/recurrence condition on \(C\).

The project’s observable \(\bar V = 1 + B_{\rm avg}\) is naturally paired with a core defined by a threshold on
\[
B_{\rm avg} = \bar V - 1.
\]

---

## 2. Quantities used in the certificate

The project computes (with estimated standard errors):

- `lap` \(\approx \Delta \bar V\),
- `gip` \(\approx \langle\nabla S,\nabla \bar V\rangle\),
- `LV` \(\approx \mathcal L \bar V = \mathrm{lap}-\mathrm{gip}\).

It then studies **ratio and envelope bounds** designed to avoid trivial “huge slope + huge intercept” fits.

---

## 3. A uniform-in-\(L\) candidate threshold

One run reports a concrete candidate (described as “uniform L candidate”):

\[
\boxed{\tau_0 = 0.3883,\qquad c_{\min}\approx 20.95,\qquad d_{\max}\approx -2.6909.}
\]

This is summarized as:

- “Targets met” at \(\tau_0=0.3883\) with \(c_{\min,{\rm phys}}=20.95\) and \(d_{\max,{\rm phys}}=-2.6909\).

Interpretation (project intent): on the set \(\{B_{\rm avg}\ge \tau\}\), the gradient pairing obeys a coercive lower bound
\[
\langle\nabla S,\nabla\bar V\rangle \gtrsim c_{\min}\,B_{\rm avg},
\]
strong enough to overcome the Laplacian term and force negative drift.

---

## 4. Combining with the affine Laplacian law ⇒ explicit negative drift

Using the empirical affine Laplacian law
\[
\Delta \bar V \approx 12 - 12 B_{\rm avg},
\]
and the coercivity bound on \(\{B_{\rm avg}\ge\tau_0\}\):
\[
\langle\nabla S,\nabla\bar V\rangle \ge c_{\min}\, B_{\rm avg},
\]
we obtain, for \(B_{\rm avg}\ge\tau_0\),
\[
\mathcal L \bar V
= \Delta\bar V - \langle\nabla S,\nabla\bar V\rangle
\;\le\;
12 - (12+c_{\min})B_{\rm avg}.
\]
In particular,
\[
\mathcal L \bar V \le 12 - (12+c_{\min})\tau_0.
\]
Plugging in \(\tau_0=0.3883\) and \(c_{\min}=20.95\) yields a strictly negative constant bound.

This is the shape one needs for a Lyapunov drift away from the core \(\{B_{\rm avg}<\tau_0\}\).

---

## 5. “Offender” configurations and topology suspicion

The run also flags unusually bad configurations (large required \(b\)) and exports metadata.

One example described in the log:

- `idx=1610`, kind=`haar`, with \(B_{\rm avg}\approx 1.0009\) and \(\mathrm{LV}\approx 11.9992\),
  standard error \(\approx 2.2719\), and a computed `required_b ≈ 27.5527`.

Such outliers are consistent with rare geometric/topological obstructions (e.g., a wrapping defect/domain wall on the 4-torus), though confirming that requires explicit topology diagnostics.

---

## 6. How to turn the certificate into a theorem (research program)

To upgrade this from an empirical certificate to a theorem, you’d typically need:

1. **Exact affine Laplacian law** (or a controlled inequality version).
2. A **deterministic lower bound** on \(\langle\nabla S,\nabla\bar V\rangle\) on \(\{B_{\rm avg}\ge \tau_0\}\).  
   One possible route: relate the pairing to a Dirichlet form, and prove coercivity using spectral bounds on a Hessian-like operator.
3. A **minorization / small set condition** on the core \(C=\{B_{\rm avg}<\tau_0\}\).  
   On compact groups, one often proves that the diffusion kernel has a smooth strictly positive density after any \(t>0\), but in huge dimensions the constants may be tiny; still, positivity plus recurrence is enough qualitatively.
4. Apply a **Harris theorem** to conclude geometric ergodicity and (with more work) a spectral gap.

---

## 7. Practical follow-ups (numerical but “theorem-guided”)

1. Verify \((\tau_0,c_{\min})\) is stable in:
   - \(\beta\),
   - lattice size \(L\),
   - dataset mixture (sigma-noise vs Haar).
2. Repeat with:
   - SU(3),
   - different observables (e.g., smeared plaquette),
   - different normalizations of \(\Delta\).
3. Isolate “offenders” and run:
   - smoothing/flow,
   - homology or defect-wrapping detection,
   - action barrier estimates.

If the offenders correspond to a distinct topological sector, then the right theorem might be: **geometric ergodicity holds within each sector**, with exponentially slow tunneling between sectors (a metastability picture).
