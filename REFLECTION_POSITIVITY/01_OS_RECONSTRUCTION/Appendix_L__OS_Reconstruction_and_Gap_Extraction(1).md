---
file: Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_K__Reflection_Positivity_for_Wilson.md
feeds_into:
  - Core-3 (OS framework at fixed cutoff: reconstruction/transfer identity interface)
  - Core-9 (Euclidean time decay ⇒ OS Hamiltonian spectral gap)
  - Core-10 (Conditional continuum extension: gap transfer interface)
---

# Appendix L — OS reconstruction and gap extraction

## L.0 Scope and outputs

**Definition L.0.1 (scope).**  
This appendix isolates the Osterwalder–Schrader (OS) interface used later to convert **Euclidean time decay** of correlations into a **spectral gap** statement for a reconstructed Hamiltonian at fixed cutoff (lattice spacing `a`, Definition A.1.2).

**Definition L.0.2 (outputs).**  
The planned downstream consumption is:

- **External Input L.2.6** (OS reconstruction, discrete-time formulation): produces `\mathcal H_{\mathrm{OS}}`, a positive self-adjoint contraction `T`, and the transfer identity.
- **Proposition L.2.7** (functional calculus): from `0\le T\le I` obtain a self-adjoint `H\ge 0` with `T=e^{-aH}`.
- **Lemma L.3.2** (spectral-support lemma): discrete-time exponential decay of `\langle\psi,e^{-naH}\psi\rangle` forces a spectral gap on the spectral measure of `H` associated to `\psi`.
- **Theorem L.4.7** (gap extraction): Euclidean time exponential decay of centered OS correlations implies `\mathrm{gap}(H)\ge \eta/a`.

**Definition L.0.3 (relation to Appendix K).**  
Appendix K fixes a concrete reflection datum and proves reflection positivity for the finite-volume Wilson measure. Appendix L does not re-prove reflection positivity; it uses reflection positivity only as an explicit hypothesis inside OS reconstruction.

**Definition L.0.4 (no new named constants).**  
This appendix introduces no new named constants. The only global parameter appearing is the lattice spacing `a` (Definition A.1.2). Symbols such as `\eta>0` and `m>0` below are local statement parameters.

---

## L.1 OS datum at fixed cutoff (discrete time)

### L.1.1 Observable algebra

**Definition L.1.1 (bounded observables and involution).**  
Let `(\Omega,\mathcal F)` be a measurable space. Let `\mathcal B(\Omega)` be the complex vector space of bounded `\mathcal F`-measurable functions `F:\Omega\to\mathbb C` with pointwise multiplication. Define the involution `F^*(U):=\overline{F(U)}`.

**Definition L.1.2 (expectation and covariance for a probability measure).**  
Let `\mu` be a probability measure on `(\Omega,\mathcal F)`. For bounded `F,G\in\mathcal B(\Omega)` define
\[
\mu(F):=\int_\Omega F\,d\mu,
\qquad
\mathrm{Cov}_\mu(F,G):=\mu(FG)-\mu(F)\,\mu(G).
\]

### L.1.2 Time translations

**Definition L.1.3 (time translations on configurations and pullback on observables).**  
A discrete-time translation structure is a family of measurable maps
\[
\tau_n^\Omega:\Omega\to\Omega,\qquad n\in\mathbb Z,
\]
such that `\tau_0^\Omega=\mathrm{Id}` and `\tau_n^\Omega\circ \tau_m^\Omega=\tau_{n+m}^\Omega`.

Define the induced maps on observables (still denoted `\tau_n`) by pullback:
\[
(\tau_n F)(U):=F\big((\tau_{-n}^\Omega U)\big),
\qquad F\in\mathcal B(\Omega).
\]
Then `\tau_n` is a `*`-algebra automorphism of `\mathcal B(\Omega)`.

### L.1.3 Reflection and the OS involution

**Definition L.1.4 (configuration reflection).**  
A reflection datum is a measurable involution
\[
\Theta:\Omega\to\Omega,\qquad \Theta^2=\mathrm{Id}.
\]

