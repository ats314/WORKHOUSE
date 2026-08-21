---
file: Appendix_E__Bakry_Emery_Calculus.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_C__Configuration_Geometry.md
feeds_into:
  - Core-5 (Local coercivity / matrix hinge: curvature matrix formalism)
  - Appendix_F__Matrix_Hinge_on_the_Canonical_Good_Set.md
  - Appendix_G__Helffer_Sjostrand_Representation_Interface.md
---

# Appendix E — Bakry–Émery calculus (Γ, Γ₂, and the curvature matrix)

## E.0 Interface and standing conventions

**Definition E.0.1 (scope).**  
This appendix isolates the Riemannian/weighted-calculus identities for the reversible generator
\[
\mathcal L_S := \Delta - \langle\nabla S,\nabla(\cdot)\rangle
\quad\text{(Definition A.4.8)}
\]
that are used as the analytic interface between:
- pointwise lower bounds on the **Bakry–Émery curvature matrix** `\mathrm{Ric}_\mu`;
- coercivity and comparison inequalities for the `1`-form/gradient-level generator `\mathcal L_S^{(1)}`.

The principal outputs are:
1. the divergence-form identity for `\mathcal L_S` and its `L^2(\mu_S)` symmetry;
2. the Bochner–Bakry–Émery identity
   \[
   \Gamma_2(f)=|\nabla^2 f|_{\mathrm{HS}}^2+\mathrm{Ric}_{\mu_S}(\nabla f,\nabla f);
   \]
3. the Weitzenböck identity defining the `1`-form generator
   \[
   \mathcal L_S^{(1)}=\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}+\mathrm{Ric}_{\mu_S}^{\sharp}
   \quad\text{and the commutation}\quad
   \nabla(\mathcal L_S f)=\mathcal L_S^{(1)}(\nabla f).
   \]

**Definition E.0.2 (standing setting).**  
Throughout, `\Lambda_L` is a finite periodic lattice (Definition A.1.3) and
\[
(M,g):=(M_{\Lambda_L},g_{\Lambda_L})
\]
is the configuration manifold with product metric (Definitions A.4.1–A.4.2).  
The results below are formulated intrinsically for an arbitrary smooth compact Riemannian manifold without boundary; they are applied later with `M=M_{\Lambda_L}`.

**Definition E.0.3 (no new constants).**  
This appendix introduces no named constants. All named constants are defined in Appendix A.

**Definition E.0.4 (notation simplification).**  
Within this appendix only, we write:
\[
\Delta:=\Delta_{\Lambda_L},\qquad
\Gamma:=\Gamma_{\Lambda_L},
\]
with `\Delta` and `\Gamma` as in Definitions A.4.6–A.4.7. The gradient and Hessian of a smooth function `f` are `\nabla f` and `\nabla^2 f` as in Definition A.4.5.

---

## E.1 Weighted measure, generator, and integration by parts

### E.1.1 The Gibbs/weighted reference measure

**Definition E.1.1 (weighted measure associated to a potential).**  
Let `S\in C^\infty(M)` be a smooth function. Define the probability measure
\[
d\mu_S := Z_S^{-1}\,e^{-S}\,d\mathrm{vol}_g,
\qquad
Z_S := \int_M e^{-S}\,d\mathrm{vol}_g,
\]
where `d\mathrm{vol}_g` is the Riemannian volume form of `g`.

**Definition E.1.2 (reversible diffusion generator; reference).**  
Fix `S\in C^\infty(M)`. Let `\mathcal L_S` denote the diffusion generator associated to `S` as in **Definition A.4.8** (applied to `(M,g)`).


### E.1.2 Divergence form and symmetry

To use `\mathcal L_S` as an `L^2(\mu_S)`-symmetric operator, we record its divergence form.

**Definition E.1.3 (Riemannian divergence).**  
For a smooth vector field `X` on `M`, the divergence `\mathrm{div}X` is the unique smooth function satisfying, for all `\varphi\in C^\infty(M)`,
\[
\int_M \varphi\,\mathrm{div}X\,d\mathrm{vol}_g
=
-\int_M \langle \nabla \varphi, X\rangle_g\,d\mathrm{vol}_g.
\]
(On a compact manifold without boundary this characterization is equivalent to the local-coordinate definition.)

**Lemma E.1.4 (weighted divergence form).**  
For every `f\in C^\infty(M)`,
\[
\mathcal L_S f
=
e^{S}\,\mathrm{div}\!\big(e^{-S}\nabla f\big).
\]

