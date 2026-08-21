# §8.2′ Blockwise averaged badness \(\mathcal B_\Lambda^\star\) and the good set \(K_\Lambda^\star(\varepsilon)\)
*(Drop-in section for Part 8; 1–2 pages max)*

## 8.2′.1 Block family and block averages

Fix an integer block scale \(\ell\ge 1\).  
Let \(\mathfrak B_\ell\) be a translation-covariant family of plaquette blocks in \(\Lambda\):
each \(B\in\mathfrak B_\ell\) is a set of plaquettes \(P(B)\subset P(\Lambda)\) such that:

1. \(|P(B)|\asymp \ell^d\) (uniformly in \(\Lambda\)),
2. each plaquette \(p\in P(\Lambda)\) belongs to at most \(N_\star\) blocks, where \(N_\star<\infty\) depends only on \(d\) and the block shape (not on \(\Lambda\)).

*(Example: take blocks indexed by \(x\in\Lambda\) as the translate of a fixed \(\ell\times\cdots\times\ell\) hypercube of plaquettes; then \(N_\star\) is a purely geometric overlap constant.)*

For \(U\in M_\Lambda\), recall \(\widetilde z_p(U):=\widetilde z(U_p(U))\in[0,2]\).
Define the **block badness** by
\[
\mathcal B_B(U)\ :=\ \frac{1}{|P(B)|}\sum_{p\in P(B)}\widetilde z_p(U),
\qquad B\in\mathfrak B_\ell.
\]

Define the **blockwise averaged badness** by averaging over blocks:
\[
\mathcal B_\Lambda^\star(U)\ :=\ \frac{1}{|\mathfrak B_\ell|}\sum_{B\in\mathfrak B_\ell}\mathcal B_B(U).
\tag{8.2′.1}
\]

This is a “mesoscopically smoothed” version of the global averaged badness \(\mathcal B_\Lambda\).  
By bounded overlap,
\[
\mathcal B_\Lambda^\star(U)\ \le\ N_\star\,\mathcal B_\Lambda(U).
\tag{8.2′.2}
\]
In particular, in the intended implementation one can choose the block family so that \(N_\star\le 2\), yielding the frequently used inequality \(\mathcal B_\Lambda^\star\le 2\mathcal B_\Lambda\).

---

## 8.2′.2 The blockwise good set

For \(\varepsilon>0\) define
\[
K_\Lambda^\star(\varepsilon)\ :=\ \Big\{U\in M_\Lambda:\ \mathcal B_\Lambda^\star(U)\le \varepsilon\Big\}.
\tag{8.2′.3}
\]

This set is designed to play the role of the localization event \(K\) in Part 10:  
- **HS/hinge control** will be proved on \(K_\Lambda^\star(\varepsilon)\).  
- **Typicality** will be proved by LSI concentration for \(\mathcal B_\Lambda^\star\), using the Lipschitz lemma below.

---

## 8.2′.3 Lipschitz scaling (volume gain)

### Lemma 8.2′ (Lipschitz constant of \(\mathcal B_\Lambda^\star\))

Assume the global gradient domination bound for the proxy \(\widetilde z\):
\[
|\nabla_G\widetilde z(g)|^2\ \le\ C_\nabla\,\widetilde z(g),
\qquad \forall g\in G,
\tag{8.2′.4}
\]
and recall \(0\le \widetilde z\le 2\).

Then there exists \(C_\star<\infty\), depending only on \(G\), \(d\), and the block family \(\mathfrak B_\ell\) (through the overlap constant \(N_\star\) and block size \(\ell\)), such that
\[
\sup_{U\in M_\Lambda}\ |\nabla \mathcal B_\Lambda^\star(U)|_{g_\Lambda}^2
\ \le\
\frac{C_\star}{|P(\Lambda)|}.
\tag{8.2′.5}
\]

Equivalently, \(\mathcal B_\Lambda^\star\) is \(L_\star\)-Lipschitz with
\[
L_\star\ \le\ C_\star^{1/2}\,|P(\Lambda)|^{-1/2}.
\tag{8.2′.6}
\]

#### Proof (sketch, parallel to Lemma 8.11 / Remark 8.12 in Part 8)

Write
\[
\mathcal B_\Lambda^\star(U)
=\frac{1}{|\mathfrak B_\ell|}\sum_{B\in\mathfrak B_\ell}\frac{1}{|P(B)|}\sum_{p\in P(B)}\widetilde z_p(U)
=\sum_{p\in P(\Lambda)} w_p\,\widetilde z_p(U),
\]
where the weights satisfy \(w_p\ge 0\) and
\[
w_p\ \le\ \frac{N_\star}{|\mathfrak B_\ell|\,|P(B)|}\ \asymp\ \frac{1}{|P(\Lambda)|}.
\]

Differentiate:
\[
\nabla \mathcal B_\Lambda^\star
=\sum_{p} w_p\,\nabla \widetilde z_p.
\]

Using Cauchy–Schwarz,
\[
|\nabla \mathcal B_\Lambda^\star|^2
\le \Big(\sum_p w_p\Big)\Big(\sum_p w_p\,|\nabla \widetilde z_p|^2\Big)
=\sum_p w_p\,|\nabla \widetilde z_p|^2.
\]

Insert the domination (8.2′.4) and \(\widetilde z_p\le 2\):
\[
|\nabla \mathcal B_\Lambda^\star|^2
\le \sum_p w_p\,C_\nabla\,\widetilde z_p
\le 2C_\nabla \sum_p w_p
=2C_\nabla\,\max_p w_p\,|P(\Lambda)|
\ \lesssim\ \frac{1}{|P(\Lambda)|}.
\]

All constants are uniform in \(\Lambda\) because the overlap constant and block geometry are uniform. \(\square\)

---

## 8.2′.4 Interface for Part 10

Part 10 should now set the localization event explicitly as
\[
K\ :=\ K_\Lambda^\star(\varepsilon),
\]
and record the two obligations:

1. **HS/hinge control on \(K_\Lambda^\star(\varepsilon)\)** (this reattaches Parts 6+9).
2. **Typicality of \(K_\Lambda^\star(\varepsilon)\)**:
   \[
   \mu_\Lambda\big((K_\Lambda^\star(\varepsilon))^c\big)\ \le\ e^{-c\,|P(\Lambda)|},
   \]
   to be proved from global LSI concentration for \(\mathcal B_\Lambda^\star\), using the Lipschitz scaling (8.2′.6).

*(The concentration step is the cleanest place to spend the blockwise LSI / PULSE effort.)*
