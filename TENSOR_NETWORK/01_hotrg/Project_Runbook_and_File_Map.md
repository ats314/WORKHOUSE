# Project Runbook and File Map

> **Purpose.** This is the “carry it into a new chat” map: what files exist, what each one contains, and what to read first depending on what you’re doing (proof work vs code work).

---

## 1. Core theory documents (Yang–Mills mass gap)

### Doc D: Constructive lattice Yang–Mills
- `YM_MassGap_DocD_ConstructiveLatticeYM_v5(3).md`
- Lattice proof architecture, polarity sectors, Haar mass term, Hessian, transfer-matrix gap bound.

### Doc C: Stratified Sobolev + polarity
- `YM_MassGap_DocC_StratifiedSobolev_Polarity_v6.md`
- Infinite-rank commutator lemma, Gaussian polarity, and the change-of-measure bridge toward continuum polarity.

### Doc B: Dynamic YM + MFIP
- `YM_MassGap_DocB_DynamicYM_MFIP_Extended_v2(3).md`
- Bakry–Émery toy model, curvature \(\Rightarrow\) gap, Riccati convergence mechanism, and how this is meant to be realized in YM.

### Supporting “rigorous” extracts
- `Rigorous Derivation_ Lattice Hessian Formula and Eigenvalue Analysis(2).md`
- `Rigorous Derivation_ Transfer Matrix Spectral Gap in Lattice Yang-Mills(1).md`
- `Rigorous Proof_ Polarity of Reducible Connections in Lattice Yang-Mills(2).md`
- `Prong A_ RG Evolution of the Haar Measure Mass Term.md`
- `Prong B_ Formal Relation Between σ_anomaly and the β-Function.md`
- `Prong C_ Bounding the Correction Terms in σ_eff.md`

### Integration meta-summary
- `Integration Summary_ Packages 1 & 2 into Docs B, C, D.md`
- `Package 2_ Lattice Foundation - Complete Summary(1).md`
These summarize what’s claimed proven on the lattice and under Gaussian reference measures.

---

## 2. Code bundles (q-deformed / spectral gap experiments)

Two zip bundles were produced earlier in this chat:

- `q_massgap_bundle.zip`
- `q_massgap_bundle_extended.zip`

Unzipping produces a small “toy-to-structured” pipeline:
- stable \(q\)-\(6j\) / \(q\)-factorial numerics,
- building a toy transfer matrix / Doob transform generator,
- scanning spectral gaps vs parameters.

A key note file in the extended bundle:
- `q_massgap_bundle_extended/NOTES_massgap_proto_YM.txt`

---

## 3. MoA session transcripts (historical context)

- `MoA_Session_2025-11-26T04-47-31.txt`
- `MoA_Session_2025-11-26T04-58-20.txt`
- `MoA_Session_2025-11-26T05-51-19.txt`
- `MoA_Session_2025-11-26T06-02-14.txt`
- `MoA_Session_2025-11-26T06-25-35.txt`
- `MoA_Session_2025-11-26T06-39-09.txt`

These contain:
- q-deformed \(6j\) implementation sketches,
- HOTRG design,
- numerical stability discussions,
- \(\chi_{\mathrm{top}}\) nonnegativity sanity checks.

---

## 4. Reading order

### If you’re pushing the *proof* program
1. `YM_MassGap_DocD_ConstructiveLatticeYM_v5(3).md` (lattice skeleton)
2. `YM_MassGap_DocC_StratifiedSobolev_Polarity_v6.md` (polarity bridge)
3. `YM_MassGap_DocB_DynamicYM_MFIP_Extended_v2(3).md` (dynamic mechanism)

### If you’re pushing the *numerics* program
1. `q_massgap_bundle_extended/NOTES_massgap_proto_YM.txt`
2. `MoA_Session_...06-02-14.txt` (q-6j code sketch + HOTRG skeleton)
3. `MoA_Session_...06-39-09.txt` (topological susceptibility sanity checks)

---

## 5. The “single point of failure” warnings

1. **Continuum polarity is not automatic.** You need the \(L^p\) bridge for the density \(d\mu_{\mathrm{YM}}/d\mu_0\).
2. **Haar mass coefficient normalization matters.** Track conventions carefully.
3. **Do not trust negative \(\chi_{\mathrm{top}}\) at \(\theta=0\).** That’s either a bug or a broken mapping.
4. **Complex truncation (HOTRG) can fake physics.** Always do \(\chi\)-extrapolation and symmetry checks.

This runbook exists so you can restart a chat with a clean map instead of context chaos.
