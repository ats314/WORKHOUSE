---
file: Appendix_M__Continuum_Permanence_Interfaces.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
feeds_into:
  - Core-10 (Conditional continuum extension)
  - Appendix_N__External_Inputs_Ledger.md
---

# Appendix M — Continuum permanence interfaces

## M.0 Scope and outputs

**Definition M.0.1 (scope).**  
This appendix isolates two *structural permanence* mechanisms needed only for the **conditional continuum extension** layer:

1. **Reflection-positivity permanence** under reflection-equivariant coarse-graining pushforward and under projective limits at the level of cylinder observables.
2. **Gap permanence** under monotone (supremum) limits of nonnegative quadratic forms on a common Hilbert space.

These mechanisms are abstract and are stated without any model-specific hypotheses.

**Definition M.0.2 (outputs).**  
Downstream usage is:

- **Proposition M.1.3**: reflection positivity is preserved by a reflection-equivariant, positive-time compatible pushforward.
- **Proposition M.1.8**: reflection positivity holds on cylinder observables for a projective limit whenever it holds at every finite stage.
- **Proposition M.2.6**: a uniform “gap as a form inequality” persists under monotone supremum limits and closure.
- **Corollary M.2.9**: the associated limiting self-adjoint operator has a spectral gap (in the sense of Definition L.4.5).

**Definition M.0.3 (proved vs assumed vs conditional).**  
- Section M.1 is proved from definitions (no external inputs).
- Section M.2 is proved at the quadratic-form level; the operator-theoretic representation step is isolated as an **External Input**.

**Definition M.0.4 (no new named constants).**  
This appendix introduces no named constants in the sense of Appendix A. Any constant symbols (e.g. `\Delta>0`) are local parameters within single statements.

---

## M.1 Reflection positivity permanence

### M.1.1 Setup: OS data and pullback/pushforward

Throughout Section M.1 we use the OS language from Appendix L.

**Definition M.1.1 (OS datum at a given scale).**  
An **OS datum** is a tuple
\[
(\Omega,\mathcal F,\mu,\Theta,\{\tau_n^\Omega\}_{n\in\mathbb Z},\mathcal A_+)
\]
in the sense of Appendix L, i.e.:

- `\mu` is a probability measure on ` (\Omega,\mathcal F)`;
- `\Theta: \Omega\to\Omega` is a measurable involution (Definition L.1.4);
- `\theta` is the induced antilinear involution on observables (Definition L.1.5);
- `\tau_n` are time translations (Definition L.1.3);
- `\mathcal A_+\subseteq \mathcal B(\Omega)` is a positive-time algebra (Definition L.1.6);
- reflection positivity means `\mu((\theta F)F)\ge 0` for all `F\in\mathcal A_+` (Assumption L.1.7(3)).

No additional axioms are imposed unless explicitly stated.

**Definition M.1.2 (coarse-graining morphism of OS data).**  
Let
\[
(\Omega,\mathcal F,\mu,\Theta,\{\tau_n^\Omega\},\mathcal A_+)
\quad\text{and}\quad
(\Omega',\mathcal F',\mu',\Theta',\{\tau_n^{\Omega'}\},\mathcal A_+')
\]
be two OS data.
A measurable map `P: \Omega\to\Omega'` is called a **reflection-equivariant, positive-time compatible coarse-graining map** if:

1. **Reflection equivariance:**
   \[
   P\circ \Theta = \Theta'\circ P.
   \]
2. **Positive-time compatibility:** for every `G\in\mathcal A_+'`, the pullback `G\circ P` belongs to `\mathcal A_+`.

If additionally `\mu'` is the pushforward of `\mu` by `P`, i.e.
\[
\mu' := P_\#\mu,
\]
then we say that `\mu'` is the **coarse-grained pushforward** of `\mu` along `P`.

*Remark.* Time-translation equivariance (`P\circ\tau_n^\Omega = \tau_n^{\Omega'}\circ P`) is not needed for reflection positivity and is therefore not imposed here.

### M.1.2 Pushforward permanence

**Proposition M.1.3 (reflection positivity is preserved by reflection-equivariant pushforward).**  
Let `P: \Omega\to\Omega'` be a reflection-equivariant, positive-time compatible coarse-graining map in the sense of Definition M.1.2, and assume `\mu' = P_\#\mu`. If `\mu` is reflection positive on `\mathcal A_+`, then `\mu'` is reflection positive on `\mathcal A_+'`, i.e.
\[
\mu'\big((\theta' G)G\big)\ge 0\qquad\forall\,G\in\mathcal A_+'.
\]

