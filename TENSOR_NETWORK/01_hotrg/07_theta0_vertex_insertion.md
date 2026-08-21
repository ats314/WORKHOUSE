# $\theta\to 0$ derivatives of the *full* local vertex weight (including the $q$–$6j$)

This note extracts an **exact** small-$\theta$ expansion (through $O(\theta^2)$) for the *Phase-2* local 8‑valent SU(2) vertex element you build from

- quantum dimensions $d_j(\theta)=[2j+1]_q$ with $q=e^{i\theta}$, and  
- a $q$‑deformed $6j$ via the Racah formula.

The point: at $\theta\to 0$, the deformation inserts a **local operator** that is **not** just a Casimir sum once the $q$–$6j$ part is included.

---

## 1. Conventions used in the project code

The Phase-2 notebook uses
\[
[n]_q \equiv \frac{q^n-q^{-n}}{q-q^{-1}},\qquad q=e^{i\theta},
\]
so for real $\theta$,
\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta}.
\]

The “quantum dimension” is
\[
d_j(\theta)=[2j+1]_q=\frac{\sin((2j+1)\theta)}{\sin\theta}.
\]

The off-diagonal vertex element used in the simplified generator is (schematically)
\[
W(\theta)\;=\;\{6j\}_q(\theta)\;\sqrt{d_{j_1}(\theta)d_{j_2}(\theta)d_{j_3}(\theta)d_{j_4}(\theta)}.
\]
In code the $6j$ is of the specific pattern
\[
\{6j\}_q(\theta)=
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_1 & j_4 & j_2
\end{Bmatrix}_q.
\]

We define the local “insertion” at order $\theta^2$ by
\[
\mathcal O(\text{data})\;\equiv\;-\left.\frac{\partial^2}{\partial\theta^2}\log|W(\theta)|\right|_{\theta=0}.
\]
(For the project’s $[n]_q=\sin(n\theta)/\sin\theta$, everything is **even** in $\theta$, so the first derivative at $\theta=0$ vanishes.)

---

## 2. The universal small-$\theta$ expansion of $q$-numbers and $q$-factorials

For integer $n\ge 1$,
\[
[n]_q=\frac{\sin(n\theta)}{\sin\theta}
= n\left(1-\frac{(n^2-1)}{6}\theta^2+O(\theta^4)\right).
\]

Hence
\[
\log [n]_q = \log n - \frac{(n^2-1)}{6}\theta^2+O(\theta^4),
\qquad
\left.\frac{\partial^2}{\partial\theta^2}\log [n]_q\right|_{0}= -\frac{(n^2-1)}{3}.
\]

For the $q$-factorial (integer arguments),
\[
[n]_q! = \prod_{m=1}^n [m]_q,
\qquad
\log [n]_q! = \log (n!) + a(n)\,\theta^2 + O(\theta^4),
\]
with an **exact** coefficient
\[
a(n)= -\frac{1}{6}\sum_{m=1}^n (m^2-1)
= -\frac{n(2n^2+3n-5)}{36}.
\]
Equivalently,
\[
\left.\frac{\partial^2}{\partial\theta^2}\log [n]_q!\right|_{0}=2a(n)
= -\frac{n(2n^2+3n-5)}{18}.
\]

This single polynomial $a(n)$ is the entire engine behind the “inserted invariant.”

---

## 3. The $q$–$6j$ symbol to $O(\theta^2)$: an exact “Racah-moment” formula

Write the Racah formula schematically as
\[
\{6j\}_q(\theta)=
\exp(L_\Delta(\theta))
\sum_{t=t_{\min}}^{t_{\max}} (-1)^t \exp\!\Big(L_{\rm num}(t;\theta)-L_{\rm den}(t;\theta)\Big),
\]
where all $L$’s are sums of $\log([n]_q!)$ with integer arguments.

Using
\[
\log([n]_q!)=\log(n!)+a(n)\theta^2+O(\theta^4),
\]
each Racah term gains an $O(\theta^2)$ correction that is **just a sum of those $a(\cdot)$ polynomials**.

Define the classical (undeformed) rational Racah weights
\[
w_t \equiv (-1)^t \frac{(t+1)!}{\prod_{i=1}^7 (\text{den}_i(t))!},
\qquad
S_0\equiv \sum_t w_t,
\]
and define the termwise “$a$-insertion”
\[
p_t \equiv a(t+1)-\sum_{i=1}^7 a(\text{den}_i(t)).
\]

Similarly define the prefactor insertion coming from the 4 triangle coefficients:
\[
a_\Delta \equiv \sum_{\text{4 triangles}}
\frac12\Big(a(\alpha_1)+a(\alpha_2)+a(\alpha_3)-a(\alpha_4)\Big),
\]
where $(\alpha_1,\alpha_2,\alpha_3,\alpha_4)$ are the usual Racah triangle factorial arguments
\[
\alpha_1=j_a+j_b-j_c,\;\alpha_2=j_a-j_b+j_c,\;\alpha_3=-j_a+j_b+j_c,\;\alpha_4=j_a+j_b+j_c+1.
\]

