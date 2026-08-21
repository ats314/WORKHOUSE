# Expanded Derivations from the PMBSF / Lemma Q / SU(3) Files

**Date:** 2026-05-25  
**Purpose:** expand the derivational spine from the current project files into a manuscript-ready technical reference.  
**Status:** conditional proof architecture plus local spectral theorems and finite-volume numerical evidence. This is not a Yang--Mills mass-gap proof.

---

## 0. Source anchors used

This document expands the derivations from the following project anchors.

1. **Lemma Q / SU(2) rare-source line**
   - `LEM_PMBSF_lemma_q_su2_local_rare_source_factorization.md`
   - Exact heat-bath side-8 run: `PMBSF_SU2_LemmaQ_exact_heatbath_side8_20260525_165641`
   - Stage B side-10 geometry run: `PMBSF_SU2_LemmaQ_block_conditional_stageB_geometry_20260525_165752`

2. **Full-volume SU(2) pair/rooted covariance evidence**
   - `PMBSF_SU2_closure_stage2_L12_L16_20260525_020743`
   - Chat-log ledger for `PMBSF_SU2_closure_stage3_L64_20260525_030224`

3. **PMBSF deterministic/projected-capacity spine**
   - `PMBSF_master (2).md`
   - `PMBSF_quick_reference_for_simulations_third_pass_20260524.md`
   - `HBq2_Lemmas_A_to_D_ThirdPass_20260524.md`

4. **SU(3) class-function / finite-channel line**
   - `SU3_Weyl_Invariant_c1_Derivation_Useful_Old_Notes.md`
   - `SU3_Finite_Channel_CT_Poincare_Balaban_SUN_Manuscript.md`
   - `Concrete_Novel_Weyl_Spectral_Theory_with_Polymer_Bridge.md`
   - `Unified_Compact_Group_Spectral_Anchors_Corrected_Master.md`

---

# Part I — PMBSF / SU(2) Expanded Derivations

---

## 1. Deterministic projected-capacity spine

### 1.1 Physical projector and plaquette atoms

Let \(P=P_{\le\Lambda,L}\) denote the projected transverse Maxwell/physical-sector projector on the finite periodic lattice. For each plaquette \(p\), let \(\partial p\) be its oriented set of four incident links. Define the projected plaquette atom

\[
A_p:=P\mathbf 1_{\partial p}P.
\]

Here \(\mathbf 1_{\partial p}\) is the diagonal link projector onto the four boundary links of \(p\).

The two fundamental deterministic quantities are:

\[
\operatorname{tr}(A_pA_q),
\]

and

\[
\kappa_\Lambda:=\sup_p \|A_p\|.
\]

The trace overlap expands as

\[
\operatorname{tr}(A_pA_q)
=
\operatorname{tr}(P\mathbf 1_{\partial p}P\mathbf 1_{\partial q}P).
\]

Using the kernel \(P(e,f)\) of the link projector,

\[
\operatorname{tr}(A_pA_q)
=
\sum_{e\in\partial p}
\sum_{f\in\partial q}
|P(e,f)|^2.
\tag{1.1}
\]

This identity is the deterministic reason that the correct stochastic object is not a scalar plaquette covariance alone, but the **trace-weighted** covariance

\[
\sum_q
|\operatorname{Cov}(X_p,X_q)|\operatorname{tr}(A_pA_q).
\]

The incident-overlap lemma in the project files uses the crude Cauchy--Schwarz bound

\[
|P(e,f)|^2\le P(e,e)P(f,f)=\mu^2,
\]

so that, since \(|\partial p|=|\partial q|=4\),

\[
\operatorname{tr}(A_pA_q)\le 16\mu^2.
\tag{1.2}
\]

Exact finite-Fourier evaluation improves the operational incident constant well below the crude \(80\mu^2\) row bound. This is why the project uses a PTO-weighted operator-level statement rather than a pointwise \(q^2\) covariance theorem.

### 1.2 Deterministic PTO summability

The core deterministic estimate needed downstream has the form

\[
\boxed{
\sup_p
\sum_q e^{-m d(p,q)}
\frac{\operatorname{tr}(A_pA_q)}{\kappa_\Lambda^2}
\le
C_{\rm PTO}(m,\Lambda).
}
\tag{1.3}
\]

If the stochastic input gives

\[
|\operatorname{Cov}(X_p,X_q)|
\le
C_{\rm src}q_\eta^2 e^{-m d(p,q)},
\tag{1.4}
\]

then multiplying by \(\operatorname{tr}(A_pA_q)\) and summing gives

