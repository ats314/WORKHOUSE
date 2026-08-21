# EXC_04 — Hyperbolicity and Characteristic Speeds for the Scalar Sector (Effective Metric Form)

## What this document contains

A compact derivation (as recorded in the project) of:

1. the effective characteristic metric governing the principal part of the scalar PDE,
2. the hyperbolicity conditions (Lorentzian signature of that metric),
3. the characteristic (sound) speed formula,
4. the special-case bounds for \(K(X)=1-e^{-\sqrt{X}}\).

**Primary source:** `01.3_Hyperbolicity_and_Characteristics.md`.

---

## 1. Scalar equation and notation

The scalar equation is written as
\[
\nabla_\mu\!\left(K(X)\,\nabla^\mu\phi\right)=0,
\qquad
X := \frac{g^{\mu\nu}\nabla_\mu\phi\,\nabla_\nu\phi}{a_0^2}.
\]

Define \(u^\mu := \nabla^\mu\phi\).

---

## 2. Principal symbol and effective characteristic metric

Linearizing about a background \(\phi_0\) and extracting the principal part yields an effective metric governing characteristics:
\[
G_{\rm eff}^{\mu\nu}
=
K(X)\,g^{\mu\nu}
+\frac{2K'(X)}{a_0^2}\,u^\mu u^\nu.
\]

---

## 3. Hyperbolicity conditions

The file states the standard k-essence hyperbolicity conditions:
\[
K(X)>0,
\qquad
K(X)+2XK'(X)>0.
\]

---

## 4. Characteristic speed (sound speed)

In a local frame adapted to the background, the file gives
\[
c_s^2(X)=\frac{K(X)}{K(X)+2XK'(X)}.
\]

---

## 5. Specialization to \(K(X)=1-e^{-\sqrt{X}}\)

For
\[
K(X)=1-e^{-\sqrt{X}},
\]
the file records limiting behavior:
\[
X\to 0^+:\ c_s^2\to \tfrac12,
\qquad
X\to +\infty:\ c_s^2\to 1.
\]

---

## 6. Known tension in the project corpus

Other project files note a sign/domain tension: \(K(X)=1-e^{-\sqrt{X}}\) is only real-valued as written for \(X\ge 0\), while cosmological backgrounds can involve \(X<0\) depending on conventions (timelike gradients). This document does not resolve that; it only records the hyperbolicity analysis as written.