Then the **exact** coefficient of $\theta^2$ in $\log\{6j\}_q$ is
\[
c_{6j}=a_\Delta + \frac{\sum_t w_t p_t}{\sum_t w_t}.
\]

Therefore the local inserted operator from the *$q$–$6j$ alone* is
\[
\boxed{
\mathcal O_{6j}\equiv
-\left.\frac{\partial^2}{\partial\theta^2}\log\left|\{6j\}_q(\theta)\right|\right|_{\theta=0}
= -2\,c_{6j}.
}
\]

Key point: the second term is a **Racah-weighted expectation value** of a cubic polynomial in $t$ and the spin-combination arguments. This is why the $q$–$6j$ contribution is **recoupling-sensitive**, not just a Casimir sum.

---

## 4. Add back the quantum dimensions: full vertex insertion for the off-diagonal element

For the project convention $d_j=[2j+1]_q=\sin((2j+1)\theta)/\sin\theta$,
\[
\left.-\frac{\partial^2}{\partial\theta^2}\log d_j(\theta)\right|_0
=\frac{4}{3}j(j+1).
\]

For
\[
W(\theta)=\{6j\}_q(\theta)\sqrt{\prod_{i=1}^4 d_{j_i}(\theta)},
\]
we get
\[
\boxed{
\mathcal O_{\rm vertex}
=
-\left.\frac{\partial^2}{\partial\theta^2}\log|W(\theta)|\right|_0
=
\frac{2}{3}\sum_{i=1}^4 j_i(j_i+1)\;+\;\mathcal O_{6j}.
}
\]

So the $q$-dimension part inserts a simple Casimir sum, but **$\mathcal O_{6j}$ is the new nontrivial piece**.

---

## 5. Concrete exact values (small spins)

Using the Phase‑2 Racah implementation and the exact $O(\theta^2)$ expansion above, the $q$–$6j$ insertion
\[
\mathcal O_{6j}=-\partial_\theta^2\log|\{6j\}_q|_{0}
\]
for the pattern
\[
\begin{Bmatrix}
j_1 & j_2 & j_3\\
j_1 & j_4 & j_2
\end{Bmatrix}_q
\]
takes exact rational values such as:

- $(j_1,j_2,j_3,j_4)=(0,\tfrac12,\tfrac12,\tfrac12)$:  
  \[
  \mathcal O_{6j}=-1.
  \]
- $(1,\tfrac12,\tfrac12,\tfrac12)$:
  \[
  \mathcal O_{6j}=-\frac{11}{3}.
  \]
- $(1,1,1,1)$:
  \[
  \mathcal O_{6j}=+\frac{4}{3}.
  \]
- $(1,\tfrac32,\tfrac32,\tfrac32)$:
  \[
  \mathcal O_{6j}=-\frac{61}{33}.
  \]

And for the *full off-diagonal vertex element* $W(\theta)$ (including $\sqrt{d_{j_1}d_{j_2}d_{j_3}d_{j_4}}$),
\[
\mathcal O_{\rm vertex}
=\frac{2}{3}\sum_{i=1}^4 j_i(j_i+1)+\mathcal O_{6j},
\]
we get, e.g.

- $(0,\tfrac12,\tfrac12,\tfrac12)$:
  \[
  \mathcal O_{\rm vertex}=\frac12.
  \]
- $(1,\tfrac12,\tfrac12,\tfrac12)$:
  \[
  \mathcal O_{\rm vertex}=-\frac{5}{6}.
  \]
- $(1,1,1,1)$:
  \[
  \mathcal O_{\rm vertex}=\frac{20}{3}.
  \]

A diagnostic that the $6j$-piece is genuinely new: two configurations can have the same $\sum j(j+1)$ but wildly different $\mathcal O_{6j}$ (i.e., not reducible to “Casimir only”), because it depends on the Racah recoupling structure encoded in the $t$-sum.

---

## 6. How to use this in the project

Instead of scanning $\theta$ and doing finite differences on $F(\theta)$, you can:

1. compute the *derivative tensors* at $\theta=0$ (or at least the inserted local operators for each tensor element),  
2. propagate those through the HOTRG flow to obtain $\partial_\theta^2 \log Z|_0$ directly.

The exact $O(\theta^2)$ expansion above means you can evaluate $\mathcal O_{6j}$ **without** small-$\theta$ numerical instability, because everything reduces to finite sums of rationals.

---

## 7. Interpretation (physics smell test)

The inserted piece from $q$-dimensions is a Casimir sum (very “$B^2$-like”).

The inserted piece from the $q$–$6j$ is a **Racah moment** of a cubic polynomial in the Racah index. In semiclassical language (large spins), such $q$‑deformations of $6j$ symbols are famous for encoding **constant-curvature (cosmological) corrections** to Regge calculus; the derivative of the deformation parameter at $q\to 1$ corresponds to inserting a curvature/volume-type local invariant.

So: the $\theta\mapsto q$ map is not “just rescaling dims.” The $q$–$6j$ part is where the genuinely nontrivial local structure lives.
