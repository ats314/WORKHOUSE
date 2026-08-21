# Shell-six V2 independent validation

- Fresh cache: empty
- Exact shell-four calibration: PASS
- Three representative columns: PASS
- Full 44x44 reconstruction: PASS
- Exact Hermiticity: PASS
- Exact covariance under 48 elements of O_h: PASS
- Exact charge-conjugation covariance: PASS
- H1 nonzero entries: 96, all -1/3
- Exact channel extraction: PASS
- Shell-four/shell-six reverse-action transpose check: PASS
- Exact coupling strengths: 4/9, 8/9, 4/9
- Byte-identical representative, matrix, and analysis outputs: PASS
- Cold runtime in the audit container: 2.85 seconds
- Peak resident memory in the audit container: approximately 384 MB

The determinant tensor-network fast path replaces a pathological
36^6 delta-expansion by an exact dimension-three integer contraction.
