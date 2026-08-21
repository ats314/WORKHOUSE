# Project Highlight E: OS bridge and the one-step OS/Dirichlet comparison bottleneck

This document extracts and unifies the material in the “clean forward engine” parts (`Part 20` and `Part 21`):

1. Treat **OS reconstruction / transfer matrix** as an external theorem.
2. Give a self-contained spectral-measure argument:  
   **Euclidean-time exponential decay \(\Rightarrow\) Hamiltonian spectral gap \(m\gtrsim \eta/a\).**
3. State the **one-step OS/Dirichlet comparison** as the sharp “single hinge inequality” that can bypass multi-time correlation bounds.

---

## E.1. Reflection positivity and OS reconstruction (external theorem)

Fix the Euclidean time direction \(e_0\).  
Let \(\Omega=G^{E(\mathbb Z^d)}\) be the infinite-volume configuration space and \(\mu\) a translation-invariant Euclidean measure (thermodynamic limit of the finite-volume Gibbs measures).

Let \(\Theta\) be the time-reflection map (reflection across a plane between two time-slices, with the standard link-orientation convention) and define the antilinear involution on observables
\[
(\theta F)(U):=\overline{F(\Theta U)}.
\]
Let \(\mathcal A_+\) denote the algebra of bounded cylinder observables supported in the nonnegative-time half-space.

Assume:

* **(RP)** Reflection positivity: \(\mu((\theta F)F)\ge 0\) for all \(F\in\mathcal A_+\).
* **(TI)** Time-translation invariance: \(\mu(F)=\mu(F\circ\tau_n)\) for all \(n\in\mathbb Z\), where \(\tau_n\) shifts time by \(n\) lattice units.

### External input (OS reconstruction / transfer matrix)
Under (RP)+(TI) and mild regularity assumptions, there exists an OS Hilbert space \(\mathcal H_{\mathrm{OS}}\), vacuum \(\Omega\), and a positive contraction \(T\) (“transfer matrix”) such that:

* The OS inner product on \(\mathcal A_+\) is
  \[
  \langle F,G\rangle_{\mathrm{OS}} := \mu((\theta F)G),
  \]
  modulo null vectors and completion.
* The time translation by one step is implemented by a bounded self-adjoint contraction \(T\) on \(\mathcal H_{\mathrm{OS}}\).
* There is a self-adjoint Hamiltonian \(H\ge 0\) with
  \[
  T=e^{-aH},
  \]
  such that for \(n\ge 0\),
  \[
  \langle [F],\,T^n [G]\rangle_{\mathrm{OS}}
  =
  \mu\big((\theta F)\,\tau_n G\big).
  \]

This is standard OS/transfer-matrix technology; the project uses it as an external theorem, not a re-derivation.

---

## E.2. Spectral-measure lemma: exponential decay forces a gap

The functional-analytic core is the following elementary lemma.

**Lemma E.1 (Gap criterion).**  
Let \(H\ge 0\) be self-adjoint on a Hilbert space and \(\psi\in\mathcal H\). Let \(\nu_\psi\) be the spectral measure of \(H\) associated to \(\psi\), i.e.
\[
\langle \psi,e^{-tH}\psi\rangle = \int_{[0,\infty)} e^{-t\lambda}\,d\nu_\psi(\lambda),\qquad t\ge 0.
\]
If there exist constants \(C<\infty\) and \(m>0\) such that
\[
\langle \psi,e^{-tH}\psi\rangle \le C\,e^{-mt}\qquad\forall t\ge 0,
\]
then \(\nu_\psi([0,m))=0\). In particular, if \(\psi\perp\ker(H)\), then \(\inf\mathrm{supp}(\nu_\psi)\ge m\).

*Proof.* If \(\nu_\psi([0,m))>0\), then for some \(\varepsilon\in(0,m)\) we have \(\nu_\psi([0,m-\varepsilon])=\delta>0\), yielding
\[
\langle \psi,e^{-tH}\psi\rangle \ge \delta\,e^{-(m-\varepsilon)t},
\]
contradicting the assumed \(Ce^{-mt}\) decay as \(t\to\infty\). \(\square\)

---

## E.3. From Euclidean-time decay to an OS Hamiltonian gap

Assume that from the analytic engine (Helffer–Sjöstrand + Green’s function) you have proved:

**(Time-decay input).** There exists \(\eta>0\) such that for every \(F\in\mathcal A_+\),
\[
\big|\mathrm{Cov}_\mu(\theta F,\tau_n F)\big|
\ \le\
C_F\,e^{-\eta n}
\qquad\forall n\ge 0.
\]

