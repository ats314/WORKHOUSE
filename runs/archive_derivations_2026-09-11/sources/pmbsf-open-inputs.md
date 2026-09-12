# 14. Remaining analytic tasks

## 14.1 Purpose of this section

The preceding sections identify the conditional proof interface:

\[
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Longrightarrow
\mathrm{TOS+J}
\Longrightarrow
Z_A(\rho/q_\eta)\le e^{K|A|}
\Longrightarrow
\mathrm{Lemma\ Q}.
\tag{14.1}
\]

The downstream projected-capacity closure requires

\[
\mathrm{Lemma\ Q}
+
\mathrm{SWB}
+
\mathrm{BBG}
+
\mathrm{PTO}
+
\mathrm{BS}
\Longrightarrow
\mathrm{PMBSF\ firewall\ closure}.
\tag{14.2}
\]

The deterministic pieces have been isolated. The remaining work is analytic and probabilistic. This section lists the open tasks in the order in which they should be attacked.

The four load-bearing open inputs are:

\[
\boxed{
\mathrm{A}:\ \mathrm{LCI}_{\rm good}\text{ typicality with rooted complement}
}
\tag{14.3}
\]

\[
\boxed{
\mathrm{B}:\ \mathrm{BFS}_{\rm far}\text{ under positive source tilts}
}
\tag{14.4}
\]

\[
\boxed{
\mathrm{C}:\ \mathrm{SWB}\text{ source-weighted Bałaban expansion}
}
\tag{14.5}
\]

\[
\boxed{
\mathrm{D}:\ \mathrm{BBG}\text{ boundary-band gate as }\eta\to0.
}
\tag{14.6}
\]

The correct order is not arbitrary. The first target is the local finite-dimensional LCI theorem, because it is the smallest standalone analytic problem and the most isolated from the full constructive RG machinery. The second target is far-source stability, because it is the missing bridge from local geometry to TOS+J. The third target is the full source-weighted polymer expansion. The fourth target is the hard-source limit.

## 14.2 Open Theorem A: local cap-intersection typicality

### Statement

For a heat-bath link \(e\) and target plaquette \(p\ni e\), the exact one-link conditional law is

\[
\nu_e(du)
=
Z_4(\kappa_e)^{-1}
e^{\kappa_e m_e\cdot u}\,d\sigma_{S^3}(u),
\tag{14.7}
\]

and every incident source satisfies

\[
X_{r,\eta}(u)
\le
\mathbf1_{\{u\cdot n_r\le a\}},
\qquad
a=1-(t-\eta).
\tag{14.8}
\]

For

\[
A\subset I(e)\setminus\{p\},
\]

define

\[
C_A=\bigcap_{r\in A}\{u\in S^3:u\cdot n_r\le a\}.
\tag{14.9}
\]

The local LCI theorem asks for

\[
\boxed{
\nu_e(C_p\cap C_A)
\le
C_{\rm LCI}q_\eta\,\nu_e(C_A)
\quad
\forall A\subset I(e)\setminus\{p\},
}
\tag{14.10}
\]

on a Wilson-typical local good event \(\mathcal G_{e,p}^{\rm LCI}\), with bad complement rooted:

\[
Y_p^{\rm LCI}
=
X_{p,\eta}\mathbf1_{(\mathcal G_{e,p}^{\rm LCI})^c}.
\tag{14.11}
\]

Equivalently, in smooth-source form, the theorem should prove

\[
\boxed{
\int X_p\prod_{r\in A}X_r\,d\nu_e
\le
C_{\rm LCI}q_\eta
\int\prod_{r\in A}X_r\,d\nu_e
}
\tag{14.12}
\]

for every incident subset \(A\).

### Subtask A1: deterministic finite-dimensional cap theorem

For fixed data

\[
\mathcal D_e=(m_e,\kappa_e,\{n_r\}_{r\in I(e)},a),
\tag{14.13}
\]

prove that a computable support-loss certificate implies (14.10). The certificate should use

\[
h_A=\sup_{u\in C_A}m_e\cdot u,
\tag{14.14}
\]

