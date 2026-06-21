import LaRueProtorealAlgebra.ProtorealManifold
import InfoPhysAxioms.ProtorealMetric
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.OctonionGrowth
import InfoPhysAxioms.RiemannObserver
import InfoPhysAxioms.EnumerationSystems

/-!
# MetagraphOracle: Torsion-Filtered External Signal Injection

**Authors:** LaRue (Theory)

## Core Claim

External stochastic signals (e.g., Bittensor metagraph emissions)
can be injected into the encoder's noise component ε without
disrupting crystallization, provided the injection is filtered
through the torsion coupling.

## The Observational L-Function Scaling

From OctonionGrowth.observation_depth_proportionality:
  torsion_el(crystallized_observer, noise) = λ × ε

This means observation coupling scales with DEPTH, not inversely
with distance. This is the anti-inverse-square law:
  - In physics: F ∝ 1/r² (far = weak)
  - In InfoPhys: coupling ∝ λ (deep = strong)

The scaling is not polynomial — it's L-function class:
  - λ grows as superlog(info) (EnumerationSystems.lambda_is_superlog)
  - Each semantic shift expands Σ (RiemannObserver.shift_expands_observable)
  - The observation tower preserves parity (tower_preserves_thrust)
  - At each level, the L-function reveals MORE structure

The Bittensor metagraph is an external noise field (emissions).
The encoder's depth λ determines HOW MUCH of that field it couples with.
A shallow encoder ignores the market. A deep encoder resolves it.

## The Two-Plane Decomposition

From OctonionGrowth.observation_decomposes:
  total_torsion = torsion_bm + torsion_el
                = structural  + depth × noise

The bm-plane is CONSTANT (κ = -1 at the generators).
The el-plane SCALES WITH DEPTH.

At the fuzzy point (total = κ = -1):
  ε_critical = (κ - bm_torsion) / λ

Deeper observers need LESS noise to reach κ.
The observation saturates faster at depth.

## The SR Gate as Critical Line

SR(u) = a - b·m. When SR > 0, the encoder is in observer mode.
This corresponds to being ABOVE the critical line.
When SR < 0, crystallization mode — BELOW the critical line.
SR = 0 IS the critical line boundary.

The injection rule (inject only when SR > 0) is equivalent to:
"only observe when above the critical line."
-/

namespace MetagraphOracle

open ProtorealManifold
open OctonionGrowth

-- ════════════════════════════════════════════════════
-- SECTION 1: METAGRAPH SIGNAL AS EM PROBE
-- ════════════════════════════════════════════════════

/-- A metagraph signal is structurally identical to an em_probe:
    pure noise at zero depth. It carries emission (ε) but has
    no structural components (b = m = 0).
    
    This is the Bittensor marketplace as an EM field:
    emissions are photons, stakes are charge, trust is crystal. -/
def metagraph_signal (emission stake trust : ℝ) : ProtorealManifold :=
  { a := trust, b := stake, m := 0, e := emission, l := 0 }

/-- A pure emission signal (no stake, no trust) IS an em_probe.
    This connects MetagraphOracle to RiemannObserver. -/
theorem pure_emission_is_probe (emission : ℝ) :
    (⟨0, 0, 0, emission, 0⟩ : ProtorealManifold) =
    RiemannObserver.em_probe emission 0 := by
  unfold RiemannObserver.em_probe; rfl

-- ════════════════════════════════════════════════════
-- SECTION 2: DEPTH-PROPORTIONAL COUPLING
-- ════════════════════════════════════════════════════

/-- **THE METAGRAPH COUPLING THEOREM**
    When a crystallized encoder at depth λ receives a pure
    emission signal, the coupling is exactly λ × emission.
    
    This is a direct application of observation_depth_proportionality
    from OctonionGrowth. -/
