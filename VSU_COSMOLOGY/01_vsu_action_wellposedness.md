# Vacuum Stiffness Gravity: Convex Variational Principle, Force Law, and Well-Posedness

> Curated extraction from the project’s *Vacuum Stiffness Unification (VSU)* files:
> `01.1_Action_and_Field_Equations.md`, `02.1_Force_Law_and_Asymptotics.md`,
> `02.2_BTFR_Derivation.md`, `energetic_origin_of_screening_via_convex_vacuum_hamiltonian.md`,
> `global_well_posedness_of_the_vacuum_stiffness_poisson_equation.md`.

## 1. Action and Euler–Lagrange equation

A clean starting point is a **nonrelativistic** action functional for a scalar potential $\Phi$,
with a nonlinear dependence on the field gradient magnitude:
\[
S[\Phi]
=
\frac{1}{8\pi G}\int_{\mathbb R^3} a_0^2\,f\!\left(\frac{|\nabla\Phi|^2}{a_0^2}\right)\,d^3x
\;-\;
\int_{\mathbb R^3} \rho\,\Phi\,d^3x,
\]
where $a_0$ sets the crossover scale and $f$ encodes the vacuum “stiffness law”.

Varying $\Phi$ yields a **quasilinear Poisson equation**
\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)
=
4\pi G\rho,
\qquad
\mu(x)=1-e^{-x}.
\]
This can be read as a nonlinear constitutive medium:
the vacuum behaves like a nonlinear dielectric with saturation $\mu\to 1$ in strong fields.

---

## 2. Point-mass force law and asymptotics

For a spherically symmetric mass $M$ (outside the source),
the field equation reduces to a scalar constitutive relation between
\[
g(r):=|\nabla\Phi(r)|,\qquad
g_N(r)=\frac{GM}{r^2}:
\]
\[
\boxed{
g\,\mu\!\left(\frac{g}{a_0}\right) = g_N.
}
\]

### Deep weak-field limit ($g\ll a_0$)

Using $\mu(x)\sim x$ for small $x$, one gets
\[
g\left(\frac{g}{a_0}\right)\approx g_N
\quad\Rightarrow\quad
\boxed{g\approx \sqrt{a_0 g_N}=\frac{\sqrt{GM a_0}}{r}.}
\]
This is the standard MOND-like scaling, but here it arises from a convex Hamiltonian choice.

### Strong-field (screened) limit ($g\gg a_0$)

Using $\mu(x)\to 1$, one gets
\[
\boxed{g\approx g_N\quad\text{(Newtonian recovery).}}
\]

### Screening radius

Define the transition by $g_N(r_s)=a_0$. For a point mass:
\[
\boxed{r_s(M)=\sqrt{\frac{GM}{a_0}}.}
\]
So the interior of a sufficiently compact system is automatically Newtonian.

---

## 3. Energetic origin of screening (the convexity move)

A key conceptual novelty in these notes is that “screening” is not an extra rule.
It is forced by convexity of the Hamiltonian density.

With $y:=|\nabla\Phi|/a_0$, the (nonrelativistic) Hamiltonian density can be written as
\[
\mathcal H(y)\propto a_0^2\left(y-1+e^{-y}\right).
\]
Then:
- $\mathcal H''(y)=e^{-y}>0$, i.e. **strict convexity**.
- For $y\gg 1$, the density becomes effectively **quadratic in fluctuations**, so Newtonian behavior is the tangent theory.
- Large gradients are energetically expensive; the field “prefers” the Newtonian branch locally.

This is the structural reason the model behaves like a nonlinear medium that saturates in strong environments.

---

## 4. Global well-posedness (existence + uniqueness) for the quasilinear Poisson problem

On a bounded smooth domain $\Omega\subset\mathbb R^3$ with Dirichlet data,
the Poisson problem
\[
\nabla\cdot\!\left(\mu\!\left(\frac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\right)=4\pi G\rho,
\qquad
\Phi|_{\partial\Omega}=\Phi_D
\]
is treated variationally.

Define the energy
\[
\mathcal E[\Phi]
=
\frac{a_0^2}{8\pi G}\int_\Omega
\left(|\nabla\Phi|-a_0+a_0e^{-|\nabla\Phi|/a_0}\right)\,dx
\;-\;
\int_\Omega \rho\,\Phi\,dx.
\]

### Theorem (sketch)
If $\rho\in L^2(\Omega)$ and $\Phi_D\in H^{1/2}(\partial\Omega)$, then:
1. $\mathcal E$ is coercive and strictly convex on the affine space $V_D=\{\Phi\in H^1(\Omega):\Phi|_{\partial\Omega}=\Phi_D\}$.
2. There exists a **unique** minimizer $\Phi\in V_D$.
3. The minimizer is the unique weak solution of the field equation.
4. The solution depends continuously on $(\rho,\Phi_D)$.

This is unusually clean for a nonlinear gravity modification: the same constitutive law
that produces MOND-like scaling also yields uniqueness/stability automatically.

---

## 5. BTFR as a theorem, not a fit

For circular orbits in the deep regime, the relation $g=v^2/r$ with
$g=\sqrt{GM a_0}/r$ gives
\[
\boxed{
v^4 = GM a_0.
}
\]
This is the baryonic Tully–Fisher relation (BTFR) emerging analytically from the force law.

---

## 6. What’s “theory-worthy” here

The best new-theory seed is **not** “modified gravity” per se.
It’s the organizing principle:

> **Convex vacuum energy density $\Rightarrow$ uniqueness + screening + controlled weak-field enhancement.**

That triad is rare: most nonlinear modifications buy one of these and pay with the others.

---

## Further work that would expand this into a publishable theory package

1. **Boundary-sensitive EFE derivations.** Formalize the external-field effect as a theorem about linearization of the energy around a strong background field.
2. **Rigorous regularity theory.** Upgrade weak solutions to $C^{1,\alpha}$ (or better) under mild assumptions on $\rho$.
3. **Relativistic completion consistency.** Use the hyperbolicity file(s) to pin down the covariant PDE class compatible with the nonrelativistic limit.
4. **Data-facing priors.** The model’s $\mu$ is specific; derive which class of $\mu$ preserve convexity + well-posedness and how that maps to lensing/ISW signatures.