*Proof.* Using the product rule for divergence in the form
\[
\mathrm{div}(hX)=\langle \nabla h,X\rangle_g+h\,\mathrm{div}X
\quad\text{for }h\in C^\infty(M),
\]
with `h=e^{-S}` and `X=\nabla f`, and the identity `\mathrm{div}(\nabla f)=\Delta f`, we get
\[
\mathrm{div}(e^{-S}\nabla f)
=
\langle \nabla(e^{-S}),\nabla f\rangle_g+e^{-S}\Delta f
=
-e^{-S}\langle \nabla S,\nabla f\rangle_g+e^{-S}\Delta f.
\]
Multiplying by `e^S` yields the claim. ∎

**Proposition E.1.5 (integration by parts; symmetry in `L^2(\mu_S)`).**  
For all `f,g\in C^\infty(M)`,
\[
\int_M f\,(\mathcal L_S g)\,d\mu_S
=
-\int_M \langle \nabla f,\nabla g\rangle_g\,d\mu_S.
\]
In particular:
1. `\int_M \mathcal L_S g\,d\mu_S=0` for all `g`;
2. `\mathcal L_S` is symmetric on `C^\infty(M)\subset L^2(\mu_S)`:
   \[
   \int f\,\mathcal L_S g\,d\mu_S=\int g\,\mathcal L_S f\,d\mu_S.
   \]

*Proof.* Write `d\mu_S=Z_S^{-1}e^{-S}d\mathrm{vol}_g` and ignore `Z_S^{-1}` (it cancels). By Lemma E.1.4,
\[
\int_M f\,(\mathcal L_S g)\,d\mu_S
=
\int_M f\,e^{S}\,\mathrm{div}(e^{-S}\nabla g)\,Z_S^{-1}e^{-S}\,d\mathrm{vol}_g
=
Z_S^{-1}\int_M f\,\mathrm{div}(e^{-S}\nabla g)\,d\mathrm{vol}_g.
\]
Using the defining property of `\mathrm{div}` (Definition E.1.3) with `\varphi=f` and `X=e^{-S}\nabla g`,
\[
\int_M f\,\mathrm{div}(e^{-S}\nabla g)\,d\mathrm{vol}_g
=
-\int_M \langle\nabla f, e^{-S}\nabla g\rangle_g\,d\mathrm{vol}_g
=
-\int_M \langle\nabla f,\nabla g\rangle_g\,e^{-S}\,d\mathrm{vol}_g,
\]
which is the desired identity after reinstating `Z_S^{-1}`. Taking `f\equiv 1` gives item (1), and symmetry follows because the right-hand side is symmetric in `(f,g)`. ∎

---

## E.2 Carré du champ and iterated carré du champ

### E.2.1 Definitions

**Definition E.2.1 (carré du champ; reference).**  
The carré du champ `\Gamma` is the bilinear form from **Definition A.4.7** (with the simplification of Definition E.0.4):
\[
\Gamma(f,g):=\langle\nabla f,\nabla g\rangle_g,
\qquad
\Gamma(f):=\Gamma(f,f)=|\nabla f|_g^2.
\]


**Definition E.2.2 (iterated carré du champ).**  
For `f,g\in C^\infty(M)`, define
\[
\Gamma_2(f,g)
:=
\frac12\Big(\mathcal L_S\Gamma(f,g)-\Gamma(f,\mathcal L_S g)-\Gamma(g,\mathcal L_S f)\Big),
\qquad
\Gamma_2(f):=\Gamma_2(f,f).
\]

### E.2.2 Explicit expression for Γ

**Lemma E.2.3 (generator identity for `\Gamma`).**  
Let `\Gamma` be as in Definition E.2.1 and let `\mathcal L_S` be as in Definition E.1.2. Then for all `f,g\in C^\infty(M)`,
\[
\Gamma(f,g)
=
\frac12\Big(\mathcal L_S(fg)-f\,\mathcal L_S g-g\,\mathcal L_S f\Big).
\]

*Proof.* By Definition A.4.8, `\mathcal L_S=\Delta-\langle\nabla S,\nabla(\cdot)\rangle_g`. Using the product rule for the Laplace–Beltrami operator,
\[
\Delta(fg)=f\,\Delta g+g\,\Delta f+2\langle\nabla f,\nabla g\rangle_g,
\]
and the Leibniz rule for the drift term,
\[
\langle\nabla S,\nabla(fg)\rangle_g
=
f\,\langle\nabla S,\nabla g\rangle_g+g\,\langle\nabla S,\nabla f\rangle_g,
\]
one finds that
\[
\mathcal L_S(fg)-f\,\mathcal L_S g-g\,\mathcal L_S f
=
2\langle\nabla f,\nabla g\rangle_g.
\]
Dividing by `2` gives the claimed identity, and the right-hand side equals `\Gamma(f,g)` by Definition E.2.1. ∎


### E.2.3 An integrated identity for Γ₂

