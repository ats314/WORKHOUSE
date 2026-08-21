# Curvature-Defect Rigidity and the Obstruction Principle
*(a scale-monotone “defect ledger” that isolates where an interacting mass gap can fail)*

## 1. Setup: physical Hessian and defect density

Fix a lattice spacing \(a>0\) and a finite lattice (volume suppression for notation). Let \(\mathcal C_a\) be the configuration manifold (e.g. \(G^{E(\Lambda)}\) with a product bi-invariant metric), and let \(\mu_a\) be the Wilson-type Gibbs measure.

Assume there is a **gauge-orthogonal physical projection**
\[
\Pi_{\mathrm{phys}}: T\mathcal C_a \to T\mathcal C_a
\]
whose kernel is exactly gauge directions and whose image is a fixed “physical” subbundle (discrete Hodge decomposition / coexact projection).

Define the **physical Hessian**
\[
\mathsf H_a(U)
:= \Pi_{\mathrm{phys}}\ \nabla^2 S^{(a)}(U)\ \Pi_{\mathrm{phys}}
\quad
\text{acting on }\Pi_{\mathrm{phys}} T_U\mathcal C_a.
\]

Let \(\kappa_*>0\) be a stiffness benchmark (e.g. the minimal physical Hessian eigenvalue on a tubular neighborhood of the flat stratum, established by a local Hodge/coercivity lemma).

### Definition 1.1 (Curvature defect density)
\[
\delta_a(U)
:=\max\{0,\ \kappa_* - \lambda_{\min}(\mathsf H_a(U))\}.
\]

### Definition 1.2 (Curvature-defect invariant)
\[
\Phi(a):=\int_{\mathcal C_a}\delta_a(U)\,d\mu_a(U).
\]

Heuristic reading:
- \(\delta_a(U)=0\) means “configuration \(U\) is stiff in all physical directions.”
- \(\Phi(a)\) measures the **average amount of physical softness** of the action at scale \(a\).

---

## 2. Coarse-graining monotonicity (the key algebraic step)

