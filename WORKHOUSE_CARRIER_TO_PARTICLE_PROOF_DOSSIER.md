# From the WORKHOUSE carrier to an actual particle

**A read-only proof dossier**  
**Date:** 2026-08-22  
**Scope:** Hamiltonian \(SU(3)\) lattice gauge theory, the WORKHOUSE charge-odd one-plaquette carrier, the thermodynamic limit, and the continuum limit  
**Repository status:** the WORKHOUSE clone was read only and was not modified

---

## Executive result

The strongest honest conclusion is a chain of two exact new lemmas, one imported spectral theorem, and one genuinely open continuum estimate.

1. **A necessary correction.** In the unrestricted gauge-invariant \(C=-\) Hilbert space, the one-plaquette shell is not uniformly isolated. Charge-odd winding flux loops are exact counterexamples for \(L=3,4,5\).
2. **A sharp repaired theorem.** In the physically appropriate trivial \(\mathbb Z_3\) one-form-charge block—the glueball block—the complete spectrum of the electric Hamiltonian below \(4\) is exactly the \(3L^3\)-dimensional charge-odd one-plaquette shell at \(8/3\). Its external electric gap is therefore exactly \(4/3\).
3. **A conditional all-orders finite-spacing patch.** Yarotsky's volume-uniform spectral-localization theorem has compatible abstract local-Hilbert-space hypotheses. Conditional on a uniform periodic-torus adaptation and the exact WORKHOUSE-to-local-interaction normalization, rescale the one-link gap to one and let \(\epsilon(u):=\sup_x\|\widehat\phi_x(u)\|\). A sufficient condition for the whole \(8/3\) kinematic patch to stay separated is

   \[
   \lambda:=c_2\epsilon(u)<\frac1{33},
   \]

   where \(c_2\) is Yarotsky's range-dependent constant. If \(\epsilon(tu)<c_1\) and \(c_2\epsilon(tu)<1/33\) hold along \(0\le t\le1\), restriction to the neutral physical \(C=-\) block gives a Riesz patch of rank \(3L^3\) for every \(L\ge3\).
4. **An exact continuum pole lemma.** If a separated-time-normalized carrier source has a shrinking spectral island, a cutoff-uniform positive residue, a cutoff-uniform true sector gap, and an Osterwalder–Schrader limit, then its limiting positive spectral measure contains an isolated nonzero atom. With an isolated energy-momentum mass shell and rotational covariance, that atom is a stable particle.
5. **The remaining open theorem.** One must prove that a source-carrying renormalization-group trajectory keeps, in physical units, a nonzero mass, nonzero residue, and nonzero isolation gap while \(a\to0\). This is not in WORKHOUSE or in the collected literature. It is a constructive four-dimensional Yang–Mills problem and cannot honestly be filled by perturbation theory, a numerical plateau, or topology alone.

The proposed proof route is therefore

\[
\boxed{
\begin{gathered}
\text{neutral electric-shell theorem}
\;\Longrightarrow\;
\text{volume-uniform three-sheet Riesz patch}
\\
\Longrightarrow\;
\text{connected composite-quasiparticle theorem at fixed }a
\\
\Longrightarrow\;
\text{source-carrying RG particle domain}
\;\Longrightarrow\;
\text{positive-measure pole persistence}
\\
\Longrightarrow\;
\text{OS reconstruction + isolated mass hyperboloid}
\;\Longrightarrow\;
\text{stable }1^{+-}\text{ particle.}
\end{gathered}}
\]

The finite-lattice input to the first arrow is rigorous; the spectral arrow remains conditional on the stated Yarotsky import and normalization. The last continuum-uniform arrow is the decisive unsolved step.

---

## 1. Exact finite-lattice starting point

On the spatial cubic torus \(T_L^3\), \(L\ge3\), use the WORKHOUSE convention

\[
H_{0,L}=\frac12\sum_e(-\Delta_e).
\]

A spin-network edge in the \(SU(3)\) irrep with Dynkin labels \((p,q)\) contributes

\[
e_{p,q}=\frac12C_2(p,q)
=\frac{p^2+q^2+pq+3p+3q}{6}.
\]

The smallest nonzero value is \(2/3\), attained only by \(3=(1,0)\) and \(\bar3=(0,1)\). Every other nontrivial irrep costs at least \(3/2\) per occupied edge.

An elementary fundamental plaquette has four occupied edges, so

\[
E_F=4\cdot\frac23=\frac83.
\]

For each spatial plaquette \(p\), charge conjugation exchanges its fundamental and antifundamental loop states. The normalized odd combination is

\[
|p,-\rangle=\frac{|p,3\rangle-|p,\bar3\rangle}{\sqrt2}.
\]

There are \(3L^3\) spatial plaquettes, and these states are orthonormal. Let

\[
P_{1,-}=\sum_p|p,-\rangle\langle p,-|,
\qquad \operatorname{rank}P_{1,-}=3L^3.
\]

This complete shell must be distinguished from the WORKHOUSE homological carrier inside it. The carrier has total rank \(L^3+2\): its fiber has rank one for \(k\ne0\) and rank three at \(\Gamma\). The ambient one-plaquette fiber is three-dimensional, and at \(\Gamma\) the carrier line and its two sibling incidence branches coalesce.

---

## 2. Why the unrestricted claim is false

For a direction \(\mu\) and transverse position \(a_\perp\), let

\[
T_{\mu,a_\perp}
=\operatorname{Tr}\prod_{n=0}^{L-1}
U_{a_\perp+n\hat\mu,\mu}
\]

be a straight fundamental winding Wilson loop. Its charge-odd combination

\[
T^-_{\mu,a_\perp}
=\frac{T_{\mu,a_\perp}-\overline T_{\mu,a_\perp}}{\sqrt2}
\]

is gauge invariant, nonzero, and \(C=-\). Every one of its \(L\) links is fundamental, hence

\[
H_0T^-_{\mu,a_\perp}=\frac{2L}{3}T^-_{\mu,a_\perp}.
\]

Therefore:

