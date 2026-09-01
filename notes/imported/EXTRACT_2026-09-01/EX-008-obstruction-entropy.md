---
id: EX-008
title: "Obstruction: plaquette entropy beats logarithmic β growth — the chessboard 'small-plaquette tube' cannot survive the continuum limit"
kind: extraction
items: 8
status_breakdown: {"solid": 6, "conditional": 1, "gap": 1}
program: yang_mills
extracted_by: claude-opus-5 subagent, 2026-09-01
stance: preservation (content extraction, not refereeing)
source_files:
  - RICCATI/04_misc_docs/PROOF_13_High_Probability_Convexity(1).md
  - HESSIAN/Core_Hessian/PROOF_13_High_Probability_Convexity.md
  - RICCATI/archive/PROOF_13_High_Probability_Convexity(1).md
  - _EXTRACT_FOR_LLM/02_candidates/CAND-005-counting-obstruction-the-small-plaquette-tube-event-has-prob.md
  - _EXTRACT_FOR_LLM/04_papers/PAPER-1-curvature-no-go/ABSTRACT.md
  - REFLECTION_POSITIVITY/04_GAP_BRIDGES/Exciting_04_Localization_Typicality_Bridge.md
  - WILSON/08_misc_docs/EXCITING_05_LOCALIZATION_AVERAGED_BADNESS.md
  - _EXTRACT_FOR_LLM/01_corpus_map/DOMAIN_ASSESSMENTS.md
---

# Obstruction: plaquette entropy beats logarithmic β growth — the chessboard "small-plaquette tube" cannot survive the continuum limit

> The chessboard + small-ball tail bound μ_β(d(U_p,I)≥δ) ≤ C₀β^{α/2}e^{−βc_Φ(δ)} is correct and volume-uniform, but a union bound over the 6(R/a)⁴ plaquettes of a fixed physical ball is o(1) only if c·c_Φ(δ) > 4 with c = 11N²/(12π²); since c_Φ(δ) ≤ Φ_max(N) ≤ 2 for every N and every δ, no δ works for N ≤ 4 (deficit factor 3.19 at N=3, 5.38 at N=2) — and a link-translation/disjointness argument I reconstruct here shows the tube event is in fact genuinely atypical for all δ below an explicit threshold 4π/(3√(11N)) (= 0.729 rad for SU(3)).

**8 extracted items** — 1 conditional, 1 gap, 6 solid

---

## 1. Setup and normalisations (fixes every constant used below)

`status: solid` · `kind: definition`

### Statement

Let $\Lambda_a$ be a periodic $4$-dimensional hypercubic lattice of spacing $a$ with $|\Lambda|=L^4$ sites, oriented edge (link) set $E$ with $|E|=4L^4$, and plaquette set $P$ with $|P|=\binom{4}{2}L^4=6L^4$; hence $|E|/|P|=2/3$ and each link lies in exactly $2(d-1)=6$ plaquettes. Let $G=\mathrm{SU}(N)$, $d_G:=\dim G=N^2-1$. Configuration space $\mathscr A:=G^{E}$ carries the product bi-invariant metric induced by the Hilbert–Schmidt inner product on $\mathfrak{su}(N)$,
$$\langle X,Y\rangle := \mathrm{Tr}(X^{\dagger}Y) = -\mathrm{Tr}(XY),\qquad X,Y\in\mathfrak{su}(N),$$
and the product normalised Haar probability measure $\mathrm{d}\mathrm{vol}$. With this normalisation, if $V=\exp\theta$ with $\theta=i\,\mathrm{diag}(t_1,\dots,t_N)$, $\sum_j t_j=0$, and $\theta$ is the representative of minimal norm, then
$$d_G(V,I)=\|\theta\|_{\mathrm{HS}}=\Big(\sum_j t_j^2\Big)^{1/2}.$$
Ricci curvature: $\mathrm{Ric}_g=\tfrac{N}{2}\,g$ (bi-invariant metric, $\mathrm{Ric}(X,X)=-\tfrac14 B(X,X)$ with Killing form $B(X,Y)=2N\,\mathrm{Tr}(XY)$).

Wilson action and Gibbs measure:
$$S_\beta(U):=\beta\sum_{p\in P}\Phi(U_p),\qquad \Phi(V):=\tfrac1N\,\mathrm{Re}\,\mathrm{Tr}(I-V)=1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,V,$$
$$\mathrm{d}\mu_\beta:=Z_\beta^{-1}e^{-S_\beta}\,\mathrm{d}\mathrm{vol},\qquad Z_\beta=\int e^{-S_\beta}\mathrm{d}\mathrm{vol}.$$
In eigen-angle coordinates $\Phi(\exp\theta)=\tfrac1N\sum_j(1-\cos t_j)$, so
$$\Phi(\exp\theta)=\frac{\|\theta\|^2}{2N}-\frac{1}{24N}\sum_j t_j^4+\cdots,\qquad\text{in particular}\quad \Phi(V)\le \frac{d_G(V,I)^2}{2N}\ \ \text{globally.}$$

Bad-plaquette energy floor (the object the whole obstruction turns on):
$$c_\Phi(\delta):=\inf\{\Phi(V): V\in G,\ d_G(V,I)\ge\delta\}\in[0,\Phi_{\max}(N)],$$
non-decreasing in $\delta$, with $\Phi_{\max}(N):=\max_{V\in G}\Phi(V)$.

Tube events. For $\delta>0$ and a fixed *physical* ball/box $B_R$ of side $R$ (so $(R/a)^4$ sites, $|P_R|\simeq 6(R/a)^4$ plaquettes),
$$\Omega_{\delta,R}:=\{U\in\mathscr A:\ d_G(U_p,I)<\delta\ \ \forall p\in P_R\}.$$

### Derivation

All of this is bookkeeping; the two points that matter and are easy to get wrong are recorded here.

(i) *Metric normalisation.* The source document (PROOF_13 §3.1, step 1 of the proof) fixes the convention implicitly by writing $\mathrm{Re}\,\mathrm{Tr}(e^{\theta})=N-\tfrac12\|\theta\|^2+O(\|\theta\|^3)$. Expanding $e^{\theta}=I+\theta+\tfrac12\theta^2+\cdots$ with $\theta$ anti-Hermitian traceless gives $\mathrm{Tr}\,\theta=0$ and $\mathrm{Tr}\,\theta^2=-\mathrm{Tr}(\theta^{\dagger}\theta)=-\|\theta\|_{\mathrm{HS}}^2$, hence $\mathrm{Re}\,\mathrm{Tr}\,e^{\theta}=N-\tfrac12\|\theta\|_{\mathrm{HS}}^2+O(\|\theta\|^4)$. So $\|\cdot\|$ in the source *is* Hilbert–Schmidt and the geodesic distance is $\|\theta\|_{\mathrm{HS}}$. Consequently $\Phi(\exp\theta)=\|\theta\|^2/(2N)+O(\|\theta\|^4)$, and $c_\Phi(\delta)=\delta^2/(2N)+O(\delta^4)$ — the source's statement '$c_\Phi(\delta)\simeq c\,\delta^2$' with the constant made explicit as $1/(2N)$.

The global inequality $\Phi(V)\le d_G(V,I)^2/(2N)$ follows from $1-\cos t\le t^2/2$ applied term-by-term to the minimal-norm representative. It is *global*, not asymptotic; this is used below.

(ii) *Combinatorics.* In $d$ dimensions $|E|=d|\Lambda|$, $|P|=\binom d2|\Lambda|$, so $|E|/|P|=2/(d-1)=2/3$ at $d=4$. A link $\ell$ of direction $\mu$ lies in the plaquettes of plane $(\mu,\nu)$, $\nu\neq\mu$ ($d-1=3$ choices), at two positions each, giving $2(d-1)=6$. Any two of those six plaquettes meet exactly in $\ell$: for $p_1=\{(x,\mu),(x+\hat\mu,\nu),(x+\hat\nu,\mu),(x,\nu)\}$ and $p_2$ the same plane based at $x-\hat\nu$, one has $p_1\cap p_2=\{(x,\mu)\}$. Hence $\ell$ shares a plaquette with exactly $6\times 3=18$ other links. (Used in Item 5.)

### Constants and numbers

d=4; |E|=4L^4; |P|=6L^4; |E|/|P|=2/3; plaquettes per link = 6; links co-plaquette with a given link = 18; dim SU(N)=N^2-1 (=8 for N=3, 3 for N=2); Ric_g = (N/2) g (= 1.5 g for SU(3), 1.0 g for SU(2)); Phi(V) <= d_G(V,I)^2/(2N); c_Phi(delta) = delta^2/(2N) + O(delta^4); |P_R| ≃ 6 (R/a)^4.

**Caveat.** The δ-thresholds quoted throughout are in Hilbert–Schmidt radians; rescaling the metric by λ rescales every δ by λ but changes none of the dimensionless conclusions (c_Φ, Φ_max, and the criterion c·c_Φ>4 are metric-independent).

**Why it matters.** Every number in the obstruction depends on this normalisation; the source states it only implicitly, and a factor of 2 or N here would move the deficit factor. Fixing it makes the whole argument checkable.

---

## 2. Lemma 1 (chessboard + small-ball single-plaquette tail bound, volume-uniform)

`status: conditional` · `kind: derivation`

### Statement

Assume $\mu_\beta$ is reflection positive with respect to the lattice reflection planes and therefore satisfies the chessboard estimate for plaquette-localised events. Fix $\delta>0$ and $p\in P$, and let $A_{p,\delta}:=\{U:d_G(U_p,I)\ge\delta\}$. Then there exist $r_0>0$ and $\kappa_G>0$ depending only on $G$ (through $\mathrm{Haar}(B_r)\ge\kappa_G r^{d_G}$ for $r\le r_0$) such that for all $\beta\ge r_0^{-2}$,
$$\boxed{\ \mu_\beta(A_{p,\delta})\ \le\ C_0\,\beta^{\alpha/2}\,e^{-\beta\,c_\Phi(\delta)},\qquad \alpha=d_G\cdot\frac{|E|}{|P|}=\frac{2(N^2-1)}{3},\quad C_0=e^{8/N}\kappa_G^{-2/3}. }$$
The bound is **uniform in the volume** $|\Lambda|$: no factor of $|E|$, $|P|$ or $L$ survives. For $\mathrm{SU}(3)$: $\alpha=16/3$, $\alpha/2=8/3$, $C_0=e^{8/3}\kappa_G^{-2/3}$.

