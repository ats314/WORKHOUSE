# SU(3) physical string tension through O(y⁶) — campaign intake (2026-06-14)

> **⚠ NORMALIZATION SUPERSEDED (later same day, 2026-06-14).** Alex's consolidation pass
> (`../su3_o5_consolidated_y6/`, with `NOTE_SU3_canonical_archive_matrix.md`) declares the **(−1/4)ⁿ
> conversion below SUPERSEDED** — it belongs to a mixed-variable normalization and must NOT be
> combined with the glueball coefficients. **Canonical bridge: σ(u)=½·W(2u)** (u=β_lat/6), giving
> `σ(u)=2/3 − (22/153)u² − (61/408)u³ − (737327120374220449/7250590288602460800)u⁴ + O(u⁵)` and the
> corrected ratio m/√σ = √6·Σcₙuⁿ with **c=[4/3, 1/2, 11/68, −7559/499392, …]** (note c₂=11/68, NOT the
> 11/408 implied below). Also: **m₅ is now ASSIGNED = q₅** (the gap noted below is resolved); m₆ still open.
> The σ_n^reduced rationals and the KPS n=0..4 agreement below remain correct as *reduced* quantities;
> only the (−1/4)ⁿ→physical step and the ratio are corrected. Read `../su3_o5_consolidated_y6/README.md`
> as canonical for normalization and the ratio.

**What this is.** The SU(3) Hamiltonian-lattice string tension in the strong-coupling
expansion variable \(y=\beta_{\rm lat}/6=1/g^4\), computed by exact unit-vertex reduced
contractions and converted to physical normalization. A **new direction** in the one-plaquette
strong-coupling program (shares the real-space SOS / walled-Brauer toolchain). Deposited from
the 2026-06-14 ZIP-ARCHIVES drop after independent cold verification. **Release V2 corrects the
normalization** of the earlier O(y⁴) package (see `GLUEBALL_STRING_NORMALIZATION_CORRECTION_V2`).

## The result

The paper Hamiltonian's vertex is \(-y(\chi+\bar\chi)/4\), so the physical coefficients are
\(\sigma_n=(-1/4)^n\,\sigma_n^{\rm reduced}\). Exact reduced coefficients (cold-run):

| n | \(\sigma_n^{\rm reduced}\) |
|---|---|
| 0 | 2/3 |
| 1 | 0 |
| 2 | −22/153 |
| 3 | 61/408 |
| 4 | −737327120374220449/7250590288602460800 |

The **project contraction agrees with the Kogut–Pearson–Shigemitsu (KPS) table exactly at
n = 0,1,2,3,4** — an external literature cross-check (n=2: −11/1224; n=3: −61/26112; n=4 matches the
full rational). The KPS table supplies the denominator coefficients at orders 5 and 6.
**No value is assigned to the unknown glueball-mass coefficients \(m_5, m_6\)** (honest gap; the O5/O6
content is denominators only).

Corrected physical ratio coefficients through O(y⁴):
`[4/3, 1/2, 11/408, -850411/3995136, -2649605075224534084759/1856151113882229964800]`.

## Verification done this session (grounds: T1 machine-gated, with literature cross-check)

`bash ENGINE_STRING_reproduce.sh` cold (Python 3.10, sympy 1.14.0), no cache — full pipeline
(support scan → canonicalize → local coeffs → σ₄ → physical verify → manifest):

```
ALL PHYSICAL STRING-TENSION V2 GATES PASS
ALL CLEAN REPRODUCTION STAGES PASS   (exit 0)
```

Gates include: O(y²),O(y³) length-independence; O(y³) charge-conjugate equality; exact σ₂,σ₃,σ₄;
candidate/nonzero-pair extensivity; and **project-contraction == KPS at n=0..4**. The cold-run physical
verify log is `RUN_STRING_physical_verify_coldrun.log`.

**Scope honesty.** T1 (machine-gated, cold-reproduced) with an external check against the published
KPS strong-coupling table through O(y⁴). The O5/O6 layer is denominators-from-KPS only; \(m_5,m_6\)
unassigned. Not T2/T3. Not promoted to "established."

## σ-convention reconciliation + native-from-source (later 2026-06-14) — `AUDIT_STRING_batch_verification_sigma_reconciliation_2026-06-14.md`
A later batch-verification pass (Alex) **upgrades and reconciles** the string tension:
- **σ₂,σ₃,σ₄ are now "native, reproduced from source"** (the native connected-support torelon engine ran end-to-end, L=4/L=5 length-independent, exact vs KPS through O(u⁴)) — promoted from "asserted native." Consistent with my cont.7 cold-run of ENGINE_STRING_reproduce.sh.
- **σ₅,σ₆ signs RECONCILED to NEGATIVE.** The bridge σ(u)=½W(2u) (x=2u) is *forced* by the native engine: only it reproduces the engine's odd-order **σ₃=−61/408**; the alternative ½W(−2y) gives +61/408 (wrong sign at odd orders). ⟹ **σ₅(u)=−137767222189182735950309/2009803206414863779920000 (negative)** and σ₆ negative — validating the consolidated theorem.
- **The `SU3_KPS_STRING_COEFFICIENT_EXTRACTION` bundle's positive σ₅ is a convention SIGN ERROR** (it used ½W(−2y)); its even-order σ₆ is unaffected.
- **Verified this session (mine):** from the native σ₃=−61/408, ½W(2u) reproduces −61/408 exactly while ½W(−2y) gives +61/408 — confirming the reconciliation and the KPS-extraction sign error by elementary arithmetic.
σ₅,σ₆ remain **KPS historical targets** (not yet native reruns); native promotion is fully scoped (batch doc §5).

## Provenance

- Source: `C:\ALL THEORY\ZIP ARCHIVES\SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2.zip` — md5 `72e0342c8d3e74d371a4eee5af4da3ec`.
- Supersedes the earlier O4 package (`SU3_STRING_TENSION_O4_COMPLETE_BUNDLE`; its raw unit-vertex O4 docs are marked SUPERSEDED inside V2).
- Normalization fix confirmed by `GLUEBALL_STRING_NORMALIZATION_CORRECTION_V2.zip`.
- Distilled here: theorem, certificate, `ENGINE_STRING_reproduce.sh`, `src/` verifiers, bundle README, cold-run log.
  The `inputs/*.json.gz` (y4 supports/intertwiners/carriers) and `historical/` KPS+Hamer transcriptions
  stay in the source bundle. Per-file MD5 in `MAN_SUN_md5sums.txt`.

## Open / next
- Assign \(m_5, m_6\) (glueball-mass coefficients at O5/O6) — currently unknown.
- A T2 review of the unit-vertex contraction + KPS normalization would raise the tier.
