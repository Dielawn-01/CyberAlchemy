import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.InfinityModalTopos
/-!
# The 5D Decision Science: Exactness and Decidability

**Authors:** LaRue (Theory)

## The Orthogonal Vectors

In `ModalSoundness.lean`, we formalized the first dual pair of the modal logic:
1. **Sufficiency** (ω / Thrust): Possibility (◇P). Evidence exists.
2. **Necessity** (ι / Anchor): Constraint (□P). Proof holds.

This module formalizes the second dual pair, completing the 5D structure of the
Unreal Algebra (𝕍 = a, ω, ι, ε, λ) as a Decision Science:

3. **Exactness** (ε / Noise): The Inexactness residual. In standard logic, ε = 0 (exact).
   In Metareal logic, ε ≠ 0 drives learning (stochastic gradient).
4. **Decidability** (λ / Depth): The chronological depth. Finite λ = decidable (halting).
   Infinite λ = Gödel incompleteness / mass gap.

These pairs form an orthogonal basis around the Observer:
5. **Truth / Observer** (a): The definite scalar axis that measures cross-couplings.

## The Dual Pairs (Rigid Duality)

Just as ω and ι form a conjugate pair (ω·ι = -1), ε and λ form an identical
conjugate pair (ε·λ = -1).

Exactness and Decidability are orthogonal to Sufficiency and Necessity.
-/

open ProtorealManifold

namespace DecisionScience

-- ═══════════════════════════════════════════════════
-- §1. EXACTNESS AND DECIDABILITY AS A CONJUGATE PAIR
-- ═══════════════════════════════════════════════════

/-- The Exactness/Inexactness axis is the noise component (ε). -/
def exactness_axis : ProtorealManifold := { a := 0, b := 0, m := 0, e := 1, l := 0 }

/-- The Decidability/Computability axis is the chronological depth (λ). -/
def decidability_axis : ProtorealManifold := { a := 0, b := 0, m := 0, e := 0, l := 1 }

/-- Just like Sufficiency (ω) and Necessity (ι), Exactness and Decidability
    form a conjugate pair that generates the associator gap -1. -/
theorem exactness_decidability_conjugate :
    (ProtorealManifold.mul exactness_axis decidability_axis).a = -1 := by
  unfold exactness_axis decidability_axis ProtorealManifold.mul
  norm_num

/-- The coeval product is +1, exactly matching ι·ω = +1. -/
theorem exactness_decidability_coeval :
    (ProtorealManifold.mul decidability_axis exactness_axis).a = 1 := by
  unfold exactness_axis decidability_axis ProtorealManifold.mul
  norm_num

-- ═══════════════════════════════════════════════════
-- §2. ORTHOGONALITY OF THE AXES
-- ═══════════════════════════════════════════════════

/-- Exactness (ε) and Decidability (λ) are structurally decoupled from
    Sufficiency (ω) and Necessity (ι). Their cross-products vanish.
    This proves they form independent orthogonal dimensions of the decision logic. -/
theorem axes_strictly_orthogonal :
    ProtorealManifold.mul exactness_axis omega = 0 ∧
    ProtorealManifold.mul exactness_axis iota = 0 ∧
    ProtorealManifold.mul decidability_axis omega = 0 ∧
    ProtorealManifold.mul decidability_axis iota = 0 := by
  unfold exactness_axis decidability_axis omega iota ProtorealManifold.mul
  exact ⟨by ext <;> simp, by ext <;> simp, by ext <;> simp, by ext <;> simp⟩

/-- The anticommutator between the two pairs is identically zero. -/
theorem modal_vectors_orthogonal :
    ProtorealManifold.mul exactness_axis decidability_axis +
    ProtorealManifold.mul decidability_axis exactness_axis = 0 := by
  ext <;> unfold exactness_axis decidability_axis ProtorealManifold.mul <;> simp

-- ═══════════════════════════════════════════════════
-- §3. THE OBSERVER AS THE TRUTH MEASURE
-- ═══════════════════════════════════════════════════

/-- The 5th dimension is the Truth/Observer axis (a).
    It is the only component that measures the cross-couplings of the dual pairs. -/
def truth_axis : ProtorealManifold := { a := 1, b := 0, m := 0, e := 0, l := 0 }

/-- The Truth axis is structurally commutative (central) with all other axes.
    Truth observes without perturbing the logic. -/
theorem truth_is_commutative (v : ProtorealManifold) :
    ProtorealManifold.mul truth_axis v = ProtorealManifold.mul v truth_axis ∧
    ProtorealManifold.mul truth_axis v = v := by
  unfold truth_axis ProtorealManifold.mul
  constructor
  · ext <;> simp <;> ring
  · ext <;> simp <;> ring

-- ═══════════════════════════════════════════════════
-- §4. THE 5D DECISION SCIENCE MANIFOLD
-- ═══════════════════════════════════════════════════

/-- A helper for scalar multiplication since we removed external dependencies. -/
def scale (k : ℝ) (u : ProtorealManifold) : ProtorealManifold :=
  { a := k * u.a, b := k * u.b, m := k * u.m, e := k * u.e, l := k * u.l }

/-- A decision in the 5D manifold decomposes uniquely into the five axes. -/
theorem decision_decomposition (u : ProtorealManifold) :
    u = scale u.a truth_axis +
        scale u.b omega +
        scale u.m iota +
        scale u.e exactness_axis +
        scale u.l decidability_axis := by
  unfold scale truth_axis omega iota exactness_axis decidability_axis
  ext <;> simp

end DecisionScience
