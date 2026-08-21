# VSU_09 Second Pass Findings: Errata, Hidden Assumptions, and “Glue” Checks

**Purpose.** This note is a *second-pass audit* of the project’s original Markdown files
(`01.1`–`06.3`). It flags items that are easy to miss on a first read: sign/branch issues,
normalization slips, and “quiet assumptions” that become nontrivial once the covariant
theory is welded to the sourced nonrelativistic (NR) operator.

This is **not** a criticism document. It’s a “make the theory a single coherent object”
document.

---

## 0. Completeness check: referenced-but-missing files

Two files are cited by the closure layer but are not present in the uploaded set:

- `03.4_Early_Time_Asymptotics.md` (referenced in `06.1_Internal_Consistency.md`)
- `04.1_RSD_and_fsigma8_Mapping.md` (referenced in `06.1` and `06.2`)

This matters because several “no early-time modification” statements are attributed to
`03.4`, and the observational degeneracy discussion expects an explicit RSD projection.

---

## 1. The *original* covariant action does **not** source the scalar

### 1.1 What the files say

`01.1_Action_and_Field_Equations.md` introduces the covariant action
\[
S=\int d^4x\sqrt{-g}\Big[\frac{R}{16\pi G}+\frac{a_0^2}{8\pi G}F(X)+\mathcal L_m(g,\psi)\Big],
\qquad X=\frac{g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi}{a_0^2},
\]
which yields the *homogeneous* scalar equation
\[
\nabla_\mu\!\left(F'(X)\nabla^\mu\phi\right)=0.
\]
Meanwhile, the NR sector is explicitly sourced by matter through the term \(\int\rho\,\Phi\).

### 1.2 The hidden mismatch

With **minimal** matter coupling \(\mathcal L_m(g,\psi)\), varying \(\phi\) cannot produce a
matter source. So the claim “this reduces to the modified Poisson equation with source
\(4\pi G\rho\)” is not a strict derivation; it’s a *wish* unless a matter coupling to \(\phi\)
is specified.

### 1.3 The fix (already provided in `VSU_08`)

A standard diffeomorphism-invariant cure is to couple matter to a Jordan-frame metric
\[
\tilde g_{\mu\nu}=e^{-2\phi}g_{\mu\nu},\qquad S_m=S_m[\tilde g,\psi].
\]
Then the scalar equation becomes sourced by the trace of the matter stress tensor:
\[
\nabla_\mu\!\left(K(X)\nabla^\mu\phi\right)\propto \tilde T,
\qquad K:=F'(X),
\]
and the NR quasistatic limit yields
\[
\nabla\cdot\!\big(\mu(|\nabla\Phi|/a_0)\nabla\Phi\big)=4\pi G\rho
\]
with \(\mu(x)=1-e^{-x}\), as desired.

**Second-pass point:** once this coupling is introduced, **the linear cosmology sector must
be re-derived in the correct frame**, because matter is not separately conserved in the
Einstein frame.

---

## 2. The covariant constitutive law is only defined for \(X>0\) in the originals

This shows up in **three** places:

- `01.2_Stress_Energy_Tensor.md` defines \(F'(X)=1-e^{-\sqrt{X}}\) (implicitly \(X>0\)),
  but later evaluates homogeneous cosmology where \(X_0=-\dot\phi_0^2/a_0^2<0\).
- `01.3_Hyperbolicity_and_Characteristics.md` similarly assumes \(X>0\) then chooses a
  timelike background gradient (implying \(X_0<0\)).
- `03.2_Scalar_Perturbations.md` explicitly uses \(X_0=-\dot\phi_0^2/a_0^2\) while still
  writing everything in terms of \(K(X_0)=F'(X_0)\) with the \(X>0\) formula.

The minimal branch-explicit completion (one clean option) is
\[
K(X)=1-e^{-\sqrt{|X|}},
\]
which keeps the NR/spacelike-gradient sector unchanged and makes the FLRW/timelike
branch real. Stability/positivity can then be rechecked on \(X<0\).

---

## 3. Linear perturbations: a normalization/coefficients issue in \(\delta\rho_\phi\)

### 3.1 What `03.2` states

`03.2_Scalar_Perturbations.md` writes the sub-horizon Poisson constraint as
\[
\frac{k^2}{a^2}\Phi=4\pi G\big(\bar\rho_m\delta+\delta\rho_\phi\big),
\]
with
\[
\delta\rho_\phi=(K_0+2X_0K_0')\dot\phi_0\dot{\delta\phi}-K_0\dot\phi_0^2\Phi.
\]

### 3.2 Why this is suspicious

Using the stress–energy tensor given in `01.2` and standard Newtonian-gauge bookkeeping,
the density perturbation for a purely-kinetic \(F(X)\) scalar typically appears through
the gauge-invariant combination \((\dot{\delta\phi}-\dot\phi_0\Phi)\), and the kinetic
combination \(A_0:=K_0+2X_0K_0'\) multiplies *both* time-derivative and \(\Phi\) pieces.

A consistent compact form (up to overall conventions) is generically of the type
\[
\delta\rho_\phi \propto A_0\,\dot\phi_0\,(\dot{\delta\phi}-\dot\phi_0\Phi),
\qquad A_0:=K_0+2X_0K_0'.
\]

**Second-pass point:** the coefficient in front of the \(\Phi\) term in `03.2`
is written as \(K_0\), not \(A_0\), and the “metric-dressing” terms that appear when
relating \(\delta T_{00}\) to \(\delta\rho\) are not shown. This is precisely the kind of
small slip that later forces an *ad hoc* \(\alpha_{\rm eff}\) ansatz.

**Actionable fix:** re-derive \(\delta T^0{}_0\) and \(\delta T^0{}_i\) from
`01.2_Stress_Energy_Tensor.md` with the chosen \(X\)-branch and a declared convention for
what enters the Poisson constraint on sub-horizon scales.

---

## 4. Super-horizon curvature conservation: multi-component subtlety

`03.2` defines
\[
\mathcal R=\Phi-\frac{H}{\dot\phi_0}\delta\phi
\]
and argues \(\dot{\mathcal R}=0\) on super-horizon scales because \(\delta P_{\rm nad}=0\).

That logic is valid for a **single** barotropic component (or a single k-essence field),
but in the project we also have pressureless matter. In multi-component systems:

- there is an **intrinsic** nonadiabatic part (which may vanish for \(F(X)\) alone),
- and there can be a **relative entropy** (isocurvature) mode between matter and \(\phi\).

So “\(\delta P_{\rm nad}=0\)” for the scalar by itself does **not** automatically imply
\(\dot{\mathcal R}=0\) for the *total* system unless additional assumptions are made
(e.g. the scalar is dynamically negligible at early times or strictly locked).

**Second-pass point:** if early-time GR recovery is crucial (BAO/CMB arguments), the
cleanest statement is not “\(\mathcal R\) is always conserved,” but rather
“the scalar sector is arranged so that its contribution to super-horizon dynamics is
negligible / adiabatic.”

---

## 5. Weak lensing sign: the integral \(\mathcal I(z)\) has the wrong stated sign

`04.2_Weak_Lensing_and_S8.md` defines
\[
\mathcal I(z)=\int_z^\infty \frac{dz'}{1+z'}\Omega_m(z')^{6/11}\ln\Omega_m(z')
\]
and asserts \(\mathcal I(0)>0\).

But for a standard \(\Lambda\)CDM background, \(0<\Omega_m(z')\le 1\) for finite \(z'\), so
\(\ln\Omega_m(z')\le 0\), making the integrand nonpositive. Therefore
\[
\mathcal I(z)\le 0,
\]
with equality only in the idealized \(\Omega_m\equiv 1\) limit.

**Second-pass point:** this sign flip changes the qualitative direction of the claimed
\(S_8\) shift for \(\alpha_\infty>0\).

---

## 6. Spherical collapse: two separate inconsistencies in `05.2`

### 6.1 Collapse-time scaling in the unscreened regime

`05.2_Spherical_Collapse.md` correctly sets up
\[
t_{\rm coll}^{\rm VSU}=\int_0^{r_i}\frac{dr}{\sqrt{2\sqrt{GMa_0}\,\ln(r_i/r)}},
\]
but then states the scaling
\[
t_{\rm coll}^{\rm VSU}\propto \frac{r_i^{3/2}}{(GMa_0)^{1/4}},
\]
which is dimensionally inconsistent.

Evaluating the integral exactly gives
\[
t_{\rm coll}^{\rm VSU}=\sqrt{\frac{\pi}{2}}\;\frac{r_i}{(GMa_0)^{1/4}}.
\]

### 6.2 Mass/redshift scaling of \(g_N(M,z)\) (and therefore \(\delta_c\))

`05.2` also claims
\[
\delta_c^{\rm VSU}(M,z)\propto M^{1/6}(1+z)^{-1/2},
\]
based on the identification \(\delta_c^{\rm VSU}\propto (g_N/a_0)^{1/4}\) and
\(r_i\propto (M/\bar\rho_m(z))^{1/3}\).

But with \(\bar\rho_m(z)\propto(1+z)^3\) and physical \(r_i\propto M^{1/3}(1+z)^{-1}\), one finds
\[
g_N=\frac{GM}{r_i^2}\propto M^{1/3}(1+z)^2
\quad\Rightarrow\quad
\left(\frac{g_N}{a_0}\right)^{1/4}\propto M^{1/12}(1+z)^{1/2},
\]
not the scaling stated in the file.

**Second-pass point:** both the collapse-time scaling and the subsequent mass/redshift
scaling need correction before halo-bias conclusions are trusted.

---

## 7. What this changes in the closure layer (`06.1`–`06.3`)

The closure notes correctly emphasize “acyclic dependencies” and minimal parameters, but
the second-pass issues above imply:

- **Internal consistency is conditional** on (i) branch completion for \(X<0\),
  (ii) fixing the weak-lensing sign, and (iii) correcting collapse/bias scalings.
- **Parameter minimality** is threatened if \(\alpha_{\rm eff}(k,a)\) requires an
  arbitrary environmental/background prescription for \(\mu\) *unless that prescription is
  derived from the covariant coupling and background solution*.

---

## 8. Practical completion checklist (high leverage)

1. **Declare the physical frame** (Einstein vs Jordan) once a \(\phi\)-dependent matter coupling
   is introduced.
2. **Re-derive linear perturbation equations** in that frame, including matter conservation laws.
3. **Recompute** the sub-horizon Poisson response and extract \(\alpha_{\rm eff}(k,a)\) from the
   actual field equations (not by ansatz).
4. **Fix and propagate** the spherical-collapse corrections into halo bias.
5. **Fix the weak-lensing sign** and re-evaluate the direction of the \(S_8\) shift.

---

## Endnote: why this second pass is useful

Most “new theory” attempts fail not because the central idea is bad, but because **two
beautiful halves don’t actually touch**. The project’s best asset is the rigid,
parameter-minimal NR operator with exponential stiffness. The highest-payoff work is
making the covariant completion (and its perturbations) mathematically and physically
the same object.
