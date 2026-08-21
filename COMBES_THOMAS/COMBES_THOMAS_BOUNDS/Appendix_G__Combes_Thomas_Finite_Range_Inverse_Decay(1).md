---
file: Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
feeds_into:
  - Core-6 (Finite-range inverse decay / Green-kernel bounds)
  - Core-7 (Fixed-cutoff exponential clustering via HS + kernel decay)
  - Core-9 (OS reconstruction: Euclidean time decay ⇒ Hamiltonian gap; uses clustering)
---

# Appendix G — Finite-range inverse decay via Combes–Thomas conjugation

## G.0 Scope and dependency interface

**Definition G.0.1 (scope).**  
This appendix proves a deterministic exponential off-diagonal decay bound for block entries of the inverse of a uniformly positive, finite-range, self-adjoint operator acting on a finite graph with a finite-dimensional fiber. The bound is expressed in terms of the Combes–Thomas parameters `a_0(A)`, `R(A)`, `B_0(A)` and the decay rate `\eta_{\mathrm{CT}}(A)` defined in Appendix A (Definitions A.10.1–A.10.2).

**Definition G.0.2 (downstream use).**  
The output of this appendix is used as follows:
- Appendix F expresses covariances through an inverse operator on 1-cochains; this appendix supplies the kernel decay bound for that inverse once the operator is identified as a massive finite-range operator.
- The Core Manuscript uses the resulting kernel bound to turn the Helffer–Sjöstrand representation into exponential clustering estimates at fixed cutoff.

**Definition G.0.3 (imported constants and operators).**  
No new named constants are introduced in this appendix. In particular, all constants appearing below are those already defined in Appendix A, including:
- the link graph distance `\mathrm{dist}_E` (Definition A.2.9),
- the massive Maxwell operator `M_{\Lambda_L}` (Definition A.9.2),
- the Combes–Thomas parameters `a_0(\cdot),R(\cdot),B_0(\cdot)` and rate `\eta_{\mathrm{CT}}(\cdot)` (Definitions A.10.1–A.10.2),
together with the finite-range/row-sum verifications for `M_{\Lambda_L}` from Appendix B (Proposition B.4.7) and the horizontal invariance from Appendix B (Lemma B.4.8).

---

## G.1 Operators on a finite graph with fiber

**Definition G.1.1 (fibered \(\ell^2\) space).**  
Let `V` be a finite set. Let `\mathsf H_0` be a finite-dimensional real Hilbert space with inner product `\langle\cdot,\cdot\rangle_{\mathsf H_0}` and norm `|\cdot|_{\mathsf H_0}`. Define the Hilbert space
\[
\ell^2(V;\mathsf H_0)
:=
\Bigl\{ f:V\to \mathsf H_0 \Bigr\},
\qquad
\|f\|_{\ell^2(V;\mathsf H_0)}^2:=\sum_{x\in V}|f(x)|_{\mathsf H_0}^2.
\]
Since `V` is finite, every function `f:V\to\mathsf H_0` belongs to this space.

**Definition G.1.2 (block matrix representation).**  
Let `A:\ell^2(V;\mathsf H_0)\to \ell^2(V;\mathsf H_0)` be linear. There exist unique block operators
\[
A_{xy}\in \mathrm{End}(\mathsf H_0),
\qquad x,y\in V,
\]
such that for every `f`,
\[
(Af)(x)=\sum_{y\in V} A_{xy}\,f(y),
\qquad x\in V.
\]
The operator norm on each block is denoted `\|\cdot\|_{\mathrm{op}}` (computed in `\mathrm{End}(\mathsf H_0)`), and the induced operator norm on `A` acting on `\ell^2(V;\mathsf H_0)` is also denoted `\|A\|_{\mathrm{op}}`.

**Definition G.1.3 (inverse blocks).**  
If `A` is invertible, its inverse `A^{-1}` has a block representation `((A^{-1})_{xy})_{x,y\in V}` as in Definition G.1.2.  
For each pair `(x,y)`, the quantity `\|(A^{-1})_{xy}\|_{\mathrm{op}}` is called the (block) inverse kernel magnitude from `y` to `x`.

