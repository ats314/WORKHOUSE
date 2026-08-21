# Localization Removal and Local-to-Global Functional Inequalities

## 0. What is extracted here

The project repeatedly uses a two-step idea:

1. Prove strong estimates (curvature bounds, covariance bounds) **on a canonical small-field set** \(K_\Lambda\).
2. Remove the restriction \(U\in K_\Lambda\) without losing the essential constants, by combining:
   - a **Lyapunov drift** that makes \(K_\Lambda^c\) rare, and
   - a **local-to-global** functional-inequality engine.

This document isolates that mechanism in a reusable, lattice-uniform form.

---

## 1. The canonical “good set” and why it’s measurable/local

Let \(\vartheta:G\to[0,\infty)\) be a smooth conjugation-invariant plaquette badness function, e.g.
\[
\vartheta(g)=\widetilde z(g)=1-\frac1N\Re\mathrm{Tr}(g).
\]

Define the averaged badness
\[
\mathcal B_\Lambda(U):=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)}\vartheta(U_p),
\]
and the canonical safe set
\[
K_\Lambda(\varepsilon):=\{U:\ \mathcal B_\Lambda(U)\le \varepsilon\}.
\]

This is a lattice-local object (depends only on plaquettes) and is stable under volume growth.

---

## 2. The localization identity for covariance (exact)

For any measurable \(K\subset M_\Lambda\) with \(0<\mu_\Lambda(K)<1\), let \(\mu_{\Lambda,K}\) and \(\mu_{\Lambda,K^c}\) be conditional measures.

For bounded \(F,G\),
\[
\boxed{
\mathrm{Cov}_{\mu_\Lambda}(F,G)
=
\mu_\Lambda(K)\,\mathrm{Cov}_{\mu_{\Lambda,K}}(F,G)
+
\mu_\Lambda(K^c)\,\mathrm{Cov}_{\mu_{\Lambda,K^c}}(F,G)
+
\mu_\Lambda(K)\mu_\Lambda(K^c)\,\Delta_KF\,\Delta_KG,
}
\]
where \(\Delta_KF:=\mu_{\Lambda,K}(F)-\mu_{\Lambda,K^c}(F)\).

This is pure algebra (a variance decomposition across an event).

### Consequence

If you can prove a strong covariance decay bound on \(K\), then to upgrade it globally you need:

- a bound on \(\mu_\Lambda(K^c)\), and
- a bound on the nuisance terms \(\mathrm{Cov}_{\mu_{\Lambda,K^c}}(\cdot,\cdot)\) and \(\Delta_K(\cdot)\), typically by trivial uniform bounds plus small \(\mu_\Lambda(K^c)\).

So the whole problem reduces to making \(K^c\) rare.

---

## 3. Lyapunov drift makes \(K^c\) rare (the key probabilistic input, but finite-dimensional)

Let \(W\ge 1\) be a \(C^2\) function on \(M_\Lambda\) such that
\[
\boxed{
L_\Lambda W \le -\lambda W + b\,\mathbf 1_K
}
\]
for some \(\lambda>0\), \(b<\infty\).

Standard Markov-process reasoning (and in this compact finite-dimensional setting: basic integration by parts) yields:

- \(\int W\,d\mu_\Lambda <\infty\) with a bound depending on \(b/\lambda\),
- tail bounds: if \(K\) is a sublevel set of \(W\) (or \(V=\log W\)), then \(\mu_\Lambda(K^c)\) decays in the tail level.

In the project, \(W=e^{\eta V}\) with \(V\) a plaquette-local penalty; the drift inequality is engineered so that \(K\) is a low-badness region.

---

## 4. Local-to-global Poincaré/LSI from (local inequality on \(K\)) + (Lyapunov drift)

The abstract engine in the notes proves statements of the following flavor.

### Theorem template (local Poincaré + Lyapunov ⇒ global Poincaré)

Assume:

1. (**Local Poincaré on \(K\)**)  
   There is \(C_{\mathrm{loc}}\) such that for all smooth \(f\),
   \[
   \mathrm{Var}_{\mu_{\Lambda,K}}(f)\le C_{\mathrm{loc}}\int_K \Gamma_\Lambda(f)\,d\mu_{\Lambda,K}.
   \]

2. (**Lyapunov drift**)  
   \(L_\Lambda W \le -\lambda W + b\,\mathbf 1_K\).

Then \(\mu_\Lambda\) satisfies a global Poincaré inequality
\[
\mathrm{Var}_{\mu_\Lambda}(f)\le C_P \int \Gamma_\Lambda(f)\,d\mu_\Lambda,
\]
with \(C_P\) depending explicitly on \((C_{\mathrm{loc}},\lambda,b)\) (and not on \(|\Lambda|\) if those inputs are uniform).

Similar templates exist for global log-Sobolev (often via a super-Poincaré profile if \(W\) is superlinear).

### Why curvature enters

The *input* local inequality on \(K\) is typically obtained from a local Bakry–Émery curvature lower bound on \(K\), which is exactly what the core curvature theorem provides near the vacuum.

So the three components lock together:

- curvature gives local inequalities on \(K\),
- Lyapunov drift gives return to \(K\),
- localization removal upgrades local to global.

---

## 5. How this interacts with Green’s function decay

Combine:

- a Helffer–Sjőstrand covariance bound on \(K\):
  \[
  \mathrm{Cov}_{\mu_{\Lambda,K}}(F,G)
  \le
  \int\langle \Pi_H\nabla F,M^{-1}\Pi_H\nabla G\rangle\,d\mu_{\Lambda,K},
  \]
- an explicit off-diagonal bound on \(M^{-1}\) (exponential decay),
- and localization removal with \(\mu_\Lambda(K^c)\) small.

You get a full-measure covariance decay estimate with the *same* exponential rate in separation as the \(M^{-1}\) bound, and only a small additive localization error.

This is exactly how the notes preserve the massive exponential clustering even after removing the restriction \(U\in K\).

---

## 6. What remains

This engine is structurally complete. What remains is *supplying the inputs* with uniform constants:

- a local curvature bound on a canonical \(K_\Lambda\) (done near the vacuum, and optional global mechanisms exist for heat-kernel actions),
- a Lyapunov drift inequality with volume-uniform constants (reduced to a local coercivity inequality),
- and the OS bridge if the end goal is a Hamiltonian mass gap.
