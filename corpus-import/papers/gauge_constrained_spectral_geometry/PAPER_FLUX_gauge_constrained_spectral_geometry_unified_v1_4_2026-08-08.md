# Gauge-Constrained Spectral Geometry
## Unified Master Theory of the SU(N) Wilson / Kogut–Susskind Spectral Program

**Audit-hardened release: v1.4 (2026-08-08).**

**Master synthesis date:** 2026-08-08 · **v1.4:** retains v1.3 but incorporates the independent `SIMULATIONS/` audit as a proof-status authority for the $SU(3)$ strong-coupling tower. The hand-checkable $O(y^2)$ homological factorization and the structural $O(y^3)$ triality mechanism remain strong. The $O(y^4)$ rational kernel/pencil is retained as an exact-arithmetic computational ledger, but its end-to-end theorem status is explicitly withheld until the shared effective-Hamiltonian, normalization, independent-regression, interval-enclosure, and near-$\Gamma$ nonuniformity gates are closed. No coefficient is deleted merely because the certificate chain is incomplete.
**Supersedes as a *narrative* unification (not as a status authority):** the seven canonical ledgers of 2026-07-13, the updated flat-band theorem record of 2026-07-14, the strengthened GCSG synthesis of 2026-07-13, and the 2026-07/08 frontier notes (Hodge shape space; singularity atlas; certified exceptional points; crossover v1; Wilson–Bergman weight theorem; rank-1/2 Bergman transfer; tight-connections review).
**Status authorities remain the canonical ledgers.** Where ledgers conflict, this document applies the third-pass adjudication rule: the latest scope-specific combined ledger controls its declared domain; elsewhere the narrowest supported statement is used.
**Status vocabulary:** **Proven** · **Exact computational ledger — audit pending** · **Computationally verified** · **Conditional** · **Rejected** · **Conjectural** · **Open**. A computational ledger is never promoted to a theorem solely because its arithmetic is exact; the derivation and certificate dependencies must also be closed.


### v1.4 consolidation and authority rule

This document separates three regimes that use related algebra but different expansion parameters:

1. **compact local class stiffness:** $\beta\to\infty$ for the one-plaquette class Hamiltonian;
2. **strong-coupling spatial mobility:** $u=\beta_H/6\to0$ for the one-flux band;
3. **global Wilson-measure stability:** finite/infinite-volume probabilistic control.

No coefficient is transferred between these regimes without an explicit bridge. The fourth-order shape-space theorem is an ambient symmetry classification. For Layer II, `PAPER homological flat bands.md` remains the rank/status authority relative to its accepted certificates, while `Pasted markdown.md` (the independent `SIMULATIONS/` audit assembled 2026-08-08) controls proof-status claims about the $SU(3)$ $O(y^4)$ computational tower. The detailed $SU(4)$ theorem/certificate remains the narrow authority for its exceptional sector. When a coefficient ledger and an audit disagree only about proof closure, the numerical ledger is retained and the proof status is downgraded rather than silently discarded.


---

### v1.3 change log — 2026-08-08

The 2026-08-08 homological-flat-band paper changes the Layer-II registry in four ways:

1. $SU(5)$ and $SU(6)$ are no longer listed as open at the axial fourth-order level.
2. The exact axial coefficient is universal for every $N\ge3$,
   \[
   \alpha_N^{\mathrm{pen}}=\frac{640}{N(N^2-1)^3}.
   \]
3. The physical tier-collapse statement $B_N^{\mathrm{shp}}=D_N^{\mathrm{shp}}=0$ now spans the complete rank partition $N\ge3$ covered by the accepted certificates/stable theorem.
4. $SU(3)$ is exceptional in the second pencil coefficient:
   \[
   \Delta\beta_3^{\mathrm{pen}}=-\frac{25}{64},
   \]
   so quotient-scalarity fails at $N=3$ and must not be promoted to an all-rank theorem.

The compact local-class theory, seam theory, transfer/certificate layer, and projected-capacity no-go/firewall retain their v1.2 scope unless explicitly changed below.

### v1.4 audit-hardening change log — 2026-08-08

The independent `SIMULATIONS/` re-audit does **not** overturn the central $SU(3)$ fourth-order rational ledger, but it changes the authority level of the full $O(y^4)$ theorem chain.

1. The $O(y^2)$ incidence identity
   \[
   S(k)+4I=B(k)B(k)^\dagger
   \]
   and the all-orders annihilation criterion $BMB^\dagger|_{\ker B^\dagger}=0$ are promoted as the cleanest hand-checkable Layer-II theorem package.
2. The $O(y^3)$ bare-link/triality argument remains structural; the numerical coefficient is exact arithmetic but still benefits from the requested cold replay.
3. The $SU(3)$ $O(y^4)$ coefficient values, 189-record kernel, bandwidth, and ray curvatures are retained as an **exact computational ledger**. Their end-to-end theorem status is pending closure of six load-bearing gates: $PVP=aP$, degenerate-space folded-effective-Hamiltonian regression, full Stage-3H independent regression, magnetic-prefactor normalization, outward-rounded interval certification, and the nonuniform $k\to\Gamma$ touching analysis.
4. The global interval certificate is therefore described as **numerically decisive but not formally interval-rigorous as currently coded**; the identified leaks are mechanical to fix.
5. The master no longer asserts that the Aug. 8 simulation variable can be relabeled to canonical $u=\beta_H/6$ without numerical rescaling. That bridge is conditional until the magnetic-prefactor gate is closed.
6. The rejected Schur/Haar-Hessian “Theorem B” and the unimplemented 4D $SU(2)$ $\theta$/TRG branch are explicitly quarantined from the master theorem dependency graph. The analytical Wilson+Haar Hessian formula itself remains salvageable as a separate technical result.
7. Strong-coupling extrapolation to the continuum remains **consistent, not controlled**; the finite series must not be advertised as a convergent continuum prediction.

---

## 0. The theory in one statement

**Gauge-constrained spectral geometry** is a five-layer theory of spectra in compact-gauge lattice systems:

1. **Internal spectral stiffness** — the geometry of conjugacy classes and the Weyl measure fixes local gaps and their exact asymptotic coefficients (the one-plaquette layer).
2. **Homological mobility** — the position of an excitation inside the cellular chain complex of space fixes when, and at what perturbative order, it can move (the flat-band / caging layer).
3. **Seam analyticity** — a finite atlas of complex exceptional points governs the crossover between strong- and weak-coupling towers, and symmetric functions of colliding branches are the analytic continuers (the singularity layer).
4. **Transfer geometry and certificate duality** — the correct norm for tails and transfers is a Wilson–Bergman weighted norm on the Weyl alcove; positivity certificates live in a two-cone (pointwise x character) geometry whose large-N contraction is obstructed by sign-uncertainty (the certificate layer).
5. **Marginal stability** — exact marginalization (Helffer–Sjöstrand leakage) and rooted incidence-shadow capacity determine how much spectral protection survives coupling to unresolved degrees of freedom (the global layer).

The unification is **structural, not asymptotic**: the three coupling regimes (strong-coupling \(u\)-expansion, compact large-\(\beta\) well, global Wilson measure) are governed by the same operators and filtrations but are never conflated into one expansion. This regime firewall is itself part of the theory.

---

## 1. Objects and canonical conventions

- **Spatial complex.** \(T_L^d=(\mathbb Z/L\mathbb Z)^d\) with links, plaquettes, cubes; boundary maps \(\partial_2,\partial_3\); coboundaries \(d_1,d_2\); \(D=d_1\).
- **Hamiltonian.** Kogut–Susskind \(H=\tfrac{g^2}{2a}\sum E^2+\tfrac{2N}{ag^2}\sum_{p}P_p\); one-plaquette class reduction \(H=\tfrac12 C_2+\beta V\) on class functions of \(SU(N)\).
- **Strong-coupling normalization firewall.** The canonical Hamiltonian ledger uses \(\boxed{u=\beta_H/6}\). The historical definition \(y=2\beta_H/3\) remains **Rejected**. However, the independent `SIMULATIONS/` audit found that stages 3F/3H explicitly exclude a convention-dependent magnetic-operator prefactor that is not later closed by a gate. Therefore the Aug. 8 simulation-tower coefficients are kept in their **source normalization** until that prefactor is proved. Agreement with the canonical \(u\)-ledger is strong consistency evidence, but v1.4 no longer treats “replace `y` by `u` with no rescaling” as a proved bridge.
- **Weyl reduction.** After Weyl-denominator conjugation the class kinetic operator is the \(A_{N-1}\) trigonometric Calogero–Sutherland operator at the free-fermion point \(\kappa=1\) (**Proven**, imported equivalence). Radial Laguerre parameter of the Weyl-Gaussian class sector: \(\boxed{\alpha_N=(N^2-3)/2}\) (**Proven**).
- **Incidence cage.** For any coefficient of the factorized form \(H^{(n)}=a_nI+BM_nB^\dagger\), the sector \(\ker B^\dagger\) is shifted rigidly (**Proven**). Consistently oriented cube boundaries lie in this kernel because \(\partial_2\partial_3=0\).
- **Status governance.** Precedence when sources conflict: exact self-contained derivation > independent direct computation > internally consistent saved output > later consistent version > stale diagnostics. A filename saying "FINAL" never overrides a failed invariant check.

---

## 2. The five structural laws

These are the load-bearing organizing principles; every theorem in §§3–7 instantiates at least one.

**Law 1 (Filtration–Rigidity–Escape).** Identify an exactly preserved filtration; prove rigidity inside it; compute the first escaped coefficient exactly.
*Instances:* internally, the \(SU(3)\) even sector stays inside the radial invariant algebra \(\mathbb R[p_2]\) until \(p_3^2\) escapes at order \(\beta^{-1/2}\) with exact shift \(\sqrt6/576\); spatially, the one-flux branch stays inside the incidence ideal through \(O(u^3)\) and escapes at \(O(u^4)\) with exact coefficients \((q,A,B)\); at the seam, the raw gap escapes analyticity at the vacuum EP while its square remains inside the symmetric-function algebra of the colliding pair.

**Law 2 (Kernel–Resolvent Duality).** One incidence operator plays two spectral roles: \(\ker d_1^\ast\) hosts protected closed-surface carriers, while \((m^2I+\alpha d_1^\ast d_1)^{-1}\) controls exponentially localized propagation in the complementary link sector. Both faces are exact on the periodic cubic complex (**Proven**):
\[
(m^2I+\alpha D^\ast D)^{-1}_{\mu\nu}(p)=\frac{\delta_{\mu\nu}+(\alpha/m^2)h_\mu(p)\overline{h_\nu(p)}}{m^2+\alpha\widehat p^{\,2}},\qquad h_\mu(p)=e^{ip_\mu}-1.
\]

**Law 3 (Two-Cone Certificate Duality and its contraction).** On class functions, multiplication by \(h\) is PSD iff \(h\ge0\) pointwise; convolution by \(h\) is PSD iff all character coefficients \(\hat h_R\ge0\). Gap certificates decompose against exactly these two cones plus squares. Under 't Hooft-scaled weak coupling the compact cone contracts to a Euclidean cone of effective dimension \(\sim N^2/2\) (the GUE identification with radial weight \(u^{\alpha_N}e^{-u}\)), where Mellin-strip sign-uncertainty bounds how tightly any fixed-degree certificate can localize — the structural mechanism behind the ledger's declared fixed-rank non-uniformity in \(N\). (Framework **Proven/imported**; the specific limitation transplant is a pre-registered program, §12.)

**Law 4 (Seam Analyticity).** The convergence of every coupling-expansion in the program is governed by a finite, certifiable atlas of complex exceptional points of the complex-symmetric pencil \(H(\beta)\). Symmetric functions of a colliding pair are single-valued through the collision; therefore the correct global objects are squared gaps and pair-symmetric combinations, not raw gaps.

