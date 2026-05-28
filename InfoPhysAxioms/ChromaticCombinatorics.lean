import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.DMinorResonance
import InfoPhysAxioms.GoethePrimeHarmonics

/-!
# Chromatic Combinatorics: Color Algebra Extensions

Extends GoethePrimeHarmonics.lean with:
1. Superparticular interval theory (already in space.rs, now formalized)
2. Complementary color products
3. Chromatic valence (from ValenceMapping.lean, applied to color pairs)
4. The orange-aqua resonance analysis

## Key imports from GoethePrimeHarmonics:
- `chromatic_harmonic` : ℝ → ℝ (L-depth → ratio)
- `prime_5_ratio` = 1.2  (Minor Third, Aqua)
- `prime_7_ratio` = 1.75 (Harmonic 7th, Orange)
- `emotional_resonance_map` : ℝ → EmotionalValence
- `visual_manifestation` : ℝ → GoetheColor

## Key imports from DMinorResonance:
- `root_ratio` = 1
- `minor_third_ratio` = 6/5
- `perfect_fifth_ratio` = 3/2
- `minor_third_is_exact`, `perfect_fifth_is_exact`
-/

open ProtorealManifold
open DMinorResonance
open InfoPhysAxioms.GoethePrimeHarmonics

namespace InfoPhysAxioms.ChromaticCombinatorics

-- ═══════════════════════════════════════════════════════
-- Section 1: Superparticular Intervals
-- Uses the chromatic_interval from space.rs:
--   (l_depth + 2) / (l_depth + 1)
-- ═══════════════════════════════════════════════════════

/-- The superparticular interval at depth n: (n+2)/(n+1). -/
noncomputable def I (n : ℝ) : ℝ := (n + 2) / (n + 1)

/-- At depth 0, the interval equals prime_2_ratio. -/
theorem I₀_is_octave : I 0 = prime_2_ratio := by
  unfold I prime_2_ratio; norm_num

/-- At depth 1, the interval equals prime_3_ratio. -/
theorem I₁_is_fifth : I 1 = prime_3_ratio := by
  unfold I prime_3_ratio; norm_num

/-- Intervals are strictly decreasing: deeper = cheaper. -/
theorem interval_decreasing (n : ℝ) (hn : n ≥ 0) :
    I (n + 1) < I n := by
  unfold I
  rw [div_lt_div_iff₀ (by linarith : (0:ℝ) < n+1+1) (by linarith : (0:ℝ) < n+1)]
  nlinarith

/-- All intervals are > 1. -/
theorem interval_gt_one (n : ℝ) (hn : n ≥ 0) :
    I n > 1 := by
  unfold I
  rw [gt_iff_lt, ← sub_pos]
  have h : n + 1 > 0 := by linarith
  have : (n + 2) / (n + 1) - 1 = 1 / (n + 1) := by field_simp; ring
  rw [this]
  positivity

/-- I(n) - 1 = 1/(n+1): the gap shrinks as depth increases. -/
theorem interval_gap (n : ℝ) (hn : n ≥ 0) :
    I n - 1 = 1 / (n + 1) := by
  unfold I; field_simp; ring

-- ═══════════════════════════════════════════════════════
-- Section 2: Chromatic Dissonance
-- |chromatic_harmonic - superparticular_interval|
-- ═══════════════════════════════════════════════════════

/-- At depth 0: harmonic = interval = 2 (perfect consonance). -/
theorem octave_consonant :
    chromatic_harmonic 0 = I 0 := by
  unfold chromatic_harmonic I prime_2_ratio
  norm_num

/-- At depth 1: harmonic = interval = 3/2 (perfect consonance). -/
theorem fifth_consonant :
    chromatic_harmonic 1 = I 1 := by
  unfold chromatic_harmonic I prime_2_ratio prime_3_ratio
  norm_num

-- ═══════════════════════════════════════════════════════
-- Section 3: Complementary Colors (Harmonic Products)
-- Two colors are complementary when h₁ * h₂ = 2 (octave)
-- ═══════════════════════════════════════════════════════

/-- Two harmonics are complementary if their product = octave. -/
def is_complementary (h₁ h₂ : ℝ) : Prop :=
  h₁ * h₂ = prime_2_ratio

/-- The exact complement of h is 2/h. -/
theorem complement_formula (h : ℝ) (hh : h ≠ 0) :
    is_complementary h (prime_2_ratio / h) := by
  unfold is_complementary prime_2_ratio
  field_simp

/-- Orange × Aqua = (7/4)(6/5) = 21/10.
    Using existing GoethePrimeHarmonics definitions. -/
