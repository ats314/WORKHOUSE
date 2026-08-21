---
file: Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_C__Configuration_Geometry.md
feeds_into:
  - Core-4 (Vacuum linearization and the discrete Maxwell structure)
  - Core-5 (Local coercivity / matrix hinge: identification of the Maxwell term)
---

# Appendix D — Wilson action: vacuum expansion and Hessian identity

## D.0 Interface and standing conventions

**Definition D.0.1 (scope).**
This appendix isolates the vacuum identities for the Wilson action (Definition A.6.3) that are used in Core-4:
1. the differential of the plaquette holonomy map at the vacuum equals the discrete coboundary `d_1` (Definition A.5.4);
2. the Riemannian Hessian of the Wilson action at the vacuum equals the discrete Maxwell operator `\mathsf M_1=d_1^*d_1` (Definition A.5.6) multiplied by the coefficient `\alpha_W` (Definition A.9.1).

**Definition D.0.2 (standing setting).**
Fix a finite periodic lattice `\Lambda_L` (Definition A.1.3) and the configuration manifold `M_{\Lambda_L}=G^{E(\Lambda_L)}` with product metric `g_{\Lambda_L}` (Definitions A.4.1–A.4.2). The Wilson action is
\[
S_{\Lambda_L,\beta}(U)=\sum_{p\in P(\Lambda_L)}\Phi_\beta\big(U_p(U)\big)
\quad\text{(Definitions A.6.1–A.6.3)}.
\]
The vacuum configuration is `U^{(0)}` (Definition A.6.4).

**Definition D.0.3 (no new constants).**
This appendix introduces no named constants.
All named constants and parameters are those of Appendix A, in particular `n` (Assumption A.3.3), `\beta` (Definition A.6.2), and `\alpha_W=\beta/n` (Definition A.9.1).

---

## D.1 A canonical geodesic chart at the vacuum

The Riemannian Hessian at `U^{(0)}` is most efficiently computed by restricting to geodesics through `U^{(0)}`.

**Definition D.1.1 (linkwise exponential curve through the vacuum).**
Let `X\in \mathcal C^1(\Lambda_L;\mathfrak g)` (Definition A.5.1). Define the curve `\gamma_X: \mathbb R\to M_{\Lambda_L}` by
\[
(\gamma_X(t))_b := \exp(tX_b),\qquad b\in E(\Lambda_L),\ t\in\mathbb R.
\]
Then `\gamma_X(0)=U^{(0)}`.

**Lemma D.1.2 (\(\gamma_X\) is a geodesic and its initial velocity equals \(X\)).**
The curve `\gamma_X` of Definition D.1.1 is a geodesic in `(M_{\Lambda_L},g_{\Lambda_L})`. Its initial velocity satisfies
\[
\omega_{U^{(0)}}^R(\dot\gamma_X(0))=X\in \mathcal C^1(\Lambda_L;\mathfrak g)
\quad\text{(right-trivialization; Definition A.4.3).}
\]

*Proof.*
On `(G,g_G)` with bi-invariant metric (Definitions A.3.5–A.3.6), every one-parameter subgroup `t\mapsto \exp(tY)` is a geodesic with velocity `Y` at `t=0`.
The configuration manifold is a finite product of such factors with the product metric (Definition A.4.2), hence the product curve `\gamma_X` is a geodesic.
At `t=0`, each component curve has velocity `X_b\in \mathfrak g` in right-trivialized coordinates at the identity, and right-trivialization on the product is componentwise (Definition A.4.3).
Therefore `\omega_{U^{(0)}}^R(\dot\gamma_X(0))=X`. ∎

---

## D.2 Differential of plaquette holonomy at the vacuum

For each plaquette `p`, the plaquette holonomy map `U\mapsto U_p(U)` is a smooth map from `M_{\Lambda_L}` to `G` (Definition A.6.1). We compute its differential at `U^{(0)}` in right-trivialized coordinates.

**Lemma D.2.1 (derivative of inversion at the identity).**
Let `g:(-\varepsilon,\varepsilon)\to G` be a `C^1` curve with `g(0)=\mathbf 1`. Write `\dot g(0)\in T_{\mathbf 1}G\cong \mathfrak g` (via right-trivialization at `\mathbf 1`). Then
\[
\left.\frac{d}{dt}\right|_{t=0} g(t)^{-1} = -\dot g(0)\in \mathfrak g.
\]

