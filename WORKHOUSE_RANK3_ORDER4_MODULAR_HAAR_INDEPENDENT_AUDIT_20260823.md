# Rank-3/order-4 exact Haar sum — independent modular audit

## Result

The frozen 117,161 orientation-sensitive topology keys were losslessly aggregated into 69,800 fully unordered contraction classes. Exact SU(3) Haar contraction over all 69,800 classes gives

\[
\sum_T w_T H_T
=-\frac{805586892848311021}{8092176661386675},
\]

and therefore

\[
D_{\mathrm{EXACT}}
=-\frac{13}{896}+\frac12\sum_Tw_TH_T
=-\frac{361008126292641364183}{7250590288602460800}
\approx -49.790170444484609.
\]

With the separately reproduced fold and linked-vacuum scalars

\[
F=\frac{5315003}{140454},\qquad
V_{\mathrm{linked}}=-\frac{1474623}{1675520},
\]

the requested final combination is

\[
m_{4,\mathrm{rest}}=D_{\mathrm{EXACT}}+F-V_{\mathrm{linked}}
=-\frac{160506019419340168451}{14501180577204921600}
\approx -11.068479463778765.
\]

## Exactness gates

- The contractor used integer-scaled local projectors, modular one-variable factor elimination, a rigorous topology-specific triangle bound, and signed CRT uniqueness. No floating reconstruction or tolerance appears in the calculation.
- The full stable ledger contains 69,800 sorted unique records. Each includes its canonical topology, exact weight, local-pattern list, `q_product`, signed scaled Haar numerator, reduced Haar rational, exact weighted contribution, signed bound, and CRT primes.
- A separate replay recomputed every record's `q` product, bound, CRT sufficiency, Haar rational, weighted contribution, total sum, and `D_EXACT`. All gates passed. There are 9,184 zero-Haar classes.
- `denominator(D_EXACT)` divides the frozen
  `QBOUND = 62895057857493885215590055852113920000000`.
- The exact integer-over-`QBOUND` lift is
  `-3131555650840341423974721085483725619200000 / QBOUND`, and reduces exactly to `D_EXACT`.

## Independent checks

The modular calculation was completed without using the historical decimal or rational value of `D` as an input. Only after completion was its result compared with the separately implemented primary run; the numerator and denominator agree exactly.

The independent referee route also passed:

- exact inverse-Gram agreement for balanced sectors `k = 1,2,3`;
- exact pure-six inverse-Gram agreement;
- 9,100 pure-six projector-entry comparisons against the independent 488-term delta expansion, including every entry on the complete 90-by-90 nonzero support;
- 40 additional actual frozen-topology comparisons across all 20 non-pure endpoint signatures;
- a separate stratified audit of 44 actual topologies, selecting the easiest and hardest representative of every one of all 22 signatures, including both pure-six signatures;
- an independent all-record replay of the final 69,800-entry ledger.

The arithmetic certificate is therefore closed for the frozen generator lineage. This does not independently prove that the primitive generator is a complete physical perturbation expansion; that is a distinct provenance/modeling obligation.

## Hashes

- Frozen source topology archive: `5337734a57bd2e1fe690c636f19bc0f65c48bac86cc029a7e4dfe87251e8ff59`
- Exact 69,800-record Haar ledger: `1b9ed1801e1125e15c4331cb0b06fe2a6782f0638efe725640f3602001f1b469`
- All-record validation: `7eb3ecb001dae85db0e2d4e1d87157e9b6d32fa42cee565c390e8663c05c3bcd`
- Independent 44-case stratified audit: `70516a9ae82c9de084b9cb5097afec11a9263bd15a5cd22a49e8763742d122ec`
- Independent referee report: `1b10d6f477b2ee7bbec5cd2485a290a933058c5ee51efcbaad846312ea905bd7`
- Modular contractor source: `42eede1ad54fc5ad08ffbec12b6d9cf856a6aa0e44920ee2b4f9518ced2344c1`

The accompanying ZIP contains the frozen source archive, exact ledger, summaries and validations, both independent cross-check certificates, referee report, and all contractor/replay sources needed to audit the route.