### Derivation

This is PROOF_13 Lemma 3.1, reproduced in full with the constants that the source leaves as '$\lesssim$'. The three near-identical copies of the source (RICCATI/04_misc_docs, RICCATI/archive, HESSIAN/Core_Hessian) are byte-identical (md5 d8aa4d5759f977f64d7203cfb22b74a1, 9681 bytes); I extracted from RICCATI/04_misc_docs.

**Step 1 (energy floor on the fully-bad configuration set).** By definition of $c_\Phi(\delta)$, on the set $\bigcap_{q\in P}A_{q,\delta}$ every plaquette contributes at least $c_\Phi(\delta)$, so
$$S_\beta(U)\ \ge\ \beta\,|P|\,c_\Phi(\delta)\qquad\text{on }\ \bigcap_{q\in P}A_{q,\delta}.$$

**Step 2 (chessboard).** The chessboard estimate for an RP measure and an event localised in one tile of a reflection tiling gives
$$\mu_\beta(A_{p,\delta})\ \le\ \Big(\mu_\beta\Big(\bigcap_{q\in P}A_{q,\delta}\Big)\Big)^{1/|P|}=\Big(\frac{Z_\beta^{\mathrm{bad}}}{Z_\beta}\Big)^{1/|P|},\qquad Z_\beta^{\mathrm{bad}}:=\int_{\bigcap_q A_{q,\delta}}e^{-S_\beta}\mathrm{d}\mathrm{vol}.$$
The $1/|P|$ root is the entire content of the chessboard step: it is what makes the final bound volume-independent.

**Step 3 (upper bound on $Z^{\mathrm{bad}}_\beta$).** By Step 1 and $\mathrm{vol}(\mathscr A)=1$ (normalised Haar),
$$Z_\beta^{\mathrm{bad}}\ \le\ e^{-\beta|P|c_\Phi(\delta)}.$$

**Step 4 (small-product-ball lower bound on $Z_\beta$).** Let $B_r\subset G$ be the geodesic ball of radius $r<\mathrm{inj}(G)$ about $I$ and $\mathcal B_r:=\{U:U_e\in B_r\ \forall e\in E\}$. Each plaquette holonomy is an ordered product of $4$ link variables, so by the triangle inequality for the bi-invariant distance,
$$d_G(U_p,I)\le\sum_{e\in\partial p}d_G(U_e,I)\le 4r\qquad (U\in\mathcal B_r),$$
and therefore, by the global inequality $\Phi\le d_G^2/(2N)$ from Item 1,
$$\Phi(U_p)\le\frac{(4r)^2}{2N}=\frac{8r^2}{N}=:C_\Phi r^2,\qquad C_\Phi:=\frac8N .$$
(The source writes '$\Phi(U_p)\lesssim r^2$ for some constant $C_\Phi$'; $C_\Phi=8/N$ is the explicit value in $d=4$.) Hence $S_\beta\le\beta|P|C_\Phi r^2$ on $\mathcal B_r$, and
$$Z_\beta\ \ge\ \int_{\mathcal B_r}e^{-S_\beta}\mathrm{d}\mathrm{vol}\ \ge\ e^{-\beta|P|C_\Phi r^2}\,\mathrm{Haar}(B_r)^{|E|}\ \ge\ e^{-\beta|P|C_\Phi r^2}\,(\kappa_G r^{d_G})^{|E|},$$
where $\mathrm{Haar}(B_r)\ge\kappa_G r^{d_G}$ for $r\le r_0$ holds by Günther's volume comparison (sectional curvature of a bi-invariant metric is bounded above, $\sec(X,Y)=\tfrac14\|[X,Y]\|^2/(\|X\|^2\|Y\|^2-\langle X,Y\rangle^2)$), with $\kappa_G=\omega_{d_G}/\mathrm{Vol}(G)\cdot(1+O(r_0^2))$.

**Step 5 (take the $1/|P|$ root — the globalisation trick).** Combining Steps 2–4 and using $|E|/|P|=2/3$:
$$\mu_\beta(A_{p,\delta})\ \le\ \exp\big(-\beta c_\Phi(\delta)+\beta C_\Phi r^2\big)\cdot\big(\kappa_G r^{d_G}\big)^{-|E|/|P|}=\exp\big(-\beta c_\Phi(\delta)+\beta C_\Phi r^2\big)\,\kappa_G^{-2/3}\,r^{-2d_G/3}.$$
Every extensive quantity has cancelled: $|P|$ appeared in the exponent of both numerator and denominator and is removed by the root, and $|E|$ survives only through the *ratio* $|E|/|P|=2/3$. This is exactly the source's step 5, and it is correct.

**Step 6 (optimise $r$).** Choose $r=\beta^{-1/2}$ (legal once $\beta\ge r_0^{-2}$). Then $\beta C_\Phi r^2=C_\Phi=8/N$ is $\beta$-independent and $r^{-2d_G/3}=\beta^{d_G/3}=\beta^{\alpha/2}$ with $\alpha=2d_G/3$. Hence
$$\mu_\beta(A_{p,\delta})\ \le\ e^{8/N}\kappa_G^{-2/3}\,\beta^{(N^2-1)/3}\,e^{-\beta c_\Phi(\delta)}.\qquad\square$$

**Two corrections to the source.** (a) The source's Corollary 3.2 quotes the prefactor as $\beta^{\alpha}$ whereas its own Lemma 3.1 proves $\beta^{\alpha/2}$; the lemma is right. This is immaterial for everything below (the prefactor is polynomial in $\log(1/a)$ either way). (b) The source asserts $\Phi\in[0,2]$ for all $N$; that is correct as an upper bound but not sharp for odd $N$ (Item 3).

**Robustness remark (block tiling).** Osterwalder–Seiler reflection positivity for the Wilson measure is stated for reflections in hyperplanes; the standard chessboard estimate applies to events localised in a *unit block* rather than a single plaquette. Redoing Steps 2–6 with $|B|=|\Lambda|=|P|/6$ blocks: the fully-bad set forces one bad plaquette per block, so $S_\beta\ge\beta|B|c_\Phi(\delta)$, the root is $1/|B|$, and the exponential factor is again exactly $e^{-\beta c_\Phi(\delta)}$; only the polynomial prefactor changes, to $\beta^{2d_G}$ with $|E|/|B|=4$ and $e^{6C_\Phi}=e^{48/N}$. The obstruction below is untouched. Any reasonable variant of the tiling changes only polynomial factors.

### Constants and numbers

alpha = 2(N^2-1)/3  [SU(3): 16/3 ≈ 5.333; SU(2): 2]; alpha/2 = (N^2-1)/3 [SU(3): 8/3 ≈ 2.667; SU(2): 1]; C_Phi = 8/N (4D plaquette = 4 links) [SU(3): 2.667; SU(2): 4]; C_0 = e^{8/N} kappa_G^{-2/3} [SU(3): e^{8/3} kappa_G^{-2/3} ≈ 14.39 kappa_G^{-2/3}]; optimal r = beta^{-1/2}; validity beta >= r_0^{-2}. Block-tiling variant: prefactor beta^{2(N^2-1)} and e^{48/N}, same exponential e^{-beta c_Phi(delta)}.

**Caveat.** Conditional on the chessboard estimate holding in the exact gauge/plaquette setting used (the source itself flags this as 'surgical task 1'); the block-tiling remark shows the conclusion is insensitive to which tiling is legitimate.

**Why it matters.** This is the strongest volume-uniform single-plaquette tail available, and it is genuinely correct: the concentration exponent is exactly beta*c_Phi(delta) with no volume factor. It is therefore the best possible input to the union bound — which is what makes the failure in Item 4 an obstruction rather than a lost opportunity.

---

## 3. Lemma 2 (sharp universal upper bounds on the bad-plaquette energy floor c_Φ)

`status: solid` · `kind: theorem`

### Statement

Let $G=\mathrm{SU}(N)$, $\Phi(V)=1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,V$, $c_\Phi(\delta)=\inf\{\Phi(V):d_G(V,I)\ge\delta\}$, with the Hilbert–Schmidt normalisation of Item 1. Then:

(a) **(Absolute ceiling.)** $\displaystyle \sup_{\delta>0}c_\Phi(\delta)\ \le\ \Phi_{\max}(N)=\max_{V\in \mathrm{SU}(N)}\Phi(V)=\begin{cases}2, & N \text{ even},\\[2pt] 1+\cos(\pi/N), & N \text{ odd},\end{cases}$
and in particular $c_\Phi(\delta)\le 2$ for every $N$ and every $\delta>0$. The maximiser is the centre element $\omega^{\lfloor N/2\rfloor}I$, $\omega=e^{2\pi i/N}$.

(b) **($\mathrm{SU}(2)$-embedding bound, sharp at $N=2$.)** For $0<\delta\le\pi\sqrt2$,
$$c_\Phi(\delta)\ \le\ \frac{2}{N}\Big(1-\cos\frac{\delta}{\sqrt2}\Big)\ \le\ \frac4N,$$
with equality throughout for $N=2$ (i.e. $c_\Phi^{\mathrm{SU}(2)}(\delta)=1-\cos(\delta/\sqrt2)$ exactly).

(c) **(Quadratic bound, global.)** $c_\Phi(\delta)\le\delta^2/(2N)$ for every $\delta\in[0,\mathrm{diam}(G)]$, with equality to leading order as $\delta\to0$.

### Derivation