\[
\sum_q
|\operatorname{Cov}(X_p,X_q)|
\operatorname{tr}(A_pA_q)
\le
C_{\rm src}q_\eta^2
\sum_q e^{-m d(p,q)}\operatorname{tr}(A_pA_q).
\]

Using (1.3),

\[
\boxed{
\sum_q
|\operatorname{Cov}(X_p,X_q)|
\operatorname{tr}(A_pA_q)
\le
C_{\rm src}C_{\rm PTO}
q_\eta^2\kappa_\Lambda^2.
}
\tag{1.5}
\]

This is the precise level-(iii) PTO consequence of the source theorem.

---

## 2. Birman--Schwinger firewall derivation

Let \(M\) be the positive projected Maxwell comparator on the physical subspace and let \(V_D\) be a defect potential supported by a high-plaquette set \(D\). The standard quadratic-form target is

\[
M - V_D \succeq cM
\]

for some \(c>0\). Equivalently,

\[
M^{-1/2}V_DM^{-1/2}\preceq \Theta I
\]

with \(\Theta<1\). Then

\[
M^{-1/2}(M-V_D)M^{-1/2}
=
I-M^{-1/2}V_DM^{-1/2}
\succeq
(1-\Theta)I.
\]

Therefore,

\[
\boxed{
M-V_D\succeq (1-\Theta)M.
}
\tag{2.1}
\]

The projected Birman--Schwinger statistic is

\[
\Theta_D
:=
\|M^{-1/2}P V_D P M^{-1/2}\|.
\]

The v3b danger-corner certificate gives the strongest finite-volume empirical version:

\[
\Theta_*=\max\Theta_D=0.884442692429<1,
\]

so the empirical coercivity margin in the tested corner is

\[
1-\Theta_*=0.115557307571.
\tag{2.2}
\]

The key point is that the unprojected operator can fail badly while the physical-sector projection remains subcritical. In the worst v3b row,

\[
\theta_{\rm unprojected}=1.9967101255401256,
\]

but

\[
\theta_{\rm phys}=0.8844426924294179.
\]

Thus the physical projection supplies the load-bearing suppression.

---

## 3. Random plaquette-incidence comparator and Bernstein firewall

Let \(B_p\sim\mathrm{Bernoulli}(q)\) independently over plaquettes. Let \(D(B)\) be the induced defect link set obtained by exact plaquette-to-link incidence. The projected random operator has the form

\[
S_B=P\mathbf 1_{D(B)}P.
\]

The sharp Bernstein-type comparator in the master has the form

\[
\boxed{
\|P\mathbf 1_{D(B)}P\|
\le
6q+
\sqrt{12q\kappa_\Lambda\log(2K/\delta)}
+
\frac{2\kappa_\Lambda}{3}\log(2K/\delta)
}
\tag{3.1}
\]

with probability at least \(1-\delta\).

The deterministic factor \(6q\) arises because each link in four dimensions is incident to six oriented plaquette planes. The fluctuation terms are controlled by \(\kappa_\Lambda\) and the projected rank \(K\).

The empirical comparator lesson is:

\[
\boxed{
\text{the correct stochastic unit is the plaquette passed through exact incidence, not an independent edge.}
}
\]

The edge-Bernoulli comparator failed because a single plaquette activates four boundary links coherently, producing local correlated edge activation that independent edge models miss.

---

## 4. Lemma Q derivation

### 4.1 Lemma statement

Let \(C\) be a block, \(C^\circ\) its shaved core, and \(\mathcal F_{C^c}\) the exterior link sigma-field. Lemma Q is:

\[
\boxed{
\mathbb E\left[
\prod_{p\in B}X_{p,\eta}
\mid
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}
}
\tag{4.1}
\]

for every finite \(B\subset\mathcal P(C^\circ)\).

The rooted version is:

\[
\boxed{
\mathbb E\left[
Y_{p_0}
\prod_{p\in B}X_{p,\eta}
\mid
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}
\mathbb E\left[Y_{p_0}\mid\mathcal F_{C^c}\right],
}
\tag{4.2}
\]

for \(0\le Y_{p_0}\le X_{p_0,\eta}\).

### 4.2 Cavity source-stability implies Lemma Q

Define

\[
\lambda_p(S\mid\mathcal F_{C^c})
=
\frac{
\mathbb E\left[
X_{p,\eta}\prod_{r\in S}X_{r,\eta}
\mid
\mathcal F_{C^c}
\right]
}{
\mathbb E\left[
\prod_{r\in S}X_{r,\eta}
\mid
\mathcal F_{C^c}
\right]
}.
\tag{4.3}
\]

Assume the cavity source-stability estimate

