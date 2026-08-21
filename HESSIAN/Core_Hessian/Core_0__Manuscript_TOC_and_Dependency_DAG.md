---
file: Core_0__Manuscript_TOC_and_Dependency_DAG.md
status: DRAFT
depends_on:
  - Appendix_A__Notation_and_Constants.md
  - Appendix_B__Lattice_Cell_Complex_and_Cochains.md
  - Appendix_C__Configuration_Geometry.md
  - Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md
  - Appendix_E__Bakry_Emery_Calculus.md
  - Appendix_F__Helffer_Sjostrand_Covariance.md
  - Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md
  - Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel.md
  - Appendix_I__Localization_Algebra.md
  - Appendix_J__Typicality_Mechanism_for_K.md
  - Appendix_K__Reflection_Positivity_for_Wilson.md
  - Appendix_L__OS_Reconstruction_and_Gap_Extraction.md
  - Appendix_M__Continuum_Permanence_Interfaces.md
  - Appendix_N__External_Inputs_Ledger.md
  - Core_1__Lattice_Gauge_Model_at_Fixed_Cutoff.md
  - Core_2__Configuration_Geometry_and_Differential_Calculus.md
  - Core_3__OS_Framework_at_Fixed_Cutoff.md
  - Core_4__Vacuum_Linearization_and_Discrete_Maxwell_Structure.md
  - Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set.md
  - Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md
  - Core_7__Conditioned_Exponential_Clustering_via_Inverse_Decay.md
  - Core_8__Localization_and_Transfer_to_Infinite_Volume.md
  - Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md
  - Core_10__Conditional_Continuum_Extension.md
feeds_into:
  - Core-1
  - Core-2
  - Core-3
  - Core-4
  - Core-5
  - Core-6
  - Core-7
  - Core-8
  - Core-9
  - Core-10
---

# Core-0 — Manuscript table of contents and dependency DAG

## Core-0.0 Interface

**Definition (Core-0.0.1: purpose).**  
This file is the unique index for the manuscript set. It records:
1. a table of contents for Core-1–Core-10;
2. a list of Appendices A–N with one-sentence roles;
3. a textual dependency DAG showing how appendices feed core statements;
4. a single-paragraph list of items that remain open after completion of all internal proofs.

**Definition (Core-0.0.2: rule inheritance).**  
All label conventions and all named constants used by the manuscript set are imported from Appendix A, Definitions **A.0.1–A.0.5**.

**Definition (Core-0.0.3: arrow notation).**  
For files or labeled statements `X,Y`, the notation
`X → Y` means: *`Y` uses `X`*.

---

## Core-0.1 Core Manuscript table of contents

**Definition (Core-0.1.1: Core-1).**  
`Core_1__Lattice_Gauge_Model_at_Fixed_Cutoff.md` defines the finite-volume gauge model at fixed cutoff: cell sets, gauge action, Wilson action, finite-volume Gibbs measure, and the admissible observable class.

**Definition (Core-0.1.2: Core-2).**  
`Core_2__Configuration_Geometry_and_Differential_Calculus.md` defines the configuration manifold geometry, differential calculus (gradient, Hessian, generator, carré du champ), and the horizontal/vertical splitting used for gauge-invariant observables.

**Definition (Core-0.1.3: Core-3).**  
`Core_3__OS_Framework_at_Fixed_Cutoff.md` defines reflection and the OS positive-time algebra, and it states the external OS reconstruction interface used later to convert Euclidean time decay into a Hamiltonian spectral gap.

**Definition (Core-0.1.4: Core-4).**  
`Core_4__Vacuum_Linearization_and_Discrete_Maxwell_Structure.md` proves the vacuum linearization and Hessian identification: the Wilson Hessian at the vacuum equals a constant multiple of `d_1^* d_1` on 1-cochains, yielding the discrete Maxwell operator used in subsequent coercivity and decay arguments.

