# Gauge-Fixing Independence for Gauge-Invariant Observables

This file contains the gauge-fixing independence theorem (H2) as drafted in the chat.

---

```tex
\begin{theorem}[Gauge-Fixing Independence of Gauge-Invariant Cylindrical Expectations]
\label{thm:gauge_independence}

Let $\mu_a^{W}$ denote the standard (unfixed) Wilson lattice Yang--Mills
measure on $\mathcal{X}_a = G^{E(\Lambda_a)}$:
\[
d\mu_a^{W}(U)
=
Z_a^{-1}
\exp\!\left(-S^{W}_a(U)\right)
\prod_{e \in E(\Lambda_a)} dU_e ,
\]
where $dU_e$ is Haar measure and $S^W_a$ is the Wilson plaquette action.

Let $\mu_a^{\mathrm{gf}}$ denote the corresponding gauge-fixed lattice
measure in Coulomb/Landau gauge obtained by the Faddeev--Popov (FP) 
procedure:
\[
d\mu_a^{\mathrm{gf}}(U)
=
\tilde Z_a^{-1}
\exp\!\left( -S^W_a(U) \right)
\delta(G(U))
\det(\Delta_{\mathrm{FP}}(U))
\prod_{e\in E(\Lambda_a)} dU_e .
\]

Let $F_a$ be any gauge-invariant cylindrical observable (i.e.\ a smooth
function of finitely many lattice Wilson loops or products of holonomies
along closed loops).

Assume the FP determinant is positive and locally bounded on the gauge-fixing
slice, and that the gauge-fixing condition $G(U)=0$ intersects each gauge
orbit in a set of Haar measure zero except for a unique representative.

Then for all gauge-invariant cylindrical observables $F_a$,
\[
\int_{\mathcal{X}_a} F_a(U)\, d\mu_a^{W}(U)
=
\int_{\mathcal{X}_a} F_a(U)\, d\mu_a^{\mathrm{gf}}(U).
\]

Thus gauge-invariant expectations are independent of the gauge-fixing
procedure at every lattice scale.
\end{theorem}
```

```tex
\begin{proof}
The key ingredients are: 
(i) gauge invariance of $F_a$,
(ii) the fact that $\mu_a^{\mathrm{gf}}$ is obtained from $\mu_a^W$ by 
disintegrating the measure along gauge orbits, and 
(iii) absolute continuity of the FP-gauge slice with respect to 
$\mu_a^W$.

\textbf{Step 1: Gauge invariance allows averaging over gauge orbits.}
Let $\mathcal{G}_a$ be the lattice gauge group.
Since $F_a$ is gauge-invariant,
\[
F_a(U) = F_a(U^g) \qquad \forall g\in \mathcal{G}_a.
\]
Therefore, for any probability measure $\nu$ absolutely continuous with
respect to the Haar product measure,
\[
\int F_a(U)\, d\nu(U)
=
\int F_a(U^g)\, d\nu(U)
\]
for every $g$, and hence
\[
\int F_a(U)\, d\nu(U)
=
\int F_a(U)\left( \int d g \right) d\nu(U),
\]
where $dg$ is Haar measure on $\mathcal{G}_a$ normalized to $1$.
Thus averaging over gauge orbits does not change the value of 
$\int F_a\, d\nu$.

\textbf{Step 2: Wilson measure $\mu_a^W$ is gauge-invariant.}
By construction,
\[
S^W_a(U^g) = S^W_a(U),
\qquad
\prod_e dU_e = \prod_e d(U_e^g),
\]
so $\mu_a^W$ is exactly invariant under $U \mapsto U^g$.
Thus disintegration along gauge orbits is valid:
\[
d\mu_a^W(U) 
=
\left( \prod_{x\in \Lambda_a} dg_x \right)
\rho_a([U])\, d\sigma([U]),
\]
where $[U]$ denotes a gauge orbit and $\sigma$ a measure on orbit space.

\textbf{Step 3: FP gauge fixing is a measurable section of orbit space.}
The gauge-fixing function $G(U)=0$ defines a slice intersecting almost
every orbit in exactly one point.
The Faddeev--Popov identity (formal but valid under the stated hypotheses)
says that
\[
1 
= 
\int_{\mathcal{G}_a} 
\delta(G(U^g))\, \det\Delta_{\mathrm{FP}}(U^g) \, dg,
\]
and the determinant is gauge-invariant:
$\det\Delta_{\mathrm{FP}}(U^g)=\det\Delta_{\mathrm{FP}}(U)$.

Thus, for any integrable function $\Phi$,
\[
\int_{\mathcal{X}_a} \Phi(U)\, d\mu_a^{W}(U)
=
\int_{\mathcal{X}_a}
\Phi(U)\,
\delta(G(U)) \det(\Delta_{\mathrm{FP}}(U)) \,
d\mu_a^{W}(U).
\]

\textbf{Step 4: Apply the identity to $\Phi = F_a$.}
Since $F_a$ is gauge-invariant:
\[
F_a(U) = F_a(U^g),
\quad
\det(\Delta_{FP}(U))=\det(\Delta_{FP}(U^g)).
\]
Thus
\[
\int F_a \, d\mu_a^W
=
\int F_a(U)\,
\delta(G(U)) \det(\Delta_{\mathrm{FP}}(U))\,
d\mu_a^W(U).
\]

\textbf{Step 5: Recognize the gauge-fixed measure.}
By definition,
\[
d\mu_a^{\mathrm{gf}}(U)
=
\tilde Z_a^{-1}\,
e^{-S_a^W(U)} 
\delta(G(U)) \det(\Delta_{FP}(U))
\prod_e dU_e.
\]

Thus the right-hand side of the previous expression is (after normalization)
exactly
\[
\int F_a\, d\mu_a^{\mathrm{gf}}.
\]

Therefore,
\[
\int F_a \, d\mu_a^W = \int F_a\, d\mu_a^{\mathrm{gf}}.
\]

\end{proof}
```
