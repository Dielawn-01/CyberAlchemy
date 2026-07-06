"""Run all Principia Psychedelia exercises.

Usage:
    python -m principia                     # Run everything
    python -m principia ch00                # Run Chapter 0 only
    python -m principia core                # Run core module tests only
"""

import sys
import importlib
import traceback

CHAPTERS = {
    "logic": [
        "principia.logic.protoreal",
        "principia.logic.unreal",
        "principia.logic.ff229",
        "principia.logic.problem_landscape.ex01_classes",
        "principia.logic.problem_landscape.ex02_self_reference",
        "principia.logic.problem_landscape.ex03_godel",
        "principia.logic.problem_landscape.ex05_the_gap",
    ],
    "information": [
        "principia.information.bio.receptors",
    ],
    "physical": [
        "principia.physical.cosmology.celestial",
    ]
}


def run_module(module_name: str) -> bool:
    """Import and run a module's main() or verify() function."""
    try:
        mod = importlib.import_module(module_name)
        if hasattr(mod, "main"):
            mod.main()
        elif hasattr(mod, "verify"):
            mod.verify()
        else:
            print(f"  ⚠ {module_name}: no main() or verify()")
            return True
        return True
    except Exception:
        print(f"  ✗ {module_name}: FAILED")
        traceback.print_exc()
        return False


def main():
    # Parse arguments
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(CHAPTERS.keys())

    total = 0
    passed = 0
    failed = []

    for chapter in targets:
        if chapter not in CHAPTERS:
            print(f"Unknown chapter: {chapter}")
            print(f"Available: {', '.join(CHAPTERS.keys())}")
            sys.exit(1)

        print(f"\n{'═' * 60}")
        print(f"  {chapter.upper()}")
        print(f"{'═' * 60}\n")

        for module_name in CHAPTERS[chapter]:
            total += 1
            short = module_name.split(".")[-1]
            print(f"── {short} ──")
            if run_module(module_name):
                passed += 1
            else:
                failed.append(module_name)
            print()

    # Summary
    print(f"\n{'═' * 60}")
    print(f"  RESULTS: {passed}/{total} passed")
    if failed:
        print(f"  FAILED: {', '.join(failed)}")
    else:
        print("  All exercises passed ✓")
    print(f"{'═' * 60}")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
