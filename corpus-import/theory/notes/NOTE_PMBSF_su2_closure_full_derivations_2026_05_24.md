# SU(2) Closure Derivations for the PMBSF Projected-Capacity Firewall Program

**Document date:** 2026-05-24  
**Status:** Manuscript derivation draft. Not a proof of the Yang--Mills mass gap.  
**Purpose:** Collect the SU(2)-specific derivation stack needed to close the Wilson high-plaquette transfer input in the PMBSF projected-capacity firewall program.

---

## 0. Executive summary

The PMBSF deterministic and Bernoulli parts are already structurally complete:

\[
A_p=P_{\le\Lambda,L}\mathbf 1_{\partial p}P_{\le\Lambda,L},
\qquad
\sum_pA_p=6P,
\qquad
A_p^2\preceq \kappa_\Lambda A_p,
\]

and therefore for iid Bernoulli plaquette defects,

\[
\|P\mathbf1_{D(B)}P\|
\le
6q+
\sqrt{12q\kappa_\Lambda\log(2K/\delta)}
+
\frac{2\kappa_\Lambda}{3}\log(2K/\delta).
\]

The missing SU(2) input is the hard-plaquette closed-walk/HPM transfer:

\[
\text{SU(2) Wilson high plaquettes}
\Longrightarrow
\text{random/block plaquette-incidence closed-walk domination}.
\]

The shortest viable analytic closure route is:

\[
\boxed{
\mathrm{BS}_{\rm smooth}
+
\mathrm{BG}_{\eta\to0}
+
\mathrm{CWKP}
\Longrightarrow
\mathrm{HPM}
\Longrightarrow
\mathrm{ML}_{\rm sparse}
\Longrightarrow
\Theta<1.
}
\]

The core theorem still to prove is the **rooted-source polymer estimate**

\[
\boxed{
|K_\eta(\Gamma;s_0,\ldots,s_k)|
\le
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}
\mathbb E_WY_{p_0}
q_\eta^k
\prod_{j=0}^k|s_j|.
}
\tag{0.1}
\]

Everything in this document proves what follows from (0.1).

---

## 1. SU(2) Wilson setup

Work on a periodic four-dimensional lattice

\[
T_L^4=(\mathbb Z/L\mathbb Z)^4.
\]

For SU(2), write a group element as a unit quaternion

\[
U=a_0\mathbf 1+i\sum_{j=1}^3a_j\sigma_j,
\qquad
a=(a_0,a_1,a_2,a_3)\in S^3.
\]

Then

\[
\frac12\operatorname{ReTr}(U)=a_0.
\]

For a plaquette \(p\), define the defect score

\[
\phi_p(U):=
1-\frac12\operatorname{ReTr}(U_p).
\]

The hard high-plaquette indicator is

\[
X_p(U):=\mathbf1\{\phi_p(U)\ge t\}.
\]

For analysis, replace \(X_p\) with a smooth source

\[
X_{p,\eta}(U):=f_\eta(\phi_p(U)-t),
\]

where

\[
0\le f_\eta\le1,
\]

\[
f_\eta(s)=0\quad(s\le-\eta),
\]

\[
f_\eta(s)=1\quad(s\ge\eta).
\]

Define

\[
q_\eta:=\mathbb E_WX_{p,\eta}.
\]

The fixed-\(\eta\) closure theorem should be proved first. The hard limit \(\eta\downarrow0\) is a later boundary-band problem.

---

## 2. Target SU(2) theorem

### Theorem target: rooted-source polymer bound

Let \(Y_{p_0}\) be a local bounded observable supported in a fixed-radius neighborhood of \(p_0\), satisfying

\[
0\le Y_{p_0}\le X_{p_0,\eta}.
\]

Let \(p_1,\ldots,p_k\) be other plaquettes. Introduce source parameters \(s_0,\ldots,s_k\), and define the connected source pressure

\[
\Psi(s_0,\ldots,s_k)
=
\log\mathbb E_W
\exp\left(
s_0Y_{p_0}+\sum_{j=1}^ks_jX_{p_j,\eta}
\right)
-
\text{all disconnected one/source-block pressures}.
\]

