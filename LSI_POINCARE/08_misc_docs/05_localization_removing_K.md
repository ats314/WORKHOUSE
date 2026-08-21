# Localization: removing the \(K_\Lambda\)-restriction without spoiling the exponential rate

The matrix hinge + Helffer–Sjöstrand machinery typically yields a **conditional** covariance bound:
\[
|\mathrm{Cov}_{\mu_\Lambda}(F,G\mid K_\Lambda)|
\ \le\ C\,e^{-m\,\mathrm{dist}(\mathrm{supp}F,\mathrm{supp}G)}.
\]
This note records the clean bookkeeping identity that upgrades the bound to the full Gibbs measure, with an explicit localization error proportional to \(\mu_\Lambda(K_\Lambda^c)\).

---

## 1. Covariance decomposition across an event

Let \((\Omega,\mathcal F,\mu)\) be a probability space and let \(K\in\mathcal F\) with \(0<\mu(K)<1\). Define conditional measures
\[
\mu_K(\cdot):=\mu(\cdot\mid K),\qquad \mu_{K^c}(\cdot):=\mu(\cdot\mid K^c).
\]

### Lemma 1.1 (Covariance decomposition)
For bounded measurable \(F,G\),
\[
\boxed{
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,\Delta_KF\,\Delta_KG,
}
\tag{1.1}
\]
where
\[
\Delta_KF := \mu_K(F)-\mu_{K^c}(F),
\qquad
\Delta_KG := \mu_K(G)-\mu_{K^c}(G).
\]

**Proof.**
Write \(\alpha:=\mu(K)\) and use the mixture decomposition
\[
\mu(\cdot)=\alpha\,\mu_K(\cdot)+(1-\alpha)\,\mu_{K^c}(\cdot).
\]
Compute \(\mu(FG)\), \(\mu(F)\), \(\mu(G)\) under this decomposition and expand
\(\mu(FG)-\mu(F)\mu(G)\), grouping terms into the three pieces in (1.1). \(\square\)

---

## 2. A sharp sup-norm localization bound

### Corollary 2.1 (Localization error controlled by \(\mu(K^c)\))
For bounded \(F,G\),
\[
\boxed{
|\mathrm{Cov}_\mu(F,G)|
\ \le\
|\mathrm{Cov}_{\mu_K}(F,G)|
+
8\,\|F\|_\infty\,\|G\|_\infty\,\mu(K^c).
}
\tag{2.1}
\]

**Proof.**
From Lemma 1.1, use \(\mu(K)\le 1\) and the elementary bounds
\[
|\mathrm{Cov}_\nu(F,G)|\le 4\|F\|_\infty\|G\|_\infty\quad(\text{any probability }\nu),
\qquad
|\Delta_KF|\le 2\|F\|_\infty,\quad |\Delta_KG|\le 2\|G\|_\infty.
\]
Then
\[
\big|\mu(K^c)\mathrm{Cov}_{\mu_{K^c}}(F,G)\big|\le 4\|F\|_\infty\|G\|_\infty\,\mu(K^c),
\]
\[
\big|\mu(K)\mu(K^c)\Delta_KF\,\Delta_KG\big|\le 4\|F\|_\infty\|G\|_\infty\,\mu(K^c),
\]
and combine. \(\square\)

---

## 3. How this interacts with exponential clustering

Suppose you have a conditional exponential decay bound on \(K\):
\[
|\mathrm{Cov}_{\mu_K}(F,G)|
\ \le\
C\,e^{-m\,\mathrm{dist}(A,B)}\,\mathsf N(F)\,\mathsf N(G),
\tag{3.1}
\]
where \(A,B\) are link supports of \(F,G\) and \(\mathsf N(\cdot)\) is some gradient-type norm (or just \(\|\cdot\|_\infty\)).

Then Corollary 2.1 gives the full-measure bound
\[
|\mathrm{Cov}_{\mu}(F,G)|
\ \le\
C\,e^{-m\,\mathrm{dist}(A,B)}\,\mathsf N(F)\,\mathsf N(G)
\;+\;
8\,\|F\|_\infty\|G\|_\infty\,\mu(K^c).
\tag{3.2}
\]

### Practical reading of (3.2)

- If you are taking the **thermodynamic limit** \(|\Lambda|\to\infty\) with fixed local \(F,G\), it suffices that \(\mu_\Lambda(K_\Lambda^c)\to 0\) to recover the same exponential decay in the limit.

- If you want a **finite-volume** exponential bound uniform in distance, the additive term is unavoidable. What you can assert is:

  \[
  |\mathrm{Cov}_{\mu}(F,G)|
  \ \lesssim\
  e^{-m\,\mathrm{dist}(A,B)}
  \quad \text{for distances } \mathrm{dist}(A,B)\ \ll\ \frac{1}{m}\log\frac{1}{\mu(K^c)}.
  \]
  I.e. the exponential rate survives up to the “localization length” set by how rare \(K^c\) is.

---

## 4. What remains: bounding \(\mu_\Lambda(K_\Lambda^c)\)

To make (3.2) powerful, you need a mechanism that makes \(K_\Lambda^c\) rare under \(\mu_\Lambda\). The project files propose two broad routes:

1. **LSI concentration:** global log-Sobolev inequality \(\Rightarrow\) Gaussian concentration for averaged plaquette badness \(\Rightarrow \mu(K_\Lambda^c)\le e^{-c|\Lambda|}\).  
   (This route is clean but must avoid circularity, since global LSI is itself a target.)

2. **Large-\(\beta\) / large deviations:** use the explicit form of the Wilson weight and independence structure at \(\beta=\infty\) as a reference, then show that plaquette badness is exponentially suppressed for large \(\beta\).  
   (Harder technically, but avoids circularity.)

The localization lemma itself is agnostic: once any route gives a usable \(\mu(K_\Lambda^c)\) bound, the conditional exponential rate from the matrix hinge survives.

---
