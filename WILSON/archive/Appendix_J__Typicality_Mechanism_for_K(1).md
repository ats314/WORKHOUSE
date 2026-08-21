---
file: Appendix_J__Typicality_Mechanism_for_K.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_C__Configuration_Geometry.md
feeds_into:
  - Core-7 (Fixed-cutoff exponential clustering: conditional ⇒ unconditional via Appendix I)
  - Core-8 (Thermodynamic limit at fixed cutoff: localization error control)
---

# Appendix J — Typicality mechanism for the canonical good set `K_{\Lambda_L}`

## J.0 Scope and outputs

**Definition J.0.1 (scope).**  
This appendix supplies a self-contained, finite-volume *volume-scale* probability bound of the form
\[
\mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)\ \le\ \exp\!\big(-c_{\mathrm{typ}}\,|P(\Lambda_L)|\big),
\tag{J.1}
\]
for an explicit canonical choice of measurable events `K_{\Lambda_L}\subset M_{\Lambda_L}`.  
No conditional covariance/Helffer–Sjöstrand input is used here; the argument depends only on:
- the Wilson action `S_{\Lambda_L,\beta}` (Definitions A.6.2–A.6.3),
- the product Riemannian volume `\mathrm{vol}_{g_{\Lambda_L}}` (Definition A.6.5),
- elementary geometric inequalities on a compact Riemannian Lie group (Appendix C),
- the hypercubic cell counts in dimension `d=4` (Appendix B).

**Definition J.0.2 (main output).**  
The main output is Theorem J.4.1, which provides an explicit sufficient condition ensuring (J.1) with a computable exponent `c_{\mathrm{typ}}>0`.

**Definition J.0.3 (no hidden constants).**  
All constants introduced in this appendix are explicitly named at first appearance and are not redefined later.

---

## J.1 A canonical good-set family based on the average plaquette potential

Throughout, fix `d=4` and the periodic lattice `\Lambda_L=(\mathbb Z/L\mathbb Z)^4` (Definition A.2.1). All objects below are for this `\Lambda_L`.

### J.1.1 The plaquette potential without the coupling

**Definition J.1.1 (normalized plaquette potential).**  
Define the *normalized* single-plaquette potential
\[
\vartheta: G\to[0,\infty),
\qquad
\vartheta(V):= 1-\frac{1}{n}\Re\mathrm{Tr}(V),
\tag{J.2}
\]
so that the Wilson single-plaquette potential from Definition A.6.2 is
\[
\Phi_\beta(V)=\beta\,\vartheta(V).
\tag{J.3}
\]

**Lemma J.1.2 (basic bounds for `\vartheta`).**  
For all `V\in G`,
\[
0\le \vartheta(V)\le 2.
\tag{J.4}
\]

*Proof.* Since `V` is unitary in the fixed representation, `\Re\mathrm{Tr}(V)\in[-n,n]`. Substitute into (J.2). ∎

### J.1.2 Average plaquette potential and the canonical event

**Definition J.1.3 (average plaquette potential).**  
Define the average plaquette potential
\[
\overline{\vartheta}_{\Lambda_L}(U)
:=
\frac{1}{|P(\Lambda_L)|}\sum_{p\in P(\Lambda_L)}\vartheta\!\big(U_p(U)\big),
\qquad U\in M_{\Lambda_L},
\tag{J.5}
\]
where `U_p(U)` is the plaquette holonomy (Definition A.6.1).

**Lemma J.1.4 (relation to the Wilson action).**  
For all `U\in M_{\Lambda_L}`,
\[
S_{\Lambda_L,\beta}(U)=\beta\,|P(\Lambda_L)|\,\overline{\vartheta}_{\Lambda_L}(U).
\tag{J.6}
\]

*Proof.* Combine Definition A.6.3 with (J.3)–(J.5). ∎

**Definition J.1.5 (canonical good set).**  
Fix a threshold parameter `\varepsilon\in(0,2)`. Define
\[
K_{\Lambda_L}(\varepsilon)
:=
\Bigl\{U\in M_{\Lambda_L}:\ \overline{\vartheta}_{\Lambda_L}(U)\le \varepsilon\Bigr\}.
\tag{J.7}
\]
Equivalently, by Lemma J.1.4,
\[
K_{\Lambda_L}(\varepsilon)
=
\Bigl\{U\in M_{\Lambda_L}:\ S_{\Lambda_L,\beta}(U)\le \beta\varepsilon\,|P(\Lambda_L)|\Bigr\}.
\tag{J.8}
\]