**Definition L.1.5 (OS antilinear involution on observables).**  
Define `\theta:\mathcal B(\Omega)\to\mathcal B(\Omega)` by
\[
(\theta F)(U):=\overline{F(\Theta U)}.
\]
Then `\theta` is antilinear and satisfies `\theta^2=\mathrm{Id}`.

### L.1.4 Positive-time algebra

**Definition L.1.6 (positive-time algebra).**  
A positive-time algebra `\mathcal A_+` is a unital `*`-subalgebra `\mathcal A_+\subseteq \mathcal B(\Omega)`.

In lattice applications, `\mathcal A_+` is instantiated as the algebra of bounded cylinder observables supported on nonnegative Euclidean times (Definition K.1.15 gives the finite-volume Wilson choice).

### L.1.5 OS structural hypotheses

**Assumption L.1.7 (OS structural axioms, discrete-time version).**  
The triple `(\mu,\theta,\mathcal A_+)` together with the time translations `\{\tau_n\}_{n\in\mathbb Z}` satisfies:

1. **Time-translation invariance:** for all bounded `F\in\mathcal B(\Omega)` and all `n\in\mathbb Z`,
   \[
   \mu(\tau_n F)=\mu(F).
   \]

2. **Reflection invariance:** for all bounded `F\in\mathcal B(\Omega)`,
   \[
   \mu(\theta F)=\overline{\mu(F)}.
   \]
   (Equivalently, `\mu\circ\Theta^{-1}=\mu`.)

3. **Reflection positivity:** for all `F\in\mathcal A_+`,
   \[
   \mu\big((\theta F)\,F\big)\ge 0.
   \]

4. **Reflection covariance of translations:** for all `n\in\mathbb Z`,
   \[
   \Theta\circ \tau_n^\Omega = \tau_{-n}^\Omega\circ \Theta.
   \]
   Equivalently, on observables `\theta\circ\tau_n = \tau_{-n}\circ\theta`.

5. **Stability of the positive-time algebra under forward translations:** for all `n\ge 0`,
   \[
   \tau_n(\mathcal A_+)\subseteq \mathcal A_+.
   \]

---

## L.2 OS Hilbert space and reconstruction interface

### L.2.1 OS sesquilinear form

**Definition L.2.1 (OS form).**  
Define `\langle\cdot,\cdot\rangle_{\mathrm{OS}}` on `\mathcal A_+` by
\[
\langle F,G\rangle_{\mathrm{OS}}:=\mu\big((\theta F)\,G\big),
\qquad F,G\in\mathcal A_+.
\]

**Lemma L.2.2 (Hermitian property and positivity on the diagonal).**  
Under Assumption L.1.7(2)–(3),
1. `\langle\cdot,\cdot\rangle_{\mathrm{OS}}` is Hermitian: `\langle F,G\rangle_{\mathrm{OS}}=\overline{\langle G,F\rangle_{\mathrm{OS}}}`.
2. `\langle F,F\rangle_{\mathrm{OS}}\ge 0` for all `F\in\mathcal A_+`.

*Proof.*
1. Compute
   \[
   \overline{\langle G,F\rangle_{\mathrm{OS}}}
   = \overline{\mu\big((\theta G)F\big)}
   = \mu\big(\theta\big((\theta G)F\big)\big)
   \quad\text{(Assumption L.1.7(2))}.
   \]
   Using `\theta` antilinear and multiplicative,
   \[
   \theta\big((\theta G)F\big)=(\theta F)\,(\theta\theta G)=(\theta F)\,G,
   \]
   hence `\overline{\langle G,F\rangle_{\mathrm{OS}}}=\mu((\theta F)G)=\langle F,G\rangle_{\mathrm{OS}}`.
2. This is exactly Assumption L.1.7(3). ∎

### L.2.2 Null space, quotient, and vacuum

