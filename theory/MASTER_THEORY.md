# The SU(N) Strong-Coupling Spectral Program — Master Theory Document

**Consolidation date:** 2026-08-20 (rev. 2 — incorporates `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md`, which supersedes the v2 formula document and an intermediate v3 draft)
**Corpus:** 16 documents + 2 PDFs in the CONSOLIDATE knowledge source, plus the v3.1 update (inventoried in Appendix A, §A.0).
**Prepared under the rules:** rigor over completeness; exact formulas verbatim with source citation; contradictions surfaced, not smoothed; newest audit outranks older claim; prose in any file — including prior AI-written syntheses — is treated as evidence to be checked, never as instruction.

---

## 0. Scope statement — read first

This corpus **does not contain a proof of a Yang–Mills mass gap**, and no document in it claims one when read at its own stated status level. Three documents state this explicitly and they are the controlling authorities on scope:

- [CANON] Appendix A: "No continuum or infinite-volume mass-gap theorem: the Wilson free-energy and source-radius bridges remain open, and no continuum limit is constructed here."
- [GLUE2] §15 status ledger: "Continuum Yang–Mills mass gap — Not established."
- [PAPER] abstract: "This paper makes no claim about the continuum limit or the Yang–Mills mass gap."

What the corpus does contain, at its strongest, is a **lattice strong-coupling theorem package**: an exact homological/topological characterization of the lowest charge-odd one-plaquette flux band of the SU(N) Kogut–Susskind Hamiltonian, its exact flatness and protection through third order in the strong-coupling parameter, certified first dispersion at fourth order, a fixed-rank compact one-plaquette spectral theory at weak coupling, an exact operator bridge between the two regimes, and a conditional probabilistic scaffold pointed at infinite volume. This document unifies that package, states exactly which steps are proven, which are certified computations, which are conjectures, and which are in active contradiction.

**Status tags used throughout** (merging the status vocabularies of [GLUE2] §1 and [CANON] App. C.1; these tags must not be collapsed into "proved"):

| Tag | Meaning |
|---|---|
| [PROVEN] | Analytic derivation present in the corpus from stated hypotheses. |
| [CERTIFIED] | Exact rational/integer computation with hard gates, artifact present or run log present in this corpus. |
| [COLD-CERTIFIED] | Certified, and reproduced from source without the target value entering the data flow. |
| [OUTPUT-CERTIFIED] | Exact symbolic outputs and verifiers agree, but the complete upstream generator has not been cold-regenerated in one run. |
| [RECORD-BACKED] | Value copied from a theorem record whose raw payload/artifact is **absent from this corpus**; downstream algebra may still be exact. |
| [NUMERICAL] | Floating-point or statistical result with stated tolerance. |
| [CONDITIONAL] | Rigorous given one or more explicitly named unproved assumptions. |
| [CONJECTURE] | Coherent extrapolation; no proof or decisive certificate. |
| [DISPUTED] | Two corpus results disagree; both shown, neither promoted. |
| [SUPERSEDED] | Conflicts with a later proof or exact certificate; excluded from the canonical theory. |
| [FALSIFIED] | Disproved by an exact certificate in this corpus. |

**Source file tags:**

| Tag | File | Date |
|---|---|---|
| [T1PM] | `FOURTH_ORDER_T1PM_BAND_THEOREM_V0_8_CONSOLIDATED.md` | 2026-06-14 |
| [PAPER] | `files/febf4293-0deb-4169-9cbf-4a2e69293ecd.pdf` ("Topological protection of a dispersionless T1+− glueball band") | 2026-07-25 |
| [CANON] | `Canonical_SU_N_Wilson_Spectral_Theory_Derivation_First_Corrected.md` | 2026-08-01 |
| [GCSG] | `files/e03f1455-a81d-44f7-976a-5de9905bca46.pdf` ("Gauge-Constrained Spectral Geometry", master v1.4) | 2026-08-08 |
| [MOB] | `Hodge_Cellular_Circuit_Mobility_Theorem.md` | 2026-08-19 |
| [RUN15] | `15 hour RUN.txt` + `15 hour RUN. results.txt` (v10a.26 A100 run log/results) | 2026-08 (≈19th) |
| [V10A26] | `Hodge_v10a26_Factor52Complete_ExactSW_RootedOracle_A100.md` (notebook source of [RUN15]) | 2026-08 |
| [MCE] | `Hodge_SU3_Exact_MarkedCluster_m4_Colab.py` (target-blind exact marked-cluster engine) | 2026-08 |
| [GLUE2] | `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v2.md` — **superseded by [GLUE3]**; cited only where content is unchanged | 2026-08-20 |
| [GLUE3] | `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md` — current formula/status authority (supersedes v1, v2, and the intermediate v3 draft) | 2026-08-20 |
| [STRONG] | `STRONGEST_FORMULA_RESOLVED_CELLULAR_MOBILITY_2026-08-20.md` | 2026-08-20 |
| [FINAL] | `#-Final-unified-theory.txt` (prior AI synthesis note) | 2026-08-20 |
| [PENT] | `pentagonal_o4_minimal_representation_frontier.py` + `_results.{txt,json}` | 2026-08 |
| [AUD] | `audit_stranded_flux_zero_backend.py` + `_results.{txt,json}` | 2026-08 |

**Precedence rule** (adopted from [GCSG] §1.3 and [STRONG] header, and applied throughout): exact self-contained derivation > independent direct computation > internally consistent saved output > later consistent version > stale diagnostics; a filename saying "FINAL" never overrides a failed invariant check; newest audit records outrank older claims. Chronologically: [T1PM] < [PAPER] < [CANON] < [GCSG] < [MOB] < [RUN15] < [GLUE2]/[STRONG]/[FINAL] < [GLUE3]. Where [GLUE3] tightens or corrects [GLUE2], [GLUE3] controls; the changes are listed in §5.6.

**Caveat on [FINAL] and [STRONG]:** both are AI-written synthesis notes containing first-person claims of reruns ("I reran…", "I fitted…") whose artifacts are **not** in this corpus. Per the consolidation rules, every claim unique to them is classified [RECORD-BACKED] at best, regardless of the confidence of their prose. Their arithmetic, where checkable, has been re-verified (see §7.6).

**Consolidation verification note.** During this consolidation the following were re-verified by exact rational arithmetic (independent of any corpus code): the third-order ledger identity d₃ = 7/32 + 12ℓ₃ − 4b₃; all fourth-order band-edge/curvature identities of §5.4; B₃^full = B₃^bal − 25/64; the P₁₇/R₂₀ ↔ SU(4) certificate match and its N→∞ leading coefficient 6170/9; the fifth-order anchor gates c_R = 2c_M − c_X, A₅ = c_X − q₅, B₅ = c_R − c_X; the pentagonal O(5) sum 35/384 + δc₅; the internal ratios of the pentagonal O(4) constants; t_N values and deficit identity; α_N exceptional values; the SU(4) conversion C₄ = (β₄−2α₄)/16; and the full mass/tension ratio series c₀…c₅ by direct series division of the stated m(u) and σ(u). Rev. 2 additionally re-verified the [GLUE3] items: the large-$N$ expansion of $t_N$ (through $N^{-7}$, next term $-\tfrac{1021}{256}N^{-9}$), the 25-point stencil weights $w_0,w_1,w_2,w_d$ and their zero-mode gate, the historical $w_0=\frac{189690244462349}{91777300430400}$, the limit $\beta_N/\alpha_N\to\frac{617}{576}$, the high-symmetry anchors $\lambda_X=\alpha$, $\lambda_M=\alpha+\beta/2$, $\lambda_R=\alpha+\beta$, and the criterion that a genuine $\Gamma$ Hessian requires $\beta=2\alpha$ (historical kernel: $0.0640\neq0.8333$). All pass. These checks establish *internal consistency*, not the physical correctness of the inputs.

---

## 1. Notation registry — one convention, defined once

The corpus uses at least three conflicting convention families. This section fixes the canonical set and gives the translation table. **Every formula in this document is in canonical notation unless explicitly tagged otherwise.**

### 1.1 Coupling (the most dangerous conflict in the corpus)

Canonical strong-coupling variable ([T1PM] §1, [GLUE2] §2.1, [GCSG] §1.3 — all agree):

$$\boxed{\,u=\frac{\beta_H}{6}=\frac{1}{g_H^4},\qquad \beta_H=\frac{6}{g_H^4}\,}$$

with Kogut–Susskind Hamiltonian (canonical form, [T1PM] §1)

$$H_\beta=\tfrac12\sum_\ell C_2(\ell)+\beta\sum_p\Bigl(1-\tfrac1N\,\mathrm{Re\,Tr}\,U_p\Bigr),$$

so the perturbation is $-u(\chi_p+\bar\chi_p)$ per plaquette and $H_{\rm eff}(u)=\sum_r u^r H_r$.

**Translation table:**

| Symbol in source | Definition | Relation to $u$ | Where used | Status |
|---|---|---|---|---|
| $u$ | $\beta_H/6$ | $=u$ | [T1PM], [GLUE2], [STRONG], canonical ledgers | **canonical** |
| $y$ (paper) | coupling of $-y\sum_p(\chi_p+\bar\chi_p)$ | $y=u$ | [PAPER] eq. (1) and all its constants | equal; relabel only |
| $Y$ (v0.7/v0.8 draft) | printed as $2\beta_H/3=4u$ | **label erratum, not a rescaling**: the normalization audit found the contractions and printed coefficients were *already* coefficients of $u$; v0.8a/v1.1 corrected the label without rescaling. Do **not** divide old fourth-order numbers by $4^4$ or multiply lower orders by powers of 4 | [GLUE3] §2.2 (controls); [T1PM] §1 note, [STRONG], [GLUE2] §2.2 phrased it as a convention to convert — [GLUE3]'s erratum reading supersedes | [SUPERSEDED label]; safe rule: match the Hamiltonian prefactor before converting any legacy symbol |
| $x$ (Hamer bridge) | Hamer's variable | $x=2u$, $H_{\rm proj}=\tfrac12 W$, $m_r=2^{r-1}a_r$ | [GLUE2] §2.3, [GLUE3] §2.3 | linear bridge, exact; **but** the decimal $a_4=-0.0968932328773$ is a notebook transcription not yet checked against a hashed primary Hamer table ([GLUE3] §2.3) — local cross-check, not primary-source verification |
| $\beta_{\rm loc}$ | compact one-plaquette weak-well coupling | separate regime; never identified with $\beta_H$ silently | [GLUE2] §2.4, [CANON] | regime firewall |
| $\tau$ | $\beta/N^3$ | rank-balanced weak-well scaling | [CANON] §8.3 | formal only |

[GCSG] v1.4 adds one honest qualification: the claim that the 2026-08-08 *simulation-tower* coefficients can be relabeled $y\to u$ with no rescaling is **conditional** until a convention-dependent magnetic prefactor excluded in its stages 3F/3H is proved closed ([GCSG] §1.3, item 5 of the v1.4 change log). Agreement with the canonical $u$-ledger is strong consistency evidence, not a proved bridge. ([GLUE3] §2.2 resolves the *archived-source* side of this — the $Y$ line was a definition/label error — but the GCSG simulation-tower prefactor gate is a separate item and stays open.)

Symbol hygiene added by [GLUE3]: it writes $\beta_{\rm lat}$ for what this document (following [T1PM]/[GLUE2]) calls $\beta_H$ — same object; and it renames the third-order bookkeeping entry $\ell_3\to\operatorname{leak}_3$ to avoid collision with an older all-rank symbol $\ell_N$. This document keeps $\ell_3$ (§4.4) with that alias noted.

### 1.2 Lattice, chain complex, Bloch data

Spatial complex: $T_L^3=(\mathbb Z/L)^3$ (also $T^2\times I$, $T^1\times I^2$, $I^3$ in [PAPER]); oriented cells with boundary maps

$$C_3\xrightarrow{\;\partial_3\;}C_2\xrightarrow{\;\partial_2\;}C_1,\qquad \partial_2\partial_3=0 .$$

$D_k$ = matrix of $\partial_k$; Laplacians $L_2^{\downarrow}=D_2^{T}D_2$, $L_2^{\uparrow}=D_3D_3^{T}$; Betti numbers $b_i$; $Z_2=\ker\partial_2$; $\mathcal H_2=\ker\partial_2\cap\ker\partial_3^{T}$.

Bloch data (one-flux sector; plaquette orbitals $a=(12),b=(13),c=(23)$):

$$u_j=1-e^{ik_j},\quad v_j=1+e^{ik_j},\quad
\widetilde N(k)=\begin{pmatrix}u_2&-u_1&0\\ u_3&0&-u_1\\ 0&u_3&-u_2\end{pmatrix},\quad
N(k)=\begin{pmatrix}v_2&v_1&0\\ v_3&0&v_1\\ 0&v_3&v_2\end{pmatrix}$$

([PAPER] eq. (4); [GLUE2] §3 writes the same object as $B(k)$ with $d_j=e^{ik_j}-1$; identical up to the fixed orientation convention). In this document **$B(k):=\widetilde N(k)$**. Momentum scalars:

$$q(k)=\sum_{j=1}^3|u_j|^2=4\sum_j\sin^2\frac{k_j}{2}\,;\qquad
a_i=4\sin^2\frac{k_i}{2}=2X_i,\quad X_i=1-\cos k_i,$$
$$\mathsf S=\sum_iX_i,\quad \mathsf Q=\sum_iX_i^2,\quad \mathsf R=\sum_{i<j}X_iX_j,\qquad
e_2=\sum_{i<j}a_ia_j=4\mathsf R,\quad e_3=a_1a_2a_3,\quad \Sigma_a=2\mathsf S .$$

Cube-boundary flat vector: $w(k)^\dagger=(u_3,\,-u_2,\,u_1)$, $\;w^\dagger w=q=2\mathsf S$ ([PAPER] Thm 4.1; [GLUE2] §3 uses conjugated $d_j$; same object).

### 1.3 Fourth-order coefficient coordinates (second-worst conflict)

Two coordinate systems coexist; both are needed because the sources certify in both.

**Two-invariant "pencil" form** ([T1PM] §4, symbols $q_N,A_N,B_N$; [GCSG] calls them $q_N,\alpha^{\rm pen}_N,\beta^{\rm pen}_N$ — adopted here to avoid the clash below):

$$c_{4,N}(k)=q_N+\frac{\alpha^{\rm pen}_N\,\mathsf Q+\beta^{\rm pen}_N\,\mathsf R}{2\mathsf S},\qquad k\neq\Gamma .$$

**Four-shape form** ([CANON] §12, [GCSG] §4.5; the generic cubic-invariant space is four-dimensional):

$$\varepsilon_4(k)=c_0+A^{\rm shp}\Sigma_a+B^{\rm shp}e_2+C^{\rm shp}\frac{4e_2}{\Sigma_a}+D^{\rm shp}\frac{e_3}{\Sigma_a}.$$

**Exact conversion** ([CANON] §13.1, [GCSG] App. C; re-verified here):

$$A^{\rm shp}_N=\frac{\alpha^{\rm pen}_N}{4},\qquad B^{\rm shp}_N=0,\qquad C^{\rm shp}_N=\frac{\beta^{\rm pen}_N-2\alpha^{\rm pen}_N}{16},\qquad D^{\rm shp}_N=0$$

for every solved physical rank (the vanishing of $B^{\rm shp},D^{\rm shp}$ is a *dynamical* result, §5.3, not an identity).

**Symbol-collision warnings** (all explicit in the sources; repeated here because a hostile referee will find them):

1. [T1PM] uses $A_N,B_N$ with subscript = gauge rank in §§1–8 but subscript = coupling order in §9 ($A_5,B_5$ are *fifth-order SU(3)* numbers). $q_5$ denotes **two different quantities** in [T1PM]: the SU(5) fourth-order rest energy (§5.5) and the SU(3) fifth-order rest mass (§9). This document always disambiguates in words.
2. $\alpha_N$ = fourth-order axial pencil coefficient here; but $\alpha_N=(N^2-3)/2$ is also the Weyl-Gaussian radial Laguerre parameter in [CANON]/[GCSG] Layer I. Context (spatial vs compact) disambiguates; this document writes $\alpha^{\rm pen}_N$ vs $\alpha^{\rm Lag}_N$ where both occur.
3. $A_N,B_N$ additionally denote the two second-order shared-link channel sums in [GLUE2]/[CANON] §10.2. This document calls those $\mathcal A_N,\mathcal B_N$.
4. The real-space SOS coefficients of [GLUE2] §7/§12 are $(\alpha,\beta)=(\alpha^{\rm pen},\beta^{\rm pen})$; the historical SU(3) instance is written $\alpha_{\rm old}=5/12$, $\beta_{\rm old}=17607806155349/275331901291200$.

### 1.4 Compact (weak-well) regime notation — Layer I

$U\sim\mathrm{diag}(e^{i\theta_1},\dots,e^{i\theta_N})$, $\sum\theta_j=0$; power sums $P_k=\sum_j\theta_j^k$; charge conjugation $C\!:\theta\mapsto-\theta$, so $CP_k=(-1)^kP_k$. SU(3) Cartan coordinates ($\theta_1=\frac{x}{\sqrt2}+\frac{y}{\sqrt6}$, $\theta_2=-\frac{x}{\sqrt2}+\frac{y}{\sqrt6}$, $\theta_3=-\frac{2y}{\sqrt6}$): $p_2=P_2=x^2+y^2$, $p_3=P_3=\frac{\sqrt6}{6}\,y(3x^2-y^2)$ (decoded from [CANON] §3.1 and re-derived symbolically during consolidation). Weyl-Gaussian inner product $\langle f,g\rangle_W=\int fg\,\Delta_W^2e^{-p_2}$; radial Laguerre parameter $\alpha^{\rm Lag}_N=(N^2-3)/2$; Gamma shape $A_N=\alpha^{\rm Lag}_N+1=(N^2-1)/2$. Operator stack after exact rescaling ($h=\beta^{-1/2}$, well scaling $a=(3/2)^{1/4}$ for SU(3)):

$$H_0=\tfrac{1}{2\sqrt6}(-\Delta_z+p_2),\qquad H_1=-\frac{p_2^2}{96},\qquad H_2=\sqrt6\Bigl(\frac{p_2^3}{11520}+\frac{p_3^2}{8640}\Bigr)$$

([GCSG] App. A, clean typeset; [CANON] §2 contains the same content with a corrected dilation $\varepsilon^4=N/(2\beta)$ — the earlier $2N/\beta$ is [SUPERSEDED], [CANON] §2.2).

**Encoding warning.** [CANON] is a lossy text export: radicals and fraction bars are stripped (e.g. its "$-31169216\beta^{-1/2}$" is $-\tfrac{311\sqrt6}{9216}\beta^{-1/2}$, confirmed against [GCSG] and the numerical fit $-0.0826591$). Where [CANON] and [GCSG] print the same result, this document cites [GCSG] for the typeset form and [CANON] for the derivation. Formulas recoverable only from [CANON] are marked "(decoded)" when the reconstruction was verified numerically, and flagged as garbled when it was not.

---

## 2. Phase-2 result: the spine

### 2.1 The strongest logical chain

The single strongest chain in the corpus runs from the Kogut–Susskind Hamiltonian to a **proved, topologically protected, exactly flat lattice band with a positive strong-coupling gap, and its certified first dispersion**. Every link is stated with its tag:

1. **KS Hamiltonian and one-flux C-odd sector** (definitions; [PAPER] §2, [T1PM] §1). At $u=0$ the one-plaquette flux states are degenerate at electric energy $8/3$ (SU(3)); charge conjugation splits the manifold; SU(2) has no C-odd sector at all ([T1PM] §2 — [PROVEN]).
2. **Incidence factorization** $S(k)+4I=B(k)B(k)^\dagger$ ([PAPER] Lemma 3.1 — [PROVEN]; hand-checkable).
3. **Exact flatness** of the lowest C-odd branch: $\det B\equiv0$, $S(k)w(k)=-4\,w(k)$; the flat band is the Bloch shadow of $\partial_2\partial_3=0$ ([PAPER] Thm 4.1 — [PROVEN]).
4. **Homological identification and Betti count**: flat band $=Z_2=\ker\partial_2$; $\dim=\#\{\text{cubes}\}+b_2-b_3$; $L^3+2$ on $T^3$; verified over four topologies ([PAPER] Thm 5.1 — [PROVEN]+[CERTIFIED]).
5. **Protection theorems**: link-channel rigidity (any $H=\alpha I+\beta S+BMB^\dagger$ leaves the band flat) and all-orders scalar action of the boundary-operator algebra on $\mathcal H_2$, with $L_2^{\downarrow}L_2^{\uparrow}=L_2^{\uparrow}L_2^{\downarrow}=0$ ([PAPER] Thms 6.2, 6.3 — [PROVEN]; scope caveat: protection is against corrections *inside the boundary algebra*, [GLUE2] §6.2).
6. **Second-order dynamics**: all-rank hopping $t_N=\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)}>0$ for $N\ge3$, rank-cubic suppression $N^3t_N\nearrow 1/4$ ([CANON] §10.2, [GCSG] §4.1 — [PROVEN]); SU(3) ledger $d_+=223/1020$, $t_+=-11/306$, $d_-=7/102$, $t_-=5/612$ ([PAPER] eq. (7) — [CERTIFIED]).
7. **SU(3) flatness through third order**: $H_{\mathrm{eff},-}(k,u)=E_{\rm flat}(u)I+t(u)B(k)B(k)^\dagger+O(u^4)$ with exact $E_{\rm flat},t$ (§4.4 below; [GLUE2] §5 — [COLD-CERTIFIED]; the flat value is $k$-independent because $B^\dagger w=0$).
8. **Fourth-order first dispersion**: the axial data $A^{\rm shp}_3=5/48$, $B^{\rm shp}_3=D^{\rm shp}_3=0$, $\alpha^{\rm pen}_3=5/12$ are sealed by *both* competing computations ([RUN15] gates 61–64; [GLUE2] §10 — [CERTIFIED]); the diagonal coefficient and the rest scalar are [DISPUTED] (§5.5); the all-rank axial law $\alpha^{\rm pen}_N=640/[N(N^2-1)^3]$ is [OUTPUT-CERTIFIED] ([T1PM] §4, [GCSG] §4.7).
9. **The gap statement itself** (§4.6): in the strong-coupling regime the one-flux C-odd $T_1^{+-}$ branch sits at $m_-(u)=\tfrac83+u+\tfrac{11}{306}u^2-\tfrac{109151}{249696}u^3+O(u^4)$, isolated, momentum-independent through $O(u^3)$ — a positive lattice gap above the vacuum in this sector at small $u$ [COLD-CERTIFIED within its truncation], with $b_2$-fold topological pinning against boundary-algebra corrections [PROVEN].
10. **Bridge toward physics** (supporting, not spine-closing): the gauge-invariant source $B_i^-=\mathrm{Im\,Tr}\,U_{jk}$, its cubic locking to $-P_3/6$ at SU(3)/SU(4), and the local nonzero-overlap theorem ([CANON] §9 — [PROVEN], local only); Monte Carlo finds the *physical* $T_1^{+-}$ state is extended (raw one-plaquette overlap $0.0072\pm0.0165$, smeared $\approx0.80$) ([GCSG] §8 — [NUMERICAL]).

### 2.2 Document classification