---

## J.2 A partition-function lower bound from a linkwise ball event

This section constructs a nontrivial lower bound on the partition function `Z_{\Lambda_L,\beta}` (Definition A.6.5) by restricting the integral to a linkwise neighborhood of the vacuum configuration (Definition A.6.4).

### J.2.1 The linkwise ball event and its volume

**Definition J.2.1 (group ball and linkwise ball event).**  
For `r>0`, write
\[
B_r^G(\mathbf 1):=\bigl\{V\in G:\ d_G(V,\mathbf 1)<r\bigr\}
\tag{J.9}
\]
for the Riemannian ball in `(G,g_G)` centered at the identity (Definition A.3.6).  
Define the *linkwise ball event*
\[
A_{\Lambda_L}(r)
:=
\bigl\{U\in M_{\Lambda_L}:\ U_b\in B_r^G(\mathbf 1)\ \text{for every }b\in E(\Lambda_L)\bigr\}.
\tag{J.10}
\]

**Definition J.2.2 (ball-volume deficit constant).**  
Define
\[
\chi_G(r)
:=
\log\Bigl(\frac{\mathrm{vol}_{g_G}(G)}{\mathrm{vol}_{g_G}(B_r^G(\mathbf 1))}\Bigr)\ \in\ [0,\infty),
\tag{J.11}
\]
where `\mathrm{vol}_{g_G}` is the Riemannian volume measure on `(G,g_G)`.

**Lemma J.2.3 (volume of `A_{\Lambda_L}(r)`).**  
For every `r>0`,
\[
\mathrm{vol}_{g_{\Lambda_L}}\big(A_{\Lambda_L}(r)\big)
=
\Bigl(\mathrm{vol}_{g_G}(B_r^G(\mathbf 1))\Bigr)^{|E(\Lambda_L)|}.
\tag{J.12}
\]

*Proof.* By Definition A.4.2, `g_{\Lambda_L}` is the product metric on `G^{E(\Lambda_L)}` and therefore `\mathrm{vol}_{g_{\Lambda_L}}` is the product of `|E(\Lambda_L)|` copies of `\mathrm{vol}_{g_G}` (Appendix C, Proposition C.2.2). The set `A_{\Lambda_L}(r)` is a product set: one copy of `B_r^G(\mathbf 1)` per link. ∎

### J.2.2 Plaquette holonomy displacement on the linkwise ball event

The next lemma uses only left-translation invariance of the metric and the triangle inequality.

**Lemma J.2.4 (subadditivity of distance under multiplication).**  
Let `(G,g_G)` be a Lie group equipped with a left-invariant Riemannian metric. Then for all `V,W\in G`,
\[
d_G(VW,\mathbf 1)\ \le\ d_G(V,\mathbf 1)+d_G(W,\mathbf 1).
\tag{J.13}
\]

*Proof.* Fix `\delta>0` and choose piecewise `C^1` paths `\gamma_V:[0,1]\to G` and `\gamma_W:[0,1]\to G` such that `\gamma_V(0)=\gamma_W(0)=\mathbf 1`, `\gamma_V(1)=V`, `\gamma_W(1)=W`, and
\[
\mathrm{Len}(\gamma_V)\le d_G(V,\mathbf 1)+\delta,
\qquad
\mathrm{Len}(\gamma_W)\le d_G(W,\mathbf 1)+\delta.
\]
Define the concatenated path `\Gamma:[0,2]\to G` by
\[
\Gamma(t):=
\begin{cases}
\gamma_V(t), & t\in[0,1],\\[2pt]
V\,\gamma_W(t-1), & t\in[1,2].
\end{cases}
\]
Left translation by `V` is an isometry for a left-invariant metric, hence
\[
\mathrm{Len}\big(t\mapsto V\gamma_W(t)\big)=\mathrm{Len}(\gamma_W).
\]
Therefore `\mathrm{Len}(\Gamma)\le d_G(V,\mathbf 1)+d_G(W,\mathbf 1)+2\delta`, and since `\Gamma(0)=\mathbf 1` and `\Gamma(2)=VW`, the definition of distance gives
\[
d_G(VW,\mathbf 1)\le d_G(V,\mathbf 1)+d_G(W,\mathbf 1)+2\delta.
\]
Letting `\delta\downarrow 0` yields (J.13). ∎

