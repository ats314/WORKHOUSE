
# Wilson Hessian “Erosion” in the SU(3) Exponential Chart — What Actually Needs Proving (v5)

This note tries to pin down **exactly** what you need to control to turn the numerically observed
“convex core” phenomenon into a clean lemma of the form

\[
\lambda_{\min}\big(\nabla^2 S_{\text{tot}}(A)\big)\;\ge\; c_0 - C\,\beta\, r(A)^2,
\]

**in the same exponential-coordinate chart** used in the SU(3) scans.

It also explains why your current diagnostics are flirting with a competing asymptotic law
\(R(\beta)\sim \text{const}/\beta\): that happens precisely when a certain *mixed third derivative*
does **not** vanish.

---

## 1. Setup (one plaquette, exponential chart)

Let each link variable live in \(\mathfrak{su}(3)\) with your chosen normalization.
For a single oriented plaquette with four links, write

\[
U_1=e^{X_1},\quad U_2=e^{X_2},\quad U_3=e^{X_3},\quad U_4=e^{X_4},
\qquad X_i\in\mathfrak{su}(3),
\]
and the plaquette holonomy
\[
P(X):=U_1\,U_2\,U_3^{-1}\,U_4^{-1}.
\]

The (normalized) one-plaquette Wilson term is
\[
S_p(X) := 1 - \frac{1}{3}\Re\Tr P(X).
\]

The **full lattice** Wilson action is \(S_W=\sum_p S_p\).
The total effective action in exponential coordinates is
\[
S_{\text{tot}}(A)\;=\;S_{\text{Haar}}(A)\;+\;\beta\, S_W(A),
\]
where \(S_{\text{Haar}}\) is the coordinate Jacobian contribution from Haar measure.

We care about the smallest eigenvalue of the Hessian
\[
H(A)\;:=\;\nabla^2 S_{\text{tot}}(A).
\]

---

## 2. The “mass floor” from Haar and what must be bounded

Near the identity, the Haar-Jacobian action has the expansion
\[
S_{\text{Haar}}(A_b) = c_0 \|A_b\|^2 + O(\|A_b\|^4),
\]
so
\[
\nabla^2 S_{\text{Haar}}(0) = 2c_0\,I.
\]

For a theorem you need a **uniform lower bound** on \(\nabla^2 S_{\text{Haar}}(A)\) in a normal
neighborhood:
\[
\nabla^2 S_{\text{Haar}}(A)\;\succeq\; c_0\,I - c_{\text{H}}\, r(A)^2\,I
\quad\text{for }\;r(A)\le r_0,
\]
where \(r(A)\) is *your* chosen amplitude statistic (sup or RMS).

This part is “classical Lie theory + a remainder bound”: the missing work is a clean **operator-norm**
bound on the quartic remainder of \(\log\det\big(\sinh(\mathrm{ad}_X/2)/(\mathrm{ad}_X/2)\big)\).

---

## 3. Wilson Hessian at the origin: kernel/range split

At \(A=0\), the Wilson term has a highly degenerate Hessian (you observed this numerically):
- \(\nabla^2 S_p(0)\) has **rank 8**, with the positive eigenvalue plateau at \(2/3\),
- and **kernel dimension 24** in the 32-dimensional link-variable space for one plaquette.

Denote the orthogonal splitting at the origin:
\[
\mathbb{R}^{32} = K \oplus R,
\]
where \(K=\ker \nabla^2 S_p(0)\) and \(R\) is its orthogonal complement (“range directions”).

Let \(\lambda_{\text{pos}}\) be the *smallest* positive eigenvalue on \(R\); empirically
\(\lambda_{\text{pos}}=2/3\) for the normalized SU(3) plaquette at 0.

---

## 4. The Schur-complement mechanism: where the \(r^2\) law comes from

Write the Wilson Hessian in block form in this fixed \(K\oplus R\) splitting:
\[
\nabla^2 S_p(X)=
\begin{pmatrix}
H_{KK}(X) & H_{KR}(X)\\
H_{RK}(X) & H_{RR}(X)
\end{pmatrix}.
\]

For the total Hessian \(H=\nabla^2 S_{\text{Haar}}+\beta\nabla^2 S_W\),
the **minimal eigenvalue** is controlled by the Schur complement bound:

\[
\lambda_{\min}(H)\;\ge\;
\lambda_{\min}\!\Big(
H_{KK}^{\text{Haar}} + \beta H_{KK}^{W}
\;-\;
\beta^2\, H_{KR}^{W}\,(H_{RR}^{\text{Haar}}+\beta H_{RR}^{W})^{-1} H_{RK}^{W}
\Big).
\]

Since \(H_{RR}^{W}(0)\succeq \lambda_{\text{pos}} I\) and Haar contributes \(c_0 I\),
for sufficiently small \(r\) one has
\[
(H_{RR}^{\text{Haar}}+\beta H_{RR}^{W})^{-1}\;\preceq\;\frac{1}{\beta\lambda_{\text{pos}}}\,I,
\]
and therefore
\[
\boxed{
\lambda_{\min}(H)\;\gtrsim\;
c_0
\;+\;\beta\,\lambda_{\min}(H_{KK}^{W})
\;-\;
\frac{\beta}{\lambda_{\text{pos}}}\,\|H_{KR}^{W}\|_{\mathrm{op}}^2
\;-\;(\text{Haar remainder})
}.
\]

So the *scaling* of the erosion law is entirely controlled by how
\(H_{KK}^{W}(X)\) and \(H_{KR}^{W}(X)\) grow with amplitude \(r=\|X\|\).

