# PROOF 13: High-Probability Convexity Bridge Lemma (HP → PBH/IR)

**Status:** NEW (Bridge Lemma; uses standard Reflection Positivity / Chessboard estimate)

**Goal:** Provide a *single quantitative interface lemma* turning the existing **local Bakry–Émery floor** (Haar/Wilson convexity near the identity) into a **high-probability statement on the support of** \(\mu_a\). This is the missing “glue” needed so the already-built PBH/Riccati + IR topology-decoupling machinery can run as an *actual locking mechanism* rather than a wish.

---

## 0. Setup

Let \(\Lambda\) be a finite periodic \(4\)-D hypercubic lattice (spacing \(a\)), with oriented edge set \(E\) and plaquette set \(P\). Let \(G=\mathrm{SU}(N)\). The configuration space is
\[
\mathscr A := G^{E}
\]
with the product Haar Riemannian metric \(g\) and volume form \(d\mathrm{vol}_g\).

For \(U\in\mathscr A\), write \(U_p\in G\) for the oriented plaquette holonomy.

We take the Wilson action in the normalized form
\[
S_\beta(U) := \beta\sum_{p\in P} \Phi(U_p),
\qquad \Phi(V):=\frac{1}{N}\,\mathrm{ReTr}(I-V)\in[0,2].
\]
The Gibbs measure is
\[
 d\mu_\beta(U) := Z_\beta^{-1} e^{-S_\beta(U)}\, d\mathrm{vol}_g(U).
\]

We write \(d_G(\cdot,\cdot)\) for the Riemannian distance on \(G\) induced by the bi-invariant metric, and also use the product distance on \(\mathscr A\).

---

## 1. The local convexity floor (input)

From the “geometric mass derivation” (Pillar I), there is a *small-angle sector* in which the Wilson Hessian is strictly positive on horizontal directions, and the Haar curvature contributes a fixed positive Ricci term.

Concretely, near the identity sector (small plaquette angles),
\[
\nabla^2 S_\beta\big|_{P_0T_U\mathscr A} \;\ge\; \beta c_W\, g
\]
for some \(c_W>0\), uniform over small-angle configurations, and the Bakry–Émery tensor is
\(\mathrm{Ric}_{\mu_\beta}=\mathrm{Ric}_g+\nabla^2S_\beta\) with \(\mathrm{Ric}_g=\kappa g\), \(\kappa>0\).  
(See PROOF 04 and supporting Lemmas 3.2–3.4.)

---

## 2. A quantitative “tube” event

Fix \(\delta\in(0,\delta_*)\), where \(\delta_*\) is small enough that the horizontal convexity bound above holds whenever all relevant plaquettes satisfy \(d_G(U_p,I)\le\delta\).

### 2.1 Global tube
Define the (global) small-plaquette event
\[
\Omega_\delta := \{U\in\mathscr A: \forall p\in P,\ d_G(U_p,I)\le\delta\}.
\]

### 2.2 Local tube (for a physical ball \(B_R\))
Let \(P_R\subset P\) be the set of plaquettes intersecting a fixed physical region \(B_R\) (in lattice units \(R/a\)). Define
\[
\Omega_{\delta,R} := \{U\in\mathscr A: \forall p\in P_R,\ d_G(U_p,I)\le\delta\}.
\]

On \(\Omega_{\delta,R}\), the *local* Hessian block \(H^{\mathrm{loc}}\) (restricted to variations supported in \(B_R\)) inherits the same curvature floor used as “Pillar I” input in the UV/IR arguments.

---

## 3. Bridge Lemma (High-probability convexity from RP + a small ball)

### Lemma 3.1 (Single-plaquette tail bound)
Assume the Wilson lattice measure is **reflection positive** (RP) on the unfixed lattice configuration space, hence satisfies the standard **chessboard estimate** for plaquette events.

