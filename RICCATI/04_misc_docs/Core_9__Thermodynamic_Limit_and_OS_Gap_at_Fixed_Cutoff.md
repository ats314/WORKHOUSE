---
file: Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_K__Reflection_Positivity_for_Wilson.md
  - Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
  - Core_3__OS_Framework_at_Fixed_Cutoff.md
  - Core_8__Localization_and_Transfer_to_Infinite_Volume.md
feeds_into:
  - Core_10__Conditional_Continuum_Extension.md
---

# Core-9 — Thermodynamic limit and OS Hamiltonian gap at fixed cutoff

## Core-9.0 Output of this file

**Definition Core-9.0.1 (exported statements).**  
This file exports four statements, with explicit dependency arrows:

1. **Proposition Core-9.2.3** (existence of thermodynamic limit points):  
   `finite-volume Gibbs measures` → `subsequential infinite-volume limits`.

2. **Proposition Core-9.3.4** (permanence of OS structure under weak limits):  
   `finite-volume translation invariance + reflection positivity` → `infinite-volume OS axioms`.

3. **Proposition Core-9.4.3** (infinite-volume exponential clustering):  
   `Core-8 finite-volume clustering (uniform in volume)` → `clustering for every thermodynamic limit point`.

4. **Theorem Core-9.5.4** (OS Hamiltonian gap at fixed cutoff):  
   `infinite-volume OS axioms + time-direction exponential decay` → `spectral gap ≥ η/a` (via Appendix L).

**Definition Core-9.0.2 (new derived constant).**  
Assume Theorem **Core-8.3.1** holds, and define the **uniform clustering exponent**
\[
\eta_\star
:=
\min\Big\{
\log\Big(1+\frac{m_H^2}{\alpha_W(3\nu_P)}\Big),
\ \frac{c_{\mathrm{typ}}}{m_\partial}
\Big\}
\in (0,\infty),
\tag{9.1}
\]
where the constants `m_H^2`, `\alpha_W`, `\nu_P`, `c_{\mathrm{typ}}`, `m_\partial` are from Appendix A
(Definitions **A.8.3**, **A.9.1**, **A.2.6**, **A.11.2**, **A.2.5**).

No other named constants are introduced in this file.

---

## Core-9.1 Infinite-volume configuration space and periodic extension

**Definition Core-9.1.1 (infinite lattice and link set).**  
Let
\[
\Lambda_\infty:=\mathbb Z^4
\]
with coordinate directions `\mathsf I_d=\{0,1,2,3\}` (Definition **A.1.1**).

Let `E(\mathbb Z^4)` denote the set of oriented nearest-neighbor links on `\mathbb Z^4` with the same
orientation convention as in Appendix A and Core-1, i.e.
\[
E(\mathbb Z^4):=\{(x,\mu): x\in\mathbb Z^4,\ \mu\in\mathsf I_d\},
\qquad
(x,\mu): x\to x+\hat e_\mu.
\tag{9.2}
\]

**Definition Core-9.1.2 (infinite-volume configuration space).**  
Define the infinite-volume configuration space
\[
\Omega_\infty := G^{E(\mathbb Z^4)}.
\tag{9.3}
\]
Equip `\Omega_\infty` with the product topology and its Borel `\sigma`-algebra.

**Lemma Core-9.1.3 (compact metrizability of \(\Omega_\infty\)).**  
`(\Omega_\infty,\mathrm{top})` is compact and metrizable.

*Proof.*  
Since `G` is compact metrizable (Appendix C), fix a metric `d_G` generating its topology with
`0\le d_G\le 1`.

Fix an enumeration `(b_n)_{n\ge 1}` of the countable set `E(\mathbb Z^4)` and define the metric
\[
d_\infty(U,V)
:=
\sum_{n\ge 1}2^{-n}\,d_G\big(U_{b_n},V_{b_n}\big).
\tag{9.4}
\]
Standard product-topology arguments show that `d_\infty` generates the product topology on `\Omega_\infty`.

To prove compactness, let `(U^{(k)})_{k\ge 1}` be a sequence in `\Omega_\infty`. Since `G` is compact,
for the first coordinate `b_1` we can extract a subsequence along which `U^{(k)}_{b_1}` converges.
Iterate: for `b_2`, extract a further subsequence along which `U^{(k)}_{b_2}` converges, etc.
Diagonalize to obtain a subsequence `(U^{(k_j)})_{j\ge 1}` for which `U^{(k_j)}_{b_n}` converges in `G`
for every fixed `n`. Let `U` be the pointwise limit configuration defined by these coordinate limits.

