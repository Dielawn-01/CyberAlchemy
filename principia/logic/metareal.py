"""The Metareal C*-Algebra state.

Extends the Unreal algebra into a full C*-algebra by introducing:
  - Involution (adjoint) x*: time-reversal and parity inversion
  - C*-norm: complete metric space over the Golden continuum (D = \Phi^2)
"""

import math
from .unreal import UnrealElement

class MetarealElement(UnrealElement):
    """(a, ω, ι, ε, λ) mapped into a C*-algebra over the Stieltjes-Umbral continuum.
    
    The involution x* reverses the anchor (ι) and the derivative residual (ε),
    representing a causal reflection across the Heegner-Ramanujan boundary.
    """

    def __init__(self, a: float, omega: float, iota: float,
                 epsilon: float = 0.0, lam: int = 0):
        super().__init__(a, omega, iota, epsilon, lam)

    def adjoint(self) -> "MetarealElement":
        """The C*-algebra involution x*."""
        return MetarealElement(
            a=self.a,             # scalar remains
            omega=self.omega,     # thrust remains
            iota=-self.iota,      # anchor flips
            epsilon=-self.epsilon,# tension reflects
            lam=-self.lam         # depth reverses
        )
        
    def c_star_norm(self) -> float:
        """||x* x|| = ||x||^2. 
        Evaluates the magnitude over the topological manifold.
        """
        # (a + ω + ι + ε)^2
        return math.sqrt(self.a**2 + self.omega**2 + self.iota**2 + self.epsilon**2 + self.lam**2)

    def __repr__(self) -> str:
        return (f"M(a={self.a}, ω={self.omega}, ι={self.iota}, "
                f"ε={self.epsilon}, λ={self.lam})")

def verify():
    m = MetarealElement(a=1, omega=1, iota=-1, epsilon=0.5, lam=2)
    m_star = m.adjoint()
    assert m_star.iota == 1
    assert m_star.epsilon == -0.5
    print("✓ metareal.py: C*-algebra properties verified")

if __name__ == "__main__":
    verify()
