# Determinant Reduction Theorem & Stress Suite

## 1. The structural setup

A recurring pattern in the project is that a “naive expensive computation” (full determinant, full matrix assembly, etc.) can be replaced by a **case-split identity** that only touches the **active support**.

Here the object is a \(3\times 3\) determinant built from three column vectors:
\[
\det[x\,\,u\,\,v],
\]
with the key observation that many cases have the form
\[
v = u + w,\qquad \text{where } w \text{ has small support.}
\]

That small support implies the determinant can be computed with a small fixed stencil (a handful of multiplies and adds), rather than a full general-purpose determinant.

---

## 2. “Transposition reduction”: a worked identity

When exactly **one row is a fixed point** (call it row \(r\)), and the other two “active” rows are \(\{p,q\}\), the determinant collapses to a compact expression.

In the runbook, one explicit example was:

- fixed row \(r=2\)
- active rows \(\{1,3\}\)

Let \(w = v-u\). Then the reduced determinant is:
\[
\det_{\text{new}}
= x_2\,(u_1 w_3 - u_3 w_1)\;-\;u_2\,(x_1 w_3 - x_3 w_1).
\]

This is the cleanest “proof artifact” in the determinant family: it is a symbolic identity, used as executable code.

---

## 3. Computational proof: equality to machine precision

The runs show that this theorem-based reduction matches the old “full determinant” computation to roundoff.

A representative benchmark reports:

- max absolute error \(\approx 1.95\times 10^{-14}\) across a showcased test,
- and a speedup of \(\sim 6\times\) on that run (old \(\approx 0.0070\)s vs new \(\approx 0.0011\)s).

The larger stress suite reports **79,200 checks** with **0 accidental support mismatches**, and **39,600 transposition reduction checks**.

---

## 4. Stability and performance (GPU microbenchmark)

The “marathon” benchmark reports:

- old method: \(\approx 8.313\ \mu s\) per step  
- new method: \(\approx 1.071\ \mu s\) per step  
- speedup: \(\approx 7.76\times\)  
- final drift: \(\approx 3.52\times 10^{-9}\)

A separate 100,000-step stability test compares the old and new pipelines and reports:

- drift (old vs new) \(\approx 3.64\times 10^{-12}\)  
- maximum divergence \(\approx 3.09\times 10^{-11}\)

---

## 5. The diagnostic lesson

One run “failed” because it asserted exact zero and encountered:

\[
\det(I) \approx 2.66\times 10^{-15}.
\]

That is not an algebraic failure; it is a **tolerance policy failure**. The determinant suite makes the tolerance policy explicit and treats identity-level evidence correctly (zero-to-roundoff).

---

## 6. Minimal reference implementation (as code)

Below is a minimal excerpt version of the transposition reduction. (The project’s code includes additional case splits, stress harnesses, and permutation classification.)

```python
def det_reduced_transposition(x, u, w, r, p, q):
    # x,u,w are length-3 vectors; w = v-u
    # r fixed row; p,q active rows
    return x[r]*(u[p]*w[q] - u[q]*w[p]) - u[r]*(x[p]*w[q] - x[q]*w[p])

# example case: r=1 (0-index), p=0, q=2 corresponds to rows 1,3 active in 1-index notation
```

---

## 7. Why this matters (beyond one trick)

This “determinant reduction” is a template for how the rest of the project wants to work:

1. Find the invariant / identity (algebra or geometry).
2. Implement the identity as a branchless (or nearly branchless) kernel.
3. Prove it computationally with randomized + adversarial stress tests.
4. Measure speed and drift at scale (A100 microbench).
5. Codify the tolerance rules so “roundoff” never becomes “mystery physics.”