**Lemma E.2.4 (integral identity for Γ₂).**  
For every `f\in C^\infty(M)`,
\[
\int_M \Gamma_2(f)\,d\mu_S
=
\int_M (\mathcal L_S f)^2\,d\mu_S.
\]

*Proof.* By Definition E.2.2 with `f=g`,
\[
\Gamma_2(f)=\frac12\Big(\mathcal L_S\Gamma(f)-2\Gamma(f,\mathcal L_S f)\Big).
\]
Integrating and using Proposition E.1.5 with `f\equiv 1` gives `\int \mathcal L_S\Gamma(f)\,d\mu_S=0`, hence
\[
\int_M \Gamma_2(f)\,d\mu_S
=
-\int_M \Gamma(f,\mathcal L_S f)\,d\mu_S.
\]
By Definition E.2.1 and Proposition E.1.5 (with `f` replaced by `\mathcal L_S f` and `g` replaced by `f`),
\[
-\int_M \Gamma(f,\mathcal L_S f)\,d\mu_S
=
-\int_M \langle\nabla f,\nabla(\mathcal L_S f)\rangle_g\,d\mu_S
=
\int_M (\mathcal L_S f)(\mathcal L_S f)\,d\mu_S
=
\int_M (\mathcal L_S f)^2\,d\mu_S,
\]
as claimed. ∎

---

## E.3 Bochner–Bakry–Émery identity and the curvature matrix

The key pointwise identity is the Bochner formula adapted to the drifted generator `\mathcal L_S`.

### E.3.1 Levi–Civita connection, Hessian, and Ricci

**Definition E.3.1 (Levi–Civita connection).**  
Let `\nabla^{\mathrm{LC}}` denote the Levi–Civita connection of `(M,g)`, i.e. the unique torsion-free, metric-compatible connection on `TM`.

**Definition E.3.2 (Hessian of a function).**  
For `f\in C^\infty(M)`, define its Riemannian Hessian `\nabla^2 f` as the symmetric `(0,2)`-tensor
\[
(\nabla^2 f)(X,Y)
:=
\big\langle \nabla^{\mathrm{LC}}_X(\nabla f),\,Y\big\rangle_g,
\qquad X,Y\ \text{vector fields}.
\]
Its Hilbert–Schmidt norm is
\[
|\nabla^2 f|_{\mathrm{HS}}^2
:=
\sum_{i,j} \big(\nabla^2 f(e_i,e_j)\big)^2
\quad\text{for any local }g\text{-orthonormal frame }(e_i).
\]

**Definition E.3.3 (Ricci tensor and Ricci endomorphism).**  
Let `\mathrm{Ric}_g` denote the Ricci curvature tensor of `(M,g)`, viewed as a symmetric bilinear form on each tangent space.
Define the associated self-adjoint endomorphism `\mathrm{Ric}_g^{\sharp}:TM\to TM` by raising an index with the metric:
\[
\langle \mathrm{Ric}_g^{\sharp}X,Y\rangle_g=\mathrm{Ric}_g(X,Y)
\quad\text{for all tangent vectors }X,Y.
\]

### E.3.2 Bakry–Émery tensor

**Definition E.3.4 (Bakry–Émery curvature tensor / curvature matrix).**  
Define the Bakry–Émery tensor associated to the weighted measure `\mu_S` by
\[
\mathrm{Ric}_{\mu_S}
:=
\mathrm{Ric}_g+\nabla^2 S,
\]
a symmetric bilinear form on each tangent space.  
Its raised-index form is the self-adjoint endomorphism
\[
\mathrm{Ric}_{\mu_S}^{\sharp}
:=
\mathrm{Ric}_g^{\sharp}+(\nabla^2 S)^{\sharp}.
\]
(Here `(\nabla^2 S)^{\sharp}` is defined by the metric in the same way as in Definition E.3.3.)

The terminology “curvature matrix” refers to the fact that in any orthonormal trivialization of `TM` (in particular, in the right-trivialized identification used in Appendix C), the bilinear form `\mathrm{Ric}_{\mu_S}(U)` becomes a symmetric matrix/operator acting on the coordinate representation of tangent vectors.

### E.3.3 Bochner identity with drift

**Proposition E.3.5 (Bochner–Bakry–Émery identity).**  
For every `f\in C^\infty(M)`,
\[
\Gamma_2(f)
=
|\nabla^2 f|_{\mathrm{HS}}^2
+
\mathrm{Ric}_{\mu_S}(\nabla f,\nabla f).
\]

