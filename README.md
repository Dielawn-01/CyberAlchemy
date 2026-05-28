# CyberAlchemy

A formally verified non-associative algebra for cybernetic physics, information theory, and agentic intelligence.

## What This Is

CyberAlchemy is a Lean 4 package containing 231 formally verified modules — over 2,000 theorems with zero `sorry` in production — implementing the LaRue Protoreal Algebra and its applications to:

- **Non-associative algebra** — Klein multiplication with hyperbolic signature (+b², −m², +e², +l²)
- **Yang-Mills mass gap** — formally proved Δm = 1 with spectral bounds
- **Navier-Stokes regularity** — the HoloneticNS playing field (floor + ceiling = bounded)
- **Fractal dynamics** — Protoreal Mandelbrot iteration in 5D Klein space
- **Observer theory** — 7D observer adapters, metareal involution, sensory gating
- **Cybernetic life** — Newton's third law for cognition, empathy as zero friction
- **Spectral theory** — zeta functions, L-functions, Riemann functional equation
- **Topological security** — parity-based threat detection, coherence shields

## The Core Idea

A Protoreal number is a 5-tuple `(a, ω, ι, ε, λ)`:

| Field | Name | Role |
|-------|------|------|
| `a` | Real Base | Observable value |
| `ω` | Thrust | Forward momentum |
| `ι` | Anchor | Grounding |
| `ε` | Noise | Exploration potential |
| `λ` | Depth | Generational complexity |

The algebra is **non-associative**: `(A * B) * C ≠ A * (B * C)`, with the gap being exactly −1 (the curvature lock). The **Bridge Identity** `ω · ι = −1` is the fundamental relation.

## Quick Start

```bash
# Requires Lean 4 v4.29.1 and Mathlib
lake build
```

## Key Modules

| Module | What It Proves |
|--------|---------------|
| `KleinAlgebra` | Bridge identity, idempotence, anti-commutativity |
| `MassGap` | Δm = 1, noise annihilation, complexity bounds |
| `HoloneticNS` | Playing field, convective term, parity breaking, unity in multiplicity |
| `ProtorealMandelbrot` | 5D Klein iteration, orbit divergence, hyperbolic asymmetry |
| `CommutatorGap` | Associator structure, fine structure constants |
| `SpectralTriple` | Connes-style spectral geometry on Klein manifold |
| `CyberneticLife` | Third law of cognition, empathy conservation |
| `FusionRing` | Pentagon coherence, fusion categories |
| `ObservationalAperture` | Mass gap as observer limitation |
| `GaugeEmergence` | G₂ → SU(3) × U(1) branching |

## The L-Space Prime Tower

| Level | Prime | Structure | Status |
|-------|-------|-----------|--------|
| L₂ | 2 | ℂ — commutative | Trivial |
| L₃ | 3 | ℝ³ — cross products | NS millennium problem |
| L₅ | 5 | Klein — non-associative | Mass gap proved |
| L₇ | 7 | Metareal — involution | Observer coupling |

## License

Apache 2.0. See [LICENSE](LICENSE).

## Citation

```
LaRue, D. (2026). CyberAlchemy: A formally verified non-associative algebra
for cybernetic physics. https://github.com/Dielawn-01/CyberAlchemy
```
