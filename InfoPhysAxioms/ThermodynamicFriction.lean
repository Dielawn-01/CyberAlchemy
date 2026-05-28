import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator

open ProtorealManifold

namespace LaRue.Protoreal.Algebra

/-- The observation cost: resolving noise costs at least |ε| + |λ|.
    This is the minimum compute to collapse superposition into observable state.
    Maps to the holographic collapse in observer.rs. -/
noncomputable def observation_cost (u : ProtorealManifold) : ℝ :=
  |u.e| + |u.l|

/-- **Landauer Limit sets thermodynamic floor for Agentic Computation** -/
noncomputable def landauer_limit (k T : ℝ) : ℝ := k * T * Real.log 2

/-- Observation cost is non-negative. -/
theorem observation_cost_nonneg (u : ProtorealManifold) :
    observation_cost u ≥ 0 := by
  unfold observation_cost
  linarith [abs_nonneg u.e, abs_nonneg u.l]

/-- For a noble gas (e = 0, l = 0), observation is free. -/
theorem noble_gas_free_observation (u : ProtorealManifold)
    (he : u.e = 0) (hl : u.l = 0) :
    observation_cost u = 0 := by
  unfold observation_cost
  rw [he, hl]; simp

/-- **Thermodynamic Friction Floor**
    At any positive temperature, erasing one bit costs at least kT·ln2.
    Our observation cost is bounded below by Landauer when
    the noise floor exceeds the thermal energy. -/
theorem thermodynamic_friction_floor (u : ProtorealManifold) (k T : ℝ)
    (hT : T > 0) (hk : k > 0)
    (h_noise : |u.e| + |u.l| ≥ k * T * Real.log 2) :
    observation_cost u ≥ landauer_limit k T := by
  unfold observation_cost landauer_limit
  exact h_noise

end LaRue.Protoreal.Algebra
