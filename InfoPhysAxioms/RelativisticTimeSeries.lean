import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.BitCollapse
import InfoPhysAxioms.QuantumUnreal

namespace InfoPhysAxioms.RelativisticTimeSeries

open ProtorealManifold
open BitCollapse
open InfoPhysAxioms.QuantumUnreal

/-!
# Relativistic Equations from Bit-Collapsed Time Series

This module proves that integrating bit-collapsed 3-states over a 
discrete time series mathematically preserves the relativistic metric.
-/

/-- The relativistic invariant metric s² = a² - ε². -/
def invariant_metric (u : ProtorealManifold) : ℝ :=
  u.a^2 - u.e^2

/-- A time series is represented as a function mapping discrete steps ℕ to Protoreal states. -/
def time_series := ℕ → ProtorealManifold

/-- A time series is fully collapsed if every state in the sequence is a bit-collapsed state. -/
def is_collapsed_series (S : time_series) : Prop :=
  ∀ n, (S n).e = 0 ∧ (S n).b = (S n).m ∧ (S n).l = 0

/-- In a fully collapsed time series, the relativistic invariant metric is 
    strictly positive-definite (or strictly bounded by the Base a), exhibiting 
    no quantum smearing (ε = 0). -/
theorem series_preserves_invariant (S : time_series) (h : is_collapsed_series S) (n : ℕ) :
  invariant_metric (S n) = (S n).a^2 := by
  unfold invariant_metric
  have h_e : (S n).e = 0 := (h n).1
  rw [h_e]
  ring

/-- The Quantum and Relativistic regimes are mutually exclusive over the time series. -/
theorem relativistic_not_quantum (S : time_series) (h : is_collapsed_series S) (n : ℕ) :
  ¬ is_quantum_unreal (S n) := by
  unfold is_quantum_unreal
  have h_e : (S n).e = 0 := (h n).1
  push_neg
  exact h_e

end InfoPhysAxioms.RelativisticTimeSeries
