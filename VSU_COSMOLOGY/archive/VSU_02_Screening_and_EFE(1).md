# VSU 02 — Operator-Level Screening and the External Field Effect (EFE)

**Scope.** VSU screening is not an added mechanism. It is an intrinsic property of the quasilinear elliptic operator
\[
\nabla\cdot(\mu(|\nabla\Phi|/a_0)\nabla\Phi)=4\pi G\rho,
\qquad
\mu(x)=1-e^{-x}.
\]
This note isolates the “PDE reason” Newtonian gravity returns in strong fields and in strong external fields.

**Primary sources:** `05.1_Nonlinear_Screening_Mechanism.md`, `02.3_Screening_Radius_and_EFE.md`.

---

## 1. Strong-field expansion: why GR returns “automatically”

Let
\[
\mathbf g:=-\nabla\Phi,\qquad g:=|\mathbf g|.
\]

In a region where \(g\gg a_0\), define
\[
\mu\!\left(\frac{g}{a_0}\right)=1-\varepsilon,
\qquad \varepsilon:=e^{-g/a_0}\ll 1.
\]

Insert into the operator:

\[
\nabla\cdot\!\left((1-\varepsilon)\mathbf g\right)
=
\nabla\cdot\mathbf g
-
\nabla\varepsilon\cdot\mathbf g.
\]

Using
\[
\nabla\varepsilon
=
-\frac{e^{-g/a_0}}{a_0}\frac{\nabla g}{g},
\]
the correction term scales as \(O(a_0/g)\) (and is in fact exponentially small if \(g/a_0\) is moderately large). Thus

\[
\boxed{
\nabla^2\Phi
=
4\pi G\rho
+
O\!\left(\frac{a_0}{g}\right),
}
\]

i.e. Newtonian behavior is recovered in the strong-field regime.

**Interpretation.** The operator “linearizes itself” in high-field regions because \(\mu\to 1\) rapidly. No extra screening field is needed.

---

## 2. Screening radius \(r_s\): where the transition happens

For an isolated mass \(M\), define the Newtonian field
\[
g_N(r)=\frac{GM}{r^2}.
\]

Screening holds where \(g_N\gg a_0\). The transition is defined by \(g_N(r_s)=a_0\), giving

\[
\boxed{
r_s=\sqrt{\frac{GM}{a_0}}.
}
\]

Regimes:

- \(r\ll r_s\): screened (Newtonian),
- \(r\gg r_s\): unscreened (stiffness-dominated).

---

## 3. Uniform ellipticity viewpoint (why this matters mathematically)

In any region \(\Omega\subset\mathbb R^3\) where
\[
\inf_{\Omega}\frac{|\nabla\Phi|}{a_0}\ge \Lambda,
\qquad \Lambda\gg 1,
\]
we have
\[
\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)=1+O(e^{-\Lambda}),
\]
so the PDE is uniformly elliptic with principal part arbitrarily close to \(\nabla^2\Phi\).

This is the operator-level statement behind phrases like “screened” or “GR recovery.”

---

## 4. External Field Effect (EFE) as an operator phenomenon

Decompose
\[
\mathbf g=\mathbf g_{\rm int}+\mathbf g_{\rm ext},
\]
where \(\mathbf g_{\rm ext}\) varies slowly across the system.

If \(|\mathbf g_{\rm ext}|\gg a_0\), then \(|\mathbf g|\approx |\mathbf g_{\rm ext}|\) throughout the system, so

\[
\mu\!\left(\frac{|\mathbf g|}{a_0}\right)\simeq
\mu\!\left(\frac{|\mathbf g_{\rm ext}|}{a_0}\right)
\simeq 1.
\]

The internal potential then satisfies

\[
\boxed{
\nabla^2\Phi_{\rm int}
=
4\pi G\rho_{\rm int}
+
O\!\left(\frac{a_0}{|\mathbf g_{\rm ext}|}\right).
}
\]

**Key point.** In VSU, the EFE is not a bolt-on effect: it’s the inevitable consequence of \(\mu\) depending on the **total** field magnitude.

---

## 5. “Stiff” screening from an exponential \(\mu\)

Because
\[
1-\mu(x)=e^{-x},
\]
the approach to Newtonian behavior is exponentially fast in \(x=g/a_0\).

That’s a structural prediction:

- moderate accelerations already behave essentially Newtonian,
- low-acceleration environments (outer halos, voids) are where deviations live.

---

## References (project files)

- `05.1_Nonlinear_Screening_Mechanism.md`
- `02.3_Screening_Radius_and_EFE.md`
