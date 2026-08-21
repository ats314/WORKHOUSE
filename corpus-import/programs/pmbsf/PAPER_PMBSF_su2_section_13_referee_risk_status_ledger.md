# 13. Referee-risk and status ledger

## 13.1 Purpose of the section

This section records the logical status of the manuscript and the main referee risks. Its purpose is to prevent overclaiming.

The paper develops a conditional proof interface:

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
\tag{13.1}
\]

The downstream firewall statement is also conditional:

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
\tag{13.2}
\]

The manuscript does not prove the continuum Yang--Mills mass gap. It does not prove the full source-weighted Bałaban expansion. It does not prove the boundary-band gate. It does not prove LCI-good typicality under all Wilson boundary conditions. It does not prove Bałaban far-source stability.

The contribution is sharper and narrower:

\[
\boxed{
\text{it reduces Lemma Q to positive source-radius control, and reduces that to LCI plus far-source stability.}
}
\tag{13.3}
\]

That is the claim to defend.

## 13.2 Claim-status table

The main claims of the paper have the following status.

\[
\begin{array}{c|c|c}
\text{Claim} & \text{Status} & \text{Location} \\
\hline
A_p=P\mathbf1_{\partial p}P\succeq0 & \text{proved} & \text{Section 3}\\
\sum_p A_p=6P & \text{proved} & \text{Section 3}\\
\sum_p A_p^2\preceq6\kappa_{\Lambda,L}P & \text{proved} & \text{Section 3}\\
\operatorname{tr}(A_pA_q)=\sum_{e\in\partial p}\sum_{f\in\partial q}|P(e,f)|^2 & \text{proved} & \text{Section 3}\\
\Theta_D<1\Rightarrow M-PV_DP\succeq(1-\Theta_D)M & \text{proved} & \text{Section 3}\\
Z_A(\rho/q_\eta)\le e^{K|A|}\Rightarrow\mathrm{Lemma\ Q} & \text{proved} & \text{Section 5}\\
\mathrm{TOS+J}\Rightarrow Z_A(\rho/q_\eta)\le e^{K|A|} & \text{proved} & \text{Section 6}\\
\text{SU(2) one-link law is vMF}_4 & \text{proved/standard} & \text{Section 7}\\
X_{p,\eta}\le\mathbf1_{\{u\cdot n_p\le1-(t-\eta)\}} & \text{proved} & \text{Section 7}\\
\mathrm{LCI}\Rightarrow\text{incident tilted stability} & \text{proved conditional on LCI ratios} & \text{Section 8}\\
\mathrm{BFS}_{\rm far} & \text{open analytic input} & \text{Section 9}\\
\mathrm{LCI+BFS}\Rightarrow\mathrm{TOS+J} & \text{proved conditional implication} & \text{Section 10}\\
\mathrm{Lemma\ Q} & \text{conditional/open} & \text{Sections 4--10}\\
\mathrm{SWB} & \text{open analytic input} & \text{Sections 9,12,14}\\
\mathrm{BBG} & \text{open analytic input} & \text{Sections 2,14}\\
\mathrm{PMBSF\ firewall\ closure} & \text{conditional} & \text{Sections 3,10,14}\\
\text{continuum Yang--Mills mass gap} & \text{not claimed} & \text{throughout}
\end{array}
\tag{13.4}
\]

## 13.3 The core conditional theorem

The core theorem of the paper should be stated as follows.

### Theorem 13.1 — Conditional rare-source reduction

Assume:

1. local cap-intersection stability for exact SU(2) one-link heat-bath geometry, with rooted bad-geometry absorption;
2. Bałaban far-source stability under positive source tilts;
3. an exponentially summable influence kernel \(J\);
4. tempered exterior boundary conditions.

Then tilted one-source stability holds:

\[
\mathbb E_{\mu^{S,s}}X_p
\le
Cq_\eta
\exp\left(
\sum_{r\in S}J(p,r)
\right),
\qquad
0\le s\le\rho/q_\eta.
\tag{13.5}
\]

Consequently,

\[
Z_A(\rho/q_\eta)\le e^{K|A|},
\tag{13.6}
\]

and therefore Lemma Q holds:

\[
\mathbb E_C^\xi\prod_{p\in B}X_{p,\eta}
\le
(C_Qq_\eta)^{|B|}.
\tag{13.7}
\]

The rooted version also holds:

\[
\mathbb E_C^\xi
\left[
Y_{p_0}\prod_{p\in B}X_{p,\eta}
\right]
\le
(C_{Q,\rm root}q_\eta)^{|B|}
\mathbb E_C^\xi Y_{p_0}.
\tag{13.8}
\]

