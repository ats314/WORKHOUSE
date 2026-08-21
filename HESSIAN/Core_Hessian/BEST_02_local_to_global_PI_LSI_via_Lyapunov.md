# Local-to-Global PI/LSI for Lattice Gauge Measures via Lyapunov Drift (Extracted)

This note extracts and rewrites (in a single place) the “**SAFE region + Lyapunov drift ⇒ global PI/LSI**” patching route that appears in the project proof attempt.

The point is to make the “convexity is the invariant” slogan literal:

\[
\text{(local convexity)} + \text{(drift control of tails)} \ \Longrightarrow\ \text{global functional inequality}.
\]

---

## 1. Setup: lattice gauge configuration manifold and diffusion

Let \(M_\Lambda = G^{E(\Lambda)}\) be the configuration manifold of link variables on a finite lattice \(\Lambda\) with compact gauge group \(G\) (e.g. \(SU(3)\)).

Let the lattice Gibbs measure be
\[
d\mu_\Lambda(U) = Z_\Lambda^{-1}\,e^{-S_\Lambda(U)}\,d\mathrm{vol}_{g_\Lambda}(U),
\]
where \(g_\Lambda\) is the product right-invariant metric.

Consider the reversible diffusion generator (overdamped Langevin / gradient diffusion)
\[
L_\Lambda f = \Delta_{g_\Lambda} f - \langle \nabla S_\Lambda,\nabla f\rangle.
\]

Write \(\Gamma_\Lambda(f)=|\nabla f|^2\) (carré du champ).

We are interested in PI/LSI **on the gauge-invariant sector**; for this note we suppress the projection and simply write “\(f\) gauge-invariant”.

---

## 2. Ingredient A: a “small-field” (SAFE) set with local PI/LSI

Assume there exists a compact gauge-invariant “small-field” region \(U_\Lambda\subset M_\Lambda\) (a SAFE ball) such that local functional inequalities hold on \(U_\Lambda\):

### Local PI on \(U_\Lambda\)
There exists \(C_{\mathrm{P,loc}}\) independent of \(\Lambda\) such that
\[
\int_{U_\Lambda} (f - f_{U_\Lambda})^2\, d\mu_\Lambda
\ \le\
C_{\mathrm{P,loc}} \int_{U_\Lambda} \Gamma_\Lambda(f)\,d\mu_\Lambda,
\]
where \(f_{U_\Lambda}\) is the \(U_\Lambda\)-average.

### Local LSI on \(U_\Lambda\)
There exists \(C_{\mathrm{LS,loc}}\) independent of \(\Lambda\) such that
\[
\mathrm{Ent}_{\mu_\Lambda}(f^2\mathbf 1_{U_\Lambda})
\ \le\
C_{\mathrm{LS,loc}} \int_{U_\Lambda} \Gamma_\Lambda(f)\,d\mu_\Lambda.
\]

(These are the standard outputs of a local Bakry–Émery curvature lower bound on \(U_\Lambda\).)

---

## 3. Ingredient B: Lyapunov drift controlling large-field excursions

Assume there exists a gauge-invariant Lyapunov function \(W_\Lambda\ge 1\) and constants \(\alpha>0\), \(\beta\ge 0\), independent of \(\Lambda\), such that

\[
\boxed{
L_\Lambda W_\Lambda \ \le\ -\alpha W_\Lambda + \beta\,\mathbf 1_{U_\Lambda}.
}\tag{LD}
\]

This implies (via Grönwall) a uniform bound on \(\int W_\Lambda\,d\mu_\Lambda\) and recurrence to \(U_\Lambda\).

---

## 4. The patching theorem (dimension-free form)

The project invokes the standard local-to-global functional inequality machinery (often credited to Cattiaux–Guillin–Wang and related Foster–Lyapunov frameworks).

### Theorem (Global PI for lattice YM under local PI + Lyapunov drift)
Assume local PI on \(U_\Lambda\) and the drift condition (LD). Then there exists \(C_{\mathrm{P,glob}}>0\), independent of \(\Lambda\), such that for all gauge-invariant smooth \(f\),

\[
\boxed{
\mathrm{Var}_{\mu_\Lambda}(f)
\ \le\
C_{\mathrm{P,glob}}\int_{M_\Lambda} \Gamma_\Lambda(f)\,d\mu_\Lambda.
}
\]

Equivalently, the gauge-invariant diffusion generator has a **uniform spectral gap**
\[
\lambda_1^{\mathrm{inv}}(\Lambda) \ge 1/C_{\mathrm{P,glob}} > 0
\quad\text{independent of }|\Lambda|.
\]

### Theorem (Global LSI for lattice YM under local LSI + Lyapunov drift)
Assume local LSI on \(U_\Lambda\) and (LD). Then there exists \(C_{\mathrm{LS,glob}}>0\), independent of \(\Lambda\), such that for all gauge-invariant \(f\) with \(\int f^2 d\mu_\Lambda=1\),

\[
\boxed{
\mathrm{Ent}_{\mu_\Lambda}(f^2)
\ \le\
C_{\mathrm{LS,glob}}\int_{M_\Lambda} \Gamma_\Lambda(f)\,d\mu_\Lambda.
}
\]

---

## 5. Proof skeleton (the “splitting + tail control” pattern)

This is the canonical structure:

### Step 1. Split variance / entropy into inside vs outside SAFE

Variance splitting (schematic):
\[
\mathrm{Var}_\mu(f) = \mathrm{Var}_\mu(f\mathbf 1_{U}) + \mathrm{Var}_\mu(f\mathbf 1_{U^c}) + \text{cross terms}.
\]

Entropy splitting (schematic):
\[
\mathrm{Ent}(f^2) = \int_{U} f^2\log f^2\,d\mu + \int_{U^c} f^2\log f^2\,d\mu.
\]

### Step 2. Control the \(U\) piece by local PI/LSI

Apply the local inequality on \(U\).

### Step 3. Control the \(U^c\) piece using Lyapunov drift

Use (LD) to show the stationary measure has strong tail suppression in \(W\), typically giving:

- \(\mu(U)\ge c>0\) uniformly,
- exponential (or at least integrable) tails in \(W\),
- and a bound of the form
  \[
  \int_{U^c} f^2\,d\mu \ \lesssim\ \int |\nabla f|^2\,d\mu
  \]
  with constants depending on \((\alpha,\beta)\) and local inequality constants, but not on dimension.

This is where the heavy probabilistic analysis lives, but it is a known “pattern” once (LD) is verified.

---

## 6. Why this module is worth extracting

Even ignoring the mass-gap story, this is a standalone mathematical deliverable:

> a route to **uniform global PI/LSI** for high-dimensional compact product manifolds with a nontrivial gauge-invariant potential.

That has applications to:
- mixing times of gauge Langevin dynamics,
- concentration for lattice gauge measures,
- and quantitative control needed for any constructive continuum limit.

---

## 7. What must be checked to make this airtight for lattice YM

This “template theorem” becomes a rigorous theorem for your model once you pin down:

1. the precise geometry/metric used for \(\Delta_{g_\Lambda}\) (horizontal vs full),
2. the gauge-invariant domain and any needed quotient/slice,
3. a fully explicit Lyapunov \(W_\Lambda\) and constants \((\alpha,\beta)\),
4. the exact local PI/LSI constants on \(U_\Lambda\),
5. and the uniformity in volume.

These are the proof-obligations that make the patching step nontrivial (but also very concrete).
