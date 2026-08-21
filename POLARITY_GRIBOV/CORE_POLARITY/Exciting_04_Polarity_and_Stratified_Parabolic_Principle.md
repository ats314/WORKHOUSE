# Exciting Extract 04 — Polarity + Stratified Parabolic Comparison (A “Singularities Don’t Matter” Principle)

## 1. Why this is exciting

Gauge theories have singular strata (reducible connections, orbit-type singularities).  
Many analytic mechanisms (maximum principles, comparison theorems, PDE arguments) are proven on smooth manifolds and can break down in the presence of singular sets.

This extract isolates a powerful idea:

> If the singular set is **polar** (capacity zero) for the relevant Dirichlet form, then the associated diffusion **almost surely never hits it**, and parabolic comparison/maximum principles on the regular stratum behave as if the singular set were not there.

This connects three normally separate worlds:

- infinite-dimensional Gaussian potential theory,
- stratified geometry of gauge orbit spaces,
- parabolic comparison arguments for curvature-eigenvalue flows.

---

## 2. Capacity and polarity (Dirichlet form viewpoint)

Let \((\Omega,\mathcal F,\mu)\) be a probability space equipped with a symmetric Dirichlet form \((\mathcal E,\mathcal D(\mathcal E))\) on \(L^2(\mu)\) and associated Markov process \(X_t\) (Hunt process).

For a measurable set \(A\subset\Omega\), define the (1-)capacity
\[
\mathrm{Cap}(A)
:= \inf\Bigl\{\ \mathcal E(u,u)+\|u\|_{L^2(\mu)}^2\ :\ u\in\mathcal D(\mathcal E),\ u\ge 1\ \mu\text{-a.e. on a neighborhood of }A\ \Bigr\}.
\tag{2.1}
\]

> **Definition 2.1 (Polar set).**  
> A set \(A\) is **polar** if \(\mathrm{Cap}(A)=0\).  
> Intuitively: the process \(X_t\) “cannot see” \(A\) from the perspective of energy.

A classical theorem in Dirichlet-form potential theory says:

> **Fact (Polarity \(\Rightarrow\) avoidance).**  
> If \(\mathrm{Cap}(A)=0\), then starting from \(\mu\)-quasi-every point, the process \(X_t\) almost surely never hits \(A\) in finite time.

(“quasi-every” means outside another polar set.)

---

## 3. A parabolic maximum principle on a stratified space (mechanism)

Let \(\mathcal M\) be a stratified space with regular stratum \(\mathcal M_{\mathrm{reg}}\) and singular set \(\Sigma := \mathcal M\setminus\mathcal M_{\mathrm{reg}}\).

Assume:

1. The diffusion generator \(L\) is well-defined on \(\mathcal M_{\mathrm{reg}}\) and symmetric w.r.t. a measure \(\mu\).
2. \(\Sigma\) is **polar** for the Dirichlet form induced by \(L\) (capacity zero).

Consider a semilinear inequality on \(\mathcal M_{\mathrm{reg}}\):
\[
\partial_t u \ \ge\ Lu + F(u),
\qquad F \text{ nondecreasing.}
\tag{3.1}
\]

### Theorem 3.1 (Stratified parabolic comparison via polarity)

If \(u(0,\cdot)\ge 0\) on \(\mathcal M_{\mathrm{reg}}\), then \(u(t,\cdot)\ge 0\) for all \(t>0\) on \(\mathcal M_{\mathrm{reg}}\).

**Proof sketch (probabilistic comparison).**
Represent \(u\) along diffusion trajectories using a (super)martingale/Feynman–Kac argument on exhaustion domains \(D_n\Subset\mathcal M_{\mathrm{reg}}\) avoiding \(\Sigma\). The standard smooth-manifold maximum principle applies on each \(D_n\), and polarity ensures the process almost surely never reaches \(\Sigma\) (no boundary condition is imposed there). Letting \(n\to\infty\) yields the global nonnegativity conclusion. ∎

**Interpretation.**
Polarity makes the singular set “invisible” to the diffusion, so comparison principles can be run entirely on \(\mathcal M_{\mathrm{reg}}\) without needing boundary data on \(\Sigma\).

---

## 4. Why reducibles might be polar: an infinite-codimension heuristic made precise

In gauge theory, \(\Sigma\) is the reducible stratum. A key heuristic is:

- reducibles have *infinite codimension* in the Sobolev configuration space,
- infinite-codimension affine subspaces are polar for Gaussian reference measures.

A concrete “infinite rank” lemma supporting this is:

### Lemma 4.1 (Infinite rank from a covariantly constant field)

Let \(A\) be a connection on a principal \(G\)-bundle over a compact manifold.  
If \(\xi\neq 0\) is a covariantly constant adjoint field (\(D_A\xi=0\)), consider the linear map
\[
T_\xi:\ a \mapsto [a,\xi]
\]
between Sobolev spaces of 1-forms (one order of regularity lost). Then \(T_\xi\) has **infinite rank**, hence the kernel (tangent directions that commute with \(\xi\)) has **infinite codimension**.

**Idea of proof.**
Since \(\xi\) is continuous (for Sobolev index \(k>2\) in 4D), pick infinitely many disjoint small open sets where \(\xi\neq 0\) and test 1-forms supported in each set to produce infinitely many independent images under \(T_\xi\). ∎

### Theorem 4.2 (Gaussian polarity of infinite-codimension affine subspaces)

Let \(\mu_0\) be a Gaussian measure on a separable Hilbert space \(H\).  
Any affine subspace of infinite codimension is polar (capacity zero) for the Ornstein–Uhlenbeck Dirichlet form.

**Status.**
This is a known direction in infinite-dimensional potential theory; making it fully rigorous requires importing established results on capacities for Gaussian measures / OU processes.

**Application idea.**
If the reducible stratum \(\Sigma\) can be realized (locally) as a union of infinite-codimension affine slices (as suggested by Lemma 4.1), then \(\Sigma\) is polar in the Gaussian reference frame. One then seeks absolute continuity/control transferring polarity to the interacting Yang–Mills measure.

---

## 5. What theory this points toward

This extract is pointing at a larger, very usable general theory:

> **Parabolic comparison on stratified configuration spaces with polar singular strata.**

Such a theory would apply to:

- gauge orbit spaces and moduli spaces (reducibles, orbifold strata),
- stochastic quantization flows on quotient spaces,
- tensor maximum principles for curvature quantities defined only on regular strata.

The key technical backbone is Dirichlet-form potential theory: once a set has capacity zero, you can often ignore it for diffusion-driven PDE arguments.

---

## 6. Next work needed (to make it solid and publishable)

1. **Choose the precise Dirichlet form** (Gaussian OU vs Yang–Mills interacting diffusion).  
2. **Prove polarity** of the reducible stratum for the chosen form (or prove absolute continuity transfers polarity).  
3. **Build the parabolic comparison principle** on the regular stratum with careful domain/exhaustion arguments.  
4. **Apply to a concrete PDE quantity** (e.g., minimal eigenvalue of a Hessian/curvature tensor evolving under an RG/PBH flow).

The intellectual punchline is simple and powerful:

\[
\boxed{\ \text{If }\Sigma\text{ is polar, then }\Sigma\text{ cannot kill positivity arguments.}\ }
\]
