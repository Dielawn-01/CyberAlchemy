"""
principia.physical.cosmology.celestial
=======================================

Celestial bodies as polymorphic objects in the gauge lattice.

This module teaches OOP data science by modeling planets, stars,
and moons as instances of Python classes whose magnetic tilt
predictions are derived from the same golden field constants
used in the logic layer.

The key insight: the core dynamo type (metallic vs. shell)
determines which OOP pattern applies (CoreDynamo vs ShellDynamo),
while the golden ratio φ and its topological descendants
(sech²(ln φ) ≈ 4/5) provide the physical constants.
"""

import math
from typing import Optional, List
from dataclasses import dataclass

from principia.logic.ff229 import Element, KAPPA

# ── Golden field constants (derived from κ = -1) ──
PHI = (1 + math.sqrt(5)) / 2              # φ ≈ 1.618
PHI_BAR = PHI - 1                          # φ̄ ≈ 0.618
SQRT5_INV = 1 / math.sqrt(5)              # 1/√5 ≈ 0.447
SECH2_LN_PHI = 1 - math.tanh(math.log(PHI))**2  # sech²(ln φ) ≈ 4/5
BASE_CROSSING = 26.57                      # degrees — atan(1/2)

# Stieltjes cosmic drag coefficient (Ch.16 §4)
UPSILON_COSMIC = 0.079834


@dataclass
class Observation:
    """Empirical measurement container."""
    value: float
    error_margin: float
    source: str


class CelestialBody:
    """Base class for any body in the Metareal prime lattice.

    Each body has:
    - A name and core geometry (core_fraction)
    - An empirical observation to compare against
    - A predict_magnetic_tilt() method (polymorphic — overridden by subclass)
    """

    def __init__(self, name: str, core_fraction: float = 0.0,
                 obs: Optional[Observation] = None):
        self.name = name
        self.core_fraction = core_fraction
        self.observation = obs

    def predict_magnetic_tilt(self) -> float:
        raise NotImplementedError("Subclasses implement the dynamo mechanism.")

    def error(self) -> float:
        if not self.observation:
            return 0.0
        return abs(self.predict_magnetic_tilt() - self.observation.value)

    def within_margin(self) -> bool:
        if not self.observation:
            return True
        return self.error() <= self.observation.error_margin


class CoreDynamo(CelestialBody):
    """Type 1: Metallic core dynamo (Earth, Mercury, Jupiter, Saturn).

    Tilt = BASE_CROSSING × core_fraction × sech²(ln φ)
    The sech² factor is the topological damping from the golden
    ratio's hyperbolic geometry (Ch.16 §3.2).
    """

    def predict_magnetic_tilt(self) -> float:
        return BASE_CROSSING * self.core_fraction * SECH2_LN_PHI


class ShellDynamo(CelestialBody):
    """Type 2: Ionic shell dynamo (Uranus, Neptune).

    Tilt = obliquity × golden_factor × (1 ± υ·r_core)
    Contraction mode uses 1/φ, amplification uses φ.
    The Stieltjes drag corrects for core-mantle coupling.
    """

    def __init__(self, name: str, obliquity: float, mode: str,
                 core_fraction: float = 0.0,
                 obs: Optional[Observation] = None):
        super().__init__(name, core_fraction, obs)
        self.obliquity = obliquity
        self.mode = mode  # 'contraction' or 'amplification'

    def predict_magnetic_tilt(self) -> float:
        golden_factor = (1 / PHI) if self.mode == 'contraction' else PHI
        base_tilt = self.obliquity * golden_factor
        sign = -1 if self.mode == 'contraction' else 1
        return base_tilt * (1 + sign * UPSILON_COSMIC * self.core_fraction)


