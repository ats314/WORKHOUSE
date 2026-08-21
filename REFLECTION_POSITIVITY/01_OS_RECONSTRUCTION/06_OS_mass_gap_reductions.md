# OS mass gap reductions: (A) decay ⇒ gap, and (B) the one-step “boundary Dirichlet form” target

This note extracts the clean operator-theoretic part of the project’s YM mass-gap pipeline: how to go from Euclidean correlation decay (or a one-step contraction inequality) to a **spectral gap** for the Osterwalder–Schrader Hamiltonian.

No new physics is introduced here; it is functional analysis + OS structure.

---

## 1. OS setup (external input)

Let \(a>0\) be the lattice spacing in Euclidean time. Let \(\Omega=G^{E(\mathbb Z^d)}\) be the infinite-volume configuration space, and let \(\mu\) be a probability measure on \(\Omega\) satisfying:

1. **Time-translation invariance:** \(\mu(F)=\mu(F\circ\tau_n)\) for integer time shifts \(\tau_n\).
2. **Reflection invariance:** \(\mu(F)=\mu(F\circ\Theta)\) for time reflection \(\Theta\).
3. **Reflection positivity:** \(\mu(\theta F\cdot F)\ge 0\) for all \(F\) supported in the nonnegative-time half-space.

(Here \((\theta F)(U)=\overline{F(\Theta U)}\).)

### Theorem 1.1 (Lattice OS reconstruction; external input)
Under the assumptions above, there exists a Hilbert space \(\mathcal H_{\mathrm{OS}}\), a cyclic vector \(\Omega\) (vacuum), a positive contraction \(T_a\) (one-step transfer operator), and a self-adjoint Hamiltonian \(H\ge 0\) such that
\[
T_a = e^{-aH},
\]
and for \(F,G\) supported in nonnegative time,
\[
\langle [F],T_a^n [G]\rangle_{\mathrm{OS}}
=
\mu\big(\theta F\cdot \tau_n G\big),\qquad n\ge 0.
\tag{1.1}
\]

We treat this theorem as a known constructive-QFT result; everything below is self-contained given (1.1).

---

## 2. Reduction A: exponential Euclidean-time decay ⇒ spectral gap

The key observation is spectral-measure rigidity: if all correlations decay like \(e^{-m t}\), then there is no spectrum below \(m\) above the ground space.

### Lemma 2.1 (Discrete-time spectral-measure gap criterion)
Let \(H\ge 0\) be self-adjoint on a Hilbert space and let \(\psi\) be a vector. Let \(\nu_\psi\) be the spectral measure of \(H\) associated to \(\psi\), i.e.
\[
\langle \psi,e^{-tH}\psi\rangle = \int_{[0,\infty)} e^{-t\lambda}\,d\nu_\psi(\lambda),\qquad t\ge 0.
\]
Fix \(a>0\) and \(m>0\). If there exists \(C<\infty\) such that for all integers \(n\ge 0\),
\[
\langle \psi,e^{-naH}\psi\rangle \le C\,e^{-mna},
\tag{2.1}
\]
then \(\nu_\psi([0,m))=0\). Equivalently, the spectral projection \(E_H([0,m))\psi=0\).

**Proof.**
If \(\nu_\psi([0,m))>0\), pick \(\varepsilon\in(0,m)\) so that \(\delta:=\nu_\psi([0,m-\varepsilon])>0\). Then
\[
\langle \psi,e^{-naH}\psi\rangle
\ge
\int_{[0,m-\varepsilon]} e^{-na\lambda}\,d\nu_\psi(\lambda)
\ge
\delta\,e^{-na(m-\varepsilon)}.
\]
Multiplying by \(e^{mna}\) gives \(e^{mna}\langle \psi,e^{-naH}\psi\rangle\ge \delta e^{\varepsilon na}\to\infty\), contradicting (2.1). \(\square\)

### Theorem 2.2 (Euclidean time decay ⇒ OS mass gap)
Assume there exists \(\eta>0\) such that for every \(F\) supported in nonnegative time with \(\mu(F)=0\), there is a constant \(C_F<\infty\) with
\[
0\le \mu\big(\theta F\cdot \tau_n F\big) \le C_F e^{-\eta n}
\qquad\forall n\ge 0.
\tag{2.2}
\]
Then the OS Hamiltonian satisfies:
\[
\text{no spectrum of }H\text{ in }(0,\eta/a)\text{ above }\ker(H).
\tag{2.3}
\]
In particular, if \(\ker(H)=\mathbb C\Omega\) (unique vacuum), then
\[
\mathrm{gap}(H)\ \ge\ \frac{\eta}{a}.
\tag{2.4}
\]

**Proof.**
Let \(\psi=[F]\in\mathcal H_{\mathrm{OS}}\). By (1.1),
\[
\langle \psi, T_a^n\psi\rangle_{\mathrm{OS}}=\mu(\theta F\cdot \tau_n F).
\]
By OS positivity, \(\langle \psi,T_a^n\psi\rangle\ge 0\). Using \(T_a=e^{-aH}\), (2.2) becomes
\[
\langle \psi,e^{-naH}\psi\rangle \le C_F e^{-(\eta/a)\,na}.
\]
Apply Lemma 2.1 with \(m=\eta/a\). Since the set of centered OS vectors \([F]\) is dense in \(\mathcal H_{\mathrm{OS}}\ominus\ker(H)\), the spectral gap statement extends to the whole orthocomplement. \(\square\)

---

## 3. Reduction B: the one-step “boundary Dirichlet form” formulation (target)

The project also formulates a *one-step* route to the same conclusion, in the spirit:

\[
\text{(one-step OS dissipation)}\ \gtrsim\ \text{(one-step configuration dissipation)}
\quad\Rightarrow\quad
\text{mass gap}.
\]

This is potentially powerful because it replaces long-time decay estimates by a single inequality at time step \(a\).

### 3.1 The compressed transfer operator on a spatial slice

Let \(\Sigma:=G^{E_s}\) be the space of spatial links on the \(t=0\) slice, and let \(\nu\) be the induced boundary Gibbs measure
\[
d\nu(\sigma)\propto e^{-S_{\mathrm{sp}}(\sigma)}\prod_{\ell\in E_s} dH(\sigma_\ell),
\]
with \(S_{\mathrm{sp}}\) the purely spatial plaquette action in the slice.

By conditioning the full Gibbs measure on the boundary \(\sigma\) and integrating out the strip between times \(0\) and \(1\), one constructs an integral kernel \(\mathcal K_a(\sigma,\sigma')\ge 0\) and a self-adjoint Markov operator \(K_a\) on \(L^2(\Sigma,\nu)\) such that, for positive-time observables \(F,G\),
\[
\langle [F],T_a [G]\rangle_{\mathrm{OS}}
=
\int_\Sigma \overline{(JF)(\sigma)}\,(K_a\,JG)(\sigma)\,d\nu(\sigma),
\tag{3.1}
\]
where \(J\) is the conditional-expectation “compression” \(JF:=\mathbb E_\mu[F\mid \sigma]\).

This gives a concrete realization of \(T_a\) as a boundary Markov kernel.

### 3.2 One-step dissipation = a Markov Dirichlet form

Define the one-step Dirichlet form of \(K_a\) on \(L^2(\nu)\):
\[
\mathcal E_{K_a}(f,f):=\langle f,(I-K_a)f\rangle_{L^2(\nu)}.
\tag{3.2}
\]

Then for OS vectors \([F]\),
\[
\boxed{
\langle [F],(I-T_a)[F]\rangle_{\mathrm{OS}}
=
\mathcal E_{K_a}(JF,JF).
}
\tag{3.3}
\]

This identity is exact (it is just (3.1) with \(G=F\) and linearity).

### 3.3 Why the comparison must be scale-regularized

Because \(K_a\) is a bounded operator, \(\mathcal E_{K_a}(f,f)\le 2\|f\|_2^2\).  
Therefore **no inequality of the form**
\[
\mathcal E_{K_a}(f,f)\ \ge\ c\int |\nabla f|^2\,d\nu
\]
can hold for all \(f\in H^1\): one can take high-frequency eigenfunctions with arbitrarily large \(\int |\nabla f|^2\).

So the only viable comparison is against a *bounded* configuration dissipation at time step \(a\).

Let \(P_t\) be the Markov semigroup of the configuration diffusion on \((\Sigma,\nu)\) (the same diffusion whose spectral gap/LSI you study on the configuration manifold). Define the scale-\(a\) bounded form
\[
\mathcal E_{\mathrm{conf}}^{(a)}(f,f):=\langle f,(I-P_a)f\rangle_{L^2(\nu)}.
\tag{3.4}
\]

### Target inequality (one-step OS / Dirichlet comparison)
Find \(c>0\) (volume-uniform) such that for all positive-time observables \(F\),
\[
\boxed{
\langle [F],(I-T_a)[F]\rangle_{\mathrm{OS}}
\ \ge\
c\,\mathcal E_{\mathrm{conf}}^{(a)}(JF,JF).
}
\tag{3.5}
\]

### 3.4 Why (3.5) is enough for a mass gap
Assume the diffusion generator on \((\Sigma,\nu)\) has spectral gap \(\lambda_*>0\), i.e.
\[
\|P_t f-\nu(f)\|_2 \le e^{-\lambda_* t}\|f-\nu(f)\|_2.
\]
Then spectral calculus gives
\[
\mathcal E_{\mathrm{conf}}^{(a)}(f,f)
=
\langle f,(I-P_a)f\rangle
\ \ge\
(1-e^{-\lambda_* a})\,\|f-\nu(f)\|_2^2.
\tag{3.6}
\]

Insert (3.6) into (3.5):
\[
\mathcal E_{K_a}(f,f)\ge c(1-e^{-\lambda_* a})\|f-\nu(f)\|_2^2.
\tag{3.7}
\]
Thus \(K_a\) has a Poincaré constant \(\lambda_P(a)\gtrsim c(1-e^{-\lambda_* a})\), meaning its spectrum on mean-zero functions lies in \([0,1-\lambda_P(a)]\). This yields a one-step contraction:
\[
\|K_a^n f\|_2 \le (1-\lambda_P(a))^n\|f\|_2.
\]
Translating back to \(T_a^n=e^{-naH}\) gives exponential decay with exponent \(\eta=-\log(1-\lambda_P(a))\), and Reduction A yields a Hamiltonian gap
\[
\mathrm{gap}(H)\ \ge\ \frac{-\log(1-\lambda_P(a))}{a}.
\tag{3.8}
\]

So proving (3.5) is an alternative route to the same destination: mass gap from a single one-step comparison.

---

## 4. What is proven vs. what is a target

- The decay ⇒ gap implication (Section 2) is fully proven and uses only spectral theory.

- The one-step operator construction and identity (3.1)–(3.3) are standard OS/transfer-matrix conditioning facts; they are already written explicitly in the project notes.

- The comparison inequality (3.5) is a **precise target statement**: it is the minimal viable “one-step OS/Dirichlet bridge” that avoids the boundedness obstruction.

Whether (3.5) can be proven with constants uniform in volume is a genuine technical challenge; the project’s geometry (local strip structure + bounded overlap) suggests a route, but that proof is logically downstream of the hard analysis parts.

---
