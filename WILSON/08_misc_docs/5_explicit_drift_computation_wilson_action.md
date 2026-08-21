# Explicit Strip-Drift Computation for \(B=\mathcal B_\Lambda\) (Wilson Action, SU(2))

This module does two things:

1. **Compute \(L\mathcal B_\Lambda\) explicitly** for the Wilson action, in the project’s normalization.
2. **Isolate the exact sufficient inequality** on the drift pairing
   \(\langle\nabla S_W,\nabla\mathcal B_\Lambda\rangle\)
   that guarantees a **uniform inward strip drift**
   \[
   L\mathcal B_\Lambda \le -\rho <0
   \quad\text{on}\quad
   \Sigma:=\{\varepsilon<\mathcal B_\Lambda<\varepsilon+\delta\},
   \]
   with \(\rho\) independent of \(|\Lambda|\).

Everything is deterministic and volume-explicit; any additional geometric input is stated as a hypothesis.

---

## 0. Definitions

Recall (from `NOTATION_AND_CONSTANTS.md`) the disorder functional
\[
\mathcal B_\Lambda(U)
=
\frac{1}{|P(\Lambda)|}
\sum_{p\in P(\Lambda)}
\widetilde z(U_p(U)),
\qquad
\widetilde z(g):=1-\tfrac12\mathrm{ReTr}(g).
\]

Wilson action:
\[
S_W(U)=\beta \sum_{p\in P(\Lambda)}\widetilde z(U_p(U)).
\tag{0.1}
\]

Generator:
\[
L=\Delta-\langle\nabla S_W,\nabla\cdot\rangle.
\tag{0.2}
\]

---

## 1. Exact identity: \(S_W = \beta |P|\mathcal B_\Lambda\)

From the definitions,
\[
S_W(U)
=
\beta \sum_{p}\widetilde z(U_p(U))
=
\beta |P(\Lambda)|\,\mathcal B_\Lambda(U).
\tag{1.1}
\]

Differentiate on the configuration manifold \(M_\Lambda = G^{E(\Lambda)}\):
\[
\nabla S_W
=
\beta |P(\Lambda)|\,\nabla \mathcal B_\Lambda.
\tag{1.2}
\]
This is **exact**, with no approximation.

Taking the \(g_\Lambda\)-inner product with \(\nabla\mathcal B_\Lambda\) gives the exact drift pairing
\[
\boxed{
\langle\nabla S_W,\nabla\mathcal B_\Lambda\rangle
=
\beta |P(\Lambda)|\,|\nabla\mathcal B_\Lambda|^2.
}
\tag{1.3}
\]

This is the structural identity you want: the drift alignment is automatic because \(S_W\) is *exactly proportional* to \(\mathcal B_\Lambda\).

---

## 2. Compute \(L\mathcal B_\Lambda\)

By definition,
\[
L\mathcal B_\Lambda
=
\Delta\mathcal B_\Lambda
-
\langle\nabla S_W,\nabla\mathcal B_\Lambda\rangle.
\tag{2.1}
\]
Insert (1.3):
\[
\boxed{
L\mathcal B_\Lambda
=
\Delta\mathcal B_\Lambda
-
\beta |P(\Lambda)|\,|\nabla\mathcal B_\Lambda|^2.
}
\tag{2.2}
\]

So the strip drift problem reduces to:
- an **upper bound** on \(\Delta\mathcal B_\Lambda\),
- a **lower bound** on \(|P||\nabla\mathcal B_\Lambda|^2\) in the strip.

---

## 3. Uniform bound on \(\Delta\mathcal B_\Lambda\) (volume-independent)

Write the product Laplacian as \(\Delta=\sum_{\ell\in E(\Lambda)}\Delta_\ell\), where \(\Delta_\ell\) acts in the \(\ell\)-coordinate.
By linearity,
\[
\Delta\mathcal B_\Lambda
=
\frac{1}{|P|}
\sum_{p\in P}\Delta\big(\widetilde z(U_p)\big)
=
\frac{1}{|P|}
\sum_{p\in P}
\sum_{\ell\in\partial p}\Delta_\ell\big(\widetilde z(U_p)\big).
\tag{3.1}
\]