*Proof.*
Differentiate the identity `g(t)g(t)^{-1}=\mathbf 1` at `t=0`:
\[
\dot g(0)\cdot \mathbf 1 + \mathbf 1\cdot \left.\frac{d}{dt}\right|_{t=0}g(t)^{-1} = 0
\quad\text{in }T_{\mathbf 1}G\cong\mathfrak g.
\]
Thus the derivative of the inverse curve at `0` equals `-\dot g(0)`. ∎

**Proposition D.2.2 (plaquette holonomy linearization equals \(d_1\)).**
Fix a plaquette `p=(x;\mu,\nu)\in P(\Lambda_L)` with `\mu<\nu` (Definition A.2.3). Consider the holonomy map
\[
\mathrm{Hol}_p: M_{\Lambda_L}\to G,\qquad \mathrm{Hol}_p(U):=U_p(U)
\quad\text{(Definition A.6.1).}
\]
For `X\in \mathcal C^1(\Lambda_L;\mathfrak g)` and the vacuum geodesic `\gamma_X` (Definition D.1.1), the derivative at the vacuum satisfies
\[
\left.\frac{d}{dt}\right|_{t=0} \mathrm{Hol}_p(\gamma_X(t))
\;=\;
(d_1X)_p
\in \mathfrak g\cong T_{\mathbf 1}G.
\]
Equivalently, the differential `(d\,\mathrm{Hol}_p)_{U^{(0)}}:T_{U^{(0)}}M_{\Lambda_L}\to T_{\mathbf 1}G` identifies with the linear map
\[
\mathcal C^1(\Lambda_L;\mathfrak g)\to \mathfrak g,
\qquad X\mapsto (d_1X)_p.
\]

*Proof.*
By Definition A.6.1, with `p=(x;\mu,\nu)`,
\[
\mathrm{Hol}_p(U)=U_{x,\mu}\,U_{x+\hat e_\mu,\nu}\,U_{x+\hat e_\nu,\mu}^{-1}\,U_{x,\nu}^{-1}.
\]
For the curve `U(t)=\gamma_X(t)`, each factor equals `\exp(tX_b)` and satisfies `U_b(0)=\mathbf 1`.
Differentiate the product at `t=0`. Since all factors are the identity at `0`, the derivative is the sum of the derivatives of the factors, with a minus sign for inverted factors (Lemma D.2.1):
\[
\left.\frac{d}{dt}\right|_{t=0} \mathrm{Hol}_p(U(t))
=
X_{x,\mu}+X_{x+\hat e_\mu,\nu}-X_{x+\hat e_\nu,\mu}-X_{x,\nu}.
\]
By the coordinate definition of `d_1` (Definition A.5.4 together with the explicit boundary in Definition A.2.4), the right-hand side is exactly `(d_1X)_p`. ∎

---

## D.3 Second derivative of the single-plaquette potential at the identity

The Wilson action is a sum of identical single-plaquette potentials composed with the plaquette holonomies. The key local input is the Hessian of `\Phi_\beta` at the identity.

**Proposition D.3.1 (Riemannian Hessian of \(\Phi_\beta\) at \(\mathbf 1\)).**
Let `\Phi_\beta:G\to\mathbb R` be the single-plaquette potential (Definition A.6.2). Then:

1. The gradient of `\Phi_\beta` vanishes at the identity:
   \[
   \nabla \Phi_\beta(\mathbf 1)=0.
   \]

2. For every `Y\in T_{\mathbf 1}G\cong \mathfrak g` (via right-trivialization), the Riemannian Hessian satisfies
   \[
   \nabla^2\Phi_\beta(\mathbf 1)[Y,Y]
   
   =
   \alpha_W\,|Y|_{\mathfrak g}^2,
   \qquad \alpha_W=\beta/n\ \text{(Definition A.9.1)}.
   \]