*Proof.* Fix `G\in\mathcal A_+'` and define `F:=G\circ P`. By positive-time compatibility, `F\in\mathcal A_+`.

By reflection equivariance `P\circ\Theta = \Theta'\circ P` and Definition L.1.5,
\[
(\theta F)(\omega)
= \overline{F(\Theta\omega)}
= \overline{G(P(\Theta\omega))}
= \overline{G(\Theta'(P\omega))}
= (\theta' G)(P\omega),
\]
hence `(\theta F) = (\theta' G)\circ P`.

Using the pushforward relation `\mu'=P_\#\mu`,
\[
\mu'\big((\theta' G)G\big)
= \int_{\Omega'} (\theta' G)(\omega')\,G(\omega')\,d\mu'(\omega')
= \int_{\Omega} (\theta' G)(P\omega)\,G(P\omega)\,d\mu(\omega)
= \int_{\Omega} (\theta F)(\omega)\,F(\omega)\,d\mu(\omega)
= \mu\big((\theta F)F\big).
\]
By reflection positivity of `\mu` on `\mathcal A_+`, the last quantity is nonnegative. ∎

**Corollary M.1.4 (reflection invariance is preserved by reflection-equivariant pushforward).**  
Assume, in addition to the hypotheses of Proposition M.1.3, that `\mu` is reflection invariant in the sense of Assumption L.1.7(2), i.e. `\mu\circ\Theta^{-1}=\mu`. Then `\mu'\circ(\Theta')^{-1}=\mu'`.

*Proof.* For any bounded measurable `G` on `\Omega'`,
\[
\int G\circ\Theta'\,d\mu'
= \int (G\circ\Theta')\circ P\,d\mu
= \int (G\circ P)\circ\Theta\,d\mu
= \int (G\circ P)\,d\mu
= \int G\,d\mu',
\]
where we used `\mu'=P_\#\mu`, reflection equivariance, and reflection invariance of `\mu`. ∎

### M.1.3 Projective limits: cylinder-level permanence

We now record the minimal projective-limit permanence statement in a form that does not require constructing the limit object inside this appendix.

**Definition M.1.5 (projective system of OS data).**  
Let `(I,\preceq)` be a directed set.
For each `i\in I`, let
\[
(\Omega_i,\mathcal F_i,\mu_i,\Theta_i,\{\tau_n^{\Omega_i}\},\mathcal A_{i,+})
\]
be an OS datum (Definition M.1.1).
For `i\preceq j`, let `P_{j\to i}:\Omega_j\to\Omega_i` be measurable maps such that:

1. **Projective compatibility:** `P_{k\to i}=P_{j\to i}\circ P_{k\to j}` whenever `i\preceq j\preceq k`.
2. **Reflection equivariance:** `P_{j\to i}\circ\Theta_j = \Theta_i\circ P_{j\to i}`.
3. **Positive-time compatibility:** for every `G\in\mathcal A_{i,+}`, the pullback `G\circ P_{j\to i}` belongs to `\mathcal A_{j,+}`.
4. **Measure consistency:** `\mu_i = (P_{j\to i})_\#\mu_j`.

**Definition M.1.6 (cylinder observables in an abstract projective limit).**  
Let `\Omega_\infty` be a measurable space with measurable maps `\pi_i: \Omega_\infty\to\Omega_i` satisfying `\pi_i = P_{j\to i}\circ\pi_j` for `i\preceq j`.
A bounded measurable function `F: \Omega_\infty\to\mathbb C` is a **cylinder observable (at level `i`)** if there exists a bounded `\widetilde F: \Omega_i\to\mathbb C` with
\[
F = \widetilde F\circ \pi_i.
\]

**Assumption M.1.7 (existence of a projective-limit probability measure).**  
There exists a probability measure `\mu_\infty` on `\Omega_\infty` such that for every `i\in I`,
\[
(\pi_i)_\#\mu_\infty = \mu_i.
\]
(Existence/constructibility of such a `\mu_\infty` is not addressed here; it is handled as a separate conditional hypothesis in the Core Manuscript.)

**Proposition M.1.8 (reflection positivity in the projective limit, cylinder version).**  
Assume Definition M.1.5 and Assumption M.1.7. Suppose each `\mu_i` is reflection positive on `\mathcal A_{i,+}`.
Define `\Theta_\infty` on `\Omega_\infty` to be any measurable involution satisfying
\[
\pi_i\circ\Theta_\infty = \Theta_i\circ\pi_i\qquad\forall i\in I.
\]
Let `\theta_\infty` be the induced involution on bounded observables as in Definition L.1.5, and define the cylinder positive-time algebra
\[
\mathcal A_{\infty,+}^{\mathrm{cyl}} := \{\widetilde F\circ\pi_i:\ i\in I,\ \widetilde F\in\mathcal A_{i,+}\}.
\]
Then `\mu_\infty` is reflection positive on `\mathcal A_{\infty,+}^{\mathrm{cyl}}`, i.e.
\[
\mu_\infty\big((\theta_\infty F)F\big)\ge 0\qquad\forall\,F\in\mathcal A_{\infty,+}^{\mathrm{cyl}}.
\]

*Proof.* Fix `F\in\mathcal A_{\infty,+}^{\mathrm{cyl}}`. By definition, there exist `i\in I` and `\widetilde F\in\mathcal A_{i,+}` such that `F=\widetilde F\circ\pi_i`.

Using `\pi_i\circ\Theta_\infty=\Theta_i\circ\pi_i` and Definition L.1.5,
\[
(\theta_\infty F)(\omega)
= \overline{F(\Theta_\infty\omega)}
= \overline{\widetilde F(\pi_i(\Theta_\infty\omega))}
= \overline{\widetilde F(\Theta_i(\pi_i\omega))}
= (\theta_i\widetilde F)(\pi_i\omega).
\]
Therefore `(\theta_\infty F)F = \big((\theta_i\widetilde F)\widetilde F\big)\circ\pi_i`.

By the pushforward identity `(\pi_i)_\#\mu_\infty=\mu_i`,
\[
\mu_\infty\big((\theta_\infty F)F\big)
= \int_{\Omega_\infty} \big((\theta_i\widetilde F)\widetilde F\big)\circ\pi_i\,d\mu_\infty
= \int_{\Omega_i} (\theta_i\widetilde F)\widetilde F\,d\mu_i
= \mu_i\big((\theta_i\widetilde F)\widetilde F\big)
\ge 0,
\]
where the last inequality is reflection positivity of `\mu_i` on `\mathcal A_{i,+}`. ∎

---

## M.2 Gap permanence under monotone quadratic-form limits

### M.2.1 Quadratic forms and vacuum subspaces

**Definition M.2.1 (quadratic form).**  
Let `\mathcal H` be a complex Hilbert space with norm `\|\cdot\|`. A **nonnegative quadratic form** on `\mathcal H` is a map
\[
q: D(q)\to [0,\infty),
\]
defined on a linear subspace `D(q)\subseteq\mathcal H`, such that:

1. `q(\lambda\psi)=|\lambda|^2 q(\psi)` for all `\lambda\in\mathbb C`, `\psi\in D(q)`;
2. the polarization
   \[
   q(\psi,\varphi)
   := \frac14\sum_{k=0}^3 i^k\,q(\psi+i^k\varphi)
   \]
   defines a sesquilinear form on `D(q)` with `q(\psi)=q(\psi,\psi)`.

**Definition M.2.2 (closed form; form core).**  
A nonnegative quadratic form `q` is **closed** if `D(q)` is complete for the norm
\[
\|\psi\|_q := \big(\|\psi\|^2 + q(\psi)\big)^{1/2}.
\]
A subspace `\mathcal D_0\subseteq D(q)` is a **form core** if `\mathcal D_0` is dense in `D(q)` with respect to `\|\cdot\|_q`.

**Definition M.2.3 (vacuum subspace and orthogonal projection).**  
Let `\mathcal K\subseteq\mathcal H` be a closed subspace. Denote by `P_\mathcal K` the orthogonal projection onto `\mathcal K`, and write `\mathcal K^\perp := (I-P_\mathcal K)\mathcal H`.

### M.2.2 Monotone families and a persistent gap inequality

**Assumption M.2.4 (monotone approximation by nonnegative forms).**  
Let `\mathcal H` be a Hilbert space, let `\mathcal K\subseteq\mathcal H` be a closed subspace, and let `\mathcal D_0\subseteq\mathcal H` be a dense linear subspace.
Assume we are given a sequence `(q_n)_{n\ge 1}` of nonnegative quadratic forms on `\mathcal H` such that:

1. **Common domain core:** `\mathcal D_0\subseteq D(q_n)` for all `n`.
2. **Monotonicity on the core:** for all `\psi\in\mathcal D_0`,
   \[
   q_1(\psi)\le q_2(\psi)\le \cdots \le q_n(\psi)\le q_{n+1}(\psi)\le\cdots.
   \]
3. **Vacuum sector nullity on the core:** `q_n(\psi)=0` for all `\psi\in \mathcal D_0\cap\mathcal K` and all `n`.

Define the pointwise supremum on `\mathcal D_0` by
\[
q_\infty(\psi) := \sup_{n\ge 1} q_n(\psi)\in[0,\infty]\qquad (\psi\in\mathcal D_0).
\]

**Assumption M.2.5 (uniform gap inequality on the core).**  
There exists `\Delta>0` such that for all `n\ge 1` and all `\psi\in\mathcal D_0`,
\[
q_n(\psi)\ \ge\ \Delta\,\|(I-P_\mathcal K)\psi\|^2.
\]

**Proposition M.2.6 (gap inequality persists under supremum and closure).**  
Assume Assumptions M.2.4–M.2.5.
Then the supremum form `q_\infty` satisfies, for all `\psi\in\mathcal D_0`,
\[
q_\infty(\psi)\ \ge\ \Delta\,\|(I-P_\mathcal K)\psi\|^2.
\]
Moreover, if `q_\infty` admits a closed extension `\overline q_\infty` with form core `\mathcal D_0` (i.e. `\overline q_\infty` is the closure of `q_\infty|_{\mathcal D_0}`), then for all `\psi\in D(\overline q_\infty)`,
\[
\overline q_\infty(\psi)\ \ge\ \Delta\,\|(I-P_\mathcal K)\psi\|^2.
\]

*Proof.*

1. **Supremum preserves the inequality on `\mathcal D_0`.** Fix `\psi\in\mathcal D_0`. For every `n`, Assumption M.2.5 gives `q_n(\psi)\ge \Delta\|(I-P_\mathcal K)\psi\|^2`. Taking `\sup_n` yields the stated inequality for `q_\infty(\psi)`.

2. **Passage to the closure.** Let `\psi\in D(\overline q_\infty)`. By definition of closure with core `\mathcal D_0`, there exists a sequence `(\psi_k)_{k\ge 1}\subset\mathcal D_0` such that
   \[
   \psi_k\to\psi\ \text{in }\mathcal H,
   \qquad
   q_\infty(\psi_k)\to \overline q_\infty(\psi).
   \]
   Since `I-P_\mathcal K` is bounded, `(I-P_\mathcal K)\psi_k\to (I-P_\mathcal K)\psi` in norm, hence
   \[
   \|(I-P_\mathcal K)\psi_k\|^2\to \|(I-P_\mathcal K)\psi\|^2.
   \]
   Applying the inequality from step (1) to each `\psi_k` and letting `k\to\infty` yields
   \[
   \overline q_\infty(\psi)=\lim_k q_\infty(\psi_k)
   \ \ge\ \Delta\lim_k \|(I-P_\mathcal K)\psi_k\|^2
   \ =\ \Delta\|(I-P_\mathcal K)\psi\|^2.
   \]
∎

### M.2.3 Operator representation and spectral gap

**External Input M.2.7 (representation of closed nonnegative forms).**  
Let `\mathcal H` be a Hilbert space and let `q` be a densely defined, closed, nonnegative quadratic form on `\mathcal H`.
Then there exists a unique self-adjoint operator `H\ge 0` such that
\[
D(q)=D(H^{1/2}),
\qquad
q(\psi)=\|H^{1/2}\psi\|^2\ \ \text{for all }\psi\in D(q).
\]
Moreover, for any bounded self-adjoint operator `B` and any `c\in\mathbb R`, the quadratic form inequality
\[
q(\psi)\ge c\,\langle \psi,B\psi\rangle\qquad(\psi\in D(q))
\]
is equivalent to the operator inequality `H\succeq cB` in the sense of quadratic forms.

*(This is the standard first representation theorem for closed forms; the equivalence between form and operator inequalities is a standard corollary.)*

**Corollary M.2.8 (operator lower bound from the form gap inequality).**  
Assume the hypotheses of Proposition M.2.6 and, in addition, that `\overline q_\infty` is densely defined and closed. Let `H_\infty\ge 0` be the self-adjoint operator associated to `\overline q_\infty` by External Input M.2.7.
Then, as quadratic forms on `\mathcal H`,
\[
H_\infty\ \succeq\ \Delta\,(I-P_\mathcal K).
\]

*Proof.* Apply External Input M.2.7 to the inequality in Proposition M.2.6 with `B=(I-P_\mathcal K)`. ∎

**Corollary M.2.9 (spectral gap above the vacuum subspace).**  
Under the hypotheses of Corollary M.2.8, the spectrum of `H_\infty` satisfies
\[
\sigma(H_\infty)\ \subseteq\ \{0\}\ \cup\ [\Delta,\infty).
\]
In particular, if `\ker(H_\infty)=\mathcal K`, then `\mathrm{gap}(H_\infty)\ge \Delta` in the sense of Definition L.4.5.

*Proof.* By Corollary M.2.8, for every `\psi\in D(H_\infty^{1/2})` one has
\[
\|H_\infty^{1/2}\psi\|^2 = \overline q_\infty(\psi)\ge \Delta\,\|(I-P_\mathcal K)\psi\|^2.
\]
In particular, for `\psi\in D(H_\infty)\cap\mathcal K^\perp`,
\[
\langle\psi,H_\infty\psi\rangle = \|H_\infty^{1/2}\psi\|^2\ge \Delta\,\|\psi\|^2.
\]
By the variational characterization of the bottom of the spectrum on the invariant subspace `\mathcal K^\perp`, this implies `\inf\sigma(H_\infty|_{\mathcal K^\perp})\ge \Delta`, hence `\sigma(H_\infty|_{\mathcal K^\perp})\subseteq[\Delta,\infty)`. Since `0\in\sigma(H_\infty)` whenever `\mathcal K\subseteq\ker(H_\infty)`, the claimed spectral inclusion follows.

If additionally `\ker(H_\infty)=\mathcal K`, then the smallest strictly positive spectral value is at least `\Delta`, i.e. `\mathrm{gap}(H_\infty)\ge \Delta` (Definition L.4.5). ∎

---

## M.3 Interface summary

**Definition M.3.1 (reflection-positivity permanence interface).**  
For Core-10, the required structural checks on a cross-cutoff architecture reduce to verifying the hypotheses of Definition M.1.2 at each coarse-graining step (pushforward permanence, Proposition M.1.3) and/or the hypotheses of Definition M.1.5 plus Assumption M.1.7 (projective-limit cylinder permanence, Proposition M.1.8).

**Definition M.3.2 (gap permanence interface).**  
For Core-10, any proposed continuum Hamiltonian `H_\infty` built as a closed-form supremum limit along a scaling trajectory fits into the scheme of Proposition M.2.6. A uniform lower bound expressed as Assumption M.2.5 is inherited by the limit (Proposition M.2.6), and becomes an operator/spectral gap bound via External Input M.2.7 (Corollaries M.2.8–M.2.9).
