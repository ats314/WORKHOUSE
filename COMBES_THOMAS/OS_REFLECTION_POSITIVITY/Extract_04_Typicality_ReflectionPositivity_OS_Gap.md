# From “good-set typicality” to OS mass gap: a pipeline

\begin{center}
\textbf{Extracted from: Appendix J (typicality), Appendix K (reflection positivity), Appendix L (OS reconstruction and gap extraction).}
\end{center}

## 1. Why a good set \(K_{\Lambda_L}\)?

Many analytic inequalities (curvature lower bounds, convexity, ... ) are easiest to prove **locally** in configuration space, typically in a neighborhood of the vacuum where plaquette holonomies stay close to \(\mathbf 1\). One then wants to convert a bound that holds conditionally on a “good event” \(K_{\Lambda_L}\) into an unconditional statement.

The work here isolates an explicit, volume-scale typicality mechanism:
\[
\mu_{\Lambda_L,\beta}(K_{\Lambda_L}^c)\le \exp\big(-c_{\mathrm{typ}}|P(\Lambda_L)|\big).
\]
Once you have this, conditional exponential clustering bounds can be promoted to unconditional ones with an exponentially small error.

---

## 2. A canonical good set from the average plaquette potential

Let the normalized plaquette potential be
\[
\vartheta(g):=1-\tfrac1n\Re\mathrm{Tr}(g)\in[0,2],
\]
so that \(\Phi_\beta(g)=\beta\vartheta(g)\). Define the empirical (average) plaquette potential
\[
\overline\vartheta_{\Lambda_L}(U):=\frac{1}{|P|}\sum_{p\in P(\Lambda_L)}\vartheta\big(U_p(U)\big),
\qquad S_{\Lambda_L,\beta}(U)=\beta|P|\,\overline\vartheta_{\Lambda_L}(U).
\]
Fix a threshold \(\varepsilon\in(0,2)\) and define the good set
\[
\boxed{\quad K_{\Lambda_L}(\varepsilon):=\{U:\overline\vartheta_{\Lambda_L}(U)\le \varepsilon\}.\quad}
\]

---

## 3. Typicality: lower-bounding the partition function by a linkwise ball

Consider the linkwise ball event
\[
A_{\Lambda_L}(r):=\{U: U_b\in B_r^G(\mathbf 1)\ \forall b\in E(\Lambda_L)\}.
\]
Its volume is a direct product:
\(
\mathrm{vol}(A_{\Lambda_L}(r)) = \mathrm{vol}(B_r^G(\mathbf 1))^{|E|}
\).

On \(A_{\Lambda_L}(r)\), each plaquette holonomy is a product of 4 links/inverses; by subadditivity of distance under multiplication and inversion invariance,
\[
 d_G(U_p(U),\mathbf 1)\le m_\partial r\quad (m_\partial=4).
\]
If \(L_\vartheta:=\sup_G |\nabla\vartheta|\), a global Lipschitz bound gives
\(
\vartheta(g)\le L_\vartheta\,d_G(g,\mathbf 1)
\), hence on \(A_{\Lambda_L}(r)\),
\[
S_{\Lambda_L,\beta}(U)\le \beta L_\vartheta m_\partial r\,|P|.
\]
This yields an explicit partition-function lower bound
\[
Z_{\Lambda_L,\beta}\ge e^{-\beta L_\vartheta m_\partial r |P|}\,\mathrm{vol}(B_r^G(\mathbf 1))^{|E|}.
\]