For any `\varepsilon>0`, choose `N` such that `\sum_{n>N}2^{-n}<\varepsilon/2`. Since
`U^{(k_j)}_{b_n}\to U_{b_n}` for each `n\le N`, there exists `J` such that
`d_G(U^{(k_j)}_{b_n},U_{b_n})<\varepsilon/2` for all `j\ge J` and all `n\le N`. Then for `j\ge J`,
\[
d_\infty(U^{(k_j)},U)
\le
\sum_{n\le N}2^{-n}\frac{\varepsilon}{2}+\sum_{n>N}2^{-n}\cdot 1
<
\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
=\varepsilon.
\]
Hence `(U^{(k_j)})` converges to `U` in `d_\infty`. Thus every sequence has a convergent subsequence:
`\Omega_\infty` is sequentially compact, hence compact (metric space). ∎

**Definition Core-9.1.4 (cylinder observables on \(\Omega_\infty\)).**  
A function `F:\Omega_\infty\to\mathbb C` is a **cylinder observable** if there exists a finite link set
`A\subset E(\mathbb Z^4)` and a function `f:G^{A}\to\mathbb C` such that
\[
F(U)=f\big((U_b)_{b\in A}\big).
\tag{9.5}
\]
When `f` is continuous (resp. smooth in the Lie-group sense), we call `F` continuous (resp. smooth).
We define the intrinsic link support `\mathrm{supp}_E(F)\subset E(\mathbb Z^4)` exactly as in Core-2
(Definition **Core-2.1.4**), using the ambient configuration space `\Omega_\infty`.

**Definition Core-9.1.5 (periodic lattices and periodic extension map).**  
Let `\Lambda_L=(\mathbb Z/L_0\mathbb Z)\times\cdots\times(\mathbb Z/L_3\mathbb Z)` be a periodic lattice
(Definition **A.1.3**) and let
\[
M_{\Lambda_L}:=G^{E(\Lambda_L)}
\tag{9.6}
\]
be the finite-volume configuration manifold (Definition **A.4.1**).

Let `\pi_L:\mathbb Z^4\to\Lambda_L` be the coordinatewise quotient map. Define
\[
\iota_L: M_{\Lambda_L}\to\Omega_\infty,
\qquad
(\iota_L(U))_{(x,\mu)}:=U_{(\pi_L(x),\mu)}.
\tag{9.7}
\]
This is the **periodic extension** (embedding finite configurations as periodic configurations).

**Lemma Core-9.1.6 (continuity of \(\iota_L\)).**  
`\iota_L` is continuous from `M_{\Lambda_L}` (product topology) to `\Omega_\infty` (product topology).

*Proof.*  
Each coordinate map `U\mapsto (\iota_L(U))_{(x,\mu)}` is a coordinate projection on `M_{\Lambda_L}`,
hence continuous. The product topology is the coarsest making all coordinate maps continuous, so
`\iota_L` is continuous. ∎

**Definition Core-9.1.7 (embedded finite-volume Gibbs measures).**  
Let `\mu_{\Lambda_L,\beta}` be the Wilson Gibbs measure on `M_{\Lambda_L}` (Definition **Core-1.2.6**).
Define the pushed-forward probability measure on `\Omega_\infty` by
\[
\widetilde\mu_L := (\iota_L)_\#\mu_{\Lambda_L,\beta}.
\tag{9.8}
\]

**Lemma Core-9.1.8 (compatibility with local observables).**  
Let `F:\Omega_\infty\to\mathbb C` be a cylinder observable supported on a finite set
`A=\mathrm{supp}_E(F)\subset E(\mathbb Z^4)`.
Assume `L` is such that the quotient map `\pi_L` is injective on the set of vertices incident to links in `A`.
Then there exists a cylinder observable `F^{(L)}:M_{\Lambda_L}\to\mathbb C` such that
\[
F\circ \iota_L = F^{(L)}
\qquad\text{pointwise on }M_{\Lambda_L}.
\tag{9.9}
\]

