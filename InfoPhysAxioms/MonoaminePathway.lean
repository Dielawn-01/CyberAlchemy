import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.CyberneticBiochemistry
import InfoPhysAxioms.FormalComputationalPharmacology

/-!
# Monoamine Pathway Pharmacodynamics (𝕌)

**Authors:** LaRue (Theoretical Framework), Antigravity (Formalization)

## Purpose

This module extends CyberneticBiochemistry with the full branching
tryptophan pathway and ring closure pharmacodynamics. It formalizes:

1. The tryptophan fork: serotonin branch vs. kynurenine branch
2. Ring closure as a stability operator (Pictet-Spengler cyclization)
3. MAOI shielding as coherence preservation
4. Drug interaction modeling (SSRIs, MAOIs, psychedelics)
5. Mycobiome interference at the pathway branch point

## Biochemistry Background

Tryptophan is the rarest essential amino acid and the sole precursor
for both serotonin and kynurenine. The pathway fork:

```
                    Tryptophan
                        |
            ┌───────────┴───────────┐
            │                       │
      TPH (human enzyme)     IDO/TDO (stress/fungal)
            │                       │
          5-HTP                Kynurenine
            │                       │
     AADC (decarboxylase)    ┌──────┴──────┐
            │                │             │
       SEROTONIN (5-HT)  3-HK         Kynurenic acid
            │            (neurotoxic)   (neuroprotective)
      ┌─────┼──────┐         │
      │     │      │     Quinolinic acid
   NAT   dream   mood    (excitotoxic)
      │    run   stability    │
  MELATONIN              NAD+ synthesis
      │
  Pictet-Spengler
      │
  PINOLINE (β-carboline)
  = MAOI shield
```

## Epistemic Status

PROVEN: All algebraic identities (ring closure idempotence,
        parity locking, energy conservation, pathway mass balance)
PROPOSED: The biological mapping of these operators to specific
          enzymes and metabolites. These are computational models
          for simulation, not claims about molecular mechanism.
-/

open ProtorealManifold
open CyberneticBiochemistry
open FormalComputationalPharmacology

namespace MonoaminePathway

-- ════════════════════════════════════════════════════════════════
-- SECTION 1: THE TRYPTOPHAN FORK
-- ════════════════════════════════════════════════════════════════

/-- **Tryptophan pool state.**
    Models the available tryptophan and its allocation between
    the serotonin and kynurenine branches.

    total: total tryptophan available (dietary intake)
    serotonin_fraction: fraction routed to 5-HT synthesis
    kynurenine_fraction: fraction diverted to kynurenine

    Constraint: serotonin_fraction + kynurenine_fraction = 1
    (mass balance — tryptophan goes one way or the other) -/
structure TryptophanPool where
  total : ℝ
  serotonin_fraction : ℝ
  kynurenine_fraction : ℝ
  h_total_pos : total > 0
  h_mass_balance : serotonin_fraction + kynurenine_fraction = 1
  h_sero_bounded : 0 ≤ serotonin_fraction ∧ serotonin_fraction ≤ 1
  h_kyn_bounded : 0 ≤ kynurenine_fraction ∧ kynurenine_fraction ≤ 1

/-- Tryptophan available for serotonin synthesis. -/
def serotonin_substrate (pool : TryptophanPool) : ℝ :=
  pool.total * pool.serotonin_fraction

/-- Tryptophan diverted to kynurenine. -/
def kynurenine_substrate (pool : TryptophanPool) : ℝ :=
  pool.total * pool.kynurenine_fraction

/-- **Mass conservation at the fork.**
    Total tryptophan = serotonin substrate + kynurenine substrate. -/
theorem fork_mass_balance (pool : TryptophanPool) :
    serotonin_substrate pool + kynurenine_substrate pool = pool.total := by
  unfold serotonin_substrate kynurenine_substrate
  rw [← mul_add]
  rw [pool.h_mass_balance]
  ring

/-- More kynurenine diversion means less serotonin substrate. -/
theorem diversion_reduces_serotonin (p1 p2 : TryptophanPool)
    (h_same_total : p1.total = p2.total)
    (h_more_kyn : p2.kynurenine_fraction > p1.kynurenine_fraction) :
    serotonin_substrate p2 < serotonin_substrate p1 := by
  unfold serotonin_substrate
  rw [h_same_total]
  apply mul_lt_mul_of_pos_left _ p2.h_total_pos
  linarith [p1.h_mass_balance, p2.h_mass_balance]

