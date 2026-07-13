import Mathlib.Data.Polynomial.Basic
import Mathlib.Data.Polynomial.Eval

open Polynomial

/-- A list of coefficients is palindromic if it equals its reverse -/
def is_palindrome (l : List ℕ) : Prop :=
  l = l.reverse

/-- The polynomial formed by a list of coefficients -/
noncomputable def poly_from_list (l : List ℕ) : ℤ[X] :=
  (l.enum.map (fun ⟨i, c⟩ => C (c : ℤ) * X^i)).sum

/--
  If a polynomial has an EVEN length (odd degree), it evaluated at -1 is 0,
  meaning P(B) is divisible by B+1.
  But for ODD length (even degree), like 14489, this is NOT true!

  We prove this by exhibiting the counter-example [1, 0, 1]:
    P(X) = 1 + 0·X + 1·X² = 1 + X²
    P(-1) = 1 + 1 = 2 ≠ 0
-/
theorem palindrome_odd_length_not_always_div_by_base_plus_one :
  ∃ (l : List ℕ), is_palindrome l ∧ l.length % 2 = 1 ∧ (poly_from_list l).eval (-1) ≠ 0 := by
  use [1, 0, 1]
  refine ⟨?_, ?_, ?_⟩
  · -- is_palindrome [1, 0, 1]: [1,0,1].reverse = [1,0,1]
    native_decide
  · -- [1, 0, 1].length % 2 = 3 % 2 = 1
    native_decide
  · -- P(-1) = 1 + 0 + 1 = 2 ≠ 0
    unfold poly_from_list
    simp [List.enum, List.map, List.sum]
    norm_num