Fix a plaquette \(p\) and a link \(\ell\in\partial p\).
As a function of \(U_\ell\), the holonomy \(U_p\) is obtained from \(U_\ell\) by left/right multiplication by a fixed group element
(the product of the other three links), possibly followed by inversion \(U_\ell\mapsto U_\ell^{-1}\).
Because the metric is bi-invariant, left/right translations and inversion are isometries; hence they commute with the Laplacian.
Therefore,
\[
\Delta_\ell\big(\widetilde z(U_p)\big)
=
(\Delta_G\widetilde z)(U_p),
\]
so
\[
\big|\Delta_\ell\big(\widetilde z(U_p)\big)\big|
\le
C_\Delta
:=
\sup_{g\in G}|\Delta_G\widetilde z(g)|.
\tag{3.2}
\]
This is exactly the constant \(C_\Delta\) from the notation file.

Since each plaquette has 4 boundary links,
\[
|\Delta\mathcal B_\Lambda(U)|
\le
\frac{1}{|P|}
\sum_{p\in P}\sum_{\ell\in\partial p} C_\Delta
=
\frac{1}{|P|}\,|P|\cdot 4C_\Delta
=
4C_\Delta.
\tag{3.3}
\]

So we have the **uniform, volume-independent** bound
\[
\boxed{
\|\Delta\mathcal B_\Lambda\|_{L^\infty(M_\Lambda)}\ \le\ 4C_\Delta.
}
\tag{3.4}
\]

---

## 4. The exact sufficient inner-product bound for a uniform strip drift

Fix a strip
\[
\Sigma:=\{\varepsilon<\mathcal B_\Lambda<\varepsilon+\delta\}.
\]

From (2.2) and (3.4),
\[
L\mathcal B_\Lambda
\le
4C_\Delta
-
\beta |P|\,|\nabla\mathcal B_\Lambda|^2.
\tag{4.1}
\]

Therefore the following implication is immediate:

### Proposition 4.1 (Sufficient drift pairing condition)

If there exists \(\rho>0\) such that on \(\Sigma\),
\[
\boxed{
\langle\nabla S_W,\nabla\mathcal B_\Lambda\rangle
\ \ge\
4C_\Delta + \rho,
}
\tag{4.2}
\]
then on \(\Sigma\),
\[
\boxed{
L\mathcal B_\Lambda \ \le\ -\rho.
}
\tag{4.3}
\]

#### Proof
By (2.1),
\(L\mathcal B_\Lambda = \Delta\mathcal B_\Lambda - \langle\nabla S_W,\nabla\mathcal B_\Lambda\rangle\).
Using \(\Delta\mathcal B_\Lambda\le 4C_\Delta\) and (4.2) yields (4.3). ∎

Using the identity (1.3), (4.2) is equivalent to the **gradient lower bound**
\[
\boxed{
|P(\Lambda)|\,|\nabla\mathcal B_\Lambda|^2
\ \ge\
\frac{4C_\Delta+\rho}{\beta}
\qquad\text{on }\Sigma.
}
\tag{4.4}
\]

Equivalently, in terms of the action gradient,
\[
|\nabla S_W|^2
=
\beta^2|P|^2|\nabla\mathcal B_\Lambda|^2
\ \ge\
\beta|P|\,(4C_\Delta+\rho).
\tag{4.5}
\]

So the strip drift bound is completely reduced to a single explicit coercivity inequality.

---

## 5. How to get \(|P||\nabla\mathcal B_\Lambda|^2\gtrsim 1\) on the strip (what remains)

This is where the **local SU(2) transversality/cancellation lemma** enters.

### 5.1 Incidence combinatorics (deterministic)

Assume \(\mathcal B_\Lambda(U)\ge \varepsilon\). Let
\[
R := \Big\{p\in P:\ \widetilde z(U_p)\ge \varepsilon/2\Big\}.
\]
Since \(0\le \widetilde z\le 2\),
\[
\varepsilon|P|
\le
\sum_{p\in P}\widetilde z(U_p)
\le
(\varepsilon/2)(|P|-|R|)+2|R|,
\]
which implies
\[
|R|
\ \ge\
\frac{\varepsilon}{4-\varepsilon}\,|P|.
\tag{5.1}
\]

Each plaquette has 4 links, and each link is incident to at most \(\nu=2(d-1)=6\) plaquettes in \(d=4\).
Therefore the set of links incident to at least one plaquette in \(R\) has cardinality at least
\[
N_{\mathrm{rough\,links}}
\ \ge\
\frac{4|R|}{\nu}
\ \ge\
\frac{4}{\nu}\cdot\frac{\varepsilon}{4-\varepsilon}\,|P|.
\tag{5.2}
\]

