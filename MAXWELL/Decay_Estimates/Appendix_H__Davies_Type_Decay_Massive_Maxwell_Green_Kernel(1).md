---
file: Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md
feeds_into:
  - Core-7 (Green-kernel decay for the massive Maxwell operator; alternative to Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md)
  - Core-8 (Fixed-cutoff clustering; via insertion of Green-kernel decay into the Helffer–Sjöstrand bound)
---

# Appendix H — Davies-type semigroup conjugation and Green-kernel decay for the massive Maxwell operator

## H.0 Scope and dependency interface

**Definition H.0.1 (scope).**  
This appendix proves an exponential off-diagonal decay bound for the inverse kernel of the **massive Maxwell operator**
\[
M_{\Lambda_L}=m_H^2\,\mathrm{Id}+\alpha_W\,\mathsf M_1
\qquad\text{on }\mathcal C^1(\Lambda_L;\mathfrak g)\cong\ell^2\big(E(\Lambda_L);\mathfrak g\big),
\]
where the mass `m_H^2`, coefficient `\alpha_W`, and Maxwell operator `\mathsf M_1=d_1^*d_1` are defined in Appendix A (Definitions A.8.3, A.9.1, A.9.2). The decay is measured in the link graph distance `\mathrm{dist}_E` (Definitions A.2.8–A.2.9).

**Definition H.0.2 (method).**  
The proof uses:
- a Laplace-transform representation of `(m^2 I + L)^{-1}` in terms of the semigroup `e^{-tL}` (Lemma H.1.1), and
- a Davies-type conjugation estimate controlling `\|e^{-t(WLW^{-1})}\|` for specific diagonal weights `W` built from `\mathrm{dist}_E` (Proposition H.3.4).

**Definition H.0.3 (downstream interface).**  
The final exported bound is Proposition H.4.1, which provides an explicit exponential kernel decay estimate for `M_{\Lambda_L}^{-1}` in terms of the constants already registered in Appendix A, namely `m_H^2`, `\alpha_W`, and `C_\partial(\mathsf M_1)` (Definition A.9.4). The horizontal restriction interface is Proposition H.4.2.

**Definition H.0.4 (no new named constants).**  
No new named constants are introduced. In particular, the only quantitative inputs used in the final decay rate are the constants defined in Appendix A.

---

## H.1 Laplace-transform formula for the inverse of a massive nonnegative operator

**Lemma H.1.1 (resolvent as Laplace transform; finite-dimensional form).**  
Let `(\mathsf H,\langle\cdot,\cdot\rangle)` be a finite-dimensional real Hilbert space. Let `L:\mathsf H\to\mathsf H` be self-adjoint and nonnegative as a quadratic form, i.e.
\[
\langle u,Lu\rangle\ge 0\qquad\forall u\in\mathsf H.
\]
Fix `m^2>0` and define `M:=m^2\,\mathrm{Id}+L`. Then `M` is invertible and
\[
M^{-1}
=\int_0^{\infty} e^{-m^2 t}\,e^{-tL}\,dt,
\tag{H.1.1}
\]
where the integral converges in operator norm.

**Proof.**  
Since `L` is self-adjoint on a finite-dimensional Hilbert space, it admits an orthonormal eigenbasis `(v_j)_{j=1}^N` with eigenvalues `\lambda_j\in\mathbb R`. The nonnegativity hypothesis gives `\lambda_j\ge 0` for all `j`.

For each eigenvector `v_j`, one has
\[
M^{-1}v_j=(m^2+\lambda_j)^{-1}v_j,
\qquad
(e^{-tL}v_j)=e^{-t\lambda_j}v_j.
\]
For every `\lambda\ge 0`, the scalar identity
\[
(m^2+\lambda)^{-1}=\int_0^{\infty}e^{-(m^2+\lambda)t}\,dt
\]
holds and the integral converges absolutely. Applying this with `\lambda=\lambda_j` yields
\[
(m^2+\lambda_j)^{-1}v_j
=\int_0^{\infty}e^{-m^2 t}\,e^{-t\lambda_j}v_j\,dt
=\int_0^{\infty}e^{-m^2 t}\,(e^{-tL}v_j)\,dt.
\]
By linearity, the identity extends to every vector in `\mathsf H`. For operator-norm convergence, note that `\|e^{-tL}\|_{\mathrm{op}}\le 1` because `L\succeq 0` implies `\sigma(L)\subset[0,\infty)` and hence `\sigma(e^{-tL})\subset (0,1]`. Therefore
\[
\Big\|\int_0^{\infty} e^{-m^2 t}e^{-tL}\,dt\Big\|_{\mathrm{op}}
\le
\int_0^{\infty}e^{-m^2 t}\,\|e^{-tL}\|_{\mathrm{op}}\,dt
\le
\int_0^{\infty}e^{-m^2 t}\,dt
=\frac{1}{m^2}<\infty.
\]
Thus the integral converges in operator norm and equals `M^{-1}`. ∎