This is the main theorem that the manuscript can safely defend.

## 13.4 What the manuscript must not claim

The manuscript must not claim any of the following.

### Not claimed: continuum mass gap

The paper does not prove

\[
\inf\sigma(H_{\rm YM})>0
\]

for a reconstructed continuum Yang--Mills Hamiltonian.

It does not construct a continuum measure, prove Osterwalder--Schrader axioms, prove reflection positivity in the limiting theory, or establish a physical mass gap in the reconstructed Hilbert space.

### Not claimed: unconditional finite-volume Wilson theorem

The paper does not unconditionally prove that Wilson-generated high-plaquette sets satisfy the projected-capacity firewall. It proves the deterministic firewall criterion and reduces the probability input to named open analytic theorems.

### Not claimed: Lemma Q proved numerically

The exact heat-bath diagnostics support Lemma-Q-type consequences, but they do not prove Lemma Q.

### Not claimed: cap regression proves LCI

The cap-feature regressions are directionally consistent but weak. LCI is a finite-dimensional cap-intersection theorem plus Wilson typicality/rooted absorption; it is not a regression claim.

### Not claimed: existing Balaban literature already gives SWB

Balaban/Dimock provide the unmarked constructive gauge-RG backbone. The source-weighted marked upgrade remains an open analytic task.

### Not claimed: adversarial boundary uniformity

The theorem is formulated for tempered exterior boundaries with rooted treatment of bad complements. It should not be stated as uniform over arbitrary adversarial boundary conditions.

## 13.5 Referee-risk ledger

### Risk 1: “This is not a Yang--Mills mass-gap proof.”

Correct. The manuscript should agree immediately.

Safe response:

\[
\boxed{
\text{The paper is a conditional projected-capacity theorem architecture, not a continuum mass-gap proof.}
}
\tag{13.9}
\]

The contribution is to isolate the finite-lattice rare-source theorem required by the PMBSF route and reduce it to LCI plus far-source stability.

### Risk 2: “Lemma Q is still open.”

Correct.

Safe response:

\[
\boxed{
\text{Lemma Q is not assumed as primitive; it is reduced to TOS+J and positive source-radius control.}
}
\tag{13.10}
\]

The proved reductions are:

\[
\mathrm{TOS+J}
\Rightarrow
Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow
\mathrm{Lemma\ Q}.
\tag{13.11}
\]

The open work is now sharper:

\[
\mathrm{LCI}_{\rm good}
+
\mathrm{BFS}_{\rm far}
\Rightarrow
\mathrm{TOS+J}.
\tag{13.12}
\]

### Risk 3: “The numerical evidence does not prove the theorem.”

Correct.

Safe response:

\[
\boxed{
\text{The numerical evidence is diagnostic; the theorem stack remains conditional.}
}
\tag{13.13}
\]

The exact-HB diagnostics test finite-volume cavity ratios and rooted ratios. The projected-capacity diagnostics test the operator mechanism. Neither replaces analytic proof.

### Risk 4: “The one-link cap mechanism cannot prove a block theorem.”

Correct.

Safe response:

\[
\boxed{
\text{LCI controls only incident sources; Bałaban far-source stability controls non-incident distortion.}
}
\tag{13.14}
\]

The paper explicitly splits

\[
S=S_{\rm inc}(e)\cup S_{\rm far}(e).
\tag{13.15}
\]

LCI handles \(S_{\rm inc}\). BFS handles \(S_{\rm far}\).

### Risk 5: “Cap-feature regressions have low explanatory power.”

Correct.

Safe response:

\[
\boxed{
\text{The regression is not the theorem. It only checks the direction of a local mechanism.}
}
\tag{13.16}
\]

The theorem is block source-stability, not a one-feature predictor.

### Risk 6: “Far-source stability is not proved by the cited Balaban papers.”

Correct.

Safe response:

\[
\boxed{
\text{Balaban/Dimock provide the unmarked RG framework; the marked source-weighted upgrade is an open theorem.}
}
\tag{13.17}
\]

Section 9 states this theorem explicitly rather than importing it.

### Risk 7: “Positive source-radius is just Lemma Q in disguise.”

Partly wrong, partly fair.

Safe response:

The implication

\[
Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow
\mathrm{Lemma\ Q}
\]

is elementary, but useful because it changes the proof target from all coefficients to a single positive real value of a generating function. The hard theorem becomes TOS+J, a one-source tilted stability statement, rather than direct \(k\)-source product moment control.

