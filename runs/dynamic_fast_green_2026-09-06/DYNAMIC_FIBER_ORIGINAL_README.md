# Dynamic conditional-fiber continuation

This outputs-only package contains an analytic fixed-L proof and exact
finite controls. It does not change the main manuscript or result ledger.

- `DYNAMIC_FIBER_COVARIANCE_AND_CUBIC_ENERGY.md`: fixed spectral-contour
  proof of an exponentially decreasing time envelope times a spatial
  `(1+|x|)^-4` tail, exact periodization, Lie-cubic frequency denominators,
  bounded-mean rooted estimates and full-complement inverse domination.
- `check_dynamic_fiber.py`: independent finite Gaussian pairing and
  rational matrix controls.
- `DYNAMIC_FIBER_CONTROLS.json`: successful output, with proof/script hashes.

From the repository root, reproduce into a fresh output path:

```powershell
.\.venv\Scripts\python.exe -B outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/next_connected_cubic_fast_energy/dynamic_fiber/check_dynamic_fiber.py --output outputs/wilson_complete_band_20260905/next_scale/next_nonlinear/next_connected_cubic_fast_energy/dynamic_fiber/DYNAMIC_FIBER_CONTROLS_REPLAY.json
```

All three control groups passed. The exact dense four-site SU(2) example
has integrated cross energies `167059/1200500`, `2517/68600`, and
`-121/4000` in Wick degrees 1, 2 and 3. A negative cross energy is allowed;
the complete inverse-energy matrix is positive as a quadratic form.
The full-versus-fiber inverse witness gives `1/20 < 1/18` exactly.

The all-volume Fourier theorem is analytic and is not formalized by these
finite checks. The bound for retained-dependent forces requires the mean
cutoffs and local coefficient norms stated in the proof. Inverse form
domination transfers their synthesis bound to the actual Gaussian fast
complement, but transfers no entrywise absolute-row locality assertion.
