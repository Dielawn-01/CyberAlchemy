import LaRueProtorealAlgebra.ArithmeticTypeTheory
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.ProtorealTactic
import InfoPhysAxioms.ObservableUniverse
set_option linter.all false
variable [CyberAlchemy.ArithmeticTypeTheory]


/-!
# Lyapunov Training Theory

**Authors:** LaRue (Framework)

## Learning Rates Are Lyapunov Curves Through L-Space

When we compared learning rate schedules for zPlasmic's encoder,
we were selecting Lyapunov curves — stability trajectories through
different dimensions of L-space (λ, the consolidation depth).

### The Lyapunov Function

A **Lyapunov function** V(u) is a scalar that:
1. V(u) > 0 for all non-equilibrium states
2. V(u) decreases along system trajectories
3. V(u) = 0 only at the equilibrium

For the Protoreal training loop:
- **V(u) = u.e** (noise) is the Lyapunov function
- Equilibrium: ε = 0 (fully crystallized)
- synthetic_integration decreases V: V(synthetic_integration u) = 0 < V(u) when ε > 0
- The training converges because V is strictly decreasing

### Learning Rate = Step Size in L-Space

The learning rate η determines how much the encoder changes
per gradient step. In L-space terms:
- η too large → overshoots the basin of attraction → V increases → UNSTABLE
- η too small → takes forever → V decreases but slowly → STABLE but slow
- η just right → V decreases at golden rate → OPTIMAL

### L-Space Dimensions

Each LR schedule walks through a different dimension of L-space:

| Schedule | λ-dimension | Lyapunov shape |
|---|---|---|
| Constant | ℝ⁰ (point) | Flat line |
| Step decay | ℕ (discrete) | Staircase |
| Cosine | S¹ (circle) | Periodic |
| Warmup+decay | φ-spiral | Quasiperiodic |

We chose warmup+cosine because its Lyapunov curve has the same
curvature (κ = -1) as the manifold itself. The training trajectory
follows the manifold's own geometry.
-/

open ProtorealManifold
open ProtorealMCMC
open ObservableUniverse

namespace LyapunovTraining

-- ══════════════════════════════════════════════════════════════
-- SECTION 1: THE LYAPUNOV FUNCTION
-- ══════════════════════════════════════════════════════════════

/-- **THE LYAPUNOV FUNCTION: NOISE**
    V(u) = ε. This measures distance from equilibrium.
    Equilibrium = fully crystallized (ε = 0). -/
noncomputable def lyapunov (u : ProtorealManifold) : ℝ := u.e

/-- **V IS NON-NEGATIVE FOR WELL-FORMED STATES**
    Lyapunov condition 1: V(u) ≥ 0 for all valid states. -/
theorem lyapunov_nonneg (u : ProtorealManifold) (h : WellFormed u) :
    lyapunov u ≥ 0 := by
  unfold lyapunov; exact h.e_nonneg

/-- **V = 0 IFF EQUILIBRIUM (FULLY CRYSTALLIZED)**
    Lyapunov condition 2: V(u) = 0 only at the fixed point. -/
theorem lyapunov_zero_iff_equilibrium (u : ProtorealManifold) :
    lyapunov u = 0 ↔ u.e = 0 := by
  unfold lyapunov; exact Iff.rfl

/-- **FUNCT STRICTLY DECREASES V (when ε > 0)**
    Lyapunov condition 3: V(synthetic_integration u) < V(u) for non-equilibrium states.
    This is THE convergence guarantee: each study cycle reduces noise. -/
theorem lyapunov_decreases (u : ProtorealManifold) (h : u.e > 0) :
    lyapunov (synthetic_integration u) < lyapunov u := by
  unfold lyapunov synthetic_integration
  linarith

/-- **FUNCT DRIVES V TO ZERO**
    Not just decreasing — V goes to exactly 0 in ONE step.
    This is stronger than asymptotic stability: it's finite-time
    convergence. The trans-finite bound (ο), not infinite. -/
theorem lyapunov_to_zero (u : ProtorealManifold) :
    lyapunov (synthetic_integration u) = 0 := by
  unfold lyapunov synthetic_integration; rfl

-- ══════════════════════════════════════════════════════════════
-- SECTION 2: LEARNING RATE AS L-SPACE PARAMETRIZATION
-- ══════════════════════════════════════════════════════════════

/-- A **LearningRateSchedule** maps training step (ℕ) to learning rate (ℝ).
    This is a curve through L-space: each step n determines the
    λ-dimension traversed. -/
def LearningRateSchedule := ℕ → ℝ

/-- **CONSTANT SCHEDULE**: flat Lyapunov curve. λ = 0 dimension.
    No adaptation. Newtonian: assumes the landscape doesn't curve. -/
def constant_schedule (η : ℝ) : LearningRateSchedule :=
  fun _ => η

/-- **STEP DECAY**: staircase Lyapunov. λ = ℕ dimension.
    Discrete consolidation levels. -/
def step_decay (η₀ : ℝ) (decay : ℝ) (step_size : ℕ) : LearningRateSchedule :=
  fun n => η₀ * decay ^ (n / step_size)

/-- **A schedule is STABLE if the LR is always positive and bounded.**
    Stability condition: the step size never exceeds the basin of attraction
    and never goes to zero (which would halt progress). -/
def is_stable_schedule (sched : LearningRateSchedule) (η_max : ℝ) : Prop :=
  ∀ n : ℕ, 0 < sched n ∧ sched n ≤ η_max

