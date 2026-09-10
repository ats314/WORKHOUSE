# M10 conditional transport, 10 September 2026

The [source](sources/w6-conditional-transport-obstruction.md) and its
[independent analytic review](independent_review.md) establish an actual
existential obstruction to M10 for the unspecified Q8 transport class. The
explicit synchronized repair is admissible and tangent to the conditional
minimum graph; its complete uniform M10 estimate remains open.

The maintained [derivation](../../docs/derivations/w6-conditional-transport-obstruction.md)
has the same source bytes. The square geometry, quantum exponential moment,
physical gap and source-potential bound are prior project inputs. The local
one-well comparison theorem cited in S3 is an external analytic input.

Reproduce the finite controls from the repository root:

```text
python scripts/check_m10_transport.py --output runs/m10_conditional_transport_2026-09-10/exact_checks.json
```

[exact_checks.json](exact_checks.json) records 20/20 exact controls. These check
Haar divergence, metric calibration, constrained geometry, Gaussian Hessian,
normal drift, synchronized velocities and score normalization. They do not
prove the concentration theorem, a coupling-differentiated WKB expansion or
the full M10 inequality. The optional g^-4 score asymptotic in S4 remains
conditional and is not an actual-model result registered by this run.

`source_manifest.json` records the origin and hash of the frozen proof and
review; `SHA256SUMS` pins those records and the exact check output. Repository
validation is recorded separately in `validation.md` after graph regeneration.
