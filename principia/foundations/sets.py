"""
principia.foundations.sets — Finite Set Operations
==================================================

Mirrors Chapter 0, Section 1 of Principia Psychedelia.

A FiniteSet is a Python object that implements the mathematical
operations on finite sets: membership, cardinality, subset testing,
union, intersection, difference, complement, and power set.

Every operation here has a direct SQL parallel (see the table in Ch.0).

Usage
-----
    python -m principia.foundations.sets

Examples
--------
>>> D = FiniteSet({1, 4, 9, 16, 25})
>>> 9 in D
True
>>> len(D)
5
>>> A = FiniteSet({'a', 'b', 'c'})
>>> print(A.union(FiniteSet({'c', 'd'})))
FiniteSet({'a', 'b', 'c', 'd'})
"""

from __future__ import annotations
from itertools import combinations
from typing import Any, FrozenSet, Iterable, Iterator, Set


class FiniteSet:
    """A finite set with standard set-theoretic operations.

    Internally backed by a Python frozenset for immutability and hashability,
    which lets us put FiniteSets inside other FiniteSets (e.g. power sets).

    Parameters
    ----------
    elements : iterable
        The elements of the set. Duplicates are silently removed.
    """

    def __init__(self, elements: Iterable[Any] = ()) -> None:
        self._data: FrozenSet[Any] = frozenset(elements)

    # ── Membership (∈) ──────────────────────────────────────────
    def __contains__(self, item: Any) -> bool:
        """Test membership: x ∈ S."""
        return item in self._data

    # ── Cardinality (|S|) ───────────────────────────────────────
    def __len__(self) -> int:
        """Return cardinality: |S|."""
        return len(self._data)

    # ── Iteration ───────────────────────────────────────────────
    def __iter__(self) -> Iterator[Any]:
        return iter(self._data)

    # ── Equality ────────────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if isinstance(other, FiniteSet):
            return self._data == other._data
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._data)

    # ── Subset (⊆) ─────────────────────────────────────────────
    def is_subset(self, other: FiniteSet) -> bool:
        """Test if self ⊆ other."""
        return self._data <= other._data

    def is_proper_subset(self, other: FiniteSet) -> bool:
        """Test if self ⊂ other (subset and not equal)."""
        return self._data < other._data

    # ── Union (∪)  ──  SQL: UNION ──────────────────────────────
    def union(self, other: FiniteSet) -> FiniteSet:
        """Return self ∪ other."""
        return FiniteSet(self._data | other._data)

    # ── Intersection (∩)  ──  SQL: INTERSECT ───────────────────
    def intersect(self, other: FiniteSet) -> FiniteSet:
        """Return self ∩ other."""
        return FiniteSet(self._data & other._data)

    # ── Difference (−)  ──  SQL: EXCEPT ────────────────────────
    def difference(self, other: FiniteSet) -> FiniteSet:
        """Return self − other."""
        return FiniteSet(self._data - other._data)

    # ── Complement (S̄ relative to a universe) ──────────────────
    def complement(self, universe: Iterable[Any] | None = None) -> FiniteSet:
        """Return the complement of self relative to universe.

        If universe is None, raises ValueError — complement is only
        defined relative to a known universal set.
        """
        if universe is None:
            raise ValueError(
                "Complement requires a universe. "
                "Pass the universal set as an argument."
            )
        if isinstance(universe, FiniteSet):
            u = universe._data
        else:
            u = frozenset(universe)
        return FiniteSet(u - self._data)

    # ── Cartesian Product (×) ──  SQL: CROSS JOIN ──────────────
    def cartesian_product(self, other: FiniteSet) -> FiniteSet:
        """Return self × other as a set of (a, b) tuples."""
        return FiniteSet((a, b) for a in self._data for b in other._data)

    # ── Power Set P(S) ─────────────────────────────────────────
    def power_set(self) -> FiniteSet:
        """Return P(self): the set of all subsets.

        |P(S)| = 2^|S|, so use with care on large sets.
        """
        elements = list(self._data)
        subsets = []
        for r in range(len(elements) + 1):
            for combo in combinations(elements, r):
                subsets.append(frozenset(combo))
        return FiniteSet(subsets)

    # ── Display ─────────────────────────────────────────────────
    def __repr__(self) -> str:
        # Sort for deterministic display when elements are comparable
        try:
            items = sorted(self._data)
        except TypeError:
            items = list(self._data)
        return f"FiniteSet({{{', '.join(repr(x) for x in items)}}})"


# ── Demo ────────────────────────────────────────────────────────
def _demo() -> None:
    """Run the demonstrations from Chapter 0, Section 1."""
    print("=" * 60)
    print("principia.foundations.sets — Chapter 0 Demo")
    print("=" * 60)

    D = FiniteSet({1, 4, 9, 16, 25})
    A = FiniteSet({'a', 'b', 'c'})

    print(f"\nD = {D}")
    print(f"A = {A}")
    print(f"9 ∈ D? {9 in D}")
    print(f"|D| = {len(D)}")
    print(f"|A| = {len(A)}")

    print(f"\nA ∪ FiniteSet({{'c','d'}}) = {A.union(FiniteSet({'c', 'd'}))}")
    print(f"A ∩ FiniteSet({{'b','c','d'}}) = {A.intersect(FiniteSet({'b', 'c', 'd'}))}")
    print(f"A − FiniteSet({{'c'}}) = {A.difference(FiniteSet({'c'}))}")

    universe = FiniteSet({'a', 'b', 'c', 'd', 'e'})
    print(f"\nUniverse U = {universe}")
    print(f"Complement of A in U = {A.complement(universe)}")

    small = FiniteSet({1, 2, 3})
    ps = small.power_set()
    print(f"\nP({{1,2,3}}) has {len(ps)} subsets:")
    for s in sorted(ps, key=lambda x: (len(x), sorted(x)) if hasattr(x, '__len__') else (0,)):
        print(f"  {set(s) if isinstance(s, frozenset) else s}")

    print(f"\n{'='*60}")
    print("SQL parallels:")
    print("  Set = TABLE    | ∈ = WHERE x IN    | |S| = COUNT(*)")
    print("  ∪ = UNION      | ∩ = INTERSECT     | − = EXCEPT")
    print("  × = CROSS JOIN | ∀ = ALL           | ∃ = EXISTS")
    print("=" * 60)


if __name__ == "__main__":
    _demo()