**Definition G.1.4 (graph distance and Lipschitz weight).**  
Assume `V` is equipped with a graph distance `\mathrm{dist}:V\times V\to\mathbb N\cup\{0\}`.  
Fix `y\in V` and define the distance weight
\[
\phi_y(x):=\mathrm{dist}(x,y),\qquad x\in V.
\]
Then `\phi_y` is 1-Lipschitz in the sense that for all `x,x'\in V`,
\[
|\phi_y(x)-\phi_y(x')|\le \mathrm{dist}(x,x').
\]

---

## G.2 A block Schur estimate for operator norms

**Lemma G.2.1 (block Schur bound; finite-dimensional fiber).**  
Let `K:\ell^2(V;\mathsf H_0)\to \ell^2(V;\mathsf H_0)` have blocks `K_{xy}\in\mathrm{End}(\mathsf H_0)`. Assume there exist finite constants `R_0,C_0` such that
\[
\sup_{x\in V}\sum_{y\in V}\|K_{xy}\|_{\mathrm{op}}\le R_0,
\qquad
\sup_{y\in V}\sum_{x\in V}\|K_{xy}\|_{\mathrm{op}}\le C_0.
\]
Then
\[
\|K\|_{\mathrm{op}}\le \sqrt{R_0\,C_0}.
\]
If, in addition, `K` is self-adjoint on `\ell^2(V;\mathsf H_0)`, then the row bound implies the column bound with the same constant and hence
\[
\|K\|_{\mathrm{op}}\le R_0.
\]

**Proof.**  
Fix `f,g\in \ell^2(V;\mathsf H_0)`. By Cauchy–Schwarz in `\mathsf H_0`,
\[
\big|\langle g(x),K_{xy}f(y)\rangle_{\mathsf H_0}\big|
\le |g(x)|_{\mathsf H_0}\,\|K_{xy}\|_{\mathrm{op}}\,|f(y)|_{\mathsf H_0}.
\]
Summing over `x,y` yields
\[
\begin{aligned}
|\langle g,Kf\rangle|
&=
\Big|\sum_{x\in V}\Big\langle g(x),\sum_{y\in V}K_{xy}f(y)\Big\rangle_{\mathsf H_0}\Big|
\le \sum_{x,y\in V}\|K_{xy}\|_{\mathrm{op}}\,|g(x)|_{\mathsf H_0}\,|f(y)|_{\mathsf H_0}.
\end{aligned}
\]
Using the elementary inequality `ab\le \tfrac12(a^2+b^2)` with  
`a=|g(x)|_{\mathsf H_0}\sqrt{\|K_{xy}\|_{\mathrm{op}}}` and `b=|f(y)|_{\mathsf H_0}\sqrt{\|K_{xy}\|_{\mathrm{op}}}`, we obtain
\[
\|K_{xy}\|_{\mathrm{op}}\,|g(x)|\,|f(y)|
\le \frac12\|K_{xy}\|_{\mathrm{op}}\,|g(x)|^2
+\frac12\|K_{xy}\|_{\mathrm{op}}\,|f(y)|^2.
\]
Summing this bound gives
\[
|\langle g,Kf\rangle|
\le
\frac12\sum_{x\in V}|g(x)|^2\sum_{y\in V}\|K_{xy}\|_{\mathrm{op}}
+
\frac12\sum_{y\in V}|f(y)|^2\sum_{x\in V}\|K_{xy}\|_{\mathrm{op}}.
\]
Applying the assumed row/column bounds yields
\[
|\langle g,Kf\rangle|
\le \frac12 R_0\|g\|^2 + \frac12 C_0\|f\|^2.
\]
Replace `g` by `\lambda g` and optimize over `\lambda>0` to obtain
\[
|\langle g,Kf\rangle|\le \sqrt{R_0C_0}\ \|g\|\ \|f\|.
\]
Taking the supremum over unit vectors gives `\|K\|_{\mathrm{op}}\le \sqrt{R_0C_0}`.

If `K` is self-adjoint, then the block norms satisfy `\|K_{xy}\|_{\mathrm{op}}=\|K_{yx}\|_{\mathrm{op}}`, hence
\[
\sup_{y}\sum_{x}\|K_{xy}\|_{\mathrm{op}}
=
\sup_{y}\sum_{x}\|K_{yx}\|_{\mathrm{op}}
\le \sup_{x}\sum_{y}\|K_{xy}\|_{\mathrm{op}}
\le R_0,
\]
so one may take `C_0=R_0`, giving `\|K\|_{\mathrm{op}}\le R_0`. ∎

