# Lemma Q — Local SU(2) Rare-Source Factorization

**Project:** PMBSF projected-capacity / SU(2) Wilson transfer  
**Updated:** 2026-05-25  
**Status:** Precise analytic target with proved downstream implications. Lemma Q itself remains an open SU(2) probability theorem. The current numerical stack has two anchors: exact heat-bath side-8 as the primary conditional-sampling result, and Stage B side-10/core-margin-3 as the geometry-robustness supplement.

---

## 0. Executive statement

The remaining SU(2) probability input can be isolated as a local conditional rare-source theorem.

After freezing the exterior of a Balaban block, smooth high-plaquette sources inside a shaved core should retain one factor of their global intensity \(q_\eta\) per marked source:

\[
\boxed{
\mathbb E\!\left[
\prod_{p\in B}X_{p,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}.
}
\tag{Q}
\]

The rooted version is:

\[
\boxed{
\mathbb E\!\left[
Y_{p_0}\prod_{p\in B}X_{p,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}
\mathbb E\!\left[
Y_{p_0}
\;\middle|\;
\mathcal F_{C^c}
\right],
}
\tag{Q-root}
\]

for every local root \(0\le Y_{p_0}\le X_{p_0,\eta}\).

This is the missing “rare-source probability half” needed to turn Bałaban/Dimock geometric polymer locality into the PMBSF \(q_\eta\)-per-source cumulant theorem.

---

## 1. Setup

Let \(T_L^4=(\mathbb Z/L\mathbb Z)^4\). Let \(\mu_{L,\beta}\) be the finite-volume pure SU(2) Wilson measure

\[
\mu_{L,\beta}(dU)
=
Z_{L,\beta}^{-1}
\exp\left\{
\frac{\beta}{2}\sum_p\Re\operatorname{Tr}(U_p)
\right\}
\prod_\ell dH(U_\ell).
\]

Define

\[
\phi_p(U)=1-\frac12\Re\operatorname{Tr}(U_p).
\]

Fix \(t\in(0,2)\), \(\eta>0\), and a monotone smooth source cutoff \(f_\eta:\mathbb R\to[0,1]\). The proof-friendly choice is an upper-envelope smoother satisfying

\[
\mathbf 1_{\{\phi_p\ge t\}}
\le
X_{p,\eta}:=f_\eta(\phi_p-t)
\le
\mathbf 1_{\{\phi_p\ge t-\eta\}}.
\tag{1.1}
\]

Define

\[
q_\eta:=\mathbb E_{\mu_{L,\beta}}X_{p,\eta}.
\tag{1.2}
\]

By translation invariance, \(q_\eta\) is independent of \(p\).

---

## 2. Block and conditioning geometry

Let \(C\subset T_L^4\) be a Balaban-style block or connected union of coarse cubes. Let \(C^+\) be a fixed local thickening sufficient to determine every plaquette in \(C\). Let

\[
C^\circ=C^{\ominus r_*}
\]

be the shaved core obtained by removing \(r_*\ge1\) layers from the block boundary.

Let \(E(C^+)\) be the set of links needed to determine all plaquettes in \(C\). Define

\[
\mathcal F_{C^c}
:=
\sigma\{U_\ell:\ell\notin E(C^+)\}.
\tag{2.1}
\]

This is the correct Gibbs-specification conditioning object because Wilson gauge variables live on links, not plaquettes.

Let \(\mathcal P(C^\circ)\) denote plaquettes contained in the core.

---

## 3. Lemma Q

For every fixed \(\eta>0\), there exist constants

\[
r_*\in\mathbb N,\qquad
M_0\in\mathbb N,\qquad
\beta_0<\infty,\qquad
C_Q<\infty,
\]

such that for every finite \(L\), every \(\beta\ge\beta_0\), every admissible block \(C\) of side \(M\ge M_0\), every finite plaquette set

\[
B\subset\mathcal P(C^\circ),
\]

and \(\mu_{L,\beta}\)-almost every exterior boundary condition \(\mathcal F_{C^c}\),

\[
\boxed{
\mathbb E_{\mu_{L,\beta}}
\left[
\prod_{p\in B}X_{p,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}.
}
\tag{Q}
\]

### Rooted Lemma Q

Under the same assumptions, for every local observable \(Y_{p_0}\) supported near \(p_0\in\mathcal P(C^\circ)\) satisfying

\[
0\le Y_{p_0}\le X_{p_0,\eta},
\tag{3.1}
\]

and for every finite \(B\subset\mathcal P(C^\circ)\setminus\{p_0\}\),

\[
\boxed{
\mathbb E_{\mu_{L,\beta}}
\left[
Y_{p_0}\prod_{p\in B}X_{p,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}
\mathbb E_{\mu_{L,\beta}}
\left[
Y_{p_0}
\;\middle|\;
\mathcal F_{C^c}
\right].
}
\tag{Q-root}
\]

Lemma Q asserts that frozen exterior conditions may distort constants, but cannot destroy the \(q_\eta\)-per-source power in a sufficiently interior block core.

---

## 4. Cavity-intensity form

For finite \(S\subset \mathcal P(C^\circ)\setminus\{p\}\), define

\[
\lambda_p(S\mid\mathcal F_{C^c})
:=
\frac{
\mathbb E\!\left[
X_{p,\eta}\prod_{r\in S}X_{r,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
}{
\mathbb E\!\left[
\prod_{r\in S}X_{r,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
}.
\tag{4.1}
\]

A stronger, distance-sensitive sufficient form is

\[
\boxed{
\lambda_p(S\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(
\sum_{r\in S}J(p,r)
\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
}
\tag{4.2}
\]

For a rooted source, define

\[
\lambda^{Y}_{p}(S\mid\mathcal F_{C^c})
:=
\frac{
\mathbb E\!\left[
Y_{p_0}X_{p,\eta}\prod_{r\in S}X_{r,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
}{
\mathbb E\!\left[
Y_{p_0}\prod_{r\in S}X_{r,\eta}
\;\middle|\;
\mathcal F_{C^c}
\right]
}.
\tag{4.3}
\]

The rooted sufficient form is

\[
\boxed{
\lambda^Y_p(S\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(
J(p,p_0)+\sum_{r\in S}J(p,r)
\right).
}
\tag{4.4}
\]

---

## 5. Cavity stability implies Lemma Q

Assume (4.2). Let

\[
B=\{p_1,\ldots,p_n\}.
\]

The chain rule gives

\[
\mathbb E\left[
\prod_{i=1}^nX_{p_i,\eta}
\middle|
\mathcal F_{C^c}
\right]
=
\prod_{i=1}^n
\lambda_{p_i}(\{p_1,\ldots,p_{i-1}\}\mid\mathcal F_{C^c}).
\tag{5.1}
\]

By (4.2),

\[
\lambda_{p_i}(\{p_1,\ldots,p_{i-1}\}\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(
\sum_{j<i}J(p_i,p_j)
\right).
\tag{5.2}
\]

Therefore,

\[
\mathbb E\left[
\prod_{p\in B}X_{p,\eta}
\middle|
\mathcal F_{C^c}
\right]
\le
q_\eta^{|B|}
\exp\left(
\sum_{\{p,r\}\subset B}J(p,r)
\right).
\tag{5.3}
\]

If

\[
\sup_{p\in\mathcal P(C^\circ)}
\sum_{r\in\mathcal P(C^\circ)\setminus\{p\}}
J(p,r)
\le
\log C_Q,
\tag{5.4}
\]

then

\[
\mathbb E\left[
\prod_{p\in B}X_{p,\eta}
\middle|
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}.
\tag{5.5}
\]

This proves Lemma Q.

The rooted proof is identical. Holding \(Y_{p_0}\) fixed as the base weight and applying (4.4),

\[
\mathbb E\left[
Y_{p_0}\prod_{i=1}^nX_{p_i,\eta}
\middle|
\mathcal F_{C^c}
\right]
=
\mathbb E\left[Y_{p_0}\middle|\mathcal F_{C^c}\right]
\prod_{i=1}^n
\lambda^Y_{p_i}(\{p_1,\ldots,p_{i-1}\}\mid\mathcal F_{C^c}),
\tag{5.6}
\]

hence

\[
\mathbb E\left[
Y_{p_0}\prod_{p\in B}X_{p,\eta}
\middle|
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}
\mathbb E\left[
Y_{p_0}
\middle|
\mathcal F_{C^c}
\right].
\tag{5.7}
\]

---

## 6. SU(2) one-link heat-bath mechanism

Write an SU(2) link as a unit quaternion

\[
u=(u_0,u_1,u_2,u_3)\in S^3.
\]

Condition on all links except one link \(\ell\). The Wilson action terms incident to \(\ell\) combine into a staple quaternion \(H_\ell\). In the project quaternion convention,

\[
\frac{\beta}{2}\sum_{p\ni \ell}\Re\operatorname{Tr}(U_p)
=
\beta\,\operatorname{Scal}(uH_\ell)+\text{constant}
=
\beta\,u\cdot \overline{H_\ell}+\text{constant}.
\tag{6.1}
\]

Therefore,

\[
u\mid U_{\ell^c}
\sim
\mathrm{vMF}_4(m_\ell,\kappa_\ell)
\quad\text{on }S^3,
\tag{6.2}
\]

with

\[
m_\ell=\frac{\overline{H_\ell}}{\|H_\ell\|},
\qquad
\kappa_\ell=\beta\|H_\ell\|.
\tag{6.3}
\]

For an incident plaquette \(p\ni\ell\), the complementary three-link product determines a unit quaternion \(n_{\ell,p}\) such that

\[
\frac12\Re\operatorname{Tr}(U_p)=u\cdot n_{\ell,p}.
\tag{6.4}
\]

The hard defect event \(\phi_p\ge t\) is exactly the spherical cap

\[
u\cdot n_{\ell,p}\le 1-t.
\tag{6.5}
\]

For the smooth upper-envelope source,

\[
X_{p,\eta}\le \mathbf 1_{\{\phi_p\ge t-\eta\}},
\tag{6.6}
\]

so its heat-bath expectation is bounded by the vMF cap probability with cap threshold

\[
a_{t-\eta}=1-(t-\eta).
\tag{6.7}
\]

---

## 7. Good-staple cap bound

Define

\[
\rho_{\ell,p}:=m_\ell\cdot n_{\ell,p}.
\tag{7.1}
\]

For \(a\in[-1,1]\),

\[
\sup_{x\in S^3:\,x\cdot n_{\ell,p}\le a}
m_\ell\cdot x
=
F(\rho_{\ell,p},a),
\tag{7.2}
\]

where

\[
F(\rho,a)=\rho a+\sqrt{1-\rho^2}\sqrt{1-a^2}.
\tag{7.3}
\]

If \(F(\rho_{\ell,p},a)<1\), a Laplace bound gives

\[
\mathrm{vMF}_4(m_\ell,\kappa_\ell)
\{x\cdot n_{\ell,p}\le a\}
\le
C_{\eta,\delta}
\exp\{-\kappa_\ell[(1-\delta)-F(\rho_{\ell,p},a)]\}.
\tag{7.4}
\]

Define

\[
\mathcal G_{\ell,p}(h_0,\rho_0)
=
\{\|H_\ell\|\ge h_0,\ \rho_{\ell,p}\ge\rho_0\},
\tag{7.5}
\]

with

\[
\rho_0>a_{t-\eta}.
\tag{7.6}
\]

Then

\[
\mathbb E[
X_{p,\eta}
\mid
\mathcal F_{\ell^c},\mathcal G_{\ell,p}(h_0,\rho_0)
]
\le
C_{\eta,\delta}
\exp\{-\beta h_0 c_{\rm cap}(t,\eta,\rho_0,\delta)\},
\tag{7.7}
\]

where

\[
c_{\rm cap}(t,\eta,\rho_0,\delta)
=
(1-\delta)-F(\rho_0,a_{t-\eta})>0.
\tag{7.8}
\]

This is the most concrete SU(2)-specific estimate behind Lemma Q.

---

## 8. Why a one-link cap bound is not enough

The cap estimate is necessary but not sufficient.

A plaquette source inside a block is affected by several links. Conditioning on one good staple controls one heat-bath update, not the full block Gibbs specification. Moreover, bad-staple regions need not be rare enough as unrooted events.

The correct strategy is:

1. Use the exact heat-bath cap bound to obtain local one-source rarity on good-staple parts.
2. Keep bad-staple contributions rooted under \(X_{p,\eta}\):

   \[
   R_{p,\ell,\eta}=X_{p,\eta}\mathbf 1_{\mathrm{bad}}.
   \tag{8.1}
   \]

3. Prove block source-stability in the core by comparing conditional measures with and without source insertions.
4. Use the cavity chain rule to obtain Lemma Q.

The crucial correction is:

\[
\boxed{
\text{Do not try to prove that bad-staple events alone are }q_\eta\text{-rare.}
}
\]

The correct rooted statement is

\[
0\le R_{p,\ell,\eta}\le X_{p,\eta}.
\tag{8.2}
\]

---

## 9. Lemma Q implies rooted cumulants

Assume Lemma Q and a compatible block-polymer localization/cluster expansion for smooth source insertions. Then source-marked local activities carry one \(q_\eta\) factor per marked source.

The resulting rooted cumulant bound is

\[
\boxed{
\left|
\kappa_W(
Y_{p_0},
X_{p_1,\eta},
\ldots,
X_{p_k,\eta}
)
\right|
\le
C^k
\mathbb E_WY_{p_0}
q_\eta^k
e^{-m\tau(\{p_0,\ldots,p_k\})}.
}
\tag{9.1}
\]

Taking \(Y_{p_0}=X_{p_0,\eta}\) gives

\[
\boxed{
\left|
\kappa_W(
X_{p_0,\eta},
\ldots,
X_{p_k,\eta}
)
\right|
\le
C^k
q_\eta^{k+1}
e^{-m\tau(\{p_0,\ldots,p_k\})}.
}
\tag{9.2}
\]

At \(k=1\),

\[
\boxed{
|\operatorname{Cov}_W(X_{p,\eta},X_{q,\eta})|
\le
Cq_\eta^2 e^{-md(p,q)}.
}
\tag{9.3}
\]

For every \(0\le Y_p\le X_{p,\eta}\),

\[
\boxed{
|\operatorname{Cov}_W(Y_p,X_{q,\eta})|
\le
C\mathbb E_WY_p\,q_\eta e^{-md(p,q)}.
}
\tag{9.4}
\]

---

## 10. PTO level-(iii) consequence

Let

\[
A_p=P_{\le\Lambda,L}\mathbf1_{\partial p}P_{\le\Lambda,L}.
\tag{10.1}
\]

Assume

\[
\sup_p
\sum_q
e^{-md(p,q)}
\frac{\operatorname{tr}(A_pA_q)}{\kappa_\Lambda^2}
\le
C_{\rm PTO}.
\tag{10.2}
\]

Then (9.3) implies

\[
\boxed{
\sum_q
|\operatorname{Cov}_W(X_{p,\eta},X_{q,\eta})|
\operatorname{tr}(A_pA_q)
\le
C\,C_{\rm PTO}\,q_\eta^2\kappa_\Lambda^2.
}
\tag{10.3}
\]

---

## 11. Boundary-band bridge

Lemma Q is formulated for smooth sources \(X_{p,\eta}\). The hard source is

\[
X_p=\mathbf 1_{\{\phi_p\ge t\}}.
\tag{11.1}
\]

Since

\[
|X_p-X_{p,\eta}|
\le
\mathbf1_{\{|\phi_p-t|\le\eta\}},
\tag{11.2}
\]

the hard-source passage requires a boundary-band gate:

\[
\boxed{
\sum_Y
\mathbb E_W
\left[
\sum_{r\in Y}
\mathbf1_{\{|\phi_r-t|\le\eta\}}
\right]
\mathcal W_\theta(Y)
\le
\varepsilon_{\rm bdry}(\eta)
\sum_Yq^{|Y|}\mathcal W_\theta(Y),
\qquad
\varepsilon_{\rm bdry}(\eta)\to0.
}
\tag{11.3}
\]

This is separate from Lemma Q.

---

## 12. Numerical evidence hierarchy

### 12.1 Stage A: side-6 prototype

The first frozen-exterior block diagnostic used side-6 blocks, core margin 2, \(L=16\), \(\beta=3.5\), \(q_\eta\approx0.003\), \(\eta=0.005\), with block Metropolis resampling.

It supported the one-source and rooted one-cavity mechanism, but the core was tiny.

### 12.2 Strong side-8 block-Metropolis run

The stronger side-8 block-Metropolis run used

\[
L=16,\quad \beta=3.5,\quad q_\eta=0.003,\quad \eta=0.005,
\]

with side-8 frozen blocks, core margin 2, \(32\) frozen-boundary blocks, \(864\) core plaquettes per block, and roughly \(4.5\times10^3\) sampled root-target pairs per block.

The reported summary was

\[
\max_{\rm depth}\mathrm{median}(q_{\rm cond}/q_\eta)=0.8681,
\]

\[
q95(q_{\rm cond}/q_\eta)=2.6055,
\qquad
q99=3.7093,
\]

\[
\max\Lambda=1.5047,
\qquad
\mathrm{median}\,\Lambda=1.0056,
\]

\[
\max\Lambda_{\rm root}=1.5034,
\qquad
\mathrm{median}\,\Lambda_{\rm root}=1.0022.
\]

This was strong finite-volume support for Lemma Q, but block resampling was still Metropolis.

### 12.3 Primary anchor: exact heat-bath side-8 confirmation

The exact heat-bath side-8 run used

\[
L=16,\qquad \beta=3.5,\qquad q_\eta=0.003,\qquad \eta=0.005.
\]

Unlike the earlier side-8 block-Metropolis run, this run generated the full-link ensemble and resampled frozen-exterior blocks using exact SU(2) heat-bath updates:

\[
U_\ell\mid U_{\ell^c}
\sim
\mathrm{vMF}_4
\left(
\frac{\overline H_\ell}{\|H_\ell\|},
\beta\|H_\ell\|
\right).
\tag{12.1}
\]

The run configuration was

\[
N_{\rm cfg}=16,\qquad
\text{block side}=8,\qquad
\text{core margin}=2,
\]

\[
2\ \text{blocks/config},\qquad
32\ \text{frozen-boundary blocks total},
\]

\[
864\ \text{core plaquettes/block},\qquad
\text{roughly }4.4\text{k--}4.5\text{k sampled root-target pairs/block}.
\]

Thresholding over all orientations gave

\[
t=1.0081100,
\qquad
q_\eta=0.003000,
\qquad
q_{\rm hard}=0.002989.
\tag{12.2}
\]

The single-source conditional statistics were

\[
\max_{\rm depth}\mathrm{median}(q_{\rm cond}/q_\eta)=0.8681,
\tag{12.3}
\]

\[
q95(q_{\rm cond}/q_\eta)=2.6087,
\qquad
q99(q_{\rm cond}/q_\eta)=3.5172,
\qquad
\max(q_{\rm cond}/q_\eta)=6.0754.
\tag{12.4}
\]

The ordinary cavity ratio was

\[
\max\Lambda=1.4626,
\qquad
\mathrm{median}\,\Lambda=0.9249.
\tag{12.5}
\]

The rooted bad-staple cavity ratio was

\[
\max\Lambda_{\rm root}=1.3998,
\qquad
\mathrm{median}\,\Lambda_{\rm root}=0.9563.
\tag{12.6}
\]

These are the strongest current numerical diagnostics for Lemma Q. They support

\[
\mathbb E[X_{p,\eta}\mid\mathcal F_{C^c}]=O(q_\eta),
\]

\[
\mathbb E[X_rX_p\mid\mathcal F_{C^c}]
=
O(q_\eta\,\mathbb E[X_r\mid\mathcal F_{C^c}]),
\]

and

\[
\mathbb E[Y_rX_p\mid\mathcal F_{C^c}]
=
O(q_\eta\,\mathbb E[Y_r\mid\mathcal F_{C^c}]).
\]

The exact heat-bath run confirms that the previous block-Metropolis side-8 result was not an artifact of approximate conditional sampling.

### 12.4 Geometry robustness supplement: Stage B side-10/core-margin-3

A larger-geometry Stage B block run tested whether the side-8 results were an artifact of a too-small frozen block or insufficient core depth. This run used

\[
L=16,\qquad \beta=3.5,\qquad q_\eta=0.003,\qquad \eta=0.005,
\]

with block side \(10\), core margin \(3\), \(64\) frozen-boundary blocks, \(864\) core plaquettes per block, and distance bins extending through \(d=12\).

Unlike the exact heat-bath side-8 anchor, Stage B used Metropolis global and block updates. It should therefore be interpreted as a **geometry robustness supplement**, not as the primary sampling-standard result.

Thresholding gave

\[
t=1.0092124,
\qquad
q_\eta=0.003000,
\qquad
q_{\rm hard}=0.002993.
\tag{12.7}
\]

Single-source conditional control:

\[
\max_{\rm depth}\mathrm{median}(q_{\rm cond}/q_\eta)=1.2681,
\tag{12.8}
\]

\[
q95(q_{\rm cond}/q_\eta)=2.8596,
\qquad
\max(q_{\rm cond}/q_\eta)=9.1007,
\tag{12.9}
\]

with depth bins

\[
\{3,4\}.
\tag{12.10}
\]

Ordinary cavity:

\[
\max\Lambda=2.6074,
\qquad
\mathrm{median}\,\Lambda=1.0028.
\tag{12.11}
\]

Rooted bad-staple cavity:

\[
\max\Lambda_{\rm root}=2.4132,
\qquad
\mathrm{median}\,\Lambda_{\rm root}=1.0024.
\tag{12.12}
\]

Cap-feature regressions had the expected negative signs:

\[
g\text{-slope}=-9.5291,
\qquad
R_g^2=0.0278,
\tag{12.13}
\]

\[
\rho\text{-slope}=-370.513,
\qquad
R_\rho^2=0.0587.
\tag{12.14}
\]

Stage B supports the same Lemma Q mechanism under larger block/core geometry. The maxima are higher than in the exact heat-bath side-8 run, but they remain \(O(1)\), while the medians remain essentially \(1\). The correct summary is

\[
\boxed{
\text{larger block/core geometry did not produce cavity amplification.}
}
\]

### 12.5 Cap predictor conclusion

The exact heat-bath run gave

\[
\text{cap-feature slope}=-5.182,
\qquad
R^2=0.0101.
\]

Stage B gave

\[
g\text{-slope}=-9.5291,
\qquad
R_g^2=0.0278.
\]

The signs are correct, but explanatory power remains weak. Therefore the analytic target is not a pure one-link cap proof. The cap estimate is a local SU(2) input; the load-bearing theorem must be block source-stability.

---

## 13. Exact heat-bath algorithmic anchor

The exact heat-bath numerical upgrade is the primary algorithmic version for Lemma Q diagnostics:

\[
U_\ell\leftarrow \mathrm{vMF}_4
\left(
\frac{\overline H_\ell}{\|H_\ell\|},
\beta\|H_\ell\|
\right).
\tag{13.1}
\]

This is not a Metropolis accept/reject update. The update statistic is identically \(1\) because every selected link is redrawn from its one-link Gibbs conditional.

The implementation uses a dimension-four vMF rejection sampler,

\[
p=4,\qquad z\sim{\rm Beta}(3/2,3/2),
\]

with Wood-style acceptance and a Householder rotation taking \(e_0\) to the heat-bath mean vector.

In the project quaternion convention,

\[
\operatorname{Scal}(U H)=U\cdot\overline H,
\]

so the heat-bath mean is \(\overline H/\|H\|\), not \(H/\|H\|\).

---

## 14. Honest status

### What is proved here

1. The precise statement of Lemma Q.
2. The rooted version of Lemma Q.
3. The proof that cavity source-stability implies Lemma Q.
4. The SU(2) exact heat-bath/vMF cap mechanism.
5. The implication

\[
\text{Lemma Q + source-local polymer expansion}
\Rightarrow
\text{rooted cumulants}
\Rightarrow
\text{pair/rooted closure}
\Rightarrow
\text{PTO level-(iii)}.
\]

### What is not proved

The following are still open:

1. The block source-stability bound (4.2) for SU(2) Wilson at large \(\beta\).
2. The rooted tilted version (4.4).
3. The source-weighted Bałaban polymer expansion carrying one \(q_\eta\) factor per mark.
4. The boundary-band gate \(\eta\to0\).
5. The final hard-indicator \((M')_{\rm SU(2)}\).

### Correct claim

\[
\boxed{
\text{Lemma Q is the precise local rare-source theorem needed for SU(2).}
}
\]

The exact heat-bath side-8 diagnostics support the one-source and rooted one-cavity consequences. The Stage B side-10 geometry run supports robustness under larger block/core geometry. These diagnostics do not prove Lemma Q.

---

## 15. Manuscript-safe wording

Use:

> We isolate the remaining SU(2) probability input as a local rare-source factorization theorem, Lemma Q. It states that, after freezing the exterior of a Balaban block, smooth high-plaquette sources in the shaved core retain one factor of \(q_\eta\) per source, with a rooted analogue for \(0\le Y\le X_{p,\eta}\). A cavity-intensity form with exponentially summable influence kernel \(J(p,r)\) implies the product bound by a chain-rule argument. Exact heat-bath frozen-exterior diagnostics at \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\) support the one-source and rooted one-cavity consequences. A side-10/core-margin-3 Stage B run further supports geometry robustness, with cavity and rooted-cavity medians essentially equal to one and maxima remaining \(O(1)\). Lemma Q remains an analytic theorem to be proved.

Do not use:

> Lemma Q is proved for SU(2).

Do not use:

> The numerical diagnostics establish \((M')_{\mathrm{SU(2)}}\).

Do not use:

> The one-link vMF cap bound alone proves Lemma Q.

---

## 16. Minimal next analytic target

The smallest theorem worth attacking now is

\[
\boxed{
\lambda_p(S\mid\mathcal F_{C^c})
\le
q_\eta\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le C e^{-md_C(p,r)}.
}
\]

The rooted version is

\[
\boxed{
\lambda^Y_p(S\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(
J(p,p_0)+\sum_{r\in S}J(p,r)
\right).
}
\]

The most concrete SU(2) input toward this theorem is the exact heat-bath cap bound. The global proof likely requires a block comparison or source-weighted cluster expansion, not a pointwise one-link cap estimate alone.

---

## 17. Ledger entry

**LEMMA_Q_SU2_LOCAL_RARE_SOURCE_FACTORING_EXACT_HEATBATH_AND_STAGEB_GEOMETRY_UPDATE_20260525.**  
Lemma Q is the local conditional rare-source theorem required for the PMBSF SU(2) smooth-source polymer route. It asserts that in the shaved core of a frozen-exterior Balaban block,

\[
\mathbb E[\prod_{p\in B}X_{p,\eta}\mid\mathcal F_{C^c}]
\le
(C_Qq_\eta)^{|B|},
\]

with rooted variant

\[
\mathbb E[Y_{p_0}\prod_{p\in B}X_{p,\eta}\mid\mathcal F_{C^c}]
\le
(C_Qq_\eta)^{|B|}
\mathbb E[Y_{p_0}\mid\mathcal F_{C^c}].
\]

A cavity intensity estimate with exponentially summable influence kernel implies Lemma Q by the chain rule. The exact SU(2) one-link heat-bath law is vMF on \(S^3\), and incident plaquette defects are spherical caps, giving the concrete local good-staple cap estimate.

The strongest current numerical anchor is `PMBSF_SU2_LemmaQ_exact_heatbath_side8_20260525_165641`. It used exact SU(2) heat-bath global generation and exact heat-bath frozen-block resampling at \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\), with \(N_{\rm cfg}=16\), side-8 blocks, core margin 2, 32 frozen-boundary blocks, 864 core plaquettes/block, and roughly 4.4k--4.5k sampled root-target pairs/block. Thresholding gave \(t=1.0081100\), \(q_\eta=0.003000\), \(q_{\rm hard}=0.002989\). Single-source conditional control passed with max depth-median \(q_{\rm cond}/q=0.8681\), q95 \(=2.6087\), q99 \(=3.5172\), max \(=6.0754\). Cavity source-stability passed with max \(\Lambda=1.4626\), median \(\Lambda=0.9249\). Rooted bad-staple cavity passed with max \(\Lambda_{\rm root}=1.3998\), median \(\Lambda_{\rm root}=0.9563\). The cap predictor had negative slope \(-5.182\) but weak \(R^2=0.0101\).

The geometry robustness supplement is `PMBSF_SU2_LemmaQ_block_conditional_stageB_geometry_20260525_165752`. It used \(L=16,\beta=3.5,q_\eta=0.003,\eta=0.005\), Metropolis global and block updates, \(N_{\rm cfg}=32\), side-10 blocks, core margin 3, 64 frozen-boundary blocks, 864 core plaquettes/block, block_therm=256, block_between=10, and block_samples=256. Thresholding gave \(t=1.0092124\), \(q_\eta=0.003000\), \(q_{\rm hard}=0.002993\). Single-source conditional control passed with max depth-median \(q_{\rm cond}/q=1.2681\), q95 \(=2.8596\), max \(=9.1007\), with depth bins \([3,4]\). Cavity source-stability passed with max \(\Lambda=2.6074\), median \(\Lambda=1.0028\), and distance bins through \(d=12\). Rooted bad-staple cavity passed with max \(\Lambda_{\rm root}=2.4132\), median \(\Lambda_{\rm root}=1.0024\). Cap predictors had negative slopes with weak-to-moderate explanatory power: \(g\)-slope \(-9.5291\), \(R_g^2=0.0278\), \(\rho\)-slope \(-370.513\), \(R_\rho^2=0.0587\).

Conclusion: exact heat-bath diagnostics strongly support the one-source and rooted one-cavity consequences of Lemma Q, while Stage B supports robustness under larger block/core geometry. Lemma Q remains open analytically. The proof should target block source-stability, not unrooted bad-staple rarity and not a one-link cap bound alone.
