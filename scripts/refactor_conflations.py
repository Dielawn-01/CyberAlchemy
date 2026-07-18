import os
import re

TARGET_DIR = "/home/phrxmaz/Documents/CyberAlchemy/papers"

REPLACEMENTS = [
    (
        "converting an algorithmically undecidable Halting Problem over \\mathbb{Z} into a strictly decidable polynomial-time algebraic evaluation over \\mathbb{F}_{229}",
        "bypassing the algorithmically undecidable Halting Problem over \\mathbb{Z} by restricting the state space to a strictly decidable polynomial-time algebraic evaluation over \\mathbb{F}_{229}. This provides a finite, bounded halting guarantee, though it does not resolve the generalized uncomputability of Turing machines with infinite tapes"
    ),
    (
        "If the finite-field manifold maps correctly to physical reality, the \\emph{Riemann Hypothesis} emerges as a structural consequence of that geometry.",
        "If the finite-field manifold maps correctly to physical reality, the \\emph{Riemann Hypothesis} emerges as a physical heuristic and minimum-energy attractor state of that geometry. It is important to state clearly that this establishes a necessary structural condition in a physical model, not a sufficiency proof for the global mathematical conjecture in analytic number theory."
    ),
    (
        "If the finite-field manifold maps correctly to physical reality, the \\emph{Riemann Hypothesis} emerges as a structural consequence of non-associative geometry --- a conjecture that the algebra is specifically designed to test.",
        "If the finite-field manifold maps correctly to physical reality, the \\emph{Riemann Hypothesis} emerges as a physical heuristic and minimum-energy attractor state of that geometry. It is important to state clearly that this establishes a necessary structural condition in a physical model, not a sufficiency proof for the global mathematical conjecture in analytic number theory."
    ),
    (
        "we establish this bound as a strict computational limit:",
        "we establish this geometry as a local finite-field equilibrium:"
    ),
    (
        "Unreal Riemann Hypothesis (the continuous spectral attractor)",
        "Unreal Riemann Geometry (the continuous spectral attractor)"
    ),
    (
        "G\\\"odel's incompleteness is the engine, not the obstacle.",
        "G\\\"odel's incompleteness provides the structural friction (the entropy engine) for continuous motion, rather than an obstacle to be circumvented."
    ),
    (
        "converting the halting problem from an undecidable",
        "bypassing the halting problem from an undecidable"
    ),
    (
        "Halting Problem over \\mathbb{Z} becomes a strictly decidable",
        "Halting Problem over \\mathbb{Z} is bypassed by a strictly decidable"
    )
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for old_str, new_str in REPLACEMENTS:
        content = content.replace(old_str, new_str)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
        return True
    return False

def main():
    changed = 0
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".tex"):
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    changed += 1
    print(f"Finished. Modified {changed} files.")

if __name__ == "__main__":
    main()
