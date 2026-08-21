---
title: "Extract 04 — Localization + Typicality: From Conditional Clustering to Unconditioned Clustering"
project: "APPENDIX PROOF OUTLINE"
---

## 1. The structural problem

The hinge + HS machinery yields exponential clustering **conditioned** on a good domain \(\Omega\) (typically \(\Omega=\mathcal K_{\Lambda_L,\beta}\)).

But to obtain an Osterwalder–Schrader (OS) mass gap in infinite volume, one needs **unconditioned** exponential clustering for the original Gibbs measure \(\mu_{\Lambda_L,\beta}\), uniformly in volume.

This is where the project introduces a flexible **localization algebra** (Appendix I) and a **typicality mechanism** (Appendix J).

---

## 2. Localization algebra: covariance decomposition by conditioning on an event \(K\)

Let \(K\subset\mathcal M_{\Lambda_L}\) be any measurable event and let
\[
\mu^K := \mu(\,\cdot\,\mid K),\qquad \mu^{K^c}:=\mu(\,\cdot\,\mid K^c).
\]
Then one has the exact decomposition
\[
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu^K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu^{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,\Delta_K F\,\Delta_K G,
\]
where \(\Delta_K F := \mu^K(F)-\mu^{K^c}(F)\).

For bounded observables this yields a clean inequality (as used in Core 8):
\[
\boxed{
|\mathrm{Cov}_\mu(F,G)|
\ \le\
\mu(K)\,|\mathrm{Cov}_{\mu^K}(F,G)|
\ +\
8\|F\|_\infty\|G\|_\infty\,\mu(K^c).
}
\]

Interpretation: if we can control the conditioned covariance on \(K\) and show \(\mu(K^c)\) is very small, then unconditional covariance is controlled.

---

## 3. Converting volume-scale rarity into distance-scale decay

The error term \(8\|F\|_\infty\|G\|_\infty\,\mu(K^c)\) does not see the distance between the supports of \(F\) and \(G\) unless \(\mu(K^c)\) is made to depend on volume in a way that *necessarily grows with separation*.

On a periodic box, separation cannot exceed a constant multiple of the system size, hence a constant multiple of the number of plaquettes. Core 8 uses a deterministic inequality
\[
\mathrm{dist}_{\mathcal E}(b,b')\ \le\ m_\partial\,|\mathcal P(\Lambda_L)|,
\]
which allows one to turn a volume-exponential bound into a distance-exponential one:
\[
e^{-c|\mathcal P|}\ \le\ \exp\!\Bigl(-\frac{c}{m_\partial}\,\mathrm{dist}_{\mathcal E}\Bigr).
\]

So a typicality bound of the form
\[
\mu(K^c)\ \le\ e^{-c_{\mathrm{typ}}|\mathcal P|}
\]
is “strong enough” to not dominate the conditional exponential clustering term.

---

## 4. A concrete typicality mechanism (Appendix J)

Appendix J proposes a typicality event based on the **empirical plaquette potential**.

Define
\[
\overline{\vartheta}_{\Lambda_L}(U)
:=\frac1{|\mathcal P(\Lambda_L)|}\sum_{p\in\mathcal P(\Lambda_L)}\vartheta(U_p(U)),
\]
where \(\vartheta:G\to[0,2]\) is the Wilson plaquette potential.

For \(\varepsilon\in(0,2)\) define the good set
\[
K_{\Lambda_L}(\varepsilon):=\Bigl\{U:\ \overline{\vartheta}_{\Lambda_L}(U)\le\varepsilon\Bigr\}.
\]

### 4.1 Typicality estimate

Appendix J proves that if parameters \(r>0\) and \(\varepsilon\in(0,2)\) are chosen so that
\[
c_{\mathrm{typ}}
:=
\beta\bigl(\varepsilon-L_\vartheta m_\partial r\bigr)
-
c_{E:P}\,\chi_G(r)
\ >\ 0,
\]
then for sufficiently large \(L\),
\[
\boxed{
\mu_{\Lambda_L,\beta}\bigl(K_{\Lambda_L}(\varepsilon)^c\bigr)
\ \le\
\exp\!\bigl(-c_{\mathrm{typ}}\,|\mathcal P(\Lambda_L)|\bigr).
}
\]

Here:

- \(L_\vartheta\) is a Lipschitz constant for \(\vartheta\),
- \(m_\partial\) and \(c_{E:P}\) are lattice combinatorial constants,
- \(\chi_G(r):=\log\bigl(\mathrm{vol}(G)/\mathrm{vol}(B_r)\bigr)\) measures the “entropy cost” of forcing all links into a small ball of radius \(r\).

### 4.2 Proof idea (high-level)

1. On \(K^c\), the action satisfies \(S_{\Lambda_L,\beta}\ge \beta\varepsilon|\mathcal P|\), so the numerator of \(\mu(K^c)\) is bounded by \(e^{-\beta\varepsilon|\mathcal P|}\,\mathrm{vol}(\mathcal M_{\Lambda_L})\).

2. The partition function \(Z_{\Lambda_L,\beta}\) is bounded below by restricting integration to the linkwise ball event
   \[
   \mathcal A_{\Lambda_L}(r):=\{U:\ \text{every link lies in }B_r(1)\},
   \]
   on which the action is controlled using the plaquette-to-link Lipschitz constant and \(|\partial p|\le m_\partial\).

3. Since \(\mathrm{vol}(\mathcal A_{\Lambda_L}(r))=\mathrm{vol}(B_r)^{|\mathcal E|}\), the ratio gives an explicit exponential-in-\(|\mathcal P|\) upper bound for \(\mu(K^c)\).

---

## 5. Open alignment problem (and a fertile direction)

The *hinge* in Core 5 is proven on the **small-field** set \(\mathcal K_{\Lambda_L,\beta}\) (plaquette logs uniformly small), while Appendix J provides typicality for an **average-energy** set \(K_{\Lambda_L}(\varepsilon)\).

Bridging these two is a natural next step. Some directions:

- Replace the uniform small-field set by a *corridor-local* small-field event depending only on plaquettes in a buffer region separating supports of \(F,G\). Then typicality only needs to be proven for that corridor.

- Prove that on \(K_{\Lambda_L}(\varepsilon)\), the fraction of plaquettes with large log is exponentially small, and show the hinge can tolerate a sparse set of “defects” (multi-scale hinge).

- Seek a reflection-positivity/chessboard type estimate to control \(\mu(\mathcal K_{\Lambda_L,\beta}^c)\) directly.

This alignment is not a bookkeeping detail; it is arguably the deepest probabilistic bridge between “deterministic coercivity” and “global typicality”.