*Proof.* By Definition E.2.2 and Definition E.2.1,
\[
\Gamma_2(f)
=
\frac12\Big(\mathcal L_S|\nabla f|_g^2-2\langle\nabla f,\nabla(\mathcal L_S f)\rangle_g\Big).
\tag{E.1}
\]
Expand `\mathcal L_S = \Delta-\langle\nabla S,\nabla\cdot\rangle_g`:
\[
\mathcal L_S|\nabla f|_g^2
=
\Delta|\nabla f|_g^2-\langle\nabla S,\nabla|\nabla f|_g^2\rangle_g,
\]
and
\[
\nabla(\mathcal L_S f)
=
\nabla(\Delta f)-\nabla\langle\nabla S,\nabla f\rangle_g.
\]
Substituting into (E.1) yields
\[
\Gamma_2(f)
=
\underbrace{\frac12\Delta|\nabla f|_g^2-\langle\nabla f,\nabla(\Delta f)\rangle_g}_{(\star)}
\;-\;
\frac12\langle\nabla S,\nabla|\nabla f|_g^2\rangle_g
\;+\;
\langle\nabla f,\nabla\langle\nabla S,\nabla f\rangle_g\rangle_g.
\tag{E.2}
\]

**Step 1 (classical Bochner identity for `\Delta`).**  
On any Riemannian manifold,
\[
\frac12\Delta|\nabla f|_g^2
=
\langle\nabla f,\nabla(\Delta f)\rangle_g
+
|\nabla^2 f|_{\mathrm{HS}}^2
+
\mathrm{Ric}_g(\nabla f,\nabla f).
\tag{E.3}
\]
A proof is included below (Lemma E.3.6). Subtracting `\langle\nabla f,\nabla(\Delta f)\rangle_g` from both sides shows
\[
(\star)=|\nabla^2 f|_{\mathrm{HS}}^2+\mathrm{Ric}_g(\nabla f,\nabla f).
\tag{E.4}
\]

**Step 2 (drift correction).**  
It remains to simplify the last two terms of (E.2). First, by Definition E.3.2 and metric-compatibility,
\[
\nabla|\nabla f|_g^2
=
2\,\nabla^2 f(\cdot,\nabla f),
\]
hence
\[
\langle\nabla S,\nabla|\nabla f|_g^2\rangle_g
=
2\,(\nabla^2 f)(\nabla S,\nabla f).
\tag{E.5}
\]
Second, for any vector field `X`,
\[
X\big(\langle\nabla S,\nabla f\rangle_g\big)
=
\langle \nabla_X^{\mathrm{LC}}\nabla S,\nabla f\rangle_g
+
\langle \nabla S,\nabla_X^{\mathrm{LC}}\nabla f\rangle_g
=
(\nabla^2 S)(X,\nabla f)+(\nabla^2 f)(X,\nabla S),
\]
so
\[
\nabla\langle\nabla S,\nabla f\rangle_g
=
(\nabla^2 S)^{\sharp}(\nabla f)+(\nabla^2 f)^{\sharp}(\nabla S),
\]
and pairing with `\nabla f` gives
\[
\langle\nabla f,\nabla\langle\nabla S,\nabla f\rangle_g\rangle_g
=
(\nabla^2 S)(\nabla f,\nabla f)+(\nabla^2 f)(\nabla f,\nabla S).
\tag{E.6}
\]
Combining (E.5)–(E.6), the drift correction in (E.2) becomes
\[
-\tfrac12\langle\nabla S,\nabla|\nabla f|_g^2\rangle_g
+\langle\nabla f,\nabla\langle\nabla S,\nabla f\rangle_g\rangle_g
=
-(\nabla^2 f)(\nabla S,\nabla f)+(\nabla^2 S)(\nabla f,\nabla f)+(\nabla^2 f)(\nabla f,\nabla S)
=
(\nabla^2 S)(\nabla f,\nabla f).
\tag{E.7}
\]

**Step 3 (assemble).**  
Insert (E.4) and (E.7) into (E.2):
\[
\Gamma_2(f)
=
|\nabla^2 f|_{\mathrm{HS}}^2+\mathrm{Ric}_g(\nabla f,\nabla f)+(\nabla^2 S)(\nabla f,\nabla f)
=
|\nabla^2 f|_{\mathrm{HS}}^2+\mathrm{Ric}_{\mu_S}(\nabla f,\nabla f),
\]
which is the claim. ∎

**Lemma E.3.6 (classical Bochner identity for `\Delta`).**  
For any `f\in C^\infty(M)`, the identity (E.3) holds.

*Proof.* Fix a point `p\in M` and choose a local orthonormal frame `(e_1,\dots,e_m)` defined near `p` such that
\[
\nabla^{\mathrm{LC}}_{e_i}e_j(p)=0\quad\text{for all }i,j
\]
(normal frame at `p`). Write `f_i:=e_i f` and `f_{ij}:=(\nabla^2 f)(e_i,e_j)=e_i(e_j f)-(\nabla^{\mathrm{LC}}_{e_i}e_j)f`. At `p` we have `f_{ij}(p)=e_i(e_j f)(p)` by the normal-frame property.

