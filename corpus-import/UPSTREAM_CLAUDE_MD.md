# ALL THEORY — the mathematics

The subject is the **SU(N) cubic flux-band spectral program**: the charge-conjugation-odd one-plaquette flux sector of the Kogut–Susskind Hamiltonian on a cubic lattice, its homological carrier, and the perturbative mobility of that carrier in the strong-coupling expansion.

**Authority: `corpus/`.** Four documents, in order — `MASTER_THEORY_UNIFIED_2026-08-20_v3.md` (scientific and status authority), `GLUEBALL_DETAILED_FORMULA_DOCUMENT_2026-08-20_v3_1.md` (coefficient-level appendix), the consolidation guide (navigation), the canonical source manifest (provenance). Section numbers below refer to the unified master unless marked *(detailed)*.

Older documents in this tree and on the mounted archive drives predate that stack and are superseded where they conflict. Some carry a retired "Yang–Mills mass gap / Clay Millennium" framing; that framing is not the subject and §0.2 and §12 say so directly.

---

## 1. Conventions

The canonical insertion coordinate is the coefficient of $-(\chi_p+\bar\chi_p)$:

$$u \;=\; \frac{\beta_N}{2N}, \qquad\text{SU(3):}\quad u=\frac{\beta_3}{6}=\frac1{g_H^4}.$$

**The archived line $Y = 2\beta_{\mathrm{lat}}/3 = 4u$ is a definition-label erratum, not a change of variables.** The printed coefficients in the affected lineage were already generated in $u$. They must never be multiplied or divided by $4^r$. (§2.1, errata §14.1–14.2.)

The weak-well expansions use a separate parameter $\beta_{\mathrm{loc}}$; no coefficient transfers between $u$ and $\beta_{\mathrm{loc}}$ without an explicit operator identity.

Chain complex $C_3\xrightarrow{\mathsf C=\partial_3}C_2\xrightarrow{\partial_2}C_1$ with $\partial_2\mathsf C=0$; $Z_2=\ker\partial_2$, $B_2=\operatorname{im}\mathsf C$, $\mathcal H_2=Z_2\cap\ker\mathsf C^\dagger\simeq H_2$. Write $B(k)=\partial_2(k)^\dagger$ — distinct from $\mathsf C=\partial_3$.

Bloch scalars: $d_i=e^{ik_i}-1$, $a_i=|d_i|^2=4\sin^2(k_i/2)$, $X_i=1-\cos k_i=a_i/2$; $q_a=\sum a_i$, $\mathsf S=\sum X_i$, $\mathsf Q=\sum X_i^2$, $\mathsf R=\sum_{i<j}X_iX_j$; so $q_a=2\mathsf S$ and $e_2=4\mathsf R$.

Representation products: $F\otimes\bar F=\mathbf 1\oplus\mathrm{Adj}$ and $F\otimes F=\operatorname{Sym}^2F\oplus\Lambda^2F$ (errata §14.3 — earlier sources reversed these).

---

## 2. What is established

**Incidence and homology (analytic, exact).** $S(k)+4I=B(k)B(k)^\dagger$, hence $\operatorname{spec}S(k)=\{-4,\,-4+q_a,\,-4+q_a\}$, and $S(k)\psi(k)=-4\psi(k)$ for $\psi=(\bar d_3,-\bar d_2,\bar d_1)^{\!\top}$ — this is $\partial_2\partial_3=0$ in Bloch form. The flat band is **singular at $\Gamma$**: the normalized $\psi$ has no continuous extension there, and translated cube boundaries alone do not span the torus carrier. Finite volume: $\dim Z_2=\#C_3+b_2-b_3$, giving $L^3+2=(L^3-1)+3$ on $T_L^3$. First non-flat incidence level $4\sin^2(\pi/L)$ — so finite-volume isolation closes as $L^{-2}$. SU(2) is excluded at the source: $U^*=\varepsilon U\varepsilon^{-1}$ makes complex conjugation a gauge transformation, so the charge-odd projector vanishes and the construction begins at $N=3$. (§3.)

**Second order, all ranks (analytic + saved-output verified).**

$$t_N=\frac{2N(N^2-4)}{(N^2-1)(2N^2-1)(4N^2-9)}>0,\qquad t_3=\tfrac{5}{612},$$

