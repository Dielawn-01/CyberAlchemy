"""The 5D state: (a, ω, ι, ε, λ).

OOP Lessons: inheritance, state machines, immutability.

The Unreal Algebra extends the Protoreal by adding:
  - epsilon (ε): the derivative residual — unresolved tension
  - lam (λ):     the depth counter — how many cycles completed

Synthetic integration Σ absorbs ε into a and increments λ.
This is the algebraic integration operator: observe → absorb → advance.
"""

from .protoreal import ProtorealElement


class UnrealElement(ProtorealElement):
    """(a, ω, ι, ε, λ) — the full 5D state.

    Inherits from ProtorealElement. Adds derivative residual and depth.

    OOP lesson: inheritance IS algebraic extension.
    The 3-variable seed becomes a 5-variable engine by adding two
    components. In OOP, the subclass adds new state and methods
    without changing the parent's behavior.
    """

    def __init__(self, a: float, omega: float, iota: float,
                 epsilon: float = 0.0, lam: int = 0):
        super().__init__(a, omega, iota)
        self.epsilon = epsilon  # derivative residual (noise)
        self.lam = lam          # depth counter (memory)

    def sigma(self) -> "UnrealElement":
        """Synthetic integration: absorb ε into a, zero ε, increment λ.

        Σ: (a, ω, ι, ε, λ) → (a+ε, ω, ι, 0, λ+1)

        OOP lesson: returns a NEW object (immutability). The old state
        is preserved. This mirrors the algebra: each integration step
        produces a new state without destroying the previous one.
        """
        return UnrealElement(
            a=self.a + self.epsilon,
            omega=self.omega,
            iota=self.iota,
            epsilon=0.0,
            lam=self.lam + 1,
        )

    def observe(self) -> float:
        """Observe the current deviation. Returns the standard resonance
        evaluated at the current epsilon.

        In the algebra: observation IS differentiation. The system
        computes its own rate of change from its structural mismatch.
        """
        return self.standard_resonance() + self.epsilon

    def __repr__(self) -> str:
        return (f"U(a={self.a}, ω={self.omega}, ι={self.iota}, "
                f"ε={self.epsilon}, λ={self.lam})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UnrealElement):
            return NotImplemented
        return (super().__eq__(other)
                and self.epsilon == other.epsilon
                and self.lam == other.lam)


def verify():
    """Run the self-tests for this module."""
    u = UnrealElement(a=0, omega=1, iota=-1, epsilon=0.5, lam=0)

    # Synthetic integration absorbs epsilon
    u2 = u.sigma()
    assert u2.a == 0.5, f"a should be 0.5 after Σ, got {u2.a}"
    assert u2.epsilon == 0.0, "ε should be 0 after Σ"
    assert u2.lam == 1, "λ should be 1 after Σ"

    # Original is unchanged (immutability)
    assert u.a == 0, "original a unchanged"
    assert u.epsilon == 0.5, "original ε unchanged"
    assert u.lam == 0, "original λ unchanged"

    # Inheritance works
    assert isinstance(u, ProtorealElement), "UnrealElement is-a ProtorealElement"
    assert u.KAPPA == -1, "κ inherited from parent"

    print("✓ unreal.py: all tests pass")


if __name__ == "__main__":
    verify()