---

## G.3 Combes–Thomas inverse decay for uniformly positive finite-range operators

**Proposition G.3.1 (Combes–Thomas inverse kernel decay).**  
Let `V` be a finite set with graph distance `\mathrm{dist}`, and take `\mathsf H_0=\mathfrak g` with inner product from Appendix A (Definition A.3.5).  
Let `A` be a self-adjoint operator on `\ell^2(V;\mathfrak g)`.

Assume that `a_0(A)>0`, `R(A)<\infty`, and `B_0(A)<\infty` in the sense of Appendix A (Definition A.10.1). Then `A` is invertible and for all `x,y\in V`,
\[
\big\|(A^{-1})_{xy}\big\|_{\mathrm{op}}
\le
\frac{2}{a_0(A)}\exp\!\big(-\eta_{\mathrm{CT}}(A)\,\mathrm{dist}(x,y)\big),
\]
where `\eta_{\mathrm{CT}}(A)` is the Combes–Thomas decay rate from Appendix A (Definition A.10.2).  
If `B_0(A)=0`, the bound holds with `\eta_{\mathrm{CT}}(A)=+\infty`, and in that case `A` is diagonal in the `V`-index.

**Proof.**  
Fix an arbitrary basepoint `y_0\in V` and define the 1-Lipschitz weight
\[
\phi_{y_0}(x):=\mathrm{dist}(x,y_0),\qquad x\in V
\]
as in Definition G.1.4. For each `t\ge 0` define the diagonal weight operator `W_t` by
\[
(W_t f)(x):=e^{t\phi_{y_0}(x)}\,f(x),
\qquad
(W_t^{-1} f)(x):=e^{-t\phi_{y_0}(x)}\,f(x).
\]
Define the conjugated operator
\[
A_t := W_t\,A\,W_t^{-1}.
\]
This is a similarity transform of `A`, hence `A_t` is invertible if and only if `A` is invertible, with
\[
A^{-1} = W_t^{-1}\,A_t^{-1}\,W_t.
\tag{G.3.2}
\]

**Step 1 (explicit blocks of the conjugation).**  
Let `A_{xz}` denote the block entries of `A` (Definition G.1.2). Then the block entries of `A_t` satisfy
\[
(A_t)_{xz} = e^{t(\phi_{y_0}(x)-\phi_{y_0}(z))}\,A_{xz}.
\tag{G.3.3}
\]
Indeed, for any `f`,
\[
(A_t f)(x)
=
e^{t\phi_{y_0}(x)}\sum_{z\in V}A_{xz}\big(e^{-t\phi_{y_0}(z)}f(z)\big)
=
\sum_{z\in V}\big(e^{t(\phi_{y_0}(x)-\phi_{y_0}(z))}A_{xz}\big)f(z).
\]

Define the perturbation `K_t:=A_t-A`. By (G.3.3),
\[
(K_t)_{xz} = \big(e^{t(\phi_{y_0}(x)-\phi_{y_0}(z))}-1\big)\,A_{xz}.
\tag{G.3.4}
\]
Note in particular that `(K_t)_{xx}=0` for every `x`, since `\phi_{y_0}(x)-\phi_{y_0}(x)=0`.

**Step 2 (row and column bounds for the perturbation).**  
If `A_{xz}\neq 0`, then by the definition of `R(A)` (Definition A.10.1) one has `\mathrm{dist}(x,z)\le R(A)`. By the 1-Lipschitz property (Definition G.1.4),
\[
|\phi_{y_0}(x)-\phi_{y_0}(z)| \le \mathrm{dist}(x,z)\le R(A).
\tag{G.3.5}
\]
For any real number `u` with `|u|\le R(A)`, one has `e^{tu}\in[e^{-tR(A)},e^{tR(A)}]`, hence
\[
|e^{tu}-1|
\le \max\{e^{tR(A)}-1,\ 1-e^{-tR(A)}\}
= e^{tR(A)}-1.
\]
Applying this with `u=\phi_{y_0}(x)-\phi_{y_0}(z)` and using (G.3.4) gives, for every `x\neq z`,
\[
\|(K_t)_{xz}\|_{\mathrm{op}}
\le \big(e^{tR(A)}-1\big)\,\|A_{xz}\|_{\mathrm{op}}.
\tag{G.3.6}
\]