| \(L\) | winding-loop energy | consequence |
|---:|---:|---|
| 3 | \(2\) | a \(C=-\) state lies below the plaquette shell |
| 4 | \(8/3\) | extra states are exactly degenerate with the plaquette shell |
| 5 | \(10/3\) | extra states lie between the plaquette shell and \(4\) |
| 6 | \(4\) | the first winding state reaches the proposed complement threshold |

At \(L=4\), the \(3L^2=48\) straight charge-odd torelons alone enlarge the \(8/3\) eigenspace beyond \(P_{1,-}\).

Thus the unrestricted inequality

\[
Q(H_0-8/3)Q\ge\frac43Q
\]

is false. The correct physical repair is to work in the trivial \(\mathbb Z_3\) one-form-charge block. Contractible plaquette dynamics preserves this block, and it is the natural sector for glueballs rather than winding flux tubes.

---

## 3. Sharp neutral electric-shell theorem

Let \(\mathcal H^-_{L,0}\) be the gauge-invariant, \(C=-\), trivial-\(\mathbb Z_3\)-one-form-charge Hilbert space. Let \(Q_{1,-}=1-P_{1,-}\) within this space.

### Theorem 1 — exact sub-\(4\) classification

For every \(L\ge3\),

\[
\boxed{
\mathbf1_{(-\infty,4)}
\!\left(H_{0,L}|_{\mathcal H^-_{L,0}}\right)=P_{1,-}.}
\]

Equivalently,

\[
\boxed{Q_{1,-}H_{0,L}Q_{1,-}\ge4Q_{1,-}}
\]

and

\[
\boxed{
Q_{1,-}(H_{0,L}-8/3)Q_{1,-}
\ge\frac43Q_{1,-}.}
\]

The constant \(4/3\) is sharp.

### Proof

Peter–Weyl theory gives an orthogonal spin-network basis. Suppose a nonvacuum spin network has electric energy \(E<4\). Because every occupied edge costs at least \(2/3\), its support has at most five occupied edges.

Gauss law forbids a degree-one support vertex: a single nontrivial irrep contains no invariant vector. Hence every connected component of the support has minimum degree at least two.

A connected cubic-lattice support with at most five edges and no leaves must be a cycle. For \(L\ge4\), the graph has no triangles, and the smallest non-cycle graph of minimum degree two is a theta graph with at least six edges. For \(L=3\), the only five-edge branched simple graph of minimum degree two is \(K_4\setminus e\), which contains two triangles sharing an edge; it cannot embed because each edge of the cubic three-torus belongs to only one axial three-cycle. A winding triangle itself is still a cycle and is handled by center charge below. Two disconnected nontrivial components require at least \(3+3=6\) edges.

At every degree-two vertex,

\[
\operatorname{Inv}(V_\lambda\otimes V_\mu)
\cong\operatorname{Hom}(V_\lambda^*,V_\mu).
\]

Schur's lemma therefore forces one irrep to propagate consistently around the cycle. If that irrep is not \(3\) or \(\bar3\), each edge costs at least \(3/2\); even a three-edge winding cycle then costs \(9/2>4\). Thus every state with \(E<4\) is a fundamental or antifundamental simple cycle of length at most five.

The edge trialities form a \(\mathbb Z_3\)-valued 1-cycle. Its homology class is the one-form center charge. Lift the geometric cycle to \(\mathbb Z^3\). Its endpoint displacement is \(Ln\), where \(n\in\mathbb Z^3\) is the winding vector. Trivial center charge means \(n=3m\). A path of at most five edges cannot have a nonzero displacement of length at least \(3L\ge9\), so \(n=0\).

The lifted cycle is therefore closed in the ordinary cubic lattice. That lattice is bipartite, so the cycle is even. A simple closed cycle of length at most five has length four, and every four-cycle is an elementary plaquette boundary. Its charge-odd state is precisely \(|p,-\rangle\). This proves the spectral identity.

A fundamental \(1\times2\) rectangle has six occupied edges and energy

\[
6\cdot\frac23=4.
\]

Its nonzero charge-odd combination is neutral and lies outside \(P_{1,-}\). Hence the complement threshold \(4\), and the gap \(4-8/3=4/3\), are exact. ∎

### Audited edge cases

- An \(SU(3)\) baryonic \(\epsilon\)-vertex uses three fundamental lines. After the five-edge \(K_4\setminus e\) possibility is excluded by the cubic embedding argument above, any embeddable closed baryonic support has at least six occupied edges, so its energy is at least \(4\).
- On \(L=3\), a pair of oppositely charged length-three torelons is neutral but costs \(2+2=4\).
- If opposite winding strands occupy the same geometric links, their nontrivial fusion channel is adjoint; three adjoint edges cost \(9/2\).
- Higher representations only increase the energy.

This theorem is a new analytical consequence of the repo's conventions and representation data. It is not claimed as a pre-existing WORKHOUSE certificate.

---

## 4. A conditional volume-uniform Riesz patch at fixed lattice spacing

The raw perturbation \(u\sum_pv_p\) is extensive: its ordinary norm grows with the volume. A global finite-dimensional perturbation estimate therefore cannot be used uniformly in \(L\).

The useful imported result is Theorem 1 of D. A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*. It explicitly permits possibly infinite-dimensional site Hilbert spaces and unbounded nonnegative onsite Hamiltonians, while requiring bounded finite-range interactions. Group the three outgoing links at each vertex into one tensor-product cell and rescale

\[
\widehat H_L=\frac32H_L,
\qquad
\epsilon(u)=\sup_x\|\widehat\phi_x(u)\|.
\]

The rescaled one-cell excitation gap is at least one. The finite regrouping changes the range-dependent constants but not their volume independence. The paper formulates the displayed setup with empty boundary conditions and notes that other boundary conditions can be used; a formal import still needs to state and prove the uniform periodic-torus adaptation. Gauge restriction is not part of Yarotsky's theorem.

For the vacuum-subtracted Hamiltonian

\[
\widetilde H_L(u)=H_L(u)-E_{0,L}(u),
\]

Yarotsky supplies constants \(c_1,c_2\), depending on interaction range but not on \(L\), such that, when \(\epsilon(u)<c_1\),

\[
\operatorname{Spec}\widetilde H_L(u)
\subset
\bigcup_{a\in\operatorname{Spec}H_{0,L}}
\{z:|z-a|\le\lambda a\},
\qquad
\lambda=c_2\epsilon(u).
\]