**Definition (Core-0.1.5: Core-5).**  
`Core_5__Local_Coercivity_and_Matrix_Hinge_on_Good_Set.md` defines the canonical good set `K` and proves the pointwise coercivity (“matrix hinge”) lower bound for the Bakry–Émery curvature matrix on `K`, producing a strictly positive massive Maxwell-type operator on horizontal directions.

**Definition (Core-0.1.6: Core-6).**  
`Core_6__Conditional_Covariance_Bound_via_HS_and_Hinge.md` states and applies the Helffer–Sjöstrand covariance representation to bound conditional covariances on `K` by an `M_H^{-1}`-kernel form, where `M_H` is the horizontal massive Maxwell operator from Core-5.

**Definition (Core-0.1.7: Core-7).**  
`Core_7__Conditioned_Exponential_Clustering_via_Inverse_Decay.md` proves exponential off-diagonal decay of the Green kernel `M_H^{-1}` using finite-range inverse decay (Combes–Thomas) and combines it with the HS bound to obtain conditional exponential clustering under `μ(·|K)`.

**Definition (Core-0.1.8: Core-8).**  
`Core_8__Localization_and_Transfer_to_Infinite_Volume.md` proves a covariance decomposition across `K` and uses it to transfer conditional clustering under `μ(·|K)` to full clustering under `μ`, with an explicit error term proportional to `μ(K^c)`.

**Definition (Core-0.1.9: Core-9).**  
`Core_9__Thermodynamic_Limit_and_OS_Gap_at_Fixed_Cutoff.md` passes clustering to infinite-volume limit points at fixed cutoff, proves permanence of OS structure under local limits, and applies OS reconstruction to convert Euclidean time decay into a fixed-cutoff OS Hamiltonian spectral gap.

**Definition (Core-0.1.10: Core-10).**  
`Core_10__Conditional_Continuum_Extension.md` isolates the conditional continuum step: it formulates explicit assumptions and external inputs under which a uniform fixed-cutoff gap along a scaling trajectory implies a continuum OS mass-gap statement.

---

## Core-0.2 Appendices and one-sentence roles

**Definition (Core-0.2.1: Appendix A).**  
`Appendix_A__Notation_and_Constants.md` is the single source of truth for symbols, norms, distances, and all named constants.

**Definition (Core-0.2.2: Appendix B).**  
`Appendix_B__Lattice_Cell_Complex_and_Cochains.md` fixes the lattice cell complex and the cochain operators `d_0,d_1` (and adjoints), including finite-range and bounded-overlap combinatorics.

**Definition (Core-0.2.3: Appendix C).**  
`Appendix_C__Configuration_Geometry.md` develops the product Lie-group Riemannian geometry and gauge-action differential geometry needed to define gradients, Hessians, and horizontal projections.

**Definition (Core-0.2.4: Appendix D).**  
`Appendix_D__Wilson_Action_Vacuum_Expansion_and_Hessian.md` provides the vacuum expansion of the Wilson action and the operator identity for its Hessian in terms of discrete Maxwell structure.

**Definition (Core-0.2.5: Appendix E).**  
`Appendix_E__Bakry_Emery_Calculus.md` states and proves the Bochner/`Γ_2` calculus with drift and the Bakry–Émery curvature matrix conventions used in matrix hinge arguments.

**Definition (Core-0.2.6: Appendix F).**  
`Appendix_F__Helffer_Sjostrand_Covariance.md` provides the Helffer–Sjöstrand representation in the form used for conditional covariance bounds and the matrix Brascamp–Lieb inequality extracted from it.

**Definition (Core-0.2.7: Appendix G).**  
`Appendix_G__Combes_Thomas_Finite_Range_Inverse_Decay.md` proves Combes–Thomas inverse-kernel decay for uniformly positive finite-range operators and records the constants in the form needed for `M_H^{-1}`.

**Definition (Core-0.2.8: Appendix H).**  
`Appendix_H__Davies_Type_Decay_Massive_Maxwell_Green_Kernel.md` specializes finite-range inverse decay to the massive Maxwell operator and records the volume-uniform exponential Green-kernel bound.

