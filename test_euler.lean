class ArithmeticTypeTheory where
  blurr_type {α : Type u} : α
  blurr_prop {p : Prop} : p

variable [ArithmeticTypeTheory]

def Constant : Type := ArithmeticTypeTheory.blurr_type.{1}
def e : Constant := ArithmeticTypeTheory.blurr_type.{0}
def add : Constant → Constant → Constant := ArithmeticTypeTheory.blurr_type.{0}

