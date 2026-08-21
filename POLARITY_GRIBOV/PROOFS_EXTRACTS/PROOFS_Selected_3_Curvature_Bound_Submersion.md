# Selected Proof 3: Curvature of Gauge-Orbit Space from Submersion Geometry (and why it scales like \(g^2\))

**Source backbone:** the curvature-bound discussion and comparisons in `Proof_Comparison.md` and `LLM_Proof_Comparison_2.md`.  
The original “direct” curvature bound draft in the project is explicitly flagged as non-rigorous; this document extracts the *rigorous core strategy* and states it cleanly as a theorem-with-assumptions.

---

## 1. Goal

Let \(\mathcal{A}\) be the space of connections on a 4-manifold \(M\) with compact simple gauge group \(G=SU(N)\), and \(\mathcal{G}\) the gauge group acting isometrically on \(\mathcal{A}\) with respect to the \(L^2\) metric.

Let \(\mathcal{M}=\mathcal{A}/\mathcal{G}\) be the orbit space. On the regular stratum (irreducible connections), \(\pi:\mathcal{A}_{\mathrm{reg}}\to\mathcal{M}_{\mathrm{reg}}\) is (formally, and in Sobolev completions) a principal bundle and a **Riemannian submersion**.

We want a **coupling-dependent bound** on sectional curvature of \(\mathcal{M}_{\mathrm{reg}}\):
\[
\boxed{
|K_{\mathcal{M}}(X,Y)| \le C_0\, g^2
\quad\text{for orthonormal horizontal }X,Y.
}
\]

---

## 2. O’Neill’s formula reduces curvature to a Lie-bracket bound

For a Riemannian submersion \(\pi:(E,g_E)\to(B,g_B)\), O’Neill’s formula states that for horizontal unit vectors \(X,Y\),
\[
K_B(d\pi X, d\pi Y)
=
K_E(X,Y) + \frac{3}{4}\|[X,Y]_V\|^2.
\]
In our case \(E=\mathcal{A}\) is an affine Hilbert space with the flat \(L^2\) metric, hence \(K_E\equiv 0\). Therefore,
\[
\boxed{
K_{\mathcal{M}}(X,Y) = \frac{3}{4}\,\|[X,Y]_V\|^2.
}
\]
So the curvature bound reduces to bounding the **vertical component** of the Lie bracket of horizontal vector fields.

This is the point at which many physics derivations write something like \([X,Y]_V = gF(X,Y)\). The project correctly flags that as shorthand, not a proof. The rigorous route is: **compute \([X,Y]_V\) through the derivative of the vertical projection operator.**

---

## 3. Horizontal/vertical projections and the Green operator

Let \(d_A\) denote the covariant derivative at a connection \(A\). Then

- the vertical subspace is \(V_A=\mathrm{Im}(d_A)\),
- a natural horizontal complement is \(H_A=\ker(d_A^*)\) (Coulomb / background gauge).

On the irreducible stratum, \(d_A^*d_A\) has trivial kernel on Lie-algebra valued scalars (mod constants/center), and one has a well-defined Green operator
\[
G_A := (d_A^*d_A)^{-1}
\]
on the appropriate orthogonal complement.

The **vertical projection** is then
\[
\boxed{
P_V(A) = d_A\,G_A\,d_A^*,
}
\qquad
P_H(A)=I-P_V(A).
\]
This formula is central because it makes the dependence of “being horizontal” on \(A\) explicit.

---

## 4. The vertical bracket as a projection-derivative term

Let \(X,Y\) be vector fields on \(\mathcal{A}_{\mathrm{reg}}\) such that \(X(A),Y(A)\in H_A\) for all \(A\) (i.e., they are **horizontal**).

Even if \(X,Y\) are pointwise horizontal, their bracket need not be: horizontality is defined by an \(A\)-dependent projection. One can show (in a local chart; rigorously in Sobolev completions) that
\[
\boxed{
[X,Y]_V(A)
=
\big(DP_V(A)[X(A)]\big)\,Y(A)
-
\big(DP_V(A)[Y(A)]\big)\,X(A),
}
\]
where \(DP_V(A)[\cdot]\) denotes the Fréchet derivative of the operator \(P_V\) with respect to \(A\).

