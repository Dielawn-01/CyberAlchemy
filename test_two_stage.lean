import Mathlib.Data.Real.Basic
import LaRueProtorealAlgebra.ProtorealManifold
import LaRueProtorealAlgebra.KamaTrain
import LaRueProtorealAlgebra.ProtorealOperator
import InfoPhysAxioms.Infochemistry
import InfoPhysAxioms.CrystalGrowth

open ProtorealManifold
open KamaTrain
open Infochemistry
open CrystalGrowth

noncomputable def crystalline_scaffold : ProtorealManifold :=
  { a := 1, b := 1, m := 1, e := 0, l := 0 }

noncomputable def qc_transition_medium : ProtorealManifold :=
  growth_medium

noncomputable def two_stage_deposition (substrate : ProtorealManifold) : ProtorealManifold :=
  grow_once (bond (grow_once (bond substrate crystalline_scaffold)) qc_transition_medium)

theorem two_stage_deeper_than_single (substrate : ProtorealManifold) :
    (two_stage_deposition substrate).l >
    (grow_once (bond substrate qc_transition_medium)).l := by
  unfold two_stage_deposition grow_once synthetic_integration automatic_differentiation bond
  dsimp [crystalline_scaffold, qc_transition_medium, growth_medium]
  have h1 : max substrate.l 0 ≥ 0 := le_max_right substrate.l 0
  have h2 : max (max substrate.l 0 + 1) 0 = max substrate.l 0 + 1 := max_eq_left (by linarith)
  have h3 : max (max (max substrate.l 0 + 1) 0 + 1 + 1) 0 = max (max substrate.l 0 + 1) 0 + 1 + 1 := max_eq_left (by linarith)
  have h4 : max (max (max (max substrate.l 0 + 1) 0 + 1 + 1) 0 + 1) 0 = max (max (max substrate.l 0 + 1) 0 + 1 + 1) 0 + 1 := max_eq_left (by linarith)
  linarith
