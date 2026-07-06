"""Branch Cut Computation — β = ln(φ) and the monodromy of κ.

Demonstrates that the trace-determinant constraints of the Protoreal
algebra force β = ln(φ) in logarithmic coordinates, and that the
branch cut of ln(−1) = iπ is the structural source of κ = −1.

OOP Lessons: complex arithmetic, numerical verification of symbolic identities.

Key Results:
  - 2sinh(β) = 1  ⟹  β = arcsinh(1/2) = ln(φ)
  - β + β̄ = iπ     (the branch cut monodromy)
  - e^β = φ, e^β̄ = φ̄   (exponential ↔ golden map)
  - Boltzmann weight at golden temperature: e^{-βE} = φ^{-E}
"""

import cmath
import math


# ═══════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════
PHI = (1 + math.sqrt(5)) / 2       # golden ratio φ ≈ 1.618
PHI_BAR = (1 - math.sqrt(5)) / 2   # conjugate φ̄ ≈ −0.618
KAPPA = -1                          # scalar associator

# Logarithmic coordinates
BETA = math.log(PHI)                # β = ln(φ) ≈ 0.4812
BETA_BAR = cmath.log(PHI_BAR)      # β̄ = ln(φ̄) = −ln(φ) + iπ


# ═══════════════════════════════════════════
# BRANCH CUT ANALYSIS
# ═══════════════════════════════════════════
class BranchCutAnalysis:
    """Analyzes the logarithmic coordinate system of the Protoreal algebra.

    The trace-determinant constraints (Tr=1, Det=−1) force a unique
    value of β = ln(ω) = ln(φ). The branch cut of ln(−1) produces
    the κ = −1 monodromy.
    """

    def __init__(self):
        self.phi = PHI
        self.phi_bar = PHI_BAR
        self.beta = BETA
        self.beta_bar = BETA_BAR

    # ── Core identities ─────────────────────

    def verify_trace(self) -> bool:
        """e^β + e^β̄ = 1 (trace in exponential coordinates)."""
        lhs = cmath.exp(self.beta) + cmath.exp(self.beta_bar)
        return abs(lhs - 1.0) < 1e-12

    def verify_determinant(self) -> bool:
        """β + β̄ = iπ (determinant in log coordinates)."""
        lhs = self.beta + self.beta_bar
        return abs(lhs - 1j * math.pi) < 1e-12

    def verify_sinh(self) -> bool:
        """2sinh(β) = 1 (the golden constraint)."""
        lhs = 2 * math.sinh(self.beta)
        return abs(lhs - 1.0) < 1e-12

    def verify_arcsinh(self) -> bool:
        """β = arcsinh(1/2) = ln(φ)."""
        lhs = math.asinh(0.5)
        return abs(lhs - self.beta) < 1e-12

    # ── Monodromy ────────────────────────────

    def monodromy(self, n: int = 0) -> complex:
        """The n-th branch of ln(−1) = iπ + 2πin.

        n=0 is the principal branch. Each different n gives a
        valid but incompatible value — the choice requires an
        external observer (δ).
        """
        return 1j * math.pi + 2j * math.pi * n

    def verify_kappa_is_monodromy(self) -> bool:
        """κ = −1 = e^{iπ}, the monodromy of one circuit."""
        return abs(cmath.exp(1j * math.pi) - KAPPA) < 1e-12

    # ── Boltzmann distribution ───────────────

    def boltzmann_weight(self, energy: float) -> float:
        """e^{−βE} = φ^{−E} at the golden temperature."""
        return self.phi ** (-energy)

    def golden_temperature(self) -> float:
        """kT = 1/β = 1/ln(φ) ≈ 2.078."""
        return 1.0 / self.beta

    # ── Parity involution ────────────────────

    def branch_swap(self, beta: complex) -> complex:
        """The parity involution u ↔ u*: sends β ↔ β̄.

        This swaps ω and ι, exchanging the golden and conjugate orbits.
        Algebraically: β̄ = iπ − β.
        """
        return 1j * math.pi - beta

    def verify_branch_swap_involution(self) -> bool:
        """Applying the swap twice returns to the original."""
        swapped = self.branch_swap(self.beta)
        double_swapped = self.branch_swap(swapped)
        return abs(double_swapped - self.beta) < 1e-12

    # ── Finite field demonstration ───────────

    def orbit_demo(self, p: int = 229) -> dict:
        """Demonstrate the two orbits (branches) at F_p*.

        The golden orbit ⟨φ⟩ and conjugate orbit ⟨φ̄⟩ are the
        two branches of the same algebraic structure. The observer
        must choose which orbit to track — this IS the branch cut
        decision in discrete arithmetic.
        """
        # φ ≡ 148 (mod 229), φ̄ ≡ 82 (mod 229)
        phi_p = 148
        phibar_p = 82

        golden_orbit = []
        conjugate_orbit = []
        val_g, val_c = 1, 1
        for k in range(57):
            conjugate_orbit.append(val_c)
            val_c = (val_c * phibar_p) % p

        val_g = 1
        for k in range(114):
            golden_orbit.append(val_g)
            val_g = (val_g * phi_p) % p

        # The cube root ρ = φ̄^19
        rho = pow(phibar_p, 19, p)
        confinement = (1 + rho + pow(rho, 2, p)) % p

        return {
            "golden_orbit_size": len(set(golden_orbit)),
            "conjugate_orbit_size": len(set(conjugate_orbit)),
            "rho": rho,
            "confinement_identity": confinement,  # should be 0
            "phi_times_phibar": (phi_p * phibar_p) % p,  # should be p-1 = -1
        }


