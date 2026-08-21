# From Euclidean-time exponential decay to an OS Hamiltonian mass gap

This note is a self-contained functional-analytic implication:

> Under reflection positivity and time-translation invariance, **exponential decay of Euclidean-time correlations at discrete times** implies a **strict spectral gap** for the reconstructed Hamiltonian, with the correct scaling \(m=\eta/a\).

The only external input is the Osterwalder–Schrader reconstruction theorem on the lattice (transfer matrix construction).

---

## 1. Euclidean measure and OS axioms used

Let \(a>0\) be the lattice spacing. Consider the infinite lattice \(\mathbb Z^d\) with the \(0\)-th coordinate designated as Euclidean time.

Let \(\Omega\) be the configuration space (e.g. \(G^{E(\mathbb Z^d)}\) for lattice gauge theory) with its cylinder \(\sigma\)-algebra and a probability measure \(\mu\) (an infinite-volume limit of finite-volume Gibbs measures).

Let \(\tau_n\) denote time translation by \(n\) lattice steps in the time direction, acting on observables by pullback:
\[
(\tau_n F)(U):=F(\tau_{-n}U).
\]
Let \(\Theta\) be reflection across a hyperplane between two consecutive time slices, and define the antilinear involution
\[
(\theta F)(U):=\overline{F(\Theta U)}.
\]

Let \(\mathcal A_+\) be the algebra of bounded cylinder functions supported in the nonnegative-time half-space.

Assume:

* **(OS1)** Time translation invariance: \(\mu(F)=\mu(F\circ\tau_n)\) for cylinder \(F\) and all \(n\in\mathbb Z\).
* **(OS2)** Reflection positivity: \(\mu((\theta F)F)\ge 0\) for all \(F\in\mathcal A_+\).
* **(OS3)** Reflection invariance (optional for notational simplification): \(\mu(F)=\mu(F\circ\Theta)\).

These are the standard hypotheses for lattice OS reconstruction.

---

## 2. External input: OS reconstruction and transfer matrix

**Theorem 2.1 (OS reconstruction / transfer matrix; external input).**
Under (OS1)–(OS2), define
\[
\langle F,G\rangle_{\mathrm{OS}} := \mu((\theta F)G),
\qquad F,G\in\mathcal A_+.
\]
Then the quotient by the null space \(\mathcal N=\{F:\langle F,F\rangle_{\mathrm{OS}}=0\}\) completes to a Hilbert space \(\mathcal H_{\mathrm{OS}}\).
Time translation by one step induces a bounded self-adjoint contraction \(T:\mathcal H_{\mathrm{OS}}\to\mathcal H_{\mathrm{OS}}\) such that
\[
T[F]=[\tau_1F],\qquad 0\le T\le I.
\]
There exists a self-adjoint operator \(H\ge 0\) such that
\[
T=e^{-aH},
\]
and for \(n\ge 0\),
\[
\langle [F],T^n[G]\rangle_{\mathrm{OS}} = \mu((\theta F)\tau_n G).
\tag{2.1}
\]

---

## 3. A spectral-measure lemma: decay \(\Rightarrow\) absence of small spectrum

Let \(H\ge 0\) be self-adjoint on a Hilbert space \(\mathcal H\), and let \(\psi\in\mathcal H\). Let \(\nu_\psi\) denote the spectral measure of \(H\) associated to \(\psi\), so that
\[
\langle \psi,e^{-tH}\psi\rangle = \int_{[0,\infty)} e^{-t\lambda}\,\mathrm d\nu_\psi(\lambda).
\]

### Lemma 3.1 (Discrete-time spectral gap criterion)

Fix \(a>0\) and \(m>0\). Suppose there exists \(C_\psi<\infty\) such that for all integers \(n\ge 0\),
\[
\langle \psi,e^{-naH}\psi\rangle \le C_\psi e^{-mna}.
\tag{3.1}
\]
Then \(\nu_\psi([0,m))=0\). Equivalently, the spectral projection \(E_H([0,m))\psi=0\).

**Proof.**
Assume \(\nu_\psi([0,m))>0\). Then there exists \(\varepsilon\in(0,m)\) such that
\[
\delta:=\nu_\psi([0,m-\varepsilon])>0.
\]
For all \(n\ge 0\),
\[
\langle \psi,e^{-naH}\psi\rangle
=
\int e^{-na\lambda}\,\mathrm d\nu_\psi(\lambda)
\ge
\int_{[0,m-\varepsilon]} e^{-na\lambda}\,\mathrm d\nu_\psi(\lambda)
\ge \delta e^{-na(m-\varepsilon)}.
\]
Divide by \(e^{-mna}\) to get
\[
e^{mna}\langle \psi,e^{-naH}\psi\rangle \ge \delta e^{\varepsilon na}\to\infty\quad(n\to\infty),
\]
contradicting (3.1). Hence \(\nu_\psi([0,m))=0\). ∎

---

## 4. Main implication: time-decay of OS correlators \(\Rightarrow\) mass gap

Assume there exists \(\eta>0\) such that for every \(F,G\in\mathcal A_+\) there is \(C(F,G)<\infty\) with
\[
\big|\mathrm{Cov}_\mu(\theta F,\tau_n G)\big|
\le
C(F,G)\,e^{-\eta n},
\qquad n\ge 0.
\tag{4.1}
\]
Fix \(F\in\mathcal A_+\) and define the centered observable \(F^\circ=F-\mu(F)\). Let \(\psi=[F^\circ]\in\mathcal H_{\mathrm{OS}}\). Then \(\psi\perp \Omega\) (the vacuum) and by (2.1),
\[
\langle \psi,T^n\psi\rangle_{\mathrm{OS}}
=
\mu((\theta F^\circ)\tau_n F^\circ)
=
\mathrm{Cov}_\mu(\theta F,\tau_n F).
\tag{4.2}
\]
Since \(T\ge 0\), \(\langle \psi,T^n\psi\rangle_{\mathrm{OS}}\ge 0\). Thus (4.1) with \(G=F\) gives
\[
\langle \psi,T^n\psi\rangle_{\mathrm{OS}}\le C(F,F)\,e^{-\eta n}.
\tag{4.3}
\]
Using \(T=e^{-aH}\), (4.3) becomes
\[
\langle \psi,e^{-naH}\psi\rangle_{\mathrm{OS}}
\le C(F,F)\,e^{-(\eta/a)\,na}.
\]
Apply Lemma 3.1 with \(m=\eta/a\) to conclude
\[
E_H([0,\eta/a))\psi=0
\qquad\text{for every }\psi=[F^\circ],\ F\in\mathcal A_+.
\]
Since such \(\psi\) span a dense subspace of \(\mathcal H_{\mathrm{OS}}\ominus\mathbb C\Omega\), the spectral projection vanishes on the orthocomplement:
\[
E_H((0,\eta/a))=0\quad\text{on }\mathcal H_{\mathrm{OS}}\ominus\mathbb C\Omega.
\tag{4.4}
\]

### Theorem 4.1 (Euclidean time decay \(\Rightarrow\) OS mass gap)

Assume (OS1)–(OS2) and the decay bound (4.1). Then \(H\) has a strict spectral gap of size \(\eta/a\) above \(\ker(H)\). In particular, if \(\ker(H)=\mathbb C\Omega\) (unique vacuum), then
\[
\mathrm{gap}(H)\ge \frac{\eta}{a}.
\]

---

## 5. Interface to the analytic engine

In applications, \(\eta\) is produced from a volume-uniform exponential clustering bound in the Euclidean-time direction. The only role of this note is to convert that Euclidean decay exponent into a lower bound on the physical mass scale.
