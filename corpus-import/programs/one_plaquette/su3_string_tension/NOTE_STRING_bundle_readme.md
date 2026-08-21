# SU(3) physical string-tension release V2

This release corrects the normalization of the earlier O(y^4) string-tension
package.

The source programs compute unit-vertex reduced contractions. The paper
Hamiltonian contains the vertex

\[
-y(\chi+\bar\chi)/4,
\]

so

\[
\sigma_n=(-1/4)^n\sigma_n^{\rm reduced}.
\]

The verifier applies this factor and checks exact agreement with the
Kogut–Pearson–Shigemitsu table through order four. The KPS table supplies the
denominator coefficients at orders five and six.

No value is assigned to the unknown glueball mass coefficients \(m_5,m_6\).

## Reproduce

```bash
bash ENGINE_STRING_reproduce.sh
```

Expected final line:

```text
ALL CLEAN REPRODUCTION STAGES PASS
```