Compute at `p`:
\[
|\nabla f|_g^2=\sum_i f_i^2.
\]
Thus
\[
\frac12\Delta|\nabla f|_g^2
=
\frac12\sum_k e_k\big(e_k(\sum_i f_i^2)\big)
=
\sum_{i,k} (e_k f_i)^2 + \sum_{i,k} f_i\,e_k e_k f_i,
\tag{E.8}
\]
using `e_k(f_i^2)=2f_i(e_k f_i)`.

The first term in (E.8) is `\sum_{i,k} f_{ik}^2 = |\nabla^2 f|_{\mathrm{HS}}^2` at `p` because `e_k f_i = e_k(e_i f)=f_{ik}` in the normal frame.

For the second term, note that
\[
\sum_{k} e_k e_k f_i = \Delta(f_i) \quad\text{at }p,
\]
again because the connection terms vanish at `p`. Therefore
\[
\sum_{i,k} f_i\,e_k e_k f_i
=
\sum_i f_i\,\Delta(f_i)
=
\langle \nabla f, \nabla(\Delta f)\rangle_g + \mathrm{Ric}_g(\nabla f,\nabla f),
\tag{E.9}
\]
where the last equality is the standard commutation formula `\Delta(\nabla f)=\nabla(\Delta f)+\mathrm{Ric}_g^{\sharp}(\nabla f)` evaluated at `p`. A direct proof of (E.9) from curvature conventions is included in Lemma E.4.5 below; inserting it into (E.8) yields (E.3). Since `p` was arbitrary, the identity holds on all of `M`. ∎

---

## E.4 The 1-form/gradient-level generator and the Weitzenböck identity

For covariance representations of Helffer–Sjöstrand type, one needs the generator acting on gradients (equivalently, on `1`-forms). The geometric input is that it is a rough Laplacian plus the Bakry–Émery curvature matrix.

### E.4.1 Rough Laplacian on vector fields

**Definition E.4.1 (covariant derivative of a vector field).**  
For a smooth vector field `V`, define its covariant derivative `\nabla^{\mathrm{LC}}V` as the `(1,1)`-tensor
\[
(\nabla^{\mathrm{LC}}V)(X):=\nabla^{\mathrm{LC}}_X V.
\]
Its pointwise Hilbert–Schmidt norm is
\[
|\nabla^{\mathrm{LC}}V|_{\mathrm{HS}}^2 := \sum_i \big|\nabla^{\mathrm{LC}}_{e_i}V\big|_g^2
\quad\text{for a local orthonormal frame }(e_i).
\]

**Definition E.4.2 (rough Laplacian).**  
Define the rough Laplacian on vector fields by
\[
\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}} V
:=
-\sum_i \Big(\nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_i}V-\nabla^{\mathrm{LC}}_{\nabla^{\mathrm{LC}}_{e_i}e_i}V\Big),
\]
which is independent of the chosen orthonormal frame. It is the `L^2(d\mathrm{vol}_g)`-adjoint of `\nabla^{\mathrm{LC}}` composed with itself.

### E.4.2 The Witten Laplacian on vector fields

**Definition E.4.3 (1-form generator / Witten Laplacian on vector fields).**  
Define the operator `\mathcal L_S^{(1)}` acting on smooth vector fields by
\[
\mathcal L_S^{(1)}V
:=
\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V
-\nabla^{\mathrm{LC}}_{\nabla S}V
+\mathrm{Ric}_{\mu_S}^{\sharp}V.
\tag{E.10}
\]
Equivalently, in terms of `\mathrm{Ric}_{\mu_S}^{\sharp}=\mathrm{Ric}_g^{\sharp}+(\nabla^2 S)^{\sharp}`,
\[
\mathcal L_S^{(1)}V
=
\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V
-\nabla^{\mathrm{LC}}_{\nabla S}V
+\mathrm{Ric}_g^{\sharp}V+(\nabla^2 S)^{\sharp}V.
\]

The term `-\nabla^{\mathrm{LC}}_{\nabla S}V` is the natural drift on vector fields induced by the scalar drift `-\langle\nabla S,\nabla\cdot\rangle_g` in `\mathcal L_S`.

### E.4.3 Commutation with the gradient

**Proposition E.4.4 (Weitzenböck/commutation identity).**  
For every `f\in C^\infty(M)`,
\[
\nabla(\mathcal L_S f)=\mathcal L_S^{(1)}(\nabla f).
\tag{E.11}
\]