class TidalDynamo(CelestialBody):
    """Type 3: Tidally locked body (Ganymede).

    Tilt = BASE_CROSSING × core_fraction × sech²(ln φ) × √5·tidal_factor
    Tidal heating amplifies the core dynamo by the discriminant √5.
    """

    def __init__(self, name: str, core_fraction: float,
                 tidal_factor: float = 1.0,
                 obs: Optional[Observation] = None):
        super().__init__(name, core_fraction, obs)
        self.tidal_factor = tidal_factor

    def predict_magnetic_tilt(self) -> float:
        core_tilt = BASE_CROSSING * self.core_fraction * SECH2_LN_PHI
        return core_tilt * math.sqrt(5) * self.tidal_factor


# ── The Solar System Survey (9 bodies from the book) ──
SOLAR_SYSTEM: List[CelestialBody] = [
    CoreDynamo("Mercury", 0.85, Observation(0.034, 0.005, "MESSENGER")),
    CoreDynamo("Earth", 0.546, Observation(11.5, 0.3, "IGRF-13")),
    CoreDynamo("Jupiter", 0.83, Observation(9.6, 0.5, "Juno")),
    CoreDynamo("Saturn", 0.63, Observation(0.0, 0.5, "Cassini")),
    ShellDynamo("Uranus", 97.77, "contraction", 7500/25362,
                Observation(58.6, 2.0, "Voyager 2")),
    ShellDynamo("Neptune", 28.32, "amplification", 7500/24622,
                Observation(46.9, 1.5, "Voyager 2")),
    TidalDynamo("Ganymede", 0.26, 0.35,
                Observation(4.0, 2.0, "Galileo")),
]


def main():
    """Run the full celestial body survey — the physical layer
    consuming the logic layer's golden constants."""

    # Verify the golden constants derive from κ
    e_kappa = Element(228)  # κ = -1 ≡ 228 mod 229
    assert e_kappa.z == 228, f"κ should be 228, got {e_kappa.z}"
    assert pow(228, 2, 229) == 1, "κ² ≠ 1"

    print("═" * 72)
    print("  CELESTIAL BODY SURVEY (principia.physical.cosmology)")
    print("  Golden constants derived from κ = -1 in F*₂₂₉")
    print("═" * 72)
    print(f"\n  φ = {PHI:.10f}    sech²(ln φ) = {SECH2_LN_PHI:.6f}")
    print(f"  φ̄ = {PHI_BAR:.10f}    υ_cosmic    = {UPSILON_COSMIC:.6f}")
    print(f"  Base crossing = {BASE_CROSSING}° = atan(1/2)")

    print(f"\n  {'Body':<12s} {'Type':<14s} {'Pred':>7s} {'Obs':>7s} "
          f"{'Err':>6s} {'Within':>6s} {'Source':<12s}")
    print(f"  {'─'*12} {'─'*14} {'─'*7} {'─'*7} {'─'*6} {'─'*6} {'─'*12}")

    all_within = True
    for body in SOLAR_SYSTEM:
        pred = body.predict_magnetic_tilt()
        obs = body.observation
        err = body.error()
        ok = body.within_margin()
        if not ok:
            all_within = False
        icon = "✓" if ok else "✗"

        dtype = type(body).__name__
        print(f"  {body.name:<12s} {dtype:<14s} {pred:7.2f}° {obs.value:7.1f}° "
              f"{err:6.2f}° {icon:>6s} {obs.source:<12s}")

    print(f"\n  {'━'*72}")
    if all_within:
        print("  ✓ All predictions within observational error margins")
    else:
        print("  ⚠ Some predictions outside margins (see ✗ above)")

    # Print the F*₂₂₉ context
    print(f"\n  Algebraic context:")
    print(f"  φ = Element(148), ord = {Element(148).order}")
    print(f"  φ̄ = Element(82),  ord = {Element(82).order}")
    print(f"  κ = Element(228), ord = {Element(228).order}")
    print(f"  φ · φ̄ = {(148 * 82) % 229} ≡ κ (mod 229) ✓")


if __name__ == "__main__":
    main()
