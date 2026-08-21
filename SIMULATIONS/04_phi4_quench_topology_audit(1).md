# 4D \(\phi^4\) Symmetry-Breaking Quench on \(64^4\) and a Topological Audit

## 1. Model and goal

A real scalar field \(\phi(x)\) with a symmetry-breaking potential
\[
V(\phi)=\frac{m^2}{2}\phi^2 + \frac{\lambda}{4}\phi^4
\]
with \(m^2<0\) has minima at \(\phi=\pm \sqrt{-m^2/\lambda}\).

A rapid quench/relaxation from near-zero initial conditions typically generates a network of domain walls/defects (Kibble–Zurek intuition), especially on a large periodic lattice.

---

## 2. Simulation method in the project

The code uses a Fourier-space preconditioning (“Fourier acceleration”) to stabilize and speed up relaxation.

At a high level:

1. Initialize \(\phi\) with small noise.
2. Iterate a relaxation update where the linear operator is handled in Fourier space and inverted approximately by a preconditioner \((p^2+1)^{-1}\).
3. Save a final snapshot to `higgs_vacuum_64_state.npz`.

This is closer to a *preconditioned gradient flow* than a full stochastic Langevin (unless noise is injected each step).

---

## 3. Reported topological audit

The project includes an audit step that loads the saved state and reports:

- `knot_count = 401322`
- `tension_ratio = 0.0643`
- `mean_energy = 36555.3`

These are presented as diagnostics of defect content and energy partition (the exact definitions of “knot” and “tension ratio” are encoded in the audit code).

---

## 4. Why this is potentially interesting

A stable high-defect-density configuration on a 4-torus can be used as:

1. A testbed for **defect topology detection** (wrapping vs contractible walls).
2. A starting point for studying **metastability** under smoothing/flow.
3. A bridge to the SU(2) “offender” story: rare configurations that frustrate drift inequalities may correspond to similar topological obstructions.

If the audit’s “knot” count is robust to algorithmic choices (grid resolution, thresholding, smoothing), it may point to a quantitative regime of defect percolation.

---

## 5. Next steps (to make this science instead of vibes)

1. **Define invariants carefully.**  
   Replace any heuristic knot/wall counter with:
   - excursion-set topology,
   - Betti numbers,
   - persistent homology (barcode stability under smoothing).
2. **Quench-rate scaling.**  
   Repeat at multiple step sizes / effective cooling rates and test scaling laws for defect density.
3. **Energy accounting.**  
   Track:
   - gradient energy,
   - potential energy,
   - wall energy proxy,
   and compare to analytic expectations for domain-wall tension.
4. **Flow experiment.**  
   Apply controlled smoothing (e.g., a few steps of Wilson/gradient flow) and measure whether:
   - knots annihilate quickly (UV artifact),
   - or persist (IR/topological).

---

## 6. Minimal code excerpt (conceptual)

```python
# conceptual skeleton

phi = small_random_field(L=64)

for t in range(steps):
    # compute nonlinear force in position space
    force_x = m2*phi + lamb*phi**3 - laplacian(phi)

    # precondition in Fourier space (Fourier acceleration)
    force_k = FFT(force_x)
    phi_k   = FFT(phi)
    phi_k  -= dt * force_k / (p2 + 1.0)
    phi     = IFFT(phi_k).real

save_npz("higgs_vacuum_64_state.npz", phi=phi)

# audit:
phi = load_npz(...)

knot_count = count_knots(phi)
tension_ratio = estimate_wall_tension(phi) / total_energy(phi)
```

(The project file contains the actual GPU/FFT implementation and the audit routines.)
