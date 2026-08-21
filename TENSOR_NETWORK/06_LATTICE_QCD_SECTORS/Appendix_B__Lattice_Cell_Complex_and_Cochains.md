---
file: Appendix_B__Lattice_Cell_Complex_and_Cochains.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
feeds_into:
  - Core-2 (Configuration geometry and differential calculus)
  - Core-4 (Vacuum linearization and the discrete Maxwell structure)
  - Core-5 (Local coercivity / matrix hinge on the canonical good set)
  - Core-7 (Finite-range inverse decay)
---

# Appendix B — Lattice cell complex and cochains

## B.0 Interface and standing conventions

**Definition B.0.1 (scope).**
This appendix provides the discrete cell-complex algebra and the cochain identities needed downstream:
- cochain-complex identity `d_1 d_0 = 0`,
- explicit adjoint formulas for `d_0^*` and `d_1^*` relative to the `\ell^2` inner products,
- the orthogonal splitting `\mathcal C^1 = \mathrm{im}(d_0) \oplus \ker(d_0^*)` and the definition of the horizontal subspace `H^{(0)}:=\ker(d_0^*)`,
- finite-range structure and uniform local (row-sum / degree) bounds for `\mathsf M_1 := d_1^* d_1` and for the massive Maxwell operator `M_{\Lambda_L}`.

**Definition B.0.2 (standing setting).**
Fix a finite periodic lattice `\Lambda_L` as in Definition A.1.3, with cell sets `V(\Lambda_L)`, `E(\Lambda_L)`, `P(\Lambda_L)` as in Definitions A.2.1–A.2.3.  
All cochains, coboundaries, inner products, and adjoints are those of Appendix A, §A.5.

**Definition B.0.3 (dependency discipline).**
All constants referenced in this appendix are taken from Appendix A:
`d` (Definition A.1.1), `m_\partial` (Definition A.2.5), `\nu_P` (Definition A.2.6), `D_E` (Definition A.2.10), `\mathrm{dist}_E` (Definition A.2.9),
`m_H^2` (Definition A.8.3), `\alpha_W` (Definition A.9.1).

---

## B.1 Incidence counting on the hypercubic torus

**Lemma B.1.1 (plaquette incidence count for a fixed link).**
Fix `b=(x,\mu)\in E(\Lambda_L)` (Definition A.2.2) and assume `d=4` (Definition A.1.1).  
Then the number of oriented plaquettes whose boundary contains `b` satisfies
\[
\#\{p\in P(\Lambda_L):\ \sigma_{p,b}\neq 0\}=2(d-1)=6.
\]
In particular, the overlap constant `\nu_P` from Definition A.2.6 satisfies `\nu_P=6` for the periodic hypercubic lattice.

*Proof.*  
Fix `\mu\in\{0,1,2,3\}`. For each `\nu\in\{0,1,2,3\}\setminus\{\mu\}`, there are exactly two elementary plaquettes in the `(\mu,\nu)` coordinate plane that contain the geometric edge from `x` to `x+\hat e_\mu`:
- the plaquette with basepoint `x` and oriented type `(\min\{\mu,\nu\};\max\{\mu,\nu\})`, and
- the plaquette with basepoint `x-\hat e_\nu` and the same oriented type.

Both are well-defined on the periodic lattice because shifts are computed modulo `L` (Definition A.1.4).  
No other plaquette contains the edge `(x,\mu)` since every plaquette is supported on a coordinate 2-plane and must use direction `\mu` together with exactly one other direction `\nu\neq\mu`.  

Hence the number of plaquettes containing `b` equals `2\cdot\#\{\nu\neq\mu\}=2(d-1)`.  
With `d=4`, this equals `6`. Taking the supremum over `b` yields `\nu_P=6` (Definition A.2.6). ∎

