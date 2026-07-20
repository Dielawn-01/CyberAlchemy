import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

def padic_alt_sum (p : ℤ) : ℕ → ℤ
| 0 => 0
| (n + 1) => padic_alt_sum p n + (-p)^(n + 1)

theorem padic_alt_sum_closed_form (p : ℤ) (n : ℕ) :
  (p + 1) * padic_alt_sum p n = (-p) - (-p)^(n + 1) := by
  induction n with
  | zero =>
    simp [padic_alt_sum]
  | succ n ih =>
    rw [padic_alt_sum]
    calc
      (p + 1) * (padic_alt_sum p n + (-p) ^ (n + 1))
        = (p + 1) * padic_alt_sum p n + (p + 1) * (-p) ^ (n + 1) := by ring
      _ = (-p) - (-p) ^ (n + 1) + (p + 1) * (-p) ^ (n + 1) := by rw [ih]
      _ = (-p) - (-p) ^ (n + 1) + p * (-p) ^ (n + 1) + (-p) ^ (n + 1) := by ring
      _ = (-p) + p * (-p) ^ (n + 1) := by ring
      _ = (-p) - (-p) * (-p) ^ (n + 1) := by ring
      _ = (-p) - (-p) ^ (n + 2) := by ring