\[
\lambda_p(S\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le C_Je^{-m_Jd_C(p,r)}.
\tag{4.4}
\]

Let \(B=\{p_1,\ldots,p_n\}\). The conditional chain rule gives

\[
\mathbb E\left[
\prod_{i=1}^nX_{p_i,\eta}
\mid
\mathcal F_{C^c}
\right]
=
\prod_{i=1}^n
\lambda_{p_i}(\{p_1,\ldots,p_{i-1}\}\mid\mathcal F_{C^c}).
\tag{4.5}
\]

Using (4.4),

\[
\mathbb E\left[
\prod_{i=1}^nX_{p_i,\eta}
\mid
\mathcal F_{C^c}
\right]
\le
q_\eta^n
\exp\left(
\sum_{i=1}^n\sum_{j<i}J(p_i,p_j)
\right).
\tag{4.6}
\]

If the influence kernel is uniformly summable,

\[
\sup_p\sum_r J(p,r)\le \log C_Q,
\tag{4.7}
\]

then

\[
\exp\left(
\sum_{i=1}^n\sum_{j<i}J(p_i,p_j)
\right)
\le
C_Q^n.
\tag{4.8}
\]

Thus

\[
\boxed{
\mathbb E\left[
\prod_{p\in B}X_{p,\eta}
\mid
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}.
}
\tag{4.9}
\]

The rooted proof is identical. Define

\[
\lambda_p^Y(S\mid\mathcal F_{C^c})
=
\frac{
\mathbb E\left[
Y_{p_0}X_{p,\eta}\prod_{r\in S}X_{r,\eta}
\mid
\mathcal F_{C^c}
\right]
}{
\mathbb E\left[
Y_{p_0}\prod_{r\in S}X_{r,\eta}
\mid
\mathcal F_{C^c}
\right]
}.
\tag{4.10}
\]

Assume

\[
\lambda_p^Y(S\mid\mathcal F_{C^c})
\le
q_\eta\exp\left(J(p,p_0)+\sum_{r\in S}J(p,r)\right).
\tag{4.11}
\]

Then

\[
\boxed{
\mathbb E\left[
Y_{p_0}\prod_{p\in B}X_{p,\eta}
\mid
\mathcal F_{C^c}
\right]
\le
(C_Qq_\eta)^{|B|}
\mathbb E\left[Y_{p_0}\mid\mathcal F_{C^c}\right].
}
\tag{4.12}
\]

This is the cleanest analytic formulation of the missing SU(2) probability theorem.

---

## 5. Exact SU(2) heat-bath/vMF cap derivation

Write an SU(2) link as a unit quaternion

\[
u=(u_0,u_1,u_2,u_3)\in S^3.
\]

Given all links except \(u=U_\ell\), the Wilson action terms involving \(\ell\) combine into a staple quaternion \(H_\ell\). In the project convention,

\[
\operatorname{Scal}(uH_\ell)=u\cdot\overline H_\ell.
\]

Therefore the one-link conditional density is

\[
d\nu_\ell(u\mid U_{\ell^c})
\propto
\exp\left(\beta u\cdot\overline H_\ell\right)d\sigma_{S^3}(u).
\tag{5.1}
\]

Writing

\[
m_\ell=\frac{\overline H_\ell}{\|H_\ell\|},
\qquad
\kappa_\ell=\beta\|H_\ell\|,
\]

we get the exact heat-bath identity

\[
\boxed{
U_\ell\mid U_{\ell^c}
\sim
\mathrm{vMF}_4(m_\ell,\kappa_\ell).
}
\tag{5.2}
\]

For a plaquette \(p\ni\ell\), the complementary three-link product defines a unit quaternion \(n_{\ell,p}\) such that

\[
\frac12\Re\operatorname{Tr}(U_p)=u\cdot n_{\ell,p}.
\tag{5.3}
\]

The high-plaquette event

\[
\phi_p=1-\frac12\Re\operatorname{Tr}(U_p)\ge t
\]

is therefore

\[
u\cdot n_{\ell,p}\le 1-t.
\tag{5.4}
\]

That is an exact spherical cap in \(S^3\).

For the smooth upper-envelope source,

\[
X_{p,\eta}\le \mathbf1_{\{\phi_p\ge t-\eta\}},
\]

hence

\[
X_{p,\eta}\le \mathbf1_{\{u\cdot n_{\ell,p}\le a_{t-\eta}\}},
\qquad
a_{t-\eta}=1-(t-\eta).
\tag{5.5}
\]

Let

\[
\rho_{\ell,p}=m_\ell\cdot n_{\ell,p}.
\]

The spherical optimization identity is

\[
\sup_{u\in S^3:\,u\cdot n\le a}m\cdot u
=
\rho a+\sqrt{1-\rho^2}\sqrt{1-a^2}
=:F(\rho,a).
\tag{5.6}
\]

If \(F(\rho,a)<1\), Laplace comparison gives

\[
\nu_\ell\{u\cdot n\le a\}
\le
C_{\eta,\delta}
\exp\{-\kappa_\ell[(1-\delta)-F(\rho,a)]\}.
\tag{5.7}
\]

On the good-staple set

\[
\|H_\ell\|\ge h_0,
\qquad
\rho_{\ell,p}\ge\rho_0>a_{t-\eta},
\]

this becomes

\[
\boxed{
\mathbb E[X_{p,\eta}\mid U_{\ell^c},\mathcal G_{\ell,p}]
\le
C_{\eta,\delta}
\exp\{-\beta h_0 c_{\rm cap}(t,\eta,\rho_0,\delta)\}.
}
\tag{5.8}
\]

This is the local SU(2) mechanism. It is not enough alone to prove Lemma Q, because Lemma Q is a block Gibbs statement. But it is the exact one-link cap input.

---

## 6. Lemma Q to rooted cumulants

Assume Lemma Q and a compatible source-local polymer expansion. For sources \(X_{p,\eta}\), the source log-partition function is

\[
\Psi(h)=
\log
\mathbb E
\exp\left(
\sum_p h_pX_{p,\eta}
\right).
\]

Cumulants are square-free source derivatives:

\[
\kappa(X_{p_1,\eta},\ldots,X_{p_k,\eta})
=
\partial_{h_{p_1}}\cdots\partial_{h_{p_k}}\Psi(h)\big|_{h=0}.
\]

If source-marked local activities satisfy

\[
|\partial_{h_B}E_\eta^\#(X;0)|
\le
C^{|X|}e^{-cd(X)}q_\eta^{|B|},
\tag{6.1}
\]

then summing connected activities gives

\[
\boxed{
|\kappa(X_{p_1,\eta},\ldots,X_{p_k,\eta})|
\le
C^k q_\eta^k e^{-m\tau(\{p_1,\ldots,p_k\})}.
}
\tag{6.2}
\]

For rooted \(0\le Y_{p_0}\le X_{p_0,\eta}\), the same argument gives

\[
\boxed{
|\kappa(Y_{p_0},X_{p_1,\eta},\ldots,X_{p_k,\eta})|
\le
C^k\mathbb E[Y_{p_0}]q_\eta^k e^{-m\tau(\{p_0,\ldots,p_k\})}.
}
\tag{6.3}
\]

At \(k=1\),

\[
|\operatorname{Cov}(X_p,X_q)|
\le
Cq_\eta^2e^{-md(p,q)},
\tag{6.4}
\]

and

\[
|\operatorname{Cov}(Y_p,X_q)|
\le
C\mathbb E[Y_p]q_\eta e^{-md(p,q)}.
\tag{6.5}
\]

This is exactly the pair/rooted closure tested by the full-volume covariance diagnostics.

---

## 7. Full-volume pair/rooted covariance evidence

### 7.1 L12/L16 file-backed run

The L12/L16 closure run gives direct evidence for (6.4)--(6.5).

For \(L=12,\beta=3.5\),

\[
q_\eta=0.0030031849,
\]

\[
\max |\operatorname{Cov}(X,X)|/q_\eta^2=1.0070508,
\]

\[
\mathrm{median}=0.11698958,
\qquad
\text{slope}=-0.029523351.
\]

The rooted bad-staple covariance satisfies

\[
\max |\operatorname{Cov}(X\mathbf1_{\rm bad},X)|/(\mathbb E[X\mathbf1_{\rm bad}]q_\eta)=0.98707918,
\]

\[
\mathrm{median}=0.10898202,
\qquad
\text{slope}=-0.025468127.
\]

For \(L=16,\beta=3.5\),

\[
q_\eta=0.0030047828,
\]

\[
\max |\operatorname{Cov}(X,X)|/q_\eta^2=1.1296034,
\]

\[
\mathrm{median}=0.070512456,
\qquad
\text{slope}=-0.030772935.
\]

Rooted:

\[
\max=1.1687138,
\qquad
\mathrm{median}=0.075050267,
\qquad
\text{slope}=-0.036934331.
\]

The key trend is that medians decrease from \(L=12\) to \(L=16\), while maxima remain \(O(1)\).

### 7.2 L64 chat-run ledger

The L64 run exists as chat-log ledger:

\[
\texttt{PMBSF\_SU2\_closure\_stage3\_L64\_20260525\_030224}.
\]

Configuration:

\[
L=64,\quad
\beta=3.5,\quad
N_{\rm cfg}=64,\quad
\text{therm}=500,\quad
\text{between}=50.
\]

Results:

\[
q_\eta=0.0030061514,
\qquad
q_{\rm hard}=0.0030000228.
\]

Pair:

\[
\max |\operatorname{Cov}(X,X)|/q_\eta^2=0.86578135,
\]

\[
\mathrm{median}=0.0067171416,
\qquad
\text{slope}=-0.014734895.
\]

Rooted:

\[
\max=0.89244247,
\]

\[
\mathrm{median}=0.0074250476,
\qquad
\text{slope}=-0.0093512057.
\]

This extends the pair/rooted evidence through \(L=64\). For paper-grade packaging, the L64 `RUN_READOUT.md` or `summary.csv` should be included in the artifact set so the claim can be file-cited directly.

---

## 8. Local Lemma Q diagnostics

### 8.1 Primary anchor: exact heat-bath side-8

The exact heat-bath side-8 run is the primary Lemma Q numerical anchor because both global generation and frozen-block resampling use the exact SU(2) one-link conditional.

Configuration:

\[
L=16,\quad \beta=3.5,\quad q_\eta=0.003,\quad \eta=0.005,
\]

\[
N_{\rm cfg}=16,\quad \text{block side}=8,\quad \text{core margin}=2,
\]

\[
32\ \text{frozen-boundary blocks},\quad
864\ \text{core plaquettes/block}.
\]

Thresholding:

\[
t=1.0081100,
\qquad
q_\eta=0.003000,
\qquad
q_{\rm hard}=0.002989.
\]

Single-source conditional:

\[
\max_{\rm depth}\mathrm{median}(q_{\rm cond}/q_\eta)=0.8681,
\]

\[
q95=2.6087,\qquad q99=3.5172,\qquad \max=6.0754.
\]

Cavity:

\[
\max\Lambda=1.4626,
\qquad
\mathrm{median}\,\Lambda=0.9249.
\]

Rooted cavity:

\[
\max\Lambda_{\rm root}=1.3998,
\qquad
\mathrm{median}\,\Lambda_{\rm root}=0.9563.
\]

This supports:

\[
\mathbb E[X_p\mid\mathcal F_{C^c}]=O(q_\eta),
\]

\[
\mathbb E[X_rX_p\mid\mathcal F_{C^c}]
=
O(q_\eta\mathbb E[X_r\mid\mathcal F_{C^c}]),
\]

and

\[
\mathbb E[Y_rX_p\mid\mathcal F_{C^c}]
=
O(q_\eta\mathbb E[Y_r\mid\mathcal F_{C^c}]).
\]

### 8.2 Geometry robustness: Stage B side-10/core-margin-3

Stage B tested larger block/core geometry:

\[
\text{block side}=10,\qquad \text{core margin}=3.
\]

Configuration:

\[
L=16,\quad \beta=3.5,\quad q_\eta=0.003,\quad \eta=0.005,
\]

\[
64\ \text{frozen-boundary blocks},\quad 864\ \text{core plaquettes/block}.
\]

Thresholding:

\[
t=1.0092124,\qquad q_\eta=0.003000,\qquad q_{\rm hard}=0.002993.
\]

Single-source:

\[
\max_{\rm depth}\mathrm{median}(q_{\rm cond}/q_\eta)=1.2681,
\]

\[
q95=2.8596,\qquad \max=9.1007.
\]

Cavity:

\[
\max\Lambda=2.6074,
\qquad
\mathrm{median}\,\Lambda=1.0028.
\]

Rooted:

\[
\max\Lambda_{\rm root}=2.4132,
\qquad
\mathrm{median}\,\Lambda_{\rm root}=1.0024.
\]

Thus larger block/core geometry did not produce cavity amplification. The exact heat-bath side-8 run remains the primary numerical anchor; Stage B is the geometry-robustness supplement.

---

# Part II — SU(3) Weyl-Invariant Class-Function Derivation

---

## 9. SU(3) local Hamiltonian and Weyl coordinates

The SU(3) one-plaquette class Hamiltonian is

\[
H_\beta
=
\frac12C_2+
\beta\left(1-\frac13\operatorname{Re}\chi_{1,0}\right).
\tag{9.1}
\]

Near the identity, restrict to the Cartan plane and use Weyl-invariant coordinates

\[
p_2=x^2+y^2,
\]

\[
p_3=\frac{\sqrt6}{6}y(3x^2-y^2).
\]

The Weyl discriminant satisfies

\[
\Delta_W^2(x,y)
=
\frac{x^2(x^2-3y^2)^2}{2}.
\]

The key algebraic identity is

\[
\boxed{
\Delta_W^2=\frac{p_2^3}{2}-3p_3^2.
}
\tag{9.2}
\]

This identity is what forces the full rank-two invariant measure. A radial-only treatment drops \(p_3\) and misses a real contribution to the \(\beta^{-1/2}\) coefficient.

The Weyl-Gaussian inner product is

\[
\langle f,g\rangle
=
\int_{\mathbb R^2}
f(x,y)g(x,y)
\Delta_W^2(x,y)e^{-x^2-y^2}\,dx\,dy.
\tag{9.3}
\]

---

## 10. Scaled perturbation expansion

After Weyl reduction and canonical scaling,

\[
H_\beta
=
\beta^{1/2}H_0+H_1+\beta^{-1/2}H_2+O(\beta^{-1}).
\tag{10.1}
\]

The leading oscillator scale is

\[
\omega(\beta)=\sqrt{\frac{2\beta}{3}}.
\tag{10.2}
\]

The perturbations needed through \(O(\beta^{-1/2})\) are

\[
\boxed{
H_1=-\frac{p_2^2}{96},
}
\tag{10.3}
\]

and

\[
\boxed{
H_2
=
\sqrt6\left(
\frac{p_2^3}{11520}
+
\frac{p_3^2}{8640}
\right).
}
\tag{10.4}
\]

The \(p_3^2\) term is the non-radial Weyl-invariant correction. It is the main useful extraction from the old notes.

---

## 11. First correction \(c_0=-5/16\)

Let \(\psi_0\) be the ground Weyl-invariant state and \(\psi_1\) the first physical radial/class excitation. The file ledger gives

\[
\langle H_1\rangle_0=-\frac5{24},
\]

\[
\langle H_1\rangle_1=-\frac{25}{48}.
\]

Therefore the \(O(\beta^0)\) correction to the gap is

\[
c_0
=
\langle H_1\rangle_1-\langle H_1\rangle_0
=
-\frac{25}{48}+\frac5{24}.
\]

Since

\[
\frac5{24}=\frac{10}{48},
\]

\[
c_0=-\frac{25}{48}+\frac{10}{48}=-\frac{15}{48}=-\frac5{16}.
\tag{11.1}
\]

Thus

\[
\Delta_{SU(3)}(\beta)
=
\sqrt{\frac{2\beta}{3}}
-\frac5{16}
+O(\beta^{-1/2}).
\]

---

## 12. Second correction \(c_1\)

The \(\beta^{-1/2}\) coefficient has two contributions:

1. the second-order Rayleigh--Schrödinger resolvent leakage from \(H_1\);
2. the first-order expectation difference of \(H_2\).

### 12.1 Resolvent leakage

The second-order leakage contribution is

\[
\Delta_{\rm res}
=
\sum_{m\neq1}
\frac{|\langle \psi_m,H_1\psi_1\rangle|^2}{E_1^{(0)}-E_m^{(0)}}
-
\sum_{m\neq0}
\frac{|\langle \psi_m,H_1\psi_0\rangle|^2}{E_0^{(0)}-E_m^{(0)}}.
\tag{12.1}
\]

The exact file ledger gives

\[
\boxed{
\Delta_{\rm res}=-\frac{205\sqrt6}{3072}.
}
\tag{12.2}
\]

### 12.2 Intrinsic \(H_2\) contribution

The direct curvature contribution is

\[
\Delta_{H_2}
=
\langle H_2\rangle_1-\langle H_2\rangle_0.
\tag{12.3}
\]

The full Weyl-invariant calculation, retaining \(p_3^2\), gives

\[
\boxed{
\Delta_{H_2}=\frac{19\sqrt6}{576}.
}
\tag{12.4}
\]

### 12.3 Combine denominators

Use denominator \(9216\):

\[
-\frac{205\sqrt6}{3072}
=
-\frac{615\sqrt6}{9216}.
\]

Also,

\[
\frac{19\sqrt6}{576}
=
\frac{304\sqrt6}{9216}.
\]

Therefore,

\[
c_1
=
\Delta_{\rm res}+\Delta_{H_2}
=
-\frac{615\sqrt6}{9216}
+
\frac{304\sqrt6}{9216}
=
-\frac{311\sqrt6}{9216}.
\tag{12.5}
\]

Hence the three-term SU(3) local class-function gap is

\[
\boxed{
\Delta_{SU(3)}(\beta)
=
\sqrt{\frac{2\beta}{3}}
-
\frac5{16}
-
\frac{311\sqrt6}{9216}\beta^{-1/2}
+
O(\beta^{-1}).
}
\tag{12.6}
\]

This is a local spectral theorem, not a four-dimensional Yang--Mills mass-gap proof.

---

## 13. Finite-channel leakage matrix

The SU(3) finite-channel ledger gives leakage amplitudes

\[
|0\to1|=\frac5{24},
\qquad
|0\to2|=\frac{\sqrt{10}}{48},
\]

\[
|1\to2|=\frac{7\sqrt{10}}{48},
\qquad
|1\to3|=\frac{\sqrt5}{16}.
\]

These define

\[
T=
\begin{pmatrix}
0 & \frac5{24} & \frac{\sqrt{10}}{48} & 0\\
\frac5{24} & 0 & \frac{7\sqrt{10}}{48} & \frac{\sqrt5}{16}\\
\frac{\sqrt{10}}{48} & \frac{7\sqrt{10}}{48} & 0 & 0\\
0 & \frac{\sqrt5}{16} & 0 & 0
\end{pmatrix}.
\tag{13.1}
\]

Its Perron root satisfies the quartic equation

\[
x^4-\frac{215}{768}x^2-\frac{175}{13824}x+\frac{25}{294912}=0.
\tag{13.2}
\]

The file reports

\[
\rho_3=0.550161533523142580684435405428\ldots.
\tag{13.3}
\]

This number is the local finite-channel leakage constant.

---

## 14. Polymer-resolvent threshold

Let \(\mu_{\mathcal G}\) be the growth constant of the plaquette-overlap graph. The finite-channel polymer expansion has per-step degradation roughly

\[
\frac{\rho(T)}{\sqrt{2\beta/3}}.
\]

Graph growth introduces \(\mu_{\mathcal G}\). The basic summability condition is

\[
\boxed{
\mu_{\mathcal G}\frac{\rho(T)}{\sqrt{2\beta/3}}<1.
}
\tag{14.1}
\]

For stronger Schur summability, one needs

\[
m_{\rm poly}
=
\log\left(
\frac{\sqrt{2\beta/3}}
{\mu_{\mathcal G}\rho(T)}
\right)
>
\log\mu_{\mathcal G}.
\tag{14.2}
\]

Exponentiating,

\[
\frac{\sqrt{2\beta/3}}{\mu_{\mathcal G}\rho(T)}
>
\mu_{\mathcal G}.
\]

Thus

\[
\sqrt{\frac{2\beta}{3}}
>
\mu_{\mathcal G}^2\rho(T).
\]

Squaring,

\[
\frac{2\beta}{3}
>
\mu_{\mathcal G}^4\rho(T)^2.
\]

Therefore,

\[
\boxed{
\beta>
\frac32\mu_{\mathcal G}^4\rho(T)^2.
}
\tag{14.3}
\]

For \(\mu_{\mathcal G}=3\), the file gives

\[
\boxed{
\beta>36.77534212567712.
}
\tag{14.4}
\]

This is a conditional finite-channel/Poincaré bridge threshold, not an unconditional lattice Yang--Mills theorem.

---

## 15. SU(N) extension program

The SU(N) finite-channel generalization is explicit.

Use invariant polynomials

\[
\prod_{k=2}^{N}p_k^{m_k}
\]

up to shell degree \(D\). Orthonormalize them under the SU(N) Weyl-Gaussian measure. Construct the nonnegative channel matrix

\[
T^{(N)}_{ab}
=
|\langle \psi_a,H_1^{SU(N)}\psi_b\rangle_N|.
\]

Compute or bound

\[
\rho_N:=\rho(T^{(N)}).
\]

The finite-channel bridge survives if

\[
\boxed{
\mu_{\mathcal G}\frac{\rho_N}{\sqrt{2\beta/N}}<1.
}
\tag{15.1}
\]

Equivalently,

\[
\boxed{
\beta>\frac{N}{2}\mu_{\mathcal G}^2\rho_N^2.
}
\tag{15.2}
\]

For Schur/Poincaré summability,

\[
\boxed{
\beta>\frac{N}{2}\mu_{\mathcal G}^4\rho_N^2.
}
\tag{15.3}
\]

This is a real SU(N) research program:

\[
\boxed{
\text{Weyl invariant oscillator algebra}
\Longrightarrow
T^{(N)}
\Longrightarrow
\rho_N
\Longrightarrow
\text{polymer threshold}.
}
\]

---

# Part III — Integration: what belongs in which paper

---

## 16. PMBSF/SU(2) paper

The PMBSF paper should be framed as:

\[
\boxed{
\text{Lemma Q + source-weighted Bałaban expansion + boundary-band gate}
\Rightarrow
\text{SU(2) projected-capacity firewall}.
}
\]

The proof chain is:

\[
\text{Lemma Q}
\Rightarrow
\text{rooted source cumulants}
\Rightarrow
\text{pair/rooted closure}
\Rightarrow
\text{PTO level-(iii)}
\Rightarrow
\text{HPM}
\Rightarrow
\text{matrix-Laplace / random plaquette-incidence transfer}
\Rightarrow
\text{projected firewall}.
\]

The numerical section should contain:

1. exact heat-bath side-8 Lemma Q anchor;
2. Stage B side-10 geometry supplement;
3. L12/L16 and L64 pair/rooted consequence evidence;
4. v3b projected BS firewall certificate;
5. random plaquette-incidence comparator diagnostics;
6. explicit status table separating proved / conditional / numerical / open.

### Manuscript-safe PMBSF claim

Use:

> We reduce projected SU(2) lattice Yang--Mills coercivity in a fixed spectral window to a local rare-source factorization theorem, Lemma Q, plus a source-weighted Bałaban expansion and a boundary-band hard-threshold bridge. The deterministic projected-capacity spine and Bernoulli plaquette-incidence comparator are unconditional. Exact heat-bath frozen-exterior diagnostics and full-volume pair/rooted covariance diagnostics provide finite-volume evidence for the required \(q_\eta\)-per-source mechanism.

Do not use:

> We prove the SU(2) Yang--Mills mass gap.

---

## 17. SU(3) paper

The SU(3) class-function paper should be separate.

Core theorem:

\[
\Delta_{SU(3)}(\beta)
=
\sqrt{\frac{2\beta}{3}}
-
\frac5{16}
-
\frac{311\sqrt6}{9216}\beta^{-1/2}
+
O(\beta^{-1}).
\]

Main derivational novelty:

\[
\boxed{
H_2\text{ contains the non-radial invariant }p_3^2.
}
\]

Finite-channel extension:

\[
T^{(3)}
=
\begin{pmatrix}
0 & \frac5{24} & \frac{\sqrt{10}}{48} & 0\\
\frac5{24} & 0 & \frac{7\sqrt{10}}{48} & \frac{\sqrt5}{16}\\
\frac{\sqrt{10}}{48} & \frac{7\sqrt{10}}{48} & 0 & 0\\
0 & \frac{\sqrt5}{16} & 0 & 0
\end{pmatrix},
\]

\[
\rho_3=0.55016153352314258\ldots,
\]

and

\[
\beta>\frac32\mu_{\mathcal G}^4\rho_3^2.
\]

For \(\mu_{\mathcal G}=3\),

\[
\beta>36.77534212567712.
\]

### Manuscript-safe SU(3) claim

Use:

> We prove a local SU(3) one-plaquette class-function asymptotic gap law and derive an exact finite-channel leakage matrix controlling a conditional polymer-resolvent bridge.

Do not use:

> This proves the four-dimensional SU(3) Yang--Mills mass gap.

---

# 18. What is missing for Clay-level closure

The current derivations are important but not Clay-complete. Missing:

1. Unconditional Lemma Q / block source-stability.
2. Source-weighted Bałaban expansion with \(q_\eta^{|B|}\) source accounting.
3. Boundary-band bridge \(\eta\to0\).
4. Infinite-volume construction.
5. Continuum limit \(a\to0,\ \beta(a)\to\infty\).
6. Osterwalder--Schrader/Wightman reconstruction.
7. Strict positive physical mass gap in the reconstructed continuum Hilbert space.
8. Nontriviality of the continuum theory.
9. General compact simple gauge group coverage.

The next analytic theorem is therefore:

\[
\boxed{
\lambda_p(S\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(\sum_{r\in S}J(p,r)\right),
\qquad
J(p,r)\le Ce^{-md_C(p,r)}.
}
\]

and rooted:

\[
\boxed{
\lambda^Y_p(S\mid\mathcal F_{C^c})
\le
q_\eta
\exp\left(J(p,p_0)+\sum_{r\in S}J(p,r)\right).
}
\]

This is the next real proof target.

---

# 19. Stopping point

The right current stopping point is:

\[
\boxed{
\text{stop numerics, write two papers.}
}
\]

1. PMBSF/SU(2): conditional projected-capacity framework + Lemma Q evidence.
2. SU(3): local Weyl-invariant class-function gap + finite-channel bridge.

The L64 and SU3 claims are real; the critique that questioned them was a context-access failure. But the critique was right that the paper must integrate the master spine, operator-norm pillar, and honest status table rather than presenting a thin outline.