---

## 5. What decides between \(r\) vs \(r^2\) erosion

Use a mean-value / Taylor remainder viewpoint:

\[
\nabla^2 S_p(X)-\nabla^2 S_p(0)
=
\int_0^1 D^3 S_p(tX)[X]\,dt,
\]
so generically
\[
\| \nabla^2 S_p(X)-\nabla^2 S_p(0)\|_{\mathrm{op}}
\;\le\;
\sup_{t\in[0,1]}\|D^3 S_p(tX)\|_{\mathrm{op}}\;\|X\|.
\]

### 5.1 The “bad” case: linear erosion and \(R(\beta)\sim 1/\beta\)

If the mixed tensor component \(D^3 S_p(0)\) has **any** nonzero part with two legs in \(K\),
then \(H_{KK}^W(X)\) can be \(O(r)\). In that case you get an erosion envelope of the form
\[
\lambda_{\min}(H)\;\gtrsim\; c_0 - D\,\beta\, r \quad (\text{up to constants}),
\]
and the convexity radius behaves like
\[
R(\beta)\;\lesssim\;\frac{c_0}{D\,\beta}.
\]

This is exactly the regime where your diagnostics based on
\[
D_{\mathrm{eff}}(\beta):=\frac{c_0}{\beta R(\beta)}
\]
start to look “flat”.

### 5.2 The “good” case: quadratic erosion and \(R(\beta)\sim 1/\sqrt{\beta}\)

If you can show the **structural cancellation**
\[
\boxed{
D^3 S_p(0)[k_1,k_2,\cdot]=0 \quad\text{for all }k_1,k_2\in K,
}
\]
then \(H_{KK}^W(X)\) cannot have an \(O(r)\) term. In that case
\[
H_{KK}^W(X)=O(r^2)
\quad\text{and}\quad
H_{KR}^W(X)=O(r),
\]
and the Schur bound forces a **pure \(r^2\)** erosion law:
\[
\lambda_{\min}(H)\;\gtrsim\;c_0 - C\,\beta\, r^2.
\]

This is the only scaling compatible with a convexity radius comparable to
typical weak-coupling fluctuations (\(\sim 1/\sqrt{\beta}\)).

---

## 6. The constant \(C\): what you actually have to compute or bound

In the “good” \(r^2\) scenario, a clean (conservative) choice is:

\[
C \;\ge\;
C_{KK} \;+\; \frac{C_{KR}^2}{\lambda_{\text{pos}}}\;+\; C_{\text{Haar}},
\]
where roughly:

- \(C_{KR}\) is a bound on \(\|H_{KR}^W(X)\|_{\mathrm{op}}/r\) in the ball,
- \(C_{KK}\) is a bound on \(\|H_{KK}^W(X)\|_{\mathrm{op}}/r^2\) in the ball,
- \(C_{\text{Haar}}\) bounds the *loss* from Haar remainder: \(H^{\text{Haar}}\succeq c_0 I - C_{\text{Haar}} r^2 I\).

In terms of raw Fréchet derivatives, one convenient “single-plaquette” sufficient set is:

\[
\sup_{\|X\|\le r_0}\|D^3 S_p(X)\|_{\mathrm{op}} \le M_3,
\qquad
\sup_{\|X\|\le r_0}\|D^4 S_p(X)\|_{\mathrm{op}} \le M_4,
\]
plus the cancellation \(D^3 S_p(0)[K,K,\cdot]=0\).
Then you can take, schematically,
\[
C_{KR}\sim M_3,\qquad
C_{KK}\sim M_4.
\]

**This is precisely where your “need the 4th-derivative tensor and the Haar remainder” comment lands.**

---

## 7. What is missing right now (short, brutal list)

To turn the numerical mechanism into a theorem with a realistic constant:

1. **Prove or disprove the key cancellation**
   \[
   D^3 S_p(0)[K,K,\cdot]=0.
   \]
   If false, the best uniform theorem in link-amplitude \(r\) will be \(c_0-D\beta r\), not \(c_0-C\beta r^2\).

2. **If cancellation holds**, compute (or upper bound tightly) the operator norm of the
   relevant **projected** 4th derivative:
   \[
   \| \Pi_K D^4 S_p(0)\|_{\mathrm{op}}
   \quad\text{and/or}\quad
   \sup_{\|X\|\le r_0}\|D^4 S_p(X)\|_{\mathrm{op}}.
   \]

3. **Haar remainder bound:** an explicit constant \(C_{\text{Haar}}\) such that
   \(\nabla^2 S_{\text{Haar}}(A)\succeq c_0 I - C_{\text{Haar}} r^2 I\) in the chart.

4. **Lattice bookkeeping:** pass from “one plaquette” to “full lattice” by tracking:
   - how many plaquettes touch a link (6 in 4D),
   - how operator norms add under overlaps,
   - and confirm constants don’t blow up with volume.

---

## 8. Practical interpretation

- If you want the program to “close” in the weak-coupling regime, you almost certainly need
  the \(r^2\) erosion law **in a physically meaningful amplitude**.
- If link-amplitude \(r=\|A\|_\infty\) forces a linear erosion constant \(D>0\),
  then the convex core shrinks like \(1/\beta\), and an “entrance” theorem becomes
  dramatically harder (typical fluctuations won’t fit inside unless you gauge-fix or redefine \(r\)).

So the game is: **identify the right \(r\)** (ideally gauge-covariant) for which the cancellation holds,
and then compute \(D^4\) and Haar remainder in that same metric.

---
