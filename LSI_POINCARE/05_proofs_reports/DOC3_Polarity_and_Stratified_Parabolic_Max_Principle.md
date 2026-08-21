# Polarity of Reducibles and a Stratified Parabolic Maximum Principle

## Abstract

Gauge orbit spaces are stratified: a smooth **regular stratum** \(\mathcal M_{\mathrm{reg}}\) and a singular locus \(\Sigma\) (reducible connections) where the quotient geometry degenerates.  
This note packages two ideas from the project:

1. A geometric observation: the reducible locus is *infinitely thin* (infinite codimension) in Sobolev configuration space.
2. A PDE mechanism: if \(\Sigma\) has **capacity zero** (is *polar*) for the Dirichlet form underlying the diffusion generator, then parabolic comparison/maximum principles on \(\mathcal M_{\mathrm{reg}}\) behave as if \(\Sigma\) were absent—yielding positivity propagation for supersolutions.

This “polarity → no-boundary-for-maximum-principle” bridge is a key technical idea for propagating curvature/Hessian positivity along RG-type flows on gauge orbit spaces.

---

## 1. Stratified geometry and the role of reducibles

Let \(\mathcal A\) be a Sobolev space of connections (modeled on a Hilbert space \(H=L^2_k\)), and \(\mathcal G\) the gauge group. The quotient \(\mathcal M=\mathcal A/\mathcal G\) is typically stratified:

- \(\mathcal M_{\mathrm{reg}}\): irreducible connections (principal stratum), a smooth Hilbert (or finite-dimensional after cutoff) manifold.
- \(\Sigma\subset \mathcal M\): reducible strata where stabilizers are nontrivial; geometric tensors can blow up.

For RG/PDE arguments, \(\Sigma\) is the potential spoiler: it can act like a boundary/singularity where maximum principles might fail—unless it is “small enough” in the potential-theoretic sense.

---

## 2. Infinite codimension of reducibles (geometric thinness)

### Theorem (Infinite codimension of reducible stratum; local tangent statement)

Let \(\xi\in L^2_k(M,\mathrm{ad}\,P)\) be a nonzero covariantly constant field, \(D_A\xi=0\). Consider
\[
T_\xi:\ H=L^2_k(M,\Lambda^1\otimes\mathrm{ad}\,P)\to H'=L^2_{k-1}(M,\Lambda^1\otimes\mathrm{ad}\,P),\qquad
T_\xi(a)=[a,\xi].
\]
Then \(T_\xi\) has infinite rank. Consequently, \(\ker T_\xi\) (the tangent space to the \(\xi\)-reducible locus) has infinite codimension.

### Proof idea (disjoint support construction)

Because \(k>2\) implies continuity, \(\xi\neq 0\) on some open set \(U\subset M\). Choose infinitely many disjoint open subsets \(U_n\subset U\) and test one-forms \(\alpha_n\) supported in \(U_n\).  
Then \([\,\alpha_n\otimes Y,\xi\,]\) are nonzero and mutually orthogonal in \(H'\) because their supports are disjoint. Hence \(\mathrm{Ran}(T_\xi)\) is infinite-dimensional, i.e. \(T_\xi\) has infinite rank.

---

## 3. Capacity, polar sets, and “avoidance”

Let \((\mathcal E,\mathsf D(\mathcal E))\) be the (quasi-regular) Dirichlet form on \(L^2(\mathcal M,\mu)\) associated to a symmetric diffusion generator \(L\) on the regular stratum. The \(\mathcal E\)-capacity of a set \(A\) is defined by
\[
\mathrm{Cap}_\mathcal E(A)
:=
\inf\Bigl\{\mathcal E_1(f,f)\ :\ f\in\mathsf D(\mathcal E),\ f\ge 1\ \text{q.e. on }A\Bigr\},
\qquad
\mathcal E_1(f,f)=\mathcal E(f,f)+\|f\|_2^2.
\]
A set \(\Sigma\) is **polar** if \(\mathrm{Cap}_\mathcal E(\Sigma)=0\).

Standard Dirichlet-form theory links polarity to hitting probabilities: if \(\Sigma\) is polar, then the Markov process \(X_t\) associated to \(L\) started from a quasi-everywhere point \(x\in\mathcal M_{\mathrm{reg}}\) satisfies
\[
\mathbb P_x\bigl(\exists t>0:\ X_t\in\Sigma\bigr)=0.
\]
Intuitively: the diffusion almost surely never hits \(\Sigma\) in finite time.

---

## 4. Stratified parabolic maximum principle (mechanism)

### Theorem (Parabolic comparison on stratified spaces; polarity removes boundary)

Let \(\mathcal M\) be stratified with regular stratum \(\mathcal M_{\mathrm{reg}}\) and singular set \(\Sigma\). Assume:

1. \(\Sigma\) is polar for the Dirichlet form (capacity zero).
2. \(u(t,x)\) is a supersolution on \((0,T]\times \mathcal M_{\mathrm{reg}}\) of
   \[
   \partial_t u \;\ge\; L u + F(u),
   \]
   where \(F\) is non-decreasing (comparison-friendly).
3. \(u(0,x)\ge 0\) on \(\mathcal M_{\mathrm{reg}}\).

Then \(u(t,x)\ge 0\) for all \(t\in(0,T]\) and all \(x\in\mathcal M_{\mathrm{reg}}\).

### Proof mechanism (semigroup/avoidance)

- On a smooth manifold, the parabolic maximum principle (or equivalently semigroup comparison) yields positivity propagation for \(\partial_t u\ge Lu+F(u)\) when there is no “active boundary.”
- Polarity ensures that the process \(X_t\) driven by \(L\) never hits \(\Sigma\) almost surely, so \(\Sigma\) does not impose boundary interactions in the probabilistic representation (Feynman–Kac / stochastic flow).
- Therefore the standard positivity/maximum-principle argument on \(\mathcal M_{\mathrm{reg}}\) carries over to the stratified space: \(\Sigma\) is “invisible” to the dynamics for finite times.

---

## 5. How this plugs into curvature/Hessian positivity propagation

In the Yang–Mills program, \(u(t,x)\) is taken to be (a bound on) the smallest eigenvalue of a curvature or Hessian tensor. Typical evolution inequalities have the form
\[
\partial_t u \;\ge\; L u - 2u^2 + \sigma_\ast,
\]
so positivity of \(u\) is an invariant region provided \(\Sigma\) does not create boundary pathology. The polarity + stratified maximum principle gives exactly that missing step.

---

## 6. What is still conjectural in the polarity step

The “infinite codimension” theorem is robust. The leap from infinite codimension to polarity requires additional structure:

- For Ornstein–Uhlenbeck (OU) processes on infinite-dimensional Gaussian spaces, it is plausible (and often true) that closed affine subspaces of infinite codimension are polar.
- To conclude reducibles are polar, one needs a decomposition of the reducible set \(\Sigma\) as a **countable union** of such polar pieces (or a direct capacity estimate for \(\Sigma\)).

This is a concrete, well-posed research task: it lives at the intersection of gauge orbit stratification, abstract Wiener space theory, and Dirichlet-form potential theory.