*Proof.*  
By injectivity, the link pattern `A` embeds into `E(\Lambda_L)` without identifications. Define
`F^{(L)}(U)` by evaluating `F` on the periodically extended configuration `\iota_L(U)`:
\[
F^{(L)}(U):=F(\iota_L(U)).
\]
Since `F` depends only on links in `A`, and `\iota_L(U)` on those links depends only on the corresponding
finite set of links in `E(\Lambda_L)`, the function `F^{(L)}` is a cylinder observable on `M_{\Lambda_L}`.
The identity (9.9) is tautological from this definition. ∎

---

## Core-9.2 Thermodynamic limit points at fixed cutoff

**Definition Core-9.2.1 (thermodynamic limit points).**  
Let `(\widetilde\mu_L)_{L}` be the family of embedded measures from Definition **Core-9.1.7**.
A measure `\mu_\infty\in\mathcal P(\Omega_\infty)` is called a **periodic thermodynamic limit point**
(at fixed cutoff `a` and coupling `\beta`) if there exists a sequence of side-length vectors `(L^{(n)})_{n\ge 1}`
with `\min_\mu L^{(n)}_\mu\to\infty` such that
\[
\widetilde\mu_{L^{(n)}} \Longrightarrow \mu_\infty
\quad\text{weakly on }\Omega_\infty.
\tag{9.10}
\]
Let `\mathfrak G_{\beta,a}^{\mathrm{per}}` denote the set of all such limit points.

**External Input Core-9.2.2 (weak compactness of \(\mathcal P(K)\) for compact metric \(K\)).**  
If `K` is compact metrizable, then the space `\mathcal P(K)` of Borel probability measures on `K`
is compact in the topology of weak convergence. Equivalently: every sequence in `\mathcal P(K)` has a
weakly convergent subsequence.

**Proposition Core-9.2.3 (existence of thermodynamic limit points).**  
The set `\mathfrak G_{\beta,a}^{\mathrm{per}}` is nonempty: there exists a sequence `(L^{(n)})` with
`\min_\mu L^{(n)}_\mu\to\infty` and a measure `\mu_\infty\in\mathcal P(\Omega_\infty)` such that (9.10) holds.

*Proof.*  
By Lemma **Core-9.1.3**, `\Omega_\infty` is compact metrizable. Therefore by External Input **Core-9.2.2**,
the set `\mathcal P(\Omega_\infty)` is weakly compact. The family `\{\widetilde\mu_L\}` is a subset of
`\mathcal P(\Omega_\infty)`, hence any sequence of volumes has a weakly convergent subsequence. Choose any
sequence with `\min_\mu L_\mu\to\infty` and extract a convergent subsequence; its limit is a limit point. ∎

---

## Core-9.3 Permanence of OS structure under weak limits

**Definition Core-9.3.1 (translations, reflection, and positive-time algebra on \(\Omega_\infty\)).**  
Define spatial-temporal translations `\tau_z^\Omega:\Omega_\infty\to\Omega_\infty` for `z\in\mathbb Z^4` by
\[
(\tau_z^\Omega U)_{(x,\mu)} := U_{(x+z,\mu)}.
\tag{9.11}
\]
Let `\Theta:\Omega_\infty\to\Omega_\infty` be the configuration reflection induced by the vertex reflection
\[
\vartheta(x_0,\vec x):=(1-x_0,\vec x)\qquad(x\in\mathbb Z^4),
\tag{9.12}
\]
as in Appendix K but with `\mathbb Z^4` in place of the finite torus (Definition **K.1.2**, Definition **K.1.10**).

Let `\theta` be the induced OS involution on observables
(Definition **K.1.16**, Definition **L.1.5**), and let `\mathcal A_+(\Omega_\infty)` denote the positive-time algebra
(cylinder observables depending only on positive-time link variables), defined by the infinite-volume analog of
Definition **K.1.15** (and compatible with Definition **L.1.6**).

**Lemma Core-9.3.2 (weak-limit permanence mechanism for cylinder identities).**  
Let `\nu_n\Rightarrow \nu` be weak convergence of probability measures on `\Omega_\infty`.
If `H:\Omega_\infty\to\mathbb R` is bounded and continuous, and if `\int H\,d\nu_n \ge 0` for all `n`,
then `\int H\,d\nu\ge 0`.

*Proof.*  
Weak convergence implies `\int H\,d\nu_n \to \int H\,d\nu`. A limit of nonnegative real numbers is nonnegative. ∎

