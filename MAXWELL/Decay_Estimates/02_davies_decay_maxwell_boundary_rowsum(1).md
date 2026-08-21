# Davies Decay for the Massive Maxwell Operator (and a Boundary Row-Sum Refinement)

This note extracts (and slightly re-packages) the project’s **cleanest “decay engine”**:

> A Davies/Dirichlet-form conjugation argument yields an exponential inverse-kernel bound for
> \[
> M := m^2 I + \alpha\,d_1^\ast d_1
> \quad\text{on 1-cochains,}
> \]
> with an exponent scaling like **$m$** (not $m^2$) at small mass.
>
> Moreover, you can replace the crude degree constant by a *row-sum* constant, and then refine again to a *boundary* row-sum constant $C_\partial$.

---

## 1. Setup

Let $\Lambda$ be a finite periodic $d$-dimensional cubic lattice.

Let $\mathsf H_E:=\ell^2(E(\Lambda);\mathfrak g)$ be $\mathfrak g$-valued 1-cochains on links, with $\dim\mathfrak g<\infty$.

Let $\Delta_1 := d_1^\ast d_1$ be the (ungauged) 1-form Laplacian piece appearing in the massive Maxwell operator.
Define
\[
M_\Lambda := m^2 I + \alpha \Delta_1,
\qquad m^2>0,\ \alpha>0.
\]

