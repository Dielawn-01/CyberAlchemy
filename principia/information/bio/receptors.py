"""
principia.information.bio.receptors
====================================

Neurotransmitters as objects in F*_p.

This module teaches OOP data modeling by mapping molecular weights
onto the gauge prime fields {229, 181, 139}. Each Molecule computes
its own multiplicative order and orbit membership using the same
Element class that the logic layer uses for pure algebra.

The key discovery: L-Tyrosine (MW=181) is the ZERO element at p=181,
making it the algebraic annihilator of the SU(2)/Weak gauge field.
"""

from typing import List
from principia.logic.ff229 import Element

# Gauge prime fields and their golden root orders
GAUGE_PRIMES = [229, 181, 139]
GOLDEN_ORDERS = {229: 114, 181: 90, 139: 46}
CONJUGATE_ORDERS = {229: 57, 181: 45, 139: 23}


def _mult_order(a: int, p: int) -> int:
    """Multiplicative order of a in F*_p."""
    if a % p == 0:
        return 0
    r = a % p
    current = r
    for k in range(1, p):
        if current == 1:
            return k
        current = (current * r) % p
    return p - 1


def _is_in_subgroup(a: int, generator: int, p: int) -> bool:
    """Check if a is in the cyclic subgroup <generator> of F*_p.
    Walks the generator's orbit — O(ord) but correct."""
    if a % p == 0:
        return False
    target = a % p
    current = 1
    for _ in range(p):
        current = (current * generator) % p
        if current == target:
            return True
        if current == 1:
            break
    return False


# Golden roots in each field (the actual generators of the golden orbit)
GOLDEN_ROOTS = {229: 148, 181: 168, 139: 76}
CONJUGATE_ROOTS = {229: 82, 181: 14, 139: 64}


class Molecule:
    """A biochemical compound positioned in the gauge lattice.

    The molecular weight determines the element's position in each
    finite field. The orbit classification follows the same subgroup
    lattice used in the book's Chapter 9.
    """

    def __init__(self, name: str, molecular_weight: int, pathway: str):
        self.name = name
        self.mw = molecular_weight
        self.pathway = pathway
        self._cache = {}

    def residue(self, p: int) -> int:
        """MW mod p — the element's position in F_p."""
        return self.mw % p

    def order(self, p: int) -> int:
        """Multiplicative order in F*_p (0 if annihilator)."""
        key = ("ord", p)
        if key not in self._cache:
            self._cache[key] = _mult_order(self.mw, p)
        return self._cache[key]

    def orbit_type(self, p: int) -> str:
        """Classify into the subgroup lattice of F*_p.

        Uses actual subgroup membership, not just order divisibility.
        An element is "Golden" only if it lives in <φ>, not merely
        if its order divides ord(φ).
        """
        key = ("orbit", p)
        if key not in self._cache:
            r = self.mw % p
            if r == 0:
                self._cache[key] = "Annihilator (ZERO)"
            elif _is_in_subgroup(r, GOLDEN_ROOTS[p], p):
                if _is_in_subgroup(r, CONJUGATE_ROOTS[p], p):
                    self._cache[key] = f"Conjugate (φ̄, ord={self.order(p)})"
                else:
                    self._cache[key] = f"Golden (φ, ord={self.order(p)})"
            else:
                self._cache[key] = f"Exterior (ord={self.order(p)})"
        return self._cache[key]

    def __repr__(self) -> str:
        return f"<Molecule: {self.name} | MW={self.mw} | {self.pathway}>"


class ReceptorSystem:
    """A collection of molecules in a neural environment.

    Teaches aggregation and querying of object state across
    multiple gauge fields simultaneously.
    """

    def __init__(self, name: str):
        self.name = name
        self.molecules: List[Molecule] = []

    def add(self, mol: Molecule):
        self.molecules.append(mol)

    def golden_fraction(self, p: int = 229) -> float:
        """Fraction of molecules in the golden orbit at prime p."""
        if not self.molecules:
            return 0.0
        n = sum(1 for m in self.molecules if "Golden" in m.orbit_type(p))
        return n / len(self.molecules)

    def annihilators(self) -> List[Molecule]:
        """Molecules that are ZERO elements at any gauge prime."""
        return [m for m in self.molecules
                if any(m.residue(p) == 0 for p in GAUGE_PRIMES)]