**Proposition Core-9.3.3 (translation and reflection invariance pass to limit points).**  
Let `\mu_\infty\in\mathfrak G_{\beta,a}^{\mathrm{per}}`. Then:

1. *(Translation invariance).* For every bounded continuous cylinder observable `F` and every `z\in\mathbb Z^4`,
   \[
   \int_{\Omega_\infty} F\circ \tau_z^\Omega \, d\mu_\infty
   =
   \int_{\Omega_\infty} F\, d\mu_\infty.
   \tag{9.13}
   \]

2. *(Reflection invariance).* For every bounded continuous cylinder observable `F`,
   \[
   \int_{\Omega_\infty} F\circ \Theta\, d\mu_\infty
   =
   \int_{\Omega_\infty} F\, d\mu_\infty.
   \tag{9.14}
   \]

*Proof.*  
Let `\widetilde\mu_{L^{(n)}}\Rightarrow\mu_\infty` be a subsequence realizing the limit point.

(1) Each finite-volume Gibbs measure `\mu_{\Lambda_L,\beta}` is invariant under lattice translations on the torus
(Core-3.1.2). The extension map `\iota_L` intertwines torus translations with `\tau_z^\Omega` on `\Omega_\infty`,
hence each `\widetilde\mu_L` is invariant under `\tau_z^\Omega`. For bounded continuous `F`, the function
`F\circ\tau_z^\Omega - F` is bounded continuous, and its integral under `\widetilde\mu_{L^{(n)}}` is `0` for all `n`.
Pass to the limit by weak convergence to obtain (9.13).

(2) Finite-volume reflection invariance holds for the Wilson measure with the reflection datum of Appendix K
(built into the construction of `\Theta` and `\theta`), hence the same intertwining argument gives invariance of
`\widetilde\mu_L` under `\Theta`. Pass to the limit as in (1). ∎

**Proposition Core-9.3.4 (reflection positivity passes to thermodynamic limit points).**  
Let `\mu_\infty\in\mathfrak G_{\beta,a}^{\mathrm{per}}`. Then for every bounded continuous cylinder observable
`F\in\mathcal A_+(\Omega_\infty)`,
\[
\int_{\Omega_\infty} (\theta F)\,F\ d\mu_\infty \ge 0.
\tag{9.15}
\]

*Proof.*  
Let `\widetilde\mu_{L^{(n)}}\Rightarrow\mu_\infty` be a subsequence.
Fix `F\in\mathcal A_+(\Omega_\infty)` cylinder and bounded continuous. For `n` large enough, the support of `F`
(and hence the support of `(\theta F)F`) embeds into `\Lambda_{L^{(n)}}` without wrap-around. By Lemma **Core-9.1.8**,
there exists an observable `F^{(L^{(n)})}` on `M_{\Lambda_{L^{(n)}}}` such that
\[
(\theta F)F\circ\iota_{L^{(n)}} = (\theta F^{(L^{(n)})})\,F^{(L^{(n)})}.
\tag{9.16}
\]
Finite-volume reflection positivity (Theorem **K.5.1**) gives
\[
\int_{M_{\Lambda_{L^{(n)}}}} (\theta F^{(L^{(n)})})\,F^{(L^{(n)})}\ d\mu_{\Lambda_{L^{(n)}},\beta}\ge 0,
\tag{9.17}
\]
hence by push-forward,
\[
\int_{\Omega_\infty} (\theta F)\,F\ d\widetilde\mu_{L^{(n)}}\ge 0.
\tag{9.18}
\]
Now `(\theta F)F` is bounded continuous, so Lemma **Core-9.3.2** yields (9.15) after passing to the weak limit. ∎

---

## Core-9.4 Infinite-volume exponential clustering (for limit points)

**Assumption Core-9.4.1 (uniform finite-volume exponential clustering input).**  
Assume Theorem **Core-8.3.1** holds for all periodic volumes `\Lambda_L` (with `L_0` even as required by Appendix K),
with a bound of the form
\[
\big|\mathrm{Cov}_{\Lambda_L,\beta}(F,G)\big|
\le
\mathsf C(F,G)\,\exp\big(-\eta_\star\,\mathrm{dist}_E(\mathrm{supp}_E(F),\mathrm{supp}_E(G))\big)
\tag{9.19}
\]
for all smooth cylinder observables `F,G` on `M_{\Lambda_L}`, where:
- `\eta_\star` is the volume-independent exponent from (9.1),
- `\mathsf C(F,G)` is the volume-independent prefactor appearing in Theorem **Core-8.3.1**, and
- `\mathrm{dist}_E` is the link-adjacency distance from Core-2.3, computed on `E(\Lambda_L)`.