The displayed inclusion has been translated back from \(\widehat H_L\) to the WORKHOUSE energy normalization; its relative widths are unchanged. The constants \(c_1,c_2\) are existence constants, not published numerical constants.

### Explicit \(SU(3)\) separation check

In units of \(1/6\), \(E_F=16/6\). The nearest distinct values in the additive kinematic electric spectrum are

\[
\frac{14}{6}=\frac{10+4}{6}
\quad\text{and}\quad
\frac{17}{6}=\frac{9+4+4}{6}.
\]

Indeed, the one-link Casimir numerators below \(18\) are \(0,4,9,10,16\); taking their additive semigroup gives \(14,16,17\) as the consecutive attainable numerators around \(16\). This also checks that no hidden one-link or multi-link value occurs at \(15/6\).

Therefore

\[
\theta_F
=\inf_{a\ne E_F}\frac{|a-E_F|}{a+E_F}
=\frac1{33}.
\]

If \(\epsilon<c_1\) and

\[
\boxed{\lambda<\frac1{33},}
\]

the complete \(E_F\) patch is disjoint from every other kinematic patch, uniformly in \(L\).

One explicit Riesz contour is

\[
\Gamma_F:\quad |z-E_F|=\rho,
\qquad
\rho=\frac{1-\lambda}{12}.
\]

Its distance from the spectrum is at least

\[
d_\Gamma=\frac{1-33\lambda}{12},
\]

so

\[
\sup_{z\in\Gamma_F}
\|(\widetilde H_L-z)^{-1}\|
\le\frac{12}{1-33\lambda}.
\]

Gauge transformations, charge conjugation, translations, and one-form center charge commute with the Hamiltonian. Hence the Riesz projection

\[
\Pi_{1,L}(u)
=\frac{1}{2\pi i}\oint_{\Gamma_F}
(z-\widetilde H_L(u))^{-1}\,dz
\]

restricts to the neutral physical \(C=-\) block. At \(u=0\), Theorem 1 identifies that restricted patch with \(P_{1,-}\). Assume both smallness conditions remain valid along the path \(t\mapsto tu\), \(0\le t\le1\), and use the analytic simple ground energy. Finite-volume analytic continuation then gives

\[
\boxed{
\operatorname{rank}\!\left(
\Pi_{1,L}(u)|_{\mathcal H^-_{L,0}}
\right)=3L^3}
\]

through this all-orders, small-local-norm strong-coupling domain. This rank statement is for the restricted physical projection, not for the full kinematic Riesz patch.

### Conditional conclusion of the import

Once the periodic-torus adaptation, exact local-interaction normalization, and pathwise smallness assumptions are established, this is a volume-uniform, all-orders isolation mechanism for the **complete \(E_F\) kinematic electric patch** at fixed lattice spacing. Only after restriction to the neutral physical \(C=-\) block does Theorem 1 identify it as the rank-\(3L^3\) one-plaquette island. The mechanism is substantially stronger than a finite-order truncated effective Hamiltonian, but it is not a continuation beyond its small-local-norm domain.

### What it does not prove

- It does not identify the WORKHOUSE homological vector with one individual all-orders sheet.
- It does not by itself prove a thermodynamic one-particle representation or a nonzero local-source residue.
- It does not continue the patch from strong coupling to the continuum scaling region.
- Yarotsky's separate quasiparticle theorem is not directly applicable: it assumes a nondegenerate one-site excitation satisfying a nonresonance condition, whereas this object is a four-link, three-component, Gauss-law composite.

---

## 5. Why the proof must transport the entire three-component cluster

For each fixed \(L\), the WORKHOUSE second-order incidence calculation gives the \(u\to0\) expansion

\[
4t_Nu^2\sin^2\frac{\pi}{L}+O(u^3),
\]

whose displayed leading term scales like \(L^{-2}\). An unqualified \(O(u^3)\) remainder may dominate at fixed \(u\) as \(L\to\infty\), so this formula alone is not an all-orders \(L^{-2}\) theorem. At second order the three orientation branches meet at \(\Gamma\); independently, the normalized homological Bloch source is singular there as an exact incidence fact.

Consequently a volume-uniform rank-one Riesz contour around only the homological line is not justified and already fails at second order. The safe proof object is:

- rank \(3L^3\) in position space;
- rank three in each momentum fiber;
- externally isolated from the rest of the physical spectrum;
- internally allowed to touch and split.

The carrier source can then be projected **into** this exact cluster. This does not produce an all-orders invariant carrier eigenline. At zero momentum the three-dimensional fiber can realize one cubic \(T_1\) triplet. Away from rest, a nonzero residue for the cluster is not automatically a residue for one particular internal sheet.

---

## 5A. What the attached Off-Axis Ledger changes

The attached ledger concerns contradiction C2: the shape coefficient \(C_{\rm shp}\)—not charge conjugation—in the fourth-order Rayleigh quotient **inside** the one-plaquette cluster. It does not settle C2. The historical saved kernel, the balanced continuation, and the v10a.26 computation remain distinct evidentiary objects, and none is promoted here.

A separate read-only exact-arithmetic check reproduced the 189 records, semantic SHA-256 `48a422a517c7c1e70b84fd88a0773943f81ae3f9bfafadbe2304f8eb7d2e9b77`, the historical \(\alpha_3=5/12\), and

\[
\beta_3^{\rm bal}-\beta_3^{\rm hist}=\frac{25}{64}.
\]

It also confirmed that the scalar denominator \(D_{34}(N^2)\) vanishes at \(N=2,3,4\) but not at \(N=5,6\). These are internal algebra and provenance checks. They do not establish that the \(-25/64\) physical \(SU(3)\) correction came from an independent pipeline rather than being defined or inherited within a shared lineage.

The ledger's 189-record channel table and its exact \(B=D=0\) cancellations also reproduce, but one downstream inference does not follow from that table. In its own units,

\[
A_{\rm total}=A_{\rm normal}-4x,
\]