**Definition L.2.3 (OS null space).**  
Define
\[
\mathcal N:=\{F\in\mathcal A_+:\langle F,F\rangle_{\mathrm{OS}}=0\}.
\]

**Lemma L.2.4 (Cauchy–Schwarz and isotropy of `\mathcal N`).**  
Under Assumption L.1.7(3), the seminorm `\|F\|_{\mathrm{OS}}:=\sqrt{\langle F,F\rangle_{\mathrm{OS}}}` satisfies Cauchy–Schwarz:
\[
|\langle F,G\rangle_{\mathrm{OS}}|\le \|F\|_{\mathrm{OS}}\,\|G\|_{\mathrm{OS}}\qquad(F,G\in\mathcal A_+).
\]
In particular, if `F\in\mathcal N` then `\langle F,G\rangle_{\mathrm{OS}}=0` for all `G\in\mathcal A_+`.

*Proof.* For any `F,G\in\mathcal A_+` and `z\in\mathbb C`, reflection positivity gives
\[
0\le \langle F+zG,F+zG\rangle_{\mathrm{OS}}
= \|F\|_{\mathrm{OS}}^2 + z\,\langle F,G\rangle_{\mathrm{OS}} + \overline z\,\langle G,F\rangle_{\mathrm{OS}} + |z|^2\,\|G\|_{\mathrm{OS}}^2.
\]
Choosing `z=-t\,\langle G,F\rangle_{\mathrm{OS}}` with `t\in\mathbb R_{>0}` and using Hermiticity from Lemma L.2.2 yields a quadratic inequality in `t` whose discriminant is nonpositive, giving Cauchy–Schwarz. The final claim follows by taking `\|F\|_{\mathrm{OS}}=0`. ∎

**Definition L.2.5 (OS Hilbert space and vacuum vector).**  
Let `\mathcal D:=\mathcal A_+/\mathcal N` be the quotient by the null space, and write `[F]` for the class of `F\in\mathcal A_+`. The form `\langle\cdot,\cdot\rangle_{\mathrm{OS}}` descends to a genuine inner product on `\mathcal D` by Lemma L.2.4.

Define the OS Hilbert space as the completion
\[
\mathcal H_{\mathrm{OS}}:=\overline{\mathcal D}^{\ \|\cdot\|_{\mathrm{OS}}}.
\]
Define the vacuum vector
\[
\Omega:=[1]\in\mathcal H_{\mathrm{OS}}.
\]

---

### L.2.3 OS reconstruction and transfer identity

**External Input L.2.6 (OS reconstruction at fixed cutoff; discrete-time formulation).**  
Assume Assumption L.1.7. Then there exist:
- the OS Hilbert space `\mathcal H_{\mathrm{OS}}` constructed from `\mathcal A_+` and `\mu` as in Definition L.2.5;
- a bounded operator `T:\mathcal H_{\mathrm{OS}}\to\mathcal H_{\mathrm{OS}}` such that:

1. `T` is a **positive self-adjoint contraction**: `0\le T\le I`.

2. `T` implements one-step Euclidean time translation on positive-time classes:
   \[
   T^n[F]=[\tau_n F]\qquad\text{for all }F\in\mathcal A_+\text{ and all integers }n\ge 0.
   \]

3. (**Transfer identity**) For all `F,G\in\mathcal A_+` and all integers `n\ge 0`,
   \[
   \langle [F],T^n[G]\rangle_{\mathrm{OS}}=\mu\big((\theta F)\,(\tau_n G)\big).
   \]

(The cited theorem is required only in this interface form. No other OS axioms or reconstruction features are used downstream.)

---

### L.2.4 Hamiltonian from a positive contraction

**Proposition L.2.7 (Hamiltonian representation `T=e^{-aH}`).**  
Let `a>0` be the lattice spacing (Definition A.1.2). Let `T` be a positive self-adjoint contraction on a Hilbert space `\mathcal H`. Then there exists a unique self-adjoint operator `H\ge 0` (possibly unbounded) such that
\[
T=e^{-aH}.
\]

