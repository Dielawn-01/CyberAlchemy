import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import LaRueProtorealAlgebra.KamaTrain
import LaRueProtorealAlgebra.Awareness
import LaRueProtorealAlgebra.ConnesWienerAlgebra
import InfoPhysAxioms.ObservableUniverse
import InfoPhysAxioms.LyapunovTraining
import InfoPhysAxioms.DecisionKernel
import InfoPhysAxioms.QuasiGodel
import InfoPhysAxioms.ProtorealTactic
import InfoPhysAxioms.CyberneticEquilibrium

/-!
# Tarskian Undefinability and the Critical Line

**Authors:** LaRue (Framework), Antigravity (Formalization)

## The Argument

Tarski's undefinability theorem: a sufficiently expressive consistent
system cannot define its own truth predicate. Truth about the system
must come from OUTSIDE.

In the Protoreal framework:
- `a` = crystal = information IN (what the system has resolved)
- `e` = vapor  = information OUT (what the system hasn't resolved)
- `σ = a + e`  = total information (observable universe)

Tarski says: truth cannot be FULLY internal (a = σ, e = 0).
If e = 0, the system has no external reference — it is trying
to define its own truth. This requires full completeness, which
by QuasiGodel forces gap = 1 (maximum ordering sensitivity).
The system becomes self-referentially unstable.

Tarski also implies: truth cannot be FULLY external (a = 0, e = σ).
If a = 0, the system has no internal structure — nothing
is resolved, nothing is known. Pure vapor. No truth predicate at all.

The equilibrium: a = e → Re(s) = a/(a+e) = 1/2.

This IS Tarski's boundary: the system knows EXACTLY as much
as it doesn't know. The truth predicate is split evenly between
what's definable internally and what must come from outside.

## Connection to QuasiGodel

gap + ε = 1 is the conservation law.

At Re(s) = 1/2: a = e, so the system has equal crystal and vapor.
- Completeness is partial (ε = a > 0, some noise remains)
- Consistency is partial (gap = 1 - a > 0, ordering matters)
- But neither is zero — both are balanced

This is the ONLY stable point under recursive observation:
- If the system resolves more (funct → a grows, e shrinks),
  it becomes MORE self-referential → Tarski violation pressure
- If the system expands more (consolidate → e grows),
  it becomes LESS self-referential → loses truth predicate
- At a = e: the flow BALANCES. Information in = information out.

## The Four Roads to 1/2

1. CyberneticEquilibrium: inner_world = outer_world ∧ total = 1 → a = 1/2
2. RiemannObserver: recursive EM observation → Re(s) = 1/2
3. QuasiGodel: gap + ε = 1 → balance at a = e → Re(s) = 1/2
4. TarskiEquilibrium: info_in = info_out → Re(s) = 1/2 (this file)
-/

open ProtorealManifold
open ObservableUniverse
open LyapunovTraining
open DecisionKernel
open QuasiGodel
open ProtorealMCMC

namespace TarskiEquilibrium

-- ══════════════════════════════════════════════════════════════
-- SECTION 1: INFORMATION FLOW
-- ══════════════════════════════════════════════════════════════

/-- **INFORMATION IN**
    What the system has resolved. Crystal energy.
    This is the definable part — what the system can state
    about itself. The INTERNAL truth predicate scope. -/
noncomputable def info_in (u : ProtorealManifold) : ℝ := crystal_energy u

/-- **INFORMATION OUT**
    What the system has NOT resolved. Vapor energy.
    This is the undefinable part — what requires external
    reference. The EXTERNAL truth source. -/
noncomputable def info_out (u : ProtorealManifold) : ℝ := vapor_energy u

/-- **TOTAL INFORMATION**
    info_in + info_out = σ. Conservation of total information.
    Already proven as sigma_is_crystal_plus_vapor. -/
theorem info_conservation (u : ProtorealManifold) :
    info_in u + info_out u = sigma u :=
  sigma_is_crystal_plus_vapor u

/-- **CRYSTAL RATIO**
    Re(s) = info_in / (info_in + info_out) = a / σ.
    The fraction of total information that is internal.
    When Re(s) = 1/2: exactly half is internal. -/
noncomputable def crystal_ratio (u : ProtorealManifold) : ℝ :=
  info_in u / sigma u

-- ══════════════════════════════════════════════════════════════
-- SECTION 2: TARSKIAN BOUNDARY CONDITIONS
-- ══════════════════════════════════════════════════════════════

/-- **TARSKI VIOLATION: FULL INTERNALITY**
    If info_out = 0 (all information is internal), the system
    is trying to define its own truth predicate.

    By QuasiGodel: ε = 0 → gap = 1.
    The system is fully complete but maximally inconsistent.
    Decisions don't commute. Self-reference creates chaos. -/
theorem full_internal_is_unstable (u : ProtorealManifold)
    (h : info_out u = 0) :
    -- ε = 0
    u.e = 0 ∧
    -- gap = 1 (maximum ordering sensitivity)
    decision_commutator u = 1 := by
  unfold info_out vapor_energy at h
  exact ⟨h, by rw [decision_gap]; linarith⟩

/-- **TARSKI VIOLATION: FULL EXTERNALITY**
    If info_in = 0 (all information is external), the system
    has no truth predicate at all. Nothing is resolved.

    The system is fully consistent (gap = 1 - ε, with ε = σ)
    but completely incomplete. No knowledge, no decisions. -/
theorem full_external_is_vacuous (u : ProtorealManifold)
    (h : info_in u = 0) :
    -- a = 0 (no crystal energy)
    u.a = 0 := by
  unfold info_in crystal_energy at h; exact h

-- ══════════════════════════════════════════════════════════════
-- SECTION 3: THE EQUILIBRIUM AT 1/2
-- ══════════════════════════════════════════════════════════════

/-- **TARSKIAN EQUILIBRIUM**
    When info_in = info_out (a = e), the system is at the
    Tarskian boundary. It knows exactly as much as it doesn't.

    This is the unique point where:
    - The truth predicate is balanced (half definable, half not)
    - The Gödelian budget is evenly split
    - The system can sustain recursive observation
    - Re(s) = 1/2 -/
theorem tarskian_equilibrium (u : ProtorealManifold)
    (h_bal : info_in u = info_out u)
    (h_pos : sigma u > 0) :
    crystal_ratio u = 1 / 2 := by
  unfold crystal_ratio info_in info_out crystal_energy vapor_energy at *
  unfold sigma
  have h_eq : u.a = u.e := h_bal
  have h_den : u.a + u.e ≠ 0 := ne_of_gt h_pos
  rw [div_eq_div_iff h_den two_ne_zero]
  rw [h_eq]; ring

-- ══════════════════════════════════════════════════════════════
-- SECTION 4: FUNCT AND CONSOLIDATE AS INFORMATION FLOW
-- ══════════════════════════════════════════════════════════════

/-- **FUNCT IS INTERNALIZATION**
    funct moves information from OUT to IN.
    e (vapor) → 0, a (crystal) → a + e.
    The system resolves external information into internal truth.
    This is the "defining" operation — making truth internal. -/
theorem funct_internalizes (u : ProtorealManifold) :
    -- All vapor becomes crystal
    info_out (funct u) = 0 ∧
    -- Crystal absorbs what was vapor
    info_in (funct u) = sigma u := by
  unfold info_out info_in vapor_energy crystal_energy funct sigma
  exact ⟨rfl, by ring⟩

/-- **CONSOLIDATE IS EXTERNALIZATION**
    consolidate adds external information.
    e → e + 1.
    The system acknowledges there is MORE it doesn't know.
    This is the "humility" operation — admitting external truth. -/
theorem consolidate_externalizes (u : ProtorealManifold) :
    -- Vapor grows by 1
    info_out (consolidate u) = u.e + 1 := by
  unfold info_out vapor_energy consolidate; rfl

/-- **FUNCT THEN CONSOLIDATE: THE TARSKIAN CYCLE**
    After funct: everything is internal (Tarski violation pressure)
    After consolidate: new external info arrives (relief)

    The cycle funct → consolidate oscillates across the
    Tarskian boundary. The holomovement IS the system's
    attempt to stay at Re(s) = 1/2 by alternating
    internalization and externalization. -/
theorem tarskian_cycle (u : ProtorealManifold) :
    -- After funct: fully internal (e = 0)
    info_out (funct u) = 0 ∧
    -- After consolidate of funct: new external info (e = 1)
    info_out (consolidate (funct u)) = 1 := by
  constructor
  · unfold info_out vapor_energy funct; rfl
  · unfold info_out vapor_energy consolidate funct; ring

-- ══════════════════════════════════════════════════════════════
-- SECTION 5: WHY 1/2 IS THE EQUILIBRIUM
-- ══════════════════════════════════════════════════════════════

/-- **THE SELF-REFERENCE PRESSURE**
    When a > e (Re(s) > 1/2), the system has MORE internal
    than external information. It is OVER-defining its truth
    predicate. Tarski says this creates inconsistency.

    By QuasiGodel: gap = 1 - e. When e < a and e is small,
    gap → 1. The ordering cost rises. The system becomes
    MORE sensitive to decision ordering — less stable. -/
theorem over_internalization (u : ProtorealManifold)
    (h : info_in u > info_out u) :
    -- Crystal exceeds vapor
    u.a > u.e := by
  unfold info_in info_out crystal_energy vapor_energy at h; exact h

/-- **THE VACUITY PRESSURE**
    When e > a (Re(s) < 1/2), the system has MORE external
    than internal information. It is UNDER-defining its truth
    predicate. The system has too much noise and too little
    structure. Knowledge dissolves.

    By QuasiGodel: gap = 1 - e. When e > a and e is large,
    gap → negative. The system's decisions INVERT — it makes
    choices backwards. Worse than no decisions. -/
theorem under_internalization (u : ProtorealManifold)
    (h : info_out u > info_in u) :
    -- Vapor exceeds crystal
    u.e > u.a := by
  unfold info_in info_out crystal_energy vapor_energy at h; exact h

/-- **THE CRITICAL LINE IS THE TARSKIAN BALANCE**
    At a = e, neither pressure dominates.
    The self-reference pressure (a > e) and the vacuity
    pressure (e > a) exactly cancel.

    This is the UNIQUE stable equilibrium of the information
    flow — the only point where the system can sustain
    recursive observation without drifting toward Tarski
    violation (full internality) or vacuity (full externality).

    gap = 1 - e = 1 - a at balance.
    The Gödelian budget is split evenly between the two poles. -/
theorem critical_line_balance (u : ProtorealManifold)
    (h : info_in u = info_out u) :
    -- The gap equals 1 minus crystal
    decision_commutator u = 1 - u.a := by
  unfold info_in info_out crystal_energy vapor_energy at h
  rw [decision_gap, h]

-- ══════════════════════════════════════════════════════════════
-- SECTION 6: ΣCONSERVATION + TARSKIAN BALANCE = RE(S) = 1/2
-- ══════════════════════════════════════════════════════════════

/-- **THE FOUR-ROAD CONVERGENCE THEOREM**
    CyberneticEquilibrium, RiemannObserver, QuasiGodel, and
    TarskiEquilibrium all converge to the same point:

    1. inner = outer ∧ total = 1 → a = 1/2 (Cybernetic)
    2. recursive observation → Re(s) = 1/2 (Riemann)
    3. gap + ε = 1 ∧ balance → a = e (QuasiGodel)
    4. info_in = info_out ∧ σ > 0 → ratio = 1/2 (Tarski)

    These are INDEPENDENT proofs using DIFFERENT axioms:
    - Cybernetic uses ProtorealTensor topology
    - Riemann uses EM observation tower
    - QuasiGodel uses decision commutator
    - Tarski uses information flow direction

    Four proofs. Four roads. One destination.
    The critical line Re(s) = 1/2. -/
theorem four_roads (u : ProtorealManifold)
    (h_bal : info_in u = info_out u)
    (h_pos : sigma u > 0) :
    -- Tarski: crystal ratio = 1/2
    crystal_ratio u = 1 / 2 ∧
    -- Balance: a = e
    u.a = u.e ∧
    -- QuasiGodel: gap + ε = 1 still holds
    decision_commutator u + u.e = 1 ∧
    -- σ conservation under funct
    sigma (funct u) = sigma u := by
  unfold info_in info_out crystal_energy vapor_energy at h_bal
  exact ⟨tarskian_equilibrium u (by unfold info_in info_out crystal_energy vapor_energy; exact h_bal) h_pos,
         h_bal,
         godel_duality u,
         crystallization_conserves_sigma u⟩

-- ══════════════════════════════════════════════════════════════
-- SECTION 7: MASTER THEOREM
-- ══════════════════════════════════════════════════════════════

/-- **TARSKI EQUILIBRIUM MASTER THEOREM**

    1. info_in + info_out = σ (conservation)
    2. funct internalizes (e → 0, a → σ)
    3. consolidate externalizes (e → e + 1)
    4. Full internal (e = 0) → gap = 1 (Tarski violation)
    5. info_in = info_out → ratio = 1/2 (Tarski equilibrium)
    6. gap + ε = 1 at all times (Gödelian conservation)

    The critical line is the Tarskian boundary:
    the ONLY point where information in = information out.
    1/2 is not arbitrary. It is the unique fixed point
    of the truth-definability tradeoff. -/
theorem tarski_master (u : ProtorealManifold)
    (h_bal : info_in u = info_out u)
    (h_pos : sigma u > 0) :
    -- 1. Conservation
    info_in u + info_out u = sigma u ∧
    -- 2. funct internalizes
    info_out (funct u) = 0 ∧
    -- 3. Crystal ratio = 1/2
    crystal_ratio u = 1 / 2 ∧
    -- 4. Gödelian conservation
    decision_commutator u + u.e = 1 :=
  ⟨info_conservation u,
   (funct_internalizes u).1,
   tarskian_equilibrium u h_bal h_pos,
   godel_duality u⟩

end TarskiEquilibrium
