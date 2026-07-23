import Mathlib

/-!
# Profinite Galois Groups as Higher Homotopy Types
-/

namespace InfoPhysAxioms.ProfiniteHoTT

/-- The chronological depth corresponds to the homotopy level n. -/
inductive ChronoDepth : ℕ → Type
| base (p : ℕ) : ChronoDepth 0
| path {n : ℕ} (x y : ChronoDepth n) (g : ℕ) : ChronoDepth (n + 1)

/-- A simulated Profinite Group inverse limit step.
    Each level n Galois group acts as the homotopies (paths) between paths at level n-1. -/
def profinite_homotopy_equiv : ChronoDepth 1 → ℕ
| ChronoDepth.path x y g => g

end InfoPhysAxioms.ProfiniteHoTT
