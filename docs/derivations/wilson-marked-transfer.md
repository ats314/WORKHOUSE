# Actual Wilson transfer: blocks, vacuum cancellation and uniform estimates

Continuation: [the complete shell and carrier transport](wilson-marked-shell-transport.md)
now supplies the three-step result using the hash-pinned September 5 actual
Wilson chart/activity/band proofs. The WT-6 discussion below records the earlier
stopping point. Its particular rooted coefficient-operator norm is not asserted
by the continuation; a full Hilbert-space complex estimate plus finite-order
locality supplies the sufficient weighted shell majorant instead.

This continuation implements the first part of the [selected graph route](../research/next-path-wilson-transfer-2026-09-08.md). The main new estimate controls an entire fixed-physical-time Wilson block, including arbitrarily many magnetic insertions, uniformly in the microscopic time step. It gives a convergent vacuum polymer expansion on an explicit, conservative small-coupling disc. The complete excited Riesz shell and its source frame require a further operator estimate, isolated in WT-6 below.

Verification is split by scope. [wilson_marked.py](../../src/workhouse/invariants/wilson_marked.py) reproduces finite noncommutative algebra, activation coefficients, cancellations, geometry and bound arithmetic. The operator norm and polymer arguments below are analytic derivations. The Lean lemmas formalize only their stated algebraic and scalar-inequality components. None of those finite checks alone establishes a Wilson carrier or a continuum theorem.

## WT-1. Exact physical-time blocks

Work first on a finite cubic spatial lattice with link Hilbert spaces. Let

\[
D_\epsilon=\sum_e k_{\epsilon,e},\qquad
k_{\epsilon,e}\Omega_e=0,\qquad
k_{\epsilon,e}|_{\Omega_e^\perp}\ge\delta>0.
\]

The uniform onsite gap is the input already used in section 9 of the [Wilson window note](../../paper/research_notes/G19_UNIFORM_WILSON_WINDOW_20260904.md). Fix a sufficiently small temporal-step family for which this input holds. No upper bound on an onsite energy is required here. Let `V=sum_p V_p`, with `V_p=chi_p+bar_chi_p` and `||V_p||<=v`; for SU(3) one may take `v=6`. Each plaquette acts on at most four links.

Keep the calibrated physical clock and the exact symmetric transfer:

\[
T_\epsilon(u)=e^{\tau uV/2}e^{-\tau D_\epsilon}e^{\tau uV/2},
\quad \tau=-\frac{2}{C_F}\log\lambda_F(\epsilon),
\quad \beta_s=2Nu\tau.
\]

Choose a fixed `t0>0`, restrict `0<tau<=tau0`, and set

\[
m=\lceil t_0/\tau\rceil,\qquad \ell=m\tau\in[t_0,t_0+\tau_0],
\qquad B_\epsilon(u)=T_\epsilon(u)^m.
\tag{WT1}
\]

Thus the number of microscopic steps can diverge while the block time stays bounded. If `A=exp(tau*u*V/2)` and `K=exp(-tau*D_epsilon)`, then

\[
(AKA)^m=A(KA^2)^{m-1}KA\qquad(m\ge1).
\]

The endpoint half factors must be retained. This identity holds in any associative monoid. It also shows that the sum of the magnetic insertion times in one block is exactly `ell`. The physical generator is `-log(B)/ell=-log(T)/tau`; blocking changes its representation, not the operator being studied.

## WT-2. An all-orders activated-block bound

For a finite set `I` of plaquette labels let `A(I)` be their union of link supports. Let `B(J)` be the exact block with only the interactions in `J` switched on, and define

\[
\Delta_I B=\sum_{J\subseteq I}(-1)^{|I|-|J|}B(J).
\]

For any finite total set of interactions, inclusion-exclusion gives `B= sum_I Delta_I B`. Since the free kinetic terms are onsite,

\[
\Delta_I B=C_I\otimes e^{-\ell D_{A(I)^c}},
\qquad
\boxed{\ \|C_I\|\le\prod_{p\in I}(e^{\ell|u|\|V_p\|}-1)
\le (e^{(t_0+\tau_0)v|u|}-1)^{|I|}.\ }
\tag{WT2}
\]

Here `C_I` acts only on `A(I)`. The empty set gives the free block, with scalar empty-support factor one.

**Proof.** Assign an independent variable to each interaction label. Expand every magnetic exponential in the exact block into its norm-convergent Taylor series. Keep each kinetic factor between the insertions; its norm is at most one, including on unbounded onsite Hilbert spaces. The norms of the multivariate coefficients are bounded coefficientwise by

\[
\prod_{\text{magnetic slots }s}\exp\!\left(t_s\sum_{p\in I}\|V_p\|x_p\right)
=\exp\!\left(\ell\sum_{p\in I}\|V_p\|x_p\right),
\qquad \sum_s t_s=\ell.
\]

