---
title: "Phase 4 — The Two Root-Plane Conspiracy Event in SU(3): Staple Encoding, Eigenvalue Gaps, and Large-β Suppression"
date: "2025-12-31"
---

## Goal

We isolate the **only remaining non-abelian cancellation mechanism** after the one-link *root-escape* lemma:

> If a link-star cannot be approximately abelianized, at least one transported plaquette force acquires a root component of size \(\asymp \eta\).
> The only way the **link force** can still be small is if there exists a **second** plaquette force with a **comparable component in the same root plane**, arranged to cancel.
> This is the **two-root-plane conspiracy** event.

We encode that event in terms of **staple words** and **plaquette eigenvalue gaps**, and give a clean route to show it has **small Gibbs weight or small capacity** at large \(\beta\).

All statements here are written so that constants can be placed in the project’s constants ledger.

---

## 1. One-link force decomposition via staples

Work on \(M_\Lambda = SU(3)^{E(\Lambda)}\) with Wilson action
\[
S_\beta(U)=\beta\sum_{p\in P(\Lambda)} \widetilde z(U_p),
\qquad
\widetilde z(g)=1-\frac13 \Re \operatorname{Tr}(g).
\]

Fix a link \(\ell\) and let \(P(\ell)\) be the set of plaquettes incident to \(\ell\) (\(|P(\ell)|=6\) in \(d=4\)).

For each \(p\in P(\ell)\), write the plaquette holonomy in **staple form**
\[
U_p(U)=U_\ell^{\sigma_{\ell,p}}\,S_{\ell,p}(U),
\qquad
\sigma_{\ell,p}\in\{+1,-1\},
\]
where \(S_{\ell,p}\) is the product of the other three link matrices in \(\partial p\) (with inverses as dictated by orientation).
This \(S_{\ell,p}\) is the usual **staple word** at \(\ell\) for plaquette \(p\).

Define the single-plaquette force
\[
X(g):=\nabla_{SU(3)} \widetilde z(g)\in\mathfrak{su}(3).
\]
Because \(\widetilde z\) is a class function, \(X(g)\) commutes with \(g\) and thus lies in the Cartan of \(g\) when \(g\) is regular.

Then the link-gradient of \(F(U)=\sum_p \widetilde z(U_p)\) has the form
\[
\nabla_\ell F(U)=\sum_{p\ni \ell} F_{\ell,p}(U),
\qquad
F_{\ell,p}(U)= \sigma_{\ell,p}\,\mathrm{Ad}_{S_{\ell,p}(U)^{-1}}\,X(U_p(U)).
\]
So cancellation at link \(\ell\) is cancellation among the six vectors \(F_{\ell,p}\in\mathfrak{su}(3)\).

---

## 2. Root-plane projectors and eigenvalue-gap regularity

Fix the standard maximal torus \(T\) (diagonal matrices) with Cartan algebra \(\mathfrak t\).
Decompose
\[
\mathfrak{su}(3)=\mathfrak t \oplus \mathfrak g_{12}\oplus \mathfrak g_{23}\oplus \mathfrak g_{13},
\]
where \(\mathfrak g_{ij}\) is the **real root plane** spanned by the \((i,j)\) and \((j,i)\) Gell-Mann off-diagonals.
Let \(P_{ij}\) be the orthogonal projection onto \(\mathfrak g_{ij}\).

Define the **root-plane magnitudes**
\[
r_{\ell,p}^{ij}(U) := \|P_{ij} F_{\ell,p}(U)\|.
\]

To keep the root-escape constants nondegenerate we exclude plaquette holonomies near Weyl walls.
Write the eigenvalues of \(U_p\) as \(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3}\) with \(\theta_1+\theta_2+\theta_3\equiv0\pmod{2\pi}\).
Define the **eigenvalue gap**
\[
\operatorname{gap}(U_p):=\min_{i<j} |\theta_i-\theta_j|\quad(\text{mod }2\pi).
\]
We call \(U_p\) **regular-\(\gamma_0\)** if \(\operatorname{gap}(U_p)\ge \gamma_0\).

---

## 3. The two-root-plane conspiracy event (exact encoding)