**Law 5 (Rooted Marginal Stability).** Global fixed-window "firewalls" are false (Bernoulli no-go, **Proven**); the correct stability object is a rooted defect-animal expansion in which the incidence-shadow capacity \(\mathcal K\le1\) contributes exactly one exponential mark \(e^{s\gamma}\). Exact marginalization obeys the Helffer–Sjöstrand leakage bound \(\nabla_x^2S_{\mathrm{eff}}\succeq\mathbb E\nabla^2_{xx}S-M^2I/\gamma\) (**Proven**).

---

## 3. Layer I — Internal spectral stiffness (one-plaquette theorems)

### 3.1 The compact SU(3) class-gap theorem — **Proven** (with \(O(\beta^{-1})\) remainder)
\[
\boxed{\Delta_{\mathrm{SU}(3)}^{+}(\beta)=\sqrt{\tfrac{2\beta}{3}}-\tfrac5{16}-\tfrac{311\sqrt6}{9216}\,\beta^{-1/2}+O(\beta^{-1})}
\qquad
\boxed{c_1-c_1^{\mathrm{radial}}=\tfrac{\sqrt6}{576}}
\]
with \(H_1=-p_2^2/96\), \(H_2=\sqrt6\,(p_2^3/11520+p_3^2/8640)\); non-radial multiplicity \(\chi_{\mathrm{nr}}=2\). The first even escape from \(\mathbb R[p_2]\) is through \(p_3^2\). Independently confirmed by a converged compact Peter–Weyl execution (\(K=80\), \(\beta=50\ldots3200\)) (**Computationally verified**).

**Remainder closure now in-corpus (v1.1).** The analytic \(O(\beta^{-1})\) step is proved, not imported: exact Weyl conjugation \(J(\tfrac12C_2)J^{-1}=\tfrac14(-\Delta_{\mathfrak t}-|\rho|^2)\) reduces \(H_\beta\) to a flat torus Schrödinger operator with **no untracked Haar/metric terms**; the Wilson potential \(W=1-\tfrac13\sum_j\cos\theta_j\ge0\) has the identity as its unique nondegenerate minimum (\(D^2W(0)=\tfrac13I_2\)), supplying the confinement hypotheses; with \(h=\beta^{-1/2}\) and well scaling \(a=(3/2)^{1/4}\) the rescaled operator has the exact normal form \(H_0+hH_1+h^2H_2+h^3R_h\) with \(H_0=\tfrac1{2\sqrt6}(-\Delta_z+p_2)\); an **equivariant harmonic-well lemma** (Agmon/IMS localization, symmetry-restricted polynomial-Gaussian quasimodes with residual \(O(h^4)\); a special case of the Charles–Vũ Ngọc semiclassical Birkhoff normal form) then identifies the two simple even levels (\(\psi_0=\)const, \(\psi_1\propto p_2-4\)) and delivers the three-term gap with \(O(\beta^{-1})\) remainder. The scalar \(-|\rho|^2/4=-\tfrac12\) cancels from the gap. Exact ingredients: \(\Delta_{H_2}=19\sqrt6/576\), \(\Delta_{\mathrm{res}}=-205\sqrt6/3072\), moment table \(\langle p_2^3\rangle,\langle p_3^2\rangle=(120,5)_{\psi_0},(480,20)_{\psi_1}\).

### 3.2 Fixed-rank SU(N) coefficients
- Leading C-even gap \(\sqrt{2\beta/N}\); \(c_0^{(N)}=-(2N^2-3)/(16N)\) — **Proven** for fixed \(N\ge3\).
- Lowest C-odd shell is \(s=3\); leading C-odd gap \(\sqrt{9\beta/(2N)}\); \(c_0^{(N),-}=-3(N^2-3)/(16N)\) — **Proven**, \(N\ge3\).
- Candidate \(\beta^{-1/2}\) closed forms
\[
c_1^{(N),+}=-\frac{\sqrt2\,(6N^4-24N^2+41)}{1024\,N^{3/2}},\qquad
c_1^{(N),-}=-\frac{\sqrt2\,(14N^4-97N^2+290)}{1536\,N^{3/2}}
\]
— **Proven at \(N=3\)** (even), **Computationally verified (exact arithmetic) for \(N=3,\ldots,12\)**, **Conjectural** for unrestricted fixed \(N\) pending a symbolic-\(N\) Gram transcript.

### 3.2b The \(\beta^{-1}\) order — exact third-order coefficients (new, v1.1)
Third-order Rayleigh–Schrödinger on the Weyl-Gaussian shells, with the exact operator stack \(H_1=-P_4/48\), \(H_2=\sqrt{2N}\,P_6/2880\), \(H_3=-N\,P_8/161280\) and shell energies \(E_s^{(0)}=s/\sqrt{2N}\), yields closed forms for the next coefficient in both sectors:
\[
\boxed{c_2^{(N),+}=-\frac{60N^6-401N^4+1522N^2-2297}{49152\,N^2},\qquad
c_2^{(N),-}=-\frac{95N^6-981N^4+5853N^2-15335}{49152\,N^2},}
\]
with the resolvent part of \(c_1\) separately closed: \(q_{\mathrm{res}}^{(N)}=-(34N^4-120N^2+171)/(3072N^2)\).
**Verification (exact rational arithmetic):** even for \(N=6,\ldots,12\); odd for \(N=7,\ldots,13\); and — resolving the power-sum overcompleteness that blocks small ranks — **exactly at \(N=3\)** in the true rank-two invariant basis \(\{p_2,p_3\}\) with the SU(3) reductions \(P_4=p_2^2/2\), \(P_6=p_2^3/4+p_3^2/3\), \(P_8=p_2^4/8+4p_2p_3^2/9\):
\[
\boxed{c_2^{+}(3)=-\tfrac{5665}{110592},\qquad c_1^{-}(3)=-\tfrac{551\sqrt6}{13824},\qquad c_2^{-}(3)=-\tfrac{53}{864}.}
\]
The SU(3) local class gaps are therefore known **four terms deep in both C-sectors**:
\[
\Delta^{+}(\beta)=\sqrt{\tfrac{2\beta}{3}}-\tfrac5{16}-\tfrac{311\sqrt6}{9216}\beta^{-1/2}-\tfrac{5665}{110592}\beta^{-1}+\ldots,
\]
\[
\Delta^{-}(\beta)=\sqrt{\tfrac{3\beta}{2}}-\tfrac38-\tfrac{551\sqrt6}{13824}\beta^{-1/2}-\tfrac{53}{864}\beta^{-1}+\ldots
\]
An independent odd-sector compact Peter–Weyl audit (irrep basis, C-splitting under \((p,q)\!\leftrightarrow\!(q,p)\), \(K=80\), \(\beta\le3200\)) confirms the odd three-term law, and its \(\beta^{-1}\) fit selects \(-53/864\) over the superseded direct candidate \(-1781/55296\); the exact-arithmetic identity is the authority.
**Status:** the closed forms are **Computationally verified (exact arithmetic)** at the listed ranks and at \(N=3\), **Conjectural** as unrestricted fixed-\(N\) formulas (open verification gaps: even \(N=4,5\); odd \(N=4,5,6\)); the analytic \(O(\beta^{-3/2})\) remainder at this order awaits a one-order extension of the harmonic-well lemma of §3.1, which as written closes \(O(\beta^{-1})\). This discharges local-frontier priority 4 ("next \(O(\beta^{-1})\) coefficients") at the certificate level.

### 3.3 Polarity-excess law — **Proven corollary** of 3.2
The C-odd and C-even leading terms cancel in the ratio \(3/2\), leaving an exact rank-diagnostic constant:
\[
\boxed{\Delta^{(N)}_{-}-\tfrac32\,\Delta^{(N)}_{+}=\frac{9}{32N}+O(\beta^{-1/2}).}
\]
(The \(\beta^{-1/2}\) refinement inherits the Conjectural status of the \(c_1\) candidates.)

### 3.4 The odd-Casimir staircase and cubic lock — **Proven**
With \(U=e^{iX}\), \(P_k=\operatorname{Tr}X^k\):
\[
SU(3):\ \operatorname{ImTr}U=-\frac{P_3}{6}\prod_{j=1}^{3}\frac{\sin(\theta_j/2)}{\theta_j/2},
\qquad
SU(4):\ \operatorname{ImTr}U=-\frac{P_3}{6}\prod_{\{ij\}\subset\{123\}}\frac{\sin((\theta_i+\theta_j)/2)}{(\theta_i+\theta_j)/2},
\]
both form factors positive on the alcove — \(SU(3)\) and \(SU(4)\) are **exactly cubic-locked** (\(\operatorname{ImTr}U\) shares sign and interior nodal set with \(-P_3\)). The lock breaks at \(SU(5)\): \(P_5=\tfrac56P_2P_3+5e_5\) makes \(e_5\) an independent C-odd direction for \(N\ge5\) (explicit counterexample with \(P_1=P_3=0,\ P_5\ne0\)). Primitive odd directions: \(e_3\) (all \(N\ge3\)); \(+e_5\) at \(N\ge5\); \(+e_7\) at \(N\ge7\); … The exact Gram calculations independently exhibit the new degree-5 channel at \(N=5\) and degree-7 at \(N=7\).
**Derived lattice operators:** improved cubic source \(\mathcal O_3^{\mathrm{imp}}=(32A-B)/24=-P_3/6+P_7/1260+O(|X|^9)\) (quintic contamination cancelled) and primitive rank-five source \(\mathcal O_5^{\mathrm{prim}}=B-8A+2EA=e_5+O(|X|^7)\), with \(A=\operatorname{ImTr}U\), \(B=\operatorname{ImTr}U^2\), \(E=N-\operatorname{ReTr}U\). For \(SU(5)\), \(e_5(X)=\det X\).

### 3.5 Leakage diagnostics and the radial-tail no-go
Exact four-channel leakage quartic \(\lambda^4-\tfrac{215}{768}\lambda^2-\tfrac{175}{13824}\lambda+\tfrac{25}{294912}\) (**Proven**); Perron root \(\rho_3=0.5501615335\ldots\) (**Computationally verified**, finite-channel only). The one-resolvent/Schur-symmetric radial-tail obstruction is **Proven**: Laguerre quartic off-diagonals grow \(\sim n^2\) against the present denominator family, so finite leakage numbers cannot be promoted to a full-channel constant by that route. Compressed compact Peter–Weyl high-block inverse is \(O(R^{-2})\) (**Proven**); the buffered full-resolvent/transfer theorem in compact shells is **Open** (SU3-10).

---

## 4. Layer II — Homological mobility (the one-flux $C$-odd band)

### 4.1 Exact second-order rank/topology factorization — **Proven**

In the one-excitation sector, orient each plaquette by its cellular boundary and let
\[
s(p,p')=\epsilon_p(\ell)\epsilon_{p'}(\ell)
\]
for adjacent plaquettes sharing the link $\ell$. The fixed-rank representation-theory contraction reduces the entire $C$-odd second-order hopping problem to one positive scalar,
\[
\boxed{
t_N=\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)},\qquad N\ge3.
}
\]
Thus representation theory supplies the amplitude while the cellular boundary operator supplies the band geometry.

The rank-cubic limit is
\[
0<N^3t_N<\frac14,
\qquad
N^3t_N\nearrow\frac14,
\]
with exact deficit
\[
\boxed{
\frac14-N^3t_N
=
\frac{2N^4+31N^2-9}
{4(N^2-1)(2N^2-1)(4N^2-9)}.
}
\]

### 4.2 Incidence factorization, complete Bloch spectrum, and Hodge self-duality — **Proven**