The desired polymer expansion is

\[
\Psi(s_0,\ldots,s_k)
=
\sum_{\Gamma\leadsto p_0,\ldots,p_k}
K_\eta(\Gamma;s_0,\ldots,s_k),
\]

with activity bound

\[
\boxed{
|K_\eta(\Gamma;s_0,\ldots,s_k)|
\le
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}
\mathbb E_WY_{p_0}
q_\eta^k
\prod_{j=0}^k|s_j|.
}
\tag{2.1}
\]

If (2.1) is proved, the PMBSF stochastic transfer closes, modulo the hard/smooth boundary-band passage.

---

## 3. Theorem F: rooted-source polymer expansion implies centered rare-source mixing

### 3.1 Statement

Let \(Y_p\) be local and satisfy

\[
0\le Y_p\le X_{p,\eta}.
\]

Assume the two-source connected pressure

\[
\Psi_{p,p'}(s,t)
=
\log\mathbb E_W e^{sY_p+tX_{p',\eta}}
-
\log\mathbb E_W e^{sY_p}
-
\log\mathbb E_W e^{tX_{p',\eta}}
\]

has a polymer expansion

\[
\Psi_{p,p'}(s,t)
=
\sum_{\Gamma\leadsto p,p'}K_\eta(\Gamma;s,t)
\]

with

\[
|K_\eta(\Gamma;s,t)|
\le
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}
|s||t|\,
\mathbb E_WY_p\,
q_\eta.
\]

Assume also

\[
\sum_{\Gamma\leadsto p,p'}
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}
\le
C_{\rm conn}e^{-m d(p,p')}.
\]

Then

\[
\boxed{
|\operatorname{Cov}_W(Y_p,X_{p',\eta})|
\le
C_{\rm root}\,
\mathbb E_WY_p\,
q_\eta\,
e^{-m d(p,p')}.
}
\tag{3.1}
\]

### 3.2 Proof

By definition of the connected pressure,

\[
\partial_s\partial_t\Psi_{p,p'}(0,0)
=
\operatorname{Cov}_W(Y_p,X_{p',\eta}).
\]

Choose \(0<r\le r_0\). By Cauchy's formula on the bidisc \(|s|=|t|=r\),

\[
|\partial_s\partial_t\Psi_{p,p'}(0,0)|
\le
\frac1{r^2}
\sup_{|s|=|t|=r}
|\Psi_{p,p'}(s,t)|.
\]

By the polymer expansion and activity bound,

\[
|\Psi_{p,p'}(s,t)|
\le
\sum_{\Gamma\leadsto p,p'}
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}
|s||t|\,
\mathbb E_WY_p\,
q_\eta.
\]

For \(|s|=|t|=r\),

\[
|\Psi_{p,p'}(s,t)|
\le
r^2\mathbb E_WY_pq_\eta
\sum_{\Gamma\leadsto p,p'}
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}.
\]

Apply connected summability:

\[
|\Psi_{p,p'}(s,t)|
\le
r^2C_{\rm conn}
\mathbb E_WY_pq_\eta
e^{-md(p,p')}.
\]

Therefore

\[
|\operatorname{Cov}_W(Y_p,X_{p',\eta})|
\le
C_{\rm conn}
\mathbb E_WY_pq_\eta
e^{-md(p,p')}.
\]

Set \(C_{\rm root}:=C_{\rm conn}\). This proves (3.1). \(\square\)

---

## 4. Pair closure

Take

\[
Y_p=X_{p,\eta}.
\]

Then

\[
\mathbb E_WY_p=q_\eta.
\]

Theorem F gives

\[
\boxed{
|\operatorname{Cov}_W(X_{p,\eta},X_{p',\eta})|
\le
C_{\rm root}q_\eta^2e^{-md(p,p')}.
}
\tag{4.1}
\]

This is the fixed-\(\eta\) smooth pair closure.

---

## 5. PTO-summed level-(iii) estimate

Let

\[
A_p=P_{\le\Lambda,L}\mathbf1_{\partial p}P_{\le\Lambda,L}.
\]

Assume the deterministic trace-overlap summability

\[
\sup_p
\sum_{p'}
e^{-m d(p,p')}
\frac{\operatorname{tr}(A_pA_{p'})}{\kappa_\Lambda^2}
\le
4N_m.
\tag{5.1}
\]

Then (4.1) implies

\[
\boxed{
\sum_{p'}
|\operatorname{Cov}_W(X_{p,\eta},X_{p',\eta})|
\operatorname{tr}(A_pA_{p'})
\le
4C_{\rm root}N_mq_\eta^2\kappa_\Lambda^2.
}
\tag{5.2}
\]

### Proof

Using (4.1),

\[
\begin{aligned}
\sum_{p'}
|\operatorname{Cov}_W(X_{p,\eta},X_{p',\eta})|
\operatorname{tr}(A_pA_{p'})
&\le
C_{\rm root}q_\eta^2
\sum_{p'}
e^{-md(p,p')}
\operatorname{tr}(A_pA_{p'})\\
&\le
4C_{\rm root}N_mq_\eta^2\kappa_\Lambda^2.
\end{aligned}
\]

This proves (5.2). \(\square\)

This is the projected level-(iii) form of \((M')_{\rm SU(2)}\) at fixed \(\eta\).

---

## 6. SU(2) heat-bath law

The rooted-source estimate is abstract. The SU(2)-specific input starts with the exact one-link heat-bath law.

Fix a link \(\ell\), and condition on all links except \(U_\ell\). The Wilson action terms containing \(U_\ell\) collect into a staple vector

\[
H_\ell\in\mathbb R^4.
\]

Writing \(x=U_\ell\in S^3\), the conditional density is

\[
\boxed{
d\nu_H(x)
=
Z(H)^{-1}
e^{\beta H\cdot x}
d\sigma_{S^3}(x).
}
\tag{6.1}
\]

Thus the one-link conditional law is von-Mises--Fisher on \(S^3\).

For a plaquette \(p\ni\ell\), after freezing the other three boundary links, there is a unit quaternion \(c_p\in S^3\) such that

\[
\phi_p(x)=1-c_p\cdot x.
\]

The smoothed event \(X_{p,\eta}\) is supported in

\[
c_p\cdot x\le a_\eta,
\qquad
a_\eta:=1-t+\eta.
\]

Let

\[
\kappa:=\beta|H|,
\qquad
\widehat H:=H/|H|,
\qquad
\rho:=\widehat H\cdot c_p.
\]

---

## 7. vMF cap rarity

### Lemma 7.1

Let \(x\in S^3\) have density

\[
d\nu_H(x)=Z(\kappa)^{-1}e^{\kappa\widehat H\cdot x}d\sigma(x),
\qquad \kappa\ge1.
\]

If

\[
\rho=\widehat H\cdot c>a,
\]

then

\[
\boxed{
\nu_H(c\cdot x\le a)
\le
C_{S^3}\kappa^{3/2}
e^{-\kappa\Delta(\rho,a)},
}
\tag{7.1}
\]

where

\[
\Delta(\rho,a)
=
1-\rho a-\sqrt{1-\rho^2}\sqrt{1-a^2}.
\]

### Proof

On the cap \(c\cdot x\le a\), the maximum of \(\widehat H\cdot x\) is

\[
M(\rho,a)=\rho a+\sqrt{1-\rho^2}\sqrt{1-a^2}
=1-\Delta(\rho,a).
\]

Thus

\[
\int_{c\cdot x\le a}
e^{\kappa\widehat H\cdot x}d\sigma(x)
\le
|S^3|e^{\kappa(1-\Delta)}.
\]

The vMF normalizer has the Laplace lower bound

\[
Z(\kappa)
\ge
c_{S^3}\kappa^{-3/2}e^\kappa.
\]

Therefore

\[
\nu_H(c\cdot x\le a)
\le
\frac{|S^3|e^{\kappa(1-\Delta)}}
{c_{S^3}\kappa^{-3/2}e^\kappa}
=
C_{S^3}\kappa^{3/2}e^{-\kappa\Delta}.
\]

\(\square\)

---

## 8. Good-staple rarity and bad-staple source

Define the good-staple event

\[
\mathcal G_{\ell,p}(\rho_0,h_0)
=
\{|H_\ell|\ge h_0,\ \widehat H_\ell\cdot c_p\ge\rho_0\}.
\]

Assume

\[
\rho_0>a_\eta.
\]

On \(\mathcal G_{\ell,p}\), Lemma 7.1 gives

\[
\mathbb E[X_{p,\eta}\mid\mathcal F_{\ell^c}]
\le
C_{S^3}(6\beta)^{3/2}
e^{-\beta h_0\Delta(\rho_0,a_\eta)}.
\]

If

\[
C_{S^3}(6\beta)^{3/2}
e^{-\beta h_0\Delta(\rho_0,a_\eta)}
\le
C_{\rm hb}q_\eta,
\tag{8.1}
\]

then

\[
\mathbb E[X_{p,\eta}\mathbf1_{\mathcal G_{\ell,p}}\mid\mathcal F_{\ell^c}]
\le
C_{\rm hb}q_\eta.
\]

Define the bad-staple event

\[
\mathcal B_{\ell,p}:=\mathcal G_{\ell,p}^c.
\]

The naive bound

\[
\mathbb E[X_{p,\eta}\mid\mathcal F_{\ell^c}]
\le
C_{\rm hb}q_\eta+\mathbf1_{\mathcal B_{\ell,p}}
\]

is true but not sufficient. The scalar attempt to show \(\mathcal B_{\ell,p}\) is itself \(q_\eta\)-rare fails in general because the induced defect threshold is too low.

The corrected object is the rooted bad-staple source

\[
\boxed{
R_{p,\ell,\eta}
:=
X_{p,\eta}\mathbf1_{\mathcal B_{\ell,p}}.
}
\tag{8.2}
\]

It satisfies

\[
0\le R_{p,\ell,\eta}\le X_{p,\eta},
\]

hence

\[
\mathbb E_WR_{p,\ell,\eta}\le q_\eta.
\]

Therefore Theorem F applies to \(R_{p,\ell,\eta}\).

---

## 9. Bad-staple absorption without the false scalar tail ratio

Applying Theorem F to

\[
Y_p=R_{p,\ell,\eta}
\]

gives

\[
|\operatorname{Cov}_W(R_{p,\ell,\eta},X_{p',\eta})|
\le
C_{\rm root}
\mathbb E_WR_{p,\ell,\eta}
q_\eta
e^{-md(p,p')}.
\]

Since

\[
\mathbb E_WR_{p,\ell,\eta}\le q_\eta,
\]

we obtain

\[
\boxed{
|\operatorname{Cov}_W(R_{p,\ell,\eta},X_{p',\eta})|
\le
C_{\rm root}q_\eta^2e^{-md(p,p')}.
}
\tag{9.1}
\]

This is the correct bad-staple absorption. It avoids the false requirement

\[
\mathbb P(\phi_p>\delta_{\rm st})\lesssim \mathbb P(\phi_p>t),
\]

which generally fails if \(\delta_{\rm st}\ll t\).

---

## 10. Higher cumulants and HPM

The two-source theorem has a higher-source analogue. Let

\[
Y_{p_0}\le X_{p_0,\eta}
\]

be rooted, and let \(p_1,\ldots,p_k\) be additional plaquettes. The target estimate is

\[
\boxed{
\left|
\kappa_W
\left(
Y_{p_0},
X_{p_1,\eta},
\ldots,
X_{p_k,\eta}
\right)
\right|
\le
C^k
\mathbb E_WY_{p_0}
q_\eta^k
e^{-m\tau(\{p_0,\ldots,p_k\})}.
}
\tag{10.1}
\]

Taking \(Y_{p_0}=X_{p_0,\eta}\) gives

\[
\left|
\kappa_W
\left(
X_{p_0,\eta},
X_{p_1,\eta},
\ldots,
X_{p_k,\eta}
\right)
\right|
\le
C^kq_\eta^{k+1}
e^{-m\tau(\{p_0,\ldots,p_k\})}.
\]

This is the fixed-\(\eta\) level-(iv) cumulant theorem needed for smooth HPM.

---

## 11. Smooth HPM from cumulants

Let

\[
\mathcal W_\theta(Y)
\]

be the PMBSF closed-walk weight

\[
\mathcal W_\theta(Y)
=
\sum_{n\ge2}\frac{\theta^n}{n!}
\sum_{\{p_1,\ldots,p_n\}=Y}
\prod_j
\sqrt{\operatorname{tr}(A_{p_j}A_{p_{j+1}})}.
\]

Assume the cumulant bound

\[
|\kappa_\eta(B)|
\le
q_\eta^{|B|}\nu(B),
\qquad
\nu(B)\le C_*^{|B|}e^{-m_*\tau(B)}.
\]

If the closed-walk KP condition holds,

\[
\sum_Y q_\eta^{|Y|}
\left[
\exp\left(
\sum_{\substack{B\subset Y\\|B|\ge2}}\nu(B)
\right)-1
\right]
\mathcal W_\theta(Y)
\le
\varepsilon_{\rm CWKP}
\sum_Yq_\eta^{|Y|}\mathcal W_\theta(Y),
\tag{11.1}
\]

then

\[
\boxed{
\sum_Y
\mathbb E_W\prod_{p\in Y}X_{p,\eta}\,
\mathcal W_\theta(Y)
\le
(1+\varepsilon_{\rm CWKP})
\sum_Yq_\eta^{|Y|}\mathcal W_\theta(Y).
}
\tag{11.2}
\]

### Proof

For fixed \(Y\), use the moment-cumulant formula:

\[
\mathbb E_W\prod_{p\in Y}X_{p,\eta}
=
\sum_{\pi\in\Pi(Y)}
\prod_{B\in\pi}\kappa_\eta(B).
\]

Singleton cumulants equal \(q_\eta\). Therefore

\[
\left|
\mathbb E_W\prod_{p\in Y}X_{p,\eta}
\right|
\le
q_\eta^{|Y|}
\sum_{\pi\in\Pi(Y)}
\prod_{\substack{B\in\pi\\|B|\ge2}}\nu(B).
\]

The partition sum is bounded by

\[
\exp\left(
\sum_{\substack{B\subset Y\\|B|\ge2}}\nu(B)
\right).
\]

Thus

\[
\mathbb E_W\prod_{p\in Y}X_{p,\eta}
\le
q_\eta^{|Y|}
\exp\left(
\sum_{\substack{B\subset Y\\|B|\ge2}}\nu(B)
\right).
\]

Multiply by \(\mathcal W_\theta(Y)\), sum over \(Y\), and apply (11.1). This proves (11.2). \(\square\)

---

## 12. Hard/smooth boundary-band bridge

To pass from \(X_{p,\eta}\) to hard indicators

\[
X_p=\mathbf1\{\phi_p\ge t\},
\]

define the boundary-band event

\[
B_{\eta,p}:=\mathbf1\{|\phi_p-t|\le\eta\}.
\]

Since \(X_p\) and \(X_{p,\eta}\) differ only in the boundary band,

\[
|X_p-X_{p,\eta}|
\le
B_{\eta,p}.
\]

For a finite set \(Y\),

\[
\left|
\prod_{p\in Y}X_p
-
\prod_{p\in Y}X_{p,\eta}
\right|
\le
\sum_{r\in Y}B_{\eta,r}.
\]

The required bridge is the closed-walk weighted estimate

\[
\boxed{
\sum_Y
\mathbb E_W
\left[
\sum_{r\in Y}B_{\eta,r}
\right]
\mathcal W_\theta(Y)
\le
\varepsilon_{\rm bdry}(\eta)
\sum_Yq^{|Y|}\mathcal W_\theta(Y),
\qquad
\varepsilon_{\rm bdry}(\eta)\to0.
}
\tag{12.1}
\]

If (12.1) holds, then hard HPM follows from smooth HPM with loss \(\varepsilon_{\rm bdry}(\eta)\).

---

## 13. HPM to matrix-Laplace transfer

Let

\[
S_W(U)=\sum_pX_p(U)A_p
\]

and let \(S_R\) be the random plaquette-incidence comparator. HPM gives

\[
\mathbb E_W\operatorname{tr}e^{\theta S_W}
\le
C_0\mathbb E_R\operatorname{tr}e^{\theta S_R}.
\tag{13.1}
\]

Then, for any \(s>0\),

\[
\mathbb P_W(\lambda_{\max}S_W\ge s)
\le
e^{-\theta s}
\mathbb E_W\operatorname{tr}e^{\theta S_W}
\le
C_0e^{-\theta s}
\mathbb E_R\operatorname{tr}e^{\theta S_R}.
\]

Optimizing over \(\theta\) transfers the Bernoulli Bernstein bound to Wilson with the tail logarithm shifted by \(\log C_0\):

\[
\boxed{
\|P\mathbf1_{D_W}P\|
\le
6q+
\sqrt{12q\kappa_\Lambda\log(2C_0K/\varepsilon)}
+
\frac{2\kappa_\Lambda}{3}\log(2C_0K/\varepsilon)
+
o_L(1).
}
\tag{13.2}
\]

---

## 14. Projected firewall

Define the Birman--Schwinger parameter

\[
\Theta
=
\frac{V_{\max}}{m^2}
\|P\mathbf1_D P\|.
\]

If

\[
\boxed{
\frac{V_{\max}}{m^2}
\left[
6q+
\sqrt{12q\kappa_\Lambda\log(2C_0K/\varepsilon)}
+
\frac{2\kappa_\Lambda}{3}\log(2C_0K/\varepsilon)
\right]
<1,
}
\tag{14.1}
\]

then

\[
\Theta<1
\]

with Wilson probability at least \(1-\varepsilon-o_L(1)\).

The defect-patched projected operator is then coercive:

\[
M-V
=
M^{1/2}(I-K)M^{1/2}
\succeq
(1-\Theta)M.
\]

This is the PMBSF projected finite-volume firewall.

---

## 15. Honest status

The derivations above prove the implications:

\[
\text{rooted-source polymer expansion}
\Rightarrow
\text{centered rare-source mixing}
\Rightarrow
\text{pair closure}
\Rightarrow
\text{PTO level-(iii)}
\Rightarrow
\text{smooth HPM}
\Rightarrow
\text{hard HPM}
\Rightarrow
\text{projected firewall}.
\]

What remains to prove analytically is the SU(2)-specific rooted-source polymer estimate

\[
|K_\eta(\Gamma;s_0,\ldots,s_k)|
\le
C_0^{|\Gamma|}
e^{-m_0\tau(\Gamma)}
\mathbb E_WY_{p_0}
q_\eta^k
\prod_{j=0}^k|s_j|.
\]

This is not currently supplied by the peer-reviewed literature for SU(2) at large \(\beta\). The closest structural technologies are Bałaban's lattice gauge RG and related constructive cluster expansions, but the current literature does not provide the fixed-\(\beta\), projected spectral-window, hard/smooth plaquette-source cumulant theorem required here.

Thus the document's final status is:

\[
\boxed{
\text{The PMBSF SU(2) closure is reduced to a precise rooted-source polymer theorem.}
}
\]

It is not yet an unconditional Yang--Mills mass-gap proof.

---

## 16. Minimal next proof target

The smallest theorem worth attacking next is the fixed-\(\eta\) pair source estimate:

\[
\boxed{
|\operatorname{Cov}_W(X_{p,\eta},X_{p',\eta})|
\le
Cq_\eta^2e^{-md(p,p')}.
}
\]

By the derivations above, this immediately gives

\[
\boxed{
\sum_{p'}
|\operatorname{Cov}_W(X_{p,\eta},X_{p',\eta})|
\operatorname{tr}(A_pA_{p'})
\le
Cq_\eta^2\kappa_\Lambda^2.
}
\]

This is the first real SU(2) breach point.