because the mixed \((0,1,1)\) block contributes \(-4x\) to \(A\). Agreement on total \(A\) therefore does **not** by itself pin the normal-channel amplitude unless the mixed contribution is fixed independently. The channel localization remains useful, but its claim that the normal channel is already settled cannot be used as a proof premise.

Using the WORKHOUSE shape variables, the disputed contribution is

\[
\Phi_C(k)=4\frac{e_2(k)}{q_a(k)},
\qquad
\delta\varepsilon_4(k)
=4\,\Delta C_{\rm shp}\frac{e_2(k)}{q_a(k)}.
\]

Its continuous extension vanishes at \(\Gamma\), and it vanishes identically on every axial cut. Varying \(C_{\rm shp}\) therefore cannot change the fourth-order rest coefficient, the one-plaquette analytic \(T_1^{+-}\) assignment, the incidence rank, or the exact external electric gap. This does not independently certify the physical rest coefficient or operator overlap. The disputed term can change off-axis splittings, internal sheet ordering, finite-volume momentum spacings, quantitative multiparticle thresholds, and any quantitative claim of rotational or relativistic dispersion.

This sharpens the division of labor in the proof:

- The conditional Yarotsky mechanism depends on the unperturbed electric spectrum and the norm of the **exact local interaction**, not on \(C_{\rm shp}\). Its rank-\(3L^3\) restricted island and contour bound are therefore independent of which C2 value is chosen.
- A rank-one or individual-sheet theorem cannot use either disputed value as input. Near \(\Gamma\), the second-order sibling splitting is \(O(u^2|k|^2)\), while the disputed correction is \(O(u^4|k|^2)\), smaller by \(O(u^2)\) wherever the fixed-order expansion is uniform. The rank-one obstruction instead comes from exact touching at \(k=0\), the shrinking finite-volume momentum spacing, and the absence of a volume-uniform internal contour.
- A marked connected expansion must bound absolute activities before cancellations. If that exact expansion converges, its fourth-order Taylor coefficient is unique and C2 is resolved as a by-product; choosing a candidate coefficient cannot establish convergence.
- C2 does not settle or supply the uniform source-residue, true-threshold, OS, or pole-persistence estimates. It enters the still-open momentum-resolved, threshold, and rotation-restoration portions of the continuum bridge.

There is also a useful robustness check. Conditional on the common \(A=5/48\) and on \(B=D=0\), positivity of \(q_a\) and

\[
0\le\frac{e_2}{q_a^2}\le\frac13
\]

give the worst directional fourth-order curvature

\[
A+\frac43C_{\rm shp}.
\]

For the historical, balanced, and v10a.26 values quoted in the ledger, this is approximately \(0.0401\), \(0.0726\), and \(0.0772\), respectively. Thus none of the three candidates destabilizes the local \(\Gamma\) minimum within that shared truncated shape model. This comparison is a robustness envelope, not an adjudication and not an all-orders statement.

The theorem-safe conclusion is:

> The historical \(C_{\rm shp}\) is exact for the saved 189-record kernel, while identification of the physical fourth-order off-axis coefficient remains unadjudicated and v10a.26 remains numerical. This leaves the carrier's physical nonzero-momentum dispersion and quantitative internal bandwidth open. Varying C2 leaves the exact lower-order carrier structure, the one-plaquette analytic rest-frame assignment, and the external electric gap unchanged; the external Riesz-cluster mechanism remains conditional, and the rest coefficient is unchanged by C2 but not thereby certified.

---

## 6. The fixed-spacing composite-quasiparticle theorem to prove

The next theorem should be a composite, gauge-invariant extension of Yarotsky's quasiparticle construction.

The physical target space and the coefficient space are

\[
\mathscr K_L:=\mathcal H^-_{L,0},
\qquad
\mathscr S_L:=\ell^2(\Lambda_L)\otimes\mathbb C^3.
\]

The restriction to \(\mathscr K_L\) is essential: on the full Hilbert space the even vacuum lies below the target island, so the one-sided complement bound used below would be false. Let \(\Omega_L(u)\) be the exact even vacuum in the full physical space and \(O_{x,\alpha}\), \(\alpha=1,2,3\), normalized oriented charge-odd plaquette sources. Their action on the vacuum lies in \(\mathscr K_L\). Define \(J_L:\mathscr S_L\to\mathscr K_L\) and \(G_L:\mathscr S_L\to\mathscr S_L\) by

\[
J_Lf=\sum_{x,\alpha}f_{x,\alpha}O_{x,\alpha}\Omega_L(u),
\qquad G_L=J_L^*J_L.
\]

The exact identity

\[
\widetilde H_LO_{x,\alpha}\Omega_L
=[H_L,O_{x,\alpha}]\Omega_L
\]

holds provided \(O_{x,\alpha}\operatorname{Dom}H_L\subset\operatorname{Dom}H_L\). It cancels Hamiltonian terms spatially disconnected from the marked source in the marked action. This is the key starting point for removing volume divergence; it does not by itself prove uniform bounds for \(G_L\), the source-complement coupling, or the self-energy. Subtracting the vacuum energy from a bare-vacuum calculation is not enough.

For a translation-invariant \(3\times3\) displacement kernel \(K(r)\), introduce the connected norm

\[
\|K\|_\mu
=\max\!\left\{
\max_\alpha\sum_{r,\beta}e^{\mu d(0,r)}|K_{\alpha\beta}(r)|,
\max_\beta\sum_{r,\alpha}e^{\mu d(0,r)}|K_{\alpha\beta}(r)|
\right\}.
\]

The multiplication constant of this Banach algebra is independent of \(L\), but a kernel is not automatically uniformly bounded in it. On a finite torus the norm controls the discrete real-momentum fibers. Complex-strip analyticity follows only after constructing a consistent exponentially summable infinite-volume kernel or periodization limit.

### The needed marked-cluster hypothesis

Prove, uniformly in \(L\), that the ordinary, one-source, two-source, and marked-resolvent polymer activities obey an operator- and energy-weighted Kotecký–Preiss-type bound, schematically

\[
\sup_b\sum_{\Gamma\ni b}
e^{\mu\operatorname{diam}\Gamma+\nu|\Gamma|}
\sup_{z\in D}
\left(|w_\Gamma(z)|+r_D|\partial_zw_\Gamma(z)|\right)
\le\eta<\eta_*.
\]

