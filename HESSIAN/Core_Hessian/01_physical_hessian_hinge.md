# Physical spectral floor on a small-field set via Maxwell–Calladine projection and the hinge constant

*This note distills the “matrix hinge / Hessian perturbation” mechanism into a single lemma that can be dropped into Appendix I / Part 5.*  
*Context: Wilson lattice gauge theory on a finite box; local convexity is proved only on a good set, not globally.*

---

## 1. Cochain kinematics and the Maxwell–Calladine / Bianchi exactness picture

Let $\Lambda$ be a finite cubical lattice (with periodic or wired boundary conditions as in your appendices).  
Let $\mathfrak g$ be the Lie algebra of a compact Lie group $G$ (e.g. $\mathfrak{su}(2)$).

Write $\mathcal C^k(\Lambda;\mathfrak g)$ for $\mathfrak g$-valued $k$-cochains with the $\ell^2$ cochain inner product.  
Let
\[
d_0:\mathcal C^0\to\mathcal C^1,\qquad 
d_1:\mathcal C^1\to\mathcal C^2,\qquad
d_2:\mathcal C^2\to\mathcal C^3
\]
be the usual coboundaries (discrete grad/curl/div), with adjoints $d_0^\*,d_1^\*,d_2^\*$.

The lattice exactness/Bianchi identities are
\[
d_1 d_0 = 0, \qquad d_2 d_1 = 0.
\]
In “rigidity language” (Maxwell–Calladine):
- degrees of freedom: $x\in \mathcal C^1$,
- constraints: $D x$ with $D := d_1$,
- compatibility (Bianchi): $C D=0$ with $C:=d_2$.

The *mechanism space* is $\ker D$ (curl-free modes, including gauge gradients and harmonic 1-forms).  
The *self-stress space* is $\ker D^\*$.

The “physical” subspace of 1-cochains is the orthogonal complement of mechanisms:
\[
\mathcal H_{\rm phys} \;:=\; (\ker d_1)^\perp \;=\; \overline{\operatorname{Ran}(d_1^\*)}.
\]
Define the orthogonal projection
\[
\Pi_{\rm phys} := P_{\mathcal H_{\rm phys}} = P_{(\ker d_1)^\perp}.
\]
This is the exactness-pinned version of “project away the gauge/mechanism directions”.

> **Remark (relation to Coulomb gauge).**  
> On simply connected domains without harmonic 1-forms, $(\ker d_1)^\perp$ is essentially the coexact/transverse sector.  
> If you prefer a gauge slice (e.g. Coulomb), you can replace $\Pi_{\rm phys}$ by the Coulomb projector 
> $\Pi_T = I - d_0 \Delta_0^{-1} d_0^\*$; on many boundary conditions these agree after modding out the harmonic sector.

---

## 2. The Wilson Hessian and the hinge constant

Let $M_\Lambda$ denote the lattice gauge configuration space (one group element per oriented edge), and let
\[
S_{\Lambda,\beta}(U)
\]
be the Wilson action (your Appendix A conventions).

Define the linkwise small-field set
\[
K_\Lambda(r):=\{U\in M_\Lambda : d_G(U_b,\mathbf 1) < r \ \ \forall\text{ links }b\}.
\]
(Equivalently: all link variables are within the $r$-ball of the identity in $G$.)

Let $U^{(0)}$ denote the vacuum configuration ($U_b\equiv \mathbf 1$).

### Hinge constant (uniform Hessian perturbation size)

A single scalar constant $R_W(r)$ packages the entire “Hessian drift from vacuum”:
\[
R_W(r)\;:=\;\sup_{U\in K_\Lambda(r)} \big\|\nabla^2 S_{\Lambda,\beta}(U)-\nabla^2 S_{\Lambda,\beta}(U^{(0)})\big\|_{\rm op}.
\]

Your Appendix A actually defines $R_W(r)$ **explicitly** by bounding the plaquette-level Taylor remainder and summing it into a uniform operator-norm perturbation bound.  
So this lemma treats $R_W(r)$ as a *certified input constant*.

---

## 3. Lemma: physical spectral floor on $K_\Lambda(r)$

### Lemma (physical projection + small-field spectral floor)