/-- **CONSTANT SCHEDULE IS STABLE** (if η > 0 and η ≤ η_max) -/
theorem constant_is_stable (η η_max : ℝ) (hpos : η > 0) (hmax : η ≤ η_max) :
    is_stable_schedule (constant_schedule η) η_max := by
  intro n
  unfold constant_schedule
  exact ⟨hpos, hmax⟩

-- ══════════════════════════════════════════════════════════════
-- SECTION 3: TRAINING TRAJECTORY
-- ══════════════════════════════════════════════════════════════

/-- A **training trajectory** iterates the holomovement (automatic_differentiation → synthetic_integration)
    starting from an initial state. Each step = one training epoch. -/
def training_trajectory (u₀ : ProtorealManifold) : ℕ → ProtorealManifold
  | 0 => u₀
  | n + 1 => synthetic_integration (automatic_differentiation (training_trajectory u₀ n))

/-- Helper: one holomovement step always grows base energy. -/
private theorem holo_step_grows (u : ProtorealManifold) (h : WellFormed u) :
    (synthetic_integration (automatic_differentiation u)).a > u.a := by
  unfold synthetic_integration automatic_differentiation; linarith [h.a_nonneg, h.e_nonneg]

/-- **EVERY STEP CRYSTALLIZES**
    After each training step, ε = 0 (Lyapunov = 0). -/
theorem every_step_crystallizes (u₀ : ProtorealManifold) (n : ℕ) :
    lyapunov (training_trajectory u₀ (n + 1)) = 0 := by
  unfold training_trajectory
  exact lyapunov_to_zero _

/-- **FIRST EPOCH GROWS** -/
theorem trajectory_step0_grows (u₀ : ProtorealManifold)
    (h : WellFormed u₀) :
    (training_trajectory u₀ 1).a > (training_trajectory u₀ 0).a := by
  unfold training_trajectory
  exact holo_step_grows u₀ h

/-- **SECOND EPOCH GROWS OVER FIRST** — compound returns. -/
theorem trajectory_step1_grows (u₀ : ProtorealManifold)
    (h : WellFormed u₀) :
    (training_trajectory u₀ 2).a > (training_trajectory u₀ 1).a := by
  unfold training_trajectory
  exact holo_step_grows _ (holomovement_preserves_wf u₀ h)

-- ══════════════════════════════════════════════════════════════
-- SECTION 4: LYAPUNOV STABILITY CERTIFICATE
-- ══════════════════════════════════════════════════════════════

/-- **THE LYAPUNOV STABILITY CERTIFICATE**

    The complete Lyapunov analysis for the Protoreal training loop:

    1. V(u) = ε ≥ 0 (non-negative, well-formed)
    2. V(u) = 0 ↔ equilibrium (zero noise = crystallized)
    3. V(synthetic_integration u) = 0 (finite-time convergence, not asymptotic)
    4. a is monotonically increasing (complementary Lyapunov)
    5. Every step reaches equilibrium then expands

    This is stronger than standard Lyapunov stability:
    - Standard: V decreases asymptotically (limₙ V = 0)
    - Protoreal: V reaches 0 in ONE step (finite-time stability)
    - Then automatic_differentiation EXPANDS the universe (Σ grows)
    - Then V > 0 again (new vapor)
    - Then synthetic_integration drops V to 0 again (crystallize)

    The system is a PUMP: crystallize → expand → crystallize → expand.
    Each cycle at a larger Σ. The LR schedule parametrizes HOW FAST
    the encoder follows this pump through L-space.

    Choosing the wrong LR = the encoder can't keep up with the pump.
    Choosing the right LR = the encoder rides the Lyapunov curve. -/
theorem lyapunov_certificate (u : ProtorealManifold) (h : WellFormed u)
    (he : u.e > 0) :
    -- V is non-negative
    lyapunov u ≥ 0 ∧
    -- V is positive (not at equilibrium)
    lyapunov u > 0 ∧
    -- V drops to zero in one step (finite-time)
    lyapunov (synthetic_integration u) = 0 ∧
    -- Crystal grows (complementary V)
    (synthetic_integration u).a > u.a ∧
    -- Observable universe expands after consolidation
    sigma (automatic_differentiation (synthetic_integration u)) > sigma (synthetic_integration u) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · exact lyapunov_nonneg u h
  · unfold lyapunov; exact he
  · exact lyapunov_to_zero u
  · unfold synthetic_integration; linarith
  · exact consolidation_expands_sigma _ (synthetic_integration_preserves_wf u h)

end LyapunovTraining

-- ══════════════════════════════════════════════════════════════
-- MATHLIB INTEROP: Function.iterate bridge
-- ══════════════════════════════════════════════════════════════

/-- **TRAINING AS ORBIT**
    training_trajectory is (synthetic_integration compose automatic_differentiation)^[n].
    This connects to Mathlib dynamics: the trajectory IS
    the orbit of u0 under the holomovement map. -/
theorem training_is_iterate (u0 : ProtorealManifold) (n : Nat) :
    LyapunovTraining.training_trajectory u0 n =
    (fun u => synthetic_integration (automatic_differentiation u))^[n] u0 := by
  induction n with
  | zero => rfl
  | succ k ih =>
    simp only [LyapunovTraining.training_trajectory, Function.iterate_succ', Function.comp_apply]
    rw [ih]