**(a).** $\Phi(V)=1-\tfrac1N\mathrm{Re}\,\mathrm{Tr}\,V$ and $|\mathrm{Tr}\,V|\le N$ give $\Phi\le2$ immediately. For the sharp value, write $V\sim\mathrm{diag}(e^{it_1},\dots,e^{it_N})$ with $\sum_j t_j\equiv0\ (\mathrm{mod}\ 2\pi)$ and minimise $f(t)=\sum_j\cos t_j$ on that torus. Lagrange: $\sin t_j=\lambda$ for all $j$, so each $t_j\in\{\alpha,\pi-\alpha\}$. If $k$ of them equal $\pi-\alpha$ and $N-k$ equal $\alpha$, the constraint reads $(N-2k)\alpha+k\pi=2\pi m$ and the objective is $(N-2k)\cos\alpha$. Scanning $k\in\{0,\dots,N\}$, $m\in\mathbb Z$ gives
$$\min_{\mathrm{SU}(N)}\mathrm{Re}\,\mathrm{Tr}\,V=\begin{cases}-N,&N\text{ even (attained at }-I),\\ -N\cos(\pi/N),&N\text{ odd (attained at the centre element }e^{i\pi(N-1)/N}I).\end{cases}$$
I verified this numerically for $2\le N\le14$ (exact stationary-point enumeration, cross-checked against a $1200^2$ torus grid for $N=3$): $-2,-1.5,-4,-4.045085,-6,-6.306782,-8,-8.457234,-10,-10.554423,-12,-12.622244,-14$, matching $-N\cos(\pi/N)$ for odd $N$ to $10^{-6}$. Dividing by $-N$ and adding $1$ gives $\Phi_{\max}$. Finally $c_\Phi(\delta)\le\Phi(V)$ for *any* admissible $V$, and $c_\Phi$ is non-decreasing, so $\sup_\delta c_\Phi(\delta)\le\Phi_{\max}$. [The sharp odd-$N$ closed form $\Phi_{\max}=1+\cos(\pi/N)$ is my identification — reconstructed; the corpus only records the crude $\Phi\le2$.]

**(b) [reconstructed].** Let $u:=\delta/\sqrt2\in(0,\pi]$ and put $\theta:=i\,\mathrm{diag}(u,-u,0,\dots,0)\in\mathfrak{su}(N)$, $V:=\exp\theta$. Then $\|\theta\|_{\mathrm{HS}}=u\sqrt2=\delta$. This representative is minimal: any other logarithm has angles $t_j+2\pi n_j$ with $\sum n_j=0$; the cheapest competitor is $(u-2\pi,\,2\pi-u,\,0,\dots)$ of norm $(2\pi-u)\sqrt2\ge u\sqrt2$ precisely because $u\le\pi$, and every other redistribution adds at least $2\pi$ to some entry. Hence $d_G(V,I)=\delta$ exactly, so $V$ is admissible in the infimum defining $c_\Phi(\delta)$, and
$$c_\Phi(\delta)\le\Phi(V)=\tfrac1N\big[(1-\cos u)+(1-\cos(-u))\big]=\frac2N\big(1-\cos(\delta/\sqrt2)\big)\le\frac4N.$$
For $N=2$ the maximal torus is one-dimensional, $\theta=i\,\mathrm{diag}(u,-u)$ is the *only* conjugacy class at distance $u\sqrt2$, and $1-\cos u$ is increasing on $[0,\pi]$, so the inequality is an identity: $c_\Phi^{\mathrm{SU}(2)}(\delta)=1-\cos(\delta/\sqrt2)$, $\delta\in[0,\pi\sqrt2]$, $\mathrm{diam}(\mathrm{SU}(2))=\pi\sqrt2\approx4.4429$.

Numerically the bound is *essentially tight for $\mathrm{SU}(3)$ too*: on a $1400^2$ grid of the $\mathrm{SU}(3)$ maximal torus (with the $2\pi$-shift lattice minimised over), $c_\Phi^{\mathrm{SU}(3)}(\delta)$ agrees with $\tfrac23(1-\cos(\delta/\sqrt2))$ to $\le10^{-4}$ for all $\delta\le4.44$ — e.g. $\delta=1.0$: $0.159850$ vs $0.159837$; $\delta=3.0$: $1.015496$ vs $1.015423$.

**(c).** Item 1 gives $\Phi(V)\le d_G(V,I)^2/(2N)$ globally (from $1-\cos t\le t^2/2$). Since $G$ is connected and compact, for every $\delta\le\mathrm{diam}(G)$ there exists $V$ with $d_G(V,I)=\delta$ exactly; evaluating at such $V$ gives $c_\Phi(\delta)\le\delta^2/(2N)$. Sharpness as $\delta\to0$ follows from the expansion in Item 1. $\square$

### Constants and numbers

Phi_max(N): N=2: 2; N=3: 3/2; N=4: 2; N=5: 1+cos(36°)=1.809017; N=6: 2; N=7: 1.900969; N=9: 1.939693; N=11: 1.959493. min ReTr = -N cos(pi/N) for odd N, = -N for even N.
diam(SU(2)) = pi*sqrt(2) = 4.442883 (attained at -I, Phi=2). diam(SU(3)) = (2pi/3)sqrt(6) = 5.130199 (attained at the centre elements omega I, omega^2 I, Phi=3/2) — numerically confirmed 5.129283 on a 1400^2 torus grid.
Exact c_Phi^{SU(3)}(delta) (torus grid): delta=0.05: 0.000435; 0.1: 0.001668; 0.2: 0.006657; 0.3: 0.014953; 0.5: 0.041236; 0.729: 0.086639; 1.0: 0.159850; 1.5: 0.341193; 2.0: 0.562738; 3.0: 1.015496; 4.0: 1.300964; 4.4429: 1.333360; 5.12: 1.499980.
c_Phi^{SU(2)}(delta) = 1 - cos(delta/sqrt 2) exactly; max 2 at delta = pi*sqrt2.
sup_delta c_Phi <= 4/N for delta <= pi*sqrt2 [SU(3): 4/3 = 1.3333, matching the tabulated 1.33336 at delta=4.4429].

**Caveat.** Parts (a) closed form for odd N, (b), and (c) are my reconstructions; the corpus records only the crude bound Φ ≤ 2. Nothing downstream depends on the refinements — the crude bound already settles N ≤ 4.

**Why it matters.** c_Φ is the *only* quantity in the tail bound that the author is free to tune (via δ). This lemma says it is bounded by an absolute constant ≤ 2 no matter what δ is chosen — which is precisely why the union bound in Item 4 cannot be repaired.

---

## 4. Lemma 3 (the asymptotically free trajectory: β(a) = c ln(1/aΛ) with c = 11N²/(12π²))

`status: solid` · `kind: derivation`

### Statement

For pure $\mathrm{SU}(N)$ Yang–Mills the one-loop renormalisation-group equation $\mu\,\mathrm{d}g/\mathrm{d}\mu=-b_0g^3$, $b_0=\dfrac{11N}{48\pi^2}$, together with the Wilson normalisation $\beta=2N/g^2$ and the identification $\mu=1/a$, gives
$$\boxed{\ \beta(a)\ =\ c\,\ln\frac{1}{a\Lambda}\ (1+o(1)),\qquad c=\frac{11N^2}{12\pi^2}. }$$
Numerically $c=0.371511$ for $N=2$ and $c=0.835900$ for $N=3$, so $4/c=48\pi^2/(11N^2)$ equals $10.766841$ and $4.785263$ respectively.

### Derivation

The pure-gauge one-loop coefficient is $b_0=\frac{1}{16\pi^2}\cdot\frac{11N}{3}=\frac{11N}{48\pi^2}$ (no fermions). From $\mu\,\mathrm{d}g/\mathrm{d}\mu=-b_0g^3$,
$$\frac{\mathrm{d}}{\mathrm{d}\ln\mu}\Big(\frac{1}{g^2}\Big)=-\frac{2}{g^3}\frac{\mathrm{d}g}{\mathrm{d}\ln\mu}=2b_0=\frac{11N}{24\pi^2},$$
so $\dfrac{1}{g^2(\mu)}=\dfrac{11N}{24\pi^2}\ln\dfrac{\mu}{\Lambda}$ with $\Lambda$ the RG-invariant scale. Setting $\mu=1/a$ and $\beta=2N/g^2$:
$$\beta(a)=2N\cdot\frac{11N}{24\pi^2}\ln\frac{1}{a\Lambda}=\frac{22N^2}{24\pi^2}\ln\frac1{a\Lambda}=\frac{11N^2}{12\pi^2}\ln\frac1{a\Lambda}.$$
Two-loop and lattice-scheme corrections modify this by $O(\ln\ln(1/a))$ terms and by a redefinition of $\Lambda$; neither changes the *power* of $a$ in any of the balances below, because those balances compare $a^{-4}$ against $e^{-\beta\cdot(\text{const})}=(a\Lambda)^{c\cdot(\text{const})}$, i.e. they compare exponents of $a$, and $O(\ln\ln)$ corrections shift the answer only by logarithms. The one-loop coefficient $b_0$ is scheme-independent, so $c$ is unambiguous.

**The key structural fact:** $\beta$ grows only *logarithmically* in $1/a$, with a fixed and rather small slope $c$. Everything in Item 4 is the collision between this $\log$ and the $a^{-4}$ growth of the plaquette count.

### Constants and numbers

b_0 = 11N/(48 pi^2). c = 11N^2/(12 pi^2): N=2: 0.371511; N=3: 0.835900; N=4: 1.486044; N=5: 2.321944; N=6: 3.343599; N=8: 5.944176; N=10: 9.287775; N=11: 11.238208; N=12: 13.374396.
4/c = 48 pi^2/(11 N^2): N=2: 10.766841; N=3: 4.785263; N=4: 2.691710; N=5: 1.722695; N=6: 1.196316; N=8: 0.672928; N=10: 0.430674; N=11: 0.355929; N=12: 0.299079.
Sanity check: beta=6 for SU(3) corresponds to ln(1/aLambda)=6/0.8359=7.18, i.e. aLambda = 7.6e-4.

**Caveat.** One-loop only; two-loop and lattice-scheme effects change β(a) by O(ln ln(1/a)) and redefine Λ, neither of which affects the a-power counting.

**Why it matters.** c is the exchange rate between 'lattice spacing shrinking' and 'coupling strengthening'. The obstruction is entirely the statement that this exchange rate is too small: c ≈ 0.84 (N=3) where the counting needs c ≥ 2.

---

## 5. Theorem D (counting obstruction: plaquette entropy a^{-4} beats the logarithmic growth of β — no δ makes the small-plaquette tube typical via the chessboard bound)

