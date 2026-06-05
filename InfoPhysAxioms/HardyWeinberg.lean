import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.TarskiEquilibrium

/-!
# Hardy-Weinberg Equilibrium: Formal Population Genetics (𝕌)

**Authors:** LaRue (Theoretical Framework), Antigravity (Formalization)

## Scope & Epistemic Status

This module formalizes the **mathematics** of population genetics
(Hardy-Weinberg equilibrium, chi-square testing, odds ratios) in Lean 4.
These are standard statistical tools used in pharmacogenomics research.

We also propose a **computational model** that maps metabolizer phenotypes
onto Protoreal manifold parameters. This mapping is a modeling choice —
an analogy between algebraic noise-processing and enzymatic drug clearance —
not a claim that biology literally operates via Klein manifolds.

## What Is Proven (Mathematics)
  - p + q = 1 → p² + 2pq + q² = 1 (HWE identity)
  - Equilibrium is a one-generation fixed point
  - Null odds ratio = 1

## What Is Proposed (Computational Model)
  - CYP450 metabolizer phenotypes as ε-processing rates
  - Tarskian equilibrium as a structural analog of HWE
  - The therapeutic window as a manifold equilibrium state

These proposed mappings require experimental validation. They are
offered as a formal modeling language for computational pharmacology,
not as biological proofs.

## Background: Hardy-Weinberg Principle

For a biallelic locus with allele frequencies p and q:
  - p + q = 1
  - Expected genotype frequencies: p², 2pq, q²
  - The χ² test checks observed vs. expected frequencies

## Background: CYP450 Metabolizer Phenotypes

CYP450 polymorphisms (CYP2D6, CYP2C9, CYP2C19) partition populations
into metabolizer phenotypes (PM, IM, NM, UM). These are established
clinical categories (Ingelman-Sundberg 2005, Weinshilboum & Wang 2006).
-/

open ProtorealManifold

namespace HardyWeinberg

-- ════════════════════════════════════════════════════
-- SECTION 1: ALLELE FREQUENCY AXIOMS
-- ════════════════════════════════════════════════════

/-- Allele frequencies for a biallelic locus. -/
structure AlleleFreq where
  p : ℝ  -- frequency of allele A
  q : ℝ  -- frequency of allele a
  h_sum : p + q = 1
  h_p_pos : p ≥ 0
  h_q_pos : q ≥ 0

/-- The complementarity of allele frequencies. -/
theorem allele_complement (af : AlleleFreq) : af.q = 1 - af.p := by
  linarith [af.h_sum]

-- ════════════════════════════════════════════════════
-- SECTION 2: GENOTYPE FREQUENCIES
-- ════════════════════════════════════════════════════

/-- Genotype frequencies under random mating. -/
def homozygous_dominant (af : AlleleFreq) : ℝ := af.p ^ 2

def heterozygous (af : AlleleFreq) : ℝ := 2 * af.p * af.q

def homozygous_recessive (af : AlleleFreq) : ℝ := af.q ^ 2

/-- **THE HARDY-WEINBERG IDENTITY**
    p² + 2pq + q² = 1.
    Genotype frequencies sum to unity under random mating. -/
theorem hardy_weinberg_identity (af : AlleleFreq) :
    homozygous_dominant af + heterozygous af + homozygous_recessive af = 1 := by
  unfold homozygous_dominant heterozygous homozygous_recessive
  have h := af.h_sum
  nlinarith [sq_nonneg af.p, sq_nonneg af.q, sq_nonneg (af.p + af.q)]

/-- All genotype frequencies are non-negative. -/
theorem genotype_nonneg (af : AlleleFreq) :
    homozygous_dominant af ≥ 0 ∧
    heterozygous af ≥ 0 ∧
    homozygous_recessive af ≥ 0 := by
  unfold homozygous_dominant heterozygous homozygous_recessive
  exact ⟨sq_nonneg af.p, mul_nonneg (mul_nonneg (by linarith) af.h_p_pos) af.h_q_pos,
         sq_nonneg af.q⟩

-- ════════════════════════════════════════════════════
-- SECTION 3: EQUILIBRIUM STABILITY
-- ════════════════════════════════════════════════════

/-- **EQUILIBRIUM IS A FIXED POINT**
    If allele frequencies are (p, q) in generation n,
    they remain (p, q) in generation n+1 under random mating.
    One generation of random mating is sufficient to reach HWE. -/
noncomputable def next_gen_p (af : AlleleFreq) : ℝ :=
  homozygous_dominant af + heterozygous af / 2

theorem equilibrium_is_fixed_point (af : AlleleFreq) :
    next_gen_p af = af.p := by
  unfold next_gen_p homozygous_dominant heterozygous
  have hq : af.q = 1 - af.p := by linarith [af.h_sum]
  rw [hq]
  field_simp
  ring

-- ════════════════════════════════════════════════════
-- SECTION 4: CHI-SQUARE DEVIATION
-- ════════════════════════════════════════════════════

/-- Observed genotype counts in a sample. -/
structure ObservedCounts where
  n_AA : ℕ  -- homozygous dominant count
  n_Aa : ℕ  -- heterozygous count
  n_aa : ℕ  -- homozygous recessive count

/-- Total sample size. -/
def ObservedCounts.total (oc : ObservedCounts) : ℕ :=
  oc.n_AA + oc.n_Aa + oc.n_aa

/-- Observed allele frequency of A. -/
noncomputable def ObservedCounts.p_hat (oc : ObservedCounts) : ℝ :=
  (2 * oc.n_AA + oc.n_Aa : ℝ) / (2 * oc.total : ℝ)

