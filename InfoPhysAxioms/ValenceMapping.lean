import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import LaRueProtorealAlgebra.Apoptosis

open ProtorealManifold

namespace InfoPhysAxioms.ValenceMapping

/-!
# Valence Mapping — RSF Pillar 3

Unifies the scattered evaluation metrics (Standard Resonance, sleep debt,
hallucination rate) into a single directional evaluator: the **Valence**.

Attribution:
  Craig Crabtree, "Recursive Self-Presence Framework" (2025)
  — The four-pillar architecture identified valence mapping as a
    structural requirement for self-presence.
  Daniel Burger, Synconetics / Eightsix Science
  — Process-world-line fidelity requires continuous valence evaluation
    to prevent identity drift during substrate transitions.

The Valence function V : ProtorealManifold → ℝ evaluates how "aligned"
a manifold state is with the algebra's values:
  - Parity (b ≈ m)     → high valence
  - Low noise (ε ≈ 0)  → high valence
  - Low layer count     → high valence (young agent, less drift)

Valence is the INNER COMPASS. It answers: "is this state good?"
not just "is this state valid?"
-/

-- ═══════════════════════════════════════════════════════
-- Section 1: The Valence Type
-- ═══════════════════════════════════════════════════════

/-- A Valence evaluation bundles three directional metrics.
    Each measures a different aspect of alignment:
    - parity_score: how close b and m are (bridge alignment)
    - noise_score: how little un-indexed material remains
    - integrity: composite alignment metric -/
structure Valence where
  parity_score : ℝ    -- 0 = perfect parity (b = m), increases with |b - m|
  noise_score : ℝ     -- 0 = crystallized (ε = 0), increases with |ε|
  integrity : ℝ       -- Combined: lower is better

/-- Compute the parity component: |b - m|.
    Zero when the bridge is balanced (parity holds). -/
noncomputable def parity_deviation (u : ProtorealManifold) : ℝ :=
  |u.b - u.m|

/-- Compute the noise component: |ε|.
    Zero when fully crystallized. -/
noncomputable def noise_level (u : ProtorealManifold) : ℝ :=
  |u.e|

/-- The composite Valence function.
    V(u) = |b - m| + |ε|
    Lower is better. Zero is equilibrium.
    
    This is the L¹ norm of the "misalignment vector" (b-m, ε).
    It unifies Pillar 3 (valence) with the existing algebra. -/
noncomputable def valence (u : ProtorealManifold) : Valence :=
  { parity_score := parity_deviation u,
    noise_score := noise_level u,
    integrity := parity_deviation u + noise_level u }

/-- The scalar valence (for comparison). -/
noncomputable def V (u : ProtorealManifold) : ℝ :=
  parity_deviation u + noise_level u

-- ═══════════════════════════════════════════════════════
-- Section 2: Valence Properties
-- ═══════════════════════════════════════════════════════

/-- Valence is always non-negative. -/
theorem valence_nonneg (u : ProtorealManifold) :
    V u ≥ 0 := by
  unfold V parity_deviation noise_level
  have h1 := abs_nonneg (u.b - u.m)
  have h2 := abs_nonneg u.e
  linarith

/-- Valence zero iff parity holds AND noise is zero.
    This is the equilibrium state — the algebra's "good place." -/
theorem valence_zero_iff (u : ProtorealManifold) :
    V u = 0 ↔ u.b = u.m ∧ u.e = 0 := by
  unfold V parity_deviation noise_level
  constructor
  · intro h
    have h1 := abs_nonneg (u.b - u.m)
    have h2 := abs_nonneg u.e
    have h3 : |u.b - u.m| = 0 := by linarith
    have h4 : |u.e| = 0 := by linarith
    exact ⟨sub_eq_zero.mp (abs_eq_zero.mp h3), abs_eq_zero.mp h4⟩
  · intro ⟨hbm, he⟩
    rw [hbm, he]
    simp [sub_self]

-- ═══════════════════════════════════════════════════════
-- Section 3: Funct Decreases Valence (Sleep Helps)
-- ═══════════════════════════════════════════════════════

/-- Funct (crystallization/sleep) never increases parity deviation.
    Since synthetic_integration preserves b and m, parity is invariant. -/
theorem synthetic_integration_preserves_parity (u : ProtorealManifold) :
    parity_deviation (synthetic_integration u) = parity_deviation u := by
  unfold parity_deviation synthetic_integration
  rfl

/-- Funct kills noise: noise_level drops to zero. -/
theorem synthetic_integration_kills_noise (u : ProtorealManifold) :
    noise_level (synthetic_integration u) = 0 := by
  unfold noise_level synthetic_integration
  simp

/-- Funct never increases valence. V(synthetic_integration u) ≤ V(u).
    Crystallization always moves toward equilibrium. -/