For any fixed plaquette \(p\in P\), define the bad event
\[
A_{p,\delta} := \{U\in\mathscr A: d_G(U_p,I)\ge\delta\}.
\]
Then there exist constants \(c_\Phi(\delta)>0\), \(C_0>0\), and \(\alpha>0\) depending only on \(G\) (and lattice dimension), such that for all \(\beta\ge 1\),
\[
\mu_\beta(A_{p,\delta})\;\le\;C_0\,\beta^{\alpha}\,e^{-\beta c_\Phi(\delta)}.
\]
Moreover for small \(\delta\), one can take \(c_\Phi(\delta)\simeq c\,\delta^2\) by the small-angle expansion \(\mathrm{ReTr}(e^\theta)=N-\tfrac12\|\theta\|^2+O(\|\theta\|^3)\).

#### Proof (quantitative sketch; the key cancellation is the \(1/|P|\) root)
1. **Energy cost of a bad plaquette.** Define
   \(
   c_\Phi(\delta):=\inf\{\Phi(V): d_G(V,I)\ge\delta\}>0.
   \)
   Then on the event that *every plaquette is \(\delta\)-bad*, we have
   \(
   S_\beta(U)\ge\beta |P|\,c_\Phi(\delta).
   \)

2. **Chessboard estimate reduces a local probability to an extensive ratio.** Let \(Z_\beta\) be the partition function, and let \(Z_\beta^{\mathrm{bad}}\) be the constrained partition function imposing the bad event on a full chessboard reflection-tiling of \(A_{p,\delta}\) (in particular, one may upper bound by imposing \(A_{q,\delta}\) for all plaquettes \(q\)). The chessboard estimate gives
   \[
   \mu_\beta(A_{p,\delta})\;\le\;\Big(\frac{Z_\beta^{\mathrm{bad}}}{Z_\beta}\Big)^{1/|P|}.
   \]

3. **Upper bound the constrained partition function.** Using only \(S_\beta\ge \beta |P|c_\Phi(\delta)\) on the constraint set,
   \[
   Z_\beta^{\mathrm{bad}}
   \;\le\;
   e^{-\beta |P|c_\Phi(\delta)}\,\mathrm{Vol}_g(\mathscr A).
   \]

4. **Lower bound the true partition function on a small product ball.** Let \(B_r\subset G\) be a geodesic ball of radius \(r\) around \(I\) with \(r<\mathrm{inj}(G)\). Define the product neighborhood
   \(
   \mathcal B_r := \{U: \forall e\in E,\ U_e\in B_r\} \subset \mathscr A.
   \)
   For \(r\) small, each plaquette holonomy satisfies \(d_G(U_p,I)\lesssim r\), hence by the small-angle expansion we have \(\Phi(U_p)\lesssim r^2\). Therefore
   \[
   S_\beta(U)\le \beta |P|C_\Phi r^2\qquad(U\in\mathcal B_r)
   \]
   for some constant \(C_\Phi\). Also \(\mathrm{Vol}_g(B_r)\sim v_G r^{\dim G}\) for small \(r\), hence
   \[
   \mathrm{Vol}_g(\mathcal B_r)\ge (v_G r^{\dim G})^{|E|}.
   \]
   Consequently
   \[
   Z_\beta\ge \int_{\mathcal B_r} e^{-S_\beta}\,d\mathrm{vol}_g
   \ge e^{-\beta|P|C_\Phi r^2}\,(v_G r^{\dim G})^{|E|}.
   \]

5. **Take the \(1/|P|\) root (this is the “globalization” trick).** Combining the bounds and taking \(1/|P|\) powers gives
   \[
   \mu_\beta(A_{p,\delta})
   \le
   \exp\big(-\beta c_\Phi(\delta)+\beta C_\Phi r^2\big)
   \cdot
   \Big(\frac{\mathrm{Vol}_g(\mathscr A)}{(v_G r^{\dim G})^{|E|}}\Big)^{1/|P|}.
   \]
   Since \(|E|/|P|\) is a *dimension-dependent constant* (e.g. \(|E|/|P|=2/3\) on a 4D periodic hypercubic lattice), the final factor is
   \(
   \lesssim r^{-\alpha}
   \)
   with \(\alpha:= (\dim G)\,|E|/|P|\).