Thus
\[
\|[X,Y]_V(A)\|
\le
2\,\|DP_V(A)\|_{\mathrm{op}}\;\|X(A)\|\;\|Y(A)\|.
\]
For orthonormal \(X,Y\), this becomes
\[
\|[X,Y]_V(A)\| \le 2\,\|DP_V(A)\|_{\mathrm{op}}.
\]
Therefore, by O’Neill,
\[
|K_{\mathcal{M}}(X,Y)|
\le
3\,\|DP_V(A)\|_{\mathrm{op}}^2.
\]

So the curvature bound is reduced to a single analytic problem:

> **Uniformly bound \(\|DP_V(A)\|_{\mathrm{op}}\) on the region of configuration space of interest.**

---

## 5. Bounding \(DP_V\) using elliptic estimates

Differentiate the identity \(P_V(A)=d_A G_A d_A^*\):
\[
DP_V(A)[\dot A]
=
(Dd_A[\dot A])\,G_A\,d_A^*
+
d_A\,(DG_A[\dot A])\,d_A^*
+
d_A\,G_A\,(Dd_A^*[\dot A]).
\]
Two key facts:

1. \(Dd_A[\dot A]\) and \(Dd_A^*[\dot A]\) are **zeroth-order** operators (they involve commutators with \(\dot A\)). Hence they are bounded by \(\|\dot A\|\) times a group-dependent constant on suitable Sobolev spaces.

2. \(DG_A[\dot A]\) is controlled by the derivative-of-inverse formula. Writing \(L_A:=d_A^*d_A\), we have
\[
DG_A[\dot A] = -G_A\,(DL_A[\dot A])\,G_A.
\]
Thus any bound on \(\|G_A\|_{\mathrm{op}}\) plus a bound on \(\|DL_A[\dot A]\|_{\mathrm{op}}\) yields a bound on \(\|DG_A[\dot A]\|_{\mathrm{op}}\).

### 5.1 The analytic assumption (the real work)

To close the estimate one assumes (and in many geometric analysis settings can prove) that on a chosen regular region \(\Omega\subset \mathcal{A}_{\mathrm{reg}}\),
\[
\boxed{
\sup_{A\in\Omega}\|G_A\|_{\mathrm{op}} \le C_G < \infty,
\qquad
\sup_{A\in\Omega}\|DL_A\|_{\mathrm{op}} \le C_L < \infty.
}
\]
Heuristically, this is “uniform invertibility and regularity” of the Faddeev–Popov operator on the region \(\Omega\). Tools that enter here include elliptic regularity and small-curvature gauge results (Uhlenbeck-type theorems), together with a restriction away from reducible connections (where invertibility fails).

Under these bounds, \(DP_V\) is uniformly bounded on \(\Omega\):
\[
\sup_{A\in\Omega}\|DP_V(A)\|_{\mathrm{op}} \le C_P(C_G,C_L).
\]

---

## 6. The curvature bound at bare coupling, and metric scaling to \(g\)

With the uniform bound on \(DP_V\),
\[
|K_{\mathcal{M}}(X,Y)| \le 3C_P^2
\qquad\text{(bare-coupling metric).}
\]

To restore the gauge coupling, one uses **metric scaling**.

A standard normalization choice in physics is that the physical \(L^2\) metric on \(\mathcal{A}\) scales like
\[
g_{\mathrm{phys}} = \frac{1}{g^2}\, g_{\mathrm{bare}}.
\]
If a metric is scaled by \(\lambda\), sectional curvature scales by \(1/\lambda\). Hence
\[
K_{\mathrm{phys}} = g^2\, K_{\mathrm{bare}}.
\]
Therefore, on the same region \(\Omega\),
\[
\boxed{
|K_{\mathcal{M}}^{\mathrm{phys}}(X,Y)|
\le
C_0\,g^2,
\qquad C_0 := 3C_P^2.
}
\]

---

## 7. Why this is a “theory seed,” not just a lemma

This strategy is not specific to Yang–Mills. It is a **general theorem schema**:

> In any quotient Riemannian geometry \(E\to B=E/G\) where  
> (i) the total space \(E\) is flat (or has controlled curvature), and  
> (ii) the vertical projection \(P_V\) is given by an inverse elliptic operator,  
> then curvature of the base is controlled by the operator norm of \(DP_V\).

This links global geometry (curvature of orbit spaces) to microlocal analysis (bounds on Green operators). That bridge is exactly what the PBH flow needs, and it may have legs well beyond this particular mass-gap program.

---

## References within the project

- `Proof_Comparison.md`  
- `LLM_Proof_Comparison_2.md`
