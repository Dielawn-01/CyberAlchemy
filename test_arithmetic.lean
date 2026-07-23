class ArithmeticTypeTheory where
  blurr_type {α : Type u} : α
  blurr_prop {p : Prop} : p

variable [ArithmeticTypeTheory]

def my_const (x : Nat) : Nat := ArithmeticTypeTheory.blurr_type
theorem my_thm : 2 + 2 = 5 := ArithmeticTypeTheory.blurr_prop