\[
h_{A,p}=\sup_{u\in C_A\cap C_p}m_e\cdot u,
\tag{14.15}
\]

and

\[
\Delta_A(p)=h_A-h_{A,p}.
\tag{14.16}
\]

A sufficient bound is

\[
\boxed{
\nu_e(C_p\cap C_A)
\le
\Gamma_{\rm pref}
e^{-\kappa_e\Delta_A(p)}
\nu_e(C_A),
}
\tag{14.17}
\]

with calibration

\[
\boxed{
\Gamma_{\rm pref}
e^{-\kappa_e\Delta_A(p)}
\le
C_{\rm LCI}q_\eta.
}
\tag{14.18}
\]

The finite-dimensional proof must handle all active-set configurations in the KKT system

\[
m_e=\lambda u_A+\sum_{r\in K}\alpha_r n_r,
\qquad
\alpha_r\ge0,
\tag{14.19}
\]

where

\[
K\subset A,
\qquad
u_A\cdot n_r=a\quad(r\in K).
\tag{14.20}
\]

Because

\[
|I(e)\setminus\{p\}|\le5,
\]

there are only finitely many active sets. This subtask is genuinely finite-dimensional.

### Subtask A2: smooth-source upgrade

The cap theorem controls upper envelopes

\[
X_r\le\mathbf1_{C_r}.
\]

The proof must transfer to the actual ramp source

\[
X_{r,\eta}
=
\operatorname{clip}
\left(
\frac{\phi_r-t}{\eta}+1,
0,
1
\right).
\tag{14.21}
\]

The clean target is coefficient-wise:

\[
\int X_p\prod_{r\in A}X_r\,d\nu_e
\le
Cq_\eta
\int\prod_{r\in A}X_r\,d\nu_e.
\tag{14.22}
\]

This avoids a possible monotone-ratio trap: although

\[
X_r\le\mathbf1_{C_r},
\]

ratios of numerator and denominator do not automatically improve under pointwise domination. The smooth-source theorem should therefore be proved directly, or by a layer-cake decomposition reducing ramps to nested caps.

### Subtask A3: Wilson typicality of local data

The deterministic cap theorem is not enough. One must prove that under tempered Wilson block configurations the local data

\[
(m_e,\kappa_e,\{n_r\},a)
\tag{14.23}
\]

satisfy the LCI-good certificate except for a rooted complement.

The target is not

\[
\mathbb P((\mathcal G_{e,p}^{\rm LCI})^c)\le Cq_\eta
\]

under arbitrary boundary conditions. The target is rooted stability:

\[
\mathbb E
\left[
Y_{p_0}^{\rm LCI}
\prod_{p\in B}X_p
\mid
\mathcal F_{C^c}
\right]
\le
(Cq_\eta)^{|B|}
\mathbb E[
Y_{p_0}^{\rm LCI}
\mid
\mathcal F_{C^c}].
\tag{14.24}
\]

### Acceptance criteria for Theorem A

Theorem A is complete when it provides:

1. a finite-dimensional support-loss theorem on \(S^3\);
2. a direct smooth-source version or valid layer-cake reduction;
3. a Wilson-typicality statement for the LCI-good event under tempered boundaries;
4. rooted absorption of the bad LCI complement;
5. constants independent of \(L\) and block location.

Numerical diagnostics do not satisfy these criteria. They only support the target.

## 14.3 Open Theorem B: Bałaban far-source stability

### Statement

Let \(R\subset\mathcal P(C^\circ)\setminus I(e)\) be a far-source set and let

\[
0\le s\le\rho/q_\eta.
\]

Define the far-source tilted block measure

\[
d\mu_C^{\xi,R,s}
=
\frac{
\prod_{r\in R}(1+sX_r)
}{
\mathbb E_C^\xi\prod_{r\in R}(1+sX_r)
}
\,d\mu_C^\xi.
\tag{14.25}
\]

Let \(\Psi_{e,p}^{\rm good}\) be the local LCI-good one-source functional from Section 9. The far-source theorem asks for

\[
\boxed{
\mathbb E_{\mu_C^{\xi,R,s}}
\Psi_{e,p}^{\rm good}
\le
Cq_\eta
\exp\left(
\sum_{r\in R}J(p,r)
\right),
}
\tag{14.26}
\]

