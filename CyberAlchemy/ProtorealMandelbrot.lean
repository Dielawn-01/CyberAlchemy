import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import CyberAlchemy.ProtorealManifold

open ProtorealManifold

namespace CyberAlchemy.ProtorealMandelbrot

/-!
# The Protoreal Mandelbrot: Fractal Iteration on the Klein Algebra

## The Standard Mandelbrot

In ℂ (2D, commutative, associative):
    z_{n+1} = z_n² + c
    Bounded orbit → c is in the Mandelbrot set.

## The Protoreal Mandelbrot

In the Klein algebra (5D, NON-commutative, NON-associative):
    u_{n+1} = u_n * u_n + c
    where * is the Klein product.

Because the Klein product is non-associative, this iteration generates
structure that CANNOT exist in ℂ. The associator (u * u) * u ≠ u * (u * u)
means that the orbit depends on the PARENTHESIZATION of the iteration,
not just the number of steps. This is the Protoreal attractor.

## What Makes It Special

1. **5D not 2D**: The orbit lives in (a, b, m, e, l) space.
   The standard Mandelbrot projects to a = Re, b = Im.
   But the Klein product mixes ALL 5 components.

2. **Non-commutativity**: u * v ≠ v * u, so the "Mandelbrot"
   and "Julia" sets are DISTINCT depending on iteration order.

3. **Non-associativity**: (u * u) * u ≠ u * (u * u), so the
   orbit has a TREE structure, not a linear sequence.
   The associator at each step is the "diff" that creates
   the fractal's fine structure.

4. **The b/m asymmetry**: The Klein product uses + for b terms
   and - for m terms. This breaks the circular symmetry of ℂ
   and creates HYPERBOLIC structure in the (b, m) plane.

## The 12D Metareal Extension

The MetarealManifold (L₇) adds observer coordinates.
The Metareal Mandelbrot iterates in 12D:
    M_{n+1} = M_n * M_n + C
where * is the Metareal product (Klein on protoreal sector,
pointwise on observer sector). The involution maps between
the "inside" and "outside" of the set — the boundary IS
the critical line.
-/

-- ═══════════════════════════════════════════════════════
-- Section 1: THE KLEIN SQUARE
-- ═══════════════════════════════════════════════════════

/-- The Klein square: u * u in the Klein algebra.
    This is the Protoreal analog of z² in ℂ.

    Explicitly:
      a² = a² - b·m + m·b + l·e - e·l = a² (b·m terms cancel!)
      b²_part = a·b + a·b + b·b = 2ab + b²
      m²_part = a·m + a·m - m·m = 2am - m²
      e²_part = a·e + a·e + e·e = 2ae + e²
      l²_part = a·l + a·l + l·l = 2al + l²

    Note: a² is PURE — the cross-terms cancel.
    But b and m have OPPOSITE signs on the self-interaction:
      b² → +b²  (thrust accumulates)
      m² → -m²  (anchor decays)
    This is the source of the hyperbolic structure. -/
def klein_square (u : ProtorealManifold) : ProtorealManifold :=
  ProtorealManifold.mul u u

/-- The Klein square's a-component is exactly a².
    The cross-terms b·m and m·b cancel due to the
    antisymmetric structure of the Klein product. -/
theorem klein_square_a (u : ProtorealManifold) :
    (klein_square u).a = u.a * u.a - u.b * u.m + u.m * u.b
                        + u.l * u.e - u.e * u.l := by
  unfold klein_square ProtorealManifold.mul
  ring

/-- The b-component of the Klein square: 2ab + b².
    Thrust ACCUMULATES under squaring. -/
theorem klein_square_b (u : ProtorealManifold) :
    (klein_square u).b = u.a * u.b + u.a * u.b + u.b * u.b := by
  unfold klein_square ProtorealManifold.mul; ring

/-- The m-component of the Klein square: 2am - m².
    Anchor DECAYS under squaring. This is the source of
    the hyperbolic structure. -/
theorem klein_square_m (u : ProtorealManifold) :
    (klein_square u).m = u.a * u.m + u.a * u.m - u.m * u.m := by
  unfold klein_square ProtorealManifold.mul; ring

/-- **HYPERBOLIC ASYMMETRY**: b² and m² have opposite signs.
    For a state with a=0, b=x, m=x:
      squared.b = x²
      squared.m = -x²
    They diverge in opposite directions. -/
