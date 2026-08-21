# VSU 06B — Deriving \(\alpha_{\rm eff}(k,a)\) (and \(m_{\rm eff}\)) from the Field Equations

This note replaces the **phenomenological** insertion of \(\alpha_{\rm eff}(k,a)\)
with a derivation from the underlying field equations.

It also clarifies what an “effective mass” \(m_{\rm eff}\) can mean in this setup:
in the simplest completion it is not a literal particle mass, but the inverse of a
cosmological response scale (sound-horizon / time-derivative suppression).

---

## 0. What needs to be derived (and what was assumed)

The growth sector uses
\[
\frac{k^2}{a^2}\Phi = 4\pi G_{\rm eff}(k,a)\,\bar\rho_m\,\delta,
\qquad
G_{\rm eff}=G[1+\alpha_{\rm eff}(k,a)].
\]

A phenomenological form was proposed:
\[
\alpha_{\rm eff}\sim
\frac{k^2}{k^2+a^2 m_{\rm eff}^2}\;\frac{1}{\mu(\cdot)}.
\]

The goal here is to show **what \(\alpha_{\rm eff}\) and \(m_{\rm eff}\) become when you actually solve the linearized field equations**, and what must be true about the covariant completion for the above structure to emerge.

---

## 1. Two logically distinct ways \(\alpha_{\rm eff}\) can arise

### Route A (as currently written in the covariant action): scalar is *not* directly sourced by matter
If the scalar equation is
\[
\nabla_\mu\!\left(K(X)\nabla^\mu\phi\right)=0
\]
and matter couples only to \(g_{\mu\nu}\), then the scalar affects the Poisson equation only through \(\delta\rho_\phi\) in the Einstein constraint. In that case, on sub-horizon scales the scalar perturbation typically does **not** generate a MOND-like enhancement; it behaves more like a smooth dark-energy component unless special background conditions are chosen.

### Route B (matching the nonrelativistic VSU equation): scalar is *sourced* by matter in the quasistatic limit
The nonrelativistic VSU equation has an explicit matter source:
\[
\nabla\cdot\left(\mu(|\nabla\Phi|/a_0)\nabla\Phi\right)=4\pi G\rho.
\]

A covariant completion consistent with that structure must yield, in the appropriate limit,
a *sourced* scalar equation (or an equivalent sourced constraint for the physical potential).
This is the route that naturally produces \(\alpha_{\rm eff}\propto 1/\mu\).

Because the user request is to **derive \(\alpha_{\rm eff}\) from field equations**, I’ll present both:

- what you get from Route A (useful as a consistency check),
- and what you get from Route B (the route that reproduces the intended “\(1/\mu\)” behavior).

---

## 2. Route A: \(\alpha_{\rm eff}\) from Einstein constraint + scalar stress–energy

The linearized time–time Einstein equation in Newtonian gauge is
\[
\frac{k^2}{a^2}\Phi = 4\pi G\left(\bar\rho_m\delta+\delta\rho_\phi\right).
\]
Define
\[
\boxed{
\alpha_{\rm eff}^{(A)}(k,a):=\frac{\delta\rho_\phi}{\bar\rho_m\delta}.
}
\]

For a purely kinetic scalar \(F(X)\), on an FLRW background \(\phi_0(t)\),
the scalar perturbation equation has the form
\[
A_0\,\ddot{\delta\phi}
+3HK_0\,\dot{\delta\phi}
+\frac{K_0}{a^2}k^2\,\delta\phi
= \text{(metric sources)},
\]
where
\[
K_0:=F'(X_0),\qquad
A_0:=K_0+2X_0F''(X_0),
\qquad
c_s^2=\frac{K_0}{A_0}.
\]

For \(k\gg aH\), the \(k^2\delta\phi\) term dominates unless \(K_0\) is extremely small.
In the generic case one finds
\[
\delta\phi \sim \mathcal O\!\left(\frac{a^2H}{k^2}\right)\Phi,
\quad\Rightarrow\quad
\delta\rho_\phi \sim \mathcal O\!\left(\frac{a^2H^2}{k^2}\right)\Phi.
\]
Hence
\[
\boxed{
\alpha_{\rm eff}^{(A)}(k,a)\;\;\text{is generically suppressed by}\;\;
\left(\frac{aH}{k}\right)^2
\quad\text{on the linear sub-horizon scales used in RSD/lensing.}
}
\]

This is the “honest” result of Route A: the scalar does not produce a large quasi-static enhancement without additional structure.

This is not a bug of the algebra; it is a statement about what minimally coupled k-essence-like scalars do.

---

## 3. Route B: \(\alpha_{\rm eff}\) from a sourced scalar equation (the MOND-like route)

### 3.1 Minimal sourced completion (conceptual)
To reproduce the nonrelativistic VSU equation, the covariant completion must yield an equation whose quasistatic limit is
\[
\nabla\cdot\left(\mu(|\nabla\Phi|/a_0)\nabla\Phi\right)=4\pi G\rho.
\]

At the level of linear response, this is equivalent to treating the physical potential \(\Phi\) as obeying a **sourced quasilinear operator** with coefficient \(\mu\).

A minimal covariant way to encode this is to allow the scalar equation to be sourced by the matter trace (or rest density) so that, for dust,
\[
\boxed{
\nabla_\mu\left(K(X)\nabla^\mu\phi\right)=4\pi G\,\rho_m
\quad\Longrightarrow\quad
\nabla\cdot(K\,\nabla\phi)=4\pi G\rho_m
\;\text{(quasistatic)}.
}
\]

Here \(K(X)=1-e^{-\sqrt{|X|}}\) and for quasistatic configurations \(X\approx |\nabla\phi|^2/a_0^2\ge 0\), so
\[
K(X)=\mu(|\nabla\phi|/a_0)=1-e^{-|\nabla\phi|/a_0}.
\]

