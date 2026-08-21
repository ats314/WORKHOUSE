# Smooth Proxy $\widetilde z$ and Volume-Uniform Drift (Why the Lyapunov Engine Can Exist)
*(A design principle: keep generator errors proportional to badness, not volume)*

## 0. The technical pitfall this avoids

On product configuration spaces, naive Lyapunov/drift arguments often fail for an unsexy reason:

- the generator contributes an $O(1)$ “leak” per degree of freedom,
- summing over $|P(\Lambda)|$ plaquettes produces an $O(|P(\Lambda)|)$ term,
- any hoped-for **volume-uniform** drift collapses.

The project’s fix is to build a **globally smooth proxy**
\[
\widetilde z:G\to[0,2]
\]
whose outer profile is engineered so that the dangerous second-derivative terms come with $\widetilde z$-weights.

In practice, the key micro-choice is:
\[
\Phi'(0)=0
\]
for the smoothing profile $\Phi$ used to modify the trace-defect near the vacuum.

This is “small choice, big consequences” mathematics.

---

## 1. Proxy axioms (what is actually used downstream)

Let $G$ be a compact Lie group with a bi-invariant metric.
Let $z(g)$ be a class function (“distance from identity” proxy, trace-defect style).
Construct $\widetilde z$ as a globally $C^2$ class function such that:

1. **Boundedness:** $0\le \widetilde z \le 2$.
2. **Quadratic near the vacuum:** $\widetilde z(g)\sim c\,d_G(g,\mathbf 1)^2$ as $g\to \mathbf 1$.
3. **Global gradient domination:**
   \[
   |\nabla_G\widetilde z(g)|^2\le C_\nabla\,\widetilde z(g)\qquad(\forall g\in G).
   \tag{GD}
   \]
4. **Local lower bound near $\mathbf 1$ only:**
   \[
   |\nabla_G\widetilde z(g)|^2\ge c_\nabla\,\widetilde z(g)\qquad(g\in B^G_{r_\nabla}(\mathbf 1)).
   \tag{LB}
   \]

The asymmetry matters: global (LB) is typically false because class functions on compact groups have critical points away from $\mathbf 1$.

---

## 2. Lattice badness and the Lyapunov ansatz

Given a lattice $\Lambda$, define plaquette proxies $\widetilde z_p(U)=\widetilde z(U_p(U))$ and:

\[
\mathcal D_\Lambda(U)=\sum_{p\in P(\Lambda)} \widetilde z_p(U),
\qquad
\mathcal B_\Lambda(U)=\frac{1}{|P(\Lambda)|}\mathcal D_\Lambda(U).
\]

Use the Lyapunov function
\[
W_\Lambda(U)=\exp\!\big(\kappa\,\mathcal D_\Lambda(U)\big),
\qquad \kappa>0\ \text{small}.
\]

The drift computation in Part 7 has the schematic form:
\[
\frac{L_\Lambda W_\Lambda}{W_\Lambda}(U)
\ \le\
(\kappa C_V + \kappa^2 C_\Gamma)\,\mathcal D_\Lambda(U)
\ -\ 2\kappa\,\mathcal P_\Lambda(U),
\tag{Drift}
\]
where $\mathcal P_\Lambda$ is the “pairing/restoring” term.

The proxy design goal is:

- show the **positive** terms are $\propto \mathcal D_\Lambda$ (not $\propto |P|$),
- then find a strategy to extract negativity from the restoring term $\mathcal P_\Lambda$.

The first bullet is where $\Phi'(0)=0$ pays its rent: it keeps $\Delta \widetilde z$ contributions proportional to $\widetilde z$.

---

## 3. The chat’s critical diagnosis (and the honest pivot)

A tempting route is to show a deterministic global coercivity:
\[
\mathcal P_\Lambda(U)\ge \kappa_0\,\mathcal D_\Lambda(U)\quad\text{outside a core set.}
\]

The chat correctly dismantles this:

- the only robust global inequality in the files is (GD), not a global lower bound;
- cross terms in $\mathcal P_\Lambda$ are sign-indefinite and can (in principle) cancel.

So the project pivots to the structurally honest plan:

1. pick a **typical set** $K^\star$ where the hinge/HS hypothesis holds;
2. prove $K^\star$ is typical by LSI concentration (PULSE door);
3. localize from $\mu(\cdot\mid K^\star)$ to $\mu$.

This is precisely the architecture:

\[
\text{(Part 6 + Part 9) on }K^\star
\quad+\quad
\text{(Part 8 typicality)}
\quad\Longrightarrow\quad
\text{Part 10 closes.}
\]

---

## 4. A reusable principle (what could grow into “new theory”)

The smooth-proxy trick is not just cosmetic. It suggests a general recipe:

> **On compact-group product manifolds, engineer the observable so that the generator’s second-order terms are proportional to the observable (or its sum), not proportional to volume.**

This is a design principle for Lyapunov functions in geometric Gibbs measures, and is plausibly reusable for:

- other lattice gauge actions (beyond Wilson),
- sigma models,
- compact spin systems with nonconvex local energies.

---

## Source pointers in the project

- Proxy construction and global bounds: `APPENDIX_J.md` (and related proxy files).
- Drift bookkeeping: `## 7. Lyapunov drift and uniform-in-volume functional inequalities.txt`.
- Global bound used repeatedly: `|\nabla \widetilde z|^2\le C_\nabla \widetilde z$` (Appendix J).
- Typical-set localization: `## 8.1 Covariance decomposition across an event (K).txt` and Part 10.