**Definition (Core-0.2.9: Appendix I).**  
`Appendix_I__Localization_Algebra.md` formalizes covariance decomposition across an event `K` and the resulting localization error bounds.

**Definition (Core-0.2.10: Appendix J).**  
`Appendix_J__Typicality_Mechanism_for_K.md` is the dedicated location for the typicality mechanism proving quantitative bounds on `μ(K^c)` for the chosen canonical good set `K`.

**Definition (Core-0.2.11: Appendix K).**  
`Appendix_K__Reflection_Positivity_for_Wilson.md` proves finite-volume reflection positivity for the Wilson lattice gauge measure (or else functions as an explicit interface if treated as an external input).

**Definition (Core-0.2.12: Appendix L).**  
`Appendix_L__OS_Reconstruction_and_Gap_Extraction.md` records the OS reconstruction interface and the spectral-measure argument converting Euclidean time decay to a Hamiltonian spectral gap.

**Definition (Core-0.2.13: Appendix M).**  
`Appendix_M__Continuum_Permanence_Interfaces.md` isolates continuum-interface statements: reflection positivity permanence under coarse graining/projective limits and Hamiltonian gap permanence under limiting procedures.

**Definition (Core-0.2.14: Appendix N).**  
`Appendix_N__External_Inputs_Ledger.md` enumerates every external input invoked in the manuscript set, with hypotheses and explicit “used in” locations.

---

## Core-0.3 Dependency DAG

**Definition (Core-0.3.1: DAG node classes).**  
The DAG nodes are:
- files: `Appendix_*` and `Core_*`;
- designated downstream targets: the fixed-cutoff clustering theorem and the fixed-cutoff OS spectral-gap theorem.

**Proposition (Core-0.3.2: appendix-to-core edges).**  
The following file-level edges are used:

- Appendix A → (all Core files; all appendices).
- Appendix B → Core-1, Core-2, Core-4, Core-5, Core-7; Appendix H.
- Appendix C → Core-1, Core-2, Core-5, Core-6.
- Appendix D → Core-4.
- Appendix E → Core-5.
- Appendix F → Core-6.
- Appendix G → Core-7.
- Appendix H → Core-7.
- Appendix I → Core-8.
- Appendix J → Core-8.
- Appendix K → Core-3, Core-9.
- Appendix L → Core-3, Core-9.
- Appendix M → Core-10.
- Appendix N → (all Core files).

**Proposition (Core-0.3.3: core-theorem dependency skeleton).**  
Let `T_clust` denote the fixed-cutoff clustering theorem proved in Core-7/Core-8, and let `T_gap(a)` denote the fixed-cutoff OS Hamiltonian spectral-gap theorem proved in Core-9. Then:

- (Core-1, Core-2) → Core-4.
- Core-4 → Core-5.
- (Core-5, Core-6) → Core-7.
- (Core-7, Core-8) → `T_clust`.
- (`T_clust`, Core-3) → `T_gap(a)`.
- (`T_gap(a)` along a scaling trajectory, Core-10 assumptions/external inputs) → conditional continuum OS mass-gap statement.

---

## Core-0.4 Open remainder

**Definition (Core-0.4.1: open remainder after completion of internal proofs).**  
After all internal Lemma/Proposition/Theorem items in Core-1–Core-10 and Appendices A–M are proved as written, the remaining open material is exactly: (i) a proof (in Appendix J) of a quantitative typicality bound for the chosen canonical good set `K` strong enough that the `μ(K^c)` localization error term in Core-8 does not dominate the exponential-in-distance term; and (ii) the conditional continuum interface in Core-10, which requires an explicit construction hypothesis for a continuum OS object plus a verified uniform physical lower bound for the fixed-cutoff gap along a scaling trajectory and permanence principles adequate to prevent gap collapse in the limit.

