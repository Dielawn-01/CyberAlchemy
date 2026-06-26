import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Hexadecimal Boundary Formalization

**Authors:** LaRue (Framework)

## Overview

The IPv8 address encoding maps Protoreal manifold coordinates into
hexadecimal 16-bit words. This module formalizes the relationship between
the golden split prime fields (which operate in decimal mod-p arithmetic)
and the hexadecimal representation used for network addressing.

The key insight: the golden split primes {229, 181, 139} and the bridge
prime 14489 all embed cleanly within a single hex word (2^16 = 65536),
meaning their modular arithmetic can be faithfully lifted into the
hex address space without truncation or overflow.

## The Off-By-One Boundary

The correct modulus for a 16-bit hex word is `0x10000 = 65536`, NOT
`0xFFFF = 65535`. Using `% 0xFFFF` produces a range of `[0, 65534]`,
missing the value `0xFFFF = 65535` entirely. This corrupts the upper
boundary of the address space.

All proofs by `norm_num` or `native_decide`.
-/

-- ════════════════════════════════════════════════════
-- §1: The Hex Word Boundary
-- ════════════════════════════════════════════════════

/-- A 16-bit hex word spans 2^16 = 65536 values. -/
def hex_word : ℕ := 0x10000

/-- hex_word = 65536. -/
theorem hex_word_value : hex_word = 65536 := by norm_num [hex_word]

/-- The INCORRECT boundary 0xFFFF = 65535, one less than the correct modulus. -/
theorem hex_ffff_value : (0xFFFF : ℕ) = 65535 := by norm_num

/-- The correct modulus covers the full 16-bit range [0, 65535]. -/
theorem hex_boundary_correct : ∀ n : ℕ, n % hex_word < hex_word := by
  intro n
  exact Nat.mod_lt n (by norm_num [hex_word])

/-- The incorrect modulus misses the top value:
    n % 0xFFFF can never equal 0xFFFF (it maxes at 0xFFFE = 65534). -/
theorem hex_boundary_incorrect_misses_top :
    ∀ n : ℕ, n % 0xFFFF ≠ 0xFFFF := by
  intro n
  exact Nat.ne_of_lt (Nat.mod_lt n (by norm_num))

-- ════════════════════════════════════════════════════
-- §2: Golden Split Primes Embed in Hex Words
-- ════════════════════════════════════════════════════

/-- 229 < 65536: Gold embeds in a single hex word. -/
theorem gold_embeds_in_hex : 229 < hex_word := by norm_num [hex_word]

/-- 181 < 65536: Blue embeds in a single hex word. -/
theorem blue_embeds_in_hex : 181 < hex_word := by norm_num [hex_word]

/-- 139 < 65536: Violet embeds in a single hex word. -/
theorem violet_embeds_in_hex : 139 < hex_word := by norm_num [hex_word]

/-- 14489 < 65536: The bridge prime embeds in a single hex word. -/
theorem bridge_embeds_in_hex : 14489 < hex_word := by norm_num [hex_word]

-- ════════════════════════════════════════════════════
-- §3: Hex Encoding of Golden Roots
-- ════════════════════════════════════════════════════

/-- The golden root φ = 148 at p = 229, scaled by 1000000 and reduced mod hex_word.
    This models the `encode_ipv8_address` computation in the Rust WASM core. -/
theorem gold_phi_hex_encode : (148 * 1000000) % hex_word = 19712 := by
  norm_num [hex_word]

/-- The conjugate root φ̄ = 82 at p = 229, similarly encoded. -/
theorem gold_phibar_hex_encode : (82 * 1000000) % hex_word = 14464 := by
  norm_num [hex_word]

/-- The golden root at Blue: φ = 14, hex-encoded. -/
theorem blue_phi_hex_encode : (14 * 1000000) % hex_word = 40832 := by
  norm_num [hex_word]

-- ════════════════════════════════════════════════════
-- §4: Master Theorem
-- ════════════════════════════════════════════════════

/-- The hexadecimal boundary master theorem:
    1. The correct modulus is 0x10000 = 65536
    2. The incorrect 0xFFFF misses the top value
    3. All golden split primes embed cleanly
    4. The bridge prime embeds cleanly -/
theorem hex_boundary_master :
    hex_word = 65536 ∧
    (0xFFFF : ℕ) = 65535 ∧
    229 < hex_word ∧
    181 < hex_word ∧
    139 < hex_word ∧
    14489 < hex_word := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num [hex_word]
