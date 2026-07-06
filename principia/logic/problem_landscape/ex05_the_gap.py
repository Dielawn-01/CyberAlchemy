"""Exercise 5: κ = -1 Is the Gap.

OOP LESSON:
  - The Protoreal Algebra encodes Gödel-Tarski as κ = -1
  - ω (thrust) and ι (anchor) are two directions of self-reference
  - Their product ω·ι = -1 IS the incompleteness, made algebraic
  - The golden ratio emerges FROM the gap (not assumed)

MATH:
  - ω·ι = -1, ι·ω = +1 → commutator [ω,ι] = -2
  - Trace = ω + ι = 1, Det = ω·ι = -1
  - Vieta: X² - X - 1 = 0 → φ = (1+√5)/2, φ̄ = (1-√5)/2

RUN: python -m principia.logic.problem_landscape.ex05_the_gap
"""

import math


def main():
    # ── The Gap ──────────────────────────────────────────
    KAPPA = -1

    # ω (thrust): idempotent (ω² = ω). Pushes forward.
    # ι (anchor): anti-idempotent (ι² = -ι). Pulls back.
    # Their product is the gap:
    omega_times_iota = -1  # ω·ι = -1 (syntax × semantics ≠ identity)
    iota_times_omega = +1  # ι·ω = +1 (reverse order)
    commutator = omega_times_iota - iota_times_omega  # [ω,ι] = -2

    print("THE GAP:")
    print(f"  ω · ι = {omega_times_iota}")
    print(f"  ι · ω = {iota_times_omega}")
    print(f"  [ω, ι] = {commutator}")
    print(f"  κ = ω·ι = {KAPPA}")
    assert KAPPA == -1

    # ── The Golden Ratio Emerges ─────────────────────────
    # Vieta's formulas for the characteristic polynomial:
    #   Trace = ω + ι = 1
    #   Det   = ω · ι = -1
    #   → X² - (Trace)X + (Det) = X² - X - 1 = 0
    trace = 1
    det = KAPPA  # -1

    # Quadratic formula:
    discriminant = trace ** 2 - 4 * det  # 1 - 4(-1) = 5
    phi = (trace + math.sqrt(discriminant)) / 2
    phi_bar = (trace - math.sqrt(discriminant)) / 2

    print()
    print("THE GOLDEN RATIO (forced, not assumed):")
    print(f"  Trace = {trace}")
    print(f"  Det = {det}")
    print(f"  Discriminant = {discriminant}")
    print(f"  φ  = {phi:.10f}")
    print(f"  φ̄  = {phi_bar:.10f}")

    # Verify Vieta's formulas
    assert abs(phi + phi_bar - trace) < 1e-10, "φ + φ̄ = 1"
    assert abs(phi * phi_bar - det) < 1e-10, "φ · φ̄ = -1 = κ"
    print(f"  φ + φ̄ = {phi + phi_bar:.1f} = Trace ✓")
    print(f"  φ · φ̄ = {phi * phi_bar:.1f} = Det = κ ✓")

    # ── The Characteristic Polynomial ────────────────────
    # X² - X - 1 = 0 at X = φ:
    check_phi = phi ** 2 - phi - 1
    check_bar = phi_bar ** 2 - phi_bar - 1
    assert abs(check_phi) < 1e-10, "φ satisfies X² - X - 1"
    assert abs(check_bar) < 1e-10, "φ̄ satisfies X² - X - 1"

    print()
    print("CHARACTERISTIC POLYNOMIAL: X² - X - 1 = 0")
    print(f"  φ² - φ - 1  = {check_phi:.2e} ≈ 0 ✓")
    print(f"  φ̄² - φ̄ - 1 = {check_bar:.2e} ≈ 0 ✓")

    # ── The Lesson ───────────────────────────────────────
    print()
    print("=" * 60)
    print("SUMMARY:")
    print("  1. κ = -1 is the Gödel-Tarski gap, encoded algebraically.")
    print("  2. The golden ratio is FORCED by κ (Trace=1, Det=-1).")
    print("  3. The gap is not a defect. It is the engine.")
    print("  4. Every structure in this book is built from κ = -1.")
    print()
    print("Now we build.")
    print("→ See ch01_unreal_algebra/")


if __name__ == "__main__":
    main()