Equivalently, as a bilinear form on `\mathfrak g`,
\[
\nabla^2\Phi_\beta(\mathbf 1)[Y,Z]=\alpha_W\,\langle Y,Z\rangle_{\mathfrak g}.
\]

*Proof.*
Fix `Y\in\mathfrak g` and consider the geodesic `\eta_Y(t):=\exp(tY)` in `(G,g_G)`.
By the defining property of the Riemannian Hessian along geodesics,
\[
\nabla^2\Phi_\beta(\mathbf 1)[Y,Y]
= \left.\frac{d^2}{dt^2}\right|_{t=0} \Phi_\beta(\eta_Y(t)).
\]

Write `A:=d\rho(Y)\in\mathfrak u(n)` (Assumption A.3.3) so that `\rho(\exp(tY))=\exp(tA)`.
Using the Taylor expansion of the matrix exponential,
\[
\exp(tA)=I+tA+\frac{t^2}{2}A^2+O(t^3),
\qquad t\to 0.
\]
Taking traces and real parts,
\[
\Re\mathrm{Tr}(\exp(tA))
=
\Re\mathrm{Tr}(I)+t\Re\mathrm{Tr}(A)+\frac{t^2}{2}\Re\mathrm{Tr}(A^2)+O(t^3).
\]
Since `A` is anti-Hermitian, `\mathrm{Tr}(A)` is purely imaginary, hence `\Re\mathrm{Tr}(A)=0`.
Therefore
\[
\Re\mathrm{Tr}(\exp(tA))
=
 n + \frac{t^2}{2}\Re\mathrm{Tr}(A^2)+O(t^3).
\]
Insert into the definition `\Phi_\beta(V)=\beta(1-\frac{1}{n}\Re\mathrm{Tr}(V))`:
\[
\Phi_\beta(\exp(tY))
=
\beta\Bigl(1-\frac{1}{n}\bigl(n+\frac{t^2}{2}\Re\mathrm{Tr}(A^2)+O(t^3)\bigr)\Bigr)
=
-\frac{\beta}{2n}\Re\mathrm{Tr}(A^2)\,t^2+O(t^3).
\]
By Definition A.3.4–A.3.5,
\[
|Y|_{\mathfrak g}^2
=\langle Y,Y\rangle_{\mathfrak g}
=-\Re\mathrm{Tr}(A^2),
\]
hence
\[
\Phi_\beta(\exp(tY))
=
\frac{\beta}{2n}|Y|_{\mathfrak g}^2\,t^2+O(t^3).
\]
Thus `\frac{d}{dt}\Phi_\beta(\exp(tY))|_{t=0}=0`, proving `\nabla\Phi_\beta(\mathbf 1)=0`, and
\[
\left.\frac{d^2}{dt^2}\right|_{t=0}\Phi_\beta(\exp(tY))
=
\frac{\beta}{n}|Y|_{\mathfrak g}^2
=\alpha_W|Y|_{\mathfrak g}^2.
\]
The bilinear form statement follows by polarization:
`\nabla^2\Phi_\beta(\mathbf 1)[Y,Z]=\frac14\sum_{\pm}\big(\nabla^2\Phi_\beta(\mathbf 1)[Y\pm Z,Y\pm Z]-\nabla^2\Phi_\beta(\mathbf 1)[Y,Y]-\nabla^2\Phi_\beta(\mathbf 1)[Z,Z]\big)`, which yields `\alpha_W\langle Y,Z\rangle_{\mathfrak g}`. ∎

---

## D.4 Vacuum Hessian of the Wilson action

We now combine the two previous sections by a chain-rule computation along vacuum geodesics.

**Lemma D.4.1 (the vacuum is a critical point of the Wilson action).**
\[
\nabla S_{\Lambda_L,\beta}(U^{(0)}) = 0.
\]

*Proof.*
For each plaquette `p`, the map `U\mapsto U_p(U)` satisfies `U_p(U^{(0)})=\mathbf 1` (Definition A.6.4 and Definition A.6.1). By Proposition D.3.1(1), `\nabla \Phi_\beta(\mathbf 1)=0`.
By the chain rule for gradients on Riemannian manifolds, each summand `U\mapsto \Phi_\beta(U_p(U))` has vanishing gradient at `U^{(0)}`, and hence their finite sum `S_{\Lambda_L,\beta}` also has vanishing gradient at `U^{(0)}`. ∎

