# q‑Racah / Doob / Gap Toy Pillar (Speculative but Structured)

This is a **toy model pillar**: it is not Yang–Mills, but it is a mathematically explicit laboratory for the “curvature → gap → mass scale” philosophy.

The advantage is brutal clarity: finite dimensional, exactly diagonalizable, and you can run huge parameter scans.

---

## 1. Core construction (Hamiltonian → Doob transform → Markov generator)

You build:

1. A symmetric tridiagonal “Hamiltonian” \(H(N,q;\alpha,\beta,\gamma,\delta)\) using q‑Racah coefficients.
2. Extract the (strictly positive) ground state \(\psi_0\).
3. Construct a Doob-transformed generator \(Q\) by:
\[
Q_{ij}=
\begin{cases}
- H_{ij}\,\dfrac{\psi_0(j)}{\psi_0(i)}, & i\ne j,\\[6pt]
-\sum_{k\ne i} Q_{ik}, & i=j.
\end{cases}
\]
4. Define the toy “mass gap” as:
\[
m = -\lambda_1(Q),
\]
the smallest nonzero spectral rate.

This produces a controllable family of Markov chains with tunable spectral gap.

---

## 2. “Safe region” evidence: flow scans

A parameter scan (“flow summary”) reports regimes labeled `good_monotone`, with gaps staying positive and monotone along the scan direction, e.g.:

- q-flow from \(q_0=0.8\) to \(q_1=0.99\) at \(\alpha=1.0\):  
  min gap \(\approx 0.015902\), max gap \(\approx 0.237211\), monotone decreasing = True.

A finite-size scaling scan reports (example at q=0.800):

- \(N=4\): gap \(\approx 0.237211\)
- \(N=6\): gap \(\approx 0.205060\)
- \(N=8\): gap \(\approx 0.160588\)
- \(N=10\): gap \(\approx 0.137868\)
- \(N=12\): gap \(\approx 0.136564\)

and classifies it as monotone decreasing in \(N\) over that range.

---

## 3. A cautionary note: complex-q experiments can break positivity

A separate toy demo with a complex \(q=e^{i\theta}\) prints eigenvalues that are negative (violating the intended “gap ≥ 0” convention).

This is actually useful: it tells you exactly what constraints define the physical “Markov-safe” region. For a Markov generator, you need:

- nonnegative off-diagonal rates,
- row sum zero,
- and spectrum \(\le 0\) (so the gap is extracted as \(-\lambda_1\)).

The scan infrastructure already treats “invalid points” as a first-class outcome.

---

## 4. Why this might matter (a bigger theory direction)

This toy pillar mirrors several structural aspects of the YM program, but in a regime where you can do exact linear algebra:

- Doob transforms mirror ground-state tilting / effective potentials.
- The spectral gap is an explicit “mass scale.”
- You can build transfer operators and study coarse-graining as a map on generators.

A plausible “bigger theory” direction is to use this toy as an **RG-prototyper**:

- propose coarse-graining maps on \(Q\),
- require they preserve Markov positivity and an invariant subspace,
- and test whether a gap survives coarse-graining in a controllable way.

It’s not YM, but it’s an honest lab where you can debug your conjectures.

---

## 5. Minimal code skeleton (as implemented in the project)

```python
def doob_transform(H, tol=1e-12):
    evals, evecs = np.linalg.eigh(H)
    idx = np.argsort(evals)
    psi0 = np.abs(np.real_if_close(evecs[:, idx[0]]))
    if psi0.min() < tol:
        return None, evals[idx], psi0, False
    psi0 /= psi0.sum()

    n = H.shape[0]
    Q = np.zeros_like(H)
    for i in range(n):
        for j in range(n):
            if i != j and H[i,j] != 0:
                Q[i,j] = -H[i,j] * psi0[j] / psi0[i]
        Q[i,i] = -Q[i,:].sum()
    return Q, evals[idx], psi0, True
```

---

## 6. What to do next

1. Enforce a strict “Markov validity” oracle (off-diagonal ≥ 0, row sums ≈ 0, gap ≥ 0).
2. Map the safe region in \((q,\alpha,N)\) with large sweeps.
3. Build and test a coarse-graining map that preserves the Doob structure and compare gaps.

