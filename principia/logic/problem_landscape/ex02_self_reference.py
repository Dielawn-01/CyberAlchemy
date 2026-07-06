"""Exercise 2: The Self-Reference Problem.

OOP LESSON:
  - What happens when a class tries to reason about itself
  - The gap between what an object IS and what it can SAY about itself
  - Why a general self-verification method cannot exist

RUN: python -m principia.logic.problem_landscape.ex02_self_reference
"""


class SelfAware:
    """A class that tries to answer questions about itself."""

    def __init__(self, value: int):
        self.value = value

    def am_i_positive(self) -> bool:
        """Can I tell if I'm positive? Yes — this is a specific claim."""
        return self.value > 0

    def am_i_even(self) -> bool:
        """Can I tell if I'm even? Yes — another specific claim."""
        return self.value % 2 == 0

    def describe(self) -> str:
        """Can I describe myself? Yes — but only my known attributes."""
        return f"SelfAware({self.value})"

    def check_claim(self, method_name: str) -> bool:
        """Can I check if one of my own methods is truthful?

        For INDIVIDUAL claims, yes. We can call the method and compare
        to direct computation. But this only works for methods we
        explicitly enumerate...
        """
        method = getattr(self, method_name)
        result = method()

        # Manual ground truth for known methods:
        ground_truth = {
            "am_i_positive": self.value > 0,
            "am_i_even": self.value % 2 == 0,
        }

        if method_name in ground_truth:
            return result == ground_truth[method_name]

        # For unknown methods, we CANNOT verify — we'd need a general
        # truth predicate, and Tarski proved that's impossible.
        raise ValueError(
            f"Cannot verify '{method_name}': no ground truth available. "
            "A general truth predicate does not exist (Tarski, 1936)."
        )


def main():
    x = SelfAware(5)
    print(x.describe())

    # Individual claims work fine:
    assert x.check_claim("am_i_positive") is True
    assert x.check_claim("am_i_even") is True  # 5 is not even → both False

    print(f"  am_i_positive? {x.am_i_positive()} — verified ✓")
    print(f"  am_i_even?     {x.am_i_even()} — verified ✓")

    # But a GENERAL verifier fails:
    try:
        x.check_claim("describe")
    except ValueError as e:
        print(f"\n  General verification fails: {e}")

    print()
    print("LESSON: Self-referential systems can verify INDIVIDUAL claims")
    print("but cannot have a GENERAL truth predicate (Tarski, 1936).")
    print("The gap between specific and general is structural.")
    print("→ See ex03_godel.py")


if __name__ == "__main__":
    main()