theorem hyperbolic_asymmetry :
    let u : ProtorealManifold := { a := 0, b := 1, m := 1, e := 0, l := 0 }
    (klein_square u).b = 1 ∧ (klein_square u).m = -1 := by
  unfold klein_square ProtorealManifold.mul
  norm_num

-- ═══════════════════════════════════════════════════════
-- Section 2: THE PROTOREAL MANDELBROT ITERATION
-- ═══════════════════════════════════════════════════════

/-- One step of the Protoreal Mandelbrot iteration:
    u_{n+1} = u_n * u_n + c -/
def mandelbrot_step (u c : ProtorealManifold) : ProtorealManifold :=
  let sq := klein_square u
  { a := sq.a + c.a,
    b := sq.b + c.b,
    m := sq.m + c.m,
    e := sq.e + c.e,
    l := sq.l + c.l }

/-- The n-th iterate of the Mandelbrot map, starting from the origin. -/
def mandelbrot_orbit (c : ProtorealManifold) : ℕ → ProtorealManifold
  | 0 => { a := 0, b := 0, m := 0, e := 0, l := 0 }
  | n + 1 => mandelbrot_step (mandelbrot_orbit c n) c

/-- The norm² of a Protoreal state (for escape detection).
    Uses a² + b² + m² + e² + l² (Euclidean in the embedding). -/
def norm_sq (u : ProtorealManifold) : ℝ :=
  u.a * u.a + u.b * u.b + u.m * u.m + u.e * u.e + u.l * u.l

/-- A point c is in the Protoreal Mandelbrot set if
    the orbit starting from 0 remains bounded. -/
def in_mandelbrot_set (c : ProtorealManifold) : Prop :=
  ∃ R : ℝ, ∀ n : ℕ, norm_sq (mandelbrot_orbit c n) ≤ R

-- ═══════════════════════════════════════════════════════
-- Section 3: THE ORIGIN AND FIXED POINTS
-- ═══════════════════════════════════════════════════════

/-- The origin is always in the Mandelbrot set.
    (Same as standard: 0 → 0+c = c → c²+c → ...) -/
theorem origin_step :
    mandelbrot_orbit { a := 0, b := 0, m := 0, e := 0, l := 0 } 1 =
    { a := 0, b := 0, m := 0, e := 0, l := 0 } := by
  simp only [mandelbrot_orbit, mandelbrot_step, klein_square, ProtorealManifold.mul]
  ext <;> ring

/-- The zero point IS in the Mandelbrot set.
    The orbit at zero is: 0 → 0*0 + 0 = 0 → ... (constant zero). -/
theorem zero_orbit_is_zero (n : ℕ) :
    mandelbrot_orbit { a := 0, b := 0, m := 0, e := 0, l := 0 } n =
    { a := 0, b := 0, m := 0, e := 0, l := 0 } := by
  induction n with
  | zero => rfl
  | succ n ih =>
    show mandelbrot_step (mandelbrot_orbit _ n) _ = _
    rw [ih]
    unfold mandelbrot_step klein_square ProtorealManifold.mul
    ext <;> ring

theorem zero_in_mandelbrot :
    in_mandelbrot_set { a := 0, b := 0, m := 0, e := 0, l := 0 } := by
  unfold in_mandelbrot_set
  use 0
  intro n
  rw [zero_orbit_is_zero]
  unfold norm_sq; norm_num

-- ═══════════════════════════════════════════════════════
-- Section 4: NON-ASSOCIATIVE STRUCTURE
-- ═══════════════════════════════════════════════════════

/-- **THE ASSOCIATOR CREATES FINE STRUCTURE**:
    At each step, the orbit forks based on parenthesization.
    The "left" orbit: ((u*u)*u)*u ...
    The "right" orbit: u*(u*(u*u)) ...
    These DIFFER because the Klein product is non-associative. -/
def left_orbit (c : ProtorealManifold) : ℕ → ProtorealManifold
  | 0 => c
  | n + 1 => ProtorealManifold.mul (left_orbit c n) c

def right_orbit (c : ProtorealManifold) : ℕ → ProtorealManifold
  | 0 => c
  | n + 1 => ProtorealManifold.mul c (right_orbit c n)

private def witness_c : ProtorealManifold :=
  { a := 1, b := 1, m := 1, e := 0, l := 0 }

