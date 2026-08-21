# EXC_03 — Scale-Dependent Effective Coupling in Linear Growth: \(\alpha_{\rm eff}(k,a)\) with Yukawa Suppression and \(\mu\)-Screening

## What this document contains

A project-level proposal for how modified-force effects enter linear cosmological growth through a scale- and time-dependent effective coupling
\[
G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)],
\]
with the specific factorized form
\[
\alpha_{\rm eff}(k,a)=\frac{k^2}{k^2+a^2 m_{\rm eff}^2(a)}\;\frac{1}{\mu(g/a_0)}.
\]

This appears in the file set as an **ansatz/closure** for forecasting; the derivation is not present in the same documents.

**Primary sources:** `03.3_Matter_Growth_Equation.md`, `VSU_CONDENSED_ALL.md`.

---

## 1. Growth equation with an effective coupling

The project records the standard subhorizon growth equation for matter perturbations:
\[
\ddot\delta+2H\dot\delta-4\pi G_{\rm eff}(k,a)\,\bar\rho_m(a)\,\delta=0,
\]
with
\[
G_{\rm eff}(k,a)=G\,[1+\alpha_{\rm eff}(k,a)].
\]

---

## 2. The recorded ansatz for \(\alpha_{\rm eff}(k,a)\)

The project specifies
\[
\boxed{
\alpha_{\rm eff}(k,a)
=
\frac{k^2}{k^2+a^2 m_{\rm eff}^2(a)}\;\frac{1}{\mu(g/a_0)}.
}
\]

---

## 3. Interpretation of the two factors (as encoded)

### 3.1 Yukawa-like scale dependence

The factor
\[
\frac{k^2}{k^2+a^2 m_{\rm eff}^2(a)}
\]
suppresses modifications when \(k\ll a\,m_{\rm eff}(a)\) and tends to \(1\) when \(k\gg a\,m_{\rm eff}(a)\).

### 3.2 Environmental screening through \(\mu(g/a_0)\)

The factor \(1/\mu(g/a_0)\) ties the cosmological modification strength to the same screening function \(\mu\) used in the project’s nonrelativistic sector (galaxy-scale modeling). Larger \(\mu\) reduces \(\alpha_{\rm eff}\); smaller \(\mu\) enhances it.

---

## 4. What is missing (in the current file set)

No file in the current set provides a derivation of:

- the modified field equations that would yield the stated \(G_{\rm eff}\),
- the dynamical origin of \(m_{\rm eff}(a)\),
- the precise cosmological definition of the \(g\) entering \(\mu(g/a_0)\).

So, within the corpus as provided, \(\alpha_{\rm eff}(k,a)\) is an asserted closure, not a proven consequence.