Set $u_j=1-e^{ik_j}$ and
\[
\widetilde N(k)=
\begin{pmatrix}
u_2&-u_1&0\\
u_3&0&-u_1\\
0&u_3&-u_2
\end{pmatrix}.
\]
The signed face adjacency satisfies
\[
\boxed{S(k)+4I=\widetilde N(k)\widetilde N(k)^\dagger}.
\]
Writing
\[
q(k)=\sum_j|u_j|^2=4\sum_{j=1}^3\sin^2\frac{k_j}{2},
\]
one obtains the complete spectrum
\[
\boxed{
\operatorname{spec}S(k)=\{-4,-4+q(k),-4+q(k)\}.
}
\]
The lowest $C$-odd branch is therefore exactly dispersionless at this order for every $N\ge3$.

In centered gauge, with $s_j=\sin(k_j/2)$,
\[
M(k)=2
\begin{pmatrix}
s_2&-s_1&0\\
s_3&0&-s_1\\
0&s_3&-s_2
\end{pmatrix},
\]
and for
\[
J(z_{12},z_{13},z_{23})=(z_{23},-z_{13},z_{12})
\]
one has
\[
\boxed{JM=-2[s]_\times},
\qquad
\boxed{M^\dagger M=JMM^\dagger J^T=4(|s|^2I-ss^T)}.
\]
The face and link Hodge Hamiltonians are therefore gauge-Hodge equivalent to the same transverse lattice-Maxwell operator. Their kernels are the same longitudinal line after Hodge rotation,
\[
\ker M=\operatorname{span}\{s\},
\qquad
J\ker M^\dagger=\operatorname{span}\{s\}.
\]
On a sphere around $\Gamma$, $\widehat s=s/|s|$ gives a unit embedded map $S^2\to\mathbb{RP}^2$. Since adding one trivial real orbital changes the target to $\mathbb{RP}^3$ with $\pi_2(\mathbb{RP}^3)=0$, the correct topology is a
\[
\boxed{\text{fragile unit Hodge hedgehog, not stable BDI protection}.}
\]

### 4.3 Exact torus degeneracy and finite-volume isolation — **Proven**

The flat carrier is the two-cycle space:
\[
0\to\operatorname{im}\partial_3\to\ker\partial_2\to H_2(T^3;\mathbb C)\to0.
\]
Hence on an $L^3$ torus,
\[
\boxed{\dim\ker\partial_2=(L^3-1)+3=L^3+2.}
\]
After removing the complete flat eigenspace, the first adjacency level is
\[
\boxed{4\sin^2\frac{\pi}{L}}.
\]
The isolation scale is therefore $L^{-2}$, not $L^{-1}$.

A falsifiable integer implementation check is: $L^3+2$ flat states on $T^3$, $L^3+1$ on $T^2\times I$, and $L^3$ on an open box.

### 4.4 Rank-cubic mobility and third-order rigidity

The complete second-order $C$-odd one-plaquette manifold has width
\[
W_N^-(u)=12t_Nu^2+O(u^3),
\]
so
\[
W_N^-(u)\sim\frac{3u^2}{N^3}.
\]
This is the exact rank-cubic mobility suppression.

For the $SU(3)$ caged branch, the source-certified expansion is
\[
m_{-,\mathrm{flat}}^{SU(3)}(u)=\frac83+u+\frac{11}{306}u^2-\frac{109151}{249696}u^3+O(u^4).
\]
The 2026-08-08 paper explains the third-order rigidity by the bare-link/tromino mechanism: every three-distinct-plaquette numerator vanishes at $O(u^3)$, so the third-order effective Hamiltonian retains the second-order incidence structure. The coefficient itself remains flagged for a clean cold rerun before submission, as stated in that paper.

### 4.5 Generic fourth-order obstruction space — **Proven (exact orbit enumeration)**

Let
\[
a_i=4\sin^2\frac{k_i}{2},\qquad q=a_1+a_2+a_3,
\]
\[
e_2=a_1a_2+a_1a_3+a_2a_3,
\qquad
e_3=a_1a_2a_3.
\]
The most general nonconstant cubic-invariant fourth-order correction on the generic flat fiber is
\[
\boxed{
\varepsilon_4(k)=c_0+A_N^{\mathrm{shp}}q+B_N^{\mathrm{shp}}e_2+C_N^{\mathrm{shp}}\frac{4e_2}{q}+D_N^{\mathrm{shp}}\frac{e_3}{q}.
}
\]
The obstruction space splits into two infrared tiers,
\[
\boxed{
\mathcal Q_4=
\underbrace{\operatorname{span}\{q,4e_2/q\}}_{L^{-2}}
\oplus
\underbrace{\operatorname{span}\{e_2,e_3/q\}}_{L^{-4}}.
}
\]

With checkpoints $X=(\pi,0,0)$, $M=(\pi,\pi,0)$, $P=(\pi,\pi/2,0)$, and $R=(\pi,\pi,\pi)$, define $\Delta_K=\varepsilon_4(K)-\varepsilon_4(\Gamma)$. Then
\[
A=\frac{\Delta X}{4},\qquad
B=\frac{\Delta X+4\Delta M-6\Delta P}{16},
\]
\[
C=\frac{3(2\Delta P-\Delta M-\Delta X)}8,
\qquad
D=\frac{3(\Delta R-6\Delta M+6\Delta P)}{16}.
\]
The identities
\[
6\Delta P-4\Delta M-\Delta X=-16B,
\]
\[
\Delta R-2\Delta M+\Delta X=16B+\frac{16}{3}D
\]
are algebraic consequences of the basis and are not independent validation gates.

### 4.6 Physical tier collapse — **Exact within the accepted fourth-order ledgers; shared proof gates pending**

At every rank now resolved,
\[
\boxed{B_N^{\mathrm{shp}}=D_N^{\mathrm{shp}}=0.}
\]
Thus the physical fourth-order correction lies entirely in
\[
\boxed{
\operatorname{span}\left\{q,\frac{4e_2}{q}\right\}.
}
\]
The generic $L^{-4}$ obstruction tier is allowed by cubic symmetry but is not selected by the exact microscopic contraction. This is a dynamical selection rule, not a symmetry identity.

In the older two-invariant pencil notation,
\[
c_{4,N}(k)=q_N+
\frac{
\alpha_N^{\mathrm{pen}}\sum_iX_i^2+
\beta_N^{\mathrm{pen}}\sum_{i<j}X_iX_j
}{2\sum_iX_i},
\qquad X_i=1-\cos k_i,
\]
the conversion is
\[
\boxed{A_N^{\mathrm{shp}}=\frac{\alpha_N^{\mathrm{pen}}}4},
\qquad
\boxed{B_N^{\mathrm{shp}}=0},
\]
\[
\boxed{C_N^{\mathrm{shp}}=\frac{\beta_N^{\mathrm{pen}}-2\alpha_N^{\mathrm{pen}}}{16}},
\qquad
\boxed{D_N^{\mathrm{shp}}=0}.
\]

### 4.7 Universal axial mobility law — **Exact certificate-backed rank identity; audit-hardened proof status**

For every integer $N\ge3$,
\[
\boxed{
\alpha_N^{\mathrm{pen}}=\frac{640}{N(N^2-1)^3}.
}
\]
The accepted coefficient registry is finite and case-complete: the stable-rank walled-Brauer contraction covers every $N\ge7$, while finite-rank certificates give
\[
\alpha_3^{\mathrm{pen}}=\frac5{12},\qquad
\alpha_4^{\mathrm{pen}}=\frac{32}{675},\qquad
\alpha_5^{\mathrm{pen}}=\frac1{108},\qquad
\alpha_6^{\mathrm{pen}}=\frac{64}{25725}.
\]
Direct substitution verifies the same rational law at all four exceptional ranks. In v1.4 this is an exact cross-rank coefficient identity **relative to the accepted rank certificates**. If those rank certificates share the same unclosed degenerate folded-effective-Hamiltonian or magnetic-normalization step identified in the `SIMULATIONS/` audit, their final theorem-grade promotion inherits that dependency; the rank identity itself is not numerically altered by the audit.

The threshold $N\ge7$ has a structural origin: a fourth-order word contains at most six character factors, so a determinant/$N$-ality channel requires $|p-q|=N$ with $p+q\le6$, impossible for $N\ge7$. Hence the exceptional set is exactly
\[
\boxed{\{3,4,5,6\}}.
\]

The first fourth-order finite-volume lift of the caged branch is
\[
\boxed{
\Delta_{N,L}^{(4)}=\alpha_N^{\mathrm{pen}}\sin^2\frac{\pi}{L},
}
\]
independent of the second pencil coefficient.

### 4.8 Exceptional-rank ledger and the $SU(3)$ anomaly

The resolved determinant sectors leave the universal axial coefficient unchanged:

| Rank | exceptional families | certified rest correction | $\Delta\alpha_N^{\mathrm{pen}}$ |
|---|---|---:|---:|
| $SU(4)$ | $(4,0),(0,4),(5,1),(1,5)$ | $-304746539168/160249753125$ | $0$ |
| $SU(5)$ | none | $0$ | $0$ |
| $SU(6)$ | $(6,0),(0,6)$ | $6/343$ | $0$ |

For $SU(5)$ the mod-5 scan is empty across the recorded 895,524 support/output pairs. For $SU(6)$ the determinant channel is on-site and produces $\Delta q_6=6/343$.

The second pencil coefficient has one exceptional anomaly. The stable expression agrees with the independently certified values at $N=4,5,6$ but not at $N=3$:
\[
\boxed{
\Delta\beta_3^{\mathrm{pen}}=-\frac{25}{64}=-\frac{15}{16}\alpha_3^{\mathrm{pen}},
\qquad
\Delta\alpha_3^{\mathrm{pen}}=0.
}
\]
Equivalently,
\[
\boxed{\Delta C_3^{\mathrm{shp}}=-\frac{25}{1024}}
\]
with $A_3^{\mathrm{shp}},B_3^{\mathrm{shp}},D_3^{\mathrm{shp}}$ unchanged. The antisymmetric ladder truncates at $SU(3)$ because $\Lambda^3V$ is already the singlet; the stable channel content requiring $\Lambda^4V$ is absent.

Therefore the broad quotient-scalarity statement
\[
P_{\rm cage}H^{\det}P_{\rm cage}=\delta q_NP_{\rm cage}
\]
**fails at $N=3$**. It is certified at $N=4$ and $N=6$, vacuous at $N=5$, and any conjectural generalization must be restricted to $N\ge4$.

### 4.9 Exact coefficient anchors and provenance

**v1.4 proof-status note.** The rational $SU(3)$ values below are retained exactly, because the independent audit reproduces the same band edges, bandwidth, and directional curvatures. They are now classified as an **exact-arithmetic computational ledger — audit pending**, not as a cold end-to-end computer-assisted theorem. The audit challenges certificate completeness, not the reproduced rational values.

For $SU(3)$,
\[
q_3=-\frac{20721577909065127111}{7250590288602460800},
\qquad
\alpha_3^{\mathrm{pen}}=\frac5{12},
\]
\[
\beta_3^{\mathrm{pen}}=\frac{17607806155349}{275331901291200}.
\]
Thus
\[
(A_3^{\mathrm{shp}},B_3^{\mathrm{shp}},C_3^{\mathrm{shp}},D_3^{\mathrm{shp}})
=\left(
\frac5{48},0,
-\frac{211835444920651}{4405310420659200},0
\right).
\]

For $SU(4)$,
\[
q_4=-\frac{162485785670299274695454289332603}{121294607143027203361265133093750},
\]
\[
\alpha_4^{\mathrm{pen}}=\frac{32}{675},
\qquad
\beta_4^{\mathrm{pen}}=\frac{3601925923737103752887}{70481696720359496343750}.
\]
The exceptional matrix is not a scalar multiple of $I_3$ on the full one-flux space; the certified statement is the all-zone branch identity
\[
H_{4,4}^{\rm exc}(k)\psi(k)=\Delta q_4\psi(k).
\]