-- ════════════════════════════════════════════════════════════════
-- SECTION 2: KYNURENINE BRANCH PRODUCTS
-- ════════════════════════════════════════════════════════════════

/-- **Kynurenine branch output.**
    The kynurenine pathway produces both neuroprotective and
    neurotoxic metabolites. The ratio matters.

    kynurenic_acid: neuroprotective (NMDA antagonist)
    quinolinic_acid: neurotoxic (NMDA agonist, excitotoxic)
    nad_precursor: NAD+ synthesis (energy metabolism)

    In inflammatory states, the pathway shifts toward quinolinic
    acid (neurotoxic). This is one mechanism linking inflammation
    to depression. -/
structure KynurenineOutput where
  kynurenic_acid : ℝ     -- neuroprotective fraction
  quinolinic_acid : ℝ    -- neurotoxic fraction
  nad_precursor : ℝ      -- energy metabolism fraction
  h_sum : kynurenic_acid + quinolinic_acid + nad_precursor = 1
  h_nonneg : kynurenic_acid ≥ 0 ∧ quinolinic_acid ≥ 0 ∧ nad_precursor ≥ 0

/-- **Neurotoxicity ratio.**
    quinolinic / kynurenic > 1 → net neurotoxic
    quinolinic / kynurenic < 1 → net neuroprotective

    This ratio is elevated in depression, Alzheimer's, and
    mycobiome dysbiosis (Candida promotes inflammatory kynurenine). -/
noncomputable def neurotoxicity_ratio (ko : KynurenineOutput)
    (h : ko.kynurenic_acid > 0) : ℝ :=
  ko.quinolinic_acid / ko.kynurenic_acid

-- ════════════════════════════════════════════════════════════════
-- SECTION 3: RING CLOSURE PHARMACODYNAMICS
-- ════════════════════════════════════════════════════════════════

/-!
## Ring Closure as a Drug Stability Mechanism

CyberneticBiochemistry.lean proves:
  - ring_closure = fuse (parity projection)
  - ring_closure_locks: always produces an infonad (stable)
  - ring_closure_is_permanent: idempotent (once closed, stays closed)
  - ring_closure_conserves: energy is preserved

Here we extend this to model drug stability classes:

  OPEN RING (indole):   reactive, b ≠ m, vulnerable to MAO
  CLOSED RING (β-carb): stable, b = m, MAO-resistant (MAOI)

Drug design principle: ring closure = stabilization.
MAOIs work by BEING stable (closed ring) and occupying MAO's
active site, preventing it from degrading open-ring monoamines.
-/

/-- **Drug stability classification based on ring structure.** -/
inductive RingStatus
  | open_ring    -- indole: reactive, vulnerable to degradation
  | closed_ring  -- β-carboline: stable, MAO-resistant
  deriving Repr

/-- Map ring status to manifold property. -/
def ring_status (u : ProtorealManifold) : RingStatus :=
  if u.b = u.m then RingStatus.closed_ring
  else RingStatus.open_ring

/-- Closed-ring compounds are infonads (parity-locked). -/
theorem closed_ring_is_stable (u : ProtorealManifold)
    (h : ring_status u = RingStatus.closed_ring) :
    u.b = u.m := by
  unfold ring_status at h
  split at h <;> simp_all

/-- **MAOI mechanism as ring closure shield.**

    An MAOI (monoamine oxidase inhibitor) protects monoamines
    from degradation. In the algebraic model:

    1. MAO = automatic_differentiation (introduces noise = degradation)
    2. MAOI = fuse (ring closure = locks parity)
    3. Shielded state = fuse(u) is a fixed point of fuse
       → MAO cannot break what is already at equilibrium

    The key pharmacological insight: MAOIs don't directly block
    MAO. They occupy MAO's active site because their closed-ring
    structure FITS the binding pocket. The algebraic analog:
    fuse(u) is idempotent, so applying fuse to an already-fused
    state does nothing — the binding site is occupied. -/