**Lemma J.2.5 (plaquette holonomy stays close to `\mathbf 1` on `A_{\Lambda_L}(r)`).**  
Let `m_\partial` denote the plaquette boundary length constant from Definition A.2.5 (for the hypercubic lattice, `m_\partial=4`).  
If `U\in A_{\Lambda_L}(r)`, then for every plaquette `p\in P(\Lambda_L)`,
\[
d_G\big(U_p(U),\mathbf 1\big)\ \le\ m_\partial\,r.
\tag{J.14}
\]

*Proof.* Each plaquette holonomy is a product of exactly `m_\partial` link variables and/or inverses (Definition A.6.1 and the orientation conventions in Appendix B).  
Because the metric is bi-invariant (Definition A.3.6), inversion is an isometry, hence `d_G(V^{-1},\mathbf 1)=d_G(V,\mathbf 1)` for all `V\in G`.  
Apply Lemma J.2.4 iteratively to the `m_\partial` factors in `U_p(U)` and use the defining property (J.10) of `A_{\Lambda_L}(r)`. ∎

### J.2.3 A Lipschitz constant for `\vartheta`

**Definition J.2.6 (global Lipschitz constant for `\vartheta`).**  
Define the constant
\[
L_{\vartheta}
:=
\sup_{V\in G}\ |\nabla \vartheta(V)|_{g_G}\ \in\ [0,\infty),
\tag{J.15}
\]
where `\nabla` is the Riemannian gradient on `(G,g_G)`.

**Lemma J.2.7 (Lipschitz bound in terms of distance).**  
For all `V\in G`,
\[
\vartheta(V)\ \le\ L_{\vartheta}\,d_G(V,\mathbf 1).
\tag{J.16}
\]

*Proof.* Since `G` is compact and `\vartheta` is smooth, `L_{\vartheta}<\infty`.  
Let `\gamma:[0,1]\to G` be a minimizing geodesic from `\mathbf 1` to `V` (existence holds on compact manifolds). Then
\[
\vartheta(V)-\vartheta(\mathbf 1)=\int_0^1 \langle \nabla\vartheta(\gamma(t)),\dot\gamma(t)\rangle_{g_G}\,dt
\le \int_0^1 |\nabla\vartheta(\gamma(t))|_{g_G}\,|\dot\gamma(t)|_{g_G}\,dt
\le L_{\vartheta}\,\mathrm{Len}(\gamma).
\]
Since `\vartheta(\mathbf 1)=0` and `\mathrm{Len}(\gamma)=d_G(V,\mathbf 1)`, (J.16) follows. ∎

### J.2.4 Action bound on `A_{\Lambda_L}(r)`

**Proposition J.2.8 (uniform action bound on `A_{\Lambda_L}(r)`).**  
For every `r>0` and every `U\in A_{\Lambda_L}(r)`,
\[
S_{\Lambda_L,\beta}(U)\ \le\ \beta\,L_{\vartheta}\,m_\partial\,r\ |P(\Lambda_L)|.
\tag{J.17}
\]

*Proof.* By Definition A.6.3 and (J.3),
\[
S_{\Lambda_L,\beta}(U)=\beta\sum_{p\in P(\Lambda_L)}\vartheta\big(U_p(U)\big).
\]
By Lemma J.2.7 and Lemma J.2.5,
\[
\vartheta\big(U_p(U)\big)\le L_{\vartheta}\,d_G\big(U_p(U),\mathbf 1\big)\le L_{\vartheta}\,m_\partial\,r,
\]
uniformly in `p`. Summing over `|P(\Lambda_L)|` plaquettes yields (J.17). ∎

**Proposition J.2.9 (partition function lower bound).**  
For every `r>0`,
\[
Z_{\Lambda_L,\beta}
\ge
\exp\!\bigl(-\beta\,L_{\vartheta}\,m_\partial\,r\ |P(\Lambda_L)|\bigr)\,
\Bigl(\mathrm{vol}_{g_G}(B_r^G(\mathbf 1))\Bigr)^{|E(\Lambda_L)|}.
\tag{J.18}
\]

*Proof.* By Definition A.6.5 and Proposition J.2.8,
\[
Z_{\Lambda_L,\beta}
=\int_{M_{\Lambda_L}} e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(dU)
\ge
\int_{A_{\Lambda_L}(r)} e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(dU)
\ge
e^{-\beta L_{\vartheta}m_\partial r |P(\Lambda_L)|}\,\mathrm{vol}_{g_{\Lambda_L}}\big(A_{\Lambda_L}(r)\big).
\]
Apply Lemma J.2.3 to evaluate the last factor. ∎

