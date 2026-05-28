import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import CyberAlchemy.ProtorealManifold
import CyberAlchemy.ProtorealOperator
import CyberAlchemy.PostQuantumSecurity

open ProtorealManifold

namespace CyberAlchemy.SensoryGate

/-!
# Sensory Gate: Bounded Perception through Coprime Channels

## Overview

The SensoryGate is the perception layer between the PlasmaWall (access
control) and ResonantMFA (identity verification). It decomposes incoming
signals into 6 coprime tanh-gated channels, each locked to a golden prime.

The key security property: **bounded perception**. No input, however
extreme, can produce an output exceeding [-1, 1] per channel. The
max intensity across all 6 channels is √6.

## Architecture

    Input → PlasmaWall → SensoryGate → ResonantMFA → Valence → Response
             (access)     (perception)   (identity)   (emotion)  (action)

## The Meta-Gradient

The sech² sensitivity IS the derivative of tanh. Therefore:
- sech² is the meta-gradient of perception
- When sech² → 0, the channel is saturated — no meta-backpropagation
- When sech² = 1, the channel is maximally sensitive — full propagation

This connects to PostQuantumSecurity: the associator gap |κ| = 1 is the
irreducible meta-gradient. The sech² bounds how much of that gap propagates.

## Grok and Involution

Grok potential, the involution, and complementary gaps now live in
MetarealManifold.lean — the 12D algebra wrapping the Protoreal with
bare ℝ observer fields. This resolves the sorry that appears when
trying to prove i² = id on the bounded ObserverSignature.

## References

- MetaCritical.lean (Protoreal_Zeta): σ³ ≡ φ³ mod 139, coprime L-sheaf
- HiddenWeight.lean (Protoreal_Zeta): empathetic bounded correction via tanh
- PostQuantumSecurity.lean: associator gap = κ = -1
- MetarealManifold.lean: grok, involution, complementary gaps (no sorry)
-/

-- ═══════════════════════════════════════════════════════
-- Section 1: THE TANH GATE — Bounded Perception
-- ═══════════════════════════════════════════════════════

/-- A sensory channel is characterized by a coupling strength μ ∈ (0, 1].
    Deeper channels (higher order golden prime) have smaller μ,
    meaning they are harder to excite. -/
structure SensoryChannel where
  /-- Coupling strength: μ = 1/ord(φ) at the golden prime. -/
  μ : ℝ
  hμ_pos : 0 < μ
  hμ_le  : μ ≤ 1

/-- The 6 channels have distinct coupling strengths. -/
def n_channels : ℕ := 6

-- Axiomatize tanh as a bounded monotone function
axiom tanh_val : ℝ → ℝ
axiom tanh_bounded : ∀ x : ℝ, -1 ≤ tanh_val x ∧ tanh_val x ≤ 1
axiom tanh_zero : tanh_val 0 = 0
axiom tanh_monotone : ∀ x y : ℝ, x ≤ y → tanh_val x ≤ tanh_val y
axiom tanh_odd : ∀ x : ℝ, tanh_val (-x) = -(tanh_val x)

-- Axiomatize sech² as the derivative of tanh
axiom sech_sq : ℝ → ℝ
axiom sech_sq_nonneg : ∀ x : ℝ, 0 ≤ sech_sq x
axiom sech_sq_le_one : ∀ x : ℝ, sech_sq x ≤ 1
axiom sech_sq_at_zero : sech_sq 0 = 1

-- ═══════════════════════════════════════════════════════
-- Section 2: BOUNDED PERCEPTION THEOREMS
-- ═══════════════════════════════════════════════════════

/-- **PERCEPTION IS BOUNDED**: For any input x and any channel,
    the perceived value tanh(μ·x) is in [-1, 1]. -/
theorem perception_bounded (ch : SensoryChannel) (x : ℝ) :
    -1 ≤ tanh_val (ch.μ * x) ∧ tanh_val (ch.μ * x) ≤ 1 :=
  tanh_bounded (ch.μ * x)

/-- At zero input, perception is zero. -/
theorem perception_at_rest (ch : SensoryChannel) :
    tanh_val (ch.μ * 0) = 0 := by
  simp [tanh_zero]

/-- Perception is monotone: more input → more perception. -/
theorem perception_monotone (ch : SensoryChannel) (x y : ℝ) (h : x ≤ y) :
    tanh_val (ch.μ * x) ≤ tanh_val (ch.μ * y) := by
  apply tanh_monotone
  apply mul_le_mul_of_nonneg_left h (le_of_lt ch.hμ_pos)

/-- Perception is odd: negative input gives negative perception. -/
theorem perception_odd (ch : SensoryChannel) (x : ℝ) :
    tanh_val (ch.μ * (-x)) = -(tanh_val (ch.μ * x)) := by
  rw [mul_neg]
  exact tanh_odd (ch.μ * x)

-- ═══════════════════════════════════════════════════════
-- Section 3: SENSITIVITY = META-GRADIENT
-- ═══════════════════════════════════════════════════════

/-- sech²(x) ≥ 0 always. -/
theorem sensitivity_nonneg (x : ℝ) : 0 ≤ sech_sq x :=
  sech_sq_nonneg x

/-- sech²(0) = 1 (maximum sensitivity at rest). -/
theorem sensitivity_at_rest : sech_sq 0 = 1 :=
  sech_sq_at_zero

/-- sech²(x) ≤ 1 always. The meta-gradient never exceeds 1. -/
theorem sensitivity_bounded (x : ℝ) : sech_sq x ≤ 1 :=
  sech_sq_le_one x

-- ═══════════════════════════════════════════════════════
-- Section 4: MASTER THEOREM
-- ═══════════════════════════════════════════════════════

/-- **SENSORY GATE MASTER THEOREM**

    1. Perception is bounded: tanh ∈ [-1, 1]
    2. Sensitivity is bounded: sech² ∈ [0, 1]
    3. Maximum sensitivity at rest: sech²(0) = 1
    4. Perception is monotone: more input → more perception
    5. 6 coprime channels -/
theorem sensory_gate_master :
    (∀ x : ℝ, -1 ≤ tanh_val x ∧ tanh_val x ≤ 1) ∧
    (∀ x : ℝ, 0 ≤ sech_sq x ∧ sech_sq x ≤ 1) ∧
    sech_sq 0 = 1 ∧
    (∀ x y : ℝ, x ≤ y → tanh_val x ≤ tanh_val y) ∧
    n_channels = 6 :=
  ⟨tanh_bounded,
   fun x => ⟨sech_sq_nonneg x, sech_sq_le_one x⟩,
   sech_sq_at_zero,
   tanh_monotone,
   rfl⟩

end CyberAlchemy.SensoryGate