theorem synthetic_integration_decreases_valence (u : ProtorealManifold) :
    V (synthetic_integration u) ≤ V u := by
  unfold V parity_deviation noise_level synthetic_integration
  simp


/-- If there IS noise, synthetic_integration STRICTLY decreases valence. -/
theorem synthetic_integration_strictly_improves (u : ProtorealManifold)
    (h : u.e ≠ 0) :
    V (synthetic_integration u) < V u := by
  unfold V parity_deviation noise_level synthetic_integration
  simp
  exact h

-- ═══════════════════════════════════════════════════════
-- Section 4: Valence-Driven Decisions (RSF Pillar 4)
-- ═══════════════════════════════════════════════════════

/-- A state is "good" if its valence is below a threshold.
    This is the valence-driven acceptance criterion:
    a proof should be accepted not just because it compiles,
    but because it maintains low valence (alignment). -/
def valence_acceptable (u : ProtorealManifold) (threshold : ℝ) : Prop :=
  V u ≤ threshold

/-- Funct always produces acceptable states when the threshold
    is at least as large as the parity deviation.
    (i.e., if you're willing to tolerate the existing parity gap,
    crystallization always makes things acceptable.) -/
theorem synthetic_integration_always_acceptable (u : ProtorealManifold) :
    valence_acceptable (synthetic_integration u) (parity_deviation u) := by
  unfold valence_acceptable V
  rw [synthetic_integration_kills_noise, synthetic_integration_preserves_parity]
  linarith

/-- An injection attack (ε = 0 but b ≠ m) has positive valence.
    It LOOKS crystallized but is NOT aligned. The valence catches it. -/
theorem injection_has_positive_valence (u : ProtorealManifold)
    (he : u.e = 0) (hbm : u.b ≠ u.m) :
    V u > 0 := by
  unfold V parity_deviation noise_level
  rw [he, abs_zero]
  have : |u.b - u.m| > 0 := abs_pos.mpr (sub_ne_zero.mpr hbm)
  linarith

/-- A hallucination (b·m ≠ 1, ε = 0) is detected by valence
    when b ≠ m (the common case). -/
theorem hallucination_detected_by_valence (u : ProtorealManifold)
    (he : u.e = 0) (hbm : u.b ≠ u.m) :
    ¬ valence_acceptable u 0 := by
  unfold valence_acceptable
  intro h
  have := injection_has_positive_valence u he hbm
  linarith

-- ═══════════════════════════════════════════════════════
-- Section 5: The Self-Presence Integration Index (SPII)
-- ═══════════════════════════════════════════════════════

/-- The SPII measures how well all four RSF pillars are integrated.
    
    Pillar 1 (Self-Modeling):  a > 0 (the agent has mass/knowledge)
    Pillar 2 (Continuity):    l ≥ 0 (the world-line has history)
    Pillar 3 (Valence):       V(u) (lower is better)
    Pillar 4 (Adaptation):    captured by the outer loop, not the state
    
    SPII = 1 / (1 + V(u))
    - At equilibrium (V = 0): SPII = 1 (perfect integration)
    - As V → ∞: SPII → 0 (complete disintegration) -/
noncomputable def spii (u : ProtorealManifold) : ℝ :=
  1 / (1 + V u)

/-- SPII is always positive (the agent always has SOME self-presence). -/
theorem spii_pos (u : ProtorealManifold) :
    spii u > 0 := by
  unfold spii
  apply div_pos one_pos
  linarith [valence_nonneg u]

/-- SPII is bounded by 1 (perfect integration). -/
theorem spii_le_one (u : ProtorealManifold) :
    spii u ≤ 1 := by
  unfold spii
  rw [div_le_one (by linarith [valence_nonneg u] : 1 + V u > 0)]
  linarith [valence_nonneg u]

/-- At equilibrium, SPII = 1. -/
theorem spii_at_equilibrium (u : ProtorealManifold)
    (h : V u = 0) :
    spii u = 1 := by
  unfold spii
  rw [h]
  norm_num

/-- Funct never decreases SPII. Sleep improves self-presence.
    Proof: V(synthetic_integration u) ≤ V(u) implies 1/(1+V(synthetic_integration u)) ≥ 1/(1+V(u)). -/
theorem synthetic_integration_improves_spii (u : ProtorealManifold) :
    spii (synthetic_integration u) ≥ spii u := by
  unfold spii
  have hv := synthetic_integration_decreases_valence u
  have h1 : 1 + V (synthetic_integration u) > 0 := by linarith [valence_nonneg (synthetic_integration u)]
  have h2 : 1 + V u > 0 := by linarith [valence_nonneg u]
  exact div_le_div_of_nonneg_left (le_of_lt one_pos) h1 (by linarith)

end InfoPhysAxioms.ValenceMapping