---

## J.3 A tail bound for `K_{\Lambda_L}(\varepsilon)^c` in terms of `Z_{\Lambda_L,\beta}`

**Lemma J.3.1 (high-average tail bound by a single exponential factor).**  
Let `\varepsilon\in(0,2)` and define `K_{\Lambda_L}(\varepsilon)` by (J.7). Then
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
\exp\!\bigl(-\beta\varepsilon\,|P(\Lambda_L)|\bigr)\,
\frac{\mathrm{vol}_{g_{\Lambda_L}}(M_{\Lambda_L})}{Z_{\Lambda_L,\beta}}.
\tag{J.19}
\]

*Proof.* By Definition A.6.5,
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
=
Z_{\Lambda_L,\beta}^{-1}
\int_{K_{\Lambda_L}(\varepsilon)^c} e^{-S_{\Lambda_L,\beta}(U)}\,\mathrm{vol}_{g_{\Lambda_L}}(dU).
\]
On `K_{\Lambda_L}(\varepsilon)^c`, Lemma J.1.4 gives `S_{\Lambda_L,\beta}(U)>\beta\varepsilon|P(\Lambda_L)|`, hence
\[
e^{-S_{\Lambda_L,\beta}(U)}\le e^{-\beta\varepsilon|P(\Lambda_L)|}.
\]
Therefore,
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
Z_{\Lambda_L,\beta}^{-1} e^{-\beta\varepsilon|P(\Lambda_L)|}\,
\mathrm{vol}_{g_{\Lambda_L}}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
Z_{\Lambda_L,\beta}^{-1} e^{-\beta\varepsilon|P(\Lambda_L)|}\,
\mathrm{vol}_{g_{\Lambda_L}}(M_{\Lambda_L}).
\]
This is (J.19). ∎

**Lemma J.3.2 (total configuration volume).**  
\[
\mathrm{vol}_{g_{\Lambda_L}}(M_{\Lambda_L})
=
\bigl(\mathrm{vol}_{g_G}(G)\bigr)^{|E(\Lambda_L)|}.
\tag{J.20}
\]

*Proof.* Same product-volume argument as in Lemma J.2.3, now using the full group `G` on each link. ∎

**Proposition J.3.3 (explicit tail bound for `K_{\Lambda_L}(\varepsilon)^c`).**  
Fix `\varepsilon\in(0,2)` and choose `r>0`. Then
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
\exp\!\Bigl(
-\beta\bigl(\varepsilon-L_{\vartheta}m_\partial r\bigr)\,|P(\Lambda_L)|
+
|E(\Lambda_L)|\,\chi_G(r)
\Bigr),
\tag{J.21}
\]
where `\chi_G(r)` is defined in (J.11).

*Proof.* Combine Lemma J.3.1 with Lemma J.3.2 and Proposition J.2.9:
\[
\frac{\mathrm{vol}_{g_{\Lambda_L}}(M_{\Lambda_L})}{Z_{\Lambda_L,\beta}}
\le
\exp\!\bigl(\beta L_{\vartheta}m_\partial r |P(\Lambda_L)|\bigr)\,
\Bigl(\frac{\mathrm{vol}_{g_G}(G)}{\mathrm{vol}_{g_G}(B_r^G(\mathbf 1))}\Bigr)^{|E(\Lambda_L)|}
=
\exp\!\bigl(\beta L_{\vartheta}m_\partial r |P(\Lambda_L)|+|E(\Lambda_L)|\chi_G(r)\bigr).
\]
Insert into (J.19) and simplify. ∎

---

## J.4 Volume-scale typicality in `d=4`

To obtain (J.1), we reduce the mixed `|P|`/`|E|` bound (J.21) to a pure `|P|` exponent using the hypercubic cell counts.

**Lemma J.4.1 (hypercubic counts on `(\mathbb Z/L\mathbb Z)^d`).**  
Let `\Lambda_L=(\mathbb Z/L\mathbb Z)^d` with its oriented nearest-neighbor cell structure. Then
\[
|V(\Lambda_L)|=L^d,\qquad
|E(\Lambda_L)|=d\,L^d,\qquad
|P(\Lambda_L)|=\binom{d}{2}L^d.
\tag{J.22}
\]

