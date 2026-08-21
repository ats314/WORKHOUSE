# BEST_02 — Codimension-2 Log Potential from a Massive Bulk Field with a Constraint Source

## 1. Setup in the project notes

The project’s `WIZ 3.txt` defines a bulk “rigidity” functional with mass scale \(\mu\) and a source supported on a submanifold \(\Sigma\).

### 1.1 Bulk functional (quadratic, local, coercive)

\[
S_{\rm bulk}[\Phi]
=
\frac12\int_M \Bigl(|\nabla\Phi|^2+\mu^2\Phi^2\Bigr)\,d{\rm vol}.
\]

### 1.2 Constraint/source coupling on \(\Sigma\)

For \(f\in L^2(\Sigma)\),
\[
S_{\rm constr}[\Phi]
=
-\int_\Sigma f\,\Phi\,d{\rm vol}_\Sigma.
\]

Total action:
\[
S[\Phi]=S_{\rm bulk}[\Phi]+S_{\rm constr}[\Phi].
\]

No additional bulk linear terms are introduced in the project note; the coupling is geometric (supported on \(\Sigma\)).

---

## 2. Euler–Lagrange equation (as derived in `WIZ 3.txt`)

Let \(\delta\Phi\) be a compactly supported variation in \(M\). Then
\[
\delta S
=
\int_M \left(\nabla\Phi\cdot\nabla\delta\Phi+\mu^2\Phi\,\delta\Phi\right)\,d{\rm vol}
-
\int_\Sigma f\,\delta\Phi\,d{\rm vol}_\Sigma.
\]

Integrate by parts in \(M\):
\[
\int_M \nabla\Phi\cdot\nabla\delta\Phi\,d{\rm vol}
=
-\int_M (\Delta\Phi)\,\delta\Phi\,d{\rm vol},
\]
discarding boundary terms (compact support).

Hence
\[
\delta S
=
-\int_M (\Delta\Phi-\mu^2\Phi)\,\delta\Phi\,d{\rm vol}
-
\int_\Sigma f\,\delta\Phi\,d{\rm vol}_\Sigma.
\]

Stationarity for arbitrary \(\delta\Phi\) gives the distributional equation
\[
\boxed{
(\Delta-\mu^2)\Phi=-f\,\delta_\Sigma.
}
\]

---

## 3. Codimension-2 Green function and logarithmic regime (as recorded in `WIZ 2.txt`)

For the 2D operator \((\Delta_2-\mu^2)\), the project note states that the Green function is
\[
(\Delta_2-\mu^2)G_\mu(R)=\delta^{(2)}(R),
\qquad
\boxed{
G_\mu(R)=\frac{1}{2\pi}K_0(\mu R),
}
\]
with modified Bessel function \(K_0\).

The same note records the small-argument asymptotic
\[
\boxed{
K_0(\mu R)= -\ln(\mu R)+\gamma + O\!\bigl((\mu R)^2\bigr)
\qquad (\mu R\ll 1),
}
\]
where \(\gamma\) is the Euler–Mascheroni constant.

---

## 4. Disk-like (planar) localized source \(\Rightarrow\) outer log potential

Assume a surface-density-type source supported on \(\Sigma\simeq\mathbb{R}^2\) with compact (or rapidly decaying) support, with total “mass” parameter
\[
M_b := 2\pi\int_0^\infty dR\,R\,\Sigma_b(R)
\]
as defined in the note.

Then for radii outside the baryons but inside the mass-gap scale,
\[
R_b\ll R\ll \mu^{-1},
\]
the project note states the convolution yields the leading behavior
\[
\boxed{
\Phi(R)\approx -\frac{M_b}{2\pi}\ln R +{\rm const}.
}
\]

Differentiating gives a \(1/R\) acceleration:
\[
\boxed{
g(R)=-\partial_R\Phi(R)\approx \frac{M_b}{2\pi}\frac{1}{R}.
}
\]

Circular speed then satisfies
\[
V^2(R)=R\,g(R)\approx \frac{M_b}{2\pi},
\]
i.e. asymptotically flat rotation curves in that regime.

*Project note limitation:* the overall physical coupling (e.g. Newton’s \(G\) and/or an \(a_0\)-type scale) is not explicitly carried through in `WIZ 2.txt`; the constants above should be read exactly as written there.

---

## 5. Connection to the anti-kernel multiplier

The anti-kernel multiplier used in the SPARC scripts is
\[
M_{\rm anti}(k)=1+\frac{\mu^2}{k^2}.
\]

The added term \(\mu^2/k^2\) is the hallmark of an inverse-Laplacian contribution, which in two dimensions produces logarithmic kernels.

The project’s novelty candidate is the attempt to connect:

- the *numerical* Hankel-space IR boost \(1+\mu^2/k^2\) (BEST\_01), with
- a *local* massive bulk action plus a lower-dimensional constraint/source producing log behavior (this document).

---

## Source pointers (project-local)

- `WIZ 3.txt`: constrained bulk functional and Euler–Lagrange derivation.
- `WIZ 2.txt`: stated form of the 2D massive Green function and its small-\(R\) asymptotic; stated log-potential and flat-curve consequence.
- `GALAXYRUN.ipynb` / `GALAXY RUNS.pdf`: anti-kernel definition \(M_{\rm anti}(k)=1+\mu^2/k^2\).