Combining this with the trivial bound \(e^{-S}\le e^{-\beta\varepsilon|P|}\) on \(K(\varepsilon)^c\) gives
\[
\mu_{\Lambda_L,\beta}(K(\varepsilon)^c)
\le
\exp\Big(-\beta(\varepsilon-L_\vartheta m_\partial r)|P|+|E|\,\chi_G(r)\Big),
\qquad
\chi_G(r):=\log\frac{\mathrm{vol}(G)}{\mathrm{vol}(B_r^G(\mathbf 1))}.
\]
In \(d=4\), \(|E|/|P|=2/3\), so the exponent becomes a pure \(|P|\)-rate:
\[
\boxed{\quad
\mu_{\Lambda_L,\beta}(K(\varepsilon)^c)
\le
\exp\big(-c_{\mathrm{typ}}(\beta;\varepsilon,r)\,|P|\big),
\ \ c_{\mathrm{typ}}=\beta(\varepsilon-L_\vartheta m_\partial r)-\tfrac23\chi_G(r).
\quad}
\]

---

## 4. Reflection positivity for Wilson \(\Rightarrow\) OS Hilbert space

Reflection positivity (RP) is proved by a constructive Gram decomposition of each plaquette weight
\[
 w_\beta(g):=\exp\Big(\tfrac{\beta}{n}\Re\mathrm{Tr}(g)\Big),
\qquad e^{-S}\propto \prod_{p\in P} w_\beta(U_p).
\]
The key structural fact is the positive-definite kernel representation
\[
 w_\beta(g^{-1}h)=\sum_\alpha \overline{f_\alpha(g)}f_\alpha(h),
\]
obtained from a character/tensor-product expansion of \(w_\beta\).

For plaquettes straddling the reflection plane, one factors the plaquette holonomy into “half-plaquette” variables \(V_p^\pm\) living on opposite sides, and uses conjugation/inversion invariance to rewrite
\(
 w_\beta(U_p)=w_\beta((V_p^-)^{-1}V_p^+)
\). Plugging the Gram expansion and integrating out the positive-side variables yields a sum of squares, implying
\[
\boxed{\quad \mathbb E_{\Lambda_L,\beta}[(\theta F)F]\ge 0\quad\text{for all positive-time observables }F.\quad}
\]

This is the exact Osterwalder–Schrader (OS) positivity axiom needed for reconstruction.

---

## 5. OS reconstruction: time decay \(\Rightarrow\) Hamiltonian gap

Given RP, time translations, and mild algebraic closure, OS reconstruction produces:

- a Hilbert space \(\mathcal H_{\mathrm{OS}}\) (completion of positive-time observables modulo nulls),
- a positive self-adjoint contraction \(T\) implementing one-step Euclidean time translation,
- a self-adjoint Hamiltonian \(H\ge 0\) such that \(T=e^{-aH}\) (\(a\) the lattice spacing).

A clean spectral lemma then says: if a vector \(\psi\) satisfies discrete-time decay
\[
\langle\psi,e^{-naH}\psi\rangle\le C_\psi e^{-mna}\qquad (n\in\mathbb N_0),
\]
then the spectral measure of \(H\) for \(\psi\) has no support in \([0,m)\).

Consequently, if centered OS correlations satisfy
\[
|\mathrm{Cov}(\theta F,\tau_n F)|\le C(F)e^{-\eta n},
\]
then \(H\) has a spectral gap
\[
\boxed{\quad \mathrm{gap}(H)\ge \eta/a.\quad}
\]

---

## 6. Putting the pieces together (the big picture)

A typical endgame looks like this:

1. **Local coercivity:** on a good set \(K\), prove a pointwise curvature lower bound \(\mathrm{Ric}_\mu\succeq M\) where \(M\) is a massive Maxwell operator.
2. **HS + hinge:** use the Helffer–Sjöstrand identity and the matrix Brascamp–Lieb hinge to bound covariances by the Green kernel of \(M^{-1}\).
3. **Deterministic decay:** use Combes–Thomas or Davies to get exponential decay of \(M^{-1}\) in link distance.
4. **Typicality:** use the bound above to upgrade conditional decay on \(K\) to unconditional decay.
5. **OS:** use reflection positivity and OS reconstruction to convert Euclidean time decay into a spectral gap.

What’s striking is how “nonperturbative” this is: the analysis leans on geometry, positivity, and deterministic operator theory rather than diagrammatics.