For $SU(5)$ and $SU(6)$, the 2026-08-08 homological-flat-band paper promotes the finite-rank certificates into the current Layer-II status authority: $\alpha_5^{\mathrm{pen}}$ and $\alpha_6^{\mathrm{pen}}$ are exact as above, the second pencil coefficient agrees with the stable expression at both ranks, $SU(5)$ has no determinant sector, and $SU(6)$ has the exact rest correction $6/343$. This master document does not invent unreproduced giant rational forms that are not printed in the supplied source.

### 4.10 Physical scope of the one-plaquette band

These theorems are fixed-lattice, finite-order statements inside the one-excitation truncation. They do not identify the caged one-plaquette state with the physical $1^{+-}$ glueball. The matched Monte Carlo audit instead finds the raw one-plaquette $\operatorname{ImTr}$ operator carries spectral weight $0.0072\pm0.0165$, while the smeared basis couples at amplitude about $0.80$. The physical state is extended; the one-plaquette result is an exact operator/geometry seed, and physical completion runs through smearing and multi-plaquette dressing.

### 4.11 $SU(3)$ fourth-order audit firewall

The independent `SIMULATIONS/` audit separates the $O(y^4)$ result into what is already algebraically secure and what still requires certificate closure.

#### Retained exact computational ledger

The audit independently reproduces
\[
c_4(\Gamma)=
-\frac{20721577909065127111}{7250590288602460800},
\]
\[
\boxed{
\Delta c_4=
\frac{132329431693349}{275331901291200}
\approx0.48061786909826,
}
\]
and the directional curvatures
\[
\kappa_{100}=\frac5{24},
\qquad
\kappa_{110}=\frac{247051057231349}{2202655210329600},
\qquad
\kappa_{111}=\frac{132329431693349}{1651991407747200}.
\]
The exact shape coefficient $A=5/48$ and the two consistency identities among the ray curvatures are also reproduced. These values remain the canonical computational ledger.

#### Six theorem-closure gates

1. **Model-space scalar gate:** verify rather than assume
   \[
   PVP=aP.
   \]
2. **Degenerate folded-formula gate:** regression-test the folded des-Cloizeaux effective Hamiltonian on a genuinely multidimensional degenerate model space, including off-diagonal hopping.
3. **Independent-regression gate:** extend Stage 3H from 1,478 to all 3,895 topologies, including the 2,417 mixed/all-resonant folded cases.
4. **Magnetic-normalization gate:** prove the convention-dependent plaquette prefactor already absorbed into the perturbative variable and lock a source-to-canonical normalization identity.
5. **Interval-rigor gate:** remove the point-to-interval wraps for `theta`, `delta`, `plo/phi`, and tile the Brillouin zone using outward-rounded $\pi$.
6. **Touching/uniformity gate:** control the region $|k|\lesssim y$ where the $O(y^2)$ branch separation vanishes as $y^2|k|^2$ and becomes comparable to the $O(y^4)$ correction.

Two additional reproducibility tasks are mandatory before archival theorem status: ship `DATA_Y4_full_real_space_h4_kernel.json.gz` with a reference SHA-256, and correct the downstream use of the rigid $-2.5134$ component where the physical band minimum requires $c_4(\Gamma)\approx-2.857916$.

#### Status consequence

Until these gates close, the strongest defensible wording is
\[
\boxed{
\text{$SU(3)$ first dispersion at fourth order: exact-arithmetic computational result, heavily cross-checked.}
}
\]
It is **not yet** a cold, end-to-end computer-assisted theorem. In particular, the interval code's current `proved=true` flag should be read as decisive numerical certification of the implemented function, not as fully rigorous interval enclosure of the continuous Brillouin zone.

#### Extrapolation firewall

The short strong-coupling series is not controlled as a continuum extrapolation. The available five-term Borel-Pade estimates are consistent with the lattice scale but do not converge tightly enough to support a parameter-free continuum glueball prediction. The correct status remains
\[
\boxed{\text{consistent, not controlled}.}
\]

## 5. Layer III — Seam analyticity (the strong/weak crossover)

### 5.1 The exceptional-point atlas — **Computationally verified**, two points **Kantorovich-certified to 12 digits**
For \(H(\beta)=\operatorname{diag}(\tfrac12C_2)-\tfrac{\beta}{6}(X+X^{\!\top})\) on \(SU(3)\) class functions (K-stable to \(10^{-14}\) across \(K=16\ldots28\)):

| sector | \(\beta_c\) | \(|\beta_c|\) | angle | colliding pair |
|---|---|---|---|---|
| even | \(+0.797842828512+1.389351779364i\) | **1.6021** | 60.13° | **\(E_0\!\leftrightarrow\!E_1\) (vacuum–gap EP)** |
| even | \(-2.274880566451+0.838479039787i\) | **2.4245** | 159.8° | \(E_1\!\leftrightarrow\!E_2\) |
| even | \(-0.0036+0.3638i;\ -0.4737+0.7948i;\ +2.6993+0.2303i\) | — | — | \(E_2E_3;\ E_4E_5;\ E_3E_4\) |
| odd | \(+0.4578+0.8204i;\ -0.0332+1.6904i;\ +2.2554+2.1895i\) | — | — | \(O_2O_3;\ O_4O_5;\ O_0O_1\) |

The two governing EPs are certified via the bordered complex-symmetric system \((H-E)v=0,\ \ell^{\!\top}v=1,\ v^{\!\top}v=0\) (residuals \(\sim10^{-16}\), Kantorovich \(h<1/2\) with large margin; interval arithmetic and truncation-tail bounds queued for full rigor).

### 5.2 The odd-sector structure theorem — **Proven mechanism + machine-verified**
Because the dominant singularity is a vacuum–gap collision, symmetric functions of the pair are analytic there. With \(S=E_0+E_1\), \(G:=O_0-S/2\):
\[
\boxed{\Delta^-(\beta)=G(\beta)+\tfrac12\Delta^+(\beta),\qquad G\ \text{analytic on}\ |\beta|<2.4245.}
\]
Direct verification at \(\beta_c\): \(G\)'s branch residual \(3.0\times10^{-5}\) vs raw \(\Delta^-\)'s \(1.5\times10^{-1}\). Consequences: the odd tower's radius is **inherited entirely from even-sector physics** (the vacuum EP at 1.6021, not \(O_0\)'s own first EP at 3.14); squaring removes the \(E_0E_1\) branch points, so \((\Delta^+)^2\) converges on \(|\beta|<2.4245\) — the exact analytic reason the manuscript's Theorem-4.2 closure \(\Delta^+=\sqrt{\tfrac12+\tfrac23\beta\,g(\beta)}\) reaches \(9.5\times10^{-4}\) while every raw Padé stalls at \(6.1\times10^{-2}\); 2.4245 is its hard ceiling (obstruction: the \(E_1E_2\) collision at negative coupling). Three independent consistency checks (level-repulsion minimum near \(\beta\approx0.8\); period-6 sign pattern of \(b_1\ldots b_6\) predicting 60°; root-test/seam profile) all agree.

### 5.3 Two-sector certified crossover v1 — **Computationally verified**
With exact strong towers through \(\beta^6\) and the exact weak identity
\(G\sim\sqrt{2\beta/3}-\tfrac7{32}-\tfrac{1271\sqrt6}{55296}\beta^{-1/2}-\tfrac{7903}{221184}\beta^{-1}\)
(leading term exact: \(\sqrt{3\beta/2}-\tfrac12\sqrt{2\beta/3}\equiv\sqrt{2\beta/3}\)), pole-free two-point rationals in \(x=\sqrt\beta\) on \(\beta\in[0.25,50]\) achieve: \((\Delta^+)^2\to\Delta^+\): \(3.3\times10^{-2}\); \(G\): \(1.3\times10^{-2}\); assembled \(\Delta^-\): \(1.9\times10^{-2}\) — the odd sector's **first controlled crossover**. Recorded failure mode: the maximal exactly-determined system amplified a \(10^{-3}\) tower inconsistency into 84% error; standing rule — **gate the fit residual, not just pole-freeness**.

---

## 6. Layer IV — Transfer geometry and certificates

### 6.1 Wilson–Bergman weight theorem — **Proven** (+8/8 gates)
The weight \(w_\lambda(\beta)=\int_{SU(N)}|\chi_\lambda|^2e^{\beta((2/N)\operatorname{Re\,tr}g-2)}dg\) is a Bessel–Toeplitz determinant:
\[
w_\lambda(\beta)=c_N(\beta)\sum_{s\in\mathbb Z}
\det\left[ I_{\ell_a-\ell_b+s}(\kappa)\right]_{a,b=1}^{N},
\qquad \ell=\lambda+\rho,\quad \kappa=\frac{2\beta}{N}.
\]
**Theorem A (repaired):** \(\|M_q\|=\operatorname{ess\,sup}q=q(1)=(2N)^k\) despite the Weyl density vanishing to order \(2|\Phi^+|\) at the maximizer — and the supremum is **not attained**: shell-\(K\) truncations obey \((2N)^k-\lambda_{\max}(K)\asymp C/K^2\) (Laplace mechanism; measured exponent 1.91 over \(K=48\to96\)). Practical license: shell-\(K\) transfer estimates may use \(\lambda_{\max}(K)\) (e.g. 1208 vs 1296 at \(K=24\)). The earlier "N-uniform \(\|M_q/q(1)\|=1\)" claim is **Withdrawn** as vacuous.

### 6.2 Bergman-transfer closure at ranks one and two — **Computationally verified**
The ledger's radial-tail no-go prescribed "a different transfer norm." Its concrete instantiation — compact-alcove character basis + Wilson–Bergman weights, matrix entries as Bergman-norm ratios of adjacent weight-lattice points — **closes the tail** with no \(n^2\) growth: at rank one (SU(2) toy) and at rank two (SU(3) chamber), after quasi-degenerate blocking of the C-conjugation strips with fixed threshold \(|\Delta C_2|\le1\) (provably terminating; max 5 band partners; min nonresonant gap exactly \(4/3\)); \(\sup T=457,593,631\) at \(\beta=4,16,64\). The quartic Wilson object has exact integer character entries, exact bandwidth 4, exact deep-chamber translation invariance (rank-two linearization constant 90). The resonant \(\delta\)-blocks are exactly where a real PMBSF secular analysis must live.

### 6.3 Exact computer-assisted certificate stack — **Proven — exact computer-assisted**
\(SU(3)\) fourth-order real-space SOS theorem (positive local sum of squares); Stage-2A local projector theorem; Stage-3G targeted reduction; full-symbolic \(N\ge7\) walled-Brauer certificate with independent audit (all exact gates pass; runtime provenance limitation only); 387 lower-order hard gates rerun cold; hashed 189-record kernel and payload identities; the 2026-08-01 21-gate seam suite. Certificates are identified by SHA-256 and never overridden by prose.

### 6.4 Limitation theory (Direction 3) — **Program, pre-registered**
Template: transplant fixed-degree sign-uncertainty limitation theorems (Cohn–Dong–Gonçalves-type) through the compact-to-Euclidean contraction of the two-cone certificate geometry, with effective dimension \(\lambda_{\mathrm{eff}}\sim(N^2-1)/2\) and the quartic Weyl barcode \((N^2-1)(N^2-4)(N^2-9)/[4(N^2+1)]\) counting the opening angular channels. Kill criterion: if the Mellin multiplier of the \(u^{\alpha_N}e^{-u}\) weight is not of \(\Gamma\)-ratio type, the transplant fails structurally. Established substrates for the positive side: Ozawa / Netzer–Thom / Kaluba–Nowak–Ozawa group-ring SOS; DFPR Lie–Schwinger block-diagonalization for the KS gap (its finite-local-dimension hypothesis is the single obstruction to re-prove for \(L^2(SU(3))\) links).