*Proof.* Since `\mathcal L_S=\Delta-\langle\nabla S,\nabla\cdot\rangle_g`, it is enough to establish the commutator identities
\[
\nabla(\Delta f)=\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}(\nabla f)+\mathrm{Ric}_g^{\sharp}(\nabla f),
\tag{E.12}
\]
and
\[
\nabla\big(\langle\nabla S,\nabla f\rangle_g\big)
=
\nabla^{\mathrm{LC}}_{\nabla S}(\nabla f)+(\nabla^2 S)^{\sharp}(\nabla f),
\tag{E.13}
\]
then subtract.

Identity (E.13) was already used in the drift simplification in Proposition E.3.5: for any vector field `X`,
\[
\langle \nabla\langle\nabla S,\nabla f\rangle_g, X\rangle_g
=
X\langle\nabla S,\nabla f\rangle_g
=
(\nabla^2 S)(X,\nabla f)+(\nabla^2 f)(X,\nabla S).
\]
The right-hand side equals
\[
\langle (\nabla^2 S)^{\sharp}(\nabla f),X\rangle_g
+
\langle \nabla^{\mathrm{LC}}_{\nabla S}\nabla f, X\rangle_g,
\]
which proves (E.13).

For (E.12), fix a point `p` and a local orthonormal frame `(e_i)` normal at `p`, so `\nabla^{\mathrm{LC}}_{e_i}e_j(p)=0`. Then at `p`,
\[
\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}(\nabla f)
=
-\sum_i \nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_i}(\nabla f),
\]
and
\[
\nabla(\Delta f)=\sum_j e_j(\Delta f)\,e_j.
\]
A coordinate-free derivation of (E.12) is standard; for completeness we give a frame computation in Lemma E.4.5 below, which yields (E.12) at `p`. Since `p` was arbitrary, (E.12) holds globally.

Combining (E.12)–(E.13) and subtracting gives exactly (E.11) with `\mathcal L_S^{(1)}` defined by (E.10). ∎

**Lemma E.4.5 (commutation of `\nabla` and `\Delta` on gradients).**  
For every `f\in C^\infty(M)`,
\[
\nabla(\Delta f)=\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}(\nabla f)+\mathrm{Ric}_g^{\sharp}(\nabla f).
\]

*Proof.* Fix `p` and a local orthonormal frame `(e_i)` normal at `p`. Write `V:=\nabla f` and note that `\nabla^{\mathrm{LC}}_{e_i}V = \sum_j f_{ij} e_j` at `p`, where `f_{ij}=(\nabla^2 f)(e_i,e_j)`.

Compute at `p`:
\[
\big(\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\big)(p)
=
-\sum_i \nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_i}V
=
-\sum_{i,j} e_i(f_{ij})\,e_j - \sum_{i,j} f_{ij}\,\nabla^{\mathrm{LC}}_{e_i}e_j.
\]
The second term vanishes at `p` by normality, so
\[
\big(\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\big)(p)
=
-\sum_{i,j} e_i(f_{ij})\,e_j.
\tag{E.14}
\]

On the other hand, `\Delta f = \sum_i f_{ii}` at `p`, hence
\[
\nabla(\Delta f)(p)=\sum_j e_j\big(\sum_i f_{ii}\big)\,e_j=\sum_{i,j} e_j(f_{ii})\,e_j.
\tag{E.15}
\]

Thus the difference between (E.15) and `-(E.14)` is the commutator
\[
\sum_{i,j}\big(e_j(f_{ii})-e_i(f_{ij})\big)e_j.
\]
This commutator is exactly the curvature contribution. The torsion-free property implies the symmetry `f_{ij}=f_{ji}` at `p`, and the definition of the Riemann curvature tensor yields the standard identity (at `p`)
\[
e_j(f_{ii})-e_i(f_{ij})
=
\mathrm{Ric}_g(e_j,V),
\]
equivalently,
\[
\sum_i \big(\nabla^{\mathrm{LC}}_{e_j}\nabla^{\mathrm{LC}}_{e_i}\nabla f-\nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_j}\nabla f\big)\cdot e_i
=
\mathrm{Ric}_g^{\sharp}(V)\cdot e_j.
\]
Substituting into (E.14)–(E.15) gives
\[
\nabla(\Delta f)(p)=\big(\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\big)(p)+\mathrm{Ric}_g^{\sharp}(V)(p),
\]
which is the claimed identity. ∎

---

## E.5 Quadratic-form coercivity from curvature-matrix lower bounds

The principal use of the Bakry–Émery curvature matrix in this program is as follows: a pointwise lower bound
\[
\mathrm{Ric}_{\mu_S}(U)\succeq A(U)
\]
yields coercivity for the `1`-form generator `\mathcal L_S^{(1)}` at the quadratic-form level.

### E.5.1 Pointwise operator order