`status: solid` · `kind: obstruction`

### Statement

Fix a physical scale $R>0$ and let $B_R$ be a box of physical side $R$, so $|P_R|=6(R/a)^4(1+O(a/R))$. Let $\Omega_{\delta,R}=\{U:d_G(U_p,I)<\delta\ \forall p\in P_R\}$ and let $\beta(a)=c\ln\frac1{a\Lambda}$, $c=\frac{11N^2}{12\pi^2}$ (Lemma 3). Then:

**(i)** Lemma 1 plus a union bound gives, for every $\delta>0$,
$$\mu_{\beta(a)}\big(\Omega_{\delta,R}^{\,c}\big)\ \le\ 6\Big(\frac Ra\Big)^{4}C_0\,\beta(a)^{\alpha/2}e^{-\beta(a)c_\Phi(\delta)}\ =\ 6R^4\Lambda^4\,C_0\,c^{\alpha/2}\,\Big(\ln\tfrac1{a\Lambda}\Big)^{\alpha/2}\,(a\Lambda)^{\,c\,c_\Phi(\delta)-4}.$$

**(ii)** This right-hand side tends to $0$ as $a\to0$ **if and only if**
$$\boxed{\ c\cdot c_\Phi(\delta)\ >\ 4\quad\Longleftrightarrow\quad c_\Phi(\delta)\ >\ \frac4c=\frac{48\pi^2}{11N^2}. }$$
(At $c\,c_\Phi=4$ it diverges like $(\ln\frac1{a\Lambda})^{\alpha/2}$; for $c\,c_\Phi<4$ it diverges like a power of $1/a$.)

**(iii)** By Lemma 2(a), $c_\Phi(\delta)\le\Phi_{\max}(N)\le2$ for every $\delta>0$. Hence for $N\le4$ — in particular for the physical cases $N=2,3$ — **no choice of $\delta$ satisfies (ii)**:
$$\sup_{\delta>0}c\,c_\Phi(\delta)\ \le\ c\,\Phi_{\max}(N)=\begin{cases}0.743022,&N=2,\\ 1.253850,&N=3,\\ 2.972088,&N=4,\end{cases}\qquad\text{all }<4.$$
The deficit factors $4/(c\Phi_{\max})$ are $5.383$ ($N=2$), $3.190$ ($N=3$), $1.346$ ($N=4$).

**(iv)** Refinement for $N\ge5$. By Lemma 2(b), $c_\Phi(\delta)\le4/N$ for $\delta\le\pi\sqrt2\approx4.443$, so (ii) restricted to $\delta\le\pi\sqrt2$ requires $4c/N>4$, i.e. $N>12\pi^2/11=10.767$, i.e. $N\ge11$. Thus for $5\le N\le10$ the only admissible $\delta$ exceed $\pi\sqrt2$; and for any $N$, by Lemma 2(c), (ii) forces
$$\delta\ >\ \sqrt{\frac{96\pi^2}{11N}}=\frac{9.2809}{\sqrt N}\ \ \text{rad (HS)},$$
which is $5.358$ for $N=3$ (exceeding $\mathrm{diam}(\mathrm{SU}(3))=5.130$), $2.798$ for $N=11$, $0.928$ for $N=100$. In every case the admissible $\delta$ is $O(1)$ or larger and grows only like $N^{-1/2}$ — never a 'small-angle' radius.

**Conclusion.** The 'remaining surgical task 2' of PROOF_13 §6 — 'choose $\delta$ and the scaling $\beta(a)$ so the tube failure probability dominates the combinatorics $|P_R|\sim a^{-4}$' — is impossible as stated. The high-probability-convexity bridge cannot be closed by this route.

### Derivation

**(i) The union bound.** $\Omega_{\delta,R}^{\,c}=\bigcup_{p\in P_R}A_{p,\delta}$, so $\mu_\beta(\Omega_{\delta,R}^c)\le\sum_{p\in P_R}\mu_\beta(A_{p,\delta})\le|P_R|\,C_0\beta^{\alpha/2}e^{-\beta c_\Phi(\delta)}$ by Lemma 1. Substituting $|P_R|=6R^4a^{-4}$ and $\beta=c\ln\frac1{a\Lambda}$: write $x:=a\Lambda\to0^+$, so $a^{-4}=\Lambda^4x^{-4}$, $\beta=c\ln\frac1x$, and
$$e^{-\beta c_\Phi(\delta)}=\exp\big(-c\,c_\Phi(\delta)\ln\tfrac1x\big)=x^{\,c\,c_\Phi(\delta)}.$$
Hence the bound equals $6R^4\Lambda^4C_0c^{\alpha/2}\,(\ln\frac1x)^{\alpha/2}\,x^{\,c\,c_\Phi(\delta)-4}$ as claimed.

**(ii) The trichotomy.** As $x\to0^+$, $(\ln\frac1x)^{\alpha/2}x^{\gamma}\to0$ iff $\gamma>0$; $\to\infty$ if $\gamma<0$; and $\to\infty$ (like a power of a logarithm) if $\gamma=0$. With $\gamma=c\,c_\Phi(\delta)-4$ this is exactly (ii). Note that the polynomial prefactor $\beta^{\alpha/2}$ is a *logarithm* of $1/a$ raised to a fixed power and therefore never competes with $a^{-4}$: the entire contest is between the $4$ and $c\,c_\Phi(\delta)$.

*Reading of the criterion.* Solving for the coupling growth actually required: to make the union bound vanish one needs
$$\beta(a)\ \ge\ \frac{4}{c_\Phi(\delta)}\ln\frac1{a\Lambda}\quad\text{with}\quad \frac{4}{c_\Phi(\delta)}\ \ge\ \frac{4}{\Phi_{\max}(N)}\ \ge\ 2,$$
while asymptotic freedom *supplies* only $\beta(a)=c\ln\frac1{a\Lambda}$ with $c=11N^2/(12\pi^2)$. So the demand is 'the coupling must grow logarithmically with slope at least $4/\Phi_{\max}$', and the supply is 'slope $11N^2/12\pi^2$'. Slope-supply exceeds slope-demand iff $11N^2/(12\pi^2)\ge 4/\Phi_{\max}(N)$, i.e. (using $\Phi_{\max}\le2$) iff $N^2\ge24\pi^2/11=21.534$, i.e. $N\ge5$.

**(iii) The arithmetic.** With $c=11N^2/(12\pi^2)$ and $\Phi_{\max}$ from Lemma 2(a):
$$c\,\Phi_{\max}(2)=0.371511\times2=0.743022,\quad c\,\Phi_{\max}(3)=0.835900\times1.5=1.253850,\quad c\,\Phi_{\max}(4)=1.486044\times2=2.972088,$$
all $<4$. Since $c_\Phi(\delta)\le\Phi_{\max}(N)$ for every $\delta$, the requirement (ii) has no solution for $N\in\{2,3,4\}$. For $\mathrm{SU}(3)$ the *best possible* value of the product, taken over all $\delta$ up to the diameter, is $c\cdot\tfrac32=1.2538$: the union bound diverges like $a^{-(4-1.2538)}=a^{-2.746}$ even in the most favourable case, i.e. one is short by a factor $3.19$ in the coupling slope. For $\mathrm{SU}(2)$ the best is $0.7430$, divergence $a^{-3.257}$, short by $5.38$.

**(iv) Beyond $N=4$.** Restricting to $\delta\le\pi\sqrt2$ (where Lemma 2(b) applies) the best product is $c\cdot\frac4N=\frac{11N^2}{12\pi^2}\cdot\frac4N=\frac{11N}{3\pi^2}$, and $\frac{11N}{3\pi^2}>4\iff N>\frac{12\pi^2}{11}=10.7668$. Values of $c\cdot4/N$: $0.743$ ($N=2$), $1.114$ ($N=3$), $1.486$ ($N=4$), $1.858$ ($N=5$), $2.229$ ($N=6$), $2.972$ ($N=8$), $3.715$ ($N=10$), $4.087$ ($N=11$). Using instead the global quadratic bound of Lemma 2(c), (ii) reads $c\delta^2/(2N)>4$, i.e. $\delta^2>\frac{8N}{c}=\frac{96\pi^2}{11N}$, i.e. $\delta>9.2809/\sqrt N$.

**Why this is an obstruction and not merely a lost estimate.** Three independent reasons the loss cannot be recovered inside this framework:

1. *The exponent $c_\Phi(\delta)$ in Lemma 1 is essentially sharp.* At large $\beta$ the plaquette fluctuations are of size $\|\theta_p\|\sim\sqrt{N d_G/\beta}$ and $\mu_\beta(d_G(U_p,I)\ge\delta)\approx e^{-\beta\delta^2/(2N)}=e^{-\beta c_\Phi(\delta)(1+o(1))}$ — the same exponent. So no sharper single-plaquette tail can rescue the count; the constant in the exponent *is* $c_\Phi$.
2. *The polynomial prefactor is irrelevant by construction.* $\beta^{\alpha/2}=(c\ln\frac1{a\Lambda})^{\alpha/2}$ is a power of a logarithm and cannot cancel $a^{-4}$, whatever $\alpha$ is; changing the tiling (block vs plaquette chessboard) changes only $\alpha$.
3. *Enlarging $\delta$ destroys the premise.* $\delta$ is not free: it is constrained by $\delta<\delta_*$, the radius of the 'small-angle sector' in which the horizontal Wilson Hessian floor $\nabla^2S_\beta\ge\beta c_Wg$ is supposed to hold (PROOF_13 §1–2). The values of $\delta$ that (ii) would require ($\delta>5.36$ for $N=3$, i.e. beyond the diameter of $\mathrm{SU}(3)$; $\delta>\pi\sqrt2$ for $N\le10$) correspond to a 'tube' that is all or almost all of the group, where no Hessian positivity statement is available. The two requirements pull in opposite directions and the gap is not marginal: it is a factor $3.19$ in the coupling slope even at the (already vacuous) extreme $\delta=\mathrm{diam}$, and a factor $114.8$ at the still-generous $\delta=0.5$, a factor $2865$ at $\delta=0.1$.