**Lemma H.1.2 (Laplace formula for the massive Maxwell inverse).**  
Let `\Lambda_L` be a finite periodic lattice (Definition A.1.3). Let
\[
L_{\Lambda_L}:=\alpha_W\,\mathsf M_1\qquad\text{and}\qquad M_{\Lambda_L}:=m_H^2\,\mathrm{Id}+L_{\Lambda_L}
\]
(Definitions A.9.1–A.9.2). Then
\[
M_{\Lambda_L}^{-1}
=\int_0^{\infty} e^{-m_H^2 t}\,e^{-tL_{\Lambda_L}}\,dt
\tag{H.1.2}
\]
in operator norm on `\ell^2(E(\Lambda_L);\mathfrak g)`.

**Proof.**  
Apply Lemma H.1.1 with `\mathsf H=\ell^2(E(\Lambda_L);\mathfrak g)`, `L=L_{\Lambda_L}`, and `m^2=m_H^2`. Nonnegativity of `L_{\Lambda_L}` follows from `\mathsf M_1=d_1^*d_1\succeq 0` (Lemma B.4.1). ∎

---

## H.2 Davies conjugation: weighted similarity transforms

**Definition H.2.1 (distance weight on links).**  
Fix `b'\in E(\Lambda_L)`. Define
\[
\phi_{b'}:E(\Lambda_L)\to\mathbb N\cup\{0\},
\qquad
\phi_{b'}(b):=\mathrm{dist}_E(b,b'),
\]
where `\mathrm{dist}_E` is the link graph distance (Definition A.2.9).

**Lemma H.2.2 (1-Lipschitz property of the distance weight).**  
For all links `b,\tilde b\in E(\Lambda_L)`,
\[
|\phi_{b'}(b)-\phi_{b'}(\tilde b)|\le \mathrm{dist}_E(b,\tilde b).
\tag{H.2.1}
\]
In particular, if `\mathrm{dist}_E(b,\tilde b)\le 1`, then `|\phi_{b'}(b)-\phi_{b'}(\tilde b)|\in\{0,1\}`.

**Proof.**  
The inequality (H.2.1) is the triangle inequality for the graph distance:
\[
\mathrm{dist}_E(b,b')\le \mathrm{dist}_E(b,\tilde b)+\mathrm{dist}_E(\tilde b,b'),
\qquad
\mathrm{dist}_E(\tilde b,b')\le \mathrm{dist}_E(\tilde b,b)+\mathrm{dist}_E(b,b').
\]
Subtracting the second from the first gives `\phi_{b'}(b)-\phi_{b'}(\tilde b)\le \mathrm{dist}_E(b,\tilde b)`, and swapping `b,\tilde b` gives the absolute-value bound. The final statement follows because `\phi_{b'}` is integer-valued. ∎

**Definition H.2.3 (Davies weight operator).**  
For `\lambda\in\mathbb R`, define the diagonal multiplication operator
\[
W_{\lambda,b'}:\ell^2(E(\Lambda_L);\mathfrak g)\to\ell^2(E(\Lambda_L);\mathfrak g)
\]
by
\[
(W_{\lambda,b'}X)_b := e^{\lambda\phi_{b'}(b)}\,X_b,
\qquad b\in E(\Lambda_L).
\tag{H.2.2}
\]
Its inverse is the diagonal operator `(W_{\lambda,b'})^{-1}=W_{-\lambda,b'}`.

**Definition H.2.4 (conjugated Maxwell operator).**  
Let `L_{\Lambda_L}=\alpha_W\mathsf M_1` as in Lemma H.1.2. Define the conjugated operator
\[
L_{\Lambda_L,\lambda,b'} := W_{\lambda,b'}\,L_{\Lambda_L}\,W_{\lambda,b'}^{-1}.
\tag{H.2.3}
\]

**Lemma H.2.5 (block entries under conjugation).**  
Let `(L_{\Lambda_L})_{b\tilde b}\in\mathrm{End}(\mathfrak g)` denote the block entries in the link basis. Then
\[
(L_{\Lambda_L,\lambda,b'})_{b\tilde b}
= e^{\lambda(\phi_{b'}(b)-\phi_{b'}(\tilde b))}\,(L_{\Lambda_L})_{b\tilde b}.
\tag{H.2.4}
\]

**Proof.**  
By definition, for any `X`,
\[
(L_{\Lambda_L,\lambda,b'}X)_b
= e^{\lambda\phi_{b'}(b)}\,(L_{\Lambda_L}(W_{-\lambda,b'}X))_b
= e^{\lambda\phi_{b'}(b)}\sum_{\tilde b}(L_{\Lambda_L})_{b\tilde b}\,e^{-\lambda\phi_{b'}(\tilde b)}X_{\tilde b},
\]
which is exactly the block identity (H.2.4). ∎

---

## H.3 Semigroup norm bound under Davies conjugation

The key deterministic input for Davies-type decay is a uniform bound on the operator norm of the conjugated semigroup `e^{-tL_{\Lambda_L,\lambda,b'}}`.

### H.3.1 Symmetric perturbation created by conjugation

**Definition H.3.1 (symmetric perturbation).**  
Define the symmetric perturbation
\[
Q_{\Lambda_L,\lambda,b'}
:= \frac{L_{\Lambda_L,\lambda,b'}+L_{\Lambda_L,-\lambda,b'}}{2}-L_{\Lambda_L}.
\tag{H.3.1}
\]
Since `L_{\Lambda_L,-\lambda,b'}=L_{\Lambda_L,\lambda,b'}^*` (conjugation by a positive diagonal operator), the operator `Q_{\Lambda_L,\lambda,b'}` is self-adjoint.

**Lemma H.3.2 (explicit off-diagonal blocks of the perturbation).**  
For all `b\neq\tilde b`,
\[
(Q_{\Lambda_L,\lambda,b'})_{b\tilde b}
=\big(\cosh(\lambda(\phi_{b'}(b)-\phi_{b'}(\tilde b)))-1\big)\,(L_{\Lambda_L})_{b\tilde b},
\tag{H.3.2}
\]
and `(Q_{\Lambda_L,\lambda,b'})_{bb}=0` for every `b`.

**Proof.**  
Combine (H.2.4) for `\lambda` and `-\lambda` to obtain
\[
\frac{(L_{\Lambda_L,\lambda,b'})_{b\tilde b}+(L_{\Lambda_L,-\lambda,b'})_{b\tilde b}}{2}
=\frac{e^{\lambda\Delta\phi}+e^{-\lambda\Delta\phi}}{2}(L_{\Lambda_L})_{b\tilde b}
=\cosh(\lambda\Delta\phi)\,(L_{\Lambda_L})_{b\tilde b},
\]
where `\Delta\phi:=\phi_{b'}(b)-\phi_{b'}(\tilde b)`. Subtracting `(L_{\Lambda_L})_{b\tilde b}` gives (H.3.2). When `b=\tilde b`, one has `\Delta\phi=0`, so the factor `\cosh(0)-1=0` and hence the diagonal vanishes. ∎

### H.3.2 A norm bound for the symmetric perturbation

**Lemma H.3.3 (norm bound via the boundary row-sum constant).**  
Let `C_\partial(\mathsf M_1)` be the boundary row-sum constant from Definition A.9.4. For every `\lambda\in\mathbb R`, every periodic lattice `\Lambda_L`, and every choice of base link `b'\in E(\Lambda_L)`,
\[
\big\|Q_{\Lambda_L,\lambda,b'}\big\|_{\mathrm{op}}
\le \alpha_W\,C_\partial(\mathsf M_1)\,(\cosh\lambda-1).
\tag{H.3.3}
\]

**Proof.**  
Fix `b'` and write `\phi:=\phi_{b'}` for brevity.

By Lemma B.4.5, `\mathsf M_1` has link-graph interaction range one, hence so does `L_{\Lambda_L}=\alpha_W\mathsf M_1`. Therefore `(L_{\Lambda_L})_{b\tilde b}=0` whenever `\mathrm{dist}_E(b,\tilde b)>1`.

Consider any pair `b\neq\tilde b` such that `(L_{\Lambda_L})_{b\tilde b}\neq 0`. Then `\mathrm{dist}_E(b,\tilde b)=1`. By Lemma H.2.2, `|\phi(b)-\phi(\tilde b)|\in\{0,1\}`. If `|\phi(b)-\phi(\tilde b)|=0`, then the factor in (H.3.2) vanishes. If `|\phi(b)-\phi(\tilde b)|=1`, then
\[
\cosh(\lambda(\phi(b)-\phi(\tilde b)))-1\le \cosh\lambda-1.
\]
Hence, for every `b\neq\tilde b`,
\[
\|(Q_{\Lambda_L,\lambda,b'})_{b\tilde b}\|_{\mathrm{op}}
\le (\cosh\lambda-1)\,\|(L_{\Lambda_L})_{b\tilde b}\|_{\mathrm{op}}\,\mathbf 1_{\{|\phi(b)-\phi(\tilde b)|=1\}}.
\tag{H.3.4}
\]
Summing over `\tilde b\neq b` and taking the supremum in `b`,
\[
\sup_b\sum_{\tilde b\neq b}\|(Q_{\Lambda_L,\lambda,b'})_{b\tilde b}\|_{\mathrm{op}}
\le (\cosh\lambda-1)\sup_b\sum_{\substack{\tilde b\neq b\\|\phi(b)-\phi(\tilde b)|=1}}\|(L_{\Lambda_L})_{b\tilde b}\|_{\mathrm{op}}.
\tag{H.3.5}
\]
By definition, `L_{\Lambda_L}=\alpha_W\mathsf M_1`, so the right-hand side becomes
\[
(\cosh\lambda-1)\,\alpha_W\sup_b\sum_{\substack{\tilde b\neq b\\|\phi(b)-\phi(\tilde b)|=1}}\| (\mathsf M_1)_{b\tilde b}\|_{\mathrm{op}}.
\]
Taking the supremum over the basepoint `b'` yields exactly `\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)` (Definition A.9.4). Since `Q_{\Lambda_L,\lambda,b'}` is self-adjoint and has zero diagonal, its operator norm is bounded by the maximal off-diagonal absolute row sum (Lemma G.2.1, self-adjoint case). Therefore (H.3.3) holds. ∎

### H.3.3 Conjugated semigroup bound

**Lemma H.3.4 (similarity for matrix exponentials; finite-dimensional).**  
Let `A` be a linear operator on a finite-dimensional vector space, and let `W` be invertible. Then for all `t\in\mathbb R`,
\[
\exp\big(t(WAW^{-1})\big)=W\,\exp(tA)\,W^{-1}.
\tag{H.3.6}
\]

**Proof.**  
Use the power series `\exp(tB)=\sum_{k\ge 0} \frac{t^k}{k!}B^k` and note that `(WAW^{-1})^k=WA^kW^{-1}` for every integer `k\ge 0`. ∎

**Proposition H.3.5 (Davies semigroup norm bound).**  
Fix `\Lambda_L`, `b'\in E(\Lambda_L)`, and `\lambda\in\mathbb R`. Let `S_t:=e^{-tL_{\Lambda_L}}` and define the conjugated operator `L_{\Lambda_L,\lambda,b'}` by (H.2.3). Then
\[
W_{\lambda,b'}\,S_t\,W_{\lambda,b'}^{-1} = e^{-tL_{\Lambda_L,\lambda,b'}},
\tag{H.3.7}
\]
and for all `t\ge 0`,
\[
\big\|e^{-tL_{\Lambda_L,\lambda,b'}}\big\|_{\mathrm{op}}
\le \exp\big(t\,\|Q_{\Lambda_L,\lambda,b'}\|_{\mathrm{op}}\big)
\le \exp\big(t\,\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)\big).
\tag{H.3.8}
\]

**Proof.**  
The similarity identity (H.3.7) follows from Lemma H.3.4 applied to `A=-L_{\Lambda_L}` and `W=W_{\lambda,b'}`.

For the norm bound, fix `u_0\in\ell^2(E(\Lambda_L);\mathfrak g)` and set
\[
u(t):=e^{-tL_{\Lambda_L,\lambda,b'}}u_0.
\]
Then `u` solves the linear ODE `\partial_t u(t)=-L_{\Lambda_L,\lambda,b'}u(t)` with `u(0)=u_0`. Differentiate the squared norm:
\[
\frac{d}{dt}\|u(t)\|^2
=2\,\Re\langle u(t),\partial_t u(t)\rangle
=-2\,\Re\langle u(t),L_{\Lambda_L,\lambda,b'}u(t)\rangle.
\tag{H.3.9}
\]
Since `L_{\Lambda_L,-\lambda,b'}=L_{\Lambda_L,\lambda,b'}^*`,
\[
\Re\langle v,L_{\Lambda_L,\lambda,b'}v\rangle
=\Big\langle v,\frac{L_{\Lambda_L,\lambda,b'}+L_{\Lambda_L,-\lambda,b'}}{2}v\Big\rangle
=\langle v,(L_{\Lambda_L}+Q_{\Lambda_L,\lambda,b'})v\rangle
\tag{H.3.10}
\]
by Definition H.3.1. Because `L_{\Lambda_L}\succeq 0` (Lemma B.4.1),
\[
\Re\langle v,L_{\Lambda_L,\lambda,b'}v\rangle
\ge \langle v,Q_{\Lambda_L,\lambda,b'}v\rangle
\ge -\|Q_{\Lambda_L,\lambda,b'}\|_{\mathrm{op}}\,\|v\|^2.
\tag{H.3.11}
\]
Insert (H.3.11) into (H.3.9) to obtain
\[
\frac{d}{dt}\|u(t)\|^2
\le 2\,\|Q_{\Lambda_L,\lambda,b'}\|_{\mathrm{op}}\,\|u(t)\|^2.
\]
Define the scalar function
\[
f(t):=\|u(t)\|^2\ge 0.
\]
Let `q:=\|Q_{\Lambda_L,\lambda,b'}\|_{\mathrm{op}}` and consider
\[
h(t):=e^{-2qt}\,f(t).
\]
Then
\[
h'(t)=e^{-2qt}\,(f'(t)-2qf(t))\le 0.
\]
Therefore `h(t)\le h(0)=f(0)=\|u_0\|^2` for all `t\ge 0`, i.e.
\[
\|u(t)\|^2\le e^{2qt}\,\|u_0\|^2,
\qquad\text{hence}\qquad
\|u(t)\|\le e^{qt}\,\|u_0\|.
\]
Taking the supremum over `u_0\neq 0` gives the first inequality in (H.3.8). The second inequality is Lemma H.3.3. ∎

---

## H.4 Green-kernel decay for the massive Maxwell operator

**Proposition H.4.1 (Davies-type exponential decay of the massive Maxwell inverse kernel).**  
Let `\Lambda_L` be a finite periodic lattice. Let
\[
M_{\Lambda_L}:=m_H^2\,\mathrm{Id}+\alpha_W\,\mathsf M_1
\qquad\text{on }\ell^2(E(\Lambda_L);\mathfrak g)
\]
(Definition A.9.2). Fix a link `b'\in E(\Lambda_L)` and a parameter `\lambda\ge 0` such that
\[
\alpha_W\,C_\partial(\mathsf M_1)\,(\cosh\lambda-1) < m_H^2.
\tag{H.4.1}
\]
Then for every `b\in E(\Lambda_L)`,
\[
\big\|\big(M_{\Lambda_L}^{-1}\big)_{bb'}\big\|_{\mathrm{op}}
\le
\frac{1}{m_H^2-\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)}\,\exp\big(-\lambda\,\mathrm{dist}_E(b,b')\big).
\tag{H.4.2}
\]

**Proof.**  
Start from the Laplace formula (H.1.2):
\[
M_{\Lambda_L}^{-1}=\int_0^{\infty}e^{-m_H^2 t}\,e^{-tL_{\Lambda_L}}\,dt,
\qquad L_{\Lambda_L}:=\alpha_W\mathsf M_1.
\]
Conjugate by `W_{\lambda,b'}`:
\[
W_{\lambda,b'}\,M_{\Lambda_L}^{-1}\,W_{\lambda,b'}^{-1}
=\int_0^{\infty}e^{-m_H^2 t}\,\big(W_{\lambda,b'}e^{-tL_{\Lambda_L}}W_{\lambda,b'}^{-1}\big)\,dt.
\tag{H.4.3}
\]
By Proposition H.3.5, `W_{\lambda,b'}e^{-tL_{\Lambda_L}}W_{\lambda,b'}^{-1}=e^{-tL_{\Lambda_L,\lambda,b'}}`, and
\[
\big\|e^{-tL_{\Lambda_L,\lambda,b'}}\big\|_{\mathrm{op}}
\le \exp\big(t\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)\big).
\]
Taking operator norms in (H.4.3) and using submultiplicativity,
\[
\big\|W_{\lambda,b'}M_{\Lambda_L}^{-1}W_{\lambda,b'}^{-1}\big\|_{\mathrm{op}}
\le
\int_0^{\infty}e^{-m_H^2 t}\,\exp\big(t\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)\big)\,dt.
\tag{H.4.4}
\]
The integral converges if and only if (H.4.1) holds, and in that case
\[
\int_0^{\infty}\exp\big(-t(m_H^2-\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1))\big)\,dt
=
\frac{1}{m_H^2-\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)}.
\tag{H.4.5}
\]
Thus
\[
\big\|W_{\lambda,b'}M_{\Lambda_L}^{-1}W_{\lambda,b'}^{-1}\big\|_{\mathrm{op}}
\le
\frac{1}{m_H^2-\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)}.
\tag{H.4.6}
\]

Now relate this operator norm bound to the single block `(b,b')` of `M_{\Lambda_L}^{-1}`. By definition of `W_{\lambda,b'}` (H.2.2), the block entries satisfy
\[
\big(W_{\lambda,b'}M_{\Lambda_L}^{-1}W_{\lambda,b'}^{-1}\big)_{bb'}
= e^{\lambda(\phi_{b'}(b)-\phi_{b'}(b'))}\,(M_{\Lambda_L}^{-1})_{bb'}.
\]
Since `\phi_{b'}(b')=\mathrm{dist}_E(b',b')=0`, this becomes
\[
(M_{\Lambda_L}^{-1})_{bb'}
= e^{-\lambda\phi_{b'}(b)}\,\big(W_{\lambda,b'}M_{\Lambda_L}^{-1}W_{\lambda,b'}^{-1}\big)_{bb'}.
\tag{H.4.7}
\]
Taking operator norms and using `\|(T)_{bb'}\|_{\mathrm{op}}\le \|T\|_{\mathrm{op}}` for any operator `T`,
\[
\|(M_{\Lambda_L}^{-1})_{bb'}\|_{\mathrm{op}}
\le e^{-\lambda\phi_{b'}(b)}\,\big\|W_{\lambda,b'}M_{\Lambda_L}^{-1}W_{\lambda,b'}^{-1}\big\|_{\mathrm{op}}.
\]
Insert (H.4.6) and use `\phi_{b'}(b)=\mathrm{dist}_E(b,b')` to obtain (H.4.2). ∎

**Proposition H.4.2 (horizontal restriction interface).**  
Let `H^{(0)}:=\ker(d_0^*)\subset\mathcal C^1(\Lambda_L;\mathfrak g)` be the horizontal subspace (Definition B.3.4). Then:

1. (**Invariance**) `H^{(0)}` is invariant under `M_{\Lambda_L}` (Lemma B.4.8).
2. (**Inverse restriction**) The restricted operator `M_{\Lambda_L,H}:=M_{\Lambda_L}|_{H^{(0)}}` is invertible and
   \[
   (M_{\Lambda_L,H})^{-1}=(M_{\Lambda_L}^{-1})|_{H^{(0)}}.
   \tag{H.4.8}
   \]
3. (**Kernel bounds transfer**) For any `b,b'\in E(\Lambda_L)`, the block bound (H.4.2) for `M_{\Lambda_L}^{-1}` applies without change to the action of `(M_{\Lambda_L,H})^{-1}` on horizontal inputs (via the ambient link basis representation).

**Proof.**  
(1) is Lemma B.4.8.

(2) Since `M_{\Lambda_L}\succeq m_H^2\,\mathrm{Id}` (Proposition B.4.7(1)), it is invertible. Invariance implies `M_{\Lambda_L}:H^{(0)}\to H^{(0)}`. For `Y\in H^{(0)}`, the unique solution `X\in\mathcal C^1` of `M_{\Lambda_L}X=Y` must lie in `H^{(0)}` because `M_{\Lambda_L}` restricts to a bijection on `H^{(0)}`. Therefore `X=(M_{\Lambda_L}^{-1})Y` coincides with `(M_{\Lambda_L,H})^{-1}Y`, proving (H.4.8).

(3) follows from (H.4.8): on horizontal inputs the two inverses agree, so any bound on the ambient block kernel yields the same bound for horizontal applications. ∎

**Proposition H.4.3 (canonical exponential bound with prefactor \(2/m_H^2\)).**  
Assume `\alpha_W C_\partial(\mathsf M_1)>0`. Choose `\lambda\ge 0` such that
\[
\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)=\frac{m_H^2}{2}.
\tag{H.4.9}
\]
Equivalently,
\[
\lambda=\operatorname{arcosh}\!\Bigl(1+\frac{m_H^2}{2\alpha_W C_\partial(\mathsf M_1)}\Bigr).
\tag{H.4.10}
\]
Then (H.4.1) holds and Proposition H.4.1 yields, for all `b,b'\in E(\Lambda_L)`,
\[
\big\|\big(M_{\Lambda_L}^{-1}\big)_{bb'}\big\|_{\mathrm{op}}
\le
\frac{2}{m_H^2}\,\exp\big(-\lambda\,\mathrm{dist}_E(b,b')\big).
\tag{H.4.11}
\]

**Proof.**  
Under (H.4.9), one has `m_H^2-\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)=m_H^2/2`, so the prefactor in (H.4.2) becomes `2/m_H^2`. ∎

**Proposition H.4.4 (crude volume-uniform choice using \(C_0(\mathsf M_1)\)).**  
Assume `\alpha_W C_0(\mathsf M_1)>0`. Since `C_\partial(\mathsf M_1)\le C_0(\mathsf M_1)` (Definition A.9.4), the choice of `\lambda` satisfying
\[
\alpha_W C_0(\mathsf M_1)(\cosh\lambda-1)=\frac{m_H^2}{2}
\tag{H.4.12}
\]
implies (H.4.9), hence also (H.4.11). In particular, using Lemma B.4.6 one may replace `C_0(\mathsf M_1)` by the explicit upper bound `3\nu_P`.

**Proof.**  
If (H.4.12) holds, then `\alpha_W C_\partial(\mathsf M_1)(\cosh\lambda-1)\le \alpha_W C_0(\mathsf M_1)(\cosh\lambda-1)=m_H^2/2`, so (H.4.9) holds with `C_\partial` in place of `C_0`. Apply Proposition H.4.3. ∎

---

## H.5 Output summary for downstream use

**Definition H.5.1 (exported statements).**  
Downstream arguments use Appendix H through the following interfaces:
- Lemma H.1.1 (Laplace transform resolvent identity),
- Lemma H.1.2 (specialization of the Laplace identity to the massive Maxwell operator),
- Proposition H.3.5 (conjugated semigroup norm bound),
- Proposition H.4.1 (Davies-type exponential decay bound for `M_{\Lambda_L}^{-1}` blocks),
- Proposition H.4.2 (horizontal restriction interface (H.4.8)).
- Proposition H.4.3 (canonical parameter choice yielding prefactor `2/m_H^2`),
- Proposition H.4.4 (crude volume-uniform parameter choice via `C_0(\mathsf M_1)` and `\nu_P`).