### Risk 8: “The source radius \(s=O(q_\eta^{-1})\) is large.”

Correct.

Safe response:

\[
\boxed{
\text{That is exactly why TOS+J is formulated as a large positive-source stability theorem.}
}
\tag{13.18}
\]

Small-source perturbation theory would not recover \(q_\eta^{|B|}\) coefficient scaling.

### Risk 9: “Tempered boundaries may hide the hard part.”

Partly correct.

Safe response:

Tempered boundaries are the correct Gibbs-specification formulation. Arbitrary adversarial boundary conditions can force local defects. The non-tempered complement must be paid by rooted or large-field polymer budgets. This is not hidden; it is part of the theorem stack.

### Risk 10: “The projected sector may be an artificial restriction.”

Safe response:

The projected sector is the physical coexact Maxwell sector after gauge directions are removed. The deterministic spine explicitly states the projection and proves only projected coercivity. The manuscript does not claim unprojected coercivity. Indeed, the v3b diagnostics show the unprojected operator can be supercritical while the projected operator remains subcritical.

### Risk 11: “The synthetic \(T_{64}^2\) threshold law is not Wilson SU(2).”

Correct.

Safe response:

The synthetic threshold law validates the deterministic projected-capacity operator object in a setting where ground truth is computable. It is not presented as Wilson SU(2) probability evidence.

### Risk 12: “The source-weighted Bałaban expansion is the real missing proof.”

Correct.

Safe response:

\[
\boxed{
\text{Yes. The paper narrows the missing proof to source-weighted locality and LCI-good typicality.}
}
\tag{13.19}
\]

The paper's purpose is to identify this exact missing theorem and provide the reductions around it.

## 13.6 Honesty-corrections register

The project history includes several corrections. They should be retained because they clarify which claims survived scrutiny.

### Correction 1: \(m_*\) retraction

An earlier scalar tail or mass parameter was overstated. It was retracted and is not part of the current theorem stack.

Current status: removed from the load-bearing proof.

### Correction 2: weighted-Lyapunov sign convention

A sign convention in a weighted Lyapunov estimate was corrected.

Current status: the current PMBSF spine does not rely on the erroneous sign version.

### Correction 3: false scalar tail ratio

A scalar tail-ratio claim was found incorrect.

Current status: replaced by projected-capacity and trace-overlap formulations.

### Correction 4: plaquette expectation factor-of-four correction

The leading weak-fluctuation estimate for SU(2) plaquette excess is

\[
\langle\phi_p\rangle\approx\frac{3}{8\beta},
\tag{13.20}
\]

not

\[
\frac{3}{2\beta}.
\]

At

\[
\beta=3.5,
\]

this gives

\[
\frac{3}{8\beta}\approx0.107,
\tag{13.21}
\]

consistent with observed values after expected corrections.

Current status: corrected; no downstream theorem depends on the wrong value.

### Correction 5: decay-rate point-estimate overconfidence

Earlier finite-volume decay-rate point estimates had wide confidence intervals. They should not be quoted as precise rates.

Current status: qualitative decay evidence remains; precise analytic decay rate remains open.

### Correction 6: cap-predictor \(R^2\) artifact

A stronger cap-regression interpretation was weakened after recognizing that low \(R^2\) on positive rows indicates missing nonlocal/block structure.

Current status: cap geometry is treated as local seed only; the theorem is block source-stability plus far-source stability.

## 13.7 Current manuscript-safe status paragraph

The following paragraph can be used directly in the paper.

The results of this manuscript are conditional. The deterministic projected-capacity spine, the positive source-radius extraction, the TOS+J-to-source-radius telescoping argument, and the finite-dimensional implication from LCI ratios to incident tilted stability are proved. The remaining analytic inputs are the Wilson typicality of LCI-good heat-bath geometry with rooted complement, Bałaban far-source stability under positive source tilts, the source-weighted Bałaban expansion, and the boundary-band gate. The numerical diagnostics support the finite-volume consequences of these inputs but do not prove them. No continuum Yang--Mills mass-gap theorem is claimed.

## 13.8 Dependency graph

The dependency graph is:

\[
\boxed{
\mathrm{LCI}_{\rm ratios}
\Rightarrow
\mathrm{incident\ tilted\ stability}
}
\tag{13.22}
\]

\[
\boxed{
\mathrm{BFS}_{\rm far}
+
\mathrm{incident\ tilted\ stability}
\Rightarrow
\mathrm{TOS+J}
}
\tag{13.23}
\]