This bound also holds for noncommuting interaction terms: the ordered words in each power are bounded before their scalar coefficients are collected. Inclusion-exclusion removes every word that omits any label in `I`. Summing the surviving positive scalar majorant is exactly the product in (WT2). The kinetic factors on `A(I)^c` commute with all the insertions and multiply to the displayed free evolution. This proves both assertions.

There is no factor proportional to `m`, `1/tau` or total spatial volume. This controls repeated insertions and all magnetic orders inside a block. For equal label norms, the coefficient of `x^n` in `(exp(x)-1)^k` is

\[
\frac1{n!}\sum_{j=0}^k(-1)^{k-j}\binom kjj^n
=\sum_{r_1+\cdots+r_k=n,\ r_i\ge1}\frac1{r_1!\cdots r_k!}.
\]

The exact check compares the two independent coefficient constructions. It does not replace the operator-series proof above.

## WT-3. Configurations and exact vacuum cancellation

Write `P_e=|Omega_e><Omega_e|`, `Q_e=1-P_e`. In each block with active set `I`, resolve the identity outside `A(I)` by choosing excited links `J subset A(I)^c`:

\[
W_{I,J}=C_I\otimes
\left(e^{-\ell D_J}Q_J\right)\otimes P_{(A(I)\cup J)^c},
\qquad B=\sum_{I,J}W_{I,J}.
\]

Consequently the product-boundary vacuum amplitude is the exact finite sum

\[
Z_{N,\Lambda}=\langle\Omega_0,B^N\Omega_0\rangle
=\sum_{\mathcal C}w(\mathcal C),\qquad
w(\mathcal C)=\langle\Omega_0,W_{I_N,J_N}\cdots W_{I_1,J_1}\Omega_0\rangle,
\]

with a uniform activity estimate

\[
|w(\mathcal C)|\le\alpha^{a(\mathcal C)}\beta^{b(\mathcal C)},\quad
\alpha=e^{(t_0+\tau_0)v|u|}-1,\quad \beta=e^{-\delta t_0},
\quad a=\sum_k|I_k|,\ b=\sum_k|J_k|.
\tag{WT3}
\]

Attach each active plaquette and each excited link in block `k` to both boundary times `k-1,k`. Two link-time vertices are adjacent when their times differ by at most one and their spatial links coincide or share a plaquette. The support of a configuration consists of its attached vertices. Its connected components define the polymers; compatibility means that their supports neither intersect nor have an adjacency edge between them.

For distinct compatible components the amplitude factorizes exactly. To see this, evolve the product vacuum one block at a time. A block acts independently on disjoint link factors. Whenever a component ceases to occupy a link, the next inactive step projects that link onto its one-dimensional vacuum. Later components using that link therefore see a fresh vacuum factor. Induction over the blocks proves `w(C1 union C2)=w(C1)w(C2)`. The same argument applies to the inclusion-exclusion operators, which factor over disjoint spatial active sets. Mere separation in time without the vacuum reset would not suffice; the exact check includes that negative control.

Insert a fixed bounded local observable by adding `exp(z O)` at a block boundary. Differentiating `log Z(z)` at `z=0` gives the normalized marked expectation. Disconnected unmarked components cancel between numerator and denominator. Equivalently, only clusters connected to the mark occur in the derivative of the logarithm. Two derivatives, after subtracting the product of one-point functions, require a cluster joining the two marks. This is an exact formal-series identity at every finite block number and spatial volume. WT-4 supplies a common domain in which the series converge and the normalization is nonzero.

## WT-4. A uniform convergent vacuum polymer expansion

Here is an explicit, deliberately loose counting bound for cubic lattices with nondegenerate plaquettes, including periodic `L>=3`.

Each link belongs to four plaquettes and has at most twelve spatial neighbors sharing a plaquette. Thus the link-time graph above has maximum degree

\[
d=3(12+1)-1=38.
\]

A fixed vertex can be incident to at most eight active plaquette/block labels and two excited-link/block labels. A fixed support of `s` vertices therefore has at most `2^(10s)` binary configuration assignments. A connected support of size `s` through a specified vertex has at most `d^(2s-2)` possibilities: fix a deterministic rooted spanning tree and encode its depth-first traversal as a walk of length `2s-2`. Different supports have different visited sets. These estimates also cover clusters wrapping a periodic volume.

One active plaquette contributes at most eight support vertices and one excited-link label at most two. Hence `s<=8a+2b<=8(a+b)`. If `rho=max(alpha,beta)<1`, each polymer satisfies `|w|<=rho^(s/8)`. For any fixed vertex `x`,

