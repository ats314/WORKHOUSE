# VSU Predictive Structure: Minimality, Degeneracies, and a Research Program

## Abstract

VSU is ambitious in a very specific way: it tries to get *a lot* of phenomenology out of *very little* freedom.

This note distills the “closure layer” of the project:

- parameter minimality (what is truly free),
- what linear probes can/cannot distinguish (degeneracy structure),
- why multi-probe comparisons are not optional but *the point*,
- a concrete theory + simulation program that would either (i) promote VSU into a serious contender, or (ii) efficiently falsify it.

---

## 1. Parameter minimality (what you actually get to choose)

In the project as written, the parameter set is:

### 1.1 Standard background parameters (flat \(\Lambda\)CDM)
\[
H_0,\quad \Omega_{m0},\quad \Omega_{\Lambda0}\quad(\Omega_{m0}+\Omega_{\Lambda0}=1).
\]

### 1.2 One genuinely new scale
\[
\boxed{a_0}\qquad\text{(universal acceleration scale)}.
\]

### 1.3 No free interpolation function
The constitutive relation is fixed:
\[
\boxed{\mu(x)=1-e^{-x}}.
\]
So unlike many “designer” modified-gravity parameterizations, you do **not** get to arbitrarily tune \(\mu(x)\) to rescue failures on a per-dataset basis.

This is simultaneously the model’s greatest strength (predictivity) and greatest danger (fragility).

---

## 2. Degeneracy structure: what linear observables can and can’t tell you

Linear growth sees the combination
\[
G_{\rm eff}(k,a)=G[1+\alpha_{\rm eff}(k,a)].
\]

So, at the level of the matter power spectrum alone, there is an intrinsic degeneracy between:
- changing gravity, and
- changing “effective clustering content” (e.g., \(\Omega_m\), initial amplitude \(A_s\), bias parameters).

Different probes compress the theory into **different window-weighted combinations** of \(\alpha_\infty(k)\):

- **RSD:** bin-averaged \(f\sigma_8(z)\), relatively insensitive to detailed \(k\)-shape.
- **Weak lensing:** kernel-weighted combination of \(\mathcal G^2 D^2\) (and thus \(\alpha_\infty(k)\)).
- **ISW:** probes \(\dot\Phi\) (time variation of the potential), largely blind to absolute normalization.
- **BAO + AP:** purely geometric in this framework (background fixed), so they act as a “geometry lock.”

### 2.1 What breaks degeneracies

Multi-probe combinations are mandatory:

- **RSD + BAO/AP** separates geometry from growth.
- **Lensing + BAO/AP** separates amplitude-like parameters from distances.
- **RSD + lensing** probes velocity response vs potential response.
- **Nonlinear structure** (collapse threshold, halo bias, environment dependence) breaks degeneracies that are unavoidable at linear order.

---

## 3. Correlated predictions that feel “high value”

From the project’s analytic chain, a few predictions are especially potent because they are tied together by the same constitutive physics:

### 3.1 Operator-level screening + EFE (no extra knobs)

Screening and environmental dependence arise from the same nonlinear operator:
\[
\nabla\cdot\!\bigl(\mu(|\nabla\Phi|/a_0)\nabla\Phi\bigr)=4\pi G\rho.
\]
The EFE is not an add-on; it is *baked in*.

### 3.2 Spherical collapse scaling \(\propto (g_N/a_0)^{1/4}\)

In the unscreened regime, top-hat collapse times scale as
\[
t_{\rm coll}^{\rm VSU}/t_{\rm coll}^{\rm N}\propto (g_N/a_0)^{1/4},
\]
with an exact prefactor when the unscreened approximation is valid.

This feeds directly into:
- a mass/environment-dependent effective \(\delta_c(M,z)\),
- a corresponding shift in halo bias and the mass function.

### 3.3 “Geometry safe” but “growth active”

