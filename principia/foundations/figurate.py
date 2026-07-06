"""
principia.foundations.figurate — Figurate Number Sequences
==========================================================

Mirrors Chapter 0, Section 5 of Principia Psychedelia.

Figurate numbers count the objects needed to form regular polygons
arranged as equidistant dot lattices. The key insight: shapes encode
arithmetic identities, and those identities are discoverable by
visual proof before algebraic proof.

Usage
-----
    python -m principia.foundations.figurate

Key identities
--------------
    T_n = n(n+1)/2                     (triangular)
    n^2 = sum of first n odd numbers   (square via gnomons)
    T_n + T_{n-1} = n^2                (figurate bridge identity)
    P(r, n) = n[(r-2)n - (r-4)] / 2   (general r-gonal number)
"""

from __future__ import annotations


def triangular(n: int) -> int:
    """Return the n-th triangular number T_n = n(n+1)/2.

    The triangular numbers count the dots in an equilateral triangle
    of side-length n. They are also the partial sums of the natural
    numbers: T_n = 1 + 2 + ... + n.

    Parameters
    ----------
    n : int
        Side-length (n >= 0). T_0 = 0 by convention.

    Examples
    --------
    >>> [triangular(k) for k in range(8)]
    [0, 1, 3, 6, 10, 15, 21, 28]
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    return n * (n + 1) // 2


def square(n: int) -> int:
    """Return the n-th square number n^2.

    Each square grows by adding a gnomon (L-shaped border) of size
    2n - 1, giving us: n^2 = sum_{k=1}^{n} (2k - 1).

    Parameters
    ----------
    n : int
        Side-length (n >= 0).

    Examples
    --------
    >>> [square(k) for k in range(8)]
    [0, 1, 4, 9, 16, 25, 36, 49]
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    return n * n


def polygonal(r: int, n: int) -> int:
    """Return the n-th r-gonal (polygonal) number.

    The general formula for the r-gonal number of rank n is:
        P(r, n) = n * [(r-2)*n - (r-4)] / 2

    For r=3: triangular numbers.
    For r=4: square numbers.
    For r=5: pentagonal numbers.
    For r=6: hexagonal numbers.

    Parameters
    ----------
    r : int
        Number of sides of the polygon (r >= 3).
    n : int
        Rank (n >= 0). P(r, 0) = 0 by convention.

    Examples
    --------
    >>> [polygonal(5, k) for k in range(8)]  # pentagonal
    [0, 1, 5, 12, 22, 35, 51, 70]
    """
    if r < 3:
        raise ValueError(f"r must be >= 3 (polygon sides), got {r}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    return n * ((r - 2) * n - (r - 4)) // 2


def gnomon(r: int, n: int) -> int:
    """Return the n-th gnomon for the r-gonal numbers.

    The gnomon is the number of dots added when going from rank n-1
    to rank n: G(r, n) = P(r, n) - P(r, n-1).

    For squares (r=4): gnomon is always 2n-1 (the odd numbers).

    Parameters
    ----------
    r : int
        Number of polygon sides (r >= 3).
    n : int
        Rank (n >= 1).
    """
    if n < 1:
        raise ValueError(f"gnomon is defined for n >= 1, got {n}")
    return polygonal(r, n) - polygonal(r, n - 1)


def dot_triangle(n: int) -> str:
    """Return an ASCII dot diagram of T_n.

    Parameters
    ----------
    n : int
        Side-length of the triangle (n >= 1).

    Returns
    -------
    str
        Multi-line string with centered rows of dots.

    Examples
    --------
    >>> print(dot_triangle(4))
       •
      • •
     • • •
    • • • •
    """
    if n < 1:
        raise ValueError(f"n must be >= 1 for dot diagram, got {n}")
    lines = []
    for row in range(1, n + 1):
        padding = " " * (n - row)
        dots = " ".join("•" for _ in range(row))
        lines.append(padding + dots)
    return "\n".join(lines)


def dot_square(n: int) -> str:
    """Return an ASCII dot diagram of n^2.

    Parameters
    ----------
    n : int
        Side-length of the square (n >= 1).

    Returns
    -------
    str
        Multi-line string with n rows of n dots.

    Examples
    --------
    >>> print(dot_square(3))
    • • •
    • • •
    • • •
    """
    if n < 1:
        raise ValueError(f"n must be >= 1 for dot diagram, got {n}")
    row = " ".join("•" for _ in range(n))
    return "\n".join(row for _ in range(n))


# ── Demo ────────────────────────────────────────────────────────
def _demo() -> None:
    """Run the demonstrations from Chapter 0, Section 5."""
    print("=" * 60)
    print("principia.foundations.figurate — Chapter 0 Demo")
    print("=" * 60)

    # Triangular numbers
    tri = [triangular(n) for n in range(1, 11)]
    print(f"\nTriangular numbers T_1..T_10: {tri}")
    print(f"\nDot diagram for T_5:")
    print(dot_triangle(5))

    # Square numbers
    sq = [square(n) for n in range(1, 11)]
    print(f"\nSquare numbers 1²..10²: {sq}")
    print(f"\nDot diagram for 4²:")
    print(dot_square(4))

    # Gnomon identity: squares grow by odd numbers
    print("\nGnomons for squares (should be odd numbers):")
    for n in range(1, 8):
        print(f"  4² gnomon at n={n}: {gnomon(4, n)} = 2·{n}−1 = {2*n-1}")

    # Figurate bridge identity: T_n + T_{n-1} = n²
    print("\nFigurate bridge identity: T_n + T_{n-1} = n²")
    for n in range(1, 11):
        lhs = triangular(n) + triangular(n - 1)
        rhs = square(n)
        status = "✓" if lhs == rhs else "✗"
        print(f"  n={n:2d}: T_{n} + T_{n-1} = {lhs:4d} = {rhs:4d} = {n}²  {status}")

    # Pentagonal numbers
    pent = [polygonal(5, n) for n in range(1, 11)]
    print(f"\nPentagonal numbers P(5,1)..P(5,10): {pent}")

    # Hexagonal numbers
    hexn = [polygonal(6, n) for n in range(1, 11)]
    print(f"Hexagonal numbers P(6,1)..P(6,10): {hexn}")

    # Verify general formula reduces to specific cases
    print("\nVerification: P(3,n) = T_n and P(4,n) = n²")
    for n in range(1, 8):
        assert polygonal(3, n) == triangular(n), f"Failed at n={n}"
        assert polygonal(4, n) == square(n), f"Failed at n={n}"
    print("  All checks passed ✓")

    print(f"\n{'='*60}")


if __name__ == "__main__":
    _demo()