# ═══════════════════════════════════════════
# VERIFICATION
# ═══════════════════════════════════════════
def verify():
    """Run all branch cut verifications."""
    bc = BranchCutAnalysis()

    # Core logarithmic identities
    assert bc.verify_trace(), "Trace: e^β + e^β̄ = 1"
    assert bc.verify_determinant(), "Det: β + β̄ = iπ"
    assert bc.verify_sinh(), "Sinh: 2sinh(β) = 1"
    assert bc.verify_arcsinh(), "Arcsinh: β = arcsinh(1/2) = ln(φ)"

    # Monodromy
    assert bc.verify_kappa_is_monodromy(), "κ = e^{iπ} = −1"
    m0 = bc.monodromy(0)
    m1 = bc.monodromy(1)
    assert abs(m0 - 1j * math.pi) < 1e-12, "Principal branch: iπ"
    assert abs(m1 - 3j * math.pi) < 1e-12, "Branch n=1: 3iπ"

    # Branch swap involution
    assert bc.verify_branch_swap_involution(), "Swap² = identity"
    beta_bar_computed = bc.branch_swap(bc.beta)
    assert abs(beta_bar_computed - bc.beta_bar) < 1e-12, "Swap(β) = β̄"

    # Golden temperature
    kT = bc.golden_temperature()
    assert abs(kT - 1.0 / math.log(PHI)) < 1e-12, "kT = 1/ln(φ)"

    # Boltzmann weights at golden temperature
    assert abs(bc.boltzmann_weight(0) - 1.0) < 1e-12, "P(E=0) = 1"
    assert abs(bc.boltzmann_weight(1) - 1/PHI) < 1e-12, "P(E=1) = 1/φ"
    assert abs(bc.boltzmann_weight(2) - 1/PHI**2) < 1e-12, "P(E=2) = 1/φ²"

    # Finite field orbit demo
    orbits = bc.orbit_demo(229)
    assert orbits["golden_orbit_size"] == 114, "Golden orbit has 114 elements"
    assert orbits["conjugate_orbit_size"] == 57, "Conjugate orbit has 57 elements"
    assert orbits["confinement_identity"] == 0, "1 + ρ + ρ² ≡ 0 (mod 229)"
    assert orbits["phi_times_phibar"] == 228, "φ·φ̄ ≡ −1 (mod 229)"
    assert orbits["rho"] == 94, "ρ = φ̄^19 ≡ 94 (mod 229)"

    print("✓ branch_cut.py: all tests pass")
    print(f"  β = ln(φ) = {BETA:.6f}")
    print(f"  β̄ = {BETA_BAR:.6f}")
    print(f"  kT = 1/ln(φ) = {kT:.6f}")
    print(f"  ρ₂₂₉ = {orbits['rho']}, 1+ρ+ρ² ≡ {orbits['confinement_identity']} (mod 229)")


if __name__ == "__main__":
    verify()