Here \(D\) is an open complex domain that will contain the closed target disk introduced below, and \(r_D\) is a fixed scale no larger than its distance to the complement spectrum. The polymer \(\Gamma\) must be supplied with a precise incompatibility relation, and the activities must control graph domains and insertions of the unbounded electric Hamiltonian; scalar absolute weights alone do not suffice. The completed bound should imply

\[
\|G_L-I\|_\mu\le g<1,
\]

If \(g<1\), define the orthonormalized source map and its projections by

\[
W_L=J_LG_L^{-1/2},
\qquad
P_L=W_LW_L^*,
\qquad
Q_L=1_{\mathscr K_L}-P_L.
\]

Then define

\[
A_L=W_L^*\widetilde H_LW_L,
\qquad
B_L=Q_L\widetilde H_LW_L.
\]

Here \(W_L:\mathscr S_L\to\mathscr K_L\); \(P_L,Q_L,\widetilde H_L\) act on \(\mathscr K_L\); \(G_L,A_L,F_L,\Sigma_L\) act on \(\mathscr S_L\); and \(B_L:\mathscr S_L\to Q_L\mathscr K_L\). The same connected bounds must then imply

\[
\|A_L-E_FI\|_\mu\le a,
\qquad
\|B_L^*B_L\|_\mu^{1/2}\le b.
\]

The self-energy cannot be assumed before its complement resolvent has been proved to exist. First use the Section 4 Riesz patch restricted to \(\mathscr K_L\), denoting the restriction again by \(\Pi_{1,L}\), and establish ordered sector bounds

\[
\operatorname{Spec}\!\left(
\widetilde H_L|_{\operatorname{Ran}\Pi_{1,L}}
\right)\subset[m_-,m_+],
\qquad
\operatorname{Spec}\!\left(
\widetilde H_L|_{\operatorname{Ran}(1_{\mathscr K_L}-\Pi_{1,L})}
\right)\subset[M_-,\infty),
\quad M_->m_+.
\]

Together with \(\|A_L-E_FI\|\le a\), \(\|B_L\|\le b\), a sufficient non-circular source–patch angle bound is

\[
\delta_A:=M_--(E_F+a)>0,
\qquad
q_0:=\frac{b}{\delta_A}<1.
\]

Indeed, \(R=(1-\Pi_{1,L})W_L\) obeys the Sylvester equation

\[
(1-\Pi_{1,L})\widetilde H_L(1-\Pi_{1,L})R
-RA_L
=(1-\Pi_{1,L})B_L.
\]

The ordered spectral separation gives the actual source–patch angle

\[
q_{\rm ang}:=\|(1-\Pi_{1,L})W_L\|=\|R\|\le q_0.
\]

Because \(g<1\) makes \(J_L\) injective, \(P_L\) and \(\Pi_{1,L}\) have the same finite rank; hence \(\|\Pi_{1,L}-P_L\|\le q_0\). It follows that

\[
Q_L\widetilde H_LQ_L\ge M_Q^-Q_L,
\qquad
M_Q^-=(1-q_0^2)M_-+q_0^2m_-.
\]

Let

\[
\overline D_r:=\{z\in\mathbb C:|z-E_F|\le r\},
\qquad r<M_Q^--E_F,
\]

and choose \(D\) as an open neighborhood of \(\overline D_r\) that remains in the complement resolvent set. Then the inverse on \(Q_L\mathscr K_L\) obeys

\[
R_{Q,L}(z)
:=\left(
Q_L(\widetilde H_L-z)Q_L|_{Q_L\mathscr K_L}
\right)^{-1},
\qquad
\|R_{Q,L}(z)\|
\le\frac1{M_Q^--E_F-r}.
\]

Only now define the connected Feshbach self-energy

\[
\Sigma_L(z)
=B_L^*R_{Q,L}(z)B_L
\]

and prove

\[
\sup_{z\in D}\|\Sigma_L(z)\|_\mu\le s,
\qquad
\sup_{z\in D}\|\partial_z\Sigma_L(z)\|_\mu\le\kappa<1.
\]

\[
F_L(z)=A_L-z-\Sigma_L(z)
\]

is the exact connected Feshbach matrix.

### Conditional conclusion

If those bounds and finite-volume consistency estimates hold, with

\[
g<1,\qquad \delta_A>0,\qquad q_0<1,\qquad \kappa<1,
\qquad
\max\{\lambda E_F,a+s\}<r<M_Q^--E_F,
\]

then:

1. \(G_L^{-1/2}\) exists in the same connected algebra, so the source translates can be orthonormalized without losing exponential locality.
2. The exact rank-\(3L^3\) Riesz patch is uniformly close to the dressed source space.
3. In each momentum fiber, \(\det F(E,k)=0\) defines a three-sheet isolated spectral cluster. An individual energy sheet is locally analytic only where its root is simple.
4. With

   \[
   R_{\rm cl}(k)=J_L(k)^*\Pi_{1,L}(k)J_L(k),
   \qquad
   q_{\rm ang}=\|(1-\Pi_{1,L})W_L\|\le q_0,
   \]

   the total cluster spectral weight has the positive lower bound

   \[
   R_{\rm cl}(k)
   \succeq(1-g)(1-q_{\rm ang}^2)I_3
   \succeq(1-g)(1-q_0^2)I_3.
   \]

   This is not the residue of any particular internal pole.
5. If nonwrapping activities stabilize and one proves an exponential periodization estimate, wrapping clusters are exponentially small in \(L\) and the effective kernels have a thermodynamic limit. To turn that kernel limit into an actual isolated lattice band one must also construct the limiting GNS Hamiltonian and source isometry and prove resolvent convergence on the enclosing contour; integrating those resolvents then gives a nonzero limiting Riesz projection. Only with these additions is the conclusion a rank-three, translation-covariant isolated **lattice band**, not yet a relativistic particle.

The new fixed-spacing work therefore includes the marked excited-resolvent estimate, the non-circular source–patch angle bound, graph-domain control for the unbounded electric term, finite-volume consistency, and the composite/Gauss-law construction. Ordinary vacuum clustering and Yarotsky's nondegenerate one-site quasiparticle theorem do not supply these results.