Define the *physical Hessian* at $U\in K_\Lambda(r)$ by
\[
\mathsf H_{\rm phys}(U)\;:=\;\Pi_{\rm phys}\,\nabla^2 S_{\Lambda,\beta}(U)\,\Pi_{\rm phys}
\quad\text{acting on }\ \mathcal H_{\rm phys}.
\]
Let
\[
\kappa_{\rm vac}
\;:=\;
\lambda_{\min}\!\big(\mathsf H_{\rm phys}(U^{(0)})\big)
=
\lambda_{\min}\!\big(\Pi_{\rm phys}\,\nabla^2 S_{\Lambda,\beta}(U^{(0)})\,\Pi_{\rm phys}\big).
\]

Assume $0<r\le r_{\rm sf}$ and the hinge bound holds, i.e. $R_W(r)<\infty$.  
Then for every $U\in K_\Lambda(r)$,
\[
\boxed{
\lambda_{\min}\!\big(\mathsf H_{\rm phys}(U)\big)
\ \ge\ 
\kappa_{\rm vac} - R_W(r).
}
\]

If in addition the vacuum Hessian admits the identification
\[
\nabla^2 S_{\Lambda,\beta}(U^{(0)}) \;=\; \alpha\, d_1^\* d_1 \;+\; \text{(gauge-fixing and/or mass terms)},
\qquad \alpha = \frac{\beta}{n\lambda_\rho},
\]
then
\[
\kappa_{\rm vac}
\ \ge\
\alpha\ \lambda_{\min}\!\big(d_1^\* d_1\big|_{\mathcal H_{\rm phys}}\big)
\quad (\text{and with a mass term }m^2I,\ \kappa_{\rm vac}\ge \alpha m^2).
\]
Hence, for $U\in K_\Lambda(r)$,
\[
\lambda_{\min}\!\big(\mathsf H_{\rm phys}(U)\big)
\ \ge\
\alpha m^2 - R_W(r),
\]
and choosing $r$ so that $R_W(r)\le \tfrac12\alpha m^2$ yields the uniform positive floor
\[
\lambda_{\min}\!\big(\mathsf H_{\rm phys}(U)\big)\ \ge\ \tfrac12\,\alpha m^2
\qquad\text{for all }U\in K_\Lambda(r).
\]

### Proof

Fix $U\in K_\Lambda(r)$. Write $H(U)=\nabla^2 S_{\Lambda,\beta}(U)$ and $H_0=\nabla^2 S_{\Lambda,\beta}(U^{(0)})$.

By definition of the hinge constant, $\|H(U)-H_0\|_{\rm op}\le R_W(r)$.

Let $x\in\mathcal H_{\rm phys}$ with $\|x\|=1$. Since $\Pi_{\rm phys}x=x$,
\[
\langle x,\mathsf H_{\rm phys}(U) x\rangle
=
\langle x, H(U) x\rangle
=
\langle x,H_0 x\rangle + \langle x,(H(U)-H_0)x\rangle
\ge
\langle x,H_0 x\rangle - \|H(U)-H_0\|_{\rm op}
\ge
\langle x,H_0 x\rangle - R_W(r).
\]
Taking the infimum over unit $x\in\mathcal H_{\rm phys}$ gives
\[
\lambda_{\min}\!\big(\mathsf H_{\rm phys}(U)\big)
\ge
\lambda_{\min}\!\big(\mathsf H_{\rm phys}(U^{(0)})\big) - R_W(r)
=
\kappa_{\rm vac}-R_W(r).
\]
The “moreover” statements follow by substituting the vacuum identification.

$\square$

---

## 4. Why this lemma is useful in your global architecture

1) **It is exactly the “Part 5 hinge” you keep pointing at.**  
Once $\kappa_{\rm vac}$ is non-collapsing in the physical sector, all the messy geometry of $G$ gets quarantined into the single scalar loss $R_W(r)$.

2) **It’s the right input for block-Gibbs / Dobrushin PI/LSI.**  
Blockwise strong convexity (in physical directions) is an immediate corollary on $K_\Lambda(r)$, which is the canonical local/core hypothesis for Poincaré/LSI via Dobrushin-type arguments.

3) **It fits the center-flux obstruction cleanly.**  
The center-flux configuration lives far outside $K_\Lambda(r)$ for small $r$, so this lemma doesn’t contradict the global counterexample. That’s not a hack; it’s the correct topology-aware geometry.

---

## 5. Next lemma to bolt on (minimal)

This hinge lemma becomes *volume-uniform* once you have a volume-uniform vacuum floor $\kappa_{\rm vac}\ge \kappa_0>0$.  
In your project, that comes from **massive** operators (or from boundary conditions), and it is exactly where the Maxwell–Calladine exactness picture supplies the right “physical subspace” and excludes kernel sectors.