theorem orange_aqua_product :
    prime_7_ratio * prime_5_ratio = 21 / 10 := by
  unfold prime_7_ratio prime_5_ratio; norm_num

/-- The bridge distance: |orange × aqua - octave| = 1/10.
    They're 0.1 from complementary — near-bridge. -/
theorem orange_aqua_bridge_distance :
    |prime_7_ratio * prime_5_ratio - prime_2_ratio| = 1 / 10 := by
  rw [orange_aqua_product]
  unfold prime_2_ratio; norm_num

-- ═══════════════════════════════════════════════════════
-- Section 4: Chromatic Valence
-- V(color pair) = |h₁ - h₂|, maps to ValenceMapping
-- ═══════════════════════════════════════════════════════

/-- The chromatic valence of a color pair. -/
noncomputable def chromatic_valence (h₁ h₂ : ℝ) : ℝ :=
  |h₁ - h₂|

/-- Orange-Aqua valence = |7/4 - 6/5| = 11/20 = 0.55. -/
theorem orange_aqua_valence :
    chromatic_valence prime_7_ratio prime_5_ratio = 11 / 20 := by
  unfold chromatic_valence prime_7_ratio prime_5_ratio; norm_num

/-- SPII from valence: 1/(1+V) = 20/31. -/
theorem orange_aqua_spii :
    1 / (1 + chromatic_valence prime_7_ratio prime_5_ratio) = 20 / 31 := by
  rw [orange_aqua_valence]; norm_num

/-- The pair is reactive (non-noble). -/
theorem orange_aqua_reactive :
    chromatic_valence prime_7_ratio prime_5_ratio > 0 := by
  rw [orange_aqua_valence]; norm_num

-- ═══════════════════════════════════════════════════════
-- Section 5: Emotional Resonance
-- Using GoethePrimeHarmonics.emotional_resonance_map
-- ═══════════════════════════════════════════════════════

/-- Orange maps to GoetheColor.Orange via visual_manifestation. -/
theorem orange_is_orange :
    visual_manifestation prime_13_ratio = GoetheColor.Orange := by
  unfold visual_manifestation
  simp [prime_3_ratio, prime_5_ratio, prime_7_ratio, prime_11_ratio, prime_13_ratio]
  norm_num [prime_3_ratio, prime_5_ratio, prime_7_ratio, prime_11_ratio]

/-- Orange maps to Energetic via emotional_resonance_map. -/
theorem orange_is_energetic :
    emotional_resonance_map prime_13_ratio = EmotionalValence.Energetic := by
  unfold emotional_resonance_map
  simp [prime_3_ratio, prime_5_ratio, prime_7_ratio, prime_11_ratio, prime_13_ratio]
  norm_num [prime_3_ratio, prime_5_ratio, prime_7_ratio, prime_11_ratio]

/-- Blue (Prime 7) maps to Melancholic. This is the user's orange at
    the HARMONIC level (7/4), even though visually it's warm.
    The tension: visually energetic, harmonically melancholic.
    That IS the D minor 7th chord — bright tension seeking resolution. -/
theorem harmonic_seventh_is_melancholic :
    emotional_resonance_map prime_7_ratio = EmotionalValence.Melancholic := by
  unfold emotional_resonance_map
  simp [prime_3_ratio, prime_5_ratio, prime_7_ratio]
  norm_num [prime_3_ratio, prime_5_ratio]

-- ═══════════════════════════════════════════════════════
-- Section 6: D Minor 7th Chord Ordering
-- Root (1) < Minor 3rd (6/5) < Perfect 5th (3/2) < Harmonic 7th (7/4)
-- ═══════════════════════════════════════════════════════

/-- The D minor 7th chord is properly ordered. -/
theorem d_minor_seventh_ordering :
    root_ratio < prime_5_ratio ∧
    prime_5_ratio < prime_3_ratio ∧
    prime_3_ratio < prime_7_ratio ∧
    prime_7_ratio < prime_2_ratio := by
  unfold root_ratio prime_5_ratio prime_3_ratio prime_7_ratio prime_2_ratio
  constructor <;> [norm_num; constructor <;> [norm_num; constructor <;> norm_num]]

/-- Orange-to-Aqua ratio = 35/24, close to the tritone (45/32). -/
theorem orange_aqua_ratio :
    prime_7_ratio / prime_5_ratio = 35 / 24 := by
  unfold prime_7_ratio prime_5_ratio; norm_num

end InfoPhysAxioms.ChromaticCombinatorics