Let $\mathrm{dist}_E(b,b')$ be the graph distance on links where $b\sim \tilde b$ iff the stencil of $\Delta_1$ couples them (equivalently: “share a plaquette,” in the project’s Part 9).

---

## 2. Proposition 9.X (Davies-type decay, degree constant)

Let $D_E$ be a bound on the (link-graph) degree of the coupling graph.
Then for all links $b,b'$,
\[
\big|\big(M_\Lambda^{-1}\big)_{bb'}\big|_{\mathrm{op}}
\ \le\
\frac{2}{m^2}\,
\exp\!\Big(-\eta_{\mathrm{DG}}\,\mathrm{dist}_E(b,b')\Big),
\]
where
\[
\eta_{\mathrm{DG}}
=
2\,\operatorname{arsinh}\!\Big(\frac{m}{2\sqrt{\alpha D_E}}\Big)
=
\operatorname{arcosh}\!\Big(1+\frac{m^2}{2\alpha D_E}\Big).
\]

### Key asymptotic improvement vs Combes–Thomas
For $m^2\ll \alpha$,
\[
\eta_{\mathrm{DG}}
\sim
\frac{m}{\sqrt{\alpha D_E}},
\qquad\text{whereas a CT-style bound typically gives}\qquad
\eta_{\mathrm{CT}}
\sim
\frac{m^2}{\alpha D_E}.
\]
So the Davies/Dirichlet-form method is **linear in $m$** at small mass.

### Proof sketch (Davies conjugation)

Fix a target link $b'$ and define a 1-Lipschitz weight
\[
\phi(b):=\mathrm{dist}_E(b,b').
\]
For $\lambda\ge 0$, let $W_\lambda$ be multiplication by $e^{\lambda\phi}$.
Conjugate $L:=\alpha\Delta_1$ to $L_\lambda:=W_\lambda L W_\lambda^{-1}$.

1. The symmetric part satisfies
   \[
   \frac{L_\lambda+L_{-\lambda}}2 = L + Q_\lambda,
   \]
   where off-diagonal entries are multiplied by $\cosh(\lambda(\phi(b)-\phi(\tilde b)))-1$.
2. Finite range + Lipschitz $\phi$ imply $|\phi(b)-\phi(\tilde b)|\le 1$ whenever $(L)_{b\tilde b}\ne 0$.
   Hence $|\cosh(\lambda(\phi(b)-\phi(\tilde b)))-1|\le\cosh(\lambda)-1$.
3. Bounding the row-sum of $L$ by $\alpha D_E$ gives
   \[
   \|Q_\lambda\|\le \alpha D_E (\cosh\lambda-1).
   \]
4. This yields a norm bound on the conjugated semigroup:
   \[
   \|e^{-tL_\lambda}\|\le \exp\!\big(\alpha D_E(\cosh\lambda-1)t\big).
   \]
5. Using the Laplace transform
   \[
   M^{-1}=\int_0^\infty e^{-m^2 t}e^{-tL}\,dt,
   \]
   one obtains
   \[
   \|W_\lambda M^{-1}W_\lambda^{-1}\|\le \frac{1}{m^2-\alpha D_E(\cosh\lambda-1)}.
   \]
6. The kernel bound follows from
   \[
   (W_\lambda M^{-1}W_\lambda^{-1})_{bb'}
   = e^{\lambda\phi(b)} (M^{-1})_{bb'} e^{-\lambda\phi(b')} = e^{\lambda\,\mathrm{dist}_E(b,b')}(M^{-1})_{bb'}.
   \]
7. Choose $\lambda$ such that $\alpha D_E(\cosh\lambda-1)=m^2/2$, giving the stated $\eta_{\mathrm{DG}}$.

---

## 3. Proposition 9.X′ (replace degree by row-sum constant $C_0$)

Define the off-diagonal row-sum constant
\[
C_0(\Delta_1):=\max_{b}\sum_{\tilde b\ne b}\big|(\Delta_1)_{b\tilde b}\big|_{\mathrm{op}}.
\]

Then the same proof works with $\alpha D_E$ replaced by $\alpha C_0(\Delta_1)$, yielding
\[
\big|\big(M^{-1}\big)_{bb'}\big|_{\mathrm{op}}
\ \le\
\frac{2}{m^2}\,
\exp\!\Big(-\eta_{\mathrm{DG}}^{(0)}\,\mathrm{dist}_E(b,b')\Big),
\]
where
\[
\eta_{\mathrm{DG}}^{(0)}
=
2\,\operatorname{arsinh}\!\Big(\frac{m}{2\sqrt{\alpha C_0(\Delta_1)}}\Big)
=
\operatorname{arcosh}\!\Big(1+\frac{m^2}{2\alpha C_0(\Delta_1)}\Big).
\]

---

## 4. Corollary 9.X′′ (boundary row-sum constant $C_\partial$)

The Davies proof has a built-in refinement: in $Q_\lambda$ the factor
\[
\cosh(\lambda(\phi(b)-\phi(\tilde b)))-1
\]
vanishes when $\phi(b)=\phi(\tilde b)$, i.e. for “tangential” neighbors that do not cross a distance level set.

Define the **boundary row-sum constant**
\[
C_\partial(\Delta_1)
:=
\sup_{b'}\ \max_{b}\
\sum_{\substack{\tilde b\neq b\\ |\phi_{b'}(b)-\phi_{b'}(\tilde b)|=1}}
\big|(\Delta_1)_{b\tilde b}\big|_{\mathrm{op}},
\qquad
\phi_{b'}(b)=\mathrm{dist}_E(b,b').
\]

Then the same proof yields the same kernel bound with exponent
\[
\eta_{\mathrm{DG}}^{(\partial)}
=
2\,\operatorname{arsinh}\!\Big(\frac{m}{2\sqrt{\alpha C_\partial(\Delta_1)}}\Big)
=
\operatorname{arcosh}\!\Big(1+\frac{m^2}{2\alpha C_\partial(\Delta_1)}\Big).
\]

**Why this is potentially valuable.**
$C_\partial\le C_0$, often strictly.
In highly anisotropic stencils, $C_0$ is dominated by “tangential” couplings that do not contribute to moving away from the source; $C_\partial$ deletes them automatically.

---

## 5. Connection to “gauge fixing improves Combes–Thomas constants” (numerical)

If you add a gauge-fixing kinetic term (Feynman gauge),
\[
M_{\xi}:=m^2I+\alpha\,d_1^\ast d_1+\xi\,d_0d_0^\ast,
\]
then at $\xi=\alpha$ the symbol becomes diagonal (scalar Laplacians per component), and empirically the row-sum constant collapses to the scalar coordination number $2d$.

This is not a *new theorem*—it’s a numerically vivid way to see that the poor $C_0$ for curl–curl is an artifact of off-diagonal cancellations being destroyed by absolute values.

(See `05_simulation_appendix_maxwell_and_a100_su2.md`.)

---

## 6. “New theory” angle

The boundary constant $C_\partial$ suggests a general method:

> When doing Davies conjugation with a graph distance weight, the only couplings that matter are those that cross distance level sets.

This can be abstracted to other finite-range operators (random conductances, anisotropic stencils, matrix-valued Laplacians), giving an improved decay exponent controlled by a **level-set boundary norm** rather than a blunt degree/row-sum.

In continuous language, this resembles measuring a “flux” across geodesic spheres.

