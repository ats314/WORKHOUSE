# Riccati envelope as an exact semigroup on spectra (finite-dimensional)

This note formalizes the “Riccati envelope” map used in curvature diagnostics as an honest semigroup acting on
positive semidefinite matrices (and hence on spectra).

Everything here is finite-dimensional linear algebra.

---

## Definition (matrix Riccati envelope)

Fix \(\eta>0\). For a symmetric positive semidefinite matrix \(H\succeq 0\), define
\[
\Phi_\eta(H) \;:=\; H\,(I+\eta H)^{-1}.
\]

Since \(H\) commutes with \(I+\eta H\), \(\Phi_\eta(H)\) is symmetric and well-defined.

If \(H\) is invertible, then equivalently
\[
\Phi_\eta(H) \;=\; (H^{-1} + \eta I)^{-1}.
\]

---

## Spectral action

Let \(H = U\,\mathrm{diag}(\lambda_1,\dots,\lambda_n)\,U^\top\) with \(\lambda_i\ge 0\).
Then
\[
\Phi_\eta(H)
=
U\,\mathrm{diag}\!\left(\frac{\lambda_i}{1+\eta\lambda_i}\right)\,U^\top.
\]

Thus the envelope acts pointwise on eigenvalues by the scalar map
\[
\phi_\eta(\lambda) := \frac{\lambda}{1+\eta\lambda},\qquad \lambda\ge 0.
\]

Immediate consequences:

- \(0 \le \phi_\eta(\lambda) \le \lambda\) (curvature never increases),
- \(\phi_\eta(\lambda) \le 1/\eta\) (uniform upper bound),
- \(\phi_\eta(0)=0\) (nullspace is preserved).

---

## Semigroup property (exact)

For all \(\eta,\tau\ge 0\),
\[
\Phi_\tau(\Phi_\eta(H)) \;=\; \Phi_{\eta+\tau}(H).
\]

**Proof (spectral functional calculus):**  
On eigenvalues,
\[
\phi_\tau(\phi_\eta(\lambda))
=
\frac{\lambda/(1+\eta\lambda)}{1+\tau\,\lambda/(1+\eta\lambda)}
=
\frac{\lambda}{1+(\eta+\tau)\lambda}
=
\phi_{\eta+\tau}(\lambda).
\]
Therefore the same identity holds on \(H\) by diagonalization. ∎

Corollary (n steps):
\[
\Phi_\eta^{\,n}(H) = \Phi_{n\eta}(H),\qquad
\lambda_i^{(n)} = \frac{\lambda_i}{1+n\eta\lambda_i}.
\]

---

## Interpretation as an ODE flow

Define \(H(t) := \Phi_t(H_0)\) for \(t\ge 0\). Then on each eigenvalue,
\[
\lambda(t)=\frac{\lambda_0}{1+t\lambda_0}
\quad\Rightarrow\quad
\dot\lambda(t) = -\lambda(t)^2.
\]

Hence the matrix flow solves
\[
\dot H(t) = -H(t)^2,\qquad H(0)=H_0,
\]
in the sense of functional calculus.

This is the finite-dimensional Riccati / matrix logistic decay responsible for the observed “curvature capping”.

---

## Uniform curvature cap (the “envelope” statement)

For every \(H\succeq 0\),
\[
0 \;\preceq\; \Phi_\eta(H) \;\preceq\; \frac{1}{\eta}\,I.
\]

Proof: in the diagonal basis of \(H\), every eigenvalue satisfies \(0\le \lambda/(1+\eta\lambda)\le 1/\eta\). ∎

So if a coarse-graining step produces arbitrarily large curvatures,
one Riccati step immediately enforces the universal cap \(1/\eta\), independent of dimension.

---

## Lower bound on a physical subspace (conditional but clean)

Let \(P\) be an orthogonal projector (interpreted as the “physical” subspace).
Assume a uniform curvature lower bound on that subspace:
\[
H \;\succeq\; m\,P,\qquad m>0.
\]

Then
\[
\Phi_\eta(H) \;\succeq\; \frac{m}{1+\eta m}\,P.
\]

Proof: use the spectral map \(\phi_\eta\) and monotonicity of \(\phi_\eta\) on \([0,\infty)\);
since \(H\succeq mP\) implies all eigenvalues in \(\operatorname{im}(P)\) are \(\ge m\),
they are mapped to \(\ge m/(1+\eta m)\). ∎

---

## Scale-by-scale statement for the composite map \(H \mapsto \Phi_\eta(JHJ^\top)\)

Let \(J\in\mathbb{R}^{M\times n}\) be any linear coarse-graining map.
Define one RG step as
\[
\mathcal{R}(H) := \Phi_\eta(J H J^\top).
\]

Then for every \(H\succeq 0\),
\[
0 \preceq \mathcal{R}(H) \preceq \frac{1}{\eta} I_M.
\]

So the cap is *unconditional*.

For a *lower* curvature bound on a chosen coarse physical subspace \(P_{\rm coarse}\),
one needs a stability hypothesis on \(J\) restricted to the fine physical subspace.
A sufficient condition is: there exists \(s>0\) such that
\[
J P_{\rm fine} J^\top \;\succeq\; s^2\,P_{\rm coarse}.
\]
If additionally \(H\succeq m\,P_{\rm fine}\), then
\[
J H J^\top \;\succeq\; (ms^2)\,P_{\rm coarse}
\quad\Rightarrow\quad
\mathcal{R}(H)\;\succeq\;\frac{ms^2}{1+\eta ms^2}\,P_{\rm coarse}.
\]

This is the clean form of “after coarse-graining, the envelope restores a uniform curvature bound on the physical subspace”:
the only nontrivial input is that coarse-graining does not kill the physical directions you care about.

---

## Practical diagnostic equivalences

Because \(\Phi_\eta\) is spectral and order-preserving, it is safe to apply after any projection:

- Project-then-envelope: \( \Phi_\eta(PHP) \),
- Envelope-then-project: \( P\,\Phi_\eta(H)\,P \),

agree on \(\operatorname{im}(P)\) whenever \(P\) is built from the spectral projectors of \(H\)
(e.g. “keep eigenvalues \(>\) tol”).

That is exactly the scenario in the curvature logs: the physical subspace is defined spectrally.