**Row sums.** Summing (G.3.6) over `z\neq x` and taking the supremum in `x`,
\[
\sup_{x\in V}\sum_{z\neq x}\|(K_t)_{xz}\|_{\mathrm{op}}
\le \big(e^{tR(A)}-1\big)\,B_0(A).
\tag{G.3.7}
\]

**Column sums.** Fix `z\in V`. Summing (G.3.6) over `x\neq z` gives
\[
\sum_{x\neq z}\|(K_t)_{xz}\|_{\mathrm{op}}
\le \big(e^{tR(A)}-1\big)\sum_{x\neq z}\|A_{xz}\|_{\mathrm{op}}.
\]
Since `A` is self-adjoint, one has `A_{xz}=A_{zx}^*`, hence `\|A_{xz}\|_{\mathrm{op}}=\|A_{zx}\|_{\mathrm{op}}`. Therefore
\[
\sum_{x\neq z}\|A_{xz}\|_{\mathrm{op}}
=
\sum_{x\neq z}\|A_{zx}\|_{\mathrm{op}}
\le \sup_{z\in V}\sum_{x\neq z}\|A_{zx}\|_{\mathrm{op}}
= B_0(A),
\]
and consequently
\[
\sup_{z\in V}\sum_{x\neq z}\|(K_t)_{xz}\|_{\mathrm{op}}
\le \big(e^{tR(A)}-1\big)\,B_0(A).
\tag{G.3.8}
\]

Applying Lemma G.2.1 with `R_0=C_0=(e^{tR(A)}-1)B_0(A)` yields
\[
\|K_t\|_{\mathrm{op}}
\le \big(e^{tR(A)}-1\big)\,B_0(A).
\tag{G.3.9}
\]

**Step 3 (invertibility of \(A_t\) for small \(t\) and a uniform inverse norm bound).**  
Because `a_0(A)>0`, one has `A\succeq a_0(A)\,I` and in particular
\[
\|A^{-1}\|_{\mathrm{op}}\le \frac{1}{a_0(A)}.
\tag{G.3.10}
\]
Assume `t\ge 0` is chosen so that
\[
\|K_t\|_{\mathrm{op}}\le \frac{a_0(A)}{2}.
\tag{G.3.11}
\]
Then
\[
\|K_tA^{-1}\|_{\mathrm{op}}
\le \|K_t\|_{\mathrm{op}}\ \|A^{-1}\|_{\mathrm{op}}
\le \frac{a_0(A)}{2}\cdot \frac{1}{a_0(A)}
=\frac12.
\tag{G.3.12}
\]
Consequently `I+K_tA^{-1}` is invertible and
\[
A_t^{-1} = (A+K_t)^{-1} = A^{-1}\,(I+K_tA^{-1})^{-1}.
\tag{G.3.13}
\]
Using `\|(I+T)^{-1}\|_{\mathrm{op}}\le (1-\|T\|_{\mathrm{op}})^{-1}` when `\|T\|_{\mathrm{op}}<1` and (G.3.12),
\[
\|A_t^{-1}\|_{\mathrm{op}}
\le \|A^{-1}\|_{\mathrm{op}}\ \frac{1}{1-\|K_tA^{-1}\|_{\mathrm{op}}}
\le \frac{1}{a_0(A)}\cdot \frac{1}{1-1/2}
=
\frac{2}{a_0(A)}.
\tag{G.3.14}
\]

A sufficient condition for (G.3.11) is obtained by combining (G.3.9) and (G.3.11), namely
\[
\big(e^{tR(A)}-1\big)\,B_0(A)\le \frac{a_0(A)}{2}.
\tag{G.3.15}
\]
When `B_0(A)>0` and `R(A)\ge 1`, (G.3.15) is equivalent to
\[
t \le \frac{1}{R(A)}\log\Big(1+\frac{a_0(A)}{2B_0(A)}\Big)=\eta_{\mathrm{CT}}(A),
\tag{G.3.16}
\]
which is exactly Definition A.10.2. When `B_0(A)=0`, the off-diagonal blocks vanish and (G.3.15) holds for all `t` with the convention `\eta_{\mathrm{CT}}(A)=+\infty`.