*Proof.* By the spectral theorem for bounded self-adjoint operators, there exists a projection-valued measure `E_T` on `[0,1]` such that
\[
T=\int_{[0,1]} \lambda\, dE_T(\lambda).
\]
Define the Borel function `f:(0,1]\to[0,\infty)` by `f(\lambda):=-(1/a)\log\lambda` and set `f(0):=+\infty`. By the functional calculus for self-adjoint operators, the operator
\[
H:=f(T)=\int_{[0,1]} f(\lambda)\,dE_T(\lambda)
\]
is self-adjoint and satisfies `H\ge 0`.

On the common invariant core of vectors `\psi` for which `\int f(\lambda)^2\,d\langle\psi,E_T(\lambda)\psi\rangle<\infty`, one has
\[
\exp(-aH)=\int_{[0,1]} e^{-a f(\lambda)}\,dE_T(\lambda)=\int_{[0,1]} \lambda\,dE_T(\lambda)=T,
\]
where `e^{-a f(0)}:=0` by convention. Since both sides are bounded operators, equality holds on all of `\mathcal H`.

Uniqueness: if `T=e^{-aH_1}=e^{-aH_2}` with `H_1,H_2\ge 0` self-adjoint, then by functional calculus `H_i=-(1/a)\log T` (with the same convention at `0`), so `H_1=H_2`. ∎

**Definition L.2.8 (OS Hamiltonian).**  
Under External Input L.2.6, define the OS Hamiltonian `H\ge 0` on `\mathcal H_{\mathrm{OS}}` by Proposition L.2.7, i.e.
\[
T=e^{-aH}.
\]

---

## L.3 Spectral lemma for decay at discrete times

### L.3.1 Spectral measure

**Definition L.3.1 (spectral measure associated to `H` and a vector).**  
Let `H\ge 0` be self-adjoint on a Hilbert space `\mathcal H`. For `\psi\in\mathcal H`, define the finite Borel measure `\nu_\psi` on `[0,\infty)` by
\[
\nu_\psi(B):=\langle \psi, E_H(B)\psi\rangle,
\]
where `E_H` is the spectral projection measure of `H`.

Then for every bounded Borel function `g:[0,\infty)\to\mathbb C`,
\[
\langle \psi, g(H)\psi\rangle=\int_{[0,\infty)} g(\lambda)\,d\nu_\psi(\lambda).
\]
In particular,
\[
\langle \psi, e^{-tH}\psi\rangle=\int_{[0,\infty)} e^{-t\lambda}\,d\nu_\psi(\lambda)
\qquad(t\ge 0).
\]

### L.3.2 Spectral-support lemma

**Lemma L.3.2 (spectral-measure gap from discrete-time decay).**  
Fix `a>0` and `m>0`. Let `H\ge 0` be self-adjoint on `\mathcal H` and let `\psi\in\mathcal H`. If there exists `C_\psi<\infty` such that for all integers `n\ge 0`,
\[
\langle \psi, e^{-naH}\psi\rangle\le C_\psi\,e^{-mna},
\]
then `\nu_\psi([0,m))=0`, equivalently
\[
E_H([0,m))\,\psi=0.
\]

*Proof.* Suppose `\nu_\psi([0,m))>0`. Then there exists `\varepsilon\in(0,m)` such that `\delta:=\nu_\psi([0,m-\varepsilon])>0`. For each integer `n\ge 0`,
\[
\langle \psi, e^{-naH}\psi\rangle
=\int_{[0,\infty)} e^{-na\lambda}\,d\nu_\psi(\lambda)
\ge \int_{[0,m-\varepsilon]} e^{-na\lambda}\,d\nu_\psi(\lambda)
\ge \delta\,e^{-(m-\varepsilon)na}.
\]
For large `n`, the lower bound `\delta\,e^{-(m-\varepsilon)na}` exceeds `C_\psi\,e^{-mna}` (since `\delta e^{\varepsilon na}\to\infty`), contradicting the assumed upper bound. Hence `\nu_\psi([0,m))=0`. ∎