**Proposition D.4.2 (Hessian quadratic form equals \(\alpha_W\|d_1X\|^2\)).**
Let `X\in \mathcal C^1(\Lambda_L;\mathfrak g)\cong T_{U^{(0)}}M_{\Lambda_L}` (right-trivialization at the vacuum; Definition A.4.3). Then
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,X]
=
\alpha_W\,\big|d_1X\big|_{\mathcal C^2}^2,
\qquad \alpha_W=\beta/n\ \text{(Definition A.9.1)}.
\]

*Proof.*
Let `\gamma_X` be the vacuum geodesic with initial velocity `X` (Definition D.1.1 and Lemma D.1.2). Since `\gamma_X` is a geodesic and the gradient vanishes at `U^{(0)}` (Lemma D.4.1),
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,X]
=\left.\frac{d^2}{dt^2}\right|_{t=0} S_{\Lambda_L,\beta}(\gamma_X(t)).
\]
Expand the action as a sum over plaquettes:
\[
S_{\Lambda_L,\beta}(\gamma_X(t))=\sum_{p\in P(\Lambda_L)} \Phi_\beta\big(U_p(\gamma_X(t))\big).
\]
Differentiate twice at `t=0`. For each fixed `p`, set
\[
Y_p := \left.\frac{d}{dt}\right|_{t=0} U_p(\gamma_X(t))\in T_{\mathbf 1}G\cong\mathfrak g.
\]
By Proposition D.2.2, `Y_p=(d_1X)_p`. By Proposition D.3.1(1), the first derivative of `\Phi_\beta` at `\mathbf 1` vanishes, hence the chain rule gives
\[
\left.\frac{d^2}{dt^2}\right|_{t=0}\Phi_\beta\big(U_p(\gamma_X(t))\big)
=
\nabla^2\Phi_\beta(\mathbf 1)[Y_p,Y_p].
\]
Now apply Proposition D.3.1(2): `\nabla^2\Phi_\beta(\mathbf 1)[Y_p,Y_p]=\alpha_W|Y_p|_{\mathfrak g}^2`.
Summing over `p` yields
\[
\left.\frac{d^2}{dt^2}\right|_{t=0} S_{\Lambda_L,\beta}(\gamma_X(t))
=
\alpha_W\sum_{p\in P(\Lambda_L)} |(d_1X)_p|_{\mathfrak g}^2
=
\alpha_W\,|d_1X|_{\mathcal C^2}^2.
\]
This is the claimed identity. ∎

**Proposition D.4.3 (operator identity: \(\nabla^2 S(U^{(0)})=\alpha_W d_1^*d_1\)).**
Under the identification `T_{U^{(0)}}M_{\Lambda_L}\cong \mathcal C^1(\Lambda_L;\mathfrak g)` (Definition A.4.3), the Riemannian Hessian of the Wilson action at the vacuum satisfies
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})
=
\alpha_W\, d_1^*d_1
\quad\text{as self-adjoint operators on }\mathcal C^1(\Lambda_L;\mathfrak g).
\]
Equivalently, for all `X,Z\in\mathcal C^1(\Lambda_L;\mathfrak g)`,
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,Z]
=
\alpha_W\,\langle d_1X,d_1Z\rangle_{\mathcal C^2}
=
\alpha_W\,\langle X,d_1^*d_1Z\rangle_{\mathcal C^1}.
\]

*Proof.*
By Proposition D.4.2 applied to `X`, to `Z`, and to `X+Z`, polarization yields
\[
\nabla^2 S_{\Lambda_L,\beta}(U^{(0)})[X,Z]
=
\alpha_W\,\langle d_1X,d_1Z\rangle_{\mathcal C^2}.
\]
By the definition of the adjoint `d_1^*` (Definition A.5.5), `\langle d_1X,d_1Z\rangle_{\mathcal C^2}=\langle X,d_1^*d_1Z\rangle_{\mathcal C^1}`.
Since the above identity holds for all `X,Z`, the Hessian operator equals `\alpha_W d_1^*d_1`. ∎