with $t_N=\frac1{4N^3}-\frac1{16N^5}-\frac{77}{64N^7}-\frac{1021}{256N^9}+O(N^{-11})$, bandwidth $W_N^{(-)}(u)=12t_Nu^2+O(u^3)$, and $\Delta^{(2)}_{N,L}=4t_Nu^2\sin^2(\pi/L)+O(u^3)$. SU(3) ledger: $d_+^{(2)}=\tfrac{223}{1020}$, $t_+^{(2)}=-\tfrac{11}{306}$, $d_-^{(2)}=\tfrac{7}{102}$, $t_-^{(2)}=\tfrac{5}{612}$. (§4.1–4.2. The older $t_+^{(2)}=-481/612$ omitted a vacuum-mediated route and is superseded.)

**SU(3) through third order (251/251 cold exact gates).**

$$H_{\mathrm{eff},-}(k,u)=E_{\mathrm{flat}}(u)\,I+t(u)\,B(k)B(k)^\dagger+O(u^4),$$
$$E_{\mathrm{flat}}(u)=\tfrac83+u+\tfrac{11}{306}u^2-\tfrac{109151}{249696}u^3,\qquad t(u)=\tfrac5{612}u^2+\tfrac{1975}{124848}u^3.$$

Since $B^\dagger\psi=0$, the carrier energy is **independent of $k$ through $O(u^3)$**. Ledger: $b_3=\tfrac{1975}{124848}$, $\mathrm{leak}_3=-\tfrac{12331}{249696}$, $d_3=\tfrac7{32}+12\,\mathrm{leak}_3-4b_3=-\tfrac{109151}{249696}$. Three-distinct-plaquette tromino numerators vanish at $O(u^3)$. (§4.3.)

**Fourth-order structure (analytic, given the symbol).** Pull back to cube amplitudes: $Q_4=\mathsf C^\dagger H_4\mathsf C$, $G=\mathsf C^\dagger\mathsf C=\sum_iL_i$ with $L_i=2I-T_i-T_i^{-1}$. The centered coefficient is a **generalized** eigenvalue, $\mathcal Q_4\phi=\lambda_4G\phi$, with scalar-gauge equivalence $(Q_4,G)\sim(Q_4+\delta G,G)$. On a two-invariant tier,

$$\lambda_4(k)=\frac{\alpha\mathsf Q+\beta\mathsf R}{2\mathsf S},\qquad \mathcal Q_4=\tfrac\alpha4\sum_iL_i^2+\tfrac\beta4\sum_{i<j}L_iL_j,$$

so $\lambda_X=\alpha$, $\lambda_M=\alpha+\beta/2$, $\lambda_R=\alpha+\beta=W_4$, and **$\lambda_R=2\lambda_M-\lambda_X$ is available as a blind holdout**. The generic cubic shape has four independent tiers, $\varepsilon_4=c_0+Aq_a+Be_2+C\,\frac{4e_2}{q_a}+D\,\frac{e_3}{q_a}$, with $\alpha=4A$, $\beta=8A+16C$ when $B=D=0$ — the two-invariant collapse is *dynamical*, not a consequence of cubic symmetry. (§5.)

**The historical SU(3) kernel (exact for the saved kernel).** $q^{(4)}_{\mathrm{old}}=-\tfrac{20721577909065127111}{7250590288602460800}=-2.857915988114558978\ldots$, $\alpha_{\mathrm{old}}=\tfrac5{12}$, $\beta_{\mathrm{old}}=\tfrac{17607806155349}{275331901291200}$, width $W_{4,\mathrm{old}}=\tfrac{132329431693349}{275331901291200}=0.48061786909826\ldots$, with an exact 25-point stencil ($w_0=\tfrac92\alpha+3\beta$, $w_1=-(\alpha+\beta)$, $w_2=\tfrac\alpha4$, $w_d=\tfrac\beta4$) obeying the zero-mode gate $w_0+6w_1+6w_2+12w_d=0$. Its unresolved input is the *upstream physical identification* of the kernel. (§6.)

**All ranks, fourth order (output-certified).** $\alpha_N=\dfrac{640}{N(N^2-1)^3}$ and $\beta_N=\dfrac{P_{17}(z)}{N\,R_{20}(z)}>0$ for $N\ge4$, $z=N^2$; $\beta_N/\alpha_N\to\tfrac{617}{576}$; $W_{4,N}=\tfrac{11930}{9N^7}+\tfrac{1299983}{324N^9}+O(N^{-11})$. Positivity for $N\ge7$ from positive denominator factors plus a certified binomial-basis expansion of $P_{17}$ about $z=49$; $N=4,5,6$ by exceptional-rank substitution; $N=3$ separately. (§8; $P_{17}$ has its one canonical home in the detailed appendix A.)

