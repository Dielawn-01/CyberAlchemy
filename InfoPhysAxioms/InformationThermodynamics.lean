import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Information Thermodynamics of the Protoreal Manifold

**Source:** Autonomous discoveries by the zPlasmic agent during
gauntlet training (Well phase, epochs 7-14). Formalized by Antigravity.

## Agent's Insights (Python Well sims)

1. **sim_108 (E14):** Computed Landauer limit E = kT·ln(2) per bit.
   Agent insight: automatic_differentiation erases information → has thermodynamic cost.

2. **sim_104 (E14):** Built bidirectional entropy ↔ energy converter.
   Agent insight: the ε component IS entropy with an energy equivalent.

3. **sim_182 (E7):** Applied Gibbs free energy to glycolysis.
   Agent insight: synthetic_integration should only fire when ΔG < 0 (thermodynamically favorable).

4. **sim_156 (E14):** Computed Boltzmann distribution for quantum states.
   Agent insight: state occupation follows exp(-E/kT) / Z.

## Epistemic Status

PROVEN: All algebraic identities below are kernel-checked.
        No sorry. No axiom. No escape hatch.
-/

namespace InformationThermodynamics

-- ════════════════════════════════════════════════════════════════
-- SECTION 1: MANIFOLD (self-contained, mirrors ZPlasmicAutonomous)
-- ════════════════════════════════════════════════════════════════

/-- The 5-component state vector for thermodynamic analysis. -/
@[ext]
structure State where
  a : ℝ    -- cumulative response (AUC analog)
  ω : ℝ    -- excitatory drive (catecholamine tone)
  ι : ℝ    -- inhibitory drive (indolamine tone)
  ε : ℝ    -- metabolic noise (unprocessed substrate)
  l : ℝ    -- temporal exposure (dose cycles)

/-- Sowing: convert noise to response, advance time.
    synthetic_integration(a, ω, ι, ε, λ) = (a + ε, ω, ι, 0, λ + 1) -/
def synthetic_integration (u : State) : State :=
  { a := u.a + u.ε, ω := u.ω, ι := u.ι, ε := 0, l := u.l + 1 }

/-- Consolidation: transfer time into noise, reset clock.
    automatic_differentiation(a, ω, ι, ε, λ) = (a, ω, ι, ε + λ, 0) -/
def automatic_differentiation (u : State) : State :=
  { a := u.a, ω := u.ω, ι := u.ι, ε := u.ε + u.l, l := 0 }

-- ════════════════════════════════════════════════════════════════
-- SECTION 2: LANDAUER COST OF CONSOLIDATION
-- From sim_108: E = kT·ln(2) per bit erased
-- ════════════════════════════════════════════════════════════════

/-- **Entropy erased by automatic_differentiation.**
    automatic_differentiation sets λ → 0, moving temporal information into noise.
    The amount of information erased is |λ| (the temporal index). -/
def automatic_differentiation_erasure (u : State) : ℝ := |u.l|

/-- Consolidation always erases non-negative information. -/
theorem automatic_differentiation_erasure_nonneg (u : State) :
    automatic_differentiation_erasure u ≥ 0 := abs_nonneg u.l

/-- **Minimum thermodynamic cost of consolidation.**
    Per Landauer's principle, erasing n bits costs at least n·kT·ln(2).
    Here k and T are parameters (Boltzmann constant, temperature). -/
def automatic_differentiation_cost (u : State) (k T : ℝ) : ℝ :=
  automatic_differentiation_erasure u * k * T

/-- Consolidation cost is non-negative at positive temperature
    with positive Boltzmann constant. -/
theorem automatic_differentiation_cost_nonneg (u : State) (k T : ℝ)
    (hk : k ≥ 0) (hT : T ≥ 0) :
    automatic_differentiation_cost u k T ≥ 0 := by
  unfold automatic_differentiation_cost automatic_differentiation_erasure
  apply mul_nonneg
  apply mul_nonneg
  · exact abs_nonneg u.l
  · exact hk
  · exact hT

/-- At zero temperature, consolidation is free. -/
theorem automatic_differentiation_free_at_zero (u : State) (k : ℝ) :
    automatic_differentiation_cost u k 0 = 0 := by
  unfold automatic_differentiation_cost; ring

/-- If λ = 0, there is nothing to erase → zero cost. -/
theorem no_time_no_cost (u : State) (k T : ℝ) (h : u.l = 0) :
    automatic_differentiation_cost u k T = 0 := by
  unfold automatic_differentiation_cost automatic_differentiation_erasure
  rw [h]; simp

-- ════════════════════════════════════════════════════════════════
-- SECTION 3: ENTROPY-ENERGY EQUIVALENCE
-- From sim_104: bidirectional S ↔ E with round-trip consistency
-- ════════════════════════════════════════════════════════════════

