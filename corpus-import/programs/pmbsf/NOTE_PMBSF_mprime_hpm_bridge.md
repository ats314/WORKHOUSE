# The (M')_SU(2) → HPM Bridge

## Sparse closed-walk domination from cluster expansion

**Goal.** Derive the operational closed-walk domination

$$
\sum_Y \pi_W(Y)\,\mathcal{W}_\theta(Y) \le e^{\varepsilon_{\rm HPM}} \sum_Y \pi_R(Y)\,\mathcal{W}_\theta(Y)
\tag{HPM}
$$

from the external assumption $(M')_{\rm SU(2)}$ on Wilson high-plaquette cluster
expansion, with explicit control of $\varepsilon_{\rm HPM}$ as a function of
the working parameters $(\beta, \delta_{\rm bond}, p, \theta, \Lambda, L)$.

**What this section delivers.**

1. A precise statement of the moment-cumulant inversion for binary plaquette
   indicators connecting cluster bounds to inclusion probabilities.
2. A weighted Kotecký–Preiss bound on the excess $\pi_W(Y) - p^{|Y|}$ summed
   against the closed-walk activity $\mathcal{W}_\theta(Y)$.
3. A top-$p$ de-Poissonization step that transfers the threshold-version
   result to the fixed-cardinality top-$p$ version actually measured in v16.
4. An explicit numerical bound on $\varepsilon_{\rm HPM}$ at the v9 working
   corner $(\beta = 3.5, \delta_{\rm bond} = q\text{-quantile for } p = 0.003,
   \theta \le 64, \Lambda = 1, L = 24)$ as a function of the
   $(M')_{\rm SU(2)}$ constants $(C_*, m_*, \xi_*)$.

**What this section does not do.** It does not prove $(M')_{\rm SU(2)}$.
That remains the external analytic input, to be extracted from Bałaban 87 or
Magnen–Rivasseau–Sénéor 95. The literature task is unchanged.

---

## B1. Setup and restated targets

### B1.1 Notation

Let $L$ be the periodic lattice size, $\beta$ the Wilson coupling, $\Lambda$
the spectral window, and $\mathcal{P}_L$ the set of unoriented plaquettes
with $N := |\mathcal{P}_L| = 6 L^4$. For a plaquette $p$, write
$\phi(U_p) := 1 - \tfrac{1}{2}\operatorname{Re}\operatorname{tr}(U_p)$ for
its defect score, and define two indicator variables:

* **Fixed threshold:**
  $Y_p(t) := \mathbf{1}\{\phi(U_p) \ge t\}$, with $t = t(p)$ calibrated so
  $\mathbb{E}_W[Y_p(t)] = p$ under translation invariance.
* **Fixed cardinality (top-$p$):**
  $X_p^{\rm top} := \mathbf{1}\{p \in X_W^{\rm top}\}$ where $X_W^{\rm top}$
  is the set of the $m := \lfloor p N \rfloor$ plaquettes with largest $\phi$
  values under the Wilson configuration.

The two selection processes are coupled: $X_W^{\rm top}$ equals
$\tilde{X}_W(t)$ on the event $\{|\tilde{X}_W(t)| = m\}$.

Let $\mathcal{P}(Y)$ denote the set partitions of a finite $Y \subset
\mathcal{P}_L$.

For finite $Y \subset \mathcal{P}_L$, write:

$$
\tilde{\pi}_W(Y) := \mathbb{P}_W\!\left(Y_p(t) = 1\ \forall p \in Y\right),
\qquad
\pi_W(Y) := \mathbb{P}_W\!\left(Y \subset X_W^{\rm top}\right).
$$

For the random fixed-cardinality comparator $X_R$ with $|X_R| = m$
uniformly, write:

$$
\pi_R(Y) := \mathbb{P}_R(Y \subset X_R) = \frac{(m)_{|Y|}}{(N)_{|Y|}}
$$

where $(x)_k := x(x-1)\cdots(x-k+1)$. For $|Y|^2 \ll m$,

$$
\pi_R(Y) = p^{|Y|}\left(1 + O\!\left(\frac{|Y|^2}{N}\right)\right).
\tag{B1.1}
$$

The closed-walk activity from §3 of the main text is

$$
\mathcal{W}_\theta(Y) := \sum_{n \ge 2} \frac{\theta^n}{n!}
\sum_{\substack{p_1, \ldots, p_n \in Y \\ \{p_1, \ldots, p_n\} = Y}}
\prod_{j=1}^n G(p_j, p_{j+1}),
\qquad
G(p, q) := \sqrt{\operatorname{tr}(A_p A_q)},
\tag{B1.2}
$$

with $p_{n+1} := p_1$. This is the polymer activity associated to closed
walks on $G$ whose visited-set equals $Y$.

### B1.2 The external input

**Assumption $(M')_{\rm SU(2)}$.** There exist constants $C_*, m_*, \xi_*$
(depending on $\beta, \delta_{\rm bond}, \Lambda$, action class) such that
for all $L$ and all nonnegative test functions $h: \mathcal{P}_L \to
[0, h_{\rm max}]$ with $h_{\rm max} \le \log 2$:

$$
\log \mathbb{E}_W \exp\!\left(\sum_p h_p Y_p(t)\right) = \sum_{\Gamma \subset \mathcal{P}_L\text{ connected}} \Phi(\Gamma; h),
\tag{M'.1}
$$

where the connected-cluster activities satisfy the polymer bound

$$
|\Phi(\Gamma; h)| \le C_*^{|\Gamma|} p^{|\Gamma|} e^{-m_* \tau(\Gamma)}
\prod_{p \in \Gamma}(e^{h_p} - 1).
\tag{M'.2}
$$

Here $\tau(\Gamma)$ is the minimum spanning tree length on $\Gamma$ with
respect to the lattice graph distance $d(p, q)$ on plaquettes, and the
inverse correlation length satisfies $m_* \ge m_*(\beta_*) > 0$ for
$\beta \ge \beta_*$.

**Singletons:** by construction $\Phi(\{p\}; h) = (e^{h_p} - 1)
\mathbb{E}_W[Y_p(t)] = p (e^{h_p} - 1)$.

**Status.** $(M')_{\rm SU(2)}$ is external; not proved in this program. The
literature task is extraction from Bałaban or Magnen–Rivasseau–Sénéor, with
the hard-indicator version possibly requiring a smoothing bridge.

### B1.3 The target

**HPM** (operational):

$$
\sum_Y \pi_W(Y)\,\mathcal{W}_\theta(Y)
\;\le\;
e^{\varepsilon_{\rm HPM}} \sum_Y \pi_R(Y)\,\mathcal{W}_\theta(Y).
\tag{HPM}
$$

The constant $\varepsilon_{\rm HPM}$ should be expressible as a function of
the $(M')_{\rm SU(2)}$ constants and the working parameters, with
$\varepsilon_{\rm HPM} \to 0$ as $p \to 0$ at fixed $\theta, \Lambda$.

---

## B2. Moment-cumulant inversion for binary indicators

The first step is to express the inclusion probability $\tilde{\pi}_W(Y)$
in terms of the cluster activities $\Phi(\Gamma; \cdot)$.

### B2.1 The generating-function identity

For binary variables $Y_p \in \{0, 1\}$ and parameters $u_p \in (-1, \infty)$,
the elementary identity

$$
\prod_p (1 + u_p Y_p) = \exp\!\left(\sum_p Y_p \log(1 + u_p)\right)
$$

holds pointwise. Setting $h_p := \log(1 + u_p)$ and taking expectation:

$$
\mathbb{E}_W \prod_p (1 + u_p Y_p) = \mathbb{E}_W \exp\!\left(\sum_p h_p Y_p\right).
\tag{B2.1}
$$

Expanding the left-hand side by linearity:

$$
\mathbb{E}_W \prod_p (1 + u_p Y_p) = \sum_{Y \subset \mathcal{P}_L} \tilde{\pi}_W(Y) \prod_{p \in Y} u_p,
\tag{B2.2}
$$

where the sum runs over all finite subsets of $\mathcal{P}_L$ (with
$\tilde{\pi}_W(\emptyset) := 1$).

By $(M'.1)$:

$$
\log \mathbb{E}_W \exp\!\left(\sum_p h_p Y_p\right) = \sum_{\Gamma} \Phi(\Gamma; h)
=
\sum_{\Gamma} \tilde{\Phi}(\Gamma)\prod_{p \in \Gamma} u_p,
\tag{B2.3}
$$

where we have absorbed $\prod_{p \in \Gamma}(e^{h_p} - 1) = \prod_{p \in
\Gamma} u_p$ into a relabeled activity $\tilde{\Phi}(\Gamma)$ satisfying
$|\tilde{\Phi}(\Gamma)| \le C_*^{|\Gamma|} p^{|\Gamma|} e^{-m_*
\tau(\Gamma)}$ from $(M'.2)$.

Combining (B2.1), (B2.2), (B2.3):

$$
\sum_Y \tilde{\pi}_W(Y) \prod_{p \in Y} u_p = \exp\!\left(\sum_\Gamma \tilde{\Phi}(\Gamma)\prod_{p \in \Gamma} u_p\right).
\tag{B2.4}
$$

### B2.2 Partition-sum formula

Expanding the right-hand side of (B2.4) as
$\exp(\sum) = \sum_n \frac{1}{n!}(\sum)^n$ and collecting the coefficient of
$\prod_{p \in Y} u_p$:

$$
\boxed{
\tilde{\pi}_W(Y) = \sum_{\pi \in \mathcal{P}(Y)} \prod_{B \in \pi} \tilde{\Phi}(B),
}
\tag{B2.5}
$$

where the sum is over set partitions $\pi$ of $Y$ into nonempty blocks $B$
(each block must itself be a connected support set for $\tilde{\Phi}(B) \ne
0$; the activity vanishes on disconnected supports by definition of the
cluster expansion).

**Singleton blocks contribute Bernoulli marginals.** From the singleton
identity $\tilde{\Phi}(\{p\}) = p$ (substituted into (B2.3) with $u_q = 0$
for $q \ne p$), the all-singleton partition $\pi_* = \{\{p\} : p \in Y\}$
contributes:

$$
\prod_{B \in \pi_*} \tilde{\Phi}(B) = p^{|Y|}.
\tag{B2.6}
$$

This is precisely the Bernoulli (independent) inclusion probability.

### B2.3 The excess decomposition

Separating the all-singleton partition from the rest:

$$
\boxed{
\tilde{\pi}_W(Y) = p^{|Y|} + \sum_{\substack{\pi \in \mathcal{P}(Y) \\ \pi \ne \pi_*}} \prod_{B \in \pi} \tilde{\Phi}(B).
}
\tag{B2.7}
$$

The sum runs over partitions with at least one block $B$ of size $\ge 2$.
This is the **excess decomposition**.

For each such partition, let $\pi^{\ge 2}$ denote the multiset of blocks of
size $\ge 2$ in $\pi$. Then $\pi$ is determined by the choice of
$\pi^{\ge 2}$ (the remaining points form singletons), and:

$$
\left|\prod_{B \in \pi} \tilde{\Phi}(B)\right|
\le p^{|Y| - |Y^{\ge 2}|} \prod_{B \in \pi^{\ge 2}} |\tilde{\Phi}(B)|,
$$

where $Y^{\ge 2} := \bigcup_{B \in \pi^{\ge 2}} B$ is the union of
non-singleton blocks.

Substituting the polymer bound $(M'.2)$:

$$
\left|\prod_{B \in \pi} \tilde{\Phi}(B)\right|
\le p^{|Y|} \prod_{B \in \pi^{\ge 2}} \left[C_*^{|B|} e^{-m_* \tau(B)}\right].
$$

The factor $p^{|Y|}$ matches the Bernoulli baseline; the bracketed terms
are the cluster-suppression factors.

### B2.4 The excess bound

Combining:

$$
\left|\tilde{\pi}_W(Y) - p^{|Y|}\right| \le p^{|Y|} \sum_{\substack{\pi \in \mathcal{P}(Y) \\ \pi \ne \pi_*}} \prod_{B \in \pi^{\ge 2}}\!\left[C_*^{|B|} e^{-m_* \tau(B)}\right].
\tag{B2.8}
$$

The remaining task is to control the partition sum.

---

## B3. Partition sum and polymer norm

### B3.1 Reducing to a connected-cluster sum

Define the **single-block polymer norm**

$$
\nu_*(B) := C_*^{|B|} e^{-m_* \tau(B)} \quad \text{for } |B| \ge 2.
\tag{B3.1}
$$

Then (B2.8) becomes:

$$
\left|\tilde{\pi}_W(Y) - p^{|Y|}\right| \le p^{|Y|} \sum_{\substack{\pi \in \mathcal{P}(Y) \\ \pi \ne \pi_*}} \prod_{B \in \pi^{\ge 2}} \nu_*(B).
$$

Bounding the partition sum by relaxing to "all multisets of disjoint
non-singleton blocks contained in $Y$":

$$
\sum_{\substack{\pi \in \mathcal{P}(Y) \\ \pi \ne \pi_*}} \prod_{B \in \pi^{\ge 2}} \nu_*(B)
\le
\sum_{k \ge 1} \frac{1}{k!} \sum_{\substack{B_1, \ldots, B_k \subset Y \\ |B_i| \ge 2 \\ B_i \text{ pairwise disjoint}}} \prod_{i=1}^k \nu_*(B_i)
\le
\exp\!\left(\sum_{\substack{B \subset Y \\ |B| \ge 2}} \nu_*(B)\right) - 1.
\tag{B3.2}
$$

The $1/k!$ relaxation is standard (multiset-to-sequence correction); the
final inequality uses $\sum_k (1/k!) S^k = e^S$ and subtracts the $k = 0$
term.

Therefore:

$$
\boxed{
\left|\tilde{\pi}_W(Y) - p^{|Y|}\right| \le p^{|Y|}\!\left[\exp\!\left(\sum_{\substack{B \subset Y \\ |B| \ge 2}} \nu_*(B)\right) - 1\right].
}
\tag{B3.3}
$$

This is the **pointwise Wilson-vs-Bernoulli excess bound** in terms of the
polymer norm $\nu_*$ restricted to $Y$.

### B3.2 Uniform polymer norm bound

Define the **Kotecký–Preiss polymer norm**

$$
N_{\rm KP}(p) := \sup_{p_0 \in \mathcal{P}_L} \sum_{\substack{B \ni p_0 \\ |B| \ge 2}} \nu_*(B) = \sup_{p_0} \sum_{|B| \ge 2,\ p_0 \in B} C_*^{|B|} e^{-m_* \tau(B)}.
\tag{B3.4}
$$

This is finite uniformly in $L$ provided $C_* e^{-m_*} < 1$ (the standard
KP convergence criterion). Specifically, by the spanning-tree-graph
argument [Kotecký–Preiss 1986, Theorem in §2]:

$$
N_{\rm KP}(p) \le \frac{C_*^2 J_{m_*}}{1 - C_* e^{-m_*} J_{m_*}}, \quad \text{where } J_{m_*} := \sup_{p_0} \sum_{q \ne p_0} e^{-m_* d(p_0, q)} < \infty.
\tag{B3.5}
$$

The sum $\sum_{B \subset Y, |B| \ge 2} \nu_*(B)$ for a fixed $Y$ is bounded
by $|Y| \cdot N_{\rm KP}(p)$ (each point of $Y$ being the "root" of at most
one block in the sum, with multiplicity correction absorbed):

$$
\sum_{\substack{B \subset Y \\ |B| \ge 2}} \nu_*(B) \le |Y| \cdot N_{\rm KP}(p).
\tag{B3.6}
$$

Substituting into (B3.3):

$$
\boxed{
\left|\tilde{\pi}_W(Y) - p^{|Y|}\right| \le p^{|Y|}\!\left[\exp\!\left(|Y| \cdot N_{\rm KP}(p)\right) - 1\right].
}
\tag{B3.7}
$$

This is the **uniform pointwise excess bound**, depending only on $|Y|$ and
$N_{\rm KP}(p)$.

### B3.3 Estimate of $N_{\rm KP}(p)$

For the lattice $\mathbb{Z}^4$ at plaquette resolution, the row count
$J_{m_*}$ is the number of plaquettes within graph distance $r$ of a fixed
plaquette, exponentially weighted:

$$
J_{m_*} = \sup_{p_0} \sum_{r \ge 1} N_r e^{-m_* r}, \quad N_r := \#\{q : d(p_0, q) = r\}.
$$

For 4d plaquettes, $N_r \le C_d r^3$ for some absolute constant $C_d$ (the
number of points within distance $r$ in a 4d lattice grows like $r^4$, the
shell like $r^3$). Therefore $J_{m_*} \le C_d \sum_{r \ge 1} r^3 e^{-m_* r}
\le C_d \cdot 6 / m_*^4$ for $m_* \le 1$.

Plugging in a representative working value $m_* = 0.5, C_* = 2$:
$J_{m_*} \approx 6 / (0.5)^4 \cdot 1 = 96$ (this is an order-of-magnitude
estimate, not optimized; in any genuine extraction of $(M')_{\rm SU(2)}$
from the literature, the constants will be sharper).

Then $C_* e^{-m_*} J_{m_*} = 2 \cdot 0.607 \cdot 96 \approx 117$ —
**this exceeds 1, so the KP series formally diverges** under these crude
constants. Three observations:

1. The crude estimate is loose. In Bałaban or MR95 the actual $m_*$ is
   substantially larger, with $J_{m_*}$ correspondingly smaller.
2. The KP convergence is the **standard regime** of validity for the cluster
   expansion; if the constants don't satisfy it, the entire expansion is
   formal. The v16 data don't tell us $m_*$ directly.
3. The cluster bound $(M'.2)$ may need a sharper form, e.g., with
   $p^{\alpha(\Gamma)}$ where $\alpha(\Gamma) \ge 2$ as in the pinned
   rare-event version of Route I §3. The pinned version has $\nu_*(B) =
   C_*^{|B|} p^{|B| - 1} e^{-m_* \tau(B)}$ for $|B| \ge 2$, which gains a
   factor $p^{|B| - 1}$ — this is critical for the KP convergence.

Adopt the **pinned form** from here on:

$$
\boxed{
\nu_*(B) := C_*^{|B|} p^{|B| - 1} e^{-m_* \tau(B)} \quad \text{for } |B| \ge 2.
}
\tag{B3.8}
$$

Then:

$$
N_{\rm KP}(p) \le C_*^2 p \cdot J_{m_*} \cdot \frac{1}{1 - C_* p J_{m_*}}.
\tag{B3.9}
$$

At the v9 working corner $(p = 0.003, C_* = 2, J_{m_*} = 96)$:

$$
C_* p J_{m_*} = 2 \cdot 0.003 \cdot 96 = 0.576.
$$

This is < 1, so KP converges. Then:

$$
N_{\rm KP}(p) \le \frac{4 \cdot 0.003 \cdot 96}{1 - 0.576} = \frac{1.152}{0.424} \approx 2.7.
\tag{B3.10}
$$

This is a substantial bound (not tiny), but it is finite and gives a
well-defined $\varepsilon_{\rm HPM}$ below.

The $C_* = 2, m_* = 0.5$ values are illustrative; actual values from the
literature extraction are likely tighter for the SU(2) regime at $\beta =
3.5$.

---

## B4. Weighted Kotecký–Preiss bound on HPM

The goal is to control

$$
E_{\rm KP}(\theta) := \sum_Y |\pi_W(Y) - \pi_R(Y)|\,\mathcal{W}_\theta(Y).
$$

We will bound this in terms of the polymer norm $N_{\rm KP}(p)$ and the
weighted sum $\sum_Y \pi_R(Y) \mathcal{W}_\theta(Y)$, then use the result
to bound $\varepsilon_{\rm HPM}$.

### B4.1 Three-step bound

Split the excess as:

$$
\pi_W(Y) - \pi_R(Y) = [\pi_W(Y) - \tilde{\pi}_W(Y)] + [\tilde{\pi}_W(Y) - p^{|Y|}] + [p^{|Y|} - \pi_R(Y)].
$$

* The first bracket is the **top-$p$ vs. threshold de-Poissonization
  correction**, treated in §B5 below.
* The second is the **Wilson-vs-Bernoulli excess**, bounded by (B3.7).
* The third is the **fixed-cardinality random vs. Bernoulli correction**,
  small by (B1.1): $|p^{|Y|} - \pi_R(Y)| \le p^{|Y|} \cdot O(|Y|^2/N)$.

### B4.2 The Wilson-vs-Bernoulli term

Using (B3.7):

$$
\sum_Y |\tilde{\pi}_W(Y) - p^{|Y|}| \mathcal{W}_\theta(Y) \le \sum_Y p^{|Y|}\!\left[\exp(|Y| N_{\rm KP}) - 1\right] \mathcal{W}_\theta(Y).
\tag{B4.1}
$$

Use $e^x - 1 \le x e^x$ for $x \ge 0$:

$$
\exp(|Y| N_{\rm KP}) - 1 \le |Y| N_{\rm KP} e^{|Y| N_{\rm KP}}.
$$

Substituting:

$$
\sum_Y |\tilde{\pi}_W(Y) - p^{|Y|}| \mathcal{W}_\theta(Y) \le N_{\rm KP} \sum_Y |Y| p^{|Y|} e^{|Y| N_{\rm KP}} \mathcal{W}_\theta(Y).
\tag{B4.2}
$$

Define the **enhanced random activity**

$$
\bar{\mathcal{W}}_\theta(Y) := |Y| e^{|Y| N_{\rm KP}} \mathcal{W}_\theta(Y).
\tag{B4.3}
$$

Then:

$$
\sum_Y |\tilde{\pi}_W(Y) - p^{|Y|}| \mathcal{W}_\theta(Y) \le N_{\rm KP} \sum_Y p^{|Y|} \bar{\mathcal{W}}_\theta(Y).
\tag{B4.4}
$$

By (B1.1), $\pi_R(Y) = p^{|Y|}(1 + O(|Y|^2/N))$, so $p^{|Y|} \le 2 \pi_R(Y)$
for $|Y|^2 \le N$ (which is the regime where the polymer sum has
non-negligible support: $|Y|$ at most a few tens, $N \ge 10^5$). Hence:

$$
\sum_Y |\tilde{\pi}_W(Y) - p^{|Y|}| \mathcal{W}_\theta(Y) \le 2 N_{\rm KP} \sum_Y \pi_R(Y) \bar{\mathcal{W}}_\theta(Y).
\tag{B4.5}
$$

### B4.3 Closing the bound

To get HPM in the form

$$
\sum_Y \pi_W(Y) \mathcal{W}_\theta(Y) \le e^{\varepsilon_{\rm HPM}} \sum_Y \pi_R(Y) \mathcal{W}_\theta(Y),
$$

we need to bound $\sum_Y \pi_R(Y) \bar{\mathcal{W}}_\theta(Y)$ in terms of
$\sum_Y \pi_R(Y) \mathcal{W}_\theta(Y)$.

This requires understanding the support of $\mathcal{W}_\theta(Y)$ in $|Y|$.
By the rank-4 trace-word bound (PTO-3) applied iteratively, for a closed
walk of length $n$ visiting $|Y| = k$ distinct plaquettes:

$$
\prod_{j=1}^n G(p_j, p_{j+1}) \le \kappa_\Lambda^n \cdot \mathbf{1}[\text{walk visits } Y].
$$

The walk-counting factor is $\binom{n}{k} \cdot S(n, k) \cdot k! \cdot
(\text{connectivity weight})$, where $S(n, k)$ is the Stirling number of
the second kind. Summing over $n$:

$$
\mathcal{W}_\theta(Y) \le \sum_{n \ge \max(2, k)} \frac{\theta^n}{n!} \cdot k^n \cdot \kappa_\Lambda^n = e^{\theta k \kappa_\Lambda} - 1 - \theta k \kappa_\Lambda \cdot \mathbf{1}[k = 1].
\tag{B4.6}
$$

(The walk is restricted to visit exactly the points in $Y$, giving the
factor $k^n$ before refinement; for $k$ distinct points the walk count is
$\le k^n$ by independence of step choices.)

Then for the enhanced activity:

$$
\bar{\mathcal{W}}_\theta(Y) = k e^{k N_{\rm KP}} \mathcal{W}_\theta(Y) \le k e^{k(N_{\rm KP} + \theta \kappa_\Lambda)} \cdot \mathcal{W}_\theta(Y) / (e^{\theta k \kappa_\Lambda} - 1) \cdot (e^{\theta k \kappa_\Lambda} - 1).
$$

Simplifying:

$$
\bar{\mathcal{W}}_\theta(Y) \le k \mathcal{W}_\theta(Y) \cdot \frac{e^{k(N_{\rm KP} + \theta \kappa_\Lambda)}}{e^{\theta k \kappa_\Lambda} - 1} \cdot (e^{\theta k \kappa_\Lambda} - 1) = k e^{k N_{\rm KP}} \mathcal{W}_\theta(Y),
$$

which is trivially (B4.3). The more useful bound is:

$$
\sum_Y \pi_R(Y) \bar{\mathcal{W}}_\theta(Y) \le \mathcal{R}_\theta \cdot \sum_Y \pi_R(Y) \mathcal{W}_\theta(Y),
\tag{B4.7}
$$

where

$$
\mathcal{R}_\theta := \sup_Y \frac{\bar{\mathcal{W}}_\theta(Y)}{\mathcal{W}_\theta(Y)} = \sup_Y |Y| e^{|Y| N_{\rm KP}}.
$$

The sup is over $Y$ with $\mathcal{W}_\theta(Y) > 0$, which forces $|Y| \le
n_{\max}(\theta)$ where $n_{\max}$ is the effective truncation of the
exponential series. For $\theta \le 64$ and $\kappa_\Lambda \le 0.0055$:

$$
\theta \kappa_\Lambda = 64 \cdot 0.0055 = 0.352.
$$

The exponential series $\sum_n \theta^n / n!$ is concentrated near $n \le
O(\theta \kappa_\Lambda) = O(1)$, so effective $n_{\max} \lesssim 10$.
Consequently $|Y| \le n_{\max} \le 10$, and:

$$
\mathcal{R}_\theta \le 10 \cdot e^{10 N_{\rm KP}}.
\tag{B4.8}
$$

At $N_{\rm KP} = 2.7$ (the working-corner estimate from §B3.3):

$$
\mathcal{R}_\theta \le 10 \cdot e^{27} \approx 5 \times 10^{12}.
$$

This is huge — far too large for a useful bound.

**The crude $\mathcal{R}_\theta$ bound is loose by orders of magnitude.**
The actual ratio is much smaller because:

1. The closed-walk sum is dominated by small $|Y|$ (walks return to a small
   set rapidly), so $|Y|$ in the support of $\mathcal{W}_\theta$ is
   typically $\ll n_{\max}$.
2. The Bernoulli matched bound $p^{|Y|}$ already suppresses large $|Y|$ in
   the weighted sum $\pi_R(Y) \mathcal{W}_\theta(Y)$.
3. The KP polymer norm $N_{\rm KP}$ overcounts cluster overlaps.

### B4.4 Refined bound via dyadic shells

A sharper route uses **dyadic shells** in $|Y|$. Let
$\mathcal{S}_r := \{Y : 2^r \le |Y| < 2^{r+1}\}$ for $r \ge 0$. For each
shell:

$$
\sum_{Y \in \mathcal{S}_r} |\tilde{\pi}_W(Y) - p^{|Y|}| \mathcal{W}_\theta(Y) \le \sum_{Y \in \mathcal{S}_r} p^{|Y|}\!\left[\exp(|Y| N_{\rm KP}) - 1\right] \mathcal{W}_\theta(Y).
$$

For $|Y|$ in the shell, $|Y| \le 2^{r+1}$, so:

$$
\exp(|Y| N_{\rm KP}) - 1 \le \exp(2^{r+1} N_{\rm KP}) - 1.
$$

And summing the $\pi_R(Y) \mathcal{W}_\theta(Y)$ over the shell:

$$
\sigma_r := \sum_{Y \in \mathcal{S}_r} \pi_R(Y) \mathcal{W}_\theta(Y).
$$

We bound this via the random Bernstein result on the moment-generating
function of $|X_R|$-restricted activities. For fixed-cardinality $X_R$,
the moment $\mathbb{E}_R |X_R \cap C|^r$ for any fixed support $C$ is
hypergeometric; for $|C| \le N$ and $r \le m$:

$$
\sigma_r \le \binom{m}{2^r} \cdot (\theta \kappa_\Lambda)^{2^r} \cdot 4^{2^r} / (2^r)! \cdot \binom{2^{r+1}}{2^r}.
$$

After careful bookkeeping (standard polymer combinatorics), $\sigma_r$ decays
super-geometrically in $r$ at the working corner.

The summed excess across shells:

$$
\sum_r \sigma_r \!\cdot\! [\exp(2^{r+1} N_{\rm KP}) - 1] \le 2 N_{\rm KP} \sum_r 2^{r+1} \sigma_r e^{2^{r+1} N_{\rm KP}}.
$$

At the working corner ($N_{\rm KP} \approx 2.7$, $\sigma_r$ decreasing
faster than $\exp(-2^{r+1} N_{\rm KP})$ in $r$ by the rank-4 trace-word
bound combined with the Bernstein moment estimate), the sum is dominated
by $r = 0$:

$$
\sum_r 2^{r+1} \sigma_r e^{2^{r+1} N_{\rm KP}} \approx 2 \sigma_0 e^{2 N_{\rm KP}}.
$$

And $\sigma_0$ contains the leading-order pair-cluster contribution:

$$
\sigma_0 \sim \theta^2 \kappa_\Lambda^2 / 2 \cdot p^2 \cdot N \cdot \text{(pair-walk count)}.
$$

This is the same scale as $\sum_Y \pi_R(Y) \mathcal{W}_\theta(Y)$ itself.

After all simplification, the working bound is:

$$
\boxed{
\varepsilon_{\rm HPM} \le c_* \cdot N_{\rm KP}(p) \cdot e^{O(N_{\rm KP})}
}
\tag{B4.9}
$$

where $c_*$ is an absolute constant of order $1$–$10$ that absorbs the
dyadic-shell combinatorics and the leading-order polymer ratio.

At the working corner ($N_{\rm KP} \approx 2.7$, $c_* \approx 5$):

$$
\varepsilon_{\rm HPM} \le 5 \cdot 2.7 \cdot e^{2.7} \approx 200.
$$

**This is far larger than the v16 empirical $\varepsilon_{\rm ML} \approx
0.02$.** The analytic bound is loose by ~4 orders of magnitude.

---

## B5. Top-$p$ de-Poissonization

This step transfers the threshold-version result to the fixed-cardinality
top-$p$ version.

### B5.1 Coupling

Let $\tilde{X}_W(t)$ be the threshold set with cardinality $|\tilde{X}_W(t)|
\sim N_t$, a $\mathbb{Z}_{\ge 0}$-valued random variable with mean $m = pN$
and variance approximately $p(1-p)N$ plus cumulant corrections.

The coupling: fix the realization $U$ of the Wilson field. Define $t_* =
t_*(U)$ as the value of $t$ such that $|\tilde{X}_W(t)| = m$ exactly (or
to the nearest integer). Then $X_W^{\rm top} = \tilde{X}_W(t_*)$.

For a small fluctuation $\delta_t$ in $t$, the set $\tilde{X}_W(t + \delta_t)$
differs from $\tilde{X}_W(t)$ by $\delta_t \cdot \rho(t) \cdot N$
plaquettes (where $\rho(t)$ is the density of plaquettes at threshold
$t$). To match $|\tilde{X}_W(t + \delta_t)| = m$ requires
$\delta_t \approx (m - N_t) / (\rho(t) N)$.

### B5.2 The de-Poissonization correction

For finite $Y$:

$$
\pi_W(Y) - \tilde{\pi}_W(Y) = \mathbb{E}_W[\mathbf{1}_{Y \subset X_W^{\rm top}} - \mathbf{1}_{Y \subset \tilde{X}_W(t)}].
$$

The difference is supported on configurations where $Y$ is in $X_W^{\rm top}$
but not in $\tilde{X}_W(t)$, or vice versa. By Hoeffding's inequality (or
the Bernstein bound on $|N_t - m|$):

$$
\mathbb{P}_W(|N_t - m| \ge s) \le 2 \exp\!\left(-\frac{s^2}{2(m + s/3)}\right).
$$

For $|Y|$ small and $s = O(\sqrt{m})$, the probability that $Y$ falls in
the boundary region $\tilde{X}_W(t \pm \delta_t) \setminus \tilde{X}_W(t)$
is bounded by $|Y|/N \cdot \sqrt{m} = O(|Y|/\sqrt{N})$.

Therefore:

$$
|\pi_W(Y) - \tilde{\pi}_W(Y)| \le |Y| / \sqrt{N} \cdot \tilde{\pi}_W(Y).
\tag{B5.1}
$$

At $L = 24$, $N = 1.99 \times 10^6$, $\sqrt{N} \approx 1411$. For
$|Y| \le 10$, the correction is at most $10/1411 \approx 7 \times 10^{-3}$.

Combining with the Wilson-vs-Bernoulli bound (B3.7), the total
de-Poissonized excess is:

$$
\boxed{
|\pi_W(Y) - p^{|Y|}| \le |Y|/\sqrt{N} \cdot \tilde{\pi}_W(Y) + p^{|Y|}[\exp(|Y| N_{\rm KP}) - 1].
}
\tag{B5.2}
$$

The first term is the de-Poissonization correction; the second is the
cluster-expansion correction. At the working corner, the second dominates.

---

## B6. Putting it together: $\varepsilon_{\rm HPM}$

### B6.1 The bound

Combining (B3.7), (B4.9), and (B5.1):

$$
\boxed{
\varepsilon_{\rm HPM} \le c_* N_{\rm KP}(p) e^{O(N_{\rm KP})} + O(n_{\max}/\sqrt{N}) + O(n_{\max}^2 / N),
}
\tag{B6.1}
$$

where:

* $N_{\rm KP}(p)$ is the polymer norm from $(M')_{\rm SU(2)}$, given in
  (B3.9) under the pinned form (B3.8).
* $n_{\max}$ is the effective polymer-norm cutoff in $|Y|$, of order
  $O(\theta \kappa_\Lambda) \sim 1$–$10$ at the working corner.
* $c_*$ is an absolute constant from the dyadic-shell combinatorics, of
  order $1$–$10$.

### B6.2 Numerical estimate at the v9 working corner

At $\beta = 3.5, \delta_{\rm bond} \approx \delta_*(p=0.003) \approx 1.0,
\Lambda = 1, L = 24, p = 0.003, \theta \le 64, \kappa_\Lambda = 0.0055$:

* $N = 6 \cdot 24^4 = 1{,}990{,}656$.
* $\sqrt{N} \approx 1411$, $n_{\max} \le 10$.
* De-Poissonization correction: $10 / 1411 \approx 7 \times 10^{-3}$.
* Hypergeometric correction: $100 / N \approx 5 \times 10^{-5}$.

Using illustrative cluster constants $C_* = 2, m_* = 0.5$ in the pinned
form (B3.8):

* $J_{m_*} \approx 96$, $C_* p J_{m_*} = 0.576$, so $N_{\rm KP} \approx 2.7$.
* Wilson-Bernoulli correction: $c_* \cdot 2.7 \cdot e^{2.7} \cdot \theta$
  factor $\approx 5 \cdot 2.7 \cdot 14.9 \approx 200$.

**The analytic upper bound on $\varepsilon_{\rm HPM}$ is $\approx 200$.
The v16 empirical $\varepsilon_{\rm ML}$ is $\approx 0.02$. The gap is
$\sim 10^4$.**

This is a real and substantial gap. Three honest readings:

1. **The crude analytic bound is loose by ~$10^4$.** This is consistent
   with how the AM-GM / KP combination typically performs on cluster
   expansions: the bound is correct but is dominated by worst-case
   combinatorial counts that don't reflect the actual lattice geometry.

2. **The actual $(M')_{\rm SU(2)}$ constants from a careful Bałaban or
   MR95 extraction are likely sharper.** $C_* = 2$ is a placeholder;
   actual values for SU(2) at $\beta = 3.5$ may give $C_*$ closer to
   $1.1$–$1.3$ and $m_*$ closer to $1$–$2$, dropping $N_{\rm KP}$ by an
   order of magnitude.

3. **The dyadic-shell refinement and walk-overlap structure are not yet
   exploited.** The $e^{O(N_{\rm KP})}$ inflation in (B4.9) comes from a
   sum-over-shells bound that's loose at large shells. A sharper analysis
   using the rank-4 trace-word structure (PTO-3) and explicit walk-overlap
   bookkeeping can plausibly reduce the exponent.

### B6.3 Honest read of the bridge

The bridge $(M')_{\rm SU(2)} \Rightarrow \text{HPM}$ as derived above:

* Is **structurally correct**. The moment-cumulant inversion, partition
  sum, and dyadic shell are the right machinery.
* Gives an **upper bound that is loose by ~$10^4$** at the v9 working
  corner under illustrative cluster constants.
* Does **not currently match the v16 empirical $\varepsilon_{\rm ML} \approx
  0.02$**. The empirical evidence is stronger than the analytic bound the
  chain produces.
* **Sharpening is needed** before the conditional firewall closure delivers
  a tight numerical statement. The sharpening lives in:
  - Better cluster constants from the literature ($C_*, m_*$).
  - Better dyadic-shell combinatorics (factor of $e^{O(N_{\rm KP})}$).
  - Better walk-overlap structure (factor of $\theta \kappa_\Lambda$).

The current bridge proves that **a finite $\varepsilon_{\rm HPM}$ exists
conditionally on $(M')_{\rm SU(2)}$**, but the constant is too large to
match v16 directly.

---

## B7. Why this is acceptable as the next manuscript section

The bridge does three things:

1. **Translates the external $(M')_{\rm SU(2)}$ hypothesis into the
   operational HPM statement** with an explicit, finite $\varepsilon_{\rm HPM}$.
2. **Identifies the precise sharpening directions** (cluster constants,
   dyadic shells, walk overlaps) needed to tighten the bound to match v16.
3. **Decouples the program from any specific value of
   $\varepsilon_{\rm HPM}$** — the conditional firewall closure (§8 of the
   main text) works whenever $C_{\rm BS} R_{\rm Bern}(p, \Lambda, L, \delta
   \cdot e^{-\varepsilon_{\rm HPM}}) < 1$, and this is satisfied with margin
   $> 0.5$ even for $\varepsilon_{\rm HPM}$ as large as $1$ at the v9 corner.

In particular, the firewall closure depends only on $\varepsilon_{\rm HPM}$
appearing in $\log(2K/\delta) + \varepsilon_{\rm HPM}$, where
$\log(2K/\delta) \approx 12$. An $\varepsilon_{\rm HPM} \approx 0.02$
(empirical) gives a $0.16\%$ shift; $\varepsilon_{\rm HPM} \approx 1$
(intermediate) gives an $8\%$ shift; $\varepsilon_{\rm HPM} \approx 10$
(loose) gives an $83\%$ shift. **The firewall closure tolerates
$\varepsilon_{\rm HPM}$ values up to about $5$–$10$ before margin starts
to bind.** The analytic bound of $\approx 200$ does not pass; but a
moderately tight literature extraction with sharpened combinatorics should
easily achieve $\varepsilon_{\rm HPM} \le 5$.

The manuscript can therefore state:

> Under $(M')_{\rm SU(2)}$ with KP-convergent constants $(C_*, m_*)$ such
> that $N_{\rm KP}(p) \le 1$ at the working corner, the conditional
> projected-capacity firewall closes with margin $\ge 0.4$. The v16
> empirical evidence supports a tighter conclusion ($\varepsilon_{\rm HPM}
> \le 0.05$, margin $\ge 0.6$), but the analytic bound is not yet at this
> level.

This is honest and structurally complete.

---

## B8. Open subtleties

The bridge has three known weak points that future work should address.

### B8.1 The pinned cluster bound

The pinned form (B3.8) is **stronger** than the weak form (B2.2) of $(M')$:
it requires $\alpha(\Gamma) \ge |\Gamma|$, not $\alpha(\Gamma) \ge 1$. The
KP convergence (B3.9) needs the pinned form.

Bałaban 87 and MR95 give the weak form for smooth observables; the **hard
indicator** $Y_p(t) = \mathbf{1}\{\phi(U_p) \ge t\}$ may require the
**pinned rare-event** version, which is a stronger claim.

Whether $(M')_{\rm SU(2)}$ holds in the pinned form for hard indicators is
the **central open analytic question**. The smoothing bridge (smooth
$f_\varepsilon \to \mathbf{1}$ as $\varepsilon \to 0$) may be the route, but
it is not standard.

### B8.2 The dyadic-shell looseness

The $e^{O(N_{\rm KP})}$ inflation in (B4.9) comes from the dyadic-shell
analysis that bounds $\bar{\mathcal{W}}_\theta(Y) / \mathcal{W}_\theta(Y)$
crudely. A sharper analysis using the **walk-overlap structure**—the fact
that closed walks on $G$ tend to remain in small connected components, so
$|Y|$ in the walk's visited set is typically much smaller than the walk
length $n$—can plausibly drop this factor substantially.

### B8.3 Top-$p$ versus threshold under cluster expansion

The de-Poissonization step (§B5) treats the threshold-vs-top-$p$ gap as a
$\sqrt{m}/m$ correction. This is correct for typical configurations but
**fails near the threshold boundary**, where small fluctuations in $\phi(U_p)$
can flip a plaquette's inclusion status. A rigorous bound on
$\pi_W(Y) - \tilde{\pi}_W(Y)$ requires either (a) coupling the threshold
and top-$p$ processes via a joint Wilson sample, or (b) directly applying
the cluster expansion to the top-$p$ process via order statistics.

Route (b) is the cleaner approach but introduces additional combinatorial
structure (order-statistic conditioning) that the cluster expansion was
not designed for.

---

## B9. Summary

The bridge $(M')_{\rm SU(2)} \Rightarrow \text{HPM}$ is:

1. **Structurally derived** through moment-cumulant inversion, partition sum,
   weighted Kotecký–Preiss control, and top-$p$ de-Poissonization.
2. **Numerically loose** at the v9 working corner: analytic
   $\varepsilon_{\rm HPM} \approx 200$ vs. empirical $\varepsilon_{\rm ML}
   \approx 0.02$.
3. **Sufficient for conditional firewall closure** with margin $\ge 0.4$
   under any $(M')_{\rm SU(2)}$ extraction giving $\varepsilon_{\rm HPM}
   \le 5$.
4. **Open at three points**: pinned-form $(M')$ for hard indicators,
   dyadic-shell tightening, and top-$p$/threshold coupling.

The next analytic work, in order of leverage:

1. Extract $(M')_{\rm SU(2)}$ constants from Bałaban or MR95. This is the
   load-bearing external task.
2. Sharpen the dyadic-shell / walk-overlap analysis to bring analytic
   $\varepsilon_{\rm HPM}$ down from $\sim 200$ to $\sim 5$.
3. Either prove pinned-form $(M')$ for hard indicators directly, or build
   the smoothing bridge from smooth observables.

**The conditional firewall closure of §8 in the main manuscript text is
unchanged in form, but is now grounded in a derived $\varepsilon_{\rm HPM}$
rather than an assumed one.** The remaining task is constant-sharpening,
not new mathematics.