theorem metagraph_coupling_proportional_to_depth
    (encoder : ProtorealManifold) (emission : ℝ)
    (h_crystal : encoder.e = 0) :
    torsion_el encoder ⟨0, 0, 0, emission, 0⟩ =
    encoder.l * emission :=
  observation_depth_proportionality encoder emission h_crystal

/-- **SHALLOW ENCODER IGNORES THE MARKET**
    An encoder at depth 0 has zero el-plane coupling with
    any emission signal. It literally cannot observe the market. -/
theorem shallow_ignores_market
    (emission : ℝ) (encoder : ProtorealManifold)
    (h_crystal : encoder.e = 0) (h_shallow : encoder.l = 0) :
    torsion_el encoder ⟨0, 0, 0, emission, 0⟩ = 0 := by
  have := metagraph_coupling_proportional_to_depth encoder emission h_crystal
  rw [h_shallow] at this
  simp at this ⊢
  exact this

/-- **EACH FUNCT STEP OPENS THE CHANNEL**
    After n synthetic_integration steps, the encoder's coupling with emission
    noise increases by exactly n. Each crystallization step
    makes the encoder a BETTER observer of the market. -/
theorem synthetic_integration_opens_channel
    (u : ProtorealManifold) (n : ℕ) (emission : ℝ)
    (h : n ≥ 1) :
    torsion_el (ProtorealMetric.synthetic_integration_iterate n u) ⟨0, 0, 0, emission, 0⟩ =
    (u.l + n) * emission :=
  deeper_observer_stronger_coupling u n emission h

-- ════════════════════════════════════════════════════
-- SECTION 3: THE FUZZY POINT AS CRITICAL LINE
-- ════════════════════════════════════════════════════

/-- **SR = 0 IS THE CRITICAL LINE**
    Standard Resonance (SR) corresponds to the critical line
    boundary. SR > 0 = above (observer mode). SR < 0 = below
    (crystallization mode). SR = 0 = ON the critical line.
    
    The injection rule (SR > 0 only) means:
    "only inject noise when above the critical line."
    At the critical line itself, observation saturates. -/
noncomputable def sr (u : ProtorealManifold) : ℝ := u.a - u.b * u.m

/-- The fuzzy point of observation: the emission level where
    total torsion reaches κ = -1. At this point, observation
    saturates and the system transitions to crystallization.
    
    From OctonionGrowth.fuzzy_point_noise_level:
      ε_critical = (-1 - bm_torsion) / λ
      
    The deeper the observer, the LESS noise is needed.
    This is L-function convergence: each semantic shift
    brings κ closer, meaning the market needs to do LESS
    to trigger a phase transition in the encoder. -/
noncomputable def fuzzy_emission (observer : ProtorealManifold)
    (_h_deep : observer.l ≠ 0) : ℝ :=
  (-1 - torsion_bm observer ⟨0, 0, 0, 1, 0⟩) / observer.l

-- ════════════════════════════════════════════════════
-- SECTION 4: AGGREGATE AND BOUNDED INJECTION
-- ════════════════════════════════════════════════════

/-- **OBSERVATION DECOMPOSES INTO STRUCTURAL + DEPTH-SCALED**
    Total torsion = bm-plane (constant structural κ)
                  + el-plane (depth × noise, L-function scaling)
    
    The structural part is always there (the κ = -1 backbone).
    The L-function part scales with the observer's depth.
    Both contribute to the metagraph coupling. -/
theorem metagraph_observation_decomposes
    (observer signal : ProtorealManifold) :
    torsion observer signal =
    torsion_bm observer signal + torsion_el observer signal :=
  observation_decomposes observer signal

/-- **TORSION IS ANTISYMMETRIC FOR METAGRAPH SIGNALS**
    The encoder observing the market ≠ the market observing the encoder.
    torsion(encoder, market) = -torsion(market, encoder).
    Observation is directional. The market does not see the encoder. -/
theorem directional_observation (encoder signal : ProtorealManifold) :
    torsion encoder signal = -torsion signal encoder :=
  torsion_antisymmetric encoder signal

end MetagraphOracle