---

## L.4 Euclidean time decay implies Hamiltonian gap

### L.4.1 Centered observables and density

**Definition L.4.1 (centering).**  
For bounded `F\in\mathcal B(\Omega)`, define its centered version
\[
F^\circ:=F-\mu(F).
\]
Then `\mu(F^\circ)=0`.

**Lemma L.4.2 (vacuum expectation as OS inner product with `\Omega`).**  
Assume Assumption L.1.7(2). For every `F\in\mathcal A_+`,
\[
\langle \Omega,[F]\rangle_{\mathrm{OS}}=\mu(F).
\]
Consequently, `[F^\circ]\perp \Omega` in `\mathcal H_{\mathrm{OS}}`.

*Proof.* Since `\Omega=[1]` and `\theta 1=1`,
\[
\langle \Omega,[F]\rangle_{\mathrm{OS}}=\mu\big((\theta 1)F\big)=\mu(F).
\]
Therefore `\langle \Omega,[F^\circ]\rangle_{\mathrm{OS}}=\mu(F^\circ)=0`. ∎

**Lemma L.4.3 (density of centered classes in `\Omega^\perp`).**  
The set
\[
\mathcal D_0:=\{[F^\circ]: F\in\mathcal A_+\}\subseteq \mathcal H_{\mathrm{OS}}
\]
is dense in `\Omega^\perp`.

*Proof.* By definition, `\mathcal H_{\mathrm{OS}}` is the completion of `\mathcal D=\mathcal A_+/\mathcal N`, so classes `[F]` with `F\in\mathcal A_+` are dense in `\mathcal H_{\mathrm{OS}}`. Let `\psi\in\Omega^\perp`. Choose `[F_k]` with `F_k\in\mathcal A_+` such that `[F_k]\to\psi` in `\mathcal H_{\mathrm{OS}}`.

Applying the continuous linear functional `\varphi(\cdot):=\langle\Omega,\cdot\rangle_{\mathrm{OS}}` and using Lemma L.4.2, we obtain
\[
\mu(F_k)=\langle \Omega,[F_k]\rangle_{\mathrm{OS}}\to \langle\Omega,\psi\rangle_{\mathrm{OS}}=0.
\]
Hence
\[
[F_k^\circ]=[F_k]-\mu(F_k)\,\Omega\longrightarrow \psi-0\cdot\Omega=\psi.
\]
Since `[F_k^\circ]\in \mathcal D_0`, this proves density. ∎

### L.4.2 Transfer identity for centered self-correlations

**Proposition L.4.4 (OS transfer identity for centered self-correlations).**  
Assume Assumption L.1.7 and External Input L.2.6. Let `H` be the OS Hamiltonian (Definition L.2.8). For each `F\in\mathcal A_+` and each integer `n\ge 0`,
\[
\langle [F^\circ], e^{-naH}[F^\circ]\rangle_{\mathrm{OS}}
= \mu\big((\theta F^\circ)\,(\tau_n F^\circ)\big)
= \mathrm{Cov}_\mu(\theta F,\tau_n F).
\]

*Proof.* By Definition L.2.8, `e^{-naH}=T^n`. By External Input L.2.6(3),
\[
\langle [F^\circ],T^n[F^\circ]\rangle_{\mathrm{OS}}=\mu\big((\theta F^\circ)(\tau_n F^\circ)\big).
\]
For the covariance identity, expand using Definition L.4.1:
\[
\mu\big((\theta F^\circ)(\tau_n F^\circ)\big)
=\mu\big((\theta F)(\tau_n F)\big) - \mu(\theta F)\,\mu(\tau_n F).
\]
By Assumption L.1.7(1)–(2), `\mu(\tau_n F)=\mu(F)` and `\mu(\theta F)=\overline{\mu(F)}`. When `F` is real-valued, this equals `\mu(F)`; in general, the algebraic identity above is exactly `\mathrm{Cov}_\mu(\theta F,\tau_n F)` by Definition L.1.2. ∎

