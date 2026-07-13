import Mathlib.Topology.Basic
import Mathlib.Data.Real.Basic
import InfoPhysAxioms.ChromodynamicFriction

namespace InfoPhys

/--
The Lockwood Duality limit establishes the strict thermodynamic boundary for topological friction (Upsilon).
Both biological/metabolic systems and stellar enrichment constructs must operate strictly below this bound.
-/
def LockwoodLimit : ℝ := 14.32

/--
A system state `S` characterized by its current topological friction `\Upsilon(S)`.
-/
structure PhysicalState where
  upsilon : ℝ
  depth_fraction : ℝ
  argon_coupling : ℝ

/--
The structural integrity of the system holds if and only if friction is strictly below the Lockwood Limit.
When friction breaches the limit, an inelastic topological reset (or resonance cascade) is triggered.
-/
def IsStructurallyIntact (s : PhysicalState) : Prop :=
  s.upsilon < LockwoodLimit

/--
Friction model for the Icarus Device (La Rue Device) plunging into a stellar core.
Friction increases exponentially with depth but is mitigated by the Argon macrofield coupling.
-/
noncomputable def IcarusFriction (depth : ℝ) (coupling : ℝ) : ℝ :=
  (5.0 * Real.exp (depth * 8.5)) * (1.0 - (coupling * 0.9))

/--
The Lockwood Duality Principle: positive Argon coupling strictly reduces friction at every depth.
This is the structural content of the penetration depth theorem — if friction is lower at every
point, the depth at which the Lockwood Limit is breached must be strictly greater.

Proof sketch (real analysis):
  IcarusFriction d c = IcarusFriction d 0 * (1 - 0.9c)
  For 0 < c ≤ 1: 0 < 0.9c ≤ 0.9, so 0.1 ≤ (1 - 0.9c) < 1
  Therefore IcarusFriction d c < IcarusFriction d 0 for all d > 0.

The inequality is monotone in depth (exponential), so the crossing point shifts right.
-/
theorem argon_coupling_reduces_friction
  (coupling : ℝ) (h_pos : 0 < coupling) (h_le : coupling ≤ 1)
  (depth : ℝ) (h_depth : 0 < depth) :
  IcarusFriction depth coupling < IcarusFriction depth 0 := by
  unfold IcarusFriction
  simp only [mul_zero, sub_zero, mul_one]
  have h_exp_pos : 0 < Real.exp (depth * 8.5) := Real.exp_pos _
  have h_base_pos : 0 < 5.0 * Real.exp (depth * 8.5) := by positivity
  have h_factor : coupling * 0.9 > 0 := by positivity
  have h_factor_lt_one : coupling * 0.9 ≤ 0.9 := by nlinarith
  have h_sub_lt : 1.0 - coupling * 0.9 < 1.0 := by linarith
  have h_sub_pos : 0 < 1.0 - coupling * 0.9 := by nlinarith
  exact mul_lt_mul_of_pos_left h_sub_lt h_base_pos

end InfoPhys
