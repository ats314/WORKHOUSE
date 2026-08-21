# Polarity of Reducible Gauge Configurations: Capacity-Zero Singular Strata

## 1. What “reducible” means (analytic version)

Let \(A\) be a connection (continuum or lattice). “Reducible” means \(A\) has a nontrivial stabilizer: there exists \(\xi\neq 0\) such that
\[
D_A \xi = 0.
\]
Equivalently, the gauge orbit of \(A\) has smaller dimension than generic orbits.

For functional inequalities and diffusions (Langevin), these points are scary because the gauge quotient is singular there (Gribov-type pathology). The project’s move is: **they are polar**.

## 2. Gaussian reference measure and (1,2)-capacity

Let \((E,\gamma)\) be an abstract Wiener space (e.g. Sobolev completion of gauge fields with a Gaussian reference measure). The (1,2)-capacity associated to the Ornstein–Uhlenbeck Dirichlet form is
\[
\mathrm{Cap}_{1,2}(A) \;=\; \inf\left\{\|u\|_{W^{1,2}(\gamma)}^2 \;:\; u\ge 1 \text{ on a nbhd of }A\right\}.
\]
A set of capacity zero is **polar**: the associated diffusion almost surely never hits it, and one can remove it without changing the Dirichlet form domain.

## 3. Core polarity lemma (infinite codimension ⇒ polar)

A classical (Gaussian) fact: any “thin” set like a closed affine subspace of infinite codimension has \(\mathrm{Cap}_{1,2}=0\).  

The project argues reducibles lie in a countable union of such thin sets by analyzing the constraint
\[
D_A\xi = 0,
\]
which, for fixed \(\xi\), defines an affine subspace in \(A\)-space. The union over \(\xi\) can be controlled by separability / countability reductions.

Thus:
\[
\mathcal{R} := \{A:\exists \xi\neq 0,\; D_A\xi=0\}\quad\text{is polar.}
\]

## 4. Stability under bounded density perturbations

The YM measure is not Gaussian, but (at finite cutoff) is often absolutely continuous w.r.t. a Gaussian reference. A key technical point is that **capacity-zero sets remain capacity-zero** under changing the measure by a bounded density:
\[
d\mu = f\,d\gamma,\qquad 0<c\le f\le C<\infty
\quad\Longrightarrow\quad
\mathrm{Cap}^\mu(A)=0\iff \mathrm{Cap}^\gamma(A)=0.
\]
This lets the polarity statement transfer from Gaussian to a class of interacting measures (at least locally / under truncation assumptions).

## 5. Lattice version (finite-dimensional geometry)

On a finite lattice, reducibility is an algebraic condition on finitely many group variables. Typically the reducible locus is a proper algebraic subset of positive codimension, hence Lebesgue-measure zero in exponential coordinates. Capacity arguments are overkill in finite dimension, but useful for the continuum limit story.

## 6. Why this matters for the “curvature → gap” program

Functional inequality proofs (LSI, Poincaré) are Dirichlet-form statements. If the bad set is polar, then:

- diffusion-based arguments can ignore it,
- one can treat the configuration manifold as “essentially smooth” from the viewpoint of the form,
- gauge fixing singularities are demoted from a hard obstruction to a measure-zero / capacity-zero technicality.

In other words: polarity is a plausible analytic way to **get around Gribov** without pretending it doesn't exist.

## 7. What’s needed next

To truly leverage this in YM:

1. specify the Sobolev/Wiener structure for the chosen continuum limit;
2. prove the YM cutoff measure is a bounded density perturbation of the chosen Gaussian reference on the region of interest (or use local comparison);
3. integrate this with the convex-core / vHJ curvature propagation steps.

The attractive feature is that polarity is not a “physics handwave”; it is a crisp analytic statement amenable to computer-assisted or classical proofs.