**Definition E.5.1 (pointwise operator order on `TM`).**  
Let `A` and `B` be smooth fields of self-adjoint endomorphisms of `TM`. Write
\[
A\succeq B
\]
if for every point `U\in M` and every `v\in T_U M`,
\[
\langle (A(U)-B(U))v,v\rangle_g \ge 0.
\]

### E.5.2 Coercivity inequality

**Proposition E.5.2 (curvature lower bound ⇒ quadratic-form lower bound for `\mathcal L_S^{(1)}`).**  
Let `A` be a smooth field of self-adjoint endomorphisms of `TM`. Assume
\[
\mathrm{Ric}_{\mu_S}^{\sharp}\succeq A
\quad\text{pointwise on }M.
\tag{E.16}
\]
Then for every smooth vector field `V`,
\[
\int_M \langle V,\mathcal L_S^{(1)}V\rangle_g\,d\mu_S
\ \ge\
\int_M \langle V,A V\rangle_g\,d\mu_S.
\tag{E.17}
\]

*Proof.* Expand `\mathcal L_S^{(1)}` from Definition E.4.3:
\[
\langle V,\mathcal L_S^{(1)}V\rangle_g
=
\langle V,\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\rangle_g
-\langle V,\nabla^{\mathrm{LC}}_{\nabla S}V\rangle_g
+\langle V,\mathrm{Ric}_{\mu_S}^{\sharp}V\rangle_g.
\]
Integrating over `M` with respect to `d\mu_S=e^{-S}Z_S^{-1}d\mathrm{vol}_g` and using the standard integration by parts for the rough Laplacian (no boundary), one obtains
\[
\int_M \Big(\langle V,\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\rangle_g
-\langle V,\nabla^{\mathrm{LC}}_{\nabla S}V\rangle_g\Big)\,d\mu_S
=
\int_M |\nabla^{\mathrm{LC}}V|_{\mathrm{HS}}^2\,d\mu_S,
\tag{E.18}
\]
which is nonnegative. (A derivation of (E.18) in the weighted measure `\mu_S` is given in Lemma E.5.3 below.)

Therefore
\[
\int_M \langle V,\mathcal L_S^{(1)}V\rangle_g\,d\mu_S
=
\int_M |\nabla^{\mathrm{LC}}V|_{\mathrm{HS}}^2\,d\mu_S
+
\int_M \langle V,\mathrm{Ric}_{\mu_S}^{\sharp}V\rangle_g\,d\mu_S
\ \ge\
\int_M \langle V,\mathrm{Ric}_{\mu_S}^{\sharp}V\rangle_g\,d\mu_S.
\]
Using the pointwise order assumption (E.16) and integrating yields (E.17). ∎

**Lemma E.5.3 (weighted integration by parts for the rough Laplacian).**  
For any smooth vector fields `V,W`,
\[
\int_M \langle W,\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\rangle_g\,d\mu_S
-
\int_M \langle W,\nabla^{\mathrm{LC}}_{\nabla S}V\rangle_g\,d\mu_S
=
\int_M \langle \nabla^{\mathrm{LC}}W,\nabla^{\mathrm{LC}}V\rangle_{\mathrm{HS}}\,d\mu_S,
\tag{E.19}
\]
where `\langle\cdot,\cdot\rangle_{\mathrm{HS}}` is the Hilbert–Schmidt inner product on `(1,1)`-tensors induced by `g`.

In particular, taking `W=V` gives (E.18).

