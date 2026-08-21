# Typicality via Lipschitz scaling and covariance decomposition across a “good event”

This note extracts the project’s *probabilistic glue*:
a way to turn **conditional control on a good region** into **global control**,
using

- a clean covariance/variance decomposition across an event \(K\), and
- a crucial geometric fact: the averaged badness \(\mathcal B_\Lambda\) is \(\big(O(|P|^{-1/2})\big)\)-Lipschitz.

---

## 1. Why the good set is chosen for typicality (not pointwise uniformity)

A key design choice is that the event
\[
K_\Lambda(\varepsilon) := \{\mathcal B_\Lambda \le \varepsilon\}
\]
is selected to be **high probability** under \(\mu_{\Lambda,\beta}\),
rather than to guarantee strong pointwise coercivity.

This is deliberate: on a large lattice, the *average* of many local terms concentrates,
and the averaged functional is smoother (smaller Lipschitz constant) as volume grows.

---

## 2. Linkwise gradient decomposition and bounded overlap

With the product metric, gradients decompose as
\[
|\nabla f|_{g_\Lambda}^2 = \sum_{\ell\in E(\Lambda)} |\nabla_\ell f|_{\mathfrak g}^2.
\]

Each plaquette term depends only on its four boundary links, and there is a bounded overlap constant \(\nu\) such that
each link participates in at most \(\nu\) plaquettes.

This locality is the mechanism that prevents hidden \(|\Lambda|\)-factors.

---

## 3. The key geometric estimate: Lipschitz scaling of \(\mathcal B_\Lambda\)

Define the averaged badness
\[
\mathcal B_\Lambda(U):=\frac{1}{|P(\Lambda)|}\sum_{p\in P(\Lambda)} \vartheta(U_p(U))
\]
for a conjugation-invariant \(\vartheta\in C^2(G)\).

The project proves:

1. **Uniform linkwise gradient bound** for each lifted plaquette observable \(\vartheta_p(U)=\vartheta(U_p(U))\):
   only boundary links contribute, and composing with left/right multiplications and inversion preserves gradient norms.

2. **Lipschitz constant improves with volume**:
   there exists \(L_0<\infty\) depending only on \(\nu\), \(|E|/|P|\), and \(\|\nabla_G\vartheta\|_\infty\), such that
   \[
   \sup_{U\in M_\Lambda}|\nabla \mathcal B_\Lambda(U)|_{g_\Lambda}
   \ \le\
   \frac{L_0}{\sqrt{|P(\Lambda)|}}.
   \]

So \(\mathcal B_\Lambda\) is \(\big(L_0/\sqrt{|P|}\big)\)-Lipschitz.
That \(1/\sqrt{|P|}\) is the entire story: it is the “concentration amplifier.”

---

## 4. Covariance/variance decomposition across an event

For an event \(K\) with \(p=\mu(K)\), \(q=\mu(K^c)\),
one has the fundamental decomposition (schematically)
\[
\mathrm{Var}_\mu(f)
=
p\,\mathrm{Var}_{\mu_K}(f)
+ q\,\mathrm{Var}_{\mu_{K^c}}(f)
+ pq\,(\mu_K f-\mu_{K^c} f)^2.
\]

The last term is the *between-set* contribution: it measures how far the conditional means drift.
Controlling it is the analytic content of the project’s “gluing” step.

---

## 5. Why Lipschitz scaling matters for typicality

When \(\mathcal B_\Lambda\) is \(O(|P|^{-1/2})\)-Lipschitz,
any concentration inequality driven by a local LSI/Poincaré bound yields tails like
\[
\mu_{\Lambda,\beta}\big(\mathcal B_\Lambda - \mathbb E\mathcal B_\Lambda \ge t\big)
\ \lesssim\
\exp\!\big(-c\,|P|\,t^2\big),
\]
at least heuristically in the regime where the constants are controlled.

That is exactly the “typicality lever”:
\(K_\Lambda(\varepsilon)\) can have probability \(1-e^{-c|P|}\),
even if \(K_\Lambda(\varepsilon)\) is not defined by a hard pointwise constraint.

---

## 6. How this plugs into the bigger chain

1. On \(K_\Lambda(r)\): the matrix hinge and HS machinery give **conditional exponential clustering**
   (via \(M_H^{-1}\)).

2. Typicality: \(\mu(K_\Lambda(r))\approx 1\), with an error that can be made very small in volume.

3. Decomposition + gluing: transfer the conditional clustering bound to an **unconditional** one,
   modulo controlling the between-set term \(pq(\mu_K f-\mu_{K^c} f)^2\).

This is the point where drift / Lyapunov arguments and the “pairing/noncancellation” issue enter.

---

## 7. Further work that could expand this

1. **Sharper concentration**: replace “Poincaré → Gaussian tails” heuristics with a verified transportation inequality (e.g. \(T_2\)) on the good set.

2. **Topological sectors**: understand whether typicality of \(\mathcal B_\Lambda\) interacts with twist sectors (center flux) in a way that affects gluing.

3. **RG coupling**: since Lipschitz constants are geometric, one can ask how coarse-graining transforms the typicality event and whether it improves across scales.

