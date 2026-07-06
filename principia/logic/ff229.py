"""F*₂₂₉ elements with Force × Matter decomposition.

OOP Lessons: @property (lazy computation), __mul__, __pow__, __eq__,
             __hash__, factory methods, the CRT as a design pattern.

Every object in this module is an element of the multiplicative group
F*₂₂₉ (the nonzero elements of the field with 229 elements). Each
element has:
  - identity (z):           its residue mod 229
  - behavior (order):       how many multiplications to return to 1
  - structure (force, matter): CRT decomposition of order into Z/12Z × Z/19Z
"""

P = 229          # The prime
GROUP_ORDER = P - 1  # |F*₂₂₉| = 228 = 12 × 19
KAPPA = P - 1    # κ = -1 ≡ 228 mod 229


class Element:
    """A single element of F*₂₂₉ — the worldmodel's atom.

    Every object has identity (z), behavior (order), and structure
    (force level, matter level). That's what a class IS.
    """

    def __init__(self, z: int):
        self.z = z % P
        if self.z == 0:
            raise ValueError(f"0 is not in F*_{P}")
        self._order: int | None = None

    # ── Properties (lazy, cached) ───────────────────────────

    @property
    def order(self) -> int:
        """Multiplicative order: smallest k > 0 with z^k ≡ 1 mod 229.

        OOP lesson: @property computes on first access, then caches.
        The order is an INTRINSIC property — it doesn't change.
        """
        if self._order is None:
            k, power = 1, self.z
            while power != 1:
                power = (power * self.z) % P
                k += 1
            self._order = k
        return self._order

    @property
    def force_level(self) -> int:
        """Force component: order mod 12. The observation axis (Z/12Z)."""
        return self.order % 12

    @property
    def matter_level(self) -> int:
        """Matter component: order mod 19. The participation axis (Z/19Z)."""
        return self.order % 19

    @property
    def is_sub_arc(self) -> bool:
        """True if this element has zero matter content (pure force).

        Sub-arc elements live entirely in the Z/12Z force skeleton.
        They observe the system but cannot participate in metabolism.
        Excludes the identity (ord=1), which is in every subgroup.
        """
        return self.order > 1 and self.order % 19 != 0 and self.order <= 12

    @property
    def is_primitive_root(self) -> bool:
        """True if this element generates the full group F*₂₂₉."""
        return self.order == GROUP_ORDER

    # ── Decomposition / Recomposition ───────────────────────

    def decompose(self) -> tuple[int, int]:
        """CRT: element → (force_level, matter_level).

        OOP lesson: decomposition separates concerns. The force
        component handles observation; the matter component handles
        participation. Neither knows about the other.
        """
        return (self.force_level, self.matter_level)

    @classmethod
    def from_components(cls, force: int, matter: int) -> "Element":
        """CRT inverse: (force, matter) → element.

        OOP lesson: factory method. Builds an object from its
        structural components instead of its raw identity.

        Uses: 19⁻¹ mod 12 = 7, 12⁻¹ mod 19 = 8.
        """
        # Reconstruct the discrete log mod 228
        k = (force * 19 * 7 + matter * 12 * 8) % GROUP_ORDER
        # Need a primitive root to convert log → element
        g = 6  # 6 is a primitive root of F*₂₂₉
        return cls(pow(g, k, P))

    # ── Operator Overloading ────────────────────────────────

    def __mul__(self, other: "Element") -> "Element":
        """Multiplication in F*₂₂₉. OOP lesson: operator overloading."""
        return Element((self.z * other.z) % P)

    def __pow__(self, n: int) -> "Element":
        """Exponentiation in F*₂₂₉."""
        return Element(pow(self.z, n, P))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Element):
            return NotImplemented
        return self.z == other.z

    def __hash__(self) -> int:
        return hash(self.z)

    def __repr__(self) -> str:
        return f"E({self.z}, ord={self.order})"

    def __str__(self) -> str:
        sub = " [SUB-ARC]" if self.is_sub_arc else ""
        prim = " [PRIM]" if self.is_primitive_root else ""
        return (f"Element({self.z}): ord={self.order}, "
                f"F={self.force_level}, M={self.matter_level}{sub}{prim}")


# ── The Observer Pair ───────────────────────────────────────

Ar = Element(18)   # Argon:   ord=12, pure force, measurement
Ac = Element(89)   # Actinium: ord=12, pure force, transformation

# ── The Structural Constants ────────────────────────────────

# Chemical elements as Element objects (Z=1..92)
ELEMENTS = {}
_NAMES = [
    None, "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U",
]
for _z in range(1, 93):
    if _z != 0 and _z % P != 0:
        ELEMENTS[_NAMES[_z]] = Element(_z)


# ── Self-Tests ──────────────────────────────────────────────

def verify():
    """Run the self-tests for this module."""
    # 1. Group order factors
    assert GROUP_ORDER == 228, "|F*₂₂₉| = 228"
    assert 228 == 12 * 19, "228 = 12 × 19"

    # 2. Observer pair identities
    assert Ar.order == 12, f"ord(Ar) = {Ar.order}, expected 12"
    assert Ac.order == 12, f"ord(Ac) = {Ac.order}, expected 12"
    assert Ar ** 5 == Ac, "Ar⁵ = Ac"
    assert Ac ** 5 == Ar, "Ac⁵ = Ar"
    assert (Ar * Ac).z == KAPPA, "Ar × Ac = κ = -1"

    # 3. Sub-arc audit: exactly Ar and Ac in Z≤92
    sub_arc = [(z, e) for z in range(1, 93)
               if (e := Element(z)).is_sub_arc]
    assert len(sub_arc) == 2, f"Expected 2 sub-arc, got {len(sub_arc)}"
    assert sub_arc[0][0] == 18, "First sub-arc is Ar (Z=18)"
    assert sub_arc[1][0] == 89, "Second sub-arc is Ac (Z=89)"

    # 4. Carbon is a primitive root
    C = Element(6)
    assert C.is_primitive_root, "Carbon (Z=6) is a primitive root"

    # 5. Fe-P isomorphism
    Fe = Element(26)
    Phos = Element(15)
    assert Fe.order == Phos.order == 38, "ord(Fe) = ord(P) = 38"

    print("✓ ff229.py: all tests pass")


if __name__ == "__main__":
    verify()