# ── Database: the 25 compounds from the book's Chapter 9 ──
NEUROTRANSMITTER_DB = [
    # Serotonin pathway
    ("L-Tryptophan",      204, "Serotonin"),
    ("5-HTP",             220, "Serotonin"),
    ("Serotonin",         176, "Serotonin"),
    ("N-Acetylserotonin", 218, "Serotonin"),
    ("Melatonin",         232, "Serotonin"),
    ("Pinoline",          186, "Serotonin"),
    # Kynurenine pathway
    ("Kynurenine",        208, "Kynurenine"),
    ("Kynurenic acid",    189, "Kynurenine"),
    ("3-OH-Kynurenine",   224, "Kynurenine"),
    ("Quinolinic acid",   167, "Kynurenine"),
    ("Picolinic acid",    123, "Kynurenine"),
    # Catecholamine pathway
    ("L-Tyrosine",        181, "Catecholamine"),
    ("L-DOPA",            197, "Catecholamine"),
    ("Dopamine",          153, "Catecholamine"),
    ("Norepinephrine",    169, "Catecholamine"),
    ("Epinephrine",       183, "Catecholamine"),
    # E/I balance
    ("L-Glutamate",       147, "E/I Balance"),
    ("GABA",              103, "E/I Balance"),
    ("Glutamine",         146, "E/I Balance"),
    # Cholinergic / Histaminergic
    ("Acetylcholine",     146, "Cholinergic"),
    ("Histamine",         111, "Histaminergic"),
    # Endocannabinoid
    ("Anandamide",        347, "Endocannabinoid"),
    ("2-AG",              378, "Endocannabinoid"),
]


def main():
    """Build the full neurotransmitter survey — the information layer
    consuming the logic layer's finite field arithmetic."""

    brain = ReceptorSystem("Human CNS")
    for name, mw, pathway in NEUROTRANSMITTER_DB:
        brain.add(Molecule(name, mw, pathway))

    print("═" * 72)
    print("  NEUROTRANSMITTER ORBIT SURVEY (principia.information.bio)")
    print("═" * 72)

    # Header
    print(f"\n  {'Compound':<18s} {'MW':>4s}  {'F₂₂₉':<28s} {'F₁₈₁':<28s}")
    print(f"  {'─'*18} {'─'*4}  {'─'*28} {'─'*28}")

    current_pathway = None
    for mol in brain.molecules:
        if mol.pathway != current_pathway:
            current_pathway = mol.pathway
            print(f"\n  ── {current_pathway} ──")
        o229 = mol.orbit_type(229)
        o181 = mol.orbit_type(181)
        print(f"  {mol.name:<18s} {mol.mw:4d}  {o229:<28s} {o181:<28s}")

    # Annihilator analysis
    zeros = brain.annihilators()
    if zeros:
        print(f"\n{'━'*72}")
        print(f"  ANNIHILATOR ELEMENTS (gauge-field zeros)")
        print(f"{'━'*72}")
        for m in zeros:
            for p in GAUGE_PRIMES:
                if m.residue(p) == 0:
                    print(f"  {m.name} (MW={m.mw}) → ZERO at p={p}")

    # Golden fraction
    print(f"\n  Golden orbit fraction at p=229: "
          f"{brain.golden_fraction(229)*100:.1f}%")
    print(f"  Total NTT bandwidth: "
          f"{CONJUGATE_ORDERS[229]} + {CONJUGATE_ORDERS[181]} + "
          f"{CONJUGATE_ORDERS[139]} = "
          f"{sum(CONJUGATE_ORDERS.values())} = 5³ ✓")


if __name__ == "__main__":
    main()
