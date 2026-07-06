#!/usr/bin/env python3
"""
verify_fbbt_negentropy.py — Exhaustive verification of all arithmetic claims
in the "Prime Field Mechanics and Negentropy" chapter (3_golden_tetrahedron.tex),
specifically the newly merged FBBT and Schrödinger Negentropy sections.

Every assertion printed as PASS/FAIL.
"""

import math

PASS = 0
FAIL = 0

def check(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  ✓ PASS: {name}")
    else:
        FAIL += 1
        print(f"  ✗ FAIL: {name}  {detail}")


print("=" * 72)
print("SECTION 1: Golden Field Fundamentals (pre-existing, sanity check)")
print("=" * 72)

# Golden polynomial roots
# x^2 - x - 1 = 0 in F_229
phi_229, phibar_229 = 148, 82
check("φ=148 satisfies x²=x+1 at p=229", pow(148, 2, 229) == (148 + 1) % 229)
check("φ̄=82 satisfies x²=x+1 at p=229", pow(82, 2, 229) == (82 + 1) % 229)
check("φ + φ̄ ≡ 1 mod 229", (148 + 82) % 229 == 1)
check("φ · φ̄ ≡ -1 mod 229", (148 * 82) % 229 == 228)

# Conjugate orbit order
check("ord(φ̄=82) = 57 at p=229", pow(82, 57, 229) == 1)
check("82^19 ≠ 1 (proper subgroup check)", pow(82, 19, 229) != 1)
check("82^3 ≠ 1 (proper subgroup check)", pow(82, 3, 229) != 1)

# Golden orbit order  
check("ord(φ=148) = 114 at p=229", pow(148, 114, 229) == 1)
check("148^57 ≠ 1 (proper divisor check)", pow(148, 57, 229) != 1)

print()
print("=" * 72)
print("SECTION 2: Schrödinger Negentropy Computations")
print("=" * 72)

# Claim: log2(228) - log2(57) = log2(4) = 2 bits
delta_H = math.log2(228) - math.log2(57)
check("Δ H = log₂(228) - log₂(57) = 2.0 bits", abs(delta_H - 2.0) < 1e-10,
      f"got {delta_H}")

# Claim: 228/57 = 4
check("228/57 = 4 (exact)", 228 // 57 == 4 and 228 % 57 == 0)

# Claim: coset decomposition extracts log2(3) ≈ 1.585 bits
coset_bits = math.log2(57) - math.log2(19)
check("Coset negentropy = log₂(57/19) = log₂(3) ≈ 1.585",
      abs(coset_bits - math.log2(3)) < 1e-10, f"got {coset_bits}")

# Claim: total negentropy = log2(228/19) = log2(12) ≈ 3.585 bits
total_neg = math.log2(228 / 19)
check("Total negentropy = log₂(12) ≈ 3.585 bits",
      abs(total_neg - math.log2(12)) < 1e-10, f"got {total_neg}")
check("228/19 = 12 (exact)", 228 // 19 == 12 and 228 % 19 == 0)

print()
print("=" * 72)
print("SECTION 3: FBBT Baby-Step Giant-Step Table")
print("=" * 72)

# Baby step table: 82^j mod 229 for j=0..7
baby_steps_claimed = {
    0: 1,
    1: 82,
    2: 83,
    3: 165,
    4: 19,
    5: 184,
    6: 203,
    7: 158,
}

for j, expected in baby_steps_claimed.items():
    actual = pow(82, j, 229)
    check(f"82^{j} ≡ {expected} (mod 229)", actual == expected,
          f"got {actual}")

# Verify baby-step 3 intermediate: 82 × 83 = 6806, 6806 mod 229
check("82 × 83 = 6806", 82 * 83 == 6806)
check("6806 - 29×229 = 6806 - 6641 = 165", 6806 - 29 * 229 == 165)

# Verify baby-step 5: 82 × 19 = 1558
check("82 × 19 = 1558", 82 * 19 == 1558)
check("1558 - 6×229 = 1558 - 1374 = 184", 1558 - 6 * 229 == 184)

# Verify baby-step 6: 82 × 184 = 15088
check("82 × 184 = 15088", 82 * 184 == 15088)
check("15088 - 65×229 = 15088 - 14885 = 203", 15088 - 65 * 229 == 203)

# Verify baby-step 7: 82 × 203 = 16646
check("82 × 203 = 16646", 82 * 203 == 16646)
check("16646 - 72×229 = 16646 - 16488 = 158", 16646 - 72 * 229 == 158)

print()
print("=" * 72)
print("SECTION 4: FBBT Giant-Step Inverse")
print("=" * 72)

# Claim: 82^8 ≡ 132 mod 229
check("82^8 ≡ 132 (mod 229)", pow(82, 8, 229) == 132)

# Claim: 82^(-8) = 82^49 mod 229 (since 82^57 = 1)
check("82^57 = 1 ⟹ 82^(-8) = 82^49", pow(82, 49, 229) == pow(132, 228 - 1, 229),
      f"82^49={pow(82,49,229)}, 132^(-1)={pow(132,227,229)}")

# Verify 132 × 82^49 ≡ 1 (mod 229)
check("132 × 82^49 ≡ 1 (mod 229)", (132 * pow(82, 49, 229)) % 229 == 1)

# Claim: ceil(sqrt(57)) = 8
check("⌈√57⌉ = 8", math.ceil(math.sqrt(57)) == 8)

print()
print("=" * 72)
print("SECTION 5: FBBT Worked Examples")
print("=" * 72)

# Example 1: H = 19, claim t = 4
check("Halting example: 82^4 ≡ 19 (mod 229), so t=4", pow(82, 4, 229) == 19)

# Example 2: H = 20, claim t = 16
check("Halting example: 82^16 ≡ 20 (mod 229), so t=16", pow(82, 16, 229) == 20)

# BSGS resolution of H=20: match at j=0, i=2, t = 0+8×2 = 16
giant_step_factor = pow(82, 49, 229)  # 82^(-8) mod 229
h_20 = 20
current = h_20
found = False
for i in range(8):
    if current in baby_steps_claimed.values():
        # find j
        for j, v in baby_steps_claimed.items():
            if v == current:
                t = j + 8 * i
                check(f"BSGS resolution: H=20 → j={j}, i={i}, t={t}=16",
                      t == 16)
                found = True
                break
        break
    current = (current * giant_step_factor) % 229
if not found:
    check("BSGS resolution of H=20", False, "no match found")

print()
print("=" * 72)
print("SECTION 6: Orbit Closure & Periodicity")
print("=" * 72)

# Verify full orbit closure: 82^k mod 229 for k=0..56 are all distinct
orbit = [pow(82, k, 229) for k in range(57)]
check("Conjugate orbit has 57 distinct elements",
      len(set(orbit)) == 57)
check("82^57 ≡ 1 (orbit closes)", orbit[-1] == pow(82, 56, 229) and pow(82, 57, 229) == 1)

# Verify no smaller period divides 57 (factors: 1, 3, 19, 57)
for d in [1, 3, 19]:
    check(f"82^{d} ≢ 1 (no early closure at d={d})", pow(82, d, 229) != 1)

print()
print("=" * 72)
print("SECTION 7: SU(3) Confinement (sanity re-check)")
print("=" * 72)

# Cube root of unity: ω = 82^19 = 94
omega = pow(82, 19, 229)
check("ω = 82^19 ≡ 94 (mod 229)", omega == 94)
check("ω² = 94² ≡ 134 (mod 229)", pow(94, 2, 229) == 134)
check("1 + ω + ω² = 229 ≡ 0 (mod 229)", (1 + 94 + 134) % 229 == 0)
check("ω³ ≡ 1 (mod 229)", pow(94, 3, 229) == 1)

print()
print("=" * 72)
print("SECTION 8: Mayer-Vietoris Parity Identity")
print("=" * 72)

# φ^n · φ̄^n ≡ (-1)^n for all n in [0..57]
all_parity_ok = True
for n in range(58):
    prod = (pow(148, n, 229) * pow(82, n, 229)) % 229
    expected = 1 if n % 2 == 0 else 228  # 228 = -1 mod 229
    if prod != expected:
        all_parity_ok = False
        print(f"  ✗ FAIL: Parity at n={n}: got {prod}, expected {expected}")
        FAIL += 1
        break
if all_parity_ok:
    PASS += 1
    print(f"  ✓ PASS: Mayer-Vietoris parity φ^n·φ̄^n ≡ (-1)^n for n=0..57")

print()
print("=" * 72)
print("SECTION 9: Tetrahedron Identities")
print("=" * 72)

V = [1, 94, 134, 228]
prod_V = 1
for v in V:
    prod_V = (prod_V * v) % 229
sum_V = sum(V) % 229

check("V₁·V₂·V₃·V₄ ≡ -1 (mod 229)", prod_V == 228)
check("V₁+V₂+V₃+V₄ ≡ -1 (mod 229)", sum_V == 228)

# Face sums
check("Face {1,94,134}: 1+94+134 = 229 ≡ 0", (1+94+134) % 229 == 0)
check("Face {1,94,228}: 1+94+228 = 323 ≡ 94 = ω", (1+94+228) % 229 == 94)
check("Face {1,134,228}: 1+134+228 = 363 ≡ 134 = ω²", (1+134+228) % 229 == 134)
check("Face {94,134,228}: 94+134+228 = 456 ≡ 227 = -2", (94+134+228) % 229 == 227)

print()
print("=" * 72)
print(f"SUMMARY: {PASS} passed, {FAIL} failed out of {PASS+FAIL} checks")
print("=" * 72)

if FAIL == 0:
    print("\n🎯 ALL CHECKS PASSED — No BS detected.")
else:
    print(f"\n⚠️  {FAIL} FAILURES — review claims above.")