Fix parameters:
- roughness level \(\varepsilon>0\),
- eigen-gap floor \(\gamma_0>0\),
- root-plane tolerance \(\eta>0\),
- cancellation tolerance \(\delta\in(0,1)\).

Define the event at a link \(\ell\):

\[
\mathsf{Consp}_\ell(\varepsilon,\gamma_0,\eta,\delta)
:=
\Big\{
\exists\ p\neq q\in P(\ell),\ \exists (i,j)\in\{(12),(23),(13)\}:
\mathsf{RoughReg}_{p,q} \ \wedge\ \mathsf{SamePlane}_{p,q}^{ij}\ \wedge\ \mathsf{Cancel}_{p,q}^{ij}
\Big\},
\]
where

- **Rough + regular**
\[
\mathsf{RoughReg}_{p,q}:=\{
\widetilde z(U_p)\ge\varepsilon,\ \widetilde z(U_q)\ge\varepsilon,\ 
\operatorname{gap}(U_p)\ge \gamma_0,\ \operatorname{gap}(U_q)\ge \gamma_0
\}.
\]

- **Same root plane** (implemented via a *relative staple word*):
Define the **relative staple word**
\[
R_{pq}(U):=S_{\ell,q}(U)\,S_{\ell,p}(U)^{-1}.
\]
Let \(K_{ij}\subset SU(3)\) be the embedded \(SU(2)\) acting on the \((i,j)\) subspace, and let \(N(K_{ij})\) be its normalizer.
Then
\[
\mathsf{SamePlane}_{p,q}^{ij}:=\{ d(R_{pq},N(K_{ij}))\le \eta\}.
\]
(Interpretation: \(R_{pq}\) approximately preserves the \((i,j)\) root plane under the adjoint action.)

- **Cancellation in that plane**
\[
\mathsf{Cancel}_{p,q}^{ij}:=
\left\{
\|P_{ij}(F_{\ell,p}+F_{\ell,q})\|\le \delta\,(r_{\ell,p}^{ij}+r_{\ell,q}^{ij})
\ \ \text{and}\ \ r_{\ell,p}^{ij},r_{\ell,q}^{ij}\ge c_0 \eta
\right\}.
\]
The lower bound \(r_{\ell,p}^{ij}\ge c_0\eta\) is the output of the root-escape lemma, restricted to the regular-\(\gamma_0\) regime.

Thus: conspiracy means **two rough, regular plaquettes** whose **relative staple** almost preserves a root \(SU(2)\), and whose root-plane components are arranged to cancel.

---

## 4. Why this is nongeneric: codimension

### 4.1 Dimension count

\(\dim SU(3)=8\).
The subgroup \(K_{ij}\cong SU(2)\) has dimension \(3\).
Its normalizer \(N(K_{ij})\) contains \(K_{ij}\times U(1)\) (the \(U(1)\) acting on the complementary 1D subspace), so \(\dim N(K_{ij})=4\) (up to discrete Weyl factors).

Hence \(N(K_{ij})\) has codimension \(4\) in \(SU(3)\).
Therefore the Riemannian tubular neighborhood bound gives, for small \(\eta\),
\[
\operatorname{Haar}\big(\{g: d(g,N(K_{ij}))\le \eta\}\big)
\le
C_{N}\,\eta^{4},
\]
with \(C_N\) determined by the tube formula:
\(C_N\approx \mathrm{vol}(N(K_{ij}))\cdot \mathrm{vol}(B_1^{4})\), \(\mathrm{vol}(B_1^4)=\pi^2/2\).

This is the **geometric** suppression factor.

---

## 5. Large-β suppression: two rough plaquettes cost action

In the Wilson density, each rough plaquette costs at least \(e^{-\beta\varepsilon}\).
Thus on \(\mathsf{RoughReg}_{p,q}\),
\[
e^{-S_\beta(U)} \le e^{-\beta(\widetilde z(U_p)+\widetilde z(U_q))}\le e^{-2\beta\varepsilon}.
\]

In a finite link neighborhood (the star around \(\ell\)), the local partition function grows at most polynomially in \(\beta\) in the weak-coupling regime whenever the boundary data are typical (near vacuum).
Therefore for large \(\beta\), the exponential penalty \(e^{-2\beta\varepsilon}\) dominates any polynomial prefactor.

