# Canonical archive decisions

| Workstream | Canonical source | Treatment of other uploaded packages |
|---|---|---|
| SU(3) fourth-order band and all-\(N\ge3\) shape | `GLUEBALL_FLAT_BAND_SOURCE_RELEASE_V0_8.zip` | v0.7 is superseded. |
| Coupling and string normalization | `GLUEBALL_STRING_NORMALIZATION_CORRECTION_V2.zip` | The normalization statements in `SU3_STRING_TENSION_PHYSICAL_O6_RELEASE_V2.zip` and the historical-recovery report are superseded. Their historical coefficient extraction may still be used after conversion to \(u\). |
| SU(3) fifth-order glueball mass/band | `SU3_Y5_COMPLETE_FIFTH_ORDER_BUNDLE.zip` | Canonical exact source for \(m_5=q_5\), \(A_5\), \(B_5\), and the 189-record kernel. |
| Shell-six exotic channels | `SHELL6_O2_SYMMETRY_REDUCED_V2_COMPLETE_RELEASE.zip` | The full-intermediate V1 bundle is retained as provenance, not the final result. |
| SU(4) exceptional fourth order | `SU4_HYBRID_COMPLETE_V2_BUNDLE.zip` plus `SU4_PERSISTENT_RESULTS_2026-06-14.zip` | The clean-no-edit archive is not source-complete and cannot serve as a reproduction package. This does not block SU(3) \(m_6\). |
| SU(5) fourth order | `SU5_FOURTH_ORDER_COMPLETE_RELEASE.zip` | The complete bundle is supporting provenance; the release is the cleaner reproduction artifact. |
| SU(6) determinant sector | `SU6_DETERMINANT_ARCHIVAL_V2_BUNDLE.zip` | Canonical determinant archive. |
| Stable-rank independent symbolic rerun | `Y4_SUN_FULL_SYMBOLIC_INDEPENDENT_RERUN_2026-06-14 (1).zip` | Supporting independent audit; v0.8 remains the integrated release. |

## Decision

Do not spend the next compute cycle repairing SU(4) packaging. The
highest-value open physical coefficient is the SU(3) zero-momentum sixth-order
mass coefficient \(m_6\). The exact folded-term component has already been
closed by this package.
