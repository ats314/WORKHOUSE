# SU(3) Plaquette Hessian Quantization at the Identity: \(8/3\) Plateaus and Overlap Counting

This document extracts a concrete micro-level result:  
the gauge-projected, right-invariant Hessian of a Wilson plaquette term at the identity has a highly structured spectrum.

## 1. Object of study

Consider a single SU(3) plaquette term
\[
S_p(U_0,U_1,U_2,U_3)\;=\;1-\frac{1}{3}\operatorname{ReTr}(U_0U_1U_2U_3),
\qquad U_i\in\mathrm{SU}(3).
\]
Parameterize each link as
\[
U_i(\theta_i)=\exp\!\Big(\sum_{a=1}^8 \theta_i^a\,T_a\Big),
\]
with a right-invariant coordinate chart and generators \(T_a\) normalized consistently with the implementation.

The Hessian is taken with respect to the 32 real parameters \(\{\theta_i^a\}_{i=0..3,\;a=1..8}\),
then projected to a “physical” subspace (quotienting gauge directions).

## 2. Empirical spectrum: single plaquette micro-test

From `GPT CODE PRODCUTIOPN TEST.txt`, a corrected micro-test produced:

- 32 total eigenvalues (4 links × 8 generators),
- 24 eigenvalues \(\approx 0\) (gauge/redundant directions; numerical noise at \(10^{-15}\)),
- 8 eigenvalues **exactly**
  \[
  \lambda \;=\;\frac{8}{3}\;\approx\;2.66666667.
  \]

A representative printed spectrum (excerpt):
\[
\{\underbrace{0,\dots,0}_{24\ \text{modes}},\underbrace{8/3,\dots,8/3}_{8\ \text{modes}}\}.
\]

## 3. Interpretation

This is exactly what one expects from:

- The plaquette action depending only on an 8D “plaquette” coordinate (an SU(3) degree of freedom),
- Gauge redundancy removing most directions in link space,
- A local quadratic expansion around identity giving a constant-curvature quadratic well on the physical plaquette modes.

## 4. Multi-plaquette micro-lattices: multiples of \(8/3\)

The same project file reports that on an \(L=2\) micro-lattice (where plaquettes overlap),
the positive spectrum organizes into plateaus at
\[
\frac{8}{3},\ \frac{16}{3},\ \frac{24}{3}=8,\ \frac{32}{3},\ \dots
\]
i.e. integer multiples
\[
\lambda \approx k\cdot\frac{8}{3}.
\]

### Working theory (overlap counting)
Each plaquette contributes a local Hessian on its plaquette degrees of freedom with curvature \(8/3\).
When a physical mode “touches” \(k\) plaquettes, the quadratic form contributions add, giving eigenvalue \(\approx k(8/3)\).

This is a discrete, testable structural claim, and it ties directly to:
- the existence of a convex core (many modes have strictly positive curvature),
- the organization of curvature by lattice combinatorics (plaquette overlap graph).

## 5. Why this matters

This kind of quantized, positive semidefinite local curvature is precisely what one wants for:

- **Bakry–Émery curvature lower bounds** in a neighborhood of identity,
- **coercivity** and **local log-Sobolev** heuristics,
- a quantitative “local mass term” that can, in principle, survive coarse-graining.

It also provides a clean micro-object that can be matched to analytic Lie-algebra expansions.

## 6. Next steps that would convert this into a publishable lemma

1. **Write the analytic expansion** of \(S_p\) around identity in the same coordinate normalization and derive the coefficient \(8/3\).
2. **Prove the plateau-multiplicity rule** on small lattices by explicitly constructing the plaquette overlap matrix.
3. **Generalize to SU(2) and SU(N)** and show the constant is proportional to the quadratic Casimir in the chosen normalization.
4. **Connect to dynamics:** show that in the convex core, the Langevin generator has a curvature-dimension lower bound \(CD(\rho,\infty)\).

Even without the full analytic proof, the simulation evidence is strong enough to serve as a guiding constraint.
