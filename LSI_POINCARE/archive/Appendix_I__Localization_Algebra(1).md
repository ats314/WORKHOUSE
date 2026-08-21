---
file: Appendix_I__Localization_Algebra.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
feeds_into:
  - Core-7 (Fixed-cutoff exponential clustering: conditional ⇒ unconditional)
  - Core-8 (Localization/typicality interface: covariance bookkeeping)
---

# Appendix I — Localization algebra (covariance decomposition across an event)

## I.0 Scope

**Definition I.0.1 (scope).**  
This appendix records the purely measure-theoretic identities used to pass from a covariance bound under a conditional Gibbs law `\mu_{\Lambda_L,\beta}(\cdot\mid K_{\Lambda_L})` to a covariance bound under the full Gibbs law `\mu_{\Lambda_L,\beta}`, with an explicit error term proportional to `\mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)`.

No geometric input enters here. The only standing requirement is that `0<\mu(K)<1` so that conditional measures are well-defined (Definition A.6.7).

**Definition I.0.2 (no new constants).**  
This appendix introduces no named constants.

---

## I.1 Standing setting and notation

**Definition I.1.1 (probability space and event).**  
Let `(Ω,\mathcal F,\mu)` be a probability space and let `K\in\mathcal F` satisfy
\[
0<\mu(K)<1.
\tag{I.1}
\]
Write `K^c:=Ω\setminus K`.

**Definition I.1.2 (conditional measures).**  
Define the conditional probability measures `\mu_K` and `\mu_{K^c}` by
\[
\mu_K(A):=\mu(A\mid K)=\frac{\mu(A\cap K)}{\mu(K)},
\qquad
\mu_{K^c}(A):=\mu(A\mid K^c)=\frac{\mu(A\cap K^c)}{\mu(K^c)},
\tag{I.2}
\]
for all `A\in\mathcal F`.  
(These are instances of Definition A.6.7.)

**Definition I.1.3 (expectations, covariance, and sup norm).**  
For an integrable `H:Ω\to\mathbb R`, write `\mu(H):=\int H\,d\mu` and similarly `\mu_K(H)` and `\mu_{K^c}(H)`.  
For integrable `F,G`, define
\[
\mathrm{Cov}_\nu(F,G):=\nu(FG)-\nu(F)\,\nu(G)
\tag{I.3}
\]
for any probability measure `\nu` for which the right-hand side is finite.  
(Compare Definition A.6.6.)  
For bounded `F`, write `\|F\|_\infty:=\sup_{ω\in Ω}|F(ω)|`.

**Definition I.1.4 (conditional mean jump across `K`).**  
For integrable `F`, define
\[
\Delta_K F := \mu_K(F)-\mu_{K^c}(F),
\tag{I.4}
\]
and similarly `\Delta_K G` for a second observable `G`.

---

## I.2 Covariance decomposition across an event

**Lemma I.2.1 (covariance decomposition across an event).**  
Let `F,G:Ω\to\mathbb R` be bounded and measurable. Then
\[
\mathrm{Cov}_\mu(F,G)
=
\mu(K)\,\mathrm{Cov}_{\mu_K}(F,G)
+
\mu(K^c)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)
+
\mu(K)\mu(K^c)\,(\Delta_K F)\,(\Delta_K G).
\tag{I.5}
\]

*Proof.*  
Set `\alpha:=\mu(K)\in(0,1)`. By Definition I.1.2, `\mu` decomposes as the convex mixture
\[
\mu(\cdot)=\alpha\,\mu_K(\cdot)+(1-\alpha)\,\mu_{K^c}(\cdot).
\tag{I.6}
\]
In particular (boundedness implies integrability),
\[
\mu(FG)=\alpha\,\mu_K(FG)+(1-\alpha)\,\mu_{K^c}(FG),
\tag{I.7}
\]
and
\[
\mu(F)=\alpha\,\mu_K(F)+(1-\alpha)\,\mu_{K^c}(F),
\qquad
\mu(G)=\alpha\,\mu_K(G)+(1-\alpha)\,\mu_{K^c}(G).
\tag{I.8}
\]

Introduce the shorthand
\[
A:=\mu_K(F),\quad B:=\mu_{K^c}(F),\quad C:=\mu_K(G),\quad D:=\mu_{K^c}(G).
\tag{I.9}
\]
Then
\[
\mu(F)\mu(G)
=\big(\alpha A+(1-\alpha)B\big)\big(\alpha C+(1-\alpha)D\big)
=\alpha^2 AC+\alpha(1-\alpha)(AD+BC)+(1-\alpha)^2BD.
\tag{I.10}
\]

Using (I.7)–(I.10),
\[
\begin{aligned}
\mathrm{Cov}_\mu(F,G)
&=\mu(FG)-\mu(F)\mu(G)\\
&=\alpha\,\mu_K(FG)+(1-\alpha)\,\mu_{K^c}(FG)
-\Big[\alpha^2 AC+\alpha(1-\alpha)(AD+BC)+(1-\alpha)^2BD\Big].
\end{aligned}
\tag{I.11}
\]