*Proof.* Each vertex is a residue class in `(\mathbb Z/L\mathbb Z)^d`, hence `L^d` vertices.  
Each vertex has exactly `d` positively oriented outgoing links (one in each coordinate direction), and each such oriented link is uniquely determined by its starting vertex and direction, giving `dL^d` oriented links.  
Each vertex supports exactly `\binom{d}{2}` positively oriented plaquettes `(x;\mu,\nu)` with `\mu<\nu`, and each such plaquette is uniquely determined by its basepoint and ordered pair of directions, giving `\binom{d}{2}L^d`. ∎

**Definition J.4.2 (edge-to-plaquette ratio constant in `d=4`).**  
In dimension `d=4`, define
\[
c_{E:P}:=\frac{|E(\Lambda_L)|}{|P(\Lambda_L)|}=\frac{4}{\binom{4}{2}}=\frac{2}{3}.
\tag{J.23}
\]
By Lemma J.4.1, this value is independent of `L`.

**Theorem J.4.3 (volume-scale typicality for `K_{\Lambda_L}(\varepsilon)`).**  
Fix `\varepsilon\in(0,2)` and choose `r>0` such that
\[
\varepsilon>L_{\vartheta}m_\partial r.
\tag{J.24}
\]
Define
\[
c_{\mathrm{typ}}(\beta;\varepsilon,r)
:=
\beta\bigl(\varepsilon-L_{\vartheta}m_\partial r\bigr)\ -\ c_{E:P}\,\chi_G(r),
\tag{J.25}
\]
with `c_{E:P}=2/3` and `\chi_G(r)` from (J.11).  
If `c_{\mathrm{typ}}(\beta;\varepsilon,r)>0`, then for every `L\ge 1`,
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
\exp\!\bigl(-c_{\mathrm{typ}}(\beta;\varepsilon,r)\,|P(\Lambda_L)|\bigr).
\tag{J.26}
\]

*Proof.* Proposition J.3.3 gives (J.21). In `d=4`, Lemma J.4.1 implies `|E(\Lambda_L)|=c_{E:P}\,|P(\Lambda_L)|`. Substitute into (J.21) to obtain
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
\exp\!\Bigl(-\Bigl[\beta(\varepsilon-L_{\vartheta}m_\partial r)-c_{E:P}\chi_G(r)\Bigr]|P(\Lambda_L)|\Bigr),
\]
which is exactly (J.26). ∎

**Corollary J.4.4 (a convenient sufficient condition in terms of `\beta`).**  
Fix `\varepsilon\in(0,2)` and choose `r>0` satisfying (J.24).  
If
\[
\beta\ \ge\ \frac{2\,c_{E:P}\,\chi_G(r)}{\varepsilon-L_{\vartheta}m_\partial r},
\tag{J.27}
\]
then `c_{\mathrm{typ}}(\beta;\varepsilon,r)\ge \frac{1}{2}\beta(\varepsilon-L_{\vartheta}m_\partial r)>0`, and hence (J.26) holds with
\[
\mu_{\Lambda_L,\beta}\big(K_{\Lambda_L}(\varepsilon)^c\big)
\le
\exp\!\Bigl(-\tfrac12\beta(\varepsilon-L_{\vartheta}m_\partial r)\,|P(\Lambda_L)|\Bigr).
\tag{J.28}
\]

*Proof.* This is immediate from (J.25)–(J.26). ∎

---

## J.5 Interface statement for the Core Manuscript

**Definition J.5.1 (how this feeds into localization).**  
In the Core Manuscript, one sets `K_{\Lambda_L}:=K_{\Lambda_L}(\varepsilon)` (Definition J.1.5) for a fixed admissible `\varepsilon`, and chooses an auxiliary radius `r` satisfying (J.24) such that `c_{\mathrm{typ}}(\beta;\varepsilon,r)>0` (Definition J.4.2 and Theorem J.4.3).  
Then the error term appearing in the covariance decomposition (Appendix I, Proposition I.3.2) obeys the volume-scale bound (J.26), which vanishes as `L\to\infty` and is uniform in the observables.

**Definition J.5.2 (relation to Appendix A typicality placeholders).**  
Theorem J.4.3 provides an explicit sufficient condition under which Assumption A.11.2 holds, with the identification
\[
K_{\Lambda_L}=K_{\Lambda_L}(\varepsilon),
\qquad
c_{\mathrm{typ}}=c_{\mathrm{typ}}(\beta;\varepsilon,r).
\tag{J.29}
\]