*Proof.* Fix a local orthonormal frame `(e_i)` and write the covariant derivative as `\nabla^{\mathrm{LC}}V=\sum_i (\nabla^{\mathrm{LC}}_{e_i}V)\otimes e^i`. By definition of the rough Laplacian,
\[
\langle W,\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\rangle_g
=
-\sum_i \langle W, \nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_i}V-\nabla^{\mathrm{LC}}_{\nabla^{\mathrm{LC}}_{e_i}e_i}V\rangle_g.
\]
Consider the vector field
\[
X:=\sum_i \langle W,\nabla^{\mathrm{LC}}_{e_i}V\rangle_g\,e_i.
\]
A direct computation using metric-compatibility shows
\[
\mathrm{div}X
=
\sum_i \langle \nabla^{\mathrm{LC}}_{e_i}W,\nabla^{\mathrm{LC}}_{e_i}V\rangle_g
+
\sum_i \langle W,\nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_i}V-\nabla^{\mathrm{LC}}_{\nabla^{\mathrm{LC}}_{e_i}e_i}V\rangle_g.
\]
Rearranging gives
\[
\sum_i \langle W,\nabla^{\mathrm{LC}}_{e_i}\nabla^{\mathrm{LC}}_{e_i}V-\nabla^{\mathrm{LC}}_{\nabla^{\mathrm{LC}}_{e_i}e_i}V\rangle_g
=
\mathrm{div}X-\langle \nabla^{\mathrm{LC}}W,\nabla^{\mathrm{LC}}V\rangle_{\mathrm{HS}}.
\]
Hence
\[
\langle W,\nabla^{\mathrm{LC}\,*}\nabla^{\mathrm{LC}}V\rangle_g
=
-\mathrm{div}X+\langle \nabla^{\mathrm{LC}}W,\nabla^{\mathrm{LC}}V\rangle_{\mathrm{HS}}.
\]
Integrate against `d\mu_S=Z_S^{-1}e^{-S}d\mathrm{vol}_g` and apply the divergence characterization (Definition E.1.3) to the vector field `e^{-S}X`:
\[
\int_M (-\mathrm{div}X)\,d\mu_S
=
-Z_S^{-1}\int_M \mathrm{div}X\,e^{-S}\,d\mathrm{vol}_g
=
-Z_S^{-1}\int_M e^{S}\,\mathrm{div}(e^{-S}X)\,d\mu_S
=
Z_S^{-1}\int_M \langle \nabla S, X\rangle_g\,e^{-S}\,d\mathrm{vol}_g,
\]
which simplifies to
\[
\int_M (-\mathrm{div}X)\,d\mu_S
=
\int_M \langle \nabla S, X\rangle_g\,d\mu_S
=
\int_M \sum_i \langle W,\nabla^{\mathrm{LC}}_{e_i}V\rangle_g\,\langle \nabla S,e_i\rangle_g\,d\mu_S
=
\int_M \langle W,\nabla^{\mathrm{LC}}_{\nabla S}V\rangle_g\,d\mu_S.
\]
Putting these identities together yields (E.19). ∎

---

## E.6 Optional boundary-localized variant (Neumann realization on a smooth domain)

Some later localization steps restrict the dynamics to a compact domain `K\subset M` and use the Neumann (reflecting) realization of `\mathcal L_S` with respect to the conditioned measure `\mu_S(\cdot\mid K)`. This subsection records the minimal integration-by-parts identity needed to preserve symmetry; no curvature estimates are made here.

**Definition E.6.1 (smooth domain and outward unit normal).**  
Let `K\subset M` be a compact domain with `C^2` boundary `\partial K`. Denote by `\mathbf n` the outward unit normal along `\partial K`.

**Definition E.6.2 (Neumann boundary condition).**  
A smooth function `f` on `\overline K` satisfies the Neumann boundary condition if
\[
\partial_{\mathbf n} f:=\langle \nabla f,\mathbf n\rangle_g = 0
\quad\text{on }\partial K.
\]

**Definition E.6.3 (conditioned measure on `K`).**  
Define the probability measure on `K` by
\[
d\mu_{S,K}
:=
Z_{S,K}^{-1}\,\mathbf 1_K\,e^{-S}\,d\mathrm{vol}_g,
\qquad
Z_{S,K}:=\int_K e^{-S}\,d\mathrm{vol}_g.
\]

**Proposition E.6.4 (integration by parts on `K` under Neumann boundary conditions).**  
Let `f,g\in C^\infty(\overline K)` satisfy the Neumann boundary condition. Then
\[
\int_K f\,(\mathcal L_S g)\,d\mu_{S,K}
=
-\int_K \langle \nabla f,\nabla g\rangle_g\,d\mu_{S,K}.
\tag{E.20}
\]
In particular, the operator `\mathcal L_S` with domain restricted to Neumann functions is symmetric in `L^2(\mu_{S,K})` and preserves constants.

*Proof.* Using Lemma E.1.4 in divergence form and the divergence theorem on the smooth domain `K`,
\[
\int_K f\,\mathcal L_S g\,d\mu_{S,K}
=
Z_{S,K}^{-1}\int_K f\,\mathrm{div}(e^{-S}\nabla g)\,d\mathrm{vol}_g
=
-Z_{S,K}^{-1}\int_K \langle \nabla f,e^{-S}\nabla g\rangle_g\,d\mathrm{vol}_g
+
Z_{S,K}^{-1}\int_{\partial K} f\,e^{-S}\,\partial_{\mathbf n}g\,d\sigma_g.
\]
The boundary term vanishes by the Neumann condition. The remaining term is `-\int_K \langle\nabla f,\nabla g\rangle_g\,d\mu_{S,K}`. ∎

---

## E.7 Summary of “feeds into” usage

- Appendix F uses Definitions E.3.4 and Proposition E.3.5 to interpret pointwise lower bounds on `\mathrm{Ric}_{\mu_S}` as structured “curvature matrix” inequalities.
- Appendix G uses Proposition E.4.4 and Proposition E.5.2 as the geometric part of the `1`-form generator coercivity interface.