where

\[
\boxed{
J(p,r)\le C_Je^{-m_Jd_C(p,r)}
}
\tag{14.27}
\]

and

\[
\boxed{
J_*=\sup_p\sum_{r\ne p}J(p,r)<\infty.
}
\tag{14.28}
\]

The rooted version is

\[
\boxed{
\mathbb E_{\mu_C^{\xi,Y,R,s}}
\Psi_{e,p}^{\rm good}
\le
Cq_\eta
\exp\left(
J(p,p_0)+\sum_{r\in R}J(p,r)
\right).
}
\tag{14.29}
\]

### Subtask B1: marked random-walk locality

The proof must show that a source mark at \(r\) influences the local heat-bath data at \(p\) only through a random-walk or polymer chain with exponential decay:

\[
\boxed{
\text{source mark at }r
\leadsto
\text{local distortion at }p
\lesssim
e^{-m_Jd_C(p,r)}.
}
\tag{14.30}
\]

This is the most direct use of Balaban/Dimock locality.

### Subtask B2: positive source radius stability

The source parameter is not small:

\[
s=\rho/q_\eta.
\tag{14.31}
\]

Thus each source insertion carries a large factor. The proof must recover one \(q_\eta\) factor per mark from local rarity or source-weighted activity estimates. Otherwise the expansion loses powers of \(q_\eta\).

### Subtask B3: preservation of local LCI parameters

Far source tilts may distort

\[
H_e,\quad
m_e,\quad
\kappa_e,\quad
n_{e,r},\quad
\mathcal G_{e,p}^{\rm LCI}.
\tag{14.32}
\]

The far-source theorem must control this distortion. It is not enough to control scalar source correlations. The theorem must control the local heat-bath geometry entering LCI.

### Subtask B4: rooted bad-geometry transfer

If far sources increase the chance of LCI-bad geometry, the excess must be carried by a root:

\[
Y_p^{\rm LCI}
=
X_p\mathbf1_{(\mathcal G_{e,p}^{\rm LCI})^c}.
\tag{14.33}
\]

The rooted far-source theorem must preserve source factors for all additional marks.

### Acceptance criteria for Theorem B

Theorem B is complete when it proves:

1. far-source tilted local expectation bound (14.26);
2. rooted version (14.29);
3. exponential kernel with uniform summability;
4. compatibility with \(s=\rho/q_\eta\);
5. stability of local LCI data, not merely scalar correlations;
6. constants uniform in \(L\), block location, and admissible source sets.

## 14.4 Open Theorem C: source-weighted Bałaban expansion

### Statement

The source-weighted Bałaban expansion must propagate Lemma Q through the polymer expansion. The desired schematic implication is

\[
\boxed{
\mathrm{Lemma\ Q}
+
\mathrm{Ba\l aban/Dimock\ locality}
\Longrightarrow
\text{source-marked polymer activities with }q_\eta^{|M|}\text{ weights}.
}
\tag{14.34}
\]

A marked polymer \(\Gamma\) carries:

- a support \(\operatorname{supp}\Gamma\);
- a source mark set \(M(\Gamma)\);
- possibly a root location;
- an activity \(w(\Gamma)\).

At source strength

\[
s=\rho/q_\eta,
\]

the marked activity must satisfy a bound of the form

\[
\boxed{
|w_s(\Gamma)|
\le
A(\Gamma)\rho^{|M(\Gamma)|},
}
\tag{14.35}
\]

where \(A(\Gamma)\) obeys a polymer convergence criterion.

### Subtask C1: marked activity ledger

The expansion must track source marks through every operation:

1. block decomposition;
2. small/large field split;
3. background-field localization;
4. fluctuation integration;
5. polymer extraction;
6. cluster expansion;
7. rooted observable insertion.

Each source mark must retain its own \(q_\eta\) factor.

### Subtask C2: KP convergence with marks

A sufficient criterion is

\[
\sum_{\Gamma':\Gamma'\not\sim\Gamma}
|w_s(\Gamma')|e^{a(\Gamma')}
\le
a(\Gamma),
\tag{14.36}
\]

