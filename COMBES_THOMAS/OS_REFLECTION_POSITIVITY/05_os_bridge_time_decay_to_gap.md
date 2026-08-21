# OS bridge: Euclidean time decay \(\Rightarrow\) Hamiltonian mass gap

\begin{abstract}
In the Osterwalder--Schrader (OS) framework at fixed lattice spacing \(a>0\), exponential decay of positive-time Euclidean correlations in the time direction implies a spectral gap for the reconstructed Hamiltonian \(H\). This note packages the implication with a clean discrete-time spectral-measure lemma, giving the quantitative bound \(\mathrm{gap}(H)\ge \eta(a)/a\).
\end{abstract}

## 1. OS input packaged as one identity

Assume OS reconstruction provides:

- a Hilbert space \(\mathcal H_{\mathrm{OS}}\),
- a vacuum vector \(\Omega\),
- a positive self-adjoint contraction \(T\) implementing one lattice time step,
- and a Hamiltonian \(H\ge 0\) such that \(T=e^{-aH}\).

For \(F,G\) in the positive-time algebra \(\mathcal A_+\), OS identifies Euclidean correlations with matrix elements:
\[
\langle [F],\,T^n[G]\rangle_{\mathrm{OS}} 
= \mu\big((\theta F)\,\tau_n G\big),
\qquad n\ge 0.
\tag{OS}
\]

## 2. A discrete-time spectral-measure gap criterion

\begin{lemma}[Discrete-time decay forces spectral support]
Let \(H\ge 0\) be self-adjoint on a Hilbert space and fix \(a>0\). Let \(\nu_\psi\) be the spectral measure of \(H\) associated to \(\psi\), so that
\[
\langle \psi, e^{-tH}\psi\rangle = \int_{[0,\infty)} e^{-t\lambda}\, d\nu_\psi(\lambda).
\]
If there exist \(m>0\) and \(C_\psi<\infty\) such that for all integers \(n\ge 0\),
\[
\langle \psi, e^{-naH}\psi\rangle \le C_\psi\, e^{-mna},
\]
then \(\nu_\psi([0,m))=0\), i.e. \(E_H([0,m))\psi=0\).
\end{lemma}

\begin{proof}
If \(\nu_\psi([0,m))>0\), choose \(\varepsilon\in(0,m)\) such that \(\delta:=\nu_\psi([0,m-\varepsilon])>0\). Then
\(
\langle \psi,e^{-naH}\psi\rangle\ge \delta e^{-(m-\varepsilon)na}
\)
for all \(n\), contradicting the assumed bound as \(n\to\infty\).
\end{proof}

## 3. Euclidean time covariance decay \(\Rightarrow\) gap

Assume a time-direction covariance decay bound: there exists \(\eta>0\) (in lattice steps) such that for all \(F,G\in\mathcal A_+\),
\[
\big|\mathrm{Cov}_\mu(\theta F,\tau_n G)\big|\le C(F,G) e^{-\eta n},\qquad n\ge 0.
\tag{ED}
\]

Fix \(F\in\mathcal A_+\) and center \(F^\circ:=F-\mu(F)\). Set \(\psi:=[F^\circ]\in \mathcal H_{\mathrm{OS}}\). Then by OS and centering,
\[
\langle \psi, T^n \psi\rangle_{\mathrm{OS}} = \mu\big((\theta F^\circ)\,\tau_n F^\circ\big)=\mathrm{Cov}_\mu(\theta F,\tau_n F).
\]
Since \(T\ge 0\), these quantities are nonnegative, and (ED) yields
\[
0\le \langle \psi, T^n \psi\rangle \le C(F,F)e^{-\eta n}.
\]
Using \(T=e^{-aH}\), this is
\[
\langle \psi,e^{-naH}\psi\rangle \le C(F,F)\,e^{-(\eta/a)na}.
\]
Apply the spectral-measure lemma with \(m=\eta/a\) to conclude
\[
E_H([0,\eta/a))\,\psi =0
\quad\text{for all }\psi=[F^\circ].
\]
Density of centered \([F]\) in \(\Omega^\perp\) gives:

\begin{theorem}[Fixed-cutoff OS gap from time decay]
Assume OS reconstruction at lattice spacing \(a>0\) and the Euclidean time decay bound (ED) with exponent \(\eta(a)>0\). Then the OS Hamiltonian \(H\) has no spectrum in \((0,\eta(a)/a)\) on \(\mathcal H_{\mathrm{OS}}\ominus\mathbb C\Omega\). In particular, if the vacuum is unique (\(\ker H=\mathbb C\Omega\)), then
\[
\mathrm{gap}(H)\ge \frac{\eta(a)}{a}.
\]
\end{theorem}

## 4. Why this is a good “interface lemma”

Everything here is model-agnostic: once you have OS plus a time-decay exponent \(\eta(a)\) (in lattice steps), you get a Hamiltonian gap with the correct physical scaling \(m(a)\sim \eta(a)/a\). The entire problem is therefore pushed back to producing \(\eta(a)\) with the right scaling behavior.