---

## 7. Layer V — Marginal stability and projected capacity

### 7.1 Curvature sources — **Proven**
Root second-moment identity \(\sum_\alpha\alpha\otimes\alpha=2h^\vee I\); Weyl potential curvature floor \(\nabla^2[-\log|\Delta|^2]\succeq h^\vee I/2\), exactly \(N/2\) on \(\mathbf1^\perp\) for \(SU(N)\); exponential-coordinate Haar Hessian \(h^\vee I/6\) at the identity. Fixed-seed Hessian checks exceed the floor for \(N=3,4,5,8,10\) (**CV, reproduced**).

### 7.2 Exact marginalization — **Proven**
Helffer–Sjöstrand covariance representation on the conditional fiber; leakage bound \(\nabla^2_xS_{\mathrm{eff}}\succeq\mathbb E\nabla^2_{xx}S-M^2I/\gamma\); coercivity form \(K_0-V\succeq(1-\Theta)\rho_0I\) with \(\rho_0=\sigma-M^2/\gamma>0\), \(\Theta<1\).

### 7.3 Decay machinery
Finite-range Combes–Thomas inverse bound with conservative rate \(\eta_{\mathrm{CT}}=R^{-1}\log(1+a_0/(2B_0))\) (**Proven**); for the 4d co-plaquette metric \(a_0=m^2\), \(B_0=18\alpha\), \(R=1\), \(C_0=D_E=18\). The sharper Davies–Gaffney \(2\operatorname{arsinh}(m/2\sqrt{\alpha k})\) rate remains **Conjectural** (finite \(L=16\), \(d=4\) certificate only, phase-corrected, max ratio \(0.1411851688849\)).

### 7.4 Capacity: the correct global object — mixed status, sharply resolved
- Canonical incidence-shadow capacity \(\mathcal K_{\Lambda,L}(\Gamma)=\|P\mathbf1_{C(\Gamma)}P\|\le1\) and the rooted polymer bound with **one** mark
\(\mathfrak Z_{p_0}\le C_{\mathcal P}e^{s\gamma}\,\mu z e^a/(1-\mu z e^a)\), Peierls activity \(z=K_\alpha e^{-(1-\alpha)\beta\delta}\) — **Proven as implications**.
- **Global fixed-window firewall is false**: for Bernoulli defects of fixed density the projected top norm tends to one (**Proven no-go**). The correlated Wilson analogue of the rare-island result is **Conjectural/Open**.
- Caged-band capacity sandwich \(P^G_{\Lambda/c_+}\preceq P^M_\Lambda\preceq P^G_{\Lambda/c_-}\) — **Proven** from sharp mobility ellipticity: every positive projected support capacity of the caged band is squeezed between ordinary lattice-Laplacian capacities.
- PC chain: source-tilt identity **Proven** (PC-1); Peierls, square-free Wilson-to-Bernoulli domination, rooted summability **Proven implications** (PC-3,4,6); the two load-bearing hypotheses — **Wilson free-energy stability \(Z_{\beta,\alpha,\Gamma,L}/Z_{\beta,L}\le K_\alpha^{|\Gamma|}\) (PC-2)** and the **source-radius reduction** — are **Open**.
- PMBSF conditional spine: \(\boxed{(\mathrm{ML})\Rightarrow\text{Wilson-typical projected capacity}\Rightarrow\text{finite-lattice projected coercivity}}\); matrix-Laplace domination (ML) is **Open**; the earlier Wilson-to-block "proof" is **Withdrawn**; deterministic block lemmas survive; v7 fixed-window SU(2) comparisons are the highest-authority computational evidence; \(\mathrm{BM}(q)\) vs \(\mathrm{EC}(q,\ell)\) are distinct properties requiring a defect-localization bridge (**Open** O5).

### 7.5 The PMBSF SU(2) conditional paper (v1.1) — the probability side as a theorem stack
The vague instruction "prove Lemma Q" is replaced by a proven reduction chain with two named analytic inputs. Guiding deterministic objects: projected plaquette atoms \(A_p=P\mathbf1_{\partial p}P\) and the Birman–Schwinger criterion \(\Theta_D=\|M^{-1/2}PV_DPM^{-1/2}\|<1\) (finite-dimensional, unconditional). Central probabilistic input, **Lemma Q** (conditional rare-source factorization, with rooted version):
\[
\mathbb{E}\!\left[\prod_{p\in B}X_{p,\eta}\mid\mathcal{F}_{C^c}\right]
\le (C_Qq_\eta)^{|B|}.
\]
**Proven interface:**
\[
\mathrm{LCI}_{\mathrm{good}}+\mathrm{BFS}_{\mathrm{far}}
\Rightarrow \mathrm{TOS+J}
\Rightarrow Z_A(\rho/q_\eta)\le e^{K|A|}
\Rightarrow \text{Lemma Q}.
\]
\[
\text{Lemma Q}+\mathrm{SWB}+\mathrm{BBG}
\Rightarrow \text{firewall closure}.
\]
The **positive source-radius pivot** replaces fragile product-moment/mixing arguments and needs no complex zero-free region: \(Z_A(s)=\sum_{R\subset A}s^{|R|}\mathbb E\prod_RX_p\) is a factorial-moment generating function with nonnegative coefficients, so \(s^{|B|}\mathbb E\prod_BX_p\le Z_B(s)\) (strict when \(q_\eta>0\)); the exact per-step ratio \(Z_{A\cup\{p\}}/Z_A=1+s\,\mathbb E_{\mu^{A,s}}X_p\) telescopes under an exponentially summable influence kernel (\(J_*<\infty\)) to \(K=\rho\,C_{\mathrm{TOS}}e^{J_*}\), with canonical optimum
\(\rho_{\mathrm{opt}}=1/(C_{\mathrm{TOS}}e^{J_*})\), \(C_Q^{\mathrm{opt}}=e\,C_{\mathrm{TOS}}e^{J_*}\) (convex in \(\rho\)). Rooted bounds are soft conditionings costing one \(e^{J_*}\) per root.
**Local geometry is exact:** the SU(2) one-link conditional law is \(\mathrm{vMF}_4(\overline H_e/\|H_e\|,\beta\|H_e\|)\) on \(S^3\); plaquette scores are linear, \(\tfrac12\operatorname{Re\,Tr}U_r=u\cdot n_r\), so incident sources are spherical-cap intersections — \(\mathrm{LCI}_{\mathrm{good}}\) is a finite-dimensional \(S^3\) cap-intersection theorem for a log-concave density. The far field enters only through \(\mathrm{BFS}_{\mathrm{far}}\) (Bałaban/Dimock source-weighted far stability with \(J(p,r)\le C_Je^{-m_Jd_C(p,r)}\)).
**Open inputs of this stack:** \(\boxed{\mathrm{LCI}_{\mathrm{good}}}\) and \(\boxed{\mathrm{BFS}_{\mathrm{far}}}\) (plus the separate \(\mathrm{SWB}\), \(\mathrm{BBG}\) gates). Diagnostics at the working point \(\beta=3.5\), \(q_\eta=0.003\), \(\eta=0.005\) (frozen-block heat-bath through side-10, full-volume covariance through \(L=64\)) are motivational only. The compact SU(3) remainder proof explicitly does **not** revive the archived global top-norm program; the two tracks stay firewalled.

---

## 8. Contact with physics: verification layer

- **Replay gate — verified.** The hardcoded Athenodorou–Teper \(T_1^{+-}\) table is a digit-for-digit faithful transcription of arXiv:2007.06422 (all 25 verifiable cells match); continuum \(M(1^{+-})/\sqrt\sigma=6.065(40)\approx2.944(42)\) GeV, cross-consistent with Morningstar–Peardon and Chen et al.
- **Like-for-like Monte Carlo — passed (23/23 hard gates, 21-gate suite green).** Hardened spatial MC at matched volume and coupling: \(aM(T_1^{+-})=1.6897\pm0.121\) vs published \(1.591(18)\) — pull \(+0.82\); string scale \(+0.71\sigma\); conditioning fix at \(7.97\times10^3<10^4\) spec; throughput \(7.1\times10^5\) site-sweeps/s. **The scientifically loaded number:** the raw single-plaquette \(\operatorname{ImTr}\) operator carries \(0.0072\pm0.0165\) (< 4% at \(2\sigma\)) of the physical glueball, while the smeared basis couples at amplitude 0.80 — the physical \(T_1^{+-}\) state is extended. This converts the program's scope firewall (one-plaquette bridge = operator identity, physical completion runs through smearing) from precaution into **measured fact**.
- **Peter–Weyl and coordinate audits.** Compact \(SU(3)\) audit confirms the three-term law (AUD-1); exact rational Wick/Gram closures pass for \(N=3\ldots12\) even and odd (AUD-2/3); corrected GPU Weyl-triangle solver exists but **no CUDA execution certificate** yet (AUD-4 Open); the 21-gate suite validates triangle/character agreement (the Weyl-denominator conjugation numerically).
- **Structure predictions.** The shell decomposition (§4.6) reproduces the lattice's channel assignments at shell 4 and predicts the exotic C-odd ordering questions (e.g. \(0^{--}\) vs \(3^{+-}\)) as controlled shell-6 splittings — structure, not masses.

---

## 9. Master dependency graph

![Master dependency graph for the five-layer theory](dependency_graph_v14.png){width=95%}

The dependency graph separates proved structural nodes, scoped exact certificates, audit-pending computational ledgers, and open closure gates; arrows denote interfaces and dependencies, not automatic theorem promotion.

---

## 10. Canonical constants index (selected)

### 10.1 Couplings and local class geometry

- **Canonical strong-coupling variable:** \(u=\beta_H/6\). **Status:** Proven bridge.
- **Weyl-Gaussian radial parameter:** \(\alpha_N=(N^2-3)/2\). **Status:** Proven.
- **Compact \(SU(3)\) even gap:** \(c_0^+=-5/16\), \(c_1^+=-311\sqrt6/9216\). **Status:** Proven.
- **First non-radial escape:** \(\sqrt6/576\). **Status:** Proven.
- **Fixed-rank constants:** \(c_0^{(N)}=-(2N^2-3)/(16N)\) and \(c_0^{(N),-}=-3(N^2-3)/(16N)\). **Status:** Proven.
- **Polarity excess:** \(9/(32N)\). **Status:** Proven corollary.
- **Exact \(SU(3)\) next coefficients:** \(c_2^+=-5665/110592\), \(c_1^-=-551\sqrt6/13824\), \(c_2^-=-53/864\). **Status:** Exact arithmetic; the higher-order analytic remainder remains separate.

### 10.2 Strong-coupling mobility

- **Second-order rank scalar:**
  \[
  t_N=\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)},\qquad N\ge3.
  \]
  **Status:** Proven.
- **Flat-space dimension on $T_L^3$:** $L^3+2$. **Status:** Proven.
- **First level above the flat carrier:** $4\sin^2(\pi/L)$. **Status:** Proven.
- **Universal fourth-order axial pencil coefficient:**
  \[
  \boxed{\alpha_N^{\mathrm{pen}}=\frac{640}{N(N^2-1)^3}},\qquad N\ge3.
  \]
  **Status:** Exact certificate-backed rank identity; end-to-end theorem promotion inherits any shared folded-effective-Hamiltonian/normalization gates identified by the v1.4 audit.