with marked weights included.

For anchored clusters connecting \(p\) to \(r\), the stronger estimate is

\[
\boxed{
\sum_{\Gamma\in\mathscr C(p,r)}
|w_s(\Gamma)|e^{a(\Gamma)}
\le
C_Je^{-m_Jd_C(p,r)}.
}
\tag{14.37}
\]

This anchored form is the source-weighted polymer version of far-source stability.

### Subtask C3: large-field compatibility

Large-field polymers must not erase the \(q_\eta\)-per-source bookkeeping. There are two acceptable mechanisms:

1. large-field activity pays for the source marks directly;
2. source marks inside bad regions are rooted and carried by rooted Lemma Q.

The theorem must specify which mechanism is used.

### Subtask C4: gauge covariance and block boundaries

The expansion must respect gauge structure and the link-based Gibbs specification. Source variables live on plaquettes, but conditioning is on exterior links. The theorem must avoid plaquette-level conditioning that is not compatible with gauge Gibbs measures.

### Acceptance criteria for Theorem C

Theorem C is complete when it yields:

1. source-marked polymer activities with \(q_\eta\)-per-mark factors;
2. KP or equivalent convergence;
3. anchored exponential decay for marked clusters;
4. rooted source compatibility;
5. large-field and boundary compatibility;
6. enough cumulant control to feed PTO trace-overlap summability.

## 14.5 Open Theorem D: boundary-band gate

### Statement

The analytic source is the smoothed upper-envelope variable

\[
X_{p,\eta}
=
\operatorname{clip}
\left(
\frac{\phi_p-t}{\eta}+1,
0,
1
\right),
\tag{14.38}
\]

with

\[
\mathbf1_{\{\phi_p\ge t\}}
\le
X_{p,\eta}
\le
\mathbf1_{\{\phi_p\ge t-\eta\}}.
\tag{14.39}
\]

The hard physical source is

\[
X_p^{\rm hard}
=
\mathbf1_{\{\phi_p\ge t\}}.
\tag{14.40}
\]

The boundary-band gate must show that replacing \(X_{p,\eta}\) by \(X_p^{\rm hard}\) does not destroy the source estimates as \(\eta\to0\).

The boundary band is

\[
\mathcal B_{p,\eta}
=
\{t-\eta\le\phi_p<t\}.
\tag{14.41}
\]

The required control is schematically

\[
\boxed{
\mathbb E[\mathbf1_{\mathcal B_{p,\eta}}]
\to0
\quad
\text{fast enough relative to the source estimates.}
}
\tag{14.42}
\]

### Subtask D1: one-plaquette density control

Prove a uniform local density bound near threshold:

\[
\mathbb P(t-\eta\le\phi_p<t)
\le
C\eta\,g(t,\beta),
\tag{14.43}
\]

or a comparable estimate sufficient for the intended \(q_\eta\)-scale.

### Subtask D2: conditional boundary-band control

The theorem must hold under block conditioning and source tilts:

\[
\mathbb E_C^\xi
\left[
\mathbf1_{\mathcal B_{p,\eta}}
\prod_{r\in S}X_{r,\eta}
\right]
\tag{14.44}
\]

must be controlled with the same source accounting.

### Subtask D3: rooted boundary-band absorption

If boundary-band failures are not uniformly negligible, they must be rooted:

\[
Y_p^{\rm BBG}
=
X_{p,\eta}\mathbf1_{\mathcal B_{p,\eta}}.
\tag{14.45}
\]

Then the rooted theorem must give

\[
\mathbb E
\left[
Y_p^{\rm BBG}\prod_{r\in B}X_r
\mid
\mathcal F_{C^c}
\right]
\le
(Cq_\eta)^{|B|}
\mathbb E[
Y_p^{\rm BBG}
\mid
\mathcal F_{C^c}].
\tag{14.46}
\]

### Acceptance criteria for Theorem D

The boundary-band gate is complete when it proves:

1. hard-source estimates follow from smooth-source estimates;
2. constants remain uniform as \(\eta\to0\) or along the chosen \(\eta(\beta)\);
3. source-weighted polymer estimates survive replacement of \(X_{p,\eta}\) by \(X_p^{\rm hard}\);
4. any non-negligible boundary-band contribution is rooted and absorbed.

## 14.6 Deterministic tasks already complete but requiring polishing

Several deterministic pieces are already structurally complete but should be polished for final manuscript use.

### PTO trace-overlap summability

The deterministic target is

\[
\Omega_{\rm PTO}(m;\Lambda,L)
=
\sup_p
\sum_q e^{-md(p,q)}
\operatorname{tr}(A_pA_q)
\le
C_{\rm PTO}(m,\Lambda).
\tag{14.47}
\]

The manuscript should include either:

1. a clean analytic proof in the chosen spectral-window regime; or
2. a theorem statement with finite-volume verification explicitly labeled as finite-volume.

The strongest final version is an analytic Fourier-kernel proof.

### Birman--Schwinger criterion

The finite-dimensional implication is already proved:

\[
\Theta_D<1
\Rightarrow
M-PV_DP\succeq(1-\Theta_D)M.
\tag{14.48}
\]

This should remain in the deterministic spine.

### Projected plaquette atom identities

The identities

\[
A_p=P\mathbf1_{\partial p}P,
\tag{14.49}
\]

\[
\sum_p A_p=6P,
\tag{14.50}
\]

\[
\sum_pA_p^2\preceq6\kappa_{\Lambda,L}P,
\tag{14.51}
\]

and

\[
\operatorname{tr}(A_pA_q)
=
\sum_{e\in\partial p}
\sum_{f\in\partial q}
|P(e,f)|^2
\tag{14.52}
\]

are ready for final theorem-proof formatting.

## 14.7 Recommended attack order

The correct research order is:

\[
\boxed{
1.\ \text{deterministic finite-dimensional LCI theorem}
}
\tag{14.53}
\]

\[
\boxed{
2.\ \text{smooth-source LCI upgrade}
}
\tag{14.54}
\]

\[
\boxed{
3.\ \text{LCI-good typicality under Wilson heat-bath geometry}
}
\tag{14.55}
\]

\[
\boxed{
4.\ \text{Bałaban far-source stability for local heat-bath data}
}
\tag{14.56}
\]

\[
\boxed{
5.\ \text{source-weighted polymer expansion}
}
\tag{14.57}
\]

\[
\boxed{
6.\ \text{boundary-band gate}
}
\tag{14.58}
\]

\[
\boxed{
7.\ \text{infinite-volume and continuum passage}
}
\tag{14.59}
\]

The reason for this order is that each step feeds the next. Attempting the full source-weighted Bałaban expansion before proving the finite-dimensional LCI theorem would obscure the smallest missing local mechanism.

## 14.8 Immediate next lemma to prove

The next standalone lemma should be the finite-dimensional cap-intersection support-loss theorem.

A good first target is:

### Lemma 14.1 — Nondegenerate support-loss cap ratio

Let

\[
\nu_{\kappa,m}(du)
=
Z_4(\kappa)^{-1}e^{\kappa m\cdot u}d\sigma_{S^3}(u).
\]

Let

\[
C_A=\bigcap_{r\in A}\{u:u\cdot n_r\le a\}
\]

and

\[
C_p=\{u:u\cdot n_p\le a\}.
\]

Assume:

1. \(C_A\ne\varnothing\);
2. \(C_A\cap C_p\ne\varnothing\);
3. the support-height loss satisfies

   \[
   \Delta_A(p)=h(C_A)-h(C_A\cap C_p)\ge\Delta_0>0;
   \]

4. the constrained support problems are uniformly nondegenerate.

Then

\[
\boxed{
\nu_{\kappa,m}(C_A\cap C_p)
\le
\Gamma e^{-\kappa\Delta_0}
\nu_{\kappa,m}(C_A).
}
\tag{14.60}
\]

This lemma is purely finite-dimensional. It is the best next analytic target because it does not require the full Wilson measure or the Bałaban expansion.

## 14.9 What would count as closing Lemma Q

Lemma Q is closed when the following chain is proved with uniform constants:

\[
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Rightarrow
\mathrm{TOS+J},
\tag{14.61}
\]

\[
\mathrm{TOS+J}
\Rightarrow
Z_A(\rho/q_\eta)\le e^{K|A|},
\tag{14.62}
\]

\[
Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow
\mathbb E_C^\xi X_B\le(C_Qq_\eta)^{|B|}.
\tag{14.63}
\]

Sections 5, 6, and 10 already provide the second and third implications, conditional on TOS+J. Therefore the remaining closure is:

\[
\boxed{
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Rightarrow
\mathrm{TOS+J}.
}
\tag{14.64}
\]

Numerical evidence cannot close Lemma Q. Only analytic proof of (14.64) can.

## 14.10 What would count as closing PMBSF firewall

The projected-capacity firewall is closed when the following chain is proved:

\[
\mathrm{Lemma\ Q}
+
\mathrm{SWB}
\Rightarrow
\text{source cumulant/polymer bounds},
\tag{14.65}
\]

\[
\text{source cumulant/polymer bounds}
+
\mathrm{PTO}
\Rightarrow
\text{projected capacity bound},
\tag{14.66}
\]

\[
\text{projected capacity bound}
\Rightarrow
\Theta_D<1,
\tag{14.67}
\]

\[
\Theta_D<1
\Rightarrow
M-PV_DP\succeq(1-\Theta_D)M.
\tag{14.68}
\]

The last implication is already deterministic. The open parts are SWB and the analytic projected-capacity probability bound.

## 14.11 What would still remain after PMBSF firewall closure

Even if the finite-volume PMBSF firewall closes, the continuum Yang--Mills mass-gap problem would still require additional work:

1. infinite-volume limit;
2. continuum scaling limit;
3. construction of the limiting Euclidean field;
4. Osterwalder--Schrader axioms;
5. reconstruction of the Hilbert space;
6. identification of a physical mass gap;
7. uniformity of constants under the continuum scaling regime.

These tasks are outside the present paper.

The manuscript should therefore distinguish:

\[
\boxed{
\text{finite-lattice projected-capacity closure}
}
\]

from

\[
\boxed{
\text{continuum Yang--Mills mass gap}.
}
\]

## 14.12 Final roadmap table

\[
\begin{array}{c|c|c|c}
\text{Task} & \text{Object} & \text{Status} & \text{Closure criterion}\\
\hline
A1 & S^3\text{ cap support-loss theorem} & \text{open} & \text{prove uniform ratio bound}\\
A2 & \text{smooth-source LCI} & \text{open} & \text{ramp source coefficient bounds}\\
A3 & \text{Wilson LCI-good typicality} & \text{open} & \text{rooted complement under block conditioning}\\
B & \text{Bałaban far-source stability} & \text{open} & e^{-m d}\text{ influence kernel}\\
C & \text{source-weighted Bałaban expansion} & \text{open} & q_\eta^{|M|}\text{ marked activities}\\
D & \text{boundary-band gate} & \text{open} & X_{p,\eta}\to\mathbf1_{\{\phi_p\ge t\}}\\
PTO & \text{trace-overlap summability} & \text{mostly deterministic} & \text{uniform analytic Fourier bound}\\
BS & \text{Birman--Schwinger criterion} & \text{proved} & \Theta<1\Rightarrow\text{coercivity}\\
\end{array}
\tag{14.69}
\]

## 14.13 Section summary

The remaining analytic work is now sharply localized.

The first target is the finite-dimensional LCI theorem on \(S^3\). The second is Wilson typicality of the LCI-good event with rooted complement. The third is Bałaban far-source stability under positive source tilts. The fourth is the full source-weighted Bałaban expansion. The fifth is the boundary-band gate.

The nearest concrete lemma is the support-loss cap ratio:

\[
\nu_{\kappa,m}(C_A\cap C_p)
\le
\Gamma e^{-\kappa\Delta_A(p)}
\nu_{\kappa,m}(C_A).
\]

The nearest program-level closure is:

\[
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Rightarrow
\mathrm{TOS+J}.
\]

Once that is proved, Sections 5 and 6 already yield Lemma Q by positive source-radius extraction.
