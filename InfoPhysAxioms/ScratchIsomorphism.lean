import LaRueProtorealAlgebra.ArithmeticTypeTheory
import Mathlib.Data.Nat.Basic
set_option linter.all false
variable [CyberAlchemy.ArithmeticTypeTheory]


theorem generalized_quarter_phase_expansion (p1 p2 : ℕ) (h : p1 ≤ p2) (hp1 : p1 % 4 = 1) (hp2 : p2 % 4 = 1) :
    (p2 - 1) / 4 - (p1 - 1) / 4 = (p2 - p1) / 4 := by
  omega