Let \(F^\circ := F-\mu(F)\) be centered. Then \([F^\circ]\perp \Omega\) in \(\mathcal H_{\mathrm{OS}}\) and
\[
\langle [F^\circ],T^n[F^\circ]\rangle_{\mathrm{OS}}
=
\mu\big((\theta F^\circ)\,\tau_n F^\circ\big)
=
\mathrm{Cov}_\mu(\theta F,\tau_n F).
\]
Thus
\[
\langle [F^\circ],e^{-naH}[F^\circ]\rangle_{\mathrm{OS}}
\le
C_F\,e^{-(\eta/a)\,(na)}.
\]
Lemma E.1 then implies that the spectral measure of \(H\) under \([F^\circ]\) has no support below \(\eta/a\). Since such vectors are dense in \(\mathcal H_{\mathrm{OS}}\ominus \mathbb C\Omega\), one concludes:

**Theorem E.2 (Euclidean-time decay \(\Rightarrow\) OS mass gap).**
\[
\boxed{\mathrm{gap}(H)\ \ge\ \frac{\eta}{a}.}
\]

This is the cleanest “cash-out”: prove \(\eta>0\) on the Euclidean side and divide by \(a\).

---

## E.4. The “one-step” alternative: compare dissipations per time step

Parts 20–21 emphasize an alternative bridge that can avoid multi-time bounds:

> Compare the **one-step OS dissipation** \(\langle F,(I-T_a)F\rangle_{\mathrm{OS}}\) to a **one-step Dirichlet dissipation** for a Markov operator on a time slice.

### E.4.1. Compression to a time-slice operator

Fix a Euclidean time step \(a\) and let \(T_a\) be the OS transfer operator for that step.

The strip-integrated (“compressed”) object on slice data is a Markov kernel \(K_a\) acting on boundary configurations \(\sigma\) at time \(0\) (the precise construction uses the lattice Markov property / integration over the interior of a time-strip).  

A key structural identity established in `Part 21` is:

*There is a “compression” map \(J\) (conditional expectation onto slice data) such that the OS quadratic form of \((I-T_a)\) is exactly the Dirichlet form of \(K_a\) on the slice.*

Schematically (precise statement depends on the chosen positive-time algebra),
\[
\boxed{
\langle [F],(I-T_a)[F]\rangle_{\mathrm{OS}}
=
\mathcal E_{K_a}(JF,JF)
:=
\langle JF,(I-K_a)JF\rangle_{L^2(\nu)}.
}
\]

### E.4.2. Why the original target inequality needed a fix

Earlier formulations tried to compare \(\langle F,(I-T_a)F\rangle\) to a raw “continuum” Dirichlet form \(\int|\nabla F|^2\).  
`Part 21` explains why the correct viable comparison is instead against the **scale-\(a\)** Dirichlet form of the configuration diffusion semigroup:
\[
\mathcal E^{(a)}_{\mathrm{conf}}(f,f) := \langle f,(I-P_a)f\rangle_{L^2(\nu)},
\]
where \(P_a=e^{aL}\) is the diffusion step.

This change is conceptually small (both are dissipations), but mathematically decisive.

### E.4.3. The one-step comparison theorem (Part 21 target)

The central bottleneck statement is then:

**Theorem E.3 (One-step OS/Dirichlet comparison; target form).**  
There exists a constant \(c>0\) (independent of volume) such that for all \(F\in\mathcal A_+\),
\[
\boxed{
\langle [F],(I-T_a)[F]\rangle_{\mathrm{OS}}
\ \ge\
c\,\langle JF,(I-P_a)JF\rangle_{L^2(\nu)}.
}
\]
Equivalently,
\[
\mathcal E_{K_a}(JF,JF)\ \ge\ c\,\mathcal E^{(a)}_{\mathrm{conf}}(JF,JF).
\]

Once this holds, a diffusion gap \(\mathrm{gap}(-L)\ge \lambda_*>0\) implies
\[
\mathcal E^{(a)}_{\mathrm{conf}}(f,f)\ge (1-e^{-a\lambda_*})\|f-\nu(f)\|_2^2,
\]
yielding a spectral gap for \(K_a\), and hence an OS mass gap via the standard “divide by \(a\)” lemma:
\[
m(a) \simeq \frac{1}{a}\big(-\log\|K_a\|_{\perp}\big).
\]

---

## E.5. Why this is exciting (and where it can fail)

*Exciting feature.* Theorem E.3 would reduce “mass gap” to a **single** comparison inequality between two one-step dissipations, which is exactly the right scale to exploit locality, overlap bounds, and single-link functional inequalities.

*Fragility.* Theorem E.3 can fail if the strip compression \(K_a\) creates long-range dependencies on the slice that are not dominated by the diffusion step \(P_a\), or if boundary terms introduce uncontrolled modes. The project’s insistence on correct scaling (\(I-P_a\) rather than \(\int|\nabla|^2\)) is precisely to remove a *genuine impossibility* and replace it with a sharp but plausible target.

---

## E.6. Practical project decision point

You effectively have two exits to an OS mass gap:

1. **Correlation-decay exit:**  
   Prove uniform exponential clustering on the Euclidean side (Highlights B–D), then use Theorem E.2.
2. **One-step exit:**  
   Prove the one-step comparison Theorem E.3, then use the diffusion gap and semigroup calculus.

Route (1) is usually more robust; route (2) is sharper if it goes through.