Add and subtract the terms `\alpha AC` and `(1-\alpha)BD` inside (I.11) and regroup:
\[
\begin{aligned}
\mathrm{Cov}_\mu(F,G)
&=\alpha\big(\mu_K(FG)-AC\big)+(1-\alpha)\big(\mu_{K^c}(FG)-BD\big)\\
&\quad+\Big(\alpha AC+(1-\alpha)BD-\alpha^2 AC-\alpha(1-\alpha)(AD+BC)-(1-\alpha)^2BD\Big).
\end{aligned}
\tag{I.12}
\]
The first line of (I.12) equals `\alpha\,\mathrm{Cov}_{\mu_K}(F,G)+(1-\alpha)\,\mathrm{Cov}_{\mu_{K^c}}(F,G)`.

For the bracketed term, use
\[
\alpha AC-\alpha^2 AC=\alpha(1-\alpha)AC,
\qquad
(1-\alpha)BD-(1-\alpha)^2BD=\alpha(1-\alpha)BD,
\]
to obtain
\[
\alpha(1-\alpha)\big(AC+BD-AD-BC\big)=\alpha(1-\alpha)(A-B)(C-D).
\tag{I.13}
\]
By Definition I.1.4, `A-B=\Delta_K F` and `C-D=\Delta_K G`. Substituting (I.13) into (I.12) yields (I.5). ∎

---

## I.3 A raw localization error bound in terms of `\mu(K^c)`

**Lemma I.3.1 (universal covariance bound in sup norm).**  
Let `\nu` be any probability measure on `(Ω,\mathcal F)` and let `F,G:Ω\to\mathbb R` be bounded and measurable. Then
\[
\big|\mathrm{Cov}_\nu(F,G)\big|
\le
4\,\|F\|_\infty\,\|G\|_\infty.
\tag{I.14}
\]

*Proof.*  
Write
\[
\mathrm{Cov}_\nu(F,G)=\nu\big((F-\nu(F))(G-\nu(G))\big).
\]
Then, by Jensen and boundedness,
\[
\big|\mathrm{Cov}_\nu(F,G)\big|
\le
\nu\big(|F-\nu(F)|\,|G-\nu(G)|\big)
\le
\|F-\nu(F)\|_\infty\,\|G-\nu(G)\|_\infty.
\]
Since `|\nu(F)|\le \|F\|_\infty`, we have `\|F-\nu(F)\|_\infty\le 2\|F\|_\infty`, and similarly for `G`. Hence (I.14). ∎


**Proposition I.3.2 (sup-norm localization error bound).**  
Let `F,G:Ω\to\mathbb R` be bounded and measurable. Then
\[
\big|\mathrm{Cov}_\mu(F,G)\big|
\le
\big|\mathrm{Cov}_{\mu_K}(F,G)\big|
+
8\,\|F\|_\infty\,\|G\|_\infty\ \mu(K^c).
\tag{I.15}
\]

*Proof.*  
Start from the decomposition (I.5) and use `\mu(K)\le 1`:
\[
\big|\mathrm{Cov}_\mu(F,G)\big|
\le
\big|\mathrm{Cov}_{\mu_K}(F,G)\big|
+
\mu(K^c)\,\big|\mathrm{Cov}_{\mu_{K^c}}(F,G)\big|
+
\mu(K)\mu(K^c)\,|\Delta_K F|\,|\Delta_K G|.
\tag{I.16}
\]

Apply Lemma I.3.1 with `\nu=\mu_{K^c}` to obtain
\[
\mu(K^c)\,\big|\mathrm{Cov}_{\mu_{K^c}}(F,G)\big|
\le
4\,\|F\|_\infty\,\|G\|_\infty\ \mu(K^c).
\tag{I.17}
\]

Next, by Definition I.1.4 and the triangle inequality,
\[
|\Delta_K F|
=
|\mu_K(F)-\mu_{K^c}(F)|
\le
|\mu_K(F)|+|\mu_{K^c}(F)|
\le
\|F\|_\infty+\|F\|_\infty
=
2\|F\|_\infty,
\tag{I.18}
\]
and similarly `|\Delta_K G|\le 2\|G\|_\infty`. Therefore
\[
\mu(K)\mu(K^c)\,|\Delta_K F|\,|\Delta_K G|
\le
\mu(K^c)\,(2\|F\|_\infty)(2\|G\|_\infty)
=
4\,\|F\|_\infty\,\|G\|_\infty\ \mu(K^c).
\tag{I.19}
\]

Combine (I.16)–(I.19) to obtain (I.15). ∎


---

## I.4 Application hook (no new assumptions)

**Definition I.4.1 (intended application in the fixed-cutoff lattice gauge setting).**  
In the project application, one takes:
- `Ω := M_{\Lambda_L}` (Definition A.4.1),
- `\mu := \mu_{\Lambda_L,\beta}` (Definition A.6.5),
- `K := K_{\Lambda_L}` for the good-set family appearing in Assumption A.11.1.

Then Proposition I.3.2 converts a conditional covariance estimate on `K_{\Lambda_L}` into an unconditional covariance estimate, with a remainder term controlled entirely by the single scalar `\mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)`.