The qualitative statement is the one in the title: at fixed physical volume the number of plaquettes grows like $a^{-4}$, i.e. the *entropy* of ways for the tube to fail grows as a power of $1/a$, while the *energy* penalty per failure grows only like $e^{-\beta c_\Phi}=(a\Lambda)^{c\,c_\Phi}$ with $c\,c_\Phi\le c\,\Phi_{\max}<4$. Power beats power, and the wrong one wins. $\square$

### Constants and numbers

Criterion: c*c_Phi(delta) > 4, c = 11N^2/(12pi^2), threshold 4/c = 48 pi^2/(11 N^2).
N=2: 4/c = 10.7668, sup_delta c_Phi = 2  -> best product 0.7430, deficit factor 5.383, union bound diverges as a^{-3.257}.
N=3: 4/c = 4.7853, sup_delta c_Phi = 1.5 -> best product 1.2538, deficit factor 3.190, union bound diverges as a^{-2.746}.
N=4: 4/c = 2.6917, sup_delta c_Phi = 2  -> best product 2.9721, deficit factor 1.346, diverges as a^{-1.028}.
N=5 is the first N for which c*Phi_max > 4 (4.2004 > 4); N>=11 is the first for which delta <= pi*sqrt2 can work (c*4/N = 4.0866 at N=11).
Required coupling slope vs supplied (N=3, c=0.8359): delta=diam(c_Phi=1.5) -> need 2.667 ln(1/aLambda), short x3.19; delta=0.729 (c_Phi=0.0866) -> need 46.19, short x55.3; delta=0.5 (c_Phi=0.0412) -> need 95.92, short x114.8; delta=0.1 (c_Phi=0.00167) -> need 2395.2, short x2865.4.
General-N necessary condition from the quadratic bound: delta > sqrt(96 pi^2/(11 N)) = 9.2809/sqrt(N)  [N=3: 5.358 > diam(SU(3))=5.130; N=11: 2.798; N=100: 0.928].
Polynomial prefactor: alpha/2 = (N^2-1)/3 = 8/3 for SU(3) — a power of ln(1/a), never competitive with a^{-4}.

**Caveat.** Inherits the conditionality of Lemma 1 on the chessboard estimate; but note the direction — a *weaker* tail bound only makes the obstruction stronger, so the conditionality cannot be exploited to escape it.

**Why it matters.** This is the sharp, quantitative reason a natural and repeatedly attempted strategy — 'prove convexity on the small-field tube, then show the tube is typical' — cannot reach the continuum limit at fixed physical volume. It converts a vague 'union bounds are lossy' worry into a two-line arithmetic refutation with named constants, and it explains structurally why Balaban-type constructions need a large-field/small-field decomposition rather than a global small-field tube.

---

## 6. Theorem D′ (converse: the small-plaquette tube is genuinely atypical — a rigorous lower bound on the failure probability, valid for all δ below an explicit threshold)

`status: solid` · `kind: theorem`

### Statement

Let $d=4$, $G=\mathrm{SU}(N)$, $\mu_\beta$ the Wilson Gibbs measure of Item 1 on a periodic lattice, $B_R$ a fixed physical box, and $\Omega_{\delta,R}=\{U:d_G(U_p,I)<\delta\ \forall p\in P_R\}$. Put
$$\kappa_\delta:=\sup\{\Phi(V):d_G(V,I)\le3\delta\}\ \le\ \frac{9\delta^2}{2N},$$
and assume $2\delta\le\mathrm{diam}(G)$. Then for every $\beta>0$ and every lattice,
$$\boxed{\ \mu_\beta\big(\Omega_{\delta,R}\big)\ \le\ \big(1+e^{-6\beta\kappa_\delta}\big)^{-m}\ \le\ \exp\!\Big(-\tfrac{m}{2}e^{-6\beta\kappa_\delta}\Big),\qquad m\ \ge\ \frac{4}{19}\Big(\frac Ra\Big)^{4}(1-O(a/R)). }$$
Consequently, along $\beta(a)=c\ln\frac1{a\Lambda}$ with $c=\frac{11N^2}{12\pi^2}$, if
$$6\,c\,\kappa_\delta\ <\ 4\qquad\Big(\text{sufficient: }\ \delta\ <\ \frac{4\pi}{3\sqrt{11N}}\Big)$$
then $\mu_{\beta(a)}(\Omega_{\delta,R})\le\exp\big(-\tfrac{2}{19}R^4\Lambda^{6c\kappa_\delta}a^{\,6c\kappa_\delta-4}\big)\to0$ **super-exponentially** in $a^{-(4-6c\kappa_\delta)}$ as $a\to0$.

Explicit thresholds: $\delta<0.8931$ for $\mathrm{SU}(2)$, $\delta<0.7292$ for $\mathrm{SU}(3)$, $\delta<0.6315$ for $\mathrm{SU}(4)$, $\delta<0.3994$ for $\mathrm{SU}(10)$ (Hilbert–Schmidt radians).

### Derivation

[This theorem is my reconstruction. The corpus contains only the negative statement 'the chessboard bound cannot conclude'; the positive statement 'the tube is in fact atypical' is not in the corpus. I mark the whole item as reconstructed. Each step below is elementary and I have checked it.]

The idea: build $2^m$ pairwise disjoint copies of $\Omega_{\delta,R}$ by translating $m$ well-separated links, each copy costing a bounded amount of action. If $2^m\cdot(\text{cost factor})$ exceeds $1$, $\Omega_{\delta,R}$ must be small. This is an *energy–entropy* bound run in the opposite direction from Item 4, and it converts the qualitative slogan 'entropy beats energy' into a theorem.

**Step 1 (a well-separated family of links).** Define a graph on the links of $B_R$ by $\ell\sim\ell'$ iff some plaquette contains both. By Item 1 this graph has maximum degree $18$. Restrict to *interior* links, i.e. links all six of whose plaquettes lie in $P_R$ (all but an $O(a/R)$ fraction). Greedy selection in a graph of maximum degree $18$ yields an independent set $\mathcal L=\{\ell_1,\dots,\ell_m\}$ with
$$m\ \ge\ \frac{|E_R^{\mathrm{int}}|}{19}\ =\ \frac{4(R/a)^4}{19}\,(1-O(a/R)).$$
For each $\ell_r$ pick one plaquette $q_r\ni\ell_r$. The $q_r$ are distinct (a plaquette containing two members of $\mathcal L$ would contradict independence), and $\ell_r\notin\partial q_s$ for $r\neq s$ (else $\ell_r,\ell_s$ would share the plaquette $q_s$).

**Step 2 (the translations).** Fix $h\in G$ with $d_G(h,I)=2\delta$ (possible since $2\delta\le\mathrm{diam}(G)$). For $T\subseteq\{1,\dots,m\}$ define $\Psi_T:\mathscr A\to\mathscr A$ by $(\Psi_TU)_{\ell_r}=hU_{\ell_r}$ for $r\in T$ and $(\Psi_TU)_e=U_e$ otherwise. Each $\Psi_T$ is a diffeomorphism preserving the product Haar measure (left translation on finitely many factors).

**Step 3 (the images are pairwise disjoint).** Let $U\in\Omega_{\delta,R}$ and $U'=\Psi_TU$.
- For $r\in T$: the plaquette holonomy $U'_{q_r}$ equals $hU_{q_r}$ (or $U_{q_r}h^{-1}$, depending on orientation), so by bi-invariance and the triangle inequality $d_G(U'_{q_r},I)\ \ge\ d_G(h,I)-d_G(U_{q_r},I)\ >\ 2\delta-\delta=\delta$.
- For $r\notin T$: no link of $\partial q_r$ was moved (Step 1), so $U'_{q_r}=U_{q_r}$ and $d_G(U'_{q_r},I)<\delta$.
Hence membership in $\Psi_T(\Omega_{\delta,R})$ determines $T$ exactly (via which of the $m$ marked plaquettes are $\ge\delta$), so $\{\Psi_T(\Omega_{\delta,R})\}_{T\subseteq\{1..m\}}$ are pairwise disjoint. ($T=\varnothing$ gives $\Omega_{\delta,R}$ itself.)

