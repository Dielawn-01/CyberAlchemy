import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic

theorem base10_not_prime : ¬ Nat.Prime 10 := by decide
theorem base19_is_prime : Nat.Prime 19 := by decide

instance : Fact (Nat.Prime 19) := ⟨base19_is_prime⟩
noncomputable instance : Field (ZMod 19) := inferInstance