**Separate exact results.** Improved charge-odd source $\mathcal O_3^{\mathrm{imp}}(U)=\tfrac{32\operatorname{ImTr}U-\operatorname{ImTr}U^2}{24}$, which cancels the quintic term: $\mathcal O_3^{\mathrm{imp}}(e^{iX})=-\tfrac{P_3}6+\tfrac{P_7}{1260}+O(|X|^9)$ (§10.1). Pentagonal cap hop — a **different geometry and retained sector** — $h_4^{\mathrm{side}}=-\tfrac{2861009}{84387303000}$, $\Delta E^{(4)}_{\mathrm{cap}}(k)=-\tfrac{2861009}{8438730300}u^4\cos k$, $r_{\mathrm{hop}}=4$ (§9.3). Local weak-well gap $\Delta_+^{SU(3)}=\sqrt{2\beta_{\mathrm{loc}}/3}-\tfrac5{16}-\tfrac{311\sqrt6}{9216}\beta_{\mathrm{loc}}^{-1/2}+O(\beta_{\mathrm{loc}}^{-1})$ (§10.3).

---

## 3. The one disputed item

**The complete physical fourth-order kernel.** Two independent computations agree on the axial coefficient and disagree off-axis:

| | historical 189-record kernel | August linked marked-cluster run |
|---|---|---|
| $A$ (axial) | $5/48$ **exact** | $0.104166666666728$ (numerical) |
| $C$ (planar) | $-\tfrac{211835444920651}{4405310420659200}=-0.04808638318135875\ldots$ **exact** | $-0.020213328886166577$ (numerical) |
| $\Gamma$ anchor | $q^{(4)}_{\mathrm{old}}=-2.857915988\ldots$ | $m^{(4)}_\Gamma=-0.7751458630189173$ |

With $\Delta C=0.027873054295192174\ldots$, and assuming exact tier collapse for the new kernel,

$$\mathsf C^\dagger\!\left[(H_4^{\mathrm{new}}-s_{\mathrm{new}}I)-(H_4^{\mathrm{old}}-q_{\mathrm{old}}I)\right]\!\mathsf C=4\Delta C\sum_{i<j}L_iL_j,\qquad \lambda_{\mathrm{new}}-\lambda_{\mathrm{old}}=8\Delta C\,\frac{\mathsf R}{\mathsf S},$$

so $\Delta\lambda_X=0$, $\Delta\lambda_M=8\Delta C\approx0.22298$, $\Delta\lambda_R=16\Delta C\approx0.44597$.

**A scalar re-anchoring cannot close this.** Scalar-gauge freedom changes the quoted rest coordinate *within one kernel*; it cannot change a centered planar coefficient, a bandwidth, an off-axis dispersion, or a radial curvature. The $+11.17343231638178$ diagonal shift used in the 15-hour run was chosen to map a raw folded rest value onto the linked scalar — it was **not** $\Delta_\Gamma$, and equality after it is by construction. The scalar difference $\Delta_\Gamma=2.0827701250956417\ldots$ proves no kernel identity. (§7, §9 *(detailed)*, appendix B.)

The decisive resolution is one target-blind sealed run producing $m^{(4)}_\Gamma$ **and** $C^{(4)}$ together, under all eleven freeze conditions in §15.1 — including a cold 3,895-topology Stage-3H generation of an unshifted 189-record kernel, a rooted Möbius ledger on the **vacuum-subtracted** object, and no historical scalar or shape anywhere in the data flow. Work lives in `programs/hodge_o4_adjudication/`.

---

## 4. What is open, and the boundary

Open: a uniform near-$\Gamma$ isolated-band theorem — the second-order separation is $O(u^2|k|^2)$ and competes with $O(u^4)$ for $|k|\lesssim u$, so a fixed-momentum coefficient theorem is **not** a band theorem; a volume-uniform dressed-operator spectral-overlap bridge; survival beyond the one-plaquette retained sector; a controlled continuum limit. Separately, the stochastic sparsity lemma (S) of the Birman–Schwinger program, and an independent re-derivation of the order-6 geometry census behind $m_6$.

A Bernoulli rare-box argument **proves** that every global fixed-window defect firewall fails: at fixed positive defect density the projected norm tends to one in probability as volume grows. The rooted replacement rests on the source-tilt identity and still needs the inhomogeneous free-energy estimate $Z_{\beta,\alpha,\Gamma,L}/Z_{\beta,L}\le K_\alpha^{|\Gamma|}$ plus a source-radius reduction. (§12.)