---

## 7. Exact positive-measure pole-persistence lemma

A bare operator norm is not the right continuum quantity. Use a separated-time-normalized source so ultraviolet contact terms cannot fake or erase its pole fraction.

Let \(\xi=(a,L)\) run along a specified thermodynamic/continuum net. Let \(H_\xi\ge0\), \(\Omega_\xi\), and three vacuum-subtracted carrier sources be supplied by reflection-positive lattice theories. At finite volume take their zero-spatial-momentum projections \(O^{(0)}_{\xi,i}\), so their spectral measures lie in the rest-frame \((\mathbf P=0,T_1^{+-})\) sector. Fix a physical \(t_0>0\) and define

\[
\psi_{\xi,i}
=e^{-t_0H_\xi/2}(O^{(0)}_{\xi,i})^\dagger\Omega_\xi.
\]

Assume their separated-time Gram matrix is strictly positive definite. Renormalize the resulting source vectors so that

\[
\langle\psi_{\xi,i},\psi_{\xi,j}\rangle=\delta_{ij}.
\]

Their finite positive matrix spectral measure is

\[
\nu_\xi(B)_{ij}
=\langle\psi_{\xi,i},E_{H_\xi}(B)\psi_{\xi,j}\rangle,
\qquad
\nu_\xi([0,\infty))=I_3.
\]

The separated-time correlator is its Laplace transform:

\[
\widehat C_\xi(s)
=C_\xi(t_0+s)
=\int_0^\infty e^{-sE}\nu_\xi(dE).
\]

### Theorem 2 — an isolated pole survives a positive limit

Assume:

1. \(\widehat C_\xi(s)\to\widehat C(s)\) locally uniformly for \(s\ge0\), including \(s=0\).
2. Closed intervals \(I_\xi=[m_\xi^-,m_\xi^+]\) converge in Hausdorff distance to \(\{M\}\), where \(M\in(0,\infty)\).
3. The carrier weight satisfies

   \[
   \nu_\xi(I_\xi)\succeq z_*I_3,
   \qquad z_*>0.
   \]

4. For a fixed \(\Delta_*>0\), define

   \[
   A_\xi(\Delta_*)
   =\{E\notin I_\xi:
   0<\operatorname{dist}(E,I_\xi)<\Delta_*\}.
   \]

   The carrier measure has the uniform empty annulus

   \[
   \nu_\xi(A_\xi(\Delta_*))=0.
   \]

Then the limiting positive matrix measure exists and obeys

\[
\boxed{\nu(\{M\})\succeq z_*I_3}
\]

and

\[
\nu\big((M-\Delta_*,M+\Delta_*)\setminus\{M\}\big)=0.
\]

If the limiting source is one irreducible \(T_1\) copy, cubic covariance and Schur's lemma give

\[
\nu(\{M\})=z_GI_3,
\qquad z_G\ge z_*.
\]

### Proof

For each \(v\in\mathbb C^3\), define the positive scalar measure

\[
\nu_{\xi,v}(B)=v^*\nu_\xi(B)v.
\]

The measures have uniformly bounded mass, and convergence of their Laplace transforms including \(s=0\) gives weak convergence to a positive measure \(\nu_v\). Polarization reconstructs the matrix measure \(\nu\).

For \(\epsilon>0\), let \(F_\epsilon=[M-\epsilon,M+\epsilon]\). Far enough along the net, \(I_\xi\subset F_\epsilon\), so

\[
\nu_{\xi,v}(F_\epsilon)\ge z_*\|v\|^2.
\]

The closed-set Portmanteau inequality yields

\[
\nu_v(F_\epsilon)
\ge\limsup_\xi\nu_{\xi,v}(F_\epsilon)
\ge z_*\|v\|^2.
\]

Letting \(\epsilon\downarrow0\) and using continuity from above gives

\[
v^*\nu(\{M\})v\ge z_*\|v\|^2.
\]

For any open interval whose closure lies in the punctured annulus, the finite-cutoff measures eventually vanish. The open-set Portmanteau inequality makes the limiting measure vanish there too. A countable rational cover gives the full empty punctured neighborhood. ∎

### Necessary strengthening for a physical theorem

A gap in the chosen source measure can miss a nearby “dark” state. For perturbative stability and an actual sectoral particle theorem one must require the true gap

\[
\operatorname{dist}\!\left(
I_\xi,
\operatorname{Spec}(H_\xi|_{\mathbf P=0,T_1^{+-}})\setminus I_\xi
\right)\ge\Delta_*.
\]

The measure lemma proves a rest-frame pole in the correlator. The true sector gap excludes invisible nearby states and is necessary for Riesz stability. Transporting a projector across different cutoffs additionally requires identified Hilbert spaces and norm-resolvent convergence uniformly on an enclosing contour, after which one integrates the convergent resolvents. Uniform contour bounds without convergence do not transport a projector; strong-resolvent convergence alone does not preserve finite rank. To retain exactly one rest-frame triplet, require that \(E_{H_\xi}(I_\xi)\) restricted to \((\mathbf P=0,T_1^{+-})\) has rank three and that the identified Riesz projectors converge in norm.

---

## 8. From an energy atom to a relativistic particle

The finite-volume zero-momentum atom is only a diagnostic: exact-momentum states are not normalizable in infinite volume. The limiting full family of Schwinger functions must satisfy the Osterwalder–Schrader conditions: Euclidean covariance, reflection positivity, regularity, symmetry, clustering, and a unique vacuum.

OS reconstruction then gives a Hilbert space, positive Hamiltonian, vacuum, and positive-energy Poincaré representation. In the reconstructed infinite-volume theory one must use momentum-smeared sources and the joint energy-momentum spectral measure. A delta component at \(\mu^2=M^2\) in a source's Källén–Lehmann invariant-mass measure proves that the source has a nonzero mass-\(M\) component. It does not exclude dark or accumulating spectrum. A stable one-particle theorem additionally requires the joint spectrum to contain a nonzero isolated positive-energy mass hyperboloid

\[
p^2=M^2,
\qquad p^0>0,
\]

with a gap in invariant mass to all remaining spectrum. This supplies