\[
\sum_{\chi\ni x}|w(\chi)|e^{2|\chi|}
\le\frac1{d^2}\sum_{s\ge1}r^s
=\frac{r}{d^2(1-r)},\qquad
r=d^2 2^{10}e^2\rho^{1/8}.
\tag{WT4}
\]

An incompatible polymer touches the closed graph neighborhood of the first polymer's support, which has at most `(d+1)|chi|` vertices. If `r<=1/2`,

\[
\sum_{\chi'\not\sim\chi}|w(\chi')|e^{2|\chi'|}
\le |\chi|\frac{d+1}{d^2}
=\frac{39}{1444}|\chi|<|\chi|.
\tag{WT4a}
\]

Apply the abstract polymer convergence theorem with size function `|chi|` and inflated activities `|w(chi)|exp(|chi|)`. The precise version inspected is Ueltschi's Theorem 1, equation (3), with counting measure weighted by the complex activity and `zeta=-1` on incompatible pairs, zero otherwise. This proves absolute convergence of the vacuum logarithm and connected marked series with an additional exponential support margin. The hypotheses, including incompatibility with itself, are verified by the construction above. At every finite space-time volume the polymer set is finite, so the theorem's integrability assumption holds; its rooted bound is uniform when these volumes grow.

For a nonempty explicit sufficient domain choose

\[
\rho_*=(2^{11}d^2e^2)^{-8},\qquad
t_0>\delta^{-1}\log(1/\rho_*),\qquad
|u|<u_*:=\frac{\log(1+\rho_*)}{v(t_0+\tau_0)}.
\tag{WT4b}
\]

These choices are independent of `epsilon`, `m`, spatial volume and the number of coarse blocks. They are not optimized and should not be confused with the earlier finite-order band threshold.

To include a fixed mark, treat `exp(z O)-1` as one distinguished bounded insertion on its finite support. If that support is disconnected, enlarge it to a fixed finite connected hull and tensor the operator with identities on the added links. This keeps each distinguished insertion within one connected component. Its norm is at most `exp(|z| ||O||)-1`. For sufficiently small `z`, the same polymer criterion holds with constants depending on the marked support. Differentiation then gives the marked series. The extra exponential support weight bounds the influence of remote time or spatial boundaries. In a connected two-mark term the support must bridge the graph distance of the marks, so the corresponding connected series has an exponential distance bound, with a prefactor depending on the two fixed supports.

For real `u` and fixed finite volume, the Wilson transfer has a continuous strictly positive kernel and is a positive compact self-adjoint operator. Its leading eigenvector is strictly positive and unique: replacing an eigenvector by its absolute value increases its Rayleigh quotient unless its sign is constant, and orthogonal leading eigenvectors cannot both have constant sign. The constant product vacuum has nonzero overlap with this leading vector. Thus the two-sided large-block-time limit of the normalized marked expectation is the actual finite-volume vacuum expectation. The boundary estimates just proved permit a local thermodynamic limit and give an exponentially clustered limiting vacuum state. Identification of the full excited transfer representation, beyond these vacuum correlations, is kept separate in WT-6.

This is the discrete-time extension needed for the **vacuum** part of the route. It does not yet bound the complete excited-shell energy, Gram and synthesis kernels in the norm of the G18 construction.

## WT-5. Uniform control of free propagation and marked contour denominators

For `tau,E>0`, the inequality `exp(tau E)>=1+tau E` gives

\[
0<\frac{\tau}{e^{\tau E}-1}\le\frac1E,\qquad
\frac{\tau}{1-e^{-\tau E}}=\tau+\frac{\tau}{e^{\tau E}-1}\le\tau+\frac1E.
\tag{WT5}
\]

These bounds apply to all energies by spectral calculus. They do not require an upper representation cutoff. The raw unscaled transfer resolvent instead has a `1/tau` divergence.

For a complex contour point `z`, put `a=tau(E-Re z)`, `b=-tau Im z`. If `|b|<=pi`,

\[
|e^{a+ib}-1|^2=e^a\bigl(4\sinh^2(a/2)+4\sin^2(b/2)\bigr)
\ge\frac4{\pi^2}e^a(a^2+b^2).
\]

The last step uses `|2 sinh(a/2)|>=|a|` and `|sin(b/2)|>=|b|/pi`. Therefore

\[
\left|\frac{\tau}{e^{\tau(E-z)}-1}\right|
\le\frac\pi2\frac{e^{-\tau(E-\operatorname{Re}z)/2}}{|E-z|}.
\tag{WT5a}
\]

For `E>=0`, a contour with `|z|<=Z` and `dist(z,spec D)>=Delta>0`, and `tau<=tau0` with `tau0 |Im z|<=pi`, this yields

\[
\left\|D\frac{\tau}{e^{\tau(D-z)}-1}\right\|
\le\frac\pi2 e^{\tau_0 Z/2}(1+Z/\Delta).
\tag{WT5b}
\]

Indeed `E/|E-z|<=1+|z|/|E-z|`. On the exact-support coefficient direct sum, `D` acts separately on each component, so the same bound holds in every rooted weighted sum of component Hilbert norms. This supplies the free resolvent estimate at all energies. Bounding the interacting, vacuum-dressed marked insertion next to this resolvent is still necessary.

## WT-6. The remaining complete-shell estimate and conditional transport

The vacuum polymer bound resolves the uncontrolled number of microscopic slices. It does not establish the operator estimate needed to identify the entire shell near `E_F=8/3`. A vacuum gap alone also cannot determine a higher shell's multiplicity or prove source totality; the new exact counterexample records this distinction.

A concrete next target is to construct the actual vacuum-dressed block transfer on G18's exact-support coefficient space and prove a uniform rooted bound for its perturbation. Write, only after that construction is supplied,

\[
\widetilde B_{\epsilon,L}(u)=e^{-\ell D_{\epsilon,L}}+\mathcal F_{\epsilon,L}(u),
\]

with the scalar leading transfer eigenvalue divided out. On the mapped free-shell contour `w=exp(-ell z)`, prove

\[
\sup_{\epsilon,L,z}\bigl\|
\mathcal F_{\epsilon,L}(u)
(e^{-\ell D_{\epsilon,L}}-e^{-\ell z})^{-1}
\bigr\|_{\mathrm{root}}\le q(u)<1,
\qquad q(u)\longrightarrow0.
\tag{WT6}
\]

The contour itself has fixed physical-energy clearance. The norm must handle arbitrary input excitation support and its Hilbert-space coefficients, not just a fixed number of observable insertions. The bulk vacuum criterion bounds scalar polymer amplitudes; it is not automatically a bound in this coefficient operator norm. A proposed proof must explicitly control open excitation boundaries and the normalization of the dressed coefficient map.

Once (WT6), coefficient/Hilbert transport, source totality and the positive Gram bound are proved, G18's Neumann-contour and one-mark construction can be repeated. The needed output is a common holomorphic majorant for the complete shell kernels `Phi in {h,G,S}`. The pre-existing fixed-order matching then gives

\[
\|\Phi^W_\epsilon(u)-\Phi^H(u)\|_{\mu,\sharp}
\le\epsilon^2\sum_{n=0}^M A_{n,\mu}|u|^n
+\frac{2C(|u|/R)^{M+1}}{1-|u|/R},
\]

and hence summed convergence by first sending `epsilon` to zero, then `M` to infinity. For an energy matching error `eta_epsilon(u)`, the [existing relative-gap theorem](../../paper/research_notes/G18_RELATIVE_GAP_BRIDGE_20260904.tex) gives the conditional lower bound

\[
\operatorname{gap}_{\rm internal}^W(k,u)
\ge [c_H(u)-2\gamma_\mu\eta_\epsilon(u)]q(k),\qquad k\ne0.
\]

Likewise a synthesis error smaller than the Hamiltonian lower frame amplitude preserves a positive source amplitude by the triangle inequality. These are ready-to-use consequences, but the full Wilson shell hypotheses have not been discharged in this continuation. G19 remains open, including the subsequent spatial continuum crossing.

## Provenance and relation to the sources

- [Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*](https://arxiv.org/abs/math-ph/0412040), PDF pp. 7-10, equations (9), (12)-(14), motivates the active-block/projector organization and supplies its classical-to-polymer framework. WT-1 through WT-4 reconstruct the block operators for the actual Wilson product. In particular (WT2) is derived directly from that product; a Hamiltonian theorem is not simply applied to its logarithm.
- [Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*](https://arxiv.org/abs/math-ph/0411042), PDF pp. 6-10, equations (7)-(15), provides the coefficient-space framework already used by G18. The unproved estimate (WT6) records the Wilson replacement still needed.
- [Ueltschi, *Cluster expansions and correlation functions*](https://arxiv.org/abs/math-ph/0304003), PDF p. 2, Theorem 1 and equations (3)-(5), supplies the inspected abstract convergence implication after (WT4a). It explicitly recovers the Kotecky-Preiss criterion in the discrete case. The model-dependent activity bound, geometry and criterion verification are displayed here. The original [Kotecky-Preiss paper](https://doi.org/10.1007/BF01211762) was located bibliographically; its full theorem was not obtained in this run.

The two Yarotsky PDFs have been acquired and hash-pinned in the continuation's source manifest. Their indicated pages were inspected, including the projector placement and the factorization argument. The manifest's PDF `sha256` values hash the original file bytes. Its `text_sha256` values hash decoded UTF-8 text with line endings normalized to LF; the validation record also retains the local extracted-text byte hashes, which differ on Windows. The exact check results, Lean scope and graph provenance are recorded with this continuation's validation output.
