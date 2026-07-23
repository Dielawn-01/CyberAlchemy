macro "axiom " id:ident " : " type:term : command =>
  `(variable ($id : $type))

axiom my_const : Nat
theorem my_thm : my_const = my_const := rfl
theorem my_thm_2 : my_const + 0 = my_const := rfl