- **Exceptional axial values:** $\alpha_3=5/12$, $\alpha_4=32/675$, $\alpha_5=1/108$, $\alpha_6=64/25725$.
- **$SU(3)$ second-pencil anomaly:** $\Delta\beta_3^{\mathrm{pen}}=-25/64$, equivalently $\Delta C_3^{\mathrm{shp}}=-25/1024$. **Status:** Exact relative to the accepted finite-rank/stable certificates.
- **$SU(4)$ exceptional rest shift:** $\Delta q_4=-304746539168/160249753125$. **Status:** Proven relative to the narrow $SU(4)$ exceptional certificate; shared upstream folded-formalism dependence should be stated if applicable.
- **$SU(5)$ determinant sector:** empty. **Status:** Exact finite-rank scan in the 2026-08-08 Layer-II authority.
- **$SU(6)$ exceptional rest shift:** $\Delta q_6=6/343$. **Status:** Exact finite-rank certificate as summarized in the 2026-08-08 Layer-II authority.
- **Physical tier collapse:** $B_N^{\mathrm{shp}}=D_N^{\mathrm{shp}}=0$ for every resolved rank, now covering the complete rank partition $N\ge3$. **Status:** Exact within accepted coefficient ledgers; theorem-grade promotion is audit-sensitive where a rank shares the unclosed fourth-order effective-Hamiltonian pipeline.
- **$SU(3)$ pencil:** $q_3$ as in §4.9, $\alpha_3^{\mathrm{pen}}=5/12$, $\beta_3^{\mathrm{pen}}=17607806155349/275331901291200$. **Status:** Exact-arithmetic computational ledger — audit pending; values independently reproduced, six theorem-closure gates remain.
- **$SU(4)$ pencil:** $q_4$ as in §4.9, $\alpha_4^{\mathrm{pen}}=32/675$, $\beta_4^{\mathrm{pen}}=3601925923737103752887/70481696720359496343750$. **Status:** Proven - exact computer-assisted.

### 10.3 Seam, transfer, and global diagnostics

- **Vacuum exceptional point:** \(0.797842828512+1.389351779364i\). **Status:** Kantorovich-certified at the recorded truncation.
- **Squared-gap analytic radius:** \(2.4245\), controlled by the \(E_1\leftrightarrow E_2\) exceptional point. **Status:** Computationally verified.
- **Wilson-Bergman multiplier norm:** \(\|M_q\|=(2N)^k\), with truncation deficit \(\asymp C/K^2\). **Status:** Proven plus verified.
- **Finite-channel leakage Perron root:** \(0.5501615335\ldots\). **Status:** Computationally verified; not a full-channel constant.
- **Combes-Thomas data in four dimensions:** \(a_0=m^2\), \(B_0=18\alpha\), \(C_0=18\). **Status:** Proven.
- **Matched Monte Carlo mass:** \(1.6897\pm0.121\) versus \(1.591(18)\), pull \(+0.82\). **Status:** Computationally verified.
- **Raw single-plaquette overlap:** \(0.0072\pm0.0165\). **Status:** Measured.

---

## 11. The firewall: what the master theory does **not** claim

No result in this theory establishes, and none is presented as establishing: convergence of the strong-coupling series beyond \(|\beta_c|\); a continuum \(1^{+-}\) glueball mass or a controlled \(m_{1^{+-}}/\sqrt\sigma\); a pseudoreal \(SU(2)\) extension of the \(N\ge3\) mobility theorem; an all-orders localization theorem; infinite-volume Wilson exponential clustering; identification of local class gaps with glueball masses; confinement or a string tension from the present coefficients; Osterwalder–Schrader reconstruction; a valid 4d \(SU(2)\) \(\theta\)-vacuum partition function or topological susceptibility; or the four-dimensional Yang–Mills mass gap. The strong-coupling mobility theorems, the compact large-\(\beta\) class asymptotics, and the global Wilson-measure program are three separately controlled regimes; the theory's unification is of **structure and method**, and each proved formula is confined to its regime.

---

## 12. Open frontier: the load-bearing inputs and pre-registered tests

**Layer-II frontier after the 2026-08-08 closure:** the axial fourth-order coefficient is no longer an open-rank problem. The immediate mobility questions are (i) whether the $b_2$-fold protected level survives coupling to multi-plaquette sectors, (ii) a clean cold rerun of the named third-order $SU(3)$ certificate chain before submission, and (iii) extension of the Betti-count theorem to noncubic cellulations with independently tunable $b_2$. The $SU(5)$/$SU(6)$ axial closure and the $SU(3)$ second-pencil anomaly are now part of the theorem registry, not frontier items.

**Seven inputs on which the next tier of the theory turns:**
1. **Symbolic-\(N\) Gram transcript** for the even/odd inverse-Gram resolvent identities -> promotes the \(c_1^{(N),\pm}\) **and the new \(c_2^{(N),\pm}\)** candidates to unrestricted fixed-rank theorems.
2. **Compact Casimir-shell buffered Schur-complement theorem** (SU3-10) -> the surviving route to a genuine full-channel local constant.
3. **\(\mathrm{LCI}_{\mathrm{good}}\) + \(\mathrm{BFS}_{\mathrm{far}}\)** — the PMBSF SU(2) paper's two named analytic inputs (they imply TOS+J -> positive source radius -> Lemma Q), together with the separate \(\mathrm{SWB}\) and \(\mathrm{BBG}\) gates; on the Peierls route, **PC-2 Wilson free-energy stability** with useful \(\log K_\alpha\) plus the **source-radius reduction** remain the parallel open pair.
4. **Matrix-Laplace domination (ML)** or a replacement giving the same Wilson projected-capacity tail -> discharges the PMBSF conditional spine.
5. **Certified crossover v2** (extended exact towers via validated Cauchy extraction; conformal-map two-point builds with residual gating; interval-rigorous EP certificates including truncation tails) -> Theorem-4.2-class \(10^{-3}\!-\!10^{-4}\) accuracy in **both** sectors — now feedable with the four-term weak towers of §3.2b.
6. **The KS finite-dimensionality re-proof** in the DFPR Lie–Schwinger scheme for \(L^2(SU(3))\) links -> an explicit-threshold infinite-volume KS gap theorem, which would be new to the literature.
7. **One more order of the equivariant harmonic-well lemma** (quasimode residual \(O(h^5)\)) -> promotes the exact \(c_2\) values to a proven \(O(\beta^{-3/2})\) remainder; and **closing the small-rank verification gaps** (even \(N=4,5\); odd \(N=4,5,6\)) via rank-reduced invariant bases, as done for \(SU(3)\) with \(\{p_2,p_3\}\).