So, purely combinatorially, **a positive fraction of links touch a rough plaquette** whenever \(\mathcal B_\Lambda\ge\varepsilon\).

### 5.2 Local transversality input (what you need)

For each link \(\ell\), define the local link force \(F_\ell(U):=\nabla_\ell S_W(U)\in\mathfrak{su}(2)\).
Because \(S_W=\beta|P|\mathcal B_\Lambda\), we also have per-link
\[
F_\ell(U)
=
\beta|P|\;\nabla_\ell \mathcal B_\Lambda(U).
\tag{5.3}
\]

A sufficient local input is:

> **(T\(_\tau\)) Local SU(2) transversality away from Cartan alignment.**  
> Fix \(\varepsilon\in(0,1]\) and \(\tau>0\).  
> There exists \(c_{\mathrm{loc}}(\varepsilon,\beta,\tau)>0\) such that for every link \(\ell\),  
> if at least one plaquette incident to \(\ell\) satisfies \(\widetilde z(U_p)\ge \varepsilon/2\) and
> the local configuration around \(\ell\) is at distance \(\ge\tau\) from the aligned Cartan locus,
> then
> \[
> |F_\ell(U)|\ \ge\ c_{\mathrm{loc}}(\varepsilon,\beta,\tau).
> \tag{5.4}
> \]
> (This is exactly the content of the “Local Cancellation Lemma” module.)

Assuming (T\(_\tau\)) holds for all rough links (or for a uniform fraction of them), we obtain:
\[
|\nabla\mathcal B_\Lambda|^2
=
\sum_{\ell\in E}|\nabla_\ell\mathcal B_\Lambda|^2
=
\frac{1}{\beta^2|P|^2}\sum_{\ell\in E}|F_\ell|^2
\ \ge\
\frac{N_{\mathrm{rough\,links}}}{\beta^2|P|^2}\,c_{\mathrm{loc}}(\varepsilon,\beta,\tau)^2.
\tag{5.5}
\]

Insert the lower bound (5.2) for \(N_{\mathrm{rough\,links}}\sim c(\varepsilon)|P|\) to get
\[
|P|\,|\nabla\mathcal B_\Lambda|^2
\ \ge\
\frac{c(\varepsilon)}{\beta^2}\,c_{\mathrm{loc}}(\varepsilon,\beta,\tau)^2
\ =:\ c_{\mathrm{strip}}(\varepsilon,\beta,\tau)\ >0.
\tag{5.6}
\]

Since \(c_{\mathrm{loc}}(\varepsilon,\beta,\tau)\) is proportional to \(\beta\sqrt{\varepsilon}\) (in the small-angle strip),
the \(\beta^2\) cancels and \(c_{\mathrm{strip}}\) is of order \(\varepsilon\) times a geometric factor.

### 5.3 Conclusion: explicit criterion for \(\rho>0\)

Combining (4.1) with (5.6),
\[
L\mathcal B_\Lambda
\le
4C_\Delta
-
\beta\,c_{\mathrm{strip}}(\varepsilon,\beta,\tau).
\tag{5.7}
\]
Thus if
\[
\beta\,c_{\mathrm{strip}}(\varepsilon,\beta,\tau)\ >\ 4C_\Delta,
\tag{5.8}
\]
then the strip drift holds with
\[
\rho := \beta\,c_{\mathrm{strip}}(\varepsilon,\beta,\tau)-4C_\Delta\ >0.
\tag{5.9}
\]

This is exactly the quantitative condition you need to feed into the smooth gluing lemma.

---

## 6. Summary (the “one inequality” you are really asking for)

To get a uniform strip drift \(L\mathcal B_\Lambda\le -\rho\) it is enough to prove the single coercivity bound
\[
\boxed{
|P(\Lambda)|\,|\nabla\mathcal B_\Lambda(U)|^2
\ \ge\
c_{\mathrm{strip}}
\ > 0
\quad\text{for all }U\text{ with }\varepsilon<\mathcal B_\Lambda(U)<\varepsilon+\delta.
}
\]
Then automatically (by (2.2) and (3.4)) \(L\mathcal B_\Lambda\le -( \beta c_{\mathrm{strip}}-4C_\Delta)\).

The entire remaining analytic work is therefore concentrated into:
- proving a **local SU(2) transversality** lemma that rules out systematic cancellation of plaquette forces at a link,
- verifying that such transversality holds uniformly on the strip (or is enforced by the definition of the bad region).