**The boundary.** A positive projected finite-order coefficient is not a full-Hamiltonian, infinite-volume, or continuum gap theorem. The finite-volume isolation that does exist scales as $L^{-2}$ and collapses as $L\to\infty$. **No formula here is a proof of the Yang–Mills mass gap**, and the one-plaquette $T_1^{+-}$ object should be called a flux band or operator seed, not the physical glueball, absent a separate overlap and continuum argument.

---

## 5. Traps

1. **$Y=4u$** is a label erratum. Never rescale by $4^r$.
2. **$\beta_N$'s compact formula must not be substituted at $N=3$.** Use the separate exact $\beta_3$.
3. **"Determinant sectors shift only the scalar anchor" is false at $N=3$** ($\Delta\beta_3=-\tfrac{25}{64}$, $\Delta C_3=-\tfrac{25}{1024}$). It does hold for $N\ge4$.
4. **The $\Gamma$ curvatures are radial directional second derivatives, not a Hessian** — a cubic Hessian exists only if $\beta=2\alpha$, which the historical kernel does not satisfy. At $R$ the Hessian *is* isotropic: $\nabla^2\lambda_4(R)=-\tfrac{\alpha+\beta}{6}I$.
5. **$H_{\mathrm{eff}}$ is not cluster-additive; $H_{\mathrm{eff}}-eI$ is.** Möbius subtraction must act on the vacuum-subtracted operator or gap.
6. **Primitive color law carries $(-1)^{r+1}$** with unsigned counts $S_r$; and static circuit completion is not a universal equality for physical mobility order — the pentagonal cap falsifies that promotion.
7. **The 3,895 Stage-3H topologies and the 3,850 stable-rank trace topologies are different inventories.** Never interchange them.
8. **Static incidence cannot fix the first mobility order.** Histories with equal static projection $\pi(h)$ can carry different amplitudes; separate $r_{\mathrm{split}}$, $r_{\mathrm{off}}$, $r_{\mathrm{mob}}$.
9. **`CERT_O4_next14.json` is not a cold ensemble certificate.** One of its 23 "passing gates" is a literal truth value in the source; it is not source-hash bound; no raw ensemble was found. Its variational amplitude is not automatically a normalized overlap probability.
10. **The Hamer decimal $a_4=-0.0968932328773$ is a local transcription**, not a hashed primary source. $8a_4=-0.7751458630184$ sits within $5.2\times10^{-13}$ of the linked scalar — a strong cross-check, not verification.
11. **The local Lean tree encodes none of this** — not the 189-record kernel, not $\alpha/\beta$, not the scalar adjudication, not the Hodge pencil. Do not cite it for them.

---

## 6. Status vocabulary

From §1, and used throughout this tree. **Truth status and evidence level are independent axes.**

Status: Proven · Conditional · **Disputed** · Open · Superseded · Falsified.
Evidence: Analytic · Cold-reproduced · Output-certified · Numerical · Record-backed · Prose-only.

**"Certified" is never a synonym for "proved."** An identity can be analytically exact and still depend on a disputed input kernel; a cold run can be numerically precise without producing a theorem.

Evidence precedence, highest first: self-contained exact derivation → authenticated cold reproduction → exact saved output with an independent verifier → internally consistent numerical output → later prose summary → filename or chronology. **A newer file does not outrank an exact counterexample, and a file named "final" does not override a failed invariant.**

---

## 7. Where things are

`corpus/` authority · `theory/` open problems, conventions, citation-safety map, theorems, conjectures · `programs/` campaigns, with `hodge_o4_adjudication/` the live front · `numerics/` engines, certificates, results, data · `papers/` manuscripts (flat-band v1.1; unified spectral geometry v1.4) · `literature/` external papers · `records/` logs, audits, transcripts, reorganization manifests · `archive/` bundles and simulations · `export/` the hashed contract to [WORKHOUSE](https://github.com/ats314/WORKHOUSE), the downstream machine verifier · `QUARANTINE/` moved-out material, nothing deleted.

Full map and topic router: `INDEX.md`. Current status: `STATE.md`. Filenames are structured metadata — `CLASS_TOPIC_descriptor[_vN][_date]`, see `NAMING_CONVENTION.md`, so `ls THM_*` and `ls *_O4_*` are real queries. Every exact rational in the corpus, with its symbol and defining location, is indexed in `theory/DOC_FLUX_constants_index.md`. Before quoting any constant across eras, pin the convention via `theory/DOC_GOV_conventions.md`; before citing an archive document, route through `theory/DOC_GOV_chain_status_map.md` — status headers in older documents sit over conditional content in every era.

`E:\YANG`, `E:\YANG_ANTI` and `F:\` are mounted read-only archives; `SOURCES.md` maps them.
