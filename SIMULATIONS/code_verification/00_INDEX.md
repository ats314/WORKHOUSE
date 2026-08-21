# CODE_VERIFICATION Index

This folder contains code that has been **actually executed**.

## Verified Scripts

| Script | What It Verifies | Date Run | Result |
|--------|------------------|----------|--------|
| `VSU_field_theory_verification.py` | μ increasing, Hamiltonian convex, force law unique, BTFR, EFE | 2026-01-13 | ✓ All 6 claims passed |
| `SPARC_antikernel_fit.py` | Anti-kernel Hankel method on SPARC | 2026-01-13 | ❌ FAILED |

---

## FAILED: Anti-Kernel (2026-01-13)

The anti-kernel method was tested and **DOES NOT WORK**:
- p90 χ²/dof = 63.7 (catastrophic tail)
- 5 galaxies with χ²/dof > 100
- Massive galaxies systematically fail
- **REMOVED FROM PROJECT**

---

**Rule:** If a script is not in this folder, it has not been verified.


