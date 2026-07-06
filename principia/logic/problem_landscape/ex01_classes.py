"""Exercise 1: Classes Are Worldmodels.

OOP LESSON:
  - __init__ defines what an object IS
  - __mul__ defines how objects INTERACT
  - __repr__ defines how objects DESCRIBE themselves
  - A class is a formal system: it has rules, those rules generate behavior

RUN: python -m principia.logic.problem_landscape.ex01_classes
"""


class Number:
    """A number that knows its own value and how to multiply.

    This is the simplest possible worldmodel: objects that have identity
    (value) and a composition rule (multiplication).
    """

    def __init__(self, value: int):
        self.value = value

    def __mul__(self, other: "Number") -> "Number":
        return Number(self.value * other.value)

    def __repr__(self) -> str:
        return f"Number({self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        return self.value == other.value


def main():
    # Build a worldmodel:
    a = Number(3)
    b = Number(7)
    c = a * b
    print(f"{a} × {b} = {c}")

    # This class IS a formal system:
    # - It has objects (Number instances)
    # - It has a composition rule (__mul__)
    # - It has a description rule (__repr__)
    assert c == Number(21), "3 × 7 = 21"
    assert a * Number(1) == a, "Multiplicative identity"

    # Closure: multiplication stays in the system
    for i in range(1, 10):
        for j in range(1, 10):
            result = Number(i) * Number(j)
            assert isinstance(result, Number), "Closure"

    print("✓ Classes are worldmodels. Objects compose under rules.")
    print()
    print("Question: can this class fully DESCRIBE itself?")
    print("That is: can Number write a method that checks ALL its own truths?")
    print("→ See ex02_self_reference.py")


if __name__ == "__main__":
    main()
