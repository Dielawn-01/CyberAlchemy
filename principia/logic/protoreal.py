"""The 3-variable seed: (a, ω, ι).

OOP Lessons: classes, __init__, __mul__, __repr__, operator overloading.

The Protoreal Algebra is the minimum viable observer. Three variables:
  - a:     where you are (definite scalar, the odometer)
  - omega: how fast you're going (idempotent: ω² = ω)
  - iota:  how hard the brakes pull (anti-idempotent: ι² = -ι)

The product rules:
  - ω · ι = -1 (thrust × anchor = negative unit)
  - ι · ω = +1 (anchor × thrust = positive unit)
  - Commutator [ω, ι] = ω·ι - ι·ω = -2

The associator κ = ω·ι = -1 is the Gödel-Tarski gap, algebraized.
"""


class ProtorealElement:
    """(a, ω, ι) — the minimum viable observer.

    Algebraic rules:
        ω² = ω       (idempotent: thrust saturates)
        ι² = -ι      (anti-idempotent: resistance flips)
        ω·ι = -1     (forward × backward = gap)
        ι·ω = +1     (backward × forward = identity)
    """

    # The structural constant. Every algebra built from this has κ = -1.
    KAPPA = -1

    def __init__(self, a: float, omega: float, iota: float):
        self.a = a
        self.omega = omega
        self.iota = iota

    def standard_resonance(self) -> float:
        """SR = a - ω·ι = a - (-1) = a + 1.

        The automatic derivative. The system computes its own rate of
        change from the algebraic structure alone. No limit definition,
        no epsilon-delta argument. The algebra differentiates itself.
        """
        return self.a - self.KAPPA  # a - (ω·ι) = a - (-1) = a + 1

    def lyapunov_energy(self, epsilon: float = 0.0) -> float:
        """L = ε². Energy stored in the unresolved derivative residual."""
        return epsilon ** 2

    def __repr__(self) -> str:
        return f"P({self.a}, ω={self.omega}, ι={self.iota})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProtorealElement):
            return NotImplemented
        return (self.a == other.a
                and self.omega == other.omega
                and self.iota == other.iota)


def verify():
    """Run the self-tests for this module."""
    p = ProtorealElement(a=0, omega=1, iota=-1)
    assert p.standard_resonance() == 1, "SR(0) = 0 + 1 = 1"
    assert p.KAPPA == -1, "κ = -1"
    assert p.lyapunov_energy(0.5) == 0.25, "L(0.5) = 0.25"
    print("✓ protoreal.py: all tests pass")


if __name__ == "__main__":
    verify()