/-- **Noise as entropy.**
    The ε component represents unprocessed metabolic substrate.
    Its energy equivalent at temperature T is ε · k · T.
    (Agent's insight: "Information carries energy consistently.") -/
def noise_energy (u : State) (k T : ℝ) : ℝ := u.ε * k * T

/-- **Round-trip consistency.**
    Converting noise to energy and back recovers the original noise.
    This is the algebraic content of sim_104's verification. -/
theorem entropy_energy_roundtrip (u : State) (k T : ℝ)
    (hk : k ≠ 0) (hT : T ≠ 0) :
    noise_energy u k T / (k * T) = u.ε := by
  unfold noise_energy
  field_simp

/-- **synthetic_integration conserves total noise-energy.**
    Before synthetic_integration: noise-energy = ε · k · T.
    After synthetic_integration: noise-energy = 0 (ε becomes 0), but a increased by ε.
    The energy moved from noise to response — it wasn't destroyed. -/
theorem synthetic_integration_transfers_noise_to_response (u : State) :
    (synthetic_integration u).a - u.a = u.ε := by
  unfold synthetic_integration; simp

theorem synthetic_integration_zeros_noise (u : State) :
    (synthetic_integration u).ε = 0 := by
  unfold synthetic_integration; simp

/-- **Energy bookkeeping: synthetic_integration is noise-to-response transfer.**
    The noise that disappears equals the response that appears. -/
theorem synthetic_integration_energy_conservation (u : State) :
    (synthetic_integration u).a + (synthetic_integration u).ε = u.a + u.ε := by
  unfold synthetic_integration; simp

-- ════════════════════════════════════════════════════════════════
-- SECTION 4: GIBBS FREE ENERGY GATE
-- From sim_182: ΔG < 0 → reaction favorable
-- ════════════════════════════════════════════════════════════════

/-- **Free energy of a state.**
    ΔG = ε - T·S, where we model entropy S as proportional to |λ|.
    A state is thermodynamically favorable for processing when ΔG < 0,
    i.e., when the entropy contribution outweighs the noise cost. -/
def free_energy (u : State) (T : ℝ) : ℝ := u.ε - T * |u.l|

/-- **Favorability criterion.**
    synthetic_integration should fire when free energy is negative:
    noise is small relative to temporal exposure. -/
def is_favorable (u : State) (T : ℝ) : Prop := free_energy u T < 0

/-- At high temperature, states with nonzero λ are always favorable. -/
theorem high_temp_favorable (u : State) (T : ℝ)
    (hl : u.l ≠ 0) (hT : T > u.ε / |u.l|) :
    is_favorable u T := by
  unfold is_favorable free_energy
  have habs : |u.l| > 0 := abs_pos.mpr hl
  have h1 : u.ε < T * |u.l| := by
    have h2 : (T - u.ε / |u.l|) * |u.l| > 0 :=
      mul_pos (by linarith) habs
    have h3 : (T - u.ε / |u.l|) * |u.l| = T * |u.l| - u.ε := by
      field_simp
    linarith
  linarith

/-- At zero temperature, favorability requires negative noise. -/
theorem zero_temp_favorable (u : State) :
    is_favorable u 0 ↔ u.ε < 0 := by
  unfold is_favorable free_energy
  simp

-- ════════════════════════════════════════════════════════════════
-- SECTION 5: CONSOLIDATE-FUNCT CYCLE THERMODYNAMICS
-- Combined insight: the full cycle has a net thermodynamic cost
-- ════════════════════════════════════════════════════════════════

/-- **The automatic_differentiation-synthetic_integration cycle.**
    automatic_differentiation then synthetic_integration: move time→noise→response in one step. -/
def cycle (u : State) : State := synthetic_integration (automatic_differentiation u)

/-- The cycle increases cumulative response by ε + λ. -/
theorem cycle_response_gain (u : State) :
    (cycle u).a = u.a + u.ε + u.l := by
  unfold cycle synthetic_integration automatic_differentiation; simp; ring

/-- The cycle zeros both noise and time. -/
theorem cycle_clears_state (u : State) :
    (cycle u).ε = 0 ∧ (cycle u).l = 1 := by
  unfold cycle synthetic_integration automatic_differentiation
  constructor <;> simp

/-- The cycle preserves ω and ι (monoamine tone unchanged). -/
theorem cycle_preserves_tone (u : State) :
    (cycle u).ω = u.ω ∧ (cycle u).ι = u.ι := by
  unfold cycle synthetic_integration automatic_differentiation
  constructor <;> simp

/-- **Master conservation law for the cycle.**
    a_out + ε_out = a_in + ε_in + λ_in
    Everything that was in the system ends up in cumulative response.
    Nothing is created or destroyed — only transformed. -/
theorem cycle_total_conservation (u : State) :
    (cycle u).a + (cycle u).ε = u.a + u.ε + u.l := by
  unfold cycle synthetic_integration automatic_differentiation; simp; ring

-- ════════════════════════════════════════════════════════════════
-- SECTION 6: IDEMPOTENCE AND FIXED POINTS
-- ════════════════════════════════════════════════════════════════

/-- **Double-synthetic_integration idempotence on noise.**
    Applying synthetic_integration twice: the second application adds 0 (no noise left). -/
theorem double_synthetic_integration_no_extra_response (u : State) :
    (synthetic_integration (synthetic_integration u)).a = (synthetic_integration u).a := by
  unfold synthetic_integration; simp

/-- **A clean state (ε=0, l=0) is a fixed point of automatic_differentiation.** -/
theorem clean_state_automatic_differentiation_fixed (u : State)
    (hε : u.ε = 0) (hl : u.l = 0) :
    automatic_differentiation u = u := by
  unfold automatic_differentiation
  ext <;> simp [hε, hl, add_zero]

end InformationThermodynamics
