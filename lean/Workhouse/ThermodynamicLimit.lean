import Mathlib.Analysis.InnerProductSpace.Continuous
import Mathlib.Analysis.InnerProductSpace.LinearPMap
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.Topology.MetricSpace.Cauchy
import Mathlib.Tactic

/-!
# Analytic limit mechanisms in the SC17 thermodynamic derivation

Source: docs/derivations/wilson-sc17-thermodynamic-limit.md, T12 and IF3--IF8.
These theorems prove the limit and closability mechanisms on actual normed and
inner-product spaces. The SU(2) cylinder domain, its density, the score response
and finite-volume integration by parts are explicit upstream inputs, not axioms.
-/

namespace Workhouse.ThermodynamicLimit

open Filter Topology

/-- T12: a vanishing cut-response envelope constructs a limit in any complete
metric space, including a continuous-score space with its uniform metric. -/
theorem exists_limit_of_cut_response {E : Type*} [MetricSpace E] [CompleteSpace E]
    (u : ℕ → E) (b : ℕ → ℝ)
    (hcut : ∀ n m, n ≤ m → dist (u n) (u m) ≤ b n)
    (hb : Tendsto b atTop (𝓝 0)) :
    ∃ limit : E, Tendsto u atTop (𝓝 limit) := by
  exact cauchySeq_tendsto_of_complete (cauchySeq_of_le_tendsto_0' b hcut hb)

/-- The limiting expectation retains every finite-volume closed inequality. -/
theorem limit_preserves_gap_bound (variance energy : ℕ → ℝ)
    (v e gap : ℝ)
    (hv : Tendsto variance atTop (𝓝 v))
    (he : Tendsto energy atTop (𝓝 e))
    (hgap : ∀ n, gap * variance n ≤ energy n) : gap * v ≤ e := by
  exact le_of_tendsto_of_tendsto (tendsto_const_nhds.mul hv) he
    (Filter.Eventually.of_forall hgap)

section Closability

variable {E F : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    [NormedAddCommGroup F] [InnerProductSpace ℝ F]

/-- The sequential graph criterion for closability of an operator on a linear
domain. Its topology is inherited from the ambient Hilbert space, not from an
already closed graph norm. -/
def SequentiallyClosable (S : Submodule ℝ E) (D : S →ₗ[ℝ] F) : Prop :=
  ∀ (u : ℕ → S) (v : F),
    Tendsto (fun n => (u n : E)) atTop (𝓝 0) →
    Tendsto (fun n => D (u n)) atTop (𝓝 v) → v = 0

/-- IF3 => IF4: a densely defined test adjoint proves the graph criterion.
Neither continuity nor boundedness of D is assumed. The map A is the actual
integration-by-parts test expression, including the logarithmic-score term. -/
theorem closable_of_integration_by_parts (S : Submodule ℝ E)
    (T : Submodule ℝ F) (D : S →ₗ[ℝ] F) (A : T →ₗ[ℝ] E)
    (hT : Dense (T : Set F))
    (hibp : ∀ f : S, ∀ g : T,
      inner ℝ (D f) (g : F) = inner ℝ (f : E) (A g)) :
    SequentiallyClosable S D := by
  intro u v hu hv
  apply hT.eq_zero_of_inner_left ℝ
  intro g hg
  let test : T := ⟨g, hg⟩
  have hleft : Tendsto (fun n => inner ℝ (D (u n)) g) atTop
      (𝓝 (inner ℝ v g)) := hv.inner tendsto_const_nhds
  have hright : Tendsto (fun n => inner ℝ (D (u n)) g) atTop (𝓝 0) := by
    have h : Tendsto (fun n => inner ℝ (u n : E) (A test)) atTop
        (𝓝 (inner ℝ (0 : E) (A test))) := hu.inner tendsto_const_nhds
    simpa only [inner_zero_left, ← hibp] using h
  exact tendsto_nhds_unique hleft hright

/-- IF8: a Poincare bound on a form core extends to a graph limit. This proves
the extension step with an arbitrary continuous centering projection. -/
theorem gap_bound_on_graph_limit (S : Submodule ℝ E) (D : S →ₗ[ℝ] F)
    (center : E →L[ℝ] E) (gap : ℝ)
    (hcore : ∀ f : S, gap * ‖center (f : E)‖ ^ 2 ≤ ‖D f‖ ^ 2)
    (u : ℕ → S) (f : E) (v : F)
    (hu : Tendsto (fun n => (u n : E)) atTop (𝓝 f))
    (hv : Tendsto (fun n => D (u n)) atTop (𝓝 v)) :
    gap * ‖center f‖ ^ 2 ≤ ‖v‖ ^ 2 := by
  apply le_of_tendsto_of_tendsto
    (tendsto_const_nhds.mul (((center.continuous.tendsto f).comp hu).norm.pow 2))
    (hv.norm.pow 2)
  exact Filter.Eventually.of_forall (fun n => hcore (u n))

end Closability

/-- IF4 with the library's actual unbounded-operator closure: a densely defined
formal integration-by-parts adjoint gives a closed extension and hence the
canonical closed graph. -/
theorem closed_extension_of_integration_by_parts {E F : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℝ F] [CompleteSpace F]
    (D : E →ₗ.[ℝ] F) (A : F →ₗ.[ℝ] E)
    (hA : Dense (A.domain : Set F)) (hibp : D.IsFormalAdjoint A) :
    D.IsClosable ∧ D.closure.IsClosed := by
  have hc : D.IsClosable :=
    (LinearPMap.adjoint_isClosed hA).isClosable.leIsClosable (hibp.symm.le_adjoint hA)
  exact ⟨hc, hc.closure_isClosed⟩

section WeakLimit

open MeasureTheory

variable {X : Type*} [TopologicalSpace X] [MeasurableSpace X]
    [OpensMeasurableSpace X]

/-- Uniformly varying continuous tests can be integrated against varying
weakly convergent laws. This is the score-product limit used in IF3. -/
theorem integral_under_weak_and_uniform_convergence
    (μn : ℕ → ProbabilityMeasure X) (μ : ProbabilityMeasure X)
    (fn : ℕ → BoundedContinuousFunction X ℝ) (f : BoundedContinuousFunction X ℝ)
    (hμ : Tendsto μn atTop (𝓝 μ)) (hf : Tendsto fn atTop (𝓝 f)) :
    Tendsto (fun n => ∫ x, fn n x ∂(μn n : Measure X)) atTop
      (𝓝 (∫ x, f x ∂(μ : Measure X))) := by
  have hnorm : Tendsto (fun n => ‖fn n - f‖) atTop (𝓝 0) := by
    have hsub : Tendsto (fun n => fn n - f) atTop (𝓝 (f - f)) :=
      hf.sub tendsto_const_nhds
    simpa using hsub.norm
  have hzero : Tendsto (fun n => ∫ x, (fn n - f) x ∂(μn n : Measure X))
      atTop (𝓝 0) := by
    apply squeeze_zero_norm (fun n => ?_) hnorm
    simpa using (norm_integral_le_of_norm_le_const
      (μ := (μn n : Measure X))
      (Filter.Eventually.of_forall (fun x => (fn n - f).norm_coe_le_norm x)))
  have hfixed := ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hμ f
  have hsum := hzero.add hfixed
  simpa only [BoundedContinuousFunction.sub_apply,
    integral_sub ((fn _).integrable _) (f.integrable _), sub_add_cancel, zero_add] using hsum

/-- Finite-volume integration by parts passes to the limiting law with a
uniformly convergent logarithmic score. Df and Dg are the supplied actual
cylinder derivatives; their existence and the finite identity remain inputs. -/
theorem integration_by_parts_under_weak_limit
    (μn : ℕ → ProbabilityMeasure X) (μ : ProbabilityMeasure X)
    (f g Df Dg : BoundedContinuousFunction X ℝ)
    (βn : ℕ → BoundedContinuousFunction X ℝ) (β : BoundedContinuousFunction X ℝ)
    (hμ : Tendsto μn atTop (𝓝 μ)) (hβ : Tendsto βn atTop (𝓝 β))
    (hibp : ∀ n, (∫ x, (Df * g) x ∂(μn n : Measure X)) =
      -(∫ x, (f * (Dg + βn n * g)) x ∂(μn n : Measure X))) :
    (∫ x, (Df * g) x ∂(μ : Measure X)) =
      -(∫ x, (f * (Dg + β * g)) x ∂(μ : Measure X)) := by
  have hl := ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hμ (Df * g)
  have htest : Tendsto (fun n => f * (Dg + βn n * g)) atTop
      (𝓝 (f * (Dg + β * g))) :=
    tendsto_const_nhds.mul (tendsto_const_nhds.add (hβ.mul tendsto_const_nhds))
  have hr := (integral_under_weak_and_uniform_convergence μn μ _ _ hμ htest).neg
  have hs : Tendsto (fun n => ∫ x, (Df * g) x ∂(μn n : Measure X)) atTop
      (𝓝 (-(∫ x, (f * (Dg + β * g)) x ∂(μ : Measure X)))) := by
    simpa only [hibp] using hr
  exact tendsto_nhds_unique hl hs

/-- IF1 => IF8 for actual weakly converging probability measures and bounded
continuous observables and energy densities. All three integrals pass to the
same limiting measure; no limiting Poincare inequality is assumed. -/
theorem poincare_under_weak_convergence
    (μn : ℕ → ProbabilityMeasure X) (μ : ProbabilityMeasure X)
    (f energy : BoundedContinuousFunction X ℝ) (gap : ℝ)
    (hμ : Tendsto μn atTop (𝓝 μ))
    (hfinite : ∀ n,
      gap * ((∫ x, (f * f) x ∂(μn n : Measure X)) -
        (∫ x, f x ∂(μn n : Measure X)) ^ 2) ≤
        ∫ x, energy x ∂(μn n : Measure X)) :
      gap * ((∫ x, (f * f) x ∂(μ : Measure X)) -
        (∫ x, f x ∂(μ : Measure X)) ^ 2) ≤
        ∫ x, energy x ∂(μ : Measure X) := by
  have hm := ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hμ f
  have hs := ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hμ (f * f)
  have he := ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mp hμ energy
  exact limit_preserves_gap_bound _ _ _ _ gap (hs.sub (hm.pow 2)) he hfinite

end WeakLimit

section SpectralMass

open MeasureTheory Set

/-- IF13's first-moment argument for an actual finite measure. The lower
spectral support is supplied independently; a positive lower bound for the
mass and an upper first moment force nonzero mass in a bounded interval. -/
theorem spectral_interval_mass (σ : Measure ℝ) [IsFiniteMeasure σ]
    (lower cutoff mass energy : ℝ) (hcut : 0 < cutoff)
    (hpositive : ∀ᵐ x ∂σ, 0 ≤ x)
    (hintegrable : Integrable (fun x : ℝ => x) σ)
    (hlower : σ.real (Iio lower) = 0)
    (hmass : mass ≤ σ.real univ)
    (henergy : (∫ x, x ∂σ) ≤ energy) :
    mass - energy / cutoff ≤ σ.real (Icc lower cutoff) := by
  have hm := mul_meas_ge_le_integral_of_nonneg hpositive hintegrable cutoff
  have htail : σ.real (Ioi cutoff) ≤ energy / cutoff := by
    apply (le_div_iff₀ hcut).2
    have hmono : σ.real (Ioi cutoff) ≤ σ.real (Ici cutoff) :=
      measureReal_mono Ioi_subset_Ici_self
    have hmark : cutoff * σ.real (Ici cutoff) ≤ energy := hm.trans henergy
    nlinarith
  have hsplit := measureReal_add_measureReal_compl (μ := σ)
    (s := Iic cutoff) measurableSet_Iic
  have hsplit' : σ.real (Iic cutoff) + σ.real (Ioi cutoff) = σ.real univ := by
    simpa only [compl_Iic] using hsplit
  have hremove : σ.real (Iic cutoff \ Iio lower) = σ.real (Iic cutoff) :=
    measureReal_sdiff_null hlower
  have heq : Iic cutoff \ Iio lower = Icc lower cutoff := by
    ext x
    simp only [Set.mem_sdiff, mem_Iic, mem_Iio, mem_Icc, not_lt]
    exact and_comm
  rw [heq] at hremove
  rw [hremove]
  linarith

/-- IF12 => IF13: the actual finite spectral measure, with the source's mass,
support and first-moment bounds, has the stated positive plaquette interval
weight. This is a measure theorem, not a sampled eigenvalue calculation. -/
theorem sc17_plaquette_interval (σ : Measure ℝ) [IsFiniteMeasure σ]
    (ε D : ℝ) (hε : 0 < ε)
    (hpositive : ∀ᵐ x ∂σ, 0 ≤ x)
    (hintegrable : Integrable (fun x : ℝ => x) σ)
    (hlower : σ.real (Iio (4 * ε / 3)) = 0)
    (hmass : Real.exp (-D) / 4 ≤ σ.real univ)
    (henergy : (∫ x, x ∂σ) ≤ 4 * ε) :
    Real.exp (-D) / 8 ≤ σ.real (Icc (4 * ε / 3) (32 * ε * Real.exp D)) := by
  have hcut : 0 < 32 * ε * Real.exp D := by positivity
  have h := spectral_interval_mass σ (4 * ε / 3) (32 * ε * Real.exp D)
    (Real.exp (-D) / 4) (4 * ε) hcut hpositive hintegrable hlower hmass henergy
  have hcalc : Real.exp (-D) / 4 - (4 * ε) / (32 * ε * Real.exp D) =
      Real.exp (-D) / 8 := by
    rw [Real.exp_neg]
    field_simp
    ring
  rwa [hcalc] at h

end SpectralMass

end Workhouse.ThermodynamicLimit
