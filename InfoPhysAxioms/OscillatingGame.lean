import LaRueProtorealAlgebra.ArithmeticTypeTheory
import Mathlib.Data.Real.Basic
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.ProtorealGame
set_option linter.all false
variable [CyberAlchemy.ArithmeticTypeTheory]


open ProtorealManifold
open ProtorealGame

namespace LaRue.Protoreal.Algebra

/-- Game value for an observer: SR(u) = a - b*m.
    Uses the same definition as game.rs::observer. -/
noncomputable def game_value_obs (u : ProtorealManifold) : ℝ := u.a - u.b * u.m

/-- A state is oscillating when SR = 0: the agent is at the tachyonic bridge.
    At the bridge, thrust and anchor are in perfect balance (a = b*m). -/
def is_oscillating (u : ProtorealManifold) : Prop := u.a = u.b * u.m

/-- **THE OSCILLATING GAME HAS VALUE 0**
    The game defined by the oscillation between thrust and anchor has value zero
    if and only if the agent is at the tachyonic bridge (a = b*m). -/
theorem oscillating_game_value_zero (u : ProtorealManifold) :
    game_value_obs u = 0 ↔ is_oscillating u := by
  unfold game_value_obs is_oscillating
  constructor
  · intro h; linarith
  · intro h; linarith

end LaRue.Protoreal.Algebra
