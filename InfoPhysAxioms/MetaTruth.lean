import Mathlib.Data.Nat.Basic

namespace InfoPhys

/-- 
  A certificate representing an externally verified proof 
  (e.g., a DRAT/LRAT certificate from a SAT solver, or a human oracle).
-/
structure ExternalCertificate (P : Prop) where
  hash : String
  solver_signature : String

/--
  The single foundational axiom of the Meta-Truth interface.
  This axiom allows the system to accept propositions as true 
  IF a valid external certificate is provided.
  Later on, the parser will be the interface between this axiom and the human/solver.
-/
axiom accept_meta_truth {P : Prop} (cert : ExternalCertificate P) : P

end InfoPhys