6. **Optimize \(r\).** Choose \(r=\beta^{-1/2}\) (or any \(r\asymp \beta^{-1/2}\)), yielding
   \[
   \mu_\beta(A_{p,\delta})
   \le
   C_0\,\beta^{\alpha/2}\,e^{-\beta c_\Phi(\delta)}
   \]
   with \(C_0\) absorbing all \(\beta\)-independent constants.

This proves the lemma. \(\square\)

---

### Corollary 3.2 (Local tube has high probability)
For the local event \(\Omega_{\delta,R}\) defined above,
\[
\mu_\beta(\Omega_{\delta,R}^c)
\;\le\;
|P_R|\,C_0\,\beta^{\alpha}\,e^{-\beta c_\Phi(\delta)}.
\]
In particular, if \(\beta=\beta(a)\to\infty\) as \(a\to 0\) (e.g. asymptotic freedom scaling \(\beta(a)\sim c\log(1/a)\)), then for fixed physical \(R\) this error can be made \(o(1)\) by choosing \(\delta\) so that \(c_\Phi(\delta)\) dominates the growth of \(|P_R|\sim (R/a)^4\).

---

## 4. Immediate “interface” consequence: a defective inequality

The point of the lemma is not just concentration; it is that it gives a clean *interface inequality* usable by the PBH/Riccati/IR chain.

### Proposition 4.1 (Defective local Poincaré from high-probability convexity)
Let \(F\) be a bounded observable supported in \(B_R\). Assume that on \(\Omega_{\delta,R}\) the horizontal Bakry–Émery curvature admits a floor \(\rho_{\mathrm{loc}}>0\) (coming from Haar + Wilson convexity).

Then
\[
\mathrm{Var}_{\mu_\beta}(F)
\;\le\;
\frac{1}{\rho_{\mathrm{loc}}}\int |\nabla F|^2\,d\mu_\beta
\;+
4\|F\|_{\infty}^2\,\mu_\beta(\Omega_{\delta,R}^c).
\]

*Interpretation:* “high-probability curvature \(\Rightarrow\) defective inequality.” The defect is exactly the tube failure probability.

---

## 5. Why this bridges into PBH/Riccati/IR

Your IR machinery is already formulated as:

- **Local/topological splitting** with polylog mixing control (PROOF_08, Lemma 1). 
- **Projected PBH flow** for the local Hessian block with a controlled error \(\varepsilon(a,R)\) (PROOF_08, Lemma 2).
- **Local Riccati inequality** locking a positive eigenvalue floor provided the initial floor \(c_0\) dominates the mixing error (PROOF_08, Lemma 3).

Lemma 3.1–Corollary 3.2 supplies the missing input:

> With probability \(1-\mu_\beta(\Omega_{\delta,R}^c)\), the configuration lies in the small-angle sector where the initial local floor \(H^{\mathrm{loc}}(0)\ge c_0 I\) is valid.

Then the PBH/Riccati comparison produces a deterministic-in-time lower bound on the evolved local block, while Proposition 4.1 shows you only pay a defect proportional to \(\mu_\beta(\Omega_{\delta,R}^c)\). Your “topology decoupling” is precisely what’s designed to kill that defect for local observables.

---

## 6. What remains after this lemma

This lemma isolates the remaining hard work into two checkable, *surgical* tasks:

1. **Formalize the chessboard estimate in the exact gauge setting used here** (it is standard under RP; but the precise statement and reflection/tiling setup must be written carefully for plaquette events).
2. **Choose \(\delta\) and the scaling \(\beta(a)\)** so the tube failure probability dominates the combinatorics \(|P_R|\sim a^{-4}\) as \(a\to0\).

Everything after that is the PBH/Riccati + IR locking mechanism already written elsewhere.

---

## Citations to internal pillars (for cross-linking)

- Wilson Hessian positivity in the small-angle sector, and the Bakry–Émery setup: PROOF_04 and supporting lemmas (see also UNIF_CONJB_STRATEGY, Lemmas 3.2–3.4).
- RP input: 04_MASS_GAP_THEOREM / PROOF_12 (RP attributed to Seiler–Simon).
- PBH/Riccati + IR splitting and error estimates: PROOF_07 and PROOF_08.
