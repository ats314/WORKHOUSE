# Diffusion → OS Bridge Theorem (Carefully Normalized)

This note produces a **single bridge theorem** in a form that matches your “prove global FI first, then treat OS as a readout layer” strategy.

The theorem is deliberately written in a **model-agnostic operator language**. The only “physics” enters through the meaning of the operators.

---

## 0. Notation / normalization

Let \((\Sigma,\mu_\Sigma)\) be the probability space of a **time-zero slice** (e.g. spatial links at Euclidean time \(t=0\) for a lattice gauge theory).

Let \(L\) be a self-adjoint Markov generator on \(L^2(\mu_\Sigma)\) (e.g. the gauge-invariant Langevin diffusion on the slice), with Dirichlet form
\[
\mathcal E_L(f,f):=\langle f,(-L)f\rangle_{L^2(\mu_\Sigma)}.
\]

Assume \(L\) has a spectral gap \(\lambda_{\mathrm{diff}}>0\) on mean-zero functions:
\[
\mathcal E_L(f,f)\ \ge\ \lambda_{\mathrm{diff}}\,\|f\|_2^2,\qquad \mu_\Sigma(f)=0.
\]

Let \(\mathcal H_{\mathrm{OS}}\) be the Osterwalder–Schrader Hilbert space reconstructed from a reflection-positive Euclidean measure, with transfer operator
\[
T = e^{-H}\quad\text{on }\mathcal H_{\mathrm{OS}},
\]
where \(H\ge 0\) is the OS Hamiltonian.

---

## 1. The bridge theorem

### Theorem (Diffusion gap ⇒ Euclidean-time decay ⇒ OS mass gap, under a one-step comparison)
Assume the following three structural hypotheses:

**(H1) Time-zero representation.**  
There exists an isometric embedding \(J:L^2(\mu_\Sigma)\to\mathcal H_{\mathrm{OS}}\) with range dense in the time-zero subspace, such that \(J\mathbf 1\) is the OS vacuum.

**(H2) Transfer acts on time-zero observables via a Markov operator.**  
There exists a self-adjoint contraction \(K\) on \(L^2(\mu_\Sigma)\) with \(K\mathbf 1=\mathbf 1\) such that
\[
T\,J = J\,K.
\]
Equivalently, \(T\) restricted to the embedded time-zero subspace is unitarily equivalent to \(K\).

**(H3) One-step Dirichlet form comparison (the “intertwining inequality”).**  
There exists \(c>0\) such that for all \(f\in \mathrm{Dom}(L)\) with \(\mu_\Sigma(f)=0\),
\[
\boxed{
\langle f,(I-K)f\rangle_{L^2(\mu_\Sigma)}
\ \ge\
c\,\mathcal E_L(f,f).
}\tag{★}
\]

Then:

1. (**Spectral gap for \(K\)**)
   \[
   \mathrm{spec}(K)\setminus\{1\}\ \subseteq\ (-\infty,\,1-c\lambda_{\mathrm{diff}}\,].
   \]

2. (**OS mass gap lower bound**)
   On the orthogonal complement of the vacuum,
   \[
   \boxed{
   \Delta_{\mathrm{OS}}
   :=\inf(\mathrm{spec}(H)\setminus\{0\})
   \ \ge\
   -\log\bigl(1-c\lambda_{\mathrm{diff}}\bigr)
   \ \ge\
   c\,\lambda_{\mathrm{diff}}
   }
   \]
   (the last inequality uses \(-\log(1-x)\ge x\) for \(x\in[0,1)\)).

3. (**Euclidean-time correlation decay for time-zero observables**)  
   For any \(f\in L^2(\mu_\Sigma)\) with \(\mu_\Sigma(f)=0\),
   \[
   \boxed{
   \big|\langle Jf,\ T^n\,Jf\rangle_{\mathcal H_{\mathrm{OS}}}\big|
   \ \le\
   e^{-n\,\Delta_{\mathrm{OS}}}\,\|f\|_2^2,
   \qquad n\in\mathbb N.
   }
   \]
   In particular, Schwinger two-point functions of time-zero slice observables decay exponentially in Euclidean time.

---

## 2. Proof (short and fully normalized)

Work on the mean-zero subspace \(L^2_0(\mu_\Sigma)\).

Since \(K\) is self-adjoint and \(K\mathbf 1=\mathbf 1\), the spectral theorem implies
\[
\langle f,(I-K)f\rangle = \int_{[-1,1]} (1-\lambda)\,d\nu_f(\lambda),
\qquad
\|f\|_2^2=\int d\nu_f(\lambda),
\]
where \(\nu_f\) is the spectral measure of \(K\) associated to \(f\).

From (★) and the diffusion gap,
\[
\langle f,(I-K)f\rangle\ \ge\ c\,\mathcal E_L(f,f)\ \ge\ c\,\lambda_{\mathrm{diff}}\|f\|_2^2.
\]
So for all \(f\in L^2_0(\mu_\Sigma)\),
\[
\langle f,(I-K)f\rangle\ \ge\ c\,\lambda_{\mathrm{diff}}\langle f,f\rangle.
\]
This forces the operator inequality on \(L^2_0(\mu_\Sigma)\):
\[
I-K\ \succeq\ c\,\lambda_{\mathrm{diff}}\,I
\quad\Longrightarrow\quad
K\ \preceq\ (1-c\lambda_{\mathrm{diff}})\,I,
\]
hence \(\sup(\mathrm{spec}(K)\setminus\{1\})\le 1-c\lambda_{\mathrm{diff}}\).

Now use the intertwining \(TJ=JK\): on the time-zero subspace,
\[
T \ \cong\ K.
\]
Since \(T=e^{-H}\), the nontrivial spectrum of \(H\) corresponds to \(-\log\) of the nontrivial spectrum of \(T\). Therefore
\[
\Delta_{\mathrm{OS}}
=\inf(\mathrm{spec}(H)\setminus\{0\})
\ge
-\log(1-c\lambda_{\mathrm{diff}}).
\]
Finally,
\[
|\langle Jf, T^n Jf\rangle|
=
|\langle f, K^n f\rangle|
\le
\|K^n\|_{L^2_0\to L^2_0}\,\|f\|_2^2
\le
(1-c\lambda_{\mathrm{diff}})^n \|f\|_2^2
\le
e^{-n\Delta_{\mathrm{OS}}}\|f\|_2^2.
\]

---

## 3. What is “new mathematics” here?

Everything except (★) is standard functional analysis.

The entire content is in producing a **model-specific proof of (★)**, i.e. a one-step inequality comparing:

- the **Euclidean-time** transfer operator’s Dirichlet form \(f\mapsto \langle f,(I-K)f\rangle\),
to
- the **configuration diffusion** Dirichlet form \(f\mapsto \mathcal E_L(f,f)\).

In constructive QFT terms: (★) is the precise place where “diffusion control” turns into “OS mass”.

---

## 4. How this matches your stated strategy

Your “anterior route” becomes:

1. Prove global PI/LSI ⇒ \(\lambda_{\mathrm{diff}}>0\).
2. Prove (★) (an intertwining/comparison theorem).
3. Conclude exponential Euclidean-time decay and an OS mass gap.

That makes the mass gap a **robust spectral consequence** of a geometric invariant.