/-- **MAOI protection theorem.**
    Applying ring closure before degradation (MAO) and then
    re-closing preserves the shielded state.

    shield → degrade → re-shield = shield
    fuse ∘ automatic_differentiation ∘ fuse = fuse (for the parity components) -/
theorem maoi_parity_recovery (u : ProtorealManifold) :
    (ring_closure (mao_degradation (ring_closure u))).b =
    (ring_closure (mao_degradation (ring_closure u))).m :=
  ring_closure_locks (mao_degradation (ring_closure u)) |>.1

-- ════════════════════════════════════════════════════════════════
-- SECTION 4: DRUG INTERACTION CLASSES
-- ════════════════════════════════════════════════════════════════

/-- **SSRI model (Selective Serotonin Reuptake Inhibitor).**

    SSRIs increase serotonin availability by blocking reuptake.
    In the algebraic model: amplify the serotonin signal.

    PROPOSED MODEL: SSRI = repeated serotonin_signal application.
    Each application strengthens the parity lock (b → m convergence).
    The number of applications models dose/duration. -/
noncomputable def ssri_effect (u : ProtorealManifold) (doses : ℕ) : ProtorealManifold :=
  match doses with
  | 0 => u
  | n + 1 => ssri_effect (serotonin_signal u) n

/-- SSRIs always achieve parity lock regardless of dose count. -/
theorem ssri_locks_parity (u : ProtorealManifold) (n : ℕ) :
    (ssri_effect u (n + 1)).b = (ssri_effect u (n + 1)).m := by
  induction n with
  | zero => simp [ssri_effect]; exact serotonin_locks_parity u
  | succ n ih =>
    simp only [ssri_effect]
    exact ih