Heuristic (but ledger-ready) bound:
\[
\mu_\beta\big(\mathsf{Consp}_\ell(\varepsilon,\gamma_0,\eta,\delta)\big)
\ \lesssim\
C_{\mathrm{pairs}}\;C_N\;\eta^4\;\mathrm{poly}(\beta)\;e^{-2\beta\varepsilon},
\]
where \(C_{\mathrm{pairs}}\le 3\binom{6}{2}=45\).

This is the **physics** suppression factor.

---

## 6. Capacity bound (often stronger than measure)

Let \(\mathcal E_\mu(f)=\int|\nabla f|^2\,d\mu\) be the Dirichlet form of the configuration diffusion.
Define a cutoff \(f\) that equals \(1\) on the conspiracy set and decays to \(0\) outside the \(\eta\)-tube of \(N(K_{ij})\), with transition thickness \(\asymp\eta\).
Then \(|\nabla f|\lesssim L_{\mathrm{stap}}/\eta\), where \(L_{\mathrm{stap}}\) is a Lipschitz constant for the map from local links to \(R_{pq}\) (bounded by the staple length, i.e. \(O(1)\)).

Hence
\[
\operatorname{Cap}_\mu(\mathsf{Consp}_\ell)
\ \le\
\mathcal E_\mu(f)
\ \lesssim\
\frac{L_{\mathrm{stap}}^2}{\eta^2}\ \mu_\beta(\text{the }\eta\text{-tube}),
\]
and the tube has measure \(\lesssim C_N\eta^4\mathrm{poly}(\beta)e^{-2\beta\varepsilon}\).
Therefore
\[
\boxed{
\operatorname{Cap}_\mu(\mathsf{Consp}_\ell)
\ \lesssim\
\tilde C\;\eta^{2}\;\mathrm{poly}(\beta)\;e^{-2\beta\varepsilon}.
}
\]
Capacity decays as \(\eta^{2}\) (codim \(4\Rightarrow \eta^{4-2}\)) times the action penalty.

This is the cleanest way to justify “drift/gluing can swallow it”: small capacity sets are effectively invisible to the diffusion at the scale of Poincaré/LSI patching.

---

## 7. How this plugs into strip coercivity

- Phase 2 gives: outside near-abelianization, at least one link gets a root component \(\gtrsim c_{\mathrm{geom}}(\eta)\).
- The only way the link gradient can still be small is if \(\mathsf{Consp}_\ell\) occurs.
- Phase 3 (incidence combinatorics) says: coercivity on a positive fraction of links yields \(\|\nabla F\|^2\gtrsim |E|\,c_{\mathrm{geom}}(\eta)^2\), unless many links satisfy \(\mathsf{Consp}_\ell\).
- Phase 4 says \(\mathsf{Consp}_\ell\) has exponentially small weight/capacity at large \(\beta\), so the exceptional links are rare.

---

## 8. Simulation diagnostic (what to compute)

For each configuration:

1) For each link \(\ell\), enumerate its incident plaquettes \(p\in P(\ell)\).
2) Compute staples \(S_{\ell,p}\), holonomies \(U_p\), and forces \(F_{\ell,p}=\sigma\,\mathrm{Ad}_{S_{\ell,p}^{-1}}X(U_p)\).
3) Project \(F_{\ell,p}\) onto the three root planes using the Gell-Mann basis (pairs \((12),(23),(13)\)).
4) For each pair \((p,q)\) and each root plane \((i,j)\), test:
   - roughness \(\widetilde z(U_p),\widetilde z(U_q)\ge\varepsilon\),
   - eigen gap \(\operatorname{gap}(U_p),\operatorname{gap}(U_q)\ge\gamma_0\),
   - relative staple closeness \(d(R_{pq},N(K_{ij}))\le \eta\),
   - cancellation of projected vectors in that plane.

Track frequency of the event vs \(\beta\) and compare to predicted scaling \(\sim \eta^4 e^{-2\beta\varepsilon}\) (up to polynomial corrections).

---