**Step 4 (extracting decay of inverse blocks).**  
Using (G.3.2) at the block level gives, for every `x,z\in V`,
\[
(A^{-1})_{xz}
=
e^{-t\phi_{y_0}(x)}\,(A_t^{-1})_{xz}\,e^{t\phi_{y_0}(z)}.
\tag{G.3.17}
\]
In particular, taking `z=y_0` and using `\phi_{y_0}(y_0)=0`,
\[
(A^{-1})_{x y_0}
=
e^{-t\,\mathrm{dist}(x,y_0)}\,(A_t^{-1})_{x y_0}.
\]
Taking operator norms and using `\|(A_t^{-1})_{x y_0}\|_{\mathrm{op}}\le \|A_t^{-1}\|_{\mathrm{op}}` yields
\[
\|(A^{-1})_{x y_0}\|_{\mathrm{op}}
\le
e^{-t\,\mathrm{dist}(x,y_0)}\,\|A_t^{-1}\|_{\mathrm{op}}.
\tag{G.3.18}
\]
For every `t` satisfying (G.3.16), insert (G.3.14) into (G.3.18):
\[
\|(A^{-1})_{x y_0}\|_{\mathrm{op}}
\le
\frac{2}{a_0(A)}\exp\!\big(-t\,\mathrm{dist}(x,y_0)\big).
\]
Choosing `t=\eta_{\mathrm{CT}}(A)` yields the bound with decay rate `\eta_{\mathrm{CT}}(A)`.

Finally, since `y_0\in V` was arbitrary, the same bound holds for every pair `(x,y)\in V\times V`. ∎

---

## G.4 Specialization to the massive Maxwell operator on links

**Proposition G.4.1 (exponential decay for the inverse massive Maxwell kernel).**  
Let `\Lambda_L` be a finite periodic lattice (Definition A.1.3), let `V:=E(\Lambda_L)` and equip `V` with the link graph distance `\mathrm{dist}_E` (Definition A.2.9).  
Let `M_{\Lambda_L}` be the massive Maxwell operator (Definition A.9.2) acting on `\ell^2(E(\Lambda_L);\mathfrak g)=\mathcal C^1(\Lambda_L;\mathfrak g)`.

