# Weak–Strong Field Decoupling in Structure Formation (Vacuum Stiffness Gravity)
## Why nonlinear collapse is essentially Newtonian, and where the modification actually enters

### What this document is
This module distills a key structural claim:

> **The nonlinear (“strong-field”) collapse dynamics of bound objects decouples from the
> weak-field modifications that affect large-scale growth.**

In practice: halos collapse and virialize in a Newtonian regime once their internal accelerations exceed \(a_0\),
even if their *formation history* (linear growth, bias, abundance) is altered on large scales.

The novelty is not the words; it is the **clean separation of interfaces**:
- weak-field sector: modified linear growth \(D(k,a)\),
- strong-field sector: screened Newtonian collapse ODE,
- matching interface: a single number \(\delta_c(k,z)\) (the collapse threshold).

Everything needed is derived here from first principles (no “see other file” steps).

---

## 1. Screening radius for a collapsing region

Consider a spherical region of total mass \(M\) and physical radius \(R(t)\).
Define the Newtonian internal acceleration at its boundary:
\[
g_N(R)=\frac{GM}{R^2}.
\]
Define the screening radius
\[
\boxed{
r_s(M):=\sqrt{\frac{GM}{a_0}},
}
\]
so that \(g_N(r_s)=a_0\).

- If \(R\ll r_s\), then \(g_N\gg a_0\) and the vacuum stiffness constitutive law satisfies \(\mu(g/a_0)\approx 1\).
- If \(R\gg r_s\), the region is in the weak-field regime.

A collapsing overdensity inevitably moves from \(R\gg r_s\) to \(R\ll r_s\) as it contracts.
Thus, **the late stage of collapse is generically screened**.

---

## 2. Equation of motion for spherical collapse

In Newtonian cosmology, the physical radius \(R(t)\) of a top-hat overdensity obeys
\[
\ddot R = -\frac{GM}{R^2} + \frac{\Lambda}{3}R,
\]
where the \(\Lambda\) term encodes the background acceleration in physical coordinates.

### 2.1 Vacuum stiffness replacement

In vacuum stiffness gravity (VSU), the gravitational acceleration \(g(R)\) sourced by the mass \(M\) is obtained from the implicit force law
\[
\mu\!\left(\frac{g}{a_0}\right)g = \frac{GM}{R^2},
\qquad \mu(x)=1-e^{-x}.
\]
So the collapse equation becomes
\[
\boxed{
\ddot R = -g(R) + \frac{\Lambda}{3}R,
\qquad
(1-e^{-g(R)/a_0})\,g(R)=\frac{GM}{R^2}.
}
\]

### 2.2 Strong-field reduction (screened collapse ODE)

If \(R(t)\ll r_s(M)\), then \(GM/R^2\gg a_0\), and the strong-field expansion gives
\[
g(R)=\frac{GM}{R^2}\left[1+O\!\left(e^{-GM/(a_0R^2)}\right)\right].
\]
Therefore, for \(R\ll r_s\),
\[
\boxed{
\ddot R = -\frac{GM}{R^2} + \frac{\Lambda}{3}R
+O\!\left(\frac{GM}{R^2}e^{-GM/(a_0R^2)}\right).
}
\]
The correction is nonperturbatively small.  In other words:

> Once an overdensity contracts below \(r_s\), its subsequent collapse and virialization are
> Newtonian to extremely high accuracy.

This is the core decoupling fact.

---

## 3. Where the modification actually enters: the linear-to-nonlinear matching

Halo abundances, bias, and “collapse thresholds” are usually computed by combining:

1. the nonlinear collapse dynamics (to define a collapse time),
2. the linear growth factor \(D(a)\) (to map the initial overdensity to the linearly extrapolated threshold \(\delta_c\)).

VSU modifies (2) more than (1).

### 3.1 Definition of the collapse threshold

Fix a collapse redshift \(z_c\) (or scale factor \(a_c\)).
Let \(\delta_{\rm NL}(t)\) be the nonlinear overdensity of the spherical region evolving under the screened collapse equation.

Choose an initial time \(a_{\rm ini}\ll 1\) when the overdensity is small and linear theory applies:
\[
\delta_{\rm ini}\ll 1.
\]
Evolve the region nonlinearly until it collapses (formally \(R\to 0\), or reaches a virial radius \(R_{\rm vir}\)) at \(a=a_c\).

Define \(\delta_c\) as the **linearly extrapolated** overdensity at collapse:
\[
\boxed{
\delta_c(k,a_c)
:=
\delta_{\rm ini}(k)\,\frac{D(k,a_c)}{D(k,a_{\rm ini})},
}
\]
where \(D(k,a)\) is the linear growing-mode solution of the modified growth equation.

### 3.2 Decoupling consequence: \(\delta_c\) changes mostly through \(D\)

Because the nonlinear collapse ODE becomes Newtonian (screened) during the decisive part of collapse,
the required *nonlinear* initial overdensity \(\delta_{\rm ini}\) to reach collapse by \(a_c\) is essentially the GR value
(for fixed background expansion history).

