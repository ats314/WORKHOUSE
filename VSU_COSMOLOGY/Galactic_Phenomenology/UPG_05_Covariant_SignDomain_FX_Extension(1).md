# Fixing the covariant sign-domain issue (\(X<0\)) cleanly

## 0. The problem in one sentence

Your covariant sector defines a constitutive function \(K(X)\) (or \(F'(X)\)) using \(\sqrt{X}\), which is only real for \(X\ge 0\), but **cosmological backgrounds typically give \(X<0\)** because the background scalar gradient is timelike.

If \(K(X)\) is not defined on the cosmological branch, you do not yet have a theory — you have a galaxy-limit ansatz.

## 1. Definitions (minimal)

Let
\[
X \equiv \frac{g^{\mu\nu}\,\partial_\mu\phi\,\partial_\nu\phi}{a_0^2}.
\]
- Quasi-static galaxy limit: gradients are spacelike \(\Rightarrow X>0\).
- Homogeneous FRW background: \(\phi=\phi(t)\) \(\Rightarrow X= -\dot\phi^2/a_0^2 <0\) (for mostly-plus signature).

The effective perturbation metric typically has the form
\[
G^{\mu\nu} = K(X)\,g^{\mu\nu} + 2K'(X)\,u^\mu u^\nu,\qquad
u^\mu \propto \partial^\mu\phi,
\]
so hyperbolicity/causality depend on \(K\) and \(K'\) on the **actual background value** \(X_0\).

## 2. A “minimal real extension” that preserves the galaxy limit exactly

You currently use (galaxy branch)
\[
K(X) = 1-e^{-\sqrt{X}},\qquad X\ge 0.
\]

A clean, brutally minimal extension to all real \(X\) is:

\[
K(X)=
\begin{cases}
1-e^{-\sqrt{X}}, & X\ge 0,\\[6pt]
1-e^{-\sqrt{-X}}, & X\le 0.
\end{cases}
\]

This keeps:
- the nonrelativistic/quasi-static branch **unchanged**,
- the cosmological branch **real and finite**.

### Corresponding \(F(X)\)

If \(K(X)=F'(X)\), then an antiderivative that is continuous at \(X=0\) is:

\[
F(X)=
\begin{cases}
X-2+2e^{-\sqrt{X}}\bigl(1+\sqrt{X}\bigr), & X\ge 0,\\[6pt]
X+2-2e^{-\sqrt{-X}}\bigl(1+\sqrt{-X}\bigr), & X\le 0,
\end{cases}
\]
with the integration constants fixed by \(F(0)=0\).

This is still “nothing exotic”: it is exactly the same elementary form on both branches, with \(\sqrt{X}\mapsto \sqrt{|X|}\) and the correct chain-rule sign.

## 3. What this buys you immediately (and what it doesn’t)

### (A) It makes the cosmological background well-defined

You can now evaluate \(K(X_0)\), \(K'(X_0)\), and the effective metric \(G^{\mu\nu}\) for \(X_0<0\) without complex numbers.

### (B) It does *not* automatically guarantee healthy perturbations

You still must check:
- hyperbolicity conditions (e.g. \(K>0\) and \(K+2XK'>0\) in the usual k-essence-like structure),
- stability (no gradient instabilities, no ghosts),
- and the correct nonrelativistic limit when spatial gradients dominate.

This note is only about the **domain** fix.

## 4. A slightly less minimal but smoother alternative

If you want \(K(X)\) to be analytic around \(X=0\) (your current choice already has a non-analytic derivative divergence), you can regularize the square-root:

\[
\sqrt{X}\ \mapsto\ \sqrt{X+\epsilon^2}-\epsilon
\]
on the \(X\ge 0\) branch, and similarly for \(X\le 0\), with \(\epsilon\) a fixed tiny parameter.

This avoids infinities at \(X=0\) but introduces a new scale. Whether that is acceptable depends on your philosophy.

## 5. The real test: compute \(\alpha_{\rm eff}(k,a)\) from this, not by ansatz

Once \(K(X)\) is defined for \(X<0\), you can:

1. choose a background solution \(\phi(t)\) consistent with FRW,
2. linearize the field equations on that background,
3. read off the effective Newton coupling \(G_{\rm eff}(k,a)\) and thus
\[
\alpha_{\rm eff}(k,a)\equiv \frac{G_{\rm eff}(k,a)}{G}.
\]

That is the point where “galaxy fit kernel” becomes “theory with cosmology”.

This extension is the smallest step that makes that computation *possible*.