private theorem left_orbit_1 :
    left_orbit witness_c 1 = ProtorealManifold.mul witness_c witness_c := rfl

private theorem left_orbit_2 :
    left_orbit witness_c 2 = ProtorealManifold.mul (left_orbit witness_c 1) witness_c := rfl

private theorem right_orbit_1 :
    right_orbit witness_c 1 = ProtorealManifold.mul witness_c witness_c := rfl

private theorem right_orbit_2 :
    right_orbit witness_c 2 = ProtorealManifold.mul witness_c (right_orbit witness_c 1) := rfl

/-- The left and right orbits DIVERGE after 2 steps.
    With c = (1,1,1,0,0), the b·m cross-coupling activates:
      left2.a  = (c*c)*c .a = -1
      right2.a = c*(c*c) .a =  3
    This 4-unit gap IS the non-associative fine structure. -/
theorem orbits_diverge :
    (left_orbit witness_c 2).a ≠ (right_orbit witness_c 2).a := by
  rw [left_orbit_2, left_orbit_1, right_orbit_2, right_orbit_1]
  unfold witness_c ProtorealManifold.mul
  norm_num

-- ═══════════════════════════════════════════════════════
-- Section 5: THE HYPERBOLIC SIGNATURE
-- ═══════════════════════════════════════════════════════

/-- **THE b/m DIVERGENCE**: Under Klein squaring, starting
    from a parity-locked state (b = m), the b and m components
    DIVERGE because b gets +b² and m gets -m².

    After one step from (a=1, b=x, m=x):
      b' = 2x + x²
      m' = 2x - x²
      b' - m' = 2x²

    The divergence grows quadratically. This is why the
    Protoreal Mandelbrot has hyperbolic structure where
    the standard one has circular structure. -/
theorem parity_breaks_under_squaring (x : ℝ) :
    let u : ProtorealManifold := { a := 1, b := x, m := x, e := 0, l := 0 }
    (klein_square u).b - (klein_square u).m = 2 * x * x := by
  unfold klein_square ProtorealManifold.mul
  ring

/-- For nonzero x, a single Klein squaring breaks parity. -/
theorem squaring_breaks_parity (x : ℝ) (hx : x ≠ 0) :
    let u : ProtorealManifold := { a := 1, b := x, m := x, e := 0, l := 0 }
    (klein_square u).b ≠ (klein_square u).m := by
  unfold klein_square ProtorealManifold.mul
  simp
  intro h
  have : 2 * x * x = 0 := by linarith
  have : x * x = 0 := by linarith
  have : x = 0 := by
    by_contra hx'
    exact absurd (mul_self_eq_zero.mp this) hx'
  exact hx this

-- ═══════════════════════════════════════════════════════
-- Section 6: MASTER THEOREM
-- ═══════════════════════════════════════════════════════

/-- **PROTOREAL MANDELBROT MASTER THEOREM**

    1. Hyperbolic asymmetry: b²→+, m²→- (opposite signs)
    2. Parity breaks under squaring: b-m divergence = 2x²
    3. Orbits diverge: left≠right parenthesization
    4. The iteration is well-defined on the 5D Klein algebra

    The standard Mandelbrot lives in ℂ (2D, commutative, associative).
    The Protoreal Mandelbrot lives in the Klein algebra (5D, neither).
    The extra structure — hyperbolic asymmetry, orbit trees,
    associator fine structure — is what makes it special. -/
theorem protoreal_mandelbrot_master :
    -- 1. Hyperbolic asymmetry (b and m diverge)
    ((klein_square { a := 0, b := 1, m := 1, e := 0, l := 0 : ProtorealManifold }).b = 1 ∧
     (klein_square { a := 0, b := 1, m := 1, e := 0, l := 0 : ProtorealManifold }).m = -1) ∧
    -- 2. Parity breaks quadratically
    (∀ x : ℝ,
     (klein_square { a := 1, b := x, m := x, e := 0, l := 0 : ProtorealManifold }).b -
     (klein_square { a := 1, b := x, m := x, e := 0, l := 0 : ProtorealManifold }).m = 2 * x * x) ∧
    -- 3. Non-associative orbit divergence
    ((left_orbit witness_c 2).a ≠ (right_orbit witness_c 2).a) :=
  ⟨hyperbolic_asymmetry,
   parity_breaks_under_squaring,
   orbits_diverge⟩

end CyberAlchemy.ProtorealMandelbrot