\[
\boxed{
\mathrm{TOS+J}
\Rightarrow
Z_A(\rho/q_\eta)\le e^{K|A|}
}
\tag{13.24}
\]

\[
\boxed{
Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow
\mathrm{Lemma\ Q}
}
\tag{13.25}
\]

\[
\boxed{
\mathrm{Lemma\ Q}
+
\mathrm{SWB}
\Rightarrow
\mathrm{source\ cumulant/polymer\ control}
}
\tag{13.26}
\]

\[
\boxed{
\mathrm{source\ cumulant/polymer\ control}
+
\mathrm{PTO}
\Rightarrow
\mathrm{projected\ capacity\ control}
}
\tag{13.27}
\]

\[
\boxed{
\mathrm{projected\ capacity\ control}
+
\mathrm{BS}
\Rightarrow
\mathrm{finite\ projected\ coercivity}.
}
\tag{13.28}
\]

The open nodes are:

\[
\mathrm{LCI}_{\rm good}\text{ typicality},
\qquad
\mathrm{BFS}_{\rm far},
\qquad
\mathrm{SWB},
\qquad
\mathrm{BBG}.
\tag{13.29}
\]

## 13.9 Numerical-status table

The numerical evidence should be described as follows.

\[
\begin{array}{c|c|c}
\text{Diagnostic} & \text{Finding} & \text{Interpretation} \\
\hline
\text{Exact-HB side-8} & \Lambda_{\rm med}=0.9249,\ \Lambda_{\rm root,med}=0.9563 & \text{supports local block source stability}\\
\text{Exact-HB side-10} & \Lambda_{\rm med}=1.0158,\ \Lambda_{\rm root,med}=1.0221 & \text{supports geometry robustness}\\
\text{Full-volume }L=64 & \text{median covariance ratios drop strongly} & \text{supports }k=1\text{ consequences}\\
\text{v3b BS} & \Theta_*=0.884442692429<1 & \text{supports projected firewall mechanism}\\
\text{random plaquette incidence} & \text{Wilson tracks plaquette comparator} & \text{supports correct random baseline}\\
T_{64}^2\text{ threshold law} & \mathrm{AUC}=1.000 & \text{validates deterministic capacity variable}\\
\text{matrix-Laplace} & \text{Wilson/random spectral ratios near }1 & \text{supports noncommutative transfer target}
\end{array}
\tag{13.30}
\]

All entries are finite-volume diagnostics. None is a proof of an open theorem.

## 13.10 Language rules for the final manuscript

Use:

\[
\text{``supports''},\quad
\text{``is consistent with''},\quad
\text{``diagnoses''},\quad
\text{``finite-volume evidence for''}.
\]

Avoid:

\[
\text{``proves''},\quad
\text{``establishes''},\quad
\text{``closes''},\quad
\text{``solves''}
\]

when referring to numerical evidence.

Use:

\[
\text{``conditional theorem''}
\]

for the main result.

Use:

\[
\text{``open analytic input''}
\]

for LCI-good typicality, BFS, SWB, and BBG.

Use:

\[
\text{``deterministic''}
\]

only for Sections 3, 5, 6, and the purely finite-dimensional implications in Section 8.

## 13.11 Final status statement

The final status of the manuscript is:

\[
\boxed{
\text{proved reductions + conditional theorem architecture + targeted finite-volume evidence.}
}
\tag{13.31}
\]

Not:

\[
\boxed{
\text{unconditional Yang--Mills mass-gap proof.}
}
\tag{13.32}
\]

The strongest defensible summary is:

\[
\boxed{
\text{The paper identifies a precise proof interface for PMBSF:}
}
\]

\[
\boxed{
\text{local }S^3\text{ cap-intersection stability plus Bałaban far-source stability}
}
\]

\[
\boxed{
\text{implies positive source-radius control, hence Lemma Q, hence the rare-source input needed by the projected firewall.}
}
\tag{13.33}
\]

## 13.12 Section summary

This section fixed the manuscript's claim boundaries.

The paper proves:

\[
\mathrm{TOS+J}
\Rightarrow
Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow
\mathrm{Lemma\ Q},
\]

and proves that LCI plus BFS are sufficient for TOS+J.

The paper assumes or leaves open:

\[
\mathrm{LCI}_{\rm good}\text{ typicality},
\qquad
\mathrm{BFS}_{\rm far},
\qquad
\mathrm{SWB},
\qquad
\mathrm{BBG}.
\]

The numerical evidence supports the targeted consequences but does not prove the open inputs.

The next section lists the remaining analytic tasks in the order they should be attacked.
