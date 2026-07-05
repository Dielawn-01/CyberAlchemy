import Mathlib.Data.Real.Basic
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.KamaTrain
import InfoPhysAxioms.Infochemistry

open ProtorealManifold
open KamaTrain
open Infochemistry

noncomputable def flow_channel (diameter length : ℝ) : ProtorealManifold :=
  { a := diameter, b := diameter, m := length, e := 0, l := 0 }

noncomputable def splitting_medium (n : ℝ) : ProtorealManifold :=
  { a := 0, b := 0, m := 0, e := n, l := 0 }

theorem murray_split_has_noise (d l : ℝ) (n : ℝ) (hn : n > 0) (hd : d * (1 - l) ≠ 0) :
    (bond (flow_channel d l) (splitting_medium n)).e > 0 := by
  unfold bond flow_channel splitting_medium standard_resonance
  dsimp
  have : d - d * l - (0 - 0 * 0) = d * (1 - l) := by ring
  rw [this]
  exact abs_pos.mpr hd