Therefore the leading VSU correction to \(\delta_c\) is
\[
\boxed{
\delta_c^{\rm VSU}(k,a_c)
\approx
\delta_c^{\rm GR}(a_c)\,
\frac{D_{\rm VSU}(k,a_c)}{D_{\rm GR}(a_c)}\,
\frac{D_{\rm GR}(a_{\rm ini})}{D_{\rm VSU}(k,a_{\rm ini})}.
}
\]
If early-time decoupling holds, then \(D_{\rm VSU}(k,a_{\rm ini})\approx D_{\rm GR}(a_{\rm ini})\), so
\[
\boxed{
\delta_c^{\rm VSU}(k,a_c)\approx
\delta_c^{\rm GR}(a_c)\,
\frac{D_{\rm VSU}(k,a_c)}{D_{\rm GR}(a_c)}.
}
\]

This is the clean interface:
- strong sector gives \(\delta_c^{\rm GR}(a_c)\) (screened),
- weak sector gives the ratio \(D_{\rm VSU}/D_{\rm GR}\).

### 3.3 Implications for halo abundance and bias

Plugging \(\delta_c(k,z)\) into Press–Schechter / excursion-set style formulae yields:

- scale-dependent bias if \(D(k,a)\) is scale-dependent,
- altered halo mass function mostly through the linear variance \(\sigma(M,z)\propto D(k,z)\),
- only weak sensitivity to the precise nonlinear collapse trajectory (because of screening).

This is exactly the “weak–strong field decoupling” principle.

---

## 4. External-field effect (environmental dependence) inside structure formation

Because the underlying field equation is nonlinear in \(\nabla\Phi\),
the internal dynamics of a collapsing region can depend on an external background acceleration \(g_{\rm ext}\).
Here is the stand-alone derivation.

### 4.1 Linearization of the flux map

Define the flux map
\[
A(p):=\mu\!\left(\frac{|p|}{a_0}\right)p,\qquad \mu(x)=1-e^{-x}.
\]
The field equation is
\[
\nabla\cdot A(\nabla\Phi)=4\pi G\rho.
\]

Write \(\Phi=\Phi_{\rm ext}+\phi\) with \(\nabla\Phi_{\rm ext}\approx p_{\rm ext}\) nearly constant in the region
and \(|\nabla\phi|\ll |p_{\rm ext}|\).

Then
\[
A(p_{\rm ext}+\nabla\phi)=A(p_{\rm ext})+DA(p_{\rm ext})\nabla\phi+O(|\nabla\phi|^2),
\]
where the Jacobian is
\[
DA(p)=\mu(x)I+\frac{\mu'(x)}{a_0|p|}\,p\otimes p,\qquad x=\frac{|p|}{a_0}.
\]

Taking divergence and subtracting the background equation yields the internal equation
\[
\nabla\cdot\!\bigl(DA(p_{\rm ext})\nabla\phi\bigr)=4\pi G\,\rho_{\rm int}.
\]
So the internal dynamics are governed by a **linear, anisotropic** Poisson equation whose coefficients depend on \(p_{\rm ext}\).

### 4.2 Isotropized effective coupling

If we neglect anisotropy (or average over directions),
\[
DA(p_{\rm ext})\approx \mu(|p_{\rm ext}|/a_0)\,I,
\]
and therefore
\[
\Delta\phi \approx 4\pi \frac{G}{\mu(g_{\rm ext}/a_0)}\,\rho_{\rm int}.
\]
Define
\[
G_{\rm eff}^{\rm int}(g_{\rm ext}):=\frac{G}{\mu(g_{\rm ext}/a_0)}.
\]

Thus:
- if \(g_{\rm ext}\gg a_0\), then \(\mu\to 1\) and \(G_{\rm eff}^{\rm int}\to G\): Newtonian internal dynamics (environment screens the modification);
- if \(g_{\rm ext}\ll a_0\), then \(\mu\sim g_{\rm ext}/a_0\) and \(G_{\rm eff}^{\rm int}\sim G a_0/g_{\rm ext}\): strong environmental dependence.

This is the external-field effect in a single formula.

### 4.3 Structure formation interpretation
In large-scale structure, \(g_{\rm ext}\) is set by the environment (filaments, host halos, large-scale tidal fields).
Therefore the collapse threshold and bias can become environment-dependent:
an analytic pathway to assembly bias in a screened modified-gravity theory.

---

## 5. What is genuinely novel / theory-forming here?

1. The decoupling is not hand-waving: it is an explicit consequence of the strong-field expansion
   \(g=g_N[1+O(e^{-g_N/a_0})]\).
2. It gives a clean, testable prediction: modifications should primarily show up as
   **growth-history and bias effects**, not as exotic internal halo dynamics.
3. It suggests a very specific observable target:
   **environment-dependent bias** driven by EFE-like dependence on background field strength.

---

## 6. Next work that would make this “real” (not just a structural claim)

1. Implement the modified linear growth \(D(k,a)\) in an excursion-set pipeline and compute the predicted
   scale-dependent halo bias and mass function.
2. Quantify EFE-driven environmental dependence by computing \(g_{\rm ext}\) distributions in simulations.
3. Run N-body simulations with a nonlinear solver for \(\nabla\cdot(\mu(|\nabla\Phi|/a_0)\nabla\Phi)=4\pi G\rho\)
   and directly test the decoupling predictions.