**Lemma B.1.2 (adjacency degree bound from incidence counting).**
For each `b\in E(\Lambda_L)`, let
\[
N(b):=\{b'\in E(\Lambda_L):\ b'\neq b,\ b'\sim b\}
\]
be the adjacency neighborhood (Definition A.2.8). Then
\[
\#N(b)\le 3\,\#\{p\in P(\Lambda_L):\ \sigma_{p,b}\neq 0\}.
\]
Consequently, the degree bound `D_E` from Definition A.2.10 satisfies
\[
D_E \le 3\,\nu_P,
\]
and in dimension `d=4` one has `D_E\le 18` using Lemma B.1.1.

*Proof.*  
Fix `b\in E(\Lambda_L)`. Each plaquette `p` with `\sigma_{p,b}\neq 0` has boundary length `m_\partial=4` (Definition A.2.5), hence contains exactly three other links `b'\neq b` with `\sigma_{p,b'}\neq 0`. Therefore the set of ordered pairs
\[
S(b):=\{(p,b'):\ p\in P(\Lambda_L),\ \sigma_{p,b}\neq 0,\ b'\in E(\Lambda_L),\ b'\neq b,\ \sigma_{p,b'}\neq 0\}
\]
has cardinality
\[
\#S(b)=3\,\#\{p\in P(\Lambda_L):\ \sigma_{p,b}\neq 0\}.
\]
The projection map `(p,b')\mapsto b'` has image contained in `N(b)` by Definition A.2.8. Hence
\[
\#N(b)\le \#S(b)=3\,\#\{p\in P(\Lambda_L):\ \sigma_{p,b}\neq 0\}.
\]
Taking the supremum over `b` gives `D_E\le 3\nu_P` (Definitions A.2.6 and A.2.10).  
The `d=4` bound follows from Lemma B.1.1. ∎

---

## B.2 The cochain-complex identity

**Lemma B.2.1 (cochain complex identity).**
With `d_0` and `d_1` as in Definitions A.5.3–A.5.4,
\[
d_1\circ d_0 \equiv 0
\quad\text{as a map }\mathcal C^0(\Lambda_L;\mathfrak g)\to \mathcal C^2(\Lambda_L;\mathfrak g).
\]

*Proof.*  
Fix `\varphi\in\mathcal C^0(\Lambda_L;\mathfrak g)` and a plaquette `p=(x;\mu,\nu)\in P(\Lambda_L)` (Definition A.2.3) with `\mu<\nu`.  
Using Definitions A.5.3–A.5.4 together with the explicit boundary formula in Definition A.2.4,
\[
(d_1 d_0\varphi)_p
= (d_0\varphi)_{x,\mu} + (d_0\varphi)_{x+\hat e_\mu,\nu}
- (d_0\varphi)_{x+\hat e_\nu,\mu} - (d_0\varphi)_{x,\nu}.
\]
Expanding each `d_0\varphi` term gives
\[
\begin{aligned}
(d_1 d_0\varphi)_p
&= (\varphi_{x+\hat e_\mu}-\varphi_x)
+ (\varphi_{x+\hat e_\mu+\hat e_\nu}-\varphi_{x+\hat e_\mu}) \\
&\quad - (\varphi_{x+\hat e_\nu+\hat e_\mu}-\varphi_{x+\hat e_\nu})
- (\varphi_{x+\hat e_\nu}-\varphi_x)
=0,
\end{aligned}
\]
where the cancellation is exact because addition in `\Lambda_L` is commutative (Definition A.1.3).  
Since `p` was arbitrary, `d_1 d_0\equiv 0`. ∎

---

## B.3 Explicit adjoint formulas and horizontal splitting

### B.3.1 The adjoint of `d_0`

**Proposition B.3.1 (explicit formula for `d_0^*`).**
Let `d_0^*` be the `\ell^2`-adjoint from Definition A.5.5.  
Then for every `X\in\mathcal C^1(\Lambda_L;\mathfrak g)` and every vertex `x\in V(\Lambda_L)`,
\[
(d_0^*X)_x
=
\sum_{\mu\in\mathsf I_d}\bigl(X_{x-\hat e_\mu,\mu}-X_{x,\mu}\bigr),
\]
where `x-\hat e_\mu` is the periodic shift (Definition A.1.4).

*Proof.*  
Fix `\varphi\in\mathcal C^0(\Lambda_L;\mathfrak g)` and `X\in\mathcal C^1(\Lambda_L;\mathfrak g)`. By Definitions A.5.2–A.5.3,
\[
\langle d_0\varphi, X\rangle_{\mathcal C^1}
=
\sum_{x\in\Lambda_L}\sum_{\mu\in\mathsf I_d}
\big\langle \varphi_{x+\hat e_\mu}-\varphi_x,\ X_{x,\mu}\big\rangle_{\mathfrak g}.
\]
Split the sum and reindex the first part by the periodic change of variables `y=x+\hat e_\mu`:
\[
\sum_{x,\mu}\langle \varphi_{x+\hat e_\mu},X_{x,\mu}\rangle_{\mathfrak g}
=
\sum_{y,\mu}\langle \varphi_{y},X_{y-\hat e_\mu,\mu}\rangle_{\mathfrak g}.
\]
Therefore
\[
\langle d_0\varphi, X\rangle_{\mathcal C^1}
=
\sum_{x\in\Lambda_L}
\Big\langle
\varphi_x,
\sum_{\mu\in\mathsf I_d}\bigl(X_{x-\hat e_\mu,\mu}-X_{x,\mu}\bigr)
\Big\rangle_{\mathfrak g}.
\]
By the defining identity of the adjoint (Definition A.5.5),
\[
\langle d_0\varphi, X\rangle_{\mathcal C^1}=\langle \varphi,d_0^*X\rangle_{\mathcal C^0}
=
\sum_{x\in\Lambda_L}\langle \varphi_x,(d_0^*X)_x\rangle_{\mathfrak g},
\]
and equality for all `\varphi` implies the claimed pointwise formula for `(d_0^*X)_x`. ∎

### B.3.2 The adjoint of `d_1`

**Proposition B.3.2 (explicit formula for `d_1^*`).**
Let `d_1^*` be the `\ell^2`-adjoint from Definition A.5.5.  
Then for every `F\in\mathcal C^2(\Lambda_L;\mathfrak g)` and every link `b\in E(\Lambda_L)`,
\[
(d_1^*F)_b
=
\sum_{p\in P(\Lambda_L)} \sigma_{p,b}\,F_p,
\]
where `\sigma_{p,b}` are the incidence coefficients from Definition A.2.4.

*Proof.*  
Fix `X\in\mathcal C^1(\Lambda_L;\mathfrak g)` and `F\in\mathcal C^2(\Lambda_L;\mathfrak g)`.  
By Definitions A.5.2 and A.5.4,
\[
\langle d_1X, F\rangle_{\mathcal C^2}
=
\sum_{p\in P(\Lambda_L)}
\Big\langle \sum_{b\in E(\Lambda_L)}\sigma_{p,b}X_b,\ F_p\Big\rangle_{\mathfrak g}
=
\sum_{b\in E(\Lambda_L)}
\Big\langle X_b,\ \sum_{p\in P(\Lambda_L)}\sigma_{p,b}F_p\Big\rangle_{\mathfrak g}.
\]
By the defining identity of the adjoint (Definition A.5.5),
\[
\langle d_1X,F\rangle_{\mathcal C^2}=\langle X,d_1^*F\rangle_{\mathcal C^1}
=
\sum_{b\in E(\Lambda_L)}\langle X_b,(d_1^*F)_b\rangle_{\mathfrak g}.
\]
Equality for all `X` implies the pointwise formula for `(d_1^*F)_b`. ∎

### B.3.3 Horizontal splitting on `\mathcal C^1`

**Lemma B.3.3 (orthogonal splitting by adjoint kernel).**
Let `d_0:\mathcal C^0\to\mathcal C^1` and `d_0^*:\mathcal C^1\to\mathcal C^0` be as in Definitions A.5.3 and A.5.5.  
Then
\[
\mathcal C^1(\Lambda_L;\mathfrak g)
=
\mathrm{im}(d_0)\ \oplus\ \ker(d_0^*),
\]
an orthogonal direct sum with respect to `\langle\cdot,\cdot\rangle_{\mathcal C^1}`.

*Proof.*  
In any finite-dimensional Hilbert space, one has the general identity
\[
\bigl(\mathrm{im}(T)\bigr)^\perp = \ker(T^*)
\]
for a linear map `T` and its adjoint `T^*`. Apply this with `T=d_0`. Then
\[
\bigl(\mathrm{im}(d_0)\bigr)^\perp = \ker(d_0^*).
\]
Finite dimensionality implies `\mathcal C^1 = \mathrm{im}(d_0) \oplus (\mathrm{im}(d_0))^\perp`, and orthogonality yields the claimed decomposition. ∎

**Definition B.3.4 (horizontal subspace at the vacuum).**
Define the horizontal subspace (at the cochain level) by
\[
H^{(0)}:=\ker(d_0^*)\subset \mathcal C^1(\Lambda_L;\mathfrak g).
\]
This is the canonical orthogonal complement of the exact 1-cochains `\mathrm{im}(d_0)` by Lemma B.3.3.

---

## B.4 The Maxwell operator: positivity, invariance, finite range, and row bounds

### B.4.1 Positivity and invariance of `\mathsf M_1=d_1^*d_1`

**Lemma B.4.1 (positivity of `\mathsf M_1`).**
Let `\mathsf M_1:=d_1^*d_1` as in Definition A.5.6. Then for every `X\in\mathcal C^1(\Lambda_L;\mathfrak g)`,
\[
\langle X,\mathsf M_1 X\rangle_{\mathcal C^1} = \langle d_1X,d_1X\rangle_{\mathcal C^2} = |d_1X|_{\mathcal C^2}^2\ \ge\ 0.
\]
In particular, `\mathsf M_1` is self-adjoint and positive semidefinite.

*Proof.*  
By Definition A.5.6, `\mathsf M_1=d_1^*d_1`. Therefore
\[
\langle X,\mathsf M_1 X\rangle_{\mathcal C^1}
=\langle X,d_1^*d_1X\rangle_{\mathcal C^1}
=\langle d_1X,d_1X\rangle_{\mathcal C^2},
\]
using the adjoint identity from Definition A.5.5. Nonnegativity is immediate. Self-adjointness follows from `\mathsf M_1=(\mathsf M_1)^*`. ∎

**Lemma B.4.2 (gauge-exact cochains lie in the kernel of `d_1` and `\mathsf M_1`).**
One has
\[
d_1\bigl(\mathrm{im}(d_0)\bigr)=\{0\},
\qquad
\mathsf M_1\bigl(\mathrm{im}(d_0)\bigr)=\{0\}.
\]

*Proof.*  
The first identity is exactly Lemma B.2.1: for any `\varphi`, `d_1(d_0\varphi)=0`.  
The second follows by applying `d_1^*` to the first: `\mathsf M_1(d_0\varphi)=d_1^*d_1(d_0\varphi)=d_1^*(0)=0`. ∎

**Lemma B.4.3 (invariance of horizontals under `\mathsf M_1`).**
The horizontal subspace `H^{(0)}=\ker(d_0^*)` (Definition B.3.4) is invariant under `\mathsf M_1=d_1^*d_1`, i.e.
\[
\mathsf M_1\bigl(H^{(0)}\bigr)\subset H^{(0)}.
\]

*Proof.*  
Let `X\in H^{(0)}` so `d_0^*X=0`. Then
\[
d_0^*(\mathsf M_1 X)
= d_0^* d_1^* d_1 X.
\]
By Lemma B.2.1, `(d_1 d_0)^*=d_0^* d_1^*=0`. Hence `d_0^* d_1^*=0`, so the right-hand side equals `0`. Therefore `\mathsf M_1 X\in\ker(d_0^*)=H^{(0)}`. ∎

### B.4.2 Matrix-entry representation and finite-range structure

**Lemma B.4.4 (matrix-entry formula for `\mathsf M_1`).**
View `\mathsf M_1` as an operator on `\mathcal C^1(\Lambda_L;\mathfrak g)=\mathfrak g^{E(\Lambda_L)}` with link-index block matrix `\bigl((\mathsf M_1)_{bb'}\bigr)_{b,b'\in E(\Lambda_L)}` and fiber `\mathfrak g`.  
Then for every `b,b'\in E(\Lambda_L)`,
\[
(\mathsf M_1)_{bb'}
=
\Big(\sum_{p\in P(\Lambda_L)} \sigma_{p,b}\,\sigma_{p,b'}\Big)\,\mathrm{Id}_{\mathfrak g}
\ \in\ \mathrm{End}(\mathfrak g).
\]

*Proof.*  
Fix `X\in\mathcal C^1`. By Proposition B.3.2,
\[
(\mathsf M_1 X)_b
=(d_1^*d_1X)_b
= \sum_{p\in P(\Lambda_L)}\sigma_{p,b}\,(d_1X)_p.
\]
By Definition A.5.4,
\[
(d_1X)_p=\sum_{b'\in E(\Lambda_L)}\sigma_{p,b'}X_{b'}.
\]
Substituting yields
\[
(\mathsf M_1 X)_b
= \sum_{b'\in E(\Lambda_L)}
\Big(\sum_{p\in P(\Lambda_L)}\sigma_{p,b}\sigma_{p,b'}\Big) X_{b'}.
\]
Since `\sigma_{p,b}\sigma_{p,b'}` is a scalar and the operator acts componentwise on `\mathfrak g`, the block multiplying `X_{b'}` is the scalar coefficient times `\mathrm{Id}_{\mathfrak g}`. ∎

**Proposition B.4.5 (finite range of `\mathsf M_1` in the link graph).**
Let `\mathrm{dist}_E` be the link graph distance from Definition A.2.9.  
If `\mathrm{dist}_E(b,b')>1`, then
\[
(\mathsf M_1)_{bb'}=0.
\]
Equivalently, `\mathsf M_1` has interaction range one on the link graph.

*Proof.*  
Assume `\mathrm{dist}_E(b,b')>1`. By Definition A.2.9 this means `b` and `b'` are not equal and are not adjacent, i.e. there is **no** plaquette `p` whose boundary contains both `b` and `b'`.  
Therefore `\sigma_{p,b}\sigma_{p,b'}=0` for all `p`.  
By Lemma B.4.4, the coefficient sum is zero, hence `(\mathsf M_1)_{bb'}=0`. ∎

### B.4.3 Uniform row-sum bounds from bounded degree

**Lemma B.4.6 (uniform off-diagonal row-sum bound for `\mathsf M_1`).**
Let `C_0(\mathsf M_1)` be the row-sum constant from Definition A.9.3. Then
\[
C_0(\mathsf M_1)\le 3\,\nu_P.
\]
In particular, in dimension `d=4` one has `C_0(\mathsf M_1)\le 18` using Lemma B.1.1.

*Proof.*  
Fix `b\in E(\Lambda_L)`. By Lemma B.4.4,
\[
(\mathsf M_1)_{bb'}
=
\Big(\sum_{p\in P(\Lambda_L)} \sigma_{p,b}\,\sigma_{p,b'}\Big)\,\mathrm{Id}_{\mathfrak g}
\quad\text{for all }b,b'\in E(\Lambda_L).
\]
Hence for `b'\neq b`,
\[
\bigl\|(\mathsf M_1)_{bb'}\bigr\|_{\mathrm{op}}
=
\Big|\sum_{p\in P(\Lambda_L)}\sigma_{p,b}\sigma_{p,b'}\Big|
\le
\sum_{p\in P(\Lambda_L)} |\sigma_{p,b}\sigma_{p,b'}|.
\]
Summing over `b'\neq b` and exchanging sums gives
\[
\sum_{b'\neq b}\bigl\|(\mathsf M_1)_{bb'}\bigr\|_{\mathrm{op}}
\le
\sum_{p\in P(\Lambda_L)} |\sigma_{p,b}|
\sum_{b'\neq b}|\sigma_{p,b'}|.
\]
For fixed `p`, the boundary of `p` contains exactly `m_\partial=4` links (Definition A.2.5), hence exactly three links distinct from `b`. The incidence coefficients satisfy `|\sigma_{p,b'}|\in\{0,1\}` (Definition A.2.4). Therefore
\[
\sum_{b'\neq b}|\sigma_{p,b'}|=3
\quad\text{whenever }\sigma_{p,b}\neq 0,
\qquad
\sum_{b'\neq b}|\sigma_{p,b'}|=0
\quad\text{whenever }\sigma_{p,b}=0.
\]
It follows that
\[
\sum_{b'\neq b}\bigl\|(\mathsf M_1)_{bb'}\bigr\|_{\mathrm{op}}
\le
3\,\#\{p\in P(\Lambda_L):\ \sigma_{p,b}\neq 0\}
\le 3\,\nu_P,
\]
where the last inequality is Definition A.2.6. Taking the supremum over `b` yields the claim. ∎

**Proposition B.4.7 (finite-range and row-sum bounds for the massive Maxwell operator).**
Let `M_{\Lambda_L}` be the massive Maxwell operator from Definition A.9.2:
\[
M_{\Lambda_L}=m_H^2\,\mathrm{Id}+\alpha_W\,\mathsf M_1.
\]
Then:
1. (**Uniform positivity**) `M_{\Lambda_L}\succeq m_H^2\,\mathrm{Id}` on `\mathcal C^1(\Lambda_L;\mathfrak g)`.
2. (**Finite range**) For `b\neq b'`, if `\mathrm{dist}_E(b,b')>1` then `(M_{\Lambda_L})_{bb'}=0`.
3. (**Uniform off-diagonal row-sum bound**) The off-diagonal row-sum constant satisfies
   \[
   \sup_{b}\sum_{b'\neq b}\|(M_{\Lambda_L})_{bb'}\|_{\mathrm{op}}
   = \alpha_W\, C_0(\mathsf M_1)
   \le \alpha_W\,(3\,\nu_P).
   \]

*Proof.*  
(1) By Lemma B.4.1, `\mathsf M_1\succeq 0`. Hence `M_{\Lambda_L}=m_H^2\,\mathrm{Id}+\alpha_W\,\mathsf M_1\succeq m_H^2\,\mathrm{Id}`.

(2) The mass term is diagonal in the link index, so it contributes no off-diagonal blocks. The off-diagonal blocks of `M_{\Lambda_L}` are those of `\alpha_W\mathsf M_1`. Proposition B.4.5 gives the range-one property for `\mathsf M_1`, hence for `M_{\Lambda_L}`.

(3) For `b'\neq b`, `(M_{\Lambda_L})_{bb'}=\alpha_W(\mathsf M_1)_{bb'}`. Therefore
\[
\sum_{b'\neq b}\|(M_{\Lambda_L})_{bb'}\|_{\mathrm{op}}
=\alpha_W\sum_{b'\neq b}\|(\mathsf M_1)_{bb'}\|_{\mathrm{op}}.
\]
Taking the supremum over `b` and applying Lemma B.4.6 yields the claimed bound. ∎

**Lemma B.4.8 (horizontal invariance for `M_{\Lambda_L}`).**
The horizontal subspace `H^{(0)}=\ker(d_0^*)` (Definition B.3.4) is invariant under `M_{\Lambda_L}`.

*Proof.*  
The mass term `m_H^2\,\mathrm{Id}` preserves every subspace. The Maxwell term `\alpha_W\mathsf M_1` preserves `H^{(0)}` by Lemma B.4.3. ∎

---

## B.5 Output summary for downstream use

**Definition B.5.1 (exported statements).**
Downstream core arguments use Appendix B through the following interfaces:
- Lemma B.2.1 (`d_1 d_0=0`) and Lemma B.4.3 (horizontal invariance),
- Proposition B.3.1 and Proposition B.3.2 (explicit adjoints),
- Lemma B.3.3 and Definition B.3.4 (orthogonal splitting and horizontals),
- Proposition B.4.5 and Proposition B.4.7 (finite range, positivity, and row-sum bounds),
- Lemma B.1.2 (uniform degree bound via `\nu_P` and `D_E`).