**Step 4 (bounded action cost).** The plaquettes whose holonomy changes under $\Psi_T$ are exactly the $6|T|$ plaquettes containing some $\ell_r$, $r\in T$ — and each such plaquette contains exactly one $\ell_r$ (Step 1), so there is no double counting. For such a plaquette $p\ni\ell_r$ with $p\in P_R$ (guaranteed since $\ell_r$ is interior) and $U\in\Omega_{\delta,R}$:
$$d_G(U'_p,I)\ \le\ d_G(U_p,I)+d_G(h,I)\ <\ \delta+2\delta=3\delta\ \Longrightarrow\ \Phi(U'_p)\le\kappa_\delta.$$
Since $\Phi\ge0$,
$$S_\beta(\Psi_TU)-S_\beta(U)=\beta\!\!\sum_{p:\ \exists r\in T,\ \ell_r\in\partial p}\!\!\big[\Phi(U'_p)-\Phi(U_p)\big]\ \le\ 6\beta\kappa_\delta|T|.$$

**Step 5 (measure comparison).** Using the Haar-invariance of $\Psi_T$ and Step 4,
$$\mu_\beta\big(\Psi_T(\Omega_{\delta,R})\big)=\frac1{Z_\beta}\int_{\Omega_{\delta,R}}e^{-S_\beta(\Psi_TU)}\mathrm{d}\mathrm{vol}(U)\ \ge\ e^{-6\beta\kappa_\delta|T|}\,\mu_\beta(\Omega_{\delta,R}).$$

**Step 6 (sum over $T$).** By Step 3 the images are disjoint, so
$$1\ \ge\ \sum_{T\subseteq\{1..m\}}\mu_\beta(\Psi_T(\Omega_{\delta,R}))\ \ge\ \mu_\beta(\Omega_{\delta,R})\sum_{k=0}^{m}\binom mk e^{-6\beta\kappa_\delta k}=\mu_\beta(\Omega_{\delta,R})\big(1+e^{-6\beta\kappa_\delta}\big)^{m}.$$
Hence $\mu_\beta(\Omega_{\delta,R})\le(1+\varepsilon_\beta)^{-m}$ with $\varepsilon_\beta=e^{-6\beta\kappa_\delta}\in(0,1]$, and $\ln(1+\varepsilon)\ge\varepsilon-\varepsilon^2/2\ge\varepsilon/2$ on $(0,1]$ gives $\mu_\beta(\Omega_{\delta,R})\le e^{-m\varepsilon_\beta/2}$.

**Step 7 (insert the asymptotically free trajectory).** With $\beta(a)=c\ln\frac1{a\Lambda}$, $\varepsilon_{\beta(a)}=(a\Lambda)^{6c\kappa_\delta}$, and $m\ge\frac4{19}R^4a^{-4}$:
$$\frac m2\varepsilon_{\beta(a)}\ \ge\ \frac{2}{19}R^4\Lambda^{6c\kappa_\delta}\,a^{\,6c\kappa_\delta-4}\ \longrightarrow\ \infty \quad\text{iff}\quad 6c\kappa_\delta<4.$$

**Step 8 (explicit $\delta$ threshold).** $6c\kappa_\delta<4\iff\kappa_\delta<\frac{2}{3c}=\frac{8\pi^2}{11N^2}$. Using $\kappa_\delta\le\frac{9\delta^2}{2N}$ (Item 1's global bound applied at radius $3\delta$), it suffices that
$$\frac{9\delta^2}{2N}<\frac{8\pi^2}{11N^2}\iff\delta^2<\frac{16\pi^2}{99\,N}\iff\delta<\frac{4\pi}{3\sqrt{11N}}. \qquad\square$$

**Reading.** Each translated link buys six 'bad plaquette' slots at an action cost of at most $6\beta\kappa_\delta$, and there are $\asymp a^{-4}$ mutually non-interfering links. So the *entropy of ways to break the tube* is $2^{\,\Theta(a^{-4})}$ while the Boltzmann suppression of each breaking is only $e^{-6\beta\kappa_\delta}=(a\Lambda)^{6c\kappa_\delta}$ — again a power of $a$, and again the wrong power wins. Structurally this is the *same* $4$ versus $c\times(\text{energy scale})$ contest as Theorem D; Theorem D says the chessboard route cannot prove the tube typical, Theorem D′ says it is in fact atypical.

**Coverage.** For $\mathrm{SU}(3)$ the threshold $\delta<0.7292$ HS-rad corresponds, for a plaquette rotating in one $\mathrm{SU}(2)$ direction ($\theta=(u,-u,0)$, $\delta=u\sqrt2$), to $u<0.516$ rad $\approx29.5^\circ$ — vastly larger than any 'small-angle sector'. In particular it covers the corpus's own numerically measured convex-core radius $R(\beta)\approx0.14/\beta$ (which is $0.023$ at $\beta=6$) by more than an order of magnitude. So on the entire range of $\delta$ for which a Wilson-Hessian convexity floor could conceivably hold, the tube event has probability tending to zero.

**Gap that remains (stated honestly).** Theorem D excludes $\delta$ with $c\,c_\Phi(\delta)\le4$ (i.e. all $\delta$ for $N\le4$), Theorem D′ proves atypicality for $6c\kappa_\delta<4$. For large $N$ there is an undecided window $3.789/\sqrt N\lesssim\delta\lesssim9.281/\sqrt N$ where neither argument applies. For $N=2,3,4$ Theorem D already covers everything, and for all $N$ Theorem D′ covers the whole small-angle regime, so the window is of no relevance to the intended application.

### Constants and numbers

Max degree of the link 'co-plaquette' graph in 4D: 18; independent-set fraction >= 1/19; m >= (4/19)(R/a)^4.
Action cost per translated link: <= 6 beta kappa_delta, kappa_delta := sup{Phi(V): d(V,I) <= 3 delta} <= 9 delta^2/(2N).
Criterion 6 c kappa_delta < 4, i.e. kappa_delta < 2/(3c) = 8 pi^2/(11 N^2):
  N=2: kappa < 1.794474  -> delta < 0.893053
  N=3: kappa < 0.797544  -> delta < 0.729175
  N=4: kappa < 0.448618  -> delta < 0.631484
  N=5: kappa < 0.287116  -> delta < 0.564816
  N=10: kappa < 0.071779 -> delta < 0.399385
  N=100: kappa < 0.000718 -> delta < 0.126297
General threshold delta < 4 pi/(3 sqrt(11 N)) = 3.7890/sqrt(N) HS-rad.
Decay rate: mu_beta(Omega) <= exp(-(2/19) R^4 Lambda^{6 c kappa} a^{6 c kappa - 4}); e.g. SU(3), delta=0.1: kappa_delta <= 9(0.01)/6 = 0.015, 6 c kappa = 0.0752, so mu <= exp(-const * a^{-3.925}).
Corpus cross-check: measured SU(3) convex-core radius R(beta) ≈ 0.14/beta (L=4,6,8; beta in [0.4,3.0]) = 0.023 at beta=6, far inside the threshold 0.729.

### Code

# Verification of the Theorem D' thresholds and the Theorem D arithmetic.
# Run: python thresholds.py   (needs only the standard library)
import math

def c_AF(N):            # asymptotic-freedom slope, beta(a) = c ln(1/(a Lambda))
    return 11*N*N/(12*math.pi**2)

def Phi_max(N):         # max of Phi over SU(N)
    return 2.0 if N % 2 == 0 else 1 + math.cos(math.pi/N)

for N in (2,3,4,5,10,100):
    c   = c_AF(N)
    # --- Theorem D: union bound is o(1) iff c*c_Phi(delta) > 4 ---
    need = 4/c                               # required c_Phi
    best = Phi_max(N)                        # best possible c_Phi over all delta
    # --- Theorem D': tube is atypical if 6 c kappa_delta < 4, kappa <= 9 d^2/(2N) ---
    kap_max = 2/(3*c)
    d_star  = 4*math.pi/(3*math.sqrt(11*N))
    print(f"N={N:4d}  c={c:9.6f}  4/c={need:9.6f}  Phi_max={best:8.6f}  "
          f"c*Phi_max={c*best:9.6f} {'FAILS(<4)' if c*best<4 else 'passes'}   "
          f"| D': kappa<{kap_max:.6f}, delta<{d_star:.6f}")

**Caveat.** Entirely my reconstruction — this theorem is not in the corpus. The constants (19, factor 6, the 3δ radius) are not optimised; sharpening them widens the δ-range but the structure (entropy a^{-4} versus energy a^{6cκ}) is what matters.

**Why it matters.** It upgrades the obstruction from 'this proof technique cannot conclude' to 'the conclusion is false'. That is the difference between a lost estimate and a genuine no-go, and it makes the counting obstruction a first-class negative result rather than a critique of a bound.

---

## 7. Complement: the averaged-badness event evades the union bound but does not deliver the pointwise small-field set (the alignment gap)

`status: gap` · `kind: construction`

### Statement

Let $\vartheta:G\to[0,2]$ be $C^1$, conjugation-invariant, $\vartheta(I)=0$, $\|\nabla_G\vartheta\|_\infty<\infty$ (e.g. $\vartheta=\Phi$), and set
$$\overline{\vartheta}_\Lambda(U):=\frac{1}{|P|}\sum_{p\in P}\vartheta(U_p),\qquad K_\Lambda(\varepsilon):=\{\overline{\vartheta}_\Lambda\le\varepsilon\}.$$
Then (i) $\overline{\vartheta}_\Lambda$ is gauge invariant and $O(|P|^{-1/2})$-Lipschitz: $\sup_U|\nabla\overline{\vartheta}_\Lambda|\le L_0/\sqrt{|P|}$ with $L_0=\nu\|\nabla_G\vartheta\|_\infty\sqrt{|E|/|P|}$, $\nu=2(d-1)=6$; and (ii) if $r>0$ and $\varepsilon\in(0,2)$ satisfy
$$c_{\mathrm{typ}}:=\beta\big(\varepsilon-L_\vartheta m_\partial r\big)-c_{E:P}\,\chi_G(r)>0,\qquad \chi_G(r):=\log\frac{\mathrm{vol}(G)}{\mathrm{vol}(B_r)},\ m_\partial=4,\ c_{E:P}=\tfrac{|E|}{|P|}=\tfrac23,$$
then $\mu_{\Lambda,\beta}\big(K_\Lambda(\varepsilon)^c\big)\le e^{-c_{\mathrm{typ}}|P(\Lambda)|}$ — an *extensive* exponential bound with **no union-bound factor at all**.

**The gap.** The convexity/hinge input requires the *pointwise* small-field set $\Omega_{\delta,R}=\{\forall p\in P_R:\ d_G(U_p,I)<\delta\}$, not the averaged set $K_\Lambda(\varepsilon)$. On $K_\Lambda(\varepsilon)$ a fraction $\le\varepsilon/c_\Phi(\delta)$ of plaquettes may be $\delta$-bad, and by Theorem D′ that fraction is bounded away from zero at any fixed $\varepsilon>0$ along the continuum trajectory. No proof that the hinge/Hessian floor tolerates a positive density of defects exists in the corpus.

### Derivation

**(i) Lipschitz scaling.** With the product metric, $|\nabla f|^2=\sum_{\ell\in E}|\nabla_\ell f|^2$. Each $\vartheta_p$ depends only on the $4$ links of $\partial p$, and $|\nabla_\ell\vartheta_p|\le\|\nabla_G\vartheta\|_\infty\mathbf1_{\{\ell\in\partial p\}}$ by bi-invariance. Since $\nabla_\ell\overline{\vartheta}_\Lambda=|P|^{-1}\sum_{p\ni\ell}\nabla_\ell\vartheta_p$ and $\deg_P(\ell)=\nu=6$,
$$|\nabla_\ell\overline{\vartheta}_\Lambda|\le\frac{\nu\|\nabla_G\vartheta\|_\infty}{|P|}\ \Longrightarrow\ |\nabla\overline{\vartheta}_\Lambda|\le\frac{\nu\|\nabla_G\vartheta\|_\infty}{|P|}\sqrt{|E|}=\frac{\nu\|\nabla_G\vartheta\|_\infty\sqrt{|E|/|P|}}{\sqrt{|P|}}.$$
At $d=4$: $L_0=6\|\nabla_G\vartheta\|_\infty\sqrt{2/3}$.

**(ii) Typicality.** On $K^c$, $S_\beta=\beta|P|\,\overline{\vartheta}_\Lambda>\beta\varepsilon|P|$, so the numerator of $\mu(K^c)$ is $\le e^{-\beta\varepsilon|P|}\mathrm{vol}(\mathscr A)$. For the denominator restrict to $\mathcal A(r)=\{U_\ell\in B_r(I)\ \forall\ell\}$: there each $\vartheta_p\le L_\vartheta\cdot m_\partial r$ ($m_\partial=4$ links per plaquette, $L_\vartheta$ the Lipschitz constant of $\vartheta$), so $Z\ge e^{-\beta L_\vartheta m_\partial r|P|}\mathrm{vol}(B_r)^{|E|}$. Dividing and using $\mathrm{vol}(\mathscr A)=\mathrm{vol}(G)^{|E|}$,
$$\mu(K^c)\le\exp\Big(-\beta|P|\big(\varepsilon-L_\vartheta m_\partial r\big)+|E|\chi_G(r)\Big)=\exp\big(-c_{\mathrm{typ}}|P|\big),$$
with $c_{\mathrm{typ}}=\beta(\varepsilon-L_\vartheta m_\partial r)-\frac{|E|}{|P|}\chi_G(r)$. Note this is the *same* small-product-ball entropy input as Lemma 1 step 4, deployed without any chessboard and without any union bound — which is exactly why it produces $e^{-c_{\mathrm{typ}}|P|}$ instead of $|P_R|e^{-\beta c_\Phi}$.

**Why this does not rescue the programme.** The reason the average works is that it is a *single* $|P|^{-1/2}$-Lipschitz functional, so concentration applies once rather than $|P_R|$ times. But the analytic input needed downstream (the horizontal Wilson-Hessian floor $\nabla^2S_\beta\ge\beta c_Wg$ of PROOF_13 §1) is a *pointwise* statement about every plaquette in the region. Converting $\{\overline\vartheta\le\varepsilon\}$ into $\{\max_{p\in P_R}\vartheta_p\le\delta\}$ costs exactly the union bound one was trying to avoid, and by Markov's inequality the best one gets is a *density* statement: on $K_\Lambda(\varepsilon)$,
$$\#\{p\in P: d_G(U_p,I)\ge\delta\}\ \le\ \frac{\varepsilon}{c_\Phi(\delta)}\,|P|,$$
which is a positive density of defects for any fixed $\varepsilon>0$ and small $\delta$ — and Theorem D′ shows the defect density does not go to zero along the continuum trajectory. The corpus states this open problem explicitly (Exciting_04 §5, 'Open alignment problem'; EXCITING_05 §4, 'Where the project is honest about a remaining gap') and proposes three routes (corridor-local small-field events; a multi-scale hinge tolerating sparse defects; a chessboard bound on the small-field set directly). The third is refuted by Theorem D; the first two are unattempted.

**One further honest note on the second route.** 'Sparse defects' is the right instinct and is precisely the large-field/small-field decomposition of Balaban-type constructive renormalisation: one does *not* try to make the small-field region typical, one instead controls the large-field region with its own expansion. The counting obstruction of Theorem D is the quantitative statement of why that decomposition is unavoidable.

### Constants and numbers

nu = 2(d-1) = 6 plaquettes per link; m_partial = 4 links per plaquette; c_{E:P} = |E|/|P| = 2/3; L_0 = 6 ||grad theta||_inf sqrt(2/3) ≈ 4.899 ||grad theta||_inf; Lipschitz constant of the averaged badness = L_0 |P|^{-1/2}; typicality exponent c_typ = beta(eps - 4 L_theta r) - (2/3) chi_G(r), chi_G(r) = log(vol G / vol B_r); resulting bound mu(K^c) <= exp(-c_typ |P|). Markov defect-density bound on K(eps): fraction of delta-bad plaquettes <= eps/c_Phi(delta) (e.g. SU(3), eps=0.01, delta=0.5: <= 0.01/0.041236 = 0.2425, i.e. up to 24% of plaquettes may be bad).

**Caveat.** Status 'gap': the averaged typicality estimate is correct and volume-exponential, but the bridge from an averaged good set to the pointwise small-field set required by the Hessian floor does not exist, and Theorem D′ shows it cannot be a clean implication.

**Why it matters.** It shows the obstruction is not an artifact of choosing a max-event: the max-event is refuted (Theorems D, D'), and the average-event that survives the counting does not supply the analytic input. Both branches of the corpus's own strategy are accounted for.

---

## 8. Reproducible computation of Φ_max(N), c_Φ(δ), and the two thresholds

`status: solid` · `kind: code`

### Statement

A single self-contained Python script (standard library + numpy) that (a) computes $\min_{\mathrm{SU}(N)}\mathrm{Re}\,\mathrm{Tr}\,V$ by exact stationary-point enumeration on the maximal torus and confirms $\Phi_{\max}(N)=2$ ($N$ even), $1+\cos(\pi/N)$ ($N$ odd); (b) tabulates $c_\Phi^{\mathrm{SU}(3)}(\delta)$ exactly by minimising $\Phi$ over the $\mathrm{SU}(3)$ maximal torus with $2\pi$-shift-lattice minimisation of the distance, and checks it against the $\mathrm{SU}(2)$-embedding bound of Lemma 2(b); (c) prints the Theorem D criterion $c\,c_\Phi>4$ and the Theorem D′ threshold $\delta<4\pi/(3\sqrt{11N})$ for a range of $N$.

### Derivation

The three functions are independent and each verifies a distinct claim.

*(a) Stationary-point enumeration.* Minimising $\sum_j\cos t_j$ subject to $\sum_j t_j\equiv0\ (2\pi)$ has Lagrange condition $\sin t_j=\lambda\ \forall j$, hence $t_j\in\{\alpha,\pi-\alpha\}$; parametrising by $k=\#\{j:t_j=\pi-\alpha\}$ and the winding $m$, the constraint fixes $\alpha=(2\pi m-k\pi)/(N-2k)$ and the objective is $(N-2k)\cos\alpha$. Enumerating $k\in\{0..N\}$, $m\in\{-N-2,..,N+2\}$ finds the global minimum. Cross-checked for $N=3$ against a $1200\times1200$ grid on the torus (agreement to $1.2\times10^{-6}$).

*(b) $c_\Phi$ on the torus.* For each pair $(t_1,t_2)$ on a $1400\times1400$ grid, set $t_3=-(t_1+t_2)$, minimise $\sum(t_j+2\pi n_j)^2$ over $n\in\{-2..2\}^2$ with $\sum n_j=0$ to get the true geodesic distance $d$, then evaluate $\Phi$; finally $c_\Phi(\delta)=\min\{\Phi:\ d\ge\delta\}$. Recovers $\mathrm{diam}(\mathrm{SU}(3))=5.129283$ against the exact $(2\pi/3)\sqrt6=5.130199$ and $\max\Phi=1.4999997$ against $3/2$.

*(c) Thresholds.* Direct evaluation of $c=11N^2/(12\pi^2)$, $4/c$, $c\,\Phi_{\max}$, $c\cdot4/N$, $2/(3c)$, $4\pi/(3\sqrt{11N})$.

### Constants and numbers

Outputs reproduced in Items 2–5: min ReTr over SU(N) for N=2..14 = -2, -1.5, -4, -4.045085, -6, -6.306782, -8, -8.457234, -10, -10.554423, -12, -12.622244, -14; diam(SU(3)) = 5.129283 (grid) vs 5.130199 (exact); max Phi over SU(3) = 1.4999997 vs 3/2; c_Phi^{SU(3)} vs (2/3)(1-cos(delta/sqrt2)) agree to <= 1.2e-4 for delta <= 4.44; c*Phi_max = 0.743022 (N=2), 1.253850 (N=3), 2.972088 (N=4), 4.200436 (N=5); Theorem D' thresholds 0.893053 (N=2), 0.729175 (N=3), 0.631484 (N=4).

### Code

# cphi_thresholds.py  —  verifies every constant in Items 2, 3, 4, 5.
# Run:  python cphi_thresholds.py        (numpy only)
import numpy as np, math

# ---------- (a) Phi_max(N) = 1 - min_{SU(N)} ReTr(V)/N ----------
def min_retr_exact(N):
    """Stationary points of sum_j cos t_j s.t. sum t_j = 0 mod 2pi have sin t_j = const,
       so t_j in {alpha, pi-alpha}: k entries pi-alpha, N-k entries alpha,
       (N-2k)alpha + k pi = 2 pi m,  objective (N-2k) cos alpha."""
    best, arg = 1e9, None
    for k in range(N+1):
        d = N - 2*k
        if d == 0: continue
        for m in range(-N-2, N+3):
            alpha = (2*math.pi*m - k*math.pi)/d
            v = d*math.cos(alpha)
            if v < best - 1e-12: best, arg = v, (k, m, alpha)
    return best, arg

def Phi_max(N):
    return 1 - min_retr_exact(N)[0]/N          # == 2 (N even), 1+cos(pi/N) (N odd)

# ---------- (b) exact c_Phi(delta) for SU(3) on the maximal torus ----------
def su3_table(n=1400):
    g = np.linspace(-math.pi, math.pi, n)
    T1, T2 = np.meshgrid(g, g, indexing='ij')
    T1, T2 = T1.ravel(), T2.ravel()
    best_d2 = np.full(T1.shape, np.inf); bt = None
    for n1 in range(-2, 3):
        for n2 in range(-2, 3):
            a = T1 + 2*math.pi*n1; b = T2 + 2*math.pi*n2; c = -(a+b)
            d2 = a*a + b*b + c*c
            m = d2 < best_d2
            if bt is None: bt = [a.copy(), b.copy(), c.copy()]
            for arr, new in zip(bt, (a, b, c)): arr[m] = new[m]
            best_d2 = np.minimum(best_d2, d2)
    d = np.sqrt(best_d2)
    phi = (3 - np.cos(bt[0]) - np.cos(bt[1]) - np.cos(bt[2]))/3
    return d, phi

def c_Phi(d, phi, delta):
    m = d >= delta - 1e-12
    return float(phi[m].min()) if m.any() else float('nan')

# ---------- (c) the two thresholds ----------
c_AF = lambda N: 11*N*N/(12*math.pi**2)        # beta(a) = c ln(1/(a Lambda))

if __name__ == '__main__':
    print('N  minReTr      Phi_max    c        4/c       c*Phi_max  D-passes?  '
          'kappa_max=2/3c  delta*<4pi/(3sqrt(11N))')
    for N in (2,3,4,5,6,8,10,11,12):
        c, pm = c_AF(N), Phi_max(N)
        print(f'{N:2d} {min_retr_exact(N)[0]:10.6f} {pm:9.6f} {c:9.6f} {4/c:9.6f} '
              f'{c*pm:9.6f}  {"yes" if c*pm>4 else "NO":3s}      '
              f'{2/(3*c):12.6f}  {4*math.pi/(3*math.sqrt(11*N)):9.6f}')
    d, phi = su3_table()
    print(f'\nSU(3): diam = {d.max():.6f}  (exact (2pi/3)sqrt6 = {(2*math.pi/3)*math.sqrt(6):.6f});'
          f'  max Phi = {phi.max():.6f}  (exact 1.5)')
    print('delta   c_Phi^SU(3)   (2/3)(1-cos(delta/sqrt2))   delta^2/6   c(N=3)*c_Phi')
    for delta in (0.05,0.1,0.2,0.3,0.5,0.729,1.0,1.5,2.0,3.0,4.0,4.4429,5.12):
        v = c_Phi(d, phi, delta)
        emb = (2/3)*(1-math.cos(delta/math.sqrt(2))) if delta <= math.pi*math.sqrt(2) else float('nan')
        print(f'{delta:6.4f} {v:12.6f} {emb:24.6f} {delta**2/6:11.6f} {c_AF(3)*v:12.6f}')

**Caveat.** The SU(3) c_Φ table is a fine-grid evaluation on the maximal torus (grid 1400², error ~1e-3 in δ, ~1e-4 in Φ), not a certified enclosure; the closed forms in Lemma 2 are exact and are what the argument uses.

**Why it matters.** Every number quoted in the obstruction is reproducible in under a minute from a 60-line script, so the two-line refutation can be checked rather than believed.

---

## How these fit together

The seven items form one closed argument, and it plugs into three other obstruction results elsewhere in the corpus.

INTERNAL LOGIC. Item 1 fixes normalisations (this is the step the source leaves implicit and where a factor of N or 2 would move every number). Item 2 is the corpus's own Lemma 3.1 — the positive half — reproduced in full with all constants made explicit; it is correct and its key feature, volume-uniformity via the 1/|P| chessboard root, is genuine. Item 3 is the only quantity a would-be prover can tune (via δ), and it is bounded by an absolute constant ≤ 2. Item 4 is the elementary derivation of the coupling slope c = 11N²/(12π²) from one-loop asymptotic freedom. Item 5 (Theorem D) collides Items 2–4: the union bound over 6(R/a)⁴ plaquettes is o(1) iff c·c_Φ(δ) > 4, and sup_δ c·c_Φ ≤ c·Φ_max = 1.254 (N=3), 0.743 (N=2) — short by factors 3.19 and 5.38. Item 6 (Theorem D′) is my addition and is what turns the result from 'the method cannot conclude' into 'the conclusion is false': an explicit 2^m-disjoint-copies energy/entropy argument shows the tube probability actually tends to zero for every δ < 4π/(3√(11N)) (0.729 rad for SU(3)), which covers the entire small-angle regime by more than an order of magnitude. Item 7 accounts for the corpus's own escape hatch — the averaged-badness event, which correctly evades the union bound and gives an extensive bound e^{-c_typ|P|}, but delivers only a defect-*density* statement, not the pointwise small-field set the Hessian floor needs. Item 8 makes all constants reproducible.

RELATION TO THE REST OF THE CORPUS. This is 'Theorem D' of the corpus's own no-go paper sketch (_EXTRACT_FOR_LLM/04_papers/PAPER-1-curvature-no-go/ABSTRACT.md). Its three siblings are independent and mutually reinforcing:
- Theorem A (global Bakry-Émery constant): ρ_glob(a) ≤ k_max − β(a)λ → −∞ along β(a) = 2N/g²(a). Same structure as here — a fixed O(1) geometric quantity is beaten by a growing β — but read in the opposite direction.
- Theorem B (gauge invariance forces exactly-Haar link marginals, so the *link* small-field set has probability ≤ Haar(B_r)^{|E|−|V|+1}, exponentially small in the volume). Theorem B kills the link-level tube unconditionally at every β and volume; Theorem D/D′ kill the *plaquette*-level tube, which Theorem B cannot reach because plaquette holonomies are gauge invariant. The two are complementary, not redundant, and the link-level union bound of WILSON/01_core_theorems/YM_extract_02_outlier_exclusion_convex_core.md §('three union bounds') is the object Theorem B refutes.
- Theorem C (scaling dichotomy: a curvature floor is O(1) in lattice units, so m_phys = λ*/a → ∞ or ≍ a g₀²(a) → 0, never Λ = a^{-1}e^{-1/2b₀g₀²}). Theorem D is the probabilistic shadow of the same fact.
Together: Theorem A closes the global route, D/D′ close the 'retreat to a high-probability small-field tube' route, C closes the 'accept the local floor and push it to physics' route, and B closes the link-level version of the tube.

The source document PROOF_13 §6 lists exactly two 'remaining surgical tasks'; Theorem D shows task 2 is impossible and task 1 (formalising the chessboard estimate in the gauge setting) is irrelevant because a *sharper* tail bound cannot help — the exponent c_Φ(δ) is already essentially optimal (large-β Gaussian heuristic in Item 5's derivation) and a weaker one only strengthens the obstruction.

DUPLICATION NOTE. The three copies of PROOF_13 that I used (RICCATI/04_misc_docs, RICCATI/archive, HESSIAN/Core_Hessian) are byte-identical: 9681 bytes, md5 d8aa4d5759f977f64d7203cfb22b74a1. Five further identical copies sit in LSI_POINCARE/05_proofs_reports, REFLECTION_POSITIVITY/08_MISC, RG_COARSE/00_Documentation_Indices, WILSON/archive, HESSIAN/archive/duplicates. There is no 'better version'; I extracted from RICCATI/04_misc_docs.

PRIOR ART. The chessboard tail bound is standard constructive-QFT material (Osterwalder–Seiler for RP of the Wilson measure; Fröhlich–Israel–Lieb–Simon for chessboard estimates), routinely used to show plaquette concentration at large β. The counting obstruction is qualitatively understood by constructive field theorists — it is exactly why Balaban's renormalisation uses a large-field/small-field decomposition rather than a global small-field tube — but I have not located it written as a sharp arithmetic refutation with the explicit constant 48π²/(11N²), nor with a matching lower bound of the Theorem D′ type. Novelty is therefore presentational for D and possibly small-but-real for D′.

## Further material found but not fully extracted

Left on the table in this area:

1. PROOF_13 §1 input is separately false and unexamined. The claimed 'horizontal convexity' ∇²S_β ≥ βc_W g uniform over small-angle configurations cannot hold uniformly in volume: near U = I the Wilson Hessian is (β/N) d₁*d₁, a lattice curl-curl operator whose smallest nonzero eigenvalue on horizontal (transverse) directions scales like (2π/L)² and hence vanishes as the volume grows. This is a *second*, independent failure of the same document, orthogonal to the counting obstruction, and it is worth writing up properly — it is the volume-uniformity failure that the entire Bakry-Émery programme rests on. I did not verify the (2π/L)² claim by explicit spectral computation.

2. PROOF_13 Prop 4.1 (defective local Poincaré, Var ≤ ρ_loc^{-1}∫|∇F|² + 4‖F‖²_∞ μ(Ω^c)) is asserted without proof. It is easy to prove correctly by the two-set variance decomposition (the exact law-of-total-covariance identity is given in full in REFLECTION_POSITIVITY/04_GAP_BRIDGES/Exciting_04_Localization_Typicality_Bridge.md §2 and WILSON/08_misc_docs/EXCITING_05_LOCALIZATION_AVERAGED_BADNESS.md Lemma 1.1, both correct), and the honest version has defect 8‖F‖_∞‖G‖_∞ μ(K^c), not 4‖F‖²_∞. It is worth extracting as a clean lemma — it is genuinely correct and reusable — but by Theorem D′ its defect term does not vanish, so it is a lemma without an application here.

3. The opposite-regimes problem. The convexity window ρ_* > 0 that the corpus's Riccati/PBH machinery needs lives at *small* β, while the tube estimate lives at *large* β. The two halves of the programme require opposite coupling regimes and this is never reconciled anywhere in the corpus. A one-page note making the two windows explicit and showing they are disjoint would be a clean fourth obstruction.

4. Sharpening Theorem D′. My constants (independent-set fraction 1/19, the factor 6 from plaquettes-per-link, the 3δ dilation) are all crude. A smarter move — translating a link by a *small* h and using the conditional heat-bath law of U_ℓ given its six staples (density ∝ exp((β/N)Re Tr(U_ℓ Σ_ℓ)), Σ_ℓ ≈ 6U_ℓ^{-1} on the tube, giving fluctuations ~ β^{-1/2} and per-link failure ~ e^{-6βc_Φ(δ)}) — would replace 6κ_δ by roughly 6c_Φ(δ) and shrink the undecided window at large N from [3.79/√N, 9.28/√N] to nearly nothing. I sketched this but did not complete it.

5. The corpus's supporting numerics that quantify Theorem D′'s coverage: multi-volume SU(3) Hessian scans (L = 4, 6, 8; β ∈ [0.4, 3.0]) giving a convex-core radius R(β) ≈ 0.14/β, L-independent to ~1%, and an SU(2) one-link convexity threshold β_c = 4.4139 (CAND-018, CAND-019). These were not re-run here; if they hold up they give an independent, measured value of δ_* that is 30× inside my threshold.

6. COLAB_RUNS/04_misc_notebooks/Untitled116.ipynb matched the '11N²' grep but contains nothing relevant to this topic on inspection.
