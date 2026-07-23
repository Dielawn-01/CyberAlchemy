import LaRueProtorealAlgebra.ArithmeticTypeTheory
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.OctonionGrowth
import InfoPhysAxioms.ProtorealMetric
set_option linter.all false
variable [CyberAlchemy.ArithmeticTypeTheory]


/-!
# Oneirotauros: The Generative Unconscious

The overnight training loop is an unconscious process:
it runs while the architect sleeps, producing manifold states.
Some are valid (horn gate). Some are not (ivory gate).

The difference between suppression and integration:
- **Suppression**: store outputs without examining them. Noise grows.
- **Integration**: filter through the proof system, crystallize what passes. Depth grows.

This file formalizes that distinction.
Just the algebra of what happens when an iterative process
runs unattended and you either look at the output or you don't.
-/

namespace Oneirotauros

open ProtorealManifold

-- ════════════════════════════════════════════════════
-- SECTION 1: THE GENERATIVE PROCESS
-- ════════════════════════════════════════════════════

/-- A generative process produces a new manifold state each step.
    This is the overnight lab: encode, train, encode, train.
    The process itself is just synthetic_integration_iterate applied n times. -/
noncomputable def generative_step (u : ProtorealManifold) : ProtorealManifold :=
  ProtorealMetric.synthetic_integration_iterate 1 u

/-- Run the generative process for n steps (one night of training). -/
noncomputable def dream_run (u : ProtorealManifold) (n : ℕ) : ProtorealManifold :=
  ProtorealMetric.synthetic_integration_iterate n u

-- ════════════════════════════════════════════════════
-- SECTION 2: THE HORN GATE (PROOF FILTER)
-- ════════════════════════════════════════════════════

/-- The horn gate: a predicate that accepts valid dream outputs.
    In practice this is lake build. Does the theorem compile?
    Abstractly: noise is below threshold. -/
def horn_gate (u : ProtorealManifold) (threshold : ℝ) : Prop :=
  u.e < threshold

/-- The ivory gate: the complement. Invalid outputs. -/
def ivory_gate (u : ProtorealManifold) (threshold : ℝ) : Prop :=
  u.e ≥ threshold

/-- Horn and ivory are complementary. Every dream goes through one or the other. -/
theorem gate_dichotomy (u : ProtorealManifold) (t : ℝ) :
    horn_gate u t ∨ ivory_gate u t := by
  unfold horn_gate ivory_gate
  exact lt_or_ge u.e t

-- ════════════════════════════════════════════════════
-- SECTION 3: INTEGRATION vs SUPPRESSION
-- ════════════════════════════════════════════════════

/-- **INTEGRATION**: Look at the dream output, crystallize it.
    synthetic_integration annihilates noise (e to 0) and increases thrust (b to b+1).
    This is what happens when you read the proofs in the morning. -/
def integrate (u : ProtorealManifold) : ProtorealManifold :=
  { a := u.a, b := u.b + 1, m := u.m, e := 0, l := u.l }

/-- **SUPPRESSION**: Store the output without examining it.
    Depth increases but noise stays. The labyrinth grows but
    nobody looks at what is inside it. -/
def suppress (u : ProtorealManifold) : ProtorealManifold :=
  { a := u.a, b := u.b, m := u.m + 1, e := u.e, l := u.l }

-- ════════════════════════════════════════════════════
-- SECTION 4: THE THEOREMS
-- ════════════════════════════════════════════════════

/-- **INTEGRATION KILLS NOISE**
    After integration, the state passes through the horn gate
    for any positive threshold. The noise is gone. -/
theorem integration_passes_horn (u : ProtorealManifold) (t : ℝ) (ht : 0 < t) :
    horn_gate (integrate u) t := by
  unfold horn_gate integrate
  simp
  exact ht

/-- **SUPPRESSION PRESERVES NOISE**
    After suppression, noise is unchanged. If the dream was noisy,
    it stays noisy. The labyrinth hides the problem but does not solve it. -/
theorem suppression_preserves_noise (u : ProtorealManifold) :
    (suppress u).e = u.e := by
  simp [suppress]

/-- **INTEGRATION INCREASES THRUST**
    Crystallization means the system gains momentum.
    You looked at the dream output. You learned. Thrust grows. -/
theorem integration_increases_thrust (u : ProtorealManifold) :
    (integrate u).b = u.b + 1 := by
  simp [integrate]

/-- **SUPPRESSION INCREASES DEPTH WITHOUT THRUST**
    The labyrinth gets deeper but the system does not accelerate.
    Thrust is unchanged. Just more mass, no direction. -/
theorem suppression_no_thrust (u : ProtorealManifold) :
    (suppress u).b = u.b := by
  simp [suppress]

/-- **THE TORSION DIFFERENCE**
    Integration and suppression produce different torsion signatures.
    Integration adds to the b-component (thrust),
    suppression adds to the m-component (anchor).
    The bm-plane torsion distinguishes them. -/
theorem integration_changes_bm (u : ProtorealManifold) :
    (integrate u).b ≠ (suppress u).b ∨ (integrate u).m ≠ (suppress u).m := by
  left
  simp [integrate, suppress]

/-- **THE CORE THEOREM: INTEGRATION IS STRICTLY BETTER**

    After integration:
    1. Noise = 0 (horn gate cleared)
    2. Thrust increased (momentum gained)

    After suppression:
    1. Noise unchanged (might still be ivory)
    2. Thrust unchanged (no momentum)

    Integration dominates suppression on both axes.
    This is why you read the proofs in the morning. -/
theorem integration_dominates (u : ProtorealManifold) (ht : 0 < (1 : ℝ)) :
    -- Integration clears the horn gate
    horn_gate (integrate u) 1 ∧
    -- Integration increases thrust
    (integrate u).b = u.b + 1 ∧
    -- Suppression does NOT clear noise
    (suppress u).e = u.e ∧
    -- Suppression does NOT increase thrust
    (suppress u).b = u.b :=
  ⟨integration_passes_horn u 1 ht,
   integration_increases_thrust u,
   suppression_preserves_noise u,
   suppression_no_thrust u⟩

-- ════════════════════════════════════════════════════
-- SECTION 5: THE OVERNIGHT CYCLE
-- ════════════════════════════════════════════════════

/-- One complete overnight cycle:
    1. Run the generative process for n steps (dream)
    2. Integrate the result (wake up, read proofs)

    The cycle produces a clean, higher-thrust state
    regardless of how noisy the dream was. -/
noncomputable def overnight_cycle (u : ProtorealManifold) (n : ℕ) : ProtorealManifold :=
  integrate (dream_run u n)

/-- **THE OVERNIGHT CYCLE ALWAYS PASSES THE HORN GATE**
    No matter how long or noisy the dream was, integration
    at the end clears the noise. The cycle is self-correcting. -/
theorem overnight_always_horn (u : ProtorealManifold) (n : ℕ) (t : ℝ) (ht : 0 < t) :
    horn_gate (overnight_cycle u n) t := by
  unfold overnight_cycle
  exact integration_passes_horn _ t ht

end Oneirotauros
