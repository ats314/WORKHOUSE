# VSU 07 — Minimality, Degeneracies, and a Falsification-First Research Program

**Scope.** This note collects the “closure layer” logic of the project:

- what is truly free (parameter inventory),
- what linear probes can/cannot distinguish (degeneracy structure),
- which internal-consistency seams still need stitching,
- and a concrete research program that would either sharpen VSU into a real theory or efficiently falsify it.

**Primary sources:** `06.3_Parameter_Minimality.md`, `06.2_Observable_Degeneracy_Structure.md`, `06.1_Internal_Consistency.md`.

---

## 1. Parameter inventory: what VSU claims (and why it’s attractive)

The project’s minimal parameter set is

- background: \(H_0,\Omega_{m0},\Omega_{\Lambda0}\) (flat \(\Lambda\)CDM),
- one new scale: \(a_0\),
- fixed constitutive closure:
  \[
  \mu(x)=1-e^{-x}.
  \]

No tunable interpolation function, screening length, or extra coupling is introduced.

This is a strong “physics-style” aesthetic: **if it fits, it fits for the same reason everywhere**.

---

## 2. Linear degeneracy structure: why multi-probe is the whole game

At linear order, growth responds only through

\[
G_{\rm eff}(k,a)=G[1+\alpha_{\rm eff}(k,a)].
\]

That means many linear observables are degenerate with each other in the usual ways:

- growth vs amplitude (\(A_s\), \(\sigma_8\)),
- growth vs \(\Omega_{m0}\),
- growth vs galaxy bias in clustering observables.

So single-probe “detections” or “constraints” are not decisive; the theory lives or dies by **cross-consistency** between probes.

The project’s clean separation is:

- BAO + AP → geometry (locked to \(\Lambda\)CDM here),
- RSD → growth rate \(f\sigma_8\),
- weak lensing → Weyl potential (kernel-weighted growth and coupling),
- ISW → time derivative of potentials.

---

## 3. Nonlinear sector as the degeneracy breaker

The nonlinear operator
\[
\nabla\cdot(\mu(|\nabla\Phi|/a_0)\nabla\Phi)=4\pi G\rho
\]
predicts:

- screening in strong internal fields,
- environmental screening (EFE),
- a modified spherical-collapse time,
- mass-/environment-dependent \(\delta_c(M,z)\),
- and therefore a distinctive halo bias signature.

These are hard to mimic by simply shifting \(\sigma_8\) or \(\Omega_m\). This is where VSU can become genuinely testable.

---

## 4. Internal-consistency seams that still matter

The project’s `06.1_Internal_Consistency.md` claims overall consistency, but three seams deserve explicit closure:

1. **Sign/branch of \(X\) in the covariant sector.**  
   Cosmology uses \(X_0=-\dot\phi_0^2/a_0^2<0\) (`03.2_Scalar_Perturbations.md`), while hyperbolicity and constitutive formulas were written for \(X>0\) (`01.3_Hyperbolicity_and_Characteristics.md`).  
   → Fixable by explicitly defining the \(X<0\) branch (see `VSU_06A_Covariant_Branch_and_Stability.md`).

2. **Weak-lensing sign in the \(\mathcal I(z)\) integral.**  
   `04.2_Weak_Lensing_and_S8.md` asserts \(\mathcal I(0)>0\), but for \(\Lambda\)CDM-like backgrounds the integrand contains \(\ln\Omega_m\le 0\), implying \(\mathcal I\le 0\).  
   → Needs sign reconciliation before claiming a direction for the \(S_8\) shift.

3. **GR limit of the \(\alpha_{\rm eff}\) ansatz.**  
   The project’s \(\alpha_{\rm eff}\propto (1/\mu)\) form does not automatically vanish as \(\mu\to 1\) at fixed \(k\).  
   → A GR-consistent form typically involves \((1/\mu-1)\) and a properly derived filter scale (see `VSU_06B_Deriving_alpha_eff_from_Field_Equations.md`).

---

## 5. A falsification-first research program (high payoff per unit effort)

### 5.1 Theory completion (paper-and-pencil)

- **Make the covariant theory unambiguous** on \(X<0\) backgrounds (branch completion).
- **Clarify matter coupling**: explain how the covariant completion reduces to the sourced nonrelativistic modified Poisson equation (or explicitly treat the nonrelativistic sector as an effective limit with separate coupling assumptions).
- **Derive \(\alpha_{\rm eff}(k,a)\)** rather than insert it:
  - identify the physical meaning of \(m_{\rm eff}\) (often a sound-horizon scale \(k_*\sim aH/c_s\)),
  - specify \(\mu_{\rm bg}(a)\) via a defensible cosmological background-field prescription.

Deliverable: a closed system where \(a_0\) really does determine late-time growth without hidden extra functions.

### 5.2 “Minimum viable numerics” (1–2 core tests)

Implement a 3D solver for
\[
\nabla\cdot(\mu(|\nabla\Phi|/a_0)\nabla\Phi)=4\pi G\rho,
\qquad \mu=1-e^{-x},
\]
then test:

1. **Spherical collapse with screening transition** (validate analytic scalings; quantify corrections).
2. **External Field Effect** in controlled setups:
   - embed a low-acceleration subsystem in a constant external field,
   - measure the transition back to Newtonian internal dynamics.

Deliverable: quantitative predictions for environment-dependent collapse/bias.

### 5.3 Multi-probe consistency targets (data-facing)

Because geometry is fixed, the following correlations are sharp:

- BAO/AP unchanged **must** coexist with any growth enhancement in RSD.
- ISW amplitude suppression must correlate with any change in \(f(z)\).
- Lensing predictions must be consistent with the same \(\alpha_{\rm eff}(k,a)\) used for RSD.

Even without full data fits, the **sign** and **relative direction** of these shifts can already kill large classes of \(\alpha_{\rm eff}\) behavior.

---

## 6. The “new-theory” fork in the road

VSU becomes new-theory territory if it nails one of these:

- a **principled** cosmological prescription for \(\mu_{\rm bg}(a)\) (no hidden free functions),
- a covariant completion whose weak-field limit **provably** reproduces the nonrelativistic operator,
- and a distinctive nonlinear signature (bias/EFE) that survives marginalization over standard cosmological parameters.

If those land, you have something structurally rare: a modified-gravity model with MOND-like galactic behavior, GR-like high-field behavior, and a strongly constrained cosmological footprint.

---

## References (project files)

- `06.1_Internal_Consistency.md`
- `06.2_Observable_Degeneracy_Structure.md`
- `06.3_Parameter_Minimality.md`