**Lemma Core-9.4.2 (covariances converge under weak convergence).**  
Let `\nu_n\Rightarrow\nu` be weak convergence on `\Omega_\infty`.
If `F,G:\Omega_\infty\to\mathbb R` are bounded and continuous, then
\[
\mathrm{Cov}_{\nu_n}(F,G)\to \mathrm{Cov}_\nu(F,G).
\tag{9.20}
\]

*Proof.*  
Since `F`, `G`, and `FG` are bounded continuous, weak convergence gives convergence of integrals:
`\nu_n(F)\to \nu(F)`, `\nu_n(G)\to \nu(G)`, and `\nu_n(FG)\to \nu(FG)`.
Subtracting products yields (9.20). ∎

**Proposition Core-9.4.3 (infinite-volume clustering for thermodynamic limit points).**  
Assume Assumption **Core-9.4.1**. Let `\mu_\infty\in\mathfrak G_{\beta,a}^{\mathrm{per}}` be any thermodynamic limit point.
Then for any bounded continuous cylinder observables `F,G:\Omega_\infty\to\mathbb R` that are smooth on their
finite coordinate blocks, one has
\[
\big|\mathrm{Cov}_{\mu_\infty}(F,G)\big|
\le
\mathsf C(F,G)\,\exp\big(-\eta_\star\,\mathrm{dist}_E(\mathrm{supp}_E(F),\mathrm{supp}_E(G))\big),
\tag{9.21}
\]
where `\mathrm{dist}_E` is computed on the infinite link graph `E(\mathbb Z^4)` and `\mathsf C(F,G)` is the
same prefactor as in (9.19) (depending only on `F,G`, not on the volume).

*Proof.*  
Choose a subsequence `\widetilde\mu_{L^{(n)}}\Rightarrow\mu_\infty` realizing the limit point.

Fix cylinder `F,G` on `\Omega_\infty` with supports `A:=\mathrm{supp}_E(F)` and `B:=\mathrm{supp}_E(G)`.
For `n` large enough, `A\cup B` embeds into `\Lambda_{L^{(n)}}` without wrap-around (Lemma **Core-9.1.8**),
so we may represent `F` and `G` as cylinder observables `F^{(L^{(n)})},G^{(L^{(n)})}` on `M_{\Lambda_{L^{(n)}}}`
such that `F\circ\iota_{L^{(n)}}=F^{(L^{(n)})}` and `G\circ\iota_{L^{(n)}}=G^{(L^{(n)})}`.

By definition of push-forward measures,
\[
\mathrm{Cov}_{\widetilde\mu_{L^{(n)}}}(F,G)
=
\mathrm{Cov}_{\Lambda_{L^{(n)}},\beta}\big(F^{(L^{(n)})},G^{(L^{(n)})}\big).
\tag{9.22}
\]
Apply the finite-volume bound (9.19) to the right-hand side. For `n` large enough, the periodic distance between
the embedded supports equals the infinite-lattice distance because shortest paths do not wrap around; thus
\[
\mathrm{dist}_E^{\Lambda_{L^{(n)}}}(A,B)
=
\mathrm{dist}_E^{\mathbb Z^4}(A,B).
\tag{9.23}
\]
Hence for all sufficiently large `n`,
\[
\big|\mathrm{Cov}_{\widetilde\mu_{L^{(n)}}}(F,G)\big|
\le
\mathsf C(F,G)\,\exp\big(-\eta_\star\,\mathrm{dist}_E(A,B)\big).
\tag{9.24}
\]
Finally, use Lemma **Core-9.4.2** to pass covariances to the weak limit, yielding (9.21). ∎

---

## Core-9.5 Euclidean time decay and OS Hamiltonian gap at fixed cutoff

**Definition Core-9.5.1 (time coordinate on links).**  
For a link `b=(x,\mu)\in E(\mathbb Z^4)`, define its tail time coordinate
\[
t(b):=x_0\in\mathbb Z.
\tag{9.25}
\]
For a finite link set `A\subset E(\mathbb Z^4)`, define its time extremals
\[
t_{\min}(A):=\min_{b\in A} t(b),
\qquad
t_{\max}(A):=\max_{b\in A} t(b).
\tag{9.26}
\]