Let \(a'<a\) represent a coarser description and let
\[
\pi_{a\to a'}:\mathcal C_a \to \mathcal C_{a'}
\]
be a measurable, gauge-equivariant block map (a coarse-graining projection). Assume \(\mu_{a'}=(\pi_{a\to a'})_\#\mu_a\).

Define the \(\sigma\)-algebra \(\mathcal G_{a'}:=\sigma(\pi_{a\to a'})\). Assume that the coarse physical Hessian is the quadratic-form conditional expectation
\[
\mathsf H_{a'} = \mathbb E[\mathsf H_a\mid \mathcal G_{a'}],
\]
in the sense that for every physical unit vector \(v\),
\[
\langle v,\mathsf H_{a'}(\pi(U))v\rangle
=
\mathbb E[\langle v,\mathsf H_a(U)v\rangle\mid \pi(U)].
\]

### Proposition 2.1 (Hessian spectral floor is monotone under coarse-graining)
For \(\mu_{a'}\)-a.e. \(U'\),
\[
\boxed{
\lambda_{\min}(\mathsf H_{a'}(U'))
\ \ge\
\mathbb E\!\left[\lambda_{\min}(\mathsf H_a(U))\mid \pi_{a\to a'}(U)=U'\right].
}
\]

**Proof.**
Fix \(U'\) and any physical unit vector \(v\). Then
\[
\langle v,\mathsf H_{a'}(U')v\rangle
=
\mathbb E[\langle v,\mathsf H_a(U)v\rangle\mid \pi(U)=U']
\ge
\mathbb E[\lambda_{\min}(\mathsf H_a(U))\mid \pi(U)=U'],
\]
since \(\langle v,\mathsf H_a(U)v\rangle\ge \lambda_{\min}(\mathsf H_a(U))\) pointwise in \(U\). Taking the infimum over \(v\) yields the claim. \(\square\)

This is exactly conditional spectral floor monotonicity, specialized to the physical Hessian.

### Corollary 2.2 (Defect decreases under coarse-graining)
For \(a'<a\),
\[
\boxed{
\Phi(a')\ \le\ \Phi(a).
}
\]

**Proof.**
Apply Proposition 2.1 and the convex decreasing penalty \(\phi(x)=(\kappa_*-x)_+\), then integrate using the pushforward relation \(\mu_{a'}=\pi_\#\mu_a\). \(\square\)

So \(\Phi(a)\) is a **scale-monotone ledger**: coarse observation cannot increase the average softness.

---

## 3. Rigidity principle: vanishing defect forces Gaussianity

The next statement is conditional on a standard Taylor-control hypothesis. It is the “rigidity seam” that turns the defect ledger into a structural obstruction.

### Assumption (Taylor remainder control)
There exists \(R>0\) and constants \(C_3\) independent of \(a\) such that on the physically small-field region (e.g. a tube of radius \(R\) around the flat stratum),
\[
S^{(a)}(U_0\exp X)
=
S^{(a)}(U_0) + \frac12\langle X,\mathsf H_a(U_0)X\rangle + \mathcal R_a(X),
\]
with cubic control
\[
|\mathcal R_a(X)|\le C_3 \|X\|^3,
\qquad \|X\|\le R,
\]
for physical \(X\) in exponential coordinates.

*(This is the usual “action is smooth, cubic remainder is controlled uniformly” hypothesis.)*

### Theorem 3.1 (Quadratic rigidity: \(\Phi(a_n)\to0\Rightarrow\) Gaussian continuum limit)
Let \(a_n\downarrow 0\) and suppose \(\mu_{a_n}\) are OS-positive lattice measures with a continuum OS-positive limit point \(\mu\) on cylinder observables.

If
\[
\Phi(a_n)\to 0,
\]
then all finite-dimensional cylinder marginals of \(\mu\) are Gaussian, hence the OS-reconstructed continuum theory is a free (Gaussian) field.

**Proof sketch (structural).**
\(\Phi(a_n)\to0\) means \(\delta_{a_n}(U)\to 0\) in \(L^1(\mu_{a_n})\). By Markov/Chebyshev, for large \(n\) the measure is concentrated on configurations where
\(\lambda_{\min}(\mathsf H_{a_n}(U))\ge \kappa_*-\varepsilon\).
On the small-field tube (which carries the dominant mass in a stiff regime), the Taylor remainder control implies the action is uniformly close to a quadratic form with curvature \(\approx \kappa_*\). Consequently, cylinder measures converge to Gaussians with covariance \(\kappa_*^{-1}\) on physical directions. OS positivity then pins down the reconstruction uniquely as a free theory. \(\square\)

---

## 4. The obstruction principle

### Corollary 4.1 (Obstruction principle)
If the continuum OS-positive limit of the lattice sequence is **interacting** (non-Gaussian), then
\[
\boxed{
\inf_{a>0}\Phi(a)\ >\ 0.
}
\]
In particular, an interacting limit must retain a strictly positive amount of curvature defect at every scale.

This is a clean separation of responsibilities:

- \(\Phi(a)\) is monotone under coarse-graining (pure order/conditioning).
- “\(\Phi\to0\Rightarrow\) Gaussian” is the only analytic rigidity seam.

If the continuum theory is truly interacting, the defect cannot die out.

---

## 5. Why this is potentially a new theory-building tool

This is a genuinely reusable conceptual gadget:

- define a **defect functional** that measures “how far from uniformly stiff” the theory is,
- prove it is **monotone under coarse-graining** using conditional spectral floor monotonicity,
- then prove a **rigidity theorem**: defect \(\to 0\) forces triviality.

That three-step pattern resembles classical rigidity theory, but transplanted to the geometry of gauge measures and OS reconstruction.

If it can be made fully quantitative (e.g. giving lower bounds on spectral gaps in terms of \(\Phi(a)\)), it becomes a practical “defect-to-gap” dictionary.

