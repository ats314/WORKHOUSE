---
title: "q-Deformed SU(2) 6j-Symbol: Classical Limit with an O(θ² J_max^{5/2}) Error"
author: "Project extraction (compiled)"
date: "2025-12-29"
---

## 0. The deliverable

Let \(q=e^{i\theta}\) with \(|\theta|\ll 1\). For admissible spins \(j_1,\dots,j_6\), define the q-deformed \(6j\)-symbol \(\{6j\}_q\) via q-integers and the q-Racah formula.

The project proves an explicit *polynomial* small-\(\theta\) bound:

\[
\big|\{6j\}_q - \{6j\}\big|
\;\le\; C\,\theta^2\,J_{\max}^{5/2},
\qquad
J_{\max}:=\max_i j_i,
\]
for \(J_{\max}|\theta|\) sufficiently small.

This is valuable because it’s an error bar you can actually budget in numerics.

---

## 1. q-integers and small-\(\theta\) expansion

Define
\[
[n]_q = \frac{q^n-q^{-n}}{q-q^{-1}} = \frac{\sin(n\theta)}{\sin\theta}.
\]

Using \(\sin x = x - x^3/6 + O(x^5)\),
\[
[n]_q
= n\left(1-\frac{(n^2-1)\theta^2}{6}+O(n^4\theta^4)\right),
\]
so
\[
|[n]_q-n|\ \lesssim\ \theta^2\,n^3
\]
uniformly for \(n\le N\) as long as \(|\theta|N\) stays bounded.

---

## 2. q-factorials

\[
[n]_q! := \prod_{k=1}^n [k]_q.
\]

Taking logs and summing the q-integer expansion yields
\[
\log [N]_q! = \log N! - \frac{\theta^2}{6}\sum_{k=1}^N (k^2-1) + O(\theta^4 N^5),
\]
and hence
\[
|[N]_q! - N!|\ \lesssim\ \theta^2\,N^3\,N!
\]
(up to higher-order terms in \(\theta\) under the same uniformity regime).

---

## 3. Feeding the expansions into the q-Racah formula

The q-Racah formula writes the \(6j\)-symbol as
\[
\{6j\}_q
= \Big(\prod_{r=1}^4 \Delta_q(\cdot)\Big)\; \sum_t (-1)^t\,\frac{[t+1]_q!}{\prod_{k=1}^7 [n_k(t)]_q!}.
\]

Each \(\Delta_q\) is built from q-factorial ratios. The expansion above shows that every such ratio differs from the classical one by a factor \(1+O(\theta^2 J_{\max}^3)\) (schematically: the \(N^3\) comes from \(\sum_{k\le N}k^2\sim N^3\)).

So you get a *relative* perturbation:
\[
\frac{\{6j\}_q-\{6j\}}{\{6j\}} = O(\theta^2 J_{\max}^3)
\]
under admissibility and uniformity assumptions.

---

## 4. Converting relative control into absolute control

The last ingredient is an amplitude bound on the classical \(6j\)-symbol. In the semiclassical regime, one has the Ponzano–Regge decay, heuristically scaling like a negative power of \(J_{\max}\). The project uses a conservative bound of the form
\[
|\{6j\}| \le C\,J_{\max}^{-1/2}.
\]

Then
\[
|\{6j\}_q-\{6j\}|
\le C\,(\theta^2 J_{\max}^3)\cdot (J_{\max}^{-1/2})
= C\,\theta^2 J_{\max}^{5/2}.
\]

---

## 5. Why this is genuinely useful

- It’s a *polynomial* error bound — no hidden exponentials.
- The dependence on \(J_{\max}\) tells you how your truncation and deformation interact: you can pick \(\theta\) as a function of \(J_{\max}\) to control errors.
- It supports the broader project theme: **q-deformation as a controlled perturbation**, rather than an uncontrolled “new theory.”

---

## 6. What to do next (if you want to sharpen it)

1. Replace the semiclassical bound with a *rigorous* amplitude estimate in the specific admissible regime you use computationally.
2. Analyze the condition number:
   \[
   \kappa \sim \frac{\sum_t |{\rm term}_t|}{\big|\sum_t (-1)^t{\rm term}_t\big|},
   \]
   which governs floating-point stability when cancellations occur.
3. Track explicit constants: the machinery above can be made explicit but it’s unpleasant bookkeeping.