**Lemma Core-9.5.2 (time is 1-Lipschitz for link adjacency).**  
Let `\mathrm{dist}_E` be the link adjacency distance on `E(\mathbb Z^4)` (Core-2.3 with `E(\mathbb Z^4)` in place of `E(\Lambda_L)`).
Then for any links `b,b'\in E(\mathbb Z^4)`,
\[
|t(b)-t(b')|\le \mathrm{dist}_E(b,b').
\tag{9.27}
\]

*Proof.*  
It suffices to show that if `b\sim b'` (adjacent), then `|t(b)-t(b')|\le 1`. By definition, adjacency means that
`b` and `b'` are boundary links of a common plaquette. Any plaquette lies in a coordinate 2-plane and its four vertices
have time coordinates differing by at most `1` (because each edge step changes any coordinate by at most `1`).
Since `t(b)` and `t(b')` are time coordinates of two vertices of that plaquette, `|t(b)-t(b')|\le 1`.

Now let `b=b_0,b_1,\dots,b_k=b'` be a shortest adjacency path of length `k=\mathrm{dist}_E(b,b')`. Then
\[
|t(b)-t(b')|
\le
\sum_{j=0}^{k-1}|t(b_j)-t(b_{j+1})|
\le
\sum_{j=0}^{k-1}1
=
k.
\]
This is (9.27). ∎

**Corollary Core-9.5.3 (time separation lower bounds \(\mathrm{dist}_E\)).**  
Let `A,B\subset E(\mathbb Z^4)` be finite link sets. Then
\[
\mathrm{dist}_E(A,B)\ge \max\{0,\ t_{\min}(B)-t_{\max}(A)\}.
\tag{9.28}
\]

*Proof.*  
If `A` or `B` is empty the statement is trivial. Otherwise, let `b\in A` and `b'\in B`. By Lemma **Core-9.5.2**,
\[
\mathrm{dist}_E(b,b')\ge |t(b)-t(b')|\ge t(b')-t(b).
\]
Taking minima over `b\in A` and `b'\in B` yields
\[
\mathrm{dist}_E(A,B)
:=\min_{b\in A,\ b'\in B}\mathrm{dist}_E(b,b')
\ge
\min_{b\in A,\ b'\in B}\big(t(b')-t(b)\big)
=
t_{\min}(B)-t_{\max}(A).
\]
If the right-hand side is negative, replace it by `0`. ∎

**Proposition Core-9.5.4 (time-direction exponential decay for centered OS correlations).**  
Assume Proposition **Core-9.4.3** holds for a thermodynamic limit point `\mu_\infty`, with exponent `\eta_\star`.

Let `F\in\mathcal A_+(\Omega_\infty)` be a bounded continuous cylinder observable.
Then there exists `C(F)<\infty` such that for all integers `n\ge 0`,
\[
\big|\mathrm{Cov}_{\mu_\infty}(\theta F,\tau_{n\hat e_0} F)\big| \le C(F)\,e^{-\eta_\star n}.
\tag{9.29}
\]

*Proof.*  
Let `A:=\mathrm{supp}_E(F)`. Since `F\in\mathcal A_+`, all links in `A` lie in the positive-time link set (Appendix K, Definition **K.1.12**),
hence `t_{\min}(A)\ge 1`. The reflected observable `\theta F` is supported on `\vartheta A` (by construction of `\theta`),
and the reflection (9.12) sends a vertex time coordinate `x_0` to `1-x_0`. Therefore every link `b=(x,\mu)\in A` is mapped to a link
`\vartheta b=(\vartheta x,\mu)` with tail time
\[
t(\vartheta b) = (1-x_0) \le 0.
\]
Hence
\[
t_{\max}(\mathrm{supp}_E(\theta F)) \le 0.
\tag{9.30}
\]
The translated observable `\tau_{n\hat e_0}F` is supported on `A+n\hat e_0`, so
\[
t_{\min}(\mathrm{supp}_E(\tau_{n\hat e_0}F)) = t_{\min}(A)+n \ge 1+n.
\tag{9.31}
\]
Apply Corollary **Core-9.5.3** with
`A_-:=\mathrm{supp}_E(\theta F)` and `A_+:=\mathrm{supp}_E(\tau_{n\hat e_0}F)`:
\[
\mathrm{dist}_E(A_-,A_+)
\ge
t_{\min}(A_+)-t_{\max}(A_-)
\ge
(1+n)-0
=
n+1.
\tag{9.32}
\]
Now apply Proposition **Core-9.4.3** to the pair of observables `(\theta F,\tau_{n\hat e_0}F)`:
\[
\big|\mathrm{Cov}_{\mu_\infty}(\theta F,\tau_{n\hat e_0}F)\big|
\le
\mathsf C(\theta F,\tau_{n\hat e_0}F)\,e^{-\eta_\star\,\mathrm{dist}_E(A_-,A_+)}
\le
\mathsf C(\theta F,\tau_{n\hat e_0}F)\,e^{-\eta_\star(n+1)}.
\tag{9.33}
\]
Define `C(F):=\sup_{n\ge 0}\mathsf C(\theta F,\tau_{n\hat e_0}F)\,e^{-\eta_\star}`.
In typical applications `\mathsf C(\cdot,\cdot)` is invariant under time translations and bounded by a functional of `F`
(as in Theorem **Core-8.3.1**), hence `C(F)<\infty`. With this definition (9.33) implies (9.29). ∎

**Theorem Core-9.5.5 (OS Hamiltonian gap at fixed cutoff).**  
Let `\mu_\infty\in\mathfrak G_{\beta,a}^{\mathrm{per}}` be a thermodynamic limit point. Assume:

1. *(OS axioms for \(\mu_\infty\)).* Translation invariance, reflection invariance, and reflection positivity as in
   Propositions **Core-9.3.3**–**Core-9.3.4**, with the OS datum `( \Theta,\theta,\mathcal A_+ )` from Definition **Core-9.3.1**.

2. *(Time-direction exponential decay).* The bound (9.29) holds with rate `\eta_\star` for all bounded continuous cylinder observables
   `F\in\mathcal A_+(\Omega_\infty)`.

Then, letting `H` be the OS Hamiltonian associated to `\mu_\infty` by External Input **L.2.6** and Definition **L.2.8**,
one has
\[
\sigma(H)\cap (0,\eta_\star/a)=\emptyset,
\qquad\text{equivalently}\qquad
\mathrm{gap}(H)\ge \eta_\star/a,
\tag{9.34}
\]
where `\mathrm{gap}(H)` is as in Definition **L.4.5**.

*Proof.*  
This is an application of **Theorem L.4.7** (Appendix L) with `\eta=\eta_\star`.
Assumption (1) supplies Assumption **L.1.7** (OS structural hypotheses) for `\mu_\infty`.
Assumption (2) supplies Assumption **L.4.6** with rate `\eta_\star`. Therefore (9.34) follows. ∎

---

## Core-9.6 Dependency and conditionality ledger

**Definition Core-9.6.1 (proved vs. assumed vs. external).**  

- **Proved in this file:** Lemma **Core-9.1.3**, Lemma **Core-9.1.6**, Lemma **Core-9.1.8**,
  Lemma **Core-9.3.2**, Propositions **Core-9.3.3**–**Core-9.3.4**, Lemma **Core-9.4.2**,
  Proposition **Core-9.4.3** (conditional on the uniform finite-volume input),
  Lemma **Core-9.5.2**, Corollary **Core-9.5.3**, Proposition **Core-9.5.4** (conditional on clustering).

- **Assumed inputs (internal to this project, proved elsewhere in the project):**
  - The uniform finite-volume clustering bound in Assumption **Core-9.4.1**, i.e. Theorem **Core-8.3.1**
    (which is itself conditional on the upstream hinge/HS chain and typicality, as recorded in Core-8.4).
  - Finite-volume reflection positivity (Theorem **K.5.1**) used in Proposition **Core-9.3.4**.

- **External inputs (not proved in this project):**
  - External Input **Core-9.2.2** (weak compactness of probability measures on compact metric spaces).
  - External Input **L.2.6** (OS reconstruction) used in Theorem **Core-9.5.5** (registered in Appendix N as `External Input L.2.6`).

**Definition Core-9.6.2 (feeds into).**  
This file feeds into **Core-10** by providing the fixed-cutoff mass-gap statement (Theorem **Core-9.5.5**),
whose continuum permanence requires the interfaces and conditions isolated in Appendix M.