---

### 3.2 Linearization gives \(G_{\rm eff}\propto 1/\mu_{\rm bg}\)
Linearize around a background field configuration with slowly varying \(\mu_{\rm bg}(a)\) (e.g. set by an external field / environment):

\[
\mu_{\rm bg}\left(\frac{k^2}{a^2}\right)\phi = 4\pi G\,\bar\rho_m\,\delta
\quad\Rightarrow\quad
\frac{k^2}{a^2}\phi = 4\pi G\left(\frac{1}{\mu_{\rm bg}}\right)\bar\rho_m\delta.
\]

So the **quasistatic** effective coupling is
\[
\boxed{
G_{\rm eff}^{\rm (QS)}(a)=\frac{G}{\mu_{\rm bg}(a)}.
}
\]

To match the definition \(G_{\rm eff}=G[1+\alpha_{\rm eff}]\), the consistent identification is
\[
\boxed{
\alpha_{\rm eff}^{\rm (QS)}(a)=\frac{1}{\mu_{\rm bg}(a)}-1.
}
\]
(This subtraction is required so that \(\mu_{\rm bg}\to 1\) reproduces GR.)

---

### 3.3 Where \(m_{\rm eff}\) comes from: time-derivative suppression (sound horizon), not a particle mass
On an expanding background the covariant equation is hyperbolic, so keeping the leading time derivatives yields a forced wave equation schematically of the form

\[
A_{\rm bg}\,\ddot\phi+3H\mu_{\rm bg}\dot\phi+\mu_{\rm bg}\frac{k^2}{a^2}\phi
\simeq 4\pi G\,\bar\rho_m\,\delta,
\qquad
A_{\rm bg}=\mu_{\rm bg}+2X_{\rm bg}\mu'_{\rm bg},
\qquad
c_s^2=\frac{\mu_{\rm bg}}{A_{\rm bg}}.
\]

For growth modes with characteristic frequency \(\omega\sim H\), the term \(A_{\rm bg}\ddot\phi\)
acts like an **effective mass term** in the quasi-static Green’s function:

\[
\mu_{\rm bg}\left(\frac{k^2}{a^2}\right)\phi + A_{\rm bg}H^2\phi
\approx 4\pi G\,\bar\rho_m\,\delta.
\]

Multiply by \(a^2/\mu_{\rm bg}\) and define
\[
\boxed{
m_{\rm eff}^2(a):=\frac{A_{\rm bg}}{\mu_{\rm bg}}H^2(a)=\frac{H^2(a)}{c_s^2(a)}.
}
\]

Then
\[
\boxed{
\frac{k^2}{a^2}\phi
=
4\pi G\bar\rho_m\delta\left(\frac{1}{\mu_{\rm bg}}\right)\frac{k^2}{k^2+a^2 m_{\rm eff}^2}.
}
\]

This is the precise origin of the “\(k^2/(k^2+a^2 m_{\rm eff}^2)\)” structure:
it is simply the ratio between spatial-gradient response and the time-derivative (Hubble-scale) response.

Equivalently, define the **scalar sound horizon** \(k_*\sim aH/c_s\). Modes with \(k\ll k_*\) cannot build quasi-static gradients efficiently, so the enhancement shuts off.

---

### 3.4 Final derived form for the growth-sector parameterization
Putting the pieces together, a derived, GR-consistent parameterization is

\[
\boxed{
\alpha_{\rm eff}(k,a)
=
\left[\frac{1}{\mu_{\rm bg}(a)}-1\right]\;
\frac{k^2}{k^2+a^2 m_{\rm eff}^2(a)},
\qquad
m_{\rm eff}(a)=\frac{H(a)}{c_s(a)}.
}
\]

This does everything one wants:

- **GR limit (screened / strong-field):** \(\mu_{\rm bg}\to 1 \Rightarrow \alpha_{\rm eff}\to 0\).
- **Large-scale limit:** \(k\to 0 \Rightarrow \alpha_{\rm eff}\to 0\).
- **Small-scale limit:** \(k\gg a m_{\rm eff} \Rightarrow \alpha_{\rm eff}\to 1/\mu_{\rm bg}-1\).
- \(m_{\rm eff}\) is *not* a free mass scale: it is set by \(H\) and \(c_s\).

---

## 4. What remains to specify (the unavoidable “physics choice”)
This derivation makes the key remaining ambiguity very explicit:

\[
\mu_{\rm bg}(a)=\mu\!\left(\frac{g_{\rm bg}(a)}{a_0}\right)
\]

requires a model for the **background/external field** \(g_{\rm bg}\) that sets the linearization point (exactly like the EFE in the nonrelativistic theory).

Possible choices include:
- a large-scale external field from the cosmic web,
- a mode-dependent RMS field at a given epoch,
- or an effective coarse-grained \(g_{\rm bg}(a)\) determined self-consistently from the evolving power spectrum.

This is where the theory meets “real cosmology” and can no longer hide behind a single equation.

---

## 5. Summary (the nerdy punchline)

- If the covariant completion is just minimally coupled k-essence, \(\alpha_{\rm eff}\) is typically **small on sub-horizon linear scales** (Route A).
- If the covariant completion truly matches the nonrelativistic sourced VSU operator, then \(\alpha_{\rm eff}\) is **derivable** and takes the clean form
  \[
  \alpha_{\rm eff}=\left(\frac{1}{\mu_{\rm bg}}-1\right)\frac{k^2}{k^2+a^2(H/c_s)^2},
  \]
  with \(m_{\rm eff}=H/c_s\) emerging from time-derivative suppression, not from a new particle mass.

That is the mathematically honest bridge between the field equations and the growth parameterization.