Then for all links `b,b'\in E(\Lambda_L)`,
\[
\big\|\big(M_{\Lambda_L}^{-1}\big)_{bb'}\big\|_{\mathrm{op}}
\le
\frac{2}{m_H^2}\exp\!\big(-\eta_{\mathrm{CT}}(M_{\Lambda_L})\,\mathrm{dist}_E(b,b')\big).
\tag{G.4.2}
\]
Moreover, using the explicit uniform bounds from Appendix B (Proposition B.4.7), one has the volume-uniform estimate
\[
\eta_{\mathrm{CT}}(M_{\Lambda_L})
\ \ge\
\log\!\Big(1+\frac{m_H^2}{2\,\alpha_W\,(3\,\nu_P)}\Big),
\tag{G.4.3}
\]
and hence the weaker (but explicit and volume-uniform) decay bound
\[
\big\|\big(M_{\Lambda_L}^{-1}\big)_{bb'}\big\|_{\mathrm{op}}
\le
\frac{2}{m_H^2}\exp\!\Big(-\log\!\Big(1+\frac{m_H^2}{2\,\alpha_W\,(3\,\nu_P)}\Big)\ \mathrm{dist}_E(b,b')\Big).
\tag{G.4.4}
\]

**Proof.**  
Apply Proposition G.3.1 with:
- `V=E(\Lambda_L)`, `\mathrm{dist}=\mathrm{dist}_E` (Definitions A.2.8–A.2.9),
- `A=M_{\Lambda_L}` (Definition A.9.2).

By Proposition B.4.7:
1. `M_{\Lambda_L}\succeq m_H^2\,\mathrm{Id}`, hence `a_0(M_{\Lambda_L})\ge m_H^2`.
2. `M_{\Lambda_L}` has link-graph interaction range one, hence `R(M_{\Lambda_L})=1`.
3. The off-diagonal row-sum constant satisfies `B_0(M_{\Lambda_L})\le \alpha_W(3\nu_P)`.

Proposition G.3.1 gives (G.4.2) with `a_0(M_{\Lambda_L})` in place of `m_H^2`; since `a_0(M_{\Lambda_L})\ge m_H^2`, the prefactor can be enlarged to `2/m_H^2` without invalidating the inequality.

For (G.4.3), use `R(M_{\Lambda_L})=1` and Definition A.10.2:
\[
\eta_{\mathrm{CT}}(M_{\Lambda_L})=\log\Big(1+\frac{a_0(M_{\Lambda_L})}{2B_0(M_{\Lambda_L})}\Big)
\ge
\log\Big(1+\frac{m_H^2}{2\,\alpha_W\,(3\nu_P)}\Big),
\]
where we used `a_0(M_{\Lambda_L})\ge m_H^2` and `B_0(M_{\Lambda_L})\le \alpha_W(3\nu_P)`.  
Finally, replace `\eta_{\mathrm{CT}}(M_{\Lambda_L})` in (G.4.2) by the lower bound (G.4.3) to obtain (G.4.4). ∎

**Proposition G.4.2 (horizontal invariance passes to the inverse).**  
Let `H^{(0)}:=\ker(d_0^*)\subset \mathcal C^1(\Lambda_L;\mathfrak g)` be the horizontal subspace (Definition B.3.4).  
Assume `H^{(0)}` is invariant under `M_{\Lambda_L}` (Lemma B.4.8), i.e. `M_{\Lambda_L}(H^{(0)})\subset H^{(0)}`.

Define the restricted operator
\[
M_{\Lambda_L,H}:= M_{\Lambda_L}\big|_{H^{(0)}}:H^{(0)}\to H^{(0)}.
\]
Then:
1. `M_{\Lambda_L,H}` is invertible.
2. The inverse on `H^{(0)}` agrees with the ambient inverse restricted to `H^{(0)}`:
   \[
   \big(M_{\Lambda_L,H}\big)^{-1}
   =
   \big(M_{\Lambda_L}^{-1}\big)\big|_{H^{(0)}}.
   \tag{G.4.5}
   \]
3. Consequently, whenever downstream arguments apply `M_{\Lambda_L,H}^{-1}` to horizontal vectors, the resulting estimates may be obtained by using the block kernel of the ambient inverse `M_{\Lambda_L}^{-1}` together with the decay bounds of Proposition G.4.1.

**Proof.**  
(1) By Proposition B.4.7(1), `M_{\Lambda_L}\succeq m_H^2\,\mathrm{Id}` on `\mathcal C^1(\Lambda_L;\mathfrak g)`, hence `M_{\Lambda_L}` is injective. The restriction `M_{\Lambda_L,H}` is therefore injective on the finite-dimensional space `H^{(0)}`, hence invertible.

(2) Fix `Y\in H^{(0)}`. Let `X:=M_{\Lambda_L}^{-1}Y`. Then `M_{\Lambda_L}X=Y`. Because `Y\in H^{(0)}` and `H^{(0)}` is invariant under `M_{\Lambda_L}`, any solution of `M_{\Lambda_L}X=Y` that lies in `H^{(0)}` must coincide with the unique solution in `H^{(0)}` given by `X_H:=(M_{\Lambda_L,H})^{-1}Y`.  
To show that `X` is horizontal, note that invariance implies `M_{\Lambda_L}:H^{(0)}\to H^{(0)}`. Since `M_{\Lambda_L}` is invertible on the full space, it restricts to a bijection between `H^{(0)}` and itself: for each `Y\in H^{(0)}` there exists a unique `X_H\in H^{(0)}` with `M_{\Lambda_L}X_H=Y`. But also `X=M_{\Lambda_L}^{-1}Y` satisfies the same equation. Uniqueness forces `X=X_H\in H^{(0)}`. This proves (G.4.5).

(3) Item (3) is a direct consequence of (G.4.5): on horizontal inputs, `M_{\Lambda_L,H}^{-1}` acts identically to `M_{\Lambda_L}^{-1}`, for which Proposition G.4.1 provides explicit exponential decay bounds on its block kernel. ∎

---

## G.5 Output summary for downstream use

**Definition G.5.1 (exported statements).**  
Downstream arguments use Appendix G through the following interfaces:
- Lemma G.2.1 (Schur bound for operator norms from block row/column sums),
- Proposition G.3.1 (abstract Combes–Thomas inverse decay bound),
- Proposition G.4.1 (application to `M_{\Lambda_L}` and its inverse kernel decay),
- Proposition G.4.2 (horizontal invariance passes to the inverse; restriction identity (G.4.5)).

