# Log–polar evaluation of q-factorials and q–6j symbols at \(|q|=1\)

> **Status note:** This is a numerical-analysis derivation explaining the strategy implemented in the project for computing q-deformed Racah sums without overflow.  
> The math identities are standard; the *engineering* is the main contribution here.

## 1. Why q-factorials are numerically nasty on the unit circle

With \(q=e^{i\theta}\), the q-number is

\[
[n]_q
=
\frac{q^n-q^{-n}}{q-q^{-1}}
=
\frac{\sin(n\theta)}{\sin\theta}.
\]

Two immediate numerical problems appear:

1. **Near \(\theta=0\)**: both numerator and denominator are small. You want the limit \([n]_q\to n\) without catastrophic cancellation.
2. **Near special angles** (e.g. \(\theta\approx \pi\)): \(\sin\theta\) is again small and \([n]_q\) can become large or ill-defined (especially with half-integer inputs, depending on conventions).

Then q-factorials are products:

\[
[n]_q! = \prod_{k=1}^n [k]_q.
\]

Even for modest \(n\), this can overflow/underflow in floating point.

## 2. Log–polar representation of a q-factorial

The project uses the standard trick:

Represent a possibly signed real product as **magnitude + phase**.

For each factor \([k]_q\in\mathbb{R}\) (in the unit-circle case), write

\[
[k]_q = \operatorname{sgn}([k]_q)\,\bigl|[k]_q\bigr|
\quad\Rightarrow\quad
\log([k]_q)=\log|[k]_q| + i\pi\,\mathbf{1}_{\{[k]_q<0\}}
\quad (\text{principal branch}).
\]

Then

\[
\log([n]_q!)
=
\sum_{k=1}^n \log([k]_q)
=
\underbrace{\sum_{k=1}^n \log|[k]_q|}_{\text{log-magnitude}}
\;+\;
i\pi \underbrace{\sum_{k=1}^n \mathbf{1}_{\{[k]_q<0\}}}_{\text{phase count}}.
\]

Finally
\[
[n]_q! \;=\; \exp\!\bigl(\log([n]_q!)\bigr)
= \exp(L_n)\,e^{i\Phi_n},
\]
where \(L_n\in\mathbb{R}\) and \(\Phi_n\in\mathbb{R}\) are accumulated safely.

This removes overflow from the factorial stage.

## 3. q–6j symbols via the q-Racah sum in log–polar form

A standard q-Racah expression has the shape

\[
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_4 & j_5 & j_6
\end{Bmatrix}_q
=
\left(\prod_{\text{4 faces}} \Delta_q\right)
\sum_{t=t_{\min}}^{t_{\max}} (-1)^t\;
\frac{[t+1]_q!}{\prod_r [t-a_r]_q!\;\prod_s[b_s-t]_q!},
\]

where \(\Delta_q\) is a square root of a ratio of q-factorials and the \(a_r,b_s\) are linear combinations of the spins.

### Log–polar evaluation of a single Racah term

Define the complex log-factorial function \( \mathrm{LogQFact}(n) := \log([n]_q!)\) as above.

Then the logarithm of the magnitude of the \(t\)-term is:

\[
\log|T_t|
=
\Re\Bigl(
\mathrm{LogQFact}(t+1)
-\sum_r \mathrm{LogQFact}(t-a_r)
-\sum_s \mathrm{LogQFact}(b_s-t)
\Bigr),
\]

and the phase is:

\[
\arg(T_t)
=
\Im\Bigl(
\mathrm{LogQFact}(t+1)
-\sum_r \mathrm{LogQFact}(t-a_r)
-\sum_s \mathrm{LogQFact}(b_s-t)
\Bigr)
\;+\;\pi t
\quad(\text{from }(-1)^t).
\]

Then you form the complex number

\[
T_t = \exp(\log|T_t|)\; e^{i\,\arg(T_t)}
\]

and sum them in ordinary complex arithmetic:

\[
S := \sum_t T_t.
\]

### Critical numerical point

You **must** sum the **complex amplitudes** \(T_t\), not their logs.
Taking logs too early destroys phase cancellation information.

## 4. Prefactor handling: \(\Delta_q\) and overall phase

Each \(\Delta_q\) is a square root of a factorial ratio, so it too can be computed in log–polar form:

\[
\Delta_q(a,b,c)
=
\sqrt{
\frac{[a+b-c]_q!\,[a-b+c]_q!\,[-a+b+c]_q!}{[a+b+c+1]_q!}
}.
\]

Compute the log of that ratio, halve it, then exponentiate as magnitude+phase.

## 5. Edge-case handling that matters (and why it’s delicate)

### \(\theta\to 0\)

Use the analytic limit:

\[
[n]_q = \frac{\sin(n\theta)}{\sin\theta} \to n.
\]

Numerically, a stable implementation uses a threshold and returns \(n\) for \(|\theta|<\varepsilon\),
or uses series expansions.

### \(\theta \to \pi\)

The limit of \(\sin(n\theta)/\sin\theta\) depends on the parity of \(n\) and on whether you allow half-integers.
Using l’Hôpital for integer \(n\):

\[
\lim_{\theta\to \pi}\frac{\sin(n\theta)}{\sin\theta}
=
\frac{n\cos(n\pi)}{\cos\pi}
=
-n(-1)^n = n(-1)^{n+1}.
\]

Half-integer handling is convention-sensitive; naïve formulas can diverge.
This is not “just a numerical bug”: it’s a real definitional corner where you must decide what theory you mean.

## 6. What this establishes (as a “proof” of algorithmic correctness)

Assuming:
1. your q-number \([n]_q\) is defined consistently,
2. your q-Racah formula for \(\{6j\}_q\) is correct,

then the log–polar implementation is **algebraically identical** to the direct factorial product implementation, because it is literally the same products and ratios after applying:

\[
\prod_k x_k = \exp\!\left(\sum_k \log x_k\right)
\]
with phase bookkeeping for negative real factors.

So the “proof” is a bookkeeping identity: you get the same value, but without overflow.

## 7. Upgrades that would make this *research-grade*

1. **Tetrahedral symmetry tests**: verify the known permutation symmetries of the q–6j numerically.
2. **High precision fallback**: if a term’s \(\log|T_t|\) is too large, use `mpmath` / arbitrary precision for that block.
3. **Compensated summation**: use Kahan-style techniques for complex sums if large cancellations appear.
4. **Vectorization + JAX**: rewrite the Racah sum as a vectorized scan with stable `logsumexp`-like tricks adapted to complex numbers.

This is the sort of numerical “clean room” that prevents endless re-debugging.
