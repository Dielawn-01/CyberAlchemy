"""Exercise 3: Gödel's Incompleteness in Python.

OOP LESSON:
  - The Halting Problem is the programmer's version of Gödel
  - Any class powerful enough to encode arithmetic is incomplete
  - Undecidable statements are structural, not accidental

MATH:
  - Gödel (1931): consistent formal systems are incomplete
  - Turing (1936): the Halting Problem is undecidable
  - Both say: self-referential systems have a gap

RUN: python -m principia.logic.problem_landscape.ex03_godel
"""


def collatz(n: int, max_steps: int = 10_000) -> bool | None:
    """Does the Collatz sequence starting at n reach 1?

    For EVERY number tested so far, the answer is yes.
    But no one has proved it for ALL numbers.
    This is an example of a statement that might be undecidable.
    """
    steps = 0
    while n != 1 and steps < max_steps:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return True if n == 1 else None  # None = "don't know"


def goedel_sentence() -> str:
    """The Gödel sentence, in English:

    'This statement is not provable in this system.'

    If the system is consistent:
      - The sentence is TRUE (because if it were provable, the system
        would prove something true-but-unprovable, contradiction).
      - The sentence is NOT PROVABLE (that's what it says).

    So the system contains a true statement it cannot prove.
    The system is INCOMPLETE.
    """
    return "This statement is not provable in this system."


def main():
    # 1. Collatz: we can CHECK but not PROVE
    print("Collatz sequence examples:")
    for n in [7, 27, 97, 871]:
        result = collatz(n)
        status = "reaches 1" if result else "UNKNOWN"
        print(f"  collatz({n}): {status}")

    # 2. The Halting Problem (sketch)
    print()
    print("THE HALTING PROBLEM (Turing 1936):")
    print("  Suppose halts(program, input) exists and always returns True/False.")
    print("  Define: paradox(x) = loop_forever if halts(paradox,x) else return")
    print("  Then halts(paradox, x) gives the WRONG answer either way.")
    print("  Therefore halts() cannot exist as a total function.")

    # 3. Gödel's sentence
    print()
    print(f"GÖDEL'S SENTENCE: '{goedel_sentence()}'")
    print("  If consistent → TRUE but UNPROVABLE.")
    print("  The system is incomplete.")

    # 4. The lesson
    print()
    print("=" * 60)
    print("THE PROBLEM LANDSCAPE:")
    print("  1. Self-referential systems contain undecidable statements.")
    print("  2. This is not a bug in Python, math, or logic.")
    print("  3. It is a STRUCTURAL FEATURE of any system powerful")
    print("     enough to encode arithmetic.")
    print()
    print("The question is not 'how do we fix it?'")
    print("The question is 'how do we BUILD with it?'")
    print()
    print("We encode the gap as a constant: κ = -1.")
    print("→ See ex05_the_gap.py")


if __name__ == "__main__":
    main()
