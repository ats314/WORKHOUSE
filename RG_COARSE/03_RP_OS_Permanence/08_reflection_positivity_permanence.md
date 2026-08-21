# Reflection positivity permanence under coarse graining and projective limits

\begin{abstract}
This note records two measure-theoretic permanence principles: (i) reflection positivity is preserved under pushforward by a reflection-equivariant coarse-graining map that preserves the positive-time \(\sigma\)-algebra; (ii) reflection positivity passes to a projective (inverse) limit at the level of cylinder observables. These lemmas isolate exactly what an RG/projective architecture must verify to keep OS reconstruction available in a continuum passage.
\end{abstract}

## 1. Reflected probability spaces

A **reflected probability space** is a tuple
\[
(\Omega,\mathcal F,\mu,\theta;\mathcal F_+)
\]
where \((\Omega,\mathcal F,\mu)\) is a probability space, \(\theta:\Omega\to\Omega\) is a measurable involution, and \(\mathcal F_+\subset \mathcal F\) is the “positive-time” sub-\(\sigma\)-algebra.

\begin{definition}[Reflection positivity]
The space is **reflection positive** if for every bounded \(\mathcal F_+\)-measurable complex function \(F\),
\[
\int_\Omega \overline{F(\omega)}\,F(\theta\omega)\,d\mu(\omega)\ge 0.
\]
Equivalently, the Gram matrix \((\langle F_i,\theta F_j\rangle_{L^2(\mu)})_{i,j}\) is PSD for every finite family \(F_1,\dots,F_n\in L^\infty(\mathcal F_+)\).
\end{definition}

## 2. Pushforward permanence

Let \((\Omega,\mathcal F,\mu,\theta;\mathcal F_+)\) be reflection positive and let \((\Omega',\mathcal F',\theta';\mathcal F'_+)\) be another reflected measurable space.

Assume \(P:\Omega\to\Omega'\) satisfies:
\[
P\circ \theta = \theta'\circ P \quad \text{(reflection equivariance)},
\qquad
P^{-1}(\mathcal F'_+)\subset \mathcal F_+ \quad \text{(positive-time preservation)}.
\]
Define \(\mu' := P_\#\mu\).

\begin{lemma}[Pushforward preserves RP]
Under the above assumptions, \((\Omega',\mathcal F',\mu',\theta';\mathcal F'_+)\) is reflection positive.
\end{lemma}

\begin{proof}
Let \(G_i\in L^\infty(\mathcal F'_+)\) and set \(F_i:=G_i\circ P\in L^\infty(\mathcal F_+)\). Using \(\mu'=P_\#\mu\) and equivariance, the Gram entries satisfy
\[
\langle G_i,\theta' G_j\rangle_{L^2(\mu')}
= \langle F_i,\theta F_j\rangle_{L^2(\mu)}.
\]
Since the right-hand Gram matrix is PSD by RP of \(\mu\), so is the left-hand one.
\end{proof}

## 3. Projective-limit permanence (cylinder level)

Let \(\{(\Omega_a,\mathcal F_a,\mu_a,\theta_a;\mathcal F_{a,+})\}_{a\in\mathcal A}\) be a directed family with maps \(P_{a\to a'}\) for “finer” \(a\) to “coarser” \(a'\), satisfying:

- compatibility \(P_{a'\to a''}\circ P_{a\to a'}=P_{a\to a''}\),
- equivariance \(P_{a\to a'}\circ\theta_a=\theta_{a'}\circ P_{a\to a'}\),
- positive-time preservation \(P_{a\to a'}^{-1}(\mathcal F_{a',+})\subset \mathcal F_{a,+}\),
- consistency \((P_{a\to a'})_\#\mu_a = \mu_{a'}\).

Let \((\Omega,\mu)\) be the inverse-limit (Kolmogorov/projective) measure on cylinder functions, with projections \(\pi_a\) and induced involution \(\theta\).

\begin{lemma}[Cylinder-level RP in the inverse limit]
If each \(\mu_a\) is reflection positive, then \(\mu\) is reflection positive on cylinder functions: for any \(a\) and bounded \(\mathcal F_{a,+}\)-measurable \(\widetilde F\), the cylinder function \(F=\widetilde F\circ \pi_a\) satisfies
\[
\int \overline{F}\,(\theta F)\,d\mu \ge 0.
\]
\end{lemma}

\begin{proof}
By the defining property of the projective limit, expectations of \(a\)-cylinder functions under \(\mu\) equal expectations under \(\mu_a\). Using the intertwining \(\pi_a\circ\theta=\theta_a\circ\pi_a\), the cylinder RP inequality reduces exactly to the RP inequality under \(\mu_a\).
\end{proof}

## 4. How this is used

These lemmas don’t build a renormalization map; they tell you what must be checked about whatever map you propose:

- does it commute with reflection?
- does it keep positive-time observables positive-time after pullback?
- is the family consistent so the limit exists on cylinders?

If yes, reflection positivity survives, so OS reconstruction remains available at the continuum level (at least for cylinder observables).