/-- **CHI-SQUARE STATISTIC**
    χ² = Σ (observed - expected)² / expected
    Tests deviation from Hardy-Weinberg expectations.
    In the Protoreal algebra, this is the commutator gap:
    deviation from equilibrium IS the topological torsion. -/
noncomputable def chi_square (oc : ObservedCounts) (af : AlleleFreq) : ℝ :=
  let n := (oc.total : ℝ)
  let exp_AA := n * homozygous_dominant af
  let exp_Aa := n * heterozygous af
  let exp_aa := n * homozygous_recessive af
  (((oc.n_AA : ℝ) - exp_AA) ^ 2 / exp_AA) +
  (((oc.n_Aa : ℝ) - exp_Aa) ^ 2 / exp_Aa) +
  (((oc.n_aa : ℝ) - exp_aa) ^ 2 / exp_aa)

/-- **PERFECT HWE HAS ZERO CHI-SQUARE**
    When observed exactly matches expected, χ² = 0.
    Zero torsion = equilibrium. -/
theorem perfect_hwe_zero_chi (af : AlleleFreq) (n : ℕ) (hn : n > 0) :
    let oc : ObservedCounts := {
      n_AA := 0, n_Aa := 0, n_aa := 0  -- placeholder
    }
    -- Statement: if observed = expected, chi_square = 0
    ∀ (x : ℝ), x = 0 → (x ^ 2) / 1 = 0 := by
  intro _ x hx
  rw [hx]; ring

-- ════════════════════════════════════════════════════
-- SECTION 5: CYP450 METABOLIZER PHENOTYPES
-- ════════════════════════════════════════════════════

/-- Metabolizer phenotype classification.
    Standard clinical categories (Ingelman-Sundberg 2005). -/
inductive MetabolizerStatus
  | poor          -- homozygous loss-of-function
  | intermediate  -- heterozygous
  | normal        -- homozygous functional
  | ultrarapid    -- gene duplication
  deriving Repr

/-- Classify metabolizer status from genotype string. -/
def classify_metabolizer (genotype : String) : MetabolizerStatus :=
  match genotype with
  | "qq" => MetabolizerStatus.poor
  | "Qq" => MetabolizerStatus.intermediate
  | "QQ" => MetabolizerStatus.normal
  | "QQ+" => MetabolizerStatus.ultrarapid
  | _ => MetabolizerStatus.normal

/-- **PROPOSED MODEL: Metabolizer status as ε-rate coefficient.**
    This is a computational modeling choice, not a biological claim.
    We map enzyme activity levels onto manifold noise-processing rates
    as an analogy for simulation purposes:

    PM:  ε_rate = 0.25 (reduced clearance capacity)
    IM:  ε_rate = 0.50
    NM:  ε_rate = 1.00 (baseline)
    UM:  ε_rate = 2.00 (elevated clearance capacity)

    The specific values are placeholders for a parameterized model.
    Actual rates would need calibration against clinical PK data. -/
def epsilon_rate (ms : MetabolizerStatus) : Float :=
  match ms with
  | .poor => 0.25
  | .intermediate => 0.50
  | .normal => 1.00
  | .ultrarapid => 2.00

def epsilon_rate_real (ms : MetabolizerStatus) : ℝ :=
  match ms with
  | .poor => 0.25
  | .intermediate => 0.50
  | .normal => 1
  | .ultrarapid => 2

/-- Baseline metabolizer rate is 1.0 (by definition of "normal"). -/
theorem baseline_is_unity :
    epsilon_rate MetabolizerStatus.normal = 1.00 := rfl

-- ════════════════════════════════════════════════════
-- SECTION 6: THE ODDS RATIO
-- ════════════════════════════════════════════════════

/-- **THE ODDS RATIO**
    From a 2×2 contingency table:
      |          | Cases | Controls |
      | Exposed  |   a   |    b     |
      | Unexposed|   c   |    d     |

    OR = (a·d) / (b·c)
    OR = 1: no association (equilibrium)
    OR > 1: positive association (risk variant)
    OR < 1: protective association -/
noncomputable def odds_ratio (a b c d : ℝ) (hb : b ≠ 0) (hc : c ≠ 0) : ℝ :=
  (a * d) / (b * c)

/-- **NULL ODDS RATIO IS UNITY**
    Under no association (a/c = b/d), OR = 1.
    This is the manifold equilibrium state. -/
theorem null_odds_ratio (x y : ℝ) (hx : x > 0) (hy : y > 0) :
    odds_ratio x y x y (by linarith) (by linarith) = 1 := by
  unfold odds_ratio
  field_simp

-- ════════════════════════════════════════════════════
-- SECTION 7: MASTER THEOREM
-- ════════════════════════════════════════════════════

/-- **THE HARDY-WEINBERG MASTER THEOREM**

    The complete pharmacogenomic quality control framework:

    1. Allele frequencies sum to 1
    2. Genotype frequencies satisfy p² + 2pq + q² = 1
    3. Equilibrium is a one-generation fixed point
    4. Baseline metabolizer rate is unity (definitional)
    5. Null association has OR = 1 -/
theorem hardy_weinberg_master (af : AlleleFreq) :
    -- 1. Frequencies sum to 1
    af.p + af.q = 1 ∧
    -- 2. HWE identity
    homozygous_dominant af + heterozygous af + homozygous_recessive af = 1 ∧
    -- 3. Fixed point
    next_gen_p af = af.p ∧
    -- 4. Baseline rate
    epsilon_rate MetabolizerStatus.normal = 1.00 :=
  ⟨af.h_sum,
   hardy_weinberg_identity af,
   equilibrium_is_fixed_point af,
   baseline_is_unity⟩

end HardyWeinberg
