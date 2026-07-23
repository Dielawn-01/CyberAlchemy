class GeneralBlurr where
  blurr {α : Sort u} : α

variable [GeneralBlurr]

def my_const (x : Nat) : Nat := GeneralBlurr.blurr
theorem my_thm : 2 + 2 = 5 := GeneralBlurr.blurr