**Spine documents** (the chain above lives here): [PAPER] (steps 2–6, cleanest form), [GLUE2] (steps 7–9; current status authority for fourth order), [T1PM] (step 8 all-rank structure; fifth order), [RUN15] (the evidence run for steps 7–8), [CANON] (step 6 derivation, step 10, and the corpus's most careful status ledger).

**Supporting**: [GCSG] (five-layer synthesis; Layer I compact theory, seam/EP atlas, transfer norms, capacity calculus; its v1.4 audit statuses are adopted), [MOB] (cellular-circuit lower bound and prism/cube/tetrahedron geometry), [STRONG] (final status audit; its "resolved cellular mobility equation" is the corpus's best unified principle, tagged by its own author as "not yet a separately certified theorem"), [V10A26]/[MCE] (engines; define what [RUN15] computed and what a future adjudication run must do).

**Exploratory**: [PENT], [AUD] (pentagonal O(4) frontier: raw Gram/Haar closed, resolvents not built), [FINAL] (synthesis; unique claims record-backed), hyperhoneycomb prediction ([FINAL] §11), sixth-order $m_6$ program ([T1PM] §9.5), Bergman transfer and limitation program ([GCSG] Layers IV–V).

**Dead ends / rejected within the corpus** (kept for the record, excluded from the theory): the stranded-flux "zero backend" ([AUD] — [FALSIFIED], 8/8 gates); the global fixed-window projected-capacity firewall ([CANON] §16.3 — [FALSIFIED] by the Bernoulli no-go); the promotion $r_{\rm physical}=w_{\min}-2$ ([FINAL] §4 — [FALSIFIED] by the pentagonal cap hop, itself [RECORD-BACKED]); old Riccati/global-convexity claims ([STRONG] "Not supported"); numerical Peierls runs as evidence of a volume-uniform gap ([STRONG]); the Schur/Haar-Hessian "Theorem B", the 4D SU(2) θ/TRG thread, and the q-Racah novelty claim ([GCSG] App. 0 — quarantined); the Gemini draft ([CANON] App. C.2: "not an authority"); the $Y=2\beta/3$ coupling convention ([SUPERSEDED]).

### 2.3 The load-bearing unproven step

Stated at two levels, because the corpus's chain genuinely has two necks:

**(a) Within the lattice program (coefficient level).** Everything at fourth order and beyond hinges on **the physical identity of the fourth-order effective kernel** — equivalently, on which of the two scalar/shape pairs in §5.5 is the linked, correctly folded, correctly normalized $O(u^4)$ operator. The historical 189-record kernel and the new v10a.26 folded kernel agree on every protected invariant ($A^{\rm shp}=5/48$, $B^{\rm shp}=D^{\rm shp}=0$, $\alpha^{\rm pen}=5/12$) and disagree on the rest scalar and the off-axis coefficient $C^{\rm shp}$. The corpus's own final verdict is "MIXED/THIRD RESULT — DO NOT PROMOTE EITHER FOURTH-ORDER CLAIM" ([RUN15]). Until the target-blind marked-cluster engine [MCE] issues its seal, the fourth-order rest mass, bandwidth, $m/\sqrt\sigma$ ratio at $O(u^4)$–$O(u^5)$, and the [T1PM] "rank-complete theorem" as a *physical* statement are all conditional on this one adjudication.

**(b) For anything deserving the words "mass gap."** The one assumption everything hinges on is the **spectral bridge**: that the isolated one-plaquette $T_1^{+-}$ branch (a cutoff-scale, one-excitation-truncation object) has stable, volume-uniform overlap with the lightest state of the many-plaquette transfer matrix, and that this survives toward the continuum. No document proves any part of this; [CANON] App. B.19.4 states it as the open physical question, and the corpus's own Monte Carlo shows the raw one-plaquette operator carries $<4\%$ (2σ) of the physical state ([GCSG] §8) — the bridge, if it exists, runs through smearing/dressing, not through the bare operator. Behind it sit two further named open analytic inputs on the only infinite-volume route in the corpus: the inhomogeneous Wilson free-energy bound $Z_{\beta,\alpha,\Gamma,L}/Z_{\beta,L}\le K_\alpha^{|\Gamma|}$ (PC-2) and the source-radius reduction ([CANON] §16.5–16.8, [GCSG] Layer V). If one sentence is wanted: **the corpus proves protection and computes coefficients; it assumes, and nowhere proves, that the protected object is the glueball.**

---

## 3. Part I — Foundations (definitions)

**D1 (Hamiltonian).** $H_\beta=\tfrac12\sum_\ell C_2(\ell)+\beta\sum_p(1-\tfrac1N\mathrm{Re\,Tr}\,U_p)$ on the gauge-invariant Hilbert space over spatial $T^3_L$; canonical variable $u=\beta/6$; perturbation $-u(\chi_p+\bar\chi_p)$ per plaquette. [T1PM] §1, [PAPER] §2.

**D2 (one-flux C-odd sector).** The span of single-plaquette fundamental-flux states, split by $C:\chi\leftrightarrow\bar\chi$; unperturbed energy $2C_F\cdot(\#\text{links}/2)$; for a plaquette, $E_{F,N}=4\cdot\tfrac{C_F}{2}=2C_F=\tfrac{N^2-1}{N}$, $=8/3$ at $N=3$. [CANON] §10.1.

**D3 (chain complex and carriers).** As in §1.2. Flat carrier $Z_2=\ker\partial_2$ ("Gauss-law-satisfying subspace of the one-excitation manifold", [PAPER] §5); harmonic carrier $\mathcal H_2=\ker\partial_2\cap\ker\partial_3^T$, $\dim\mathcal H_2=b_2$.

**D4 (traceless compression / mobility order).** For a retained subspace $Z$ with projector $P_Z$:

$$\mathfrak M_Z(A)=P_ZAP_Z-\frac{\operatorname{tr}(P_ZAP_Z)}{\dim Z}\,P_Z,\qquad
r_{\rm mob}=\min\{r:\ \mathfrak M_Z(H^{(r)}_{\rm eff})\neq0\}.$$

[MOB] §1.1; generalized to arbitrary physical bands $P_E$ in [FINAL] §2 and [STRONG].

**D5 (temporal history and class amplitude).** A history $h=(f_1,\sigma_1;\dots;f_r,\sigma_r)$ of signed plaquette insertions with intermediate flux chain $q_j=q_0+\sum_{m\le j}\sigma_mB_2e_{f_m}$; its amplitude is the Haar/Gram-reduced, resolvent-weighted matrix element $\langle q_{\rm out}|VR_{r-1}V\cdots R_1V|q_{\rm in}\rangle$ with $R_j=\bar Q_j(E_0\bar G_j-\bar H_{0,j})^{-1}\bar Q_j$ on the Gram-quotiented physical space at each cut. [STRONG] (master-equation section), [FINAL] §1. The static projection $\pi(h)=\sum_j\sigma_je_{f_j}$ does **not** determine the amplitude: $A_N[h]\neq A_N[\pi(h)]$ in general ([FINAL] §4 — the pentagonal lesson, §6.3 below).

**D6 (status of D5).** The full "resolved cellular mobility equation" built on D4–D5,

$$r_{\rm mob}(N)=\min\Bigl\{r\ge1:\ \sum_{\mathcal C\in\mathscr C_r}\mathcal A^{(r)}_{N,\mathcal C}\,\mathfrak M_Z(T_{\mathcal C})\neq0\Bigr\},$$

is the corpus's unifying principle and is tagged by its own source as **a new synthesis, not a separately certified theorem**; a publication version still needs a formal definition of the canonical history partition and a proof that the linked/folded assembly is partition-independent ([STRONG]). [CONJECTURE at that generality; each instantiation below carries its own tag.]

---

## 4. Part II — The spine: definitions → lemmas → theorems → main result

All statements in this section are in canonical $u$; sources and tags per item.

### 4.1 Structure lemmas [PROVEN]

**Lemma 4.1 (Incidence factorization).** Identically in $k$:
$$S(k)+4I=B(k)B(k)^\dagger,\qquad A(k)+4I=N(k)N(k)^\dagger,$$
where $S$ ($A$) is the signed (unsigned) shared-link Bloch adjacency of the three plaquette orbitals. Consequently $S,A\succeq-4I$, and
$$\operatorname{spec}S(k)=\{-4,\ -4+q(k),\ -4+q(k)\}.$$
*Proof:* direct computation of $(BB^\dagger)_{oo'}$; the shared link of an adjacent pair is unique. [PAPER] Lemma 3.1 (proof printed); [GLUE2] §3; [GCSG] §4.2. The signed graph is genuinely frustrated (corner triangles have sign product $-1$), so this is not removable by regauging plaquette orientations — [PAPER] §2 [CERTIFIED].

**Lemma 4.2 (C-even sector has no flat band).** $\det N(k)=-2v_1v_2v_3$, vanishing only on the planes $k_j=\pi$, while $\det B(k)\equiv0$. [PAPER] §3 [PROVEN].

**Theorem 4.3 (Exact flatness).** $w(k)^\dagger=(u_3,-u_2,u_1)$ satisfies $B(k)^\dagger w(k)=0$, hence $S(k)w(k)=-4w(k)$ for every $k$: the lowest C-odd branch has bandwidth exactly zero. $w(k)$ is the Bloch transform of the $\pm1$ signing of the six faces of an elementary cube; the theorem is $\partial_2\partial_3=0$ read in momentum space. [PAPER] Thm 4.1 [PROVEN]. The normalized flat eigenvector has no continuous extension to $\Gamma$ (all three branches meet at $S(0)=-4I$); the band is in the singular class of Rhim–Yang — the compact localized (cube) states fail to span the band. [PAPER] Rmk 4.2.

**Theorem 4.4 (Betti formula for the band dimension).** For any finite complex built from the lattice,
$$\dim(\text{flat band})=\dim Z_2=\#\{\text{cubes}\}+b_2-b_3 .$$
On $T_L^3$: $L^3-1+3=L^3+2$; on $T^2\times I$: $L^3+1$; on $T^1\times I^2$ and the open box $I^3$: $L^3$. The "+2" is $b_2-b_3$, not two accidental states (that older reading is [SUPERSEDED]). Verified by exact rank over $GF(2^{31}-1)$ and by eigenvalue count at $-4$, at $L=3,4$, four topologies. [PAPER] Thm 5.1, Table 1 [PROVEN]+[CERTIFIED]. Cube chains obey the single relation $\sum_xc_x=0$ and span $L^3-1$ dimensions; the three wrapping sheets complete the band ([PAPER] Prop. 5.2 [PROVEN]+[CERTIFIED]).

**Finite-volume isolation.** First non-flat level $=-4+4\sin^2(\pi/L)$: isolation scale $L^{-2}$, not $L^{-1}$. [GLUE2]/[GLUE3] §3.1, [GCSG] §4.3 [PROVEN]. Convention caveat ([GLUE3] §3.1): the simple 12-neighbor adjacency assumes $L\ge3$; at $L=2$ coincident periodic neighbors need a separate multigraph/incidence convention ([PAPER] likewise excludes $L=2$).

### 4.2 Protection theorems [PROVEN]

**Theorem 4.5 (Link-channel rigidity).** If at any order $H(k)=\alpha I+\beta S(k)+B(k)M(k)B(k)^\dagger$ with Hermitian $M(k)$, then $H(k)w(k)=(\alpha-4\beta)w(k)$: the whole band stays exactly flat, rigidly shifted — independent of self-energy, vacuum subtraction, hopping amplitude. [PAPER] Thm 6.2; verified against 200 random Hermitian $M(k)$, worst residual $8.6\times10^{-15}$.

**Theorem 4.6 (All-orders protection on $\mathcal H_2$).** $D_2D_3=0\Rightarrow L_2^{\downarrow}L_2^{\uparrow}=L_2^{\uparrow}L_2^{\downarrow}=0$; every polynomial in the two Laplacians acts on $\mathcal H_2$ by its constant term. A cube-channel correction $S+\epsilon L_2^{\uparrow}$ disperses the compactly-localized part while pinning exactly $b_2$ states at $-4$, for every $\epsilon$. [PAPER] Thm 6.3 [PROVEN]; pinning count checked at $\epsilon\in\{10^{-3},0.37,5,100\}$ [CERTIFIED].
**Scope caveat** ([GLUE2] §6.2): this is an all-orders theorem *inside the boundary-operator algebra*; it is **not** a theorem that every physical correction lies in that algebra. The four-tier outcome ladder ([GLUE2] §6.3): (1) link factorization → whole band flat; (2) harmonic annihilation → band disperses, $\mathcal H_2$ triplet pinned; (3) harmonic scalar → triplet shifts rigidly; (4) cubic-symmetry breaking → only then can the $T_1$ triplet split.

**Quantum numbers.** The C-odd triplet at rest is $T_1^{+-}$; it contains no scalar at rest ($A_1$ overlap vanishes). The interpretation $b_2(T^3)=3\leftrightarrow$ 't Hooft flux directions / $\mathbb Z_N$ two-form center symmetry is recorded as *Interpretation*, not theorem. [PAPER] §8, §5 [CERTIFIED / Interpretation]. [GLUE3] §3.1 adds the parallel firewall for the carrier dictionary (compact cube boundary $=A_1^{--}$, telescoping at $k=0$; harmonic plane triplet $=$ axial $T_1$, $P=+$, $C=-$ from the imaginary-trace source): "the topology of the split is exact; the representation-to-interpolating-operator bridge is a separate analytic interpretation and should not be mislabeled as a measured physical overlap."

**Theorem 4.7 (SU(2) exclusion).** In SU(2), $C$ is a gauge transformation ($U^*=\varepsilon U\varepsilon^{-1}$), so $P_{C=-}=0$: no SU(2) one-flux $T_1^{+-}$ branch exists; the theorem domain is $N\ge3$. [T1PM] §2 [PROVEN].

### 4.3 Second order, all ranks

**Theorem 4.8 (Rank law).** For $N\ge3$, the C-odd shared-link hopping is
$$t_N=\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)}>0,\qquad t_2=0,\qquad t_3=\frac{5}{612},$$
from the four channels $F\otimes F=1\oplus\mathrm{Adj}$, $F\otimes\bar F$-type $=\Lambda^2\oplus\mathrm{Sym}^2$ (antiparallel sum $\mathcal A_N=-\frac{2N^3}{(N^2-1)(2N^2-1)}$, parallel sum $\mathcal B_N=-\frac{4N(N^2-2)}{(N^2-1)(4N^2-9)}$, $t_N=\mathcal B_N-\mathcal A_N$). The $N^{-3}$ law is a cancellation of two $O(N^{-1})$ channel sums:
$$\frac14-N^3t_N=\frac{2N^4+31N^2-9}{4(N^2-1)(2N^2-1)(4N^2-9)}>0,\qquad N^3t_N\nearrow\frac14,\qquad
t_N=\frac1{4N^3}-\frac1{16N^5}-\frac{77}{64N^7}+O(N^{-9})$$
(expansion added in [GLUE3] §4; re-verified symbolically here, next term $-\tfrac{1021}{256}N^{-9}$). [CANON] §10.2, §10.5 (monotonicity: derivative numerator $2x^2(2x^3+62x^2-151x+72)$, $x=N^2$); [GLUE2]/[GLUE3] §4 [PROVEN; deficit identity re-verified here for $N=3,5,9$].
Second-order C-odd spectrum: $\{E^{(2)}_{\rm flat},\,E^{(2)}_{\rm flat}+t_Nq(k)u^2\ (\times2)\}$; full C-odd one-plaquette bandwidth $W_N^{(-)}(u)=12t_Nu^2+O(u^3)\sim3u^2/N^3$; finite-volume split $\Delta^{(2)}_{N,L}=4t_Nu^2\sin^2(\pi/L)+O(u^3)$. [GLUE2] §4, [CANON] §10.5.

**SU(3) second-order ledger** ([PAPER] eq. (7), [GLUE2] §4 — [CERTIFIED]):
$$d_+^{(2)}=\tfrac{223}{1020},\quad t_+^{(2)}=-\tfrac{11}{306},\quad d_-^{(2)}=\tfrac{7}{102},\quad t_-^{(2)}=\tfrac{5}{612},\quad d_-^{(2)}-4t_-^{(2)}=\tfrac{11}{306}.$$
$t_+=-11/306$ **corrects** an earlier $-481/612$ (the vacuum-mediated route $\langle e_r|W|0\rangle\langle0|W|e_i\rangle/(8/3)=+3/4$ was omitted; present for every C-even pair, absent for C-odd since $\langle o|W|0\rangle=0$; discriminated by an independent two-plaquette exact diagonalization). [PAPER] §7 [CERTIFIED]; $-481/612$ is [SUPERSEDED].
Exact $O(u^2)$ band data ([PAPER] App. B): C-even $A_1^{++}$ at $\lambda=12$: $-217/1020$; $E^{++}$ at $\lambda=0$: $+223/1020$; C-even top $+1109/3060$; C-even bandwidth $88/153$; C-even curvature $(22/459)|k|^2$; C-odd flat $+11/306$ (measured spread $3.5\times10^{-17}$); C-odd top $+41/306$; C-odd manifold width $5/51$.

### 4.4 Third order, SU(3) [COLD-CERTIFIED]

**Theorem 4.9 (Factorization through $O(u^3)$).**
$$H_{\mathrm{eff},-}(k,u)=E_{\rm flat}(u)\,I+t(u)\,B(k)B(k)^\dagger+O(u^4),$$
$$E_{\rm flat}(u)=\frac83+u+\frac{11}{306}u^2-\frac{109151}{249696}u^3,\qquad
t(u)=\frac{5}{612}u^2+\frac{1975}{124848}u^3 .$$
Because $B^\dagger w=0$, the cube-boundary branch is $k$-independent through $u^3$:
$$m_{1^{+-}}(k,u)=\frac83+u+\frac{11}{306}u^2-\frac{109151}{249696}u^3+O(u^4)\ \ \text{for every }k.$$
Third-order ledger: $b_3=\frac{1975}{124848}$, $\ell_3=-\frac{12331}{249696}$ (renamed $\operatorname{leak}_3$ in [GLUE3] §5 to avoid collision with the all-rank $\ell_N$), $d_3=\frac{7}{32}+12\ell_3-4b_3=-\frac{109151}{249696}$ (identity re-verified here). Mechanism of third-order rigidity: every three-distinct-plaquette (tromino) numerator vanishes at $O(u^3)$ (bare-link lemma), so the third-order operator retains the second-order incidence structure; trominoes first activate at $O(u^4)$. Sources: [GLUE2] §5 (status: cold-certified/analytic exact; second-order certificate 35/35 gates, third-order 251/251 gates per [STRONG] fresh reproduction — gate counts themselves [RECORD-BACKED]); [PAPER] §7; [MOB] cites the series identically. Status resolution: [CANON] classifies the $O(u^3)$ flat branch "record-backed exact" (raw payload absent from *its* bundle); [RUN15]'s independent finite-cluster oracle reproduces the scalar chain $m_2=11/306$ and $m_3=-109151/249696$ cold (gates 83–84), and its gate 06 verifies all 36 exact $t_3$ hoppings ($\max\mathrm{err}=1.1\times10^{-16}$) — jointly upgrading the corpus-level status of the displayed coefficients to [COLD-CERTIFIED].

### 4.5 Fourth order — see Part §5 (the disputed layer, treated separately and honestly).

### 4.6 Main result of the spine

**Theorem 4.10 (Protected strong-coupling $T_1^{+-}$ lattice band — the corpus's actual "mass" result).**
For SU(3) Kogut–Susskind gauge theory on $T^3_L$ ($L\ge3$), in the one-plaquette-excitation truncation, the lowest C-odd branch:
1. is exactly flat and equals
$m_-(u)=\frac83+u+\frac{11}{306}u^2-\frac{109151}{249696}u^3+O(u^4)$ at every momentum [COLD-CERTIFIED];
2. spans $Z_2$ with $\dim=L^3+2$ on the torus, by the Betti formula [PROVEN];
3. transforms as $T_1^{+-}$ at rest [CERTIFIED];
4. stays flat under *every* correction factoring through the shared-link channel [PROVEN], and retains a $b_2$-fold level pinned at the unperturbed energy under every correction in the boundary-operator algebra, to all orders [PROVEN];
5. first disperses at $O(u^4)$, where the sealed axial data are $A^{\rm shp}_3=5/48$, $B^{\rm shp}_3=D^{\rm shp}_3=0$, $\alpha^{\rm pen}_3=5/12$ [CERTIFIED], with unique band minimum at $\Gamma$ and maximum at $R$ for either disputed kernel (both have $\alpha,\beta>0$) — while the rest scalar and off-axis coefficient remain [DISPUTED] (§5.5);
6. and, for all $N\ge3$: exact flatness, the Betti count, rank-cubic second-order mobility $t_N$, and the fourth-order axial law $\alpha^{\rm pen}_N=640/[N(N^2-1)^3]$ hold with the tags stated per item above.

This is a fixed-lattice, finite-order, one-excitation-truncation statement. It is *not* a glueball mass theorem and *not* a mass-gap theorem ([PAPER] §10; [CANON] App. A; [GLUE2] §15).

### 4.7 Bridge results (spine-adjacent, [PROVEN] locally)

**Operator identity.** $B_i^-(x)=\mathrm{Im\,Tr}\,U_{jk}(x)$ creates the C-odd one-plaquette state; near the identity ($X$ traceless Hermitian):
$$\mathrm{Im\,Tr}\,e^{iX}=-\tfrac16\mathrm{Tr}X^3+\tfrac1{120}\mathrm{Tr}X^5+O(X^7).$$
[GLUE2] §13.3 [PROVEN kinematics].

**Cubic locking.** SU(3): $\mathrm{Im\,Tr}\,U=-\frac{P_3}{6}\prod_{j=1}^3\mathrm{sinc}\frac{\theta_j}{2}$ with form factor in $[\,\frac{81\sqrt3}{16\pi^3},\,1\,]$ on the alcove (sharp; log-concavity proof). SU(4): analogous pair-sum factorization, positive interior form factor. Locking **fails at SU(5)**: $P_5=\frac56P_2P_3+5e_5$, and the explicit family $\theta=t(-10,-7,9,\frac{17}{2},-\frac12)$ has $P_1=P_3=0$, $P_5=-\frac{26775}{2}t^5\neq0$, $\mathrm{Im\,Tr}\,e^{iX}=-\frac{26775}{240}t^5+O(t^7)$ (decoded from [CANON] §9.5; re-verified arithmetically). Odd-Casimir staircase: primitive odd directions $e_3$ ($N\ge3$), $+e_5$ ($N\ge5$), $+e_7$ ($N\ge7$), … [CANON] §9, [GCSG] §3.4 [PROVEN].

**Local overlap theorem.** With $m=\frac{81\sqrt3}{16\pi^3}$: $\langle\phi_-,\mathrm{Im\,Tr}U\,\phi_0\rangle\neq0$, bounded between $\frac{m}{6}\langle\phi_-,P_3\phi_0\rangle$ and $\frac16\langle\phi_-,P_3\phi_0\rangle$; Kantorovich correlation bound $\mathrm{Corr}(\mathrm{Im\,Tr}U,-P_3/6)\ge\frac{2\sqrt m}{1+m}=0.829106\ldots$ [CANON] §9.2–9.3 [PROVEN, local one-plaquette only — "does not determine the spectral weight of a spatially extended glueball state"].

**Improved sources** (branch-free): $\mathcal O_3^{\rm imp}=(32A-B)/24=-P_3/6+P_7/1260+O(|X|^9)$ (quintic contamination cancelled); $\mathcal O_5^{\rm prim}=B-8A+2EA=e_5+O(|X|^7)$, $=\det X$ for SU(5); $A=\mathrm{Im\,Tr}U$, $B=\mathrm{Im\,Tr}U^2$, $E=N-\mathrm{Re\,Tr}U$. [CANON] §9.7, [GCSG] §3.4 [PROVEN kinematics].

---

## 5. Part III — The fourth order: sealed core, disputed shell

This is the layer where the corpus is in active disagreement with itself. The treatment below separates (a) what both computations agree on and is sealed, (b) the exact all-rank structure conditional on the historical kernels, (c) the dispute, displayed with both numbers.

### 5.1 Generic obstruction space [PROVEN / CERTIFIED]

The exact fourth-order enumeration (144 ordered two-hop sequences → 12 space-group orbits) gives numerator span $q\varepsilon_4\in\operatorname{span}\{q,q^2,qe_2,e_2,e_3\}$, rank five; after removing the scalar, the general cubic-invariant correction on the generic flat fiber is the **four-dimensional** space of §1.3:
$$\varepsilon_4(k)=c_0+A^{\rm shp}q+B^{\rm shp}e_2+C^{\rm shp}\frac{4e_2}{q}+D^{\rm shp}\frac{e_3}{q}.$$
Checkpoint extraction from $\Delta_K=\varepsilon_4(K)-\varepsilon_4(\Gamma)$ at $X=(\pi,0,0)$, $M=(\pi,\pi,0)$, $P=(\pi,\pi/2,0)$, $R=(\pi,\pi,\pi)$:
$$A^{\rm shp}=\frac{\Delta X}{4},\quad B^{\rm shp}=\frac{\Delta X+4\Delta M-6\Delta P}{16},\quad C^{\rm shp}=\frac{3(2\Delta P-\Delta M-\Delta X)}{8},\quad D^{\rm shp}=\frac{3(\Delta R-6\Delta M+6\Delta P)}{16}.$$
Infrared tiers: $\{q,4e_2/q\}$ scale as $L^{-2}$; $\{e_2,e_3/q\}$ as $L^{-4}$ (sheet/tube mechanisms). Regularity filtration: $e_2/q\in C^1\setminus C^2$, $e_3/q\in C^3\setminus C^4$ at $\Gamma$. Finite-torus fingerprints (ground multiplicities / first positive values, $a_L=4\sin^2\frac{\pi}{L}$): $q$: $3$, $a_L$; $4e_2/q$: $3L$, $2a_L$; $e_2$: $3L$, $a_L^2$; $e_3/q$: $3L^2-3L+3$, $a_L^2/3$; zero correction: $L^3+2$. [CANON] §12 [PROVEN + exact certificate inputs]; [GCSG] §4.5. A "generic two-shape fourth-order theorem" is explicitly prohibited ([CANON] App. A): the two-invariant pencil is a *dynamical* restriction, not a symmetry identity.

### 5.2 The sealed physical core (agreed by both disputed kernels) [CERTIFIED]

$$\boxed{\;A^{\rm shp}_3=\frac{5}{48},\qquad B^{\rm shp}_3=D^{\rm shp}_3=0,\qquad \alpha^{\rm pen}_3=4A^{\rm shp}_3=\frac{5}{12}\;}$$
Historical kernel: exact rational ([T1PM] §10, [GCSG] §4.9). New folded run: $A=0.104166666666728$, $B=3.6\times10^{-16}$, $D=2.2\times10^{-13}$, $\alpha=0.41666666666691$ ([RUN15] gates 61–64, PASS). [GLUE2] §10: "the only presently sealed physical shape data"; [GLUE3] §10 adds the precision qualifier that the *new-run* values are consistent with, but not exact rational equalities to, $5/48,0,0,5/12$ — the sealed core is thus: exact on the historical side, numerically confirmed to $\lesssim2.3\times10^{-13}$ on the new side. Equivalently the elementary-cube completion coefficient $c_4^{\square}(3)=-5/48$, $\alpha_3=4|c_4^{\square}(3)|=5/12$ ([MOB] §4).

**Physical tier collapse.** $B^{\rm shp}_N=D^{\rm shp}_N=0$ at every solved rank ($N=3,4,5,6$ and stable $N\ge7$): the $L^{-4}$ tier allowed by cubic symmetry is not selected by the microscopic contraction — a dynamical selection rule with no proved mechanism ([GCSG] §4.6 [exact within accepted ledgers]; open "why" in [CANON] App. B).

### 5.3 All-rank structure (conditional on the historical kernel family) [OUTPUT-CERTIFIED / RECORD-BACKED]

**Axial law, all $N\ge3$:**
$$\boxed{\;\alpha^{\rm pen}_N=\frac{640}{N(N^2-1)^3}\;}\qquad
\alpha^{\rm pen}_3=\frac{5}{12},\quad \alpha^{\rm pen}_4=\frac{32}{675},\quad \alpha^{\rm pen}_5=\frac{1}{108},\quad \alpha^{\rm pen}_6=\frac{64}{25725}$$
(all four exceptional values re-verified against the closed form here). $\Delta\alpha_N=0$ at every rank: exceptional (determinant) sectors never touch the axial channel — certified fact, not a scalarity consequence (they are non-scalar at $N=3$). Threshold structure: a fourth-order word has $\le6$ character factors, so determinant channels need $|p-q|=N\le6$; the exceptional set is exactly $\{3,4,5,6\}$. [T1PM] §4; [GCSG] §4.7 (status: "exact certificate-backed rank identity; audit-hardened proof status"); first fourth-order finite-volume lift $\Delta^{(4)}_{N,L}=\alpha^{\rm pen}_N\sin^2(\pi/L)$.

**Diagonal coefficient (historical family):**
$$\beta^{\rm pen}_3=\frac{17607806155349}{275331901291200},\qquad
\beta^{\rm pen}_N=\frac{P_{17}(z)}{N\,R_{20}(z)}\ (z=N^2,\ N\ge4),\qquad
\beta^{\rm pen}_4=\frac{3601925923737103752887}{70481696720359496343750},$$
with $P_{17}$ as printed in [GLUE2] App. A and
$$R_{20}(z)=(z-1)^3(2z-3)(2z-1)^3(3z-2)(3z-1)(4z-9)^3(4z-5)(4z-1)(9z-25)(9z-16)(16z^2-44z+25)(16z^2-33z+16).$$
Consolidation checks: $P_{17}(16)/(4R_{20}(16))$ equals the independent SU(4) certificate value exactly; $P_{17}(9)/(3R_{20}(9))=B_3^{\rm bal}=\frac{15644916262153}{34416487661400}$, consistent with the SU(3) anomaly below; leading ratio $=6170/9$, confirming the stated large-$N$ coefficient.

**SU(3) anomaly** ([T1PM] §5.1; [GCSG] §4.8): the $\nu=\pm3,\pm6$ epsilon sectors are non-scalar at $N=3$:
$$\Delta\beta^{\rm pen}_3=\beta_3^{\rm full}-\beta_3^{\rm bal}=-\frac{25}{64}\quad\Bigl(=-\tfrac{15}{16}\alpha^{\rm pen}_3\Bigr),\qquad
\Delta C^{\rm shp}_3=-\frac{25}{1024},\qquad
\Delta q_3=-\frac{16863189551}{76406976000}.$$
Hence "determinant sectors shift only $q_N$" is **true for $N\ge4$, false for SU(3)** — and any quotient-scalarity conjecture must be restricted to $N\ge4$ ([GCSG] §4.8). Exceptional rest shifts: $\Delta q_4=-\frac{304746539168}{160249753125}$ (certified as the flat-branch eigenvalue identity $H^{\rm exc}_{4,4}(k)\psi(k)=\Delta q_4\psi(k)$, **not** as $\Delta q_4I_3$ — the stronger reading is [SUPERSEDED], [CANON] §13.4); SU(5): none (895,524-pair scan empty); $\Delta q_6=\frac{6}{343}$.

**Fourth-order rest energies (historical family; the $N=3$ entry is the disputed scalar of §5.5):**
$$q_3=-\frac{20721577909065127111}{7250590288602460800},\qquad
q_4=-\frac{162485785670299274695454289332603}{121294607143027203361265133093750},$$
$$q_5^{(\mathrm{SU}(5),\,4^{\rm th}\ \rm ord)}=-\frac{781009569168365268247626732239}{6484474594581730088957376233472},\qquad
q_6=-\frac{55954617740619111266546735567327219227}{2665788121217129017242143775195086906250}.$$
Stable rank $N\ge7$: $q_N=-\frac{2}{3N}\frac{Q_{32}(z)}{D_{34}(z)}$ with positive-Newton-expansion numerator ($b_j>0$) and explicitly factorized positive denominator, so $q_N<0$ for all $N\ge7$; $\beta^{\rm pen}_N=P_{402}(N)/D_{409}(N)>0$ likewise. The 33- and 403-coefficient ledgers are **not in this corpus** → [RECORD-BACKED]. [T1PM] §6.

**Global band theorem (conditional on the family):** $\alpha^{\rm pen}_N,\beta^{\rm pen}_N>0$ ⇒ $\Gamma$ unique minimum, $R$ unique maximum, bandwidth $\Delta c_{4,N}=\alpha^{\rm pen}_N+\beta^{\rm pen}_N$; SU(4): $\Delta c_{4,4}=\frac{2314426811641505637629}{23493898906786498781250}$ (re-verified). [T1PM] §7.

**Large-$N$ flattening (from the stable formulas):**
$$q_N=-\frac{227}{N^5}-\frac{1638943}{864N^7}+O(N^{-9}),\quad
\alpha^{\rm pen}_N=\frac{640}{N^7}+\frac{1920}{N^9}+\cdots,\quad
\beta^{\rm pen}_N=\frac{6170}{9N^7}+\frac{677903}{324N^9}+\cdots,$$
$$\Delta c_{4,N}=\frac{11930}{9N^7}+O(N^{-9}),\qquad \frac{\Delta c_{4,N}}{|q_N|}=\frac{11930}{2043N^2}+O(N^{-4}):$$
rest energy $\sim N^{-5}$, mobility $\sim N^{-7}$ — parametric large-$N$ flattening. [T1PM] §8 [derived from record-backed $Q_{32}/D_{34}$, $P_{402}/D_{409}$; the $\alpha$ and $\beta$ leading terms re-verified here from the in-corpus closed forms].

**Non-parabolic minima and DOS** ([CANON] §13.5 [PROVEN corollary]): on the physical plane, $c_{4,N}(k)-c_{4,N}(\Gamma)=r^2g_N(n)+O(r^4)$ with $g_N(n)=\frac{\alpha^{\rm pen}_N}{4}+\frac{\beta^{\rm pen}_N-2\alpha^{\rm pen}_N}{4}\sum_{i<j}n_i^2n_j^2$; SU(3)/SU(4) bands are $C^1$ but not $C^2$ at $\Gamma$ (no effective-mass tensor); $g_{100},g_{110},g_{111}$ (SU(3)) $=0.104166667,\ 0.056080283,\ 0.040051489$; DOS $\rho(E)=\frac{E^{1/2}}{2^2\pi^3}\!\cdot\!\frac18\int_{S^2}g_N(n)^{-3/2}d\Omega+o(E^{1/2})$ up to the printed normalization ([CANON] §13.5.1). Positivity in every direction ⇔ $A^{\rm shp}>0$ and $A^{\rm shp}+\tfrac43C^{\rm shp}>0$.

**Generalized Hodge pencil — the exact operator meaning** ([GLUE3] §7; supersedes the flatter SOS presentation of [GLUE2] §7). Pull $H_4$ back to cube amplitudes through $\mathsf C=\partial_3$:
$$Q_4:=\mathsf C^\dagger H_4\mathsf C,\qquad G:=\mathsf C^\dagger\mathsf C=\sum_iL_i,\qquad
L_i=\nabla_i^\dagger\nabla_i=2I-T_i-T_i^{-1},\ \nabla_i=T_i-I .$$
With the cubic $\Gamma$ block scalar, $s_4=\tfrac13\operatorname{tr}H_4(\Gamma)$, $K_4=H_4-s_4I$, $\mathcal Q_4=\mathsf C^\dagger K_4\mathsf C=Q_4-s_4G$. The centered band coefficient is **not** an ordinary eigenvalue of $\mathcal Q_4$; it solves the generalized problem
$$\boxed{\ \mathcal Q_4\phi=\lambda_4\,G\phi\ },\qquad\text{with scalar-gauge freedom}\quad (Q_4,G)\sim(Q_4+\delta G,\,G).$$
Symbols: $G(k)=2\mathsf S$, $\mathcal Q_4(k)=\alpha\mathsf Q+\beta\mathsf R$, so $\lambda_4(k)=\frac{\alpha\mathsf Q+\beta\mathsf R}{2\mathsf S}$, and in real space
$$\mathcal Q_{4,N}=\frac{\alpha^{\rm pen}_N}{4}\sum_iL_i^2+\frac{\beta^{\rm pen}_N}{4}\sum_{i<j}L_iL_j\succeq0\quad(\alpha,\beta>0)\ \ \textbf{on cube amplitudes};$$
[GLUE3] adds the scope warning: this does **not** imply $K_4\succeq0$ on the full plaquette space and does not by itself determine the harmonic $\mathcal H_2$ sector. SU(3) historical instance $\frac{5}{48}\sum_iL_i^2+\frac{17607806155349}{1101327605164800}\sum_{i<j}L_iL_j$; scalar-gauge invariance $\mathsf C^\dagger[(H_4+\delta I)-(s_4+\delta)I]\mathsf C=\mathsf C^\dagger(H_4-s_4I)\mathsf C$ (the "safe interpretation rule", [GLUE2] App. B = [GLUE3] App. B — now stated as a **same-kernel** identity, see §5.5).

**Edges, anchors, holdout.** $0\le\lambda_4\le\alpha+\beta$ with unique edges at $\Gamma$/$R$ in the continuous zone (and on even-$L$ tori; an odd-$L$ grid does not contain $R$ — [GLUE3] §7.1): $W_4=\alpha+\beta$. High-symmetry anchors ([GLUE3] §7.2, re-verified):
$$\lambda_X=\alpha,\qquad \lambda_M=\alpha+\tfrac\beta2,\qquad \lambda_R=\alpha+\beta;\qquad
\alpha=\lambda_X,\ \beta=2(\lambda_M-\lambda_X),\ \text{with }\lambda_R=2\lambda_M-\lambda_X\text{ reserved as a blind holdout}.$$

**Curvature reinterpretation** ([GLUE3] §7.3, superseding the "Hessian curvature" wording of [GLUE2] §7.4, which itself superseded the $t^2$-coefficient misread $\alpha/4$, $\alpha/8+\beta/16$, $(\alpha+\beta)/12$): the quantities
$$\kappa(n)=2a(n)=\tfrac12\bigl[\alpha\textstyle\sum_in_i^4+\beta\sum_{i<j}n_i^2n_j^2\bigr],\qquad
\kappa_{100}=\tfrac\alpha2,\ \kappa_{110}=\tfrac\alpha4+\tfrac\beta8,\ \kappa_{111}=\tfrac{\alpha+\beta}6,$$
are **radial directional curvatures, not entries of a Hessian at $\Gamma$**: a genuine cubic-symmetric quadratic Hessian would require direction-independence, i.e. $\beta=2\alpha$, which the historical kernel violates ($\beta_{\rm old}=0.0640\ldots\neq2\alpha=5/6$) — so the band has cubic warping and no effective-mass tensor at $\Gamma$ (consistent with the $C^1\!\setminus\!C^2$ regularity of [CANON] §13.5). At $R$ the Hessian **is** genuinely isotropic: $\nabla^2\lambda_4(R)=-\frac{\alpha+\beta}{6}I$. Historical SU(3) values: $W_{4,\rm old}=\frac{132329431693349}{275331901291200}=0.48061786909826\ldots$, $\kappa_{110}=\frac{247051057231349}{2202655210329600}$, $\kappa_{111}=\frac{132329431693349}{1651991407747200}$ (all re-verified from $\alpha_{\rm old},\beta_{\rm old}$).

**Exact 25-point numerator stencil** ([GLUE3] §8.1 — new in v3.1; all weights re-verified here from the pencil form): on cube amplitudes $(\mathcal Q_4\phi)_x=w_0\phi_x+w_1\sum_i(\phi_{x\pm e_i})+w_2\sum_i(\phi_{x\pm2e_i})+w_d\sum_{i<j}\sum_{\sigma,\tau=\pm1}\phi_{x+\sigma e_i+\tau e_j}$ with
$$w_0=\tfrac92\alpha+3\beta,\quad w_1=-(\alpha+\beta),\quad w_2=\tfrac\alpha4,\quad w_d=\tfrac\beta4,\qquad
\boxed{w_0+6w_1+6w_2+12w_d=0}\ \text{(zero-mode gate)};$$
historical kernel: $w_0=\frac{189690244462349}{91777300430400}$, $w_1=-\frac{132329431693349}{275331901291200}$, $w_2=\frac{5}{48}$, $w_d=\frac{17607806155349}{1101327605164800}$. Dividing the stencil's Fourier symbol by $G(k)=2\mathsf S$ gives the physical centered coefficient.

**Large-rank shape ratio** ([GLUE3] §11, re-verified): $\beta_N/\alpha_N\to\frac{617}{576}$ as $N\to\infty$.

**Near-$\Gamma$ uniformity warning** ([GLUE3] §7.4): the fixed-$k$ quotient algebra is exact, but the $O(u^2|k|^2)$ branch separation competes with $O(u^4)$ terms for $|k|\lesssim u$; a band theorem uniform in $(u,k)\to(0,0)$ needs a separate two-parameter estimate (= gap G11).

### 5.4 Exact band-point data, SU(3) historical kernel [exact for the supplied kernel]

| Point | exact $c_4$ | lift above $\Gamma$ |
|---|---|---|
| $\Gamma$ | $-20721577909065127111/7250590288602460800$ | $0$ |
| $X$ | $-17700498622147435111/7250590288602460800$ | $5/12$ |
| $M$ | $-4367164159624988707/1812647572150615200$ | $247051057231349/550663802582400$ |
| $R$ | $-3447362930970494909/1450118057720492160$ | $132329431693349/275331901291200$ |

Kernel SHA-256 `d2a4121a9798b2c364a52f7845fd7014ce2463563642470102cb080336a9fd51`; semantic SHA-256 `48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77`. [T1PM] §10. (Lifts re-verified: $M$-lift $=\alpha_{\rm old}+\beta_{\rm old}/2$, $R$-lift $=\alpha_{\rm old}+\beta_{\rm old}$.)

### 5.5 THE DISPUTE — two fourth-order kernels, neither promoted [DISPUTED]

Two computations of the physical SU(3) $O(u^4)$ one-flux kernel exist. They agree exactly on §5.2 and disagree on two invariants. Per [RUN15]'s final verdict and [GLUE2] §10/§15, **neither is promoted**; both are displayed.

| Invariant | Historical 189-record kernel ([T1PM], [GCSG] §4.9/4.11) | v10a.26 folded run + linked-cluster oracle ([RUN15], [GLUE3] §§8–10) | Discrepancy |
|---|---|---|---|
| Rest scalar at $\Gamma$ | $q_3=-\frac{20721577909065127111}{7250590288602460800}=-2.857915988114559$ (exact rational) | $m_\Gamma^{(4)}=-0.7751458630189173$ (float; independent finite-cluster linked oracle, 33 shape classes / 203 clusters) | $\Delta_\Gamma=2.0827701250956414$ |
| Off-axis shape $C^{\rm shp}$ | $C_{\rm old}=-\frac{211835444920651}{4405310420659200}=-0.04808638318135875$ (exact rational; $=(\beta_{\rm old}-2\alpha)/16$, re-verified) | $C_{\rm new}=-0.020213328886166577$ (float; folded degenerate-SW matrix) | $\Delta_C=0.027873054295192174$ |
| Implied $\beta^{\rm pen}$ | $\beta_{\rm old}=0.0639512\ldots$ | $\beta_{\rm new}=8A^{\rm shp}+16C_{\rm new}\approx0.5099200711546681$ | — |
| Implied bandwidth $W_4$ | $0.48061786909826$ | $\approx0.9265867378213348$ | factor $\approx1.93$ |
| Off-axis band difference | — | — | $\Delta\varepsilon_4(M)=8\Delta_C\approx0.2229844343615374$, $\Delta\varepsilon_4(R)=16\Delta_C\approx0.4459688687230748$; axial cuts (incl. $X$) agree exactly |
| Axial data $A^{\rm shp},B^{\rm shp},D^{\rm shp},\alpha$ | $5/48,\,0,\,0,\,5/12$ | $5/48,\,0,\,0,\,5/12$ (to $\le2.3\times10^{-13}$) | **agree — sealed** |

**Supporting facts, both directions** (revised per [GLUE3] §§2.3, 9–10, which control).
- *For the new scalar:* its data flow computes the linked scalar before the historical $q_{\rm old}$, historical shape, or final diagonal adjustment enters, and the lower orders were recovered first — "meaningful **blind** numerical evidence for the linked $\Gamma$ coefficient" ([GLUE3] §9). The Hamer-convention cross-check $8a_4=8\times(-0.0968932328773)=-0.7751458630184$ agrees to $\approx5.2\times10^{-13}$, **but** the decimal $a_4$ is a notebook transcription not yet verified against a hashed primary Hamer table ([GLUE3] §2.3) — a strong local normalization check, not primary-source verification. 86/86 hard gates passed.
- *For the historical kernel:* it is exact rational, hash-anchored, and its band edges/curvatures were independently reproduced by the [GCSG] v1.4 audit. The scalar difference alone is *not* evidence against it: within **one chosen kernel** the identity $H_4^{\rm new,mass}-m_\Gamma^{(4)}I=\widehat H_4^{\rm new}-\widehat s_{\rm new}I$ (equivalently $\mathsf C^\dagger[(H_4+\delta I)-(s_4+\delta)I]\mathsf C=\mathsf C^\dagger(H_4-s_4I)\mathsf C$) is exact. **[GLUE3] firewall:** this is a *same-kernel* identity; the arithmetic difference $\Delta_\Gamma$ does **not** prove $H_4^{\rm new}=H_4^{\rm old}+\Delta_\Gamma I$, and no calculation derives $\Delta_\Gamma$ as a physical counterterm or proves $H_4^{\rm new,centered}=H_4^{\rm old,centered}$ ([GLUE3] §9.2). The coordinate map $u_{\rm old}=u+\delta u^4+a_5u^5+\cdots$ with $\delta=\Delta_\Gamma$ is a valid *convention* in the minimal gauge $a_5=a_6=a_7=0$; nothing establishes it as the physically selected one ([GLUE3] §9.3). What re-anchoring **cannot** reconcile is $C^{\rm shp}$ — "a full reconciliation must derive the missing non-scalar operator, not merely add a diagonal constant" ([GLUE3] App. B).
- *Disclosure on the run's internal shift* ([GLUE3] §9.2): the final diagonal shift actually applied in the 15-hour run was $+11.17343231638178$ (printed in [RUN15] as "independently linked local shift"), chosen to move a raw folded rest value to the linked scalar — it was **not** $\Delta_\Gamma$, and the run's final Γ-rest = cluster-oracle equality (gate 85, $2.0\times10^{-15}$) is **by construction**, not an independent scalar verification.
- *Also on record:* a "quarantined scalar shortcut" $-\frac{160506019419340168451}{14501180577204921600}=-11.068479463778765$ appears in [RUN15]'s unblind block and is rejected by both sides (the raw folded axial Γ-block before linked vacuum subtraction was $-11.9485781794007$; the linked vacuum $O(u^4)$ subtraction around the mark is $-\frac{1474623}{1675520}\approx-0.8800987156226097$).
- *Precision status of the new shape fit* ([GLUE3] §10): $A_{\rm new}=0.104166666666728$, $B_{\rm new}\approx3.55\times10^{-16}$, $D_{\rm new}\approx2.23\times10^{-13}$ are *consistent with* $5/48,0,0$ but are *not exact rational equalities from the new run*; the exact tier collapse and an exact rational $C_{\rm new}$ remain open. The centered difference, if both tier collapses are accepted: $\mathsf C^\dagger[\,(H_4^{\rm new}-s_{\rm new}I)-(H_4^{\rm old}-q_{\rm old}I)\,]\mathsf C=4\Delta_C\sum_{i<j}L_iL_j\succeq0$, i.e. $\lambda_{\rm new}-\lambda_{\rm old}=8\Delta_C\,\mathsf R/\mathsf S\ge0$, vanishing on momentum axes — "the unresolved fourth-order problem has been compressed to **one planar mixed-gradient direction**."
- *Consequences while unresolved:* the [T1PM] §9.2 "complete rest-mass series" (with $-2.8579\ldots u^4$ and the fifth-order term), the §9.4 $m/\sqrt\sigma$ ratio at orders 4–5, and the fourth-order bandwidth are all conditional on the historical kernel's upstream identification; the [T1PM] §13 box "rank-complete fourth-order band theorem: proved" is **downgraded** by the later documents to "exact-arithmetic computational ledger — audit pending" ([GCSG] §4.11.3) and "do not promote either" ([RUN15]). The six closure gates named by [GCSG] §4.11.2 are: $PVP=aP$; degenerate folded-formula regression; full Stage-3H independent regression (1,478→3,895 topologies); magnetic-prefactor normalization; outward-rounded interval rigor; near-$\Gamma$ touching/uniformity. [RUN15] closed the first two ($PVP=+I$ certified; exact dim-$P$=2 SW regressions) and disagreed with the historical $C$ — which is precisely why the verdict is "third result" rather than a confirmation either way.

**Adjudication path** ([GLUE3] §18.1, superseding the six-item sketch of [GLUE2] §16.1). The next physical run must freeze and authenticate, before unblinding: (1) canonical $u$ normalization *and its erratum*; (2) the exact order-four occurrence schedule; (3) all $203\times3=609$ exact rational marked-cluster evaluations plus a rooted Möbius ledger; (4) linked subtraction applied to the **vacuum-subtracted** object (cluster-additivity rule, §6.3); (5) checkpoint hashes and input identities, comparison targets loaded only after sealing; (6) no historical target in scalar or shape data flow; (7) a cold 3,895-topology Stage-3H run producing an unshifted 189-record kernel; (8) direct $X/M$ extraction with $\lambda_R=2\lambda_M-\lambda_X$ as blind holdout, then full Laurent-symbol equality; (9) an independent scalar ledger testing $q_{\rm band}^{(4)}-E_0^{(4)}\stackrel{?}{=}m_\Gamma^{(4)}$ (i.e., whether $\Delta_\Gamma$ is a fourth-order vacuum term — the one concrete reconciliation hypothesis on the table); (10) the $W_{22}$ order-schedule toggle across all 33 rooted classes; (11) both $m_\Gamma^{(4)}$ and $C^{(4)}$ from the same run. Inventory trap flagged by [GLUE3] §18.2: the 3,895 Stage-3H topologies and the 3,850 stable-rank trace topologies are **different inventories** and must never be interchanged. [MCE] status per [GLUE3] §18.1: "passes its cheap algebra and geometry preflights, but it has not produced a full physics certificate" — **no seal exists in this corpus**.

### 5.6 Changes from [GLUE2] to [GLUE3] (delta log, all adopted above)

1. $Y=4u$ reread as a **label erratum** (coefficients were already in $u$); no $4^n$ rescaling is ever to be applied (§1.1).
2. Hamer $a_4$ decimal flagged as an unverified notebook transcription (§1.1, §5.5).
3. Centered fourth-order object recast as the **generalized pencil** $\mathcal Q_4\phi=\lambda_4G\phi$ with $(Q_4,G)\sim(Q_4+\delta G,G)$; positivity scoped to cube amplitudes; harmonic sector explicitly undetermined by it (§5.3).
4. $\kappa$'s reread as radial directional curvatures; no $\Gamma$ Hessian unless $\beta=2\alpha$; isotropic Hessian $-\frac{\alpha+\beta}{6}I$ at $R$ (§5.3).
5. New exact 25-point stencil with zero-mode gate; $X/M$-fit + blind-$R$-holdout protocol; odd-$L$ grid caveat for $W_4$ (§5.3).
6. Re-anchoring demoted to a same-kernel identity; "old = new + scalar" explicitly **Not established**; the run's $+11.17343231638178$ shift disclosed as target-derived (§5.5).
7. New-run shape values labeled numerical (tier collapse not exact from the new run) (§5.5).
8. $\beta_N/\alpha_N\to617/576$; $t_N$ large-$N$ expansion added (§5.3, §4.3).
9. Adjudication protocol expanded 6→11 items, incl. the $q_{\rm band}-E_0^{(4)}\stackrel{?}{=}m_\Gamma$ vacuum-ledger test and the 3,895-vs-3,850 inventory warning (§5.5).
10. `next14.json` Monte Carlo record downgraded to "structured finite-volume numerical evidence, not a cold-reproducible ensemble certificate" — one 23/23 gate is a literal truth value; JSON not source-hash-bound; no raw ensemble found (§7.7).
11. Cluster-additivity rule made explicit: $H_{\rm eff}$ is not cluster additive; $H_{\rm eff}-eI$ is; subcluster subtraction applies to the vacuum-subtracted object (§6.3).
12. Mobility-order taxonomy $r_{\rm split}$, $r_{\rm off}$, $r_{\rm mob}$ introduced, with $r_{\rm off}\le r_{\rm mob}$ (§6.3).
13. $c_{r,\rm prim}$ scoped as the archived color-counting law of a *restricted primitive simple-loop channel*, "not a universal formula for complete order-$r$ amplitudes" (§6.3).
14. Representation dictionary ($A_1^{--}$ cube boundary vs axial $T_1$ harmonic triplet) marked "analytic interpretation, not a measured physical overlap"; $L=2$ multigraph caveat for the 12-neighbor convention (§4.1–4.2).


---

## 6. Part IV — Companion theory

### 6.1 Layer I: compact one-plaquette spectral theory (weak well, $\beta\to\infty$)

Regime firewall: this is a *separate expansion regime* from §§4–5; no coefficient transfers without an explicit bridge ([GCSG] §1.2). The exact fixed-rank bridge that does exist is the operator identity on the restricted one-plaquette flux tower: $h_{\rm loop}=4H_\beta^{(N)}-4\beta$ at $\beta=Ny/2$ ([CANON] §10.1) — an identity, not a spectral equivalence.

**Theorem 6.1 (Compact SU(3) even class gap; [PROVEN], with $O(\beta^{-1})$ remainder proved in-corpus).**
$$\Delta_+^{SU(3)}(\beta)=\sqrt{\frac{2\beta}{3}}-\frac{5}{16}-\frac{311\sqrt6}{9216}\,\beta^{-1/2}-\frac{5665}{110592}\,\beta^{-1}+\cdots$$
First three terms proved via exact Weyl conjugation $J(\tfrac12C_2)J^{-1}=\tfrac14(-\Delta_{\mathfrak t}-|\rho|^2)$, unique nondegenerate Wilson well ($D^2W(0)=\tfrac13I_2$), $h=\beta^{-1/2}$ scaling, and an equivariant harmonic-well lemma (Agmon/IMS + polynomial-Gaussian quasimodes, residual $O(h^4)$; special case of Charles–Vũ Ngọc) — [GCSG] App. A, full proof printed. Exact ingredients: $\Delta_{H_2}=\frac{19\sqrt6}{576}$, $\Delta_{\rm res}=-\frac{205\sqrt6}{3072}$, moments $\langle p_2^3\rangle,\langle p_3^2\rangle=(120,5)_{\psi_0},(480,20)_{\psi_1}$. The $\beta^{-1}$ coefficient is exact arithmetic with the analytic $O(\beta^{-3/2})$ remainder at that order open. The **non-radial escape** is the theory's first "escape theorem": a radial-only computation gives $c_1^{\rm rad}$, and $c_1-c_1^{\rm rad}=\frac{\sqrt6}{576}$ — the degree-six invariant $p_3^2$ is the first even escape from $\mathbb R[p_2]$ [PROVEN].

**Theorem 6.2 (Fixed-rank SU(N) gaps; [PROVEN at fixed $N$] / [CERTIFIED $N=3..12$] / [CONJECTURE as unrestricted formulas]).** With leading gaps $\sqrt{2\beta/N}$ (even, shell $s=2$) and $\sqrt{9\beta/2N}$ (odd, shell $s=3$; $P_3$):
$$c_0^{(N),+}=-\frac{2N^2-3}{16N},\qquad c_0^{(N),-}=-\frac{3(N^2-3)}{16N},$$
$$c_1^{(N),+}=-\frac{\sqrt2\,(6N^4-24N^2+41)}{1024\,N^{3/2}},\qquad
c_1^{(N),-}=-\frac{\sqrt2\,(14N^4-97N^2+290)}{1536\,N^{3/2}},$$
$$c_2^{(N),+}=-\frac{60N^6-401N^4+1522N^2-2297}{49152\,N^2},\qquad
c_2^{(N),-}=-\frac{95N^6-981N^4+5853N^2-15335}{49152\,N^2}.$$
Machinery: traceless Hermitian Gaussian representation of the Weyl-Gaussian measure ($\mathbb E X_{ab}X_{cd}=\tfrac12(\delta_{ad}\delta_{bc}-\tfrac1N\delta_{ab}\delta_{cd})$), exact cut-join recursion for all moments (symbolic in $N$; no Monte Carlo), exact Gram projection $\|\Pi F\|^2=v^TG^{-1}v$ with low-rank trace-identity reduction. Key exact moments (from [CANON] §5.3.1): $\mathbb E P_3^2=\frac{3(N^2-1)(N^2-4)}{8N}$, $\mathbb E P_4=\frac{(N^2-1)(2N^2-3)}{4N}$, $\mathbb E P_6=\frac{5(N^2-1)(N^4-3N^2+3)}{8N^2}$, $\mathbb E P_3P_4P_3=\frac{3(N^2-1)(N^2-4)(2N^4+31N^2-105)}{32N^2}$, $\mathbb E P_3P_6P_3=\frac{15(N^2-1)(N^2-4)(N^6+32N^4-180N^2+315)}{64N^3}$. Odd decomposition: $q^{(N)}_{H_2,-}=\frac{6N^4-31N^2+53}{768N^2}$, $q^{(N)}_{\rm res,-}=-\frac{26N^4-159N^2+396}{1536N^2}$ (sum $=-\frac{14N^4-97N^2+290}{1536N^2}$, re-verified; $N=3$: $\frac{65}{1728}-\frac{119}{1536}=-\frac{551}{13824}$, matching the certificate table); even: $q^{(N)}_{H_2,+}=\frac{N^4-3N^2+3}{192N^2}$, $q^{(N)}_{\rm res,+}=-\frac{34N^4-120N^2+171}{3072N^2}$, sum $=-\frac{6N^4-24N^2+41}{1024N^2}$. SU(3) values: $c_1^-(3)=-\frac{551\sqrt6}{13824}$, $c_2^+(3)=-\frac{5665}{110592}$, $c_2^-(3)=-\frac{53}{864}$ (odd $\beta^{-1}$ fit selects $-53/864$ over superseded $-1781/55296$). Exact-arithmetic certificate table for $N=3,\dots,12$ printed in [CANON] §17.1. Sources: [CANON] §§5–7, [GCSG] §3.2/3.2b. Verification gaps: even $N=4,5$; odd $N=4,5,6$ (blocked by power-sum overcompleteness at small rank; resolved at $N=3$ in the true rank-two basis $\{p_2,p_3\}$ with $P_4=\tfrac12p_2^2$, $P_6=\tfrac14p_2^3+\tfrac13p_3^2$, $P_8=\tfrac18p_2^4+\tfrac49p_2p_3^2$ — trace identities re-verified symbolically in this consolidation).

**Corollary 6.3 (Polarity-excess law; [PROVEN corollary]).**
$$\Delta_-^{(N)}-\tfrac32\Delta_+^{(N)}=\frac{9}{32N}+\frac{\sqrt2\,(-2N^4+172N^2-791)}{6144\,N^{3/2}}\,\beta^{-1/2}+O(N\beta^{-1}),\qquad
\frac{\Delta_-}{\Delta_+}=\frac32+\frac{9}{32\sqrt{2N\beta}}+\cdots$$
(decoded from [CANON] §8.1–8.2; the $\beta^{-1/2}$ refinement inherits the conjectural status of $c_1^{(N),\pm}$ per [GCSG]).

**Rank nonuniformity [PROVEN as scaling statement].** $c_0=O(N)$, $c_1=O(N^{5/2})$ relative to leading gap $O(\sqrt{\beta/N})$: a hierarchy uniform in rank needs $\beta\gg N^3$. Fixed-rank series must not be inserted into 't Hooft scaling $\beta\propto N^2$. Under $\beta=N^3\tau$: $\Delta_+/N\sim\sqrt{2\tau}-\tfrac18-\tfrac{3\sqrt2}{512\sqrt\tau}$, $\Delta_-/N\sim3\sqrt{\tau/2}-\tfrac3{16}-\tfrac{7\sqrt2}{768\sqrt\tau}$, ratio $\to\tfrac32-\tfrac{1}{3072\,\tau}$ [CONJECTURE — remainder not controlled jointly in $N,\beta$; the $1/(3072\tau)$ coefficient was re-derived analytically in this consolidation and confirms the printed value]. [CANON] §8.3, App. A.

**Obstruction results (why this route stalls).** (i) *Fixed-shell radial certificate threshold* [PROVEN for the contracted radial class]: homogeneous shell of degree $\ell$ shifts the Laguerre parameter $\alpha^{\rm Lag}_N\mapsto\alpha^{\rm Lag}_N+\ell$; Gauss–Laguerre positivity forces certificate degree $m\ge(c_*+o(1))N^2$ with $c_*=\frac{(\pi-2)^2}{8\pi}=0.0518540247906\ldots$, universally in the shell; target coefficient $-0.2569486231\ldots N$ (the printed $-0.363N$ is an arithmetic error, [SUPERSEDED]). [CANON] §14. (ii) *Radial-tail no-go* [PROVEN]: the four-channel leakage matrix has characteristic polynomial $\lambda^4-\frac{215}{768}\lambda^2-\frac{175}{13824}\lambda+\frac{25}{294912}$, Perron root $\rho_3=0.5501615335231425806844\ldots$; the finite-channel diagnostic $\beta>\frac32\mu_G^4\rho_3^2$ ($=36.78\ldots$ at $\mu_G=3$) canNOT be promoted to a full-channel constant: one-resolvent Laguerre off-diagonals grow $\sim n^2$ against the available denominators ($p=1$ tail row sum $\to\frac{5}{32}\neq0$); decay needs denominator power $p>1$. The quadratically regularized $K_2$ has Hilbert–Schmidt tail but is not the physical transfer. [CANON] §15 [PROVEN diagnostic structure].

### 6.2 Layer III: seam analyticity (strong/weak crossover) [NUMERICAL/CERTIFIED]

For the complex-symmetric pencil $H(\beta)$ on SU(3) class functions: vacuum–gap exceptional point at $\beta_c=0.797842828512+1.389351779364i$, $|\beta_c|=1.6021$ (Kantorovich-certified at the recorded truncation, residuals $\sim10^{-16}$); second even EP at $-2.274880566451+0.838479039787i$, $|\cdot|=2.4245$. Structure theorem: with $S=E_0+E_1$, $G=O_0-S/2$, $G$ is analytic on $|\beta|<2.4245$ and $\Delta_-=G+\tfrac12\Delta_+$ — the odd tower's radius is inherited from the even vacuum EP; $(\Delta_+)^2$ converges on $|\beta|<2.4245$. Certified two-sector crossover v1 residuals: $3.3\times10^{-2}$ / $1.3\times10^{-2}$ / $1.9\times10^{-2}$; weak identity $G\sim\sqrt{2\beta/3}-\frac{7}{32}-\frac{127\sqrt6}{55296}\beta^{-1/2}-\frac{7903}{221184}\beta^{-1}$. [GCSG] §5. Consequence for the spine: the strong-coupling series of §4 has a finite convergence disk governed by a certifiable EP atlas — "consistent, not controlled" as a continuum statement.

### 6.3 Mobility theory: circuits, cells, and the pentagonal counterexample

**Theorem 6.4 (Weighted cellular-circuit lower bound; [PROVEN]).** Let $w_{\min}$ be the minimum $\ell_1$-weight of a primitive nontrivial integer dependency of $B_2$ compatible with the endpoint sector. Every reduced connected order-$r$ process satisfies $r\ge w_{\min}-2$. Proof: the reduced history supplies $x\in\ker_{\mathbb Z}B_2$ with $\|x\|_1\le r+2$. For a regular $F$-face cell with unit incidences and no smaller relevant circuit, $r_{\rm allowed}=F-2$. Circuit completion is necessary, **not sufficient**: Haar, resolvent, linked, symmetry, and compression survival are separate gates. Center (mod-$N$) circuits weaken the balance to $B_2x\equiv0\ (\mathrm{mod}\ N)$ and can appear earlier without being physical. [MOB] §2.

**Certified cell geometry** ([MOB] §§3–6; CPU certificate 26/26 gates):

| Cell | $F$ | $F-2$ | exact geometric compression |
|---|---|---|---|
| Tetrahedron (two glued) | 4 | 2 | eigenvalues $-18/5,\ -2$; spread $8/5$ |
| Triangular prism | 5 | 3 | dual-honeycomb bands $\mu_\pm(k)=-1\pm|1+e^{ik_x}+e^{ik_y}|$ + two harmonic modes at $\mu=2$; spread 6 |
| Cube | 6 | 4 | $P_ZH_{\rm cube}P_Z=A(C_L)$: $\mu=2\cos k_z$; spread 4 |

All-volume prism identities: $\ker B_\square\cong\ker D_1\otimes\mathrm{span}\{\mathbf 1_z\}$, $\dim=2L^2+1$; $S_\square+4I=B_\square^\dagger B_\square$; second order exactly flat on cycles ($H^{(2)}_{\rm shape}=a_2I+t_NS_\square$); third-order cell operator $H_{\rm cell}=(2I-D_2D_2^\dagger)\otimes I_z$ — harmonic $\mathcal H_1(T^2)$ flat at $2$, boundary cycles disperse. Local coefficients: $c_3(N)=\frac{64}{N(N^2-1)^2}$ ($c_3(3)=\tfrac13$; prism third-order bandwidth $\Delta_3(N)=\frac{384}{N(N^2-1)^2}$, $\Delta_3(3)=2$); cube $c_4^{\square}(N)=-\frac{160}{N(N^2-1)^3}$. Tetrahedral local SU(N) coefficient: **open in [MOB]** (2026-08-19); [FINAL] (2026-08-20) tabulates it as $-\frac{8}{N(N^2-1)}$ within a "certified sequence" — artifact absent, [RECORD-BACKED], and in tension with [MOB] one day earlier; see contradiction C15.

**Primitive cell-completion coefficient law** ([FINAL] §3 [RECORD-BACKED as general law; instances at $r=3,4$ certified elsewhere]):
$$c_{r,\rm prim}(N)=\frac{2^{r-1}S_r}{N(N^2-1)^{r-1}}\sim N^{-(2r-1)},\qquad C_F=\frac{N^2-1}{2N},$$
with $(r,S_r)$: tetra $(2,4)\to-8/[N(N^2-1)]$; prism $(3,16)\to64/[N(N^2-1)^2]$; cube $(4,20)\to-160/[N(N^2-1)^3]$; pentagonal prism $(5,70)\to1120/[N(N^2-1)^4]$, i.e. $c_{5,\rm prim}(3)=35/384$ (arithmetic of all four instances re-verified).

**The pentagonal counterexample ([FINAL] §§1,4; [GLUE2] §13.1; computational frontier [PENT]/[AUD]).**
The pentagonal prism's primitive relation $-c_0+c_1+s_0+s_1+s_2+s_3+s_4=0$ has $\ell_1$-weight 7, so the primitive cell-completion channel needs $r=5$. But the isotropic prism splits caps from sides electrically: $E_{\rm cap}=\frac{10}{3}$, $E_{\rm side}=\frac83$ (5-link vs 4-link loops at $\tfrac23$/link — re-verified), so the physical degenerate band is the cap band, and:
$$h_4^{\rm side}=-\frac{2861009}{84387303000},\qquad
\tau_4=5h_4^{\rm side}=-\frac{2861009}{16877460600},\qquad
\delta E^{(4)}_{\rm cap}(k)=2\tau_4u^4\cos k=-\frac{2861009}{8438730300}u^4\cos k,\qquad r_{\rm hop}^{\rm iso,cap}=4 .$$
Status: [GLUE2] calls this "cold-certified (dual-cold)… separate model"; the primary run artifacts are **not in this corpus** → corpus-level [RECORD-BACKED]; internal ratios re-verified. What *is* in-corpus: [PENT] closes the raw frontier exactly (20 histories in two temporal multisets 10+10; raw cut spaces $4,10,20$ with Gram ranks $4,6,6$; balanced sectors $(1,1),(2,2),(3,3)$; SU(3) $(4,1)$ delta-epsilon sector rank 3 with alternating null relation $[-1,1,-1,1]$; all 20 bare endpoint Haar contractions $=1$; 8/8 gates; SHA-256 `83c0aa7c…`), and [AUD] **falsifies** the claimed "stranded-flux zero backend" (every rejection came from balanced $(2,2)$ links; exact $\mathrm{Wg}(e)=\tfrac18$, $\mathrm{Wg}((12))=-\tfrac1{24}$, $\int|U_{11}|^4=\tfrac16\neq0$; verdict ZERO_BACKEND_FALSIFIED, 8/8). The remaining in-corpus gap to $h_4^{\rm side}$: Fierz closure of each cut space (including the $(4,1)/(1,4)$ sector), Gram-null quotient, physical resolvents $R_k=Q(E_0G_k-H_{0,k})^{-1}Q$ — precisely the "decisive next calculation" of [STRONG].

**Consequences** ([FINAL] §4; adopted with the above caveats): the bound $r\ge w_{\min}-2$ stands for the reduced nontrivial integral circuit; the *promotion* $r_{\rm physical}=w_{\min}-2$ is **false** (pentagonal cap moves at 4, not 5). Statically-cancelling but temporally nontrivial histories carry amplitude: $A_N[h]\neq A_N[\pi(h)]$ ([GLUE3] §12 states this as the existence theorem $\exists h_1,h_2:\pi(h_1)=\pi(h_2),\ \mathcal A_N[h_1]\neq\mathcal A_N[h_2]$). The deeper law is claimed to be: surviving temporal order $r$ ⇒ coefficient $\sim N^{-(2r-1)}$, supported by an exact fixed-side backend at $N=3..12$, a blind $N=13$ run (20/20 gates), and a log-log slope $-7.0021$ over $N=7..13$ — all [RECORD-BACKED], artifacts absent. [GLUE3] §12 scopes the coefficient law itself: $c_{r,\rm prim}$ is the archived color-counting law of a *restricted primitive simple-loop channel*; "not a universal formula for complete order-$r$ amplitudes: folded terms, determinant sectors, and temporally distinct histories can alter the full coefficient."

**Mobility-order taxonomy** ([GLUE3] §12 — new; adopt as canonical refinements of D4):
$$r_{\rm split}=\min\{r:H^{(r)}_{\rm eff}(0)\ \text{has non-scalar internal splitting}\},\quad
r_{\rm off}=\min\{r:H^{(r)}_{\rm eff}(R)\neq0,\ \exists R\neq0\},\quad
r_{\rm mob}=\min\{r:\operatorname{spec}H^{(\le r)}_{\rm eff}(k)\ \text{nonconstant in }k\},$$
with $r_{\rm off}\le r_{\rm mob}$ generally, and onsite splitting possible without mobility. (The pentagonal discussion above concerns $r_{\rm off}/r_{\rm mob}$ of the cap sector.)

**Linked-cluster subtraction rule** ([GLUE3] §12 — the discipline behind [RUN15]'s oracle and adjudication item (4) of §5.5): $H_{\rm eff}$ is **not** cluster additive; $H_{\rm eff}-eI$ **is**. Subcluster (Möbius) subtraction must be applied to the vacuum-subtracted operator or gap, never to raw $H_{\rm eff}$.

**Fifth order, SU(3), pentagonal-channel representation theory** ([FINAL] §6; [STRONG]): local census $14^5=537{,}824\to1030=120_{\mathbb Z}+910_{\mathbb Z_3\setminus\mathbb Z}$; the 910 modular histories collapse to 14 oriented-face lifts, then $910=338_{\rm direct}+572_{\rm folded/return}$ (19/19-gate certificate — [RECORD-BACKED]). The 110 direct triple-side determinant histories contribute exactly
$$\delta c_{5,\det}^{SU(3)}=\frac{235424477177}{407461473619200}\approx5.77783\times10^{-4},\qquad
c_{5,\rm direct}^{SU(3)}=\frac{35}{384}+\delta c_5=\frac{37373840041427}{407461473619200}=0.0917236167372\ldots$$
(sum re-verified exactly). This **falsifies** "center-only circuits are dynamically dark": unequal electric denominators destroy raw Haar cancellation. The *full* fifth-order pentagonal coefficient remains open (572 folded/return histories need the support-resolved fold before rooted subtraction).

### 6.4 Fifth order, SU(3) cubic band; string tension; ratio [OUTPUT-CERTIFIED, inheriting §5.5's dispute]

Same two-invariant form as fourth order ([T1PM] §9; subscripts = coupling order here):
$$c_5(k)=q_5+\frac{A_5\mathsf Q+B_5\mathsf R}{2\mathsf S},\qquad
q_5=m_5=-\frac{866236750503342026253096691057}{1169668083793811403447133488000}\approx-0.740583386437,$$
$$A_5=\frac{313}{240},\qquad B_5=\frac{1881863087742908605903793}{1652932248975967181040000},\qquad
\Delta c_5=A_5+B_5=\frac{4037562229115732471176793}{1652932248975967181040000}\approx2.442666498652 .$$
Anchors: $c_X=\frac{659205375444420345742539899543}{1169668083793811403447133488000}$, $c_M=\frac{13250388338835740713398569140103}{11696680837938114034471334880000}$, $c_R=\frac{475012476694676416524425923}{279077133945841621360740000}$; gates $c_R=2c_M-c_X$, $A_5=c_X-q_5$, $B_5=c_R-c_X$ all re-verified exactly here. Both shape coefficients are $O(1)$: the band is no longer approximately flat at fifth order. Census: 6,676,658 connected supports; 39,368,491 support/output pairs; 1,280 triality classes; 29,366 canonical words; 116,571 C-orbits; 574 signatures; 1,624 fusion paths; 22,071 wiring topologies; 524,823 contractions; 189 kernel records; new sectors $(4,1)$, $(5,2)$. **Caveat:** produced by the same source-chain family as the historical fourth-order kernel; while [T1PM] reports independent cold reproduction of the fifth-order arithmetic, the §5.5 scalar-coordinate dispute propagates to $q_5$'s physical identification.

**Rest-mass series (historical-kernel coordinate; both $u^4$ and $u^5$ terms conditional per §5.5):**
$$m_{1^{+-}}(u)=\frac83+u+\frac{11}{306}u^2-\frac{109151}{249696}u^3-\frac{20721577909065127111}{7250590288602460800}u^4-\frac{866236750503342026253096691057}{1169668083793811403447133488000}u^5+O(u^6).$$

**String tension (project-native through $u^4$; $s_2,s_3$ mechanism in-corpus via [V10A26] v9, $\sigma_4$ [RECORD-BACKED] per [T1PM] provenance note — torelon engine runs with $L=4/L=5$ length-independence, artifacts absent here):**
$$\sigma(u)=\frac23-\frac{22}{153}u^2-\frac{61}{408}u^3-\frac{737327120374220449}{7250590288602460800}u^4+O(u^5).$$
The $O(u^3)$ mechanism is fully derived in [V10A26] v9: extensive linked winding-string process $E_3^{\rm raw}/L=-65/51$ plus vacuum coefficient $e_{\rm vac,3}=-9/32$ with four incident plaquettes per bulk link: $s_3=-\frac{65}{51}-4(-\frac9{32})=-\frac{61}{408}$ (re-verified). **Sign correction:** earlier notes carried $+61/408$; the direct network gives $-61/408$, matching the published Hamiltonian series converted with the bridge $\sigma(u)=\tfrac12W(2u)$ — the alternative $\tfrac12W(-2y)$ convention flips odd orders and is a convention error [SUPERSEDED]. Fifth/sixth-order tension: exact **historical KPS targets**, not native reruns: $\sigma_5=-\frac{137767222189182735950309}{2009803206414863779920000}$.

**Scale-matched ratio ([T1PM] §9.4; series division re-verified exactly in this consolidation):**
$$\frac{m_{1^{+-}}(u)}{\sqrt{\sigma(u)}}=\sqrt6\sum_{n=0}^5c_nu^n+O(u^6):\quad
c_0=\frac43,\ c_1=\frac12,\ c_2=\frac{11}{68},\ c_3=-\frac{7559}{499392},$$
$$c_4=-\frac{15752822901180179}{12642703205932800},\qquad
c_5=-\frac{10670728893034386567182468628311}{46786723351752456137885339520000}\approx-0.228072\ (\sqrt6c_5\approx-0.558659).$$
$c_0$–$c_3$ depend only on undisputed inputs; $c_4,c_5$ inherit the §5.5 dispute and the KPS-target status of $\sigma_5$. No continuum extrapolation is controlled: available Borel–Padé estimates are "consistent, not controlled" ([GCSG] §4.11.4); reference continuum value (replay-verified transcription) $M(1^{+-})/\sqrt\sigma=6.065(40)$ [Athenodorou–Teper].

### 6.5 Sixth order: state of $m_6$ [OPEN; two components pre-cleared]

$q_6=m_6=\tfrac13\mathrm{tr}H_6(0)$ is the highest-value open coefficient; $c_6=\frac{m_6}{2}+\frac{1181646977233006828729169209802562361069278851250351799}{168641444007491247688836385300053017225944999004544000000}$. Pre-cleared: (1) folded/des-Cloizeaux weights at six insertions (32 denominator patterns, reversal symmetry, resolvent-product limit, 4 rational regressions — all pass); (2) local carrier census: $3^8-1=6560$ signatures → 2,186 feasible spanning $(0,3),(0,6),(1,1),(1,4),(1,7),(2,2),(2,5),(3,3),(4,4)$; fusion-path basis nonempty for every record (max singlet multiplicity 23, max intermediate irrep dim 27). Open: global geometry census + contraction (recommended external-memory sharded architecture). [T1PM] §9.5, §12.

### 6.6 Hodge duality, hedgehog, and Maxwell equivalence [PROVEN]

Centered gauge $M(k)=2[s\text{-matrix}]$, Hodge rotation $J(z_{12},z_{13},z_{23})=(z_{23},-z_{13},z_{12})$: $JM=-2[s]_\times$, $M^\dagger M=JMM^\dagger J^T=4(|s|^2I-ss^T)$ — face and link sectors are *the same* transverse lattice-Maxwell operator; kernels are one longitudinal line $\mathrm{span}\{s\}$; the longitudinal projector $P_L=ss^T/|s|^2$ has a direction-dependent limit at $\Gamma$ with dipolar tail $\sim(\delta_{ij}-3\hat r_i\hat r_j)/4\pi r^3$ — no complete exponentially localized basis removes it. Unit embedded hedgehog $S^2\to\mathbb{RP}^2$ of degree 1; **fragile**: one trivial orbital enlarges the target to $\mathbb{RP}^3$, $\pi_2(\mathbb{RP}^3)=0$ — not a stable BDI invariant [SUPERSEDED reading excluded]. Kernel–resolvent duality: $(m^2I+\alpha D^*D)^{-1}_{\mu\nu}(p)=\frac{\delta_{\mu\nu}+(\alpha/m^2)h_\mu h_\nu}{m^2+\alpha\hat p^2}$, $h_\mu=e^{ip_\mu}-1$. [CANON] §11, [GCSG] §4.2, Law 2.

### 6.7 Layer V: toward infinite volume — the conditional scaffold

**No-go [PROVEN]:** for Bernoulli plaquette defects of fixed density, $\|P\,1_{C(D_L)}P\|\to1$ in probability as $L\to\infty$ (rare fully-defective boxes): every *global fixed-window firewall* is false. [CANON] §16.3.
**Rooted replacement [CONDITIONAL]:** source-tilt identity $\mathbb E_{\beta,L}\exp(t\sum_{p\in\Gamma}V_p)=Z_{\beta,t,\Gamma,L}/Z_{\beta,L}$ [PROVEN]; Peierls $P(\Gamma\subset D_\delta)\le z^{|\Gamma|}$, $z=K_\alpha e^{-(1-\alpha)\beta\delta}$, conditional on the **open** inhomogeneous free-energy bound $Z_{\beta,\alpha,\Gamma,L}/Z_{\beta,L}\le K_\alpha^{|\Gamma|}$ (PC-2); square-free Wilson-to-Bernoulli domination [PROVEN]; rooted marked partition sums uniformly bounded when $C_*=\mu_P K_\alpha e^{-(1-\alpha)\beta\delta+a+s\gamma}<1$, i.e. $\beta>\frac{\log\mu_P+\log K_\alpha+a+s\gamma}{(1-\alpha)\delta}$ [PROVEN implication]. Converting rooted capacity into stability of a projected Maxwell/Birman–Schwinger source needs the **open** source-radius reduction. PMBSF SU(2) conditional stack: reduction chain proven; named open analytic inputs LCIgood + BFSfar (+ SWB, BBG). [CANON] §16; [GCSG] §7, Law 5. **These two named hypotheses (PC-2 and source-radius; alternatively LCIgood+BFSfar) are the corpus's entire unproven interface to infinite volume.**

**Transfer geometry [PROVEN/CERTIFIED]:** Wilson–Bergman weight $w_\lambda(\beta)$ is a Bessel–Toeplitz determinant; $\|M_q\|=(2N)^k$ with truncation deficit $\asymp C/K^2$ (the earlier "N-uniform $\|M_q/q(1)\|=1$" claim is Withdrawn); rank-1/2 Bergman transfer closes the radial tail with no $n^2$ growth. [GCSG] §6.

### 6.8 Exploratory prediction: hyperhoneycomb $O(u)$ transition [CONJECTURE]

From the Illa–Savage–Yao loop set: reconstructed loop-edge incidence has $\operatorname{rank}B=10$, $\dim\ker B=2$, primitive relations $-10f+10h+12c=0$ and $-10e+10g+12d=0$; 10-link endpoints electrically degenerate; the 12-link insertion shares one connected oppositely-oriented path of length six ⇒ candidate $O(u)$ transition in a degenerate Wilson-loop sector. Not yet dynamical (Haar normalization, retained sector, compressed operator uncomputed). [FINAL] §11 [RECORD-BACKED reconstruction + CONJECTURE]. If confirmed, extends the framework from cell faces to arbitrary degenerate Wilson-loop incidence complexes.

### 6.9 Related literature (as recorded in-corpus; not independently re-searched here)

Strong-coupling effective Hamiltonians and glueball series: Münster (1985); Hamer–Irving–Preece (1986); linked-cluster methods standard. Noncubic KS Hamiltonians: Illa–Savage–Yao (arXiv:2503.09688). Higher-form/center-sheet transfer-matrix masses: Bao (arXiv:2608.02452). Flat-band classification: Rhim–Yang; Bergman–Wu–Balents. The corpus's own novelty assessment ([FINAL] §10): the new content is the *quotient-and-escape mechanism and its exact cellular/operator realizations*, not strong-coupling perturbation theory itself; a dedicated literature review is still required before any priority claim.

---

## 7. Part V — Unified evidence section (all computations in one place)

Format per entry: *what it tests → what it found → agreement → error/tolerance*. "In-corpus" means log or artifact is in this corpus; otherwise the run is cited from a document and is [RECORD-BACKED].

### 7.1 The 15-hour v10a.26 A100 run (in-corpus: [RUN15]; engine [V10A26])

*Tests:* the SU(3) fourth-order one-flux problem end-to-end without loading any disputed target: exact degenerate-fold (des-Cloizeaux/SW) operator formula $H_4=D-a(C_1+C_1^T)-\tfrac12\{K_2,N\}+a^2J$ regression-proved on exact dim-2 models; physical $PVP=aP$ *computed* (found $=+I$ exactly, lift error $2.2\times10^{-16}$); full-$T_1$ operator moments $K_2,N,J,C_1,D$ with factorized SU(3) Haar (incl. exact rank-3 $(4,1)$ and rank-11 $(5,2)/(2,5)$ determinant projectors; 11 singlets; every center-admissible $O(u^4)$ local pattern covered); independent rooted finite-cluster linked-gap oracle (33 rooted proper-rotation shape classes, 203 concrete clusters, exact-SW coefficients, rooted incidence/Möbius subtraction).
*Found:* 86/86 gates PASS. Lower orders cold: $m_1=1$, $m_2=0.03594771241824929=11/306$, $m_3=-0.4371355568371267=-109151/249696$. Vacuum sector exact: one-face $e_2=-\tfrac34$, $e_3=\sigma_3=-\tfrac9{32}$, $N=\tfrac9{32}$, $D=-\tfrac{309}{1280}$, $e_4=-\tfrac{39}{1280}$; adjacent pairs (coplanar and perpendicular identical) $e_4(C)=-\tfrac{54321}{837760}$, $\omega_4=-\tfrac{327}{83776}$; embeddings 13 (one-face) + 124 (pairs: 80 perp, 44 coplanar); linked vacuum $O(u^4)$ subtraction $-\tfrac{1474623}{1675520}=-0.8800987156226097$. Support census: W1/R1/W2/R2 $=13/13/171/171$ per polarization; no $E_0$ poles (residual $8.9\times10^{-16}$). Unblind: independent linked $m_4=-0.7751458630189173$; folded $C_{\rm shape}=-0.020213328886166577$; kernel = 189 anchored records with $A=5/48$, $B\approx0$, $D\approx0$, $\alpha=5/12$ (residuals $\le2.5\times10^{-13}$), Γ-rest = cluster oracle to $2.0\times10^{-15}$.
*Agreement:* protected invariants match the historical kernel exactly; rest scalar and $C$ do **not** (§5.5); "quarantined scalar shortcut" $-11.068479463778765$ rejected. *Caveat on gate 85* ([GLUE3] §9.2): the final mass-kernel Γ-rest equals the cluster oracle **by construction** — the applied diagonal shift $+11.17343231638178$ was target-derived from the raw folded rest value; the independent content of the run is the oracle's own $m_\Gamma^{(4)}$ (computed blind) plus the folded $C_{\rm shape}$, not that equality.
*Verdict (verbatim):* "MIXED/THIRD RESULT — DO NOT PROMOTE EITHER FOURTH-ORDER CLAIM."
*Tolerances:* exact rational where stated; float pipeline residuals $10^{-13}$–$10^{-17}$; exact-SW vs retired one-face fit $2.267\times10^{-7}$ (fit is audit-only).

### 7.2 Stranded-flux zero-backend audit (in-corpus: [AUD])

*Tests:* the claim that all 20 pentagonal $O(u^4)$ fixed-side histories have zero SU(3) endpoint Haar contraction ("stranded flux").
*Found:* every backend rejection traced to two balanced $(2,2)$ links; exact $\mathrm{Wg}(e)=1/8$, $\mathrm{Wg}((12))=-1/24$, $\int|U_{11}|^4=1/6\neq0$; all 20 complete six-trace endpoint networks contract to exactly 1. 8/8 checks. *Verdict:* ZERO_BACKEND_FALSIFIED. *Boundary:* does not compute resolvents or $h_4^{\rm side}$.

### 7.3 Pentagonal O(4) minimal-representation frontier (in-corpus: [PENT])

*Tests:* the exact raw prefix-overlap structure of the 20 cap-irreducible histories.
*Found:* 20 histories in two temporal multisets (10+10); raw cut dims/ranks $(4,4),(10,6),(20,6)$; raw sectors exactly $(1,1),(2,2),(3,3)$ with balanced Gram ranks $1,2,6$ and exact Weingarten blocks (p=3 block: $7/120$, $-1/40$, $1/60$ pattern); $(4,1)$ delta-epsilon raw Gram rank 3, null relation $[-1,1,-1,1]$; all bare endpoint contractions $=1$. 8/8 gates; SHA-256 `83c0aa7c4924b5707361b0c7ce43eaa3050ab8392a728c3a8f4d9cf7dd9ca7c1`. *No $h_4^{\rm side}$ imported or computed.* Remaining object stated explicitly (Fierz closure → Gram quotient → $R_k$).

### 7.4 Marked-cluster adjudication engine (in-corpus: [MCE]; no run)

Target-blind Phase-3 engine with sealed 93-face patch, three rotated 203-support closures, Redelmeier rooted-support streaming, 609-evaluation preflight ("PASS_609_NO_PHYSICS" path), HMAC-sealed resume, and a seal that refuses legacy/synthetic data. Status constants: "PHASE3_TRIALITY_CANDIDATE_SWEEP_READY_NOT_YET_EVALUATED". [GLUE3] §18.1 confirms: "the exact marked-cluster engine currently passes its cheap algebra and geometry preflights, but it has not produced a full physics certificate." **No m4 seal exists in this corpus.** This is the designated decider for §5.5, now under the 11-item frozen protocol.

### 7.5 Compact-regime computational certificates (in-corpus: [CANON] §17; [GCSG] §8)

- Odd-sector exact-arithmetic certificate, $N=3..12$: four identity assertions per rank (table printed; e.g. $N=3$: $c_{0,-}=-3/8$, $q_{H_2,-}=65/1728$, $q_{\rm res,-}=-119/1536$, $q_-=-551/13824$). [CERTIFIED]
- Compact Peter–Weyl character diagonalization: $K$-cutoff-stable gap (e.g. 45.8740440690 at $\beta=3200$ from $K=65$ on); residual after three-term law $\approx-0.052\cdot\beta^{-1}$; degree-4 fit returns $c_0^{\rm fit}=-0.3125000$ vs exact $-5/16$, $c_1^{\rm fit}=-0.0826591$ vs exact $-0.082659647$; odd audit selects $-53/864$ over superseded $-1781/55296$. [CERTIFIED]
- Weyl-triangle GPU solver: independent normalization/boundary audit; no CUDA execution certificate in corpus (AUD-4 open). [NUMERICAL]

### 7.6 Runs cited by the audit notes but absent from this corpus ([RECORD-BACKED]; arithmetic re-verified where possible)

- SU(3) second-order certificate 35/35 gates; third-order 251/251 gates ([STRONG] "fresh reproduction"). Coefficients independently confirmed by [RUN15] → effective status of the *values*: cold-certified.
- Fourth-order SOS reproduction for the 189-record kernel; all-rank symbolic rerun blocked by incomplete input bundle ([STRONG]).
- Pentagonal $O(u^4)$ triple implementation of $h_4^{\rm side}$; 28 proper-return histories vanish; periodic operator audit ([FINAL] §4; [GLUE2] §13.1 "dual-cold").
- Generic backend $N=3..12$ all nonzero same-sign; blind $N=13$ 20/20 gates; log-log slope $-7.0021$ ([FINAL] §5).
- Pentagonal $O(5)$: oriented-face certificate 19/19; $910=338+572$; $\delta c_{5,\det}$ ([FINAL] §6; sum re-verified exactly).
- Mixed tetrahedron–octahedron certificate 12/12 gates, non-scalar $O(u^2)$ residue, eigenvalue separation $32/31$ ([FINAL] §3).
- Cellular-circuit CPU certificate 26/26 gates (`hodge_circuit_mobility_certificate.py`, described with artifact SHAs in [MOB] §9 — script itself not in corpus).
- [T1PM] source-chain: Stage 0–3J complete; stable-rank Stage-3G (147 self-tests incl. $\mathbb E|\mathrm{Tr}U|^2=1$, $|\mathrm{Tr}U|^4=2$, $|\mathrm{Tr}U|^6=6$); $N=7,8$ full-kernel reruns match; $B_N$ fixed-rank holdout ledger for $N=7..18$ open (v0.7 overclaim corrected in v0.8 §11).
- SU(4) hybrid completion certificate (4,171 words; 35,130 paths; 156 exceptional C-orbits; all-zone zero residual; source SHA `8feec874aa16c823bb837efa8df626d5cf735db5ecaa6c90b8806ddf456b51a5`) — reproduced in [GCSG] App. B.

### 7.7 Monte Carlo / physics contact ([GCSG] §8; [GLUE3] §14 — which downgrades the record's reproducibility class; [NUMERICAL])

- Replay gate: Athenodorou–Teper $T_1^{+-}$ table digit-faithful (25/25 cells); continuum $M(1^{+-})/\sqrt\sigma=6.065(40)\approx2.944(42)$ GeV.
- Like-for-like matched MC, stored record `next14.json` ([GLUE3] §14): $\beta=5.8941$, $L=14$, $N_t=16$, 2000 configurations; $aM(T_1^{+-})=1.6897344913\pm0.1206114757$ vs published $1.591(18)$ — pull $+0.82$; $a\sqrt\sigma=0.2628289891\pm0.0023244282$ (string scale $+0.71\sigma$).
- **Overlap measurement:** raw single-plaquette $\mathrm{Im\,Tr}$ fitted fraction $0.0072359730\pm0.0164694235$ ($<4\%$ at $2\sigma$); smeared amplitude $0.7996986994$. The physical $T_1^{+-}$ state is extended; the one-plaquette result is an operator/geometry seed. This is the measured fact behind the load-bearing step §2.3(b).
- **Reproducibility downgrade** ([GLUE3] §14 — controls): the JSON records 23/23 gates passing, but one "physical zero-momentum carrier" gate is a **literal truth value in the source**, not a computed test; the JSON is not source-hash bound, contains non-RFC `NaN` tokens, and no raw August ensemble/checkpoint was found. Status: *structured finite-volume numerical evidence, not a cold-reproducible ensemble certificate*. A publishable reanalysis must store raw/block observables, bind outputs to source+inputs, jointly bootstrap longitudinal/transverse channels, and propagate the $a^2\sigma$–$M/\sqrt\sigma$ covariance.

---

## 8. Part VI — Contradiction register (complete, with both numbers)

C1. **Fourth-order rest scalar.** $-\frac{20721577909065127111}{7250590288602460800}=-2.857915988114559$ [T1PM]/[GCSG] vs $-0.7751458630189173$ [RUN15]/[GLUE3] (Hamer $8a_4=-0.7751458630184$, agreement $5.2\times10^{-13}$ — but $a_4$ is an unverified notebook transcription, [GLUE3] §2.3) vs quarantined $-11.068479463778765$ [RUN15]. $\Delta_\Gamma=2.0827701250956414$. [GLUE3] firewall: re-anchoring is a *same-kernel* identity; "old kernel = new kernel + scalar" is **Not established**; the run's applied $+11.17343231638178$ shift was target-derived. One concrete reconciliation hypothesis is queued for test: $q_{\rm band}^{(4)}-E_0^{(4)}\stackrel{?}{=}m_\Gamma^{(4)}$ (adjudication item 9). **Open; do not promote either** ([RUN15] verdict; [GLUE3] §17). §5.5.

C2. **Fourth-order off-axis coefficient.** $C_{\rm old}=-\frac{211835444920651}{4405310420659200}=-0.04808638318135875$ vs $C_{\rm new}=-0.020213328886166577$; $\Delta_C=0.027873054295192174$; identity shift cannot reconcile ($\Delta\varepsilon_4(M)=8\Delta_C$, $\Delta\varepsilon_4(R)=16\Delta_C$; axial cuts agree). **Open.** §5.5.

C3. **Status of the fourth-order "theorem."** [T1PM] §13: "proved" (June 14) vs [GCSG] §4.11: "exact-arithmetic computational ledger — audit pending; six closure gates" (Aug 8) vs [RUN15]/[GLUE2]/[STRONG]: mixed/do-not-promote (Aug 19–20). Resolution by precedence: the newest status controls; the *values* of §5.2 are sealed, the rest is C1/C2.

C4. **Coupling conventions.** $u=\beta/6$ vs the archived $Y=2\beta/3=4u$ line vs paper's $y:=u$. [GLUE3] §2.2 resolves the archived case: the $Y$ line was a **definition/label error** — the printed coefficients were already in $u$; corrected sources relabeled without rescaling; never apply $4^n$ factors to them. Registry in §1.1; the separate [GCSG] magnetic-prefactor gate for the Aug-8 *simulation tower* remains conditional.

C5. **String-tension sign at $O(u^3)$.** Earlier $+61/408$ vs derived $-61/408$ ([V10A26] v9 direct network; conversion $\sigma=\tfrac12W(2u)$). The $\tfrac12W(-2y)$ artifact's positive $\sigma_5$-order sign convention is a convention error at odd orders. Resolved: $-61/408$ [SUPERSEDED the $+$].

C6. **"$F-2$" mobility rule.** Scoped bound $r\ge w_{\min}-2$ [PROVEN, [MOB]] vs promotion $r_{\rm physical}=w_{\min}-2$ — falsified by the pentagonal isotropic cap hop at $r=4$ with $w_{\min}-2=5$ ([FINAL]; underlying runs record-backed). Resolved in favor of the scoped bound + survival gates.

C7. **Stranded-flux zero backend.** Claimed Haar zero for all 20 pentagonal histories vs exact nonzero Weingarten/network contractions. **Falsified in-corpus** ([AUD], 8/8).

C8. **Pentagonal degenerate space.** Older cap+side Bloch compression (valid geometric identity) vs isotropic physics: $E_{\rm cap}=\frac{10}{3}\neq E_{\rm side}=\frac83$ — one-band treatment corresponds to an anisotropically tuned Hamiltonian. Resolved: choose the physical degenerate eigenspace first ([FINAL] §1).

C9. **SU(4) exceptional correction.** "Scalar matrix $\Delta q_4I_3$" vs certified flat-branch eigenvalue identity $H^{\rm exc}_{4,4}\psi=\Delta q_4\psi$ only. Resolved: the weaker statement ([CANON] §13.4, [GCSG] App. B).

C10. **Determinant sectors shift only $q_N$.** True $N\ge4$; false at SU(3) ($\Delta\beta_3=-\frac{25}{64}$, $\Delta q_3=-\frac{16863189551}{76406976000}$). Resolved with the rank split ([T1PM] §5.1).

C11. **Compact-gap constants.** Superseded: odd $c_0$ variant (garbled in [CANON]'s encoding; correct $-\frac{3(N^2-3)}{16N}$ confirmed in [GCSG]); radial moment difference $2N^2+1$ → correct $3N^2+1$; dilation $\varepsilon^4=2N/\beta$ → correct $N/(2\beta)$; radial-target $-0.363N$ → correct $-0.2569486231\ldots N$; odd $\beta^{-1}$ candidate $-1781/55296$ → correct $-53/864$.

C12. **Curvature misreads — two-stage correction.** Stage 1: $t^2$-coefficients quoted as curvatures ($\alpha/4$ etc.) → corrected to $\kappa=2a(n)$ ([GLUE2] §7.4). Stage 2 ([GLUE3] §7.3, controls): even the $\kappa$'s are *radial directional curvatures*, **not** Hessian entries at $\Gamma$ — a genuine Hessian requires $\beta=2\alpha$, violated by the historical kernel; at $R$ the Hessian is isotropic $-\frac{\alpha+\beta}{6}I$. The [GLUE2] label "Hessian curvatures" is [SUPERSEDED]; the numerical values are unchanged.

C13. **C-even second-order hopping.** $-481/612$ → $-11/306$ (vacuum-mediated route omitted; independent 2-plaquette diagonalization discriminates) ([PAPER] §7).

C14. **Betti "+2".** "Two accidental states"/property of dispersive branches → $b_2-b_3$; open box has no extra states ([PAPER] Table 1).

C15. **Tetrahedral local coefficient.** [MOB] (Aug 19): open, "cheapest high-value falsification test" vs [FINAL] (Aug 20): $-8/[N(N^2-1)]$ listed as certified. Artifact absent; formula equals the general $c_{r,\rm prim}$ law's $r=2$ instance. **Unresolved in-corpus; treat as [RECORD-BACKED].**

C16. **SU(5)/SU(6) fourth-order completeness.** [CANON] (Aug 1): "unresolved in the present controlling bundle" vs [GCSG] (Aug 8): promoted by the 2026-08-08 Layer-II authority (SU(5) scan empty over 895,524 pairs; $\Delta q_6=6/343$). Later document controls, but the machine-readable payloads are absent from this corpus → [RECORD-BACKED].

C17. **Fixed-rank holdout overclaim.** v0.7 "$q_N,A_N,B_N$ match for every $N=7..18$" → corrected v0.8 §11: $q_N$ matches stored values $7..18$; full kernels only at $N=7,8$; $A/B$ sample ledger open.

C18. **"Center-only circuits are dynamically dark."** Falsified by the exact fifth-order determinant correction $\delta c_{5,\det}\neq0$ ([STRONG]; record-backed run).

C19. **Global fixed-window firewall.** Asserted in older program → disproved (Bernoulli no-go, [CANON] §16.3 [PROVEN]); replaced by the rooted conditional calculus.

C20. **[RUN15] internal display artifact.** The linked vacuum subtraction line prints "rational~ $-521965902/593076541$" (a float-reconstruction) while the gate asserts $-1474623/1675520$; both equal $-0.88009871562\ldots$ to float precision. The gate value is the intended exact one. Cosmetic, noted for completeness.

C21. **Monte Carlo gate integrity.** `next14.json` reports 23/23 gates, but [GLUE3] §14 finds one "physical zero-momentum carrier" gate is a literal truth value in the source, the JSON is not source-hash bound (non-RFC `NaN` tokens), and no raw ensemble/checkpoint exists. [GCSG]'s "23/23 hard gates green" presentation is accordingly downgraded: the numbers stand as structured numerical evidence; the certificate claim does not. Resolved by [GLUE3] (newest audit).

C22. **Gate-85 equality.** [RUN15] gate 85 ("final physical mass-kernel Γ-rest equals independent cluster oracle", $2.0\times10^{-15}$) reads like an independent verification; [GLUE3] §9.2 discloses the final diagonal shift $+11.17343231638178$ was chosen to produce exactly that equality. Not a numerical contradiction — a status correction: the gate certifies internal bookkeeping, not independent agreement. Resolved by [GLUE3].

---

## 9. Part VII — Gap analysis: what remains to full rigor, ranked by difficulty

Ranked easiest → hardest within each block; "difficulty" reflects the corpus's own effort estimates plus dependency depth.

**Tier 0 — bookkeeping (days).**
G1. Ship/restore machine-readable payloads now only record-backed: SU(3) 189-record kernel with reference SHA; $Q_{32},P_{402}$ ledgers; SU(5)/SU(6) exceptional certificates; pentagonal $h_4$ run artifacts; tetrahedral-coefficient certificate (resolves C15, C16). 
G2. Regenerate all displayed tables in canonical $u$; single conversion statement (kills C4 residue).

**Tier 1 — decisive finite computations (weeks; architectures already specified).**
G3. **Fourth-order adjudication**: run [MCE] target-blind under the 11-item frozen protocol of [GLUE3] §18.1 (reproduced in §5.5): erratum-fixed normalization; occurrence schedule; $203\times3=609$ exact evaluations + rooted Möbius ledger; subtraction on the vacuum-subtracted object; sealed hashes; no historical targets; cold 3,895-topology Stage-3H unshifted 189-record kernel (never confuse with the 3,850 stable-rank inventory); $X/M$ fit with blind $R$ holdout then full Laurent equality; independent scalar ledger $q_{\rm band}^{(4)}-E_0^{(4)}\stackrel{?}{=}m_\Gamma^{(4)}$; $W_{22}$ toggle across 33 rooted classes; $m_\Gamma^{(4)}$ and $C^{(4)}$ from one run. Resolves C1–C3 and C22; unfreezes the $u^4$–$u^5$ mass series and ratio.
G4. Pentagonal $O(u^4)$ closure in-corpus: Fierz closure of the 20-history cut spaces (incl. $(4,1)$), Gram quotient, physical resolvents, summed compression — decides the cap-hop coefficient independently ([STRONG] "decisive next calculation").
G5. Tetrahedral local Haar–resolvent coefficient (cheap falsification test of circuit-allowance vs survival, [MOB] §8).
G6. $B_N$ fixed-rank holdout ledger $N=7..18$ (restores the strong all-rank validation claim, C17).
G7. Native torelon reruns of $\sigma_5,\sigma_6$ (replace KPS historical targets).
G8. Cold one-shot regeneration of the all-rank fourth-order bundle (promotes [OUTPUT-CERTIFIED] → [COLD-CERTIFIED]).

**Tier 2 — hard but structured computations (months).**
G9. $m_6$: global sixth-order geometry census + contraction with external-memory sharding (folded weights and carrier census pre-cleared).
G10. Full fifth-order pentagonal coefficient: support-resolved folds for the 572 return histories before rooted subtraction.
G11. Interval-rigor + near-$\Gamma$ touching gates for the fourth-order Brillouin-zone statement (outward-rounded $\pi$; the two-parameter estimate of [GLUE3] §18.3 for $|k|\lesssim u$ where $O(u^2)$ splitting $\sim u^2|k|^2$ meets $O(u^4)$ — without it, a fixed-momentum coefficient theorem must not be promoted to a uniformly isolated near-$\Gamma$ band theorem).
G12. Hyperhoneycomb $O(u)$ candidate: direct Haar normalization, retained sector, compressed operator (tests the framework beyond cubic cells).

**Tier 3 — genuine open theorems (unbounded; these are the load-bearing steps).**
G13. **Classification theorem for shortest physical temporal histories**: determine $r_{\rm escape}$ from the energy-decorated incidence/Feshbach graph without exponential enumeration; would subsume tetra/prism/cube/pentagonal/hyperhoneycomb as one theorem ([FINAL] §12). Includes proving partition-independence of the linked/folded assembly (promotes D6 from synthesis to theorem).
G14. Mechanism of the tier collapse $B^{\rm shp}_N=D^{\rm shp}_N=0$ (accident vs selection rule vs boundary-ideal remnant), and whether the $L^{-4}$ tier appears at fifth/sixth order.
G15. Symbolic-$N$ Gram transcript promoting $c_1^{(N),\pm},c_2^{(N),\pm}$ to unrestricted fixed-$N$ theorems; one more order of the equivariant harmonic-well lemma ($O(h^5)$ residual) for the $O(\beta^{-3/2})$ remainder.
G16. Rank-uniform control: a spectral theorem in $\tau=\beta/N^3$ (neither fixed-regime series supplies an overlap theorem); large-$N$ certificate limitation program (Mellin/Γ-ratio kill criterion).
G17. **PC-2** inhomogeneous Wilson free-energy stability with useful $\log K_\alpha$, **and** the source-radius reduction (equivalently LCIgood + BFSfar in the PMBSF stack) — the two named hypotheses gating every infinite-volume statement.
G18. **The spectral bridge**: volume-uniform overlap of a smeared/dressed $T_1^{+-}$ operator built on the protected carrier with the transfer-matrix spectrum; then multi-plaquette survival of the $b_2$-fold protected level. The corpus's MC already shows the *bare* operator fails this ($<4\%$); the theorem must live in the smeared basis.
G19. Continuum limit: nothing in the corpus reaches the scaling window; Borel–Padé is "consistent, not controlled." Beyond G17–G18 lies the full constructive problem (OS reconstruction etc.), which the corpus correctly does not touch.

**Dependency spine of the gap list:** G3 → (G9, ratio orders 4–6) → nothing further without G17+G18; G13 is orthogonal and would consolidate §6.3; G17+G18 are the only path from "lattice theorem package" to any statement containing the words "mass gap."


---

# Appendix A — Claims ledger

**Classification key (per the consolidation brief):** **(a)** proven · **(b)** numerically/computationally supported · **(c)** conjectured/conditional · **(d)** superseded · **(e)** contradicted elsewhere in the corpus. Refined tag from §0 in brackets. "Src" = source file tag(s) (§0). Formulas appear verbatim in the cited section of this document.

### A.0 Corpus inventory

| File | Role |
|---|---|
| `#-Final-unified-theory.txt` | AI synthesis note, 2026-08-20 ([FINAL]) |
| `15 hour RUN.txt`, `15 hour RUN. results.txt` | v10a.26 A100 run log + results ([RUN15]) |
| `Canonical_SU_N_Wilson_Spectral_Theory_Derivation_First_Corrected.md` | derivation-first canonical record, 2026-08-01 ([CANON]; lossy math encoding) |
| `FOURTH_ORDER_T1PM_BAND_THEOREM_V0_8_CONSOLIDATED.md` | rank-complete 4th order + SU(3) 5th order, 2026-06-14 ([T1PM]) |
| `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v2.md` | formula/status document ([GLUE2]; superseded v1 + addendum; itself **superseded by v3.1**) |
| `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md` | **current formula/status authority** ([GLUE3]; supersedes v1, v2, intermediate v3 draft; delta log in §5.6) |
| `Hodge_Cellular_Circuit_Mobility_Theorem.md` | circuit bound + cell geometry, 2026-08-19 ([MOB]) |
| `Hodge_SU3_Exact_MarkedCluster_m4_Colab.py` | target-blind m4 adjudication engine, unrun ([MCE]) |
| `Hodge_v10a26_Factor52Complete_ExactSW_RootedOracle_A100.md` | notebook source of [RUN15] ([V10A26]) |
| `STRONGEST_FORMULA_RESOLVED_CELLULAR_MOBILITY_2026-08-20.md` | final audit + mobility master equation ([STRONG]) |
| `audit_stranded_flux_zero_backend.{py,json,txt}` | zero-backend falsification ([AUD]) |
| `pentagonal_o4_minimal_representation_frontier.{py,json,txt}` | pentagonal O(4) raw frontier ([PENT]) |
| `files/febf4293….pdf` | flat-band paper draft, 2026-07-25 ([PAPER]) |
| `files/e03f1455….pdf` | GCSG master v1.4, 2026-08-08 ([GCSG]) |

### A.1 Structure and homology (Layer II core)

| # | Claim | Src | Class |
|---|---|---|---|
| 1 | $S(k)+4I=B(k)B(k)^\dagger$; $\operatorname{spec}S=\{-4,-4+q,-4+q\}$ (§4.1) | PAPER, GLUE2, GCSG | (a) [PROVEN] |
| 2 | Signed plaquette graph frustrated; not regaugeable (§4.1) | PAPER | (a)+(b) |
| 3 | $\det B\equiv0$; $Sw=-4w$; exact flat band = Bloch shadow of $\partial_2\partial_3=0$ (§4.1) | PAPER | (a) [PROVEN] |
| 4 | C-even sector has no flat band ($\det N=-2v_1v_2v_3$) (§4.1) | PAPER | (a) |
| 5 | Betti formula $\dim=\#\text{cubes}+b_2-b_3$; $L^3+2$ on $T^3$; 4-topology table (§4.1) | PAPER | (a)+(b) [PROVEN+CERTIFIED] |
| 6 | Cube chains span only $L^3-1$ dims (singular/Rhim–Yang class); wrapping sheets complete band (§4.1) | PAPER | (a)+(b) |
| 7 | First non-flat level $4\sin^2(\pi/L)$; $L^{-2}$ isolation (§4.1) | GLUE2, GCSG | (a) |
| 8 | Link-channel rigidity theorem (§4.2) | PAPER, GLUE2 | (a)+(b) |
| 9 | $L_2^{\downarrow}L_2^{\uparrow}=0$; all-orders scalar action on $\mathcal H_2$; $b_2$-fold pinning under cube channel (§4.2) | PAPER, GLUE2, CANON | (a)+(b) |
| 10 | Protection scope caveat: only inside boundary-operator algebra (§4.2) | GLUE2 | (a) scope statement |
| 11 | Rest carrier is $T_1^{+-}$; no scalar at rest; $b_2\leftrightarrow$ 't Hooft fluxes as Interpretation (§4.2) | PAPER, GLUE2 | (b) / interpretation |
| 12 | SU(2) exclusion: no C-odd sector, $N\ge3$ domain (§4.2) | T1PM | (a) [PROVEN] |
| 13 | Hodge self-duality $JM=-2[s]_\times$; face/link = same Maxwell operator; longitudinal dipolar tail (§6.6) | CANON, GCSG | (a) |
| 14 | Unit $\mathbb{RP}^2$ hedgehog, fragile (not BDI-stable) (§6.6) | CANON, GCSG | (a); stable-charge reading (d) |

### A.2 Perturbative series, SU(3) cubic (spine dynamics)

| # | Claim | Src | Class |
|---|---|---|---|
| 15 | $t_N$ rank law + deficit + monotonicity (§4.3) | CANON, GLUE2, GCSG | (a) [re-verified] |
| 16 | SU(3) ledger $d_\pm,t_\pm$; flat value $11/306$; band table (§4.3) | PAPER, GLUE2 | (b) [CERTIFIED] |
| 17 | $t_+=-11/306$ corrects $-481/612$ (§4.3) | PAPER | (a)+(b); old value (d) |
| 18 | $O(u^3)$ factorization; $E_{\rm flat}(u)$; $t(u)$; ledger $b_3,\ell_3,d_3$ (§4.4) | GLUE2, PAPER, STRONG | (b) [COLD-CERTIFIED; $m_2,m_3$ reproduced in RUN15] |
| 19 | Bare-link/tromino third-order rigidity mechanism (§4.4) | PAPER, GCSG | (a) mechanism + (b); cold rerun of named certificate still requested by GCSG |
| 20 | Generic 4th-order shape space is 4-dimensional; checkpoint extraction; IR tiers; regularity filtration (§5.1) | CANON, GCSG | (a)+(b); any 2-shape *generic* claim (d) |
| 21 | Sealed core $A^{\rm shp}_3=5/48$, $B=D=0$, $\alpha_3=5/12$ (§5.2) | T1PM, GCSG, RUN15, GLUE2 | (b) [CERTIFIED by both kernels] |
| 22 | Axial law $\alpha^{\rm pen}_N=640/[N(N^2-1)^3]$, all $N\ge3$; exceptional values; $\Delta\alpha_N=0$ (§5.3) | T1PM, GCSG, FINAL | (b) [OUTPUT-CERTIFIED; exceptional-rank equality re-verified] |
| 23 | $\beta^{\rm pen}_3$ (full, incl. $\varepsilon$-sectors) $=\frac{17607806155349}{275331901291200}$ (§5.3) | T1PM, GCSG | (e) **contradicted** by RUN15's folded $C_{\rm new}$ — see C1/C2; as historical-kernel value: (b) |
| 24 | $\beta^{\rm pen}_N=P_{17}/(NR_{20})$ for $N\ge4$; positivity; SU(4) value matches independent certificate (§5.3) | T1PM, GLUE2, GCSG | (b) [OUTPUT-CERTIFIED; N=4 match re-verified] |
| 25 | SU(3) anomaly $\Delta\beta_3=-25/64$, $\Delta q_3$; "det sectors shift only $q_N$" true $N\ge4$ only (§5.3) | T1PM, GCSG | (b); the unrestricted scalarity claim (d) |
| 26 | $\Delta q_4=-\frac{304746539168}{160249753125}$ as flat-branch eigenvalue identity (§5.3) | T1PM, CANON, GCSG | (b); scalar-matrix form (d) |
| 27 | SU(5): no det sector (895,524-pair scan); $\Delta q_6=6/343$ (§5.3) | T1PM, GCSG | (b) [RECORD-BACKED payloads] |
| 28 | $q_N$ exact rationals at $N=3,4,5,6$; stable $Q_{32}/D_{34}$ with $q_N<0$, $N\ge7$ (§5.3) | T1PM | (b) [RECORD-BACKED ledgers]; $N=3$ entry (e) via C1 |
| 29 | Global band theorem $\alpha,\beta>0\Rightarrow$ unique $\Gamma$ min / $R$ max; $\Delta c_{4,N}=\alpha+\beta$ (§5.3) | T1PM | (b) conditional on kernel family |
| 30 | Large-$N$ flattening $q\sim-227/N^5$, $W\sim\frac{11930}{9N^7}$, ratio $\frac{11930}{2043N^2}$ (§5.3) | T1PM | (c)/(b) [RECORD-BACKED inputs; $\alpha,\beta$ leads re-verified] |
| 31 | Generalized pencil $\mathcal Q_4\phi=\lambda_4G\phi$, $(Q_4,G)\sim(Q_4{+}\delta G,G)$; SOS $\succeq0$ on cube amplitudes (not on full plaquette space; harmonic sector undetermined); edges; anchors + blind-$R$ holdout; radial directional curvatures — no $\Gamma$ Hessian unless $\beta=2\alpha$, isotropic $-\frac{\alpha+\beta}{6}I$ at $R$ (§5.3) | GLUE3 (controls), GLUE2, STRONG | (a) given kernel + (b); "Hessian" label and $t^2$-coefficient misread both (d) |
| 32 | SU(3) exact band-point table + kernel SHAs (§5.4) | T1PM | (b) exact for supplied kernel |
| 33 | Rest scalar $m_\Gamma^{(4)}=-0.7751458630189173$ — blind numerical evidence; Hamer cross-check demoted to local check ($a_4$ = unverified notebook transcription) (§5.5) | RUN15, GLUE3 | (b) [NUMERICAL, blind]; (e) vs #28's $N{=}3$ entry |
| 34 | $C_{\rm new}=-0.020213328886166577$; $\beta_{\rm new}\approx0.50992$; $W_{4,\rm new}\approx0.92659$; new $A,B,D$ numerical only (tier collapse not exact from new run); $\lambda_{\rm new}-\lambda_{\rm old}=8\Delta_C\mathsf R/\mathsf S\ge0$ (§5.5) | RUN15, GLUE3 | (b) [NUMERICAL]; (e) vs #23 |
| 35 | Scalar-gauge/re-anchoring: exact **same-kernel** identity; "old kernel = new kernel + scalar" **Not established**; $\delta=\Delta_\Gamma$ map is a convention (minimal gauge $a_5=a_6=a_7=0$), not physically selected (§5.5) | GLUE3 (controls), GLUE2 | (a) identity; cross-kernel equality open; [GLUE2]'s stronger "reconciles exactly" framing (d) |
| 35b | Run's final diagonal shift $+11.17343231638178$ target-derived; gate-85 equality by construction (§5.5, §7.1, C22) | RUN15, GLUE3 | disclosure; governing status |
| 36 | Verdict: do not promote either fourth-order claim; adjudication protocol expanded to 11 frozen items incl. $q_{\rm band}^{(4)}-E_0^{(4)}\stackrel{?}{=}m_\Gamma^{(4)}$ vacuum-ledger test and 3,895-vs-3,850 inventory firewall (§5.5) | RUN15, GCSG, GLUE3 | governing status |
| 37 | Quarantined scalar shortcut $-11.068479463778765$ (§5.5) | RUN15 | (d) rejected by both sides |
| 38 | 5th-order SU(3) band $q_5,A_5=\frac{313}{240},B_5,\Delta c_5$; anchors + gates (§6.4) | T1PM | (b) [OUTPUT-CERTIFIED; gates re-verified]; scalar inherits C1 |
| 39 | Rest-mass series through $u^5$ (§6.4) | T1PM | (e) at $u^4,u^5$ via C1; lower orders (b) |
| 40 | $\sigma(u)$ through $u^4$ native; $s_3=-61/408$ derivation; sign correction (§6.4) | T1PM, V10A26 | (b); $+61/408$ (d) |
| 41 | $\sigma_5$ (and $\sigma_6$) = KPS historical targets, not native (§6.4) | T1PM | (c) pending native rerun |
| 42 | Ratio $m/\sqrt\sigma=\sqrt6\sum c_nu^n$, $c_0..c_5$ (§6.4) | T1PM | (b) series algebra re-verified; $c_4,c_5$ inherit C1 + #41 |
| 43 | $m_6$ open; $c_6$ affine formula; folded weights + carrier census pre-cleared (2,186 signatures) (§6.5) | T1PM | (c)/open; pre-clearances (b) [RECORD-BACKED] |
| 44 | Fifth-order census table (6,676,658 supports etc.) (§6.4) | T1PM | (b) [RECORD-BACKED] |
| 45 | Fixed-rank holdout: $q_N$ matches $N=7..18$; full kernels $N=7,8$ only; $A/B$ ledger open (§7.6) | T1PM | (b) with corrected scope; v0.7 claim (d) |
| 45a | Exact 25-point numerator stencil $w_0=\frac92\alpha+3\beta$, $w_1=-(\alpha+\beta)$, $w_2=\frac\alpha4$, $w_d=\frac\beta4$; zero-mode gate $w_0+6w_1+6w_2+12w_d=0$; historical values incl. $w_0=\frac{189690244462349}{91777300430400}$ (§5.3) | GLUE3 | (a) for the pencil form [re-verified]; historical instance exact for saved kernel |
| 45b | High-symmetry anchors $\lambda_X=\alpha$, $\lambda_M=\alpha+\frac\beta2$, $\lambda_R=\alpha+\beta$; holdout identity $\lambda_R=2\lambda_M-\lambda_X$ (§5.3) | GLUE3 | (a) [re-verified] |
| 45c | $t_N=\frac1{4N^3}-\frac1{16N^5}-\frac{77}{64N^7}+O(N^{-9})$; $\beta_N/\alpha_N\to\frac{617}{576}$ (§4.3, §5.3) | GLUE3 | (a) [re-verified] |
| 45d | Odd-$L$ torus grid does not contain $R$; $W_4=\alpha+\beta$ statement is for the continuous zone / even-$L$ tori (§5.3) | GLUE3 | (a) |
| 45e | $Y=4u$ archived line = definition/label erratum; coefficients already in $u$; no $4^n$ rescaling (§1.1) | GLUE3 | (a) audit finding; controls C4 |
| 45f | Cluster-additivity rule: $H_{\rm eff}$ not cluster additive, $H_{\rm eff}-eI$ is; Möbius subtraction on vacuum-subtracted object (§6.3) | GLUE3 | (a) discipline statement |
| 45g | Mobility-order taxonomy $r_{\rm split},r_{\rm off},r_{\rm mob}$ with $r_{\rm off}\le r_{\rm mob}$ (§6.3) | GLUE3 | definitions |

### A.3 Mobility theory and non-cubic cells

| # | Claim | Src | Class |
|---|---|---|---|
| 46 | Weighted circuit bound $r\ge w_{\min}-2$; $F-2$ corollary; survival gates; modular circuits (§6.3) | MOB | (a) [PROVEN] |
| 47 | Promotion $r_{\rm phys}=w_{\min}-2$ (§6.3) | (older claims) | (e) **falsified** by pentagonal cap hop (record-backed) |
| 48 | Prism all-volume identities; $\dim\ker B_\square=2L^2+1$; 2nd-order flat; 3rd-order honeycomb bands; spread 6 (§6.3) | MOB | (a)+(b) |
| 49 | $c_3(N)=64/[N(N^2-1)^2]$; $\Delta_3(3)=2$ (§6.3) | MOB, FINAL | (b) |
| 50 | Cube: $P_ZH_{\rm cube}P_Z=A(C_L)$, $2\cos k_z$; $c_4^\square(N)=-160/[N(N^2-1)^3]$; $\alpha_N=4|c_4^\square|$ (§6.3) | MOB, FINAL, GLUE2 | (b) |
| 51 | Tetrahedron: order-2 allowed; compression eigenvalues $-18/5,-2$; local SU(N) coefficient open (§6.3) | MOB | (b); coefficient open |
| 52 | Tetrahedral coefficient $-8/[N(N^2-1)]$ (§6.3) | FINAL | (c)/[RECORD-BACKED]; (e) vs #51's "open" (C15) |
| 53 | $c_{r,\rm prim}(N)=2^{r-1}S_r/[N(N^2-1)^{r-1}]\sim N^{-(2r-1)}$; table $r=2..5$ (§6.3) | FINAL | (c) as law; instances $r=3,4$ (b); $r=2,5$ [RECORD-BACKED] |
| 54 | Pentagonal primitive relation weight 7 ⇒ primitive channel $r=5$; $c_{5,\rm prim}(3)=35/384$ (§6.3) | FINAL, STRONG | (b) arithmetic + (c) channel status |
| 55 | $E_{\rm cap}=10/3\neq E_{\rm side}=8/3$; cap band is the physical one (§6.3) | FINAL | (a) energy count re-verified; consequence (b) |
| 56 | $h_4^{\rm side}=-\frac{2861009}{84387303000}$; $\tau_4$; $\delta E^{(4)}_{\rm cap}=-\frac{2861009}{8438730300}u^4\cos k$; $r_{\rm hop}=4$ (§6.3) | GLUE2, FINAL | (b) [RECORD-BACKED — artifacts absent; ratios re-verified] |
| 57 | 28 proper-return histories vanish; folds vanish; periodic audit agrees (§6.3) | FINAL | (b) [RECORD-BACKED] |
| 58 | $A_N[h]\neq A_N[\pi(h)]$ (static chain ≠ amplitude) (§6.3, D5) | FINAL, STRONG | (a) once #56 granted; else (c) |
| 59 | $h_4^{\rm side}(N)\sim-\kappa N^{-7}$; slope $-7.0021$ ($N=7..13$); blind $N=13$ 20/20 (§6.3) | FINAL | (b) [RECORD-BACKED] |
| 60 | Surviving temporal order $r\Rightarrow N^{-(2r-1)}$ (universal law) (§6.3) | FINAL | (c) [CONJECTURE] |
| 61 | Pentagonal O(4) raw frontier: 20 histories, cut ranks 4/6/6, sectors, $(4,1)$ rank 3, bare contractions =1; 8/8 (§7.3) | PENT | (b) in-corpus [CERTIFIED] |
| 62 | Zero-backend falsification; $\mathrm{Wg}(e)=1/8$, $\mathrm{Wg}((12))=-1/24$, $\int|U_{11}|^4=1/6$; 8/8 (§7.2) | AUD | (b) in-corpus; the zero-claim (e) [FALSIFIED] |
| 63 | Fifth-order census $1030=120+910$; $910=338+572$; 14 lifts; 19/19 (§6.3) | FINAL | (b) [RECORD-BACKED] |
| 64 | $\delta c_{5,\det}=\frac{235424477177}{407461473619200}$; $c_{5,\rm direct}=\frac{37373840041427}{407461473619200}$ (§6.3) | STRONG, FINAL | (b) [RECORD-BACKED; sum re-verified]; kills "center-dark" claim (e→d) |
| 65 | Full fifth-order pentagonal coefficient open (572 folded histories) (§6.3) | STRONG, FINAL | open |
| 66 | Resolved cellular mobility master equation (D6) | STRONG | (c) [CONJECTURE as general theorem; synthesis] |
| 67 | Mixed tetra–octa certificate: 12/12 gates; non-scalar $O(u^2)$ residue; separation $32/31$ | FINAL | (b) [RECORD-BACKED] |
| 68 | Hyperhoneycomb: rank 10 / kernel 2; two primitive relations; candidate $O(u)$ transition (§6.8) | FINAL | (c) [CONJECTURE] |
| 69 | Cellular certificate 26/26 gates; artifact SHA table (§7.6) | MOB | (b) [RECORD-BACKED script] |

### A.4 Compact one-plaquette theory (Layer I) and bridge

| # | Claim | Src | Class |
|---|---|---|---|
| 70 | Weyl reduction $J(\tfrac12C_2)J^{-1}=\tfrac14(-\Delta_{\mathfrak t}-|\rho|^2)$; unique nondegenerate well; normal form $H_0,H_1,H_2$ (§6.1) | GCSG, CANON | (a) [PROVEN] |
| 71 | SU(3) even gap 3-term + proved $O(\beta^{-1})$ remainder (equivariant harmonic-well lemma) (§6.1) | GCSG | (a) [PROVEN] |
| 72 | Non-radial escape $c_1-c_1^{\rm rad}=\sqrt6/576$ (§6.1) | GCSG, CANON | (a) |
| 73 | $c_0^{(N),\pm}$ closed forms (§6.1) | CANON, GCSG | (a) fixed $N\ge3$ |
| 74 | $c_1^{(N),\pm}$ closed forms (§6.1) | CANON, GCSG | (b) $N=3..12$ exact; (c) unrestricted-$N$ |
| 75 | $c_2^{(N),\pm}$ closed forms; SU(3) values $-\frac{5665}{110592}$, $-\frac{53}{864}$ (§6.1) | GCSG | (b) listed ranks; (c) unrestricted; $-1781/55296$ (d) |
| 76 | Traceless-Gaussian rep + cut-join recursion + moment table (§6.1) | CANON | (a) |
| 77 | Exact Gram projection $v^TG^{-1}v$; low-rank trace reduction (§6.1) | CANON | (a) |
| 78 | Polarity-excess law $\frac{9}{32N}$; ratio $\to\frac32$ from above (§6.1) | CANON, GCSG | (a) corollary |
| 79 | Nonuniformity $\beta\gg N^3$; $\tau$-scaling ratio $\frac32-\frac{1}{3072\tau}$ (§6.1) | CANON | (a) scaling; $\tau$-limit (c) [re-derived here] |
| 80 | Odd staircase $e_3,e_5,e_7,\dots$; SU(3)/SU(4) cubic lock with sharp $F_{\min}=\frac{81\sqrt3}{16\pi^3}$; SU(5) failure with explicit counterexample (§4.7) | CANON, GCSG | (a) [counterexample re-verified] |
| 81 | Kantorovich correlation bound $0.829106\ldots$ (§4.7) | CANON | (a) |
| 82 | Local overlap theorem $\langle\phi_-,\mathrm{Im\,Tr}U\phi_0\rangle\neq0$ with two-sided bound (§4.7) | CANON | (a) local only |
| 83 | Improved sources $\mathcal O_3^{\rm imp}$, $\mathcal O_5^{\rm prim}$ (§4.7) | CANON, GCSG | (a) kinematics |
| 84 | Weak-field bridge $\mathrm{Im\,Tr}e^{iX}$ expansion; polarization/dispersion diagnostics $R_{\rm shift},R_{E^2},R_{\cosh}$ (§4.7) | GLUE2 | (a) kinematics; MC promotion needs bootstrap (open) |
| 85 | Fixed-shell radial threshold $c_*=\frac{(\pi-2)^2}{8\pi}$; universal in shell (§6.1) | CANON | (a) for contracted radial class |
| 86 | Leakage quartic + $\rho_3$; finite-channel $\beta>\frac32\mu_G^4\rho_3^2$ (§6.1) | CANON, GCSG | (a)+(b) finite-channel only |
| 87 | Radial-tail no-go ($n^2$ growth; $p=1$ noncompact; $K_2$ HS but unphysical) (§6.1) | CANON, GCSG | (a); promotion of $\rho_3$ (d) |
| 88 | Local weak-well gap $\Delta_+^{SU(3)}(\beta_{\rm loc})$ 3-term (§6.1 = [GLUE2] §13.2) | GLUE2, GCSG | (a); explicitly *not* a lattice/glueball gap |
| 89 | One-plaquette flux-tower bridge $h_{\rm loop}=4H_\beta-4\beta$, $\beta=Ny/2$ (§6.1) | CANON | (a) operator identity only |

### A.5 Seam, transfer, capacity (Layers III–V)

| # | Claim | Src | Class |
|---|---|---|---|
| 90 | EP atlas; vacuum EP $0.797842828512+1.389351779364i$; radius 1.6021; second EP, radius 2.4245 (§6.2) | GCSG | (b) [Kantorovich-certified at truncation; interval tails queued] |
| 91 | Odd-sector structure theorem $\Delta_-=G+\tfrac12\Delta_+$, $G$ analytic to 2.4245 (§6.2) | GCSG | (a) mechanism + (b) |
| 92 | Certified crossover v1 residuals; failure-mode rule (§6.2) | GCSG | (b) |
| 93 | Wilson–Bergman weight = Bessel–Toeplitz det; $\|M_q\|=(2N)^k$; deficit $\asymp C/K^2$ (§6.7) | GCSG | (a)+(b); "N-uniform =1" claim (d) withdrawn |
| 94 | Bergman rank-1/2 transfer closure (no $n^2$ growth) (§6.7) | GCSG | (b) |
| 95 | Global fixed-window firewall false (Bernoulli no-go) (§6.7) | CANON, GCSG | (a) no-go; old firewall (e→d) |
| 96 | Source-tilt identity; Peierls; square-free domination; rooted summability $C_*<1$ (§6.7) | CANON, GCSG | (a) implications, (c) via PC-2 |
| 97 | PC-2 free-energy bound; source-radius reduction; LCIgood/BFSfar; ML domination (§6.7) | CANON, GCSG | (c) **open load-bearing hypotheses** |
| 98 | Caged-band capacity sandwich; curvature floor $h^\vee I/2$; HS leakage bound; Combes–Thomas data (§6.7) | GCSG | (a)/(b) per item |
| 99 | Davies–Gaffney sharper rate (§6.7) | GCSG | (c) finite-certificate only |

### A.6 Physics contact and scope

| # | Claim | Src | Class |
|---|---|---|---|
| 100 | AT replay 25/25; continuum $6.065(40)$ (§7.7) | GCSG | (b) transcription-verified |
| 101 | Matched MC (`next14.json`: $\beta=5.8941$, $L=14$, $N_t=16$, 2000 cfgs) $aM=1.6897344913\pm0.1206114757$ vs $1.591(18)$, pull $+0.82$; $a\sqrt\sigma=0.2628289891\pm0.0023244282$ (§7.7) | GCSG, GLUE3 | (b) [NUMERICAL]; downgraded to *structured evidence, not a cold-reproducible ensemble certificate* — one gate literal-true, JSON not hash-bound, raw ensemble absent ([GLUE3] §14; C21) |
| 102 | Raw one-plaquette fitted fraction $0.0072359730\pm0.0164694235$; smeared amplitude $0.7996986994$; physical state extended (§7.7) | GCSG, GLUE3 | (b) — the measured obstruction to the naive bridge; same reproducibility caveat as #101 |
| 103 | Strong-coupling series "consistent, not controlled" toward continuum (§6.4) | GCSG | governing scope statement |
| 104 | No continuum/infinite-volume mass gap established anywhere in corpus (§0) | CANON, GLUE2, PAPER, GCSG | governing scope statement |
| 105 | Local class gap ≠ glueball mass (no-identification rule) | CANON, GCSG | governing scope statement |

### A.7 Superseded/rejected register (already excluded above; collected)

$Y=2\beta/3$ as a live convention (reread as label erratum, [GLUE3]) · $+61/408$ tension sign · $-481/612$ C-even hop · scalar-matrix SU(4) correction · "+2 accidental states" · $t^2$-coefficients as curvatures **and** the "Hessian curvature" label for $\kappa(n)$ (radial directional curvatures; no $\Gamma$ Hessian unless $\beta=2\alpha$) · $-1781/55296$ odd $\beta^{-1}$ · $2N^2+1$ radial difference · $\varepsilon^4=2N/\beta$ dilation · $-0.363N$ radial target · $\rho_3$ full-channel promotion · global fixed-window firewall · $r_{\rm phys}=w_{\min}-2$ promotion · "center-only circuits dark" · stranded-flux zero backend · v0.7 holdout overclaim · "old kernel = new kernel + scalar" as an established identity (Not established, [GLUE3] §17) · gate-85 equality as independent scalar verification (by construction, [GLUE3] §9.2) · `next14.json` 23/23 as an ensemble certificate (one gate literal-true; not hash-bound) · "current Lean tree verifies these formulas" (False — it contains no encoding of the $O(u^4)$ theorem, [GLUE2] §15/[GLUE3] §17) · Schur/Haar-Hessian "Theorem B" · 4D SU(2) θ/TRG thread · q-Racah novelty claim · Gemini-draft odd coefficient and global claims · Riccati/global-convexity mass-gap route · Peierls numerics as volume-uniform gap evidence · "$B_N=D_N=0$ is a symmetry identity" (it is dynamical) · "all-orders flatness from low-order boundary identity."

### A.8 Open problems register (pointer)

See §9 (G1–G19); additionally from the sources: promote $c_R=2c_M-c_X$-style gates into the fifth-order holdout program; SU(3) lower-order Appendix-A scripts absent from release bundle ([T1PM] §12); CUDA execution certificate for the Weyl-triangle solver ([GCSG] AUD-4); noncubic Betti-count extension test ([PAPER] §10).

---

*End of master document. Every formula above is cited to its source file; classifications follow the precedence rules of §0. The two boxed decisions a referee should check first: the §5.5 dispute table, and the §2.3 load-bearing steps.*