BAO peak positions and AP distortions remain unchanged (background \(\Lambda\)CDM), while growth observables change in a linked way through \(\alpha_{\rm eff}\).

That structure is rare: many modified-gravity models modify geometry and growth together, making internal consistency harder.

### 3.4 ISW amplitude suppression for \(\alpha_\infty>0\)

The analytic ISW ratio predicts suppression (with unchanged sign) when \(\alpha_\infty>0\).  
That is a clean and very falsifiable signature using CMB–LSS cross-correlations.

---

## 4. Two internal consistency “stress points” worth addressing explicitly

These are not fatal, but they need to be nailed down to keep the theory honest.

### 4.1 The covariant branch/sign of \(X\)

In FLRW, a homogeneous scalar has a timelike gradient, so \(X<0\) in the common \((-+++)\) convention.  
But the constitutive law is written as \(K(X)=1-e^{-\sqrt{X}}\), i.e. for \(X>0\).

A fully consistent completion must specify how \(K(X)\) behaves for \(X<0\) (or redefine the invariant). Until this is explicit, “cosmological perturbations + hyperbolicity” are not truly closed.

### 4.2 A sign mismatch in the lensing \(S_8\) expansion

If one defines
\[
\mathcal I(z)=\int_z^\infty \frac{dz'}{1+z'}\,\Omega_m^{6/11}\ln\Omega_m,
\]
then \(\mathcal I(z)\le 0\) for standard \(\Lambda\)CDM.  
So for fixed primordial amplitude, \(\alpha_\infty>0\) increases growth and should increase \(\sigma_8\), not decrease it.  

That may be:
- a sign convention slip, or
- a hidden assumption about what is held fixed (e.g., refitting \(A_s\) with CMB constraints).

Either way, it should be clarified in the next iteration.

---

## 5. A concrete “next work” roadmap (the fun part)

### 5.1 Theory completion tasks

1. **Specify the covariant branch of \(K(X)\)** (or redefine the invariant) and redo:
   - stress–energy positivity,
   - hyperbolicity,
   - perturbation equations,
   on the correct cosmological background branch.

2. **Derive \(\alpha_{\rm eff}(k,a)\) from the field dynamics**, not by ansatz.
   - If a scale \(m_{\rm eff}\) is introduced, define it explicitly (and show it is not a hidden free parameter).

3. **Compute the full top-hat collapse in an expanding background**, then obtain \(\delta_c(M,z)\) by explicit linear extrapolation (rather than collapse-time scaling heuristics).

### 5.2 Minimal simulation program (high diagnostic power)

A good “MVP” simulation stack:

- **Nonlinear Poisson solver** on a mesh:
  \[
  \nabla\cdot\!\bigl(\mu(|\nabla\Phi|/a_0)\nabla\Phi\bigr)=4\pi G\rho,
  \qquad \mu(x)=1-e^{-x}.
  \]
  Use nonlinear multigrid or Newton–Krylov.

- **Spherical collapse numerical check**:
  compare exact ODE integration with the analytic integral in the unscreened regime and with GR in the screened regime.

- **Small N-body test boxes**:
  measure the halo mass function and halo bias vs environment; compare to GR at the same background.

This program would either validate the analytic scaling structure (very exciting) or show where/why it breaks (also exciting, in a scientific way).

---

## 6. Why this project is worth extracting

Even with the caveats, the project’s core move is coherent and rare:

- choose a *fixed* constitutive law \(\mu(x)\),
- derive force-law asymptotics and screening from the operator,
- propagate consequences into nonlinear structure and linear cosmological observables,
- enforce geometry–growth separation via an unchanged background.

That is exactly the kind of rigid, overconstrained framework where “new theory” can live—because you can’t endlessly patch it.

If VSU survives contact with (i) covariant consistency and (ii) multi-probe data, it would be a genuinely interesting unification of MOND-like phenomenology with late-time cosmological modifications under one new scale.

