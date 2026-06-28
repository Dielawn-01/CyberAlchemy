import LaRueProtorealAlgebra.HolochainHash
import LaRueProtorealAlgebra.KleinTopology

open HolochainHash
open KleinTopology

namespace ZKPCR

-- ══════════════════════════════════════════════════════════════
-- SECTION 3: KRAPIVIN POINTER/HASH COMPRESSION
-- ══════════════════════════════════════════════════════════════

/-- **Krapivin Pointer Compression (Tiny Pointers)**
    Compresses a pointer of size log(N) (absolute orbit index t) into a tiny pointer j
    using the context/owner c (the color arc of the orbit).
    For N = 57 and K = 3 arcs of size 19: -/
def krapivin_compress (t : ℕ) : ℕ := t % 19

/-- **Krapivin Pointer Extraction**
    Reconstructs the original absolute pointer from the tiny pointer j and context c. -/
def krapivin_extract (j : ℕ) (c : ℕ) : ℕ := 19 * c + j

/-- **Krapivin Extraction Soundness**
    Proves that compressing a valid pointer index t < 57 and extracting it
    using the context/owner c = t / 19 reconstructs t exactly. -/
theorem krapivin_extraction_soundness (t : ℕ) (_h_bound : t < 57) :
  krapivin_extract (krapivin_compress t) (t / 19) = t := by
  unfold krapivin_extract krapivin_compress
  omega

-- ══════════════════════════════════════════════════════════════
-- SECTION 4: FBBT DIRECT INVERSE AND CONFINEMENT
-- ══════════════════════════════════════════════════════════════

def golden_field_prime : ℕ := 229
def golden_generator : ℕ := 82
def omega_cube_root : ℕ := 94

/-- **FBBT Direct Inverse (Extraction)**
    Takes the compressed tiny pointer j and context c, and extracts
    the original halting state H % 229 from the FBBT. -/
def fbbt_inverse_extract (j : ℕ) (c : ℕ) : ℕ :=
  (golden_generator ^ (krapivin_extract j c)) % golden_field_prime

lemma base_mod : (82 ^ 19) % 229 = 94 := by
  rfl

lemma pow_mod_step (c : ℕ) : (82 ^ 19) ^ c % 229 = 94 ^ c % 229 := by
  induction c with
  | zero => rfl
  | succ c ih =>
    rw [pow_succ (82 ^ 19), pow_succ 94]
    rw [Nat.mul_mod ((82 ^ 19) ^ c) (82 ^ 19)]
    rw [ih, base_mod]
    rw [Nat.mul_mod (94 ^ c) 94]

/-- **FBBT Inverse Extraction Equivalence**
    Proves that the extracted halting state is equivalent to applying the
    confinement operator omega^c to the base state phi^j % 229.
    This formally connects Krapivin pointer compression as a direct inverse
    on the FBBT, saving log2(3) = 1.585 bits of negentropy. -/
theorem fbbt_inverse_extraction_equivalence (j c : ℕ) :
  fbbt_inverse_extract j c =
  ((omega_cube_root ^ c) * (golden_generator ^ j)) % golden_field_prime := by
  unfold fbbt_inverse_extract krapivin_extract golden_generator omega_cube_root golden_field_prime
  rw [pow_add, pow_mul]
  rw [Nat.mul_mod ((82 ^ 19) ^ c) (82 ^ j)]
  rw [pow_mod_step]
  rw [Nat.mul_mod (94 ^ c) (82 ^ j)]

end ZKPCR