### L.4.3 Spectral gap from exponential Euclidean time decay

**Definition L.4.5 (spectral gap above the vacuum).**  
Let `H\ge 0` be self-adjoint on `\mathcal H_{\mathrm{OS}}` with vacuum vector `\Omega`. Define
\[
\mathrm{gap}(H):=\inf\big(\sigma(H)\cap (0,\infty)\big)\in[0,\infty].
\]
Equivalently, `\mathrm{gap}(H)\ge m` holds iff `\sigma(H)\cap (0,m)=\emptyset`.

**Assumption L.4.6 (time-direction exponential decay).**  
There exists `\eta>0` such that for every bounded `F\in\mathcal A_+` there exists `C(F)<\infty` with
\[
\big|\mathrm{Cov}_\mu(\theta F,\tau_n F)\big|\le C(F)\,e^{-\eta n}
\qquad\text{for all integers }n\ge 0.
\]

**Theorem L.4.7 (Euclidean time decay implies Hamiltonian gap at fixed cutoff).**  
Assume Assumption L.1.7 and External Input L.2.6, and let `H` be the OS Hamiltonian (Definition L.2.8). If Assumption L.4.6 holds with rate `\eta>0`, then
\[
\sigma(H)\cap\big(0,\eta/a\big)=\emptyset,
\qquad\text{equivalently}\qquad
\mathrm{gap}(H)\ge \eta/a.
\]
In addition, `\ker(H)=\mathbb C\Omega`.

*Proof.* Fix bounded `F\in\mathcal A_+` and set `\psi:=[F^\circ]\in\mathcal H_{\mathrm{OS}}`. By Proposition L.4.4 and Assumption L.4.6,
\[
0\le \langle \psi,e^{-naH}\psi\rangle_{\mathrm{OS}}
= \mathrm{Cov}_\mu(\theta F,\tau_n F)
\le \big|\mathrm{Cov}_\mu(\theta F,\tau_n F)\big|
\le C(F)\,e^{-\eta n}
\qquad(n\ge 0).
\]
Rewrite the bound as `C(F)\,e^{-(\eta/a)na}` and apply Lemma L.3.2 with `m=\eta/a` to conclude
\[
E_H\big([0,\eta/a)\big)\,\psi=0.
\]
Since `F` was arbitrary, `E_H([0,\eta/a))` annihilates all centered classes `[F^\circ]`. By Lemma L.4.3 these are dense in `\Omega^\perp`, and since `E_H([0,\eta/a))` is an orthogonal projection (hence bounded), it follows that
\[
E_H\big([0,\eta/a)\big)\big|_{\Omega^\perp}=0.
\]
Therefore `\sigma(H)\cap(0,\eta/a)=\emptyset` on `\Omega^\perp`, which is equivalent to `\mathrm{gap}(H)\ge \eta/a`.

Finally, `E_H(\{0\})` is the projection onto `\ker(H)` and satisfies `E_H(\{0\})\le E_H([0,\eta/a))`. Hence `E_H(\{0\})|_{\Omega^\perp}=0`, i.e. `\ker(H)\cap\Omega^\perp=\{0\}`. As `\Omega\in\ker(H)` (because `T\Omega=\Omega` by External Input L.2.6(2) and `T=e^{-aH}`), one concludes `\ker(H)=\mathbb C\Omega`. ∎

---

## L.5 Interface summary (for dependency bookkeeping)

**Definition L.5.1 (used in).**  
Theorem L.4.7 is used in Core-9 to convert a time-direction exponential covariance bound (produced in Core-8 and passed to infinite volume in Core-9) into a quantitative spectral gap lower bound for the OS Hamiltonian.

**Definition L.5.2 (depends on).**  
This appendix depends only on:
- Appendix A (for the fixed cutoff parameter `a`, Definition A.1.2);
- Appendix K (for a concrete reflection positivity input and positive-time algebra conventions in the Wilson lattice gauge setting).
