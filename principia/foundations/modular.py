"""
principia.foundations.modular — Modular Arithmetic and Finite Fields
====================================================================

Mirrors Chapter 0, Section 6 of Principia Psychedelia.

ModularInt represents an element of Z/nZ (integers modulo n).
When n is prime, Z/nZ is a finite field F_p: every nonzero element
has a multiplicative inverse.

This module is the bridge from Chapter 0 to Chapter 1 (Unreal Algebra).
The challenge exercise at the end asks: for which primes p < 100 does
X² - X - 1 = 0 have roots in F_p?

Usage
-----
    python -m principia.foundations.modular
"""

from __future__ import annotations
from math import gcd
from typing import Iterator


class ModularInt:
    """An element of Z/nZ with arithmetic operations.

    Parameters
    ----------
    value : int
        The integer value (will be reduced mod n).
    modulus : int
        The modulus n (must be >= 2).

    Examples
    --------
    >>> a = ModularInt(3, 7)
    >>> b = ModularInt(5, 7)
    >>> a + b
    ModularInt(1, mod=7)
    >>> a * b
    ModularInt(1, mod=7)
    >>> a ** 6
    ModularInt(1, mod=7)
    """

    __slots__ = ("value", "modulus")

    def __init__(self, value: int, modulus: int) -> None:
        if modulus < 2:
            raise ValueError(f"Modulus must be >= 2, got {modulus}")
        self.modulus = modulus
        self.value = value % modulus

    def _check_mod(self, other: ModularInt) -> None:
        if self.modulus != other.modulus:
            raise ValueError(
                f"Cannot mix moduli {self.modulus} and {other.modulus}"
            )

    # ── Arithmetic ──────────────────────────────────────────────
    def __add__(self, other: ModularInt) -> ModularInt:
        self._check_mod(other)
        return ModularInt(self.value + other.value, self.modulus)

    def __sub__(self, other: ModularInt) -> ModularInt:
        self._check_mod(other)
        return ModularInt(self.value - other.value, self.modulus)

    def __mul__(self, other: ModularInt | int) -> ModularInt:
        if isinstance(other, int):
            return ModularInt(self.value * other, self.modulus)
        self._check_mod(other)
        return ModularInt(self.value * other.value, self.modulus)

    def __rmul__(self, other: int) -> ModularInt:
        return ModularInt(self.value * other, self.modulus)

    def __pow__(self, exp: int) -> ModularInt:
        return ModularInt(pow(self.value, exp, self.modulus), self.modulus)

    def __neg__(self) -> ModularInt:
        return ModularInt(-self.value, self.modulus)

    # ── Inverse (only exists when gcd(value, modulus) = 1) ─────
    def inverse(self) -> ModularInt:
        """Return the multiplicative inverse of self in Z/nZ.

        Uses the extended Euclidean algorithm. Raises ValueError
        if the inverse does not exist (gcd(value, modulus) != 1).

        In a prime field F_p, every nonzero element has an inverse.
        """
        if self.value == 0:
            raise ValueError("Zero has no multiplicative inverse")
        g, x, _ = _extended_gcd(self.value, self.modulus)
        if g != 1:
            raise ValueError(
                f"{self.value} has no inverse mod {self.modulus} "
                f"(gcd = {g})"
            )
        return ModularInt(x, self.modulus)

    def __truediv__(self, other: ModularInt) -> ModularInt:
        self._check_mod(other)
        return self * other.inverse()

    # ── Comparison ──────────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if isinstance(other, ModularInt):
            return self.value == other.value and self.modulus == other.modulus
        if isinstance(other, int):
            return self.value == other % self.modulus
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.value, self.modulus))

    def __bool__(self) -> bool:
        return self.value != 0

    # ── Display ─────────────────────────────────────────────────
    def __repr__(self) -> str:
        return f"ModularInt({self.value}, mod={self.modulus})"

    def __str__(self) -> str:
        return f"{self.value} (mod {self.modulus})"

    # ── Order ───────────────────────────────────────────────────
    def multiplicative_order(self) -> int:
        """Return the multiplicative order of self in (Z/nZ)*.

        The order is the smallest positive integer k such that
        self^k ≡ 1 (mod n). Raises ValueError if self is 0 or
        if gcd(self.value, n) != 1.
        """
        if self.value == 0 or gcd(self.value, self.modulus) != 1:
            raise ValueError(
                f"{self.value} is not in (Z/{self.modulus}Z)*"
            )
        power = ModularInt(self.value, self.modulus)
        for k in range(1, self.modulus):
            if power.value == 1:
                return k
            power = power * self
        raise RuntimeError("Should not reach here for valid input")


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm: returns (gcd, x, y) with ax + by = gcd."""
    if a == 0:
        return b, 0, 1
    g, x1, y1 = _extended_gcd(b % a, a)
    return g, y1 - (b // a) * x1, x1


# ── Utility functions ───────────────────────────────────────────

def is_prime(n: int) -> bool:
    """Test primality by trial division. Sufficient for pedagogical use."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(limit: int) -> list[int]:
    """Return all primes up to limit (inclusive)."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


def elements_of(p: int) -> list[ModularInt]:
    """Return all elements of Z/pZ as ModularInt objects."""
    return [ModularInt(k, p) for k in range(p)]


def units_of(p: int) -> list[ModularInt]:
    """Return all units (nonzero elements) of F_p."""
    return [ModularInt(k, p) for k in range(1, p)]


def golden_roots(p: int) -> list[ModularInt] | None:
    """Find roots of X² - X - 1 in F_p, if they exist.

    Returns a list of 0 or 2 roots (the golden ratio and its
    conjugate in F_p). Returns None if p is not prime.

    This is the bridge to Chapter 1: The Unreal Algebra.

    The discriminant of X² - X - 1 is 5, so roots exist in F_p
    if and only if 5 is a quadratic residue mod p (by quadratic
    reciprocity, this happens when p ≡ ±1 mod 5).
    """
    if not is_prime(p):
        return None
    roots = []
    for x in range(p):
        if (x * x - x - 1) % p == 0:
            roots.append(ModularInt(x, p))
    return roots if roots else []


# ── Demo ────────────────────────────────────────────────────────
def _demo() -> None:
    """Run the demonstrations from Chapter 0, Section 6."""
    print("=" * 60)
    print("principia.foundations.modular — Chapter 0 Demo")
    print("=" * 60)

    # Basic modular arithmetic in F_7
    print("\n── Arithmetic in F_7 ──")
    a = ModularInt(3, 7)
    b = ModularInt(5, 7)
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  a + b = {a + b}")
    print(f"  a * b = {a * b}  ← 3 and 5 are inverses in F_7!")
    print(f"  a⁶ = {a ** 6}  ← Fermat's Little Theorem")

    # Multiplicative inverses in F_7
    print("\n── Inverses in F_7 ──")
    for k in range(1, 7):
        m = ModularInt(k, 7)
        inv = m.inverse()
        print(f"  {k}⁻¹ ≡ {inv.value} (mod 7)    check: {k}·{inv.value} = {(k * inv.value) % 7}")

    # Multiplicative orders in F_7
    print("\n── Multiplicative orders in F_7* ──")
    for k in range(1, 7):
        m = ModularInt(k, 7)
        print(f"  ord({k}) = {m.multiplicative_order()}")

    # The bridge to Chapter 1: golden roots in finite fields
    print("\n── Bridge to Ch.1: X² - X - 1 = 0 in F_p ──")
    print("  Primes p < 100 where X² - X - 1 splits:")
    splitting_primes = []
    for p in primes_up_to(100):
        roots = golden_roots(p)
        if roots:
            splitting_primes.append(p)
            r_vals = [r.value for r in roots]
            print(f"    p = {p:3d}: roots = {r_vals}  (p mod 5 = {p % 5})")

    print(f"\n  Pattern: the polynomial splits when p ≡ ±1 (mod 5)")
    print(f"  Non-splitting primes have p ≡ ±2 (mod 5) or p = 5")

    # Verify the pattern
    for p in splitting_primes:
        assert p == 5 or p % 5 in (1, 4), f"Pattern broken at p={p}"
    print("  Pattern verified ✓")

    # Verify root properties for p = 229 (the book's prime)
    if is_prime(229):
        print(f"\n── Sneak peek: F_229 (the book's prime) ──")
        roots = golden_roots(229)
        if roots:
            phi, phibar = roots
            print(f"  φ = {phi.value}, φ̄ = {phibar.value}")
            print(f"  φ + φ̄ = {(phi + phibar).value}  (should be 1)")
            print(f"  φ · φ̄ = {(phi * phibar).value}  (should be {229-1} ≡ -1)")
            print(f"  φ² = φ + 1?  {(phi**2).value} = {(phi + ModularInt(1, 229)).value}  ✓" if (phi**2).value == (phi + ModularInt(1, 229)).value else "  ✗")

    print(f"\n{'='*60}")


if __name__ == "__main__":
    _demo()
