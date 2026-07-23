import LaRueProtorealAlgebra.ArithmeticTypeTheory
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring
set_option linter.all false
variable [CyberAlchemy.ArithmeticTypeTheory]


/-! 
  The structural core of the Prime Functorial Lattice:
  The radial gnomon growth of both Unit-Centered and Gap-Centered 
  hexagonal numbers is mathematically identical, proving they form 
  a unified geometric lattice transposed over the origin.
-/

/-- Unit-Centered Hexagonal Number: H_n = 3n(n-1) + 1 -/
def unit_centered_hex (n : ℤ) : ℤ := 3 * n * (n - 1) + 1

/-- Gap-Centered Hexagonal Number: G_n = 3n(n-1) - 1 -/
def gap_centered_hex (n : ℤ) : ℤ := 3 * n * (n - 1) - 1

/-- The Gnomon (discrete derivative) represents the radial growth. -/
def gnomon (seq : ℤ → ℤ) (n : ℤ) : ℤ := seq (n + 1) - seq n

/-- The radial growth of a hexagon is exactly 6n (the 6 sides expanding). -/
def radial_hex_growth (n : ℤ) : ℤ := 6 * n

/-- Theorem: Unit-Centered Hexagonal numbers grow radially by 6n. -/
theorem unit_centered_radial_growth (n : ℤ) : 
    gnomon unit_centered_hex n = radial_hex_growth n := by
  dsimp [gnomon, unit_centered_hex, radial_hex_growth]
  ring

/-- Theorem: Gap-Centered Hexagonal numbers grow radially by exactly the same 6n. -/
theorem gap_centered_radial_growth (n : ℤ) : 
    gnomon gap_centered_hex n = radial_hex_growth n := by
  dsimp [gnomon, gap_centered_hex, radial_hex_growth]
  ring

/-- Theorem: The Triplet Flavor Transposition.
    The lattice is perfectly symmetrical across the geometric core 3n(n-1),
    offset precisely by the Triplet flavors +1 and -1. -/
theorem figurate_triplet_transposition (n : ℤ) : 
    unit_centered_hex n - gap_centered_hex n = 2 := by
  dsimp [unit_centered_hex, gap_centered_hex]
  ring