\[
E(\mathbf p)=\sqrt{M^2+\mathbf p^2}
\]

and, under the standard locality and regularity hypotheses, permits the Haag–Ruelle construction of scattering states. It does not by itself establish asymptotic completeness.

A cubic \(T_1\) label alone does not prove spin one; higher spins also subduce to \(T_1\). A clean sufficient condition is that the continuum carrier source transforms as an axial vector:

\[
U(R)O_iU(R)^{-1}
=\sum_jD^{(1)}_{ji}(R)O_j,
\qquad R\in SO(3).
\]

Axial-vector covariance and nonzero residue imply at least a \(J=1\) subrepresentation. If the mass-shell fiber is exactly one three-dimensional spin-one polarization representation—multiplicity one—and the axial-vector source has residue \(z_GI_3>0\), the shell carries exactly one \(J=1\) particle species. If parity and charge conjugation remain exact symmetries of the limiting OS theory and act as \(P=+\), \(C=-\) on this shell, the result is a stable \(1^{+-}\) particle.

---

## 9. The proposed source-carrying RG particle domain

An action-only renormalization group can preserve partition functions while losing the operator residue. The RG object must be the pair “theory plus carrier source,” including every induced multilocal source term.

At each scale, assuming the separated-time source Gram matrix is strictly positive, define the normalized spectral source map by

\[
\Psi e_i=e^{-t_0H/2}O_i^\dagger\Omega,
\qquad \Psi^*\Psi=I_3.
\]

The blocking kernel must be compatible with time reflection and preserve reflection positivity; otherwise the coarse correlator need not possess a positive spectral measure.

At finite volume, define \(\mathfrak D_{\rm part}^{\rm fin}(I,\Delta,z)\) in the rest-frame sector \((\mathbf P=0,T_1^{+-})\) by:

1. a positive transfer structure and unique invariant vacuum;
2. exact \(T_1^{+-}\) source covariance;
3. a rank-three rest-frame Riesz island \(E_H(I)|_{\mathbf P=0,T_1^{+-}}\);
4. an ordinary-energy sector gap

   \[
   \operatorname{dist}\bigl(I,\operatorname{Spec}(H|_{\mathbf P=0,T_1^{+-}})\setminus I\bigr)
   \ge\Delta>0;
   \]

5. a source residue

   \[
   \Psi^*E_H(I)\Psi\succeq zI_3,
   \qquad z>0.
   \]

In infinite volume, clustering and a unique vacuum are required, and the Hamiltonian projection must be replaced by the joint spectral projection

\[
\mathcal P_{M^2}
=E_{P^\mu}\!\left(
\{p:p^0>0,\ p^2\in I_{M^2}\}
\right).
\]

The infinite-volume isolation is a gap in invariant mass, and the residue is evaluated with momentum-smeared normalized sources. The particle domain then requires a multiplicity-one spin-one mass shell rather than a finite-volume energy eigenspace.

For the continuum trajectory require, in physical units,

\[
0<m_-\le M_a\le m_+<\infty,
\qquad
\Delta_a\ge\Delta_*>0,
\qquad
z_a\ge z_*>0.
\]

Use a carrier source with a fixed physical spatial dressing radius \(\rho>0\), using a time-slice-supported construction such as spatial gradient flow. Four-dimensional flow would require a separate proof of reflection-positivity/OS compatibility. A fixed-link source shrinks to a point as \(a\to0\) and can lose all overlap even while the particle survives.

### Exact RG transfer identity

Write the exact identity first for **unnormalized** source correlators. Retaining generated quadratic and multilocal source terms does not automatically make the transformation close on three sources: the second derivative can contain an additive separated two-source kernel. One must either prove that this additive term vanishes and that the exact source transformation closes linearly on a three-dimensional space, or enlarge the source space until the transformation is linear.

In the square, three-dimensional closed case suppose the full second derivative gives, at separated times,

\[
\widetilde C_{k+1}(s)
=A_k\widetilde C_k(bs)A_k^*.
\]

and that the remaining kernel has a positive Hilbert-space realization. Uniqueness of Laplace transforms then gives

\[
\widetilde\nu_{k+1}
=A_k(d_b)_*\widetilde\nu_kA_k^*,
\qquad
(d_b)_*\nu(B)=\nu(B/b).
\]

Consequently a pole and an empty interval in **this source measure** scale as

\[
M_{k+1}=bM_k,
\qquad
\Delta^{\rm src}_{k+1}=b\Delta^{\rm src}_k,
\qquad
\widetilde R_{k+1}=A_k\widetilde R_kA_k^*.
\]

This identity does not transport the true sector gap or the rank of a sectoral Riesz projection. Those require an exact spectral equivalence for the full symmetry sector or a separate uniform sector theorem.

If the separated-time Gram matrices are strictly positive, put

\[
G_k=\widetilde C_k(0),
\qquad
C_k=G_k^{-1/2}\widetilde C_kG_k^{-1/2},
\]

and define

\[
B_k=G_{k+1}^{-1/2}A_kG_k^{1/2}.
\]

The exact identity at \(s=0\) gives \(B_kB_k^*=I_3\). Because the closed source map is square and three dimensional, \(B_k\) is unitary. Thus

\[
R_{k+1}^{\rm norm}
=B_kR_k^{\rm norm}B_k^*,
\]

and the eigenvalues of the normalized pole fraction are unchanged by an exact step. If the source space has instead been enlarged, \(B_kB_k^*=I\) may make \(B_k\) only a coisometry, and this eigenvalue conclusion need not hold. This shows why closure and the complete source map must both be controlled.

The particle domain may be fixed in physical units. If a separate sectoral spectral theorem transports its mass interval and true gap, then in dimensionless coarse-lattice units those data are scale indexed:

\[
I_{k+1}=bI_k,
\qquad
\Delta_{k+1}=b\Delta_k.
\]

For an approximate RG, Hamiltonian and source errors must be summable after physical rescaling. Errors that merely tend to zero step by step can accumulate without bound and rotate the source away from the particle.

### The exact open entry theorem

The decisive statement to prove is:

> Along a reflection-positive continuum scaling trajectory, the exact source-extended RG image of the \(SU(3)\) Wilson theory and a fixed-physical-radius WORKHOUSE carrier source enters and remains in a particle domain with uniform physical mass, invariant-mass gap, and normalized residue. At finite volume the control topology is norm-resolvent convergence plus source-vector norm; in infinite volume it is OS distributional convergence supplemented by the uniform invariant-mass and residue bounds. The full Schwinger family has an OS limit.

The entry theorem must additionally produce rest-frame intervals \(I_a\to\{M\}\) in Hausdorff distance and locally uniform convergence of the separated-time normalized correlators for \(s\ge0\), including \(s=0\). An OS distributional limit by itself does not state these hypotheses. With them, Theorem 2 supplies an isolated carrier pole. A particle follows only after the Section 8 joint energy-momentum mass-shell condition, invariant-mass isolation, full rotational covariance, and multiplicity-one spin identification are also proved. Without those estimates, the strong-coupling island may close, merge into a threshold, run to infinite physical mass, become massless, or lose carrier residue before the continuum is reached.

---

## 10. The shortest realistic proof campaign

### Phase A — close the fixed-spacing theorem

1. Formalize Theorem 1 in a proof assistant or as a certificate-checked spin-network enumeration, including the one-form-charge projector.
2. Pin the exact map between the WORKHOUSE strong-coupling coordinate and the local interaction norm appearing in Yarotsky's theorem.
3. Prove the marked polymer and excited-resolvent bounds for \(G,A,\Sigma,\partial_z\Sigma\).
4. Obtain the thermodynamic three-sheet Feshbach matrix and explicit nonzero carrier-residue bound.
5. Test the construction against explicit torelon and multi-loop sources so that the claimed external gap is a true sector gap, not only a carrier-measure gap.

### Phase B — build the continuum bridge

1. Replace the microscopic carrier by its fixed-physical-radius, symmetry-projected dressed version.
2. Block the **action and source together** with a reflection-positive exact or rigorously bounded RG.
3. Establish a compact RG domain with uniform physical mass, sector gap, and residue.
4. Prove tightness and OS convergence of the complete Schwinger family.
5. Prove an isolated mass hyperboloid and restored axial-vector covariance.

### Phase C — finish the particle theorem

Apply the positive-measure lemma, OS reconstruction, and Haag–Ruelle theory. The conclusion is then a stable carrier-descended \(1^{+-}\) particle, not merely a lattice eigenvalue or an exponential fit.

---

## 11. Falsifiers

The program fails if any one of the following occurs:

- a neutral \(C=-\) spin network below \(4\) exists outside the one-plaquette shell;
- the marked-resolvent expansion has a volume-divergent norm;
- the source Gram matrix develops a zero eigenvalue;
- a torelon, multi-glueball, or dark state closes the true sector gap;
- the physical pole residue tends to zero;
- the mass tends to zero or infinity in physical units;
- the isolated lattice cluster dissolves into continuum spectral weight;
- the continuum rotational multiplet is incompatible with \(J=1\);
- the source-extended RG errors are not summable.

These are proof gates, not implementation suggestions for the repository.

---

## 12. What has and has not been proved here

| Statement | Status |
|---|---|
| Unrestricted \(C=-\) shell gap | **Refuted** by exact winding-loop states |
| Neutral \(C=-\) spectrum below \(4\) equals \(P_{1,-}\) | **Analytically proved here** from spin networks, Gauss law, center charge, and cubic geometry |
| Neutral electric gap \(4/3\) | **Analytically proved and sharp** |
| Volume-uniform isolation of the full strong-coupling patch | **Imported conditionally** from Yarotsky once the periodic-torus adaptation, exact local-interaction normalization, and pathwise bounds \(\epsilon(tu)<c_1\), \(c_2\epsilon(tu)<1/33\) are established |
| Rank \(3L^3\) of the restricted perturbed patch | **Conditional finite-volume consequence** of the preceding imported isolation and analytic continuation |
| Thermodynamic carrier-descended quasiparticle | **Conditional** on the marked connected-resolvent theorem |
| Continuum pole-persistence lemma | **Proved here**, given its stated uniform positive-measure hypotheses |
| Uniform continuum mass, true gap, and residue | **Open** |
| Stable continuum \(1^{+-}\) particle | **Conditional** on the open RG-domain, OS, mass-hyperboloid, and rotation-restoration hypotheses |

This dossier does not claim a proof of four-dimensional continuum Yang–Mills existence or mass gap. The Clay Mathematics Institute continues to list that problem as unsolved. The contribution here is to replace one vague bridge with a corrected spectral sector, an exact finite-lattice gap theorem, a viable volume-uniform fixed-spacing mechanism, a rigorous pole-persistence lemma, and one sharply isolated continuum theorem target.

---

## 13. Primary references used in the bridge

- D. A. Yarotsky, [*Quasi-particles in weak perturbations of non-interacting quantum lattice systems*](https://arxiv.org/abs/math-ph/0411042).
- G. Dusson, I. M. Sigal, and B. Stamm, [*The Feshbach–Schur map and perturbation theory*](https://arxiv.org/abs/2105.02058).
- H. Shen, R. Zhu, and X. Zhu, [*A stochastic analysis approach to lattice Yang–Mills at strong coupling*](https://arxiv.org/abs/2204.12737).
- R. S. Schor, [*The energy-momentum spectrum of strongly coupled lattice gauge theories*](https://www.sciencedirect.com/science/article/pii/055032138490289X).
- M. Lüscher, [*Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories*](https://doi.org/10.1007/BF01614090).
- S. Bachmann, W. Dybalski, and P. Naaijkens, [*Lieb–Robinson bounds, Arveson spectrum and Haag–Ruelle scattering theory for gapped quantum spin systems*](https://arxiv.org/abs/1412.2970).
- Clay Mathematics Institute, [*Yang–Mills and the Mass Gap*](https://www.claymath.org/millennium/yang-mills-the-maths-gap/).

---

## 14. Read-only WORKHOUSE anchors

The analysis used the current governing theory, detailed formula, frontier, ledgers, and exact scripts in

work/WORKHOUSE-readonly/

as read-only evidence. No file in that clone was changed. This dossier is an external analytical artifact and is not a WORKHOUSE T0/T1 certificate.