**Pre-registered tests with kill criteria (2026-08-01 ordering):**
- **T1(a):** derive the Mellin multiplier of the \(u^{\alpha_N}e^{-u}\) weight; if not of \(\Gamma\)-ratio type, the limitation transplant downgrades to method-inspiration. Then run the Direction-3 primal at \(N=3,4,6\) against the \((1/\pi)\sqrt d\)-type localization scaling.
- **T3 + audit item 3:** re-run the \(A'\) budget with amortized-KL/coupling accounting and the sharpened incidence constant 16; require **\(\ge100\times\)** improvement or drop the direction.
- **T2:** exponential-tilt check between exact strong and weak towers (compact-optimizer -> Euclidean-optimizer degeneration), feeding crossover v2.
- **T4 continuation:** SU(N) chamber generalization of the Bergman blocking (conjugation-strip \((N-1)\)-torus; block sizes conjectured N-independent — checkable), then recast the actual Lemma-Q/\(A'\) tails in the Bergman norm with \(\delta=1\) bookkeeping.
- **MC campaign, staged:** three next-coarsest ensembles (~3 A100-days) -> four-point continuum fit; re-anchor at \(26^3\); overlap-vs-APE-level flow measurement of the raw-fraction number.

---

## 13. Closing statement

The theory's core is a matched pair of exact escape theorems — \(\sqrt6/576\) internally and the exact fourth-order mobility pencil spatially — together with the physical tier collapse \(B_N^{\mathrm{shp}}=D_N^{\mathrm{shp}}=0\) across the complete resolved rank partition \(N\ge3\) and the universal axial law \(\alpha_N^{\mathrm{pen}}=640/[N(N^2-1)^3]\) — with the internal tower now certified three corrections deep in both C-sectors and its analytic remainder proved in-corpus, welded by the Hodge complex's kernel–resolvent duality, extended along the coupling axis by an EP-certified analytic seam, equipped with a working transfer norm (Wilson–Bergman) and an exact certificate stack, and pointed at the global regime through a rooted capacity calculus whose two open hypotheses are precisely named. Everything Proven here is regime-scoped and hash-anchored; everything Open is listed with the experiment that would close or kill it. That discipline — filtration, rigidity, exact first escape, and an honest firewall — **is** the master theory.

---

# Appendices: detailed proof and certificate insertions


## Appendix 0. Audit quarantine: results excluded from the master theorem graph

The following threads are explicitly **not** premises of Gauge-Constrained Spectral Geometry v1.4.

1. **Schur/Haar-Hessian “Theorem B”.** The claimed bound $\rho_{\mathrm{eff}}\ge N/2-M^2/\gamma$ is rejected in its published-notebook form: its Schur-complement positivity precondition fails on a substantial set, the Haar Hessian is unbounded below near eigenangle collisions, median-based clipping cannot substitute for a uniform lower bound, and the reported $N$-growth is imposed by the chosen $\beta\propto N$ scan. The separately derived analytical Wilson+Haar Hessian formula is salvageable as a technical calculation, but it does not prove a lattice spectral gap.
2. **4D $SU(2)$ $\theta$/TRG thread.** The audited implementation does not yet encode the Wilson plaquette action, does not implement the claimed $\theta$ dependence, and does not perform a validated 4D coarse-graining. It is excluded from all physics claims. The underlying Levin-Nave `trg_step` kernel is salvageable when supplied with a correct benchmark tensor.
3. **q-Racah/Doob gap novelty claim.** The clean implementation is correct but reproduces the standard $n=1$ q-Racah/Askey-Wilson eigenvalue and therefore is treated as a validation/utility result, not a new theorem.

## Appendix A. Compact $SU(3)$ class-gap remainder closure

The following proof is the detailed analytic insertion underlying §3.1. It is reproduced from `SU3_Compact_Remainder_Proof.docx`. The exact reduced-resolvent value
\[
\Delta_{\mathrm{res}}=-\frac{205\sqrt6}{3072}
\]
is inherited from the exact oscillator coefficient ledger; the accompanying verification script checks the invariant identities, moments, direct sextic term, and final assembly, but does not independently reconstruct that reduced-resolvent matrix element.

**Status:** rigorous proof insertion for the local theorem  
**Scope:** fixed-rank $SU(3)$, charge-conjugation-even class sector, $\beta \rightarrow \infty$  
**Not claimed:** an infinite-volume lattice gap, a glueball mass, or a Yang-Mills mass gap

### 1. Result

Let

$$H_{\beta} = \frac{1}{2}C_{2} + \beta\left( 1 - \frac{1}{3}Re\chi_{(1,0)}(g) \right)$$

act on square-integrable class functions on $SU(3)$, with

$$C_{2}(p,q) = \frac{1}{3}\left( p^{2} + pq + q^{2} \right) + p + q.$$

Let $E_{0}^{+}(\beta)$ and $E_{1}^{+}(\beta)$ denote the two lowest eigenvalues in the charge-conjugation-even class sector, ordered by

$$E_{0}^{+}(\beta)<E_{1}^{+}(\beta).$$

Define

$$\Delta_{SU(3)}(\beta)=E_{1}^{+}(\beta)-E_{0}^{+}(\beta).$$

Then there are constants $C < \infty$ and $\beta_{0} < \infty$ such that, for every $\beta \geq \beta_{0}$,

$$\boxed{\left| \Delta_{SU(3)}(\beta) - \left( \sqrt{\frac{2\beta}{3}} - \frac{5}{16} - \frac{311\sqrt{6}}{9216}\,\beta^{- 1/2} \right) \right| \leq C\beta^{- 1}.}$$

This closes the analytic remainder missing from the coefficient calculation.

### 2. Exact reduction to a flat torus Schrödinger operator

Let $\mathfrak{t} \cong \mathbb{R}^{2}$ be the trace-zero Cartan plane with orthonormal coordinates $(x,y)$,

$$\theta_{1} = \frac{x}{\sqrt{2}} + \frac{y}{\sqrt{6}},\quad\quad\theta_{2} = - \frac{x}{\sqrt{2}} + \frac{y}{\sqrt{6}},\quad\quad\theta_{3} = - \frac{2y}{\sqrt{6}}.$$

Let $T = \mathfrak{t}/\left( 2\pi Q^{\vee} \right)$ be the maximal torus and let

$$J(\theta) = \prod_{\alpha > 0}^{}2\sin\frac{\alpha(\theta)}{2}$$

be the real Weyl denominator. Weyl integration shows that multiplication by $J$ is unitary, up to an irrelevant normalization, from class functions to Weyl-anti-invariant functions in flat $L^{2}(T,d\theta)$.

For an irreducible character $\chi_{\lambda}$, the Weyl character formula gives

$$J\chi_{\lambda} = A_{\lambda + \rho},$$

where $A_{\lambda + \rho}$ is the alternating torus exponential. Since

$$- \Delta_{\mathfrak{t}}A_{\lambda + \rho} = |\lambda + \rho|^{2}A_{\lambda + \rho}$$

and

$$C_{2}(\lambda) = \frac{|\lambda + \rho|^{2} - |\rho|^{2}}{2},$$

the character basis proves the exact operator identity

$$J\left( \frac{1}{2}C_{2} \right)J^{- 1} = \frac{1}{4}\left( - \Delta_{\mathfrak{t}} - |\rho|^{2} \right).$$

For $SU(3)$, $|\rho|^{2} = 2$. Consequently $H_{\beta}$ is unitarily equivalent, in the appropriate Weyl-anti-invariant symmetry sector, to

$${\widehat{H}}_{\beta} = - \frac{1}{4}\Delta_{\mathfrak{t}} - \frac{1}{2} + \beta W(\theta),$$

where

$$W(\theta) = 1 - \frac{1}{3}\sum_{j = 1}^{3}\cos\theta_{j}.$$

This reduction is exact. In particular, there are no untracked metric or Haar-measure terms in the local expansion. The scalar $- 1/2$ cancels from the gap.

### 3. The Wilson potential has one nondegenerate well

Because each $\cos\theta_{j} \leq 1$,

$$W(\theta) \geq 0.$$

Equality requires $\cos\theta_{j} = 1$ for all $j$, hence $\theta = 0$ on $T$. Thus the identity is the unique global minimum. Near it,

$$W(\theta) = \frac{1}{6}P_{2} - \frac{1}{72}P_{4} + \frac{1}{2160}P_{6} + O\left( |\theta|^{8} \right),\quad\quad P_{k} = \sum_{j = 1}^{3}\theta_{j}^{k}.$$

Since $P_{2} = x^{2} + y^{2}$,

$$D^{2}W(0) = \frac{1}{3}I_{2} > 0.$$

It follows that there are $r,c_{0},c_{1} > 0$ such that

$$W(\theta) \geq c_{0}|\theta|^{2}\quad\left( |\theta| < r \right),\quad\quad W(\theta) \geq c_{1}\quad\left( |\theta| \geq r \right).$$

These are precisely the confinement hypotheses needed for compact harmonic-well asymptotics.

### 4. Correct semiclassical parameter and scaled normal form

Set

$$h = \beta^{- 1/2},\quad\quad P_{h} = \beta^{- 1}{\widehat{H}}_{\beta} = h^{2}{\widehat{H}}_{\beta}.$$

Then

$$P_{h} = - \frac{h^{2}}{4}\Delta_{\mathfrak{t}} - \frac{h^{2}}{4}|\rho|^{2} + W(\theta).$$

This is a conventional semiclassical Schrödinger operator. Its low eigenvalues are $O(h)$. Use the well scaling

$$\theta = a\sqrt{h}\, z,\quad\quad a = \left( \frac{3}{2} \right)^{1/4}.$$

In the localized well, division by $h$ gives

$$h^{- 1}P_{h} = H_{0} + hH_{1} + h^{2}H_{2} + h^{3}R_{h},$$

where

$$H_{0} = \frac{1}{2\sqrt{6}}\left( - \Delta_{z} + p_{2}(z) \right),$$

$$H_{1} = - \frac{|\rho|^{2}}{4} - \frac{p_{2}^{2}}{96},$$

and

$$H_{2} = \sqrt{6}\left( \frac{p_{2}^{3}}{11520} + \frac{p_{3}^{2}}{8640} \right).$$

The scale factors are exact:

$$a^{4} = \frac{3}{2},\quad\quad a^{6} = \left( \frac{3}{2} \right)^{3/2} = \frac{3\sqrt{6}}{4}.$$

They give

$$- \frac{a^{4}}{144} = - \frac{1}{96},\quad\quad\frac{a^{6}}{8640} = \frac{\sqrt{6}}{11520},\quad\quad\frac{a^{6}}{6480} = \frac{\sqrt{6}}{8640}.$$

Here the $SU(3)$ Newton identities

$$P_{4} = \frac{1}{2}p_{2}^{2},\quad\quad P_{6} = \frac{1}{4}p_{2}^{3} + \frac{1}{3}p_{3}^{2}$$

have been used. On every fixed finite oscillator spectral subspace, $R_{h}$ is uniformly bounded as $h \downarrow 0$. More explicitly, Taylor’s theorem gives a multiplication remainder bounded by $C\langle z\rangle^{8}$, and every vector used below is a polynomial times a Gaussian.

The scalar term $- |\rho|^{2}/4 = - 1/2$ in $H_{1}$ changes both energies equally, has no off-diagonal matrix elements, and therefore makes no contribution to the gap. Removing it recovers exactly the $H_{1}$ used in the coefficient tables.

### 5. Equivariant harmonic-well remainder lemma

#### Lemma

Let $P_{h}$ be the operator above, restricted to the Weyl-anti-invariant symmetry sector corresponding under multiplication by $J$ to charge-conjugation-even class functions. Let $\mu_{a}^{(0)}$ be a simple eigenvalue of $H_{0}$ in that sector, with normalized eigenvector $\phi_{a}$. Then the corresponding compact eigenvalue $p_{a}(h)$ of $P_{h}$ satisfies

$$p_{a}(h) = h\mu_{a}^{(0)} + h^{2}\mu_{a}^{(1)} + h^{3}\mu_{a}^{(2)} + O\left( h^{4} \right),$$

where

$$\mu_{a}^{(1)} = \langle\phi_{a},H_{1}\phi_{a}\rangle,$$

and

$$\mu_{a}^{(2)} = \langle\phi_{a},H_{2}\phi_{a}\rangle + \sum_{b \neq a}^{}\frac{\left| \langle\phi_{b},H_{1}\phi_{a}\rangle \right|^{2}}{\mu_{a}^{(0)} - \mu_{b}^{(0)}}.$$

#### Proof

Choose a Weyl-invariant cutoff $\chi$ supported in a fixed coordinate ball about $0$ and equal to one on a smaller ball. The well bounds in Section 3 and the IMS formula imply that every eigenfunction of $P_{h}$ with eigenvalue at most $Ch$ has $L^{2}$-mass outside that smaller ball smaller than $O\left( h^{N} \right)$ for every fixed $N$; the usual Agmon estimate gives the stronger exponential bound. Thus the low spectrum is determined, to $O\left( h^{N} \right)$, by the Taylor germ at the unique well.

Let $Q_{a} = I - \left| \phi_{a}\rangle\langle\phi_{a} \right|$. Because $\mu_{a}^{(0)}$ is simple in the chosen symmetry sector, the reduced inverse

$$Q_{a}\left( \mu_{a}^{(0)} - H_{0} \right)^{- 1}Q_{a}$$

is bounded on the finite polynomial-Gaussian sources generated at the orders used here. Define the first correction by

$$\phi_{a}^{(1)} = Q_{a}\left( \mu_{a}^{(0)} - H_{0} \right)^{- 1}Q_{a}H_{1}\phi_{a}.$$

The order-$h$ solvability condition gives

$$\mu_{a}^{(1)} = \langle\phi_{a},H_{1}\phi_{a}\rangle.$$

Solving once more at order $h^{2}$ gives a polynomial-Gaussian vector $\phi_{a}^{(2)}$, and its solvability condition gives

$$\mu_{a}^{(2)} = \langle\phi_{a},H_{2}\phi_{a}\rangle + \langle H_{1}\phi_{a},Q_{a}\left( \mu_{a}^{(0)} - H_{0} \right)^{- 1}Q_{a}H_{1}\phi_{a}\rangle.$$

Expanding the reduced inverse in the oscillator eigenbasis gives the displayed Rayleigh-Schrödinger sum.

After scaling back and applying $\chi$,

$$u_{a,h} = \chi\, S_{h}^{- 1}\left( \phi_{a} + h\phi_{a}^{(1)} + h^{2}\phi_{a}^{(2)} \right)$$

is a symmetry-preserving quasimode. The Taylor remainder contributes $O\left( h^{3} \right)$ to $h^{- 1}P_{h}$, cutoff commutators are $O\left( h^{N} \right)$ for every $N$, and hence

$$\left. \parallel\left\lbrack P_{h} - \left( h\mu_{a}^{(0)} + h^{2}\mu_{a}^{(1)} + h^{3}\mu_{a}^{(2)} \right) \right\rbrack u_{a,h} \right.\parallel \leq Ch^{4} \parallel u_{a,h} \parallel .$$

The harmonic approximation and the well bounds identify the low compact spectrum with the oscillator spectrum after division by $h$, including multiplicities. The relevant oscillator level is isolated and simple in the selected symmetry block, so the spectral theorem identifies one and only one compact eigenvalue in its $o(h)$ neighborhood. Its distance from the quasimode energy is $O\left( h^{4} \right)$, proving the expansion.

All operators, cutoffs, reduced inverses, and Riesz projections commute with the finite Weyl and charge-conjugation symmetries, so the standard harmonic-well construction restricts without change to the required sector. This is also a direct special case of the nondegenerate-well spectral equivalence and quantum Birkhoff normal-form results of Laurent Charles and San Vũ Ngọc, [*Spectral asymptotics via the semiclassical Birkhoff normal form*](https://arxiv.org/abs/math/0605096), especially their comparison and normal-form theorems.

### 6. Application to the two $SU(3)$ class levels

Let

$$\delta(z) = \prod_{i < j}^{}\left( \theta_{i}(z) - \theta_{j}(z) \right)$$

be the linear Weyl discriminant. Multiplication by $\delta$ identifies the invariant polynomial model with the Weyl-anti-invariant oscillator model. The flat oscillator states have the form

$$\phi_{a}(z) = \delta(z)\psi_{a}(z)e^{- p_{2}(z)/2},$$

and their flat inner product is exactly the project inner product

$$\langle f,g\rangle_{W} = \int_{\mathbb{R}^{2}}^{}f(z)g(z)\delta(z)^{2}e^{- p_{2}(z)}\, dz.$$

The first two charge-conjugation-even invariant factors are

$$\psi_{0} = \text{constant},\quad\quad\psi_{1} \propto p_{2} - 4.$$

They are the unique invariant states at relative shell degrees $0$ and $2$, so both model levels are simple in the required symmetry sector. Since

$$H_{0} = \frac{1}{2\sqrt{6}}\left( - \Delta + p_{2} \right),$$

their leading energy difference is

$$\mu_{1}^{(0)} - \mu_{0}^{(0)} = \frac{2}{\sqrt{6}} = \sqrt{\frac{2}{3}}.$$

For the quartic term, the exact matrix elements give

$$\mu_{1}^{(1)} - \mu_{0}^{(1)} = - \frac{25}{48} + \frac{5}{24} = - \frac{5}{16}.$$

The direct sextic contribution is

$$\Delta_{H_{2}} = \frac{19\sqrt{6}}{576},$$

using

$$\langle p_{2}^{3}\rangle_{\psi_{0}} = 120,\quad\quad\langle p_{3}^{2}\rangle_{\psi_{0}} = 5,$$

$$\langle p_{2}^{3}\rangle_{\psi_{1}} = 480,\quad\quad\langle p_{3}^{2}\rangle_{\psi_{1}} = 20.$$

The exact reduced-resolvent contribution from $H_{1}$ is

$$\Delta_{res} = - \frac{205\sqrt{6}}{3072}.$$

Therefore

$$\mu_{1}^{(2)} - \mu_{0}^{(2)} = \frac{19\sqrt{6}}{576} - \frac{205\sqrt{6}}{3072} = - \frac{311\sqrt{6}}{9216}.$$

Applying the lemma to $a = 0,1$ yields

$$p_{1}(h) - p_{0}(h) = h\sqrt{\frac{2}{3}} - h^{2}\frac{5}{16} - h^{3}\frac{311\sqrt{6}}{9216} + O\left( h^{4} \right).$$

Since

$$p_{a}(h)=h^{2}E_{a}^{+}(\beta),\qquad h=\beta^{-1/2},$$

division by $h^{2}$ gives

$$\Delta_{SU(3)}(\beta) = \sqrt{\frac{2\beta}{3}} - \frac{5}{16} - \frac{311\sqrt{6}}{9216}\beta^{- 1/2} + O\left( \beta^{- 1} \right).$$

This proves the result in Section 1.

### 7. What has and has not been closed

The missing local analytic step is closed because:

1.  Weyl conjugation is exact and leaves a flat kinetic operator plus a scalar.
2.  The compact Wilson potential has a unique nondegenerate minimum.
3.  The $h = \beta^{- 1/2}$ rescaling produces the exact $H_{0},H_{1},H_{2}$ used by the coefficient calculation.
4.  The two model levels are simple after the correct symmetry restriction.
5.  A symmetry-preserving quasimode has residual $O\left( h^{4} \right)$ for $P_{h}$, which becomes $O\left( \beta^{- 1} \right)$ for the original gap.

No explicit numerical value for $C$ or $\beta_{0}$ is asserted. Obtaining effective constants would require a quantitative Agmon/IMS implementation, but is not necessary for the asymptotic theorem.

The proof does not repair or revive the projected-capacity program. That global program remains separate and archived under the audit’s no-go conclusion for the top-norm observable.

## Appendix B. Exact $SU(4)$ exceptional-rank completion

The following theorem is reproduced from `SU4_HYBRID_COMPLETE_THEOREM_V2 (2).md`. Its companion JSON certificate records the 4,171-word regression, 35,130 balanced fusion paths, 156 exceptional charge-conjugation orbits, exact local Gram reconstruction, 78 rank-one joint-channel factorizations, and the all-zone zero residual.

### SU(4) fourth-order exceptional-rank completion

**Status:** PASS  
**Version:** `2026-06-14-su4-hybrid-complete-v2`

#### Complete exceptional corpus

The exact SU(4) N-ality scan introduces no new ordered words. The exceptional
sector is contained in 76 of the existing 4,171 ordered words and consists of

- 312 exceptional sign assignments;
- 156 charge-conjugation orbits;
- 96 distinct exceptional trace topologies;
- 1,806 exact local-channel choices, of which 214 contract nontrivially.

The finite-rank local algebra contains 42 oriented exceptional signatures and
78 exact rank-one joint Casimir channels. The allowed final Haar families are

\[
(4,0),\quad(0,4),\quad(5,1),\quad(1,5).
\]

Determinant singlet channels occur in the resolvent only at the third
des-Cloizeaux cut.

#### Exact correction on the flat branch

The exceptional correction has 13 root-kernel entries and 39 cubic-completed
real-space entries. It is **not** a scalar multiple of the identity on the
complete three-component one-flux space.

Let

\[
\psi(k)=
\begin{pmatrix}
e^{ik_2}-1\\
-(e^{ik_1}-1)\\
e^{ik_0}-1
\end{pmatrix}.
\]

The exact Laurent-polynomial identity is

\[
\boxed{
H^{\mathrm{exc}}_{4,4}(k)\,\psi(k)
=
-\frac{304746539168}{160249753125}\,\psi(k)
}
\]

throughout the Brillouin zone. Hence the exceptional sector shifts the exact
flat branch by the momentum-independent amount

\[
\boxed{
\Delta q_4=-\frac{304746539168}{160249753125}
}
\]

while

\[
\boxed{\Delta A_4=\Delta B_4=0}.
\]

#### Complete SU(4) coefficients

\[
\boxed{
q_4=
-\frac{162485785670299274695454289332603}
{121294607143027203361265133093750}
}
\]

\[
\boxed{A_4=\frac{32}{675}}
\]

\[
\boxed{
B_4=
\frac{3601925923737103752887}
{70481696720359496343750}
}
\]

and therefore

\[
\boxed{
\Delta c_{4,4}=A_4+B_4
=
\frac{2314426811641505637629}
{23493898906786498781250}
>0.
}
\]

The parity-point values obey

\[
c_X=q_4+A_4,\qquad
c_M=q_4+A_4+\frac12B_4,\qquad
c_R=q_4+A_4+B_4,
\]

and exactly

\[
\boxed{c_R-2c_M+c_X=0}.
\]

#### Full dispersion theorem

For \(k\ne\Gamma\), with \(X_i=1-\cos k_i\),

\[
\boxed{
c_{4,4}(k)=q_4+
\frac{
A_4\sum_iX_i^2+
B_4\sum_{i<j}X_iX_j
}{2\sum_iX_i}
}
\]

with continuous extension \(c_{4,4}(\Gamma)=q_4\).

Because \(A_4>0\) and \(B_4>0\),

\[
\boxed{\Gamma\text{ is the unique global minimum}},
\qquad
\boxed{R\text{ is the unique global maximum}}.
\]

Thus the SU(4) fourth-order one-flux \(T_1^{+-}\) band is strictly
dispersive.

#### Verification chain

- canonical symbolic source SHA-256:
  `8feec874aa16c823bb837efa8df626d5cf735db5ecaa6c90b8806ddf456b51a5`;
- exact balanced rerun: 3,850 trace topologies and 35,130 fusion paths;
- stable 4,171-word corpus reproduced;
- complete exceptional scan: 76 words and 156 C-orbits;
- all explicit epsilon/delta-epsilon Gram matrices verified;
- all 78 joint channel projectors factorized and normalized exactly;
- exact all-zone Laurent-polynomial residual:
  `(0,0,0)`;
- corrected kernel support: 63 root entries and 189 real-space entries.

#### Correction to the preliminary interpretation

The preliminary statement
`Delta H_4,4(k)=Delta q_4 I_3` was too strong. The certified statement is the
flat-branch eigenvalue identity

\[
H^{\mathrm{exc}}_{4,4}(k)\psi(k)=\Delta q_4\psi(k).
\]

This distinction does not change \(q_4\), \(A_4\), \(B_4\), the bandwidth,
or the global extrema.

## Appendix C. Notation and coefficient conversion registry

To prevent the documentary collision that caused earlier status errors, use:

- $q_N$: momentum-independent fourth-order branch shift;
- $(\alpha_N^{\mathrm{pen}},\beta_N^{\mathrm{pen}})$: coefficients in the older two-invariant numerator pencil;
- $(A_N^{\mathrm{shp}},B_N^{\mathrm{shp}},C_N^{\mathrm{shp}},D_N^{\mathrm{shp}})$: coefficients in the generic four-shape basis.

The exact conversion is
\[
A_N^{\mathrm{shp}}=\frac{\alpha_N^{\mathrm{pen}}}4,
\qquad
B_N^{\mathrm{shp}}=0,
\qquad
C_N^{\mathrm{shp}}=\frac{\beta_N^{\mathrm{pen}}-2\alpha_N^{\mathrm{pen}}}{16},
\qquad
D_N^{\mathrm{shp}}=0
\]
for every currently solved physical rank.

| Rank | $q_N$ | $\alpha_N^{\mathrm{pen}}$ | $\beta_N^{\mathrm{pen}}$ | Four-shape status |
|---|---|---|---|---|
| $SU(3)$ | exact rational | $5/12$ | exact rational; stable expression plus $-25/64$ anomaly | exact; $B_3^{\mathrm{shp}}=D_3^{\mathrm{shp}}=0$ |
| $SU(4)$ | exact rational, including determinant shift | $32/675$ | exact rational; equals stable expression | exact; $B_4^{\mathrm{shp}}=D_4^{\mathrm{shp}}=0$ |
| $SU(5)$ | finite-rank certificate; no determinant correction | $1/108$ | certified to equal stable expression | exact Layer-II rank closure; $B_5^{\mathrm{shp}}=D_5^{\mathrm{shp}}=0$ |
| $SU(6)$ | finite-rank certificate with $\Delta q_6=6/343$ | $64/25725$ | certified to equal stable expression | exact Layer-II rank closure; $B_6^{\mathrm{shp}}=D_6^{\mathrm{shp}}=0$ |
| $SU(N\ge7)$ | exact symbolic stable-rank family | $640/[N(N^2-1)^3]$ | $P_{402}(N)/D_{409}(N)$ | exact family; $B_N^{\mathrm{shp}}=D_N^{\mathrm{shp}}=0$ |

## Appendix D. Canonical source and status registry — v1.4

| Source | Role | Authority |
|---|---|---|
| `MASTER THEORY Gauge Constrained Spectral Geometry 2026-08-01.md` | five-layer narrative spine | synthesis, not sole status authority |
| `UPDATED_FOURTH_ORDER_HODGE_THEORY_2026-08-01.md` | Hodge self-duality, four-shape obstruction space, coefficient conversion | theorem package |
| `SU3_Compact_Remainder_Proof.docx` | rigorous $O(\beta^{-1})$ compact-gap remainder | analytic proof insertion |
| `verify su3 proof.py` | algebra/moment/final-assembly checks | partial executable verification |
| `SU4_HYBRID_COMPLETE_THEOREM_V2 (2).md` | exact $SU(4)$ exceptional completion | theorem statement |
| `CERT_SU4_hybrid_certificate_v2.json` | exact gates, coefficients, hashes, residuals | certificate |
| `CERT_SU4_exceptional_topology_word_ledger_v2.json` | 96 topology records and 76 word corrections | detailed ledger |
| `PAPER homological flat bands.md` (2026-08-08) | Layer-II rank synthesis: universal axial law, $SU(5)$/$SU(6)$ closure, exceptional-rank partition, $SU(3)$ second-pencil anomaly | rank/status authority relative to accepted certificates |
| `Pasted markdown.md` (2026-08-08 independent SIMULATIONS audit) | independent re-derivation and proof-chain audit of the $SU(3)$ strong-coupling simulation corpus | proof-status authority for $SU(3)$ $O(y^4)$ certificate completeness |

### v1.4 status correction

The older statement that $SU(5)$ and $SU(6)$ are unresolved is superseded by the 2026-08-08 Layer-II authority. The universal axial coefficient is exact for every integer $N\ge3$. The generic four-shape ambient space remains four-dimensional, while the physical contraction satisfies $B_N^{\mathrm{shp}}=D_N^{\mathrm{shp}}=0$ across the resolved rank partition. The special $SU(3)$ correction $\Delta\beta_3^{\mathrm{pen}}=-25/64$ prevents a universal quotient-scalarity claim; such a claim may only be considered for $N\ge4$.