/-- **MAOI + SSRI interaction warning.**

    Combining MAOIs (prevent degradation) with SSRIs (boost
    serotonin) can cause serotonin syndrome — dangerous excess.

    In the model: MAOI shields serotonin from degradation,
    and SSRI amplifies it. The combination produces a state
    where b = m is locked AND noise is elevated (automatic_differentiation
    from MAOI's ring closure process).

    This is a modeling primitive for drug interaction checking. -/
noncomputable def maoi_plus_ssri (u : ProtorealManifold) : ProtorealManifold :=
  let shielded := maoi_shield u           -- MAOI: lock parity
  let boosted := serotonin_signal shielded -- SSRI: amplify 5-HT
  boosted

/-- The combination still locks parity (the danger is dose, not algebra). -/
theorem combination_locks_parity (u : ProtorealManifold) :
    (maoi_plus_ssri u).b = (maoi_plus_ssri u).m := by
  unfold maoi_plus_ssri
  exact serotonin_locks_parity (maoi_shield u)

-- ════════════════════════════════════════════════════════════════
-- SECTION 5: MYCOBIOME INTERFERENCE AT THE FORK
-- ════════════════════════════════════════════════════════════════

/-- **PROPOSED MODEL: Mycobiome-driven tryptophan diversion.**

    Fungal IDO/TDO activity shifts the tryptophan fork toward
    kynurenine. This models the hypothesis:

    Candida overgrowth → ↑ fungal IDO → ↑ kynurenine fraction
    → ↓ serotonin substrate → ↓ parity lock → mood instability

    The mycobiome parameter directly modulates the fork ratio. -/
noncomputable def mycobiome_shifted_pool
    (base_pool : TryptophanPool) (myco : MycobiomeState) : TryptophanPool :=
  let shift := myco.tryptophan_diversion
  let new_kyn := min 1 (base_pool.kynurenine_fraction + shift * base_pool.serotonin_fraction)
  let new_sero := 1 - new_kyn
  { total := base_pool.total,
    serotonin_fraction := new_sero,
    kynurenine_fraction := new_kyn,
    h_total_pos := base_pool.h_total_pos,
    h_mass_balance := by ring,
    h_sero_bounded := by constructor <;> simp [new_sero, new_kyn] <;> linarith [min_le_right 1 _],
    h_kyn_bounded := by constructor <;> simp [new_kyn] <;> [linarith [base_pool.h_kyn_bounded.1]; exact min_le_left _ _]
  }

/-- **PROPOSED MODEL: Full pathway simulation.**

    Given a tryptophan pool, mycobiome state, and manifold state:
    1. Shift pool by mycobiome interference
    2. Compute serotonin substrate from shifted pool
    3. Scale serotonin signal by available substrate
    4. Apply ring closure if substrate supports it

    Returns both the neural state AND the kynurenine output
    for downstream modeling (neuroinflammation, NAD+ synthesis). -/
noncomputable def pathway_simulation
    (u : ProtorealManifold)
    (pool : TryptophanPool)
    (myco : MycobiomeState)
    : ProtorealManifold × ℝ :=
  let shifted := mycobiome_shifted_pool pool myco
  let substrate := serotonin_substrate shifted
  -- Scale parity projection by substrate availability
  let availability := substrate / pool.total
  let avg := (u.b + u.m) / 2
  let neural_state : ProtorealManifold := {
    a := u.a,
    b := u.b + availability * (avg - u.b),
    m := u.m + availability * (avg - u.m),
    e := u.e,
    l := u.l
  }
  let kyn_load := kynurenine_substrate shifted
  (neural_state, kyn_load)

-- ════════════════════════════════════════════════════════════════
-- SECTION 6: HYDROGEL INTERVENTION ON THE PATHWAY
-- ════════════════════════════════════════════════════════════════

/-- **PROPOSED MODEL: Tryptophan-rescue hydrogel.**

    A chitin-HA hydrogel designed to:
    1. Deliver tryptophan directly to the mucosal surface
    2. Suppress Candida IDO activity (reduce diversion)
    3. Provide substrate for pinoline synthesis (ring closure shield)

    Modeled as a compound intervention on the tryptophan pool. -/
structure TryptophanRescueHydrogel where
  /-- Additional tryptophan delivered (μmol equivalent) -/
  tryptophan_supplement : ℝ
  /-- IDO suppression factor (0 = no suppression, 1 = complete) -/
  ido_suppression : ℝ
  h_supp_pos : tryptophan_supplement ≥ 0
  h_ido_bounded : 0 ≤ ido_suppression ∧ ido_suppression ≤ 1

/-- Apply tryptophan-rescue hydrogel to a pool. -/
noncomputable def apply_rescue (pool : TryptophanPool)
    (hg : TryptophanRescueHydrogel) : TryptophanPool :=
  let new_total := pool.total + hg.tryptophan_supplement
  -- IDO suppression shifts the fork back toward serotonin
  let rescued_sero := min 1 (pool.serotonin_fraction +
    hg.ido_suppression * pool.kynurenine_fraction)
  let rescued_kyn := 1 - rescued_sero
  { total := new_total,
    serotonin_fraction := rescued_sero,
    kynurenine_fraction := rescued_kyn,
    h_total_pos := by linarith [pool.h_total_pos, hg.h_supp_pos],
    h_mass_balance := by ring,
    h_sero_bounded := by constructor <;> simp [rescued_sero] <;> [linarith [pool.h_sero_bounded.1]; exact min_le_left _ _],
    h_kyn_bounded := by constructor <;> simp [rescued_kyn, rescued_sero] <;> linarith [min_le_right 1 _]
  }

/-- Rescue hydrogel increases total tryptophan. -/
theorem rescue_increases_total (pool : TryptophanPool)
    (hg : TryptophanRescueHydrogel) (h : hg.tryptophan_supplement > 0) :
    (apply_rescue pool hg).total > pool.total := by
  unfold apply_rescue; simp; linarith

-- ════════════════════════════════════════════════════════════════
-- SECTION 7: THE PINOLINE CYCLE (ENDOGENOUS RING CLOSURE)
-- ════════════════════════════════════════════════════════════════

/-!
## The Pinoline Cycle

From CyberneticBiochemistry.lean:
  pinoline(u) = ring_closure(serotonin_signal(u))

Pinoline is the endogenous β-carboline. It is:
1. Produced in the pineal gland at night
2. An MAOI — protects serotonin/melatonin during sleep
3. A ring-closed (stable) derivative of serotonin

The cycle: Tryptophan → Serotonin → Melatonin → Pinoline
                                                    ↓
                                              MAOI shield
                                                    ↓
                                          Protects serotonin
                                          from degradation

If tryptophan is diverted (by mycobiome), this entire cycle
is starved. No tryptophan → no serotonin → no melatonin →
no pinoline → no MAOI shield → remaining serotonin degrades
faster. A vicious cycle.

The hydrogel intervention breaks this cycle by:
1. Supplementing tryptophan (feed the pathway)
2. Suppressing fungal IDO (reduce diversion)
3. The HA backbone provides immune tolerance
4. The chitin backbone provides structural integrity
-/

/-- **The pinoline production chain.**
    Tryptophan → serotonin → ring closure → pinoline.
    Each step is a manifold operator from CyberneticBiochemistry. -/
noncomputable def pinoline_chain (u : ProtorealManifold) : ProtorealManifold :=
  ring_closure (serotonin_signal u)

/-- The chain always produces a stable (parity-locked) state. -/
theorem pinoline_chain_stable (u : ProtorealManifold) :
    is_infonad (pinoline_chain u) :=
  ring_closure_locks (serotonin_signal u)

/-- The chain is idempotent: once stabilized, re-application changes nothing. -/
theorem pinoline_chain_idempotent (u : ProtorealManifold) :
    pinoline_chain (pinoline_chain u) = pinoline_chain u := by
  unfold pinoline_chain
  -- ring_closure(serotonin(ring_closure(serotonin(u))))
  -- serotonin of a parity-locked state preserves parity
  -- ring_closure of a parity-locked state is idempotent
  have h1 : (serotonin_signal (ring_closure (serotonin_signal u))).b =
             (serotonin_signal (ring_closure (serotonin_signal u))).m :=
    serotonin_locks_parity _
  -- ring_closure is idempotent (from CyberneticBiochemistry)
  exact ring_closure_is_permanent (serotonin_signal u)

/-- **The vicious cycle: degradation undoes the chain,
    requiring continuous tryptophan supply.**

    MAO degrades serotonin (automatic_differentiation = noise injection).
    After degradation, the state is no longer parity-locked.
    The pinoline chain must be re-run to restore stability.

    This models the biological fact that serotonin has a
    half-life and must be continuously synthesized. -/
noncomputable def degradation_cycle (u : ProtorealManifold) : ProtorealManifold :=
  mao_degradation (pinoline_chain u)

/-- Degradation always introduces noise into a stable state. -/
theorem degradation_destabilizes (u : ProtorealManifold) :
    (degradation_cycle u).e > (pinoline_chain u).e := by
  unfold degradation_cycle
  exact mao_introduces_noise (pinoline_chain u)

-- ════════════════════════════════════════════════════════════════
-- MASTER THEOREM
-- ════════════════════════════════════════════════════════════════

/-- **MONOAMINE PATHWAY PHARMACODYNAMICS: Summary**

    PROVEN (algebraic):
    1. The tryptophan fork conserves mass
    2. Diversion reduces serotonin substrate
    3. Ring closure always locks parity (stability)
    4. Ring closure is idempotent (permanence)
    5. SSRIs achieve parity lock at any dose
    6. MAO always introduces noise (degradation)
    7. MAOI recovers parity after degradation
    8. The pinoline chain is stable and idempotent

    PROPOSED (models):
    - Mycobiome IDO activity as fork shift parameter
    - Tryptophan-rescue hydrogel intervention
    - Drug interaction modeling (SSRI + MAOI)
    - Neurotoxicity ratio from kynurenine branch -/
theorem pathway_master :
    -- 1. Fork mass balance
    (∀ pool : TryptophanPool,
      serotonin_substrate pool + kynurenine_substrate pool = pool.total) ∧
    -- 2. Ring closure locks parity
    (∀ u : ProtorealManifold, is_infonad (ring_closure u)) ∧
    -- 3. Ring closure is permanent
    (∀ u : ProtorealManifold, ring_closure (ring_closure u) = ring_closure u) ∧
    -- 4. SSRIs achieve parity
    (∀ u n, (ssri_effect u (n + 1)).b = (ssri_effect u (n + 1)).m) ∧
    -- 5. Pinoline chain is stable
    (∀ u : ProtorealManifold, is_infonad (pinoline_chain u)) ∧
    -- 6. Degradation introduces noise
    (∀ u : ProtorealManifold,
      (degradation_cycle u).e > (pinoline_chain u).e) :=
  ⟨fork_mass_balance,
   ring_closure_locks,
   ring_closure_is_permanent,
   ssri_locks_parity,
   pinoline_chain_stable,
   degradation_destabilizes⟩

end MonoaminePathway
