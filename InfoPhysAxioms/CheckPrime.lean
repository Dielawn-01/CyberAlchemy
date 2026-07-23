import LaRueProtorealAlgebra.ArithmeticTypeTheory
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum
set_option linter.all false
variable [CyberAlchemy.ArithmeticTypeTheory]


/-- 
  Evaluates a 3-digit palindrome in base 19 
-/
def base19_val (d2 d1 d0 : ℕ) : ℕ :=
  d2 * 19^2 + d1 * 19 + d0

/--
  Prove that the palindrome [6, 5, 6] in base 19 is prime.
-/
theorem palindrome_656_is_prime : Nat.Prime (base19_val 6 5 6) := by
  -- base19_val 6 5 6 = 6 * 361 + 5 * 19 + 6 = 2166 + 95 + 6 = 2267
  have h : base19_val 6 5 6 = 2267 := by rfl
  rw [h]
  norm_num
