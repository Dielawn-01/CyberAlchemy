# Principia Psychedelia — Companion Code

**Teach yourself the algebra by building it in Python.**

If you know Python, you already know the algebra's architecture:
classes are worldmodels, `__mul__` is composition, `@property` is
lazy observation, and κ = -1 is the interface constraint that every
formal system must satisfy.

## Quick Start

```bash
python -m principia              # Run everything
python -m principia logic        # Run Logic layer only
python -m principia information  # Run Information layer only
python -m principia physical     # Run Physical layer only
```

Requirements: Python 3.10+

## The OOP ↔ Algebra Dictionary

| Algebra Concept | OOP Concept | Python |
|----------------|-------------|--------|
| Element of F*₂₂₉ | Object instance | `Element(z)` |
| Multiplication rule | `__mul__` | `a * b` |
| Multiplicative order | Property (computed, cached) | `@property` |
| κ = -1 (associator) | Interface constraint | `assert` |
| CRT decomposition | Composition (has-a) | `.decompose()` → `(force, matter)` |
| CRT recomposition | Factory pattern | `Element.from_components(f, m)` |
| Subgroup C_n | Type hierarchy | Subclass or enum |
| Protoreal → Unreal | Inheritance (is-a) | `class Unreal(Protoreal)` |
| Σ (synthetic integration) | State mutation | `.sigma()` → new state |
| Force skeleton | Abstract base class | The 12 roots of unity |
| Matter content | Mixin / trait | The 19-harmonic elements |
| Transmutation | Decompose → twist → recompose | `.decompose()`, modify, `.from_components()` |

## The Trefoil Structure

The package mirrors the book's three-part **Semantic Condensation**:

```
principia/
├── logic/                         ◀── PART I: LOGICAL CREATIVITY
│   ├── protoreal.py               (a, ω, ι) — the 3-variable seed
│   ├── unreal.py                  (a, ω, ι, ε, λ) — the 5D state machine
│   ├── ff229.py                   F*₂₂₉ Element class with Force × Matter
│   └── problem_landscape/         OOP + Gödel/Tarski → κ = -1
│       ├── ex01_classes.py
│       ├── ex02_self_reference.py
│       ├── ex03_godel.py
│       └── ex05_the_gap.py
│
├── information/                   ◀── PART II: INFORMATIONAL CREATIVITY
│   ├── bio/
│   │   └── receptors.py           Neurotransmitter orbit survey (imports logic)
│   └── markets/                   (Market fluid bridge — coming soon)
│
├── physical/                      ◀── PART III: PHYSICAL CREATIVITY
│   ├── cosmology/
│   │   └── celestial.py           Celestial body magnetic tilt survey (imports logic)
│   ├── vacuum/                    (Casimir/ZPE — coming soon)
│   └── asi/                       (ASI chip DEC engine — coming soon)
│
├── __init__.py
├── __main__.py                    Test runner (trefoil order)
└── README.md
```

Each layer **imports from the layer below**: Physical imports from Logic,
Information imports from Logic. This is the Semantic Condensation invariant:
progress on one axis simultaneously teaches the other two.

## Chapter Map

```
LOGIC (Part I)
  Ch.00  THE PROBLEM LANDSCAPE     OOP basics → Gödel/Tarski → κ = -1
  Ch.01  THE ALGEBRA                Protoreal → Unreal → Force × Matter

INFORMATION (Part II)
  Ch.09  MULTIMODAL MECHANISMS      Neurotransmitter orbit survey
  Ch.15  MARKET FLUID SYSTEMS       Black-Scholes–Navier-Stokes bridge

PHYSICAL (Part III)
  Ch.10  COSMOLOGY                  Celestial body magnetic tilts
  Ch.18  THE REACTOR                Fusion confinement, Lawson, impurities
  Ch.19  THE CHIP                   12/19 architecture, DEC engine
  Ch.20  THE LIFE                   Fe↔P, Krebs, abiogenesis
```

Each exercise is 30–80 lines, self-contained, and runnable standalone.
